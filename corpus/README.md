# Corpus management — entry point

**Established:** 2026-07-24, per `wiki/planning/corpus-management-plan.md` v0.2.1
(decisions confirmed by Shawn 2026-07-24). **Principle: never redistribute
third-party content, regardless of licence** — no article PDF, supplement, or
derived full text ever enters git.

## Architecture

Third-party materials live in an **out-of-tree store**; git holds only the
citable *manifests* (metadata + hashes) and this documentation. The store
location is deliberately outside the repository so that no gitignore pattern,
Large File Storage (LFS) rule, or future reorganisation can sweep publisher
content into public history — a hard requirement since the Open Science
Framework (OSF) registration pins commit hashes that any history rewrite would
invalidate.

```text
~/corpora/llm-reproducibility/<slug>/    # the store (CORPUS_ROOT)
  vor.pdf  preprint.pdf  supplement-*.pdf  extracted.txt  processed*.md  meta.json
```

- `CORPUS_ROOT` resolution: the `corpus_root` key in each manifest, overridable
  by the `CORPUS_ROOT` environment variable.
- `corpus/store` is a gitignored convenience symlink to the store (safe even if
  accidentally committed — git stores the path string, never the content).
- `meta.json` files are **machine-generated** from the manifest by
  `scripts/fetch-corpus.py gen-meta` — never hand-edited.

## Manifests (the citable corpus record)

| Manifest | Covers |
|---|---|
| [`development-manifest.yaml`](development-manifest.yaml) | 11 pre-study papers (pipeline development corpus) |
| [`../studies/open-science-compliance/corpus/manifest.yaml`](../studies/open-science-compliance/corpus/manifest.yaml) | Study corpus: 5 Phase 1 pilots; Phase 2 census entries appended at acquisition |

Manifests are the stable record (what the corpus *is*); each study's
`queue.yaml` remains workflow state (what has been *done*). One schema
(`corpus-manifest/1.0`), any number of manifests.

## Rebuilding the corpus

```bash
# Verify local holdings against manifest hashes
python3 scripts/fetch-corpus.py verify --manifest corpus/development-manifest.yaml

# Fetch missing open-access items via Unpaywall (email required for politeness)
python3 scripts/fetch-corpus.py fetch --manifest <manifest> --email <you@example.org>

# List closed items needing manual acquisition (with source URLs)
python3 scripts/fetch-corpus.py report --manifest <manifest>
```

A fresh clone plus `fetch` rebuilds the open-access portion of the corpus on
any machine; `report` tells you exactly what must be obtained manually (or via
the Elsevier text-and-data-mining route, if institutional entitlement is
confirmed — corpus plan decision 5).

## Provenance and sync

- Every extraction records its source file and sha256 in `extraction.json`
  (schema v2.7+); reproduction runs record URL + sha256 of anything fetched
  mid-run in that run's `log.md`.
- Second copy: `scripts/sync-corpus.sh` rsyncs the store to the QNAP array on
  rpi-server (mount-verified before writing). **No automated schedule exists
  yet** — run it after each acquisition session.
