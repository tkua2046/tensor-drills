import numpy as np


def assert_array(actual, wanted, name, *, rtol=0, atol=0):
    assert isinstance(actual, np.ndarray), f"{name}: return a NumPy array."
    assert actual.shape == wanted.shape, f"{name}: expected shape {wanted.shape}, got {actual.shape}."
    assert actual.dtype == wanted.dtype, f"{name}: expected dtype {wanted.dtype}, got {actual.dtype}."
    np.testing.assert_allclose(actual, wanted, rtol=rtol, atol=atol, err_msg=name)


def check_case(call, inputs, expected):
    values = np.array(inputs["values"], dtype=inputs["dtype"])
    original = values.copy()

    result = call("reduce_and_center", values)
    assert isinstance(result, tuple) and len(result) == 3, "Return (totals, means, centered)."
    for name, actual, data in zip(("totals", "means", "centered"), result, expected):
        wanted = np.array(data, dtype=original.dtype)
        assert_array(actual, wanted, name, rtol=1e-6, atol=1e-6)
    assert_array(values, original, "Input values changed")
