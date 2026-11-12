import numpy as np


def check_case(call, inputs, expected):
    values = np.array(inputs["values"], dtype=np.int32)
    original = values.copy()
    result = call("safe_integer_sum", values)
    assert isinstance(result, np.int64), "Return a numpy.int64 scalar."
    assert int(result) == expected, f"Expected exact total {expected}, got {result}."
    np.testing.assert_array_equal(values, original, err_msg="Input changed")
