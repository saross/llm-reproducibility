#!/usr/bin/env python3
"""Pass 3 (explicit RDMAP) — G12: Discussion 5.2 design principles (pp. 21-22).

Equal-attention scan. Design-principle argumentation is claims territory; the
own-practice checkpoint-allocation description is extracted as a method.
"""

from rdmap_lib import save_group

methods = [
    {
        "method_id": "M038",
        "method_text": (
            "Human-checkpoint allocation practice: considerable human judgement spent on early "
            "tool-documentation outputs (model choice, prompt refinement) before stepping back "
            "to spot-checks as quality improved, whereas every literature-search result was "
            "human-reviewed because errors persisted."
        ),
        "method_type": "quality_control",
        "method_status": "explicit",
        "verbatim_quote": (
            "In our work, for example, considerable human judgement was spent on early tool "
            "documentation outputs (choosing a model and refining the prompt) before we "
            "stepped back to spot-checks as quality improved (Olofsson et al., 2014), whereas "
            "a human reviewed every literature search result since errors persisted (Sections "
            "4.3 and 4.1)."
        ),
        "location": {"section": "Discussion", "subsection": "5.2 Design principles (Stage-gated workflows)", "page": 22},
        "implements_designs": ["RD016"],
        "expected_information_missing": [
            "Criteria for 'quality improved' sufficient to step back to spot-checks are not stated",
        ],
    },
]

save_group(
    {
        "group": "G12",
        "section_title": "Discussion 5.2 design principles (re-grounding through mandate-matching)",
        "page_range": "21-22",
        "scan_note": (
            "Equal-attention Discussion scan. The eight design principles are prescriptive "
            "claims (Session B). Own-practice content: checkpoint allocation (M038) "
            "extracted; the external-state summary (Zotero tags, templated CSV, claims "
            "blocks/audit trail) and multi-source-authority statements restate protocols "
            "P007, P002, P009-P010, and P025 and were not duplicated."
        ),
    },
    methods=methods,
)
