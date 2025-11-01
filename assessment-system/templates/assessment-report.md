# Extraction Assessment Report

**Paper:** [Title, Authors, Year]
**Extraction File:** [path/to/extraction.json]
**Assessor:** [Human or LLM model]
**Assessment Date:** [YYYY-MM-DD]
**Assessment Depth:** [Quick / Medium / Deep]

---

## Summary Scores

| Dimension | Score | Grade | Status |
|-----------|-------|-------|--------|
| Accuracy | [X]% | [A-F] | [Excellent/Good/Acceptable/Poor/Unacceptable] |
| Granularity | [X]% | [A-F] | [Excellent/Good/Acceptable/Poor/Unacceptable] |
| Mapping Accuracy | [X]% | [A-F] | [Excellent/Good/Acceptable/Poor/Unacceptable] |
| **Overall** | **[X]%** | **[A-F]** | **[Status]** |

**Overall Calculation:** `([Accuracy] × 0.50) + ([Granularity] × 0.30) + ([Mapping] × 0.20) = [Overall]`

---

## Accuracy Assessment

**Items Assessed:** [N] / [Total] total (stratified sample / all items)
- Claims: [N] assessed
- Evidence: [N] assessed
- Methods: [N] assessed
- Protocols: [N] assessed
- Research Designs: [N] assessed

### Error Summary

| Error Type | Count | Penalty Points | Total Penalty |
|------------|-------|----------------|---------------|
| Hallucinations | [N] | 5 per error | [X] |
| Confabulations | [N] | 3 per error | [X] |
| Misattributions | [N] | 3 per error | [X] |
| Miscategorisations | [N] | 1 per error | [X] |
| Page Errors | [N] | 0.5 per error | [X] |
| Context Errors | [N] | 2 per error | [X] |
| **Total Penalties** | | | **[X]** |

### Score Calculation

```
Verified Correct Items: [N]
Total Items Assessed: [N]
Error Penalties: [X]

Accuracy Score = ([Verified Correct] - [Error Penalties]) / [Total Items] × 100%
               = ([N] - [X]) / [N] × 100%
               = [X]%
```

### Error Details

#### Critical Errors (Hallucinations)
[None found / List errors:]
- **[Item ID]**: [Description of hallucination]

#### Major Errors (Confabulations)
[None found / List errors:]
- **[Item ID]**: [Description - quote exists but meaning misrepresented]
  - *Example: Paper says "no evidence of X" but extracted as "Evidence shows X"*

#### Major Errors (Misattributions)
[None found / List errors:]
- **[Item ID]**: [Description - from cited work, not paper's claim]
  - *Example: "Smith (2015) found X" extracted as paper's own evidence*

#### Moderate Errors (Miscategorisations)
[None found / List errors:]
- **[Item ID]**: [Description - wrong category]
  - *Actual category should be: [claim/evidence/method/protocol/design]*

#### Minor Errors (Page Errors)
[None found / List errors:]
- **[Item ID]**: Quote on page [X] but extraction says page [Y]

#### Moderate Errors (Context Errors)
[None found / List errors:]
- **[Item ID]**: [Description - missing important context]
  - *Example: Regional qualifier omitted, changing meaning*

### Patterns and Observations

[Describe any systematic patterns:]
- [Are errors concentrated in specific sections?]
- [Are certain item types more prone to errors?]
- [Are there systematic miscategorisations (e.g., claims as evidence)?]

---

## Granularity Assessment

**Items Assessed:** [N]

### Granularity Issues

| Issue Type | Count | Percentage |
|------------|-------|------------|
| Appropriate Granularity | [N] | [X]% |
| Over-Split (Too Fine) | [N] | [X]% |
| Under-Split (Too Coarse) | [N] | [X]% |
| Inconsistent Detail Level | [N] | [X]% |

### Score Calculation

```
Appropriate Granularity Items: [N]
Total Items Assessed: [N]

Granularity Score = [Appropriate] / [Total] × 100%
                  = [N] / [N] × 100%
                  = [X]%
```

### Issue Details

#### Over-Split Items (Should Be Merged)
[None found / List issues:]

**[Item ID] + [Item ID]**: [Description]
- **Issue**: [Why these should be merged]
- **Example**: [Quote the items]
- **Suggested Action**: Merge into single [claim/evidence/method/protocol]

#### Under-Split Items (Should Be Split)
[None found / List issues:]

**[Item ID]**: [Description]
- **Issue**: [Why this should be split]
- **Example**: [Quote the item showing multiple distinct components]
- **Suggested Action**: Split into [2-3] separate [claims/evidence/methods/protocols]

#### Inconsistent Granularity
[None found / List issues:]

**[Item ID]**: [Description]
- **Issue**: [Too detailed compared to similar items / Too vague compared to similar items]
- **Comparison**: [Compare to similar item with different detail level]
- **Suggested Action**: [Increase detail / Reduce detail to match consistency]

### Patterns and Observations

[Describe granularity consistency:]
- [Is granularity generally consistent within item types?]
- [Are certain item types more granular than others? Is this justified?]
- [Are there systematic over/under-splitting patterns?]
- [Example: "Claims show high detail for genetic interpretations but low detail for environmental claims"]

---

## Mapping Assessment

**Mappings Assessed:** [N]

### Mapping Strength Distribution

| Strength | Count | Percentage |
|----------|-------|------------|
| Strong Mappings | [N] | [X]% |
| Weak Mappings | [N] | [X]% |
| Incorrect Mappings | [N] | [X]% |

### Score Calculation

```
Mapping Score = (Strong Mappings + 0.5 × Weak Mappings) / Total Mappings × 100%
              = ([N] + 0.5 × [N]) / [N] × 100%
              = [X]%
```

### Mapping Details

#### Strong Mappings
[List representative examples:]
- **[Item A] → [Item B]** ([mapping type]): [Why this mapping is strong]

#### Weak Mappings (Flag for Review)
[None found / List mappings:]
- **[Item A] → [Item B]** ([mapping type]): [Why this mapping is weak/uncertain]
  - **Issue**: [Connection requires inference, chain not fully clear]
  - **Action**: [Review / Strengthen with additional evidence / Keep with caveat]

#### Incorrect Mappings (Should Be Removed)
[None found / List mappings:]
- **[Item A] → [Item B]** ([mapping type]): [Why this mapping is incorrect]
  - **Issue**: [No logical connection / Misinterprets relationship]
  - **Action**: Remove mapping

### Patterns and Observations

[Describe mapping quality:]
- [Are certain types of mappings stronger than others?]
- [Are weak mappings concentrated in specific sections?]
- [Are there systematic mapping issues?]

---

## Priority Corrections

[List corrections in order of priority:]

1. **Critical**: [Fix hallucinations in: [Item IDs]]
2. **High Priority**: [Fix confabulations in: [Item IDs]]
3. **High Priority**: [Fix misattributions in: [Item IDs]]
4. **Medium Priority**: [Merge over-split items: [Item ID + Item ID, ...]]
5. **Medium Priority**: [Split under-split items: [Item IDs]]
6. **Medium Priority**: [Remove incorrect mappings: [Item A → Item B, ...]]
7. **Low Priority**: [Fix page errors in: [Item IDs]]
8. **Low Priority**: [Review weak mappings: [Item A → Item B, ...]]

---

## Overall Assessment

### Strengths

[List what the extraction does well:]
- [Example: "Generally consistent extraction with accurate quotes"]
- [Example: "Good coverage of methodological argumentation"]
- [Example: "Clear mapping of claims to supporting evidence"]

### Weaknesses

[List systematic issues:]
- [Example: "Some confabulations in Discussion section"]
- [Example: "Inconsistent granularity for environmental claims"]
- [Example: "Background literature occasionally extracted as paper's own claims"]

### Recommendation

**Grade: [A-F]** - [Excellent / Good / Acceptable / Poor / Unacceptable]

**Usability:** [One of:]
- ✅ Suitable for assessment framework use with confidence (minimal corrections needed)
- ✅ Usable for assessment with awareness of limitations (some corrections needed)
- ⚠️ Usable but requires significant review (systematic corrections needed)
- ❌ Not suitable for assessment without substantial corrections
- ❌ Re-extraction recommended rather than correction

**Next Steps:** [What should be done:]
- [Example: "Fix identified confabulations and misattributions, then re-run validation"]
- [Example: "Merge over-split items and reassess granularity consistency"]
- [Example: "Use as-is with noted limitations for pilot assessment"]

---

## Assessor Notes

[Any additional observations, patterns, concerns, or praise:]

[Examples:]
- "This is a methodological paper, so the profile (heavy claims, light evidence) is expected and appropriate"
- "Extraction quality appears higher in Methods section compared to Discussion - may indicate different extraction sessions or fatigue"
- "Liberal over-extraction principle appears to be working well - Pass 2 consolidation should handle the few over-split items"
- "Consider whether claims about preregistration practices should be claims or implicit arguments (practice assumptions)"

---

## Metadata

**Rubric Version:** 1.0
**Assessment Workflow:** [Manual / LLM-assisted / Fully automated]
**Time Taken:** [Hours] hours
**Statistical Confidence:** [For sampled assessments: confidence intervals, extrapolation notes]

---

## Appendix: Sampled Items (if applicable)

[For quick/medium assessments, list the items that were assessed:]

### Claims Assessed
- [C001, C005, C012, ...]

### Evidence Assessed
- [E002, E008, E015, ...]

### Methods Assessed
- [M001, M003, M007, ...]

### Protocols Assessed
- [P001, P004, ...]

### Research Designs Assessed
- [RD001, RD003]

[End of Report]
