#!/usr/bin/env python3
"""Pass 3 (explicit RDMAP) — G10: Results 4.5 The 2026 literature search re-application (pp. 17-19).

The 2026 episode's verification methods and the two-guard protocols (Guard A
re-grounding, Guard B independent-context verifier, multi-source checking).
"""

from rdmap_lib import save_group

methods = [
    {
        "method_id": "M034",
        "method_text": (
            "Sampled spot-check of the agent's first run: four rows sampled from the 37-row "
            "findings table, checking author attributions, DOIs, and titles."
        ),
        "method_type": "validation",
        "method_status": "explicit",
        "verbatim_quote": (
            "A spot-check of four rows sampled from the table found the author attributions "
            "wrong on three of them, while DOIs and titles were correct throughout."
        ),
        "location": {"section": "Results", "subsection": "4.5.1 The failure: partial-grounding collapse", "page": 17},
        "implements_designs": ["RD016"],
        "expected_information_missing": [
            "Sampling procedure for the four rows is not described",
        ],
    },
    {
        "method_id": "M035",
        "method_text": (
            "Two-guard mitigation architecture: once mature, mitigation consisted of two "
            "guards situated at different levels of the agent's architecture (workflow-level "
            "re-grounding and independent-context verification)."
        ),
        "method_type": "quality_control",
        "method_status": "explicit",
        "verbatim_quote": (
            "Like the 2025 prompts, the agent-based approach to literature survey evolved over "
            "several iterations. Once mature, our mitigation consisted of two guards situated "
            "at different levels of the agent's architecture (per Section 2.3)."
        ),
        "location": {"section": "Results", "subsection": "4.5.2 The fix: two guards", "page": 18},
        "implements_designs": ["RD010", "RD012"],
        "expected_information_missing": [],
    },
    {
        "method_id": "M036",
        "method_text": (
            "Operational deployment of the redesigned proposer-verifier pair: fifteen runs "
            "between April and June 2026, re-checking some 360 records in fresh context and "
            "against external sources."
        ),
        "method_type": "validation",
        "method_status": "explicit",
        "verbatim_quote": (
            "The redesigned proposer–verifier pair ran fifteen times between April and June "
            "2026, rechecking some 360 records in fresh context and against external sources."
        ),
        "location": {"section": "Results", "subsection": "4.5.2 The fix: two guards", "page": 18},
        "implements_designs": ["RD017", "RD016"],
        "expected_information_missing": [],
    },
]

protocols = [
    {
        "protocol_id": "P023",
        "protocol_text": (
            "Guard A — workflow-level re-grounding: before drafting any narrative column, the "
            "proposer agent must re-ground outputs by running a metadata query on every "
            "candidate and use the results to populate key fields, with no synthesis from "
            "memory; a required retrieval step rather than an exhortation."
        ),
        "protocol_type": "verification",
        "protocol_status": "explicit",
        "verbatim_quote": (
            "The first, Guard A, is an explicit workflow-level discipline incorporated into "
            "the proposer agent. Before drafting any narrative column, the agent must "
            "re-ground outputs by running a metadata query on every candidate and use the "
            "results to populate key fields, with no synthesis from memory."
        ),
        "location": {"section": "Results", "subsection": "4.5.2 The fix: two guards", "page": 18},
        "implements_methods": ["M035"],
        "expected_information_missing": [],
    },
    {
        "protocol_id": "P024",
        "protocol_text": (
            "Guard B — independent-context adversarial verifier: a separate agent whose only "
            "input is the drafted report, re-querying metadata from source in a context that "
            "cannot see the proposer's reasoning; it verifies anew from evidence rather than "
            "assessing whether the proposer's claims look correct."
        ),
        "protocol_type": "verification",
        "protocol_status": "explicit",
        "verbatim_quote": (
            "The second, Guard B, is an independent-context adversarial verifier: a separate "
            "agent whose only input is the drafted report, which re-queries the metadata from "
            "source in a context that cannot see the proposer's reasoning. It verifies anew "
            "from evidence rather than assessing whether the proposer's claims look correct."
        ),
        "location": {"section": "Results", "subsection": "4.5.2 The fix: two guards", "page": 18},
        "implements_methods": ["M035"],
        "expected_information_missing": [],
    },
    {
        "protocol_id": "P025",
        "protocol_text": (
            "Multi-source independence check: for claims where sources of independent "
            "provenance exist, the verifier's check terminates in more than one source, so an "
            "error carried by a single registry cannot confirm itself (e.g., a registry author- "
            "order error corrected by querying the arXiv preprint directly)."
        ),
        "protocol_type": "verification",
        "protocol_status": "explicit",
        "verbatim_quote": (
            "For claims where sources of independent provenance exist, the check terminates in "
            "more than one, so that an error carried by a single registry cannot confirm "
            "itself."
        ),
        "location": {"section": "Results", "subsection": "4.5.2 The fix: two guards", "page": 18},
        "implements_methods": ["M035"],
        "expected_information_missing": [
            "Which claim types have multi-source coverage is not enumerated",
        ],
    },
]

save_group(
    {
        "group": "G10",
        "section_title": "Results 4.5 The 2026 literature search re-application (failure + fix)",
        "page_range": "17-19",
        "scan_note": (
            "2026-episode RDMAP: spot-check method, two-guard architecture, 15-run "
            "deployment, and the Guard A / Guard B / multi-source protocols. The "
            "partial-grounding-collapse narrative and correction counts are evidence; the "
            "improvised-verifier episode is evidence (its design implications extracted in "
            "Discussion groups)."
        ),
    },
    methods=methods,
    protocols=protocols,
)
