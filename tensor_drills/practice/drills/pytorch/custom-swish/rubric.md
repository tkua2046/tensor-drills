# Implement a custom smooth backward rubric

## Ground truth

Swish derivative includes both the direct x factor and the sigmoid derivative. A real custom Function participates in the graph and returns one input gradient. Native composition alone is numerically right but does not fulfill this task.

## Assessment

Correctness: fixed signed/nonuniform VJPs and float64 numerical gradcheck. Framework mechanism: inspect actual Function participation, saved context and backward return arity; accept differing class names, wrappers and valid saved-value choices. Forward values alone do not establish a custom backward.

Fixed cases: `custom derivative 0`, `custom derivative 1`, `custom derivative 2`.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

[Fixed cases](tests.json)
