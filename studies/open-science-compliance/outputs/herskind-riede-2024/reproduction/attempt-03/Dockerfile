# Dockerfile — Herskind & Riede 2024 (JAS 165, 105969), reproduction attempt 03
#
# Purpose: build the execution environment for the authors' S2.R (Zenodo record
# 10801706, version 2). The authors supplied no container or lockfile, only a
# README stating R 4.3.2 and seven exact package versions (environment-
# specification level 2). The base image is therefore the reproducer's choice,
# and its built-in package-manager snapshot date (2024-02-28) is NOT the
# authors'. It is overridden below (invariant 2, "Package repository dates"):
#
#   - the seven README pins are built from their own CRAN source tarballs
#     (https://cloud.r-project.org/src/contrib/Archive/<pkg>/), and
#   - every package the authors left unspecified comes from the Posit Package
#     Manager snapshot dated to the article's first online appearance,
#     2024-04-03 (Ubuntu jammy binaries).
#
# Nothing from the attempt directory is copied into the image: the lane mounts
# the checked work copy at WORKDIR at run time. No R start-up file is edited.
#
# Build (from the repository root; label = this file's sha256):
#   docker build --label llmr.dockerfile.sha256=<sha256 of this file> \
#     -t llmr-herskind-riede-2024-attempt-03 <attempt dir>

FROM rocker/r-ver:4.3.2@sha256:4e32addfc4da3e660f6e0d05ce5e43d3eceb9db58a60b9a142e0dde9a654ead1

# UTF-8 locale: S2.R uses the identifier ertebølledata and the literal
# "Ertebølle" (rocker/r-ver already generates en_US.UTF-8).
ENV LANG=en_US.UTF-8 \
    LC_ALL=en_US.UTF-8

# System libraries: compilers come with rocker/r-ver. libxml2/libicu/zlib for
# xml2, stringi, and data.table; fontconfig plus DejaVu so that the PNG device
# has a fallback font (Gill Sans MT is proprietary and unavailable) and so that
# extrafont::font_import() has a system font directory to scan.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        curl \
        ca-certificates \
        libxml2-dev \
        libicu-dev \
        zlib1g-dev \
        libfontconfig1-dev \
        libfreetype6-dev \
        fontconfig \
        fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*

# Step 1: fetch the seven pinned source tarballs from CRAN's archive and print
# their sha256 into the build log.
RUN mkdir -p /opt/llmr/pins \
    && cd /opt/llmr/pins \
    && for pv in extrafont_0.19 data.table_1.15.0 dplyr_1.1.4 ggplot2_3.5.0 \
                 readxl_1.4.3 quanteda_3.3.1 forcats_1.0.0; do \
         p="${pv%_*}"; \
         curl -fsSL -o "${pv}.tar.gz" \
           "https://cloud.r-project.org/src/contrib/Archive/${p}/${pv}.tar.gz" || exit 1; \
       done \
    && sha256sum ./*.tar.gz

# Step 2: dependencies the authors left unspecified. Read the Depends, Imports,
# and LinkingTo fields of each pinned version's own DESCRIPTION, drop the pins
# themselves and anything already installed with R (base and recommended), and
# install the rest (recursively) from the 2024-04-03 snapshot. A missing
# package after installation fails the build.
RUN Rscript -e "\
  pins <- c(extrafont = '0.19', data.table = '1.15.0', dplyr = '1.1.4', \
            ggplot2 = '3.5.0', readxl = '1.4.3', quanteda = '3.3.1', forcats = '1.0.0'); \
  options(repos = c(CRAN = 'https://packagemanager.posit.co/cran/__linux__/jammy/2024-04-03')); \
  descs <- lapply(names(pins), function(p) { \
    tf <- sprintf('/opt/llmr/pins/%s_%s.tar.gz', p, pins[[p]]); \
    ex <- tempfile(); untar(tf, files = paste0(p, '/DESCRIPTION'), exdir = ex); \
    read.dcf(file.path(ex, p, 'DESCRIPTION')) }); \
  fields <- c('Depends', 'Imports', 'LinkingTo'); \
  db <- do.call(rbind, lapply(descs, function(d) { \
    m <- matrix(NA_character_, 1, 1 + length(fields), dimnames = list(NULL, c('Package', fields))); \
    m[1, 'Package'] <- d[1, 'Package']; \
    for (f in fields) if (f %in% colnames(d)) m[1, f] <- d[1, f]; m })); \
  deps <- unique(unlist(tools::package_dependencies(names(pins), db = db, which = fields))); \
  have <- rownames(installed.packages()); \
  need <- setdiff(deps, c('R', names(pins), have)); \
  cat('Unspecified direct dependencies to install:', need, '\n'); \
  install.packages(need, dependencies = c('Depends', 'Imports', 'LinkingTo')); \
  miss <- setdiff(need, rownames(installed.packages())); \
  if (length(miss)) stop('not installed: ', paste(miss, collapse = ', ')); \
  bad <- intersect(names(pins), rownames(installed.packages())); \
  if (length(bad)) stop('a pinned package was installed from the snapshot: ', paste(bad, collapse = ', '))"

# Step 3: the seven pins, built from source at exactly the README versions. A
# build failure is promoted from a warning to an error, and the installed
# versions are asserted.
RUN Rscript -e "\
  pins <- c(extrafont = '0.19', data.table = '1.15.0', dplyr = '1.1.4', \
            ggplot2 = '3.5.0', readxl = '1.4.3', quanteda = '3.3.1', forcats = '1.0.0'); \
  tars <- sprintf('/opt/llmr/pins/%s_%s.tar.gz', names(pins), pins); \
  withCallingHandlers(install.packages(tars, repos = NULL, type = 'source'), \
    warning = function(w) stop('pinned build failed: ', conditionMessage(w))); \
  got <- vapply(names(pins), function(p) as.character(packageVersion(p)), ''); \
  print(cbind(pinned = pins, installed = got)); \
  if (!identical(unname(got), unname(pins))) stop('pinned version mismatch')"

# Step 4: inventory. Every installed package with its version, library, and
# provenance class (pinned / unspecified / bundled with R), written inside the
# image so that the run can copy it into its sealed outputs.
RUN Rscript -e "\
  pins <- c('extrafont', 'data.table', 'dplyr', 'ggplot2', 'readxl', 'quanteda', 'forcats'); \
  ip <- as.data.frame(installed.packages(fields = 'Repository')[, c('Package', 'Version', 'LibPath', 'Priority', 'Repository')], stringsAsFactors = FALSE); \
  ip\$class <- ifelse(ip\$Package %in% pins, 'pinned (README; CRAN Archive source)', \
               ifelse(!is.na(ip\$Priority), paste('bundled with R 4.3.2 (', ip\$Priority, ')', sep = ''), \
                      'unspecified (P3M snapshot 2024-04-03)')); \
  ip <- ip[order(ip\$class, ip\$Package), ]; \
  write.csv(ip, '/opt/llmr/package-inventory.csv', row.names = FALSE); \
  print(ip[, c('Package', 'Version', 'class')], row.names = FALSE); \
  cat('capabilities: cairo =', capabilities('cairo'), ' png =', capabilities('png'), '\n')"

# extrafont::font_import() writes its font table into the extrafontdb package
# directory. The lane runs as a non-root user, so the directory is made
# writable to keep the authors' statement behaving as it did for them (it can
# still fail for want of Gill Sans MT; see run-analysis.R).
RUN chmod -R a+rwX /usr/local/lib/R/site-library/extrafontdb

WORKDIR /project
