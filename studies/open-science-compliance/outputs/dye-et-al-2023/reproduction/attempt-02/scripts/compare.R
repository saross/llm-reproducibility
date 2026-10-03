#!/usr/bin/env Rscript
## ===========================================================================
## compare.R — value-level comparison of published and reproduced results
##
## NOT THE AUTHORS' CODE. Reads (read-only) the outputs of run-analysis.R
## (outputs/authors/) and verification-aids.R (outputs/aids/), and the
## published values transcribed from the paper and supplement
## (comparisons/published-values.csv, plus the figure readings encoded below
## with their sources). Writes one value-level CSV per locked target to
## comparisons/values/, which comparisons/comparison.json cites as evidence.
##
## Matching rule (plan tolerances, deterministic analyses): a reproduced value
## is EXACT at published precision when R's round(x, 2) — the rounding the
## authors' own code applies — equals the published value; it is
## WITHIN_PRECISION when |x - published| <= 0.005 (inside the rounding interval
## of a 2-dp figure) without satisfying the former.
##
## Usage (inside Docker, after run-analysis.R and verification-aids.R):
##   Rscript scripts/compare.R
## ===========================================================================

suppressPackageStartupMessages(library(ArchaeoPhases))
vdir <- "comparisons/values"
dir.create(vdir, showWarnings = FALSE, recursive = TRUE)
eps <- 1e-9

mat <- function(s) {
  f <- sprintf("outputs/authors/section-%s-observed.rds", s)
  if (file.exists(f)) readRDS(f) else NULL
}
split_bar <- function(x) strsplit(x, "|", fixed = TRUE)[[1]]
classify <- function(x, pub) {
  ifelse(is.na(x), "NOT_COMPUTED",
         ifelse(abs(round(x, 2) - pub) < eps, "EXACT",
                ifelse(abs(x - pub) <= 0.005 + eps, "WITHIN_PRECISION", "DIFFERENT")))
}
write_target <- function(df, tid, stem) {
  write.csv(df, file.path(vdir, sprintf("%s-%s.csv", tid, stem)), row.names = FALSE)
}

## ---- Matrix-derived values: T05, T06, T12-T20, T24-T32 --------------------
pv <- read.csv("comparisons/published-values.csv", stringsAsFactors = FALSE,
               check.names = FALSE)
pv$reproduced_unrounded <- NA_real_
for (i in seq_len(nrow(pv))) {
  m <- mat(pv$section[i]); if (is.null(m)) next
  rows <- split_bar(pv$row[i]); cols <- split_bar(pv$col[i])
  vals <- as.vector(m[rows, cols, drop = FALSE])
  pv$reproduced_unrounded[i] <- switch(pv$kind[i],
    cell = vals[1], min = min(vals), max = max(vals),
    npos = sum(vals > 0))
}
pv$reproduced_round2 <- round(pv$reproduced_unrounded, 2)
pv$abs_difference <- abs(pv$reproduced_unrounded - pv$published)
pv$match <- ifelse(pv$kind == "npos",
                   ifelse(pv$reproduced_unrounded == pv$published, "EXACT", "DIFFERENT"),
                   classify(pv$reproduced_unrounded, pv$published))
stems <- c(T05 = "amber-branching", T06 = "cowrie-disc", T12 = "supp-table-2",
           T13 = "supp-table-3", T14 = "supp-table-4", T15 = "supp-table-5",
           T16 = "supp-table-6", T17 = "supp-table-7", T18 = "supp-table-8",
           T19 = "supp-table-9", T20 = "supp-table-10", T24 = "supp-10-1-text",
           T25 = "supp-10-2-text", T26 = "supp-10-3-text", T27 = "supp-10-4-text",
           T28 = "supp-10-5-text", T29 = "supp-10-6-text", T30 = "supp-10-7-text",
           T31 = "supp-10-8-text", T32 = "supp-10-9-text")
for (tid in names(stems)) write_target(pv[pv$target_id == tid, ], tid, stems[[tid]])

## T06 supplementary evidence for the PAPER_ERROR check: the whole section 7
## matrix, so the location of the published 0.87 can be seen.
m7 <- mat("07")
if (!is.null(m7)) {
  long7 <- as.data.frame(as.table(m7), stringsAsFactors = FALSE)
  names(long7) <- c("ancestor_row", "descendant_col", "p_oFD_unrounded")
  long7$p_oFD_round2 <- round(long7$p_oFD_unrounded, 2)
  long7$equals_published_0_87 <- abs(long7$p_oFD_round2 - 0.87) < eps
  write_target(long7[!is.na(long7$p_oFD_unrounded), ], "T06", "section-07-full-matrix")
}

## ---- T07: BE1-CylRound the most probable early ancestor (section 8, oFD) --
m8 <- mat("08")
if (!is.null(m8)) {
  anc <- c("BE1-CylRound", "BE1-CylPen", "BE1-Melon", "BE1-SegGlob")
  t07 <- do.call(rbind, lapply(c("BE1-Orange", "BE1-WoundSp", "BE1-Dghnt"), function(late) {
    p <- m8[anc, late]
    data.frame(late_type = late, `p_CylRound` = p[1], `p_CylPen` = p[2],
               `p_Melon` = p[3], `p_SegGlob` = p[4],
               published_argmax = "BE1-CylRound", reproduced_argmax = anc[which.max(p)],
               unique_max = sum(p == max(p)) == 1,
               match = ifelse(anc[which.max(p)] == "BE1-CylRound" && sum(p == max(p)) == 1,
                              "EXACT", "DIFFERENT"), check.names = FALSE)
  }))
  write_target(t07, "T07", "cylround-ancestor")
}

## ---- T08: BE3-Amber the most probable stable-solid ancestor of BE1-Dghnt --
m9 <- mat("09")
if (!is.null(m9)) {
  anc <- c("BE3-Amber", "BE1-Amethyst", "BE1-Cowrie", "BE1-Disc")
  p <- m9[anc, "BE1-Dghnt"]
  t08 <- data.frame(ancestor = anc, p_oFDm_to_Dghnt = p,
                    published_argmax = "BE3-Amber", reproduced_argmax = anc[which.max(p)],
                    match = ifelse(anc[which.max(p)] == "BE3-Amber" && sum(p == max(p)) == 1,
                                   "EXACT", "DIFFERENT"))
  write_target(t08, "T08", "amber-dghnt-reticulation")
}

## ---- T09: summary of the 54 relations -------------------------------------
rels <- read.csv("outputs/aids/T22-54-relations.csv", stringsAsFactors = FALSE)
pub54 <- pv[pv$kind == "cell" & pv$target_id %in% sprintf("T%02d", 12:20), ]
gt9 <- function(earlier, later, p) sum(p > 0.9 & later == "BE1-Disc")
t09 <- data.frame(
  quantity = c("number of relations", "median probability",
               "relations with probability <= 0.10 (2 dp)",
               "relations with probability > 0.9", "of which involve BE1-Disc",
               "statement (a) 'variable, but typically quite low'",
               "statement (b) 'most constraints with probability > 0.9 involve BE1-Disc'"),
  published_tables = c(nrow(pub54), median(pub54$published), sum(pub54$published <= 0.1),
                       sum(pub54$published > 0.9),
                       sum(pub54$published > 0.9 & grepl("BE1-Disc$", pub54$item)),
                       NA, NA),
  reproduced = c(nrow(rels), median(round(rels$probability, 2)),
                 sum(round(rels$probability, 2) <= 0.1), sum(rels$probability > 0.9),
                 gt9(rels$earlier, rels$later, rels$probability), NA, NA),
  stringsAsFactors = FALSE)
t09$match <- ifelse(is.na(t09$published_tables), NA,
                    ifelse(abs(as.numeric(t09$published_tables) - as.numeric(t09$reproduced)) < eps,
                           "EXACT", "DIFFERENT"))
t09$match[6] <- if (median(rels$probability) < 0.5 &&
                    sum(round(rels$probability, 2) <= 0.1) == sum(pub54$published <= 0.1))
  "EXACT (holds identically: the reproduced 54 values equal the published tables)" else "CHECK"
t09$match[7] <- if (gt9(rels$earlier, rels$later, rels$probability) == sum(rels$probability > 0.9))
  "EXACT (all reproduced relations above 0.9 involve BE1-Disc)" else "CHECK"
write_target(t09, "T09", "54-relations-summary")

## ---- T22: Supplement Figure 2 bin counts ----------------------------------
bins <- read.csv("outputs/aids/T22-histogram-bins.csv", stringsAsFactors = FALSE,
                 check.names = FALSE)
bins$published_bar_height <- c(20, 4, 2, 3, 3, 4, 4, 1, 1, 12)  # read from Supp Fig 2
bins$match_planned_method <- ifelse(bins$unrounded_right_closed == bins$published_bar_height,
                                    "EXACT", "DIFFERENT")
bins$match_round2_right_closed <- ifelse(bins$round2_right_closed == bins$published_bar_height,
                                         "EXACT", "DIFFERENT")
write_target(bins, "T22", "supp-fig-2-bins")

## ---- Lattice memberships: T01, T21, T23, T33, T34 -------------------------
codes <- c("p", "m", "o", "F", "s", "D", "e", "d", "S", "f", "O", "M", "P")
member <- function(set) as.integer(codes %in% strsplit(set, "")[[1]])
## Published relation sets read from the opaque labels of each lattice (paper
## Fig 2 p.8; Supp Figs 1 and 3 pp.48-49) and stated in the text (paper
## section 3; Supp sections 11-12).
fig2_pub <- c("left-top" = "oFDdfO", "left-middle" = "mM", "left-bottom" = "moFDdfOM",
              "right-top" = "pmoFsDedSfOMP", "right-middle" = "p",
              "right-bottom" = "oFsDedSfO")
f2 <- read.csv("outputs/aids/T01-fig2-lattices.csv", stringsAsFactors = FALSE)
f2$published_member <- unlist(lapply(fig2_pub[unique(f2$panel)], member))[
  match(paste(f2$panel, f2$code), paste(rep(unique(f2$panel), each = 13), codes))]
f2$reproduced_member <- as.integer(f2$value > 0)
f2$match <- ifelse(f2$published_member == f2$reproduced_member, "EXACT", "DIFFERENT")
write_target(f2, "T01", "fig-2-memberships")

s1 <- read.csv("outputs/aids/T21-T33-suppfig1-lattices.csv", stringsAsFactors = FALSE)
s1$published_member <- c(member("pmoFsDedSfOMP"), member("e"))
s1$reproduced_member <- as.integer(s1$value > 0)
s1$match <- ifelse(s1$published_member == s1$reproduced_member, "EXACT", "DIFFERENT")
write_target(s1, "T21", "supp-fig-1-memberships")
t33 <- data.frame(item = "posterior probability BE1-Dghnt(e)BE1-Dghnt", published = 1,
                  reproduced_unrounded = s1$value[s1$panel == "bottom" & s1$code == "e"])
t33$match <- classify(t33$reproduced_unrounded, t33$published)
write_target(t33, "T33", "dghnt-identity")

s3 <- read.csv("outputs/aids/T23-T34-suppfig3-lattices.csv", stringsAsFactors = FALSE)
s3$published_member <- c(member("p"), member("poDd"))
s3$reproduced_member <- as.integer(s3$value > 0)
s3$match <- ifelse(s3$published_member == s3$reproduced_member, "EXACT", "DIFFERENT")
write_target(s3, "T23", "supp-fig-3-memberships")
right <- s3[s3$panel == "right", ]
o <- right$value[right$code == "o"]
t34 <- data.frame(
  item = c("observed relation set BE1-Koch20Wh(?)BE1-WhSpiral", "P(overlaps)"),
  published = c("poDd", "0.73"),
  reproduced = c(paste(right$code[right$value > 0], collapse = ""), format(o, digits = 15)),
  reproduced_round2_R = c(NA, round(o, 2)),
  reproduced_round2_half_up = c(NA, floor(o * 100 + 0.5) / 100),
  stringsAsFactors = FALSE)
t34$match <- c(ifelse(t34$reproduced[1] == "poDd", "EXACT", "DIFFERENT"),
               classify(o, 0.73))
write_target(t34, "T34", "koch20wh-whspiral")

## ---- T03: tempo plot shape summary (supports the visual comparison) -------
tempo <- unclass(readRDS("outputs/authors/section-06-tempo-plot-object.rds"))
first_year <- function(d, q) d$year[which(d$count >= q)[1]]
t03 <- do.call(rbind, lapply(names(tempo), function(n) {
  d <- tempo[[n]]; k <- max(d$count)
  data.frame(bead_type = n, panel_label = d$name[1], n_dates = round(k),
             first_event_year = round(first_year(d, 0.5)),
             median_event_year = round(first_year(d, k / 2)),
             last_event_year = round(first_year(d, k - 0.5)))
}))
late <- c("BE1.Cowrie", "BE1.Disc", "BE1.Amethyst", "BE1.Dghnt", "BE1.Orange", "BE1.WoundSp")
early <- c("BE1.Dot34", "BE1.DotReg", "BE1.Koch20Wh", "BE1.Koch20Ye", "BE1.Koch34Bl",
           "BE1.Koch34Wh", "BE1.Koch34Ye", "BE1.Koch49.50", "BE1.Melon", "BE1.Reticella",
           "BE3.Amber", "BE1.CylPen", "BE1.CylRound", "BE2.c.Metal")
t03$text_shape_class <- ifelse(t03$bead_type %in% late, "late (paper p.12-14)",
                               ifelse(t03$bead_type %in% early, "early (paper p.12)",
                                      "not classified in text"))
t03$published_panel_present <- TRUE   # all 23 panel titles appear in paper Fig 4
write_target(t03, "T03", "tempo-shape-summary")

## ---- T04: paper Figure 6 links and placements -----------------------------
links <- data.frame(
  from = c("BE1-CylRound", "BE1-CylRound", "BE1-CylRound", "BE1-CylRound",
           "BE3-Amber", "BE3-Amber", "BE3-Amber", "BE1-Cowrie"),
  to = c("BE1-Orange", "BE1-SegGlob", "BE1-WoundSp", "BE1-Dghnt",
         "BE1-Dghnt", "BE1-Cowrie", "BE1-Amethyst", "BE1-Disc"),
  mode_depicted = c(rep("branching", 4), "reticulation", "branching", "branching", "branching"),
  relation = c(rep("oFD", 4), "oFDm", "oFD", "oFD", "oFD"),
  section = c(rep("08", 4), "09", "07", "07", "07"), stringsAsFactors = FALSE)
links$reproduced_probability <- mapply(function(f, t, s) mat(s)[f, t],
                                       links$from, links$to, links$section)
links$supported <- links$reproduced_probability >= 0.5
write_target(links, "T04", "fig-6-links")
## Fig 6 box positions: bottom edge of each illustration box's scale bar,
## located programmatically on a 400 dpi render of paper p.20 (gridlines
## 800..400 at pixel rows 733, 1050, 1368, 1685, 2002); box centres are about
## 20-25 years above the bar. BE1-Melon lower box and BE3-Amber symbols were
## read visually. See log.md.
fig6 <- data.frame(
  bead_type = c("BE1.Melon", "BE1.CylPen", "BE1.Orange", "BE1.SegGlob", "BE1.WoundSp",
                "BE1.CylRound", "BE1.Dghnt", "BE1.Cowrie", "BE1.Disc", "BE1.Amethyst",
                "BE3.Amber"),
  fig6_lower_box_bar_year = c(433, 433, 498, 527, 579, 435, 573, 560, 690, 565, NA),
  fig6_upper_box_bar_year = c(573, 607, 672, 630, 709, 627, 706, 692, 720, 680, NA),
  stringsAsFactors = FALSE)
fig6$fig6_lower_box_centre_approx <- fig6$fig6_lower_box_bar_year + 22
fig6$fig6_upper_box_centre_approx <- fig6$fig6_upper_box_bar_year + 22
fig6$fig6_lower_box_centre_approx[fig6$bead_type == "BE3.Amber"] <- 430  # 'A' symbol
fig6$fig6_upper_box_centre_approx[fig6$bead_type == "BE3.Amber"] <- 703  # 'A' symbol
fig6 <- merge(fig6, t03[, c("bead_type", "first_event_year", "median_event_year",
                            "last_event_year")], by = "bead_type")
fig6$diff_lower_vs_first <- fig6$fig6_lower_box_centre_approx - fig6$first_event_year
fig6$diff_upper_vs_last <- fig6$fig6_upper_box_centre_approx - fig6$last_event_year
write_target(fig6, "T04", "fig-6-placements")

## ---- Untestable targets: T02, T10, T11 ------------------------------------
st <- read.csv("outputs/logs/section-status.csv", stringsAsFactors = FALSE)
write_target(st[st$section == "section-04-occurrence-plot.R", ], "T02", "section-04-status")
write_target(st[st$section == "section-03-replicability.R", ], "T10", "section-03-status")
write_target(st[st$section == "section-03-replicability.R", ], "T11", "section-03-status")

## ---- Console summary --------------------------------------------------------
cat("\nMatrix-derived values by target:\n")
print(table(pv$target_id, pv$match))
cat("compare.R finished\n")
