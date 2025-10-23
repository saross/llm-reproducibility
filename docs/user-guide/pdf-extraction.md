# PDF Text Extraction for LLM Analysis

This toolkit extracts clean, LLM-optimized text from academic PDFs using PyMuPDF and pdfplumber.

## Quick Start

```bash
# 1. Set up virtual environment (first time only)
python3 -m venv venv
source venv/bin/activate  # On Linux/Mac
# OR: venv\Scripts\activate  # On Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Extract a PDF
python scripts/extract_pdf_text.py "sources/PDF/your-paper.pdf"

# Output will be in: sources/extracted/your-paper.md
```

## Features

- **Clean Text Extraction**: Removes headers, footers, page numbers, and hyphenation
- **Structure Preservation**: Detects and formats section headings
- **Table Extraction**: Extracts tables as Markdown
- **Metadata Extraction**: Captures title, authors, and other PDF metadata
- **LLM-Optimized Output**: Produces clean, flowing Markdown ideal for LLM analysis
- **Configurable**: Customize extraction behavior via config file
- **Offline**: Works completely offline, no API calls needed

## Usage Examples

### Basic Extraction

```bash
python scripts/extract_pdf_text.py input.pdf
```

Output: `sources/extracted/input.md`

### Custom Output Location

```bash
python scripts/extract_pdf_text.py input.pdf -o custom/output.md
```

### Using Configuration File

```bash
python scripts/extract_pdf_text.py input.pdf -c scripts/config.yaml
```

### Command-Line Options

```bash
# Skip metadata extraction
python scripts/extract_pdf_text.py input.pdf --no-metadata

# Skip table extraction (faster)
python scripts/extract_pdf_text.py input.pdf --no-tables

# Use aggressive cleaning (better for complex PDFs)
python scripts/extract_pdf_text.py input.pdf --aggressive

# Combine options
python scripts/extract_pdf_text.py input.pdf --no-tables --aggressive -o output.md
```

### Batch Processing

```bash
# Extract all PDFs in a directory
for pdf in sources/PDF/*.pdf; do
    python scripts/extract_pdf_text.py "$pdf"
done
```

## Configuration

Edit `scripts/config.yaml` to customize extraction behavior:

```yaml
# Remove headers and footers
remove_headers_footers: true
header_threshold: 0.08  # Top 8% of page
footer_threshold: 0.92  # Bottom 8% of page

# Detect section headings
detect_sections: true

# Extract tables
extract_tables: true

# Extract abstract separately
extract_abstract: true

# Use aggressive text cleaning
aggressive_cleaning: false

# Include PDF metadata in output
include_metadata: true
```

## Output Format

The extracted text is formatted as Markdown with:

### Document Header

```markdown
# Paper Title

**Authors:** Author Names

**Pages:** 13

---
```

### Abstract (if detected)

```markdown
## Abstract

[Abstract text...]
```

### Structured Sections

```markdown
## 1. Introduction

[Section text...]

## 2. Methods

[Section text...]
```

### Tables (if extracted)

```markdown
## Tables

### Table 1 (Page 5)

| Header 1 | Header 2 | Header 3 |
| -------- | -------- | -------- |
| Data 1   | Data 2   | Data 3   |
```

## Extraction Quality

The Sobotkova et al. 2023 paper extraction results:

- **Pages processed**: 13
- **Total characters**: 78,193
- **Total words**: 11,970
- **Sections detected**: 59
- **Output file size**: 81 KB
- **Extraction time**: ~5 seconds

### Common Issues and Solutions

#### Text is jumbled or paragraphs are broken

**Solution**: Use aggressive cleaning mode

```bash
python scripts/extract_pdf_text.py input.pdf --aggressive
```

#### Headers/footers still present

**Solution**: Adjust threshold in config.yaml

```yaml
header_threshold: 0.10  # Increase to remove more at top
footer_threshold: 0.90  # Decrease to remove more at bottom
```

#### Tables not extracted

**Likely cause**: Tables are images, not text

**Solution**: PyMuPDF/pdfplumber can only extract text-based tables. For image tables, consider using OCR or describe them manually.

#### Equations are garbled

**Limitation**: Math equations are challenging for all PDF extractors. Options:
- Use specialized tools like Nougat (deep learning-based)
- Manually review and fix equations
- Or accept that equations may not be perfect for LLM analysis of methods/claims

## When to Use This Tool

### ✅ Good Fit

- **2-10 academic papers** to process
- **Standard academic layout** (like most journal articles)
- **Extracting prose content** (claims, methods, evidence)
- **Need immediate solution** without complex setup
- **Offline environment** or no cloud services

### ⚠️ May Need Enhancement

- **100+ papers** - Consider adding GROBID
- **Complex math-heavy papers** - May need Nougat or specialized tools
- **Perfect reference extraction required** - Consider GROBID
- **Poor quality scans** - May need OCR preprocessing

## Architecture

```
scripts/
├── extract_pdf_text.py    # Main extraction script
├── pdf_cleaner.py         # Text cleaning utilities
└── config.yaml            # Configuration file

sources/
├── PDF/                   # Input PDFs
└── extracted/             # Output Markdown files
```

### Modular Design

The system is designed to be extensible:

- **pdf_cleaner.py**: Reusable text cleaning functions
- **extract_pdf_text.py**: Main extraction logic
- **config.yaml**: User-facing configuration

Can be extended with:
- Additional cleaning functions
- Different output formats (JSON, plain text)
- Integration with GROBID for better metadata
- Batch processing scripts
- Quality validation checks

## Future Enhancements

### Potential Additions

1. **GROBID Integration** - For better metadata and reference extraction
2. **Nougat Integration** - For math-heavy papers
3. **OCR Preprocessing** - For scanned papers
4. **Quality Scoring** - Automatic assessment of extraction quality
5. **Citation Extraction** - Parse and structure references
6. **Figure Caption Extraction** - Extract and index figure captions
7. **Batch Dashboard** - Web interface for batch processing

### When to Upgrade to GROBID

Consider adding GROBID if:
- Processing **100+ papers**
- Need **structured reference extraction**
- Working with **varied paper formats**
- Have time for **Docker setup** (a few hours)

GROBID can be added alongside this tool without replacing it.

## Troubleshooting

### ImportError when running script

```bash
# Make sure you're in the virtual environment
source venv/bin/activate  # Linux/Mac
# OR: venv\Scripts\activate  # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

### "File not found" error

- Use absolute paths or check your current directory
- Ensure PDF file exists: `ls -la "sources/PDF/your-file.pdf"`

### Output is empty or very short

- Check the PDF is text-based, not a scanned image
- Try with a different PDF to rule out PDF-specific issues
- Use `--aggressive` flag for complex layouts

### Script is slow

- Large PDFs (50+ pages) may take 30-60 seconds
- Use `--no-tables` to skip table extraction
- Check if your PDF is very large (>100 MB)

## Dependencies

- **PyMuPDF (fitz)**: Fast PDF text extraction with layout information
- **pdfplumber**: Table extraction and detailed layout analysis
- **PyYAML**: Configuration file parsing
- **python-slugify**: Filename generation

All dependencies are open-source and well-maintained.

## License Considerations

- **PyMuPDF**: AGPL license (GPL-compatible, free for internal use)
- **pdfplumber**: MIT license (permissive)
- **This toolkit**: Use in accordance with your project's needs

## Contributing

To enhance this toolkit:

1. Add functions to `pdf_cleaner.py` for new cleaning capabilities
2. Extend `extract_pdf_text.py` for new extraction features
3. Update `config.yaml` with new configuration options
4. Test with diverse paper types and document results

## Support

For issues:
1. Check this README for common solutions
2. Review the extraction statistics for clues
3. Try different configuration options
4. Test with a simpler PDF to isolate the issue

## Comparison with Alternatives

| Tool | Setup Time | Best For | Limitations |
|------|-----------|----------|-------------|
| **This toolkit (PyMuPDF)** | 5 minutes | 2-100 papers, standard layouts | Struggles with complex math |
| **GROBID** | 2-3 hours | 100+ papers, metadata focus | Requires Docker, complex setup |
| **Nougat** | 1-2 hours | Math-heavy papers | Slow, GPU recommended |
| **Desktop GIS + manual** | Immediate | 1-5 papers | Not scalable, tedious |

## Citation

If you use this toolkit in research, please cite the underlying tools:

**PyMuPDF:**
```
Artifex Software, Inc. (2024). PyMuPDF: Python bindings for MuPDF.
https://pymupdf.readthedocs.io/
```

**pdfplumber:**
```
Singer-Vine, J. (2024). pdfplumber: Plumb a PDF for detailed information about each char, rectangle, line, et cetera.
https://github.com/jsvine/pdfplumber
```

## Next Steps

Once you have extracted text:

1. **Review the output** in `sources/extracted/`
2. **Check extraction statistics** to assess quality
3. **Use the Markdown** directly with Sonnet 4.5 for claims/evidence/methods extraction
4. **Iterate on configuration** if needed for better results
5. **Process additional papers** using the same approach

The extracted Markdown is optimized for LLM analysis and ready to use immediately.
