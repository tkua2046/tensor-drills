# Normalize masks with safe backward behavior rubric

## Ground truth

Only allowed positions contribute. Handling all-invalid rows must be checked through actual backward results, not only repaired forward values. Equivalent native repairs are valid when the supplied logits receive finite correct gradients; no blanket ban on intermediate NaNs is imposed.

## Assessment

An excluded highest logit, broadcast masks, singleton support and fully masked rows separate normalization and backward failures. Inspect stable native operations; accept elementary or guarded native softmax.

Fixed cases: `masked gradients 0`, `masked gradients 1`.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

[Fixed cases](tests.json)
