# RDMAP Tier Assignment Guide

## The Three-Tier Hierarchy

**Research Designs** (Strategic Level - WHY)
**Methods** (Tactical Level - WHAT) 
**Protocols** (Operational Level - HOW)

## Decision Framework

### Start Here: The Core Questions

For any methodological statement, ask these three questions in order:

**Q1: "Is this about WHY the research was framed this way?"**
- YES → Research Design
- NO → Continue to Q2

**Q2: "Is this about WHAT was done at a high level?"**
- YES → Method
- NO → Continue to Q3

**Q3: "Is this about HOW it was specifically implemented?"**
- YES → Protocol

## Tier-Specific Indicators

### Research Design Indicators

**Framing & Rationale:**
- Research questions
- Hypotheses
- Theoretical frameworks
- Study design justification
- Scope definition
- Positionality statements

**Key phrases:**
- "We aimed to..."
- "The research question was..."
- "We hypothesized that..."
- "We adopted a [comparative/longitudinal/case study] design because..."
- "Our theoretical framework..."

**Test:** "Does this explain the strategic choices that shaped the research?"

### Research Design Granularity Principle

**Key principle:** Each strategic decision requiring independent justification = separate Research Design.

**Design language keywords that signal strategic decisions:**
- Decision points: "chose," "selected," "decision to"
- Rationale: "because," "rationale," "reasoning"
- Purpose: "sought to," "aimed to," "designed to"
- Grounding: "framework," "guided by," "informed by"

**When to extract as SEPARATE designs:**
✓ Different rationales provided (even for related choices)
✓ Independent assessment possible (could evaluate transparency separately)
✓ Distinct strategic questions ("Why X?" vs "Why Y?")

**When to keep as ONE design:**
✓ Single unified rationale
✓ Genuinely inseparable decisions

**Quick counter-example:**
- ❌ "We used FAIMS Mobile" → Method (describes WHAT)
- ✅ "We chose FAIMS Mobile for offline capability and usability" → Design (explains WHY with rationale)

**Important notes:**
- Theoretical frameworks ARE Research Designs (they ground design choices)
- Most Research Designs appear in Abstract/Introduction/Background, NOT only in Methods
- Design elements often feel "too high-level" - extract them anyway for transparency assessment

### Method Indicators

**General Approaches:**
- Data collection approach (survey, excavation, etc.)
- Sampling strategy
- Analysis technique
- Quality control approach
- Validation method

**Key phrases:**
- "We used [survey/experimental/ethnographic] methods"
- "Data were collected through..."
- "We employed [stratified sampling/cluster sampling]"
- "Analysis involved..."
- "We validated using..."

**Test:** "Is this describing the general approach without implementation details?"

### Protocol Indicators

**Specific Implementations:**
- Exact procedures
- Tool configurations
- Parameter specifications
- Decision rules
- Step-by-step instructions

**Key phrases:**
- "GPS points were collected using [specific device and settings]"
- "The tool was configured with..."
- "Parameters were set to..."
- "Each sample was processed by..."
- Specific software versions, coordinates, measurements

**Test:** "Could someone replicate from this level of detail?"

## The Replication Test

**Most reliable test for tier assignment:**

- **Cannot replicate from this** → Research Design (strategic framing)
- **Could replicate generally but not precisely** → Method (high-level approach)
- **Could replicate precisely** → Protocol (operational detail)

## Common Boundary Cases

### Case 1: "We conducted a survey"

**Too vague - need more context:**
- If discussing WHY survey was chosen → Design
- If describing WHAT kind of survey → Method  
- If specifying HOW survey was executed → Protocol

**Example breakdown:**
- Design: "We chose survey methodology to cover large spatial area efficiently"
- Method: "Pedestrian archaeological survey with systematic transects"
- Protocol: "20m-spaced transects, 5m visibility on each side, GPS point at each artifact"

### Case 2: Sampling statements

- **Design level:** "We used purposive sampling because..."
- **Method level:** "Purposive sampling targeting diverse site types"
- **Protocol level:** "Sites selected based on: (1) ceramic presence >10 sherds/m², (2) distance from water <500m, (3) elevation 300-600m"

### Case 3: Analysis descriptions

- **Design level:** "Comparative analysis framework to test hypothesis"
- **Method level:** "Statistical comparison using regression models"
- **Protocol level:** "Multiple linear regression in R v4.1, model specification: lm(y ~ x1 + x2 + x3), alpha=0.05"

## Hierarchical Relationships

**Designs enable Methods:**
```
Design: "Comparative study of platform effectiveness"
  ↓ enables
Method: "Mobile data collection"
Method: "Traditional paper recording"
```

**Methods are realized through Protocols:**
```
Method: "GPS-based spatial documentation"
  ↓ realized through
Protocol: "Garmin GPSMAP 64s, WGS84, ±3-5m accuracy"
Protocol: "Point collection at each feature center"
```

## When Uncertain

**If unsure about tier assignment in Pass 1:**
1. Mark as uncertain in extraction_notes
2. Include at multiple tiers if necessary
3. Let Pass 2 rationalize the placement

**Pass 1 philosophy:** Over-extraction is acceptable. Pass 2 will refine.

**Pass 2 verification:** Apply all three tests above and finalize placement.

## Quick Reference Table

| Level | Focus | Granularity | Replication |
|-------|-------|-------------|-------------|
| Design | WHY framed this way | Strategic choices | Cannot replicate strategy |
| Method | WHAT was done | General approach | Could replicate generally |
| Protocol | HOW implemented | Specific details | Could replicate precisely |

| Level | Typical Length | Specificity |
|-------|---------------|-------------|
| Design | 1-3 sentences | High-level rationale |
| Method | 2-5 sentences | Approach description |
| Protocol | 3-10+ sentences | Detailed specifications |

## Remember

- **When in doubt, favor finer granularity in Pass 1**
- **The hierarchy should feel natural:** Designs → Methods → Protocols flows logically
- **Cross-references should make sense:** If Protocol P implements Method M, and M implements Design D, the chain should be coherent
- **Not all papers will have all three levels explicitly:** Some may have methods without explicit design discussion, or methods without protocol-level detail. That's okay - extract what's present.
