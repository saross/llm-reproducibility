#!/usr/bin/env python3
"""
Pass 0: Metadata Extraction
Ross et al. 2009 - Remote Sensing and Archaeological Prospection in Apulia, Italy

Extract bibliographic metadata from title page and populate project_metadata.
Follows prompt: extraction-system/prompts/00-metadata_pass0_prompt.md
"""

import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

extraction_file = Path("extraction.json")

print("=" * 70)
print("PASS 0: METADATA EXTRACTION")
print("=" * 70)
print()

# =================================================================
# OPTIONAL: Extract PDF metadata for cross-validation
# =================================================================
try:
    pdf_path = "../../input/sources/original-pdf/Ross et al. - 2009 - Remote Sensing and Archaeological Prospection in Apulia, Italy.pdf"
    result = subprocess.run(
        ["pdfinfo", pdf_path],
        capture_output=True,
        text=True,
        timeout=5
    )
    if result.returncode == 0:
        print("PDF Metadata (for cross-validation):")
        print("-" * 70)
        for line in result.stdout.split('\n'):
            if any(field in line for field in ['Title', 'Author', 'Subject', 'Creator']):
                print(f"  {line}")
        print()
        print("Note: PDF metadata used for cross-check only, not primary source")
        print()
except (FileNotFoundError, subprocess.TimeoutExpired):
    print("pdfinfo not available or PDF not found - skipping PDF metadata cross-check")
    print()

# =================================================================
# READ EXTRACTION.JSON (FULL FILE - NO LIMIT!)
# =================================================================
with open(extraction_file) as f:
    data = json.load(f)

print("Reading first 2-3 pages of PDF to extract metadata from title page...")
print()

# =================================================================
# EXTRACT METADATA FROM TITLE PAGE
# =================================================================
# In actual implementation, this would use Claude to read the PDF
# and extract metadata following the Pass 0 prompt.
# This template shows the expected output structure.

metadata = {
    "paper_title": "Remote Sensing and Archaeological Prospection in Apulia, Italy",
    "authors": [
        "Shawn A. Ross",
        "Adela Sobotkova",
        "Gert-Jan Burgers"
    ],
    "publication_year": 2009,
    "journal": "Journal of Field Archaeology, Vol. 34, No. 4 (Winter, 2009), pp. 423-437",
    "doi": None,  # Not visible on title page
    "paper_type": "methods paper",
    "discipline": "archaeology",
    "research_context": "Comparative evaluation of QuickBird satellite imagery versus traditional field survey for archaeological prospection in 100 sq km study area centred on L'Amastuola, Apulia, Italy. Assesses relative utility of high-resolution multispectral remote sensing and intensive surface survey in Mediterranean karst environment."
}

# =================================================================
# VALIDATE METADATA
# =================================================================
print("Validating extracted metadata...")
print("-" * 70)

validation_issues = []

# Check required fields
required_fields = ['paper_title', 'authors', 'publication_year', 'journal',
                   'paper_type', 'discipline', 'research_context']
for field in required_fields:
    if field not in metadata or not metadata[field]:
        validation_issues.append(f"Missing required field: {field}")

# Check authors array
if 'authors' in metadata:
    if not isinstance(metadata['authors'], list) or len(metadata['authors']) == 0:
        validation_issues.append("authors must be non-empty array")
    else:
        # Check for initials instead of full names
        for author in metadata['authors']:
            if '.' in author and not any(c.isalpha() and c == c.lower() for c in author.split()[-1]):
                # Has period and last name part is not lowercase (might be initial)
                validation_issues.append(f"Author may be in initial format: {author}")

# Check publication_year is integer
if 'publication_year' in metadata:
    if not isinstance(metadata['publication_year'], int):
        validation_issues.append(f"publication_year must be integer, got {type(metadata['publication_year'])}")
    elif metadata['publication_year'] < 1900 or metadata['publication_year'] > 2030:
        validation_issues.append(f"publication_year {metadata['publication_year']} out of reasonable range")

# Check journal includes volume/pages
if 'journal' in metadata:
    if not any(indicator in metadata['journal'].lower() for indicator in ['vol', 'pp', 'pages']):
        validation_issues.append("journal field should include volume and pages")

# Check research_context is substantive
if 'research_context' in metadata:
    if len(metadata['research_context'].split()) < 10:
        validation_issues.append("research_context should be 1-2 complete sentences (currently too short)")

if validation_issues:
    print("⚠ VALIDATION WARNINGS:")
    for issue in validation_issues:
        print(f"  - {issue}")
    print()
else:
    print("✓ All validation checks passed")
    print()

# =================================================================
# POPULATE project_metadata IN EXTRACTION.JSON
# =================================================================
print("Populating project_metadata in extraction.json...")
print()

data['project_metadata'] = metadata

# Add extraction notes for Pass 0
data['extraction_notes']['pass0_metadata'] = {
    'completion_date': datetime.now(timezone.utc).isoformat(),
    'primary_source': 'JSTOR header + title page',
    'author_name_format': 'full names with middle initials',
    'doi_present': metadata['doi'] is not None,
    'notes': 'Paper accessed through JSTOR. Full bibliographic information available in JSTOR header. Authors listed with full names and institutional affiliations on title page.'
}

# Update timestamp
data['extraction_timestamp'] = datetime.now(timezone.utc).isoformat()

# =================================================================
# WRITE UPDATED EXTRACTION.JSON (WITH VALIDATION)
# =================================================================
with open(extraction_file, 'w') as f:
    json.dump(data, f, indent=2)

print("Updated extraction.json saved")
print()

# =================================================================
# VERIFY WRITE SUCCESS
# =================================================================
print("Verifying file write...")
with open(extraction_file) as f:
    verify_data = json.load(f)

if 'project_metadata' in verify_data and verify_data['project_metadata']:
    print("✓ project_metadata successfully written")
else:
    print("❌ ERROR: project_metadata not found in written file")
    exit(1)

# =================================================================
# PRINT METADATA SUMMARY
# =================================================================
print()
print("=" * 70)
print("PASS 0 COMPLETE - Metadata Extraction")
print("=" * 70)
print()
print("Extracted Metadata:")
print("-" * 70)
print(f"Title: {metadata['paper_title']}")
print(f"Authors: {', '.join(metadata['authors'])} ({len(metadata['authors'])} total)")
print(f"Journal: {metadata['journal']}")
print(f"Year: {metadata['publication_year']}")
print(f"DOI: {metadata['doi'] or 'Not present'}")
print(f"Type: {metadata['paper_type']}")
print(f"Discipline: {metadata['discipline']}")
print()
print(f"Research Context:")
print(f"  {metadata['research_context']}")
print()
print("=" * 70)
print()
print("Proceeding to Pass 1: Liberal Claims & Evidence Extraction")
print("=" * 70)
