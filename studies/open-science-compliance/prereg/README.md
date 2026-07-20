# OSF lodgement materials — Phase 2 preregistration

Submission-ready artefacts for the Open Science Framework (OSF) Open-Ended
Registration of the Phase 2 study. Convention modelled on the inscriptions
project (`~/Code/inscriptions/wiki/prereg/`): plain-prose paste files for OSF
form fields, PDF reading copies for upload, canonical markdown as the source
of truth. Located here (study-scoped) rather than in `wiki/` because this
repository hosts multiple studies.

## Artefacts

| File | Purpose |
|------|---------|
| `osf-registration-summary.txt` | Registration Summary (§1–§11 of the draft), plain prose with markdown emphasis stripped — paste into the Open-Ended Registration Summary field |
| `osf-project-metadata.txt` | Plain-text paste values for the project and registration metadata fields (title, description with commit pin, contributors, licence, subjects, tags) |
| `phase-2-preregistration-draft.pdf` | Reading copy of the full preregistration — upload alongside the canonical `.md` |
| `pilot-findings-report.pdf` | Reading copy of pilot findings report v1.2 — upload alongside the canonical `.md` |

## Canonical sources (upload the `.md` files as the frozen artefacts)

1. `../protocol/phase-2-preregistration-draft.md` (v0.7)
2. `../reports/pilot-findings-report.md` (v1.2)
3. `../protocol/study-protocol.md` (v1.0) — **markdown only, no PDF**: contains
   ✅/❌ status glyphs that xelatex silently drops, and a rendered copy that
   loses glyphs from an instrument document risks inverting meaning
4. `../../../extraction-system/prompts/06-infrastructure_pass6_prompt.md` —
   **markdown only, no PDF**, same glyph reasoning

## Regeneration

Plain-text summary: extract the `## Registration summary` section of the
draft, strip heading hashes, backticks, and emphasis markers (iterate bold
and italic substitution to a fixpoint — nested and line-wrapped spans need
it), as scripted in the git history of this directory. Then unwrap hard
line-breaks so each paragraph and each list item is a single flowing line —
OSF text boxes render pasted line-breaks literally, so wrapped source lines
break mid-sentence. Applies to every paste file in this directory
(`osf-registration-summary.txt`, `osf-project-metadata.txt`).

PDFs (pandoc 3.6.3 via Quarto's bundled binary, matching the inscriptions
house build):

```bash
/opt/quarto/bin/tools/x86_64/pandoc \
  -f markdown+autolink_bare_uris --pdf-engine=xelatex \
  -V geometry:margin=0.8in \
  -V mainfont="DejaVu Serif" -V monofont="DejaVu Sans Mono" \
  -V monofontoptions="Scale=0.78" \
  --include-in-header=header.tex \
  <source.md> -o <output.pdf>
```

where `header.tex` contains `\usepackage{xurl}`,
`\setlength{\emergencystretch}{3em}`, and `\sloppy`. DejaVu fonts (not the
inscriptions build's Latin Modern) because the preregistration's statistical
notation (α, δ, ≤, ≈) is outside Latin Modern's coverage and xelatex drops
missing glyphs silently — verify any rebuild with
`pdftotext <pdf> - | grep "α = 0.05"`.

## Lodgement checklist

- [x] Regenerate summary + PDFs if the draft changed since the last commit here
      (2026-07-20: upload set verified byte-identical to `ee3fda3`; PDFs
      glyph-checked via pdftotext)
- [ ] Upload the four canonical `.md` files plus the two PDFs to OSF Storage
- [ ] Record the repo commit hash in the OSF project description
- [ ] Tag the lodged commit: `git tag osf-prereg-phase2-<YYYY-MM-DD> && git push --tags`
- [ ] Registration: Open-Ended template; paste `osf-registration-summary.txt`;
      metadata from the draft's OSF metadata block; no embargo (public immediately)
