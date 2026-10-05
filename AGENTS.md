# Project: llm-reproducibility

Codex entry point. Shared project policy lives in
[docs/agent-guidance.md](docs/agent-guidance.md); edit that file when policy
changes, and keep this entry point limited to Codex mechanisms.

## Session start

Run `git fetch origin` first and report ahead/behind against the fetched
`origin/main` using `git rev-list --left-right --count origin/main...HEAD`
(behind, then ahead). Then read `docs/agent-guidance.md` **in full** and follow
it, followed by `wiki/continuity.md` for current state. A link here is an
instruction to read the shared file, not evidence that it has been loaded.

## Codex mechanisms

- **File reads:** shell output can be truncated by `max_output_tokens`, and
  commands such as `head` or `sed -n` show only part of a file. Read existing
  files completely before editing; use consecutive, bounded reads for large
  files and check for truncation. Prefer targeted patches, and never rebuild
  a file from an incomplete tool response. Apply the shared guidance's
  post-write validation to extraction outputs.
- **Extraction, assessment, and reproduction:** use the canonical workflows,
  prompts, queues, and schemas linked from the shared guidance. Claude's
  skills, agent definitions, and workflow tools are not automatically
  available in Codex; do not assume equivalent tools are installed or treat
  a harness substitution as an approved research procedure.
- **Paper reading:** use the available PDF skill and page rendering to
  preserve the visual context required by the shared guidance.

## Commits in this lane

Git hooks are disabled in the admitted Codex clone. Before **every commit**,
read the current gates in `scripts/install-git-hooks.sh` and check the staged
changes explicitly against them and the shared guidance. Do not run the
installer without checking its compatibility with the lane admission.

- Stage explicit paths, inspect `git diff --cached`, and check filename,
  corpus-content, credential, and ownership prohibitions. A disabled hook
  does not waive a prohibition.
- Run the manifest-consistency gate:
  `python3 scripts/check-manifest-consistency.py --quiet`.
- Run the test-suite gate with `venv/bin/python -m pytest tests/ -q` when
  that environment has pytest; otherwise use
  `python3 -m unittest discover -s tests`.
- Run applicable lint checks and `git diff --cached --check`. Resolve failed
  gates before committing, and report checks that could not run.
- Fetch again and verify the branch is zero commits behind `origin/main`
  before committing and pushing. Keep review work on its pull-request branch.
