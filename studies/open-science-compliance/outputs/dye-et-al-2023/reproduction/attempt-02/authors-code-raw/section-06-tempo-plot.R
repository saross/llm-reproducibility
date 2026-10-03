library(ArchaeoPhases)
# Depends on previous definition of bead_list and bead_names
burials.ox <- read_oxcal("https://tsdye.online/AP/beads-1.csv")
foo <- tempo_plot(data = burials.ox, position = bead_list, name = bead_names, title = "", file = "test-bead-tempos.pdf", height = 8, width = 13, caption = "", x_min = 400, x_max = 800, columns = 6, line_types = c("solid", "solid", "solid"), line_sizes = c(1.2, 0.6, 0.6), legend_label = c("Mean", "Credible interval", ""))
