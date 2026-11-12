# Diagnose future-token leakage rubric

## Ground truth

The missing causal condition lets future key/value rows influence earlier queries despite correct padding. A controlled future-only perturbation reveals dependency leakage; padding alone cannot enforce causality.

## Assessment

Diagnosis evidence: save original and repaired results for the same future-only K/V change with Q fixed; earlier outputs must become invariant while permitted dependencies remain meaningful. Explain absolute-position/padding interaction. Fixed numeric/VJP and baseline/changed cases reject the missing condition and constant-zero repairs. Assess both repaired code and the saved probe; passing fixed cases alone is incomplete.

An active equality case includes a key at exactly the query position; strict inequality must fail both values and gradients.

Fixed cases: `shifted rectangular`, `future probe baseline`, `future probe changed`, `all excluded`, `no keys`, `no queries`, `active equal positions`.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

[Fixed cases](tests.json)
