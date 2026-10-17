# Environment Specification

## Herskind and Riede 2024 Reproduction (attempt 04)

Paper: Herskind, L.L.P. and Riede, F. (2024). A computational linguistic
methodology for assessing semiotic structure in prehistoric art and the
meaning of southern Scandinavian Mesolithic ornamentation. *Journal of
Archaeological Science* 165, 105969. Available online 3 April 2024.

### Software Versions

| Component | Version | Source |
|-----------|---------|--------|
| R | 4.3.2 (2023-10-31) | `rocker/r-ver:4.3.2` Docker image (pin from the deposit README) |
| quanteda | 3.3.1 | CRAN archive tarball (pinned) |
| readxl | 1.4.3 | CRAN archive tarball (pinned) |
| ggplot2 | 3.5.0 | CRAN archive tarball (pinned) |
| dplyr | 1.1.4 | CRAN archive tarball (pinned) |
| data.table | 1.15.0 | CRAN archive tarball (pinned) |
| forcats | 1.0.0 | CRAN archive tarball (pinned) |
| extrafont | 0.19 | CRAN archive tarball (pinned) |
| Docker base | `rocker/r-ver:4.3.2` (local image id `f0b4e058dcfa`; Ubuntu 22.04.4 LTS) | Docker Hub |
| Built image | `llmr-herskind-riede-2024-attempt-04`, `sha256:d333d7285568e4ac204b94a7dc2da7128d0c728c6e0ef3d9ca24a16b53ee7548` | `reproduction-lane.py build-image` (build-01) |
| Host | AMD-tower-ubuntu (Linux 6.14), 16 CPUs | Local execution through `run-container`; nothing sent to sapphire |

**Environment-specification level of the paper: 2** (an unpinned dependency
list in the scale's terms: the README names R and package versions, but there
is no lockfile and no container specification). The paper's own methods text
gives a different R version (4.2.2) and no package versions. The plan uses the
README's R 4.3.2, the approver accepted that choice, and the R 4.3.2 pin agrees
with the listed package versions (ggplot2 3.5.0 was released in February 2024).

**Pins honoured: in full, with 0 fallbacks.** All seven README pins built at
their supplied versions on the first attempt (build log
`lane-records/build-01/build.log`; per-attempt record
`outputs/run-05/files/captured/pin-attempts.csv`).

### Package repository dates

The authors supplied no container, so the base image was the reproducer's
choice. `rocker/r-ver:4.3.2` points R's `repos` at a Posit Package Manager
snapshot dated 2024-02-28 (the image's own date). That date was overridden:

| Use | URL | Date |
|-----|-----|------|
| Pinned versions and their release history | `https://cloud.r-project.org` (`src/contrib/` and `src/contrib/Archive/<pkg>/`) | Not a snapshot: the exact pinned tarballs |
| Packages the authors left unspecified | `https://packagemanager.posit.co/cran/__linux__/jammy/2024-04-03` | 2024-04-03, the article's first online appearance |
| The image's built-in snapshot (not used) | `https://p3m.dev/cran/__linux__/jammy/2024-02-28` | 2024-02-28 |

The snapshot served source tarballs (`/src/contrib/`), which were compiled
in the image. `install-pins.R` asserted that every snapshot-installed package
matches the snapshot's own version, and that every pin is installed at its
pinned version.

### Installed package inventory

The full machine-readable inventory, with status per package, is
`outputs/run-05/files/captured/package-inventory.csv`.

- **Pinned (7):** data.table 1.15.0, dplyr 1.1.4, extrafont 0.19, forcats
  1.0.0, ggplot2 3.5.0, quanteda 3.3.1, readxl 1.4.3.
- **Fallback (0):** none.
- **Unspecified, from the 2024-04-03 snapshot (44):** cellranger 1.1.0, cli
  3.6.2, colorspace 2.1-0, cpp11 0.4.7, crayon 1.5.2, extrafontdb 1.0, fansi
  1.0.6, farver 2.1.1, fastmatch 1.1-4, generics 0.1.3, glue 1.7.0, gtable
  0.3.4, hms 1.1.3, isoband 0.2.7, ISOcodes 2024.02.12, jsonlite 1.8.8,
  labeling 0.4.3, lifecycle 1.0.4, magrittr 2.0.3, munsell 0.5.1, pillar
  1.9.0, pkgconfig 2.0.3, prettyunits 1.2.0, progress 1.2.3, R6 2.5.1,
  RColorBrewer 1.1-3, Rcpp 1.0.12, RcppArmadillo 0.12.8.1.0, RcppParallel
  5.1.7, rematch 2.0.0, rlang 1.1.3, Rttf2pt1 1.3.12, scales 1.3.0, SnowballC
  0.7.1, stopwords 2.3, stringi 1.8.3, tibble 3.2.1, tidyselect 1.2.1, utf8
  1.2.4, vctrs 0.6.5, viridisLite 0.4.2, withr 3.0.0, xml2 1.3.6, yaml 2.3.8.
- **Unspecified, shipped with R 4.3.2 (15 recommended packages):** boot
  1.3-28.1, class 7.3-22, cluster 2.1.4, codetools 0.2-19, foreign 0.8-85,
  KernSmooth 2.23-22, lattice 0.21-9, MASS 7.3-60, Matrix 1.6-1.1, mgcv 1.9-0,
  nlme 3.1-163, nnet 7.3-19, rpart 4.1.21, spatial 7.3-17, survival 3.5-7.
- **Unspecified, carried by the base image (2):** docopt 0.7.1, littler
  0.3.19 (rocker tooling; not loaded by the analysis).

### System Dependencies Added to Docker

The base rocker image required the following additional system libraries
(from Ubuntu 22.04's floating apt archive, which pins no date):

- `build-essential`, `gfortran` — compilers for the pinned source tarballs
  and the snapshot's source packages (quanteda, data.table, readxl, dplyr,
  stringi, RcppArmadillo, and others are compiled code)
- `libicu-dev` — ICU, for stringi (a quanteda dependency)
- `libxml2-dev` — for xml2 (a quanteda dependency)
- `libcurl4-openssl-dev`, `libssl-dev`, `zlib1g-dev` — downloads and
  compression during the build
- `libfontconfig1`, `libfreetype6`, `libcairo2`, `fonts-liberation`,
  `fonts-dejavu-core` — the cairo PNG device and fonts to render text. The
  proprietary Gill Sans MT font that S2.R names is not available, so text
  renders in a substitute font.

### R Package Dependencies (Automatic)

quanteda 3.3.1 pulls in stringi, Rcpp, RcppParallel, RcppArmadillo,
fastmatch, SnowballC, stopwords, ISOcodes, xml2, yaml, and jsonlite.
ggplot2 3.5.0 pulls in gtable, isoband, scales (with farver, labeling,
munsell, colorspace, RColorBrewer, viridisLite), and the tidyverse core
(rlang, vctrs, cli, glue, lifecycle, tibble, pillar, withr). readxl 1.4.3
pulls in cellranger and cpp11. extrafont 0.19 pulls in extrafontdb and
Rttf2pt1.

### Data Source(s)

- **File:** `deposit/Herskind&Riede_S1.xlsx` (442,983 bytes; sha256
  `d76b9d6328465658aa1582c5c8de0912f9167ff1f8c737bd7998d91fd5692030`)
- **Source:** Zenodo record 10801706
  (<https://doi.org/10.5281/zenodo.10801706>), the version named in the
  paper's data availability statement and selected by AP-12; unauthenticated
  HTTPS download from the Zenodo REST interface; md5 matched Zenodo's
  published `0bcde6d178b5a8f3da80a023a64ff510`
- **Format:** sheet `Data`, 483 numbered object rows (the sheet's range runs
  to row 505 with empty trailing rows), 290 columns (metadata in A-N, motif
  presence/absence in AE-KC = columns 31-289, a Total column); sheet `Legend`
  documents the columns
- **Access level:** L1 (open repository, direct download, no barrier)

#### Data Availability Inventory

| Dataset | Records | Source | Access Level | Available? |
|---------|---------|--------|--------------|------------|
| S1 analysis dataset (South Scandinavian objects digitised from Plonka 2003) | 483 objects | Zenodo 10.5281/zenodo.10801706 | L1 | Yes |

**Overall availability:** 1/1 datasets (100% by dataset), 483/483 records
(100% by records).

### Upstream Software (Not Reproduced)

- **GIMP** (free image editor) — the authors combined the six Fig. 3 panels,
  added the Fig. 4 boxes, motif drawings, and axis edits, and composed the
  final figures in GIMP. These edits are manual and have no code; they were
  compared against verification aids.
- **Unnamed GIS software** — the Fig. 2 map and Fig. 5 map (with its
  motif-extent patches) have no code; the README says the S1 coordinate
  columns were used for Fig. 2.

### Notes

- **R version.** R 4.3.2 is the deposit README's pin; the paper's methods
  text says R 4.2.2. The approver accepted 4.3.2 (plan approval note,
  2026-10-13).
- **Determinism.** The whole analysis is deterministic: skipgram counting,
  PMI, and subsetting involve no random numbers, so exact matches are
  expected.
- **Locale.** `LANG`/`LC_ALL` = `C.UTF-8`, so the non-ASCII identifier
  `ertebølledata` and the factor level "Ertebølle" parse and match.
- **Graphics.** The run's default device is a cairo PNG device (see
  `log.md`, modifications); `ggsave()` writes the authors' PNGs with its own
  device. `capabilities("cairo")` is TRUE in the image.
- **Fonts.** `font_import(pattern = "GIL", prompt = FALSE)` (S2.R line 27)
  failed as expected ("arguments imply differing number of rows: 0, 1") and
  was tolerated as declared; it registers fonts and computes nothing.
