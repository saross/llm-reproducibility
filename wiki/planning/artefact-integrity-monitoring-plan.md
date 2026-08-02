---
title: "Artefact-Integrity Monitoring — Plan v0.1"
tags: [infrastructure, reproducibility, governance]
created: 2026-08-02
updated: 2026-08-02
status: draft-for-approval
---

# Artefact-Integrity Monitoring — Plan v0.1

**Status: DRAFT, NOT IMPLEMENTED.** Written 2026-08-02 on Shawn's decision to
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

Two findings from 2026-07-27 and 2026-08-02, both re-verified at source:

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

- [ ] **Phase 0 — enumerate and classify.** Assign every current registry entry
      to a class from §4; produce the coverage table as it stands. No code
      changes. Output: a table in this file. **GATE.**
- [ ] **Phase 1 — registry reorganisation.** Add `check:` blocks for all
      entries. Purely additive to `manifest.yaml`; gate not yet reading them.
      **GATE.**
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

## 9. Open questions for Shawn

1. **Scope of "registered entity"** — §4 covers what `manifest.yaml` names.
   Should the `wiki/` four-artefact set (continuity, working-notes,
   reflections, user-observations) also be registered and checked, or does it
   stay deliberately low-authority prose?
2. **E7 severity** — block commits on an unresolvable commit hash, or warn?
   Warn-first is proposed; blocking would currently fail 18 times.
3. **The 18 remaining stale hashes** — remap by message match in one pass, or
   leave and let the E7 check surface them as they are touched?
