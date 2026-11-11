import numpy as np


def assert_array(actual, wanted, name):
    assert isinstance(actual, np.ndarray), f"{name}: return a NumPy array."
    assert actual.shape == wanted.shape, f"{name}: expected shape {wanted.shape}, got {actual.shape}."
    assert actual.dtype == wanted.dtype, f"{name}: expected dtype {wanted.dtype}, got {actual.dtype}."
    np.testing.assert_array_equal(actual, wanted, err_msg=name)


def check_case(call, inputs, expected):
    matrix = np.array(inputs["matrix"], dtype=inputs["dtype"])
    rows = np.array(inputs["rows"], dtype=np.intp)
    columns = np.array(inputs["columns"], dtype=np.intp)
    original_matrix, original_rows, original_columns = matrix.copy(), rows.copy(), columns.copy()

    result = call("select_entries", matrix, rows, columns)
    assert isinstance(result, tuple) and len(result) == 2, "Return (paired, grid)."
    for name, actual, data in zip(("paired", "grid"), result, expected):
        wanted = np.array(data, dtype=original_matrix.dtype)
        assert_array(actual, wanted, name)
    assert_array(matrix, original_matrix, "Matrix changed")
    assert_array(rows, original_rows, "Row indices changed")
    assert_array(columns, original_columns, "Column indices changed")
