# Standardize selected observations

NumPy · Composite create

**Goal.** Select valid observations and standardize each feature using the selected rows.

Implement `masked_standardize(x, flags)` in [attempt.py](attempt.py).

Input float64 observations are `(N,F)` with Boolean row flags `(N,)`, and `0<=N<=8`. All values have magnitude at most 16. Return selected rows in original order as `(K,F)`, subtracting selected feature means and dividing by selected population standard deviations (`ddof=0`). Constant selected features return exact zeros; no selection gives `(0,F)`. Nonconstant selected features have standard deviation at least 1e-3. Do not add a normalization epsilon.

Use native vectorized operations. Preserve all input values, shapes and dtypes. Independent shape parameters are 1–8 unless another bound is stated; derived extents and output counts follow their formulas. Calls must emit no warnings. Float64 results use relative and absolute tolerances 1e-10 unless stated otherwise; exact zeros and discrete outputs are checked exactly. Python loops over elements, rows or groups are excluded.

Use [the Python setup](../../../README.md#setup) with NumPy. Run from the drill workspace root.

```sh
tensor-drills check numpy/masked-standardize
```

The untouched starter reports an unimplemented operation. Save your code, check output and explanation for review.
