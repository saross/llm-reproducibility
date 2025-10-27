# Research Assessor v2.6.3 - Package Summary

**Package Date:** 2025-10-27
**Active Version:** `.claude/skills/research-assessor/` (used by Claude Code)
**Archive Version:** `extraction-system/skill/research-assessor/` (for reference/documentation)
**Previous Versions:** v2.6.1 (2025-10-25), v2.6 (2025-10-24)
**Size:** ~240 KB (uncompressed)

---

## What's New in v2.6.3

### Implicit RDMAP Improvements (2025-10-27)
✅ **Section-by-section extraction guidance** added to extraction-fundamentals.md
✅ **Recognition patterns** for implicit RDMAP:
  - VERBS without procedures (cleaned, validated, checked)
  - EFFECTS implying causes (performance degradation → monitoring)
  - MENTIONS without descriptions (assigned maps → assignment protocol)
  - Implied strategic decisions (comparative positioning)
✅ **Common mistakes section** prevents known failure modes
✅ **Cross-reference repair procedure** in consolidation-patterns.md (MANDATORY)
✅ **Template scripts** created:
  - `extraction-system/scripts/extraction/consolidation_template.py`
  - `extraction-system/scripts/extraction/section_rdmap_template.py`
✅ **Expected improvement:** 0 → 1-4 implicit RDMAP items per paper

### Implicit Arguments Improvements (2025-10-27)
✅ **Comprehensive extraction section** added to extraction-fundamentals.md (parallel to RDMAP)
✅ **6 recognition patterns** for implicit arguments:
  - Pattern 1: Undefended quality judgments
  - Pattern 2: Comparison without baseline
  - Pattern 3: Capability assumptions
  - Pattern 4: Inferential leaps
  - Pattern 5: Definitional assumptions
  - Pattern 6: Causal assumptions
✅ **Common mistakes section** addresses Type 1 bias and other failure modes
✅ **Section-by-section workflow** with systematic 4-type scans
✅ **Cross-section synthesis patterns** for Pass 2
✅ **Template script** created: `extraction-system/scripts/extraction/section_implicit_arguments_template.py`
✅ **Pass 1 prompt enhancement** with common pitfalls checklist
✅ **Expected improvement:** More consistent extraction, better Type 2-4 coverage, reduced fragility

---

## What's New in v2.6.1

### Phase 3: Implicit Arguments Systematic Extraction
✅ **Systematic 4-type framework** required for all core claims (Pass 1)
✅ **Completeness review** added to Pass 2 for cross-section synthesis
✅ **Documentation requirement** if <3 implicit arguments found
✅ **Updated prompts:** 01-claims-evidence_pass1_prompt.md, 02-claims-evidence_pass2_prompt.md
✅ **Expected improvement:** 0 → 8-12 implicit arguments per paper

### Phase 4: Research Design Granularity Guidance
✅ **Granularity principle** - each strategic decision requiring independent justification = separate RD
✅ **Design language keywords** to identify strategic decisions
✅ **Conservative consolidation** for Research Designs (preserve granularity)
✅ **Updated references:** tier-assignment-guide.md, consolidation-patterns.md
✅ **Updated prompts:** 03-rdmap_pass1_prompt.md, 04-rdmap_pass2_prompt.md
✅ **Expected improvement:** 1-2 → 3-6 research designs per paper

---

## What's New in v2.6

### Phase 1: Consolidation Refinement
✅ **Empirical graph-based consolidation** now primary method for evidence items
✅ **New consolidation type:** `identical_support_pattern`
✅ **Expected improvement:** 9.6% → 14-15% consolidation rate

### Phase 2: Verbatim Quote Requirements
✅ **Comprehensive verbatim quote enforcement** to prevent source verification failures
✅ **New reference file:** `verbatim-quote-requirements.md` (12KB)
✅ **Expected improvement:** 53% → 85-95% Pass 3 validation rate

---

## Package Contents

### Root Level (1 file)
- `SKILL.md` - Main skill file with consolidated workflow guidance

### references/ Directory Structure

```text
references/
├── extraction-fundamentals.md           # Universal sourcing (ALWAYS read first)
│                                        # + Implicit RDMAP patterns (NEW v2.6.3)
│                                        # + Implicit Arguments patterns (NEW v2.6.3)
├── verbatim-quote-requirements.md       # Strict verbatim quote requirements
├── verification-procedures.md           # Pass 3 validation procedures
├── research-design-extraction-guide.md  # Research Design guidance
├── checklists/                          # Decision frameworks
│   ├── consolidation-patterns.md        # Lump vs split + cross-ref repair (v2.6.3)
│   ├── tier-assignment-guide.md         # Design/Method/Protocol decisions
│   └── expected-information.md          # Completeness checklists
├── schema/                              # Schema documentation
│   └── schema-guide.md                  # Human-readable schema docs (v2.6.2)
└── examples/                            # Worked examples
    └── sobotkova-example.md             # Complete worked extraction
```

### Updated Files in v2.6.3

**Major Updates:**
- `extraction-fundamentals.md` - Added two comprehensive sections:
  - Implicit RDMAP Extraction (68 lines, 4 recognition patterns)
  - Implicit Arguments Extraction (154 lines, 6 recognition patterns)
- `consolidation-patterns.md` - Added cross-reference repair section (MANDATORY for Pass 2/4)
- `SKILL.md` - Updated references description to highlight new pattern sections

**Minor Updates:**
- `01-claims-evidence_pass1_prompt.md` - Added common pitfalls checklist for implicit arguments

**New Files:**
- Template scripts (in extraction-system/scripts/extraction/):
  - `consolidation_template.py` - Cross-reference repair reference implementation
  - `section_rdmap_template.py` - Implicit RDMAP extraction examples
  - `section_implicit_arguments_template.py` - Implicit arguments extraction examples (4 types)

---

## Installation

1. **Unzip the package** to your skills directory (if packaged)
2. **Replace the old skill** if upgrading from v2.6.1 or earlier
3. **Update runtime prompts** if using separate prompts directory

---

## Runtime Prompts (Separate Directory)

The following prompt files have been updated:

**v2.6.3 Updates:**
- `01-claims-evidence_pass1_prompt.md` - Added implicit arguments common pitfalls checklist

**v2.6.1 Updates:**
- `01-claims-evidence_pass1_prompt.md` - Added systematic implicit argument extraction workflow
- `02-claims-evidence_pass2_prompt.md` - Added STEP 3: Implicit Argument Completeness Review
- `03-rdmap_pass1_prompt.md` - Updated Step 1 with Research Design granularity guidance
- `04-rdmap_pass2_prompt.md` - Added Research Design consolidation section

**v2.6 Updates:**
- All prompts - Added verbatim critical reminder
- Pass 2 prompts - Updated consolidation hierarchy + enhanced verification

**Note:** These prompts are in `extraction-system/prompts/` and are NOT included in the skill package per architectural design.

---

## Schema Synchronisation

**Important:** The schema exists in two locations:

**Source of Truth:**
- `.claude/skills/research-assessor/references/schema/extraction_schema.json`
- This is the version used by Claude Code when skill is invoked

**Archive/Reference Copy:**
- `extraction-system/schema/extraction_schema.json`

**Current Status:** ✅ Both versions are identical (verified 2025-10-27)

**Sync Protocol:**
1. Always update the skill schema (`.claude/skills/`) first
2. Copy to `extraction-system/schema/` for archival/documentation
3. Verify sync with: `diff .claude/skills/research-assessor/references/schema/extraction_schema.json extraction-system/schema/extraction_schema.json`
4. Commit both versions together to maintain sync

**Why Two Copies?**
- Skill version: Active runtime schema used by Claude Code
- Extraction-system version: Documentation, reference for users, git tracking visibility

---

## Usage Pattern

When Claude Code invokes the research-assessor skill:

1. **Skill triggers** based on metadata (name + description)
2. **SKILL.md loads** with workflow guidance
3. **Claude consults references as needed** using progressive disclosure

### Reference Usage by Pass

**For Pass 1 & Pass 2 (Extraction & Consolidation):**
- **ALWAYS read first:** `extraction-fundamentals.md`
  - Universal sourcing requirements
  - Implicit RDMAP recognition patterns (v2.6.3)
  - Implicit Arguments recognition patterns (v2.6.3)
- **When uncertain:**
  - Schema questions? → `schema/schema-guide.md`
  - Tier assignment? → `checklists/tier-assignment-guide.md`
  - Consolidation? → `checklists/consolidation-patterns.md` (includes cross-ref repair v2.6.3)
  - Completeness? → `checklists/expected-information.md`
- **For examples:** `examples/sobotkova-example.md`

**For Pass 3 (Validation):**
- **ALWAYS read first:** `verification-procedures.md`
  - Complete verification procedures for all object types
  - Decision trees and worked examples

**For Pass 4 (Rationalisation):**
- **Critical:** `checklists/consolidation-patterns.md` for cross-reference repair (v2.6.3)

---

## Breaking Changes

### v2.6.3 Changes

**Skill Structure:**
- **Removed:** `references/README.md` (per skill-creator best practices)
- **Impact:** None - navigation in SKILL.md is sufficient

**Extraction Fundamentals:**
- **Added:** Comprehensive implicit extraction sections (RDMAP + Arguments)
- **Impact:** More systematic extraction, fewer missed implicit items
- **Compatibility:** Backward compatible (additive)

**Consolidation:**
- **Added:** MANDATORY cross-reference repair after consolidation
- **Impact:** Prevents broken cross-references (41 broken refs → 0)
- **Compatibility:** Backward compatible but consolidation without repair now causes validation failures

### v2.6.1 Changes

**Schema:**
- No schema changes in v2.6.1

**Extraction Logic:**
- Implicit Arguments now systematically required for all core claims

### v2.6 Changes

**Schema:**
- **Added:** `identical_support_pattern` to `consolidation_metadata.consolidation_type` enum
- **Compatibility:** Backward compatible (additive change)

**Consolidation Logic:**
- **Changed:** Evidence consolidation now uses graph analysis FIRST
- **Impact:** May identify additional consolidations when re-running Pass 2

**Verbatim Requirements:**
- **Changed:** More stringent quote construction standards
- **Impact:** Existing extractions may not meet new standards
- **Recommendation:** Re-run Pass 1 & 2 on existing extractions

---

## Testing Recommendations

### Test 1: Implicit RDMAP Recognition (v2.6.3)
1. Run full extraction on paper with implicit procedures
2. Check for implicit RDMAP items (expect 1-4)
3. Verify trigger_text arrays properly populated
4. Verify recognition patterns mentioned in extraction reasoning

### Test 2: Implicit Arguments Recognition (v2.6.3)
1. Run full extraction on paper with complex arguments
2. Check Type distribution (not just Type 1)
3. Verify 6 recognition patterns applied
4. Check for cross-section synthesis patterns in Pass 2

### Test 3: Cross-Reference Repair (v2.6.3)
1. Run Pass 2 or Pass 4 with consolidations
2. Verify cross-reference repair executed
3. Check validation shows 0 broken references
4. Verify consolidation_metadata preserved

### Test 4: Consolidation Improvements (v2.6)
1. Re-run Pass 2 on Sobotkova extraction
2. Verify additional consolidations identified
3. Check consolidation_type = "identical_support_pattern" used
4. Measure reduction percentage (target: 14%+)

### Test 5: Verbatim Quote Compliance (v2.6)
1. Run full extraction on test paper
2. Check verbatim rules mentioned in extraction reasoning
3. Verify Pass 2 verification step executed
4. Measure Pass 3 source verification pass rate (target: 85-90%)

---

## File Sizes

| File | Size | Change from v2.6.1 |
|------|------|--------------------|
| SKILL.md | 10 KB | Unchanged |
| extraction-fundamentals.md | ~15 KB | +8 KB (new sections) |
| consolidation-patterns.md | 25 KB | +12 KB (cross-ref repair) |
| verbatim-quote-requirements.md | 12 KB | Unchanged |
| verification-procedures.md | 59 KB | Unchanged |
| schema-guide.md | 19 KB | Unchanged |
| Other reference files | 17 KB | Unchanged |
| Template scripts (external) | 15 KB | +15 KB (new) |
| **Total (skill only)** | **~240 KB** | +20 KB |

---

## Support Files Provided

In addition to the skill package, the following files are maintained:

1. **This SKILL_README.md** - Package summary and installation guide
2. **extraction-system/prompts/** - Runtime prompts (separate from skill)
3. **extraction-system/scripts/extraction/** - Template scripts for reference
4. **planning/** - Implementation reports and assessments

---

## Version History

- **v2.6.3** (2025-10-27) - Implicit RDMAP recognition patterns + Implicit Arguments recognition patterns + Cross-reference repair + Template scripts
- **v2.6.2** (2025-10-26) - Research Design schema simplification (conditional objects optional)
- **v2.6.1** (2025-10-25) - Implicit arguments systematic extraction + Research Design granularity
- **v2.6** (2025-10-24) - Consolidation refinement + verbatim quote requirements
- **v2.6** (2025-10-24) - Consolidation refinement + verbatim quote requirements
- **v2.5** (2025-10-21) - Hallucination prevention (mandatory sourcing)
- **v2.4** - RDMAP objects (research_design, method, protocol)
- **v2.3** - Consolidation metadata + multi-dimensional evidence
- **v2.2** - Extraction vs assessment-time field separation
- **v2.1** - Type 3 disciplinary assumptions
- **v2.0** - Initial comprehensive schema

---

## Key Improvements Summary

### Robustness Improvements (v2.6.3)
- **Implicit RDMAP:** From fragile (0 items) → systematic (1-4 items) with recognition patterns
- **Implicit Arguments:** From fragile → robust with 6 recognition patterns preventing Type 1 bias
- **Cross-References:** From broken (41) → valid (0) with automated repair

### Quality Improvements (v2.6.1)
- **Implicit Arguments:** From inconsistent → systematic 4-type framework
- **Research Designs:** From under-granular (1-2) → appropriate (3-6)

### Quality Improvements (v2.6)
- **Consolidation:** From ad-hoc (9.6%) → empirical graph-based (14-15%)
- **Source Verification:** From failing (53%) → passing (85-95%) via verbatim requirements

### Foundation (v2.5)
- **Sourcing:** From optional → mandatory (hallucination prevention)
- **Verification:** From informal → systematic three-step procedures

---

## Questions or Issues?

Refer to:
- **This SKILL_README.md** - Package summary (you are here)
- **planning/skill-improvement-implementation-plan.md** - RDMAP improvements details
- **planning/implicit-arguments-skill-assessment.md** - Implicit arguments improvements details
- **planning/skill-structure-assessment.md** - Skill structure analysis
- **SKILL.md** - Main skill instructions
- **extraction-fundamentals.md** - Comprehensive sourcing + recognition patterns
- **consolidation-patterns.md** - Cross-reference repair procedure

---

**Package Status:** ✅ Ready for deployment and testing

**Structure Status:** ✅ 100% compliant with skill-creator best practices
