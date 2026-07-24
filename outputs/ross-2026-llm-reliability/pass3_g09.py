#!/usr/bin/env python3
"""Pass 3 (explicit RDMAP) — G9: Results 4.4 Tool evidence collection (pp. 15-17).

Evidence-collection stage method, every-event verification, trial comparison
and production selection, and the evidence-prompt protocols (conservative
guardrail, failed aggregate schema, one-row-per-sighting schema).
"""

from rdmap_lib import save_group

methods = [
    {
        "method_id": "M031",
        "method_text": (
            "Evidence-of-life collection: gathering dated references, citations, releases, and "
            "mentions establishing a temporal footprint for each documented tool."
        ),
        "method_type": "data_collection",
        "method_status": "explicit",
        "verbatim_quote": (
            "The final stage gathered 'evidence of life' for each documented tool: dated "
            "references, citations, releases, and mentions establishing a temporal footprint."
        ),
        "location": {"section": "Results", "subsection": "4.4 Tool evidence collection", "page": 15},
        "implements_designs": ["RD021", "RD013"],
        "expected_information_missing": [],
    },
    {
        "method_id": "M032",
        "method_text": (
            "Every-event verification in fresh context: each of the ~1,040 evidence events "
            "reviewed against the three-point workflow (source exists; source mentions the "
            "tool; year matches), re-grounded in the sources themselves."
        ),
        "method_type": "validation",
        "method_status": "explicit",
        "verbatim_quote": (
            "Every event was reviewed against the three-point workflow of Section 3.1 (source "
            "exists; source mentions the tool; year matches). This check occurred in fresh "
            "context and was re-grounded in the sources themselves."
        ),
        "location": {"section": "Results", "subsection": "4.4 Tool evidence collection", "page": 16},
        "implements_designs": ["RD016", "RD010"],
        "expected_information_missing": [],
    },
    {
        "method_id": "M033",
        "method_text": (
            "Trial comparison and production selection for evidence collection: Claude "
            "(inappropriate tool fragmentation) and Gemini (snapshot-inflated counts) trialled "
            "against ChatGPT Deep Research, which was retained for production on aggregation, "
            "source-type classification, and yield."
        ),
        "method_type": "validation",
        "method_status": "explicit",
        "verbatim_quote": (
            "In trial comparisons Claude fragmented individual tools inappropriately (e.g., "
            "FAIMS was split into four tools: FAIMS, FAIMS Mobile Platform, FAIMS 3.0, and "
            "Fieldmark), requiring manual reconciliation. Gemini inflated counts by treating "
            "successive web-archive snapshots as distinct evidence-events. ChatGPT Deep "
            "Research was used in production since it maintained appropriate aggregation, "
            "classified source types cleanly, and yielded the most evidence."
        ),
        "location": {"section": "Results", "subsection": "4.4 Tool evidence collection", "page": 16},
        "implements_designs": ["RD015", "RD026"],
        "expected_information_missing": [
            "Trial run counts and tool sets used for the comparison are given only in Supplement A",
        ],
    },
]

protocols = [
    {
        "protocol_id": "P020",
        "protocol_text": (
            "Conservative evidence prompt: prohibited synthesis, required the model to report "
            "only what a source explicitly stated (leaving assessment to the researchers), and "
            "articulated a precision-over-recall guardrail ('if there is any doubt, there is "
            "no doubt')."
        ),
        "protocol_type": "prompt_specification",
        "protocol_status": "explicit",
        "verbatim_quote": (
            "Outputs were constrained by a conservative prompt that prohibited synthesis, "
            "required the model to report only what a source explicitly stated (leaving "
            "assessment to the researchers), and articulated a guardrail that traded recall "
            "for precision (\"if there is any doubt, there is no doubt\", from the film Ronin, "
            "Frankenheimer, 1998)."
        ),
        "location": {"section": "Results", "subsection": "4.4 Tool evidence collection", "page": 15},
        "implements_methods": ["M031"],
        "expected_information_missing": [],
    },
    {
        "protocol_id": "P021",
        "protocol_text": (
            "Superseded aggregate-metrics evidence prompt: early iterations asked the model to "
            "compute aggregate metrics and emit one synthesised row per tool; consistently "
            "failed with refusals or confabulations."
        ),
        "protocol_type": "prompt_specification",
        "protocol_status": "explicit",
        "verbatim_quote": (
            "Early iterations of the prompt asked the model to compute aggregate metrics and "
            "emit one synthesised row per tool, but they consistently failed (with refusals or "
            "confabulations)."
        ),
        "location": {"section": "Results", "subsection": "4.4 Tool evidence collection", "page": 15},
        "implements_methods": ["M031", "M009"],
        "expected_information_missing": [],
    },
    {
        "protocol_id": "P022",
        "protocol_text": (
            "One-row-per-sighting evidence schema: refined prompt recording each piece of "
            "evidence individually, decomposing the task and narrowing the model's remit."
        ),
        "protocol_type": "prompt_specification",
        "protocol_status": "explicit",
        "verbatim_quote": (
            "Later, we refined the prompt into a well-specified, one-row-per-sighting schema "
            "that recorded each piece of evidence individually. Decomposing the task and "
            "narrowing the model's remit produced consistent output."
        ),
        "location": {"section": "Results", "subsection": "4.4 Tool evidence collection", "page": 15},
        "implements_methods": ["M031", "M009"],
        "expected_information_missing": [],
    },
]

save_group(
    {
        "group": "G9",
        "section_title": "Results 4.4 Tool evidence collection",
        "page_range": "15-17",
        "scan_note": (
            "Evidence-stage RDMAP: collection method, every-event fresh-context verification, "
            "trial comparison/production selection, and the evidence-prompt lineage "
            "(conservative guardrail; failed v1 aggregate schema; one-row-per-sighting "
            "schema). Verification outcome tables and the ArboDat/dplR narratives are "
            "evidence."
        ),
    },
    methods=methods,
    protocols=protocols,
)
