#!/usr/bin/env python3
"""Pass 3 (explicit RDMAP) — G2: Background 2.1 + 2.2 (pp. 3-4).

Equal-attention scan. This group is literature argumentation (capabilities
debate, limits of 'disclose and verify'); nearly all content is claims/evidence
territory already extracted in Session B. One design-level framing statement
(the deployment question that motivates the study) is extracted liberally.
"""

from rdmap_lib import save_group

designs = [
    {
        "design_id": "RD007",
        "design_text": (
            "Research agenda framing: the study's question is not whether to use LLMs but how "
            "to deploy them so research tasks complete and output can be trusted, with "
            "verification identified as the practice needing development."
        ),
        "design_type": "research_question",
        "design_status": "explicit",
        "verbatim_quote": (
            "The real question is not whether to use these systems but how to deploy them so "
            "that research tasks can be completed and their output can be trusted. Verification "
            "is where practice needs development."
        ),
        "location": {"section": "Background", "subsection": "2.1 LLMs in research", "page": 3},
        "expected_information_missing": [],
    },
]

save_group(
    {
        "group": "G2",
        "section_title": "Background 2.1 (LLMs in research) + 2.2 (The limits of 'disclose and verify')",
        "page_range": "3-4",
        "scan_note": (
            "Systematic scan performed with equal attention. Group is literature synthesis and "
            "argumentation (verification failure evidence, self-check limits); no procedures of "
            "the present study are documented here. One explicit design-level framing statement "
            "extracted (deployment question). Prior work's methods (Luo et al., Steyvers et al.) "
            "deliberately NOT extracted per literature-review attribution rule."
        ),
    },
    research_designs=designs,
)
