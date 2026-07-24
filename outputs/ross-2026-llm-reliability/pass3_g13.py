#!/usr/bin/env python3
"""Pass 3 (explicit RDMAP) — G13: Discussion 5.2 end + 5.3 Limitations + 6 Conclusion (pp. 23-24).

Qualification-trials method, reporting-stance designs from Limitations, and the
transparency-provision method.
"""

from rdmap_lib import save_group

designs = [
    {
        "design_id": "RD027",
        "design_text": (
            "Direction-not-magnitude reporting stance: because the samples are small (a "
            "four-row spot-check, a single agent build), the paper reports the direction of "
            "each failure and treats its magnitude as uncertain."
        ),
        "design_type": "scope_definition",
        "design_status": "explicit",
        "verbatim_quote": (
            "The samples mentioned are small (a four-row spotcheck, a single agent build), so "
            "we report the direction of each failure and treat its magnitude as uncertain."
        ),
        "location": {"section": "Discussion", "subsection": "5.3 Limitations", "page": 24},
        "expected_information_missing": [],
    },
    {
        "design_id": "RD028",
        "design_text": (
            "Worked-pattern framing of the verifier: given limited performance testing "
            "(fifteen runs, thirteen corrections, two manually caught misses), the verifier is "
            "presented as a worked design pattern rather than a benchmarked result."
        ),
        "design_type": "scope_definition",
        "design_status": "explicit",
        "verbatim_quote": (
            "As such, we present the verifier as a worked design pattern rather than a "
            "benchmarked result (Section 4.5)."
        ),
        "location": {"section": "Discussion", "subsection": "5.3 Limitations", "page": 24},
        "expected_information_missing": [],
    },
]

methods = [
    {
        "method_id": "M039",
        "method_text": (
            "Instrument-qualification trials: during tool documentation, trials run against "
            "software known first-hand until the task completed reliably and the failure mode "
            "was understood to be all-or-nothing and thus readily identifiable."
        ),
        "method_type": "validation",
        "method_status": "explicit",
        "verbatim_quote": (
            "In our case, during tool documentation, we ran trials against software we knew "
            "first-hand, until we were sure that the task was completing reliably and had come "
            "to understand that failures were all-or-nothing and thus readily identifiable "
            "(Section 4.3)."
        ),
        "location": {"section": "Discussion", "subsection": "5.2 Design principles (Match the mandate)", "page": 23},
        "implements_designs": ["RD026"],
        "expected_information_missing": [
            "Number of qualification trials and the reliability criterion are not quantified",
        ],
    },
    {
        "method_id": "M040",
        "method_text": (
            "Transparency provision: all outputs, specifications, and session transcripts "
            "provided (Supplement A) so readers can assess the paper's claims."
        ),
        "method_type": "quality_control",
        "method_status": "explicit",
        "verbatim_quote": (
            "Provision of all outputs, specifications, and session transcripts (Supplement A) "
            "allows readers to assess our claims."
        ),
        "location": {"section": "Discussion", "subsection": "5.3 Limitations", "page": 24},
        "implements_designs": ["RD019"],
        "expected_information_missing": [
            "Repository location and persistent identifiers for the archived materials are not final in this pre-submission draft",
        ],
    },
]

save_group(
    {
        "group": "G13",
        "section_title": "Discussion 5.2 (end) + 5.3 Limitations + 6 Conclusion",
        "page_range": "23-24",
        "scan_note": (
            "Equal-attention scan. Limitations yields two reporting-stance designs; "
            "qualification trials and transparency provision extracted as methods. The Jones "
            "90% threshold adoption and future-work programme are prescriptive/prospective "
            "claims, not executed RDMAP, and were not extracted."
        ),
    },
    research_designs=designs,
    methods=methods,
)
