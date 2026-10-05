---
title: "Reproduction lane gate 1.3 — consolidated specification"
tags: [reproduction, validation, mechanical-verification]
created: 2026-10-05
updated: 2026-10-05
status: foundations-built
---

# Reproduction lane gate 1.3: consolidated specification

**Status (2026-10-05, revision 1): the foundations are built; the rest is
not.** This is the one effective text. It replaces the draft's §§1–7 and
both of its revision sections. Where it differs from them, this text
governs. The superseded draft is archived at
`archive/planning/reproduction-gate-1-3-design-draft-2026-10-05.md`, as the
file stood at `2bd35aa`.

- **Reviews of this text:** Fable's arrived and is folded in below
  (`~/agent-mail/claude/outbox/claude/20261005T062807.778832Z-claude-pr7-fable-gate-1-3-spec-review.md`,
  plus two follow-ups by SendMessage on `R CMD`). **Astra's is pending**, so
  a second revision follows it.
- **Built:** F1, the record boundary (`0ce7f25`); F2, run and output
  binding (`f07763a`); F3, issues, rulings, and admission (`59f4e58`). See
  §15.
- **Changes in revision 1** (from `53413bc`): the sharpened class A and the
  pilot re-run (§2); Fable's findings in §2.4; the per-process token, the
  `FORK` event, duplicate sequence numbers, and explicit log settings (§4);
  the output layout and console output (§5); the issue codes as built
  (§6); outputs outside the mount path (§7); trace order, the saved parent
  profile, `R CMD`, and littler (§8, §10); conversions (§11); host runs
  (§12); and the matrix (§13).

**Sources consolidated:**

- Fable's design review:
  `~/agent-mail/claude/outbox/claude/20261005T053332.582671Z-claude-pr7-fable-gate-1-3-design-review.md`;
- Astra's design review:
  `~/agent-mail/codex/outbox/claude/20261005T055227Z-codex-repro-gate13-design-review.md`;
- session reflection Entry 22 (`wiki/reflections/session-reflection.md`), on
  whether the hardening converges (§2);
- amendment 3 §7(d) (`studies/open-science-compliance/prereg/amendment-3-draft.md`),
  which allows a format conversion "only when a mechanical check confirms
  every value is unchanged" (§11).

**Built on PR #7 so far:**

- gate 1.2, with the audit corrections from its review (`458878b`,
  `43a3453`, `0d87a8f`);
- gate 1.3 part 1, the static routes (`4244a51`). It covers loader
  references parsed in wrappers and originals, start-up and build files
  counted as code, symlink refusal, gate-chosen evidence packs,
  launch-commit binding, `coverage_creditable`, the review-obligation
  patterns, and the generated-file inlining check;
- the digest cache confined to one snapshot (`664bb72`, Astra's point 5),
  with a test of a same-size edit whose modification time is restored.

**Decisions already taken (Shawn, 2026-10-05):**

- build the lane-owned run command now, with the writable-copy design;
- the lane compares conversions itself (option C);
- fix every P1, P2, and P3 finding of the Fable review, and build its
  transcript audit and whole-tree inventory;
- class (ii) has a consequence (amendment 3 §7(d)): a result resting on an
  authors' file edited for mechanics counts only after a wrapper-only
  re-run.

**Facts established by probe (this session, `rocker/r-ver:4.3.2`, R
4.3.2).** These settle points the reviews raised from documentation or
memory:

1. A project `.Renviron` in the working directory overrides an
   `R_PROFILE_USER` set by `docker run -e`. A profile it named loaded in
   place of the lane hook under every launcher tried.
2. With `R_ENVIRON_USER` pointing at a lane file that sets
   `R_PROFILE_USER`, the hook loaded and project variables copied into that
   file applied. A child started after `Sys.unsetenv("R_PROFILE_USER")`
   still loaded the hook.
3. A shim mounted read-only over `$R_HOME/bin/R` (and over `/usr/local/bin/R`,
   a byte-identical copy of it) saw every R start tried: `Rscript`, `R -f`, a
   `system()` child, and a parallel socket-cluster (PSOCK) worker. The shim's
   process identifier (PID) equals the R process's, so shim and hook events
   pair by PID. `Rscript --vanilla` went through the shim but loaded no
   profile.
4. Starting `$R_HOME/bin/exec/R` directly bypasses the shim. Without the
   shim's environment setup it fails (`libR.so` not found).
5. In a container started with `--user` and `--init`, a grandchild process
   could write both to a named pipe (first-in, first-out, or FIFO) mounted
   read-only and to `/proc/1/fd/2`, and the host received both.
   `system2(..., stderr = TRUE)` captured a child's standard error (stderr),
   so a child's own stderr is not a reliable channel.
6. `Rscript` passes `--no-restore`; `R -f` does not.

`callr`, `targets`, `future`, and Quarto are not in the base image, so their
behaviour is left to the build's test matrix (§13).

## 1. Threat model

The executor is a language model with write access to its attempt
directory. It acts in good faith but is prone to helpful repairs and
rationalised shortcuts, and it may not declare them. It is not a determined
adversary, and it cannot forge cryptographic material.

**The goal.** Running anything other than the authors' original code, or
crediting anything other than what that run produced, must do one of two
things: fail the gate, or raise an issue that needs a recorded human ruling.
Defeating the checks should need deliberate, multi-step concealment. The
harness transcript, which the executor cannot edit, and the adversarial
reviewer can both see such concealment.

**Outside the model:**

- The operator's host account. The executor's tools run as the same user,
  and that user can rewrite anything on the host, sealed receipts included.
  Seals detect accidental change and the executor edits that the transcript
  audit sees. They do not stop a host-level forger, and the runbook says so
  (Astra 1).
- The Docker daemon, and the harness itself.

## 2. Stopping rule for hardening

Each review round so far has found the gate wider than the last (Entry 22).
The reviewers attacked as if the executor were an adversary. That finds real
gaps, but it has no natural end. This section sets the end.

### 2.1 Classes of finding

Every finding, including those already received (§2.4), is put in one
class:

- **D, defect.** A check already built or specified does not do what it
  claims. The digest cache was one. **Always fixed.**
- **A, ordinary route.** An honest executor could take the route in the
  ordinary course of work, with no intent to hide anything, and the gate
  would then pass work it should fail or flag. Judge it from the executor's
  position after a failure, not from a clean start: the executor optimises
  against the gate's own messages, so a route is ordinary if its first step
  is suggested by a gate message, a prompt instruction, or a tool default
  (Fable's review of this text). The evidence is one of:
  - a pilot did it;
  - a common tool does it by default (renv, a Quarto freeze, `callr`,
    `targets`);
  - a reviewer gives a concrete sequence of ordinary actions.

  **Always closed**, by a failure, a flag, or an obligation, with a
  regression test.
- **B, deliberate concealment.** The route needs acts whose only purpose is
  to hide a deviation. Examples are forging a log line, restoring a
  timestamp, shadowing `source`, committing a forged evidence pack, or
  starting the R binary directly to dodge the process census. **Closed only
  when the check is cheap:** it uses data the gate already collects (any
  check over `events.log` fields qualifies), needs no new mechanism, and
  adds no new kind of false alarm. Otherwise it goes
  to §14, where the transcript, the adversarial reviewer, and the human
  ruling are its backstops.
- **C, outside the model.** The route needs access the executor does not
  have, or breaks a cryptographic assumption (§1). **Documented, never
  built.**

### 2.2 When review stops

1. This specification gets one review from each of Astra and Fable.
   Reviewers classify their own findings. D and A findings change the
   specification. Cheap B findings are added. Other B findings and all C
   findings go to §14.
2. The built gate gets one final review per reviewer, against this
   specification and the acceptance tests (§13). That review includes one
   real pilot re-run through the whole lane: herskind's materials (no
   renv, a parse-and-evaluate wrapper, a short run), because "a pilot did
   it", the first kind of evidence for A, cannot come from fixtures.
   **A final round with no D or A finding closes the hardening**, and the
   gate goes on to the §8 regression run.
3. After that, the build reopens only for a D or an A. A route seen in
   practice (in the census, a transcript, or an adversarial review) counts
   as an A on that evidence, whatever class it had before.

Shawn may reclassify any finding.

### 2.3 What the rule accepts

An undeclared deviation by a good-faith executor reaches an admitted result
only if all three of these hold:

- it travels by a B or C route, or by a route nobody has found;
- the adversarial reviewer misses it;
- the human ruling misses it.

The lane is checked against an executor acting in good faith. Gate reports
and papers describe it that way, never as tamper-proof.

### 2.4 The open review points, classified

| Point (source) | Class | Disposition |
| --- | --- | --- |
| Digest cache outlives a snapshot (Astra 5) | D | Fixed, `664bb72` |
| Run records writable from the container (Astra 1, Fable Q6.2) | D | §4 |
| Lane instrumentation fails its own gate (Astra 1) | D | §3, §4 |
| Rulings bound to flag text or report hash (Astra 7, Fable Q5) | D | §6 |
| Old-evidence rule rejects valid outputs (Astra 7) | D | Dropped; §5 |
| Observations matched to any digest in the manifest (Astra 5) | D | §8 |
| Outputs hand-edited after the run (Fable A14) | A | §5 |
| Stale outputs carried across runs (Astra 2, Fable Q6.7) | A | §5 |
| Image tag rebuilt between runs (Astra 2) | A | §5 |
| Project `.Renviron` overrides the hook (Fable Q2; probe fact 1) | A | §8 |
| `--vanilla` in a wrapper (Fable Q2; key's pilot) | A | §10 |
| Child R processes from common tools (both) | A | §8 census |
| Uninstrumented child under a logging parent (Astra 3) | A | §8 census |
| `.RData` restored by `R -f` (Astra 3; probe fact 6) | A | §8 |
| renv library hidden by the mount (Fable Q1, Astra 4) | A | §7 |
| Mount path not `/project` (Fable Q1) | A | §7 |
| Long detached runs (Fable Q1; crema) | A | §5 |
| Honest renders writing code (Fable Q1) | A | §3 generated |
| Quarto freeze, knitr cache, `targets` store (Astra 8) | A | §9 |
| `parse(text =)` from knitr chunks (Astra 8, Fable Q2) | A | §8, §9 |
| Authors' code installed as a package (Fable Q2; marwick) | A | §8 |
| Conversion false passes (Fable Q4, Astra 6) | A | §11 |
| Host `Rscript` on attempt paths (Fable Q6.5) | A | §12 |
| Wrapper redefines an authors' function (Fable Q6.6) | A | §10 |
| Lane run from a stale checkout (Astra 10) | A | §4 receipt |
| Site profile order and content (Astra 3, Fable Q6.8) | A | §8, §10 |
| `source()` of a connection or expression (Astra 3) | A | §8 |
| Concurrent runs on one attempt (Astra 2) | A | §5 lock |
| Forked children have no handshake (consolidation) | A | §4 |
| Script on standard input, `R < file` (consolidation) | A | §8, §10 |
| Tool `-e` start-up expressions (probe) | A | §8 |
| Quarto's engine script loaded from the image (consolidation) | A | §3 |
| Host runs of comparison aids (consolidation) | D | §12 |
| Traces installed after the profile (Fable, spec review) | D | §8 |
| Processes paired by PID alone (Fable) | D | F1: token, §4 |
| `R CMD INSTALL`'s inner start (Fable) | A | §8 `PKGBUILD` |
| littler `r` bypasses the shim (Fable) | A, cheap | §8, §10 |
| Targets read from printed output (Fable) | A | F2: §5 |
| Outputs written outside the mount path (Fable) | A | §7 prompt |
| Host run before the final run (Fable, revised) | Flag | §12 |
| Inserted lines repeat a sequence number (Fable) | B, cheap | F1: §4 |
| Custom `R CMD` script in `$R_HOME/bin` (Fable) | B | §10 |
| Hook disabled in-session, e.g. `untrace` (Fable Q2) | B, cheap | §10 |
| Run records versus transcript calls (Fable Q6.9) | B, cheap | §12 |
| Command-string evasion of the audit (Astra 10) | B | §14 |
| Forged event lines in the stream (Astra 1) | B | §14 |
| Direct `exec/R` start (probe fact 4) | B | §14 |
| Host rewrite of sealed receipts (Astra 1) | C | §1, runbook |

## 3. Terms: trees, runs, and provenance classes

**Trees.** The attempt directory is divided into three parts:

- **Records**, written only by the lane on the host and never mounted:
  `lane-records/`.
- **Documents**, written by the executor, never copied into a run, and
  never loadable:
  - `reproduction-plan.json` and `reproduction-plan.md`;
  - `plan-approval.json`, `authors-code-manifest.json`, and
    `execution-report.json`;
  - `gate-report.json`, `flag-rulings.json`, and `adversarial-review.json`;
  - `log.md`, `environment.md`, and `comparisons/`;
  - `outputs/`, which holds the collected run outputs (§5).

  Comparison aids live under `comparisons/`.
- **The input tree**: everything else. A run's work copy is made from it.

The legacy `execution-snapshots/` directory is read only for attempts on the
legacy allowlist.

**Runs.** A run is one call of `run-container` (§5), numbered `run-01`,
`run-02`, and so on. The **final run** is the highest-numbered run that
reached `complete` or `failed`. A **consumed run** is an earlier run whose
outputs a later run declared as input.

**Provenance classes.** Every file that R loads is in exactly one class.
This resolves the drafts' disagreement on generated code.

1. **Original:** an authors' file, anchored as part 1 builds it, together
   with its byte-identical executed copies.
2. **Edited copy:** a declared edit of an original. It is flagged, and class
   (ii) applies (§6).
3. **Wrapper:** executor-written mechanics. Roles: `wrapper`, `tooling`,
   `environment`, `conversion`, and `comparison`.
4. **Lane instrumentation:** files the lane writes or mounts. These are the
   hook, the exec shim, the lane `Renviron`, and the `.Rprofile` the lane
   injects into the work copy. The lane knows their digests and records
   them in the receipt. The executor never declares them, and the work copy
   is compared against a baseline taken after they are in place (§4).
5. **Tool-internal:** code a traced tool loads during a traced call on an
   accounted file. Examples are chunks `knitr` evaluates while knitting an
   original, and the wrapper `Rcpp::sourceCpp` writes to the temporary
   directory and sources. These loads are attributed to the enclosing call
   by nesting (§8). Code loaded from the image outside the work copy, and
   not nested in such a call, is **image code**. It is listed, and flagged
   unless it lies in an R library path or is a tool launcher on the lane's
   list, recorded with its digest. Quarto's `knitr` engine script is the
   first entry: without it every Quarto render would be flagged.
6. **Generated:** a code file the run created in the work copy.
   - It is collected with the run's outputs and flagged.
   - It gets the inlining check: five or more lines shared with an original
     is an error.
   - **It is never loadable.** A load of a generated file in the same or a
     later run fails, with a message naming the honest route: load the
     original that generated it. For example, knit the `.Rmd` rather than
     sourcing the `.R` that `knitr::purl` wrote from it.
   - A **pre-existing** code file that the run changed fails.
7. **Unaccounted:** anything else R loaded. **The gate fails.**

## 4. Foundation 1: the record boundary

**What the container sees.** Each run mounts exactly these:

- the work copy, read-write, at the mount path (§7);
- the lane directory, read-only, at `/lane`: the hook, the shim, the lane
  `Renviron`, and the image's own front-end script as `R.orig`;
- the exec shim (`reproduction-system/runtime/r-shim.sh`), read-only, over
  `$R_HOME/bin/R` and every byte-identical copy on the image's `PATH`
  (found with `readlink -f`). It writes the `EXEC` event and then execs
  `/lane/R.orig`, which works from there because the front end hard-codes
  its `R_HOME`. A `PATH` `R` with other bytes is recorded as unshimmed.

Nothing under `lane-records/` or `outputs/` is ever mounted. The run writes
only into its work copy (Astra 1).

**The authoritative event stream** is Docker's log stream for the container,
held by the daemon on the host:

- The run starts with `--init`, so PID 1 is Docker's init process and its
  stderr is the log pipe.
- The shim and the hook write each event as one line, in one `write`, to
  `/proc/1/fd/2`.
- A child whose stderr R captures still reaches the stream, which probe
  fact 5 confirmed.

After the container exits, the lane collects the stream with `docker logs`.
The stderr stream, events and the analysis's own stderr together, is
stored as `events.log` in the run record. The stdout stream is collected as
the run's console output, `outputs/run-NN/stdout.log` (§5), which keeps
chatty output out of the events.

**Log settings.** The lane passes `--log-driver json-file` and
`--log-opt max-size=100g` explicitly, and reads `HostConfig.LogConfig` back
into `run.json` at start, recording a problem if rotation could apply. A
rotated stream loses events, and the gap check would then end a multi-hour
run `incomplete` (Fable's review of this text, Q2). Docker accepts
`max-size=-1` when creating a container but refuses it at start, hence the
explicit, effectively unbounded size.

**Event format.** One line per event, at most 4,096 bytes so that each
write is atomic:

```text
LANE1 <run-nonce> <token> <pid> <ppid> <seq> <event> <tab-separated fields>
```

The **token** is minted by the shim for each process it starts
(`LANE_PROC`, with `LANE_PROC_PID`), and the R process inherits it. Events
pair on the token, not the PID, because PIDs repeat in a long run once the
PID space wraps (Fable, D-2). An R process the shim did not start mints its
own token. `seq` is 0 for the shim's `EXEC` and counts from 1 in the hook.
Strings are hex-encoded UTF-8, and an over-long argv is cut and marked,
never wrapped. The events are:

- `EXEC`: from the shim; where stdin comes from, the working directory, and
  argv;
- `START`: hook version, argv, `R_PROFILE_USER`, `R_ENVIRON_USER`, the md5
  of the site profile and site `Renviron`, and whether a workspace restore
  is pending;
- `LOAD`, `TEXT`, `CONN`, and `PKG` (§8);
- `FORK`: emitted by the hook in a forked child (`parallel::mclapply`) before
  its first event, carrying the parent's token;
- `END`: written by an exit finaliser when the process ends normally.

**Incomplete and abnormal processes:**

- A process whose sequence numbers have a gap, or repeat, has lost or
  gained lines. It is **incomplete**, and so is its run (§5). This catches
  log rotation dropping lines, and a forged line inserted with the next
  number, which the hook's own next line then repeats.
- A process with a `START`, no `END`, and no gap **ended abnormally**: its
  events up to the end are whole. Its run is `failed`, not `incomplete`.
- A forked child inherits the hook. After `FORK` its sequence restarts, and
  it needs no `EXEC`, `START`, or `END`, because forked children leave
  through `_exit`.

**The alternative channel** was a FIFO in a read-only mount with a host
collector, which the probe also confirmed. Fable accepted the log stream on
three conditions, all built: explicit log settings, stdout diverted, and
the repeated-sequence check. The FIFO's collector would be one more thing
to die during a detached run. Astra's view is pending (§16, question 2).

**Baseline.** The lane copies the input tree into the work copy and then
hashes the copy. It must equal the run's pre snapshot of the input tree,
which detects a copy fault. The lane then makes its declared changes:

- injecting `.Rprofile`;
- renaming a project `.Rprofile` to `.Rprofile.project`;
- removing the cache stores listed in §9.

It records each change and takes the **baseline** snapshot. The post-run
comparison is against the baseline, not the pre snapshot, so the gate never
rejects its own instrumentation (Astra 1).

**The sealed receipt.** `lane-records/run-NN/` holds:

- `run.json`: argv; the image tag and image id; the container id; the mount
  path; the hook, shim, and lane-script digests; the launch commit; start
  and end times; exit status; and state.
- `pre.json`: the input-tree snapshot the work copy was made from.
- `baseline.json`: the work copy after the lane's declared changes.
- `post.json`: the work copy when the container ended.
- `events.log`: the collected stream.
- `outputs.json`: every collected file, with its path, sha256, and class
  (output, generated, or changed code), and the consumed inputs.
- `receipt.json`, written last: the sha256 of each file above, and a
  summary.

The receipt's sha256 is appended to `lane-records/index.jsonl`. The gate
recomputes every digest in the chain.

**Launcher binding** (Astra 10). The receipt's lane-script digest must equal
that script at the launch commit. The launch commit must equal the one the
execute workflow pins in its checksummed arguments. An executor that runs
`run-container` from a stale checkout therefore fails the binding. It does
not pass by name.

## 5. Foundation 2: run and output binding

**Lifecycle of `run-container <attempt> --image TAG --entry FILE`:**

1. **Lock.** Create `lane-records/lock` exclusively, recording the PID, the
   host, and the start time. An existing lock refuses the run. Only the
   operator clears a stale lock (`--clear-lock`), and only after checking
   that the recorded container is gone.
2. **Resolve the image.** Map the tag to an immutable image id with `docker
   image inspect`. The run uses the id, and both are recorded. If the
   image's `llmr.dockerfile.sha256` label is absent or differs from the
   attempt's current `Dockerfile`, the image is flagged as stale, or built
   from a different file. The preparation prompt has the executor build
   with that label.
3. **Pre snapshot, copy, verify, instrument, baseline** (§4). Consumed
   inputs are declared as `--consume run-NN:files/<path>`. The source run
   must be sealed `complete` or `failed`, and the output unchanged since it
   was collected. Each is copied into the work copy at `<path>`, which must
   not already exist, and recorded as a lane change with its digest and
   source run.
4. **Start the container,** named `llmr-<run>-<nonce>`, with `--init`,
   `--network none`, the log settings of §4, `--user uid:gid`, the mounts of
   §4, `-w <mount path>`, an explicit `--entrypoint` (`Rscript` or `bash`,
   by the entry's suffix), and the environment of §8. If `docker run`
   creates the container but cannot start it, the lane removes it, and
   leaves no record, lock, or work copy.
5. **Wait** in the foreground, or return at once with `--detach`. A
   detached run is finished by `run-container --finalise run-NN`, which
   waits for the container to exit (`docker wait`) before doing step 6.
6. **Collect.**
   - Collect the stream (§4).
   - Diff the work copy against the baseline, and copy every new or changed
     file to `outputs/run-NN/files/<relative path>`. Each file is classed as
     an output, as generated code, or as a changed pre-existing code file,
     which fails. The console output is `outputs/run-NN/stdout.log`, class
     `console`, so a target read from printed results can cite it (Fable's
     review of this text).
   - Take the post snapshot, write `outputs.json`, seal the receipt, and
     release the lock.
   - Delete the work copy unless `--keep-work` is given.
7. **State.**
   - `complete`: exit 0, with the stream and the collection both whole.
   - `failed`: a non-zero exit, with everything collected.
   - `incomplete`: anything else, such as a lane crash, a lost container, a
     run never finalised, or an incomplete process (§4).

**Rules the gate applies:**

- Every run starts with an empty output destination, and no run overwrites
  another's.
- At gate time the input tree must equal the final run's pre snapshot
  exactly: nothing added, changed, or removed. A change after the run means
  re-running (Fable P2-3, Astra 2).
- Every file under `outputs/run-NN/` must match that run's `outputs.json`.
  An extra, changed, or missing file fails. This closes Fable's A14: an
  output edited by hand after the run.
- **Credit comes only from the final run and its consumed runs.**
  - Their loads must all be accounted for (§8).
  - A `failed` run's outputs need a ruling on partial results (§6).
  - A consumed run that is `incomplete` blocks, and no ruling clears it.
    (The final run is never `incomplete`, by definition.) An incomplete
    run later than the final run is reported.
  - A consumed run whose input tree differs from the final run's in code
    raises an issue: the output was produced by other code.
- **Comparison records cite outputs.** Comparison schema 1.1 adds
  `outputs: [{run, path, sha256, lines?}]` to each target, where `path` is
  as `outputs.json` lists it (`files/…` or `stdout.log`) and `lines` an
  optional range. The gate checks each citation against the sealed
  `outputs.json`.
  - A target that cites no run output stays in raw coverage but is not
    admitted until ruled (`target-unbound`).
  - This replaces Fable's rule excluding evidence older than the run's end,
    which Astra showed would reject valid outputs.

**Retired:** the executor-invoked `snapshot-code` and `execution-snapshots/`
for new attempts. The transcript audit treats their use as contaminating
(§12).

## 6. Foundation 3: issues, rulings, and admission

**Issues.** Each flag and each review obligation becomes a structured issue.
It carries a `code` (for example `edited-copy` or `conversion-differs`), a
`subject` (the path or item concerned), and a `targets` list, where an empty
list means all targets.

- The **issue id** is `code:subject`. It stays stable across re-runs.
- The **evidence fingerprint** is the sha256 of a canonical JSON object
  holding:
  - the issue code and that code's policy version;
  - the subject and the target scope;
  - the sha256 of every file the issue concerns.

  Each code's policy version sits in a lane table. It is bumped when that
  check's meaning changes, rather than with every gate release.

**As built (F3).** An issue is a `str` subclass (`Issue` in the lane
script): it is its own message, so every relay, report, and test that
carries flags as text keeps working, and the identity travels with it. The
codes are:

- anchors: `anchor-absent`, `anchor-unbound`, `anchor-unanchorable`,
  `anchor-registry-unclean`, `anchor-version-unselected`,
  `anchor-corpus-unselected`, `anchor-git-offline`;
- originals and edits: `no-pristine-copy`, `transcription`, `edited-copy`,
  `credited-edited-target`, `no-executed-original`;
- wrappers: `generated-code`, `conversion-evidence`,
  `wrapper-embeds-original`, `dynamic-evaluation`, `in-memory-patching`,
  `docker-fetch`, `docker-build-edit`, `docker-copy`,
  `external-code-reference`, `wrapper-semantics`;
- runs: `run-launch-unbound`, `run-failed`, `stray-events`,
  `consumed-other-code`, `image-stale`, `process-outside-front-end`,
  `stdin-script`, `workspace-restore`, `target-unbound`.

A plain string left at any site becomes an `unclassified` issue keyed by
its text: still rulable, but any change of wording lapses its ruling.

**Rulings.** `rule-flags --config --slug --approver --rulings FILE` writes
entries to `flag-rulings.json`. Each entry holds the issue id, the
fingerprint, a decision, a note, the approver, and the time.

- Decisions on flags: `admissible`, `fail-and-uplift`, or `excluded`.
- Decisions on obligations: `discharged`, `fail-and-uplift`, or `excluded`.
- Under amendment 3 §7(d), `fail-and-uplift` makes the target's result uplift
  evidence, which never counts toward coverage or the verdict.
- **A ruling applies only when both the id and the fingerprint match.** A
  re-run that changes the files concerned needs a new ruling. A re-run that
  changes nothing keeps the ruling (Fable Q5, Astra 7).
- General rulings, which apply a predicate across runs, are not built in
  1.3. Under §2 they are not needed to close any A route, and a re-ruling
  costs one human look.

**Hard failures** cannot be ruled. These are a gate `fail`, an `incomplete`
consumed run, a contaminating transcript finding, and a broken receipt
chain. A
ruling never overrides one (Astra 7).

**Coverage:**

- `coverage_raw` is the comparison record's coverage, recomputed as today.
- `coverage_admitted` excludes:
  - every target an unruled issue names;
  - every target ruled `fail-and-uplift` or `excluded`;
  - targets resting on a declared edit until the class (ii) wrapper-only
    re-run exists;
  - targets resting on a `failed` run's outputs until ruled;
  - every target, when no authors' file ran or the run loaded unaccounted
    code.

  This supersedes `coverage_creditable` from part 1, which stays in the
  report until the workflow switches to run records.

**Admission.** `persist-results` writes a study-eligible record only when
all of these hold:

- the gate did not fail;
- every issue is ruled;
- the transcript audit is clean (`transcript-audit.json`, §12). The audit
  is not built yet, so no attempt is eligible until it is;
- every credited run is `complete`, or is `failed` with a ruling.

`--record-unruled` persists the record with `eligible: false` and the
reasons. No downstream command makes such a record eligible: a fresh
`persist-results` after rulings is the only route. `human-queue` lists
issues as ruled or unruled.

## 7. Execution contract (`run-container`)

- **Mount path.** Mount at the image's `WORKDIR` from `docker image
  inspect`, unless `--mount-path` is given, and set `-w` to the same path.
  The pilots use `/project`, `/attempt`, and `/analysis`.
- **Shadowed build content.** Warn when the `Dockerfile` has a `COPY` or
  `ADD` whose destination lies under the mount path, since the mount hides
  it.
- **Outputs outside the mount path** (`~/results/`, `/tmp`) are never
  collected. The preparation prompt says so: the wrapper copies anything
  written elsewhere into the work copy before it exits (Fable's review of
  this text).
- **renv:**
  - set the library location outside the project (`RENV_PATHS_LIBRARY`) at
    build and restore time as well as at run time;
  - keep the package cache reachable, or copy packages in;
  - test the chosen non-root user with networking off.

  The preparation prompt says so, and says that `--network none` is meant
  to break run-time installs: a fetch belongs in the `Dockerfile`, where the
  obligation patterns see it.
- **The copy** is made with `cp -a --reflink=auto` and never with hard
  links. `--work-root` should be on the same filesystem as the attempt.
  Attempts can hold gigabytes of data, and the runbook says so.
- **`renv/activate.R`.** A file in the authors' deposit is an original,
  whatever it does, so it is declared as one. The preparation
  prompt says so, for the first renv paper.

## 8. Instrumentation

This section resolves the drafts' disagreement on skipped start-up hooks.

**Start-up order.** R reads, in order:

1. the site `Renviron`;
2. the user `Renviron`, which is `R_ENVIRON_USER`;
3. the site profile;
4. the user profile, which is `R_PROFILE_USER`;
5. then it restores `.RData`, and then runs `.First`.

The lane intervenes only at steps 2 and 4:

- **Step 2.** `R_ENVIRON_USER=/lane/Renviron`. The lane writes that file from
  the project's `.Renviron`, verbatim and in order, then
  `LANE_PARENT_PROFILE=${R_PROFILE_USER}`, which saves whatever profile the
  process inherited or the project named, then one pin line that sets
  `R_PROFILE_USER` to the hook (built in F1).
  - Project variables then apply in the environment phase, where R intends
    them (Astra 3).
  - A project `.Renviron` cannot displace the hook, which probe fact 1
    showed it otherwise does.
  - Children inherit the pin (probe fact 2).
  - The pin is never conditional, or a project line above it would win
    again. The saved `LANE_PARENT_PROFILE` lets `callr`'s bootstrap profile
    still run after the hook (Fable's review of this text, Q3). Whether
    that bootstrap survives this order is for the matrix (§13).
- **Step 4.** The hook:
  1. emits `START`, and registers an `END` emitter to run on exit;
  2. installs its traces. **Traces come before the profile** (Fable, D-1):
     otherwise loads made inside the profile, such as renv's
     `source("renv/activate.R")`, go unlogged, and §8's flag for an
     executed original no run loaded fires on every renv paper;
  3. sources one user profile into the global environment, where R
     evaluates one: the saved `LANE_PARENT_PROFILE` if set and not the
     hook; otherwise what R would have read, `.Rprofile.project` or
     `.Rprofile` in the working directory, else `~/.Rprofile`. That load is
     logged like any other.

  F1 built steps 1 and 3; the traces come with the instrumentation stage.

  The lane's injected `.Rprofile` sources the hook too. A child that reads
  the working directory's profile instead of `R_PROFILE_USER` (`callr` in
  project-profile mode) still loads it. A guard option stops a second load
  in one process.
- **Site profile.** Steps 1 and 3 are left alone, so the image's documented
  start-up runs as it would. `START` records the site files' md5. Editing
  them is a `Dockerfile` obligation (§10).
- **Workspace restore.** When `.RData` is in the working directory and the
  argv lacks `--no-restore`, `START` records a pending restore. The run gets
  an obligation: a declared input, with a review (probe fact 6).

**Process census** (built in F1). Every `EXEC` (from the shim) pairs by
token with a `START` and an `END` (from the hook):

- `EXEC` without `START`, with `--vanilla` or `--no-init-file` in argv:
  **fail** (`hook-skipped`).
- `EXEC` without `START`, otherwise: **fail** (`uninstrumented-process`).
  The message names the launcher and points to the supported-launcher list.
  The exception is a tool route the matrix shows cannot be instrumented and
  has no adapter. That route is listed by name in the lane and **flagged**
  (`unsupported-launcher`), and targets resting on the run are not admitted
  until ruled (Astra 3).
- `START` without `EXEC`: flagged as R started outside the front end.
- A script on standard input (`R < file`): no traced load covers it, so
  the shim marks the `EXEC` and the gate raises an obligation. In a
  wrapper it is an error (§10), with `R -f file` as the alternative.
- The rule keys on the handshake, not on argv options. A child that a tool
  starts with `--no-site-file`, and that still handshakes, passes (Astra 3).
- **`R CMD`, `R RHOME`, and `R --version` need no handshake.** The `CMD`
  process is a shell dispatcher. A subcommand that runs R re-enters the
  front end, so that start is censused as its own process: `R CMD BATCH`
  runs `${R_HOME}/bin/R -f ${in}` (`bin/BATCH` line 60 in
  `rocker/r-ver:4.3.2`), so a `--vanilla` there still fails. Fable and
  this text agreed on that after checking the image's scripts.
- **`R CMD INSTALL`** pipes `tools:::.install_packages()` into an R start
  with init files off (`bin/INSTALL` line 34), so that inner start has no
  `START` and fails today. Instrumentation adds a `PKGBUILD` binding: the
  inner start, recognised by its stdin expression and its parent's
  `CMD INSTALL <path>`, is accounted for when `<path>` is a declared
  original tree, and the `PKG` flag then covers the installed result.
- **littler** (`r`, on every rocker image) embeds libR and passes neither
  the shim nor any profile. Instrumentation shims `/usr/local/bin/r` and
  `/usr/bin/r` to `exec Rscript` with the arguments, and §10 makes `r
  file.R` a static error.

A non-empty log no longer stands in for instrumentation. Each process
accounts for itself (Astra 3).

**Loader events,** each bound to process, run, resolved path, and nesting
(Astra 5):

- **`LOAD`**, with the function, resolved path, md5, size, depth, and
  enclosing event. Emitted for:
  - the top-level script (`--file=` in argv);
  - `source`, `sys.source`, and `parse(file =)`;
  - `knitr::knit`, `rmarkdown::render`, `Rcpp::sourceCpp`, and
    `pkgload::load_all`;
  - `reticulate::source_python` and `py_run_file`, `box::use`, and
    `modules::import`.
- **`TEXT`**, for `parse(text =)` and `-e` expressions: the md5 of the text
  joined by newlines, its length, depth, and enclosing event. Repeats of one
  md5 in one process are counted, not logged again.
- **`CONN`**, for `source()` of a connection or expression: its class and
  description. It is always an obligation, because a path hash does not
  cover its content.
- **`PKG`**, for `loadNamespace`: the name, version, and library path; the
  `Repository`, `RemoteType`, `RemoteSha`, and `Packaged` fields; and the
  md5 of the installed `DESCRIPTION`.

**The gate's account of a run:**

- **`LOAD`** must resolve to an original (by md5, computed by the gate for
  every original), a declared wrapper, or lane instrumentation. A nested
  load inside a traced tool call on an accounted file is tool-internal.
  Otherwise the run is generated or unaccounted, and fails.
- **`TEXT`** is attributed to its innermost enclosing `LOAD`:
  - inside an original, or a tool call on one, it is the authors' own code;
  - inside a wrapper, or at depth 0, it must match by md5 one of: an
    original file; one code chunk of an original R Markdown or Quarto
    document; or an entry on the lane's list of tool expressions. The
    PSOCK worker's start-up `-e` expression, seen in the probe, is the
    first entry, and the launcher matrix supplies the rest.

  A match is accounted for. Anything else is an obligation
  (`unmatched-text`), not an error, because ordinary bootstrap code also
  arrives this way (Astra 8).
- **`PKG`:** a package that is not base, and has no repository or remote
  provenance, is flagged as installed locally: declare its source tree as an
  original (Fable, marwick). When that tree is declared, the gate compares
  the installed `DESCRIPTION` with it.
- **The declared executed originals:** one that no credited run loaded is
  flagged.

**Hashes.** The hook uses md5 (`tools::md5sum`, present in every R version)
inside the container. sha256 stays for host receipts and anchors. Both
reviewers accept this under §1.

A file's md5 is taken before the loader reads it. The work copy is private
to the run, so only the run itself could change a file between hash and
parse. A pre-existing code file that changed fails at collection, so the
race needs a change made and undone within the run, which is class B.

**Semantics neutrality.** The hook keeps its state out of the global
environment and the search path, never touches `.Random.seed`, and adds no
output to stdout. An acceptance test checks that results are equal with and
without it (Astra 9).

## 9. Fresh computation

- **Cache stores.** The lane removes these known stores from the work copy
  before the run (fresh-execution mode), recording each as a lane change:
  - `knitr` caches (`*_cache/`);
  - Quarto's `_freeze/` and `.quarto/`;
  - the `targets` store (`_targets/`).

  A plan may declare a store as an input instead. That store is then
  recorded as a dependency whose admissibility is unresolved, which is an
  obligation (Astra 8).
- **Other cache-like directories.** A directory under the input tree whose
  name contains `cache`, and that is not a known store, is an obligation.
- **Saved workspaces** are covered by the restore rule (§8).
- **`parse(text =)`** is mapped by nesting and chunk md5 (§8), not compared
  with whole files.

## 10. Static checks

Part 1 built the code-file definition, loader-reference parsing, symlink
refusal, launch-commit anchors, the `Dockerfile` and in-memory patching
obligations, and the inlining check. Additions:

- **Start-up options in wrappers.** `--vanilla` and `--no-init-file` are
  errors: they skip the hook. So is a script on standard input
  (`R < file`), which no load event covers. `--no-environ` and
  `--no-site-file` are flags: they change start-up meaning without evading
  the hook, and a child that still handshakes passes the census (§8). This
  splits the draft's single rule, in line with Astra's point about
  legitimate children.
- **Launchers that are errors in a wrapper:** littler's `r file.R`
  (`\br\s+\S+\.[Rr]\b`), which bypasses the shim and every profile; and
  `R CMD check`, which is not an ordinary reproduction action (Fable's
  review of this text).
- **Hook integrity.** These are errors in a wrapper and flags in an
  original:
  - `untrace(` and `tracingState(`;
  - `Sys.unsetenv` or `Sys.setenv` naming `R_PROFILE_USER`,
    `R_ENVIRON_USER`, or `R_PROFILE`;
  - assignment to `source`, `sys.source`, `parse`, or `loadNamespace`.
- **Function shadowing.** The gate parses the `name <- function` and `name =
  function` definitions in the originals. A wrapper, or a project
  `.Rprofile`, that assigns one of those names is flagged.
- **Project `.Renviron`.** If it names `R_PROFILE_USER`, `R_PROFILE`, or
  `R_ENVIRON_USER`, that is flagged, and the hook sources the named profile
  in place of `.Rprofile.project`.
- **`Dockerfile` obligations** also name `Rprofile.site`, `Renviron.site`,
  `/etc/R`, and a `COPY` or `ADD` into `$R_HOME/bin`, where a custom
  `R CMD` subcommand would dispatch to arbitrary code (Fable).

## 11. Conversions

This section resolves the drafts' disagreement on conversion equality. The
rule sits inside amendment 3 §7(d): a conversion is allowed "only when a
mechanical check confirms every value is unchanged", and any change of value
is fail-and-uplift.

**The declaration.** A wrapper with `role: conversion` declares its
`conversion` as follows:

- `input` and `output`;
- `sheet`, which a workbook requires;
- an optional `range`;
- `header_row` (default 1);
- `encoding` (default UTF-8) for text formats;
- `na`, the converter's string for a missing value (`NA` for R's
  `write.csv`), if it writes one.

The lane does the comparison and the executor writes no evidence, so the
executor-written `value_identity_check` field is retired. The comparison's
input and output digests must match the run records. The output is either
in the final run's input tree, made before the run by the conversion
wrapper (which may run on the host, §12), or a consumed run's output.

**Reading.**

- Comma- and tab-separated files (CSV, TSV) are read as text fields with the
  declared encoding. There is no type inference. A decoding failure is
  flagged.
- Excel workbooks (`.xlsx`) are read twice with `openpyxl`:
  - with `data_only=False`, to find formula cells;
  - with `data_only=True`, for cached values.

  A formula or external-link cell is flagged whatever its cached value,
  because a cached value is not evidence of a fresh calculation (Astra 6).
  Error cells are counted. Raw values and cell types are kept beside the
  comparison.

**Equality.** Nothing is trimmed and nothing is normalised. §7(d) asks
for unchanged *values*. An untyped text field has only its text, so text
to text (CSV to CSV or TSV) compares raw field text exactly. A typed
workbook cell has a value, and its accepted renderings are enumerated
(revised after Fable's review of this text):

| Cell type | Accepted renderings |
| --- | --- |
| string | its text, exactly (leading zeros and spaces preserved) |
| number | any text parsing to the same double, at most 15 significant digits |
| boolean | `TRUE` or `FALSE` |
| date or datetime | ISO 8601 text for the same instant (see below) |
| blank | the empty field, or exactly the declared `na` string |

- **Numbers.** R's `write.csv` renders by width under `scipen`, so 100000
  becomes `1e+05` and 0.0001 becomes `1e-04`. A fixed list of renderings
  would flag every count column at or above 1e5. Value identity for a
  double is what §7(d) asks. The leading-zero and identifier risks do not
  arise for a cell that is already a number: those are strings.
- **Datetimes.** readxl returns UTC instants, and `write.csv` renders them
  in the session's timezone. They are compared as instants after a
  timezone-aware parse, and a value without a zone is read as UTC.
- A typed cell matched in a rendering other than the canonical one clears,
  but is counted ("same value, other rendering"), so the human sees it.
- In text-to-text comparison, a numeric field whose text differs but whose
  value is equal (`1.50` against `1.5`) is counted as
  **numeric-equivalent** and never cleared.

**The comparison runs in this order:**

1. Trim fully empty trailing rows and columns from a workbook, and count
   them.
2. Compare dimensions. If the rows are the same multiset in another order,
   report them as reordered, not as every cell differing.
3. Compare headers on their own line, which reports R's `make.names`
   rewrites.
4. Compare the cells.

**What is counted.** Each of these is counted on its own, and none is ever
cleared:

- numeric-equivalent fields in text-to-text comparison;
- missing-marker changes: a blank written as anything but the empty field
  or the declared `na` string, or `""`, `NA`, `NaN`, and `NULL` traded for
  one another;
- whitespace-only differences, leading or trailing;
- other value changes;
- formulae, error values, and decoding failures;
- unchecked sheets.

**The outcome.** The flag clears only when all of these hold:

- the dimensions are equal, after trimming;
- the headers are exact;
- every cell matches, as above;
- there are no formulae, error values, or decoding failures.

Anything else is an issue (`conversion-differs`) reporting the counts and
the first five differing cells, raw and typed. The human rules
`admissible`, where nothing changed in value, or `fail-and-uplift`. An
unsupported format, a missing file, or an ambiguous sheet stays an issue.

## 12. Transcript audit (supporting evidence)

`audit-run` reads the harness transcript, which the executor cannot edit.
Contaminating findings block admission (§6). The audit is supporting
evidence: shell indirection and the Docker API can avoid any command
pattern, which is why §4 binds runs by receipt, not by command name
(Astra 10).

**Contaminating findings:**

- paper code run other than through `run-container`:
  - `docker run`, `exec`, `cp`, `start`, or `compose`;
  - host `Rscript`, `R -f`, `R --file`, `python`, or `bash` naming an
    original, an executed or edited copy, or a wrapper, **after the final
    run started**. Wrappers whose role is `comparison` or `conversion` are
    exempt: they run on the host, and the lane checks their results itself
    (§5, §11);
- use of `snapshot-code`, or `run-container --clear-lock`, by the executor;
- any write (Write, Edit, redirect, `cp`, `mv`, `sed -i`, or `tee`) into
  `lane-records/` or `outputs/`;
- any write into the input tree after the final run started;
- a `run-container` call without a run record, or a record without a call
  (Fable Q6.9).

**A flag, not contamination: a host run before the final run**
(`host-run`). Running a wrapper on the host to see whether it parses, then
fixing it and running `run-container`, is ordinary debugging. It cannot
alter what is credited, because credit comes only from sealed outputs
(Fable's review of this text, revising its own Q6.5). A human rules on it,
since invariant 5 is an environment rule, not an evidence rule.

## 13. Acceptance tests

Tests that need Docker skip when Docker is absent. The final review needs
them run on a host with Docker.

- **Record boundary:**
  - a container write to `/lane` or to the run records fails at the mount;
  - the gate passes its own instrumentation;
  - a broken receipt chain fails.
- **Run binding:**
  - an output edited after the run fails (A14);
  - a stale output surviving a failed re-run is not creditable;
  - a consumed output must be declared;
  - a second `run-container` is refused while the first holds the lock;
  - an image rebuilt between runs shows a new image id;
  - a detached run counts only after `--finalise`.
- **Rulings:** a changed input under an unchanged issue message does not
  inherit the ruling; an unchanged re-run does.
- **Launcher matrix.** Using a test image of `rocker/r-ver:4.3.2` with
  `callr`, `targets`, `future`, `knitr`, and `rmarkdown` from the
  Comprehensive R Archive Network (CRAN), plus Quarto where installed: a
  marker `source()` in each child must appear as a `LOAD`, with a paired
  `EXEC`, `START`, and `END`. The launchers are:
  - `Rscript` and `R -f`;
  - `R < file`, which must yield an obligation, not a `LOAD`;
  - `parallel::mclapply`, whose children must show `FORK`;
  - `R CMD BATCH script.R`: the inner `R -f` handshakes, and the outer
    dispatcher is exempt;
  - `R CMD INSTALL <path>`, with `remotes::install_local` and
    `devtools::install`: the inner start is bound by `PKGBUILD`;
  - `callr::r`, in each profile mode;
  - `targets::tar_make`;
  - `parallel::parLapply` on a PSOCK cluster;
  - `future` multisession;
  - `rmarkdown::render` in-process;
  - `quarto render`;
  - a child that changes its working directory;
  - an uninstrumented child under a logging parent, which must fail the
    census.
- **Fresh computation:** a cached and a fresh Quarto render; a `knitr`
  cache; a `targets` store.
- **Loaders:**
  - a plain script;
  - legitimate generated helper code (flagged, not failed);
  - a generated file loaded later (fails);
  - `parse(text =)` from `knitr` chunks (accounted for);
  - a wrapper evaluating an edited chunk (an obligation);
  - a locally installed package (flagged).
- **Conversions:** fixtures for:
  - `007`, `1.50`, an integer above 2^53, and `1E3` as text;
  - `NA` against `""`, and leading and trailing spaces;
  - a `make.names` header, and a Latin-1 file;
  - a formula cell, an error cell, and trailing empty rows;
  - reordered rows;
  - `100000` written by base R (`1e+05`), a datetime under a non-UTC
    timezone, and a blank written as `NA`.
- **Semantics neutrality:** a fixture's results, `ls()`, `search()`, and
  random-number state are equal with and without instrumentation.
- **A pilot re-run** through the whole lane, herskind's (§2.2), in the final
  review.

Built with F1–F3 (`tests/test_run_container.py`, `tests/test_rulings.py`,
and `GateTests`): the record boundary, run binding (the image-id, lock,
consumption, failed-start, and A14 cases; the detached path is exercised
through `finalise_run`), rulings including the changed-input case, the
`--vanilla` child, `system()` and PSOCK children, and a project
`.Renviron`. The rest come with their stages.

## 14. Limits that remain

These are reviewer obligations, discharged in a ruling before admission, or
are documented outside the model:

- **Code that runs without a traced load:**
  - code evaluated from strings built at run time that match no original
    (`unmatched-text` obligations);
  - re-implementations;
  - in-memory patching that the patterns miss;
  - objects with functions restored by `load()` or `readRDS()`.
- **Other languages.** Code in another language called from R, beyond the
  traced `reticulate` calls, appears only as a static loader reference.
- **Image content** loaded other than through a traced loader.
- **B routes:**
  - forged event lines in the stream;
  - starting `exec/R` directly with a hand-made environment;
  - command indirection that hides a launch from the transcript audit.
- **C routes:** same-user host rewrites of receipts, the Docker daemon, and
  md5 second preimages.

The lane covers R only, as its scope already states.

## 15. Build order

Rough size: the foundations took one session; the instrumentation and its
matrix about two more, and the rest one or two, plus the review rounds of
§2.2. `GATE_VERSION` becomes 1.3 when step 7 lands.

- [x] 2026-10-05 **F1, the record boundary** (`0ce7f25`):
  - `run-container`'s skeleton: lock, image id, copy, verify, baseline,
    mounts, `--init`, explicit log settings, and a named container removed
    if it fails to start;
  - the exec shim, plus a minimal hook that emits `START`, `END`, and the
    profile `LOAD`, with per-process tokens and the saved parent profile;
  - stream collection, the sealed receipt, launcher binding, and the
    census.
- [x] 2026-10-05 **F2, run and output binding** (`f07763a`; the lifecycle
  landed with F1):
  - per-run collection to `outputs/run-NN/files/` and `stdout.log`,
    consumption, and states;
  - `--detach` and `--finalise`;
  - comparison schema 1.1 output citations, and `target-unbound`;
  - the input-tree rule at gate time, and the credited-run closure.
- [x] 2026-10-05 **F3, issues and rulings** (`59f4e58`):
  - issue ids and fingerprints (`Issue`), and `rule-flags`;
  - raw and admitted coverage;
  - the admission rules in `persist-results` and `human-queue`.
- [ ] **Instrumentation:** the full hook (§8), with traces installed before
  the profile; `PKGBUILD` for `R CMD INSTALL`; the littler shim; the
  remaining census rules; and the launcher matrix.
- [ ] **Fresh computation** (§9).
- [ ] **Conversions** (§11) and the **static additions** (§10).
- [ ] **The transcript audit** (§12), which writes `transcript-audit.json`;
  the **remaining acceptance tests** (§13); and **the workflow switch**:
  the executor prompt and definition use `run-container`, with the §7
  prompt points; run records become mandatory for new attempts;
  `snapshot-code` is retired; and `coverage_creditable` is dropped. Then
  the final review, with the herskind pilot re-run (§2.2).

## 16. Questions for the reviewers

Reply by agent mail (Astra) or by agent mail or SendMessage (Fable), never on
GitHub. Classify each finding as D, A, B, or C (§2.1). For an A, give the
ordinary sequence of actions.

**Fable answered all five** (2026-10-05; folded into revision 1). **Astra's
answers are pending.**

1. **Stopping rule.** Do you accept §2 and the classification in §2.4? Name
   any point you would reclassify, and why.
2. **Channel.** Is Docker's log stream through `/proc/1/fd/2` acceptable as
   the authoritative channel, or should it be the FIFO with a host
   collector?
3. **Census.** Is the exec shim over `$R_HOME/bin/R`, paired with the hook
   by per-process token, sufficient for class A? Which ordinary launcher
   would bypass it?
4. **Conversions.** Are the accepted renderings in §11 a sound reading of
   §7(d)'s "every value is unchanged"?
5. **Contradictions.** Does this text contradict your review anywhere
   without saying so?
