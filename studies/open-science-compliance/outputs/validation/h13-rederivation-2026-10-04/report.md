# H13 gate statistics: blinded independent re-derivation (2026-10-04)

An independent, fresh-context re-derivation of the two validation-phase gate
statistics for six FAIR (Findable, Accessible, Interoperable, Reusable)
scoring arms: 3-run **stability**, and **concordance** against the E8-v2
re-derived human reference, the latter over all items and with the
"beyond instrument" (BI) items excluded. The derivation was written without
sight of any other derivation of these figures. The blinding rules and the
full access log are in §5.

- Script: `h13-rederive.py` (this directory). Run it from the repository root
  with `python3 studies/open-science-compliance/outputs/validation/h13-rederivation-2026-10-04/h13-rederive.py`.
- Output: `h13-results.json` (this directory). It holds every statistic as an
  exact count over its denominator, every miss item with its direction, and
  the full item-level score matrix (three runs plus the reference) per arm.
- Cross-check: a second, independently written computation (NumPy arrays,
  with prefix-parsed rather than table-mapped reference keys) reproduced every
  stability, reading-A, reading-B, and reading-C count for all six arms. That
  check was run ad hoc in the shell and is not saved as a file.

## 1. Operationalisations derived from the registered text

### 1.1 Sources

- Registration (Open Science Framework (OSF), DOI 10.17605/OSF.IO/DQNHG):
  `prereg/phase-2-preregistration-draft.pdf` §7.1 and §8. I checked the
  wording against `prereg/osf-registration-summary.txt`, whose §7.1 and §8
  lines match.
- Amendment 1 (lodged 2026-08-03): `prereg/amendment-1-draft.md` §3, and
  `prereg/osf-amendment-1.txt`. The two files' §3 text is identical.

### 1.2 Item unit and denominator

> "15 binary GO-FAIR sub-principles (F1–F4, A1–A2 incl. A1.1/A1.2, I1–I3, R1
> incl. R1.1–R1.3), scored independently for data (/15) and code (/15); never
> aggregated into a combined score." (Registration §7.1)

> "The stability check scores all five pilot papers, where the registration
> requires at least three. This raises the item count from 90 to 150"
> (Amendment 1 §3)

The figure of 150 equals 5 papers × 30, so an **item** is one paper × one
section (data or code) × one sub-principle, and each item carries one binary
score per run. The arithmetic of 90 = 3 × 30 confirms that both sections
enter the same item pool. Data and code scores are never summed: every item
is compared at sub-principle level, and no paper or section totals enter any
statistic.

### 1.3 Stability

> "Acceptance threshold: mean per-sub-principle agreement ≥ 0.90 across runs.
> If below threshold, the census is scored by majority vote of three
> independent runs per paper" (Registration §8(a))

> "Agreement statistic. The 3-run stability check uses the unanimity
> proportion, the proportion of sub-principle items on which all three runs
> agree. This is the strictest of the candidate agreement definitions."
> (Amendment 1 §3)

**Operationalisation:** stability = (number of items for which run 1 = run 2
= run 3) / 150. An arm clears the gate when this is ≥ 0.90, which requires
at least 135 of 150 items.

**Interpretive note (no alternative needed).** The registration's phrase
"mean per-sub-principle agreement" could also be read as the mean of 15
per-sub-principle unanimity rates. The design is balanced, with exactly 10
items (5 papers × 2 sections) per sub-principle, so that mean equals the
pooled proportion identically. The script asserts this equality and records
both values for every arm (for example, sonnet-5 gives 64/75 = 128/150).
Amendment 1 fixes unanimity as the agreement definition, so I computed no
other stability statistic.

### 1.4 Concordance

> "any model that passes both (a) the registered 0.90 stability gate and (b)
> a concordance floor of at least 0.90 (same statistic) against the pilot
> reference scores is eligible, and among eligible models the cheapest scores
> the census." (Amendment 1 §3)

The registered text leaves open how the "same statistic", a three-run
unanimity proportion, applies when three runs are compared with a single
reference score. I computed four readings.

**Reading A, primary: four-way unanimity.** An item is concordant if and only
if run 1 = run 2 = run 3 = the reference score. The statistic is the
concordant count divided by the number of items.

- *Reasoning.* The literal definition of the statistic is "the proportion of
  sub-principle items on which all three runs agree". Extending "agree" to
  include the reference, so that all three runs agree with the reference, is
  the most direct transfer of that definition. It needs no extra aggregation
  choice (no mean, minimum, or vote), and it keeps the amendment's stated
  preference for "the strictest of the candidate agreement definitions".
- *Property to note.* Every item on which the runs are not unanimous is
  automatically a reading-A miss, so reading-A concordance can never exceed
  stability. Reading A therefore mixes instability with inaccuracy. §3 splits
  each arm's misses into split-run misses and unanimous-wrong misses so that
  the two sources can be told apart.

**Reading B, alternative: per-run agreement.** Each run is compared with the
reference on its own. With two raters (one run and the reference), "all
agree" reduces to simple percent agreement. I report the pooled proportion
over all run-items (denominator 450, or 423 with BI excluded). This equals
the mean of the three per-run proportions, because the denominators are
equal. I also report each run's proportion and the minimum, for a reading in
which every run must clear the floor.

- *Reasoning.* The registration's other machine-versus-reference comparison,
  the human validation subsample in §8, uses "Per-sub-principle percent
  agreement". In addition, an arm that passes the stability gate scores the
  census with a single run, so the accuracy of a single run is what matters
  in operation.

**Reading C, alternative: majority vote.** The arm's score for an item is the
majority of its three binary runs, which is always defined, and that score is
compared with the reference.

- *Reasoning.* Registration §8(a) names majority vote as the census scoring
  mode for an arm that fails stability. This reading therefore measures the
  accuracy of the scores that would be used in that case.

**Reading D, supplementary and not recommended: conditional on unanimous
runs.** Among the items on which the three runs agree, this is the
proportion whose shared score equals the reference.

- I report it only for completeness. Its denominator changes from arm to arm
  and is no longer "sub-principle items" in the registered sense. It also
  rewards instability, because unstable items leave the denominator.

**Direction of misses.** Every score is binary, so a missed item has exactly
one direction:

- **Over-credit:** the reference is 0 and at least one counted arm score
  is 1.
- **Under-credit:** the reference is 1 and at least one counted arm score
  is 0.

No item can be both. Reading B counts direction per run-item, reading C per
majority score, and readings A and D per item.

**BI exclusion.** An item is BI-tagged when its reference leaf field
`beyond_instrument` is a non-empty list. The BI-excluded statistic drops those
items from both the numerator and the denominator.

**Gate comparison.** Comparisons are exact rational ones (`fractions.Fraction`
≥ 9/10), with no intermediate rounding. Proportions are rounded to 3 decimal
places for display only. Minimum counts to clear the gate are 135/150,
127/141, 405/450, and 381/423.

### 1.5 Other interpretive choices

1. **Reference values.** The brief designates the E8-v2 reference as the
   "pilot reference scores". I used each leaf's `present` value and ignored
   `old_present`, which holds the pre-re-derivation values.
2. **Missing or unscoreable values.** Registration §7.1 says "Unscoreable
   sub-principles score 0". This rule was never needed: every arm, run, paper,
   and section has all 15 items, each scored as integer 0 or 1 (§2). Had a
   score been missing, the script would have reported it and dropped the item
   for that arm rather than imputing a value. No item was dropped.
3. **Section marked unavailable but scored.** One section is flagged
   `available: false` but still carries item scores (§2). I used its scores
   exactly as recorded and give the sensitivity of the results in §4.
4. **Arm effort labels.** The effort level is taken from the directory names
   and the brief. The payload receipts record a model identifier but no
   effort level, so effort cannot be verified from the payloads.

## 2. Data checks

- **Payloads.** All 90 files exist (6 arms × 3 runs × 5 papers), each with
  `status: "OK"` and `schema_version: "1.1"`. Each `paper_slug` matches its
  filename. `escalate_reason` is absent in 37 payloads and `null` in the other
  53, so no run escalated.
- **Item set.** Every one of the 180 sections (90 files × data and code)
  carries exactly the 15 keys F1, F2, F3, F4, A1, A1_1, A1_2, A2, I1, I2, I3,
  R1, R1_1, R1_2, and R1_3. There are no missing or extra items.
- **Score values.** Every one of the 2,700 payload item scores is integer 0 or
  1 (848 zeros, 1,852 ones), with no nulls and no non-numeric values. Each
  recorded section `total` equals the sum of its items.
- **Reference.** All 5 files have `reference: "E8-v2"`. Each section has 15
  leaves in the groups findable, accessible, interoperable, and reusable,
  which makes **150 items**. Every descriptive key maps to exactly one payload
  code, with the mapping hard-coded and failing loudly on any unknown key.
  Every group subtotal matches its leaves. The reference holds 95 ones and 55
  zeros.
- **BI items.** **9** items are BI-tagged:

  | Item | Tags | Reference score |
  | --- | --- | --- |
  | crema-et-al-2024 / data / I1 | input | 1 |
  | crema-et-al-2024 / data / I3 | input, rule | 0 |
  | dye-et-al-2023 / code / I1 | input, rule | 0 |
  | dye-et-al-2023 / data / F1 | input | 0 |
  | dye-et-al-2023 / data / I1 | input, rule | 0 |
  | dye-et-al-2023 / data / R1_1 | input | 0 |
  | herskind-riede-2024 / data / I1 | input | 1 |
  | marwick-2025 / code / I3 | input, rule | 1 |
  | marwick-2025 / data / I1 | input | 1 |

  The BI-excluded denominator is therefore 141.

**Anomalies**

1. **fable-5 (xhigh), run 1, key-et-al-2024, data section.** The section is
   recorded as `available: false`, yet it carries a full set of 15 item scores
   with R1 = 1 (total 1). The other 89 data sections, and all 90 code
   sections, are `available: true`. Scores were used as recorded. The
   sensitivity analysis is in §4.
2. **Model identifier (provenance only, no effect on any statistic).** Both
   opus arms record `model_id: "claude-opus-5[1m]"`. Amendment 1 pins the
   identifier string `claude-opus-5`. The sonnet and fable arms record
   `claude-sonnet-5` and `claude-fable-5`, as pinned.
3. **Instrument version (observation only).** Every payload records
   `fair-instrument` version 2.1 and `fair-principles-guide` version 1.1.
   Registration §7.1 names "Instrument v2.0". I read no file that documents
   this version step and make no inference from it.

## 3. Results, primary reading (A: four-way unanimity)

| Arm | Stability | ≥ 0.90 | Concordance, all items | Over / under | ≥ 0.90 | Concordance, BI excluded | Over / under | ≥ 0.90 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sonnet-5 (xhigh) | 128/150 (0.853) | no | 112/150 (0.747) | 22 / 16 | no | 111/141 (0.787) | 18 / 12 | no |
| opus-5 (xhigh) | 143/150 (0.953) | yes | 129/150 (0.860) | 17 / 4 | no | 126/141 (0.894) | 12 / 3 | no |
| fable-5 (xhigh) | 142/150 (0.947) | yes | 132/150 (0.880) | 12 / 6 | no | 129/141 (0.915) | 7 / 5 | yes |
| sonnet-5-high | 122/150 (0.813) | no | 108/150 (0.720) | 23 / 19 | no | 107/141 (0.759) | 19 / 15 | no |
| sonnet-5-max | 130/150 (0.867) | no | 119/150 (0.793) | 17 / 14 | no | 118/141 (0.837) | 13 / 10 | no |
| opus-5-high | 143/150 (0.953) | yes | 128/150 (0.853) | 18 / 4 | no | 124/141 (0.879) | 14 / 3 | no |

Joint gate clearance, meaning stability ≥ 0.90 and reading-A concordance
≥ 0.90:

| Arm | Stability gate | Eligible (all items) | Eligible (BI excluded) |
| --- | --- | --- | --- |
| sonnet-5 (xhigh) | no | no | no |
| opus-5 (xhigh) | yes | no | no |
| fable-5 (xhigh) | yes | no | yes |
| sonnet-5-high | no | no | no |
| sonnet-5-max | no | no | no |
| opus-5-high | yes | no | no |

Reading-A misses split into split-run misses (the runs disagree among
themselves, which also makes the item a stability miss) and unanimous-wrong
misses (all three runs agree, and disagree with the reference):

| Arm | Misses, all | Split-run misses | Unanimous-wrong (over / under) | Misses, BI excl. | Split-run misses | Unanimous-wrong (over / under) |
| --- | --- | --- | --- | --- | --- | --- |
| sonnet-5 (xhigh) | 38 | 22 | 16 (12 / 4) | 30 | 19 | 11 (9 / 2) |
| opus-5 (xhigh) | 21 | 7 | 14 (13 / 1) | 15 | 6 | 9 (9 / 0) |
| fable-5 (xhigh) | 18 | 8 | 10 (9 / 1) | 12 | 7 | 5 (5 / 0) |
| sonnet-5-high | 42 | 28 | 14 (9 / 5) | 34 | 25 | 9 (6 / 3) |
| sonnet-5-max | 31 | 20 | 11 (8 / 3) | 23 | 17 | 6 (5 / 1) |
| opus-5-high | 22 | 7 | 15 (14 / 1) | 17 | 7 | 10 (10 / 0) |

In every arm, the number of split-run misses over all items equals
150 minus the stability count, as it must.

## 4. Alternative-reading results

### 4.1 Reading B: per-run agreement with the reference

| Arm | Pooled, all items | Over / under | ≥ 0.90 | Per-run counts (/150) | Min run ≥ 0.90 | Pooled, BI excluded | Over / under | ≥ 0.90 | Per-run counts (/141) | Min run ≥ 0.90 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sonnet-5 (xhigh) | 369/450 (0.820) | 51 / 30 | no | 123, 126, 120 (min 0.800) | no | 362/423 (0.856) | 41 / 20 | no | 120, 124, 118 (min 0.837) | no |
| opus-5 (xhigh) | 399/450 (0.887) | 45 / 6 | no | 134, 135, 130 (min 0.867) | no | 388/423 (0.917) | 32 / 3 | yes | 130, 131, 127 (min 0.901) | yes |
| fable-5 (xhigh) | 409/450 (0.909) | 30 / 11 | yes | 137, 135, 137 (min 0.900) | yes | 398/423 (0.941) | 17 / 8 | yes | 134, 131, 133 (min 0.929) | yes |
| sonnet-5-high | 371/450 (0.824) | 44 / 35 | no | 124, 121, 126 (min 0.807) | no | 364/423 (0.861) | 33 / 26 | no | 122, 118, 124 (min 0.837) | no |
| sonnet-5-max | 386/450 (0.858) | 37 / 27 | no | 131, 123, 132 (min 0.820) | no | 379/423 (0.896) | 27 / 17 | no | 128, 122, 129 (min 0.865) | no |
| opus-5-high | 394/450 (0.876) | 50 / 6 | no | 131, 132, 131 (min 0.873) | no | 382/423 (0.903) | 38 / 3 | yes | 127, 128, 127 (min 0.901) | yes |

Over and under counts here are per run-item, so their denominator is 450 (or
423). Two results sit exactly on or just above the line:

- fable-5's minimum run over all items is 135/150 = 0.900 exactly, which
  clears under the ≥ rule.
- The opus arms' BI-excluded minimum runs are 127/141 = 0.9007.

### 4.2 Reading C: majority vote of three runs against the reference

| Arm | All items | Over / under | ≥ 0.90 | BI excluded | Over / under | ≥ 0.90 |
| --- | --- | --- | --- | --- | --- | --- |
| sonnet-5 (xhigh) | 123/150 (0.820) | 17 / 10 | no | 121/141 (0.858) | 14 / 6 | no |
| opus-5 (xhigh) | 134/150 (0.893) | 15 / 1 | no | 130/141 (0.922) | 11 / 0 | yes |
| fable-5 (xhigh) | 137/150 (0.913) | 9 / 4 | yes | 133/141 (0.943) | 5 / 3 | yes |
| sonnet-5-high | 127/150 (0.847) | 12 / 11 | no | 125/141 (0.887) | 8 / 8 | no |
| sonnet-5-max | 128/150 (0.853) | 12 / 10 | no | 126/141 (0.894) | 9 / 6 | no |
| opus-5-high | 131/150 (0.873) | 18 / 1 | no | 127/141 (0.901) | 14 / 0 | yes |

### 4.3 Reading D: conditional on unanimous runs (supplementary, not recommended)

| Arm | All items | Over / under | ≥ 0.90 | BI excluded | Over / under | ≥ 0.90 |
| --- | --- | --- | --- | --- | --- | --- |
| sonnet-5 (xhigh) | 112/128 (0.875) | 12 / 4 | no | 111/122 (0.910) | 9 / 2 | yes |
| opus-5 (xhigh) | 129/143 (0.902) | 13 / 1 | yes | 126/135 (0.933) | 9 / 0 | yes |
| fable-5 (xhigh) | 132/142 (0.930) | 9 / 1 | yes | 129/134 (0.963) | 5 / 0 | yes |
| sonnet-5-high | 108/122 (0.885) | 9 / 5 | no | 107/116 (0.922) | 6 / 3 | yes |
| sonnet-5-max | 119/130 (0.915) | 8 / 3 | yes | 118/124 (0.952) | 5 / 1 | yes |
| opus-5-high | 128/143 (0.895) | 14 / 1 | no | 124/134 (0.925) | 10 / 0 | yes |

### 4.4 Summary of gate outcomes across readings

Stability is the same under every reading. Opus-5 (xhigh), fable-5 (xhigh),
and opus-5-high clear it; the three sonnet arms do not.

Among the three arms that clear stability, concordance ≥ 0.90 goes as
follows:

| Reading | All items | BI excluded |
| --- | --- | --- |
| A (primary) | none | fable-5 only |
| B, pooled | fable-5 only | fable-5, opus-5, and opus-5-high |
| B, minimum run | fable-5 only | fable-5, opus-5, and opus-5-high |
| C | fable-5 only | fable-5, opus-5, and opus-5-high |
| D | opus-5 and fable-5 | all three |

### 4.5 Sensitivity: the fable-5 `available: false` section

The item fable-5 / key-et-al-2024 / data / R1 has run scores [1, 0, 1] and a
reference score of 1. Suppose the unscoreable-scores-0 rule were applied to
the unavailable section, setting run 1's R1 to 0. Then:

- **Unchanged:** stability (142/150) and readings A and D (the item is a
  split-run miss either way).
- **Reading B:** all items 409 → 408/450 (0.907); BI excluded 398 → 397/423
  (0.939); run 1 137 → 136/150 and 134 → 133/141.
- **Reading C:** all items 137 → 136/150 (0.907); BI excluded 133 → 132/141
  (0.936).

No gate outcome changes under any reading.

## 5. Access log (for blinding audit)

All paths are relative to `/home/shawn/Code/llm-reproducibility` unless
absolute. The list is in the order of access.

1. `git fetch`, then `git rev-list --left-right --count origin/main...HEAD`
   (the result was 0 0). This step read no file content and no history.
2. `ls -la studies/open-science-compliance/prereg/`, a directory listing. It
   showed filenames only, including the blinded `amendment-2-draft.md` and
   `osf-amendment-2.txt`, neither of which was opened.
3. Read in full: `studies/open-science-compliance/prereg/README.md`.
4. Read in full: `studies/open-science-compliance/prereg/amendment-1-draft.md`.
5. Read in full: `studies/open-science-compliance/prereg/osf-amendment-1.txt`.
6. `pdfinfo` and `pdftotext -layout` on
   `studies/open-science-compliance/prereg/phase-2-preregistration-draft.pdf`,
   writing to the scratchpad file
   `/tmp/claude-1000/-home-shawn-Code-llm-reproducibility/c51bef29-c20e-400f-94db-056e31bb50f3/scratchpad/prereg.txt`.
   I then ran a heading grep and viewed lines 330–446, covering §7 to the
   start of §10.
7. `grep -n -i` on
   `studies/open-science-compliance/prereg/osf-registration-summary.txt` for
   reliability, agreement, unanimity, concordance, majority, unscoreable, and
   stability. I saw only the matching lines, each truncated to 400
   characters.
8. `test -f` existence checks on exactly the 90 payload paths and 5 reference
   paths. No directory under `outputs/validation/` was listed.
9. Read in full:
   `studies/open-science-compliance/outputs/validation/benchmark-2026-08-17/arm-sonnet-5/run-1/crema-et-al-2024.json`.
10. Read in full:
    `studies/open-science-compliance/outputs/validation/e8-v2-rederivation/reference/crema-et-al-2024.json`.
11. Parsed by Python (structure surveys, the script, and the ad hoc
    cross-check): all 90 payloads at
    `studies/open-science-compliance/outputs/validation/{benchmark-2026-08-17/arm-{sonnet-5,opus-5,fable-5},effort-study-2026-08-17/arm-{sonnet-5-high,sonnet-5-max,opus-5-high}}/run-{1,2,3}/{crema-et-al-2024,dye-et-al-2023,herskind-riede-2024,key-et-al-2024,marwick-2025}.json`,
    and all 5 files under
    `studies/open-science-compliance/outputs/validation/e8-v2-rederivation/reference/`,
    opened by explicit filename.
12. `test -e` on
    `studies/open-science-compliance/outputs/validation/h13-rederivation-2026-10-04`,
    which was absent before I created it.
13. My own outputs in that directory: `h13-rederive.py` (written, partly
    re-read, and edited), `h13-results.json` (written by the script, then
    read), and `report.md` (this file). The results tables were generated
    from `h13-results.json` into the scratchpad file `tables.md` and
    transcribed from there.

**Not opened, listed, or grepped:**

- anything under `e8-v2-concordance-2026-10-03/`;
- any `run-record.json` or `reconciliation/` directory;
- the effort-study `study-summary-2026-08-17.md` and `design-note.md`, and any
  benchmark `*summary*` file;
- `protocol/validation/analyse-benchmark-disagreements.py`, any other
  analysis script, and `tests/`;
- `wiki/`, `manifest.yaml`, `amendment-2-draft.md`, and `osf-amendment-2.txt`;
- the E8-v2 `worksheet.*` and `adjudication-log.md`;
- git history.

The reference JSON files contain the *paths* of the worksheet and
adjudication log as string fields. I saw those strings but did not open the
files. As a precaution I also left unopened
`studies/open-science-compliance/prereg/erratum-log.md`, which was not on the
permitted list, and the FAIR instrument directory, which was not needed
because item identity follows from §7.1 and the key structure.

**Blinded figures seen:** none. The only score figures I encountered outside
the permitted inputs are pilot-era section totals quoted inside
`amendment-1-draft.md` (for example, crema data and code 12/15). Those are
pilot results, not gate statistics.
