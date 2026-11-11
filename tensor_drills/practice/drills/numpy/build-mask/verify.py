import numpy as np


def assert_array(actual, wanted, name):
    assert isinstance(actual, np.ndarray), f"{name}: return a NumPy array."
    assert actual.shape == wanted.shape, f"{name}: expected shape {wanted.shape}, got {actual.shape}."
    assert actual.dtype == wanted.dtype, f"{name}: expected dtype {wanted.dtype}, got {actual.dtype}."
    np.testing.assert_array_equal(actual, wanted, err_msg=name)


def check_case(call, inputs, expected):
    values = np.array(inputs["values"], dtype=inputs["dtype"])
    original = values.copy()

    result = call("build_masks", values, inputs["lower"], inputs["upper"])
    assert isinstance(result, tuple) and len(result) == 2, "Return (inside, outside)."
    for name, actual, data in zip(("inside", "outside"), result, expected):
        wanted = np.array(data, dtype=np.bool_)
        assert_array(actual, wanted, name)
    assert_array(values, original, "Input values changed")
