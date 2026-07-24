#!/usr/bin/env python3
"""Pass 3 (explicit RDMAP) — G15: Supplement A.1 synthesis detail + A.2 per-journal confabulation (pp. 32-34).

The error-classification taxonomy with its category definitions is the RDMAP
content here; per-journal rates and per-model narratives are evidence.
"""

from rdmap_lib import save_group

methods = [
    {
        "method_id": "M042",
        "method_text": (
            "Error-classification taxonomy for discovery verification: outcomes classified as "
            "verified legitimate research software, misattributions (real software not meeting "
            "the supplied tool definition), confabulations (fabricated tools with no "
            "real-world counterpart), or granularity errors (a non-tool entity such as a "
            "project or consortium reported as a specific tool). Note: totals here (243 "
            "unique tools, 155 verified) are among the recorded pre-submission QA flags "
            "(supplement-vs-main-text offsets); extracted as stated."
        ),
        "method_type": "analysis",
        "method_status": "explicit",
        "verbatim_quote": (
            "Across multiple discovery runs against the target journals, the systems "
            "identified 243 unique tools, of which 155 (63.8%) verified as legitimate "
            "research software; 53 (21.8%) were misattributions (real software that did not "
            "meet the definition of 'tool' provided to the model), 33 (13.6%) were "
            "confabulations (fabricated tools with no real-world counterpart), and 2 (0.8%) "
            "were granularity errors (a non-tool entity, such as a project or consortium, "
            "reported as a specific tool)."
        ),
        "location": {"section": "Supplement A", "subsection": "A.2 Per-journal confabulation detail", "page": 33},
        "implements_designs": ["RD016"],
        "expected_information_missing": [
            "Classification procedure (who classified, adjudication of borderline cases) is not described",
        ],
    },
]

save_group(
    {
        "group": "G15",
        "section_title": "Supplement A.1 source synthesis per-model detail + other tools screened out + A.2 per-journal confabulation detail",
        "page_range": "32-34",
        "scan_note": (
            "Equal-attention supplement scan. Synthesis per-model detail and per-journal "
            "rates are evidence (Session B). RDMAP: the error-classification taxonomy with "
            "explicit category definitions (M042). No new protocols."
        ),
    },
    methods=methods,
)
