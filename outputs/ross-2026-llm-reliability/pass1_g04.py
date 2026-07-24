#!/usr/bin/env python3
"""Pass 1, Group G4: Methods 3 intro + 3.1 'The 2025 phase: systematic evaluation' (pp. 6-8, ~970 words).

Procedure descriptions are left for Pass 3 (RDMAP); here we capture observations
(evidence) and the study's assertions (claims).
"""

from pass1_lib import save_group

EVIDENCE = [
    {
        "evidence_id": "E046",
        "evidence_text": "The case study covers February 2025 to mid-2026: primary domain-research phase (February–July 2025), systematic verification during manuscript preparation (November–December 2025), and a secondary episode during preparation of this paper (April–June 2026).",
        "evidence_type": "study_scope_summary",
        "verbatim_quote": "This case study examines LLM-assisted research conducted between February 2025 and mid-2026: a primary phase of domain research (February–July 2025), systematic verification of its outputs during manuscript preparation (November–December 2025), and a secondary episode arising during the preparation of this paper (April–June 2026).",
        "location": {"section": "3 Methods", "page": 6},
        "supports_claims": ["C069"],
        "notes": "Borderline project_metadata; retained liberally.",
        "extraction_confidence": "medium"
    },
    {
        "evidence_id": "E047",
        "evidence_text": "The software-longevity project, conceived in the mid-2010s, stalled for lack of research assistance; the authors had completed discovery/documentation/evidence collection for a handful of tools but could not scale without assistance.",
        "evidence_type": "observation",
        "verbatim_quote": "This project, originally conceived in the mid-2010s, had stalled due to a lack of research assistance needed to locate, describe, and find lifecycle evidence for the software. We had worked through this tool discovery, tool documentation, and evidence collection process for a handful of tools, but could not scale it without assistance.",
        "location": {"section": "3.1 The 2025 phase: systematic evaluation", "page": 6},
        "supports_claims": ["C034", "C027"],
        "notes": "Expands E024 (Background revival statement); Pass 2 may consolidate."
    },
    {
        "evidence_id": "E048",
        "evidence_text": "Prompts were saved and reflections recorded during the work; session transcripts were later bulk-exported where possible to create a more comprehensive record (Supplement A).",
        "evidence_type": "observation",
        "verbatim_quote": "During this process, we also saved prompts and recorded our reflections on the work. Later, we bulk-exported session transcripts where possible to create a more comprehensive record (see Supplement A).",
        "location": {"section": "3.1 The 2025 phase: systematic evaluation", "page": 7},
        "supports_claims": ["C078"],
        "notes": "Preceding sentence about spreadsheet logging spans the p6/p7 page break and is not quoted; content verifiable against the PDF."
    },
    {
        "evidence_id": "E049",
        "evidence_text": "The authors' practice began as trial-and-error assembly of long prompts, working from circulating practitioner principles (e.g., on Substack) without knowledge of the information-science literature the paper now engages.",
        "evidence_type": "observation",
        "verbatim_quote": "Our practice began as trial-and-error assembly of long prompts that the literature identifies as brittle (Section 2.3): we worked empirically from practitioner principles and techniques then circulating (e.g., on Substack), without knowledge of the information-science literature this paper now engages.",
        "location": {"section": "3.1 The 2025 phase: systematic evaluation", "page": 7},
        "supports_claims": ["C072"],
        "notes": "Reflexive starting-point observation; relevant to the knack-to-method trajectory."
    },
    {
        "evidence_id": "E050",
        "evidence_text": "Initial outputs were checked comprehensively until prompt performance was acceptable, then informally spot-checked; tool discoveries and basic metadata were compared to the open-archaeo curated GitHub source where possible.",
        "evidence_type": "observation",
        "verbatim_quote": "During the initial research, outputs (including on these familiar targets) were first checked comprehensively until prompts evolved to the point where performance was acceptable, and then we switched to informal spot-checks. Tool discoveries and basic metadata were compared to an external curated source (the open-archaeo project on GitHub) where possible.",
        "location": {"section": "3.1 The 2025 phase: systematic evaluation", "page": 7},
        "supports_claims": ["C071"],
        "notes": "First verification wave ('Verification proceeded in two waves.' immediately precedes)."
    },
    {
        "evidence_id": "E051",
        "evidence_text": "The literature search showed persistent errors and received stricter treatment: manual item-by-item verification of every AI-supplied bibliographic reference, each item's disposition tagged in a shared Zotero library, never falling back to spot-checks.",
        "evidence_type": "observation",
        "verbatim_quote": "The literature search received stricter treatment due to persistent errors: we undertook a manual, item-by-item verification of every AI-supplied bibliographic reference and tagged each item's disposition in a shared Zotero library, never falling back to spot-checks.",
        "location": {"section": "3.1 The 2025 phase: systematic evaluation", "page": 7},
        "supports_claims": ["C071"],
        "notes": "Documents both persistent literature-search errors and the strict verification response."
    },
    {
        "evidence_id": "E052",
        "evidence_text": "Meta-prompting (enlisting models to draft, critique, and reword prompts) cut both ways: it could propagate a flaw as readily as repair one.",
        "evidence_type": "observation",
        "verbatim_quote": "The practice cut both ways: it could propagate a flaw as readily as repair one.",
        "location": {"section": "3.1 The 2025 phase: systematic evaluation", "page": 7},
        "supports_claims": ["C042"],
        "notes": "Behavioural observation on model-assisted prompt revision."
    },
    {
        "evidence_id": "E053",
        "evidence_text": "Asked for a snapshot of current state, models would often provide a history instead; dedicated fields (tool-history, technical-implementation, AI-notes/AI-tags) 'domesticated' tendencies that could not be suppressed.",
        "evidence_type": "observation",
        "verbatim_quote": "Asked for a snapshot of the current state, for example, models would often provide a history instead; a tool-history field 'domesticated' this tendency, with a technical-implementation field and AI-notes/AI-tags fields playing similar roles for implementation detail and commentary.",
        "location": {"section": "3.1 The 2025 phase: systematic evaluation", "page": 7},
        "supports_claims": ["C072"],
        "notes": "Model-behaviour observation grounding the guardrail/redirection technique."
    },
    {
        "evidence_id": "E054",
        "evidence_text": "Prompts evolved from open-ended research-assistant scripts to tightly templated, format-checked data-entry instruments (prompt lineage in Supplement A).",
        "evidence_type": "observation",
        "verbatim_quote": "In short, prompts evolved from open-ended research-assistant scripts to tightly templated, format-checked data-entry instruments (see Supplement A for the prompt lineage).",
        "location": {"section": "3.1 The 2025 phase: systematic evaluation", "page": 7},
        "supports_claims": ["C072", "C011"],
        "notes": ""
    },
    {
        "evidence_id": "E055",
        "evidence_text": "In November–December 2025, after discovering inconsistencies between phase outputs (tool discovery vs tool documentation), the authors audited tool discovery and tool evidence outputs exhaustively, switching harness to Claude Code with primarily Claude Opus 4.5.",
        "evidence_type": "observation",
        "verbatim_quote": "Later (November–December 2025), upon discovering inconsistencies between phase outputs (e.g., tool discovery versus tool documentation), we audited tool discovery and tool evidence outputs exhaustively. At this time we switched harness to Claude Code and used the best available model (primarily Claude Opus 4.5).",
        "location": {"section": "3.1 The 2025 phase: systematic evaluation", "page": 7},
        "supports_claims": ["C069"],
        "notes": "Second verification wave trigger and tooling."
    },
    {
        "evidence_id": "E056",
        "evidence_text": "Evidence-events were at greater scale with no ready-made external source equivalent to open-archaeo, so they were LLM-reviewed against a documented three-point workflow (source exists; mentions the tool; stated year matches).",
        "evidence_type": "observation",
        "verbatim_quote": "Since the scale of evidence-events was greater and no ready-made external source equivalent to open-archaeo was available, evidence-events were LLM-reviewed against a documented three-point workflow (the source exists; it mentions the tool; the stated year matches).",
        "location": {"section": "3.1 The 2025 phase: systematic evaluation", "page": 8},
        "supports_claims": ["C069"],
        "notes": "Documents the constraint (no curated external source) shaping the verification design."
    },
    {
        "evidence_id": "E057",
        "evidence_text": "Across the stages, verification yielded some two thousand discrete, verifiable outcomes (tool exists or not; reference resolves or not; stated year matches or not); per-tool results in Supplement A.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "Across the stages this yielded some two thousand discrete, verifiable outcomes: a tool exists or does not, a reference resolves or does not, a stated year matches or does not. Per-tool results appear in Supplement A.",
        "location": {"section": "3.1 The 2025 phase: systematic evaluation", "page": 8},
        "supports_claims": ["C069", "C014"],
        "notes": "Scale of the verified-outcome evidence base."
    },
    {
        "evidence_id": "E058",
        "evidence_text": "Candidate services were selected for commercial availability and task fit, then narrowed by progressive elimination as fundamental limitations emerged.",
        "evidence_type": "observation",
        "verbatim_quote": "Candidate services were selected for commercial availability and task fit, then narrowed by progressive elimination as fundamental limitations emerged; Section 4 details what was deployed at each stage.",
        "location": {"section": "3.1 The 2025 phase: systematic evaluation", "page": 6},
        "supports_claims": ["C070"],
        "notes": "Selection/elimination observation; the eliminations themselves are detailed in Results."
    },
]

CLAIMS = [
    {
        "claim_id": "C069",
        "claim_text": "Failure modes persist across models and harnesses, and reliability must be engineered into the human–AI system; the primary phase illustrates the argument in depth while the secondary episode indicates persistence.",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "We argue that failure modes persist across models and harnesses, and that reliability must be engineered into the human–AI system; the primary phase illustrates our argument in depth, while the secondary episode indicates persistence of the characteristics.",
        "location": {"section": "3 Methods", "page": 6},
        "supported_by": ["E046", "E055", "E056", "E057"],
        "supports_claims": ["C016", "C019"],
        "notes": "States the evidential division of labour between the two episodes; restates the thesis (Pass 2 consolidation candidate)."
    },
    {
        "claim_id": "C070",
        "claim_text": "The evaluation prioritised what matters to working researchers: whether these systems make research 'faster', 'better', or neither.",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "verbatim_quote": "The evaluation prioritised what matters to working researchers: whether these systems make research 'faster', 'better', or neither.",
        "location": {"section": "3.1 The 2025 phase: systematic evaluation", "page": 6},
        "supported_by": [],
        "supports_claims": [],
        "notes": "Evaluation-framing claim."
    },
    {
        "claim_id": "C071",
        "claim_text": "Because the discovery/documentation/evidence outputs would serve as a research dataset, they had to be correct.",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "verbatim_quote": "Because the results from tool discovery, documentation, and evidence collection would serve as a research dataset, they had to be correct.",
        "location": {"section": "3.1 The 2025 phase: systematic evaluation", "page": 7},
        "supported_by": [],
        "supports_claims": ["C069"],
        "notes": "Justifies the verification investment."
    },
    {
        "claim_id": "C072",
        "claim_text": "Iterative prompt revision to mitigate failures converged on techniques groupable as decomposition, templating, and guardrails.",
        "claim_type": "empirical",
        "claim_role": "intermediate",
        "verbatim_quote": "We iteratively revised prompts to mitigate failures and improve quality, converging on techniques that can be grouped into decomposition, templating, and guardrails.",
        "location": {"section": "3.1 The 2025 phase: systematic evaluation", "page": 7},
        "supported_by": ["E049", "E053", "E054"],
        "supports_claims": ["C011", "C015"],
        "notes": "The three technique families mirror the scaffolding framework of Section 2.3."
    },
]

IMPLICIT_ARGUMENTS = [
    {
        "implicit_argument_id": "IA009",
        "argument_text": "The binary verification checks chosen (tool exists; source mentions tool; stated year matches; reference resolves) adequately proxy the correctness of the outputs overall — errors that evade these checks (subtler misrepresentation, selective omission) are not material to the reliability findings.",
        "type": "methodological_assumption",
        "trigger_text": [
            "Every discovery event was manually reviewed under a verification protocol (tool exists, tool is mentioned in source, tool definition met).",
            "Across the stages this yielded some two thousand discrete, verifiable outcomes: a tool exists or does not, a reference resolves or does not, a stated year matches or does not."
        ],
        "trigger_locations": [
            {"section": "3.1 The 2025 phase: systematic evaluation", "page": 7},
            {"section": "3.1 The 2025 phase: systematic evaluation", "page": 8}
        ],
        "inference_reasoning": "The persistence findings are quantified over discrete binary outcomes. Treating these as the measure of reliability assumes the chosen checkable properties capture the error space that matters for the dataset's research use; error types not expressible as these binaries would be invisible to the count.",
        "supports_claims": ["C069", "C014"],
        "assessment_implications": "Affects construct validity of the two-thousand-outcomes evidence base: the failure-mode taxonomy is bounded by what the verification protocol could see."
    },
]

save_group(
    {
        "group": "G4",
        "section_title": "Methods 3 (intro) + 3.1 The 2025 phase: systematic evaluation",
        "page_range": "6-8",
        "estimated_words": 970,
        "natural_boundary": "Before '3.2 The 2026 phase: incidental re-application' heading (p. 8)",
        "split_rationale": "Methods intro plus the 2025-phase subsection; under 1,500-word cap. Decomposition/Templating/Guardrails procedure paragraphs deferred to Pass 3 (RDMAP)."
    },
    evidence=EVIDENCE,
    claims=CLAIMS,
    implicit_arguments=IMPLICIT_ARGUMENTS,
)
