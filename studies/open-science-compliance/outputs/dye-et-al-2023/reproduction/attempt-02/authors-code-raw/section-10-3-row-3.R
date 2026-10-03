library(ArchaeoPhases)
burials.ox <- read_oxcal("https://tsdye.online/AP/beads-1.csv")
## Depends on previous definition of bead_list
row.3 <- list("BE1-Disc" = bead_list$BE1.Disc,
"BE1-WhSpiral" = bead_list$BE1.WhSpiral,
"BE1-WoundSp" = bead_list$BE1.WoundSp,
"BE1-Dghnt" = bead_list$BE1.Dghnt,
"BE1-Amethyst" = bead_list$BE1.Amethyst,
"BE1-Koch20Ye" = bead_list$BE1.Koch20Ye)
res <- allen_observe_frequency(burials.ox, row.3, "p")
round(res$observed,2)
