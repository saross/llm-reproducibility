# Dockerfile Patterns for R-Based Analyses

Reference for building Docker containers to reproduce R-based computational research.

## Rocker Image Hierarchy

The [Rocker Project](https://rocker-project.org/) maintains versioned Docker images for R. Each
tier extends the one below it:

| Image | Adds | Typical Size |
|-------|------|--------------|
| `rocker/r-ver:{version}` | Base R at a specific version | ~800 MB |
| `rocker/rstudio:{version}` | RStudio Server | ~1.5 GB |
| `rocker/tidyverse:{version}` | tidyverse, devtools, and common dependencies | ~2 GB |
| `rocker/verse:{version}` | LaTeX (TinyTeX), publishing tools | ~3 GB |
| `rocker/geospatial:{version}` | Spatial libraries (sf, terra, stars, etc.) | ~4 GB |

**Recommendation:** Start with `rocker/r-ver` and add only what the analysis requires. Higher-tier
images bundle packages the paper may never use, inflating build time and image size.

**Version selection priority:**

1. Explicit Dockerfile in the repository (use the same base version)
2. `renv.lock` — check the `R.Version` field
3. `sessionInfo()` output printed in the paper or supplementary materials
4. Paper publication date — use the current R release as of that date

## Common System Dependencies

When `install.packages()` fails with `configure: error`, the message typically names the missing
C/C++ library. This table maps the most frequent R packages to their Debian/Ubuntu system
dependencies:

| R Package(s) | System Library | `apt-get install` |
|--------------|----------------|-------------------|
| igraph | GLPK | `libglpk-dev` |
| sf, proj4 | PROJ | `libproj-dev` |
| sf, rgdal | GDAL | `libgdal-dev` |
| sf | GEOS | `libgeos-dev` |
| curl, httr | libcurl | `libcurl4-openssl-dev` |
| openssl | OpenSSL | `libssl-dev` |
| xml2 | libxml2 | `libxml2-dev` |
| units | UDUNITS-2 | `libudunits2-dev` |
| rJava | Java Development Kit (JDK) | `default-jdk` |
| magick | ImageMagick++ | `libmagick++-dev` |
| textshaping | HarfBuzz, FriBidi | `libharfbuzz-dev libfribidi-dev` |
| ragg | FreeType, PNG, TIFF | `libfreetype6-dev libpng-dev libtiff5-dev` |
| V8 | V8 JavaScript engine | `libv8-dev` |

**Pattern:** Read the `configure: error` output carefully. It almost always names the missing
library or the `pkg-config` name to search for.

## Iterative Build Strategy

Expect 1--3 build iterations before a Dockerfile works cleanly. This is normal, not a failure.

**Iteration 1 — Base image plus explicit R packages.** Install the packages listed in the paper's
scripts. This will likely fail on missing system dependencies.

**Iteration 2 — Add system deps from error messages.** Read the build log, identify the missing
libraries, add them to the `apt-get install` block, and rebuild. This may reveal further transitive
dependencies.

**Iteration 3 — Final fixes.** Resolve any remaining edge cases (GitHub-only packages, version
conflicts, non-standard repositories).

**Key principles:**

- Install all system dependencies *before* R packages — a single `RUN apt-get` block followed by a
  single `RUN R -e "install.packages(...)"` block
- Order R package installation so that dependencies come first, or rely on
  `install.packages()` to resolve the dependency tree automatically
- Use `--no-install-recommends` with `apt-get` to keep the image lean
- Clean up the apt cache at the end of the `RUN` block: `rm -rf /var/lib/apt/lists/*`

## renv Pathway

When the repository includes an `renv.lock` file, use renv to restore the exact package versions
the authors used.

```dockerfile
# Copy lockfile first (layer caching)
COPY renv.lock /project/renv.lock
WORKDIR /project

# Install renv and restore packages
RUN R -e "install.packages('renv', repos='https://cloud.r-project.org')" \
    && R -e "renv::restore()"
```

**Notes:**

- renv handles version pinning automatically, but it does *not* install system-level dependencies.
  You still need the `apt-get` block for C/C++ libraries.
- If the R version in the rocker image differs from the version recorded in `renv.lock`, renv will
  issue a warning. This is usually safe to ignore — package installation generally succeeds unless
  the mismatch is large (e.g., R 3.x lockfile on an R 4.x image).
- If renv restoration fails on a single package, install its system deps and re-run
  `renv::restore()`. It will skip already-installed packages.

## Dockerfile Template

Minimal working template for most R-based reproductions:

```dockerfile
FROM rocker/r-ver:{VERSION}

# System dependencies (adjust to the paper's package requirements)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libcurl4-openssl-dev \
    libssl-dev \
    libxml2-dev \
    && rm -rf /var/lib/apt/lists/*

# R packages
RUN R -e "install.packages(c('package1', 'package2'), repos='https://cloud.r-project.org')"

# Copy analysis files
COPY . /project
WORKDIR /project

CMD ["Rscript", "run-analysis.R"]
```

Replace `{VERSION}` with the target R version (e.g., `4.3.1`). Add system dependencies and R
packages as identified during the iterative build process.

## Volume Mount vs COPY Strategy

Two approaches for getting analysis files into the container:

| Strategy | Command | Use Case |
|----------|---------|----------|
| **COPY** | `COPY . /project` in Dockerfile | Final reproducible build; files baked into image |
| **Volume mount** | `-v $(pwd):/project` at runtime | Development and iteration; files live on host |

**Guidance:**

- During iterative development, use volume mounts. This avoids rebuilding the image every time a
  script changes.
- For long-running analyses (Markov chain Monte Carlo (MCMC), bootstrapping), always use volume
  mounts so results persist on the host filesystem even if the container exits unexpectedly.
- For the final reproducible build, prefer COPY. The image then contains everything needed to
  reproduce the analysis without any host-side file dependencies.
- Volume mounts can be combined with COPY: bake the code into the image but mount an output
  directory for results.

## Gotchas from Pilot Reproductions

Lessons learned from actual reproduction attempts:

- **`.here` sentinel file:** When using volume mounts, the container's working directory has no
  `.git` folder. If the analysis uses the `here` package, it cannot find the project root. Create
  an empty `.here` file in the mounted directory to serve as the sentinel.

- **`rnaturalearthhires` not on CRAN:** This package is only available from GitHub. Install it with
  `remotes::install_github("ropensci/rnaturalearthhires")` or
  `install.packages("rnaturalearthhires", repos="https://ropensci.r-universe.dev")`.

- **Ampersands in filenames:** Docker volume mount paths containing `&` cause shell parsing issues.
  Rename files on the host before mounting, or use the long-form `--mount` syntax instead of `-v`.

- **R version mismatch with `renv.lock`:** This typically produces a warning, not a build failure.
  If packages install and load correctly, the reproduction can proceed. Document the mismatch in
  the reproduction notes.

- **MRAN retirement:** The Microsoft R Application Network (MRAN) snapshot repository was retired
  in July 2023. Older Dockerfiles or lockfiles referencing `mran.microsoft.com` will fail.
  Replace with `https://cloud.r-project.org` or use Posit Package Manager snapshots
  (`https://packagemanager.posit.co/cran/{date}`).

- **Data server unreliability:** Scripts that download data from author personal servers or
  institutional URLs may fail during Docker build if the server is offline, has moved, or
  rate-limits. Download data locally first and COPY it into the image rather than relying on
  `RUN curl` or `RUN wget` during the build. This also improves build reproducibility.

- **Column naming mismatches:** Data files may use different column names than the analysis
  scripts expect (e.g., `Length_mm` vs `length_mm`, `Mass` vs `mass_g`). Check column names
  in the actual data file against the script's references. This is especially common when
  data files are downloaded from different sources than the original analysis used.

- **Base R sufficiency:** Not all analyses require external packages. Simple statistical
  methods (arithmetic, basic plotting, file I/O) may run on base R alone. In these cases,
  `rocker/r-ver:{version}` with zero additional `install.packages()` calls is sufficient,
  resulting in fast builds and small images (e.g., Key et al. 2024: ~820 MB, ~5s runtime).
