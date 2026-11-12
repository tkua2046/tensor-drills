# Compose attention with absolute causality rubric

## Ground truth

Causality compares supplied absolute positions, not row numbers or a triangular shape. Query and key padding both matter. Safe empty normalization must preserve graph connections for zero gradients.

## Assessment

Correctness/gradients: independent scalar expectations with nonuniform upstream, active equal-position dependencies, shifted/unordered positions, rectangular extents, padding, unequal D/E, strided and empty axes. Exact masked outputs and excluded source contributions are checked. Accept safe elementary contractions or native attention with explicit masks/dropout policy.

An active equality case includes a key at exactly the query position; strict inequality must fail both values and gradients.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

Integer precision: `adjacent large causal positions`, `adjacent negative positions with gradients` exercise adjacent large int64 values. Preserve their exact ordering when comparing positions or choosing indices; inspect conversions for loss of integer distinctions. Equivalent operations that preserve the full input domain are valid.

Fixed cases: `shifted rectangular`, `future probe baseline`, `future probe changed`, `all excluded`, `no keys`, `no queries`, `active equal positions`, `adjacent large causal positions`, `adjacent negative positions with gradients`.

[Fixed cases](tests.json)
