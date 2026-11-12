# Apply one supervised training update rubric

## Ground truth

The update clears stale gradients, uses raw logits and the supplied mean loss, backpropagates and invokes the supplied optimizer once. Detached loss is useful as a log value without retaining its graph.

## Assessment

- Known stale buffers and different consecutive batches expose missing clearing. Identical examples distinguish mean from sum gradients. Hooks observe forward/step count, actual step-time gradients and updated parameters.
- Inspect use of supplied model/loss/optimizer and explain update ordering. Accept clearing via model or optimizer, None or zeros; post-step clearing is allowed.

[Fixed cases](tests.json)
