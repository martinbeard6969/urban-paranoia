---
title: Writer's fixes
version: 1.1
date: 2026-10-26
from: creative critic (up-creative-critic)
source-version: 41f2c5f
covers: chapters 1–5, Dead Drop 01, ARG launch playbook, outline/synopsis length
status: applied 2026-10-26 (all parts; Martin ticked all of Part D)
---

# Writer's fixes v1.0

**Status: applied 2026-10-26, commit a9ea277. See applied-log.md.**

For the writing agent. Full reasoning is in the critic's reviews (`up-creative-critic/reviews/`, 26 Oct 2026). Every "Find" string below has been checked against commit `41f2c5f` and occurs exactly once in its file.

**How to use this**
- **Part A:** approved by Martin. Apply it.
- **Part B:** factual and continuity errors. Apply all of them unless Martin strikes one.
- **Part C:** line polish. Apply unless Martin strikes one.
- **Part D:** craft changes. Apply **only** the ones Martin ticks `[x]`.
- After applying, rebuild the chapter PDFs (`python3 tools/build_chapter.py book/chapters/<file>.md`). Record what was applied in the change log at the bottom, and bump the version (v1.1 for partial application, v2.0 for the next review round).

---

## Part A — Approved: the book is a full novel (70,000–80,000 words)

Ruling: Martin, 26 Oct 2026.

| # | File | Change |
|---|---|---|
| A1 | `book/outline.md` frontmatter | `target-length: ~40,000 words (novella upper limit for SF awards; see "Length" below)` → `target-length: full-length novel, 70,000–80,000 words (see "Length" below)` |
| A2 | `book/outline.md` § Length | Remove the novella rationale. Keep *"grow by expanding Act Two, not by adding plot."* New act budgets: **Act One ~22,000–24,000 · Act Two ~26,000–30,000 · Act Three ~22,000–26,000** (≈2,300–2,700 words a chapter). Interludes ~1,400–2,000; key chapters (1, the Wall, 26, 30) ~3,000–5,000. |
| A3 | `book/outline.md` act headings | Update "(chapters 1–10, ~13,500 words)", "(chapters 11–20, ~13,500 words)" and "(chapters 21–30, ~13,000 words)" to the budgets in A2. |
| A4 | `book/synopsis.md` frontmatter | `medium: novel (novella-length first book)` → `medium: novel` |
| A5 | `README.md` | Update any length reference in the status section. |
| A6 | Drafted chapters | **No changes for length alone.** Chapters 1–5 already fit this pace. |

---

## Part B — Factual and continuity errors (apply)

| # | File | Find | Replace with | Why |
|---|---|---|---|---|
| B1 | `book/chapters/01-day-zero.md` | `A young clerk from a central bank in Rio` | `A young clerk from the currency office in Rio` | Brazil's central bank wasn't founded until Dec 1964. |
| B2 | `book/chapters/02-contribution-to-the-transition.md` | `On my last day at the desk, a Thursday in March,` | `One Thursday in March,` | It contradicts "In three weeks there would be nobody at this desk", and the March letter that follows. |
| B3 | `book/chapters/03-reconciliation.md` | `then day one was 3,062 days before it.` | `then day nought was 3,062 days before it.` | Off by one: the next line says Day 0. |
| B4 | `book/chapters/03-reconciliation.md` | `I had nine days of notice left` | `I had six days of notice left` | Counted from Fri 24 Apr, her notice ends ~30 Apr (D5, continuity review). |
| B5 | `book/chapters/03-reconciliation.md` | `Somebody had started counting the day the world held its breath.` | `Somebody had started counting a week before the world held its breath.` | 14 Oct 1962 is eight days before the crisis became public. This is more accurate and echoes ch 1's forecast. It stays backdrop only. |
| B6 | `book/chapters/04-not-far-only-elsewhere.md` | `Harrowgate, the second of March, 1971. The fog was the same.` | `The fog was the same.` | It duplicates the narrator label directly above it (visible in the PDF). |
| B7 | `content/phase-2/dead-drop-01-6b6e70.md` (Fragment Four) | `the machine was not connected to any line` | `the machine was not connected to any supply` | Ch 1 (cable to the wall plate), ch 3 ("WITH LINE CONNECTION") and ch 4 ("THE LINE IS OPEN") all say it *had* a line. It had no power. |
| B8 | `marketing/arg-launch-playbook.md` §7 | `how a "is this real?" campaign` | `how an "is this real?" campaign` | Grammar. The PDF already has it right. |

---

## Part C — Line polish (apply unless struck)

| # | File | Find | Replace with | Why |
|---|---|---|---|---|
| C1 | `book/chapters/01-day-zero.md` | `By about four o'clock she had noticed` | `By four that morning she had noticed` | It's in the breakfast scene, so it briefly reads as 4 p.m. |
| C2 | `book/chapters/01-day-zero.md` | `his face did something she would spend a long time afterwards trying to describe.` | `his face did something she never found the words for.` | This is the second "trying to describe a face" in the chapter. |
| C3 | `book/chapters/02-contribution-to-the-transition.md` | `on a firm that has never moved a paperclip for free` | `from a firm that has never moved a paperclip for free` | Preposition. |
| C4 | `book/chapters/03-reconciliation.md` | `my back informed me in no uncertain terms that I was thirty-eight` | `my back reminded me I was thirty-eight` | Stock phrase. |
| C5 | `book/chapters/05-the-sensible-voice.md` | `the kind that comes round to check meters and photograph damp` | `the kind that comes round to photograph damp and never fix it` | Letting agents don't read meters, and the new line adds character. |
| C6 | `book/chapters/05-the-sensible-voice.md` | `It sounded madder than it did on the page, and also, somehow, more real.` | `It sounded madder out loud than on the page, and more real.` | Cuts a hedge and a doubled "it did". |

---

## Part D — Craft changes (Martin to tick)

Each item is a recommendation, not canon. Tick `[x]` to approve. The writer applies only ticked items.

### Chapter 1
- [ ] **D1. Don't spoil ch 4.** Delete: `He played them on his piano once, in 1971, and was so frightened by what he had done that he closed the lid and never opened it again.` The sentence before it stays. Ch 4 then owns the piano reveal.
- [ ] **D2. The seven cars.** Foreign guests driving themselves (one came by train) is odd. Make them seven identical hire cars arranged by the Institute (one sentence in the driver's opening). The driver's note stays as it is.
- [ ] **D3. Replace the national stereotypes** for the German, Tokyo and Rio guests with one specific, non-national detail each (as the Delhi sheep calculation does). Keep the German's *"Doubts. Very well organised."*
- [ ] **D4. Echo Fragment Four.** `Later, when she did say it and the American told her exactly that, she would insist that it be written down.` → `Later, when she said it and the American told her it was not the most pressing point, she insisted it be minuted.`

### Chapter 2
- [ ] **D5. Early pull.** One hindsight sentence in the first section, so the reader knows the archive is coming. For example: *"It was the archive that did it, in the end. But I'll come to the archive."*
- [ ] **D6. Danny's line.** `They used to make me sign half of them.` → `I used to sit across the table from the men who signed them.` As written, it suggests Danny signed tax dodges.
- [ ] **D7. One weather simile, not two** (the contractor paragraph and "true in the way that weather reports are true"). Keep one.

### Chapter 3
- [ ] **D8. Nell's own deduction.** After Len mentions Old Tommy's "man with no face", one line where Nell connects two drivers, twenty years apart, describing the same man.

### Chapter 4
- [ ] **D9.** `in something sensible and German` → `in the same grey saloon he'd driven in 1962, now with a dent he had measured`
- [ ] **D10. The container berth** (idea #1). One sentence or a short paragraph: from the actuary's window, the new container berth stands where the dock gangs used to. It's a real trend described accurately, with no real dispute named.

### Chapter 5
- [ ] **D11. Cut the issue density.** Keep the meter queue, the boarded window and Wharf Road. Fold the payday lender and job club into one glance, and cut the noticeboard to two items. Saves ~200 words.
- [ ] **D12. The bird logo.** Give Nell a reason not to place it (the van's bird is stylised differently, or *"half the logos in the world are birds"*). She calls it "my bird-logo coaster" in ch 2.
- [ ] **D13. The name leak costs something.** Later in the chapter @longweather_ is the first to use "Nell" (no "I" in its voice).
- [ ] **D14. Danny's three-week gap.** One line: he texted *tax dodge x* the morning after ch 2; this is the first time he's read the posts.
- [ ] **D15. The anniversary.** Sunday 17 May is a year since go-live. Add one line ("A year ago today, the croissants.").
- [ ] **D16. Seed Jack's anger.** Let Nell glimpse something on his screen (invented, vague, fictional) that Clearfell can use in ch 16.
- [ ] **D17. Ama's back room** pays off in ch 17 (idea #2). Note it in `book/outline.md` ch 17.

### ARG and marketing
- [ ] **D18. Align Post #2 with ch 5.** In the book, Danny reveals Nell's name by commenting after **both** posts. In Post #2, Nell quotes D. after Post #1. Recommended: change Post #2 to "D. left a comment…". Nothing is published yet.
- [ ] **D19. Archivist's voice.** `MS OKAFOR-REYES` → `MS OKAFOR REYES` (full stops only), or log the hyphen as an exception in `bible/voices.md`.
- [ ] **D20. Pitch pack.** `[Chapter 1](../book/chapters/01-day-zero.md), polished.` → chapters **1–3**, polished (typical UK agent submission; check each agent's guidelines).
- [ ] **D21. Sign-up from week 0.** Add an out-of-world "Get the book first" sign-up to every `/about` page.
- [ ] **D22. Week-8 buying-intent survey.** Add it to the playbook (§3 W8 and §8 log).
- [ ] **D23. Privacy for "What's your Day?".** Calculate in the browser only; store and send nothing. The share card shows the Day number, never the birth date.
- [ ] **D24. One source of truth** for the pilot plan: build `outputs/arg-pilot-plan.pdf` from `marketing/arg-launch-playbook.md`, or mark the PDF as a dated snapshot.
- [ ] **D25. HG-68 transcript** for deaf players (in-world, typed beneath the player).

### Audio and production
- [ ] **D26. A contrast-bed promo** of the three tones (~6–8 s): hiss and a clock, true silence under the tones, then hiss again. Keep the clean 3 s file as well.
- [ ] **D27. Sound-mark check:** confirm G–E♭–G doesn't closely match a known broadcaster's, transport operator's or device sound (rule 3).
- [ ] **D28. Hyphenation** in `tools/build_chapter.py` (or ragged-right review copies) to fix loose justified lines.

---

## Change log

| Version | Date | By | Change |
|---|---|---|---|
| 1.0 | 2026-10-26 | Creative critic | First issue: Part A approved; B–D from the 26 Oct review pass. |
| 1.1 | 2026-10-26 | Writing agent | All parts applied (commit `a9ea277`). Changes from the file as issued: B7 "the mains"; D9 reworded to fit D2; D16 thread described, not quoted. Details in `applied-log.md`. |
