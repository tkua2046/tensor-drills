# Repair pairwise squared distances rubric

## Ground truth

The starter reduces norms across rows rather than features. Correct norm vectors align with each collection's row count; contraction supplies pairwise dot products.

## Assessment

Unequal and equal dimensions expose both symptoms of the norm-axis bug. Compare independent coordinate-wise sums, input preservation and exact nonnegativity. Inspect allocation shapes; a broadcast cube may pass fixed values but violates the prompt.

The `nearby floating coordinates` case checks cancellation within the stated allowance while nonnegativity stays exact.

Fixed cases: `distances 0`, `distances 1`, `distances 2`, `distances 3`, `distances 4`.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

[Fixed cases](tests.json)
