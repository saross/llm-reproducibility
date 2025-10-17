# Schemas for Evidence-Claims-Methods Extraction: A Comprehensive Survey

Research on existing schemas, taxonomies, and ontologies for evidence-claims-methods extraction and credibility assessment reveals a rich but fragmented landscape. While numerous frameworks exist across multiple domains, **no single schema adequately addresses the full scope of credibility assessment needs for HASS research contexts**. This report synthesizes findings from 40+ schemas and tools across five domains, identifies critical gaps, and provides concrete recommendations for schema development.

## Executive synthesis: The current landscape

The research identified production-ready tools (GROBID, SciBERT processing 1.14M papers), mature formal ontologies (SPAR with 1B+ citations, W3C PROV-O), and specialized frameworks (Cochrane systematic reviews, repliCATS credibility assessment). However, every framework exhibits significant gaps: **none integrate claim-evidence-method linkages with credibility assessment mechanisms**. Computational argumentation models lack provenance tracking. Provenance ontologies lack argumentation structures. Research methodology frameworks remain primarily manual. This fragmentation presents both a challenge and an opportunity for synthesis.

## Domain 1: Argumentation theory and claim-evidence structures

### Argument Interchange Format (AIF)

**Developers:** University of Dundee Argumentation Research Group (Reed, Rahwan, Chesñevar), 2005-2011  
**Adoption:** 50+ research papers, thousands of analyzed arguments in AIFdb database

AIF provides the most comprehensive formal framework for computational argumentation. Its two-layer architecture separates **information nodes** (claims, evidence) from **scheme nodes** (inference patterns), ensuring explicit reasoning. I-nodes connect only through S-nodes, forcing transparency about inferential relationships.

**Structure:** Upper ontology defines three scheme types: RA-nodes (rule application for support), CA-nodes (conflict application for attacks), PA-nodes (preference application for priorities). The Forms Ontology specifies inference schemes, conflict schemes, and preference schemes with premises, conclusions, assumptions, and exceptions.

**Formats:** RDF/XML, OWL, MySQL (AIFdb), Prolog, JSON, with DOT/SVG visualization

**Tools:** Araucaria (argument diagramming), OVA (web-based visualization), AIFdb (database infrastructure with REST API), Carneades (integration), Center for Argument Technology maintains ecosystem

**Strengths:** Highly formalized, multiple serialization formats, extensive tooling, handles both support and attack relationships, integrates argumentation schemes (expert opinion, analogy, consequences)

**Critical limitations for credibility assessment:** No built-in quality metrics for sources or evidence strength. No provenance tracking beyond basic attribution. Binary relations without numerical confidence values. Context-independent—difficult to model domain-specific credibility factors like sample size, methodology rigor, or replication status. No explicit uncertainty representation or confidence levels.

### IBM Project Debater

**Organization:** IBM Research (Israel/US), 2014-2021  
**Scale:** 400M newspaper articles indexed, 200K labeled examples for evidence detection

IBM Debater represents the most advanced production deployment of computational argumentation, demonstrated in 2019 live debate with world champion debater Harish Natarajan. The system processes **sentence-level claims and evidence** with automated quality scoring—unique among argumentation frameworks.

**Components:** Context-Dependent Claims (CDC) detection, evidence detection (95% precision for top 40 candidates), stance classification (pro/con/neutral), argument quality assessment (neural network trained on 30K scored arguments), Key Point Analysis for summarization, rebuttal matching

**Available as cloud APIs:** Claim detection, evidence detection, stance classification, quality assessment, term wikification, semantic relatedness, Key Point Analysis

**Strengths:** Production-ready with proven performance, massive training scale, quality scoring built-in (30K human-scored arguments), handles real-world text at scale, comprehensive pipeline from detection to generation

**Limitations:** Quality scoring ≠ credibility assessment (persuasiveness ≠ accuracy). No fact-checking—doesn't verify claims against ground truth. Limited source reliability assessment despite identifying sources. Newspaper corpus may have quality variations. Optimized for debate persuasiveness rather than scholarly accuracy. Black box neural components lack interpretability for understanding *why* an argument scores high.

### Toulmin Model

**Origin:** Stephen Toulmin (1958), "The Uses of Argument"  
**Adoption:** Ubiquitous in education, communication studies, widespread in argumentation research

The six-component Toulmin model (Claim, Grounds/Data, Warrant, Backing, Qualifier, Rebuttal) provides an intuitive conceptual framework originally based on legal arguments. Its simplicity explains widespread adoption for teaching critical thinking.

**Structure:** Essential core is Claim + Grounds + Warrant (data linked to claim via warrant). Extended with Backing (supports warrant), Qualifier (degree of certainty), Rebuttal (exceptions/counterarguments)

**Implementations:** Computational versions exist (Araucaria tool, PyLLMCore, machine learning classifiers achieving 0.88-0.91 F1 for component detection), but no standardized digital format

**Strengths:** Intuitive and widely understood, educational value, applicable across domains, handles both support and challenge, explicit about degree of certainty (qualifiers)

**Limitations:** Considered overly simplistic for complex arguments by researchers. Warrants often implicit and difficult to extract automatically. No built-in quality metrics—doesn't distinguish strong vs weak evidence or evaluate warrant validity. No mechanism for assessing backing sufficiency or determining rebuttal completeness. Scale challenges for arguments with many interacting premises.

### Microtext Corpus

**Developers:** Peldszus & Stede (University of Potsdam), 2013-2018  
**Scale:** 112 original + ~240 expanded texts, multilingual (German, English, Italian, Russian, Persian)

Argumentative Microtext provides a **benchmark corpus** for argument mining research with tree-structured annotations based on Freeman's macro-structure theory. Average 5 argumentative components per controlled-complexity text.

**Annotations:** Multi-layer including RST (Rhetorical Structure Theory), SDRT (Segmented Discourse Representation Theory), ARG (Argumentation), with support and attack relations in tree structures

**Tools:** MST-style parsers, BERT-based classifiers (0.85-0.97 F1 on specific tasks), cross-corpus training frameworks

**Strengths:** Widely used benchmark (50+ citing papers), clean controlled data, multiple language versions, enables comparative evaluation of argument mining approaches

**Limitations:** Artificial context may not reflect real credibility issues. Binary relations without strength values. Small scale (240 texts) limits coverage. No credibility annotations—corpus doesn't include source quality, fact-checking, or validation. Simplified structure may miss complexity of credibility assessment in longer academic papers.

### ASPIC+ Framework

**Developers:** Prakken (Utrecht), Modgil (King's College), 2007-2014  
**Citations:** 500+ citations of tutorial paper

ASPIC+ provides a **formal theoretical foundation** for structured argumentation with explicit rationality postulates. It's a framework for specifying systems rather than a system itself, generating Dung-style abstract argumentation frameworks.

**Structure:** Strict rules (deductive, →) vs defeasible rules (presumptive, ⇒). Three attack types: undermining (attacks premises), rebutting (attacks conclusions), undercutting (attacks inferences). Preference orderings resolve conflicts—attack becomes defeat only if attacker not weaker.

**Implementation:** Arg2p-kt (tuProlog/2P-Kt) available on GitHub with GUI (theory editor, solver, graph visualization), cross-platform Java/Kotlin/JavaScript

**Strengths:** Domain-independent and highly flexible, strong theoretical foundation with rationality postulates, explicit about defeat/priorities, models defeasibility central to scientific reasoning, maps cleanly to Dung semantics

**Limitations:** Abstract level requires instantiation for specific domains. No built-in credibility mechanisms—preference orderings must be pre-specified. Limited provenance metadata. Manual rule encoding required. Logical focus optimized for formal consistency rather than empirical credibility.

## Domain 2: Semantic publishing and scholarly communication

### SPAR Ontologies (Semantic Publishing and Referencing)

**Maintainers:** Peroni (Bologna), Shotton (Oxford)  
**Adoption:** OpenCitations (1B+ citations), 40%+ of Crossref via I4OC, Nature.com, DataCite, dozens of publishers

SPAR represents the **most mature and widely adopted** semantic framework for scholarly publishing, comprising 16+ interconnected ontologies. The suite covers the complete scholarly lifecycle from creation through citation.

**Core ontologies:** FaBiO (bibliographic entities: JournalArticle, Book, Thesis), CiTO (50+ citation types: citesAsEvidence, refutes, confirms, supports), DoCO (document components: Methods, Results, Discussion sections), BiRO (bibliographic references), PRO (publishing roles: author, editor, reviewer), PWO (publishing workflow), PSO (publishing status: draft→published→retracted)

**Extended suite:** SCoRO (scholarly contributions), FRAPO (funding/projects, CERIF-compliant), DataCite mapping, BiDO (bibliometric data: h-index, impact factors), FiveStars (article ratings), FR (FAIR reviews)

**Format:** OWL 2 DL with RDF/XML, Turtle, N-Triples serialization. PURLs with content negotiation. GitHub repositories with LODE-generated documentation.

**Tools:** SPACIN (SPAR Citation Indexer for OpenCitations), JATS2RDF (242 mapping statements from Journal Article Tag Suite XML), Biotea (PubMed Central in RDF), VocBench 3

**Strengths:** Comprehensive bibliographic coverage, citation typing provides rhetorical context (citesAsEvidence indicates evidential relationships), massive real-world deployment enables data integration at scale, interoperability with other Semantic Web standards, document structure via DoCO enables section-level analysis

**Critical gaps for credibility:** No explicit claim verification framework. No evidence strength quantification—CiTO provides types but not weights. Limited retraction tracking (PSO has status flag but no structured reasons). No conflict of interest metadata. No peer review process modeling. BiDO provides bibliometric indicators (citations, h-index) but these are **impact** metrics, not **validity** metrics. Claims implicit in document structure rather than explicitly modeled as first-class objects.

### Research Object Ontologies

**Origin:** EU Wf4Ever Project (2011-2014)  
**Modern successor:** RO-Crate (WorkflowHub, Zenodo)

Research Objects provide **semantically rich aggregations** for reproducible research, particularly strong for computational workflows. The framework bundles workflows, data, metadata, and execution provenance into portable packages.

**Ontologies:** ro: (core, based on OAI-ORE), wfdesc: (workflow description—templates), wfprov: (workflow provenance—executions, aligned with PROV-O), roevo: (evolution tracking), annotation ontology

**Structure:** wfdesc captures **step-by-step processes** (Workflow, Process, Input, Output, Parameter) at template level. wfprov captures **execution artifacts** (WorkflowRun, ProcessRun, Artifact) with complete provenance chains (wasOutputFrom, usedInput, describedByProcess).

**Tools:** Taverna (native RO support), Galaxy (RO-Crate export), Common Workflow Language (RO packaging), myExperiment (workflow sharing), RO-Crate tools

**Strengths:** Excellent computational reproducibility—complete workflow bundles enable exact re-execution. Detailed execution provenance via wfprov + PROV-O. Strong for neuroimaging (ReproNim), bioinformatics (Galaxy), computational chemistry. Bundles everything needed: code, data, environment, parameters.

**Limitations:** Workflow-centric—limited to computational research, less applicable to qualitative HASS methods. Claims not explicitly modeled. No quality metrics or validation tracking. Doesn't capture interpretive reasoning or professional judgment. Missing: interview protocols, archival research methods, ethnographic procedures. Strong on *how* computations executed, weak on *what* claims supported and *why* credible.

### Nanopublications

**Community:** International, decentralized  
**Scale:** Millions deployed (DisGeNET: 1M+ gene-disease associations, NeXtProt protein annotations)

Nanopublications provide **minimal, citable knowledge assertions** with provenance, using a distinctive four-part RDF structure with cryptographic Trusty URIs for immutability.

**Structure (4 named graphs):** Head (connects sub-graphs), Assertion (main claim, e.g., "gene X → disease Y"), Provenance (how assertion generated), PublicationInfo (nanopub metadata with ORCID attribution)

**Ontology:** np: namespace with hasAssertion, hasProvenance, hasPublicationInfo. Uses W3C PROV-O vocabulary (wasDerivedFrom, wasAttributedTo).

**Tools:** Nanodash (web creation with ORCID login), templates for reusable patterns, Nanopub-Java/Python libraries, NanoWeb (search/browse), distributed SPARQL

**Strengths:** Fine-grained provenance at triple level. Immutability via Trusty URI cryptographic hashing. Citable atomic facts with persistent identifiers. Strong ORCID-based attribution. Massive life sciences deployment proves scalability.

**Limitations:** Variable provenance depth—quality of provenance depends on creator diligence. No standardized quality assessment framework. No peer review integration. Trust via provenance inspection only—no automated verification. No conflict of interest tracking. Granularity can fragment complex arguments across many nanopubs, obscuring higher-level reasoning.

### Micropublications Ontology

**Developers:** Tim Clark, Paolo Ciccarese, Carole Goble (2014)  
**Paper:** J. Biomedical Semantics doi:10.1186/2041-1480-5-28

Micropublications **uniquely model claims explicitly** as first-class objects with evidence graphs and argumentation relationships—closest to what's needed for HASS credibility assessment.

**Core classes:** Micropublication (container), **Claim** (explicit scientific statement class), Statement, SupportGraph (bundles evidence/context/materials), Attribution (author/curator/timestamp), Quotation (source text excerpts), Argument (support/attack/refine/qualify relationships)

**Relationships:** supportsStatement, attacksStatement, refinesStatement, qualifiesStatement enable rich argumentation networks

**Format:** OWL ontology with RDF/Turtle, abstract logic compatible with AI argumentation systems

**Tools:** Domeo annotation tool with micropub plugin, Open Annotation Data Model integration, DIKB (Drug Interaction Knowledge Base)

**Strengths:** **Explicit Claim class** with natural language + optional formalization. Evidence graphs structure reasoning chains. Argumentation transparency via support/attack networks. Quotations anchor to exact source locations. Temporal modeling of claim evolution. Defeasible logic models scientific argument.

**Limitations:** Limited adoption (primarily research prototype, pharmaceutical R&D). No peer review model. No quality metrics beyond argumentation structure. Argument structure ≠ validity assessment—can represent bad arguments well. Manual curation labor-intensive. No automated claim extraction from papers. No conflict of interest tracking. Need to scale from drug interactions to broader HASS domains.

## Domain 3: Research methodology and reproducibility frameworks

### Cochrane Systematic Review Framework

**Organization:** Cochrane Collaboration  
**Scope:** Evidence-based healthcare systematic reviews

Cochrane provides the **gold standard for systematic review methodology** with comprehensive data extraction forms and quality assessment tools refined over decades.

**Data extraction forms:** Customizable templates with study identification, methodology details, population characteristics, interventions, outcomes (primary/secondary), results for meta-analysis, setting/context, funding/conflicts. Closed-ended questions preferred to avoid post-hoc interpretation.

**Risk of Bias 2.0 tool (RoB 2):** Evaluates five domains: randomization process (selection bias), deviations from interventions (performance bias), outcome measurement (detection bias), missing data (attrition bias), selective reporting (reporting bias). Results in Low/Some Concerns/High risk judgment per domain.

**GRADE (Grading of Recommendations):** Four evidence quality levels (Very Low/Low/Moderate/High), two recommendation strengths (Strong/Weak). Considers risk of bias, inconsistency, indirectness, imprecision, publication bias. Explicit rules for downgrading/upgrading.

**Software:** RevMan (Review Manager proprietary), Covidence (web-based), EPPI-Reviewer, GRADEpro GDT, SRDR+ (AHRQ)

**Format:** Primarily Excel/Word/web forms. Some machine-readable exports. Handbook documentation: https://training.cochrane.org/handbook

**Strengths:** Mature methodology with decades of refinement. Explicit quality assessment mechanisms. Standardized across thousands of reviews. Detailed guidance on every step. Methodological Expectations (MECIR) standards ensure consistency.

**Limitations for HASS:** **Heavily RCT-focused**—designed for healthcare interventions. May not accommodate qualitative or mixed-methods research. Less suitable for non-intervention studies. Terminology specific to clinical research. Single-case studies, ethnography, archival research, theoretical contributions don't fit naturally. Adaptation needed for humanities scholarship.

### FAIR Data Principles

**Origin:** GO FAIR Initiative, 2016 Scientific Data publication  
**Adoption:** Increasingly mandated by funders (NIH, EU)

The 15 FAIR principles emphasize **machine-actionability** for Findability, Accessibility, Interoperability, and Reusability of digital research objects.

**Principles:** F1-F4 (globally unique identifiers, rich metadata, registered in searchable resources), A1-A2 (retrievable via standard protocols, metadata persists even when data unavailable), I1-I3 (formal knowledge representation, FAIR vocabularies, qualified references), R1-R1.3 (rich descriptions, clear license, detailed provenance, community standards)

**Implementation schemas:** DataCite Schema, Dublin Core, HCLS Dataset Descriptors, Schema.org, domain-specific minimal information models

**FAIRification process:** Retrieve non-FAIR data → analyze structure → define semantic model → make linkable (Linked Data) → assign license → define metadata → deploy

**Tools:** Dataverse, FAIRsharing.org (registry), FAIR Data Point, Google Dataset Search, various repository platforms (Zenodo, Dryad, Figshare)

**Assessment:** FAIR Data Maturity Model (Research Data Alliance), FAIR Assessment Tools for compliance evaluation

**Strengths:** Comprehensive data lifecycle coverage. Machine-readable by design. Growing adoption and funder mandates. Cross-domain applicability. Strong provenance requirements (R1.2).

**Limitations for HASS:** Highly technical, computational focus—may be over-engineered for smaller projects. Requires significant metadata infrastructure. Implementation complexity barrier. Community standards less developed in some HASS fields. Emphasizes data *availability* and *format*, not content *validity* or *credibility*. No mechanisms for assessing claim quality or methodological rigor.

### repliCATS Project

**Organization:** University of Melbourne, DARPA SCORE program  
**Domain:** Social and behavioral sciences (8 fields)  
**Performance:** 61-84% classification accuracy, 0.94 AUC

repliCATS applies **structured expert judgment** to predict research replicability, providing the closest existing model to HASS credibility assessment needs.

**IDEA Protocol:** Investigate (independent reading + initial estimates) → Discuss (view others' reasoning, interactive dialogue) → Estimate (private revision) → Aggregate (mathematical combination with Bayesian approaches, weighted by forecasting performance)

**Phase 2 assessment (7 credibility signals):** Comprehensibility, Transparency, Plausibility, Validity, Robustness, Replicability, Generalizability—evaluated for 900 claims + 200 papers

**Qualitative coding:** 13,901 justifications coded with inclusion/exclusion criteria. Direct replicability markers (statistical power, effect size, sample) and proxy markers (clarity, prior plausibility, publication venue, author expertise). Inter-coder reliability assessed.

**Format:** Web-based platform with structured elicitation, real-time aggregation, data export (R, CSV), anonymized datasets on OSF

**Strengths:** **Proven for credibility assessment** with validation against actual replications. Captures expert reasoning explicitly. Accommodates uncertainty (three-point estimates). Discussion phase synthesizes diverse perspectives. Applicable to broad claim types. Alternative peer review model.

**Limitations:** Resource-intensive (expert time required). Primarily quantitative research focus—testable hypotheses. Requires domain expertise for each claim. Participant fatigue with scale. Limited to claims with clear replication criteria. Challenging for interpretive/theoretical research where "successful replication" undefined. No automated extraction from papers—manual claim identification.

### PRISMA 2020

**Organization:** PRISMA Group (international)  
**Adoption:** Required by 200+ journals, used for thousands of reviews

PRISMA provides **reporting standards** for systematic reviews with a 27-item checklist and flow diagram, improving transparency and completeness.

**Key sections:** Title (identifies as review) → Structured abstract → Introduction (rationale, objectives) → Methods (13 items: eligibility, sources, search, selection, data collection, risk of bias, synthesis, reporting bias, certainty, registration/protocol) → Results (8 items) → Discussion → Funding

**Flow diagram:** Visual documentation of records identified → screened → excluded (with reasons) → included at each stage

**Extensions:** PRISMA-P (protocols), PRISMA-S (searches), PRISMA-ScR (scoping reviews), PRISMA-IPD (individual patient data), PRISMA-NMA (network meta-analyses), 40+ specialized extensions

**Software:** Integrated in Covidence, RevMan, EPPI-Reviewer. Shiny App for checklist completion: https://prisma.shinyapps.io/checklist/

**Strengths:** Improves reporting quality and transparency. Widely adopted standard. Explicit about exclusions and decisions. Adaptable via extensions. Checklist prevents omissions.

**Limitations for HASS:** Originally healthcare-focused with intervention-centric language. Quantitative emphasis (though improving). Less suitable for pure qualitative synthesis. May require adaptation for humanities research. Reporting guideline, not quality assessment tool—doesn't evaluate *what* was reported, only *that* it was reported.

## Domain 4: Provenance and knowledge representation

### PROV-O (W3C Provenance Ontology)

**Status:** W3C Recommendation 1.0 (2013)  
**Adoption:** Foundation for scientific workflow provenance across domains

PROV-O provides the **standard vocabulary** for provenance, tracking the origins and history of entities through activities and agents.

**Core model (3 classes):** Entity (physical/digital/conceptual things), Activity (how entities created/changed/used), Agent (responsibility for activities)

**Key relationships:** wasGeneratedBy, used (activity used entity), wasDerivedFrom (entity derived from another), wasAttributedTo (agent responsible), wasAssociatedWith (agent associated with activity), actedOnBehalfOf (delegation)

**Qualified patterns:** For detailed provenance: Generation, Usage, Derivation, Attribution, Association, Delegation classes with additional properties (time, location, role)

**Format:** OWL2 ontology with RDF/XML, Turtle, JSON-LD serializations. Namespace: http://www.w3.org/ns/prov#

**Tools:** PROV Toolbox (Java library), ProvStore (repository), ProvValidator, multiple visualization tools

**Strengths:** International standard with broad adoption. Clean conceptual model. Extensible for domain-specific needs. Interoperability across systems. Captures "who, what, when, why, how" of data generation.

**Limitations for HASS claim-evidence-method linkage:** **Lacks argumentation structures**—no claim→evidence→reasoning chains. No claim types or evidence types. No Toulmin model elements (warrant, qualifier, rebuttal). Missing evidence quality/confidence measures or reliability assessments. Weak qualitative methods support—no interview provenance, ethnographic procedure tracking, or archival research chains. No coding provenance for qualitative analysis. Insufficient contextual factors (historical context, cultural setting). Citations not linked to specific claims. No quote→interpretation chains. Designed for computational workflows, not humanistic reasoning.

### ProvONE (Workflow Provenance)

**Developers:** DataONE (2015)  
**Systems:** Taverna, Kepler, Galaxy, VisTrails, Wings/Pegasus

ProvONE extends PROV-O for **prospective + retrospective workflow provenance**, distinguishing templates from executions.

**Prospective (what *could* happen):** Program, Workflow, Port, Channel describe abstract workflow definitions

**Retrospective (what *did* happen):** Execution, ProcessRun, Artifact describe actual runs with inputs/outputs

**Relationships:** hadInPort, hadOutPort (workflow structure), hadPlan (execution→program), wasPartOf (workflow composition)

**Format:** OWL with PROV-O alignment. URL: https://purl.dataone.org/provone-v1-dev

**Strengths:** Enables workflow reproducibility. Clean separation of template vs execution. Cross-system interoperability for computational science. Detailed process tracking.

**Limitations:** Computational workflow-specific. Not applicable to non-computational HASS methods (interviews, archival analysis, textual interpretation, fieldwork). Claims and argumentation not modeled.

### DDI (Data Documentation Initiative)

**Versions:** DDI Codebook 2.5, DDI Lifecycle 3.3  
**Target:** Social science survey/quantitative data  
**Tools:** Colectica, Nesstar, DDI on Rails

DDI provides comprehensive **survey data documentation** covering the full lifecycle from conceptualization through archiving and repurposing.

**Lifecycle phases:** Study concept → data collection design → implementation → data processing → archiving → distribution → discovery → repurposing

**Components:** Conceptual components (universe, concept, variable), data collection (questions, instruments), logical product (variables, categories, codes), physical product (files, records), archive (preservation metadata)

**Format:** XML Schema with complex nested structure. RDF mapping experimental.

**Strengths:** Mature standard for quantitative social science. Captures complex survey designs. Variables linked to concepts. Extensive reuse support. Preservation focus.

**Limitations:** **Primarily quantitative**—survey questionnaires, structured datasets. Limited qualitative/interpretive methods. Weak argumentation support—doesn't model claim-evidence reasoning. No mechanisms for assessing data quality beyond technical validation. Missing: expert judgment provenance, interpretive framework documentation, theory-data linkages.

### OpenAlex / SemOpenAlex

**Scale:** 209M+ works, 201M+ authors, 124K venues, 109K institutions, 2.5B+ citations  
**License:** CC0 (public domain)  
**SPARQL:** SemOpenAlex (26B triples)

OpenAlex provides a massive **knowledge graph for scientific literature**, replacing Microsoft Academic Graph with citation networks and author disambiguation.

**Format:** JSON via REST API with full data dumps. SemOpenAlex adds RDF representation with Schema.org, FOAF, Dublin Core ontologies.

**Features:** Citation networks, author disambiguation, concept classification (hierarchical taxonomy), affiliation tracking, open access status, funding information

**Access:** https://openalex.org/ with generous rate limits

**Strengths:** Enormous scale enables bibliometric analysis. Open data (CC0). Citation contexts extracted. Regular updates. Author disambiguation quality. Free access.

**Limitations:** **No formal knowledge representation** in base OpenAlex (JSON, not RDF ontology). Claims not modeled—papers as black boxes. Citation counts only quality signal, not validity measure. No peer review data. No retraction tracking. Search-focused, not analysis-focused. Doesn't extract or verify claims within papers. SemOpenAlex adds structure but still lacks claim-level granularity.

## Domain 5: Legal reasoning frameworks

### Carneades Argumentation System

**Developers:** Thomas Gordon (Fraunhofer FOKUS), Douglas Walton (Windsor), 2006-2007  
**Software:** http://carneades.github.com/ (open source, 4 versions)

Carneades provides **computational legal argumentation** with graduated proof standards and explicit burden of proof allocation—highly applicable to research claim evaluation.

**Structure:** Argument graphs with statement nodes + argument nodes. Pro arguments (support) vs con arguments (attack). Arguments instantiate argumentation schemes with three premise types: ordinary (must prove), assumptions (accepted unless challenged), exceptions (must disprove if raised).

**Five proof standards per statement:**  
1. Scintilla of evidence—any pro argument suffices  
2. Preponderance—max pro weight \> max con weight  
3. Clear \u0026 convincing—max pro substantially \> max con  
4. Beyond reasonable doubt—max pro meets threshold AND no con arguments  
5. Dialectical exhaustion—all possible arguments evaluated

**Burden of proof:** Allocated **per-premise** (not just per-conclusion). Burden of production (present evidence) vs persuasion (convince audience). Can differ for different premises of same argument. Shifts through dialogue stages.

**Quality:** Argument weights (0.0-1.0) represent audience acceptance based on credibility, reliability, corroboration.

**Features:** Argument visualization, interactive construction, case analysis, knowledge base integration, forward/backward/abductive reasoning, generates Dung-style frameworks

**Strengths:** **Graduated standards match research contexts** better than binary. Explicit burden allocation models who must justify claims. Scheme-based construction guides valid reasoning. Weights enable credibility modeling. Visualization aids understanding. Open source with active development.

**Applicability to research:** Preponderance for exploratory claims, clear \u0026 convincing for policy recommendations, beyond reasonable doubt for causal mechanisms. Different burdens for theoretical assumptions vs empirical observations.

**Limitations:** Still adversarial framing (though less than law). Manual argument construction required. Weight assignment subjective. Doesn't capture statistical evidence naturally. No direct integration with research data.

### LKIF (Legal Knowledge Interchange Format)

**Origin:** European ESTRELLA Project (2004-2008)  
**Software:** https://github.com/RinkeHoekstra/lkif-core (15 OWL modules)

LKIF provides **15 modular ontologies** for representing legislation, cases, and justificatory arguments with defeasible reasoning.

**Modules:** Top, Place, Mereology, Time, Spacetime (abstract); Process, Role, Action (basic); Expression (propositions); Legal-Action, Legal-Role, Norm, Modification, Rules \u0026 Argumentation (legal); LKIF-Core (integration)

**Format:** OWL-DL + SWRL with XML Schema for arguments. Axioms (certain) + defeasible rules (presumptive). Preference orderings: extensional (explicit priorities) and intensional (meta-rules like lex posterior).

**Evidence-inference:** Statements with dialectical status (stated, questioned, accepted, rejected). Arguments from premises, assumptions, exceptions. Proof standards attached.

**Tools:** Integration with Carneades, MetaLex XML, LegalRuleML, OWL Judge

**Strengths:** Highly modular and compositional. Formal logical representation. Explicit conflict resolution. Reusable across legal systems. Defeasibility built-in.

**Applicability:** Adaptable to policy analysis, regulatory compliance, normative reasoning in ethics/philosophy research.

**Limitations:** Includes deontic logic (obligations, permissions) less relevant to empirical science. Legal interpretation (teleological) differs from empirical. Requires expertise to instantiate. No explicit credibility assessment beyond logical consistency.

### Wigmore Evidence Charts

**Origin:** John Henry Wigmore (1913, 1937), Northwestern Law School

Wigmore charts provide **graphical analysis of complex evidence** through directed acyclic graphs showing inferential chains from evidence to ultimate conclusions.

**Structure:** Rectangles = facts, circles = testimony, lines = inferences. Hierarchical: evidence (leaves) → intermediate inferences → ultimate probanda (root). Shows corroboration and contradiction explicitly.

**Quality:** Based on "common course of events" generalizations. Inductive probability graded by resistance to falsification—tests/challenges survived measure strength.

**Modern equivalents:** Similar to Bayesian Networks but with qualitative reasoning

**Applicability:** Complex evidence synthesis in systematic reviews, meta-analysis structure, tracking how multiple studies support/contradict claims

**Limitations:** Largely manual/paper-based historically. No standardized digital format. Limited computational implementations (Anderson, Schum \u0026 Twining reconstructions). Binary outcomes and time-bounded decisions differ from open-ended scientific inquiry.

### Walton Argumentation Schemes

**Origin:** Douglas Walton with Reed \u0026 Macagno, building on Aristotle  
**Catalog:** 60+ schemes

Walton schemes provide a **comprehensive catalog** of common argument patterns, each with premises, conclusion, and critical questions for evaluation.

**Categories:** Source-based (expert opinion, witness testimony, position to know), reasoning (analogy, generalization, sign, cause-effect), practical (consequences, values, precedent), rule-based (rules, established rules, exception)

**Example—Argument from Expert Opinion:**  
Premises: E is expert in D, E asserts A, A is in D  
Conclusion: A (presumptively)  
Critical questions: Is E truly expert? Is D relevant field? Is A within E's expertise? Is E trustworthy? Are experts consistent? Is A backed by evidence?

**Implementations:** Integrated in Carneades, ArguMed, Araucaria, OVA, various AI systems

**Strengths:** **Extremely transferable**—designed for general use across domains. Critical questions target key assumptions. Empirical grounding in actual arguments. Dialectical testing framework. Identifies implicit warrants.

**Applicability to research:** Argument from Expert Opinion (peer review), Argument from Sign (correlational evidence), Argument from Cause to Effect (mechanisms), Argument from Analogy (comparative methods), Argument from Generalization (sampling studies)

**Limitations:** Requires mapping research arguments to schemes. Critical questions need domain-specific instantiation. Doesn't provide answers, only evaluation framework. No built-in quality metrics—relies on human judgment.

## Comparative analysis: Component extraction and synthesis

### Claim modeling approaches

| Schema | Claim Representation | Granularity | Relationships | Credibility Support |
|--------|---------------------|-------------|---------------|---------------------|
| **Micropublications** | Explicit Claim class | Single assertion | Support/attack/refine/qualify | Argumentation structure |
| **Nanopublications** | Assertion graph | Triple-level | Provenance links | Immutable identifiers |
| **IBM Debater** | Context-dependent claims | Sentence-level | Stance (pro/con) | Quality scores (0-1) |
| **Toulmin** | Central claim component | Argument-level | Warrant-linked to data | Qualifiers (certainty) |
| **AIF** | I-nodes | Propositional | S-nodes (inference/conflict) | Preference schemes |
| **SPAR/DoCO** | Implicit in sections | Section-level | Citation types (CiTO) | None directly |

**Best for HASS:** Micropublications explicit Claim class with support graphs, extended with Nanopublications' provenance and IBM Debater's quality scoring.

### Evidence representation

| Schema | Evidence Type | Structure | Source Tracking | Quality Assessment |
|--------|--------------|-----------|-----------------|-------------------|
| **PROV-O** | Entity | Derivation chains | Agent attribution | None |
| **Research Objects** | Artifact | Workflow outputs | Complete provenance | Re-executability |
| **Cochrane** | Study data | Structured forms | Risk of Bias tool | GRADE levels |
| **repliCATS** | Results/methods | Qualitative coding | Paper metadata | 7 credibility signals |
| **Carneades** | Premises | Typed (ordinary/assumption/exception) | Argument weights | Proof standards |
| **Legal standards** | Admissible evidence | 3D (admissibility/weight/sufficiency) | Chain of custody | Multiple standards |

**Best for HASS:** Combine PROV-O derivation with Cochrane Risk of Bias assessment, repliCATS credibility signals, and Carneades weights. Evidence types from legal frameworks (direct/circumstantial, primary/secondary sources).

### Methods description

| Schema | Methods Capture | Procedural Detail | Reproducibility | Domain Coverage |
|--------|----------------|-------------------|-----------------|-----------------|
| **Research Objects** | Workflow templates | Step-by-step | Executable | Computational only |
| **DDI** | Survey instruments | Question-level | Reusable | Quantitative surveys |
| **CONSORT** | Trial methodology | Detailed checklist | Protocol registration | RCTs only |
| **GROBID** | Methods sections | Section extraction | No interpretation | Cross-domain |
| **ReproNim** | Neuroimaging pipelines | Complete specification | Re-executable | Neuroimaging |

**Gaps for HASS:** No framework captures qualitative methods well (interviews, ethnography, archival research, textual analysis, participant observation). Needed: interview protocols, sampling strategies, coding procedures, reflexivity documentation, triangulation approaches.

### Claim-evidence-method linkages

| Schema | Links Claims? | Links Evidence? | Links Methods? | Integrated? |
|--------|---------------|-----------------|----------------|-------------|
| **Micropublications** | Yes | Yes (support graphs) | Partial | Claims+evidence |
| **SPAR (DoCO+CiTO)** | Implicit | Yes (citations) | Section-based | Structure only |
| **Research Objects** | No | Yes (artifacts) | Yes (workflows) | Methods+data |
| **repliCATS** | Yes | Yes (qualitative) | Yes (assessment) | All three |
| **Toulmin** | Yes | Yes (grounds) | No | Claims+evidence |
| **PROV-O** | No | Yes (entities) | Yes (activities) | Data+process |

**Critical finding:** **No schema integrates all three comprehensively with credibility assessment.** repliCATS closest but manual/qualitative. Research Objects strong on methods+data, weak on claims. Micropublications strong on claims+evidence, weak on methods.

### Credibility and quality mechanisms

| Schema | Quality Metrics | Assessment Type | Validation | Peer Review |
|--------|----------------|-----------------|------------|-------------|
| **Cochrane RoB/GRADE** | Explicit levels | Domain-based | Manual expert | Implied |
| **IBM Debater** | Neural scores (0-1) | Holistic | Trained on 30K | No |
| **repliCATS** | 7 signals + probability | Multi-dimensional | Validated on replications | Alternative to |
| **FAIR** | Maturity model | Compliance | Automated checks | No |
| **Legal standards** | Proof standards | Context-dependent | Adversarial testing | No |
| **Nanopublications** | None | N/A | Cryptographic only | No |
| **SPAR (BiDO)** | Citations, h-index | Impact-based | Bibliometric | No |

**Major gap:** Almost all schemas lack integrated credibility assessment. Cochrane and repliCATS exceptions, but domain-specific (healthcare RCTs, quantitative replication).

## Gap analysis: What's missing for HASS credibility assessment

### Methodological gaps

**1. Qualitative methods representation**

No schema adequately captures:
- **Interview methods:** Sampling strategies, interview protocols, consent procedures, recording/transcription methods, member checking
- **Ethnographic procedures:** Fieldwork duration, participant observation roles, field notes practices, reflexivity documentation
- **Archival research:** Archive selection, document sampling, source criticism procedures, contextualization methods
- **Textual analysis:** Close reading procedures, coding frameworks, inter-coder reliability, interpretation documentation
- **Mixed methods:** Integration strategies, triangulation procedures, sequential vs concurrent designs

**2. Single-case to generalization patterns**

Abductive reasoning from cases to theory poorly modeled:
- How single case studies support theoretical claims
- Generalization logic from qualitative samples
- Thick description as evidence type
- Exemplar-based reasoning
- Pattern matching across cases

**3. Professional judgment vs observation boundaries**

Missing distinction between:
- Direct observations (primary data)
- Expert interpretations (secondary analysis)
- Theoretical inferences (tertiary claims)
- Implicit assumptions underlying each

### Structural gaps

**4. Methods-results linkages for reproducibility**

Weak connections between:
- Specific methodological choices and results obtained
- Parameter variations and outcome sensitivity
- Missing details that prevent replication
- Sufficient vs insufficient methodological detail

**5. Cross-sectional claim synthesis**

Claims spanning multiple paper sections not captured:
- Introduction hypothesis + Methods procedures + Results data + Discussion interpretation as integrated claim
- Background literature + current findings synthesis
- Implicit arguments assembled across sections

**6. Implicit arguments and unstated assumptions**

Warrants, background assumptions, and implicit reasoning chains unmodeled:
- Disciplinary assumptions taken as given
- Theoretical frameworks as unstated warrants
- Methodological paradigms (positivist/interpretivist/critical)
- Value commitments shaping research design

### Evidence and credibility gaps

**7. Evidence strength quantification**

No systematic approach to:
- Weighting different evidence types (statistical, observational, testimonial, archival, experimental)
- Assessing evidential support degree (strong/moderate/weak/insufficient)
- Triangulation documentation (multiple sources converging)
- Contradictory evidence handling

**8. Source credibility assessment**

Limited mechanisms for:
- Author expertise evaluation
- Institutional credibility
- Publication venue reputation (beyond impact factor)
- Funding source influence
- Conflict of interest documentation
- Retraction/correction history

**9. Temporal validity and knowledge evolution**

Missing:
- Claims' shelf life and updating
- Consensus shifts over time
- Cumulative evidence tracking
- Superseded vs current findings

**10. Uncertainty representation**

Inadequate handling of:
- Confidence intervals and statistical uncertainty
- Epistemic uncertainty (knowledge gaps)
- Linguistic hedging ("may," "suggests," "possibly")
- Acknowledged limitations
- Boundary conditions for claims

### Integration gaps

**11. Cross-document claim tracking**

No framework for:
- Same claim across multiple papers
- Claim evolution through research programs
- Supporting vs contradicting replications
- Meta-analytic evidence synthesis
- Consensus vs controversy identification

**12. Argumentation-provenance integration**

Separated in current schemas:
- PROV-O tracks data provenance but not claim structure
- AIF models arguments but not data lineage
- Need: Combined system where claims have both argumentative structure AND provenance chains

**13. Peer review and validation process**

Almost entirely missing:
- Reviewer comments and revisions
- Pre-registration vs post-hoc analysis
- Registered Reports workflow
- Post-publication peer review
- Retraction reasons and affected claims

## Recommendations: Schema development strategies

### Option 1: Use existing schema as-is

**Not recommended** for HASS credibility assessment. While individual schemas have strengths, none provides sufficient coverage. SPAR excellent for bibliographic infrastructure but lacks claim-level granularity. PROV-O strong for data provenance but missing argumentation. Cochrane comprehensive for RCTs but not transferable to interpretive research.

### Option 2: Adapt single existing schema

**Candidate:** Micropublications Ontology  
**Rationale:** Explicit Claim class, evidence graphs, argumentation relationships  
**Required extensions:**
- Add PROV-O properties for data provenance
- Integrate Cochrane-style quality assessment
- Add qualitative methods classes
- Include repliCATS credibility signals
- Add peer review/validation classes

**Effort:** Moderate. Ontology extensible but limited current adoption means building ecosystem.

### Option 3: Assemble components from multiple schemas (RECOMMENDED)

**Strategy:** Modular composition drawing best components from each domain

**Core architecture:**

**Layer 1 (Foundation):** PROV-O for data provenance  
- Provides standard vocabulary (Entity, Activity, Agent)
- Widely adopted with tool support
- Extends with domain-specific classes

**Layer 2 (Document structure):** SPAR (DoCO) for paper sections  
- Identifies Methods, Results, Discussion sections
- CiTO for citation typing
- FaBiO for publication metadata
- Provides structural scaffolding

**Layer 3 (Claims):** Micropublications for explicit claims  
- Claim class with attribution
- Support/attack relationships
- Quotations anchoring to source text
- Add claim types: Descriptive, Causal, Interpretive, Evaluative, Theoretical

**Layer 4 (Evidence):** Hybrid approach  
- Evidence class as PROV-O Entity subclass
- Types: Primary source, Secondary source, Statistical, Observational, Testimonial, Archival, Experimental, Theoretical
- Properties: evidenceFor (links to claims), evidenceStrength (weak/moderate/strong), sourceCredibility, triangulatedBy

**Layer 5 (Methods):** Research Object concepts + qualitative methods  
- Process class for procedures
- MethodType: Quantitative, Qualitative, Mixed, Computational, Archival, Experimental, Ethnographic, Comparative
- Subclasses for specific methods with appropriate properties

**Layer 6 (Argumentation):** AIF + Carneades  
- Scheme nodes for inference patterns
- Walton schemes as instances
- Proof standards from Carneades
- Burden of proof allocation

**Layer 7 (Quality assessment):** repliCATS + Cochrane + legal standards  
- CredibilityAssessment class with 7+ signals
- RiskOfBias for methodological quality
- EvidenceQuality levels (GRADE-style)
- ProofStandard for claim acceptance thresholds

**Layer 8 (Validation):** Peer review and replication  
- PeerReview class (comments, revisions, acceptance)
- Replication class (successful/failed/partial)
- Retraction class (reasons, affected claims)
- Preregistration/protocol links

**Interoperability:**
- Map to Schema.org for web visibility
- Export to JATS XML for publishers
- RDF/OWL for semantic web
- JSON-LD for practical implementation

**Borrowed elements summary:**

| Schema | Components Borrowed | Why |
|--------|-------------------|-----|
| PROV-O | Core provenance model | W3C standard, tool support |
| SPAR | Document structure, citations | Deployed at scale, publishers |
| Micropublications | Explicit claims, support graphs | Best claim modeling |
| Research Objects | Workflow concepts | Computational reproducibility |
| AIF | Inference schemes, attack/support | Formal argumentation |
| Carneades | Proof standards, burden of proof | Graduated credibility |
| Cochrane | Risk of bias, GRADE | Evidence quality proven |
| repliCATS | Credibility signals | Validated for prediction |
| Walton | Argumentation schemes | 60+ patterns, critical questions |
| Nanopublications | Immutable identifiers | Citation granularity |

### Option 4: Build new schema with specific borrowed elements

**Only if:** Modular composition proves too complex or performance issues arise

**Strategy:** Design purpose-built ontology learning from existing schemas but optimized for HASS credibility

**Core commitments:**
- Claims as first-class objects (from Micropublications)
- Evidence types matching HASS needs (qualitative, archival, textual)
- Methods taxonomy for HASS disciplines
- Explicit credibility assessment (inspired by repliCATS)
- Argumentation structure (simplified from AIF)
- Provenance integration (PROV-O patterns)

**Trade-off:** Clean design, optimized for use case, but loses interoperability with existing systems and requires building full ecosystem.

## Trade-offs: Formal ontology vs practical JSON schema

### Formal ontology approach (OWL/RDF)

**Advantages:**
- Semantic precision with formal logic
- Reasoning capabilities (infer new facts)
- Interoperability via Linked Data
- Tool ecosystem (reasoners, validators, SPARQL)
- Academic credibility in KR community
- Modular composition via imports

**Disadvantages:**
- Steep learning curve for users
- Verbosity in representation
- Performance overhead for large datasets
- Limited integration with mainstream tools
- Requires specialized expertise
- Ontology engineering complexity

**Best for:** Research with strong semantic requirements, integration with existing LOD, formal reasoning needs, cross-system interoperability

### Practical JSON Schema approach

**Advantages:**
- Ubiquitous format understood by developers
- Excellent tool support (validators, editors)
- Lightweight and fast
- Easy integration with web services/APIs
- Lower barrier to adoption
- Straightforward documentation

**Disadvantages:**
- No formal semantics
- Limited reasoning capabilities
- Less precise (string vs URI)
- Weaker interoperability
- Difficult to extend/compose
- No standard query language (vs SPARQL)

**Best for:** Practical deployment, web applications, broad adoption goals, rapid prototyping, when formal semantics not critical

### Hybrid recommendation: JSON-LD

**Rationale:** JSON-LD provides **best of both worlds**—JSON's practicality with RDF's semantics.

**Benefits:**
- Valid JSON (works with existing tools)
- RDF semantics via @context
- Upgradeable (JSON → JSON-LD → RDF)
- Progressive enhancement
- Schema.org uses this approach
- Growing adoption (Google Dataset Search)

**Structure:**
```json
{
  "@context": {
    "claim": "https://hass-credibility.org/vocab#Claim",
    "evidence": "https://hass-credibility.org/vocab#evidence",
    "supports": "https://hass-credibility.org/vocab#supports",
    "method": "https://hass-credibility.org/vocab#Method",
    "credibility": "https://hass-credibility.org/vocab#credibility"
  },
  "@type": "claim",
  "text": "Social media increases political polarization",
  "claimType": "Causal",
  "evidence": [
    {
      "@type": "Evidence",
      "source": "doi:10.xxxx/yyyy",
      "evidenceType": "Statistical",
      "strength": "strong"
    }
  ],
  "method": {
    "@type": "Method",
    "methodType": "Longitudinal survey",
    "sampleSize": 2500
  },
  "credibility": {
    "overallScore": 0.82,
    "transparency": 0.9,
    "validity": 0.8,
    "replicability": 0.75
  }
}
```

**Implementation path:**
1. Define JSON Schema for validation
2. Add JSON-LD @context for semantics
3. Map to OWL ontology for reasoning
4. Provide both JSON and RDF serializations
5. Tools accept/produce either format

## Practical next steps for schema development

### Phase 1: Foundation (Months 1-3)

**Task 1.1:** Convene expert working group  
- Representation: HASS disciplines, information science, computer science, research methodology
- Review this report and prioritize components
- Define core requirements and use cases

**Task 1.2:** Map existing schemas in detail  
- Formal mapping between PROV-O, SPAR, Micropublications, AIF
- Identify overlaps and conflicts
- Create alignment ontology

**Task 1.3:** Draft core ontology modules  
- Claim module (types, properties, relationships)
- Evidence module (types, quality, provenance)
- Method module (qualitative, quantitative, mixed)
- Start with JSON Schema + JSON-LD @context

**Task 1.4:** Develop exemplar annotations  
- Annotate 10-20 papers from diverse HASS disciplines
- Test schema expressiveness and identify gaps
- Iterate on schema design

### Phase 2: Extension (Months 4-6)

**Task 2.1:** Add argumentation layer  
- Integrate AIF schemes and Carneades proof standards
- Define inference patterns common in HASS
- Add Walton schemes relevant to HASS (expert opinion, analogy, generalization)

**Task 2.2:** Add credibility assessment layer  
- Adapt repliCATS 7 signals for HASS
- Define domain-specific quality indicators
- Create assessment rubrics per discipline

**Task 2.3:** Add methods taxonomy  
- Comprehensive qualitative methods (interviews, ethnography, archival, textual)
- Mixed methods designs
- Computational methods for digital humanities
- Methodological quality indicators

**Task 2.4:** Develop validation classes  
- Peer review process model
- Replication/reproducibility tracking
- Retraction and correction handling
- Pre-registration integration

### Phase 3: Tooling (Months 7-9)

**Task 3.1:** Annotation tool development  
- Web-based interface for annotating papers
- Integration with PDF readers
- Semi-automated extraction (leverage GROBID, SciBERT)
- User-friendly for non-technical scholars

**Task 3.2:** Validation and query tools  
- JSON Schema validators
- SHACL shapes for RDF validation
- SPARQL query templates for common questions
- Credibility score calculators

**Task 3.3:** Visualization tools  
- Argument maps showing claim-evidence-method links
- Provenance visualizations
- Credibility dashboards
- Citation network integration

**Task 3.4:** Integration with existing infrastructure  
- GROBID extraction pipeline
- SciBERT for claim/evidence classification
- OSF for storage and sharing
- Zotero/Mendeley for reference managers
- ORCID for attribution

### Phase 4: Evaluation (Months 10-12)

**Task 4.1:** Pilot with research projects  
- Partner with 5-10 HASS research teams
- Annotate their papers and datasets
- Gather usability feedback
- Measure annotation time and inter-annotator agreement

**Task 4.2:** Automated extraction evaluation  
- Train ML models on annotated corpus
- Measure extraction accuracy (claims, evidence, methods)
- Compare to baselines (SciBERT, PubMed RCT models)
- Identify difficult cases

**Task 4.3:** Credibility prediction validation  
- Use schema-based features to predict replication outcomes
- Compare to repliCATS performance
- Analyze which features most predictive
- Validate against expert judgments

**Task 4.4:** Community feedback and revision  
- Present at disciplinary conferences
- Gather feedback from potential users
- Revise schema based on real-world use
- Document lessons learned

### Phase 5: Deployment (Months 13-18)

**Task 5.1:** Public release  
- Publish ontology/schema on GitHub
- Register persistent URIs (w3id.org or similar)
- Create comprehensive documentation
- Provide tutorials and examples

**Task 5.2:** Tool ecosystem  
- Release annotation tool as open source
- Provide Python/R libraries
- Create API for validation services
- Develop plugins for common platforms

**Task 5.3:** Corpus creation  
- Annotate 500-1000 papers across HASS disciplines
- Release as benchmark dataset
- Enable reproducible evaluation
- Support training ML models

**Task 5.4:** Community building  
- Organize workshops
- Create user forum
- Establish governance structure
- Develop maintenance plan

### Immediate first steps (This month)

**Week 1-2:** 
- Share this report with key stakeholders
- Form small core team (3-5 people)
- Set up infrastructure (GitHub repo, Slack/Discord, Google Drive)
- Define decision-making process

**Week 3-4:**
- Draft initial JSON Schema for core classes (Claim, Evidence, Method)
- Create 5-10 example annotations manually
- Identify any showstopper issues
- Schedule first working group meeting

**Success metrics:**
- Schema expressiveness (can represent 90%+ of HASS claims)
- Annotation speed (\<30 min per paper after training)
- Inter-annotator agreement (\>0.7 kappa)
- Extraction accuracy (\>0.75 F1 for claims/evidence)
- Adoption (50+ researchers using within 2 years)

## Conclusion: Toward an integrated schema for HASS credibility

The landscape of existing schemas provides rich components but no integrated solution. **The path forward combines the best elements from each domain into a modular, extensible framework.** Start with proven foundations (PROV-O, SPAR), add explicit claim modeling (Micropublications), integrate argumentation (AIF, Carneades), incorporate credibility assessment (repliCATS, Cochrane), and extend for HASS methods.

The JSON-LD approach balances practical adoption with semantic precision. Immediate action should focus on core ontology development, exemplar annotations, and tool prototyping. Success requires sustained community engagement across HASS disciplines, information science, and computer science.

The prize is significant: **a standard framework enabling systematic credibility assessment, automated extraction, cross-study synthesis, and reproducible research at scale**. This infrastructure could transform scholarly communication from opaque publications to transparent, machine-readable knowledge graphs where claims, evidence, methods, and quality are explicitly linked and rigorously evaluated.