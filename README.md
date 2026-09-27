# Balm theme documentation

Public documentation of the Balm Shopify theme, published with GitHub Pages at
https://balm.webesencia.com/

The site is plain HTML and CSS with one small script for the search and the mobile menu.
The pages are generated from the theme by the scripts in `_tools/` (see `_tools/README.md`);
GitHub Pages serves the generated files as they are and does not publish `_tools/`.

- `index.html` and the other `.html` files: the pages
- `assets/style.css`: the shared stylesheet
- `assets/docs.js`: search, mobile menu, settings opened on a deep link
- `assets/search-index.js`: the search index
- `assets/inter-latin.woff2`: the Inter typeface, under the SIL Open Font License (`assets/inter-OFL.txt`)

To publish: Settings, Pages, deploy from the `main` branch, root folder. The `CNAME` file
serves the site at the root of balm.webesencia.com: pages link to each other relatively, and
`404.html`, which GitHub Pages serves for a missing path at any depth, links from the
domain root.
