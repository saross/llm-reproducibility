# Corpus Interpretation Framework
## From Metrics to Insights: LLM-Powered Corpus Analysis

**Document Purpose:** Design framework for rich interpretation of corpus profile and paper scorecards using LLM analysis

**Date Created:** 2025-11-16
**Status:** Planning phase - recovering from VS Code crash
**Context:** Phase 6 complete (8 credibility metrics implemented), ready for interpretation layer

---

## Executive Summary

### What We Have Now (Phase 6 Complete)

**Completed 2025-11-15 to 2025-11-16:**
- ✅ 8 credibility metrics implemented (ESD, TCI, SCS, RTI, RIS, PGCS, FCS, MDD)
- ✅ Corpus profile generation with metric statistics and interpretations
- ✅ Individual paper scorecards for all 10 papers
- ✅ Bug fixes in ESD and SCS calculations
- ✅ Location tracking simplified (schema v2.5)
- ✅ Comprehensive metrics reference guide (docs/assessment-guide/credibility-metrics-reference.md)

**Current Outputs:**
- `reports/corpus-profile-2025-11-16-0724.md` - Statistical summary with basic interpretation
- 10 individual scorecards in `outputs/*/assessment/scorecard-*.md`

### What We Need (Interpretation Layer)

**The Gap:** Current corpus profile provides **descriptive statistics** but requires **manual pattern analysis**. An LLM-powered interpretation layer could:

- Identify corpus-level patterns and trends automatically
- Cluster papers by metric profiles
- Explain outliers with context
- Analyse metric correlations
- Detect disciplinary or temporal patterns
- Generate actionable recommendations for corpus improvement

---

## Design Questions (From active-todo-list.md Task 10.2)

### 1. What Specific Interpretations Are Most Valuable?

**Options to consider:**

#### A. Pattern Recognition and Clustering
- **Paper clustering by metric profiles:** Group papers with similar credibility signatures
  - Example: "High transparency, low replicability" cluster (good RDMAP, no infrastructure)
  - Example: "Infrastructure-rich" cluster (2020+ papers with data/code repositories)
  - Example: "Mixed credibility" cluster (strong in some signals, weak in others)
- **Outlier identification with explanations:** Papers that deviate significantly from corpus norms
  - Example: Why does Penske et al. 2023 score 14/15 FAIR while corpus median is 4/15?
  - Example: Why does Eftimoski et al. 2017 have such low transparency despite being published in *Antiquity*?

#### B. Metric Correlation Analysis
- **Which metrics tend to co-occur?**
  - Does high transparency (TCI) predict high replicability (RIS)?
  - Are FAIR scores (FCS) correlated with evidence density (ESD)?
  - Do PID-rich papers also have better scope discipline (SCS)?
- **Trade-offs and tensions:**
  - Do papers with extensive data sharing (RIS) also have privacy/CARE concerns?
  - Does methodological rigour (TCI) come at the cost of accessibility?

#### C. Temporal and Disciplinary Patterns
- **Adoption trends over time:**
  - How has FAIR compliance evolved from 2013 to 2024?
  - When did ORCID adoption begin in this corpus?
  - Are infrastructure metrics improving over time?
- **Disciplinary differences:**
  - Do software-focused papers (Ballsun-Stanton 2018) have different profiles than field archaeology papers?
  - Are genomics papers (Penske 2023) systematically different from archaeological surveys?

#### D. Actionable Recommendations
- **Corpus-level improvement priorities:**
  - "Most papers (70%) lack data repositories - target for improvement"
  - "ORCID coverage is 40% - recommend ORCID requirement for future extractions"
- **Paper-specific guidance:**
  - "Sobotkova et al. 2024 would benefit most from archiving code on Zenodo"
  - "Ross et al. 2015 has excellent transparency but no PIDs - retrospective DOI minting recommended"

#### E. Methodological Validation
- **Assessment quality checks:**
  - Are metric scores internally consistent? (high ESD should predict high validity)
  - Are there systematic biases in assessment? (newer papers systematically higher scores?)
  - Which metrics show highest variance? (indicates potential measurement issues)
- **Cross-validation opportunities:**
  - Do LLM interpretations align with expert intuitions?
  - Can we identify papers that need manual review?

**Recommendation:** Start with **A (Clustering), B (Correlations), and D (Recommendations)** as highest value. Add C and E in later iterations.

---

### 2. Should This Be Standalone Script or Integrated?

**Options:**

#### Option A: Standalone Script (`scripts/interpret_corpus.py`)
**Pros:**
- Clean separation of concerns (generation vs interpretation)
- Can be run on-demand after corpus profile updates
- Easier to test and iterate
- Can generate multiple interpretation reports with different prompts/models

**Cons:**
- Requires reading corpus profile and scorecards from files
- Potential duplication of data loading logic
- Two-step workflow (generate profile, then interpret)

#### Option B: Integrated into `generate_corpus_profile.py`
**Pros:**
- Single workflow (one command produces full analysis)
- No file I/O overhead (interpretation uses in-memory data)
- Guaranteed consistency (interpretation matches generated profile)

**Cons:**
- Increases script complexity
- Harder to iterate on interpretation prompts (requires full regeneration)
- Couples two distinct analytical phases

#### Option C: Hybrid - Optional Flag in `generate_corpus_profile.py`
**Pros:**
- Best of both worlds: integrated workflow OR standalone generation
- `--interpret` flag triggers LLM analysis phase
- Default behaviour unchanged (backward compatible)

**Cons:**
- Most complex to implement
- Flag proliferation risk

**Recommendation:** **Option C (Hybrid)** - Add `--interpret` flag to `generate_corpus_profile.py` for integrated workflow, but also create standalone `scripts/interpret_corpus.py` for ad-hoc analysis of existing profiles.

**Implementation:**
```bash
# Generate profile only (current behaviour)
python assessment-system/scripts/generate_corpus_profile.py

# Generate profile + interpretation (new)
python assessment-system/scripts/generate_corpus_profile.py --interpret

# Interpret existing profile (new standalone script)
python assessment-system/scripts/interpret_corpus.py reports/corpus-profile-2025-11-16-0724.md
```

---

### 3. What Format for Output?

**Options:**

#### Option A: Extended Markdown Section in Corpus Profile
**Structure:**
```markdown
# Corpus Profile: 10 Papers (2013-2024)

[... existing statistical sections ...]

---

## Rich Interpretation (LLM-Generated Analysis)

### Paper Clustering and Profiles
[LLM analysis of clusters]

### Metric Correlation Insights
[LLM analysis of correlations]

### Temporal Trends
[LLM analysis of adoption patterns]

### Recommendations
[LLM-generated actionable recommendations]

---

**Interpretation Metadata:**
- Generated: 2025-11-16
- Model: Claude Sonnet 4.5
- Prompt version: v1.0
```

**Pros:**
- Single comprehensive document
- Easy to share and read
- Interpretation context preserved with data

**Cons:**
- File becomes very long
- Harder to iterate (regeneration replaces entire file)
- Mixing descriptive stats with interpretive analysis

#### Option B: Separate Interpretation Report
**Files:**
- `reports/corpus-profile-2025-11-16-0724.md` (stats only, as now)
- `reports/corpus-interpretation-2025-11-16-0730.md` (LLM analysis)

**Pros:**
- Clean separation of data vs interpretation
- Can generate multiple interpretations from same profile
- Easier to version and compare interpretations
- Reader can choose depth level

**Cons:**
- Requires reading two files for full picture
- Risk of interpretations becoming stale if profile regenerated

#### Option C: Interactive HTML Dashboard
**Structure:**
- Metrics displayed as interactive visualisations
- Click to expand LLM interpretations
- Drill-down to individual paper scorecards
- Correlation matrices with hover explanations

**Pros:**
- Best user experience for exploration
- Can combine stats + interpretation + drill-down
- Modern, shareable format

**Cons:**
- Significant implementation effort (~6-8 hours)
- Requires JavaScript/plotting libraries
- Not plain-text (harder to version control)
- May be out of scope for current phase

**Recommendation:** **Option B (Separate Report)** for Phase 1, with **Option A (Extended Section)** as alternative if user prefers single-document output. Option C deferred for future enhancement.

**Rationale:** Separation allows iteration on interpretation prompts without regenerating statistics. Can easily switch to integrated format later if preferred.

---

### 4. Should Interpretation Be Deterministic or LLM-Based?

**Options:**

#### Option A: Deterministic (Rule-Based)
**Approach:** Hard-coded rules for pattern detection
```python
# Example deterministic interpretation
if fair_score > 12:
    interpretation = "Highly FAIR compliant"
elif fair_score > 8:
    interpretation = "Moderately FAIR compliant"
else:
    interpretation = "Minimal FAIR compliance"

if publication_year < 2016:
    interpretation += " (published before FAIR principles - score reflects historical context)"
```

**Pros:**
- Fully reproducible (same input = same output)
- Fast (no API calls)
- Transparent logic
- No cost per interpretation

**Cons:**
- Limited flexibility
- Cannot detect complex patterns
- Brittle (requires manual updating as corpus grows)
- No natural language explanations

#### Option B: LLM-Based (Flexible Analysis)
**Approach:** Prompt LLM with corpus data, ask for interpretation
```python
# Example LLM interpretation prompt
prompt = f"""
You are analysing a corpus of {n} research papers with credibility metrics.

CORPUS STATISTICS:
{metric_statistics}

INDIVIDUAL PAPER SCORES:
{paper_scores}

TASK:
1. Identify 2-4 distinct clusters of papers with similar metric profiles
2. Explain what characterises each cluster
3. Identify outliers and explain why they're unusual
4. Analyse correlations between metrics
5. Provide 3-5 actionable recommendations for improving corpus credibility

OUTPUT: Structured markdown report
"""
```

**Pros:**
- Rich, contextual explanations
- Can detect complex patterns
- Natural language output
- Adapts to corpus changes automatically
- Can incorporate domain knowledge

**Cons:**
- Non-deterministic (slight variation between runs)
- API cost per interpretation (~$0.10-0.50 per run estimated)
- Requires prompt engineering
- Potential hallucination risk (must validate against data)

#### Option C: Hybrid (Deterministic + LLM Augmentation)
**Approach:**
1. Deterministic rules detect patterns
2. LLM explains and contextualises patterns
3. Human-reviewable outputs

```python
# Deterministic pattern detection
clusters = hierarchical_clustering(paper_metrics, n_clusters=4)
outliers = detect_outliers(paper_metrics, threshold=2.5)
correlations = calculate_correlations(metric_matrix)

# LLM interpretation of detected patterns
interpretation = llm_interpret(
    clusters=clusters,
    outliers=outliers,
    correlations=correlations,
    prompt="Explain these patterns in context of HASS research credibility"
)
```

**Pros:**
- Combines reproducibility with flexibility
- LLM grounded in detected patterns (less hallucination)
- Can validate LLM output against deterministic findings
- Best of both worlds

**Cons:**
- More complex implementation
- Still has API costs (though potentially lower than pure LLM)

**Recommendation:** **Option C (Hybrid)** - Use deterministic methods for pattern detection, LLM for rich explanation and contextualisation.

**Rationale:**
- Leverages strengths of both approaches
- Grounding LLM in detected patterns reduces hallucination risk
- Deterministic layer provides validation baseline
- Natural language explanations make findings accessible

---

## Proposed Implementation Plan

### Phase 1: Deterministic Pattern Detection (Week 1)

**Tasks:**
1. Implement clustering algorithm (hierarchical or k-means)
2. Implement outlier detection (z-score or IQR method)
3. Implement correlation matrix calculation
4. Generate deterministic pattern report

**Outputs:**
- `assessment-system/scripts/pattern_detector.py`
- Basic pattern report (JSON or markdown)

**Effort:** 4-6 hours

---

### Phase 2: LLM Interpretation Layer (Week 1-2)

**Tasks:**
1. Design interpretation prompt template
2. Implement LLM interpreter (Claude API integration)
3. Generate rich interpretation report
4. Validate against deterministic findings

**Outputs:**
- `assessment-system/scripts/interpret_corpus.py`
- First interpretation report for 10-paper corpus
- Prompt template documentation

**Effort:** 5-7 hours

---

### Phase 3: Integration and Testing (Week 2)

**Tasks:**
1. Add `--interpret` flag to `generate_corpus_profile.py`
2. Test on current 10-paper corpus
3. Refine prompts based on output quality
4. Document interpretation workflow

**Outputs:**
- Updated `generate_corpus_profile.py`
- Validated interpretation report
- User documentation

**Effort:** 3-4 hours

**Total Phase 1-3 Effort:** 12-17 hours (aligns with original estimate of 3-4 hours design + 2-3 hours implementation, now refined with more detail)

---

## Interpretation Prompt Design (Draft)

### Prompt Template Structure

```markdown
# CORPUS INTERPRETATION TASK

You are a research methodologist analysing credibility metrics for a corpus of {n} HASS research papers.

## CORPUS OVERVIEW

{corpus_metadata}

## METRIC DEFINITIONS

{metric_definitions_brief}

## DETECTED PATTERNS (Deterministic Analysis)

### Clustering
{cluster_assignments_with_metrics}

### Outliers
{outlier_list_with_scores}

### Correlations
{correlation_matrix}

## YOUR TASK

Generate a rich interpretation report covering:

1. **Cluster Characterisation** (2-3 sentences per cluster)
   - What defines each cluster?
   - What credibility profile does each represent?
   - Example papers from each cluster

2. **Outlier Explanation** (2-3 sentences per outlier)
   - Why is this paper unusual?
   - Is this positive deviance or concerning anomaly?
   - Context (year, discipline, research type)

3. **Correlation Insights** (3-4 paragraphs)
   - Which metrics co-occur?
   - Are there trade-offs or tensions?
   - What does this reveal about credibility patterns?

4. **Temporal/Disciplinary Trends** (2-3 paragraphs)
   - How do patterns vary by publication year?
   - Are there disciplinary differences?
   - Evidence of adoption trends (FAIR, ORCIDs, repositories)?

5. **Actionable Recommendations** (5-7 recommendations)
   - Corpus-level improvements (what's systematically missing?)
   - High-impact interventions (biggest credibility gains)
   - Paper-specific guidance (which papers need what?)
   - Field-level policy implications

## OUTPUT FORMAT

Structured markdown with clear headings, bullet points for recommendations, specific paper citations (use paper IDs).

## CONSTRAINTS

- Ground all interpretations in provided data (no speculation)
- Cite specific papers and metrics when making claims
- Acknowledge limitations (small corpus, specific domain)
- Use UK spelling throughout
- Avoid over-generalisation - this is a 10-paper pilot corpus
```

---

## Validation Strategy

### How to Validate Interpretation Quality

**Criteria:**

1. **Grounding:** All claims must reference specific papers/metrics
2. **Consistency:** Interpretations must align with deterministic findings
3. **Actionability:** Recommendations must be specific and implementable
4. **Transparency:** Reasoning must be explicit and traceable
5. **Domain appropriateness:** Must reflect HASS research norms

**Validation Process:**

1. **Automated checks:**
   - All cited paper IDs exist in corpus
   - All cited metrics exist in schema
   - Clusters/outliers match deterministic detection

2. **Manual review:**
   - Do cluster descriptions make sense?
   - Are recommendations feasible?
   - Is domain context appropriate?

3. **Comparison baseline:**
   - Run interpretation 3 times (different seeds)
   - Check for consistency in major findings
   - Identify stable vs variable interpretations

---

## Success Criteria

### Interpretation Phase Complete When:

- ✅ Deterministic pattern detection running on 10-paper corpus
- ✅ LLM interpretation prompt generates coherent, grounded analysis
- ✅ Interpretation report provides actionable insights
- ✅ Findings validate against corpus profile statistics
- ✅ Workflow documented and reproducible
- ✅ Integration with corpus profile generation tested

---

## Open Questions for Discussion

### Before Implementation

1. **Clustering approach:** Hierarchical vs k-means vs manual classification?
2. **Number of clusters:** Fixed (e.g., 4 clusters) or determined by data (elbow method)?
3. **Outlier threshold:** How many standard deviations = outlier?
4. **API budget:** What's acceptable cost for interpretation? (~$0.10-0.50 per run estimated)
5. **Iteration strategy:** Generate multiple interpretations and compare, or single authoritative run?
6. **Temporal analysis depth:** Simple year trends or more sophisticated time-series?
7. **Visualisation:** Text-only or include plots (correlation heatmaps, cluster dendrograms)?

### Future Enhancements

8. **Cross-corpus comparison:** Compare this corpus to future corpora (20-25 paper FAIR vocabulary corpus)?
9. **Longitudinal tracking:** Re-interpret corpus as new papers added?
10. **Interactive exploration:** Move to HTML dashboard (Option C from Q3)?
11. **Domain expert validation:** Formal review by research methodologists?

---

## Next Steps (Immediate Actions)

### Week 1 Tasks

1. **Decision session:** Review open questions, make design decisions
2. **Implement pattern detector:** Clustering, outliers, correlations
3. **Draft interpretation prompt:** Refine template with real corpus data
4. **Test interpretation:** Generate first interpretation report
5. **Validate and refine:** Check grounding, revise prompt

### Week 2 Tasks

6. **Integration:** Add `--interpret` flag to corpus profile script
7. **Documentation:** Update workflow docs, add interpretation guide
8. **Create planning document:** Formalise interpretation framework (this document)

---

**Document Status:** Planning framework v1.0 (recovered from VS Code crash)
**Next Update:** After design decisions and first implementation
**Location:** `planning/corpus-interpretation-framework.md`
