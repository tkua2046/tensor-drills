import numpy as np


def check_case(call, inputs, expected):
    values = np.array(inputs["values"], dtype=np.float32)
    original = values.copy()
    result = call("precise_sum", values)
    assert isinstance(result, np.float64), "Return a numpy.float64 scalar."
    assert result == np.float64(expected), f"Expected exact total {expected}, got {result}."
    np.testing.assert_array_equal(values, original, err_msg="Input changed")
