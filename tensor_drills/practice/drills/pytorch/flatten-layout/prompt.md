# Flatten logical values and inspect sharing

PyTorch · Atomic create

**Goal.** Flatten noncontiguous inputs in logical order and demonstrate the resulting storage relationship.

Implement `flatten_layout(x)` in [attempt.py](attempt.py).

Input is a nonempty 2D int64 array or tensor, possibly transposed or stepped. Return a 1D result in row-major logical order: visit each row in order, then its columns. A view or a copy is permitted. For review, also save a small mutation probe and its output showing whether your chosen result shares input data, and explain that observed relationship. The probe may mutate its disposable inputs after the function returns.

Use native operations without Python element or row loops. Preserve all input values, shapes and dtypes during the call. All tensors are on CPU and do not require gradients. Independent shape parameters are 1–8 unless another bound is stated; derived extents and selected counts follow their formulas.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/flatten-layout
```

The untouched starter reports an unimplemented operation. Save your code and check output for review. Explain the operations, shapes and evidence that meet the contract.
