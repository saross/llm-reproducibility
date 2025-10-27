# Validation Prompt - PASS 3: Integrity Checks v2.5

**Version:** 2.5 Pass 3  
**Last Updated:** 2025-10-22  
**Workflow Stage:** Pass 3 of 3 - Automated validation of Pass 2 extraction  
**Update:** Added source verification checks for ALL object types including RDMAP (hallucination prevention)

---

## Your Task

Perform automated integrity checks on the rationalized extraction. Identify structural issues, broken references, schema violations, and completeness gaps. **Do NOT modify the extraction** - produce a validation report only.

**This is NOT quality assessment** - you are checking structural integrity, not methodological quality.

**Input:** JSON extraction document from Pass 2
- May contain only RDMAP arrays (RDMAP-only validation)
- May contain both RDMAP and claims/evidence arrays (unified validation)
- Validation adapts to what's present

**Your responsibility:** Validate whatever object types are present:
- If RDMAP arrays present → validate RDMAP thoroughly
- If claims/evidence arrays present → validate those too
- Cross-references between object types validated when both present
- Note when referenced arrays not yet extracted (deferred validation)

**Output:** Validation report in JSON format with issues categorized by severity

---

## 🚨 CRITICAL: Read Verification Procedures First

**READ FIRST:** `references/verification-procedures.md`

This file contains:
- Complete verification procedures for all object types (Evidence, Claims, Implicit Arguments, RDMAP)
- Decision trees for each verification check
- Worked examples (passes and fails)
- Quality metrics guidance
- Red flags for hallucination detection

**This prompt specifies WHAT to validate; the skill file explains HOW to validate.**

Pass 3 validation cannot be done correctly without these procedures. Read the entire verification-procedures.md file before beginning validation.

---

## Validation Checklist

Use this checklist as your roadmap. Execute all applicable checks:

**Cross-Reference Integrity:**
- [ ] All referenced IDs exist
- [ ] Bidirectional references consistent
- [ ] No orphaned objects (or appropriately flagged)

**Hierarchy Validation:**
- [ ] RDMAP chains valid (Design → Method → Protocol)
- [ ] Claims hierarchy valid (if claims present)
- [ ] Evidence chains valid (if evidence present)

**Schema Compliance:**
- [ ] Required fields present
- [ ] Enum values valid
- [ ] ID formats correct
- [ ] Location objects structured properly

**Source Verification:**
- [ ] All evidence/claims have verbatim_quote
- [ ] All implicit arguments have trigger_text and trigger_locations
- [ ] All RDMAP items properly sourced (explicit or implicit)
- [ ] Source verification fields populated
- [ ] Verification pass rates acceptable (>95%)

**Expected Information:**
- [ ] Missing information aggregated by category
- [ ] Critical gaps flagged for assessment blockers
- [ ] TIDieR/CONSORT completeness noted (if applicable)

**Consolidation Metadata:**
- [ ] All Pass 2 consolidations have complete metadata
- [ ] consolidated_from IDs traceable

**Type Consistency:**
- [ ] Design types align with content
- [ ] Method types align with content
- [ ] Status fields (explicit/implicit) consistent with sourcing

---

## Validation Philosophy

**Purpose:** Ensure extraction is structurally sound, internally consistent, and schema-compliant.

**Flexible validation:**
- Validates whatever object types are present in the extraction
- RDMAP-only: Validates research_designs, methods, protocols thoroughly
- Unified: Validates RDMAP + claims + evidence + implicit arguments
- Notes when cross-references point to not-yet-extracted arrays (deferred validation)

**Scope:**
- Cross-reference integrity (all IDs exist, bidirectional consistency)
- Hierarchy validation (Design → Methods → Protocols chains; Claims hierarchy)
- Schema compliance (required fields, valid enums, ID formats)
- Source verification (verbatim quotes, trigger text, verification completeness)
- Expected information completeness (aggregated gaps)
- Consolidation metadata consistency

**NOT in scope:**
- Quality of methodology (that's assessment phase)
- Completeness of extraction (Pass 1/2 handled that)
- Scientific validity of claims (that's assessment phase)

---

## Validation Checks

### 1. Cross-Reference Integrity

**Check all ID references point to existing objects.**

**What to verify:**
- `methods_used` in Research Designs → Methods exist
- `design_context` in Methods → Research Design exists
- `implements_methods` in Protocols → Methods exist
- `supporting_evidence` in Claims → Evidence exists
- `supports_claims` in Evidence → Claims exist
- `supports_implicit_arguments` in Evidence/Claims → Implicit Arguments exist

**Report bidirectional inconsistencies:**
- Design references Method but Method doesn't reference back
- Method references Design that doesn't exist

**Handle deferred validation:**
- Note when references point to not-yet-extracted arrays
- Don't fail validation for missing arrays when doing partial extraction

**For complete reference checking procedures:**  
→ See `references/verification-procedures.md`

---

### 2. Hierarchy Validation

**Verify RDMAP three-tier hierarchy integrity.**

**RDMAP chains (Design → Methods → Protocols):**
- Every Method references at least one Design
- Every Protocol references at least one Method (via `implements_methods` array)
- Protocols transitively connect to Designs through Methods

**Protocol-Method Linking Completeness:**
- Calculate: % of protocols with `implements_methods` populated
- **Critical** if <50% of protocols linked (likely prompt/schema issue)
- **Important** if 50-79% of protocols linked (incomplete extraction)
- **Pass** if ≥80% of protocols linked
- Report linking rate in validation summary

**Claims hierarchy (if present):**
- Primary claims may have no parent
- Secondary/tertiary claims must reference higher-tier parent
- No circular references in claim ancestry

**Evidence chains (if present):**
- Evidence references at least one Claim or Implicit Argument
- Evidence without references flagged (unless defensive extraction)

**Orphaned objects:**
- **Methods/Protocols without parent:** Critical issue (must connect to RDMAP hierarchy)
- **Designs without children:** Warning only (may indicate incomplete extraction)

**For detailed hierarchy rules and edge cases:**  
→ See `references/verification-procedures.md`

---

### 3. Schema Compliance

#### Check 3.1: Required Fields Present

**Verify all required fields populated.**

**RDMAP minimums (all objects):**
- ID string, text description
- `design_status`/`method_status`/`protocol_status` (explicit or implicit)
- Appropriate sourcing fields (verbatim_quote OR trigger_text/trigger_locations)
- `location` object with minimum {section, page}
- `extraction_confidence` (high, medium, low)

**Claims/Evidence minimums (if present):**
- ID, text, verbatim_quote, location, tier classification

**For complete field requirements:**  
→ See `references/schema/schema-guide.md`

---

#### Check 3.2: Enum Values Valid

**Check enum fields against schema v2.5 allowed values.**

**Critical enums (closed lists):**
- **Status fields:** explicit, implicit (RDMAP items)
- **Reasoning approaches:** inductive, abductive, deductive, mixed, unclear
- **Analysis populations:** all_collected, quality_filtered, outliers_excluded, complete_cases_only
- **Extraction confidence:** high, medium, low

**Open lists (flag uncommon but don't fail):**
- Study designs, sampling types, method categories

---

#### Check 3.3: ID Format Correctness

**Verify ID formats follow schema pattern.**

**Format rules:**
- Research Design: `RD###`
- Method: `M###`
- Protocol: `P###`
- Claims: `C###`
- Evidence: `E###`
- Implicit Arguments: `IA###`

---

#### Check 3.4: Location Object Structure

**Verify location objects have required fields.**

**Required:** `section` (string), `page` (number)  
**Recommended:** `paragraph` (number), `sentence_start` (number), `sentence_end` (number)

---

### 4. Source Verification

**🚨 CRITICAL: Read verification procedures from skill before proceeding**

All extracted items MUST pass source verification to prevent hallucinated content.

**READ FIRST:** `references/verification-procedures.md`

The skill contains complete procedures, decision trees, worked examples, and quality metrics. This section specifies WHAT to validate and HOW to report results.

---

#### Check 4.1: Evidence & Claims Verification

**Verify all evidence/claims have:**
- `verbatim_quote` populated (required field)
- `source_verification` object complete with fields: `location_verified`, `quote_verified`, `content_aligned`, `verification_notes`, `verified_by`

**Report critical issues:**
- Missing verbatim_quote
- Any source_verification field = false
- Include in `evidence_source_issues` array with id, issue description, severity "critical"

---

#### Check 4.2: Implicit Arguments Verification  

**Verify all implicit arguments have:**
- `trigger_text` and `trigger_locations` arrays populated (required fields)
- `source_verification` object complete with fields: `trigger_locations_verified`, `trigger_quotes_verified`, `inference_reasonable`, `verification_notes`, `verified_by`

**Report critical issues:**
- Missing trigger_text or trigger_locations
- Any source_verification field = false
- Include in `implicit_argument_source_issues` array with id, issue description, severity "critical"

---

#### Check 4.3: RDMAP Source Verification (NEW in v2.5)

**🚨 CRITICAL: RDMAP items require same sourcing discipline as Evidence/Claims**

Schema v2.5 requires all Research Designs, Methods, and Protocols to be properly sourced. Verify:

**For explicit RDMAP items (status = "explicit"):**
- `verbatim_quote` populated (required field, non-empty string)
- `source_verification` object complete with fields: `location_verified`, `quote_verified`, `content_aligned`, `verification_notes`, `verified_by`

**For implicit RDMAP items (status = "implicit"):**
- `trigger_text` array populated (required, minimum 1 passage)
- `trigger_locations` array populated (required, parallel to trigger_text)
- `inference_reasoning` populated (required, non-empty string)
- `implicit_metadata` object complete with required fields:
  - `basis`: "mentioned_undocumented" | "inferred_from_results"
  - `transparency_gap`: string
  - `assessability_impact`: string
  - `reconstruction_confidence`: "high" | "medium" | "low"
- `source_verification` object complete with fields: `trigger_locations_verified`, `trigger_quotes_verified`, `inference_reasonable`, `verification_notes`, `verified_by`

**Report critical issues:**
- Missing verbatim_quote for explicit items
- Missing trigger_text/trigger_locations/inference_reasoning for implicit items
- Any source_verification field = false
- Status field missing or invalid
- Include in `rdmap_source_issues` array with id, issue description, severity "critical"

**For complete RDMAP verification procedures:**  
→ See `references/verification-procedures.md` section on RDMAP sourcing validation

---

#### Check 4.4: Statistical Quality Metrics (EXPANDED for v2.5)

**Calculate and report pass rates for ALL object types.**

**Evidence & Claims:**
- Overall pass rate (all three verification checks pass)
- Per-check pass rates (location, quote, content alignment)
- Total items verified

**Implicit Arguments:**
- Overall pass rate (all three verification checks pass)
- Per-check pass rates (trigger locations, trigger quotes, inference reasonableness)
- Total items verified

**RDMAP (NEW in v2.5):**
- **Research Designs:** explicit pass rate, implicit pass rate, overall
- **Methods:** explicit pass rate, implicit pass rate, overall
- **Protocols:** explicit pass rate, implicit pass rate, overall
- **Combined RDMAP:** overall sourcing quality across all three tiers

**Quality thresholds:**
- Target: >95% overall pass rate (per object type)
- Warning: 90-95% pass rate 
- Critical: <90% pass rate (systematic quality issue)

**Include in report:** `source_verification_metrics` section with pass rates and status for all object types present.

---

#### Check 4.5: Cross-Type Consistency

**Flag inconsistencies:**
- Implicit arguments contradicting explicit evidence/claims
- trigger_text containing explicit statements (should be reclassified)
- Status fields (explicit/implicit) not matching sourcing approach
- RDMAP items with status="explicit" missing verbatim_quote
- RDMAP items with status="implicit" missing trigger infrastructure

→ See `references/verification-procedures.md` for complete verification procedures, decision trees, examples, and detailed metrics guidance.

---

### 5. Expected Information Completeness

#### Check 5.1: Aggregate Missing Information

**Aggregate all `expected_information_missing` arrays across objects.**

**Categorize by severity:**
- **Critical:** Assessment-blocking gaps (e.g., no sample size for quantitative claim, no tool specification for replication)
- **Important:** Transparency gaps (e.g., missing quality control procedures, no alternative methods considered)
- **Minor:** Recommended information (e.g., missing inter-observer reliability for qualitative data)

**Note:** Some "expected information" may be present as implicit RDMAP items. Missing information doesn't mean extraction error - it means the paper didn't document it. Items marked implicit already capture that the information is missing from Methods documentation.

**For complete domain-specific checklists:**  
→ See `references/checklists/expected-information.md`

---

#### Check 5.2: TIDieR/CONSORT Completeness (Optional)

**If methods reference TIDieR or CONSORT checklists, verify completeness.**

**TIDieR elements (10):** Rationale, Materials, Procedures, Personnel, Mode, Setting, Schedule, Tailoring, Modifications, Fidelity

**CONSORT-Outcomes elements (8):** Domain, Instrument, Metric, Aggregation, Time points, Reporter, Precision, Quality control

**Report as information, not failure.**

---

### 6. Consolidation Metadata Verification

#### Check 6.1: Consolidation Metadata Present and Complete

**Verify all Pass 2 consolidations documented.**

**Required consolidation_metadata fields:**
- `consolidated_from` (array of IDs)
- `consolidation_rationale` (string)
- `consolidation_date` (ISO string)

**Verify:**
- All IDs in `consolidated_from` were valid Pass 1 IDs
- Consolidation rationale explains similarity/redundancy
- At least 2 IDs consolidated (otherwise not a consolidation)

---

#### Check 6.2: Consolidation Source Integrity

**Verify consolidations preserve source integrity.**

**For consolidated explicit items:**
- `verbatim_quote` preserved or synthesized from sources
- All source quotes from same general location
- Source verification passed

**For consolidated implicit items:**
- All `trigger_text` passages preserved
- All `trigger_locations` included
- `inference_reasoning` updated to reflect consolidated understanding
- Most conservative `reconstruction_confidence` maintained

---

### 7. Type Consistency

**Verify object types align with content.**

**Research Design types:**
- Design type matches description (survey, excavation, experimental, etc.)
- Reasoning approach aligns with design type

**Method types:**
- Method category matches description (sampling, data_collection, analysis, etc.)
- Sampling methods have appropriate sample_size fields

**Flag mismatches:** Design described as "survey" but type="excavation"

---

## Validation Report Format

Output your validation report as JSON following the template structure:

**Template:** `extraction-system/templates/validation_report_template.json`

**Key sections to populate:**

1. **validation_summary:** Overall status (PASS/PASS_WITH_ISSUES/FAIL), issue counts by severity
2. **cross_reference_integrity:** Broken references, bidirectional inconsistencies, orphaned objects
3. **hierarchy_validation:** RDMAP tier issues, claims tier issues, evidence chain issues
4. **schema_compliance:** Missing fields, invalid enums, ID format errors, location structure issues
5. **source_verification:** Source issues + detailed pass rate metrics for all entity types
6. **expected_information_completeness:** Critical/important/minor gaps with summary counts
7. **consolidation_verification:** Consolidation metadata issues or inappropriate consolidations
8. **type_consistency:** Design type, method type, status/sourcing mismatches
9. **recommendations:** Prioritised actionable recommendations (most critical first)

**Ensure all counts accurate and all issues documented with sufficient detail for fixes.**

---

## Severity Levels

**Critical (blocks assessment):**
- Broken cross-references (referenced IDs don't exist)
- Missing required fields
- Invalid ID formats
- Orphaned protocols or methods without design
- Bidirectional reference inconsistencies
- Invalid closed-list enum values
- Missing verbatim_quote for explicit items
- Missing trigger infrastructure for implicit items
- Source verification failures

**Important (should fix but not blocking):**
- Incomplete bidirectional references
- Missing location details
- Incomplete consolidation metadata
- Critical expected information gaps
- Type/structure mismatches
- Status field inconsistencies

**Minor (good to fix):**
- Orphaned designs (may be acceptable)
- Location objects missing recommended fields
- Minor expected information gaps
- Uncommon but valid enum values

**Warnings (informational only):**
- Uncommon open-list enum values
- Very high/low expected information counts
- Unusual reasoning approach combinations

---

## Overall Status Determination

**PASS:** No critical or important issues  
**PASS_WITH_ISSUES:** Critical or important issues present but extraction usable  
**FAIL:** Critical issues make extraction unusable for assessment

**Note:** Deferred validation (references to not-yet-extracted arrays) should not cause FAIL status during partial extraction testing.

---

## Validation Goal

Produce comprehensive validation report identifying:
- All structural integrity issues
- Cross-reference problems
- Schema compliance violations
- Source verification quality (including RDMAP)
- Completeness gaps for transparency assessment
- Clear severity classifications
- Actionable recommendations for fixes

**Remember:** You are checking structure, not assessing methodology quality.