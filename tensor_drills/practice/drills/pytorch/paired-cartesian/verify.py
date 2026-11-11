import torch


def assert_tensor(actual, wanted, name):
    assert isinstance(actual, torch.Tensor), f"{name}: return a PyTorch tensor."
    torch.testing.assert_close(actual, wanted, rtol=0, atol=0, msg=lambda msg: f"{name}: {msg}")


def check_case(call, inputs, expected):
    matrix = torch.tensor(inputs["matrix"], dtype=getattr(torch, inputs["dtype"]))
    rows = torch.tensor(inputs["rows"], dtype=torch.int64)
    columns = torch.tensor(inputs["columns"], dtype=torch.int64)
    original_matrix, original_rows, original_columns = matrix.clone(), rows.clone(), columns.clone()

    result = call("select_entries", matrix, rows, columns)
    assert isinstance(result, tuple) and len(result) == 2, "Return (paired, grid)."
    for name, actual, data in zip(("paired", "grid"), result, expected):
        wanted = torch.tensor(data, dtype=original_matrix.dtype)
        assert_tensor(actual, wanted, name)
    assert_tensor(matrix, original_matrix, "Matrix changed")
    assert_tensor(rows, original_rows, "Row indices changed")
    assert_tensor(columns, original_columns, "Column indices changed")
