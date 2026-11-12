# Compare two products with the same shape rubric

## Ground truth

Elementwise products pair equal coordinates; matrix products sum over the first input's columns and second input's rows. Matching output shapes do not make them interchangeable.

## Assessment

Distinct nonsymmetric matrices expose swapped product roles and reversed multiplication. Identity and singleton inputs provide regression checks. Inspect the actual multiplication/contraction operations and explanation.

Fixed case names: `products 2 identity=False contiguous`, `products 3 identity=False strided`, `products 3 identity=True transpose`, `products 1 identity=False contiguous`.

Use the saved code, check output and explanation as evidence. Required native operations and ownership explanations are assessed here in addition to fixed values. Equivalent approaches that meet the prompt are valid; general style suggestions are advisory.

[Fixed cases](tests.json)
