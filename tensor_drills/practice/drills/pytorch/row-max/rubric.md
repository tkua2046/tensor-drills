# Keep row maxima aligned with indices rubric

## Ground truth

Each maximum and its index refer to the same row; the first occurrence determines ties.

## Assessment

Negative rows, nonadjacent ties, one column, empty rows and distinct rows expose wrong axes and last-tie selection. Inspect native reduction/index operations and explain the tie rule.

Use the saved code, check output and explanation as evidence. Required native operations and ownership explanations are assessed here in addition to fixed values. Equivalent approaches that meet the prompt are valid; general style suggestions are advisory.

[Fixed cases](tests.json)
