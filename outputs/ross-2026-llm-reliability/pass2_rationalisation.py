#!/usr/bin/env python3
"""Pass 2: conservative rationalisation of claims/evidence for ross-2026-llm-reliability.

Consolidation strategy (whole-paper review):
- Claims: absorb cross-section restatements of the same assertion (the paper restates its
  core theses in Abstract, Introduction, Background, Methods, Discussion, Conclusion, and
  Supplement) and merge compound fragments that would be assessed together. 26 absorptions,
  13.5% reduction — at the lower edge of the 15-20% target, appropriate for a methodological
  paper whose Discussion principles are genuinely well-differentiated.
- Evidence: redundancy elimination only where a Discussion/Supplement restatement duplicates
  a Results observation with an identical support pattern (4 merges), plus one boundary
  correction (E007 definitional literature grounding -> project_metadata). 1.7% reduction,
  preserving data granularity.
- Implicit arguments: no reduction (already selective); Pass 2 cross-section review found
  the cross-arc assumptions already covered (IA002, IA016, IA018).

All references are repaired transitively in both directions; absorbed items' quotes and
locations are preserved in consolidation_metadata for audit.
"""

import json
from datetime import datetime, timezone, timedelta
from pathlib import Path

BASE = Path(__file__).resolve().parent
EXTRACTION = BASE / "extraction.json"

# (removed_id, target_id, consolidation_type, rationale)
CLAIM_MERGES = [
    ("C017", "C007", "redundancy_elimination",
     "Abstract restatement bridging augment/automate and the engineering prescription; canonical statement kept in C007 (with C008 covering the distinction)."),
    ("C024", "C022", "compound_interpretation",
     "Vocabulary-renaming point is the justificatory half of the functional-boundary claim; assessed together."),
    ("C032", "C002", "redundancy_elimination",
     "Background restatement of the cannot-appraise-from-within premise (Introduction C002)."),
    ("C038", "C005", "compound_interpretation",
     "Disclosure-necessary-but-insufficient and disclosure-tells-what-to-suspect are one assessed position; E015 support carried over."),
    ("C041", "C040", "narrative_consolidation",
     "Checking-cost observation is one strand of the conditions-inhibit-verification claim."),
    ("C051", "C007", "redundancy_elimination",
     "Section 2.3 'must be engineered into the scaffolding' restates C007 with literature grounding; compound-systems evidence (E025-E027) carried over."),
    ("C052", "C013", "redundancy_elimination",
     "Two-complementary-halves (2.3) restates the Introduction two-part scaffolding structure (C013)."),
    ("C058", "C013", "redundancy_elimination",
     "'First half of the structure' summary line folded into the two-part structure claim."),
    ("C075", "C118", "redundancy_elimination",
     "Methods forward-reference ('registry grounding did not foreclose confabulation') is the same finding as Results C118 (narrowed but not removed)."),
    ("C076", "C174", "redundancy_elimination",
     "Methods 3.3 case-study framing restated in Limitations; canonical statement kept in C174."),
    ("C081", "C070", "narrative_consolidation",
     "Reporting-standard sentence merged with the evaluation-priorities framing claim."),
    ("C095", "C094", "redundancy_elimination",
     "Episode-framing sentence absorbed into the premise-inheritance conclusion it introduces."),
    ("C102", "C101", "redundancy_elimination",
     "'Changing the question, and the questioner' is the summary line of the orthogonal-check claim C101."),
    ("C119", "C014", "redundancy_elimination",
     "Discussion opening restates the synthesis-boundary failure (C014), mitigation triad (C015), and persistence (C019); E184 support moved to C014."),
    ("C125", "C014", "redundancy_elimination",
     "'The failure mode, however, persisted' restates C014 with the cross-episode mechanism; support carried over."),
    ("C126", "C127", "narrative_consolidation",
     "Formal-thoroughness-amplifies and whole-artefact-credibility are one argument about partial grounding."),
    ("C128", "C015", "redundancy_elimination",
     "Discussion restatement that the three mitigations carried over; E185 support moved to the mitigation-triad claim."),
    ("C133", "C174", "redundancy_elimination",
     "'Argue rather than prove' epistemic qualifier consolidated into the Limitations case-study claim; supports C132 carried over."),
    ("C140", "C137", "redundancy_elimination",
     "'Independence of context, not severity of instruction' restates the architecture-of-attention principle within the same subsection."),
    ("C163", "C097", "redundancy_elimination",
     "Discussion articulation of working-with-the-grain; canonical principle kept in C097 (Results)."),
    ("C182", "C001", "redundancy_elimination",
     "Conclusion restatement of the thesis and persistence; canonical statement kept in C001."),
    ("C184", "C008", "redundancy_elimination",
     "Conclusion restatement of augment-not-automate; canonical statement kept in C008."),
    ("C187", "C094", "redundancy_elimination",
     "Supplement articulation of the premise-inheritance verification limit; transcript support (E252, E253) carried over."),
    ("C190", "C107", "redundancy_elimination",
     "Supplement narrowing-the-remit lesson restates the Results decomposition-consistency claim; E265 support carried over."),
    ("C191", "C111", "redundancy_elimination",
     "Supplement ArboDat interpretation (correspondence, not retrieval) restates C111; E277 support carried over."),
    ("C192", "C109", "redundancy_elimination",
     "Supplement borrowed-plausibility interpretation restates C109; E280 support carried over."),
]

EVIDENCE_MERGES = [
    ("E024", "E047", "redundancy_elimination",
     "Background revival statement duplicates the fuller Methods account of the stalled project; identical support pattern (C034)."),
    ("E203", "E124", "redundancy_elimination",
     "Discussion restatement of the version-history domestication example (Results E124); identical support after C163->C097 merge."),
    ("E204", "E125", "redundancy_elimination",
     "Discussion restatement of the reproducibility-codification example (Results E125); identical support after C163->C097 merge."),
    ("E258", "E222", "redundancy_elimination",
     "A.2 'asserted versus accomplished' restates the A.1 Debates-snippet anecdote (E222/E084); identical support pattern (C014/C085)."),
]

# Boundary correction: definitional literature grounding, not evidence supporting a claim.
EVIDENCE_TO_PROJECT_METADATA = ["E007"]


def resolve(mapping: dict, ref: str) -> str:
    while ref in mapping:
        ref = mapping[ref]
    return ref


def main() -> None:
    data = json.loads(EXTRACTION.read_text(encoding="utf-8"))
    claims = {c["claim_id"]: c for c in data["claims"]}
    evidence = {e["evidence_id"]: e for e in data["evidence"]}

    n_before = len(data["evidence"]) + len(data["claims"]) + len(data["implicit_arguments"])

    claim_map = {r: t for r, t, _, _ in CLAIM_MERGES}
    ev_map = {r: t for r, t, _, _ in EVIDENCE_MERGES}

    # Absorb claims into targets.
    for removed, target, ctype, rationale in CLAIM_MERGES:
        src, dst = claims[removed], claims[resolve(claim_map, target)]
        meta = dst.setdefault("consolidation_metadata", {
            "consolidated_from": [dst["claim_id"]],
            "consolidation_type": ctype,
            "information_preserved": "complete",
            "absorbed_items": [],
            "rationale": rationale,
        })
        meta["consolidated_from"].append(removed)
        meta.setdefault("absorbed_items", []).append({
            "id": removed,
            "verbatim_quote": src["verbatim_quote"],
            "location": src["location"],
        })
        if rationale not in meta["rationale"]:
            meta["rationale"] += f" | {removed}: {rationale}"
        dst["supported_by"] = sorted(set(dst.get("supported_by", []))
                                     | set(src.get("supported_by", [])))
        dst["supports_claims"] = sorted(set(dst.get("supports_claims", []))
                                        | set(src.get("supports_claims", [])))

    # Absorb evidence into targets.
    for removed, target, ctype, rationale in EVIDENCE_MERGES:
        src, dst = evidence[removed], evidence[resolve(ev_map, target)]
        meta = dst.setdefault("consolidation_metadata", {
            "consolidated_from": [dst["evidence_id"]],
            "consolidation_type": ctype,
            "information_preserved": "complete",
            "absorbed_items": [],
            "rationale": rationale,
        })
        meta["consolidated_from"].append(removed)
        meta.setdefault("absorbed_items", []).append({
            "id": removed,
            "verbatim_quote": src["verbatim_quote"],
            "location": src["location"],
        })
        dst["supports_claims"] = sorted(set(dst.get("supports_claims", []))
                                        | set(src.get("supports_claims", [])))

    # Boundary correction: E007 -> project_metadata.
    for ev_id in EVIDENCE_TO_PROJECT_METADATA:
        src = evidence[ev_id]
        data["project_metadata"].setdefault("definitional_grounding", []).append({
            "moved_from": ev_id,
            "text": src["evidence_text"],
            "verbatim_quote": src["verbatim_quote"],
            "location": src["location"],
            "rationale": "Definitional literature grounding for the 'scaffolding' concept; does not evidence a specific claim (Pass 2 boundary correction).",
        })
        ev_map[ev_id] = None  # references to it are dropped

    # Drop removed items.
    removed_claims = set(claim_map)
    removed_evidence = set(ev_map)
    data["claims"] = [c for c in data["claims"] if c["claim_id"] not in removed_claims]
    data["evidence"] = [e for e in data["evidence"] if e["evidence_id"] not in removed_evidence]

    # Repair all references transitively, drop self-references and dropped targets.
    def fix_refs(refs, mapping, self_id=None):
        out = []
        for r in refs:
            r2 = resolve(mapping, r) if r in mapping else r
            if r2 is None or r2 == self_id:
                continue
            out.append(r2)
        return sorted(set(out))

    for c in data["claims"]:
        c["supported_by"] = fix_refs(c.get("supported_by", []), ev_map)
        c["supports_claims"] = fix_refs(c.get("supports_claims", []), claim_map, c["claim_id"])
    for e in data["evidence"]:
        e["supports_claims"] = fix_refs(e.get("supports_claims", []), claim_map)
    for a in data["implicit_arguments"]:
        a["supports_claims"] = fix_refs(a.get("supports_claims", []), claim_map)

    n_after = len(data["evidence"]) + len(data["claims"]) + len(data["implicit_arguments"])

    notes = data["extraction_notes"]
    notes["passes_completed"].append("pass2")
    notes["pass2_rationalisation"] = {
        "items_before": n_before,
        "items_after": n_after,
        "reduction_percentage": round(100 * (n_before - n_after) / n_before, 1),
        "claims_before": 192, "claims_after": len(data["claims"]),
        "claims_reduction_pct": round(100 * (192 - len(data["claims"])) / 192, 1),
        "evidence_before": 288, "evidence_after": len(data["evidence"]),
        "evidence_reduction_pct": round(100 * (288 - len(data["evidence"])) / 288, 1),
        "implicit_arguments": len(data["implicit_arguments"]),
        "consolidations_performed": len(CLAIM_MERGES) + len(EVIDENCE_MERGES),
        "boundary_corrections": len(EVIDENCE_TO_PROJECT_METADATA),
        "additions_performed": 0,
        "rationale": ("Conservative consolidation targeting cross-section restatements "
                      "(Abstract/Background/Methods/Discussion/Conclusion/Supplement chains). "
                      "13.5% claims reduction at the lower edge of the 15-20% target, appropriate "
                      "for a methodological paper with genuinely well-differentiated design "
                      "principles; evidence reduced 1.7% to preserve data granularity. "
                      "Implicit arguments unchanged. Addition patterns reviewed: recommendations, "
                      "comparisons, and synthesis claims were already captured in Pass 1 "
                      "(C112, C177-C181); no additions required."),
    }
    notes["session_log"].append(
        "Session B (2026-07-24): Pass 2 rationalisation - claims 192->" +
        str(len(data['claims'])) + ", evidence 288->" + str(len(data['evidence'])) +
        ", implicit arguments unchanged (20); 30 consolidations + 1 boundary correction "
        "(E007 -> project_metadata.definitional_grounding); all cross-references repaired "
        "transitively in both directions")

    aest = timezone(timedelta(hours=10))
    data["extraction_timestamp"] = datetime.now(aest).isoformat(timespec="seconds")
    EXTRACTION.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n",
                          encoding="utf-8")

    # Post-write integrity check.
    ev_ids = {e["evidence_id"] for e in data["evidence"]}
    cl_ids = {c["claim_id"] for c in data["claims"]}
    dangling = []
    for c in data["claims"]:
        dangling += [f"{c['claim_id']}->{r}" for r in c["supported_by"] if r not in ev_ids]
        dangling += [f"{c['claim_id']}->{r}" for r in c["supports_claims"] if r not in cl_ids]
    for e in data["evidence"]:
        dangling += [f"{e['evidence_id']}->{r}" for r in e["supports_claims"] if r not in cl_ids]
    for a in data["implicit_arguments"]:
        dangling += [f"{a['implicit_argument_id']}->{r}" for r in a["supports_claims"]
                     if r not in cl_ids]

    print(f"Pass 2 complete: evidence {len(data['evidence'])}, claims {len(data['claims'])}, "
          f"implicit_arguments {len(data['implicit_arguments'])}")
    print(f"Claims reduction: {round(100 * (192 - len(data['claims'])) / 192, 1)}% | "
          f"Evidence reduction: {round(100 * (288 - len(data['evidence'])) / 288, 1)}%")
    print(f"Dangling references after repair: {len(dangling)}")
    for d in dangling:
        print("  ", d)


if __name__ == "__main__":
    main()
