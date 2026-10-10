# Diagnostic (read-only) for ruling L18: does the true curve lie inside the 95%
# band that v1.0.0's archived posteriors give, at every plotted year? Tests
# the paper's §5.1 claim ("the 'true' curve within the 95% posterior fitted
# range (Fig. 2a and b)") against the selected version's archive, using the
# deposit's own sigmoid() and plot.fitted()'s band construction.
# Run from the deposit root in the probe image: Rscript curve-containment.R
source("src/utility.R")
check <- function(post_file, sim_file, post_obj, truth_obj, years) {
  load(post_file); load(sim_file)
  x <- get(post_obj); truth <- get(truth_obj)
  mat <- sapply(seq_len(nrow(x)), function(i)
    sigmoid(x = years, r = x[i, "r"], m = round(x[i, "m"]), k = x[i, "mu_k"]))
  lo <- apply(mat, 1, quantile, 0.025); hi <- apply(mat, 1, quantile, 0.975)
  tr <- sigmoid(x = years, r = truth$r, m = truth$m, k = truth$mu_k)
  inside <- tr >= lo & tr <= hi
  margin <- pmin(tr - lo, hi - tr)
  cat(sprintf("%s: %d draws; true curve inside the 95%% band at %d of %d years; ",
              post_obj, nrow(x), sum(inside), length(years)))
  # Where all curves are near 0 the margin is trivially 0; report it where the
  # true proportion exceeds 0.05 as well.
  live <- tr > 0.05
  cat(sprintf("smallest margin %.4f; where true p > 0.05, %.4f at %d BP\n", min(margin),
              min(margin[live]), years[live][which.min(margin[live])]))
}
check("sim/results/post_sim1a.RData", "sim/simdata/simdata1a.RData",
      "post.sample.core.sim1a", "true.param.1a", 4000:1700)
check("sim/results/post_sim1b.RData", "sim/simdata/simdata1b.RData",
      "post.sample.core.sim1b", "true.param.1b", 7000:3000)
