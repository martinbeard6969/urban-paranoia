# lmnotebook: NotebookLM source pack

Sources for a private NotebookLM notebook for the executive editor. It covers the novel and the ARG, **with the full secret canon and ending**. Don't share the notebook with test readers.

## Load it

1. In NotebookLM, create a notebook called *Urban Paranoia: editor*.
2. Upload every numbered file (`01-` to `15-`). Don't upload this README or the `_written/` folder.
3. Start with the prompts in `15-visual-prompts-guide.md`.

If NotebookLM won't accept `.md`, run `python3 tools/build_lmnotebook.py --txt` and upload the `.txt` copies instead.

## What's in it

| File | Made by | Contents |
|---|---|---|
| `01-series-overview.md` | Written | Premise, the lease, the twist, the ending, book shape, ARG phases, rules in brief |
| `02-whos-who.md` | Built | Character tables (from `_written/whos-who.md`) plus the full character bible |
| `03-timeline.md` | Built | `bible/timeline.md` |
| `04-places-organisations-glossary.md` | Built | Locations and organisations, glossary |
| `05-lodge-tenants-deep-time.md` | Built | The Lodge, the Tenants, deep time, the ladder, canon decisions, artefacts register, open questions |
| `06-rules-voices-pressures.md` | Built | Hard rules and voice and style (from `CLAUDE.md`), public figures, voices, modern pressures |
| `07-book-plan.md` | Built | Synopsis, outline, resolution map, the Wall |
| `08`–`13` chapter files | Built | Editor's summary (from `_written/chNN.md`), full text, author's notes |
| `14-arg-campaign.md` | Built | Campaign plan, puzzle map, moderation and safety, every phase 1–2 post and page |
| `15-visual-prompts-guide.md` | Written | Prompts for Audio and Video Overviews, Mind Maps, reports and chat |

## Keep it current

Built files are regenerated from the project, so **never edit them by hand**. Edit the canon, then rebuild:

```bash
python3 tools/build_lmnotebook.py
```

- **New chapter:** add `_written/chNN.md` (an editor's summary in the same shape as the others), rebuild, upload the new chapter file, and re-upload 03 and 07. Add the chapter to the source list in 15.
- **Fixes applied:** rebuild and re-upload the files for the chapters that changed.
- **Who's who:** edit `_written/whos-who.md` when a character's status changes, then rebuild.
- Each built file carries its build date and commit, so you can see in NotebookLM which version a source is.
