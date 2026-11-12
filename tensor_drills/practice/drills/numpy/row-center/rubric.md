# Center rows using their own means rubric

## Ground truth

The row statistic broadcasts along that row's columns, rather than across rows or the entire matrix.

## Assessment

Rectangular and square inputs with differing row means expose wrong reduction axes and silent broadcast alignment errors. Single rows, columns and empty batches preserve rank. Compare expected entries, not only the mean of the result. Inspect the actual reduction and operand shape.

Fixed case names: `center 2-3 contiguous`, `center 3-3 contiguous`, `center 1-4 contiguous`, `center 3-1 contiguous`, `center 0-3 contiguous`, `center 2-4 strided`.

Use the saved code, check output and explanation as evidence. Required native operations and ownership explanations are assessed here in addition to fixed values. Equivalent approaches that meet the prompt are valid; general style suggestions are advisory.

[Fixed cases](tests.json)
