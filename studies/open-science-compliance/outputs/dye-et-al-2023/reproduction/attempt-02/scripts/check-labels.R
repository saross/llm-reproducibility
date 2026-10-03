#!/usr/bin/env Rscript
## ===========================================================================
## check-labels.R — read-only transcription check (not the authors' code)
##
## Purpose
##   PDF line wrapping breaks the authors' string literals (column labels such
##   as "UB-6476 (BuD339)") across lines. A transcription slip would silently
##   drop a grave from a bead type, because the ArchaeoPhases functions index
##   MCMC columns by name. This script checks that every label used by the
##   transcribed code — section 3's `pos` and section 5's `bead_list` — exists
##   exactly as a column name of the verified beads-1.csv.
##
##   It also reports the column count after read_oxcal(), which bears on the
##   section 4 index vector c(3:5, 7, 9, 12:78).
##
## Usage (inside Docker): Rscript scripts/check-labels.R
## Output: outputs/checks/label-check.txt (non-zero exit if any label is missing)
## ===========================================================================

suppressPackageStartupMessages(library(ArchaeoPhases))
dir.create("outputs/checks", showWarnings = FALSE, recursive = TRUE)

ox <- read_oxcal("data/beads-1.csv", quiet = "yes")
cols <- colnames(ox)

## Evaluate section 5 (pure assignments) and section 3's `pos` in a sandbox.
sandbox <- new.env()
sys.source("authors-code/section-05-bead-classification.R", envir = sandbox)
sec3 <- parse("authors-code/section-03-replicability.R")
for (expr in sec3) {
  if (is.call(expr) && identical(expr[[1]], as.name("<-")) &&
      identical(expr[[2]], as.name("pos"))) eval(expr, sandbox)
}

bead_labels <- unique(unlist(sandbox$bead_list))
report <- c(
  sprintf("read_oxcal column count: %d (rows: %d)", length(cols), nrow(ox)),
  sprintf("section 3 pos: %d labels, %d missing from beads-1.csv",
          length(sandbox$pos), sum(!sandbox$pos %in% cols)),
  sprintf("section 3 pos identical to column order: %s",
          identical(as.character(sandbox$pos), cols)),
  sprintf("section 5 bead_list: %d bead types, %d distinct labels, %d missing",
          length(sandbox$bead_list), length(bead_labels),
          sum(!bead_labels %in% cols)),
  sprintf("bead_list names: %s", paste(names(sandbox$bead_list), collapse = ", ")),
  sprintf("bead_names: %s", paste(unlist(sandbox$bead_names), collapse = ", ")),
  "Labels per bead type:",
  sprintf("  %-14s n=%2d (distinct %2d)", names(sandbox$bead_list),
          lengths(sandbox$bead_list), sapply(sandbox$bead_list, function(x) length(unique(x)))),
  "Missing labels:",
  paste0("  ", c(setdiff(sandbox$pos, cols), setdiff(bead_labels, cols)))
)
writeLines(report, "outputs/checks/label-check.txt")
writeLines(report)

## Section 4 index check (read-only): which columns c(3:5, 7, 9, 12:78) select.
idx <- c(3:5, 7, 9, 12:78)
idx_report <- c(
  sprintf("section 4 index vector: %d indices, max %d; data columns: %d",
          length(idx), max(idx), length(cols)),
  sprintf("indices beyond the last column: %s",
          paste(idx[idx > length(cols)], collapse = ", "))
)
writeLines(idx_report, "outputs/checks/section-04-index-check.txt")
writeLines(idx_report)

if (any(!bead_labels %in% cols) || any(!sandbox$pos %in% cols)) quit(status = 1)
