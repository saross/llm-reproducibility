#!/usr/bin/env python3
"""Pass 3 (explicit RDMAP) — G17: Supplement A.3 prompt evolution + A.4 ground-truth comparison (pp. 35-38).

Prompt-lineage protocols (metadata v1->v8, register evolution, domestication
adjustments, evidence v1/v5 schemas) and the model-as-prompt-designer and A.4
ground-truth testing methods.
"""

from rdmap_lib import save_group

methods = [
    {
        "method_id": "M044",
        "method_text": (
            "Model-as-prompt-designer collaboration: the researcher enlisted the model as "
            "prompt designer, asking how the definition could be improved to help the model "
            "make determinations — the supplement-level record of the domestication strategy."
        ),
        "method_type": "analysis",
        "method_status": "explicit",
        "verbatim_quote": (
            "The evolution followed a distinctive collaborative strategy: the researcher "
            "enlisted the model as prompt designer, asking \"How could the definition be "
            "improved to help you make that determination?\""
        ),
        "location": {"section": "Supplement A", "subsection": "A.3 Domestication examples", "page": 36},
        "implements_designs": ["RD014"],
        "expected_information_missing": [],
    },
    {
        "method_id": "M045",
        "method_text": (
            "A.4 ground-truth testing for metadata collection: three services tested (named "
            "here as Claude Research, Google Gemini 2.5 Pro, ChatGPT Deep Research) with "
            "Claude retained for production on output quality; FAIMS as primary ground truth, "
            "with outputs for other familiar archaeological tools also validated. Note: "
            "service naming differs from Section 4.3 (recorded pre-submission QA flag); "
            "extracted as stated."
        ),
        "method_type": "validation",
        "method_status": "explicit",
        "verbatim_quote": (
            "We tested three services for metadata collection — Claude Research, Google "
            "Gemini 2.5 Pro, and ChatGPT Deep Research — and retained Claude Research for "
            "production on output quality. The primary ground truth was FAIMS, a tool the "
            "authors created and maintained over a decade; outputs for other familiar "
            "archaeological tools were also validated."
        ),
        "location": {"section": "Supplement A", "subsection": "A.4 Per-tool ground-truth comparison", "page": 36},
        "implements_designs": ["RD026"],
        "expected_information_missing": [
            "Which 'other familiar archaeological tools' were validated is not enumerated",
        ],
    },
]

protocols = [
    {
        "protocol_id": "P030",
        "protocol_text": (
            "Metadata prompt v1-v8 specification: initial prompt requested five prose fields "
            "per tool (description, history, technical discussion, strengths, weaknesses) as "
            "CSV; over eight iterations the schema expanded to 34 data fields — additional "
            "prose fields (interoperability, survivability, alternatives, usage indicators) "
            "plus structured metadata (URLs, repository locations, licence, language, "
            "platform, authors, release dates, development status, institutional backing). "
            "(Line-count sentence spans the p35/p36 break; quote clipped at p35.)"
        ),
        "protocol_type": "prompt_specification",
        "protocol_status": "explicit",
        "verbatim_quote": (
            "The initial metadata prompt requested five prose fields per tool (description, "
            "history, technical discussion, strengths, and weaknesses) formatted as CSV "
            "output. Over eight iterations, the schema expanded to 34 data fields: the "
            "original five were joined by additional prose fields (interoperability, "
            "survivability, alternatives, usage indicators) and structured metadata (URLs, "
            "repository locations, licence, language, platform, authors, release dates, "
            "development status, and institutional backing)."
        ),
        "location": {"section": "Supplement A", "subsection": "A.3 The eight-version metadata prompt", "page": 35},
        "implements_methods": ["M025", "M009"],
        "expected_information_missing": [],
    },
    {
        "protocol_id": "P031",
        "protocol_text": (
            "Prompt-register evolution: emphatic epistemic ground rules of the February "
            "evidence prompts ('ABOVE ALL ELSE... If there is any doubt, there is no doubt'), "
            "copied into early metadata versions, were dropped from the metadata lineage by "
            "version 8 (replaced by controlled vocabularies and validation checks) while the "
            "evidence lineage retained its guardrail deliberately as precision-over-recall "
            "calibration."
        ),
        "protocol_type": "prompt_specification",
        "protocol_status": "explicit",
        "verbatim_quote": (
            "The register evolved with the structure: the emphatic epistemic ground rules of "
            "the February evidence prompts (\"ABOVE ALL ELSE. . . If there is any doubt, "
            "there is no doubt\"), copied into early metadata versions, had been dropped from "
            "the metadata lineage by version 8, their work taken over by controlled "
            "vocabularies and validation checks — while the evidence lineage retained its "
            "guardrail deliberately, as the precision-over-recall calibration described below."
        ),
        "location": {"section": "Supplement A", "subsection": "A.3 Prompt evolution histories", "page": 35},
        "implements_methods": ["M009"],
        "expected_information_missing": [],
    },
    {
        "protocol_id": "P032",
        "protocol_text": (
            "Domestication schema adjustments: loosening the model's overly binary "
            "classification (adding a 'maybe' category for human review), broadening a "
            "discipline-specific definition after cross-domain tools were misclassified, and "
            "separating current from historical information after the model conflated the two."
        ),
        "protocol_type": "prompt_specification",
        "protocol_status": "explicit",
        "verbatim_quote": (
            "This domestication also involved loosening the model's overly binary "
            "classification (adding a \"maybe\" category for human review), broadening a "
            "discipline-specific definition after cross-domain tools were misclassified, and "
            "separating current from historical information after the model conflated the two."
        ),
        "location": {"section": "Supplement A", "subsection": "A.3 Domestication examples", "page": 36},
        "implements_methods": ["M044", "M027"],
        "expected_information_missing": [],
    },
    {
        "protocol_id": "P033",
        "protocol_text": (
            "Evidence prompt version 1 (superseded): a complex 15-column synthesis format "
            "requiring the model to calculate aggregate metrics (commit counts, contributor "
            "numbers, release tags) and produce a single row per tool; consistently failed "
            "with refusals or heavily confabulated synthesis."
        ),
        "protocol_type": "prompt_specification",
        "protocol_status": "explicit",
        "verbatim_quote": (
            "Version 1 specified a complex 15-column synthesis format that required the model "
            "to calculate aggregate metrics (commit counts, contributor numbers, release "
            "tags) and produce a single row per tool. This approach consistently failed: "
            "models either refused the task or produced heavily confabulated synthesis."
        ),
        "location": {"section": "Supplement A", "subsection": "A.3 The fifteen-column to five-column evidence prompt", "page": 36},
        "implements_methods": ["M031", "M009"],
        "expected_information_missing": [],
    },
    {
        "protocol_id": "P034",
        "protocol_text": (
            "Evidence prompt version 5: output reduced to 5 columns (Tool, Year, Source, URL, "
            "AI_Notes) with one row per source and an explicit prohibition of synthesis — "
            "narrowing the model's remit to achieve more extensive and consistent output."
        ),
        "protocol_type": "prompt_specification",
        "protocol_status": "explicit",
        "verbatim_quote": (
            "Version 5 inverted the approach, reducing output to 5 columns (Tool, Year, "
            "Source, URL, AI_Notes) with one row per source and an explicit prohibition of "
            "synthesis."
        ),
        "location": {"section": "Supplement A", "subsection": "A.3 The fifteen-column to five-column evidence prompt", "page": 36},
        "implements_methods": ["M031", "M009"],
        "expected_information_missing": [],
    },
]

save_group(
    {
        "group": "G17",
        "section_title": "Supplement A.3 prompt evolution histories + A.4 per-tool ground-truth comparison",
        "page_range": "35-38",
        "scan_note": (
            "Prompt-lineage protocols (metadata v1-v8, register evolution, domestication "
            "adjustments, evidence v1/v5) and two methods (model-as-designer, A.4 "
            "ground-truth testing). A.4 per-model failure narratives (Gemini version "
            "confusion, ade4 flip, Claude CSV refusal, ArboDat timestamp) are evidence; the "
            "conservative-guardrail paragraph restates P020 and was not duplicated."
        ),
    },
    methods=methods,
    protocols=protocols,
)
