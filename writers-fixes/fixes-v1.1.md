---
title: Writer's fixes
version: 1.1
date: 2026-10-26
from: creative critic (up-creative-critic)
source-version: ad7cc1e
covers: chapter 6 (Count Forwards), its knock-on changes in chapter 2, Posts #1 and #3, the bible, the asset list and the PDF builder; idea #4 (outline ch 19)
supersedes: nothing (v1.0 is fully applied; see applied-log.md)
status: Part A requested by Martin, apply. Part B is required by Part A, apply. Part C needs Martin's tick.
---

# Writer's fixes v1.1

For the writing agent. The reasoning is in the critic's review `up-creative-critic/reviews/chapters/2026-10-26-ch06-count-forwards.md`. Every "Find" string was checked against commit `ad7cc1e` and occurs exactly once in its file, unless noted.

**How to use this**
- **Part A:** the chapter 6 fixes and idea #4, requested by Martin. Apply them.
- **Part B:** companion changes that Part A makes necessary elsewhere. Apply them in the same commit as Part A, or the canon splits.
- **Part C:** one new suggestion found while cross-checking. Apply only if Martin ticks it.
- Then rebuild **chapters 1, 2, 4 and 6** (the typography change affects every chapter that uses `>` blocks), log the result in `applied-log.md`, and leave v1.1 in place.

---

## Part A — Chapter 6 and idea #4 (apply)

### A1. The "office copy" becomes the consignee's copy (High)

**Problem.** In ch 3 (and Post #2), Len says *"The stamp was on the office copy, not yours."* The copy Nell found in Coyle's own archive (ch 2) has the stamp, so it *is* the office copy. The enclosed copy needs to be a different one. It's the copy that travelled with the machine, weighed in at the receiving end. That also tells Nell the letter-writer has papers from the Lodge's side (the Aldane Papers), which is true.

File: `book/chapters/06-count-forwards.md`

| # | Find | Replace with |
|---|---|---|
| A1a | `This was the **office copy**, the one Len had told me about, the one the drivers never saw.` | `Mine was the office copy; Len had as good as told me so. This one had come from the other end: the copy that travelled with the machine, signed for in a small, cramped hand, *recd. Ashby Tst.*` |
| A1b | `Someone had filled it in, in the same neat clerk's hand:` | `Someone at the far end had weighed it in and written it down:` |
| A1c | (author's notes) `the 1971 office copy and the May 2025 server cabinet` | `the 1971 consignee's copy (signed for at the Ashby Trust) and the May 2025 server cabinet` |

The next sentence ("Same consignment, same date that wasn't a date, the same purple stamp pressed harder…") stays as it is.

### A2. A separate typeface for letters and documents (Medium)

**Problem.** The Archivist's letter is typeset exactly like the Tenants' counsel: centred Courier capitals. It prints "I AM SORRY" and "WHY I KNOW IT" in the machine's style. That blurs the book's key tell (the Tenants never say "I") and weakens the epilogue's *I*.

**The rule from now on:** `>` is **for the Tenants only** (centred Courier). A new `>>` marker is for **letters, documents, stamps and notes** (left-aligned Courier, indented, with a thin rule above and below, like a sheet pasted into the page). Counsel *quoted inside* a document (e.g. the Minutes in ch 12) uses `>>`, because the reader is seeing paper, not the voice.

File: `tools/build_chapter.py`
- Add a `document` ParagraphStyle: `fontName="Courier"`, `fontSize=9.5`, `leading=13`, `alignment=TA_LEFT`, `leftIndent=8*mm`, `rightIndent=8*mm`, `spaceBefore=4`, `spaceAfter=4`. Add a thin grey rule (e.g. `HRFlowable`, 0.4 pt, colour `GREY`) **before the first and after the last** of each run of consecutive `>>` blocks.
- In the block loop, check `block.startswith(">>")` **before** the existing `block.startswith(">")` test, stripping `>> ` from each line.
- In the docstring, after `- Counsel:         > LINES IN CAPITALS`, add: `- Documents:       >> LETTERS, STAMPS, MANIFESTS (left-aligned; never the Tenants)`

File: `book/chapters/06-count-forwards.md`
- Change the eight letter lines (`> MS OKAFOR-REYES.` … `> WHEN YOU ARE READY THE DOOR IS GREY.`) from `>` to `>>`. The text is unchanged.

(Part B2 covers the same change in ch 2.)

### A3. The window scene: cut the explanation, add one flicker of suspicion of Danny (Medium; two fixes merged)

These two fixes touch the same paragraph, so they are given as **one** replacement. Don't apply them separately.

File: `book/chapters/06-count-forwards.md`

**Find** (one paragraph):

`I'd heard that sentence before. Not in those words, but nearly. Danny had said it in my kitchen, a week ago, with chips going cold on the counter: *Don't let anyone tell you it's the people down your street.* A man who'd known me since I was nine, and a stranger who'd broken into my website, had told me the same thing within seven days of each other, almost word for word.`

**Replace with** (three paragraphs):

```
I'd heard that sentence before. Danny, in my kitchen, a week ago, with chips going cold on the counter: *Don't let anyone tell you it's the people down your street.*

And for one second, at that window, the thought came in the way cold comes under a door. Danny knew where I lived. Danny had known my father's birthday for nearly thirty years; he'd eaten half the cake at most of them. Danny had said it first.

I said "No," out loud, to the empty flat, the way you'd tell a dog to get down.
```

**Then find:** `I didn't know what to do with that. I still don't, entirely.`
**Replace with:** `I didn't know what to do with any of it. I still don't, entirely.`

**Canon guard:** this is a thought she refuses, not a clue. Danny is **not** to be made suspicious in later chapters. The beat exists to test the letter's sentence on the person nearest to her.

### A4. Her full name (Medium)

File: `book/chapters/06-count-forwards.md`

| # | Find | Replace with |
|---|---|---|
| A4a | `My name and my address, typed.` | `My full name and my address, typed.` |
| A4b | `My **home** address. Which has never been on the blog` | `My full name: not *Nell*, which @longweather_ had already picked up, but all of it. And my **home** address. Which has never been on the blog` |

(This fits ch 5 as revised in v1.0: *"The last one used my name. Not Vesper: Nell."*)

### A5. Line edits

File: `book/chapters/06-count-forwards.md`

| # | Find | Replace with | Why |
|---|---|---|---|
| A5a | `and four hundred people had read past it` | `and hundreds of people had read past it` | "Four hundred" was the week-one figure. |
| A5b | `posted them to an address I'd never given anyone` | `posted them to an address I'd never given any of my readers` | Danny, the council and Coyle's all have it. |
| A5c | `delivery of one server cabinet to the comms room at head office, for the new routing system.` | `delivery of one server cabinet to the comms room at head office: the local box the new routing system ran through.` | Ch 2 says the system runs "on a cloud". This explains the physical box and supports canon decision D5 (the cabinet logs the keycards). |

### A6. Idea #4: Dad's dictionary pays off in ch 19 (outline only)

**No chapter text yet.** Add this to the outline so the gun that ch 6 loads is tracked.

File: `book/outline.md`
- **Ch 19 entry:** after `Her father **stopped**.`, insert: `That night she opens his crossword dictionary (closed unread in ch 6): the small pencil numbers in its margins are **Lodge day-counts**, the runs he phoned through, kept privately. After the last one there is no number, only a single word he looked up and underlined (word to be found in drafting). He counted too, and he stopped.`
- **"Threads and payoffs" table:** add the row `| Dad's dictionary margins | ch 6 (closed unread) | ch 19 (day-counts; one word) |`

**Guards:**
- Make the last entry a **single word**, not a sentence. Ch 26's notebook ends with *a line that isn't a number* ("The Frenchman was the lucky one…"). The two should rhyme, not duplicate.
- The margins say **nothing about Nell's job**. "Placement noted" stays unresolved (D8).
- The day-counts must check out with the `README.md` command, and fall between 1979 and his refusal in 1987 (ch 11), unless canon says he continued after it.

---

## Part B — Companion changes (required by Part A; apply in the same commit)

### B1. The consignee's copy everywhere else (follows A1)

| # | File | Find | Replace with |
|---|---|---|---|
| B1a | `content/phase-1/post-03-count-forwards.md` | `**The first** is the **office copy** of the 1971 manifest, the one Len told me about, the one the drivers never saw.` | `**The first** is another copy of the 1971 manifest. Not mine: mine, I'm now fairly sure, is the office copy Len told me about. This one travelled with the machine and was signed for at the far end: *recd. Ashby Tst.*` |
| B1b | same file | `*[Scan: 1971 manifest, office copy, weight 144 LB]*` | `*[Scan: 1971 manifest, consignee's copy, signed "recd. Ashby Tst.", weight 144 LB]*` |
| B1c | same file (production notes) | `**144 lb** on both the 1971 office copy and the 2025 goods-in note.` | `**144 lb** on both the 1971 consignee's copy and the 2025 goods-in note.` |
| B1d | same file (production notes) | `**A prop office copy** of the 1971 manifest, with 144 LB and a stronger stamp.` | `**A prop consignee's copy** of the 1971 manifest, with 144 LB, a stronger stamp and "recd. Ashby Tst."` |
| B1e | `content/phase-1/post-01-for-the-long-weather.md` (production notes) | `when the Archivist sends the office copy showing **144 LB**` | `when the Archivist sends the consignee's copy showing **144 LB**` |
| B1f | `bible/artefacts-register.md` | `\| 1971 manifest, office copy \| 144 LB \|` | `\| 1971 manifest, consignee's copy (recd. Ashby Tst.) \| 144 LB \|` |
| B1g | `campaign/asset-list.md` | `\| 1971 manifest, office copy \| Post #3 \| Same as driver copy plus "144 LB" and a stronger stamp \|` | `\| 1971 manifest, consignee's copy \| Post #3 \| Same consignment as Nell's archive copy, plus "144 LB", a stronger stamp and "recd. Ashby Tst." \|` |

**Unchanged on purpose:** Len's line in ch 3 and Post #2 (*"The stamp was on the office copy, not yours"*). It's now consistent.

### B2. Chapter 2's manifest is a document, not counsel (follows A2)

File: `book/chapters/02-contribution-to-the-transition.md`

| # | Find | Replace with |
|---|---|---|
| B2a | `> OFFICE EQUIPMENT — TELETYPE APPARATUS, 1 UNIT. HANDLE AS INSTRUCTED.` | `>> OFFICE EQUIPMENT — TELETYPE APPARATUS, 1 UNIT. HANDLE AS INSTRUCTED.` |
| B2b | `> **FOR THE LONG WEATHER**` | `>> **FOR THE LONG WEATHER**` |

Leave chapters 1 and 4 alone: every `>` there is genuine counsel.

### B3. Record the convention (follows A2)

| # | File | Change |
|---|---|---|
| B3a | `book/outline.md`, after the **Rhythm rule** paragraph | Add: `**Typography rule:** centred capitals (`>`) are reserved for the Tenants. Letters, documents, stamps and notes use `>>` (left-aligned, ruled). Counsel quoted inside a document is set as a document.` |
| B3b | `CLAUDE.md`, "Working conventions", narrator-labels bullet | Add one sentence: `In chapter files, `>` is for the Tenants' counsel only; use `>>` for letters and documents (see the outline's typography rule).` |
| B3c | `bible/voices.md`, Archivist section | Add: `In the novel, her letters are set as documents (`>>`), never in the Tenants' centred style.` |

---

## Part C — Martin to tick

- [ ] **C1. Redact Nell's surname in Post #3.** Found while cross-checking A4: in the ARG, Nell publishes the letter in Post #3 with `MS OKAFOR-REYES.` in full. A frightened Nell would remove it. Then the Archivist's Dead Drop page (W5) is the first place her full name goes public, which is a darker beat that the campaign gets for free.
  - In `content/phase-1/post-03-count-forwards.md`, replace the letter line `> MS OKAFOR-REYES.` with `> MS [—].`
  - Add one sentence after the letter: *"It used my full name. I've taken that out. You can have the rest."*
  - The **book's** ch 6 is unaffected: Nell, writing later, sets the letter down "exactly as it is".

---

## Cross-checks done (so nothing collides)

| Check | Result |
|---|---|
| A3's two fixes vs each other | Same paragraph, so they're merged into one replacement. |
| A4 vs ch 5 (v1.0 D13) | Wording builds on "@longweather_ had already picked up" *Nell*. ✓ |
| A1 vs Len (ch 3, Post #2) | Len's line is untouched and now consistent. ✓ |
| A1 vs asset list, artefacts register, Posts #1 and #3 | All renamed in B1. "Office copy" now means only Nell's archive copy. ✓ |
| A2 vs chapters 1, 2 and 4 | Ch 1 and 4 are counsel only (unchanged). Ch 2 has two document lines (B2). ✓ |
| A2 vs v1.0 D19 (hyphen exception) and D28 (hyphenation) | No conflict. Courier blocks don't hyphenate. ✓ |
| A5c vs canon decision D5 | Supports it (the cabinet logs the keycards). ✓ |
| A6 vs D8, ch 26's notebooks, ch 11's refusal | Guards written into A6. ✓ |
| A3 vs the hard rules | Ordinary neighbour suspicion, refused. No group named. ✓ |
| All Find strings | Checked against `ad7cc1e`; each occurs once in its file. ✓ |

---

## Change log

| Version | Date | By | Change |
|---|---|---|---|
| 1.0 | 2026-10-26 | Creative critic | First issue (applied in `a9ea277`). |
| 1.1 | 2026-10-26 | Creative critic | Chapter 6 fixes, companion changes, idea #4 (outline), Post #3 surname option. |
