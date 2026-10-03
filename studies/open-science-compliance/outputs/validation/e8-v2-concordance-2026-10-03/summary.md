# Six-arm concordance against E8-v2 — 2026-10-03

**What this is.** The one-pass computation queued since 2026-08-19. All six
FAIR-lane arms are scored for concordance against the re-derived pilot
reference (`manifest.yaml` `reference_datasets.pilot_fair_assessments_v2`,
assembled from the adjudicated worksheet). It is reported over all 150
items and with the 9 beyond-instrument (BI) items excluded (141). No API
calls were made; it was computed from committed artefacts by
`analyse-benchmark-disagreements.py` v1.2.
**Status:** results only. The gates ruling is the registrant's (continuity
item 3), and it is preceded by H13, the fresh-context re-derivation.

## Invocation (from the repository root)

```bash
V=studies/open-science-compliance/outputs/validation
venv/bin/python studies/open-science-compliance/protocol/validation/analyse-benchmark-disagreements.py \
  --arms $V/benchmark-2026-08-17/arm-{sonnet-5,opus-5,fable-5} \
         $V/effort-study-2026-08-17/arm-{sonnet-5-high,sonnet-5-max,opus-5-high} \
  --reference-key pilot_fair_assessments_v2 [--exclude-bi] \
  --out-dir $V/e8-v2-concordance-2026-10-03/{all-items|bi-excluded}
```

Machine-readable figures are in `all-items/summary.json` and
`bi-excluded/summary.json`. The disputed items are in each directory's
`disputed-items.json`: 49 of 150 in both runs. The disputed list is an
evidence record, so BI items stay in it; `--exclude-bi` removes them only
from the concordance statistic.

## Results (both registered gates require at least 0.90)

| Arm (effort) | Stability | Concordance, all 150 | Errors (over / under) | Concordance, BI excluded (141) | Errors (over / under) |
|---|---|---|---|---|---|
| sonnet-5 (xhigh) | 128/150 = 0.853 | 123/150 = 0.820 | 17 / 10 | 121/141 = 0.858 | 14 / 6 |
| opus-5 (xhigh) | 143/150 = 0.953 | 134/150 = 0.893 | 15 / 1 | 130/141 = 0.922 | 11 / 0 |
| fable-5 (xhigh) | 142/150 = 0.947 | 137/150 = 0.913 | 9 / 4 | 133/141 = 0.943 | 5 / 3 |
| sonnet-5 (high) | 122/150 = 0.813 | 127/150 = 0.847 | 12 / 11 | 125/141 = 0.887 | 8 / 8 |
| sonnet-5 (max) | 130/150 = 0.867 | 128/150 = 0.853 | 12 / 10 | 126/141 = 0.894 | 9 / 6 |
| opus-5 (high) | 143/150 = 0.953 | 131/150 = 0.873 | 18 / 1 | 127/141 = 0.901 | 14 / 0 |

Stability is unchanged by the reference, and the three effort-study arms
reproduce their run-record figures exactly (tool verification line "OK").

## Readings for the gates ruling (not rulings)

1. **Over all 150 items, only fable-5 clears both gates.** opus-5 is 0.893
   at xhigh and 0.873 at high. Amendment 1 §3 states that, on the prices
   in force at amendment time, the most capable and most expensive arm
   "cannot be selected for the census under any outcome". If that holds,
   the all-items reading leaves no selectable arm, and the registered
   remediation ladder applies.
2. **With the BI items excluded, opus-5 clears both gates at both efforts**
   (0.922 xhigh, 0.901 high), as does fable-5. Under price-ordered
   selection, opus-5 would then be the cheapest eligible arm. Whether the
   BI-excluded figure is admissible as the gate statistic is the central
   question for the ruling. BI items are those whose adjudication needed
   input or a rule outside the frozen instrument, so an arm working from
   the instrument alone could not have reached them.
3. **Error direction separates the models.** opus-5's misses are almost all
   over-credit: 15 of 16 at xhigh and 18 of 19 at high, and every miss once
   BI items are excluded. fable-5 is mixed (9 / 4). The sonnet arms are
   roughly balanced. A one-directional error pattern may be addressable by
   instrument clarification, whereas noise is not. This is worth naming in
   the ruling.
4. **Prices have moved since amendment 1.** Opus 5.5 is now listed at $4 /
   $20 per million tokens, against Opus 5 at $5 / $25, according to the
   claude-api skill price table (2026-09-25). Amendment 1 applies "the
   prices in force at selection". Register F-013 also shows that the
   recorded token metric over-counts in a model-dependent way, so any
   cost comparison should use per-request counts.

## Provenance

- Reference: `e8-v2-rederivation/reference/<slug>.json`, built by
  `scripts/assemble-e8v2-reference.py` v1.0 from `worksheet.json`
  (sha256 recorded in the manifest entry and in every reference file).
  `--check` reports it in sync.
- Tool: `analyse-benchmark-disagreements.py` v1.2. It adds `--exclude-bi`
  and `summary.json`; `disputed-items.json` keeps its v1.1 shape for
  untagged references.
