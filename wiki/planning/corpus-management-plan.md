# Corpus management plan: articles, supplements, and third-party materials

**Version:** 0.2
**Date:** 2026-07-23 (v0.1: 2026-07-13)
**Status:** Agreed direction (Shawn, 2026-07-13); implementation SCOPED 2026-07-23
(repo audit + build order + target structure below, §Implementation scope) —
execution on hold pending Shawn's confirmation of decisions 1 and 3 and his
routing-design v0.2 review. Sequenced as pre-Phase-1 infrastructure for the agentic
modernisation plan (the JAS census and corpus-screener need the manifest this plan
creates).
**Origin:** The 2026-07-13 open-access audit and history purge. A publisher supplement
(dye-et-al-2023) entered public git history because a third-party file landed under a
*tracked* output directory and the blanket `*.pdf` LFS rule swept it in; the extracted
text of a closed-access article (marwick-2025) had the same problem, compounded by
`source: null` extraction metadata that forced forensic reconstruction of its origin.
Both were purged via `git filter-repo` (2026-07-13). At census scale this failure mode
recurs unless the design changes.

## Principle

**Never redistribute third-party content, regardless of licence.** Once nothing
third-party is ever in git, open-access checking stops being a compliance gate and
becomes optional metadata recorded once. The default is safe by construction; safety
must not depend on files landing in the correctly gitignored directory.

## 1. Corpus store (outside the repository tree)

A single store, e.g. `~/corpora/llm-reproducibility/<slug>/`, holding per paper:
`vor.pdf`, `preprint.pdf`, `supplement-*.pdf`, `extracted.txt`, and `meta.json`.
All third-party material lives ONLY here — including extracted full text, which is
derivative of the article and carries its copyright. Being outside the tree beats
gitignore: there is no pattern to get wrong. The pipeline locates it via a single
`CORPUS_ROOT` configuration value (or transitional symlinks from the current
gitignored paths: `studies/*/corpus/pdfs/`, `input/sources/`).

## 2. Manifest in git (the citable, shareable corpus)

Extend the existing queue.yaml or add `corpus/manifest.yaml`: per paper — DOI,
bibliographic basics, open-access status and licence (recorded once, informational),
source URLs (version of record, preprint, supplements, datasets), sha256 of each
retrieved file, and retrieval date. Pair with `scripts/fetch-corpus.py`:

- resolves each DOI via Unpaywall and downloads the best open-access copy;
- verifies stored hashes on every fetch;
- lists closed items requiring manual acquisition (with their URLs).

This dissolves the "partial corpora" problem in the sense that matters: the public
manifest is always complete; the local store is complete; third parties can rebuild
the open-access portion with one command and know exactly what to obtain manually.

**Provenance rule:** every extraction records its source file and hash in
extraction.json (the marwick `source: null` gap must not recur).

## 3. What stays in git

Original research data only: extraction.json graphs, scores and verdicts, assessment
outputs, reproduction code, Dockerfiles, logs, comparison reports, and generated
figures. Short location-anchored quotations inside extraction.json are fine
(quotation/fair dealing); derived full text is not, and lives in the store.

## 4. Reproduction runs (fetch-with-checksum — endorsed by Shawn 2026-07-13)

Anything an agent downloads mid-run — publisher supplements, datasets from CDNs —
goes to the corpus store or run scratch, never under `outputs/`, with the URL and
sha256 recorded in the run's `log.md`. Wherever inputs are accessible in open
repositories (Zenodo, OSF, journal data links), the Dockerfile or run script
**fetches with checksum verification at build/run time rather than vendoring the
file** — good reproduction practice independent of licensing, and the preferred
default. Vendor into the store only what cannot be re-fetched reliably.
The reproduction-assessor skill/prompts need a corresponding update.

## 5. Deterministic guardrails (gates, not vigilance)

- **Narrow the blanket LFS rule:** `.gitattributes` `*.pdf filter=lfs` scoped to
  own-artefact directories only (e.g. `**/reproduction/**/outputs/`, `docs/`), so a
  stray third-party PDF cannot be swept into history by the pattern.
- **Pre-commit hook extension** (the filename-convention hook already exists): block
  any newly added `.pdf`/`.txt` outside a whitelist without an explicit override.
  This makes the supplement incident structurally impossible — the working-notes
  Obs 4 point (deterministic gates over agent/human assertions) applied to licensing.

## 6. Cross-machine sync (out of git)

Canonical copy of the store on rpi-server (verify drives mounted before writing, per
network guardrails) with an rsync pull script. This matters less than it sounds: the
fetch script regenerates the open-access majority on any machine from the manifest;
only closed/manually acquired items truly need syncing. Include the store in the
normal backup regime.

## Alternatives considered (and passed on)

- **DataLad / git-annex:** the principled heavyweight solution; real operational load
  for a solo project; revisit only if collaborators need versioned blob access.
- **Zotero storage as the store:** attractive given existing infrastructure, but
  attachment-key paths make pipeline access awkward. Keep Zotero as the bibliographic
  layer and the store as the blob layer, joined by DOI.

## Implementation scope (v0.2, 2026-07-23)

Repo audited against this plan (session of 2026-07-23). **Already in place:** the
gitignore pattern layer (both `corpus/pdfs/` paths, `input/sources/`, extracted-text
patterns, reproduction supplements); every tracked `.pdf`/`.txt` verified to be an
own-artefact; queue.yaml carries rich per-paper metadata to seed the manifest.
**Missing — all six substantive pieces:** no store; no manifest; no fetch script;
the blanket `*.pdf` Large File Storage (LFS) rule is still in force; the pre-commit
hook gates filenames only; no source-provenance fields in the extraction schema.
**Migration inventory:** 11 PDFs in `input/sources/original-pdf/` (41 MB,
publisher-named files to be renamed to slugs), 6 PDFs in the study corpus dir
(27 MB, five pilots + marwick preprint), plus untracked extracted texts in output
dirs.

**Registration-integrity rationale (new since v0.1):** the OSF registration pins
commit `ee3fda3` / tag `osf-prereg-phase2-2026-07-20`. Any future third-party-content
purge would rewrite history and invalidate the hashes the public registration cites —
so "never need a purge again" is now a hard requirement, which the out-of-tree store
satisfies by construction.

**Target structure:**

```text
~/corpora/llm-reproducibility/            # the store, out of tree
  <slug>/                                 # flat, one dir per paper slug
    vor.pdf  preprint.pdf  supplement-*.pdf  extracted.txt  meta.json

repo:
  corpus/
    README.md                             # entry point: architecture, CORPUS_ROOT,
                                          # fetch recipe, index of all manifests
    development-manifest.yaml             # the 11 pre-study papers
    store -> ~/corpora/llm-reproducibility  # gitignored convenience symlink
                                          # (safe even if committed: git stores the
                                          # path string, never the content)
  studies/open-science-compliance/corpus/
    manifest.yaml                         # 5 pilots now; census entries appended
    queue.yaml                            # unchanged — workflow state, churns
  scripts/fetch-corpus.py                 # --manifest <path>; one schema, any manifest
```

Principle: **manifest = stable citable record of a corpus; queue = workflow state** —
side by side per study, never merged. Store stays flat by slug (slugs are
project-unique), so `CORPUS_ROOT/<slug>/` resolves without knowing the study.

**Build order and effort** (items 1–4 are census blockers; 5–8 trail; ≈1 day total;
no Large Language Model (LLM) API spend — Unpaywall/CrossRef are free public APIs):

| # | Work item | Effort |
|---|---|---|
| 1 | Create store; migrate all 17 papers (PDFs + extracted texts + `meta.json` stubs); transitional symlinks; verify pipeline paths | ~1 h |
| 2 | Manifest schema + populate all holdings (sha256 everything; metadata from queue.yaml/CrossRef) | ~1–2 h |
| 3 | `fetch-corpus.py` (Unpaywall resolution, checksum verify, closed-item report) | ~half day |
| 4 | Narrow LFS to own-artefact dirs; pre-commit gate on new PDF/txt outside whitelist | ~30 min |
| 5 | reproduction-assessor prompt updates (fetch-with-checksum default; store/scratch destinations; log URL+hash) — §8 implementation change, rides the post-build regression gate | ~1 h |
| 6 | Additive schema bump v2.6→v2.7: `source_file` + `source_sha256` in extraction metadata | ~30 min |
| 7 | rsync script to rpi-server (drive-mount check per network guardrails) + backups | ~30 min |
| 8 | CLAUDE.md PDF-handling update + cross-references | ~15 min |

**Decision log (2026-07-23):**

1. Store location in-repo vs out-of-tree — discussed; recommendation **out-of-tree**
   (registration-integrity argument above; public repo; clones can never be complete
   anyway), with the manifest + fetch script providing one-command rebuild and the
   gitignored symlink providing in-tree ergonomics. *Awaiting Shawn's confirmation.*
2. Path mechanism — **AGREED (Shawn):** `corpus_root` key in manifest + env-var
   override + transitional symlinks from the old gitignored paths, retired after the
   census tooling is proven.
3. Manifest home — recommendation **study-scoped manifests** beside each study's
   queue, plus root `corpus/README.md` as the index (structure above). *Awaiting
   Shawn's confirmation.*
4. Timing — **HOLD (Shawn, 2026-07-23):** execution waits on his routing-design v0.2
   review.

## Implementation checklist (v0.1, superseded by the scoped build order above)

1. Create the store; move existing PDFs/extracted texts from
   `studies/*/corpus/pdfs/`, `input/sources/`, and outputs dirs; add symlinks or
   `CORPUS_ROOT` config; confirm pipeline paths still resolve.
2. Write manifest schema + populate from queue.yaml and existing holdings (hashes).
3. Write `fetch-corpus.py` (Unpaywall resolution, checksum verify, closed-item list).
4. Narrow `.gitattributes` LFS scope; extend the pre-commit hook.
5. Update reproduction-assessor prompts: store/scratch destinations;
   fetch-with-checksum default; log URL+hash.
6. Add source-file+hash fields to extraction metadata (schema note).
7. Sync: rsync script to rpi-server; add store to backups.
8. Update CLAUDE.md (PDF handling section) and the modernisation plan cross-reference.

Estimated effort: manifest + fetch script ≈ half a day of agent work; migration and
guardrails smaller. Must land before the JAS census acquires papers at scale.
