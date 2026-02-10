# Dockerfile for Dye et al. 2023 reproduction
# "Bayesian chronology construction and substance time"
# Journal of Archaeological Science, 153, 105765
#
# Uses ArchaeoPhases (CRAN) for post-processing pre-computed OxCal MCMC output.
# R version 4.3.1 chosen as plausible 2023-era version (paper does not specify).
# Analysis is deterministic post-processing, so exact version matching is less critical.

FROM rocker/r-ver:4.3.1

RUN apt-get update && apt-get install -y \
    libcurl4-openssl-dev \
    libssl-dev \
    libxml2-dev \
    libglpk-dev \
    libproj-dev \
    libgdal-dev \
    && rm -rf /var/lib/apt/lists/*

# Install ArchaeoPhases from CRAN and ArchaeoData from r-universe
RUN R -e 'install.packages("ArchaeoPhases")' && \
    R -e 'install.packages("ArchaeoData", repos = "https://archaeostat.r-universe.dev")'

WORKDIR /analysis
