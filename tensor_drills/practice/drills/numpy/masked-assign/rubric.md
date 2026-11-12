# Assign through a mask so aliases see the update rubric

## Ground truth

Selected positions in the existing storage receive the replacement; unselected positions and the mask stay unchanged. Return None. Rebinding a local variable or assigning through an advanced-index temporary does not update the caller. A noncontiguous input view must update the corresponding base entries without touching the gaps.

## Assessment

`mixed mask` includes positive selected entries and negative unselected entries, so the supplied mask governs the update. `input is a strided view` checks aliases and the whole base, including unselected gaps. All-true, all-false, empty and singleton cases check shape and return semantics. Inspect actual mutation of existing storage. Equivalent native assignment, masked fill, or copying a computed result back into the supplied storage is valid.

Check the learner's code and explanation alongside the fixed-case output. A named API alone is insufficient evidence: identify the actual operands, shapes, and effects. Discuss avoidable allocations where useful while preserving equivalent valid approaches.

[Fixed cases](tests.json)
