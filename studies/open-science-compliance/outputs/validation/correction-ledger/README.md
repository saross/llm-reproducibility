# Correction ledger for the §8 regression gate — DRAFT

**Status: DRAFT for Shawn's ruling (2026-10-09). Not ruled, not frozen, and
not hashed.** No run may use any value here until the registrant has ruled
the open questions, the ruled copy is committed, and its sha256 is recorded in
the gate's run configuration (amendment 3 §9 and §10 step 3).

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
| `correction-ledger.json` | The ledger: the artefact to be ruled, frozen, and hashed |
| `correction-ledger.md` | Rendered review copy (`render-ledger.py`); never edit it by hand |
| `render-ledger.py` | Renders the JSON as Markdown |
| `check-printed-values.py` | Re-checks every printed value against its cited PDF page |
| `deposit-checksums/crema-v1.0.0.sha256` | sha256 of all 50 files in crema's v1.0.0 deposit |

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

## Sets and gate selection

| Paper | Testable unchanged targets | Corrected | Expected verdict (pilot) |
|---|---|---|---|
| crema | 0 (registered leg, Table 1 only) | 1 | SUCCESSFUL (SUCCESSFUL) |
| dye | 11 | 2 | PARTIAL (SUCCESSFUL) |
| herskind | 2, including the 1,601-cell S3 table | 2 | SUCCESSFUL (SUCCESSFUL) |
| key | 0; all nine targets untestable | 2 | BLOCKED (PARTIAL) |
| marwick | 8 | 5 | SUCCESSFUL, provisional on L11 (SUCCESSFUL) |

The recommendation (L6) is dye and marwick, plus crema's mandatory
archived-posterior leg. Herskind is the alternative if elements, not targets,
measure the unchanged set (L7).

## Rulings needed (details in `correction-ledger.md`)

- **L1:** the de facto target list. **L2:** exclusions. **L3:** scope
  changes. **L4:** "unchanged" ignores pilot credit eligibility. **L5:**
  crema's role. **L6:** gate papers. **L7:** how to measure an unchanged set.
- **L8:** the visual tolerance. **L9:** evidence for two paper-error
  corrections (recommend an operator confirmation run). **L10:** dye's
  verdict. **L11:** marwick's static figure includes. **L12:** marwick's
  mis-recorded values. **L13:** marwick's review counts. **L14:** key's
  verdict. **L15:** freezing. **L16:** key's swapped cells and the
  amendment's example.

## Before freezing

- [ ] Rule L1–L16 and apply the rulings to the JSON (then re-render).
- [ ] Hold the crema v1.0.0 and herskind v1 deposits in the corpus store with
      manifest entries (audit Q10).
- [ ] Hash marwick's files inside the 1.3 zip; confirm review counts in
      `paper.qmd` at 1.3 (L13).
- [ ] Confirmation runs for L9, if ruled (b).
- [ ] Commit the ruled copy as `correction-ledger-v1.0.json` and record its
      sha256 in the run configuration (L15).

## Re-running the checks

```bash
python3 check-printed-values.py      # needs pdftotext and the corpus store
python3 render-ledger.py             # regenerates correction-ledger.md
```
