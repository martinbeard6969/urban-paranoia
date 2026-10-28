---
title: Writer's fixes
version: 1.2 (revised: reader-panel fixes folded in)
date: 2026-10-26
from: creative critic (up-creative-critic)
source-version: 5aa6758 (after v1.2 Parts A–B were applied in 9b52ee4)
covers: chapters 1–6 and Post #2; from the whole-book re-review and the reader-panel assessment of 26 Oct 2026
supersedes: the first issue of v1.2 (same day). Replace that file with this one.
status: Parts A–B already applied (record only). Part P is new: apply it. Part C needs Martin's tick.
---

# Writer's fixes v1.2 (revised)

**What changed in this revision.** Martin asked for the reader-panel fixes to be folded into v1.2 rather than issued as v1.3. Parts A and B of the first issue were already applied (`9b52ee4`), so they're kept below **as a record only**. The panel fixes are a new **Part P**, checked against the current text (`5aa6758`). Part C carries the original two style items, corrected and widened, plus four new tick items from the panel.

The reasoning is in two critic files:
- `up-creative-critic/reviews/whole-work/2026-10-26-rereview-ch01-06.md`
- `up-creative-critic/reviews/whole-work/2026-10-26-reader-panel-assessment.md`

**How to use this**
- **Parts A and B:** already applied. Don't reapply.
- **Part P:** apply. Every Find string was checked by script against `5aa6758` and occurs exactly once.
- **Part C:** apply only the items Martin ticks.
- Then rebuild **chapters 1, 4, 5 and 6** (plus 2 if C3 is ticked), log the result in `applied-log.md` against this revision, and leave the file in place.

---

## Parts A and B — Already applied in `9b52ee4` (record only)

| Item | What | Status |
|---|---|---|
| A1 | Ch 5: thread paragraph moved after the "Which is always." exchange | ✓ applied |
| A2 | Ch 1: "It didn't seem to matter yet." | ✓ applied |
| A3 | Ch 4: "until the boxes came" | ✓ applied |
| A4 | Ch 6: the goods-in sentence, one colon | ✓ applied |
| A5 | Ch 3: "Anyone old enough remembers that autumn" | ✓ applied |
| B1–B7 | Seven "the way…" cuts (ch 2, 3, 5, 6) | ✓ applied |

**Critic's corrections to the first issue** (the writer's applied-log was right on both counts):
- Ch 3's "the way" count after B4 is **5**, not 4. My earlier figure didn't count one non-simile use. No missed cut.
- "His face did the thing" occurs **twice** (ch 5 ×1, ch 6 ×1), not three times. My count included Ama's "she did the thing almost nobody can do". C2 below is corrected.

---

## Part P — Reader-panel fixes (apply)

### P1. Chapter 5: settle Jack's name (panel: "Jack becoming Jordan without warning")

The casual reader didn't know which name to hold onto. With A1 applied, the name joke now runs unbroken; one plain line after it settles the matter before the thread paragraph.

File: `book/chapters/05-the-sensible-voice.md`

**Find:**

```
"Which is always."

"Which is always."

What I'd glanced at
```

**Replace with:**

```
"Which is always."

"Which is always."

He stayed Jack to me.

What I'd glanced at
```

### P2. Date corrections (panel: hard-SF reader; all three confirmed by the critic)

Oct 1962 to March 1971 is **8 years, 4 months** (to 2 March: 8 years, 4 months and 16 days), not eight and a half. The seminar runs Saturday to Monday, which is **two** nights. The 03:12 edit (~27 April) to 19 May is about **three** weeks.

| # | File | Find | Replace with |
|---|---|---|---|
| P2a | `book/chapters/01-day-zero.md` | `It invited her to a residential seminar, three nights, all expenses met,` | `It invited her to a residential seminar, two nights, all expenses met,` |
| P2b | `book/chapters/03-reconciliation.md` | `And somebody had still been counting, carefully, eight and a half years later.` | `And somebody had still been counting, carefully, eight years and four months later.` |
| P2c | `book/chapters/04-not-far-only-elsewhere.md` | `Eight and a half years. The field had been frightened` | `Eight years, four months and sixteen days. The field had been frightened` |
| P2d | same file | `a dream he had had perhaps a thousand times in eight and a half years` | `a dream he had had perhaps a thousand times in eight years` |
| P2e | `book/chapters/06-count-forwards.md` | `Three and a half weeks. It had sat there for three and a half weeks under my own words` | `Three weeks. It had sat there for three weeks under my own words` |
| P2f | same file (author's notes) | `and sat unnoticed for about three and a half weeks` | `and sat unnoticed for about three weeks` |
| P2g | `content/phase-1/post-02-day-zero.md` | `Eight and a half years later, perhaps the same machine came back out` | `Eight years and four months later, perhaps the same machine came back out` |

P2c gives THREE the exact count a demographer would keep. P2d leaves the actuary's rounding loose, as a non-counter's would be.

### P3. Chapter 6: say why 144 lb is eerie (panel: casual reader)

File: `book/chapters/06-count-forwards.md`

**Find:**

```
*144 LB.*

I rang Danny.
```

**Replace with:**

```
*144 LB.*

As if one machine had been carried out of that house and the same weight of machine set down beside my desk.

I rang Danny.
```

This is Nell's image, not a claim. Danny's "heavy office kit is heavy office kit" still answers it, and canon decision D5's reveal ("the server *was* the new teletype") stays for ch 23.

### P4. Chapter 4: introduce terms gently, and cut one foretold death (panel: "too many names and terms", 4 of 6; "the narrator tells how people will die")

Ch 4 brings in *counsel, the Long Room, the Table, the Listening Room* and *the Founders*, all canon names, without a gloss. Keep every name, but explain each one at first use. And of the two foretold deaths in ch 4, keep the piano dealer's and cut THREE's.

File: `book/chapters/04-not-far-only-elsewhere.md`

| # | Find | Replace with |
|---|---|---|
| P4a | `After that the counsel had told them other things` | `After that the machine's advice (the counsel, they called it now, as if it were a lawyer) had told them other things` |
| P4b | `The Long Room had thirteen chairs now.` | `The long dining room, where four places had once stayed clean, had thirteen chairs now. They called it the Long Room.` |
| P4c | `on the nights the Table met:` | `on the nights the twelve of them met as the Table:` |
| P4d | `Only the three of them were in the Listening Room. That was the rule now, for the old machine: the Founders, and nobody else.` | `Only the three of them were in the small panelled room, which the others called the Listening Room. That was the rule now, for the old machine: the three who had stayed in 1962, the Founders, and nobody else.` |
| P4e | (author's notes) `*"The machine would not print again for fifty-five years. By then she would have been dead for twenty-five of them."* (1971 + 55 = 2026; THREE dies in 2001.)` | `*"The machine would not print again for fifty-five years."* (1971 + 55 = 2026.) The death clause was cut in fixes v1.2 (panel: foretold deaths).` |

**P4f.** The sentence in P4e also appears in the chapter text, so use this two-paragraph anchor.

**Find:**

```
and would be kept.

The machine would not print again for fifty-five years. By then she would have been dead for twenty-five of them.
```

**Replace with:**

```
and would be kept.

The machine would not print again for fifty-five years.
```

P4b ties the Long Room back to ch 1's dining table, "still set for seven". **Same paragraph as P2c:** P4a and P2c are both in the "Eight and a half years…" paragraph. Their Find strings don't overlap, so apply both.

### P5. Chapter 5: trim the Wharf Road exposition (panel: "ch 5 is a catalogue", 4 of 6)

File: `book/chapters/05-the-sensible-voice.md`

**Find:**

```
His mum did two cleaning jobs, he said, mornings at an office and evenings at a hotel, and in between she worried. Their flat was on the Wharf Road estate. The council had sent a letter about a regeneration scheme in partnership with a private developer, and a list of blocks to be demolished in phase one, and theirs was on it. Nobody could tell them where they'd go, or when, or whether they'd ever afford to come back.
```

**Replace with:**

```
His mum did two cleaning jobs, he said, and in between she worried. Their block on the Wharf Road estate was on the council's list for demolition, for a regeneration scheme with a private developer, and nobody could tell them where they'd go, or whether they'd ever afford to come back.
```

The private developer (secretly a Larkspire fund) and the demolition list both stay. Jack's next line ("*Consultation*… Means they've decided.") still follows naturally.

---

## Part C — Martin to tick

### Style rules
- [ ] **C1. Similes, stings and foretold deaths** (widened from the first issue). Add to `CLAUDE.md` § "Voice & style": `**Restraint devices:** at most two "the way…" similes per chapter (interludes avoid Nell's "the way you'd…" habit); at most one closing aphorism or "sting" per chapter; at most one foretold death per interlude.`
- [ ] **C2. Retire Danny's tic** (count corrected). In `bible/voices.md`, under Danny: `"His face did the thing" is used up (ch 5, ch 6). Find a new tell for him from ch 7.`

### Date labels at time jumps (panel: the casual reader "counted on his fingers")
- [ ] **C3.** Add section labels where a chapter jumps in time. The builder already supports them (`LABEL = ^\*\*([^*a-z]+)\*\*$`). Each goes on its own line directly after the `---` that opens the section:
  - Ch 2, before `The archive was in a storage unit by the old rail yard`: `**APRIL 2026**`
  - Ch 5, before `On Saturday he walked me to the Mission Hall.`: `**SATURDAY 16 MAY**`
  - Ch 6, before `The letter came on the Saturday.`: `**SATURDAY 23 MAY**`

  Then note them in the outline's narrator-labels table. Keep the day-counts in the chapter labels: ch 2's 22,861 pays off for close readers in ch 6.

### Outline notes (`book/outline.md`; no chapter text yet)
- [ ] **C4. Ch 8 makes the best case for the plan.** Add to the ch 8 entry: `Crane's overnight arithmetic should be an argument a reasonable reader could half-accept (the panel's literary-political and thriller readers want "a reasoned villain"). It is the book's strongest case for the plan, made before anyone answers it.`
- [ ] **C5. One false clue in Act Two.** Add under Act Two: `At least one clue leads nowhere or the wrong way and costs Nell time (e.g. Graham's grey door, ch 6 → 7). The panel found the trail "interlocking a little too neatly".`
- [ ] **C6. Give the blamed a voice (critic's idea #5).** Add to ch 20 (or 17): `A member of the family behind the rainbow (ch 5–6) gets a full scene and speaks for themselves: specific, funny, not a spokesperson. A person, never a category; no real group named.`

---

## Cross-checks done

| Check | Result |
|---|---|
| Part P vs the applied A1–A5 and B1–B7 | No overlap. P1 anchors on A1's new order; nothing else touches an applied sentence. ✓ |
| P1, P5 (ch 5) | Separate paragraphs. P1's line is plain, not a hindsight tease. ✓ |
| P2c vs P4a (same ch 4 paragraph) | Different sentences; apply both. ✓ |
| P2d vs A3 (ch 4 Le Havre) | Different paragraphs. ✓ |
| P2e, P2f, P3 (ch 6) vs A4, B7 | Five distinct places. P3 anchors on the second `*144 LB.*` (followed by "I rang Danny."). ✓ |
| P2b (ch 3) vs A5, B4 | Different paragraphs. ✓ |
| P4 vs canon names (bible: Long Room, Listening Room, Founders, the Table) | All names kept; only glossed. ✓ |
| P4f vs the ch 24 setup | "Would not print again for fifty-five years" kept. ✓ |
| P2g | The ARG's Post #2 is corrected to match the book. ✓ |
| P3 vs canon decision D5 | Image only; the reveal stays in ch 23. ✓ |
| C3 vs the builder | Labels match the `LABEL` regex. ✓ |
| Hard rules | No content risk. C6 has its guard written in. ✓ |
| All Part P Find strings | Script-checked against `5aa6758`; each occurs once. ✓ |

---

## Change log

| Version | Date | By | Change |
|---|---|---|---|
| 1.0 | 2026-10-26 | Creative critic | First issue (applied in `a9ea277`). |
| 1.1 | 2026-10-26 | Creative critic | Chapter 6 fixes, idea #4 (applied in `2dd2f71`). |
| 1.2 | 2026-10-26 | Creative critic | Re-review issues #1–6 (Parts A–B applied in `9b52ee4`; C1–C2 awaiting tick). |
| 1.2 rev. | 2026-10-26 | Creative critic | Reader-panel fixes folded in at Martin's request as Part P. C1 widened, C2 count corrected, C3–C6 added. |
