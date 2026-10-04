#!/usr/bin/env python3
"""Build the D3 benchmark workflow's args deterministically (audit F15/F17).

**Version:** 1.4

The clean-context audit (2026-08-17) found nothing binding the S4 probe's
schema decision — or anything else — to the arm invocations: args were
ad hoc. This launcher makes the args a single derived artefact:

- `agentType` is derived from the arm (never typed independently — the
  workflow additionally asserts the binding, audit F17);
- papers are enumerated from the E8 registry order with corpus-store
  `vor.pdf` paths, existence-checked;
- each paper's evidence pack path + sha256 are computed from the committed
  pack bytes at build time (the workflow injects them; the reconciler
  re-verifies them);
- the structured-output schema is loaded from its manifest-registered file
  (`assessment.schemas.benchmark_fair_output`), so a stale or wrong schema
  cannot be handed to an arm without the manifest saying so. If the S4
  probe forces the named retreat (conditionals → reconciliation layer),
  the schema file changes under governance and this builder picks it up.

v1.2 (effort pinning, 2026-08-17): reasoning effort was session-inherited
and attestation-only through the D3 cycle. The launcher now requires
``--effort`` and embeds it in the args (the workflow passes it in the
scoring spawns' opts AND states it in every scoring prompt, so it becomes
artefact-derived from the transcripts), and embeds ``launch_commit`` — the
repository HEAD at build time. Building from a tree with modified tracked
files is refused outright (no bypass flag): args built from uncommitted
instrument, schema, pack, or manifest edits would carry an unreproducible
vintage. Commit first, then build.

v1.3 (re-run support, 2026-08-17): optional ``--items slug:run,...`` embeds
an items list restricting the workflow (v1.6+) to declared
contract-mandated re-run items; slugs are validated against the registry
and runs against 1-3.

Usage:
    venv/bin/python scripts/build-benchmark-args.py <arm> --effort LEVEL \\
        [--items slug:run,slug:run] [--out FILE]

    <arm> ∈ {sonnet-5, opus-5, fable-5, opus-5-5}
    LEVEL ∈ {low, medium, high, xhigh, max}

Output: the args JSON for Workflow({scriptPath, args}) on stdout (or FILE).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
CORPUS_STORE = Path.home() / "corpora" / "llm-reproducibility"
# opus-5-5 (v1.4, 2026-10-04): the Opus 5.5 validation arm, added when the
# registrant held D4 selection to validate claude-opus-5-5 through the same
# gates (gates-ruling-2026-10-04/ruling.md). Its agent definition is
# registered in manifest.yaml like the three registered arms.
ARMS = ("sonnet-5", "opus-5", "fable-5", "opus-5-5")
EFFORT_LEVELS = ("low", "medium", "high", "xhigh", "max")


def resolve_launch_commit(repo_root: Path) -> str:
    """HEAD commit hash, refusing a tree with modified tracked files.

    Untracked files (porcelain ``??`` lines) are ignored: they cannot alter
    the build's inputs, which are all tracked (manifest, schema, packs).
    Modified or staged tracked files mean the args would embed a commit hash
    that does not describe the bytes actually used — refuse, no bypass.

    Inherited ``GIT_*`` variables are scrubbed (2026-10-03): git exports
    ``GIT_DIR`` and ``GIT_INDEX_FILE`` to hook processes, and in a linked
    worktree they are absolute, so ``git -C <repo_root>`` would silently
    inspect the hook's repository instead of ``repo_root``. That blocked
    every commit from a worktree (the pre-commit test gate ran this against
    the wrong tree) and could misreport cleanliness when run from a hook.

    Raises:
        RuntimeError: if tracked files are modified/staged, or git fails.
    """
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    status = subprocess.run(
        ["git", "-C", str(repo_root), "status", "--porcelain"],
        capture_output=True, text=True, timeout=30, env=env)
    if status.returncode != 0:
        raise RuntimeError(f"git status failed: {status.stderr.strip()}")
    dirty = [line for line in status.stdout.splitlines()
             if line and not line.startswith("??")]
    if dirty:
        raise RuntimeError(
            "tracked files modified — commit before building args "
            f"(launch_commit must describe the bytes used): {dirty}")
    head = subprocess.run(
        ["git", "-C", str(repo_root), "rev-parse", "HEAD"],
        capture_output=True, text=True, timeout=30, env=env)
    if head.returncode != 0:
        raise RuntimeError(f"git rev-parse failed: {head.stderr.strip()}")
    return head.stdout.strip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("arm", choices=ARMS)
    parser.add_argument("--effort", choices=EFFORT_LEVELS, required=True,
                        help="reasoning-effort pin for the scoring spawns "
                             "(passed in workflow opts AND stated in every "
                             "scoring prompt; required — no session inherit)")
    parser.add_argument("--items", default=None,
                        help="comma-separated slug:run pairs restricting the "
                             "workflow to declared re-run items "
                             "(e.g. dye-et-al-2023:2,key-et-al-2024:2)")
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()

    try:
        launch_commit = resolve_launch_commit(REPO_ROOT)
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    items = None
    if args.items:
        items = []
        for token in args.items.split(","):
            slug, _, run = token.partition(":")
            if not run.isdigit() or int(run) not in (1, 2, 3):
                print(f"ERROR: --items entry {token!r}: run must be 1-3",
                      file=sys.stderr)
                return 1
            items.append({"slug": slug, "run": int(run)})

    manifest = yaml.safe_load((REPO_ROOT / "manifest.yaml").read_text())

    schema_rel = manifest["assessment"]["schemas"]["benchmark_fair_output"]["file"]
    schema = json.loads((REPO_ROOT / schema_rel).read_text())
    # S4 retreat (probed 2026-08-17, wf_56a0ba6f-93e): the spawn-side API
    # rejects top-level allOf/anyOf/oneOf in tool input schemas ("400
    # input_schema does not support oneOf, allOf, or anyOf at the top
    # level"), so the runtime variant strips the conditionals; the
    # registered v1.1 file remains the contract of record and its
    # conditional requirements are enforced post hoc by reconcile-run's
    # --contract-schema full validation (the C9 layer), exactly as the
    # pre-specified fallback decided. $ref/definitions are retained —
    # proven acceptable by the 2026-08-03 v1.0 run.
    schema.pop("allOf", None)

    packs = manifest["evidence_packs"]["packs"]
    registry = manifest["reference_datasets"]["pilot_fair_assessments"]["items"]

    papers = []
    for entry in registry:
        slug = entry["slug"]
        paper_path = CORPUS_STORE / slug / "vor.pdf"
        if not paper_path.is_file():
            print(f"ERROR: paper source missing: {paper_path}", file=sys.stderr)
            return 1
        pack_rel = packs[slug]["file"]
        pack_bytes = (REPO_ROOT / pack_rel).read_bytes()
        papers.append({
            "slug": slug,
            "path": str(paper_path),
            "pack": pack_rel,
            "pack_sha256": hashlib.sha256(pack_bytes).hexdigest(),
        })

    payload = {
        "agentType": f"fair-assessor-{args.arm}",
        "arm": args.arm,
        "effort": args.effort,
        "launch_commit": launch_commit,
        "papers": papers,
        "schema": schema,
    }
    if items is not None:
        known = {p["slug"] for p in papers}
        unknown = [it["slug"] for it in items if it["slug"] not in known]
        if unknown:
            print(f"ERROR: --items slugs not in registry: {unknown}",
                  file=sys.stderr)
            return 1
        payload["items"] = items
    text = json.dumps(payload, indent=1, sort_keys=True) + "\n"
    if args.out:
        args.out.write_text(text, encoding="utf-8")
        item_note = f", {len(items)} re-run item(s)" if items is not None else ""
        print(f"args for arm {args.arm}: {len(papers)} papers{item_note}, "
              f"effort {args.effort}, commit {launch_commit[:12]} -> {args.out}")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
