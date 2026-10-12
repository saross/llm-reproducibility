# Probe environment for marwick-2025, compendium version 1.3 (Zenodo
# 10.5281/zenodo.15603267). The authors' Dockerfile, built as supplied on
# 2026-10-10, fails at renv::restore(): Posit Package Manager's current
# binary of rstan 2.32.7 cannot load against the lockfile's RcppParallel
# 5.1.10 (undefined symbol tbb::detail::r1::observe). This file repeats the
# authors' steps in a wrapper, leaving their Dockerfile untouched. One
# build-repair event, no version substitution: StanHeaders and rstan are
# built from CRAN source at their lockfile pins (2.32.10 and 2.32.7).
# (Comments reworded on 2026-10-11 after the build; instructions as built.)
FROM rocker/verse:4.4.1

ENV PROJ_DIR=/home/rstudio/web-of-science-archaeology
ENV RENV_PATHS_CACHE=/renv/cache
WORKDIR $PROJ_DIR
COPY . $PROJ_DIR
RUN chown -R rstudio:rstudio $PROJ_DIR
RUN R -e "install.packages('renv', repos = c(CRAN = 'https://cloud.r-project.org'))"

# The authors' restore, less the Stan stack and brms, its one importer.
RUN R -e "renv::restore(exclude = c('StanHeaders', 'rstan', 'brms'))"
# Repair: the same pinned versions, compiled from source.
RUN R -e "renv::install(c('StanHeaders@2.32.10', 'rstan@2.32.7'), type = 'source'); \
          stopifnot(packageVersion('rstan') == '2.32.7', packageVersion('StanHeaders') == '2.32.10'); \
          library(rstan)"
# The rest of the lockfile (brms at its pin).
RUN R -e "renv::restore(); stopifnot(packageVersion('brms') == '2.22.0'); library(brms)"

RUN chmod -R 777 /home/
# The authors' CI render of the main paper, kept as a build check.
RUN R -e "rmarkdown::render('analysis/paper/paper.qmd')"
