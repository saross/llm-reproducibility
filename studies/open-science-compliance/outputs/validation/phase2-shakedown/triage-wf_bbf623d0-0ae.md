# Plan triage — phase2-shakedown-2026-10

Workflow run `wf_bbf623d0-0ae`; generated 2026-10-03T08:53:08+00:00 by `scripts/reproduction-lane.py persist-plans`. Approve, hold, or reject each plan with `reproduction-lane.py approve`. On approval the target list becomes the locked coverage denominator.

| Paper | Status | Type | Targets | Excluded | Detected | Compute (h) | Flags | Plan sha256 |
|---|---|---|---|---|---|---|---|---|
| dye-et-al-2023 | OK | C,D | 34 | 5 | 19 | 4 | 2 | 7ff05a24d134 |
| herskind-riede-2024 | OK | B,C | 15 | 9 | 11 | 1 | 1 | 5cdc80717f2f |

## dye-et-al-2023

- ⚠ enumeration_check.items_excluded (2) != exclusions listed (5)
- ⚠ planner flagged the enumeration for human attention
- ❓ Approve excluding paper Figures 1 and 5 as conceptual, non-computational illustrations? If they should be targets, they must be added before approval; they would likely be scored CANNOT_COMPARE or visual-only.
- ❓ Supplement section 10.5 states 'nine' relations but 'six' in the same subsection, and Table 6 has 6 cells. I excluded structural relation counts from the named-value targets. Do you want this count added as a target, so that it enters the R4 PAPER_ERROR protocol?
- ❓ The corpus 'vor.pdf' is the White Rose accepted manuscript, not the Elsevier typeset version of record, and ScienceDirect returned 403. Should the version of record be obtained to confirm that the figure numbering and values are identical before locking? The supplement refers to the occurrence and tempo plots as 'Figure 7' and 'Figure 8'; I mapped them to the manuscript's Figures 3 and 4.
- ❓ Supplement Table 1 (T11) and its summary (T10) need four MCMC runs that are not published (404 at the author's server). Should the executor send the standardised L4 data request to the corresponding author (T.S. Dye), or simply record them as unavailable?
- ❓ T09 folds the main-paper Discussion statement and the Supplement section 12 restatement into one target, and T10 folds in the main paper's 'negligible between-run variability' claim. Confirm this granularity, or split them into separate targets.

## herskind-riede-2024

- ⚠ planner flagged the enumeration for human attention
- ❓ Confirm excluding the 'nearly half of the total number of European Mesolithic ornamented artefacts listed by Płonka (2003)' claim (p. 2). Should it instead be locked as an expected-untestable named value under R2?
- ❓ T08: the text says 'nine' Ertebølle-exclusive bigrams but lists only eight. Confirm scoring against the stated 0/1/9 counts per R4, with PAPER_ERROR escalation if the reproduction differs.
- ❓ Confirm treating the log2-versus-ln PMI formula inconsistency (p. 3 formula versus S2.R and the published values) as a documented finding rather than a scored target.
- ❓ Confirm R 4.3.2 (README) over R 4.2.2 (paper text) as the target language version.
- ❓ Confirm S3.xlsx as a supplementary display-item target (T15, 1601 numeric values). Its size dominates value counts, but coverage is counted per target.
- ❓ Confirm that a ggplot2 point plot of the S1 coordinates (Fig. 2 map panel, Fig. 5) and applying the authors' createResultTable function to all observed > 2 bigrams (Fig. 4 boxes) are acceptable R1 verification aids.
- ❓ Confirm the granularity of grouped named values: T05 (44, 44, ~9%) and T13 (ten objects; nine axes + one shaft) are each one target.
