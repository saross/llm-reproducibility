#!/usr/bin/env python3
"""Pass 1, Group G5: Methods 3.2 'The 2026 phase: incidental re-application' + 3.3 Reflexivity (pp. 8-9, ~500 words)."""

from pass1_lib import save_group

EVIDENCE = [
    {
        "evidence_id": "E059",
        "evidence_text": "In April 2026, one author built lit-scout, a Claude Code agent for systematic literature discovery, as a training exercise for an unrelated project.",
        "evidence_type": "observation",
        "verbatim_quote": "In April 2026, one of us built lit-scout, a Claude Code agent for systematic literature discovery, as a training exercise in preparation for an unrelated project.",
        "location": {"section": "3.2 The 2026 phase: incidental re-application", "page": 8},
        "supports_claims": ["C073"],
        "notes": ""
    },
    {
        "evidence_id": "E060",
        "evidence_text": "The agent's first opportunistic test run (Claude Opus 4.6) was this paper's search of information-science literature on LLM output verification.",
        "evidence_type": "observation",
        "verbatim_quote": "The agent's first opportunistic test run (using Claude Opus 4.6) was this paper's search of information-science literature related to LLM output verification.",
        "location": {"section": "3.2 The 2026 phase: incidental re-application", "page": 8},
        "supports_claims": ["C073"],
        "notes": ""
    },
    {
        "evidence_id": "E061",
        "evidence_text": "The 2026 instrument was a declaratively defined agent paired with a tested helper script (lit-search.py) wrapping the CrossRef, Semantic Scholar, and OpenAlex APIs to ground output.",
        "evidence_type": "observation",
        "verbatim_quote": "Instead of prompts pasted into a web interface, the instrument was now a declaratively defined agent, paired with a tested helper script (lit-search.py) wrapping the application programming interfaces (APIs) of three bibliographic registries (CrossRef, Semantic Scholar, and OpenAlex) to ground its output.",
        "location": {"section": "3.2 The 2026 phase: incidental re-application", "page": 8},
        "supports_claims": ["C074", "C019"],
        "notes": "Documents the instrument change between episodes."
    },
    {
        "evidence_id": "E062",
        "evidence_text": "The agent was iteratively refined with verification runs and literature-review use through June 2026, maturing into a proposer-verifier agent pair.",
        "evidence_type": "observation",
        "verbatim_quote": "Like the earlier prompts, this agent was iteratively refined, with verification runs and literature-review use continuing through June 2026, eventually maturing into a proposer-verifier agent pair.",
        "location": {"section": "3.2 The 2026 phase: incidental re-application", "page": 8},
        "supports_claims": ["C074"],
        "notes": ""
    },
    {
        "evidence_id": "E063",
        "evidence_text": "The 2026 workflow comprises a proposer drafting the discovery report, a verifier auditing it, and a driver skill executed outside both agents' context windows that dispatches each agent and shuttles corrections in a loop until outputs pass.",
        "evidence_type": "observation",
        "verbatim_quote": "The workflow comprises a proposer that drafts the discovery report, a verifier that audits it, and a driver: a reusable skill definition, executed outside both agents' context windows, that dispatches each agent in turn and shuttles corrections from verifier to proposer as needed to iterate in a loop until the outputs pass.",
        "location": {"section": "3.2 The 2026 phase: incidental re-application", "page": 8},
        "supports_claims": ["C074"],
        "notes": "Architecture summary; full specification detail deferred to Pass 3 (RDMAP)."
    },
    {
        "evidence_id": "E064",
        "evidence_text": "Despite the change in implementation, the pattern was familiar: similar errors still occurred and the same families of mitigation were still required.",
        "evidence_type": "observation",
        "verbatim_quote": "Despite the change in implementation, the pattern was familiar: similar errors still occurred, and the same families of mitigation were still required.",
        "location": {"section": "3.2 The 2026 phase: incidental re-application", "page": 8},
        "supports_claims": ["C014", "C015", "C019", "C020"],
        "notes": "Key persistence observation at the methods level."
    },
    {
        "evidence_id": "E065",
        "evidence_text": "Artefacts captured across both phases (transcripts, observations, version histories) form the shared evidence base; a manifest indexes sources per stage including known gaps (for Perplexity, Elicit, and most Gemini runs, tabulated results survive but not conversation transcripts).",
        "evidence_type": "observation",
        "verbatim_quote": "The artefacts captured across both phases (transcripts, observations, and version histories) form the shared evidence base for the claims that follow; a manifest accompanying the archived materials indexes sources for each stage, including known gaps (e.g., for Perplexity, Elicit, and most Gemini runs, tabulated results survive but not conversation transcripts).",
        "location": {"section": "3.3 Reflexivity", "page": 8},
        "supports_claims": ["C078"],
        "notes": "Declares the evidence base and its known gaps."
    },
]

CLAIMS = [
    {
        "claim_id": "C073",
        "claim_text": "The second phase was incidental rather than designed.",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "verbatim_quote": "The second phase was incidental rather than designed.",
        "location": {"section": "3.2 The 2026 phase: incidental re-application", "page": 8},
        "supported_by": ["E059", "E060"],
        "supports_claims": [],
        "notes": "Bears on the epistemic status of the persistence evidence (not a preregistered test)."
    },
    {
        "claim_id": "C074",
        "claim_text": "The 2025 techniques (decomposition, templating, guardrails) reappear in the 2026 agents' specifications.",
        "claim_type": "empirical",
        "claim_role": "intermediate",
        "verbatim_quote": "The 2025 techniques again appear in these agents' specifications.",
        "location": {"section": "3.2 The 2026 phase: incidental re-application", "page": 8},
        "supported_by": ["E061", "E062", "E063"],
        "supports_claims": ["C019", "C020"],
        "notes": ""
    },
    {
        "claim_id": "C075",
        "claim_text": "Registry grounding did not by itself foreclose confabulation.",
        "claim_type": "empirical",
        "claim_role": "core",
        "verbatim_quote": "As Section 4.5 shows, registry grounding did not by itself foreclose confabulation.",
        "location": {"section": "3.2 The 2026 phase: incidental re-application", "page": 8},
        "supported_by": [],
        "supports_claims": ["C014", "C016"],
        "notes": "Core 2026-episode finding, substantiated in Section 4.5 (Results)."
    },
    {
        "claim_id": "C076",
        "claim_text": "The approach is a case study presenting situated depth rather than statistical generalisability.",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "The approach is a case study presenting situated depth rather than statistical generalisability (Flyvbjerg, 2006; Yin, 2018).",
        "location": {"section": "3.3 Reflexivity", "page": 8},
        "supported_by": [],
        "supports_claims": ["C021"],
        "notes": "Methodological self-positioning with citations (Flyvbjerg 2006; Yin 2018); qualifies the scope of the persistence claims."
    },
    {
        "claim_id": "C077",
        "claim_text": "The main risk of extensive LLM use in the research process is that an LLM may fluently and confidently affirm anything proposed to it.",
        "claim_type": "theoretical",
        "claim_role": "supporting",
        "verbatim_quote": "The main risk of such use is that an LLM may fluently and confidently affirm anything proposed to it.",
        "location": {"section": "3.3 Reflexivity", "page": 8},
        "supported_by": [],
        "supports_claims": [],
        "notes": "Motivates the mitigation described in C078."
    },
    {
        "claim_id": "C078",
        "claim_text": "The affirmation risk was mitigated through validation between co-authors and by anchoring every empirical claim to a logged artefact (session transcripts, git history, output spreadsheets).",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "verbatim_quote": "We mitigated this through validation between co-authors and especially by anchoring every empirical claim to a logged artefact (session transcripts, git history, output spreadsheets).",
        "location": {"section": "3.3 Reflexivity", "page": 8},
        "supported_by": ["E048", "E065"],
        "supports_claims": [],
        "notes": ""
    },
    {
        "claim_id": "C079",
        "claim_text": "Because newer models and research tools were released throughout the study, each phase is a snapshot of the capabilities of its moment.",
        "claim_type": "interpretation",
        "claim_role": "supporting",
        "verbatim_quote": "Newer models and research-oriented tools were released throughout the study and during manuscript preparation; each phase is therefore a snapshot of the capabilities of its moment (full release timeline in Supplement A).",
        "location": {"section": "3.3 Reflexivity", "page": 8},
        "supported_by": [],
        "supports_claims": ["C076"],
        "notes": ""
    },
]

IMPLICIT_ARGUMENTS = [
    {
        "implicit_argument_id": "IA010",
        "argument_text": "The logged artefacts (transcripts, git history, spreadsheets) are themselves complete and accurate enough that anchoring claims to them secures those claims — despite acknowledged transcript gaps for several services.",
        "type": "methodological_assumption",
        "trigger_text": [
            "We mitigated this through validation between co-authors and especially by anchoring every empirical claim to a logged artefact (session transcripts, git history, output spreadsheets).",
            "The artefacts captured across both phases (transcripts, observations, and version histories) form the shared evidence base for the claims that follow; a manifest accompanying the archived materials indexes sources for each stage, including known gaps (e.g., for Perplexity, Elicit, and most Gemini runs, tabulated results survive but not conversation transcripts)."
        ],
        "trigger_locations": [
            {"section": "3.3 Reflexivity", "page": 8},
            {"section": "3.3 Reflexivity", "page": 8}
        ],
        "inference_reasoning": "The reflexivity defence treats artefact-anchoring as the guarantee against LLM-affirmation risk, which assumes the artefact record is faithful and sufficiently complete. The paper itself notes transcript gaps for Perplexity, Elicit, and most Gemini runs, so for those stages the anchoring rests on tabulated results alone; the adequacy of that thinner record is assumed.",
        "supports_claims": ["C078"],
        "assessment_implications": "Claims about stages with transcript gaps carry a weaker audit trail than the anchoring principle suggests; assessors should weight per-stage evidence accordingly."
    },
]

save_group(
    {
        "group": "G5",
        "section_title": "Methods 3.2 The 2026 phase + 3.3 Reflexivity",
        "page_range": "8-9",
        "estimated_words": 500,
        "natural_boundary": "Before 'Results' heading (Section 4, p. 9)",
        "split_rationale": "Short group kept separate to respect the natural Methods→Results boundary (merging with G4 would approach the 1,500-word cap)."
    },
    evidence=EVIDENCE,
    claims=CLAIMS,
    implicit_arguments=IMPLICIT_ARGUMENTS,
)
