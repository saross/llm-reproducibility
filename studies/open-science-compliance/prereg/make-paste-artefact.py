#!/usr/bin/env python3
"""Build an OSF paste artefact from an amendment draft's lodged portion.

Open Science Framework (OSF) text boxes render pasted line-breaks literally
and do not render markdown, so the lodged portion of an amendment draft is
converted to plain flowing prose before it is pasted into the registration's
Summary field. This script does the conversion that earlier amendments did
by hand, following the conventions the lodged amendment-2 artefact
(``osf-amendment-2.txt``) set:

- the portion between ``## Amendment text`` and ``## Decisions for the
  registrant`` is taken, and nothing else;
- heading hashes, backticks, and emphasis markers are stripped, emphasis
  iterated to a fixpoint because nested and line-wrapped spans need it;
- angle-bracketed autolinks become bare URLs;
- the section sign becomes the word ("§5(c)" to "section 5(c)", "§§2–3" to
  "sections 2–3"), and the draft's two arrows become words, as in
  amendment 2 ("unscoreable-scores-0", "v2.1 to v2.2");
- the registrant-decision markers (``[D-n]`` and ``[D-n, ruled]``) are
  removed, since they belong to the drafting record, not the lodged text;
- a one-line registration banner is prepended, naming the lodgement date
  and the repository tag.

Tables are refused outright: they do not survive a plain-text paste (README,
"Tables: avoid entirely"). So is any repository tag in the text that differs
from the banner's, such as a ``<date>`` placeholder or a tag left at an
earlier lodgement date: the lodged text names its own tag, and the two must
agree. The result still has hard line-breaks; run
``unwrap-paste-file.py`` on it afterwards, and check that word, bullet, and
numbered-line counts are unchanged by the unwrap.

Usage:
    python3 make-paste-artefact.py <draft.md> <out.txt> <lodgement-date>

Example:
    python3 make-paste-artefact.py amendment-3-draft.md osf-amendment-3.txt 2026-10-07
    python3 unwrap-paste-file.py osf-amendment-3.txt
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

START_HEADING = "## Amendment text (draft for the OSF field)"
END_HEADING = "## Decisions for the registrant before lodgement"

# Earlier amendments' lodgement dates, for the banner. Each is the date the
# amendment was lodged through the OSF API (README; the amendment drafts'
# checklists).
PRIOR_LODGEMENTS = (
    "Registration: Phase 2 preregistration, DOI 10.17605/OSF.IO/DQNHG, "
    "lodged 2026-07-20, public 2026-07-21; amendment 1 lodged 2026-08-03; "
    "amendment 2 lodged 2026-08-17."
)

# Word forms for the draft's arrows, in the order they are tried. The first
# is amendment 2's own rendering of the same phrase.
ARROW_FORMS = (
    ("unscoreable → 0", "unscoreable-scores-0"),
    (" → ", " to "),
)

DECISION_MARKER = re.compile(r" ?\[D-\d+(?:, ruled)?\]")


def lodged_portion(draft: str) -> str:
    """Return the text between the amendment-text and decisions headings.

    Args:
        draft: The full amendment draft.

    Returns:
        The lodged portion, without its own heading or the closing rule.

    Raises:
        ValueError: if either heading is missing, or a table row is found.
    """
    try:
        start = draft.index(START_HEADING)
        end = draft.index(END_HEADING)
    except ValueError as exc:
        raise ValueError("the draft lacks the amendment-text or decisions heading") from exc
    body = draft[start:end].split("\n", 1)[1]
    body = re.sub(r"\n---\s*$", "\n", body.rstrip() + "\n")
    if re.search(r"^\s*\|", body, flags=re.M):
        raise ValueError("a table row is in the lodged portion; convert it to prose first")
    return body


def to_plain(body: str) -> str:
    """Convert markdown in the lodged portion to plain OSF prose.

    Args:
        body: The lodged portion, as markdown.

    Returns:
        Plain text, still hard-wrapped.

    Raises:
        ValueError: if an arrow remains that has no word form.

    Example:
        >>> to_plain("### 2. Rule\\n\\nSee §5(c) and **this** `x`. [D-2, ruled]\\n")
        '2. Rule\\n\\nSee section 5(c) and this x.\\n'
    """
    body = DECISION_MARKER.sub("", body)
    body = re.sub(r"^#{1,6}\s+", "", body, flags=re.M)
    body = re.sub(r"<(https?://[^>]+)>", r"\1", body)
    body = body.replace("`", "")
    previous = None
    while previous != body:
        previous = body
        body = re.sub(r"\*\*(.+?)\*\*", r"\1", body, flags=re.S)
        body = re.sub(r"(?<!\w)\*(?!\s)(.+?)(?<!\s)\*(?!\w)", r"\1", body, flags=re.S)
    body = body.replace("§§", "sections ").replace("§", "section ")
    for arrow, words in ARROW_FORMS:
        body = body.replace(arrow, words)
    if "→" in body:
        raise ValueError("an arrow without a word form remains; add one to ARROW_FORMS")
    return re.sub(r"\n{3,}", "\n\n", body)


def check_tags(body: str, amendment: int, date: str) -> None:
    """Refuse any tag for this amendment that is not the banner's tag.

    Args:
        body: The plain lodged text.
        amendment: The amendment number.
        date: The lodgement date the banner names.

    Raises:
        ValueError: if the text names this amendment's tag with another date
            or a placeholder.

    Example:
        >>> check_tags("at tag osf-amendment-3-2026-10-08.", 3, "2026-10-08")
    """
    expected = f"osf-amendment-{amendment}-{date}"
    # A tag runs to the first space or closing punctuation; the trailing
    # full stop of a sentence is not part of it.
    for tag in re.findall(rf"osf-amendment-{amendment}-[^\s),;]+", body):
        if tag.rstrip(".") != expected:
            raise ValueError(f"the text names {tag}, not the banner's {expected}")


def banner(date: str, amendment: int) -> str:
    """The registration banner line that opens the paste artefact."""
    return (f"{PRIOR_LODGEMENTS} Amendment {amendment} lodged {date}; artefact set "
            f"at repository tag osf-amendment-{amendment}-{date}.\n\n")


def main(argv: list[str]) -> int:
    """Write the paste artefact; return a process exit status."""
    if len(argv) != 4:
        print(__doc__.split("Usage:")[1].split("Example:")[0].strip(), file=sys.stderr)
        return 2
    draft, out, date = Path(argv[1]), Path(argv[2]), argv[3]
    match = re.search(r"amendment-(\d+)", draft.name)
    if not match:
        print(f"cannot tell the amendment number from {draft.name}", file=sys.stderr)
        return 2
    amendment = int(match.group(1))
    try:
        body = to_plain(lodged_portion(draft.read_text(encoding="utf-8")))
        check_tags(body, amendment, date)
    except ValueError as exc:
        print(f"refused: {exc}", file=sys.stderr)
        return 1
    out.write_text(banner(date, amendment) + body.lstrip("\n"), encoding="utf-8")
    print(f"wrote {out}: {len(body.split())} words in the lodged portion")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
