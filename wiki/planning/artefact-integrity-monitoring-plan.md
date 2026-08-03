---
title: "Artefact-Integrity Monitoring — Plan v0.1"
tags: [infrastructure, reproducibility, governance]
created: 2026-08-02
updated: 2026-08-03
status: active — phase-gated
---

# Artefact-Integrity Monitoring — Plan v0.1

**Status: ACTIVE, phase-gated. §9 questions resolved and Phase 0 complete
(2026-08-03, output in §10); Phase 1 awaits the Phase 0 gate review.**
Written 2026-08-02 on Shawn's decision to
widen the D5 gate so that *every registered entity is checked hard*, with a
reorganisation acceptable if one is needed. Inspiration taken from the
map-reader-llm verification charter (`~/Code/map-reader-llm/planning/audit-charter.md`,
revised 2026-07-29) — which already names this repository as a future target
for the same apparatus — but the two problems differ in shape, and §7 below
says where the analogy stops.

**This document is self-sufficient by design** (charter lesson): a later
session should be able to resume from this file plus the manifest alone,
without conversational memory.

---

## 1. The problem, measured

Three findings from 2026-07-27 and 2026-08-02, all re-verified at source:

**(a) The version check covers 7 of 25 registered entries.**
`scripts/check-manifest-consistency.py:467-468` iterates `shared_content` only,
so `check_canonical_entry` — the function comparing a manifest version against
the file's `**Version:**` line — never runs on the extraction prompts, the
assessment prompts, the reproduction prompts, the workflow, or the schemas.
Demonstrated by probe: a deliberately wrong `9.9` for the reproduction
preparation prompt still produced `PASS`.

A sweep of all 25 registered `file`+`version` entries found 8 matching, 6
differing only by a `v` prefix (`v1.0` in file vs `1.0` in manifest), 8 with no
`**Version:**` line at all, and 1 apparent conflict that proved to be a
measurement error (below).

**(b) Recorded commit hashes decay silently.** Of backticked commit-shaped
references across `wiki/`, `manifest.yaml`, `studies/`, and `corpus/`,
**115 resolve and 21 do not**. A history rewrite orphaned the 21. Three were
re-identified by exact commit-message match and fixed on 2026-08-02
(`e1e4cba`→`aa75817`, `c3654f6`→`faef450`, `c026756`→`be7271a`); **18 remain**.

**(c) A five-item reference set was enumerated as four by two silent
scope-narrowers (found 2026-08-02, E2 flag-3 investigation).** The persisted
pilot FAIR assessments — the concordance-floor denominator for
validation-phase model selection (amendment §3) — number five, but every
sweep to date returned four: crema-et-al-2024's assessment sits one directory
below the `outputs/*/extraction.json` glob and under the pre-v2.6 top-level
key `infrastructure` rather than `reproducibility_infrastructure`. The
shortfall was visible (five pilots are named throughout the study record) and
was rationalised into prose rather than investigated (erratum-log Entry 2,
coverage correction 2026-08-02; working-notes Observation 20). Unlike (a),
no gate even nominally covers these files: reference data consumed by a
registered analysis currently sits outside the registry altogether.

**The measurement error is itself a design requirement.** The apparent
`assessment_json` conflict — manifest `1.1` versus file `**Version:** 2.1` —
was not drift. Those are two different version axes: the *document* version of
`assessment-schema.md`, and the *payload* `schema_version` stamped into each
`assessment.json`. Both correct. A naive widened check would flag this forever
as a false positive. **Any check must know which axis it is comparing**, which
means the manifest has to say so.

## 2. Operational definition

Adapted from the charter's §1:

> Every entity registered in `manifest.yaml` either **carries a mechanically
> verified anchor to a less-writable artefact**, or **declares the weaker
> guarantee explicitly**, in a form the gate reports rather than assumes.
> Coverage is generated from the registry, never asserted by hand.

The second clause already exists in miniature and works: `mirror_mode:
structural` declares that prose divergence is undetected and warns on every
run. That pattern — *announce the weaker guarantee, don't quietly hold it* —
generalises to every entity class.

Corollary, and the lesson of Observation 16: **reliability transfers exactly as
far as a structural check exists.** A gate that reports PASS over a narrower
scope than its readers assume is worse than no gate, because it converts an
open question into a false assurance.

## 3. Authority hierarchy (least-writable first)

Does not currently exist explicitly; several checks assume it informally. It
should be written down, because it decides which side of a mismatch is wrong.

1. **The lodged OSF registration** (DOI 10.17605/OSF.IO/DQNHG, lodged
   2026-07-20) and the frozen artefact set at tag
   `osf-prereg-phase2-2026-07-20`, commit `ee3fda3`. Never edited; a divergence
   is corrected on the *other* side, or becomes an erratum.
2. **Amendments and the erratum register** — authority for *what was decided*,
   never for *what the registration says* (charter's rule, worth importing
   verbatim: the errata register in map-reader had itself carried false
   content).
3. **Canonical instruments** —
   `studies/open-science-compliance/protocol/instruments/*.md`, each carrying a
   version line and an end-of-file receipt token.
4. **`manifest.yaml`** — the registry; authoritative for *what is registered*,
   not for the content of what it registers.
5. **Operational artefacts** — prompts, schemas, agent definitions, templates.
6. **Generated artefacts** — `meta.json`, coverage reports, rendered docs.
   Never hand-edited; verified by regeneration.
7. **Wiki prose** — continuity, working notes, reflections. Lowest authority;
   this is where the 21 stale hashes live, and that is the expected place for
   decay.

## 4. Entity classes and their checks

The registry currently mixes entities that need genuinely different checks.
Naming the classes is what makes "check everything hard" tractable.

| Class | Entities | Check | Status |
|---|---|---|---|
| **E1 Frozen instrument** | the 7 `shared_content` canonical files | version line + receipt token + byte-exact mirror regions (named segments) + reverse sweep | **implemented** |
| **E2 Agent definition** | `.claude/agents/*.md` | sha256 of whole file + model pin vs frontmatter + registry both directions | **implemented** |
| **E3 Versioned prose artefact** | extraction/assessment/reproduction prompts, planning guides, launch primers | version line vs manifest, with `v`-prefix normalised | **absent** |
| **E4 Versioned data artefact** | JSON schemas | internal `version` / `const` field vs manifest; no `**Version:**` line exists | **absent** |
| **E5 Two-axis entity** | `assessment_json` and anything like it | manifest must name *which* axis it tracks; check that axis only | **absent; requires registry change** |
| **E6 Unversioned registered file** | templates (`log-template.md` etc.) | existence + optional content hash; must declare "unversioned" explicitly rather than silently having no check | **absent** |
| **E7 Cross-reference** | commit hashes, file paths, and DOIs cited in registered docs | resolvability (`git cat-file -t`, path exists, DOI resolves) | **absent** |
| **E8 Reference dataset** | the five pilot FAIR assessments (the §3 concordance-floor denominator); any future set an analysis reads as ground truth | explicit per-item path **and JSON key path** declared in the registry; enumeration generated from the registry, never re-derived by glob; expected cardinality asserted and checked | **absent; items not registered at all** (added 2026-08-02 from finding (c)) |

## 5. Proposed registry reorganisation

The minimum change that makes E3–E7 checkable is an explicit per-entity check
declaration. Sketch only — exact key names to be settled at implementation:

```yaml
  preparation:
    version: "1.1"
    file: reproduction-system/prompts/01-preparation.md
    check:
      class: E3                 # versioned prose artefact
      version_source: markdown-heading   # **Version:** line
      normalise: strip-v-prefix
```

```yaml
    assessment_json:
      version: "1.1"
      file: .claude/skills/research-assessor/references/schema/assessment-schema.md
      check:
        class: E5
        version_source: json-field
        json_path: '$.schema_version'   # the PAYLOAD axis, not the doc heading
        note: "document heading is 2.1 — a different axis; do not reconcile"
```

Two properties matter more than the syntax:

- **No entity may lack a `check` block.** A registry entry with no declared
  check fails the gate. This is the reverse sweep generalised from files to
  entities, and it is what structurally prevents "7 of 25" from recurring.
- **`class: none` is legal but loud** — the E6 case. It declares the absence of
  a check, and the gate warns on every run, exactly as `mirror_mode: structural`
  does today.

## 6. Coverage self-report

Directly from the charter: the coverage matrix is **generated, never
hand-maintained**. The gate should end its run with a line of the form

```
manifest consistency: PASS — 25/25 entities checked (E1:7 E2:6 E3:8 E4:2 E5:1 E6:1), 0 undeclared
```

so the *scope* of the assurance is visible in the same breath as the verdict.
Had this existed, the 7-of-25 gap would have been obvious from the first run
rather than found by probe eight months later.

## 7. Where the map-reader analogy stops

Worth stating so the apparatus is not over-imported:

- **map-reader verifies prose claims against artefacts**; the anchor is a
  number in a document and the check recomputes it. **This repo verifies
  artefacts against each other** — registry against file, canonical against
  mirror. Ledger rows with `claim_text`/`evidence` verbatim spans are the right
  shape there and mostly the wrong shape here; our equivalent of a verbatim
  span is the byte-exact mirror region, which already exists.
- **No JSONL ledger is proposed.** map-reader needs one because its claims are
  discovered by reading and cannot be re-enumerated mechanically. Our entities
  are enumerable from `manifest.yaml` on every run, so the registry *is* the
  ledger. Adding a parallel ledger would create the two-hand-maintained-records
  drift pathology that decision D-10 in the corpus plan exists to avoid.
- **Governance consequences differ.** A drift here can require an OSF erratum or
  amendment; map-reader's charter has an analogous errata register but the
  frozen-artefact-set boundary is specific to this study, and the gate must keep
  reporting which side of that boundary a divergence falls on.
- **Worth importing wholesale:** the least-writable-authority principle, the
  generated-coverage rule, the verdict vocabulary
  (VERIFIED / CORRECTED / FLAGGED / DEFERRED), and the build-time revalidation
  stance — *the swept state must persist rather than decay*. That last one is
  the whole point: the April-2026 map-reader audit verified a snapshot and
  decayed, and our 21 stale hashes are the same decay in a different medium.

## 8. Phasing

Each phase ends at a **GATE** — Shawn reviews before the next starts.

- [x] 2026-08-03 **Phase 0 — enumerate and classify.** Done — output in §10
      (55 entities, per-entry version re-check run same day, no true drift;
      four missing-version-carrier flags for Phase 1). **GATE: presented for
      review 2026-08-03.**
- [x] 2026-08-03 **Phase 1 — registry reorganisation.** Done, gate-approved
      same day. Implementation decision (the "settled at implementation"
      the §5 sketch anticipated): a central `entity_checks:` map keyed by
      dotted registry path, not inline per-entry blocks — one insertion
      point, the commented sections above it untouched. 56 declarations
      (E1:7, E2:6, E3:26, E4:3, E5:1, E6:12, E8:1) plus the
      `reference_datasets:` E8 registration (five items, declared keys,
      all five verified resolving to `binary_sub_principles` assessments).
      Two version carriers added (`input/workflow.md` gains a Version
      line; the credibility JSON schema gains a top-level `version`
      field). **Two Phase 0 flags dissolved on closer reading** — the
      skills carry `version:` in SKILL.md frontmatter matching the
      manifest, and the credibility template carries `**Assessor
      Version:** v1.0`; the Phase 0 regex looked only for `**Version:**`,
      an instance of the very scope-narrowing this plan exists to catch.
      Their actual carriers are now declared (`skill-frontmatter`,
      `header_label`). Gate PASS, 32/32 tests. **GATE.**
- [ ] **Phase 2 — widen the checker.** Implement E3/E4/E5/E6, the
      `v`-prefix normalisation, and the undeclared-entity failure. Extend the
      test suite (currently 32 tests) with a negative test per class — each new
      check must be demonstrated to fail on an injected defect, per the existing
      fixture pattern in `tests/test_manifest_consistency.py`. **GATE.**
- [ ] **Phase 3 — coverage self-report.** Emit the §6 line; wire into
      pre-commit and orchestrator pre-flight. **GATE.**
- [ ] **Phase 4 — E7 cross-reference resolvability.** Commit-hash resolution
      first (18 known stale refs to remap by message match), then paths, then
      DOIs. Likely warn-only at first: these live in low-authority prose and
      should not block a commit until the backlog is cleared.

**Sequencing note.** None of this blocks the amendment lodgement (pending
task E) or the validation phase. It should not start until the amendment is
lodged, because Phase 2 touches the gate that guards the frozen artefact set,
and changing that gate between now and lodgement would mean the lodged state
was verified by a different instrument than the one described.

## 9. Open questions — RESOLVED (Shawn, 2026-08-03)

1. **Scope of "registered entity" — NOT registered.** The `wiki/`
   four-artefact set stays deliberately low-authority prose, per the §3
   hierarchy (level 7 is the expected place for decay). The E7 sweep checks
   references *in* wiki files without registering their content.
2. **E7 severity — warn-first**, then revisit tightening once the stale-hash
   backlog is cleared.
3. **The 18 stale hashes — one verified pass, early in Phase 4.** Each remap
   by exact commit-message match, verified per commit, never guessed.
4. **Crema's divergent artefact — register-without-rewrite.** The run-02
   file records what a 2026-01 run actually emitted; the E8 registry entry
   declares its path and its `infrastructure` key, extending the
   declare-the-axis principle (§5) to declare-the-key.

## 10. Phase 0 output — registry enumeration and classification (2026-08-03)

Every `manifest.yaml` entry enumerated and classified; every E3/E4 version
re-checked against its file **today** (post schema-v2.7 merge, `58c3fe7`),
not inherited from the 2026-08-02 sweep. Paths shortened:
`instruments/` = `studies/open-science-compliance/protocol/instruments/`.

**E1 — frozen instruments (7), check implemented, all PASS today:**
fair-instrument 2.0 (mirror: Pass 6 prompt, byte-exact region);
data-availability-taxonomy 1.0; verdicts-and-precision 1.0 (mirror:
reproduction SKILL.md, six named segments); coverage-rules 1.0;
eligibility-criteria 1.0; pipeline-invariants 1.0 (`.claude/shared/`);
adversarial-review-framework 1.1.

**E2 — agent definitions (6), check implemented (sha256 + model pin +
registry both directions), all PASS today:** fair-assessor-sonnet-5 /
-opus-5 / -fable-5, reproduction-planner, reproduction-executor,
adversarial-reviewer, all v1.0.

**E3 — versioned prose artefacts (26), check absent:**

| Entity | Manifest v | Today's finding |
|---|---|---|
| components.workflow | 5.0.0 | **no `**Version:**` line in `input/workflow.md`** — Phase 1: add line or declare source |
| components.extraction_plan | 1.1.0 | match |
| components.extraction_launch | 2.0.0 | match |
| assessment.prompts ×6 | 1.0–1.1 | all match (v-prefix, normalise in checker) |
| assessment.templates.credibility_report | 1.0 | **no version line in file** — Phase 1: add or declare |
| reproduction.planning_guide, .launch | 1.0.0 | match |
| reproduction.prompts ×4 | 1.0–1.1 | all match |
| components.skill, reproduction.skill | 2.6, 1.1 | **directory-scoped** — Phase 1: declare version_source (SKILL.md header?) |
| workflow_passes prompts ×8 | **(no version field in registry)** | files carry headers (2.7 Pass 1–7 post-cascade; pass 0 = 1.0.0; pass 6 = 2.0) — Phase 1: add version fields |

**E4 — versioned data artefacts (3), check absent:** components.schema 2.7
(JSON version field matches); components.schema.previous 2.6 (pinned
historical, matches — checker should assert the const); 
assessment.schemas.credibility_report 1.0 (**JSON carries no version
field** — Phase 1: add field or declare none).

**E5 — two-axis (1):** assessment_json — payload 1.1 vs document 2.1, both
correct, axis note already in the manifest; Phase 1 formalises
`json_path`.

**E6 — unversioned registered files (12), no explicit check:** 3
reproduction templates, 8 documentation pointers, corpus.queue_file.
Phase 1: explicit `class: none`-or-hash declarations, loud not silent.

**E7 — cross-references (check class, not entities):** 115 resolve / 18
stale remain, all in `wiki/`. Warn-first (Q2); one verified remap pass
early in Phase 4 (Q3).

**E8 — reference datasets (1 set, 5 items, unregistered):** the pilot FAIR
assessments — dye-et-al-2023, herskind-riede-2024, key-et-al-2024,
marwick-2025 (key `reproducibility_infrastructure`), crema-et-al-2024
run-02 (key `infrastructure`, one directory deeper). Register per Q4:
per-item path + JSON key path + asserted cardinality of five.

**Coverage as it stands: 55 registered entities; 13 checked hard (E1+E2),
42 unchecked or implicit; plus one unregistered E8 set.** No true drift
found today — the four flagged items are missing version carriers, not
mismatched versions.
