library(ArchaeoPhases)
# Depends on previous definition of bead_list
burials.ox <- read_oxcal("https://tsdye.online/AP/beads-1.csv")
monochrome <- list("BE1-ConSeg" = bead_list$BE1.ConSeg, "BE1-CylPen" = bead_list$BE1.CylPen, "BE1-CylRound" = bead_list$BE1.CylRound, "BE1-SegGlob" = bead_list$BE1.SegGlob, "BE1-Orange" = bead_list$BE1.Orange, "BE1-Dghnt" = bead_list$BE1.Dghnt, "BE1-WoundSp" = bead_list$BE1.WoundSp, "BE1-Melon" = bead_list$BE1.Melon)
res <- allen_observe_frequency(burials.ox, monochrome, "oFD")
round(res$observed, 2)
