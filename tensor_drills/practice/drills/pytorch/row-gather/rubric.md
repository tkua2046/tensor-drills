# Gather one score per row rubric

## Ground truth

Output position `i` contains the score at row `i` and column `columns[i]`. The CPU result has shape `(N,)` and the score dtype, including when `N` is zero. Both inputs stay unchanged.

## Assessment

- Use `rectangular tensor` and `repeated columns` to check that each output gets its own row and the column for that row. `empty batch` checks the zero-row result; `one row` and `one column` check singleton dimensions.
- The verifier checks shape, dtype, and unchanged inputs. Check that the learner explains how the row and column indices stay paired, including when several rows select the same column.

[Fixed cases](tests.json)
