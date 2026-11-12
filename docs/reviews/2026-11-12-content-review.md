# Content review — 2026-11-12

Candidate: `49b9c9fba13d71edc61149823cdfeef5df4e6fd5`, containing 55 NumPy and 61 PyTorch drills.

Two independent reviewers assessed curriculum breadth and assessment robustness. They found three bounded defects and recommended additional practice areas. The existing overlapping drills generally earn separate outcomes; no immediate consolidation is supported. The six delivered milestones remain complete. The recommendations below describe potential future curriculum work.

## Findings and disposition

| ID | Priority | Finding | Recommended action | Disposition |
| --- | --- | --- | --- | --- |
| A-D1 | P2 | Eight integer-domain drills accept a lossy floating-point comparison or selection approach on their current fixtures. | Add adjacent-large-integer cases, retain direct-integer valid alternatives, and replay the original counterexamples. | Open; reproduced during review. |
| C-D1 | P2 | `masks` and `masking` split direct filtered catalog entries for the same practice family. | Use a consistent preferred mask label across construction and applications. | Open; reproduced in both tracks. |
| C-D2 | P3 | A NumPy softmax prerequisite link promises statistic alignment that its target does not assess. | Narrow the capability statement or link practice that also assesses alignment. | Open; established by tracing the linked materials. |

These reviews did not change drill content, metadata, or curriculum scope. Reusable review instructions and a report template were added separately. Future repairs should append their revised candidate and verification to this record, preserving the original findings.

### A-D1: adjacent large integers

Affected drills:

- [NumPy causal mask](../../tensor_drills/practice/drills/numpy/causal-mask/prompt.md) and [PyTorch causal mask](../../tensor_drills/practice/drills/pytorch/causal-mask/prompt.md)
- [NumPy row maximum](../../tensor_drills/practice/drills/numpy/row-max/prompt.md) and [PyTorch row maximum](../../tensor_drills/practice/drills/pytorch/row-max/prompt.md)
- [NumPy sorted events](../../tensor_drills/practice/drills/numpy/sorted-events/prompt.md) and [partition selection](../../tensor_drills/practice/drills/numpy/partition-topk/prompt.md)
- [PyTorch causal attention](../../tensor_drills/practice/drills/pytorch/causal-attention/prompt.md) and [causal leak repair](../../tensor_drills/practice/drills/pytorch/causal-leak-debug/prompt.md)

Each admits integer values or positions that require exact ordering. An implementation can convert those integers to float64, perform native comparisons or selection, and still pass the existing fixtures. Adjacent integers around `2**53` can become indistinguishable after that conversion. The reviewer reproduced the numerical error in all eight drills; direct-integer alternatives passed the added probes.

For example, let `r = 2**53`, query position `r`, and key positions `[r-1, r+1]`, with both keys valid. The correct causal mask is `[True, False]`. A float conversion admits the future key. With equal attention scores and values `[2, 4]`, correct attention returns `2`; the faulty approach returns `3`. The correct value gradient is `[1, 0]`; the faulty two-key weighting would send half the upstream gradient to each value. The CLI probe stops at the wrong forward result.

Opposite int64 extremes already appear in some fixtures, but they do not expose this loss of adjacency. The faulty approach still uses native operations. A careful reviewer can reject the lossy conversion against the full-domain contract; the finding concerns a semantic gap in fixed coverage and numeric review cues. It differs from a deliberate operation requirement delegated to a rubric. Fixed regression cases should distinguish the error without prescribing a single correct implementation.

### C-D1: mask-topic discovery

The [catalog filter](../../tensor_drills/_catalog.py) matches topic labels exactly. In both tracks, `build-mask`, `conditional-replace`, and `masked-assign` use `masking`, while supplied-mask applications use `masks`.

Four actual CLI probes returned successfully. `--library numpy --topic masks` returned 14 entries and the PyTorch equivalent returned nine; each omitted those three foundational entries. Filtering `masking` returned exactly the three omitted entries per track. Some application entries still name the foundations through prerequisite IDs, providing partial recovery, but the direct topic-filter results split the family.

Choose a preferred label consistently. This correction can preserve multi-label, freeform metadata; it does not require a closed enum or CLI synonym system.

### C-D2: prerequisite evidence

[NumPy row-softmax metadata](../../tensor_drills/practice/drills/numpy/row-softmax/metadata.json) links `numpy/row-mean` for the capability “Compute a row reduction and align it with its original rows.” [Row mean](../../tensor_drills/practice/drills/numpy/row-mean/prompt.md) returns `(R,)` and assesses reduction, without the alignment step.

Narrowing the statement to row reduction would match its evidence. [Row centering](../../tensor_drills/practice/drills/numpy/row-center/prompt.md) is another available practice link when alignment is the intended prerequisite. The softmax drill itself remains useful.

## Curriculum recommendations

These priorities are reviewer judgments about transfer to everyday fluency, not a target number of new drills.

| Priority | Capability to consider | Why existing practice does not establish it |
| --- | --- | --- |
| High | NumPy missing/nonfinite-data reasoning: derive validity from values and use per-feature counts. | Current masked means and standardization supply masks and finite data. The learner does not have to diagnose NaN propagation or derive numerical validity. |
| High | PyTorch-native reproducible data delivery, using an in-memory Dataset/DataLoader and shuffled epochs. | `labeled-batches` correctly permits ordered slicing of existing tensors. It does not require native dataset access, generator ownership, or shuffled epoch behavior. |
| Medium | Cumulative and adjacent-difference reasoning with explicit axes, boundaries, and accumulator dtype. | Moving-window sums permit direct window reduction; prefix summaries return one aggregate per sequence. Neither requires an array of cumulative results. |

Public technical references support what these capabilities entail; the priority order is the reviewer's inference from the fluency goal. [NumPy special values](https://numpy.org/doc/stable/user/misc.html), [PyTorch data tutorial](https://docs.pytorch.org/tutorials/beginner/basics/data_tutorial.html), [PyTorch reproducibility](https://docs.pytorch.org/docs/2.15/notes/randomness.html), and [NumPy cumulative sums](https://numpy.org/doc/stable/reference/generated/numpy.cumsum.html).

Keep the existing ordered-batch, finite-data and sliding-window contracts scoped as written. Evaluate new briefs through the normal curation process before changing the skill map or delivery plan.

## Scope, evidence and limits

The curriculum reviewer inventoried every metadata record and learner prompt, inspected rubric and fixture evidence across overlapping families, and executed the four discovery probes. The [116-drill matrix](2026-11-12-drill-matrix.md) records each drill's distinct assessed contribution. Prerequisite targets resolve, with no cross-track links or cycles. Workload ratings and the explicit general-allocation deferral remain defensible.

The assessment reviewer inspected all 116 assessment packages by family, inventorying 539 fixed cases, and executed independent CLI attempts on 48 risk-selected drills. There were 80 original-fixture CLI runs and 20 additional corrected-fixture runs. Original runs included 55 accepted valid attempts, 15 rejected semantic mistakes, the eight surviving integer-cast mutants, and two deliberately rubric-assessed mechanism shortcuts. Another 610 independent scalar/property scenarios exercised the reviewer-authored approaches. These counts exclude malformed harness experiments.

The probes covered numerical behavior, masks and empty inputs, indexing, storage, RNG and streaming state, autograd, and training transitions. Python 3.12.4, NumPy 2.5.4 and CPU PyTorch 2.15.0 were used in separate library environments. Full attempts, immutable candidate hashes, commands and outputs were preserved as development evidence. This is sampled runtime evidence, not exhaustive verification of every allowed input.

Numerically correct shortcuts that miss an explicit custom Function, manual-VJP, allocation, vectorization or diagnosis requirement were assessed against the prompt and rubric. A fixed-test pass alone was not classified as a defect when that combined assessment fairly covered the requirement.

The review also raised a numeric-contract concern for `reduce-axes`: newly constructed cancellation inputs can make ordinary float32 accumulation miss the stated `1e-6` tolerance, while promoted alternatives pass. This was not a valid implementation rejected by the original fixtures. Clarifying intended accumulation accuracy is a separate contract decision.

No human learning, realistic completion time, or accelerator portability was established by these reviews. Shared storage, denominator, gradient, rank and diagnosis differences justify retaining related drills, including both causal attention creation and the separate controlled leakage probe.

## Reusable workflow

The [authoring guide](../DRILL_AUTHORING.md#challenge-the-assessment) now standardizes requirement-to-evidence tracing, independent valid approaches, semantic near misses, active boundaries, generated-probe records and original-reproducer rechecks. It distinguishes fixed-test coverage from rubric-assessed requirements.

[Whole-catalog review](../DRILL_AUTHORING.md#review-the-catalog) evaluates marginal learning outcomes, prerequisite evidence, discovery and gaps beyond the completed plan. The [review template](../../templates/content-review.md) records scope, findings and dispositions without introducing another drill file.

A separate independent reviewer tried the workflow on NumPy partition selection and PyTorch saved-value repair. Two valid approaches per drill passed; semantic errors failed; numerically passing full-sort and analytic-gradient shortcuts were correctly identified as missing explicit rubric requirements. The workflow and its two additional guards for integer adjacency and topic-filter consistency were reviewed and rechecked without material findings.
