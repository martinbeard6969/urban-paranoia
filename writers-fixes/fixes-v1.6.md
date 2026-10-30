---
title: Writer's fixes
version: 1.6
date: 2026-10-30
from: creative critic (up-creative-critic)
source-version: d8ec1de
covers: chapter 5 (v3.1), chapter 6 (v3.1), and reader panel round 3 points in chapters 3 (v3.2) and 4 (v3.1); outline; ARG Post #2
status: Part A requested by Martin ("generate one fixes file for ch 5, ch 6 and the round 3 points"): apply. Part C needs Martin's tick.
---

# Writer's fixes v1.6: chapters 5 and 6, and the round 3 points

**What this is.** These are the fixes from the critic's ch 5 v3.1 review and the reader panel round 3 assessment (with the chair's notes). Chapter 5 and chapter 6 depend on each other, so they come in one file. **Part A** gives Nell three small actions in ch 5 and ends it on Danny's hand. It fixes three continuity errors (ch 4's driver, ch 6's "1h40", the plate figures), gives the faceless-man device one appearance only (the face line, in ch 1), and makes the keycard sinister rather than lucky. **Part C** holds the choices Martin needs to make.

The reasoning is in:
- `up-creative-critic/reviews/chapters/2026-10-30-ch05-the-sensible-voice-v3.md`
- `up-creative-critic/reviews/whole-work/2026-10-30-reader-panel-round-3.md` (with the addendum)

**How to use this**
- **Part A:** apply. Every Find string was checked by script against `d8ec1de`. Each occurs exactly once, and A1–E2 apply cleanly in sequence. Part C was checked on top of Part A.
- **Part C:** apply only the items Martin ticks.
- Then:
  - rebuild ch 3, 4, 5 and 6;
  - update each chapter's author's notes where they quote changed text (ch 3 "a face that didn't stick"; ch 5 the ending and speed map; ch 6 "an hour and forty minutes", "65 KG", "small wardrobe");
  - update the plate in `bible/timeline.md` (Mon 25 May row; it quotes 65 KG);
  - log the result in `applied-log.md` against v1.6.

---

## Part A — apply

### Chapter 5 (`book/chapters/05-the-sensible-voice.md`)

**A1. Trim the first recap** (~l. 54). Find:
`Len's face when the man sat down. *Who else did you tell?* The man nobody could describe. My paragraph,`
Replace:
`Len's face when the man sat down. *Who else did you tell?* My paragraph,`

**A2. Compress the second recap** (~l. 128). Find:
`So I told her. The box, the stamp, the date, the drivers, the café, the man. I'd never said it all out loud from beginning to end. It sounded madder out loud, and more real.`
Replace:
`So I told her, all of it, beginning to end, out loud for the first time. It sounded madder out loud, and more real.`
*Why (A1–A2):* Nell told the story twice, and the reader learned nothing new either time. This is the main reason readers skimmed ch 5.

**A3. Nell answers Ama's question** (~l. 140). Find:
`I hadn't rung him since the café. I'd told myself it was to keep him safe.`
Replace:
`I hadn't rung him since the café. I got my phone out under the table and texted him: *You all right?* Three dots came and went. Then: *Leave it, love.*`
*Why:* it gives her an action, and he turns her down. Len is alive and frightened, and stays no victim (D14). "Leave it" is his line from ch 3. It also fixes the unclear "it" in the next sentence ("While I was looking at it"), which now means the phone.

**A4. The back room: Nell chooses** (~l. 148). Find:
`Nobody watched them go. In a room where everyone noticed everything, nobody looked at that door, and that was how I knew it mattered. Later,`
Replace:
`Nobody looked at that door, and after a second, neither did I. It was the first thing that room taught me. Later,`
*Why:* four readers asked for someone to notice and choose not to look. The care rule holds: support only, nothing shown or explained.

**A5. Cut the narrator's verdict on Danny** (~l. 64). Delete this paragraph and the blank line after it:
`He was nearly right. That's the thing about Danny: he's nearly always nearly right, and the gap between nearly and actually is so narrow that most people never notice it's there.`
*Why:* it explains the scene. The wave at the end shows how wrong he is. "nearly" ×5 falls to 1.

**A6. Danny's shift time** (~l. 70). Find:
`rang every night at seven, because at eight he had to be at the warehouse.`
Replace:
`rang every night at seven, before he went to the warehouse.`
*Why:* on Saturday he calls in "at nine, on his way to the warehouse". The new wording matches `characters.md`.

**A7. Trim the pension sum** (~l. 86). Find:
`I did it. I'm good at sums. A man of fifty-seven who'd spent twenty years making sure other people were paid fairly, working days and nights to stay exactly where he was.`
Replace:
`I did it. I'm good at sums.`
*Why:* the sum is already clear from his two lines. This is the chair's "trim the pension material". Esme's call is unchanged.

**A8. The settlement clause, said once** (~l. 96). Find (note the leading space):
` My settlement had a clause about company records. Coyle's`
Replace (note the leading space):
` Coyle's`
*Why:* ch 3 (~l. 92) already gives the clause. The 1 a.m. reading that follows still names it.

**A9. A fact she can hold: the van's number** (~l. 202). Find:
`indicated, which nobody does, and turned out of sight.`
Replace:
`indicated, which nobody does, and turned out of sight.`
`(blank line)`
`I'd got four characters of its number plate, and I wrote them on the back of my hand, because I write things down.`
*Why:* it's an action, and it's a new fact the reader can test (Graham's "no new fact"). **Never put the characters on the page:** nothing should be traceable to a real vehicle. Add a line to the ch 10 brief: the four characters are one of the things that connect the sightings.

**A10. End on Danny's hand** (~l. 206–212). Delete everything from the blank line after `Danny stood in the middle of the road and looked at his own hand.` up to the closing `---` rules. That is these four paragraphs:
`Then he looked up at my window, and spread his arms a little, and shook his head.`
`My phone buzzed in my hand. *Who was that?*`
`I didn't answer. I didn't know what I'd say.`
`I had seen the driver's face. I'd seen it, and it was gone: an ordinary face, under the cab light, which I'd lost before the van reached the corner.`
*Why:* five of the six readers flag the faceless-man repeats, and the chair and three readers want the text cut. Cobb is carried by his behaviour (the indicator). The chapter now ends on its best image: her hand, then his.

### Chapter 6 (`book/chapters/06-count-forwards.md`)

**B1. "1h40"** (~l. 28). Find:
`*stood at the shelves for an hour and forty minutes, on the Tuesday*`
Replace:
`*stood at the shelves for six hours and fifty minutes, on the Tuesday, and didn't stop for lunch*`
*Why:* ch 3 has her there with no lunch until past five. The exact figure is an estimate (ch 3 gives no arrival time); any figure that covers the day will do. ~l. 30 ("I knew it was right… the time on my phone when I came out") still works.

**B2. Cut a tic** (~l. 32). Delete this paragraph and the blank line after it:
`I told myself it was a guess. I'm a reconciler. I know what a guess looks like.`
*Why:* "I told myself" ×3 falls to 2, and "reconciler" ×2 to 1 (the one at ~l. 194 stays).

**B3. "Two of them": show the step** (~l. 86). Find:
`Whoever had been in my account at 03:12 couldn't have told @longweather_. Someone else knew.`
Replace:
`Whoever had been in my account at 03:12 couldn't have told @longweather_. Someone else knew, and they hadn't needed my laptop to know it.`
*Why:* Graham couldn't follow the logic. "Two of them, then." stays (two watchers).

**B4. Don't invite the wardrobe mix-up** (~l. 108). Find:
`the size of a small wardrobe, with a fan`
Replace:
`the size of a fridge, with a fan`
*Why:* Len's wardrobe is the 1983 Exchange (D3), not this cabinet. "Chest-high" (~l. 158) stays consistent. The hum at ~l. 168 stays as a family resemblance.

**B5. The keycard: sinister, not lucky** (~l. 146). Find:
`It beeped. Green.`
Replace:
`It beeped. Green. On its stand, the tablet changed its mind: *Welcome back.*`
*Why:* the panel found the working keycard too convenient. The routing system runs the doors (D5). Now the page shows it, with no name and no new canon.

**B6. The plate figures** (~l. 162). Find:
`*NET WT 65 KG.*`
Replace:
`*NET WT 65.3 KG.*`
*Why:* 65 kg is 143.3 lb, and 144 lb is 65.3 kg. Precise to a tenth, the pounds come out at exactly 144.

**B7. Why she doesn't phone, and the doubt about Danny** (~l. 132). Find:
`I said "No," out loud, to the empty flat.`
Replace:
`I said "No," out loud, to the empty flat. But I didn't ring him. I didn't know yet what I'd be asking.`
*Why:* it answers Helen (why she phones no one) and Graham (the doubt about Danny was told in four lines and dropped). It's also a small choice of what to keep back (C8 thread).

### Chapters 3 and 4 (round 3)

**D1. Len in his own words** (ch 3, ~l. 100). Find:
`You'd not remember his face after. Not a bad face. Just one that didn't stick."`
Replace:
`You'd not remember his face after. Nothing wrong with it. It just slid off you."`
*Why:* Len quoted the ch 1 driver's private, italic thought word for word, the panel's clearest case of the repeats. **Companion, ARG Post #2** (`content/phase-1/post-02-day-zero.md`, ~l. 71): make the same replacement. The Find string occurs once there.

**D2. Let the reader join them up** (ch 3, ~l. 148). Delete this paragraph and the blank line after it:
`A man with no face at the door in 1962. A cash man whose face didn't stick in the eighties. A man at the next table whose face I couldn't keep for ten minutes. I made myself stop there.`
*Why:* it explains the device. The rule from now on: the face line appears once, in ch 1, and every later sighting gets a behaviour.

**D3. Ch 4's driver** (ch 4, ~l. 23). Find:
`because nobody who was paid could be allowed to stay the night.`
Replace:
`because nobody who was paid could be allowed inside after dark.`
*Why:* the American's driver sits outside in the car all night (~l. 19, ~l. 79). Now he's part of the rule, not a breach of it.

### Outline (`book/outline.md`, ch 6 entry)

**E1.** Find:
`*"stood at the shelves for an hour and forty minutes, on the Tuesday"*`
Replace:
`*"stood at the shelves for six hours and fifty minutes, on the Tuesday, and didn't stop for lunch"*`

**E2.** Find:
`*NET WT 65 KG / 144 LB*`
Replace:
`*NET WT 65.3 KG / 144 LB*`

Also add to the outline's Act One rewrite notes: **the faceless-man rule** (the face line once, in ch 1; behaviours afterwards).

---

## Part C — Martin to tick

- [ ] **C1. Danny's moral** (ch 5, ~l. 188). **Tick one.** *What changed since the review:* ARG Post #2 (~l. 93) and `bible/voices.md` (~l. 72) both quote the moral word for word, and ch 6 builds the suspicion of Danny on it. So the review's Option A now costs ARG and bible edits as well. **My recommendation moves to C1b.**
  - [ ] **C1a. Cut the lecture and the moral.**
    - Ch 5: Find (note the leading space) ` Twenty years I sat across tables from them. Always some bloke in a suit, always very polite, and he never, ever pays for anything. Not the rent. Not the jobs. Not that window." He was still looking down at the street. "Don't let anyone tell you it's the people down your street."` and replace it with `" He was still looking down at the street.`
    - Ch 6: delete the paragraph `I'd heard that sentence before. Danny, at this same window, a week ago: *Don't let anyone tell you it's the people down your street.*` and the blank line after it. Delete ` Danny had said it first.` (with its leading space). The suspicion then stands on the password.
    - Post #2 and `voices.md`: cut "Don't let anyone tell you it's the people down your street." from Danny's quote. In Post #2, also rework "I want it on the record" and "I'll come back to why he said that."
    - Outline ch 5 *Ends:* update to Danny's hand.
  - [ ] **C1b (recommended). Cut the lecture only.** Ch 5: Find (note the leading space) ` Twenty years I sat across tables from them. Always some bloke in a suit, always very polite, and he never, ever pays for anything. Not the rent. Not the jobs. Not that window."` and replace it with `"`. Danny's speech becomes: "It'll be some bloke in a suit. It always is." … "Don't let anyone tell you it's the people down your street." Ch 6, Post #2, `voices.md` and the outline are unchanged. This removes the class-shaped lecture (the watch item) and keeps his line, which the ARG uses as his signature.
- [ ] **C2. Ch 4: one face fewer** (round 3). Give the glove-and-chair beat to the Rotterdam man and drop the diplomat from the page. He stays in `the-lodge.md`'s list.
  - Find: `the junior diplomat who never took his gloves off had reached for it` → Replace: `the shipping manager from Rotterdam had reached for it`
  - Find: `Tonight the shipping manager from Rotterdam had brought figures.` → Replace: `Tonight the man from Rotterdam had brought figures.`
  - Find: `The diplomat smoothed his gloves, and the talk came back` → Replace: `The man from Rotterdam smoothed his folded figures, and the talk came back`
  - Update the ch 4 author's note ("gloved diplomat").
- [ ] **C3. The letter in the book** (ch 6). Anton says it states the thesis in capitals. **Option:** the book quotes only four of its lines (the writer to propose which), and the ARG's Post #3 keeps the full text. No change unless ticked.
- [ ] **C4. A question for the writer, Post #2's in-world date.** Post #2 is dated "~10 days after Post #1" (about 30 Apr in the book's timeline), but it thanks "D." for naming her (ch 5, Mon 11 May) and quotes Danny's window line (Sat 16 May). Post #3 is "~2 weeks after Post #2". Please re-date both so they fall after the ch 5 and ch 6 events they report, and check them against ch 6's dates. No text change is proposed; it's dates only.
- [ ] **C5. A question for the writer, the two accounts with no picture.** The account that reposted Nell's paragraph (ch 3; ch 5 ~l. 54, "no picture and no other posts") and @longweather_ (ch 6, "no picture") are described the same way. If they're different accounts, give the reposter one distinguishing trait. If they're the same, ch 6 should let Nell notice.

---

## Cross-checks done
- **UP version:** HEAD was still `d8ec1de` when this was issued. Nothing has changed since the reviews.
- **Hard rules:** no new names, places, companies or real events. The number plate stays off the page. The care rules in ch 5 hold. No Tenant lines are changed. No use of "urban paranoia".
- **Against each other:**
  - A9 and A10 together leave Nell's hand, then Danny's hand, as the ending.
  - A3 changes the antecedent of the next sentence (intended).
  - B7 sits after the C1a cuts in ch 6 and reads cleanly with or without them (checked).
  - C1a and C1b are alternatives; both were tested on the post-Part-A text.
- **Against earlier fixes:**
  - v1.4 C3 (Danny's lines) and C5 (the coaster isn't named) hold.
  - v1.3 A2 (the flask after "whoever's nearest") holds.
  - v1.5 C4 (Len owns the driver's later life) holds: D1 changes only the face words.
- **Other UP files:**
  - Post #2 quotes Len's face line (companion in D1) and Danny's moral (handled in C1).
  - `voices.md` quotes the moral (C1).
  - The outline quotes "1h40" and the plate (E1, E2).
  - Nothing else quotes the cut lines.
- **Find strings:** A1–A10, B1–B7, D1–D3 and E1–E2 each occur exactly once in `d8ec1de`, checked by script, and they apply cleanly in sequence. The C strings were checked on the post-Part-A text.

## Change log
- 1.6 (2026-10-30): first issue.
