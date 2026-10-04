# Mechanical F2 rule and the hybrid scorer — validation (2026-10-04)

**What this is.** The no-spend validation of the mechanical F2 rule (AP-15)
that amendment 3 running-list item 6(b) declares
(`../../../prereg/erratum-log.md`). It covers the rule's output on the five
pilots, its agreement with the re-derived pilot reference (E8-v2), and both
registered gate statistics recomputed for the **hybrid scorer**: the rule
decides F2, and the model scores the other 14 sub-principles. No language
model was called. The only network traffic was the public metadata fetch
the registrant approved for harvester v1.2 (below).
**Status: results only.** Adopting the rule is the registrant's decision,
through amendment 3.

## Scope of the rule (registrant ruling, 2026-10-04)

"The rule gives the 0s; you confirm the 1s." `scripts/score-f2-rule.py`
v1.0 returns one of three statuses per item:

- **mechanical-0**: decided by the rule. A principal artefact is
  unpublished (AP-13), served only as a journal supplement (Row 6), or
  served from unmanaged hosting with no record (AP-3). Or a principal
  deposit's scored-version DataCite record lacks creators, a title, a
  non-empty description, or a subject keyword (AP-15). The test is
  conjunctive across principal artefacts.
- **confirm-1**: every principal deposit has all four fields. Whether the
  description is *substantive* (AP-15's one remaining judgement) goes to the
  registrant. The rule never awards a 1 by itself.
- **no-structured-input**: an input is missing. The model's score stands
  and is flagged (disagreement policy, item 2, fallback).

## Inputs

| Input | Location | Note |
|---|---|---|
| Registry | `corpus/evidence-packs/declared-links.yaml` | curation fields added 2026-10-04 (`role`, `home`, `carries`, `scored_version`, `unpublished_principal`), each anchored to an adjudication sitting in `curation_basis` |
| Packs | `corpus/evidence-packs/harvest-2026-10-04/` | harvester v1.2; sha256 of each pack in `f2-rule-results.json` |
| Raw responses | `$CORPUS_ROOT/registry-responses/<sha256>.json` | out of tree, content-addressed; every pack field can be re-derived from the bytes its `response_sha256` names |
| Reference | `../e8-v2-rederivation/reference/` | `manifest.yaml` `reference_datasets.pilot_fair_assessments_v2` |

**Network use.** The harvest ran twice, about 19 requests each, to public
DataCite, Zenodo, Crossref, and GitHub endpoints, with 1 s spacing. The
second run added the Crossref `created` date after the first showed that
Elsevier's records carry no `published-online` date (AP-12's stated
fallback). The packs in the directory are from the second run.

**Why curation stays out of the packs.** The `role`, `home`, and `carries`
fields record adjudication outcomes, such as dye's CRAN entry being a
dependency. Copying them into the packs would give the scoring model
judgements taken from its own reference. The harvester therefore never
copies them (tested), and the rule reads them from the registry.

## Rule output on the pilots

| Paper | Data F2 | Code F2 | Reason (from `f2-rule-results.json`) |
|---|---|---|---|
| crema-et-al-2024 | 0 | 0 | v1.0.0 record (10.5281/zenodo.10782943): no subject keyword |
| dye-et-al-2023 | 0 | 0 | supplement only (Row 6); data also on unmanaged hosting (AP-3) |
| herskind-riede-2024 | 0 | 0 | v2 record (10.5281/zenodo.10801706): no description, no subject keyword |
| key-et-al-2024 | 0 | 0 | data: unpublished principal data (AP-13); code: supplement only (Row 6) |
| marwick-2025 | 0 | 0 | v1.3 record (10.5281/zenodo.15603267): no subject keyword |

Every status is mechanical-0, and every reason matches the adjudication
log's note for that item. The rule reads the scored version's record, as
AP-12 requires, and not the concept DOI's record. Crema's concept DOI now
resolves to v2.0.0, which has a longer description than v1.0.0 (and also
no keywords).

## Criterion 1: the rule against the reference

The amendment 3 criterion is that the rule matches the E8-v2 reference on
the pilot F2 items at least as well as the selected model does.

- **Rule:** 10/10.
- **Model (majority vote):** 4/10 for `claude-opus-5-5` at every effort, and
  4–6/10 across all nine arms. Every Opus arm scores F2 = 1 wherever a
  Zenodo deposit exists (crema, herskind, and marwick, data and code), and
  every run agrees.

**Why the model over-credits: missing input, not judgement.** The
2026-08-17 packs that every arm read carry no creators, descriptions, or
keywords (harvester v1.1 kept only identifier, licence, and type fields).
The model's F2 evidence cites `metadata_record: true` and the Row 2
entitlement. It could not see that the keyword fields were empty, and it
often said so: 20 of the 90 F2 evidence strings from the five Opus arms
for crema, herskind, and marwick state that the pack did not show the
description or keyword fields (for example, opus-5-5-medium, marwick r1
data: "Description/keywords not shown in pack; scored on existence of a
structured DataCite record"). The
v1.2 packs carry these fields, so the pre-census re-validation will show
whether the model scores F2 correctly once it can see them.

**Limitation: the pilots test only the rule's 0 paths.** All ten reference
F2 items are 0, so a rule that always returned 0 would also score 10/10.
The pilots exercise five of the rule's paths (supplement, unmanaged
hosting, unpublished data, no description, no keyword). They never reach
the missing-creators or missing-title paths, confirm-1, or
no-structured-input. Those paths are covered by unit tests only
(`tests/test_f2_rule.py`, 16 tests). This is why the rule's scope stops at
0s: a positive F2 is never awarded mechanically.

## Criterion 2: both gates for the hybrid scorer

Gate statistics come from the registered analysis tool
(`analyse-benchmark-disagreements.py` v1.2), unchanged, run over the hybrid
copies of all nine arms. Concordance is majority vote (Ruling 1), and the
beyond-instrument (BI) excluded figure is the gate (Ruling 2). Both gates
require at least 0.90.

| Arm | Stability | Concordance, BI excluded (gate) | Errors over/under | Concordance, all 150 |
|---|---|---|---|---|
| sonnet-5 | 128/150 = 0.853 → 131/150 = 0.873 | 121/141 = 0.858 → 126/141 = 0.894 | 14/6 → 9/6 | 123/150 = 0.820 → 128/150 = 0.853 |
| opus-5 | 143/150 = 0.953 → 143/150 = 0.953 | 130/141 = 0.922 → 136/141 = 0.965 | 11/0 → 5/0 | 134/150 = 0.893 → 140/150 = 0.933 |
| fable-5 | 142/150 = 0.947 → 144/150 = 0.960 | 133/141 = 0.943 → 137/141 = 0.972 | 5/3 → 1/3 | 137/150 = 0.913 → 141/150 = 0.940 |
| sonnet-5-high | 122/150 = 0.813 → 123/150 = 0.820 | 125/141 = 0.887 → 131/141 = 0.929 | 8/8 → 2/8 | 127/150 = 0.847 → 133/150 = 0.887 |
| sonnet-5-max | 130/150 = 0.867 → 133/150 = 0.887 | 126/141 = 0.894 → 132/141 = 0.936 | 9/6 → 3/6 | 128/150 = 0.853 → 134/150 = 0.893 |
| opus-5-high | 143/150 = 0.953 → 143/150 = 0.953 | 127/141 = 0.901 → 133/141 = 0.943 | 14/0 → 8/0 | 131/150 = 0.873 → 137/150 = 0.913 |
| opus-5-5-high | 143/150 = 0.953 → 143/150 = 0.953 | 130/141 = 0.922 → 136/141 = 0.965 | 8/3 → 2/3 | 134/150 = 0.893 → 140/150 = 0.933 |
| **opus-5-5-medium (selected)** | **143/150 = 0.953 → 143/150 = 0.953** | **131/141 = 0.929 → 137/141 = 0.972** | **7/3 → 1/3** | **133/150 = 0.887 → 139/150 = 0.927** |
| opus-5-5-xhigh | 145/150 = 0.967 → 145/150 = 0.967 | 130/141 = 0.922 → 136/141 = 0.965 | 9/2 → 3/2 | 135/150 = 0.900 → 141/150 = 0.940 |

The "before" figures are `../opus-5-5-arms-2026-10/concordance/*/summary.json`;
the "after" figures are `bi-excluded/summary.json` and `all-items/summary.json`
here.

**Two derivations, zero disagreements.** `h13/h13-rederive.py` is a copy of
`../opus-5-5-arms-2026-10/h13/h13-rederive.py` whose only change is the
`ARMS` dictionary, pointed at the hybrid copies. It agrees with the
analysis tool on stability, on reading C over 150 and 141 items, and on the
over/under split, for all nine arms. For the selected configuration, the
other readings with BI items excluded are: A (four-way unanimity) 134/141 =
0.950, B (per-run pooled) 410/423 = 0.969, and D (conditional on unanimous
runs) 134/136 = 0.985.

**Readings (not rulings):**

1. **The hybrid at `medium` clears both gates under both concordance
   readings.** Gate concordance is 0.972; even over all 150 items it is
   0.927. Under the hybrid, the selected configuration no longer depends on
   the BI-exclusion deviation (Entry 5(b)) to clear the gate. The deviation
   still stands as ruled; this only reduces how much rests on it.
2. **Stability is unchanged for every Opus arm**, because the model's F2
   scores were already identical across runs. Stability rises for the
   Sonnet and Fable arms, where F2 had split runs.
3. **The F2 errors were all over-credits**, so the hybrid removes six
   over-credits per Opus arm and adds no errors.
4. **Remaining `medium` misses inside the gate (4):** crema code I3
   (under), dye code R1.1 (under), key data R1 (under), and marwick code R1.3
   (over). Outside the gate, 7 BI items. Three of these are data I1 items
   tagged [input] (crema, herskind, and marwick), whose deposits' file
   formats the v1.2 packs now list.

## Derived fields

`build-hybrid-arms.py` recomputes each section `total` as its item sum
(disagreement policy, item 1). One model miscount across all nine arms is
corrected: `opus-5-5-medium` run 3, dye `code_fair`, total 7 against an
item sum of 8, the case that prompted Layer 1. It does not affect the
statistics, which are item-level.

## Reproducing this

```bash
venv/bin/python scripts/harvest-artefact-metadata.py --out corpus/evidence-packs/harvest-2026-10-04
venv/bin/python scripts/score-f2-rule.py --packs corpus/evidence-packs/harvest-2026-10-04 \
  --out studies/open-science-compliance/outputs/validation/f2-rule-hybrid-2026-10-04/f2-rule-results.json
V=studies/open-science-compliance/outputs/validation
venv/bin/python $V/f2-rule-hybrid-2026-10-04/build-hybrid-arms.py
A=$V/f2-rule-hybrid-2026-10-04/arms
venv/bin/python studies/open-science-compliance/protocol/validation/analyse-benchmark-disagreements.py \
  --arms $A/arm-{sonnet-5,opus-5,fable-5,sonnet-5-high,sonnet-5-max,opus-5-high,opus-5-5-high,opus-5-5-medium,opus-5-5-xhigh} \
  --reference-key pilot_fair_assessments_v2 [--exclude-bi] \
  --out-dir $V/f2-rule-hybrid-2026-10-04/{all-items|bi-excluded}
venv/bin/python $V/f2-rule-hybrid-2026-10-04/h13/h13-rederive.py
```

A re-harvest would fetch live records, which can drift. To reproduce these
figures, use the committed packs and start from `score-f2-rule.py`. The
hybrid copies in `arms/` are git-ignored. Rebuilding them is
byte-identical (checked by rebuilding and comparing `hybrid-build.json`,
which records the sha256 of every source and hybrid payload).
