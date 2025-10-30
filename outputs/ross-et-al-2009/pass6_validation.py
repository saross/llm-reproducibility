#!/usr/bin/env python3
"""
Pass 6: Validation
Ross et al. 2009 - Remote Sensing and Archaeological Prospection in Apulia, Italy

Comprehensive quality checks:
- Cross-reference integrity (claims ↔ evidence, implicit_arguments → claims)
- RDMAP hierarchy validation (designs → methods → protocols)
- Schema compliance (required fields, status consistency)
- Sourcing completeness (100% verbatim_quote or trigger_text)
- Page number validity
- Metadata completeness (project_metadata fields)
"""

import json
from datetime import datetime, timezone
from pathlib import Path
from collections import defaultdict

extraction_file = Path("extraction.json")
with open(extraction_file) as f:
    data = json.load(f)

print("=" * 70)
print("PASS 6: VALIDATION")
print("=" * 70)
print()

# Validation results tracking
validation_results = {
    "critical": [],
    "important": [],
    "minor": [],
    "warnings": [],
    "stats": {}
}

# =================================================================
# 1. CROSS-REFERENCE INTEGRITY VALIDATION
# =================================================================
print("1. Cross-Reference Integrity Validation")
print("-" * 70)

# Build ID sets for lookup
evidence_ids = {e['evidence_id'] for e in data['evidence']}
claim_ids = {c['claim_id'] for c in data['claims']}
implicit_arg_ids = {ia['implicit_argument_id'] for ia in data['implicit_arguments']}
design_ids = {rd['research_design_id'] for rd in data['research_designs']}
method_ids = {m['method_id'] for m in data['methods']}
protocol_ids = {p['protocol_id'] for p in data['protocols']}

# Check claims → evidence references
broken_claim_evidence_refs = []
for claim in data['claims']:
    if 'supporting_evidence' in claim:
        for eid in claim['supporting_evidence']:
            if eid not in evidence_ids:
                broken_claim_evidence_refs.append(f"{claim['claim_id']}.supporting_evidence → {eid}")

# Check evidence → claims references
broken_evidence_claim_refs = []
for evidence in data['evidence']:
    if 'supports_claims' in evidence:
        for cid in evidence['supports_claims']:
            if cid not in claim_ids:
                broken_evidence_claim_refs.append(f"{evidence['evidence_id']}.supports_claims → {cid}")

# Check implicit_arguments → claims references
broken_implicit_claim_refs = []
for implicit_arg in data['implicit_arguments']:
    if 'related_claims' in implicit_arg:
        for cid in implicit_arg['related_claims']:
            if cid not in claim_ids:
                broken_implicit_claim_refs.append(f"{implicit_arg['implicit_argument_id']}.related_claims → {cid}")

if broken_claim_evidence_refs:
    validation_results['critical'].extend(broken_claim_evidence_refs)
    print(f"  ❌ CRITICAL: {len(broken_claim_evidence_refs)} broken claim→evidence references")
    for ref in broken_claim_evidence_refs:
        print(f"     {ref}")
else:
    print("  ✓ Claim→Evidence references: All valid")

if broken_evidence_claim_refs:
    validation_results['critical'].extend(broken_evidence_claim_refs)
    print(f"  ❌ CRITICAL: {len(broken_evidence_claim_refs)} broken evidence→claim references")
    for ref in broken_evidence_claim_refs:
        print(f"     {ref}")
else:
    print("  ✓ Evidence→Claim references: All valid")

if broken_implicit_claim_refs:
    validation_results['important'].extend(broken_implicit_claim_refs)
    print(f"  ⚠ IMPORTANT: {len(broken_implicit_claim_refs)} broken implicit_argument→claim references")
    for ref in broken_implicit_claim_refs:
        print(f"     {ref}")
else:
    print("  ✓ Implicit_Argument→Claim references: All valid")

print()

# =================================================================
# 2. RDMAP HIERARCHY VALIDATION
# =================================================================
print("2. RDMAP Hierarchy Validation")
print("-" * 70)

# Check protocols → methods
broken_protocol_method_refs = []
orphaned_protocols = []
for protocol in data['protocols']:
    if 'implements_method' in protocol:
        mid = protocol['implements_method']
        if mid not in method_ids:
            broken_protocol_method_refs.append(f"{protocol['protocol_id']}.implements_method → {mid}")
    else:
        orphaned_protocols.append(protocol['protocol_id'])

# Check methods → designs
broken_method_design_refs = []
orphaned_methods = []
for method in data['methods']:
    if 'implements_design' in method:
        did = method['implements_design']
        if did not in design_ids:
            broken_method_design_refs.append(f"{method['method_id']}.implements_design → {did}")
    else:
        orphaned_methods.append(method['method_id'])

# Check methods ← protocols linkage completeness
method_has_protocols = defaultdict(list)
for protocol in data['protocols']:
    if 'implements_method' in protocol:
        method_has_protocols[protocol['implements_method']].append(protocol['protocol_id'])

methods_without_protocols = []
for method in data['methods']:
    if method['method_id'] not in method_has_protocols:
        methods_without_protocols.append(method['method_id'])

# Check designs ← methods linkage completeness
design_has_methods = defaultdict(list)
for method in data['methods']:
    if 'implements_design' in method:
        design_has_methods[method['implements_design']].append(method['method_id'])

designs_without_methods = []
for design in data['research_designs']:
    if design['research_design_id'] not in design_has_methods:
        designs_without_methods.append(design['research_design_id'])

if broken_protocol_method_refs:
    validation_results['critical'].extend(broken_protocol_method_refs)
    print(f"  ❌ CRITICAL: {len(broken_protocol_method_refs)} broken protocol→method references")
    for ref in broken_protocol_method_refs:
        print(f"     {ref}")
else:
    print("  ✓ Protocol→Method references: All valid")

if broken_method_design_refs:
    validation_results['critical'].extend(broken_method_design_refs)
    print(f"  ❌ CRITICAL: {len(broken_method_design_refs)} broken method→design references")
    for ref in broken_method_design_refs:
        print(f"     {ref}")
else:
    print("  ✓ Method→Design references: All valid")

if orphaned_protocols:
    validation_results['warnings'].extend([f"Orphaned protocol: {pid}" for pid in orphaned_protocols])
    print(f"  ⚠ WARNING: {len(orphaned_protocols)} orphaned protocols (no implements_method)")
    for pid in orphaned_protocols:
        print(f"     {pid}")
else:
    print("  ✓ No orphaned protocols")

if orphaned_methods:
    validation_results['warnings'].extend([f"Orphaned method: {mid}" for mid in orphaned_methods])
    print(f"  ⚠ WARNING: {len(orphaned_methods)} orphaned methods (no implements_design)")
    for mid in orphaned_methods:
        print(f"     {mid}")
else:
    print("  ✓ No orphaned methods")

if methods_without_protocols:
    validation_results['warnings'].extend([f"Method without protocols: {mid}" for mid in methods_without_protocols])
    print(f"  ⚠ WARNING: {len(methods_without_protocols)} methods without child protocols")
    for mid in methods_without_protocols:
        print(f"     {mid}")
else:
    print("  ✓ All methods have child protocols")

if designs_without_methods:
    validation_results['warnings'].extend([f"Design without methods: {did}" for did in designs_without_methods])
    print(f"  ⚠ WARNING: {len(designs_without_methods)} designs without child methods")
    for did in designs_without_methods:
        print(f"     {did}")
else:
    print("  ✓ All designs have child methods")

print()

# =================================================================
# 3. SCHEMA COMPLIANCE VALIDATION
# =================================================================
print("3. Schema Compliance Validation")
print("-" * 70)

schema_violations = []

# Check evidence required fields
for evidence in data['evidence']:
    eid = evidence['evidence_id']
    if 'content' not in evidence or not evidence['content']:
        schema_violations.append(f"{eid}: missing content")
    if 'evidence_type' not in evidence:
        schema_violations.append(f"{eid}: missing evidence_type")
    if 'page' not in evidence:
        schema_violations.append(f"{eid}: missing page")

# Check claims required fields
for claim in data['claims']:
    cid = claim['claim_id']
    if 'content' not in claim or not claim['content']:
        schema_violations.append(f"{cid}: missing content")
    if 'claim_type' not in claim:
        schema_violations.append(f"{cid}: missing claim_type")
    if 'page' not in claim:
        schema_violations.append(f"{cid}: missing page")

# Check implicit_arguments required fields
for implicit_arg in data['implicit_arguments']:
    iaid = implicit_arg['implicit_argument_id']
    if 'content' not in implicit_arg or not implicit_arg['content']:
        schema_violations.append(f"{iaid}: missing content")
    if 'page' not in implicit_arg:
        schema_violations.append(f"{iaid}: missing page")

# Check RDMAP required fields
for design in data['research_designs']:
    did = design['research_design_id']
    if 'content' not in design or not design['content']:
        schema_violations.append(f"{did}: missing content")
    if 'page' not in design:
        schema_violations.append(f"{did}: missing page")

for method in data['methods']:
    mid = method['method_id']
    if 'content' not in method or not method['content']:
        schema_violations.append(f"{mid}: missing content")
    if 'page' not in method:
        schema_violations.append(f"{mid}: missing page")

for protocol in data['protocols']:
    pid = protocol['protocol_id']
    if 'content' not in protocol or not protocol['content']:
        schema_violations.append(f"{pid}: missing content")
    if 'page' not in protocol:
        schema_violations.append(f"{pid}: missing page")

if schema_violations:
    validation_results['critical'].extend(schema_violations)
    print(f"  ❌ CRITICAL: {len(schema_violations)} schema violations")
    for violation in schema_violations[:10]:  # Show first 10
        print(f"     {violation}")
    if len(schema_violations) > 10:
        print(f"     ... and {len(schema_violations) - 10} more")
else:
    print("  ✓ All required fields present")

print()

# =================================================================
# 4. SOURCING COMPLETENESS VALIDATION
# =================================================================
print("4. Sourcing Completeness Validation")
print("-" * 70)

sourcing_violations = []

# Check explicit items have verbatim_quote
for evidence in data['evidence']:
    eid = evidence['evidence_id']
    status = evidence.get('status', 'explicit')
    if status == 'explicit':
        if 'verbatim_quote' not in evidence or not evidence['verbatim_quote']:
            sourcing_violations.append(f"{eid}: explicit evidence missing verbatim_quote")

for claim in data['claims']:
    cid = claim['claim_id']
    status = claim.get('status', 'explicit')
    if status == 'explicit':
        if 'verbatim_quote' not in claim or not claim['verbatim_quote']:
            sourcing_violations.append(f"{cid}: explicit claim missing verbatim_quote")

for design in data['research_designs']:
    did = design['research_design_id']
    status = design.get('status', 'explicit')
    if status == 'explicit':
        if 'verbatim_quote' not in design or not design['verbatim_quote']:
            sourcing_violations.append(f"{did}: explicit design missing verbatim_quote")

for method in data['methods']:
    mid = method['method_id']
    status = method.get('status', 'explicit')
    if status == 'explicit':
        if 'verbatim_quote' not in method or not method['verbatim_quote']:
            sourcing_violations.append(f"{mid}: explicit method missing verbatim_quote")

for protocol in data['protocols']:
    pid = protocol['protocol_id']
    status = protocol.get('status', 'explicit')
    if status == 'explicit':
        if 'verbatim_quote' not in protocol or not protocol['verbatim_quote']:
            sourcing_violations.append(f"{pid}: explicit protocol missing verbatim_quote")

# Check implicit items have trigger_text
for implicit_arg in data['implicit_arguments']:
    iaid = implicit_arg['implicit_argument_id']
    if 'trigger_text' not in implicit_arg or not implicit_arg['trigger_text']:
        sourcing_violations.append(f"{iaid}: implicit argument missing trigger_text")

for protocol in data['protocols']:
    pid = protocol['protocol_id']
    status = protocol.get('status', 'explicit')
    if status == 'implicit':
        if 'trigger_text' not in protocol or not protocol['trigger_text']:
            sourcing_violations.append(f"{pid}: implicit protocol missing trigger_text")

for method in data['methods']:
    mid = method['method_id']
    status = method.get('status', 'explicit')
    if status == 'implicit':
        if 'trigger_text' not in method or not method['trigger_text']:
            sourcing_violations.append(f"{mid}: implicit method missing trigger_text")

if sourcing_violations:
    validation_results['critical'].extend(sourcing_violations)
    print(f"  ❌ CRITICAL: {len(sourcing_violations)} sourcing violations")
    for violation in sourcing_violations[:10]:  # Show first 10
        print(f"     {violation}")
    if len(sourcing_violations) > 10:
        print(f"     ... and {len(sourcing_violations) - 10} more")
else:
    print("  ✓ 100% sourcing completeness achieved")

# Calculate sourcing statistics
total_explicit = sum([
    len([e for e in data['evidence'] if e.get('status', 'explicit') == 'explicit']),
    len([c for c in data['claims'] if c.get('status', 'explicit') == 'explicit']),
    len([d for d in data['research_designs'] if d.get('status', 'explicit') == 'explicit']),
    len([m for m in data['methods'] if m.get('status', 'explicit') == 'explicit']),
    len([p for p in data['protocols'] if p.get('status', 'explicit') == 'explicit'])
])

total_implicit = sum([
    len(data['implicit_arguments']),
    len([m for m in data['methods'] if m.get('status') == 'implicit']),
    len([p for p in data['protocols'] if p.get('status') == 'implicit'])
])

total_items = total_explicit + total_implicit
print(f"  Total items: {total_items} ({total_explicit} explicit + {total_implicit} implicit)")

print()

# =================================================================
# 5. PAGE NUMBER VALIDITY
# =================================================================
print("5. Page Number Validity")
print("-" * 70)

invalid_pages = []

# Check all items have valid page numbers
for evidence in data['evidence']:
    if 'page' in evidence:
        page = evidence['page']
        if not isinstance(page, int) or page < 1:
            invalid_pages.append(f"{evidence['evidence_id']}: invalid page {page}")

for claim in data['claims']:
    if 'page' in claim:
        page = claim['page']
        if not isinstance(page, int) or page < 1:
            invalid_pages.append(f"{claim['claim_id']}: invalid page {page}")

for implicit_arg in data['implicit_arguments']:
    if 'page' in implicit_arg:
        page = implicit_arg['page']
        if not isinstance(page, int) or page < 1:
            invalid_pages.append(f"{implicit_arg['implicit_argument_id']}: invalid page {page}")

for design in data['research_designs']:
    if 'page' in design:
        page = design['page']
        if not isinstance(page, int) or page < 1:
            invalid_pages.append(f"{design['research_design_id']}: invalid page {page}")

for method in data['methods']:
    if 'page' in method:
        page = method['page']
        if not isinstance(page, int) or page < 1:
            invalid_pages.append(f"{method['method_id']}: invalid page {page}")

for protocol in data['protocols']:
    if 'page' in protocol:
        page = protocol['page']
        if not isinstance(page, int) or page < 1:
            invalid_pages.append(f"{protocol['protocol_id']}: invalid page {page}")

if invalid_pages:
    validation_results['minor'].extend(invalid_pages)
    print(f"  ⚠ MINOR: {len(invalid_pages)} invalid page numbers")
    for issue in invalid_pages[:10]:
        print(f"     {issue}")
    if len(invalid_pages) > 10:
        print(f"     ... and {len(invalid_pages) - 10} more")
else:
    print("  ✓ All page numbers valid")

print()

# =================================================================
# 6. METADATA COMPLETENESS VALIDATION
# =================================================================
print("6. Metadata Completeness Validation")
print("-" * 70)

metadata_issues = []

# Check project_metadata exists
if 'project_metadata' not in data:
    metadata_issues.append("project_metadata object missing from extraction.json")
    validation_results['critical'].append("Missing project_metadata")
else:
    metadata = data['project_metadata']

    # Check required fields are present and non-empty
    required_fields = ['paper_title', 'authors', 'publication_year', 'journal',
                       'paper_type', 'discipline', 'research_context']

    for field in required_fields:
        if field not in metadata:
            metadata_issues.append(f"Missing required field: {field}")
            validation_results['important'].append(f"project_metadata missing {field}")
        elif not metadata[field]:
            metadata_issues.append(f"Empty required field: {field}")
            validation_results['important'].append(f"project_metadata {field} is empty")

    # Check authors array
    if 'authors' in metadata:
        if not isinstance(metadata['authors'], list):
            metadata_issues.append("authors must be an array")
            validation_results['important'].append("project_metadata authors not an array")
        elif len(metadata['authors']) == 0:
            metadata_issues.append("authors array is empty")
            validation_results['important'].append("project_metadata authors array empty")
        else:
            # Check for initial format instead of full names
            for author in metadata['authors']:
                # Check if author has period not followed by lowercase (likely initial)
                if '.' in author:
                    parts = author.split('.')
                    for i, part in enumerate(parts[:-1]):  # All parts except last
                        if part and part[-1].isupper():
                            # Last char before period is uppercase - likely initial
                            metadata_issues.append(f"Author may be in initial format: {author}")
                            validation_results['warnings'].append(f"Author possibly in initial format: {author}")
                            break

    # Check publication_year is integer
    if 'publication_year' in metadata:
        if not isinstance(metadata['publication_year'], int):
            metadata_issues.append(f"publication_year must be integer, got {type(metadata['publication_year']).__name__}")
            validation_results['important'].append("publication_year not integer")
        elif metadata['publication_year'] < 1900 or metadata['publication_year'] > 2030:
            metadata_issues.append(f"publication_year {metadata['publication_year']} outside reasonable range (1900-2030)")
            validation_results['warnings'].append(f"publication_year {metadata['publication_year']} unusual")

    # Check journal includes volume/pages
    if 'journal' in metadata and metadata['journal']:
        if not any(indicator in metadata['journal'].lower() for indicator in ['vol', 'pp', 'pages', 'p.']):
            metadata_issues.append("journal field should include volume and pages")
            validation_results['warnings'].append("journal field missing volume/pages")

    # Check research_context is substantive
    if 'research_context' in metadata and metadata['research_context']:
        word_count = len(metadata['research_context'].split())
        if word_count < 10:
            metadata_issues.append(f"research_context too short ({word_count} words, should be 1-2 sentences)")
            validation_results['warnings'].append("research_context too short")

    # DOI can be null or string, both are valid

if metadata_issues:
    issue_levels = []
    if any('Missing required field' in issue or 'Empty required field' in issue for issue in metadata_issues):
        issue_levels.append("IMPORTANT")
    if any('may be in initial format' in issue.lower() for issue in metadata_issues):
        issue_levels.append("WARNING")

    level_str = " & ".join(set(issue_levels)) if issue_levels else "ISSUES"
    print(f"  ⚠ {level_str}: {len(metadata_issues)} metadata completeness issues")
    for issue in metadata_issues:
        print(f"     {issue}")
else:
    print("  ✓ Metadata completeness: All required fields present and valid")

print()

# =================================================================
# VALIDATION SUMMARY
# =================================================================
print("=" * 70)
print("VALIDATION SUMMARY")
print("=" * 70)

critical_count = len(validation_results['critical'])
important_count = len(validation_results['important'])
minor_count = len(validation_results['minor'])
warning_count = len(validation_results['warnings'])

total_issues = critical_count + important_count + minor_count + warning_count

print(f"Critical issues: {critical_count}")
print(f"Important issues: {important_count}")
print(f"Minor issues: {minor_count}")
print(f"Warnings: {warning_count}")
print(f"Total issues: {total_issues}")
print()

# Determine validation status
if critical_count > 0:
    validation_status = "FAIL"
    print("❌ VALIDATION STATUS: FAIL (critical issues present)")
elif important_count > 0:
    validation_status = "WARN"
    print("⚠ VALIDATION STATUS: WARN (important issues present)")
elif minor_count > 0 or warning_count > 0:
    validation_status = "PASS_WITH_WARNINGS"
    print("✓ VALIDATION STATUS: PASS (with warnings)")
else:
    validation_status = "PASS"
    print("✓✓✓ VALIDATION STATUS: PASS (no issues)")

print()

# =================================================================
# UPDATE EXTRACTION FILE
# =================================================================

validation_results['stats'] = {
    'total_items': total_items,
    'explicit_items': total_explicit,
    'implicit_items': total_implicit,
    'cross_reference_checks': {
        'claim_evidence_refs': len(data['claims']),
        'evidence_claim_refs': len(data['evidence']),
        'implicit_claim_refs': len(data['implicit_arguments'])
    },
    'rdmap_hierarchy_checks': {
        'protocol_method_refs': len(data['protocols']),
        'method_design_refs': len(data['methods']),
        'designs_with_methods': len(design_has_methods),
        'methods_with_protocols': len(method_has_protocols)
    }
}

data['extraction_notes']['pass6_validation'] = {
    'completion_date': datetime.now(timezone.utc).isoformat(),
    'validation_status': validation_status,
    'issue_counts': {
        'critical': critical_count,
        'important': important_count,
        'minor': minor_count,
        'warnings': warning_count,
        'total': total_issues
    },
    'validation_results': validation_results,
    'notes': f"Comprehensive validation checks performed. Status: {validation_status}. Total items validated: {total_items} ({total_explicit} explicit + {total_implicit} implicit)."
}

data['extraction_timestamp'] = datetime.now(timezone.utc).isoformat()

with open(extraction_file, 'w') as f:
    json.dump(data, f, indent=2)

print("Validation results saved to extraction.json")
print("=" * 70)
