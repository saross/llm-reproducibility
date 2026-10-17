# =============================================================================
# run-analysis.R -- wrapper for herskind-riede-2024, reproduction attempt 04
#
# Runs the authors' deposited script, deposit/Herskind&Riede_S2.R (Zenodo
# record 10801706, sha256 487a00a0...8720), byte-identical, through the
# lane's evaluator, then saves the authors' own objects for comparison.
#
# Execution mechanics only (invariant 2, wrapper cardinal rule):
#   1. Working directory: deposit/, where S2.R expects
#      "Herskind&Riede_S1.xlsx" and writes its PNGs and CSVs.
#   2. Default graphics device: a cairo PNG device instead of Rscript's
#      default pdf(). S2.R prints its ggplot objects (lines 70, 411, 432,
#      607-612, 690), which in the authors' RStudio session went to the
#      on-screen device; pdf() has no "Gill Sans MT" font family and would
#      stop at the first print. ggsave() opens its own device either way, so
#      the saved figures are unaffected.
#   3. Error tolerance on S2.R line 27 only, font_import(pattern = "GIL",
#      prompt = FALSE): it registers fonts and computes nothing that enters a
#      result (planned and declared; RULED 2026-10-05, executed-code audit
#      Q6). The lane's evaluator records whether it fired.
#   4. Output capture after the script ends: the authors' objects (tables,
#      summaries, plot data, matrix m) are written under captured/ without
#      recomputing anything.
# No statistical method, parameter, data filter, model specification, or
# analysis step is changed. The wrapper's own objects stay inside local().
# =============================================================================

local({
  root <- getwd()                       # the lane's mount path (/project)
  captured <- file.path(root, "captured")
  dir.create(captured, showWarnings = FALSE)

  # Provenance: the executed copy must be the deposited file (checked again
  # by the gate from the run's own records).
  authors_file <- file.path(root, "deposit", "Herskind&Riede_S2.R")
  expected <- "487a00a09db92b484dac136f13a5745a3a2ac699c3a01cfccf528d4d550a8720"
  digest_line <- system2("sha256sum", shQuote(authors_file), stdout = TRUE)
  stopifnot(identical(strsplit(digest_line, " ")[[1]][1], expected))

  # Mechanic 2: on-screen-equivalent default device (cairo PNG files).
  options(device = function(...) {
    grDevices::png(filename = "Rplot%03d.png", type = "cairo",
                   width = 7, height = 7, units = "in", res = 96)
  })

  # Mechanics 1 and 3: run the authors' script statement by statement.
  setwd(file.path(root, "deposit"))
  getOption("lane.hook")$run_file("Herskind&Riede_S2.R", tolerate = 27L,
                                  encoding = "UTF-8")
  while (grDevices::dev.cur() > 1L) grDevices::dev.off()
  setwd(root)

  # Mechanic 4: capture the authors' objects (no recomputation).
  g <- globalenv()
  get_g <- function(name) get(name, envir = g, inherits = FALSE)

  # Table 1: the four frequency tables and lengths S2.R prints (Part 4).
  t1 <- do.call(rbind, lapply(c(unigrams = "freqs", bigrams = "bigramfreqs",
                                trigrams = "trigramfreqs",
                                quadrigrams = "quadrigramfreqs"), function(obj) {
    tab <- table(get_g(obj))
    data.frame(object = obj, frequency = as.integer(names(tab)),
               n = as.integer(tab), stringsAsFactors = FALSE)
  }))
  t1$level <- sub("\\..*", "", rownames(t1))
  write.csv(t1[order(t1$level, -t1$frequency), c("level", "object", "frequency", "n")],
            file.path(captured, "table1-reproduced.csv"), row.names = FALSE)
  write.csv(data.frame(level = c("unigrams", "bigrams", "trigrams", "quadrigrams"),
                       n_types = c(length(get_g("freqs")), length(get_g("bigramfreqs")),
                                   length(get_g("trigramfreqs")),
                                   length(get_g("quadrigramfreqs")))),
            file.path(captured, "table1-totals-reproduced.csv"), row.names = FALSE)

  # Table 2: the three summaries S2.R prints (Part 5), at full precision.
  t2 <- sapply(c(maglemose = "magle_ksngram_subset", kongemose = "konge_ksngram_subset",
                 ertebolle = "erte_ksngram_subset"), function(obj) {
    unclass(summary(get_g(obj)$PMI))
  })
  t2 <- data.frame(statistic = rownames(t2), t2, row.names = NULL)
  write.csv(t2, file.path(captured, "table2-reproduced.csv"), row.names = FALSE)
  for (obj in c("magle_ksngram_subset", "konge_ksngram_subset", "erte_ksngram_subset")) {
    write.csv(get_g(obj), file.path(captured, paste0(obj, ".csv")), row.names = FALSE)
  }

  # Fig. 3: each panel's bars as plotted (order top to bottom, composition,
  # and the PMI label text the plot draws).
  panels <- c(a = "bigramsBYfrequency", b = "bigramsBYpmi", c = "trigramsBYfrequency",
              d = "trigramsBYpmi", e = "quadrigramsBYfrequency", f = "quadrigramsBYpmi")
  fig3 <- do.call(rbind, lapply(names(panels), function(letter) {
    p <- get_g(panels[[letter]])
    built <- ggplot2::ggplot_build(p)
    labels_bottom_up <- built$layout$panel_params[[1]]$y$get_labels()
    text_layer <- built$data[[2]]
    n <- length(labels_bottom_up)
    do.call(rbind, lapply(seq_len(n), function(pos) {
      sg <- labels_bottom_up[[pos]]
      rows <- p$data[p$data$Skipgram == sg, ]
      comp <- tapply(rows$Frequency, rows$Chronology, sum)
      pick <- function(level) if (level %in% names(comp)) unname(comp[[level]]) else 0
      data.frame(panel = letter, rank = n - pos + 1L, ngram = sg,
                 pmi_label = text_layer$label[round(text_layer$y) == pos][1],
                 pmi_full = sprintf("%.17g", unique(rows$PMI)[1]),
                 total = sum(rows$Frequency),
                 ertebolle = pick("Ertebølle"), kongemose = pick("Kongemose"),
                 kongemose_ertebolle = pick("Kongemose/Ertebølle"),
                 maglemose = pick("Maglemose"), stringsAsFactors = FALSE)
    }))
  }))
  fig3 <- fig3[order(fig3$panel, fig3$rank), ]
  write.csv(fig3, file.path(captured, "fig3-reproduced.csv"), row.names = FALSE)

  # Fig. 2 bar panel: counts per artefact type and chronology, in plot order.
  p2 <- get_g("artefact_type_chronology")
  built2 <- ggplot2::ggplot_build(p2)
  order2 <- rev(built2$layout$panel_params[[1]]$y$get_labels())   # top to bottom
  tab2 <- table(p2$data$Artefact_Type, p2$data$Chronology, useNA = "ifany")
  fig2 <- data.frame(rank = seq_along(order2), category = order2,
                     stringsAsFactors = FALSE)
  for (lvl in colnames(tab2)) {
    fig2[[ifelse(is.na(lvl), "chronology_NA", lvl)]] <- as.integer(tab2[order2, lvl])
  }
  fig2$total <- as.integer(rowSums(tab2[order2, , drop = FALSE]))
  write.csv(fig2, file.path(captured, "fig2-bars-reproduced.csv"), row.names = FALSE)
  # The same panel's built layer data (stat_count output: one row per
  # segment, with its y position, fill colour, and count), with the y labels.
  layer2 <- built2$data[[1]]
  labels2 <- built2$layout$panel_params[[1]]$y$get_labels()
  write.csv(data.frame(y = layer2$y, category = labels2[round(layer2$y)],
                       fill = layer2$fill, count = layer2$count,
                       xmin = layer2$xmin, xmax = layer2$xmax),
            file.path(captured, "fig2-layer-data.csv"), row.names = FALSE)

  # Fig. 4: the matrix m as plotted (rows and columns in the plotted order).
  # Written at 17 significant digits (write.csv's default of 15 rounds the
  # last digit, which would blur a comparison at S3's 15-digit precision).
  m <- get_g("m")
  m_text <- apply(m, 2, function(col) sprintf("%.17g", col))
  rownames(m_text) <- rownames(m)
  write.csv(m_text, file.path(captured, "fig4-matrix-m.csv"))

  # Objects for the verification aids (read-only use, separate process).
  saveRDS(list(corpus = get_g("corpus"), toks = get_g("toks"), k = get_g("k"),
               t = get_g("t"), freqs = get_g("freqs"),
               bigramfreqs = get_g("bigramfreqs"), bigrams_final = get_g("bigrams"),
               fig3b_data = get_g("bigramsBYpmi")$data, data_nrow = nrow(get_g("data"))),
          file.path(captured, "authors-objects.rds"))

  # Environment record.
  writeLines(utils::capture.output(utils::sessionInfo()),
             file.path(captured, "session-info.txt"))
  for (f in c("package-inventory.csv", "pin-attempts.csv")) {
    file.copy(file.path("/opt/llmr", f), file.path(captured, f), overwrite = TRUE)
  }
  writeLines(c(paste("capabilities cairo:", capabilities("cairo")),
               paste("locale:", Sys.getlocale())),
             file.path(captured, "runtime-notes.txt"))
  message("run-analysis.R: finished")
})
