import torch

def make(spec):
    result = torch.tensor(spec["data"], dtype=getattr(torch, spec["dtype"]), device="cpu").reshape(spec["shape"])
    if spec.get("layout") == "strided" and result.shape[-1]:
        shape = tuple(result.shape[:-1]) + (2 * result.shape[-1] + 2,)
        backing = torch.zeros(shape, dtype=result.dtype)
        view = backing[..., 1:1 + 2 * result.shape[-1]:2]
        view.copy_(result)
        return view
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
    torch.testing.assert_close(actual, wanted, rtol=1e-12 if wanted.is_floating_point() else 0,
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


def check_case(call, inputs, expected):
    args = {key: make(value) if isinstance(value,dict) and "data" in value else value for key,value in inputs.items()}
    saved = {key: copy(value) for key,value in args.items() if isinstance(inputs[key],dict) and "data" in inputs[key]}
    first, second = pair(call("boolean_select", args["x"], args["elements"], args["rows"]))
    same(first, expected[0], "Selected elements")
    same(second, expected[1], "Selected rows")
    unchanged(args, saved)
