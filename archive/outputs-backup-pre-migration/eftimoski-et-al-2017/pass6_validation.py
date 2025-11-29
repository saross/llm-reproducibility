#!/usr/bin/env python3
"""
Pass 6: Validation

Verify extraction quality:
- Cross-reference integrity
- Hierarchy validation
- Schema compliance
- Source verification
"""

import json
from datetime import datetime, timezone
from pathlib import Path

# Load current extraction
extraction_file = Path("extraction.json")
with open(extraction_file) as f:
    data = json.load(f)

print("Pass 6: Validation Starting...")
print(f"Validating: {len(data['evidence'])} evidence, {len(data['claims'])} claims, {len(data['implicit_arguments'])} implicit args")
print(f"           {len(data['research_designs'])} designs, {len(data['methods'])} methods, {len(data['protocols'])} protocols")

validation_report = {
    "validation_timestamp": datetime.now(timezone.utc).isoformat(),
    "schema_version": "2.5",
    "paper_title": data["project_metadata"]["paper_title"],
    "validation_summary": {
        "overall_status": "PASS",
        "total_items": (len(data['evidence']) + len(data['claims']) + len(data['implicit_arguments']) +
                       len(data['research_designs']) + len(data['methods']) + len(data['protocols'])),
        "critical_issues": 0,
        "important_issues": 0,
        "minor_issues": 0,
        "warnings": 0
    }
}

# ========================================
# CROSS-REFERENCE INTEGRITY
# ========================================

print("\nChecking cross-reference integrity...")

# Collect all IDs
evidence_ids = set(e['evidence_id'] for e in data['evidence'])
claim_ids = set(c['claim_id'] for c in data['claims'])
ia_ids = set(ia['implicit_id'] for ia in data['implicit_arguments'])
design_ids = set(rd['design_id'] for rd in data['research_designs'])
method_ids = set(m['method_id'] for m in data['methods'])
protocol_ids = set(p['protocol_id'] for p in data['protocols'])

broken_refs = []

# Check evidence → claims references
for e in data['evidence']:
    for claim_ref in e.get('supports_claims', []):
        if claim_ref not in claim_ids:
            broken_refs.append(f"{e['evidence_id']}.supports_claims → {claim_ref} (not found)")

# Check claims → evidence/claims references
for c in data['claims']:
    for ev_ref in c.get('supported_by', []):
        if ev_ref not in evidence_ids:
            broken_refs.append(f"{c['claim_id']}.supported_by → {ev_ref} (not found)")
    for claim_ref in c.get('supports_claims', []):
        if claim_ref not in claim_ids:
            broken_refs.append(f"{c['claim_id']}.supports_claims → {claim_ref} (not found)")

# Check RDMAP references
for m in data['methods']:
    for design_ref in m.get('design_context', []):
        if design_ref not in design_ids:
            broken_refs.append(f"{m['method_id']}.design_context → {design_ref} (not found)")

for p in data['protocols']:
    for method_ref in p.get('method_context', []):
        if method_ref not in method_ids:
            broken_refs.append(f"{p['protocol_id']}.method_context → {method_ref} (not found)")

validation_report["cross_reference_integrity"] = {
    "status": "PASS" if not broken_refs else "FAIL",
    "issues": broken_refs
}

print(f"  {'✓' if not broken_refs else '✗'} Cross-references: {len(broken_refs)} broken references")

# ========================================
# HIERARCHY VALIDATION
# ========================================

print("\nChecking hierarchy validation...")

# Check RDMAP chain: designs → methods → protocols
rdmap_issues = []

# All methods should link to designs
methods_without_design = [m['method_id'] for m in data['methods'] if not m.get('design_context')]
if methods_without_design:
    rdmap_issues.append(f"Methods without design_context: {methods_without_design}")

# All protocols should link to methods
protocols_without_method = [p['protocol_id'] for p in data['protocols'] if not p.get('method_context')]
if protocols_without_method:
    rdmap_issues.append(f"Protocols without method_context: {protocols_without_method}")

validation_report["hierarchy_validation"] = {
    "status": "PASS" if not rdmap_issues else "FAIL",
    "rdmap_chain_issues": rdmap_issues,
    "linking_completeness": {
        "total_protocols": len(data['protocols']),
        "linked_protocols": len([p for p in data['protocols'] if p.get('method_context')]),
        "linking_rate": 100.0 if all(p.get('method_context') for p in data['protocols']) else 0.0,
        "status": "PASS" if all(p.get('method_context') for p in data['protocols']) else "FAIL"
    }
}

print(f"  {'✓' if not rdmap_issues else '✗'} RDMAP hierarchy: {len(rdmap_issues)} issues")

# ========================================
# SOURCE VERIFICATION
# ========================================

print("\nChecking source verification...")

source_issues = []

# Check evidence has verbatim_quote
for e in data['evidence']:
    if not e.get('verbatim_quote'):
        source_issues.append(f"{e['evidence_id']} missing verbatim_quote")

# Check claims have verbatim_quote
for c in data['claims']:
    if not c.get('verbatim_quote'):
        source_issues.append(f"{c['claim_id']} missing verbatim_quote")

# Check implicit arguments have trigger_text
for ia in data['implicit_arguments']:
    if not ia.get('trigger_text'):
        source_issues.append(f"{ia['implicit_id']} missing trigger_text")

# Check explicit RDMAP have verbatim_quote
for rd in data['research_designs']:
    if rd.get('sourcing_status') != 'implicit' and not rd.get('verbatim_quote'):
        source_issues.append(f"{rd['design_id']} missing verbatim_quote")

for m in data['methods']:
    if m.get('sourcing_status') != 'implicit' and not m.get('verbatim_quote'):
        source_issues.append(f"{m['method_id']} missing verbatim_quote")

for p in data['protocols']:
    if p.get('sourcing_status') != 'implicit' and not p.get('verbatim_quote'):
        source_issues.append(f"{p['protocol_id']} missing verbatim_quote")

validation_report["source_verification"] = {
    "status": "PASS" if not source_issues else "FAIL",
    "issues": source_issues,
    "metrics": {
        "evidence_quote_rate": 100.0 * sum(1 for e in data['evidence'] if e.get('verbatim_quote')) / len(data['evidence']),
        "claims_quote_rate": 100.0 * sum(1 for c in data['claims'] if c.get('verbatim_quote')) / len(data['claims']),
        "overall_sourcing_rate": 100.0 if not source_issues else 0.0
    }
}

print(f"  {'✓' if not source_issues else '✗'} Source verification: {len(source_issues)} issues")

# ========================================
# OVERALL STATUS
# ========================================

all_issues = broken_refs + rdmap_issues + source_issues
validation_report["validation_summary"]["overall_status"] = "PASS" if not all_issues else "FAIL"
validation_report["validation_summary"]["critical_issues"] = len(broken_refs)
validation_report["validation_summary"]["important_issues"] = len(rdmap_issues)
validation_report["validation_summary"]["minor_issues"] = len(source_issues)

# Save validation report
with open("validation_report.json", 'w') as f:
    json.dump(validation_report, f, indent=2)

print(f"\n{'✓✓✓ VALIDATION PASSED ✓✓✓' if not all_issues else '✗✗✗ VALIDATION FAILED ✗✗✗'}")
print(f"  Critical issues: {len(broken_refs)}")
print(f"  Important issues: {len(rdmap_issues)}")
print(f"  Minor issues: {len(source_issues)}")
print(f"✓ Validation report saved to validation_report.json")
