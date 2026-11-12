# Contract a matrix VJP manually

PyTorch · Atomic create

**Goal.** Compute input and weight vector-Jacobian products for a matrix product without autograd.

Implement `matrix_vjp(x, w, u)` in [attempt.py](attempt.py).

Supply nontrainable float64 x `(M,F)`, w `(F,O)` and upstream u `(M,O)` for y=x@w. Independent dimensions are1–4, magnitudes at most4. Return `(dx,dw)` with shapes `(M,F)` and `(F,O)`. Compute the VJP using native contractions; do not invoke autograd or backward in your implementation.

Use native vectorized operations. Preserve input data, shapes and dtypes except for the explicitly required gradients or model updates. Independent dimensions are 1–4 unless another bound is stated; derived extents follow their formulas. Use CPU tensors. Floating results and gradients use relative and absolute tolerances 1e-10 unless stated otherwise; explicit zeros and discrete results are exact. Python loops over elements, rows or groups are excluded.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/matrix-vjp
```

The untouched starter reports an unimplemented operation. Save your code, check output and explanation for review.
