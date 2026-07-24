#!/usr/bin/env python3
"""Pass 3 (explicit RDMAP) — G16: Supplement A.2 episode anatomy (pp. 34-35).

Transcript-based failure diagnosis method and the o3-mini-high verification
instruction protocol.
"""

from rdmap_lib import save_group

methods = [
    {
        "method_id": "M043",
        "method_text": (
            "Transcript-based failure diagnosis: chat transcripts examined to identify failure "
            "triggers (e.g., the JOAD silent mode-switch identified from the internal "
            "reasoning trace after prompting to continue from volumes 1-8 to 9-16)."
        ),
        "method_type": "analysis",
        "method_status": "explicit",
        "verbatim_quote": (
            "Examination of the chat transcript revealed the trigger: when prompted to "
            "continue from JOAD volumes 1–8 (which used research mode and returned legitimate "
            "articles) to volumes 9–16, ChatGPT Deep Research silently dropped out of "
            "research mode."
        ),
        "location": {"section": "Supplement A", "subsection": "A.2 The JOAD silent mode-switch", "page": 34},
        "implements_designs": ["RD014"],
        "expected_information_missing": [],
    },
]

protocols = [
    {
        "protocol_id": "P029",
        "protocol_text": (
            "o3-mini-high verification instruction protocol: complete run output supplied as "
            "CSV input with explicit instructions — 'Do not search for articles. Use the CSV "
            "I gave you. My intention is for you to read each article as linked.'"
        ),
        "protocol_type": "verification",
        "protocol_status": "explicit",
        "verbatim_quote": (
            "Suspicious of the JOSS output, the researcher tasked o3-mini-high with verifying "
            "Deep Research's results, supplying the complete run output as a CSV input with "
            "explicit instructions: \"Do not search for articles. Use the CSV I gave you. My "
            "intention is for you to read each article as linked.\""
        ),
        "location": {"section": "Supplement A", "subsection": "A.2 The o3-mini-high verification pass", "page": 34},
        "implements_methods": ["M024"],
        "expected_information_missing": [],
    },
]

save_group(
    {
        "group": "G16",
        "section_title": "Supplement A.2 episode anatomy (JOAD mode-switch, JOSS DOI-walking, o3-mini-high pass, fabricated performance, difficulty-avoidant substitution, Debates snippet)",
        "page_range": "34-35",
        "scan_note": (
            "Equal-attention supplement scan. Episode anatomies are evidence (Session B). "
            "RDMAP: transcript-based diagnosis method (M043) and the o3-mini-high "
            "verification instruction protocol (P029). The verification-run count-exclusion "
            "rule (excluded from Table 4 discovery counts) spans a page break + footnote and "
            "is recorded here as a scan note rather than a separate protocol."
        ),
    },
    methods=methods,
    protocols=protocols,
)
