# Probe environment v3 for crema-et-al-2024, deposit v1.0.0 (Zenodo), built
# under amendment 3 §7(d) after Astra's review of PR #10 (B3, 2026-10-10).
# The deposit has no Dockerfile or lockfile; its README's session info is the
# authors' environment specification. R 4.3.1 comes from it, and every
# package version it lists, attached or namespace-only, is a supplied pin
# (install-pins.R; inventory and attempts in /build). v3 corrects two
# defects in v2's install script (release listing, dependency order).
FROM rocker/r-ver:4.3.1

RUN apt-get update && apt-get install -y --no-install-recommends \
      libgdal-dev libgeos-dev libproj-dev libudunits2-dev libssl-dev \
      libcurl4-openssl-dev libxml2-dev libfontconfig1-dev libglpk-dev \
      libgmp-dev libicu-dev zlib1g-dev pkg-config poppler-utils git \
    && rm -rf /var/lib/apt/lists/*

# Build tooling only; the analysis does not use it.
RUN R -q -e "install.packages('remotes', repos = 'https://cloud.r-project.org')"

COPY pins.csv install-pins.R /build/
RUN MAKEFLAGS=-j8 Rscript /build/install-pins.R

# rnaturalearthhires is not in the session info, so it is unspecified: an
# initial choice, not a fallback. It is not on CRAN; the tag current at the
# article's first online appearance (2024-03-16) is v1.0.0 (2023-12-12,
# commit db8e433bfb80dc775f04bd5b0d8911fa6b9a568c).
RUN R -q -e "remotes::install_github('ropensci/rnaturalearthhires@v1.0.0', \
      upgrade = 'never', dependencies = FALSE); \
      stopifnot(packageVersion('rnaturalearthhires') == '1.0.0')"
WORKDIR /work
