# Normalize allowed logits in float32

NumPy · Composite create

**Goal.** Compute stable float32 probabilities over allowed positions and return zeros for fully masked rows.

Implement `masked_softmax(x, mask)` in [attempt.py](attempt.py).

Input logits are float16/float32 `(B,T,C)` in [-1000,1000], with `1<=C<=131072`. Boolean mask has rank three and each axis is singleton or matches logits. Normalize over C and return float32 probabilities of the same shape. Excluded entries and all-invalid rows are exact zero. Nonempty row sums are one within 1e-5. Negligible underflow is allowed; probabilities use rtol=1e-5 and atol=1e-7. Promote before exponentiation and accumulation; avoid materialized repeated masks.

Use native vectorized operations. Preserve all input values, shapes and dtypes. Independent shape parameters are 1–8 unless another bound is stated; derived extents and output counts follow their formulas. Calls must emit no warnings. Float64 results use relative and absolute tolerances 1e-10 unless stated otherwise; exact zeros and discrete outputs are checked exactly. Python loops over elements, rows or groups are excluded.

Use [the Python setup](../../../README.md#setup) with NumPy. Run from the drill workspace root.

```sh
tensor-drills check numpy/masked-softmax
```

The untouched starter reports an unimplemented operation. Save your code, check output and explanation for review.
