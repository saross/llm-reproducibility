# Environment Specification: crema-et-al-2024 Reproduction

**Paper:** Crema et al. (2024) "Modelling diffusion of innovation curves using radiocarbon data"
**Repository:** https://github.com/ercrema/diffusionCurve
**DOI:** 10.5281/zenodo.10782942

## Repository Analysis

### Structure

The repository is well-organised with clear separation of concerns:

```text
diffusionCurve/
├── analysis/          # Empirical case study scripts
│   ├── britain_abot.R
│   ├── burial_icar.R
│   ├── japan_abot.R
│   ├── post_check_gb_abot.R
│   └── post_check_jp_abot.R
├── data/              # Raw and processed data
│   ├── raw/           # Original CSV files
│   ├── *.RData        # Processed datasets
│   └── *_clean.R      # Data processing scripts
├── figures_and_tables/
│   ├── figure*.pdf    # Published figures
│   ├── figures_main.R # Figure generation scripts
│   └── table1.csv     # Published Table 1
├── results/           # Pre-computed MCMC outputs
│   └── *.RData        # Posterior distributions
├── sim/               # Simulation studies
│   ├── simdata/       # Simulated datasets
│   ├── results/       # Simulation posteriors
│   └── *.R            # Simulation scripts
├── src/
│   └── utility.R      # Helper functions
├── Dockerfile         # Docker configuration
└── README.md          # Documentation
```

### Documentation Quality

**Excellent** — README.md includes:
- Complete file structure documentation
- Execution pipeline with dependencies
- Runtime estimates per script
- R session info with package versions
- Docker instructions

### Pre-computed Results

The repository includes pre-computed MCMC outputs:

| File | Size | Description |
|------|------|-------------|
| `post_jp_abot.RData` | 1.2 MB | Japan sigmoid model posterior |
| `post_gb_abot.RData` | 1.2 MB | Britain sigmoid model posterior |
| `post_icar_burial.RData` | 24.7 MB | Burial ICAR model posterior |
| `ppc_*.RData` | 8-20 MB | Posterior predictive samples |

This enables figure/table regeneration without re-running 24-hour MCMC analyses.

## Required Environment

### R Version

**R 4.3.1** (from session info) / **R 4.3.3** (from Dockerfile)

### R Packages (Attached)

| Package | Version | Purpose |
|---------|---------|---------|
| `nimble` | 1.0.1 | Bayesian MCMC engine |
| `nimbleCarbon` | 0.2.4 | Radiocarbon-specific nimble functions |
| `rcarbon` | 1.5.0 | Radiocarbon calibration |
| `coda` | 0.19-4 | MCMC diagnostics |
| `sf` | 1.0-14 | Spatial data handling |
| `rnaturalearth` | 0.3.3 | Map data |
| `dplyr` | 1.1.2 | Data manipulation |
| `here` | 1.0.1 | Project paths |
| `truncnorm` | 1.0-9 | Truncated normal distribution |
| `latex2exp` | 0.9.6 | LaTeX in plots |
| `RColorBrewer` | 1.1-3 | Colour palettes |

### System Dependencies

From Dockerfile:
- `libicu-dev`
- `libglpk-dev`
- `libxml2-dev`
- `pandoc`
- `libssl-dev`
- `libgdal-dev`, `gdal-bin`
- `libgeos-dev`
- `libproj-dev`
- `libsqlite3-dev`
- `libudunits2-dev`
- `libcurl4-openssl-dev`

## Current System Status

**System:** Ubuntu (Linux 6.16.9)
**User:** shawn (sudo group member)

### Availability Check

| Component | Status | Notes |
|-----------|--------|-------|
| R | ❌ Not installed | Not in PATH, not in `/usr/bin` |
| Docker | ❌ Not installed | `docker --version` failed |
| conda/mamba | ❌ Not installed | No conda environments found |

## Environment Setup Options

### Option A: Docker (Recommended)

The repository provides a Dockerfile that creates a complete, isolated environment.

**Pros:**
- Exact R 4.3.3 version
- All dependencies pre-configured
- Isolated from system
- Most reproducible

**Cons:**
- Requires Docker installation
- Higher disk usage
- Container overhead

**Installation:**
```bash
sudo apt install docker.io
sudo usermod -aG docker $USER
# Log out and back in
cd /tmp/diffusionCurve
docker build -t diffusion .
docker run --rm -it -e ROOT=TRUE -e PASSWORD=rstudio -dp 8787:8787 diffusion
# Access at http://localhost:8787
```

### Option B: Native R + renv

Install R system-wide and use renv for package management.

**Pros:**
- Direct access to R console
- Faster iteration
- Lower overhead

**Cons:**
- System dependency management
- Potential version mismatches

**Installation:**
```bash
# Add CRAN repository for R 4.3
sudo apt install software-properties-common
sudo add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu jammy-cran40/'
sudo apt update
sudo apt install r-base r-base-dev

# System dependencies
sudo apt install libicu-dev libglpk-dev libxml2-dev pandoc libssl-dev \
    libgdal-dev gdal-bin libgeos-dev libproj-dev libsqlite3-dev \
    libudunits2-dev libcurl4-openssl-dev

# R packages
Rscript -e 'install.packages(c("truncnorm","here","coda","latex2exp","RColorBrewer","dplyr","nimbleCarbon","nimble","sf","rnaturalearth","rcarbon","emdbook","renv"))'
```

### Option C: Partial Verification

Use pre-computed results to verify figure/table generation without re-running MCMC.

**Pros:**
- Faster setup
- Verifies output generation pipeline
- Still requires R but less compute

**Cons:**
- Does not verify MCMC results themselves
- Partial reproduction only

## Runtime Estimates

From README (Intel Xeon W-2295, 128GB RAM):

| Analysis | Runtime |
|----------|---------|
| Full pipeline | 120-150 hours |
| Single MCMC analysis | ~24 hours |
| Figure/table generation | < 1 minute |
| Data cleaning scripts | < 1 minute |

## Verification Targets

### Table 1 Parameters (from repository)

| Region | r | m | μ | φ |
|--------|---|---|---|---|
| Japan | 0.1003 | BC844 | 0.701 | 0.75 |
| Britain | 0.0135 | BC4054 | 0.182 | 0.31 |

### Success Criteria

For MCMC analyses (stochastic), success is:
- Point estimates within published 90% Highest Posterior Density (HPD) intervals
- Same qualitative patterns in figures
- Identical conclusions

## Notes

1. **Dockerfile typo:** Line 11 has `RColoBrewer` instead of `RColorBrewer`
2. **Pre-computed results:** Allow verification without 120+ hour runtime
3. **Zenodo archive:** Provides persistent, versioned snapshot
