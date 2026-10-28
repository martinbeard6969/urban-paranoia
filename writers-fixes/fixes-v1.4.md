---
title: Writer's fixes
version: 1.4
date: 2026-10-28
from: creative critic (up-creative-critic)
source-version: da4c126
covers: chapter 2 (draft v3.0); notes for the rewrite of chapters 3 onwards
status: Part A requested by Martin ("generate fixes file"): apply. Part C needs Martin's tick.
---

# Writer's fixes v1.4: chapter 2 (v3.0) and notes for the rewrite

**Status: applied 2026-10-28, commits 4df7431 (Part A) and b5a4f3a (Part C, all ticked). See applied-log.md.**

**What this is.** These are the fixes from the critic's review of chapter 2 v3.0. That review was redrafted on the basis that chapters 3 onwards will be rewritten. **Part A** fixes chapter 2 itself. **Part C** turns what chapter 2 now commits the rewrite to into notes for the outline's revision briefs, so the new chapters are drafted against them rather than corrected afterwards.

The reasoning is in `up-creative-critic/reviews/chapters/2026-10-28-ch02-contribution-to-the-transition-v3.md`.

**How to use this**
- **Part A:** apply. Every Find string was checked by script against `da4c126` and occurs exactly once.
- **Part C:** apply only the items Martin ticks.
- Then rebuild **chapter 2**, log the result in `applied-log.md` against v1.4, and leave the file in place.

---

## Part A — Chapter 2 (apply)
`book/chapters/02-contribution-to-the-transition.md`

### A1–A3. The sting rule (v1.2 C1: at most one closing aphorism per chapter)
v3.0 ends about seven sections on an aphorism. These three cuts, with A4, leave three: "I don't know what I'd circle", "They wanted the person they were letting go to decide what to keep" and the lantern. "He was right about everything" stays as a character line. If Martin would rather keep it as a sting, cut one of the other three.

**A1.** Find:
`*Nimfold's pushing an update tonight. The cloud's slow in the mornings.* It was everywhere and nowhere, and it had my job.`
Replace:
`*Nimfold's pushing an update tonight. The cloud's slow in the mornings.*`

**A2.** Find:
`The fish arrived on time. Nobody said thank you, because nobody knew.`
Replace:
`The fish arrived on time.`

**A3.** Delete this paragraph and the blank line after it:
`It was the least important document in the building. It was the first thing in a year that had needed me.`
*Why:* it repeats "I was the only person alive who could have noticed" from two paragraphs earlier, and cutting it runs the find straight into the plastic sleeve and the red light.

### A4. Continuity: Danny's van and kettle
Find:
`He answered on the second ring, still in the van, the engine ticking as it cooled.`
Replace:
`He answered on the second ring, just in from the van, still in his jacket.`
*Why:* a few lines later "The click of a kettle." puts him at home.

### A5. The dictionary and the coaster
Find:
`at the kitchen table, under my father's dictionary and beside my bird-logo coaster, and started a blog.`
Replace:
`at the kitchen table, opposite my father's dictionary and beside my rent-statement coaster, and started a blog.`
*Why:* the dictionary is on "the shelf opposite" earlier in the chapter. Naming the bird a second time points at the clue, which should land when Nell half-recognises the van.

*Withdrawn from the review:* the double `---` before the author's notes. Every chapter has one, so it's house convention, not a slip.

---

## Part C — Notes for the rewrite of chapters 3 onwards (Martin to tick)
Add the ticked items to the matching revision briefs in `book/outline.md`. These are plan notes, with no chapter text.

- [ ] **C1. Chapter 3 opens fast.** Ch 2 runs slow, then fast, then slow, and ch 4 is a slow interlude, so ch 3 must not be slow throughout (pacing rule: no two slow present-day chapters in a row). Open on a fast beat: Cobb's first sighting at the next table, or Nell's night of reconciling told as action. Len's talk is the slow centre.
- [ ] **C2. The red light is seen again before ch 23** (D5): one glance in ch 3 or 6. If it's off once, it becomes a clue.
- [ ] **C3. Danny's first exchange is used up.** "It's a tax dodge" / "You haven't seen it" now belong to ch 2. In ch 5 play it as a callback ("Still a tax dodge.") or retire it. "Don't let it get in your head, Nell" is his sign-off; use it sparingly.
- [ ] **C4. Danny's door timer (D14, ch 5) belongs to the same app** as ch 2's 4.9: a number that judges him.
- [ ] **C5. The bird logo is planted once,** on the coaster. When the van appears (ch 5 or 6), Nell half-recognises it, and the narration doesn't name the coaster. It pays off at 3:40 a.m. in ch 18.
- [ ] **C6. Pete stays one memory** until his pen pays off (ch 18 or 29), and the payoff is the first thing she circles. He mustn't become a second Emmanuel.
- [ ] **C7. "It had seen the future" stays unremarked** until ch 23 ("the new teletype"). No later chapter underlines it.
- [ ] **C8. Track what Nell keeps off the blog**, starting with the red light (ch 2). Each thing she withholds is a small choice, which makes her more active (critic's re-review, Risk A: she mostly receives clues). Add it as a row in the outline's thread table, paying off at the Wall (ch 18) or in the smear campaign (ch 22).
- [ ] **C9. Style ceilings for the rewrite**, matching ch 2 after Part A: at most two "the way…" similes per chapter and one closing sting (already in `CLAUDE.md`), and no telling ahead. In ch 5, the shop parade becomes one image, the queue holding plastic meter keys, with Danny's "your kids' heating" line.

---

## Cross-checks done
- **Hard rules:** no new names, places, companies or real events. No Tenant lines. No use of "urban paranoia".
- **Other fixes files:** v1.0–v1.3 are applied, and none touches these lines of the v3.0 redraft. A5 keeps the bird-logo plant that ch 18 depends on (the outline's thread table).
- **Find strings:** A1–A5 each occur exactly once in `da4c126`, checked by script, and they apply cleanly in sequence.

## Change log
- 1.4 (2026-10-28): first issue.
