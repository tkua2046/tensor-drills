import torch

def make(spec):
    result = torch.full(spec["shape"], spec["fill"], dtype=getattr(torch,spec["dtype"])) if "fill" in spec else torch.tensor(spec["data"], dtype=getattr(torch, spec["dtype"]), device="cpu").reshape(spec["shape"])
    if spec.get("layout") == "strided" and result.shape[-1]:
        shape = tuple(result.shape[:-1]) + (2 * result.shape[-1] + 2,)
        backing = torch.zeros(shape, dtype=result.dtype)
        view = backing[..., 1:1 + 2 * result.shape[-1]:2]
        view.copy_(result)
        return view
    if spec.get("layout") == "heads":
        return result.transpose(1,2).contiguous().transpose(1,2)
    if spec.get("layout") == "transpose" and result.ndim >= 2:
        return result.transpose(0, 1).contiguous().transpose(0, 1)
    return result

def same(actual, spec, label, index=False):
    assert isinstance(actual, torch.Tensor), f"{label}: return a tensor."
    wanted = make(spec)
    assert actual.device.type == "cpu", f"{label}: keep results on CPU."
    assert actual.shape == wanted.shape, f"{label}: expected shape {wanted.shape}, got {actual.shape}."
    if index:
        assert actual.dtype in (torch.int8, torch.uint8, torch.int16, torch.int32, torch.int64), f"{label}: use integer indices."
        actual = actual.to(wanted.dtype)
    else:
        assert actual.dtype == wanted.dtype, f"{label}: preserve the required dtype."
    torch.testing.assert_close(actual, wanted, rtol=1e-10 if wanted.is_floating_point() else 0,
                               atol=1e-10 if wanted.is_floating_point() else 0, equal_nan=False,
                               msg=lambda message: f"{label}: {message}")

def copy(value):
    return value.clone()

def unchanged(args, saved):
    for key, original in saved.items():
        torch.testing.assert_close(args[key], original, rtol=0, atol=0, msg=lambda message: f"Input {key} changed: {message}")

def pair(value):
    assert isinstance(value, (tuple, list)) and len(value) == 2, "Return the two requested results."
    return value


def items(value, count):
    assert isinstance(value, (tuple, list)) and len(value) == count, f"Return {count} requested outputs."
    return value

from torch import nn

def backward(result, upstream=None):
    assert result.requires_grad and result.grad_fn is not None, "Return a result connected to its supplied trainable input."
    try:
        result.backward(upstream)
    except Exception as error:
        raise AssertionError(f"Backward failed: {error}") from error

def leaf(args, key):
    args[key] = args[key].detach().requires_grad_()
    return args[key]

def tracked_unchanged(value):
    assert value.is_leaf and value.requires_grad and value.grad is None, "Preserve the supplied leaf and its empty gradient buffer during the call."


def check_case(call, inputs, expected):
    args = {key: make(value) if isinstance(value, dict) and "shape" in value and "dtype" in value else value for key,value in inputs.items()}
    saved = {key: copy(value) for key,value in args.items() if isinstance(inputs[key],dict) and "shape" in inputs[key] and "dtype" in inputs[key]}
    model=call("RegisteredAffine",args["features"])
    assert isinstance(model,nn.Module), "Construct an nn.Module."
    assert set(dict(model.named_parameters()))=={"scale"}, "Register only scale as a parameter."
    assert set(dict(model.named_buffers()))=={"center","scratch"}, "Register both buffers."
    assert set(model.state_dict())=={"scale","center"}, "Scratch must be nonpersistent."
    same(model.scale,dict(shape=[args["features"]],dtype="float64",fill=1.,layout="contiguous"),"Initial scale")
    for name in ["center","scratch"]:
        value=getattr(model,name)
        same(value,dict(shape=[args["features"]],dtype="float64",data=[0.]*args["features"],layout="contiguous"),"Initial buffer")
        assert not value.requires_grad, "Buffers must be nontrainable."
    with torch.no_grad():
        model.scale.copy_(args["scale"])
        model.center.copy_(args["center"])
        model.scratch.fill_(5.)
    before_buffers={name:value.clone() for name,value in model.named_buffers()}
    try: result=model(args["x"])
    except Exception as error: raise AssertionError(f"Forward failed: {error}") from error
    same(result,expected["values"],"Affine values")
    for name,value in model.named_buffers():
        torch.testing.assert_close(value,before_buffers[name],rtol=0,atol=0,msg=lambda message: f"Forward changed buffer {name}: {message}")
    backward(result,args["upstream"])
    same(model.scale.grad,expected["gradient"],"Scale gradients")
    for name,value in model.named_buffers():
        torch.testing.assert_close(value,before_buffers[name],rtol=0,atol=0,msg=lambda message: f"Backward changed buffer {name}: {message}")
    assert model.center.grad is None and model.scratch.grad is None, "Only scale is trainable."
    for dtype in [torch.float32,torch.float64]:
        model.to(dtype=dtype)
        assert all(v.dtype==dtype for v in list(model.parameters())+list(model.buffers())), "Convert all registered state."
    device=torch.device("cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu")
    print(f"State conversion device exercised: {device}")
    model.to(device=device,dtype=torch.float32)
    assert all(v.device.type==device.type for v in list(model.parameters())+list(model.buffers())), "Move all registered state."
    model.to(device="cpu")
    model.to(dtype=torch.float64)
    fresh=call("RegisteredAffine",args["features"])
    with torch.no_grad():
        fresh.scale.fill_(9.)
        fresh.center.fill_(7.)
        fresh.scratch.fill_(11.)
    try: fresh.load_state_dict(model.state_dict())
    except Exception as error: raise AssertionError(f"State loading failed: {error}") from error
    same(fresh.scale,inputs["scale"],"Restored scale")
    same(fresh.center,inputs["center"],"Restored center")
    assert bool((fresh.scratch==11).all()), "Nonpersistent destination state must remain unchanged."

    unchanged(args,saved)
