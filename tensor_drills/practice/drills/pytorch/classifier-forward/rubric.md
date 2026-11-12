# Build and register a two-layer classifier rubric

## Ground truth

Module registration makes both layers appear in named parameters and follow dtype conversion. The nonlinear hidden activation precedes a final linear layer whose logits may be negative.

## Assessment

- Known parameters and negative hidden activations distinguish missing or misplaced ReLU; negative logits reject a final ReLU or softmax. Singleton/empty batches retain both output axes.
- Inspect actual registered layer construction and forward composition. Equivalent registration via attributes or add_module is accepted. Do not grade random initialization values, since the checker injects them.

[Fixed cases](tests.json)
