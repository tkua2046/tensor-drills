# Search event boundaries rubric

## Ground truth

Left boundaries count strictly smaller events; right boundaries count smaller-or-equal events. Half-open counts subtract left boundaries at both endpoints.

## Assessment

Correctness: repeated endpoints, unsorted queries, empty vectors and int64 extremes distinguish boundary choices and unsafe arithmetic. Operations: inspect actual native boundary searches. Reasoning follow-up: explain why upper uses a left boundary.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

Integer precision: `adjacent large int64 event boundaries` exercise adjacent large int64 values. Preserve their exact ordering when comparing positions or choosing indices; inspect conversions for loss of integer distinctions. Equivalent operations that preserve the full input domain are valid.

Fixed cases: `event boundaries 0`, `event boundaries 1`, `event boundaries 2`, `event boundaries 3`, `adjacent large int64 event boundaries`.

[Fixed cases](tests.json)
