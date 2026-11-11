import torch


def assert_tensor(actual, wanted, name):
    assert isinstance(actual, torch.Tensor), f"{name}: return a PyTorch tensor."
    torch.testing.assert_close(actual, wanted, rtol=0, atol=0, msg=lambda msg: f"{name}: {msg}")


def check_case(call, inputs, expected):
    scores = torch.tensor(inputs["scores"], dtype=getattr(torch, inputs["dtype"])).reshape(inputs["shape"])
    columns = torch.tensor(inputs["columns"], dtype=torch.int64)
    original_scores, original_columns = scores.clone(), columns.clone()

    result = call("gather_scores", scores, columns)
    wanted = torch.tensor(expected, dtype=original_scores.dtype)
    assert_tensor(result, wanted, "Gathered scores")
    assert_tensor(scores, original_scores, "Scores changed")
    assert_tensor(columns, original_columns, "Column indices changed")
