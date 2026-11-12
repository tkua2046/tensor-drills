# Split unequal sections and rejoin them rubric

## Ground truth

Sections follow the supplied sizes along the named axis. Zero sizes produce empty parts that retain both dimensions. Joining the parts in order restores the input. Aliasing is allowed, and the input stays unchanged.

## Assessment

`unequal columns` and `split rows` test both axes. `zero-size middle section` distinguishes sizes from boundaries and equal chunks. Empty and strided cases preserve dimensions and order. Inspect both the sectioning operation and the join consuming its parts. Returning the original instead of performing a join can pass values but misses the disclosed operation requirement. Accept equivalent APIs and bookkeeping over sizes.

Check the learner's code and explanation alongside the fixed-case output. A named API alone is insufficient evidence: identify the actual operands, shapes, and effects. Discuss avoidable allocations where useful while preserving equivalent valid approaches.

[Fixed cases](tests.json)
