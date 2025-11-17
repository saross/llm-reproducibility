# Track A Quality Monitoring and Gating Criteria

**Purpose:** Self-assessment framework for extraction and assessment quality with three-state gating logic

**Date:** 2025-11-17

**Version:** 2.0 (with quality gating framework)

---

## Overview

**Track A** assesses the quality of our own extraction and assessment processes (in contrast to **Track B**, which assesses the credibility of the research paper itself).

This framework provides:

1. **Quality dimensions** to monitor
2. **Assessment questions** for each dimension
3. **Quality gating decision logic** (HIGH/MODERATE/LOW states)
4. **Behavioural rules** for each quality state
5. **Output format** specifications

**Key Innovation (v2.0):** Three-state quality gating system that routes papers to appropriate assessment pathways based on extraction and classification quality.

---

## Quality Dimensions

### Dimension 1: Extraction Confidence

**Question:** How confident are we that the extraction is complete and accurate?

**Assessment factors:**

- **Completeness:** Are all major claims, evidence, methods, and research designs captured?
- **Accuracy:** Are extracted elements correctly interpreted?
- **Section coverage:** Are all relevant paper sections processed?
- **Cross-references:** Are relationships between elements correctly identified?

**Confidence levels:**

**HIGH:**

- Comprehensive extraction across all major paper sections
- Claims, evidence, and methods well-represented
- Cross-references complete
- No major structural issues identified

**MEDIUM:**

- Extraction mostly complete (minor gaps acceptable)
- Core elements present but some details may be missing
- Cross-references mostly present
- Some extraction challenges noted

**LOW:**

- Significant gaps in extraction
- Core elements incomplete (e.g., only 2 of 8 methods captured)
- Cross-references sparse or absent
- Major structural or access issues (paywall, corrupted PDF)

---

### Dimension 2: Metric-Signal Alignment

**Question:** Do the quantitative metrics align with qualitative assessment expectations?

**Assessment factors:**

- **TCI vs Transparency:** Does Transparency & Completeness Index correlate with Transparency signal assessment?
- **ESD vs Validity:** Does Evidence Sufficiency Density correlate with Validity signal assessment?
- **RIS vs Replicability:** Does Reproducibility Infrastructure Score correlate with Replicability signal assessment?
- **Divergence flagging:** Are major metric-signal divergences noted and explained?

**Alignment levels:**

**YES (Aligned):**

- Metrics and signals directionally consistent
- High TCI → High Transparency (or explanation for divergence)
- Major divergences explained and justified

**PARTIAL:**

- Some metrics align, others diverge
- Divergences noted but explanation partial
- Unclear whether divergence is meaningful

**NO (Misaligned):**

- Systematic divergence between metrics and signals
- High metrics with low signals (or vice versa) unexplained
- Suggests extraction or assessment errors

---

### Dimension 3: Classification Confidence

**Question:** How confident are we in the research approach classification?

**Assessment factors:**

- **Expressed vs revealed clarity:** Is the mismatch (if any) clear and well-justified?
- **Approach determination:** Is the primary research approach unambiguous?
- **Mixed-method complexity:** If mixed, is the characterisation coherent?
- **HARKing flag certainty:** If flagged, is the evidence strong?

**Confidence levels:**

**HIGH:**

- Clear research approach determination
- Expressed vs revealed either aligned or mismatch well-evidenced
- If mixed, characterisation coherent
- HARKing flag (if present) well-supported

**MEDIUM:**

- Research approach determinable (some ambiguity)
- Expressed vs revealed comparison present (may have gaps)
- Mixed characterisation present but may lack specificity
- Classification usable for framework selection

**LOW:**

- Research approach ambiguous or contradictory
- Expressed vs revealed comparison unclear
- Mixed characterisation incoherent
- Cannot confidently select assessment framework

---

### Dimension 4: Assessment Consistency

**Question:** Are assessment judgements internally consistent and well-justified?

**Assessment factors:**

- **Cross-signal coherence:** Do signal scores cohere? (e.g., high Transparency + low Replicability should be explained)
- **Evidence-score alignment:** Do scores match the evidence cited in justifications?
- **Approach-anchor application:** Are approach-specific anchors correctly applied?
- **Reasoning quality:** Are justifications clear, specific, and evidence-based?

**Consistency levels:**

**HIGH:**

- Signal scores mutually coherent
- Scores match cited evidence
- Anchors correctly applied
- Justifications clear and specific

**MEDIUM:**

- Mostly coherent (minor tensions explained)
- Scores generally match evidence
- Anchors mostly correctly applied
- Justifications adequate

**LOW:**

- Contradictions unexplained
- Scores don't match cited evidence
- Anchors misapplied
- Justifications vague or circular

---

## Quality Gating Decision Logic (v2.0 Framework)

**Quality assessment produces three possible states that determine assessment pathway:**

---

### STATE 1: HIGH QUALITY → Full Assessment

**Triggers (ALL of):**

- Extraction confidence: High
- Metric-assessment alignment: Yes
- Classification confidence: High OR Medium
- No major extraction errors identified

**Behaviour:**

1. **Run all 7 signal assessments** (3 cluster prompts)
2. **Generate full 3-5 page report** with comprehensive analysis
3. **Apply approach-specific anchors with confidence** (precise scoring)
4. **Use precise scores** (within 5-point bands: 72, 68, 85, etc.)
5. **Standard file naming:** `credibility-report-v1.md`

**Report characteristics:**

- Full narrative development
- Approach-specific anchor citations
- Precise signal scores (0-100)
- No quality caveats required (standard header only)

**File outputs:**

```
assessment/
├── track-a-quality.md
├── clusters/
│   ├── cluster-1-foundational-clarity.md
│   ├── cluster-2-evidential-strength.md
│   └── cluster-3-reproducibility-scope.md
└── credibility-report-v1.md
```

---

### STATE 2: MODERATE QUALITY → Caveated Assessment

**Triggers (ANY of):**

- Extraction confidence: Medium
- Metric-assessment alignment: Partial
- Classification confidence: Low
- Classification expressed vs revealed: Mismatched (unclear mismatch type)
- Research approach: "Mixed" with high ambiguity
- Notable extraction gaps (but not severe)

**Behaviour:**

1. **Run all 7 signal assessments** (3 cluster prompts)
2. **Generate report with prominent "Assessment Limitations" section** at top (before signal summaries)
3. **Constrain scoring to 20-point bands** (e.g., 60-80, not precise 72)
4. **All signal cluster files include bold caveat header**
5. **Use approach-generic rubrics** if classification ambiguous (cannot confidently apply approach-specific anchors)
6. **File naming:** `credibility-report-v1-CAVEATED.md`

**Caveat header template for cluster files:**

```markdown
> **ASSESSMENT QUALITY CAVEAT**
>
> This assessment is based on [medium-confidence extraction | low-confidence classification | partial metric alignment].
> [Specific limitation: e.g., "Classification is ambiguous - paper may be mixed inductive-abductive" OR
> "Extraction has notable gaps in methods documentation"]. Scores should be interpreted as approximate
> ranges (20-point bands) rather than precise values.
```

**Assessment Limitations section template for report:**

```markdown
## Assessment Limitations

**Quality State:** MODERATE

This credibility assessment is subject to the following limitations:

- **[Primary limitation]:** [Specific issue: e.g., "Classification confidence is low - research approach ambiguous between inductive and abductive"]
- **[Secondary limitation if applicable]:** [Specific issue]

**Interpretation guidance:**

- Signal scores are constrained to 20-point bands (e.g., 60-80) rather than precise values
- [If classification unclear:] Approach-generic scoring criteria used (not approach-specific anchors)
- Assessment should be considered indicative rather than definitive
- [Specific caution relevant to this paper]

**Recommended actions:**

- [If extraction gaps:] Consider re-extraction with targeted prompts for [specific sections]
- [If classification unclear:] Manual review of research design may clarify approach
- Use assessment to identify areas requiring closer manual review
```

**File outputs:**

```
assessment/
├── track-a-quality.md
├── clusters/
│   ├── cluster-1-foundational-clarity.md (with caveat header)
│   ├── cluster-2-evidential-strength.md (with caveat header)
│   └── cluster-3-reproducibility-scope.md (with caveat header)
└── credibility-report-v1-CAVEATED.md (with Assessment Limitations section)
```

---

### STATE 3: LOW QUALITY → Abort Assessment

**Triggers (ANY of):**

- Extraction confidence: Low
- Major extraction errors identified (e.g., claims/evidence severely incomplete)
- Classification completely ambiguous (cannot determine approach)
- Structural problems with paper (e.g., paywall, corrupted PDF, non-research content)
- Metrics calculation failed
- Fundamental extraction failures (e.g., < 5 claims extracted from 30-page paper)

**Behaviour:**

1. **Do NOT run signal cluster assessments** (Prompts 3-5 should not execute)
2. **Generate Track A quality report only** (track-a-quality.md)
3. **Create brief `assessment-not-viable.md`** explaining why assessment aborted
4. **Flag paper for re-extraction or manual review**
5. **File naming:** `track-a-only.md` + `assessment-not-viable.md`

**assessment-not-viable.md template:**

```markdown
# Credibility Assessment Not Viable

## Paper: {paper-slug}

**Quality State:** LOW

**Assessment Date:** {date}

---

## Reason for Abortion

Extraction confidence is low due to [specific issue: e.g., "incomplete methods extraction - only 2 of estimated 8-10 methods captured" OR "classification completely ambiguous - cannot determine research approach" OR "PDF corrupted - only partial text extraction possible"].

Credibility assessment requires higher extraction quality to produce meaningful signal scores. Proceeding with assessment would generate unreliable scores that misrepresent paper quality.

---

## Extraction Quality Analysis

**Extraction confidence:** Low

**Specific issues:**

- [Issue 1: e.g., "Methods section extraction incomplete (estimated 20% coverage)"]
- [Issue 2: e.g., "Claims extraction severely incomplete (5 claims from 30-page paper)"]
- [Issue 3: e.g., "Cross-references between claims and evidence absent"]

**Impact on assessment:**

- Cannot reliably assess [specific signals: e.g., "Transparency, Validity, Robustness"] without complete extraction
- Signal scores would be artificially low due to extraction gaps, not paper quality
- Assessment would misrepresent paper credibility

---

## Recommended Actions

1. **Re-extract** paper with revised prompt guidance for [specific sections: e.g., "methods section with emphasis on analytical procedures"]
2. **Manual review** of extraction to identify systematic errors or structural issues
3. **Check source file:** Verify PDF integrity, check for paywall/access issues
4. **Alternative:** If urgent assessment needed, manual expert assessment recommended (LLM assessment not viable at this quality level)

---

## Track A Quality Notes

[Full Track A analysis explaining quality issues in detail, including specific extraction gaps, metrics issues, classification problems, etc.]
```

**File outputs:**

```
assessment/
├── track-a-only.md (or track-a-quality.md)
└── assessment-not-viable.md
```

**No cluster files or credibility report generated.**

---

## Output Format Specification

### Required Track A Output

**Track A prompt must output quality state explicitly in structured format:**

```yaml
track_a_quality:
  # REQUIRED: Determines assessment pathway
  quality_state: "high|moderate|low"

  # Quality dimensions
  extraction_confidence: "high|medium|low"
  extraction_notes: "Comprehensive extraction with [details]"

  metric_signal_alignment: "yes|partial|no"
  metric_notes: "TCI correlates with Transparency assessment [details]"

  classification_confidence: "high|medium|low"
  classification_notes: "Clear inductive research approach [details]"

  # Overall assessment
  assessment_viability_summary: "High quality extraction and classification enable confident credibility assessment."

  # Improvement opportunities (even for high quality)
  improvement_opportunities:
    - "Consider additional [specific improvement]"
    - "Future extractions could [specific enhancement]"
```

### Gating Decision Output

**track-a-quality.md file must prominently display quality state:**

```markdown
# Track A Quality Assessment

## Quality State: [HIGH | MODERATE | LOW]

**Assessment Date:** {date}

**Decision:** [Proceed with full assessment | Proceed with caveated assessment | Abort assessment]

---

## Quality Dimensions

### Extraction Confidence: [HIGH | MEDIUM | LOW]

[Analysis of extraction completeness, accuracy, coverage]

### Metric-Signal Alignment: [YES | PARTIAL | NO]

[Analysis of metric-signal correlations and divergences]

### Classification Confidence: [HIGH | MEDIUM | LOW]

[Analysis of research approach classification clarity]

### Assessment Consistency: [Expected evaluation]

[Notes on anticipated assessment coherence]

---

## Gating Decision Rationale

[Explanation of why HIGH/MODERATE/LOW state was assigned]
[Reference to specific triggers that led to state determination]

---

## Implications for Assessment

**[If HIGH:]** Full credibility assessment with approach-specific anchors and precise scoring.

**[If MODERATE:]** Caveated assessment with 20-point score bands and prominent limitation warnings.

**[If LOW:]** Assessment aborted. Re-extraction or manual review required.

---

## Improvement Opportunities

[Specific suggestions for enhancing extraction or assessment quality]
```

---

## Implementation Guidance for Prompts

### track-a-quality-gate.md Prompt Requirements

The Track A quality gating prompt must:

1. **Evaluate all four quality dimensions** systematically
2. **Apply gating decision logic** using trigger conditions
3. **Output quality_state prominently** in structured format
4. **Generate track-a-quality.md** with decision justification
5. **Include specific improvement opportunities** (even for high quality)

**Critical:** quality_state output must be machine-readable for downstream prompts to conditionally execute.

---

### Signal Cluster Prompts (3-5) Requirements

Signal cluster assessment prompts must:

1. **Read quality_state** from track-a-quality.md before executing
2. **If quality_state = "moderate":**
   - Apply caveats and 20-point score bands
   - Add bold caveat header to cluster file
   - Use generic rubrics if classification confidence low
3. **If quality_state = "low":**
   - Should not execute (workflow skips signal assessment)
   - Orchestrator should detect LOW state and skip cluster prompts

**Example conditional logic:**

```markdown
# In signal cluster prompt

## Pre-Execution Check

1. Read track-a-quality.md
2. Extract quality_state value
3. If quality_state = "low": ABORT (do not proceed with assessment)
4. If quality_state = "moderate": APPLY CAVEAT MODE
5. If quality_state = "high": STANDARD ASSESSMENT
```

---

### generate-credibility-report.md Prompt Requirements

The report generation prompt must:

1. **Read quality_state** from track-a-quality.md
2. **Apply state-appropriate formatting:**
   - HIGH: Standard report format
   - MODERATE: Insert Assessment Limitations section at top
   - LOW: Skip (report prompt should not execute)
3. **Name file according to state:**
   - HIGH: `credibility-report-v1.md`
   - MODERATE: `credibility-report-v1-CAVEATED.md`
   - LOW: N/A (generate assessment-not-viable.md instead)
4. **Apply experimental system disclaimer** (all quality states)

**Experimental system disclaimer (for all reports):**

```markdown
> **EXPERIMENTAL SYSTEM - DEVELOPMENT PHASE**
>
> This credibility assessment was generated by an experimental LLM-assisted system currently in development and validation.
> Assessment quality: [HIGH | MODERATE with caveats]. Findings should be considered preliminary and subject to revision as
> the system is refined through validation testing.
```

---

## Quality Monitoring Best Practices

### Continuous Improvement

Track A is not just a gate - it's a learning mechanism:

1. **Document patterns:** What types of papers trigger MODERATE or LOW states?
2. **Identify systematic issues:** Are certain paper types consistently problematic?
3. **Refine extraction prompts:** Use Track A feedback to improve Pass 0-6 extraction
4. **Calibrate thresholds:** Are gating triggers appropriately sensitive?

### Validation Metrics

Track quality gating decisions:

- **State distribution:** What % of papers are HIGH/MODERATE/LOW?
- **False positives:** Papers marked LOW that actually have good quality (manual review)
- **False negatives:** Papers marked HIGH with poor quality signals (validation catch)
- **MODERATE conversion rate:** Can re-extraction move MODERATE → HIGH?

### Human Review Integration

- **LOW state papers:** Always queue for manual review
- **MODERATE state papers:** Periodic manual audit (10% sample)
- **HIGH state papers:** Spot-check (5% sample) for validation

---

## Related References

- `signal-definitions-hass.md` - Signal assessment guidance
- `assessment-frameworks.md` - Framework selection by approach
- `approach-taxonomy.md` - Classification framework (affects classification confidence)
- `harking-detection-guide.md` - HARKing detection (affects classification confidence)
