#!/usr/bin/env Rscript
# =============================================================================
# run-analysis.R — execution wrapper for Herskind & Riede 2024, S2.R
# Reproduction attempt 03 (run gate-1-3-pilot-rerun-2026-10)
# =============================================================================
#
# Purpose
#   Run the authors' "Herskind&Riede_S2.R" (Zenodo 10.5281/zenodo.10801706,
#   version 2) byte-identical and non-interactively, inside the lane container.
#   This file changes HOW the script runs, never WHAT it computes (invariant 2).
#
# What the wrapper does (all mechanics, each declared in log.md)
#   1. Creates a working directory, authors-run/, and copies the deposited data
#      file S1.xlsx into it, because S2.R reads "Herskind&Riede_S1.xlsx" by a
#      relative path and writes its PNG and CSV outputs to the same directory.
#   2. Parses the pristine S2.R once (parse(file =), UTF-8; the file has CRLF
#      line endings and non-ASCII identifiers) and evaluates its top-level
#      expressions in the script's own order in the global environment, as
#      Rscript would. No expression is skipped, re-ordered, or altered.
#   3. Prints each visible value, reproducing Rscript's auto-printing of
#      table(), summary(), length(), head(), and ggplot objects (Table 1 and
#      Table 2 are hand-copied from this printed output in the paper).
#   4. Per-expression error capture. The ONLY declared error tolerance is the
#      authors' font_import(pattern = "GIL", prompt = FALSE) on S2.R line 27,
#      which registers a proprietary font (Gill Sans MT) and computes nothing
#      that enters a result (invariant 2, Q6 ruling). Whether it fired is
#      recorded. Any other error is recorded too, and the run continues so the
#      log shows everything, but the expression log marks it and no target is
#      credited from a section downstream of a failed expression.
#   5. Routes warnings and messages to standard output with the index of the
#      expression that raised them (output capture only).
#   6. Read-only captures: a copy of `bigrams` taken immediately before S2.R
#      line 633 (`bigrams <- subset(bigrams, observed_freq > 2)`, Part 7) reads
#      it, because Part 7 overwrites the full-corpus object; then, after the
#      script ends, the whole session (save.image) for the comparison script,
#      sessionInfo(), and the image's package inventory.
#
# Usage (through the lane only; never on the host):
#   run-container <attempt dir> --image llmr-herskind-riede-2024-attempt-03 \
#     --entry run-reproduction.sh --launch-commit <commit>
#
# Outputs (in the work copy; the lane seals them under outputs/run-NN/files/)
#   authors-run/                       S2.R's own outputs (8 PNGs, 3 CSVs, Rplots.pdf)
#   wrapper-captures/expression-log.csv  one row per top-level expression
#   wrapper-captures/bigrams-before-part7.rds
#   wrapper-captures/authors-session.RData
#   wrapper-captures/session-info.txt
#   wrapper-captures/package-inventory.csv
# =============================================================================

# The whole wrapper runs inside local(): its own variables (loop index,
# logs, paths) never enter the global environment where the authors'
# expressions are evaluated. S2.R line 642 runs its own `for (i in ...)`
# loop in the global environment, so a global wrapper index would be
# overwritten, and authors' code could otherwise see wrapper objects.
local({
  # ---- 0. Paths ---------------------------------------------------------------
  project_root <- getwd()
  authors_script <- file.path(project_root, "materials", "Herskind&Riede_S2.R")
  data_source <- file.path(project_root, "materials", "Herskind&Riede_S1.xlsx")
  run_dir <- file.path(project_root, "authors-run")
  capture_dir <- file.path(project_root, "wrapper-captures")

  # S2.R line on which Part 7 overwrites the full-corpus `bigrams` object.
  PART7_SUBSET_LINE <- 633L
  # S2.R line of the one statement whose error is tolerated (font registration).
  FONT_IMPORT_LINE <- 27L

  dir.create(run_dir, showWarnings = FALSE)
  dir.create(capture_dir, showWarnings = FALSE)

  # Integrity record before execution: the executed copy must equal the
  # retrieved original (sha256 recorded in authors-code-manifest.json).
  cat("LLMR: S2.R md5 before run:", unname(tools::md5sum(authors_script)), "\n")

  # ---- 1. Data into the authors' working directory ----------------------------
  stopifnot(file.copy(data_source, file.path(run_dir, "Herskind&Riede_S1.xlsx"),
                      overwrite = TRUE))

  # ---- 2. Parse the pristine script once --------------------------------------
  # keep.source = TRUE only to read each expression's line numbers (srcref) for
  # the expression log and the Part 7 capture point; it changes no computation.
  exprs <- parse(file = "materials/Herskind&Riede_S2.R", encoding = "UTF-8",
                 keep.source = TRUE)
  refs <- attr(exprs, "srcref")
  cat("LLMR: parsed", length(exprs), "top-level expressions from S2.R\n")

  setwd(run_dir)

  # Display device (mechanic, declared in log.md). S2.R auto-prints ggplot
  # objects at the top level (lines 70, 411, 432, 607-612, 690), as the
  # authors did in an interactive session. Under Rscript the default device
  # is pdf(), whose font database rejects the unregistered family
  # "Gill Sans MT" with an error; an interactive screen device does not. A
  # cairo PNG device stands in for the screen, one file per page. It changes
  # where those display-only prints go, not what any expression computes;
  # the authors' own ggsave() calls choose their device themselves.
  options(device = function(...) {
    grDevices::png(filename = file.path(run_dir, "screen-device-%02d.png"),
                   width = 7, height = 7, units = "in", res = 100, type = "cairo")
  })

  # ---- 3-5. Evaluate in order, print visible values, capture conditions -------
  expression_log <- data.frame(index = seq_along(exprs),
                               first_line = vapply(refs, function(r) r[1], integer(1)),
                               last_line = vapply(refs, function(r) r[3], integer(1)),
                               status = NA_character_, warnings = 0L, messages = 0L,
                               error = NA_character_, stringsAsFactors = FALSE)
  font_tolerance_fired <- FALSE
  part7_captured <- FALSE

  for (i in seq_along(exprs)) {
    first_line <- expression_log$first_line[i]
    # Read-only capture of the full-corpus bigram table before Part 7 subsets it.
    if (first_line == PART7_SUBSET_LINE) {
      saveRDS(get("bigrams", envir = globalenv()),
              file.path(capture_dir, "bigrams-before-part7.rds"))
      part7_captured <- TRUE
      cat("LLMR: captured `bigrams` before S2.R line", PART7_SUBSET_LINE, "\n")
    }
    cat(sprintf("\nLLMR-EXPR %d (S2.R lines %d-%d)\n", i, first_line,
                expression_log$last_line[i]))
    counts <- new.env()
    counts$warn <- 0L
    counts$msg <- 0L
    outcome <- tryCatch(
      withCallingHandlers(
        {
          result <- withVisible(eval(exprs[[i]], envir = globalenv()))
          if (result$visible) print(result$value)
          "ok"
        },
        warning = function(w) {
          counts$warn <- counts$warn + 1L
          cat("LLMR-WARNING [expr ", i, "]: ", conditionMessage(w), "\n", sep = "")
          invokeRestart("muffleWarning")
        },
        message = function(m) {
          counts$msg <- counts$msg + 1L
          cat("LLMR-MESSAGE [expr ", i, "]: ", conditionMessage(m), sep = "")
          invokeRestart("muffleMessage")
        }),
      error = function(e) {
        cat("LLMR-ERROR [expr ", i, "]: ", conditionMessage(e), "\n", sep = "")
        conditionMessage(e)
      })
    expression_log$warnings[i] <- counts$warn
    expression_log$messages[i] <- counts$msg
    if (identical(outcome, "ok")) {
      expression_log$status[i] <- "ok"
    } else if (first_line == FONT_IMPORT_LINE) {
      # Declared tolerance (font registration only; computes nothing used).
      expression_log$status[i] <- "error-tolerated (declared: font registration)"
      expression_log$error[i] <- outcome
      font_tolerance_fired <- TRUE
    } else {
      expression_log$status[i] <- "ERROR"
      expression_log$error[i] <- outcome
    }
  }

  setwd(project_root)

  # ---- 6. Captures after the script ends --------------------------------------
  write.csv(expression_log, file.path(capture_dir, "expression-log.csv"), row.names = FALSE)
  cat("\nLLMR: font_import tolerance fired:", font_tolerance_fired, "\n")
  cat("LLMR: Part 7 capture taken:", part7_captured, "\n")
  cat("LLMR: expressions with an untolerated error:",
      sum(expression_log$status == "ERROR"), "\n")

  # The authors' finished session, for the comparison script (read-only use).
  save(list = ls(envir = globalenv(), all.names = TRUE), envir = globalenv(),
       file = file.path(capture_dir, "authors-session.RData"))

  writeLines(c(capture.output(sessionInfo()),
               paste("Sys.getlocale():", Sys.getlocale()),
               paste("capabilities cairo:", capabilities("cairo")),
               paste("png bitmapType:", getOption("bitmapType"))),
             file.path(capture_dir, "session-info.txt"))
  file.copy("/opt/llmr/package-inventory.csv",
            file.path(capture_dir, "package-inventory.csv"), overwrite = TRUE)

  cat("LLMR: S2.R md5 after run:", unname(tools::md5sum(authors_script)), "\n")
  cat("LLMR: run-analysis.R finished\n")
})
