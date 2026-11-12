# Gather scores at batch/time target indices rubric

## Ground truth

The class coordinate is selected separately at each batch/time position; upstream weights return only to those selected coordinates.

## Assessment

Nonuniform upstream weights, distinct lengths and repeated target IDs expose axis/rank errors and detachment. Inspect native gather or equivalent advanced indexing.

Fixed cases: `token scores 0`, `token scores 1`, `token scores 2`.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

[Fixed cases](tests.json)
