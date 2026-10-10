# Diagnostic (read-only): the plateau of Fig. 2 panel a, from v1.0.0's archived posterior.
# Run from the deposit root in the probe image: Rscript posterior-plateau.R
source("src/utility.R")
load("sim/results/post_sim1a.RData"); load("sim/simdata/simdata1a.RData")
print(ls())
x <- post.sample.core.sim1a
cat("draws:", nrow(x), " columns:", paste(colnames(x), collapse = ", "), "\n")
print(t(apply(x[, c("r", "m", "mu_k")], 2, quantile, c(0.025, 0.5, 0.975))))
cat("mean mu_k:", mean(x[, "mu_k"]), "\n")
print(true.param.1a)
# Value of the plotted posterior mean and 95% band at the last plotted year (1700 BP).
v <- sigmoid(x = 1700, r = x[, "r"], m = round(x[, "m"]), k = x[, "mu_k"])
cat("at 1700 BP: mean", mean(v), " 2.5%", quantile(v, 0.025), " 97.5%", quantile(v, 0.975), "\n")
