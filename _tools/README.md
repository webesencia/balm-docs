Regenerates every page of the documentation from the Balm theme: labels, options, defaults and the changelog are read from the theme, the prose lives in the `content_*.py` files.
Each time the theme changes, run from the repository root: `python3 _tools/build.py /path/to/balm-theme && python3 _tools/check_dashes.py`
Review the diff, then commit and push to `main`: GitHub Pages republishes the site, and this `_tools` folder is never published.
