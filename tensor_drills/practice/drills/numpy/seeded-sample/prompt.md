# Draw reproducible row indices with a local generator

NumPy · Atomic create

**Goal.** Draw row indices without replacement using a local generator seeded by the caller.

Implement `seeded_sample(rows, count, seed)` in [attempt.py](attempt.py).

- `rows` and `count` are Python integers with `0 <= count <= rows <= 100`. `seed` is a Python integer in `[0,2**32)`.
- Return an int64 NumPy array of shape `(count,)` containing distinct row indices in drawn order.
- Reproducibility contract: use the semantics of a fresh PCG64 generator seeded by `seed`, followed by `Generator.choice(rows, size=count, replace=False)` with its other defaults. Equivalent generator construction or population representation is allowed when it gives the same draws.
- Every call starts from its supplied seed, including after calls with other seeds. Leave NumPy's legacy global RNG state unchanged, even for an empty draw.

The same `(rows, count, seed)` must reproduce exactly the same drawn order after an intervening call using another seed.

Use [the Python setup](../../../README.md#setup) with NumPy. Run from the drill workspace root.

```sh
tensor-drills check numpy/seeded-sample
```

The untouched starter reports that the function is unimplemented. For review, save your code and check output. Explain the actual operations and numeric or RNG choices in your implementation.
