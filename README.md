# parkertse.github.io

Personal site for Parker Tse. Plain static HTML/CSS, no build step.

- `index.html` &mdash; page content
- `style.css` &mdash; custom styles on top of [Pico.css](https://picocss.com/) (loaded via CDN)
- `assets/img/` &mdash; images

Pushing to `main` deploys automatically via `.github/workflows/deploy.yml`.

To preview locally, just open `index.html` in a browser, or run a tiny local server:

```
python3 -m http.server
```
