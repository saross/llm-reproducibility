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
