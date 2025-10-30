# Expected Information Checklists

## Purpose

These checklists help identify what information SHOULD be present but is MISSING from research papers. We don't penalize absence - we document it for transparency assessment.

## Core Principle

**Expected information varies by:**
- Research domain (archaeology vs biology vs ethnography)
- Method type (survey vs experimental vs computational)
- Claim type (quantitative vs qualitative vs causal)

## Universal Checklists

### For All Quantitative Claims

- [ ] Method specified?
- [ ] Error margins or confidence intervals provided?
- [ ] Sample size reported?
- [ ] Precision justified?
- [ ] Measurement units clear?

### For All Comparative Claims

- [ ] Basis of comparison explicit?
- [ ] What was held constant?
- [ ] Alternative explanations considered?
- [ ] Statistical significance (if applicable)?

### For All Causal Claims

- [ ] Mechanism proposed?
- [ ] Alternative causes ruled out?
- [ ] Temporal sequence established?
- [ ] Confounding factors addressed?

### For All Methods

- [ ] Method choice justified?
- [ ] Alternative methods considered?
- [ ] Implementation details sufficient for replication?
- [ ] Limitations acknowledged?

### For All Measurements

- [ ] Instrument/tool specified?
- [ ] Precision/accuracy reported?
- [ ] Calibration described?
- [ ] Quality control procedures?
- [ ] Observer/operator identified?

## Domain-Specific Checklists

### Archaeology (Field Survey)

**Spatial Data Collection:**
- [ ] GPS device and settings
- [ ] Accuracy specifications
- [ ] Datum/coordinate system
- [ ] Visibility conditions
- [ ] Survey coverage calculation method

**Artifact Recording:**
- [ ] Classification system used
- [ ] Diagnostic vs non-diagnostic criteria
- [ ] Measurement protocols
- [ ] Photography standards
- [ ] Spatial precision for artifacts

**Site Definition:**
- [ ] Artifact density thresholds
- [ ] Site boundary criteria
- [ ] Inter-site spacing rules
- [ ] Feature identification criteria

### Biology (Field Sampling)

**Specimen Collection:**
- [ ] Sampling protocol (transect, quadrat, trap)
- [ ] Sample size justification
- [ ] Collection technique
- [ ] Temporal parameters (time of day, season)
- [ ] Environmental conditions

**Species Identification:**
- [ ] Identification criteria
- [ ] Reference materials used
- [ ] Expert consultation
- [ ] Voucher specimens
- [ ] Confidence assessment

**Measurement Protocols:**
- [ ] Measurement techniques
- [ ] Instrument precision
- [ ] Observer training
- [ ] Inter-observer reliability
- [ ] Quality control

### Ethnography (Interviews/Observation)

**Participant Recruitment:**
- [ ] Selection criteria
- [ ] Recruitment method
- [ ] Response rate (if applicable)
- [ ] Demographic characteristics
- [ ] Sampling rationale

**Data Collection:**
- [ ] Interview structure (structured/semi-structured)
- [ ] Question development process
- [ ] Recording method
- [ ] Interviewer positionality
- [ ] Saturation assessment

**Analysis:**
- [ ] Coding framework
- [ ] Inter-coder reliability
- [ ] Member checking
- [ ] Triangulation methods
- [ ] Reflexivity practices

### Literary Studies / Philology

**Primary Source Evidence:**
- [ ] ALL ancient text citations extracted as evidence (not just block quotes)
- [ ] Inline citations to primary sources captured (e.g., "Il. 2.802-6", "Hdt. 8.144")
- [ ] Passing mentions of primary texts included (e.g., "Unlike in Od. 19.172...")
- [ ] Comparative references to other texts/versions recorded
- [ ] Manuscript/edition information specified when discussed

**Decision Rule:**
"When paper references ancient text → evidence item"

Includes:
- Direct quotations (block quotes with translations)
- Inline citations by reference (Il. X.Y, Od. X.Y, Hdt. X.Y)
- Paraphrased passages from primary sources
- Comparative references ("Similar to Hymn to Aphrodite...")
- Manuscript variant discussions

**Why This Matters:**
In literary scholarship, every reference to a primary source is an act of evidence selection. What the scholar chooses to cite—and what they omit—is methodologically significant.

**Common Omissions:**
- [ ] Passing textual references not extracted as evidence
- [ ] Comparative examples mentioned but not captured
- [ ] Critical edition information missing
- [ ] Translation choices not documented
- [ ] Dating/authorship assumptions not explicit

## Sampling Checklists

### Probability Sampling
- [ ] Sampling frame defined
- [ ] Selection method (random/systematic/stratified)
- [ ] Sample size calculation
- [ ] Achieved sample vs target
- [ ] Non-response bias assessment

### Non-Probability Sampling
- [ ] Sampling strategy (purposive/convenience/snowball)
- [ ] Selection criteria
- [ ] Saturation justification
- [ ] Transferability considerations
- [ ] Limitations acknowledged

## Statistical Analysis Checklists

### For Regression Models
- [ ] Model specification
- [ ] Variable definitions
- [ ] Model selection process
- [ ] Assumptions tested
- [ ] Diagnostics reported
- [ ] Effect sizes with confidence intervals
- [ ] Software and version

### For Descriptive Statistics
- [ ] Measures of central tendency
- [ ] Measures of spread
- [ ] Distribution characteristics
- [ ] Sample size for each statistic
- [ ] Missing data handling

## Quality Control Checklists

### Data Collection QC
- [ ] Training procedures
- [ ] Pilot testing
- [ ] Inter-observer reliability
- [ ] Calibration protocols
- [ ] Error detection methods
- [ ] Correction procedures

### Data Processing QC
- [ ] Validation checks
- [ ] Error rates reported
- [ ] Outlier treatment
- [ ] Missing data handling
- [ ] Version control
- [ ] Data backup procedures

## How to Use

### During Pass 1 Extraction:
1. Identify method/claim type
2. Consult relevant checklist
3. Note missing items in `expected_information_missing` array
4. Don't penalize - just document

### During Pass 2 Rationalization:
1. Review aggregated missing information
2. Flag critical gaps (assessment blockers)
3. Note patterns of missing information

### During Assessment:
1. Use missing information to inform transparency scores
2. Distinguish: unavailable vs unreported
3. Consider domain norms

## Comprehensive Checklists

Full, detailed domain-specific checklists with examples are available in project knowledge:
- Archaeology checklists (survey, excavation, analysis)
- Biology checklists (field, lab, statistical)
- Ethnography checklists (qualitative methods)

These can be consulted for comprehensive expected information frameworks.

## Remember

- **Absence is data** - Document what's missing, don't ignore it
- **Context matters** - Expected information varies by domain and method
- **Don't penalize** - These are transparency indicators, not quality judgments
- **Be systematic** - Apply checklists consistently
- **Flag critical gaps** - Note when absence blocks assessment
