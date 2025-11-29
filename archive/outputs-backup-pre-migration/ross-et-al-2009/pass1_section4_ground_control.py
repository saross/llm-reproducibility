#!/usr/bin/env python3
"""
Pass 1, Section 4: Liberal Claims/Evidence Extraction
Ross et al. 2009 - Remote Sensing and Archaeological Prospection in Apulia, Italy

Section: Methods - Ground Control (~900 words, pages 428-430)

Approach: Liberal extraction, cast wide net, aim for over-extraction.
Focus on field procedures, categorization systems, and validation methodology.
"""

import json
from datetime import datetime, timezone
from pathlib import Path

# Load current extraction
extraction_file = Path("extraction.json")
with open(extraction_file) as f:
    data = json.load(f)

# ============================================================================
# EVIDENCE - Liberal extraction
# ============================================================================

evidence_items = [
    {
        "evidence_id": "E061",
        "content": "Features were placed into one of five categories: sites, off-site scatters, ambiguous, false positives, and unassessed.",
        "evidence_type": "methodological_observation",
        "verbatim_quote": "Ultimately, they were placed into one of five categories: sites, off-site scatters, ambiguous (significant image anomaly but little or no surface material), false positives, and unassessed.",
        "page": 428,
        "relevance": "Documents feature categorization system",
        "supports_claims": ["C084"]
    },
    {
        "evidence_id": "E062",
        "content": "Ground control teams consisted of two or three people who walked feature perimeters and multiple paths across each feature.",
        "evidence_type": "methodological_observation",
        "verbatim_quote": "A team consisting of two or three people visited each feature, walked its perimeter and then walked several paths across it.",
        "page": 428,
        "relevance": "Describes field team composition and walking pattern",
        "supports_claims": ["C085"]
    },
    {
        "evidence_id": "E063",
        "content": "Modern or natural features were noted as such, while non-obvious features were fully documented.",
        "evidence_type": "methodological_observation",
        "verbatim_quote": "Modern or natural features were noted as such, while features that were not obviously modern or natural were fully documented.",
        "page": 428,
        "relevance": "Describes documentation criteria",
        "supports_claims": ["C086"]
    },
    {
        "evidence_id": "E064",
        "content": "The density of ancient surface material (if present) was systematically recorded.",
        "evidence_type": "methodological_observation",
        "verbatim_quote": "The density of ancient surface material (if present) was systematically recorded.",
        "page": 428,
        "relevance": "Documents quantitative recording procedure",
        "supports_claims": ["C087"]
    },
    {
        "evidence_id": "E065",
        "content": "The project employed the same site definition criteria as the MTS: a threshold of five sherds per square metre for historical sites and two sherds per square metre for prehistoric sites.",
        "evidence_type": "methodological_specification",
        "verbatim_quote": "We employed the same site definition criteria as the MTS (a threshold of five sherds per sq m for historical sites and two sherds per sq m for prehistoric sites)",
        "page": 429,
        "relevance": "Specifies quantitative site definition thresholds",
        "supports_claims": ["C088", "C089"]
    },
    {
        "evidence_id": "E066",
        "content": "The project corrected for low surface visibility following MTS procedures.",
        "evidence_type": "methodological_observation",
        "verbatim_quote": "and, like the MTS, we corrected for surface visibility",
        "page": 429,
        "relevance": "Documents visibility correction procedure",
        "supports_claims": ["C090"]
    },
    {
        "evidence_id": "E067",
        "content": "Correction for surface visibility was particularly important because fields could not be chosen based primarily on agricultural condition and visibility.",
        "evidence_type": "methodological_observation",
        "verbatim_quote": "Correction for surface visibility was particularly important because, unlike a typical surface survey, we could not choose fields based primarily on agricultural condition and visibility.",
        "page": 429,
        "relevance": "Explains constraint unique to remote sensing approach",
        "supports_claims": ["C091"]
    },
    {
        "evidence_id": "E068",
        "content": "Following MTS procedures, off-site scatters that did not meet the site threshold (even after correction) were also recorded.",
        "evidence_type": "methodological_observation",
        "verbatim_quote": "Again, following the procedures of the MTS, off-site scatters that did not meet the site threshold (even after correction) were also recorded.",
        "page": 429,
        "relevance": "Documents sub-threshold scatter recording",
        "supports_claims": ["C092"]
    },
    {
        "evidence_id": "E069",
        "content": "Wherever ancient material was present, a grab sample was collected.",
        "evidence_type": "methodological_observation",
        "verbatim_quote": "Wherever ancient material was present, a grab sample was collected.",
        "page": 429,
        "relevance": "Documents artifact sampling procedure",
        "supports_claims": ["C093"]
    },
    {
        "evidence_id": "E070",
        "content": "Ground control data allowed determination of whether image features were associated with ancient material and provided indication of site period and function.",
        "evidence_type": "methodological_observation",
        "verbatim_quote": "The data collected through ground control allowed us to ascertain whether or not the features identified in the satellite image were associated with ancient material, and provided some indication of each site's period of habitation and function.",
        "page": 429,
        "relevance": "Describes analytical outputs of ground control",
        "supports_claims": ["C094"]
    },
    {
        "evidence_id": "E071",
        "content": "When no material was present, ground control often explained the origin of false positives.",
        "evidence_type": "methodological_observation",
        "verbatim_quote": "When no material was present, ground control often explained the origin of these false positives.",
        "page": 429,
        "relevance": "Documents diagnostic value of negative results",
        "supports_claims": ["C095"]
    },
    {
        "evidence_id": "E072",
        "content": "Several types of false positives were identified in the first days: bedrock outcroppings, modern agricultural improvements/soil conditioning, and underground pipelines were most common.",
        "evidence_type": "empirical_observation",
        "verbatim_quote": "Several types of false positives were identified in the first days of ground control. Outcroppings of bedrock, modern agricultural improvements or soil conditioning, and underground pipelines were the most common.",
        "page": 429,
        "relevance": "Documents common false positive types",
        "supports_claims": ["C096"]
    },
    {
        "evidence_id": "E073",
        "content": "As ground control proceeded, image patterns associated with false positive features became readily identifiable and were eliminated during subsequent analysis.",
        "evidence_type": "methodological_observation",
        "verbatim_quote": "As ground control proceeded, image patterns associated with these features became readily identifiable, and were eliminated during the subsequent image analysis.",
        "page": 429,
        "relevance": "Documents iterative learning process",
        "supports_claims": ["C097"]
    },
    {
        "evidence_id": "E074",
        "content": "Features associated with ancient surface material were scrutinized and similar features were carefully searched for thereafter.",
        "evidence_type": "methodological_observation",
        "verbatim_quote": "Conversely, features identified in the image that proved to be associated with ancient surface material were scrutinized, and a careful search was conducted for similar features thereafter.",
        "page": 429,
        "relevance": "Documents positive pattern recognition learning",
        "supports_claims": ["C098"]
    },
    {
        "evidence_id": "E075",
        "content": "Nine features identified in the satellite image could not be subjected to ground control due to inaccessibility or destruction between image acquisition and investigation.",
        "evidence_type": "methodological_observation",
        "verbatim_quote": "Nine features identified in the satellite image could not be subjected to ground control because of inaccessibility or destruction between the date the image was acquired and the time of investigation.",
        "page": 429,
        "relevance": "Documents unassessed feature count and reasons",
        "supports_claims": ["C099"]
    },
    {
        "evidence_id": "E076",
        "content": "Unassessed features were excluded from consideration.",
        "evidence_type": "methodological_observation",
        "verbatim_quote": "These features were excluded from consideration.",
        "page": 429,
        "relevance": "Documents handling of unassessable features",
        "supports_claims": ["C100"]
    }
]

# ============================================================================
# CLAIMS - Liberal extraction
# ============================================================================

claims_items = [
    {
        "claim_id": "C084",
        "content": "A five-category system (sites, off-site scatters, ambiguous, false positives, unassessed) provides comprehensive classification for ground-controlled features.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "Ultimately, they were placed into one of five categories: sites, off-site scatters, ambiguous (significant image anomaly but little or no surface material), false positives, and unassessed.",
        "page": 428,
        "supporting_evidence": ["E061"],
        "confidence": "high",
        "relevance": "Describes classification framework"
    },
    {
        "claim_id": "C085",
        "content": "Small teams (2-3 people) can effectively conduct ground control by walking perimeters and transects.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "A team consisting of two or three people visited each feature, walked its perimeter and then walked several paths across it.",
        "page": 428,
        "supporting_evidence": ["E062"],
        "confidence": "high",
        "relevance": "Describes efficient field procedure"
    },
    {
        "claim_id": "C086",
        "content": "Selective full documentation of non-obvious features balances thoroughness with efficiency.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "Modern or natural features were noted as such, while features that were not obviously modern or natural were fully documented.",
        "page": 428,
        "supporting_evidence": ["E063"],
        "confidence": "high",
        "relevance": "Justifies differential documentation strategy"
    },
    {
        "claim_id": "C087",
        "content": "Systematic recording of surface material density enables quantitative site definition.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "The density of ancient surface material (if present) was systematically recorded.",
        "page": 428,
        "supporting_evidence": ["E064"],
        "confidence": "high",
        "relevance": "Connects field recording to classification"
    },
    {
        "claim_id": "C088",
        "content": "Using the same site definition criteria as the MTS enables valid comparison between methods.",
        "claim_type": "methodological_justification",
        "verbatim_quote": "We employed the same site definition criteria as the MTS",
        "page": 429,
        "supporting_evidence": ["E065"],
        "confidence": "high",
        "relevance": "Justifies methodological standardization"
    },
    {
        "claim_id": "C089",
        "content": "Different density thresholds for historical versus prehistoric sites reflect differential artifact production rates.",
        "claim_type": "interpretive_principle",
        "verbatim_quote": "a threshold of five sherds per sq m for historical sites and two sherds per sq m for prehistoric sites",
        "page": 429,
        "supporting_evidence": ["E065"],
        "confidence": "medium",
        "relevance": "Explains rationale for differential thresholds"
    },
    {
        "claim_id": "C090",
        "content": "Surface visibility correction is necessary for valid density-based site classification.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "and, like the MTS, we corrected for surface visibility",
        "page": 429,
        "supporting_evidence": ["E066"],
        "confidence": "high",
        "relevance": "Asserts necessity of visibility correction"
    },
    {
        "claim_id": "C091",
        "content": "Remote sensing-guided ground control cannot optimize field selection for visibility like traditional survey, making visibility correction especially important.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "Correction for surface visibility was particularly important because, unlike a typical surface survey, we could not choose fields based primarily on agricultural condition and visibility.",
        "page": 429,
        "supporting_evidence": ["E067"],
        "confidence": "high",
        "relevance": "Explains constraint of remote sensing approach"
    },
    {
        "claim_id": "C092",
        "content": "Recording sub-threshold off-site scatters provides additional landscape data beyond site locations.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "Again, following the procedures of the MTS, off-site scatters that did not meet the site threshold (even after correction) were also recorded.",
        "page": 429,
        "supporting_evidence": ["E068"],
        "confidence": "high",
        "relevance": "Justifies recording low-density material"
    },
    {
        "claim_id": "C093",
        "content": "Grab sampling provides sufficient material for period and function determination.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "Wherever ancient material was present, a grab sample was collected.",
        "page": 429,
        "supporting_evidence": ["E069"],
        "confidence": "medium",
        "relevance": "Justifies sampling strategy"
    },
    {
        "claim_id": "C094",
        "content": "Ground control serves dual purposes: validating image feature-archaeology associations and providing chronological/functional information.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "The data collected through ground control allowed us to ascertain whether or not the features identified in the satellite image were associated with ancient material, and provided some indication of each site's period of habitation and function.",
        "page": 429,
        "supporting_evidence": ["E070"],
        "confidence": "high",
        "relevance": "Identifies multiple functions of ground control"
    },
    {
        "claim_id": "C095",
        "content": "False positive identification contributes to understanding of image interpretation by revealing natural and modern phenomena.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "When no material was present, ground control often explained the origin of these false positives.",
        "page": 429,
        "supporting_evidence": ["E071"],
        "confidence": "high",
        "relevance": "Asserts value of negative results"
    },
    {
        "claim_id": "C096",
        "content": "Bedrock outcroppings, modern agricultural modifications, and underground infrastructure are the most common sources of false positives.",
        "claim_type": "empirical_claim",
        "verbatim_quote": "Outcroppings of bedrock, modern agricultural improvements or soil conditioning, and underground pipelines were the most common.",
        "page": 429,
        "supporting_evidence": ["E072"],
        "confidence": "high",
        "relevance": "Identifies primary false positive sources"
    },
    {
        "claim_id": "C097",
        "content": "Early identification of false positive patterns enables more efficient subsequent analysis through pattern elimination.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "As ground control proceeded, image patterns associated with these features became readily identifiable, and were eliminated during the subsequent image analysis.",
        "page": 429,
        "supporting_evidence": ["E073"],
        "confidence": "high",
        "relevance": "Describes learning-based efficiency gain"
    },
    {
        "claim_id": "C098",
        "content": "Positive pattern recognition allows targeted searching for similar features, improving discovery efficiency.",
        "claim_type": "methodological_assertion",
        "verbatim_quote": "Conversely, features identified in the image that proved to be associated with ancient surface material were scrutinized, and a careful search was conducted for similar features thereafter.",
        "page": 429,
        "supporting_evidence": ["E074"],
        "confidence": "high",
        "relevance": "Describes adaptive search strategy"
    },
    {
        "claim_id": "C099",
        "content": "Landscape changes between image acquisition and ground control can limit feature assessment.",
        "claim_type": "methodological_limitation",
        "verbatim_quote": "Nine features identified in the satellite image could not be subjected to ground control because of inaccessibility or destruction between the date the image was acquired and the time of investigation.",
        "page": 429,
        "supporting_evidence": ["E075"],
        "confidence": "high",
        "relevance": "Identifies temporal limitation of archival imagery"
    },
    {
        "claim_id": "C100",
        "content": "Excluding unassessable features maintains methodological rigor in comparative analysis.",
        "claim_type": "methodological_justification",
        "verbatim_quote": "These features were excluded from consideration.",
        "page": 429,
        "supporting_evidence": ["E076"],
        "confidence": "high",
        "relevance": "Justifies conservative approach to uncertain data"
    }
]

# ============================================================================
# IMPLICIT ARGUMENTS
# ============================================================================

implicit_arguments = [
    {
        "implicit_argument_id": "IA017",
        "content": "The five-category system is exhaustive and mutually exclusive (implied by using it as complete classification).",
        "argument_type": "unstated_assumption",
        "trigger_text": "Ultimately, they were placed into one of five categories",
        "page": 428,
        "reconstruction_confidence": "high",
        "related_claims": ["C084"],
        "critical_for_logic": True,
        "notes": "Classification system assumes all features fit into one category"
    },
    {
        "implicit_argument_id": "IA018",
        "content": "Walking perimeters and transects provides representative coverage of feature characteristics (implied by using this as standard procedure).",
        "argument_type": "methodological_assumption",
        "trigger_text": "walked its perimeter and then walked several paths across it",
        "page": 428,
        "reconstruction_confidence": "high",
        "related_claims": ["C085"],
        "critical_for_logic": True,
        "notes": "Assumes crossing pattern captures feature variability"
    },
    {
        "implicit_argument_id": "IA019",
        "content": "Grab sampling is representative of the artifact assemblage present (implied by using it for period/function determination).",
        "argument_type": "unstated_premise",
        "trigger_text": "Wherever ancient material was present, a grab sample was collected... provided some indication of each site's period of habitation and function.",
        "page": 429,
        "reconstruction_confidence": "medium",
        "related_claims": ["C093", "C094"],
        "critical_for_logic": True,
        "notes": "Non-systematic sampling assumed adequate for chronological assignment"
    },
    {
        "implicit_argument_id": "IA020",
        "content": "The MTS site definition criteria are appropriate for this study area and research questions (implied by adopting them).",
        "argument_type": "unstated_premise",
        "trigger_text": "We employed the same site definition criteria as the MTS",
        "page": 429,
        "reconstruction_confidence": "high",
        "related_claims": ["C088"],
        "critical_for_logic": True,
        "notes": "Assumes MTS thresholds are valid, not just convenient for comparison"
    },
    {
        "implicit_argument_id": "IA021",
        "content": "Early learning about false positives can be applied to the rest of the image (implied by elimination during subsequent analysis).",
        "argument_type": "unstated_assumption",
        "trigger_text": "As ground control proceeded, image patterns associated with these features became readily identifiable, and were eliminated during the subsequent image analysis.",
        "page": 429,
        "reconstruction_confidence": "high",
        "related_claims": ["C097"],
        "critical_for_logic": True,
        "notes": "Assumes false positive patterns are consistent across study area"
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
    'section': 'Section 4: Methods (Ground Control)',
    'pages': '428-430',
    'word_count_estimate': 900,
    'items_extracted': {
        'evidence': len(evidence_items),
        'claims': len(claims_items),
        'implicit_arguments': len(implicit_arguments)
    },
    'notes': 'Methodological section focused on field procedures. Extracted detailed evidence about team procedures, categorization systems, and iterative learning. Claims emphasize methodological standardization with MTS and adaptive learning benefits. Rich material for future protocol extraction.'
})

with open(extraction_file, 'w') as f:
    json.dump(data, f, indent=2)

print(f"✓ Pass 1, Section 4 complete: Methods (Ground Control)")
print(f"  - Evidence items: {len(evidence_items)}")
print(f"  - Claims: {len(claims_items)}")
print(f"  - Implicit arguments: {len(implicit_arguments)}")
print(f"  - Total items this section: {len(evidence_items) + len(claims_items) + len(implicit_arguments)}")
print(f"  - Running total: {len(data['evidence'])} evidence, {len(data['claims'])} claims, {len(data['implicit_arguments'])} implicit arguments")
