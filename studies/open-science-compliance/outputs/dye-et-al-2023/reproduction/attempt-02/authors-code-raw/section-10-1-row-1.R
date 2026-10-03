library(ArchaeoPhases)
burials.ox <- read_oxcal("https://tsdye.online/AP/beads-1.csv")
## Depends on previous definition of bead_list
row.1 <- list("BE1-Disc" = bead_list$BE1.Disc,
"BE1-WhSpiral" = bead_list$BE1.WhSpiral,
"BE1-WoundSp" = bead_list$BE1.WoundSp,
"BE1-Dghnt" = bead_list$BE1.Dghnt,
"BE1-Amethyst" = bead_list$BE1.Amethyst,
"BE1-Cowrie" = bead_list$BE1.Cowrie,
"BE1-Orange" = bead_list$BE1.Orange,
"BE2-c Metal" = bead_list$BE2.c.Metal,
"BE1-Reticella" = bead_list$BE1.Reticella,
"BE1-Melon" = bead_list$BE1.Melon)
res <- allen_observe_frequency(burials.ox, row.1, "p")
round(res$observed,2)
