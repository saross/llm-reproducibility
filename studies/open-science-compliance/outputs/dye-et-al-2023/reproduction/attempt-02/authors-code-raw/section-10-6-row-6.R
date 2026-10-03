library(ArchaeoPhases)
burials.ox <- read_oxcal("https://tsdye.online/AP/beads-1.csv")
## Depends on previous definition of bead_list
row.6 <- list("BE1-Disc" = bead_list$BE1.Disc,
"BE1-Dot34" = bead_list$BE1.Dot34,
"BE1-Dghnt" = bead_list$BE1.Dghnt)
res <- allen_observe_frequency(burials.ox, row.6, "p")
round(res$observed,2)
