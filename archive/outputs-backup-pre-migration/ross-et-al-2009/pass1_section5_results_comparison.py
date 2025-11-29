#!/usr/bin/env python3
"""
Pass 1, Section 5: Liberal Claims/Evidence Extraction
Ross et al. 2009 - Remote Sensing and Archaeological Prospection in Apulia, Italy

Section: Results + Comparison with MTS (~1200 words, pages 430-433)

Approach: Liberal extraction, cast wide net, aim for over-extraction.
Focus on quantitative results, comparative analysis, and performance metrics.
"""

import json
from datetime import datetime, timezone
from pathlib import Path

# Load current extraction
extraction_file = Path("extraction.json")
with open(extraction_file) as f:
    data = json.load(f)

# ============================================================================
# EVIDENCE - Liberal extraction of quantitative results
# ============================================================================

evidence_items = [
    {
        "evidence_id": "E077",
        "content": "The iterative process of image analysis, ground control, and review was performed across the entire northern half of the image over approximately three weeks in July 2007.",
        "evidence_type": "methodological_observation",
        "verbatim_quote": "Over the course of approximately three weeks of fieldwork in July 2007, this iterative process of image analysis, ground control, image review, and subsequent ground control was performed across the entire northern half of the image.",
        "page": 430,
        "relevance": "Documents fieldwork timing and coverage for northern section",
        "supports_claims": ["C101"]
    },
    {
        "evidence_id": "E078",
        "content": "The southern half of the image was completed during an additional 10 days in June and July 2008.",
        "evidence_type": "methodological_observation",
        "verbatim_quote": "The southern half of the image was completed during an additional 10 days in June and July 2008.",
        "page": 430,
        "relevance": "Documents fieldwork timing for southern section",
        "supports_claims": ["C102"]
    },
    {
        "evidence_id": "E079",
        "content": "In total, over 70 square kilometres were assessed.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "In total, over 70 sq km were assessed",
        "page": 430,
        "relevance": "Documents total area analyzed in image",
        "supports_claims": ["C103"]
    },
    {
        "evidence_id": "E080",
        "content": "One hundred and twenty-three features of interest were identified in the image and inventoried.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "One hundred and twenty-three features of interest were identified in the image and inventoried.",
        "page": 430,
        "relevance": "Documents total features detected in imagery",
        "supports_claims": ["C104"]
    },
    {
        "evidence_id": "E081",
        "content": "Ground control evaluated 1.45 square kilometres, including 114 features.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "Ground control evaluated 1.45 sq km, including 114 features.",
        "page": 430,
        "relevance": "Documents ground control coverage area and feature count",
        "supports_claims": ["C105"]
    },
    {
        "evidence_id": "E082",
        "content": "Urban areas were omitted from analysis, as was an area in the extreme southwestern part that was a wetland before 20th century drainage.",
        "evidence_type": "methodological_observation",
        "verbatim_quote": "Urban areas were omitted, as was an area in the extreme southwestern part of the image that was deemed very unlikely to yield any ancient remains since it was a wetland before drainage in the 20th century and is now subject to intensive use.",
        "page": 430,
        "relevance": "Documents exclusion criteria and areas",
        "supports_claims": ["C106"]
    },
    {
        "evidence_id": "E083",
        "content": "Ground control determined that 14 image features corresponded to ancient surface scatters meeting MTS site definition (after modest correction for surface visibility).",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "Ground control determined that 14 image features corresponded to ancient surface scatters that met the MTS's definition of a site (after modest correction for surface visibility).",
        "page": 430,
        "relevance": "Documents site-level discoveries",
        "supports_claims": ["C107"]
    },
    {
        "evidence_id": "E084",
        "content": "Significant off-site scatters were associated with an additional 15 image features.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "Significant off-site scatters were associated with an additional 15 image features.",
        "page": 430,
        "relevance": "Documents off-site scatter discoveries",
        "supports_claims": ["C108"]
    },
    {
        "evidence_id": "E085",
        "content": "Another 13 image features displayed distinctive and unusual reflectance patterns with no obvious explanation and often low or no surface visibility, remaining ambiguous.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "Another 13 image features displayed such distinctive and unusual reflectance patterns that they remain ambiguous; they had no obvious explanation and often low or no surface visibility",
        "page": 430,
        "relevance": "Documents ambiguous feature count",
        "supports_claims": ["C109"]
    },
    {
        "evidence_id": "E086",
        "content": "Overall, 14 out of 114 features (12.3%) identified and assessed yielded surface finds meeting the site density criterion.",
        "evidence_type": "quantitative_result",
        "verbatim_quote": "Overall, 14 out of 114 features (12.3%) identified in the satellite image and assessed in the field yielded surface finds that met the density criterion for a \"site\" employed by the project.",
        "page": 431,
        "relevance": "Key true positive rate result",
        "supports_claims": ["C110"]
    },
    {
        "evidence_id": "E087",
        "content": "Another 15 features (13.1%) yielded some ancient material below the site threshold.",
        "evidence_type": "quantitative_result",
        "verbatim_quote": "Another 15 features (13.1%) yielded some ancient material below the site threshold",
        "page": 432,
        "relevance": "Documents off-site scatter rate",
        "supports_claims": ["C111"]
    },
    {
        "evidence_id": "E088",
        "content": "13 features (11.4%) remain features of interest despite not yet yielding any ancient material.",
        "evidence_type": "quantitative_result",
        "verbatim_quote": "while 13 (11.4%) remain features of interest despite the fact that they have not yet yielded any ancient material.",
        "page": 432,
        "relevance": "Documents ambiguous feature rate",
        "supports_claims": ["C112"]
    },
    {
        "evidence_id": "E089",
        "content": "Some 25.4% of features yielded significant surface material, while another 11.4% could neither be confirmed nor eliminated.",
        "evidence_type": "quantitative_result",
        "verbatim_quote": "Thus, some 25.4% of features yielded significant surface material, while another 11.4% could neither be confirmed nor eliminated from consideration.",
        "page": 432,
        "relevance": "Summarizes positive and ambiguous rates",
        "supports_claims": ["C113"]
    },
    {
        "evidence_id": "E090",
        "content": "72 of 114 (63.1%) features were eliminated as false positives after ground control.",
        "evidence_type": "quantitative_result",
        "verbatim_quote": "Still, some 72 of 114 (63.1%) features were eliminated from consideration after ground control.",
        "page": 432,
        "relevance": "Documents false positive rate",
        "supports_claims": ["C114"]
    },
    {
        "evidence_id": "E091",
        "content": "27 false positives (23.6%) resulted from modern agriculture or other activity.",
        "evidence_type": "quantitative_result",
        "verbatim_quote": "Many were the result of modern agriculture or other activity (27 or 23.6%)",
        "page": 432,
        "relevance": "Breaks down false positive sources",
        "supports_claims": ["C115"]
    },
    {
        "evidence_id": "E092",
        "content": "33 false positives (28.9%) resulted from natural phenomena.",
        "evidence_type": "quantitative_result",
        "verbatim_quote": "or natural phenomena (33 or 28.9%).",
        "page": 432,
        "relevance": "Breaks down false positive sources",
        "supports_claims": ["C116"]
    },
    {
        "evidence_id": "E093",
        "content": "The MTS yielded an average of 6.3 sites and off-site scatters per square kilometre (63 sites total).",
        "evidence_type": "comparative_measurement",
        "verbatim_quote": "The MTS, which explored a representative transect of our study area, yielded an average of 6.3 sites and off-site scatters per sq km (63 sites in total).",
        "page": 432,
        "relevance": "Establishes MTS discovery rate baseline",
        "supports_claims": ["C117"]
    },
    {
        "evidence_id": "E094",
        "content": "At the MTS rate, an area the size of the ground control area (1.45 sq km) should have produced about nine ancient sites and off-site scatters.",
        "evidence_type": "comparative_calculation",
        "verbatim_quote": "At this rate, an area the size of that analyzed during remote sensing ground control (1.45 sq km) should have produced a total of about nine ancient sites and off-site scatters.",
        "page": 432,
        "relevance": "Calculates expected random discovery rate",
        "supports_claims": ["C118"]
    },
    {
        "evidence_id": "E095",
        "content": "The discovery of 29 sites and off-site scatters exceeds the number expected from a randomly chosen area of equal size by more than three times.",
        "evidence_type": "comparative_result",
        "verbatim_quote": "The discovery of 29 sites and off-site scatters exceeds the number expected from a randomly chosen area of equal size by more than three times.",
        "page": 432,
        "relevance": "Key comparative finding demonstrating effectiveness",
        "supports_claims": ["C119"]
    },
    {
        "evidence_id": "E096",
        "content": "The project encountered 51 false negatives: sites or off-site scatters previously discovered by MTS but not detected during image analysis.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "Our project encountered 51 such false negatives.",
        "page": 432,
        "relevance": "Documents missed site count",
        "supports_claims": ["C120"]
    },
    {
        "evidence_id": "E097",
        "content": "The median size of scatters discovered through remote sensing was 0.65 ha versus 0.1 ha for surface survey.",
        "evidence_type": "comparative_measurement",
        "verbatim_quote": "a tendency reflected in the difference between the median size of scatters discovered through remote sensing (0.65 ha) versus surface survey (0.1 ha)",
        "page": 432,
        "relevance": "Shows size bias in remote sensing discovery",
        "supports_claims": ["C121"]
    },
    {
        "evidence_id": "E098",
        "content": "Twelve image features corresponded to surface concentrations previously defined as sites or off-site scatters by the MTS (out of 63 total).",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "Twelve image features corresponded to surface concentrations previously defined as sites or off-site scatters by the MTS (out of a total of 63).",
        "page": 432,
        "relevance": "Documents overlap between methods",
        "supports_claims": ["C122"]
    },
    {
        "evidence_id": "E099",
        "content": "Only eight of the 12 overlapping features yielded site or off-site sherd densities during ground control, while four produced little if any ancient surface material.",
        "evidence_type": "comparative_observation",
        "verbatim_quote": "Curiously, only eight of these 12 features yielded site or off-site sherd densities during ground control. The other four produced little if any ancient surface material",
        "page": 432,
        "relevance": "Documents resurvey discrepancy",
        "supports_claims": ["C123"]
    }
]

# ============================================================================
# CLAIMS - Liberal extraction
# ============================================================================

claims_items = [
    {
        "claim_id": "C101",
        "content": "The iterative analysis and ground control process can cover half of a 100 sq km study area in approximately three weeks.",
        "claim_type": "efficiency_claim",
        "verbatim_quote": "Over the course of approximately three weeks of fieldwork in July 2007, this iterative process of image analysis, ground control, image review, and subsequent ground control was performed across the entire northern half of the image.",
        "page": 430,
        "supporting_evidence": ["E077"],
        "confidence": "high",
        "relevance": "Documents practical efficiency rate"
    },
    {
        "claim_id": "C102",
        "content": "The project was conducted in two field seasons (2007, 2008) totaling about four weeks of fieldwork.",
        "claim_type": "methodological_description",
        "verbatim_quote": "Over the course of approximately three weeks of fieldwork in July 2007... The southern half of the image was completed during an additional 10 days in June and July 2008.",
        "page": 430,
        "supporting_evidence": ["E077", "E078"],
        "confidence": "high",
        "relevance": "Documents total project timeline"
    },
    {
        "claim_id": "C103",
        "content": "Over 70 square kilometres represents a substantial area for intensive archaeological prospection.",
        "claim_type": "scale_assertion",
        "verbatim_quote": "In total, over 70 sq km were assessed",
        "page": 430,
        "supporting_evidence": ["E079"],
        "confidence": "medium",
        "relevance": "Emphasizes scale achievement"
    },
    {
        "claim_id": "C104",
        "content": "Image analysis identified 123 features of interest worthy of ground control investigation.",
        "claim_type": "results_description",
        "verbatim_quote": "One hundred and twenty-three features of interest were identified in the image and inventoried.",
        "page": 430,
        "supporting_evidence": ["E080"],
        "confidence": "high",
        "relevance": "Documents detection success"
    },
    {
        "claim_id": "C105",
        "content": "Ground control coverage of 1.45 sq km evaluating 114 features is sufficient for assessing image analysis effectiveness.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "Ground control evaluated 1.45 sq km, including 114 features.",
        "page": 430,
        "supporting_evidence": ["E081"],
        "confidence": "medium",
        "relevance": "Asserts adequacy of ground control sample"
    },
    {
        "claim_id": "C106",
        "content": "Urban areas and former wetlands should be excluded from archaeological remote sensing analysis.",
        "claim_type": "methodological_recommendation",
        "verbatim_quote": "Urban areas were omitted, as was an area in the extreme southwestern part of the image that was deemed very unlikely to yield any ancient remains since it was a wetland before drainage in the 20th century and is now subject to intensive use.",
        "page": 430,
        "supporting_evidence": ["E082"],
        "confidence": "high",
        "relevance": "Justifies area exclusions"
    },
    {
        "claim_id": "C107",
        "content": "Remote sensing with ground control can successfully identify sites meeting established density criteria.",
        "claim_type": "effectiveness_claim",
        "verbatim_quote": "Ground control determined that 14 image features corresponded to ancient surface scatters that met the MTS's definition of a site",
        "page": 430,
        "supporting_evidence": ["E083"],
        "confidence": "high",
        "relevance": "Demonstrates site detection capability"
    },
    {
        "claim_id": "C108",
        "content": "Remote sensing detects not only sites but also significant off-site scatters.",
        "claim_type": "capability_claim",
        "verbatim_quote": "Significant off-site scatters were associated with an additional 15 image features.",
        "page": 430,
        "supporting_evidence": ["E084"],
        "confidence": "high",
        "relevance": "Demonstrates broader detection capability"
    },
    {
        "claim_id": "C109",
        "content": "Some image features with distinctive spectral patterns resist straightforward interpretation even after ground control.",
        "claim_type": "methodological_observation",
        "verbatim_quote": "Another 13 image features displayed such distinctive and unusual reflectance patterns that they remain ambiguous",
        "page": 430,
        "supporting_evidence": ["E085"],
        "confidence": "high",
        "relevance": "Identifies interpretive challenge category"
    },
    {
        "claim_id": "C110",
        "content": "A 12.3% true positive rate for site-level discoveries represents meaningful archaeological prospection success.",
        "claim_type": "effectiveness_claim",
        "verbatim_quote": "Overall, 14 out of 114 features (12.3%) identified in the satellite image and assessed in the field yielded surface finds that met the density criterion for a \"site\"",
        "page": 431,
        "supporting_evidence": ["E086"],
        "confidence": "medium",
        "relevance": "Evaluates practical success rate"
    },
    {
        "claim_id": "C111",
        "content": "Combined site and off-site discovery rate of 25.4% demonstrates substantial archaeological signal in imagery.",
        "claim_type": "effectiveness_claim",
        "verbatim_quote": "Thus, some 25.4% of features yielded significant surface material",
        "page": 432,
        "supporting_evidence": ["E087", "E089"],
        "confidence": "high",
        "relevance": "Summarizes overall detection success"
    },
    {
        "claim_id": "C112",
        "content": "Ambiguous features (11.4%) warrant further investigation with improved ground visibility or additional techniques.",
        "claim_type": "methodological_recommendation",
        "verbatim_quote": "while another 11.4% could neither be confirmed nor eliminated from consideration.",
        "page": 432,
        "supporting_evidence": ["E088"],
        "confidence": "medium",
        "relevance": "Identifies follow-up research opportunity"
    },
    {
        "claim_id": "C113",
        "content": "Combined positive and ambiguous features (36.8%) suggest significant untapped potential in remote sensing prospection.",
        "claim_type": "interpretive_claim",
        "verbatim_quote": "Thus, some 25.4% of features yielded significant surface material, while another 11.4% could neither be confirmed nor eliminated from consideration.",
        "page": 432,
        "supporting_evidence": ["E089"],
        "confidence": "medium",
        "relevance": "Interprets cumulative potential"
    },
    {
        "claim_id": "C114",
        "content": "A 63.1% false positive rate illustrates both the challenges and learning opportunities in archaeological remote sensing.",
        "claim_type": "interpretive_claim",
        "verbatim_quote": "Still, some 72 of 114 (63.1%) features were eliminated from consideration after ground control. Such false positives further illustrate the strengths and weaknesses of archaeological prospection using satellite image analysis.",
        "page": 432,
        "supporting_evidence": ["E090"],
        "confidence": "high",
        "relevance": "Interprets false positive implications"
    },
    {
        "claim_id": "C115",
        "content": "Modern agricultural activity is a major source of false positives in archaeological remote sensing.",
        "claim_type": "methodological_finding",
        "verbatim_quote": "Many were the result of modern agriculture or other activity (27 or 23.6%)",
        "page": 432,
        "supporting_evidence": ["E091"],
        "confidence": "high",
        "relevance": "Identifies primary interference source"
    },
    {
        "claim_id": "C116",
        "content": "Natural phenomena (especially geological features) are the single largest source of false positives.",
        "claim_type": "methodological_finding",
        "verbatim_quote": "or natural phenomena (33 or 28.9%).",
        "page": 432,
        "supporting_evidence": ["E092"],
        "confidence": "high",
        "relevance": "Identifies primary confounding factor"
    },
    {
        "claim_id": "C117",
        "content": "The MTS provides a robust baseline for evaluating remote sensing discovery rates.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "The MTS, which explored a representative transect of our study area, yielded an average of 6.3 sites and off-site scatters per sq km",
        "page": 432,
        "supporting_evidence": ["E093"],
        "confidence": "high",
        "relevance": "Establishes validity of comparison"
    },
    {
        "claim_id": "C118",
        "content": "Random site discovery in the ground control area would be expected to yield about nine sites and scatters.",
        "claim_type": "statistical_calculation",
        "verbatim_quote": "At this rate, an area the size of that analyzed during remote sensing ground control (1.45 sq km) should have produced a total of about nine ancient sites and off-site scatters.",
        "page": 432,
        "supporting_evidence": ["E094"],
        "confidence": "high",
        "relevance": "Establishes null hypothesis baseline"
    },
    {
        "claim_id": "C119",
        "content": "Exceeding expected random discovery by more than 3× demonstrates that image analysis provides genuine archaeological signal.",
        "claim_type": "effectiveness_claim",
        "verbatim_quote": "The discovery of 29 sites and off-site scatters exceeds the number expected from a randomly chosen area of equal size by more than three times.",
        "page": 432,
        "supporting_evidence": ["E095"],
        "confidence": "high",
        "relevance": "Core finding demonstrating method effectiveness"
    },
    {
        "claim_id": "C120",
        "content": "False negatives reveal the value and limitations of remote sensing compared to surface survey.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "\"False negatives,\" sites or off-site scatters previously discovered by the MTS but not detected during our image analysis (FIG. 6), also reveal the value and limitations of remote sensing.",
        "page": 432,
        "supporting_evidence": ["E096"],
        "confidence": "high",
        "relevance": "Frames complementary method relationship"
    },
    {
        "claim_id": "C121",
        "content": "Remote sensing preferentially detects larger sites, missing the smallest tier discovered by intensive survey.",
        "claim_type": "methodological_finding",
        "verbatim_quote": "The smallest tier of sites proved difficult to detect through image analysis, even using high-resolution imagery... a tendency reflected in the difference between the median size of scatters discovered through remote sensing (0.65 ha) versus surface survey (0.1 ha)",
        "page": 432,
        "supporting_evidence": ["E097"],
        "confidence": "high",
        "relevance": "Identifies key size bias in detection"
    },
    {
        "claim_id": "C122",
        "content": "Moderate overlap (12/63 features) between remote sensing and MTS results indicates complementary rather than redundant methods.",
        "claim_type": "interpretive_claim",
        "verbatim_quote": "Twelve image features corresponded to surface concentrations previously defined as sites or off-site scatters by the MTS (out of a total of 63).",
        "page": 432,
        "supporting_evidence": ["E098"],
        "confidence": "medium",
        "relevance": "Interprets methods as complementary"
    },
    {
        "claim_id": "C123",
        "content": "Discrepancies between initial and resurvey results highlight a familiar problem in archaeological surface survey reproducibility.",
        "claim_type": "methodological_observation",
        "verbatim_quote": "Since variations in surface visibility are probably not responsible (most of the sites in question are located in fields characterized by well-established perennial agriculture), this discrepancy highlights a familiar problem in archaeological surface survey: later fieldwork may fail to reproduce initial results when sites are resurveyed",
        "page": 432,
        "supporting_evidence": ["E099"],
        "confidence": "high",
        "relevance": "Identifies broader survey methodology issue"
    }
]

# ============================================================================
# IMPLICIT ARGUMENTS
# ============================================================================

implicit_arguments = [
    {
        "implicit_argument_id": "IA022",
        "content": "About four weeks of fieldwork for 70+ sq km is efficient compared to traditional survey (implied by emphasis on time period).",
        "argument_type": "unstated_comparison",
        "trigger_text": "Over the course of approximately three weeks... additional 10 days",
        "page": 430,
        "reconstruction_confidence": "medium",
        "related_claims": ["C101", "C102"],
        "critical_for_logic": False,
        "notes": "Efficiency argument requires implicit comparison to alternative methods"
    },
    {
        "implicit_argument_id": "IA023",
        "content": "Statistical significance threshold for 'too high to be explained by random association' is met by 3× exceedance (implied by presenting this as meaningful).",
        "argument_type": "unstated_premise",
        "trigger_text": "exceeds the number expected from a randomly chosen area of equal size by more than three times",
        "page": 432,
        "reconstruction_confidence": "high",
        "related_claims": ["C119"],
        "critical_for_logic": True,
        "notes": "Statistical argument without explicit significance testing"
    },
    {
        "implicit_argument_id": "IA024",
        "content": "The MTS transect is representative of the full study area (implied by using its rate for expected discovery calculation).",
        "argument_type": "unstated_premise",
        "trigger_text": "The MTS, which explored a representative transect of our study area",
        "page": 432,
        "reconstruction_confidence": "high",
        "related_claims": ["C117", "C118"],
        "critical_for_logic": True,
        "notes": "Extrapolation requires representativeness assumption"
    },
    {
        "implicit_argument_id": "IA025",
        "content": "A 63% false positive rate is acceptable given the 3× improvement over random discovery (implied by presenting both as complementary findings).",
        "argument_type": "unstated_evaluation",
        "trigger_text": "Still, some 72 of 114 (63.1%) features were eliminated... Even considering the number of false positives, the number of sites... proved higher than would be expected from a random sample.",
        "page": 432,
        "reconstruction_confidence": "medium",
        "related_claims": ["C114", "C119"],
        "critical_for_logic": False,
        "notes": "Trade-off between false positives and true positive enhancement"
    },
    {
        "implicit_argument_id": "IA026",
        "content": "Detecting larger sites is valuable even if smaller sites are missed (implied by framing size bias as complementarity rather than limitation).",
        "argument_type": "unstated_value_judgment",
        "trigger_text": "a tendency reflected in the difference between the median size... Moderate overlap... indicates complementary rather than redundant methods",
        "page": 432,
        "reconstruction_confidence": "medium",
        "related_claims": ["C121", "C122"],
        "critical_for_logic": False,
        "notes": "Positive framing of size bias as complementarity"
    }
]

# ============================================================================
# UPDATE EXTRACTION FILE
# ============================================================================

data['evidence'].extend(evidence_items)
data['claims'].extend(claims_items)
data['implicit_arguments'].extend(implicit_arguments)
data['extraction_timestamp'] = datetime.now(timezone.utc).isoformat()

data['extraction_notes']['pass1_sections'].append({
    'section': 'Section 5: Results + Comparison with MTS',
    'pages': '430-433',
    'word_count_estimate': 1200,
    'items_extracted': {
        'evidence': len(evidence_items),
        'claims': len(claims_items),
        'implicit_arguments': len(implicit_arguments)
    },
    'notes': 'Results-heavy section with extensive quantitative data. Extracted detailed evidence about discovery rates, false positives/negatives, and comparative performance. Claims emphasize effectiveness demonstration, methodological findings, and complementarity of methods. Critical section for evaluating project success.'
})

with open(extraction_file, 'w') as f:
    json.dump(data, f, indent=2)

print(f"✓ Pass 1, Section 5 complete: Results + Comparison with MTS")
print(f"  - Evidence items: {len(evidence_items)}")
print(f"  - Claims: {len(claims_items)}")
print(f"  - Implicit arguments: {len(implicit_arguments)}")
print(f"  - Total items this section: {len(evidence_items) + len(claims_items) + len(implicit_arguments)}")
print(f"  - Running total: {len(data['evidence'])} evidence, {len(data['claims'])} claims, {len(data['implicit_arguments'])} implicit arguments")
