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
    values = tensor(inputs["values"]); original = values.clone()
    result = call("scalar_gradient", values)
    assert isinstance(result, tuple) and len(result) == 2, "Return (x, loss)."
    x, loss = result
    same(x, original, "Leaf values")
    assert x.is_leaf and x.requires_grad and x.grad_fn is None, "Return an independent trainable leaf."
    assert isinstance(loss, torch.Tensor) and loss.shape == () and loss.requires_grad and loss.grad_fn is not None, "Return the actual scalar loss with history."
    same(loss, tensor(expected["loss"]), "Loss")
    assert x.grad is not None, "backward() must populate the leaf gradient."
    same(x.grad, tensor(expected["grad"]), "Leaf gradient")
    assert not values.requires_grad, "Do not enable gradients on the caller's input."
    same(values, original, "Input changed")
    with torch.no_grad(): x.fill_(99)
    same(values, original, "Leaf shares input storage")
