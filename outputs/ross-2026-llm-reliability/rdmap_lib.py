#!/usr/bin/env python3
"""Shared helper for Pass 3/4 RDMAP extraction scripts (ross-2026-llm-reliability).

Adapted from pass1_lib.py (Session B). Enforces 100% sourcing discipline
mechanically: every verbatim_quote and every trigger_text passage is verified
against the page-anchored markdown source before any item is committed to
extraction.json. A failed verification aborts the whole group save so partial
writes cannot occur.

Additional RDMAP-specific checks:
- duplicate-ID rejection across research_designs, methods, and protocols;
- forward cross-reference validation (methods.implements_designs and
  protocols.implements_methods must point at IDs that exist after the save);
- deterministic reverse-reference sync: research_designs.implemented_by_methods,
  methods.realized_through_protocols, and methods.implemented_by_protocols are
  rebuilt from the forward references on every save, so the document is always
  bidirectionally consistent (Phase 5b then verifies rather than repairs).

Normalisation mirrors the processed-md pipeline (normalise_for_matching): curly
quotes to straight, en/em dashes to hyphen, whitespace runs collapsed. Words are
never altered, so verification remains a strict substring test on normalised text.
"""

import json
import re
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

BASE = Path(__file__).resolve().parent
EXTRACTION = BASE / "extraction.json"
MD_SOURCE = (
    BASE.parent.parent / "input" / "sources" / "processed-md" / "ross-2026-llm-reliability.md"
)


def normalise(text: str) -> str:
    """Normalise text for quote matching (whitespace, dashes, quote marks)."""
    text = (
        text.replace("‘", "'").replace("’", "'")
        .replace("“", '"').replace("”", '"')
        .replace("–", "-").replace("—", "-")
        .replace("­", "")  # soft hyphen
        .replace("ﬁ", "fi").replace("ﬂ", "fl")  # ligatures
    )
    return re.sub(r"\s+", " ", text).strip()


def load_corpus() -> str:
    """Load the page-anchored markdown, normalised for matching."""
    return normalise(MD_SOURCE.read_text(encoding="utf-8"))


def verify_quotes(items: list, corpus: str, kind: str) -> list:
    """Return a list of error strings for any unverifiable quote/trigger text."""
    errors = []
    for item in items:
        item_id = item.get(f"{kind}_id", "?")
        quote = item.get("verbatim_quote")
        if quote is not None and normalise(quote) not in corpus:
            errors.append(f"{item_id}: verbatim_quote NOT FOUND in source")
        for i, trigger in enumerate(item.get("trigger_text", [])):
            if normalise(trigger) not in corpus:
                errors.append(f"{item_id}: trigger_text[{i}] NOT FOUND in source")
        status = item.get(f"{kind}_status")
        if status == "explicit" and not quote:
            errors.append(f"{item_id}: explicit item missing verbatim_quote")
        if status == "implicit" and not item.get("trigger_text"):
            errors.append(f"{item_id}: implicit item missing trigger_text")
    return errors


def sync_reverse_refs(data: dict) -> None:
    """Rebuild RDMAP reverse references deterministically from forward references.

    Forward references (the single source of truth during Passes 3-4):
    - methods[].implements_designs   -> research_designs[].implemented_by_methods
    - protocols[].implements_methods -> methods[].realized_through_protocols
                                        and methods[].implemented_by_protocols
    """
    design_methods: dict[str, list] = {}
    for method in data["methods"]:
        for did in method.get("implements_designs", []):
            design_methods.setdefault(did, []).append(method["method_id"])
    for design in data["research_designs"]:
        design["implemented_by_methods"] = design_methods.get(design["design_id"], [])

    method_protocols: dict[str, list] = {}
    for protocol in data["protocols"]:
        for mid in protocol.get("implements_methods", []):
            method_protocols.setdefault(mid, []).append(protocol["protocol_id"])
    for method in data["methods"]:
        pids = method_protocols.get(method["method_id"], [])
        method["realized_through_protocols"] = pids
        method["implemented_by_protocols"] = list(pids)


def save_group(group_meta: dict, research_designs: list = (), methods: list = (),
               protocols: list = (), notes_key: str = "pass3_section_extracted") -> None:
    """Verify sourcing, then append RDMAP items and section metadata to extraction.json."""
    corpus = load_corpus()
    errors = (
        verify_quotes(list(research_designs), corpus, "design")
        + verify_quotes(list(methods), corpus, "method")
        + verify_quotes(list(protocols), corpus, "protocol")
    )
    if errors:
        print("SOURCING VERIFICATION FAILED — nothing saved:")
        for e in errors:
            print(f"  ✗ {e}")
        sys.exit(1)

    data = json.loads(EXTRACTION.read_text(encoding="utf-8"))

    # Reject duplicate IDs across the three RDMAP arrays.
    existing = (
        {d["design_id"] for d in data["research_designs"]}
        | {m["method_id"] for m in data["methods"]}
        | {p["protocol_id"] for p in data["protocols"]}
    )
    new_ids = (
        [d["design_id"] for d in research_designs]
        + [m["method_id"] for m in methods]
        + [p["protocol_id"] for p in protocols]
    )
    dupes = [i for i in new_ids if i in existing]
    if dupes or len(new_ids) != len(set(new_ids)):
        print(f"DUPLICATE IDs — nothing saved: {dupes or 'within-batch duplicate'}")
        sys.exit(1)

    # Validate forward cross-references against the post-save ID space.
    design_ids = {d["design_id"] for d in data["research_designs"]} | {
        d["design_id"] for d in research_designs
    }
    method_ids = {m["method_id"] for m in data["methods"]} | {
        m["method_id"] for m in methods
    }
    ref_errors = []
    for method in methods:
        for did in method.get("implements_designs", []):
            if did not in design_ids:
                ref_errors.append(f"{method['method_id']}: implements_designs -> {did} missing")
    for protocol in protocols:
        for mid in protocol.get("implements_methods", []):
            if mid not in method_ids:
                ref_errors.append(f"{protocol['protocol_id']}: implements_methods -> {mid} missing")
    if ref_errors:
        print("CROSS-REFERENCE VALIDATION FAILED — nothing saved:")
        for e in ref_errors:
            print(f"  ✗ {e}")
        sys.exit(1)

    data["research_designs"].extend(research_designs)
    data["methods"].extend(methods)
    data["protocols"].extend(protocols)
    sync_reverse_refs(data)

    notes = data["extraction_notes"]
    notes.setdefault(notes_key, []).append(group_meta | {
        "items_extracted": {
            "research_designs": len(research_designs),
            "methods": len(methods),
            "protocols": len(protocols),
        }
    })
    aest = timezone(timedelta(hours=10))
    data["extraction_timestamp"] = datetime.now(aest).isoformat(timespec="seconds")

    EXTRACTION.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n",
                          encoding="utf-8")
    print(f"Saved {group_meta['group']}: +{len(research_designs)} designs, "
          f"+{len(methods)} methods, +{len(protocols)} protocols")
    print(f"Totals: research_designs={len(data['research_designs'])}, "
          f"methods={len(data['methods'])}, protocols={len(data['protocols'])}")
