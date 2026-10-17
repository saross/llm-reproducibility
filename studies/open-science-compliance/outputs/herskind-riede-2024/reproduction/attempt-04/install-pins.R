# =============================================================================
# install-pins.R -- build-time package installation for herskind-riede-2024
# (reproduction attempt 04). Runs only inside `docker build` (see Dockerfile).
#
# What it does
# ------------
# The deposit README (Zenodo record 10801706) pins R 4.3.2 and seven packages:
#   extrafont 0.19, data.table 1.15.0, dplyr 1.1.4, ggplot2 3.5.0,
#   readxl 1.4.3, quanteda 3.3.1, forcats 1.0.0.
# The authors supplied no container, so the base image (rocker/r-ver:4.3.2)
# is the reproducer's choice and its built-in Posit Package Manager date
# (2024-02-28) is not the authors'. Following invariant 2 ("Supplied pins
# take precedence", "Version-search cap") and dockerfile-patterns.md
# ("Package repository dates"):
#   * each pinned package is built from CRAN's own source tarball
#     (src/contrib/ or src/contrib/Archive/<pkg>/), never from a snapshot;
#   * packages the authors left unspecified (the pins' dependencies) come
#     from a Posit Package Manager snapshot dated to the article's first
#     online appearance, 2024-04-03 (Journal of Archaeological Science 165,
#     "Available online 3 April 2024");
#   * a pin that fails to build is retried at its immediately preceding,
#     then immediately following, CRAN release (at most three attempts),
#     and every attempt is logged;
#   * a failed installation (which install.packages reports only as a
#     warning) is promoted to an error;
#   * the final inventory of every non-base package is written to
#     /opt/llmr/package-inventory.csv, each marked pinned, unspecified, or
#     fallback, and the build fails on any mismatch with the pins.
#
# This file changes nothing the authors' code computes: it only chooses and
# installs public package releases (routine under invariant 2).
# =============================================================================

SNAPSHOT_DATE <- "2024-04-03"
SNAPSHOT <- paste0("https://packagemanager.posit.co/cran/__linux__/jammy/", SNAPSHOT_DATE)
CRAN <- "https://cloud.r-project.org"

# Pinned versions, in an order where no pinned package needs a later one.
PINS <- c(data.table = "1.15.0", forcats = "1.0.0", dplyr = "1.1.4",
          ggplot2 = "3.5.0", readxl = "1.4.3", extrafont = "0.19",
          quanteda = "3.3.1")

options(repos = c(CRAN = SNAPSHOT), Ncpus = 8L)
dir.create("/opt/llmr", showWarnings = FALSE, recursive = TRUE)
attempt_log <- list()
base_pkgs <- rownames(installed.packages(priority = "base"))
# Packages the base image already carries (R's recommended set, and rocker's
# own tools such as littler); recorded separately, never reinstalled.
preinstalled <- installed.packages()
preinstalled <- rownames(preinstalled)[is.na(preinstalled[, "Priority"]) |
                                       preinstalled[, "Priority"] != "base"]

#' Every CRAN release of a package: current (src/contrib) and archived.
#'
#' @param pkg Package name.
#' @return A data frame of version strings and tarball URLs, oldest first.
cran_releases <- function(pkg) {
  archive_url <- sprintf("%s/src/contrib/Archive/%s/", CRAN, pkg)
  html <- tryCatch(readLines(url(archive_url), warn = FALSE), error = function(e) character())
  pattern <- sprintf("%s_([0-9][0-9.\\-]*)\\.tar\\.gz", gsub(".", "\\.", pkg, fixed = TRUE))
  hits <- unique(regmatches(html, regexpr(pattern, html)))
  versions <- sub(pattern, "\\1", hits)
  urls <- paste0(archive_url, hits)
  current <- available.packages(repos = CRAN)
  if (pkg %in% rownames(current)) {
    v <- current[pkg, "Version"]
    versions <- c(versions, v)
    urls <- c(urls, sprintf("%s/src/contrib/%s_%s.tar.gz", CRAN, pkg, v))
  }
  out <- data.frame(version = versions, url = urls, stringsAsFactors = FALSE)
  out <- out[!duplicated(out$version), ]
  out[order(package_version(out$version)), ]
}

#' Dependencies (Depends, Imports, LinkingTo) named in a tarball's DESCRIPTION.
#'
#' @param tarball Path to a source tarball.
#' @param pkg Package name (the tarball's top directory).
#' @return Character vector of package names, base packages and R removed.
tarball_deps <- function(tarball, pkg) {
  tmp <- tempfile()
  dir.create(tmp)
  utils::untar(tarball, files = file.path(pkg, "DESCRIPTION"), exdir = tmp)
  desc <- read.dcf(file.path(tmp, pkg, "DESCRIPTION"))
  fields <- intersect(c("Depends", "Imports", "LinkingTo"), colnames(desc))
  raw <- unlist(strsplit(paste(desc[1, fields], collapse = ","), ","))
  names <- trimws(sub("\\(.*", "", raw))
  setdiff(names[nzchar(names)], c("R", base_pkgs))
}

#' Install one version of a pinned package from its CRAN tarball.
#'
#' Missing dependencies come from the dated snapshot. Any warning (including
#' "installation of package ... had non-zero exit status") is an error.
#'
#' @param pkg Package name.
#' @param version Version string.
#' @param url Tarball URL.
#' @return TRUE on success, FALSE on failure (logged).
install_one <- function(pkg, version, url) {
  message(sprintf("[install-pins] %s %s from %s", pkg, version, url))
  ok <- tryCatch(withCallingHandlers({
    tarball <- file.path(tempdir(), basename(url))
    utils::download.file(url, tarball, quiet = TRUE, mode = "wb")
    deps <- tarball_deps(tarball, pkg)
    missing <- setdiff(deps, c(rownames(installed.packages()), names(PINS)))
    if (length(missing)) {
      message(sprintf("[install-pins]   dependencies from snapshot %s: %s",
                      SNAPSHOT_DATE, paste(missing, collapse = ", ")))
      install.packages(missing, repos = SNAPSHOT)
    }
    install.packages(tarball, repos = NULL, type = "source")
    if (!identical(as.character(packageVersion(pkg, lib.loc = .libPaths()[1])), version)) {
      stop("installed version differs from the requested version")
    }
    TRUE
  }, warning = function(w) stop(conditionMessage(w))),
  error = function(e) {
    message(sprintf("[install-pins]   FAILED: %s", conditionMessage(e)))
    FALSE
  })
  attempt_log[[length(attempt_log) + 1L]] <<- data.frame(
    package = pkg, version = version, url = url, success = ok, stringsAsFactors = FALSE)
  ok
}

status <- character()
for (pkg in names(PINS)) {
  pin <- PINS[[pkg]]
  releases <- cran_releases(pkg)
  idx <- match(pin, releases$version)
  if (is.na(idx)) stop(sprintf("pinned %s %s is not a CRAN release", pkg, pin))
  # The version-search cap: the pin, then the preceding, then the following.
  order_idx <- c(idx, idx - 1L, idx + 1L)
  order_idx <- order_idx[order_idx >= 1L & order_idx <= nrow(releases)]
  done <- FALSE
  for (k in order_idx) {
    if (install_one(pkg, releases$version[k], releases$url[k])) {
      status[[pkg]] <- if (k == idx) "pinned" else "fallback"
      done <- TRUE
      break
    }
  }
  if (!done) stop(sprintf("no release of %s within the version-search cap builds", pkg))
}

# Final inventory: every package outside base R, with its classification.
ip <- installed.packages()
snapshot_avail <- available.packages(repos = SNAPSHOT)
inventory <- data.frame(package = rownames(ip), version = ip[, "Version"],
                        priority = ifelse(is.na(ip[, "Priority"]), "", ip[, "Priority"]),
                        libpath = ip[, "LibPath"], stringsAsFactors = FALSE)
inventory <- inventory[inventory$priority != "base", ]
inventory$status <- ifelse(inventory$package %in% names(status),
                           status[inventory$package],
                           ifelse(inventory$package %in% preinstalled,
                                  ifelse(inventory$priority == "recommended",
                                         "unspecified (shipped with R 4.3.2)",
                                         "unspecified (base image rocker/r-ver:4.3.2)"),
                                  "unspecified (snapshot 2024-04-03)"))
inventory$snapshot_version <- ifelse(inventory$package %in% rownames(snapshot_avail),
                                     snapshot_avail[match(inventory$package,
                                                          rownames(snapshot_avail)), "Version"],
                                     NA)
write.csv(inventory, "/opt/llmr/package-inventory.csv", row.names = FALSE)
write.csv(do.call(rbind, attempt_log), "/opt/llmr/pin-attempts.csv", row.names = FALSE)
print(inventory[order(inventory$status, inventory$package), ], row.names = FALSE)
print(do.call(rbind, attempt_log), row.names = FALSE)

# Assertions: every pin present at its version (or a logged fallback), and
# every snapshot-installed package at the snapshot's version.
for (pkg in names(PINS)) {
  got <- as.character(packageVersion(pkg))
  if (status[[pkg]] == "pinned" && got != PINS[[pkg]]) {
    stop(sprintf("%s is %s, pinned %s", pkg, got, PINS[[pkg]]))
  }
}
snap <- inventory[inventory$status == "unspecified (snapshot 2024-04-03)", ]
off <- snap[!is.na(snap$snapshot_version) & snap$version != snap$snapshot_version, ]
if (nrow(off)) {
  print(off, row.names = FALSE)
  stop("a snapshot-installed package differs from the snapshot's version")
}
message("[install-pins] all pins honoured: ",
        all(status == "pinned"), " (fallbacks: ", sum(status == "fallback"), ")")
