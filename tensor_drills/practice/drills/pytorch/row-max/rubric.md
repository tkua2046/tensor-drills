# Keep row maxima aligned with indices rubric

## Ground truth

Each maximum and its index refer to the same row; the first occurrence determines ties.

## Assessment

Negative rows, nonadjacent ties, one column, empty rows and distinct rows expose wrong axes and last-tie selection. Inspect native reduction/index operations and explain the tie rule.

Use the saved code, check output and explanation as evidence. Required native operations and ownership explanations are assessed here in addition to fixed values. Equivalent approaches that meet the prompt are valid; general style suggestions are advisory.

Integer precision: `adjacent large int64 maxima` exercise adjacent large int64 values. Preserve their exact ordering when comparing positions or choosing indices; inspect conversions for loss of integer distinctions. Equivalent operations that preserve the full input domain are valid.

Fixed cases: `max 2-4 contiguous`, `max 3-1 strided`, `max 2-3 transpose`, `empty batch`, `adjacent large int64 maxima`.

[Fixed cases](tests.json)
