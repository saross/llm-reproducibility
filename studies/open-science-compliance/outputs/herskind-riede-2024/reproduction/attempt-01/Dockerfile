FROM rocker/r-ver:4.2.2

# System dependencies for readxl, extrafont, etc.
RUN apt-get update && apt-get install -y \
    libxml2-dev \
    libfontconfig1-dev \
    fonts-dejavu \
    && rm -rf /var/lib/apt/lists/*

# Install R packages
RUN R -e 'install.packages(c("quanteda", "readxl", "ggplot2", "dplyr", "data.table", "extrafont"))'

# Register available system fonts for extrafont
RUN R -e 'extrafont::font_import(prompt=FALSE)'

WORKDIR /analysis
