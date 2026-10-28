# Urban Paranoia

*A novel by **Martin Defries** (pen name).*

A fictional transmedia property (novel, audio drama, and later film and comics), launched through an alternate reality game (ARG). The ARG gives audiences an *"is this real?"* experience and then leads them into the book.

**Agent instructions, canon summary and hard rules:** see [CLAUDE.md](CLAUDE.md). Read the hard rules before writing anything.

## Where things are

| Path | What's in it |
|---|---|
| [CLAUDE.md](CLAUDE.md) | Agent brief: premise, campaign structure, **hard rules**, voice |
| [bible/](bible/) | Canon: [timeline](bible/timeline.md), [characters](bible/characters.md), [the Lodge](bible/the-lodge.md), [the Tenants](bible/the-tenants.md), [modern pressures](bible/modern-pressures.md), [deep time](bible/deep-time.md), [the ladder](bible/the-ladder.md), [public figures](bible/public-figures.md), [locations & organisations](bible/locations-and-organisations.md), [artefacts register](bible/artefacts-register.md), [canon decisions](bible/canon-decisions.md), [voices](bible/voices.md), [glossary](bible/glossary.md), [open questions](bible/open-questions.md) |
| [campaign/](campaign/) | [Campaign plan](campaign/campaign-plan.md), [puzzle map](campaign/puzzle-map.md), [pre-launch checklist](campaign/prelaunch-checklist.md), [asset list](campaign/asset-list.md), [moderation & safety](campaign/moderation-and-safety.md), [news desk](campaign/news-desk.md) |
| [content/phase-1/](content/phase-1/) | Vesper's blog, Posts #1–3 |
| [content/phase-2/](content/phase-2/) | Dead Drop 01 (`/6b6e70`), Harlow-Vane site and card 0144, Weather report #1, Posts #4–5 |
| [news-desk/](news-desk/) | Weekly news digests ([first digest, 25 Oct 2026](news-desk/digest-2026-10-25.md)). See the [news desk process](campaign/news-desk.md). |
| [book/](book/) | [Synopsis](book/synopsis.md) · [Chapter outline](book/outline.md) · [Resolution map](book/resolution-map.md) · [Chapter 1: "Day Zero"](book/chapters/01-day-zero.md) · [Chapter 2](book/chapters/02-contribution-to-the-transition.md) · [Chapter 3](book/chapters/03-reconciliation.md) · [Chapter 4](book/chapters/04-not-far-only-elsewhere.md) · [Chapter 5](book/chapters/05-the-sensible-voice.md) · [Chapter 6](book/chapters/06-count-forwards.md) · [Act 2 midpoint: "The Wall"](book/act-2/scene-the-wall.md) (outline) |
| [marketing/](marketing/) | [ARG launch playbook: 8-week pilot](marketing/arg-launch-playbook.md) |
| [outputs/](outputs/) | Shareable PDFs (pilot plan snapshot, chapters 1–6) and the three-tones audio (clean and contrast-bed promos) |
| `audio/`, `comics/` | Not started |

## Status (as of 25 Oct 2026)

- **Bible:** draft v1, with core canon questions settled (see [canon decisions](bible/canon-decisions.md)). Remaining items are in [open questions](bible/open-questions.md).
- **Content:** all 8 pilot weeks drafted: Posts #1–5, Dead Drop 01, the Harlow-Vane site and Weather report #1. Nothing is published.
- **Book:** synopsis (v3), 30-chapter outline, resolution map, chapters 1–6 drafted (~14,400 words), and the "The Wall" scene outline.
- **Marketing:** 8-week ARG pilot playbook; PDFs in [outputs/](outputs/).
- **Blocking launch:** the name-clash checks (Harrowgate House especially) and all items in the [pre-launch checklist](campaign/prelaunch-checklist.md).

## Conventions

- **Chapter PDFs:** `python3 tools/build_chapter.py book/chapters/<file>.md` writes `outputs/chapter-<file>.pdf` (needs `reportlab`, version 4.0.9 on Python 3.9, and `pyphen` for hyphenation). Chapters open with a narrator label (see the [outline](book/outline.md)).
- Every content file has `phase:`, `channel:` and `canon-refs:` frontmatter, plus a **PRODUCTION NOTES** section at the end that is never published.
- New canon goes into `bible/` in the same change that introduces it.
- Lodge dates are counted in days from **14 Oct 1962 (Day 0)**. Check any new day-count with:

```bash
python3 -c "from datetime import date,timedelta; print(date(1962,10,14)+timedelta(days=3062))"
```
