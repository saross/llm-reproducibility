## ===========================================================================
## Dye et al. (2023) supplement (mmc1.pdf), section 10.5 — authors' R code.
## Transcribed from the printed listing by tools/transcribe_supplement.py
## (typographic restoration only: line numbers and wrap marks removed, curly
## quotes made ASCII). Raw transcription: authors-code-raw/section-10-5-row-5.R
## Execution-mechanics edits in this copy (wrapper cardinal rule, invariant 2)
## are marked inline with 'LLMR-PATH:' and listed in log.md.
## ===========================================================================
library(ArchaeoPhases)
burials.ox <- read_oxcal("data/beads-1.csv")  ## LLMR-PATH: was "https://tsdye.online/AP/beads-1.csv" (verified local copy, same sha256)
## Depends on previous definition of bead_list
row.5 <- list("BE1-Disc" = bead_list$BE1.Disc,
"BE1-Koch34Wh" = bead_list$BE1.Koch34Wh,
"BE1-Koch34Ye" = bead_list$BE1.Koch34Ye,
"BE1-WhSpiral" = bead_list$BE1.WhSpiral,
"BE1-Dghnt" = bead_list$BE1.Dghnt)
res <- allen_observe_frequency(burials.ox, row.5, "p")
round(res$observed,2)
