# Combine causal positions and padding validity rubric

## Ground truth

Causality is a comparison of supplied positions, including equality, combined independently with query and key validity.

## Assessment

Rectangular and shifted positions expose triangular-only masks; equality exposes strict comparison; differing batch padding exposes missing query masks or swapped axes. Empty query/key dimensions remain valid Boolean shapes. Inspect broadcast construction and avoid position subtraction that could overflow int64.

Use the saved code, check output and explanation as evidence. Required native operations and ownership explanations are assessed here in addition to fixed values. Equivalent approaches that meet the prompt are valid; general style suggestions are advisory.

[Fixed cases](tests.json)
