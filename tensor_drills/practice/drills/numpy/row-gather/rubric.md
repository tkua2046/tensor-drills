# Row gathering rubric

## Ground truth

Output position `i` contains the score at row `i` and column `columns[i]`. The result has shape `(N,)` and the score dtype, including when `N` is zero. Both inputs stay unchanged.

## Assessment

- Use `rectangular array` and `repeated columns` to check that each output position gets its own row and the column for that row. Use `empty batch` for the zero-row result and `one row` and `one column` for singleton dimensions. The verifier checks shape, dtype, and unchanged inputs in each case.
- Look for an explanation of how the code pairs each row with one column index, including when several rows select the same column. [Fixed cases](tests.json)
