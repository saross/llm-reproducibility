#!/usr/bin/env Rscript
# =============================================================================
# compare-results.R — value-level comparison, Herskind & Riede 2024, attempt 03
# =============================================================================
#
# Purpose
#   Compare the reproduced values against the published values for the 20
#   locked targets (T01-T20) of the approved plan, at the plan's tolerances,
#   and write one value-level CSV per target to comparison-out/.
#
# Rules this script keeps
#   - It never runs or edits the authors' code. It reads, read-only:
#       * wrapper-captures/authors-session.RData — the authors' finished S2.R
#         session (objects as the authors' code left them);
#       * wrapper-captures/bigrams-before-part7.rds — `bigrams` just before
#         S2.R line 633 overwrote it;
#       * wrapper-captures/analysis-console.txt — S2.R's printed output;
#       * authors-run/*.csv — S2.R's own exported tables;
#       * materials/Herskind&Riede_S3.xlsx — the authors' deposited tables;
#       * published-values/*.csv — values transcribed from the paper.
#   - Every verification aid is labelled "R1 aid" (registrant ruling R1):
#     either a read-only lookup in the deposited data or a call to a documented
#     function of a package the authors used (ggplot2::layer_data,
#     ggplot2::ggplot_build, quanteda::ntoken, base summary/table). Aids make
#     no new statistical choice.
#   - Visual targets (T04, T06, T07) also get aid plots under
#     comparison-out/aid-plots/; their scoring is done by eye in the report.
#
# Usage: run by run-reproduction.sh inside the lane container, after
#   run-analysis.R; never on the host.
# =============================================================================

suppressPackageStartupMessages({
  library(quanteda)
  library(readxl)
  library(ggplot2)
  library(dplyr)
  library(data.table)
})

out_dir <- "comparison-out"
aid_dir <- file.path(out_dir, "aid-plots")
dir.create(aid_dir, recursive = TRUE, showWarnings = FALSE)

# The authors' finished session is restored into the global environment, as
# it was when S2.R ended: the plots' aesthetics (quosures) refer to the global
# environment (e.g. skipgram_order1), and save() stores that only by reference.
# Every comparison variable lives inside local() below, so nothing here can
# overwrite or shadow an authors' object.
load("wrapper-captures/authors-session.RData", envir = globalenv())

local({
  authors <- globalenv()
  bigrams_full <- readRDS("wrapper-captures/bigrams-before-part7.rds")
  console <- readLines("wrapper-captures/analysis-console.txt", encoding = "UTF-8")
  expr_log <- read.csv("wrapper-captures/expression-log.csv", stringsAsFactors = FALSE)
  pub_dir <- "published-values"

  # Accumulators live in an environment (no super-assignment needed).
  acc <- new.env()
  acc$summary_rows <- list()
  acc$nv <- list()
  record <- function(target, compared, matched, note = "") {
    acc$summary_rows[[length(acc$summary_rows) + 1]] <- data.frame(
      target_id = target, values_compared = compared, values_matched = matched,
      note = note, stringsAsFactors = FALSE)
    cat(sprintf("COMPARE %s: %d/%d matched %s\n", target, matched, compared, note))
  }

  # ---- Helper: printed output of one S2.R expression, by its first line -------
  expr_output <- function(first_line) {
    idx <- expr_log$index[expr_log$first_line == first_line]
    stopifnot(length(idx) == 1)
    start <- grep(sprintf("^LLMR-EXPR %d \\(", idx), console)
    nxt <- grep("^LLMR-EXPR ", console)
    end <- min(c(nxt[nxt > start], length(console) + 1)) - 1
    out <- console[(start + 1):end]
    out[!grepl("^LLMR-(WARNING|MESSAGE)", out) & nzchar(trimws(out))]
  }

  # Parse a printed 1-D table (alternating name and count lines after a header).
  parse_printed_table <- function(lines) {
    body <- lines[-1]  # first line is the dimnames header (e.g. "freqs")
    stopifnot(length(body) %% 2 == 0)
    nm <- character(); val <- character()
    for (j in seq(1, length(body), by = 2)) {
      nm <- c(nm, strsplit(trimws(body[j]), "\\s+")[[1]])
      val <- c(val, strsplit(trimws(body[j + 1]), "\\s+")[[1]])
    }
    stopifnot(length(nm) == length(val))
    data.frame(frequency = as.integer(nm), n = as.integer(val))
  }

  # Status of the expressions a target depends on (credit rule, invariant 2 Q6).
  untolerated_errors <- sum(expr_log$status == "ERROR")
  cat("Expressions with untolerated errors:", untolerated_errors, "\n")

  # ============================================================================
  # T01 — Table 1 (frequency-of-frequencies; 126 cells + 4 header totals)
  # ============================================================================
  pub1 <- read.csv(file.path(pub_dir, "table1.csv"))
  pub1_tot <- read.csv(file.path(pub_dir, "table1-totals.csv"))
  printed <- list(unigram = parse_printed_table(expr_output(232)),
                  bigram = parse_printed_table(expr_output(234)),
                  trigram = parse_printed_table(expr_output(241)),
                  quadrigram = parse_printed_table(expr_output(248)))
  # Consistency: the printed tables equal table() of the session objects.
  from_objects <- list(unigram = table(authors$freqs), bigram = table(authors$bigramfreqs),
                       trigram = table(authors$trigramfreqs),
                       quadrigram = table(authors$quadrigramfreqs))
  for (lv in names(printed)) {
    stopifnot(identical(printed[[lv]]$n, as.integer(unname(from_objects[[lv]]))),
              identical(printed[[lv]]$frequency, as.integer(names(from_objects[[lv]]))))
  }
  t1 <- do.call(rbind, lapply(names(printed), function(lv) {
    p <- pub1[pub1$level == lv, ]
    r <- printed[[lv]]
    m <- merge(p, r, by = "frequency", all = TRUE, suffixes = c("_published", "_reproduced"))
    m$level <- lv
    m[order(-m$frequency), c("level", "frequency", "n_published", "n_reproduced")]
  }))
  # Two elements per row (the plan's 126 cells): the frequency value itself
  # (present in both tables) and its count n.
  t1$frequency_match <- !is.na(t1$n_published) & !is.na(t1$n_reproduced)
  t1$match <- t1$frequency_match & t1$n_published == t1$n_reproduced
  printed_len <- vapply(c(256, 258, 260, 262), function(l)
    as.integer(sub("^\\[1\\]\\s+", "", expr_output(l)[1])), integer(1))
  t1_tot <- data.frame(level = pub1_tot$level, n_distinct_published = pub1_tot$n_distinct,
                       n_distinct_reproduced = printed_len)
  t1_tot$match <- t1_tot$n_distinct_published == t1_tot$n_distinct_reproduced
  write.csv(t1, file.path(out_dir, "t01-table1-cells.csv"), row.names = FALSE)
  write.csv(t1_tot, file.path(out_dir, "t01-table1-totals.csv"), row.names = FALSE)
  record("T01", 2 * nrow(t1) + nrow(t1_tot),
         sum(t1$frequency_match) + sum(t1$match) + sum(t1_tot$match),
         sprintf("(rows %d = %d cells, header totals %d; element gate expects 130)",
                 nrow(t1), 2 * nrow(t1), nrow(t1_tot)))

  # Paper-error protocol evidence for T01 (labelled; computes nothing new).
  # (a) Tier 2: the authors' deposited S3 tables list every skipgram with
  #     observed frequency > 2, so their frequency-of-frequencies for f >= 3
  #     can arbitrate the published and reproduced Table 1 cells there.
  s3_obs <- list(
    bigram = read_excel("materials/Herskind&Riede_S3.xlsx", sheet = "bigrams", skip = 2,
                        col_names = FALSE, .name_repair = "minimal")[[5]],
    trigram = read_excel("materials/Herskind&Riede_S3.xlsx", sheet = "trigrams", skip = 2,
                         col_names = FALSE, .name_repair = "minimal")[[7]],
    quadrigram = read_excel("materials/Herskind&Riede_S3.xlsx", sheet = "quadrigrams",
                            skip = 2, col_names = FALSE, .name_repair = "minimal")[[9]])
  t1$n_in_s3 <- NA_integer_
  for (lv in names(s3_obs)) {
    tab <- table(s3_obs[[lv]])
    sel <- t1$level == lv & t1$frequency >= 3
    t1$n_in_s3[sel] <- as.integer(tab[as.character(t1$frequency[sel])])
    t1$n_in_s3[sel & is.na(t1$n_in_s3)] <- 0L
  }
  # (b) Consistency of each column's total occurrences with the deposited
  #     data: with k = 13 and at most 15 motifs per object, every combination
  #     of an object's motifs is a skipgram, so sum(frequency x n) must equal
  #     sum over objects of choose(tokens, n). Tokens per object from
  #     quanteda::ntoken on the authors' corpus (R1 aid: documented function).
  ntok <- ntoken(tokens(authors$corpus))
  t1_occ <- do.call(rbind, lapply(c(bigram = 2, trigram = 3, quadrigram = 4), function(nn) {
    lv <- c("2" = "bigram", "3" = "trigram", "4" = "quadrigram")[[as.character(nn)]]
    x <- t1[t1$level == lv, ]
    data.frame(level = lv,
               published_sum_f_times_n = sum(x$frequency * x$n_published, na.rm = TRUE),
               reproduced_sum_f_times_n = sum(x$frequency * x$n_reproduced, na.rm = TRUE),
               deposited_data_sum_choose = sum(choose(ntok, nn)))
  }))
  write.csv(t1, file.path(out_dir, "t01-table1-cells.csv"), row.names = FALSE)
  write.csv(t1_occ, file.path(out_dir, "t01-occurrence-totals.csv"), row.names = FALSE)
  print(t1[!t1$match, ])
  print(t1_occ)

  # ============================================================================
  # T02 — Table 2 (PMI summary statistics by culture complex; 18 values)
  # ============================================================================
  pub2 <- read.csv(file.path(pub_dir, "table2.csv"), check.names = FALSE)
  vecs <- list(Maglemose = authors$magle_ksngram_subset$PMI,
               Kongemose = authors$konge_ksngram_subset$PMI,
               Ertebolle = authors$erte_ksngram_subset$PMI)
  # summary() is the authors' own call (S2.R lines 318-320); unclass() reads its
  # unrounded values (R >= 4.0 keeps full precision and rounds only on print).
  stat_map <- c("Maximum" = "Max.", "3rd quartile" = "3rd Qu.", "Mean" = "Mean",
                "Median" = "Median", "1st quartile" = "1st Qu.", "Minimum" = "Min.")
  t2 <- do.call(rbind, lapply(names(vecs), function(cx) {
    s <- unclass(summary(vecs[[cx]]))
    data.frame(complex = cx, statistic = pub2$statistic,
               published = pub2[[cx]], reproduced_full = unname(s[stat_map[pub2$statistic]]),
               n_bigrams = length(vecs[[cx]]))
  }))
  t2$reproduced_2dp <- round(t2$reproduced_full, 2)
  t2$abs_diff <- abs(t2$reproduced_full - t2$published)
  t2$exact_2dp <- abs(t2$reproduced_2dp - t2$published) < 1e-9
  t2$within_0005 <- t2$abs_diff <= 0.005 + 1e-12
  t2$category <- ifelse(t2$exact_2dp, "EXACT_MATCH",
                        ifelse(t2$within_0005, "WITHIN_PRECISION", "MISMATCH"))
  write.csv(t2, file.path(out_dir, "t02-table2.csv"), row.names = FALSE)
  # Printed summary() output, for the record.
  writeLines(c(expr_output(318), expr_output(319), expr_output(320)),
             file.path(out_dir, "t02-printed-summaries.txt"))
  # Cross-check: the Ertebolle maximum is the top bigram PMI in S3 (I5-I13).
  s3_bi <- read_excel("materials/Herskind&Riede_S3.xlsx", sheet = "bigrams",
                      skip = 2, col_names = FALSE, .name_repair = "minimal")
  cat("T02 cross-check: Ertebolle max", max(vecs$Ertebolle), "vs S3 top PMI",
      max(s3_bi[[7]]), "\n")
  record("T02", nrow(t2), sum(t2$category != "MISMATCH"),
         sprintf("(exact at 2 dp: %d; max |diff| %.5f)", sum(t2$exact_2dp), max(t2$abs_diff)))

  # ============================================================================
  # T03 — Table 3 (ten cluster objects; 50 values). R1 aid: read-only lookup.
  # ============================================================================
  pub3 <- read.csv(file.path(pub_dir, "table3.csv"), stringsAsFactors = FALSE,
                   encoding = "UTF-8")
  dat <- authors$data   # the authors' read_excel() of S1
  motif_cols <- 16:30   # S1 'Motifs' columns (P-AD)
  norm <- function(x) tolower(gsub("[[:space:]\"'“”„]+", " ", trimws(x)))
  motif_set <- function(row) {
    v <- unlist(lapply(motif_cols, function(j) as.character(dat[[j]][row])))
    v <- trimws(v[!is.na(v) & nzchar(trimws(v))])
    paste(sort(toupper(v)), collapse = " ")
  }
  t3 <- do.call(rbind, lapply(seq_len(nrow(pub3)), function(r) {
    p <- pub3[r, ]
    hits <- which(as.character(dat$Figure) == p$figure_plonka)
    if (length(hits) > 1) {
      by_site <- hits[norm(dat$Site[hits]) == norm(p$site)]
      if (length(by_site) >= 1) hits <- by_site
    }
    if (length(hits) != 1) {
      return(data.frame(row = p$row, element = c("site", "region", "artefact_type",
                                                 "motifs", "figure"),
                        published = c(p$site, p$region, p$artefact_type, p$motifs,
                                      p$figure_plonka),
                        s1_value = NA_character_, s1_row_no = NA_character_,
                        match = FALSE, note = sprintf("%d S1 rows matched", length(hits))))
    }
    h <- hits
    type_s1 <- paste(dat$Material[h], dat[["Artefact type"]][h])
    pub_motifs <- paste(sort(strsplit(p$motifs, " ")[[1]]), collapse = " ")
    vals <- c(dat$Site[h], dat$Region[h], type_s1, motif_set(h), as.character(dat$Figure[h]))
    pubs <- c(p$site, p$region, p$artefact_type, pub_motifs, p$figure_plonka)
    data.frame(row = p$row, element = c("site", "region", "artefact_type", "motifs", "figure"),
               published = pubs, s1_value = vals, s1_row_no = as.character(dat[["No."]][h]),
               match = norm(vals) == norm(pubs),
               note = c("normalised: case, whitespace, quotation marks", "",
                        "S1 Material + Artefact type", "order-free set", ""))
  }))
  write.csv(t3, file.path(out_dir, "t03-table3.csv"), row.names = FALSE, fileEncoding = "UTF-8")
  record("T03", nrow(t3), sum(t3$match), "(R1 aid: read-only S1 lookup)")
  t3_rows <- unique(as.integer(t3$s1_row_no[!is.na(t3$s1_row_no)]))

  # ============================================================================
  # T04 — Figure 2 (left: bar chart from the authors' code; right: map aid)
  # ============================================================================
  ld <- layer_data(authors$artefact_type_chronology, 1)   # R1 aid: documented ggplot2
  bld <- ggplot_build(authors$artefact_type_chronology)
  ylab <- bld$layout$panel_params[[1]]$y$get_labels()
  fill_levels <- levels(factor(authors$DS$Chronology))
  fill_map <- setNames(fill_levels, c("#FAD02E", "#D98888", "#E8BB8B", "#B4A1C1")[seq_along(fill_levels)])
  t4 <- data.frame(artefact_type = ylab[as.integer(ld$y)], chronology = unname(fill_map[ld$fill]),
                   count = ld$count)
  t4_wide <- reshape(t4, idvar = "artefact_type", timevar = "chronology", direction = "wide")
  t4_wide[is.na(t4_wide)] <- 0
  t4_wide$total <- rowSums(t4_wide[, -1, drop = FALSE])
  t4_wide <- t4_wide[match(rev(ylab), t4_wide$artefact_type), ]
  write.csv(t4_wide, file.path(out_dir, "t04-fig2-left-bars.csv"), row.names = FALSE,
            fileEncoding = "UTF-8")
  cat("T04 left panel: bars", nrow(t4_wide), "; objects", sum(t4_wide$total), "\n")
  # Scored against the measured published segments (published-values/fig2-left.csv).
  pub2l <- read.csv(file.path(pub_dir, "fig2-left.csv"), stringsAsFactors = FALSE,
                    encoding = "UTF-8")
  chron4 <- c("Maglemose", "Kongemose", "Kongemose/Ertebølle", "Ertebølle")
  t4_cmp <- do.call(rbind, lapply(seq_len(nrow(t4_wide)), function(i) {
    ty <- t4_wide$artefact_type[i]
    pb <- pub2l[pub2l$artefact_type == ty, ]
    data.frame(bar_rank = i, artefact_type = ty,
               published_rank = if (nrow(pb)) pb$bar_rank[1] else NA,
               chronology = chron4,
               published = vapply(chron4, function(cn) sum(pb$count[pb$chronology == cn]),
                                   numeric(1)),
               reproduced = vapply(chron4, function(cn) {
                 v <- t4_wide[[paste0("count.", cn)]][i]; if (is.null(v)) 0 else v },
                 numeric(1)),
               published_stack_order = paste(pb$chronology[order(pb$segment_order)],
                                             collapse = " > "),
               stringsAsFactors = FALSE)
  }))
  # The reproduced stack order (left to right) of each bar, from layer_data xmin.
  ord <- tapply(seq_len(nrow(ld)), ylab[as.integer(ld$y)], function(ix)
    paste(unname(fill_map[ld$fill[ix][order(ld$xmin[ix])]]), collapse = " > "))
  t4_cmp$reproduced_stack_order <- unname(ord[t4_cmp$artefact_type])
  t4_cmp$match <- t4_cmp$published == t4_cmp$reproduced &
    t4_cmp$published_rank == t4_cmp$bar_rank
  write.csv(t4_cmp, file.path(out_dir, "t04-fig2-left-compare.csv"), row.names = FALSE,
            fileEncoding = "UTF-8")
  same_order <- t4_cmp$published_stack_order == t4_cmp$reproduced_stack_order
  cat("T04 left panel: segment counts matching", sum(t4_cmp$match), "of", nrow(t4_cmp),
      "; bars whose stack order matches", sum(same_order[!duplicated(t4_cmp$artefact_type)]),
      "of", nrow(t4_wide), "\n")
  print(unique(t4_cmp[, c("published_stack_order", "reproduced_stack_order")]))
  # Right panel, R1 aid: plot S1 coordinates coloured by Chronology (no statistics).
  map_df <- data.frame(lon = as.numeric(dat$Coord.Long), lat = as.numeric(dat$Coord.Lat),
                       Chronology = dat$Chronology)
  # Objects whose coordinates do not parse as numbers, with their raw values.
  bad_xy <- which(is.na(map_df$lon) | is.na(map_df$lat))
  write.csv(data.frame(No = dat[["No."]][bad_xy], Site = dat$Site[bad_xy],
                       Coord.Long = as.character(dat$Coord.Long[bad_xy]),
                       Coord.Lat = as.character(dat$Coord.Lat[bad_xy]),
                       Chronology = dat$Chronology[bad_xy]),
            file.path(out_dir, "t04-fig2-map-unplotted.csv"), row.names = FALSE,
            fileEncoding = "UTF-8")
  write.csv(as.data.frame(table(Chronology = map_df$Chronology, has_coords =
                                  !is.na(map_df$lon) & !is.na(map_df$lat))),
            file.path(out_dir, "t04-fig2-map-counts.csv"), row.names = FALSE,
            fileEncoding = "UTF-8")
  map_plot <- ggplot(map_df[!is.na(map_df$lon), ], aes(lon, lat, colour = Chronology)) +
    geom_point(size = 1.6) + coord_quickmap() +
    scale_colour_manual(values = c("Maglemose" = "#B4A1C1", "Kongemose" = "#D98888",
                                   "Kongemose/Ertebølle" = "#E8BB8B", "Ertebølle" = "#FAD02E")) +
    labs(title = "R1 aid: S1 coordinates by Chronology (Fig. 2 map check)") + theme_bw()
  ggsave(file.path(aid_dir, "t04-fig2-map-aid.png"), map_plot, width = 8, height = 6, dpi = 120)
  record("T04", nrow(t4_cmp), sum(t4_cmp$match),
         sprintf("(left panel: 18 bars x 4 chronology segments; stack order matches in %d of 18 bars; map by eye)",
                 sum(same_order[!duplicated(t4_cmp$artefact_type)])))

  # ============================================================================
  # T05 — Figure 3 (six panels, 128 bars: label+PMI and total each = 256)
  # ============================================================================
  pub3f <- read.csv(file.path(pub_dir, "fig3.csv"), stringsAsFactors = FALSE)
  plots <- list(a = "bigramsBYfrequency", b = "bigramsBYpmi", c = "trigramsBYfrequency",
                d = "trigramsBYpmi", e = "quadrigramsBYfrequency", f = "quadrigramsBYpmi")
  chron_cols <- c(Maglemose = "maglemose", "Kongemose/Ertebølle" = "kongemose_ertebolle",
                  Kongemose = "kongemose", "Ertebølle" = "ertebolle")
  t5 <- do.call(rbind, lapply(names(plots), function(pn) {
    p <- get(plots[[pn]], envir = authors)
    b <- ggplot_build(p)                                   # R1 aid: documented ggplot2
    labs_y <- b$layout$panel_params[[1]]$y$get_labels()    # bottom-to-top order
    order_top <- rev(labs_y)
    txt <- layer_data(p, 2)                                # the drawn PMI labels
    pmi_lab <- setNames(as.character(txt$label), labs_y[as.integer(txt$y)])
    d <- p$data
    seg <- tapply(d$Frequency, list(d$Skipgram, d$Chronology), sum)
    seg[is.na(seg)] <- 0
    pub <- pub3f[pub3f$panel == pn, ]
    n <- max(nrow(pub), length(order_top))
    rows <- lapply(seq_len(n), function(r) {
      sk <- if (r <= length(order_top)) order_top[r] else NA_character_
      segs <- setNames(rep(0, 4), chron_cols)
      if (!is.na(sk)) for (cn in colnames(seg)) segs[chron_cols[[cn]]] <- seg[sk, cn]
      data.frame(panel = pn, rank = r,
                 published_skipgram = if (r <= nrow(pub)) pub$skipgram[r] else NA,
                 reproduced_skipgram = sk,
                 published_pmi = if (r <= nrow(pub)) sprintf("%.4f", pub$pmi_label[r]) else NA,
                 reproduced_pmi = if (!is.na(sk)) pmi_lab[[sk]] else NA,
                 published_total = if (r <= nrow(pub)) pub$total[r] else NA,
                 reproduced_total = sum(segs),
                 published_segments = if (r <= nrow(pub)) paste(pub[r, chron_cols], collapse = "/") else NA,
                 reproduced_segments = paste(segs, collapse = "/"),
                 stringsAsFactors = FALSE)
    })
    do.call(rbind, rows)
  }))
  t5$label_pmi_match <- !is.na(t5$published_skipgram) & !is.na(t5$reproduced_skipgram) &
    t5$published_skipgram == t5$reproduced_skipgram & t5$published_pmi == t5$reproduced_pmi
  t5$total_match <- !is.na(t5$published_total) & t5$published_total == t5$reproduced_total
  t5$segments_match <- !is.na(t5$published_segments) &
    t5$published_segments == t5$reproduced_segments
  # PMI labels that differ in identity/order only through exactly tied PMI values.
  t5$pmi_value_match <- t5$published_pmi == t5$reproduced_pmi
  write.csv(t5, file.path(out_dir, "t05-fig3-bars.csv"), row.names = FALSE, fileEncoding = "UTF-8")
  record("T05", 2 * nrow(t5), sum(t5$label_pmi_match) + sum(t5$total_match),
         sprintf("(bars %d; label+PMI %d; totals %d; segments %d/%d; element gate expects 256)",
                 nrow(t5), sum(t5$label_pmi_match), sum(t5$total_match),
                 sum(t5$segments_match), nrow(t5)))
  # Cross-check the drawn PMI labels against S3 (authors' tabulated values).
  s3_tri <- read_excel("materials/Herskind&Riede_S3.xlsx", sheet = "trigrams", skip = 2,
                       col_names = FALSE, .name_repair = "minimal")
  s3_quad <- read_excel("materials/Herskind&Riede_S3.xlsx", sheet = "quadrigrams", skip = 2,
                        col_names = FALSE, .name_repair = "minimal")
  s3_pmi <- c(setNames(s3_bi[[7]], paste(s3_bi[[1]], s3_bi[[2]])),
              setNames(s3_tri[[9]], paste(s3_tri[[1]], s3_tri[[2]], s3_tri[[3]])),
              setNames(s3_quad[[11]], paste(s3_quad[[1]], s3_quad[[2]], s3_quad[[3]],
                                            s3_quad[[4]])))
  xs <- data.frame(skipgram = t5$published_skipgram, published_pmi = t5$published_pmi,
                   s3_pmi_4dp = sprintf("%.4f", s3_pmi[t5$published_skipgram]))
  xs$agree <- xs$published_pmi == xs$s3_pmi_4dp
  write.csv(xs, file.path(out_dir, "t05-fig3-vs-s3.csv"), row.names = FALSE)
  cat("T05 cross-check: published labels agreeing with S3 at 4 dp:", sum(xs$agree, na.rm = TRUE),
      "of", nrow(xs), "\n")

  # ============================================================================
  # T06 — Figure 4 (heatmap): matrix m and the culture-exclusive box aid
  # ============================================================================
  m <- authors$m
  axis_order <- c("a14","b3","a24","b10","b2","b12","e4","a5","d5","b13","b4","b1","a1","a3","ant",
                  "f12","e1","b6","e5","f5","f13","f38","d29","b8","d33","h1","g2","c1","f14","i1",
                  "f35","zoo","d19","g1","d3","d15","f15","c12","c14","c5","c13","c4","c6","d7",
                  "f55","g7","i13","i5","relief")
  cat("T06: matrix", nrow(m), "x", ncol(m), "; axis order as specified:",
      identical(rownames(m), axis_order), "; non-zero off-diagonal cells (lower triangle):",
      sum(m[lower.tri(m)] != 0), "\n")
  # R1 aid: chronology of objects carrying both motifs of each freq > 2 bigram.
  chron <- dat$Chronology
  bg <- authors$bigrams_dt   # S2.R Part 8: freq > 2 bigrams, uppercase tokens
  excl <- do.call(rbind, lapply(seq_len(nrow(bg)), function(r) {
    t1n <- bg$token1[r]; t2n <- bg$token2[r]
    has <- dat[[t1n]] == 1 & dat[[t2n]] == 1
    cls <- sort(unique(chron[which(has)]))
    data.frame(token1 = t1n, token2 = t2n, observed_freq = bg$observed_freq[r], PMI = bg$PMI[r],
               objects = sum(has, na.rm = TRUE), classes = paste(cls, collapse = "; "),
               single_class = length(cls) == 1)
  }))
  write.csv(excl, file.path(out_dir, "t06-fig4-exclusive-lookup.csv"), row.names = FALSE,
            fileEncoding = "UTF-8")
  cat("T06 aid: freq>2 bigrams", nrow(excl), "; confined to one Chronology class",
      sum(excl$single_class), "\n")
  print(table(excl$classes[excl$single_class]))
  # Aid plot: the reproduced heatmap in the published orientation with boxes.
  hm <- as.data.frame(as.table(m)); names(hm) <- c("token1", "token2", "PMI")
  pos <- setNames(seq_along(axis_order), axis_order)
  hm$x <- pos[as.character(hm$token2)]; hm$y <- pos[as.character(hm$token1)]
  hm <- hm[hm$x <= hm$y, ]   # lower triangle incl. diagonal, as published
  bx <- excl[excl$single_class, ]
  bx$a <- pos[tolower(bx$token1)]; bx$b <- pos[tolower(bx$token2)]
  bx$x <- pmin(bx$a, bx$b); bx$y <- pmax(bx$a, bx$b)
  box_cols <- c("Maglemose" = "purple", "Kongemose" = "red", "Ertebølle" = "goldenrod",
                "Kongemose/Ertebølle" = "orange")
  hm_plot <- ggplot(hm, aes(x, y, fill = PMI)) + geom_tile(colour = "gray90") +
    scale_fill_gradient2(low = "white", mid = "white", high = "red", midpoint = 0.5) +
    geom_tile(data = bx, aes(x, y, colour = classes), fill = NA, linewidth = 0.6,
              inherit.aes = FALSE) +
    scale_colour_manual(values = box_cols, name = "single class") +
    scale_x_continuous(breaks = seq_along(axis_order), labels = toupper(axis_order),
                       expand = c(0, 0)) +
    scale_y_continuous(breaks = seq_along(axis_order), labels = toupper(axis_order),
                       expand = c(0, 0)) +
    coord_equal() + theme_minimal(base_size = 7) +
    theme(axis.text.x = element_text(angle = 90, vjust = 0.4)) +
    labs(x = NULL, y = NULL, title = "R1 aid: reproduced Fig. 4 matrix with single-class boxes")
  ggsave(file.path(aid_dir, "t06-fig4-box-aid.png"), hm_plot, width = 9, height = 9, dpi = 120)

  # Extended R1 aid (read-only lookup): the published boxes also surround
  # blank cells (co-occurrences with frequency <= 2, which the heatmap leaves
  # white), so the box criterion covers co-occurring pairs of any frequency.
  # For every pair of the 49 axis motifs that co-occur on at least one object:
  # the number of objects and their Chronology classes.
  ax_up <- toupper(axis_order)
  pairs <- do.call(rbind, lapply(seq_along(ax_up)[-1], function(b) {
    do.call(rbind, lapply(seq_len(b - 1), function(a) {
      has <- which(dat[[ax_up[a]]] == 1 & dat[[ax_up[b]]] == 1)
      if (!length(has)) return(NULL)
      cls <- sort(unique(chron[has]))
      data.frame(x_motif = ax_up[a], y_motif = ax_up[b], x = a, y = b, objects = length(has),
                 classes = paste(cls, collapse = "; "), single_class = length(cls) == 1)
    }))
  }))
  write.csv(pairs, file.path(out_dir, "t06-fig4-all-pairs-lookup.csv"), row.names = FALSE,
            fileEncoding = "UTF-8")
  cat("T06 extended aid: co-occurring pairs", nrow(pairs), "; single-class", sum(pairs$single_class),
      "; single-class with >= 2 objects", sum(pairs$single_class & pairs$objects >= 2), "\n")
  print(table(pairs$classes[pairs$single_class], pmin(pairs$objects[pairs$single_class], 3)))
  sb <- pairs[pairs$single_class, ]
  sb$freq_band <- factor(ifelse(sb$objects >= 3, ">= 3 objects", ifelse(sb$objects == 2,
                         "2 objects", "1 object")), levels = c("1 object", "2 objects", ">= 3 objects"))
  hm2 <- hm[hm$x < hm$y, ]
  hm_plot2 <- ggplot(hm2, aes(x, y, fill = PMI)) + geom_tile(colour = "gray92") +
    scale_fill_gradient2(low = "white", mid = "white", high = "red", midpoint = 0.5) +
    geom_tile(data = sb, aes(x, y, colour = classes, linetype = freq_band), fill = NA,
              linewidth = 0.7, width = 0.8, height = 0.8, inherit.aes = FALSE) +
    scale_colour_manual(values = box_cols, name = "single class") +
    scale_linetype_manual(values = c("1 object" = "dotted", "2 objects" = "dashed",
                                     ">= 3 objects" = "solid"), name = "objects") +
    scale_x_continuous(breaks = seq_along(axis_order), labels = ax_up, expand = c(0, 0),
                       position = "top") +
    scale_y_continuous(breaks = seq_along(axis_order), labels = ax_up, expand = c(0, 0)) +
    coord_equal() + theme_minimal(base_size = 8) +
    theme(axis.text.x = element_text(angle = 90, vjust = 0.4, hjust = 0)) +
    labs(x = NULL, y = NULL,
         title = "R1 aid: single-class co-occurrences of any frequency (published orientation)")
  ggsave(file.path(aid_dir, "t06-fig4-all-pairs-aid.png"), hm_plot2, width = 12, height = 12,
         dpi = 110)

  # Scored T06 comparison against the cell-by-cell transcription of the
  # published figure (published-values/fig4-cells.csv; method in
  # tools/read-published-fig4.py): every lower-triangle cell's box state, and
  # its centre colour against the fill the authors' heatmap object assigns.
  pub4 <- read.csv(file.path(pub_dir, "fig4-cells.csv"), stringsAsFactors = FALSE,
                   encoding = "UTF-8")
  pub4$box_class[is.na(pub4$box_class)] <- ""
  key4 <- paste(pub4$x_motif, pub4$y_motif)
  single_key <- paste(pairs$x_motif, pairs$y_motif)[pairs$single_class]
  single_cls <- pairs$classes[pairs$single_class]
  pub4$expected_box <- ifelse(key4 %in% single_key, single_cls[match(key4, single_key)], "")
  pub4$objects <- pairs$objects[match(key4, paste(pairs$x_motif, pairs$y_motif))]
  pub4$objects[is.na(pub4$objects)] <- 0L
  pub4$box_match <- pub4$box_class == pub4$expected_box
  # Expected fill: layer_data() of the authors' `heatmap` (documented ggplot2).
  hl <- layer_data(authors$heatmap, 1)
  hl_key <- paste(toupper(axis_order[as.integer(hl$x)]), toupper(axis_order[as.integer(hl$y)]))
  exp_fill <- hl$fill[match(key4, hl_key)]   # x = token2 (column), y = token1 (row)
  rgb_exp <- grDevices::col2rgb(exp_fill)
  pub4$expected_fill <- exp_fill
  pub4$PMI <- m[cbind(match(tolower(pub4$y_motif), rownames(m)),
                      match(tolower(pub4$x_motif), colnames(m)))]
  pub4$colour_distance <- sqrt((rgb_exp[1, ] - pub4$centre_r)^2 +
                                 (rgb_exp[2, ] - pub4$centre_g)^2 +
                                 (rgb_exp[3, ] - pub4$centre_b)^2)
  # Visibly coloured: green channel clearly below white, in both images.
  pub4$expected_coloured <- rgb_exp[2, ] < 230
  pub4$published_coloured <- pub4$centre_g < 230
  pub4$fill_match <- pub4$expected_coloured == pub4$published_coloured
  write.csv(pub4, file.path(out_dir, "t06-fig4-cells.csv"), row.names = FALSE,
            fileEncoding = "UTF-8")
  bad_box <- pub4[!pub4$box_match, ]
  cat("T06 scored: cells", nrow(pub4), "; box states matching", sum(pub4$box_match),
      "; published boxes", sum(pub4$box_class != ""), "; lookup single-class",
      sum(pub4$expected_box != ""), "\n")
  cat("T06 scored: fill coloured/uncoloured matching", sum(pub4$fill_match), "of", nrow(pub4),
      "; colour distance quantiles", round(quantile(pub4$colour_distance), 1), "\n")
  print(bad_box[, c("x_motif", "y_motif", "box_class", "expected_box", "objects")])
  print(pub4[!pub4$fill_match, c("x_motif", "y_motif", "PMI", "expected_fill", "centre_r",
                                 "centre_g", "centre_b", "colour_distance")])
  # The S1 objects behind each disagreeing box (read-only lookup).
  if (nrow(bad_box)) {
    objs <- do.call(rbind, lapply(seq_len(nrow(bad_box)), function(i) {
      h <- which(dat[[bad_box$x_motif[i]]] == 1 & dat[[bad_box$y_motif[i]]] == 1)
      data.frame(cell = paste(bad_box$x_motif[i], bad_box$y_motif[i]),
                 published_box = bad_box$box_class[i], No = dat[["No."]][h], Site = dat$Site[h],
                 Chronology = dat$Chronology[h], Region = dat$Region[h])
    }))
    write.csv(objs, file.path(out_dir, "t06-fig4-box-disagreements.csv"), row.names = FALSE,
              fileEncoding = "UTF-8")
    print(objs)
  }
  record("T06", 2 * nrow(pub4), sum(pub4$box_match) + sum(pub4$fill_match),
         sprintf("(cells %d: box states %d/%d, fill states %d/%d; axis order as published %s)",
                 nrow(pub4), sum(pub4$box_match), nrow(pub4), sum(pub4$fill_match), nrow(pub4),
                 identical(rownames(m), axis_order)))

  # ============================================================================
  # T07 — Figure 5 (map of the ten cluster objects). R1 aid: lookups and plot.
  # ============================================================================
  cluster <- c("C4", "C5", "C12", "C13", "D7")
  t7 <- do.call(rbind, lapply(t3_rows, function(no) {
    h <- which(as.character(dat[["No."]]) == as.character(no))
    data.frame(s1_no = no, site = dat$Site[h], lon = as.numeric(dat$Coord.Long[h]),
               lat = as.numeric(dat$Coord.Lat[h]),
               t(setNames(vapply(cluster, function(cm) dat[[cm]][h] == 1, logical(1)), cluster)),
               check.names = FALSE)
  }))
  t7$table3_row <- t3$row[match(t7$s1_no, as.integer(t3$s1_row_no))]
  t7 <- t7[order(t7$table3_row), ]
  write.csv(t7, file.path(out_dir, "t07-fig5-objects.csv"), row.names = FALSE, fileEncoding = "UTF-8")
  # Scored: pie membership (10 objects x 5 motifs) against the transcription,
  # and relative positions as pairwise orderings (east-west by longitude and
  # north-south by latitude) for pairs at least 0.15 degrees apart.
  pies <- read.csv(file.path(pub_dir, "fig5-pies.csv"))
  pies <- pies[match(t7$table3_row, pies$table3_row), ]
  memb <- do.call(rbind, lapply(cluster, function(cm)
    data.frame(table3_row = t7$table3_row, motif = cm, published = pies[[cm]],
               reproduced = t7[[cm]])))
  memb$match <- memb$published == memb$reproduced
  pairs7 <- do.call(rbind, combn(nrow(t7), 2, simplify = FALSE, FUN = function(ij) {
    i <- ij[1]; j <- ij[2]
    rbind(data.frame(a = t7$table3_row[i], b = t7$table3_row[j], axis = "east-west",
                     separation_deg = abs(t7$lon[i] - t7$lon[j]),
                     reproduced_a_first = t7$lon[i] < t7$lon[j],
                     published_a_first = pies$pie_x_px[i] < pies$pie_x_px[j]),
          data.frame(a = t7$table3_row[i], b = t7$table3_row[j], axis = "north-south",
                     separation_deg = abs(t7$lat[i] - t7$lat[j]),
                     reproduced_a_first = t7$lat[i] > t7$lat[j],
                     published_a_first = pies$pie_y_px[i] < pies$pie_y_px[j]))
  }))
  pairs7 <- pairs7[pairs7$separation_deg >= 0.15, ]
  pairs7$match <- pairs7$reproduced_a_first == pairs7$published_a_first
  write.csv(memb, file.path(out_dir, "t07-fig5-membership.csv"), row.names = FALSE)
  write.csv(pairs7, file.path(out_dir, "t07-fig5-relative-positions.csv"), row.names = FALSE)
  cat("T07: pie membership matching", sum(memb$match), "of", nrow(memb),
      "; pairwise orderings matching", sum(pairs7$match), "of", nrow(pairs7), "\n")
  record("T07", nrow(memb) + nrow(pairs7), sum(memb$match) + sum(pairs7$match),
         "(pie membership + pairwise relative positions; motif extents compared by eye)")
  motif_pts <- do.call(rbind, lapply(cluster, function(cm) {
    h <- which(dat[[cm]] == 1)
    data.frame(motif = cm, lon = as.numeric(dat$Coord.Long[h]), lat = as.numeric(dat$Coord.Lat[h]))
  }))
  write.csv(as.data.frame(table(motif = motif_pts$motif)), file.path(out_dir,
            "t07-fig5-motif-object-counts.csv"), row.names = FALSE)
  f5 <- ggplot(motif_pts, aes(lon, lat)) +
    geom_point(aes(colour = motif), size = 2, alpha = 0.7,
               position = position_jitter(width = 0.03, height = 0.03, seed = 1)) +
    geom_text(data = t7, aes(lon, lat, label = table3_row), nudge_y = 0.12, size = 4) +
    scale_colour_manual(values = c(C4 = "#E8174D", C5 = "#3DAA35", C12 = "#E6E61E",
                                   C13 = "#F58A2A", D7 = "#8A3FD1")) +
    coord_quickmap() + theme_bw() +
    labs(title = "R1 aid: S1 objects carrying each cluster motif; numbers = Table 3 rows")
  ggsave(file.path(aid_dir, "t07-fig5-aid.png"), f5, width = 8, height = 6, dpi = 120)

  # ============================================================================
  # T08 — S3 (2329 cells): authors' CSV exports vs deposited S3.xlsx
  # ============================================================================
  cmp_sheet <- function(sheet, csv, ntok) {
    s3 <- as.data.frame(read_excel("materials/Herskind&Riede_S3.xlsx", sheet = sheet, skip = 2,
                                   col_names = FALSE, .name_repair = "minimal"))
    rp <- as.data.frame(fread(file.path("authors-run", csv)))
    stopifnot(ncol(s3) == ncol(rp))
    names(s3) <- names(rp)
    key <- function(d) do.call(paste, d[, seq_len(ntok)])
    s3$key <- key(s3); rp$key <- key(rp)
    both <- intersect(s3$key, rp$key)
    cells <- do.call(rbind, lapply(names(rp)[names(rp) != "key"], function(col) {
      a <- s3[[col]][match(both, s3$key)]; b <- rp[[col]][match(both, rp$key)]
      if (is.numeric(a)) {
        rel <- abs(a - b) / pmax(abs(a), 1e-300)
        data.frame(sheet = sheet, key = both, column = col, s3 = format(a, digits = 17),
                   reproduced = format(b, digits = 17), abs_diff = abs(a - b),
                   match = rel <= 1e-12)
      } else {
        data.frame(sheet = sheet, key = both, column = col, s3 = a, reproduced = b,
                   abs_diff = NA_real_, match = a == b)
      }
    }))
    # Order: S3 is sorted by descending PMI; compare row order up to exact ties.
    # Same order up to exact ties: both sorted by descending PMI, and the PMI
    # at every row position agrees (rows may swap only within a tied PMI value).
    order_ok <- nrow(s3) == nrow(rp) && !is.unsorted(rev(s3$PMI)) &&
      !is.unsorted(rev(rp$PMI)) &&
      all(abs(s3$PMI - rp$PMI) <= 1e-12 * pmax(abs(s3$PMI), 1e-300))
    list(cells = cells, only_s3 = setdiff(s3$key, rp$key), only_rp = setdiff(rp$key, s3$key),
         rows = c(s3 = nrow(s3), reproduced = nrow(rp)),
         same_position = sum(s3$key == rp$key[seq_len(nrow(s3))]), order_ok = order_ok)
  }
  s3cmp <- list(bigrams = cmp_sheet("bigrams", "Bigrams.csv", 2),
                trigrams = cmp_sheet("trigrams", "Trigrams.csv", 3),
                quadrigrams = cmp_sheet("quadrigrams", "Quadrigrams.csv", 4))
  t8 <- do.call(rbind, lapply(s3cmp, `[[`, "cells"))
  write.csv(t8, file.path(out_dir, "t08-s3-cells.csv"), row.names = FALSE)
  t8_rows <- do.call(rbind, lapply(names(s3cmp), function(s) {
    x <- s3cmp[[s]]
    data.frame(sheet = s, rows_s3 = x$rows[["s3"]], rows_reproduced = x$rows[["reproduced"]],
               only_in_s3 = length(x$only_s3), only_in_reproduction = length(x$only_rp),
               rows_in_same_position = x$same_position,
               order_consistent_up_to_ties = x$order_ok)
  }))
  write.csv(t8_rows, file.path(out_dir, "t08-s3-rows.csv"), row.names = FALSE)
  print(t8_rows)
  record("T08", nrow(t8), sum(t8$match),
         sprintf("(max abs diff %.3g; element gate expects 2329)", max(t8$abs_diff, na.rm = TRUE)))

  # ============================================================================
  # T09-T20 — named values
  # ============================================================================
  add_nv <- function(target, element, published, reproduced, match, source) {
    acc$nv[[length(acc$nv) + 1]] <- data.frame(target_id = target, element = element,
                                        published = as.character(published),
                                        reproduced = as.character(reproduced),
                                        match = match, source = source)
  }
  # T09 — corpus size 483
  s1_raw <- read_excel("materials/Herskind&Riede_S1.xlsx", sheet = "Data")  # R1 aid
  n_no <- sum(!is.na(s1_raw[["No."]]))
  add_nv("T09", "objects in corpus (nrow of the authors' data)", 483, nrow(dat),
         nrow(dat) == 483, "authors' read_excel() object `data`")
  add_nv("T09", "cross-check: S1 rows with a non-empty No. (R1 aid)", 483, n_no, n_no == 483,
         "read-only S1 lookup")
  # T10 — maximum of 15 motifs on one object
  rs <- rowSums(as.data.frame(dat[, 31:289]), na.rm = TRUE)
  ntok_max <- max(ntoken(tokens(authors$corpus)))           # R1 aid: documented quanteda
  add_nv("T10", "max motifs on one object (row sums of S1 columns 31:289; R1 aid)", 15, max(rs),
         max(rs) == 15, "authors' `data`, columns used by S2.R Part 4")
  add_nv("T10", "cross-check: max S1 Total column", 15, max(as.numeric(dat$Total), na.rm = TRUE),
         max(as.numeric(dat$Total), na.rm = TRUE) == 15, "read-only S1 lookup")
  add_nv("T10", "cross-check: max tokens per document (quanteda::ntoken)", 15, ntok_max,
         ntok_max == 15, "authors' `corpus` object")
  # T11 — two bigrams at 44 (A1-C1, C1-G1)
  bf <- authors$bigramfreqs                                  # S2.R Part 4 colSums
  top <- sort(toupper(names(bf)[bf == max(bf)]))
  add_nv("T11", "top bigram frequency", 44, max(bf), max(bf) == 44, "Part 4 `bigramfreqs`")
  add_nv("T11", "bigrams at top frequency", "A1 C1;C1 G1", paste(top, collapse = ";"),
         identical(top, c("A1 C1", "C1 G1")), "Part 4 `bigramfreqs`")
  add_nv("T11", "cross-check: top frequency in full `bigrams` before Part 7", 44,
         max(bigrams_full$observed_freq), max(bigrams_full$observed_freq) == 44,
         "bigrams-before-part7.rds")
  # T12 — approximately 9% (R1 aid: inferred formula on reproduced inputs)
  pct <- 100 * max(bf) / nrow(dat)
  add_nv("T12", "share of objects carrying each top bigram (%)", "approximately 9",
         sprintf("%.2f", pct), pct >= 8.5 && pct < 9.5, "T11 frequency / T09 object count")
  # T13 — A1-G1 third, at 28
  f_a1g1 <- unname(bf["a1 g1"]); rank_a1g1 <- sum(bf > f_a1g1) + 1
  add_nv("T13", "frequency of A1 G1", 28, f_a1g1, f_a1g1 == 28, "Part 4 `bigramfreqs`")
  add_nv("T13", "rank of A1 G1 by descending frequency", 3, rank_a1g1, rank_a1g1 == 3,
         "Part 4 `bigramfreqs`")
  # T14-T18 — culture-specific bars in Fig. 3a and 3b (authors' plot data)
  classes_of <- function(p) {
    d <- p$data[p$data$Frequency > 0, ]
    tapply(d$Chronology, d$Skipgram, function(x) paste(sort(unique(x)), collapse = "; "))
  }
  cf <- classes_of(authors$bigramsBYfrequency)
  cp <- classes_of(authors$bigramsBYpmi)
  single_f <- cf[!grepl(";", cf)]
  add_nv("T14", "Fig. 3a bigrams confined to one Chronology class", 0, length(single_f),
         length(single_f) == 0, "plot data of `bigramsBYfrequency`")
  magle_only <- names(cp)[cp == "Maglemose"]
  konge_only <- names(cp)[cp == "Kongemose"]
  erte_only <- names(cp)[cp == "Ertebølle"]
  add_nv("T15", "Fig. 3b bigrams exclusive to Maglemose", 0, length(magle_only),
         length(magle_only) == 0, "plot data of `bigramsBYpmi`")
  add_nv("T16", "Fig. 3b bigrams specific to Kongemose (count)", 1, length(konge_only),
         length(konge_only) == 1, "plot data of `bigramsBYpmi`")
  add_nv("T16", "Fig. 3b bigrams specific to Kongemose (identity)", "B10 F38",
         paste(konge_only, collapse = ";"), identical(konge_only, "B10 F38"),
         "plot data of `bigramsBYpmi`")
  listed <- c("I5 I13", "C5 D7", "C4 C12", "C12 C13", "C4 C5", "I1 I13", "C5 C13", "I1 I5")
  add_nv("T17", "Fig. 3b bigrams unique to Ertebolle (count)", 9, length(erte_only),
         length(erte_only) == 9, "plot data of `bigramsBYpmi`")
  add_nv("T17", "the eight listed identities all present", paste(listed, collapse = ";"),
         paste(intersect(listed, erte_only), collapse = ";"), all(listed %in% erte_only),
         "plot data of `bigramsBYpmi`")
  add_nv("T17", "unlisted Ertebolle-only bigram(s) (record only)", "(not listed in text)",
         paste(setdiff(erte_only, listed), collapse = ";"), NA, "plot data of `bigramsBYpmi`")
  spec <- c(konge_only, erte_only, magle_only)
  tot_p <- tapply(authors$bigramsBYpmi$data$Frequency, authors$bigramsBYpmi$data$Skipgram, sum)
  add_nv("T18", "max co-occurrence frequency among culture-specific Fig. 3b bigrams", 5,
         max(tot_p[spec]), max(tot_p[spec]) == 5, "plot data of `bigramsBYpmi`")
  # T19 — antler axes and one antler shaft (R1 aid lookup on the T03 objects)
  ty <- vapply(t3_rows, function(no) {
    h <- which(as.character(dat[["No."]]) == as.character(no))
    paste(dat$Material[h], dat[["Artefact type"]][h])
  }, character(1))
  add_nv("T19", "cluster objects that are antler axes", 9, sum(ty == "antler axe"),
         sum(ty == "antler axe") == 9, "read-only S1 lookup (T03 objects)")
  add_nv("T19", "cluster objects that are antler shafts", 1, sum(ty == "antler shaft"),
         sum(ty == "antler shaft") == 1, "read-only S1 lookup (T03 objects)")
  # T20 — ten objects carry the cluster strings (inferred rule: >= 2 of the five)
  k <- rowSums(sapply(cluster, function(cm) as.numeric(dat[[cm]] == 1)), na.rm = TRUE)
  carriers <- as.character(dat[["No."]][k >= 2])
  add_nv("T20", "objects carrying >= 2 of C4, C5, C12, C13, D7 (inferred rule)", 10,
         length(carriers), length(carriers) == 10, "read-only S1 lookup")
  add_nv("T20", "cross-check: that set equals the ten Table 3 objects", "Table 3 rows",
         paste(sort(as.integer(carriers)), collapse = ";"),
         setequal(as.integer(carriers), t3_rows), "read-only S1 lookup")
  nv_df <- do.call(rbind, acc$nv)
  write.csv(nv_df, file.path(out_dir, "t09-t20-named-values.csv"), row.names = FALSE,
            fileEncoding = "UTF-8")
  print(nv_df[, c("target_id", "element", "published", "reproduced", "match")], right = FALSE)
  for (tid in sprintf("T%02d", 9:20)) {
    x <- nv_df[nv_df$target_id == tid & !is.na(nv_df$match), ]
    record(tid, nrow(x), sum(x$match))
  }

  # ============================================================================
  summary_df <- do.call(rbind, acc$summary_rows)
  write.csv(summary_df, file.path(out_dir, "summary.csv"), row.names = FALSE)
  print(summary_df, right = FALSE)
  cat("compare-results.R finished\n")
})
