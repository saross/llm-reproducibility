# Reproduction lane hook (gate 1.3, F1: handshake only).
#
# run-container makes this the user profile of every R process in a run:
# R_PROFILE_USER points here, the lane's R_ENVIRON_USER file pins that
# variable (a project .Renviron would otherwise displace it; spec, probe
# fact 1), and the .Rprofile the lane injects into the work copy sources it
# for children that read the working directory's profile instead.
#
# F1 emits the per-process handshake the process census needs (spec §8):
#   START  once, as the profile runs: hook version, working directory, the
#          start-up variables, the site files' md5, whether R will restore a
#          saved workspace, and argv;
#   LOAD   for the user profile the hook sources in R's place;
#   FORK   first, in a forked child (parallel::mclapply), with the parent's
#          token;
#   END    from an exit finaliser, when the process ends normally.
# Loader tracing (LOAD for source() and friends, TEXT, CONN, PKG) comes in
# the instrumentation stage. Its traces must be installed BEFORE the user
# profile is sourced, or loads made inside it (renv's activate.R) go
# unlogged (Fable's specification review, D-1).
#
# Events go to PID 1's stderr, the Docker log pipe held on the host, one line
# each, under the 4,096-byte atomic-write limit:
#   LANE1 <nonce> <token> <pid> <ppid> <seq> <event> <tab> fields...
# The token is the one the exec shim minted for this process, so the census
# pairs EXEC and START on it rather than on a PID that can repeat. Strings are
# hex-encoded UTF-8. The hook keeps its state out of the global environment
# and the search path, never touches .Random.seed (its own randomness comes
# from /dev/urandom), and writes nothing to stdout (semantics neutrality,
# spec §8). If the stream cannot be written, the process stops rather than
# run unrecorded.

local({
    if (isTRUE(getOption("lane.hook.loaded"))) {
        return(invisible(NULL))
    }
    options(lane.hook.loaded = TRUE)

    hex <- function(x) {
        vapply(x, function(s) {
            paste(as.character(charToRaw(enc2utf8(as.character(s)))), collapse = "")
        }, character(1), USE.NAMES = FALSE)
    }
    fresh_token <- function() {
        random <- tryCatch(readBin("/dev/urandom", "raw", 8L), error = function(e) raw(0))
        paste0(Sys.getpid(), "-r", paste(as.character(random), collapse = ""))
    }

    state <- new.env(parent = baseenv())
    state$version <- "1.0-f1"
    state$nonce <- Sys.getenv("LANE_RUN_NONCE", "none")
    state$seq <- 0L
    state$pid <- Sys.getpid()
    # The shim's token, if the shim started this very process; otherwise R
    # started outside the front end, and the hook mints its own.
    state$token <- if (identical(Sys.getenv("LANE_PROC_PID"), as.character(state$pid))) {
        Sys.getenv("LANE_PROC")
    } else {
        fresh_token()
    }

    parent_pid <- function() {
        # Field 4 of /proc/self/stat, counted after the parenthesised command
        # name (which may itself contain spaces).
        stat <- tryCatch(readLines("/proc/self/stat", warn = FALSE), error = function(e) "")
        rest <- sub("^.*\\) ", "", stat[1])
        fields <- strsplit(rest, " ", fixed = TRUE)[[1]]
        if (length(fields) >= 2) fields[2] else "0"
    }

    md5_or_none <- function(path) {
        if (file.exists(path)) unname(tools::md5sum(path)) else "none"
    }

    write_line <- function(event, fields) {
        line <- paste0(sprintf("LANE1 %s %s %d %s %d %s", state$nonce, state$token,
                               Sys.getpid(), parent_pid(), state$seq, event),
                       paste0("\t", fields, collapse = ""), "\n")
        # raw = TRUE: the target is a pipe, and R would otherwise warn and
        # switch to raw mode itself. A real failure is an error or warning.
        ok <- tryCatch({
            con <- file("/proc/1/fd/2", open = "a", raw = TRUE)
            on.exit(close(con), add = TRUE)
            cat(line, file = con)
            TRUE
        }, error = function(e) FALSE, warning = function(w) FALSE)
        if (!ok) {
            message("lane hook: the event stream is not writable; stopping")
            quit(save = "no", status = 125, runLast = FALSE)
        }
    }

    emit <- function(event, fields = character()) {
        if (Sys.getpid() != state$pid) {
            # A forked child inherits this state: give it its own token and
            # sequence, and say whose fork it is.
            parent <- state$token
            state$pid <- Sys.getpid()
            state$token <- fresh_token()
            state$seq <- 1L
            write_line("FORK", parent)
        }
        state$seq <- state$seq + 1L
        write_line(event, fields)
    }

    args <- commandArgs(trailingOnly = FALSE)
    restore <- file.exists(".RData") &&
        !any(args %in% c("--no-restore", "--no-restore-data", "--vanilla"))
    emit("START", c(
        hex(state$version),
        hex(getwd()),
        hex(Sys.getenv("R_PROFILE_USER")),
        hex(Sys.getenv("R_ENVIRON_USER")),
        md5_or_none(file.path(R.home("etc"), "Rprofile.site")),
        md5_or_none(file.path(R.home("etc"), "Renviron.site")),
        if (restore) "restore" else "no-restore",
        hex(args)
    ))
    reg.finalizer(state, function(e) emit("END"), onexit = TRUE)

    # R reads one user profile: R_PROFILE_USER if set, else the working
    # directory's .Rprofile, else ~/.Rprofile. The lane's Renviron saves any
    # R_PROFILE_USER the process inherited (callr's bootstrap profile, or one a
    # project .Renviron names) as LANE_PARENT_PROFILE before pinning the hook,
    # so the hook sources that first; otherwise it does what R would have
    # done. The lane renames a project-root .Rprofile to .Rprofile.project, so
    # that its own injected .Rprofile can stand there. The profile is sourced
    # into the global environment, where R evaluates a user profile.
    is_lane_file <- function(path) {
        identical(normalizePath(path, mustWork = FALSE),
                  normalizePath("/lane/hook.R", mustWork = FALSE)) ||
            (file.exists(path) && !dir.exists(path) &&
                 identical(readLines(path, n = 1L, warn = FALSE),
                           "# reproduction lane profile"))
    }
    inherited <- Sys.getenv("LANE_PARENT_PROFILE")
    candidates <- if (nzchar(inherited) && !is_lane_file(inherited)) {
        inherited
    } else {
        c(".Rprofile.project", ".Rprofile", path.expand("~/.Rprofile"))
    }
    for (path in candidates) {
        if (file.exists(path) && !dir.exists(path) && !is_lane_file(path)) {
            emit("LOAD", c(hex("profile"), hex(normalizePath(path)), md5_or_none(path),
                           as.character(file.size(path)), "0", "0"))
            sys.source(path, envir = globalenv(), keep.source = FALSE)
            break
        }
    }
})
