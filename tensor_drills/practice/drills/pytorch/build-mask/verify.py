import torch


def assert_tensor(actual, wanted, name):
    assert isinstance(actual, torch.Tensor), f"{name}: return a PyTorch tensor."
    torch.testing.assert_close(actual, wanted, rtol=0, atol=0, msg=lambda msg: f"{name}: {msg}")


def check_case(call, inputs, expected):
    values = torch.tensor(inputs["values"], dtype=getattr(torch, inputs["dtype"]))
    original = values.clone()

    result = call("build_masks", values, inputs["lower"], inputs["upper"])
    assert isinstance(result, tuple) and len(result) == 2, "Return (inside, outside)."
    for name, actual, data in zip(("inside", "outside"), result, expected):
        wanted = torch.tensor(data, dtype=torch.bool)
        assert_tensor(actual, wanted, name)
    assert_tensor(values, original, "Input values changed")
