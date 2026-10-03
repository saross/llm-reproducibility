## ===========================================================================
## Dye et al. (2023) supplement (mmc1.pdf), section 09 — authors' R code.
## Transcribed from the printed listing by tools/transcribe_supplement.py
## (typographic restoration only: line numbers and wrap marks removed, curly
## quotes made ASCII). Raw transcription: authors-code-raw/section-09-dghnt-reticulation.R
## Execution-mechanics edits in this copy (wrapper cardinal rule, invariant 2)
## are marked inline with 'LLMR-PATH:' and listed in log.md.
## ===========================================================================
library(ArchaeoPhases)
# Depends on previous definition of bead_list
burials.ox <- read_oxcal("data/beads-1.csv")  ## LLMR-PATH: was "https://tsdye.online/AP/beads-1.csv" (verified local copy, same sha256)
stable <- list("BE1-Amethyst" = bead_list$BE1.Amethyst, "BE1-Cowrie" = bead_list$BE1.Cowrie, "BE1-Disc" = bead_list$BE1.Disc, "BE3-Amber" = bead_list$BE3.Amber, "BE1-Dghnt" = bead_list$BE1.Dghnt)
res <- allen_observe_frequency(burials.ox, stable, "oFDm")
round(res$observed, 2)
