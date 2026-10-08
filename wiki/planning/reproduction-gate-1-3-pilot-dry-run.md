---
title: "Gate 1.3 — herskind pilot dry run (2026-10-09)"
tags: [reproduction, validation, mechanical-verification]
created: 2026-10-09
updated: 2026-10-09
status: evidence-for-final-review
---

# Gate 1.3: herskind pilot dry run

**What this is.** The final review of gate 1.3 includes one real pilot
re-run through the whole lane, herskind's (specification §2.2, in
`wiki/planning/reproduction-gate-1-3-design.md`). The whole lane means the
agentic workflow: planner, human plan approval, executor, gate, and
adversarial reviewer. Shawn has to start that. This dry run does the
execution layer's part now, with no agent and no model call. Herskind's
existing attempt-02 materials ran through `run-container`, and the
gate 1.3 integrity check read the result. It gives the reviewers real run
records, and it tests the account of loads against a real analysis rather
than fixtures.

## Method

- **Materials.** These are copied from
  `studies/open-science-compliance/outputs/herskind-riede-2024/reproduction/attempt-02/`
  into a scratch attempt: the `Dockerfile`, `run-analysis.R` (the
  executor's wrapper from the 2026-10-03 shakedown), and `data/`. The
  copies are byte-identical.
- **Manifest.** Attempt-02 predates the authors' code manifest, so one was
  written for the dry run. It names one original, `Herskind&Riede_S2.R`,
  with a pristine copy, executed at `data/Herskind&Riede_S2.R`. Its anchor
  is the committed evidence pack
  `corpus/evidence-packs/harvest-2026-10-04/herskind-riede-2024.json`,
  record `zenodo:10.5281/zenodo.10801706`, which publishes md5
  `6760ccb30ecc1de7c280bc1e0fa182e5` for the file. The executed copy has
  that md5, and the gate reported the anchor `verified`. The wrappers are
  `run-analysis.R` and the `Dockerfile`.
- **Run.** The image was the existing `llmr-herskind-riede-2024-attempt-02`
  (id `2d31bf850733`, built 2026-10-03), mounted at its `WORKDIR`,
  `/attempt`. The launch commit was PR #7's head at the time, `3d45454`.
- **Check.** `check_code_integrity`, with the anchor root and launch
  commit set to the worktree, at `3d45454` and again at `f5b77d7`.

## Results

**The run.** The run sealed `complete`, with exit 0 and one R process.
The census, the stream, and the collection were all whole, and the run
recorded no problem.

**Results unchanged by the lane.** All 34 CSV and text outputs are
byte-identical to attempt-02's committed outputs, which ran outside the
lane on 2026-10-03, and so are the PNG figures checked. `console-plots.pdf`
differs at one byte offset at the same size, consistent with the creation
time cairo embeds. Attempt-02 also kept a `run-console.log` that its
executor redirected by hand; the lane collects the console as
`outputs/run-01/stdout.log` instead.

**Findings at `3d45454`, before the fix:**

- `executed-not-loaded` on `S2.R`, with `originals_loaded` empty, so
  `check-attempt` would have excluded every target as "no credited run
  loaded an authors' file". **Wrong.** The wrapper evaluates `S2.R`
  verbatim, in its own order, one `#PART` at a time
  (`parse(text = chunk)`, then `eval`), so no text matched the whole file.
  This was a defect: the specification counts herskind's
  "parse-and-evaluate wrapper" as accounted for.
- `external-code-reference` for `Herskind&Riede_S2.R`. Its basename exists
  twice, as the pristine and the executed copy, and the reference did not
  resolve. Noise.
- `image-stale`: the 2026-10-03 image carries no `llmr.dockerfile.sha256`
  label. This is expected, since the label came in with gate 1.3; a real
  re-run builds with it.
- The static obligations expected of this wrapper: `dynamic-evaluation`
  on the wrapper and on the `Dockerfile` (its build-time assertion uses
  `Rscript -e`), and `wrapper-semantics`.
- 127 `unmatched-text` obligations (below).

**The fix, `f5b77d7`.** Within a process, texts that are contiguous,
in-order slices of an R original's lines now run that original when they
cover every code line; comment and blank lines may be skipped. Slices
that leave code unrun are flagged as an omission (`original-partly-run`).
A basename shared by a pristine and an executed copy resolves to the
executed copy. After it, the eight `#PART` slices bind
(`text-original-part: 8`), `S2.R` is loaded, and the first two findings
are gone. What remains is the image label, the static obligations, and
119 `unmatched-text` obligations.

## The open question: 119 texts built at run time

The 119 remaining texts were traced with a probe copy of the hook that
printed each text and its callers (a diagnostic only, not committed).
They are code evaluated from strings built at run time, which the
specification makes obligations by design (§14, first limit):

| Source | Unique texts | Examples |
| --- | --- | --- |
| The authors' own subset conditions, built from the data and parsed inside dplyr's data mask | 107 | `A1 == 1 & A24 == 1`, `C1 == 1 & F12 == 1 & G1 == 1` |
| glue placeholders in rlang and cli message templates | 9 | ` arg `, ` fn `, ` pkg ` |
| ggplot2 3.5.0 parsing a scale's or a theme element's name (`rlang::parse_expr`) | 3 | `scale_x_continuous()`, `scale_y_discrete()`, `theme(legend.position.inside)` |

That is 119. The probe saw 142 unique texts in all, matching the run's
142 `TEXT` events; the other 23 are the wrapper's eight slices, now bound,
and 15 data.table option settings evaluated while its namespace loaded,
which count as package code. Each unique text is one obligation, because
the hook reports each md5 once per process.

**Why it matters.** Each is a separate issue needing its own human
ruling. Nothing here passes silently: the gate is behaving as specified.
But a reviewer cannot judge an md5, and 119 rulings for one ordinary
dplyr and ggplot2 analysis would make admission impractical. herskind is
not unusual; any analysis using these packages does the same.

**A possible design, for the reviewers and Shawn, not built:**

1. The `TEXT` event carries a short text verbatim (up to 512 bytes,
   hex-encoded) and its verified caller, as `CONN` now does. A reviewer can
   then read what ran.
2. The lane lists package-internal templates, matched against the verbatim
   text, whose only holes are string literals or bare names: ggplot2's
   `scale_<aesthetic>_<type>()`, and glue placeholders that are a single
   name.
3. The remaining texts are grouped into one obligation per (place,
   caller), listing them, rather than one each. The authors' 107 subset
   conditions would then be one ruling with all 107 shown.

Each piece changes the evidence a ruling rests on, so the design needs the
reviewers' classification before it is built. Is the noise class A (an
ordinary route the gate mishandles), or an operability limit outside §2's
classes? Shawn decides whether to build it before the final review.

## Reproducing this

The dry run used scratch scripts, not committed. In outline:

1. Copy the three inputs into a new attempt directory, with a pristine
   copy of `S2.R` under `authors-code-raw/`.
2. Write the manifest as above.
3. Call `start_run(attempt, "llmr-herskind-riede-2024-attempt-02",
   "run-analysis.R", launch_commit=<head>)`, then `finalise_run`.
4. Call `check_code_integrity(attempt, manifest, schema,
   anchor_root=<repo>, launch_commit=<head>,
   plan_slug="herskind-riede-2024")`.
