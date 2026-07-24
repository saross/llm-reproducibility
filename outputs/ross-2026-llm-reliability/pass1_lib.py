#!/usr/bin/env python3
"""Shared helper for Pass 1 section-group extraction scripts (ross-2026-llm-reliability).

Enforces 100% sourcing discipline mechanically: every verbatim_quote and every
trigger_text passage is verified against the page-anchored markdown source before
any item is committed to extraction.json. A failed verification aborts the whole
group save so partial writes cannot occur.

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
    return errors


def save_group(group_meta: dict, evidence: list = (), claims: list = (),
               implicit_arguments: list = ()) -> None:
    """Verify sourcing, then append items and section metadata to extraction.json."""
    corpus = load_corpus()
    errors = (
        verify_quotes(list(evidence), corpus, "evidence")
        + verify_quotes(list(claims), corpus, "claim")
        + verify_quotes(list(implicit_arguments), corpus, "implicit_argument")
    )
    if errors:
        print("SOURCING VERIFICATION FAILED — nothing saved:")
        for e in errors:
            print(f"  ✗ {e}")
        sys.exit(1)

    data = json.loads(EXTRACTION.read_text(encoding="utf-8"))

    # Reject duplicate IDs across the whole document.
    existing = {
        item[f"{kind}_id"]
        for kind, key in (
            ("evidence", "evidence"), ("claim", "claims"),
            ("implicit_argument", "implicit_arguments"),
        )
        for item in data[key]
    }
    new_ids = (
        [e["evidence_id"] for e in evidence]
        + [c["claim_id"] for c in claims]
        + [a["implicit_argument_id"] for a in implicit_arguments]
    )
    dupes = [i for i in new_ids if i in existing]
    if dupes or len(new_ids) != len(set(new_ids)):
        print(f"DUPLICATE IDs — nothing saved: {dupes or 'within-batch duplicate'}")
        sys.exit(1)

    data["evidence"].extend(evidence)
    data["claims"].extend(claims)
    data["implicit_arguments"].extend(implicit_arguments)

    notes = data["extraction_notes"]
    notes.setdefault("section_extracted", []).append(group_meta | {
        "items_extracted": {
            "evidence": len(evidence),
            "claims": len(claims),
            "implicit_arguments": len(implicit_arguments),
        }
    })
    aest = timezone(timedelta(hours=10))
    data["extraction_timestamp"] = datetime.now(aest).isoformat(timespec="seconds")

    EXTRACTION.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n",
                          encoding="utf-8")
    print(f"Saved {group_meta['group']}: +{len(evidence)} evidence, "
          f"+{len(claims)} claims, +{len(implicit_arguments)} implicit_arguments")
    print(f"Totals: evidence={len(data['evidence'])}, claims={len(data['claims'])}, "
          f"implicit_arguments={len(data['implicit_arguments'])}")
