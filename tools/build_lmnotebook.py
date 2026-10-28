"""Build the NotebookLM source pack in lmnotebook/ from the project files.

Usage:
    python3 tools/build_lmnotebook.py          # Markdown sources
    python3 tools/build_lmnotebook.py --txt    # also write .txt copies (if NotebookLM won't take .md)

Hand-written files (README, 01 overview, 02 who's who, 15 prompts guide and the chapter summaries
in lmnotebook/_written/, which also holds the who's who) are kept as they are. Everything else is assembled from the canon files,
so re-run this after every new chapter or fixes file and re-upload the changed sources.
"""
import datetime
import glob
import os
import re
import subprocess
import sys

OUT = "lmnotebook"
STAMP = "%s, commit %s" % (
    datetime.date.today().isoformat(),
    subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip() or "unknown")


def body(path):
    """A file's text without its YAML frontmatter."""
    t = open(path, encoding="utf-8").read()
    return re.sub(r"\A---\n.*?\n---\n", "", t, flags=re.S).strip()


def section(path, heading):
    """One '## heading' section of a file, up to the next '---' rule."""
    t = open(path, encoding="utf-8").read()
    m = re.search(r"^## " + re.escape(heading) + r".*?(?=^---$)", t, flags=re.M | re.S)
    return m.group(0).strip()


def header(title, sources, note=""):
    lines = ["# " + title, "",
             "*Urban Paranoia source pack for NotebookLM. Private: contains the full canon and ending.*",
             "*Assembled from: " + ", ".join("`%s`" % s for s in sources) + ". Built " + STAMP + ".*"]
    if note:
        lines += ["", note]
    return "\n".join(lines) + "\n"


def assemble(name, title, sources, note="", parts=None):
    out = [header(title, sources, note)]
    for s in sources:
        out += ["\n---\n", "<!-- source: %s -->" % s, parts[s] if parts and s in parts else body(s)]
    write(name, "\n".join(out))


def write(name, text):
    path = os.path.join(OUT, name)
    open(path, "w", encoding="utf-8").write(text.rstrip() + "\n")
    print("written", path, "(%d words)" % len(text.split()))


write("02-whos-who.md", "\n".join([
    header("Who's who", ["lmnotebook/_written/whos-who.md", "bible/characters.md"]),
    open(os.path.join(OUT, "_written", "whos-who.md"), encoding="utf-8").read().strip(),
    "\n---\n", "## Appendix: the character bible in full\n", body("bible/characters.md")]))

assemble("03-timeline.md", "Timeline", ["bible/timeline.md"],
         "Key: 🟦 real-world trend (backdrop only) · 🟥 fictional canon event · 📄 ARG artefact source. "
         "Day-counts run from Day 0 = Sunday 14 October 1962.")

assemble("04-places-organisations-glossary.md", "Places, organisations and glossary",
         ["bible/locations-and-organisations.md", "bible/glossary.md"],
         "Every company, place and body here is fictional unless marked as real backdrop.")

assemble("05-lodge-tenants-deep-time.md", "The Lodge, the Tenants and deep time",
         ["bible/the-lodge.md", "bible/the-tenants.md", "bible/deep-time.md", "bible/the-ladder.md",
          "bible/canon-decisions.md", "bible/artefacts-register.md", "bible/open-questions.md"],
         "The secret canon. The canon decisions (D-numbers) settle questions the drafts must not contradict.")

assemble("06-rules-voices-pressures.md", "Hard rules, voices and modern pressures",
         ["CLAUDE.md", "bible/public-figures.md", "bible/voices.md", "bible/modern-pressures.md"],
         "The rules every chapter and ARG post must pass. From CLAUDE.md only the hard rules and the "
         "voice and style section are included.",
         parts={"CLAUDE.md": section("CLAUDE.md", "Hard rules") + "\n\n" + section("CLAUDE.md", "Voice & style")})

assemble("07-book-plan.md", "Book plan: synopsis, outline and resolution map",
         ["book/synopsis.md", "book/outline.md", "book/resolution-map.md", "book/act-2/scene-the-wall.md"],
         "Chapters 1-6 are drafted; 7-30 and the epilogue are planned. The outline's 'Threads and payoffs' "
         "table tracks every set-up.")

for path in sorted(glob.glob("book/chapters/[0-9][0-9]-*.md")):
    slug = os.path.basename(path)[:-3]
    num = slug[:2]
    text = body(path)
    split = text.find("---\n\n---\n\n## AUTHOR")
    story, notes = (text[:split], text[split:].replace("---\n\n---\n\n", "", 1)) if split >= 0 else (text, "")
    summary_path = os.path.join(OUT, "_written", "ch%s.md" % num)
    summary = open(summary_path, encoding="utf-8").read().strip() if os.path.exists(summary_path) else \
        "*(No summary yet: add one to %s.)*" % summary_path
    title = re.search(r"^# \w+: (.+)$", story, flags=re.M).group(1)
    parts = [header("Chapter %d: %s" % (int(num), title), [path]),
             "## Editor's summary\n\n" + summary,
             "\n---\n\n## Full text\n", story.strip()]
    if notes:
        parts += ["\n---\n", notes.strip()]
    write("%02d-chapter-%s.md" % (7 + int(num), slug), "\n\n".join(parts))

posts = sorted(glob.glob("content/phase-1/*.md")) + sorted(glob.glob("content/phase-2/*.md"))
assemble("14-arg-campaign.md", "The ARG campaign: plan, puzzles and in-world content",
         ["campaign/campaign-plan.md", "campaign/puzzle-map.md", "campaign/moderation-and-safety.md"] + posts,
         "In-world posts are written as if real; each has out-of-world production notes at the end. "
         "Every puzzle resolves to a campaign-owned page.")

if "--txt" in sys.argv:
    for f in glob.glob(os.path.join(OUT, "[0-9][0-9]-*.md")):
        open(f[:-3] + ".txt", "w", encoding="utf-8").write(open(f, encoding="utf-8").read())
    print("txt copies written")
