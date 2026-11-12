import math

import torch


def make_values(data, shape, dtype, strided=False):
    values = torch.tensor(data, dtype=dtype).reshape(shape)
    if strided and shape[-1]:
        base = torch.zeros(tuple(shape[:-1]) + (2 * shape[-1],), dtype=dtype)
        result = base[..., ::2]
        result.copy_(values)
        return result
    return values


def assert_values(actual, wanted, name, *, factor=0, budgets=None):
    assert isinstance(actual, torch.Tensor), f"{name}: return a PyTorch tensor."
    assert actual.shape == wanted.shape, f"{name}: expected shape {wanted.shape}, got {actual.shape}."
    assert actual.dtype == wanted.dtype, f"{name}: expected dtype {wanted.dtype}, got {actual.dtype}."
    assert actual.device == wanted.device, f"{name}: expected device {wanted.device}, got {actual.device}."
    if budgets is None:
        torch.testing.assert_close(actual, wanted, rtol=0, atol=0, msg=lambda msg: f"{name}: {msg}")
    else:
        for i, (a, b, budget) in enumerate(zip(actual.reshape(-1), wanted.reshape(-1), budgets)):
            torch.testing.assert_close(a, b, rtol=factor, atol=budget, msg=lambda msg, i=i: f"{name} at flat position {i}: {msg}")

def check_case(call, inputs, expected):
    dtype = getattr(torch, inputs["dtype"])
    values = make_values(inputs["values"], inputs["shape"], dtype, inputs.get("strided", False))
    original = values.clone()
    target = getattr(torch, inputs["target_dtype"])
    result = call("convert_dtype", values, target)
    wanted = torch.tensor(expected, dtype=target).reshape(inputs["shape"])
    assert_values(result, wanted, "Converted values")
    assert_values(values, original, "Input changed")
