# Compare expansion with independent repeated data

PyTorch · Atomic create

**Goal.** Expand singleton data without materializing repeats and create a separately writable copy.

Implement `expand_copy(x, batch)` in [attempt.py](attempt.py).

Input is a writable int64 `(1,F)` array or tensor and a positive target batch size. Return `(shared, independent)` shaped `(batch,F)`. The shared result must use zero stride on the expanded axis when batch>1 and reflect source writes. The independent result must be writable, independent of source and shared result, with no aliasing between its rows. Do not write through the overlapping expanded tensor; use the independent copy for writes. Inputs may be strided.

Use native operations without Python element or row loops. Preserve all input values, shapes and dtypes during the call. All tensors are on CPU and do not require gradients. Independent shape parameters are 1–8 unless another bound is stated; derived extents and selected counts follow their formulas.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/expand-copy
```

The untouched starter reports an unimplemented operation. Save your code and check output for review. Explain the operations, shapes and evidence that meet the contract.
