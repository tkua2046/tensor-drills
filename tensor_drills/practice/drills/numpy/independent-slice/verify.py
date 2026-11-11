import numpy as np


def assert_result(actual, wanted, name, *, tolerance=0):
    assert isinstance(actual, np.ndarray), f"{name}: return a NumPy array."
    assert actual.shape == wanted.shape, f"{name}: expected shape {wanted.shape}, got {actual.shape}."
    assert actual.dtype == wanted.dtype, f"{name}: expected dtype {wanted.dtype}, got {actual.dtype}."
    if tolerance and wanted.dtype.kind == "f":
        np.testing.assert_allclose(actual, wanted, rtol=tolerance, atol=tolerance, err_msg=name)
    else:
        np.testing.assert_array_equal(actual, wanted, err_msg=name)


def check_case(call, inputs, expected):
    values = np.array(inputs["values"], dtype=inputs["dtype"])
    original = values.copy()
    result = call("edit_slice", values, inputs["start"], inputs["stop"], inputs["step"], inputs["increment"])
    assert_result(result, np.array(expected, dtype=original.dtype), "Edited slice", tolerance=1e-6)
    assert_result(values, original, "Source changed during the edit")
    if result.size:
        try:
            result[...] = -999
        except Exception as error:
            raise AssertionError("The returned slice must be writable.") from error
        assert_result(values, original, "Source changed when the result was mutated")
        held = result.copy()
        values[...] = 777
        assert_result(result, held, "Result changed when the source was mutated")
