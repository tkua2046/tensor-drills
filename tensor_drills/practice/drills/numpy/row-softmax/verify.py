import numpy as np


def check_case(call, inputs, expected):
    values = np.array(inputs["values"], dtype=inputs["dtype"]).reshape(inputs["shape"])
    original = values.copy()
    with np.errstate(over="raise", invalid="raise", divide="raise", under="ignore"):
        result = call("row_softmax", values)
    wanted = np.array(expected, dtype=values.dtype).reshape(values.shape)
    assert isinstance(result, np.ndarray), "Return a NumPy array."
    assert result.shape == wanted.shape, "Preserve both row and column dimensions."
    assert result.dtype == wanted.dtype, "Preserve the input dtype."
    assert np.isfinite(result).all(), "Probabilities must be finite."
    factor = 1e-5 if wanted.dtype == np.float32 else 1e-12
    floor = 2 * float(np.finfo(values.dtype).smallest_subnormal)
    np.testing.assert_allclose(result, wanted, rtol=factor, atol=floor)
    np.testing.assert_array_equal(values, original, err_msg="Input changed")
