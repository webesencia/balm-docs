INTRO = ('Theme settings apply to the whole store. Open them in the theme editor with the '
         '<strong>Theme settings</strong> icon (the gear) in the left bar. The groups below follow the order of the '
         'editor, and every label is written exactly as the editor shows it. The Default column gives the theme\'s '
         'built in value; the <a href="index.html#preset">Balm Studio preset</a>, which your store starts from, replaces the '
         'colors, fonts, corners, glass and typography values with its own.')

GROUPS = {
    'Colors': '''
<p>Balm Studio organizes its colors in <strong>color schemes</strong>. A scheme is a set of seven colors designed to work
together, and every section, popup and drawer picks one scheme with its own <strong>Color scheme</strong> setting.
Edit a scheme here and every place that uses it follows.</p>
<p>The Balm Studio preset ships two schemes. Scheme 1 is the main one, white; Scheme 2 is its contrasting partner, near
black. Add as many schemes as you need with <strong>Add scheme</strong>.</p>
<ul>
  <li><strong>Background</strong>: the section background. <strong>Background gradient</strong> is optional and replaces it where set.</li>
  <li><strong>Text</strong>: body text, headings and icons.</li>
  <li><strong>Button / accent</strong> and <strong>Button label</strong>: the fill and the text of primary buttons.</li>
  <li><strong>Secondary background</strong>: the second surface of the scheme, used by cards, drawers, panels, inputs
  and secondary buttons. Balm Studio derives a raised tone and a hairline from it, so dark schemes keep visible layers.</li>
  <li><strong>Accent (links / highlights)</strong>: links and highlighted details.</li>
</ul>
<p>Keep the text and button colors readable on their background: aim for a contrast ratio of at least 4.5:1 for
body text. Glass surfaces measure their own contrast and switch the label to black or white when needed, but plain
surfaces use exactly the colors you set.</p>
''',
    'Typography': '''
<p>Two fonts drive the whole theme: the <strong>Heading font</strong> for headings and titles, and the
<strong>Body font</strong> for paragraphs, forms and everything else. Both come from the Shopify font library, so they
are served by Shopify and free to use on your store. The Balm Studio preset pairs Outfit 400 for headings with Inter for body
text.</p>
<p><strong>Type sizes.</strong> Balm Studio sets its text on one fluid scale. Every size has a mobile value, reached on a
screen 390 px wide, and a desktop value, reached at 1440 px. In between, the size grows in a straight line; outside
that range, it holds at the nearer value. On the scale, the product title runs from 32 to 44 px, section headings from
26 to 36 px, card titles from 15 to 17 px, body text from 15 to 16 px and small text from 12 to 13 px, each level with
its own line height and letter spacing.</p>
<p>The text size settings of sections and blocks follow the same rule: the value of a setting ending in
<strong>(mobile)</strong> applies at 390 px, the one ending in <strong>(desktop)</strong> at 1440 px, and the size moves
smoothly between them. Their defaults sit on the scale, so a section you add matches the rest of the page. The
announcement bar and the mega menu are the exceptions: they switch from one value to the other at the menu breakpoint,
1200 px, where the header changes menus. Decorative texts, such as the text behind cutouts of the product page or the
two words across the Gallery banner, keep their own desktop and mobile sizes, off the scale.</p>
<p><strong>Heading scale</strong> and <strong>Body scale</strong> (80 to 130%, 100% by default) multiply every size at
once, the sizes set in sections and blocks included. Heading scale acts on headings, titles and product card titles;
Body scale on body text, buttons, labels and prices. Set Heading scale to 110% and every heading of the store grows by
a tenth, without opening a single section.</p>
<p>Three shared recipes follow. <strong>Headings</strong> sets the case, the slant and the weight of every display
heading. <strong>Button labels</strong> sets the case, weight, letter spacing and slant of every button.
<strong>Labels and small text</strong> sets the case of eyebrows, badges, prices, filters, variant pills, the
announcement bar, the footer links and the main menu. Because the recipes are global, a section title, a product card
and a page title always speak with the same voice.</p>
<p>Not every family offers every weight or an italic. When a family lacks the face you ask for, the browser uses the
closest one it has, or slants an upright face. Outfit, the heading font of the Balm Studio preset, has no italic at all: with
<strong>Heading style</strong> set to Italic, its letters are slanted by the browser. For true italic headings, pick a
heading font whose family includes italics.</p>
''',
    'Layout': '''
<p><strong>Page width</strong> sets how wide the content of the product, collection and search pages can grow, together
with the Featured collection, Product recommendations and Recently viewed sections.</p>
<ul>
  <li><strong>Standard</strong>, the default: 1400 px at most, centered.</li>
  <li><strong>Wide</strong>: 1600 px at most.</li>
  <li><strong>Full width with margins</strong>: the whole screen, less the side margins of the header. The page
  content, the breadcrumbs and the footer then line up with the logo and the icons of the header, a floating header
  included.</li>
</ul>
<p>Product card images are served at the size the chosen width draws them, so cards stay sharp on a wider page. The
other sections set their own width with their <strong>Section width</strong> setting, whose Page width option stops at
the width chosen here: see <a href="sections.html#section-width">Section width</a>.</p>
''',
    'Buttons': '''
<p>One recipe for every button of the theme, primary and secondary. <strong>Size</strong> (Small, Medium by default,
or Large) sets the height, the padding and the text size on desktop and on mobile, one step down or up the
<a href="#ts-typography">type scale</a> from Medium. A Small button keeps a tap area of 44 px around it.
<strong>Border width</strong> (1 or 2 px) applies to outline buttons, and <strong>Font weight</strong> (Regular, Medium
or Semibold) to every label.</p>
<p>The case, letter spacing and slant of the labels are set in <a href="#ts-typography">Typography</a>, the corners in
<a href="#ts-corner-style">Corner style</a>. A few buttons can step out of the shared size: the Buy buttons block of the
product page (<strong>Button size</strong>), the quick add button of the cards (<strong>Size</strong> in
<a href="#ts-product-cards">Product cards</a>) and the button of a Products showcase spotlight. Each offers
<strong>Follow buttons</strong>, which keeps this setting.</p>
''',
    'Product cards': '''
<p>One look for the product cards of the Collection, Search, Featured collection, Product recommendations, Recently
viewed and Lookbook sections, set once here.</p>
<ul>
  <li><strong>Sizes.</strong> The title and price sizes, on desktop and on mobile. The defaults sit on the
  <a href="#ts-typography">type scale</a>: titles 17 px on desktop and 15 px on mobile, prices 16 and 14 px, with the
  compare-at price at 85% of the price. Heading scale applies to the titles, Body scale to the prices. The cards of the
  404 page follow them too; the Complementary products block of the product page keeps its own title size.</li>
  <li><strong>Image.</strong> <strong>Hover effect</strong> decides what a mouse does to the picture. With
  <strong>Second image on hover</strong> turned on in the section, <strong>Fade</strong> crossfades the product's two
  images and <strong>Swap</strong> changes them at once. <strong>Zoom</strong> enlarges the image, and crossfades to the
  second one when it is on.</li>
  <li><strong>Quick add button.</strong> The style of the card button (Add to cart, Choose options, Shop now): Solid,
  Outline, Text link, Glass or Icon only (a bag icon), Auto or Full width, below the product details or on the image
  (shown on hover on desktop, always on touch screens), and the button colors of the color scheme or your own. Its size
  follows <a href="#ts-buttons">Buttons</a> unless you pick one here. Where the button shows is set per section, with
  <strong>Quick add</strong>.</li>
</ul>
<h3 id="ts-product-cards-cutouts">Text behind cutouts on the cards</h3>
<p>The product's title, or its <code>custom.tagline</code> metafield, can stand as a large decorative text behind the
picture of each card of a collection grid, seen through the transparent areas of PNG and WebP images. JPG images never
get it. The Collection section decides where it shows, with <strong>Text behind cutouts</strong>,
<strong>Show on desktop</strong> and <strong>Show on mobile</strong>; this group sets its look for every card at once:
<strong>Text</strong>, <strong>Font</strong>, <strong>Font weight</strong>, <strong>Text case</strong>,
<strong>Letter spacing</strong>, <strong>Line height</strong>, <strong>Lines</strong>, the vertical and horizontal
position per device, the <strong>Text color</strong> (the scheme text, the product's
<code>custom.background_color_end</code> metafield or a custom color), <strong>Text opacity</strong> (15% by default)
and <strong>Text style</strong>, Solid or Outline with its thickness. The text is hidden from screen readers. The
product page has its own version of it: see <a href="product-page.html#text-behind-cutouts">Text behind cutout
images</a>.</p>
''',
    'Corner style': '''
<p>Four sliders set the maximum corner radius of the whole theme: <strong>Buttons and pills</strong>,
<strong>Cards and panels</strong>, <strong>Form fields</strong> and <strong>Images and media</strong>. Each value is a
ceiling: elements designed with smaller corners keep them, and 0 gives square corners everywhere. Section settings that
carry their own radius, such as the floating header or the cart drawer, are capped by these values too.</p>
<p>The Balm Studio preset sets buttons and form fields to 12 px, cards and media to 20 px.</p>
''',
    'Product badges': '''
<p>Four badges can sit on the product cards, in quick view, in Compare products and on the product page.
<strong>Sale</strong> shows automatically when the compare-at price is above the price, <strong>Sold out</strong> when
the product can no longer be bought. <strong>New</strong> is off by default: set <strong>New badge</strong> to
<strong>Product tag</strong> and name the tag, or to <strong>Created in the last X days</strong> and set the number of
days. <strong>Custom</strong> prints the product's <code>custom.badge_label</code> metafield, read directly. This group
sets their position, shape and colors once for the whole store.</p>
<p>A product can give its Custom badge its own colors through two optional Color metafields,
<code>custom.badge_color</code> (background) and <code>custom.badge_text_color</code> (text). Left empty, the badge
uses <strong>Custom background</strong> and <strong>Custom text</strong> from this group. With a background and no text
color, the text turns dark or light by itself, at a contrast of at least 4.5:1. See
<a href="features.html#custom-badge-colors">Give one product its own badge colors</a>.</p>
<p>On the product page, turn on <strong>Badges on media</strong> in the Product section, or add a <strong>Badge</strong>
block. Every section that shows product cards has its own <strong>Badges</strong> setting (All, Automatic only, Custom
only or None) to keep some of them, or none, in that section: see
<a href="features.html#badges-per-section">Choose the badges of each section</a>. See
<a href="features.html#product-badges">Product badges</a> for the full walkthrough.</p>
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
    'Cart': '''
<p>The whole cart is set up here, once: the drawer, the notification and the cart page share these settings, so the
Cart drawer section has none of its own.</p>
<ul>
  <li><strong>Cart type</strong>: <strong>Drawer</strong> (the default) slides a panel in after each add,
  <strong>Page</strong> opens the cart page, <strong>Notification</strong> confirms the add with the line just added,
  View cart and Check out.</li>
  <li><strong>Drawer and notification</strong>: <strong>Style</strong> Solid (the color scheme's background) or Glass
  (the <a href="#ts-glass-effect">Glass effect</a> over the whole drawer, top to bottom). <strong>Floating
  drawer</strong>, on by default, detaches the drawer and the notification from the screen edges by the margins you set
  for desktop and mobile, with the corners of <a href="#ts-corner-style">Corner style</a>. Panel width, paddings,
  heading and title sizes, thumbnail size and <strong>Line density</strong> (Comfortable, or Compact for a smaller
  thumbnail and tighter lines, in the drawer and on the cart page) follow.</li>
  <li><strong>Colors</strong>: <strong>Text colors</strong> on Color scheme keeps the scheme's text; on Auto, the cart
  reads its real background, glass included, and keeps the scheme text when it reaches 4.5:1, otherwise white or
  black.</li>
  <li><strong>Free shipping bar</strong>: progress toward the <strong>Free shipping threshold</strong> you type, in your
  store currency and converted for visitors who shop in another one. Nothing shows while the threshold is empty. The bar
  only displays progress: create the matching free shipping rate or discount in your admin and keep the two amounts the
  same. <strong>Measure progress on</strong> the subtotal before cart discounts, which is what Shopify's own free
  shipping rates use, or on the total after discounts.</li>
  <li><strong>Recommendations</strong>: Shopify's complementary products of the cart's lines first, then related ones,
  or a manual selection, never a product already in the cart, as a carousel or a list, with quick add.</li>
  <li><strong>Cart content</strong>: the order note, the discount code field (off by default; codes are checked by
  Shopify as soon as they are applied, then listed and removable), a You save line, the taxes and shipping note, a
  shipping notice and a promotion note on each line.</li>
  <li><strong>Checkout</strong>: the accelerated checkout buttons in the drawer and on the cart page, both on
  by default, and the payment icons of your store.</li>
  <li><strong>Empty cart</strong>: a message, a button to the collection you choose and an optional selection of
  products.</li>
</ul>
<p><a href="features.html#gift-wrapping">Gift wrapping</a> adds its checkbox to the drawer and the cart page from its own
group.</p>
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
<p><strong>Glass elements</strong> is a second, lighter recipe for the small pieces set to Glass inside the sections:
cards, FAQ questions, form fields, buttons and the round controls that sit over a picture (carousel arrows, Lookbook
hotspots, the media controls of the product gallery, the video controls of the Hero). <strong>Element fill
opacity</strong>, <strong>Element blur</strong> and <strong>Element border opacity</strong> set it; the tint is the one
above. These elements turn nearly solid for visitors who ask for less transparency. See
<a href="features.html#glass">Glass</a>.</p>
''',
    'Backgrounds': '''
<p>The section backgrounds set to <strong>Gradient (two colors)</strong> can take three styles, chosen in each
section with <strong>Gradient style</strong>: Linear, Radial glow (a halo of the lighter color, placed and sized by the
halo settings) or Aurora (soft fields of the two colors). <strong>Animate auroras slowly</strong>, off by default, sets
every Aurora of the store in a very slow movement. It stays still for visitors whose device asks for reduced motion.
See <a href="sections.html#section-background">Section background</a>.</p>
''',
    'Carousels': '''
<p>One look for the arrows and the dots of every carousel: the product gallery, Product recommendations,
Testimonials, Key ingredients and the other sliders of the theme.</p>
<ul>
  <li><strong>Arrow style</strong>: Solid, Outline, Glass (the <a href="#ts-glass-effect">Glass elements</a> recipe,
  with a halo that keeps the arrow readable over a light or a dark photo) or Icon only.</li>
  <li><strong>Arrow shape</strong> (Square, Rounded, Circle), <strong>Arrow size</strong> on desktop and on mobile, and
  <strong>Arrow icon</strong> (Arrow or Chevron).</li>
  <li><strong>Arrow colors</strong>: Auto takes the colors of the section around the carousel, readable on its real
  background; Custom uses <strong>Arrow background</strong> and <strong>Arrow icon color</strong>.</li>
  <li><strong>Dots style</strong>: Dots or Bars.</li>
</ul>
<p>Where the arrows sit (on the sides, on hover, below, with dots, or none) is set in each section. Carousels move
one card at a time, follow a mouse drag and the keyboard, and stay still for visitors who ask for reduced motion.</p>
''',
    'Loader': '''
<p>The <strong>Page loader</strong>: an optional loading screen shown while pages open, with your logo, a progress bar
or a spinner, and an exit animation. It is the theme's only loader, and it covers everything on the page, the header and the announcement bar included. See
<a href="features.html#page-loader">Page loader</a>.</p>
<p>The progress bar has three settings of its own, shown with the <strong>Logo and progress bar</strong> and
<strong>Progress bar only</strong> layouts: <strong>Bar ends</strong> (Square, or Rounded, the default, which rounds
the track and the fill), <strong>Bar thickness</strong> (1 to 6 px, 2 by default) and <strong>Bar animation</strong>
(None, Smooth by default, or Shimmer).</p>
<p>Preview versions of Balm Studio had a second loader here: a loading indicator drawn on the hero while its video loaded,
with seven settings (Style, Loader image, Animation, Size (desktop), Size (mobile), Color and Custom color). It has
been removed with those settings. The hero now shows its cover image while its video loads, sharp or blurred, as set by
<strong>While the video loads</strong> in the <a href="sections.html#s-hero">Hero</a> section.</p>
''',
    'Favicon': '''
<p>The small icon shown in browser tabs and bookmarks. Upload a square image of at least 32 by 32 pixels; a PNG with a
transparent background works best.</p>
''',
    'Social media': '''
<p>The addresses of your profiles, typed once: Facebook, Instagram, TikTok, X, YouTube, Pinterest, Snapchat, Threads,
Tumblr, Vimeo and LinkedIn. Enter the full URL of each profile, for example
<code>https://www.instagram.com/yourbrand</code>. Only the networks with a URL show, each with its icon, in the order of
this list. A link opens in a new tab and is named for screen readers after your store, such as <q>Balm on
Instagram</q>.</p>
<p>The icons appear in three places: the <strong>Social media links</strong> block of the footer, the
<a href="sections.html#s-socials">Social media links</a> section, and the header on desktop when <strong>Show social
media icons</strong> is checked in the Header section. See <a href="features.html#social-media">Social media</a>.</p>
''',
    'Social media sharing': '''
<p>Controls how your pages look when someone shares a link on social media or in a messaging app. Product, collection
and blog post pages use their own featured image. The <strong>Fallback share image</strong> covers every other page
(1200 x 630 pixels is the recommended size), and the <strong>X (Twitter) account</strong> is shown as the source of
shared cards. The links to your own profiles are in <a href="#ts-social-media">Social media</a>.</p>
''',
    'Filters': '''
<p><strong>Filter drawer style</strong> sets the look of the filter drawer: the panel opened by the Filter and sort
button on phones, and by the Filters button when the Collection or Search section uses the Drawer filter layout.
<strong>Solid</strong> uses the section's color scheme, <strong>Glass</strong> the
<a href="#ts-glass-effect">Glass effect</a>, like the cart drawer. The drawer opens over the announcement bar and the
header, full height, with the filters in accordions, Sort by on phones, and Clear all and Apply fixed at the bottom.
The filters themselves come from Shopify's Search &amp; Discovery app.</p>
''',
    'Breadcrumbs': '''
<p>A trail of links back to the home page, shown on product, collection and blog post pages. Position, separator and
alignment are set here for the whole store. The Product, Collection and Article sections each have a
<strong>Breadcrumbs on this page</strong> setting that shows or hides the trail on that page type only.</p>
<p><strong>Show the collection</strong>, on by default, adds a collection to the trail of a product page, and to the
breadcrumb data search engines read: the collection the visitor came through, otherwise the collection set in the
product's <code>custom.primary_collection</code> metafield, otherwise its first collection. See
<a href="metafields.html#primary-collection">Metafields, Primary collection</a>.</p>
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
