# Dockerfile for Key et al. 2024 OLE reproduction
# Paper: "Identifying accurate artefact morphological ranges using optimal
#         linear estimation: Method validation, case studies, and code"
# Journal of Archaeological Science 162, 105921
#
# Type C reproduction: interactive scripts without Dockerfile, no renv
# Only base R needed — OLE function uses no external packages
#
# Build:  docker build -t reproduction-key-et-al-2024 .
# Run:    docker run --rm -v $(pwd)/outputs:/analysis/outputs \
#           reproduction-key-et-al-2024

FROM rocker/r-ver:4.3.2

LABEL maintainer="Reproduction pipeline"
LABEL description="Key et al. 2024 OLE morphometric range estimation"
LABEL paper.doi="10.1016/j.jas.2024.105921"

WORKDIR /analysis

# Copy wrapper script
COPY run-analysis.R /analysis/

# Copy source data
COPY source-data/olduvai-cleavers-key-et-al-2024.csv /analysis/data/
COPY source-data/key-et-al-2024-paleoindian-points.csv /analysis/data/

# Create output directory and .here sentinel
RUN mkdir -p /analysis/outputs && touch /analysis/.here

CMD ["Rscript", "--vanilla", "run-analysis.R"]
