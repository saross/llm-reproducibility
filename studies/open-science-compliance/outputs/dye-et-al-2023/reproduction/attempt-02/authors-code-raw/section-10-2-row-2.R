library(ArchaeoPhases)
burials.ox <- read_oxcal("https://tsdye.online/AP/beads-1.csv")
## Depends on previous definition of bead_list
row.2 <- list("BE1-Disc" = bead_list$BE1.Disc,
"BE1-WhSpiral" = bead_list$BE1.WhSpiral,
"BE1-WoundSp" = bead_list$BE1.WoundSp,
"BE1-Dghnt" = bead_list$BE1.Dghnt,
"BE1-Amethyst" = bead_list$BE1.Amethyst,
"BE1-Cowrie" = bead_list$BE1.Cowrie,
"BE1-Orange" = bead_list$BE1.Orange,
"BE1-DotReg" = bead_list$BE1.DotReg)
res <- allen_observe_frequency(burials.ox, row.2, "p")
round(res$observed,2)
