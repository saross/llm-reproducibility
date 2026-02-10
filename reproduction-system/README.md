# Reproduction System

Systematic reproduction framework for computational research papers. Part of the
LLM Reproducibility Project.

## Overview

This system provides the runtime components for reproducing computational analyses
from research papers:

- **Prompts:** Session-specific instructions for each reproduction phase
- **Templates:** Document structure for reproduction artefacts
- **Planning guide:** Flexible model for paper-specific adaptation
- **Launch prompt:** Quick-start primer for new reproductions

## Architecture

```text
reproduction-system/
├── prompts/                          # Session-specific prompts
│   ├── 00-reproduction-plan.md       # Session R-Plan
│   ├── 01-preparation.md             # Session R-A
│   ├── 02-execution-and-verification.md  # Session R-B
│   └── 03-adversarial-review.md      # Session R-C
├── templates/                        # Document templates (copies from skill)
│   ├── environment-template.md
│   ├── log-template.md
│   └── comparison-report-template.md
├── reproduction-plan-guide.md        # Flexible planning model
├── reproduction-launch.md            # Quick-start primer
└── README.md                         # This file
```

## Companion Skill

The `reproduction-assessor` skill (`.claude/skills/reproduction-assessor/`) provides
stable decision frameworks (Dockerfile strategy, verification approach, etc.) that
prompts reference. This separation allows prompts to evolve through testing without
modifying the skill.

## Workflow

1. **R-Plan:** Analyse paper → classify type → produce plan → user approval
2. **R-A:** Acquire materials → build Docker → adapt scripts → user approval
3. **R-B:** Execute analysis → compare results → write documentation → user approval
4. **R-C:** Fresh-context adversarial review → overall assessment

## Scope

- **v1.0:** R-based papers only
- **Future:** Python, Julia support (extension points documented in planning guide)

## Pilot Results

| Paper | Type | Verdict | Runtime |
|-------|------|---------|---------|
| Crema et al. 2024 | B | SUCCESSFUL | ~18h |
| Marwick 2025 | A | SUCCESSFUL | ~13 min |
| Herskind & Riede 2024 | C | SUCCESSFUL | ~30s |
| Dye et al. 2023 | C+D | SUCCESSFUL | ~30s |

---

**Version:** 1.0.0 | **Date:** 2026-02-10
