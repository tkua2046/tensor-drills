# Normalize allowed entries by their RMS

NumPy · Composite create

**Goal.** Normalize each row by its valid-entry RMS while leaving excluded and zero-norm rows at zero.

Implement `masked_rms(x, flags)` in [attempt.py](attempt.py).

Inputs are float64 `(B,T)` values and Boolean flags of the same shape, with `0<=T<=8`. Values have magnitude at most 16; each nonzero magnitude is at least 1e-6. For each row, normalize allowed values by `sqrt(sum(allowed x**2)/allowed_count)`. Excluded entries and rows with zero count or zero norm return exact zero. Return `(B,T)` float64 without adding an epsilon.

Use native vectorized operations. Preserve all input values, shapes and dtypes. Independent shape parameters are 1–8 unless another bound is stated; derived extents and output counts follow their formulas. Calls must emit no warnings. Float64 results use relative and absolute tolerances 1e-10 unless stated otherwise; exact zeros and discrete outputs are checked exactly. Python loops over elements, rows or groups are excluded.

Use [the Python setup](../../../README.md#setup) with NumPy. Run from the drill workspace root.

```sh
tensor-drills check numpy/masked-rms
```

The untouched starter reports an unimplemented operation. Save your code, check output and explanation for review.
