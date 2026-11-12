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
    samples=tensor(inputs["values"],inputs["shape"]);labels=tensor(inputs["labels"],dtype=torch.int64);sx=samples.clone();ly=labels.clone()
    result=call("labeled_batches",samples,labels,inputs["batch_size"])
    assert isinstance(result,list) and len(result)==len(expected),"Return the ordered batch list, including the final partial batch."
    for pair,wanted in zip(result,expected):
        assert isinstance(pair,(tuple,list)) and len(pair)==2,"Return paired sample/label batches."
        same(pair[0],tensor(wanted["values"],(len(wanted["labels"]),inputs["shape"][1])),"Samples")
        same(pair[1],tensor(wanted["labels"],dtype=torch.int64),"Labels")
    same(samples,sx,"Samples changed");same(labels,ly,"Labels changed")
