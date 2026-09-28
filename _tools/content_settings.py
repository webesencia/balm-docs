INTRO = ('Theme settings apply to the whole store. Open them in the theme editor with the '
         '<strong>Theme settings</strong> icon (the gear) in the left bar. The groups below follow the order of the '
         'editor, and every label is written exactly as the editor shows it. The Default column gives the theme\'s '
         'built in value; the <a href="index.html#preset">Balm preset</a>, which your store starts from, replaces the '
         'colors, fonts, corners, glass and typography values with its own.')

GROUPS = {
    'Colors': '''
<p>Balm organizes its colors in <strong>color schemes</strong>. A scheme is a set of seven colors designed to work
together, and every section, popup and drawer picks one scheme with its own <strong>Color scheme</strong> setting.
Edit a scheme here and every place that uses it follows.</p>
<p>The Balm preset ships two schemes. Scheme 1 is the main one, white; Scheme 2 is its contrasting partner, near
black. Add as many schemes as you need with <strong>Add scheme</strong>.</p>
<ul>
  <li><strong>Background</strong>: the section background. <strong>Background gradient</strong> is optional and replaces it where set.</li>
  <li><strong>Text</strong>: body text, headings and icons.</li>
  <li><strong>Button / accent</strong> and <strong>Button label</strong>: the fill and the text of primary buttons.</li>
  <li><strong>Secondary background</strong>: the second surface of the scheme, used by cards, drawers, panels, inputs
  and secondary buttons. Balm derives a raised tone and a hairline from it, so dark schemes keep visible layers.</li>
  <li><strong>Accent (links / highlights)</strong>: links and highlighted details.</li>
</ul>
<p>Keep the text and button colors readable on their background: aim for a contrast ratio of at least 4.5:1 for
body text. Glass surfaces measure their own contrast and switch the label to black or white when needed, but plain
surfaces use exactly the colors you set.</p>
''',
    'Typography': '''
<p>Two fonts drive the whole theme: the <strong>Heading font</strong> for headings and titles, and the
<strong>Body font</strong> for paragraphs, forms and everything else. Both come from the Shopify font library, so they
are served by Shopify and free to use on your store.</p>
<p>Three shared recipes follow. <strong>Headings</strong> sets the case, the slant and the weight of every display
heading. <strong>Button labels</strong> sets the case, weight, letter spacing and slant of every button.
<strong>Labels and small text</strong> sets the case of eyebrows, badges, prices, filters, variant pills, the
announcement bar, the footer links and the main menu. Because the recipes are global, a section title, a product card
and a page title always speak with the same voice.</p>
<p>Not every family offers every weight or an italic. When a family lacks the face you ask for, the browser uses the
closest one it has, or slants an upright face. The help text of <strong>Heading style</strong> lists the weights
available in italic for the default font.</p>
''',
    'Corner style': '''
<p>Four sliders set the maximum corner radius of the whole theme: <strong>Buttons and pills</strong>,
<strong>Cards and panels</strong>, <strong>Form fields</strong> and <strong>Images and media</strong>. Each value is a
ceiling: elements designed with smaller corners keep them, and 0 gives square corners everywhere. Section settings that
carry their own radius, such as the floating header or the cart drawer, are capped by these values too.</p>
<p>The Balm preset sets buttons and form fields to 12 px, cards and media to 20 px.</p>
''',
    'Product badges': '''
<p>Four badges can sit on the product cards, in quick view, in Compare products and on the product page.
<strong>Sale</strong> shows automatically when the compare-at price is above the price, <strong>Sold out</strong> when
the product can no longer be bought. <strong>New</strong> is off by default: set <strong>New badge</strong> to
<strong>Product tag</strong> and name the tag, or to <strong>Created in the last X days</strong> and set the number of
days. <strong>Custom</strong> prints the product's <code>custom.badge_label</code> metafield, read directly. This group
sets their position, shape and colors once for the whole store.</p>
<p>On the product page, turn on <strong>Badges on media</strong> in the Product section, or add a <strong>Badge</strong>
block. See <a href="features.html#product-badges">Product badges</a> for the full walkthrough.</p>
''',
    'Pre-order': '''
<p>Pre-order turns itself on for a variant whose quantity is tracked, whose stock is at 0 and that has
<strong>Continue selling when out of stock</strong> checked. The add to cart button, the sticky add to cart bar and the
quick add button then read <strong>Pre-order</strong>, or the label you type here. See
<a href="features.html#pre-order">Pre-order</a>.</p>
''',
    'Quick view': '''
<p>Quick view opens a product in a modal from its card, so shoppers can pick a variant and add to cart without leaving
the page. This group sets what the modal shows and how it looks. You turn it on per section, with the
<strong>Quick view</strong> setting of the Collection, Featured collection, Search, Recently viewed and Lookbook
sections. See <a href="features.html#quick-view">Quick view</a>.</p>
''',
    'Gift wrapping': '''
<p>Adds a gift wrapping checkbox, and an optional gift message, to the cart drawer and the cart page. The wrapping is a
real product you create in your admin, so its price, taxes and stock work like any other product. See
<a href="features.html#gift-wrapping">Gift wrapping</a> for the setup.</p>
''',
    'Back to top': '''
<p>A round button in a bottom corner that scrolls back to the top of the page. It appears after the visitor has
scrolled the distance set in <strong>Show after scrolling</strong>, can be turned on for desktop and mobile separately,
lifts above the sticky add to cart bar and steps aside from the hero video controls. Visitors who ask their device for
reduced motion get an instant jump instead of a smooth scroll.</p>
''',
    'Age verifier': '''
<p>A modal that asks visitors to confirm their age before they browse the store, for brands that sell alcohol, tobacco
or other age restricted products. The answer is remembered in the visitor's browser for the number of days you choose.
See <a href="features.html#age-verifier">Age verifier</a>.</p>
''',
    'Glass effect': '''
<p>One frosted glass recipe shared by every glass surface of the theme: the glass header and mega menu, the announcement
bar in Glass style, glass buttons, the popups and the cart drawer when they use a glass card. Set the
<strong>Tint</strong>, <strong>Fill opacity</strong>, <strong>Blur</strong> and <strong>Border opacity</strong> once
and every surface moves together.</p>
<p><strong>Glass on phones</strong> decides what happens on screens under 768 px wide: Frosted keeps the blur, Near
opaque swaps it for an almost solid fill that is lighter to scroll on older phones. Browsers without backdrop blur and
visitors who ask for reduced transparency always get the near opaque fill.</p>
''',
    'Loader': '''
<p>The <strong>Page loader</strong>: an optional loading screen shown while pages open, with your logo, a progress bar
(square or rounded ends, 1 to 6 px, with a None, Smooth or Shimmer animation) or a spinner, and an exit animation. It is the theme's only loader, and it covers everything on the page, the header
and the announcement bar included. See <a href="features.html#page-loader">Page loader</a>.</p>
''',
    'Favicon': '''
<p>The small icon shown in browser tabs and bookmarks. Upload a square image of at least 32 by 32 pixels; a PNG with a
transparent background works best.</p>
''',
    'Social sharing': '''
<p>Controls how your pages look when someone shares a link on social media or in a messaging app. Product, collection
and blog post pages use their own featured image. The <strong>Fallback share image</strong> covers every other page,
and the <strong>X (Twitter) account</strong> is shown as the source of shared cards.</p>
''',
    'Breadcrumbs': '''
<p>A trail of links back to the home page, shown on product, collection and blog post pages. Position, separator and
alignment are set here for the whole store. The Product, Collection and Article sections each have a
<strong>Breadcrumbs on this page</strong> setting that shows or hides the trail on that page type only.</p>
''',
    'Search': '''
<p><strong>Search scope</strong> decides what the storefront searches, both in the header suggestions and on the
results page. Products only keeps the results page to product cards, which is also what the search filters need.
Products, articles and pages adds your blog posts and pages to the results.</p>
''',
    'Search engines': '''
<p>Shopify already tells search engines to treat a filtered or sorted collection URL as the plain collection URL.
Internal search results pages are not covered by default, and they rarely deserve a place in Google. This setting
adds a noindex instruction to them, and optionally to filtered collections too.</p>
''',
}
