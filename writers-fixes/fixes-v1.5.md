---
title: Writer's fixes
version: 1.5
date: 2026-10-29
from: creative critic (up-creative-critic)
source-version: 3aa7377
covers: chapter 1 (draft v2.4)
status: Part A requested by Martin ("generate fixes file for chapter 1"): apply. Part C needs Martin's tick.
---

# Writer's fixes v1.5: chapter 1 (v2.4)

**Status: Part A applied 2026-10-29, commit f211d75. Part C awaits Martin's ticks. See applied-log.md.**

**What this is.** These are the fixes from the critic's review of chapter 1 v2.4. The redrafts of chapters 3 and 4 now carry beats that chapter 1 still gives away, and the chapter has one real-history timing error. **Part A** fixes chapter 1 and cuts about 70 words. **Part C** holds the options that need Martin's ruling.

The reasoning is in `up-creative-critic/reviews/chapters/2026-10-29-ch01-day-zero-v2.md`.

**How to use this**
- **Part A:** apply. Every Find string was checked by script against `3aa7377`. Each occurs exactly once, and they apply cleanly in sequence, with Part C's strings too.
- **Part C:** apply only the items Martin ticks.
- Then rebuild **chapter 1**, bump it to v2.5, log the result in `applied-log.md` against v1.5, and leave this file in place.

All edits are in `book/chapters/01-day-zero.md`.

---

## Part A — Chapter 1 (apply)

### A1. The reconnaissance flight's timing (~l. 173)
Find:
`A long way off, an aeroplane had flown that morning very high over an island and taken photographs that were even now being carried, in sealed canisters, towards people who would not sleep for thirteen days.`
Replace:
`A long way off, where it was still night, an aeroplane was flying very high towards an island, to take photographs for people who would not sleep for thirteen days.`
*Why:* the run over the island began at about 07:30 Eastern time on 14 October, which was about 12:30 in England (British Summer Time ran until 28 October 1962). At breakfast at Harrowgate the plane was still in the air, so the photographs weren't yet being carried. It's still backdrop only, with no real people named.

### A2. The driver's ending (~l. 37)
Find:
`He drove out between the raked lines of gravel and did not think about the house again for almost forty years. Then he thought about it every day.`
Replace:
`He drove out between the raked lines of gravel, and in the mirror the fog closed over the house.`
*Why:* in ch 3, Len now tells the driver's later life ("Then when he got old he never talked about anything else"), and ch 3 ends on "You notice it for forty years." The old line gave away the first and pre-echoed the second. It was also the chapter's second closing sting. Now the section ends on an image.

### A3. The Frenchman's foretold death (~l. 139)
Find (note the leading space):
` For the rest of his life, thirty-five years in a narrow house above the harbour at Le Havre, he would dream of those three notes.`
Replace with nothing, so the paragraph ends "…and went upstairs."
*Why:* ch 4 opens in "a narrow house above the harbour at Le Havre" and reveals the dream he has "never once described to anyone". This also brings ch 1 to one foretold death (THREE's "thirty-nine years she had left"), as the house rule requires.

### A4–A6. Simile cuts
Ch 1 has about 15 "as if / like / as though" similes. These three cuts remove repeated frames.

**A4** (~l. 55). Find:
`on the gravel for a long time, as if the valley were reluctant to let him go.`
Replace:
`on the gravel for a long time.`
*Why:* l. 19 already has "as if the valley".

**A5** (~l. 77). Find:
`The clerk from Rio held his arm across his chest as if he were cold.`
Replace:
`The clerk from Rio held his arm across his chest.`
*Why:* it's the second "as if" in one paragraph, after Tokyo's "as if at a funeral".

**A6** (~l. 123). Find:
`But that night it was brief, as though it were introducing itself, or measuring how much they could carry.`
Replace:
`But that night it was brief. It seemed to be measuring how much they could carry.`
*Why:* l. 25 already has "as though it were".

### A7–A9. Line edits
**A7** (~l. 73). Find:
`A sound she had heard all her working life was unmistakable when it arrived where it didn't belong.`
Replace:
`She had heard that sound all her working life, and it was never more unmistakable than where it didn't belong.`
*Why:* as written, the logic is slightly off: the sound is always unmistakable.

**A8** (~l. 35). Find:
`because something about the place wanted writing down:`
Replace:
`because the place seemed to want writing down:`
*Why:* one of ten uses of "something" in the chapter. The driver's note after the colon is unchanged, so it still matches Post #2 word for word.

**A9** (~l. 159). Find:
`Something frightens everyone in eight days, and it doesn't burn.`
Replace:
`Everyone will be frightened in eight days, and it doesn't burn.`
*Why:* the same "something" count. The American now echoes the counsel's wording more closely.

---

## Part C — Martin to tick

- [ ] **C1. "Never *we*" and the Day 203 counsel *NOT OURS*.** Ch 1 (~l. 169) says the voice never said *I*, "Never *we*, either", but the ch 12 counsel *GIVE EVERY FEAR A FACE THAT IS NOT OURS* is plural. **Tick one:**
  - [ ] **C1a (recommended; idea #7).** Keep ch 1 as it is. Add to the ch 12 brief in `book/outline.md`: *Nell notices, in one line and with no explanation, that NOT OURS is the only time the voice owns anything, and what it owns is not being blamed.* That gives the voice a progression: no *I* or *we* (1962), then *OURS* (1963), then the epilogue's *I*. About 30 words when ch 12 is drafted.
  - [ ] **C1b.** Cut it from ch 1. Find (note the leading space): ` Never *we*, either.` Replace with nothing.
- [ ] **C2. Give the dinner a live question** (~l. 61, about 20 words). Find: `found a discrepancy in the timings, which he mentioned.` Replace: `found a discrepancy in the timings: the programme listed a session on Sunday with no time against it. He mentioned it. Nobody knew what it meant.` *Why:* the dinner (about 620 words) is the chapter's slow stretch, and this gives it suspense that pays off at 02:10. It adds no new canon, since "needed from tomorrow" already implies the hosts knew.
- [ ] **C3. Optional cut** (~l. 117). Find: `In the morning he would be gone. ` (with the trailing space). Replace with nothing. *Why:* it tells ahead, and l. 153 shows it anyway. The Tokyo letters stay.
- [ ] **C4. Rewrite notes** for `book/outline.md` (Act One rewrite notes). These are plan notes, with no chapter text:
  - Len (ch 3) owns the driver's later life; don't restate it elsewhere.
  - Ch 4 owns the Frenchman's dream and his house above the harbour.
  - 02:10 is a motif (ch 1 contact, the ch 4 waking, D15 call 1), so keep the time exact everywhere.

---

## Cross-checks done
- **UP version:** HEAD was still `3aa7377` when this was issued, with no changes to ch 1 or the outline since the review.
- **Hard rules:** no new names, places, companies or events. The 1962 crisis stays backdrop only, with no real people named and the Tenants predicting it rather than causing it. No Tenant line changes. No use of "urban paranoia".
- **Other UP files:** Post #2 quotes only the driver's note, which is unchanged. Nothing in `content/`, `bible/`, the synopsis or the resolution map quotes the lines cut in A2 or A3. A2 also stops ch 1 pre-echoing ch 3's closing "forty years".
- **Other fixes files:** v1.0–v1.4 are applied, and none touches these lines in their v2.4 form. A3 completes the foretold-death rule (v1.2 C1) for ch 1, which v1.2 applied to ch 4 only.
- **After Part A (measured):** about 12 "as if / like / as though" similes remain and "something" falls to 8. Two "the way…" similes remain, within the cap.
- **Find strings:** A1–A9 and C1b–C3 each occur exactly once in `3aa7377`, checked by script, and they apply cleanly in sequence.

## Change log
- 1.5 (2026-10-29): first issue.
