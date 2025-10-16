# Implementation Plan Supplement
## Strategic Decisions and Context for Extraction Prototype Development

### Prepared for Continuation in New Conversation

This document captures strategic clarifications and methodological decisions established during initial planning discussions that are not yet incorporated into the main CWTS Implementation Plan. These points inform the immediate commencement of extraction prototype development.

---

## Copyright and Access Strategy

Initial corpus development will be restricted to co-authored papers and open access publications to avoid copyright complications during the prototype phase. This constraint applies throughout extraction protocol validation; expansion strategies for subsequent phases will be determined based on institutional data governance requirements and legal counsel where necessary.

## Multilingual Development Pathway

We begin with English-language publications for extraction prototype validation, establishing baseline accuracy benchmarks in a single language before introducing additional complexity. However, there is explicit intention to expand to multilingual papers once English extraction protocols stabilise. This is particularly important for classical archaeology, where German, French, and Italian scholarship constitutes substantial disciplinary contributions. The timeline for multilingual expansion will be determined empirically based on Phase 1 performance metrics.

## Community Engagement Plan

Active involvement with CAA-Australasia (Computer Applications and Quantitative Methods in Archaeology, Australasian chapter) provides opportunity for early disciplinary feedback on work-in-progress. Presenting emerging findings to colleagues within this network complements CWTS metascience validation with domain-specific critique from the archaeological data management community. This engagement strategy plants seeds for broader community acceptance whilst maintaining scope discipline during the fellowship period.

## Publication Strategy for Marginal or Negative Results

I have confirmed commitment to publishing findings regardless of whether LLM-expert correlation achieves optimistic targets. Specific journals committed to open science have been identified that would consider rigorous documentation of automation limitations as valid scholarly contribution. The framing approach for negative results will be developed collaboratively if accuracy benchmarks fall below targets—positioning systematic documentation of failure modes as methodologically valuable for the field.

## CLIO Investigation Decision

Assessment of Anthropic's CLIO system has been completed, yielding the following conclusions:

**Validation of Feasibility**: CLIO demonstrates that large language models can perform semantic extraction at scale whilst preserving contextual complexity—directly addressing the central risk that automated extraction might reduce interpretive scholarship to simplistic categories.

**Domain Transfer Constraints**: Substantial divergence exists between CLIO's conversational domain and scholarly argumentation. Techniques optimised for processing dialogic exchanges may not transfer cleanly to decomposing extended, formal, monologic arguments with complex evidential structures and theoretical scaffolding.

**Strategic Decision**: We defer deep CLIO research at this stage, prioritising empirical validation with actual papers over attempting to preemptively incorporate approaches that may prove unnecessary. The high-level insights (scale is feasible, complexity can be preserved, confidence must be quantified) are already incorporated into the architectural design.

**Contingent Research Trigger**: If Week 3 extraction accuracy falls below 70% precision/recall despite systematic prompt iteration, we will investigate CLIO's specific techniques for reliability enhancement. Additional triggers include persistent evidence-claim relationship mapping failures (<60% accuracy with multi-model consensus) or excessive hallucination rates (>10% of extracted elements unsupported by text).

**Future Integration Pathway**: Should CLIO research prove valuable in later phases, integration would focus on: (1) aggregation methods for identifying cross-paper patterns (Month 4+), (2) confidence calibration refinement if uncertainty quantification proves unreliable, and (3) extraction verification loops if hallucination mitigation requires additional architecture.

## Status and Immediate Priorities

We are now positioned to commence extraction prototype design. The implementation plan document provides comprehensive strategic framework; the next phase focuses on tactical execution:

1. **Corpus selection**: Identifying specific papers balancing disciplinary diversity with validation feasibility
2. **CEM schema formalisation**: Defining node types, edge types, attribute requirements, and provenance tracking mechanisms
3. **Ground truth annotation**: Hand-coding one paper completely to establish validation standard
4. **Prompt architecture development**: Designing multi-turn conversational prompts for claim, evidence, and method extraction
5. **Validation metric specification**: Establishing precision, recall, and F1 targets for different extraction tasks

All preparatory work is complete; we proceed directly to implementation in the next conversation with maximum context window availability.

---

**Document Purpose**: This supplement ensures continuity across conversation boundaries, capturing methodological refinements and strategic clarifications that inform extraction prototype development but are not yet integrated into the formal implementation plan.
