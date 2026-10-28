---
title: Writer's fixes
version: 1.3
date: 2026-10-28
from: creative critic (up-creative-critic)
source-version: 92c8132
covers: idea #6 "The Missing Knock" (Act Two strand); two seeds in chapter 5; outline, canon and character notes
status: accepted by Martin on 2026-10-28 ("proceed with idea and fixes"). Apply all of it. Nothing to tick.
independent of: v1.2 Part P. Neither touches the other's text, so apply them in either order.
---

# Writer's fixes v1.3: The Missing Knock

**Status: applied 2026-10-28, commit 22ca2c0. See applied-log.md.**

**What this is.** Martin has accepted a new Act Two strand. Three ordinary deaths are spun into a rumour that "someone is killing people like us". Every death is natural. In each one, the help that would normally have come didn't come: nobody knocked. Six people close to Nell each get one detail that makes them look suspicious or complicit. The reader suspects them, and so learns from the inside what the chapter 6 letter warned against: *DO NOT BLAME ANYONE YOU CAN SEE FROM YOUR WINDOW*.

The strand gives a specific content to outline ch 17's "crime that never happened". It runs on the ch 12 counsel *GIVE EVERY FEAR A FACE THAT IS NOT OURS*, so there's **no new Tenant line** and **no new major character**.

The full reasoning is in `up-creative-critic/ideas/backlog.md`, idea #6.

**How to use this**
- **Part A:** two seeds in ch 5. Every Find string was checked by script against `92c8132` and occurs exactly once. Rebuild ch 5 afterwards.
- **Part B:** the canon decision, the outline changes and the character notes. These are plan files only, with no chapter text.
- Log the result in `applied-log.md` against v1.3.

---

## Part A — Chapter 5 seeds (apply)

### A1. Danny's door timer (pointer: he left the parcels and didn't knock)
`book/chapters/05-the-sensible-voice.md`, opening paragraph.

**Find:**
`with his phone buzzing in his pocket every forty seconds to tell him he was late.`

**Replace:**
`with his phone buzzing in his pocket every forty seconds to tell him he was late. The app gave him ninety seconds at each door. Every second over came off his rating.`

### A2. The old man's flask (plants the first person to die)
Same file, the radiator scene.

**Find:**
`Ama poured two teas from the same pot and handed them over without a word.`

**Replace:**
`Ama poured two teas from the same pot and handed them over without a word. The old man didn't drink his. He tipped it into a tartan flask from his coat pocket and screwed the lid down tight, for later. Danny said he'd done that every Saturday since his wife died.`

He stays unnamed in ch 5 to keep the name load down. He's named when he dies (ch 13, name to be chosen in drafting).

---

## Part B — Plan files (apply)

### B1. New canon decision: `bible/canon-decisions.md`, after D13

> ## D14. The missing knock: safeguard
> - **The deaths are natural.** Three people die in Act Two (ch 13, 16, 17): a fall, a fire, a heart attack or similar. Nobody causes them. The Lodge's guilt is the **story** told about them, not the deaths.
> - **What links them is missing help:** a neighbour who stopped knocking, a care-alarm rota that changed, a spare key taken back. The neighbours stopped knocking because the rumour taught them to fear each other.
> - **Reported, never shown.** Nell learns of each death second-hand. There's no death scene and no point of view from a victim.
> - **No group selection.** Each victim is a specific person, with one planted detail while alive. The rumour sorts them into "sides"; the book shows the sorting is false.
> - **Nobody the reader suspects is a killer.** Six suspects (see `characters.md`) are innocent or complicit only in small, human ways.
> - **The plywood-window family is never one of the reader's suspects.** Only the rumour targets them. The book directs the reader's suspicion at Nell's own circle, so the reader's guilt lands on themselves, never on a group.
> - **Invented services only.** If a care-alarm or welfare-check firm is named, it's invented and goes on the name-clearance list (open question 1). Never real emergency services or the NHS, and never a hint that real health or care services fail on purpose.
> - **The Tenants never order deaths.** The only counsel involved is ch 12's *GIVE EVERY FEAR A FACE THAT IS NOT OURS*. The Table and Ward read it their own way (D13: humans own what they build).
> - **@longweather_ is never quoted.** Nell paraphrases it.
> - **Book and film only.** No ARG post, drop or account mentions the deaths or a pattern of deaths. The ARG may echo the rumour's *tone* at most.

### B2. Outline changes: `book/outline.md`
Add to each chapter entry. Everything not listed stays as it is, including every chapter ending.

| Ch | Add |
|---|---|
| **12** | No change. Note that *GIVE EVERY FEAR A FACE THAT IS NOT OURS* is the counsel the strand runs on. |
| **13** | **Death 1:** the old man with the tartan flask (planted ch 5) is found after a fall, three days late. Nell hears at the hall. **Danny** mentions he left a parcel on that doorstep on the Tuesday. **Ama** let slip that she gave the man's spare key back a fortnight ago, and won't say why. Nobody suspects anything yet. It's a sad, ordinary death. |
| **14** | **Crane's slip:** over tea, he mentions a detail of death 1 that Nell hadn't told him. She notices, and lets it go. |
| **15** | One line in the Factor's briefing, among other figures: *welfare-check rates down eleven per cent, Ward reports.* Nobody reacts. Nobody orders, causes or welcomes a death. |
| **16** | **Death 2:** someone on the Wharf Road estate. Frostline's posts, which already blame Jack's estate, now have a death to blame. Danny mentions he was at that block that week. Jack's slide toward Clearfell speeds up. The ending is unchanged. |
| **17** | **Death 3:** someone on the plywood-window family's street. **The "crime that never happened" is the killings:** "three, all on our side". **Jack's** Jordan account posts it before the local news. **Cobb** (or the bird-logo Larkspire van) is seen on that street the day before. **Nell posts** *"Three streets, one pattern?"* (curious, not blaming) and @longweather_ shares it with its own spin. Then the existing beats: "Jordan Pryce" named in one feed, the crowd outside the hall, Ama's back room. |
| **18** | **The Wall:** Nell pins up the three deaths and her six suspects. When she maps who *didn't* knock, every arrow runs sideways, at a neighbour. She sees she has done what the letter warned against. **Danny and Ama are explained here** (the app timer; the key, which the old man asked for back after the rumour made him afraid of visitors). |
| **20** | **Thursday:** the neighbour who didn't knock on victim 3's door comes to the meeting and says so. They are the design's second victim, and Nell has to refuse to blame them too. They mention that the only person who knocked that week was "a man from the letting agent. Polite. Nobody answered." **That was Cobb.** Nell's existing post *"Every arrow on my wall points sideways"* now also retracts her ch 17 post. (This is also the natural home for idea #5, a voice for the blamed, if Martin accepts it.) |
| **22** | The smear campaign uses Nell's ch 17 post as evidence that she's a crank. |
| **23** | Teo traces the rumour's posts to the same Larkspire racks. That proves someone wrote the pattern. **Jack is explained:** his recruiter fed him death 3 first. Optional: the care-alarm contractor whose rota changed is on Larkspire's books. |
| **25** | **Crane is explained:** he was briefed as her handler. The U.P. column now has a cost the reader has seen. It mirrors Ruth's mother, the accident the Table let everyone believe was murder. |
| **29** | The strike network sets up its own knock rota: neighbours checking on neighbours. The missing help is put back by the people themselves. Cobb's ending gains weight: he's the one who knocked, and now he signs. |

**Thread table** (`book/outline.md`, "Threads and payoffs"): add
- *The missing knock* | ch 5 (flask, timer) | ch 18, 20, 29
- *The man who knocked* | ch 17 | ch 20, 29

**Word cost (estimate):** ~3,000–4,000 across Act Two, mostly reallocated within ch 13, 16 and 17. Act Two stays inside its 26,000–30,000 budget.

### B3. Character notes: `bible/characters.md`
Add one line to each entry: **"Missing knock (D14):"** followed by:

| Character | Pointer (planted) | Explained | Complicit? |
|---|---|---|---|
| **Danny** | He was at all three doors the week before (ch 13, 16, 17). | ch 18: the app's ninety-second timer (ch 5). He left the parcels. | A little: the system punished knocking, and he obeyed it. |
| **Ama** | She gave back the old man's spare key and won't say why (ch 13). | ch 18: he asked for it back, afraid; her silence protects the back room. | A little: she chose the people she was sheltering over checking on him. |
| **Jack** | His Jordan account posted death 3 first (ch 17). | ch 23: the recruiter fed it to him. | Yes: he spread it. He caused nothing. |
| **Crane** | He knew a detail of death 1 that Nell hadn't told him (ch 14). | ch 25: a Factor briefed him. | Yes, for the long term: he built the measure. |
| **Cobb** | Seen on death 3's street the day before (ch 17). | ch 20: he was the only one who knocked. | No. |
| **Nell** | Her post *"Three streets, one pattern?"* is shared by @longweather_ (ch 17). | ch 18 and 20: she says on the page that she believed it for nine days, and retracts. | Yes: she lent the rumour her credibility. |

---

## Cross-checks done
- **Hard rules:** no real group, person, company or event; no real-world call to action. Deaths are natural and never shown. The cull and the Taken are untouched. The anti-scapegoating twist is strengthened, not inverted. No use of "urban paranoia". No Tenant "I".
- **Existing canon kept:** Cobb as a Steward who signs in ch 29 and doesn't know what the Lodge is; @longweather_ never quoted; "Jordan Pryce" named in one feed (`characters.md`); Ama's back room in ch 17 (idea #2, D17 in v1.0); Crane's ch 25 confession; Ruth's mother; chapter endings.
- **Other fixes files:** A1 and A2 sit outside every passage that v1.2 Part P changes (P1 is after "Which is always."; P5 is the Wharf Road paragraph). The new A2 sentences use no "the way…" simile (v1.2 C1 ceiling) and no closing sting.
- **Find strings:** both unique in `92c8132`, checked by script.

## Change log
- 1.3 (2026-10-28): first issue.
