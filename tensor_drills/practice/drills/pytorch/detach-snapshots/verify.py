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
    base, source = tracked(inputs); original = source.detach().clone(); history = source.grad_fn
    result = call("detach_snapshots", source)
    assert isinstance(result, tuple) and len(result) == 2, "Return (shared, independent)."
    shared, independent = result
    for value in result:
        same(value, original, "Snapshot")
        assert not value.requires_grad and value.grad_fn is None, "Detach both outputs."
    assert source.requires_grad and source.grad_fn is history, "Source tracking/history changed."
    same(source, original, "Source changed during conversion")
    shared.fill_(17)
    same(source, torch.full_like(original,17), "Shared snapshot does not reach source")
    same(independent, original, "Independent snapshot shares storage")
    independent.fill_(-19)
    same(source, torch.full_like(original,17), "Independent write reaches source")
