## ===========================================================================
## Dye et al. (2023) supplement (mmc1.pdf), section 06 — authors' R code.
## Transcribed from the printed listing by tools/transcribe_supplement.py
## (typographic restoration only: line numbers and wrap marks removed, curly
## quotes made ASCII). Raw transcription: authors-code-raw/section-06-tempo-plot.R
## Execution-mechanics edits in this copy (wrapper cardinal rule, invariant 2)
## are marked inline with 'LLMR-PATH:' and listed in log.md.
## ===========================================================================
library(ArchaeoPhases)
# Depends on previous definition of bead_list and bead_names
burials.ox <- read_oxcal("data/beads-1.csv")  ## LLMR-PATH: was "https://tsdye.online/AP/beads-1.csv" (verified local copy, same sha256)
foo <- tempo_plot(data = burials.ox, position = bead_list, name = bead_names, title = "", file = "outputs/test-bead-tempos.pdf", height = 8, width = 13, caption = "", x_min = 400, x_max = 800, columns = 6, line_types = c("solid", "solid", "solid"), line_sizes = c(1.2, 0.6, 0.6), legend_label = c("Mean", "Credible interval", ""))  ## LLMR-PATH: output file was "test-bead-tempos.pdf" (written to outputs/)
