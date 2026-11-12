# Repair a saved-value mutation rubric

## Ground truth

detach shares storage. The in-place update changes a value saved by multiplication backward, violating its version check. An independent update snapshot permits actual backward on the original source.

## Assessment

Diagnosis: explain aliasing, saved values and the error, with a reproduced failure. Correctness/storage: signed, fractional and singleton sources; actual loss history/leaf gradients; later writes to the snapshot must leave x unchanged. Inspect real backward rather than analytic assignment.

Fixed cases: `saved value 0`, `saved value 1`, `saved value 2`.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

[Fixed cases](tests.json)
