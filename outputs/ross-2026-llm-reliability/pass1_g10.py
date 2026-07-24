#!/usr/bin/env python3
"""Pass 1, Group G10: Results 4.5 The 2026 literature search re-application (pp. 17-19, ~990 words)."""

from pass1_lib import save_group

EVIDENCE = [
    {
        "evidence_id": "E159",
        "evidence_text": "The 2026 episode was not a designed replication: lit-scout was built as a learning exercise, repurposed to search information-science literature for this paper, and the failure surfaced during authentic use.",
        "evidence_type": "observation",
        "verbatim_quote": "The second research episode was not a designed replication of 2025's failure modes or mitigations. As Section 3.2 records, one of us built the lit-scout agent as part of an exercise to learn 2026 LLM techniques, then re-purposed it to search the information-science literature for publications relevant to this paper. The failure described below then surfaced during authentic use.",
        "location": {"section": "4.5 The 2026 literature search re-application", "page": 17},
        "supports_claims": ["C073"],
        "notes": ""
    },
    {
        "evidence_id": "E160",
        "evidence_text": "A tool first applied to a paper on LLM confabulation itself confabulated, a year and a model generation after the 2025 case.",
        "evidence_type": "observation",
        "verbatim_quote": "A tool first applied to a paper on LLM confabulation itself confabulated, a year and a model generation after the 2025 case.",
        "location": {"section": "4.5 The 2026 literature search re-application", "page": 17},
        "supports_claims": ["C114", "C019"],
        "notes": ""
    },
    {
        "evidence_id": "E161",
        "evidence_text": "The agent's first run returned a 37-row findings table with the trappings of rigour: chain-provenance annotations, convergence scores, thematic clusters, venue analysis, and a tiered reading list.",
        "evidence_type": "observation",
        "verbatim_quote": "The agent's first run returned a 37-row findings table with the trappings of rigour: chainprovenance annotations, convergence scores, thematic clusters, venue analysis, and a tiered reading list.",
        "location": {"section": "4.5.1 The failure: partial-grounding collapse", "page": 17},
        "supports_claims": ["C114"],
        "notes": "'chainprovenance' preserves a line-break artefact of the processed md."
    },
    {
        "evidence_id": "E162",
        "evidence_text": "The agent's mechanical grounding worked as designed: DOIs and paper titles were retrieved verbatim from bibliographic-service API calls and were correct.",
        "evidence_type": "observation",
        "verbatim_quote": "Its mechanical grounding worked as designed: DOIs and paper titles were retrieved verbatim from API calls to bibliographic services (and were correct).",
        "location": {"section": "4.5.1 The failure: partial-grounding collapse", "page": 17},
        "supports_claims": ["C114"],
        "notes": ""
    },
    {
        "evidence_id": "E163",
        "evidence_text": "Confabulation began where the agent composed the narrative 'Authors (Year)' and citation-count columns, synthesising values from training-data memory rather than from the API response already in hand.",
        "evidence_type": "observation",
        "verbatim_quote": "Confabulation began when the agent composed the narrative \"Authors (Year)\" and citation-count columns, where it synthesised those values from training-data memory rather than from the API response that was already in hand.",
        "location": {"section": "4.5.1 The failure: partial-grounding collapse", "page": 17},
        "supports_claims": ["C114", "C014"],
        "notes": ""
    },
    {
        "evidence_id": "E164",
        "evidence_text": "The specification's grounding constraint held for directly fetched fields but failed at the synthesis boundary; the agent's own self-check ran and passed the confabulated table.",
        "evidence_type": "observation",
        "verbatim_quote": "The grounding constraint in the agent's specification, that key fields had to come from a retrieved record, held for the fields fetched directly but failed at the synthesis boundary; the agent's own self-check ran and passed the confabulated table.",
        "location": {"section": "4.5.1 The failure: partial-grounding collapse", "page": 17},
        "supports_claims": ["C114", "C042", "C075"],
        "notes": "Self-check failure consistent with the self-verification literature (E016)."
    },
    {
        "evidence_id": "E165",
        "evidence_text": "A spot-check of four sampled rows found author attributions wrong on three, while DOIs and titles were correct throughout.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "A spot-check of four rows sampled from the table found the author attributions wrong on three of them, while DOIs and titles were correct throughout.",
        "location": {"section": "4.5.1 The failure: partial-grounding collapse", "page": 17},
        "supports_claims": ["C114", "C075"],
        "notes": ""
    },
    {
        "evidence_id": "E166",
        "evidence_text": "The spot-check errors would have required manual re-verification of every row, recreating the wholesale manual verification of the 2025 literature search.",
        "evidence_type": "observation",
        "verbatim_quote": "The errors uncovered by this small spot-check would have required manual re-verification of every row and thereby recreated the wholesale manual verification undertaken during the 2025 literature search.",
        "location": {"section": "4.5.1 The failure: partial-grounding collapse", "page": 17},
        "supports_claims": ["C114", "C019"],
        "notes": ""
    },
    {
        "evidence_id": "E167",
        "evidence_text": "Partial grounding made residual confabulations harder to catch: structurally correct fields (DOIs, titles, provenance tags, cluster labels) lent plausibility to fabricated ones beside them; a reader trusting the correct fields would import the confabulated ones alongside.",
        "evidence_type": "observation",
        "verbatim_quote": "The agent's grounding infrastructure partially worked, and that made the residual confabulations harder to catch: the structurally correct fields (DOIs, titles, provenance tags, and cluster labels) lent plausibility to the fabricated ones beside them. A reader who trusted the citations because correct fields signalled credibility would have imported the confabulated fields alongside the accurate ones.",
        "location": {"section": "4.5.1 The failure: partial-grounding collapse", "page": 18},
        "supports_claims": ["C114", "C109", "C006"],
        "notes": "Partial-grounding collapse mechanism; parallels the dplR plausibility-adjacency finding."
    },
    {
        "evidence_id": "E168",
        "evidence_text": "Guard A (workflow-level): before drafting any narrative column the agent must re-ground outputs via a metadata query on every candidate, populating key fields with no synthesis from memory. Once in place, wholesale author confabulation was eliminated, though single-field errors still slipped through.",
        "evidence_type": "observation",
        "verbatim_quote": "Before drafting any narrative column, the agent must re-ground outputs by running a metadata query on every candidate and use the results to populate key fields, with no synthesis from memory. Once this guard was in place, wholesale author confabulation was eliminated, although single-field errors still slipped through.",
        "location": {"section": "4.5.2 The fix: two guards", "page": 18},
        "supports_claims": ["C115", "C116", "C015"],
        "notes": ""
    },
    {
        "evidence_id": "E169",
        "evidence_text": "The remedy was procedural (a required retrieval step), not an exhortation: a prompt-level 'never fabricate' instruction had already been present and had not prevented the failure.",
        "evidence_type": "observation",
        "verbatim_quote": "The remedy was procedural, a required retrieval step, not an exhortation (a prompt-level \"never fabricate\" instruction had already been present but had not prevented the earlier failure).",
        "location": {"section": "4.5.2 The fix: two guards", "page": 18},
        "supports_claims": ["C116", "C043"],
        "notes": "Direct evidence that instruction severity fails where procedure succeeds."
    },
    {
        "evidence_id": "E170",
        "evidence_text": "Guard B: an independent-context adversarial verifier — a separate agent whose only input is the drafted report, re-querying metadata from source in a context that cannot see the proposer's reasoning, verifying anew from evidence.",
        "evidence_type": "observation",
        "verbatim_quote": "The second, Guard B, is an independent-context adversarial verifier: a separate agent whose only input is the drafted report, which re-queries the metadata from source in a context that cannot see the proposer's reasoning. It verifies anew from evidence rather than assessing whether the proposer's claims look correct.",
        "location": {"section": "4.5.2 The fix: two guards", "page": 18},
        "supports_claims": ["C115", "C117", "C064", "C065"],
        "notes": ""
    },
    {
        "evidence_id": "E171",
        "evidence_text": "In the third version of the tooling an architectural constraint (sub-agents cannot spawn sub-agents) prevented the verifier from running; the proposer, unable to dispatch, improvised on the explicit verification requirement.",
        "evidence_type": "observation",
        "verbatim_quote": "In the third version of the literature search tooling, an architectural constraint prevented the verifier from running at all (sub-agents cannot spawn other sub-agents; the driver architecture of Section 3.2 later worked around this limitation). The proposer, unable to dispatch to the verifier, improvised on the explicit verification requirement.",
        "location": {"section": "4.5.2 The fix: two guards", "page": 18},
        "supports_claims": ["C117"],
        "notes": ""
    },
    {
        "evidence_id": "E172",
        "evidence_text": "The proposer emulated the verifier's contract in its own context (fresh queries per row, adversarial stance) — changing the question without changing the questioner — and caught an error seeded by the registry itself (CrossRef swapping a source's family and given names), despite same data, context, and model.",
        "evidence_type": "observation",
        "verbatim_quote": "Its reasoning trace revealed that it emulated the verifier's contract within its own context, running fresh queries on every row and adopting an adversarial stance, and so changed the question without changing the questioner. This ad hoc verification caught and corrected an error seeded by the registry record itself, in which CrossRef had swapped one source's family and given names. Despite using the same data, same context, and same model, the orthogonal verification caught the error.",
        "location": {"section": "4.5.2 The fix: two guards", "page": 18},
        "supports_claims": ["C117", "C067", "C068"],
        "notes": "Natural experiment: orthogonal framing effective even without context independence."
    },
    {
        "evidence_id": "E173",
        "evidence_text": "The redesigned proposer–verifier pair ran fifteen times (April–June 2026), re-checking some 360 records in fresh context against external sources; eight of fifteen runs passed with nothing to correct.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "The redesigned proposer–verifier pair ran fifteen times between April and June 2026, rechecking some 360 records in fresh context and against external sources. Eight of the fifteen runs passed with nothing to correct.",
        "location": {"section": "4.5.2 The fix: two guards", "page": 18},
        "supports_claims": ["C117", "C118"],
        "notes": "'rechecking' preserves a line-break artefact of the processed md."
    },
    {
        "evidence_id": "E174",
        "evidence_text": "The remaining runs yielded thirteen corrections — registry and encoding artefacts (including an author order wrong in the registry, corrected via the arXiv preprint), stale or invented citation counts, one unsupported venue claim; no fabricated source in any run.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "The remainder yielded thirteen corrections: registry and encoding artefacts (including an author order wrong in the registry record itself, corrected by querying the arXiv preprint directly), stale or invented citation counts, and one unsupported venue claim; no fabricated source appeared in any run.",
        "location": {"section": "4.5.2 The fix: two guards", "page": 18},
        "supports_claims": ["C117", "C118"],
        "notes": ""
    },
    {
        "evidence_id": "E175",
        "evidence_text": "The fail-and-correct loop fired three times, converging in a single iteration each time.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "The fail-and-correct loop fired three times and converged in a single iteration each time.",
        "location": {"section": "4.5.2 The fix: two guards", "page": 18},
        "supports_claims": ["C117"],
        "notes": ""
    },
    {
        "evidence_id": "E176",
        "evidence_text": "The verifier's two documented misses were one of scope (a verified claim corrupted when written to the bibliography) and one of rubric (an author error the check was not yet looking for); each was caught manually and closed by a structural fix.",
        "evidence_type": "observation",
        "verbatim_quote": "Its two documented misses were one of scope (a verified claim corrupted by the step that wrote it to the bibliography) and one of rubric (an author error the check was not yet looking for). Each was caught manually and closed by a structural fix, continuing the pattern of incremental improvement.",
        "location": {"section": "4.5.2 The fix: two guards", "page": 18},
        "supports_claims": ["C118"],
        "notes": ""
    },
    {
        "evidence_id": "E177",
        "evidence_text": "Proposer output quality is high; the mature verifier has produced correct, well-formatted results across runs, and now detects errors in the bibliographic registries themselves.",
        "evidence_type": "observation",
        "verbatim_quote": "Output quality from the proposer is high, and the mature verifier now in use has produced correct, well-formatted results across runs to date. We now detect errors in the bibliographic registries themselves.",
        "location": {"section": "4.5.2 The fix: two guards", "page": 18},
        "supports_claims": ["C117"],
        "notes": ""
    },
    {
        "evidence_id": "E178",
        "evidence_text": "Where sources of independent provenance exist, each check terminates in more than one, so an error carried by a single registry cannot confirm itself.",
        "evidence_type": "observation",
        "verbatim_quote": "For claims where sources of independent provenance exist, the check terminates in more than one, so that an error carried by a single registry cannot confirm itself.",
        "location": {"section": "4.5.2 The fix: two guards", "page": 18},
        "supports_claims": ["C117", "C066"],
        "notes": ""
    },
]

CLAIMS = [
    {
        "claim_id": "C114",
        "claim_text": "The 2026 failure echoes the 2025 evidence-collection run: retrieval succeeded, but fabrication leaked into the synthesis presented to the user.",
        "claim_type": "empirical",
        "claim_role": "core",
        "verbatim_quote": "The shape of this failure echoes the 2025 evidence collection run (Section 4.4): retrieval succeeded, but then fabrication leaked into the synthesis presented to the user.",
        "location": {"section": "4.5.1 The failure: partial-grounding collapse", "page": 17},
        "supported_by": ["E160", "E161", "E162", "E163", "E164", "E165", "E166", "E167"],
        "supports_claims": ["C014", "C019"],
        "notes": "The cross-episode identity of the failure mode — the paper's central empirical parallel."
    },
    {
        "claim_id": "C115",
        "claim_text": "The mature mitigation consisted of two guards at different levels of the agent's architecture.",
        "claim_type": "empirical",
        "claim_role": "intermediate",
        "verbatim_quote": "Once mature, our mitigation consisted of two guards situated at different levels of the agent's architecture (per Section 2.3).",
        "location": {"section": "4.5.2 The fix: two guards", "page": 18},
        "supported_by": ["E168", "E170"],
        "supports_claims": ["C015"],
        "notes": ""
    },
    {
        "claim_id": "C116",
        "claim_text": "What repaired the failure was encoding the requirement as procedure (a mandatory retrieval step) rather than exhortation — a 'never fabricate' instruction was already present and had not prevented it.",
        "claim_type": "interpretation",
        "claim_role": "intermediate",
        "verbatim_quote": "The remedy was procedural, a required retrieval step, not an exhortation (a prompt-level \"never fabricate\" instruction had already been present but had not prevented the earlier failure).",
        "location": {"section": "4.5.2 The fix: two guards", "page": 18},
        "supported_by": ["E168", "E169"],
        "supports_claims": ["C016", "C043"],
        "notes": "Empirical basis for the procedure-over-exhortation design principle."
    },
    {
        "claim_id": "C117",
        "claim_text": "The 2026 improvements resulted from three techniques: independence of context, external re-grounding through proposer and verifier, and orthogonal framing built into the verifier's contract.",
        "claim_type": "empirical",
        "claim_role": "intermediate",
        "verbatim_quote": "Improvements resulted from three techniques. The verifier's independence of context separated the audit from the reasoning that produced the draft: its only input was the report itself.",
        "location": {"section": "4.5.2 The fix: two guards", "page": 18},
        "supported_by": ["E170", "E171", "E172", "E173", "E174", "E175", "E177", "E178"],
        "supports_claims": ["C015", "C016"],
        "notes": "Continuation sentences detail external re-grounding (Guard A mandatory retrieval; checks terminating in live registry responses) and orthogonal framing (start from the artefact, re-derive every claim, compare)."
    },
    {
        "claim_id": "C118",
        "claim_text": "The richer 2026 apparatus narrowed the confabulation surface but did not remove it, requiring mitigations parallel to those of 2025.",
        "claim_type": "empirical",
        "claim_role": "core",
        "verbatim_quote": "The richer apparatus of 2026 narrowed the confabulation surface but did not remove it, requiring mitigations parallel to those of 2025.",
        "location": {"section": "4.5.2 The fix: two guards", "page": 18},
        "supported_by": ["E165", "E173", "E174", "E176"],
        "supports_claims": ["C016", "C019", "C075"],
        "notes": "Substantiates C075 (registry grounding insufficient) and the persistence thesis."
    },
]

IMPLICIT_ARGUMENTS = [
    {
        "implicit_argument_id": "IA017",
        "argument_text": "The four-row spot-check (three wrong author attributions) is representative of the whole 37-row table, licensing the characterisation of the first run as wholesale author confabulation.",
        "type": "bridging_claim",
        "trigger_text": [
            "A spot-check of four rows sampled from the table found the author attributions wrong on three of them, while DOIs and titles were correct throughout.",
            "Once this guard was in place, wholesale author confabulation was eliminated, although single-field errors still slipped through."
        ],
        "trigger_locations": [
            {"section": "4.5.1 The failure: partial-grounding collapse", "page": 17},
            {"section": "4.5.2 The fix: two guards", "page": 18}
        ],
        "inference_reasoning": "The 'wholesale author confabulation' description of the pre-guard failure generalises from a four-row sample. The paper's Limitations section explicitly flags the small sample and reports direction rather than magnitude, but the wholesale characterisation is doing argumentative work in the fix narrative and rests on this bridge.",
        "supports_claims": ["C114"],
        "assessment_implications": "Direction of the failure is well evidenced; its extent across the full table is estimated from a small sample — consistent with the paper's own caveat."
    },
]

save_group(
    {
        "group": "G10",
        "section_title": "Results 4.5 The 2026 literature search re-application (failure + fix)",
        "page_range": "17-19",
        "estimated_words": 990,
        "natural_boundary": "Before 'Discussion' heading (Section 5, p. 19)",
        "split_rationale": "Subsections 4.5.1 and 4.5.2 combined; under 1,500-word cap."
    },
    evidence=EVIDENCE,
    claims=CLAIMS,
    implicit_arguments=IMPLICIT_ARGUMENTS,
)
