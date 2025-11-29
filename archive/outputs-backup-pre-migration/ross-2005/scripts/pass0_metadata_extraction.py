#!/usr/bin/env python3
"""
Pass 0: Metadata Extraction for Ross 2005

Extracts bibliographic metadata from title page of:
Ross, S.A. (2005). Barbarophonos: Language and Panhellenism in the Iliad.
Classical Philology, 100(4), 299-316.

Schema: v2.5
Workflow: v3.0.0
"""

import json
from pathlib import Path

# Metadata extracted from title page (JSTOR header + paper title page)
metadata = {
    "paper_title": "Barbarophonos: Language and Panhellenism in the Iliad",
    "authors": ["Shawn A. Ross"],  # Full name from title page
    "publication_year": 2005,  # Integer, not string
    "journal": "Classical Philology, Vol. 100, No. 4 (October 2005), pp. 299-316",
    "doi": "10.1086/500434",  # From JSTOR stable URL
    "paper_type": "research article",
    "discipline": "classical philology",
    "research_context": "Analysis of linguistic patterns in Homeric epic to argue for proto-Panhellenic identity c. 700 BCE, examining how the Iliad represents linguistic diversity among Greeks (suppressed) versus Trojans (emphasised)."
}

# Validation
assert len(metadata["authors"]) >= 1, "Must have at least one author"
assert isinstance(metadata["publication_year"], int), "Year must be integer"
assert metadata["doi"] is not None, "DOI should be string or null"
assert all(key in metadata for key in ["paper_title", "authors", "publication_year",
                                        "journal", "doi", "paper_type", "discipline",
                                        "research_context"]), "All required fields present"

print(f"✓ Metadata validation passed")
print(f"  - Authors: {len(metadata['authors'])}")
print(f"  - Journal: {metadata['journal']}")
print(f"  - DOI: {metadata['doi']}")
print(f"  - Paper type: {metadata['paper_type']}")
print(f"  - Discipline: {metadata['discipline']}")

# Create blank extraction schema with metadata
extraction = {
    "project_metadata": metadata,
    "evidence": [],
    "claims": [],
    "implicit_arguments": [],
    "research_designs": [],
    "methods": [],
    "protocols": [],
    "extraction_notes": [
        "RUN-02: Clean extraction addressing RUN-01 evidence under-extraction failure",
        "Pass 0: Metadata extracted from JSTOR header and title page",
        "Critical objective: Capture 20-30 evidence items (2-3x RUN-01 count of 10)",
        "Missing RUN-01 citations to capture: Il. 20.74, Il. 2.668, Od. 10.305, Od. 14.229-31, Hymn Cer. 118-44, Hymn Bacch. 53-57"
    ]
}

# Write to extraction.json
output_path = Path("outputs/ross-2005/extraction.json")
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(extraction, f, indent=2, ensure_ascii=False)

print(f"\n✓ Created extraction.json with metadata at: {output_path}")
print(f"  Ready for Pass 1 (Claims & Evidence extraction)")
