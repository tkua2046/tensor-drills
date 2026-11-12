# Contract a matrix VJP manually rubric

## Ground truth

Each output contribution is weighted by its upstream value, then contracted over the output feature or observation axis as appropriate.

## Assessment

Correctness: rectangular and singleton axes, signed nonuniform upstream and strided inputs, with independent scalar VJP values. Operations: inspect manual contractions; autograd can pass values but misses the skill.

Fixed cases: `matrix reverse 0`, `matrix reverse 1`, `matrix reverse 2`.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

[Fixed cases](tests.json)
