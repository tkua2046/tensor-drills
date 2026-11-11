import torch


def assert_tensor(actual, wanted, name, *, rtol=0, atol=0):
    assert isinstance(actual, torch.Tensor), f"{name}: return a PyTorch tensor."
    torch.testing.assert_close(actual, wanted, rtol=rtol, atol=atol, msg=lambda msg: f"{name}: {msg}")


def check_case(call, inputs, expected):
    values = torch.tensor(inputs["values"], dtype=getattr(torch, inputs["dtype"]))
    original = values.clone()

    result = call("reduce_and_center", values)
    assert isinstance(result, tuple) and len(result) == 3, "Return (totals, means, centered)."
    for name, actual, data in zip(("totals", "means", "centered"), result, expected):
        wanted = torch.tensor(data, dtype=original.dtype)
        assert_tensor(actual, wanted, name, rtol=1e-6, atol=1e-6)
    assert_tensor(values, original, "Input values changed")
