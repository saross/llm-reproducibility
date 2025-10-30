#!/usr/bin/env python3
"""
Pass 0: Metadata Extraction
Ross 2005 - Barbarophonos: Language and Panhellenism in the Iliad

Extract bibliographic metadata from title page and populate project_metadata.
Follows prompt: extraction-system/prompts/00-metadata_pass0_prompt.md
"""

import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

extraction_file = Path("extraction.json")

print("=" * 80)
print("PASS 0: METADATA EXTRACTION - Ross 2005")
print("=" * 80)
print()

# =================================================================
# OPTIONAL: Extract PDF metadata for cross-validation
# =================================================================
try:
    pdf_path = "../../input/sources/original-pdf/Ross - 2005 - Barbarophonos Language and Panhellenism in the Iliad.pdf"
    result = subprocess.run(
        ["pdfinfo", pdf_path],
        capture_output=True,
        text=True,
        timeout=5
    )
    if result.returncode == 0:
        print("PDF Metadata (for cross-validation):")
        print("-" * 80)
        for line in result.stdout.split('\n'):
            if any(field in line for field in ['Title', 'Author', 'Subject', 'Creator', 'Pages']):
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

print("Reading title page of PDF to extract metadata...")
print()

# =================================================================
# EXTRACT METADATA FROM TITLE PAGE
# =================================================================

metadata = {
    "paper_title": "Barbarophonos: Language and Panhellenism in the Iliad",
    "authors": [
        "Shawn A. Ross"
    ],
    "publication_year": 2005,
    "journal": "Classical Philology, Vol. 100, No. 4 (October 2005), pp. 299-316",
    "doi": None,  # Not visible on title page
    "paper_type": "literary_analysis",
    "discipline": "classical_philology",
    "research_context": "Literary/philological analysis investigating the extent to which Panhellenism was present in early Archaic Greece through linguistic patterns in Homeric epic. Uses close reading of Iliad, Odyssey, Hesiod's Theogony, and Homeric Hymns to argue that the Iliad reflects proto-Panhellenic consciousness through representation of linguistic diversity among Trojans versus linguistic unity among Akhaians, dating to 8th century BCE oral tradition stabilisation."
}

# =================================================================
# VALIDATE METADATA
# =================================================================
print("Validating extracted metadata...")
print("-" * 80)

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

# Check publication_year is integer
if 'publication_year' in metadata:
    if not isinstance(metadata['publication_year'], int):
        validation_issues.append(f"publication_year must be integer, got {type(metadata['publication_year'])}")
    elif metadata['publication_year'] < 1900 or metadata['publication_year'] > 2030:
        validation_issues.append(f"publication_year {metadata['publication_year']} out of reasonable range")

# Check journal includes volume/pages
if 'journal' in metadata:
    if not any(indicator in metadata['journal'].lower() for indicator in ['vol', 'pp', 'pages', 'no.']):
        validation_issues.append("journal field should include volume and pages")

# Check research_context is substantive
if 'research_context' in metadata:
    word_count = len(metadata['research_context'].split())
    if word_count < 10:
        validation_issues.append(f"research_context should be 1-2 complete sentences (currently {word_count} words)")

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
    'primary_source': 'Journal title page',
    'author_name_format': 'full name with middle initial',
    'doi_present': metadata['doi'] is not None,
    'notes': 'Classical philology paper published in Classical Philology journal (University of Chicago Press). Single author. Literary analysis methodology examining linguistic patterns in ancient Greek epic poetry to investigate proto-Panhellenic identity formation in 8th century BCE.'
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
    print(f"  - Title: {verify_data['project_metadata']['paper_title']}")
    print(f"  - Authors: {len(verify_data['project_metadata']['authors'])} author(s)")
    print(f"  - Year: {verify_data['project_metadata']['publication_year']}")
else:
    print("❌ ERROR: project_metadata not found in written file")
    exit(1)

# =================================================================
# PRINT METADATA SUMMARY
# =================================================================
print()
print("=" * 80)
print("PASS 0 COMPLETE - Metadata Extraction")
print("=" * 80)
print()
print("Extracted Metadata:")
print("-" * 80)
print(f"Title: {metadata['paper_title']}")
print(f"Authors: {', '.join(metadata['authors'])} ({len(metadata['authors'])} total)")
print(f"Journal: {metadata['journal']}")
print(f"Year: {metadata['publication_year']}")
print(f"DOI: {metadata['doi'] or 'Not present'}")
print(f"Type: {metadata['paper_type']}")
print(f"Discipline: {metadata['discipline']}")
print()
print(f"Research Context ({len(metadata['research_context'].split())} words):")
print(f"  {metadata['research_context']}")
print()
print("=" * 80)
print("Paper Characteristics:")
print("-" * 80)
print("  - First literary/philological analysis in extraction corpus")
print("  - 18 pages (vs 44-53 for empirical papers)")
print("  - Interpretive methodology (no formal methods section)")
print("  - Textual evidence (ancient Greek texts, not empirical data)")
print("  - Argumentative structure (not IMRaD)")
print("  - Expected lower RDMAP counts (13-23 vs 60-80 typical)")
print("  - Expected higher implicit claims (30-40% vs 20-25%)")
print()
print("=" * 80)
print()
print("Ready for Pass 1: Liberal Claims & Evidence Extraction (10 sections)")
print("=" * 80)
