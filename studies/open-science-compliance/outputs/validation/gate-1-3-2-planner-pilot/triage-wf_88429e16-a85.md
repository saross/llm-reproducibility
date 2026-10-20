# Plan triage — gate-1-3-2-planner-pilot-2026-10

Workflow run `wf_88429e16-a85`; generated 2026-10-20T23:15:48+00:00 by `scripts/reproduction-lane.py persist-plans`. Approve, hold, or reject each plan with `reproduction-lane.py approve`. On approval the target list becomes the locked coverage denominator.

| Paper | Status | Type | Targets | Excluded | Detected | Compute (h) | Flags | Plan sha256 |
|---|---|---|---|---|---|---|---|---|
| herskind-riede-2024 | OK | C | 17 | 8 | 11 | 1.5 | 1 | aab8410e4b1b |

## herskind-riede-2024

- ⚠ planner flagged the enumeration for human attention
- ❓ BLINDING: at planning, `ls /home/shawn/Code/llm-reproducibility/reproduction-system/ | grep -v -E 'workflows'` printed the blinded filename lodged-rules.yaml. The file was not opened, read, or searched, and its content was not seen; the rules were quoted only from the spawn prompt. Please rule on whether this run remains admissible.
- ❓ R version: the README (deposit v2) states R 4.3.2 with seven package pins, but the paper's methods state R v.4.2.2. The plan honours the README as the authors' environment specification (rocker/r-ver:4.3.2). Approve, or direct R 4.2.2?
- ❓ S3 granularity: Supplementary Information S3 is enumerated as one target (T08) with three sheets, by analogy with R3's multi-panel rule. Should each sheet be a separate target instead (+2 targets)?
- ❓ Log base and t: the paper's PMI formula uses log2 and defines t as the total number of objects (483), but S2.R uses natural log() and t = 482. Under R4 the plan scores the printed values and reports the inconsistency. Should the formula-text mismatch also be escalated as a PAPER_ERROR finding if the printed values prove to be natural-log based?
- ❓ T13: the text says 'nine are unique for the Ertebølle period' but lists eight pairs; Fig. 3b shows C5-C12 as the ninth. The plan scores the stated counts (0, 1, 9) and the listed identities, and escalates the omission. Approve?
- ❓ T14: the plan pre-states that 'highest frequency of cooccurrence being five' refers to the culture-exclusive Fig. 3b bigrams. Over all 21 bars the published maximum is 6 (E1-F12). Approve this reading?
- ❓ T06 convention: pairs involving 'Kongemose/Ertebølle' objects are expected unboxed in Fig. 4, and deviations are MINOR (R1). Approve?
- ❓ Q5 reading for the inferred aid rules (T06, T11, T13, T14, T15): the plan treats `data` and the other run objects created by executing the authors' S2.R as 'inputs from executing the authors' code', and records each rule's printed-input qualification check. Approve this reading of the inputs-from-authors-code condition?
- ❓ Exclusions: Fig. 1 (photographs), S1 (input data), S2 (code), k = 13 (parameter), the 'nearly half of Płonka's European total' claim (literature background; if ruled a named value it enters as expected-untestable under R2), date ranges, non-data graphic elements, and interpretive statements. Approve?
- ❓ Reproduction type: classified C (an interactive-style script with a known error at line 27 and manual post-processing), although the computational core runs in batch through a wrapper. Approve, or reclassify as B?
