---
date: 25 Oct 2026
scope: whole project (bible, chapters 1–5, synopsis, outline, resolution map, ARG content, campaign, marketing, CLAUDE.md, README)
status: all fixes applied 25 Oct 2026 (finding 2: option A)
---

# Continuity review

## What was checked
- **Automated:**
  - broken links (**none**)
  - leftover old names: Calder, Meridian, Ninefold, Julian or Philip Mercer, Common Soil, Rootstock, Quarantine (**none**, apart from deliberate history notes)
  - every date and Lodge day-count pair in every file (**34 checked, all correct**)
  - chapter word counts against outline labels
  - real place names in chapters and ARG content
- **By hand:** character facts (ages, dates, relationships), timeline order, canon decisions against the chapters, ARG content against the novel, and the rules in CLAUDE.md against the text.

## Findings

| # | Severity | Where | Issue | Proposed fix |
|---|---|---|---|---|
| 1 | **High** | ch 5 | @longweather_ knows Nell went *"back to the shelves on Tuesday"* in **mid-May**, but ch 3 says her notice (and keycard) ended about **30 April**. She couldn't have been in the archive. | Change it to *"been back to the shelves on the last Tuesday of my notice"*, which keeps the keycard-log clue (canon decision D5) intact. |
| 2 | **High** (decision needed) | ch 1, synopsis, CLAUDE.md vs `public-figures.md` rule 5 | The rule says the country is **never named**, but ch 1 says *"the train from London"* and *"the most British thing"*, and the canon premise is *"a remote English house"*. The present-day city is in the same country, so Britain is effectively confirmed. | **Option A (recommended):** relax the rule. The story is **recognisably set in Britain**, but no real present-day towns, institutions or leaders are named; invented leaders stay composites with vague dates. **Option B:** remove "London" and "British" from ch 1 and make the house's country vague. |
| 3 | Medium | Dead Drop 01, Fragment Four | *"It **printed** the three tones"*. The tones are a **sound** everywhere else. | Change to *"It **sounded** the three tones"*. |
| 4 | Medium | `bible/characters.md` | Ch 5 v2 adds new canon: **Danny is 57**, works **nights at a warehouse** as a second job, and has a **granddaughter** in the same class as the attacked family's child. Not yet in the bible. | Add these to Danny's entry. |
| 5 | Low | `bible/characters.md` | Ch 2 says **Pete retired in 2016 and died in 2020**, and his daughter gave Nell a green pen. Not in the bible. | Add to Pete's entry. |
| 6 | Low | `book/outline.md` | The ch 5 label says *~2,300 words*; the actual is **~2,740** (v2). | Update the label. |
| 7 | Low | `README.md` | The status line says *"chapter 1 (v2)"*; chapters **1–5** are now drafted. | Update the status line. |
| 8 | Low | synopsis | *"a telephone **engineer** from Ohio"*; ch 1 and the Lodge file say a **planner** at a telephone company. | Change to *"a telephone planner from Ohio"*. |
| 9 | Low | ch 3 | Len carried *"teletypes, early on"*, but canon only follows **one** teletype (Harrowgate, 1962 to 1971). | Either accept it (the Lodge used other teletypes, such as Harlow-Vane's line) and note it in the bible, or change Len's line to *"a teletype, once, early on"*. **Recommend:** note it in the bible; it adds texture. |
| 10 | Low (decision) | Dead Drop 01, HG-68 cue sheet vs `outputs/three-tones.wav` | The cue sheet says each tone lasts about **2 seconds** (0:53–1:01); the WAV is **3 seconds in total** (0.9 seconds each). | Keep both: the WAV is the short **promotional** version, and HG-68 uses the slower 2-second tones. Note it in the asset list. |

## Checked and consistent (no action)
- **Nell:** born about 1988, joined Coyle's in 2014 at 26, team of nine, go-live **Sat 17 May 2025 (Day 22,861)**, manifest found **Mon 20 Apr 2026 (Day 23,199)**, blog at 03:10. Matches ch 2–3, Posts #1–5 and Weather report #1.
- **Emmanuel:** Coyle's 1979–2009, died 2019. **Mother:** died about 2015. Ch 3's "seven years" and Post #4's "eleven years" both fit.
- **Danny:** a family friend since Nell was nine (ch 5), which fits Post #3's *"my oldest friend"*.
- **Len:** 1968–2014, *"retired the year I joined"*. The Exchange went to Harrowgate in 1983 (canon decision D3).
- **Old Tommy:** 23 in 1962, died about 2016. Fits ch 1's *"almost forty years… then every day."*
- **The Frenchman:** 44 in 1971, died 1997. Ch 1's *"thirty-five years"* and ch 4's *"twenty-six years later"* agree.
- **The demographer:** 36 in 1962, 44 in 1971, died 2001 (*"thirty-nine years she had left"*).
- **The Table:** three Founders plus nine seated by 1969 equals twelve, plus the empty chair. Mother Quill seated 1966. The American is the Listener until 1976.
- **The 1971 removal:** HG-71 on Day 3,061, collected on Day 3,062 (ch 4, Posts #1–2, the timeline).
- **@longweather_:** created 2022, older than the blog (ch 5, Post #2).
- **Pen name:** Martin Defries in every file and PDF; the front cover is correct.
- **Rules:** no real people or companies; @longweather_ never quoted; no group blamed; book-only themes absent from ARG content.

## Fixes to apply on approval
Findings **1, 3, 4, 5, 6, 7, 8**, plus a decision on **2**. Notes for **9** and **10**. Then rebuild the affected PDF (chapter 5).
