# Research Design Extraction Guide

**Purpose:** Operational guidance for extracting 4-6 research designs per paper (vs common under-extraction of 1-2)

**Context:** Research designs are strategic-level decisions (WHY research was framed this way). They appear throughout paper but are often missed because they feel "too obvious" or get misclassified as methods.

---

## Section 1: The Chatbot's Success - 10 Practices That Worked

A chatbot extraction achieved 5 RDs where current extractions get 2. Analysis of its success reveals these practices:

### 1. Read Fundamentals First
**What:** Actually read `extraction-fundamentals.md` BEFORE starting extraction
**Why:** Grounded in sourcing requirements and explicit/implicit distinction from beginning

### 2. Internalized the "WHY" Test
**What:** Consistently asked "Does this explain WHY research was framed this way?"
**Why:** Sharp distinction between rationale (Design) vs approach (Method) vs procedure (Protocol)

### 3. Recognized Multiple Design Types
**What:** Didn't just hunt for research questions. Extracted:
- Research questions and hypotheses
- Study design decisions with rationale
- Theoretical frameworks

**Why:** Schema supports 5 design_type values - using full taxonomy increases coverage

### 4. Paid Close Attention to Introduction/Background
**What:** Most Research Designs live in Abstract/Introduction, not Methods
**Why:** Strategic framing appears early; methods describe execution

### 5. Looked for "Design Language" Keywords
**What:** Actively scanned for decision/rationale/purpose language
**Why:** These phrases signal design-level thinking vs procedural description

### 6. Distinguished Description from Rationale
**What:** "Three activities undertaken" = Design (structure). Each activity's procedure = Method/Protocol
**Why:** Framing is design-level; execution is method/protocol-level

### 7. Captured Design Philosophy as Design
**What:** High-level/abstract workflow philosophy = Research Design
**Why:** Explains WHY they structured workflow (strategic thinking)

### 8. Recognized Theoretical Frameworks as Designs
**What:** Theoretical frameworks ARE Research Designs (not just background)
**Why:** They ground design choices conceptually

### 9. Was Liberal in Pass 1
**What:** Took "when in doubt, include it" seriously for Research Designs
**Why:** Even "obvious" or "too meta" items should be extracted if they explain WHY

### 10. Read for Meta-Level Framing
**What:** Recognized paper isn't just describing what they did - it's testing a design hypothesis
**Why:** Meta-level awareness catches holistic designs (comparative evaluation AS strategic choice)

---

## Section 2: Pre-Scan Checklist

**Before extracting anything, spend 2-3 minutes scanning:**

### Abstract Section
- [ ] Research questions stated?
- [ ] Hypotheses stated?
- [ ] Study framing language ("comparative," "case study," "exploratory")?
- [ ] Aims or objectives?

### Introduction Section
- [ ] Research context and rationale?
- [ ] Gap in knowledge being addressed?
- [ ] Strategic choices explained ("We chose X because...")?
- [ ] Theoretical positioning?

### Background/Literature Review Section
- [ ] Theoretical frameworks referenced?
- [ ] Conceptual grounding discussed?
- [ ] Prior approaches critiqued (setting up design choice)?
- [ ] ⚠️ **Don't extract others' designs** (test: "Smith et al." = not ours)

### Methods/Approach Section
- [ ] Study design rationale explained?
- [ ] Framework application described?
- [ ] Design justification provided?
- [ ] Comparative/evaluative framing?

**Mark passages with decision/rationale/purpose/framework language for Step 1 extraction.**

---

## Section 3: Design Types & Classification

### When to Use Each design_type:

**`research_framing`** - Use when extracting:
- Research questions explicitly stated
- Hypotheses with predictions
- Emergent findings framed as post-hoc hypotheses
- Critical for assessment: Captures hypothesis timing (pre/post-data) for HARKing detection

**`theoretical_framework`** - Use when extracting:
- Named theories grounding research (e.g., "Nielsen's usability principles")
- Conceptual frameworks guiding design
- Paradigmatic positioning (positivist, interpretivist, etc.)
- Critical for assessment: Theoretical grounding vs purely empirical work

**`study_design`** - Use when extracting:
- Study structure choices (case study, comparative, longitudinal, experimental)
- Design rationale ("We chose comparative because...")
- Strategic approach decisions
- Critical for assessment: Transparency of strategic choices

**`scope_definition`** - Use when extracting:
- Spatial/temporal/thematic boundaries with justification
- Inclusion/exclusion criteria with rationale
- Sampling frame decisions

**`positionality`** - Use when extracting:
- Researcher positioning statements
- Reflexivity about bias/perspective
- Standpoint epistemology

### Decision Tree:

```
Does it state a question or hypothesis?
├─ YES → research_framing
└─ NO → Does it reference theory grounding choices?
    ├─ YES → theoretical_framework
    └─ NO → Does it explain study structure choice?
        ├─ YES → study_design
        └─ NO → Does it justify boundaries?
            ├─ YES → scope_definition
            └─ NO → Does it position researcher?
                ├─ YES → positionality
                └─ NO → Probably not a Research Design (may be method)
```

---

## Section 4: Meta-Level Framing Patterns

**Most commonly missed Research Designs are meta-level framings that feel "obvious":**

### Pattern 1: Comparative Evaluation AS Design Choice
**Example:** "We conducted a comparative evaluation to test efficiency thresholds"
**Why it's missed:** Seems like description of what they did
**Why it's a Design:** Comparison is a STRATEGIC CHOICE requiring justification

**Extract as:**
- design_type: `study_design`
- design_text: Statement of comparative evaluation purpose/rationale
- Critical for assessment: Was comparison justified? Pre-planned vs post-hoc?

### Pattern 2: Case Study AS Deliberate Decision
**Example:** "We employed a case study design to demonstrate transferability"
**Why it's missed:** Entire paper is obviously a case study
**Why it's a Design:** Case study is a CHOICE with alternatives (survey, experiment, etc.)

**Extract as:**
- design_type: `study_design`
- design_text: Case study choice + rationale (if provided)

### Pattern 3: Exploratory Stance AS Strategic Framing
**Example:** "We adopted an exploratory approach to identify emergent patterns"
**Why it's missed:** Seems like description of analysis method
**Why it's a Design:** Exploratory vs confirmatory is STRATEGIC LEVEL decision

**Extract as:**
- design_type: `research_framing` (if framed as research question/approach)
- Captures critical assessment info: Exploratory (hypothesis-generating) vs confirmatory (hypothesis-testing)

### Pattern 4: Platform/Tool Selection Rationale
**Example:** "We chose FAIMS Mobile for offline capability and usability"
**Why it's missed:** Seems like method description
**Why it's a Design:** IF rationale provided, it's a strategic choice (WHY chosen)

**Extract as:**
- design_type: `study_design`
- Only if rationale present (not just "We used X")

---

## Section 5: NOT a Design → IS a Design (Counter-Examples)

### Set 1: Description vs Rationale

❌ **NOT a Design:** "We used FAIMS Mobile"
✅ **IS a Design:** "We chose FAIMS Mobile for offline capability and usability"

❌ **NOT a Design:** "Data were collected via survey"
✅ **IS a Design:** "We selected survey methodology to cover large spatial area efficiently"

❌ **NOT a Design:** "We analyzed patterns"
✅ **IS a Design:** "We adopted an exploratory analytical framework to identify emergent patterns"

❌ **NOT a Design:** "Students participated"
✅ **IS a Design:** "We recruited field school students as novice volunteers to test generalizability"

### Set 2: Method vs Design Boundary

❌ **NOT a Design:** "Systematic transect survey with 20% coverage" (WHAT was done)
✅ **IS a Design:** "We chose systematic over opportunistic survey to ensure unbiased spatial sampling" (WHY chosen)

❌ **NOT a Design:** "GPS coordinates recorded at each artifact" (HOW implemented)
✅ **IS a Design:** "We employed GPS-based documentation to enable spatial analysis" (WHY approach)

### Set 3: Too Obvious ≠ Skip Extraction

❌ **WRONG:** "This paper is obviously a case study, no need to extract"
✅ **RIGHT:** "Case study design is a strategic choice - extract with rationale if provided"

❌ **WRONG:** "Comparative evaluation is just what they did, not a design"
✅ **RIGHT:** "Comparative evaluation is meta-level strategic framing - extract it"

---

## Section 6: Worked Example - Sobotkova et al. 2023 (4-6 RDs)

**Paper:** Creating large, high-quality geospatial datasets from historical maps using novice volunteers

**What 4-6 RD extraction looks like:**

### RD001: Research Goal/Aims (research_framing)
**Text:** "Assess whether mobile crowdsourcing with novice volunteers can produce high-quality geospatial data from historical maps"
**Location:** Abstract, Introduction
**Why extracted:** Explicit research question framing entire study

### RD002: Case Study Design Choice (study_design)
**Text:** "Single case study design to demonstrate approach in real-world archaeological field school context"
**Location:** Introduction, Methods
**Why extracted:** Strategic choice of case study over multi-site comparison (with implicit rationale: depth over breadth)

### RD003: Comparative Evaluation Framework (study_design)
**Text:** "Comparative evaluation design to assess digitization approach efficiency thresholds relative to desktop GIS baseline"
**Location:** Introduction, Methods
**Why extracted:** Meta-level framing - comparison AS strategic design decision to enable threshold assessment

### RD004: Efficiency Threshold Hypothesis (research_framing)
**Text:** "Hypothesis that mobile crowdsourcing becomes most efficient for datasets between 10,000-60,000 features"
**Location:** Introduction, Discussion
**Why extracted:** Explicit hypothesis about when approach is viable (critical for assessment: pre-data or post-hoc?)

### RD005: Mobile Platform Selection Rationale (study_design)
**Text:** "Selection of FAIMS Mobile platform for offline capability, customizability, and reduced training burden"
**Location:** Methods
**Why extracted:** Strategic choice with explicit rationale (WHY this platform vs alternatives)

### RD006 (Optional): Novice Volunteer Strategy (study_design)
**Text:** "Deliberate use of field school students as novice volunteers to test approach generalizability beyond expert users"
**Location:** Methods, Discussion
**Why extracted:** Strategic decision to use novices (not just convenience) to test scalability

**Result:** 5-6 distinct strategic decisions, each with independent justification, enabling separate transparency assessment

---

## Section 7: Quality Checks

### Count-Based Checks (Guidelines, Not Targets)

**If <3 Research Designs:**
- [ ] Re-scan Abstract/Introduction for research questions/aims
- [ ] Check: Did I extract meta-level framing (comparative evaluation, case study rationale)?
- [ ] Check: Did I recognize theoretical frameworks as RDs?
- [ ] Check: Did I distinguish design rationale from method description?
- [ ] Check: Did I overcome "too obvious" hesitation?

**If >10 Research Designs:**
- [ ] Check: Does each RD have independent justification?
- [ ] Check: Am I extracting methods/protocols as designs?
- [ ] Check: Am I fragmenting single decisions into multiple RDs?
- [ ] Consider consolidation in Pass 2 if genuinely redundant

**Quality Over Count:**
- Extract what's genuinely present in the paper
- Paper-dependent: Some papers have 2 legitimate RDs, others have 8
- Goal is completeness and accuracy, not hitting a number

### Common Consolidation Mistakes to Avoid

**DON'T consolidate:**
- ✗ Research question + hypothesis (separate strategic elements)
- ✗ Case study choice + comparative evaluation (distinct design decisions)
- ✗ Theoretical framework + empirical approach (different design types)
- ✗ Multiple rationales for different choices (even if related)

**DO consolidate:**
- ✓ Three statements of same research question (redundant restatement)
- ✓ Multiple justifications for single decision (rationale synthesis)
- ✓ Spatial + temporal scope if presented as unified boundary

---

## Section 8: Future Watch - Known Challenges

### Literature Review Misattribution (Monitoring Status: Green)

**Challenge:** Accidentally extracting prior work's designs as current paper's designs

**Risk Level:** Moderate (not yet systematically observed)

**Current Mitigations:**
- Lit review warning in Pass 1 prompt (4 lines)
- Verbatim quotes capture attribution context ("Smith et al.")
- Location field tags Background/Literature Review sections
- "WHY test" requires decision by AUTHORS, not others

**Escalation Triggers:**
- If >10% of RDs in validation show misattribution to prior work
- If systematic pattern emerges across multiple papers

**Escalation Action:**
- Expand to full disambiguation section in this guide
- Add worked examples showing correct attribution
- Enhance validation checks for author vs cited work distinction

**Current Status:** No action needed - existing mitigations sufficient

### Other Potential Challenges (Not Yet Observed)

**Over-extraction from hypothetical scenarios:**
- Papers discussing "one could also..." or "future work might..."
- Mitigation: Verbatim quotes should make hypothetical language visible

**Confusion of limitations with design choices:**
- "We were limited to..." vs "We chose to limit..."
- Mitigation: Design requires CHOICE, not constraint

---

## Section 9: Reasoning Approach Classification

**Purpose:** Classify research designs by reasoning approach (inductive, abductive, deductive, mixed, unclear)

**Critical for assessment:** Hypothesis timing (pre-data vs post-data), theoretical grounding, research transparency

### The Five Reasoning Approaches

#### Inductive - Data to patterns to theory

**Characteristics:**
- Exploratory, pattern discovery, grounded theory
- No pre-stated hypotheses
- Theory emerges from data

**Indicators:**
- "emerged from"
- "patterns suggested"
- "we observed"
- "grounded in data"

**Example:** "Patterns of artifact distribution emerged from spatial analysis"

#### Abductive - Anomaly to best explanation

**Characteristics:**
- Puzzle-solving, inference to best explanation
- Anomaly or surprising finding drives inquiry
- Retroductive reasoning

**Indicators:**
- "surprising finding"
- "best explained by"
- "accounts for"
- "puzzle of"

**Example:** "The unexpected ceramic assemblage is best explained by trade networks"

#### Deductive - Theory to predictions to test

**Characteristics:**
- Hypothesis testing, theory verification
- Pre-stated predictions
- Confirmatory analysis

**Indicators:**
- "we hypothesized"
- "predicted"
- "tested whether"
- "expected that"

**Example:** "We hypothesized that platform efficiency would exceed desktop GIS for datasets >10,000 features"

#### Mixed - Genuine combination (NOT default)

**Characteristics:**
- Explicit integration of approaches
- Must show BOTH exploratory AND confirmatory phases
- Sequential or integrated combination

**Important:** Don't default to "mixed" - requires explicit evidence

**Indicators:**
- "Exploratory phase identified patterns, confirmatory phase tested hypotheses"
- "We first explored X, then tested predictions about Y"

**Example:** "Initial exploratory analysis identified efficiency patterns; subsequent phase tested specific threshold hypotheses"

#### Unclear - Insufficient information

**Use when:**
- Approach not explicitly stated
- Cannot be reliably inferred from content
- Ambiguous or contradictory indicators

**Don't use "unclear" as default** - attempt to infer from available information first

### Classification Workflow

**Step 1:** Look for explicit statements about approach
- Check Introduction, Methods sections
- Look for methodological positioning

**Step 2:** Check hypothesis timing
- **Pre-data:** Hypotheses stated in Introduction/Methods before Results
- **Post-data:** Hypotheses first mentioned in Results/Discussion, or marked as "emerged"
- **Critical:** Pre-data = deductive; post-data = inductive/abductive

**Step 3:** Assess confidence level
- High: Explicit statement of approach
- Medium: Strong indicators, clear timing
- Low: Inferred from limited evidence

**Step 4:** Document reasoning
- Include in `extraction_notes` or research design object
- Note evidence for classification
- Flag if uncertain

### Hypothesis Timing Inference

**Critical for detecting HARKing (Hypothesising After Results are Known)**

#### Pre-Data Indicators

**Strong evidence:**
- Hypotheses stated in Abstract or Introduction
- "We predicted..." or "We hypothesized..." before Results
- Registered study design (rare in fieldwork)

**Medium evidence:**
- Hypotheses in Methods section
- Timing ambiguous but likely pre-data

#### Post-Data Indicators

**Strong evidence:**
- Hypotheses first appear in Results or Discussion
- Language: "emerged," "suggested," "we observed"
- Marked as "unexpected" or "surprising"

**Medium evidence:**
- Timing unclear but language suggests discovery

**Document:**
- Timing basis (section location, language used)
- Confidence level (high, medium, low)
- Implications for assessment (HARKing risk)

### Verification (Pass 2)

**Check claimed vs inferred consistency:**
- If `explicit_statement` present → should match `inferred_approach`
- If mismatch → document in `extraction_notes`, flag for review

**Verify hypothesis timing inference:**
- Cross-check section locations
- Verify language indicators
- Assess confidence level

**Mixed vs Unclear distinction:**
- Mixed requires evidence of BOTH exploratory AND confirmatory
- Don't default to "mixed" - use "unclear" if insufficient information

**Common errors:**
- Assuming "mixed" when approach not stated
- Missing post-data hypothesis timing (HARKing)
- Over-inferring from weak indicators

---

## Section 10: Research Questions vs Hypotheses

**Purpose:** Distinguish research questions from hypotheses, assess timing implications

**Critical for:** Detecting HARKing, assessing research transparency, understanding reasoning approach

### The Core Distinction

#### Research Questions - Open-ended inquiry

**Characteristics:**
- No specific prediction
- Exploratory stance
- "How" or "What" framing

**Examples:**
- "How does X affect Y?"
- "What is the relationship between X and Y?"
- "What factors influence Z?"

**Reasoning approach:** Typically inductive or abductive

#### Hypotheses - Specific predictions

**Characteristics:**
- Testable prediction
- Confirmatory stance
- Directional or specific expectation

**Examples:**
- "X will increase Y"
- "X is positively correlated with Y"
- "We hypothesized that efficiency would exceed baseline by >50%"

**Reasoning approach:** Typically deductive

### The Timing Distinction

**Critical question:** When was this formulated?

#### Pre-Data (Planned)

**Indicators:**
- Stated in Abstract, Introduction, or Methods
- Before Results section
- Language: "We asked," "We hypothesized," "We predicted"

**Implications:**
- Planned inquiry (transparent)
- Deductive reasoning (if hypothesis)
- Lower HARKing risk

#### Post-Data (Emergent)

**Indicators:**
- First mentioned in Results or Discussion
- Language: "emerged," "suggested," "we observed," "unexpected"
- Marked as discovery

**Implications:**
- Exploratory discovery (acceptable if acknowledged)
- Inductive/abductive reasoning
- HARKing risk if presented as pre-data

### Extraction Guidance

**Document in research design object:**
- `design_type`: "research_framing"
- `design_text`: The question or hypothesis verbatim
- `reasoning_approach`: Based on RQ vs hypothesis + timing
- `extraction_notes`: Timing basis, confidence level

**For research questions:**
```json
{
  "design_id": "RD001",
  "design_type": "research_framing",
  "design_text": "How does mobile crowdsourcing efficiency compare to desktop GIS for archaeological georeferencing?",
  "reasoning_approach": {
    "claimed_approach": "unclear",
    "inferred_approach": "inductive",
    "timing_basis": "Research question stated in Introduction, no specific predictions",
    "confidence": "medium"
  }
}
```

**For hypotheses:**
```json
{
  "design_id": "RD002",
  "design_type": "research_framing",
  "design_text": "We hypothesized that mobile crowdsourcing becomes most efficient for datasets between 10,000-60,000 features",
  "reasoning_approach": {
    "claimed_approach": "deductive",
    "inferred_approach": "deductive",
    "hypothesis_timing": "pre-data",
    "timing_basis": "Hypothesis stated in Introduction before data collection",
    "confidence": "high"
  }
}
```

### If Unclear

**Flag in `extraction_notes`:**
- "Timing unclear - hypothesis mentioned in Methods but may be post-hoc"
- "Language ambiguous - presented as prediction but first appears in Discussion"

**Document reasoning:**
- Evidence for pre-data vs post-data
- Confidence level
- Assessment implications

**Pass 2 verification:**
- Cross-check section locations
- Verify language indicators
- Resolve ambiguities if possible

---

## Section 11: Fieldwork-Specific Considerations

**Purpose:** Recognise and document fieldwork-specific methodological patterns

**Applies to:** Archaeological surveys, ethnographic fieldwork, ecological surveys, biological field studies

### Pattern 1: Opportunistic Decisions

**Definition:** Unplanned adaptations made during fieldwork in response to field conditions

**Characteristics:**
- Not pre-planned
- Responsive to discoveries or conditions
- Documented as methodological adaptations

**Examples:**
- "Extended survey area due to high artifact density"
- "Added interview protocol based on emergent themes"
- "Increased sampling intensity where rare species observed"

**Extraction:**
- Mark as `opportunistic: true` in relevant RDMAP item
- Document in `extraction_notes`: Why change was made
- Note in `expected_information_missing` if justification lacking

**Example:**
```json
{
  "method_id": "M005",
  "method_text": "Extended pedestrian survey to additional 5 ha area based on observed artifact density",
  "opportunistic": true,
  "extraction_notes": "Methodological adaptation during fieldwork - responded to discovery of dense artifact scatter"
}
```

### Pattern 2: Contingency Plans

**Definition:** Pre-planned IF-THEN responses to anticipated field conditions

**Characteristics:**
- Pre-planned alternatives
- Documented in advance (ideally)
- Conditional protocols

**Examples:**
- "If GPS unavailable, use total station for backup positioning"
- "If weather prevents outdoor surveys, conduct indoor interviews"
- "If sample size <30, increase sampling effort or adjust analysis"

**Extraction:**
- Extract as protocols with `contingent: true`
- Document trigger condition
- Note whether actually triggered

**Example:**
```json
{
  "protocol_id": "P007",
  "protocol_text": "If GPS signal unavailable (accuracy >10m), use total station with ±1cm accuracy for feature positioning",
  "contingent": true,
  "extraction_notes": "Pre-planned contingency protocol - triggered in 3 of 22 sites due to heavy tree cover"
}
```

### Pattern 3: Emergent Discoveries

**Definition:** Patterns or hypotheses discovered during data collection or analysis

**Characteristics:**
- Not pre-planned
- Discovered from data
- May lead to post-hoc hypotheses

**Examples:**
- "Unexpected ceramic pattern suggested trade networks"
- "Artifact distribution revealed previously unknown site structure"
- "Efficiency threshold emerged at ~25,000 features"

**Extraction:**
- Mark hypothesis timing in research questions/hypotheses
- Document emergence in `extraction_notes`
- Extract as research design with `hypothesis_timing: "post-data"`

**Example:**
```json
{
  "design_id": "RD003",
  "design_type": "research_framing",
  "design_text": "Analysis revealed efficiency threshold at approximately 25,000 features where mobile platform advantages diminish",
  "reasoning_approach": {
    "inferred_approach": "inductive",
    "hypothesis_timing": "post-data",
    "timing_basis": "Pattern emerged during analysis, first mentioned in Results section",
    "confidence": "high"
  },
  "extraction_notes": "Emergent finding - not pre-stated hypothesis. Discovered during comparative efficiency analysis."
}
```

### Fieldwork Transparency Assessment

**Key questions for assessment:**
- Were opportunistic changes documented and justified?
- Were contingency plans pre-specified or post-hoc?
- Were emergent discoveries acknowledged as such?
- Is there sufficient documentation to assess validity of adaptations?

**Expected information for fieldwork:**
- Justification for opportunistic changes
- Trigger conditions for contingencies
- Acknowledgment of emergent vs planned findings
- Field notes or documentation supporting adaptations

**Common gaps:**
- Opportunistic changes not documented
- Contingencies presented as if they were primary plan
- Post-hoc hypotheses presented as pre-data
- Insufficient justification for methodological adaptations

---

## Quick Reference

**Pre-scan:** Abstract, Intro, Background, Methods/Approach for design elements (2-3 min)

**Design language keywords:** chose, selected, because, aimed to, framework, compared

**5 design types:** research_framing, theoretical_framework, study_design, scope_definition, positionality

**"Too obvious" rule:** If it feels obvious/meta-level → extract it anyway (that's strategic framing)

**Meta-level patterns:** Comparative evaluation, case study choice, exploratory stance = Designs

**Count guidance:** <3 review for under-extraction, >10 review for over-extraction, quality > count

**Critical for assessment:** Hypothesis timing (pre/post-data), theoretical grounding, design rationale
