# =============================================================================
# run-analysis.R — batch wrapper for Herskind & Riede (2024) S2.R
# =============================================================================
# Reproduction attempt 02, run phase2-shakedown-2026-10.
#
# PURPOSE
#   Execute the authors' unmodified analysis script (data/Herskind&Riede_S2.R,
#   Zenodo 10.5281/zenodo.10801706 v2) non-interactively inside Docker, and
#   capture the console output and intermediate objects the paper's tables and
#   figures were hand-copied from.
#
# WRAPPER CARDINAL RULE (pipeline invariant 2)
#   This wrapper changes HOW S2.R runs, never WHAT it computes:
#     * S2.R is read verbatim and evaluated statement by statement, in its own
#       order, in the global environment. No authors' statement is edited,
#       removed, reordered, or added.
#     * Evaluation proceeds by the script's own "#PART n:" boundaries; between
#       parts the wrapper only WRITES copies of existing objects to CSV.
#     * Exactly one authors' statement is error-tolerant:
#       font_import(pattern = "GIL", prompt = FALSE). The authors' own comment
#       reports that it errors on their machine without affecting output; the
#       proprietary Gill Sans MT font is absent here. Any other error stops the
#       run.
#     * Interactive screen rendering (auto-printed ggplot objects) is routed to
#       a cairo PDF file, because Rscript's default pdf() device cannot resolve
#       the "Gill Sans MT" family name. ggsave() calls are untouched.
#
# USAGE (inside the container, attempt directory mounted at /attempt)
#   docker run --rm --mount type=bind,src=<attempt-dir>,dst=/attempt \
#       llmr-herskind-riede-2024-attempt-02 Rscript run-analysis.R
#
# OUTPUTS (all under outputs/)
#   Authors' own files: artefact_type_chronology.png, six Fig. 3 panel PNGs,
#     heatmapPMI.png, Bigrams.csv, Trigrams.csv, Quadrigrams.csv
#   Wrapper captures (prefixed "capture-"): console-equivalent tables and
#     intermediate objects saved between parts; console-plots.pdf;
#     session-info.txt
# =============================================================================

# ---- Execution set-up (mechanics only) --------------------------------------

attempt_root <- normalizePath(".")
script_path <- file.path(attempt_root, "data", "Herskind&Riede_S2.R")
data_path <- file.path(attempt_root, "data", "Herskind&Riede_S1.xlsx")
out_dir <- file.path(attempt_root, "outputs")
dir.create(out_dir, showWarnings = FALSE, recursive = TRUE)

# S2.R reads "Herskind&Riede_S1.xlsx" and writes PNG/CSV files relative to the
# working directory. Run from outputs/ with a temporary symbolic link to the
# data file, so the authors' relative paths resolve unchanged.
setwd(out_dir)
link_name <- "Herskind&Riede_S1.xlsx"
if (file.exists(link_name)) file.remove(link_name)
stopifnot(file.symlink(file.path("..", "data", link_name), link_name))

# Headless graphics: cairo bitmaps for ggsave(png); auto-printed plots go to a
# single cairo PDF (fontconfig resolves the Gill Sans MT alias to DejaVu Sans).
options(bitmapType = "cairo", width = 120, warn = 1)
options(device = function(...) {
  grDevices::cairo_pdf(filename = file.path(out_dir, "console-plots.pdf"),
                       onefile = TRUE)
})

#' Write a data frame copy to outputs/ with a "capture-" prefix.
#'
#' @param x A data frame (or object coercible to one) — an existing object.
#' @param name File stem; written as outputs/capture-<name>.csv.
#' @return Invisibly, the path written.
#' @examples
#' save_capture(data.frame(a = 1), "example")
save_capture <- function(x, name) {
  path <- file.path(out_dir, paste0("capture-", name, ".csv"))
  utils::write.csv(as.data.frame(x), path, row.names = FALSE,
                   fileEncoding = "UTF-8")
  invisible(path)
}

#' Write a table() object as level/count pairs.
#'
#' @param tab A one-way table() result.
#' @param name File stem.
#' @return Invisibly, the path written.
save_table <- function(tab, name) {
  save_capture(data.frame(level = names(tab), count = as.integer(tab)), name)
}

# ---- Read S2.R verbatim and split by its own PART headers -------------------

s2_lines <- readLines(script_path, encoding = "UTF-8", warn = FALSE)
part_starts <- grep("^#PART [0-9]+:", s2_lines)
stopifnot(length(part_starts) == 8)
part_ends <- c(part_starts[-1] - 1, length(s2_lines))
cat("S2.R lines:", length(s2_lines), "\n")
cat("Part boundaries (start-end lines):\n")
print(data.frame(part = 1:8, start = part_starts, end = part_ends))

# The single authors' statement allowed to fail (see header).
tolerated_call <- 'font_import(pattern = "GIL", prompt = FALSE)'

#' Evaluate one PART of S2.R statement by statement, echoing like
#' source(echo = TRUE): each statement's source text is printed with a prompt,
#' it is evaluated in the global environment, and visible values auto-print.
#'
#' @param part Part number (1-8).
#' @return Invisibly NULL. Stops on any error except the tolerated call.
run_part <- function(part) {
  cat("\n", strrep("=", 78), "\n", sep = "")
  cat(sprintf("== S2.R PART %d (lines %d-%d)\n", part, part_starts[part],
              part_ends[part]))
  cat(strrep("=", 78), "\n", sep = "")
  chunk <- s2_lines[part_starts[part]:part_ends[part]]
  exprs <- parse(text = chunk, keep.source = TRUE, encoding = "UTF-8")
  refs <- attr(exprs, "srcref")
  for (i in seq_along(exprs)) {
    src <- as.character(refs[[i]])
    cat(paste0(c("> ", rep("+ ", length(src) - 1)), src), sep = "\n")
    is_tolerated <- identical(trimws(src[1]), tolerated_call)
    result <- withCallingHandlers(
      tryCatch(
        withVisible(eval(exprs[[i]], envir = globalenv())),
        error = function(e) {
          if (is_tolerated) {
            cat("[wrapper] tolerated error at authors' font_import() call:",
                conditionMessage(e), "\n")
            return(list(value = NULL, visible = FALSE))
          }
          stop(e)
        }
      ),
      warning = function(w) {
        cat("[warning]", conditionMessage(w), "\n")
        invokeRestart("muffleWarning")
      },
      message = function(m) {
        cat("[message]", conditionMessage(m))
        invokeRestart("muffleMessage")
      }
    )
    if (isTRUE(result$visible)) print(result$value)
  }
  invisible(NULL)
}

# ---- Execute the eight parts, capturing objects between parts ---------------

run_part(1)
cat("[wrapper] nrow(data) =", nrow(data), "; ncol(data) =", ncol(data), "\n")

run_part(2)
# Fig. 2 bar panel: per-type x chronology counts of the authors' DS object.
save_capture(as.data.frame(table(Artefact_Type = DS$Artefact_Type,
                                 Chronology = DS$Chronology)),
             "fig2-artefact-type-by-chronology")

run_part(3)
save_capture(bigrams, "part3-bigrams-all")
save_capture(trigrams, "part3-trigrams-all")
save_capture(quadrigrams, "part3-quadrigrams-all")
cat("[wrapper] corpus documents =", quanteda::ndoc(corpus), "; t =", t, "\n")

run_part(4)
# Table 1: the four table() outputs and four length() outputs.
save_table(table(freqs), "table1-unigram-frequencies")
save_table(table(bigramfreqs), "table1-bigram-frequencies")
save_table(table(trigramfreqs), "table1-trigram-frequencies")
save_table(table(quadrigramfreqs), "table1-quadrigram-frequencies")
save_capture(data.frame(
  level = c("unigrams", "bigrams", "trigrams", "quadrigrams"),
  total = c(length(freqs), length(bigramfreqs), length(trigramfreqs),
            length(quadrigramfreqs))), "table1-totals")

run_part(5)
# Table 2: full-precision summary() values per culture complex.
table2 <- do.call(rbind, lapply(
  list(Maglemose = magle_ksngram_subset, Kongemose = konge_ksngram_subset,
       `Ertebølle` = erte_ksngram_subset),
  function(s) {
    v <- summary(s$PMI)
    data.frame(statistic = names(v), value = sprintf("%.15g", as.numeric(v)),
               n_bigrams = nrow(s))
  }))
table2$complex <- sub("\\..*$", "", rownames(table2))
save_capture(table2, "table2-pmi-summary")
cat("[wrapper] subset sizes: Maglemose", nrow(maglemosedata), "Kongemose",
    nrow(kongemosedata), "Ertebølle", nrow(ertebølledata), "\n")

run_part(6)
# Fig. 3: each authors' ggplot object stores its stacked-bar data (the
# skipgramsFreq/skipgramsPMI table current when it was built) and its label
# layer data (summary_freq/summary_pmi). Copy both, read-only.
fig3_panels <- list(a = bigramsBYfrequency, b = bigramsBYpmi,
                    c = trigramsBYfrequency, d = trigramsBYpmi,
                    e = quadrigramsBYfrequency, f = quadrigramsBYpmi)
for (p in names(fig3_panels)) {
  plot_obj <- fig3_panels[[p]]
  save_capture(plot_obj$data, paste0("fig3", p, "-bars"))
  labels <- plot_obj$layers[[2]]$data
  labels$label_4dp <- sprintf("%.4f", labels$PMI)
  labels$PMI <- sprintf("%.15g", labels$PMI)
  save_capture(labels, paste0("fig3", p, "-labels"))
  # Bar order on the y axis as ggplot builds it (bottom to top).
  built <- ggplot2::ggplot_build(plot_obj)
  save_capture(data.frame(position = seq_along(built$layout$panel_params[[1]]$y$get_labels()),
                          skipgram = built$layout$panel_params[[1]]$y$get_labels()),
               paste0("fig3", p, "-axis-order"))
}
# Full-corpus bigrams (uppercased ksngrams) before Part 7 subsets them.
bigrams_full_part6 <- bigrams
bigrams_full_part6$PMI <- sprintf("%.15g", bigrams_full_part6$PMI)
save_capture(bigrams_full_part6, "part6-bigrams-full")
rm(bigrams_full_part6)

run_part(7)
heatmap_cells <- df
heatmap_cells$PMI <- sprintf("%.15g", heatmap_cells$PMI)
save_capture(heatmap_cells, "fig4-heatmap-cells")
rm(heatmap_cells)

run_part(8)

# ---- Close-out --------------------------------------------------------------

while (!is.null(grDevices::dev.list())) grDevices::dev.off()
file.remove(link_name)
writeLines(utils::capture.output(sessionInfo()), file.path(out_dir, "session-info.txt"))
cat("\n[wrapper] completed:", format(Sys.time(), tz = "UTC", usetz = TRUE), "\n")
