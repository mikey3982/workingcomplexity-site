#!/usr/bin/env python3
"""Mechanical consistency check for an advisory board session document.

Usage: check_session.py SESSION.md [--international]

Reads the canonical roster next to this script and reports problems a model
tends to miss when writing a long multi-voice document. Exit code 1 if any
ERROR is found; WARN lines are for review only.
"""
import re
import sys
from pathlib import Path

ROSTER = Path(__file__).resolve().parent.parent / "references" / "board-roster.md"
PATIENTS = ["Harold", "George", "Francis", "Victor"]
TITLES = r"(?:Dr|Prof\.?|Professor|Director|President|Mr|Ms|Mrs|Deputy Director)"
BANNED = ["simply", "leverage", "leveraging", "unlock", "unlocks", "stakeholder",
          "stakeholders", "solution", "solutions"]
US_SPELLINGS = ["organization", "center", "centers", "behavior", "analyze",
                "analyzed", "color", "favor", "prioritize", "recognize",
                "modeling", "pediatric", "fiber"]


def load_roster():
    members = {}  # surname -> (id, full line)
    for line in ROSTER.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\*\*((US|CN|DE|JP)-\d) · ([^*]+)\*\*", line)
        if not m:
            continue
        mid, name = m.group(1), m.group(3)
        name = re.sub(r"\s*\(.*?\)", "", name).split(",")[0]
        name = re.sub(rf"^{TITLES}\s+(Dr\s+)?(med\.\s+)?", "", name).strip()
        surname = name.split()[-1]
        # Chinese names are family-name first: Li Wenjuan -> Li
        if mid.startswith("CN"):
            surname = name.split()[0]
        members[surname] = (mid, name)
    return members


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    international = "--international" in sys.argv
    if len(args) != 1:
        print(__doc__)
        return 2
    text = Path(args[0]).read_text(encoding="utf-8")
    members = load_roster()
    errors, warns = [], []

    # 1. Titled names that are not on the roster.
    known_words = set(members) | {w for _, n in members.values() for w in n.split()}
    for m in re.finditer(rf"\b{TITLES}\s+((?:Dr\s+)?[A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)", text):
        words = m.group(1).replace("Dr ", "").split()
        if not any(w in known_words for w in words):
            errors.append(f"Unknown titled name not in roster: '{m.group(0)}'")

    # 2. Scope: international members present / absent.
    present = {mid for s, (mid, _) in members.items() if re.search(rf"\b{s}\b", text)}
    intl = sorted(p for p in present if not p.startswith("US"))
    if not international and intl:
        errors.append(f"International members in a US-only session: {', '.join(intl)} "
                      "(pass --international if Mike asked for them)")
    if international:
        missing = sorted(mid for mid, _ in members.values()
                         if mid not in present and not mid.startswith("US"))
        if missing:
            errors.append(f"International session missing members: {', '.join(missing)}")
    us_missing = sorted(mid for mid, _ in members.values()
                        if mid.startswith("US") and mid not in present)
    if us_missing:
        warns.append(f"US core members not mentioned: {', '.join(us_missing)} "
                     "(fine only if Mike narrowed the room)")

    # 3. Patients given speaking turns.
    for p in PATIENTS:
        if re.search(rf"^\s*(?:#{{1,6}}\s*{p}\b|\*\*{p}\s*:|\*\*{p}\b[^*\n]*\*\*\s*[:—-])", text, re.M):
            warns.append(f"{p} looks like a speaker heading — Patients are test cases "
                         "unless Mike asked for them to speak")

    # 4. Required sections.
    lower = text.lower()
    if "fiction is in the names" not in lower and "not a real meeting" not in lower:
        errors.append("Persona-honesty footer missing")
    if "minority" not in lower:
        errors.append("Minority report section missing (Move 6)")
    if "idea register" not in lower and not re.search(r"\bI-\d{2}\b", text):
        errors.append("Idea register missing (Move 2)")
    if not re.search(r"dropped|drop audit|cut,? and why", lower):
        warns.append("No dropped-idea audit found (Move 6)")

    # 5. Brand words and spellings (quotes from US members may be exempt).
    for w in BANNED:
        n = len(re.findall(rf"\b{w}\b", text, re.I))
        if n:
            warns.append(f"Banned word '{w}' ×{n} — fine only inside a member's own quote")
    for w in US_SPELLINGS:
        n = len(re.findall(rf"\b{w}\b", text, re.I))
        if n:
            warns.append(f"US spelling '{w}' ×{n} — narration must be UK English")

    for e in errors:
        print("ERROR", e)
    for w in warns:
        print("WARN ", w)
    if not errors and not warns:
        print("OK — no issues found")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
