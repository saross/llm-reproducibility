# Batch Analysis: Structural Assessment

## Purpose

This directory contains the **initial structural analysis** of the 10-paper pilot corpus, performed before detailed three-pass assessments.

## Assessment Type: Structural (Phase 1)

**What was assessed:**
- Item counts (evidence, claims, methods, protocols, research designs)
- Claims-to-Evidence (C:E) ratios
- Relationship mapping presence and counts
- Schema field naming consistency
- Sample verbatim quote verification (sobotkova-et-al-2024 only)

**What was NOT assessed:**
- Full accuracy verification of all items against source text
- Granularity appropriateness (over/under-splitting)
- Mapping quality (strong vs weak relationships)

**Method:** Automated structural analysis with sample detailed verification

**Time investment:** ~3 hours for all 10 papers

## Key Findings

**Critical patterns identified:**
1. **30% missing ALL mappings** (3/10 papers) - Pass 6 workflow failure
2. **40% extreme C:E ratios** (>2.5:1) - extraction methodology issues
3. **Schema inconsistencies** - field naming evolution across extractions
4. **Verbatim quote fidelity** - 33% non-exact matches (sample)
5. **Bidirectional mapping inconsistency** - potential data integrity issues

**Grade distribution:** 5 A's, 2 B's, 1 D, 2 F's (70% pass rate based on structural metrics)

## Files

- **STRUCTURAL_SUMMARY.md** - Comprehensive narrative report with failure patterns
- **structural-summary.json** - Structured JSON with prioritised recommendations
- **batch-metrics.json** - Raw metrics for all 10 papers
- **generate-batch-reports.py** - Script that generated individual structural reports

## Relationship to Detailed Assessment

This structural analysis provided:
- ✅ Efficient cross-paper pattern identification
- ✅ Prioritisation for detailed assessment (flagged critical failures)
- ✅ Baseline metrics for comparison

The **detailed three-pass assessments** (Pass A/B/C) complement this work by:
- Verifying accuracy of every extracted item against source
- Assessing granularity appropriateness
- Evaluating mapping quality (not just presence)
- Providing item-level error analysis

See `outputs/DETAILED_ASSESSMENT_SUMMARY.md` for the comprehensive analysis combining both approaches.

## Next Steps

1. Full Pass A/B/C assessments on all 10 papers (individual reports in `outputs/{paper-id}/assessment/`)
2. Comprehensive summary comparing structural vs detailed findings
3. Updated failure pattern analysis with accuracy/granularity insights
4. Refined recommendations for prompts/skill/schema improvement
