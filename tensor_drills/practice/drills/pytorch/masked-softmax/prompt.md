# Normalize masks with safe backward behavior

PyTorch · Composite create

**Goal.** Normalize over allowed positions with finite backward gradients and zero outputs for fully masked rows.

Implement `masked_softmax(x, mask)` in [attempt.py](attempt.py).

Trainable float64 leaf logits `(B,H,Q,K)` lie in [-1000,1000] with no incoming gradient. Boolean mask is rank four with each axis singleton or matching logits. Normalize over K, retaining shape, dtype and gradient path. Excluded positions and fully excluded rows have exact zero probabilities and gradients; other row sums are one. All outputs/gradients must be finite; negligible underflow is allowed. Preserve source tracking/gradient state during the call.

Use native vectorized operations. Preserve all input values, shapes and dtypes. Independent shape parameters are 1–8 unless another bound is stated; derived extents and output counts follow their formulas. Use CPU tensors. Floating results and gradients use relative and absolute tolerances 1e-10 unless stated otherwise; explicit zeros and discrete results are exact. Python loops over elements, rows or groups are excluded.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/masked-softmax
```

The untouched starter reports an unimplemented operation. Save your code, check output and explanation for review.
