# Select elements or retain whole rows rubric

## Ground truth

Element masking collapses matched entries; row masking preserves the complete feature axis and selected row order.

## Assessment

No-match, full-match64-element and empty-batch cases assess counts and rank. Distinct element and row masks expose accidental reuse or flattening. Inspect actual native selection and explain both output shapes.

Fixed case names: `selection 3-4 mixed contiguous`, `selection 8-8 all strided`, `selection 2-3 none contiguous`, `selection 0-3 none contiguous`, `selection 3-1 mixed transpose`.

Use the saved code, check output and explanation as evidence. Required native operations and ownership explanations are assessed here in addition to fixed values. Equivalent approaches that meet the prompt are valid; general style suggestions are advisory.

[Fixed cases](tests.json)
