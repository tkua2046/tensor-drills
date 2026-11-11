import torch


def assert_tensor(actual, wanted, name, *, tolerance=0):
    assert isinstance(actual, torch.Tensor), f"{name}: return a PyTorch tensor."
    torch.testing.assert_close(actual, wanted, rtol=tolerance, atol=tolerance, msg=lambda msg: f"{name}: {msg}")


def check_case(call, inputs, expected):
    dtype = getattr(torch, inputs["dtype"])
    values = torch.tensor(inputs["values"], dtype=dtype)
    offsets = torch.tensor(inputs["offsets"], dtype=dtype)
    original_values, original_offsets = values.clone(), offsets.clone()
    result = call("add_sequence_offsets", values, offsets)
    assert_tensor(result, torch.tensor(expected, dtype=dtype), "Offset values", tolerance=1e-6)
    assert_tensor(values, original_values, "Input values changed")
    assert_tensor(offsets, original_offsets, "Offsets changed")
