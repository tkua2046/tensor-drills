# Observe an intermediate gradient rubric

## Ground truth

Backward needs an upstream seed for a non-scalar result. retain_grad exposes a non-leaf gradient; retain_graph is a different operation controlling graph lifetime.

## Assessment

Correctness: nonuniform signed/zero upstream and x values. Inspect real graph, retained non-leaf gradient, and supplied seed. Reasoning follow-up: distinguish the intermediate gradient from the total derivative at x.

Fixed cases: `upstream gradient 0`, `upstream gradient 1`, `upstream gradient 2`.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

[Fixed cases](tests.json)
