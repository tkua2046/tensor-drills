# Repair a sequence calibration calculation rubric

## Ground truth

The intended bug aligns timestep bias to the batch axis. Unequal B/T raises; equal B/T silently uses the wrong bias. Sequence offsets and feature scales already have their intended roles.

## Assessment

Unequal and equal B/T cases isolate both symptoms of the one bug; T/F equality distinguishes bias aligned to the trailing feature axis. Diagnose the cause and trace the repaired operand shapes. Accept algebraically equivalent native calculations.

Fixed case names: `calibration 2-3-4 contiguous`, `calibration 3-3-2 contiguous`, `calibration 2-3-3 strided`, `calibration 1-3-2 contiguous`, `calibration 2-1-1 contiguous`.

Use the saved code, check output and explanation as evidence. Required native operations and ownership explanations are assessed here in addition to fixed values. Equivalent approaches that meet the prompt are valid; general style suggestions are advisory.

[Fixed cases](tests.json)
