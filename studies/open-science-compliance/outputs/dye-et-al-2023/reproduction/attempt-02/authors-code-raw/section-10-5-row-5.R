library(ArchaeoPhases)
burials.ox <- read_oxcal("https://tsdye.online/AP/beads-1.csv")
## Depends on previous definition of bead_list
row.5 <- list("BE1-Disc" = bead_list$BE1.Disc,
"BE1-Koch34Wh" = bead_list$BE1.Koch34Wh,
"BE1-Koch34Ye" = bead_list$BE1.Koch34Ye,
"BE1-WhSpiral" = bead_list$BE1.WhSpiral,
"BE1-Dghnt" = bead_list$BE1.Dghnt)
res <- allen_observe_frequency(burials.ox, row.5, "p")
round(res$observed,2)
