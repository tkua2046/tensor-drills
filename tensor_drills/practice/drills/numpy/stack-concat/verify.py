import numpy as np


def assert_array(actual, wanted, name):
    assert isinstance(actual, np.ndarray), f"{name}: return a NumPy array."
    assert actual.shape == wanted.shape, f"{name}: expected shape {wanted.shape}, got {actual.shape}."
    assert actual.dtype == wanted.dtype, f"{name}: expected dtype {wanted.dtype}, got {actual.dtype}."
    np.testing.assert_array_equal(actual, wanted, err_msg=name)


def check_case(call, inputs, expected):
    first = np.array(inputs["first"], dtype=inputs["dtype"])
    second = np.array(inputs["second"], dtype=first.dtype)
    original_first, original_second = first.copy(), second.copy()

    result = call("join_matrices", first, second, inputs["axis"])
    assert isinstance(result, tuple) and len(result) == 2, "Return (stacked, concatenated)."
    for name, actual, data in zip(("stacked", "concatenated"), result, expected):
        wanted = np.array(data, dtype=original_first.dtype)
        assert_array(actual, wanted, name)
    assert_array(first, original_first, "First input changed")
    assert_array(second, original_second, "Second input changed")
