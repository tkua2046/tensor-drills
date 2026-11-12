# Maintain stable streaming entropy rubric

## Ground truth

Softmax entropy can be recovered from a fixed number of sufficient statistics, rescaled when the running maximum increases. Retaining all logits violates the state/storage contract even if values are right.

## Assessment

Correctness/numerics: prefix values, repeated queries, empty/constant/dominant streams and a late jump in maximum. The same sequence is split two ways. Storage/mechanism: inspect every retained object and chunk-local temporary; fixed cases alone cannot prove no hidden history. Accept any scalar representation satisfying the contract.

Fixed cases: `stream partition 0`, `stream partition 1`, `stream partition 2`, `stream partition 3`, `stream partition 4`, `stream partition 5`.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

[Fixed cases](tests.json)
