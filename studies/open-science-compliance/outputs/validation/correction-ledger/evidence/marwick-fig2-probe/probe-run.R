# Probe wrapper for MAR-T10 (correction-ledger ruling L17 (c), 2026-10-10).
#
# Runs the code of supplement-GAMS-details.qmd's single `eval: false` chunk
# (the authors' brms fit, "this takes a few hours") verbatim, after the
# chunks that precede it in document order, then renders the supplement
# unchanged so that its unconditional readRDS() loads the saved fit and its
# fig-smooth-plots-paper chunk redraws Fig. 2. No authors' file is edited:
# chunk code is read from the .qmd at run time and its text hash recorded.
#
# Usage (inside the probe image, from the project directory):
#   Rscript /probe/probe-run.R smoke   # data rows per variable, a tiny fit
#   Rscript /probe/probe-run.R full    # the authors' fit, then the render
#
# Outputs go to /out: run log lines on stdout, chunk hashes, session info,
# the saved fit's size, the rendered supplement, and the redrawn figure.

args <- commandArgs(trailingOnly = TRUE)
mode <- if (length(args)) args[[1]] else "smoke"
stopifnot(mode %in% c("smoke", "full"))

qmd <- "analysis/paper/supplement-GAMS-details.qmd"
out <- "/out"
stamp <- function(...) cat(format(Sys.time(), "%Y-%m-%dT%H:%M:%S%z"), ..., "\n")

# --- Parse the .qmd into R chunks (fence lines are never executed) -------
lines <- readLines(qmd, warn = FALSE)
starts <- grep("^```\\{r", lines)
fences <- grep("^```\\s*$", lines)
chunks <- lapply(starts, function(s) {
  e <- fences[fences > s][1]
  list(start = s, end = e, code = lines[seq.int(s + 1, e - 1)])
})
disabled <- which(vapply(chunks, function(ch) any(grepl("^#\\|\\s*eval:\\s*false", ch$code)),
                         logical(1)))
stopifnot(length(disabled) == 1)  # exactly one switched-off chunk
hash <- function(x) digest::digest(paste(x, collapse = "\n"), algo = "sha256", serialize = FALSE)
for (i in seq_len(disabled)) {
  stamp(sprintf("chunk %d: lines %d-%d, sha256 %s%s", i, chunks[[i]]$start, chunks[[i]]$end,
                hash(chunks[[i]]$code), if (i == disabled) " (eval: false)" else ""))
}

# Timestamp the authors' message() calls, e.g. "Fitting brms model for: ...".
run_chunk <- function(ch) {
  withCallingHandlers(
    eval(parse(text = ch$code), envir = globalenv()),
    message = function(m) {
      stamp("message:", trimws(conditionMessage(m)))
      invokeRestart("muffleMessage")
    }
  )
}

# --- Chunks before the switched-off one, in document order ---------------
for (i in seq_len(disabled - 1)) {
  stamp(sprintf("running chunk %d", i))
  run_chunk(chunks[[i]])
}
rows <- vapply(over_time_long_colour_gams_testing_nested_df$data, nrow, integer(1))
names(rows) <- over_time_long_colour_gams_testing_nested_df$variable
stamp("rows per variable:", paste(names(rows), rows, sep = " = ", collapse = "; "))

if (mode == "smoke") {
  # Toolchain check only: one short chain on the first variable, same family
  # rules as the authors' chunk would choose for a Gaussian variable.
  library(brms)
  d <- over_time_long_colour_gams_testing_nested_df$data[[
    which(over_time_long_colour_gams_testing_nested_df$variable == "Diversity of references")]]
  t0 <- Sys.time()
  m <- brm(bf(value ~ s(year, bs = "cr")), family = gaussian(), data = d,
           prior = prior(exponential(1), class = "sds"),
           chains = 1, iter = 400, warmup = 200, seed = 123, refresh = 0, silent = 2)
  stamp("smoke fit OK in", format(round(difftime(Sys.time(), t0, units = "mins"), 2)))
  print(summary(m))
  quit(status = 0)
}

# --- The switched-off chunk, verbatim -------------------------------------
stamp(sprintf("running chunk %d (eval: false), detectCores() = %d", disabled,
              parallel::detectCores()))
t0 <- Sys.time()
run_chunk(chunks[[disabled]])
stamp("fit chunk done in", format(round(difftime(Sys.time(), t0, units = "hours"), 2)))
rds <- here::here("analysis/data/results_brms.RData")
stamp("saved fit:", rds, file.size(rds), "bytes")
writeLines(capture.output(sessionInfo()), file.path(out, "session-info.txt"))

# --- Render the supplement unchanged --------------------------------------
fig <- here::here("analysis/figures/fig-smooth-plots-paper.png")
file.copy(fig, file.path(out, "fig-smooth-plots-paper-deposited.png"), overwrite = TRUE)
t1 <- Sys.time()
rmarkdown::render(qmd, output_dir = out, quiet = TRUE)
stamp("render done in", format(round(difftime(Sys.time(), t1, units = "mins"), 2)))
file.copy(fig, file.path(out, "fig-smooth-plots-paper-probe.png"), overwrite = TRUE)
stamp("probe complete")
