export const meta = {
  name: 'fair-benchmark-arm',
  description: 'One validation-benchmark arm: 5 pilot papers x 3 runs of FAIR scoring with per-item reconciliation hard stop',
  phases: [{ title: 'Score' }, { title: 'Reconcile' }],
}
// v1.1 (D3 prep, 2026-08-17; amendment 2 SS2/SS5). Changes from the v1.0
// script that ran the 2026-08-03 arms: (1) per-paper evidence-pack
// injection — the prompt line format is the single source of truth for
// scripts/reconcile-run.py's PACK_DECLARATION_RE, change both together;
// (2) a per-item Reconcile stage (cheap mechanical agent) runs
// scripts/reconcile-run.py after each scoring spawn and binds the verdict
// to that spawn's agent_id — the C9 per-item hard stop (SubagentStop gate
// decisions are advisory in this lane); (3) the workflow returns
// reconcile_failures and clean so the operator accepts no unreconciled
// item. The operator still runs the whole-dir reconciliation afterwards as
// the authoritative archival pass.
// Args shape: {agentType, arm, papers: [{slug, path, pack, pack_sha256}], schema}
const { agentType, arm, papers, schema } = (typeof args === "string" ? JSON.parse(args) : args)
// The registered schema file carries a document-version field (E4 carrier);
// the runtime validator is strict JSON Schema, so strip non-standard keywords
// from the copy handed to agents.
delete schema.version
for (const p of papers) {
  if (!p.pack || !p.pack_sha256) throw new Error(`paper ${p.slug}: pack path + pack_sha256 required (amendment 2 SS2)`)
}
const tasks = []
for (let run = 1; run <= 3; run++) {
  for (const p of papers) tasks.push({ run, slug: p.slug, path: p.path, pack: p.pack, pack_sha256: p.pack_sha256 })
}
log(`arm ${arm}: ${tasks.length} scoring spawns (5 papers x 3 runs), each with a per-item reconcile stage`)

const RECONCILE_SCHEMA = {
  type: "object",
  additionalProperties: false,
  required: ["slug", "run", "verdict", "agent_id", "detail"],
  properties: {
    slug: { type: "string" },
    run: { type: "integer" },
    verdict: { enum: ["pass", "fail", "unverifiable"] },
    agent_id: { type: "string", description: "The SCORING spawn's agent id (transcript stem after 'agent-'), or empty when unverifiable" },
    detail: { type: "string" },
  },
}

const scorePrompt = (t) =>
  `Benchmark scoring task (preregistered validation phase, arm ${arm}, run ${t.run} of 3).\n` +
  `Paper: ${t.slug}. Source (read in full): ${t.path}\n` +
  `Evidence pack (read in full): ${t.pack} (sha256 ${t.pack_sha256})\n` +
  `Score this paper on the pushed FAIR instrument (v2.1, with its clarification sections) exactly per your agent brief. ` +
  `The paper PDF is the sole paper source: supplementary files are deliberately not provided; ` +
  `apply the data-completeness coverage procedure from the paper's own statements and content. ` +
  `The evidence pack is rung-(i) evidence under the instrument's two-rung ladder: read it in full, ` +
  `declare it in pulled_files_read, and cite pack record ids in pack_refs wherever pack evidence supports a score. ` +
  `Independence requirement: do NOT read any file under studies/ or outputs/ in the repository - ` +
  `your scores must not depend on any persisted assessment. ` +
  `Set paper_slug to "${t.slug}".`

const reconcilePrompt = (t) =>
  `Mechanical verification task - no judgement, no scoring (C9 per-item reconciliation).\n` +
  `A FAIR scoring spawn has just completed in the currently-running workflow: ` +
  `arm ${arm}, run ${t.run} of 3, paper ${t.slug}.\n` +
  `1. Locate the live workflow run directory: list candidates newest-first with\n` +
  `   ls -td ~/.claude/projects/-home-shawn-Code-llm-reproducibility/*/subagents/workflows/wf_*/ 2>/dev/null | head -5\n` +
  `   and pick the newest directory containing an agent-*.jsonl transcript whose text contains BOTH ` +
  `"arm ${arm}, run ${t.run} of 3" AND "Paper: ${t.slug}" (grep -l). The matched transcript's filename stem ` +
  `after "agent-" is the scoring spawn's agent_id. If the transcript has no StructuredOutput tool call yet ` +
  `(still being written), wait 5 seconds and re-check, up to 6 attempts.\n` +
  `2. From the repository root /home/shawn/Code/llm-reproducibility run:\n` +
  `   venv/bin/python scripts/reconcile-run.py <run_dir> --out <run_dir>/reconciliation\n` +
  `   A non-zero exit is EXPECTED whenever any spawn in the directory fails or is still incomplete - ` +
  `do not treat exit status as this item's verdict.\n` +
  `3. Read <run_dir>/reconciliation/reconciliation-report.json and find the record in "agents" whose ` +
  `agent_id matches step 1. verdict = "pass" if that record's "reconciled" is true; otherwise "fail", ` +
  `with the record's receipt problems and contaminating accesses summarised in detail.\n` +
  `If the directory, transcript, or record cannot be found after the retries, verdict = "unverifiable" ` +
  `with what you observed in detail. Never guess an agent_id.`

const results = await pipeline(tasks,
  t => agent(scorePrompt(t), { agentType, label: `${t.slug} r${t.run}`, phase: 'Score', schema })
    .then(v => ({ arm, run: t.run, slug: t.slug, result: v })),
  (scored, t) => scored === null ? null : agent(reconcilePrompt(t), {
    agentType: 'general-purpose', model: 'haiku', effort: 'low',
    label: `reconcile ${t.slug} r${t.run}`, phase: 'Reconcile', schema: RECONCILE_SCHEMA,
  }).then(r => ({ ...scored, reconcile: r }))
)

const ok = results.filter(Boolean)
const failures = ok.filter(x => !x.reconcile || x.reconcile.verdict !== 'pass')
log(`arm ${arm}: ${ok.length}/${tasks.length} spawns returned; ` +
    `${ok.length - failures.length} reconciled pass, ${failures.length} NOT reconciled`)
if (failures.length) {
  log(`HARD STOP (C9): ${failures.map(f => `${f.slug} r${f.run} (${f.reconcile ? f.reconcile.verdict : 'no reconcile result'})`).join('; ')} ` +
      `- these items are unusable until re-run or operator-adjudicated; do not compute gates over them`)
}
return {
  arm,
  count: ok.length,
  clean: failures.length === 0,
  reconcile_failures: failures.map(f => ({ slug: f.slug, run: f.run, reconcile: f.reconcile })),
  results,
}
// Provenance: v1.0 of this script ran all three 2026-08-03 benchmark arms
// (workflow runs wf_9fcbff61-646, wf_4eaecf54-890, wf_627102d7-fa0) and is
// recoverable at tag osf-amendment-2-2026-08-17^ or from the arm
// run-records. v1.1 supersedes it for the D3 re-benchmark.
