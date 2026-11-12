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
    x = tensor(inputs["values"]).requires_grad_(); original = x.detach().clone()
    outputs = call("gradient_sequence", x)
    assert isinstance(outputs, tuple) and len(outputs) == 3, "Return three gradient snapshots."
    for value, key in zip(outputs, ["first", "accumulated", "cleared"]):
        same(value, tensor(expected[key]), key)
        assert not value.requires_grad and value.grad_fn is None, "Detach gradient snapshots."
    assert x.is_leaf and x.requires_grad and x.grad is not None, "Preserve the trainable leaf and final gradient."
    same(x.grad, tensor(expected["cleared"]), "Final gradient")
    same(x, original, "Leaf data changed")
    held = [value.clone() for value in outputs]
    outputs[0].fill_(99)
    same(outputs[1], held[1], "Snapshots share storage"); same(outputs[2], held[2], "Snapshots share storage")
    same(x.grad, tensor(expected["cleared"]), "Snapshot aliases final gradient")
    x.grad.zero_()
    same(outputs[2], held[2], "Final snapshot aliases gradient buffer")
