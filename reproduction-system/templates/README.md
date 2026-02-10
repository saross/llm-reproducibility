# Reproduction Templates

These templates are copies of the canonical versions maintained in the skill package.

**Canonical location:** `.claude/skills/reproduction-assessor/references/templates/`

## Available Templates

| Template | Purpose |
|----------|---------|
| `environment-template.md` | Software versions, dependencies, and data sources |
| `log-template.md` | Reproduction timeline, modifications, and FAIR findings |
| `comparison-report-template.md` | Quantitative comparison and verdict justification |

## Usage

Templates are referenced during Session R-B (execution and verification) when writing
reproduction documentation. Each reproduction populates a copy of each template into
`outputs/{paper-slug}/reproduction/attempt-{NN}/`.

## Updating Templates

If templates need modification, update the canonical copies in the skill references
directory. Then copy the updated versions here. The skill references are the source
of truth.
