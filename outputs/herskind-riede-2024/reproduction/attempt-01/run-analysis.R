#!/usr/bin/env Rscript
# Automated wrapper for Herskind & Riede 2024 analysis
#
# The original S2.R is designed for interactive (RStudio) execution with manual
# re-running for different n-gram levels and cultural period subsets. This wrapper
# automates the full pipeline for batch reproduction.
#
# Outputs:
#   - CSV tables: bigrams.csv, trigrams.csv, quadrigrams.csv (filtered obs_freq > 2)
#   - PMI heatmap: heatmapPMI.png
#   - Bar plots: freq_bigrams.png, pmi_bigrams.png (and tri/quadrigrams)
#   - Summary statistics: summary-stats.txt
#   - All period-specific PMI summary stats

library(quanteda)
library(readxl)
library(ggplot2)
library(dplyr)
library(data.table)
library(extrafont)

cat("=== Package versions ===\n")
cat("R:", paste(R.version$major, R.version$minor, sep="."), "\n")
cat("quanteda:", as.character(packageVersion("quanteda")), "\n")
cat("readxl:", as.character(packageVersion("readxl")), "\n")
cat("ggplot2:", as.character(packageVersion("ggplot2")), "\n")
cat("dplyr:", as.character(packageVersion("dplyr")), "\n")
cat("data.table:", as.character(packageVersion("data.table")), "\n")
cat("extrafont:", as.character(packageVersion("extrafont")), "\n")
cat("========================\n\n")

# Try to load Gill Sans MT; fall back to sans if unavailable
tryCatch({
  font_import(pattern = "GIL", prompt = FALSE)
  loadfonts(device = "pdf", quiet = TRUE)
  plot_font <- "Gill Sans MT"
  cat("Using font: Gill Sans MT\n")
}, error = function(e) {
  cat("Gill Sans MT not available, using default sans font\n")
})
# Check if font is actually available
available_fonts <- fonts()
if (!("Gill Sans MT" %in% available_fonts)) {
  plot_font <- "sans"
  cat("Font fallback: using 'sans'\n")
} else {
  plot_font <- "Gill Sans MT"
}

# Create output directory
dir.create("outputs", showWarnings = FALSE)

# ============================================================================
# Load data
# ============================================================================
data <- read_excel("S1.xlsx")
cat("Loaded", nrow(data), "objects from S1.xlsx\n")
cat("Chronology distribution:\n")
print(table(data$Chronology))
cat("\n")

# ============================================================================
# Core analysis function: generate skip-grams and calculate PMI
# ============================================================================
generate_skipgram_pmi <- function(input_data, n_value, k_values = 0:13, total_objects = NULL) {
  # Build corpus from motif text
  corp <- corpus(input_data$Motifs_as_text)
  toks <- tokens(corp)

  # Generate k-skip-n-grams
  ksngrams <- tokens_ngrams(toks, n = n_value, skip = k_values, concatenator = " ")
  dfm_ng <- dfm(ksngrams)
  freqs <- colSums(dfm_ng)

  cat(sprintf("  n=%d: %d unique k-skip-n-grams generated\n", n_value, length(freqs)))

  # Individual token frequencies
  dfm_toks <- dfm(toks)
  token_freqs <- colSums(dfm_toks)

  # Build data frame
  result <- data.frame(
    ksngrams = names(freqs),
    observed_freq = freqs,
    stringsAsFactors = FALSE
  )
  rownames(result) <- NULL

  # Split tokens
  split_tokens <- strsplit(result$ksngrams, " ")
  result$token1 <- sapply(split_tokens, `[`, 1)
  result$token2 <- sapply(split_tokens, `[`, 2)
  if (n_value >= 3) result$token3 <- sapply(split_tokens, `[`, 3)
  if (n_value >= 4) result$token4 <- sapply(split_tokens, `[`, 4)

  # Token frequencies
  all_tokens <- names(token_freqs)
  result$token1_freq <- token_freqs[match(result$token1, all_tokens)]
  result$token2_freq <- token_freqs[match(result$token2, all_tokens)]
  if (n_value >= 3) result$token3_freq <- token_freqs[match(result$token3, all_tokens)]
  if (n_value >= 4) result$token4_freq <- token_freqs[match(result$token4, all_tokens)]

  # Total objects (482 for full dataset — one object has empty motif string)
  if (is.null(total_objects)) {
    total_objects <- sum(nchar(trimws(input_data$Motifs_as_text)) > 0, na.rm = TRUE)
  }
  t_val <- total_objects

  # Expected frequency calculation
  if (n_value == 2) {
    result$expected_freq <- ((result$token1_freq / t_val) * (result$token2_freq / t_val)) * t_val
  } else if (n_value == 3) {
    result$expected_freq <- ((result$token1_freq / t_val) * (result$token2_freq / t_val) *
                              (result$token3_freq / t_val)) * t_val
  } else if (n_value == 4) {
    result$expected_freq <- ((result$token1_freq / t_val) * (result$token2_freq / t_val) *
                              (result$token3_freq / t_val) * (result$token4_freq / t_val)) * t_val
  }

  # PMI calculation: log(observed / expected)
  result$PMI <- log(result$observed_freq / result$expected_freq)

  return(result)
}

# ============================================================================
# Part 1 + 5: Run all n-gram levels and export tables
# ============================================================================
cat("\n=== Part 1: Generating skip-grams and PMI for full dataset ===\n")

# Run for n=2 (bigrams), using n=4 as main (as original script sets n <- 4 last)
ngram_labels <- c("bigrams", "trigrams", "quadrigrams")
ngram_results <- list()

for (n_val in 2:4) {
  cat(sprintf("\nProcessing %s (n=%d)...\n", ngram_labels[n_val - 1], n_val))
  result <- generate_skipgram_pmi(data, n_value = n_val)

  # Frequency distribution (for Table 1 equivalent)
  freq_count <- table(result$observed_freq)
  cat("  Frequency distribution of observed frequencies:\n")
  print(freq_count)

  # Store full result
  ngram_results[[ngram_labels[n_val - 1]]] <- result

  # Export filtered table (obs_freq > 2, sorted by PMI descending)
  export <- result
  export$ksngrams <- toupper(export$ksngrams)
  export$token1 <- toupper(export$token1)
  export$token2 <- toupper(export$token2)
  if (n_val >= 3) export$token3 <- toupper(export$token3)
  if (n_val >= 4) export$token4 <- toupper(export$token4)

  if (n_val == 2) {
    export <- export %>%
      select(token1, token2, token1_freq, token2_freq, observed_freq, expected_freq, PMI)
  } else if (n_val == 3) {
    export <- export %>%
      select(token1, token2, token3, token1_freq, token2_freq, token3_freq,
             observed_freq, expected_freq, PMI)
  } else if (n_val == 4) {
    export <- export %>%
      select(token1, token2, token3, token4, token1_freq, token2_freq, token3_freq,
             token4_freq, observed_freq, expected_freq, PMI)
  }

  export_dt <- as.data.table(export)
  export_dt <- subset(export_dt, observed_freq > 2)
  export_dt <- export_dt %>% arrange(desc(PMI))

  outfile <- paste0("outputs/", ngram_labels[n_val - 1], ".csv")
  fwrite(export_dt, outfile)
  cat(sprintf("  Exported %d rows to %s\n", nrow(export_dt), outfile))
}

# ============================================================================
# Part 2: Culture complex-specific subsets and PMI summary stats
# ============================================================================
cat("\n=== Part 2: Period-specific analyses ===\n")

# Use the quadrigram result as the "all" reference (matching original script flow)
# But for period comparison, the original matches on ksngrams from the full dataset
# The original script uses whatever n-gram level was last run
# We use bigrams (n=2) for the period analysis since that's what Table 2 focuses on
ksngram_freq_all <- ngram_results[["quadrigrams"]]

periods <- c("Maglemose", "Kongemose", "Ertebølle")
# Note: "Ertebølle" in original script uses the ø character
# Check what's actually in the data
cat("Checking chronology values in data:\n")
print(unique(data$Chronology))

period_results <- list()

sink("outputs/summary-stats.txt")
cat("=== PMI Summary Statistics ===\n\n")

for (period in periods) {
  # The original data uses "Ertebolle" (without ø) based on the xlsx
  period_match <- period
  period_data <- subset(data, Chronology == period_match)

  if (nrow(period_data) == 0) {
    # Try without special character
    period_alt <- gsub("ø", "o", period)
    period_data <- subset(data, Chronology == period_alt)
    if (nrow(period_data) > 0) {
      period_match <- period_alt
    }
  }

  cat(sprintf("\n%s: %d objects\n", period_match, nrow(period_data)))

  if (nrow(period_data) > 0) {
    # Generate skip-grams for this period (using n=4 to match original)
    period_sg <- generate_skipgram_pmi(period_data, n_value = 4)

    # Match with overall stats
    period_stats <- ksngram_freq_all[match(period_sg$ksngrams, ksngram_freq_all$ksngrams,
                                           nomatch = 0), ]
    period_subset <- period_stats[period_stats$observed_freq > 2, ]

    cat(sprintf("  Matched skip-grams with obs_freq > 2: %d\n", nrow(period_subset)))

    # PMI summary
    cat(sprintf("  PMI summary for %s (obs_freq > 2):\n", period_match))
    print(summary(period_subset$PMI))

    period_results[[period_match]] <- period_subset
  }
}

# Overall PMI summary (obs_freq > 2)
ksngram_freq_subset_all <- subset(ksngram_freq_all, observed_freq > 2)
cat("\nOverall PMI summary (obs_freq > 2):\n")
print(summary(ksngram_freq_subset_all$PMI))

sink()
cat("Summary stats written to outputs/summary-stats.txt\n")

# Also print to stdout
cat(readLines("outputs/summary-stats.txt"), sep = "\n")

# ============================================================================
# Part 3: Bar plots (using bigram data as primary, matching paper figures)
# ============================================================================
cat("\n=== Part 3: Generating bar plots ===\n")

# Use the quadrigram result for the main analysis (as the original script ends with n=4)
# But the bar plots in the paper show bigram-level data
# The original script plots whatever n-gram level is currently loaded
# We generate plots for all levels

for (n_idx in 1:3) {
  n_label <- ngram_labels[n_idx]
  ksngram_freq <- ngram_results[[n_label]]

  # Frequency-sorted subset (obs_freq > 9)
  ksngram_freq_sub <- subset(ksngram_freq, observed_freq > 9)
  if (nrow(ksngram_freq_sub) == 0) {
    cat(sprintf("  No %s with observed_freq > 9, skipping bar plots\n", n_label))
    next
  }
  ksngram_freq_sub <- ksngram_freq_sub %>% arrange(desc(observed_freq))

  # PMI-sorted subset (obs_freq > 2, top N matching frequency count)
  ksngram_PMI <- ksngram_freq %>% arrange(desc(PMI))
  ksngram_PMI <- subset(ksngram_PMI, observed_freq > 2)
  n_top <- nrow(ksngram_freq_sub)
  ksngram_PMI_top <- head(ksngram_PMI, n_top)

  # Uppercase for matching with motif columns
  ksngram_freq_sub$ksngrams <- toupper(ksngram_freq_sub$ksngrams)
  ksngram_PMI_top$ksngrams <- toupper(ksngram_PMI_top$ksngrams)

  # Create chronology-attributed frequency table
  chrongrams <- data[, c(11, 31:289)]

  createResultTable <- function(sg_data) {
    result_tables <- list()
    skipgrams <- unique(sg_data$ksngrams)

    for (skipgram in skipgrams) {
      tokens_split <- strsplit(skipgram, " ")[[1]]
      filter_condition <- paste(tokens_split, "== 1", collapse = " & ")
      tryCatch({
        filtered_data <- chrongrams %>% filter(eval(parse(text = filter_condition)))
        result_table <- table(filtered_data$Chronology)
        result_tables[[skipgram]] <- data.frame(
          Skipgram = skipgram,
          Chronology = names(result_table),
          Frequency = as.numeric(result_table)
        )
      }, error = function(e) {
        cat(sprintf("  Warning: could not filter for '%s': %s\n", skipgram, e$message))
      })
    }

    final_result <- do.call(rbind, result_tables)
    return(final_result)
  }

  skipgramsFreq <- createResultTable(ksngram_freq_sub)
  skipgramsPMI <- createResultTable(ksngram_PMI_top)

  if (is.null(skipgramsFreq) || nrow(skipgramsFreq) == 0) {
    cat(sprintf("  No chronology-attributed data for %s, skipping\n", n_label))
    next
  }

  # Add PMI values
  ksngram_freq_uc <- ksngram_freq
  ksngram_freq_uc$ksngrams <- toupper(ksngram_freq_uc$ksngrams)

  skipgramsFreq$PMI <- ksngram_freq_uc$PMI[match(skipgramsFreq$Skipgram, ksngram_freq_uc$ksngrams)]
  skipgramsPMI$PMI <- ksngram_freq_uc$PMI[match(skipgramsPMI$Skipgram, ksngram_freq_uc$ksngrams)]

  # Frequency-sorted plot
  skipgram_order <- unique(ksngram_freq_sub$ksngrams)
  summary_freq <- skipgramsFreq %>% distinct(Skipgram, .keep_all = TRUE)

  p_freq <- ggplot(skipgramsFreq, aes(x = Frequency, fill = Chronology,
                                       y = reorder(Skipgram, desc(match(Skipgram, skipgram_order))))) +
    geom_col(position = "stack") +
    geom_text(data = summary_freq, aes(label = sprintf("%.4f", PMI)),
              position = position_stack(vjust = 0), color = "black", size = 3) +
    scale_fill_manual(values = c("#FAD02E", "#D98888", "#E8BB8B", "#B4A1C1")) +
    xlab("Frequency") +
    ylab("Co-occurrence") +
    theme(plot.title = element_text(size = 13, face = "bold", hjust = 0.5),
          legend.text = element_text(size = 10),
          legend.title = element_blank(),
          legend.position = c(0.85, 0.15),
          legend.background = element_rect(fill = "transparent"),
          axis.text.x = element_text(vjust = 0.4, hjust = 1),
          text = element_text(size = 14, family = plot_font)) +
    ggtitle(paste("Most frequent", n_label))

  ggsave(paste0("outputs/freq_", n_label, ".png"), plot = p_freq,
         width = 10, height = 8, units = "in", dpi = 300)
  cat(sprintf("  Saved outputs/freq_%s.png\n", n_label))

  # PMI-sorted plot
  if (!is.null(skipgramsPMI) && nrow(skipgramsPMI) > 0) {
    skipgram_order_pmi <- unique(skipgramsPMI$Skipgram)
    summary_pmi <- skipgramsPMI %>% distinct(Skipgram, .keep_all = TRUE)

    p_pmi <- ggplot(skipgramsPMI, aes(x = Frequency, fill = Chronology,
                                       y = reorder(Skipgram, PMI))) +
      geom_col(position = "stack") +
      geom_text(data = summary_pmi, aes(label = sprintf("%.4f", PMI)),
                position = position_stack(vjust = 0), color = "black", size = 3) +
      scale_fill_manual(values = c("#FAD02E", "#D98888", "#E8BB8B", "#B4A1C1")) +
      xlab("Frequency") +
      ylab("Co-occurrence") +
      theme(plot.title = element_text(size = 13, face = "bold", hjust = 0.5),
            axis.text.x = element_text(vjust = 1, hjust = 0.5),
            text = element_text(size = 14, family = plot_font)) +
      ggtitle(paste(n_label, "by highest PMI value")) +
      guides(fill = "none")

    ggsave(paste0("outputs/pmi_", n_label, ".png"), plot = p_pmi,
           width = 10, height = 8, units = "in", dpi = 300)
    cat(sprintf("  Saved outputs/pmi_%s.png\n", n_label))
  }
}

# ============================================================================
# Part 4: Heatmap (bigram PMI matrix)
# ============================================================================
cat("\n=== Part 4: Generating PMI heatmap ===\n")

# Use bigram data for heatmap
ksngram_freq_hm <- ngram_results[["bigrams"]]

# Subset to obs_freq > 2
ksngram_freq_hm <- subset(ksngram_freq_hm, observed_freq > 2)

# Get unique tokens
tokens_hm <- unique(c(as.character(ksngram_freq_hm$token1),
                       as.character(ksngram_freq_hm$token2)))

# Create symmetric PMI matrix
m <- matrix(0, nrow = length(tokens_hm), ncol = length(tokens_hm),
            dimnames = list(tokens_hm, tokens_hm))

for (i in 1:nrow(ksngram_freq_hm)) {
  row_idx <- match(ksngram_freq_hm[i, "token1"], tokens_hm)
  col_idx <- match(ksngram_freq_hm[i, "token2"], tokens_hm)
  m[row_idx, col_idx] <- ksngram_freq_hm[i, "PMI"]
  m[col_idx, row_idx] <- ksngram_freq_hm[i, "PMI"]
}

# Chronological ordering from original script
chrono_order <- c("a14","b3","a24","b10","b2","b12","e4","a5","d5","b13","b4","b1",
                  "a1","a3","ant","f12","e1","b6","e5","f5","f13","f38","d29","b8",
                  "d33","h1","g2","c1","f14","i1","f35","zoo","d19","g1","d3","d15",
                  "f15","c12","c14","c5","c13","c4","c6","d7","f55","g7","i13","i5",
                  "relief")

# Only keep tokens that exist in our matrix
chrono_order_avail <- chrono_order[chrono_order %in% colnames(m)]
cat(sprintf("  %d of %d tokens in chronological order present in matrix\n",
            length(chrono_order_avail), length(chrono_order)))

m_ordered <- m[chrono_order_avail, chrono_order_avail]

# Convert to data frame for ggplot
df_hm <- as.data.frame.table(m_ordered)
names(df_hm) <- c("token1", "token2", "PMI")

# Plot heatmap
heatmap <- ggplot(df_hm, aes(x = token2, y = token1, fill = PMI)) +
  geom_tile(color = "gray90") +
  scale_fill_gradient2(low = "white", mid = "white", high = "red",
                       midpoint = 0.5, name = "PMI") +
  labs(x = "Token 2", y = "Token 1", title = "Co-occurrence matrix") +
  theme(axis.text.x = element_text(angle = 90, hjust = 1, vjust = 0.4),
        plot.title = element_text(size = 14, face = "bold", hjust = 0.5),
        text = element_text(family = plot_font, size = 12),
        legend.text = element_text(size = 10)) +
  scale_x_discrete(limits = chrono_order_avail, labels = toupper,
                   name = NULL, drop = FALSE) +
  scale_y_discrete(limits = chrono_order_avail, labels = toupper,
                   name = NULL, drop = FALSE) +
  ggtitle("Motif co-occurrence heatmap by PMI")

ggsave("outputs/heatmapPMI.png", plot = heatmap, width = 8, height = 8,
       units = "in", dpi = 300)
cat("  Saved outputs/heatmapPMI.png\n")

# Also export the PMI matrix as CSV for verification
write.csv(m_ordered, "outputs/pmi-matrix.csv")
cat("  Saved outputs/pmi-matrix.csv\n")

cat("\n=== Analysis complete ===\n")
cat("Output files in outputs/:\n")
cat(paste(" ", list.files("outputs"), collapse = "\n"), "\n")
