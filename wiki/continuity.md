---
title: "llm-reproducibility — Continuity (Living Doc)"
tags: [infrastructure, coding-practices]
created: 2026-06-07
updated: 2026-07-07
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

## Repo state (2026-07-08)

- `main` current through the 2026-07-07/08 session's commits (plan v0.3 review,
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
- **Cosmos application:** proposal draft v0.3 committed (`7435865`) in
  `wiki/planning/cosmos-application-draft.md` (body 482/500 words; field 19
  evidence pack + bibliography drafted; guard-pass null folded in). Remaining
  fields: title, one-liner, self-pitch, grant amount. Deadline 26 Jul 2026.
- **OSF preregistration CONFIRMED (2026-07-13):** Shawn will draft/lodge it
  as the next task after finishing Paper B (this week). It precedes any
  new-corpus FAIR scoring (Option A ordering) and should be linked live from
  the Cosmos application. Content largely exists (H1–H5, pilot findings
  report §7; drafting-care notes in the cosmos draft's prereg section).
- **Current gates:** Phase 1 of the agentic modernisation plan
  (`wiki/planning/agentic-modernisation-plan.md`, now v0.3) remains ON HOLD —
  the 2026-07-07 guided walkthrough recorded six judgement calls in plan §9;
  Shawn's verdicts on those unlock Phase 1. OSF preregistration must precede
  FAIR scoring of any new JAS papers (Option A ordering constraint, plan §6);
  preregistration drafting is independent of the Phase 1 hold and would
  strengthen the Cosmos application (plan §9 item 6).
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
- **§9 verdicts: Shawn has committed (2026-07-13)** to delivering the six
  judgement-call verdicts (agentic modernisation plan v0.3 §9) that unlock
  Phase 1; captured to the personal-assistant inbox; sequenced after Paper B
  and the OSF preregistration.
- **OA check RESOLVED (2026-07-13), two actions pending:** six of eight
  papers are CC BY 4.0 — no purge needed (ballsun-stanton-et-al-2018,
  penske-et-al-2023, sobotkova-et-al-2016 [OA book], sobotkova-et-al-2024
  [Emerald page confirms CC BY despite Unpaywall "bronze"], crema-et-al-2024,
  key-et-al-2024). PENDING: (1) `git filter-repo` purge of
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
