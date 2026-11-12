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
    weights = np.array(inputs["weights"], dtype=dtype).reshape(inputs["weight_shape"])
    original_weights = weights.copy()
    result = call("shared_weight_matmul", values, weights)
    output_shape = (inputs["shape"][0], inputs["shape"][1], inputs["weight_shape"][1])
    wanted = np.array(expected, dtype=dtype).reshape(output_shape)
    factor = 1e-5 if dtype == np.dtype("float32") else 1e-12
    underflow_budget = inputs["shape"][2] * float(np.finfo(dtype).smallest_subnormal)
    x, w = original.tolist(), original_weights.tolist()
    budgets = [underflow_budget + factor * math.fsum(abs(v * w[i][o]) for i, v in enumerate(row))
               for batch in x for row in batch for o in range(inputs["weight_shape"][1])]
    assert_values(result, wanted, "Shared-weight product", factor=factor, budgets=budgets)
    assert_values(weights, original_weights, "Weights changed")
    assert_values(values, original, "Input changed")
