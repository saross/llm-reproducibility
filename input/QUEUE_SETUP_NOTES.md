# Extraction Queue Setup - Multi-Paper Testing

**Date:** 2025-10-28
**Purpose:** Test extraction workflow on diverse corpus of 8 papers

---

## Archive Status

**RUN-08 archived successfully:**
- Location: `archive/output/cc-sonnet45/sobotkova-et-al-2023-RUN-08/`
- Contents: Complete extraction (159 items) with all scripts, reports, and analysis
- Status: Production-ready baseline for comparison

---

## Queue Configuration

**Total papers queued:** 8 papers (all status: pending)

**Note:** Source PDFs are excluded from git tracking (copyright and storage concerns). Papers are available locally in `input/sources/original-pdf/` but not committed to repository. Queue configuration and paper metadata are tracked in `queue.yaml`.

### Paper 1: sobotkova-et-al-2023 (RE-RUN)
**Purpose:** Test run-to-run variation

**Previous run:** RUN-08 (archived)
- 159 items total
- 53 evidence, 61 claims, 16 implicit_arguments
- 4 designs, 8 methods, 17 protocols
- Ranked #3 of 7 runs (total items)
- Ranked #2 of 7 runs (RDMAP coverage)

**Testing goal:** Assess consistency of extraction workflow across independent runs of same paper.

---

## New Papers - Diverse Corpus (7 papers)

### By Domain

**Archaeology & Landscape (4 papers):**
1. **sobotkova-et-al-2024** - Predictive modelling validation
2. **sobotkova-et-al-2021** - Mobile GIS deployment
3. **eftimoski-et-al-2017** - Land use change analysis
4. **ross-et-al-2009** - Remote sensing methodology

**Environmental Science (1 paper):**
5. **connor-et-al-2013** - Palaeoenvironmental reconstruction

**Prehistoric Archaeology (1 paper):**
6. **penske-et-al-2023** - Archaeological evidence synthesis

**Ancient History/Philology (1 paper):**
7. **ross-2005** - Literary analysis (Homer's Iliad)

---

## Paper Characteristics - Diversity Testing

### File Sizes
- **Smallest:** ross-2005 (166K) - Single-author philology paper
- **Largest:** penske-et-al-2023 (13M) - Multi-author archaeological synthesis
- **Range:** 166K to 13M (78x variation)

### Methodological Diversity

**Quantitative/Technical:**
- sobotkova-et-al-2024 (predictive modelling)
- sobotkova-et-al-2021, sobotkova-et-al-2023 (system implementation)
- ross-et-al-2009 (remote sensing)

**Environmental/Proxy Data:**
- connor-et-al-2013 (palaeoenvironmental reconstruction)

**Qualitative/Interpretive:**
- eftimoski-et-al-2017 (landscape analysis)
- penske-et-al-2023 (archaeological synthesis)
- ross-2005 (literary/historical interpretation)

### Expected Transparency Levels

**High transparency (technical papers):**
- sobotkova-et-al-2023, sobotkova-et-al-2021, sobotkova-et-al-2024
- ross-et-al-2009
- Expected: High RDMAP coverage, minimal implicit items

**Medium transparency:**
- eftimoski-et-al-2017
- connor-et-al-2013
- penske-et-al-2023
- Expected: Moderate RDMAP, some implicit methods/protocols

**Lower transparency (interpretive):**
- ross-2005 (literary analysis)
- Expected: Lower RDMAP, higher implicit arguments, qualitative evidence

---

## Testing Priorities

### 1. Run-to-Run Variation (High Priority)
**Paper:** sobotkova-et-al-2023
**Compare:** New extraction vs RUN-08
**Metrics:**
- Total item count consistency
- Category distribution (evidence, claims, RDMAP)
- Relationship mapping completeness
- Implicit extraction consistency

**Success criteria:**
- ±10% total items (143-175 items)
- Same claims identified (core findings should match)
- Similar RDMAP structure (same designs/methods identified)

---

### 2. Generalization Across Methods (High Priority)
**Papers:** All 7 new papers
**Goal:** Validate workflow works across diverse methodologies
**Metrics:**
- Successful completion rate
- Quality across transparency levels
- RDMAP extraction appropriateness
- Implicit vs explicit ratio by transparency

**Success criteria:**
- All papers extract successfully
- Relationship mapping >50% for all papers
- RDMAP hierarchy present (designs→methods→protocols)

---

### 3. Transparency Level Handling (Medium Priority)
**Papers:** Compare high (sobotkova-et-al-2023) vs medium (eftimoski-et-al-2017) vs low (ross-2005)
**Metrics:**
- Explicit vs implicit RDMAP ratio
- Implicit argument counts
- Expected information flagging

**Success criteria:**
- Lower transparency → higher implicit extraction
- Appropriate "expected information missing" flags
- Quality maintained regardless of transparency

---

### 4. Domain Transfer (Medium Priority)
**Papers:** Cross-domain comparison
**Goal:** Ensure extraction works for environmental science and ancient history
**Metrics:**
- Evidence types appropriate to domain
- Claim types reflect disciplinary norms
- Implicit arguments capture disciplinary assumptions

**Success criteria:**
- Domain-appropriate extraction (proxy data for connor-et-al-2013, textual evidence for ross-2005)
- Disciplinary assumptions identified correctly
- No method-specific bias (e.g., over-extracting from technical papers)

---

## Execution Strategy

### Recommended Order

**Phase 1: Re-run baseline (1 paper)**
1. sobotkova-et-al-2023 → Compare to RUN-08 immediately

**Phase 2: Technical papers (3 papers)**
2. sobotkova-et-al-2024 (similar methodology to 2023)
3. sobotkova-et-al-2021 (similar methodology to 2023)
4. ross-et-al-2009 (different but still technical)

**Phase 3: Mixed methods (3 papers)**
5. eftimoski-et-al-2017 (landscape analysis)
6. connor-et-al-2013 (environmental reconstruction)
7. penske-et-al-2023 (archaeological synthesis)

**Phase 4: Interpretive (1 paper)**
8. ross-2005 (literary analysis - most different from baseline)

**Rationale:** Progress from similar to different, allowing workflow adjustments between phases if needed.

---

## Expected Challenges

### By Paper

**sobotkova-et-al-2023:**
- Challenge: Maintaining consistency with RUN-08
- Mitigation: Same workflow, same skill version, autonomous execution

**sobotkova-et-al-2024, 2021:**
- Challenge: Very similar papers (same authors, methods, domains)
- Risk: Over-fitting to this paper type
- Mitigation: Compare to ross-et-al-2009 (different technical approach)

**connor-et-al-2013:**
- Challenge: Proxy data interpretation, multi-proxy synthesis
- Risk: Implicit assumptions in proxy-climate relationships
- Mitigation: Look for disciplinary assumptions in implicit_arguments

**penske-et-al-2023:**
- Challenge: Large file (13M), potential for many items
- Risk: Extraction becoming unwieldy
- Mitigation: Monitor item counts, apply conservative rationalization

**ross-2005:**
- Challenge: Literary/historical interpretation, low methods transparency
- Risk: Difficulty extracting RDMAP (minimal "methods" section)
- Mitigation: Accept minimal RDMAP, focus on claims and implicit arguments

---

## Success Metrics - Overall Corpus

### Minimum Success
- ✅ All 8 papers extract to completion
- ✅ Validation passes for all papers
- ✅ Run-to-run variation <20% for sobotkova-et-al-2023

### Good Success
- ✅ Run-to-run variation <10%
- ✅ RDMAP extracted for 6/8 papers (technical + mixed methods)
- ✅ Relationship mapping >50% for 7/8 papers
- ✅ No systematic extraction failures by paper type

### Excellent Success
- ✅ Run-to-run variation <5%
- ✅ RDMAP extracted for all papers (appropriate to transparency)
- ✅ Relationship mapping >60% average
- ✅ Implicit extraction working across transparency levels
- ✅ Quality consistent across domains and methods

---

## Analysis Plan Post-Extraction

### 1. Individual Paper Reports
For each paper:
- extraction.json
- validation-pass6.md
- summary.md

### 2. Comparative Analysis
- Multi-paper comparison (like multi-run-comparison.md)
- Metrics by domain, transparency, file size
- RDMAP coverage analysis
- Implicit vs explicit patterns

### 3. Run-to-Run Variation Report
- Detailed comparison: sobotkova-et-al-2023 (new) vs RUN-08
- Item-by-item matching analysis
- Consistency metrics
- Reliability assessment

### 4. Workflow Validation Report
- Success rate by paper type
- Quality metrics across corpus
- Recommendations for improvements
- Assessment of production-readiness for diverse papers

---

## Next Steps

1. **Begin extractions** - Start with sobotkova-et-al-2023 re-run
2. **Compare to RUN-08** - Immediate assessment of run-to-run variation
3. **Proceed through queue** - Follow recommended order
4. **Generate comparative reports** - After completing all 8
5. **Update workflow if needed** - Based on findings across diverse corpus

---

*Queue setup: 2025-10-28*

*Papers queued: 8 (1 re-run + 7 new)*

*Estimated total extraction time: 16-24 hours (2-3 hours per paper)*
