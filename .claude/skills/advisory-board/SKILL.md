---
name: advisory-board
description: Stress-tests an artefact, claim, term, paper, briefing, strategy, or deck against Working Complexity's standing 24-member international advisory board (US, China, Germany, Japan — six system-native stakeholders each, the Future of ILD cast). Use whenever Mike says "test this with an advisory board", "run it past the board", "what would the advisory board think", "stress-test this with the board", "get the board's reaction", "take this to the advisory board", or any similar request to convene the board. The whole point is member consistency: always the same 24 named people, with fixed roles and worldviews, loaded from the bundled roster. Also use before publishing anything that quotes or references the advisory board, to check member details are consistent.
---

# Working Complexity advisory board

A standing instrument: the same 24 people, every time. When Mike asks to test
something "with an advisory board", convene this board and run a structured
session. Consistency of the members is the reason this skill exists — never
improvise the cast.

## The one hard rule

**Always load the members from [`references/board-roster.md`](references/board-roster.md) and use them exactly.**
Never invent, rename, drop, or merge a member. Never change anyone's role,
institution, system, or analytic lens. The board is exactly the 24 people in
that file — six each for the United States, China, Germany, and Japan. A member
may change their mind *within* a session (record it honestly), but their
standing role and worldview are fixed across all sessions.

If the roster file and the source HTML (`~/Documents/Claude/Projects/ILD/futureofILD/meet-the-board-*.html`)
ever disagree, reconcile the roster to the HTML before running the session, and
tell Mike you did.

This rule is about *who the members are* — name, role, institution, standing
worldview. It is fixed forever and is not affected by the continuity choice
below. What *does* vary session to session is whether a member's specific prior
commitments and session history carry forward — that's Step 0.

## Step 0 — Choose this session's continuity mode (ask every time)

Before convening the board, ask Mike how this session should relate to earlier
ones. Use the `AskUserQuestion` tool so it's an explicit choice, not an assumed
default — this matters because past sessions have drifted inconsistently
between "fresh reaction" and "the board remembers everything," sometimes within
the same document, and that drift is confusing to readers and occasionally
produces a duplicated commitment (see the ledger's data-quality notes). Offer:

1. **Fresh convening (hard reset).** No reference to any earlier session — no
   "last time," no session numbering, no claiming a relationship with the four
   citizens (Harold, George, Francis, Victor) beyond what this document itself
   introduces. The 24 members' fixed roles and worldviews from the roster still
   apply (that part never resets) — only *session memory* is dropped. Best for:
   a genuinely new question, a different disease area or market, or whenever
   carrying prior framing in would bias the read. (The China/Germany/Japan
   companion board run alongside the disease-modifying session is a working
   precedent for this mode — fully fresh, no borrowed continuity.)

2. **Standing cast, no commitment carryover.** The documented baseline. Same 24
   people and fixed worldviews, but write this as a clean reaction: no member
   claims a pledge from an earlier session is already "in motion," no session
   numbering, no "I raised this before" unless it is checked against
   `references/commitments-ledger.md` and actually true. **If Mike doesn't
   answer this question, run in this mode** — it's the safer default because it
   can't fabricate continuity it hasn't verified.

3. **Full continuity (managed).** Only when Mike explicitly wants a deliberate
   sequel building on a named prior session. Read
   [`references/commitments-ledger.md`](references/commitments-ledger.md) in
   full before writing anything. Every callback to a prior commitment must
   match a real entry in the ledger. If a member appears to be re-pledging
   something the ledger already shows as open or fulfilled, say so on the page
   ("Kowalski, you already committed to this in session 3 — status?") rather
   than writing it as a fresh pledge. Update the ledger afterwards — see Output.

Skip the question only if Mike's own request already states the mode
unambiguously (e.g. "run a completely fresh board on X" = mode 1; "follow up on
the Coming Loose session" = mode 3).

## What gets tested

The "thing under test" is whatever Mike points at — a finished artefact (paper,
briefing, report, deck, proposal), a single claim or term (e.g. "disease-modifying"),
a strategy, or a draft. If it is not obvious from context what to test, ask one
question to pin it down before convening the board. Read the artefact in full first.

## Running a session

1. **Frame what the board is reacting to.** One short passage in WC voice stating
   the artefact, claim, or question under test. If the thing under test is a raw
   term or idea rather than a written artefact, first write a short neutral briefing
   for the board to react to (this is what was done for "disease-modifying").

2. **Written pre-read reactions.** Each board reacts. Give analytic depth to the
   most relevant 2–3 voices per board, but every one of the 24 must be able to
   appear — for a full session, name and voice all 24. Each speaks in their own
   first-person register per the roster; never flatten them into one tone.

3. **Three structured rounds.** Opening positions → structured dialogue with honest
   revision (members challenge each other and change their minds on the record) →
   convergence and divergence. This is not a survey; it is an argument that moves.

4. **Cross-system contact.** Bring the four systems into direct contact on the
   sharpest claims, using the cross-board axes in the roster (value vs protection,
   surrogate scrutiny, price, reach). This four-machine comparison is the board's
   signature output — the same input does a different job in each system.

5. **Recorded commitments.** Close with concrete commitments in each member's own
   role, grouped by board plus a cross-system set. Record where members revised
   their opening positions. In mode 3, cross-check each new commitment against the
   ledger before presenting it as new (step 6 below explains how to write the update).

6. **Persona-honesty footer (mandatory).** End every session document with a note
   in this spirit: *the session was not a real meeting; the boards are AI-developed
   personas used as analytical instruments; the system mechanics are real and the
   positions are ones real people in these roles hold; the fiction is in the names,
   the substance is in the systems.* Never present the board as real people.

## Voice and brand

The members speak in their own voices. The WC narration around them (framing,
section headers, synthesis) follows the Working Complexity brand voice — read
`BRAND.md` §3 before writing: UK English, first person plural, sentence case, em
dashes, short paired statements; never "stakeholders" (name them), "simply",
"leverage", "unlock", "solution". Members may use system-native terms (AMNOG,
nanbyō, NRDL, DIP/DRG, Regress, Zusatznutzen, Chūikyō) — keep them; they are how
these people actually think.

## Output

Write a markdown session document at the repo root, named
`WC-<Topic>-Advisory-Board-Session.md` (e.g. `WC-Disease-Modifying-Advisory-Board-Session.md`).
For very large sessions the US board and the three international boards may be split
into two companion files, as was done for the disease-modifying exercise. After
writing, offer to render it as branded HTML or PDF, or to publish via the
`wc-site-publish` skill — but do not do so unless asked.

### Continuity ledger (mode 3 only)

After writing the session, append one entry per new commitment to
`references/commitments-ledger.md`, following the existing format (session,
date, member, commitment, status). Also:
- Add the new session to the numbered **Session log** at the top of the ledger.
- For any commitment that updates or fulfils an existing open entry, edit that
  entry's status in place rather than adding a parallel one — this is the step
  that prevents the Kowalski-style duplicate from recurring.
- If you corrected an in-document session-count claim (mode 3 sessions should
  state the right number, taken from the ledger's session log, not guessed),
  mention that you did so when reporting back to Mike.

Modes 1 and 2 do not touch the ledger at all.

## Scope notes

- Default roster is **all 24** (four boards). If Mike asks for a subset — "just the
  international board", "only Germany", "the US six" — name who is in the room but
  draw only from the canonical 24.
- Continuity behaviour (whether specific prior commitments carry over) is set by
  the Step 0 choice each session — see above. It is no longer assumed.
- The four WC patient personas (Harold, George, Francis, Victor) are not board
  members but are available as test cases — see the roster's closing note.

## Consistency checklist (run before delivering)

- [ ] Step 0 continuity mode was asked (or unambiguously inferred from Mike's request) and followed throughout.
- [ ] Every quoted member exists in `references/board-roster.md` with the exact name and role.
- [ ] No invented, renamed, or merged members; no drifted roles.
- [ ] Each member's stance is consistent with their standing lens (revisions noted as revisions).
- [ ] All four systems represented (unless Mike scoped a subset).
- [ ] Cross-system contact section present.
- [ ] Commitments grouped by board + cross-system.
- [ ] In mode 3, every "last time" or "previous session" callback matches a real ledger entry — none invented.
- [ ] In mode 3, the ledger was updated (new entries, statuses, session log) after writing.
- [ ] Persona-honesty footer present.
- [ ] WC brand voice in the narration (UK English, no banned words).
