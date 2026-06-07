"""
PDF Text Cleaning Utilities

Functions to clean and normalize text extracted from academic PDFs.
Optimized for preparing text for LLM analysis.
"""

import collections
import re
import unicodedata
from typing import List, Tuple


def remove_hyphenation(text: str) -> str:
    """
    Fix hyphenation across line breaks.

    Example: 'archaeo-\nlogy' -> 'archaeology'

    Args:
        text: Raw text with potential hyphenation

    Returns:
        Text with hyphenation fixed
    """
    # Remove hyphens at end of lines followed by lowercase letter
    text = re.sub(r'-\s*\n\s*([a-z])', r'\1', text)
    return text


def remove_page_numbers(text: str) -> str:
    """
    Remove standalone page numbers (common patterns).

    Args:
        text: Text potentially containing page numbers

    Returns:
        Text with page numbers removed
    """
    # Remove lines that are just page numbers
    text = re.sub(r'^\s*\d+\s*$', '', text, flags=re.MULTILINE)
    # Remove page numbers at start/end of lines
    text = re.sub(r'^\d+\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\s+\d+$', '', text, flags=re.MULTILINE)
    return text


def clean_whitespace(text: str) -> str:
    """
    Normalize whitespace while preserving paragraph breaks.

    Args:
        text: Text with irregular whitespace

    Returns:
        Text with normalized whitespace
    """
    # Replace multiple spaces with single space
    text = re.sub(r' +', ' ', text)
    # Replace 3+ newlines with 2 (preserve paragraph breaks)
    text = re.sub(r'\n{3,}', '\n\n', text)
    # Remove spaces at start/end of lines
    text = re.sub(r'^ +', '', text, flags=re.MULTILINE)
    text = re.sub(r' +$', '', text, flags=re.MULTILINE)
    return text


def remove_headers_footers(blocks: List[dict], page_height: float,
                           header_threshold: float = 0.1,
                           footer_threshold: float = 0.9) -> List[dict]:
    """
    Filter out text blocks likely to be headers or footers.

    Args:
        blocks: List of text blocks with bbox coordinates
        page_height: Height of the page
        header_threshold: Top % of page to consider header (0.0-1.0)
        footer_threshold: Bottom % of page to consider footer (0.0-1.0)

    Returns:
        Filtered list of text blocks
    """
    filtered = []
    header_y = page_height * header_threshold
    footer_y = page_height * footer_threshold

    for block in blocks:
        if 'bbox' in block:
            y0, y1 = block['bbox'][1], block['bbox'][3]
            # Skip if entirely in header or footer region
            if y1 < header_y or y0 > footer_y:
                continue
        filtered.append(block)

    return filtered


def detect_section_heading(text: str, font_size: float = None,
                           avg_font_size: float = None) -> bool:
    """
    Heuristic to detect if text is likely a section heading.

    Args:
        text: Text to check
        font_size: Font size of this text
        avg_font_size: Average font size in document

    Returns:
        True if likely a heading
    """
    if not text or len(text) > 200:  # Headings are typically short
        return False

    # Check for numbered sections (1., 1.1, etc.)
    if re.match(r'^\d+\.(\d+\.)*\s+[A-Z]', text):
        return True

    # Check if all caps (but not too long)
    if text.isupper() and len(text) < 100:
        return True

    # Check if starts with capital and ends without punctuation
    if text[0].isupper() and not text.rstrip().endswith(('.', '!', '?', ',')):
        # Check font size if available
        if font_size and avg_font_size and font_size > avg_font_size * 1.1:
            return True

    return False


def format_as_markdown_heading(text: str, level: int = 2) -> str:
    """
    Format text as Markdown heading.

    Args:
        text: Heading text
        level: Heading level (1-6)

    Returns:
        Markdown-formatted heading
    """
    level = max(1, min(6, level))  # Clamp to 1-6
    return f"\n\n{'#' * level} {text.strip()}\n\n"


def remove_common_artifacts(text: str) -> str:
    """
    Remove common PDF extraction artifacts.

    Args:
        text: Raw extracted text

    Returns:
        Cleaned text
    """
    # Remove form feed characters
    text = text.replace('\f', '\n\n')

    # Remove soft hyphens
    text = text.replace('\u00ad', '')

    # Remove zero-width spaces
    text = text.replace('\u200b', '')

    # Remove bullet point characters that don't render well
    text = text.replace('•', '- ')
    text = text.replace('◦', '  - ')

    return text


def extract_abstract(text: str) -> Tuple[str, str]:
    """
    Attempt to extract abstract from text.

    Args:
        text: Full document text

    Returns:
        Tuple of (abstract_text, remaining_text)
    """
    # Look for abstract section
    patterns = [
        r'ABSTRACT\s*\n+(.*?)\n+(?:1\.|Introduction|INTRODUCTION)',
        r'Abstract\s*\n+(.*?)\n+(?:1\.|Introduction|INTRODUCTION)',
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
        if match:
            abstract = match.group(1).strip()
            # Remove the abstract from the main text
            remaining = text[:match.start()] + text[match.end():]
            return abstract, remaining

    return "", text


def clean_reference_section(text: str) -> str:
    """
    Clean up references section for better formatting.

    Args:
        text: Text containing references

    Returns:
        Cleaned references text
    """
    # Ensure each reference starts on a new line
    # Look for patterns like "Author, A. (year)"
    text = re.sub(r'([.!?])\s+([A-Z][a-z]+,\s+[A-Z]\.)', r'\1\n\2', text)

    return text


def reconstruct_paragraphs(text: str) -> str:
    """
    Reconstruct paragraphs that may have been broken by PDF extraction.

    Lines ending with lowercase letters or commas likely continue to next line.

    Args:
        text: Text with potentially broken paragraphs

    Returns:
        Text with reconstructed paragraphs
    """
    lines = text.split('\n')
    reconstructed = []
    current_para = []

    for line in lines:
        line = line.strip()
        if not line:
            # Empty line - end of paragraph
            if current_para:
                reconstructed.append(' '.join(current_para))
                current_para = []
            reconstructed.append('')
        else:
            current_para.append(line)
            # Check if this line ends a sentence
            if line.endswith(('.', '!', '?', ':', ';')) or detect_section_heading(line):
                reconstructed.append(' '.join(current_para))
                current_para = []

    # Add any remaining paragraph
    if current_para:
        reconstructed.append(' '.join(current_para))

    return '\n'.join(reconstructed)


def clean_extracted_text(text: str, aggressive: bool = False) -> str:
    """
    Apply all cleaning operations to extracted text.

    Args:
        text: Raw extracted text
        aggressive: If True, apply more aggressive cleaning

    Returns:
        Cleaned text optimized for LLM input
    """
    # Basic cleaning
    text = remove_common_artifacts(text)
    text = remove_hyphenation(text)
    text = remove_page_numbers(text)

    if aggressive:
        # More aggressive cleaning for complex PDFs
        text = reconstruct_paragraphs(text)

    # Final whitespace normalization
    text = clean_whitespace(text)

    return text.strip()


# ===========================================================================
# Matching-grade normalisation (added 2026-06-07)
#
# Some consumers (e.g. an annotated-bibliography pipeline that extracts quotes
# and later verifies them against the source) need text in a *canonical* form,
# so that a quoted span matches its source iff it is genuinely present. Two
# forms are provided, sharing identical character-level cleanup:
#
#   * ``normalise_text_readable``  — character-normalised + dehyphenated, with
#     line/paragraph structure preserved. What a reader/LLM quotes FROM.
#   * ``normalise_for_matching``   — the comparison KEY: same cleanup but ALL
#     whitespace collapsed to single spaces, so matching is whitespace-
#     insensitive. A quote Q is present in page text T iff
#     ``normalise_for_matching(Q) in normalise_for_matching(T)``.
#
# Both are deterministic and idempotent (``f(f(x)) == f(x)``) and case-
# preserving. Existing behaviour of ``clean_extracted_text`` / ``extract`` is
# unchanged — these are additive, opt-in helpers.
# ===========================================================================

# Presentation-form ligatures -> ASCII. NFKC already maps U+FB00-FB06, but the
# explicit map is a belt-and-braces guard (idempotent: targets are gone after
# the first pass).
_LIGATURES = {
    "ﬀ": "ff", "ﬁ": "fi", "ﬂ": "fl",
    "ﬃ": "ffi", "ﬄ": "ffl", "ﬅ": "ft", "ﬆ": "st",
}

# Smart quotes / apostrophes / primes -> ASCII.
_QUOTE_MAP = {
    "‘": "'", "’": "'", "‚": "'", "‛": "'", "′": "'",
    "“": '"', "”": '"', "„": '"', "‟": '"', "″": '"',
    "´": "'", "`": "'",
}

# Hyphen-like variants -> ASCII hyphen-minus. En dash (U+2013) and em dash
# (U+2014) are deliberately LEFT INTACT: they are semantic punctuation that the
# extractor preserves consistently, and collapsing them would corrupt the text
# of displayed quotations.
_HYPHEN_MAP = {
    "‐": "-", "‑": "-", "‒": "-", "−": "-",
}

# Zero-width / invisible characters to drop outright.
_ZERO_WIDTH = ["­", "​", "‌", "‍", "﻿"]


def _apply_char_normalisation(text: str) -> str:
    """Character-level canonicalisation shared by both matching forms.

    NFKC, then ligature / quote / hyphen maps and zero-width removal, plus
    form-feed -> newline. Idempotent.
    """
    text = unicodedata.normalize("NFKC", text)
    for src, dst in _LIGATURES.items():
        text = text.replace(src, dst)
    for src, dst in _QUOTE_MAP.items():
        text = text.replace(src, dst)
    for src, dst in _HYPHEN_MAP.items():
        text = text.replace(src, dst)
    for ch in _ZERO_WIDTH:
        text = text.replace(ch, "")
    text = text.replace("\f", "\n")
    return text


def _dehyphenate(text: str) -> str:
    """Join words split by an end-of-line hyphen before a lowercase letter.

    ``'archaeo-\\nlogy' -> 'archaeology'``. Conservative: only a lowercase
    letter triggers the join, so a hyphenated compound broken before a capital
    (``'well-\\nKnown'``) is left intact rather than mis-joined.
    """
    return re.sub(r"-\s*\n\s*([a-z])", r"\1", text)


def normalise_text_readable(text: str) -> str:
    """Readable canonical text: character-normalised + dehyphenated, with
    paragraph structure preserved (intra-line whitespace collapsed, blank-line
    runs capped at one). This is the text a quote is taken FROM.

    Deterministic and idempotent.
    """
    if not text:
        return ""
    text = _apply_char_normalisation(text)
    text = _dehyphenate(text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r" *\n *", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def normalise_for_matching(text: str) -> str:
    """Canonical comparison key for verifying a quote against its source.

    Same character-level cleanup as :func:`normalise_text_readable`, but
    collapses ALL whitespace (including newlines) to single spaces so matching
    is whitespace-insensitive. Use as:
    ``normalise_for_matching(quote) in normalise_for_matching(page_text)``.

    Deterministic, idempotent, case-preserving.
    """
    if not text:
        return ""
    text = _apply_char_normalisation(text)
    text = _dehyphenate(text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


# ===========================================================================
# Promoted from the style-analyser wrapper (2026-06-07)
#
# Generic, academic-paper-oriented cleanup that was developed in
# personal-assistant/scripts/style-analyser/extract_corpus.py and belongs in
# the canonical extractor. All opt-in: nothing here is wired into the default
# extract() pipeline, so existing consumers are behaviourally unchanged.
# ===========================================================================

# Single-word section headings that are legitimate (whitelist for the
# fragment-heading dropper). All lower-case for comparison.
SECTION_WORDS = frozenset({
    "abstract", "introduction", "methods", "methodology", "results",
    "discussion", "conclusion", "conclusions", "bibliography", "references",
    "acknowledgements", "acknowledgments", "funding", "background",
    "materials", "procedure", "findings", "implications", "limitations",
    "summary", "appendix", "appendices", "preface", "foreword", "epilogue",
    "afterword", "notes", "footnotes", "endnotes", "glossary", "index",
    "preliminaries", "data", "supplementary", "overview", "scope",
})


def strip_running_headers(markdown: str, min_chars: int = 15,
                          min_occurrences: int = 4) -> Tuple[str, int]:
    """Strip lines that appear verbatim many times (PDF running headers).

    PyMuPDF / pdfplumber preserve journal running headers, chapter running
    titles, and other per-page boilerplate, which the section detector may
    H2-promote. A line of >= ``min_chars`` chars appearing >= ``min_occurrences``
    times verbatim is almost always such boilerplate (genuine repeated section
    headings are short and handled by :func:`drop_fragment_headings`).

    Returns ``(cleaned_markdown, n_lines_stripped)``. Repeat-based, so it
    catches boilerplate regardless of page position (unlike the geometric
    :func:`remove_headers_footers`).
    """
    lines = markdown.split("\n")

    def normalise(line: str) -> str:
        return line.strip().lstrip("#").strip()

    counts: "collections.Counter[str]" = collections.Counter()
    for line in lines:
        key = normalise(line)
        if len(key) >= min_chars:
            counts[key] += 1

    repeating = {k for k, c in counts.items() if c >= min_occurrences}
    if not repeating:
        return markdown, 0

    n_stripped = 0
    kept = []
    for line in lines:
        if normalise(line) in repeating:
            n_stripped += 1
            continue
        kept.append(line)
    cleaned = "\n".join(kept)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned, n_stripped


def drop_fragment_headings(markdown: str) -> Tuple[str, int]:
    """Drop H1-H6 lines whose text is a 1-2 word fragment.

    The section detector aggressively promotes title-case or all-caps lines to
    headings; on PDFs with rich masthead typography this explodes the heading
    count with fragments such as ``## JD`` (running header), ``## Z.,`` (broken
    reference initial), ``## (AI)`` (parenthetical), or a DOI fragment. These
    are not section structure.

    Keeps: numbered headings (``1.``, ``3.2``, ``A.1 Methods``); whitelisted
    single-word section names (see :data:`SECTION_WORDS`); 2-word all-caps
    labels (``AUTHOR AFFILIATIONS``); 3+ word headings. Drops the rest.

    Returns ``(cleaned_markdown, n_headings_dropped)``.
    """
    n_dropped = 0

    def maybe_drop(match: "re.Match") -> str:
        nonlocal n_dropped
        text = match.group(2).strip()
        words = text.split()
        if re.match(r"^([A-Z]?\d+)(\.\d+)*\.?\s+\S", text):  # numbered section
            return match.group(0)
        if len(words) >= 3:                                  # real titles
            return match.group(0)
        if len(words) == 2 and text.isupper():               # AUTHOR AFFILIATIONS
            return match.group(0)
        if words:
            first = words[0].lower().rstrip(":.,;").strip("()")
            if first in SECTION_WORDS:
                return match.group(0)
        n_dropped += 1
        return ""

    cleaned = re.sub(r"^(#{1,6})\s+(.+)$", maybe_drop, markdown, flags=re.MULTILINE)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned, n_dropped


# --- Body / references split -------------------------------------------------

_REF_HEADING_RE = re.compile(
    r"^\s{0,3}(#{1,4})\s+("
    r"REFERENCES?|References?|"
    r"BIBLIOGRAPHY|Bibliography|"
    r"WORKS\s+CITED|Works\s+Cited|"
    r"LITERATURE\s+CITED|Literature\s+Cited|"
    r"REFERENCES\s+CITED|References\s+Cited"
    r")\s*$",
    re.MULTILINE,
)

_REF_HEADING_LOOSE_RE = re.compile(
    r"^\s{0,3}(#{1,4})\s+(References?|Bibliography|Works\s+Cited).*$",
    re.MULTILINE | re.IGNORECASE,
)

_REF_PARAGRAPH_RE = re.compile(
    r"(?:^|\n)\s*(References?|Bibliography|Works\s+Cited)\s+"
    r"(?=[A-Z][a-z]*[,.\s]|[A-Z]\.|[A-Z][A-Z][a-z]|\[\d+\]\s+[A-Z])",
    re.MULTILINE,
)

_REF_BRACKETED_RE = re.compile(
    r"(?:^|\n)\s*\[1\]\s+[A-Z].{0,1500}?\n.{0,1500}?\[2\]\s+[A-Z]",
    re.DOTALL,
)

_END_OF_BODY_MARKERS_RE = re.compile(
    r"^#{1,4}\s+("
    r"Disclosure\s+Statement|"
    r"Funding(?:\s+(?:Statement|Information))?|"
    r"Acknowledg(?:e)?ments?|"
    r"Author\s+Contributions?|"
    r"Conflict\s+of\s+Interest|"
    r"Declaration\s+of\s+(?:Competing|Conflicting)\s+Interests?|"
    r"Supplementary\s+(?:Data|Materials?)|"
    r"Appendix\s+[A-Z](?:\.|\s)"
    r")\b",
    re.MULTILINE | re.IGNORECASE,
)

_AUTHOR_YEAR_TAIL_RE = re.compile(
    r"[A-Z][A-Za-z'\-]+,\s+[A-Z]\.(?:\s*[A-Z]\.)?[^.\n]*?\(\d{4}[a-z]?\)"
)


def split_body_references(markdown: str) -> Tuple[str, str, str]:
    """Return ``(body_md, references_md, method)``.

    Splits an academic-paper Markdown document at the last References-style
    boundary, trying five detectors in order: strict heading -> loose heading
    -> paragraph-prefix ("References Author, ...") -> bracketed-numbered
    ("[1] Author ...") -> end-of-body marker + author-year density tail. If
    none fires, the body keeps everything and references is empty. The chosen
    method is returned so callers can flag papers where detection failed.

    Complements :func:`clean_reference_section`, which formats a references
    block once it has been split out.
    """
    matches = list(_REF_HEADING_RE.finditer(markdown))
    if matches:
        cut = matches[-1].start()
        return markdown[:cut].rstrip(), markdown[cut:].strip(), "strict-heading"

    matches = list(_REF_HEADING_LOOSE_RE.finditer(markdown))
    if matches:
        cut = matches[-1].start()
        return markdown[:cut].rstrip(), markdown[cut:].strip(), "loose-heading"

    matches = list(_REF_PARAGRAPH_RE.finditer(markdown))
    if matches:
        cut = matches[-1].start()
        return markdown[:cut].rstrip(), markdown[cut:].strip(), "paragraph-prefix"

    matches = list(_REF_BRACKETED_RE.finditer(markdown))
    if matches:
        cut = matches[-1].start()
        return markdown[:cut].rstrip(), markdown[cut:].strip(), "bracketed-numbered"

    end_markers = list(_END_OF_BODY_MARKERS_RE.finditer(markdown))
    if end_markers:
        tail_start = end_markers[-1].end()
        tail = markdown[tail_start:]
        ay_in_tail = list(_AUTHOR_YEAR_TAIL_RE.finditer(tail))
        if len(ay_in_tail) >= 8:
            cut_in_tail = ay_in_tail[0].start()
            abs_cut = tail_start + cut_in_tail
            line_start = markdown.rfind("\n", 0, abs_cut) + 1
            return (
                markdown[:line_start].rstrip(),
                markdown[line_start:].strip(),
                "end-marker-author-year-density",
            )

    return markdown.strip(), "", "no-references-heading-found"


# --- Affiliation tail --------------------------------------------------------

_AFFILIATION_TAIL_RE = re.compile(
    r"^#{1,4}\s+(AUTHOR\s+AFFILIATIONS?|Author\s+Affiliations?|"
    r"AFFILIATIONS?|Affiliations?|Corresponding\s+Author)\s*$",
    re.MULTILINE,
)


def strip_affiliation_tail(markdown: str) -> Tuple[str, int]:
    """Strip from an ``AUTHOR AFFILIATIONS`` (or similar) heading to EOF.

    Some journals place an author-affiliations block (ORCIDs, institutional
    addresses) at the end of the body; when it leaks into the body it pollutes
    pronoun counts and lexical metrics. Returns
    ``(cleaned_markdown, n_chars_stripped)``.
    """
    match = _AFFILIATION_TAIL_RE.search(markdown)
    if not match:
        return markdown, 0
    cleaned = markdown[: match.start()].rstrip()
    return cleaned, len(markdown) - len(cleaned)
