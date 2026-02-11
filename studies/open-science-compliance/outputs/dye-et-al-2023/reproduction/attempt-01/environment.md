# Environment Specification

## Dye et al. 2023 Reproduction

### Software Versions

| Component | Version | Source |
|-----------|---------|--------|
| R | 4.3.1 (2023-06-16) | rocker/r-ver:4.3.1 Docker image |
| ArchaeoPhases | 1.8 | CRAN |
| ArchaeoData | (installed but not used) | r-universe (archaeostat) |
| Docker base | rocker/r-ver:4.3.1 | Docker Hub |
| Host OS | Ubuntu (Docker) | Local execution |

### System Dependencies Added to Docker

The base rocker image required the following additional system libraries:

- `libcurl4-openssl-dev` — HTTP client library (for remote data access)
- `libssl-dev` — Secure Sockets Layer (SSL) development files
- `libxml2-dev` — Extensible Markup Language (XML) library
- `libglpk-dev` — GNU Linear Programming Kit (required by igraph)
- `libproj-dev` — Cartographic Projections library (required by proj4)
- `libgdal-dev` — Geospatial Data Abstraction Library (GDAL, required by proj4)

### R Package Dependencies (Automatic)

ArchaeoPhases v1.8 pulls in these key dependencies:

- `coda` — MCMC output analysis
- `hdrcde` — Highest density region estimation
- `igraph` — Graph/network analysis
- `ggplot2` — Plotting
- `ggalt` — Extended ggplot2 geometries (dumbbell plots)
- `proj4` — Cartographic projections

### MCMC Data Source

- **File:** `beads-1.csv` (3.7 MB)
- **Source:** `https://tsdye.online/AP/beads-1.csv` (author's server)
- **Format:** 6001 rows (6000 MCMC samples + header), 79 columns
- **Content:** Calibrated posterior date estimates (calendar years CE) for 77
  Anglo-Saxon burial samples from one of five independent OxCal calibration runs

### Upstream Proprietary Software (Not Reproduced)

- **OxCal 4.4.2** — Bayesian chronological modelling software (proprietary,
  University of Oxford)
- Used to generate the MCMC samples from radiocarbon dates
- Pre-computed output provided by authors via remote server
- The ArchaeoPhases post-processing (the paper's analytical contribution) is
  fully open and reproducible

### Notes

- The paper does not specify R version; 4.3.1 was chosen as a plausible
  2023-era version
- Analysis is fully deterministic post-processing of pre-computed MCMC
  samples, so exact R version matching is not critical
- ArchaeoPhases v1.8 (installed from CRAN in Docker) matches the paper's
  publication timeline (v2.0 was released later in 2023)
- The supplement code references a remote server URL for MCMC data; we
  downloaded a local copy for reproducibility
