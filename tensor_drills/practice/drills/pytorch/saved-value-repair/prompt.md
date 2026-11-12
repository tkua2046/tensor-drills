# Repair a saved-value mutation

PyTorch · Atomic debug

**Goal.** Repair mutation of a value needed by backward without changing the intended loss or update.

Repair `saved_value_repair(x)` in [attempt.py](attempt.py).

Supply a trainable float64 leaf vector x, length 1–4, magnitude at most4, with x.grad=None. Form loss=sum(x*x), create an updated snapshot x+1, call backward, and return `(updated, loss)`. Preserve x data and tracking. x.grad must be 2*x; updated must be detached and independently stored; loss must retain real graph history. The starter raises a backward error and changes its source. Explain the cause and save before/after evidence. Assigning analytic gradients or detaching loss does not satisfy the task.

Use native vectorized operations. Preserve input data, shapes and dtypes except for the explicitly required gradients or model updates. Independent dimensions are 1–4 unless another bound is stated; derived extents follow their formulas. Use CPU tensors. Floating results and gradients use relative and absolute tolerances 1e-10 unless stated otherwise; explicit zeros and discrete results are exact. Python loops over elements, rows or groups are excluded.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/saved-value-repair
```

The faulty starter raises a backward error and changes its source. Explain the cause and the evidence for your repair. Save your code, check output and explanation for review.
