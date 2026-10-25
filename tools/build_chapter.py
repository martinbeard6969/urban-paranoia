"""Typeset one chapter of Urban Paranoia as a book-style PDF.

Usage:
    python3 tools/build_chapter.py book/chapters/05-the-sensible-voice.md

Writes outputs/<same-name>.pdf. Needs reportlab (4.0.9 works on Python 3.9).

Chapter file conventions:
- Title line:      # Five: The Sensible Voice
- Narrator line:   **NELL · DAY 23,220 · MONDAY 11 MAY 2026**   (first block after the title)
- Section labels:  **THE ACTUARY · LE HAVRE, THE SAME NIGHT**   (a bold, all-capitals block)
- Section break:   ---
- Counsel:         > LINES IN CAPITALS
- Everything after "---\\n\\n---\\n\\n## AUTHOR" is notes and is not printed.
"""
import os
import re
import sys

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

AUTHOR = "Martin Defries"
PAGE = (138 * mm, 216 * mm)  # UK Demy trade paperback
GREY = colors.HexColor("#6B6E70")

SRC = sys.argv[1]
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(
    "outputs", "chapter-" + os.path.basename(SRC).replace(".md", ".pdf"))

text = open(SRC, encoding="utf-8").read()
m = re.search(r"^# (\w+): (.+)$", text, re.M)
NUMWORD, TITLE = m.group(1), m.group(2).strip()
end = text.index("---\n\n---\n\n## AUTHOR")
body = text[m.end():end].strip()

base = dict(fontName="Times-Roman", fontSize=10.5, leading=14.5, alignment=TA_JUSTIFY)
para = ParagraphStyle("p", firstLineIndent=5 * mm, **base)
para_first = ParagraphStyle("p0", firstLineIndent=0, **base)
counsel = ParagraphStyle("c", fontName="Courier", fontSize=9.5, leading=13, alignment=TA_CENTER, spaceBefore=6, spaceAfter=6)
brk = ParagraphStyle("b", fontName="Times-Roman", fontSize=10.5, leading=14.5, alignment=TA_CENTER, spaceBefore=6, spaceAfter=6)
num = ParagraphStyle("n", fontName="Times-Roman", fontSize=12, leading=16, alignment=TA_CENTER, textColor=GREY)
ttl = ParagraphStyle("t", fontName="Times-Italic", fontSize=22, leading=28, alignment=TA_CENTER)
narr = ParagraphStyle("nar", fontName="Times-Roman", fontSize=8.5, leading=12, alignment=TA_CENTER, textColor=GREY)
label = ParagraphStyle("lab", fontName="Times-Roman", fontSize=8.5, leading=12, alignment=TA_CENTER, textColor=GREY, spaceBefore=2, spaceAfter=8)
small = ParagraphStyle("bk", fontName="Times-Roman", fontSize=9, leading=12, alignment=TA_CENTER, textColor=GREY)
auth = ParagraphStyle("au", fontName="Times-Roman", fontSize=10, leading=14, alignment=TA_CENTER, textColor=GREY)
endline = ParagraphStyle("end", fontName="Times-Italic", fontSize=13, leading=18, alignment=TA_CENTER)

LABEL = re.compile(r"^\*\*([^*a-z]+)\*\*$")


def smart(s):
    s = re.sub(r'(^|[\s(\[])"', "\\1\u201c", s)
    s = s.replace('"', "\u201d")
    s = re.sub(r"(^|[\s(\[])'", "\\1\u2018", s)
    return s.replace("'", "\u2019")


def md(s):
    s = smart(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    s = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", s)
    return re.sub(r"\*([^*]+)\*", r"<i>\1</i>", s)


def spaced(s):
    # letter-spaced capitals for labels
    return "&nbsp;".join(s.split(" "))


blocks = [b.strip() for b in body.split("\n\n") if b.strip()]
story = [Spacer(1, 22 * mm), Paragraph("URBAN PARANOIA", small), Paragraph(AUTHOR, auth),
         Spacer(1, 12 * mm), Paragraph(NUMWORD.upper(), num), Spacer(1, 4 * mm), Paragraph(TITLE, ttl)]

if blocks and LABEL.match(blocks[0]):
    story += [Spacer(1, 3 * mm), Paragraph(smart(LABEL.match(blocks[0]).group(1)), narr)]
    blocks = blocks[1:]
story.append(Spacer(1, 12 * mm))

first = True
for block in blocks:
    if block == "---":
        story.append(Paragraph("*&nbsp;&nbsp;&nbsp;*&nbsp;&nbsp;&nbsp;*", brk))
        first = True
        continue
    lm = LABEL.match(block)
    if lm:
        story.append(Paragraph(smart(lm.group(1)), label))
        continue
    if block.startswith(">"):
        line = " ".join(l.lstrip("> ").strip() for l in block.splitlines())
        story.append(Paragraph(md(line), counsel))
        first = False
        continue
    t = md(" ".join(block.splitlines()))
    if block == "*Day 0.*":
        story += [Spacer(1, 4 * mm), Paragraph(t, endline)]
        continue
    if first:
        words = t.split(" ", 3)
        if len(words) > 3 and "<" not in " ".join(words[:3]):
            t = " ".join(w.upper() for w in words[:3]) + " " + words[3]
        story.append(Paragraph(t, para_first))
        first = False
    else:
        story.append(Paragraph(t, para))


def deco(c, doc):
    if doc.page == 1:
        return
    c.saveState()
    c.setFont("Times-Italic", 8.5)
    c.setFillColor(GREY)
    w, h = PAGE
    c.drawCentredString(w / 2, h - 12 * mm, "Urban Paranoia" if doc.page % 2 == 0 else TITLE)
    c.setFont("Times-Roman", 8.5)
    c.drawCentredString(w / 2, 9 * mm, str(doc.page))
    c.restoreState()


doc = SimpleDocTemplate(OUT, pagesize=PAGE, leftMargin=17 * mm, rightMargin=17 * mm, topMargin=19 * mm,
                        bottomMargin=17 * mm, title="Urban Paranoia: Chapter %s, %s" % (NUMWORD, TITLE),
                        author=AUTHOR)
doc.build(story, onFirstPage=deco, onLaterPages=deco)
print("written", OUT)
