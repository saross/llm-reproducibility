#!/usr/bin/env Rscript
# ===========================================================================
# Wrapper script for Key et al. 2024 OLE reproduction
# Paper: "Identifying accurate artefact morphological ranges using optimal
#         linear estimation: Method validation, case studies, and code"
# Journal of Archaeological Science 162, 105921
# DOI: 10.1016/j.jas.2024.105921
#
# Reproduces:
#   - Table 5 (Olduvai Bed IV Cleavers rows only, n=134)
#   - Table 6 (Paleoindian Projectile Points, all 4 types)
#
# Cannot reproduce:
#   - Table 7 (Geometric microliths) — full morphometric data not publicly
#     available. GitHub repos contain classification data but not the
#     Length/Breadth/Thickness/Area measurements Key et al. used.
#   - Table 5 (all other rows) — data held by co-authors, not deposited
#   - Tables 2-4 (validation) — replica data not published
#
# This wrapper makes NO algorithmic modifications. The OLE.test function
# is copied verbatim from mmc1 (Main OLE script). The wrapper only:
#   - Substitutes file paths for the placeholder "###file location###"
#   - Parameterises repeated operations (type loop for Paleoindian)
#   - Adds output capture (write.csv, sink)
# ===========================================================================

cat("=== Key et al. 2024 OLE Reproduction ===\n")
cat("Date:", format(Sys.time(), "%Y-%m-%d %H:%M:%S %Z"), "\n")
cat("R version:", R.version.string, "\n\n")

# Create output directory
dir.create("outputs", showWarnings = FALSE, recursive = TRUE)

# Start console log capture
sink("outputs/run.log", split = TRUE)

# ===========================================================================
# OLE function — verbatim from mmc1 (Main script), lines 26-45
# No modifications whatsoever to the analytical logic
# ===========================================================================
OLE.test <-
  function(dd, alpha){
    # records are sorted in a reverse order, as required by OLE method
    sights <- rev(sort(dd))
    # calculation of k, v, e, lambda and other values
    k <- length(sights)
    v <- (1/(k-1)) * sum(log((sights[1] - sights[k])/(sights[1] - sights[2:(k-1)])))
    e <- matrix(rep(1,k), ncol=1)
    SU<-(-log(alpha)/length(sights))^-v
    myfun <- function(i,j,v){(gamma(2*v+i)*gamma(v+j))/(gamma(v+i)*gamma(j))}
    lambda <- outer(1:k, 1:k, myfun, v=v)
    lambda <- ifelse(lower.tri(lambda), lambda, t(lambda))
    a <- as.vector(solve(t(e)%*%solve(lambda)%*%e)) * solve(lambda)%*%e
    # calculation of CI ("upperCI") and extinction time ("extest")
    upperCI<-max(sights) + ((max(sights)-min(sights))/(SU-1))
    extest<-sum(t(a)%*%sights)
    # return of results produced by the function
    res<-data.frame(Estimate=extest, upperCI=upperCI)
    return(res)
  }

# ===========================================================================
# Helper: run OLE on a single numeric vector
# Returns both TE (point estimate) and CI (confidence interval) values
# Uses the same logic as mmc1 lines 48-61
# ===========================================================================
run_ole <- function(values, alpha = 0.05, k.size = 10) {
  data.i <- sort(values)
  n <- length(data.i)
  obs_min <- min(data.i)
  obs_max <- max(data.i)
  n_unique <- length(unique(data.i))
  n_dups <- n - n_unique

  # Top-k and bottom-k values (same as mmc1 lines 51-53)
  # NOTE: No deduplication applied here — matching mmc1 exactly.
  # The mmc1 instructions state "Duplicates should be avoided" but the
  # script does not enforce this. If the k-window contains duplicates,
  # OLE.test will produce NaN (division by zero in log). This indicates
  # the authors pre-processed data to jitter or remove duplicates
  # before running mmc1, but this step is not documented.
  max.range.data <- rev(sort(data.i))
  max.range.data <- max.range.data[1:k.size]
  min.range.data <- sort(data.i)
  min.range.data <- min.range.data[1:k.size]

  # Transform to distances from boundary of k-window (same as mmc1)
  min.range.data.b <- max(min.range.data) - min.range.data
  max.range.data.b <- max.range.data - min(max.range.data)

  # Apply OLE (same as mmc1 lines 56-57)
  OLE.min <- max(min.range.data) - OLE.test(min.range.data.b, alpha)
  OLE.max <- min(max.range.data) + OLE.test(max.range.data.b, alpha)

  # Extract results: [[1]] = Estimate (TE), [[2]] = upperCI (CI)
  min_te <- OLE.min[[1]]
  min_ci <- OLE.min[[2]]
  max_te <- OLE.max[[1]]
  max_ci <- OLE.max[[2]]

  # OLE Range Extension %
  # Formula: ((OLE range / original range) - 1) * 100
  # Using CI values (which extend further than TE values)
  orig_range <- obs_max - obs_min
  ole_range_ci <- max_ci - min_ci
  ole_range_te <- max_te - min_te
  range_ext_ci <- ((ole_range_ci / orig_range) - 1) * 100
  range_ext_te <- ((ole_range_te / orig_range) - 1) * 100

  data.frame(
    N = n,
    N_unique = n_unique,
    N_duplicates = n_dups,
    Mean = round(mean(values), 1),
    Minimum = obs_min,
    Maximum = obs_max,
    Min_TE = round(min_te, 1),
    Min_CI = round(min_ci, 1),
    Max_TE = round(max_te, 1),
    Max_CI = round(max_ci, 1),
    Range_Ext_CI_Pct = round(range_ext_ci, 1),
    Range_Ext_TE_Pct = round(range_ext_te, 1)
  )
}


# ===========================================================================
# TABLE 5: Olduvai Bed IV Cleavers (n = 134)
# Data source: Martin-Ramos (2022/2023) PhD thesis, UCL Discovery
# Access level: 0 (direct download)
# Analysis type: deterministic (mmc1 Main script)
# ===========================================================================
cat("\n")
cat("============================================================\n")
cat("TABLE 5: Olduvai Bed IV Cleavers (n = 134)\n")
cat("============================================================\n\n")

olduvai <- read.csv("data/olduvai-cleavers-key-et-al-2024.csv")
cat("Loaded Olduvai data:", nrow(olduvai), "records,",
    ncol(olduvai), "columns\n")
cat("Columns:", paste(names(olduvai), collapse = ", "), "\n\n")

# Variables to analyse (matching Table 5 column order)
table5_vars <- list(
  Length     = olduvai$length_mm,
  Breadth    = olduvai$breadth_mm,
  Thickness  = olduvai$thickness_mm,
  EdgeLength = olduvai$edge_length_mm,
  Mass       = olduvai$mass_g
)

# Run OLE on each variable
table5_results <- do.call(rbind, lapply(names(table5_vars), function(var_name) {
  vals <- table5_vars[[var_name]]
  vals <- vals[!is.na(vals)]
  result <- run_ole(vals)
  result$Variable <- var_name
  result
}))

# Reorder columns for readability
table5_results <- table5_results[, c("Variable", "N", "Mean", "Minimum",
                                      "Min_TE", "Min_CI", "Maximum",
                                      "Max_TE", "Max_CI",
                                      "Range_Ext_CI_Pct", "Range_Ext_TE_Pct")]

cat("Results:\n")
print(table5_results, row.names = FALSE)
write.csv(table5_results, "outputs/table-5-olduvai-results.csv",
          row.names = FALSE)

# Published values for comparison (from Table 5 in paper)
cat("\nPublished Table 5 values (Olduvai rows) for comparison:\n")
cat("Variable      Mean   Min  OLE_Min  Max   OLE_Max  Ext%\n")
cat("Length        142.9    93   84.0    205   216.3    27.5\n")
cat("Breadth        87.6    57   49.5    119   126.8    24.7\n")
cat("Thickness      42.3    22   19.5     60    60.9     8.9\n")
cat("Edge Length   259.7    20  -10.6    481   501.2    11.0\n")
cat("Mass          588.3   252  224.6   1269  1557.8    31.1\n")


# ===========================================================================
# TABLE 6: Paleoindian Projectile Points (4 types)
# Data source: Buchanan & Hamilton (2021) Springer ESM
# Access level: 0 (direct download)
# Analysis type: deterministic (mmc1 Main script)
# ===========================================================================
cat("\n\n")
cat("============================================================\n")
cat("TABLE 6: Paleoindian Projectile Points\n")
cat("============================================================\n\n")

paleo <- read.csv("data/key-et-al-2024-paleoindian-points.csv")
cat("Loaded Paleoindian data:", nrow(paleo), "records\n")

types <- c("Clovis", "Eastern Clovis", "Folsom", "Midland")
variables <- c(
  "Length_mm"    = "length_mm",
  "Breadth_mm"   = "breadth_mm",
  "Thickness_mm" = "thickness_mm",
  "Mass_g"       = "mass_g"
)

# Count records per type
for (type in types) {
  n_total <- sum(paleo$type == type)
  n_mass  <- sum(paleo$type == type & !is.na(paleo$mass_g))
  cat(sprintf("  %s: n=%d (mass n=%d)\n", type, n_total, n_mass))
}
cat("\n")

# Run OLE for each type x variable combination
table6_results <- data.frame()

for (type in types) {
  subset_data <- paleo[paleo$type == type, ]
  for (var_label in names(variables)) {
    col_name <- variables[var_label]
    vals <- subset_data[[col_name]]
    vals <- vals[!is.na(vals)]

    # Only run if enough records for k.size = 10
    if (length(vals) >= 10) {
      result <- run_ole(vals)
      result$Type <- type
      result$Variable <- var_label
      table6_results <- rbind(table6_results, result)
    } else {
      cat(sprintf("  SKIPPED: %s / %s — only %d records (need >= 10)\n",
                  type, var_label, length(vals)))
    }
  }
}

# Reorder columns
table6_results <- table6_results[, c("Variable", "Type", "N", "Mean",
                                      "Minimum", "Min_TE", "Min_CI",
                                      "Maximum", "Max_TE", "Max_CI",
                                      "Range_Ext_CI_Pct", "Range_Ext_TE_Pct")]

cat("Results:\n")
print(table6_results, row.names = FALSE)
write.csv(table6_results, "outputs/table-6-paleoindian-results.csv",
          row.names = FALSE)

# Published values for comparison (from Table 6 in paper)
cat("\nPublished Table 6 values for comparison:\n")
cat("Variable       Type            Mean    Min  OLE_Min   Max   OLE_Max  Ext%\n")
cat("Length (mm)    Clovis          67.3   21.9    20.5   230.5  243.4     6.9\n")
cat("               E. Clovis      54.2   27.5    26.6   151.0  211.0    49.3\n")
cat("               Folsom         40.5   16.7    11.7    92.7  105.8    23.8\n")
cat("               Midland        42.0   19.1    14.5    68.0   70.5    14.8\n")
cat("Breadth (mm)   Clovis         27.1   13.0    12.6    64.4   66.3     4.5\n")
cat("               E. Clovis      24.5   11.9     7.5    41.0   46.7    34.8\n")
cat("               Folsom         20.4   10.9     8.8    36.3   40.1    23.3\n")
cat("               Midland        19.5   12.5    10.4    30.5   35.1    37.1\n")
cat("Thickness (mm) Clovis          7.2    3.0     2.8    13.7   14.9    12.2\n")
cat("               E. Clovis       6.8    3.0     1.8    14.0   19.4    60.0\n")
cat("               Folsom          4.2    2.3     2.1    11.1   15.0    46.2\n")
cat("               Midland         4.3    3.0     2.9     6.0    6.5     3.1\n")
cat("Mass (g)       Clovis         38.8    1.9     1.4   196.2  201.8    19.6\n")
cat("               E. Clovis      10.2    2.6     1.6    23.9   27.6    21.9\n")
cat("               Folsom          4.3    0.5    -0.4    32.5   57.9    82.3\n")
cat("               Midland         4.1    1.2     1.0     8.6    8.8     5.1\n")


# ===========================================================================
# TABLE 7: Geometric Microliths — NOT REPRODUCED
# ===========================================================================
cat("\n\n")
cat("============================================================\n")
cat("TABLE 7: Geometric Microliths — NOT REPRODUCED\n")
cat("============================================================\n\n")
cat("Table 7 cannot be reproduced.\n")
cat("Reason: The full morphometric data (Length, Breadth, Thickness, Area)\n")
cat("for the Cueva de la Cocina microliths is not publicly available.\n\n")
cat("The GitHub repositories contain:\n")
cat("  - Geometrics_Cocina: classification/retouching data only (no measurements)\n")
cat("  - GS_GM_AAS: morphometric data for 97 Phase A + 142 Phase B Cocina records\n")
cat("    (vs Key et al.'s n=344 Phase A + n=390 Phase B)\n")
cat("  - Geo_performance: mechanical performance data (different study)\n\n")
cat("The Garcia-Puchol et al. (2023) dataset with n=344/390 morphometric\n")
cat("measurements appears not to be publicly deposited with full variable set.\n\n")
cat("Additionally, Table 7 uses the Randomised OLE script (mmc2) which has\n")
cat("no set.seed() — results would vary between runs even with correct data.\n")


# ===========================================================================
# Summary
# ===========================================================================
cat("\n\n")
cat("============================================================\n")
cat("REPRODUCTION SUMMARY\n")
cat("============================================================\n\n")
cat("Tables reproduced:\n")
cat("  - Table 5 (Olduvai cleavers only): 5 variables, deterministic OLE\n")
cat("  - Table 6 (Paleoindian points):    4 types x 4 variables, deterministic OLE\n")
cat("\n")
cat("Tables NOT reproduced:\n")
cat("  - Table 5 (all other case studies): data not publicly available\n")
cat("  - Table 7 (microliths): morphometric data not publicly available\n")
cat("  - Tables 2-4 (validation): replica data not published\n")
cat("\n")
cat("Output files:\n")
cat("  - outputs/table-5-olduvai-results.csv\n")
cat("  - outputs/table-6-paleoindian-results.csv\n")
cat("  - outputs/run.log\n")
cat("\n")
cat("=== Reproduction complete ===\n")
cat("Date:", format(Sys.time(), "%Y-%m-%d %H:%M:%S %Z"), "\n")

# Close log
sink()
