#!/usr/bin/env python3
"""Pass 3 (explicit RDMAP) — G8: Results 4.3 Tool documentation (pp. 13-15).

Metadata-collection stage: FAIMS ground-truth design, service assessment,
work-with-the-grain schema evolution, orthogonal checking, manual accuracy
checks, the March 2026 slop re-assessment, and the metadata prompt protocols.
"""

from rdmap_lib import save_group

designs = [
    {
        "design_id": "RD026",
        "design_text": (
            "FAIMS ground-truth design: model selection for the documentation stage rested on "
            "comparison of output across four prompt iterations against FAIMS, software the "
            "authors built and maintained over a decade — using first-hand knowledge as ground "
            "truth."
        ),
        "design_type": "study_design",
        "design_status": "explicit",
        "verbatim_quote": (
            "We had built and maintained FAIMS over a decade, and model selection rested on "
            "comparison of output across four prompt iterations against it."
        ),
        "location": {"section": "Results", "subsection": "4.3 Tool documentation", "page": 13},
        "expected_information_missing": [],
    },
]

methods = [
    {
        "method_id": "M025",
        "method_text": (
            "Metadata-collection stage method: structured metadata collected for each verified "
            "tool, with the scaffolding (the metadata prompt) treated as an explicit artefact."
        ),
        "method_type": "data_collection",
        "method_status": "explicit",
        "verbatim_quote": (
            "The third stage collected structured metadata for each verified tool, and here "
            "the scaffolding became an explicit artefact."
        ),
        "location": {"section": "Results", "subsection": "4.3 Tool documentation", "page": 13},
        "implements_designs": ["RD021"],
        "expected_information_missing": [],
    },
    {
        "method_id": "M026",
        "method_text": (
            "Comparative three-service assessment for metadata collection: OpenAI o3, Claude "
            "Sonnet 3.7 in research mode, and Gemini 2.5 Pro via Google AI Studio."
        ),
        "method_type": "validation",
        "method_status": "explicit",
        "verbatim_quote": (
            "We assessed three services: OpenAI o3, Claude Sonnet 3.7 in research mode, and "
            "Gemini 2.5 Pro via Google AI Studio."
        ),
        "location": {"section": "Results", "subsection": "4.3 Tool documentation", "page": 13},
        "implements_designs": ["RD026", "RD015"],
        "expected_information_missing": [
            "Note: Supplement A.4 names the services differently (Claude Research, Google Gemini 2.5 Pro, ChatGPT Deep Research) — recorded as presubmission QA flag in Session B; extracted as stated in each location",
        ],
    },
    {
        "method_id": "M027",
        "method_text": (
            "Work-with-the-grain schema evolution: recurring revision principle of folding the "
            "model's spontaneous tendencies into the schema rather than fighting them "
            "(domesticating unwanted tendencies; codifying useful additions)."
        ),
        "method_type": "analysis",
        "method_status": "explicit",
        "verbatim_quote": (
            "One principle recurred across these revisions: work with the model's grain, "
            "folding its spontaneous tendencies into the schema rather than fighting them."
        ),
        "location": {"section": "Results", "subsection": "4.3 Tool documentation", "page": 13},
        "implements_designs": ["RD014"],
        "expected_information_missing": [],
    },
    {
        "method_id": "M028",
        "method_text": (
            "Orthogonal metadata check on discovery outputs: in fresh context, asking for a "
            "tool's repository, licence, and version (rather than merely whether it existed) "
            "exposed misattributions and granularity errors that had survived discovery "
            "verification. (The second sentence spans the p14/p15 break; quote clipped to the "
            "first sentence.)"
        ),
        "method_type": "validation",
        "method_status": "explicit",
        "verbatim_quote": (
            "Metadata collection doubled as an orthogonal check on discovery outputs."
        ),
        "location": {"section": "Results", "subsection": "4.3 Tool documentation", "page": 14},
        "implements_designs": ["RD016", "RD010"],
        "expected_information_missing": [],
    },
    {
        "method_id": "M029",
        "method_text": (
            "Manual accuracy checking of documentation outputs against first-hand knowledge "
            "or external sources (open-archaeo catalogue, GitHub)."
        ),
        "method_type": "quality_control",
        "method_status": "explicit",
        "verbatim_quote": (
            "We manually checked accuracy against first-hand knowledge of tools or against "
            "sources like the open-archaeo catalogue and GitHub."
        ),
        "location": {"section": "Results", "subsection": "4.3 Tool documentation", "page": 15},
        "implements_designs": ["RD016"],
        "expected_information_missing": [
            "Sampling and coverage of the manual checks are not quantified",
        ],
    },
    {
        "method_id": "M030",
        "method_text": (
            "Slop re-assessment (March 2026): Claude Opus 4.6 assessed 88 of 89 documented "
            "entries using the Shaib et al. (2025) slop taxonomy, with overall severity "
            "summarised on a four-band scale of the authors' own design; assessment measured "
            "stylistic quality and information density, not factual accuracy, with "
            "self-preference bias acknowledged."
        ),
        "method_type": "analysis",
        "method_status": "explicit",
        "verbatim_quote": (
            "In March 2026, a newer Claude model (Opus 4.6) subsequently assessed 88 of the 89 "
            "documented entries (one was excluded by a configuration error) using the slop "
            "taxonomy proposed by Shaib et al. (2025), with overall severity summarised on a "
            "four-band scale of our own design (Shaib et al.'s protocol elicits a binary "
            "judgement)."
        ),
        "location": {"section": "Results", "subsection": "4.3 Tool documentation", "page": 15},
        "implements_designs": ["RD014"],
        "expected_information_missing": [
            "The configuration error that excluded one entry is not described",
        ],
    },
]

protocols = [
    {
        "protocol_id": "P015",
        "protocol_text": (
            "Metadata prompt eight-iteration evolution: from five prose fields rendered as CSV "
            "to a thirty-four-field schema, each elaboration fixing a documented failure or "
            "absence in the previous run."
        ),
        "protocol_type": "prompt_specification",
        "protocol_status": "explicit",
        "verbatim_quote": (
            "The metadata prompt began as five prose fields rendered as commaseparated values "
            "and grew, over eight iterations, into a thirty-four-field schema, each "
            "elaboration fixing a documented failure or absence in the previous run."
        ),
        "location": {"section": "Results", "subsection": "4.3 Tool documentation", "page": 13},
        "implements_methods": ["M025", "M009"],
        "expected_information_missing": [
            "Per-iteration change log is summarised only in Supplement A.3",
        ],
    },
    {
        "protocol_id": "P016",
        "protocol_text": (
            "History-field domestication: when Claude persisted in supplying version histories "
            "despite requests for a current snapshot only, a structured history field was "
            "added to the schema."
        ),
        "protocol_type": "prompt_specification",
        "protocol_status": "explicit",
        "verbatim_quote": (
            "Sometimes that meant 'domesticating' an initially unwanted tendency. When Claude, "
            "for example, was asked to provide only a current snapshot of each tool but "
            "persisted in supplying version histories, we added a structured history field."
        ),
        "location": {"section": "Results", "subsection": "4.3 Tool documentation", "page": 13},
        "implements_methods": ["M027"],
        "expected_information_missing": [],
    },
    {
        "protocol_id": "P017",
        "protocol_text": (
            "Codification of spontaneous additions: when the model unprompted noted that a "
            "tool's closed, proprietary design undermined reproducibility, instructions were "
            "added to capture 'transparency and reproducibility' consistently."
        ),
        "protocol_type": "prompt_specification",
        "protocol_status": "explicit",
        "verbatim_quote": (
            "Sometimes it meant codifying a useful addition spontaneously produced by the "
            "model. When the model noted in a 'weaknesses' field that one tool's closed, "
            "proprietary design undermined reproducibility, we added instructions to capture "
            "'transparency and reproducibility' consistently."
        ),
        "location": {"section": "Results", "subsection": "4.3 Tool documentation", "page": 13},
        "implements_methods": ["M027"],
        "expected_information_missing": [],
    },
    {
        "protocol_id": "P018",
        "protocol_text": (
            "CSV follow-up workaround: the production model emitted narrative reports on first "
            "response; comma-separated output was obtained via a follow-up 'please provide the "
            "requested CSV' prompt in each session."
        ),
        "protocol_type": "operational_workaround",
        "protocol_status": "explicit",
        "verbatim_quote": (
            "It was retained for production runs, despite one intractable annoyance: it "
            "produced narrative reports only on first response, emitting comma-separated "
            "output only after a follow-up \"please provide the requested CSV\" prompt."
        ),
        "location": {"section": "Results", "subsection": "4.3 Tool documentation", "page": 14},
        "implements_methods": ["M025"],
        "expected_information_missing": [],
    },
    {
        "protocol_id": "P019",
        "protocol_text": (
            "Slop-assessment operationalisation: seven-code taxonomy from Shaib et al. (2025); "
            "four overall assessment bands (none/minimal/moderate/significant) as the authors' "
            "operationalisation, with thresholds on generic-phrase count and anchored-claim "
            "density; anchored claims defined as verifiable factual statements."
        ),
        "protocol_type": "assessment_specification",
        "protocol_status": "explicit",
        "verbatim_quote": (
            "Assessed using the seven-code taxonomy from Shaib et al. (2025); the four overall "
            "assessment bands (none/minimal/moderate/significant) are our operationalisation, "
            "with thresholds on genericphrase count and anchored-claim density, where Shaib et "
            "al. elicit a binary judgement. Anchored claims are verifiable factual statements "
            "(named individuals, specific dates, version numbers, funding codes)."
        ),
        "location": {"section": "Results", "subsection": "4.3 Tool documentation (Table 8 caption)", "page": 15},
        "implements_methods": ["M030"],
        "expected_information_missing": [
            "Numeric threshold values for the four bands are not stated",
        ],
    },
]

save_group(
    {
        "group": "G8",
        "section_title": "Results 4.3 Tool documentation",
        "page_range": "13-15",
        "scan_note": (
            "Documentation-stage RDMAP: FAIMS ground-truth design, stage method, service "
            "assessment, work-with-grain principle, orthogonal check (p14/p15 clip noted on "
            "M028), manual checks, slop re-assessment, and five prompt/assessment protocols. "
            "Binary-failure-mode narrative and spawning events are evidence, not RDMAP."
        ),
    },
    research_designs=designs,
    methods=methods,
    protocols=protocols,
)
