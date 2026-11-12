# Align a window with full-input validity flags

NumPy · Composite create

**Goal.** Select rows in a specified slice using a Boolean mask aligned to the original input.

Implement `window_mask(x, flags, start, stop, step)` in [attempt.py](attempt.py).

Input int64 data is `(R,C)`, flags are Boolean `(R,)`, and bounds satisfy `0<=start<=stop<=R` with positive step. R may be zero; C is positive. Return `(K,C)` containing rows whose original positions belong to the slice and whose original flags are true, in original order. Output sharing is unrestricted.

Use native operations without Python element or row loops. Preserve all input values, shapes and dtypes during the call. Independent shape parameters are 1–8 unless another bound is stated; derived extents and selected counts follow their formulas.

Use [the Python setup](../../../README.md#setup) with NumPy. Run from the drill workspace root.

```sh
tensor-drills check numpy/window-mask
```

The untouched starter reports an unimplemented operation. Save your code and check output for review. Explain the operations, shapes and evidence that meet the contract.
