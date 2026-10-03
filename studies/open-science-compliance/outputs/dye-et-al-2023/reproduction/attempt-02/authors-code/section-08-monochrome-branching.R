## ===========================================================================
## Dye et al. (2023) supplement (mmc1.pdf), section 08 — authors' R code.
## Transcribed from the printed listing by tools/transcribe_supplement.py
## (typographic restoration only: line numbers and wrap marks removed, curly
## quotes made ASCII). Raw transcription: authors-code-raw/section-08-monochrome-branching.R
## Execution-mechanics edits in this copy (wrapper cardinal rule, invariant 2)
## are marked inline with 'LLMR-PATH:' and listed in log.md.
## ===========================================================================
library(ArchaeoPhases)
# Depends on previous definition of bead_list
burials.ox <- read_oxcal("data/beads-1.csv")  ## LLMR-PATH: was "https://tsdye.online/AP/beads-1.csv" (verified local copy, same sha256)
monochrome <- list("BE1-ConSeg" = bead_list$BE1.ConSeg, "BE1-CylPen" = bead_list$BE1.CylPen, "BE1-CylRound" = bead_list$BE1.CylRound, "BE1-SegGlob" = bead_list$BE1.SegGlob, "BE1-Orange" = bead_list$BE1.Orange, "BE1-Dghnt" = bead_list$BE1.Dghnt, "BE1-WoundSp" = bead_list$BE1.WoundSp, "BE1-Melon" = bead_list$BE1.Melon)
res <- allen_observe_frequency(burials.ox, monochrome, "oFD")
round(res$observed, 2)
