library(ArchaeoPhases)
# Depends on previous definition of bead_list
burials.ox <- read_oxcal("https://tsdye.online/AP/beads-1.csv")
stable <- list("BE1-Amethyst" = bead_list$BE1.Amethyst, "BE1-Cowrie" = bead_list$BE1.Cowrie, "BE1-Disc" = bead_list$BE1.Disc, "BE3-Amber" = bead_list$BE3.Amber, "BE1-Dghnt" = bead_list$BE1.Dghnt)
res <- allen_observe_frequency(burials.ox, stable, "oFDm")
round(res$observed, 2)
