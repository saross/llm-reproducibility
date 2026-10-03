# Plan triage — phase2-shakedown-2026-10

Workflow run `wf_5d10728a-820`; generated 2026-10-03T08:13:08+00:00 by `scripts/reproduction-lane.py persist-plans`. Approve, hold, or reject each plan with `reproduction-lane.py approve`. On approval the target list becomes the locked coverage denominator.

| Paper | Status | Type | Targets | Excluded | Detected | Compute (h) | Flags | Plan sha256 |
|---|---|---|---|---|---|---|---|---|
| dye-et-al-2023 | OK | C,D | 23 | 7 | 19 | 4 | 2 | 4b2f8b231ab5 |
| herskind-riede-2024 | OK | B | 14 | 11 | 13 | 0.5 | 0 | bb57ae0ab457 |

## dye-et-al-2023

- ⚠ enumeration_check.items_excluded (4) != exclusions listed (7)
- ⚠ planner flagged the enumeration for human attention
- ❓ Exclusions of Figures 1, 2, 5, and 6: do you accept these as non-computational? Figure 2 holds analytic Allen-composition results that ArchaeoPhases could in principle recompute, but the authors supplied no code for it. Figure 6 is a hand-composed summary whose link structure is scored through T03-T05. If either should be a target, add it before approval, because the list locks at approval.
- ❓ Reconstruction policy for no-code targets T19-T23: may the executor write minimal calls to documented ArchaeoPhases 1.8 functions (e.g. allen_observe_frequency, Allen lattice plotting) to test these? Or should they be recorded CANNOT_COMPARE (no code supplied)? The plan currently leaves this conditional, and it should be fixed at approval.
- ❓ T08 and T09 (Supplement Table 1 and the between-run summary) depend on unpublished OxCal runs. Do you confirm they stay in this attempt's locked denominator (expected untestable, counting against coverage) rather than being moved exclusively to attempt-03's denominator? The coverage rules read as keeping them.
- ❓ Blinding disclosure: printing the corpus metadata file (/home/shawn/corpora/llm-reproducibility/dye-et-al-2023/meta.json) showed a provenance field that names a path containing 'reproduction/attempt-01'. The planner did not read, list, or access that path or anything under it, but the string was printed in the planner's tool output. Please decide whether this counts as a blinding breach for this run.
- ❓ Instrument delivery: the SubagentStart hook persisted the injected instrument text to a file under a '.claude/projects/' path, which is blinded, so the planner did not read it. Instead it read the canonical instrument files from the repository at launch commit 344049db and verified each against manifest.yaml: version 1.0, receipt token, and C7 sha256 all match for coverage-rules, eligibility-criteria, data-availability-taxonomy, pipeline-invariants, and verdicts-and-precision. The planner used the manifest's shared_content keys as instrument names, because only 'data-availability-taxonomy' was visible as a name attribute in the hook preview. Please confirm this is acceptable, or treat it as a pipeline defect to fix (the hook's persistence path collides with the blinding list).

## herskind-riede-2024

- ❓ Verification aids: T03 (Table 3), T07 (Fig. 5 pie content), T12 (maximum 15 motifs), and the T04 map panel have no author code. The plan checks them with read-only lookups or point plots against S1 in a separate comparison script that never touches S2.R. Do you approve this, or should these be scored CANNOT_COMPARE (still counted in the denominator)?
- ❓ Granularity: Fig. 3 is enumerated as one target (T05, 128 PMI labels plus visual stacking), following the 'one target per figure' rule. Do you want it split into six panel targets (a to f) before the denominator is locked?
- ❓ T14 records a possible internal inconsistency in the paper: the text says 'nine' Ertebølle-exclusive salient bigrams but lists eight. Please confirm that the target should be scored against the stated 'nine', with PAPER_ERROR escalation if the reproduction gives eight.
- ❓ Instrument receipts: the spawn hook's injected instrument text was saved by the harness under ~/.claude/projects/…/tool-results/, which is a blinded path, so it was NOT read. The four pushed instruments were instead read from their canonical repository paths (coverage-rules.md, eligibility-criteria.md, data-availability-taxonomy.md, .claude/shared/invariants.md). All are version 1.0 and the receipts are quoted from those files. instrument_versions and instrument_receipts are keyed by file stem ('coverage-rules', 'eligibility-criteria', 'data-availability-taxonomy', 'invariants'). Only 'data-availability-taxonomy' was visible as a name attribute in the injection preview. Please confirm the keys and that reading the canonical files is acceptable. Also, one of the planner's own Bash outputs (README plus S2.R printed together) was saved by the harness to the same blinded tool-results directory; that file was not read, and the script was re-printed in smaller chunks instead. You may wish to check the blinding audit for harness-generated persistence paths.
- ❓ Both pulled references named in the agent brief (verification-strategies.md and pilot-reproduction-summary.md) are on the blinded list and were skipped, not declared. Only verdicts-and-precision.md (receipt fe9bca3d3c95f931) was pulled.
