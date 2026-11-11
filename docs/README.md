# Tensor Drills documentation

Tensor Drills helps learners who know basic Python become fluent in NumPy and PyTorch. Start with the document that owns the question you are trying to answer.

| Document | Responsibility |
| --- | --- |
| [Content Design](CONTENT_DESIGN.md) | Defines the learning goals, criteria for choosing skills and drills, and progression for each track. |
| [Skill Map](SKILL_MAP.md) | Maps shared and library-specific skills by topic. Describes what to practice and links bundled drills beside the skills they teach. |
| [Content Implementation Plan](CONTENT_IMPLEMENTATION_PLAN.md) | Sets delivery order for each track, maps skill coverage to milestones or deferrals, and owns authoring briefs and acceptance criteria. |
| [Infrastructure Design](INFRA_DESIGN.md) | Defines how drills are packaged, discovered, run, and assessed, including the roles of fixed tests and rubrics. |
| [Drill metadata schema](drill-metadata.schema.json) | Defines the fields and allowed values in a drill's catalog metadata. |
| [Resources and Drill Sources](RESOURCES.md) | Records public references, drill origins, and applicable attribution. |
| [Drill Authoring Guide](DRILL_AUTHORING.md) | Explains how to use the drill template, verify a drill in a fresh workspace, and hand it off for review. Includes author and reviewer prompts. |
| [Development Notes](../DEVNOTES.md) | Explains how to run project checks and build distributions. |

For a specific drill, use the prompt for the learner's task and contract, the fixed cases for expected behavior, and the rubric for review evidence. [Drill package and assessment](INFRA_DESIGN.md#drill-package-and-assessment)

## Editing and review

1. **Identify the owner.** Name the question the edit answers. Put the change in the document that owns that question and link to it where readers need the context. For example, add a bundled drill link beside its skill in the map and update the milestone status in the implementation plan when delivery changes.
2. **Check the full document.** For a structural edit, read the document from its entry point. Check that headings group related material consistently, parallel sections use the same structure, and readers can still find the next step.
3. **Check related documents.** Use the relevant checks below to trace changed claims to their source. Verify links and anchors affected by moves or renames.

| Change | What to verify |
| --- | --- |
| Milestone scope | Name the drills or outcomes that complete the milestone and link their briefs. When later work builds on earlier practice, name where that practice is scheduled. |
| Skill coverage | Trace each mapped skill to a milestone or explicit deferral in the implementation plan, for each affected track. Read the linked drill's prompt and fixed cases or rubric. Link it for the outcomes it assesses. Mark practice within a larger task as applied practice. |
| Drill verification | Keep the exact steps and pass criteria in the drill authoring guide. Check summaries against that guide and try any changed commands in a fresh workspace. |
| Infrastructure definitions and examples | Check that the definition fits the learning goals of both tracks. Link to drill files for contracts and cases. Track pending work in the implementation plan. |

For an independent review that spans documents, share the exact revision and ask the reviewer to trace changed claims using these checks. Ask for file locations and evidence for any mismatch.

Use the [project README](../README.md) to get started as a learner.
