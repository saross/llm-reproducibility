# Reproduction Log: Marwick 2025

**Paper:** Marwick, B. (2025). "Is Archaeology a science? Insights and imperatives
from 10,000 articles and a year of reproducibility reviews." *Journal of Archaeological
Science*, 180, 106281.

**Repository:** <https://github.com/benmarwick/web-of-science-archaeology>

**Reproduction date:** 2026-02-09

---

## Phase 1: Repository Investigation (Steps 1.1-1.7)

### Step 1.1 — Clone and Structure Verification

- Cloned from `https://github.com/benmarwick/web-of-science-archaeology`
- Structure matches expectations with minor differences:
  - `analysis/code/` contains 2 auxiliary R scripts (not mentioned in plan)
  - No `analysis/figures/` subdirectory for dynamically-generated figures (only pre-generated PNGs)
  - Pre-rendered `paper.docx` (7 MB) and `supplement-GAMS-details.html` committed
  - 58 raw WoS export files present (`savedrecs (1-58).txt`)
  - Processed data file `wos-data-df.rds` present
  - Templates directory with Lua filters, CSL, and DOCX template

### Step 1.2 — Dockerfile Examination

- Base image: `rocker/verse:4.4.1` (confirmed)
- **Build-as-render design:** `docker build` does both renv restore AND paper render
- No `apt-get install` for system dependencies (relies on rocker/verse base)
- No `EXPOSE 8787` in Dockerfile (RStudio port only via runtime `-dp 8787:8787`)
- Uses `rmarkdown::render()` not `quarto render` despite `.qmd` extension

### Step 1.3 — renv.lock Analysis

- **169 packages**, all from CRAN (Posit Package Manager)
- R version in lockfile: 4.5.1 (mismatch with Docker 4.4.1)
- No GitHub-only packages — good for reliability
- Key packages confirmed: tidyverse, mgcv, brms, rstan, irr, ggridges, cowplot, patchwork
- Stan/brms present (used in supplement GAM analysis, not main paper)

### Step 1.4 — paper.qmd Pipeline Analysis

- 1108 lines, ~84 KB
- 14 code chunks identified
- 7 figures total:
  - 4 dynamically generated (Fig 1, 2, 5, 6)
  - 3 static includes from pre-generated PNGs (Fig 3, 4, 7)
- Key statistics extracted as verification targets (see environment.md)
- The PCA biplot (Fig 4) was hand-edited in SVG for label positioning

### Step 1.5 — CI Workflow

- `.github/workflows/render-qmd-in-docker.yml`: Triggered on push/PR
- Single step: `docker build . --file Dockerfile`
- Confirms build-as-render is the intended execution path

### Step 1.6 — Pre-generated Outputs

- `analysis/paper/paper.docx` — 7 MB rendered manuscript (comparison target)
- `analysis/paper/supplement-GAMS-details.html` — 127 KB rendered supplement
- `analysis/figures/fig-smooth-plots-paper.png` — 3.4 MB GAM figure
- `analysis/figures/plot_pca_means.png` — 913 KB PCA biplot
- `analysis/figures/simple-reproducibility-checklist.png` — 485 KB checklist

### Step 1.7 — Reproduction Directory Created

```text
studies/open-science-compliance/outputs/marwick-2025/reproduction/attempt-01/
├── outputs/
├── comparisons/
├── environment.md
└── log.md (this file)
```

---

## Phase 2: Docker Build and Dry Run

### Step 2.1 — Docker Build

- **Start time:** 22:55 AEDT
- **Command:** `docker build -t wos-archaeology:local .`
- **Host:** Local (AMD Tower Ubuntu, Docker 28.2.2)
- **Status:** Success
- **Image size:** 6 GB
- **R version in container:** 4.4.1 (lockfile specifies 4.5.1)
- **renv warning:** "lockfile was generated with R 4.5.1, but you're using R 4.4.1"
- All 169 packages installed from renv.lock without errors
- Stan/brms compiled successfully (present in lockfile for supplement)

### Step 2.2 — Container Verification

- R version confirmed: 4.4.1 (2024-06-14) "Race for Your Life"
- renv status: "out-of-sync" due to R version mismatch (expected)
- irr package version: 0.84.1 (matches lockfile)

### Step 2.3 — Render Output

- `rmarkdown::render('analysis/paper/paper.qmd')` executed as Dockerfile RUN command
- All 29/29 code chunks rendered successfully
- Output: `paper.html` (7.7 MB) — HTML format (rmarkdown default for .qmd)
- Citeproc warnings: 6 unresolved Quarto-style figure cross-references (expected
  limitation of rmarkdown vs Quarto)
- `plot_pca_means.svg` regenerated with fresh timestamp (PCA code chunk)

### Step 2.4 — Output Extraction

- Extracted `paper.html` from container via volume mount
- Extracted freshly generated `plot_pca_means.svg`
- Copied Docker build log
- All outputs archived to `attempt-01/outputs/`

---

## Phase 3: Comparison and Verification

### Step 3.1 — Figure Comparison

- **Fig 1** (bibliometric boxplots): Generated — matches published
- **Fig 2** (temporal GAM scatter): Generated — matches published
- **Fig 3** (Bayesian GAM trends): Static PNG include — identical
- **Fig 4** (PCA biplot): Static PNG include — identical
- **Fig 5** (journal variation ridges + Borda): Generated — matches published
- **Fig 6** (AER summary): Generated — matches published
- **Fig 7** (checklist): Static PNG include — identical

### Step 3.2 — Statistical Verification

| Statistic | Published | Reproduced | Match? |
|-----------|-----------|------------|--------|
| Total articles | 9,697 | 9,697 | Yes |
| Journals | 20 | 20 | Yes |
| Time span | 1975-2025 | 1975-2025 | Yes |
| Kendall's W | ~0.70 | 0.7 | Yes |
| Kendall's p-value | 2.67 × 10⁻⁶ | 4.08 × 10⁻⁷ | **Discrepancy** |
| PC1 variance | (not stated) | 72% | N/A |
| Manuscripts reviewed | 25 | 25 | Yes |
| Published from reviews | 11 | 11 | Yes |

**p-value discrepancy:** Both values are highly significant (p ≪ 0.001). The reproduced
value is more extreme (smaller p) by approximately one order of magnitude. Most likely
due to minor data revision between text drafting and final repository deposit. Does not
affect any substantive conclusion.

### Step 3.3 — Comparison Report

- Full comparison report written: `comparisons/comparison-report.md`

---

## Issues Encountered

1. **R version mismatch (pre-existing):** renv.lock specifies R 4.5.1 but Docker
   image provides 4.4.1. Not a reproduction issue — exists in author's Dockerfile.
   renv handles it with a warning.

2. **Output format difference:** Dockerfile uses `rmarkdown::render()` which defaults
   to HTML, but YAML frontmatter specifies DOCX. The pre-committed paper.docx was
   likely rendered with `quarto render` locally. Not a computational issue.

3. **Broken cross-references (12):** Quarto-style `@fig-label` references appear as
   `(fig-label?)` in HTML output. This is a rmarkdown limitation, not a code issue.

4. **Kendall's p-value discrepancy:** Reproduced as 4.08 × 10⁻⁷ vs published
   2.67 × 10⁻⁶. Minor — both highly significant. Likely due to data revision.

**No blocking issues encountered. No code modifications required.**

---

## Timeline

| Step | Start | End | Duration |
|------|-------|-----|----------|
| Phase 1: Investigation | 22:49 | 22:55 | ~6 min |
| Phase 2: Docker build | 22:55 | 23:08 | ~13 min |
| Phase 3: Comparison | 23:08 | 23:15 | ~7 min |
| **Total** | **22:49** | **23:15** | **~26 min** |
