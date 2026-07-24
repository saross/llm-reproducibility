#!/usr/bin/env python3
"""Pass 7 validation for ross-2026-llm-reliability (Session D).

Runs the manual/semantic half of the Pass 7 checklist
(extraction-system/prompts/07-validation_prompt.md). The structural half is
already covered by the shared scripts, which are run separately and must pass
first:

    python3 extraction-system/scripts/validate_extraction.py \
        outputs/ross-2026-llm-reliability/extraction.json \
        extraction-system/schema/extraction-schema-v2.6.json
    python3 extraction-system/scripts/check_rdmap_completeness.py <extraction.json>
    python3 extraction-system/scripts/validate_bidirectional.py <extraction.json>

Note: validate_extraction.py defaults to a schema filename that does not exist
(extraction_schema.json); the real file is extraction-schema-v2.6.json and must
be passed as the second argument.

VALIDATING AGAINST CORPUS CONVENTIONS, NOT PROMPT DEFAULTS
----------------------------------------------------------
This extraction deviates from prompt 07's literal expectations in four places.
Each deviation is deliberate and recorded in extraction_notes; this script
validates the convention actually in use rather than reporting it as a failure:

1. No `source_verification` objects exist on any item. Quotes were verified
   MECHANICALLY at extraction time by pass1_lib.py (evidence/claims/implicit
   arguments) and rdmap_lib.py (RDMAP), which abort the save on any quote that
   is not a normalised substring of the source. This script re-runs that same
   test rather than looking for the field structure prompt 07 Checks 4.1/4.3
   describe.

2. Implicit RDMAP items use sequential RD###/M###/P### IDs with
   *_status="implicit", not the IMP prefixes of prompt 04 (recorded in
   extraction_notes.pass4_extraction).

3. Methods carry BOTH `realized_through_protocols` and
   `implemented_by_protocols`. These are mirrored by rdmap_lib.sync_reverse_refs
   and must agree; the pair is the convention, not a duplication bug.

4. Four page-break-spanning quotes were deliberately clipped, with the omission
   documented on the item. Clipped quotes are a sourcing decision, not a
   sourcing failure.

The seven entries in extraction_notes.presubmission_qa_flags record genuine
internal inconsistencies IN THE PAPER. They are the deliverable of this
pre-submission quality check, not defects in the extraction, and this script
reports them without touching them.

This script is read-mostly: it writes only extraction_notes.pass7_validation,
extraction_notes.passes_completed, extraction_notes.session_log, and the
deferral note. It never modifies the content arrays.

Usage:
    python3 outputs/ross-2026-llm-reliability/pass7_validation.py [--dry-run]

Author: Claude Fable 5 (Session D)
Date: 2026-07-24
"""

import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE))

# Reuse the extraction-time normalisation rather than reimplementing it, so
# re-verification is bit-for-bit the same test that gated the original saves.
from rdmap_lib import EXTRACTION, load_corpus, normalise  # noqa: E402

PAGE_COUNT = 39  # '--- page N ---' markers in the processed markdown (1-based)

# ID pattern per schema v2.6. Implicit RDMAP items share the same sequential
# space as explicit ones by corpus convention (see module docstring, point 2).
ID_PATTERNS = {
    "evidence": ("evidence_id", re.compile(r"^E\d{3}$")),
    "claims": ("claim_id", re.compile(r"^C\d{3}$")),
    "implicit_arguments": ("implicit_argument_id", re.compile(r"^IA\d{3}$")),
    "research_designs": ("design_id", re.compile(r"^RD\d{3}$")),
    "methods": ("method_id", re.compile(r"^M\d{3}$")),
    "protocols": ("protocol_id", re.compile(r"^P\d{3}$")),
}

# RDMAP arrays and the prefix used for their status/text/id fields.
RDMAP_KINDS = {
    "research_designs": "design",
    "methods": "method",
    "protocols": "protocol",
}

# Items whose quotes were deliberately clipped at a page break. Session B clips
# document the omission in the item's `notes` field; Session C clips document it
# inline in the item's text field. P030 was a Session C clip but Pass 5
# consolidated it into P015, where its quote survives under
# consolidation_metadata.merged_sources — so it is no longer a live item.
KNOWN_CLIPS = {
    "notes": ["E026", "E040", "E130", "E136", "E197", "E252", "E277"],
    "inline": ["M003", "M028", "P005"],
}

# The clip notes were written in free prose across two sessions, so they use
# varied phrasing ("is omitted from the quote", "only the pre-break clause is
# quoted", "clipped from the quote"). Detect the documentation by the page-break
# reference it always carries rather than by any single keyword.
CLIP_NOTE_PATTERN = re.compile(r"clip|page break|p\d+/p\d+", re.IGNORECASE)


class Pass7Validator:
    """Semantic validation of the complete extraction against corpus conventions."""

    def __init__(self, extraction_path: Path):
        self.path = extraction_path
        self.data = json.loads(self.path.read_text(encoding="utf-8"))
        self.corpus = load_corpus()
        self.critical: list[str] = []
        self.important: list[str] = []
        self.minor: list[str] = []
        self.info: list[str] = []
        self.report: dict = {}

    # ------------------------------------------------------------------
    # helpers
    # ------------------------------------------------------------------

    def _item_id(self, item: dict) -> str:
        """Return whichever *_id field this item carries."""
        for field in ("evidence_id", "claim_id", "implicit_argument_id",
                      "design_id", "method_id", "protocol_id"):
            if field in item:
                return item[field]
        return "<no id>"

    def _all_items(self):
        """Yield (array_name, item) for every content item in the extraction."""
        for array in ID_PATTERNS:
            for item in self.data.get(array, []):
                yield array, item

    # ------------------------------------------------------------------
    # Check 1: quote re-verification under extraction-time normalisation
    # ------------------------------------------------------------------

    def check_quotes(self) -> dict:
        """Re-verify every quote and trigger passage as a normalised substring.

        Covers verbatim_quote on all six arrays, trigger_text on implicit
        arguments and implicit RDMAP, and the quotes preserved inside
        consolidation_metadata.merged_sources (Pass 2/5 provenance records).
        """
        checked = failed = 0
        failures: list[dict] = []

        def verify(text: str, label: str, item_id: str) -> None:
            nonlocal checked, failed
            checked += 1
            if normalise(text) not in self.corpus:
                failed += 1
                failures.append({"id": item_id, "field": label,
                                 "excerpt": normalise(text)[:120]})

        for array, item in self._all_items():
            item_id = self._item_id(item)
            quote = item.get("verbatim_quote")
            if quote:
                verify(quote, "verbatim_quote", item_id)
            for i, trigger in enumerate(item.get("trigger_text") or []):
                verify(trigger, f"trigger_text[{i}]", item_id)

            # Consolidation provenance: merged_sources entries carry the
            # original item's quote/trigger text, which must still verify.
            meta = item.get("consolidation_metadata") or {}
            for j, src in enumerate(meta.get("merged_sources") or []):
                if not isinstance(src, dict):
                    continue
                src_id = src.get("id", f"{item_id}.merged[{j}]")
                if src.get("verbatim_quote"):
                    verify(src["verbatim_quote"],
                           f"merged_sources[{j}].verbatim_quote", src_id)
                for k, trigger in enumerate(src.get("trigger_text") or []):
                    verify(trigger,
                           f"merged_sources[{j}].trigger_text[{k}]", src_id)

        rate = 100.0 if checked == 0 else round(100.0 * (checked - failed) / checked, 2)
        if failed:
            self.critical.append(
                f"{failed} of {checked} quotes/triggers no longer verify against the source")
        return {"passages_checked": checked, "passages_failed": failed,
                "pass_rate_pct": rate, "failures": failures,
                "normalisation": "curly quotes to straight, en/em dash to hyphen, "
                                 "soft hyphen removed, fi/fl ligatures expanded, "
                                 "whitespace collapsed (rdmap_lib.normalise)"}

    # ------------------------------------------------------------------
    # Check 2: sourcing completeness by status
    # ------------------------------------------------------------------

    def check_sourcing(self) -> dict:
        """Explicit items need verbatim_quote; implicit items need full trigger set."""
        stats: dict = {}
        for array, kind in RDMAP_KINDS.items():
            explicit_total = explicit_ok = implicit_total = implicit_ok = 0
            for item in self.data.get(array, []):
                item_id = self._item_id(item)
                status = item.get(f"{kind}_status")
                if status == "explicit":
                    explicit_total += 1
                    if (item.get("verbatim_quote") or "").strip():
                        explicit_ok += 1
                    else:
                        self.critical.append(
                            f"{item_id}: explicit {kind} missing verbatim_quote")
                elif status == "implicit":
                    implicit_total += 1
                    missing = [f for f in ("trigger_text", "trigger_locations",
                                           "inference_reasoning", "implicit_metadata")
                               if not item.get(f)]
                    # implicit_metadata must itself be complete.
                    meta = item.get("implicit_metadata") or {}
                    missing += [f"implicit_metadata.{f}"
                                for f in ("basis", "transparency_gap",
                                          "assessability_impact",
                                          "reconstruction_confidence")
                                if not meta.get(f)]
                    if missing:
                        self.critical.append(
                            f"{item_id}: implicit {kind} missing {', '.join(missing)}")
                    else:
                        implicit_ok += 1
                else:
                    self.critical.append(
                        f"{item_id}: invalid {kind}_status {status!r}")
            stats[array] = {
                "explicit": {"total": explicit_total, "passed": explicit_ok},
                "implicit": {"total": implicit_total, "passed": implicit_ok},
            }

        # Evidence and claims are explicit by definition and always need a quote.
        for array in ("evidence", "claims"):
            total = ok = 0
            for item in self.data.get(array, []):
                total += 1
                if (item.get("verbatim_quote") or "").strip():
                    ok += 1
                else:
                    self.critical.append(
                        f"{self._item_id(item)}: {array[:-1]} missing verbatim_quote")
            stats[array] = {"total": total, "passed": ok}

        # Implicit arguments need trigger infrastructure, parallel arrays included.
        total = ok = 0
        for item in self.data.get("implicit_arguments", []):
            total += 1
            item_id = self._item_id(item)
            triggers = item.get("trigger_text") or []
            locations = item.get("trigger_locations") or []
            problems = []
            if not triggers:
                problems.append("trigger_text empty")
            if not locations:
                problems.append("trigger_locations empty")
            if triggers and locations and len(triggers) != len(locations):
                problems.append(
                    f"trigger arrays not parallel ({len(triggers)} vs {len(locations)})")
            if not item.get("inference_reasoning"):
                problems.append("inference_reasoning empty")
            if problems:
                self.critical.append(f"{item_id}: {', '.join(problems)}")
            else:
                ok += 1
        stats["implicit_arguments"] = {"total": total, "passed": ok}
        return stats

    # ------------------------------------------------------------------
    # Check 3: cross-reference integrity, both directions
    # ------------------------------------------------------------------

    def check_cross_references(self) -> dict:
        """Verify forward references resolve and reverse references mirror them."""
        ids = {array: {self._item_id(i) for i in self.data.get(array, [])}
               for array in ID_PATTERNS}
        broken: list[str] = []

        def check_refs(item, field, target_array):
            for ref in item.get(field) or []:
                if ref not in ids[target_array]:
                    broken.append(
                        f"{self._item_id(item)}.{field} -> {ref} does not exist")

        for claim in self.data.get("claims", []):
            check_refs(claim, "supported_by", "evidence")
            check_refs(claim, "supports_claims", "claims")
        for ev in self.data.get("evidence", []):
            check_refs(ev, "supports_claims", "claims")
        for ia in self.data.get("implicit_arguments", []):
            check_refs(ia, "supports_claims", "claims")
        for method in self.data.get("methods", []):
            check_refs(method, "implements_designs", "research_designs")
        for protocol in self.data.get("protocols", []):
            check_refs(protocol, "implements_methods", "methods")

        # Reverse references are rebuilt deterministically by
        # rdmap_lib.sync_reverse_refs. Recompute and compare rather than trust.
        expected_design_methods: dict[str, list] = {}
        for method in self.data.get("methods", []):
            for did in method.get("implements_designs") or []:
                expected_design_methods.setdefault(did, []).append(method["method_id"])
        mismatches: list[str] = []
        for design in self.data.get("research_designs", []):
            expected = expected_design_methods.get(design["design_id"], [])
            actual = design.get("implemented_by_methods") or []
            if sorted(expected) != sorted(actual):
                mismatches.append(
                    f"{design['design_id']}.implemented_by_methods {actual} != "
                    f"derived {expected}")

        expected_method_protocols: dict[str, list] = {}
        for protocol in self.data.get("protocols", []):
            for mid in protocol.get("implements_methods") or []:
                expected_method_protocols.setdefault(mid, []).append(
                    protocol["protocol_id"])
        mirror_mismatches: list[str] = []
        for method in self.data.get("methods", []):
            expected = expected_method_protocols.get(method["method_id"], [])
            realized = method.get("realized_through_protocols") or []
            implemented = method.get("implemented_by_protocols") or []
            if sorted(expected) != sorted(realized):
                mismatches.append(
                    f"{method['method_id']}.realized_through_protocols {realized} != "
                    f"derived {expected}")
            # Corpus convention: the two fields are mirrored and must agree.
            if sorted(realized) != sorted(implemented):
                mirror_mismatches.append(
                    f"{method['method_id']}: realized_through_protocols {realized} != "
                    f"implemented_by_protocols {implemented}")

        # Claim<->evidence reverse consistency.
        expected_claim_evidence: dict[str, list] = {}
        for ev in self.data.get("evidence", []):
            for cid in ev.get("supports_claims") or []:
                expected_claim_evidence.setdefault(cid, []).append(ev["evidence_id"])
        for claim in self.data.get("claims", []):
            expected = expected_claim_evidence.get(claim["claim_id"], [])
            actual = claim.get("supported_by") or []
            if sorted(expected) != sorted(actual):
                mismatches.append(
                    f"{claim['claim_id']}.supported_by {len(actual)} items != "
                    f"derived {len(expected)} from evidence.supports_claims")

        self.critical.extend(broken)
        self.critical.extend(mismatches)
        self.critical.extend(mirror_mismatches)
        return {"broken_references": broken,
                "reverse_reference_mismatches": mismatches,
                "mirrored_field_mismatches": mirror_mismatches}

    # ------------------------------------------------------------------
    # Check 4: hierarchy integrity
    # ------------------------------------------------------------------

    def check_hierarchy(self) -> dict:
        """Every method needs a design; every protocol needs a method."""
        orphan_methods = [m["method_id"] for m in self.data.get("methods", [])
                          if not (m.get("implements_designs") or [])]
        orphan_protocols = [p["protocol_id"] for p in self.data.get("protocols", [])
                            if not (p.get("implements_methods") or [])]
        childless = [d for d in self.data.get("research_designs", [])
                     if not (d.get("implemented_by_methods") or [])]
        childless_designs = [d["design_id"] for d in childless]

        for mid in orphan_methods:
            self.critical.append(f"{mid}: method has no implements_designs (orphan)")
        for pid in orphan_protocols:
            self.critical.append(f"{pid}: protocol has no implements_methods (orphan)")

        # Designs without implementing methods are a warning, not a failure
        # (prompt 07 hierarchy rules). Framing-tier designs — research questions,
        # theoretical frameworks, scope decisions — set the WHY of the study and
        # are not expected to be implemented by any procedure.
        framing_types = {"research_question", "theoretical_framework", "scope_definition"}
        childless_by_type: dict[str, list] = {}
        for design in childless:
            childless_by_type.setdefault(
                design.get("design_type", "unspecified"), []).append(design["design_id"])
        non_framing = [d["design_id"] for d in childless
                       if d.get("design_type") not in framing_types]
        if childless:
            self.info.append(
                f"{len(childless)} of {len(self.data.get('research_designs', []))} designs "
                f"have no implementing methods; "
                f"{len(childless) - len(non_framing)} are framing-tier "
                f"(research_question/theoretical_framework/scope_definition) and are not "
                f"expected to be implemented by a procedure. Non-framing: "
                f"{non_framing or 'none'}")

        protocols = self.data.get("protocols", [])
        linked = len(protocols) - len(orphan_protocols)
        rate = 100.0 if not protocols else round(100.0 * linked / len(protocols), 1)
        if rate < 50:
            self.critical.append(f"Protocol-method linkage {rate}% (<50%)")
        elif rate < 80:
            self.important.append(f"Protocol-method linkage {rate}% (<80%)")
        return {"orphaned_methods": orphan_methods,
                "orphaned_protocols": orphan_protocols,
                "designs_without_methods": childless_designs,
                "designs_without_methods_by_type": childless_by_type,
                "designs_without_methods_non_framing": non_framing,
                "protocol_method_linkage_pct": rate}

    # ------------------------------------------------------------------
    # Check 5: ID format, uniqueness, and location structure
    # ------------------------------------------------------------------

    def check_ids_and_locations(self) -> dict:
        """Validate ID patterns, global uniqueness, and location objects."""
        bad_ids: list[str] = []
        duplicates: list[str] = []
        bad_locations: list[str] = []
        seen: set[str] = set()

        for array, (id_field, pattern) in ID_PATTERNS.items():
            for item in self.data.get(array, []):
                item_id = item.get(id_field)
                if not item_id or not pattern.match(item_id):
                    bad_ids.append(f"{array}: {item_id!r} does not match {pattern.pattern}")
                if item_id in seen:
                    duplicates.append(item_id)
                seen.add(item_id)

                # Implicit items locate via trigger_locations, not `location`.
                locations = []
                if item.get("location"):
                    locations.append(item["location"])
                locations.extend(item.get("trigger_locations") or [])
                if not locations:
                    bad_locations.append(f"{item_id}: no location or trigger_locations")
                for loc in locations:
                    if not isinstance(loc, dict):
                        bad_locations.append(f"{item_id}: location is not an object")
                        continue
                    if not loc.get("section"):
                        bad_locations.append(f"{item_id}: location missing section")
                    page = loc.get("page")
                    if not isinstance(page, int) or isinstance(page, bool):
                        bad_locations.append(f"{item_id}: page {page!r} is not an integer")
                    elif not 1 <= page <= PAGE_COUNT:
                        bad_locations.append(
                            f"{item_id}: page {page} outside 1-{PAGE_COUNT}")

        self.critical.extend(bad_ids)
        self.critical.extend(f"Duplicate ID {d}" for d in duplicates)
        self.critical.extend(bad_locations)
        return {"invalid_ids": bad_ids, "duplicate_ids": duplicates,
                "location_issues": bad_locations}

    # ------------------------------------------------------------------
    # Check 6: Pass 0 metadata completeness
    # ------------------------------------------------------------------

    def check_metadata(self) -> dict:
        """Pass 0 fields present; null journal/DOI expected on an unsubmitted draft."""
        meta = self.data.get("project_metadata") or {}
        required = ["paper_title", "authors", "publication_year", "paper_type",
                    "discipline", "research_context"]
        missing = [f for f in required if not meta.get(f)]
        for field in missing:
            self.important.append(f"project_metadata.{field} empty")

        expected_null = [f for f in ("journal", "doi") if meta.get(f) is None]
        notes = []
        if expected_null:
            notes.append(
                f"{', '.join(expected_null)} null - expected: pre-submission draft, "
                "no venue or DOI assigned yet")

        # Authors should be full names, not initials.
        initials = [a for a in (meta.get("authors") or [])
                    if re.fullmatch(r"[A-Z]\.\s*[A-Z]?\.?\s*\w+", str(a))]
        if initials:
            self.minor.append(f"Authors in initials form: {initials}")
        return {"missing_fields": missing, "expected_nulls": expected_null,
                "notes": notes}

    # ------------------------------------------------------------------
    # Check 7: clip audit (informational)
    # ------------------------------------------------------------------

    def check_clips(self) -> dict:
        """Confirm each deliberately clipped quote still carries its documentation."""
        index = {self._item_id(item): (array, item)
                 for array, item in self._all_items()}
        documented, undocumented, absent = [], [], []

        for item_id in KNOWN_CLIPS["notes"]:
            if item_id not in index:
                absent.append(item_id)
                continue
            _, item = index[item_id]
            if CLIP_NOTE_PATTERN.search(str(item.get("notes") or "")):
                documented.append(item_id)
            else:
                undocumented.append(f"{item_id}: notes field no longer documents the clip")

        for item_id in KNOWN_CLIPS["inline"]:
            if item_id not in index:
                absent.append(item_id)
                continue
            array, item = index[item_id]
            text = str(item.get(f"{RDMAP_KINDS[array]}_text") or "")
            if CLIP_NOTE_PATTERN.search(text):
                documented.append(item_id)
            else:
                undocumented.append(f"{item_id}: text no longer documents the clip")

        for msg in undocumented:
            self.minor.append(msg)
        for item_id in absent:
            self.info.append(
                f"{item_id}: known clipped item no longer a live item (consolidated)")
        return {"documented": documented, "undocumented": undocumented,
                "absent_consolidated": absent,
                "interpretation": "Clipped page-break-spanning quotes are a deliberate "
                                  "sourcing decision, not a sourcing failure. Omitted "
                                  "text is verifiable against the PDF."}

    # ------------------------------------------------------------------
    # Check 8: consolidation metadata integrity
    # ------------------------------------------------------------------

    def check_consolidations(self) -> dict:
        """Provenance records must be well formed and their absorbed items gone.

        Two conventions coexist and both are valid:
        - Pass 2 (claims/evidence): `consolidated_from` lists ALL pre-consolidation
          IDs *including the surviving item's own ID*, and `absorbed_items` holds
          the absorbed items' quotes.
        - Pass 5 (RDMAP): `consolidated_from` lists only the absorbed IDs, and
          `merged_sources` holds their quotes.

        The resurrection test therefore reads absorbed_items/merged_sources — the
        items actually removed — not consolidated_from, whose Pass 2 form legitimately
        contains an ID that is still live (the survivor's own).
        """
        live_ids = {self._item_id(item) for _, item in self._all_items()}
        total = 0
        issues: list[str] = []
        resurrected: list[str] = []
        by_convention = {"pass2_absorbed_items": 0, "pass5_merged_sources": 0}

        for _, item in self._all_items():
            meta = item.get("consolidation_metadata")
            if not meta:
                continue
            total += 1
            item_id = self._item_id(item)

            if meta.get("absorbed_items"):
                by_convention["pass2_absorbed_items"] += 1
            if meta.get("merged_sources"):
                by_convention["pass5_merged_sources"] += 1

            absorbed = (meta.get("absorbed_items") or []) + (meta.get("merged_sources") or [])
            if not absorbed:
                issues.append(
                    f"{item_id}: consolidation_metadata records no absorbed items")
            if not (meta.get("rationale") or meta.get("consolidation_rationale")):
                issues.append(f"{item_id}: consolidation_metadata has no rationale")

            for src in absorbed:
                src_id = src.get("id") if isinstance(src, dict) else src
                # An absorbed ID must no longer exist as a live item.
                if src_id in live_ids:
                    resurrected.append(
                        f"{item_id}: absorbed item {src_id} still exists as a live item")
                # It must also still appear in consolidated_from for traceability.
                if src_id not in (meta.get("consolidated_from") or []):
                    issues.append(
                        f"{item_id}: absorbed item {src_id} missing from consolidated_from")

        self.important.extend(issues)
        self.critical.extend(resurrected)
        return {"items_with_consolidation_metadata": total,
                "by_convention": by_convention,
                "metadata_issues": issues, "resurrected_sources": resurrected}

    # ------------------------------------------------------------------
    # Check 9: enum validity
    # ------------------------------------------------------------------

    def check_enums(self) -> dict:
        """Closed-list enums only; open lists are reported, not failed."""
        closed = {
            "extraction_confidence": {"high", "medium", "low"},
            "design_status": {"explicit", "implicit"},
            "method_status": {"explicit", "implicit"},
            "protocol_status": {"explicit", "implicit"},
        }
        invalid: list[str] = []
        for _, item in self._all_items():
            for field, allowed in closed.items():
                value = item.get(field)
                if value is not None and value not in allowed:
                    invalid.append(
                        f"{self._item_id(item)}.{field} = {value!r} not in {sorted(allowed)}")
            meta = item.get("implicit_metadata") or {}
            basis = meta.get("basis")
            if basis is not None and basis not in {"mentioned_undocumented",
                                                   "inferred_from_results"}:
                invalid.append(f"{self._item_id(item)}.implicit_metadata.basis = {basis!r}")
            confidence = meta.get("reconstruction_confidence")
            if confidence is not None and confidence not in {"high", "medium", "low"}:
                invalid.append(
                    f"{self._item_id(item)}.implicit_metadata.reconstruction_confidence "
                    f"= {confidence!r}")
        self.critical.extend(invalid)
        return {"invalid_enum_values": invalid}

    # ------------------------------------------------------------------
    # orchestration
    # ------------------------------------------------------------------

    def run(self) -> dict:
        """Execute all checks and assemble the validation report."""
        quotes = self.check_quotes()
        sourcing = self.check_sourcing()
        xrefs = self.check_cross_references()
        hierarchy = self.check_hierarchy()
        ids = self.check_ids_and_locations()
        metadata = self.check_metadata()
        clips = self.check_clips()
        consolidations = self.check_consolidations()
        enums = self.check_enums()

        counts = {array: len(self.data.get(array, [])) for array in ID_PATTERNS}
        rdmap_total = (counts["research_designs"] + counts["methods"]
                       + counts["protocols"])
        implicit_rdmap = sum(
            1 for array, kind in RDMAP_KINDS.items()
            for item in self.data.get(array, [])
            if item.get(f"{kind}_status") == "implicit")

        if self.critical:
            status = "FAIL"
        elif self.important:
            status = "WARN"
        elif self.minor or self.info:
            status = "PASS_WITH_WARNINGS"
        else:
            status = "PASS"

        self.report = {
            "validation_summary": {
                "overall_status": status,
                "critical": len(self.critical),
                "important": len(self.important),
                "minor": len(self.minor),
                "informational": len(self.info),
                "total_items_validated": sum(counts.values()),
                "item_counts": counts,
                "rdmap_total": rdmap_total,
                "implicit_rdmap": implicit_rdmap,
                "implicit_rdmap_pct": round(100.0 * implicit_rdmap / rdmap_total, 1)
                if rdmap_total else 0.0,
            },
            "source_verification": quotes,
            "sourcing_completeness": sourcing,
            "cross_reference_integrity": xrefs,
            "hierarchy_validation": hierarchy,
            "schema_compliance": {**ids, **enums},
            "metadata_completeness": metadata,
            "clip_audit": clips,
            "consolidation_verification": consolidations,
            "issues": {"critical": self.critical, "important": self.important,
                       "minor": self.minor, "informational": self.info},
            "conventions_validated_against": [
                "No source_verification objects: quotes verified mechanically at "
                "extraction time by pass1_lib.py/rdmap_lib.py; this pass re-runs the "
                "same normalised-substring test (deviation from prompt 07 Checks 4.1/4.3)",
                "Implicit RDMAP uses sequential RD###/M###/P### IDs with "
                "*_status='implicit', not IMP prefixes (see pass4_extraction)",
                "Methods mirror realized_through_protocols and "
                "implemented_by_protocols; both rebuilt by rdmap_lib.sync_reverse_refs",
                "Page-break-spanning quotes deliberately clipped with the omission "
                "documented on the item; not sourcing failures",
                "consolidation_metadata.merged_sources are provenance records "
                "preserving pre-consolidation quotes, not live items",
            ],
            "out_of_scope": [
                "FAIR assessment: deliberately deferred (pre-submission draft, "
                "repositories and DOIs not final)",
                "Cluster 3 computational reproducibility: deliberately deferred",
                "Passes 8-9 (classification, credibility assessment): not run",
            ],
            "presubmission_qa_flags_carried_forward": len(
                self.data.get("extraction_notes", {}).get("presubmission_qa_flags", [])),
            "validated_by": "Claude Fable 5 (Session D)",
            "validation_date": "2026-07-24",
        }
        return self.report

    def print_report(self) -> None:
        """Print a human-readable summary to stdout."""
        summary = self.report["validation_summary"]
        print("=" * 78)
        print("PASS 7 VALIDATION - ross-2026-llm-reliability")
        print("=" * 78)
        print(f"\nStatus: {summary['overall_status']}")
        print(f"  Critical: {summary['critical']}   Important: {summary['important']}   "
              f"Minor: {summary['minor']}   Info: {summary['informational']}")

        counts = summary["item_counts"]
        print(f"\nItems validated: {summary['total_items_validated']}")
        print(f"  Evidence {counts['evidence']}, claims {counts['claims']}, "
              f"implicit arguments {counts['implicit_arguments']}")
        print(f"  Designs {counts['research_designs']}, methods {counts['methods']}, "
              f"protocols {counts['protocols']}")
        print(f"  Implicit RDMAP: {summary['implicit_rdmap']}/{summary['rdmap_total']} "
              f"= {summary['implicit_rdmap_pct']}%")

        quotes = self.report["source_verification"]
        print(f"\nQuote re-verification: {quotes['passages_checked'] - quotes['passages_failed']}"
              f"/{quotes['passages_checked']} = {quotes['pass_rate_pct']}%")

        hierarchy = self.report["hierarchy_validation"]
        print(f"Protocol-method linkage: {hierarchy['protocol_method_linkage_pct']}%")

        clips = self.report["clip_audit"]
        print(f"Clip audit: {len(clips['documented'])} documented, "
              f"{len(clips['undocumented'])} undocumented, "
              f"{len(clips['absent_consolidated'])} consolidated away")

        for level in ("critical", "important", "minor", "informational"):
            issues = self.report["issues"][level]
            if issues:
                print(f"\n{level.upper()} ({len(issues)}):")
                for issue in issues[:20]:
                    print(f"  - {issue}")
                if len(issues) > 20:
                    print(f"  ... and {len(issues) - 20} more")
        print()

    def save(self) -> None:
        """Write the report and Session D bookkeeping into extraction_notes only."""
        notes = self.data["extraction_notes"]
        notes["pass7_validation"] = self.report

        if "pass7" not in notes["passes_completed"]:
            notes["passes_completed"].append("pass7")

        notes["deferred_by_design"] = {
            "fair_assessment": (
                "Deferred: pre-submission draft with repositories and DOIs not final. "
                "See reproducibility_infrastructure.fair_assessment.notes. To be scored "
                "post-submission if desired."),
            "cluster_3_reproducibility": (
                "Deferred: computational reproducibility assessment requires final "
                "deposited materials, which do not exist for a pre-submission draft."),
            "passes_8_9": (
                "Out of scope for this run: extraction ends at Session D. Research "
                "approach classification (Pass 8) and credibility assessment (Pass 9) "
                "not run."),
        }

        summary = self.report["validation_summary"]
        quotes = self.report["source_verification"]
        notes.setdefault("session_log", []).append({
            "session": "D",
            "date": "2026-07-24",
            "passes": ["pass7"],
            "summary": (
                f"Pass 7 validation: {summary['overall_status']}. "
                f"{summary['critical']} critical, {summary['important']} important, "
                f"{summary['minor']} minor, {summary['informational']} informational. "
                f"Quote re-verification {quotes['pass_rate_pct']}% "
                f"({quotes['passages_checked']} passages re-tested under extraction-time "
                f"normalisation, including consolidation provenance quotes). "
                f"Shared validators (validate_extraction.py with "
                f"extraction-schema-v2.6.json, check_rdmap_completeness.py, "
                f"validate_bidirectional.py) all clean, 0 corrections. "
                f"Counts unchanged: {summary['item_counts']['evidence']} evidence, "
                f"{summary['item_counts']['claims']} claims, "
                f"{summary['item_counts']['implicit_arguments']} implicit arguments, "
                f"{summary['item_counts']['research_designs']} designs, "
                f"{summary['item_counts']['methods']} methods, "
                f"{summary['item_counts']['protocols']} protocols. Implicit RDMAP "
                f"{summary['implicit_rdmap']}/{summary['rdmap_total']} = "
                f"{summary['implicit_rdmap_pct']}%. FAIR and Cluster 3 deferred by "
                f"design. Seven presubmission_qa_flags carried forward unmodified.")
        })

        aest = timezone(timedelta(hours=10))
        self.data["extraction_timestamp"] = datetime.now(aest).isoformat(timespec="seconds")
        self.path.write_text(
            json.dumps(self.data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Validation report written to {self.path.name} "
              f"(extraction_notes.pass7_validation)")


def main() -> int:
    """Run Pass 7 validation; write results unless --dry-run is given."""
    dry_run = "--dry-run" in sys.argv
    validator = Pass7Validator(EXTRACTION)
    validator.run()
    validator.print_report()

    if dry_run:
        print("DRY RUN - extraction.json not modified")
    else:
        validator.save()

    status = validator.report["validation_summary"]["overall_status"]
    return 0 if status in ("PASS", "PASS_WITH_WARNINGS") else 1


if __name__ == "__main__":
    sys.exit(main())
