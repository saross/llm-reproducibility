# Plan triage — gate-1-3-1-pilot-rerun-2026-10

Workflow run `wf_db7d121a-5d5`; generated 2026-10-13T05:06:13+00:00 by `scripts/reproduction-lane.py persist-plans`. Approve, hold, or reject each plan with `reproduction-lane.py approve`. On approval the target list becomes the locked coverage denominator.

| Paper | Status | Type | Targets | Excluded | Detected | Compute (h) | Flags | Plan sha256 |
|---|---|---|---|---|---|---|---|---|
| herskind-riede-2024 | OK | B | 18 | 4 | 9 | 1 | 2 | 6837cf60785a |

## herskind-riede-2024

- ⚠ enumeration_check.items_excluded (1) != exclusions listed (4)
- ⚠ planner flagged the enumeration for human attention
- ❓ Version identity: the Zenodo concept DOI 10.5281/zenodo.10623549 holds four records (10623550, 10623970, 10731941, 10801706), so 10801706 is not 'version 2' by Zenodo's history. The plan reproduces 10801706 as AP-12 directs. Please confirm, and note that the publisher-supplement byte-identity was not re-checked here.
- ❓ Runtime: the README pins R 4.3.2, but the paper states R 4.2.2. The plan uses 4.3.2 (the deposit's supplied pin). Confirm or rule otherwise.
- ❓ The paper's PMI formula says log2, but the code (and S3's values) use the natural log, and the code uses t = 482, not the stated 483. The plan scores against printed values and records this as a methods-description note, not a target. Is a PAPER_ERROR-style escalation wanted for the formula text?
- ❓ T14: the text says nine Ertebølle-unique bigrams but lists eight. The plan scores against the stated nine per R4. Confirm.
- ❓ T15: the plan reads 'highest frequency of cooccurrence being five' as scoped to the culture-specific Fig. 3b bigrams. Confirm, or rule that it covers all 21 Fig. 3b bars.
- ❓ Exclusion of the upstream claim that the 483 objects are 'nearly half' of Płonka's European total: confirm it is background, not a named value. If it is ruled a target, it enters as expected-untestable under R2, and Płonka (2003) becomes a required dataset for the L2 counting unit.
