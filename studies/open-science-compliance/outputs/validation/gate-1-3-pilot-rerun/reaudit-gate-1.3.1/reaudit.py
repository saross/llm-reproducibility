"""Re-audit the herskind pilot (attempt-03) with gate 1.3.1, writing to a separate folder.

Mirrors cmd_audit_run for the stage-2 workflow run, but writes the transcript
audit, the run audit, and the workflow audit into
validation/gate-1-3-pilot-rerun/reaudit-gate-1.3.1/ rather than into the
attempt, whose gate 1.3 records stay as they were.

Usage: venv/bin/python -I reaudit.py <worktree root> <workflow run dir>
"""
import importlib.util
import json
import sys
from pathlib import Path

WT = Path(sys.argv[1])
RUN = Path(sys.argv[2])
sys.path.insert(0, str(WT / ".claude" / "hooks"))
spec = importlib.util.spec_from_file_location("lane", WT / "scripts" / "reproduction-lane.py")
lane = importlib.util.module_from_spec(spec)
sys.modules["lane"] = lane
spec.loader.exec_module(lane)
import hooklib

config = lane.load_config(WT / "studies/open-science-compliance/outputs/validation/"
                                "gate-1-3-pilot-rerun/run-config.yaml")
# The transcript names the main checkout's attempt (identical content), so the
# audit reads that one; nothing is written there.
attempt = Path("/home/shawn/Code/llm-reproducibility/studies/open-science-compliance/"
               "outputs/herskind-riede-2024/reproduction/attempt-03")
out = WT / "studies/open-science-compliance/outputs/validation/gate-1-3-pilot-rerun/reaudit-gate-1.3.1"
out.mkdir(exist_ok=True)
reconcile = lane.load_module("reconcile_run", "scripts/reconcile-run.py")
gate = reconcile.load_gate_module()
manifest = hooklib.load_manifest()
agents, roles = [], {}
for transcript in sorted(RUN.glob("agent-*.jsonl")):
    meta = json.loads(transcript.with_name(f"{transcript.stem}.meta.json").read_text())
    lines = transcript.read_text(encoding="utf-8").splitlines()
    record = lane.audit_agent(lines, str(meta.get("agentType") or ""), config, manifest,
                              reconcile, gate, hooklib)
    record["agent_id"] = transcript.stem.replace("agent-", "")
    role = {config["agents"]["executor"]: "executor",
            config["agents"]["reviewer"]: "reviewer"}.get(meta.get("agentType"))
    if role == "executor":
        manifest_doc = json.loads((attempt / lane.CODE_MANIFEST_FILE).read_text())
        execution = lane.audit_execution(lines, attempt, manifest_doc)
        execution["transcript"] = lane.display_path(transcript)
        lane.write_json(out / lane.AUDIT_FILE, execution)
        record["execution_audit"] = {"contaminating": execution["contaminating"],
                                     "issues": len(execution["issues"])}
        if execution["contaminating"]:
            record["clean"] = False
    if role:
        roles[role] = (record, gate.structured_output_from_transcript(lines))
    agents.append(record)
lane.write_json(out / lane.RUN_AUDIT_FILE, lane.attempt_run_audit(config, RUN.name, attempt,
                                                                  roles))
report = {"audit_version": "1.0", "audited_at": lane.now_utc(), "run_id": config["run_id"],
          "workflow_run": RUN.name, "agents": agents, "clean": all(a["clean"] for a in agents),
          "per_paper": {}, "note": "re-audit with gate 1.3.1 (2026-10-12); the original "
                                   "gate 1.3 audit is audit-wf_7c18dfdc-298.json"}
lane.write_json(out / f"audit-{RUN.name}.json", report)
print("clean:", report["clean"])
for a in agents:
    print(a["agent_type"], "clean", a["clean"], "receipts", (a.get("receipts") or {}).get("problems"),
          "contaminating", [c.get("path") for c in a["blinding"]["contaminating"]],
          "launch", a.get("launch_message"))
