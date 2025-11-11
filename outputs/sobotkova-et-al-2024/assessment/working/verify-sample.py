#!/usr/bin/env python3
"""Verify sample of evidence items against source PDF"""
import json

# Load evidence
with open('evidence.json') as f:
    evidence = json.load(f)

# Sample verification results
print(f"Total evidence items: {len(evidence)}")
print(f"\nFirst 5 evidence items for verification:")
for i, e in enumerate(evidence[:5]):
    print(f"\n{e['evidence_id']}: {e['evidence_text']}")
    print(f"  Quote: {e['verbatim_quote']}")
    print(f"  Location: {e['location']}")
    
# Count by type
from collections import Counter
types = Counter(e['evidence_type'] for e in evidence)
print(f"\n\nEvidence types: {dict(types)}")
