# Reproduction Prompts

Session-specific prompts for the reproduction-assessor workflow.

## Prompt Index

| # | File | Session | Focus |
|---|------|---------|-------|
| 00 | `00-reproduction-plan.md` | R-Plan | Paper analysis, type classification, plan production |
| 01 | `01-preparation.md` | R-A | Material acquisition, Docker construction, script adaptation |
| 02 | `02-execution-and-verification.md` | R-B | Analysis execution, quantitative comparison, documentation |
| 03 | `03-adversarial-review.md` | R-C | 5-dimension sceptical audit (fresh context) |

## Architecture

Prompts provide session-specific instructions. The `reproduction-assessor` skill
(`.claude/skills/reproduction-assessor/SKILL.md`) provides stable decision frameworks
that prompts reference. This separation allows prompts to evolve through testing without
modifying the skill.

## Session Boundaries

- **R-Plan → R-A:** User must approve the reproduction plan
- **R-A → R-B:** User confirms preparation is complete
- **R-B → R-C:** User confirms verification is complete
- **R-C:** Fresh context required (no memory from prior sessions)

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02-10 | Initial release — 4 prompts derived from 4 pilot reproductions |
