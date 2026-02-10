---
name: reproduction-assessor
description: "Reproduces computational research papers through systematic Docker-based execution, quantitative verification, and adversarial review. This skill should be used when the user requests reproduction of a paper, verification of computational results, or assessment of reproducibility infrastructure. Handles R analyses with deterministic or stochastic outputs via a 4-session workflow (R-Plan, R-A, R-B, R-C). R-based papers only in v1.0; extension points for Python/Julia documented."
version: "1.0"
license: Apache 2.0
---

# Reproduction Assessor

Systematic reproduction framework for computational research papers. Executes analyses in isolated Docker environments, quantitatively verifies results against published values, and subjects the reproduction to adversarial review.

## What This Skill Does

This skill enables systematic reproduction of computational analyses from research papers through a 4-session workflow:

1. **Planning** (Session R-Plan) — Analyse the paper, classify reproduction type, identify verification targets, produce a paper-specific execution plan
2. **Preparation** (Session R-A) — Acquire materials (code, data, supplements), construct Docker environment, adapt scripts for batch execution
3. **Execution & Verification** (Session R-B) — Run analysis in Docker, quantitatively compare results against published values, write documentation
4. **Adversarial Review** (Session R-C) — Fresh-context sceptical audit across 5 dimensions: provenance, quantitative claims, scope, bias, methodology

**Scope:** R-based papers only in v1.0. All 5 pilot papers in the current study are R-based. Extension points for Python and Julia are noted in references but not implemented.

## When to Use This Skill

Use when users request:

- "Reproduce this paper"
- "Verify the computational results"
- "Can we reproduce the analysis from [paper]?"
- "Run the reproduction workflow"
- "Assess reproducibility of this paper"
- Any task involving Docker-based execution and verification of published computational analyses

## Core Workflow

```text
Paper + extraction.json + repository
    ↓
Session R-Plan: Paper analysis + type classification + plan
    ↓ (user approval of plan)
Session R-A: Materials + Docker + script adaptation
    ↓ (user approval)
Session R-B: Docker execution + quantitative verification + documentation
    ↓ (user approval)
Session R-C: Adversarial review (fresh context)
    ↓
Reproduction complete: artefact set + verdict
```

**Key principles:**

- **Session R-Plan** produces a paper-specific plan — user must approve before execution begins
- **Sessions R-A and R-B** are the execution core — preparation flows into execution
- **Session R-C** starts fresh — reads artefacts only, has no context from reproduction itself
- **Within sessions:** work autonomously without stopping
- **At session boundaries:** provide handoff summary and STOP

## Using This Skill

### Architecture: Skill + Runtime Prompts

This skill provides:

- **Core decision frameworks** (Dockerfile strategy, script adaptation, verification approach, compute allocation, discrepancy classification)
- **Artefact specifications** (required outputs per reproduction)
- **Reference materials** (patterns, templates, examples)

The user provides:

- **Session prompts** (detailed instructions for each session, from `reproduction-system/prompts/`)
- **Paper materials** (PDF, extraction.json, code repository)
- **Planning guide** (adaptation model, from `reproduction-system/reproduction-plan-guide.md`)

**Why this separation?** Session prompts evolve through testing. This architecture allows prompt tuning without modifying the skill package, minimising versioning conflicts. Mirrors the `research-assessor` separation of skill and extraction prompts.

### Step 1: Identify the Session

Users will typically indicate which phase they want. Listen for:

- "Plan the reproduction" → Session R-Plan (use prompt 00)
- "Prepare the environment" → Session R-A (use prompt 01)
- "Run the analysis" → Session R-B (use prompt 02)
- "Review the reproduction" → Session R-C (use prompt 03)
- "Reproduce this paper" → Start at Session R-Plan

### Step 2: Receive the Session Prompt

The user will provide or reference the session prompt for the current phase. These prompts are stored in `reproduction-system/prompts/` and contain detailed instructions for that specific session.

### Step 3: Consult Supporting References As Needed

If you encounter uncertainty during reproduction, consult:

**Decision Frameworks:**

- `references/dockerfile-patterns.md` — Rocker hierarchy, common deps, iterative build strategy, renv pathway
- `references/wrapper-script-patterns.md` — Interactive-to-batch conversion, parameterisation, output saving
- `references/verification-strategies.md` — Deterministic vs stochastic comparison, Highest Posterior Density (HPD) interval checking, figure assessment

**Review:**

- `references/adversarial-review-framework.md` — 5-dimension audit protocol with per-dimension verdicts

**Templates:**

- `references/templates/environment-template.md` — Environment specification document structure
- `references/templates/log-template.md` — Reproduction log document structure
- `references/templates/comparison-report-template.md` — Comparison report document structure

**Examples:**

- `references/examples/pilot-reproduction-summary.md` — Condensed patterns from 4 pilot reproductions

### Step 4: Execute and Return

Follow the session prompt to:

1. Complete all sub-phases within the session
2. Generate required artefacts
3. Provide handoff summary at session end

## Core Decision Frameworks

### A. Dockerfile Strategy

**When authors provide a Dockerfile, always use it.**

Rationale: represents the authors' tested environment; bundles system dependencies (often the hardest part); ensures version matching; documents implicit dependencies.

Even if the Dockerfile has minor issues, fix rather than reconstruct:

| Situation | Action |
|-----------|--------|
| Author Dockerfile works | Use as-is |
| Minor issues (typos, missing packages) | Fix and document |
| Uses renv.lock | Let renv restore handle packages |
| Clearly broken or incomplete | Construct from scratch |
| No Dockerfile provided | Construct from `rocker/r-ver:{version}` |

**When constructing a Dockerfile:**

1. Start with `rocker/r-ver:{version}` — use the R version from the paper, sessionInfo, or a contemporary version
2. Add system dependencies iteratively (expect 1-3 build attempts for transitive deps)
3. Install R packages from CRAN/GitHub as specified
4. Copy analysis scripts and data into the image (or use volume mounts)

**For complete patterns and the rocker hierarchy:**
→ See `references/dockerfile-patterns.md`

### B. Script Adaptation Strategy

**CRITICAL: NO algorithmic modifications.** Wrapper scripts may reorganise execution order, parameterise repeated operations, and add output saving — but must never change the analytical logic.

| Script Type | Adaptation Required | Example |
|-------------|--------------------| --------|
| Batch-ready | None — use as-is | Crema et al. 2024 |
| Literate programming (Rmd/Qmd) | `rmarkdown::render()` in Docker | Marwick 2025 |
| Interactive (RStudio) | Write wrapper with parameterised functions | Herskind & Riede 2024 |
| Incremental code blocks | Assemble into batch script, fix indices | Dye et al. 2023 |

**Permissible modifications:**

- Add `pdf()` / `png()` / `ggsave()` for output capture
- Parameterise repeated operations (e.g., n-gram size)
- Add `write.csv()` for numerical output
- Redirect `print()` output to files
- Add `sink()` for console capture

**Prohibited modifications:**

- Changing statistical methods or parameters
- Modifying data filtering or subsetting logic
- Altering model specifications
- Adding or removing analysis steps

**For complete patterns:**
→ See `references/wrapper-script-patterns.md`

### C. Verification Strategy

| Analysis Type | Strategy | Tolerance | Example |
|---------------|----------|-----------|---------|
| Deterministic | Exact match | 0 | Herskind (frequency counts), Dye (post-processing) |
| Stochastic (MCMC) | Within HPD intervals | Published confidence intervals | Crema (Bayesian posteriors) |
| Stochastic (bootstrap/permutation) | Within expected variance | ±2 SE or similar | — |
| GAM/regression | Coefficient comparison | Within reported precision | Marwick (minor p-value difference) |
| Proprietary upstream | Document scope limitation | N/A | Dye (OxCal not reproduced) |

**Deterministic analyses:** Every value must match. Differences indicate a bug in the reproduction, not expected variation.

**Stochastic analyses:** Fresh MCMC runs will produce different point estimates. Verify:

1. Point estimates within published HPD/CI intervals
2. Qualitative conclusions unchanged
3. Direction and magnitude of effects consistent

**Figure verification:** Visual comparison — layout, patterns, relative positions. Exact pixel matching not expected (rendering differences). Focus on whether the scientific content matches.

**For complete strategies and HPD interval checking:**
→ See `references/verification-strategies.md`

### D. Compute Resource Allocation

| Runtime Estimate | Resource | Rationale |
|-----------------|----------|-----------|
| < 1 hour | Local Docker | Quick verification |
| 1-24 hours | Consider sapphire | Avoids tying up user's machine |
| > 24 hours | Sapphire with detached containers | Survives SSH disconnects |

**Sapphire workflow for long-running tasks:**

1. Build Docker image on sapphire
2. Launch detached container: `docker run -d --name reproduction-{slug} ...`
3. Monitor: `docker logs -f reproduction-{slug}` or `docker stats`
4. Results via volume mounts to `~/cc-scratch/`

**Parallel MCMC strategy:** For analyses with multiple independent model runs, launch separate Docker containers concurrently. Create separate working directories to prevent write conflicts. Monitor with `docker stats --no-stream`.

### E. Discrepancy Classification

| Category | Definition | Verdict Impact |
|----------|-----------|----------------|
| EXACT_MATCH | Values identical to reported precision | SUCCESSFUL |
| WITHIN_PRECISION | Difference within rounding of reported precision | SUCCESSFUL |
| WITHIN_CONFIDENCE | Within published confidence/HPD intervals (stochastic only) | SUCCESSFUL |
| MINOR_DISCREPANCY | Small difference, conclusions unchanged | SUCCESSFUL with note |
| MAJOR_DISCREPANCY | Substantive difference affecting conclusions | PARTIAL or FAILED |

**Verdict categories:**

- **SUCCESSFUL** — All (or nearly all) values reproduced within expected tolerances; conclusions confirmed
- **PARTIAL** — Some analyses reproduced, others could not (scope limitations, missing data, etc.)
- **FAILED** — Material discrepancies; reproduced results contradict published findings
- **BLOCKED** — Reproduction could not be attempted (missing code, inaccessible data, proprietary tools with no intermediates)

## Artefact Specifications

Each reproduction produces a standard artefact set in `outputs/{paper-slug}/reproduction/attempt-{NN}/`:

### Required Artefacts

| Artefact | Purpose | Template |
|----------|---------|----------|
| `Dockerfile` | Reproducible environment definition | — |
| `run-analysis.R` (or wrapper) | Batch-executable analysis script | — |
| `environment.md` | Software versions, dependencies, data sources | `references/templates/environment-template.md` |
| `log.md` | Timeline, modifications, outputs, FAIR findings | `references/templates/log-template.md` |
| `comparisons/comparison-report.md` | Quantitative results + verdict | `references/templates/comparison-report-template.md` |
| `outputs/` | All generated outputs (plots, CSVs, logs) | — |

### Optional Artefacts

| Artefact | When Needed |
|----------|-------------|
| `run.log` | Console output from Docker execution |
| `docker-build.log` | Docker build output (if non-trivial) |
| `adversarial-review.md` | Session R-C output |

## Session Structure

Four sessions: mandatory planning followed by three execution sessions.

| Session | Prompt | Focus | Duration |
|---------|--------|-------|----------|
| **R-Plan** | `00-reproduction-plan.md` | Analyse paper, classify type, identify targets, produce plan | 30-60 min |
| **R-A** | `01-preparation.md` | Material acquisition + Docker build + script adaptation | 30-90 min |
| **R-B** | `02-execution-and-verification.md` | Run analysis + compare results + write documentation | 30 min - hours |
| **R-C** | `03-adversarial-review.md` | 5-dimension sceptical audit | 30-60 min |

### Session Boundaries

**R-Plan → R-A:** User must approve the reproduction plan before execution begins.

**R-A → R-B:** Preparation complete; Docker image built; scripts adapted. User approval.

**R-B → R-C:** Results verified; documentation written. User approval.

**R-C:** Fresh session. Reads artefacts only. No context from R-A or R-B.

### Handoff Format

```text
Session R-[Plan/A/B] complete for {paper-slug}

Completed:
- {summary of what was done}

Environment: {Docker image, build iterations}
Verification: {N/M values matched, preliminary verdict}

Next session: R-[A/B/C/Complete]
```

### Long-Running Exception

If execution requires >1 hour compute (e.g., MCMC on sapphire):

1. R-A launches the Docker run in detached mode
2. User monitors completion
3. R-B resumes after computation finishes

### R-C Independence

The adversarial review session starts fresh — reads artefacts only, has no context from the reproduction itself. This prevents confirmation bias and mirrors independent peer review.

## Common R System Dependencies

Quick-reference table for Docker construction. These are system-level libraries required by common R packages:

| R Package | System Dependency | Debian Package |
|-----------|-------------------|----------------|
| igraph | GLPK solver | `libglpk-dev` |
| sf, proj4 | PROJ library | `libproj-dev` |
| sf, rgdal | GDAL library | `libgdal-dev` |
| sf | GEOS library | `libgeos-dev` |
| curl, httr | libcurl | `libcurl4-openssl-dev` |
| openssl | OpenSSL | `libssl-dev` |
| xml2 | libxml2 | `libxml2-dev` |
| units | UDUNITS | `libudunits2-dev` |
| rJava | Java | `default-jdk` |
| magick | ImageMagick | `libmagick++-dev` |
| Cairo | Cairo graphics | `libcairo2-dev` |
| sodium | libsodium | `libsodium-dev` |
| textshaping | HarfBuzz + FriBidi | `libharfbuzz-dev libfribidi-dev` |
| ragg | FreeType + PNG + TIFF | `libfreetype6-dev libpng-dev libtiff5-dev` |
| V8 | V8 JavaScript engine | `libv8-dev` |

**Pattern:** When R package installation fails with "configure: error", check the error message for the missing library name and install the corresponding Debian package.

## Reproduction Type Classification

Papers fall into four types based on their computational infrastructure:

| Type | Description | Effort | Example |
|------|-------------|--------|---------|
| **A** | Batch-ready with Dockerfile | Lowest | Marwick 2025 |
| **B** | Batch-ready without Dockerfile | Docker construction needed | Crema et al. 2024 |
| **C** | Interactive scripts without Dockerfile | Wrapper + Docker | Herskind & Riede 2024, Dye et al. 2023 |
| **D** | Proprietary upstream with pre-computed intermediates | Scope limitation | Dye et al. 2023 (OxCal) |

**Note:** A paper may be multiple types (e.g., Dye is both C and D).

**For complete classification guidance and per-paper adaptation:**
→ See `reproduction-system/reproduction-plan-guide.md`

---

## Important Notes

**For testing/debugging:**

- Can run individual sessions independently (R-A without R-Plan if plan already exists)
- Templates provide consistent structure across reproductions
- Pilot reproduction summary provides pattern reference

**Expected outcomes:**

- R-Plan: Paper-specific execution plan with verification targets
- R-A: Working Docker image + adapted scripts
- R-B: Quantitative comparison report + documentation artefacts
- R-C: Adversarial review report with per-dimension verdicts

**v1.0 limitations:**

- R-based papers only (Python/Julia extension points documented but not implemented)
- Single-paper workflow (no batch processing queue)
- Manual supplement retrieval may be needed (ScienceDirect blocks programmatic access)

---

**The user will provide the detailed session prompt for each phase. Use this skill's reference materials to support decision-making during reproduction.**
