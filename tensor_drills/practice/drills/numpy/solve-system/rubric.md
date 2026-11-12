# Solve while preserving RHS rank rubric

## Ground truth

The RHS rank determines result rank. The requirement is to practice a solve operation; explicit inversion may produce correct numbers but does not meet it.

## Assessment

Correctness: non-diagonal systems, vector versus one-column RHS, multiple RHS, singleton D and strided RHS. Fixed coefficients plus residuals check results. Operations: inspect actual solve/factorization calls, accepting equivalent native approaches.

Fixed cases: `solve rank 0`, `solve rank 1`, `solve rank 2`, `solve rank 3`.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

[Fixed cases](tests.json)
