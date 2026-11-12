# Compute safe masked log mass rubric

## Ground truth

Excluded high logits must not affect log mass. Empty reductions have log mass negative infinity, unlike the zero probabilities used by masked softmax.

## Assessment

Correctness/numerics: extreme logits, excluded maxima, one allowed value, mixed empty rows, broadcast masks and no physical classes. Accept stable max-shift or native log-add reductions. Check infinity signs explicitly.

Fixed cases: `masked log mass 0`, `masked log mass 1`, `masked log mass 2`.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

[Fixed cases](tests.json)
