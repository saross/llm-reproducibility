# Reproduction-Assessor Skill v1.0 Review Report

**Date:** 2026-02-10
**Scope:** Systematic review of the reproduction-assessor skill (v1.0) based on the complete
5-paper pilot in the Open Science Compliance Study
**Output:** Findings report with prioritised recommendations for v1.1

---

## 1. Executive Summary

The reproduction-assessor skill (v1.0) was tested across all 5 pilot papers in the Open
Science Compliance Study. Results: 4 SUCCESSFUL, 1 PARTIAL (Key et al. 2024 — data
availability bottleneck).

| Paper | Type | Verdict | Match Rate | Key Challenge |
|-------|------|---------|------------|---------------|
| Crema et al. 2024 | B | SUCCESSFUL | All within HPD | MCMC runtime (~18h) |
| Marwick 2025 | A | SUCCESSFUL | 1 minor discrepancy | None |
| Herskind & Riede 2024 | C | SUCCESSFUL | 291/291 exact | Wrapper script needed |
| Dye et al. 2023 | C+D | SUCCESSFUL | 54/54 exact | Proprietary upstream (OxCal) |
| Key et al. 2024 | C | PARTIAL | 98.3% (116/118) | 10/13 datasets unavailable |

**Key findings:**

1. **The system works well for straightforward reproductions.** The 4-session workflow,
   type classification, Dockerfile strategy, and verification framework all performed as
   designed across Types A, B, C, and D.

2. **Gaps emerge with partial data, paper errors, and complex scope limitations.** Key
   et al. 2024 — the most challenging paper — exposed 3 critical, 5 important, and 5
   minor issues not visible in the first 4 reproductions.

3. **2 of 5 reproductions have no persisted artefacts.** Crema et al. 2024 and Marwick
   2025 are referenced in queue.yaml with report paths, but their output directories do
   not exist in the repository. This is itself a finding about artefact persistence gaps.

4. **Only 1 of 5 papers has a complete 4-session workflow.** Key et al. 2024 is the only
   paper with an adversarial review (R-C session). Herskind and Dye completed R-A and
   R-B but predate the R-C formalisation. Crema and Marwick have no artefacts at all.

5. **12 distinct improvement opportunities** identified across 3 severity tiers (3
   critical, 5 important, 4 minor), all addressable in v1.1 without architectural
   changes.

---

## 2. What Worked Well

### 2.1 Workflow Structure

The 4-session design (R-Plan → R-A → R-B → R-C) worked for all paper types. Session
boundaries were in the right places:

- **R-Plan** produced appropriately scoped plans across all 5 papers
- **R-A** successfully resolved environment and script adaptation for all papers
- **R-B** completed execution and verification without session-boundary issues
- **R-C** (where used) caught a real error and validated verdict calibration

Within-session autonomy worked as designed — no premature stops or unnecessary user
queries during sessions. Handoff format carried sufficient information for session
resumption.

### 2.2 Type Classification

The A/B/C/D framework correctly predicted complexity and effort for all 5 papers:

- **Type A** (Marwick): ~20 min total hands-on — accurately predicted as lowest effort
- **Type B** (Crema): Dockerfile fixes + compute wait — correctly anticipated
- **Type C** (Herskind, Key): Wrapper scripts required — predicted by classification
- **Type C+D** (Dye): Multi-type classification handled elegantly, scoping proprietary
  upstream (OxCal) while fully verifying open components (ArchaeoPhases)

### 2.3 Dockerfile Strategy

Iterative build approach (1-3 iterations) matched reality across all papers:

- **Marwick**: 0 iterations (pristine author Dockerfile)
- **Crema**: 1 iteration (typo fix + missing package)
- **Herskind**: 1 iteration (constructed, straightforward deps)
- **Key**: 1 iteration (constructed, minimal deps — base R only)
- **Dye**: 3 iterations (transitive deps: igraph → libglpk, proj4 → libproj + libgdal)

Rocker hierarchy guidance was appropriate: papers correctly matched to `rocker/r-ver`
(Key, Herskind) or higher tiers as needed.

### 2.4 Script Adaptation

"No algorithmic modifications" rule was clear and enforceable across all wrapper scripts.
Key achievement: the rule was never ambiguous in practice — wrapper modifications were
obviously infrastructure (output capture, parameterisation) rather than analysis.

- **Herskind**: Parameterised function pattern (n-gram sizes 2, 3, 4)
- **Dye**: Incremental code block assembly (38 supplement sections)
- **Key**: Parameterised loop pattern (5 variables × dataset, 4 types × 4 variables)

Output capture patterns (`write.csv`, `sink`, `pdf`) were sufficient for all papers.

### 2.5 Verification Strategy

The deterministic/stochastic distinction worked perfectly:

- **Deterministic = exact match**: Herskind 291/291, Dye 54/54, Key 116/118 comparable
- **Stochastic = HPD checking**: Crema all within 90% HPD intervals
- **Regression/GAM**: Marwick p-value difference (4.08e-7 vs 2.67e-6) correctly
  classified as MINOR_DISCREPANCY (both highly significant)

### 2.6 Adversarial Review

When used (Key et al. only), the 5-dimension framework demonstrated clear value:

- **Caught a transcription error** in the wrapper script's hardcoded comparison section
  (27.5% Extension value attributed to wrong dataset row)
- **Validated PARTIAL verdict** through systematic challenge testing across all 5
  dimensions
- **All 5 dimensions passed**, confirming the reproduction's integrity

### 2.7 Templates and Artefact Structure

Templates produced consistent artefact structure across the 3 papers with directories
(Key, Herskind, Dye). The standard artefact set (Dockerfile, run-analysis.R,
environment.md, log.md, comparison-report.md) was sufficient for all reproduction types.

---

## 3. Gaps and Issues

### Critical

#### C1. Missing Artefact Persistence (2 of 5 Papers)

**Description:** Crema et al. 2024 and Marwick 2025 reproductions are referenced in
queue.yaml (dated 2026-02-09) with specific output paths including
`comparison-report.md`, but their `outputs/{slug}/reproduction/` directories do not exist
in the repository.

**Impact:** 40% of pilot reproductions have no verifiable artefacts. The queue.yaml
references to nonexistent files undermine the reproducibility of the reproduction process
itself.

**Root cause:** The skill specifies that artefacts should be saved to
`outputs/{slug}/reproduction/attempt-{NN}/` but does not enforce this or include a
checklist to verify artefact persistence before session completion.

**Files affected:** SKILL.md (artefact specifications), prompts 01-02 (output steps),
queue.yaml (references nonexistent files)

**Motivated by:** File system audit during this review

#### C2. CANNOT_COMPARE Not a Formal Discrepancy Category

**Description:** Key et al. 2024 produced 8 NaN values from undocumented duplicate
handling in the Paleoindian dataset. These values could not be compared because the
reproduction's input data contained duplicates that the original analysis apparently
removed through an undocumented preprocessing step.

**Impact:** The current 5-category classification system (EXACT_MATCH through
MAJOR_DISCREPANCY) has no category for "value could not be computed due to upstream
data/preprocessing issues." NaN ≠ MAJOR_DISCREPANCY because the algorithm is not wrong
— the input data has an undocumented preprocessing step.

**Files affected:** SKILL.md §E, verification-strategies.md (discrepancy classification
reference), comparison-report-template.md

**Motivated by:** Key et al. R-B session (8 NaN values classified ad hoc as
`cannot_compare` in queue.yaml)

#### C3. Data Availability Assessment Inadequate

**Description:** The reproduction plan guide mentions data availability briefly
(Part 1.2, 7 rows in a table) but Key et al. 2024 showed this is THE primary bottleneck
for papers with aggregated datasets. Key had 13 datasets across 13 sources, of which only
3 were accessible (42.6% by record weight).

**Impact:** Without a formal data provenance protocol, the planning session cannot
adequately assess whether a reproduction is feasible before committing to execution. The
5-level access taxonomy (Level 0-4) developed ad hoc for Key et al. should be
standardised.

**Data access levels developed for Key et al.:**

| Level | Description | Example |
|-------|-------------|---------|
| 0 | Fully accessible — can download immediately | Zenodo deposit, GitHub, supplement |
| 1 | Accessible with effort — registration, request, or paywall | Institutional repo |
| 2 | Partially accessible — subset or summary available | Published summary stats |
| 3 | Inaccessible — held by co-authors, in monographs | "Available on request" |
| 4 | Never published — unpublished or lost | Replica collections, pilot data |

**Files affected:** reproduction-plan-guide.md (Part 1.2), prompt 00 (Phase 2),
environment-template.md (data sources section)

**Motivated by:** Key et al. R-Plan (42.6% data accessibility, 10/13 datasets at
Level 3-4)

### Important

#### I1. Paper Calculation Errors Not Distinguished from Reproduction Failures

**Description:** Key et al. 2024 found 2 Extension% values wrong in the published paper
itself — not algorithmic failures in the reproduction. The paper reports Midland Thickness
Extension as 3.1% and Clovis Mass Extension as 19.6%, but applying the Extension% formula
to the paper's own tabulated min/max values yields ~20% and ~3.1% respectively (the
values appear swapped or miscalculated).

**Impact:** The skill's verdict system does not distinguish "our reproduction disagrees
because the paper is wrong" from "our reproduction disagrees because we made an error."
Both show up as MAJOR_DISCREPANCY, but they have fundamentally different implications: the
former strengthens confidence in the reproduction, while the latter undermines it.

**Recommendation:** Add guidance on handling paper errors: verify independently (apply the
formula to the paper's own tabulated values), classify separately (PAPER_ERROR vs
MAJOR_DISCREPANCY), and document the verification in the comparison report.

**Files affected:** verification-strategies.md, comparison-report-template.md, SKILL.md §E

**Motivated by:** Key et al. R-B (2 Extension% calculation errors independently verified)

#### I2. Adversarial Reviews Inconsistent — Only 1 of 5 Papers Has One

**Description:** Key et al. 2024 is the only paper with an adversarial review (R-C
session). Herskind and Dye completed R-A and R-B but not R-C. Crema and Marwick have no
artefacts at all.

**Impact:** The skill specifies R-C as the 4th mandatory session, but the first 4
reproductions predate the full framework formalisation. This creates inconsistency in the
pilot corpus.

**Resolution path:** This is not a skill design issue per se — it reflects the
chronological development of the framework (the adversarial review was formalised after
the first 4 reproductions). The pilot summary should document this explicitly rather
than requiring backfilling.

**Files affected:** pilot-reproduction-summary.md (note about pre-v1.0 reproductions),
queue.yaml notes

**Motivated by:** Cross-paper artefact audit

#### I3. Pilot Reproduction Summary Outdated

**Description:** The pilot-reproduction-summary.md covers only 4 papers (Crema, Marwick,
Herskind, Dye) and is titled "Condensed patterns from 4 completed reproductions." Key
et al. 2024 (Type C, PARTIAL, data availability bottleneck) is not included.

**Impact:** The summary is the primary reference document for future reproductions.
Missing Key et al. means several important patterns are not captured:

- Parameterised analysis loops for multi-dataset papers
- Data provenance chains for aggregated-dataset papers
- Paper error detection during verification
- Publishing errors (empty supplement files)
- PARTIAL verdict calibration

**Files affected:** pilot-reproduction-summary.md

**Motivated by:** Key et al. completion

#### I4. Scope Limitation Categories Not Distinguished

**Description:** The current system treats all scope limitations identically under a
single "Scope Limitation(s)" section. At least 4 distinct categories emerged from the
pilots:

1. **Proprietary upstream software** — Dye → OxCal (cannot reproduce, use intermediates)
2. **Data unavailability** — Key → 10/13 datasets (cannot reproduce affected analyses)
3. **Stochastic non-reproducibility by design** — Key → no `set.seed()` in stochastic
   scripts (results will vary between runs)
4. **Publishing errors** — Key → `mmc4.csv` is empty (header only, 75 bytes)

**Impact:** Each category has different implications for the verdict and for
documentation. Proprietary upstream is not a FAIR failure; data unavailability IS a FAIR
failure; stochastic non-reproducibility is expected behaviour; publishing errors are
journal process failures.

**Files affected:** verification-strategies.md (scope limitations section), SKILL.md §E
(verdict categories)

**Motivated by:** Key et al. (3 of 4 categories in a single paper)

#### I5. No Formal R-Plan Output Artefact

**Description:** The planning session produces notes in the handoff summary but no
archived document. Key et al. created `session-handoff.md` and
`data-availability-inventory.md` ad hoc, but these are not prescribed by the skill.

**Impact:** Planning decisions are not preserved in the artefact set, making it difficult
to review why certain scope decisions were made or what risks were anticipated. The
adversarial review (R-C) cannot assess planning quality without access to the plan.

**Recommendation:** Prescribe `reproduction-plan.md` as a formal R-Plan artefact,
consolidating the plan document and any data availability inventory.

**Files affected:** SKILL.md (artefact specifications), prompt 00 (output section)

**Motivated by:** Key et al. R-Plan (extensive planning produced valuable artefacts worth
preserving)

### Minor

#### M1. Template Duplication

**Description:** Templates exist in two locations:

- `.claude/skills/reproduction-assessor/references/templates/` (canonical)
- `reproduction-system/templates/` (copies with README noting they are copies)

**Impact:** Risk of divergence if one location is updated without the other. The
`reproduction-system/templates/README.md` correctly identifies the skill package as
canonical, but the duplication adds maintenance overhead.

**Recommendation:** Replace `reproduction-system/templates/` files with symlinks or
remove them entirely, keeping only the README with cross-references. Alternatively,
keep the copies but add a verification step to detect divergence.

**Files affected:** Both template directories, cross-references in prompts

#### M2. Wrapper Patterns Missing Key-Style Parameterised Loop

**Description:** Key et al.'s wrapper script used a load → subset → analyse → extract
pattern repeated for 5 Olduvai variables and then 4 Paleoindian types × 4 variables.
This nested parameterised loop is a common pattern for papers with multi-dataset,
multi-variable analyses but is not documented in wrapper-script-patterns.md.

**Files affected:** wrapper-script-patterns.md (new pattern section)

**Motivated by:** Key et al. R-A wrapper script (314 lines)

#### M3. Interactive Placeholder Substitution Undocumented

**Description:** Key et al.'s supplementary R scripts used `###file location###` as a
placeholder for file paths that users must replace manually. This is a common pattern in
journal supplements — worth documenting as a pitfall.

**Files affected:** wrapper-script-patterns.md (pitfalls section)

**Motivated by:** Key et al. supplement R scripts (all 3 mmc files)

#### M4. Figure Comparison Guidance Thin

**Description:** The verification-strategies.md figure verification section provides
correct principles (layout, patterns, relative positions) but limited procedural guidance.
All 3 reproduced papers with artefacts mention figures but provide limited detail on how
figure comparison was conducted.

**Recommendation:** Add a structured checklist for figure comparison, distinguish between
computationally generated figures (verify underlying data) and presentation figures
(visual comparison only), and provide guidance on documenting figure comparison results.

**Files affected:** verification-strategies.md (figure verification section),
comparison-report-template.md

#### M5. Dockerfile Gotchas Section Incomplete

**Description:** Several gotchas discovered during Key et al. are not documented:

- **Empty supplement files** (mmc4.csv: header only, 75 bytes — publishing error)
- **Column naming mismatches** between data files and script expectations
- **Data server unreliability** (personal servers going offline)
- **Unit conversion requirements** (implicit conversions not documented in code)

Some of these are data/script gotchas rather than Docker-specific, but they are
encountered during the Docker preparation phase and should be documented.

**Files affected:** dockerfile-patterns.md (gotchas section), wrapper-script-patterns.md
(pitfalls section)

---

## 4. Recommendations for v1.1

| # | Change | Severity | Files | Effort |
|---|--------|----------|-------|--------|
| R1 | Add CANNOT_COMPARE as 6th discrepancy category | Critical | SKILL.md, verification-strategies.md, comparison-report-template.md | Small |
| R2 | Add data provenance protocol (5-level access taxonomy) | Critical | reproduction-plan-guide.md, prompt 00, environment-template.md | Medium |
| R3 | Add artefact persistence checklist to R-A and R-B handoffs | Critical | prompts 01-02, SKILL.md | Small |
| R4 | Add paper error handling guidance | Important | verification-strategies.md, comparison-report-template.md, SKILL.md §E | Small |
| R5 | Update pilot-reproduction-summary.md with Key et al. | Important | pilot-reproduction-summary.md | Small |
| R6 | Add scope limitation taxonomy (4 categories) | Important | verification-strategies.md, SKILL.md §E | Small |
| R7 | Prescribe reproduction-plan.md as formal R-Plan artefact | Important | SKILL.md, prompt 00 | Small |
| R8 | Consolidate templates to single canonical location | Minor | Template directories, cross-references | Small |
| R9 | Add parameterised loop pattern to wrapper-script-patterns.md | Minor | wrapper-script-patterns.md | Small |
| R10 | Add interactive placeholder pattern | Minor | wrapper-script-patterns.md | Small |
| R11 | Strengthen figure comparison guidance | Minor | verification-strategies.md, comparison-report-template.md | Small |
| R12 | Expand gotchas catalogue | Minor | dockerfile-patterns.md, wrapper-script-patterns.md | Small |

### Implementation Order

1. **R1 + R4 + R6** (discrepancy classification expansion) — all touch the same sections
2. **R2** (data provenance protocol) — new content in plan guide and prompt 00
3. **R3** (artefact persistence checklist) — touches prompts 01-02 and SKILL.md
4. **R5** (pilot summary update) — standalone
5. **R7** (R-Plan artefact) — touches SKILL.md and prompt 00
6. **R8** (template consolidation) — touches both template directories
7. **R9 + R10 + R12** (pattern additions) — all add content to reference docs
8. **R11** (figure comparison) — touches verification-strategies.md and template

---

## 5. Pilot Reproduction Summary Update (Draft)

The current summary covers 4 papers. Key et al. 2024 should be added:

### New Entry for Overview Table

| Paper | Type | Dockerfile | Runtime | Discrepancies | Verdict |
|-------|------|------------|---------|---------------|---------|
| Key et al. 2024 | C (interactive, aggregated data) | Constructed (1 iteration) | ~5s | 2 (paper errors) + 8 NaN | PARTIAL |

### New Patterns to Document

1. **Data availability as primary bottleneck** — When papers aggregate datasets from
   multiple sources, data accessibility becomes the dominant constraint. Key had 13
   datasets across 13 sources; only 3 accessible (42.6% by record weight).

2. **Paper calculation errors** — Reproductions can reveal errors in the published paper
   itself. Key's Extension% values for Midland Thickness and Clovis Mass are internally
   inconsistent (verifiable from the paper's own tabulated values).

3. **Publishing errors** — Supplement files may be empty or corrupted. Key's mmc4.csv
   contained only a header row (75 bytes) — a publishing error, not a data availability
   issue.

4. **PARTIAL verdict calibration** — 98.3% match rate with discrepancies traceable to
   paper errors (not reproduction errors) still warrants PARTIAL when 77% of datasets are
   inaccessible.

5. **Parameterised analysis loops** — Multi-dataset, multi-variable papers require nested
   loop patterns in wrapper scripts. Key's 314-line wrapper iterated over 5 variables for
   Olduvai and 4 types × 4 variables for Paleoindian.

### Updated Statistics

- Papers attempted: 5 (was 4)
- Papers successful: 4 (was 4)
- Papers partial: 1 (new)
- Success rate: 80% (was 100%)
- Mean hands-on time: ~1.8 hours (was ~1.5 hours)

### Notes on Pre-v1.0 Reproductions

Crema et al. 2024 and Marwick 2025 were reproduced on 2026-02-09, before the
reproduction-assessor skill v1.0 was formalised. Their queue.yaml entries record verdicts
and metadata but no artefact directories exist in the repository. These reproductions
predate the adversarial review (R-C) session requirement.

Herskind & Riede 2024 and Dye et al. 2023 were reproduced on 2026-02-10 during v1.0
development. They have complete R-A and R-B artefacts but predate the R-C formalisation.

Key et al. 2024 is the only paper with the complete 4-session workflow including the
adversarial review.

---

## 6. Appendix: Gotcha Catalogue

Comprehensive catalogue of gotchas encountered across all 5 pilot reproductions,
indicating whether each is currently documented in the skill reference materials.

### Documented Gotchas (in v1.0)

| Gotcha | Paper(s) | Reference Location |
|--------|----------|--------------------|
| Interactive scripts requiring wrapper | Herskind, Dye, Key | wrapper-script-patterns.md |
| System dependencies for R packages | Dye, Crema | dockerfile-patterns.md |
| `.here` sentinel file for volume mounts | Dye | dockerfile-patterns.md |
| `rnaturalearthhires` not on CRAN | Crema | dockerfile-patterns.md |
| Ampersands in filenames | Herskind | dockerfile-patterns.md |
| R version mismatch with renv.lock | Crema | dockerfile-patterns.md |
| MRAN retirement | — | dockerfile-patterns.md |
| Supplement access (ScienceDirect HTTP 403) | Dye | pilot-reproduction-summary.md |
| Font dependencies in Docker | Herskind | wrapper-script-patterns.md |
| Column index shifts from data processing | Dye | wrapper-script-patterns.md |
| `print()` vs `ggsave()` in batch mode | Herskind | wrapper-script-patterns.md |

### Undocumented Gotchas (new in Key et al.)

| Gotcha | Paper | Recommended Location |
|--------|-------|----------------------|
| Empty supplement files (publishing errors) | Key | wrapper-script-patterns.md |
| Interactive placeholder patterns (`###file location###`) | Key | wrapper-script-patterns.md |
| Undocumented data preprocessing (duplicate removal) | Key | verification-strategies.md |
| Data aggregated from 13+ dispersed sources | Key | reproduction-plan-guide.md |
| No `set.seed()` in stochastic scripts | Key | verification-strategies.md |
| Paper calculation errors detectable from internal consistency | Key | verification-strategies.md |
| Parameterised loop pattern for multi-dataset analyses | Key | wrapper-script-patterns.md |
| Data on personal websites (persistence risk) | Key, Dye | reproduction-plan-guide.md |
| Supplement file naming inconsistency (mmc1/mmc2/mmc3/mmc4) | Key | wrapper-script-patterns.md |

### Gotchas by Frequency

| Category | Count | Papers |
|----------|-------|--------|
| Script adaptation | 6 | All except Marwick |
| Docker/environment | 5 | Crema, Dye, Herskind |
| Data access/quality | 5 | Key, Dye |
| Verification | 3 | Key |
| Publishing/supplement | 3 | Key, Dye |

---

*This review was conducted on 2026-02-10 as part of the reproduction-assessor skill v1.0
→ v1.1 upgrade cycle.*
