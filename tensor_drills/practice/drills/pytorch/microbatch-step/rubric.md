# Accumulate one globally normalized update rubric

## Ground truth

A window has one global valid-token denominator and one optimizer step. A zero-valid window must skip the step because momentum and weight decay can change parameters even with zero data gradient.

## Assessment

Correctness/state: independently aggregated scalar loss/gradients, actual step-time gradients, parameter and momentum updates, forward/backward/step counts, stale-gradient clearing, and nonempty→zero→nonempty windows. Empty list, empty batch, ignored batch and unequal counts are included. Inspect actual backward and supplied optimizer use; do not replace the optimizer or manually edit state. Explain sum-versus-mean scaling.

Fixed cases: `optimizer windows 0`, `optimizer windows 1`, `optimizer windows 2`.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

[Fixed cases](tests.json)
