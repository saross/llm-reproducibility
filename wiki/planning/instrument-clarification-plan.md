---
title: "Instrument clarification plan — amendment 2 route"
tags: [governance, validation, planning]
created: 2026-08-03
updated: 2026-08-03
status: active
---

# Instrument clarification plan — amendment 2 route

**Decision (Shawn, 2026-08-03):** the amendment 1 §2 routing-fix card is
declined as the candidate stood; the project takes the instrument-
clarification route (benchmark summary, registered decision path 3).
Overriding goal: a robust and useful instrument — root problems are solved
even where that requires errata or a further amendment. Shawn contributes
FAIR (Findable, Accessible, Interoperable, Reusable) domain expertise at
Phase B.

**Compliance position.** The preregistration's erratum-then-amendment
mechanism is established practice in this project (amendment 1 lodged
2026-08-03, Open Science Framework (OSF) registration Version 2, DOI
10.17605/OSF.IO/DQNHG). Amendment 2 will be dated and lodged *before* the
re-validation it governs, and both pre-fix and post-fix reliability results
are reported with study outcomes, per amendment 1 §2's reporting rule
(`studies/open-science-compliance/prereg/amendment-1-draft.md:109–118`).
Because amendment 2 changes instrument text, it re-specifies the validation
check itself; the §2 ladder is restated within amendment 2 rather than
consumed (see Phase D).

## Evidence base (verified 2026-08-03, this session)

- **The routing-fix premise held only for the sonnet arm.** Pull receipts
  (`.receipts.pulled_files_read` across
  `studies/open-science-compliance/outputs/validation/benchmark-2026-08/arm-*/run-*/*.json`):
  sonnet-5 pulled `fair-principles-guide.md` in 9/15 spawns; opus-5 and
  fable-5 in 15/15 each. Both full-pulling arms failed both 0.90 gates
  (stability 0.873 / 0.813; concordance 0.807 / 0.820 —
  `benchmark-summary.md`).
- **The disagreement is item-structured and survives full guide exposure.**
  Top disagreement sub-principles in the full-pulling arms: R1.1 (5 and 4
  items), A1.2 (4 and 4), A2 (2 and 4), plus R1.3, I3, and the F-block
  upstream-crediting question (dye-et-al-2023 flips 6–13 on data FAIR
  within the fable arm).
- **The interpretation guide is silent on the disputed cases.** Its A1.2
  guidance
  (`.claude/skills/research-assessor/references/infrastructure/fair-principles-guide.md:180–184`)
  covers restricted-with-justification and closed-without-justification but
  never the fully-open, no-authentication-needed case; the R1.1 licence
  target and F-block upstream questions are likewise unaddressed. Pushing a
  document that does not contain the answer cannot make the answer uniform.
- **Within sonnet, guide absence does correlate with instability** — of its
  29 disagreement items, roughly 17 have the minority vote from a guideless
  spawn against ~11 expected by chance (hand-tallied 2026-08-03 from
  `arm-sonnet-5/run-record.json` `.stability.disagreements` plus receipts;
  the Phase A script re-verifies this figure). Real but secondary: the
  binding constraint is concordance, which no delivery fix plausibly lifts
  from 0.773 to 0.90 when full-exposure arms sit at 0.807/0.820.
- **The concordance gate is structurally confounded** (benchmark summary):
  reference scores were produced with reproduction-informed context under
  the pre-clarification instrument; the census lane scores from the paper
  alone. Phase B addresses this.

## Phase A — root-cause analysis and clarification drafting (no API spend)

- [x] 2026-08-03 **A1. Disagreement mining pass.** Script recomputes stability and
      concordance from the 45 spawn outputs and the E8-registered reference
      scores (`manifest.yaml:510–533`), verifying the published figures;
      extracts every disputed item (within-arm disagreement or
      majority-vs-reference mismatch) with each spawn's `evidence` string;
      clusters by sub-principle and ambiguity class. Outputs:
      `disagreement-analysis.md` (+ machine-readable `disputed-items.json`)
      in the benchmark package. Also re-verifies the sonnet
      guideless-minority correlation above.
- [x] 2026-08-10 **A2. One clarification draft per ambiguity class** —
      all eight decision points ruled by Shawn (see rulings sections
      above); drafted operative text written as erratum-log **Entry 3 +
      "Queued amendment 2 scope"** (ten items, in
      `studies/open-science-compliance/prereg/erratum-log.md`).
      **RATIFIED 2026-08-14:** registrant read the log end-to-end and
      approved, incorporating the 2026-08-11 ratification-read
      consolidations (item-1 clause restored; two-rung ladder; per-artefact
      licence scope; endpoint/table independence; supplement-row
      qualification). Original decision list, for the record:
      - A1.2 — does a fully open resource needing no authentication score 1?
      - R1.1 — which artefact's licence counts?
      - A2 — metadata persistence for supplement-only deposits.
      - R1.3 — what counts as a domain-relevant community standard?
      - F-block — does a DOI-bearing *upstream* dataset credit the paper's
        own data FAIR?
- [x] 2026-08-15 **A3. Align `fair-principles-guide.md`** with the clarified
      text and decide its routing — DONE in the D1 window (branch
      `feat/d1-amendment-2-window`): guide v1.0 → v1.1 with an
      instrument-v2.1 alignment section (supremacy clause; F1/A1.2/R1.1/
      R1.3 bullets patched to the ratified rules), registered in
      `shared_content` and **promoted pull → push** to all three
      fair-assessor arms, receipt token + version line + C7 hash;
      push-list regression test pins the promotion. Original candidate
      adopted as drafted: interpretive context uniform by construction,
      pre-declared in amendment 2 §5 (not consuming the routing-fix
      attempt).

### Working position on decision point #1 (2026-08-10, pending scout)

**The assessment target is the "research surface"** (Shawn's framing): the
study assesses credibility — reproducibility, transparency, FAIRness — from
a reviewer's, funder's, or consumer-researcher's standpoint. What matters is
what the available research surface of the publication supports as the
culmination of the research programmes that produced it (the authors' work
and whatever the authors chose to utilise), not who created or deposited any
given artefact. Consequences accepted:

- Well-archived third-party inputs earn full credit; closed or unpublished
  inputs are penalised even where blameless — the empirical status of the
  research is what is measured, fault is not.
- Decision points #1 and #8 merge: the coverage denominator and the
  assessment object are the same rule ("the set of artefacts required to
  reproduce the result").
- **Provenance is recorded as a per-input flag** (author-deposited /
  third-party / undeterminable) that never touches scores — keeping fault
  visible as a reportable *finding* (e.g. the share of FAIR failures
  attributable to upstream artefacts). Flag rides the schema work (C3).
- The aggregation rule for heterogeneous input sets is acknowledged
  non-trivial: make a reasonable initial choice, iterate until results
  "vibe right" against pilot papers, and declare instrument refinement an
  explicit research goal as the study expands.
- Final ruling deferred until the prior-art scout report
  (`wiki/planning/scout-reports/2026-08-10-fair-third-party-artefacts-prior-art.md`)
  is in and verified, so any departure from field convention is deliberate
  and citable.
- **Scout's two full-text gaps closed by direct reads (2026-08-10; PDFs in
  Zotero, collection Archaeology-reproducibility).** Both strengthen the
  working position. *Marwick 2017* (JAMT 24(2), manuscript p. 6): the
  release obligation attaches to "the most raw form possible of the data
  from which the summaries and plots were generated" — the paper's
  evidentiary basis, with no authorship gate — while "the provenance of
  the data must always be stated, even if the data are not publicly
  accessible" (copyright, cultural sensitivity acknowledged as legitimate
  closure); the Madjebebe compendium treats its nineteen user-contributed
  R packages as declared infrastructure, not a liability. *Tedersoo et
  al. 2021* (Sci Data 8:192): unit is the article; availability of "most
  critical data" is coded by access method with storage options that
  explicitly include "previous publications" and "museum" (Fig. 9) — 
  reused/third-party holdings count as the article's data — and authors'
  reasons for declining (data lost, agreements, privacy; Fig. 8) are
  recorded as findings separate from the availability score: the
  score-status/record-reasons split already operating in a major audit.

**Stretch goal (not scheduled):** a sidecar report per paper — "how did
these researchers, at their stage of the greater research chain, do on
reproducibility?" — crediting value added (data/code clean-up, artefact
quality). Side quest; recorded so it is not lost.

### Scout verification outcome (2026-08-10)

The adversarial verifier found **material defects in the scout draft**:
four direct quotations do not exist at their cited sources, and the ACM
Artifact Review and Badging claim is **inverted** — the operative v1.1
"Artifacts Available" text reads "**Author-created artifacts** relevant to
this paper have been placed on a publically accessible archival
repository…", so ACM is origin-gated: a named **counter-example** the
research-surface rule deliberately departs from, not supporting precedent.
The JIE Data Openness Badges precedent survives on its verified text (gold
data contribution via "links to external or secondary data sets (including
licensed databases)"; the scheme's own term is "secondary data", and its
"not data ownership" framing sentence was fabricated). RDA FDMM must be
cited as v1.00, DOI 10.15497/rda00050 (the draft cited the superseded
v0.90 draft DOI). Cite ONLY the verified report
(`…-prior-art-verified.md`); the draft is banner-marked superseded.
**Process finding (working-notes candidate, pending verdict):** the
proposer's claims ledger passed 65/68 while every fabricated quotation sat
outside the emitted claim set — a claims-ledger audit clears exactly the
prose it never covers (Observation-16 shape); verifier recommends
requiring claim emission for every direct quotation (prior-art-scout agent
definition change, Shawn's tooling, pending his nod).

### Ruling — decision point #1 (RULED: Shawn, 2026-08-10)

**Adopted as drafted, as the baseline to iterate from.** Decision point #8
(coverage denominator) is merged into this rule; the aggregation rule for
heterogeneous input sets is drafted under A2 as a reasonable initial
choice and iterated per the 2026-08-10 decision.

> **Research-surface rule.** The unit of assessment is the paper's
> research surface: the complete set of digital artefacts — data, code,
> and other digital inputs — required to reproduce the paper's reported
> results, as reachable from the published paper. Each FAIR sub-principle
> scores the empirical status of those artefacts; creator identity,
> depositor identity, and responsibility for closure never affect scores.
> A precisely cited, well-archived third-party input earns full credit; a
> closed or unpublished input is penalised even where closure is beyond
> the authors' control. Provenance (author-deposited / third-party /
> undeterminable) is recorded per required input as non-scoring metadata,
> keeping responsibility reportable as a study finding.

Precedent set (verified): RDA FDMM v1.00 resource/reuse definitions with
no creator-conditioned indicator (10.15497/rda00050); JIE Data Openness
Badges secondary-data rule (10.1111/jiec.12738 + policy page); CODECHECK
author-guide language; Colavizza et al. 2020 category coding; Culina et
al. 2020 (verified negative finding); Tedersoo et al. 2021 storage-mode
coding with decline reasons recorded separately (direct read); Marwick
2017 evidentiary-data framing (direct read). **Named departure:** ACM
Artifact Review and Badging v1.1 (origin-gated) — departed from
deliberately because the study measures the credibility of published
results, not author compliance.

### Rulings — decision points #2–#5 and #7 (Shawn, 2026-08-10); #6 open

- **#2 RULED — two-rung evidence ladder adopted:** (i) paper text;
  (ii) by-construction properties of a closed, instrument-listed platform
  table. Publisher supplements enter that table with a deliberately thin
  entitlement row: standard HTTPS delivery via the article landing page
  and article-level Crossref persistence — but no independent metadata
  record, no licence field, no registry indexing, no resource-level
  identifier of their own.
  *Consolidated 2026-08-11 (ratification read): rung (i) is direct
  evidence — paper text plus the item-8 evidence pack, with same-artefact
  disagreements governed by the specific rules (e.g. most-restrictive
  licence); rung (ii) is the by-construction table, applicable only to
  facts on which rung (i) is silent. Table entitlements are floors, not
  ceilings. The supplement row applies only to supplements served
  directly from the article landing page with no independent deposit;
  repository-hosted supplements (e.g. Figshare-hosted journal
  supplements, Dryad) score as deposits on that platform.*
- **#3 RULED:** A1.2 is satisfied where no restriction is necessary.
- **#4 RULED:** R1.3 targets what GO-FAIR measures — artefact
  reusability, deposit-level standards only; methodological standards
  (IntCal20, OxCal) excluded. Explicitly includes deposit in an
  accredited domain repository whose ingest enforces its metadata
  standard (e.g. ADS, tDAR, DANS) — R1.3 = 1 by construction,
  interlocking with the #2 platform table. Flips the current reference
  score on dye-et-al-2023 data R1.3.
- **#5 RULED (operational):** unless explicitly stated otherwise, an
  article's licence extends to publisher-hosted supplements — check for
  both article and supplement licences (they can differ); absent a
  separate supplement licence, default to same-as-paper. Artefacts hosted
  on third-party services (Zenodo, OSF, GitHub/GitLab, …) MUST be
  licence-checked at the service, via the appropriate API — analogous to
  verifying citations against Crossref/OpenAlex. **Conflicts default to
  the most restrictive licence** (consumer-realist reading).
  **Operationalisation (proposed): a deterministic artefact-metadata
  harvester** — per paper, resolve declared artefact links via
  DataCite/Crossref/Zenodo/GitHub/OSF APIs into a small verified
  evidence pack pushed to scoring spawns with receipts. Keeps spawns
  network-free, holds evidence identical across runs (stability stays
  meaningful), replaces much rung-(ii) inference with fetched fact, and
  narrows the reference-configuration concordance confound.
  **Amendment 2 must re-specify the §4 read-scope rule:** paper + the
  evidence pack (enumerated endpoints); still no persisted-assessment
  reads.
- **#7 RULED:** the registered unscoreable→0 default applies only after
  the #2 ladder (including the evidence pack) is exhausted.
- **#6 RULED (Shawn, 2026-08-10):** the gradient proposal adopted — F1
  reads "a persistent identifier explicitly associated with the artefact"
  (own DOI, or the article DOI where the artefact is distributed as its
  supplement); F2/F3/F4 carry the granularity penalty. F-subtotal
  gradient within binary items: own-DOI deposit 4/4; supplement under
  the article DOI 1/4; unpublished 0/4. Stated explicitly in the
  instrument as a deliberate departure from the F-UJI-strict reading.
- **Harvester platform list is extensible by design** (Shawn,
  2026-08-10): start with DataCite/Crossref/Zenodo/GitHub/OSF; add
  platforms as encountered — Dataverse, the Australian Data Archive
  (ADA), and Figshare already flagged as likely early additions.
- **Publication stance (Shawn, 2026-08-10):** in early publications the
  approach and metrics are presented as *up for discussion*, not the
  last word. Two consequences: (a) iterate now during paper work —
  Sonnet-arm probe runs are cheap for testing rule variations where
  output is unsatisfying or uncertain (caveat from the benchmark:
  sonnet's within-arm stability is ~7 points below opus, so probes
  should be 3-run majority-voted, and gate-grade conclusions still need
  the registered configuration); (b) adjust in response to engagement
  once publishing begins, via the established dated-amendment path.

## Phase B — concordance-reference decision (Shawn + Claude)

The E8 reference scores are old-instrument, reproduction-informed; the
census lane is new-instrument, paper-only. Comparing across both axes is
incoherent and structurally caps concordance below the gate. Options
(Claude's preference order; Shawn decides with FAIR expertise):

- [x] 2026-08-15 **B1 (preferred). Re-derive reference scores** under the
      clarified instrument and census configuration, anchored by human
      adjudication (the preregistration's n=12 human-validation subsample
      can seed this); register the new set as an E8 update, retaining the
      old set. **RULED (Shawn, 2026-08-15) — B1 adopted with this shape:**
      - **Anchor — ruling-driven + targeted adjudication.** Start from the
        old E8 set; apply the ratified Entry 3 rulings item by item; Shawn
        adjudicates every changed item, all 68 A1-disputed items, and any
        item whose old score rests on reproduction-only evidence (a
        census-surface check runs across all 150 items: each reference
        score must be derivable from paper + receipt-covered evidence pack
        via the ratified two-rung ladder, unscoreable→0 only after the
        ladder); plus a spot-check sample of undisputed items. No API
        spend; no machine-derived reference (circularity declined).
      - **n=12 linkage — shared protocol, separate exercises.** One
        hand-scoring/adjudication protocol is written; the pilot
        re-derivation rehearses it now, and the census n=12 subsample runs
        it later exactly as registered (blinded, post-census). Amendment 2
        records that the pilot adjudication is unblinded (benchmark
        outputs seen) while the census subsample remains blinded.
      - **E8 — new set registered as v2, old set retained.** Per-item
        provenance (old score → ruling applied → adjudication note); the
        old set stays registered as historical; amendment 2 re-points the
        concordance gate at v2.
      Harvester findings feed the re-derivation: marwick's dead cited DOI
      (10.5281/zenodo.14561925 404s at DataCite and Zenodo), its
      three-licence conflict vs Zenodo's cc-by-4.0 (most-restrictive rule,
      per-artefact scope), and the CRAN endpoint-flagged gap.
- [ ] **B2. Redefine the concordance check** in amendment 2 to compare
      like-with-like another way. — Not taken (2026-08-15): B1 ruled.
- [ ] **B3. Keep the gate as-is** — advised against: a structurally
      unreachable gate measures nothing. — Not taken (2026-08-15): B1
      ruled.

## Phase C — harness hardening (pre-census register, runs in parallel)

Register of record: `wiki/planning/audit-2026-08-03-follow-ups.md`.

- [x] 2026-08-14 **C1. Audit fix round 2** — all register items closed
      (1, 2a, 3–8) across eight commits `f00d6dd`…`d2cb58a`; tests
      84 → 106, gate PASS throughout; item 2b (field-name confirmation)
      rides C2 by design. Includes the re-specified fallback-binding
      rule, the one fail-closed policy across both hooks, and the
      pre-commit test-suite gate (block-tested live). The S1
      index-vs-worktree residual manifested live the same day (a staged
      probe test leaked into `5618e30` while the worktree-reading gate
      saw green; removed in `d2cb58a`) — the residual is observed, not
      theoretical, and the pathspec discipline stands.
- [x] 2026-08-14 **C2. Capture one live SubagentStop event + operative
      demo** — three probes run (A: Agent-lane pass; B: workflow-lane
      transcript-borne pass; C: workflow-lane catch), operator-approved.
      Field names anchored (2b closed; workflow-lane events lack
      `last_assistant_message`); pass paths proven in both lanes; the
      catch fires correctly but its consequence is ABSENT in the
      workflow lane (block undelivered, output collected — pre-run audit
      B1's mechanism confirmed), so the workflow-lane gate is operative
      only once C9 lands. Diagnostic bonus: today's search + full
      validation over all 45 retained benchmark transcripts passes
      45/45 — the 39 benchmark blocks were transcript-write-lag false
      alarms and the benchmark's receipt provenance is now
      machine-verified. Annex:
      `studies/open-science-compliance/outputs/validation/c2-probes-2026-08-14/`.
- [x] 2026-08-14 **C3. Schema v1.1** — landed (`89f6706` + gate check):
      conditional ESCALATE requirements (C6), bounds + minLength (M12),
      soft A1 cross-reference honouring the instrument's ethical
      exception (rule re-verified against canon before encoding), M13
      naming note, `schema_version` const (S3), the ratified
      `input_provenance` flag, and `pack_refs` per the joint design note
      below. 20 defect-injection tests; the receipt gate now blocks
      mismatched schema_version claims. Supply mechanism: contract
      self-identification + E4/C7 registry hashes close the chain;
      workflow-side stop-stripping and run-record wiring ride C9/D3
      prep; the runtime-validator probe (S4) remains a D3-prep stop
      condition.
- [x] 2026-08-14 **C4. C7 GOVERNED decision (Shawn): RULED YES** — add
      `sha256:` content-integrity hashes to `shared_content` entries.
      Implementation rides the amendment 2 instrument edits (D1/D2
      window), so clarified text lands hash-checked from day one.
- [x] 2026-08-14 **C5. `unwrap-paste-file.py` M14–M16 fixes** with a
      self-check — done: indented items protected (M14), list numbers
      capped at 3 digits so year-sentences unwrap (M15), double-space
      collapse restricted to joined prose (M16);
      `tests/test_unwrap_paste.py` (audit N4's committed home) anchors
      each fix plus idempotence on the lodged amendment-1 artefact.
      Tests 130 → 139. Ready for amendment 2's paste artefact.
- [x] 2026-08-15 **C6. Artefact-metadata harvester** — built (`897959f` +
      GitLab fix in `5fdc172`): curated links registry (anchored to the
      pilots' extraction records) → five committed evidence packs, every
      record carrying retrieved_at + response_sha256; dedupe by
      record_id with declared_by merging; CC-URL canonicalisation;
      conflict flags (marwick's three asserted component licences vs
      Zenodo's single cc-by-4.0 fired; key's CC BY correctly cleared);
      CRAN recorded as an honest endpoint-flagged gap; marwick's cited
      10.5281/zenodo.14561925 404s at both DataCite and Zenodo — a
      dead-link finding for Phase B. Delivery mechanism decided:
      workflow-prompt injection with pack sha256 echoed in receipts,
      implemented with C9 wiring at D3 prep. **Platform-row entitlement
      verification done, dated 2026-08-15** (6/6 rows, 34 assertions,
      denominator disclosed):
      `studies/open-science-compliance/outputs/validation/platform-rows-2026-08-15/verification-note.md`
      — every row HOLDS WITH CAVEAT; the corrections (DataCite tombstone
      metadata contradiction; Zenodo licence-field scoping +
      default-licence artefact; non-uniform ADS/DANS/tDAR floors;
      GitLab no-SPDX/opt-in; Crossref persistence as member obligation;
      9.3M component DOIs) are **amendment-2 draft material — RULED
      2026-08-15, see decision log** (all §A rewrites accepted; row 4
      graded; all §B additions adopted; item 7 footnote with the
      operative-default principle; item 12 as amendment-2 methods
      commitment). tDAR/DANS bot-gating noted: scripted
      fetches get 403/challenge pages — future endpoint additions for
      those hosts need rendering + a challenge-page detector.
- [x] 2026-08-15 **C8 — implemented via `scripts/reconcile-run.py`**
      (`5fdc172`): per-spawn file-access lists derived from Read/Grep/
      Glob use+result pairs, contamination flagging (successful
      out-of-scope access fails; failed attempts and empty Globs warn),
      report + log-slice archival into run directories (audit S8).
      **Empirical §4 result: all 45 benchmark spawns show zero
      contaminating accesses** — isolation held; one warning-grade
      path-confusion case (dye/sonnet attempted the reference guides at
      a nonexistent user-level path, failed, honestly declared no
      pulls, and scored guideless — part of the §2-card guide-pull
      story). **Infeasible remainder per the 2026-08-14 ruling:**
      spawn-time path-scoped read enforcement (the harness permission
      model is repo-wide) — §4's "enforced by tool allowlist and
      sandbox scope" wording goes to the erratum-route text
      modification at D1 (allowlist + post-hoc verification +
      reconciliation gate is the real control). Original item text:
      **Implement amendment 1 §4's asserted isolation controls**
      (pre-run audit B4; registrant ruled 2026-08-14: implement, and
      where a control is infeasible, modify the registered text by
      erratum/amendment instead). The lodged §4 asserts enforcement by
      tool allowlist and sandbox scope, verification from the harness
      transcript, and per-run file-access lists archived with run
      artefacts — none of which the harness currently provides beyond
      the agent tool list. Build: derive each scoring spawn's complete
      file-access list from its transcript (the gate already parses
      transcripts), archive it with the run artefacts, and flag
      out-of-scope reads as a gate failure; mechanical log-slice
      archival into run directories (audit S8) rides this item. Any §4
      clause that cannot honestly be implemented is recorded in the
      erratum log for amendment 2 wording at D1.
- [x] 2026-08-15 **C9 — tool built, tested, and proven** (`5fdc172`,
      with `tests/test_reconcile.py`): receipt re-validation from
      completed transcripts (including the new attempts-are-not-reads
      rule, also landed in the live gate), divergence tripwire, exit-1
      hard stop. Proven on all retained runs: three benchmark arms
      45/45 clean; the C2 probe run correctly fails probe C — the
      output that was silently collected on 2026-08-14 can no longer
      survive reconciliation. **Remaining, explicitly at D3 prep:**
      wire the tool into `fair-benchmark-arm.workflow.js` as a
      per-item gate (plus schema push with sha256 receipts per the C6
      delivery decision). Original item text:
      **C9. Workflow-lane gate reconciliation** (C2 probes, 2026-08-14 —
      pre-census requirement; **the D3 re-benchmark must not run without
      it**). SubagentStop blocks are advisory in the workflow lane
      (probe C: block logged, never delivered to the agent, output
      collected anyway), and hook-time transcript lag produced all 39
      benchmark false-alarm blocks (45/45 transcripts re-validated clean
      post-hoc). Build: after each workflow `agent()` returns, look up
      the gate log by `agent_id`; anything but `pass` triggers
      authoritative post-hoc re-validation of the completed transcript
      (the C2 prototype); failed or unverifiable items are re-run or
      failed, never collected silently. Implements the adopted
      gate-events-vs-outputs divergence tripwire; wires into
      `fair-benchmark-arm.workflow.js` as part of D3 preparation.

### C3/C6 joint design note — evidence-pack record shape (2026-08-14)

Settled once in C3 (contract hardening 4); C6 conforms. A pack is one
JSON file per paper: `{paper_slug, harvested_at, endpoint_versions,
records: []}`. Each record carries `record_id`
("<endpoint>:<identifier>", stable within and across packs),
`source_endpoint` (from the ratified item-8 endpoint list), `url`,
`retrieved_at` (ISO 8601), `response_sha256` (the determinism anchor,
hardening 8), plus typed fields (licence, metadata record, conflict
flags under the most-restrictive rule). Scoring outputs cite records
via schema v1.1's optional `pack_refs` arrays. Packs are registered,
receipt-covered artefacts (audit S7); their delivery mechanism is C6's
first build task (audit B3). Validator-compat fallback (audit S4): if
the runtime validator rejects draft-07 conditionals at the D3-prep
probe, v1.1's conditional requirements move to C9's reconciliation
layer and the schema retreats to unconditional requireds — decided at
the probe, recorded by dated note here.

### Phase C pre-run review — hardened execution contract (2026-08-14)

Six-section `/pre-run-review` dialogue (operator: Shawn; sections 1–6
presented, probed, and approved 2026-08-14). Hardenings of record:

1. **Step 0 (DONE 2026-08-14):** amd-tower venv recreated; baseline
   suite green at 84/84 before any Phase C edit (matches `3b01676`).
2. **Ordering:** C1's logging fix precedes the C2 capture; C2's
   field-name confirmation closes C1 item 2; the pass-plus-catch demo
   runs only after all C1 hook fixes land. C3's supply mechanism and
   C6's receipt registration land after C1 (shared hook files). C5 is
   simultaneous-safe and slots anywhere.
3. **One-commit rule:** each fix lands with its regression test and its
   register tick in one commit; no red tests at commit boundaries.
4. **C3/C6 joint design note:** the evidence-pack record shape and the
   schema's pack-citation shape are settled once, inside C3; C6
   conforms. Schema v1.1 is designed against the ratified instrument
   (provenance flag included) so C6 does not force a v1.2 bump.
5. **Consolidated D1 governed-edit window (ADOPTED):** the gated
   agent-definition edits (output-contract wording, v1.1 pointer),
   guide pull→push promotion (A3), and C7 sha256 hashes land as ONE
   governed batch at D1, hash-checked from day one — not piecemeal.
   Interim v1.0-era definition wording is accepted as benign (no
   scoring spawns before D3).
6. **Registration compliance:** no scoring spawn receives an evidence
   pack before amendment 2 lodges (amendment 1 §4's read-scope governs
   until then). C2 probes are harness-test spawns: pack-free, output
   discarded, nothing persisted. Amendment 2 lodgement (D2) is a hard
   stop before the D3 re-benchmark, exactly as amendment 1 was for the
   first validation run.
7. **C2 spend gate:** up to three cheap probe spawns (capture; pass;
   catch), presented under the standing API review gate before running.
8. **C6 determinism:** every pack record carries retrieval timestamp
   and response-content hash ("evidence identical across runs" is
   checked, not hoped). Rate limits: wait or authenticate; never
   substitute a different endpoint mid-harvest (Shawn can supply a
   GitHub token — see continuity). Dead links or licence conflicts
   found in pilot papers are recorded findings feeding Phase B, never
   scored around.
9. **Layer-2 verification commitments:** C1 gets a fresh-context
   round-3 re-audit of the fix commits; C6 gets a cold re-fetch
   verifier that re-derives licence/metadata conclusions and diffs
   against the packs. Both report their denominator; a conflicting
   correction triggers a third derivation or operator adjudication,
   never verifier-wins.
10. **Anchors:** the captured SubagentStop event is committed as a
    dated annex (the anchor for all field-name claims); the
    platform-row entitlement note is dated and cites platform
    documentation URLs. Pack-staleness policy sentence queued for
    amendment 2 item 8 wording at D1.

Clean-context audit (proof of concept for extending `/pre-run-review`):
one Opus-class fresh-context agent audits this contract from the
committed artefacts after the operator dialogue — naive-reviewer
stance, denominator required, findings are claims not verdicts —
folded before the operator go/no-go.

**Audit outcome (2026-08-14):** the clean-context pass returned 4
blockers, 9 should-fixes, 5 notes (its denominator: 27 files opened,
16 contract claims checked, 27 command probes). All four blockers
CONFIRMED on adjudication — B1 extended by independent re-derivation:
the receipt gate blocked 39/45 benchmark spawns (opus 15/15, sonnet
15/15, fable 9/15) with every output still collected; the block
decision had no downstream consequence on any arm. Registrant rulings:

- **B4 → new item C8** (implement; text modification by
  erratum/amendment where a control is infeasible).
- **B1 → C2's finish line is a consequence-verified catch**, plus a new
  tripwire: gate events diverging from outputs-collected halts any run.
  C2 probe budget revised to up to four cheap spawns (capture +
  three-case demo).
- **B2 → register item 1 re-specified** (well-formed-payload search
  order; the contradictory wording struck in place).
- **B3 → C6 gains an early delivery-architecture design task**:
  per-spawn pack delivery + receipting (candidate mechanisms: workflow
  prompt injection with sha256 echoed in receipts, or per-spawn
  push-hook context) — settled at C6's start, not inside the D1 window.

Disposition table approved in full. Folded into the register: S1
(pytest in pre-commit + documented index/worktree residual), S2
(three-case demo), S3 (schema identity receipted; workflow stops
stripping `version`), S4 (standard keywords + validator probe + new
stop condition), N1 (item 2 split 2a/2b), N4 (self-check at
`tests/test_unwrap_paste.py`), N5 (preflight flag unification).
Recorded here as contract amendments: **S5** — the pre-lodgement fence
generalises to ALL amendment-2-derived content, and C2 probes score a
synthetic fixture, never a corpus paper, so the committed annex carries
no real scores; **S7** — the harvester script and its packs are
registered in the manifest with checks; **S8** — log-slice archival
rides C8; **S9** — the operative demo is the compensating control for
D5's substring routing evidence (checker enhancement noted as future
work, not Phase C scope); **N2** — the D1 governed-edit window executes
on a branch + PR; **N3** — packs live outside `studies/` and
`outputs/`, and the benchmark workflow file is registered in the
manifest.

## Phase D — amendment 2, re-benchmark, then the registered ladder

- [x] 2026-08-15 **D1-prep. Repository-evaluation enrichment pass**
      (RULED 2026-08-15, rides the row-4 grading) — DONE same day
      (`506125c`): CoreTrustSeal register queried via its GraphQL
      backend (the public register SPA returns an empty shell to
      scripted fetches — item-12 failure class confirmed live) +
      five re3data records; raw evidence archived with checksums.
      Headlines: ADS certified to 2027-02-12 (renewal chain); DANS
      Data Station Archaeology certified to 2028-02-27; **tDAR lapsed
      2025-12-16, renewal at First Submit**; **Zenodo absent from all
      556 certification requests** (never applied); CRAN pidSystem
      none at the registry layer. re3data's certificate field diverges
      from the CTS register on every certified row — certification
      must be cited at the service. Addendum:
      `studies/open-science-compliance/outputs/validation/platform-rows-2026-08-15/enrichment-addendum-2026-08-15.md`. Principle (Shawn, from eResearch
      practice): **evaluate at the infrastructure layer, where all
      lodged artefacts inherit the platform's characteristics; spend
      artefact-level investigation only where the infrastructure is
      silent.** Repositories are assessed once; the table is the
      instrument's memory of that assessment and is built out over
      time (Dataverse, ADA, Figshare, Dryad flagged).
- [x] 2026-08-15 **D1. Consolidate amendment 2** — EXECUTED as the
      governed-edit window on branch `feat/d1-amendment-2-window`
      (four commits: instrument v2.1 + mirror + manifest; A3 guide
      promotion + agent definitions v1.1; C7 hashes + gate + hook
      byte-verification; amendment-2 draft + erratum-log execution
      note). The consolidated draft
      (`studies/open-science-compliance/prereg/amendment-2-draft.md`)
      carries: instrument clarifications (items 1–9 + corrected platform
      table), §2 evidence-pack/read-scope re-specification superseding
      amendment 1 §4 (with pack-staleness rule + harvester-integrity
      commitment), §3 E8-v2 reference re-derivation (Phase B shape as
      ruled), §4 re-validation design + restated remediation ladder,
      §5 delivery/receipts spec, §6 escaped-comparator fixes, and the
      D2 pre-lodgement checklist. **Awaiting the registrant's read +
      branch merge; then D2.**
- [ ] **D2. Lodge** via the proven OSF API route (versioned registration
      update; DOI unchanged).
- [ ] **D3. Re-benchmark** on the clarified instrument, schema v1.1, and
      fixed harness — same design (3 arms × 5 papers × 3 runs = 45 spawns,
      ≈ $27 API-equivalent at benchmark rates), harness
      `studies/open-science-compliance/protocol/validation/fair-benchmark-arm.workflow.js`.
      Standing API review gate presented before the run.
- [ ] **D4. Gates → selection → census.** Pass: cheapest eligible arm,
      registered regression gate, census. Still below: majority-vote
      consequence, now with a defensible claim that the residual is
      irreducible; arm choice recorded explicitly.

## Decision log

| Date | Decision | By |
|---|---|---|
| 2026-08-03 | Routing-fix card declined as candidate stood; instrument-clarification route (path 3) adopted; robust-instrument goal overrides speed-to-census | Shawn |
| 2026-08-03 | Phase B to draw on Shawn's FAIR expertise; plan externalised to this file | Shawn |
| 2026-08-10 | Working position, decision point #1: assessment target = the research surface (empirical status, fault-free); ruling deferred to the verified prior-art scout report | Shawn |
| 2026-08-10 | Provenance flag accepted: per-input author-deposited / third-party / undeterminable metadata, never affecting scores; upstream-attributable failures become findings | Shawn |
| 2026-08-10 | Aggregation rule: reasonable initial choice, then iterate; instrument refinement declared an explicit research goal for the study's expansion | Shawn |
| 2026-08-10 | Amendment 2 names the assessment-object definition the **research-surface rule** (framing endorsed) | Shawn |
| 2026-08-10 | **Decision point #1 RULED:** research-surface rule adopted as drafted (baseline to iterate from); #8 merged into #1; ACM v1.1 recorded as the named deliberate departure | Shawn |
| 2026-08-10 | prior-art-scout agent definition amended: every direct quotation must be emitted as a verifiable claim (personal-assistant `a3f5793`) | Shawn |
| 2026-08-11 | Ratification-read fixes to Entry 3: item-1 clause restored; ladder consolidated to two rungs — rung (i) direct evidence (paper + evidence pack), rung (ii) by-construction table; entitlements are floors, not ceilings | Shawn |
| 2026-08-11 | R1.1 conflict rule scoped per artefact: clean paper/dataset/software licence divisions score separately; most-restrictive applies only to same-artefact disagreements (in-document supplements; paper-vs-service assertions) | Shawn |
| 2026-08-11 | Endpoint list and platform table maintained independently; GitLab added to endpoints; CRAN + Dryad flagged as early endpoint additions; row-entitlement verification queued at C6 | Shawn |
| 2026-08-11 | Supplement table row qualified: applies only to supplements served from the article landing page with no independent deposit; repository-hosted supplements (Figshare, Dryad) score as platform deposits; Dryad added to flagged table additions | Shawn |
| 2026-08-14 | Erratum-log Entry 3 + queued amendment 2 scope RATIFIED (end-to-end read, as amended through 2026-08-11) — A2 closed; D1 consolidation unblocked pending the Phase B shape decision and A3 | Shawn |
| 2026-08-14 | C7 RULED YES: sha256 content-integrity hashes on `shared_content` entries, implementation riding the amendment 2 instrument edits; Phase B shape discussion scheduled as a focused session before D1 | Shawn |
| 2026-08-14 | Phase C pre-run review (six-section dialogue) approved: hardened contract recorded in Phase C; consolidated D1 governed-edit window adopted; C2 probes gated and pack-free; amendment 2 lodgement confirmed as hard stop before D3, not before Phase C | Shawn |
| 2026-08-14 | Clean-context audit (Opus PoC) adjudicated: all 4 blockers confirmed, B1 extended (39/45 spawns blocked with no downstream consequence); B4 ruled IMPLEMENT → new item C8, with erratum-route text modification where infeasible; B1 consequence-verified catch confirmed; disposition table approved in full | Shawn |
| 2026-08-14 | C2 probes run (3 sonnet spawns, approved): field names anchored, pass paths proven both lanes, workflow-lane block consequence ABSENT → new pre-census item C9 (gate reconciliation, blocks D3); benchmark receipts retroactively machine-verified 45/45 — the 39 blocks were transcript-lag false alarms | Claude (probes approved by Shawn) |
| 2026-08-14 | C3 schema v1.1 landed with the A1 cross-reference soft-enforced (named exception rationale) rather than hard-zeroed — faithful to canon's ethical-restriction exception; pack record shape settled in the C3/C6 joint design note | Claude (per ratified instrument text) |
| 2026-08-15 | C6 built and run: five evidence packs committed; conflict detector proven live (marwick fired, key cleared after canonicalisation); dead cited DOI (zenodo.14561925) recorded for Phase B; GitHub token adopted (fine-grained, public read-only) | Claude (build); Shawn (token) |
| 2026-08-15 | C8+C9 built as one reconciliation tool; benchmark retro-reconciled 45/45 clean with zero contaminating accesses (§4 isolation empirically held); attempts-are-not-reads rule added to gate and reconciler; workflow wiring deferred to D3 prep | Claude |
| 2026-08-15 | Platform-row verification note committed (6/6 rows, every verdict HOLDS WITH CAVEAT; DataCite tombstone sub-assertion contradicted; Zenodo/DANS default-licence artefact) — corrections queued as amendment-2 draft material for the registrant's D1 ruling | Claude (findings); Shawn (ruling pending) |
| 2026-08-15 | **Phase B shape RULED — B1 adopted:** anchor = ruling-driven re-derivation + targeted adjudication (changed items, all 68 A1-disputed items, census-surface check across all 150, spot-check of undisputed items; no machine-derived reference); n=12 linkage = shared protocol, separate exercises (pilot rehearsal unblinded and recorded as such; census subsample blinded as registered); E8 = new set registered as v2 with per-item provenance, old set retained, concordance gate re-pointed at v2 in amendment 2. D1 now blocked only on A3 and the platform-table rulings | Shawn |
| 2026-08-15 | **Platform-table corrections RULED:** §A rewrites 1/2/4/5 accepted as drafted (DataCite tombstone; Zenodo licence-field scoped to open records; GitLab no-SPDX/opt-in split from GitHub; Crossref persistence = member obligation + right, not warranty); row 4 graded within one row — ADS keeps R1.3-by-construction, DANS and tDAR require rung-(i) evidence (dye data R1.3 flip unaffected: dye's deposit is ADS, DOI 10.5284/1018290); §B additions 6/8/9/10/11/13 all adopted incl. the Zenodo persistence strengthening; item 7 = footnote on Zenodo+DANS rows; item 12 = amendment-2 methods commitment (rendering + challenge-page detection), implementation at D3 prep | Shawn |
| 2026-08-15 | **Operative-default principle (item 7 footnote wording):** a default-valued licence is fully operative even where author choice is doubtful — the instrument assesses the research surface, not intent; the footnote records the empirical default-domination (82.6% Zenodo CC-BY-4.0; DANS CC0) as interpretive context only, never a score modifier | Shawn |
| 2026-08-15 | **Infrastructure-layer evaluation principle + table build-out endorsed** (from Shawn's eResearch practice): evaluate at the infrastructure layer, where all lodged artefacts inherit platform characteristics; artefact-level investigation only where the infrastructure is silent; repositories assessed once, so enrich rows with CoreTrustSeal + re3data evidence and build the table out over time → new item D1-prep | Shawn |
| 2026-08-15 | **A3 + D1 governed-edit window EXECUTED** on branch `feat/d1-amendment-2-window` (per the adopted one-batch contract): instrument v2.1 with ratified clarifications + corrected platform table (mirror byte-synced); guide v1.1 aligned + promoted pull→push; agent definitions v1.1 (diff-verified variants); C7 sha256 hashes registered, gate-required, and push-hook byte-verified; amendment-2 draft consolidated. Gate PASS 66/66, tests 207 green throughout. Awaiting registrant read + merge, then D2 lodgement (hard stop before D3) | Claude (build); Shawn (read pending) |
| 2026-08-15 | **Identifier-recovery rule adopted** (amendment 2 §2): where a declared DOI/PID fails to resolve, attempt a bounded recovery — one registrar-API search (DataCite/Crossref) by title + author, one search of the named repository — before recording a dead link; recovered records enter the pack flagged `recovered` (query recorded), never silently substituted for the cited identifier; the citation defect stays reportable as a finding. No heroic efforts — the analogue of the reproduction lane's minimal documented code corrections. Harvester implementation rides D3 prep (before the next pack harvest); marwick's dead zenodo.14561925 is the precedent case | Shawn |
