# Reduce shared affine gradients rubric

## Ground truth

Weight and bias are reused across both batch and time, so their VJPs sum contributions from both axes. Mean reductions change the derivative.

## Assessment

Correctness: unequal batch/time/feature/output extents, signed unequal upstream, singleton and strided cases. Inspect native manual reductions and explain reverse broadcasting.

Fixed cases: `shared reverse 0`, `shared reverse 1`, `shared reverse 2`.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

[Fixed cases](tests.json)
