# Dockerfile — Dye et al. (2023) reproduction, attempt 02
#
# Purpose: a pinned R environment for the R post-processing printed in the
# supplement (mmc1.pdf, sections 3-10) of Dye, Buck, DiNapoli & Philippe (2023),
# "Bayesian chronology construction and substance time", Journal of
# Archaeological Science 153, 105765.
#
# Pinning decisions (approved reproduction plan, environment block):
#   - R 4.2.3 (rocker/r-ver:4.2.3): contemporary with the March 2023
#     supplement; the authors state no R version.
#   - CRAN dependencies from the Posit Package Manager (PPM) snapshot of
#     2023-03-23 (date of the beads.oxcal entry in mmc2.zip).
#   - ArchaeoPhases 1.8 installed from the CRAN archive tarball (sha256
#     728a0d0c3a487e8f90b8c550a977a7678855d0c355a0347629d4a4afd5a5a801),
#     the only release exporting every function the supplement calls.
#
# Build:  docker build -t llmr-dye-et-al-2023-attempt-02 <attempt dir>
# Run:    docker run --rm --network none -v <attempt dir>:/project \
#             llmr-dye-et-al-2023-attempt-02

FROM rocker/r-ver:4.2.3

# System libraries required by ArchaeoPhases' dependency tree:
#   libproj-dev       -> proj4 (via ggalt)
#   libglpk-dev, libgmp-dev, libxml2-dev -> igraph (via ggraph)
#   libcairo2-dev, libfontconfig1-dev, libfreetype6-dev, libpng-dev,
#   libharfbuzz-dev, libfribidi-dev -> cairo_pdf graphics and text shaping
#   libcurl4-openssl-dev, libssl-dev -> curl/openssl (via readr/shiny stack)
RUN apt-get update && apt-get install -y --no-install-recommends \
        libproj-dev \
        libglpk-dev \
        libgmp-dev \
        libxml2-dev \
        libcairo2-dev \
        libfontconfig1-dev \
        libfreetype6-dev \
        libpng-dev \
        libharfbuzz-dev \
        libfribidi-dev \
        libcurl4-openssl-dev \
        libssl-dev \
        fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*

# Pin CRAN to the PPM snapshot (Ubuntu jammy binaries) dated 2023-03-23.
ENV CRAN_SNAPSHOT=https://packagemanager.posit.co/cran/__linux__/jammy/2023-03-23
RUN echo "options(repos = c(CRAN = '${CRAN_SNAPSHOT}'))" \
        >> /usr/local/lib/R/etc/Rprofile.site

# ArchaeoPhases 1.8 Depends + Imports (DESCRIPTION of the 1.8 tarball).
RUN R -q -e "install.packages(c('coda', 'hdrcde', 'shiny', 'readr', 'toOrdinal', \
        'ggplot2', 'ggalt', 'reshape2', 'dplyr', 'digest', 'gplots', 'magrittr', \
        'ggraph', 'gtools', 'jsonlite'))" \
    && R -q -e "stopifnot(all(sapply(c('coda','hdrcde','shiny','readr','toOrdinal', \
        'ggplot2','ggalt','reshape2','dplyr','digest','gplots','magrittr','ggraph', \
        'gtools','jsonlite'), requireNamespace, quietly = TRUE)))"

# ArchaeoPhases 1.8 from the verified CRAN archive tarball (vendored).
COPY vendor/ArchaeoPhases_1.8.tar.gz /tmp/ArchaeoPhases_1.8.tar.gz
RUN echo "728a0d0c3a487e8f90b8c550a977a7678855d0c355a0347629d4a4afd5a5a801  /tmp/ArchaeoPhases_1.8.tar.gz" \
        | sha256sum -c - \
    && R CMD INSTALL /tmp/ArchaeoPhases_1.8.tar.gz \
    && R -q -e "library(ArchaeoPhases); stopifnot(packageVersion('ArchaeoPhases') == '1.8'); \
        stopifnot(all(c('read_oxcal','allen_observe_frequency','allen_illustrate', \
        'allen_observe','estimate_range','occurrence_plot','tempo_plot') %in% \
        getNamespaceExports('ArchaeoPhases')))" \
    && rm /tmp/ArchaeoPhases_1.8.tar.gz

WORKDIR /project

# Default: run the full pipeline (authors' transcribed code, then the
# separate verification-aid and comparison scripts).
CMD ["bash", "run-all.sh"]
