#!/usr/bin/env python3
"""
Add 2 missing evidence items discovered in comprehensive citation scan.
- Il. 2.862-63 (Phrygian remoteness in Trojan Catalogue)
- Il. 3.181-90 (Priam mentions Otreus and Phrygians)

Part of RUN-02 evidence completeness correction.
"""

import json

# Read current extraction
with open('/home/shawn/Code/llm-reproducibility/outputs/ross-2005/extraction.json', 'r') as f:
    data = json.load(f)

# Define the 2 missing evidence items
missing_evidence = [
    {
        "id": "E016",
        "content": "Iliad 2.862-63: Remoteness of Phrygian homeland noted by phrase 'from afar' (thel' ex) in Trojan Catalogue, indicating geographic distance",
        "evidence_type": "primary_source",
        "evidence_status": "explicit",
        "page": 313,
        "verbatim_quote": "the remoteness of the Phrygian homeland is noted by the phrase thÅl' ejx, \"from afar,\" in the Trojan Catalogue (2.862–63)",
        "source": "Homer, Iliad 2.862-63",
        "related_claims": [],
        "supports_claims": [],
        "notes": "RUN-02 ADDITION - Citation found in comprehensive scan. Geographic remoteness marker supporting linguistic alterity theme"
    },
    {
        "id": "E017",
        "content": "Iliad 3.181-90: Priam names Otreus (mentioned in Hymn to Aphrodite) as contemporary of his youth, establishing Phrygian connection to Trojan cycle",
        "evidence_type": "primary_source",
        "evidence_status": "explicit",
        "page": 313,
        "verbatim_quote": "Elsewhere in the Iliad (3.181–90), the Otreus mentioned in the Hymn to Aphrodite is named by Priam as a contemporary of his youth",
        "source": "Homer, Iliad 3.181-90",
        "related_claims": [],
        "supports_claims": [],
        "notes": "RUN-02 ADDITION - Citation found in comprehensive scan. Establishes Phrygian remoteness and connection supporting Hymn to Aphrodite analysis"
    }
]

# Add the missing evidence items
data["evidence"].extend(missing_evidence)

# Update extraction notes
data["extraction_notes"].append("RUN-02 Evidence Addition: Added 2 missing citations found in comprehensive scan (Il. 2.862-63, Il. 3.181-90). Total evidence now 17 items.")

# Write updated extraction
with open('/home/shawn/Code/llm-reproducibility/outputs/ross-2005/extraction.json', 'w') as f:
    json.dump(data, f, indent=2)

print("✓ Added E016: Il. 2.862-63 (Phrygian remoteness)")
print("✓ Added E017: Il. 3.181-90 (Priam mentions Otreus)")
print(f"✓ Total evidence items now: {len(data['evidence'])}")
print(f"✓ Total extraction items: {len(data['evidence']) + len(data['claims']) + len(data['implicit_arguments']) + len(data['research_designs']) + len(data['methods']) + len(data['protocols'])}")
