# Center rows using their own means

NumPy · Composite create

**Goal.** Subtract each row's own mean from its entries.

Implement `row_center(x)` in [attempt.py](attempt.py).

Float64 data is `(R,C)` with R possibly zero and C positive. Return the same shape with `out[r,c]=x[r,c]-mean(x[r,:])`. Leave the original unchanged. Output sharing is unrestricted.

Use native operations without Python element or row loops. Preserve all input values, shapes and dtypes during the call. Independent shape parameters are 1–8 unless another bound is stated; derived extents and selected counts follow their formulas. All numeric inputs are finite float64 with magnitude at most 16. Results are compared with relative tolerance 1e-12 and absolute tolerance 1e-10.

Use [the Python setup](../../../README.md#setup) with NumPy. Run from the drill workspace root.

```sh
tensor-drills check numpy/row-center
```

The untouched starter reports an unimplemented operation. Save your code and check output for review. Explain the operations, shapes and evidence that meet the contract.
