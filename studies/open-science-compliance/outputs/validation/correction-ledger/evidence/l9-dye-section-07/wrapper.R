# Operator evidence run for ledger ruling L9 (2026-10-09). The authors'
# section 5 and section 7 transcriptions run byte-identical, in order. The
# only mechanic: the authors' URL read is redirected to the local copy of
# the same file (sha256 02cf52d4...ab9051), outside the authors' files.
library(ArchaeoPhases)
.read_oxcal_pkg <- ArchaeoPhases::read_oxcal
read_oxcal <- function(file, ...) {
  if (identical(file, "https://tsdye.online/AP/beads-1.csv")) file <- "/data/beads-1.csv"
  .read_oxcal_pkg(file, ...)
}
cat("ArchaeoPhases", as.character(packageVersion("ArchaeoPhases")), R.version.string, "\n")
for (f in c("section-05-bead-classification.R", "section-07-stable-branching.R")) {
  cat("== sourcing", f, "md5", tools::md5sum(file.path("/code", f)), "\n")
  source(file.path("/code", f), echo = FALSE, print.eval = TRUE)
}
cat("== unrounded oFD matrix\n"); print(res$observed, digits = 6)
