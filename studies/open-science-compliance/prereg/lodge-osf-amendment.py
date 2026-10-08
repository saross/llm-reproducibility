#!/usr/bin/env python3
"""Lodge a preregistration amendment on OSF as a versioned registration update.

This scripts the route that amendments 1 and 2 followed by hand (the
amendment-2 draft's status block; the archived lodgement session of
2026-08-17). The Open Science Framework (OSF) Application Programming
Interface (API) stores each version of a registration as a "schema
response". An amendment is a new schema response whose Summary field is the
previous version's Summary with the amendment appended under a dated
banner. The Digital Object Identifier (DOI) does not change.

Two modes:

- ``plan`` reads only, needs no credentials, and changes nothing. It fetches
  the latest approved version anonymously, composes the new Summary, runs
  every check that can run before writing, and saves the composed text and a
  report to ``--out``.
- ``lodge`` runs ``plan`` again (the registration may have changed), then
  creates the revision, writes the Summary and the revision justification,
  and verifies what OSF stored. Only if every check passes does it submit
  and approve the revision, which makes it public, and then verify the
  public copy anonymously. A failed check stops it before submission and
  leaves an unsubmitted revision that only the registrant can see.

OSF stores literal ``<`` and ``>`` as HTML entities and renders them back
correctly (amendment 2's record calls this "the registry's known write
transform"). The checks compare against that transformed text.

Usage:
    python3 lodge-osf-amendment.py plan <artefact.txt> <justification.txt> \
        <amendment-number> <date> --out <dir>
    OSF_API_KEY=... python3 lodge-osf-amendment.py lodge <same arguments>

Example:
    python3 lodge-osf-amendment.py plan osf-amendment-3.txt \
        osf-amendment-3-justification.txt 3 2026-10-08 --out /tmp/osf-plan
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

API = "https://api.osf.io/v2"
REGISTRATION = "dqnhg"  # DOI 10.17605/OSF.IO/DQNHG
SEPARATOR = "=" * 40  # the separator amendments 1 and 2 were lodged under


def entity_form(text: str) -> str:
    """Return the text as OSF stores it: ``<`` and ``>`` as HTML entities.

    Example:
        >>> entity_form("post > pre")
        'post &gt; pre'
    """
    return text.replace("<", "&lt;").replace(">", "&gt;")


def banner_line(amendment: int, date: str) -> str:
    """The banner heading an amendment inside the Summary field."""
    return f"AMENDMENT {amendment} ({date})"


def compose_summary(previous: str, artefact: str, amendment: int, date: str) -> str:
    """Append the artefact to the previous Summary under the dated banner.

    Args:
        previous: The latest approved Summary, exactly as OSF returned it.
        artefact: The unwrapped paste artefact.
        amendment: The amendment number.
        date: The lodgement date, which must match the artefact's own banner.

    Returns:
        The Summary to send.

    Raises:
        ValueError: if the amendment is already present, the previous
            amendment is missing, or the artefact names another date.

    Example:
        >>> compose_summary("Body.\\n\\nAMENDMENT 1 (d1)\\n\\nA1.", "Amendment 2 lodged d2; x",
        ...                 2, "d2").endswith("AMENDMENT 2 (d2)\\n\\nAmendment 2 lodged d2; x")
        True
    """
    if f"AMENDMENT {amendment} (" in previous:
        raise ValueError(f"amendment {amendment} is already in the Summary")
    if amendment > 1 and f"AMENDMENT {amendment - 1} (" not in previous:
        raise ValueError(f"amendment {amendment - 1} is not in the Summary")
    if f"Amendment {amendment} lodged {date};" not in artefact.split("\n", 1)[0]:
        raise ValueError(f"the artefact's banner does not say amendment {amendment} "
                         f"lodged {date}")
    return (previous + "\n\n" + SEPARATOR + "\n\n" + banner_line(amendment, date)
            + "\n\n" + artefact.rstrip("\n"))


def request(method: str, path: str, token: str | None = None,
            payload: dict | None = None) -> dict:
    """Make one OSF API request and return the decoded JSON body.

    Raises:
        SystemExit: on an HTTP error, after printing OSF's response.
    """
    headers = {"Content-Type": "application/vnd.api+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(f"{API}/{path}", data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as response:
            return json.load(response)
    except urllib.error.HTTPError as exc:
        sys.exit(f"{method} {path}: HTTP {exc.code} {exc.read().decode()[:600]}")


def latest_approved() -> tuple[str, str]:
    """Return the id and Summary of the newest approved version, anonymously."""
    listing = request("GET", f"registrations/{REGISTRATION}/schema_responses/")["data"]
    newest = listing[0]
    if newest["attributes"]["reviews_state"] != "approved":
        sys.exit(f"the newest revision {newest['id']} is "
                 f"{newest['attributes']['reviews_state']}, not approved; resolve it first")
    body = request("GET", f"schema_responses/{newest['id']}/")
    return newest["id"], body["data"]["attributes"]["revision_responses"]["summary"]


def check(results: list[tuple[str, bool]], name: str, passed: bool) -> None:
    """Record and print one named check."""
    results.append((name, passed))
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}")


def plan(args: argparse.Namespace) -> tuple[str, str, str]:
    """Compose and check the new Summary without writing anything to OSF.

    Returns:
        The previous version's Summary, the Summary to send, and the
        justification.
    """
    artefact = Path(args.artefact).read_text(encoding="utf-8")
    justification = Path(args.justification).read_text(encoding="utf-8").strip()
    previous_id, previous = latest_approved()
    try:
        new = compose_summary(previous, artefact, args.amendment, args.date)
    except ValueError as exc:
        sys.exit(f"refused: {exc}")
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "previous-summary.txt").write_text(previous, encoding="utf-8")
    (out / "new-summary.txt").write_text(new, encoding="utf-8")
    print(f"latest approved version {previous_id}: {len(previous)} characters")
    print(f"new Summary: {len(new)} characters ({len(new) - len(previous)} appended); "
          f"justification: {len(justification)} characters")
    results: list[tuple[str, bool]] = []
    check(results, "the artefact has no literal < or >, so OSF stores it unchanged",
          entity_form(artefact) == artefact)
    check(results, "the justification has no literal < or >", entity_form(justification)
          == justification)
    check(results, "the new Summary begins with the previous one, byte for byte",
          new.startswith(previous))
    if not all(passed for _, passed in results):
        sys.exit("plan failed; nothing was written")
    return previous, new, justification


def lodge(args: argparse.Namespace) -> None:
    """Create, write, verify, submit, and approve the revision, then verify it publicly."""
    token = os.environ.get("OSF_API_KEY")
    if not token:
        sys.exit("OSF_API_KEY is not set")
    previous, new, justification = plan(args)
    created = request("POST", "schema_responses/", token, {"data": {
        "type": "schema-responses",
        "relationships": {"registration": {"data": {"id": REGISTRATION,
                                                    "type": "registrations"}}}}})
    rid = created["data"]["id"]
    print(f"created revision {rid} ({created['data']['attributes']['reviews_state']})")
    patched = request("PATCH", f"schema_responses/{rid}/", token, {"data": {
        "id": rid, "type": "schema-responses",
        "attributes": {"revision_responses": {"summary": new},
                       "revision_justification": justification}}})
    attributes = patched["data"]["attributes"]
    stored = attributes["revision_responses"]["summary"]
    (Path(args.out) / "stored-summary.txt").write_text(stored, encoding="utf-8")
    results: list[tuple[str, bool]] = []
    check(results, "stored Summary equals the sent one under the entity transform",
          stored == entity_form(new))
    check(results, "the previous versions' text is preserved byte for byte",
          stored.startswith(previous))
    check(results, "the change set is exactly ['summary']",
          attributes.get("updated_response_keys") == ["summary"])
    check(results, "the justification was stored", attributes.get("revision_justification")
          == justification)
    if not all(passed for _, passed in results):
        sys.exit(f"verification failed: revision {rid} is unsubmitted and not public. "
                 "Inspect it, then fix or delete it before any retry.")
    for trigger in ("submit", "approve"):
        action = request("POST", f"schema_responses/{rid}/actions/", token, {"data": {
            "type": "schema-response-actions", "attributes": {"trigger": trigger},
            "relationships": {"target": {"data": {"id": rid, "type": "schema-responses"}}}}})
        print(f"{trigger}: {action['data']['attributes'].get('from_state')} to "
              f"{action['data']['attributes'].get('to_state')}")
        time.sleep(2)
    public_id, public = latest_approved()
    results = []
    check(results, "the newest approved version is the new revision", public_id == rid)
    check(results, "the anonymous copy equals the sent Summary under the entity transform",
          public == entity_form(new))
    print(f"version URL: https://osf.io/{REGISTRATION}?revisionId={rid}")
    if not all(passed for _, passed in results):
        sys.exit("public verification failed; the revision is public, so inspect it now")


def main() -> None:
    """Parse arguments and run the chosen mode."""
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("mode", choices=("plan", "lodge"))
    parser.add_argument("artefact")
    parser.add_argument("justification")
    parser.add_argument("amendment", type=int)
    parser.add_argument("date")
    parser.add_argument("--out", required=True, help="directory for the composed texts")
    args = parser.parse_args()
    if args.mode == "plan":
        plan(args)
        print("plan passed; nothing was written to OSF")
    else:
        lodge(args)


if __name__ == "__main__":
    main()
