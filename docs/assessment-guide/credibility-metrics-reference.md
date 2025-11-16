# Credibility Metrics Reference Guide

**Version:** 1.0
**Date:** 2025-11-14
**Status:** Exploratory metrics for iterative refinement

---

## Overview

This guide documents the eight quantitative credibility metrics used to assess research transparency, replicability, and methodological rigour. These metrics are **exploratory instruments** designed for iterative refinement based on empirical validation, not validated psychometric tools.

### Purpose and Scope

The metrics serve as a **first-stage screening and triage system** within a hybrid quantitative-qualitative assessment architecture:

- **Quantitative metrics** (this document): Fast, objective, scalable screening to identify papers warranting deeper review
- **Qualitative rubrics** (Phase 2): Nuanced human/LLM judgement for in-depth assessment

### Design Philosophy

1. **Corpus-relative interpretation**: Compare papers within a corpus using percentiles, not just absolute scores
2. **Complementary indicators**: Use multiple metrics together; no single metric defines "quality"
3. **Transparency about limitations**: Document known biases and failure modes
4. **Iterative refinement**: Calibrate thresholds and formulas based on empirical data
5. **Extraction dependency**: Metrics measure what we extracted and how we structured it, not just research quality

### Important Caveats

These metrics are subject to several systematic limitations:

- **Domain/genre bias**: Different paper types (theoretical vs empirical, articles vs book chapters) score differently
- **Extraction granularity dependency**: How we split items during extraction affects counts
- **Fixed thresholds**: Current "expected" values are bootstrapping placeholders needing calibration
- **No ground truth validation**: Metrics not yet validated against external quality assessments
- **"More is better" fallacy**: Higher counts don't always mean better research (e.g., limitations quality vs quantity)
- **Sample size dependency**: Small corpora produce unstable percentiles and unreliable statistics

---

## The Eight Metrics

### ESD: Evidential Support Density

**Full name:** Evidential Support Density

**Scale:** Ratio (lower is better)

**Formula:** `claims_count / evidence_count`

#### What It Measures

The ratio of claims to evidence items. Lower scores indicate more evidence per claim, suggesting stronger empirical support.

#### Calculation Method

```python
claims_count = len(extraction['claims'])
evidence_count = len(extraction['evidence'])
esd = claims_count / evidence_count if evidence_count > 0 else float('inf')
```

#### Interpretation Scale

- **Lower is better**: More evidence per claim
- **0.0**: No explicit claims extracted (edge case)
- **< 1.0**: More evidence than claims (strong empirical support)
- **1.0**: Equal evidence and claims (balanced)
- **> 1.0**: More claims than evidence (potentially under-supported)
- **inf**: No evidence extracted (critical concern)

#### Strengths

- Objective count-based metric
- Computationally efficient
- Highlights papers needing evidence review
- Correlates with empirical vs theoretical emphasis

#### Limitations

1. **Confuses extraction with quality**: Well-extracted verbose descriptions score "better" than nuanced interpretations
2. **Genre bias**: Theoretical papers naturally have higher ratios
3. **Extraction granularity**: How we split claims and evidence affects scores dramatically
4. **Zero-claim edge case**: ESD=0.0 may indicate extraction issue, not quality
5. **Doesn't assess evidence quality**: Ten weak evidence items beat one strong one

#### When to Use

- Identifying papers with potentially unsupported claims (high ESD)
- Comparing empirical vs theoretical emphasis across corpus
- Flagging extraction issues (ESD=0.0 or inf)

#### When NOT to Use

- Comparing papers from different genres (methods vs empirical)
- As sole criterion for research quality
- Without reviewing actual claim and evidence content

---

### TCI: Transparency Completeness Index

**Full name:** Transparency Completeness Index

**Scale:** 0-1 (higher is better)

**Formula:** `(RD_count + methods_count + protocols_count) / (expected_RD + expected_methods + expected_protocols)`

#### What It Measures

Coverage of Research Design and Methods Assessment Protocol (RDMAP) documentation. Higher scores indicate more comprehensive methodological transparency.

#### Calculation Method

```python
rd_count = len(extraction['research_designs'])
methods_count = len(extraction['methods'])
protocols_count = len(extraction['protocols'])

# Current expected values (bootstrapping placeholders)
expected_rd = 2
expected_methods = 5
expected_protocols = 8

actual_total = rd_count + methods_count + protocols_count
expected_total = expected_rd + expected_methods + expected_protocols
tci = min(actual_total / expected_total, 1.0)  # Cap at 1.0
```

#### Interpretation Scale

- **Higher is better**: More complete RDMAP documentation
- **0.0**: No RDMAP items extracted (critical concern)
- **< 0.5**: Sparse methodological documentation
- **0.5-0.8**: Moderate documentation
- **0.8-1.0**: Strong documentation
- **1.0**: Meets or exceeds expected RDMAP coverage

#### Strengths

- Simple, interpretable metric
- Directly measures methodological transparency
- Computationally efficient
- Highlights papers with insufficient methods documentation

#### Limitations

1. **Fixed thresholds**: "Expected" values (2 RD, 5 methods, 8 protocols) are arbitrary bootstrapping placeholders
2. **Doesn't distinguish broad vs narrow research**: A focused study with 1 RD, 3 methods, 5 protocols (narrow but complete) scores worse than a multi-method study (broad)
3. **Extraction granularity**: How we split RDMAP items affects scores dramatically
4. **Doesn't assess RDMAP quality**: Ten vague protocol descriptions beat five detailed ones
5. **Genre bias**: Experimental papers naturally have more protocols than archival research
6. **Caps at 1.0**: Can't distinguish papers with 15 items from those with 30 items

#### When to Use

- Identifying papers with sparse methodological documentation (TCI < 0.5)
- Comparing RDMAP completeness across similar paper types
- Flagging papers needing methods review

#### When NOT to Use

- Comparing papers from different genres/domains
- As sole criterion for methodological rigour
- Without corpus-relative benchmarks

#### Future Refinement Needed

1. **Adaptive thresholds**: Calculate corpus mean or use domain-specific benchmarks
2. **Tier weighting**: Should protocols count more than RD? Should all three tiers be weighted equally?
3. **Quality incorporation**: Combine count with verbatim quote length (see MDD) or expert ratings

---

### SCS: Scope Constraint Score

**Full name:** Scope Constraint Score

**Scale:** Count (higher is better, but with caveats)

**Formula:** `len(extraction['limitations'])`

#### What It Measures

Number of explicit limitation, qualification, or scope constraint statements. Higher scores theoretically indicate more transparent acknowledgement of research boundaries.

#### Calculation Method

```python
limitations = extraction.get('limitations', [])
scs = len(limitations)
```

#### Interpretation Scale

- **Higher is theoretically better**: More explicit scope constraints
- **0**: No limitations extracted (potential concern or extraction issue)
- **1-3**: Few limitations acknowledged
- **4-10**: Moderate constraint transparency
- **> 10**: Extensive limitation discussion

#### Strengths

- Simple count-based metric
- Highlights papers with explicit scope discussions
- Computationally efficient

#### Limitations

1. **Most critical limitation**: **Counts limitations, not quality**. One serious unresolved limitation (e.g., "no validation data") is worse than ten trivial ones (e.g., "sample limited to Bulgaria").
2. **"Solved limitation" problem**: Papers may acknowledge limitations only to claim they solved them (e.g., "Previous studies lacked X. We addressed this by Y."). Current extraction doesn't distinguish acknowledged limitations from resolved ones.
3. **Extraction inconsistency**: Papers may discuss limitations implicitly (embedded in methods discussion) rather than in dedicated "Limitations" sections. Extraction varies.
4. **Genre bias**: Methodological papers naturally discuss more technical limitations than descriptive papers.
5. **Perverse incentives**: If used as target, encourages listing trivial limitations rather than addressing serious ones (Campbell's Law).
6. **Zero scores ambiguous**: Could mean no limitations (overconfident paper), no limitations section (structural issue), or extraction failure.

#### When to Use

- Identifying papers with no explicit limitation discussion (SCS = 0) for review
- Comparing limitation transparency across similar papers
- Corpus-level assessment: What proportion of papers discuss limitations?

#### When NOT to Use

- **As primary quality metric**: High SCS doesn't mean good research
- Comparing papers from different genres
- Without reviewing actual limitation content and severity

#### Future Refinement Needed

1. **Qualitative coding**: Distinguish trivial vs serious limitations, resolved vs unresolved
2. **Severity weighting**: Weight limitations by impact on conclusions
3. **Implicit limitation extraction**: Capture limitations embedded in methods sections
4. **Corpus benchmarking**: Establish domain-specific norms

#### Critical Note

**SCS is the most problematic metric in the current suite.** It needs significant refinement based on empirical data. Consider it a placeholder for a more sophisticated limitation assessment.

---

### RTI: Robustness Triangulation Index

**Full name:** Robustness Triangulation Index

**Scale:** Shannon H (0-3+ typical range, higher is better)

**Formula:** Shannon diversity index of evidence types

#### What It Measures

Diversity of evidence types used to support claims. Higher scores indicate more varied evidential basis (triangulation), suggesting more robust findings.

#### Calculation Method

Uses Shannon diversity index from information theory:

```python
from collections import Counter
import math

evidence_items = extraction.get('evidence', [])
evidence_types = [e.get('type', 'unspecified') for e in evidence_items]
type_counts = Counter(evidence_types)
total = len(evidence_types)

# Shannon H = -Σ(p_i × ln(p_i))
shannon_h = 0.0
for count in type_counts.values():
    p_i = count / total
    shannon_h -= p_i * math.log(p_i)

rti = round(shannon_h, 2)
```

#### Interpretation Scale

- **Higher is better**: More diverse evidence types
- **0.0**: All evidence is same type (no diversity)
- **0.5-1.5**: Low diversity (1-2 dominant types)
- **1.5-2.5**: Moderate diversity (multiple types, some dominant)
- **2.5-3.5**: High diversity (many types, balanced)
- **> 3.5**: Very high diversity (many balanced types)

**Shannon H properties:**

- Maximum when all types equally frequent
- Penalises both low richness (few types) and low evenness (unbalanced distribution)
- Typical range: 0-3 for most research papers

#### Strengths

- Well-established diversity measure from ecology/information theory
- Captures both richness (number of types) and evenness (balanced distribution)
- Interpretable: H=0 (mono-method), H=2 (moderate diversity), H=3+ (high diversity)
- Highlights papers with triangulation

#### Limitations

1. **Evidence type ontology dependency**: RTI depends on how we categorise evidence types during extraction. Fine-grained ontology (20 types) inflates RTI vs coarse ontology (5 types).
2. **Doesn't assess evidence quality**: Ten weak evidence types beat one strong type.
3. **Genre bias**: Experimental papers naturally have more diverse evidence types than archival/textual papers.
4. **Extraction granularity**: How we split evidence items affects type distribution.
5. **"More is better" assumption**: High diversity isn't always better. A focused single-method study with deep analysis may be stronger than a shallow multi-method study.
6. **Type specificity varies**: Some papers have very specific evidence types ("archaeobotanical macrofossils"), others generic ("qualitative interview"). Affects comparability.

#### When to Use

- Comparing methodological diversity across corpus
- Identifying mono-method papers (RTI < 0.5) vs multi-method papers (RTI > 2.0)
- Flagging papers with potential triangulation (high RTI) for quality review

#### When NOT to Use

- Comparing papers from different genres (archival vs experimental)
- As sole criterion for robustness (quality matters more than diversity)
- Without reviewing actual evidence types and their appropriateness

#### Future Refinement Needed

1. **Evidence type ontology standardisation**: Define consistent, domain-appropriate evidence type taxonomy
2. **Quality weighting**: Incorporate evidence strength into diversity calculation
3. **Genre-specific benchmarks**: Establish domain norms for RTI

---

### RIS: Replicability Infrastructure Score

**Full name:** Replicability Infrastructure Score

**Scale:** 0-10 (higher is better)

**Formula:** Sum of binary/weighted indicators for PIDs and sharing statements

#### What It Measures

Availability of Persistent Identifiers (PIDs) and data/code/materials sharing infrastructure. Higher scores indicate better replicability infrastructure.

#### Calculation Method

```python
infrastructure = extraction['reproducibility_infrastructure']
pids = infrastructure['persistent_identifiers']
data_avail = infrastructure['data_availability']
code_avail = infrastructure['code_availability']

score = 0

# Paper DOI (1 point)
if pids['paper_doi'] and pids['paper_doi']['doi']:
    score += 1

# Author ORCIDs (1 point if >0% coverage)
if pids['orcid_coverage']['coverage_percentage'] > 0:
    score += 1

# Dataset PIDs (2 points if any present)
if len(pids['dataset_pids']) > 0:
    score += 2

# Software PIDs (2 points if any present)
if len(pids['software_pids']) > 0:
    score += 2

# Data availability statement (1 point)
if data_avail['statement_present']:
    score += 1

# Code availability statement (1 point)
if code_avail['statement_present']:
    score += 1

# Supplementary materials (1 point)
if infrastructure['supplementary_materials']['present']:
    score += 1

# Preregistration (1 point)
if infrastructure['preregistration']['preregistered']:
    score += 1

# Total: 0-10
```

#### Interpretation Scale

- **Higher is better**: More replicability infrastructure
- **0**: No PIDs or sharing infrastructure
- **1-3**: Minimal infrastructure (paper DOI only, maybe ORCIDs)
- **4-6**: Moderate infrastructure (paper DOI, ORCIDs, some data/code sharing)
- **7-9**: Strong infrastructure (PIDs + sharing statements + supplements)
- **10**: Exemplary infrastructure (all components present)

#### Strengths

- Objective, auditable metric based on verifiable infrastructure
- Directly measures FAIR-aligned replicability components
- Encourages adoption of PIDs and sharing norms
- Computationally efficient

#### Limitations

1. **Binary scoring**: Presence/absence, not quality. A DOI linking to inaccessible data scores same as open data with rich metadata.
2. **Doesn't assess accessibility**: PID present ≠ data accessible. Many dataset DOIs lead to login walls or institutional access.
3. **Doesn't assess usability**: Shared data may be poorly documented, wrong format, or incomplete.
4. **Genre bias**: Experimental/quantitative papers more likely to have dataset PIDs than archival/qualitative papers.
5. **Temporal bias**: Older papers (pre-2015) predate PID infrastructure norms; unfairly penalised.
6. **Weighting arbitrary**: Why are dataset PIDs (2 points) worth more than data statements (1 point)? Current weights are bootstrapping placeholders.
7. **Incomplete infrastructure coverage**: Doesn't measure protocols.io, registered reports, open peer review, etc.

#### When to Use

- Identifying papers with strong replicability infrastructure (RIS ≥ 6)
- Flagging papers with no infrastructure (RIS = 0) for potential data/code requests
- Corpus-level assessment: What proportion of papers share data/code?
- Temporal trends: Are newer papers scoring higher?

#### When NOT to Use

- Comparing papers from different time periods (pre-2015 vs post-2020)
- Comparing papers from different genres (experimental vs archival)
- As sole criterion for replicability (infrastructure present ≠ actually replicable)
- Without reviewing actual accessibility and usability of shared resources

#### Future Refinement Needed

1. **Quality weighting**: Distinguish open data (3 points) from restricted data (1 point)
2. **Accessibility checking**: Verify DOIs resolve and data is accessible
3. **Usability assessment**: Check for documentation, metadata, standard formats
4. **Genre-specific scoring**: Adjust expectations for archival vs experimental papers
5. **Temporal adjustment**: Control for publication year when comparing papers

---

### PGCS: PID Graph Connectivity Score

**Full name:** PID Graph Connectivity Score

**Scale:** 0-10 (higher is better)

**Formula:** Uses existing connectivity score from Pass 6 infrastructure extraction

#### What It Measures

Connectivity between different Persistent Identifiers (PIDs) in the research PID graph. Higher scores indicate more integrated FAIR infrastructure.

#### Calculation Method

```python
infrastructure = extraction['reproducibility_infrastructure']
pids = infrastructure['persistent_identifiers']
pid_graph = pids['pid_graph_summary']

# Use existing Pass 6 assessment
connectivity_score = pid_graph['connectivity_score']  # 0-10 scale
connectivity_rating = pid_graph['connectivity_rating']  # 'none', 'minimal', 'moderate', 'strong', 'exemplary'
rationale = pid_graph['rationale']

# Count PID types for context
pid_counts = {
    'paper_doi': 1 if pids['paper_doi'] else 0,
    'author_orcids': len(pids['author_orcids']),
    'dataset_pids': len(pids['dataset_pids']),
    'software_pids': len(pids['software_pids']),
    'sample_pids': len(pids['sample_pids']),
    'project_pid': 1 if pids['project_pid'] else 0,
    'vocabulary_pids': len(pids['vocabulary_pids'])
}
```

#### Interpretation Scale

- **Higher is better**: More connected PID infrastructure
- **0 (none)**: No PIDs or no connections
- **1-3 (minimal)**: Few PIDs, minimal connections (e.g., paper DOI only)
- **4-6 (moderate)**: Multiple PIDs with some connections
- **7-9 (strong)**: Well-connected PID graph
- **10 (exemplary)**: Fully connected PID ecosystem

**Connectivity ratings from Pass 6:**

- **None**: No PIDs or isolated PIDs
- **Minimal**: Paper DOI only or paper DOI + ORCIDs
- **Moderate**: Paper DOI + ORCIDs + dataset/software PIDs
- **Strong**: Rich PID graph with dataset, software, sample, project PIDs
- **Exemplary**: Comprehensive PID graph including vocabulary/ontology PIDs

#### Strengths

- Directly measures FAIR infrastructure integration
- Captures relational structure of research outputs (not just presence/absence)
- Highlights papers with exemplary PID practices
- Leverages existing Pass 6 assessment (no duplicate calculation)

#### Limitations

1. **Subjective connectivity assessment**: Pass 6 connectivity score is LLM-assessed, not formula-based. Variability across extractions.
2. **Doesn't assess PID quality**: PIDs present and connected ≠ PIDs resolve correctly or link to accessible resources.
3. **Genre bias**: Experimental papers with datasets/software naturally score higher than archival papers.
4. **Temporal bias**: PID infrastructure adoption increased over time; older papers penalised.
5. **Binary presence/absence**: Doesn't distinguish 1 dataset PID from 10 dataset PIDs.
6. **Missing PIDs**: Doesn't capture all PID types (e.g., grants, institutions, instruments).

#### When to Use

- Identifying papers with exemplary PID infrastructure (PGCS ≥ 7)
- Comparing PID adoption across corpus
- Flagging papers with isolated PIDs (PGCS ≤ 2) for infrastructure improvement
- Temporal trends: Is PID connectivity improving over time?

#### When NOT to Use

- Comparing papers from different time periods
- Comparing papers from different genres
- As sole criterion for FAIR compliance (connectivity ≠ accessibility or reusability)
- Without reviewing actual PID resolution and accessibility

#### Relationship to RIS

- **RIS**: Measures PID presence/absence (binary)
- **PGCS**: Measures PID connectivity (relational)
- **Complementary**: RIS asks "Do you have PIDs?" PGCS asks "Are your PIDs connected?"

A paper can have high RIS but low PGCS (many isolated PIDs) or low RIS but moderate PGCS (few well-connected PIDs).

#### Future Refinement Needed

1. **Formula-based calculation**: Replace LLM assessment with objective formula based on PID graph structure
2. **PID resolution checking**: Verify PIDs resolve correctly
3. **Weighting by PID type**: Are dataset PIDs more important than vocabulary PIDs?
4. **Graph metrics**: Use network analysis (degree centrality, clustering coefficient) for sophisticated connectivity assessment

---

### FCS: FAIR Compliance Score

**Full name:** FAIR Compliance Score

**Scale:** 0-15 (higher is better)

**Formula:** Sum of Findable + Accessible + Interoperable + Reusable scores from Pass 6 FAIR assessment

#### What It Measures

Aggregate compliance with FAIR (Findable, Accessible, Interoperable, Reusable) principles. Higher scores indicate better alignment with open science infrastructure standards.

#### Calculation Method

```python
infrastructure = extraction['reproducibility_infrastructure']
fair = infrastructure['fair_assessment']

if not fair['assessed']:
    return {'score': 0, 'assessed': False}

# Extract dimension scores (from Pass 6 assessment)
findable_score = fair['findable']['score']  # Max 4
accessible_score = fair['accessible']['score']  # Max 4
interoperable_score = fair['interoperable']['score']  # Max 3
reusable_score = fair['reusable']['score']  # Max 4

# Total score
fcs = findable_score + accessible_score + interoperable_score + reusable_score  # Max 15
```

#### FAIR Dimensions and Scoring

**Findable (0-4 points):**

- Globally unique and persistent identifier (PID)
- Rich metadata describing data
- Metadata indexed in searchable resource
- PID in metadata

**Accessible (0-4 points):**

- Data retrievable via open, standardised protocol
- Metadata remains accessible even if data is not
- Authentication and authorisation when necessary
- Metadata preservation

**Interoperable (0-3 points):**

- Data use formal, accessible, shared vocabulary
- Data include qualified references to other data
- Metadata use vocabulary following FAIR principles

**Reusable (0-4 points):**

- Rich metadata with provenance
- Data meet domain-relevant community standards
- Clear data usage licence
- Detailed data description

#### Interpretation Scale

- **Higher is better**: Better FAIR compliance
- **0**: FAIR assessment not conducted or failed all criteria
- **1-5**: Low compliance (minimal FAIR infrastructure)
- **6-10**: Moderate compliance (some FAIR components)
- **11-13**: Strong compliance (most FAIR components)
- **14-15**: Exemplary compliance (nearly full or full FAIR)

#### Strengths

- Directly aligned with established FAIR principles
- Comprehensive assessment across four dimensions
- Widely recognised open science standard
- Highlights papers with exemplary open science practices

#### Limitations

1. **Subjective dimension scoring**: Pass 6 FAIR assessment is LLM-based, not formula-based. Variability across extractions.
2. **Doesn't assess actual accessibility**: Score reflects claimed accessibility, not verified access.
3. **Doesn't assess actual reusability**: Shared data may be poorly documented or wrong format despite high score.
4. **Genre bias**: FAIR principles designed for datasets; less applicable to purely theoretical papers.
5. **Temporal bias**: FAIR principles formalised in 2016; older papers penalised.
6. **Equal weighting**: All four dimensions weighted equally. Should Accessible be more important than Interoperable?
7. **Domain-specific standards**: "Interoperable" and "Reusable" depend on domain standards (archaeology vs genetics different).

#### When to Use

- Identifying papers with exemplary FAIR compliance (FCS ≥ 14)
- Comparing open science infrastructure across corpus
- Temporal trends: Is FAIR compliance improving?
- Flagging papers with low compliance (FCS < 6) for infrastructure improvement

#### When NOT to Use

- Comparing papers from different time periods (pre-2016 vs post-2020)
- Comparing papers from different genres (theoretical vs empirical)
- As sole criterion for research quality (FAIR ≠ rigorous or impactful)
- Without reviewing actual data accessibility and usability

#### Relationship to RIS and PGCS

- **RIS**: Measures PID infrastructure presence/absence
- **PGCS**: Measures PID connectivity
- **FCS**: Measures FAIR compliance (broader than PIDs, includes metadata, accessibility, licences)

All three are complementary aspects of replicability infrastructure.

#### Future Refinement Needed

1. **Formula-based calculation**: Replace LLM assessment with objective checklist
2. **Verification**: Check PIDs resolve, data is accessible, formats are standard
3. **Domain-specific benchmarks**: Different FAIR expectations for different domains
4. **Dimension weighting**: Should some FAIR dimensions be weighted more heavily?

---

### MDD: Methods Documentation Density

**Full name:** Methods Documentation Density

**Scale:** Mean characters per RDMAP item (higher is better)

**Formula:** `mean(len(verbatim_quote) for all RDMAP items)`

#### What It Measures

Average length of verbatim quotes extracted for Research Design, Methods, and Protocols (RDMAP) items. Higher values indicate more detailed methodological documentation.

#### Calculation Method

```python
research_designs = extraction['research_designs']
methods = extraction['methods']
protocols = extraction['protocols']

def get_text_length(item):
    # Try multiple possible text field names
    text = (item.get('verbatim_quote') or
            item.get('text') or
            item.get('description') or
            item.get('research_design_text') or
            item.get('method_text') or
            item.get('protocol_text') or
            '')
    return len(text)

# Calculate lengths for each tier
rd_lengths = [get_text_length(rd) for rd in research_designs]
method_lengths = [get_text_length(m) for m in methods]
protocol_lengths = [get_text_length(p) for p in protocols]

# Overall mean across all RDMAP items
all_lengths = rd_lengths + method_lengths + protocol_lengths
mdd = sum(all_lengths) / len(all_lengths) if all_lengths else 0
```

#### Interpretation Scale

- **Higher is better**: More detailed methodological documentation
- **0**: No RDMAP items or no verbatim quotes
- **< 100**: Sparse documentation (terse descriptions)
- **100-200**: Moderate documentation (paragraph-length descriptions)
- **200-300**: Detailed documentation (multi-paragraph descriptions)
- **> 300**: Extensive documentation (very detailed descriptions)

#### Strengths

- Objective metric based on extracted text length
- Computationally efficient
- Highlights papers with extensive methodological detail
- Complements TCI (count-based): TCI measures breadth, MDD measures depth

#### Limitations

1. **Confuses verbosity with quality**: Long descriptions aren't necessarily better. A concise, precise 50-character protocol may be clearer than a rambling 500-character one.
2. **Extraction dependency**: MDD measures how much text we extracted, not how much detail the paper contains. Extraction decisions (where to start/stop verbatim quote) affect scores dramatically.
3. **Genre bias**: Some domains (archaeology, ecology) write longer methods sections than others (mathematics, theoretical computer science).
4. **Doesn't assess clarity or usability**: Long methods section with jargon scores higher than short methods section with clear step-by-step instructions.
5. **Tier aggregation**: Averages across RD, methods, protocols. Are all three tiers equally important? Should protocols (specific, actionable) be weighted more than RD (high-level)?
6. **Arbitrary thresholds**: No empirical calibration for what constitutes "good" MDD.

#### When to Use

- Identifying papers with sparse methodological detail (MDD < 100)
- Comparing methodological documentation depth across corpus
- Flagging papers for replicability review (low MDD = potentially insufficient detail to replicate)

#### When NOT to Use

- Comparing papers from different genres (fieldwork vs computational)
- As sole criterion for methodological rigour (detail ≠ clarity or replicability)
- Without reviewing actual methods text for clarity and completeness

#### Relationship to TCI

- **TCI**: Breadth (how many RDMAP items?)
- **MDD**: Depth (how detailed is each RDMAP item?)
- **Complementary**: High TCI + high MDD = comprehensive, detailed methods. High TCI + low MDD = many terse items. Low TCI + high MDD = few items, but detailed.

#### Future Refinement Needed

1. **Quality assessment**: Combine length with clarity, precision, actionability ratings
2. **Tier weighting**: Should protocols be weighted more than RD?
3. **Genre-specific benchmarks**: Different expectations for different domains
4. **Extraction standardisation**: Define consistent extraction boundaries for verbatim quotes

---

## Using Metrics Together

### Complementary Patterns

Metrics should be interpreted in combination to build a multi-dimensional assessment:

**High transparency, low infrastructure:**

- TCI = 1.0, FCS = 8, RIS = 1
- Interpretation: Good methodological documentation, but poor data/code sharing
- Action: Encourage authors to deposit data and obtain PIDs

**High infrastructure, sparse methods:**

- TCI = 0.5, FCS = 14, RIS = 6
- Interpretation: Excellent FAIR compliance, but insufficient methodological detail
- Action: Request more detailed methods documentation

**High claims, low evidence:**

- ESD = 2.5, RTI = 0.5
- Interpretation: Many claims, little evidence, mono-method
- Action: Flag for evidence quality review

**Low limitations, high confidence:**

- SCS = 0, ESD = 2.0
- Interpretation: No limitations acknowledged, many claims per evidence
- Action: Flag for overconfidence or extraction issue

### Corpus-Relative Interpretation

Always compare papers to corpus distribution using percentiles:

**Percentile calculation:**

```python
# For metric score x in corpus with n papers
percentile = (rank(x) / n) * 100

# Example: Paper with FCS = 12 in corpus with scores [8, 10, 10, 11, 11, 12, 13, 14, 14, 15]
# Rank = 6 (6th position in sorted list)
# Percentile = (6/10) * 100 = 60th percentile
```

**Interpretation:**

- **< 25th percentile**: Below average for corpus (flag for review)
- **25-50th percentile**: Below median (may need improvement)
- **50-75th percentile**: Above median (acceptable)
- **> 75th percentile**: Top quartile (strong performance)

### Metric Combinations for Triage

**Priority 1 (urgent review):**

- ESD > 75th percentile (many claims per evidence)
- SCS = 0 (no limitations)
- RIS < 25th percentile (poor infrastructure)
- Any metric = 0 or inf (extraction issue or critical concern)

**Priority 2 (moderate review):**

- TCI < 0.5 (sparse methods)
- RTI < 25th percentile (low triangulation)
- FCS < 25th percentile (poor FAIR compliance)

**Priority 3 (exemplars for learning):**

- All metrics > 75th percentile
- FCS = 15, RIS ≥ 6, PGCS ≥ 7 (exemplary infrastructure)

---

## Calibration and Validation

### Current Status: Uncalibrated, Unvalidated

These metrics are **exploratory instruments** for iterative refinement. They have not been:

- Validated against expert quality assessments
- Calibrated with empirical thresholds
- Tested for inter-rater reliability
- Evaluated for construct validity

### Validation Approach

**Phase 2: Domain expert validation**

- Review scorecards across initial corpus
- Identify mis-assessments or problematic metrics
- Calibrate thresholds based on domain expertise

**Phase 3: External validation**

- Test metrics on larger corpus (50-100 papers)
- Compare with existing credibility assessment frameworks
- Statistical validation (correlations, reliability)

**Phase 4: Domain expansion**

- Test on diverse genres (theoretical, computational, experimental)
- Identify genre-specific biases
- Develop genre-specific benchmarks

### Thresholds Needing Calibration

**TCI expected values:**

- Current: 2 RD, 5 methods, 8 protocols (arbitrary)
- Needed: Domain-specific benchmarks or corpus-relative (e.g., mean ± 1 SD)

**SCS limitations count:**

- Current: Count all limitations equally
- Needed: Weight by severity, distinguish resolved vs unresolved

**RIS component weights:**

- Current: Dataset PIDs (2 pts), Data statement (1 pt), etc. (arbitrary)
- Needed: Evidence-based weights (which components most predict replicability?)

**MDD character thresholds:**

- Current: None (raw mean)
- Needed: Benchmarks (e.g., 150 chars = sufficient for replication?)

---

## Recommendations for Use

### Do

✅ Use metrics **together** as complementary indicators

✅ Compare papers **within corpus** using percentiles

✅ Flag papers for **qualitative review** (don't use metrics as final judgement)

✅ Account for **genre and temporal biases** when interpreting

✅ Treat scores as **hypotheses to test**, not verdicts

✅ Review actual extracted content when scores seem anomalous

✅ Document limitations and caveats when reporting metrics

### Don't

❌ Use any single metric as sole criterion for quality

❌ Compare papers from different genres/domains without adjustments

❌ Compare papers from different time periods (pre/post-2015 FAIR norms)

❌ Assume higher scores always mean better research

❌ Ignore extraction quality issues when interpreting scores

❌ Report metrics without confidence intervals or percentiles

❌ Use metrics as targets for authors (Campbell's Law risk)

---

## Future Development

### Near-Term

1. Add percentile calculations to scorecards
2. Identify problematic metrics based on user validation (especially SCS)
3. Refine extraction guidelines to improve consistency
4. Document genre-specific patterns observed in corpora

### Medium-Term

1. Expand corpus to 50-100 papers across diverse genres/domains
2. Statistical validation against expert assessments
3. Inter-rater reliability testing (multiple extractors)
4. Develop genre-specific benchmarks (theoretical vs empirical)
5. Implement adaptive thresholds (corpus-relative or evidence-based)

### Long-Term

1. Quality-weighted metrics (incorporate evidence strength, not just counts)
2. Machine learning calibration (learn optimal weights from validated data)
3. Integration with qualitative rubrics (hybrid scores)
4. Automated extraction (reduce human extraction variability)
5. Public benchmark corpus (high-quality papers for calibration)

---

## Quick Reference Table

| Metric | Scale | Direction | What It Measures | Primary Use |
|--------|-------|-----------|------------------|-------------|
| **ESD** | Ratio | ↓ Lower better | Claims:Evidence ratio | Flag under-supported claims |
| **TCI** | 0-1 | ↑ Higher better | RDMAP coverage | Flag sparse methods |
| **SCS** | Count | ↑ Higher better* | Limitations count | Flag no-limitation papers |
| **RTI** | 0-3+ | ↑ Higher better | Evidence diversity | Flag mono-method papers |
| **RIS** | 0-10 | ↑ Higher better | Replicability infrastructure | Flag poor data/code sharing |
| **PGCS** | 0-10 | ↑ Higher better | PID connectivity | Flag isolated PIDs |
| **FCS** | 0-15 | ↑ Higher better | FAIR compliance | Flag poor open science |
| **MDD** | Chars | ↑ Higher better | Methods detail | Flag sparse documentation |

*SCS caveat: Higher count doesn't always mean better quality

---

## References

- **FAIR Principles**: Wilkinson et al. (2016). *The FAIR Guiding Principles for scientific data management and stewardship.* Scientific Data, 3, 160018.
- **Shannon Diversity**: Shannon, C. E. (1948). *A mathematical theory of communication.* Bell System Technical Journal, 27(3), 379-423.
- **Campbell's Law**: Campbell, D. T. (1979). *Assessing the impact of planned social change.* Evaluation and Program Planning, 2(1), 67-90.

---

**End of Metrics Reference Guide**
