# Observe an intermediate gradient

PyTorch · Atomic create

**Goal.** Use an explicit upstream tensor and retain the gradient of a non-leaf intermediate.

Implement `non_scalar_backward(x, u)` in [attempt.py](attempt.py).

Supply trainable float64 leaf vector x, length1–4, and same-shaped nontrainable upstream u, both magnitude at most4; x.grad starts None. Form z=x*x and out=z+2*x. Retain z.grad, invoke out.backward(u) once (or equivalent native backward), and return the real `(z,out)` tensors. z must be non-leaf with retained gradient u; x.grad=(2*x+2)*u. Preserve input data and u. Use actual backward and retention, not analytic gradient assignment. A second backward and retain_graph are not required.

Use native vectorized operations. Preserve input data, shapes and dtypes except for the explicitly required gradients or model updates. Independent dimensions are 1–4 unless another bound is stated; derived extents follow their formulas. Use CPU tensors. Floating results and gradients use relative and absolute tolerances 1e-10 unless stated otherwise; explicit zeros and discrete results are exact. Python loops over elements, rows or groups are excluded.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/non-scalar-backward
```

The untouched starter reports an unimplemented operation. Save your code, check output and explanation for review.
