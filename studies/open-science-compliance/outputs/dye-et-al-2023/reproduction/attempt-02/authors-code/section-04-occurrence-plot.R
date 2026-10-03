## ===========================================================================
## Dye et al. (2023) supplement (mmc1.pdf), section 04 — authors' R code.
## Transcribed from the printed listing by tools/transcribe_supplement.py
## (typographic restoration only: line numbers and wrap marks removed, curly
## quotes made ASCII). Raw transcription: authors-code-raw/section-04-occurrence-plot.R
## Execution-mechanics edits in this copy (wrapper cardinal rule, invariant 2)
## are marked inline with 'LLMR-PATH:' and listed in log.md.
## ===========================================================================
library(ArchaeoPhases)
burials.ox <- read_oxcal("data/beads-1.csv")  ## LLMR-PATH: was "https://tsdye.online/AP/beads-1.csv" (verified local copy, same sha256)
burial.dates <- c(3:5, 7, 9, 12:78)
occurrence_plot(burials.ox, burial.dates, title = "Anglo-Saxon Female Graves", occurrence = "interment", file = "outputs/all-burials.pdf", height = 9, width = 6, caption = "95% credible interval", x_min = 500, x_max = 700)  ## LLMR-PATH: output file was "all-burials.pdf" (written to outputs/)
