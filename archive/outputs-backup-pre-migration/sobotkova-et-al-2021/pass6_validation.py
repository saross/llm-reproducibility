#!/usr/bin/env python3
"""
Pass 6: Validation for sobotkova-et-al-2021

Performs systematic integrity checks on the extraction including:
- Cross-reference integrity
- Hierarchy validation
- Schema compliance
- Source verification completeness
- Expected information aggregation
- Consolidation metadata verification
- Type consistency
"""

import json
from pathlib import Path
from collections import defaultdict
from datetime import datetime, timezone

# Load extraction
extraction_file = Path("extraction.json")
with open(extraction_file) as f:
    data = json.load(f)

print("=" * 70)
print("PASS 6: VALIDATION")
print("=" * 70)

# Initialize validation report
validation_report = {
    "validation_timestamp": datetime.now(timezone.utc).isoformat(),
    "schema_version": data.get("schema_version", "2.5"),
    "paper_title": data["project_metadata"]["paper_title"],
    "validation_summary": {
        "overall_status": "PENDING",
        "total_items": 0,
        "critical_issues": 0,
        "important_issues": 0,
        "minor_issues": 0,
        "warnings": 0
    },
    "cross_reference_integrity": {
        "status": "PENDING",
        "issues": []
    },
    "hierarchy_validation": {
        "status": "PENDING",
        "rdmap_chain_issues": [],
        "claims_hierarchy_issues": [],
        "evidence_chain_issues": [],
        "linking_completeness": {}
    },
    "schema_compliance": {
        "status": "PENDING",
        "missing_fields": [],
        "invalid_enums": [],
        "id_format_errors": [],
        "location_structure_issues": []
    },
    "source_verification": {
        "status": "PENDING",
        "evidence_issues": [],
        "claims_issues": [],
        "implicit_argument_issues": [],
        "rdmap_issues": [],
        "metrics": {}
    },
    "expected_information_completeness": {
        "critical_gaps": [],
        "important_gaps": [],
        "minor_gaps": [],
        "gap_summary": {}
    },
    "consolidation_verification": {
        "status": "PENDING",
        "issues": []
    },
    "type_consistency": {
        "status": "PENDING",
        "issues": []
    },
    "recommendations": []
}

# Calculate total items
total_items = (len(data.get('evidence', [])) +
               len(data.get('claims', [])) +
               len(data.get('implicit_arguments', [])) +
               len(data.get('research_designs', [])) +
               len(data.get('methods', [])) +
               len(data.get('protocols', [])))

validation_report["validation_summary"]["total_items"] = total_items

print(f"\nValidating {total_items} items...")
print(f"  Evidence: {len(data.get('evidence', []))}")
print(f"  Claims: {len(data.get('claims', []))}")
print(f"  Implicit Arguments: {len(data.get('implicit_arguments', []))}")
print(f"  Research Designs: {len(data.get('research_designs', []))}")
print(f"  Methods: {len(data.get('methods', []))}")
print(f"  Protocols: {len(data.get('protocols', []))}")

# ============================================================================
# 1. CROSS-REFERENCE INTEGRITY
# ============================================================================

print("\n" + "=" * 70)
print("1. CROSS-REFERENCE INTEGRITY")
print("=" * 70)

# Build ID sets
evidence_ids = {e['evidence_id'] for e in data.get('evidence', [])}
claim_ids = {c['claim_id'] for c in data.get('claims', [])}
ia_ids = {ia['implicit_id'] for ia in data.get('implicit_arguments', [])}
design_ids = {rd['design_id'] for rd in data.get('research_designs', [])}
method_ids = {m['method_id'] for m in data.get('methods', [])}
protocol_ids = {p['protocol_id'] for p in data.get('protocols', [])}

broken_refs = []

# Check Design → Method references
for rd in data.get('research_designs', []):
    for method_id in rd.get('methods_used', []):
        if method_id not in method_ids:
            broken_refs.append({
                "from_id": rd['design_id'],
                "to_id": method_id,
                "reference_type": "Design → Method",
                "severity": "critical"
            })

# Check Method → Design references
for m in data.get('methods', []):
    design_context = m.get('design_context', [])
    if isinstance(design_context, str):
        design_context = [design_context]
    for design_id in design_context:
        if design_id not in design_ids:
            broken_refs.append({
                "from_id": m['method_id'],
                "to_id": design_id,
                "reference_type": "Method → Design",
                "severity": "critical"
            })

# Check Protocol → Method references
for p in data.get('protocols', []):
    for method_id in p.get('implements_methods', []):
        if method_id not in method_ids:
            broken_refs.append({
                "from_id": p['protocol_id'],
                "to_id": method_id,
                "reference_type": "Protocol → Method",
                "severity": "critical"
            })

# Check Claim → Evidence references
for c in data.get('claims', []):
    for evidence_id in c.get('supporting_evidence', []):
        if evidence_id not in evidence_ids:
            broken_refs.append({
                "from_id": c['claim_id'],
                "to_id": evidence_id,
                "reference_type": "Claim → Evidence",
                "severity": "critical"
            })

# Check Evidence → Claim references
for e in data.get('evidence', []):
    for claim_id in e.get('supports_claims', []):
        if claim_id not in claim_ids:
            broken_refs.append({
                "from_id": e['evidence_id'],
                "to_id": claim_id,
                "reference_type": "Evidence → Claim",
                "severity": "critical"
            })

# Check Implicit Argument references
for ia in data.get('implicit_arguments', []):
    for evidence_id in ia.get('supporting_evidence', []):
        if evidence_id not in evidence_ids:
            broken_refs.append({
                "from_id": ia['implicit_id'],
                "to_id": evidence_id,
                "reference_type": "Implicit Argument → Evidence",
                "severity": "critical"
            })

validation_report["cross_reference_integrity"]["issues"] = broken_refs
validation_report["cross_reference_integrity"]["status"] = "PASS" if not broken_refs else "FAIL"

print(f"Broken references: {len(broken_refs)}")
if broken_refs:
    validation_report["validation_summary"]["critical_issues"] += len(broken_refs)
    for ref in broken_refs[:5]:  # Show first 5
        print(f"  ✗ {ref['from_id']} → {ref['to_id']} ({ref['reference_type']})")
    if len(broken_refs) > 5:
        print(f"  ... and {len(broken_refs) - 5} more")
else:
    print("  ✓ All cross-references valid")

# ============================================================================
# 2. HIERARCHY VALIDATION
# ============================================================================

print("\n" + "=" * 70)
print("2. HIERARCHY VALIDATION")
print("=" * 70)

hierarchy_issues = []

# Check RDMAP chains (Design → Methods → Protocols)
print("\nRDMAP Hierarchy:")

# Every Method should reference at least one Design
orphaned_methods = []
for m in data.get('methods', []):
    design_context = m.get('design_context', [])
    if isinstance(design_context, str):
        design_context = [design_context] if design_context else []
    if not design_context or (len(design_context) == 1 and design_context[0] == ""):
        orphaned_methods.append(m['method_id'])
        hierarchy_issues.append({
            "item_id": m['method_id'],
            "issue": "Method has no design_context",
            "severity": "critical"
        })

print(f"  Methods without Design: {len(orphaned_methods)}")
if orphaned_methods:
    validation_report["validation_summary"]["critical_issues"] += len(orphaned_methods)
    for mid in orphaned_methods[:3]:
        print(f"    ✗ {mid}")

# Every Protocol should reference at least one Method
orphaned_protocols = []
for p in data.get('protocols', []):
    if not p.get('implements_methods', []):
        orphaned_protocols.append(p['protocol_id'])
        hierarchy_issues.append({
            "item_id": p['protocol_id'],
            "issue": "Protocol has no implements_methods",
            "severity": "critical"
        })

print(f"  Protocols without Method: {len(orphaned_protocols)}")
if orphaned_protocols:
    validation_report["validation_summary"]["critical_issues"] += len(orphaned_protocols)
    for pid in orphaned_protocols[:3]:
        print(f"    ✗ {pid}")

# Calculate linking completeness
total_protocols = len(data.get('protocols', []))
linked_protocols = total_protocols - len(orphaned_protocols)
linking_rate = (linked_protocols / total_protocols * 100) if total_protocols > 0 else 0

validation_report["hierarchy_validation"]["linking_completeness"] = {
    "total_protocols": total_protocols,
    "linked_protocols": linked_protocols,
    "linking_rate": linking_rate,
    "status": "PASS" if linking_rate >= 80 else ("WARNING" if linking_rate >= 50 else "CRITICAL")
}

print(f"  Protocol-Method linking rate: {linking_rate:.1f}%")

validation_report["hierarchy_validation"]["rdmap_chain_issues"] = hierarchy_issues
validation_report["hierarchy_validation"]["status"] = "PASS" if not hierarchy_issues else "FAIL"

# ============================================================================
# 3. SCHEMA COMPLIANCE
# ============================================================================

print("\n" + "=" * 70)
print("3. SCHEMA COMPLIANCE")
print("=" * 70)

missing_fields = []
invalid_enums = []
id_format_errors = []
location_issues = []

# ID format validation
def validate_id_format(item_id, expected_prefix):
    """Check if ID matches expected format (e.g., E001, C001, RD001)"""
    if not item_id.startswith(expected_prefix):
        return False
    # Check that suffix is numeric
    suffix = item_id[len(expected_prefix):]
    return suffix.isdigit() and len(suffix) >= 2

# Validate Evidence
for e in data.get('evidence', []):
    if not validate_id_format(e['evidence_id'], 'E'):
        id_format_errors.append(f"Evidence ID format invalid: {e['evidence_id']}")
    if 'verbatim_quote' not in e or not e['verbatim_quote']:
        missing_fields.append(f"{e['evidence_id']}: missing verbatim_quote")
    if 'location' not in e:
        location_issues.append(f"{e['evidence_id']}: missing location object")
    elif 'section' not in e['location'] or 'page' not in e['location']:
        location_issues.append(f"{e['evidence_id']}: location missing section or page")

# Validate Claims
for c in data.get('claims', []):
    if not validate_id_format(c['claim_id'], 'C'):
        id_format_errors.append(f"Claim ID format invalid: {c['claim_id']}")
    if 'verbatim_quote' not in c or not c['verbatim_quote']:
        missing_fields.append(f"{c['claim_id']}: missing verbatim_quote")
    if 'location' not in c:
        location_issues.append(f"{c['claim_id']}: missing location object")

# Validate Implicit Arguments
for ia in data.get('implicit_arguments', []):
    if not validate_id_format(ia['implicit_id'], 'IA'):
        id_format_errors.append(f"Implicit Argument ID format invalid: {ia['implicit_id']}")
    if 'trigger_text' not in ia or not ia['trigger_text']:
        missing_fields.append(f"{ia['implicit_id']}: missing trigger_text")
    if 'trigger_locations' not in ia or not ia['trigger_locations']:
        missing_fields.append(f"{ia['implicit_id']}: missing trigger_locations")
    if 'inference_reasoning' not in ia or not ia['inference_reasoning']:
        missing_fields.append(f"{ia['implicit_id']}: missing inference_reasoning")

# Validate Research Designs
for rd in data.get('research_designs', []):
    if not validate_id_format(rd['design_id'], 'RD'):
        id_format_errors.append(f"Research Design ID format invalid: {rd['design_id']}")
    if 'design_status' not in rd or rd['design_status'] not in ['explicit', 'implicit']:
        invalid_enums.append(f"{rd['design_id']}: invalid design_status")
    if 'verbatim_quote' not in rd or not rd['verbatim_quote']:
        missing_fields.append(f"{rd['design_id']}: missing verbatim_quote")

# Validate Methods
for m in data.get('methods', []):
    if not validate_id_format(m['method_id'], 'M') and not validate_id_format(m['method_id'], 'IM'):
        id_format_errors.append(f"Method ID format invalid: {m['method_id']}")
    if 'method_status' not in m or m['method_status'] not in ['explicit', 'implicit']:
        invalid_enums.append(f"{m['method_id']}: invalid method_status")

    # Check sourcing based on status
    if m.get('method_status') == 'explicit':
        if 'verbatim_quote' not in m or not m['verbatim_quote']:
            missing_fields.append(f"{m['method_id']}: explicit method missing verbatim_quote")
    elif m.get('method_status') == 'implicit':
        if 'trigger_text' not in m or not m['trigger_text']:
            missing_fields.append(f"{m['method_id']}: implicit method missing trigger_text")
        if 'implicit_metadata' not in m:
            missing_fields.append(f"{m['method_id']}: implicit method missing implicit_metadata")

# Validate Protocols
for p in data.get('protocols', []):
    if not validate_id_format(p['protocol_id'], 'P') and not validate_id_format(p['protocol_id'], 'IP'):
        id_format_errors.append(f"Protocol ID format invalid: {p['protocol_id']}")
    if 'protocol_status' not in p or p['protocol_status'] not in ['explicit', 'implicit']:
        invalid_enums.append(f"{p['protocol_id']}: invalid protocol_status")

    # Check sourcing based on status
    if p.get('protocol_status') == 'explicit':
        if 'verbatim_quote' not in p or not p['verbatim_quote']:
            missing_fields.append(f"{p['protocol_id']}: explicit protocol missing verbatim_quote")
    elif p.get('protocol_status') == 'implicit':
        if 'trigger_text' not in p or not p['trigger_text']:
            missing_fields.append(f"{p['protocol_id']}: implicit protocol missing trigger_text")
        if 'implicit_metadata' not in p:
            missing_fields.append(f"{p['protocol_id']}: implicit protocol missing implicit_metadata")

validation_report["schema_compliance"]["missing_fields"] = missing_fields
validation_report["schema_compliance"]["invalid_enums"] = invalid_enums
validation_report["schema_compliance"]["id_format_errors"] = id_format_errors
validation_report["schema_compliance"]["location_structure_issues"] = location_issues

schema_issues = len(missing_fields) + len(invalid_enums) + len(id_format_errors) + len(location_issues)
validation_report["schema_compliance"]["status"] = "PASS" if schema_issues == 0 else "FAIL"

print(f"Missing required fields: {len(missing_fields)}")
if missing_fields:
    validation_report["validation_summary"]["critical_issues"] += len(missing_fields)
    for issue in missing_fields[:3]:
        print(f"  ✗ {issue}")
    if len(missing_fields) > 3:
        print(f"  ... and {len(missing_fields) - 3} more")

print(f"Invalid enum values: {len(invalid_enums)}")
if invalid_enums:
    validation_report["validation_summary"]["critical_issues"] += len(invalid_enums)
    for issue in invalid_enums[:3]:
        print(f"  ✗ {issue}")

print(f"ID format errors: {len(id_format_errors)}")
if id_format_errors:
    validation_report["validation_summary"]["critical_issues"] += len(id_format_errors)
    for issue in id_format_errors[:3]:
        print(f"  ✗ {issue}")

print(f"Location structure issues: {len(location_issues)}")
if location_issues:
    validation_report["validation_summary"]["important_issues"] += len(location_issues)

# ============================================================================
# 4. SOURCE VERIFICATION METRICS
# ============================================================================

print("\n" + "=" * 70)
print("4. SOURCE VERIFICATION METRICS")
print("=" * 70)

# Note: Full source verification (checking verbatim quotes against source PDF)
# would require PDF reading. Here we check for PRESENCE of required sourcing fields.

source_issues = []

# Evidence & Claims - must have verbatim_quote
evidence_with_quote = sum(1 for e in data.get('evidence', []) if e.get('verbatim_quote'))
claims_with_quote = sum(1 for c in data.get('claims', []) if c.get('verbatim_quote'))

evidence_quote_rate = (evidence_with_quote / len(data.get('evidence', [])) * 100) if data.get('evidence') else 100
claims_quote_rate = (claims_with_quote / len(data.get('claims', [])) * 100) if data.get('claims') else 100

print(f"\nExplicit Content Sourcing:")
print(f"  Evidence with verbatim_quote: {evidence_with_quote}/{len(data.get('evidence', []))} ({evidence_quote_rate:.1f}%)")
print(f"  Claims with verbatim_quote: {claims_with_quote}/{len(data.get('claims', []))} ({claims_quote_rate:.1f}%)")

# Implicit Arguments - must have trigger_text and trigger_locations
ia_with_triggers = sum(1 for ia in data.get('implicit_arguments', [])
                       if ia.get('trigger_text') and ia.get('trigger_locations'))
ia_trigger_rate = (ia_with_triggers / len(data.get('implicit_arguments', [])) * 100) if data.get('implicit_arguments') else 100

print(f"\nImplicit Arguments:")
print(f"  With trigger infrastructure: {ia_with_triggers}/{len(data.get('implicit_arguments', []))} ({ia_trigger_rate:.1f}%)")

# RDMAP sourcing by status
print(f"\nRDMAP Sourcing:")

# Research Designs
explicit_designs = [rd for rd in data.get('research_designs', []) if rd.get('design_status') == 'explicit']
explicit_designs_with_quote = sum(1 for rd in explicit_designs if rd.get('verbatim_quote'))
explicit_design_rate = (explicit_designs_with_quote / len(explicit_designs) * 100) if explicit_designs else 100

print(f"  Research Designs (explicit): {explicit_designs_with_quote}/{len(explicit_designs)} ({explicit_design_rate:.1f}%)")

# Methods
explicit_methods = [m for m in data.get('methods', []) if m.get('method_status') == 'explicit']
implicit_methods = [m for m in data.get('methods', []) if m.get('method_status') == 'implicit']

explicit_methods_with_quote = sum(1 for m in explicit_methods if m.get('verbatim_quote'))
implicit_methods_with_triggers = sum(1 for m in implicit_methods if m.get('trigger_text') and m.get('trigger_locations'))

explicit_method_rate = (explicit_methods_with_quote / len(explicit_methods) * 100) if explicit_methods else 100
implicit_method_rate = (implicit_methods_with_triggers / len(implicit_methods) * 100) if implicit_methods else 100

print(f"  Methods (explicit): {explicit_methods_with_quote}/{len(explicit_methods)} ({explicit_method_rate:.1f}%)")
print(f"  Methods (implicit): {implicit_methods_with_triggers}/{len(implicit_methods)} ({implicit_method_rate:.1f}%)")

# Protocols
explicit_protocols = [p for p in data.get('protocols', []) if p.get('protocol_status') == 'explicit']
implicit_protocols = [p for p in data.get('protocols', []) if p.get('protocol_status') == 'implicit']

explicit_protocols_with_quote = sum(1 for p in explicit_protocols if p.get('verbatim_quote'))
implicit_protocols_with_triggers = sum(1 for p in implicit_protocols if p.get('trigger_text') and p.get('trigger_locations'))

explicit_protocol_rate = (explicit_protocols_with_quote / len(explicit_protocols) * 100) if explicit_protocols else 100
implicit_protocol_rate = (implicit_protocols_with_triggers / len(implicit_protocols) * 100) if implicit_protocols else 100

print(f"  Protocols (explicit): {explicit_protocols_with_quote}/{len(explicit_protocols)} ({explicit_protocol_rate:.1f}%)")
print(f"  Protocols (implicit): {implicit_protocols_with_triggers}/{len(implicit_protocols)} ({implicit_protocol_rate:.1f}%)")

# Overall sourcing rate
all_rates = [evidence_quote_rate, claims_quote_rate, ia_trigger_rate,
             explicit_design_rate, explicit_method_rate, implicit_method_rate,
             explicit_protocol_rate, implicit_protocol_rate]
overall_sourcing_rate = sum(all_rates) / len([r for r in all_rates if r is not None])

print(f"\nOverall sourcing completeness: {overall_sourcing_rate:.1f}%")

validation_report["source_verification"]["metrics"] = {
    "evidence_quote_rate": evidence_quote_rate,
    "claims_quote_rate": claims_quote_rate,
    "implicit_arguments_trigger_rate": ia_trigger_rate,
    "explicit_designs_quote_rate": explicit_design_rate,
    "explicit_methods_quote_rate": explicit_method_rate,
    "implicit_methods_trigger_rate": implicit_method_rate,
    "explicit_protocols_quote_rate": explicit_protocol_rate,
    "implicit_protocols_trigger_rate": implicit_protocol_rate,
    "overall_sourcing_rate": overall_sourcing_rate
}

validation_report["source_verification"]["status"] = "PASS" if overall_sourcing_rate >= 95 else "WARNING"

if overall_sourcing_rate < 95:
    validation_report["validation_summary"]["warnings"] += 1

# ============================================================================
# 5. EXPECTED INFORMATION COMPLETENESS
# ============================================================================

print("\n" + "=" * 70)
print("5. EXPECTED INFORMATION COMPLETENESS")
print("=" * 70)

# Aggregate all expected_information_missing arrays
all_gaps = defaultdict(int)

for m in data.get('methods', []):
    for gap in m.get('expected_information_missing', []):
        all_gaps[gap] += 1

for p in data.get('protocols', []):
    for gap in p.get('expected_information_missing', []):
        all_gaps[gap] += 1

print(f"\nTotal unique gaps identified: {len(all_gaps)}")
print(f"Total gap instances: {sum(all_gaps.values())}")

# Show most common gaps
if all_gaps:
    sorted_gaps = sorted(all_gaps.items(), key=lambda x: x[1], reverse=True)
    print(f"\nMost common gaps:")
    for gap, count in sorted_gaps[:10]:
        print(f"  {count}x {gap}")
        # Categorize as minor (these are documentation gaps, not extraction errors)
        validation_report["expected_information_completeness"]["minor_gaps"].append({
            "gap": gap,
            "count": count
        })

validation_report["expected_information_completeness"]["gap_summary"] = {
    "unique_gaps": len(all_gaps),
    "total_instances": sum(all_gaps.values())
}

# ============================================================================
# 6. CONSOLIDATION METADATA VERIFICATION
# ============================================================================

print("\n" + "=" * 70)
print("6. CONSOLIDATION METADATA VERIFICATION")
print("=" * 70)

consolidation_issues = []

# Find all items with consolidation_metadata
items_with_consolidation = []

for p in data.get('protocols', []):
    if 'consolidation_metadata' in p:
        items_with_consolidation.append({
            'id': p['protocol_id'],
            'type': 'protocol',
            'metadata': p['consolidation_metadata']
        })

print(f"Items with consolidation_metadata: {len(items_with_consolidation)}")

for item in items_with_consolidation:
    meta = item['metadata']

    # Check required fields
    if 'consolidated_from' not in meta:
        consolidation_issues.append({
            "item_id": item['id'],
            "issue": "Missing consolidated_from field",
            "severity": "critical"
        })
    elif len(meta.get('consolidated_from', [])) < 2:
        consolidation_issues.append({
            "item_id": item['id'],
            "issue": "Consolidation must merge at least 2 items",
            "severity": "important"
        })

    if 'rationale' not in meta and 'consolidation_rationale' not in meta:
        consolidation_issues.append({
            "item_id": item['id'],
            "issue": "Missing consolidation rationale",
            "severity": "important"
        })

    print(f"  {item['id']}: consolidated from {meta.get('consolidated_from', [])}")

validation_report["consolidation_verification"]["issues"] = consolidation_issues
validation_report["consolidation_verification"]["status"] = "PASS" if not consolidation_issues else "FAIL"

if consolidation_issues:
    validation_report["validation_summary"]["important_issues"] += len([i for i in consolidation_issues if i['severity'] == 'important'])
    validation_report["validation_summary"]["critical_issues"] += len([i for i in consolidation_issues if i['severity'] == 'critical'])

# ============================================================================
# 7. TYPE CONSISTENCY
# ============================================================================

print("\n" + "=" * 70)
print("7. TYPE CONSISTENCY")
print("=" * 70)

type_issues = []

# Check status field matches sourcing approach
for m in data.get('methods', []):
    status = m.get('method_status')
    has_quote = bool(m.get('verbatim_quote'))
    has_triggers = bool(m.get('trigger_text'))

    if status == 'explicit' and not has_quote:
        type_issues.append({
            "item_id": m['method_id'],
            "issue": "Status=explicit but missing verbatim_quote",
            "severity": "critical"
        })
    elif status == 'implicit' and not has_triggers:
        type_issues.append({
            "item_id": m['method_id'],
            "issue": "Status=implicit but missing trigger_text",
            "severity": "critical"
        })

for p in data.get('protocols', []):
    status = p.get('protocol_status')
    has_quote = bool(p.get('verbatim_quote'))
    has_triggers = bool(p.get('trigger_text'))

    if status == 'explicit' and not has_quote:
        type_issues.append({
            "item_id": p['protocol_id'],
            "issue": "Status=explicit but missing verbatim_quote",
            "severity": "critical"
        })
    elif status == 'implicit' and not has_triggers:
        type_issues.append({
            "item_id": p['protocol_id'],
            "issue": "Status=implicit but missing trigger_text",
            "severity": "critical"
        })

validation_report["type_consistency"]["issues"] = type_issues
validation_report["type_consistency"]["status"] = "PASS" if not type_issues else "FAIL"

print(f"Type consistency issues: {len(type_issues)}")
if type_issues:
    validation_report["validation_summary"]["critical_issues"] += len(type_issues)
    for issue in type_issues[:5]:
        print(f"  ✗ {issue['item_id']}: {issue['issue']}")

# ============================================================================
# OVERALL STATUS DETERMINATION
# ============================================================================

print("\n" + "=" * 70)
print("VALIDATION SUMMARY")
print("=" * 70)

# Determine overall status
critical = validation_report["validation_summary"]["critical_issues"]
important = validation_report["validation_summary"]["important_issues"]
warnings = validation_report["validation_summary"]["warnings"]

if critical > 0:
    overall_status = "FAIL"
elif important > 0:
    overall_status = "PASS_WITH_ISSUES"
else:
    overall_status = "PASS"

validation_report["validation_summary"]["overall_status"] = overall_status

print(f"\nOverall Status: {overall_status}")
print(f"  Critical Issues: {critical}")
print(f"  Important Issues: {important}")
print(f"  Minor Issues: {validation_report['validation_summary']['minor_issues']}")
print(f"  Warnings: {warnings}")

# ============================================================================
# RECOMMENDATIONS
# ============================================================================

recommendations = []

if critical == 0 and important == 0:
    recommendations.append({
        "priority": "info",
        "recommendation": "Extraction passes all structural validation checks. Ready for assessment phase.",
        "rationale": "No critical or important issues found."
    })
else:
    if broken_refs:
        recommendations.append({
            "priority": "high",
            "recommendation": f"Fix {len(broken_refs)} broken cross-references",
            "rationale": "Broken references prevent proper hierarchy traversal and assessment"
        })

    if orphaned_methods or orphaned_protocols:
        recommendations.append({
            "priority": "high",
            "recommendation": f"Link {len(orphaned_methods)} orphaned methods and {len(orphaned_protocols)} orphaned protocols to parent items",
            "rationale": "All RDMAP items must connect to hierarchy for proper assessment"
        })

    if missing_fields:
        recommendations.append({
            "priority": "high",
            "recommendation": f"Populate {len(missing_fields)} missing required fields",
            "rationale": "Required fields necessary for source verification and assessment"
        })

    if overall_sourcing_rate < 95:
        recommendations.append({
            "priority": "medium",
            "recommendation": f"Improve sourcing completeness from {overall_sourcing_rate:.1f}% to >95%",
            "rationale": "Comprehensive sourcing critical for preventing hallucination and enabling verification"
        })

validation_report["recommendations"] = recommendations

print("\nRecommendations:")
for i, rec in enumerate(recommendations, 1):
    print(f"{i}. [{rec['priority'].upper()}] {rec['recommendation']}")
    print(f"   Rationale: {rec['rationale']}")

# ============================================================================
# SAVE VALIDATION REPORT
# ============================================================================

validation_file = Path("validation_report.json")
with open(validation_file, 'w') as f:
    json.dump(validation_report, f, indent=2)

print(f"\n{'=' * 70}")
print(f"Validation report saved to: {validation_file}")
print(f"{'=' * 70}")

# Update extraction.json metadata
data['validation'] = {
    'last_validated': validation_report['validation_timestamp'],
    'validation_status': overall_status,
    'critical_issues': critical,
    'important_issues': important
}

with open(extraction_file, 'w') as f:
    json.dump(data, f, indent=2)

print(f"\nExtraction metadata updated with validation status")

print("\n" + "=" * 70)
print("PASS 6 VALIDATION COMPLETE")
print("=" * 70)
print(f"Status: {overall_status}")
