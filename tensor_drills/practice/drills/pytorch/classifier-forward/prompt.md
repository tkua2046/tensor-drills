# Build and register a two-layer classifier

PyTorch · Atomic create

**Goal.** Build a registered two-layer classifier that returns raw logits.

Implement `Classifier(in_features, hidden_features, classes)` in [attempt.py](attempt.py).

- Implement `Classifier` as an `nn.Module`. Register exactly two biased `nn.Linear` children named `hidden` and `output`, with dimensions `in_features -> hidden_features -> classes`, all positive.
- Forward accepts CPU features `(N,in_features)`, including `N=0`, applies the hidden layer, ReLU, then the output layer, and returns raw logits `(N,classes)`.
- The model must support ordinary `.to(dtype=torch.float64)` conversion of its registered parameters. The checker injects known weights and biases. Leave feature inputs unchanged.

Negative final logits are valid; the output is not a probability distribution.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/classifier-forward
```

The untouched starter reports an unimplemented operation. For review, save your code and check output. Explain the actual tensor/module operations, state changes and evidence that meet the contract.
