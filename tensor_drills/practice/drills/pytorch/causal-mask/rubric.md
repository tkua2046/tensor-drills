# Combine causal positions and padding validity rubric

## Ground truth

Causality is a comparison of supplied positions, including equality, combined independently with query and key validity.

## Assessment

Rectangular and shifted positions expose triangular-only masks; equality exposes strict comparison; differing batch padding exposes missing query masks or swapped axes. Empty query/key dimensions remain valid Boolean shapes. Inspect broadcast construction and avoid position subtraction that could overflow int64.

Use the saved code, check output and explanation as evidence. Required native operations and ownership explanations are assessed here in addition to fixed values. Equivalent approaches that meet the prompt are valid; general style suggestions are advisory.

Integer precision: `adjacent large int64 positions` exercise adjacent large int64 values. Preserve their exact ordering when comparing positions or choosing indices; inspect conversions for loss of integer distinctions. Equivalent operations that preserve the full input domain are valid.

Fixed cases: `causal 0`, `causal 1`, `causal 2`, `causal 3`, `causal 4`, `extreme position comparisons`, `adjacent large int64 positions`.

[Fixed cases](tests.json)
