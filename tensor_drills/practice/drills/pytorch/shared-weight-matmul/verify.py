import math

import torch


def make_values(data, shape, dtype, strided=False):
    values = torch.tensor(data, dtype=dtype).reshape(shape)
    if strided and shape[-1]:
        base = torch.zeros(tuple(shape[:-1]) + (2 * shape[-1],), dtype=dtype)
        result = base[..., ::2]
        result.copy_(values)
        return result
    return values


def assert_values(actual, wanted, name, *, factor=0, budgets=None):
    assert isinstance(actual, torch.Tensor), f"{name}: return a PyTorch tensor."
    assert actual.shape == wanted.shape, f"{name}: expected shape {wanted.shape}, got {actual.shape}."
    assert actual.dtype == wanted.dtype, f"{name}: expected dtype {wanted.dtype}, got {actual.dtype}."
    assert actual.device == wanted.device, f"{name}: expected device {wanted.device}, got {actual.device}."
    if budgets is None:
        torch.testing.assert_close(actual, wanted, rtol=0, atol=0, msg=lambda msg: f"{name}: {msg}")
    else:
        for i, (a, b, budget) in enumerate(zip(actual.reshape(-1), wanted.reshape(-1), budgets)):
            torch.testing.assert_close(a, b, rtol=factor, atol=budget, msg=lambda msg, i=i: f"{name} at flat position {i}: {msg}")

def check_case(call, inputs, expected):
    dtype = getattr(torch, inputs["dtype"])
    values = make_values(inputs["values"], inputs["shape"], dtype, inputs.get("strided", False))
    original = values.clone()
    weights = torch.tensor(inputs["weights"], dtype=dtype).reshape(inputs["weight_shape"])
    original_weights = weights.clone()
    result = call("shared_weight_matmul", values, weights)
    output_shape = (inputs["shape"][0], inputs["shape"][1], inputs["weight_shape"][1])
    wanted = torch.tensor(expected, dtype=dtype).reshape(output_shape)
    factor = 1e-5 if dtype == torch.float32 else 1e-12
    underflow_budget = inputs["shape"][2] * torch.nextafter(torch.tensor(0, dtype=dtype), torch.tensor(1, dtype=dtype)).item()
    x, w = original.tolist(), original_weights.tolist()
    budgets = [underflow_budget + factor * math.fsum(abs(v * w[i][o]) for i, v in enumerate(row))
               for batch in x for row in batch for o in range(inputs["weight_shape"][1])]
    assert_values(result, wanted, "Shared-weight product", factor=factor, budgets=budgets)
    assert_values(weights, original_weights, "Weights changed")
    assert_values(values, original, "Input changed")
