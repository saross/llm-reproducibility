#!/usr/bin/env python3
"""
Pass 0: Metadata Extraction for ross-ballsun-stanton-2022
Extracts bibliographic metadata from title page
"""

import json
from datetime import datetime

# Load extraction
with open('outputs/ross-ballsun-stanton-2022/extraction.json', 'r') as f:
    data = json.load(f)

print("=" * 80)
print("PASS 0: METADATA EXTRACTION")
print("=" * 80)
print()

# Extract metadata from title page (pages 1-2 of PDF)
# Title page shows:
# - Title: "Introducing Preregistration of Research Design to Archaeology"
# - Authors: Shawn A. Ross (Macquarie University), Brian Ballsun-Stanton (Macquarie University)
# - Preprint: 22 April 2021
# - DOI: 10.31235/osf.io/sbwcq
# - Citation: Accepted 2 April 2020 for book "Digital Heritage and Archaeology in Practice"
#   edited by Ethan Watrall and Lynne Goldstein, University Press of Florida

metadata = {
    "paper_title": "Introducing Preregistration of Research Design to Archaeology",
    "authors": [
        "Shawn A. Ross",
        "Brian Ballsun-Stanton"
    ],
    "publication_year": 2021,
    "journal": "Digital Heritage and Archaeology in Practice, edited by Ethan Watrall and Lynne Goldstein. Gainesville, FL: University Press of Florida. (SocArXiv preprint, April 2021)",
    "doi": "10.31235/osf.io/sbwcq",
    "paper_type": "book chapter (methodological argument)",
    "discipline": "archaeology, research methodology, open science",
    "research_context": "Introduces the concept of preregistration to archaeological research as a mechanism to improve research transparency, combat cognitive biases, overcome perverse professional incentives, and encourage thoughtful advance planning of research design and data collection methodologies before fieldwork begins."
}

# Update extraction with metadata
data['project_metadata'] = metadata
data['extraction_timestamp'] = datetime.now().isoformat() + 'Z'

# Update extraction notes
data['extraction_notes'] = {
    'pass': 0,
    'section_extracted': 'Pass 0 complete - metadata extracted from title page',
    'extraction_strategy': 'Extracted bibliographic metadata from pages 1-2 (ResearchGate page and SocArXiv title page). Full author names used. Book chapter published as preprint.',
    'known_uncertainties': []
}

# Save updated extraction
with open('outputs/ross-ballsun-stanton-2022/extraction.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Metadata extracted:")
print()
print(f"Title: {metadata['paper_title']}")
print(f"Authors: {', '.join(metadata['authors'])}")
print(f"Publication Year: {metadata['publication_year']}")
print(f"Journal: {metadata['journal']}")
print(f"DOI: {metadata['doi']}")
print(f"Paper Type: {metadata['paper_type']}")
print(f"Discipline: {metadata['discipline']}")
print(f"Research Context: {metadata['research_context'][:100]}...")
print()
print("✓ Pass 0 complete - metadata extraction successful")
print("✓ All 8 required project_metadata fields populated")
print()
