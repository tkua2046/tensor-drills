# Replace negative values in an independent result rubric

## Ground truth

Negative values become zero in an independent result; every other value retains its position. Shape and dtype are preserved. The source remains unchanged during replacement and under later writes, even when there are no negative entries or the input is empty.

## Assessment

`no negatives` catches returning the input unchanged without creating independent storage. Every case verifies source preservation, result writability, and writes in both directions. Strided and empty cases preserve shape. Inspect native operations; accept conditional selection, clipping/maximum, or assignment on an independent copy. A Python element-loop solution can pass values but misses the prompt's operation requirement.

Check the learner's code and explanation alongside the fixed-case output. A named API alone is insufficient evidence: identify the actual operands, shapes, and effects. Discuss avoidable allocations where useful while preserving equivalent valid approaches.

[Fixed cases](tests.json)
