#!/usr/bin/env python3
"""Pass 1, Group G9: Results 4.4 Tool evidence collection (pp. 15-17, ~870 words). Tables 9-10."""

from pass1_lib import save_group

EVIDENCE = [
    {
        "evidence_id": "E142",
        "evidence_text": "The final stage gathered 'evidence of life' for each documented tool: dated references, citations, releases, and mentions establishing a temporal footprint.",
        "evidence_type": "observation",
        "verbatim_quote": "The final stage gathered 'evidence of life' for each documented tool: dated references, citations, releases, and mentions establishing a temporal footprint.",
        "location": {"section": "4.4 Tool evidence collection", "page": 15},
        "supports_claims": ["C106"],
        "notes": ""
    },
    {
        "evidence_id": "E143",
        "evidence_text": "Outputs were constrained by a conservative prompt prohibiting synthesis, requiring the model to report only what a source explicitly stated, and trading recall for precision ('if there is any doubt, there is no doubt').",
        "evidence_type": "observation",
        "verbatim_quote": "Outputs were constrained by a conservative prompt that prohibited synthesis, required the model to report only what a source explicitly stated (leaving assessment to the researchers), and articulated a guardrail that traded recall for precision (\"if there is any doubt, there is no doubt\", from the film Ronin, Frankenheimer, 1998).",
        "location": {"section": "4.4 Tool evidence collection", "page": 15},
        "supports_claims": ["C107", "C112"],
        "notes": "Guardrail design; full prompt lineage in Supplement A."
    },
    {
        "evidence_id": "E144",
        "evidence_text": "Early prompt iterations asking the model to compute aggregate metrics and emit one synthesised row per tool consistently failed (refusals or confabulations); the refined one-row-per-sighting schema recorded each piece of evidence individually.",
        "evidence_type": "observation",
        "verbatim_quote": "Early iterations of the prompt asked the model to compute aggregate metrics and emit one synthesised row per tool, but they consistently failed (with refusals or confabulations). Later, we refined the prompt into a well-specified, one-row-per-sighting schema that recorded each piece of evidence individually.",
        "location": {"section": "4.4 Tool evidence collection", "page": 15},
        "supports_claims": ["C107"],
        "notes": ""
    },
    {
        "evidence_id": "E145",
        "evidence_text": "Production returned roughly a thousand evidence events across nearly a hundred tools, typically around ten per tool.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "Production returned roughly a thousand evidence events across nearly a hundred tools, typically around ten per tool (Table 10).",
        "location": {"section": "4.4 Tool evidence collection", "page": 16},
        "supports_claims": ["C112"],
        "notes": ""
    },
    {
        "evidence_id": "E146",
        "evidence_text": "Every evidence event was reviewed against the three-point workflow (source exists; mentions the tool; year matches), in fresh context and re-grounded in the sources themselves.",
        "evidence_type": "observation",
        "verbatim_quote": "Every event was reviewed against the three-point workflow of Section 3.1 (source exists; source mentions the tool; year matches). This check occurred in fresh context and was re-grounded in the sources themselves.",
        "location": {"section": "4.4 Tool evidence collection", "page": 16},
        "supports_claims": ["C112", "C015"],
        "notes": "The verification applies the paper's own independence and re-grounding prescriptions."
    },
    {
        "evidence_id": "E147",
        "evidence_text": "Over nine in ten events confirmed; residual errors were properties of individual events (mainly fabricated attributions to real sources, plus unretrievable references, granularity misclassifications, and same-name collisions).",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "Over nine in ten confirmed; the residual errors were each a property of an individual event rather than of a search run, and they consisted mainly of fabricated attributions to real sources, alongside some references that could not be retrieved for verification at all and a few granularity misclassifications and same-name collisions (see Table 9).",
        "location": {"section": "4.4 Tool evidence collection", "page": 16},
        "supports_claims": ["C112", "C014"],
        "notes": ""
    },
    {
        "evidence_id": "E148",
        "evidence_text": "In trial comparisons Claude fragmented individual tools inappropriately (FAIMS split into FAIMS, FAIMS Mobile Platform, FAIMS 3.0, and Fieldmark), requiring manual reconciliation.",
        "evidence_type": "observation",
        "verbatim_quote": "In trial comparisons Claude fragmented individual tools inappropriately (e.g., FAIMS was split into four tools: FAIMS, FAIMS Mobile Platform, FAIMS 3.0, and Fieldmark), requiring manual reconciliation.",
        "location": {"section": "4.4 Tool evidence collection", "page": 16},
        "supports_claims": ["C112"],
        "notes": ""
    },
    {
        "evidence_id": "E149",
        "evidence_text": "Gemini inflated counts by treating successive web-archive snapshots as distinct evidence-events.",
        "evidence_type": "observation",
        "verbatim_quote": "Gemini inflated counts by treating successive web-archive snapshots as distinct evidence-events.",
        "location": {"section": "4.4 Tool evidence collection", "page": 16},
        "supports_claims": ["C112"],
        "notes": ""
    },
    {
        "evidence_id": "E150",
        "evidence_text": "ChatGPT Deep Research was used in production because it maintained appropriate aggregation, classified source types cleanly, and yielded the most evidence.",
        "evidence_type": "observation",
        "verbatim_quote": "ChatGPT Deep Research was used in production since it maintained appropriate aggregation, classified source types cleanly, and yielded the most evidence.",
        "location": {"section": "4.4 Tool evidence collection", "page": 16},
        "supports_claims": ["C112"],
        "notes": ""
    },
    {
        "evidence_id": "E151",
        "evidence_text": "Evidence verification outcomes (Table 9, n=1,040): confirmed 945 (90.9%); confabulated 52 (5.0%, source exists but does not mention tool); unverifiable 22 (2.1%); granularity error 17 (1.6%); collision 4 (0.4%).",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "Confirmed 945 90.9 Source exists and mentions the correct tool Confabulated 52 5.0 Source exists but does not mention the tool Unverifiable 22 2.1 Could not access source to confirm or deny Granularity error 17 1.6 Source verified but tool classification invalid Collision 4 0.4 Source mentions a different tool with the same name Total 1,040 100",
        "location": {"section": "4.4 Tool evidence collection", "page": 16},
        "supports_claims": ["C112", "C014"],
        "notes": "Flattened Table 9; layout verifiable against the PDF."
    },
    {
        "evidence_id": "E152",
        "evidence_text": "Evidence collection summary (Table 10, part 1): 1,040 total events; 945 confirmed (90.9%); 96 unique tools; 94 tools with confirmed events; 962 production events via ChatGPT DR (92.5%); 75 trial events (7.2%); 3 malformed provenance (0.3%).",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "Total evidence events 1,040 Confirmed events 945 (90.9%) Unique tools 96 Tools with confirmed events 94 Production events (ChatGPT DR) 962 (92.5%) Trial/model-comparison events 75 (7.2%) Malformed provenance 3 (0.3%)",
        "location": {"section": "4.4 Tool evidence collection", "page": 16},
        "supports_claims": ["C112"],
        "notes": "Flattened Table 10 (upper rows); layout verifiable against the PDF."
    },
    {
        "evidence_id": "E153",
        "evidence_text": "Evidence collection summary (Table 10, part 2): confirmed events per tool mean 10.1 / median 9; events per tool range 1–41; year range 1995–2025; undated events 139 (13.4%); contributions BBS 840 (80.8%), SAR 197 (18.9%).",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "Confirmed events per tool (mean / median) 10.1 / 9 Events per tool (range) 1–41 Year range 1995–2025 Undated events 139 (13.4%) BBS contributions 840 (80.8%) SAR contributions 197 (18.9%)",
        "location": {"section": "4.4 Tool evidence collection", "page": 16},
        "supports_claims": ["C112"],
        "notes": "Flattened Table 10 (lower rows); layout verifiable against the PDF."
    },
    {
        "evidence_id": "E154",
        "evidence_text": "Failures were fractal: bad rows interleaved with good ones, and within a bad row individual fabricated fields hid among genuine ones.",
        "evidence_type": "observation",
        "verbatim_quote": "Failures were fractal: bad rows were interleaved with good ones, and within a bad row, individual fabricated fields hid among genuine ones.",
        "location": {"section": "4.4 Tool evidence collection", "page": 16},
        "supports_claims": ["C108", "C014"],
        "notes": "Following sentence spans the p16/p17 page break; verifiable against the PDF."
    },
    {
        "evidence_id": "E155",
        "evidence_text": "Almost two-thirds of confabulated events were real sources cited for a tool they never mentioned; other cases invented version-release events, fabricated DOIs, or attached evidence to a same-name tool. All read fluently.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "Almost two-thirds of confabulated events were real sources cited for a tool they never mentioned. In other cases, version-release events were invented, DOIs were fabricated, or evidence attached to an unrelated tool with the same name. All read fluently.",
        "location": {"section": "4.4 Tool evidence collection", "page": 17},
        "supports_claims": ["C108", "C014"],
        "notes": ""
    },
    {
        "evidence_id": "E156",
        "evidence_text": "Confabulated events dispersed across many tools, but dplR — heavily documented with a long version history — attracted the largest share (12 of 52), every one an invented release event.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "Confabulated events were dispersed across many tools, but a single, heavily documented package (dplR) attracted the largest share (12 of 52), every one an invented release event for a real package with a long version history.",
        "location": {"section": "4.4 Tool evidence collection", "page": 17},
        "supports_claims": ["C109"],
        "notes": ""
    },
    {
        "evidence_id": "E157",
        "evidence_text": "For ArboDat, the model reached the homepage stating the software 'has been developed since 1997', recorded the statement in its notes, yet failed to carry 1997 into any date field (reporting 'no date'); other rows took a year from the citing page's much later date.",
        "evidence_type": "observation",
        "verbatim_quote": "Collecting evidence for ArboDat, the model reached the tool's homepage, which states plainly that the software \"has been developed since 1997\"; it read the page and recorded the statement in its notes, yet failed to carry 1997 into any date field, reporting \"no date\" instead. Other ArboDat rows carried a year, but taken from the citing page's own (much later) date.",
        "location": {"section": "4.4 Tool evidence collection", "page": 17},
        "supports_claims": ["C110", "C111"],
        "notes": "Companion paper (Ballsun-Stanton and Ross 2026) analyses this error epistemologically."
    },
    {
        "evidence_id": "E158",
        "evidence_text": "Only record-by-record human review that re-read the source caught the ArboDat date failure.",
        "evidence_type": "observation",
        "verbatim_quote": "Only record-by-record human review that re-read the source caught it.",
        "location": {"section": "4.4 Tool evidence collection", "page": 17},
        "supports_claims": ["C111", "C015"],
        "notes": ""
    },
]

CLAIMS = [
    {
        "claim_id": "C106",
        "claim_text": "In evidence collection the unit of error was the individual claim, and the dataset was large enough that an error rate of a few per cent would produce many spurious records.",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "verbatim_quote": "The unit of error was the individual claim, and the dataset was large enough that an error rate of a few per cent would produce many spurious records.",
        "location": {"section": "4.4 Tool evidence collection", "page": 15},
        "supported_by": ["E142"],
        "supports_claims": ["C071"],
        "notes": ""
    },
    {
        "claim_id": "C107",
        "claim_text": "Decomposing the task and narrowing the model's remit produced consistent output.",
        "claim_type": "empirical",
        "claim_role": "intermediate",
        "verbatim_quote": "Decomposing the task and narrowing the model's remit produced consistent output.",
        "location": {"section": "4.4 Tool evidence collection", "page": 15},
        "supported_by": ["E143", "E144"],
        "supports_claims": ["C053", "C080", "C015"],
        "notes": ""
    },
    {
        "claim_id": "C108",
        "claim_text": "Evidence collection was the hardest stage to verify.",
        "claim_type": "empirical",
        "claim_role": "supporting",
        "verbatim_quote": "This stage was the hardest to verify.",
        "location": {"section": "4.4 Tool evidence collection", "page": 16},
        "supported_by": ["E154", "E155"],
        "supports_claims": ["C112"],
        "notes": ""
    },
    {
        "claim_id": "C109",
        "claim_text": "The dplR concentration suggests abundant genuine material lends plausibility to adjacent fabrications.",
        "claim_type": "interpretation",
        "claim_role": "intermediate",
        "verbatim_quote": "This concentration suggests that abundant, genuine material lends plausibility to adjacent fabrications (see Section 4.5).",
        "location": {"section": "4.4 Tool evidence collection", "page": 17},
        "supported_by": ["E156"],
        "supports_claims": ["C014"],
        "notes": "Anticipates the partial-grounding collapse mechanism of Section 4.5."
    },
    {
        "claim_id": "C110",
        "claim_text": "Dates were a consistent problem in evidence collection.",
        "claim_type": "empirical",
        "claim_role": "supporting",
        "verbatim_quote": "Dates were a consistent problem.",
        "location": {"section": "4.4 Tool evidence collection", "page": 17},
        "supported_by": ["E157"],
        "supports_claims": ["C014"],
        "notes": ""
    },
    {
        "claim_id": "C111",
        "claim_text": "The ArboDat failure lay not in retrieval, nor in reading the source, but in carrying what was read into the record.",
        "claim_type": "interpretation",
        "claim_role": "intermediate",
        "verbatim_quote": "The failure lay not in retrieval, nor even in reading the source, but in carrying what it read into the record.",
        "location": {"section": "4.4 Tool evidence collection", "page": 17},
        "supported_by": ["E157", "E158"],
        "supports_claims": ["C014"],
        "notes": "Locates the failure at the synthesis boundary — retrieval succeeded, composition failed."
    },
    {
        "claim_id": "C112",
        "claim_text": "Across all four 2025 stages, reliable output rested on a deliberate guard (iteratively refined narrowed prompts, explicit constraints, process monitoring, externally re-grounded verification); where a guard was absent or silently bypassed, fluent fabrication followed.",
        "claim_type": "empirical",
        "claim_role": "core",
        "verbatim_quote": "Taken together, the four stages of research indicate that where output was reliable, such as verified tools, accurate metadata, or confirmed evidence, a deliberate guard underpinned success: an iteratively refined, deliberately narrowed prompt; explicit constraints; process monitoring; human or machine verification re-grounded outside the producing context. Where a guard was absent or silently bypassed, fluent fabrication followed.",
        "location": {"section": "4.4 Tool evidence collection", "page": 17},
        "supported_by": ["E143", "E145", "E146", "E147", "E151", "E152", "E153"],
        "supports_claims": ["C080", "C016", "C015"],
        "notes": "The 2025 campaign's summary finding."
    },
    {
        "claim_id": "C113",
        "claim_text": "Literature discovery is deliberately omitted from the reliable-output list: its yield was valuable, but its output never became reliable under any 2025 scaffold — reliability came only from wholesale manual verification and correction.",
        "claim_type": "empirical",
        "claim_role": "intermediate",
        "verbatim_quote": "The omission of literature discovery from the list is deliberate: its yield was valuable, but its output never became reliable under any 2025 scaffold. Reliability was only achieved through wholesale manual verification and correction.",
        "location": {"section": "4.4 Tool evidence collection", "page": 17},
        "supported_by": ["E086", "E089"],
        "supports_claims": ["C112"],
        "notes": "Sets up the 2026 literature-search re-application as the unresolved case."
    },
]

IMPLICIT_ARGUMENTS = [
    {
        "implicit_argument_id": "IA016",
        "argument_text": "The LLM-based review of evidence events, because it ran in fresh context and was re-grounded in the sources, is itself trustworthy — the design mitigations suffice to exempt this verifier from the model-verification failures the paper documents elsewhere.",
        "type": "methodological_assumption",
        "trigger_text": [
            "Every event was reviewed against the three-point workflow of Section 3.1 (source exists; source mentions the tool; year matches). This check occurred in fresh context and was re-grounded in the sources themselves.",
            "Since the scale of evidence-events was greater and no ready-made external source equivalent to open-archaeo was available, evidence-events were LLM-reviewed against a documented three-point workflow (the source exists; it mentions the tool; the stated year matches)."
        ],
        "trigger_locations": [
            {"section": "4.4 Tool evidence collection", "page": 16},
            {"section": "3.1 The 2025 phase: systematic evaluation", "page": 8}
        ],
        "inference_reasoning": "The 90.9% confirmed rate is produced largely by an LLM verifier. The paper's own results (o3-mini-high episode; self-check literature) show model verification can fail; the design here differs in exactly the ways the paper argues matter (fresh context, source re-grounding, narrow binary checks, manual spot-checks), but the sufficiency of those differences for this verifier is assumed rather than independently measured.",
        "supports_claims": ["C112"],
        "assessment_implications": "The headline verification statistics inherit the reliability of the verifying workflow; the paper's later verifier-testing figures (thirteen corrections, two missed errors in fifteen runs, for the 2026 verifier) suggest good but imperfect catching power."
    },
]

save_group(
    {
        "group": "G9",
        "section_title": "Results 4.4 Tool evidence collection",
        "page_range": "15-17",
        "estimated_words": 870,
        "natural_boundary": "Before '4.5 The 2026 literature search re-application' heading (p. 17)",
        "split_rationale": "Single Results subsection; under 1,500-word cap. Tables 9-10 extracted as flattened quotes."
    },
    evidence=EVIDENCE,
    claims=CLAIMS,
    implicit_arguments=IMPLICIT_ARGUMENTS,
)
