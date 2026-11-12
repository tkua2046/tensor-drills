# Changelog

## Unreleased

## 0.2.0 - 2026-11-12

### Added

- Expand the bundled catalog to 116 independently runnable drills: 55 NumPy and 61 PyTorch, each with a learner prompt, starter, fixed cases and review rubric.
- Practice core shapes, dtypes, indexing, masks, reductions, broadcasting, storage and matrix products in either library, with an optional indexing warm-up.
- Practice NumPy stable numerics, sampling, grouped statistics, sequence loss, search, partition selection, overlapping windows, streaming entropy, linear systems, regression and masked attention.
- Practice PyTorch modules, device placement, NumPy conversion, autograd, model state, token losses, routing, training updates, manual/custom gradients and causal attention diagnosis.
- Follow independent NumPy and PyTorch learning paths through the skill map and linked prerequisite practice.
- Author drills with documented briefs, a six-file template, fresh-workspace verification, adversarial assessment and whole-catalog review workflows.

### Changed

- Present Tensor Drills as a standalone NumPy and PyTorch learning library, with separate content, infrastructure and contributor documentation.

### Fixed

- Detect lossy int64 comparisons and selections with adjacent-large-integer cases in eight drills.
- Include mask construction, replacement and assignment under the `masks` topic while preserving `masking` filters.
- Match NumPy softmax's prerequisite description to the row-mean practice it links.

## 0.1.0 - 2026-11-11

### Added

- Create editable practice workspaces and run fixed checks through the `tensor-drills` CLI or the Python API.
- Practice NumPy row gathering, PyTorch classifier debugging, and PyTorch inline validation with fixed checks and Markdown review rubrics.
- Author custom drills with JSON test manifests and Python verifiers.
- Bundle catalog metadata for the example drills and document its JSON schema.
- List and filter drills by library, scope, task type, topics, and workload with `tensor-drills list`.
- Show which drills a prerequisite practice drill prepares learners for.
