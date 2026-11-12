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
    values = make_values(inputs["values"], inputs["shape"], dtype, inputs.get("strided", False))
    original = values.copy()
    result = call("replace_negatives", values)
    wanted = np.array(expected, dtype=dtype).reshape(inputs["shape"])
    assert_values(result, wanted, "Replaced values")
    assert_values(values, original, "Source changed during replacement")
    try:
        result[...] = -777
    except Exception as error:
        raise AssertionError("Return a writable independent result.") from error
    assert_values(values, original, "Source changed through result")
    held = result.copy()
    values[...] = 333
    assert_values(result, held, "Result changed through source")
