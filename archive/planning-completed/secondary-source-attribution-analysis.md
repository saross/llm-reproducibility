# Secondary Source Attribution and Role Classification - Analysis

**Date:** 2025-10-31
**Status:** Brainstorming / Requirements Analysis
**Context:** Post-10-extraction reflection on citation role tracking needs
**Priority:** DEFERRED until Phase 2 assessment framework defines requirements

---

## Overview

This document explores the challenge of systematically tracking the role and provenance of secondary sources (citations to previous work) in extracted research papers. Current extraction captures citations within verbatim_quote fields but doesn't distinguish their argumentative or evidential role.

**Key Question:** How do we categorize and track citations to enable assessment of transparency, novelty, and evidence chain integrity?

---

## Observations from Recent Extractions

Citation patterns vary substantially by paper type:

### 1. Methodological Papers (e.g., Ross & Ballsun-Stanton 2022)
- Heavy citation load building argumentative claims
- Literature evidence used to support methodological arguments
- Citations often function as "here's the problem others identified"
- Cited claims become evidence for meta-level arguments

### 2. Empirical Papers (e.g., Penske et al. 2023, Connor et al. 2013)
- **Method provenance:** "qpAdm (Haak et al. 2015)"
- **Comparative evidence:** "Our pollen assemblages differ from those reported by Smith (2018)"
- **Interpretive context:** "This pattern is consistent with regional climate shifts (Jones et al. 2020)"
- Mix of primary data generation and secondary source comparison

### 3. Literary/Theoretical Papers (e.g., Ross 2005)
- Engaging with scholarly interpretations
- Citations as claims being argued against
- "Smith (1995) argues X, but the textual evidence suggests Y"
- Citation discourse is the primary content

---

## Practical Taxonomy (Draft)

### For Evidence Items

**Proposed field:** `source_type`

**Values:**
- **`primary`** - Generated/collected by current paper (measurements, observations, new data)
- **`secondary`** - Results cited from other papers used as evidence
- **`hybrid`** - Re-analysis of published data (e.g., existing databases, repositories)

**Examples:**
- **PRIMARY:** "We obtained 47 new radiocarbon dates from the site"
- **SECONDARY:** "Previous excavations yielded dates of 4500-4200 BCE (Smith 2018)" [used as comparative evidence]
- **HYBRID:** "Re-analysis of published genetic data (1000 Genomes Project) using updated methods"

**Extraction guidance:**
- Clear when paper states "we measured/observed/collected"
- Clear when citing published results for comparison
- Ambiguous when synthesising multiple sources

---

### For Claims

**Proposed field:** `claim_origin`

**Values:**
- **`novel`** - New interpretation/conclusion from current paper
- **`tested`** - Claim from literature being evaluated/challenged
- **`supported`** - Claim from literature being corroborated by new evidence
- **`synthesised`** - Integration of current findings + cited work

**Examples:**
- **NOVEL:** "Our results indicate early contact between farming and pastoralist populations by 4500 BCE"
- **TESTED:** "Contrary to Smith's (2015) claim of genetic isolation, we find evidence of admixture"
- **SUPPORTED:** "As proposed by Jones (2018), the pollen data confirm regional deforestation"
- **SYNTHESISED:** "Combining our dates with those of Brown (2019), the transition spans 300 years"

**Extraction guidance:**
- Novel: Paper makes claim without explicit citation support
- Tested: Paper explicitly frames as evaluating/challenging prior claim
- Supported: Paper explicitly frames as confirming prior claim
- Synthesised: Paper combines current + cited work into new claim

**Ambiguity:** Many claims are simultaneously novel AND synthesised - may need multiple tags or confidence scores.

---

### For Methods/Protocols

**Proposed field:** `method_provenance`

**Values:**
- **`original`** - Developed in current paper
- **`adapted`** - Modified from cited work (need to extract what was modified)
- **`standard`** - Direct application of established method with citation
- **comparative** - Multiple methods compared

**Examples:**
- **ORIGINAL:** "We developed a new Bayesian model for..."
- **ADAPTED:** "Modified the qpAdm approach of Haak et al. (2015) by adding..."
- **STANDARD:** "Pollen extracted following Faegri & Iversen (1989)"
- **COMPARATIVE:** "We compared results from three dating methods (Smith 2010, Jones 2012, Brown 2015)"

**Extraction guidance:**
- Original: Paper states "we developed/designed"
- Adapted: Paper states "modified from" or "following X with changes"
- Standard: Direct citation without modification notes
- Comparative: Multiple methods explicitly compared

**Transparency implication:** Adapted methods should document what changed - this is critical for replicability.

---

## Assessment Dimensions This Would Enable

### 1. Transparency Assessment

**Questions:**
- Does the paper clearly distinguish new claims from cited claims?
- Is evidence provenance clear (primary vs secondary)?
- Are methods properly attributed?

**Potential Metrics:**
- % of claims with clear origin attribution
- % of evidence marked as primary vs secondary
- Citation transparency score (clarity of source roles)

**Assessment value:** HIGH - directly relates to transparency and replicability evaluation

---

### 2. Novelty/Contribution Assessment

**Questions:**
- What proportion of claims are genuinely novel?
- How much depends on re-interpretation vs new data?
- Is the paper primarily synthesis or primary research?

**Potential Metrics:**
- Novel claims / total claims
- Primary evidence / total evidence
- Ratio of novel to tested/supported claims

**Assessment value:** MEDIUM - useful for understanding research contribution type, but requires disciplinary context (synthesis papers can be highly valuable)

---

### 3. Evidence Chain Integrity

**Questions:**
- Can you trace claims back to primary sources?
- How many citation hops to primary evidence?
- Are secondary sources used appropriately?

**Potential Metrics:**
- Citation depth (hops to primary source)
- Proportion of claims supported by primary (not secondary) evidence
- Misattribution risk (secondary sources treated as primary)

**Assessment value:** HIGH - critical for credibility assessment in fields where "citation of citations" can propagate errors

---

### 4. Citational Practice Quality

**Questions:**
- Are citations used accurately for their stated role?
- Is there citation inflation (unnecessary citations)?
- Are key sources missing?

**Potential Metrics:**
- Citation role accuracy (if verifiable)
- Citation necessity (background vs essential)
- Key source identification (domain expert validation)

**Assessment value:** UNCERTAIN - requires domain expertise to validate, may be beyond scope of automated extraction

---

## Practical Extraction Challenges

### Challenge 1: Synthesis Claims Are Very Common

**Example:**
> "Our dates (4500-4200 BCE) align with those from nearby sites (Smith 2018: 4400-4100 BCE), suggesting regional synchronicity"

**Issue:** Is this novel, supported, or synthesised? It's all three!
- Novel interpretation of synchronicity
- Supported by cited dates from Smith
- Synthesised from current + cited evidence

**Resolution options:**
- Allow multiple role tags
- Primary + secondary role assignment
- Confidence scores for each role

---

### Challenge 2: Implicit vs Explicit Attribution

**Examples:**
- "The genetic data show admixture" - Novel claim based on primary evidence? Or restating consensus?
- "Genetic admixture is evident" - Could be novel OR citing established view
- Context required, often subtle

**Issue:** Same phrasing can indicate different citation relationships depending on context.

**Resolution options:**
- Default to explicit attribution only (conservative)
- Use surrounding context (more inference)
- Flag ambiguous cases for manual review

---

### Challenge 3: Method Citation Chains

**Example:**
> "We used qpAdm (Haak 2015) implemented in ADMIXTOOLS (Patterson 2012) with parameters from Lazaridis (2016)"

**Issue:**
- Is this standard or adapted?
- Multiple sources to track (software, algorithm, parameters)
- What level of granularity matters for assessment?

**Resolution options:**
- Track primary method source only (qpAdm → Haak 2015)
- Track all sources in chain (3 citations)
- Separate software citation from method citation

---

### Challenge 4: Background vs Evidence Citations

**Example:**
> "Climate change occurred during this period (Smith 2015, Jones 2017, Brown 2019)"

**Issue:**
- Is this evidence supporting a claim?
- Or background context establishing setting?
- Role depends on argumentative structure

**Resolution options:**
- Distinguish "background" from "evidence" citation roles
- Track position in paper (intro = background, results/discussion = evidence)
- Extract based on explicit argumentative framing only

---

## Proposed Implementation Pathway

### Phase 1: Simple Addition (Low Complexity)

**What:** Add optional fields to existing schema

**Schema changes:**
```json
{
  "evidence_id": "E001",
  "evidence_type": "quantitative_data",
  "source_type": "primary",  // NEW: primary/secondary/hybrid
  "verbatim_quote": "...",
  "page": 5
}
```

```json
{
  "claim_id": "C001",
  "claim_type": "interpretation",
  "claim_origin": "novel",  // NEW: novel/tested/supported/synthesised
  "verbatim_quote": "...",
  "page": 8
}
```

**Extraction approach:**
- During Pass 1, flag obvious cases (clearly primary evidence, explicitly tested claims)
- Leave ambiguous cases unmarked (field optional)
- No requirement for 100% coverage initially
- Learn from patterns across multiple papers

**Advantages:**
- Low extraction burden
- Minimal schema disruption
- Enables learning before committing to complex structure

**Disadvantages:**
- Incomplete coverage
- No structured citation metadata
- Limited provenance tracking

**Estimated effort:**
- Schema update: 1 hour
- Prompt update: 2 hours
- Testing on 3 papers: 3-4 hours
- **Total: 6-7 hours**

---

### Phase 2: Structured Citation Metadata (Medium Complexity)

**What:** Add structured tracking of cited claims and evidence

**Schema changes:**
```json
{
  "claim_id": "C001",
  "claim_origin": "tested",
  "cited_claim": {
    "source": "Smith 2015",
    "claim_text": "genetic isolation throughout Copper Age",
    "relationship": "contradicted_by_current_evidence",
    "page": 8
  },
  "verbatim_quote": "...",
  "page": 8
}
```

**Relationship types:**
- `supports_claim` - Citation supports current paper's claim
- `contradicted_by_current_evidence` - Claim being challenged
- `corroborated_by_current_evidence` - Claim being supported
- `method_source` - Citation for method used
- `comparative_data` - Cited data for comparison
- `background_context` - General context setting

**Advantages:**
- Explicit citation role tracking
- Enables assessment of citation accuracy
- Supports evidence chain analysis

**Disadvantages:**
- Higher extraction burden
- Requires careful reading of citation context
- Ambiguity in relationship assignment

**Estimated effort:**
- Schema design: 3 hours
- Prompt development: 4-5 hours
- Testing on 5 papers: 8-10 hours
- **Total: 15-18 hours**

---

### Phase 3: Full Provenance Tracking (High Complexity)

**What:** Track evidence chains across papers, potentially to primary sources

**Schema changes:**
```json
{
  "evidence_id": "E001",
  "source_type": "secondary",
  "cited_evidence": {
    "source_paper": "Jones 2018",
    "evidence_type": "radiocarbon_dates",
    "primary_source": "Jones 2018",  // Could trace further back
    "doi": "10.1234/example",
    "data_availability": "published_supplementary",
    "reliability_flags": ["peer_reviewed", "data_available", "methods_documented"]
  },
  "verbatim_quote": "...",
  "page": 5
}
```

**Advantages:**
- Complete provenance tracking
- Enables deep evidence chain analysis
- Supports data availability assessment

**Disadvantages:**
- Very high extraction burden
- May require external data sources (DOI lookup, citation graphs)
- Uncertain value until assessment framework defined

**Estimated effort:**
- Schema design: 5-6 hours
- External API integration (if needed): 8-10 hours
- Prompt development: 6-8 hours
- Testing on 5-10 papers: 15-20 hours
- **Total: 34-44 hours**

---

## Assessment-Driven Decision Points

Before implementing any phase, answer these questions:

### 1. What Specific Assessment Goals Require This?

**Possible goals:**
- RepliCATS-style credibility scoring incorporating citation transparency
- Transparency tier assignment requiring evidence provenance clarity
- Evidence strength weighting distinguishing primary from secondary sources
- Novelty scoring for research contribution assessment

**Decision:** Don't implement until specific assessment goal identified

---

### 2. What's the Extraction Burden vs Assessment Value?

**Trade-off analysis:**

| Feature | Extraction Burden | Assessment Value | Recommendation |
|---------|------------------|------------------|----------------|
| Simple source_type field | Low | Moderate | Test first |
| Citation relationship tracking | Medium | High (if needed) | Defer until assessment design |
| Full provenance chains | High | Uncertain | Defer indefinitely |

---

### 3. How Do We Handle Ambiguity?

**Options:**

**Option A: Conservative (explicit only)**
- Only code what's clearly stated
- Leave ambiguous cases unmarked
- Accept incomplete coverage

**Option B: Inference-based**
- Use context to infer roles
- Higher coverage but lower confidence
- Requires validation

**Option C: Multi-valued**
- Allow multiple role tags (e.g., "novel" AND "synthesised")
- Captures complexity but complicates analysis
- May need weighting or primary/secondary designation

**Option D: Confidence scores**
- Assign confidence to each role assignment
- Enables downstream filtering
- Adds complexity to extraction

**Recommendation:** Start with Option A (conservative), expand if assessment needs justify it

---

### 4. Testing Approach Before Full Implementation

**Proposed pilot:**

1. **Select 2-3 completed extractions** with different citation profiles:
   - Methodological paper (heavy argumentation, cited claims)
   - Empirical paper (mix of primary data + comparative citations)
   - Review/synthesis paper (primarily secondary sources)

2. **Manual coding exercise:**
   - Code 10-15 claims per paper for `claim_origin`
   - Code 10-15 evidence items per paper for `source_type`
   - Document time required
   - Track ambiguous cases

3. **Ambiguity analysis:**
   - What % of items are clearly categorisable?
   - What % require inference or context?
   - What patterns emerge for ambiguous cases?
   - Can we develop resolution heuristics?

4. **Assessment value test:**
   - Calculate proposed metrics (e.g., % primary evidence, % novel claims)
   - Do these metrics reveal anything useful about paper quality/transparency?
   - How would these feed into assessment framework?

5. **Decision point:**
   - If categorisation is straightforward and metrics are useful → proceed with Phase 1
   - If categorisation is difficult or metrics unclear value → defer until assessment needs clarify
   - If only certain item types are useful (e.g., evidence source_type but not claim_origin) → implement selectively

**Estimated pilot effort:** 4-6 hours

---

## Key Question to Answer First

**What would you DO with this information in your assessment framework?**

**If the answer is:**
- "Compare transparency of primary vs secondary source attribution" → Worth pursuing
- "Weight claims by novelty in contribution assessment" → Worth pursuing
- "Track evidence chains to evaluate credibility" → Worth pursuing (but define how first)
- "Nice to have but not sure how to use it" → Defer until assessment goals crystallise

---

## Empirical Findings from 10-Paper Corpus Analysis (2025-11-02)

**Source:** Cross-paper error analysis of completed extractions
**Papers analysed:** 10 completed assessments (ross-2005 through sobotkova-et-al-2024)
**Finding type:** Observed patterns from systematic quality review

### Citation Pattern Observations

**Pattern 1: Literature Review vs Empirical Misclassification**

**Frequency:** 6 instances across 4 papers (sobotkova-et-al-2023, connor-et-al-2013, penske-et-al-2023, sobotkova-et-al-2024)

**Description:** Claims citing prior work categorised as "empirical" rather than "theoretical" when paper presents no new evidence for the claim.

**Examples:**

**Case 1 - sobotkova-et-al-2023 C018:**
- Claim text: "Volunteers often lack GIS skills necessary"
- Citations: (Elwood 2008, Jones 2012)
- Extracted as: `claim_type = "empirical"`
- Should be: `claim_type = "theoretical"` (literature review, not TRAP project finding)
- Pattern: Literature statement presented as if it were an empirical finding from the paper
- Impact: Misrepresents evidence basis (makes literature synthesis appear as primary research)

**Case 2 - connor-et-al-2013 C096:**
- Claim text: "Pollen source-area of large sites dominated by regional component (Jacobson & Bradshaw 1981)"
- Extracted as: `claim_type = "methodological"`
- Should be: `claim_type = "theoretical"` (established theory, not Connor finding)
- Pattern: Established theoretical framework presented as paper's methodological contribution
- Impact: Confuses application of existing theory with novel methodological development

**Diagnostic triggers for literature review (theoretical):**
- "Literature indicates...", "Prior work shows...", "Research suggests..."
- "(Citation YYYY)" without "our data/study/analysis/results"
- "It is known that...", "Studies have shown..."

**Diagnostic triggers for empirical (this paper's findings):**
- "Our results show...", "We observed...", "Measurements indicate..."
- "Our radiocarbon dates...", "Our survey found...", "Analysis revealed..."
- "The data show..." (in context of paper's own data)

**Pattern 2: Citation Role Ambiguity**

**Observation:** Same phrasing can indicate different citation relationships depending on context.

**Ambiguous patterns identified:**
- "The genetic data show admixture" - Could be novel claim OR restating consensus
- "Genetic admixture is evident" - Novel interpretation OR literature synthesis?
- "Standard procedures were followed" - Method provenance OR assumed knowledge?

**Disambiguation requirement:** Checking for explicit citations, section context (Methods vs Results vs Discussion), relationship to paper's empirical work.

**Finding:** Without clear decision rules, extraction varies based on context reading and can be inconsistent across papers.

**Pattern 3: Method Provenance Citations**

**Observation:** Heavy use of method citations in empirical papers without clear documentation of adaptations.

**Examples from corpus:**
- "qpAdm (Haak et al. 2015)" - Standard application or adapted?
- "Following Faegri & Iversen (1989)" - Exact replication or modified?
- "FAIMS Mobile platform" - Original development, customisation, or standard use?

**Current extraction practice:** Method citations extracted in verbatim_quote field but provenance status (original/adapted/standard) not systematically tracked.

**Implication:** Cannot distinguish methodological innovation from standard application without additional categorisation.

**Pattern 4: Misattribution (Source of Statement)**

**Frequency:** 2 instances identified (overlaps with Pattern 1)

**Cases:**
- **sobotkova-et-al-2023 C018:** Literature statement attributed as paper's empirical finding
- **connor-et-al-2013 C096:** Established theory attributed as paper's methodological finding

**Root cause:** Source of statement (paper vs literature) not clearly distinguished during extraction. Closely related to empirical vs theoretical categorisation errors.

**Finding:** Misattribution and categorisation errors are two facets of same underlying issue - insufficient guidance on distinguishing paper's contributions from cited work.

### Distribution by Paper Type

**Methodological papers (ross-ballsun-stanton-2022):**
- Heavy citation load building argumentative claims
- Literature evidence used to support meta-level arguments about methodology
- Citations function as "problem statements" (what others identified)
- Pattern: Cited claims often become evidence for current paper's meta-level claims
- **No categorisation errors observed** - methodological papers appear easier to extract correctly

**Empirical papers (penske-et-al-2023, connor-et-al-2013, sobotkova-et-al-2023/2024):**
- Mix of primary data generation + secondary source comparison
- Method provenance citations frequent ("using X method from Y paper")
- Comparative evidence from literature ("our results differ from Smith 2018")
- Interpretive context from prior work
- **Higher error rate:** 6 categorisation errors across 4 empirical papers
- **Vulnerability:** Literature review sections easily confused with empirical findings

**Literary/theoretical papers (ross-2005, eftimoski-2017):**
- Citation discourse is primary content
- Engaging with scholarly interpretations as main activity
- Clear distinction between "what text says" (primary source) and "what scholars argue" (secondary source)
- **No misclassification errors observed** - clearer distinction in this domain
- **Success factor:** Primary sources (ancient texts) clearly distinguished from secondary sources (scholarly interpretations)

### Corpus Statistics

- **Total secondary source attribution errors:** 6 instances (2.6% of total 230 errors across all papers)
- **Papers affected:** 4 of 10 (40%)
- **Error type distribution:**
  - Empirical vs theoretical misclassification: 6 instances
  - Misattribution (source of statement): 2 instances (overlap with above)
- **Error severity:** Moderate (categorisation refinement, not critical accuracy issue)
- **Error preventability:** High (decision tree in prompts would prevent 100% per cross-paper analysis)

**Distribution across extractions:**
- sobotkova-et-al-2023: 1 error (C018)
- connor-et-al-2013: 1 error (C096)
- penske-et-al-2023: 8 claims flagged for background_synthesis reclassification
- sobotkova-et-al-2024: Schema inconsistency noted (related to field naming, not categorisation)

**Error concentration:** Penske-et-al-2023 accounts for 8 of 6 distinct errors (some may be the same underlying pattern identified multiple times).

### Implications for Taxonomy Design

**Finding 1: Simple binary (primary/secondary) insufficient for all use cases**

Secondary sources serve multiple distinct roles in empirical papers:
- **Background context** (not evidence or claims, just framing)
- **Comparative evidence** (cited results used to compare with paper's findings)
- **Method provenance** (citation for method used, not evidence or claims)
- **Theoretical framing** (claims being tested/supported/challenged)
- **Literature synthesis** (overview of field, not paper's contribution)

**Implication:** Single "secondary source" flag doesn't capture functional diversity.

**Finding 2: Empirical vs theoretical distinction most critical for accuracy**

Cross-paper errors concentrated in:
- Distinguishing paper's empirical findings from literature review statements
- NOT in tracking citation chains or deep provenance
- NOT in method provenance (though under-documented, not causing errors)

**Implication:** Priority should be clear rules for "is this claim from THIS paper or from cited work?"

**Finding 3: Decision tree more effective than complex taxonomy**

**Evidence from Recommendation 9 in cross-paper analysis:**
- Simple decision tree ("Does THIS paper present NEW evidence?") would prevent 100% of observed errors
- Complexity of provenance tracking not required for current error types
- Clear criteria beat elaborate categorisation schemes

**Recommendation:** If implementing secondary source tracking, prioritise `claim_origin` field (novel/tested/supported/synthesised) over complex provenance chains.

### Observed Citation Roles (from corpus examples)

**Role 1: Method provenance** (frequent in empirical papers)
- "qpAdm (Haak et al. 2015)"
- "Following Faegri & Iversen (1989)"
- Extraction: Currently in verbatim_quote, no provenance categorisation

**Role 2: Comparative baseline** (common in results/discussion)
- "Our dates (4500-4200 BCE) differ from Smith (2018: 4400-4100 BCE)"
- "Contrary to Smith's (2015) claim of genetic isolation, we find admixture"
- Extraction: Paper's finding is empirical, cited work is comparison context

**Role 3: Literature synthesis** (common in introduction/background)
- "Volunteers often lack GIS skills (Elwood 2008, Jones 2012)"
- "Prior research indicates X"
- Extraction: Should be theoretical, NOT empirical (error pattern observed)

**Role 4: Theoretical framework** (common in methods/background)
- "Pollen source-area dominated by regional component (Jacobson & Bradshaw 1981)"
- "Bayesian chronological modelling (Bronk Ramsey 2009)"
- Extraction: Should be theoretical or methodological context, NOT empirical finding

**Role 5: Methodological background** (not evidence)
- "Standard archaeological survey methods"
- "Established GIS procedures"
- Extraction: Goes to project_metadata or implicit RDMAP, not claims/evidence

### Updated Section 6 Implementation Status

**Original plan (2025-10-31):** Deferred until Phase 2 assessment framework

**Corpus evidence supports:**

**Simple addition (Phase 1 - low complexity):**
- `claim_origin` field with 4 values: novel/tested/supported/synthesised
- Decision tree in prompts for empirical vs theoretical distinction
- **Would prevent:** 100% of observed categorisation errors (6 instances)
- **Effort:** 1 hour prompt update + 2 hour schema addition = 3 hours
- **Assessment value:** Enables novelty/contribution analysis, improves categorisation accuracy

**NOT supported by corpus evidence:**
- Complex provenance tracking (not causing errors)
- Citation chain tracing (not required for current use cases)
- Full secondary source taxonomy (complexity not justified by error patterns)

**Recommendation remains:** Defer full implementation until assessment needs clarify, BUT simple categorisation field (`claim_origin`: novel/tested/supported/synthesised) would:
1. Prevent all observed categorisation errors
2. Enable basic novelty assessment
3. Require minimal extraction burden
4. Provide data for future assessment framework design

**Decision point:** Implement simple `claim_origin` field NOW (prevents errors) or wait until assessment framework defines full requirements?

**Next review:** During Phase 2 assessment framework design (Months 3-4 of CWTS fellowship)

---

## Recommended Next Steps

1. **Defer implementation** until Phase 2 assessment framework development
2. **During assessment framework design**, consider:
   - Does transparency assessment require evidence provenance?
   - Does credibility scoring weight primary vs secondary sources differently?
   - Do we need to trace citation chains?
3. **If assessment needs emerge**, run pilot study (4-6 hours)
4. **Based on pilot results**, decide on implementation phase (1, 2, or 3)

---

## Open Questions

1. **Disciplinary variation:** Do citation practices differ enough across disciplines that we need field-specific taxonomies?

2. **Grey literature and unpublished sources:** How do we categorise citations to datasets, reports, theses, conference abstracts?

3. **Temporal dimension:** Does citation recency matter? (Recent citation to primary source vs dated secondary interpretation)

4. **Citation completeness:** Should we flag when key citations appear missing? (Requires domain knowledge)

5. **Self-citation:** Does author self-citation affect credibility assessment differently?

6. **Citation accuracy:** Can/should we verify that cited sources actually support the claims attributed to them? (Very high effort)

---

## Related Documentation

- **Active task:** `planning/active-todo-list.md` Section 6 (Deferred/Future Projects)
- **Schema documentation:** `extraction-system/schema/extraction_schema.json`
- **Assessment framework:** TBD (Phase 2)

---

**Status:** Analysis complete, awaiting assessment framework requirements to determine implementation priority.

**Next review:** During Phase 2 assessment framework design (planned for Months 3-4 of CWTS fellowship)
