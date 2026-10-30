export const meta = {
  name: 'reproduction-review',
  description: 'Reproduction lane review-only re-run: per executed attempt, a mechanical gate check that stages a clean copy of the reviewable state, then a fresh-context adversarial reviewer on that copy; no executor',
  phases: [{ title: 'Gate', model: 'haiku' }, { title: 'Review' }],
}
// reproduction-review.workflow.js v1.0 (2026-10-30, gate 1.3.2 criterion 4:
// the review-only mode; design in wiki/planning/reproduction-gate-1-3-design.md,
// "The review-only mode as designed").
//
// Re-reviews attempts that have already been executed, with a fresh reviewer
// and no executor spawn. Runs only on attempts whose persisted executor result
// an earlier run audit cleared for the attempt as it stands:
// scripts/reproduction-lane.py build-review-args refuses anything else, and
// binds that executor result in the args, so this script trusts its args for
// the binding and re-asserts only their shape. Per paper, pipelined:
//
//   Gate    — a cheap mechanical agent runs check-attempt with the executor's
//             launch commit (the sealed run records are checked against it),
//             then stage-review, which copies the reviewable state and the
//             gate report into a fresh folder and prints the state it copied,
//             so the harness records the reviewed state.
//   Review  — governed `adversarial-reviewer` in a fresh context, reading only
//             the staged copy (Shawn, 2026-10-30: a clean copy, never the
//             attempt with the earlier review blinded by name). It runs only
//             where the copy was staged: with no copy there is nothing to
//             review.
//
// The operator afterwards re-runs check-attempt (the authoritative gate),
// audits the run with audit-run (which carries the executor's clearance from
// the attempt's earlier run audit), rules the new issues, persists the review
// with persist-results, and adjudicates. Prompt line formats are the single
// source of truth for the regexes in scripts/reproduction-lane.py (PAPER_RE,
// PROVENANCE_RE, REVIEW_COPY_RE) — change both together. audit-run binds the
// review to the copy its gate step staged: the "Review copy:" line must name it.
//
// Args shape (built only by reproduction-lane.py build-review-args):
// {mode: "review-only", run_id, attempt, effort, launch_commit,
//  agent_types: {reviewer}, schemas: {review}, repo_root, blinding,
//  papers: [{slug, attempt, attempt_dir, plan_path, plan_sha256, approval_path,
//  target_ids, paper_pdf, paper_pdf_sha256, supplements, deposits, run_notes,
//  image_tag, review_dir, executor: {run_id, workflow_run, agent_id,
//  payload_sha256, launch_commit}}], skipped, receipt_keys: {reviewer},
//  rulings, args_checksum}
const ARGS = (typeof args === 'string' ? JSON.parse(args) : args)

// Args integrity, as in the execute workflow: recompute args_checksum over
// what arrived and refuse to start on any difference. Algorithm mirrors
// reproduction-lane.py args_checksum(); change all three together.
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
  mode, run_id, attempt, effort, launch_commit, agent_types, receipt_keys, rulings, schemas,
  repo_root, blinding, papers, skipped,
} = ARGS

const HEX40 = /^[0-9a-f]{40}$/
const EFFORT_LEVELS = ['low', 'medium', 'high', 'xhigh', 'max']
if (mode !== 'review-only') throw new Error(`mode must be "review-only", got: ${mode}`)
if (!EFFORT_LEVELS.includes(effort)) {
  throw new Error(`effort must be one of ${EFFORT_LEVELS.join('/')}, got: ${effort}`)
}
if (!HEX40.test(launch_commit || '')) {
  throw new Error(`launch_commit must be a full 40-hex commit hash, got: ${launch_commit}`)
}
if (agent_types.reviewer !== 'adversarial-reviewer' || agent_types.executor !== undefined) {
  throw new Error(`unexpected agent types: ${JSON.stringify(agent_types)}`)
}
if (!Array.isArray(papers) || papers.length === 0) throw new Error('papers: empty')
if (!receipt_keys || !Array.isArray(receipt_keys.reviewer) || receipt_keys.reviewer.length === 0) {
  throw new Error('receipt_keys.reviewer: empty')
}
if (!Array.isArray(rulings)) throw new Error('rulings: must be a list (may be empty)')
for (const p of papers) {
  for (const key of ['slug', 'attempt_dir', 'plan_path', 'plan_sha256', 'paper_pdf',
    'review_dir', 'image_tag']) {
    if (!p[key]) throw new Error(`paper ${p.slug || '?'}: missing ${key}`)
  }
  if (!Array.isArray(p.target_ids) || p.target_ids.length === 0) {
    throw new Error(`paper ${p.slug}: no locked target ids`)
  }
  const ex = p.executor || {}
  for (const key of ['run_id', 'workflow_run', 'agent_id', 'payload_sha256']) {
    if (!ex[key]) throw new Error(`paper ${p.slug}: the executor binding has no ${key}`)
  }
  if (!HEX40.test(ex.launch_commit || '')) {
    throw new Error(`paper ${p.slug}: the executor's launch commit is not a 40-hex hash`)
  }
}
for (const s of skipped || []) log(`SKIPPED ${s.slug}: ${s.reason} (not reviewed; not dropped silently)`)

const GATE_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  required: ['slug', 'exit_code', 'verdict', 'report_path', 'errors', 'warnings', 'flags',
    'staged', 'artefact_state_sha256'],
  properties: {
    slug: { type: 'string' },
    exit_code: { type: 'integer' },
    verdict: { enum: ['pass', 'fail', 'unverifiable'] },
    report_path: { type: 'string' },
    errors: { type: 'array', items: { type: 'string' } },
    warnings: { type: 'array', items: { type: 'string' } },
    flags: { type: 'array', items: { type: 'string' } },
    staged: { type: 'boolean' },
    artefact_state_sha256: { type: 'string' },
    detail: { type: 'string' },
  },
}

const blindingBlock = (slug) =>
  `Blinded paths — never read, list, search, or print any path containing one of these ` +
  `substrings, with any tool (Read, Grep, Glob, Bash, git): ` +
  `${blinding.forbidden_substrings.join(' ; ')}. ` +
  `Also never touch any path naming another paper: ` +
  `${blinding.cross_paper_slugs.filter(s => s !== slug).join(' ; ')}. ` +
  `Earlier reproduction attempts of this paper are blinded too, and so is the attempt ` +
  `directory this copy was staged from. ` +
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

const gatePrompt = (p) =>
  `Mechanical verification task — no judgement, no repairs (review-only gate check and staging).\n` +
  `Paper: ${p.slug}\n` +
  `1. From the repository root ${repo_root} run exactly this one command:\n` +
  `   venv/bin/python scripts/reproduction-lane.py check-attempt ${p.attempt_dir} --plan ${p.plan_path} ` +
  `--image ${p.image_tag} --launch-commit ${p.executor.launch_commit} ${forbidArgs(p)}\n` +
  `2. Read ${p.attempt_dir}/gate-report.json.\n` +
  `3. Then, from the same root, run exactly this one command, even if step 1 failed:\n` +
  `   venv/bin/python scripts/reproduction-lane.py stage-review ${p.attempt_dir} --to ${p.review_dir}\n` +
  `Return: slug "${p.slug}"; exit_code (step 1's exit status); verdict "pass" only if step 1's exit ` +
  `status is 0 AND the report's verdict is "pass", otherwise "fail"; report_path; errors, warnings, ` +
  `and flags copied verbatim from the report (each a list; return an empty list when the report's ` +
  `list is empty, and never omit one); staged true only if step 3 exited 0, otherwise false; ` +
  `artefact_state_sha256 copied verbatim from step 3's output, or an empty string if it printed ` +
  `none. If a command cannot run at all, verdict "unverifiable" with what you observed in detail. ` +
  `Do not modify any file and do not re-run with different arguments.`

const reviewPrompt = (p) =>
  `Adversarial review task (run ${run_id}, attempt ${attempt}; review-only re-run).\n` +
  `Paper: ${p.slug}\n` +
  `Provenance: run ${run_id}; launch commit ${launch_commit}; reasoning effort pinned: ${effort}.\n` +
  `Review copy: ${p.review_dir}\n` +
  `This reproduction was executed earlier, in workflow run ${p.executor.workflow_run}; no ` +
  `executor runs now. The lane staged a copy of its reviewable state, with its gate report, in ` +
  `${p.review_dir}, and that copy is the attempt directory for this review: every path you cite ` +
  `is relative to it. The executor's report and any earlier review are withheld by design; do ` +
  `not look for them.\n` +
  `Artefacts under review — read the approved plan ${p.review_dir}/reproduction-plan.json ` +
  `(sha256 ${p.plan_sha256}) and every artefact under ${p.review_dir} (Dockerfile, run scripts, ` +
  `environment.md, log.md, comparisons/, outputs/, lane-records/, gate-report.json).\n` +
  `Locked target ids (${p.target_ids.length}): ${p.target_ids.join(', ')}\n` +
  inputsBlock(p) + `\n` +
  `You have no memory of this reproduction and must not seek any. Audit it across the pushed ` +
  `framework's five dimensions and try to refute the verdict. Spot-check with Bash where the ` +
  `artefacts permit — hashes, recomputing a sample of reproduced and published values from the ` +
  `output and comparison files, reading the paper's tables, parsing the scripts — but never re-run ` +
  `the analysis and write nothing anywhere. Set paper_slug to "${p.slug}". Key instrument_versions ` +
  `and instrument_receipts by exactly these pushed-instrument names: ` +
  `${receipt_keys.reviewer.join(', ')}. In pulled_files_read list bare file paths only — no ` +
  `versions, tokens, or comments in the string. ` +
  `List a file in pulled_files_read only if you read all of it (Read with no limit or ` +
  `offset, or a Bash command that is only cat <path>, perhaps after cd <dir> &&); head, ` +
  `tail, sed -n, grep, and a cat that is piped, redirected, or one step among other ` +
  `commands do not count, and make your receipts invalid and the run inadmissible, so ` +
  `read the file in full or leave it out.\n` +
  `gate-report.json lists review_obligations: what the mechanical gate cannot verify (wrapper ` +
  `semantics, dynamic evaluation, content fetched into the image). Address each one explicitly ` +
  `in your provenance dimension.\n` +
  (rulings.length ? `Registrant rulings the reproduction was run under: ${rulings.join(' ')}\n` : '') +
  `${blindingBlock(p.slug)}`

log(`run ${run_id} (review-only): ${papers.length} executed attempt(s); effort pinned ${effort}; ` +
    `launch commit ${launch_commit.slice(0, 12)}`)

const results = await pipeline(papers,
  p => agent(gatePrompt(p), {
    agentType: 'general-purpose', model: 'haiku', effort: 'low', label: `gate ${p.slug}`,
    phase: 'Gate', schema: GATE_SCHEMA,
  }).then(g => (g === null ? null : { slug: p.slug, gate: g })),
  (r, p) => (r === null || !r.gate.staged ? r : agent(reviewPrompt(p), {
    agentType: agent_types.reviewer, effort, label: `review ${p.slug}`, phase: 'Review',
    schema: schemas.review,
  }).then(v => ({ ...r, review: v }))),
)

const done = results.filter(Boolean)
const missing = papers.filter(p => !done.some(r => r.slug === p.slug)).map(p => p.slug)
// The human escalation queue, as in the execute workflow, less the executor's
// items (its escalations were raised and ruled in its own run).
const queue = []
for (const r of done) {
  if (!r.gate || r.gate.verdict !== 'pass') queue.push(`${r.slug}: gate ${r.gate ? r.gate.verdict : 'did not return'}`)
  if (r.gate && !r.gate.staged) queue.push(`${r.slug}: the review copy was not staged, so nothing was reviewed`)
  if (r.gate && (!Array.isArray(r.gate.flags) || !Array.isArray(r.gate.warnings))) {
    queue.push(`${r.slug}: gate relay omitted its flags or warnings — rebuild the queue with ` +
      `reproduction-lane.py human-queue before clearing anything`)
  }
  for (const f of (r.gate && Array.isArray(r.gate.flags) ? r.gate.flags : [])) {
    queue.push(`${r.slug}: ${f}`)
  }
  if (r.gate && r.gate.staged && !r.review) queue.push(`${r.slug}: review did not return`)
  else if (r.review && r.review.status === 'ESCALATE') queue.push(`${r.slug}: reviewer ESCALATE — ${r.review.escalate_reason}`)
  else if (r.review && r.review.overall !== 'CONFIRMED') queue.push(`${r.slug}: review ${r.review.overall}`)
}
log(`${done.length}/${papers.length} papers through the pipeline; missing: ${missing.join(', ') || 'none'}; ` +
    `${queue.length} item(s) for human attention. Next, in this order: check-attempt with the ` +
    `executor's --launch-commit, audit-run, human-queue (the authoritative queue, reconciled ` +
    `against this one), rule-flags, persist-results, and adjudicate last (study data reads its record).`)
return {
  run_id,
  mode,
  launch_commit,
  effort,
  missing,
  human_queue: queue,
  summary: done.map(r => ({
    slug: r.slug,
    executor_workflow_run: (papers.find(p => p.slug === r.slug) || {}).executor.workflow_run,
    gate: r.gate ? r.gate.verdict : null,
    staged: r.gate ? r.gate.staged : false,
    review: r.review ? (r.review.status === 'OK' ? r.review.overall : r.review.status) : null,
  })),
}
