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
    dtype=getattr(torch,inputs["dtype"]);values=tensor(inputs["values"],inputs["shape"],dtype);original=values.clone()
    result=call("row_softmax",values);wanted=tensor(expected,inputs["shape"],dtype)
    assert isinstance(result,torch.Tensor) and result.shape==wanted.shape and result.dtype==wanted.dtype and result.device==wanted.device,"Preserve tensor shape/dtype/device."
    assert torch.isfinite(result).all(),"Return finite probabilities."
    floor=2*torch.nextafter(torch.tensor(0,dtype=dtype),torch.tensor(1,dtype=dtype)).item()
    torch.testing.assert_close(result,wanted,rtol=1e-5 if dtype==torch.float32 else 1e-12,atol=floor)
    same(values,original,"Input changed")
