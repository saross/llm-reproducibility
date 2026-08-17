export const meta = {
  name: 'fair-benchmark-arm',
  description: 'One validation-benchmark arm: 5 pilot papers x 3 runs of FAIR scoring with per-item reconciliation hard stop',
  phases: [{ title: 'Score' }, { title: 'Reconcile' }],
}
// v1.5 (effort pinning, 2026-08-17). Changes from v1.4 (which ran the D3
// arms): (4) reasoning effort is PINNED, never session-inherited — args
// carry {effort, launch_commit} (built only by
// scripts/build-benchmark-args.py, which refuses a dirty tracked tree);
// effort rides the scoring agent() opts (behavioural pin) AND a Provenance
// line in every scoring prompt (artefact-derived record: the harness
// persists no effort field in spawn metadata, so the transcript prompt is
// the only durable carrier). The Provenance line format is the single
// source of truth for scripts/assemble-arm-record.py's PROVENANCE_RE —
// change both together, and never touch prompt lines 1-3 (assembler
// PROMPT_RE + reconciler PACK_DECLARATION_RE anchor there).
// Prior changes from the v1.0 script that ran the 2026-08-03 arms:
// (1) per-paper evidence-pack injection — the prompt line format is the
// single source of truth for scripts/reconcile-run.py's
// PACK_DECLARATION_RE, change both together;
// (2) a per-item Reconcile stage (cheap mechanical agent) runs
// scripts/reconcile-run.py after each scoring spawn and binds the verdict
// to that spawn's agent_id — the C9 per-item hard stop (SubagentStop gate
// decisions are advisory in this lane); (3) the workflow returns
// reconcile_failures and clean so the operator accepts no unreconciled
// item. The operator still runs the whole-dir reconciliation afterwards as
// the authoritative archival pass.
// Args shape: {agentType, arm, effort, launch_commit, papers: [{slug, path, pack, pack_sha256}], schema}
const { agentType, arm, effort, launch_commit, papers, schema } = (typeof args === "string" ? JSON.parse(args) : args)
const EFFORT_LEVELS = ["low", "medium", "high", "xhigh", "max"]
if (!EFFORT_LEVELS.includes(effort)) {
  // Effort pinning: an absent or malformed pin means the spawns would
  // silently inherit the session's effort — the exact failure this build
  // exists to close. Hard stop, never default.
  throw new Error(`effort must be one of ${EFFORT_LEVELS.join("/")}, got: ${effort}`)
}
if (!/^[0-9a-f]{40}$/.test(launch_commit || "")) {
  throw new Error(`launch_commit must be a full 40-hex commit hash, got: ${launch_commit}`)
}
// The registered schema file carries a document-version field (E4 carrier);
// the runtime validator is strict JSON Schema, so strip non-standard keywords
// from the copy handed to agents.
delete schema.version
if (agentType !== `fair-assessor-${arm}`) {
  // Audit F17: a mislabelled invocation (sonnet scores filed as opus) would
  // otherwise be invisible in-band.
  throw new Error(`arm/agentType mismatch: arm=${arm} agentType=${agentType}`)
}
for (const p of papers) {
  if (!p.pack || !p.pack_sha256) throw new Error(`paper ${p.slug}: pack path + pack_sha256 required (amendment 2 SS2)`)
}
const tasks = []
for (let run = 1; run <= 3; run++) {
  for (const p of papers) tasks.push({ run, slug: p.slug, path: p.path, pack: p.pack, pack_sha256: p.pack_sha256 })
}
log(`arm ${arm}: ${tasks.length} scoring spawns (5 papers x 3 runs), each with a per-item reconcile stage; ` +
    `effort pinned ${effort}, launch commit ${launch_commit.slice(0, 12)}`)

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
  `Provenance: launch commit ${launch_commit}; reasoning effort pinned: ${effort}.\n` +
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
  `"arm ${arm}, run ${t.run} of 3" AND "Paper: ${t.slug}" (grep -l). TWO CRITICAL disambiguations: ` +
  `(a) your own transcript also contains those strings — for EVERY grep match, read the sibling ` +
  `agent-<id>.meta.json and keep only transcripts whose agentType is "${agentType}"; ` +
  `(b) OLDER benchmark runs used identical prompt wording — the transcript must ALSO contain the ` +
  `literal string "Evidence pack (read in full)" (pre-2026-08-17 runs have none). Use ONLY the newest ` +
  `directory; if the expected transcript is not yet visible there, wait 5 seconds and re-check the ` +
  `NEWEST directory again (up to 6 attempts) — NEVER fall back to an older directory. The surviving ` +
  `transcript's filename stem after "agent-" is the scoring spawn's agent_id.\n` +
  `2. From the repository root /home/shawn/Code/llm-reproducibility run:\n` +
  `   venv/bin/python scripts/reconcile-run.py <run_dir> --require-pack --contract-schema assessment-system/schema/benchmark-fair-output-schema.json --out <run_dir>/reconciliation\n` +
  `   A non-zero exit is EXPECTED whenever any spawn in the directory fails or is still incomplete - ` +
  `do not treat exit status as this item's verdict.\n` +
  `3. Read <run_dir>/reconciliation/reconciliation-report.json and find the record in "agents" whose ` +
  `agent_id matches step 1. verdict = "pass" if that record's "reconciled" is true; otherwise "fail", ` +
  `with the record's receipt problems and contaminating accesses summarised in detail.\n` +
  `If the directory, transcript, or record cannot be found after the retries, verdict = "unverifiable" ` +
  `with what you observed in detail. Never guess an agent_id.`

const results = await pipeline(tasks,
  t => agent(scorePrompt(t), { agentType, effort, label: `${t.slug} r${t.run}`, phase: 'Score', schema })
    .then(v => ({ arm, run: t.run, slug: t.slug, result: v })),
  (scored, t) => scored === null ? null : agent(reconcilePrompt(t), {
    agentType: 'general-purpose', model: 'haiku', effort: 'low',
    label: `reconcile ${t.slug} r${t.run}`, phase: 'Reconcile', schema: RECONCILE_SCHEMA,
  }).then(r => ({ ...scored, reconcile: r }))
)

const ok = results.filter(Boolean)
const missing = tasks.length - ok.length
const failures = ok.filter(x => !x.reconcile || x.reconcile.verdict !== 'pass')
// Audit F13: ESCALATE outputs are counted in-band, not left to log archaeology.
const escalates = ok.filter(x => x.result && x.result.status === 'ESCALATE')
log(`arm ${arm}: ${ok.length}/${tasks.length} spawns returned (${missing} missing); ` +
    `${ok.length - failures.length} reconciled pass, ${failures.length} NOT reconciled; ` +
    `${escalates.length} ESCALATE`)
if (failures.length || missing || escalates.length) {
  log(`HARD STOP (C9): ${failures.map(f => `${f.slug} r${f.run} (${f.reconcile ? f.reconcile.verdict : 'no reconcile result'})`).join('; ') || 'no reconcile failures'}; ` +
      `${missing} item(s) never returned; ${escalates.length} ESCALATE(s) ` +
      `- unusable items must be re-run or operator-adjudicated; do not compute gates over them`)
}
return {
  arm,
  effort,
  launch_commit,
  count: ok.length,
  missing,
  // Audit F4: an arm with items that never returned is NOT clean.
  clean: failures.length === 0 && missing === 0 && escalates.length === 0,
  escalates: escalates.map(x => ({ slug: x.slug, run: x.run })),
  reconcile_failures: failures.map(f => ({ slug: f.slug, run: f.run, reconcile: f.reconcile })),
  results,
}
// Provenance: v1.0 of this script ran all three 2026-08-03 benchmark arms
// (workflow runs wf_9fcbff61-646, wf_4eaecf54-890, wf_627102d7-fa0) and is
// recoverable at tag osf-amendment-2-2026-08-17^ or from the arm
// run-records. v1.1 supersedes it for the D3 re-benchmark.
