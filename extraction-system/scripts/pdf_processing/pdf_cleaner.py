"""
PDF Text Cleaning Utilities

Functions to clean and normalize text extracted from academic PDFs.
Optimized for preparing text for LLM analysis.
"""

import re
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
