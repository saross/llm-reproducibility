#!/usr/bin/env python3
"""Conduct comprehensive Pass A/B/C assessment"""
import json
from collections import Counter, defaultdict

# Load all components
with open('evidence.json') as f:
    evidence = json.load(f)
with open('claims.json') as f:
    claims = json.load(f)
with open('methods.json') as f:
    methods = json.load(f)
with open('protocols.json') as f:
    protocols = json.load(f)
with open('research_designs.json') as f:
    research_designs = json.load(f)

total_items = len(evidence) + len(claims) + len(methods) + len(protocols) + len(research_designs)

print(f"=== ASSESSMENT OVERVIEW ===")
print(f"Total items: {total_items}")
print(f"  Evidence: {len(evidence)}")
print(f"  Claims: {len(claims)}")
print(f"  Methods: {len(methods)}")
print(f"  Protocols: {len(protocols)}")
print(f"  Research Designs: {len(research_designs)}")

# Count mappings
claim_evidence_mappings = sum(len(c.get('supported_by_evidence', [])) for c in claims)
method_design_mappings = sum(len(m.get('linked_designs', [])) for m in methods)
protocol_method_mappings = sum(len(p.get('linked_methods', [])) for p in protocols)
total_mappings = claim_evidence_mappings + method_design_mappings + protocol_method_mappings

print(f"\n=== RELATIONSHIP MAPPINGS ===")
print(f"Total mappings: {total_mappings}")
print(f"  Claim → Evidence: {claim_evidence_mappings}")
print(f"  Method → Design: {method_design_mappings}")
print(f"  Protocol → Method: {protocol_method_mappings}")

# Claims-to-Evidence ratio
ce_ratio = len(claims) / len(evidence) if evidence else 0
print(f"\n=== METRICS ===")
print(f"Claims-to-Evidence ratio: {ce_ratio:.2f}:1")

# Based on structural analysis, this paper had NO errors detected
# Let me verify a few more samples from different sections

print(f"\n=== SAMPLE VERIFICATION (Methods section) ===")
methods_evidence = [e for e in evidence if 'Methods' in str(e.get('location', {}))]
print(f"Evidence from Methods section: {len(methods_evidence)}")
for e in methods_evidence[:3]:
    print(f"\n{e['evidence_id']}: {e['evidence_text'][:80]}...")
    print(f"  Location: {e['location']}")

print(f"\n=== SAMPLE VERIFICATION (Results section) ===")
results_evidence = [e for e in evidence if 'Results' in str(e.get('location', {}))]
print(f"Evidence from Results section: {len(results_evidence)}")
for e in results_evidence[:3]:
    print(f"\n{e['evidence_id']}: {e['evidence_text'][:80]}...")
    print(f"  Location: {e['location']}")

