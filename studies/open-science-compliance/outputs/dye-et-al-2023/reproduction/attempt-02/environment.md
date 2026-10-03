# Environment Specification

## Dye et al. (2023) Reproduction — attempt 02

Run `phase2-shakedown-2026-10`; approved plan sha256
`7ff05a24d1342b84ebe5f61f2f0e7b15df040baf73ad1c67aa13c63ff49f0f35`.

### Software Versions

| Component | Version | Source |
|-----------|---------|--------|
| R | 4.2.3 (2023-03-15) | `rocker/r-ver:4.2.3` Docker image |
| ArchaeoPhases | 1.8 (Date/Publication 2022-06-21) | CRAN archive tarball, sha256 `728a0d0c3a487e8f90b8c550a977a7678855d0c355a0347629d4a4afd5a5a801` (vendored at `vendor/ArchaeoPhases_1.8.tar.gz`) |
| coda | 0.19-4 | Posit Package Manager (PPM) snapshot 2023-03-23 |
| hdrcde | 3.4 | PPM snapshot 2023-03-23 |
| ggplot2 | 3.4.1 | PPM snapshot 2023-03-23 |
| ggraph | 2.1.0 | PPM snapshot 2023-03-23 |
| igraph | 1.4.1 | PPM snapshot 2023-03-23 |
| readr | 2.1.4 | PPM snapshot 2023-03-23 |
| dplyr | 1.1.1 | PPM snapshot 2023-03-23 |
| gtools | 3.9.4 | PPM snapshot 2023-03-23 |
| toOrdinal | 1.3-0.0 | PPM snapshot 2023-03-23 |
| Docker base | `rocker/r-ver:4.2.3@sha256:6dff804fb051f7c38cf9ebcaf307b5102b46e5187ffe2ce921d760a26facd693` | Docker Hub |
| Built image | `llmr-dye-et-al-2023-attempt-02`, id `sha256:981fd7690fe67cc345ad3a2e3dc406cca2990f8d79831a9b8ec472d7caf0a6a7` (1.33 GB) | Built locally, 1 build iteration |
| Container OS | Ubuntu 22.04.4 LTS (jammy), OpenBLAS 0.3.20, locale C | from base image |
| Host OS | Ubuntu 25.04, Linux 6.14.0-37-generic x86_64, Docker 29.2.1 (amd-tower, 16 cores) | Local execution |

The full `sessionInfo()` is in `outputs/logs/session-info.txt`; the full build log
is in `outputs/logs/docker-build.log`.

### System Dependencies Added to Docker

- `libproj-dev`: PROJ library (required by proj4, which ggalt imports)
- `libglpk-dev` and `libgmp-dev`: GNU Linear Programming Kit and GNU Multiple Precision library (required by igraph, via ggraph)
- `libxml2-dev`: XML parsing (required by igraph)
- `libcairo2-dev`, `libfontconfig1-dev`, `libfreetype6-dev`, `libpng-dev`: Cairo graphics and fonts (needed for `cairo_pdf()` in ArchaeoPhases' `allen_plot()` and for ggplot2 output)
- `libharfbuzz-dev`, `libfribidi-dev`: text shaping (required by the graphics stack)
- `libcurl4-openssl-dev`, `libssl-dev`: HTTPS and TLS (required by the readr/shiny dependency stack)
- `fonts-dejavu-core`: an open font, so text renders without proprietary fonts

The CRAN repository is pinned in `Rprofile.site` to
`https://packagemanager.posit.co/cran/__linux__/jammy/2023-03-23`, which serves
Ubuntu binaries frozen on that date.

### R Package Dependencies (Automatic)

ArchaeoPhases v1.8 declares `Depends: R (>= 3.5.0), coda, hdrcde` and imports
stats, utils, graphics, grDevices, shiny, readr, toOrdinal, ggplot2, ggalt,
reshape2, dplyr, digest, gplots, magrittr, ggraph, and gtools. The ones that
carry the analysis are:

- `readr`: reads the OxCal Markov chain Monte Carlo (MCMC) CSV file in `read_oxcal()`
- `gtools`: `permutations()` builds the pairwise matrix in `allen_observe_frequency()`
- `ggplot2`, `ggalt`, and `ggraph`: tempo plots, occurrence plots, and Nökel lattices
- `toOrdinal`: ordinal labels ("1st interment") in `occurrence_plot()`

### Data Source(s)

- **File:** `beads-1.csv` (3,688,071 bytes; sha256 `02cf52d4ace408b6329e69e7a0e4bd457084ae9605f2fa5eccc2abad20ab9051`; md5 `026cc220f4e56bafa307274d0f77bcd4`; server Last-Modified 2022-10-20 16:24:44 GMT)
- **Source:** `https://tsdye.online/AP/beads-1.csv` (author's personal server; HTTPS GET with no authentication; URL hard-coded in the supplement's `read_oxcal()` calls)
- **Format:** OxCal MCMC sample output: 6,001 lines (header plus 6,000 samples, `Pass` 20 to 119980), 79 fields (`Pass`, 77 dated contexts, and an empty trailing field). `read_oxcal()` returns 6,000 × 77.
- **Access level:** this dataset is openly machine-retrievable, as for L1, but from a personal server rather than through a persistent identifier.

#### Data Availability Inventory

The paper-level L-level is assigned under data-availability taxonomy v1.0. The
counting unit is the planner's dataset enumeration (approved plan,
`data_retrieval_plan`).

| Dataset | Records | Source | Access Level | Available? |
|---------|---------|--------|--------------|------------|
| beads-1.csv (OxCal MCMC run used for all reported post-processing) | 6,000 samples × 77 contexts | `https://tsdye.online/AP/beads-1.csv` | open HTTPS (L1-type retrieval) | Yes, sha256 verified |
| beads-0.csv, beads-2.csv, beads-3.csv, beads-4.csv (four further OxCal runs, Supplement Table 1) | unknown | none stated (supplement code uses `/path/to/beads-N.csv` placeholders) | L6 (absent) | No: HTTP 404 at `https://tsdye.online/AP/beads-{0,2,3,4}.csv` on 2026-10-03 |

**Overall availability:** 1 of 2 datasets (50% by dataset). With 50%, the L2
condition (more than 50%) is not met. The paper-level terminal failure mode is
**L6**: the open-availability claim "Data and materials are available in the
Supplement" goes unfulfilled for the four replicate runs. The approver ruled
that no L4 request be sent in this shakedown.

**Sensitivity note:** if the OxCal model file (`beads.oxcal` in mmc2.zip,
retrievable) and the Archaeology Data Service archive (Hines 2013,
doi:10.5284/1018290) were also counted as datasets, and the four runs counted
as one, availability would be 3 of 4 (75%) and the level L2. This attempt
follows the plan's enumeration. The executor did not attempt the ADS archive,
which only OxCal regeneration (attempt-03) needs.

### Upstream Software (Not Reproduced)

- **OxCal 4.4.2** (with IntCal20): Bayesian radiocarbon calibration, freely
  available but closed-source, so it is a proprietary upstream.
- Used to generate the MCMC samples (`beads-1.csv` and the four further runs)
  from the revised chronological model (`beads.oxcal`, mmc2.zip).
- Not regenerated here: the run notes scope OxCal regeneration to a separately
  approved attempt (attempt-03).
- The archived MCMC output `beads-1.csv` stands in for regeneration (the
  archived-intermediates path).

### Notes

- **R version selection:** the authors state no R or package versions
  (environment-specification level 0 for the R analysis). R 4.2.3 and the
  2023-03-23 snapshot are contemporary with the supplement (mmc2.zip entry dated
  2023-03-23). ArchaeoPhases 1.8 is the only CRAN release that exports every
  function the supplement calls. Release 2.0 (2024) and later drop `read_oxcal`
  and `allen_observe_frequency`.
- **Determinism:** with `beads-1.csv` fixed, every R step (`read_oxcal`,
  `allen_observe_frequency`, `tempo_plot`, `allen_observe`, `allen_illustrate`)
  is deterministic. No random-number generation is involved, and repeated runs
  gave identical values.
- **Known mismatch:** the published figures (paper Figs 3 and 4, Supplement
  Figs 1-3) use a white panel background. ArchaeoPhases 1.8 with ggplot2 3.4.1
  renders the ggplot2 default grey background. The authors' theme setting is not
  published. See the comparison report (T03, T21, and T23).
- **Execution isolation:** every run used `docker run --rm --network none`, so
  the analysis read only the verified local `beads-1.csv`. The final run also
  used `--user $(id -u):$(id -g)`.
