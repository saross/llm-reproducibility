library(ArchaeoPhases)
burials.ox <- read_oxcal("https://tsdye.online/AP/beads-1.csv")
burial.dates <- c(3:5, 7, 9, 12:78)
occurrence_plot(burials.ox, burial.dates, title = "Anglo-Saxon Female Graves", occurrence = "interment", file = "all-burials.pdf", height = 9, width = 6, caption = "95% credible interval", x_min = 500, x_max = 700)
