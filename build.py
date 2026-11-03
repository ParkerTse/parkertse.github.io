"""Build editorial pages from Markdown.

Reads _editorials/*.md (YAML front matter + Markdown body) and writes
editorials/<slug>.html plus editorials/index.html. Files starting with "_"
are skipped, so _editorials/_template.md never gets published.

    pip install -r requirements.txt
    python build.py
"""

import datetime
import html
import shutil
from pathlib import Path
from string import Template

import markdown
import yaml
from pygments.formatters import HtmlFormatter

ROOT = Path(__file__).parent
SRC = ROOT / "_editorials"
OUT = ROOT / "editorials"
TEMPLATES = ROOT / "templates"

MD_EXTENSIONS = [
    "tables",
    "toc",
    "pymdownx.superfences",
    "pymdownx.highlight",
    "pymdownx.arithmatex",
    "pymdownx.inlinehilite",
]
MD_CONFIG = {
    "pymdownx.highlight": {"css_class": "highlight"},
    "pymdownx.arithmatex": {"generic": True},
}

DIFFICULTIES = {"easy", "medium", "hard"}


def load_post(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise SystemExit(f"{path}: missing front matter")
    _, front, body = text.split("---", 2)
    meta = yaml.safe_load(front) or {}

    for key in ("title", "number", "difficulty", "date"):
        if key not in meta:
            raise SystemExit(f"{path}: front matter is missing '{key}'")
    if str(meta["difficulty"]).lower() not in DIFFICULTIES:
        raise SystemExit(f"{path}: difficulty must be Easy, Medium or Hard")
    if not isinstance(meta["date"], datetime.date):
        raise SystemExit(f"{path}: date must look like 2026-11-03")

    meta.setdefault("tags", [])
    meta.setdefault("link", "")
    meta["slug"] = path.stem
    meta["body"] = markdown.markdown(
        body, extensions=MD_EXTENSIONS, extension_configs=MD_CONFIG
    )
    return meta


def badge(difficulty):
    d = str(difficulty).lower()
    return f'<span class="badge badge-{d}">{html.escape(d.capitalize())}</span>'


def tag_list(tags):
    return "".join(f'<span class="tag">{html.escape(t)}</span>' for t in tags)


def pygments_css():
    light = HtmlFormatter(style="default").get_style_defs(".highlight")
    dark = HtmlFormatter(style="github-dark").get_style_defs(".highlight")
    return f"{light}\n\n@media (prefers-color-scheme: dark) {{\n{dark}\n}}\n"


def main():
    post_tpl = Template((TEMPLATES / "post.html").read_text(encoding="utf-8"))
    index_tpl = Template((TEMPLATES / "index.html").read_text(encoding="utf-8"))

    posts = [load_post(p) for p in sorted(SRC.glob("*.md")) if not p.name.startswith("_")]
    posts.sort(key=lambda p: (p["date"], p["number"]), reverse=True)

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    (OUT / "pygments.css").write_text(pygments_css(), encoding="utf-8")

    for p in posts:
        link = (
            f'<a href="{html.escape(p["link"])}" target="_blank" rel="noopener">View on LeetCode</a>'
            if p["link"]
            else ""
        )
        page = post_tpl.substitute(
            title=html.escape(f'{p["number"]}. {p["title"]}'),
            badge=badge(p["difficulty"]),
            tags=tag_list(p["tags"]),
            date=p["date"].strftime("%B %-d, %Y"),
            link=link,
            body=p["body"],
            year=datetime.date.today().year,
        )
        (OUT / f'{p["slug"]}.html').write_text(page, encoding="utf-8")

    if posts:
        rows = "\n".join(
            f'          <li>\n'
            f'            <a href="{p["slug"]}.html">{p["number"]}. {html.escape(p["title"])}</a>\n'
            f'            <span class="post-meta">{badge(p["difficulty"])}{tag_list(p["tags"])}'
            f'<time datetime="{p["date"].isoformat()}">{p["date"].strftime("%b %-d, %Y")}</time></span>\n'
            f'          </li>'
            for p in posts
        )
        listing = f'<ul class="post-list">\n{rows}\n        </ul>'
    else:
        listing = "<p><em>Coming soon.</em></p>"

    page = index_tpl.substitute(listing=listing, year=datetime.date.today().year)
    (OUT / "index.html").write_text(page, encoding="utf-8")
    print(f"Built {len(posts)} editorial(s) into {OUT.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
