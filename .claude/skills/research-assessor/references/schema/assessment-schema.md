# Credibility Assessment Schema

**Purpose:** Define output structures for signal cluster assessments and canonical assessment consolidation

**Date:** 2025-11-29

**Version:** 2.1 (with three pillars framework and reproducibility readiness)

---

## Output Files Overview

Three types of assessment outputs:

1. **Signal Cluster Files** (Markdown) - Detailed narrative assessments per cluster
2. **Canonical assessment.json** (JSON) - Machine-readable consolidation
3. **Credibility Report** (Markdown) - Human-readable synthesis

---

## Part 1: Signal Cluster File Structure

### File Locations

```
assessment/
├── cluster-1-foundational-clarity.md       # Transparency pillar: Comprehensibility + Transparency
├── cluster-2-evidential-strength.md        # Credibility pillar: Plausibility + Validity + Robustness + Generalisability
└── cluster-3-reproducibility.md            # Reproducibility pillar: Reproducibility (single signal)
```

### Three Pillars Framework

Clusters are organised by assessment pillar:

| Cluster | Pillar | Signals |
|---------|--------|---------|
| Cluster 1 | Transparency | Comprehensibility, Transparency |
| Cluster 2 | Credibility | Plausibility, Validity, Robustness, Generalisability |
| Cluster 3 | Reproducibility | Reproducibility |

**See:** `references/credibility/assessment-pillars.md` for full framework

### Standard Cluster File Template

```markdown
# Signal Cluster Assessment: [Cluster Name]
## [Signals Included]
## Paper: {paper-slug}

**Assessment Date:** {date}
**Cluster:** [cluster number/name]
**Research Approach:** [deductive|inductive|abductive from classification]
**Quality State:** [high|moderate] (if moderate, see caveat below)

---

[IF QUALITY_STATE = "MODERATE", ADD CAVEAT HEADER:]

> **ASSESSMENT QUALITY CAVEAT**
>
> This assessment is based on [medium-confidence extraction | low-confidence classification | partial metric alignment].
> [Specific limitation: e.g., "Classification is ambiguous - paper may be mixed inductive-abductive" OR
> "Extraction has notable gaps in methods documentation"]. Scores should be interpreted as approximate
> ranges (20-point bands) rather than precise values.

---

## Cluster Overview

[2-3 sentences explaining why these signals are grouped together and what this cluster assesses]

Example:
> This cluster assesses how clearly the research is communicated. Comprehensibility evaluates clarity of claims and argument structure; Transparency evaluates completeness of research design and methods documentation. These signals are assessed together because poor comprehensibility undermines ability to evaluate transparency.

---

## Signal [N]: [Signal Name]

**Score:** [75]/100 [or 60-80 if moderate quality]
**Confidence:** [High|Medium|Low]

### Signal Definition

[Brief 1-sentence definition from signal-definitions-hass.md]

### Assessment Summary

[2-3 sentence summary of signal evaluation for this paper]

### Key Strengths

- [Specific strength with evidence citation from extraction]
- [Specific strength]
- [Specific strength]

### Key Weaknesses

- [Specific weakness with evidence citation]
- [Specific weakness]
- [Specific weakness]

### Supporting Evidence from Extraction

**[Relevant extraction elements for this signal]:**

- **[Element 1]:** [Evidence and analysis]
- **[Element 2]:** [Evidence and analysis]
- **[Element 3]:** [Evidence and analysis]

Example for Comprehensibility:
- **Claim structure:** Claims clearly formulated with explicit scope and boundaries
- **Argument flow:** Logical progression from evidence to claims traceable
- **Terminology:** Most key terms defined; some domain-specific terms assumed

### Scoring Justification

[Detailed rationale citing approach-specific anchors from signal-definitions-hass.md]

**Template:**
> "Scored [X] ([Band Description] for [approach] research). This paper [meets anchor criteria A, B, C for band X-Y], but [lacks criterion D which would move to higher band]. [Additional justification with specifics]."

**Example:**
> "Scored 75 (Good Comprehensibility for inductive research). Claims are clearly formulated with explicit scope (meets 60-79 anchor: 'pattern descriptions mostly clear'), argument structure is logical and traceable (meets 60-79: 'logical progression traceable'), but some domain-specific terminology lacks definition for non-specialist readers (prevents 80-100: 'key terms defined'). For inductive research, comprehensibility emphasises clear pattern descriptions - this paper meets that standard."

### Approach-Specific Context

**Research Approach:** [Inductive|Deductive|Abductive]

[How this signal's criteria apply to this specific research approach]

**Example for Transparency in inductive research:**
> "For inductive research, transparency emphasises workflow documentation and data archiving over pre-registration (which is not expected for exploratory work). This paper meets inductive transparency standards by clearly documenting data collection procedures and archiving datasets, but lacks detailed analysis workflow documentation."

### Relevant Metrics

[List relevant quantitative metrics from metrics.json that inform this signal]

**Example for Transparency:**
- **TCI (Transparency & Completeness Index):** 68/100
- **MDD (Methodological Documentation Density):** 71/100

**Metric-signal alignment:** [Discussion of whether metrics align with signal assessment]

---

[REPEAT SIGNAL STRUCTURE FOR EACH SIGNAL IN CLUSTER]

---

## Cross-Signal Coherence Check

**Do the signals in this cluster cohere?**

[Analysis of whether signal scores are mutually consistent or require explanation]

**Example:**
> Comprehensibility (75) and Transparency (70) are closely aligned, which is expected - clear communication supports transparent methods documentation. The slightly lower Transparency score reflects workflow documentation gaps, not communication issues.

**Unexplained tensions (if any):**
- [Flag any signal score combinations that seem contradictory]
- [Provide explanation or note as concern]

---

## Cluster Summary

**Overall Assessment:** [Foundational Clarity is good/moderate/weak]

**Primary Strengths:**
- [Strength 1]
- [Strength 2]

**Primary Weaknesses:**
- [Weakness 1]
- [Weakness 2]

**Implications for Overall Credibility:**
[How this cluster affects overall paper credibility]

---

## Assessment Metadata

**Assessor:** research-assessor skill v{version}
**Assessment Date:** {date}
**Approach-Specific Anchors Applied:** [Yes|No] (No if quality_state = moderate + classification ambiguous)
**Quality State:** [high|moderate]
```

---

## Part 2: Canonical assessment.json Structure

### File Location

`assessment/assessment.json`

### Purpose

Machine-readable consolidation of all assessment data for:

- Corpus-level statistics
- Cross-paper comparisons
- Downstream tooling (dashboards, visualisations)

### Complete Schema

```json
{
  "paper_id": "paper-slug",
  "assessment_date": "2025-11-17",
  "system_version": "v0.2-alpha",

  "classification": {
    "expressed_approach": "inductive|deductive|abductive|mixed|none_stated",
    "revealed_approach": "inductive|deductive|abductive|mixed",
    "expressed_vs_revealed": "matched|partial|mismatched",
    "primary_approach": "inductive|deductive|abductive",
    "revealed_confidence": "high|medium|low",
    "harking_flag": true|false,
    "credibility_framework_to_use": "inductive_emphasis|deductive_emphasis|abductive_emphasis|mixed_assessment",
    "signal_prioritisation": {
      "primary_signals": ["transparency", "comprehensibility", "generalisability"],
      "secondary_signals": ["validity", "robustness", "reproducibility"],
      "deemphasised_signals": []
    }
  },

  "track_a": {
    "quality_state": "high|moderate|low",
    "extraction_confidence": "high|medium|low",
    "metric_signal_alignment": "yes|partial|no",
    "classification_confidence": "high|medium|low",
    "assessment_viability_summary": "Brief summary of quality assessment",
    "improvement_opportunities": [
      "Specific improvement suggestion 1",
      "Specific improvement suggestion 2"
    ]
  },

  "signals": [
    {
      "signal_name": "comprehensibility",
      "signal_number": 1,
      "cluster": "foundational_clarity",
      "score": 75,
      "score_band": "60-79",
      "confidence": "high|medium|low",
      "summary": "1-2 sentence assessment summary",
      "strengths": [
        "Specific strength 1",
        "Specific strength 2",
        "Specific strength 3"
      ],
      "weaknesses": [
        "Specific weakness 1",
        "Specific weakness 2"
      ],
      "justification": "Detailed scoring rationale citing approach-specific anchors",
      "approach_context": "How this signal applies to this research approach",
      "approach_anchors_applied": true|false,
      "relevant_metrics": {
        "TCI": 68,
        "MDD": 71
      }
    },
    {
      "signal_name": "transparency",
      "signal_number": 2,
      "cluster": "foundational_clarity",
      "score": 70,
      "score_band": "60-79",
      "confidence": "high",
      "summary": "...",
      "strengths": [...],
      "weaknesses": [...],
      "justification": "...",
      "approach_context": "...",
      "approach_anchors_applied": true,
      "relevant_metrics": {
        "TCI": 68,
        "RIS": 72
      }
    },
    {
      "signal_name": "plausibility",
      "signal_number": 3,
      "cluster": "evidential_strength",
      "score": 80,
      "score_band": "80-100",
      "confidence": "high",
      "summary": "...",
      "strengths": [...],
      "weaknesses": [...],
      "justification": "...",
      "approach_context": "...",
      "approach_anchors_applied": true,
      "relevant_metrics": {}
    },
    {
      "signal_name": "validity",
      "signal_number": 4,
      "cluster": "evidential_strength",
      "score": 65,
      "score_band": "60-79",
      "confidence": "medium",
      "summary": "...",
      "strengths": [...],
      "weaknesses": [...],
      "justification": "...",
      "approach_context": "...",
      "approach_anchors_applied": true,
      "relevant_metrics": {
        "ESD": 2.3,
        "SCS": 55
      }
    },
    {
      "signal_name": "robustness",
      "signal_number": 5,
      "cluster": "evidential_strength",
      "score": 60,
      "score_band": "60-79",
      "confidence": "medium",
      "summary": "...",
      "strengths": [...],
      "weaknesses": [...],
      "justification": "...",
      "approach_context": "...",
      "approach_anchors_applied": true,
      "relevant_metrics": {}
    },
    {
      "signal_name": "generalisability",
      "signal_number": 6,
      "cluster": "evidential_strength",
      "score": 78,
      "score_band": "60-79",
      "confidence": "high",
      "summary": "...",
      "strengths": [...],
      "weaknesses": [...],
      "justification": "...",
      "approach_context": "...",
      "approach_anchors_applied": true,
      "relevant_metrics": {
        "SCS": 55
      }
    },
    {
      "signal_name": "reproducibility",
      "signal_number": 7,
      "cluster": "reproducibility",
      "score": 72,
      "score_band": "60-79",
      "confidence": "high",
      "summary": "...",
      "strengths": [...],
      "weaknesses": [...],
      "justification": "...",
      "approach_context": "...",
      "approach_anchors_applied": true,
      "relevant_metrics": {
        "RIS": 72,
        "PGCS": 45,
        "FCS": 60
      }
    }
  ],

  "reproducibility_readiness": {
    "applies": true,
    "pathway": "standard|methodological_transparency_variant",
    "if_not_applicable_reason": "",
    "inputs_available": {
      "status": "yes|partial|no",
      "details": "Description of data/input availability"
    },
    "code_available": {
      "status": "yes|partial|no|not_applicable",
      "tool_type": "open_scriptable|proprietary_scriptable|gui_based|mixed|none",
      "details": "Description of code/workflow availability"
    },
    "environment_specified": {
      "status": "yes|partial|no|not_applicable",
      "details": "Description of computational environment documentation"
    },
    "outputs_documented": {
      "status": "yes|partial|no",
      "details": "Description of expected outputs for verification"
    },
    "execution_feasibility": "ready|needs_work|not_feasible",
    "feasibility_rationale": "Explanation of feasibility assessment",
    "publication_year": 2024,
    "adoption_context": "innovator|early_adopter|early_majority|mainstream"
  },

  "metrics": {
    "ESD": 2.3,
    "TCI": 68,
    "SCS": 55,
    "RTI": 0.42,
    "RIS": 72,
    "PGCS": 45,
    "FCS": 60,
    "MDD": 71
  },

  "report_metadata": {
    "report_path": "assessment/credibility-report-v1.md",
    "report_type": "standard|caveated",
    "word_count": 2150,
    "quality_caveats": false|true
  }
}
```

---

## Field Definitions

### Top-Level Fields

- `paper_id`: Paper slug identifier
- `assessment_date`: ISO date of assessment
- `system_version`: Skill version for reproducibility

### classification Object

Condensed from classification.json - includes only essential fields for reference:

- `expressed_approach`: What paper states
- `revealed_approach`: What paper does
- `expressed_vs_revealed`: Alignment status
- `primary_approach`: Authoritative classification
- `revealed_confidence`: Classification confidence
- `harking_flag`: HARKing concern flag
- `credibility_framework_to_use`: Framework applied
- `signal_prioritisation`: Which signals emphasised

### track_a Object

Quality assessment consolidated:

- `quality_state`: HIGH/MODERATE/LOW (determines pathway)
- `extraction_confidence`: HIGH/MEDIUM/LOW
- `metric_signal_alignment`: YES/PARTIAL/NO
- `classification_confidence`: HIGH/MEDIUM/LOW
- `assessment_viability_summary`: Brief quality summary
- `improvement_opportunities`: Array of improvement suggestions

### signals Array

One object per signal (7 total), with:

- `signal_name`: Signal identifier
- `signal_number`: 1-7
- `cluster`: Which cluster this signal belongs to
- `score`: 0-100 (or score_band midpoint if moderate quality)
- `score_band`: e.g., "60-79" (narrow for high quality, 20-point for moderate)
- `confidence`: HIGH/MEDIUM/LOW
- `summary`: 1-2 sentence assessment
- `strengths`: Array of specific strengths
- `weaknesses`: Array of specific weaknesses
- `justification`: Detailed scoring rationale
- `approach_context`: How signal applies to this approach
- `approach_anchors_applied`: Boolean (false if moderate quality + classification ambiguous)
- `relevant_metrics`: Object with relevant metric values

### metrics Object

All 8 quantitative metrics from metrics.json:

- ESD, TCI, SCS, RTI, RIS, PGCS, FCS, MDD

### reproducibility_readiness Object

Gateway assessment for future reproduction attempts:

- `applies`: Boolean - whether reproducibility assessment applies to this paper
- `pathway`: "standard" or "methodological_transparency_variant" (for non-computational papers)
- `if_not_applicable_reason`: Explanation if applies=false
- `inputs_available`: Object with status (yes/partial/no) and details
- `code_available`: Object with status, tool_type, and details
  - `tool_type` values: open_scriptable (Python, R), proprietary_scriptable (SPSS syntax, Stata), gui_based (Excel), mixed, none
- `environment_specified`: Object with status and details
- `outputs_documented`: Object with status and details
- `execution_feasibility`: "ready", "needs_work", or "not_feasible"
- `feasibility_rationale`: Explanation of feasibility assessment
- `publication_year`: Year of publication (metadata only)
- `adoption_context`: Era context - "innovator" (pre-2015), "early_adopter" (2015-2020), "early_majority" (2020-2025), "mainstream" (post-2025)

**Note:** Adoption context is metadata for interpretation only — scores are not adjusted for era.

**See:** `references/credibility/assessment-pillars.md` for full reproducibility framework

### report_metadata Object

- `report_path`: Relative path to Markdown report
- `report_type`: "standard" or "caveated"
- `word_count`: Report length
- `quality_caveats`: Boolean indicating if caveat section present

---

## Quality State Variations

### HIGH Quality State

- **Precise scores:** 72, 68, 85 (within 5-point precision)
- **Score bands:** Narrow (e.g., "70-75")
- **approach_anchors_applied:** true
- **Confidence:** Generally high
- **No caveat headers** in cluster files

### MODERATE Quality State

- **Score bands:** 20-point ranges (e.g., 60-80)
- **Score:** Band midpoint (e.g., 70 for 60-80 band)
- **Score_band:** "60-80" (20-point range)
- **approach_anchors_applied:** false if classification ambiguous
- **Caveat headers** in all cluster files
- **Assessment Limitations section** in report

### LOW Quality State

- **No signal assessments performed**
- **No assessment.json generated**
- **Only track-a-quality.md + assessment-not-viable.md**

---

## Validation Checklist

**Before outputting assessment.json:**

- [ ] All 7 signals present in signals array
- [ ] classification object populated from classification.json
- [ ] track_a object populated from track-a-quality.md
- [ ] All signals have required fields (name, number, cluster, score, confidence, summary, justification)
- [ ] Score bands match quality state (narrow for HIGH, 20-point for MODERATE)
- [ ] approach_anchors_applied = false if classification ambiguous + moderate quality
- [ ] metrics object populated from metrics.json
- [ ] **reproducibility_readiness object populated** (required for all papers)
- [ ] report_metadata populated

---

## Corpus-Level Queries (Examples)

**Using `jq` for corpus analysis:**

```bash
# Mean Transparency score across corpus
jq '[.[] | .signals[] | select(.signal_name=="transparency") | .score] | add/length' corpus-assessments.json

# Signal score profile for inductive papers
jq '.[] | select(.classification.primary_approach=="inductive") | {paper: .paper_id, signals: [.signals[] | {signal: .signal_name, score: .score}]}' corpus-assessments.json

# Papers with HIGH quality state
jq '.[] | select(.track_a.quality_state=="high") | .paper_id' corpus-assessments.json

# Metric-signal correlation (Transparency vs TCI)
jq '.[] | {tci: .metrics.TCI, transparency: (.signals[] | select(.signal_name=="transparency") | .score)}' corpus-assessments.json
```

---

## Schema Version History

**v2.1 (2025-11-29):**

- Added Three Pillars Framework (Transparency, Credibility, Reproducibility)
- Reorganised clusters: Generalisability moved from Cluster 3 to Cluster 2
- Renamed Replicability → Reproducibility throughout
- Added reproducibility_readiness object for future automation gateway
- Updated signal numbering (Generalisability = 6, Reproducibility = 7)
- Added pathway and tool_type fields for reproducibility assessment

**v2.0 (2025-11-17):**

- Added quality_state awareness throughout
- Added approach_anchors_applied field to signals
- Added caveat header templates
- Enhanced track_a object structure
- Added cross-signal coherence section to cluster template

**v1.0 (2025-11-16):**

- Initial schema definition

---

## Related References

- `assessment-pillars.md` - **Three pillars framework** (Transparency, Credibility, Reproducibility)
- `signal-definitions-hass.md` - Signal definitions and approach-specific anchors
- `assessment-frameworks.md` - Framework selection and signal prioritisation
- `track-a-quality-criteria.md` - Quality gating decision logic
- `classification-schema.md` - Classification output structure
