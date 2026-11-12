# Compare two products with the same shape

NumPy · Atomic create

**Goal.** Distinguish elementwise multiplication from matrix multiplication when output shapes agree.

Implement `product_kinds(x, y)` in [attempt.py](attempt.py).

Two float64 square matrices are `(N,N)`. Return `(elementwise, matrix_product)` containing `x*y` and the matrix product `x@y`, respectively. Both outputs have shape `(N,N)`. Use native operations and explain which coordinates are paired and which axis is contracted.

Use native operations without Python element or row loops. Preserve all input values, shapes and dtypes during the call. Independent shape parameters are 1–8 unless another bound is stated; derived extents and selected counts follow their formulas. All numeric inputs are finite float64 with magnitude at most 16. Results are compared with relative tolerance 1e-12 and absolute tolerance 1e-10.

Use [the Python setup](../../../README.md#setup) with NumPy. Run from the drill workspace root.

```sh
tensor-drills check numpy/product-kinds
```

The untouched starter reports an unimplemented operation. Save your code and check output for review. Explain the operations, shapes and evidence that meet the contract.
