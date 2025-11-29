#!/usr/bin/env python3
"""Verify samples from all item types"""
import json

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

print("=== VERIFICATION SAMPLES FROM ALL TYPES ===\n")

print("--- CLAIMS (3 samples) ---")
for c in claims[:3]:
    print(f"\n{c['claim_id']}: {c['claim_text'][:100]}...")
    print(f"  Type: {c['claim_type']}, Role: {c['claim_role']}")
    print(f"  Quote: {c['verbatim_quote'][:100]}...")
    print(f"  Evidence support: {c.get('supported_by_evidence', [])}")

print("\n--- METHODS (2 samples) ---")
for m in methods[:2]:
    print(f"\n{m['method_id']}: {m['method_name']}")
    print(f"  Type: {m['method_type']}")
    print(f"  Linked designs: {m.get('linked_designs', [])}")

print("\n--- PROTOCOLS (2 samples) ---")
for p in protocols[:2]:
    print(f"\n{p['protocol_id']}: {p['protocol_name'][:80]}...")
    print(f"  Linked methods: {p.get('linked_methods', [])}")

print("\n--- RESEARCH DESIGNS (all) ---")
for rd in research_designs:
    print(f"\n{rd['design_id']}: {rd['design_name']}")
    print(f"  Type: {rd['design_type']}")
    print(f"  Design: {rd.get('design', 'N/A')}")

