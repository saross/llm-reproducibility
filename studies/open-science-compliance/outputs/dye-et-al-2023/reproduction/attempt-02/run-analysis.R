#!/usr/bin/env Rscript
## ===========================================================================
## run-analysis.R — batch wrapper for the authors' R code
## Dye, Buck, DiNapoli & Philippe (2023), J. Archaeol. Sci. 153, 105765,
## supplement (mmc1.pdf) sections 3-10.
##
## Purpose
##   The authors' code is printed as interactive code blocks that are meant to
##   be pasted into one R session, in order, with section 5 (bead_list) run
##   before sections 6-10. This wrapper does exactly that, non-interactively:
##   it sources each transcribed section file (authors-code/) into a single
##   global environment, in supplement order, and captures each result to
##   outputs/.
##
## Wrapper cardinal rule (pipeline invariant 2)
##   This file changes HOW the code runs, never WHAT it computes. It adds only:
##     - directory creation and a console transcript (sink);
##     - a null default graphics device, so interactive dev.new() previews are
##       discarded instead of writing Rplots.pdf (the authors' file= outputs
##       are unaffected);
##     - error capture per section (tryCatch), so one failing block is recorded
##       rather than aborting the remaining, independent blocks;
##     - writes of objects the authors' code already computes (res$observed,
##       the occurrence/tempo plot data, bead_list) to CSV/RDS.
##   No statistical method, parameter, data filter, or analysis step is altered.
##   Section 3 is executed only if all five MCMC runs exist (plan step 7).
##
## Usage (inside Docker only; see Dockerfile and run-all.sh)
##   Rscript run-analysis.R
## ===========================================================================

dir.create("outputs/authors", showWarnings = FALSE, recursive = TRUE)
dir.create("outputs/logs", showWarnings = FALSE, recursive = TRUE)

## Discard interactive preview devices opened by dev.new() in batch mode.
options(device = function(...) grDevices::pdf(file = NULL))

transcript <- file("outputs/logs/run-analysis-transcript.txt", open = "wt")
sink(transcript, split = TRUE)
sink(transcript, type = "message")

cat("run-analysis.R started:", format(Sys.time(), tz = "UTC", usetz = TRUE), "\n")

## Record of each section's execution outcome.
status <- data.frame(section = character(), outcome = character(),
                     seconds = numeric(), message = character(),
                     stringsAsFactors = FALSE)

#' Source one transcribed section in the global environment, with capture.
#'
#' @param file Path to the transcribed section file.
#' @return The value of the section's last expression (source()$value), or
#'   NULL if the section raised an error.
run_section <- function(file) {
  cat("\n\n######## Sourcing", file, "########\n")
  t0 <- Sys.time()
  out <- tryCatch({
    v <- source(file, echo = TRUE, print.eval = TRUE, max.deparse.length = Inf,
                local = globalenv())
    list(ok = TRUE, value = v$value, msg = "")
  }, error = function(e) {
    cat("ERROR in", file, ":", conditionMessage(e), "\n")
    list(ok = FALSE, value = NULL, msg = conditionMessage(e))
  })
  secs <- as.numeric(difftime(Sys.time(), t0, units = "secs"))
  status[nrow(status) + 1, ] <<- list(basename(file),
                                      if (out$ok) "ok" else "error",
                                      round(secs, 1), out$msg)
  out$value
}

#' Write a section's res$observed matrix (unrounded and rounded to 2 dp).
#'
#' @param tag Output file stem, e.g. "section-07".
write_observed <- function(tag) {
  if (!exists("res", envir = globalenv())) return(invisible(NULL))
  obs <- get("res", envir = globalenv())$observed
  write.csv(obs, sprintf("outputs/authors/%s-observed-unrounded.csv", tag))
  write.csv(round(obs, 2), sprintf("outputs/authors/%s-observed-round2.csv", tag))
  saveRDS(obs, sprintf("outputs/authors/%s-observed.rds", tag))
  rm("res", envir = globalenv())   # so a failed later section cannot reuse it
  invisible(obs)
}

sec <- function(stem) file.path("authors-code", paste0(stem, ".R"))

## ---- Section 3: replicability across five runs (needs beads-0..4) --------
five_runs <- file.path("data", sprintf("beads-%d.csv", 0:4))
if (all(file.exists(five_runs))) {
  run_section(sec("section-03-replicability"))
  if (exists("foo")) write.csv(foo$range_table, "outputs/authors/section-03-range-table.csv")
} else {
  missing <- five_runs[!file.exists(five_runs)]
  cat("\nSection 3 NOT EXECUTED: missing inputs:", paste(missing, collapse = ", "), "\n")
  status[nrow(status) + 1, ] <- list("section-03-replicability.R", "not-executed", 0,
                                     paste("missing inputs:", paste(missing, collapse = ", ")))
}

## ---- Section 4: interment occurrence plot (paper Figure 3) ---------------
occ <- run_section(sec("section-04-occurrence-plot"))
if (!is.null(occ)) {
  saveRDS(occ, "outputs/authors/section-04-occurrence-plot-object.rds")
  write.csv(as.data.frame(occ$x), "outputs/authors/section-04-occurrence-intervals.csv",
            row.names = FALSE)
}

## ---- Section 5: bead classification (bead_list, bead_names) --------------
run_section(sec("section-05-bead-classification"))
if (exists("bead_list")) {
  saveRDS(list(bead_list = bead_list, bead_names = bead_names),
          "outputs/authors/section-05-bead-list.rds")
}

## ---- Sections 7-9: branching and reticulation relations ------------------
run_section(sec("section-07-stable-branching"));      write_observed("section-07")
run_section(sec("section-08-monochrome-branching"));  write_observed("section-08")
run_section(sec("section-09-dghnt-reticulation"));    write_observed("section-09")

## ---- Section 10: Bayliss et al. (2013) Table 7.18 rows 1-9 ---------------
for (r in 1:9) {
  stem <- grep(sprintf("^section-10-%d-", r), sub("\\.R$", "", list.files("authors-code")),
               value = TRUE)
  run_section(sec(stem))
  write_observed(sprintf("section-10-%d", r))
}

## ---- Section 6: bead deposition tempo plots (paper Figure 4) -------------
## Run last only because it is slow ("will run for a long time"); it is
## independent of sections 7-10 (each re-reads the MCMC file and only reads
## bead_list / bead_names), so the order does not affect any result.
foo <- NULL
run_section(sec("section-06-tempo-plot"))
if (!is.null(foo)) {
  saveRDS(foo, "outputs/authors/section-06-tempo-plot-object.rds")
  ## The returned object is a list of one data frame per bead type; stack them
  ## (with the bead type as a column) for the comparison script.
  parts <- unclass(foo)
  tempo_long <- do.call(rbind, lapply(names(parts), function(n) {
    cbind(bead_type = n, as.data.frame(parts[[n]]), stringsAsFactors = FALSE)
  }))
  write.csv(tempo_long, "outputs/authors/section-06-tempo-data.csv", row.names = FALSE)
}

write.csv(status, "outputs/logs/section-status.csv", row.names = FALSE)
print(status)

writeLines(capture.output(sessionInfo()), "outputs/logs/session-info.txt")
cat("\nrun-analysis.R finished:", format(Sys.time(), tz = "UTC", usetz = TRUE), "\n")
sink(type = "message")
sink()
