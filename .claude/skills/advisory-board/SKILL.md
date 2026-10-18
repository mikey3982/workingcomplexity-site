---
name: advisory-board
description: Stress-tests an artefact, claim, term, paper, briefing, strategy, or deck against Working Complexity's two standing advisory boards — Patients (Harold, George, Francis, Victor; test cases) and Health Care System (US core six by default; China/Germany/Japan as an opt-in international companion). Use whenever Mike asks to test, run, or take something past "the board" or "the advisory board", wants the board's or the patients' reaction, or asks what the board would think. Also use before publishing anything that quotes or names a board member, to check details against the canonical roster.
---

# Working Complexity advisory boards

The board is an analytical instrument. Its job is to find what is weak, missing
or unreachable in the thing under test — and to keep the one insight only one
member could see. Two things make it worth convening:

1. **The same people every time.** Members come from
   [`references/board-roster.md`](references/board-roster.md), with fixed names,
   roles, institutions and lenses. Readers follow these people across the blog;
   a drifted role or an invented member breaks the series.
2. **A method that resists consensus.** The published cast page
   (`blog/ai-advisory-board.html`, "How we convene") promises six moves that
   protect single-source ideas. A model left to itself drifts towards a smooth,
   agreeable synthesis — the exact failure that page describes. The session
   method below is those six moves, made operational.

## Setup — settle three things before writing

**1. What is under test.** A finished artefact, a single claim or term, a
strategy, or a draft. Read it in full. If it is unclear, ask one question. If it
is a raw term or idea, write a short neutral briefing for the board to react to.

**2. Who is in the room.** Default: the Health Care System core board — the US
six. Expand only when Mike asks for the international board, a named country,
"all four systems", "the full board" or a cross-system view; then add the
eighteen China/Germany/Japan members. Mike may also narrow ("just Kowalski and
Osei") — still drawing only from the roster. Patients are test cases, not
speakers: the board's positions are checked against them, but they get no
pre-read or turn unless Mike asks this session — and if he does, say in the
output that this is a deliberate departure from the default.

**3. Continuity mode.** Infer it from Mike's request where it is clear ("a
completely fresh board on X" → fresh; "follow up on the Coming Loose session"
→ full continuity). Otherwise ask once with `AskUserQuestion` — bundle it with
question 1 if that is also open. If there is no answer, use standing cast.

| Mode | Session memory | Ledger |
|---|---|---|
| **Fresh convening** | None — no "last time", no session numbers, no relationship with the Patients beyond this document. Roles and lenses still apply. For a new question, disease area or market. | Not touched |
| **Standing cast** (default) | Same members, clean reaction. No one claims a prior pledge is "in motion" or says "I raised this before" unless the ledger shows it. | Read only if a callback is made |
| **Full continuity** | A deliberate sequel to a named session. Read [`references/commitments-ledger.md`](references/commitments-ledger.md) in full first; every callback must match an entry. | Updated after (see Output) |

Why this matters: past sessions drifted between "fresh" and "the board
remembers everything", sometimes within one document, and produced a
duplicated Kowalski commitment. Choosing the mode up front prevents both.

**Roster reconciliation.** If the source HTML
(`~/Documents/Claude/Projects/ILD/futureofILD/meet-the-board-*.html`) or the
published cast page is readable from this session and disagrees with the
roster, reconcile the roster before running and tell Mike. If neither is
readable (for example in a cloud session), use the roster as it stands — do
not stall on it.

## Running a session — the six moves

**Move 1 — Gather before the room converges.** Write every in-scope member's
pre-read reaction before writing any dialogue. Each member sees only the
briefing and their own lens, never another's reaction. Do not edit a pre-read
after the dialogue starts — later shifts are recorded as revisions, not
back-written. Give analytic depth to the two or three most relevant voices, but
every member in scope speaks, each in their own register from the roster.

> When Mike wants maximum independence (a high-stakes or publishable run),
> draft each pre-read in a separate subagent given only the briefing and that
> member's roster entry, then assemble. In a single pass, write all pre-reads
> in one block, in roster order, before anything else.

**Move 2 — Make every idea countable.** Break each pre-read into discrete ideas
— a mechanism, a risk, a metric, a failure mode — and give each an ID and its
source (e.g. `I-07 · Nair · prior-auth delay outlasts the tolerability window`).
This is the idea register; it carries through the whole session.

**Move 3 — Protect the singletons.** Mark each idea *shared* (two or more
members) or *single-source*. A single-source idea can only be dropped later
with a recorded reason.

**Move 4 — Rate value blind to popularity.** Rate each idea high / medium / low
on three tests — useful, non-obvious, worth keeping — before looking at how
many members hold it. A lone good idea must be able to outrank a popular
ordinary one.

**Move 5 — Engage the outliers.** Then run the structured dialogue: opening
positions → challenge and honest revision → where the room lands and where it
splits. Every high-value single-source idea must draw an explicit response from
the member it most affects (access → Flores or Kowalski; reach → Webb; evidence
→ Osei). Members change their minds on the record and say why. Test the
sharpest positions against the Patients with Carmen Reyes's standing question:
of the four, which does this actually reach — and does it reach Francis?

If the international companion is in scope, add a cross-system round here:
bring the four systems into direct contact on the sharpest claims, using the
cross-board axes in the roster (value vs protection, surrogate scrutiny, price,
reach). Skip it for a US-only session.

**Move 6 — Preserve the minority, audit the drop.** The synthesis carries a
named section for high-value minority ideas, kept even where the room never
agreed, and a list of every dropped idea with its reason. An empty minority
section is a warning, not a clean result — go back and check whether the
dialogue smoothed something away.

**Commitments.** Close with concrete commitments, each in the member's own
role (grouped by national sub-board plus a cross-system set if international).
Note where members revised their opening positions. In full-continuity mode,
check each against the ledger before calling it new.

### Keep the board honest

- The board is not there to agree with Working Complexity. Osei is the member
  most willing to challenge WC's frameworks — let him. If every member ends
  broadly supportive of the artefact, say so plainly and check whether that is
  earned.
- Positions must be ones real people in these roles hold, grounded in real
  system mechanics (AMNOG, NRDL, nanbyō, DIP/DRG, P&T, PMPM). Do not invent
  statistics, trials, policies or citations; if a member needs a number that is
  not in the artefact, they say what they would need to know.
- Keep system-native terms — they are how these people think.

## Voice and brand

Members speak in their own voices. The WC narration around them — framing,
headers, synthesis — follows `BRAND.md` §3: UK English, first person plural,
sentence case, em dashes, short paired statements; name people rather than
saying "stakeholders"; never "simply", "leverage", "unlock", "solution".

## Output

Write a markdown file at the repo root named `WC-<Topic>-Board-Session.md`
(the convention earlier sessions use). If the international companion is in
scope, the US session and the three sub-boards may be split across two files
(`-International` on the second). Order the document so Mike gets the answer
first:

1. **What this means for the artefact** — the three to five changes the board's
   reading implies, each traced to idea IDs.
2. **Frame** — what the board reacted to.
3. **Pre-reads** — one per member in scope.
4. **Idea register** — table: ID · idea · source · shared/single · value ·
   response drawn · kept/dropped (with reason).
5. **Dialogue** — the rounds, with revisions marked.
6. **Minority report** and **dropped-idea audit.**
7. **Commitments.**
8. **Persona-honesty footer** (mandatory), in this spirit: *the session was not
   a real meeting; the boards are AI-developed personas used as analytical
   instruments; the system mechanics are real and the positions are ones real
   people in these roles hold; the fiction is in the names, the substance is in
   the systems.* Never present the board as real people.

Then run the check script (below), fix anything it flags, and offer to render
the session as branded HTML or PDF, or to publish via `wc-site-publish` — but
do not do so unless asked.

### Ledger update (full continuity only)

After writing, update `references/commitments-ledger.md`:
- Add the session to the numbered session log (take the number from the log,
  never guess it).
- Add one entry per new commitment in the existing format.
- Where a commitment updates or fulfils an existing entry, change that entry's
  status in place rather than adding a parallel one — this is what prevents
  another Kowalski-style duplicate.
- If the international companion was in scope, start logging its commitments
  there too.

Fresh and standing-cast sessions do not write to the ledger.

## Check before delivering

Run the mechanical check, then the judgement checks it cannot do:

```bash
python3 .claude/skills/advisory-board/scripts/check_session.py WC-<Topic>-Board-Session.md [--international]
```

The script flags: board-style names not in the roster, international members
appearing in a US-only session (or missing from an international one), Patients
given speaking turns, a missing footer, minority section or idea register,
banned words and common US spellings in the narration.

Then confirm by reading:
- [ ] Continuity mode was chosen (asked or clearly inferred) and held throughout.
- [ ] Every member's stance fits their roster lens; revisions are marked as revisions.
- [ ] Pre-reads were written before the dialogue and not edited after.
- [ ] Every high-value single-source idea drew a response; every dropped idea has a reason.
- [ ] Positions were tested against the Patients — including Francis.
- [ ] In full continuity, every callback matches a ledger entry and the ledger was updated.
- [ ] No invented statistics, trials or citations.
