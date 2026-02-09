# Environment — Herskind & Riede 2024 Reproduction

## Original Environment (from paper)

- **R version:** 4.2.2 (stated in paper text; not recorded in script)
- **Package versions:** Not specified anywhere (no renv.lock, no Dockerfile, no session info)
- **Operating system:** Not stated
- **IDE:** Likely RStudio (script designed for interactive use)

## Reproduction Environment

- **Docker base image:** `rocker/r-ver:4.2.2`
- **Docker image tag:** `herskind-riede:local`
- **Operating system (host):** Ubuntu (Linux 6.16.9)
- **Date:** 2026-02-10

### R Package Versions (Reproduction)

| Package | Version | Purpose |
|---------|---------|---------|
| R | 4.2.2 | Base (matches paper) |
| quanteda | 3.2.4 | Corpus linguistics / skip-gram generation |
| readxl | 1.4.2 | Excel file reading |
| ggplot2 | 3.4.1 | Data visualisation |
| dplyr | 1.1.0 | Data manipulation |
| data.table | 1.14.8 | Efficient data frame operations |
| extrafont | 0.19 | Font management |

### System Dependencies Added to Dockerfile

```text
libxml2-dev        # Required by readxl
libfontconfig1-dev # Required by extrafont
fonts-dejavu       # System fonts (Gill Sans MT not available)
```

### Font Substitution

The original script specifies `Gill Sans MT` (proprietary Monotype font, typically available only
on Windows/macOS with Microsoft Office). This font is not available in the Docker container.
The reproduction uses the default `sans` font. This affects **aesthetics only** — no computational
outputs are affected.

## Environment Comparison

| Aspect | Original | Reproduction | Match? |
|--------|----------|--------------|--------|
| R version | 4.2.2 | 4.2.2 | Exact |
| Package versions | Unknown | See table above | Cannot verify |
| Containerisation | None | Docker (our construction) | N/A |
| Dependency management | None | Manual install.packages() | N/A |
| Font | Gill Sans MT | DejaVu Sans (fallback) | Aesthetic only |
| OS | Unknown | Ubuntu 22.04 (Jammy) in Docker | Cannot verify |

## Key Observation

This is the first reproduction in our study where the authors provided **no environment
specification whatsoever** — no Dockerfile, no renv.lock, no conda environment, no session
info dump. The only version information available is the R version stated in the paper text.
Package versions were determined by whatever CRAN served as compatible with R 4.2.2 at the
time of our Docker build (2026-02-10).

Despite this gap, the analysis reproduced exactly because:

1. The computations are fully deterministic (frequency counts and logarithms)
2. The `quanteda` API for `tokens_ngrams()` has remained stable
3. No stochastic elements (no MCMC, no random sampling)
4. Simple mathematical operations (PMI = log(observed/expected)) are implementation-invariant
