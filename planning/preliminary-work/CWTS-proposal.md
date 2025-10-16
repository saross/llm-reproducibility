# Automated Assessment of Research Credibility in the Humanities and Social Sciences: Leveraging Large Language Models to Advance Transparent and Reliable Scholarship

## Abstract

This proposal outlines a six-month research phase to develop and evaluate a computational system for assessing the reliability and transparency of humanities and social science publications. The project addresses fundamental challenges in evaluating research quality in disciplines characterised by interpretive complexity, methodological diversity, and varied modes of reasoning. Using large language models (LLMs), the proposed system first extracts and structures the knowledge claims, evidence, and arguments within scholarly publications, then employs this structured representation to assess multiple dimensions of research credibility. These dimensions include the transparency and coherency of research design, the adequacy of evidence supporting claims, efforts to reduce bias, the acknowledgement of limitations, and the appropriate documentation and management of research data and analytical pipelines. By automating the extraction and assessment process, this project provides scalable tools for assessing research in the service of higher standards of research transparency in domains where traditional quality indicators prove inadequate. The six-month phase from September 2025 to February 2026 will establish proof-of-concept systems and validation frameworks, laying foundations for broader implementation across institutions and disciplines.

## Problem Statement and Rationale

### The Challenge of Research Quality in Interpretive Disciplines

Over the past two decades, researchers have identified widespread concerns about the reliability of published research findings. Studies suggest that a substantial proportion of published research – perhaps one-third to two-thirds – may present conclusions that cannot be substantiated upon closer examination (Baker 2016; Ioannidis 2005). This ‘reproducibility crisis’ has, in turn, sparked what Vazire (2018) terms the 'credibility revolution' – a movement to establish more rigorous standards for research design, data sharing, and analytical transparency. This revolution has produced transformative changes in experimental sciences, from pre-registered study protocols to requirements for making data Findable, Accessible, Interoperable, and Reusable (FAIR) (Nosek et al. 2018; Wilkinson et al. 2016).

Yet the adoption of these enhanced standards remains uneven across disciplines. In the humanities and social sciences – particularly in field-based disciplines such as archaeology, anthropology, and historical studies – implementing credibility-enhancing practices faces unique challenges. These disciplines often employ inductive or abductive reasoning (insights driven by ‘surprise’; cycling between pattern-seeking and hypothesis-testing), investigate unique or non-repeatable phenomena, and produce knowledge through interpretive frameworks that resist empirical adjudication.

Recent systematic evaluations reveal the extent of these challenges. Taking one of the most fundamental aspects of transparency \- the availability of FAIR data \- reveals the extent of the gap. In archaeology, D'Gluyas and Gibbs (2022) found only 15% of field projects published genuinely reusable datasets. Lodwick (2019) discovered that while half of archaeobotany articles share some form of data, few provide sufficient documentation for meaningful reuse. Similar patterns emerge across humanities and social sciences, where established practices of narrative argumentation often obscure the empirical foundations and analytical processes underlying scholarly claims.

### The Promise of Computational Approaches

The emergence of large language models (LLMs) presents unprecedented opportunities for addressing these challenges systematically. Recent advances demonstrate the technical feasibility of our approach. Anthropic's CLIO system successfully performed semantic extraction at scale, analysing over one million conversations through bottom-up pattern discovery whilst preserving contextual complexity – demonstrating that LLMs can identify meaningful categories in large text corpora without losing nuance (Anthropic 2024). More directly relevant, the repliCATS project at the University of Melbourne has operationalised credibility assessment for social science research, achieving 73% accuracy in predicting replicability through structured evaluation of transparency, validity, and robustness signals (Camerer et al. 2018; Wintle et al. 2021). The project has evolved into the SMART program, which continues to develop traditional machine learning approaches for automated credibility assessment, validating both the importance and feasibility of this challenge (Gordon et al. 2020).

My project builds upon these foundations while addressing their limitations. Unlike current extraction tools that focus on surface-level information retrieval, we propose deep semantic extraction that preserves argumentative structure and interpretive complexity. Unlike repliCATS's statistical approaches, we leverage LLMs' capacity for understanding natural language argumentation. Recent work on extracting structured data from scientific papers using conversational LLMs demonstrates that careful prompt engineering can achieve high accuracy in complex extraction tasks (Polak & Morgan 2024).

For this initial phase, we will employ frontier models – Claude 4, Gemini Pro 2.5, and ChatGPT o3 (or ChatGPT 5 should it be released on schedule) – which offer sophisticated capabilities in parsing complex argumentative structures, identifying methodological approaches, and evaluating the relationship between evidence and claims. These general-purpose models provide the flexibility needed to explore diverse disciplinary conventions and develop robust extraction frameworks. Future phases will investigate domain-specific approaches to enhance model performance on humanities and social science texts. Approaches may include retrieval-augmented generation (RAG) using frontier models with disciplinary corpora, fine-tuning open-weight models on scholarly publications, or hybrid systems combining both approaches. The optimal strategy will depend on performance benchmarks established in Phase 1 and available computational resources.

### Conceptualising Credibility in Humanities and Social Sciences

I propose reconceptualising research quality assessment around the concept of credibility rather than reproducibility. Credible research in these fields demonstrates several key characteristics:

**Coherent and transparent Research Design:** Authors explicitly articulate whether their work seeks to explore phenomena and generate hypotheses (exploratory research) or to test specific propositions (confirmatory research) – and follow through with conformant implementation. Methods align appropriately with stated aims, and limitations are acknowledged explicitly.

**Adequate Evidentiary Foundations:** Claims rest upon evidence that is sufficient, representative, and appropriately contextualised. Researchers acknowledge sampling limitations, consider alternative interpretations, and avoid over-generalising from limited data.

**Methodological Documentation:** Research processes are documented sufficiently to allow critical evaluation. This includes not only data collection procedures but also analytical workflows, theoretical frameworks, and interpretive decisions.

**Data Stewardship:** Where applicable, researchers follow FAIR principles adapted for humanities data types, recognising that 'data' may include archaeological assemblages, historical documents, ethnographic field notes, or digital corpora.

**Analytical Transparency:** Where relevant, analyses employ reproducible workflows that document data transformations from raw to final states. Researchers prioritise programmatic approaches (scripts, code) over black-box or manual processes, enabling others to trace analytical decisions and reproduce results. This includes documenting data cleaning procedures, transformation steps, statistical choices, and providing access to analytical code where applicable.

**Reflexive Positioning:** Credible research acknowledges how theoretical commitments, disciplinary traditions, and practical constraints shape research outcomes, positioning findings within broader scholarly conversations.

### The Need for Structured Knowledge Representation

Assessing these credibility dimensions requires first extracting and structuring the knowledge content of publications. By 'knowledge representation', I refer to the computational modelling of the claims, evidence, methods, and logical relationships within scholarly texts. This structured representation – transforming narrative arguments into computationally tractable elements – provides the foundation for systematic credibility assessment. Only by understanding what a paper claims, what evidence supports those claims, and how that evidence was gathered and analysed can we evaluate whether the research meets appropriate standards of credibility.

## Research Objectives for the Six-Month Phase

### Primary Objectives (September 2025 – February 2026\)

This initial phase of a longer research programme will:

1. **Develop knowledge extraction systems** that decompose humanities and social science publications into structured representations of claims, evidence, methods, and theoretical frameworks, preserving the interpretive complexity characteristic of these domains. This extraction provides the essential foundation for all subsequent assessment.  
     
2. **Create credibility assessment modules** that evaluate research quality indicators based on the extracted knowledge structures, adapting principles from the broader movement toward research transparency to the specific contexts of humanities and social sciences.  
     
3. **Validate system performance** through rigorous comparison with expert human assessment, establishing benchmarks for automated evaluation and documenting systematic limitations.  
     
4. **Produce technical specifications** for scaling automated assessment beyond the proof-of-concept phase, including architectural designs, integration pathways, and resource requirements.

### Secondary Objectives

- Develop initial ontologies for representing knowledge claims in interpretive research contexts  
- Establish workflows for quality assurance in automated assessment  
- Create training materials for potential system users  
- Build foundations for community-driven refinement and extension

## Methodology

### Phase 1: Framework Development and Corpus Assembly (September – October 2025\)

The project begins by establishing theoretical and empirical foundations:

**Framework Adaptation:** Drawing upon my prior work developing manual assessment frameworks for archaeological field research, I will translate human evaluation criteria into computationally tractable indicators. This involves operationalising concepts such as 'methodological transparency' and 'evidential adequacy' for automated assessment.

**Corpus Development:** I will assemble 50 – 70 open access publications spanning archaeology, history, and cognate fields. Selection criteria prioritise:

- Recent publications explicitly addressing research transparency  
- Studies employing diverse methodological approaches  
- Well-resourced 'flagship' research projects  
- Geographic and temporal diversity (with a focus on more recent work)

**Ontology Selection / Development:** Initial knowledge representation schemas will build upon existing standards while addressing unique requirements of humanities scholarship, particularly the need to represent interpretive claims and contested evidence. This is an area where input and advice from CWTS staff would be particularly appreciated.

### Phase 2: Knowledge Extraction Development (November – December 2025\)

The core technical work involves developing LLM-based extraction systems:

**Claim Extraction Module:** Distinguishing empirical assertions from interpretive arguments, identifying confidence levels, and mapping logical relationships between claims.

**Evidence Mapping System:** Capturing diverse evidence types (material culture, textual sources, oral histories, quantitative data) and their relationships to specific claims.

**Methodological Extraction:** Identifying research designs, sampling strategies, analytical approaches, and theoretical frameworks, including those left implicit in the text.

**Relationship Modelling:** Mapping how claims, evidence, and methods interconnect to form scholarly arguments, preserving nuance and complexity.

### Phase 3: Credibility Assessment Implementation (January 2026\)

Building upon extracted knowledge structures, I will develop assessment modules initially adapted from the repliCATS credibility signals framework (Wintle et al. 2021), which identified seven key indicators: comprehensibility, transparency, plausibility, validity, robustness, replicability, and generalisability. My implementation will translate these human-assessed signals into LLM-based evaluators:

**Transparency and Design Evaluator:** Adapting repliCATS' transparency signal, this module assesses whether research clearly articulates its exploratory or confirmatory nature, whether methods align with stated objectives, and whether analytical decisions are explicitly documented.

**Validity and Evidential Adequacy Assessor:** Building on repliCATS' validity and plausibility signals, this evaluates whether evidence sufficiently supports claims, identifies over-interpretation, and flags unacknowledged limitations.

**Robustness and Completeness Checker:** Extending repliCATS' robustness signal, this determines whether research processes are documented sufficiently for critical evaluation and whether findings would likely hold under alternative analytical approaches.

**Generalisability and Limitation Detector:** Incorporating repliCATS' generalisability assessment, this identifies geographical, temporal, or theoretical constraints on findings, selective evidence use, and missing alternative explanations.

This approach explicitly builds on validated assessment criteria whilst leveraging LLMs' capacity for nuanced textual analysis that goes beyond the binary classifications used in the original repliCATS implementation. I will develop and modify these concepts and approaches as necessary for the use of LLMs.

### Phase 4: Validation and Refinement (February 2026\)

Rigorous validation ensures system reliability:

**Expert Panel Validation:** Assembling researchers from multiple disciplines to evaluate system outputs against their professional judgment.

**Systematic Error Analysis:** Identifying patterns in assessment failures to guide iterative refinement.

**Benchmark Establishment:** Documenting achieved accuracy levels and systematic limitations to set realistic expectations for operational deployment.

**Documentation and Dissemination:** Preparing comprehensive documentation, technical specifications, and initial publication drafts.

## Alignment with CWTS Mission and Strategic Opportunities

This project advances CWTS's mission across all three focal areas:

### Information & Openness

The project embodies open science principles through transparent, auditable assessment processes. All outputs – code, data, and documentation – will be openly licensed and FAIR compliant. By developing standards for machine-readable credibility assessment, we contribute to emerging infrastructure for transparent research evaluation.

### Evaluation & Culture

Moving beyond citation metrics to substantive content assessment addresses fundamental limitations of current evaluation systems. The project demonstrates concrete alternatives to journal-based metrics, supporting implementation of the Declaration on Research Assessment (DORA) principles and fostering cultural change toward quality over quantity.

### Engagement & Inclusion

Automated assessment tools democratise sophisticated evaluation capabilities, enabling institutions with limited resources to conduct comprehensive assessments. By focusing on 'small science' domains often marginalised in metric-based systems, we promote more inclusive and equitable research evaluation.

### Integration Opportunities

The project offers multiple pathways for integration with CWTS initiatives:

- Complementing the Leiden Ranking with experimental credibility indicators for humanities disciplines  
- Supporting research assessment reform through practical implementation tools  
- Advancing open science monitoring with systematic evaluation frameworks  
- Contributing to European research infrastructure through standardisation efforts

## Expected Deliverables (February 2026\)

### Technical Outputs

- Functional prototype processing 50 – 70 publications  
- Comprehensive API documentation  
- Validation dataset with expert annotations  
- Open-source codebase (MIT/Apache 2.0 licensed)

### Academic Publications (drafts)

- Technical implementation paper for Journal of Open Source Software  
- Methodological innovation article for Digital Scholarship in the Humanities  
- Research evaluation position paper for Research Evaluation  
- Disciplinary application for archaeological/historical journals

### Community Resources

- Prompt engineering libraries optimised for humanities texts  
- Credibility assessment rubrics adaptable across disciplines  
- Implementation guidelines for institutions  
- Training materials for research assessment professionals

## Resource Requirements and Support Structure

This project will be conducted during my long-service leave with computational resources provided by my home institution (estimated €3,000 for LLM API access). The visiting fellowship at CWTS would provide essential intellectual community, access to research evaluation expertise, and a platform for disseminating findings internationally.

## Future Phases and Long-term Vision

This six-month phase establishes foundations for a comprehensive research programme. Subsequent phases will:

**Phase 2 (March – August 2026):** Expand to additional disciplines, develop multilingual capabilities, pilot institutional implementations, and explore fine-tuning domain-specific models on humanities and social science texts to enhance recognition of disciplinary conventions and methodological terminology.

**Phase 3 (September 2026 – February 2027):** Create production-ready systems, establish governance frameworks, and build sustainable community infrastructure.

**Phase 4 (March 2027 onwards):** Support widespread adoption, develop specialised modules for different research contexts, and integrate with emerging research information systems.

The long-term vision encompasses fundamental transformation in how we assess research quality – moving from proxy metrics to direct evaluation of research credibility, scaled through computational approaches but grounded in disciplinary expertise.

## Conclusion

The movement toward more transparent and reliable research practices has transformed experimental sciences, yet humanities and social sciences remain largely disconnected from these advances. This project bridges that gap by developing computational tools that respect disciplinary epistemologies whilst implementing rigorous quality standards. By automating the extraction of knowledge structures and their subsequent credibility assessment, we enable systematic evaluation at scales impossible through traditional peer review.

The project's significance extends beyond technical innovation. By demonstrating practical pathways for implementing credibility assessment in interpretive disciplines, we address urgent needs in research evaluation, institutional assessment, and public trust in scholarship. The six-month phase at CWTS will establish proof-of-concept systems and validation frameworks, creating foundations for broader transformation in how we recognise and reward research quality across all domains of human knowledge.

I welcome the opportunity to pursue this work within CWTS's collaborative environment, contributing to the Centre's mission whilst advancing novel approaches to research assessment. Together, we can build evaluation systems that promote rigorous, transparent, and credible research, strengthening the foundations of scholarly knowledge in an era of justified scepticism.

