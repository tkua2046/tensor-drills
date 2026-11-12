# Pack head features into contiguous sequence order

PyTorch · Composite create

**Goal.** Pack head features into contiguous sequence order while preserving their gradient path.

Implement `head_pack(x)` in [attempt.py](attempt.py).

Trainable float64 leaf heads are `(B,H,T,D)` with no incoming gradient. Return contiguous `(B,T,H*D)` satisfying `out[b,t,h*D+d]=x[b,h,t,d]`. Inputs may have positive noncontiguous strides and nonzero storage offsets. Sharing or copying is allowed if the result is contiguous and retains the source gradient path. Preserve source tracking state and gradient buffers during the call.

Use native vectorized operations. Preserve all input values, shapes and dtypes. Independent shape parameters are 1–8 unless another bound is stated; derived extents and output counts follow their formulas. Use CPU tensors. Floating results and gradients use relative and absolute tolerances 1e-10 unless stated otherwise; explicit zeros and discrete results are exact. Python loops over elements, rows or groups are excluded.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/head-pack
```

The untouched starter reports an unimplemented operation. Save your code, check output and explanation for review.
