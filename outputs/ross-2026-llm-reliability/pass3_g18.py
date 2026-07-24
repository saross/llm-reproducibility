#!/usr/bin/env python3
"""Pass 3 (explicit RDMAP) — G18: Supplement A.5 full evidence-collection error catalogue (pp. 38-39).

Full-review procedure with cross-stage reconciliation and the
unverifiable-category classification rule.
"""

from rdmap_lib import save_group

protocols = [
    {
        "protocol_id": "P035",
        "protocol_text": (
            "Full evidence-event review procedure: all 1,040 evidence events reviewed by hand "
            "and with LLM assistance; for each event, checks that the cited source existed, "
            "that it mentioned the correct tool, and that the stated year matched the "
            "source's publication date, with results reconciled against discovery and "
            "metadata outcomes."
        ),
        "protocol_type": "verification",
        "protocol_status": "explicit",
        "verbatim_quote": (
            "All 1,040 evidence events were reviewed, by hand and with LLM assistance. For "
            "each event we checked whether the cited source existed, whether it mentioned the "
            "correct tool, and whether the stated year matched the source's publication "
            "date, reconciling results with the discovery and metadata outcomes."
        ),
        "location": {"section": "Supplement A", "subsection": "A.5 Full evidence-collection error catalogue", "page": 38},
        "implements_methods": ["M032", "M012"],
        "expected_information_missing": [
            "Division of labour between hand review and LLM assistance is not quantified",
        ],
    },
    {
        "protocol_id": "P036",
        "protocol_text": (
            "Unverifiable-category classification rule: events whose sources could not be "
            "accessed are recorded as a distinct category — asserted neither confirmed nor "
            "confabulated — because verification could not be completed."
        ),
        "protocol_type": "classification_rule",
        "protocol_status": "explicit",
        "verbatim_quote": (
            "These are not asserted to be either confirmed or confabulated; they are "
            "recorded as a distinct category precisely because the verification could not be "
            "completed."
        ),
        "location": {"section": "Supplement A", "subsection": "A.5 The 22 unverifiable events", "page": 38},
        "implements_methods": ["M032"],
        "expected_information_missing": [],
    },
]

save_group(
    {
        "group": "G18",
        "section_title": "Supplement A.5 full evidence-collection error catalogue + per-model selection comparison",
        "page_range": "38-39",
        "scan_note": (
            "Equal-attention supplement scan. Error catalogue contents (52 confabulated "
            "events, collisions, granularity errors, malformed provenance) and per-model "
            "selection comparison are evidence (Session B). RDMAP: full-review procedure "
            "with reconciliation (P035) and the unverifiable-category rule (P036)."
        ),
    },
    protocols=protocols,
)
