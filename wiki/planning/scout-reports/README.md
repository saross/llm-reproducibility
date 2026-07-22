# Scout reports — 2026-07-07/08 stack-positioning sweep

Verified landscape reports positioning every component of the llm-reproducibility stack
against the state of the art. Each pipeline paired a literature scout (lit-scout agent,
citation-chained, DOI-grounded) with a prior-art scout (tools/repos/services), and every
run was adversarially verified by a fresh-context verifier re-querying each claim against
its authoritative source (CrossRef/OpenAlex/Semantic Scholar for papers; GitHub/PyPI/
Hugging Face APIs and live fetches for tools). Corrected tables are authoritative; each
file's header records the verification outcome.

**Start here:** [2026-07-08-stack-positioning-synthesis.md](2026-07-08-stack-positioning-synthesis.md)
— the cross-stack synthesis (position by lane, adopt/adapt list, competitive watch list,
verification meta-findings, follow-up queue).

| Pipeline | Literature report | Prior-art report |
|----------|-------------------|------------------|
| P1 Reproduction/replication | [p1 lit](2026-07-07-p1-reproduction-lit-verified.md) | [p1 prior-art](2026-07-07-p1-reproduction-prior-art-verified.md) |
| P2 CEM claims–evidence extraction | [p2 lit](2026-07-07-p2-cem-lit-verified.md) | [p2 prior-art](2026-07-07-p2-cem-prior-art-verified.md) |
| P3 RDMAP methods/designs/protocols | [p3 lit](2026-07-07-p3-rdmap-lit-verified.md) | [p3 prior-art](2026-07-07-p3-rdmap-prior-art-verified.md) |
| P4 Credibility / repliCATS | [p4 lit](2026-07-07-p4-credibility-lit-verified.md) | [p4 prior-art](2026-07-07-p4-credibility-prior-art-verified.md) |
| P5 FAIR / open-science compliance | [p5 lit](2026-07-08-p5-fair-lit-verified.md) | [p5 prior-art](2026-07-07-p5-fair-prior-art-verified.md) |
| P6 Literature/discourse engagement | [p6 lit](2026-07-08-p6-citation-lit-verified.md) | [p6 prior-art](2026-07-07-p6-citation-prior-art-verified.md) |

**arXiv/preprint follow-up sweep (2026-07-08)** — covers the DOI pipeline's blind spot
(CrossRef-invisible 2024–2026 preprints), grounded via the arXiv Atom API + Semantic
Scholar with DataCite DOIs (`10.48550/arXiv.*`):

| Sweep | Report | Covers |
|-------|--------|--------|
| S1 Citation integrity/coverage preprints | [s1 arXiv](2026-07-08-s1-citation-integrity-arxiv-verified.md) | P6 lane gap (30 rows, 150/150 verified) |
| S2 Protocol/methods-extraction preprints | [s2 arXiv](2026-07-08-s2-protocol-extraction-arxiv-verified.md) | P3 lane gap (27 rows, 135/135 verified) |

**Deeper-chaining round + guard pass (2026-07-08, approved go/no-gos):**

| Run | Report | Headline |
|-----|--------|----------|
| C1 Competitor watch (Fraser/Thelwall/Serghiou forwards) | [c1](2026-07-08-c1-competitor-watch-chains-verified.md) | No direct rival; nearest threats named (Chakravorti 2026; Zhu 2026 pair); speed-to-publish now |
| C2 Citation-integrity toolchain (Schreieder/CiteAudit/Sarol) | [c2](2026-07-08-c2-citation-toolchain-chains-verified.md) | Accuracy engine off-the-shelf; CitaLaw the lone non-STEM analogue |
| C3 CEM/RDMAP lineages (Carriero/ReplicatorBench/Laï-king/Micropub) | [c3](2026-07-08-c3-cem-rdmap-chains-verified.md) | 7 competitor flags; appropriateness niche has zero citers |
| G1 Archaeology guard pass (OSF/grey literature) | [g1](2026-07-08-g1-archaeology-guard-null-result.md) | Documented null (26 queries); first-mover claim holds scoped + "to our knowledge" |

**Routing-design review pass (2026-07-22)** — prior-art scout against the agent
content-routing design's §7 open questions, adversarially verified (110 claims,
107 confirmed, 0 corrected, 3 declared-null):

| Run | Report | Headline |
|-----|--------|----------|
| Routing-design prior art | [routing prior-art](2026-07-22-routing-design-prior-art-verified.md) | Harness-native `skills:` push answers §7.1/§7.5; subagent cold-cache caveat (issue #29966) means census cost gate must not assume caching; deterministic-sweep + narrow-LLM-triage screener shape well supported |

The companion implementation review lives in
[`../reviews/2026-07-22-routing-design-implementation-review.md`](../reviews/2026-07-22-routing-design-implementation-review.md).

Provenance notes: proposer drafts and BibTeX exports live under the session scratchpad and
`/tmp/lit-scout-*` (transient); the verified reports here are the durable record. The
sweep was interrupted once by a session usage limit (2026-07-08 ~00:30–03:30 AEST); four
agents were relaunched after reset and their reruns are noted in the affected file headers.
