#!/usr/bin/env python3
"""Pass 3 (explicit RDMAP) — G3: Background 2.3 Reliability as a property of structure (pp. 4-6).

Theoretical frameworks grounding the study's design, plus one explicit method of
the authors' own practice (three-step task decomposition) described within the
background discussion.
"""

from rdmap_lib import save_group

designs = [
    {
        "design_id": "RD008",
        "design_text": (
            "Theoretical framework: compound AI systems — quality and reliability arise not from "
            "the model itself but as a property of interacting components (multiple model calls, "
            "retrievers, external tools), grounding the paper's system-level treatment of "
            "reliability."
        ),
        "design_type": "theoretical_framework",
        "design_status": "explicit",
        "verbatim_quote": (
            "A growing body of work on compound AI systems contends that quality and reliability "
            "arise not from the model itself, but as a property of interacting components, "
            "including multiple calls to one or more models, alongside invocation of retrievers "
            "or other external tools (Zaharia et al., 2024)."
        ),
        "location": {"section": "Background", "subsection": "2.3 Reliability as a property of structure", "page": 4},
        "expected_information_missing": [],
    },
    {
        "design_id": "RD009",
        "design_text": (
            "Conceptual structure for the study's scaffolding: two complementary halves — "
            "building judgement into the workflow (decomposition and externalisation) and "
            "verifying whether it worked from a position the producer cannot influence. This "
            "framework organises both the Methods account and the design principles."
        ),
        "design_type": "theoretical_framework",
        "design_status": "explicit",
        "verbatim_quote": (
            "Reliability, therefore, must be engineered into the scaffolding of the human–AI "
            "system (Ballsun-Stanton and S. A. Ross, 2026). That scaffold has two complementary "
            "halves: building judgement into the workflow, so the model can do the task, and "
            "verifying whether it worked, from a position the producer cannot influence."
        ),
        "location": {"section": "Background", "subsection": "2.3 Reliability as a property of structure", "page": 5},
        "expected_information_missing": [],
    },
    {
        "design_id": "RD010",
        "design_text": (
            "Verification-design framework: because unaided LLM (self or second) and human "
            "review both fail, verification power must come from the compound system — "
            "especially independence of context and external reference (later joined by "
            "orthogonal framing). This framework governs the study's verification architecture."
        ),
        "design_type": "theoretical_framework",
        "design_status": "explicit",
        "verbatim_quote": (
            "Again, decomposition is necessary but not sufficient; the mechanics of the "
            "verification are also important. Unaided LLM (self or second) and human review "
            "both fail, so verification power has to come from the compound system, especially "
            "independence and external reference."
        ),
        "location": {"section": "Background", "subsection": "2.3 Reliability as a property of structure", "page": 5},
        "expected_information_missing": [],
    },
]

methods = [
    {
        "method_id": "M001",
        "method_text": (
            "Three-step task decomposition of the software-tool research: after initial failures "
            "of an integrated approach, the task was split into tool discovery, tool "
            "documentation, and cataloguing tool-use evidence."
        ),
        "method_type": "data_collection",
        "method_status": "explicit",
        "verbatim_quote": (
            "After initial failures of an integrated approach, for example, we split our own "
            "software tool research into three steps: tool discovery, tool documentation, and "
            "cataloguing tool use evidence (Section 4)."
        ),
        "location": {"section": "Background", "subsection": "2.3 Reliability as a property of structure", "page": 5},
        "implements_designs": ["RD009"],
        "expected_information_missing": [
            "The 'initial failures of an integrated approach' that motivated the split are not documented in detail",
        ],
    },
]

save_group(
    {
        "group": "G3",
        "section_title": "Background 2.3 Reliability as a property of structure",
        "page_range": "4-6",
        "scan_note": (
            "Three theoretical frameworks extracted as designs (compound systems, two-halves "
            "scaffold, verification principles); one own-practice method (three-step "
            "decomposition) described within the background. The CSV output-constraint mention "
            "(p. 5) is extracted with the templating protocol in G4 where fully described."
        ),
    },
    research_designs=designs,
    methods=methods,
)
