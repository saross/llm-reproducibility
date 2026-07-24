#!/usr/bin/env python3
"""Pass 3 (explicit RDMAP) — G5: Methods 3.2 The 2026 phase + 3.3 Reflexivity (pp. 8-9).

The 2026 agent instrument (lit-scout, proposer-verifier pair, driver skill) and
the case-study/reflexivity designs.
"""

from rdmap_lib import save_group

designs = [
    {
        "design_id": "RD017",
        "design_text": (
            "Incidental second-phase design: the 2026 phase was incidental rather than "
            "designed — lit-scout was built as a training exercise for an unrelated project, "
            "and its first opportunistic test run (Claude Opus 4.6) was this paper's "
            "information-science literature search."
        ),
        "design_type": "study_design",
        "design_status": "explicit",
        "verbatim_quote": (
            "The second phase was incidental rather than designed. In April 2026, one of us "
            "built lit-scout, a Claude Code agent for systematic literature discovery, as a "
            "training exercise in preparation for an unrelated project. The agent's first "
            "opportunistic test run (using Claude Opus 4.6) was this paper's search of "
            "information-science literature related to LLM output verification."
        ),
        "location": {"section": "Methods", "subsection": "3.2 The 2026 phase", "page": 8},
        "expected_information_missing": [],
    },
    {
        "design_id": "RD018",
        "design_text": (
            "Case-study design: situated depth rather than statistical generalisability "
            "(Flyvbjerg 2006; Yin 2018), with the artefacts captured across both phases as the "
            "shared evidence base."
        ),
        "design_type": "study_design",
        "design_status": "explicit",
        "verbatim_quote": (
            "The approach is a case study presenting situated depth rather than statistical "
            "generalisability (Flyvbjerg, 2006; Yin, 2018)."
        ),
        "location": {"section": "Methods", "subsection": "3.3 Reflexivity", "page": 8},
        "expected_information_missing": [],
    },
    {
        "design_id": "RD019",
        "design_text": (
            "Reflexivity/positionality: LLMs were used extensively in the research process "
            "itself; the risk that an LLM may fluently affirm anything proposed to it was "
            "mitigated through validation between co-authors and by anchoring every empirical "
            "claim to a logged artefact (session transcripts, git history, output "
            "spreadsheets)."
        ),
        "design_type": "positionality",
        "design_status": "explicit",
        "verbatim_quote": (
            "LLMs were used extensively in the research process. The main risk of such use is "
            "that an LLM may fluently and confidently affirm anything proposed to it. We "
            "mitigated this through validation between co-authors and especially by anchoring "
            "every empirical claim to a logged artefact (session transcripts, git history, "
            "output spreadsheets)."
        ),
        "location": {"section": "Methods", "subsection": "3.3 Reflexivity", "page": 8},
        "expected_information_missing": [
            "Co-author validation procedure is not described",
        ],
    },
    {
        "design_id": "RD020",
        "design_text": (
            "Snapshot scope framing: because newer models and research tools were released "
            "throughout the study, each phase is treated as a snapshot of the capabilities of "
            "its moment."
        ),
        "design_type": "scope_definition",
        "design_status": "explicit",
        "verbatim_quote": (
            "Newer models and research-oriented tools were released throughout the study and "
            "during manuscript preparation; each phase is therefore a snapshot of the "
            "capabilities of its moment (full release timeline in Supplement A)."
        ),
        "location": {"section": "Methods", "subsection": "3.3 Reflexivity", "page": 8},
        "expected_information_missing": [],
    },
]

methods = [
    {
        "method_id": "M014",
        "method_text": (
            "Registry-grounded agent instrument: a declaratively defined Claude Code agent "
            "(lit-scout) paired with a tested helper script (lit-search.py) wrapping the APIs "
            "of three bibliographic registries (CrossRef, Semantic Scholar, OpenAlex) to "
            "ground its output."
        ),
        "method_type": "data_collection",
        "method_status": "explicit",
        "verbatim_quote": (
            "Instead of prompts pasted into a web interface, the instrument was now a "
            "declaratively defined agent, paired with a tested helper script (lit-search.py) "
            "wrapping the application programming interfaces (APIs) of three bibliographic "
            "registries (CrossRef, Semantic Scholar, and OpenAlex) to ground its output."
        ),
        "location": {"section": "Methods", "subsection": "3.2 The 2026 phase", "page": 8},
        "implements_designs": ["RD017"],
        "expected_information_missing": [
            "Agent definition and helper-script code are referenced but not reproduced in the paper body",
        ],
    },
    {
        "method_id": "M015",
        "method_text": (
            "Iterative agent refinement: the agent was iteratively refined through "
            "verification runs and literature-review use (through June 2026), maturing into a "
            "proposer-verifier agent pair."
        ),
        "method_type": "analysis",
        "method_status": "explicit",
        "verbatim_quote": (
            "Like the earlier prompts, this agent was iteratively refined, with verification "
            "runs and literature-review use continuing through June 2026, eventually maturing "
            "into a proposer-verifier agent pair."
        ),
        "location": {"section": "Methods", "subsection": "3.2 The 2026 phase", "page": 8},
        "implements_designs": ["RD017"],
        "expected_information_missing": [],
    },
    {
        "method_id": "M016",
        "method_text": (
            "Artefact evidence base with manifest: transcripts, observations, and version "
            "histories captured across both phases form the shared evidence base; a manifest "
            "accompanying the archived materials indexes sources per stage, including known "
            "gaps."
        ),
        "method_type": "data_collection",
        "method_status": "explicit",
        "verbatim_quote": (
            "The artefacts captured across both phases (transcripts, observations, and version "
            "histories) form the shared evidence base for the claims that follow; a manifest "
            "accompanying the archived materials indexes sources for each stage, including "
            "known gaps (e.g., for Perplexity, Elicit, and most Gemini runs, tabulated results "
            "survive but not conversation transcripts)."
        ),
        "location": {"section": "Methods", "subsection": "3.3 Reflexivity", "page": 8},
        "implements_designs": ["RD018"],
        "expected_information_missing": [],
    },
    {
        "method_id": "M017",
        "method_text": (
            "Co-author validation and artefact anchoring: empirical claims validated between "
            "co-authors and anchored to logged artefacts (session transcripts, git history, "
            "output spreadsheets) to mitigate LLM affirmation risk."
        ),
        "method_type": "quality_control",
        "method_status": "explicit",
        "verbatim_quote": (
            "We mitigated this through validation between co-authors and especially by "
            "anchoring every empirical claim to a logged artefact (session transcripts, git "
            "history, output spreadsheets)."
        ),
        "location": {"section": "Methods", "subsection": "3.3 Reflexivity", "page": 8},
        "implements_designs": ["RD019"],
        "expected_information_missing": [
            "Anchoring procedure (how claims were traced to artefacts) is not described",
        ],
    },
]

protocols = [
    {
        "protocol_id": "P008",
        "protocol_text": (
            "Driver skill protocol: a reusable skill definition executed outside both agents' "
            "context windows dispatches proposer then verifier in turn, shuttling corrections "
            "from verifier to proposer and iterating in a loop until outputs pass."
        ),
        "protocol_type": "workflow_orchestration",
        "protocol_status": "explicit",
        "verbatim_quote": (
            "The workflow comprises a proposer that drafts the discovery report, a verifier "
            "that audits it, and a driver: a reusable skill definition, executed outside both "
            "agents' context windows, that dispatches each agent in turn and shuttles "
            "corrections from verifier to proposer as needed to iterate in a loop until the "
            "outputs pass."
        ),
        "location": {"section": "Methods", "subsection": "3.2 The 2026 phase", "page": 8},
        "implements_methods": ["M015"],
        "expected_information_missing": [
            "Pass/fail criteria for loop termination are not specified in the Methods section",
        ],
    },
    {
        "protocol_id": "P009",
        "protocol_text": (
            "Proposer agent protocol: discovery decomposed into phases (seed searches across "
            "multiple indices, then backward and forward citation chaining); output templated "
            "as a named-column table plus a machine-readable claims block of granular "
            "verifiable assertions; guardrails prohibit generation from memory — every author, "
            "year, title, and citation count must come from a registry response; unverifiable "
            "attributions flagged; draft carries an explicit verification-pending marker."
        ),
        "protocol_type": "agent_specification",
        "protocol_status": "explicit",
        "verbatim_quote": (
            "The proposer agent decomposes discovery into phases (seed searches across "
            "multiple indices, then backward and forward citation chaining). Its output is "
            "templated as a table with named columns plus a machine-readable claims block that "
            "decomposes the table into granular, verifiable assertions. Its guardrails "
            "prohibit generation from memory: every author, year, title, and citation count "
            "must come from a registry response. Unverifiable attributions are flagged, and "
            "the draft carries an explicit \"verification-pending\" marker."
        ),
        "location": {"section": "Methods", "subsection": "3.2 The 2026 phase", "page": 8},
        "implements_methods": ["M015"],
        "expected_information_missing": [],
    },
    {
        "protocol_id": "P010",
        "protocol_text": (
            "Verifier agent protocol: invoked in a fresh context window; re-queries every DOI "
            "against the same registry APIs, compares each claimed field, and emits an audit "
            "trail of corrections (original table, verification summary, corrected table)."
        ),
        "protocol_type": "verification",
        "protocol_status": "explicit",
        "verbatim_quote": (
            "A verifier agent is then invoked in a fresh context window; this verifier "
            "re-queries every digital object identifier (DOI) against the same registry APIs, "
            "compares each claimed field, and emits an audit trail of corrections (original "
            "table, verification summary, corrected table)."
        ),
        "location": {"section": "Methods", "subsection": "3.2 The 2026 phase", "page": 8},
        "implements_methods": ["M015"],
        "expected_information_missing": [],
    },
    {
        "protocol_id": "P011",
        "protocol_text": (
            "lit-search.py helper-script specification: a tested script wrapping the CrossRef, "
            "Semantic Scholar, and OpenAlex APIs, supplying registry grounding to the agent."
        ),
        "protocol_type": "software_specification",
        "protocol_status": "explicit",
        "verbatim_quote": (
            "Instead of prompts pasted into a web interface, the instrument was now a "
            "declaratively defined agent, paired with a tested helper script (lit-search.py) "
            "wrapping the application programming interfaces (APIs) of three bibliographic "
            "registries (CrossRef, Semantic Scholar, and OpenAlex) to ground its output."
        ),
        "location": {"section": "Methods", "subsection": "3.2 The 2026 phase", "page": 8},
        "implements_methods": ["M014"],
        "expected_information_missing": [
            "Script version, query parameters, and how it was 'tested' are not documented",
        ],
    },
]

save_group(
    {
        "group": "G5",
        "section_title": "Methods 3.2 The 2026 phase + 3.3 Reflexivity",
        "page_range": "8-9",
        "scan_note": (
            "Short group but RDMAP-dense: 2026 instrument methods and agent protocols plus the "
            "case-study, reflexivity, and snapshot designs."
        ),
    },
    research_designs=designs,
    methods=methods,
    protocols=protocols,
)
