#!/usr/bin/env python3
"""
Pass 1: Liberal Extraction - Sections 1-4 (Abstract through Regional Setting End)
Connor et al. 2013 - Environmental conditions in SE Balkans since LGM

Sections covered:
- Section 1: Abstract (page 3)
- Section 2: Introduction (pages 3-4)
- Section 3: Regional setting start (page 4)
- Section 4: Regional setting end (pages 4-6)

Liberal over-extraction approach: 40-50% over expected targets
"""

import json

# Load current extraction
with open('/home/shawn/Code/llm-reproducibility/outputs/connor-et-al-2013/extraction.json', 'r') as f:
    data = json.load(f)

# SECTION 1: ABSTRACT (page 3, lines 33-48)
# Expected: 8-12 claims, 2-4 evidence

abstract_items = [
    # Evidence
    {
        "id": "E001",
        "content": "Record indicates persistence of cold steppe vegetation from ~37,500 to 17,900 cal. a BP",
        "evidence_type": "proxy_observation",
        "page": 3,
        "verbatim_quote": "Our record indicates the persistence of cold steppe vegetation from ~37,500 to 17,900 cal. a BP",
        "supports_claims": ["C001"]
    },
    {
        "id": "E002",
        "content": "Semidesert vegetation from ~17,900 to 10,300 cal. a BP",
        "evidence_type": "proxy_observation",
        "page": 3,
        "verbatim_quote": "semidesert vegetation from ~17,900 to 10,300 cal. a BP",
        "supports_claims": ["C001"]
    },
    {
        "id": "E003",
        "content": "Forest-steppe vegetation from ~10,300 to 8900 cal. a BP",
        "evidence_type": "proxy_observation",
        "page": 3,
        "verbatim_quote": "forest-steppe vegetation from ~10,300 to 8900 cal. a BP",
        "supports_claims": ["C001"]
    },
    {
        "id": "E004",
        "content": "Mixed oak woods from ~8900 to 4000 cal. a BP",
        "evidence_type": "proxy_observation",
        "page": 3,
        "verbatim_quote": "mixed oak woods from ~8900 to 4000 cal. a BP",
        "supports_claims": ["C001"]
    },
    {
        "id": "E005",
        "content": "Widespread deforestation, burning and grazing followed oak woods phase",
        "evidence_type": "proxy_observation",
        "page": 3,
        "verbatim_quote": "followed by widespread deforestation, burning and grazing",
        "supports_claims": ["C001", "C008"]
    },
    {
        "id": "E006",
        "content": "Early-Holocene forest expansion in Bulgarian Thrace closely followed changes in Black Sea's regional moisture balance",
        "evidence_type": "correlation",
        "page": 3,
        "verbatim_quote": "Early-Holocene forest expansion in Bulgarian Thrace closely followed changes in the Black Sea's regional moisture balance",
        "supports_claims": ["C004"]
    },

    # Claims
    {
        "id": "C001",
        "content": "New record of vegetation, fire and lacustrine sedimentation from Bulgarian Thrace examines environmental change since Last Glacial Maximum",
        "claim_type": "descriptive",
        "page": 3,
        "verbatim_quote": "We present a new record of vegetation, fire and lacustrine sedimentation from Bulgarian Thrace to examine environmental change in this region since the Last Glacial Maximum.",
        "supported_by_evidence": ["E001", "E002", "E003", "E004", "E005"]
    },
    {
        "id": "C002",
        "content": "Thracian Plain was one of the main corridors through which Neolithic agriculture spread into continental Europe",
        "claim_type": "descriptive",
        "page": 3,
        "verbatim_quote": "The Thracian Plain in the SE Balkans was one of the main corridors through which Neolithic agriculture spread into continental Europe.",
        "supported_by_evidence": []
    },
    {
        "id": "C003",
        "content": "Previous studies have invoked rapid sea-level and climatic changes to explain timing of agricultural expansion",
        "claim_type": "citation",
        "page": 3,
        "verbatim_quote": "Previous studies have invoked rapid sea-level and climatic changes to explain the timing of agricultural expansion.",
        "supported_by_evidence": []
    },
    {
        "id": "C004",
        "content": "Early-Holocene forest expansion appears to have been influenced by solar-forced changes in seasonality",
        "claim_type": "causal",
        "page": 3,
        "verbatim_quote": "Early-Holocene forest expansion in Bulgarian Thrace closely followed changes in the Black Sea's regional moisture balance and appears to have been influenced by solar-forced changes in seasonality.",
        "supported_by_evidence": ["E006"]
    },
    {
        "id": "C005",
        "content": "Climatic aridity and/or enhanced seasonality lasting until at least ~8900 cal. a BP could have delayed spread of early agriculture from Aegean coast into continental lowlands of Balkans",
        "claim_type": "causal",
        "page": 3,
        "verbatim_quote": "We suggest that climatic aridity and/or enhanced seasonality – lasting until at least ~8900 cal. a BP – could have delayed the spread of early agriculture from the Aegean coast into the continental lowlands of the Balkans and thence into the rest of Europe.",
        "supported_by_evidence": ["E002", "E003"]
    },
]

# SECTION 2: INTRODUCTION (pages 3-4, lines 50-77)
# Expected: 15-20 claims, 5-8 evidence

introduction_items = [
    # Evidence
    {
        "id": "E007",
        "content": "First agricultural settlements in Bulgarian Thrace date to around 8000 cal. a BP",
        "evidence_type": "archaeological",
        "page": 4,
        "verbatim_quote": "The first agricultural settlements in Bulgarian Thrace date to around 8000 cal. a BP (Boyadziev, 1995, 2009).",
        "supports_claims": ["C013"]
    },
    {
        "id": "E008",
        "content": "Until now there has been no direct palaeoenvironmental evidence from this area to enlighten debate about causes of apparent delay in agricultural expansion",
        "evidence_type": "research_gap",
        "page": 4,
        "verbatim_quote": "Until now there has been no direct palaeoenvironmental evidence from this area to enlighten debate about the causes of the apparent delay in agricultural expansion.",
        "supports_claims": ["C014"]
    },

    # Claims
    {
        "id": "C006",
        "content": "Climate changes during late Pleistocene and early Holocene triggered major migrations of species and biomes in temperate latitudes",
        "claim_type": "citation",
        "page": 3,
        "verbatim_quote": "Climate changes during the late Pleistocene and early Holocene triggered major migrations of species and biomes in temperate latitudes (Roberts, 1998).",
        "supported_by_evidence": []
    },
    {
        "id": "C007",
        "content": "Spread of Neolithic farming into Europe is a potential example of climate-triggered migration",
        "claim_type": "descriptive",
        "page": 3,
        "verbatim_quote": "A potential example of this is the spread of Neolithic farming into Europe, which resulted in the transmission of technology, cultural traditions, genetic heritage and multiple plant and animal species from Western Asia.",
        "supported_by_evidence": []
    },
    {
        "id": "C008",
        "content": "Degree to which environmental change influenced Neolithic transition remains topic of vast scientific debate",
        "claim_type": "citation",
        "page": 3,
        "verbatim_quote": "The degree to which environmental change influenced this complex and essentially cultural event remains the topic of a vast scientific debate",
        "supported_by_evidence": []
    },
    {
        "id": "C009",
        "content": "Rapid environmental changes like 8200 cal. a BP climatic event and Black Sea flood had major impacts on Neolithic transition",
        "claim_type": "citation",
        "page": 4,
        "verbatim_quote": "It has been argued that rapid environmental changes, such as the 8200 cal. a BP climatic event and Black Sea flood, had major impacts on the Neolithic transition",
        "supported_by_evidence": []
    },
    {
        "id": "C010",
        "content": "Precise timing of arrival of Neolithic agriculture in SE Europe remains contentious",
        "claim_type": "citation",
        "page": 4,
        "verbatim_quote": "While the precise timing of the arrival of Neolithic agriculture in SE Europe remains contentious",
        "supported_by_evidence": []
    },
    {
        "id": "C011",
        "content": "General agreement that farming reached Aegean coast somewhat earlier than Balkans' inland valleys and plains",
        "claim_type": "citation",
        "page": 4,
        "verbatim_quote": "there is general agreement that farming reached the Aegean coast somewhat earlier than the Balkans' inland valleys and plains",
        "supported_by_evidence": []
    },
    {
        "id": "C012",
        "content": "Geographical factors mean Thracian Plain is one of probable corridors through which agriculture made its way into rest of Europe",
        "claim_type": "citation",
        "page": 4,
        "verbatim_quote": "Geographical factors mean that the Thracian Plain is one of the probable corridors through which agriculture made its way into the rest of Europe",
        "supported_by_evidence": []
    },
    {
        "id": "C013",
        "content": "There has been apparent delay in agricultural expansion in Bulgarian Thrace",
        "claim_type": "descriptive",
        "page": 4,
        "verbatim_quote": "debate about the causes of the apparent delay in agricultural expansion",
        "supported_by_evidence": ["E007"]
    },
    {
        "id": "C014",
        "content": "Study presents late-Quaternary pollen, non-pollen palynomorph, magnetic susceptibility and charcoal record from formerly Bulgaria's largest inland water body",
        "claim_type": "methodological",
        "page": 4,
        "verbatim_quote": "Here we present a late-Quaternary pollen, non-pollen palynomorph, magnetic susceptibility and charcoal record from a site that was formerly Bulgaria's largest inland water body.",
        "supported_by_evidence": ["E008"]
    },
    {
        "id": "C015",
        "content": "Study addresses three research questions about vegetation response to climate change, environmental influence on Neolithic transition, and palaeological registration of human activity",
        "claim_type": "methodological",
        "page": 4,
        "verbatim_quote": "Our aim is to address the following questions: 1. How did the vegetation of the Thracian Plain respond to climate changes since the Last Glacial Maximum? 2. Could the environment have influenced the Neolithic transition to agriculture? 3. Is Neolithic and later human activity registered palaeoecologically?",
        "supported_by_evidence": []
    },
]

# SECTION 3: REGIONAL SETTING START (page 4, lines 78-86)
# Expected: 6-9 claims, 4-6 evidence

regional_setting_start_items = [
    # Evidence
    {
        "id": "E009",
        "content": "Six Neolithic sites on Thracian Plain and adjacent foothills have been archaeobotanically analysed",
        "evidence_type": "archaeological",
        "page": 5,
        "verbatim_quote": "Archaeobotanically, six Neolithic sites on the Thracian Plain and adjacent foothills have been analysed",
        "supports_claims": ["C019"]
    },
    {
        "id": "E010",
        "content": "Full range of Near Eastern crops was cultivated on Thracian Plain",
        "evidence_type": "archaeological",
        "page": 5,
        "verbatim_quote": "showing that the full range of Near Eastern crops was cultivated here (Marinova 2006; Leshtakov et al. 2007)",
        "supports_claims": ["C019"]
    },

    # Claims
    {
        "id": "C016",
        "content": "Thracian Plain is a fertile basin wedged between mountain chains of Balkans and coastlines of Aegean, Marmara and Black Seas",
        "claim_type": "descriptive",
        "page": 4,
        "verbatim_quote": "The Thracian Plain is a fertile basin wedged between the mountain chains of the Balkans and the coastlines of the Aegean, Marmara and Black Seas.",
        "supported_by_evidence": []
    },
    {
        "id": "C017",
        "content": "Throughout its history, the plain has acted as cultural conduit between East and West, criss-crossed by trade routes and rich in archaeological remains",
        "claim_type": "descriptive",
        "page": 4,
        "verbatim_quote": "Throughout its history, the plain has acted as a cultural conduit between East and West, criss-crossed by trade routes and rich in archaeological remains.",
        "supported_by_evidence": []
    },
    {
        "id": "C018",
        "content": "Thracian Plain was one of main routes by which agriculture made its way into Europe from Western Asia and was home to Europe's earliest metalworking cultures",
        "claim_type": "citation",
        "page": 5,
        "verbatim_quote": "It was one of the main routes by which agriculture made its way into Europe from Western Asia, and was home to Europe's earliest metalworking cultures",
        "supported_by_evidence": []
    },
    {
        "id": "C019",
        "content": "Near Eastern crop suite was cultivated on Thracian Plain during Neolithic",
        "claim_type": "descriptive",
        "page": 5,
        "verbatim_quote": "the full range of Near Eastern crops was cultivated here",
        "supported_by_evidence": ["E009", "E010"]
    },
]

# SECTION 4: REGIONAL SETTING END (pages 4-6, lines 87-112)
# Expected: 10-15 claims, 6-10 evidence

regional_setting_end_items = [
    # Evidence
    {
        "id": "E011",
        "content": "Previous palynological studies of Bulgaria's past vegetation have focussed on mountains or present-day coastlines",
        "evidence_type": "research_gap",
        "page": 5,
        "verbatim_quote": "Previous palynological studies of Bulgaria's past vegetation have focussed on the mountains (e.g. Tonkov et al., 2011; Marinova et al., 2012) or on present-day coastlines (e.g. Filipova, 1985; Bozilova and Beug, 1992).",
        "supports_claims": ["C020"]
    },
    {
        "id": "E012",
        "content": "Mountain sites were too remote from early farming populations to directly register arrival of agriculture and pastoralism",
        "evidence_type": "methodological_limitation",
        "page": 5,
        "verbatim_quote": "Mountain sites were too remote from early farming populations to directly register the arrival of agriculture and pastoralism in the region",
        "supports_claims": ["C020"]
    },
    {
        "id": "E013",
        "content": "Coastal sites began to form as sea-levels rose 8000–6000 years ago, usually missing early-Holocene advent of agriculture altogether",
        "evidence_type": "methodological_limitation",
        "page": 5,
        "verbatim_quote": "while the coastal sites began to form as sea-levels rose 8000–6000 years ago, usually missing the early-Holocene advent of agriculture altogether",
        "supports_claims": ["C020"]
    },
    {
        "id": "E014",
        "content": "Lowlands where most Neolithic settlements were situated lack detailed palaeoenvironmental records",
        "evidence_type": "research_gap",
        "page": 5,
        "verbatim_quote": "The lowlands, where most of the Neolithic settlements were situated, lack detailed palaeoenvironmental records",
        "supports_claims": ["C020", "C021"]
    },
    {
        "id": "E015",
        "content": "Few pollen data that exist from Bulgaria's Thracian Plain miss the early Holocene altogether",
        "evidence_type": "research_gap",
        "page": 5,
        "verbatim_quote": "The few pollen data that exist from Bulgaria's Thracian Plain miss the early Holocene altogether (Filipovitch and Stojanova, 1990; Magyari et al., 2008; Tonkov et al., 2008a, 2009).",
        "supports_claims": ["C021"]
    },
    {
        "id": "E016",
        "content": "Oak pollen never exceeds 20% in mid to late Holocene pollen records from Sadovo and Straldzha",
        "evidence_type": "proxy_observation",
        "page": 5,
        "verbatim_quote": "Oak pollen never exceeds 20% in mid to late Holocene pollen records from Sadovo and Straldzha",
        "supports_claims": ["C023"]
    },
    {
        "id": "E017",
        "content": "Marine sediments from Black Sea provide good evidence for early-mid Holocene expansion of Quercus",
        "evidence_type": "proxy_observation",
        "page": 5,
        "verbatim_quote": "Only marine sediments from the Black Sea provide good evidence for the early-mid Holocene expansion of Quercus",
        "supports_claims": ["C025"]
    },

    # Claims
    {
        "id": "C020",
        "content": "Surprisingly little is known about environmental context of early agriculture on Thracian Plain",
        "claim_type": "descriptive",
        "page": 5,
        "verbatim_quote": "In contrast to other parts of Europe, surprisingly little is known about the environmental context of early agriculture on the Thracian Plain.",
        "supported_by_evidence": ["E011", "E012", "E013", "E014"]
    },
    {
        "id": "C021",
        "content": "Existing pollen data from Thracian Plain miss early Holocene period",
        "claim_type": "descriptive",
        "page": 5,
        "verbatim_quote": "The few pollen data that exist from Bulgaria's Thracian Plain miss the early Holocene altogether",
        "supported_by_evidence": ["E014", "E015"]
    },
    {
        "id": "C022",
        "content": "Previous studies unanimously assert that Thracian Plain was dominated by oak forests prior to clearing associated with agriculture",
        "claim_type": "citation",
        "page": 5,
        "verbatim_quote": "These studies unanimously assert that the Thracian Plain was dominated by oak forests prior to clearing associated with agriculture",
        "supported_by_evidence": []
    },
    {
        "id": "C023",
        "content": "No previous studies provide direct palynological evidence supporting claim of oak forest dominance on Thracian Plain",
        "claim_type": "descriptive",
        "page": 5,
        "verbatim_quote": "but none provide direct palynological evidence that would support such a claim",
        "supported_by_evidence": ["E016"]
    },
    {
        "id": "C024",
        "content": "Authors of Sadovo and Straldzha studies conclude that Thracian Plain's oak forests were destroyed prior to ~4000 cal. a BP",
        "claim_type": "citation",
        "page": 5,
        "verbatim_quote": "leading the authors of these studies to conclude that the Thracian Plain's oak forests were destroyed prior to ~4000 cal. a BP",
        "supported_by_evidence": ["E016"]
    },
    {
        "id": "C025",
        "content": "Marine sediments from Black Sea show early-mid Holocene Quercus expansion",
        "claim_type": "citation",
        "page": 5,
        "verbatim_quote": "Only marine sediments from the Black Sea provide good evidence for the early-mid Holocene expansion of Quercus",
        "supported_by_evidence": ["E017"]
    },
    {
        "id": "C026",
        "content": "Timing of deforestation is unclear from marine records, with some showing abrupt Quercus decline around 6000 cal. a BP and others showing no decline at all",
        "claim_type": "citation",
        "page": 5,
        "verbatim_quote": "the timing of subsequent deforestation is unclear, however, with some marine and coastal records showing an abrupt decline in Quercus around 6000 cal. a BP and others showing no decline at all",
        "supported_by_evidence": []
    },
    {
        "id": "C027",
        "content": "In marine cores, palaeoecological responses to human impact, climatic changes and sea-level rise can be difficult to disentangle",
        "claim_type": "citation",
        "page": 6,
        "verbatim_quote": "In the marine cores, moreover, palaeoecological responses to human impact, climatic changes and sea-level rise can be difficult to disentangle",
        "supported_by_evidence": []
    },
]

# Combine all items from sections 1-4
all_items = (abstract_items + introduction_items +
             regional_setting_start_items + regional_setting_end_items)

# Separate by type
evidence = [item for item in all_items if item['id'].startswith('E')]
claims = [item for item in all_items if item['id'].startswith('C')]

# Add to extraction
data['evidence'].extend(evidence)
data['claims'].extend(claims)

# Save
with open('/home/shawn/Code/llm-reproducibility/outputs/connor-et-al-2013/extraction.json', 'w') as f:
    json.dump(data, f, indent=2)

print(f"Pass 1 Sections 1-4 Extraction Complete!")
print(f"\nItems Extracted:")
print(f"  Evidence: {len(evidence)}")
print(f"  Claims: {len(claims)}")
print(f"  Total: {len(all_items)}")
print(f"\nRunning Totals:")
print(f"  Evidence: {len(data['evidence'])}")
print(f"  Claims: {len(data['claims'])}")
print(f"  Total: {len(data['evidence']) + len(data['claims'])}")
print(f"\nReady for Sections 5-7 extraction")
