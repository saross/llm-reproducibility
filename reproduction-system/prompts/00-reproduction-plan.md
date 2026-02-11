# Reproduction Planning Prompt — Session R-Plan

**Version:** 1.0
**Last Updated:** 2026-02-10
**Session:** R-Plan (Planning)
**Skill:** reproduction-assessor

---

## Your Task

Analyse the target paper and produce a paper-specific reproduction plan. This plan must be reviewed and approved by the user before execution begins in Session R-A.

**Input:** Paper PDF, extraction.json (if available), code repository or supplement

**Output:** A concrete reproduction plan (`reproduction-plan.md`) with numbered execution
steps, verification targets, risk assessment, and compute strategy. Save to
`outputs/{paper-slug}/reproduction/attempt-{NN}/reproduction-plan.md`.

---

## Critical Rules

1. **Read before planning.** Read the paper (or extraction.json) thoroughly before writing the plan. Understand what the analysis does, what software it uses, and what results it produces.
2. **Classify the reproduction type.** Use the reproduction type framework (A/B/C/D) from the skill to categorise the paper.
3. **Enumerate ALL verification targets.** Every table, figure, and key statistic in the paper should appear in the plan. Do not plan to reproduce only the "easy" ones.
4. **Identify paper-specific risks.** Every reproduction has encountered unique challenges. Anticipate them.
5. **Produce a concrete plan.** Numbered steps, expected outputs, specific tools. Not a generic outline.
6. **Stop after the plan.** Do NOT proceed to execution. The plan requires user approval first.

---

## Procedure

### Phase 1: Read and Understand

1. **Read the paper** — Focus on Methods, Results, and Supplementary Materials sections
2. **Read extraction.json** (if available) — Check `reproducibility_infrastructure` for code/data availability assessment
3. **Examine the code repository** — Clone or browse. Check for:
   - Dockerfile
   - renv.lock / DESCRIPTION / requirements files
   - Script structure (batch-ready? interactive? literate?)
   - README with reproduction instructions
   - Data files included or referenced
4. **Check queue.yaml** — Verify paper status and any prior reproduction notes

### Phase 2: Landscape Analysis

Following the Reproduction Plan Guide (`reproduction-system/reproduction-plan-guide.md`):

1. **Code location:** Where is the code? (GitHub, Zenodo, supplement, personal site)
2. **Data availability:** Where is the data? Classify each dataset using the 5-level
   access taxonomy (Level 0 = fully accessible through Level 4 = never published). For
   papers with multiple data sources, create a data availability inventory with
   dataset-weighted and record-weighted availability percentages. See the Reproduction
   Plan Guide §1.2 for the full protocol.
3. **Environment specification:** What does the paper provide? (Dockerfile, renv, sessionInfo, nothing)
4. **Script execution mode:** How is the analysis designed to run? (batch, interactive, literate, incremental)

### Phase 3: Classification

Classify the reproduction using the type framework:

- **Type A:** Batch-ready with Dockerfile — lowest effort
- **Type B:** Batch-ready without Dockerfile — Docker construction needed
- **Type C:** Interactive scripts without Dockerfile — wrapper + Docker needed
- **Type D:** Proprietary upstream — scope limitation, use intermediates

Note: papers can be multiple types simultaneously.

### Phase 4: Verification Target Enumeration

List every quantitative and qualitative result to verify:

| Target | Location | Values | Classification |
|--------|----------|--------|----------------|
| Table N | p. X | N values | Deterministic/Stochastic |
| Figure N | p. X | Visual | Deterministic/Stochastic |
| Statistic | p. X, §Y | 1 value | Deterministic/Stochastic |

**Classify each target** as deterministic or stochastic. This determines the verification tolerance.

### Phase 5: Risk Assessment

Identify paper-specific risks beyond the standard challenges. Consult:

- `references/examples/pilot-reproduction-summary.md` — Common gotchas from 4 pilot reproductions
- `references/dockerfile-patterns.md` — Expected Docker build challenges
- `references/wrapper-script-patterns.md` — Script adaptation challenges

### Phase 6: Write the Plan

Produce the plan document following the template in the Reproduction Plan Guide. Include:

1. **Paper metadata** — Citation, DOI, reproduction type classification
2. **Materials inventory** — Code, data, supplements with locations and access methods
3. **Execution steps** (for Session R-A) — Numbered, specific, with expected outputs
4. **Verification targets** (for Session R-B) — Complete table with classifications
5. **Risks and mitigations** — Paper-specific challenges with planned responses
6. **Compute strategy** — Runtime estimate, resource allocation (local vs sapphire)
7. **Scope limitations** — What will not be reproduced and why

---

## Handoff

When the plan is complete:

```text
Session R-Plan complete for {paper-slug}

Completed:
- Paper analysis and type classification: {Type A/B/C/D}
- Verification targets identified: {N tables, M figures, K statistics}
- Data availability: {N/M datasets accessible, percentage by records}
- Risks assessed: {brief list}
- Compute estimate: {runtime category}

Plan location: {where the plan was written/presented}

Artefact persistence check:
- [ ] reproduction-plan.md saved to outputs/{paper-slug}/reproduction/attempt-{NN}/
- [ ] data-availability-inventory.md saved (if multi-source paper)

Next session: R-A (Preparation)
Awaiting plan approval before proceeding.
```

**STOP.** Do not proceed to Session R-A without explicit user approval of the plan.

---

## Common Pitfalls

- **Insufficient paper reading.** Skimming the paper and missing key methodological details that affect reproduction strategy
- **Incomplete verification targets.** Missing supplementary tables or inline statistics
- **Underestimating interactive scripts.** Not recognising that a script requires a wrapper until Session R-A
- **Ignoring data access risks.** Assuming all URLs will work without testing
- **Generic plans.** Writing a plan that could apply to any paper rather than being specific to this one

---

## Decision Framework References

When uncertain about classification or strategy, consult:

- **SKILL.md** §A-E — Core decision frameworks
- **reproduction-plan-guide.md** — Flexible planning model with full classification guidance
- **pilot-reproduction-summary.md** — Patterns from 4 completed reproductions
