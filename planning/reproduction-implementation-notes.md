# Reproduction Implementation Notes

Lessons learned and decisions made during reproduction attempts. This document captures implementation guidance that should inform future reproduction workflows.

---

## Environment Setup

### Dockerfile Policy

**When authors provide a Dockerfile, always use it as part of the reproduction.**

Rationale:
- Represents the authors' tested, working environment
- Bundles system dependencies (often the hardest part)
- Ensures version matching for language runtime and packages
- Documents implicit dependencies that may not appear in README
- Isolates reproduction environment from local system

Even if the Dockerfile has minor issues (typos, outdated base images), it's easier to fix a provided Dockerfile than to reconstruct the environment from scratch.

**Exceptions:**
- Dockerfile is clearly broken or incomplete
- Security concerns with the image
- Need to test across multiple environments (in which case, use Dockerfile as reference)

### Discovered: crema-et-al-2024

The authors provided a Dockerfile with:
- Exact R version (4.3.3 via rocker/rstudio)
- All system dependencies (gdal, geos, proj, etc.)
- R package installation commands

One typo found: `RColoBrewer` should be `RColorBrewer` — fix before building.

---

## Compute Resources

### Task Categories

| Task Type | Typical Duration | Suitable Compute |
|-----------|------------------|------------------|
| Data cleaning scripts | < 1 minute | Local laptop |
| Figure/table generation | < 1 minute | Local laptop |
| Short simulations | Minutes to 1 hour | Local laptop |
| MCMC analyses | Hours to days | Remote/cloud |
| Full reproduction pipelines | Days | Remote/cloud |

### Long-Running Task Considerations

For tasks exceeding ~2 hours:

1. **Thermal throttling** — Laptops may throttle CPU under sustained load
2. **Machine availability** — Ties up the user's primary computer
3. **Power/sleep interruption** — Risk of incomplete runs
4. **Monitoring** — Harder to monitor progress remotely

**Recommendation:** For 24+ hour tasks, use dedicated compute:
- Remote desktop on local network (if available)
- Cloud compute (AWS, GCP, Azure)
- University/institutional HPC (if accessible)

### Cloud Compute Notes

For occasional 24-hour tasks:
- Spot/preemptible instances offer significant savings (60-90% off)
- But risk interruption — only use if analysis can checkpoint/resume
- On-demand instances for critical single-run analyses
- Consider instance with good single-thread performance for R (often not parallelised)

### Local Infrastructure Strategy (Updated 2026-02)

Current setup:
- **Laptop (AMD-tower-ubuntu)** — Docker for quick verification; avoid sustained 24h+ loads
- **Sapphire (Ryzen 9 7900, 12C/24T, 64 GB RAM)** — Primary compute server for long-running
  MCMC and ML tasks. Docker v28.4.0. 558 GB disk free.

Workflow:
1. Docker on laptop for quick verification (<1h tasks)
2. Sapphire for all long-running reproductions (MCMC, simulations)
3. Use detached Docker containers (`docker run -d`) so runs survive SSH disconnects
4. Work on less compute-intensive reproductions in parallel

### Parallel MCMC Strategy (Sapphire)

For analyses with multiple independent model runs (e.g., crema-et-al-2024 with 3 case
studies), run all concurrently in separate Docker containers:

```bash
# Create separate working directories to prevent write conflicts
for run in model-1 model-2 model-3; do
  docker cp temp-extract:/project ~/cc-scratch/project/workdir-${run}
  touch ~/cc-scratch/project/workdir-${run}/.here  # For R `here` package
done

# Launch each in a detached container with volume mount
docker run -d --name mcmc-model1 \
  -v ~/cc-scratch/project/workdir-model1:/project \
  -w /project \
  image:tag Rscript analysis/model1.R
```

**Key considerations:**
- Each container runs 4 MCMC chains at ~100% CPU each → ~400% CPU per container
- 3 containers × 400% = 12 cores used out of 24 available
- Memory is typically modest (~3-6 GB per container for R MCMC)
- Use `docker stats --no-stream` to monitor resource usage
- Detached containers (`-d`) persist through SSH disconnects
- Volume mounts (`-v`) ensure results persist on host filesystem

---

## Pre-computed Results

### When to Use Pre-computed Results

Many repositories include pre-computed outputs (MCMC posteriors, model fits, etc.). These enable:

1. **Quick verification** — Regenerate figures/tables from saved results
2. **Partial reproduction** — Verify output pipeline without full compute
3. **Comparison baseline** — Compare fresh runs against archived outputs

### Verification Levels

| Level | What's Verified | Compute Required |
|-------|-----------------|------------------|
| **Output generation** | Figures/tables from pre-computed | Minutes |
| **Partial reproduction** | One representative analysis | Hours |
| **Full reproduction** | All analyses from raw data | Days |

For initial assessment, output generation verification may be sufficient. Full reproduction reserved for high-stakes verification or when discrepancies found.

---

## Lessons from Specific Papers

### crema-et-al-2024

- **Runtime:** 120-150 hours full pipeline; ~24 hours per MCMC analysis
- **Pre-computed:** Yes — posteriors included in `results/`
- **Dockerfile:** Yes — minor typo to fix (`RColoBrewer` → `RColorBrewer`)
- **Verification strategy:** Three-phase approach:
  1. Quick verification: regenerate figures/table from pre-computed (Phase 1, ~45 min hands-on)
  2. Fresh MCMC: run all 3 case studies in parallel on sapphire (Phase 2, ~24h unattended)
  3. Comparison: quantitative comparison of pre-computed vs fresh (Phase 3, ~1.5h)

**Gotchas discovered during reproduction:**

1. **Missing `rnaturalearthhires` package** — Not included in Dockerfile's `install.packages()`
   call. Required for map figures (Figure 2). Install at runtime:
   ```r
   install.packages("remotes")
   remotes::install_github("ropensci/rnaturalearthhires")
   ```

2. **`.here` sentinel file needed** — When running via Docker volume mounts (not inside the
   Docker image's built-in copy), the `.git` directory is absent, so the `here` R package
   cannot find the project root. Solution: `touch .here` in the working directory.

3. **MCMC output file dependencies** — Post-check scripts must run after MCMC before figures
   can be regenerated from fresh results:
   - `japan_abot.R` → `post_jp_abot.RData`, `ppcheck_jp_abot.RData`
   - `post_check_jp_abot.R` → `ppc_jp_abot.RData` (needed for Figure 3)
   - `britain_abot.R` → `post_gb_abot.RData`, `ppcheck_gb_abot.RData`
   - `post_check_gb_abot.R` → `ppc_gb_abot.RData` (needed for Figure 4)
   - `burial_icar.R` → `post_icar_burial.RData` (no separate post-check needed)

4. **Table 1 determinism** — Table 1 values from pre-computed posteriors are perfectly
   deterministic (identical `diff` against repository original). Fresh MCMC values are
   stochastic but should fall within published 90% HPD intervals.

### marwick-2025

- **Runtime:** ~13 minutes total Docker build (includes render)
- **Pre-computed:** 3 static figure PNGs; pre-committed paper.docx
- **Dockerfile:** Yes — works correctly with zero modifications
- **Dependency management:** renv with 169 CRAN packages pinned in renv.lock
- **Verification strategy:** Single-phase: Docker build renders paper inline
  1. `docker build` does renv restore + rmarkdown::render() (Phase 1+2 combined, ~13 min)
  2. Extract HTML from container, compare statistics and figures (Phase 3, ~7 min)

**Key observations:**

1. **renv vs manual install.packages()** — renv eliminated the package typo and missing
   dependency issues seen in Crema. All 169 packages installed without errors. This is
   a clear advantage of pinned dependency management.

2. **Build-as-render architecture** — The Dockerfile renders the manuscript as a build
   step (`RUN R -e "rmarkdown::render(...)"`), so `docker build` is the complete
   reproduction. This is elegant but means the rendered output is baked into an image
   layer and must be extracted via container start.

3. **R version mismatch (pre-existing)** — renv.lock specifies R 4.5.1 but Docker image
   provides R 4.4.1. This exists in the author's own Dockerfile. renv handles it with
   a warning. Packages installed correctly regardless.

4. **rmarkdown vs Quarto rendering** — The Dockerfile uses `rmarkdown::render()` which
   produces HTML, but the YAML specifies DOCX output. The pre-committed paper.docx was
   likely rendered with `quarto render`. The `rmarkdown` path cannot resolve Quarto-style
   `@fig-label` cross-references (12 broken refs in HTML output). This is a presentation
   artefact, not a computational issue.

5. **Static figure includes** — 3 of 7 figures use `knitr::include_graphics()` to include
   pre-generated PNGs rather than rendering inline. These are necessarily identical between
   original and reproduction. The PCA biplot was hand-edited in SVG for label positioning.

6. **Minor statistical discrepancy** — Kendall's p-value reproduced as 4.08 × 10⁻⁷ vs
   published 2.67 × 10⁻⁶. Both highly significant. Most likely due to minor data revision
   between text drafting and final repository deposit.

**Comparison with Crema:**

| Aspect | Crema et al. 2024 | Marwick 2025 |
|--------|-------------------|--------------|
| Dockerfile modifications | 2 (typo + missing package) | 0 |
| Time to reproduce | ~18h compute + ~3h hands-on | ~13 min compute + ~7 min hands-on |
| Dependency approach | Manual install.packages() | renv.lock (169 packages) |
| Stochastic elements | MCMC → expected variation | GAM → deterministic |
| Statistical discrepancies | 0 (all within HPD) | 1 (p-value, non-material) |

### herskind-riede-2024

- **Runtime:** ~30 seconds (deterministic frequency counts and PMI)
- **Pre-computed:** Yes — S3.xlsx contains bigram, trigram, and quadrigram PMI tables
- **Dockerfile:** None — we constructed one using `rocker/r-ver:4.2.2`
- **Dependency management:** None — 6 packages listed in `library()` calls, no version pinning
- **Verification strategy:** Single-phase: Docker build + batch execution + CSV comparison
  1. Built Docker image with R 4.2.2 and 6 packages (~20 min)
  2. Wrote wrapper script to automate interactive workflow (~15 min)
  3. Executed and compared all 291 n-gram entries against S3.xlsx (exact match)

**Gotchas discovered during reproduction:**

1. **Interactive script design** — S2.R is designed for RStudio with manual re-runs. Part 1
   must be executed 3 times (n=2, 3, 4) with parameter changes, and again for each cultural
   period subset. Lines are conditionally included/excluded by commenting. This required
   writing a wrapper script with a parameterised function.

2. **Proprietary font dependency** — Script specifies `Gill Sans MT` (Monotype, not freely
   available). Falls back to `sans` without computational impact, but exact visual reproduction
   of figures is impossible without purchasing the font.

3. **No output file saving** — Bar plots use interactive `print()` only. Only the heatmap has
   a `ggsave()` call. CSV export uses a generic `_grams.csv` filename that must be manually
   renamed between runs.

4. **Ampersand in filenames** — Original filenames contain `&` (`Herskind&Riede_S1.xlsx`)
   which caused Docker volume mount issues. Renamed for compatibility.

5. **GIMP post-processing** — The published PMI heatmap figure was manually refined in GIMP
   after computational generation. The computational output (matrix values) matches exactly,
   but the publication figure cannot be reproduced without manual intervention.

**Comparison with Crema and Marwick:**

| Aspect | Crema et al. 2024 | Marwick 2025 | Herskind & Riede 2024 |
|--------|-------------------|--------------|----------------------|
| Dockerfile modifications | 2 (typo + missing package) | 0 | N/A (no Dockerfile provided) |
| Time to reproduce | ~18h compute + ~3h hands-on | ~13 min compute + ~7 min hands-on | ~30s compute + ~50 min hands-on |
| Dependency approach | Manual install.packages() | renv.lock (169 packages) | None (6 library() calls) |
| Stochastic elements | MCMC → expected variation | GAM → deterministic | None → exact match |
| Statistical discrepancies | 0 (all within HPD) | 1 (p-value, non-material) | 0 (exact to machine epsilon) |
| Script execution mode | Batch-ready | Literate programming | Interactive (wrapper required) |
| Environment specification | Dockerfile | Dockerfile + renv.lock | R version in paper text only |

**Key lesson: Determinism compensates for missing environment specification.** Despite having
no Docker, no renv, and no session info, the analysis reproduced exactly because all
computations are deterministic (frequency counts and logarithms). For stochastic analyses
(MCMC, bootstrap, etc.), this level of environment under-specification would likely produce
different numerical results. The reproducibility of this paper is a function of its analytical
simplicity rather than its infrastructure practices.

### dye-et-al-2023

- **Runtime:** ~30 seconds (deterministic post-processing of pre-computed MCMC)
- **Pre-computed:** Yes — MCMC output on author's personal server (`tsdye.online/AP/beads-1.csv`)
- **Dockerfile:** None — we constructed one using `rocker/r-ver:4.3.1` (3 iterations)
- **Dependency management:** None — ArchaeoPhases from CRAN, no version pinning
- **Upstream proprietary software:** OxCal 4.4.2 (University of Oxford, not reproduced)
- **Verification strategy:** Single-phase: Docker build + batch execution + exact comparison
  1. Built Docker image with R 4.3.1 and ArchaeoPhases (~15 min, 3 iterations)
  2. Wrote wrapper script from supplement sections (~30 min)
  3. Executed and compared all 54 Allen algebra probability values against Tables 2-10 (exact match)

**Gotchas discovered during reproduction:**

1. **Supplement access barriers** — ScienceDirect returns HTTP 403 for programmatic download.
   The undocumented CDN URL pattern (`ars.els-cdn.com/content/image/1-s2.0-{PII}-mmc1.pdf`)
   works but could change at any time. This is a significant machine-actionability failure —
   supplementary materials should be deposited in an open repository (Zenodo, GitHub, etc.).

2. **MCMC data on personal server** — The MCMC output is hosted on the lead author's personal
   domain (`tsdye.online`), not an institutional or archival repository. Still accessible in
   February 2026, but could become unavailable at any time. The ArchaeoData package provides
   `burials.csv` as an alternative, but it contains different data (different run or format).

3. **Column index shift after `read_oxcal()`** — The supplement specifies column indices
   `c(3:5, 7, 9, 12:78)` based on the raw CSV which includes a "Pass" column. `read_oxcal()`
   drops this column, shifting all indices by -1. Required adjustment to `c(2:4, 6, 8, 11:77)`.
   Both yield the same 72 interments.

4. **Incremental code blocks** — The supplement uses 38 incremental code sections (5.1-5.38)
   with manual list index management, designed for interactive R execution. Assembling these
   into a batch script required careful tracking of positional indices and named list
   construction. Multi-line string literals with embedded newlines (line wrapping in PDF)
   broke column name matching.

5. **Transitive system dependencies** — ArchaeoPhases pulls in `igraph` (needs `libglpk-dev`)
   and `proj4` (needs `libproj-dev`, `libgdal-dev`). Three Docker build iterations needed.

6. **`tempo_plot()` list vs vector** — The `tempo_plot()` function's `name` parameter expects
   a list, not a character vector. Passing `c("name1", "name2")` fails; requires
   `as.list(c("name1", "name2"))`.

**Comparison with previous reproductions:**

| Aspect | Crema 2024 | Marwick 2025 | Herskind 2024 | Dye 2023 |
|--------|-----------|--------------|---------------|----------|
| Dockerfile modifications | 2 (typo + missing pkg) | 0 | N/A (constructed) | N/A (constructed, 3 iterations) |
| Time to reproduce | ~18h compute + ~3h hands-on | ~13 min compute + ~7 min hands-on | ~30s compute + ~50 min hands-on | ~30s compute + ~1.5h hands-on |
| Dependency approach | Manual install.packages() | renv.lock (169 pkgs) | None (6 library() calls) | None (CRAN + r-universe) |
| Stochastic elements | MCMC → expected variation | GAM → deterministic | None → exact match | None (post-processing) → exact match |
| Statistical discrepancies | 0 (all within HPD) | 1 (p-value, non-material) | 0 (exact) | 0 (54/54 exact) |
| Script execution mode | Batch-ready | Literate programming | Interactive (wrapper) | Incremental sections (wrapper) |
| Environment specification | Dockerfile | Dockerfile + renv.lock | R version in text only | None |
| Upstream proprietary software | None | None | None | OxCal 4.4.2 |

**Key lesson: Proprietary upstream software need not block reproduction of analytical
contributions.** The paper's contribution is the ArchaeoPhases methodology (Allen's interval
algebra for archaeological chronology), not the OxCal modelling. Using the authors'
pre-computed MCMC output for post-processing verification is analogous to Phase 1 of the
Crema reproduction (using pre-computed posteriors). The deterministic nature of the
post-processing step means that results are exactly reproducible given fixed MCMC samples,
regardless of R version or platform.

**Key lesson: Data persistence matters.** Hosting critical research data on a personal domain
(`tsdye.online`) rather than an institutional or archival repository introduces a single point
of failure. Similarly, depositing supplements on ScienceDirect rather than an open repository
creates machine-actionability barriers. Both practices are common but undermine long-term
reproducibility.

---

*Last updated: 2026-02-10*
