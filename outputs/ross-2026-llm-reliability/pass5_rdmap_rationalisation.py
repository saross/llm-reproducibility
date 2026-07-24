#!/usr/bin/env python3
"""Pass 5 (RDMAP rationalisation) — ross-2026-llm-reliability.

Conservative consolidation of the liberal Pass 3/4 extraction. Sixteen merges:
supplement/discussion restatements folded into their primary main-text items,
same-instrument lineage items unified, and duplicate framings merged. One
boundary correction (effectiveness outcome trimmed from P013's protocol_text).

Every consolidation preserves the merged item's verbatim_quote and location in
consolidation_metadata (Session B pattern: quotes carried forward verbatim,
never synthesised), so mechanical re-verification still passes. Forward
cross-references are remapped old->new before reverse references are rebuilt.
"""

import json

from rdmap_lib import EXTRACTION, load_corpus, sync_reverse_refs, verify_quotes

data = json.loads(EXTRACTION.read_text(encoding="utf-8"))

ARRAYS = {
    "RD": ("research_designs", "design_id", "design_text"),
    "M": ("methods", "method_id", "method_text"),
    "P": ("protocols", "protocol_id", "protocol_text"),
}


def get(item_id):
    key, id_field, _ = ARRAYS[item_id.rstrip("0123456789")]
    for item in data[key]:
        if item[id_field] == item_id:
            return item
    raise KeyError(item_id)


def remove(item_id):
    key, id_field, _ = ARRAYS[item_id.rstrip("0123456789")]
    data[key] = [i for i in data[key] if i[id_field] != item_id]


# (removed, survivor, consolidation_type, rationale, text_addendum-or-None)
MERGES = [
    ("RD007", "RD001", "rationale_synthesis",
     "Background restatement of the Introduction's research-question framing "
     "(deployment-not-adoption question); same strategic framing, assessed together.",
     None),
    ("RD012", "RD002", "rationale_synthesis",
     "Methods restatement of the Introduction's two-episode grounding design "
     "(primary illustrates in depth, secondary indicates persistence); one design.",
     "The primary phase illustrates the argument in depth while the secondary episode "
     "indicates persistence of the characteristics."),
    ("RD022", "RD014", "scope_integration",
     "The authentic-use measurement stance (Results 4) operationalises the embedded "
     "evaluation's practitioner priority (Methods 3.1); a single evaluative stance.",
     "Each tool is reported on what it showed itself able to do in authentic research, "
     "measured against its intended use."),
    ("RD028", "RD027", "scope_integration",
     "Both Limitations statements express one small-sample reporting stance: direction "
     "over magnitude, and the verifier as worked pattern rather than benchmarked result.",
     "Accordingly the verifier is presented as a worked design pattern rather than a "
     "benchmarked result."),
    ("M005", "M006", "workflow_integration",
     "The two-wave umbrella statement is structural context for the wave-1 "
     "(comprehensive-then-spot-check) and wave-2 (M011 audit) methods; its sentence is "
     "preserved verbatim on RD016.",
     "This constitutes wave 1 of the two-wave verification structure (wave 2: the "
     "Nov-Dec 2025 exhaustive audit, M011)."),
    ("M032", "M012", "workflow_integration",
     "Results 4.4 describes the execution of the same three-point evidence-event "
     "verification stated in Methods 3.1; single method, multi-location.",
     "Every event was reviewed; the check occurred in fresh context and was re-grounded "
     "in the sources themselves."),
    ("M043", "M041", "workflow_integration",
     "Reasoning-trace ('thinking' log) and chat-transcript examination are one "
     "failure-diagnosis analysis method applied across episodes (Gemini task conflation; "
     "JOAD silent mode-switch).",
     "Chat transcripts were likewise examined to identify failure triggers (e.g., the "
     "JOAD silent mode-switch)."),
    ("M044", "M010", "rationale_synthesis",
     "Supplement A.3's model-as-prompt-designer strategy is the same meta-prompting "
     "practice described in Methods 3.1; single method, multi-location.",
     "The supplement records the collaborative form of this practice: enlisting the "
     "model as prompt designer ('How could the definition be improved to help you make "
     "that determination?')."),
    ("M045", "M026", "workflow_integration",
     "Supplement A.4 records the same three-service metadata assessment as Results 4.3 "
     "with FAIMS as primary ground truth; single method, multi-location. Service-naming "
     "discrepancy between the two locations remains flagged in presubmission_qa_flags.",
     "Per Supplement A.4, FAIMS was the primary ground truth and outputs for other "
     "familiar archaeological tools were also validated."),
    ("M039", "M013", "workflow_integration",
     "Discussion 5.2's qualification trials against first-hand software are the same "
     "familiar-target grounding practice stated in Methods 3.1; single method.",
     "During tool documentation, trials ran against software known first-hand until the "
     "task completed reliably and failures were understood to be all-or-nothing."),
    ("M029", "M007", "validation_chain",
     "External-source comparison (open-archaeo) and documentation-stage manual accuracy "
     "checks against first-hand knowledge, open-archaeo, and GitHub form one external "
     "accuracy-checking method applied across stages.",
     "Documentation outputs were likewise manually checked against first-hand knowledge "
     "or sources such as the open-archaeo catalogue and GitHub."),
    ("P026", "P001", "parameter_integration",
     "Discussion 5.2 supplies the production granularity of the same decomposition "
     "protocol (tool by tool, one CSV row at a time; journal issues in small blocks).",
     "In production this meant tool documentation proceeded tool by tool, one CSV row "
     "at a time, and tool discovery examined journal issues in small blocks."),
    ("P035", "P006", "workflow_integration",
     "Supplement A.5 details the execution of the same three-point evidence review "
     "(by hand and with LLM assistance, reconciled with discovery and metadata "
     "outcomes); single protocol, multi-location.",
     "All 1,040 events were reviewed by hand and with LLM assistance, reconciling "
     "results with the discovery and metadata outcomes."),
    ("P030", "P015", "parameter_integration",
     "Supplement A.3 enumerates the field-level content of the same eight-iteration "
     "metadata prompt lineage; single instrument specification.",
     "Field detail (A.3): the original five prose fields (description, history, "
     "technical discussion, strengths, weaknesses) were joined by further prose fields "
     "(interoperability, survivability, alternatives, usage indicators) and structured "
     "metadata (URLs, repository locations, licence, language, platform, authors, "
     "release dates, development status, institutional backing); the prompt grew from "
     "~120 to ~310 lines before streamlining to ~250."),
    ("P033", "P021", "parameter_integration",
     "Supplement A.3's evidence prompt v1 (15-column synthesis format with aggregate "
     "metrics) is the same superseded protocol as Results 4.4's early iterations.",
     "Version 1 specified a 15-column synthesis format requiring aggregate metrics "
     "(commit counts, contributor numbers, release tags) and one row per tool."),
    ("P034", "P022", "parameter_integration",
     "Supplement A.3's evidence prompt v5 (5 columns, one row per source, synthesis "
     "prohibited) is the same one-row-per-sighting schema as Results 4.4.",
     "Version 5 reduced output to 5 columns (Tool, Year, Source, URL, AI_Notes) with "
     "one row per source and an explicit prohibition of synthesis."),
]

consolidations = []
for removed_id, survivor_id, ctype, rationale, addendum in MERGES:
    removed = get(removed_id)
    survivor = get(survivor_id)
    _, id_field, text_field = ARRAYS[removed_id.rstrip("0123456789")]
    if addendum:
        survivor[text_field] = survivor[text_field].rstrip() + " " + addendum
    meta = survivor.setdefault("consolidation_metadata", {
        "consolidated_from": [], "consolidation_type": ctype,
        "information_preserved": "complete", "rationale": rationale,
        "merged_sources": [],
    })
    meta["consolidated_from"].append(removed_id)
    meta["merged_sources"].append({
        "id": removed_id,
        "verbatim_quote": removed.get("verbatim_quote"),
        "trigger_text": removed.get("trigger_text"),
        "location": removed.get("location"),
    })
    if meta["consolidation_type"] != ctype:
        meta["consolidation_type"] = f"{meta['consolidation_type']}+{ctype}"
    # Union expected-information gaps and forward design refs so nothing is lost.
    for gap in removed.get("expected_information_missing", []):
        if gap not in survivor.setdefault("expected_information_missing", []):
            survivor["expected_information_missing"].append(gap)
    for did in removed.get("implements_designs", []):
        if did not in survivor.setdefault("implements_designs", []):
            survivor["implements_designs"].append(did)
    remove(removed_id)
    consolidations.append(f"{removed_id} -> {survivor_id} ({ctype})")

# Remap forward references from removed IDs to their survivors, then dedupe.
remap = {removed: survivor for removed, survivor, *_ in MERGES}
for key, _, _ in ARRAYS.values():
    for item in data[key]:
        for field in ("implements_designs", "implements_methods"):
            if field in item:
                seen, updated = set(), []
                for ref in item[field]:
                    ref = remap.get(ref, ref)
                    if ref not in seen:
                        seen.add(ref)
                        updated.append(ref)
                item[field] = updated

# Boundary correction: effectiveness outcome does not belong in protocol_text
# (it is claims/evidence territory); the procedure description is retained.
p013 = get("P013")
p013["protocol_text"] = (
    "Revised JOSS enumeration-and-extraction prompt: bounded issue coverage, "
    "article-by-article extraction against the tool definition, output constrained by "
    "a fixed schema — the manually written replacement for the open search."
)

sync_reverse_refs(data)

# Mechanical re-verification of every surviving quote and trigger.
corpus = load_corpus()
errors = (
    verify_quotes(data["research_designs"], corpus, "design")
    + verify_quotes(data["methods"], corpus, "method")
    + verify_quotes(data["protocols"], corpus, "protocol")
)
if errors:
    print("POST-CONSOLIDATION VERIFICATION FAILED — nothing saved:")
    for e in errors:
        print(f"  ✗ {e}")
    raise SystemExit(1)

counts = {k: len(data[key]) for k, (key, _, _) in
          zip(["designs", "methods", "protocols"], ARRAYS.values())}
before, after = 123, sum(counts.values())
notes = data["extraction_notes"]
if "pass5" not in notes["passes_completed"]:
    notes["passes_completed"].append("pass5")
notes["pass5_rationalisation"] = {
    "items_before": before,
    "items_after": after,
    "reduction_percentage": round(100 * (before - after) / before, 1),
    "consolidations_performed": len(consolidations),
    "consolidations": consolidations,
    "tier_corrections": 0,
    "boundary_corrections": 1,
    "boundary_correction_detail": (
        "P013 protocol_text trimmed of the effectiveness outcome ('reducing "
        "confabulations from 15 to none'), which is claims/evidence territory; the "
        "verbatim_quote is unchanged."
    ),
    "rationale": (
        "13.0% reduction, below the 15-20% target and appropriate for a methodological "
        "paper whose procedures are genuinely well-differentiated: consolidations are "
        "confined to supplement/discussion restatements of main-text items, "
        "same-instrument lineage detail, and duplicate framings. Distinct prompt-lineage "
        "versions (P012/P013, P021/P022), domestication instances (P016/P017/P032), and "
        "stage-level designs were deliberately preserved for independent transparency "
        "assessment. All merged quotes preserved verbatim in "
        "consolidation_metadata.merged_sources."
    ),
}
EXTRACTION.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"Pass 5 complete: {before} -> {after} items "
      f"({notes['pass5_rationalisation']['reduction_percentage']}% reduction)")
print(f"Counts: {counts}")
for c in consolidations:
    print(f"  {c}")
