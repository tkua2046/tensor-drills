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
    base, source = tracked(inputs); source.retain_grad(); original = source.detach().clone(); history = source.grad_fn
    fork = call("trainable_fork", source)
    same(fork, original, "Fork values")
    assert fork.is_leaf and fork.requires_grad and fork.grad_fn is None, "Create a trainable leaf without inherited history."
    assert source.requires_grad and source.grad_fn is history, "Source tracking/history changed."
    (fork.square().sum()).backward()
    same(fork.grad, 2*original, "Fork gradient")
    assert base.grad is None and source.grad is None, "Fork backward reached source history."
    same(source, original, "Source changed")
    with torch.no_grad(): fork.fill_(31)
    same(source, original, "Fork shares source storage")
