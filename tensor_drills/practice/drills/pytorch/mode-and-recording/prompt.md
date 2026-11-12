# Control module mode and recording independently

PyTorch · Atomic create

**Goal.** Control model mode and gradient recording independently across three forwards.

Implement `mode_and_recording(model, features)` in [attempt.py](attempt.py).

- The supplied CPU float64 model has uniform incoming train/eval mode and deterministic dropout/linear behavior, with no mutable running-statistic buffers. Features are a nonempty matrix requiring gradients.
- Make exactly three forwards on those features, in order: evaluation mode with recording enabled; training mode with recording disabled; evaluation mode with recording disabled. Return their outputs as a tuple.
- The first forward must record even if called inside an outer no_grad context. Restore the incoming uniform model mode and ambient recording state. Leave parameters and feature values unchanged.
- Restoration of RNG state or independently mixed child modes is outside this drill.

Model evaluation mode controls behavior; gradient recording is a separate control.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/mode-and-recording
```

The untouched starter reports an unimplemented operation. For review, save your code and check output. Explain the actual tensor/module operations, state changes and evidence that meet the contract.
