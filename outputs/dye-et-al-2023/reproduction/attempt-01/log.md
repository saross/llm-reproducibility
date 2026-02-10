# Reproduction Log

## Dye et al. 2023

**Paper:** Dye, T.S., Buck, C.E., DiNapoli, R.J., & Philippe, A. (2023)
"Bayesian chronology construction and substance time."
*Journal of Archaeological Science*, 153, 105765.

### Timeline

| Time | Activity | Duration |
|------|----------|----------|
| 00:00 | Attempted programmatic supplement download | 5 min |
| 00:05 | Downloaded supplement PDF (820 KB) from ScienceDirect CDN | 2 min |
| 00:07 | Read supplement (50 pages): OxCal model, bead mappings, R code | 20 min |
| 00:27 | Downloaded MCMC CSV from author's server (3.7 MB) | 1 min |
| 00:28 | Wrote Dockerfile (rocker/r-ver:4.3.1 + ArchaeoPhases) | 5 min |
| 00:33 | Wrote run-analysis.R wrapper script (477 lines) | 30 min |
| 00:63 | Docker build attempt 1 — missing libglpk | 5 min |
| 00:68 | Docker build attempt 2 — missing libproj | 5 min |
| 00:73 | Docker build attempt 3 — successful | 5 min |
| 00:78 | First run — occurrence plot column index error | 3 min |
| 00:81 | Second run — bead list name alignment errors | 10 min |
| 00:91 | Third run — tempo plot name/position list mismatch | 3 min |
| 00:94 | Fourth run — **complete success** | 2 min |
| 00:96 | Verified all outputs against published values | 15 min |
| 01:11 | Wrote documentation | 20 min |
| **Total** | | **~1.5 hours** |

### Modifications Required

1. **Dockerfile construction** (3 iterations):
   - The paper provides no Dockerfile or environment specification
   - Built from `rocker/r-ver:4.3.1` with ArchaeoPhases from CRAN
   - Required adding `libglpk-dev`, `libproj-dev`, `libgdal-dev` for
     transitive dependencies (igraph, proj4)

2. **Column index adjustment**:
   - Supplement specifies `burial.dates <- c(3:5, 7, 9, 12:78)` for raw CSV
   - `read_oxcal()` drops the "Pass" column, shifting indices by -1
   - Adjusted to `c(2:4, 6, 8, 11:77)` — yields identical 72 interments

3. **MCMC data source**:
   - Supplement code reads from `https://tsdye.online/AP/beads-1.csv`
   - Downloaded local copy for reproducibility
   - Remote URL confirmed still accessible (February 2026)

4. **Bead list assembly**:
   - Supplement uses incremental code blocks (sections 5.1-5.38) with manual
     list index management
   - Wrapper script uses named list construction and `$` access for robustness
   - All 23 bead types validated against MCMC column names

### Outputs Generated

| File | Description | Size |
|------|-------------|------|
| `outputs/occurrence-plot.pdf` | 72-interment occurrence plot (Paper Figure 7) | 12.7 KB |
| `outputs/tempo-plots.pdf` | 23 bead type tempo plots (Paper Figure 8) | 95.1 KB |
| `outputs/summary-stats.txt` | All Allen algebra probability values | 7.8 KB |
| `run.log` | Complete execution log | ~12 KB |

### FAIR/Machine-Actionability Findings

1. **Supplement access**: ScienceDirect blocks programmatic access (HTTP 403).
   The direct CDN URL pattern (`ars.els-cdn.com/content/image/1-s2.0-{PII}-mmc1.pdf`)
   worked, but this is an undocumented URL pattern that could change. Depositing
   in Zenodo or GitHub would be more reliable.

2. **MCMC data on personal server**: The MCMC output is hosted on the lead
   author's personal domain (`tsdye.online`), not an institutional or archival
   repository. This URL could become unavailable at any time. The ArchaeoData
   package provides `burials.csv` as a more persistent alternative, but it
   contains different data (appears to be a different run or format).

3. **No environment specification**: No Dockerfile, no renv.lock, no R version
   specified. Required three Docker build iterations to resolve transitive
   dependencies.
