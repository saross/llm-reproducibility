# Marwick 2025 — Reproduction Environment

## Paper

**Title:** Is Archaeology a science? Insights and imperatives from 10,000 articles
and a year of reproducibility reviews

**Authors:** Ben Marwick

**Journal:** Journal of Archaeological Science, 180, 106281

**DOI:** 10.1016/j.jas.2025.106281

**Repository:** <https://github.com/benmarwick/web-of-science-archaeology>

**Zenodo DOI:** 10.5281/zenodo.14897252

## Original Environment

| Component | Version/Details |
|-----------|----------------|
| Docker base image | `rocker/verse:4.4.1` |
| R version (renv.lock) | 4.5.1 |
| R version (container) | 4.4.1 (from rocker/verse tag) |
| Dependency management | renv (169 packages, all from CRAN) |
| CRAN repository | Posit Package Manager (`https://packagemanager.posit.co/cran/latest`) |
| Render engine | `rmarkdown::render()` (called during `docker build`) |
| Output format | DOCX (via `reference-doc: templates/template.docx`) |
| Quarto filters | scholarly-metadata.lua, author-info-blocks.lua, pagebreak.lua |
| CSL style | journal-of-archaeological-science.csl |

## R Version Mismatch Note

The renv.lock specifies R 4.5.1 but the Docker base image is `rocker/verse:4.4.1`.
This is likely because the lockfile was generated on the author's local R 4.5.1
installation, while the Docker image uses 4.4.1. renv will use the container's R
version (4.4.1) and install packages from the lockfile regardless. This is a minor
discrepancy that should not affect results — renv pins package versions, not R versions.

## Key Packages (from renv.lock)

### Analysis

- **tidyverse** (meta-package: dplyr, ggplot2, tidyr, readr, purrr, stringr, forcats, tibble)
- **mgcv** — Generalised Additive Models (GAM) for temporal trends
- **brms** — Bayesian Regression Models using Stan (present in lockfile; used in supplement)
- **rstan** + **StanHeaders** — Stan backend for brms
- **irr** — Inter-rater reliability (Kendall's W)
- **confintr** — Confidence intervals

### Visualisation

- **ggplot2**, **cowplot**, **patchwork** — Plot composition
- **ggridges** — Ridge plots for journal distributions
- **ggrepel** — Non-overlapping text labels
- **ggpmisc** — Statistical annotations on plots
- **viridisLite** — Colour palettes
- **svglite** — SVG output

### Other

- **here** — Project-relative file paths
- **knitr**, **rmarkdown** — Document rendering
- **kableExtra** — Table formatting

## Repository Structure

```text
web-of-science-archaeology/
├── Dockerfile                          # Build + render in single step
├── renv.lock                           # 169 packages pinned
├── .Rprofile                           # renv activation
├── renv/
│   ├── activate.R                      # renv bootstrap
│   └── settings.json                   # renv config
├── analysis/
│   ├── code/
│   │   ├── 000-import-raw-data.R       # Raw WoS data processing
│   │   └── 001-redraw-Fanelli-and-Glanzel-Fig-2.R  # Comparison data
│   ├── data/
│   │   ├── wos-data-df.rds             # 9,697 articles (processed)
│   │   ├── JAS AER data analysis.csv   # Reproducibility review data
│   │   ├── BenMarwick_JCR_JournalResults_12_2024.csv  # Journal metrics
│   │   └── savedrecs (1-58).txt        # Raw WoS exports (58 files)
│   ├── figures/
│   │   ├── fig-smooth-plots-paper.png  # Pre-generated GAM figure (Fig 3)
│   │   ├── plot_pca_means.png          # PCA biplot (Fig 4)
│   │   ├── plot_pca_means.svg          # PCA biplot source SVG
│   │   ├── plot_pca_means-edited-by-hand.svg  # Hand-edited PCA labels
│   │   └── simple-reproducibility-checklist.png  # Checklist (Fig 6)
│   └── paper/
│       ├── paper.qmd                   # Main manuscript (84 KB, ~1108 lines)
│       ├── paper.docx                  # Pre-rendered output (7 MB)
│       ├── references.bib              # Bibliography (51 KB)
│       ├── supplement-GAMS-details.qmd # Supplement document
│       ├── supplement-GAMS-details.html  # Pre-rendered supplement
│       └── templates/                  # DOCX template, Lua filters, CSL
├── .github/workflows/
│   └── render-qmd-in-docker.yml        # CI: just runs docker build
├── README.md / README.Rmd
├── CONDUCT.md / CONTRIBUTING.md / LICENSE.md
└── web-of-science-archaeology.Rproj
```

## Pipeline Architecture

### Build-as-Render Design

The Dockerfile performs both dependency installation and document rendering in a
single `docker build`:

1. `FROM rocker/verse:4.4.1` — Base image with R, RStudio, pandoc, TinyTeX
2. `COPY . $PROJ_DIR` — Copy entire repository into container
3. `R -e "install.packages('renv')"` — Install renv
4. `R -e "renv::restore()"` — Restore all 169 packages from lockfile
5. `R -e "rmarkdown::render('analysis/paper/paper.qmd')"` — Render manuscript

The CI workflow (`render-qmd-in-docker.yml`) simply runs `docker build`, confirming
this is the intended execution path.

### Figures: Dynamic vs Static

| Figure | Label | Type | Source |
|--------|-------|------|--------|
| Fig 1 | fig-compare-other-fields | **Dynamic** | Generated inline (cowplot grid of 5 boxplots) |
| Fig 2 | fig-change-over-time_from_V1_1 | **Dynamic** | Generated inline (GAM scatter + smooth) |
| Fig 3 | fig-change-over-time | **Static** | `knitr::include_graphics("fig-smooth-plots-paper.png")` |
| Fig 4 | fig-pca | **Static** | `knitr::include_graphics("plot_pca_means.png")` |
| Fig 5 | fig-variation-by-journal | **Dynamic** | Generated inline (6-panel ridge + Borda) |
| Fig 6 | fig-aer-summary | **Dynamic** | Generated inline (5-panel AER summary) |
| Fig 7 | fig-checklist | **Static** | `knitr::include_graphics("simple-reproducibility-checklist.png")` |

**Note:** The "fig-change-over-time" figure (Fig 3 in published paper) is included
as a pre-generated PNG from the supplement GAM analysis, not rendered dynamically.
The PCA biplot was generated then hand-edited in SVG for label spacing. The checklist
is a Canva-designed infographic.

### Code Chunks in paper.qmd

| Chunk | Lines | Purpose | Key Outputs |
|-------|-------|---------|-------------|
| 1 (unlabelled) | 62-91 | Load WoS data, compute basic counts | `n_articles`, `n_journals` |
| 2 (unlabelled) | 101-408 | Five bibliometric boxplots + Shannon index | Plot objects |
| 3 (`fig-compare-other-fields`) | 410-428 | **Fig 1**: Cowplot grid of boxplots | Figure |
| 4 (unlabelled) | 434-502 | Temporal trend data + linear models | `over_time_long_colour` |
| 5 (`fig-change-over-time_from_V1_1`) | 504-568 | **Fig 2**: GAM scatter plots | Figure |
| 6 (`fig-change-over-time`) | 570-578 | **Fig 3**: Include pre-generated GAM PNG | Static image |
| 7 (unlabelled) | 586-706 | Journal metrics, PCA, loadings | PCA objects |
| 8 (unlabelled) | 709-769 | Kendall's W, Borda Count | Test statistics |
| 9 (unlabelled) | 772-866 | Five ridge plots | Plot objects |
| 10 (`fig-variation-by-journal`) | 868-885 | **Fig 5**: 6-panel journal variation | Figure |
| 11 (`fig-pca`) | 887-893 | **Fig 4**: Include pre-generated PCA PNG | Static image |
| 12 (unlabelled) | 919-1031 | AER data: software, methods, issues | Plot objects |
| 13 (`fig-aer-summary`) | 1034-1041 | **Fig 6**: 5-panel AER summary | Figure |
| 14 (`fig-checklist`) | 1067-1074 | **Fig 7**: Include checklist PNG | Static image |

## Verification Targets

### Key Statistics (from paper text)

| Statistic | Published Value | Location in paper.qmd |
|-----------|----------------|-----------------------|
| Total articles | ~9,697 | Line 93 (inline R: `n_articles`) |
| Journals | 20 | Line 93 (inline R: `n_journals`) |
| Time span | 1975-2025 | Line 93 |
| Kendall's W | "moderate to strong" | Line 895 |
| Kendall's p-value | 2.67 × 10⁻⁶ | Line 895 (inline R: `pretty_print_sci()`) |
| PC1 variance explained | Extract from output | Line 901 |
| Reproducibility reviews | 25 manuscripts | Line 1043 |
| Published from reviews | 11 | Line 1043 |
| First-try success | 4 of 7 | Line 1043 |

### Figures to Verify

All dynamically generated figures should match the pre-rendered paper.docx.
Static figures (Fig 3, 4, 7) are exact includes from PNGs so will be identical.

## Reproduction Environment

| Component | Version |
|-----------|---------|
| Host OS | Ubuntu (local Docker) |
| Docker Engine | (check at build time) |
| Docker image built | (record timestamp) |
| Build duration | (record) |
| Render duration | (included in build) |

## Differences from Crema Reproduction

| Aspect | Crema et al. 2024 | Marwick 2025 |
|--------|-------------------|--------------|
| Analysis type | 3 independent MCMC scripts | Single Quarto document |
| Runtime | ~5-9 hours per analysis | Minutes |
| Dependency management | Manual `install.packages()` | renv.lock (169 packages) |
| Pre-computed results | Yes (RData posteriors) | No (code IS the paper) |
| Comparison method | Parameter medians within HPD | Figures + exact statistics |
| Compute needed | Sapphire (parallel Docker) | Local Docker |
| Stochastic elements | MCMC sampling | Minimal (GAM fitting) |
| Build = Render? | No (separate steps) | Yes (render during build) |
| Static figures | None | 3 of 7 (pre-generated PNGs) |
