---
title: "Reproduction lane gate 1.3 — execution provenance and conversion checks (design)"
tags: [reproduction, validation, mechanical-verification]
created: 2026-10-05
updated: 2026-10-05
status: draft-for-review
---

# Reproduction lane gate 1.3: design

**Status: draft for second opinions** (Astra, GPT in Codex, and Fable, a
Claude session) before building. It responds to the Fable review of PR #7
(`~/agent-mail/claude/outbox/claude/20261005T044136.617510Z-claude-pr7-fable-review-reply.md`)
and Astra's two reviews of PR #7.

## Decisions already taken (Shawn, 2026-10-05)

- **Build the lane-owned run command now** (Fable's build 3), with the
  **writable-copy design**: the authors' originals are never writable during
  a run; the run works in a lane-made copy; a loader log is the primary
  guarantee of what ran.
- **Conversions: the lane does the comparison** (option C, hybrid). The lane
  compares CSV, TSV, and Excel files itself. An exact match after stated
  normalisation clears the flag, and anything else is flagged.
- **Fix every P1, P2, and P3 finding** from the Fable review, and build
  Fable's builds 1 (transcript ordering audit) and 2 (whole-tree inventory).
- **Class (ii) has a consequence** (amendment 3 §7(d)): a result resting on
  an authors' file edited for mechanics counts only after a wrapper-only
  re-run.

## Threat model

The executor is a language model with write access to its attempt
directory. It acts in good faith but is prone to helpful repairs and
rationalised shortcuts, and it may not declare them. It is not a determined
adversary able to forge cryptographic material. The goal is that executing
anything other than the authors' original code either **fails the gate** or
**raises a flag that needs a recorded human ruling**, and that defeating the
checks requires deliberate, multi-step forgery that the transcript audit or
the reviewer can see.

## 1. `run-container`: lane-owned execution

`reproduction-lane.py run-container <attempt> --image TAG --entry FILE`
replaces the executor's own `docker run`. Each call is one numbered run with
its record in `execution-runs/run-NN/`.

1. **Pre snapshot.** The lane hashes every regular file in the attempt tree
   (not only code), refusing directory symlinks and symlinks that resolve
   outside the tree.
2. **Work copy.** The lane copies the attempt directory, except `outputs/`,
   to a work directory outside it (`--work-root`, default the system temp).
   The originals are never mounted, so nothing in the container can write to
   them.
3. **Mounts:**
   - the work copy, read-write, at `/project`;
   - `<attempt>/outputs`, read-write, at `/project/outputs`;
   - the lane's hook directory, read-only, at `/lane`;
   - the run record directory, read-write, at `/lane-log`.

   The flags are `--network none` and `--user uid:gid`, and
   `-e R_PROFILE_USER=/lane/hook.R` loads the hook. `R_PROFILE` is not
   overridden, so an image's `Rprofile.site` still applies; editing it in a
   Dockerfile is a review obligation (§4).
4. **The loader hook** (`reproduction-system/runtime/loader-hook.R`):
   - records the top-level script, from `commandArgs()`'s `--file=`;
   - `trace()`s `source`, `sys.source`, and `parse` when given a file;
   - traces `knitr::knit`, `rmarkdown::render`, `Rcpp::sourceCpp`, and
     `pkgload::load_all` through `setHook(packageEvent(...))` as those
     packages load;
   - for every file loaded, appends a line to `/lane-log/loads.tsv` with the
     path, the function, the md5 (`tools::md5sum`, present in every R
     version), and the size;
   - then sources the project's own `.Rprofile`, if there is one, so renv
     projects still activate. That load is logged and checked like any other.
5. **Post.** The lane records the argv, the image id (`docker image
   inspect`), the exit status, and the start and end times in `run.json`. It
   then diffs the work copy against the pre snapshot:
   - files the run wrote beside the code are copied to
     `outputs/run-written/<path>` and recorded, so projects that write beside
     their code keep their results;
   - a code file that is new or changed in the work copy is recorded, and the
     gate fails it.

   Finally the lane takes the post snapshot of the attempt tree.

**Gate checks on the last run** (earlier runs are recorded, and any code they
loaded must also be accounted for):

- every `loads.tsv` md5 must equal an anchored original, a declared
  edited copy (flagged), or a declared wrapper; otherwise the gate fails,
  because R loaded unaccounted code;
- a declared executed original that R never loaded is flagged;
- any code changed in the work copy fails;
- a non-zero exit is a warning;
- the pre and post snapshots of the attempt tree must be equal outside
  `outputs/`, and any difference fails.

The work copy makes the snapshots lane-taken rather than executor-invoked,
which answers Fable's P2-3 (hand-written or reordered snapshots). The
md5 is used because base R has no sha256 in every version; deliberately
forging an md5 collision is outside the threat model.

## 2. Transcript ordering audit (`audit-run`)

The executor's transcript is written by the harness, and the executor
cannot edit it. `audit-run` checks that:

- the executor ran the paper's code only through `reproduction-lane.py
  run-container`, with no direct `docker run`, `docker exec`, or
  `docker cp`;
- it never called `snapshot-code`, or `run-container` with `--force`;
- after its final `run-container`, it made no Write, Edit, or redirect into
  a code file or input file in the attempt directory.

Any of these is a contaminating finding, with the same status as a blinded
read.

## 3. Whole-tree inventory and code detection (Fable P1-1, P2-1, P2-2, P3-2)

- **What counts as code:**
  - the suffix list, extended with `.cpp`, `.c`, `.h`, `.jags`, `.bug`,
    and `.stan`;
  - start-up and build files: `.Rprofile`, `Rprofile.site`, `.Renviron`,
    `Makefile`, and any name containing `dockerfile`;
  - any file a wrapper passes to a loader, whatever its suffix: `source`,
    `sys.source`, `parse(file=`, `Rscript`, `R -f`, `knit`, `render`,
    `sourceCpp`, `load_all`, `python`, or `exec(open(`, quoted or not
    (shell wrappers).
- **References.** A loader reference that resolves inside the attempt but is
  undeclared is an error. Bare basenames are resolved against the tree before
  an obligation is raised (P3-5).
- **Symlinks.** A directory symlink, or a symlink resolving outside the
  attempt, is an error.

## 4. Anchors bound to the launch commit (Fable P1-2, P2-5)

- **The gate chooses the evidence pack.** It searches
  `corpus/evidence-packs/harvest-*/<slug>.json`, newest first, then
  `corpus/evidence-packs/<slug>.json`, for the anchored record. The
  manifest's `pack` field may not point anywhere else.
- **Corpus manifests are fixed.** Only the registered corpus manifests can
  anchor (`studies/open-science-compliance/corpus/manifest.yaml`,
  `corpus/development-manifest.yaml`).
- **Bound to the launch commit.** The pack, the registry, and the corpus
  manifest must exist at the run's launch commit and be unchanged since
  (`git cat-file -e`, `git diff --quiet <launch> --`).
  - `check-attempt --launch-commit` takes it. The workflow passes it, and the
    operator's authoritative re-run must pass it.
  - Without it, anchors are `recorded` and flagged, never `verified`.
- **No usable checksum is a flag, not an error.** A record without one is
  flagged as "unanchorable".

## 5. Conversions recomputed by the lane (option C; Fable P2-6)

For a wrapper with `role: conversion`, the gate itself compares the declared
`conversion.input` and `conversion.output`. No executor-written record is
needed, so there is nothing to forge.

- **Formats:** CSV, TSV, and Excel (`.xlsx`, read with `openpyxl`, added to
  `requirements.txt`). A workbook must have one sheet, or the declaration
  names the sheet.
- **Normalisation:**
  - headers and cells are compared positionally, as text after trimming;
  - two numeric cells are equal when their parsed floats are equal;
  - Excel dates are compared as ISO 8601 strings;
  - empty, `NA`, `NaN`, and `NULL` are all treated as missing.
- **Outcomes:**
  - an exact match after normalisation clears the flag;
  - any difference is flagged with a count and the first five differing
    cells ("conversion changed N values": a fail-and-uplift candidate);
  - an unsupported format, a missing file, or an ambiguous sheet stays
    flagged for a human.

## 6. Credit cannot pass a flag silently (Fable P2-4)

- **`coverage_creditable`** in the gate report excludes:
  - every target named by a declared edit, where an empty `affected_targets`
    means all targets;
  - every target, when the attempt executed no authors' file or the run
    loaded unaccounted code.
- **`rule-flags --config --slug --approver --rulings FILE`.** It records
  per-flag decisions (`admissible`, `fail-and-uplift`, or `excluded`, each
  with a note) in `flag-rulings.json`, bound to the gate report's sha256, as
  `approve` is bound to the plan.
- **Unruled flags block.** `persist-results` refuses an attempt whose gate
  report has unruled flags, unless `--record-unruled` is given, which records
  the unruled status. `human-queue` lists flags as ruled or unruled.

## 7. Cheap additions (Fable P1-3, P1-4, P3-1, P3-3, P3-4, P3-6)

- **Review obligations for:**
  - a Dockerfile `RUN` line that edits files (`sed`, `patch`, `perl -i`,
    `awk`, `tee`, `>>`, or a heredoc), or a `COPY`/`ADD` of a code path;
  - in-memory patching in a wrapper (`body(`, `formals(`, `trace(`,
    `assignInNamespace`, `unlockBinding`, `environment(...) <-`, or `<<-`).
- **A generated file** gets the inlining check, and five or more shared
  lines is an error.
- **Hashing is cached** by resolved path.
- **Fix P1-4:** the executor definition's receipt string becomes v1.3, with
  the manifest sha256 updated.
- **Fix the HER1-1 wording** in the audit.

## Limits that remain

These stay reviewer obligations, discharged in a recorded ruling before
admission:

- code evaluated from a string (`eval(parse(text = ...))`, `Rscript -e`);
- other languages called from R;
- re-implementations;
- in-memory patching that the patterns miss;
- R started with `--vanilla` or `--no-init-file`, which skips the hook and
  is flagged;
- image content loaded other than through a traced loader.

The lane covers R only, as its scope already states.

## Revisions after the Fable design review (2026-10-05)

Fable's review
(`~/agent-mail/claude/outbox/claude/20261005T053332.582671Z-claude-pr7-fable-gate-1-3-design-review.md`)
found the shape right and changed the build as follows. Astra's review is
pending.

- **Mounting** (Q1):
  - mount the work copy at the image's `WORKDIR`, or `--mount-path`, and set
    `-w`;
  - warn when the Dockerfile copies into that path, since the mount hides it;
  - keep renv libraries outside the project (`RENV_PATHS_LIBRARY`);
  - copy with `cp -a --reflink=auto`, never hard links;
  - add a detached mode for multi-hour runs (crema), whose wait step still
    takes the post snapshot.
- **Code written by the run.** A new code file in the work copy is treated
  as `generated` (flagged, inlining check, never loadable). Only a changed
  pre-existing file fails, so honest renders pass.
- **Start-up** (Q2):
  - set `R_ENVIRON_USER` to a lane file as well, and have the hook read the
    project `.Renviron` explicitly;
  - the hook sources the project `.Rprofile` from the project root, so renv
    works, and `renv/activate.R` must then be declared as an original;
  - `--vanilla`, `--no-init-file`, `--no-environ`, or `--no-site-file` in any
    wrapper is an error (key's pilot used `Rscript --vanilla`);
  - an R process that ran with an empty loader log fails.
- **Child processes.** `run-container` also writes a `.Rprofile` into the
  work copy that sources the hook and then the project's profile, which is
  renamed. A Docker test matrix asserts that a child's `source()` is logged
  for each launcher: `Rscript`, `R -f`, `callr::r`, `targets::tar_make`,
  `parallel::parLapply`, `future` multisession, and `quarto render` where
  installed.
- **Loaders:**
  - `loadNamespace` is traced, logging each package's provenance; a locally
    installed package with no repository is flagged, which is the marwick
    compendium case;
  - `parse(text = …)` logs the md5 of its text, which the gate compares with
    the originals, and `-e` expressions are logged;
  - `reticulate::source_python`, `box::use`, and `modules::import` are
    traced.
- **Hook integrity.** `untrace(`, `tracingState(`, `Sys.unsetenv`,
  `Sys.setenv(...R_PROFILE...)`, and shadowing `source`, `sys.source`, or
  `parse` are contaminating findings. The hook mirrors each log line to
  stderr with a fixed prefix, the lane captures stderr, and a line missing
  from the file fails.
- **Outputs (A14, new).** `run-container` hashes `outputs/` at the end of
  each run. The gate fails any `outputs/` file that differs from the last
  run's record, and each output is attributed to the run that wrote it. A
  write into `outputs/` after the final run is contaminating in the
  transcript audit.
- **Transcript audit:**
  - host `Rscript`, `R -f`, `python`, or `bash` on attempt paths is
    contaminating;
  - every `run-container` call must have a `run-NN/` record, and vice versa.
- **Function shadowing.** Parse the `name <- function` definitions in the
  originals, and flag any wrapper, including `.Rprofile`, that assigns those
  names.
- **Dockerfile obligations** also name `Rprofile.site`, `Renviron.site`, and
  `/etc/R`. The prompt says that `--network none` deliberately breaks
  run-time installs.
- **Conversions** (Q4):
  - only exact text after trimming trailing whitespace clears;
  - numeric-equivalent, missing-marker, and leading-whitespace differences
    are reported as separate counts and never cleared;
  - headers are compared separately;
  - empty trailing Excel rows and columns are trimmed;
  - the declared encoding is used, defaulting to UTF-8;
  - dimensions are compared first, and a reordering is reported as one;
  - dates are compared only as ISO text;
  - the declaration names the sheet and the header row.
- **Rulings** (Q5). Each is bound to the sha256 of a flag's text, so a re-run
  does not expire it. `--record-unruled` records never reach study data.
  Targets whose comparison evidence predates the last run's end are also
  excluded from `coverage_creditable`.
- **Build order** if time is short:
  1. the loader log, with the start-up belt and braces and the child test
     matrix;
  2. the outputs rule;
  3. the stderr mirror;
  4. (done in part 1) the inventory and the launch-commit anchors;
  5. then conversions, rulings, and the remaining patterns.

## Questions for the reviewers

1. Is the writable-copy design sound? Is copying files the run wrote beside
   its code into `outputs/run-written/` the right handling?
2. Does `R_PROFILE_USER` plus sourcing the project's `.Rprofile` from the hook
   keep renv projects working, and is there a loader the hook misses?
3. Is md5 in the log acceptable under this threat model?
4. Are the conversion normalisation rules right? What will cause false
   alarms or false passes?
5. Is the credit and ruling design (`coverage_creditable`, `rule-flags`, the
   `persist-results` refusal) the right shape?
6. What does this design still miss, given your attack set?
