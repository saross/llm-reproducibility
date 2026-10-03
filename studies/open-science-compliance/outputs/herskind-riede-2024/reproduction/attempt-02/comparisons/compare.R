# =============================================================================
# compare.R — VERIFICATION AIDS AND COMPARISON (not the authors' code)
# =============================================================================
# Herskind & Riede (2024) reproduction, attempt 02.
#
# PURPOSE
#   Compare the reproduced outputs (outputs/, produced by run-analysis.R from
#   the authors' unmodified S2.R) with the published values transcribed in
#   comparisons/published-values/, one result file per target.
#
# REGISTRANT RULING R1 — verification aids
#   This script is kept separate from the authors' code. Its aids are:
#     (a) read-only lookups in the deposited data (S1.xlsx, S3.xlsx);
#     (b) calls to documented functions of packages the authors used
#         (readxl::read_excel, ggplot2 point plots);
#     (c) the authors' own createResultTable() and chrongrams definitions,
#         parsed verbatim from S2.R and applied read-only to the bigrams with
#         observed frequency > 2 (approved aid for the Fig. 4 boxes).
#   No aid makes a new statistical choice.
#
# USAGE (inside the container, attempt directory mounted at /attempt)
#   docker run --rm --mount type=bind,src=<attempt-dir>,dst=/attempt \
#       llmr-herskind-riede-2024-attempt-02 Rscript comparisons/compare.R
#
# OUTPUTS
#   comparisons/results/t01..t15-*.csv  value-level comparison tables
#   comparisons/results/summary.csv     per-target counts
#   comparisons/aids/*.png              aid figures (Fig. 2 map, Fig. 4 boxes,
#                                       Fig. 5 positions)
# =============================================================================

suppressPackageStartupMessages({
  library(readxl)
  library(dplyr)
  library(ggplot2)
})

root <- normalizePath(".")
pub_dir <- file.path(root, "comparisons", "published-values")
res_dir <- file.path(root, "comparisons", "results")
aid_dir <- file.path(root, "comparisons", "aids")
out_dir <- file.path(root, "outputs")
dir.create(res_dir, showWarnings = FALSE, recursive = TRUE)
dir.create(aid_dir, showWarnings = FALSE, recursive = TRUE)

#' Read a CSV as character columns (UTF-8).
#'
#' @param path File path.
#' @return A data frame with character columns.
read_chr <- function(path) {
  utils::read.csv(path, colClasses = "character", fileEncoding = "UTF-8",
                  check.names = FALSE)
}

#' Write a result table under comparisons/results/.
#'
#' @param x Data frame.
#' @param name File stem.
#' @return Invisibly, the path.
write_result <- function(x, name) {
  path <- file.path(res_dir, paste0(name, ".csv"))
  utils::write.csv(x, path, row.names = FALSE, fileEncoding = "UTF-8")
  invisible(path)
}

summary_rows <- list()

#' Record per-target counts for the summary file.
#'
#' @param target Target id.
#' @param compared Values compared.
#' @param matched Values matched.
#' @param max_abs Maximum absolute difference (or NA).
#' @param note Free-text note.
record <- function(target, compared, matched, max_abs = NA_real_, note = "") {
  summary_rows[[length(summary_rows) + 1]] <<- data.frame(
    target_id = target, values_compared = compared, values_matched = matched,
    max_abs_difference = max_abs, note = note)
  cat(sprintf("%s: %d/%d matched %s\n", target, matched, compared, note))
}

s1 <- suppressMessages(read_excel(file.path(root, "data", "Herskind&Riede_S1.xlsx")))
cluster <- c("C4", "C5", "C12", "C13", "D7")

# ---- T01: corpus size (aid: read-only S1 lookup) -----------------------------
console <- readLines(file.path(out_dir, "run-console.log"), encoding = "UTF-8")
ndoc_line <- grep("^\\[wrapper\\] corpus documents", console, value = TRUE)
ndoc <- as.integer(sub(".*corpus documents = ([0-9]+).*", "\\1", ndoc_line))
t01 <- data.frame(
  item = c("S1 Data rows (non-empty No.)", "S2.R Part 3 corpus documents"),
  published = c(483L, 483L),
  reproduced = c(sum(!is.na(s1$`No.`)), ndoc))
t01$match <- t01$published == t01$reproduced
write_result(t01, "t01-corpus-size")
record("T01", 1L, as.integer(all(t01$match)),
       note = "published 483 compared with S1 rows and S2.R corpus; t = 482 in code")

# ---- T03: maximum motifs on one object (aid: read-only S1 lookup) ------------
t03 <- data.frame(
  item = c("max of S1 Total column", "max row sum of S1 columns 31:289"),
  published = c(15, 15),
  reproduced = c(max(s1$Total), max(rowSums(s1[, 31:289]))))
t03$match <- t03$published == t03$reproduced
write_result(t03, "t03-max-motifs")
record("T03", 1L, as.integer(all(t03$match)))

# ---- T04: Table 1 -------------------------------------------------------------
pub1 <- read_chr(file.path(pub_dir, "table1.csv"))
files1 <- c(unigrams = "unigram", bigrams = "bigram", trigrams = "trigram",
            quadrigrams = "quadrigram")
rep1 <- do.call(rbind, lapply(names(files1), function(col) {
  x <- read_chr(file.path(out_dir, paste0("capture-table1-", files1[[col]],
                                          "-frequencies.csv")))
  data.frame(column = col, frequency = x$level, n_reproduced = x$count)
}))
t04 <- merge(pub1, rep1, by = c("column", "frequency"), all = TRUE)
t04$level_in_both <- !is.na(t04$n) & !is.na(t04$n_reproduced)
t04$n_match <- t04$level_in_both & t04$n == t04$n_reproduced
t04$n_difference <- as.integer(t04$n_reproduced) - as.integer(t04$n)
t04 <- t04[order(match(t04$column, names(files1)), -as.numeric(t04$frequency)), ]
# S3 cross-check (authors' deposited Part 8 output) for levels >= 3.
s3_obs <- function(sheet) {
  x <- suppressMessages(read_excel(file.path(root, "data", "Herskind&Riede_S3.xlsx"),
                                   sheet = sheet, skip = 2, col_names = FALSE,
                                   col_types = "text"))
  table(as.integer(x[[ncol(x) - 2]]))
}
s3_tabs <- list(bigrams = s3_obs("bigrams"), trigrams = s3_obs("trigrams"),
                quadrigrams = s3_obs("quadrigrams"))
t04$n_in_s3_deposit <- mapply(function(col, f) {
  tab <- s3_tabs[[col]]
  if (is.null(tab) || as.integer(f) < 3) return(NA_integer_)
  v <- tab[as.character(f)]
  if (is.na(v)) 0L else as.integer(v)
}, t04$column, t04$frequency)
write_result(t04, "t04-table1")
pub_tot <- read_chr(file.path(pub_dir, "table1-totals.csv"))
rep_tot <- read_chr(file.path(out_dir, "capture-table1-totals.csv"))
names(rep_tot) <- c("column", "total_reproduced")
t04_tot <- merge(pub_tot, rep_tot, by = "column")
t04_tot$match <- t04_tot$total == t04_tot$total_reproduced
write_result(t04_tot, "t04-table1-totals")
# PAPER_ERROR verification (read-only arithmetic on S1): with k = 13 and at
# most 15 motifs per object, every pair/triple of motifs on an object is a
# skipgram, so sum(frequency x n) in a Table 1 column must equal the sum over
# objects of choose(m, 2) or choose(m, 3), m = the S1 Total column.
occ <- function(df, col, nmcol) {
  x <- df[df$column == col, ]
  sum(as.numeric(x$frequency) * as.numeric(x[[nmcol]]), na.rm = TRUE)
}
t04_occ <- data.frame(
  column = c("bigrams", "trigrams"),
  from_s1_total_column = c(sum(choose(s1$Total, 2)), sum(choose(s1$Total, 3))),
  implied_by_published_table1 = c(occ(t04, "bigrams", "n"), occ(t04, "trigrams", "n")),
  implied_by_reproduction = c(occ(t04, "bigrams", "n_reproduced"),
                              occ(t04, "trigrams", "n_reproduced")))
write_result(t04_occ, "t04-occurrence-check")
print(t04_occ)
n_pairs <- nrow(pub1)
matched_levels <- sum(t04$level_in_both)
matched_n <- sum(t04$n_match)
record("T04", 2L * n_pairs + nrow(pub_tot),
       matched_levels + matched_n + sum(t04_tot$match),
       max_abs = max(abs(t04$n_difference), na.rm = TRUE),
       note = sprintf("%d frequency levels, %d n cells, %d totals",
                      matched_levels, matched_n, sum(t04_tot$match)))

# ---- T05, T06: named bigram frequencies ---------------------------------------
bg <- read_chr(file.path(out_dir, "capture-part6-bigrams-full.csv"))
bg$observed_freq <- as.integer(bg$observed_freq)
freq_of <- function(g) bg$observed_freq[bg$ksngrams == g]
rank_of <- function(g) {
  r <- rank(-bg$observed_freq, ties.method = "min")
  r[bg$ksngrams == g]
}
t05 <- data.frame(
  item = c("A1 C1 observed", "C1 G1 observed", "share of 483 objects (%)",
           "share of t = 482 (%)"),
  published = c("44", "44", "approx. 9", "approx. 9"),
  reproduced = c(freq_of("A1 C1"), freq_of("C1 G1"),
                 sprintf("%.2f", 100 * 44 / 483), sprintf("%.2f", 100 * 44 / 482)))
t05$match <- c(freq_of("A1 C1") == 44, freq_of("C1 G1") == 44,
               round(100 * 44 / 483) == 9, round(100 * 44 / 482) == 9)
write_result(t05, "t05-a1c1-c1g1")
record("T05", 3L, as.integer(sum(t05$match[1:3])),
       note = "two counts plus the ~9% share (44/483 = 9.11%)")
t06 <- data.frame(item = c("A1 G1 observed", "A1 G1 rank by frequency"),
                  published = c(28L, 3L),
                  reproduced = c(freq_of("A1 G1"), rank_of("A1 G1")))
t06$match <- t06$published == t06$reproduced
write_result(t06, "t06-a1g1")
record("T06", 1L, as.integer(all(t06$match)), note = "frequency 28 and rank 3")

# ---- T07: Figure 3 PMI labels and bar order -----------------------------------
pub3 <- read_chr(file.path(pub_dir, "fig3-labels.csv"))
t07 <- do.call(rbind, lapply(letters[1:6], function(p) {
  lab <- read_chr(file.path(out_dir, paste0("capture-fig3", p, "-labels.csv")))
  ord <- read_chr(file.path(out_dir, paste0("capture-fig3", p, "-axis-order.csv")))
  top_down <- rev(ord$skipgram)
  pp <- pub3[pub3$panel == p, ]
  data.frame(panel = p, position_from_top = pp$position_from_top,
             skipgram = pp$skipgram, published_label = pp$label,
             reproduced_label = lab$label_4dp[match(pp$skipgram, lab$Skipgram)],
             reproduced_pmi_full = lab$PMI[match(pp$skipgram, lab$Skipgram)],
             reproduced_skipgram_at_position = top_down[as.integer(pp$position_from_top)])
}))
t07$label_match <- !is.na(t07$reproduced_label) &
  t07$published_label == t07$reproduced_label
t07$order_match <- t07$skipgram == t07$reproduced_skipgram_at_position
write_result(t07, "t07-fig3-labels")
# Bar stacks (per-chronology object counts) for visual comparison.
bars <- do.call(rbind, lapply(letters[1:6], function(p) {
  b <- read_chr(file.path(out_dir, paste0("capture-fig3", p, "-bars.csv")))
  data.frame(panel = p, b[, c("Skipgram", "Chronology", "Frequency")])
}))
write_result(bars, "t07-fig3-bar-stacks")
record("T07", nrow(t07), sum(t07$label_match),
       max_abs = max(abs(as.numeric(t07$published_label) -
                           as.numeric(t07$reproduced_label)), na.rm = TRUE),
       note = sprintf("labels; bar order matches at %d/%d positions",
                      sum(t07$order_match), nrow(t07)))

# ---- T08, T09: culture-exclusive salient bigrams (Fig. 3b objects) ----------
b3 <- read_chr(file.path(out_dir, "capture-fig3b-bars.csv"))
b3$Frequency <- as.integer(b3$Frequency)
excl <- b3 %>% group_by(Skipgram) %>%
  summarise(levels = paste(sort(unique(Chronology)), collapse = " + "),
            n_levels = n_distinct(Chronology), objects = sum(Frequency),
            .groups = "drop")
excl$exclusive_to <- ifelse(excl$n_levels == 1, excl$levels, NA_character_)
write_result(excl, "t08-fig3b-chronology-exclusivity")
named_erte <- c("I5 I13", "C5 D7", "C4 C12", "C12 C13", "C4 C5", "I1 I13",
                "C5 C13", "I1 I5")
rep_erte <- excl$Skipgram[excl$exclusive_to %in% "Ertebølle"]
t08 <- data.frame(
  item = c("exclusive to Maglemose (count)", "exclusive to Kongemose (count)",
           "exclusive to Ertebølle (count)", "Kongemose-exclusive bigram named",
           "8 named Ertebølle bigrams all exclusive", "Ertebølle-exclusive not named in text"),
  published = c("0", "1", "9", "B10 F38", "yes", "(none: text says nine, lists eight)"),
  reproduced = c(sum(excl$exclusive_to %in% "Maglemose"),
                 sum(excl$exclusive_to %in% "Kongemose"),
                 length(rep_erte),
                 paste(excl$Skipgram[excl$exclusive_to %in% "Kongemose"], collapse = "; "),
                 ifelse(all(named_erte %in% rep_erte), "yes", "no"),
                 paste(setdiff(rep_erte, named_erte), collapse = "; ")))
t08$match <- c(t08$published[1:5] == t08$reproduced[1:5], NA)
write_result(t08, "t08-culture-exclusive-counts")
record("T08", 3L, sum(t08$match[1:3]),
       note = "counts 0/1/9; names checked separately (C5 C12 unnamed in text)")
excl_any <- excl[!is.na(excl$exclusive_to), ]
t09 <- data.frame(item = "max objects among culture-exclusive Fig. 3b bigrams",
                  published = 5L, reproduced = max(excl_any$objects),
                  argmax = paste(excl_any$Skipgram[excl_any$objects ==
                                                     max(excl_any$objects)],
                                 collapse = "; "))
t09$match <- t09$published == t09$reproduced
write_result(t09, "t09-max-exclusive-frequency")
record("T09", 1L, as.integer(t09$match))

# ---- T10: Table 2 --------------------------------------------------------------
pub2 <- read_chr(file.path(pub_dir, "table2.csv"))
rep2 <- read_chr(file.path(out_dir, "capture-table2-pmi-summary.csv"))
t10 <- merge(pub2, rep2[, c("complex", "statistic", "value")],
             by = c("complex", "statistic"), suffixes = c("_published", "_reproduced"))
t10$abs_difference <- abs(as.numeric(t10$value_published) -
                            as.numeric(t10$value_reproduced))
t10$reproduced_2dp <- sprintf("%.2f", as.numeric(t10$value_reproduced))
t10$within_precision <- t10$abs_difference <= 0.005 + 1e-12
write_result(t10, "t10-table2")
record("T10", nrow(t10), sum(t10$within_precision), max_abs = max(t10$abs_difference))

# ---- T11: Figure 4 culture-exclusive boxes (aid: authors' createResultTable) --
s2_exprs <- parse(file.path(root, "data", "Herskind&Riede_S2.R"), encoding = "UTF-8")
pick <- function(name) {
  for (e in s2_exprs) {
    if (is.call(e) && identical(e[[1]], as.name("<-")) &&
        identical(e[[2]], as.name(name))) return(e)
  }
  stop("expression not found: ", name)
}
data <- s1  # the authors' object name, required by their chrongrams line
eval(pick("chrongrams"))          # chrongrams <- data[,c(11,31:289)]
eval(pick("createResultTable"))   # the authors' function, verbatim
heat_bigrams <- bg[bg$observed_freq > 2, ]
heat_table <- createResultTable(heat_bigrams)
heat_excl <- heat_table %>% group_by(Skipgram) %>%
  summarise(levels = paste(sort(unique(Chronology)), collapse = " + "),
            n_levels = n_distinct(Chronology), .groups = "drop")
heat_excl$box_colour <- ifelse(heat_excl$n_levels == 1,
                               c(Maglemose = "purple", Kongemose = "red",
                                 `Ertebølle` = "yellow")[heat_excl$levels], NA)
heat_excl$PMI <- as.numeric(heat_bigrams$PMI[match(heat_excl$Skipgram,
                                                    heat_bigrams$ksngrams)])
write_result(heat_excl, "t11-fig4-exclusive-cells-observed-gt-2")
axis_order <- toupper(c("a14","b3","a24","b10","b2","b12","e4","a5","d5","b13","b4",
                        "b1","a1","a3","ant","f12","e1","b6","e5","f5","f13","f38",
                        "d29","b8","d33","h1","g2","c1","f14","i1","f35","zoo","d19",
                        "g1","d3","d15","f15","c12","c14","c5","c13","c4","c6","d7",
                        "f55","g7","i13","i5","relief"))
cells <- do.call(rbind, lapply(seq_len(nrow(heat_excl)), function(i) {
  tk <- strsplit(heat_excl$Skipgram[i], " ")[[1]]
  o <- match(tk, axis_order)
  data.frame(x = axis_order[min(o)], y = axis_order[max(o)],
             PMI = heat_excl$PMI[i], box = heat_excl$box_colour[i])
}))
cells$x <- factor(cells$x, levels = axis_order)
cells$y <- factor(cells$y, levels = axis_order)
box_cols <- c(purple = "#8E7CC3", red = "#CC4125", yellow = "#F1C232")
p11 <- ggplot(cells, aes(x = x, y = y)) +
  geom_tile(aes(fill = PMI), colour = "grey90") +
  geom_tile(data = cells[!is.na(cells$box), ], aes(colour = box), fill = NA,
            linewidth = 0.9, width = 0.8, height = 0.8) +
  scale_fill_gradient2(low = "white", mid = "white", high = "red", midpoint = 0.5) +
  scale_colour_manual(values = box_cols, name = "single culture") +
  scale_x_discrete(limits = axis_order, drop = FALSE, position = "top") +
  scale_y_discrete(limits = axis_order, drop = FALSE) +
  labs(x = NULL, y = NULL,
       title = "AID: observed > 2 bigrams, upper-left triangle; boxes = single-culture") +
  theme_minimal(base_size = 9) +
  theme(axis.text.x = element_text(angle = 90, hjust = 0, vjust = 0.5))
ggsave(file.path(aid_dir, "fig4-exclusive-boxes-aid.png"), p11, width = 9,
       height = 8.5, dpi = 200)
record("T11", sum(!is.na(heat_excl$box_colour)), NA_integer_,
       note = paste("aid cells with single-culture box (observed > 2):",
                    paste(names(table(heat_excl$box_colour)),
                          table(heat_excl$box_colour), collapse = ", "),
                    "- compared visually"))

# ---- T12, T13, T14: Table 3 objects, counts, and Fig. 5 (aid: S1 lookup) -----
pub3t <- read_chr(file.path(pub_dir, "table3.csv"))
cluster_k <- rowSums(s1[, cluster])
# Row lookup: a site name can occur on several S1 rows (e.g. "Korsør,
# Glasværk"), so among the rows with the published site name take the one
# bearing >= 2 of the five cluster motifs (the Table 3 / Fig. 5 selection
# basis). The Figure field is deliberately NOT used as a key, because it is one
# of the compared fields. Ambiguity (0 or > 1 candidates) is recorded.
row_for_site <- vapply(pub3t$site, function(site) {
  cand <- which(s1$Site == site & cluster_k >= 2)
  if (length(cand) == 1) cand else NA_integer_
}, integer(1))
site_rows_total <- vapply(pub3t$site, function(site) sum(s1$Site == site), integer(1))
s1_lookup <- s1[row_for_site,
                c("No.", "Site", "Region", "Material", "Artefact type",
                  "Motifs_as_text", "Figure", "Chronology", "Coord.Long",
                  "Coord.Lat")]
t12 <- data.frame(number = pub3t$number, s1_row_no = s1_lookup$`No.`,
                  s1_rows_with_site_name = unname(site_rows_total),
                  site_published = pub3t$site, site_s1 = s1_lookup$Site,
                  region_published = pub3t$region, region_s1 = s1_lookup$Region,
                  type_published = pub3t$artefact_type,
                  type_s1 = paste(s1_lookup$Material, s1_lookup$`Artefact type`),
                  motifs_published = pub3t$motifs,
                  motifs_s1 = trimws(s1_lookup$Motifs_as_text),
                  figure_published = pub3t$figure_plonka, figure_s1 = s1_lookup$Figure)
t12$site_match <- t12$site_published == t12$site_s1
t12$region_match <- t12$region_published == t12$region_s1
t12$type_match <- tolower(t12$type_published) == tolower(t12$type_s1)
t12$motifs_match <- t12$motifs_published == t12$motifs_s1
t12$figure_match <- t12$figure_published == t12$figure_s1
write_result(t12, "t12-table3")
m12 <- sum(t12[, grep("_match$", names(t12))], na.rm = TRUE)
record("T12", 50L, m12,
       note = "type compared as S1 Material + Artefact type, case-insensitive")

bearing <- s1[cluster_k >= 2, c("No.", "Site", "Material", "Artefact type")]
t13 <- data.frame(
  item = c("S1 objects bearing >= 2 of C4/C5/C12/C13/D7",
           "same objects identical to the Table 3 list",
           "antler axes among Table 3 objects", "antler shafts among Table 3 objects"),
  published = c("10", "yes", "9", "1"),
  reproduced = c(nrow(bearing),
                 ifelse(setequal(bearing$Site, pub3t$site), "yes", "no"),
                 sum(s1_lookup$Material == "antler" & s1_lookup$`Artefact type` == "axe"),
                 sum(s1_lookup$Material == "antler" & s1_lookup$`Artefact type` == "shaft")))
t13$match <- t13$published == t13$reproduced
write_result(t13, "t13-cluster-objects")
record("T13", 2L, as.integer(t13$match[1]) + as.integer(all(t13$match[3:4])),
       note = "count 10; 9 axes + 1 shaft")

pies <- read_chr(file.path(pub_dir, "fig5-pies.csv"))
s1_pies <- vapply(seq_len(nrow(s1_lookup)), function(i) {
  present <- cluster[unlist(s1[row_for_site[i], cluster]) == 1]
  paste(present, collapse = " ")
}, character(1))
t14 <- data.frame(number = pies$number, site = pub3t$site,
                  pie_published = pies$cluster_motifs_in_pie, pie_s1 = s1_pies,
                  long = as.numeric(s1_lookup$Coord.Long),
                  lat = as.numeric(s1_lookup$Coord.Lat))
t14$pie_match <- t14$pie_published == t14$pie_s1
write_result(t14, "t14-fig5-pies")
p14 <- ggplot(t14, aes(long, lat, label = number)) + geom_point(size = 3) +
  geom_text(nudge_y = 0.06) + coord_quickmap() +
  labs(title = "AID: S1 coordinates of the ten Table 3 objects") + theme_bw()
ggsave(file.path(aid_dir, "fig5-object-positions-aid.png"), p14, width = 6,
       height = 5, dpi = 150)
record("T14", 10L, sum(t14$pie_match),
       note = "pie compositions; positions compared visually; patches untestable")

# Fig. 2 map panel aid: all S1 coordinates coloured by chronology.
map_df <- data.frame(long = suppressWarnings(as.numeric(s1$Coord.Long)),
                     lat = suppressWarnings(as.numeric(s1$Coord.Lat)),
                     Chronology = s1$Chronology)
write_result(data.frame(objects = nrow(map_df),
                        with_coordinates = sum(complete.cases(map_df[, 1:2]))),
             "t02-map-coordinate-coverage")
p02 <- ggplot(map_df[complete.cases(map_df[, 1:2]), ],
              aes(long, lat, colour = Chronology)) +
  geom_point(size = 1.6, alpha = 0.85) +
  scale_colour_manual(values = c("#FAD02E", "#D98888", "#E8BB8B", "#B4A1C1")) +
  coord_quickmap() + labs(title = "AID: S1 coordinates by chronology") + theme_bw()
ggsave(file.path(aid_dir, "fig2-map-points-aid.png"), p02, width = 7, height = 6,
       dpi = 150)

# ---- T15: S3 deposit vs reproduced Part 8 CSVs --------------------------------
compare_sheet <- function(sheet, csv, n_tok) {
  s3 <- suppressMessages(read_excel(file.path(root, "data", "Herskind&Riede_S3.xlsx"),
                                    sheet = sheet, skip = 2, col_names = FALSE,
                                    col_types = "text"))
  s3 <- as.data.frame(s3)
  names(s3) <- c(paste0("token", 1:n_tok), paste0("token", 1:n_tok, "_freq"),
                 "observed_freq", "expected_freq", "PMI")
  rp <- utils::read.csv(file.path(out_dir, csv), colClasses = "character")
  key_s3 <- do.call(paste, s3[, 1:n_tok])
  key_rp <- do.call(paste, rp[, 1:n_tok])
  num_cols <- names(s3)[-(1:n_tok)]
  idx <- match(key_s3, key_rp)
  long <- do.call(rbind, lapply(num_cols, function(col) {
    a <- as.numeric(s3[[col]]); b <- as.numeric(rp[[col]][idx])
    data.frame(sheet = sheet, skipgram = key_s3, column = col, s3 = s3[[col]],
               reproduced = rp[[col]][idx], abs_diff = abs(a - b),
               rel_diff = ifelse(a == 0, abs(a - b), abs(a - b) / abs(a)))
  }))
  list(cells = long,
       membership = data.frame(sheet = sheet, rows_s3 = nrow(s3), rows_reproduced = nrow(rp),
                               s3_not_in_reproduced = sum(is.na(idx)),
                               reproduced_not_in_s3 = sum(!key_rp %in% key_s3),
                               row_order_identical = identical(key_s3, key_rp)))
}
t15 <- list(compare_sheet("bigrams", "Bigrams.csv", 2),
            compare_sheet("trigrams", "Trigrams.csv", 3),
            compare_sheet("quadrigrams", "Quadrigrams.csv", 4))
t15_cells <- do.call(rbind, lapply(t15, `[[`, "cells"))
t15_cells$within_precision <- !is.na(t15_cells$rel_diff) & t15_cells$rel_diff <= 1e-12
t15_cells$exact <- !is.na(t15_cells$abs_diff) & t15_cells$abs_diff == 0
write_result(t15_cells, "t15-s3-cells")
write_result(do.call(rbind, lapply(t15, `[[`, "membership")), "t15-s3-membership")
record("T15", nrow(t15_cells), sum(t15_cells$within_precision),
       max_abs = max(t15_cells$abs_diff, na.rm = TRUE),
       note = sprintf("exact %d; max relative difference %.3g",
                      sum(t15_cells$exact), max(t15_cells$rel_diff, na.rm = TRUE)))

write_result(do.call(rbind, summary_rows), "summary")
cat("compare.R completed\n")
