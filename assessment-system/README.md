# Extraction Assessment System

Operational scaffolding for executing the extraction assessment rubric (`planning/extraction-assessment-rubric-v1.md`).

**Purpose:** Systematic quality evaluation of completed extractions along two dimensions:
1. **Accuracy** - Correct quotes, proper interpretation, no hallucinations
2. **Granularity** - Appropriate atomicity and consistency

**Out of scope:** Completeness assessment (handled separately via multi-run comparison studies)

---

## Quick Start

### Medium Assessment (Recommended)

```bash
# 1. Sample extraction (52 stratified items)
python assessment-system/scripts/sample_extraction.py \
  outputs/ross-ballsun-stanton-2022/extraction.json \
  --depth medium \
  --output sample.json

# 2. Provide these inputs to your LLM of choice:
#    - prompts/assessment-medium.md (assessment instructions)
#    - sample.json (sampled items)
#    - Source paper: input/papers/processed-md/ross-ballsun-stanton-2022.md
#
# 3. LLM outputs structured JSON assessment
#
# 4. Fill in templates/assessment-report.md with results
```

**Time:** 2-3 hours LLM processing + 30 min report writing

---

## Assessment Depths

### Quick Assessment (30-45 min)
- **Sample:** 20 items (proportional stratified)
- **Mappings:** 10 random pairs
- **Use case:** Initial quality check, triage, periodic spot-checks
- **Prompt:** `prompts/assessment-quick.md` *[Not yet implemented - Phase 3]*

### Medium Assessment (2-3 hours) ✅ READY
- **Sample:** 52 items (15 claims, 20 evidence, 10 methods, 5 protocols, 2 designs)
- **Mappings:** 25 pairs (one complete section)
- **Use case:** Standard assessment, quality certification, diagnosing systematic issues
- **Prompt:** `prompts/assessment-medium.md`

### Deep Assessment (4-6+ hours)
- **Sample:** ALL items (no sampling)
- **Mappings:** ALL mappings
- **Use case:** Gold standard, problematic extractions, training dataset QA
- **Prompt:** `prompts/assessment-deep.md` *[Not yet implemented - Phase 3]*

---

## Workflow Detail

### Step 1: Sample Extraction

Use `scripts/sample_extraction.py` to create a stratified random sample:

```bash
python assessment-system/scripts/sample_extraction.py \
  <extraction.json> \
  --depth quick|medium|deep \
  --output sample.json \
  [--seed 42]
```

**Arguments:**
- `extraction.json`: Path to extraction file to assess
- `--depth`: Assessment depth (quick=20 items, medium=52 items, deep=all items)
- `--output`: Output path for sample JSON
- `--seed`: Optional random seed for reproducibility

**Output:** `sample.json` containing:
- Sampled items formatted for LLM readability (ID, type, content, quote, page, context)
- Mapping pairs to verify
- Metadata (paper slug, sample sizes, totals)

**Example:**
```bash
python assessment-system/scripts/sample_extraction.py \
  outputs/ross-ballsun-stanton-2022/extraction.json \
  --depth medium \
  --output ross-ballsun-stanton-2022-sample.json \
  --seed 42
```

### Step 2: Run Assessment (Manual)

**Inputs to provide your LLM:**

1. **Assessment prompt:** `prompts/assessment-medium.md`
   - Contains multi-pass workflow (Accuracy → Granularity → Mapping)
   - Includes category definitions and verification protocols
   - Specifies output format

2. **Sampled items:** `sample.json` (from Step 1)

3. **Source paper:** `input/papers/processed-md/[paper-slug].md`
   - Full text needed to verify quotes and context

**LLM Options:**
- Claude 3.7 Sonnet (recommended - built for this workflow)
- Gemini 2.5 Pro (good alternative)
- GPT-4.5 (alternative)
- Human assessor (gold standard)

**Process:**
1. Paste assessment prompt into LLM chat
2. Provide sample.json contents
3. Provide source paper text (or relevant sections)
4. LLM works through multi-pass assessment
5. LLM outputs structured JSON assessment

**Expected LLM time:**
- Quick: 30-45 min
- Medium: 2-3 hours
- Deep: 4-6+ hours (scales with extraction size)

### Step 3: Generate Report

**Manual (Current):**
1. Copy `templates/assessment-report.md`
2. Fill in sections using LLM's JSON output:
   - Summary scores
   - Error details
   - Granularity issues
   - Mapping analysis
   - Priority corrections
   - Overall assessment
3. Save to `outputs/[paper-slug]/assessment-report.md`

**Automated (Phase 2):**
```bash
# Future: Script to parse JSON and generate markdown report
python assessment-system/scripts/generate_report.py \
  assessment-output.json \
  --output assessment-report.md
```

---

## File Structure

```
assessment-system/
├── README.md                         # This file
├── prompts/
│   ├── assessment-quick.md           # [Phase 3] Quick assessment (30-45 min)
│   ├── assessment-medium.md          # ✅ Medium assessment (2-3 hours)
│   ├── assessment-deep.md            # [Phase 3] Deep assessment (4-6+ hours)
│   └── assessment-pass-templates/    # [Phase 3] Individual pass templates
│       ├── pass-a-accuracy.md
│       ├── pass-b-granularity.md
│       └── pass-c-mapping.md
├── scripts/
│   ├── sample_extraction.py          # ✅ Stratified sampling
│   ├── prepare_assessment_input.py   # [Phase 2] Format JSON → LLM input
│   ├── calculate_scores.py           # [Phase 2] Parse JSON → rubric scores
│   ├── generate_report.py            # [Phase 2] JSON → markdown report
│   └── aggregate_results.py          # [Phase 3] Multi-paper summary
└── templates/
    ├── assessment-report.json        # [Phase 2] Structured output schema
    └── assessment-report.md          # ✅ Human-readable template
```

**Status:**
- ✅ Phase 1 (Core): COMPLETE - Manual workflow ready to use
- [Phase 2] (Automation): Planned - Scripts for pre/post processing
- [Phase 3] (Scaling): Planned - Quick/Deep prompts, aggregation

---

## Sample Sizes

### Quick (20 items total)
- Proportional stratified sampling
- Maintains type distribution from extraction
- 10 random mappings

### Medium (52 items total) ✅
- **15 claims** (random sample)
- **20 evidence** (random sample)
- **10 methods** (random sample)
- **5 protocols** (random sample)
- **2 research designs** (random sample)
- **25 mappings** (one complete section)

### Deep (ALL items)
- No sampling - comprehensive assessment
- All mappings verified
- Critical for granularity assessment and edge case detection

---

## Scoring Methodology

### Accuracy Score
```
Accuracy = (Verified Correct Items - Error Penalties) / Total Items × 100%

Error Penalties:
  Hallucinations:       5 points each
  Confabulations:       3 points each
  Misattributions:      3 points each
  Miscategorisations:   1 point each
  Page Errors:          0.5 points each
  Context Errors:       2 points each
```

**Grades:**
- 95-100% (A): Excellent
- 85-94% (B): Good
- 75-84% (C): Acceptable
- 65-74% (D): Poor
- <65% (F): Unacceptable

### Granularity Score
```
Granularity = (Items at Appropriate Level) / Total Items × 100%

Appropriate Level = Total - Over-Split - Under-Split - Inconsistent
```

**Grades:** Same as Accuracy

### Mapping Score
```
Mapping = (Strong Mappings + 0.5 × Weak Mappings) / Total Mappings × 100%
```

**Grades:** Same as Accuracy

### Overall Score
```
Overall = (Accuracy × 0.50) + (Granularity × 0.30) + (Mapping × 0.20)
```

**Weights rationale:**
- Accuracy (50%): Most critical - errors undermine extraction
- Granularity (30%): Important for usability and assessment
- Mapping (20%): Useful but secondary - can be fixed post-hoc

---

## Output Formats

### JSON Output (from LLM)

```json
{
  "assessment_metadata": {
    "paper": "ross-ballsun-stanton-2022",
    "assessor": "claude-3.7-sonnet",
    "assessment_date": "2025-10-31",
    "assessment_depth": "medium",
    "sample_size": 52,
    "total_items_in_extraction": 176
  },
  "accuracy_assessment": {
    "items_assessed": 52,
    "verified_correct": 48,
    "errors_by_type": {...},
    "error_details": [...],
    "accuracy_score": 92.3,
    "grade": "A"
  },
  "granularity_assessment": {
    "items_assessed": 52,
    "appropriate_granularity": 45,
    "issue_details": [...],
    "granularity_score": 86.5,
    "grade": "B"
  },
  "mapping_assessment": {
    "mappings_assessed": 25,
    "strong_mappings": 20,
    "weak_mappings": 3,
    "incorrect_mappings": 2,
    "mapping_details": [...],
    "mapping_score": 88.0,
    "grade": "B"
  },
  "overall_assessment": {
    "weighted_score": 89.2,
    "grade": "B",
    "recommendation": "Good quality, some corrections needed"
  },
  "priority_corrections": [...]
}
```

### Markdown Report (for humans)

See `templates/assessment-report.md` for full template.

**Key sections:**
- Summary scores table
- Error details by type
- Granularity issues (over/under-split, inconsistent)
- Mapping analysis (strong/weak/incorrect)
- Priority corrections list
- Overall assessment and recommendations

---

## Usage Examples

### Example 1: Assess Ross & Ballsun-Stanton 2022

```bash
# Sample extraction
python assessment-system/scripts/sample_extraction.py \
  outputs/ross-ballsun-stanton-2022/extraction.json \
  --depth medium \
  --output rbs2022-sample.json \
  --seed 42

# Manual assessment
# 1. Open Claude/Gemini/GPT
# 2. Paste prompts/assessment-medium.md
# 3. Provide rbs2022-sample.json
# 4. Provide input/papers/processed-md/ross-ballsun-stanton-2022.md
# 5. LLM outputs JSON assessment

# Fill in report template
cp templates/assessment-report.md outputs/ross-ballsun-stanton-2022/assessment-report.md
# Edit with assessment results
```

### Example 2: Quick Check on Multiple Papers

```bash
# Sample all papers for quick assessment
for paper in outputs/*/extraction.json; do
  slug=$(basename $(dirname $paper))
  python assessment-system/scripts/sample_extraction.py \
    $paper \
    --depth quick \
    --output ${slug}-quick-sample.json \
    --seed 42
done

# Run quick assessments (30-45 min each)
# Identify outliers for deeper review
```

### Example 3: Deep Assessment of Gold Standard

```bash
# Deep assessment (all items)
python assessment-system/scripts/sample_extraction.py \
  outputs/sobotkova-et-al-2023/extraction.json \
  --depth deep \
  --output sobotkova2023-deep-sample.json

# This will use ALL items (no sampling)
# Run comprehensive assessment (4-6+ hours)
# Use as gold standard / training data QA
```

---

## Tips and Best Practices

### For Assessors

1. **Always read context:** Don't verify quotes in isolation - read ±2 paragraphs
2. **Document ambiguity:** Edge cases inform rubric refinement
3. **Focus on patterns:** You're assessing extraction quality, not paper quality
4. **Use consistent standards:** Apply category definitions uniformly
5. **Note systematic issues:** Are errors clustered by section, item type, or topic?

### For LLM Assessment

1. **Choose appropriate model:**
   - Claude 3.7 Sonnet: Best for accuracy verification, good context handling
   - Gemini 2.5 Pro: Good alternative, strong on structured output
   - GPT-4.5: Alternative option

2. **Provide full context:** Always include source paper text, not just sample.json

3. **Cross-validate critical extractions:**
   - Run same assessment with 2-3 different LLMs
   - Items flagged by multiple LLMs → high confidence errors
   - Items flagged by one LLM only → human review needed

4. **Spot-check LLM assessments:**
   - Human verify 20% of LLM's findings
   - If agreement >90%, trust LLM
   - If agreement <90%, investigate LLM systematic errors

### For Reproducibility

1. **Use --seed parameter:** Ensures same sample across runs
2. **Document LLM model:** Record exact model version
3. **Save raw JSON output:** Before filling markdown template
4. **Archive sample.json:** Keep record of which items were assessed

---

## Troubleshooting

### "Sample is smaller than requested"

If extraction has fewer items than sample size, script uses all available items.

**Example:**
- Requested: medium (15 claims)
- Available: 12 claims
- Result: All 12 claims sampled

### "Not all item types present"

Some papers may lack certain item types (e.g., no protocols).

**Solution:** Script will sample 0 items for missing types. Assessment proceeds with available types.

### "LLM output doesn't match JSON schema"

If LLM produces non-conforming JSON:
1. Check prompt was provided completely
2. Verify sample.json format
3. Try different LLM model
4. Fall back to manual report filling

### "Assessment takes too long"

For large extractions (>200 items):
- Use medium or quick depth initially
- Reserve deep assessment for critical papers
- Consider splitting across multiple LLM sessions

---

## Future Enhancements (Phase 2-3)

### Phase 2: Automation Scripts (Planned)
- `prepare_assessment_input.py`: Auto-extract context from paper around quotes
- `calculate_scores.py`: Parse LLM JSON → automatic scoring
- `generate_report.py`: JSON → markdown report (auto-fill template)

### Phase 3: Scaling Features (Planned)
- Quick and Deep assessment prompts
- `aggregate_results.py`: Multi-paper summary statistics
- Confidence intervals for sampled assessments
- Cross-model comparison tools

---

## Related Documentation

- **Rubric:** `planning/extraction-assessment-rubric-v1.md` - Complete assessment methodology
- **Metrics Analysis:** `planning/extraction-metrics-guidance-analysis.md` - Discussion of numeric targets
- **Multi-run Protocol:** `planning/active-todo-list.md` Section 7 - Completeness via comparison
- **Schema:** `extraction-system/schema/` - Extraction structure definitions

---

## Support and Feedback

For issues, questions, or suggestions:
1. Check this README and the rubric
2. Review example assessments in `outputs/*/assessment-report.md`
3. Document issues in `planning/active-todo-list.md`

---

## Changelog

**v1.0 (2025-10-31):**
- Phase 1 (Core) implementation
- Medium assessment prompt
- sample_extraction.py script
- Assessment report template
- Manual workflow documentation
- Ready for pilot testing
