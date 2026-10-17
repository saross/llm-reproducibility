# =============================================================================
# Dockerfile -- herskind-riede-2024, reproduction attempt 04
#
# Paper: Herskind, L.L.P. & Riede, F. (2024) Journal of Archaeological
#   Science 165, 105969 (available online 2024-04-03).
# Authors' environment statement (deposit README.txt, Zenodo 10801706):
#   R 4.3.2; extrafont 0.19, data.table 1.15.0, dplyr 1.1.4, ggplot2 3.5.0,
#   readxl 1.4.3, quanteda 3.3.1, forcats 1.0.0. No container or lockfile
#   (environment-specification level 2), so this base image is the
#   reproducer's choice.
#
# Build through the lane only:
#   venv/bin/python scripts/reproduction-lane.py build-image <attempt dir> \
#     --tag llmr-herskind-riede-2024-attempt-04 --launch-commit <commit>
# =============================================================================
FROM rocker/r-ver:4.3.2

# UTF-8 locale: S2.R has a non-ASCII identifier (ertebølledata) and the data
# use "Ertebølle" as a factor level.
ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8

# System libraries: compilers for the pinned source tarballs (quanteda,
# data.table, readxl, dplyr are compiled code); ICU and libxml2 for stringi
# and xml2 binaries (quanteda dependencies); libcurl/OpenSSL for downloads;
# fontconfig, FreeType, cairo, and open fonts so the cairo PNG device can
# render text (the proprietary Gill Sans MT the code names is unavailable).
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        gfortran \
        libxml2-dev \
        libicu-dev \
        libcurl4-openssl-dev \
        libssl-dev \
        zlib1g-dev \
        libfontconfig1 \
        libfreetype6 \
        libcairo2 \
        fonts-liberation \
        fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*

# R packages: the seven README pins from CRAN's own tarballs; everything
# they need that the authors left unspecified from the Posit Package Manager
# snapshot of 2024-04-03 (first online appearance), not the image's own
# 2024-02-28 date. The script logs every attempt and writes the inventory to
# /opt/llmr/package-inventory.csv.
COPY install-pins.R /opt/llmr/install-pins.R
RUN Rscript /opt/llmr/install-pins.R

# The lane mounts the work copy here.
WORKDIR /project
