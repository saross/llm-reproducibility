# CWTS Fellowship Implementation Plan
## LLM-Based Credibility Assessment for Humanities and Social Sciences
### September 2025 â€“ February 2026

# CWTS Fellowship Implementation Plan
## LLM-Based Credibility Assessment for Humanities and Social Sciences
### September 2025 â€“ February 2026

## Executive Summary: Strategic Decisions and Implementation Pathway

This revised implementation plan incorporates confirmed strategic assets and methodological decisions that significantly strengthen the project's feasibility:

**Strategic Assets**:
- **Local compute infrastructure**: Access to models up to 120b parameters (GPT-OSS, llama3.3:70b, qwen3-thinking, gemma3) enables cost-effective multi-model consensus development
- **Multidisciplinary domain expertise**: Training and publication record spanning archaeology, ancient history, and collaborative fieldwork projects (geoscience, ecology) provides expert validation capacity across target domains
- **repliCATS data access**: Collaborator's access to ~3,900 claim judgements and 200 paper assessments provides calibration dataset and external validation benchmark
- **CWTS metascience expertise**: Three-week residence provides immediate access to research evaluation specialists for methodological critique
- **Co-authored papers**: Own publications provide ground truth for rapid validation without external recruitment delays

**Implementation Architecture**:
- **Corpus**: Moderately multidisciplinary from outsetâ€”fieldwork-based HASS and environmental sciences (archaeology, ancient history, geoscience, ecology)â€”exploiting shared epistemological characteristics (abductive reasoning, serendipity, non-repeatable phenomena)
- **Model strategy**: Phased approachâ€”Claude prototyping (Weeks 1-3), local multi-model consensus (Weeks 4-6), SOTA integration for assessment (Months 2-6)
- **Validation**: CWTS expert feedback (Weeks 1-3), self-validation via domain expertise (Months 2-4), formal panel (Months 5-6)
- **Development environment**: Web interface for prompt engineering (Weeks 1-3), transition to Claude Code for systematic development (Week 4+)
- **Documentation**: Open research project publishing findings regardless of outcome; rigorous failure analysis as valuable contribution

**Critical Path**: Extraction-first strategy remains essentialâ€”six-month timeline depends entirely on achieving reliable Claim-Evidence-Method graph extraction by Month 2. All subsequent assessment work builds upon this foundation.

## Executive Orientation

You have three key assets to leverage:

1. **Proven methodology**: repliCATS demonstrated 73-84% accuracy using structured human elicitation; your ChatGPT review provides a concrete translation pathway to LLM-assisted implementation
2. **Direct access to validation data**: Your collaborator's repliCATS data gives you ground truth for calibrationâ€”a massive advantage over starting from scratch
3. **Focused domain expertise**: Beginning with archaeology/landscape studies where you have deep disciplinary knowledge enables rapid iteration

The core challenge is not whether this can workâ€”repliCATS proved structured credibility assessment worksâ€”but rather **how to translate human deliberation protocols into reliable LLM-based extraction and assessment whilst preserving the nuance essential to interpretive scholarship**.

## Strategic Architecture: Three Interconnected Layers

### Layer 1: Semantic Extraction (Claim-Evidence-Method Graphs)

**Purpose**: Decompose papers into structured knowledge representations before assessment can begin

**Core Task**: Extract and link:
- **Claims** (typed: empirical vs interpretive; with scope/confidence indicators)
- **Evidence** (material culture, contexts, textual sources, datasets, quantitative data)
- **Methods** (field protocols, sampling strategies, analytical workflows, theoretical frameworks)
- **Limitations** (explicitly stated constraints, acknowledged alternatives)

**Technical Approach**:
- Multi-turn conversational prompting (following Polak & Morgan's ChatExtract pattern)
- Self-verification loops to catch hallucinations
- Provenance tracking (every extracted element links to specific text passages)
- Multi-model consensus where stakes are high

**Critical Dependency**: This layer **must** work reliably before credibility assessment becomes meaningful. Poor extraction â†’ unreliable assessment regardless of scoring sophistication.

### Layer 2: Credibility Assessment (Adapted repliCATS Signals)

**Purpose**: Score research quality on dimensions appropriate to interpretive scholarship

**Seven Signals** (directly adapted from repliCATS Phase 2):

1. **Comprehensibility**: Are claims explicit, bounded, and logically structured?
2. **Transparency**: Is the research design clear (exploratory vs confirmatory); are methods documented?
3. **Plausibility**: Do interpretations cohere with domain knowledge (chronology, regional patterns)?
4. **Validity** (Evidential Adequacy): Are claims supported by sufficient, representative evidence; are alternatives considered?
5. **Robustness**: Would conclusions survive reasonable analytical variations?
6. **Replicability** (as Analytic Reproducibility): Can analytical steps be traced and reproduced?
7. **Generalisability**: Are scope constraints and limitations explicitly acknowledged?

**Technical Approach**:
- Each signal scored by ensemble of LLM agents (3-5 runs with varied seeding)
- Interval estimates (lower bound / best estimate / upper bound) to quantify uncertainty
- Structured justifications with citations to extracted graph elements
- Mathematical aggregation (trimmed means) with calibration against expert panels

### Layer 3: Infrastructure Integration

**Purpose**: Connect assessments to archaeological data ecosystems for automated verification

**Key Integrations**:
- **Repository checks**: Open Context, tDAR, ARIADNE (verify DOIs resolve, metadata completeness)
- **Ontology mapping**: CRMarchaeo for method/context standardisation
- **FAIR/CARE compliance**: Automated scoring for data stewardship dimensions

## Six-Month Phase Structure

### Phase 1: Foundation and Proof-of-Concept (Months 1-2: Sept-Oct 2025)

**Primary Objective**: Demonstrate that LLM-based extraction can reliably produce Claim-Evidence-Method (CEM) graphs for archaeology/landscape papers

**Deliverables**:
1. **Extraction prototype**: Working system that processes 5-10 papers into structured graphs
2. **Validation dataset**: Hand-coded ground truth for 10-15 papers (claims, evidence, methods, relationships)
3. **Accuracy benchmarks**: Precision/recall metrics for extraction against human coding
4. **Schema specification**: Finalised CEM graph structure aligned with CRMarchaeo where relevant

**Critical Activities**:
- Corpus assembly (30-50 open access archaeology/landscape papers, emphasising methodological diversity)
- Intensive prompt engineering for extraction accuracy
- Expert validation panel recruitment (3-5 archaeologists/historians for ongoing consultation)
- Repository infrastructure mapping (which data sources exist and can be machine-checked?)

**Success Criteria**:
- >80% precision/recall on claim extraction (comparable to ChatExtract benchmarks)
- Reliable evidence-claim linking (>70% of relationships correctly identified)
- Provenance tracking functioning (every extracted element traceable to source text)

### Phase 2: Assessment Module Development (Months 3-4: Nov-Dec 2025)

**Primary Objective**: Implement and validate LLM-based scoring for 3-4 core credibility signals

**Deliverables**:
1. **Signal assessors**: Working implementations for Transparency, Validity, Robustness, Generalisability
2. **Ensemble architecture**: Multi-agent scoring with aggregation protocols
3. **Calibration dataset**: Expert panel ratings on same papers for comparison
4. **Inter-rater reliability analysis**: Agreement between LLM ensemble and human experts

**Critical Activities**:
- Adapt repliCATS signal definitions for LLM implementation
- Build expert panel rating interface (structured rubrics mirroring LLM prompts)
- Implement uncertainty quantification (interval estimates, between-agent variance)
- Develop escalation protocols (when does disagreement trigger human review?)

**Success Criteria**:
- Correlation >0.6 between LLM ensemble and expert panel scores
- Calibrated probability estimates (Brier score <0.25 on held-out papers)
- Systematic error analysis identifying failure modes

**Risk**: If LLM-expert correlation is weak, need to diagnose whether problem is extraction layer, assessment prompts, or fundamental limits of automation

### Phase 3: Integration and Validation (Months 5-6: Jan-Feb 2026)

**Primary Objective**: Complete system integration, conduct rigorous validation, produce technical specifications

**Deliverables**:
1. **Full system**: End-to-end pipeline from PDF â†’ CEM graph â†’ credibility scorecard
2. **Validation study**: Performance analysis across 30-50 papers with expert comparison
3. **Technical documentation**: API specifications, deployment requirements, cost models
4. **Research outputs**: Draft manuscripts for JOSS (technical), Digital Scholarship in Humanities (methodological)

**Critical Activities**:
- Implement remaining signals (Comprehensibility, Plausibility, Replicability)
- Add repository integration for automated data availability checking
- Cross-validation with repliCATS data (if your collaborator can provide suitable test cases)
- Error analysis and limitation documentation

**Success Criteria**:
- System processes 50+ papers with consistent output quality
- Published accuracy benchmarks and known limitations
- Clear roadmap for Phase 2 expansion

## Three Viable Starting Points for Immediate Prototyping

### Option A: Extraction-First (RECOMMENDED)

**Focus**: Build robust CEM graph extraction for 5-10 archaeology papers

**Why Start Here**:
- Everything depends on extraction qualityâ€”foundation must be solid
- Fastest path to tangible output you can evaluate
- Lets you validate that archaeological argumentation can be computationally tractured
- Provides concrete artifacts for discussing with CWTS colleagues

**Week 1-2 Tasks**:
1. Select 5 exemplar papers (mix of well-documented and typical)
2. Hand-code one paper completely (create ground truth)
3. Develop initial extraction prompts for claims
4. Iterate on 2-3 papers until extraction is reliable
5. Document failure modes and edge cases

**Validation Approach**:
- Compare automated extraction against your hand-coding
- Calculate precision/recall/F1 scores
- Identify systematic errors (missed claims, hallucinated relationships, context loss)

### Option B: Signal Definition via repliCATS Data

**Focus**: Use your collaborator's repliCATS data to reverse-engineer what signals look like

**Why Start Here**:
- Leverages unique asset (access to validated human judgments)
- Provides ground truth for calibration from day one
- Could accelerate validation by building on proven assessment framework

**Week 1-2 Tasks**:
1. Obtain sample of repliCATS papers with expert ratings
2. Manually code 3-5 papers for the seven signals in archaeology/HASS context
3. Compare your coding with repliCATS structured justifications
4. Identify which signals translate cleanly vs require adaptation
5. Draft signal definitions and scoring rubrics for archaeology

**Risk**: RepliCATS focused on experimental social science; translation to interpretive archaeology may not be straightforward

### Option C: Hybrid Mini-System (5 Papers, 2 Signals)

**Focus**: Build complete but minimal system (extraction + assessment) on tiny corpus

**Why Start Here**:
- Fastest path to end-to-end demonstration
- Reveals integration challenges early
- Creates concrete artifact for feedback from CWTS and collaborators

**Week 1-2 Tasks**:
1. Select 3 papers with known quality issues, 2 exemplars
2. Extract CEM graphs (moderate prompt engineering)
3. Implement Transparency and Validity assessors only
4. Compare LLM scores with your own expert judgment
5. Document where system succeeds and fails

**Risk**: Spreading effort across both layers risks neither working well

## Claude Code Transition Strategy

### Strategic Timing for Claude Code Integration

**Claude Code** offers distinct advantages for systematic code development, file management, and iterative refinementâ€”but introduces overhead that may not be warranted in early prototyping phases. The optimal transition point balances exploration flexibility against development rigour.

### Recommended Transition Points

**Phase 1: Continue with Claude Web Interface (Weeks 1-3)**

*Rationale*:
- Rapid prompt experimentation requires conversational iteration
- Extraction protocol development benefits from immediate feedback loops
- Document viewing and inline annotation support ideation
- No deployment complexity while concepts are fluid

*Activities Well-Suited to Web Interface*:
- Prompt engineering and testing
- Manual validation of extraction outputs
- Schema design discussions
- Conceptual refinement with CWTS colleagues

**Phase 2: Transition to Claude Code (Week 4 / Month 2)**

*Trigger Conditions*:
- Extraction prompts stabilise (>75% accuracy on test cases)
- Multi-model orchestration architecture defined
- Codebase exceeds ~500 lines
- Need for systematic testing infrastructure
- Local model integration begins

*Activities Requiring Claude Code*:
- Building multi-model consensus pipelines
- Implementing provenance tracking database
- Developing automated validation scripts
- Creating reproducible evaluation workflows
- Managing configuration files across models

**Phase 3: Hybrid Approach (Months 3-6)**

*Strategy*:
- Use **Claude Code** for production code development, testing, and debugging
- Return to **web interface** for conceptual discussions, paper analysis, and manuscript drafting
- Leverage web interface for explaining code outputs and design decisions

### Technical Architecture Considerations

**Local Development Environment**:
- Python 3.11+ with virtual environment management
- LangChain or similar for model orchestration
- SQLite for provenance tracking (upgrade to PostgreSQL if scaling)
- Git repository with clear documentation
- Automated testing (pytest) and CI/CD considerations

**Claude Code Advantages for This Project**:
- Systematic management of prompt libraries across models
- Database schema evolution tracking
- Automated extraction validation pipelines
- Integration of local and API-based model calls
- Generation of reproducible analysis scripts

**When Web Interface Remains Superior**:
- Discussing extraction quality issues with example passages
- Iterating on credibility signal definitions
- Interpreting validation results
- Drafting academic papers with inline citations
- Collaborative discussions with CWTS colleagues

### Practical Implementation Pathway

**Week 3 Preparation**:
1. Document current extraction prompts and workflows
2. Define CEM graph schema formally
3. Specify evaluation metrics and testing protocols
4. Prepare corpus data (papers, ground truth annotations)

**Week 4 Claude Code Setup**:
1. Initialize project repository
2. Implement first extraction module with tests
3. Build multi-model orchestration framework
4. Create validation harness

**Ongoing**:
- Develop systematic code in Claude Code
- Return to web for analysis and interpretation
- Use version control to track prompt evolution

### Recommendation

**Transition to Claude Code at the start of Month 2** (Week 4-5), immediately after:
- Completing initial prompt engineering with 5-10 test papers
- Establishing baseline extraction accuracy benchmarks
- Presenting initial findings to CWTS colleagues
- Defining CEM graph schema and validation protocols

This timing allows creative exploration during CWTS residence whilst building rigorous implementation infrastructure for sustained development.

### 1. Corpus Strategy

**Decision**: Moderately multidisciplinary from early prototyping, focused on fieldwork-based HASS and environmental sciences

**Strategic Rationale**: 
- Your multidisciplinary archaeological projects (spanning geoscience, ecology) and ancient history training provide expert validation across domains
- Fieldwork-based disciplines share epistemological characteristics (abductive reasoning, serendipity, unique/non-repeatable phenomena) making them ideal test cases
- Early inclusion of co-authored papers enables rapid iteration with deep contextual knowledge
- Tests generalisability claims immediately whilst maintaining expert evaluation capacity

**Initial Corpus Composition** (5-10 papers for Month 1):
- 3-4 archaeology papers (including 1-2 you co-authored for ground truth validation)
- 2-3 ancient history papers (leveraging your publication record)
- 1-2 environmental fieldwork papers (geoscience, ecology from collaborative projects)

**Expansion Strategy**: Add anthropology and historical studies by Month 3 once extraction protocols are robust

### 2. Model Strategy

**Decision**: Phased multi-model approach leveraging local compute infrastructure

**Phase 1a (Weeks 1-3): Claude Prototyping**
- Develop extraction protocols with Claude Sonnet 4.5 via API (enabling direct prompt engineering collaboration)
- Establish baseline accuracy on 5-10 papers
- Validate extraction architecture before expanding to ensemble

**Phase 1b (Weeks 4-6): Local Multi-Model Validation**
- Implement consensus ensemble using locally hosted models:
  - GPT-OSS:120b (strong general reasoning)
  - qwen3-thinking:30b (explicit reasoning traces)
  - llama3.3:70b (well-calibrated outputs)
  - gemma3:27b (efficient baseline)
- Compare local model consensus against Claude baseline
- Establish cost-performance trade-offs for scaling decisions

**Phase 2 (Months 2-3): SOTA Model Consensus**
- Add frontier models via API for high-stakes assessments:
  - ChatGPT o3 / GPT-5 (when available)
  - Gemini Pro 2.5
- Reserve API calls for final credibility assessment; use local models for iterative extraction refinement

**Strategic Advantages**:
- Dramatically reduced iteration costs (local inference nearly free)
- Rapid experimentation without API rate limits
- Model diversity reveals systematic biases
- Scalable architecture (local for volume, API for accuracy where needed)

**Cost Model**: Estimated â‚¬500-800 for SOTA API calls (assessment phase only) vs â‚¬3,000+ for full API-based pipeline

### 3. Validation Approach

**Decision**: Phased validation leveraging immediate CWTS access followed by formal panel evaluation

**Phase 1 (Weeks 1-3): Rapid CWTS Metascience Feedback**
- **Strategic Window**: Three weeks of in-residence access to CWTS expertise
- **Tactical Use**: Present initial extraction outputs and credibility signal adaptations to metascience researchers
- **Focus**: Methodological soundness, comparison with repliCATS framework, identification of systematic blind spots
- **Format**: Informal presentations, working group discussions, rapid iteration based on expert critique
- **Deliverable**: Refined extraction protocols and signal definitions validated by research evaluation experts

**Phase 2 (Months 2-4): Self-Validation via Domain Expertise**
- Expert evaluation of extraction outputs across archaeology, ancient history, environmental fieldwork domains where you hold specialist knowledge
- Systematic error analysis identifying failure modes
- Iterative prompt refinement based on disciplinary familiarity

**Phase 3 (Months 5-6): Formal Expert Panel Validation**
- Recruit 3-5 disciplinary experts for structured credibility assessment
- Compare LLM ensemble scores against expert panel ratings
- Calculate inter-rater reliability (Gwet's AC1, Kendall's W)
- Calibration analysis (Brier scores, isotonic calibration)

**Rationale**: Frontload methodological validation whilst you have CWTS access, defer resource-intensive disciplinary panel recruitment until system architecture is stable

### 4. repliCATS Data Integration

**Confirmed Asset**: Your collaborator (repliCATS data scientist) has access to:
- ~3,900 claim-level judgements with replication outcomes
- Paper-level credibility signal ratings for 200 papers across 62 journals
- Structured justifications from expert deliberation process

**Strategic Integration Points**:

**Month 2**: Obtain sample of 10-15 social science papers with full repliCATS assessments
- Use as calibration dataset for signal translation
- Compare your archaeology-adapted signal definitions against original repliCATS rubrics
- Identify where disciplinary differences require modified assessment criteria

**Month 4**: Validate LLM assessments against repliCATS ground truth
- Select subset of papers suitable for methodological comparison
- Test whether LLM-based scoring correlates with structured human elicitation
- Benchmark performance: Target correlation >0.6 with repliCATS composite scores

**Month 6**: Incorporate into validation study design
- Use repliCATS data to establish external validity
- Demonstrate that approach generalises across HASS domains
- Position findings relative to proven baseline (repliCATS 73-84% accuracy)

**Action Item**: Contact collaborator immediately to clarify data access protocols, ethics approvals, and usage constraints

### 5. Infrastructure Development Priorities

**Immediate (Months 1-2)**:
- Simple DOI resolution checking (validates data availability claims)
- Local model orchestration infrastructure
- Provenance tracking database (links extracted elements to source text)

**Deferred to Phase 2 (Post-Fellowship)**:
- Complex repository integration (Open Context, tDAR, ARIADNE)
- CRMarchaeo ontology mapping
- FAIR/CARE automated compliance scoring
- Vision model integration for figure/map analysis

**Rationale**: Prioritise core extraction and assessment functionality; demonstrate infrastructure integration pathways through lightweight implementations

## Risk Register and Mitigation Strategies

### High-Impact Risks

**R1: Extraction Accuracy Insufficient**
- *Manifestation*: <70% precision/recall on claims; frequent hallucinations
- *Impact*: Entire credibility assessment layer becomes unreliable
- *Mitigation*: Over-invest in extraction validation; use multi-stage verification prompts; leverage multi-model consensus from Week 4; implement confidence scoring
- *Trigger*: If Month 1 benchmarks miss targets, pause and diagnose before proceeding
- **UPDATED**: Local model capacity enables rapid iteration without cost constraintsâ€”exploit this advantage

**R2: Disciplinary Resistance**
- *Manifestation*: Expert panel or CWTS colleagues view automation as inappropriate reductionism
- *Impact*: Difficulty recruiting validators; negative reception of findings
- *Mitigation*: Frame as augmentation not replacement; emphasise transparency and auditability; involve sceptics early via CWTS presentations
- *Preemptive Action*: Present proposal at CWTS research seminar in Weeks 1-2; solicit critical feedback from metascience experts
- **UPDATED**: Three-week CWTS window provides ideal testing ground for methodological critique

**R3: repliCATS Translation Challenges**
- *Manifestation*: Signals designed for experimental work don't map cleanly to interpretive fieldwork research
- *Impact*: Assessment module lacks validity; unclear evaluation criteria
- *Mitigation*: Co-develop adapted signals with CWTS metascience experts during residence; use repliCATS data for calibration in Month 2
- *Fallback*: Develop fieldwork-specific credibility dimensions de novo (drawing on your manual assessment framework experience)
- **UPDATED**: Direct access to repliCATS data via collaborator reduces translation uncertainty

**R4: Time Fragmentation**
- *Manifestation*: Fellowship period interrupted by competing obligations or scope creep
- *Impact*: Insufficient focused time for deep technical work; incomplete deliverables
- *Mitigation*: Calendar blocking; clear boundaries; resist premature infrastructure integration
- *Opportunity*: ANU masters course next semester may provide RA support for Phase 2 expansion
- **UPDATED**: Good availability during fellowship; maintain scope discipline essential

**R5: Multimodal Evidence Gap**
- *Manifestation*: Credibility assessments miss critical evidence in figures, maps, stratigraphic sections
- *Impact*: Validity and robustness signals systematically under-detect documentation issues
- *Mitigation*: Document limitation explicitly; design Phase 2 vision model integration
- *Strategic Framing*: Position text-only extraction as validated baseline for future multimodal expansion
- **NEW RISK**: Local vision models available but deferredâ€”ensure integration pathway remains tractable

### Medium-Impact Risks

**R6: Validation Panel Recruitment Challenges**
- *Mitigation*: Start recruitment immediately; offer co-authorship; leverage learned society networks

**R7: Prompt Engineering Proves More Difficult Than Expected**
- *Mitigation*: Budget 40% of time for prompt iteration; study successful examples (ChatExtract); use systematic testing

**R8: CWTS Integration Expectations Mismatch**
- *Mitigation*: Establish explicit deliverables agreement in Month 1; regular progress updates

## What Might We Be Missing?

### Potential Blind Spots (Proactive Agency)

1. **Multimodal Evidence**: Most archaeology papers include figures, maps, stratigraphic sections critical to claims. Your current plan focuses on text extraction. Are you comfortable deferring image analysis, or does this fundamentally limit validity assessment?

2. **Non-English Publications**: Archaeology is internationally diverse. Leiden has strong European networksâ€”will limiting to English create sampling bias that undermines generalisability claims?

3. **Grey Literature**: Much archaeological data appears in unpublished reports, theses, conference proceedings. Academic journals may not represent typical transparency levelsâ€”this could inflate your accuracy if you validate only on published papers.

4. **Computational Infrastructure**: CWTS may have preferred computing environments, institutional LLM access, or data governance requirements. Have you confirmed API access permissions and data handling protocols?

5. **Publication Strategy**: You mention multiple target journals but six months is barely enough for one submission cycle. Which publication is highest priority for your CV/field impact?

6. **Community Building**: The CLAIMS vision emphasized community governance and learned society partnerships. Six months doesn't allow for thisâ€”is there a lightweight engagement strategy that plants seeds for Phase 2?

7. **Comparison Baselines**: You'll compare LLM scores to expert panels, but what about comparing to existing metrics (citation counts, journal prestige) to demonstrate added value? Showing what traditional metrics miss could strengthen impact.

8. **Failure Documentation**: What if accuracy is only 60%? What if experts disagree fundamentally about credibility? The most valuable outcome might be rigorously documenting where automation failsâ€”have you planned for "negative results" as valid contribution?

## Confirmed Strategic Direction

Based on your specifications, the implementation pathway is now clearly defined:

**Corpus Strategy**: Moderately multidisciplinary from the outset, focused on fieldwork-based HASS and environmental sciences (archaeology, ancient history, geoscience, ecology). Initial corpus includes papers you have co-authored to enable rapid ground truth validation.

**Model Architecture**: Begin with Claude Sonnet 4.5 for prompt engineering (Weeks 1-3), transition to multi-model consensus using local infrastructure (Weeks 4-6), integrate SOTA API models for final assessment phase (Months 2-6). Local compute capacity (up to 120b parameters) provides cost-effective iteration and experimentation.

**Validation Approach**: Leverage three-week CWTS residence for methodological validation with metascience experts, followed by self-validation using your domain expertise, culminating in formal expert panel assessment (Months 5-6).

**repliCATS Integration**: Your collaborator's access to ~3,900 claim judgements and 200 paper-level assessments provides calibration dataset for signal translation and external validation benchmark.

**Development Environment**: Begin extraction prototyping in Claude web interface (conversational iteration advantage), transition to Claude Code at Month 2 (Week 4-5) once extraction protocols stabilise and multi-model orchestration begins.

**Documentation Philosophy**: Open research project documenting both successes and failures; publish findings regardless of whether LLM-expert correlation meets optimistic targets.

## Immediate Implementation Path

**This Week (Week 1):**

1. **Corpus Selection** (Priority 1)
   - Identify 5 papers for initial extraction testing:
     * 2 archaeology papers you co-authored (immediate ground truth validation)
     * 1 ancient history paper (testing disciplinary transfer)
     * 1 environmental fieldwork paper (ecology or geoscience)
     * 1 "problematic" paper with known documentation issues
   
2. **Ground Truth Development** (Priority 2)
   - Hand-code one paper completely:
     * Extract all explicit claims (tag as empirical/interpretive)
     * Map evidence to claims (material culture, contexts, datasets)
     * Document methods (field protocols, analytical workflows)
     * Identify stated limitations and alternative interpretations
   - This becomes validation gold standard for automated extraction

3. **CEM Schema Definition** (Priority 3)
   - Specify formal structure for Claim-Evidence-Method graphs:
     * Node types and required attributes
     * Edge types and relationship semantics
     * Provenance tracking requirements
     * Confidence score representations

4. **CWTS Engagement** (Priority 4)
   - Schedule informal presentation with metascience researchers
   - Prepare 10-minute overview of credibility signal adaptation challenge
   - Solicit critique on repliCATSâ†’fieldwork translation strategy

**Weeks 2-3:**

5. **Extraction Prototype Development**
   - Implement claim extraction with Claude Sonnet 4.5
   - Test on 3-4 papers; calculate precision/recall against ground truth
   - Iterate prompts until achieving >75% accuracy
   - Add evidence mapping and method extraction
   - Produce first complete CEM graphs

6. **Multi-Model Preparation**
   - Set up local model infrastructure
   - Test orchestration framework
   - Compare Claude outputs against llama3.3:70b baseline

7. **repliCATS Collaboration Initiation**
   - Contact collaborator for data access clarification
   - Request sample papers with full assessment data
   - Begin signal translation analysis

**Week 4 Transition:**
- Migrate to Claude Code for systematic development
- Implement multi-model consensus architecture
- Build automated validation pipelines

## Questions to Clarify Before Proceeding

1. **Scope Constraint**: Are you genuinely committed to 30-50 papers for validation, or would 15-20 deeply analysed papers be more realistic given the six-month window and exploratory nature?

2. **repliCATS Collaboration**: What data can your collaborator actually provide? Original papers with ratings? Structured justifications? Just aggregate statistics? This significantly affects validation strategy.

3. **CWTS Expectations**: What does "visiting fellowship" entailâ€”physical presence requirements, seminar presentations, teaching? This affects available deep work time.

4. **Publication Priority**: Which publication matters most for your career trajectory? Technical demonstration (JOSS), methodological innovation (DSH), or research evaluation impact (Research Evaluation)?

5. **Disciplinary Breadth**: Do you need to demonstrate cross-disciplinary applicability in Phase 1, or is deep validation in archaeology sufficient for the fellowship deliverables?

6. **Continuation Funding**: Is there Phase 2 funding secured or anticipated? This affects whether you optimise for immediate completeness vs establishing foundations for continuation.

7. **Risk Tolerance**: If extraction accuracy plateaus at 70% (below ChatExtract's 85-90%), is that sufficient for proof-of-concept, or would you pivot approaches?

## Next Steps: From Planning to Implementation

The immediate priority is operationalising the extraction layerâ€”transforming conceptual frameworks into functioning code that reliably decomposes scholarly arguments into structured representations.

**Priority Actions (This Week)**:

1. **Corpus Assembly** 
   - Select initial 5 papers balancing disciplinary diversity with validation feasibility
   - Prioritise papers where you possess deep contextual knowledge
   - Include 2-3 co-authored works for ground truth development

2. **Ground Truth Development**
   - Hand-code one paper completely to establish validation standard
   - Document decision heuristics for claim identification, evidence typing, method extraction
   - Create annotation schema that can guide both human validation and prompt engineering

3. **Initial Extraction Prototyping**
   - Develop claim extraction prompts collaboratively
   - Test on first paper; measure against ground truth
   - Iterate rapidly given zero-cost web interface experimentation

4. **CWTS Integration**
   - Schedule methodological presentation
   - Prepare repliCATS signal translation for critique
   - Solicit feedback on validation approach

**Subsequent Milestones**:
- **Week 2**: Functioning claim + evidence extraction with initial accuracy benchmarks
- **Week 3**: Complete CEM graph generation; multi-model preparation
- **Week 4**: Transition to Claude Code; begin systematic development
- **Month 2**: Multi-model consensus functioning; repliCATS calibration dataset obtained
- **Month 3**: Credibility assessment modules operational
- **Months 4-6**: Validation, refinement, documentation, publication preparation

The path forward is now clearly definedâ€”the next conversation should focus on **elaborating the extraction prototype**: specific prompt architectures, validation metrics, and testing protocols for Week 1 implementation.

Shall we proceed to extraction prototype design?