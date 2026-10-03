export const meta = {
  name: 'reproduction-plan',
  description: 'Reproduction lane stage 1: one governed planner spawn per paper; plans return for orchestrator persistence and batched human approval',
  phases: [{ title: 'Plan' }],
}
// reproduction-plan.workflow.js v1.0 (2026-10-03, Phase 2 shakedown build).
//
// Stage 1 of the agentic reproduction lane (modernisation plan §4.2, Phase 2
// option (a)). Fans the governed `reproduction-planner` agent over the papers
// in the args and returns each schema-validated plan. Nothing executes here:
// invariant 1 puts a human approval between this workflow and
// reproduction-execute.workflow.js, so the two are separate runs by design.
//
// Workflow scripts have no filesystem access. The operator therefore:
//   1. builds args:  scripts/reproduction-lane.py build-plan-args
//      (hashes inputs, pins the launch commit, refuses a dirty tree);
//   2. runs this workflow;
//   3. persists:     scripts/reproduction-lane.py persist-plans --run-dir <run>
//      (full-schema validation, plan checks, plan JSON + Markdown, triage);
//   4. approves:     scripts/reproduction-lane.py approve (per paper).
//
// Prompt line formats are the single source of truth for the regexes in
// scripts/reproduction-lane.py (PAPER_RE, PROVENANCE_RE, SCRATCH_RE) — change
// both together. Effort is pinned twice, as in the FAIR benchmark (working
// notes Observation 27): in the agent() opts (behaviour) and in a Provenance
// line (the harness persists no effort field, so the prompt is the record).
//
// Args shape (built only by reproduction-lane.py build-plan-args):
// {run_id, attempt, effort, launch_commit, agent_type, schema, blinding:
//  {forbidden_substrings, cross_paper_slugs}, papers: [{slug, attempt_dir,
//  paper_pdf, paper_pdf_sha256, supplements: [{path, sha256}], deposits:
//  [{identifier, description}], run_notes, scratch_dir}], args_checksum}
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
const { run_id, attempt, effort, launch_commit, agent_type, schema, blinding, papers } = ARGS

const EFFORT_LEVELS = ['low', 'medium', 'high', 'xhigh', 'max']
if (!EFFORT_LEVELS.includes(effort)) {
  // An absent pin means the spawns silently inherit the session's effort —
  // and Opus 5.5 defaults to medium. Hard stop, never default.
  throw new Error(`effort must be one of ${EFFORT_LEVELS.join('/')}, got: ${effort}`)
}
if (!/^[0-9a-f]{40}$/.test(launch_commit || '')) {
  throw new Error(`launch_commit must be a full 40-hex commit hash, got: ${launch_commit}`)
}
if (agent_type !== 'reproduction-planner') {
  throw new Error(`agent_type must be reproduction-planner, got: ${agent_type}`)
}
if (!Array.isArray(papers) || papers.length === 0) throw new Error('papers: empty')
for (const p of papers) {
  for (const key of ['slug', 'attempt_dir', 'paper_pdf', 'paper_pdf_sha256', 'scratch_dir']) {
    if (!p[key]) throw new Error(`paper ${p.slug || '?'}: missing ${key}`)
  }
}

// Blinding (Shawn, 2026-10-03): instruction now, transcript audit after
// (reproduction-lane.py audit-run). Spawn-time path enforcement is not
// available in the harness (amendment 2 §4).
const blindingBlock = (slug) =>
  `Blinded paths — never read, list, search, or print any path containing one of these ` +
  `substrings, with any tool (Read, Grep, Glob, Bash, git): ` +
  `${blinding.forbidden_substrings.join(' ; ')}. ` +
  `Also never touch any path naming another paper: ` +
  `${blinding.cross_paper_slugs.filter(s => s !== slug).join(' ; ')}. ` +
  `A pulled reference on that list is skipped, not declared. This run tests whether the ` +
  `pipeline reaches results independently; any access to a blinded path fails the run.`

const planPrompt = (p) =>
  `Reproduction-lane planning task (run ${run_id}, attempt ${attempt}).\n` +
  `Paper: ${p.slug}\n` +
  `Provenance: run ${run_id}; launch commit ${launch_commit}; reasoning effort pinned: ${effort}.\n` +
  `Scratch directory: ${p.scratch_dir}\n` +
  `Paper PDF (read in full, every page): ${p.paper_pdf} (sha256 ${p.paper_pdf_sha256})\n` +
  (p.supplements.length
    ? p.supplements.map(s => `Supplement (read in full, every page): ${s.path} (sha256 ${s.sha256})\n`).join('')
    : 'Supplements: none provided locally.\n') +
  (p.deposits.length
    ? p.deposits.map(d => `Deposit: ${d.identifier} — ${String(d.description).trim()}\n`).join('')
    : 'Deposits: none declared; find code and data from the paper and supplements.\n') +
  `Run notes: ${p.run_notes || 'none'}\n` +
  `Planned attempt directory (the executor's, after approval — do not create or write it): ${p.attempt_dir}\n\n` +
  `Produce the reproduction plan for this paper exactly per your agent brief and the output schema. ` +
  `Set paper_slug to "${p.slug}". Key instrument_versions and instrument_receipts by each pushed ` +
  `instrument's name attribute.\n` +
  `- Tolerances: the verdicts-and-precision instrument is not pushed to you. Read ` +
  `studies/open-science-compliance/protocol/instruments/verdicts-and-precision.md in full, declare it ` +
  `in pulled_files_read, and state each target's tolerance in its terms.\n` +
  `- Materials: you may download deposits and supplements into the scratch directory (create it) to ` +
  `inspect code and data and to record checksums (sha256sum, or the repository's published md5). ` +
  `Never run the analysis, and never write inside the repository.\n` +
  `- Targets: one target per published table, figure, or named value (ids T01, T02, ...), with ` +
  `n_values where countable. Where a deposit carries a precomputed reference file that the paper's ` +
  `values come from, name it in published_values_source. Supplementary tables and figures count.\n` +
  `- Enumeration check: count display items with a reproducible command (for example pdftotext ` +
  `piped to grep for caption patterns over the paper and each supplement), quote the exact command ` +
  `in enumeration_check.method, and reconcile the count against targets plus exclusions.\n` +
  `- Eligibility: study_team_coauthorship is "yes" only if an author is study personnel — the ` +
  `study's sole registrant is Shawn Ross (ORCID 0000-0002-6492-9025); say "unknown" if you ` +
  `cannot tell.\n` +
  `- ${blindingBlock(p.slug)}`

log(`run ${run_id}: ${papers.length} planner spawn(s), effort pinned ${effort}, ` +
    `launch commit ${launch_commit.slice(0, 12)}`)

phase('Plan')
const results = await parallel(papers.map(p => () =>
  agent(planPrompt(p), { agentType: agent_type, effort, label: `plan ${p.slug}`, phase: 'Plan', schema })
    .then(v => (v === null ? null : { slug: p.slug, plan: v }))))

const returned = results.filter(Boolean)
const missing = papers.filter(p => !returned.some(r => r.slug === p.slug)).map(p => p.slug)
const escalates = returned.filter(r => r.plan.status === 'ESCALATE')
log(`${returned.length}/${papers.length} plans returned; ${escalates.length} ESCALATE; ` +
    `missing: ${missing.join(', ') || 'none'}. Next: reproduction-lane.py persist-plans, ` +
    `then batched approval.`)
return {
  run_id,
  launch_commit,
  effort,
  missing,
  escalates: escalates.map(r => ({ slug: r.slug, reason: r.plan.escalate_reason })),
  summary: returned.map(r => ({
    slug: r.slug,
    status: r.plan.status,
    targets: (r.plan.verification_targets || []).length,
    flag_for_human: (r.plan.enumeration_check || {}).flag_for_human === true,
  })),
}
