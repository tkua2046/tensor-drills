# Compose attention with absolute causality rubric

## Ground truth

Causality compares supplied absolute positions, not row numbers or a triangular shape. Query and key padding both matter. Safe empty normalization must preserve graph connections for zero gradients.

## Assessment

Correctness/gradients: independent scalar expectations with nonuniform upstream, active equal-position dependencies, shifted/unordered positions, rectangular extents, padding, unequal D/E, strided and empty axes. Exact masked outputs and excluded source contributions are checked. Accept safe elementary contractions or native attention with explicit masks/dropout policy.

An active equality case includes a key at exactly the query position; strict inequality must fail both values and gradients.

Fixed cases: `shifted rectangular`, `future probe baseline`, `future probe changed`, `all excluded`, `no keys`, `no queries`, `active equal positions`.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

[Fixed cases](tests.json)
