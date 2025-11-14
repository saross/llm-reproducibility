# CLAIMS: Contextual Linked Arguments in Machine-actionable Scholarship
## A Comprehensive Product Plan for Automated Research Credibility Assessment in the Humanities and Social Sciences

### Executive Summary

This proposal outlines the development of CLAIMS (Contextual Linked Arguments in Machine-actionable Scholarship), an innovative system leveraging large language models to decompose scholarly publications into structured knowledge representations whilst assessing multiple dimensions of research credibility. Unlike existing research assessment tools that operate at the document level and privilege citation metrics, CLAIMS extracts individual claims, maps supporting evidence, evaluates methodological transparency, and identifies potential biases – all whilst preserving the interpretive complexity characteristic of humanities and social science scholarship.

The system addresses a critical gap in research evaluation infrastructure. Whilst the 'credibility revolution' has transformed research practices in experimental sciences, humanities and social sciences remain largely disconnected from these advances due to fundamental epistemological differences. CLAIMS bridges this gap by reconceptualising research quality around credibility rather than reproducibility, developing assessment frameworks appropriate to interpretive, abductive, and 'small science' research contexts.

Building upon proven technologies – including Anthropic's CLIO semantic extraction system and the University of Melbourne's repliCATS credibility framework – CLAIMS represents the first comprehensive attempt to automate substantive quality assessment for interpretive disciplines at scale.

### The Vision: Beyond Papers to Knowledge Structures

Current scholarly communication remains trapped in a document-centric paradigm optimised for human narrative consumption rather than computational understanding or systematic quality assessment. CLAIMS proposes a fundamental restructuring of how we represent and evaluate scholarly knowledge:

**From monolithic papers to composable knowledge units**: Research decomposed into formally stated claims, typed evidence, explicit methods, and documented theoretical frameworks – all interconnected through a knowledge graph architecture.

**From citation counting to credibility assessment**: Evaluation based on research design transparency, evidential adequacy, methodological documentation, analytical transparency, bias recognition, and reflexive positioning rather than bibliometric proxies.

**From opaque peer review to transparent evaluation**: Automated assessment processes that are auditable, consistent, and scalable whilst preserving disciplinary nuance.

**From reactive to proactive quality enhancement**: Systems that not only assess existing work but guide researchers toward more credible practices during the research process.

### Technical Architecture

The system comprises five interconnected layers:

#### 1. Semantic Extraction Layer
- **Deep semantic extraction** using frontier LLMs (Claude 4, Gemini Pro 2.5, ChatGPT o3) to decompose papers into structured components
- **Bottom-up pattern discovery** inspired by CLIO's approach, preserving contextual complexity
- **Multi-model consensus approaches** for reliability across different LLM architectures
- **Confidence scoring** for all extracted elements with uncertainty quantification
- **Preservation of interpretive complexity** through retention of alternative readings and contested evidence

#### 2. Knowledge Representation Layer
- **Graph-based storage** of claims, evidence, methods, theoretical frameworks, and their interrelationships
- **Persistent identifiers** (leveraging RAiD infrastructure) for all knowledge entities
- **Versioning and provenance tracking** to document knowledge evolution
- **FAIR-compliant metadata schemas** adapted for humanities data types
- **Support for multimodal evidence** including textual sources, material culture, and visual data

#### 3. Credibility Assessment Layer
Building directly on the repliCATS framework whilst extending for humanities contexts:

- **Transparency and Design Evaluator**: Assesses research design coherence, exploratory/confirmatory alignment, and methodological transparency
- **Validity and Evidential Adequacy Assessor**: Evaluates claim-evidence relationships, identifies over-interpretation, and flags unsupported generalisations
- **Robustness and Completeness Checker**: Determines documentation sufficiency and alternative interpretation consideration
- **Generalisability and Limitation Detector**: Identifies scope constraints, sampling biases, and missing contextualisation
- **Analytical Transparency Evaluator**: Assesses reproducibility of analytical workflows and data transformation documentation
- **Reflexive Positioning Analyser**: Evaluates acknowledgement of theoretical commitments and disciplinary constraints

#### 4. Query and Synthesis Layer
- **Natural language querying** across decomposed knowledge structures
- **Comparative analysis** across papers, claims, and methodological approaches
- **Discourse tracking** and debate mapping within scholarly communities
- **'What-if' reasoning** to explore alternative interpretations
- **Trend analysis** of credibility indicators across time and disciplines

#### 5. Integration and Delivery Layer
- **RESTful API** for institutional integration
- **Web interface** for individual researchers and reviewers
- **Export capabilities** to standard bibliographic and knowledge management systems
- **Customisable dashboards** for different stakeholder groups
- **Audit trails** for all assessments with full explainability

### Implementation Roadmap

#### Phase 1: Foundation and Proof of Concept (Months 1-6)
**Objectives**: Establish core extraction and assessment capabilities

- Develop and refine LLM prompts for knowledge extraction
- Create initial ontologies for humanities knowledge representation
- Implement basic credibility assessment modules
- Process 50-70 open access publications as validation corpus
- Conduct expert panel validation with 73% accuracy target (matching repliCATS baseline)

**Deliverables**:
- Functional prototype with API
- Validation dataset with expert annotations
- Technical documentation
- Performance benchmarks

#### Phase 2: Expansion and Refinement (Months 7-12)
**Objectives**: Scale capabilities and enhance accuracy

- Expand to 500+ publications across multiple disciplines
- Implement multi-model consensus mechanisms
- Develop discipline-specific assessment heuristics
- Create user interfaces for different stakeholder groups
- Explore retrieval-augmented generation (RAG) for enhanced accuracy

**Deliverables**:
- Production-ready API
- Web application for researchers
- Institutional dashboard
- Expanded validation datasets

#### Phase 3: Domain Specialisation (Months 13-18)
**Objectives**: Optimise for specific disciplinary contexts

- Investigate domain-specific model approaches (fine-tuning, RAG, hybrid systems)
- Develop specialised modules for archaeology, history, anthropology
- Implement multimodal evidence handling
- Create discipline-specific training materials
- Build community governance structures

**Deliverables**:
- Domain-optimised models
- Specialised assessment rubrics
- Community contribution framework
- Training programmes

#### Phase 4: Institutional Integration (Months 19-24)
**Objectives**: Enable widespread adoption

- Pilot implementations at 5-10 institutions
- Develop integration pathways with research information systems
- Create sustainability models (SaaS, on-premise, hybrid)
- Establish certification programmes for credibility assessment
- Build policy frameworks for research evaluation reform

**Deliverables**:
- Enterprise deployment options
- Integration documentation
- Business model validation
- Policy recommendations

### Market Analysis and Positioning

#### Target Markets

**Primary Markets**:
- Research-intensive universities seeking assessment reform
- Funding bodies implementing responsible research assessment
- Publishers developing editorial quality assurance
- Research assessment agencies modernising evaluation approaches

**Secondary Markets**:
- Individual researchers seeking feedback on manuscripts
- Systematic review teams requiring quality assessment at scale
- Policy organisations evaluating research evidence
- Libraries developing collection assessment criteria

#### Competitive Landscape

CLAIMS occupies a unique position in the research technology ecosystem:

**Versus Citation Analysis Tools** (Web of Science, Scopus):
- Assesses content quality rather than counting citations
- Provides actionable feedback rather than retrospective metrics
- Evaluates unpublished and recent work immediately

**Versus AI Literature Review Tools** (Elicit, Consensus, Semantic Scholar):
- Operates at claim level rather than paper level
- Provides credibility assessment rather than just extraction
- Preserves interpretive complexity rather than surface summaries

**Versus Traditional Peer Review**:
- Offers consistent, auditable assessment criteria
- Scales to handle volume beyond human capacity
- Provides immediate feedback rather than months-long delays
- Supplements rather than replaces human judgment

**Versus Statistical Reproducibility Tools** (statcheck, p-checker):
- Designed for interpretive rather than quantitative research
- Assesses broader credibility dimensions beyond statistics
- Handles narrative argumentation and qualitative evidence

### Revenue Model and Sustainability

#### Tiered Service Model

**Institutional Tier** (Primary Revenue):
- Annual licensing based on researcher FTE
- Unlimited processing within institution
- Custom integrations and training
- Priority support and feature requests
- Estimated pricing: €25,000-100,000 annually

**Publisher Tier**:
- Per-journal licensing for editorial assessment
- API access for submission systems
- Bulk processing capabilities
- White-label options
- Estimated pricing: €10,000-50,000 per journal annually

**Individual Tier** (Market Development):
- Freemium model with basic assessment free
- Premium features for detailed feedback
- Subscription for unlimited use
- Estimated pricing: €50-200 monthly

**Grant Integration**:
- Partnerships with funders for applicant assessment
- Bulk processing of funded research outputs
- Custom reporting for research programmes
- Revenue sharing or direct licensing

#### Sustainability Strategy

1. **Open Core Model**: Base assessment capabilities open source, premium features proprietary
2. **Community Development**: Academic advisory board ensures continued relevance
3. **Grant Funding**: Initial development through research councils and foundations
4. **Strategic Partnerships**: Integration with established research infrastructure providers

### Critical Assessment

#### Strengths of the Approach

1. **Addresses Genuine Market Need**: The humanities and social sciences urgently require assessment frameworks that respect their epistemological foundations whilst maintaining rigorous standards. No existing solution adequately serves this market.

2. **Leverages Proven Technologies**: Combines established approaches (semantic extraction via CLIO, credibility assessment via repliCATS, knowledge graphs, persistent identifiers) rather than requiring fundamental breakthroughs.

3. **Strong Domain Expertise**: Team combines deep understanding of humanities research practices, research data management, and computational approaches.

4. **Timely Market Entry**: Aligns with global movements toward research assessment reform (DORA, CoARA, Leiden Manifesto) whilst providing concrete implementation pathways.

5. **Scalable Technology Stack**: LLM-based approach can expand to new disciplines and languages without fundamental re-engineering.

6. **Clear Value Proposition**: Offers tangible benefits to multiple stakeholder groups with quantifiable ROI through improved research quality and reduced review burden.

#### Challenges and Limitations

1. **LLM Hallucination Risk**: Current models may generate plausible but incorrect assessments, requiring careful validation and confidence scoring.

2. **Disciplinary Resistance**: Humanities scholars may view automated assessment as reductive or threatening to interpretive scholarship traditions.

3. **Validation Complexity**: Establishing ground truth for credibility assessment in disciplines where experts legitimately disagree presents ongoing challenges.

4. **Cost Structure**: LLM API costs currently high (€3,000 for 50-70 papers), though falling rapidly. Local deployment options needed for sustainability.

5. **Bias Amplification**: Risk of perpetuating existing biases in scholarly communication if training data reflects current inequities.

6. **Technical Complexity**: Maintaining extraction quality across diverse writing styles, theoretical frameworks, and argumentation structures requires continuous refinement.

7. **Market Education**: Significant effort required to shift from entrenched citation-based metrics to content-based assessment.

#### Risk Mitigation Strategies

1. **Hybrid Human-AI Approach**: Position as augmenting rather than replacing human judgment
2. **Transparent Methodology**: Open source core components and assessment criteria
3. **Continuous Validation**: Ongoing expert review and model refinement
4. **Community Governance**: Advisory boards from target disciplines
5. **Gradual Deployment**: Start with willing early adopters before broader rollout

### Next Steps and Recommendations

#### Immediate Actions (Next 3 Months)

1. **Technical Feasibility Study**
   - Process 10-20 papers across target disciplines
   - Benchmark extraction accuracy against human coding
   - Estimate processing costs at scale
   - Identify technical bottlenecks

2. **Market Validation**
   - Interview 20+ potential institutional customers
   - Survey 100+ researchers on assessment pain points
   - Engage with 5+ publishers on editorial needs
   - Validate pricing model assumptions

3. **Team Assembly**
   - Recruit NLP engineer with LLM expertise
   - Engage humanities scholars as disciplinary advisors
   - Identify business development lead
   - Establish scientific advisory board

4. **Funding Strategy**
   - Prepare grant applications for major funders:
     * European Research Council (ERC Proof of Concept)
     * UK Research and Innovation (UKRI Future Leaders)
     * Australian Research Council (ARC Linkage)
     * Private foundations (Mellon, Sloan, Moore)
   - Explore university spin-out options
   - Engage with research infrastructure investors

#### Strategic Development Priorities

1. **Start Narrow, Expand Systematically**
   - Initial focus on archaeology and ancient history (leveraging domain expertise)
   - Validate approach thoroughly before expanding
   - Build discipline-specific modules incrementally

2. **Prioritise Transparency**
   - Make assessment criteria fully auditable
   - Provide detailed explanations for all evaluations
   - Enable researchers to contest and correct assessments

3. **Build Community Trust**
   - Engage learned societies as partners not targets
   - Co-develop assessment criteria with disciplinary experts
   - Publish validation studies in target discipline journals

4. **Design for Integration**
   - Ensure compatibility with existing research systems
   - Provide multiple deployment options
   - Build partnerships with established providers

#### Technical Development Priorities

1. **Prompt Engineering Excellence**
   - Invest heavily in prompt design and testing
   - Build libraries of discipline-specific prompts
   - Develop prompt versioning and testing infrastructure

2. **Explainability First**
   - Every assessment must trace to specific textual evidence
   - Confidence scores for all outputs
   - Clear documentation of reasoning chains

3. **Scalability Planning**
   - Design for 100,000+ papers annually
   - Implement caching and efficiency optimisations
   - Plan for multilingual expansion

4. **Flexibility Architecture**
   - Modular design for easy feature addition
   - API-first development approach
   - Support for multiple LLM providers

### Conclusion

CLAIMS represents an ambitious yet achievable vision for transforming research assessment in the humanities and social sciences. By leveraging cutting-edge language models to extract and assess knowledge structures, we can move beyond superficial metrics to evaluate what truly matters: the credibility and rigour of scholarly arguments.

The convergence of technological capability (advanced LLMs), methodological frameworks (repliCATS), and market demand (research assessment reform) creates a unique window of opportunity. Success requires navigating significant technical and social challenges, particularly around community acceptance and validation complexity. However, the potential impact – enabling fairer, more substantive research evaluation at scale – justifies the effort.

With careful implementation, sustained community engagement, and realistic expectations about capabilities and limitations, CLAIMS can catalyse fundamental change in how we recognise and reward quality scholarship. The system promises not just better assessment, but better research – guiding scholars toward more transparent, rigorous, and credible practices from the outset.

The path forward requires assembling the right team, securing adequate funding, and maintaining unwavering focus on serving the genuine needs of the scholarly community. By starting with proof of concept in focused disciplines and expanding systematically based on validated success, CLAIMS can grow from innovative idea to essential infrastructure for 21st-century scholarship.