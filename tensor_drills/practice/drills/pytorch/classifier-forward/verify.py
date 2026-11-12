import torch
from torch import nn


def tensor(data, shape=None, dtype=torch.float64):
    result = torch.tensor(data, dtype=dtype, device="cpu")
    return result.reshape(shape) if shape is not None else result


def same(actual, wanted, name):
    assert isinstance(actual, torch.Tensor), f"{name}: return a tensor."
    torch.testing.assert_close(actual, wanted, rtol=1e-8, atol=1e-10, msg=lambda m: f"{name}: {m}")


def tracked(inputs):
    base = tensor(inputs["values"]).requires_grad_()
    if inputs.get("strided"):
        base = base.repeat_interleave(2).detach().requires_grad_()
        source = base[::2]
    else:
        source = base * 1.0 if inputs.get("nonleaf") else base
    return base, source


def check_case(call, inputs, expected):
    model = call("Classifier", inputs["D"], inputs["H"], inputs["C"])
    assert isinstance(model, nn.Module), "Return an nn.Module."
    assert isinstance(getattr(model, "hidden", None), nn.Linear) and isinstance(getattr(model, "output", None), nn.Linear), "Register Linear children hidden and output."
    assert set(dict(model.named_parameters())) == {"hidden.weight", "hidden.bias", "output.weight", "output.bias"}, "Register the four expected parameters."
    model.to(dtype=torch.float64)
    for module, weight, bias in [(model.hidden, inputs["hw"], inputs["hb"]), (model.output, inputs["ow"], inputs["ob"])]:
        assert module.weight.dtype == torch.float64 and module.bias.dtype == torch.float64, "Registered parameters must follow dtype conversion."
        assert module.weight.shape == tensor(weight).shape and module.bias.shape == tensor(bias).shape, "Layer dimensions disagree."
        with torch.no_grad():
            module.weight.copy_(tensor(weight)); module.bias.copy_(tensor(bias))
    values = tensor(inputs["values"], inputs["shape"]); original = values.clone()
    try:
        result = model(values)
    except Exception as error:
        raise AssertionError(f"Forward failed: {error}") from error
    same(result, tensor(expected, (inputs["shape"][0], inputs["C"])), "Raw logits")
    same(values, original, "Features changed")
