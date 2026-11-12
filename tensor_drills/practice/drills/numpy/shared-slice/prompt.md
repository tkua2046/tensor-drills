# Return a view and an independent slice

NumPy · Atomic create

**Goal.** Return both a shared stepped slice and an independent copy of its initial values.

Implement `shared_slice(x, start, stop, step)` in [attempt.py](attempt.py).

Input is a writable int64 vector of length 1–64. Slice bounds satisfy `0<=start<stop<=len(x)` with positive step and at least one selected entry. Return `(shared, independent)` with the initial slice values. Later writes must propagate in both directions between x and shared; the copy must stay independent of both. Do not edit x during construction. The supplied vector may itself be a stepped view with nonzero offset.

Use native operations without Python element or row loops. Preserve all input values, shapes and dtypes during the call. Independent shape parameters are 1–8 unless another bound is stated; derived extents and selected counts follow their formulas.

Use [the Python setup](../../../README.md#setup) with NumPy. Run from the drill workspace root.

```sh
tensor-drills check numpy/shared-slice
```

The untouched starter reports an unimplemented operation. Save your code and check output for review. Explain the operations, shapes and evidence that meet the contract.
