# Rank eligible candidates and retain their IDs rubric

## Ground truth

Eligibility precedes ranking; original indices preserve identity through truncation and deterministic ties.

## Assessment

High ineligible scores, tied scores with unrelated IDs, short results and empty choices expose incorrect eligibility/identity/tie handling. Inspect coupled native indexing. The `tie crossing cutoff` case requires the tie rule during selection, not only sorting the retained subset; `eligible negative scores` must not be filtered by sign.

Fixed cases: `eligible ranking 0`, `eligible ranking 1`, `eligible ranking 2`, `eligible ranking 3`, `eligible ranking 4`.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

[Fixed cases](tests.json)
