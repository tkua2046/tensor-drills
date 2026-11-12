# Save state and restore a fresh model

PyTorch · Composite create

**Goal.** Save a supplied model's parameters and load them into a fresh instance.

Implement `model_roundtrip(source, destination, path)` in [attempt.py](attempt.py).

- Source and destination are supplied CPU float64 instances of the same architecture with different initial parameters and a persistent registered buffer. path is a writable file path supplied by the checker.
- Save the source's bare state_dict to path, load that saved file into destination, and return the same destination object. Parameters and persistent buffers must match source and reproduce its predictions.
- Leave source values and both models' mode flags unchanged. Subsequent changes to source state must not change destination state. Use native PyTorch save/load operations.

Registered buffers are part of persistent state as well as trainable parameters.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/model-roundtrip
```

The untouched starter reports an unimplemented operation. For review, save your code and check output. Explain the actual tensor/module operations, state changes and evidence that meet the contract.
