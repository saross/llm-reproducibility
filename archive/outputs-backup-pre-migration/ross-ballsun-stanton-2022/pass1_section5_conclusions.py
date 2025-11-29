#!/usr/bin/env python3
"""
Pass 1: Liberal Claims & Evidence Extraction
Section Group 5: Slow Archaeology + Conclusions
Pages: 11-13 (PDF pages, sections 5-6)

Extraction Strategy:
- Evidence from Ocean Health Index project
- Claims about slow archaeology
- Synthesis claims about preregistration value
- Claims about data quality and future requirements
- Concluding arguments

Word count estimate: ~1400 words
"""

import json
from datetime import datetime

# Load existing extraction
with open('outputs/ross-ballsun-stanton-2022/extraction.json', 'r') as f:
    data = json.load(f)

# Section Group 5: Slow Archaeology + Conclusions
# Pages 11-13 of PDF

# ============================================================================
# EVIDENCE ITEMS
# ============================================================================

evidence_items = [
    {
        "id": "E014",
        "content": "The Ocean Health Index project discovered that environmental scientists are expected to work with highly heterogeneous data but are seldom formally trained to do so, leading to bespoke workarounds that result in non-reproducible work.",
        "evidence_type": "case_study",
        "source_type": "published_research",
        "verbatim_quote": "Environmental scientists are expected to work effectively with ever-increasing quantities of highly heterogeneous data even though they are seldom formally trained to do so... Without training, scientists tend to develop their own bespoke workarounds to keep pace, but with this comes wasted time struggling to create their own conventions for managing, wrangling and versioning data. If done haphazardly or without a clear protocol, these efforts are likely to result in work that is not reproducible - by the scientist's own 'future self' or by anyone else.",
        "page_number": 11-12,
        "context": "Ocean Health Index lessons for archaeology",
        "interpretation_notes": "Parallel discipline (oceanography) faced similar small data problems as archaeology"
    },
    {
        "id": "E015",
        "content": "The Ocean Health Index project's response to scalability and reproducibility was implementing data collection, manipulation, and analysis techniques based on open data formats, data standardisation, and script-based analysis with shareable script libraries.",
        "evidence_type": "case_study",
        "source_type": "published_research",
        "verbatim_quote": "The Ocean Health Index project's response to scalability and reproducibility was to implement data collection, manipulation, and analysis techniques based on open data formats, data standardization, and script-based analysis. Then, they created libraries of scripts that could perform commonly required analyses on well-structured data.",
        "page_number": 12,
        "context": "Solution from oceanography",
        "interpretation_notes": "Demonstrates successful approach to similar problems in related field"
    }
]

# ============================================================================
# CLAIMS ITEMS
# ============================================================================

claims_items = [
    {
        "id": "C096",
        "content": "The discipline of oceanography has grappled with small data problems including diverse data structures emerging from fieldwork, producing internally inconsistent datasets and mid-course research changes.",
        "claim_type": "empirical",
        "reasoning_type": "analogical",
        "evidence_links": ["E014"],
        "verbatim_quote": "The discipline of oceanography has also grappled with 'small data' problems (Borgman 2015; Kansa and Bissell 2010), including diverse data and data structures that emerge from fieldwork, producing internally inconsistent datasets and mid-course changes to research.",
        "page_number": 11,
        "context": "Opening of Section 5, establishing analogy",
        "certainty_qualifier": "documented in literature"
    },
    {
        "id": "C097",
        "content": "Oceanography's small data problems include those that shade into questionable research practices, judging from Fraser et al.'s survey of related disciplines.",
        "claim_type": "empirical",
        "reasoning_type": "analogical",
        "evidence_links": [],
        "verbatim_quote": "These problems include those that shade into questionable research practices, judging from Fraser et al.'s (Fraser et al. 2018) survey of related disciplines.",
        "page_number": 11,
        "context": "Connecting to earlier HARKing discussion",
        "certainty_qualifier": "inferred from related fields"
    },
    {
        "id": "C098",
        "content": "Oceanography's problems inhibited large-scale synthetic research needed to address grand challenges, paralleling archaeology's situation.",
        "claim_type": "empirical",
        "reasoning_type": "analogical",
        "evidence_links": [],
        "verbatim_quote": "As in archaeology, these problems inhibited the large-scale, synthetic research needed to address grand challenges in oceanography.",
        "page_number": 11,
        "context": "Parallel with archaeology",
        "certainty_qualifier": "explicit comparison"
    },
    {
        "id": "C099",
        "content": "In the Ocean Health Index project, increases in data quantity and improving data quality were functions of reducing friction, avoiding technical debt, and implementing requirements around data formats, structures, and analytical methods.",
        "claim_type": "empirical",
        "reasoning_type": "causal",
        "evidence_links": ["E015"],
        "verbatim_quote": "Increases in the quantity of available data and improving data quality were functions of reducing friction, avoiding technical debt, and implementing requirements around data formats, data structures, and analytical methods.",
        "page_number": 12,
        "context": "Ocean Health Index success factors",
        "certainty_qualifier": "causal claim from case study"
    },
    {
        "id": "C100",
        "content": "More important than generating standardised data and scripts was the thoughtful and planned research design, including approach to creating, recording, and analysing data.",
        "claim_type": "evaluative",
        "reasoning_type": "comparative",
        "evidence_links": ["E015"],
        "verbatim_quote": "More important than the generation of standardized, reusable data and scripts, however, was the thoughtful and planned research design, including its approach to creating, recording, and analyzing data.",
        "page_number": 12,
        "context": "Key lesson from Ocean Health Index",
        "certainty_qualifier": "evaluative judgement"
    },
    {
        "id": "C101",
        "content": "Careful planning aligns with both early processualists' call for a priori research design and Caraher's argument for slow archaeology.",
        "claim_type": "theoretical",
        "reasoning_type": "synthetic",
        "evidence_links": ["E005"],
        "verbatim_quote": "Such careful planning not only aligns with the early processualists' call for more emphasis on thoughtful, a priori research design, but also with Caraher's recent argument for a 'slow archaeology'",
        "page_number": 12,
        "context": "Connecting multiple theoretical traditions",
        "certainty_qualifier": "synthetic claim"
    },
    {
        "id": "C102",
        "content": "Slow archaeology evokes practice of archaeology as a craft, prioritising embodied attentiveness to the entire fieldwork process as challenge to fragmented perspectives offered by efficient, industrialised workflows.",
        "claim_type": "theoretical",
        "reasoning_type": "conceptual",
        "evidence_links": [],
        "verbatim_quote": "Slow archaeology evokes the practice of archaeology as a craft. It prioritizes an embodied attentiveness to the entire process of fieldwork as a challenge to the fragmented perspectives offered by workflows influenced by our own efficient, industrialized age",
        "page_number": 12,
        "context": "Caraher quote defining slow archaeology",
        "certainty_qualifier": "cited from Caraher"
    },
    {
        "id": "C103",
        "content": "Preregistration and associated digital approaches supporting transparency and reproducibility are not antithetical to slow archaeology - the chaos of just-in-time approaches to fieldwork are.",
        "claim_type": "theoretical",
        "reasoning_type": "conceptual",
        "evidence_links": [],
        "verbatim_quote": "Preregistration and associated digital approaches that support transparency and reproducibility are not antithetical to slow archaeology – the chaos of 'just-in-time' approaches to fieldwork are.",
        "page_number": 12,
        "context": "Reconciling preregistration with slow archaeology",
        "certainty_qualifier": "strong assertion"
    },
    {
        "id": "C104",
        "content": "Under-planned fieldwork might offer more freedom and delay reckoning with messy data, but represents the opposite of the considered approach suggested by Caraher and is likely to result in biased and opaque research not reaching full potential.",
        "claim_type": "evaluative",
        "reasoning_type": "normative",
        "evidence_links": [],
        "verbatim_quote": "Under-planned fieldwork might offer more freedom (and delay the day of reckoning with messy data), but it represents the opposite of the considered approach suggested by Caraher and is likely to result in biased and opaque research that does not reach its full potential.",
        "page_number": 12,
        "context": "Critique of under-planning",
        "certainty_qualifier": "evaluative with modal qualifier"
    },
    {
        "id": "C105",
        "content": "Preregistration encourages thoughtfulness.",
        "claim_type": "methodological",
        "reasoning_type": "conceptual",
        "evidence_links": [],
        "verbatim_quote": "Preregistration encourages thoughtfulness.",
        "page_number": 12,
        "context": "Simple summary claim",
        "certainty_qualifier": "strong statement"
    },
    {
        "id": "C106",
        "content": "Calls for archaeologists to improve data quality for large-scale research have been made for at least two decades but limited progress has been made.",
        "claim_type": "empirical",
        "reasoning_type": "observational",
        "evidence_links": [],
        "verbatim_quote": "Calls for archaeologists to improve data quality for large-scale research have been made for at least the past two decades (Doerr et al. 2004; Kansa and Kansa 2011; Faniel et al. 2013; Austin 2014), but limited progress has been made (Kintigh et al. 2014; Sobotkova 2018).",
        "page_number": 12-13,
        "context": "Opening of Section 6 (Conclusions)",
        "certainty_qualifier": "documented in literature"
    },
    {
        "id": "C107",
        "content": "Concerns over transparency and reproducibility of archaeological research are more recent than data quality concerns.",
        "claim_type": "empirical",
        "reasoning_type": "observational",
        "evidence_links": [],
        "verbatim_quote": "Concerns over the transparency and reproducibility of archaeological research are more recent (Marwick 2017b)",
        "page_number": 13,
        "context": "Distinguishing two types of concerns",
        "certainty_qualifier": "temporal observation"
    },
    {
        "id": "C108",
        "content": "Archaeology is unlikely to avoid the reproducibility crisis so profoundly affecting other disciplines.",
        "claim_type": "empirical",
        "reasoning_type": "predictive",
        "evidence_links": ["E001"],
        "verbatim_quote": "archaeology is unlikely to avoid the reproducibility crisis so profoundly affecting other disciplines.",
        "page_number": 13,
        "context": "Prediction about archaeology's future",
        "certainty_qualifier": "unlikely (modal qualifier)"
    },
    {
        "id": "C109",
        "content": "The recommendation to adopt preregistration as a means of increasing rigour is a pathway to solving challenges of data quality and reproducibility.",
        "claim_type": "methodological",
        "reasoning_type": "prescriptive",
        "evidence_links": [],
        "verbatim_quote": "Our recommendation to adopt preregistration as a means of increasing rigor is a pathway to solving those challenges.",
        "page_number": 13,
        "context": "Core recommendation of chapter",
        "certainty_qualifier": "prescriptive claim"
    },
    {
        "id": "C110",
        "content": "Preregistration promotes built-in rather than bolt-on good practice in research design, data management, and analysis.",
        "claim_type": "methodological",
        "reasoning_type": "conceptual",
        "evidence_links": [],
        "verbatim_quote": "Preregistration promotes 'built-in' rather than 'bolt-on' good practice in research design, data management, and analysis.",
        "page_number": 13,
        "context": "Reiterating key benefit",
        "certainty_qualifier": "stated as fact"
    },
    {
        "id": "C111",
        "content": "Preregistration fosters thoughtful, slow archaeology rather than just-in-time archaeology.",
        "claim_type": "methodological",
        "reasoning_type": "conceptual",
        "evidence_links": [],
        "verbatim_quote": "It likewise fosters thoughtful, 'slow' archaeology rather than 'just-in-time' archaeology.",
        "page_number": 13,
        "context": "Connecting to slow archaeology theme",
        "certainty_qualifier": "stated as fact"
    },
    {
        "id": "C112",
        "content": "Robust, scalable, transparent, and reproducible results underlying persuasive research directed at grand challenges require planning and forethought.",
        "claim_type": "methodological",
        "reasoning_type": "conceptual",
        "evidence_links": [],
        "verbatim_quote": "Robust, scalable, transparent, and reproducible results, underlying persuasive research directed at grand challenges, require planning and forethought.",
        "page_number": 13,
        "context": "Justification for planning emphasis",
        "certainty_qualifier": "stated as requirement"
    },
    {
        "id": "C113",
        "content": "Making a public commitment to research design via preregistration before fieldwork provides a mechanism that makes space for necessary time and thought.",
        "claim_type": "methodological",
        "reasoning_type": "pragmatic",
        "evidence_links": [],
        "verbatim_quote": "Making a public commitment to research design via preregistration, before setting out for the field, provides a mechanism that makes space for the necessary time and thought.",
        "page_number": 13,
        "context": "Final sentence of chapter",
        "certainty_qualifier": "concluding assertion"
    }
]

# ============================================================================
# IMPLICIT ARGUMENTS ITEMS
# ============================================================================

implicit_arguments = [
    {
        "id": "IA022",
        "content": "Oceanography provides an appropriate model for archaeology to follow.",
        "reasoning": "Authors use Ocean Health Index as exemplar without acknowledging potential disanalogies between disciplines.",
        "trigger_text": "The discipline of oceanography has also grappled with 'small data' problems... As in archaeology, these problems inhibited the large-scale, synthetic research",
        "page_number": 11,
        "context": "Oceanography analogy",
        "theoretical_significance": "Cross-disciplinary analogies may obscure important differences"
    },
    {
        "id": "IA023",
        "content": "Thoughtful planning and slow, considered approaches are inherently valuable and opposed to industrialised efficiency.",
        "reasoning": "Authors invoke 'slow archaeology' approvingly without acknowledging potential costs of slowness or benefits of efficiency.",
        "trigger_text": "Slow archaeology evokes the practice of archaeology as a craft... as a challenge to the fragmented perspectives offered by workflows influenced by our own efficient, industrialized age",
        "page_number": 12,
        "context": "Slow archaeology framing",
        "theoretical_significance": "Romanticises craft tradition vs modern efficiency dichotomy"
    },
    {
        "id": "IA024",
        "content": "Just-in-time approaches are chaotic and represent lack of consideration rather than deliberate adaptive strategies.",
        "reasoning": "Consistently negative framing of emergent/just-in-time approaches as chaos rather than acknowledging potential benefits of flexibility.",
        "trigger_text": "the chaos of 'just-in-time' approaches to fieldwork",
        "page_number": 12,
        "context": "Negative characterisation",
        "theoretical_significance": "Frames adaptive approaches as inherently problematic"
    },
    {
        "id": "IA025",
        "content": "Freedom in fieldwork is a temptation to be resisted rather than a methodological value.",
        "reasoning": "Freedom framed as offering ability to 'delay day of reckoning' - negative characterisation.",
        "trigger_text": "Under-planned fieldwork might offer more freedom (and delay the day of reckoning with messy data)",
        "page_number": 12,
        "context": "Critique of flexibility",
        "theoretical_significance": "Prioritises accountability over methodological flexibility"
    },
    {
        "id": "IA026",
        "content": "Archaeological research should be directed at addressing grand challenges requiring large-scale synthesis.",
        "reasoning": "Concluding paragraph frames grand challenges as appropriate goal without acknowledging value of smaller-scale or idiographic research.",
        "trigger_text": "Robust, scalable, transparent, and reproducible results, underlying persuasive research directed at grand challenges",
        "page_number": 13,
        "context": "Final paragraph",
        "theoretical_significance": "Privileges nomothetic over idiographic research goals despite earlier claims about accommodation"
    }
]

# ============================================================================
# UPDATE EXTRACTION DATA
# ============================================================================

# Add new items to extraction
data['evidence'].extend(evidence_items)
data['claims'].extend(claims_items)
data['implicit_arguments'].extend(implicit_arguments)

# Update extraction notes to mark Pass 1 complete
data['extraction_notes'] = {
    'pass': 1,
    'section_extracted': 'ALL SECTIONS: Groups 1-5 complete, pages 2-13 (full paper excluding references)',
    'extraction_strategy': 'Section 5: Liberal extraction focusing on: (1) Ocean Health Index case study evidence, (2) slow archaeology theoretical framing, (3) concluding synthesis claims about preregistration value, (4) implicit assumptions about craft vs efficiency, flexibility vs accountability, and research goals. PASS 1 COMPLETE - All 5 section groups extracted liberally. Total ~7000 words extracted.',
    'known_uncertainties': [
        'Oceanography analogy (IA022) may need more critical examination',
        'Slow archaeology framing (C102-C105, IA023-IA025) introduces values that may tension with earlier pragmatism',
        'Final paragraph emphasis on grand challenges (C112, IA026) may contradict earlier accommodation of idiographic research',
        'Pass 2 rationalization should examine whether slow archaeology section truly integrates or merely adds another justification'
    ],
    'section_word_count_estimate': 7000,
    'pass1_complete': True,
    'total_sections': 5
}

data['extraction_timestamp'] = datetime.now().isoformat() + 'Z'

# Save updated extraction
with open('outputs/ross-ballsun-stanton-2022/extraction.json', 'w') as f:
    json.dump(data, f, indent=2)

print("=" * 80)
print("PASS 1 - SECTION GROUP 5 EXTRACTION COMPLETE")
print("=" * 80)
print()
print(f"Section: Slow Archaeology + Conclusions")
print(f"Pages: 11-13")
print(f"Estimated word count: ~1400 words")
print()
print("Items extracted:")
print(f"  Evidence: {len(evidence_items)} items (E014-E015)")
print(f"  Claims: {len(claims_items)} items (C096-C113)")
print(f"  Implicit Arguments: {len(implicit_arguments)} items (IA022-IA026)")
print()
print(f"Total this section: {len(evidence_items) + len(claims_items) + len(implicit_arguments)} items")
print()
print("=" * 80)
print("PASS 1 COMPLETE - FINAL TOTALS")
print("=" * 80)
print()
print("All 5 section groups extracted:")
print("  Group 1: Introduction + Predictive/Postdictive (pages 2-4)")
print("  Group 2: Just-in-Time Problem (pages 5-6)")
print("  Group 3: Suitability for Archaeology (pages 7-8)")
print("  Group 4: Introducing to Practice (pages 8-11)")
print("  Group 5: Slow Archaeology + Conclusions (pages 11-13)")
print()
print("Final extraction counts:")
print(f"  Evidence: 15 items (E001-E015)")
print(f"  Claims: 113 items (C001-C113)")
print(  "  Implicit Arguments: 26 items (IA001-IA026)")
print(f"  TOTAL: 154 items extracted")
print()
print("Paper characteristics:")
print("  - Methodological argument paper (19 pages)")
print("  - Evidence profile: Light (15 items) - primarily literature citations and case studies")
print("  - Claims profile: Heavy (113 items) - extensive methodological argumentation")
print("  - Implicit arguments: Substantial (26 items) - many assumptions about practice and values")
print()
print("Expected Pass 2 rationalization:")
print("  - Target: 15-20% reduction (130-140 items after Pass 2)")
print("  - Focus: Consolidate similar methodological claims")
print("  - Preserve: Distinct conceptual arguments and all evidence")
print()
print("✓ PASS 1 EXTRACTION COMPLETE")
print("✓ Ready for Pass 2: Rationalize Claims & Evidence")
print()
