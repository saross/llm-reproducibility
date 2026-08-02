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

---

## Entry 2 — 2026-07-27: Pass 6 prompt restated the FAIR instrument incompletely

**Artefact affected:** `extraction-system/prompts/06-infrastructure_pass6_prompt.md`
(uploaded to OSF as markdown in the frozen artefact set at `ee3fda3`).
**Discovered by:** extending the manifest-consistency check
(`scripts/check-manifest-consistency.py`, build item D5) with a byte-exact
comparison of the marker-delimited mirror region against the canonical file
(`studies/open-science-compliance/protocol/instruments/fair-instrument.md`,
extracted 2026-07-24). The check as first built compared the canonical file's
fenced code blocks and table rows — all of which matched. The banner added at
extraction asserted a *verbatim* mirror; the first byte-level comparison showed
the assertion was untrue, because everything missing was prose.
**Corrected in repository:** 2026-07-27 (see the session log).

Four normative statements present in preregistration §7.1 and in the canonical
file were absent from the operational prompt:

| # | Omitted from the Pass 6 prompt | Source |
|---|---|---|
| 1 | "Unscoreable sub-principles score 0 (the instrument scores evidenced practice)" | Registration §7.1 |
| 2 | Scores are "never aggregated into a combined score" | Registration §7.1 |
| 3 | The A1 completeness rule in full: "A1 requires that a majority of the research data be retrievable via standard protocol, with an exception for documented ethical/legal restriction" (the prompt carried only the coverage-category trigger) | Registration §7.1 |
| 4 | The FAIR4RS out-of-scope statement (planned amendment-path extension, not part of this registration) | Registration §7.1 |

**Correction.** The prompt's FAIR section now embeds a byte-exact,
marker-delimited copy of the canonical instrument. Pass 6 workflow content that
previously interleaved with the instrument — output JSON structures, the
coverage-category threshold table, the barrier-type enumeration, and the
context-dependent assessment notes — was relocated below the mirrored region
under a heading marking it as workflow guidance, not instrument. No workflow
content was removed: the restructure was performed programmatically and the
result diffed line by line against the original, every difference accounted for
as either a canonical rewording or one of the four additions above.

**Impact assessment.** The registration's normative instrument statement (§7.1)
is unchanged and was always the governing text; the defect was an incomplete
operational restatement of it, so this is the same erratum class as Entry 1.
Checked against the persisted pilot outputs
(`studies/open-science-compliance/outputs/*/extraction.json`, the four papers
carrying FAIR assessments — dye-et-al-2023, herskind-riede-2024, key-et-al-2024,
marwick-2025):

- all four use the `binary_sub_principles` /15 scale;
- no sub-principle is recorded unscored (zero null `present` values), so
  omission 1 changed no pilot score;
- no output carries a combined or aggregate FAIR field, so omission 2 was
  honoured in practice;
- omission 3 was likewise applied where it bit — key-et-al-2024 records
  A1 = false with the evidence "Only 3 of 13 datasets (23.1%) retrievable via
  HTTPS", the majority rule operating as registered;
- omission 4 is declaratory and affects no score.

**Coverage correction (2026-08-02).** The scoping statement above — "the four
papers carrying FAIR assessments" — under-counts. A fifth persisted FAIR
assessment exists, for crema-et-al-2024, at
`studies/open-science-compliance/outputs/crema-et-al-2024/run-02-session-per-pass/extraction.json`.
The 2026-07-27 sweep missed it for two structural reasons: the file sits one
directory below the `outputs/*/extraction.json` pattern swept, and it stores
the assessment under the pre-v2.6-convention top-level key `infrastructure`
rather than `reproducibility_infrastructure`. Located 2026-08-02 on the
registrant's query and re-checked the same day: it uses the
`binary_sub_principles` /15 scale (data 12/15, code 12/15, matching pilot
findings report v1.2 Table 5 exactly), leaves no sub-principle unscored,
carries no aggregate field, and records A1 present — so key-et-al-2024 remains
the one pilot where the A1 majority rule was decisive. All four impact
conclusions above therefore hold across five of five pilots; this entry's
conclusion is strengthened, not weakened. (The related run-01 artefacts were
archived, not deleted — `c41242b`, 2026-01-13. Working-notes Observation 20
records the sweep-scope lesson; the monitoring plan §1(c) and class E8 carry
the structural fix.)

Classification: erratum-class corrections aligning the operational file with the
registration's own normative text; no instrument semantics changed and no pilot
score is revised. The corrections ride the §8 regression gate with the Phase 1
validation runs, and this entry folds into the consolidated amendment below.

**Recurrence prevented.** The mirror is now byte-compared on every commit and at
orchestrator pre-flight. A future divergence fails loudly instead of persisting
behind a banner asserting it cannot happen — which is the failure mode this
entry documents: the assertion was written before anything checked it.

**Related finding, resolved the same day — deliberately not an erratum.** The
same comparison showed the second registered mirror — `verdicts-and-precision.md`
into the reproduction-assessor `SKILL.md` — carried the canonical prose only in
reworded form, and omitted two things outright: the sentence escalating
PAPER_ERROR findings for human confirmation before they enter study data, and
the environment-specification levels 0–5 (registration §7.5), which the skill
never carried at all.

No erratum entry and no amendment are required for that mirror, on three
independent grounds. First, `SKILL.md` is not part of the frozen artefact set —
the registration froze four files (the preregistration draft, the pilot findings
report, `study-protocol.md`, and the Pass 6 prompt), and an erratum by definition
records a defect in a frozen artefact. Second, the content brought into line is
either not registered at all (the discrepancy vocabulary — `CANNOT_COMPARE`,
`PAPER_ERROR`, `MAJOR_DISCREPANCY` — appears nowhere in the registration; it
comes from the reproduction-assessor protocol v1.1 that §7.2's "definitions as
in" clause points to) or is registered text already faithfully carried by the
canonical file (§7.4 precision, §7.5 environment levels). Third, converging a
mirror changes delivery, not instrument semantics: it removes a divergence
between two lanes rather than altering what either lane is supposed to apply.
It is therefore an ordinary §8 implementation change, riding the Phase 1
regression gate with everything else before production use.

**Resolved 2026-07-27:** the mirror is now byte-exact. Because the canonical
content lands in four different places in the skill's workflow, the check gained
named segments (`#precision`, `#tolerances`, `#discrepancy`, `#verdicts`,
`#scope`, `#environment`), each compared separately, so the skill keeps its
structure without giving up byte-exactness. `mirror_mode: structural` — the
declared-weaker fallback — is retained in the checker for any future mirror that
genuinely cannot be segmented, and warns on every run when used. Nothing in the
registry uses it now.

---

## Queued amendment scope (running list)

**Consolidated draft written 2026-07-24:** `amendment-1-draft.md` (this
directory) carries the lodgement wording for every item below plus Entry 1;
new entries added here after that date must also be folded into the draft
(its pre-lodgement checklist enforces this).

**RATIFIED by the registrant 2026-07-24** (proposed the same day from the
pre-build juncture review, findings D-1/D-4/D-5 + E-1/E-4/E-7/E-8; report at
`wiki/planning/reviews/2026-07-24-pre-build-juncture-review.md`). Registrant's
lodgement timing decision: **defer to the hard stop** — the amendment lodges
just before the validation phase runs, so any further errata found during the
corpus and Phase 1 builds accumulate into the same single amendment.
**Deadline note:** items 2–4 below govern the combined validation phase itself, so
the consolidated amendment must lodge **before the validation phase runs** — earlier
than the before-census-scoring deadline that Entry 1 alone would require.

1. **Entry 1 and Entry 2 corrections** (Pass 6 instrument defects, above) — already
   committed to an amendment; fold in here. Entry 2 was found on 2026-07-27, after the
   consolidated draft was written, by the D5 check's first byte-exact mirror
   comparison; the draft's §1 and its pre-lodgement checklist are updated accordingly.
2. **Below-threshold remediation ladder** (routing design §2.2): one routing-fix
   attempt (delivery mechanism only; instrument text untouched) followed by a re-run
   of the §8(a) stability check, permitted **once**; a still-below-threshold re-run
   → the registered majority-vote consequence applies with no further iteration;
   both pre-fix and post-fix reliability results reported with study outcomes.
3. **Validation-phase pre-specifications:**
   - *Agreement statistic* for the 3-run stability check — proposed: **unanimity
     proportion** (strictest of the three candidate definitions; the review shows
     the candidates cross the 0.90 gate at item-flip rates from ~10% to ~30%, so
     the choice cannot be left implicit).
   - *Pilot-paper set* — proposed: **all five** pilot papers (preregistration says
     "at least three"; n rises 90→150 items and the false-pass rate at true 0.85
     halves, ~12%→~5.5%; no amendment strictly required for this item, recorded for
     completeness).
   - *Model-selection rule* — proposed: **gates-plus-cost**. The spot-check cannot
     statistically rank models (±0.09 confidence interval on an agreement
     difference; no preregistration-compliant n exists before the census). Any
     model passing (a) the 0.90 stability gate and (b) a concordance floor against
     the pilot reference scores (proposed ≥0.90 on the same statistic — the
     accuracy gate, review E-4) is eligible; among eligible models the cheapest
     scores the census; agreement differences inside the confidence interval are
     pre-declared not to be selection grounds.
   - *Within-phase ordering:* spot-check → select model → regression-gate the
     **selected** configuration (both lanes pinned) → census.
   - *Run independence and provenance:* each run is a fresh spawn with no shared
     context and no persistent memory; sampling seeds are not controllable in this
     harness, so each run records session ID, timestamp, and the full receipt
     triple {instrument_versions, agent_version, model_id}, and reports state that
     run-to-run variation reflects default-temperature sampling.
4. **Read-scope isolation rule** (review D-4): validation-phase scoring runs
   execute with read access only to the paper source and the pushed/pulled
   instrument files — the repository holds the pilot papers' canonical scores, so
   an unisolated scorer could reproduce recorded answers and return perfect,
   uninformative agreement. Enforced by tool allowlist/sandbox scope and verified
   from the harness transcript; per-run file-access lists archived with run
   artefacts. The same hygiene applies at census to any paper with pre-existing
   repository artefacts.
5. **Robustness annex** (review E-7): scored runs from non-selected passing model
   arms are archived and citable as cross-model robustness data, not discarded.
