library(ArchaeoPhases)
burials.ox <- read_oxcal("https://tsdye.online/AP/beads-1.csv")
## Depends on previous definition of bead_list
row.7 <- list("BE1-Disc" = bead_list$BE1.Disc,
"BE1-CylRound" = bead_list$BE1.CylRound)
res <- allen_observe_frequency(burials.ox, row.7, "p")
round(res$observed,2)
