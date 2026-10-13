"""Re-audit the herskind pilot (attempt-03) with gate 1.3.1 through the real audit-run.

Runs scripts/reproduction-lane.py's own cmd_audit_run on the stage-2 workflow
run, with two redirections so nothing in the attempt changes: the paper's
attempt resolves to the main checkout's copy, which the transcripts name
(identical content), and every file the command would write into the attempt
is written into this folder instead. Receipts are checked against the
manifest at the run's launch commit.

Usage: venv/bin/python -I reaudit.py <worktree root> <main checkout root> <workflow run dir>
"""
import argparse
import importlib.util
import sys
from pathlib import Path

WT, MAIN, RUN = (Path(a) for a in sys.argv[1:4])
REL = "studies/open-science-compliance/outputs/herskind-riede-2024/reproduction/attempt-03"
OUT = WT / "studies/open-science-compliance/outputs/validation/gate-1-3-pilot-rerun/reaudit-gate-1.3.1"
spec = importlib.util.spec_from_file_location("lane", WT / "scripts" / "reproduction-lane.py")
lane = importlib.util.module_from_spec(spec)
sys.modules["lane"] = lane
spec.loader.exec_module(lane)

attempt = MAIN / REL
lane.attempt_dir = lambda config, slug: attempt
original_write = lane.write_json


def redirected(path, doc):
    """Write into this folder whatever the command would write into the attempt."""
    path = Path(path)
    if path.parent == attempt:
        path = OUT / path.name
    original_write(path, doc)


lane.write_json = redirected
config = WT / "studies/open-science-compliance/outputs/validation/gate-1-3-pilot-rerun/run-config.yaml"
status = lane.cmd_audit_run(argparse.Namespace(config=config, run_dir=RUN,
                                               out=OUT / f"audit-{RUN.name}.json"))
print("audit-run exit status:", status)
