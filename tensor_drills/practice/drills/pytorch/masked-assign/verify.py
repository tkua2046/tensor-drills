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
    if "base" in inputs:
        base = make_values(inputs["base"], inputs["base_shape"], dtype)
        values = base[..., ::2]
    else:
        base = values = make_values(inputs["values"], inputs["shape"], dtype)
    alias = values
    view = values[..., ::2]
    mask = torch.tensor(inputs["mask"], dtype=torch.bool).reshape(inputs["shape"])
    original_mask = mask.clone()
    result = call("masked_assign", values, mask, inputs["replacement"])
    assert result is None, "Return None after the in-place assignment."
    wanted = torch.tensor(expected["values"], dtype=dtype).reshape(inputs["shape"])
    assert_values(values, wanted, "Assigned values")
    assert_values(alias, wanted, "Existing alias")
    assert_values(view, wanted[..., ::2], "Existing basic-slice view")
    if "base" in expected:
        wanted_base = torch.tensor(expected["base"], dtype=dtype).reshape(inputs["base_shape"])
        assert_values(base, wanted_base, "Source base changed outside selected view entries")
    assert_values(mask, original_mask, "Mask changed")
