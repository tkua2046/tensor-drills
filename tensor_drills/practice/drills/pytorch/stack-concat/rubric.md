# Stack and concatenate two matrices rubric

## Ground truth

For two inputs of shape `(R, C)`, axis 0 gives stacked shape `(2, R, C)` and concatenated shape `(2R, C)`. Axis 1 gives `(R, 2, C)` and `(R, 2C)`. In both outputs the first matrix comes first on the specified axis. Values and dtype are preserved, and neither input changes.

## Assessment

- Use `insert and extend axis 1` and `insert and extend axis 0` to check the ranks, axis positions, and value order. Distinct matrices catch reversing the operands.
- Use `singleton column` to check that a dimension of length one is still present where required. The verifier checks dtype and unchanged inputs in each case.
- Check that the learner distinguishes adding an axis from extending an existing one, and explains how to predict both shapes.

[Fixed cases](tests.json)
