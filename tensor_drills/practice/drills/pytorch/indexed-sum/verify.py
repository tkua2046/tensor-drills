import math

import torch


def assert_result(actual, wanted, name, *, factor=0, budgets=None):
    assert isinstance(actual, torch.Tensor), f"{name}: return a PyTorch tensor."
    assert actual.shape == wanted.shape, f"{name}: expected shape {wanted.shape}, got {actual.shape}."
    assert actual.dtype == wanted.dtype, f"{name}: expected dtype {wanted.dtype}, got {actual.dtype}."
    assert actual.device == wanted.device, f"{name}: expected device {wanted.device}, got {actual.device}."
    if budgets is None:
        torch.testing.assert_close(actual, wanted, rtol=0, atol=0, msg=lambda msg: f"{name}: {msg}")
    else:
        for index, (value, target, budget) in enumerate(zip(actual, wanted, budgets)):
            torch.testing.assert_close(value, target, rtol=factor, atol=budget, msg=lambda msg, index=index: f"{name} at destination {index}: {msg}")


def check_case(call, inputs, expected):
    values = torch.tensor(inputs["values"], dtype=getattr(torch, inputs["dtype"]))
    destinations = torch.tensor(inputs["destinations"], dtype=torch.int64)
    original_values, original_destinations = values.clone(), destinations.clone()
    result = call("indexed_sum", values, destinations, inputs["size"])
    wanted = torch.tensor(expected, dtype=original_values.dtype)
    factor, budgets = 0, None
    if original_values.is_floating_point():
        factor = 1e-5 if original_values.dtype == torch.float32 else 1e-12
        magnitudes = [[] for _ in range(inputs["size"])]
        for destination, value in zip(original_destinations.tolist(), original_values.tolist()):
            magnitudes[destination].append(abs(value))
        budgets = [factor * math.fsum(group) for group in magnitudes]
    assert_result(result, wanted, "Destination sums", factor=factor, budgets=budgets)
    assert_result(values, original_values, "Input values changed")
    assert_result(destinations, original_destinations, "Destination indices changed")
