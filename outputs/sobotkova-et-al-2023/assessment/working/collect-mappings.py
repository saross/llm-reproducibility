#!/usr/bin/env python3
import json

# Read extraction
with open('/tmp/assessment-long/claims.json') as f:
    claims = json.load(f)
with open('/tmp/assessment-long/evidence.json') as f:
    evidence = json.load(f)
with open('/tmp/assessment-long/methods.json') as f:
    methods = json.load(f)
with open('/tmp/assessment-long/protocols.json') as f:
    protocols = json.load(f)
with open('/tmp/assessment-long/research_designs.json') as f:
    designs = json.load(f)

# Collect Claim → Evidence mappings
claim_evidence = []
for c in claims:
    if 'supported_by' in c and c['supported_by']:
        for e in c['supported_by']:
            claim_evidence.append(f"{c['claim_id']} → {e}")

# Collect Method → Design mappings
method_design = []
for m in methods:
    if 'implements_designs' in m and m['implements_designs']:
        for d in m['implements_designs']:
            method_design.append(f"{m['method_id']} → {d}")

# Collect Protocol → Method mappings
protocol_method = []
for p in protocols:
    if 'implements_methods' in p and p['implements_methods']:
        for m in p['implements_methods']:
            protocol_method.append(f"{p['protocol_id']} → {m}")

print(f"=== CLAIM → EVIDENCE MAPPINGS ({len(claim_evidence)}) ===")
for mapping in sorted(claim_evidence):
    print(mapping)

print(f"\n=== METHOD → DESIGN MAPPINGS ({len(method_design)}) ===")
for mapping in sorted(method_design):
    print(mapping)

print(f"\n=== PROTOCOL → METHOD MAPPINGS ({len(protocol_method)}) ===")
for mapping in sorted(protocol_method):
    print(mapping)

print(f"\n=== SUMMARY ===")
print(f"Total mappings: {len(claim_evidence) + len(method_design) + len(protocol_method)}")
print(f"  Claim → Evidence: {len(claim_evidence)}")
print(f"  Method → Design: {len(method_design)}")
print(f"  Protocol → Method: {len(protocol_method)}")

