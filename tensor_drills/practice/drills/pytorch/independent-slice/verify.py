import torch


def assert_result(actual, wanted, name, *, tolerance=0):
    assert isinstance(actual, torch.Tensor), f"{name}: return a PyTorch tensor."
    tolerance = tolerance if wanted.is_floating_point() else 0
    torch.testing.assert_close(actual, wanted, rtol=tolerance, atol=tolerance, msg=lambda msg: f"{name}: {msg}")


def check_case(call, inputs, expected):
    values = torch.tensor(inputs["values"], dtype=getattr(torch, inputs["dtype"]))
    original = values.clone()
    result = call("edit_slice", values, inputs["start"], inputs["stop"], inputs["step"], inputs["increment"])
    assert_result(result, torch.tensor(expected, dtype=original.dtype), "Edited slice", tolerance=1e-6)
    assert_result(values, original, "Source changed during the edit")
    if result.numel():
        try:
            with torch.no_grad():
                result.fill_(-999)
        except Exception as error:
            raise AssertionError("The returned slice must be writable.") from error
        assert_result(values, original, "Source changed when the result was mutated")
        held = result.clone()
        with torch.no_grad():
            values.fill_(777)
        assert_result(result, held, "Result changed when the source was mutated")
