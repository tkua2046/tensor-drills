# Repair a sequence calibration calculation

PyTorch · Composite debug

**Goal.** Combine sequence offsets, timestep biases and feature scales on their intended axes.

Repair `broadcast_calibration(x, offsets, bias, scale)` in [attempt.py](attempt.py).

Float64 values are `(B,T,F)`, sequence offsets `(B,F)`, timestep bias `(T,)` and feature scales `(F,)`. Return `(B,T,F)` with `out[b,t,f]=(x[b,t,f]+offsets[b,f]+bias[t])*scale[f]`. The starter can raise a shape error or return incorrect values depending on the input dimensions. Repair it using native broadcasting without materializing repeated operands. Explain the cause and how your checks distinguish a repair from a shape-only workaround.

Use native operations without Python element or row loops. Preserve all input values, shapes and dtypes during the call. All tensors are on CPU and do not require gradients. Independent shape parameters are 1–8 unless another bound is stated; derived extents and selected counts follow their formulas. All numeric inputs are finite float64 with magnitude at most 16. Results are compared with relative tolerance 1e-12 and absolute tolerance 1e-10.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/broadcast-calibration
```

The starter raises a shape error on some cases and returns incorrect values on others. Save your code and check output for review. Explain the operations, shapes and evidence that meet the contract.
