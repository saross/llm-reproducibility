# Environment Specification

## {Paper Author(s)} {Year} Reproduction

### Software Versions

| Component | Version | Source |
|-----------|---------|--------|
| R | {version} ({release date}) | rocker/r-ver:{version} Docker image |
| {Primary package} | {version} | CRAN / GitHub / r-universe |
| {Additional packages} | {version} | {source} |
| Docker base | rocker/r-ver:{version} | Docker Hub |
| Host OS | {OS description} | {Local / Sapphire} execution |

### System Dependencies Added to Docker

The base rocker image required the following additional system libraries:

- `{package}` — {description} (required by {R package})

<!-- List each system dependency with its purpose and which R package requires it -->

### R Package Dependencies (Automatic)

{Primary package} v{version} pulls in these key dependencies:

- `{dep}` — {purpose}

<!-- List significant transitive dependencies, not every package -->

### Data Source(s)

- **File:** {filename} ({size})
- **Source:** {URL or repository} ({access method})
- **Format:** {rows, columns, content description}

<!-- If multiple data sources, list each separately -->

### Upstream Software (Not Reproduced)

<!-- Include this section only if relevant -->

- **{Software name} {version}** — {description} ({licence type})
- {What it was used for}
- {Why it was not reproduced}
- {What pre-computed outputs were used instead}

### Notes

<!-- Paper-specific environment notes: version selection rationale, -->
<!-- determinism properties, known mismatches, etc. -->

- {Note about R version selection}
- {Note about determinism / stochasticity}
- {Note about any version mismatches}
