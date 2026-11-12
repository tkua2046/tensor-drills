import math

import numpy as np


def make_values(data, shape, dtype, strided=False):
    values = np.array(data, dtype=dtype).reshape(shape)
    if strided and shape[-1]:
        base = np.zeros(tuple(shape[:-1]) + (2 * shape[-1],), dtype=dtype)
        result = base[..., ::2]
        result[...] = values
        return result
    return values


def assert_values(actual, wanted, name, *, factor=0, budgets=None):
    assert isinstance(actual, np.ndarray), f"{name}: return a NumPy array."
    assert actual.shape == wanted.shape, f"{name}: expected shape {wanted.shape}, got {actual.shape}."
    assert actual.dtype == wanted.dtype, f"{name}: expected dtype {wanted.dtype}, got {actual.dtype}."
    if budgets is None:
        np.testing.assert_array_equal(actual, wanted, err_msg=name)
    else:
        for i, (a, b, budget) in enumerate(zip(actual.reshape(-1), wanted.reshape(-1), budgets)):
            np.testing.assert_allclose(a, b, rtol=factor, atol=budget, err_msg=f"{name} at flat position {i}")

def check_case(call, inputs, expected):
    dtype = inputs["dtype"]
    if "base" in inputs:
        base = make_values(inputs["base"], inputs["base_shape"], dtype)
        values = base[..., ::2]
    else:
        base = values = make_values(inputs["values"], inputs["shape"], dtype)
    alias = values
    view = values[..., ::2]
    mask = np.array(inputs["mask"], dtype=np.bool_).reshape(inputs["shape"])
    original_mask = mask.copy()
    result = call("masked_assign", values, mask, inputs["replacement"])
    assert result is None, "Return None after the in-place assignment."
    wanted = np.array(expected["values"], dtype=dtype).reshape(inputs["shape"])
    assert_values(values, wanted, "Assigned values")
    assert_values(alias, wanted, "Existing alias")
    assert_values(view, wanted[..., ::2], "Existing basic-slice view")
    if "base" in expected:
        wanted_base = np.array(expected["base"], dtype=dtype).reshape(inputs["base_shape"])
        assert_values(base, wanted_base, "Source base changed outside selected view entries")
    assert_values(mask, original_mask, "Mask changed")
