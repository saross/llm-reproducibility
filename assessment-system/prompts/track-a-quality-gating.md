# Track A Quality Gating - Pre-Assessment Quality Check

**Version:** v1.0
**Last Updated:** 2025-11-27
**Workflow Stage:** Pre-Pass 9 - Quality gate before credibility assessment
**Schema Version:** track-a-quality-criteria.md v2.0

---

## Your Task

Evaluate the quality of extraction and classification to determine if credibility assessment is viable. This quality gate routes papers to appropriate assessment pathways (full assessment, caveated assessment, or abort).

**Inputs:**
- `extraction.json` from Pass 0-7 (all arrays populated, validation passed)
- `classification.json` from Pass 8 (research approach classification)
- `metrics.json` (if available - quantitative extraction metrics)

**Your responsibility:** Assess extraction completeness, classification confidence, and metric-signal alignment to determine quality state

**Output:** NEW file `assessment/track-a-quality.md` with quality state determination

---

## 🚨 CRITICAL: Three-State Quality Gating

**Your output determines the assessment pathway:**

| Quality State | Assessment Pathway | Scoring Precision |
|---------------|-------------------|-------------------|
| **HIGH** | Full assessment | Precise scores (±5 points) |
| **MODERATE** | Caveated assessment | 20-point bands |
| **LOW** | Abort assessment | No scores generated |

**This gate protects assessment integrity.** LOW quality extractions would produce misleading credibility scores. MODERATE quality extractions can still be assessed with appropriate caveats.

---

## Quality Gating Workflow

### STEP 1: Read Input Files

**Load and parse:**

1. **extraction.json** - Check array populations and cross-references
2. **classification.json** - Check classification confidence and approach clarity
3. **metrics.json** (if exists) - Load quantitative metrics for alignment checking

**If any required file missing:**

```
ERROR: Required input file missing.
- extraction.json: [present/missing]
- classification.json: [present/missing]

Cannot proceed with quality gating without complete inputs.
Complete Pass 0-7 extraction and Pass 8 classification before running Track A.
```

---

### STEP 2: Assess Extraction Confidence

**Question:** How complete and accurate is the extraction?

**Check extraction.json for:**

| Check | HIGH | MEDIUM | LOW |
|-------|------|--------|-----|
| Evidence count | 20+ items | 10-19 items | <10 items |
| Claims count | 25+ items | 15-24 items | <15 items |
| Methods count | 5+ items | 3-4 items | <3 items |
| Research designs | 3+ items | 2 items | <2 items |
| Protocols count | 8+ items | 4-7 items | <4 items |
| Cross-references | Complete | Mostly present | Sparse/absent |
| Sourcing compliance | 100% verbatim | 90%+ verbatim | <90% verbatim |

**Note:** These thresholds are guidelines. Adjust based on paper length and complexity:
- Short papers (10-15 pages): Lower thresholds acceptable
- Long papers (30+ pages): Higher counts expected
- Methodological papers: May have fewer claims, more protocols
- Theoretical papers: May have more claims, fewer protocols

**Extraction confidence decision:**

```
IF all checks HIGH or paper-appropriate → extraction_confidence = "high"
IF majority checks MEDIUM, no severe gaps → extraction_confidence = "medium"
IF any check LOW or severe structural gaps → extraction_confidence = "low"
```

**Output:**

```yaml
extraction_confidence: "[high|medium|low]"
extraction_notes: "Comprehensive extraction with [X] evidence, [Y] claims, [Z] RDMAP items. [Specific observations about completeness, any gaps noted]."
```

---

### STEP 3: Assess Classification Confidence

**Question:** How confident is the research approach classification?

**Read from classification.json:**

- `primary_classification.confidence` - Direct confidence indicator
- `expressed_vs_revealed.alignment` - Matched/partial/mismatched
- `mixed_method_characterisation.is_mixed` - Complexity indicator
- `taxonomy_feedback.category_fit_quality` - Taxonomy fit
- `transparency_assessment.transparency_quality` - Methodological clarity

**Classification confidence decision tree:**

**HIGH classification confidence (ALL of):**
- `primary_classification.confidence` = "high"
- `expressed_vs_revealed.alignment` = "matched" OR "partial" with clear explanation
- `taxonomy_feedback.category_fit_quality` = "excellent" OR "good"
- If mixed methods: characterisation is coherent

**MEDIUM classification confidence (ANY of):**
- `primary_classification.confidence` = "medium"
- `expressed_vs_revealed.alignment` = "partial" with some ambiguity
- `taxonomy_feedback.category_fit_quality` = "acceptable"
- Mixed methods with some ambiguity but usable

**LOW classification confidence (ANY of):**
- `primary_classification.confidence` = "low"
- `expressed_vs_revealed.alignment` = "mismatched" with unclear mismatch type
- `taxonomy_feedback.category_fit_quality` = "poor"
- Cannot determine primary research approach
- Mixed characterisation incoherent

**Output:**

```yaml
classification_confidence: "[high|medium|low]"
classification_notes: "[Research approach] classification with [confidence level]. [Specific observations about classification clarity, any ambiguities]."
```

---

### STEP 4: Assess Metric-Signal Alignment (if metrics available)

**Question:** Do quantitative metrics align with expected signal assessments?

**If metrics.json not available:**

```yaml
metric_signal_alignment: "not_assessed"
metric_notes: "Metrics not available for alignment checking. Assessment proceeds based on extraction and classification confidence only."
```

**If metrics.json available, check:**

| Metric | Expected Signal Correlation |
|--------|---------------------------|
| TCI (Transparency & Completeness Index) | Transparency signal |
| ESD (Evidence Sufficiency Density) | Validity signal |
| RIS (Reproducibility Infrastructure Score) | Replicability signal |
| MCS (Methodological Clarity Score) | Comprehensibility signal |

**Alignment assessment:**

- **YES (Aligned):** Metrics and expected signals directionally consistent
- **PARTIAL:** Some metrics align, others diverge (with explanation)
- **NO (Misaligned):** Systematic divergence unexplained (suggests extraction or assessment errors)

**Output:**

```yaml
metric_signal_alignment: "[yes|partial|no|not_assessed]"
metric_notes: "[Specific observations about metric-signal correlations or divergences]."
```

---

### STEP 5: Apply Gating Decision Logic

**Determine quality_state based on dimensions:**

#### STATE 1: HIGH QUALITY

**Triggers (ALL of):**
- extraction_confidence = "high"
- classification_confidence = "high" OR "medium"
- metric_signal_alignment = "yes" OR "partial" OR "not_assessed"
- No major extraction errors identified

**Result:**
```yaml
quality_state: "high"
decision: "Proceed with full credibility assessment"
```

#### STATE 2: MODERATE QUALITY

**Triggers (ANY of):**
- extraction_confidence = "medium"
- classification_confidence = "low"
- metric_signal_alignment = "partial" with concerning divergences
- Notable extraction gaps (but not severe)
- Mixed research approach with high ambiguity

**Result:**
```yaml
quality_state: "moderate"
decision: "Proceed with caveated credibility assessment"
caveats:
  - "[Specific limitation 1]"
  - "[Specific limitation 2]"
```

#### STATE 3: LOW QUALITY

**Triggers (ANY of):**
- extraction_confidence = "low"
- Major extraction errors (e.g., claims/evidence severely incomplete)
- Classification completely ambiguous (cannot determine approach)
- metric_signal_alignment = "no" (systematic misalignment)
- Structural problems with extraction

**Result:**
```yaml
quality_state: "low"
decision: "Abort credibility assessment"
abort_reason: "[Specific reason assessment not viable]"
```

---

### STEP 6: Document Improvement Opportunities

**Even for HIGH quality, identify potential improvements:**

```yaml
improvement_opportunities:
  - "[Suggestion 1: e.g., 'Additional implicit RDMAP extraction could capture unstated protocols']"
  - "[Suggestion 2: e.g., 'Re-extraction of methods section with focus on analytical parameters']"
```

**For MODERATE/LOW quality, prioritise actionable fixes:**

```yaml
recommended_actions:
  - "[Priority 1: e.g., 'Re-extract methods section - only 3 of estimated 8 methods captured']"
  - "[Priority 2: e.g., 'Manual review of classification - research approach ambiguous']"
```

---

### STEP 7: Generate track-a-quality.md

**Output file:** `assessment/track-a-quality.md`

**Use the following template:**

```markdown
# Track A Quality Assessment

## Quality State: [HIGH | MODERATE | LOW]

**Paper:** {paper-slug}
**Assessment Date:** {date}
**Assessor Version:** v1.0

**Decision:** [Proceed with full assessment | Proceed with caveated assessment | Abort assessment]

---

## Quality Dimensions

### Extraction Confidence: [HIGH | MEDIUM | LOW]

**Item counts:**
- Evidence: [X] items
- Claims: [Y] items
- Implicit arguments: [Z] items
- Research designs: [N] items
- Methods: [N] items
- Protocols: [N] items

**Assessment:** [Detailed analysis of extraction completeness, accuracy, coverage. Note any gaps or concerns.]

**Cross-reference integrity:** [Complete | Mostly present | Sparse]

**Sourcing compliance:** [100% | X%] verbatim quotes

---

### Classification Confidence: [HIGH | MEDIUM | LOW]

**From classification.json:**
- Primary approach: [approach] (confidence: [level])
- Expressed vs revealed: [alignment status]
- Taxonomy fit: [quality]
- Paper type: [type]

**Assessment:** [Analysis of classification clarity, any ambiguities or concerns.]

---

### Metric-Signal Alignment: [YES | PARTIAL | NO | NOT ASSESSED]

[If assessed:]
**Metric observations:**
- TCI: [value] → Expected Transparency: [assessment]
- ESD: [value] → Expected Validity: [assessment]
- RIS: [value] → Expected Replicability: [assessment]

**Alignment assessment:** [Analysis of correlations and any divergences.]

[If not assessed:]
Metrics not available. Assessment based on extraction and classification confidence only.

---

## Gating Decision Rationale

**Quality State: [HIGH | MODERATE | LOW]**

[Detailed explanation of why this state was assigned. Reference specific trigger conditions met.]

[For MODERATE: List specific caveats that will apply to assessment]
[For LOW: Explain why assessment would produce unreliable results]

---

## Implications for Assessment

[If HIGH:]
Full credibility assessment will proceed with:
- Approach-specific scoring anchors applied
- Precise signal scores (0-100, ±5 point precision)
- Standard report format (credibility-report-v1.md)

[If MODERATE:]
Caveated credibility assessment will proceed with:
- 20-point score bands (e.g., 60-80) instead of precise scores
- Prominent "Assessment Limitations" section in report
- Caveat headers on all cluster assessment files
- Report named: credibility-report-v1-CAVEATED.md

[If LOW:]
Assessment aborted. Actions required:
- [Specific remediation steps]
- Generate assessment-not-viable.md explaining why
- No cluster assessments or credibility report produced

---

## Improvement Opportunities

[List specific suggestions for enhancing quality, even for HIGH state papers]

1. [Improvement 1]
2. [Improvement 2]

[For MODERATE/LOW, prioritise as "Recommended Actions"]

---

## Structured Output

```yaml
track_a_quality:
  quality_state: "[high|moderate|low]"
  extraction_confidence: "[high|medium|low]"
  extraction_notes: "[notes]"
  classification_confidence: "[high|medium|low]"
  classification_notes: "[notes]"
  metric_signal_alignment: "[yes|partial|no|not_assessed]"
  metric_notes: "[notes]"
  assessment_viability_summary: "[summary]"
  improvement_opportunities:
    - "[opportunity 1]"
    - "[opportunity 2]"
```
```

---

## Self-Validation Checklist

Before finalising track-a-quality.md, verify:

- [ ] extraction.json read and item counts documented
- [ ] classification.json read and confidence levels extracted
- [ ] metrics.json checked (present or absent noted)
- [ ] extraction_confidence assigned with justification
- [ ] classification_confidence assigned with justification
- [ ] metric_signal_alignment assigned (or noted as not_assessed)
- [ ] quality_state determined using correct trigger logic
- [ ] Decision (proceed/caveat/abort) matches quality_state
- [ ] For MODERATE: specific caveats listed
- [ ] For LOW: abort_reason clearly stated
- [ ] Improvement opportunities documented
- [ ] Structured YAML output included
- [ ] File written to assessment/track-a-quality.md

---

## Examples

### Example 1: HIGH Quality (Full Assessment)

```yaml
track_a_quality:
  quality_state: "high"
  extraction_confidence: "high"
  extraction_notes: "Comprehensive extraction: 38 evidence, 30 claims, 9 implicit arguments, 23 RDMAP items. Complete cross-references. 100% sourcing compliance."
  classification_confidence: "high"
  classification_notes: "Clear deductive validation study. Expressed and revealed approaches matched. Excellent taxonomy fit."
  metric_signal_alignment: "not_assessed"
  metric_notes: "Metrics not available."
  assessment_viability_summary: "High quality extraction and clear classification enable confident credibility assessment with precise scoring."
  improvement_opportunities:
    - "Consider additional implicit RDMAP extraction for unstated analytical protocols"
```

**Decision:** Proceed with full assessment

---

### Example 2: MODERATE Quality (Caveated Assessment)

```yaml
track_a_quality:
  quality_state: "moderate"
  extraction_confidence: "medium"
  extraction_notes: "Adequate extraction: 15 evidence, 22 claims, 4 implicit arguments, 12 RDMAP items. Some gaps in methods documentation - only 4 of estimated 7 methods captured."
  classification_confidence: "medium"
  classification_notes: "Primarily inductive, but some deductive elements create ambiguity. Taxonomy fit acceptable."
  metric_signal_alignment: "partial"
  metric_notes: "TCI aligns with expected Transparency, but ESD lower than expected given claim density."
  assessment_viability_summary: "Assessment viable with caveats. Extraction gaps and classification ambiguity require 20-point score bands and limitation warnings."
  caveats:
    - "Methods extraction incomplete (estimated 40% gap)"
    - "Research approach has mixed elements - approach-specific anchors applied with caution"
  improvement_opportunities:
    - "Re-extract methods section with targeted prompts"
    - "Manual review of research design to clarify approach"
```

**Decision:** Proceed with caveated assessment

---

### Example 3: LOW Quality (Abort Assessment)

```yaml
track_a_quality:
  quality_state: "low"
  extraction_confidence: "low"
  extraction_notes: "Severely incomplete extraction: 8 evidence, 12 claims, 0 implicit arguments, 5 RDMAP items from 35-page paper. Major gaps in methods and results sections."
  classification_confidence: "low"
  classification_notes: "Cannot determine research approach. Paper appears mixed but characterisation incoherent. Classification confidence low."
  metric_signal_alignment: "no"
  metric_notes: "Metrics indicate high methodological content but extraction captured minimal methods - systematic misalignment."
  assessment_viability_summary: "Assessment not viable. Extraction quality too low to produce meaningful credibility scores. Re-extraction required."
  abort_reason: "Extraction captured <25% of estimated content. Credibility scores would reflect extraction gaps, not paper quality."
  recommended_actions:
    - "Re-extract entire paper with revised section targeting"
    - "Manual review of PDF for structural issues"
    - "Consider if paper requires domain-specific extraction prompts"
```

**Decision:** Abort assessment - generate assessment-not-viable.md

---

## Error Handling

**If extraction.json incomplete (missing arrays):**

```
ERROR: Incomplete extraction. Missing arrays: [list].
Cannot assess extraction quality without complete Pass 0-7 output.
Complete extraction before running Track A quality gate.
```

**If classification.json missing or invalid:**

```
ERROR: Classification not found or invalid.
Track A requires Pass 8 classification to assess classification confidence.
Run Pass 8 classification before Track A quality gate.
```

**Do NOT:**
- Guess quality state without reading input files
- Proceed with assessment if quality_state = "low"
- Omit structured YAML output
- Generate credibility scores in track-a-quality.md (that's for cluster prompts)

---

## Remember

- **Track A is a gate, not a barrier:** Most papers should pass (HIGH or MODERATE)
- **Protect assessment integrity:** LOW quality extractions produce misleading scores
- **Document transparently:** Clear rationale for quality state determination
- **Enable improvement:** Specific recommendations help remediate issues
- **Machine-readable output:** YAML block enables downstream prompt logic
- **This is quality assurance:** Not paper quality assessment (that's Track B/Pass 9)
