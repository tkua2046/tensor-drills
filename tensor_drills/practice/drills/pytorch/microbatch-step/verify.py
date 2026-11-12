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



def check_case(call, inputs, expected):
    args = {key: make(value) if isinstance(value, dict) and "shape" in value and "dtype" in value else value for key,value in inputs.items()}
    saved = {key: copy(value) for key,value in args.items() if isinstance(inputs[key],dict) and "shape" in inputs[key] and "dtype" in inputs[key]}
    import copy as copying
    model=torch.nn.Linear(inputs["weight"]["shape"][1],inputs["bias"]["shape"][0],bias=True,dtype=torch.float64)
    with torch.no_grad():
        model.weight.copy_(make(inputs["weight"]));model.bias.copy_(make(inputs["bias"]))
    optimizer=torch.optim.SGD(model.parameters(),lr=.1,momentum=.9,weight_decay=.01)
    def equal_state(left,right):
        assert type(left)==type(right), "Optimizer state type changed."
        if isinstance(left,torch.Tensor): torch.testing.assert_close(left,right,rtol=0,atol=0)
        elif isinstance(left,dict):
            assert left.keys()==right.keys()
            for key in left: equal_state(left[key],right[key])
        elif isinstance(left,(list,tuple)):
            assert len(left)==len(right)
            for a,b in zip(left,right): equal_state(a,b)
        else: assert left==right
    for window,wanted in zip(inputs["windows"],expected):
        batches=[(make(v["features"]),make(v["targets"])) for v in window]
        snapshots=[(x.clone(),y.clone()) for x,y in batches]
        model.eval()
        for parameter in model.parameters(): parameter.grad=torch.full_like(parameter,3.)
        before=copying.deepcopy(optimizer.state_dict());before_params=[p.detach().clone() for p in model.parameters()]
        observations={"forward":0,"backward":0,"step":0,"step_grad":None}
        def forward_hook(module,args,out):
            observations["forward"]+=1
            assert module.training, "Use training mode."
        def backward_hook(gradient): observations["backward"]+=1
        handle=model.register_forward_hook(forward_hook);grad_handle=model.weight.register_hook(backward_hook)
        original_step=optimizer.step
        def step(*a,**kw):
            observations["step"]+=1
            observations["step_grad"]=[p.grad.detach().clone() if p.grad is not None else None for p in model.parameters()]
            return original_step(*a,**kw)
        optimizer.step=step
        try: result=call("microbatch_step",model,optimizer,batches)
        finally:
            optimizer.step=original_step;handle.remove();grad_handle.remove()
        same(result,wanted["loss"],"Pre-update global loss")
        assert not result.requires_grad and result.grad_fn is None and model.training
        for (x,y),(oldx,oldy) in zip(batches,snapshots):
            torch.testing.assert_close(x,oldx,rtol=0,atol=0);torch.testing.assert_close(y,oldy,rtol=0,atol=0)
        same(model.weight,wanted["weight"],"Updated weight");same(model.bias,wanted["bias"],"Updated bias")
        after=optimizer.state_dict()
        equal_state(before["param_groups"],after["param_groups"])
        if not wanted["valid"]:
            assert result.item()==0 and observations["forward"]==observations["backward"]==observations["step"]==0
            equal_state(before,after)
            for parameter,old in zip(model.parameters(),before_params):
                torch.testing.assert_close(parameter,old,rtol=0,atol=0)
                assert parameter.grad is None or bool((parameter.grad==0).all()), "Clear stale gradients even in a zero window."
        else:
            assert observations["step"]==1
            assert observations["forward"]==sum(len(y)>0 for x,y in batches)
            assert observations["backward"]==sum(bool((y!=-100).any()) for x,y in batches)
            for gradient,key in zip(observations["step_grad"],["gradient_weight","gradient_bias"]): same(gradient,wanted[key],"Step-time gradient")
        if wanted["has_state"]:
            assert set(optimizer.state)==set(model.parameters())
            for parameter,key in [(model.weight,"momentum_weight"),(model.bias,"momentum_bias")]:
                assert set(optimizer.state[parameter])=={"momentum_buffer"}
                same(optimizer.state[parameter]["momentum_buffer"],wanted[key],"Momentum state")
        else: assert len(optimizer.state)==0

    unchanged(args,saved)
