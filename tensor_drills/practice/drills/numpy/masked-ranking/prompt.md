# Rank eligible candidates and retain their IDs

NumPy · Composite create

**Goal.** Rank eligible candidates while keeping their original indices, IDs and scores aligned.

Implement `masked_ranking(scores, ids, flags, k)` in [attempt.py](attempt.py).

Supply float64 scores `(C,)` of magnitude at most16, int64 IDs `(C,)`, Boolean eligibility and `0<=k<=C`, with `0<=C<=64`. Return original indices, selected IDs and selected scores for min(k,eligible_count) candidates. Order by descending score, then ascending original index for ties. IDs may repeat and need not be sorted. Full stable sorting is allowed.

Use native vectorized operations. Preserve all input values, shapes and dtypes. Independent shape parameters are 1–8 unless another bound is stated; derived extents and output counts follow their formulas. Calls must emit no warnings. Float64 results use relative and absolute tolerances 1e-10 unless stated otherwise; exact zeros and discrete outputs are checked exactly. Python loops over elements, rows or groups are excluded.

Use [the Python setup](../../../README.md#setup) with NumPy. Run from the drill workspace root.

```sh
tensor-drills check numpy/masked-ranking
```

The untouched starter reports an unimplemented operation. Save your code, check output and explanation for review.
