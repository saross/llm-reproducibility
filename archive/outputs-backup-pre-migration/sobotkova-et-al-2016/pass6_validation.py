#!/usr/bin/env python3
"""
Pass 6 Validation for sobotkova-et-al-2016
Comprehensive integrity checks on rationalized extraction
"""

import json
from datetime import datetime
from collections import defaultdict

# Load extraction
with open('outputs/sobotkova-et-al-2016/extraction.json', 'r') as f:
    data = json.load(f)

print("=" * 80)
print("PASS 6 VALIDATION")
print("=" * 80)
print()

# Initialize validation report
report = {
    'validation_timestamp': datetime.now().isoformat(),
    'validator': 'Claude Sonnet 4.5',
    'schema_version': data.get('schema_version', 'unknown'),
    'paper_id': data.get('paper_id', 'unknown'),
    'validation_summary': {
        'overall_status': 'PASS',
        'critical_issues': 0,
        'important_issues': 0,
        'minor_issues': 0,
        'warnings': 0
    },
    'cross_reference_integrity': {
        'broken_references': [],
        'bidirectional_inconsistencies': [],
        'orphaned_objects': []
    },
    'hierarchy_validation': {
        'rdmap_hierarchy_issues': [],
        'claims_hierarchy_issues': [],
        'evidence_chain_issues': []
    },
    'schema_compliance': {
        'missing_required_fields': [],
        'invalid_enum_values': [],
        'id_format_errors': [],
        'location_structure_issues': []
    },
    'source_verification': {
        'rdmap_source_issues': [],
        'evidence_source_issues': [],
        'claims_source_issues': [],
        'implicit_argument_source_issues': [],
        'metrics': {}
    },
    'expected_information_completeness': {
        'critical_gaps': [],
        'important_gaps': [],
        'minor_gaps': []
    },
    'consolidation_verification': {
        'metadata_issues': [],
        'source_integrity_issues': []
    },
    'type_consistency': {
        'design_type_mismatches': [],
        'method_type_mismatches': [],
        'status_sourcing_mismatches': []
    },
    'recommendations': []
}

print("Running validation checks...")
print()

# Check 1: Cross-Reference Integrity
print("1. Cross-Reference Integrity...")

# Build ID sets
rd_ids = {rd['design_id'] for rd in data.get('research_designs', [])}
m_ids = {m['method_id'] for m in data.get('methods', [])}
p_ids = {p['protocol_id'] for p in data.get('protocols', [])}
c_ids = {c['claim_id'] for c in data.get('claims', [])}
e_ids = {e['evidence_id'] for e in data.get('evidence', [])}
ia_ids = {ia['implicit_argument_id'] for ia in data.get('implicit_arguments', [])}

# Check Design → Method references
for rd in data.get('research_designs', []):
    if rd.get('enables_methods'):
        for mid in rd.get('enables_methods', []):
            if mid not in m_ids:
                report['cross_reference_integrity']['broken_references'].append({
                    'source_id': rd['design_id'],
                    'target_id': mid,
                    'reference_type': 'enables_methods',
                    'severity': 'critical'
                })
                report['validation_summary']['critical_issues'] += 1

# Check Method → Design references (bidirectional)
for m in data.get('methods', []):
    if m.get('implements_design'):
        design_id = m.get('implements_design')
        if design_id not in rd_ids:
            report['cross_reference_integrity']['broken_references'].append({
                'source_id': m['method_id'],
                'target_id': design_id,
                'reference_type': 'implements_design',
                'severity': 'critical'
            })
            report['validation_summary']['critical_issues'] += 1

# Check Method → Protocol references
for m in data.get('methods', []):
    if m.get('realized_through_protocols'):
        for pid in m.get('realized_through_protocols', []):
            if pid not in p_ids:
                report['cross_reference_integrity']['broken_references'].append({
                    'source_id': m['method_id'],
                    'target_id': pid,
                    'reference_type': 'realized_through_protocols',
                    'severity': 'critical'
                })
                report['validation_summary']['critical_issues'] += 1

# Check Protocol → Method references (bidirectional)
for p in data.get('protocols', []):
    if p.get('implements_method'):
        # Handle both string and array formats for backward compatibility
        method_refs = p.get('implements_method')
        if isinstance(method_refs, str):
            method_refs = [method_refs] if method_refs else []
        elif method_refs is None:
            method_refs = []

        for mid in method_refs:
            if mid and mid not in m_ids:
                report['cross_reference_integrity']['broken_references'].append({
                    'source_id': p['protocol_id'],
                    'target_id': mid,
                    'reference_type': 'implements_method',
                    'severity': 'critical'
                })
                report['validation_summary']['critical_issues'] += 1

# Check Claim → Evidence references
for c in data.get('claims', []):
    if c.get('supported_by_evidence'):
        for eid in c.get('supported_by_evidence', []):
            if eid not in e_ids:
                report['cross_reference_integrity']['broken_references'].append({
                    'source_id': c['claim_id'],
                    'target_id': eid,
                    'reference_type': 'supported_by_evidence',
                    'severity': 'critical'
                })
                report['validation_summary']['critical_issues'] += 1

print(f"   Broken references: {len(report['cross_reference_integrity']['broken_references'])}")

# Check 2: Hierarchy Validation
print("2. Hierarchy Validation...")

# Check Protocol-Method linking completeness
protocols_with_methods = sum(1 for p in data.get('protocols', []) if p.get('implements_method'))
total_protocols = len(data.get('protocols', []))
linking_rate = (protocols_with_methods / total_protocols * 100) if total_protocols > 0 else 0

if linking_rate < 50:
    report['hierarchy_validation']['rdmap_hierarchy_issues'].append({
        'issue': 'Low protocol-method linking rate',
        'details': f'{linking_rate:.1f}% of protocols linked to methods',
        'severity': 'critical'
    })
    report['validation_summary']['critical_issues'] += 1
elif linking_rate < 80:
    report['hierarchy_validation']['rdmap_hierarchy_issues'].append({
        'issue': 'Incomplete protocol-method linking',
        'details': f'{linking_rate:.1f}% of protocols linked to methods',
        'severity': 'important'
    })
    report['validation_summary']['important_issues'] += 1

print(f"   Protocol-method linking rate: {linking_rate:.1f}%")

# Check orphaned methods (methods without design)
orphaned_methods = [m['method_id'] for m in data.get('methods', []) if not m.get('implements_design')]
if orphaned_methods:
    report['cross_reference_integrity']['orphaned_objects'].append({
        'type': 'methods',
        'ids': orphaned_methods,
        'severity': 'critical'
    })
    report['validation_summary']['critical_issues'] += len(orphaned_methods)

print(f"   Orphaned methods: {len(orphaned_methods)}")

# Check 3: Schema Compliance
print("3. Schema Compliance...")

# Check required fields for RDMAP
for rd in data.get('research_designs', []):
    if not rd.get('design_id'):
        report['schema_compliance']['missing_required_fields'].append({
            'object_id': rd.get('design_id', 'unknown'),
            'object_type': 'research_design',
            'missing_field': 'design_id',
            'severity': 'critical'
        })
        report['validation_summary']['critical_issues'] += 1
    if not rd.get('design_name'):
        report['schema_compliance']['missing_required_fields'].append({
            'object_id': rd.get('design_id', 'unknown'),
            'object_type': 'research_design',
            'missing_field': 'design_name',
            'severity': 'critical'
        })
        report['validation_summary']['critical_issues'] += 1

# Check ID formats
for rd in data.get('research_designs', []):
    if not rd.get('design_id', '').startswith('RD'):
        report['schema_compliance']['id_format_errors'].append({
            'object_id': rd.get('design_id', 'unknown'),
            'object_type': 'research_design',
            'issue': 'ID must start with RD',
            'severity': 'critical'
        })
        report['validation_summary']['critical_issues'] += 1

for m in data.get('methods', []):
    if not m.get('method_id', '').startswith('M'):
        report['schema_compliance']['id_format_errors'].append({
            'object_id': m.get('method_id', 'unknown'),
            'object_type': 'method',
            'issue': 'ID must start with M',
            'severity': 'critical'
        })
        report['validation_summary']['critical_issues'] += 1

for p in data.get('protocols', []):
    if not p.get('protocol_id', '').startswith('P'):
        report['schema_compliance']['id_format_errors'].append({
            'object_id': p.get('protocol_id', 'unknown'),
            'object_type': 'protocol',
            'issue': 'ID must start with P',
            'severity': 'critical'
        })
        report['validation_summary']['critical_issues'] += 1

print(f"   Missing required fields: {len(report['schema_compliance']['missing_required_fields'])}")
print(f"   ID format errors: {len(report['schema_compliance']['id_format_errors'])}")

# Check 4: Source Verification
print("4. Source Verification...")

# RDMAP source verification
rdmap_verified = {'explicit': {'pass': 0, 'total': 0}, 'implicit': {'pass': 0, 'total': 0}}

# Research Designs
for rd in data.get('research_designs', []):
    status = rd.get('design_status', 'explicit')

    if status == 'explicit':
        rdmap_verified['explicit']['total'] += 1
        if rd.get('verbatim_quote'):
            rdmap_verified['explicit']['pass'] += 1
        else:
            report['source_verification']['rdmap_source_issues'].append({
                'object_id': rd['design_id'],
                'issue': 'Missing verbatim_quote for explicit item',
                'severity': 'critical'
            })
            report['validation_summary']['critical_issues'] += 1

    elif status == 'implicit':
        rdmap_verified['implicit']['total'] += 1
        has_trigger = bool(rd.get('trigger_text'))
        has_locations = bool(rd.get('trigger_locations'))
        has_reasoning = bool(rd.get('inference_reasoning'))
        has_metadata = bool(rd.get('implicit_metadata'))

        if has_trigger and has_locations and has_reasoning and has_metadata:
            rdmap_verified['implicit']['pass'] += 1
        else:
            missing = []
            if not has_trigger: missing.append('trigger_text')
            if not has_locations: missing.append('trigger_locations')
            if not has_reasoning: missing.append('inference_reasoning')
            if not has_metadata: missing.append('implicit_metadata')

            report['source_verification']['rdmap_source_issues'].append({
                'object_id': rd['design_id'],
                'issue': f'Missing implicit infrastructure: {", ".join(missing)}',
                'severity': 'critical'
            })
            report['validation_summary']['critical_issues'] += 1

# Methods
for m in data.get('methods', []):
    status = m.get('method_status', 'explicit')

    if status == 'explicit':
        rdmap_verified['explicit']['total'] += 1
        if m.get('verbatim_quote'):
            rdmap_verified['explicit']['pass'] += 1
        else:
            report['source_verification']['rdmap_source_issues'].append({
                'object_id': m['method_id'],
                'issue': 'Missing verbatim_quote for explicit item',
                'severity': 'critical'
            })
            report['validation_summary']['critical_issues'] += 1

    elif status == 'implicit':
        rdmap_verified['implicit']['total'] += 1
        has_trigger = bool(m.get('trigger_text'))
        has_locations = bool(m.get('trigger_locations'))
        has_reasoning = bool(m.get('inference_reasoning'))
        has_metadata = bool(m.get('implicit_metadata'))

        if has_trigger and has_locations and has_reasoning and has_metadata:
            rdmap_verified['implicit']['pass'] += 1
        else:
            missing = []
            if not has_trigger: missing.append('trigger_text')
            if not has_locations: missing.append('trigger_locations')
            if not has_reasoning: missing.append('inference_reasoning')
            if not has_metadata: missing.append('implicit_metadata')

            report['source_verification']['rdmap_source_issues'].append({
                'object_id': m['method_id'],
                'issue': f'Missing implicit infrastructure: {", ".join(missing)}',
                'severity': 'critical'
            })
            report['validation_summary']['critical_issues'] += 1

# Protocols
for p in data.get('protocols', []):
    status = p.get('protocol_status', 'explicit')

    if status == 'explicit':
        rdmap_verified['explicit']['total'] += 1
        if p.get('verbatim_quote'):
            rdmap_verified['explicit']['pass'] += 1
        else:
            report['source_verification']['rdmap_source_issues'].append({
                'object_id': p['protocol_id'],
                'issue': 'Missing verbatim_quote for explicit item',
                'severity': 'critical'
            })
            report['validation_summary']['critical_issues'] += 1

    elif status == 'implicit':
        rdmap_verified['implicit']['total'] += 1
        has_trigger = bool(p.get('trigger_text'))
        has_locations = bool(p.get('trigger_locations'))
        has_reasoning = bool(p.get('inference_reasoning'))
        has_metadata = bool(p.get('implicit_metadata'))

        if has_trigger and has_locations and has_reasoning and has_metadata:
            rdmap_verified['implicit']['pass'] += 1
        else:
            missing = []
            if not has_trigger: missing.append('trigger_text')
            if not has_locations: missing.append('trigger_locations')
            if not has_reasoning: missing.append('inference_reasoning')
            if not has_metadata: missing.append('implicit_metadata')

            report['source_verification']['rdmap_source_issues'].append({
                'object_id': p['protocol_id'],
                'issue': f'Missing implicit infrastructure: {", ".join(missing)}',
                'severity': 'critical'
            })
            report['validation_summary']['critical_issues'] += 1

# Calculate pass rates
explicit_pass_rate = (rdmap_verified['explicit']['pass'] / rdmap_verified['explicit']['total'] * 100) if rdmap_verified['explicit']['total'] > 0 else 100
implicit_pass_rate = (rdmap_verified['implicit']['pass'] / rdmap_verified['implicit']['total'] * 100) if rdmap_verified['implicit']['total'] > 0 else 100

report['source_verification']['metrics'] = {
    'rdmap': {
        'explicit_pass_rate': round(explicit_pass_rate, 1),
        'implicit_pass_rate': round(implicit_pass_rate, 1),
        'explicit_total': rdmap_verified['explicit']['total'],
        'implicit_total': rdmap_verified['implicit']['total']
    }
}

print(f"   RDMAP explicit pass rate: {explicit_pass_rate:.1f}%")
print(f"   RDMAP implicit pass rate: {implicit_pass_rate:.1f}%")

# Check 5: Consolidation Metadata
print("5. Consolidation Metadata...")

# Check Pass 2 consolidations (claims/evidence)
for e in data.get('evidence', []):
    if e.get('consolidation_metadata'):
        if not e['consolidation_metadata'].get('consolidated_from'):
            report['consolidation_verification']['metadata_issues'].append({
                'object_id': e['evidence_id'],
                'issue': 'Missing consolidated_from array',
                'severity': 'important'
            })
            report['validation_summary']['important_issues'] += 1

# Check Pass 5 consolidations (RDMAP)
for m in data.get('methods', []):
    if m.get('consolidation_metadata'):
        if not m['consolidation_metadata'].get('consolidated_from'):
            report['consolidation_verification']['metadata_issues'].append({
                'object_id': m['method_id'],
                'issue': 'Missing consolidated_from array',
                'severity': 'important'
            })
            report['validation_summary']['important_issues'] += 1

print(f"   Consolidation metadata issues: {len(report['consolidation_verification']['metadata_issues'])}")

# Determine overall status
if report['validation_summary']['critical_issues'] > 0:
    if report['validation_summary']['critical_issues'] > 5:
        report['validation_summary']['overall_status'] = 'FAIL'
    else:
        report['validation_summary']['overall_status'] = 'PASS_WITH_ISSUES'
elif report['validation_summary']['important_issues'] > 0:
    report['validation_summary']['overall_status'] = 'PASS_WITH_ISSUES'
else:
    report['validation_summary']['overall_status'] = 'PASS'

# Generate recommendations
if report['validation_summary']['critical_issues'] == 0 and report['validation_summary']['important_issues'] == 0:
    report['recommendations'].append('Extraction passed all validation checks. Ready for assessment.')
else:
    if report['cross_reference_integrity']['broken_references']:
        report['recommendations'].append('CRITICAL: Repair broken cross-references before assessment.')
    if report['cross_reference_integrity']['orphaned_objects']:
        report['recommendations'].append('CRITICAL: Link orphaned methods/protocols to RDMAP hierarchy.')
    if report['source_verification']['rdmap_source_issues']:
        report['recommendations'].append('CRITICAL: Fix RDMAP source verification issues.')
    if report['schema_compliance']['missing_required_fields']:
        report['recommendations'].append('CRITICAL: Populate missing required fields.')
    if report['consolidation_verification']['metadata_issues']:
        report['recommendations'].append('IMPORTANT: Complete consolidation metadata.')

# Save validation report
with open('outputs/sobotkova-et-al-2016/validation_report.json', 'w') as f:
    json.dump(report, f, indent=2)

# Print summary
print()
print("=" * 80)
print("VALIDATION SUMMARY")
print("=" * 80)
print()
print(f"Overall Status: {report['validation_summary']['overall_status']}")
print()
print(f"Issue Counts:")
print(f"  Critical: {report['validation_summary']['critical_issues']}")
print(f"  Important: {report['validation_summary']['important_issues']}")
print(f"  Minor: {report['validation_summary']['minor_issues']}")
print(f"  Warnings: {report['validation_summary']['warnings']}")
print()
print(f"RDMAP Source Verification:")
print(f"  Explicit pass rate: {report['source_verification']['metrics']['rdmap']['explicit_pass_rate']}%")
print(f"  Implicit pass rate: {report['source_verification']['metrics']['rdmap']['implicit_pass_rate']}%")
print()
print(f"Protocol-Method Linking: {linking_rate:.1f}%")
print()
print("Recommendations:")
for rec in report['recommendations']:
    print(f"  - {rec}")
print()
print("✓ Validation report saved to: outputs/sobotkova-et-al-2016/validation_report.json")
