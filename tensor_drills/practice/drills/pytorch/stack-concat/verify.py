import torch


def assert_tensor(actual, wanted, name):
    assert isinstance(actual, torch.Tensor), f"{name}: return a PyTorch tensor."
    torch.testing.assert_close(actual, wanted, rtol=0, atol=0, msg=lambda msg: f"{name}: {msg}")


def check_case(call, inputs, expected):
    first = torch.tensor(inputs["first"], dtype=getattr(torch, inputs["dtype"]))
    second = torch.tensor(inputs["second"], dtype=first.dtype)
    original_first, original_second = first.clone(), second.clone()

    result = call("join_matrices", first, second, inputs["axis"])
    assert isinstance(result, tuple) and len(result) == 2, "Return (stacked, concatenated)."
    for name, actual, data in zip(("stacked", "concatenated"), result, expected):
        wanted = torch.tensor(data, dtype=original_first.dtype)
        assert_tensor(actual, wanted, name)
    assert_tensor(first, original_first, "First input changed")
    assert_tensor(second, original_second, "Second input changed")
