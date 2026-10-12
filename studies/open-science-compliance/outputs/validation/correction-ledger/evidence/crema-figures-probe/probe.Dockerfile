# Probe environment for crema-et-al-2024, deposit v1.0.0 (Zenodo).
# Constructed per reproduction-system/prompts/01-preparation.md §2.2: the
# deposit has no Dockerfile, so the R version and attached packages come from
# the README's session info (R 4.3.1). rocker/r-ver:4.3.1 installs from a
# dated Posit Package Manager snapshot; the attached packages are pinned to
# the session-info versions with remotes::install_version.
FROM rocker/r-ver:4.3.1

RUN apt-get update && apt-get install -y --no-install-recommends \
      libgdal-dev libgeos-dev libproj-dev libudunits2-dev libssl-dev \
      libcurl4-openssl-dev libxml2-dev libfontconfig1-dev libglpk-dev \
      poppler-utils git \
    && rm -rf /var/lib/apt/lists/*

RUN R -q -e "install.packages('remotes')"
RUN R -q -e "v <- c(truncnorm='1.0-9', here='1.0.1', coda='0.19-4', latex2exp='0.9.6', \
      RColorBrewer='1.1-3', dplyr='1.1.2', nimble='1.0.1', sf='1.0-14', \
      rnaturalearth='0.3.3', rcarbon='1.5.0'); \
      for (p in names(v)) remotes::install_version(p, version = v[[p]], upgrade = 'never'); \
      ip <- installed.packages()[, 'Version']; stopifnot(all(ip[names(v)] == v))"
# Logged fallback (amendment 3 §7(d) version search): the session info's
# nimbleCarbon 0.2.4 was never released (CRAN archive: 0.1.1, 0.1.2, 0.2.1,
# 0.2.5; GitHub tags: v0.1.1, v0.2.5), so the pin cannot be built. The
# immediately preceding release, 0.2.1, is tried first. figures_main.R only
# attaches the package; the figures call base graphics, rcarbon, and the
# deposit's src/utility.R.
RUN R -q -e "remotes::install_version('nimbleCarbon', version = '0.2.1', upgrade = 'never'); \
      stopifnot(packageVersion('nimbleCarbon') == '0.2.1')"
# rnaturalearthhires is not on CRAN. Amendment 3 §7(d): a GitHub dependency
# is pinned to the tagged release current at publication. The paper was
# available online 2024-03-16; the tag then current is v1.0.0 (2023-12-12,
# commit db8e433bfb80dc775f04bd5b0d8911fa6b9a568c).
RUN R -q -e "remotes::install_github('ropensci/rnaturalearthhires@v1.0.0', upgrade = 'never'); \
      stopifnot(packageVersion('rnaturalearthhires') == '1.0.0')"
WORKDIR /work
