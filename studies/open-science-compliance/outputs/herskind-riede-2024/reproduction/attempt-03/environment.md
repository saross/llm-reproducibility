# Environment Specification

## Herskind and Riede 2024 Reproduction (attempt 03)

Run `gate-1-3-pilot-rerun-2026-10`; launch commit
`cd5d54ac890fafc9061547694c7d0fad9c065912`; executor reproduction-executor v1.6
(`claude-opus-5-5`). All execution went through the lane's `run-container`
(Docker, networking off, non-root user); the credited run is `run-04`.

### Environment-specification level (the paper's)

**Level 2: unpinned dependency list.** On the ordinal scale of
verdicts-and-precision v1.1 (§7.5), the deposit's `README.txt` gives the R
version (4.3.2) and exact versions for seven packages. There is no lockfile,
container specification, or `sessionInfo()`. Exact versions without a lockfile
are still a level 2 dependency list: the transitive dependencies are
unspecified. The paper text (p. 3) gives a different R version, 4.2.2. The
deposit README is used as the supplied pin, because it is the
version-of-record environment statement (approved plan, risks); the
discrepancy is a documentation finding.

**Supplied pins honoured: in full, with 0 fallbacks.** R 4.3.2 and all seven
README package versions were built at exactly the supplied version on the
first attempt. The version-search cap (pin, preceding release, following
release) was never needed.

### Software Versions

| Component | Version | Source | Class |
|-----------|---------|--------|-------|
| R | 4.3.2 (2023-10-31) | `rocker/r-ver:4.3.2` | pinned (README) |
| Docker base | `rocker/r-ver:4.3.2@sha256:4e32addfc4da3e660f6e0d05ce5e43d3eceb9db58a60b9a142e0dde9a654ead1` | Docker Hub | reproducer's choice |
| quanteda | 3.3.1 | CRAN Archive source tarball | pinned (README) |
| readxl | 1.4.3 | CRAN Archive source tarball | pinned (README) |
| ggplot2 | 3.5.0 | CRAN Archive source tarball | pinned (README) |
| dplyr | 1.1.4 | CRAN Archive source tarball | pinned (README) |
| data.table | 1.15.0 | CRAN Archive source tarball | pinned (README) |
| forcats | 1.0.0 | CRAN Archive source tarball | pinned (README) |
| extrafont | 0.19 | CRAN Archive source tarball | pinned (README) |
| Image | `llmr-herskind-riede-2024-attempt-03`, id `sha256:9519b8dac291dc275bd40f7f6c0759eebeda8b5ebd38e5b50f64871ae2c58e5e` | built locally (1 build) | label `llmr.dockerfile.sha256=5b17276d68ea1f6a81ee72f77c330858c6338693d8fe43a7b1e5af7a91e1fb01` |
| Host OS | Linux 6.14.0-37-generic (host `AMD-tower-ubuntu`) | local execution through `run-container` | sapphire not used (held for a memory fault, Shawn 2026-10-10) |
| Container OS | Ubuntu 22.04.4 LTS (jammy), OpenBLAS 0.3.20 | from the base image | |
| Locale | `en_US.UTF-8` (set in the Dockerfile) | S2.R uses `ertebølledata` and `"Ertebølle"` | |

Pinned source tarballs (sha256 printed in the build log, Dockerfile step 1):

| Tarball | sha256 |
|---------|--------|
| `data.table_1.15.0.tar.gz` | `39b7db5dbc76fed91ac60bc351f37a0275a51f306120086b5cd92c1062241062` |
| `dplyr_1.1.4.tar.gz` | `cf730414d5d4ab387b4e9890a4b1df9d17a3903488e8da8df1cf2e11e44558cb` |
| `extrafont_0.19.tar.gz` | `4e8f90152df13fc5dee573222a26b4d66553493fdf6af1c7777e59521ccdab8d` |
| `forcats_1.0.0.tar.gz` | `c5bb157909d92e1e1a427c0dc5cb358ea00a43a14918a9088fa4f6630962254e` |
| `ggplot2_3.5.0.tar.gz` | `07fa1cd4e02d409ade32e69a9088d9209f864c6ddd70fa2f904769dec21090e2` |
| `quanteda_3.3.1.tar.gz` | `628542307d7ac45d4996fbc993a43ed5efcca73d97735ca74a10ccea401d4166` |
| `readxl_1.4.3.tar.gz` | `7efebbcdefeb8523633db62b3eeb6ea2e4e81e3d010d8b2adb134011c09a5948` |

### Package repository dates

The base image was the reproducer's choice: the authors supplied no container.
So its built-in repository date is not the authors', and was overridden
(invariant 2, "Supplied pins take precedence"; dockerfile-patterns.md,
"Package repository dates").

- **Base image's own date (not used for any install):** `rocker/r-ver:4.3.2`
  sets `CRAN=https://p3m.dev/cran/__linux__/jammy/2024-02-28`.
- **Pinned versions:** read and built from CRAN itself,
  `https://cloud.r-project.org/src/contrib/Archive/<pkg>/<pkg>_<version>.tar.gz`
  (all seven pins are in `Archive/`; none is current on CRAN).
- **Packages the authors left unspecified:** the Posit Package Manager
  snapshot dated to the article's first online appearance (3 April 2024),
  `https://packagemanager.posit.co/cran/__linux__/jammy/2024-04-03` (Ubuntu
  jammy binaries), set explicitly via `options(repos = ...)` in the install step.
- **Which packages were unspecified:** the Depends, Imports, and LinkingTo
  fields of each pinned version's own DESCRIPTION, resolved recursively,
  excluding packages that ship with R 4.3.2. 44 packages were fetched from the
  snapshot (build log, Dockerfile step 2).

### Installed packages (all), by class

From `wrapper-captures/package-inventory.csv` (sealed in `outputs/run-04/`)
and the build log.

**Pinned (README; CRAN Archive source):** data.table 1.15.0, dplyr 1.1.4,
extrafont 0.19, forcats 1.0.0, ggplot2 3.5.0, quanteda 3.3.1, readxl 1.4.3.

**Unspecified (P3M snapshot 2024-04-03), 44:** cellranger 1.1.0, cli 3.6.2,
colorspace 2.1-0, cpp11 0.4.7, crayon 1.5.2, extrafontdb 1.0, fansi 1.0.6,
farver 2.1.1, fastmatch 1.1-4, generics 0.1.3, glue 1.7.0, gtable 0.3.4, hms
1.1.3, isoband 0.2.7, ISOcodes 2024.02.12, jsonlite 1.8.8, labeling 0.4.3,
lifecycle 1.0.4, magrittr 2.0.3, munsell 0.5.1, pillar 1.9.0, pkgconfig 2.0.3,
prettyunits 1.2.0, progress 1.2.3, R6 2.5.1, RColorBrewer 1.1-3, Rcpp 1.0.12,
RcppArmadillo 0.12.8.1.0, RcppParallel 5.1.7, rematch 2.0.0, rlang 1.1.3,
Rttf2pt1 1.3.12, scales 1.3.0, SnowballC 0.7.1, stopwords 2.3, stringi 1.8.3,
tibble 3.2.1, tidyselect 1.2.1, utf8 1.2.4, vctrs 0.6.5, viridisLite 0.4.2,
withr 3.0.0, xml2 1.3.6, yaml 2.3.8.

**Bundled with R 4.3.2:** base packages (base, compiler, datasets, graphics,
grDevices, grid, methods, parallel, splines, stats, stats4, tcltk, tools,
utils) and recommended packages (boot 1.3-28.1, class 7.3-22, cluster 2.1.4,
codetools 0.2-19, foreign 0.8-85, KernSmooth 2.23-22, lattice 0.21-9, MASS
7.3-60, Matrix 1.6-1.1, mgcv 1.9-0, nlme 3.1-163, nnet 7.3-19, rpart 4.1.21,
spatial 7.3-17, survival 3.5-7). Among these, ggplot2 needs MASS and mgcv, and
quanteda needs Matrix. All three were taken as shipped with the pinned R
runtime, not from the snapshot.

**Pre-installed by the base image (rocker tooling, the image's own
2024-02-28 snapshot):** docopt 0.7.1 and littler 0.3.19. The package
inventory labels them "unspecified (P3M snapshot 2024-04-03)" because its
classifier only distinguishes pinned and R-bundled packages; the build log
shows neither was fetched in the install step. Neither is a dependency of the
analysis, and the run did not load either (`session-info.txt`).

**Fallbacks:** none.

### System Dependencies Added to Docker

- `curl`, `ca-certificates`: fetching the pinned tarballs at build time.
- `libxml2-dev`: xml2 (quanteda dependency).
- `libicu-dev`: stringi (quanteda dependency).
- `zlib1g-dev`: data.table (compiled from source).
- `libfontconfig1-dev`, `libfreetype6-dev`, `fontconfig`, `fonts-dejavu-core`:
  a system font directory, for `extrafont::font_import()` to scan and as a
  fallback font for the cairo PNG device (Gill Sans MT is proprietary and
  unavailable).
- `chmod -R a+rwX` on the `extrafontdb` package directory, so that the
  authors' `font_import()` can write its font table as it could for the
  authors, although the run is non-root. Computes nothing that enters a result.

### R Package Dependencies (Automatic)

quanteda 3.3.1 pulls in, among others: stringi 1.8.3 (ICU 70.1, Unicode 14.0),
RcppParallel 5.1.7, RcppArmadillo 0.12.8.1.0, fastmatch 1.1-4, SnowballC
0.7.1, stopwords 2.3. ggplot2 3.5.0 pulls in scales 1.3.0, gtable 0.3.4,
isoband 0.2.7, and the tidyverse core (rlang 1.1.3, vctrs 0.6.5, cli 3.6.2,
lifecycle 1.0.4). readxl 1.4.3 pulls in cellranger 1.1.0 and progress 1.2.3.

### Data Source(s)

- **File:** `Herskind&Riede_S1.xlsx` (442,983 bytes; sha256
  `d76b9d6328465658aa1582c5c8de0912f9167ff1f8c737bd7998d91fd5692030`)
- **Source:** Zenodo record 10801706, version 2, 2024-03-10
  (`https://zenodo.org/api/records/10801706/files/Herskind&Riede_S1.xlsx/content`;
  DOI 10.5281/zenodo.10801706), unauthenticated HTTPS GET; md5 matched the
  published `0bcde6d178b5a8f3da80a023a64ff510`.
- **Format:** sheet `Data`, 290 columns, 483 objects (No. 1-483) plus 18
  formatted empty rows, which `readxl::read_excel()` drops (`nrow(data)` =
  483). Motif presence/absence in columns 31-289, Chronology in column 11,
  coordinates in columns 13-14 (17 objects at unknown sites have "-").
- **Access level:** L1 (open-complete). See `log.md`, "Data availability".

#### Data Availability Inventory

| Dataset | Records | Source | Access Level | Available? |
|---------|---------|--------|--------------|------------|
| S1.xlsx (analysis data, sole input to all 20 targets) | 483 objects | Zenodo 10.5281/zenodo.10801706 (v2) | L1 | Yes |
| S3.xlsx (authors' precomputed tables; published-values reference for T08) | 165 + 106 + 20 rows | same record | L1 | Yes |
| Płonka (2003) printed catalogue (upstream provenance only; no target needs it) | not counted | printed book | not a counted dataset | not needed |

**Overall availability:** 1/1 required input datasets (100% by dataset) and
483/483 objects (100% by records). S3 is a reference file, also retrieved.

### Upstream Software (Not Reproduced)

- **GIMP**: post-processing of Figs 2-4 (panel composition, box annotations
  in Fig. 4, inset motif drawings) and production of the Fig. 5 map. Open
  source but manual, with no code path. Data-bearing annotations were checked
  with labelled R1 verification aids and transcriptions of the published
  figures (see the comparison report).
- **Fig. 2 map and Fig. 5**: made outside R; no authors' code. Checked with R1
  aids that plot S1 coordinates.
- **Gill Sans MT** (Monotype/Microsoft): proprietary typeface used only for
  figure typography; unavailable, so figures render in a fallback face.

### Notes

- **R version.** The README pin (4.3.2) was used, not the paper's 4.2.2. This
  is a documentation inconsistency between the paper and its deposit; no
  build failed.
- **Determinism.** The analysis is closed-form counting (skipgrams with
  k = 0:13 over at most 15 tokens per object) and natural-log PMI. There is
  no random-number generator and no seed. quanteda reports parallel
  computing on 16 threads; counts do not depend on thread scheduling, and
  every count was identical across runs 02-04.
- **Graphics device.** ggsave() PNGs use the cairo device
  (`capabilities("cairo") = TRUE`, `bitmapType = cairo`). The authors' top-level
  plot prints go to a cairo PNG "screen device" set by the wrapper, because
  Rscript's default `pdf()` device rejects the unregistered family "Gill Sans
  MT" (declared mechanic; see `log.md`).
- **Font registration.** The authors' `font_import(pattern = "GIL", prompt =
  FALSE)` (S2.R line 27) errored ("arguments imply differing number of rows:
  0, 1", because no font file matched "GIL"). The authors' own comment notes an error
  message here too. The declared wrapper tolerance fired, and the expression
  computes nothing that enters a result.
