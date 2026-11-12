# Control module mode and recording independently rubric

## Ground truth

Evaluation and recording are independent. Context managers should enable/disable recording for each call and restore ambient state; uniform model mode is restored afterward.

## Assessment

- Hooks observe exact forward modes, child mode and recording. Deterministic dropout changes training values without random expectations. All four incoming mode/recording combinations are checked.
- Explain each control and restoration. Accept equivalent context/state APIs that meet the contract; changing only eval or only no_grad is insufficient.

[Fixed cases](tests.json)
