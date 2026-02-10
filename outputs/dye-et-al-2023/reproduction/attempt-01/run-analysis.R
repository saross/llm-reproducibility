#!/usr/bin/env Rscript
# ============================================================================
# Reproduction of Dye et al. 2023
# "Bayesian chronology construction and substance time"
# Journal of Archaeological Science, 153, 105765
#
# This script reproduces the analyses from the supplement using ArchaeoPhases.
# It reads pre-computed OxCal Markov Chain Monte Carlo (MCMC) output and
# performs deterministic post-processing:
#   - Interment occurrence plot (Supplement Section 4, Paper Figure 7)
#   - Bead deposition tempo plots (Supplement Section 6, Paper Figure 8)
#   - Stable solid bead branching relation (Supplement Section 7)
#   - Monochrome bead branching relation (Supplement Section 8)
#   - BE1-Dghnt reticulation ancestor relation (Supplement Section 9)
#   - Bayliss et al. Table 7.18 non-overlapping relations (Section 10)
#
# MCMC source: beads-1.csv (one of five calibration runs)
# The analysis uses a local copy rather than the remote server URL.
# ============================================================================

library(ArchaeoPhases)

cat("=== Dye et al. 2023 Reproduction ===\n")
cat("ArchaeoPhases version:", as.character(packageVersion("ArchaeoPhases")), "\n")
cat("R version:", R.version.string, "\n")
cat("Date:", format(Sys.time(), "%Y-%m-%d %H:%M:%S"), "\n\n")

# ============================================================================
# Section 1: Load MCMC output
# ============================================================================
cat("--- Loading MCMC output ---\n")

# Use local copy (downloaded from https://tsdye.online/AP/beads-1.csv)
burials.ox <- read_oxcal("/analysis/beads-1.csv")

cat("MCMC samples:", nrow(burials.ox), "\n")
cat("Burial columns:", ncol(burials.ox), "\n\n")

# ============================================================================
# Section 2: Define bead-to-burial mappings (Supplement Section 5)
# All strings must be on single lines to match column names exactly
# ============================================================================
cat("--- Defining bead-to-burial mappings ---\n")

# 5.1 BE3-Amber Beads
be3.amber <- c("UB-4836 (WG27)", "UB-5208 (ApD107)", "UB-4965 (ApD117)", "UB-4735 (Ber022)", "UB-4739 (Ber134/1)", "UB-4728 (MH064)", "UB-4729 (MH068)", "UB-4732 (MH094)", "UB-4733 (MH095)", "UB-4734 (MH105c)", "UB-4984 (Lec018)", "UB-4709 (EH014)", "UB-4707 (EH079)", "UB-4708 (EH083)", "UB-6033 (WHes113)", "UB-4706 (WHes118)", "UB-4705 (WHes123)", "UB-6040 (CasD053)", "UB-6037 (CasD134)", "UB-6472 (BuD222)", "UB-6473 (BuD250)", "UB-6476 (BuD339)", "UB-4963 (SPTip208)", "UB-4890 (MelSG075)", "UB-4887 (MelSG082)", "UB-4888 (MelSG089)", "UB-4551 (MaDE1 & E2)", "UB-4552 (MaDE3)", "UB-4975 (AstCli12)", "UB-4835 (ApD134)")

# 5.2 BE1-ConSeg Beads
bel.conseg <- c("UB-6472 (BuD222)", "UB-6476 (BuD339)", "UB-6040 (CasD053)", "UB-4984 (Lec018)", "UB-4734 (MH105c)")

# 5.3 BE1-CylRound Beads
bel.cylround <- c("UB-4965 (ApD117)", "UB-4735 (Ber022)", "UB-4739 (Ber134/1)", "UB-6473 (BuD250)", "UB-6476 (BuD339)", "UB-4729 (MH068)", "UB-4835 (ApD134)", "UB-4708 (EH083)", "UB-4733 (MH095)", "UB-4888 (MelSG089)", "UB-4963 (SPTip208)", "UB-4890 (MelSG075)", "UB-4732 (MH094)")

# 5.4 BE1-CylPen Beads
bel.cylpen <- c("UB-4963 (SPTip208)", "UB-4735 (Ber022)", "UB-4890 (MelSG075)", "UB-6472 (BuD222)", "UB-6473 (BuD250)", "UB-6476 (BuD339)", "UB-4732 (MH094)", "UB-4729 (MH068)")

# 5.5 BE1-MelonBl Beads
bel.melonbl <- c("UB-6472 (BuD222)", "UB-6476 (BuD339)", "UB-4890 (MelSG075)", "UB-4732 (MH094)", "UB-4733 (MH095)")

# 5.6 BE1-Koch34Wh Beads
bel.koch34wh <- c("UB-4965 (ApD117)", "UB-4739 (Ber134/1)", "UB-4836 (WG27)", "UB-5208 (ApD107)", "UB-4888 (MelSG089)", "UB-4706 (WHes118)", "UB-4733 (MH095)", "UB-4735 (Ber022)", "UB-4835 (ApD134)", "UB-4963 (SPTip208)", "UB-6472 (BuD222)", "UB-6035 (CasD096)", "UB-4890 (MelSG075)")

# 5.7 BE1-Koch20Ye Beads
bel.koch20ye <- c("UB-5208 (ApD107)", "UB-4733 (MH095)", "UB-4835 (ApD134)", "UB-4732 (MH094)", "UB-4975 (AstCli12)", "UB-4963 (SPTip208)", "UB-4890 (MelSG075)", "UB-4735 (Ber022)", "UB-4965 (ApD117)", "UB-4708 (EH083)")

# 5.8 BE1-MelonYG Beads
bel.melonyg <- c("UB-6476 (BuD339)", "UB-4733 (MH095)", "UB-4728 (MH064)")

# 5.9 BE1-Reticella Beads
bel.reticella <- c("UB-6037 (CasD134)", "UB-4707 (EH079)", "UB-4729 (MH068)", "UB-4732 (MH094)", "UB-4728 (MH064)", "UB-6476 (BuD339)", "UB-6473 (BuD250)")

# 5.10 BE1-Koch20Wh Beads
bel.koch20wh <- c("UB-5208 (ApD107)", "UB-4835 (ApD134)", "UB-4960 (BuD391B)", "UB-4705 (WHes123)", "UB-4890 (MelSG075)", "UB-4963 (SPTip208)")

# 5.11 BE1-Dot34 Beads
bel.dot34 <- c("UB-4735 (Ber022)", "UB-4836 (WG27)", "UB-4835 (ApD134)", "UB-4890 (MelSG075)", "UB-4732 (MH094)", "UB-4709 (EH014)", "UB-4963 (SPTip208)")

# 5.12 BE1-Koch34Bl Beads
bel.koch34bl <- c("UB-4835 (ApD134)", "UB-4890 (MelSG075)", "UB-4735 (Ber022)", "UB-4708 (EH083)", "UB-4965 (ApD117)", "UB-4739 (Ber134/1)", "UB-4836 (WG27)", "UB-6038 (CasD183)", "UB-4888 (MelSG089)", "UB-4706 (WHes118)")

# 5.13 BE1-Koch49/50 Beads
bel.koch49.50 <- c("UB-6472 (BuD222)", "UB-6476 (BuD339)", "UB-4965 (ApD117)")

# 5.14 BE1-Koch34Ye Beads
bel.koch34ye <- c("UB-4708 (EH083)", "UB-4888 (MelSG089)", "UB-6472 (BuD222)", "UB-4975 (AstCli12)", "UB-4890 (MelSG075)")

# 5.15 BE1-DotReg Beads
bel.dotreg <- c("UB-4835 (ApD134)", "UB-4975 (AstCli12)", "UB-5208 (ApD107)", "UB-4739 (Ber134/1)", "UB-6042 (CasD088)")

# 5.16 BE1-SegGlob Beads
bel.segglob <- c("UB-4890 (MelSG075)", "UB-4963 (SPTip208)")

# 5.17 BE2c-Metal Beads
be2c.metal <- c("UB-4964 (Cod30)", "UB-6035 (CasD096)", "UB-4888 (MelSG089)", "UB-6033 (WHes113)")

# 5.18 BE1-Orange Beads
bel.orange <- c("UB-4889 (MelSG069)", "UB-4963 (SPTip208)", "UB-4888 (MelSG089)", "UB-4883 (MelSG095)", "UB-4964 (Cod30)")

# 5.19 BE1-Cowrie Beads
bel.cowrie <- c("UB-4552 (MaDE3)", "UB-4553 (MaDD10)", "UB-4554 (MaDF2)", "UB-4889 (MelSG069)", "UB-6032 (SPTip073)", "UB-4503 (Lec148)", "UB-4887 (MelSG082)")

# 5.20 BE1-WoundSp Beads
bel.woundsp <- c("UB-4551 (MaDE1 & E2)", "UB-4552 (MaDE3)", "UB-4910 (BloodH22)", "UB-4077 (But4275)", "UB-4964 (Cod30)", "UB-4553 (MaDD10)", "UB-4554 (MaDF2)", "UB-4549 (MaDC7)", "UB-4512 (EH091)", "UB-4503 (Lec148)", "UB-4501 (Lec014)", "UB-4502 (Lec138)", "UB-4042 (But1674)")

# 5.21 BE1-Dghnt Beads
bel.dghnt <- c("UB-4503 (Lec148)", "UB-4506 (Lec172/2)", "UB-6038 (CasD183)", "UB-4512 (EH091)", "UB-4501 (Lec014)", "UB-4507 (Lec187)", "UB-4502 (Lec138)", "UB-4042 (But1674)")

# 5.22 BE1-Amethyst Beads
bel.amethyst <- c("UB-4551 (MaDE1 & E2)", "UB-4959 (BuD391A)", "UB-4964 (Cod30)", "UB-4506 (Lec172/2)", "UB-4552 (MaDE3)")

# 5.23 BE1-Disc Beads
bel.disc <- c("UB-4553 (MaDD10)", "UB-4554 (MaDF2)", "UB-4549 (MaDC7)")

# ============================================================================
# Section 3: Assemble bead list and apply Lakenheath updates (Sections 5.24-5.38)
# ============================================================================
cat("--- Assembling bead list with Lakenheath updates ---\n")

# Build named list directly
bead_list <- list(
    BE3.Amber     = be3.amber,
    BE1.ConSeg    = bel.conseg,
    BE1.CylRound  = bel.cylround,
    BE1.CylPen    = bel.cylpen,
    BE1.MelonBl   = bel.melonbl,
    BE1.Koch34Wh  = bel.koch34wh,
    BE1.Koch20Ye  = bel.koch20ye,
    BE1.MelonY.G  = bel.melonyg,
    BE1.Reticella = bel.reticella,
    BE1.Koch20Wh  = bel.koch20wh,
    BE1.Dot34     = bel.dot34,
    BE1.Koch34Bl  = bel.koch34bl,
    BE1.Koch49.50 = bel.koch49.50,
    BE1.Koch34Ye  = bel.koch34ye,
    BE1.DotReg    = bel.dotreg,
    BE1.SegGlob   = bel.segglob,
    BE2.c.Metal   = be2c.metal,
    BE1.Orange    = bel.orange,
    BE1.Cowrie    = bel.cowrie,
    BE1.WoundSp   = bel.woundsp,
    BE1.Dghnt     = bel.dghnt,
    BE1.Amethyst  = bel.amethyst,
    BE1.Disc      = bel.disc
)

# Display names for tempo plots (must match order of bead_list after updates)
bead_names <- c("BE3-Amber", "BE1-ConSeg", "BE1-CylRound", "BE1-CylPen",
    "BE1-MelonBl", "BE1-Koch34Wh", "BE1-Koch20Ye", "BE1-MelonY-G",
    "BE1-Reticella", "BE1-Koch20Wh", "BE1-Dot34", "BE1-Koch34Bl",
    "BE1-Koch49/50", "BE1-Koch34Ye", "BE1-DotReg", "BE1-SegGlob",
    "BE2-c Metal", "BE1-Orange", "BE1-Cowrie", "BE1-WoundSp",
    "BE1-Dghnt", "BE1-Amethyst", "BE1-Disc")

# 5.25 Update BE1-Melon (consolidate MelonBl and MelonYG + Lakenheath)
bead_list$BE1.Melon <- c(bead_list$BE1.MelonBl, bead_list$BE1.MelonY.G, "SUERC-39113 (ERL G417)")
# Remove old melon entries
bead_list$BE1.MelonBl <- NULL
bead_list$BE1.MelonY.G <- NULL
# Update display names accordingly
bead_names <- bead_names[!bead_names %in% c("BE1-MelonBl", "BE1-MelonY-G")]
bead_names <- c(bead_names, "BE1-Melon")

# 5.26 Update BE1-Amethyst
bead_list$BE1.Amethyst <- c(bead_list$BE1.Amethyst, "SUERC-39100 (ERL G266)", "SUERC-39096 (ERL G112)")

# 5.27 Update BE1-Cowrie
bead_list$BE1.Cowrie <- c(bead_list$BE1.Cowrie, "SUERC-39096 (ERL G112)", "SUERC-39100 (ERL G266)")

# 5.28 Update BE1-Dghnt
bead_list$BE1.Dghnt <- c(bead_list$BE1.Dghnt, "SUERC-39100 (ERL G266)")

# 5.29 Update BE1-Orange
bead_list$BE1.Orange <- c(bead_list$BE1.Orange, "SUERC-39100 (ERL G266)", "SUERC-51551 (ERL G193)", "SUERC-51552 (ERL G107)", "SUERC-51553 (ERL G116)")

# 5.30 Update BE1-WhSpiral (new category)
bead_list$BE1.WhSpiral <- c("UB-4889 (MelSG069)", "SUERC-51548 (ERL G210)")
bead_names <- c(bead_names, "BE1-WhSpiral")

# 5.31 Update BE2-c
bead_list$BE2.c.Metal <- c(bead_list$BE2.c.Metal, "SUERC-39100 (ERL G266)", "SUERC-51553 (ERL G116)")

# 5.32 Update BE1-Koch20Ye
bead_list$BE1.Koch20Ye <- c(bead_list$BE1.Koch20Ye, "SUERC-51539 (ERL G353)", "SUERC-51539 (ERL G353)")

# 5.33 Update BE1-Koch34Wh
bead_list$BE1.Koch34Wh <- c(bead_list$BE1.Koch34Wh, "SUERC-51551 (ERL G193)", "SUERC-51552 (ERL G107)")

# 5.34 Update BE1-Koch34Ye
bead_list$BE1.Koch34Ye <- c(bead_list$BE1.Koch34Ye, "SUERC-51539 (ERL G353)", "SUERC-51543 (ERL G281)", "SUERC-51552 (ERL G107)")

# 5.35 Update BE1-CylRound
bead_list$BE1.CylRound <- c(bead_list$BE1.CylRound, "SUERC-51539 (ERL G353)", "SUERC-51551 (ERL G193)")

# 5.36 Update BE1-SegGlob
bead_list$BE1.SegGlob <- c(bead_list$BE1.SegGlob, "SUERC-51549 (ERL G195)")

# 5.37 Update BE1-Koch34Bl
bead_list$BE1.Koch34Bl <- c(bead_list$BE1.Koch34Bl, "SUERC-51539 (ERL G353)", "SUERC-51543 (ERL G281)", "SUERC-51549 (ERL G195)", "SUERC-51551 (ERL G193)", "SUERC-51552 (ERL G107)")

# 5.38 Update BE3-Amber
bead_list$BE3.Amber <- c(bead_list$BE3.Amber, "SUERC-39108 ERLK G322", "SUERC-39109 ERL G362", "SUERC-39112 ERL G405", "SUERC-51560 ERL G038", "SUERC-39091 (ERL G003)", "SUERC-39092 (ERL G005)", "SUERC-39113 (ERL G417)", "SUERC-51549 (ERL G195)", "SUERC-51552 (ERL G107)", "SUERC-51550 (ERL G254)")

cat("Total bead types defined:", length(bead_list), "\n")
cat("Bead type names:", paste(names(bead_list), collapse = ", "), "\n\n")

# Validate: check all sample IDs exist in MCMC columns
all_samples <- unique(unlist(bead_list))
missing <- all_samples[!all_samples %in% colnames(burials.ox)]
if (length(missing) > 0) {
    cat("WARNING: Missing samples in MCMC data:\n")
    print(missing)
    cat("\n")
} else {
    cat("All sample IDs validated against MCMC columns.\n\n")
}

# ============================================================================
# Section 4: Occurrence plot (Supplement Section 4, Paper Figure 7)
# ============================================================================
cat("--- Generating occurrence plot ---\n")

# Supplement specifies c(3:5, 7, 9, 12:78) relative to original CSV with Pass column
# After read_oxcal drops Pass, shift indices: c(2:4, 6, 8, 11:77)
burial.dates <- c(2:4, 6, 8, 11:77)

cat("Number of interments:", length(burial.dates), "\n")

occurrence_plot(burials.ox, burial.dates, title = "Anglo-Saxon Female Graves",
    occurrence = "interment", file = "outputs/occurrence-plot.pdf",
    height = 9, width = 6, caption = "95% credible interval",
    x_min = 500, x_max = 700)

cat("Occurrence plot saved to outputs/occurrence-plot.pdf\n\n")

# ============================================================================
# Section 5: Tempo plots (Supplement Section 6, Paper Figure 8)
# ============================================================================
cat("--- Generating tempo plots ---\n")

# Convert bead_list to positional list matching bead_names order
bead_positions <- lapply(bead_list, function(samples) {
    which(colnames(burials.ox) %in% samples)
})

foo <- tempo_plot(data = burials.ox, position = bead_list,
    name = as.list(bead_names), title = "", file = "outputs/tempo-plots.pdf",
    height = 8, width = 13, caption = "",
    x_min = 400, x_max = 800, columns = 6,
    line_types = c("solid", "solid", "solid"),
    line_sizes = c(1.2, 0.6, 0.6),
    legend_label = c("Mean", "Credible interval", ""))

cat("Tempo plots saved to outputs/tempo-plots.pdf\n\n")

# ============================================================================
# Section 6: Stable solid bead branching relation (Supplement Section 7)
# Uses Allen set "oFD" (overlaps, finished by, or contains)
# ============================================================================
cat("--- Stable solid bead branching relation ---\n")

stable <- list("BE1-Amethyst" = bead_list$BE1.Amethyst,
    "BE1-Cowrie" = bead_list$BE1.Cowrie,
    "BE1-Disc" = bead_list$BE1.Disc,
    "BE3-Amber" = bead_list$BE3.Amber)
res <- allen_observe_frequency(burials.ox, stable, "oFD")
stable_branching <- round(res$observed, 2)
cat("Stable solid branching (oFD):\n")
print(stable_branching)
cat("\n")

# ============================================================================
# Section 7: Monochrome bead branching relation (Supplement Section 8)
# Uses Allen set "oFD"
# ============================================================================
cat("--- Monochrome bead branching relation ---\n")

monochrome <- list("BE1-ConSeg" = bead_list$BE1.ConSeg,
    "BE1-CylPen" = bead_list$BE1.CylPen,
    "BE1-CylRound" = bead_list$BE1.CylRound,
    "BE1-SegGlob" = bead_list$BE1.SegGlob,
    "BE1-Orange" = bead_list$BE1.Orange,
    "BE1-Dghnt" = bead_list$BE1.Dghnt,
    "BE1-WoundSp" = bead_list$BE1.WoundSp,
    "BE1-Melon" = bead_list$BE1.Melon)
res <- allen_observe_frequency(burials.ox, monochrome, "oFD")
monochrome_branching <- round(res$observed, 2)
cat("Monochrome branching (oFD):\n")
print(monochrome_branching)
cat("\n")

# ============================================================================
# Section 8: BE1-Dghnt reticulation ancestor relation (Supplement Section 9)
# Uses Allen set "oFDm" (overlaps, finished by, contains, or meets)
# ============================================================================
cat("--- BE1-Dghnt reticulation ancestor relation ---\n")

stable2 <- list("BE1-Amethyst" = bead_list$BE1.Amethyst,
    "BE1-Cowrie" = bead_list$BE1.Cowrie,
    "BE1-Disc" = bead_list$BE1.Disc,
    "BE3-Amber" = bead_list$BE3.Amber,
    "BE1-Dghnt" = bead_list$BE1.Dghnt)
res <- allen_observe_frequency(burials.ox, stable2, "oFDm")
reticulation <- round(res$observed, 2)
cat("BE1-Dghnt reticulation (oFDm):\n")
print(reticulation)
cat("\n")

# ============================================================================
# Section 9: Bayliss et al. Table 7.18 non-overlapping relations
# (Supplement Section 10, rows 1-9)
# Uses Allen set "p" (precedes)
# ============================================================================
cat("=== Bayliss et al. Table 7.18 Relations ===\n\n")

# Row 1: Earlier types (BE1-Reticella, BE1-Melon) vs Later types
cat("--- Row 1 (Earlier: BE1-Reticella, BE1-Melon) ---\n")
row.1 <- list("BE1-Disc" = bead_list$BE1.Disc,
    "BE1-WhSpiral" = bead_list$BE1.WhSpiral,
    "BE1-WoundSp" = bead_list$BE1.WoundSp,
    "BE1-Dghnt" = bead_list$BE1.Dghnt,
    "BE1-Amethyst" = bead_list$BE1.Amethyst,
    "BE1-Cowrie" = bead_list$BE1.Cowrie,
    "BE1-Orange" = bead_list$BE1.Orange,
    "BE2-c Metal" = bead_list$BE2.c.Metal,
    "BE1-Reticella" = bead_list$BE1.Reticella,
    "BE1-Melon" = bead_list$BE1.Melon)
res <- allen_observe_frequency(burials.ox, row.1, "p")
row1_result <- round(res$observed, 2)
cat("Row 1 (p):\n")
print(row1_result)
cat("\n")

# Row 2: Earlier type (BE1-DotReg) vs Later types
cat("--- Row 2 (Earlier: BE1-DotReg) ---\n")
row.2 <- list("BE1-Disc" = bead_list$BE1.Disc,
    "BE1-WhSpiral" = bead_list$BE1.WhSpiral,
    "BE1-WoundSp" = bead_list$BE1.WoundSp,
    "BE1-Dghnt" = bead_list$BE1.Dghnt,
    "BE1-Amethyst" = bead_list$BE1.Amethyst,
    "BE1-Cowrie" = bead_list$BE1.Cowrie,
    "BE1-Orange" = bead_list$BE1.Orange,
    "BE1-DotReg" = bead_list$BE1.DotReg)
res <- allen_observe_frequency(burials.ox, row.2, "p")
row2_result <- round(res$observed, 2)
cat("Row 2 (p):\n")
print(row2_result)
cat("\n")

# Row 3: Earlier type (BE1-Koch20Ye) vs Later types
cat("--- Row 3 (Earlier: BE1-Koch20Ye) ---\n")
row.3 <- list("BE1-Disc" = bead_list$BE1.Disc,
    "BE1-WhSpiral" = bead_list$BE1.WhSpiral,
    "BE1-WoundSp" = bead_list$BE1.WoundSp,
    "BE1-Dghnt" = bead_list$BE1.Dghnt,
    "BE1-Amethyst" = bead_list$BE1.Amethyst,
    "BE1-Koch20Ye" = bead_list$BE1.Koch20Ye)
res <- allen_observe_frequency(burials.ox, row.3, "p")
row3_result <- round(res$observed, 2)
cat("Row 3 (p):\n")
print(row3_result)
cat("\n")

# Row 4: Earlier types (BE1-CylPen, BE1-Koch20Wh, BE1-Koch49/50) vs Later types
cat("--- Row 4 (Earlier: BE1-CylPen, BE1-Koch20Wh, BE1-Koch49/50) ---\n")
row.4 <- list("BE1-Disc" = bead_list$BE1.Disc,
    "BE1-WhSpiral" = bead_list$BE1.WhSpiral,
    "BE1-WoundSp" = bead_list$BE1.WoundSp,
    "BE1-Dghnt" = bead_list$BE1.Dghnt,
    "BE1-CylPen" = bead_list$BE1.CylPen,
    "BE1-Koch20Wh" = bead_list$BE1.Koch20Wh,
    "BE1-Koch49/50" = bead_list$BE1.Koch49.50)
res <- allen_observe_frequency(burials.ox, row.4, "p")
row4_result <- round(res$observed, 2)
cat("Row 4 (p):\n")
print(row4_result)
cat("\n")

# Row 5: Earlier types (BE1-Koch34Wh, BE1-Koch34Ye) vs Later types
cat("--- Row 5 (Earlier: BE1-Koch34Wh, BE1-Koch34Ye) ---\n")
row.5 <- list("BE1-Disc" = bead_list$BE1.Disc,
    "BE1-Koch34Wh" = bead_list$BE1.Koch34Wh,
    "BE1-Koch34Ye" = bead_list$BE1.Koch34Ye,
    "BE1-WhSpiral" = bead_list$BE1.WhSpiral,
    "BE1-Dghnt" = bead_list$BE1.Dghnt)
res <- allen_observe_frequency(burials.ox, row.5, "p")
row5_result <- round(res$observed, 2)
cat("Row 5 (p):\n")
print(row5_result)
cat("\n")

# Row 6: Earlier type (BE1-Dot34) vs Later types
cat("--- Row 6 (Earlier: BE1-Dot34) ---\n")
row.6 <- list("BE1-Disc" = bead_list$BE1.Disc,
    "BE1-Dot34" = bead_list$BE1.Dot34,
    "BE1-Dghnt" = bead_list$BE1.Dghnt)
res <- allen_observe_frequency(burials.ox, row.6, "p")
row6_result <- round(res$observed, 2)
cat("Row 6 (p):\n")
print(row6_result)
cat("\n")

# Row 7: Earlier type (BE1-CylRound) vs Later type (BE1-Disc)
cat("--- Row 7 (Earlier: BE1-CylRound) ---\n")
row.7 <- list("BE1-Disc" = bead_list$BE1.Disc,
    "BE1-CylRound" = bead_list$BE1.CylRound)
res <- allen_observe_frequency(burials.ox, row.7, "p")
row7_result <- round(res$observed, 2)
cat("Row 7 (p):\n")
print(row7_result)
cat("\n")

# Row 8: Earlier type (BE1-SegGlob) vs Later type (BE1-Disc)
cat("--- Row 8 (Earlier: BE1-SegGlob) ---\n")
row.8 <- list("BE1-Disc" = bead_list$BE1.Disc,
    "BE1-SegGlob" = bead_list$BE1.SegGlob)
res <- allen_observe_frequency(burials.ox, row.8, "p")
row8_result <- round(res$observed, 2)
cat("Row 8 (p):\n")
print(row8_result)
cat("\n")

# Row 9: Earlier types vs Later type (BE1-Disc)
cat("--- Row 9 (Earlier: BE1-Koch34Bl, BE1-Orange, BE1-WhSpiral, BE2-c Metal) ---\n")
row.9 <- list("BE1-Disc" = bead_list$BE1.Disc,
    "BE1-Orange" = bead_list$BE1.Orange,
    "BE1-WhSpiral" = bead_list$BE1.WhSpiral,
    "BE2-c Metal" = bead_list$BE2.c.Metal,
    "BE1-Koch34Bl" = bead_list$BE1.Koch34Bl)
res <- allen_observe_frequency(burials.ox, row.9, "p")
row9_result <- round(res$observed, 2)
cat("Row 9 (p):\n")
print(row9_result)
cat("\n")

# ============================================================================
# Section 10: Export all numerical results
# ============================================================================
cat("--- Exporting numerical results ---\n")

sink("outputs/summary-stats.txt")
cat("=== Dye et al. 2023 Reproduction Results ===\n")
cat("Generated:", format(Sys.time(), "%Y-%m-%d %H:%M:%S"), "\n")
cat("ArchaeoPhases version:", as.character(packageVersion("ArchaeoPhases")), "\n")
cat("R version:", R.version.string, "\n")
cat("MCMC source: beads-1.csv (6000 samples)\n\n")

cat("=== Stable Solid Branching (oFD) ===\n")
print(stable_branching)
cat("\n=== Monochrome Branching (oFD) ===\n")
print(monochrome_branching)
cat("\n=== BE1-Dghnt Reticulation (oFDm) ===\n")
print(reticulation)

cat("\n=== Bayliss Table 7.18 Relations (p) ===\n")
cat("\nRow 1 (Earlier: BE1-Reticella, BE1-Melon):\n")
print(row1_result)
cat("\nRow 2 (Earlier: BE1-DotReg):\n")
print(row2_result)
cat("\nRow 3 (Earlier: BE1-Koch20Ye):\n")
print(row3_result)
cat("\nRow 4 (Earlier: BE1-CylPen, BE1-Koch20Wh, BE1-Koch49/50):\n")
print(row4_result)
cat("\nRow 5 (Earlier: BE1-Koch34Wh, BE1-Koch34Ye):\n")
print(row5_result)
cat("\nRow 6 (Earlier: BE1-Dot34):\n")
print(row6_result)
cat("\nRow 7 (Earlier: BE1-CylRound):\n")
print(row7_result)
cat("\nRow 8 (Earlier: BE1-SegGlob):\n")
print(row8_result)
cat("\nRow 9 (Earlier: BE1-Koch34Bl, BE1-Orange, BE1-WhSpiral, BE2-c Metal):\n")
print(row9_result)
sink()

cat("Summary saved to outputs/summary-stats.txt\n")
cat("\n=== Reproduction complete ===\n")
