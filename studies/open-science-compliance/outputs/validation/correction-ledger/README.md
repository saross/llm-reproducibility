# Correction ledger for the §8 regression gate — version 1.0 (frozen)

**Status: FROZEN on 2026-10-12 as version 1.0 (ruling L15 (a)).
`correction-ledger-v1.0.json`, sha256 `189e8a33c9ceaa99eee18736e92314deff10862c51dcbdc2c0aa0e05dc090317`
(`correction-ledger-v1.0.json.sha256`).** Shawn ruled L1 to L4 and L6 to
L16 on 2026-10-09, L5 and L17 on 2026-10-10, and L18 (re-ruled on complete
options), L19, and L20 on 2026-10-11; the pre-freeze checks were completed
on 2026-10-12. The file does not change during the gate run, and a change
needs a new version, ruled and frozen in the same way. No run
may use any value here until the frozen copy is committed and its sha256 is
recorded in the gate's run configuration (amendment 3 §9 and §10 step 3).

## What this is

Amendment 3 to the Open Science Framework (OSF) registration, lodged
2026-10-08, re-bases the registered §8 regression gate. An audit of the
pilots' executed code (2026-10-04) found that the gate's baseline, the five
pilots' attempt-01 artefacts, is not what the gate assumes. Three pilots
executed a reproducer's re-implementation rather than the authors' files, and
two executed a version other than the one the version-selection rule (AP-12)
picks. Matching the pilots exactly would reward a pipeline for reproducing
their errors. §9 therefore adds a versioned **correction ledger**. For each
pilot target it records the selected source version and checksum, the printed
value and tolerance, any corrected expected value with its evidence tier and
ruling, the pilot's recorded value and outcome, the repair class, credit
eligibility, and the coverage treatment. The amended gate passes against the
frozen ledger; the strict comparison against the pilot artefacts is still
reported.

## Files

| File | Role |
|---|---|
| `correction-ledger-v1.0.json` | The frozen ledger, version 1.0 (renamed from the draft `correction-ledger.json` at the freeze, so no draft copy can drift from it) |
| `correction-ledger-v1.0.json.sha256` | Its sha256, for the gate's run configuration |
| `correction-ledger.md` | Rendered review copy (`render-ledger.py`); never edit it by hand |
| `render-ledger.py` | Renders the JSON as Markdown |
| `check-printed-values.py` | Re-checks every printed value against its cited PDF page |
| `deposit-checksums/crema-v1.0.0.sha256` | sha256 of all 50 files in crema's v1.0.0 deposit |
| `deposit-checksums/marwick-1.3.sha256` | sha256 of all 116 files in marwick's 1.3 deposit zip |
| `evidence/l9-dye-section-07/` | Operator run of dye's section 5 and 7 code, byte-identical (L9) |
| `evidence/crema-figures-content/` | Pilot against v1.0.0 figures, pixel by pixel (L4, L5) |
| `evidence/crema-figures-probe/` | v1.0.0's figure script run in a probe environment (L5, L18) |
| `evidence/marwick-fig2-probe/` | Marwick's switched-off fitting chunk run and Fig. 2 redrawn (L17, L19, L20) |

## How it was drafted

- **Target list.** No pilot attempt-01 has a locked target list: the pilots
  predate that instrument. The draft takes each attempt-01 comparison report's
  compared items, mapped to the paper's own display items (ruling L1), and
  lists every exclusion with its reason (L2).
- **Values.** Printed values come from the corpus store's PDFs and the
  selected deposits only. Four read-only Opus subagents transcribed them, and
  every value was then checked mechanically. `check-printed-values.py` finds
  239 of 239 text-layer values on their cited pages; the five figure labels
  drawn inside herskind's Fig. 3 raster were read on a 250 dpi render. The
  pilot values were checked against the pilot reports and output files by
  script.
- **Shakedown evidence.** The shakedown's attempt-02 results appear only as
  evidence that the authors' unmodified code yields a value, and are labelled
  so, as §9 requires.
- **Deposits fetched on 2026-10-09** (public, no login): crema v1.0.0 from
  Zenodo (sha256 and md5 match the audit and the published checksum) and
  marwick's rendered `paper.docx` at tag 1.3 from GitHub (git blob hash equals
  the tag's tree entry). A Zenodo re-download of marwick's 1.3 zip returned
  HTTP 504 and was not retried.

## Findings beyond the executed-code audit

1. **Marwick: the published Kendall's W is 0.64, not about 0.70.** The pilot
   recorded the published value as "~0.70 (moderate to strong)" and credited
   its 0.7 as an exact match. It also said PC1's variance is not printed (the
   paper prints 71 %). Version 1.3's own rendered `paper.docx` reads W 0.64,
   p = 2.67 × 10⁻⁶, and PC1 71 %, the printed values. So all three of the
   pilot's marwick differences trace to running post-1.3 code (audit MAR-1),
   and the "data revision" explanation is unsupported.
2. **Key: the two "paper errors" are the pilot's own transcription slip.**
   The paper prints Midland Thickness Extension % = 19.6 and Clovis Mass =
   3.1; the pilot's wrapper swapped them. Audit ruling Q5(ii), and the example
   in lodged amendment 3 §7(d), rest on the swap (ruling L16). The pilot also
   mis-recorded Olduvai Thickness Mean (42.3 for the printed 42.2), the
   paper's DOI, and its author list.
3. **Dye: three of the five "published" branching values are not printed.**
   0.83, Amethyst→Disc 0.87, and Cowrie→Disc 1.00 match the pilot's own
   output; the paper prints only Cowrie→Disc 0.87. The report lists 53
   comparisons, not 54, and leaves out six printed zeros. Its figure numbers
   (7 and 8) are the supplement's stale cross-references; the paper's are
   Figs 3 and 4. The corpus store's `vor.pdf` is the accepted manuscript.
4. **Crema: confirmed at source.** The printed Table 1 equals v1.0.0's
   `table1.csv` in all 24 cells. 18 of the pilot's 24 archived-posterior
   values differ from it. The pilot report swaps the labels of Figs 1 and 2
   and names the wrong journal.
5. **Herskind: the pilot's figure labels match none of the paper's figures.**
   Its frequency table silently differs from the printed Table 1, which has
   eight paper-error cells (shakedown ruling 3), and its "top PMI"
   (pointwise mutual information) values are not the global top five.
6. **Marwick: Fig. 2 cannot be redrawn from the deposit.** The published
   image comes from `supplement-GAMS-details.qmd`, whose model-fitting chunk
   is marked `eval: false` with the authors' note "this takes a few hours"
   (five brms models, 4 chains of 50,000 iterations each). Its saved fit,
   `results_brms.RData`, is not in the tag 1.3 tree. Found 2026-10-09 while
   applying ruling L11; it raises ruling L17.
7. **Crema: the pilot's Figs 2 to 4 are not v1.0.0's.** Drawn from version
   2.0.0's archived results, they differ in content from the deposit's own
   v1.0.0 figures: the simulation fits' bands in Fig. 2 (panels a and b) and
   the prediction envelopes in Figs 3 and 4. Figs 1 and 5 render
   pixel-identical. Found 2026-10-10 while applying ruling L5
   (`evidence/crema-figures-content/`).
8. **Crema: v1.0.0's archived inputs do not regenerate its own Fig. 2
   panel a.** The probe regenerates Figs 1, 3, 4, and 5 pixel-identical to
   the deposit's PDFs. From v1.0.0's `post_sim1a.RData`, panel a's 95 %
   band at the curve's late end reads 0.592 to 0.729; the version of record
   reads 0.567 to 0.691, as do the deposit's own `figure2.pdf` and the
   pilot's render from v2.0.0's archive. Across the whole curve the bands
   differ by up to 0.082 on the rising limb. The regenerated band still
   contains the true curve at every year, so §5.1's recovery claim holds.
   The images do not identify the posterior the authors used. Found
   2026-10-10 by the L5 probe and confirmed on 2026-10-11 in an
   environment honouring every supplied pin (`evidence/crema-figures-probe/`);
   it raises ruling L18. The deposited posterior and unmodified code support
   the regenerated panel, while the deposit's own figure agrees with the
   paper: an inconsistency within the supplied materials that does not show
   which artefact is in error. Ruled L18 (a) on 2026-10-11: a minor
   discrepancy, reported as a finding about the deposit.
9. **Marwick: the deposit's two environment specifications disagree on
   R.** The `Dockerfile` builds on `rocker/verse:4.4.1`; `renv.lock`
   records R 4.5.0. Amendment 3 §7(d) sets no precedence between them. The
   probe followed the Dockerfile and honoured all 152 package pins. Found
   2026-10-11 by the L17 probe, and ruled L20 (a): the gate keeps R 4.4.1
   and reports the conflict beside the verdict as a minor discrepancy in
   the deposit.

**Astra's review (2026-10-09, at `9b66683`)** confirmed the key and marwick
printed-value findings independently and found two errors, both fixed in
ledger 0.2.1-draft:

- **B1. Two marwick figures were labelled unchanged though their content
  changes.** The pilot's Fig. 1 and Fig. 3, rendered from 652e542, differ
  from the version of record in the diversity panels and in Fig. 3's Borda
  ranking, not just in styling. MAR-T09 and MAR-T11 are now corrected, with
  the pilot figures kept as their historical baseline; marwick's unchanged
  set falls from eight to six. Fig. 5 (MAR-T13) was checked the same way
  and matches, so it stays unchanged.
- **B2. HER-T02 tightened the pilot's precision without a correction.**
  Amendment 3 §9 compares an unchanged deterministic target at the pilot
  table's precision, after the same rounding. HER-T02 now compares at 3 dp;
  the 4-dp figure labels stay with HER-T03 (corrected).

**Astra's re-review (2026-10-11, at `d6beec4`)** accepted the compliant
crema build (B3) and supported L18 (a), with three changes, all applied in
ledger 0.3.5-draft. L18's recommendation no longer excludes PAPER_ERROR
categorically, since the evidence shows conflicting author artefacts
without showing which is wrong. L18 (a) now covers the whole figure and
names its reference. MAR-T10 gains explicit content and a tolerance from
the authors' published intervals (L19), and marwick's conflicting R
versions are recorded as a conflict, not as a fallback (L20). The probe
write-ups were corrected where they claimed more than their checks show.

Shawn accepted L16's finding on 2026-10-09: the erratum log's Entry 7
records the key slip, and the public correction is queued for the next OSF
amendment.

## Sets and gate selection

| Paper | Testable unchanged targets | Corrected | Expected verdict (pilot) |
|---|---|---|---|
| crema | 2 (registered leg: Figs 1 and 5) | 4 | SUCCESSFUL (SUCCESSFUL) |
| dye | 11 | 2 | PARTIAL (SUCCESSFUL) |
| herskind | 2, including the 1,601-cell S3 table | 2 | SUCCESSFUL (SUCCESSFUL) |
| key | 0; all nine targets untestable | 2 | BLOCKED (PARTIAL) |
| marwick | 6 | 7 | SUCCESSFUL (SUCCESSFUL) |

**Ruled (L6 (c), 2026-10-09): the gate runs dye, herskind, and marwick,**
plus crema's mandatory archived-posterior leg, which covers Table 1 and the
five main figures (L5 (c)). Key is not a gate paper; its
record keeps the expected verdict for the strict comparison. Each paper's
agentic run passes the API review gate before it starts.

## Rulings (details in `correction-ledger.md`)

Ruled by Shawn on 2026-10-09:

- **L1 (a):** the de facto target list. **L2 (a):** exclusions listed with
  reasons. **L3 (a):** scope changes extend the target. **L4 (a):**
  "unchanged" ignores pilot credit eligibility. **L6 (c):** dye, herskind,
  and marwick. **L7 (a):** testable unchanged targets.
- **L8 (a):** styling-only differences count as reproduced. **L9 (b):** the
  two operator runs are admitted as tier-3 evidence. **L10 (a):** dye
  PARTIAL. **L11 (a):** a static include never counts. **L12 (a):**
  marwick's printed values stand. **L13 (a):** review counts kept, checked
  before freezing. **L14 (a):** key BLOCKED. **L15 (a):** freezing.
  **L16 (a):** erratum-log Entry 7; OSF note with the next amendment.

Ruled by Shawn on 2026-10-10:

- **L5 (c):** crema's leg covers Table 1 and all five main figures, drawn by
  v1.0.0's `figures_main.R` in the same run. Figs 2 to 4 become corrected
  (finding 7); Figs 1 and 5 stay unchanged. Shawn also asked for a rule, or
  at least a heuristic, separating key figures from ancillary ones in the
  study's runs. It is queued for amendment 4 and does not apply in the gate.
- **L17 (c), probe first:** marwick's Fig. 2 stays in the gate, expected
  REPRODUCED_VISUAL. The approved plan names the operator step: the
  supplement's `eval: false` fitting chunk runs verbatim from a wrapper,
  then the supplement renders unchanged. (a) was withdrawn after Astra's
  review. (b) would have needed the plan to forbid the attempt, rehearsing
  the opposite of what the study's runs must do. If the probe fails, Shawn
  re-rules with (b) the fallback. It did not: on 2026-10-11 the fit ran in
  19.2 hours on zbook and the redrawn figure matched the version of record
  in content, with two Pseudo R² labels differing in the fourth digit
  (`evidence/marwick-fig2-probe/`).

Ruled by Shawn on 2026-10-11:

- **L18 (a), re-ruled:** CREMA-T04 (Fig. 2) is expected MINOR_DISCREPANCY
  against the version of record (SUCCESSFUL with note). Shawn first ruled
  (a) on 2026-10-10; Astra's review found the options lacked the
  PAPER_ERROR route (amendment 3 §7(a)), the comparison covered only the
  plateau, and the gate's expected content was unstated. Put again with
  four options and whole-curve evidence, and ruled (a) again. The gate's
  figure must match the one regenerated from v1.0.0's archive in the
  compliant environment, in all three panels, so the label alone cannot
  pass. Shawn: "exactly the kind of minor error we should point out,
  without failing the entire run".
- **L19 (a):** MAR-T10 (marwick's Fig. 2) must match the authors'
  deposited image in content, and each Pseudo R² label must fall within
  its model's 95 % interval in the authors' deposited supplement, not
  within the probe's own agreement.
- **L20 (a):** the gate keeps the Dockerfile's R 4.4.1 and reports, beside
  the verdict, the package pins honoured in full and the runtime conflict
  with the lockfile's R 4.5.0, documented as a minor discrepancy in the
  deposit (finding 9). Shawn: "these discrepancy reports are extremely
  valuable".

## Before freezing

- [x] 2026-10-09 Rule L1–L4 and L6–L16 and apply them to the JSON
      (ledger 0.2.0-draft, re-rendered).
- [x] 2026-10-10 Rule L5 and L17 and apply them (ledger 0.3.0-draft,
      re-rendered).
- [x] 2026-10-10 Probe crema's figures (L5): Figs 1, 3, 4, and 5
      regenerate pixel-identical; Fig. 2's panel a does not (finding 8,
      `evidence/crema-figures-probe/`).
- [x] 2026-10-11 Re-rule L18 on the complete options and apply it (a);
      rule and apply L19 (a) and L20 (a) (ledger 0.3.5-draft, re-rendered).
- [x] 2026-10-11 Rebuild crema's probe environment honouring every
      session-info pin, attached and namespace-only (Astra's B3), assert the
      full inventory, and confirm the figures there: 67 of 68 pins honoured,
      nimbleCarbon 0.2.4 to 0.2.1 by the bounded search, and every result
      identical to the first probe's (`evidence/crema-figures-probe/`).
- [x] 2026-10-11 Probe marwick's Fig. 2: the fitting chunk run verbatim
      from a wrapper on zbook, then the supplement rendered unchanged and
      the figure compared with the version of record (L17). Trend lines
      within one pixel and data points identical; one build repair, no
      version substitution; 152 of 152 lockfile pins installed
      (`evidence/marwick-fig2-probe/`).
- [x] 2026-10-12 Hold the crema v1.0.0 and herskind v1 deposits in the
      corpus store with manifest entries (audit Q10), with marwick's 1.3
      zip. Every hash equals the audit's or ledger's record, and herskind's
      md5s equal Zenodo's published checksums (main `280165d`).
- [x] 2026-10-12 Hold L18's reference figure (crema v3 `figure2.pdf`,
      sha256 `cf61c685…`) in the corpus store with a manifest entry, so the
      gate's comparison can reach it; it is a render of a third-party
      figure, so it stays out of git (main `280165d`).
- [x] 2026-10-12 Hash marwick's files inside the 1.3 zip
      (`deposit-checksums/marwick-1.3.sha256`): the four cited files equal
      their GitHub hashes, and L19's two files are added. Confirm review
      counts in `paper.qmd` at 1.3 (L13): typed prose at line 974, but the
      deposited `JAS AER data analysis.csv` gives both, 25 manuscripts and
      11 published in JAS, so the gate can verify them from the authors'
      data.
- [x] 2026-10-09 Operator runs for L9: dye's section 5 and 7 code
      byte-identical (`evidence/l9-dye-section-07/`); herskind's Fig. 4
      check already used the authors' function verbatim.
- [x] 2026-10-09 Admit the two runs as tier-3 evidence (L9 (b)).
- [x] 2026-10-12 Commit the ruled copy as `correction-ledger-v1.0.json`
      (sha256 `189e8a33c9ceaa99…`, in `correction-ledger-v1.0.json.sha256`) and
      record its sha256 in the run configuration (L15). The gate's run
      configuration does not exist yet: whoever writes it copies the hash
      from the `.sha256` file, and its launch commit must contain this
      file.

## Re-running the checks

```bash
python3 check-printed-values.py      # needs pdftotext and the corpus store
python3 render-ledger.py             # regenerates correction-ledger.md
```
