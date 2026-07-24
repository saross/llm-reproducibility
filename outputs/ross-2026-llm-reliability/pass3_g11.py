#!/usr/bin/env python3
"""Pass 3 (explicit RDMAP) — G11: Discussion 5 + 5.1 + 5.2 opening (pp. 19-20).

Equal-attention scan of the Discussion. Own-practice methodology surfacing
here: the build-fail-fix development loop and the decomposed-production
granularity practice.
"""

from rdmap_lib import save_group

methods = [
    {
        "method_id": "M037",
        "method_text": (
            "Build-fail-fix system-construction loop: build the tool, run it on a real task, "
            "manually observe and characterise the failure, design a scaffold around it, "
            "re-test — the persistent development experience across both episodes."
        ),
        "method_type": "analysis",
        "method_status": "explicit",
        "verbatim_quote": (
            "The experience of constructing systems also persisted: build the tool, run it on "
            "a real task, manually observe and characterise the failure, design a scaffold "
            "around it, re-test."
        ),
        "location": {"section": "Discussion", "subsection": "5.1 The persistence finding", "page": 20},
        "implements_designs": ["RD012", "RD014"],
        "expected_information_missing": [],
    },
]

protocols = [
    {
        "protocol_id": "P026",
        "protocol_text": (
            "Decomposed-production granularity: tool documentation proceeded tool by tool, one "
            "CSV row at a time; tool discovery examined journal issues in small blocks — each "
            "parcel worked in a separate context with results passed upwards as artefacts."
        ),
        "protocol_type": "task_structuring",
        "protocol_status": "explicit",
        "verbatim_quote": (
            "Our tool documentation was most reliable when it proceeded tool by tool, one CSV "
            "row at a time, and tool discovery when it examined journal issues in small blocks "
            "(Sections 3.1, 4.2, and 4.3)."
        ),
        "location": {"section": "Discussion", "subsection": "5.2 Design principles (Independence of context)", "page": 20},
        "implements_methods": ["M009"],
        "expected_information_missing": [],
    },
]

save_group(
    {
        "group": "G11",
        "section_title": "Discussion 5 (opening) + 5.1 The persistence finding + 5.2 opening (independence of context)",
        "page_range": "19-20",
        "scan_note": (
            "Equal-attention Discussion scan. The persistence analysis and design-principle "
            "argumentation are claims (Session B); own-practice methodology extracted where "
            "the Discussion describes what was actually done: build-fail-fix loop (M037) and "
            "decomposed-production granularity (P026). Restatements of the evidence-check and "
            "verifier protocols (already extracted from Methods/Results) not duplicated."
        ),
    },
    methods=methods,
    protocols=protocols,
)
