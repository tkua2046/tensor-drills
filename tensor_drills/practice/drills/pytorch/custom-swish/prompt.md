# Implement a custom smooth backward

PyTorch · Composite create

**Goal.** Implement a custom autograd backward for the smooth Swish operation.

Implement `custom_swish(x)` in [attempt.py](attempt.py).

Implement x*sigmoid(x) via a real torch.autograd.Function subclass, saving values with the context/saved-tensor mechanism and providing an analytic backward for arbitrary upstream weights. x is a trainable float64 leaf, length1–5, values in [-4,4], with no incoming gradient. Return same-shaped float64 output with real custom graph history. Preserve input data and leave x.grad empty during forward. First-order derivatives only; higher-order differentiation is not required.

Use native vectorized operations. Preserve input data, shapes and dtypes except for the explicitly required gradients or model updates. Independent dimensions are 1–4 unless another bound is stated; derived extents follow their formulas. Use CPU tensors. Floating results and gradients use relative and absolute tolerances 1e-10 unless stated otherwise; explicit zeros and discrete results are exact. Python loops over elements, rows or groups are excluded.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/custom-swish
```

The untouched starter reports an unimplemented operation. Save your code, check output and explanation for review.
