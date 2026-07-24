#!/usr/bin/env python3
"""Pass 3 (explicit RDMAP) — G14: Supplement A intro + A.1 per-tool literature-discovery detail (pp. 30-32).

Supplement-level procedural detail: reasoning-trace examination method, the
lit-discovery prompt revision, and the identical-prompt comparison protocol.
"""

from rdmap_lib import save_group

methods = [
    {
        "method_id": "M041",
        "method_text": (
            "Reasoning-trace examination: model 'thinking' logs examined to diagnose failure "
            "mechanisms (e.g., Gemini's conflation of multiple complex tasks into single "
            "operations)."
        ),
        "method_type": "analysis",
        "method_status": "explicit",
        "verbatim_quote": (
            "Examination of its \"thinking\" logs revealed a tendency to conflate multiple "
            "complex tasks into single operations."
        ),
        "location": {"section": "Supplement A", "subsection": "A.1 The Gemini 'source soup' anecdote", "page": 31},
        "implements_designs": ["RD014"],
        "expected_information_missing": [
            "Which runs' traces were examined, and how systematically, is not stated",
        ],
    },
]

protocols = [
    {
        "protocol_id": "P027",
        "protocol_text": (
            "Lit-discovery prompt revision: an initial standard prompt produced unusable "
            "output; a revised prompt emphasising scholarly sources yielded the documented "
            "results (ChatGPT Deep Research required two prompting attempts)."
        ),
        "protocol_type": "prompt_specification",
        "protocol_status": "explicit",
        "verbatim_quote": (
            "It required two prompting attempts: an initial standard prompt produced unusable "
            "output, while a revised prompt emphasising scholarly sources yielded the "
            "documented results."
        ),
        "location": {"section": "Supplement A", "subsection": "A.1 Per-tool source-type composition and citation accuracy", "page": 30},
        "implements_methods": ["M009"],
        "expected_information_missing": [
            "Neither prompt's text is reproduced",
        ],
    },
    {
        "protocol_id": "P028",
        "protocol_text": (
            "Identical-prompt comparison: the same prompts run across services to compare "
            "yield (e.g., Elicit's 9 useful sources against 55 from Deep Research from "
            "identical prompts)."
        ),
        "protocol_type": "comparison_specification",
        "protocol_status": "explicit",
        "verbatim_quote": (
            "From identical prompts, Elicit yielded only 9 useful sources against 55 from "
            "Deep Research."
        ),
        "location": {"section": "Supplement A", "subsection": "A.1 Per-tool source-type composition and citation accuracy", "page": 31},
        "implements_methods": ["M018"],
        "expected_information_missing": [
            "Which prompt variants were standardised across services is not documented",
        ],
    },
]

save_group(
    {
        "group": "G14",
        "section_title": "Supplement A intro + A.1 per-tool literature-discovery detail, source overlap, Gemini 'source soup'",
        "page_range": "30-32",
        "scan_note": (
            "Equal-attention supplement scan. Mostly granular evidence (per-service yields, "
            "error compositions — Session B). RDMAP: trace-examination method, two-attempt "
            "prompt revision, identical-prompt comparison. Screened-out tool evaluations "
            "(Operator, Computer Use, Claude Code) are evidence supporting RD023."
        ),
    },
    methods=methods,
    protocols=protocols,
)
