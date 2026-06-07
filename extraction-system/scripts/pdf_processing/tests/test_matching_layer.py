#!/usr/bin/env python3
"""
Golden tests for the matching-grade extraction layer (added 2026-06-07).

Covers:
  * normalise_for_matching / normalise_text_readable (E1)
  * PDFExtractor.extract_pages locator round-trip (E2)
  * promoted utilities: strip_running_headers, drop_fragment_headings,
    split_body_references, strip_affiliation_tail (P1-P4)

Dependency-free: the string tests run under any Python 3 (stdlib only). The
extract_pages round-trip test auto-skips if PyMuPDF (fitz) is unavailable.
Runs either under pytest (functions named test_*) or directly as a script:

    python test_matching_layer.py
"""

import sys
from pathlib import Path

# Make the pdf_processing package importable when run directly.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pdf_cleaner as C  # noqa: E402


# --- E1: normalise_for_matching / normalise_text_readable -------------------

def test_ligatures():
    # ﬃ (U+FB03), ﬁ (U+FB01)
    assert C.normalise_for_matching("oﬃce ﬁle") == "office file"


def test_smart_quotes_and_apostrophe():
    assert C.normalise_for_matching("“it’s”") == '"it\'s"'


def test_dehyphenation_lowercase():
    assert C.normalise_for_matching("archaeo-\nlogy") == "archaeology"


def test_dehyphenation_before_capital_preserved():
    # capital after the break => not joined (conservative); newline -> space
    assert C.normalise_for_matching("well-\nKnown") == "well- Known"


def test_whitespace_collapse():
    assert C.normalise_for_matching("a   b\n\nc\td e") == "a b c d e"


def test_en_em_dash_preserved():
    assert C.normalise_for_matching("a — b – c") == "a — b – c"


def test_soft_hyphen_and_zero_width_removed():
    assert C.normalise_for_matching("co­oper​ate") == "cooperate"


def test_empty():
    assert C.normalise_for_matching("") == ""
    assert C.normalise_text_readable("") == ""


def test_matching_idempotent():
    samples = [
        "oﬃce ﬁle", "archaeo-\nlogy", "“quote”  spaced\ttabs",
        "multi\n\n\npara", "well-\nKnown", "a — b",
    ]
    for s in samples:
        once = C.normalise_for_matching(s)
        assert C.normalise_for_matching(once) == once, repr(s)


def test_readable_preserves_paragraphs():
    out = C.normalise_text_readable("para one\nline two\n\n\npara two")
    assert out == "para one\nline two\n\npara two"


def test_readable_idempotent():
    s = "ﬁne  text\nwith-\nbreak\n\n\ngap"
    once = C.normalise_text_readable(s)
    assert C.normalise_text_readable(once) == once


def test_matching_substring_roundtrip():
    # ligature + line-break hyphenation in the source; plain quote should match.
    src = C.normalise_for_matching("The ﬁndings were sig-\nnificant across sites.")
    quote = C.normalise_for_matching("findings were significant")
    assert quote in src


# --- P1-P4: promoted utilities ---------------------------------------------

def test_strip_running_headers():
    header = "Journal of Things, Vol 12 (2024), pp. 1-20"
    md = "\n".join([header] * 5 + ["Real body text that is long enough to keep."])
    cleaned, n = C.strip_running_headers(md)
    assert n == 5
    assert "Journal of Things" not in cleaned
    assert "Real body text" in cleaned


def test_strip_running_headers_keeps_rare_lines():
    md = "A unique long sentence that appears only once here.\nAnother distinct long line."
    cleaned, n = C.strip_running_headers(md)
    assert n == 0
    assert cleaned == md


def test_drop_fragment_headings():
    md = "## JD\n\n## Introduction\n\n## A1B2C3D4\n\nbody text"
    cleaned, n = C.drop_fragment_headings(md)
    assert "## Introduction" in cleaned   # whitelisted single word kept
    assert "## JD" not in cleaned         # 1-word fragment dropped
    assert "## A1B2C3D4" not in cleaned   # DOI-ish fragment dropped
    assert n == 2


def test_drop_fragment_headings_keeps_real_titles():
    md = "## 3.2 Methods and Materials\n\n## AUTHOR AFFILIATIONS\n\n## Data\n\nbody"
    cleaned, n = C.drop_fragment_headings(md)
    assert "## 3.2 Methods and Materials" in cleaned
    assert "## AUTHOR AFFILIATIONS" in cleaned
    assert "## Data" in cleaned
    assert n == 0


def test_split_body_references_strict_heading():
    md = "Body text here.\n\n## References\n\nSmith, J. (2020). A paper. Journal."
    body, refs, method = C.split_body_references(md)
    assert method == "strict-heading"
    assert "Body text here." in body
    assert "Smith, J. (2020)" in refs


def test_split_body_references_none():
    md = "Just a body with no reference section at all."
    body, refs, method = C.split_body_references(md)
    assert method == "no-references-heading-found"
    assert refs == ""
    assert body == md.strip()


def test_strip_affiliation_tail():
    md = "Body conclusion.\n\n## Author Affiliations\n\nDept of X, University of Y."
    cleaned, n = C.strip_affiliation_tail(md)
    assert "Author Affiliations" not in cleaned
    assert "Body conclusion." in cleaned
    assert n > 0


# --- E2: extract_pages round-trip (PDF; skipped without fitz) ----------------

def test_extract_pages_roundtrip():
    try:
        import fitz  # noqa: F401
    except Exception:
        print("SKIP test_extract_pages_roundtrip (PyMuPDF not installed)")
        return
    import fitz
    import extract_pdf_text as E

    doc = fitz.open()
    doc.new_page().insert_text((72, 72), "Alpha page one unique phrase here.")
    doc.new_page().insert_text((72, 72), "Beta page two distinct marker here.")
    tmp = Path("/tmp/_test_extract_pages_matching.pdf")
    doc.save(str(tmp))
    doc.close()

    try:
        pages = E.PDFExtractor().extract_pages(tmp)
        assert len(pages) == 2
        assert [p["page_index"] for p in pages] == [0, 1]
        assert C.normalise_for_matching("page one unique phrase") in \
            C.normalise_for_matching(pages[0]["text"])
        assert C.normalise_for_matching("page two distinct marker") in \
            C.normalise_for_matching(pages[1]["text"])
        # a phrase from page 1 must NOT match page 0 (locator integrity)
        assert C.normalise_for_matching("distinct marker") not in \
            C.normalise_for_matching(pages[0]["text"])
    finally:
        tmp.unlink(missing_ok=True)
    print("test_extract_pages_roundtrip OK")


# --- runner (no pytest dependency) ------------------------------------------

def _run() -> int:
    fns = [v for k, v in sorted(globals().items())
           if k.startswith("test_") and callable(v)]
    failed = 0
    for fn in fns:
        try:
            fn()
            print(f"PASS {fn.__name__}")
        except AssertionError as exc:
            failed += 1
            print(f"FAIL {fn.__name__}: {exc}")
    print(f"\n{len(fns) - failed}/{len(fns)} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(_run())
