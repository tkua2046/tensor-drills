import numpy as np


def check_case(call, inputs, expected):
    scores = np.array(inputs["scores"], dtype=inputs["dtype"]).reshape(inputs["shape"])
    columns = np.array(inputs["columns"], dtype=np.intp)
    original_scores, original_columns = scores.copy(), columns.copy()
    wanted = np.array(expected, dtype=scores.dtype)

    result = call("gather_scores", scores, columns)
    assert isinstance(result, np.ndarray), "Return a NumPy array."
    assert result.shape == wanted.shape, f"Expected shape {wanted.shape}, got {result.shape}."
    assert result.dtype == wanted.dtype, f"Expected dtype {wanted.dtype}, got {result.dtype}."
    np.testing.assert_array_equal(result, wanted)
    np.testing.assert_array_equal(scores, original_scores, err_msg="Scores changed.")
    np.testing.assert_array_equal(columns, original_columns, err_msg="Column indices changed.")
