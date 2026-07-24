#!/usr/bin/env python3
"""Pass 3 (explicit RDMAP) — G4: Methods 3 (intro) + 3.1 The 2025 phase (pp. 6-8).

Densest RDMAP group: the case-study arc, 2025-phase designs, verification
methods (two waves), prompt-engineering methods, and the decomposition/
templating/guardrails and verification protocols.

Two page-break clips (Session B precedent, noted on items): the run-logging
sentence spans pp. 6-7 and the LLM confabulation-check sentence spans pp. 7-8.
"""

from rdmap_lib import save_group

designs = [
    {
        "design_id": "RD011",
        "design_text": (
            "Case-study temporal scope: LLM-assisted research February 2025 to mid-2026, "
            "structured as a primary phase of domain research (Feb-Jul 2025), systematic "
            "verification during manuscript preparation (Nov-Dec 2025), and a secondary episode "
            "during preparation of this paper (Apr-Jun 2026)."
        ),
        "design_type": "scope_definition",
        "design_status": "explicit",
        "verbatim_quote": (
            "This case study examines LLM-assisted research conducted between February 2025 and "
            "mid-2026: a primary phase of domain research (February–July 2025), systematic "
            "verification of its outputs during manuscript preparation (November–December 2025), "
            "and a secondary episode arising during the preparation of this paper (April–June "
            "2026)."
        ),
        "location": {"section": "Methods", "page": 6},
        "expected_information_missing": [],
    },
    {
        "design_id": "RD012",
        "design_text": (
            "Argument-role design: the primary phase illustrates the argument in depth while the "
            "secondary episode indicates persistence — supporting the claims that failure modes "
            "persist across models and harnesses and that reliability must be engineered into "
            "the human-AI system."
        ),
        "design_type": "research_question",
        "design_status": "explicit",
        "verbatim_quote": (
            "We argue that failure modes persist across models and harnesses, and that "
            "reliability must be engineered into the human–AI system; the primary phase "
            "illustrates our argument in depth, while the secondary episode indicates "
            "persistence of the characteristics."
        ),
        "location": {"section": "Methods", "page": 6},
        "expected_information_missing": [],
    },
    {
        "design_id": "RD013",
        "design_text": (
            "Host-study revival design: LLMs adopted as research assistants to revive a stalled "
            "mid-2010s study of longevity and succession in archaeological research software — "
            "for tool discovery, documentation, and evidence collection, plus literature review, "
            "ideation, and writing support — because the process could not be scaled without "
            "assistance."
        ),
        "design_type": "study_design",
        "design_status": "explicit",
        "verbatim_quote": (
            "This project, originally conceived in the mid-2010s, had stalled due to a lack of "
            "research assistance needed to locate, describe, and find lifecycle evidence for the "
            "software. We had worked through this tool discovery, tool documentation, and "
            "evidence collection process for a handful of tools, but could not scale it without "
            "assistance. In early 2025, we turned to LLMs as research assistants for these "
            "tasks, plus literature review and ideation and writing support, to see if we could "
            "revive the project."
        ),
        "location": {"section": "Methods", "subsection": "3.1 The 2025 phase", "page": 6},
        "expected_information_missing": [],
    },
    {
        "design_id": "RD014",
        "design_text": (
            "Embedded evaluation design: LLM performance, failures, and mitigations were "
            "evaluated while the disciplinary research was underway, prioritising what matters "
            "to working researchers — whether these systems make research 'faster', 'better', "
            "or neither."
        ),
        "design_type": "study_design",
        "design_status": "explicit",
        "verbatim_quote": (
            "While this disciplinary research was underway, we evaluated LLM performance, "
            "failures, and mitigations. The evaluation prioritised what matters to working "
            "researchers: whether these systems make research 'faster', 'better', or neither."
        ),
        "location": {"section": "Methods", "subsection": "3.1 The 2025 phase", "page": 6},
        "expected_information_missing": [
            "'Faster' and 'better' are not operationalised as measurable criteria",
        ],
    },
    {
        "design_id": "RD015",
        "design_text": (
            "Service-selection design: candidate services selected for commercial availability "
            "and task fit, then narrowed by progressive elimination as fundamental limitations "
            "emerged."
        ),
        "design_type": "scope_definition",
        "design_status": "explicit",
        "verbatim_quote": (
            "Candidate services were selected for commercial availability and task fit, then "
            "narrowed by progressive elimination as fundamental limitations emerged; Section 4 "
            "details what was deployed at each stage."
        ),
        "location": {"section": "Methods", "subsection": "3.1 The 2025 phase", "page": 6},
        "expected_information_missing": [
            "Initial candidate pool and the task-fit criteria are not enumerated in Methods",
        ],
    },
    {
        "design_id": "RD016",
        "design_text": (
            "Correctness requirement driving the verification regime: because tool discovery, "
            "documentation, and evidence-collection outputs would serve as a research dataset, "
            "they had to be correct; verification was therefore designed in two waves."
        ),
        "design_type": "study_design",
        "design_status": "explicit",
        "verbatim_quote": (
            "Because the results from tool discovery, documentation, and evidence collection "
            "would serve as a research dataset, they had to be correct. Verification proceeded "
            "in two waves."
        ),
        "location": {"section": "Methods", "subsection": "3.1 The 2025 phase", "page": 7},
        "expected_information_missing": [],
    },
]

methods = [
    {
        "method_id": "M002",
        "method_text": (
            "Web-interface deployment with prompts as the empirical instrument: work conducted "
            "in the services' web interfaces, with prompts backed by user customisation."
        ),
        "method_type": "data_collection",
        "method_status": "explicit",
        "verbatim_quote": (
            "The work was conducted in the services' web interfaces. Prompts, backed by user "
            "customisation, were the empirical instrument."
        ),
        "location": {"section": "Methods", "subsection": "3.1 The 2025 phase", "page": 6},
        "implements_designs": ["RD013", "RD014"],
        "expected_information_missing": [
            "User-customisation settings (system instructions) are not reproduced in the Methods section",
        ],
    },
    {
        "method_id": "M003",
        "method_text": (
            "Contemporaneous documentation: run outcomes logged in spreadsheets and notes at "
            "the time of execution; prompts saved and reflections recorded during the process. "
            "(The sentence 'Run outcomes were logged in spreadsheets and notes at the time of "
            "execution' spans the p6/p7 page break; the quote is clipped to the p7 sentences.)"
        ),
        "method_type": "data_collection",
        "method_status": "explicit",
        "verbatim_quote": (
            "During this process, we also saved prompts and recorded our reflections on the "
            "work."
        ),
        "location": {"section": "Methods", "subsection": "3.1 The 2025 phase", "page": 7},
        "implements_designs": ["RD011"],
        "expected_information_missing": [
            "Spreadsheet structure and logging fields are not specified",
        ],
    },
    {
        "method_id": "M004",
        "method_text": (
            "Retrospective record consolidation: session transcripts bulk-exported where "
            "possible to create a more comprehensive record (detailed in Supplement A)."
        ),
        "method_type": "data_collection",
        "method_status": "explicit",
        "verbatim_quote": (
            "Later, we bulk-exported session transcripts where possible to create a more "
            "comprehensive record (see Supplement A)."
        ),
        "location": {"section": "Methods", "subsection": "3.1 The 2025 phase", "page": 7},
        "implements_designs": ["RD011"],
        "expected_information_missing": [
            "Export mechanism and coverage criteria ('where possible') are not specified in Methods",
        ],
    },
    {
        "method_id": "M005",
        "method_text": (
            "Two-wave verification structure: initial verification during the research (wave 1) "
            "followed by systematic audit during manuscript preparation (wave 2)."
        ),
        "method_type": "validation",
        "method_status": "explicit",
        "verbatim_quote": (
            "Because the results from tool discovery, documentation, and evidence collection "
            "would serve as a research dataset, they had to be correct. Verification proceeded "
            "in two waves."
        ),
        "location": {"section": "Methods", "subsection": "3.1 The 2025 phase", "page": 7},
        "implements_designs": ["RD016"],
        "expected_information_missing": [],
    },
    {
        "method_id": "M006",
        "method_text": (
            "Comprehensive-then-spot-check verification (wave 1): outputs first checked "
            "comprehensively until prompt performance was acceptable, then switched to informal "
            "spot-checks."
        ),
        "method_type": "quality_control",
        "method_status": "explicit",
        "verbatim_quote": (
            "During the initial research, outputs (including on these familiar targets) were "
            "first checked comprehensively until prompts evolved to the point where performance "
            "was acceptable, and then we switched to informal spot-checks."
        ),
        "location": {"section": "Methods", "subsection": "3.1 The 2025 phase", "page": 7},
        "implements_designs": ["RD016"],
        "expected_information_missing": [
            "Acceptability threshold for switching to spot-checks is not defined",
            "Spot-check sampling rate and procedure are not documented",
        ],
    },
    {
        "method_id": "M007",
        "method_text": (
            "External curated-source comparison: tool discoveries and basic metadata compared "
            "against the open-archaeo project on GitHub where possible."
        ),
        "method_type": "validation",
        "method_status": "explicit",
        "verbatim_quote": (
            "Tool discoveries and basic metadata were compared to an external curated source "
            "(the open-archaeo project on GitHub) where possible."
        ),
        "location": {"section": "Methods", "subsection": "3.1 The 2025 phase", "page": 7},
        "implements_designs": ["RD016"],
        "expected_information_missing": [
            "Comparison procedure and handling of disagreements are not documented",
        ],
    },
    {
        "method_id": "M008",
        "method_text": (
            "Item-by-item manual verification of the literature search: every AI-supplied "
            "bibliographic reference manually verified and its disposition tagged in a shared "
            "Zotero library, never falling back to spot-checks."
        ),
        "method_type": "validation",
        "method_status": "explicit",
        "verbatim_quote": (
            "The literature search received stricter treatment due to persistent errors: we "
            "undertook a manual, item-by-item verification of every AI-supplied bibliographic "
            "reference and tagged each item's disposition in a shared Zotero library, never "
            "falling back to spot-checks."
        ),
        "location": {"section": "Methods", "subsection": "3.1 The 2025 phase", "page": 7},
        "implements_designs": ["RD016"],
        "expected_information_missing": [
            "Disposition tag vocabulary is not enumerated in the Methods section",
        ],
    },
    {
        "method_id": "M009",
        "method_text": (
            "Iterative prompt revision: prompts revised iteratively to mitigate failures and "
            "improve quality, converging on techniques grouped as decomposition, templating, "
            "and guardrails."
        ),
        "method_type": "analysis",
        "method_status": "explicit",
        "verbatim_quote": (
            "We iteratively revised prompts to mitigate failures and improve quality, "
            "converging on techniques that can be grouped into decomposition, templating, and "
            "guardrails."
        ),
        "location": {"section": "Methods", "subsection": "3.1 The 2025 phase", "page": 7},
        "implements_designs": ["RD014"],
        "expected_information_missing": [
            "Revision trigger criteria (what counted as a failure requiring revision) are not stated",
        ],
    },
    {
        "method_id": "M010",
        "method_text": (
            "Meta-prompting: models enlisted to draft, critique, and reword prompts and to "
            "suggest task-definition reframings, with the recognised risk that the practice "
            "could propagate flaws as readily as repair them."
        ),
        "method_type": "analysis",
        "method_status": "explicit",
        "verbatim_quote": (
            "In revising, we routinely enlisted the models themselves, asking them to draft, "
            "critique, and reword prompts, and even to suggest how a task definition might be "
            "reframed so the model could apply it more reliably (meta-prompting). The practice "
            "cut both ways: it could propagate a flaw as readily as repair one."
        ),
        "location": {"section": "Methods", "subsection": "3.1 The 2025 phase", "page": 7},
        "implements_designs": ["RD014"],
        "expected_information_missing": [],
    },
    {
        "method_id": "M011",
        "method_text": (
            "Exhaustive audit (wave 2, Nov-Dec 2025): tool discovery and tool evidence outputs "
            "audited exhaustively after inconsistencies were discovered between phase outputs, "
            "using the Claude Code harness with primarily Claude Opus 4.5."
        ),
        "method_type": "validation",
        "method_status": "explicit",
        "verbatim_quote": (
            "Later (November–December 2025), upon discovering inconsistencies between phase "
            "outputs (e.g., tool discovery versus tool documentation), we audited tool "
            "discovery and tool evidence outputs exhaustively. At this time we switched harness "
            "to Claude Code and used the best available model (primarily Claude Opus 4.5)."
        ),
        "location": {"section": "Methods", "subsection": "3.1 The 2025 phase", "page": 7},
        "implements_designs": ["RD016"],
        "expected_information_missing": [
            "How the phase-output inconsistencies were detected is not described",
        ],
    },
    {
        "method_id": "M012",
        "method_text": (
            "LLM-review of evidence events at scale: because no ready-made external source "
            "equivalent to open-archaeo existed for evidence events, they were LLM-reviewed "
            "against a documented three-point workflow, with informal manual spot-checks in all "
            "cases."
        ),
        "method_type": "validation",
        "method_status": "explicit",
        "verbatim_quote": (
            "Since the scale of evidence-events was greater and no ready-made external source "
            "equivalent to open-archaeo was available, evidence-events were LLM-reviewed "
            "against a documented three-point workflow (the source exists; it mentions the "
            "tool; the stated year matches). In all cases informal manual spot-checks were "
            "performed."
        ),
        "location": {"section": "Methods", "subsection": "3.1 The 2025 phase", "page": 8},
        "implements_designs": ["RD016"],
        "expected_information_missing": [
            "Spot-check sampling procedure is not documented",
        ],
    },
    {
        "method_id": "M013",
        "method_text": (
            "Familiar-target grounding: initial runs focused on sources and tools known "
            "first-hand, including software the authors had built, enabling direct accuracy "
            "assessment."
        ),
        "method_type": "validation",
        "method_status": "explicit",
        "verbatim_quote": (
            "Initial runs were focused on sources and tools we knew first-hand, including "
            "software we had built."
        ),
        "location": {"section": "Methods", "subsection": "3.1 The 2025 phase", "page": 7},
        "implements_designs": ["RD016"],
        "expected_information_missing": [],
    },
]

protocols = [
    {
        "protocol_id": "P001",
        "protocol_text": (
            "Decomposition protocol: compound prompts decomposed into tightly scoped tasks "
            "(e.g., separating tool discovery from documentation and evidence collection); "
            "limited iterations per prompt (up to five journal issues; a single tool's "
            "metadata); each task undertaken in a new chat with fresh context."
        ),
        "protocol_type": "task_structuring",
        "protocol_status": "explicit",
        "verbatim_quote": (
            "Compound prompts were decomposed into tightly scoped tasks (e.g., separating tool "
            "discovery from documentation and evidence collection), limited iterations of a "
            "task were undertaken per prompt (examine up to five issues of a journal; find "
            "metadata about a single tool), and each task was undertaken in a new chat with "
            "fresh context."
        ),
        "location": {"section": "Methods", "subsection": "3.1 The 2025 phase", "page": 7},
        "implements_methods": ["M009"],
        "expected_information_missing": [],
    },
    {
        "protocol_id": "P002",
        "protocol_text": (
            "Templating protocol: output template specifying quoted CSV inside a fenced code "
            "block, named column schemas, controlled vocabularies, date formats, "
            "row-granularity rules, and a self-check of column counts against the header row."
        ),
        "protocol_type": "output_constraint",
        "protocol_status": "explicit",
        "verbatim_quote": (
            "An output template specified quoted CSV inside a fenced code block, with named "
            "column schemas and controlled vocabularies, date formats, and row-granularity "
            "rules, plus a self-check of column counts against the header row."
        ),
        "location": {"section": "Methods", "subsection": "3.1 The 2025 phase", "page": 7},
        "implements_methods": ["M009"],
        "expected_information_missing": [
            "The controlled vocabularies themselves are not reproduced in the Methods section",
        ],
    },
    {
        "protocol_id": "P003",
        "protocol_text": (
            "Guardrails protocol: prompt constraints prohibiting conjecture, extrapolation, and "
            "synthesis; unsuppressible tendencies redirected into dedicated fields "
            "(tool-history, technical-implementation, AI-notes/AI-tags); plus a tool definition "
            "with inclusion-exclusion rubric, source-quality hierarchy, readback confirmation, "
            "thoroughness-over-speed directive, and an explicit uncertainty field."
        ),
        "protocol_type": "output_constraint",
        "protocol_status": "explicit",
        "verbatim_quote": (
            "Constraints built into the prompt prohibited conjecture, extrapolation, and "
            "synthesis, while tendencies that could not be suppressed were redirected into "
            "dedicated fields. Asked for a snapshot of the current state, for example, models "
            "would often provide a history instead; a tool-history field 'domesticated' this "
            "tendency, with a technical-implementation field and AI-notes/AI-tags fields "
            "playing similar roles for implementation detail and commentary. Quality was "
            "further encouraged by providing a tool definition with an inclusion-exclusion "
            "rubric, a source-quality hierarchy, a readback confirmation of the task, a "
            "thoroughness-over-speed directive, and an explicit uncertainty field."
        ),
        "location": {"section": "Methods", "subsection": "3.1 The 2025 phase", "page": 7},
        "implements_methods": ["M009"],
        "expected_information_missing": [
            "The inclusion-exclusion rubric and source-quality hierarchy contents are not reproduced in Methods (prompt lineage in Supplement A.3)",
        ],
    },
    {
        "protocol_id": "P004",
        "protocol_text": (
            "Discovery-event verification protocol (Nov-Dec 2025 audit): every discovery event "
            "manually reviewed against three criteria — tool exists, tool is mentioned in "
            "source, tool definition met."
        ),
        "protocol_type": "verification",
        "protocol_status": "explicit",
        "verbatim_quote": (
            "Every discovery event was manually reviewed under a verification protocol (tool "
            "exists, tool is mentioned in source, tool definition met)."
        ),
        "location": {"section": "Methods", "subsection": "3.1 The 2025 phase", "page": 7},
        "implements_methods": ["M011"],
        "expected_information_missing": [],
    },
    {
        "protocol_id": "P005",
        "protocol_text": (
            "LLM-based confabulation-check protocol: where a confabulation was suspected, tool "
            "existence checked against the cited links, GitHub, GitLab, CRAN, PyPI, and a "
            "general web search, with an evidence report indicating which sources were checked "
            "and the outcome. (The sentence spans the p7/p8 page break; the quote is clipped at "
            "the break — it completes 'and the outcome' on p. 8.)"
        ),
        "protocol_type": "verification",
        "protocol_status": "explicit",
        "verbatim_quote": (
            "If a confabulation was suspected, we implemented an additional LLM-based "
            "verification, where the existence of the tool was checked against the cited links, "
            "GitHub, GitLab, CRAN, PyPI, and a general web search, with an evidence report "
            "indicating which sources were checked"
        ),
        "location": {"section": "Methods", "subsection": "3.1 The 2025 phase", "page": 7},
        "implements_methods": ["M011"],
        "expected_information_missing": [
            "Prompt used for the LLM-based verification is not reproduced",
        ],
    },
    {
        "protocol_id": "P006",
        "protocol_text": (
            "Evidence-event three-point verification workflow: for each evidence event, check "
            "that the source exists, that it mentions the tool, and that the stated year "
            "matches."
        ),
        "protocol_type": "verification",
        "protocol_status": "explicit",
        "verbatim_quote": (
            "Since the scale of evidence-events was greater and no ready-made external source "
            "equivalent to open-archaeo was available, evidence-events were LLM-reviewed "
            "against a documented three-point workflow (the source exists; it mentions the "
            "tool; the stated year matches)."
        ),
        "location": {"section": "Methods", "subsection": "3.1 The 2025 phase", "page": 8},
        "implements_methods": ["M012"],
        "expected_information_missing": [],
    },
    {
        "protocol_id": "P007",
        "protocol_text": (
            "Zotero disposition-tagging protocol: each verified bibliographic item's "
            "disposition recorded as a tag in a shared Zotero library."
        ),
        "protocol_type": "recording",
        "protocol_status": "explicit",
        "verbatim_quote": (
            "The literature search received stricter treatment due to persistent errors: we "
            "undertook a manual, item-by-item verification of every AI-supplied bibliographic "
            "reference and tagged each item's disposition in a shared Zotero library, never "
            "falling back to spot-checks."
        ),
        "location": {"section": "Methods", "subsection": "3.1 The 2025 phase", "page": 7},
        "implements_methods": ["M008"],
        "expected_information_missing": [
            "Disposition tag vocabulary is not enumerated",
        ],
    },
]

save_group(
    {
        "group": "G4",
        "section_title": "Methods 3 (intro) + 3.1 The 2025 phase: systematic evaluation",
        "page_range": "6-8",
        "scan_note": (
            "Densest RDMAP group as expected: 6 designs, 12 methods, 7 protocols. Two "
            "page-break-spanning sentences handled by clipping (M003 p6/p7; P005 p7/p8), noted "
            "on the items. The 'prompts evolved from open-ended scripts to templated "
            "data-entry instruments' summary sentence treated as context for M009 rather than "
            "a separate item."
        ),
    },
    research_designs=designs,
    methods=methods,
    protocols=protocols,
)
