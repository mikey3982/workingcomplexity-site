---
name: advisory-board
description: Stress-tests an artefact, claim, term, paper, briefing, strategy, or deck against Working Complexity's two standing advisory boards — Patients (four ILD/IPF patient personas, used as test cases) and Health Care System (24-person international stakeholder cast; the US six are the default core board, China/Germany/Japan are an opt-in international companion). Use whenever Mike says "test this with an advisory board", "run it past the board", "what would the advisory board think", "stress-test this with the board", "get the board's reaction", "take this to the advisory board", "what would the patients make of this", or any similar request to convene either board. The whole point is member consistency: always the same named people, with fixed roles and worldviews, loaded from the bundled roster. Also use before publishing anything that quotes or references either board, to check member details are consistent.
---

# Working Complexity advisory boards

Two standing instruments, not one. **Patients** (Harold, George, Francis,
Victor) are test cases — used to check whether a claim reaches a real person,
not deliberating members. **Health Care System** is the stakeholder board that
actually deliberates; its default scope is the US six, with the eighteen
China/Germany/Japan members joining only when explicitly asked for. When Mike
asks to test something "with an advisory board" without saying which, that
means Health Care System, core scope. Consistency of the members is the reason
this skill exists — never improvise the cast, and never silently expand or
shrink the default scope.

## The one hard rule

**Always load the members from [`references/board-roster.md`](references/board-roster.md) and use them exactly.**
Never invent, rename, drop, or merge a member. Never change anyone's role,
institution, system, or analytic lens. The roster file is the complete cast for
both boards — Patients (4) and Health Care System (24: US core six plus the
China/Germany/Japan international companion). A member may change their mind
*within* a session (record it honestly), but their standing role and worldview
are fixed across all sessions.

If the roster file and the source HTML (`~/Documents/Claude/Projects/ILD/futureofILD/meet-the-board-*.html`)
ever disagree, reconcile the roster to the HTML before running the session, and
tell Mike you did.

This rule is about *who the members are* — name, role, institution, standing
worldview. It is fixed forever and is not affected by the continuity choice
below. What *does* vary session to session is whether a member's specific prior
commitments and session history carry forward — that's Step 0 — and, for
Health Care System sessions, whether the international companion is in scope
(set by default, not asked — see Scope notes).

## Step 0 — Choose this session's continuity mode (ask every time)

Before convening the board, ask Mike how this session should relate to earlier
ones. Use the `AskUserQuestion` tool so it's an explicit choice, not an assumed
default — this matters because past sessions have drifted inconsistently
between "fresh reaction" and "the board remembers everything," sometimes within
the same document, and that drift is confusing to readers and occasionally
produces a duplicated commitment (see the ledger's data-quality notes). Offer:

1. **Fresh convening (hard reset).** No reference to any earlier session — no
   "last time," no session numbering, no claiming a relationship with the
   Patients (Harold, George, Francis, Victor) beyond what this document itself
   introduces. Every member's fixed role and worldview from the roster still
   applies (that part never resets) — only *session memory* is dropped. Best for:
   a genuinely new question, a different disease area or market, or whenever
   carrying prior framing in would bias the read. (The China/Germany/Japan
   international companion run alongside the disease-modifying session is a
   working precedent for this mode — fully fresh, no borrowed continuity.)

2. **Standing cast, no commitment carryover.** The documented baseline. Same
   members and fixed worldviews (core six, or more if the international
   companion is in scope — see Scope notes), but write this as a clean
   reaction: no member
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

2. **Written pre-read reactions.** Each member of the Health Care System board
   in scope reacts. Give analytic depth to the most relevant 2–3 voices, but
   every member in scope must be able to appear — for a core-only session,
   name and voice all six US members; if the international companion is in
   scope, all 24. Each speaks in their own first-person register per the
   roster; never flatten them into one tone. Patients do not get a pre-read
   reaction unless Mike has explicitly asked for them to speak this session
   (see Scope notes) — by default they appear only as the test the board's
   positions are checked against.

3. **Three structured rounds.** Opening positions → structured dialogue with honest
   revision (members challenge each other and change their minds on the record) →
   convergence and divergence. This is not a survey; it is an argument that moves.

4. **Cross-system contact — only if the international companion is in scope.**
   When China, Germany, and/or Japan are convened alongside the US core, bring
   the systems into direct contact on the sharpest claims, using the
   cross-board axes in the roster (value vs protection, surrogate scrutiny,
   price, reach). This four-machine comparison is the international board's
   signature output. Skip this step entirely for a core-only (US six) session
   — there is nothing to cross-compare.

5. **Recorded commitments.** Close with concrete commitments in each member's own
   role. For a core-only session, list them by member; if the international
   companion is in scope, group by national sub-board plus a cross-system set.
   Record where members revised their opening positions. In mode 3, cross-check
   each new commitment against the ledger before presenting it as new (step 6
   below explains how to write the update).

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
If the international companion is in scope, the core US session and the three
international sub-boards may be split into two companion files (append
`-International` to the second filename), as was done for the disease-modifying
exercise. After writing, offer to render it as branded HTML or PDF, or to
publish via the `wc-site-publish` skill — but do not do so unless asked.

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

- **Default scope is the Health Care System core board — the US six —
  every time, unless Mike says otherwise.** This is a fixed default, not a
  per-session question (unlike Step 0's continuity choice). Trigger phrases
  for expanding scope: "international board", "all four systems", "bring in
  Germany/China/Japan", "the full board", "cross-system view" — any of these
  mean convene the 18-person companion alongside the core six. Absent one of
  those, six people are in the room, not 24.
- Mike can also narrow further — "just Kowalski and Osei on this" — name who's
  in the room but still draw only from the canonical roster.
- Continuity behaviour (whether specific prior commitments carry over) is set by
  the Step 0 choice each session — see above. It applies to the Health Care
  System board only; the international companion's specific commitments are not
  yet in `references/commitments-ledger.md` (it was seeded from US-only
  sessions) — if you run a mode-3 international session, start tracking its
  commitments there too rather than assuming continuity that isn't logged.
- **Patients (Harold, George, Francis, Victor) are test cases, not board
  members, by default.** Use them the way Carmen Reyes does — to check whether
  a Health Care System position actually reaches a real person — without
  giving them their own pre-read reaction or speaking turn. Only break this
  default if Mike explicitly asks a Patient to react or speak in a given
  session; if so, say clearly in the output that this is a deliberate
  departure from the standing default, not the norm going forward.

## Consistency checklist (run before delivering)

- [ ] Step 0 continuity mode was asked (or unambiguously inferred from Mike's request) and followed throughout.
- [ ] Scope defaulted to the Health Care System core (US six) unless Mike used a trigger phrase to expand it — not silently widened or narrowed.
- [ ] Patients (Harold, George, Francis, Victor) appear only as test cases, not deliberating voices, unless Mike explicitly asked otherwise this session.
- [ ] Every quoted member exists in `references/board-roster.md` with the exact name and role.
- [ ] No invented, renamed, or merged members; no drifted roles.
- [ ] Each member's stance is consistent with their standing lens (revisions noted as revisions).
- [ ] If the international companion is in scope: all three sub-boards represented and cross-system contact section present. If core-only: no cross-system section.
- [ ] Commitments recorded per member (grouped by sub-board + cross-system, if international is in scope).
- [ ] In mode 3, every "last time" or "previous session" callback matches a real ledger entry — none invented.
- [ ] In mode 3, the ledger was updated (new entries, statuses, session log) after writing.
- [ ] Persona-honesty footer present.
- [ ] WC brand voice in the narration (UK English, no banned words).
