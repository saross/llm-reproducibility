---
title: "llm-reproducibility — Continuity (Living Doc)"
tags: [infrastructure, coding-practices]
created: 2026-06-07
updated: 2026-07-18
status: active
---

# llm-reproducibility — Continuity (Living Doc)

**Purpose:** cross-session state, pending work, and a session-by-session log
for this repo. Updated in place at session end (no new file per session).

**Status: ACTIVE** (promoted from seed 2026-07-06). The four-artefact wiki
layout is fully in place (migration completed 2026-07-03, task B below):
continuity, working-notes, reflections/, user-observations, claude-observations,
and planning/ all live under `wiki/`; `docs/` stays at repo root as product
documentation (decided 2026-07-03). This file was created 2026-06-07 as the
migration seed, from a session working primarily in the
`2026-mq-llm-dh-judgement-paper-b` repo (the matching-grade PDF extractor
merged here as PR #1).

**How to update at session end** (per the canonical convention —
`~/personal-assistant/global-claude-md/handoff-protocol.md`):

1. Mark done items in place: `[ ]` → `[x] YYYY-MM-DD`; never delete.
2. Add new items as `[ ]` with a brief note.
3. Append a new "Session log" entry at the bottom (most recent first).
4. Carry forward open questions.

---

## Repo state (2026-07-18)

- `main` current through 2026-07-15 @ `885e664` (history rewritten 2026-07-13 —
  pre-purge hashes are stale). Earlier landmarks: plan v0.3 review,
  Cosmos form capture + proposal draft v0.2, article-text untracking, and the
  scout-report series). Project v3.0.1.
- **Scout sweep COMPLETE (2026-07-08), all follow-ups executed:** whole-stack
  positioning (12 verified reports + synthesis), arXiv blind-spot sweeps (S1/S2),
  approved deeper chaining (C1–C3), and the OSF/grey-literature guard pass (G1)
  all live in `wiki/planning/scout-reports/` (start at the synthesis; README
  indexes everything). Headlines: no direct competitor to any lane, but the
  middle is converging (Chakravorti 2026; Zhu 2026 pair) — speed-to-publish now
  matters; the zero-archaeology null is DOCUMENTED (G1, 26-query log) so
  first-mover claims must be scoped + "to our knowledge" with Spennemann 2023
  demarcated; Zotero staging holds all verified finds (P1–P6, S1–S2, chains).
  lit-scout + verifier agents patched (author-count rule; arXiv handling).
- **Cosmos application:** proposal draft v0.4 (2026-07-21, academic-prose pass)
  in `wiki/planning/cosmos-application-draft.md` — body 499/500 aligned with the
  lodged registration (already-preregistered + osf.io/dqnhg, control series,
  pilot error-detection, window 2022–2026); field 19 extended (human-validation
  link, agent-relay audit line, delivery-and-follow-on paragraph: Claude/Codex
  skills + self-hostable runner with Brian Ballsun-Stanton, FAIR4RS, CC0 data
  outputs, follow-on API-cost driver); field 18 Brian entry (affiliation line
  pending); candidates drafted for title/one-liner/self-pitch/amount (worked
  US$8,000). Awaiting Shawn's manual edit + field selection. Pre-submission
  gates: lift OSF embargo (journal check 2026-07-21: no candidate venue
  requires double-blind — JAS/JAS:R single-anonymised, JAS:R dropped
  double-blind since mid-2024, JCAA author's choice), verify URL + DOI resolve.
  Deadline 26 Jul 2026. (v0.3 was `7435865`, body 482/500.)
- **OSF preregistration DRAFTED + STRESS-TESTED (2026-07-14/15):**
  `studies/open-science-compliance/protocol/phase-2-preregistration-draft.md`
  v0.2 (`885e664`; v0.1 `9405182`). Open-ended registration format; honours all
  three drafting-care constraints (instrument fixed, regression-gated pipeline
  changes, no-new-corpus-contact). /review-implementation revisions: H2
  de-circularised (verification-target coverage endpoint, exact
  Jonckheere–Terpstra primary, fractional-logit secondary), H1 restricted to
  quantitative papers (post-treatment conditioning argument) with
  trend-adjusted secondary, **JAS: Reports DiD control arm (Shawn approved
  2026-07-14** — FAIR lane; reproduction = exploratory stretch; AER absence
  grounded in Marwick 2025, re-verify guidelines pre-launch), H4 reworded to
  match its test, assessment-before-reproduction blinding, 0.90 stability
  threshold, human-validation subsample (n=12), power table. **v0.7
  LODGEMENT-READY at `ee3fda3` (2026-07-18)** — all resolutions applied plus
  four review-batch revisions (see the 2026-07-18 session log entry);
  lodgement materials in `studies/open-science-compliance/prereg/` (plain
  summary, two glyph-verified PDFs, README with recipe + checklist).
  **LODGED 2026-07-20: <https://osf.io/dqnhg/>** — by hand from the project
  flow (standalone Registries flow caps form attachments at five files; the
  project flow froze all six artefacts from OSF Storage); **EMBARGOED at
  lodgement** (Shawn 2026-07-21: deliberate deviation from the no-embargo
  plan — some journals require author anonymity for double-blind review;
  lift once the target journal is chosen, and before Cosmos submission so
  the linked URL resolves; journal policy check for JAS / JAS:R / JCAA
  delegated 2026-07-21; note the lodgement tag's annotation still says "no
  embargo" — predates the correction); tag `osf-prereg-phase2-2026-07-20`;
  paste files unwrapped to flowing lines (OSF text boxes render line-breaks
  literally). Known cosmetic defect: §10 power table pasted as run-together
  pipe text — accepted, fix rides with any future amendment (tables rule
  now in prereg README + convention memory). The URL will NOT resolve
  publicly until the embargo lifts. Option A ordering satisfied:
  new-corpus FAIR scoring is unblocked. Live URL linked from the Cosmos draft (body now reads "already
  preregistered", census window corrected 2023→2022, 484/500 words).
- **Current gates:** the §9 verdicts are DELIVERED (2026-07-15/16), so the
  Phase 1 hold on the agentic modernisation plan
  (`wiki/planning/agentic-modernisation-plan.md`, v0.3) is now gated only on
  (a) review of the content-routing design (below) and (b) the
  corpus-management-plan implementation (pre-Phase-1 prerequisite). ~~OSF
  preregistration must precede FAIR scoring of any new JAS papers (Option A
  ordering constraint, plan §6).~~ [x] 2026-07-20 SATISFIED — registration
  lodged (<https://osf.io/dqnhg/>).
- **Agent content-routing design v0.1 WRITTEN (2026-07-15, `10947aa`):**
  `wiki/planning/agent-content-routing-design.md` — resolves plan §9 item 3
  with a three-way routing rule (embed role behaviour / push instruments
  verbatim with read receipts / pull pattern libraries; silent-vs-loud
  failure as the routing criterion). Read receipts decided by Shawn
  (reliability-first, duplication acceptable if cleanly split;
  no-agent-to-agent-duplication rule; shared_content registry folds into
  manifest.yaml). Queued: `/review-implementation` + prior-art-scout passes
  against it (Shawn wants both) → v0.2 before Phase 1 build.
- **Framework paper QUEUED (2026-07-13):** plan externalised to
  `wiki/planning/long-tail-credibility-framework-paper.md` (v0.1) — a
  state-of-play/agenda paper staking out long-tail research credibility
  assessment with AI, built on the verified scout sweeps. Prioritisation
  deferred until Shawn finishes his current paper (week of 2026-07-13); open
  question is authorship model (solo lit-review-and-state-of-play — his
  current lean — vs consortium via COS/CWTS Leiden/RDA contacts).
- **Deferred watch list (from chain reports C1/C3):** re-check forward citers
  of Chakravorti et al. 2026 (10.48550/arXiv.2605.27394) and the
  ReplicatorBench cluster around Sep–Oct 2026; Cheng & Khoo 2025
  (10.31083/ko44513) and Bolanos-Burgos et al. 2026 (10.7717/peerj-cs.3921)
  around Oct 2026–Jan 2027. Sources: c1/c3 reports' deeper-chaining sections.
- **Working notes WRITTEN (2026-07-13):** Obs 5 (prompt-injection sightings)
  and Obs 6 (verifier catch taxonomy) in `wiki/working-notes.md` (`f51737b`).
  The gap Obs 5 flagged — no standing anti-injection rule in the scout agent
  definitions — was closed the same day (personal-assistant `b31342b`,
  injection-defence rule added to all four scout agents' Constraints).
- ~~**§9 verdicts: Shawn has committed (2026-07-13)** to delivering the six
  judgement-call verdicts~~ [x] 2026-07-15/16 ALL DELIVERED: items 1–2 =
  prereg Decision 7 (reliability checks + 0.90 threshold, confirmed); item 3
  = content-routing design (sign-off pending the review passes); items 4–5
  accepted (R-A+R-B merge; drift clause as encoded in prereg §8); item 6
  realised by the prereg draft itself.
- **HISTORY PURGE COMPLETE (2026-07-13, pushed by Shawn; remote verified
  clean):** git filter-repo removed the dye-et-al-2023 supplement.pdf (both
  historical paths) and marwick-2025.txt from all 242 commits; local
  untracked copies intact; full pre-purge backup (mirror, LFS objects, plain
  files, commit-map) at
  `~/Code/repo-backups/llm-reproducibility-pre-purge-20260713/`.
  Residual notes: (1) commit hashes cited in wiki/docs before 2026-07-13 are
  stale — translate via the backed-up commit-map or search by commit
  subject; (2) GitHub's server-side LFS storage may retain the unreferenced
  supplement object — full scrub needs a GitHub Support ticket or repo
  delete/recreate (low urgency: nothing references it); (3) other local
  clones must be re-cloned or hard-reset. The CC BY SocArXiv preprint of
  Marwick 2025 is at
  `studies/open-science-compliance/corpus/pdfs/marwick-2025-socarxiv-preprint.pdf`
  (gitignored dir) for future licence-clean extraction.
- **Corpus management redesign AGREED (2026-07-13), implementation queued:**
  `wiki/planning/corpus-management-plan.md` — out-of-tree corpus store, DOI
  manifest + fetch-with-checksum script (Shawn endorsed fetch-with-checksum
  as the reproduction-run default), LFS/pre-commit guardrails, rpi-server
  sync. Sequenced as a PRE-PHASE-1 prerequisite in the agentic modernisation
  plan; must land before the JAS census acquires papers at scale.
- **OA check RESOLVED (2026-07-13):** six of eight
  papers are CC BY 4.0 — no purge needed (ballsun-stanton-et-al-2018,
  penske-et-al-2023, sobotkova-et-al-2016 [OA book], sobotkova-et-al-2024
  [Emerald page confirms CC BY despite Unpaywall "bronze"], crema-et-al-2024,
  key-et-al-2024). ~~PENDING~~ [x] 2026-07-13 both actions COMPLETED (see
  HISTORY PURGE COMPLETE above); original scoping notes retained: (1) `git filter-repo` purge of
  dye-et-al-2023's `reproduction/attempt-01/supplement.pdf` — publisher
  (Elsevier) supplement to a green-only article, no open licence; NOTE it
  was tracked via Git LFS, so the purge must remove the LFS object as well
  as the pointer; history rewrite of the public repo awaits Shawn's go.
  (2) `marwick-2025.txt` near-certainly from the closed VoR: the on-disk
  source PDF (studies/open-science-compliance/corpus/pdfs/marwick-2025.pdf)
  IS the Elsevier JAS version of record (first-page check 2026-07-13) and no
  preprint PDF is present — joins the purge list pending Shawn's one-word
  confirmation. LOCAL COPIES CONFIRMED before any purge (Shawn's
  requirement, 2026-07-13): dye supplement intact on disk (820,582 bytes,
  real PDF, not an LFS pointer) and marwick text + VoR PDF both on disk.
  Purge scoping: the dye supplement exists at TWO historical paths
  (pre-reorg `outputs/dye-et-al-2023/...` and the current `studies/...`
  path) — filter by basename/blob, not one path — and the LFS object must
  be removed too. History audit of all ever-tracked PDFs found one other
  publisher PDF (Sobotkova et al. 2023, old `sources/PDF/` path) — checked:
  Applied Geography, 10.1016/j.apgeog.2023.102967, hybrid OA, CC BY →
  CLEAR, no purge. The corpus PDFs and `input/sources/original-pdf/` were
  never tracked; all currently tracked PDFs are the project's own artefacts
  (reproduction figures; a draft proposal). Side-fix applied:
  key-et-al-2024's DOI in the corpus queue corrected to the resolving
  2023-prefix form (recorded 2024-prefix form 404s; verified at CrossRef).
- **Identity confabulation CORRECTED (2026-07-14, `38adf36`):** CITATION.cff,
  codemeta.json, CONTRIBUTING.md, and the pilot findings report had carried
  "Shawn Graham" / Carleton University / github.com/shawngraham since their
  2025-11-13 creation. Now Shawn Ross / Macquarie University /
  github.com/saross, ORCID 0000-0002-6492-9025 (verified against author lines
  in Shawn's published papers). archive/ and verbatim extracted texts left
  untouched (the sobotkova-et-al-2016 mention is the real Shawn Graham).
- **Machine sync COMPLETE (2026-07-15):** amd-tower ready for resume. Old
  pre-purge clone quarantined (NOT deleted) at
  `~/Code/repo-backups/llm-reproducibility-pre-purge-clone-20260715` on
  amd-tower — never pull/push from it (pre-purge history; also holds on-disk
  copies of the purged files, consistent with keep-local-copies). Fresh clone
  at `~/Code/llm-reproducibility`: purged paths absent from history (verified
  0 hits), pre-commit hooks installed, 30 gitignored corpus/text assets
  rsynced from zbook with all checksums verified (incl. dye supplement
  820,582 bytes; marwick CC BY preprint). Gotchas: amd-tower remote is now
  **HTTPS + gh credentials** (its GitHub SSH key needs an interactive agent;
  `git remote set-url origin git@github.com:saross/llm-reproducibility.git`
  to switch back); venv not recreated (`python -m venv venv &&
  venv/bin/pip install -r requirements.txt` when scripts are needed);
  `.claude/settings.local.json` deliberately not copied (machine-local).
- **Immediate priority (displaces the above):** draft the Cosmos Institute
  grant application (deadline 26 Jul 2026); framing in
  `wiki/planning/cosmos-grant-application-framing.md`.
- Stale-carry-forward note for future resumes: the 2026-07-06 handoff
  verdicts were already applied in `a1e52de` — do not re-solicit them.

### Earlier state (2026-06-07)

- `main` @ `1c4650e` (merge of PR #1). Working tree clean.
- **PR #1** added a matching-grade extraction layer to
  `extraction-system/scripts/pdf_processing/`: `normalise_for_matching`,
  `normalise_text_readable`, `PDFExtractor.extract_pages` (per-page text with
  page-index + section locators), and promoted cleaners (`strip_running_headers`,
  `drop_fragment_headings`, `split_body_references`, `strip_affiliation_tail`,
  `looks_like_heading`). First tests in the repo at
  `extraction-system/scripts/pdf_processing/tests/test_matching_layer.py`
  (24/24 pass). Additive/opt-in: existing `extract()` behaviour unchanged.
  Built for an annotated-bibliography (AB+) pipeline in the paper-b project;
  design context in that repo's
  `planning/pdf-extractor-consolidation-plan-2026-06-07.md`.

## Pending tasks

### A. Git hygiene — untrack the committed virtualenv  [x] 2026-07-03

> Done 2026-07-03 exactly as prescribed below: 2,114 index deletions, files kept
> on disk; post-check `git ls-files | grep -c '^venv/'` = 0; stray-bytecode sweep
> outside venv = 0 tracked files.

The repo tracks the **entire `venv/`** — **2,114 files** (verified 2026-06-07:
`git ls-files | grep -c '^venv/'`), including thousands of `.pyc`. `.gitignore`
**already** lists `venv/`, `__pycache__/`, and `*.py[cod]` (lines ~5–10), so
these were force-added or pre-date the ignore (tracked files are not
auto-ignored).

Fix (own commit/PR — large, mechanical):

```bash
git rm -r --cached venv
git commit -m "chore: untrack committed virtualenv (already in .gitignore)"
```

Caveats:

- ~2,114 deletions from the index (files stay on disk). Do it standalone.
- Anyone relying on the committed venv must recreate it:
  `python -m venv venv && venv/bin/pip install -r requirements.txt` — note this
  in the commit body and/or README.
- After: `git ls-files | grep -c '^venv/'` should be `0`.
- Also sweep any other tracked bytecode outside venv:
  `git ls-files | grep -E '__pycache__|\.pyc$' | grep -v '^venv/'` (should be
  empty — PR #1 already removed the one stray
  `extraction-system/scripts/pdf_processing/__pycache__/pdf_cleaner.cpython-312.pyc`).

### B. Migrate docs to the wiki-style layout  [x] 2026-07-03

> Done 2026-07-03. `docs/notes/working-notes.md` → `wiki/working-notes.md`;
> `docs/notes/reflections/` → `wiki/reflections/`; repo-root `planning/` →
> `wiki/planning/` (all via `git mv`); created `wiki/index.md`,
> `wiki/user-observations.md`, `wiki/claude-observations.md`; wiki frontmatter
> merged into migrated pages (additive — `/reflect`'s priority/scope/audience
> keys preserved); reference sweep across all living docs (archive/ and frozen
> reproduction artefacts deliberately untouched); CLAUDE.md continuity pointer
> added; README gained a docs-vs-wiki disambiguation map. **docs/ disposition
> decided (Shawn, 2026-07-03): stays at repo root** — product documentation
> follows the GitHub/JOSS convention (Pages builds from /docs); only the
> process layer moved to wiki/.

This repo uses the **legacy `docs/notes/` layout** and lacks `continuity.md`
(this seed) and `user-observations.md`. Target = the canonical per-project
wiki layout (authoritative reference: `~/personal-assistant/wiki/index.md`,
"PA project layer" table; migration precedent:
`~/personal-assistant/wiki/planning/wiki-index-draft.md`).

| Artefact | Target | Source now |
|---|---|---|
| `continuity.md` | `wiki/continuity.md` | **this file (seed, in place)** |
| `index.md` | `wiki/index.md` | new (small index; model on PA's) |
| `working-notes.md` | `wiki/working-notes.md` | `docs/notes/working-notes.md` |
| `reflections/` | `wiki/reflections/` | `docs/notes/reflections/*` (session-log, session-reflection, abductive-reasoning, llm-observations) |
| `user-observations.md` | `wiki/user-observations.md` | new (model on paper-b's `docs/notes/user-observations.md`) |
| `planning/` | `wiki/planning/` | repo-root `planning/` |
| Documentation | decide: keep `docs/` vs `wiki/docs/` | repo-root `docs/` |

Steps:

1. `git mv` legacy files into `wiki/` (preserve history).
2. Create `wiki/index.md` + `wiki/user-observations.md` from the convention.
3. Add wiki frontmatter (`title`/`tags`/`created`/`updated`/`status`) to
   migrated pages; tags from the 24-term vocabulary in PA's `wiki/index.md`.
4. Add a "Session continuity → `wiki/continuity.md`" pointer to this repo's
   `CLAUDE.md` (belt-and-braces; the global session-start protocol already
   reads `wiki/continuity.md`).
5. Resolve the `docs/` disposition (see open decision).

Caveats:

- `docs/` here is large and public-facing (assessment guides, background
  research, FAIR docs) — unlike PA's, it may warrant staying at repo root
  rather than moving under `wiki/docs/`. Decide deliberately.
- `/reflect`, `/observe`, `/handoff` are layout-aware and fall back to legacy
  paths; after migration they target `wiki/`.

### C. Fix lossy de-hyphenation of genuine compounds  [x] 2026-07-06

> Done 2026-07-06, following the fix direction below with one refinement: the
> dictionary check takes precedence over the affix list (if the joined form is
> a known closed-form word, join — so `multi-\nple` → `multiple` even though
> `multi-` is a compound prefix; otherwise a compound prefix keeps its hyphen —
> `self-\ncorrection` → `self-correction`). Dictionary = frozen subset of
> wamerican 2020.12.07-2 shipped at
> `extraction-system/scripts/pdf_processing/affix-joined-words.txt` (9,810
> affix-prefixed words) so canonical matching keys stay machine-independent.
> Chained breaks handled (dict check sees the flattened fragment:
> `multi-\nfa-\nceted` → `multifaceted`). Idempotence preserved; golden tests
> green; 8 regression tests added incl. the Huang self-correction case
> (32/32 pass). Residual ambiguity documented in the `_dehyphenate` docstring:
> a deliberate hyphen broken at exactly that hyphen resolves to the closed
> form when that form is a dictionary word; non-prefix compounds
> (`decision-\nmaking`) keep the historical joining behaviour.

`_dehyphenate` (`extraction-system/scripts/pdf_processing/pdf_cleaner.py:348-361`,
regex `re.sub(r"(?:-\s*\n\s*)+([a-z])", r"\1", text)`) joins any end-of-line
hyphen followed by a **lowercase** letter and **drops the hyphen
unconditionally**. This is correct for line-break artefacts
(`archaeo-\nlogy` → `archaeology`) but **lossy for genuinely-hyphenated
compounds broken before a lowercase letter** — e.g. `self-\ncorrection` →
`selfcorrection` (hyphen lost). The existing guard only protects compounds
broken before a **capital** (`well-\nKnown` stays). Feeds **both**
`normalise_for_matching` and `normalise_text_readable`.

Concrete case (re-verifiable): Huang et al. 2023 (Zotero attachment
`K294C8KD`), `page_index 3`, "...after self-\ncorrection, the accuracies..." →
the matching key contains `selfcorrection`, so a naturally-written quote
("after self-correction, ...") **fails** the deterministic quote-checker even
though the content is present. Discovered 2026-06-10 during the paper-b AB+
co-design (`planning/section2-grounding/ab-plus/huang2023large.md`, "Extraction /
fidelity notes").

Impact: a quote spanning a line-broken hyphenated compound silently fails the
checker; paper-b currently works around it (quote from text-as-extracted +
display-cleanup) but the canonical key itself is wrong here.

Fix direction (heuristic — full de-hyphenation is ambiguous): keep the hyphen
when the prefix is a known hyphenating affix (`self-`, `multi-`, `non-`, `pre-`,
`co-`, `anti-`, `inter-`, `intra-`, `well-`, `re-`, `e-`, …) or when **both**
fragments are independently valid words (wordlist check); drop it otherwise.
Must preserve `_dehyphenate`'s **idempotence** (the readable + matching
normalisers depend on it) and keep golden tests green; add a regression test
for the `self-correction` case. Additive/worktree discipline.

### D. Consolidate version-history sources  [ ]

Version history is now maintained by hand in four places (`manifest.yaml`
`version_history` — nominally canonical; `CHANGELOG.md`; README "Development
History"; `docs/research-assessor-guide/version.md`). The 2026-07-06 session
updated three of them in parallel to say the same thing. Candidate fix: derive
the CHANGELOG and README sections from the manifest (script or documented
cascade checklist, mirroring the assessment-schema compliance pattern from
February). Low priority; logged from llm-observations 2026-07-06.

## Open decisions

- [x] 2026-07-03 `docs/` disposition: **stays at repo root** (decided with the
  conventions rationale recorded in task B note above and README's docs-vs-wiki map).
- [x] 2026-07-03 Sequencing: done as separate commits (A on 2026-07-03 standalone;
  B as its own migration commit).

## Session log

### 2026-07-18 — Prereg v0.3→v0.7 lodgement-ready; OSF materials; authorship posture

Shawn returned (Paper B finished on the train) and final-reviewed the prereg
through four revision batches; everything committed and pushed; lodgement is
the morning of 2026-07-19. Version chain (all 2026-07-18):

- **v0.3** — nine decision-point resolutions applied (D3 → 168 h on named
  hardware + archived-intermediates partial path; others as drafted).
- **v0.4** — census window start → 2022-01-01 (two full pre-policy years;
  H1b parallel trends partially checkable; power table recomputed, δ ≈ 0.28
  at 80/80); H5 + credibility lane reclassified pre-specified exploratory;
  *Reports* control census option via cost gate.
- **v0.5** — credibility outputs constrained to descriptive structural
  metrics; availability taxonomy → six friction-ordered levels (machine
  boundary L2/L3, discretion boundary L3/L4; "on request" split from
  archive registration; standardised L4 request protocol); sampling-cap gate
  clause; pre-specified descriptive reporting block; R-only limitation
  sharpened (Marwick-adjacent oversampling caveat).
- **v0.6** — H5 gains two schema-verified RDMAP metrics (implicit-status
  proportion; expected-information gaps); L4 window → 3 weeks + late-response
  clause; credibility signals computable internally with aggregate-only
  reporting (per-paper scores never published); FAIR4RS named as
  amendment-path extension; FAIR×coverage estimation added; human-validation
  wording fixed (one instrument, data + code applications).
- **v0.7 + pilot report v1.2** — LLM removed from authorship per
  journal/university policy: report has sole human author + §10 LLM-use
  statement (v1.0–v1.1 correction recorded in-document); CITATION.cff and
  codemeta author fields cleaned (tooling disclosure retained in
  runtimePlatform/softwareRequirements); git Co-Authored-By trailers stay
  (Shawn confirmed — VCS provenance, not scholarly authorship).

Lodgement materials (`studies/open-science-compliance/prereg/`, convention
transferred from `~/Code/inscriptions/wiki/prereg/`): plain-prose summary
(4,347 words, emphasis stripped to fixpoint), glyph-verified PDFs of prereg +
pilot report (DejaVu fonts — Latin Modern silently dropped α/δ/≤; verified by
pdftotext), README with regeneration recipe + lodgement checklist. Study
protocol and Pass 6 prompt upload as markdown only (✅/❌ glyphs drop silently
under xelatex). Upload set: 4 canonical .md + 2 PDFs at `ee3fda3`; commit
hash goes in the OSF project description; tag `osf-prereg-phase2-<date>`
after submission. OSF approach memorised (memory `2026-07-18-10b38c994a0a`);
Quarto-workflow discussion captured to PA inbox for a future session.

**NEXT:** (1) lodge on OSF (morning 2026-07-19; checklist in prereg README);
(2) Cosmos application remaining fields + link the live registration
(deadline 26 Jul); (3) weekend run: FAIR reliability spot-check + pilot
regression gate (pilot papers only — prereg-safe before and after lodgement);
(4) routing-design review passes (/review-implementation + prior-art-scout);
(5) corpus-management implementation before census.

**Held over pending Shawn's verdicts (no silent discard):** working-notes
candidates WN-a (xelatex silently drops out-of-font glyphs — meaning-inversion
hazard for instruments; verify builds by text extraction) and WN-b
(markdown-emphasis stripping needs fixpoint iteration — nested/line-wrapped
spans survive one pass); user-obs candidates 1–4 in
`wiki/user-observations.md` (pending review).

### 2026-07-15/16 — All prereg decision points resolved; content-routing design v0.1

amd-tower resume session, closed for machine swap to the laptop (train). All nine
preregistration decision points resolved with Shawn:

- **D1** sole registrant + LLM disclosure in Summary §8. **D2** cutoff 2026-06-30,
  **D4** 15–25 band, **D5** per-hypothesis families (Holm only within H1a's pair),
  **D6** availability taxonomy, **D8** *Reports* 120/60, **D9** n = 12 — all confirmed
  as drafted.
- **D3 REVISED:** compute cap raised 48 h → **168 h wall-clock on named reference
  hardware**, with the archived-intermediates/table-regeneration partial path written
  into §5 criterion 4 (over-cap papers scoped down via archived posteriors, not
  excluded). Rationale: ad-hoc drops would systematically exclude Bayesian/MCMC papers
  — exactly H4's stochastic side.
- **D7** reliability checks + 0.90 threshold confirmed (= §9 items 1–2).
- Verdict-capture caveat: D3, D7, and §9 items 4–5 arrived via rejected
  AskUserQuestion dialogs (provisional but consistent; D7 twice) — reconfirm wording
  when applying the draft edits.

§9 verdicts thereby all delivered (see repo-state bullet). Item 3 resolved by the new
`wiki/planning/agent-content-routing-design.md` v0.1 (`10947aa`): embed role behaviour
/ push instruments with read receipts / pull pattern libraries. Shawn's design brief:
reliability first, duplication acceptable if split cleanly; read receipts definitely
in. Discussion en route covered pull-miss risk calibration (low per-call, silent,
non-trivial at census scale; stability checks don't catch a consistently-wrong scorer
— the n = 12 human subsample does).

**NEXT ACTIONS (laptop):** (1) apply D1–D9 resolutions to the prereg draft and close
its decision table; (2) run `/review-implementation` + prior-art-scout against the
routing design → v0.2; (3) lodge prereg on OSF; (4) Cosmos remaining fields (deadline
26 Jul); (5) corpus-management implementation before census. PA data synced for the
swap (data `38b78d3`, pointer `183d5e0`). Interaction lesson recorded in the PA
scratchpad: don't pair substantive prose with an AskUserQuestion dialog in one turn —
the prose may not render.

### 2026-07-14/15 — Prereg drafted + stress-tested to v0.2; identity fix; amd-tower sync

One-day session on zbook, closed for machine switch to amd-tower. Phase 2 OSF
preregistration drafted (v0.1 `9405182`) then stress-tested via
`/review-implementation` and revised to v0.2 (`885e664`) — see the repo-state
bullet for the full change list; nine decision points open. Author-identity
confabulation corrected across public metadata and living docs (`38adf36`).
amd-tower brought into sync (quarantine + fresh clone + verified asset rsync;
repo-state bullet has gotchas). Also: prereg v0.1 commit `9405182` includes the
seven-decision table later superseded by v0.2's nine.
~~**Held over pending Shawn's verdicts (no silent discard):**~~ [x] 2026-07-15
all verdicts returned same session: WN-a and WN-b both ACCEPTED (now
Observations 7–8 in `wiki/working-notes.md`); user-obs candidates 1–3 all
ACCEPTED (pending marker cleared). Follow-on question from Shawn: is
`/review-implementation` fit for purpose for study-design reviews, or does it
need a checklist update? Assessment delivered 2026-07-15: protocol phases
generalise; a "Study Designs and Preregistrations" domain checklist is the
gap (circularity, criterion contamination, post-treatment conditioning,
wording-vs-test match, counterfactual presence, pre-specification
completeness, blinding, instrument validation, power-as-estimation) —
APPLIED 2026-07-15 to the canonical skill (personal-assistant `5b76a87`,
`skills/review-implementation/SKILL.md`; live everywhere via the
sync-symlinks convention — canonical skills in personal-assistant
`skills/`, symlinked into `~/.claude/skills/` by
`scripts/sync-symlinks.sh`; amd-tower gets it on next pull/cron sync).

### 2026-07-07/14 — Verified stack sweep, Cosmos evidence, licence purge, corpus plan

Eight-day conversation (compaction 2026-07-08; two usage-limit interruptions).
Full detail in `wiki/reflections/session-log.md` (2026-07-07/14 entry); highlights:
19 verified scout reports + synthesis (P1–P6, S1–S2, C1–C3, G1) with the
speed-to-publish competitor finding; eleven Zotero staging collections; three
scout-agent patches (author gating, arXiv handling, injection defence); Cosmos
draft v0.3 + field-19 evidence pack; framework-paper and corpus-management plans
externalised; working notes Obs 5–6; OA audit → `git filter-repo` purge of two
copyrighted files (Shawn pushed; remote verified clean; backup + commit-map at
`~/Code/repo-backups/llm-reproducibility-pre-purge-20260713/`); Marwick CC BY
preprint downloaded. Held-over gates: none new — queue is Paper B → OSF prereg →
§9 verdicts → corpus implementation → Phase 1. No unreviewed working-note
candidates (Obs 5–6 written and pushed).

### 2026-07-03/06 — Revival: modernisation plan, wiki migration, tasks A-C closed

Project revived after the February pause (one conversation spanning four days,
Shawn intermittently AFK). Three parallel explorers mapped repo state: the JAS
pilot is COMPLETE (5/5 papers, 4 SUCCESSFUL / 1 PARTIAL reproductions; headline
finding: data availability, not code availability, predicts reproduction
outcome). Wrote the agentic modernisation plan and took two structural
decisions with Shawn: **study shape Option A** (OSF preregistration first →
JAS 2023-2026 FAIR census as sampling frame → preregistered confirmatory
reproduction subset) and **docs/ stays at repo root** (wiki/ = process record;
convention promoted to the PA template in a parallel session). Executed the
wiki-layout migration (task B), untracked the committed venv (task A), fixed
lossy de-hyphenation with a frozen-dictionary heuristic (task C; 32/32 tests),
reconciled all stale metadata to v3.0.1, and refreshed README/CHANGELOG.
**Phase 1 build of the modernisation plan is ON HOLD by explicit instruction**
until Shawn reviews the plan. Gotcha for future revivals: the local clone was 8
commits behind origin at session start — fetch before characterising repo state.

- Commits: `11f5734` (metadata reconciliation), `bab66ce` (modernisation plan),
  `5440d12` (venv untrack), `8845a45` (wiki migration), `245d820` (task C fix),
  `3c7313c` (README/CHANGELOG refresh), plus session-close commits
- Key docs: `wiki/planning/agentic-modernisation-plan.md` (v0.2, Option A
  recorded in §6); `extraction-system/scripts/pdf_processing/affix-joined-words.txt`
  (frozen dictionary, regeneration command in header)
- Memories saved: study shape (2026-07-04-856141514e0f), repo-layout convention
  (2026-07-04-e6d2685b35b4), build-on-hold (2026-07-04-f24eccedb145)
- Handoff verdicts (Shawn, 2026-07-06): both working-notes candidates ACCEPTED
  (now Observations 3-4 in `wiki/working-notes.md`); user-obs candidate 1
  accepted, candidates 2-4 discarded. Nothing held over.

### 2026-07-05 — Cosmos grant application framing externalised

From a personal-assistant hub session (cross-repo candidate evaluation deliberately run
there, not here). Decision: this repo is the basis for the Cosmos Institute grant
application (AI x Truth-seeking track, deadline 26 Jul 2026). Full record — grant facts,
portfolio proximity scan (186 grantees, no overlap; Metalens is complementary), pitch
framing (reproduction + FAIR lanes with a sampled human-verification surface; extraction/
credibility lanes as frame and track record, not deliverable), and a brainstorm-grade
budget section — in `wiki/planning/cosmos-grant-application-framing.md`. Also indexed the
agentic modernisation plan + the new doc in `wiki/planning/README.md` (the former was
missing from the index).

### 2026-06-10 — de-hyphenation defect logged (task C)

From a paper-b AB+ co-design session (no code changes to this repo). Building
the first AB+ entry surfaced a lossy-de-hyphenation defect in `_dehyphenate`:
genuinely-hyphenated compounds broken across a line before a lowercase letter
(e.g. `self-\ncorrection`) lose their hyphen in the canonical matching key,
breaking otherwise-valid quote checks. Logged as **pending task C** with a
re-verifiable concrete case and a fix direction. Shawn asked for this to be
recorded here for a proper fix later; paper-b proceeds with the
quote-from-extracted-text + display-cleanup workaround for now.

### 2026-06-07 — seed created

Created this `wiki/continuity.md` as the seed of the wiki migration, from a
session centred on the paper-b repo (matching-grade PDF extractor, merged here
as **PR #1**, `1c4650e`; 24/24 tests; validated on real PDFs). Logged the two
pending infrastructure tasks: untrack the committed `venv/` (2,114 files) and
migrate docs to the wiki layout. No other changes to this repo in that session
beyond PR #1.
