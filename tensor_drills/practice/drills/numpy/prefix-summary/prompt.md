# Join each valid-prefix mean and last vector

NumPy · Composite create

**Goal.** Summarize each valid sequence prefix with its mean and last valid feature vector.

Implement `prefix_summary(x, lengths)` in [attempt.py](attempt.py).

Float64 values are `(B,T,F)`, magnitude at most16, with int64 lengths `(B,)` in [0,T] and `0<=T<=8`. Return `(B,2*F)`, concatenating the valid-prefix mean and last valid feature vector. Length-zero sequences return exact zeros in both halves, including when T=0.

Use native vectorized operations. Preserve all input values, shapes and dtypes. Independent shape parameters are 1–8 unless another bound is stated; derived extents and output counts follow their formulas. Calls must emit no warnings. Float64 results use relative and absolute tolerances 1e-10 unless stated otherwise; exact zeros and discrete outputs are checked exactly. Python loops over elements, rows or groups are excluded.

Use [the Python setup](../../../README.md#setup) with NumPy. Run from the drill workspace root.

```sh
tensor-drills check numpy/prefix-summary
```

The untouched starter reports an unimplemented operation. Save your code, check output and explanation for review.
