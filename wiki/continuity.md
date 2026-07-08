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
- **Scout sweep COMPLETE (2026-07-08):** whole-stack positioning vs state of the
  art — 12 verified reports + synthesis in `wiki/planning/scout-reports/`
  (start at `2026-07-08-stack-positioning-synthesis.md`). Headline: our
  combination is unclaimed in every lane; HASS/archaeology empty across all six.
  Follow-up queue lives in synthesis §7 (incl. lit-scout author-rendering patch,
  deeper-chaining go/no-gos, Zotero imports).
- **Cosmos application:** proposal draft v0.2 in
  `wiki/planning/cosmos-application-draft.md` awaiting Shawn's read; remaining
  fields (title, one-liner, self-pitch, grant amount) undrafted; OSF
  preregistration recommended before submission (draft on request).
- **Current gates:** Phase 1 of the agentic modernisation plan
  (`wiki/planning/agentic-modernisation-plan.md`, now v0.3) remains ON HOLD —
  the 2026-07-07 guided walkthrough recorded six judgement calls in plan §9;
  Shawn's verdicts on those unlock Phase 1. OSF preregistration must precede
  FAIR scoring of any new JAS papers (Option A ordering constraint, plan §6);
  preregistration drafting is independent of the Phase 1 hold and would
  strengthen the Cosmos application (plan §9 item 6).
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
