# Environment Specification

## Herskind and Riede (2024) Reproduction — attempt 02

Run `phase2-shakedown-2026-10`; executor `reproduction-executor v1.1`
(`claude-opus-5-5`, effort high). Launch commit
`e5f35543c07d2a9314d1742ff34df40a12bd35fd`.

### Software Versions

| Component | Version | Source |
|-----------|---------|--------|
| R | 4.3.2 (2023-10-31) | `rocker/r-ver:4.3.2` Docker image |
| quanteda | 3.3.1 | Posit Package Manager (P3M) snapshot `jammy/2024-02-28` (binary) |
| readxl | 1.4.3 | P3M snapshot 2024-02-28 |
| ggplot2 | 3.5.0 | P3M snapshot 2024-02-28 |
| dplyr | 1.1.4 | P3M snapshot 2024-02-28 |
| data.table | 1.15.0 | P3M snapshot 2024-02-28 |
| forcats | 1.0.0 | P3M snapshot 2024-02-28 |
| extrafont | 0.19 | P3M snapshot 2024-02-28 |
| Docker base | `rocker/r-ver:4.3.2` (`sha256:4e32addfc4da3e660f6e0d05ce5e43d3eceb9db58a60b9a142e0dde9a654ead1`) | Docker Hub |
| Built image | `llmr-herskind-riede-2024-attempt-02` (`sha256:2d31bf850733e9bfaa59bf5d75eb8011c0c71e143e2570732e07449a0c82f0c1`, 931 MB) | Local build |
| Container OS | Ubuntu 22.04.4 LTS | Base image |
| Host | Linux 6.14.0-37-generic, Docker 29.2.1, 16 threads | Local execution (hostname `AMD-tower-ubuntu`) |

All seven README pins and the R version are asserted during `docker build`; a
mismatch fails the build. The assertion passed on the first build. The full
`sessionInfo()` is in `outputs/session-info.txt`.

### System Dependencies Added to Docker

- `fontconfig`, `fonts-dejavu-core` — an open fallback font. The authors'
  ggplot themes request "Gill Sans MT", a proprietary Monotype font that is not
  distributed with the deposit. A fontconfig alias maps that family name to
  DejaVu Sans. This affects typography only.
- `libcairo2`, `libfreetype6`, `libpng16-16` — the cairo-backed `png()` device
  that `ggsave()` uses in a headless container.
- Locale `C.UTF-8` (`LANG`, `LC_ALL`) — S2.R contains the non-ASCII identifier
  `ertebølledata` and the string literal `"Ertebølle"`.

### R Package Dependencies (Automatic)

quanteda 3.3.1 pulls in, among others:

- `stringi` 1.8.3 — tokenisation (International Components for Unicode (ICU)
  based)
- `RcppParallel` 5.1.7 — parallel n-gram construction (deterministic output)
- `Matrix` 1.6-1.1 — sparse document-feature matrices
- `fastmatch` 1.1-4 and `stopwords` 2.3

extrafont 0.19 pulls in `Rttf2pt1` 1.3.12 and `extrafontdb` 1.0.

### Data Source(s)

- **Files:** `Herskind&Riede_S1.xlsx` (442,983 bytes), `Herskind&Riede_S2.R`
  (33,834 bytes), `Herskind&Riede_S3.xlsx` (31,598 bytes), and `README.txt`
  (1,704 bytes). All are stored verbatim in `data/`.
- **Source:** Zenodo record 10.5281/zenodo.10801706, version 2 (2024-03-10),
  through the Zenodo files Application Programming Interface (API). Open
  HTTPS, no authentication. Version 1 (10.5281/zenodo.10623550) and the concept
  DOI were not used (run note AP-12).
- **Format:** S1 sheet `Data` holds 483 objects × 290 columns. Column 11 is
  `Chronology`, 13–14 are the coordinates, and 15 is `Motifs_as_text`. Columns
  31–289 are the motif indicators A1 to ZOO, and column 290 is `Total`. S3 has
  three sheets (165 / 106 / 20 skipgram rows).
- **Data-availability level:** L1 (open-complete; see `log.md`).

#### Data Availability Inventory

| Dataset | Records | Source | Level | Available? |
|---------|---------|--------|-------|------------|
| S1 motif presence/absence data | 483 objects | Zenodo 10.5281/zenodo.10801706 v2 | L1 | Yes |
| Płonka (2003) analogue catalogue (upstream of S1) | — | Monograph | not retrieved (outside computational scope) | n/a |
| Fig. 2 / Fig. 5 base maps and Fig. 5 motif-extent layers | — | No source stated | not a dataset enumerated by the paper | No |

**Overall availability:** 1/1 datasets enumerated in the paper's data
availability statement and methods (100%), 483/483 records.

### Upstream Software (Not Reproduced)

- **GIMP** (free software) was used by the authors to composite and annotate
  Fig. 3 and Fig. 4: panel assembly, coloured boxes, and motif drawings. No
  GIMP project files are deposited. The R skeletons were reproduced; the boxes
  were checked with verification aids.
- **Microsoft Word / Excel** were used to hand-transcribe Tables 1 and 2 from
  the R console and to assemble S3 from the Part 8 CSVs. The R outputs were
  reproduced.
- **The Fig. 2 map panel and Fig. 5** were made in unstated mapping software.
  No code or layers are deposited.

### Notes

- **R version:** 4.3.2, as stated in the deposit README (the deposit version
  of record per AP-12 and approval ruling 4). The paper text (p. 3) states R
  v.4.2.2. That conflict is recorded as a finding; the reproduction matched to
  machine precision on 4.3.2, so no diagnostic 4.2.2 run was needed.
- **Determinism:** the analysis uses no random number generation. Two
  independent container runs (12:06 and 12:15 UTC) produced byte-identical
  outputs. The only exceptions were `console-plots.pdf`, which embeds a
  creation timestamp, and the completion-time line in `run-console.log`.
- **Pins:** the base image's frozen P3M snapshot (2024-02-28) resolved every
  README version exactly, so `remotes::install_version` was not needed.
- **Environment-specification level (paper):** 2. The README gives an R
  version and exact package versions as a list, with no lockfile, container,
  or `sessionInfo()`.
