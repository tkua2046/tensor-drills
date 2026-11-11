import torch
from torch import nn


def check_case(call, inputs, expected):
    def floats(values):
        return torch.tensor(values, dtype=torch.float64, device="cpu")

    parameters = inputs["parameters"]
    weights = floats(parameters["weight"])
    layer = nn.Linear(weights.shape[1], weights.shape[0], dtype=torch.float64, device="cpu")
    with torch.no_grad():
        layer.weight.copy_(weights)
        layer.bias.copy_(floats(parameters["bias"]))
    dropout = nn.Dropout(inputs["dropout"])
    model = nn.Sequential(dropout, layer)
    optimizer = torch.optim.SGD(model.parameters(), lr=inputs["learning_rate"])
    torch.manual_seed(inputs["seed"])

    forwards, updates = [], []

    def record_forward(module, _args):
        forwards.append([module.training, dropout.training, torch.is_grad_enabled()])

    def record_update(_optimizer, _args, _kwargs):
        updates.append((layer.weight.detach().clone(), layer.bias.detach().clone()))

    model.register_forward_pre_hook(record_forward)
    optimizer.register_step_post_hook(record_update)

    def batch(data):
        return floats(data["features"]), torch.tensor(data["labels"], dtype=torch.long, device="cpu")

    predictions = call(
        "train_with_validation",
        model,
        optimizer,
        [batch(data) for data in inputs["training_batches"]],
        floats(inputs["validation_features"]),
    )
    assert isinstance(predictions, (list, tuple)), "Return a list or tuple of validation logits."

    assert len(updates) == len(expected["updates"]), "Unexpected number of optimizer updates."
    for index, ((weight, bias), wanted) in enumerate(zip(updates, expected["updates"]), 1):
        assert_parameters(weight, bias, wanted, f"Update {index}", floats)
    assert_parameters(layer.weight, layer.bias, expected["parameters"], "Final parameters", floats)
    assert forwards == expected["forward_states"], "A forward pass ran in the wrong mode."
    assert len(predictions) == len(expected["logits"]), "Unexpected number of validation results."
    for actual, wanted in zip(predictions, expected["logits"]):
        assert isinstance(actual, torch.Tensor), "Return logits as a tensor."
        assert not actual.requires_grad, "Evaluation logits should have gradient recording disabled."
        torch.testing.assert_close(actual, floats(wanted), atol=1e-10, rtol=1e-8)


def assert_parameters(weight, bias, expected, label, floats):
    for name, actual in (("weight", weight), ("bias", bias)):
        torch.testing.assert_close(
            actual,
            floats(expected[name]),
            atol=1e-10,
            rtol=1e-8,
            msg=lambda details: f"{label} ({name})\n{details}",
        )
