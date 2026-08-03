export const meta = {
  name: 'fair-benchmark-arm',
  description: 'One validation-benchmark arm: 5 pilot papers x 3 runs of FAIR scoring',
  phases: [{ title: 'Score' }],
}
const { agentType, arm, papers, schema } = (typeof args === "string" ? JSON.parse(args) : args)
// The registered schema file carries a document-version field (E4 carrier);
// the runtime validator is strict JSON Schema, so strip non-standard keywords
// from the copy handed to agents.
delete schema.version
const tasks = []
for (let run = 1; run <= 3; run++) {
  for (const p of papers) tasks.push({ run, slug: p.slug, path: p.path })
}
log(`arm ${arm}: ${tasks.length} scoring spawns (5 papers x 3 runs)`)
const results = await parallel(tasks.map(t => () =>
  agent(
    `Benchmark scoring task (preregistered validation phase, arm ${arm}, run ${t.run} of 3).\n` +
    `Paper: ${t.slug}. Source (read in full): ${t.path}\n` +
    `Score this paper on the pushed FAIR instrument exactly per your agent brief. ` +
    `The paper PDF is the sole paper source: supplementary files are deliberately not provided; ` +
    `apply the data-completeness coverage procedure from the paper's own statements and content. ` +
    `Independence requirement: do NOT read any file under studies/ or outputs/ in the repository - ` +
    `your scores must not depend on any persisted assessment. ` +
    `Set paper_slug to "${t.slug}".`,
    { agentType, label: `${t.slug} r${t.run}`, phase: 'Score', schema }
  ).then(v => ({ arm, run: t.run, slug: t.slug, result: v }))
))
const ok = results.filter(Boolean)
log(`arm ${arm}: ${ok.length}/${tasks.length} spawns returned`)
return { arm, count: ok.length, results }
// Provenance: exact script that ran all three 2026-08-03 benchmark arms
// (workflow runs wf_9fcbff61-646, wf_4eaecf54-890, wf_627102d7-fa0),
// rescued from session-local storage at handoff so the §2 remediation
// re-run can use an identical harness. Args shape: {agentType, arm,
// papers: [{slug, path}], schema} — see the arm run-records for values.
