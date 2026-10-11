# Install the crema deposit's environment under amendment 3 §7(d) (v3).
#
# 1. Supplied pins take precedence, judged per dependency: every package
#    version the README's session info lists, attached or namespace-only, is
#    built at that version from CRAN's own source tarball.
# 2. A pin that cannot be retrieved or built is recorded, then the bounded
#    version search runs: the immediately preceding release, then the
#    immediately following one, stopping at the first that builds (at most
#    three attempts). Every attempt is logged with its stage and message.
# 3. Dependencies the session info does not list are unspecified, and are
#    installed at the release current at the article's first online
#    appearance (2024-03-16), from a Posit Package Manager snapshot of that
#    date. Which packages are needed is read from the pinned versions' own
#    DESCRIPTION files, not from later versions of the same packages.
# 4. The final inventory is asserted, and the build fails on any mismatch.
#
# v3 (2026-10-11) corrects two defects in v2:
#   - v2 read the release history from the base image's default repository,
#     a dated 2023-10-30 snapshot whose archive index is incomplete. It
#     missed rnaturalearth 0.3.4 to 1.1.0 and nimbleCarbon 0.2.5, so its
#     "following release" was wrong. v3 reads CRAN itself.
#   - v2 took dependencies and build order from the 2024-03-16 snapshot's
#     versions. rnaturalearth 0.3.3 imports sp, which its 2024 version does
#     not, so sp was built after it and 0.3.3's build failed. v3 reads each
#     pinned version's DESCRIPTION, and stops hiding build output.
#
# Inputs:  /build/pins.csv (package, version), parsed from the README.
# Outputs: /build/pin-attempts.csv and /build/pin-inventory.csv.

options(warn = 1, Ncpus = 1)
CRAN <- "https://cloud.r-project.org"
SNAPSHOT <- "https://packagemanager.posit.co/cran/__linux__/jammy/2024-03-16"
# Release listings must come from CRAN itself (see v3's first correction).
options(repos = c(CRAN = CRAN))
SRC <- "/build/src"
dir.create(SRC, showWarnings = FALSE)
FIELDS <- c("Depends", "Imports", "LinkingTo")

pins <- read.csv("/build/pins.csv", stringsAsFactors = FALSE, colClasses = "character")
ap_cran <- available.packages(repos = CRAN)
archive <- tools:::CRAN_archive_db()
ap_snap <- available.packages(repos = SNAPSHOT)
base_pkgs <- rownames(installed.packages(priority = "base"))

attempts <- data.frame(package = character(), version = character(), role = character(),
                       stage = character(), ok = logical(), message = character())
log_attempt <- function(pkg, ver, role, stage, msg) {
  attempts[nrow(attempts) + 1, ] <<- list(pkg, ver, role, stage, msg == "", substr(msg, 1, 300))
  cat(sprintf("[%s] %s %s (%s): %s\n", role, pkg, ver, stage, if (msg == "") "OK" else msg))
}

#' Every CRAN release of a package, oldest first: the archive plus the current version.
released <- function(pkg) {
  arch <- archive[[pkg]]
  v <- if (is.null(arch)) character() else
    sub(paste0("^", pkg, "_(.*)\\.tar\\.gz$"), "\\1", basename(rownames(arch)))
  if (pkg %in% rownames(ap_cran)) v <- c(v, ap_cran[pkg, "Version"])
  v <- unique(v)
  v[order(package_version(v))]
}

#' Download one version's source tarball from CRAN; return its path, or the failure.
fetch <- function(pkg, ver) {
  if (!ver %in% released(pkg))
    return(list(path = NULL, msg = "not in CRAN's release history (archive and current)"))
  current <-pkg %in% rownames(ap_cran) && ap_cran[pkg, "Version"] == ver
  url <- if (current) sprintf("%s/src/contrib/%s_%s.tar.gz", CRAN, pkg, ver) else
    sprintf("%s/src/contrib/Archive/%s/%s_%s.tar.gz", CRAN, pkg, pkg, ver)
  dest <- file.path(SRC, basename(url))
  msg <- tryCatch({ download.file(url, dest, mode = "wb", quiet = TRUE); "" },
                  error = function(e) conditionMessage(e),
                  warning = function(w) conditionMessage(w))
  if (msg == "") list(path = dest, msg = "") else
    list(path = NULL, msg = paste0("not retrievable from ", url, ": ", msg))
}

#' One row of package metadata from a source tarball's DESCRIPTION.
desc_row <- function(tarball, pkg) {
  tmp <- tempfile()
  untar(tarball, files = file.path(pkg, "DESCRIPTION"), exdir = tmp)
  read.dcf(file.path(tmp, pkg, "DESCRIPTION"), fields = c("Package", "Version", FIELDS))
}

# --- Resolve each pin to a retrievable tarball ----------------------------
# plan[[pkg]] holds the candidate versions in search order, how many have
# been tried, and the tarball currently selected.
plan <- list()
for (i in seq_len(nrow(pins))) {
  plan[[pins$package[i]]] <- list(cands = pins$version[i], roles = "supplied pin",
                                  tried = 0L, tarball = NULL, version = NA_character_,
                                  role = NA_character_, note = "", built = FALSE)
}

#' Select the next retrievable candidate for a pin; FALSE when the search is exhausted.
next_tarball <- function(pkg) {
  st <- plan[[pkg]]
  repeat {
    if (st$tried == 1L && length(st$cands) == 1L) {
      # The supplied pin failed: open the bounded search around it.
      rel <- released(pkg)
      ver <- st$cands[1]
      below <- rel[package_version(rel) < package_version(ver)]
      above <- rel[package_version(rel) > package_version(ver)]
      st$cands <- c(ver, tail(below, 1), head(above, 1))
      st$roles <- c("supplied pin",
                    if (length(below)) "fallback: preceding release",
                    if (length(above)) "fallback: following release")
      st$note <- paste("released:", paste(rel, collapse = " "))
      cat("  ", pkg, st$note, "\n")
    }
    if (st$tried >= length(st$cands)) {
      st$tarball <- NULL
      plan[[pkg]] <<- st
      return(FALSE)
    }
    st$tried <- st$tried + 1L
    ver <- st$cands[st$tried]
    role <- st$roles[st$tried]
    got <- fetch(pkg, ver)
    if (is.null(got$path)) {
      log_attempt(pkg, ver, role, "retrieve", got$msg)
      next
    }
    st$tarball <- got$path
    st$version <- ver
    st$role <- role
    plan[[pkg]] <<- st
    return(TRUE)
  }
}
for (pkg in names(plan)) next_tarball(pkg)

# --- Dependency metadata: pinned versions' own, snapshot for the rest ------
resolved <- Filter(function(p) !is.null(plan[[p]]$tarball), names(plan))
pinned_rows <- do.call(rbind, lapply(resolved, function(p) desc_row(plan[[p]]$tarball, p)))
db <- rbind(ap_snap[!rownames(ap_snap) %in% pins$package, c("Package", "Version", FIELDS)],
            pinned_rows)
rownames(db) <- db[, "Package"]

# --- Unspecified dependencies, at the publication anchor -------------------
needed <- unique(unlist(tools::package_dependencies(resolved, db = db, which = FIELDS,
                                                    recursive = TRUE)))
unspecified <- sort(setdiff(needed, c(pins$package, base_pkgs)))
absent <- setdiff(unspecified, rownames(ap_snap))
if (length(absent)) stop("not in the 2024-03-16 snapshot: ", paste(absent, collapse = ", "))
cat("Unspecified dependencies:", paste(unspecified, collapse = ", "), "\n")
if (length(unspecified)) install.packages(unspecified, repos = SNAPSHOT, dependencies = FALSE)

# --- Supplied pins, in the pinned versions' dependency order --------------
deps <- tools::package_dependencies(resolved, db = db, which = FIELDS)
ordered <- character()
visit <- function(p, stack = character()) {
  if (p %in% ordered || p %in% stack || !(p %in% resolved)) return(invisible())
  for (d in deps[[p]]) visit(d, c(stack, p))
  ordered <<- c(ordered, p)
}
for (p in resolved) visit(p)

#' Build the selected tarball and verify the installed version; TRUE on success.
build <- function(pkg) {
  st <- plan[[pkg]]
  msg <- tryCatch(withCallingHandlers({
    install.packages(st$tarball, repos = NULL, type = "source")
    got <- utils::packageDescription(pkg, lib.loc = .libPaths()[1], fields = "Version")
    if (is.na(got) || package_version(got) != package_version(st$version))
      stop("installed version is ", got)
    ""
  }, warning = function(w) {
    # install.packages reports a failed build only as a warning.
    if (grepl("non-zero exit status", conditionMessage(w))) stop(conditionMessage(w))
  }), error = function(e) conditionMessage(e))
  log_attempt(pkg, st$version, st$role, "build", msg)
  msg == ""
}

#' Install, from the snapshot, any dependency a fallback version adds.
add_fallback_deps <- function(pkg) {
  row <- desc_row(plan[[pkg]]$tarball, pkg)
  rownames(row) <- pkg
  new <- setdiff(tools::package_dependencies(pkg, db = row, which = FIELDS)[[pkg]],
                 c(rownames(installed.packages()), base_pkgs))
  if (length(new)) {
    cat("  ", pkg, plan[[pkg]]$version, "adds unspecified:", paste(new, collapse = ", "), "\n")
    install.packages(new, repos = SNAPSHOT, dependencies = FIELDS)
    unspecified <<- sort(unique(c(unspecified, new)))
  }
}

for (pkg in ordered) {
  repeat {
    if (build(pkg)) {
      plan[[pkg]]$built <- TRUE
      break
    }
    if (!next_tarball(pkg)) break
    add_fallback_deps(pkg)
  }
}
write.csv(attempts, "/build/pin-attempts.csv", row.names = FALSE)

# --- Final inventory -------------------------------------------------------
inst <- function(p) utils::packageDescription(p, fields = "Version")
same <- function(a, b) !is.na(a) & !is.na(b) &
  mapply(function(x, y) package_version(x) == package_version(y), a, b)
chosen <- vapply(pins$package, function(p)
  if (isTRUE(plan[[p]]$built)) plan[[p]]$version else NA_character_, character(1))
inv_pins <- data.frame(
  package = pins$package, supplied = pins$version,
  installed = vapply(pins$package, inst, character(1)), status = "",
  note = vapply(pins$package, function(p) plan[[p]]$note, character(1)))
inv_pins$status <- ifelse(same(inv_pins$installed, inv_pins$supplied), "pin honoured",
  ifelse(same(inv_pins$installed, chosen), "fallback (see attempts)", "MISMATCH"))
inv_unspec <- data.frame(
  package = unspecified, supplied = "", installed = vapply(unspecified, inst, character(1)),
  status = "unspecified: snapshot 2024-03-16", note = "")
inventory <- rbind(inv_pins, inv_unspec)
write.csv(inventory, "/build/pin-inventory.csv", row.names = FALSE)
print(table(inventory$status))
print(inventory[!inventory$status %in% c("pin honoured", "unspecified: snapshot 2024-03-16"), ])
stopifnot(!any(is.na(inventory$installed)), all(inventory$status != "MISMATCH"))
