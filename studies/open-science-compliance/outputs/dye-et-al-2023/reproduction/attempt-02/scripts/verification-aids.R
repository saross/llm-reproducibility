#!/usr/bin/env Rscript
## ===========================================================================
## verification-aids.R — VERIFICATION AIDS (registrant ruling R1)
##
## NOT THE AUTHORS' CODE. These aids test published results for which the
## authors supplied no code (paper Figure 2; Supplement Figures 1-3; the
## Supplement section 11/12 named values). Under ruling R1 an aid may only
##   (a) make read-only lookups in the deposited data (beads-1.csv) and in
##       objects the authors' code already produced (outputs/authors/), and
##   (b) call documented, exported functions of the package the authors used
##       (ArchaeoPhases 1.8: allen_illustrate, allen_observe), passing only
##       display arguments (file name, plot title) through the documented
##       `...` to allen_plot().
## They make no new statistical choices. Display-only conventions that the
## paper does not publish (plot titles, histogram bin edges) are recorded as
## such in the comparison report.
##
## Targets served: T01 (paper Fig 2), T21 + T33 (Supp Fig 1, section 11),
## T22 (Supp Fig 2), T23 + T34 (Supp Fig 3, section 12).
##
## Usage (inside Docker, after run-analysis.R): Rscript scripts/verification-aids.R
## Outputs: outputs/aids/
## ===========================================================================

suppressPackageStartupMessages({
  library(ArchaeoPhases)
  library(ggplot2)
})
options(device = function(...) grDevices::pdf(file = NULL))
out <- "outputs/aids"
dir.create(out, showWarnings = FALSE, recursive = TRUE)

relation_codes <- c("p", "m", "o", "F", "s", "D", "e", "d", "S", "f", "O", "M", "P")

#' Tidy an allen_set data frame into code / relation / value columns.
#'
#' @param df Data frame returned by allen_illustrate() or allen_observe()$x-like.
#' @param label Panel label to record.
#' @return A data frame with one row per basic relation.
tidy_set <- function(df, label) {
  data.frame(panel = label, code = relation_codes, relation = as.character(df$node),
             value = as.numeric(df$result), title = as.character(df$title),
             stringsAsFactors = FALSE)
}

## ---- T01: paper Figure 2, six analytic Nokel lattices --------------------
## Documented allen_illustrate() options for the three modes of change
## (left column: ancestor-descendant relation and its converse) and their
## compositions (right column).
fig2_options <- c(branching = "left-top", transformation = "left-middle",
                  reticulation = "left-bottom", branch = "right-top",
                  transform = "right-middle", reticulate = "right-bottom")
fig2 <- do.call(rbind, lapply(names(fig2_options), function(opt) {
  df <- allen_illustrate(opt, file_name = file.path(out, sprintf("T01-fig2-%s.pdf", opt)))
  cbind(option = opt, tidy_set(df, fig2_options[[opt]]))
}))
write.csv(fig2, file.path(out, "T01-fig2-lattices.csv"), row.names = FALSE)

## ---- Inputs for the empirical aids: authors' data and bead_list ----------
ox <- read_oxcal("data/beads-1.csv", quiet = "yes")
bl <- readRDS("outputs/authors/section-05-bead-list.rds")$bead_list

## ---- T21 + T33: Supplement Figure 1 --------------------------------------
## Top: analytic lattice of the 13 basic relations (published with no title).
top <- allen_illustrate("basic", plot_title = "",
                        file_name = file.path(out, "T21-suppfig1-top-basic.pdf"))
## Bottom: empirical lattice BE1-Dghnt(e)BE1-Dghnt.
dghnt <- allen_observe(data = ox,
                       chains = list(list("BE1-Dghnt" = bl$BE1.Dghnt,
                                          "BE1-Dghnt" = bl$BE1.Dghnt)),
                       file_name = file.path(out, "T21-suppfig1-bottom-dghnt.pdf"))
suppfig1 <- rbind(tidy_set(top, "top"), tidy_set(as.data.frame(unclass(dghnt)), "bottom"))
write.csv(suppfig1, file.path(out, "T21-T33-suppfig1-lattices.csv"), row.names = FALSE)

## ---- T23 + T34: Supplement Figure 3 --------------------------------------
## Right: empirical relation BE1-Koch20Wh vs BE1-WhSpiral from the MCMC output.
koch <- allen_observe(data = ox,
                      chains = list(list("BE1-Koch20Wh" = bl$BE1.Koch20Wh,
                                         "BE1-WhSpiral" = bl$BE1.WhSpiral)),
                      file_name = file.path(out, "T23-suppfig3-right-observed.pdf"))
## Left: the expected relation (p) posited by the occurrence seriation. The
## documented option 'transform' (composition m.m) renders exactly the set {p};
## the published panel title is passed as a display argument only.
left <- allen_illustrate("transform", plot_title = "BE1-Koch20Wh(p)BE1-WhSpiral",
                         file_name = file.path(out, "T23-suppfig3-left-expected.pdf"))
suppfig3 <- rbind(tidy_set(left, "left"), tidy_set(as.data.frame(unclass(koch)), "right"))
write.csv(suppfig3, file.path(out, "T23-T34-suppfig3-lattices.csv"), row.names = FALSE)

## ---- T22: Supplement Figure 2, histogram of the 54 relations -------------
## Read-only lookup of the 54 Earlier(p)Later cells of Supplement Tables 2-10
## in the matrices the authors' section 10 code produced.
cells <- list(
  "10-1" = list(rows = c("BE1-Reticella", "BE1-Melon"),
                cols = c("BE1-Disc", "BE1-WhSpiral", "BE1-WoundSp", "BE1-Dghnt",
                         "BE1-Amethyst", "BE1-Cowrie", "BE1-Orange", "BE2-c Metal")),
  "10-2" = list(rows = "BE1-DotReg",
                cols = c("BE1-Disc", "BE1-WhSpiral", "BE1-WoundSp", "BE1-Dghnt",
                         "BE1-Amethyst", "BE1-Cowrie", "BE1-Orange")),
  "10-3" = list(rows = "BE1-Koch20Ye",
                cols = c("BE1-Disc", "BE1-WhSpiral", "BE1-WoundSp", "BE1-Dghnt",
                         "BE1-Amethyst")),
  "10-4" = list(rows = c("BE1-CylPen", "BE1-Koch20Wh", "BE1-Koch49/50"),
                cols = c("BE1-Disc", "BE1-WhSpiral", "BE1-WoundSp", "BE1-Dghnt")),
  "10-5" = list(rows = c("BE1-Koch34Wh", "BE1-Koch34Ye"),
                cols = c("BE1-Disc", "BE1-WhSpiral", "BE1-Dghnt")),
  "10-6" = list(rows = "BE1-Dot34", cols = c("BE1-Disc", "BE1-Dghnt")),
  "10-7" = list(rows = "BE1-CylRound", cols = "BE1-Disc"),
  "10-8" = list(rows = "BE1-SegGlob", cols = "BE1-Disc"),
  "10-9" = list(rows = c("BE1-Orange", "BE1-WhSpiral", "BE2-c Metal", "BE1-Koch34Bl"),
                cols = "BE1-Disc"))
rels <- do.call(rbind, lapply(names(cells), function(s) {
  m <- readRDS(sprintf("outputs/authors/section-%s-observed.rds", s))
  g <- expand.grid(earlier = cells[[s]]$rows, later = cells[[s]]$cols,
                   stringsAsFactors = FALSE)
  g$section <- s
  g$probability <- mapply(function(r, c) m[r, c], g$earlier, g$later)
  g
}))
write.csv(rels, file.path(out, "T22-54-relations.csv"), row.names = FALSE)

## Bin counts over [0, 1] in 0.1-wide bins (the published figure's bar edges),
## under both closure conventions, from unrounded and from 2-dp values.
breaks <- seq(0, 1, by = 0.1)
count_bins <- function(x, right) as.integer(table(cut(x, breaks, right = right,
                                                       include.lowest = TRUE)))
bins <- data.frame(
  bin = levels(cut(0.5, breaks, include.lowest = TRUE)),
  unrounded_right_closed = count_bins(rels$probability, TRUE),
  unrounded_left_closed = count_bins(rels$probability, FALSE),
  round2_right_closed = count_bins(round(rels$probability, 2), TRUE),
  round2_left_closed = count_bins(round(rels$probability, 2), FALSE))
write.csv(bins, file.path(out, "T22-histogram-bins.csv"), row.names = FALSE)

## ggplot2 geom_histogram with the published bar edges (binwidth 0.1 from 0;
## ggplot2's default closure, right-closed).
p <- ggplot(rels, aes(x = probability)) +
  geom_histogram(binwidth = 0.1, boundary = 0, colour = "white") +
  scale_x_continuous(breaks = seq(0.1, 0.9, 0.1)) +
  labs(x = "Observed relation probability", y = "Count") + theme_bw()
ggsave(file.path(out, "T22-suppfig2-histogram.pdf"), p, width = 6, height = 3.5)
write.csv(layer_data(p)[, c("xmin", "xmax", "count")],
          file.path(out, "T22-ggplot-layer-counts.csv"), row.names = FALSE)

cat("verification-aids.R finished\n")
