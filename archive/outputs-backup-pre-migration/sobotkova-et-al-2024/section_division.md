# Section Division Plan for RUN-10

**Paper:** Sobotkova et al. 2024 - Validating predictions of burial mounds

**Total estimated words:** ~9,000 (excluding references)

**Target:** 4-8 section groups, ~1000 words each (max 1500)

## Section Groups

### Group 1: Abstract + Introduction + Background (Lines 21-253)
**Estimated words:** ~2,400
**Sections included:**
- Abstract (Purpose, Design/methodology/approach, Findings, etc.)
- Introduction (ML in archaeology, CNNs, literature review)
- Burial mounds as heritage under threat
- Detecting archaeological features in satellite imagery

**Rationale:** Combines abstract, intro, and contextual background sections. Provides research context, problem statement, and feature characteristics.

### Group 2: Automated Approaches + Data (Lines 255-373)
**Estimated words:** ~1,500
**Sections included:**
- Automated approaches to remotely sensed data (literature review, adoption trends, publication bias analysis)
- Data
  - Pedestrian survey
  - Satellite imagery

**Rationale:** Covers literature positioning and data description. Natural grouping of context and data sources.

### Group 3: Methods + Results (Lines 376-559)
**Estimated words:** ~2,200
**Sections included:**
- Methods
  - Transfer learning
  - Additional CNN training (training data preparation, training execution)
  - Assessment (performance evaluation, model validation against field data)
- Results
  - First run (2021): full training dataset
  - Second run (2022): training data filtered for visible mounds only

**Rationale:** Combines methodology and empirical outcomes. Natural flow from "how we did it" to "what we found".

### Group 4: Discussion + Conclusion (Lines 562-764)
**Estimated words:** ~2,500
**Sections included:**
- Discussion
  - Limitations and challenges of pre-trained CNNs
  - Building a better model
  - Is it worth it?
- Conclusion

**Rationale:** Combines interpretation, limitations, and conclusions. Natural grouping of analytical synthesis and takeaways.

## Word Count Verification

- Group 1: ~2,400 words (within acceptable range, below 2,500 threshold where split would be needed)
- Group 2: ~1,500 words (perfect target size)
- Group 3: ~2,200 words (acceptable, within range)
- Group 4: ~2,500 words (acceptable, within range)

**Total groups:** 4 (within 4-8 recommended range)

## Equal Attention Strategy

**CRITICAL:** Apply equal attention to ALL section groups, not just Methods/Results.

- **Group 1** (Abstract+Intro+Background): High potential for research designs, claims about problem significance, implicit arguments about ML adoption and limitations
- **Group 2** (Automated+Data): Claims about literature trends, evidence about publication bias, data characteristics
- **Group 3** (Methods+Results): Methods, protocols, evidence (quantitative findings), claims about model performance
- **Group 4** (Discussion+Conclusion): Core claims, implicit arguments, research design reflections, methodological insights

## Extraction Order

1. Extract Group 1 → Save to extraction.json → Update extraction_notes
2. Extract Group 2 → Save to extraction.json → Update extraction_notes
3. Extract Group 3 → Save to extraction.json → Update extraction_notes
4. Extract Group 4 → Save to extraction.json → Update extraction_notes

All groups will be extracted in this single Pass 1 session without stopping between groups (autonomous execution mode).
