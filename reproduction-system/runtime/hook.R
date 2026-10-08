# Reproduction lane hook (gate 1.3: handshake and loader tracing).
#
# run-container makes this the user profile of every R process in a run:
# R_PROFILE_USER points here, the lane's R_ENVIRON_USER file pins that
# variable (a project .Renviron would otherwise displace it; spec, probe
# fact 1), and the .Rprofile the lane injects into the work copy sources it
# for children that read the working directory's profile instead.
#
# Events (spec §8), one line each to PID 1's stderr, the Docker log pipe held
# on the host, under the 4,096-byte atomic-write limit:
#   LANE1 <nonce> <token> <pid> <ppid> <seq> <event> <tab> fields...
#
#   START  once, as the profile runs: hook version, working directory, the
#          start-up variables, the site files' md5, whether R will restore a
#          saved workspace, and argv.
#   LOAD   a file R loads: function, resolved path, md5, size, depth, and the
#          seq of the enclosing LOAD (0 at the top). Emitted for the script
#          named on the command line ("file"), the user profile ("profile"),
#          source(), sys.source(), parse(file =), and, when their packages
#          load, knitr::knit, rmarkdown::render, Rcpp::sourceCpp,
#          pkgload::load_all, reticulate::source_python and py_run_file,
#          box::use, and modules::import.
#   TEXT   code evaluated from a string, parse(text =) or a -e expression: the
#          md5 of the text joined by newlines and ending in one, its length
#          in bytes, depth, and enclosing seq. An -e expression is decoded as
#          R decodes it (~+~, ~n~, ~t~) first. Repeats of one md5 in one
#          process are counted, not logged again; END carries the count.
#   CONN   source() or parse() of a connection or of expressions: the
#          function, class, and description, depth, enclosing seq, and the
#          calling function (namespace::name when verified as that
#          namespace's own). A path hash does not cover such content, so the
#          gate makes it an obligation, unless R's NAMESPACE parser read it.
#   PKG    a namespace load: name, version, library path, the DESCRIPTION's
#          Repository, RemoteType, RemoteSha, and Packaged fields, and the
#          DESCRIPTION's md5. Once per package per process.
#   FORK   first, in a forked child (parallel::mclapply), with the parent's
#          token and the seq of the parent's innermost active load (0 at the
#          top). The child's events inside that load nest under the FORK.
#   END    from an exit finaliser when the process ends normally, or, in a
#          forked child, from a trace on parallel:::mcexit, which every
#          mclapply and mcparallel child calls before it leaves through _exit.
#          Field: the number of suppressed TEXT repeats.
#   HOOKERR a tracer failed: the function and the message. A load may then
#          have gone unlogged, so the gate treats it as an error.
#
# The traces are installed BEFORE the user profile is sourced, or loads made
# inside it (renv's activate.R) would go unlogged (Fable's specification
# review, D-1). trace() rewrites the traced functions in their namespaces; its
# messages go to stderr and are suppressed, and its return values are made
# invisible so that nothing reaches stdout. A tracer runs in the traced
# function's own frame; it only calls into the hook through an option, so it
# leaves no variable behind in that frame. Nesting is read from the call
# stack at entry, by frame identity and sys.parents(), because exit tracers
# do not fire reliably (2026-10-06 probe).
#
# The token is the one the exec shim minted for this process, so the census
# pairs EXEC and START on it rather than on a PID that can repeat. Strings
# are hex-encoded UTF-8. The hook keeps its state out of the global
# environment and the search path, never touches .Random.seed (its own
# randomness comes from /dev/urandom), and writes nothing to stdout
# (semantics neutrality, spec §8). If the stream cannot be written, the
# process stops rather than run unrecorded.

local({
    if (isTRUE(getOption("lane.hook.loaded"))) {
        return(invisible(NULL))
    }
    options(lane.hook.loaded = TRUE)
    hook_env <- environment()

    hex <- function(x) {
        vapply(x, function(s) {
            paste(as.character(charToRaw(enc2utf8(as.character(s)))), collapse = "")
        }, character(1), USE.NAMES = FALSE)
    }
    fresh_token <- function() {
        # raw = TRUE: /dev/urandom is not a regular file, and R 4.3 warns
        # otherwise, which would reach the analysis (options(warn = 2)).
        random <- tryCatch({
            con <- file("/dev/urandom", open = "rb", raw = TRUE)
            on.exit(close(con), add = TRUE)
            readBin(con, "raw", 8L)
        }, error = function(e) raw(0), warning = function(w) raw(0))
        paste0(Sys.getpid(), "-r", paste(as.character(random), collapse = ""))
    }

    state <- new.env(parent = baseenv())
    state$version <- "1.4-inst"
    # The run's nonce, or, where the environment was cleared, the lane's copy.
    state$nonce <- Sys.getenv("LANE_RUN_NONCE", "")
    if (!nzchar(state$nonce)) {
        state$nonce <- tryCatch(readLines("/lane/nonce", n = 1L, warn = FALSE),
                                error = function(e) "none", warning = function(w) "none")
        if (length(state$nonce) != 1L || !nzchar(state$nonce)) state$nonce <- "none"
    }
    state$seq <- 0L
    state$pid <- Sys.getpid()
    # The shim's token, if the shim started this very process; otherwise R
    # started outside the front end, and the hook mints its own.
    state$token <- if (identical(Sys.getenv("LANE_PROC_PID"), as.character(state$pid))) {
        Sys.getenv("LANE_PROC")
    } else {
        fresh_token()
    }
    state$loads <- list()          # active LOADs: list(env = <frame>, seq = <seq>)
    state$text_seen <- new.env(parent = emptyenv())
    state$text_repeats <- 0L
    state$pkg_seen <- new.env(parent = emptyenv())
    state$in_pkg <- FALSE          # re-entrancy guard for the loadNamespace tracer
    state$ended <- FALSE

    parent_pid <- function() {
        # Field 4 of /proc/self/stat, counted after the parenthesised command
        # name (which may itself contain spaces).
        stat <- tryCatch(readLines("/proc/self/stat", warn = FALSE), error = function(e) "")
        rest <- sub("^.*\\) ", "", stat[1])
        fields <- strsplit(rest, " ", fixed = TRUE)[[1]]
        if (length(fields) >= 2) fields[2] else "0"
    }

    is_file <- function(path) {
        length(path) == 1L && !is.na(path) && file.exists(path) && !dir.exists(path)
    }
    md5_or_none <- function(path) if (is_file(path)) unname(tools::md5sum(path)) else "none"
    size_or_none <- function(path) if (is_file(path)) as.character(file.size(path)) else "none"
    resolved <- function(path) {
        tryCatch(normalizePath(path, mustWork = FALSE), error = function(e) as.character(path))
    }
    text_md5 <- function(joined) {
        # tools::md5sum hashes files only (R 4.3), so the text is written with
        # one final newline; the gate hashes chunks the same way.
        tmp <- tempfile("lane-text-")
        on.exit(unlink(tmp), add = TRUE)
        writeLines(joined, tmp, useBytes = TRUE)
        unname(tools::md5sum(tmp))
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
        # Fields are computed first: computing them can itself trace an event
        # (tools::md5sum loads a namespace), which must take its number and
        # be written before this one.
        force(fields)
        check_fork()
        state$seq <- state$seq + 1L
        write_line(event, fields)
        state$seq
    }

    emit_end <- function() {
        if (!state$ended) {
            state$ended <- TRUE
            emit("END", as.character(state$text_repeats))
        }
    }

    # -- Nesting -----------------------------------------------------------
    # A tracer runs in the traced function's own frame and hands that frame
    # to the hook. Active loads are those whose frame environment is still
    # on the stack; the innermost is the enclosing one. Frame identity and
    # sys.parents() are used rather than frame arithmetic, because the
    # tracer's own eval frames sit between the loader and this code.
    frame_index <- function(env, frames) {
        for (i in seq_along(frames)) {
            if (identical(frames[[i]], env)) return(i)
        }
        0L
    }
    caller_of <- function(env) {
        # The frame that called the function whose frame is `env`, or NULL at
        # the top level.
        frames <- sys.frames()
        parents <- sys.parents()
        i <- frame_index(env, frames)
        if (i > 0L && parents[i] > 0L) frames[[parents[i]]] else NULL
    }
    active_loads <- function() {
        # The recorded loads whose frames are still on the stack, with each
        # frame's position.
        frames <- sys.frames()
        active <- list()
        for (entry in state$loads) {
            index <- frame_index(entry$env, frames)
            if (index > 0L) {
                active[[length(active) + 1L]] <- list(index = index, seq = entry$seq,
                                                      env = entry$env)
            }
        }
        active
    }
    innermost_seq <- function(active) {
        if (length(active) == 0L) return(0L)
        active[[which.max(vapply(active, function(a) a$index, integer(1)))]]$seq
    }
    check_fork <- function() {
        # A forked child (parallel::mclapply) inherits this state. Before its
        # first event it takes its own token and sequence, and its FORK says
        # whose fork it is and where in the parent it was made: the seq of
        # the parent's innermost active load. The parent's frames are still on
        # the child's stack, so its active loads stay active in the child,
        # renumbered to the FORK: a load the child makes inside the parent's
        # knit nests under the FORK, which the gate follows to the parent's
        # load. This runs before any nesting is taken, so no child event names
        # a parent's seq.
        if (Sys.getpid() == state$pid) return(invisible(NULL))
        active <- active_loads()
        parent <- state$token
        state$pid <- Sys.getpid()
        state$token <- fresh_token()
        state$seq <- 1L
        state$loads <- lapply(active, function(a) list(env = a$env, seq = 1L))
        state$ended <- FALSE
        write_line("FORK", c(parent, as.character(innermost_seq(active))))
    }
    nesting <- function() {
        check_fork()
        active <- active_loads()
        state$loads <- lapply(active, function(a) list(env = a$env, seq = a$seq))
        list(depth = length(active), enclosing = innermost_seq(active))
    }
    called_from_load <- function(frame) {
        # Whether the function in `frame` was called directly by an active
        # load: parse() inside source() is source()'s own mechanics.
        caller <- caller_of(frame)
        if (is.null(caller)) return(FALSE)
        for (entry in state$loads) {
            if (identical(entry$env, caller)) return(TRUE)
        }
        FALSE
    }

    on_load <- function(fn, path, frame) {
        nest <- nesting()
        path <- resolved(path)
        seq <- emit("LOAD", c(hex(fn), hex(path), md5_or_none(path), size_or_none(path),
                              as.character(nest$depth), as.character(nest$enclosing)))
        if (!is.null(frame)) {
            state$loads[[length(state$loads) + 1L]] <- list(env = frame, seq = seq)
        }
        invisible(seq)
    }
    on_text <- function(text) {
        joined <- paste(as.character(text), collapse = "\n")
        md5 <- text_md5(joined)
        if (exists(md5, envir = state$text_seen, inherits = FALSE)) {
            state$text_repeats <- state$text_repeats + 1L
            return(invisible(NULL))
        }
        assign(md5, TRUE, envir = state$text_seen)
        nest <- nesting()
        emit("TEXT", c(md5, as.character(nchar(joined, type = "bytes") + 1L),
                       as.character(nest$depth), as.character(nest$enclosing)))
    }
    caller_label <- function(frame) {
        # The function that called the loader whose frame is `frame`, as
        # namespace::name only when that function object is the namespace's
        # own binding of the name (so a look-alike defined elsewhere does not
        # pass as base::parseNamespaceFile); otherwise its bare name.
        caller <- caller_of(frame)
        if (is.null(caller)) return("top level")
        index <- frame_index(caller, sys.frames())
        if (index < 1L) return("unknown")
        call <- sys.call(index)
        name <- sub("^.*:::?", "", paste(deparse(call[[1L]]), collapse = ""))
        fun <- sys.function(index)
        owner <- environment(fun)
        if (!is.null(owner) && isNamespace(owner) &&
                exists(name, envir = owner, inherits = FALSE) &&
                identical(get(name, envir = owner, inherits = FALSE), fun)) {
            return(paste0(getNamespaceName(owner), "::", name))
        }
        name
    }
    on_conn <- function(fn, what, frame) {
        nest <- nesting()
        description <- if (inherits(what, "connection")) {
            tryCatch(summary(what)$description, error = function(e) "unknown")
        } else {
            "expressions"
        }
        emit("CONN", c(hex(fn), hex(class(what)[1]), hex(description),
                       as.character(nest$depth), as.character(nest$enclosing),
                       hex(caller_label(frame))))
    }
    on_pkg <- function(package, lib.loc) {
        name <- as.character(package)[1]
        if (is.na(name) || !nzchar(name) ||
                exists(name, envir = state$pkg_seen, inherits = FALSE)) {
            return(invisible(NULL))
        }
        assign(name, TRUE, envir = state$pkg_seen)
        path <- tryCatch(find.package(name, lib.loc, quiet = TRUE),
                         error = function(e) character())
        if (length(path) == 0L) {
            path <- tryCatch(find.package(name, quiet = TRUE), error = function(e) character())
        }
        if (length(path) == 0L) {
            emit("PKG", c(hex(name), "none", "none", "none", "none", "none", "none", "none"))
            return(invisible(NULL))
        }
        description <- file.path(path[1], "DESCRIPTION")
        fields <- tryCatch(read.dcf(description, fields = c("Version", "Repository",
                                                              "RemoteType", "RemoteSha",
                                                              "Packaged"))[1, ],
                           error = function(e) rep(NA_character_, 5L))
        field <- function(i) if (is.na(fields[[i]])) "none" else hex(fields[[i]])
        # The library as an absolute path: lib.loc may be relative ("lib"),
        # and the gate places the package's own files by it.
        library <- normalizePath(dirname(path[1]), mustWork = FALSE)
        emit("PKG", c(hex(name), field(1), hex(library), field(2), field(3),
                      field(4), field(5), md5_or_none(description)))
    }

    # -- The tracers' entry points ------------------------------------------
    # Each takes the traced function's frame and the arguments it needs, and
    # never errors: a tracer that errors would break the analysis, so a
    # failure is reported as HOOKERR and the call continues.
    guard <- function(fn, expr) {
        tryCatch(expr, error = function(e) {
            emit("HOOKERR", c(hex(fn), hex(conditionMessage(e))))
        })
    }
    api <- new.env(parent = baseenv())
    api$source <- function(frame, exprs, file) guard("source", {
        if (!is.null(exprs)) {
            on_conn("source", exprs, frame)
        } else if (is.character(file)) {
            on_load("source", file, frame)
        } else {
            on_conn("source", file, frame)
        }
    })
    api$sys_source <- function(frame, file) guard("sys.source", {
        if (identical(caller_of(frame), hook_env)) {
            # The hook's own load of the user profile was logged as "profile"
            # just before; its frame still counts as that load, so the parse()
            # inside it is mechanics and not a second LOAD.
            state$loads[[length(state$loads) + 1L]] <- list(env = frame, seq = state$seq)
        } else {
            on_load("sys.source", file, frame)
        }
    })
    api$parse <- function(frame, text, file) guard("parse", {
        if (!called_from_load(frame)) {
            if (!is.null(text)) {
                on_text(text)
            } else if (is.character(file) && length(file) == 1L && nzchar(file)) {
                on_load("parse", file, frame)
            } else if (inherits(file, "connection")) {
                on_conn("parse", file, frame)
            }
        }
    })
    api$load_namespace <- function(frame, package, lib.loc) guard("loadNamespace", {
        # The guard stops the tracer's own calls (find.package, read.dcf)
        # from recursing; it is reset before returning so that the imports
        # loadNamespace itself loads next are still seen.
        if (!isTRUE(state$in_pkg)) {
            state$in_pkg <- TRUE
            tryCatch(on_pkg(package, lib.loc), finally = state$in_pkg <- FALSE)
        }
        # The sys.source() of a package's lazy-load stub is loadNamespace's
        # own mechanics, not a load of the authors' code: its frame counts as
        # the PKG event, so loads made directly from it are skipped and loads
        # inside package code (an .onLoad that sources a file) nest under it.
        state$loads[[length(state$loads) + 1L]] <- list(env = frame, seq = state$seq)
    })
    api$load <- function(fn, frame, path) guard(fn, on_load(fn, path, frame))
    api$text <- function(fn, text) guard(fn, on_text(text))
    api$end <- emit_end
    options(lane.hook = api)

    # -- Traces ------------------------------------------------------------
    install <- function(what, where, tracer) {
        ok <- tryCatch({
            invisible(suppressMessages(trace(what, where = where, tracer = tracer,
                                             print = FALSE)))
            TRUE
        }, error = function(e) FALSE)
        if (!ok) emit("HOOKERR", c(hex(paste0("trace:", what)), hex("install failed")))
        invisible(ok)
    }
    for (dependency in c("methods", "tools")) {
        if (!dependency %in% loadedNamespaces()) suppressMessages(loadNamespace(dependency))
    }
    base_ns <- baseenv()
    install("source", base_ns, quote(getOption("lane.hook")$source(
        environment(), if (missing(exprs)) NULL else exprs, if (missing(file)) NULL else file)))
    install("sys.source", base_ns, quote(getOption("lane.hook")$sys_source(
        environment(), file)))
    install("parse", base_ns, quote(getOption("lane.hook")$parse(
        environment(), if (missing(text)) NULL else text, if (missing(file)) NULL else file)))
    install("loadNamespace", base_ns, quote(getOption("lane.hook")$load_namespace(
        environment(), package, if (missing(lib.loc)) NULL else lib.loc)))

    # Package-conditional traces, installed when the package loads (or now,
    # if it already has).
    on_package <- function(package, what, tracer) {
        setHook(packageEvent(package, "onLoad"), function(...) {
            install(what, asNamespace(package), tracer)
        })
        if (package %in% loadedNamespaces()) install(what, asNamespace(package), tracer)
    }
    on_package("parallel", "mcexit", quote(getOption("lane.hook")$end()))
    on_package("knitr", "knit", quote(
        if (!missing(input) && is.character(input)) {
            getOption("lane.hook")$load("knitr::knit", environment(), input)
        } else if (!missing(text) && !is.null(text)) {
            getOption("lane.hook")$text("knitr::knit", text)
        }))
    on_package("rmarkdown", "render", quote(
        if (!missing(input) && is.character(input)) {
            getOption("lane.hook")$load("rmarkdown::render", environment(), input)
        }))
    on_package("Rcpp", "sourceCpp", quote(
        if (!missing(file) && is.character(file) && nzchar(file)) {
            getOption("lane.hook")$load("Rcpp::sourceCpp", environment(), file)
        } else if (!missing(code) && !is.null(code)) {
            getOption("lane.hook")$text("Rcpp::sourceCpp", code)
        }))
    on_package("pkgload", "load_all", quote(
        getOption("lane.hook")$load("pkgload::load_all", environment(), path)))
    on_package("reticulate", "source_python", quote(
        getOption("lane.hook")$load("reticulate::source_python", environment(), file)))
    on_package("reticulate", "py_run_file", quote(
        getOption("lane.hook")$load("reticulate::py_run_file", environment(), file)))
    on_package("box", "use", quote(
        getOption("lane.hook")$load("box::use", environment(),
                                    paste(deparse(sys.call()), collapse = " "))))
    on_package("modules", "import", quote(
        getOption("lane.hook")$load("modules::import", environment(),
                                    paste(deparse(sys.call()), collapse = " "))))

    # -- Handshake ---------------------------------------------------------
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
    reg.finalizer(state, function(e) emit_end(), onexit = TRUE)

    # The code named on the command line is a LOAD that no source() call
    # covers: Rscript's --file=, and R's own -f and --file, which reach R
    # unrewritten (2026-10-08 probe: callr starts R -f, and commandArgs()
    # shows "-f", path). Each -e expression is a TEXT. Options end at
    # --args; what follows is the script's own arguments.
    #
    # R's front end escapes an -e expression's spaces, newlines, and tabs as
    # ~+~, ~n~, and ~t~ (bin/R lines 195-196 in rocker/r-ver:4.3.2), and R's
    # start-up decodes them, scanning left to right, before it evaluates the
    # code; commandArgs() shows the escaped form. The TEXT is the code R
    # evaluated, so it is decoded the same way. The 2026-10-08 probe showed a
    # typed "~+~" decodes too, and "~n~+~" gives a newline, then "+~".
    unescape_e <- function(x) {
        hits <- gregexpr("~[+nt]~", x)
        regmatches(x, hits) <- lapply(regmatches(x, hits), function(found) {
            unname(c("~+~" = " ", "~n~" = "\n", "~t~" = "\t")[found])
        })
        x
    }
    options_end <- match("--args", args, nomatch = length(args) + 1L) - 1L
    opts <- args[seq_len(options_end)]
    scripts <- sub("^--file=", "", grep("^--file=", opts, value = TRUE))
    for (i in which(opts %in% c("-f", "--file"))) {
        if (i < length(opts)) scripts <- c(scripts, opts[i + 1L])
    }
    for (path in scripts) {
        on_load("file", path, NULL)
    }
    for (i in which(opts == "-e")) {
        if (i < length(opts)) on_text(unescape_e(opts[i + 1L]))
    }

    # R reads one user profile: R_PROFILE_USER if set, else the working
    # directory's .Rprofile, else ~/.Rprofile. The lane's Renviron saves any
    # R_PROFILE_USER the process inherited (callr's bootstrap profile, or one a
    # project .Renviron names) as LANE_PARENT_PROFILE before pinning the hook,
    # so the hook sources that first; otherwise it does what R would have
    # done. The lane renames a project-root .Rprofile to .Rprofile.project, so
    # that its own injected .Rprofile can stand there. The profile is sourced
    # into the global environment, where R evaluates a user profile. The
    # traces above are already in place, so loads inside it are logged.
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
            on_load("profile", normalizePath(path), hook_env)
            sys.source(path, envir = globalenv(), keep.source = FALSE)
            break
        }
    }
})
