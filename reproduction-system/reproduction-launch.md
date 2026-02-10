# Reproduction Launch Prompt

## Session-per-Phase Approach

Reproduction is organised into 4 focused sessions:

| Session | Prompt | Focus |
|---------|--------|-------|
| **R-Plan** | `00-reproduction-plan.md` | Analyse paper, classify type, produce plan |
| **R-A** | `01-preparation.md` | Materials + Docker + script adaptation |
| **R-B** | `02-execution-and-verification.md` | Run analysis + compare + document |
| **R-C** | `03-adversarial-review.md` | 5-dimension sceptical audit |

## Starting a New Reproduction (Session R-Plan)

1. **Check queue:** Read `studies/open-science-compliance/corpus/queue.yaml` → identify target paper
2. **Invoke skill:** Launch `reproduction-assessor` skill
3. **Read planning guide:** `reproduction-system/reproduction-plan-guide.md`
4. **Run Session R-Plan:** Analyse paper → classify type → produce plan → STOP for approval

## Continuing a Reproduction (Sessions R-A / R-B / R-C)

1. **Read the plan:** Check the approved reproduction plan
2. **Read artefacts:** Check any completed artefacts from prior sessions
3. **Run next session:** Complete all phases within the session → handoff summary → STOP

---

## Session Execution Rules

**Within each session:**

- Work autonomously without stopping
- Complete all phases in the session
- Generate required artefacts

**At session boundaries:**

- Provide handoff summary
- Stop and wait for user approval before proceeding

**R-C independence:**

- Start with fresh context (no reproduction memory)
- Read artefacts only
- Be sceptical

---

## Key Decision Frameworks

| Framework | Purpose | Location |
|-----------|---------|----------|
| Dockerfile Strategy | When to use author's vs construct | SKILL.md §A |
| Script Adaptation | Interactive → batch conversion | SKILL.md §B |
| Verification Strategy | Deterministic vs stochastic comparison | SKILL.md §C |
| Compute Allocation | Local vs sapphire | SKILL.md §D |
| Discrepancy Classification | EXACT_MATCH → MAJOR_DISCREPANCY | SKILL.md §E |

## Do NOT

- Skip Session R-Plan (every paper needs a specific plan)
- Run all sessions in one context (session boundaries matter)
- Modify analytical logic in wrapper scripts
- Skip verification targets from the plan
- Run R-C with context from R-A/R-B (fresh context required)

---

## Files to Reference

- `reproduction-system/reproduction-plan-guide.md` — Planning model
- `reproduction-system/prompts/` — Session-specific prompts
- `.claude/skills/reproduction-assessor/SKILL.md` — Decision frameworks
- `.claude/skills/reproduction-assessor/references/` — Patterns, templates, examples
- `studies/open-science-compliance/corpus/queue.yaml` — Paper queue

---

**Version:** 1.0.0 | **Date:** 2026-02-10
**Purpose:** Brief primer for reproduction workflow
**Principle:** 4 focused sessions with fresh-context adversarial review
