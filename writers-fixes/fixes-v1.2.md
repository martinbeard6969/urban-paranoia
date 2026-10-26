---
title: Writer's fixes
version: 1.2
date: 2026-10-26
from: creative critic (up-creative-critic)
source-version: 68de6b9
covers: chapters 1–6, from the whole-book re-review of 26 Oct 2026
supersedes: nothing (v1.0 and v1.1 are fully applied; see applied-log.md)
status: Part A apply; Part B apply unless Martin strikes an item; Part C needs Martin's tick
---

**Status: Parts A and B applied 2026-10-26, commit 9b52ee4. Part C ticked by Martin and applied in the follow-up commit. See applied-log.md.**

# Writer's fixes v1.2

For the writing agent. The reasoning is in `up-creative-critic/reviews/whole-work/2026-10-26-rereview-ch01-06.md`, issues #1–6. Every "Find" string was checked against commit `68de6b9` and occurs exactly once in its file. No two items touch the same sentence.

**How to use this**
- **Part A:** one structural fix and four one-line corrections. Apply them.
- **Part B:** thinning the "the way…" similes (re-review issue #2). Apply unless Martin strikes an item.
- **Part C:** a standing style rule for future chapters. Apply only if Martin ticks it.
- Then rebuild **chapters 1–6**, log the result in `applied-log.md`, and leave v1.2 in place.

---

## Part A — Apply

### A1. Chapter 5: move the message-thread paragraph (re-review #1, Medium)

**Problem.** The v1.0 D16 paragraph sits between "Everybody called him Jordan." and Danny's "Except me." Danny's joke now seems to answer Jack locking his phone, not the name. Moving the paragraph lets the name joke run unbroken, and the scene then ends on the locked phone, which is the stronger last beat before "That night the comments changed."

File: `book/chapters/05-the-sensible-voice.md`

**Find** (this whole block):

```
He went by Jordan online, he told me, when I glanced at his screen. Jordan Pryce. It had been a joke when he was sixteen and it had stuck. Everybody called him Jordan.

What I'd glanced at was a message thread: long, patient paragraphs from someone whose name I didn't catch, the kind of writing that sounds like listening, and agrees with everything you'd already decided while you were too tired to argue. Jack saw me looking and locked the phone, not quickly, the way you'd close a door on a room you weren't ashamed of yet.

"Except me," said Danny.

"Except Danny. When he's cross with me."

"Which is always."

"Which is always."
```

**Replace with:**

```
He went by Jordan online, he told me, when I glanced at his screen. Jordan Pryce. It had been a joke when he was sixteen and it had stuck. Everybody called him Jordan.

"Except me," said Danny.

"Except Danny. When he's cross with me."

"Which is always."

"Which is always."

What I'd glanced at was a message thread: long, patient paragraphs from someone whose name I didn't catch, the kind of writing that sounds like listening, and agrees with everything you'd already decided while you were too tired to argue. Jack saw me looking and locked the phone, not quickly, the way you'd close a door on a room you weren't ashamed of yet.
```

No words change; only the order does. The section break (`---`) and "That night the comments changed." follow as before.

### A2–A5. One-line corrections

| # | File | Find | Replace with | Why (re-review #) |
|---|---|---|---|---|
| A2 | `book/chapters/01-day-zero.md` | `It didn't seem the most pressing point.` | `It didn't seem to matter yet.` | #3: "most pressing point" appears twice in two sentences. The second (the American's) stays, because it echoes Fragment Four. |
| A3 | `book/chapters/04-not-far-only-elsewhere.md` | `where the dock gangs had worked when he was a boy` | `where the dock gangs had worked until the boxes came` | #4: the gangs worked until a few years before 1971, not decades before. |
| A4 | `book/chapters/06-count-forwards.md` | `A Coyle's goods-in note, printed, from May last year: delivery of one server cabinet to the comms room at head office: the local box the new routing system ran through.` | `A Coyle's goods-in note, printed, from May last year, for one server cabinet delivered to the comms room at head office: the local box the new routing system ran through.` | #5: two colons in one sentence. |
| A5 | `book/chapters/03-reconciliation.md` | `Everyone of a certain age knows that autumn` | `Anyone old enough remembers that autumn` | #6: a stock phrase, and anyone who remembers 1962 is now over seventy. |

---

## Part B — Thin the "the way…" similes (apply unless struck)

**Problem (re-review #2).** "The way…" appears 36 times in 14,431 words, about once every 400 words. Some of those uses aren't similes ("the way Pete taught me", "on the way out"), but the simile form has become the narration's default, and it makes the interludes sound like Nell. These seven cuts target the densest places (ch 2 has 9, ch 5 has 7, and ch 6 has three within a page). The best images are kept: the hotel croissants, the darkening room, the sea, the glass about to break, the dog, the cold under the door. After this pass: ch 2 has 6, ch 3 has 4, ch 5 has 5 and ch 6 has 4.

| # | File | Find | Replace with |
|---|---|---|---|
| B1 | `book/chapters/02-contribution-to-the-transition.md` | `The contractor talked about both the way people talk about plumbing: something you only think about when it fails.` | `The contractor talked about both as if they were plumbing: something you only think about when it fails.` |
| B2 | same file | `I read it until the words came apart, the way a word does if you say it too often.` | `I read it until the words came apart.` |
| B3 | same file | `it smelled the way old paper smells: of nothing, almost, and then of dust and something sweeter underneath, like a church.` | `it smelled of old paper: of nothing, almost, and then of dust and something sweeter underneath, like a church.` |
| B4 | `book/chapters/03-reconciliation.md` | `in a small grey number at the top of the screen, the way a hospital monitor tells you your pulse.` | `in a small grey number at the top of the screen, like a pulse on a hospital monitor.` |
| B5 | `book/chapters/05-the-sensible-voice.md` | `quickly, the way he does everything, and posted it` | `quickly, and posted it` |
| B6 | same file | `turned, the way a road turns without warning, and ended` | `turned without warning, and ended` |
| B7 | `book/chapters/06-count-forwards.md` | `I knew before I got there, the way you know which stair creaks.` | `I knew before I got there.` |

**Check after B2:** the next sentence ("*Contribution*, as if I'd put money in a tin.") still follows naturally. No other change is needed.

---

## Part C — Martin to tick

- [x] **C1. A style ceiling for new chapters.** Add to `CLAUDE.md` § "Voice & style": `**Similes:** at most two "the way…" similes per chapter; vary the shape (a plain statement, "like", or a concrete detail). Interludes avoid Nell's "the way you'd…" habit altogether.`
- [x] **C2. Retire a tic.** Danny's "his face did the thing" appears three times (ch 5 ×2, ch 6). Add to `bible/voices.md` under Danny: `"His face did the thing" is used up (ch 5–6). Find a new tell for him from ch 7.`

---

## Cross-checks done

| Check | Result |
|---|---|
| A1 vs B5 and B6 (all in ch 5) | Different paragraphs. A1 only reorders; B5 and B6 edit lines outside the moved block. ✓ |
| A1's moved paragraph keeps "the way you'd close a door…" | Kept on purpose: it's one of the strongest images, and ch 5 still has 5 after Part B. ✓ |
| A2 vs v1.0 D4 (the Fragment Four echo) | The echo ("told her it was not the most pressing point") is untouched. ✓ |
| A3 vs v1.0 D10 (container berth) | Only the timing phrase changes; the image stays. ✓ |
| A4 vs v1.1 A5c and canon decision D5 | Same meaning, one colon. ✓ |
| A5 and B4 (both in ch 3) | Different paragraphs. ✓ |
| B7 vs v1.1 A3 (the Danny flicker, ch 6) | Different section; the flicker's two similes are kept. ✓ |
| Hard rules | No content changes; style only. ✓ |
| All Find strings | Checked against `68de6b9`; each occurs once in its file. ✓ |

---

## Change log

| Version | Date | By | Change |
|---|---|---|---|
| 1.0 | 2026-10-26 | Creative critic | First issue (applied in `a9ea277`). |
| 1.1 | 2026-10-26 | Creative critic | Chapter 6 fixes, idea #4 (applied in `2dd2f71`). |
| 1.2 | 2026-10-26 | Creative critic | Re-review issues #1–6: ch 5 paragraph order, four one-line fixes, seven simile cuts, two optional style rules. |
