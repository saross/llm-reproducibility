#!/usr/bin/env python3
"""Pass 4 (implicit RDMAP) — whole-paper scan (ross-2026-llm-reliability).

Systematic 4-pattern scan (mentioned-undocumented procedures; effects implying
causes; tools without specifications; strategic positioning without statement)
across each tier and all major sections, seeded from the explicit RDMAP of
Pass 3. Every item carries verbatim trigger_text (mechanically verified),
parallel trigger_locations, inference_reasoning, and implicit_metadata.

ID convention: sequential RD###/M###/P### numbering continues from Pass 3 with
*_status="implicit", matching corpus practice (e.g. sobotkova-et-al-2024
P010-P012) rather than the IMP-prefixed IDs suggested by prompt 04; deviation
recorded in extraction_notes by the bookkeeping block below.
"""

import json
from pathlib import Path

from rdmap_lib import EXTRACTION, save_group

designs = [
    {
        "design_id": "RD029",
        "design_text": (
            "Capability-adoption-upon-release strategy: newly released models, research modes, "
            "and harnesses were adopted as they became available (Claude research mode on "
            "release; Claude Code + Opus 4.5 for the audit; Opus 4.6 for the 2026 agent and "
            "slop re-assessment), an operative strategic practice never stated as a design "
            "decision."
        ),
        "design_type": "study_design",
        "design_status": "implicit",
        "trigger_text": [
            "After Anthropic released such a mode, we began using it (see Supplement A for the release and availability timeline).",
            "At this time we switched harness to Claude Code and used the best available model (primarily Claude Opus 4.5).",
            "Newer models and research-oriented tools were released throughout the study and during manuscript preparation",
        ],
        "trigger_locations": [
            {"section": "Results", "subsection": "4 (coverage)", "page": 9},
            {"section": "Methods", "subsection": "3.1 The 2025 phase", "page": 7},
            {"section": "Methods", "subsection": "3.3 Reflexivity", "page": 8},
        ],
        "inference_reasoning": (
            "Across both phases the study repeatedly moved to the newest available capability "
            "(research modes on release, harness switch for the audit, newest model for the "
            "re-assessment). This consistent practice shaped which services were compared at "
            "each stage, yet no section states adoption-on-release as a strategic decision or "
            "discusses its trade-offs (e.g., comparability across stages versus capability)."
        ),
        "implicit_metadata": {
            "basis": "inferred_from_results",
            "transparency_gap": (
                "No stated policy for when/why newer models or harnesses were adopted "
                "mid-study, or how adoption interacts with cross-stage comparability"
            ),
            "assessability_impact": (
                "Readers cannot assess whether stage-to-stage differences reflect task "
                "characteristics or capability drift from rolling adoption"
            ),
            "reconstruction_confidence": "medium",
        },
        "location": {"section": "Methods/Results (multiple)", "page": 7},
        "expected_information_missing": [],
    },
]

methods = [
    {
        "method_id": "M046",
        "method_text": (
            "Cross-phase consistency checking: inconsistencies between phase outputs (tool "
            "discovery versus tool documentation) were discovered, triggering the exhaustive "
            "audit — implying a comparison method that is never described."
        ),
        "method_type": "quality_control",
        "method_status": "implicit",
        "trigger_text": [
            "upon discovering inconsistencies between phase outputs (e.g., tool discovery versus tool documentation), we audited tool discovery and tool evidence outputs exhaustively",
        ],
        "trigger_locations": [
            {"section": "Methods", "subsection": "3.1 The 2025 phase", "page": 7},
        ],
        "inference_reasoning": (
            "Discovering inconsistencies between phase outputs presupposes some procedure for "
            "comparing them (joining datasets, matching tool identities across stages), but "
            "no comparison procedure is documented anywhere in the paper."
        ),
        "implicit_metadata": {
            "basis": "mentioned_undocumented",
            "transparency_gap": "How phase outputs were compared and what counted as an inconsistency is not described",
            "assessability_impact": "Cannot assess the sensitivity of the check that triggered the wave-2 audit",
            "reconstruction_confidence": "medium",
        },
        "location": {"section": "Methods", "subsection": "3.1 The 2025 phase", "page": 7},
        "implements_designs": ["RD016"],
        "expected_information_missing": [],
    },
    {
        "method_id": "M047",
        "method_text": (
            "QA reclassification process (to March 2026): verification columns in Tables 4-5 "
            "were amended by 'QA reclassifications' after the Nov-Dec 2025 audit, implying a "
            "continuing quality-assurance review whose procedure is undocumented."
        ),
        "method_type": "quality_control",
        "method_status": "implicit",
        "trigger_text": [
            "as amended by QA reclassifications to March 2026",
            "verification columns reflect the Nov–Dec 2025 audit, as amended by QA reclassifications to March 2026",
        ],
        "trigger_locations": [
            {"section": "Results", "subsection": "4.2 Tool discovery (Table 4 caption)", "page": 11},
            {"section": "Results", "subsection": "4.2 Tool discovery (Table 5 caption)", "page": 12},
        ],
        "inference_reasoning": (
            "Both discovery-outcome tables state their verification columns were amended by "
            "QA reclassifications continuing to March 2026, implying a post-audit review "
            "process that changed classifications; neither the trigger for reclassification "
            "nor the procedure is described."
        ),
        "implicit_metadata": {
            "basis": "mentioned_undocumented",
            "transparency_gap": "Reclassification criteria, count of changes, and reviewer are not documented",
            "assessability_impact": "Cannot trace which reported numbers changed after the audit or why",
            "reconstruction_confidence": "low",
        },
        "location": {"section": "Results", "subsection": "4.2 Tool discovery", "page": 11},
        "implements_designs": ["RD016"],
        "expected_information_missing": [],
    },
    {
        "method_id": "M048",
        "method_text": (
            "Verified-outcome accounting: the campaign is summarised as yielding 'some two "
            "thousand discrete, verifiable outcomes', implying an accounting method for "
            "defining and tallying outcome units across heterogeneous stages."
        ),
        "method_type": "analysis",
        "method_status": "implicit",
        "trigger_text": [
            "Across the stages this yielded some two thousand discrete, verifiable outcomes: a tool exists or does not, a reference resolves or does not, a stated year matches or does not.",
        ],
        "trigger_locations": [
            {"section": "Methods", "subsection": "3.1 The 2025 phase", "page": 8},
        ],
        "inference_reasoning": (
            "Reporting a cross-stage total of verifiable outcomes requires a unitisation and "
            "counting method (what counts as one outcome per stage, how overlaps are "
            "handled); the examples indicate the unit types but the accounting is not "
            "documented."
        ),
        "implicit_metadata": {
            "basis": "inferred_from_results",
            "transparency_gap": "Outcome unitisation and the composition of the ~2,000 figure are not itemised",
            "assessability_impact": "The headline verification scale cannot be decomposed or recomputed by a reader from the main text alone",
            "reconstruction_confidence": "medium",
        },
        "location": {"section": "Methods", "subsection": "3.1 The 2025 phase", "page": 8},
        "implements_designs": ["RD016"],
        "expected_information_missing": [],
    },
    {
        "method_id": "M049",
        "method_text": (
            "Literature inclusion criteria and academic-seriousness thresholds: source "
            "validity judgements ('sources meeting inclusion criteria', 'academic seriousness "
            "thresholds') are applied throughout the literature-discovery evaluation without "
            "the criteria being specified."
        ),
        "method_type": "analysis",
        "method_status": "implicit",
        "trigger_text": [
            "Valid: sources meeting inclusion criteria.",
            "all met academic seriousness thresholds, with no lightweight or non-academic content requiring exclusion",
            "5 web pages failed to meet academic seriousness thresholds",
        ],
        "trigger_locations": [
            {"section": "Results", "subsection": "4.1 (Table 2 caption)", "page": 10},
            {"section": "Supplement A", "subsection": "A.1 Per-tool source-type composition", "page": 30},
            {"section": "Supplement A", "subsection": "A.1 Per-tool source-type composition", "page": 31},
        ],
        "inference_reasoning": (
            "Valid/invalid classification of every discovered source depends on inclusion "
            "criteria and 'academic seriousness thresholds' that are referenced repeatedly "
            "but never defined; the classification method must exist for the reported error "
            "tables to have been produced."
        ),
        "implicit_metadata": {
            "basis": "mentioned_undocumented",
            "transparency_gap": "Inclusion criteria and seriousness thresholds are not enumerated",
            "assessability_impact": "Error rates by service cannot be independently reproduced from stated criteria",
            "reconstruction_confidence": "medium",
        },
        "location": {"section": "Results", "subsection": "4.1 Literature discovery and synthesis", "page": 10},
        "implements_designs": ["RD024"],
        "expected_information_missing": [],
    },
    {
        "method_id": "M050",
        "method_text": (
            "Co-author validation procedure: validation between co-authors is stated as a "
            "reflexivity mitigation, but the procedure (what was validated, how disagreements "
            "were resolved) is undocumented."
        ),
        "method_type": "quality_control",
        "method_status": "implicit",
        "trigger_text": [
            "We mitigated this through validation between co-authors and especially by anchoring every empirical claim to a logged artefact (session transcripts, git history, output spreadsheets).",
        ],
        "trigger_locations": [
            {"section": "Methods", "subsection": "3.3 Reflexivity", "page": 8},
        ],
        "inference_reasoning": (
            "Co-author validation is named as one of two mitigations for LLM affirmation "
            "risk, implying a review process between authors; no procedure, scope, or "
            "disagreement-resolution mechanism is described."
        ),
        "implicit_metadata": {
            "basis": "mentioned_undocumented",
            "transparency_gap": "Validation scope and procedure between co-authors are unspecified",
            "assessability_impact": "The strength of this mitigation cannot be assessed",
            "reconstruction_confidence": "low",
        },
        "location": {"section": "Methods", "subsection": "3.3 Reflexivity", "page": 8},
        "implements_designs": ["RD019"],
        "expected_information_missing": [],
    },
    {
        "method_id": "M051",
        "method_text": (
            "Run-type classification and error-rate computation: runs are classified as "
            "exploratory, main production, and final targeted, with error rates computed per "
            "class ('about half', 'about a third', 'single digits'), but the classification "
            "and computation method is undocumented."
        ),
        "method_type": "analysis",
        "method_status": "implicit",
        "trigger_text": [
            "Overall, exploratory runs produced errors about half the time, main production runs with structured prompts about a third, and final, targeted runs drove error rates into the single digits.",
        ],
        "trigger_locations": [
            {"section": "Results", "subsection": "4.2 Tool discovery", "page": 13},
        ],
        "inference_reasoning": (
            "Per-class error rates presuppose that runs were classified into exploratory/"
            "production/targeted categories and that errors were tallied per class; neither "
            "the class assignment rules nor the denominators are given."
        ),
        "implicit_metadata": {
            "basis": "inferred_from_results",
            "transparency_gap": "Run classification rules and per-class denominators are not reported",
            "assessability_impact": "The improvement trajectory across run types cannot be recomputed",
            "reconstruction_confidence": "medium",
        },
        "location": {"section": "Results", "subsection": "4.2 Tool discovery", "page": 13},
        "implements_designs": ["RD014"],
        "expected_information_missing": [],
    },
]

protocols = [
    {
        "protocol_id": "P037",
        "protocol_text": (
            "Informal spot-check procedure: spot-checks are the stated fallback verification "
            "across stages ('informal spot-checks', 'informal manual spot-checks were "
            "performed'), but sample sizes, frequency, and selection criteria are "
            "undocumented (the single documented instance is the 2026 four-row spot-check)."
        ),
        "protocol_type": "verification",
        "protocol_status": "implicit",
        "trigger_text": [
            "and then we switched to informal spot-checks",
            "In all cases informal manual spot-checks were performed.",
        ],
        "trigger_locations": [
            {"section": "Methods", "subsection": "3.1 The 2025 phase", "page": 7},
            {"section": "Methods", "subsection": "3.1 The 2025 phase", "page": 8},
        ],
        "inference_reasoning": (
            "Spot-checking is repeatedly invoked as a verification mechanism but no "
            "procedure (sampling rate, selection, escalation on failure) is documented for "
            "the 2025 campaign; the practice must have had some operational form to be "
            "'performed' in all cases."
        ),
        "implicit_metadata": {
            "basis": "mentioned_undocumented",
            "transparency_gap": "Spot-check sampling rates, selection method, and escalation rules are unspecified",
            "assessability_impact": "Cannot assess residual error risk in stages verified only by spot-checks",
            "reconstruction_confidence": "low",
        },
        "location": {"section": "Methods", "subsection": "3.1 The 2025 phase", "page": 7},
        "implements_methods": ["M006", "M012"],
        "expected_information_missing": [],
    },
    {
        "protocol_id": "P038",
        "protocol_text": (
            "Session-transcript bulk-export procedure: transcripts were bulk-exported 'where "
            "possible', with known gaps for some services; the export mechanism, tooling, and "
            "the conditions determining possibility are undocumented."
        ),
        "protocol_type": "recording",
        "protocol_status": "implicit",
        "trigger_text": [
            "Later, we bulk-exported session transcripts where possible to create a more comprehensive record (see Supplement A).",
            "for Perplexity, Elicit, and most Gemini runs, tabulated results survive but not conversation transcripts",
        ],
        "trigger_locations": [
            {"section": "Methods", "subsection": "3.1 The 2025 phase", "page": 7},
            {"section": "Methods", "subsection": "3.3 Reflexivity", "page": 8},
        ],
        "inference_reasoning": (
            "Bulk export happened and produced the archived record with service-specific "
            "gaps, implying a per-service export procedure whose mechanism and coverage "
            "rules are not documented."
        ),
        "implicit_metadata": {
            "basis": "mentioned_undocumented",
            "transparency_gap": "Export tooling and why some services could not be exported are unspecified",
            "assessability_impact": "Archive completeness per service cannot be predicted from the described procedure",
            "reconstruction_confidence": "medium",
        },
        "location": {"section": "Methods", "subsection": "3.1 The 2025 phase", "page": 7},
        "implements_methods": ["M004"],
        "expected_information_missing": [],
    },
    {
        "protocol_id": "P039",
        "protocol_text": (
            "Run-outcome logging schema: run outcomes were logged in spreadsheets and notes "
            "at execution time (the sentence spans the p6/p7 break; first trigger clipped at "
            "the break), but the spreadsheet structure, fields, and logging conventions are "
            "undocumented."
        ),
        "protocol_type": "recording",
        "protocol_status": "implicit",
        "trigger_text": [
            "Run outcomes were logged in spreadsheets and",
            "anchoring every empirical claim to a logged artefact (session transcripts, git history, output spreadsheets)",
        ],
        "trigger_locations": [
            {"section": "Methods", "subsection": "3.1 The 2025 phase", "page": 6},
            {"section": "Methods", "subsection": "3.3 Reflexivity", "page": 8},
        ],
        "inference_reasoning": (
            "Contemporaneous spreadsheet logging is the evidentiary backbone for run "
            "outcomes, and output spreadsheets are named as anchoring artefacts, implying a "
            "logging schema; its fields and conventions are never described."
        ),
        "implicit_metadata": {
            "basis": "mentioned_undocumented",
            "transparency_gap": "Spreadsheet fields, granularity, and update discipline are unspecified",
            "assessability_impact": "A reader cannot judge what was captured at execution time versus reconstructed later",
            "reconstruction_confidence": "low",
        },
        "location": {"section": "Methods", "subsection": "3.1 The 2025 phase", "page": 6},
        "implements_methods": ["M003"],
        "expected_information_missing": [],
    },
    {
        "protocol_id": "P040",
        "protocol_text": (
            "Journal issue/volume coverage allocation: discovery prompts bounded issue "
            "coverage (up to five issues per prompt; JOAD volumes 1-8 then 9-16), implying a "
            "coverage plan allocating volumes/issues per journal; the overall allocation and "
            "completeness of coverage per journal is undocumented."
        ),
        "protocol_type": "task_structuring",
        "protocol_status": "implicit",
        "trigger_text": [
            "examine up to five issues of a journal",
            "when prompted to continue from JOAD volumes 1–8 (which used research mode and returned legitimate articles) to volumes 9–16",
            "bounded issue coverage",
        ],
        "trigger_locations": [
            {"section": "Methods", "subsection": "3.1 The 2025 phase", "page": 7},
            {"section": "Supplement A", "subsection": "A.2 The JOAD silent mode-switch", "page": 34},
            {"section": "Results", "subsection": "4.2 Tool discovery", "page": 12},
        ],
        "inference_reasoning": (
            "Batched issue examination and volume-range continuation prompts imply a "
            "coverage allocation across each journal's run history; whether every volume of "
            "every journal was covered, and in what order, is not documented."
        ),
        "implicit_metadata": {
            "basis": "mentioned_undocumented",
            "transparency_gap": "Per-journal volume/issue coverage and completeness are not reported",
            "assessability_impact": "Discovery yield per journal cannot be normalised against corpus coverage",
            "reconstruction_confidence": "medium",
        },
        "location": {"section": "Results", "subsection": "4.2 Tool discovery", "page": 12},
        "implements_methods": ["M022"],
        "expected_information_missing": [],
    },
    {
        "protocol_id": "P041",
        "protocol_text": (
            "Verifier field-check rubric: the 2026 verifier compares 'each claimed field', "
            "and one documented miss was 'an author error the check was not yet looking "
            "for', implying an evolving rubric enumerating which fields and error types are "
            "checked; the rubric's contents and versions are undocumented in the paper body."
        ),
        "protocol_type": "verification",
        "protocol_status": "implicit",
        "trigger_text": [
            "compares each claimed field",
            "Its two documented misses were one of scope (a verified claim corrupted by the step that wrote it to the bibliography) and one of rubric (an author error the check was not yet looking for).",
        ],
        "trigger_locations": [
            {"section": "Methods", "subsection": "3.2 The 2026 phase", "page": 8},
            {"section": "Results", "subsection": "4.5.2 The fix: two guards", "page": 18},
        ],
        "inference_reasoning": (
            "A miss attributed to 'rubric' entails a defined check-list of fields/error "
            "types the verifier inspects, which changed over time as misses were closed by "
            "structural fixes; the rubric itself is not reproduced."
        ),
        "implicit_metadata": {
            "basis": "inferred_from_results",
            "transparency_gap": "The verifier's field/error rubric and its version history are not documented in the body",
            "assessability_impact": "Coverage of the automated verification cannot be enumerated by a reader",
            "reconstruction_confidence": "medium",
        },
        "location": {"section": "Results", "subsection": "4.5.2 The fix: two guards", "page": 18},
        "implements_methods": ["M015"],
        "expected_information_missing": [],
    },
    {
        "protocol_id": "P042",
        "protocol_text": (
            "Manual bibliographic-correction procedure: roughly two-thirds of valid "
            "AI-discovered sources needed manual correction of URLs, DOIs, or author "
            "information, implying a correction workflow (rediscovery, canonical-source "
            "lookup) that is not described."
        ),
        "protocol_type": "data_processing",
        "protocol_status": "implicit",
        "trigger_text": [
            "roughly two-thirds of the valid AI-discovered sources needed manual correction of URLs, DOIs, or author information",
            "10 sources carried incorrect URLs requiring manual rediscovery",
        ],
        "trigger_locations": [
            {"section": "Results", "subsection": "4.1 Literature discovery and synthesis", "page": 10},
            {"section": "Supplement A", "subsection": "A.1 Per-tool source-type composition", "page": 30},
        ],
        "inference_reasoning": (
            "Correcting URLs, DOIs, and author fields at that scale requires a repeatable "
            "manual workflow (how canonical values were found and recorded); the workflow "
            "is mentioned by its outcomes only."
        ),
        "implicit_metadata": {
            "basis": "mentioned_undocumented",
            "transparency_gap": "Correction sources and recording of corrections are unspecified",
            "assessability_impact": "Cannot distinguish corrected from originally correct fields in the final corpus",
            "reconstruction_confidence": "medium",
        },
        "location": {"section": "Results", "subsection": "4.1 Literature discovery and synthesis", "page": 10},
        "implements_methods": ["M008"],
        "expected_information_missing": [],
    },
    {
        "protocol_id": "P043",
        "protocol_text": (
            "Line-by-line quote verification during Claude Code evaluation: Claude Code's "
            "qualitative-research trial required line-by-line verification of all quoted "
            "material due to its confabulation rate; the verification procedure is "
            "undocumented."
        ),
        "protocol_type": "verification",
        "protocol_status": "implicit",
        "trigger_text": [
            "though its confabulation rate remained high enough to require line-by-line verification of all quoted material",
        ],
        "trigger_locations": [
            {"section": "Supplement A", "subsection": "A.1 Other tools screened out", "page": 33},
        ],
        "inference_reasoning": (
            "The stated requirement for line-by-line verification of quoted material during "
            "the Claude Code trial implies a quote-checking procedure against source files; "
            "no procedure is described."
        ),
        "implicit_metadata": {
            "basis": "mentioned_undocumented",
            "transparency_gap": "Quote-verification procedure for the Claude Code trial is unspecified",
            "assessability_impact": "Minor: affects only the screened-tool evaluation, not production outputs",
            "reconstruction_confidence": "low",
        },
        "location": {"section": "Supplement A", "subsection": "A.1 Other tools screened out", "page": 33},
        "implements_methods": ["M018"],
        "expected_information_missing": [],
    },
]

save_group(
    {
        "group": "Pass4-implicit",
        "section_title": "Whole-paper implicit RDMAP scan (4 patterns x 3 tiers x all sections)",
        "page_range": "1-39",
        "scan_note": (
            "Systematic scan: Abstract/Intro (no implicit RDMAP beyond explicit designs); "
            "Background (frameworks explicit); Methods (logging schema, transcript export, "
            "spot-checks, co-author validation, outcome accounting); Results (QA "
            "reclassifications, run-type classification, inclusion criteria, coverage "
            "allocation, verifier rubric, correction workflow); Discussion (practices "
            "explicit); Supplement (line-by-line verification). One implicit design "
            "(capability adoption-upon-release). Implicit ratio 14/123 = 11.4%, consistent "
            "with a methods-transparent methodological paper."
        ),
    },
    research_designs=designs,
    methods=methods,
    protocols=protocols,
    notes_key="pass4_implicit_scan",
)

# Bookkeeping: record pass4 completion and the ID-convention decision.
data = json.loads(EXTRACTION.read_text(encoding="utf-8"))
notes = data["extraction_notes"]
if "pass4" not in notes["passes_completed"]:
    notes["passes_completed"].append("pass4")
notes["pass4_extraction"] = {
    "approach": (
        "Whole-paper implicit RDMAP scan using the 4 recognition patterns per tier per major "
        "section, seeded from Pass 3 explicit RDMAP. All trigger_text mechanically verified "
        "against the processed markdown. ID convention: sequential RD###/M###/P### numbering "
        "continued from Pass 3 with *_status='implicit' (corpus convention, e.g. "
        "sobotkova-et-al-2024 P010-P012), deviating from prompt 04's suggested IMP-prefixed "
        "IDs for consistency with prior extractions and downstream tooling."
    ),
    "counts": {"implicit_designs": 1, "implicit_methods": 6, "implicit_protocols": 7},
    "implicit_ratio": "14/123 (11.4%)",
    "script": "pass4_implicit_rdmap.py",
}
EXTRACTION.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("pass4 recorded:", notes["passes_completed"])
