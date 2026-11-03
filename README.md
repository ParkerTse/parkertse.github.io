# parkertse.github.io

Personal site for Parker Tse. Plain static HTML/CSS, plus a small Markdown build for editorials.

- `index.html` &mdash; page content
- `style.css` &mdash; site styles
- `assets/img/` &mdash; images
- `_editorials/` &mdash; LeetCode editorials in Markdown (built into `editorials/`)
- `build.py`, `templates/` &mdash; turns the Markdown into HTML pages

## Writing an editorial

1. Copy `_editorials/_template.md` to `_editorials/<slug>.md` (e.g. `two-sum.md`) and fill it in.
   Files starting with `_` are never published.
2. Preview: `pip install -r requirements.txt`, then `python build.py && python3 -m http.server`
   and open http://localhost:8000/editorials/.
3. Commit the `.md` file and push. CI runs `build.py` before deploying; `editorials/` itself is gitignored.

Math goes in `$...$` / `$$...$$` (KaTeX), code in fenced blocks with a language (Pygments).

Pushing to `main` deploys automatically via `.github/workflows/deploy.yml`.

To preview locally, just open `index.html` in a browser, or run a tiny local server:

```
python3 -m http.server
```
