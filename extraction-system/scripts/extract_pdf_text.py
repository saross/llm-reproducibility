#!/usr/bin/env python3
"""
PDF Text Extraction for LLM Analysis

Extract and clean text from academic PDFs, outputting LLM-optimized Markdown.

Usage:
    python extract_pdf_text.py input.pdf -o output.md
    python extract_pdf_text.py input.pdf --config config.yaml
"""

import argparse
import sys
from pathlib import Path
from typing import Dict, List, Optional
import yaml

try:
    import fitz  # PyMuPDF
    import pdfplumber
    from slugify import slugify
except ImportError as e:
    print(f"Error: Required package not found. Please run: pip install -r requirements.txt")
    print(f"Details: {e}")
    sys.exit(1)

# Import our cleaning utilities
from pdf_cleaner import (
    clean_extracted_text,
    detect_section_heading,
    format_as_markdown_heading,
    extract_abstract,
    remove_headers_footers,
    clean_reference_section
)


class PDFExtractor:
    """Extract and process text from PDF files."""

    def __init__(self, config: Optional[Dict] = None):
        """
        Initialize extractor with optional configuration.

        Args:
            config: Configuration dictionary
        """
        self.config = config or self._default_config()
        self.stats = {
            'pages': 0,
            'total_chars': 0,
            'total_words': 0,
            'tables_found': 0,
            'sections_detected': 0
        }

    @staticmethod
    def _default_config() -> Dict:
        """Default extraction configuration."""
        return {
            'remove_headers_footers': True,
            'header_threshold': 0.08,  # Top 8% of page
            'footer_threshold': 0.92,  # Bottom 8% of page
            'detect_sections': True,
            'extract_tables': True,
            'extract_abstract': True,
            'aggressive_cleaning': False,
            'include_metadata': True
        }

    def extract_metadata(self, pdf_path: Path) -> Dict[str, str]:
        """
        Extract basic metadata from PDF.

        Args:
            pdf_path: Path to PDF file

        Returns:
            Dictionary of metadata
        """
        metadata = {}

        try:
            with fitz.open(pdf_path) as doc:
                meta = doc.metadata
                metadata['title'] = meta.get('title', '')
                metadata['author'] = meta.get('author', '')
                metadata['subject'] = meta.get('subject', '')
                metadata['creator'] = meta.get('creator', '')
                metadata['producer'] = meta.get('producer', '')
                metadata['pages'] = len(doc)

        except Exception as e:
            print(f"Warning: Could not extract metadata: {e}")

        return metadata

    def extract_text_pymupdf(self, pdf_path: Path) -> List[Dict]:
        """
        Extract text blocks using PyMuPDF with layout information.

        Args:
            pdf_path: Path to PDF file

        Returns:
            List of text blocks with metadata
        """
        blocks = []

        try:
            with fitz.open(pdf_path) as doc:
                self.stats['pages'] = len(doc)

                for page_num, page in enumerate(doc):
                    # Get text blocks with position info
                    page_blocks = page.get_text("dict")["blocks"]
                    page_height = page.rect.height

                    for block in page_blocks:
                        if block.get('type') == 0:  # Text block
                            for line in block.get('lines', []):
                                for span in line.get('spans', []):
                                    blocks.append({
                                        'text': span.get('text', ''),
                                        'bbox': span.get('bbox'),
                                        'font_size': span.get('size'),
                                        'font': span.get('font'),
                                        'page': page_num,
                                        'page_height': page_height
                                    })

        except Exception as e:
            print(f"Error extracting text with PyMuPDF: {e}")
            raise

        return blocks

    def extract_tables_pdfplumber(self, pdf_path: Path) -> List[Dict]:
        """
        Extract tables using pdfplumber.

        Args:
            pdf_path: Path to PDF file

        Returns:
            List of extracted tables with page numbers
        """
        tables = []

        if not self.config.get('extract_tables', True):
            return tables

        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page_num, page in enumerate(pdf.pages):
                    page_tables = page.extract_tables()
                    for table in page_tables:
                        if table:
                            tables.append({
                                'page': page_num,
                                'data': table
                            })
                            self.stats['tables_found'] += 1

        except Exception as e:
            print(f"Warning: Could not extract tables: {e}")

        return tables

    def format_table_as_markdown(self, table: List[List[str]]) -> str:
        """
        Convert table data to Markdown format.

        Args:
            table: 2D list of table cells

        Returns:
            Markdown-formatted table
        """
        if not table or len(table) < 2:
            return ""

        # Get max width for each column
        col_widths = [max(len(str(row[i] or '')) for row in table)
                     for i in range(len(table[0]))]

        md_lines = []

        # Header row
        header = table[0]
        md_lines.append('| ' + ' | '.join(str(cell or '').ljust(col_widths[i])
                                          for i, cell in enumerate(header)) + ' |')

        # Separator
        md_lines.append('| ' + ' | '.join('-' * col_widths[i]
                                          for i in range(len(header))) + ' |')

        # Data rows
        for row in table[1:]:
            md_lines.append('| ' + ' | '.join(str(cell or '').ljust(col_widths[i])
                                              for i, cell in enumerate(row)) + ' |')

        return '\n'.join(md_lines)

    def process_blocks_to_markdown(self, blocks: List[Dict], tables: List[Dict]) -> str:
        """
        Convert text blocks to clean Markdown.

        Args:
            blocks: List of text blocks
            tables: List of extracted tables

        Returns:
            Markdown-formatted text
        """
        # Filter headers/footers if configured
        if self.config.get('remove_headers_footers', True):
            filtered_blocks = []
            for block in blocks:
                page_height = block.get('page_height', 1000)
                header_y = page_height * self.config.get('header_threshold', 0.08)
                footer_y = page_height * self.config.get('footer_threshold', 0.92)

                bbox = block.get('bbox', [0, 0, 0, 0])
                y0, y1 = bbox[1], bbox[3]

                # Keep if not in header/footer region
                if not (y1 < header_y or y0 > footer_y):
                    filtered_blocks.append(block)
            blocks = filtered_blocks

        # Calculate average font size for heading detection
        font_sizes = [b.get('font_size', 10) for b in blocks if b.get('font_size')]
        avg_font_size = sum(font_sizes) / len(font_sizes) if font_sizes else 10

        # Build text with structure
        markdown_parts = []
        current_para = []

        for i, block in enumerate(blocks):
            text = block.get('text', '').strip()
            if not text:
                continue

            self.stats['total_chars'] += len(text)
            self.stats['total_words'] += len(text.split())

            # Check if this is a section heading
            font_size = block.get('font_size', avg_font_size)
            is_heading = (self.config.get('detect_sections', True) and
                         detect_section_heading(text, font_size, avg_font_size))

            if is_heading:
                # Flush current paragraph
                if current_para:
                    markdown_parts.append(' '.join(current_para))
                    current_para = []

                # Add heading
                markdown_parts.append(format_as_markdown_heading(text))
                self.stats['sections_detected'] += 1
            else:
                # Add to current paragraph
                current_para.append(text)

                # Check if this ends a sentence/paragraph
                if text.endswith(('.', '!', '?', ':', ';')) or (
                    i < len(blocks) - 1 and
                    blocks[i + 1].get('page') != block.get('page')
                ):
                    markdown_parts.append(' '.join(current_para))
                    current_para = []

        # Add any remaining text
        if current_para:
            markdown_parts.append(' '.join(current_para))

        # Join parts with appropriate spacing
        markdown = '\n\n'.join(part for part in markdown_parts if part.strip())

        # Insert tables at appropriate positions (simplified: at end)
        if tables:
            markdown += "\n\n---\n\n## Tables\n\n"
            for i, table in enumerate(tables):
                markdown += f"\n### Table {i+1} (Page {table['page']+1})\n\n"
                table_md = self.format_table_as_markdown(table['data'])
                if table_md:
                    markdown += table_md + "\n\n"

        return markdown

    def extract(self, pdf_path: Path) -> str:
        """
        Main extraction method.

        Args:
            pdf_path: Path to PDF file

        Returns:
            Extracted and cleaned Markdown text
        """
        print(f"Extracting text from: {pdf_path}")

        # Extract metadata
        metadata = self.extract_metadata(pdf_path) if self.config.get('include_metadata') else {}

        # Extract text blocks
        print("  - Extracting text blocks...")
        blocks = self.extract_text_pymupdf(pdf_path)
        print(f"    Found {len(blocks)} text blocks")

        # Extract tables
        print("  - Extracting tables...")
        tables = self.extract_tables_pdfplumber(pdf_path)
        print(f"    Found {len(tables)} tables")

        # Process to Markdown
        print("  - Processing to Markdown...")
        markdown = self.process_blocks_to_markdown(blocks, tables)

        # Apply text cleaning
        print("  - Cleaning text...")
        markdown = clean_extracted_text(
            markdown,
            aggressive=self.config.get('aggressive_cleaning', False)
        )

        # Extract abstract if configured
        if self.config.get('extract_abstract', True):
            print("  - Extracting abstract...")
            abstract, remaining = extract_abstract(markdown)
            if abstract:
                # Rebuild with abstract section
                markdown = f"## Abstract\n\n{abstract}\n\n{remaining}"

        # Add metadata header if available
        if metadata and metadata.get('title'):
            header_parts = [f"# {metadata['title']}\n"]
            if metadata.get('author'):
                header_parts.append(f"**Authors:** {metadata['author']}\n")
            if metadata.get('pages'):
                header_parts.append(f"**Pages:** {metadata['pages']}\n")
            header = '\n'.join(header_parts) + '\n---\n\n'
            markdown = header + markdown

        return markdown

    def print_stats(self):
        """Print extraction statistics."""
        print("\nExtraction Statistics:")
        print(f"  Pages processed: {self.stats['pages']}")
        print(f"  Total characters: {self.stats['total_chars']:,}")
        print(f"  Total words: {self.stats['total_words']:,}")
        print(f"  Tables extracted: {self.stats['tables_found']}")
        print(f"  Sections detected: {self.stats['sections_detected']}")


def load_config(config_path: Optional[Path]) -> Dict:
    """Load configuration from YAML file."""
    if not config_path or not config_path.exists():
        return PDFExtractor._default_config()

    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)

    # Merge with defaults
    default = PDFExtractor._default_config()
    default.update(config)
    return default


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Extract text from academic PDFs for LLM analysis'
    )
    parser.add_argument('input', type=Path, help='Input PDF file')
    parser.add_argument('-o', '--output', type=Path,
                       help='Output Markdown file (default: auto-generated)')
    parser.add_argument('-c', '--config', type=Path,
                       help='Configuration YAML file')
    parser.add_argument('--no-metadata', action='store_true',
                       help='Skip metadata extraction')
    parser.add_argument('--no-tables', action='store_true',
                       help='Skip table extraction')
    parser.add_argument('--aggressive', action='store_true',
                       help='Use aggressive text cleaning')

    args = parser.parse_args()

    # Validate input
    if not args.input.exists():
        print(f"Error: Input file not found: {args.input}")
        sys.exit(1)

    # Determine output path
    if args.output:
        output_path = args.output
    else:
        # Auto-generate from input filename
        output_dir = args.input.parent / '../extracted'
        output_dir = output_dir.resolve()
        output_dir.mkdir(parents=True, exist_ok=True)
        output_name = slugify(args.input.stem) + '.md'
        output_path = output_dir / output_name

    # Load configuration
    config = load_config(args.config)

    # Apply command-line overrides
    if args.no_metadata:
        config['include_metadata'] = False
    if args.no_tables:
        config['extract_tables'] = False
    if args.aggressive:
        config['aggressive_cleaning'] = True

    # Extract
    extractor = PDFExtractor(config)

    try:
        markdown = extractor.extract(args.input)

        # Save output
        print(f"\nSaving to: {output_path}")
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown)

        # Print stats
        extractor.print_stats()

        print(f"\n✓ Successfully extracted to: {output_path}")
        print(f"  File size: {output_path.stat().st_size:,} bytes")

    except Exception as e:
        print(f"\n✗ Error during extraction: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
