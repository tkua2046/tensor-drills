# Reduce shared affine gradients

PyTorch · Composite create

**Goal.** Reduce shared weight and bias gradients across batch and time axes.

Implement `shared_affine_vjp(x, w, bias, u)` in [attempt.py](attempt.py).

Supply nontrainable float64 x `(B,T,F)`, shared w `(F,O)`, bias `(O,)` and upstream u `(B,T,O)` for y=x@w+bias. Dimensions1–4, magnitudes at most4. Return dx `(B,T,F)`, dw `(F,O)` and dbias `(O,)`, without autograd/backward. Use native contractions and reductions. Bias values do not affect this affine derivative.

Use native vectorized operations. Preserve input data, shapes and dtypes except for the explicitly required gradients or model updates. Independent dimensions are 1–4 unless another bound is stated; derived extents follow their formulas. Use CPU tensors. Floating results and gradients use relative and absolute tolerances 1e-10 unless stated otherwise; explicit zeros and discrete results are exact. Python loops over elements, rows or groups are excluded.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/shared-affine-vjp
```

The untouched starter reports an unimplemented operation. Save your code, check output and explanation for review.
