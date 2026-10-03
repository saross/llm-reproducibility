# =============================================================================
# Dockerfile — Herskind & Riede (2024) reproduction, attempt 02
# =============================================================================
# Paper: Herskind, L.L.P., Riede, F., 2024. A computational linguistic
#   methodology for assessing semiotic structure in prehistoric art ...
#   Journal of Archaeological Science 165, 105969.
# Code and data: Zenodo record 10.5281/zenodo.10801706, version 2 (2024-03-10).
#
# Environment target (approved plan, ruling 4): R 4.3.2 and the exact package
# versions listed in the deposit README.txt. The paper text says R 4.2.2; that
# conflict is recorded as a discrepancy, not followed.
#
# Package source: rocker/r-ver:4.3.2 ships a frozen Posit Package Manager
# (P3M) snapshot, https://p3m.dev/cran/__linux__/jammy/2024-02-28. That date
# precedes data.table 1.15.2 (2024-02-29), so the snapshot resolves every
# README pin exactly. The build ends with an assertion that fails the build
# if any installed version differs from the README.
#
# Build:  docker build -t llmr-herskind-riede-2024-attempt-02 <attempt-dir>
# Run:    docker run --rm --mount type=bind,src=<attempt-dir>,dst=/attempt \
#             llmr-herskind-riede-2024-attempt-02
# =============================================================================

FROM rocker/r-ver:4.3.2

# UTF-8 locale: S2.R contains the non-ASCII identifier `ertebølledata` and the
# string literal "Ertebølle" (Part 5 culture-complex subset).
ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8

# System libraries:
#   fontconfig, fonts-dejavu-core — an open fallback font. The authors' Gill
#     Sans MT is proprietary (Monotype) and cannot be shipped; the fontconfig
#     alias below maps the family name to DejaVu Sans. Typography only; no
#     computed value depends on it.
#   libcairo2, libfreetype6, libpng16-16 — cairo-backed png() device used by
#     ggsave() in a headless container.
RUN apt-get update && apt-get install -y --no-install-recommends \
        fontconfig \
        fonts-dejavu-core \
        libcairo2 \
        libfreetype6 \
        libpng16-16 \
    && rm -rf /var/lib/apt/lists/*

# Fontconfig alias: "Gill Sans MT" -> DejaVu Sans (execution mechanics only).
RUN printf '%s\n' \
    '<?xml version="1.0"?>' \
    '<!DOCTYPE fontconfig SYSTEM "fonts.dtd">' \
    '<fontconfig>' \
    '  <alias><family>Gill Sans MT</family><prefer><family>DejaVu Sans</family></prefer></alias>' \
    '</fontconfig>' > /etc/fonts/conf.d/99-gill-sans-fallback.conf \
    && fc-cache -f

# R packages named in the deposit README.txt, installed from the image's
# frozen 2024-02-28 P3M snapshot (Ubuntu 22.04 binaries).
RUN Rscript -e "install.packages(c('quanteda', 'readxl', 'ggplot2', 'dplyr', \
        'data.table', 'forcats', 'extrafont'))"

# Build-time assertion: every README pin must be met exactly.
RUN Rscript -e "\
  pins <- c(quanteda = '3.3.1', readxl = '1.4.3', ggplot2 = '3.5.0', \
            dplyr = '1.1.4', data.table = '1.15.0', forcats = '1.0.0', \
            extrafont = '0.19'); \
  got <- vapply(names(pins), function(p) as.character(packageVersion(p)), ''); \
  print(rbind(required = pins, installed = got)); \
  stopifnot(identical(unname(got), unname(pins))); \
  stopifnot(getRversion() == '4.3.2')"

WORKDIR /attempt

# The attempt directory is bind-mounted at /attempt at run time; the wrapper
# writes everything under /attempt/outputs.
CMD ["Rscript", "run-analysis.R"]
