# =============================================================================
# t11-all-bigrams.R — herskind-riede-2024 T11 completion: expected Fig. 4 boxes
# =============================================================================
#
# PURPOSE
#   Operator deviation (Shawn's ruling, 2026-10-04, shakedown human queue
#   item 4): complete the T11 check that the executor's approved aid left
#   partial. The executor applied the authors' createResultTable() only to
#   bigrams with observed frequency > 2. The Fig. 4 caption ("Motif
#   combinations limited to one specific culture complex are marked with a
#   small, coloured box") covers every displayed pair, so this script applies
#   the same function, read-only and verbatim, to ALL bigrams whose two motifs
#   are among the 49 Fig. 4 axis motifs.
#
#   No new statistical choice is made: the function and the chrongrams
#   definition are parsed verbatim from the authors' S2.R, exactly as the
#   executor's compare.R does (lines 272-283 of attempt-02/comparisons/compare.R).
#
# USAGE (attempt-02 mounted read-only at /attempt; this directory at /out)
#   docker run --rm \
#     --mount type=bind,src=<attempt-02>,dst=/attempt,readonly \
#     --mount type=bind,src=<this-dir>,dst=/out \
#     -w /attempt llmr-herskind-riede-2024-attempt-02 \
#     Rscript /out/t11-all-bigrams.R
#
# OUTPUT
#   /out/t11-expected-boxes-all-bigrams.csv — one row per bigram within the
#   Fig. 4 axis: observed frequency, culture levels, expected box colour
#   (NA = no box), and the displayed cell (row = later axis motif, column =
#   earlier axis motif, matching the published upper-left triangle).
# =============================================================================

suppressPackageStartupMessages({
  library(readxl)
  library(dplyr)
})

# ---- Inputs (read-only) -----------------------------------------------------
s1 <- suppressMessages(read_excel("/attempt/data/Herskind&Riede_S1.xlsx"))
bg <- utils::read.csv("/attempt/outputs/capture-part6-bigrams-full.csv",
                      colClasses = "character", fileEncoding = "UTF-8",
                      check.names = FALSE)

# ---- The authors' definitions, parsed verbatim from S2.R ---------------------
s2_exprs <- parse("/attempt/data/Herskind&Riede_S2.R", encoding = "UTF-8")

#' Return the top-level assignment expression `name <- ...` from S2.R.
#'
#' @param name Object name assigned in S2.R.
#' @return The unevaluated assignment expression.
pick <- function(name) {
  for (e in s2_exprs) {
    if (is.call(e) && identical(e[[1]], as.name("<-")) &&
        identical(e[[2]], as.name(name))) return(e)
  }
  stop("expression not found: ", name)
}

data <- s1                        # the authors' object name
eval(pick("chrongrams"))          # chrongrams <- data[,c(11,31:289)]
eval(pick("createResultTable"))   # the authors' function, verbatim

# ---- Fig. 4 axis (the authors' manual order, S2.R Part 7) -------------------
axis_order <- toupper(c("a14","b3","a24","b10","b2","b12","e4","a5","d5","b13","b4",
                        "b1","a1","a3","ant","f12","e1","b6","e5","f5","f13","f38",
                        "d29","b8","d33","h1","g2","c1","f14","i1","f35","zoo","d19",
                        "g1","d3","d15","f15","c12","c14","c5","c13","c4","c6","d7",
                        "f55","g7","i13","i5","relief"))

# Every bigram whose two motifs both appear on the Fig. 4 axis, at any
# observed frequency (the executor's aid stopped at observed > 2).
in_axis <- vapply(strsplit(bg$ksngrams, " "),
                  function(tk) all(tk %in% axis_order), logical(1))
sub <- bg[in_axis, ]

# The authors' function counts objects bearing both motifs, per chronology.
tab <- createResultTable(sub)
cat("Chronology levels seen:", paste(sort(unique(tab$Chronology)), collapse = " | "), "\n")

excl <- tab %>%
  filter(Frequency > 0) %>%
  group_by(Skipgram) %>%
  summarise(levels = paste(sort(unique(Chronology)), collapse = " + "),
            n_levels = n_distinct(Chronology), .groups = "drop")

colour_of <- c(Maglemose = "purple", Kongemose = "red", `Ertebølle` = "yellow")
excl$expected_box <- ifelse(excl$n_levels == 1, unname(colour_of[excl$levels]), NA)
excl$observed_freq <- as.integer(sub$observed_freq[match(excl$Skipgram, sub$ksngrams)])

# Displayed cell: the published triangle puts the later axis motif on the row
# and the earlier one on the column (as in the executor's aid).
pos <- t(vapply(strsplit(excl$Skipgram, " "), function(tk) {
  o <- match(tk, axis_order); c(axis_order[max(o)], axis_order[min(o)])
}, character(2)))
excl$row <- pos[, 1]
excl$col <- pos[, 2]

utils::write.csv(excl[order(excl$row, excl$col), ],
                 "/out/t11-expected-boxes-all-bigrams.csv",
                 row.names = FALSE, fileEncoding = "UTF-8")
cat("Bigrams within axis:", nrow(sub), "| with a result row:", nrow(excl),
    "| single-culture:", sum(!is.na(excl$expected_box)), "\n")
print(table(excl$expected_box, useNA = "ifany"))
print(table(single = excl$n_levels == 1, freq_le2 = excl$observed_freq <= 2))
