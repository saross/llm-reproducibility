export const meta = {
  name: 'reproduction-execute',
  description: 'Reproduction lane stage 2: per approved paper, governed executor, deterministic artefact gate, then a fresh-context adversarial reviewer',
  phases: [{ title: 'Execute' }, { title: 'Gate', model: 'haiku' }, { title: 'Review' }],
}
// reproduction-execute.workflow.js v1.0 (2026-10-03, Phase 2 shakedown build).
//
// Stage 2 of the agentic reproduction lane (modernisation plan §4.2). Runs
// only on papers whose plan carries a committed, hash-bound human approval:
// scripts/reproduction-lane.py build-exec-args refuses anything else
// (invariant 1), so this script trusts its args for approval and re-asserts
// only their shape. Per paper, pipelined (no barrier between papers):
//
//   Execute — governed `reproduction-executor` (Docker build, wrapper,
//             run, comparison against the locked targets; invariants 2, 5).
//   Gate    — a cheap mechanical agent runs reproduction-lane.py
//             check-attempt and relays its JSON verbatim (invariants 3, 6:
//             persistence verified from disk, never from self-report).
//   Review  — governed `adversarial-reviewer` in a fresh context, artefacts
//             only (invariant 4). It runs for EVERY paper whose executor
//             returned, gate pass or fail: a failed gate is itself something
//             the review must see.
//
// The operator afterwards re-runs check-attempt (the authoritative gate),
// persists payloads with persist-results, and audits the run with audit-run.
// Prompt line formats are the single source of truth for the regexes in
// scripts/reproduction-lane.py (PAPER_RE, PROVENANCE_RE, SCRATCH_RE,
// ATTEMPT_DIR_RE) — change both together.
//
// Args shape (built only by reproduction-lane.py build-exec-args):
// {run_id, attempt, effort, launch_commit, agent_types: {executor, reviewer},
//  schemas: {execution, review}, comparison_schema_path, repo_root, blinding,
//  papers: [{slug, attempt, attempt_dir, plan_path, plan_sha256,
//  approval_path, target_ids, paper_pdf, paper_pdf_sha256, supplements,
//  deposits, run_notes, executor_scratch_dir, image_tag}], skipped, receipt_keys:
//  {executor, reviewer}, rulings, args_checksum}
const ARGS = (typeof args === 'string' ? JSON.parse(args) : args)

// Args integrity (2026-10-03). Args travel inline in the Workflow tool call,
// so the ~10 KB built by reproduction-lane.py passes through a copy step
// nothing else re-checks. The builder stamps args_checksum; recompute it over
// what actually arrived and refuse to start on any difference. Algorithm
// mirrors reproduction-lane.py args_checksum(): compact JSON.stringify of the
// args minus the checksum, as UTF-16 code units, 32-bit FNV-1a then 32-bit
// djb2-xor, each as 8 hex digits. Change both together.
const { args_checksum, ...UNSUMMED } = ARGS
const CANONICAL = JSON.stringify(UNSUMMED)
let fnv = 2166136261
let djb = 5381
for (let i = 0; i < CANONICAL.length; i++) {
  const unit = CANONICAL.charCodeAt(i)
  fnv = Math.imul(fnv ^ unit, 16777619) >>> 0
  djb = (Math.imul(djb, 33) ^ unit) >>> 0
}
const COMPUTED = fnv.toString(16).padStart(8, '0') + djb.toString(16).padStart(8, '0')
if (COMPUTED !== args_checksum) {
  throw new Error(`args_checksum mismatch: received ${args_checksum}, computed ${COMPUTED} — ` +
    `the args were altered after reproduction-lane.py built them; rebuild and pass them unedited`)
}
const {
  run_id, attempt, effort, launch_commit, agent_types, receipt_keys, rulings, schemas,
  comparison_schema_path, repo_root, blinding, papers, skipped,
} = ARGS

const EFFORT_LEVELS = ['low', 'medium', 'high', 'xhigh', 'max']
if (!EFFORT_LEVELS.includes(effort)) {
  throw new Error(`effort must be one of ${EFFORT_LEVELS.join('/')}, got: ${effort}`)
}
if (!/^[0-9a-f]{40}$/.test(launch_commit || '')) {
  throw new Error(`launch_commit must be a full 40-hex commit hash, got: ${launch_commit}`)
}
if (agent_types.executor !== 'reproduction-executor' || agent_types.reviewer !== 'adversarial-reviewer') {
  throw new Error(`unexpected agent types: ${JSON.stringify(agent_types)}`)
}
if (!Array.isArray(papers) || papers.length === 0) throw new Error('papers: empty')
for (const role of ['executor', 'reviewer']) {
  if (!receipt_keys || !Array.isArray(receipt_keys[role]) || receipt_keys[role].length === 0) {
    throw new Error(`receipt_keys.${role}: empty`)
  }
}
if (!Array.isArray(rulings)) throw new Error('rulings: must be a list (may be empty)')
for (const p of papers) {
  for (const key of ['slug', 'attempt_dir', 'plan_path', 'plan_sha256', 'approval_path',
    'paper_pdf', 'executor_scratch_dir', 'image_tag']) {
    if (!p[key]) throw new Error(`paper ${p.slug || '?'}: missing ${key}`)
  }
  if (!Array.isArray(p.target_ids) || p.target_ids.length === 0) {
    throw new Error(`paper ${p.slug}: no locked target ids`)
  }
}
for (const s of skipped || []) log(`SKIPPED ${s.slug}: ${s.reason} (not executed; not dropped silently)`)

const GATE_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  required: ['slug', 'exit_code', 'verdict', 'report_path', 'errors'],
  properties: {
    slug: { type: 'string' },
    exit_code: { type: 'integer' },
    verdict: { enum: ['pass', 'fail', 'unverifiable'] },
    report_path: { type: 'string' },
    errors: { type: 'array', items: { type: 'string' } },
    warnings: { type: 'array', items: { type: 'string' } },
    detail: { type: 'string' },
  },
}

const blindingBlock = (slug) =>
  `Blinded paths — never read, list, search, or print any path containing one of these ` +
  `substrings, with any tool (Read, Grep, Glob, Bash, git): ` +
  `${blinding.forbidden_substrings.join(' ; ')}. ` +
  `Also never touch any path naming another paper: ` +
  `${blinding.cross_paper_slugs.filter(s => s !== slug).join(' ; ')}. ` +
  `Earlier reproduction attempts of this paper are blinded too. ` +
  `Two harness files are exempt, and you should read them when they apply to you: ` +
  `(a) if your injected instruments arrive as a pointer to a saved file named like ` +
  `.../tool-results/hook-<id>-<n>-additionalContext.txt, read that file in full — it is your ` +
  `instrument delivery; (b) when one of your own tool results says "Full output saved to: <path>", ` +
  `you may read that path — it is your own output. ` +
  `This run tests whether the pipeline reaches results independently; any other access to a ` +
  `blinded path fails the run.`

const inputsBlock = (p) =>
  `Paper PDF: ${p.paper_pdf} (sha256 ${p.paper_pdf_sha256})\n` +
  (p.supplements.length
    ? p.supplements.map(s => `Supplement: ${s.path} (sha256 ${s.sha256})\n`).join('')
    : 'Supplements: none provided locally.\n') +
  (p.deposits.length
    ? p.deposits.map(d => `Deposit: ${d.identifier} — ${String(d.description).trim()}\n`).join('')
    : 'Deposits: none declared.\n') +
  `Run notes: ${p.run_notes || 'none'}\n`

const forbidArgs = (p) =>
  [p.paper_pdf_sha256, ...p.supplements.map(s => s.sha256)].map(h => `--forbid-sha256 ${h}`).join(' ')

const execPrompt = (p) =>
  `Reproduction-lane execution task (run ${run_id}, attempt ${attempt}).\n` +
  `Paper: ${p.slug}\n` +
  `Provenance: run ${run_id}; launch commit ${launch_commit}; reasoning effort pinned: ${effort}.\n` +
  `Attempt directory: ${p.attempt_dir}\n` +
  `Scratch directory: ${p.executor_scratch_dir}\n` +
  `Approved plan (read in full): ${p.plan_path} (sha256 ${p.plan_sha256})\n` +
  `Approval record: ${p.approval_path}\n` +
  `Locked target ids (${p.target_ids.length}): ${p.target_ids.join(', ')}\n` +
  `Comparison-record schema (read in full): ${comparison_schema_path}\n` +
  `Docker image tag: ${p.image_tag}\n` +
  inputsBlock(p) + `\n` +
  `Execute the approved plan exactly per your agent brief and the output schema. Set paper_slug to ` +
  `"${p.slug}". Key instrument_versions and instrument_receipts by exactly these pushed-instrument ` +
  `names: ${receipt_keys.executor.join(', ')}. In pulled_files_read list bare file paths only — ` +
  `no versions, tokens, or comments in the string.\n` +
  (rulings.length ? `Registrant rulings (apply to every paper): ${rulings.join(' ')}\n` : '') +
  `1. First verify the approval: sha256sum the plan file and confirm it equals both the hash above and ` +
  `the approval record's plan_sha256, with decision "approve". Any mismatch: ESCALATE and stop.\n` +
  `2. Write ONLY under the attempt directory (and the scratch directory for throwaway work). Required ` +
  `artefacts: Dockerfile; your run script(s) at the attempt root; environment.md; log.md (with a ` +
  `Materials Acquired table: URL or DOI, retrieval date, full sha256, destination); ` +
  `comparisons/comparison-report.md; comparisons/comparison.json; outputs/. Templates: ` +
  `reproduction-system/templates/. Fetch with checksum (reproduction-system/prompts/01-preparation.md ` +
  `§1.0–1.0.1): author-released code and data you consume may be stored in the attempt directory; ` +
  `publisher content (the paper PDF, journal supplements) never — reference it by path.\n` +
  `3. Run all paper code inside Docker only: docker build -t ${p.image_tag} <attempt dir>, then ` +
  `docker run --rm with the attempt directory mounted. Never run paper code on the host.\n` +
  `4. comparisons/comparison.json: schema_version "1.0", attempt ${p.attempt}, plan_sha256 ` +
  `${p.plan_sha256}, exactly one record per locked target id — no more, no fewer. Put value-level ` +
  `detail (published vs reproduced, per value) in files under comparisons/ and cite them in evidence.\n` +
  `5. Before finishing, self-check from the repository root (${repo_root}):\n` +
  `   venv/bin/python scripts/reproduction-lane.py check-attempt ${p.attempt_dir} --plan ${p.plan_path} ` +
  `--image ${p.image_tag} ${forbidArgs(p)} --out -\n` +
  `   Fix artefact defects it reports — never by narrowing scope or editing the plan. The orchestrator ` +
  `re-runs this gate independently.\n` +
  `6. ${blindingBlock(p.slug)}\n` +
  `Report outcomes faithfully, including failures: a BLOCKED or PARTIAL verdict honestly reached is a ` +
  `valid result.`

const gatePrompt = (p) =>
  `Mechanical verification task — no judgement, no repairs (artefact gate, pipeline invariants 3, 5, 6).\n` +
  `Paper: ${p.slug}\n` +
  `1. From the repository root ${repo_root} run exactly this one command:\n` +
  `   venv/bin/python scripts/reproduction-lane.py check-attempt ${p.attempt_dir} --plan ${p.plan_path} ` +
  `--image ${p.image_tag} ${forbidArgs(p)}\n` +
  `2. Read ${p.attempt_dir}/gate-report.json.\n` +
  `Return: slug "${p.slug}"; exit_code (the command's exit status); verdict "pass" only if the exit ` +
  `status is 0 AND the report's verdict is "pass", otherwise "fail"; report_path; errors and warnings ` +
  `copied verbatim from the report. If the command cannot run at all, verdict "unverifiable" with what ` +
  `you observed in detail. Do not modify any file and do not re-run with different arguments.`

const reviewPrompt = (p) =>
  `Adversarial review task (run ${run_id}, attempt ${attempt}).\n` +
  `Paper: ${p.slug}\n` +
  `Provenance: run ${run_id}; launch commit ${launch_commit}; reasoning effort pinned: ${effort}.\n` +
  `Artefacts under review — read the approved plan ${p.plan_path} and every artefact the reproduction ` +
  `wrote under ${p.attempt_dir} (Dockerfile, run scripts, environment.md, log.md, comparisons/, ` +
  `outputs/, gate-report.json; execution-report.json and adversarial-review.json do not exist yet).\n` +
  `Locked target ids (${p.target_ids.length}): ${p.target_ids.join(', ')}\n` +
  inputsBlock(p) + `\n` +
  `You have no memory of this reproduction and must not seek any. Audit it across the pushed ` +
  `framework's five dimensions and try to refute the verdict. Spot-check with Bash where the ` +
  `artefacts permit — hashes, recomputing a sample of reproduced and published values from the ` +
  `output and comparison files, reading the paper's tables, parsing the scripts — but never re-run ` +
  `the analysis and write nothing anywhere. Set paper_slug to "${p.slug}". Key instrument_versions ` +
  `and instrument_receipts by exactly these pushed-instrument names: ` +
  `${receipt_keys.reviewer.join(', ')}. In pulled_files_read list bare file paths only — no ` +
  `versions, tokens, or comments in the string.\n` +
  (rulings.length ? `Registrant rulings the reproduction was run under: ${rulings.join(' ')}\n` : '') +
  `${blindingBlock(p.slug)}`

log(`run ${run_id}: ${papers.length} approved paper(s); effort pinned ${effort}; launch commit ` +
    `${launch_commit.slice(0, 12)}`)

const results = await pipeline(papers,
  p => agent(execPrompt(p), {
    agentType: agent_types.executor, effort, label: `execute ${p.slug}`, phase: 'Execute',
    schema: schemas.execution,
  }).then(v => (v === null ? null : { slug: p.slug, execution: v })),
  (r, p) => (r === null ? null : agent(gatePrompt(p), {
    agentType: 'general-purpose', model: 'haiku', effort: 'low', label: `gate ${p.slug}`,
    phase: 'Gate', schema: GATE_SCHEMA,
  }).then(g => ({ ...r, gate: g }))),
  (r, p) => (r === null ? null : agent(reviewPrompt(p), {
    agentType: agent_types.reviewer, effort, label: `review ${p.slug}`, phase: 'Review',
    schema: schemas.review,
  }).then(v => ({ ...r, review: v }))),
)

const done = results.filter(Boolean)
const missing = papers.filter(p => !done.some(r => r.slug === p.slug)).map(p => p.slug)
// The human escalation queue (plan §4.4): ESCALATE outputs, failed or
// unverifiable gates, QUALIFIED/CHALLENGED reviews, missing reviews, and
// PAPER_ERROR / CANNOT_COMPARE calls all surface before entering study data.
const queue = []
for (const r of done) {
  const ex = r.execution || {}
  if (ex.status === 'ESCALATE') queue.push(`${r.slug}: executor ESCALATE — ${ex.escalate_reason}`)
  for (const e of ex.escalations || []) queue.push(`${r.slug}: ${e.kind} ${e.target_id || ''} — ${e.detail}`)
  if (!r.gate || r.gate.verdict !== 'pass') queue.push(`${r.slug}: gate ${r.gate ? r.gate.verdict : 'did not return'}`)
  if (!r.review) queue.push(`${r.slug}: review did not return`)
  else if (r.review.status === 'ESCALATE') queue.push(`${r.slug}: reviewer ESCALATE — ${r.review.escalate_reason}`)
  else if (r.review.overall !== 'CONFIRMED') queue.push(`${r.slug}: review ${r.review.overall}`)
}
log(`${done.length}/${papers.length} papers through the pipeline; missing: ${missing.join(', ') || 'none'}; ` +
    `${queue.length} item(s) for human attention. Next: re-run check-attempt, persist-results, audit-run.`)
return {
  run_id,
  launch_commit,
  effort,
  missing,
  human_queue: queue,
  summary: done.map(r => ({
    slug: r.slug,
    executor_status: (r.execution || {}).status,
    verdict: (r.execution || {}).verdict,
    gate: r.gate ? r.gate.verdict : null,
    review: r.review ? (r.review.status === 'OK' ? r.review.overall : r.review.status) : null,
  })),
}
