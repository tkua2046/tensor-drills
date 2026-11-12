# Project each sequence with its own weights

PyTorch · Composite create

**Goal.** Apply each batch item's own projection matrix to its mean over valid timesteps.

Implement `batched_projection(x, flags, weights)` in [attempt.py](attempt.py).

Float64 values are `(B,T,F)`, Boolean flags `(B,T)` and float64 weights `(B,F,O)`. Every sequence has at least one valid timestep. Return `(B,O)` by averaging valid timesteps separately and multiplying each mean by that sequence's own matrix. Projection before averaging is also valid when equivalent. All inputs are supplied; this function does not consume an earlier submission.

Use native operations without Python element or row loops. Preserve all input values, shapes and dtypes during the call. All tensors are on CPU and do not require gradients. Independent shape parameters are 1–8 unless another bound is stated; derived extents and selected counts follow their formulas. All numeric inputs are finite float64 with magnitude at most 16. Results are compared with relative tolerance 1e-12 and absolute tolerance 1e-10.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/batched-projection
```

The untouched starter reports an unimplemented operation. Save your code and check output for review. Explain the operations, shapes and evidence that meet the contract.
