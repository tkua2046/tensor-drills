import torch
from torch import nn


def tensor(data, shape=None, dtype=torch.float64):
    result = torch.tensor(data, dtype=dtype, device="cpu")
    return result.reshape(shape) if shape is not None else result


def same(actual, wanted, name):
    assert isinstance(actual, torch.Tensor), f"{name}: return a tensor."
    torch.testing.assert_close(actual, wanted, rtol=1e-8, atol=1e-10, msg=lambda m: f"{name}: {m}")


def tracked(inputs):
    base = tensor(inputs["values"]).requires_grad_()
    if inputs.get("strided"):
        base = base.repeat_interleave(2).detach().requires_grad_()
        source = base[::2]
    else:
        source = base * 1.0 if inputs.get("nonleaf") else base
    return base, source


def check_case(call, inputs, expected):
    model = nn.Sequential(nn.Dropout(1.0),nn.Linear(2,2,dtype=torch.float64))
    with torch.no_grad():
        model[1].weight.copy_(tensor([[1,-1],[.5,1]])); model[1].bias.copy_(tensor([.25,-.5]))
    model.train(inputs["training"]); saved = {k:v.clone() for k,v in model.state_dict().items()}
    features = tensor([[1,2],[-1,1]]).requires_grad_(); original=features.detach().clone(); states=[]
    model.register_forward_pre_hook(lambda m,a: states.append([m.training,m[0].training,torch.is_grad_enabled()]))
    with torch.set_grad_enabled(inputs["recording"]):
        try:
            result = call("mode_and_recording", model, features)
            restored = torch.is_grad_enabled()
        finally:
            torch.set_grad_enabled(inputs["recording"])
        assert restored == inputs["recording"], "Restore ambient recording state."
    assert isinstance(result,tuple) and len(result)==3, "Return the three outputs."
    assert states==[[False,False,True],[True,True,False],[False,False,False]], "Forward mode/recording controls disagree."
    assert all(m.training==inputs["training"] for m in model.modules()), "Restore incoming model mode."
    for output,data in zip(result,[expected["eval"],expected["train"],expected["eval"]]):same(output,tensor(data),"Forward values")
    assert result[0].requires_grad and result[0].grad_fn is not None, "First forward must retain history."
    assert not result[1].requires_grad and not result[2].requires_grad, "Disable recording for later forwards."
    same(features,original,"Features changed")
    for k,v in model.state_dict().items():same(v,saved[k],"Parameters changed")
