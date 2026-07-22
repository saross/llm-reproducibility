# OSF registration erratum log — Phase 2 preregistration

**Registration:** <https://osf.io/dqnhg/> — DOI 10.17605/OSF.IO/DQNHG,
lodged 2026-07-20, public 2026-07-21.
**Frozen artefact set:** repository state at commit `ee3fda3`
(tag `osf-prereg-phase2-2026-07-20`).
**Purpose:** records defects discovered in the frozen registration artefacts
after lodgement, together with the corresponding repository-side corrections.
The frozen Open Science Framework (OSF) copies cannot be edited by design;
entries here accumulate until an amendment is worthwhile, at which point this
log is folded into a dated OSF amendment. Any instrument-affecting change must
pass the preregistration §8 regression gate, and an amendment must be lodged
before census scoring begins (prereg §8–§9). Decision path approved by the
registrant 2026-07-22 (erratum log now; amendment when warranted).

---

## Entry 1 — 2026-07-22: three defects in the Pass 6 FAIR instrument prompt

**Artefact affected:** `extraction-system/prompts/06-infrastructure_pass6_prompt.md`
(uploaded to OSF as markdown in the frozen artefact set at `ee3fda3`).
**Discovered by:** implementation review of the agent content-routing design
(`wiki/planning/reviews/2026-07-22-routing-design-implementation-review.md`,
finding D1), with each defect re-verified at source against both the working
tree and `git show ee3fda3` before correction.
**Corrected in repository:** commit `abdc526` (2026-07-22).

| # | Defect (line refs in the frozen copy) | Correction |
|---|---|---|
| 1 | Stale scoring example "Total FAIR score (e.g., 14/16)" / "87.5%" at lines 662–663, contradicting the v2.0 rubric of 15 binary sub-principles defined at lines ~115–163 of the same file | Example corrected to 14/15 / 93.3% |
| 2 | Legacy "5-level access taxonomy" (Level 0–4) at lines 202–208, colliding in vocabulary with the preregistered six-level data-availability taxonomy (L1–L6, registration §7.3) | Renamed to "five-tier access classification (Tier 0–4)" with an explicit demarcation note; the L1–L6 taxonomy remains reproduction-time-only per §7.3 |
| 3 | Dead file pointer "→ See `wiki/planning/REPRODUCIBILITY_INFRASTRUCTURE_SCHEMA.md`" at line 802 (file removed in the 2026-07-03 wiki migration) | Repointed to `extraction-system/schema/extraction-schema-v2.6.json` (canonical), with the archived proposal noted as historical reference |

**Impact assessment.** The registration's normative instrument statement
(§7.1: 15 binary GO-FAIR sub-principles, independent data/code scoring) is
internally consistent and unaffected. The pilot re-scoring (standardised
2026-02-11) demonstrably applied the /15 scale — all five pilot papers carry
/15 scores (pilot findings report v1.2, Table 5) — so no scored output was
produced under the defective example. Defects 1 and 3 are clerical
(a stale worked example from the pre-standardisation era; a pointer broken by
a file move). Defect 2 is a vocabulary-collision hazard rather than a scoring
error: the access tiers feed only the data-completeness coverage computation,
and no persisted schema field uses the "Level n" labels (verified against
pilot `extraction.json` files — `data_completeness` stores aggregate counts
only). Classification: erratum-class corrections that align the operational
file with the registration's own normative text; no instrument semantics
changed. The corrections will nonetheless ride through the §8 regression gate
with the Phase 1 validation runs before census scoring, and this entry is
queued for inclusion in the first OSF amendment.
