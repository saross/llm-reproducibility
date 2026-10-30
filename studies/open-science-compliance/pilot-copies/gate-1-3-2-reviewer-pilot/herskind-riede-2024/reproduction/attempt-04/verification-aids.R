# =============================================================================
# verification-aids.R -- LABELLED VERIFICATION AIDS (registrant ruling R1)
# herskind-riede-2024, reproduction attempt 04
#
# These aids test published results that no authors' code produces. Each is
# either a read-only lookup in the deposited data (deposit/Herskind&Riede_S1
# .xlsx, Zenodo record 10801706) or a call to a documented function of a
# package the authors used (quanteda, readxl, ggplot2), applied to the
# authors' own objects saved by run-analysis.R. They make no new statistical
# choice, and they are never part of the authors' code. Every output file
# is prefixed "aid-" and names the target it serves.
#
#   aid-T09  object count: S1 rows with an object number; ndoc() of the
#            authors' corpus
#   aid-T10  maximum motifs per object: max(quanteda::ntoken()) over the
#            authors' tokens; the authors' k
#   aid-T13  unigram frequencies: colSums(dfm(tokens(corpus))) -- the
#            documented quanteda calls ngramfunction() makes internally --
#            on the authors' corpus, and the authors' own `freqs` (Part 4)
#   aid-T14  chronology of the objects bearing each Fig. 3b bigram (S1)
#   aid-T16  chronology of the objects bearing each pair of the five
#            cluster motifs (S1), with the authors' PMI where plotted
#   aid-T17  objects bearing at least two of the five cluster motifs (S1)
#   aid-T07  Table 3 rows looked up in S1 by Plonka figure number
#   aid-T03  chronology of the objects bearing every pair of the 49 Fig. 4
#            axis motifs (S1), to test the culture-exclusive boxes
#   aid-T01  map panel: ggplot2 point plot of S1 coordinates by Chronology
#   aid-T04  Fig. 5 objects: S1 coordinates and cluster-motif presence,
#            plotted with ggplot2
# =============================================================================

local({
  root <- getwd()
  out <- file.path(root, "captured")
  s1 <- readxl::read_excel(file.path(root, "deposit", "Herskind&Riede_S1.xlsx"),
                           sheet = "Data")
  s1 <- s1[!is.na(s1[["No."]]), ]
  motif_cols <- names(s1)[31:289]              # A1 ... ZOO, as S2.R indexes them
  authors <- readRDS(file.path(out, "authors-objects.rds"))
  write_aid <- function(df, name) {
    write.csv(df, file.path(out, paste0("aid-", name, ".csv")), row.names = FALSE)
  }
  # Read-only lookup: S1 rows bearing every motif in `motifs` (presence = 1).
  bearing <- function(motifs) {
    keep <- rep(TRUE, nrow(s1))
    for (mo in motifs) keep <- keep & !is.na(s1[[mo]]) & s1[[mo]] == 1
    s1[keep, ]
  }
  chron_levels <- c("Maglemose", "Kongemose", "Kongemose/Ertebølle", "Ertebølle")
  chron_summary <- function(rows) {
    tab <- table(factor(rows$Chronology, levels = chron_levels), useNA = "ifany")
    present <- names(tab)[tab > 0]
    data.frame(n_objects = nrow(rows),
               maglemose = as.integer(tab["Maglemose"]),
               kongemose = as.integer(tab["Kongemose"]),
               kongemose_ertebolle = as.integer(tab["Kongemose/Ertebølle"]),
               ertebolle = as.integer(tab["Ertebølle"]),
               other_or_na = nrow(rows) - sum(tab[chron_levels]),
               exclusive_to = if (nrow(rows) > 0 && length(present) == 1 &&
                                  nrow(rows) == sum(tab[chron_levels])) present else "",
               stringsAsFactors = FALSE)
  }

  # aid-T09
  write_aid(data.frame(
    item = c("S1 Data rows with an object number", "ndoc(authors' corpus)",
             "nrow(authors' data)", "authors' t"),
    value = c(nrow(s1), quanteda::ndoc(authors$corpus), authors$data_nrow, authors$t)),
    "T09-object-count")

  # aid-T10
  nt <- quanteda::ntoken(authors$toks)
  write_aid(data.frame(
    item = c("max ntoken over the authors' tokens", "documents with that maximum",
             "authors' k (min)", "authors' k (max)"),
    value = c(max(nt), sum(nt == max(nt)), min(authors$k), max(authors$k))),
    "T10-max-motifs")

  # aid-T13
  # Matrix::colSums is the method an attached quanteda session dispatches to
  # for a dfm (base colSums cannot dispatch on it without quanteda attached).
  tf <- Matrix::colSums(quanteda::dfm(quanteda::tokens(authors$corpus)))
  tf <- sort(tf, decreasing = TRUE)
  fr <- sort(authors$freqs, decreasing = TRUE)
  write_aid(data.frame(rank = seq_len(10), token_freqs_motif = toupper(names(tf)[1:10]),
                       token_freqs = as.integer(tf[1:10]),
                       authors_freqs_motif = names(fr)[1:10],
                       authors_freqs = as.integer(fr[1:10])), "T13-unigram-top")

  # aid-T14 (also serves T15): S1 chronology of objects bearing each Fig. 3b bigram.
  fig3b <- unique(as.character(authors$fig3b_data$Skipgram))
  t14 <- do.call(rbind, lapply(fig3b, function(sg) {
    cbind(data.frame(bigram = sg, stringsAsFactors = FALSE),
          chron_summary(bearing(strsplit(sg, " ")[[1]])))
  }))
  write_aid(t14, "T14-fig3b-chronology")

  # aid-T16: pairs among the five cluster motifs.
  cluster <- c("C4", "C5", "C12", "C13", "D7")
  pairs <- t(utils::combn(cluster, 2))
  bf <- authors$bigrams_final                     # observed_freq > 2, as Fig. 4
  t16 <- do.call(rbind, lapply(seq_len(nrow(pairs)), function(i) {
    a <- pairs[i, 1]; b <- pairs[i, 2]
    hit <- which((toupper(bf$token1) == a & toupper(bf$token2) == b) |
                 (toupper(bf$token1) == b & toupper(bf$token2) == a))
    cbind(data.frame(pair = paste(a, b), authors_observed_freq =
                       if (length(hit)) bf$observed_freq[hit[1]] else NA,
                     authors_pmi = if (length(hit)) sprintf("%.15g", bf$PMI[hit[1]]) else NA,
                     stringsAsFactors = FALSE),
          chron_summary(bearing(c(a, b))))
  }))
  write_aid(t16, "T16-cluster-pairs")
  write_aid(cbind(data.frame(motif = cluster), do.call(rbind, lapply(cluster, function(mo) {
    chron_summary(bearing(mo))
  }))), "T16-cluster-motifs")

  # aid-T17: objects bearing at least two of the five cluster motifs.
  n_cluster <- rowSums(sapply(cluster, function(mo) !is.na(s1[[mo]]) & s1[[mo]] == 1))
  motif_list <- function(rows) {
    apply(as.data.frame(rows[, motif_cols]), 1, function(r) {
      paste(motif_cols[!is.na(r) & r == 1], collapse = " ")
    })
  }
  t17 <- s1[n_cluster >= 2, ]
  write_aid(data.frame(no = t17[["No."]], site = t17$Site, region = t17$Region,
                       artefact_type = t17[["Artefact type"]], material = t17$Material,
                       figure = t17$Figure, chronology = t17$Chronology,
                       n_cluster_motifs = n_cluster[n_cluster >= 2],
                       cluster_motifs = apply(sapply(cluster, function(mo) {
                         ifelse(!is.na(t17[[mo]]) & t17[[mo]] == 1, mo, "")
                       }), 1, function(x) paste(x[nzchar(x)], collapse = " ")),
                       motifs = motif_list(t17), lon = t17$Coord.Long, lat = t17$Coord.Lat,
                       stringsAsFactors = FALSE), "T17-cluster-objects")

  # aid-T07 (also T18, T04): Table 3 rows by Plonka figure number (lookup keys
  # transcribed from Table 3).
  table3_figures <- c("145", "136:5", "159", "150:2", "153", "134", "148", "165",
                      "192:1", "161")
  t07 <- do.call(rbind, lapply(seq_along(table3_figures), function(i) {
    rows <- s1[as.character(s1$Figure) == table3_figures[i], ]
    if (!nrow(rows)) {
      return(data.frame(table3_number = i, figure = table3_figures[i], matches = 0L,
                        no = NA, site = NA, region = NA, artefact_type = NA,
                        material = NA, chronology = NA, motifs = NA, lon = NA, lat = NA))
    }
    data.frame(table3_number = i, figure = table3_figures[i], matches = nrow(rows),
               no = rows[["No."]], site = rows$Site, region = rows$Region,
               artefact_type = rows[["Artefact type"]], material = rows$Material,
               chronology = rows$Chronology, motifs = motif_list(rows),
               lon = rows$Coord.Long, lat = rows$Coord.Lat, stringsAsFactors = FALSE)
  }))
  write_aid(t07, "T07-table3-lookup")

  # aid-T03: every pair of the 49 Fig. 4 axis motifs (the authors' matrix
  # order), with the chronology of the objects bearing both.
  axis <- toupper(rownames(read.csv(file.path(out, "fig4-matrix-m.csv"), row.names = 1,
                                    check.names = FALSE)))
  axis_pairs <- t(utils::combn(axis, 2))
  t03 <- do.call(rbind, lapply(seq_len(nrow(axis_pairs)), function(i) {
    cbind(data.frame(x_token = axis_pairs[i, 1], y_token = axis_pairs[i, 2],
                     stringsAsFactors = FALSE),
          chron_summary(bearing(axis_pairs[i, ])))
  }))
  write_aid(t03, "T03-axis-pair-chronology")

  # aid-T01: map panel (point plot of S1 coordinates by Chronology; the
  # authors' fill colours, no basemap). S1 records an unknown location as
  # "-", so readxl reads the coordinate columns as text: the aid reads them
  # as numbers, with "-" as missing, and counts the objects it cannot place.
  s1_map <- data.frame(lon = suppressWarnings(as.numeric(s1$Coord.Long)),
                       lat = suppressWarnings(as.numeric(s1$Coord.Lat)),
                       Chronology = s1$Chronology, stringsAsFactors = FALSE)
  unplaced <- is.na(s1_map$lon) | is.na(s1_map$lat)
  write_aid(as.data.frame(table(Chronology = s1_map$Chronology[unplaced], useNA = "ifany")),
            "T01-map-unplaced-by-chronology")
  s1_map <- s1_map[!unplaced, ]
  map <- ggplot2::ggplot(s1_map, ggplot2::aes(x = lon, y = lat, colour = Chronology)) +
    ggplot2::geom_point(size = 1.6, alpha = 0.85) +
    ggplot2::scale_colour_manual(values = c("Ertebølle" = "#FAD02E", "Kongemose" = "#D98888",
                                            "Kongemose/Ertebølle" = "#E8BB8B",
                                            "Maglemose" = "#B4A1C1")) +
    ggplot2::coord_quickmap() +
    ggplot2::labs(title = "aid-T01: S1 coordinates by Chronology (verification aid)")
  ggplot2::ggsave(file.path(out, "aid-T01-map.png"), map, width = 7, height = 6, dpi = 150)
  write_aid(as.data.frame(table(Chronology = s1$Chronology, useNA = "ifany")),
            "T01-map-chronology-counts")
  write_aid(data.frame(
    item = c("lon_min", "lon_max", "lat_min", "lat_max", "objects_placed",
             "objects_without_coordinates"),
    value = c(range(s1_map$lon), range(s1_map$lat), nrow(s1_map), sum(unplaced))),
    "T01-map-extent")

  # aid-T04: the Table 3 objects with their cluster motifs, plotted.
  t04 <- t07[!is.na(t07$no), c("table3_number", "site", "lon", "lat")]
  t04$lon <- suppressWarnings(as.numeric(t04$lon))
  t04$lat <- suppressWarnings(as.numeric(t04$lat))
  t04$cluster_motifs <- sapply(seq_len(nrow(t04)), function(i) {
    row <- s1[s1[["No."]] == t07$no[!is.na(t07$no)][i], ]
    paste(cluster[sapply(cluster, function(mo) !is.na(row[[mo]]) && row[[mo]] == 1)],
          collapse = " ")
  })
  write_aid(t04, "T04-fig5-objects")
  p5 <- ggplot2::ggplot(t04, ggplot2::aes(x = lon, y = lat)) +
    ggplot2::geom_point(size = 3) +
    ggplot2::geom_text(ggplot2::aes(label = paste0(table3_number, ": ", cluster_motifs)),
                       hjust = -0.1, size = 3) +
    ggplot2::coord_quickmap() +
    ggplot2::labs(title = "aid-T04: Table 3 objects and their cluster motifs (verification aid)")
  ggplot2::ggsave(file.path(out, "aid-T04-fig5-objects.png"), p5, width = 7, height = 6,
                  dpi = 150)
  message("verification-aids.R: finished")
})
