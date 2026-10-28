# Visual prompts guide

*For the executive editor. These prompts are ready to paste into NotebookLM: into the chat box, or into "Customise" on an Audio or Video Overview, a Mind Map or a report. Upload this file as a source too, so NotebookLM knows the house terms.*

---

## Before you start

- **Keep the notebook private.** The sources contain the ending, the cull and Book 2's Freeholder. Don't share it with test readers.
- **Check answers against the sources.** NotebookLM cites its sources; click the citation before acting on anything. The canon decisions (D-numbers, source 05) and the outline (source 07) win any argument.
- **In-world and out-of-world.** The ARG posts are written as if real. Their "production notes" sections are the out-of-world truth.
- **Refresh after changes.** After a new chapter or fixes file, rebuild the pack with `python3 tools/build_lmnotebook.py` and re-upload the changed sources (the chapter file, 03, 05 and 07 usually).

## 1. Audio Overviews (listen on the move)

**Weekly editor's briefing.** Choose sources 01, 07 and the latest chapter files. Customise:
> You are two senior editors briefing the executive editor. Summarise where the novel stands: what the latest chapters do, which threads they plant, what the outline needs next, and the three biggest risks to the story. Be candid, and cite chapters.

**The twist, from the reader's side.** Choose 01, 05 and chapters 1–6. Customise:
> Discuss how the story teaches that every scapegoat is a decoy, without ever blaming a real group. Where is the message shown, and where is it only stated? Where could a reader misread it?

**Character deep-dive.** Choose 02 and the chapter files. Customise:
> Talk only about [Danny / Crane / Jack / the Archivist]. What do we know, what has the reader seen, what is still hidden, and where does the outline take them?

**The ARG walkthrough.** Choose 14 and 03. Customise:
> Walk a new player through the rabbit hole in order: each post, puzzle and dead drop, what solves it, and where the fiction trail sits on each site.

## 2. Mind Maps

Click **Mind Map** with these source sets:
- **The Table's structure:** 05 only. It shows the Seats, Portfolios, Factors, Stewards and companies.
- **The ladder:** 05 and 01. It shows Freeholder, Tenants, Table, Factors, Stewards and tenants.
- **Threads and payoffs:** 07 and the chapter files. Then ask in chat: *"Which threads planted in chapters 1–6 have no payoff in the outline?"*
- **Six pressures (the Wall):** 06 and 07. Each pressure, who it hurts and who gets blamed.

## 3. Reports (Briefing doc, Study guide, FAQ, Timeline)

- **Timeline:** sources 03 and the chapter files. Ask for a dated timeline of everything the *reader* has seen by the end of chapter 6, with day-counts.
- **Briefing doc:** sources 01, 05 and 07. Use it as a one-page pitch summary for agents or co-producers (check it for spoilers before sending).
- **Study guide:** sources 08–13. Use it as a quiz on your own book, to test what a reader retains.
- **FAQ:** sources 05 and 06. Answers to "Is the Lodge real?" and "Who are the Tenants?" for the community team (out-of-world).

## 4. Chat prompts for editing

**Continuity**
> List every date, day-count and age stated in chapters 1–6 and check each against the timeline (source 03). Show any mismatch with both citations.

> Which facts about Nell's father appear in chapters 2, 3 and 6, and in the ARG posts? Do any contradict each other?

**Rules (run before signing off a chapter)**
> Check chapter [n] against the hard rules in source 06. Does it name any real person, company, place, event or group? Does it present any real group as part of the plan? Quote each risky line.

> Is the title phrase "urban paranoia" used anywhere except chapter 25's plan and out-of-world material?

**Craft**
> Find every line in chapters 1–6 that tells the reader what is coming, or explains what a scene means, rather than showing it. Quote them.

> How many new names and invented terms does each chapter introduce? Which chapter introduces the most, and are any introduced before the reader needs them?

> Count the "the way…" similes per chapter. The house rule is at most two.

**Planning the next chapter**
> Using the outline entry for chapter [n] and everything set up in chapters 1–6, list what this chapter must deliver, what it must not reveal yet, and which earlier lines it can echo.

> What does the reader know at the end of chapter 6 that Nell doesn't, and what does Nell know that the reader doesn't?

**Market and pitch**
> Write a 150-word back-cover blurb from source 01 with no spoilers past Act One.

> Which comparable titles named in the synopsis fit this book best, and why?

## 5. Video Overview and slides

Choose sources 01 and 02 and customise:
> Make a short explainer for a new collaborator (an illustrator or audio producer): the premise, the main characters, the tone and the rules. No spoilers past chapter 10.

## Source list

| # | Source | Use it for |
|---|---|---|
| 01 | Series overview | The whole property on one page |
| 02 | Who's who | Characters, with the full character bible as an appendix |
| 03 | Timeline | Every dated event, real backdrop marked |
| 04 | Places, organisations, glossary | Names and terms |
| 05 | Lodge, Tenants, deep time | The secret canon and the canon decisions |
| 06 | Rules, voices, pressures | Hard rules, character voices, the six pressures |
| 07 | Book plan | Synopsis, 30-chapter outline, resolution map, the Wall |
| 08–13 | Chapters 1–6 | Editor's summary, full text, author's notes |
| 14 | ARG campaign | Plan, puzzle map, safety, every in-world post |
| 15 | This guide | Prompts and house terms |
