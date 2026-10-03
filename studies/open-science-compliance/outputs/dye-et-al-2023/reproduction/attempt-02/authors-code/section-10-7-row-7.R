## ===========================================================================
## Dye et al. (2023) supplement (mmc1.pdf), section 10.7 — authors' R code.
## Transcribed from the printed listing by tools/transcribe_supplement.py
## (typographic restoration only: line numbers and wrap marks removed, curly
## quotes made ASCII). Raw transcription: authors-code-raw/section-10-7-row-7.R
## Execution-mechanics edits in this copy (wrapper cardinal rule, invariant 2)
## are marked inline with 'LLMR-PATH:' and listed in log.md.
## ===========================================================================
library(ArchaeoPhases)
burials.ox <- read_oxcal("data/beads-1.csv")  ## LLMR-PATH: was "https://tsdye.online/AP/beads-1.csv" (verified local copy, same sha256)
## Depends on previous definition of bead_list
row.7 <- list("BE1-Disc" = bead_list$BE1.Disc,
"BE1-CylRound" = bead_list$BE1.CylRound)
res <- allen_observe_frequency(burials.ox, row.7, "p")
round(res$observed,2)
