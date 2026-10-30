"""Build a Kindle-ready EPUB 3 of every drafted chapter of Urban Paranoia.

Usage:
    python3 tools/build_epub.py

Writes kindle/urban-paranoia.epub. Python standard library only. The chapter conventions are
those of tools/build_chapter.py; everything after "---\\n\\n---\\n\\n## AUTHOR" is notes and is left out.
Act headings are read from the PARTS table below, so update it if the act titles change.
"""
import datetime
import glob
import html
import os
import re
import uuid
import zipfile

TITLE = "Urban Paranoia"
AUTHOR = "Martin Defries"
OUT = "kindle/urban-paranoia.epub"
COVER = "book/cover/front.png"
BOOK_ID = "urn:uuid:" + str(uuid.uuid5(uuid.NAMESPACE_URL, "urban-paranoia-novel"))

# (first chapter number, heading, subtitle)
PARTS = [
    (1, "Act One", "The Long Weather"),
    (11, "Act Two", "Thirteen Chairs"),
    (21, "Act Three", "Interesting"),
    (31, "Epilogue", ""),
]

CSS = """
body { margin: 0; line-height: 1.4; }
p { margin: 0; text-indent: 1.3em; }
p.first, p.line { text-indent: 0; }
h1 { font-size: 1.6em; font-weight: normal; font-style: italic; text-align: center; margin: 0.3em 0 1em; }
.num { font-size: 1em; text-align: center; text-indent: 0; margin-top: 3em; color: #555; }
.narrator, .label { font-size: 0.75em; letter-spacing: 0.08em; text-align: center; text-indent: 0; color: #555; }
.narrator { margin: 0 0 2.5em; }
.label { margin: 1.5em 0; }
.break { text-align: center; text-indent: 0; margin: 1.2em 0; }
.counsel { font-family: monospace; text-align: center; text-indent: 0; margin: 1em 0; }
.document { font-family: monospace; font-size: 0.9em; text-align: left; text-indent: 0; margin: 0;
            padding: 0.35em 0.8em; border-left: 1px solid #777; border-right: 1px solid #777; }
.document.top { margin-top: 1em; border-top: 1px solid #777; padding-top: 0.6em; }
.document.bottom { margin-bottom: 1em; border-bottom: 1px solid #777; padding-bottom: 0.6em; }
.part { text-align: center; margin-top: 30%; }
.part h1 { margin-bottom: 0.3em; }
.part p { text-indent: 0; text-align: center; }
.front { text-align: center; margin-top: 25%; }
.front p { text-indent: 0; text-align: center; margin-bottom: 0.8em; }
.small { font-size: 0.8em; }
.cover { text-align: center; margin: 0; padding: 0; }
.cover img { max-width: 100%; max-height: 100%; }
nav ol { list-style-type: none; padding-left: 1em; }
"""

LABEL = re.compile(r"^\*\*([^*a-z]+)\*\*$")
WORDS = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]


def smart(s):
    s = re.sub(r'(^|[\s(\[*])"', "\\1\u201c", s)
    s = s.replace('"', "\u201d")
    s = re.sub(r"(^|[\s(\[*])'", "\\1\u2018", s)
    return s.replace("'", "\u2019")


def inline(s):
    s = smart(html.escape(s, quote=False))
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"\*(.+?)\*", r"<i>\1</i>", s)
    s = re.sub(r"~~(.+?)~~", r"<s>\1</s>", s)
    return re.sub(r"`(.+?)`", r"\1", s)


def page(title, body, extra=""):
    return ('<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE html>\n'
            '<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" '
            'lang="en-GB" xml:lang="en-GB">\n<head><meta charset="utf-8"/><title>%s</title>'
            '<link rel="stylesheet" type="text/css" href="style.css"/>%s</head>\n<body>\n%s\n</body>\n</html>\n'
            % (html.escape(title), extra, body))


def chapter_html(path):
    text = open(path, encoding="utf-8").read()
    m = re.search(r"^# ([^:\n]+): (.+)$", text, re.M)
    word, name = m.group(1).strip(), m.group(2).strip()
    body = text[m.end():text.index("---\n\n---\n\n## AUTHOR")].strip()
    out = ['<p class="num">%s</p>' % html.escape(word), "<h1>%s</h1>" % inline(name)]
    first, seen_narrator = True, False
    for block in re.split(r"\n\s*\n", body):
        block = block.strip()
        if not block:
            continue
        if block == "---":
            out.append('<p class="break">* * *</p>')
            first = True
            continue
        lab = LABEL.match(block)
        if lab:
            out.append('<p class="%s">%s</p>' % ("label" if seen_narrator else "narrator", inline(lab.group(1))))
            seen_narrator, first = True, True
            continue
        lines = block.split("\n")
        if lines[0].startswith(">>"):
            out += ['<p class="document">%s</p>' % inline(ln.lstrip("> ")) for ln in lines]
            first = True
            continue
        if lines[0].startswith(">"):
            for ln in lines:
                out.append('<p class="counsel">%s</p>' % inline(ln.lstrip("> ")))
            first = True
            continue
        cls = ' class="first"' if first else ""
        out.append("<p%s>%s</p>" % (cls, "<br/>".join(inline(ln) for ln in lines)))
        first = False
    # A run of document lines is one ruled box, so only its ends get the top and bottom rules.
    is_doc = [x.startswith('<p class="document">') for x in out]
    for i, doc in enumerate(is_doc):
        if doc:
            cls = "document"
            if not is_doc[i - 1]:
                cls += " top"
            if i == len(out) - 1 or not is_doc[i + 1]:
                cls += " bottom"
            out[i] = out[i].replace('class="document"', 'class="%s"' % cls)
    return word, name, "\n".join(out)


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    chapters = []
    for path in sorted(glob.glob("book/chapters/[0-9][0-9]-*.md")):
        n = int(os.path.basename(path)[:2])
        chapters.append((n,) + chapter_html(path))

    items, spine, toc = [], [], []

    def add(fname, title, content, props=""):
        items.append((fname, content, props))
        spine.append(fname)

    add("cover.xhtml", "Cover", page("Cover", '<div class="cover"><img src="cover.png" alt="Cover of %s"/></div>' % TITLE))
    add("title.xhtml", "Title", page(TITLE, '<div class="front"><h1>%s</h1><p>%s</p></div>' % (TITLE, AUTHOR)))
    add("copyright.xhtml", "Copyright", page("Copyright", (
        '<div class="front small"><p>Copyright \u00a9 2026 %s</p>'
        "<p>This is a work of fiction. The Lodge, the Tenants and every person, company and organisation "
        "in this story are invented. Any resemblance to real people or organisations is coincidental.</p>"
        "<p>Review copy. Draft text, chapters 1 to %d.</p></div>" % (AUTHOR, chapters[-1][0]))))

    for n, word, name, content in chapters:
        for start, part, sub in PARTS:
            if start == n:
                fname = "part-%02d.xhtml" % n
                subtitle = "<p>%s</p>" % html.escape(sub) if sub else ""
                add(fname, part, page(part, '<div class="part"><h1>%s</h1>%s</div>' % (part, subtitle)))
                toc.append((part + (": " + sub if sub else ""), fname, []))
        fname = "chapter-%02d.xhtml" % n
        add(fname, name, page(name, content))
        toc[-1][2].append(("%s: %s" % (word, name), fname))

    nav = ['<nav epub:type="toc" id="toc"><h1>Contents</h1><ol>']
    for part, fname, kids in toc:
        nav.append('<li><a href="%s">%s</a><ol>' % (fname, html.escape(part)))
        nav += ['<li><a href="%s">%s</a></li>' % (f, html.escape(t)) for t, f in kids]
        nav.append("</ol></li>")
    nav.append("</ol></nav>")
    nav.append('<nav epub:type="landmarks" hidden="hidden"><ol>'
               '<li><a epub:type="cover" href="cover.xhtml">Cover</a></li>'
               '<li><a epub:type="toc" href="nav.xhtml">Contents</a></li>'
               '<li><a epub:type="bodymatter" href="%s">Start</a></li></ol></nav>' % toc[0][1])
    items.append(("nav.xhtml", page("Contents", "\n".join(nav)), "nav"))
    spine.insert(3, "nav.xhtml")

    # toc.ncx, for older Kindle readers
    points, order = [], 1
    for part, fname, kids in toc:
        inner = []
        points.append('<navPoint id="p%d" playOrder="%d"><navLabel><text>%s</text></navLabel><content src="%s"/>'
                      % (order, order, html.escape(part), fname))
        order += 1
        for t, f in kids:
            inner.append('<navPoint id="p%d" playOrder="%d"><navLabel><text>%s</text></navLabel><content src="%s"/></navPoint>'
                         % (order, order, html.escape(t), f))
            order += 1
        points.append("".join(inner) + "</navPoint>")
    ncx = ('<?xml version="1.0" encoding="utf-8"?>\n<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">'
           '<head><meta name="dtb:uid" content="%s"/></head><docTitle><text>%s</text></docTitle><navMap>%s</navMap></ncx>\n'
           % (BOOK_ID, TITLE, "".join(points)))

    manifest = ['<item id="css" href="style.css" media-type="text/css"/>',
                '<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>',
                '<item id="cover-image" href="cover.png" media-type="image/png" properties="cover-image"/>']
    for fname, _, props in items:
        p = ' properties="%s"' % props if props else ""
        manifest.append('<item id="%s" href="%s" media-type="application/xhtml+xml"%s/>' % (fname.replace(".xhtml", ""), fname, p))
    refs = "\n".join('<itemref idref="%s"/>' % f.replace(".xhtml", "") for f in spine)
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    opf = ('<?xml version="1.0" encoding="utf-8"?>\n'
           '<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid" xml:lang="en-GB">\n'
           '<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">'
           '<dc:identifier id="bookid">%s</dc:identifier><dc:title>%s</dc:title><dc:creator>%s</dc:creator>'
           '<dc:language>en-GB</dc:language><meta property="dcterms:modified">%s</meta>'
           '<meta name="cover" content="cover-image"/></metadata>\n<manifest>\n%s\n</manifest>\n'
           '<spine toc="ncx">\n%s\n</spine>\n</package>\n'
           % (BOOK_ID, TITLE, AUTHOR, stamp, "\n".join(manifest), refs))
    container = ('<?xml version="1.0" encoding="utf-8"?>\n'
                 '<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">'
                 '<rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>'
                 '</rootfiles></container>\n')

    with zipfile.ZipFile(OUT, "w") as z:
        z.writestr(zipfile.ZipInfo("mimetype"), "application/epub+zip", zipfile.ZIP_STORED)
        z.writestr("META-INF/container.xml", container, zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/content.opf", opf, zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/toc.ncx", ncx, zipfile.ZIP_DEFLATED)
        z.writestr("OEBPS/style.css", CSS, zipfile.ZIP_DEFLATED)
        z.write(COVER, "OEBPS/cover.png", zipfile.ZIP_DEFLATED)
        for fname, content, _ in items:
            z.writestr("OEBPS/" + fname, content, zipfile.ZIP_DEFLATED)
    print("written %s (%d chapters, %d KB)" % (OUT, len(chapters), os.path.getsize(OUT) // 1024))


main()
