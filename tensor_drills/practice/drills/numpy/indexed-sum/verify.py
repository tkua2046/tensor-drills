import math

import numpy as np


def assert_result(actual, wanted, name, *, factor=0, budgets=None):
    assert isinstance(actual, np.ndarray), f"{name}: return a NumPy array."
    assert actual.shape == wanted.shape, f"{name}: expected shape {wanted.shape}, got {actual.shape}."
    assert actual.dtype == wanted.dtype, f"{name}: expected dtype {wanted.dtype}, got {actual.dtype}."
    if budgets is None:
        np.testing.assert_array_equal(actual, wanted, err_msg=name)
    else:
        for index, (value, target, budget) in enumerate(zip(actual, wanted, budgets)):
            np.testing.assert_allclose(value, target, rtol=factor, atol=budget, err_msg=f"{name} at destination {index}")


def check_case(call, inputs, expected):
    values = np.array(inputs["values"], dtype=inputs["dtype"])
    destinations = np.array(inputs["destinations"], dtype=np.int64)
    original_values, original_destinations = values.copy(), destinations.copy()
    result = call("indexed_sum", values, destinations, inputs["size"])
    wanted = np.array(expected, dtype=original_values.dtype)
    factor, budgets = 0, None
    if original_values.dtype.kind == "f":
        factor = 1e-5 if original_values.dtype == np.float32 else 1e-12
        magnitudes = [[] for _ in range(inputs["size"])]
        for destination, value in zip(original_destinations.tolist(), original_values.tolist()):
            magnitudes[destination].append(abs(value))
        budgets = [factor * math.fsum(group) for group in magnitudes]
    assert_result(result, wanted, "Destination sums", factor=factor, budgets=budgets)
    assert_result(values, original_values, "Input values changed")
    assert_result(destinations, original_destinations, "Destination indices changed")
