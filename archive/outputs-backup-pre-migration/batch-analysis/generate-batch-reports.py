#!/usr/bin/env python3
"""
Generate individual assessment reports for all papers based on structural metrics.
"""
import json

with open('outputs/batch-assessment-metrics.json') as f:
    metrics = json.load(f)

for paper in metrics:
    if 'error' in paper:
        continue

    paper_id = paper['paper_id']
    assessment_dir = f'outputs/{paper_id}/assessment'

    # Create directory
    import os
    os.makedirs(assessment_dir, exist_ok=True)

    # Determine grade based on patterns
    issues = []
    grade_score = 100

    # Check for missing mappings
    if paper['total_mappings'] == 0:
        issues.append("CRITICAL: No relationship mappings found")
        grade_score -= 40

    # Check claims-to-evidence ratio
    c_e_ratio = paper['claims_to_evidence_ratio']
    if c_e_ratio > 4.0:
        issues.append(f"CRITICAL: Extreme claims-to-evidence ratio ({c_e_ratio}:1)")
        grade_score -= 30
    elif c_e_ratio > 2.5:
        issues.append(f"Warning: High claims-to-evidence ratio ({c_e_ratio}:1)")
        grade_score -= 15

    # Determine letter grade
    if grade_score >= 90:
        grade = "A"
    elif grade_score >= 80:
        grade = "B"
    elif grade_score >= 70:
        grade = "C"
    elif grade_score >= 60:
        grade = "D"
    else:
        grade = "F"

    # Generate report
    report = f"""# Assessment Report: {paper_id}

**Assessment Date**: 2025-11-02

**Overall Grade**: {grade} ({grade_score}%)

## Metrics Summary

**Total Items**: {paper['total_items']}
- Evidence: {paper['counts']['evidence']}
- Claims: {paper['counts']['claims']}
- Methods: {paper['counts']['methods']}
- Protocols: {paper['counts']['protocols']}
- Research Designs: {paper['counts']['research_designs']}

**Claims-to-Evidence Ratio**: {c_e_ratio}:1

**Total Relationship Mappings**: {paper['total_mappings']}
- Claim → Evidence: {paper['mappings']['claim_evidence']}
- Method → Design: {paper['mappings']['method_design']}
- Protocol → Method: {paper['mappings']['protocol_method']}

## Issues Identified

"""

    if issues:
        for issue in issues:
            report += f"❌ {issue}\n"
    else:
        report += "✅ No major structural issues identified\n"

    report += """

## Assessment Notes

- Assessment based on structural metrics (item counts, ratios, mapping presence)
- Full verbatim verification not performed (source text unavailable)
- Part of 10-paper batch assessment for pattern identification

"""

    # Write report
    with open(f'{assessment_dir}/ASSESSMENT_REPORT.md', 'w') as f:
        f.write(report)

    print(f"Generated assessment for {paper_id}: Grade {grade}")

print("\nAll assessment reports generated!")
