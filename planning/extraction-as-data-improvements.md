# Extraction-as-Data: Improvement Options with Risk Assessment

**Created:** 2025-12-06
**Source:** Variability analysis (25 runs) + active-todo-list.md observations (Sections 8a, 8b)
**Purpose:** Risk-assessed improvements for extraction-as-data use case

---

## Context

The variability test (5 papers × 5 runs) revealed that while **assessment outcomes are stable** (96% verdict stability, 3-6 point aggregate range), **extraction counts vary significantly** (CV 0-138% depending on array type).

For the primary use case (credibility assessment), this variability is acceptable — assessments track core concepts, not peripheral details.

For **extraction-as-data** use cases (meta-analysis, training data, corpus statistics), count variability may be problematic. This document outlines possible improvements, assessed for regression risk.

---

## Summary Table

| Array | CV% Range | Improvement | Risk Level | Recommendation |
|-------|-----------|-------------|------------|----------------|
| **Protocols** | 25-138% | Explicit/implicit standardisation | 🟢 LOW | **Implement first** |
| **Claims** | 3-28% | Consolidation guidance | 🟡 MEDIUM | Consider after protocols |
| **Evidence** | 7-31% | Granularity guidance | 🟡 MEDIUM | Consider after protocols |
| **Methods** | 12-35% | Scope boundary guidance | 🟡 MEDIUM | Lower priority |
| **Implicit Arguments** | 0-18% | None needed | — | No action |
| **Research Designs** | 0-45%* | None needed | — | No action |

*One outlier paper (sobotkova-et-al-2016); otherwise 0-15%

---

## Improvement 1: Protocols — Explicit vs Implicit Standardisation

### Current Issue

From active-todo-list.md Section 8b:

> "Some runs extract only explicitly described protocols — procedures stated directly in the paper text. Other runs infer protocols from methods descriptions — procedures implied by methodology but not spelled out."

### Variability Data

| Paper | Protocol Counts | CV% |
|-------|-----------------|-----|
| sobotkova-et-al-2024 | 7, 12, 12, 14, 15 | 25% |
| penske-et-al-2023 | 20, 24, 24, 29, 39 | 26% |
| ballsun-stanton-2018 | 3, 6, 6, 9, 9 | 36% |
| ross-2005 | 0, 0, 0, 2, 2 | 138% |
| sobotkova-et-al-2016 | 5, 5, 10, 14, 14 | 46% |

**This is the worst-performing array across all papers.**

### Proposed Intervention

Add definition and boundary examples to Pass 3 (`03-rdmap_pass1a_prompt.md`) and Pass 5 (`05-rdmap_pass2_prompt.md`):

```markdown
## Protocol Definition

A protocol is a specific, documented procedure with explicit steps that
could be followed by another researcher to reproduce a step. Include only:

- Named procedures with explicit steps (e.g., "sieving through 4mm mesh")
- Documented workflows with specific parameters (e.g., "70:20:10 train/val/test split")
- Standard operating procedures referenced by name (e.g., "following protocols.io dx.doi.org/...")

Do NOT include:

- General method descriptions without procedural detail
- Inferred procedures from results (e.g., "they must have used X because...")
- One-sentence mentions without parameters (e.g., "samples were processed")
- Implicit methodological choices that could be documented but aren't
```

### Risk Assessment

**Risk Level:** 🟢 **LOW**

| Factor | Assessment |
|--------|------------|
| **Additive vs breaking** | Additive — clarifies scope, doesn't change extraction logic |
| **Targets root cause** | Yes — to-do 8b already diagnosed explicit/implicit confusion |
| **Spillover to other arrays** | Unlikely — protocols are distinct from claims/evidence |
| **Testability** | High — can measure CV before/after on same papers |

### Expected Impact

Reduce protocol CV from 25-138% to <30%

### Action Items

- [ ] Add protocol definition section to `extraction-system/prompts/03-rdmap_pass1a_prompt.md`
- [ ] Add consolidation guidance to `extraction-system/prompts/05-rdmap_pass2_prompt.md`
- [ ] Add worked examples distinguishing explicit from implicit protocols
- [ ] Test on 2 papers from variability corpus to verify reduced variability
- [ ] If successful, update `.claude/skills/research-assessor/references/` with protocol guidance

---

## Improvement 2: Claims — Consolidation Granularity Guidance

### Current Issue

Same argumentative content extracted as 1 consolidated claim OR 3 granular sub-claims depending on run. This creates count variability without conceptual difference.

### Variability Data

| Paper | Claims Counts | CV% |
|-------|---------------|-----|
| sobotkova-et-al-2024 | 27, 40, 45, 47, 62 | 28% |
| penske-et-al-2023 | 60, 63, 63, 64, 65 | 3% |
| ballsun-stanton-2018 | 42, 58, 59, 59, 61 | 14% |
| ross-2005 | 23, 26, 29, 30, 31 | 12% |
| sobotkova-et-al-2016 | 22, 49, 50, 50, 50 | 28% |

Most papers show moderate variability (12-28%), with penske-et-al-2023 notably stable (3%).

### Proposed Intervention

Add consolidation heuristics to Pass 2 (`02-claims-evidence_pass2_prompt.md`):

```markdown
## Claim Consolidation Rules

When reviewing claims from Pass 1, apply these consolidation heuristics:

1. **Shared evidence test:** If multiple claims share identical supporting evidence
   AND make the same argumentative point → consolidate into single claim

2. **Argumentative unity test:** If claims are components of a single argumentative
   move (premise + conclusion) → consolidate, preserving logical structure

3. **Independence test:** If claims could stand alone as separate contributions
   to the field → keep separate even if related

4. **Granularity anchor:** A claim should represent ONE assertable proposition.
   "X AND Y" is two claims unless X and Y are inseparable (e.g., "correlation
   between X and Y").
```

### Risk Assessment

**Risk Level:** 🟡 **MEDIUM**

| Factor | Assessment |
|--------|------------|
| **Additive vs breaking** | Potentially breaking — could shift extraction philosophy |
| **Targets root cause** | Partially — granularity is inherently subjective |
| **Spillover to other arrays** | Low — claims are processed separately |
| **Testability** | Medium — consolidation effects harder to measure |
| **Unintended consequences** | May reduce valid granular claims users want |

### Mitigation

- Frame as "guidance" not "rules"
- Test on 2 papers before full adoption
- Compare consolidated output against original to ensure no information loss

### Expected Impact

Reduce claims CV from 3-28% to <15% (uncertain)

### Action Items

- [ ] Draft consolidation guidance for Pass 2 prompt
- [ ] Test on sobotkova-et-al-2024 (highest CV) and penske-et-al-2023 (lowest CV)
- [ ] Compare claim content (not just counts) before/after
- [ ] Only adopt if content quality maintained

---

## Improvement 3: Evidence — Granularity Guidance

### Current Issue

Same data point extracted as 1 evidence item OR split into multiple items depending on run (e.g., "773 mounds from 85 sq km" vs "773 mounds" + "85 sq km survey area").

### Variability Data

| Paper | Evidence Counts | CV% |
|-------|-----------------|-----|
| sobotkova-et-al-2024 | 23, 25, 45, 45, 45 | 31% |
| penske-et-al-2023 | 56, 64, 67, 67, 67 | 7% |
| ballsun-stanton-2018 | 26, 43, 43, 43, 47 | 20% |
| ross-2005 | 16, 17, 21, 21, 21 | 13% |
| sobotkova-et-al-2016 | 28, 34, 35, 35, 35 | 9% |

Paper 1 (sobotkova-et-al-2024) shows highest variability (31%); others are moderate.

### Proposed Intervention

Add granularity anchor examples to Pass 1 (`01-claims-evidence_pass1_prompt.md`):

```markdown
## Evidence Granularity

Each evidence item should represent ONE observation, measurement, or finding.

**Split when:**
- Different data types (e.g., "sample size" vs "geographic extent")
- Different sources (e.g., "survey data" vs "excavation data")
- Different time points (e.g., "2021 run" vs "2022 run")

**Keep together when:**
- Same observation with multiple attributes (e.g., "773 mounds across 85 sq km"
  is ONE observation about survey coverage)
- Composite metrics (e.g., "F1 score of 0.87" includes precision and recall)
```

### Risk Assessment

**Risk Level:** 🟡 **MEDIUM**

| Factor | Assessment |
|--------|------------|
| **Additive vs breaking** | Additive but prescriptive |
| **Targets root cause** | Partially — granularity is inherently subjective |
| **Spillover to other arrays** | Low |
| **Testability** | Medium — effects may be subtle |
| **Unintended consequences** | Over-specific rules may reduce useful variability |

### Expected Impact

Reduce evidence CV from 7-31% to <20% (uncertain)

### Action Items

- [ ] Draft granularity guidance for Pass 1 prompt
- [ ] Test on sobotkova-et-al-2024 (highest CV)
- [ ] Assess whether guidance actually reduces variability or just shifts it
- [ ] Consider whether this intervention is necessary given moderate baseline CV

---

## Improvement 4: Methods — Scope Boundary Guidance

### Current Issue

Unclear boundary between method and protocol; some runs classify same item differently.

### Variability Data

| Paper | Methods Counts | CV% |
|-------|----------------|-----|
| sobotkova-et-al-2024 | 7, 7, 9, 9, 9 | 13% |
| penske-et-al-2023 | 15, 15, 16, 19, 19 | 12% |
| ballsun-stanton-2018 | 4, 4, 8, 8, 8 | 34% |
| ross-2005 | 2, 3, 3, 3, 3 | 16% |
| sobotkova-et-al-2016 | 4, 5, 5, 8, 9 | 35% |

### Proposed Intervention

Add method vs protocol decision tree to RDMAP prompts.

### Risk Assessment

**Risk Level:** 🟡 **MEDIUM**

| Factor | Assessment |
|--------|------------|
| **Coordination required** | Must align with protocol changes |
| **May shift without reducing** | Could move items between arrays |
| **Priority** | Lower — methods variability less problematic |

### Recommendation

**Defer until protocol intervention is tested.** If protocol changes resolve method/protocol boundary confusion, this may not be needed.

---

## What NOT to Change

### 1. Implicit Arguments Extraction

**CV Range:** 0-18% (4/5 papers at 0%)

This is the most stable array. The extraction is inherently at a consistent level of abstraction because implicit arguments represent conceptual gaps, not extractable text spans.

**Recommendation:** No intervention needed.

### 2. Research Designs Extraction

**CV Range:** 0-45% (but mostly 0-15%)

One outlier (sobotkova-et-al-2016 at 45%) doesn't warrant system-wide change. Most papers show stable research design extraction.

**Recommendation:** No intervention needed.

### 3. Liberal Extraction Philosophy

The "capture first, consolidate later" approach is sound. It produces variable counts but consistent *concepts*. The variability test confirmed that assessment outcomes are stable despite count variability.

**Recommendation:** Preserve liberal extraction philosophy.

### 4. Pass Structure

The 8-pass workflow produces stable assessments. Changing pass structure risks regression in assessment quality.

**Recommendation:** No structural changes.

---

## Implementation Priority

| Priority | Intervention | Risk | Effort | When |
|----------|--------------|------|--------|------|
| **1** | Protocol explicit/implicit standardisation | 🟢 LOW | 2-3 hrs | Implement now |
| **2** | Claims consolidation guidance | 🟡 MEDIUM | 2-3 hrs | After protocol test |
| **3** | Evidence granularity guidance | 🟡 MEDIUM | 1-2 hrs | Optional |
| **4** | Methods scope boundary | 🟡 MEDIUM | 2-3 hrs | Defer |

---

## Testing Protocol

For any intervention:

1. **Baseline:** Use existing variability corpus data (25 runs already complete)
2. **Test:** Run 2-3 extractions on same papers with modified prompts
3. **Compare:** Calculate CV% for modified runs
4. **Validate:** Check that content quality is maintained (not just count consistency)
5. **Adopt:** Only if CV reduced AND content quality preserved

---

## Success Criteria

| Metric | Current | Target |
|--------|---------|--------|
| Protocol CV | 25-138% | <30% |
| Claims CV | 3-28% | <20% |
| Evidence CV | 7-31% | <25% |
| Assessment stability | 96% | ≥96% (no regression) |

---

## Related Documentation

- `outputs/variability-test/variability-analysis-report.md` — Full variability analysis
- `planning/active-todo-list.md` Section 8a — Variability test findings
- `planning/active-todo-list.md` Section 8b — Protocol standardisation proposal
- `input/variability-queue.yaml` — Complete run data

---

*Document created from variability analysis session, 2025-12-06*
