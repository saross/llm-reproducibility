library(ArchaeoPhases)
burials.ox <- read_oxcal("/home/dk/Projects/hierarchical- sequence-prior/phyletic- seriation/project_source/lakenheath/beads-1.csv")
## Depends on previous definition of bead_list
row.4 <- list("BE1-Disc" = bead_list$BE1.Disc,
"BE1-WhSpiral" = bead_list$BE1.WhSpiral,
"BE1-WoundSp" = bead_list$BE1.WoundSp,
"BE1-Dghnt" = bead_list$BE1.Dghnt,
"BE1-CylPen" = bead_list$BE1.CylPen,
"BE1-Koch20Wh" = bead_list$BE1.Koch20Wh,
"BE1-Koch49/50" = bead_list$BE1.Koch49.50)
res <- allen_observe_frequency(burials.ox, row.4, "p")
round(res$observed,2)
