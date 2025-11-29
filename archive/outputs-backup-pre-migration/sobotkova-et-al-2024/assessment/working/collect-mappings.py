#!/usr/bin/env python3
"""Collect all relationship mappings from extraction for Pass C verification."""
import json

# Read extraction components
with open('outputs/sobotkova-et-al-2024/assessment/working/claims.json') as f:
    claims = json.load(f)
with open('outputs/sobotkova-et-al-2024/assessment/working/evidence.json') as f:
    evidence = json.load(f)
with open('outputs/sobotkova-et-al-2024/assessment/working/methods.json') as f:
    methods = json.load(f)
with open('outputs/sobotkova-et-al-2024/assessment/working/protocols.json') as f:
    protocols = json.load(f)
with open('outputs/sobotkova-et-al-2024/assessment/working/research_designs.json') as f:
    designs = json.load(f)

# Collect Claim → Evidence mappings (check both field names)
claim_evidence = []
for c in claims:
    claim_id = c.get('claim_id', 'UNKNOWN')
    # Check both 'supported_by_evidence' and 'supported_by' field names
    evidence_refs = c.get('supported_by_evidence', c.get('supported_by', []))
    if evidence_refs:
        for e in evidence_refs:
            claim_evidence.append(f"{claim_id} → {e}")

# Also check Evidence → Claim mappings (reverse direction)
evidence_claim = []
for e in evidence:
    evidence_id = e.get('evidence_id', 'UNKNOWN')
    if 'supports_claims' in e and e['supports_claims']:
        for c_id in e['supports_claims']:
            evidence_claim.append(f"{c_id} → {evidence_id}")

# Collect Method → Design mappings (check both field names)
method_design = []
for m in methods:
    method_id = m.get('method_id', 'UNKNOWN')
    design_refs = m.get('linked_designs', m.get('implements_designs', []))
    if design_refs:
        for d in design_refs:
            method_design.append(f"{method_id} → {d}")

# Collect Protocol → Method mappings (check both field names)
protocol_method = []
for p in protocols:
    protocol_id = p.get('protocol_id', 'UNKNOWN')
    method_refs = p.get('linked_methods', p.get('implements_methods', []))
    if method_refs:
        for m_id in method_refs:
            protocol_method.append(f"{protocol_id} → {m_id}")

# Determine which direction is used
if claim_evidence and evidence_claim:
    print("Warning: Both claim→evidence and evidence→claim mappings found!")
    print(f"  claim.supported_by: {len(claim_evidence)} mappings")
    print(f"  evidence.supports_claims: {len(evidence_claim)} mappings")

primary_ce_mappings = evidence_claim if evidence_claim else claim_evidence
direction = "Evidence → Claim (supports_claims)" if evidence_claim else "Claim → Evidence (supported_by)"

print(f"\n=== CLAIM ↔ EVIDENCE MAPPINGS ({len(primary_ce_mappings)}) ===")
print(f"Direction: {direction}")
for mapping in sorted(primary_ce_mappings):
    print(mapping)

print(f"\n=== METHOD → DESIGN MAPPINGS ({len(method_design)}) ===")
for mapping in sorted(method_design):
    print(mapping)

print(f"\n=== PROTOCOL → METHOD MAPPINGS ({len(protocol_method)}) ===")
for mapping in sorted(protocol_method):
    print(mapping)

print(f"\n=== SUMMARY ===")
print(f"Total mappings: {len(primary_ce_mappings) + len(method_design) + len(protocol_method)}")
print(f"  Claim ↔ Evidence: {len(primary_ce_mappings)}")
print(f"  Method → Design: {len(method_design)}")
print(f"  Protocol → Method: {len(protocol_method)}")
