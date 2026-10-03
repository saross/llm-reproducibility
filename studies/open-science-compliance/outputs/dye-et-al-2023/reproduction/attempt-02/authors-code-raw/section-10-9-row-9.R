library(ArchaeoPhases)
burials.ox <- read_oxcal("https://tsdye.online/AP/beads-1.csv")
## Depends on previous definition of bead_list
row.9 <- list("BE1-Disc" = bead_list$BE1.Disc,
"BE1-Orange" = bead_list$BE1.Orange,
"BE1-WhSpiral" = bead_list$BE1.WhSpiral,
"BE2-c Metal" = bead_list$BE2.c.Metal,
"BE1-Koch34Bl" = bead_list$BE1.Koch34Bl)
res <- allen_observe_frequency(burials.ox, row.9, "p")
round(res$observed,2)
