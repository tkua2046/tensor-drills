# Gather scores with ignored target IDs

NumPy · Atomic create

**Goal.** Gather each target score while returning zero at ignored targets.

Implement `ignored_score_gather(x, targets, ignore)` in [attempt.py](attempt.py).

Float64 scores are `(N,C)`, targets are int64 `(N,)`, N may be zero, and ignore is an int64 value. Every nonignored target is a valid column; ignore may be inside or outside the valid column range. Return float64 `(N,)`, gathering each nonignored score and returning exact zero for ignored entries.

Use native vectorized operations. Preserve all input values, shapes and dtypes. Independent shape parameters are 1–8 unless another bound is stated; derived extents and output counts follow their formulas. Calls must emit no warnings. Float64 results use relative and absolute tolerances 1e-10 unless stated otherwise; exact zeros and discrete outputs are checked exactly. Python loops over elements, rows or groups are excluded.

Use [the Python setup](../../../README.md#setup) with NumPy. Run from the drill workspace root.

```sh
tensor-drills check numpy/ignored-score-gather
```

The untouched starter reports an unimplemented operation. Save your code, check output and explanation for review.
