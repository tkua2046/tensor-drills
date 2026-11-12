# Use true-class denominators for accuracy

NumPy · Composite create

**Goal.** Measure accuracy separately for each true class using that class's observation count.

Implement `per_class_accuracy(true, pred, classes)` in [attempt.py](attempt.py).

Int64 true labels and predictions are `(N,)`, with `0<=N<=32`. True labels are valid classes or -1 to ignore; predictions are valid classes. Return float64 per-class accuracy `(classes,)` and native-integer true-class counts. Absent classes have exact zero accuracy/counts.

Use native vectorized operations. Preserve all input values, shapes and dtypes. Independent shape parameters are 1–8 unless another bound is stated; derived extents and output counts follow their formulas. Calls must emit no warnings. Float64 results use relative and absolute tolerances 1e-10 unless stated otherwise; exact zeros and discrete outputs are checked exactly. Python loops over elements, rows or groups are excluded.

Use [the Python setup](../../../README.md#setup) with NumPy. Run from the drill workspace root.

```sh
tensor-drills check numpy/per-class-accuracy
```

The untouched starter reports an unimplemented operation. Save your code, check output and explanation for review.
