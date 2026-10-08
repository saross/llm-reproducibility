# Launcher-matrix test image for the reproduction lane, gate 1.3.
#
# Specification: wiki/planning/reproduction-gate-1-3-design.md §13. The
# matrix checks that every ordinary way of starting R, or of loading code
# through a common tool, is seen by the lane's exec shim and hook. The base
# image lacks the tools concerned, so this image adds them from the base
# image's own pinned CRAN snapshot (Posit Package Manager, 2024-02-28), plus
# pandoc and Quarto through rocker's own install scripts, at the versions
# first built here (2026-10-08), so that a rebuild fetches the same ones.
#
# Build (once per host; the Docker-backed tests skip when it is absent):
#   docker build -t llmr-launcher-matrix:4.3.2 tests/fixtures/launcher-matrix
#
# System libraries are for devtools' dependency tree (gert needs libgit2;
# the graphics stack needs the font and image libraries).

FROM rocker/r-ver:4.3.2

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libgit2-dev libcurl4-openssl-dev libssl-dev libxml2-dev \
        libfontconfig1-dev libharfbuzz-dev libfribidi-dev libfreetype6-dev \
        libpng-dev libtiff5-dev libjpeg-dev \
    && rm -rf /var/lib/apt/lists/*

RUN install2.r --error --skipinstalled \
        callr targets future knitr rmarkdown remotes Rcpp pkgload pkgbuild \
    && rm -rf /tmp/downloaded_packages

RUN install2.r --error --skipinstalled devtools \
    && rm -rf /tmp/downloaded_packages

RUN /rocker_scripts/install_pandoc.sh 3.12.1 \
    && /rocker_scripts/install_quarto.sh 1.10.19 \
    && rm -rf /var/lib/apt/lists/*
