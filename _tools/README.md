Regenerates every page of the documentation from the Balm Studio theme: labels, options, defaults, the version and the changelog are read from the theme, the prose lives in `content_studio.py` (Getting started, Sections and one page per section of the demo, More sections, Theme settings, Metafields, Features, FAQ, the changelog entry), `content_product.py` (Product page blocks) and `content_pages.py` (Custom code, Support).

Each time the theme changes, run from the repository root:

    python3 _tools/build.py /path/to/balm-theme && python3 _tools/check_dashes.py

The build stops when a section, a block or a theme settings group has no prose, when the prose documents one the theme no longer has, and when a name set in bold on a section page, a product block, Theme settings or Features is not a label of the theme.

The captures in `assets/shots/` come from the preview of the development theme, at 1440 x 900 (`name-desktop.jpg`) and 390 x 844 (`name-mobile.jpg`). To take them again (the storefront password in `STOREFRONT_PASSWORD`, Playwright from the theme's harness):

    HARNESS=/path/to/balm-theme/harness node _tools/shots.mjs

Review the diff, then commit and push to `main`: GitHub Pages republishes the site, and this `_tools` folder is never published.
