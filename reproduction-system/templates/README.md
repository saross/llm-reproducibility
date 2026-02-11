# Reproduction Templates

**Canonical location:** `.claude/skills/reproduction-assessor/references/templates/`

These files are **copies** of the canonical versions. The skill package is the source of
truth. If templates need modification, update the canonical copies first, then synchronise
here.

## Available Templates

| Template | Purpose |
|----------|---------|
| `environment-template.md` | Software versions, dependencies, and data sources |
| `log-template.md` | Reproduction timeline, modifications, and FAIR findings |
| `comparison-report-template.md` | Quantitative comparison and verdict justification |

## Synchronisation

To check whether copies are in sync with canonical versions:

```bash
diff reproduction-system/templates/environment-template.md \
     .claude/skills/reproduction-assessor/references/templates/environment-template.md
diff reproduction-system/templates/log-template.md \
     .claude/skills/reproduction-assessor/references/templates/log-template.md
diff reproduction-system/templates/comparison-report-template.md \
     .claude/skills/reproduction-assessor/references/templates/comparison-report-template.md
```

If differences are found, copy from the canonical location to here.

## Usage

Templates are referenced during Session R-B (execution and verification) when writing
reproduction documentation. Each reproduction populates a copy of each template into
`outputs/{paper-slug}/reproduction/attempt-{NN}/`.
