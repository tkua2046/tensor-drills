# Keep top-k scores and labels aligned

PyTorch · Composite create

**Goal.** Select the highest scores per batch while keeping labels and score gradients aligned.

Implement `topk_labels(x, labels, k)` in [attempt.py](attempt.py).

Trainable float64 leaf scores `(B,C)` have no incoming gradient and are distinct within each row. Labels are int64 `(B,C)` and k satisfies `0<=k<=C`. Return `(indices,scores,selected_labels)`, each `(B,k)`, in descending score order. Keep the selected scores connected to x, including k=0. Preserve source tracking/gradient state during the call. Labels may repeat and need not match index order.

Use native vectorized operations. Preserve all input values, shapes and dtypes. Independent shape parameters are 1–8 unless another bound is stated; derived extents and output counts follow their formulas. Use CPU tensors. Floating results and gradients use relative and absolute tolerances 1e-10 unless stated otherwise; explicit zeros and discrete results are exact. Python loops over elements, rows or groups are excluded.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/topk-labels
```

The untouched starter reports an unimplemented operation. Save your code, check output and explanation for review.
