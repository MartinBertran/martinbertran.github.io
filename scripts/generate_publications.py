# scripts/generate_publications.py
"""
Generate Markdown files for every Google Scholar paper
author: Martin Bertran
usage:  python scripts/generate_publications.py
"""
from pathlib import Path
from datetime import datetime
import re, html, textwrap, json
from slugify import slugify
from scholarly import scholarly  # https://pypi.org/project/scholarly/ :contentReference[oaicite:0]{index=0}

AUTHOR_ID = "1kki_voAAAAJ"               # your Scholar ID
OUT_DIR   = Path("_publications")        # AcademicPages directory
OUT_DIR.mkdir(exist_ok=True)

BIB_DIR = Path("files/bibtex")          # ← Git-tracked assets
BIB_DIR.mkdir(parents=True, exist_ok=True)

def _bibtex_key(slug, year):
    """create a unique, BibTeX‑safe key like bertran2025-privacy"""
    return re.sub(r"[^a-zA-Z0-9]", "", slug)[:20] + str(year)

def _to_bibtex(entry, slug, year, venue):
    """minimal @article/@misc fallback"""
    authors = entry["bib"].get("author", "Unknown").replace("…,"," and").replace("…"," and")
    key = _bibtex_key(slug, year)
    bt = (
        f"@misc{{{key},\n"
        f"  title={{\"{entry['bib']['title']}\"}},\n"
        f"  author={{\"{authors}\"}},\n"
        f"  year={{\"{year}\"}},\n"
        f"  howpublished={{\"{venue}\"}},\n"
        f"}}\n"
    )
    return bt

def first_safe(d, *keys):
    """return first present key or blank"""
    for k in keys:
        if k in d and d[k]:
            return d[k]
    return ""

# def fmt_front_matter(p):
#     bib  = p["bib"]
#     year = int(bib.get("pub_year", datetime.now().year))
#     month = 1      # Scholar has year only; default to Jan 1
#     day   = 1
#     date  = f"{year:04d}-{month:02d}-{day:02d}"
#     title = bib["title"]
#     slug  = slugify(title)[:60]
#     permalink = f"/publication/{date}-{slug}"
#     venue = first_safe(bib, "journal", "venue", "publisher")
#     citation = scholarly.bibtex(p)  # raw BibTeX → prettify if you like

#     escaped_title = title.replace('"', r'\"')   # r'\"' avoids back‑slashes in the f‑string

#     md = f"""---
#     title: "{escaped_title}"
#     collection: publications
#     permalink: {permalink}
#     date: {date}
#     venue: "{venue}"
#     excerpt: ""
#     paperurl: "{first_safe(p, 'pub_url')}"
#     bibtexurl: ""
#     slidesurl: ""
#     citation: "{html.escape(venue)}"
#     ---

#     <!-- more details can go here -->
#     """
#     return date, slug, md

def fmt_front_matter(p):
    """Return (date, slug, markdown_text) for one publication dict."""
    bib  = p["bib"]
    year = int(bib.get("pub_year", datetime.now().year))
    date = f"{year:04d}-01-01"              # Scholar gives only the year
    title = bib["title"]
    slug  = slugify(title)[:60]
    permalink = f"/publication/{date}-{slug}"

    # ------- simple citation fallback ---------
    authors = bib.get("author", "Unknown").replace("…", "et al.")
    venue   = bib.get("journal") or bib.get("venue") or bib.get("conference") or bib.get("publisher", "")
    citation = f"{authors}. “{title}.” {venue}."

    # ------- write BibTeX file & path -------
    bibtex_text = _to_bibtex(p, slug, year, venue)
    bib_path = BIB_DIR / f"{slug}.bib"
    bib_path.write_text(bibtex_text, encoding="utf‑8")
    bibtexurl = f"/{bib_path.as_posix()}"        # '/files/bibtex/<slug>.bib'

    # escape quotes for YAML
    escaped_title = title.replace('"', r'\"')
    escaped_venue = venue.replace('"', r'\"')
    escaped_cite  = citation.replace('"', r'\"')

    md = f"""---
title: "{escaped_title}"
category: manuscripts
collection: publications
permalink: {permalink}
date: {date}
venue: "{escaped_venue}"
excerpt: ""
paperurl: "{p.get('pub_url', '')}"
bibtexurl: "{bibtexurl}"
citation: "{escaped_cite}"
---

<!-- add abstract or notes here -->
"""
    return date, slug, md

def main():
    print("Fetching author profile…")
    auth = scholarly.fill(scholarly.search_author_id(AUTHOR_ID))
    pubs = auth["publications"]
    print(f"Found {len(pubs)} publications")
    for pub in pubs:
        pub_filled = scholarly.fill(pub)
        date, slug, text = fmt_front_matter(pub_filled)
        fn = OUT_DIR / f"{date}-{slug}.md"
        fn.write_text(text, encoding="utf‑8")
        print("✓", fn.name)

if __name__ == "__main__":
    main()
