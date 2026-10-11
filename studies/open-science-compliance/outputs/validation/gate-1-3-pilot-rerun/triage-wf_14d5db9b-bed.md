# Plan triage — gate-1-3-pilot-rerun-2026-10

Workflow run `wf_14d5db9b-bed`; generated 2026-10-11T10:59:06+00:00 by `scripts/reproduction-lane.py persist-plans`. Approve, hold, or reject each plan with `reproduction-lane.py approve`. On approval the target list becomes the locked coverage denominator.

| Paper | Status | Type | Targets | Excluded | Detected | Compute (h) | Flags | Plan sha256 |
|---|---|---|---|---|---|---|---|---|
| herskind-riede-2024 | OK | B | 20 | 7 | 9 | 2 | 2 | 89f2c93784d4 |

## herskind-riede-2024

- ⚠ enumeration_check.items_excluded (1) != exclusions listed (7)
- ⚠ planner flagged the enumeration for human attention
- ❓ Relayed user question: 'I assume you're using my max account?' The planner cannot see billing or account context, so the orchestrator or the session should answer this directly. The planner made no API calls beyond public Zenodo downloads.
- ❓ S3 granularity: S3.xlsx is enumerated as ONE target (T08, three sheets, 2329 values), by analogy with R3's one target per multi-panel item. Should it instead be three targets (bigrams, trigrams, quadrigrams)? This changes the denominator from 20 to 22.
- ❓ The statement that the corpus is 'nearly half' of Płonka's European total (p.2) is excluded as a non-numeric background claim. If you rule it a named value, it enters as expected-untestable (R2). Under the L2 counting unit the Płonka catalogue would then become a required dataset: one of two datasets retrievable is not more than 50%, which would move the paper's data-availability level off L1/L2. Please confirm the exclusion.
- ❓ Are the R1 aids for the Fig. 2 map panel and Fig. 5 (plotting deposited coordinates and motif lookups with ggplot2) acceptable as full-scope checks? If not, T04 and T07 will be recorded as partially verified and count against coverage.
- ❓ T17: the paper says 'nine' Ertebølle-specific bigrams but lists eight. Please confirm R4 scoring against the stated nine, with the unlisted ninth (C5-C12 on the planner's reading of Fig. 3b) recorded as a text inconsistency.
- ❓ The paper's methods give PMI as log2, while the code and all published values use the natural log. The plan records this as a documentation finding, not a target or a paper error. Is that the intended treatment?
