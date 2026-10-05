# Executed-code audit of the five pilots (2026-10-04)

*Provenance: written on 2026-10-04 by the reproduction-lane subagent
(Opus 5.5) that built gate 1.1. Its harness does not let subagents write
report files, so it returned this text to the parent session, which saved it
verbatim on 2026-10-05 at the registrant's request. The parent session
checked the crema Table 1 comparison-basis finding (CREMA-3) at source. The
paper's Japan r is 0.1023, against 0.1003 in the comparison report's
"published" column. The other findings are the subagent's and have not been
re-checked line by line.*

**Status:** findings are candidates for Shawn's ruling. Nothing here is
ruled, and nothing changes a frozen instrument or study data.

**Ruling being implemented:** fail-and-uplift follow-on (4), 2026-10-04
(`wiki/planning/instrument-clarification-plan.md`, decision log). The pilots'
executed code is audited against the authors' originals before the
registered regression gate, to find undeclared repairs like dye's T02.

**Machine-readable record:** `findings.json` (19 findings, 16 downloads with
sha256, and 10 open questions). `audit-checks.py` re-runs the mechanical
checks. Its output is `audit-checks-output.json`.

## Scope and method

The audit covers each pilot's most recent attempt, plus attempt-01 where an
attempt-02 exists. The pilot verdicts in `studies/open-science-compliance/corpus/queue.yaml`
all cite the attempt-01 reports, so the regression gate's baseline rests on
attempt-01 too. That makes seven attempts in all.

The authors' original is the AP-12 version: the adjudication-log rule
(refined 2026-10-03) that fixes which deposit version is scored and
reproduced. Originals came from local copies first:

- attempt directories;
- the corpus store;
- the Docker image `diffusion-curve:run`, kept on sapphire, which still holds
  the crema run's code with its git history.

Missing originals came from public deposits: Zenodo, GitHub, and the
Elsevier supplement content delivery network (CDN). Requests went at most
one a second, with a descriptive User-Agent. Every URL and sha256 is in
`findings.json`. Nothing was behind a login. Nothing downloaded is
committed, because the files are publisher content, large, or both.

Every difference is classified:

- **(i)** a declared wrapper or routine environment mechanics (queued
  amendment 3, item 7(d));
- **(ii)** a mechanical change made in or to the authors' code rather than in
  a wrapper, including running a re-assembled or inlined copy instead of the
  authors' file. This is a process breach, not necessarily a repair;
- **(iii)** an edit that changes logic, indices, data selection, parameters,
  or the functions called (the T02 class). Whether it was declared, and
  whether its result is identical, are recorded separately.

Two kinds of finding fall outside those three classes and are kept apart:

- **(iv)** the executed code is a different authors' version from the AP-12
  version. This is not a reproducer edit;
- **(v)** credited values come from code the reproducer wrote and the
  authors' code does not contain, or from inputs the reproducer
  reconstructed.

## Summary

| Pilot / attempt | Executed against AP-12 original | (iii) candidates | Credited? |
|---|---|---|---|
| crema / 01 | Tag v2.0.0 plus a one-line authors' Dockerfile edit (ii), against AP-12 v1.0.0 (iv). The analysis code differs only in comments and one `save()` argument. | none | Table 1 credited against v2.0.0's own `table1.csv`, not the paper's Table 1 (iv) |
| dye / 02 | Transcription plus path edits inside 16 authors' files (ii, declared) | none | 22 targets rest on edited files |
| dye / 01 | Reproducer re-assembly; no authors' file run (ii) | **T02 index shift** (already ruled); bead-list restructure (declared, result-identical) | T02 credited qualitatively; 54/54 table values credited |
| herskind / 02 | `S2.R` byte-identical to Zenodo v2 (i only) | none | n/a |
| herskind / 01 | Re-implementation of v1 (ii, iv) | **Fig. 3 top-N parameter** (undeclared); `t` computed (result-identical) | Fig. 3 credited loosely; S3 291/291 exact |
| key / 01 | Inlined `OLE.test` plus a re-implemented loop (ii); the kept scripts are byte-identical to the supplement | none found | Mean and Extension % are reproducer-computed (v), 36 values credited |
| marwick / 01 | GitHub main `652e542`, 8 commits past AP-12 1.3 (iv) | none (no reproducer edits; self-reported) | Kendall's W credited; Fig. 2 mis-mapped |

**Headline:** apart from T02, no undeclared repair of the authors' own code
by a reproducer was found. The audit did find three other things the
regression gate needs to know:

1. **Re-implementation.** In three pilot attempt-01s (dye, herskind, key),
   no authors' file was executed at all.
2. **Wrong versions.** Two pilots (crema, marwick) executed authors' code at
   a version other than the AP-12 one. For crema, the comparison basis
   follows the wrong version.
3. **Edits inside the authors' files.** Dye attempt-02, the agentic run,
   made declared path edits inside the authors' files. The wrapper-only
   rule forbids this, but it was ruled after the run.

## Per pilot

### crema-et-al-2024, attempt-01 (pilot SUCCESSFUL)

**Identifying the executed code.** The image `diffusion-curve:run`
(`66feaed41a2b`, created 2026-02-08 on sapphire) is where the run's working
directories were copied from. Inside it, `git log` puts HEAD at
`c6d1aae`, which is tag **v2.0.0**. `git status` with file modes ignored
shows one content change, the Dockerfile. The AP-12 version is **v1.0.0**
(10.5281/zenodo.10782943). The Zenodo zip's md5 matches the published
checksum, and its root folder names commit `a0d1e66` (tag v1.0.0).

**Comparing the files.** Of the 50 v1.0.0 files, 14 are byte-identical to the
executed copies: `burial_icar.R`, both `post_check_*.R` scripts, the three
data-cleaning scripts, `table_main.R`, `utility.R`, `simulate_icar.R`, and
the raw data. The differences between v1.0.0 and v2.0.0 (`git diff`, run in
the image) are:

- `japan_abot.R` (+0/−8 lines) and `figures_main.R` (+0/−4): commented-out
  lines removed;
- `britain_abot.R` (+1/−7): comments removed, and `save()` writes one more
  object, `ppmat.gb.abot` (output only);
- `figures_esm.R` (+30/−32): object and file names corrected. v1.0.0 loads
  `simdata1.RData`, which v1.0.0 does not contain, so its supplementary
  figure script cannot run as published. The authors fixed this themselves
  in v2.0.0;
- the data objects `gbdata` and `burial`: `identical()` is TRUE across the
  two versions;
- the pre-computed posteriors and `table1.csv`: differ, because v2.0.0
  re-ran the model.

**Findings:**

- **CREMA-1 (ii):** the reproducer ran `sed` on the authors' v2.0.0
  Dockerfile, changing `RColoBrewer` to `RColorBrewer` (1 line, declared).
  The Dockerfile does not exist at v1.0.0.
- **CREMA-2 (i):** `rnaturalearthhires` was installed at run time from
  untagged GitHub HEAD. It was not pinned, and the log does not say where it
  was installed. It affects the Fig. 2 maps only.
- **CREMA-3 (iv), and a comparison-basis error:** the report's "Published
  (table1.csv)" column is v2.0.0's re-run, for example Japan r 0.1003. The
  paper's Table 1 equals v1.0.0's (Japan r 0.1023; corpus `extracted.txt`
  line 463). So the credited claim "byte-for-byte identical to the published
  table1.csv" compares v2.0.0 with itself.
  - The fresh Markov chain Monte Carlo (MCMC) medians all lie inside the
    paper's own 90% highest posterior density (HPD) intervals, so the
    stochastic verdict may survive re-basing.
  - That is for ruling (Q4).

### dye-et-al-2023, attempt-02 (shakedown; PARTIAL, 25/34)

**The original.** The authors' code exists only as listings printed in
supplement mmc1. The corpus store's `supplement-1.pdf` has sha256
`9b497fc2…7018b71`. The audit re-ran `pdftotext -layout` (Poppler 25.03.0)
and the attempt's `tools/transcribe_supplement.py`. All 16 regenerated files
are byte-identical to `authors-code-raw/`, so the transcription is
deterministic. Section 4 was spot-checked against the PDF text.

**DYE2-1 (ii, declared): path edits inside all 16 executed files.** Each
executed copy in `authors-code/` differs from its transcription:

- an 8-line header comment in every file;
- the `read_oxcal()` source (a URL, or the author-local path in section
  10.4) changed to `data/beads-1.csv`, the verified local copy with the same
  sha256;
- in sections 4 and 6, the output file moved to `outputs/`.

The functional lines changed are 2 in each of sections 4 and 6, 1 in each
of the others, and 0 in section 5. Gate 1.1 counts them with the header
included: 8 to 10 per file (`audit-checks-output.json`). Section 4's indices
and x-limits are untouched, so the T02 defect was left in place, as invariant
2 requires.

The edits were declared in `log.md` and marked inline (`LLMR-PATH:`). They
were made before the wrapper-only rule was ruled. The URL was live (HTTP
200), so a wrapper could have supplied the file without touching the
authors' code. 22 credited targets rest on the edited sections:

- T05 and T07–T09 (sections 7–9);
- T12–T20 (Supplement Tables 2–10);
- T24–T32 (section 10 text).

The edits change only where the file is read from (Q1).

**DYE2-2 (i):** per-section error capture, section 6 run after sections
7–10 (a declared deviation), and a null graphics device.

**DYE2-3 (i):** verification aids under run ruling R1. None of the
reproducer's files shares a substantive line with the authors' code.

### dye-et-al-2023, attempt-01 (pilot SUCCESSFUL; ruled too generous on T02)

`run-analysis.R` is a 476-line reproducer re-assembly. No authors' file was
executed (**DYE1-3, ii**). It shares 18 substantive lines with section 5 and
3 to 11 with each section-10 row.

**DYE1-1 (iii), T02, already ruled.** `c(3:5, 7, 9, 12:78)` became
`c(2:4, 6, 8, 11:77)`. It was declared as an "adjustment" that "yields
identical 72 interments", not as a repair. It was credited qualitatively
("72 interments confirmed"). Ruled 2026-10-04: fail-and-uplift, and
CANNOT_COMPARE stands.

**DYE1-2 (iii by 7(d)'s wording; declared; result-identical; not a
repair).** The bead list was rebuilt with named construction and `NULL`
assignment instead of the authors' positional
`names(bead_list) <- bead_names_r` and `bead_list[-c(5,8)]`, with
`as.list()` added in `tempo_plot()`.

- The log declares it "for robustness". It follows the then R-A prompt
  §3.4, which this build has now changed.
- The audit compared the 23 bead-type vectors, the `bead_names` additions,
  and all 14 updates (5.25–5.38) with the transcription. All are identical
  and in the same order.
- The authors' positional code runs unmodified in attempt-02 and gives the
  same 54 + 12 cells. So this is not a repair, but 7(d)'s text ("changes
  … indices … or the functions called") reaches it (Q2).

Finally, every other attempt-01 difference is mechanical. The input path and
output names changed, and validation and dead code were added.

### herskind-riede-2024, attempt-02 (shakedown; SUCCESSFUL)

**HER2-1 (i) only.** `data/Herskind&Riede_S2.R` is byte-identical to Zenodo
v2: its md5, `6760ccb3…`, equals the published checksum. The wrapper parses
the authors' file verbatim and evaluates it statement by statement, in
order. Its mechanics are:

- the working directory and a symbolic link to the data file;
- captures between the script's parts;
- cairo graphics devices;
- a fontconfig alias.

One authors' statement, `font_import(pattern = "GIL", prompt = FALSE)`, is
made error-tolerant. That is a boundary case for 7(d) (Q6). No reproducer
file shares a substantive line with `S2.R`.

### herskind-riede-2024, attempt-01 (pilot SUCCESSFUL)

`run-analysis.R` re-implements `S2.R` **v1** (10.5281/zenodo.10623550;
downloaded, and its md5 matches the published checksum) in functions and
loops (**HER1-4, ii**). No authors' file was executed, and the wrapper shares
33 substantive lines with v1.

**HER1-1 (iv):** the AP-12 version is v2, which computes Table 2 at bigram
level. It sets Fig. 3 thresholds per n-gram level: > 9 with 21 bars for
bigrams, > 4 with 23 for trigrams, and > 2 with 20 for quadrigrams. v1 has
only the bigram settings, and its script ends with a literal `n <- 4`.
Attempt-01's period summaries are quadrigram-level (Ertebølle maximum
7.925, against Table 2's bigram 4.10), but they were never compared with
Table 2.

**HER1-2 (iii candidate, undeclared):** the Fig. 3 PMI panels replaced v1's
literal `head(…, 21)` with "the number of n-grams with observed frequency
> 9".

- For bigrams the two agree (21).
- For trigrams, the panel shows 1 bar instead of 21 (v1) or 23 (v2), and the
  quadrigram panels were skipped.
- The report says "No algorithmic modifications", yet credits the figures as
  a "structural match" under labels that do not correspond to the paper's
  figures.

Pointwise mutual information (PMI) is the association score these panels
rank by.

**HER1-3 (iii-form, undeclared, result-identical):** `t <- 482` was replaced
by a count of non-empty motif strings. That count is 482 on the full data,
which is why the S3 expected frequencies match exactly. For the period
subsets `t` differs, but those subset scores are never used.

The pilot verdict rests on the S3 tables (291/291 exact). None of these
findings touches them (Q3).

### key-et-al-2024, attempt-01 (pilot PARTIAL)

The three supplement scripts kept in `scripts/` are byte-identical to the
Elsevier supplements `mmc1`–`mmc3`. The audit downloaded them; the article is
Creative Commons Attribution (CC BY) 4.0 per Crossref. But the scripts were
never executed: the Dockerfile copies only `run-analysis.R`.

**KEY-1 (ii):** `OLE.test` is copied from `mmc1` lines 26–45. It differs only
in trailing whitespace on two lines. The per-dataset loop (`mmc1` lines
48–61) is re-implemented in `run_ole()`. Inspection found no change of logic
or parameters, with the same:

- sort;
- k-window of 10;
- boundary transforms;
- alpha of 0.05;
- extraction.

The wrapper shares 15 substantive lines with `mmc1`. OLE is optimal linear
estimation.

**KEY-2 (v):** Mean and Extension % are computed by reproducer code. The
extension uses the confidence-interval estimates, and `mmc1` computes
neither quantity. 21 Mean values and 15 Extension % values were credited.
The two MAJOR_DISCREPANCY calls also rest on this formula, although the
report's own arithmetic from the paper's values supports them.

**KEY-3 (v):** the inputs were reconstructed from upstream sources:

- a subtype filter;
- a conversion from decigrams to grams;
- a type filter;
- a renamed column.

So far, 7(d)'s wrapper-boundary text covers only format conversion with a
value-identity check (Q5).

### marwick-2025, attempt-01 (pilot SUCCESSFUL)

The executed copy was not kept: no `wos-archaeology` image exists. The
executed version can still be identified as GitHub main `652e542`
(last push 2025-07-07), because it is the only version matching all of the
log's evidence:

- `paper.qmd` at 1107 lines (the log says 1108) with 14 code chunks;
- `renv.lock` with R 4.5.1 and 169 packages;
- the `fig-change-over-time_from_V1_1` chunk the log lists.

The AP-12 version is **1.3**: tag `c9332a8`, 10.5281/zenodo.15603267, whose
zip md5 matches the published checksum. In the 1.3 zip, all five files
checked equal tag 1.3.

**MAR-1 (iv).** The executed version is 8 commits past 1.3, including a
merged third-party pull request.

- `paper.qmd` has 78 lines changed (gate method):
  - the Shannon diversity index is computed differently,
    `group_by(id, journal_name)` instead of `group_by(id, x)` plus a join;
  - a figure chunk absent from the published paper is added.
- `renv.lock` moved from 152 to 169 packages, and from R 4.5.0 to 4.5.1.
- The Journal Citation Reports (JCR) CSV and the import script also changed.
  The Dockerfile render runs neither.

The Shannon index enters the Kendall's W test (`rank_mean_shannon`). The
report's p-value discrepancy (4.08 × 10⁻⁷ reproduced against 2.67 × 10⁻⁶
published) was put down to a data revision. The post-publication Shannon
change is an untested alternative. The report also credits "Fig 2 matches
published" to the added chunk, but the published Fig. 2 is the Bayesian
generalised additive model (GAM) image.

**MAR-2 (i):** the log reports no code modifications. This is self-reported
only (Q4).

## Gate 1.1 replay (illustrative)

The new check was run read-only on the real attempt directories. Its
manifests were written retroactively by the auditor, kept in the scratchpad,
and not committed. Results are in `findings.json` under `gate_1_1_replay`:

| Attempt | Result |
|---|---|
| dye / 02 (edits undeclared) | **fail**: 16 undeclared differences |
| dye / 02 (edits declared) | **flagged**: 16 flagged edits, sized |
| herskind / 02 | **identical** |
| key / 01 | **flagged**: no authors' file executed; the wrapper embeds 15 lines |
| dye / 01 | **flagged**: no authors' file executed; no pristine copy kept |
| herskind / 01 | **flagged**: no authors' file executed; no pristine copy kept |

## Open questions for Shawn

1. **Q1 (dye attempt-02):** the path edits inside the authors' files were
   declared, and made before the wrapper-only rule was ruled. Are they a
   process breach only, or do the 22 credited targets become
   fail-and-uplift?
2. **Q2 (dye attempt-01):** the bead-list restructuring is declared and
   result-identical, but it changes indexing form and the functions called.
   Is it (ii) or (iii)?
3. **Q3 (herskind attempt-01):** two parameter changes are undeclared. One
   is result-identical. The other affects Fig. 3 panels c–f, which were
   credited only qualitatively. Does either change the pilot baseline?
4. **Q4 (crema, marwick):** do the version deviations leave the pilot
   verdicts standing? The alternatives are to re-base them on the AP-12
   version, or to re-run that version in the regression gate. Crema's
   comparison basis was v2.0.0's own table.
5. **Q5 (key):** are the reproducer-computed Mean and Extension % values, and
   the reconstructed inputs, admissible as R1-style aids, or excluded from
   credit?
6. **Q6:** four wrapper boundary cases are not listed in 7(d):
   - error tolerance of a statement that computes nothing (herskind's
     `font_import`);
   - per-section error capture (dye attempt-02);
   - re-ordering sections (dye attempt-02);
   - an untagged GitHub install at run time (crema's `rnaturalearthhires`).
7. **Q7 (crema):** is an environment edit inside an authors' Dockerfile that
   is itself post-AP-12 class (ii)?
8. **Q8 (dye):** is a deterministic transcription, identified by the source
   PDF's sha256 and the tool, an acceptable "original" for byte identity?
9. **Q9 (gate 1.1 design):**
   - flags, not failures, for declared edits;
   - `--allow-missing-code-manifest` for legacy attempts;
   - five shared lines as the inlining threshold;
   - every reproducer code file must be declared.
10. **Q10:** the downloaded originals sit only in a transient scratchpad.
    Should the crema v1.0.0 and herskind v1 deposits (CC BY 4.0) go into the
    corpus store with manifest entries?

## Re-running the mechanical checks

1. Re-fetch the originals by the URLs in `findings.json`, and check each
   sha256. Lay them out as the header of `audit-checks.py` describes.
2. Run:
   `venv/bin/python studies/open-science-compliance/outputs/validation/executed-code-audit-2026-10-04/audit-checks.py --originals <dir>`

The crema image checks need sapphire's `diffusion-curve:run`. The commands
are the `git status`, `git diff v1.0.0 v2.0.0`, and `sha256sum` steps
described above, run in a `docker run --rm --network none` container.
