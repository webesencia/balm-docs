SUPPORT_FORM = 'https://form.jotform.com/262695466571066'

# ------------------------------------------------------------------ Getting started
GS_LEAD = ('Balm Studio is an Online Store 2.0 theme for Shopify: every page is built from sections and blocks that you add, '
           'remove and reorder in the theme editor, without code. This guide takes you from installation to a store '
           'ready to publish.')

GETTING_STARTED = '''
<ul class="cards">
  <li><a href="theme-settings.html"><strong>Theme settings</strong><span>Colors, fonts, corners and storewide features.</span></a></li>
  <li><a href="sections.html"><strong>Sections</strong><span>Every section, its settings and a typical use.</span></a></li>
  <li><a href="product-page.html"><strong>Product page blocks</strong><span>Build the product page, block by block.</span></a></li>
  <li><a href="features.html"><strong>Features</strong><span>Quick view, badges, age verifier, gift wrapping and more.</span></a></li>
  <li><a href="metafields.html"><strong>Metafields</strong><span>Per product colors, texts and images.</span></a></li>
  <li><a href="faq.html"><strong>FAQ</strong><span>Answers to the questions merchants ask most.</span></a></li>
</ul>

<h2 id="install">Install Balm Studio from the Theme Store</h2>
<ol class="steps">
  <li>Open the Balm Studio page on the <a href="https://themes.shopify.com/">Shopify Theme Store</a> while logged in to your store.</li>
  <li>Select <strong>View demo store</strong> to browse Balm Studio with its content before you install it.</li>
  <li>Select <strong>Try theme</strong> to add a trial copy to your theme library, or buy the theme straight away. A trial lets you customize everything; you pay when you publish.</li>
  <li>In your admin, go to <strong>Online Store, Themes</strong>. Balm Studio is in your theme library. Select <strong>Customize</strong> to open the theme editor.</li>
  <li>When the store is ready, open the theme's <strong>...</strong> menu in the theme library and choose <strong>Publish</strong>.</li>
</ol>
<p>Balm Studio needs no app to work. Apps that offer app blocks, such as reviews, subscriptions or bundles, plug into the
product page and into most sections.</p>

<h3 id="updates">Updating Balm Studio</h3>
<p>When a new version is released, your theme library shows an update notice. Shopify adds the new version to your
library as a separate copy that keeps your theme editor settings and content, so you can review it before publishing.
Changes made directly in the theme code are not carried over: see <a href="custom-code.html">Custom code</a>. What changed
in each version is listed in the <a href="changelog.html">Changelog</a>.</p>

<h2 id="preset">The Balm Studio preset</h2>
<p>A preset is a starting style: color schemes, font pairing, corner radii, glass recipe and typography recipes. Balm Studio
comes with one preset, also named Balm Studio, and your store starts from it.</p>
<ul>
  <li><strong>Look.</strong> Clean and neutral: a white scheme, a near black scheme and two violet schemes (a pale lavender and a deep violet), sentence case headings and buttons, a white frosted glass. A calm base that lets product photography lead.</li>
  <li><strong>Fonts.</strong> Outfit 400 for headings, Inter for body text, on one fluid type scale.</li>
  <li><strong>Layout.</strong> Pages and sections in Full width with margins (side margins of 60 px on desktop and 20 px on mobile), and small buttons.</li>
  <li><strong>Corners.</strong> Softly rounded: buttons 12 px, cards 20 px.</li>
</ul>
<p>Every value of the preset is a starting point. Change the colors, fonts, corners, glass and typography in
<a href="theme-settings.html">Theme settings</a>; your sections, blocks and content stay as they are.</p>

<h2 id="editor">How the theme editor is organized</h2>
<ul>
  <li><strong>Header group</strong>: the Announcement bar and the Header, shared by every page.</li>
  <li><strong>Template</strong>: the sections of the page you are editing. Switch page type with the menu at the top of the editor (Home page, Products, Collections and so on).</li>
  <li><strong>Footer group</strong>: the Footer, shared by every page.</li>
  <li><strong>Theme settings</strong> (the gear icon): colors, fonts and storewide features. See <a href="theme-settings.html">Theme settings</a>.</li>
</ul>
<p>Most sizes and spacings have two settings, one ending in <strong>(desktop)</strong> and one ending in
<strong>(mobile)</strong>, so you can tune phones without touching large screens. Spacings switch from one value to the
other at 768 px wide. Text sizes are fluid: the mobile value applies on a phone 390 px wide, the desktop value from
1440 px, and the size moves smoothly in between (see <a href="theme-settings.html#ts-typography">Typography</a>). Use
the device switch at the top of the editor to preview both.</p>

<h2 id="first-setup">First setup, step by step</h2>
<ol class="steps">
  <li><strong>Logo and menu.</strong> Open the <a href="sections.html#s-header">Header</a> section. Set <strong>Logo type</strong> and upload your <strong>Logo image</strong>, then pick your main menu under <strong>Menu</strong>. Menus themselves are edited in your admin, under Content, Menus (Online Store, Navigation on older admins). The header is transparent over the first section by default and picks its colors from what lies under it: upload a white logo in <strong>Logo for dark backgrounds</strong> so it reads over dark images (see <a href="sections.html#s-header-tone">Automatic header colors</a>).</li>
  <li><strong>Countries and languages.</strong> The header shows a globe with the country and language selectors as soon as there is a choice to make: two countries or regions in <strong>Settings, Markets</strong>, or two published languages in <strong>Settings, Languages</strong>. Until then it shows nothing. <strong>Country and language selectors</strong> in the Header picks which ones appear (Both by default). See <a href="sections.html#s-header-localization">Country and language selectors</a>.</li>
  <li><strong>Colors.</strong> In <a href="theme-settings.html#ts-colors">Theme settings, Colors</a>, adjust the four color schemes of the Balm Studio preset to your brand. Every section picks one of them.</li>
  <li><strong>Fonts, sizes and corners.</strong> Set the <strong>Heading font</strong> and <strong>Body font</strong> in <a href="theme-settings.html#ts-typography">Typography</a>. To make every heading or every text of the store larger or smaller at once, move <strong>Heading scale</strong> or <strong>Body scale</strong> there rather than each section's sizes. Set the corner radii in <a href="theme-settings.html">Corner style</a>, and the title and price sizes of the product cards in <a href="theme-settings.html#ts-tiles">Product cards</a>.</li>
  <li><strong>Page width and section width.</strong> In <a href="theme-settings.html#ts-layout">Theme settings, Layout</a>, the Balm Studio preset sets <strong>Page width</strong> to Full width with margins, in line with the header; choose Standard (1400 px) or Wide (1600 px) for a narrower product, collection and search page. <strong>Default section width</strong> (Full width with margins) and <strong>Section side margins</strong> (60 px on desktop, 20 px on mobile) set every section left on Theme default.</li>
  <li><strong>Home page.</strong> The home page starts with a Hero, a Marquee, a Products showcase, a Bento, Rich text, Image with text, a Featured collection, a Lookbook, Social media links and the Newsletter popup, as on the demo store. Replace their images and texts, remove what you do not need, and add sections with <strong>Add section</strong>. In the Products showcase, pick one product per <strong>Spotlight</strong>: its name, link, image, tagline and colors follow on their own (see <a href="metafields.html#product-color">Metafields</a>).</li>
  <li><strong>Product page.</strong> Open a product in the editor and review the block stack. See <a href="product-page.html">Product page blocks</a>, and <a href="metafields.html">Metafields</a> if each product should carry its own color or texts. For a background in each product's own colors, set <strong>Background mode</strong> of the Product section to <a href="product-page.html#bg-product-gradient">Product gradient (metafields)</a>; with cutout packshots (PNG or WebP), try the <a href="product-page.html#text-behind-cutouts">text behind cutouts</a>.</li>
  <li><strong>Badges.</strong> Sale and Sold out show on their own, from the prices and the stock. In <a href="theme-settings.html#ts-product-badges">Theme settings, Product badges</a>, turn on New if you want it and set the badge colors. For a badge of your own words, such as <q>Limited edition</q>, fill the <code>custom.badge_label</code> metafield: see <a href="features.html#product-badges">Product badges</a>.</li>
  <li><strong>Collections and search.</strong> Install Shopify's free Search &amp; Discovery app to choose the filters shown on collection and search pages, then set their layout in the <a href="sections.html#s-main-collection">Collection</a> section.</li>
  <li><strong>Cart.</strong> In <a href="theme-settings.html#ts-cart">Theme settings, Cart</a>, choose a drawer, the cart page or a notification, then set the free shipping bar, the recommendations, the order note and the discount code field. Turn on <a href="features.html#gift-wrapping">gift wrapping</a> if you offer it.</li>
  <li><strong>Social media.</strong> Type the address of each of your profiles in <a href="theme-settings.html#ts-social-media">Theme settings, Social media</a>. The icons then show in the footer, in the Social media links section and, if you want, in the header (see <a href="features.html#social-media">Social media</a>).</li>
  <li><strong>Footer.</strong> Add your menus, newsletter and social media links. The footer opens with a <a href="sections.html#s-footer-large-logo">Large logo</a>, your store name set across the whole width: keep it, switch it to your own SVG, or remove it. The Localization block repeats the country and language selectors in the footer, with the same choices as the header.</li>
  <li><strong>Favicon and sharing.</strong> Upload a favicon and a fallback share image in Theme settings.</li>
  <li><strong>Pages.</strong> Create your About, Contact, FAQ and Where to buy pages in Online Store, Pages, and assign them the matching template under <strong>Theme template</strong>: <code>page.about</code>, <code>page.contact</code>, <code>page.faq</code>, <code>page.find-us</code>. The <code>page.products</code> template presents your range with a Featured set and a Products showcase.</li>
  <li><strong>Check and publish.</strong> Preview every page type on desktop and on a phone, place a test order, then publish.</li>
</ol>

<h2 id="templates">Templates included</h2>
<p>Home page, product, collection, list of collections, search, cart, blog, blog post, page, 404, password and gift card,
a second product template, <code>product.immersive</code> (each product's own gradient under the header, see
<a href="product-page.html#bg-under-header">Extend the gradient under the header</a>), a second collection template,
<code>collection.colorful</code> (an Aurora gradient that runs under the header, with the column selector on), plus
five page templates: <code>page.about</code> (About), <code>page.contact</code> (Contact), <code>page.faq</code> (FAQ),
<code>page.find-us</code> (Store locator) and <code>page.products</code> (Products). All of them are built from sections,
so you can reshape any of them in the editor.</p>

<h2 id="help">Need help?</h2>
<p>Search this documentation with the box at the top of the page, read the <a href="faq.html">FAQ</a>, or contact
<a href="support.html">Balm Studio support</a>.</p>
'''

# ------------------------------------------------------------------ Features
FEATURES_LEAD = ('The features that span several sections or the whole store: what they do, where to turn them on '
                 'and what to know before you rely on them.')

FEATURES = '''
<nav class="contents" aria-label="Features"><ol class="contents__list contents__list--cols">
<li><a href="#quick-view">Quick view</a></li><li><a href="#product-badges">Product badges</a></li>
<li><a href="#age-verifier">Age verifier</a></li>
<li><a href="#gift-wrapping">Gift wrapping</a></li><li><a href="#lookbook">Lookbook</a></li>
<li><a href="#compare-products">Compare products</a></li><li><a href="#recently-viewed">Recently viewed</a></li>
<li><a href="#pagination">Pagination</a></li><li><a href="#translations">Translations</a></li>
<li><a href="#combined-listings">Combined listings</a></li><li><a href="#pre-order">Pre-order</a></li>
<li><a href="#type-sizes">Type sizes</a></li><li><a href="#page-width">Page width</a></li>
<li><a href="#header-colors">Automatic header colors</a></li><li><a href="#section-width">Section width</a></li>
<li><a href="#social-media">Social media</a></li>
<li><a href="#sticky-add-to-cart">Sticky add to cart</a></li>
<li><a href="#collection-columns">Column selector</a></li>
</ol></nav>

<section class="entry" id="quick-view-entry">
<h2 id="quick-view">Quick view</h2>
<p>Quick view opens a product in a modal from its card, so shoppers choose a variant and add to cart without leaving
the page. The modal shows the gallery with thumbnails, the price with its badges and unit price, the rating, the same
variant picker as the product page (swatches included), quantity rules, purchase options, the add to cart button, pickup
availability, a short description and a link to the full product page. Adding to cart opens the cart drawer.</p>
<h3 id="quick-view-on">Turn it on</h3>
<ol class="steps">
  <li>Open a section that shows product cards: Collection, Featured collection, Search, Recently viewed or Lookbook.</li>
  <li>Set <strong>Quick view</strong> to <strong>Show on hover</strong> or <strong>Always show</strong>. On touch screens the button is always visible.</li>
  <li>In <a href="theme-settings.html#ts-quick-view">Theme settings, Quick view</a>, choose what the modal shows and its card style: Solid, Tinted glass or Glass.</li>
</ol>
<p><strong>Short description metafield</strong> takes the namespace and key of a product metafield, for example
<code>custom.short_description</code>; products without it show the first paragraph of their description, cut to
<strong>Description length</strong>. <strong>Preload on hover</strong> loads the product when the pointer rests on its
card so the modal opens at once, at the cost of more data. Without JavaScript the button simply opens the product page.</p>
<p>Quick view is separate from <strong>Quick add</strong>, the setting that puts an add to cart button on the card
itself: Off, Single-variant products, or All products (which opens an option picker for products with variants).</p>
</section>

<section class="entry" id="product-badges-entry">
<h2 id="product-badges">Product badges</h2>
<p>Four badges can appear on product cards, in quick view, in Compare products and on the product page. Every one of
them states a fact of the product: nothing shows a text typed once for all products. Their position, shape and colors
are set once in <a href="theme-settings.html#ts-product-badges">Theme settings, Product badges</a>.</p>
<div class="table-wrap"><table class="plain">
<thead><tr><th scope="col">Badge</th><th scope="col">Shown when</th><th scope="col">Options</th></tr></thead>
<tbody>
<tr><th scope="row">Sale</th><td>Automatically, when the variant shown has a compare-at price above its price. Never on a price without a compare-at price.</td><td><strong>Sale badge text</strong>: Sale, Percentage off or Amount saved.</td></tr>
<tr><th scope="row">Sold out</th><td>Automatically, when the product can no longer be bought. It then replaces Sale and New.</td><td>Colors.</td></tr>
<tr><th scope="row">New</th><td>Off by default. With <strong>New badge</strong> set to <strong>Product tag</strong>: the product carries the tag you name in <strong>Tag</strong> (<code>new</code> by default, upper and lower case ignored). Set to <strong>Created in the last X days</strong>: the product was created fewer days ago than <strong>Number of days (X)</strong>.</td><td>Colors. A tag is the safer choice: a store whose products were all imported recently would otherwise show New everywhere.</td></tr>
<tr><th scope="row">Custom</th><td>The product has a value in its <code>custom.badge_label</code> metafield.</td><td>The text is the metafield value. Colors from Theme settings, or the product's own through the <code>custom.badge_color</code> and <code>custom.badge_text_color</code> metafields.</td></tr>
</tbody></table></div>
<h3 id="custom-badge">Set up the Custom badge</h3>
<ol class="steps">
  <li>Create the <code>custom.badge_label</code> definition once, as described in <a href="metafields.html#badge-label">Metafields, Badge label</a>.</li>
  <li>Fill it on the products that need a badge, for example <q>Limited edition</q> or <q>Vegan</q>. Leave it empty on the others.</li>
  <li>That is all: the cards, quick view, Compare products and the product page read the metafield directly. There is no key to type and nothing to connect in the theme editor.</li>
</ol>
<h3 id="custom-badge-colors">Give one product its own badge colors</h3>
<p>The Custom badge wears the <strong>Custom background</strong> and <strong>Custom text</strong> colors of Theme
settings. To color it differently on one product, for example green on a vegan product, create two optional product
metafields of type <strong>Color</strong>: <code>custom.badge_color</code> for the background and
<code>custom.badge_text_color</code> for the text (see <a href="metafields.html#badge-colors">Metafields, Badge
colors</a>). They change the Custom badge of that product only, everywhere it shows. Sale, Sold out and New keep the
colors of Theme settings.</p>
<ul>
  <li><strong>Both filled</strong>: the badge takes both colors as they are.</li>
  <li><strong>Background only</strong>: the text is picked for you. It takes the text color or the background color of Scheme 1, your main color scheme, whichever contrasts more with the badge. If even that one stays below a contrast of 4.5:1, which happens on mid tones, the text turns pure black or pure white, one of which always reaches it.</li>
  <li><strong>Text only</strong>: the text color sits on the Custom background of Theme settings. Check that the two contrast enough.</li>
  <li><strong>Neither</strong>: the colors of Theme settings, as on every other product.</li>
</ul>
<h3 id="badges-product-page">Badges on the product page</h3>
<ul>
  <li><strong>Badges on media</strong>, in the Product section settings, shows the badges in the corner of the gallery: <strong>Off</strong> (the default) or <strong>Automatic</strong>, the same Sale, Sold out, New and Custom badges as the cards.</li>
  <li>The <strong>Badge</strong> block, in the information column, draws the same badges in a row when its <strong>Badge type</strong> is <strong>Automatic (Sale, Sold out, New, Custom)</strong>, the default. Its other type, <strong>Image</strong>, places your own artwork in a corner of the product area.</li>
  <li>The <strong>Spinning badge</strong> block turns the <code>custom.badge_label</code> text around a ring, on a corner of the gallery or next to the title, with its own position and size on desktop and on mobile. It has no text field of its own: a product without the metafield shows no ring. See <a href="product-page.html#pb-product-badge">Spinning badge</a>.</li>
</ul>
<p>On the product page, Sale and Sold out follow the selected variant: choosing a variant without a compare-at price
removes Sale, choosing a sold out one shows Sold out. When no badge applies, nothing is drawn and no space is left.</p>
<h3 id="badges-per-section">Choose the badges of each section</h3>
<p>Every section that shows product cards has its own <strong>Badges</strong> setting: Collection, Search, Featured
collection, Product recommendations, Recently viewed, Lookbook, the 404 page, Compare products, the Product tile of
Bento and the Complementary products block of the product page.</p>
<ul>
  <li><strong>All</strong>, the default: every badge that applies.</li>
  <li><strong>Automatic only</strong>: Sale, Sold out and New, as set in Theme settings, Product badges.</li>
  <li><strong>Custom only</strong>: only the product's <code>custom.badge_label</code> metafield.</li>
  <li><strong>None</strong>: no badge in that section.</li>
</ul>
<p>For example, keep All on the collection pages and choose Custom only in Featured collection on the home page, so it
shows your Limited edition badges without the Sale ones.</p>
</section>

<section class="entry" id="page-loader-entry">
<h2 id="age-verifier">Age verifier</h2>
<p>A modal that asks visitors to confirm their age before they browse the store. It shows on every page of the online
store, never at checkout, and waits for the page loader to leave first.</p>
<ol class="steps">
  <li>In <a href="theme-settings.html#ts-age-verifier">Theme settings, Age verifier</a>, check <strong>Enable the age verifier</strong>.</li>
  <li>Set the <strong>Minimum age</strong>. Write <code>[age]</code> in the texts to print it. Fields left empty use the translated storefront text.</li>
  <li>Choose what happens when the visitor declines: <strong>Show a message</strong> or <strong>Redirect to a link</strong>.</li>
  <li>Set <strong>Remember the answer for</strong>: the number of days before the same browser is asked again. 0 asks on every visit.</li>
  <li>Style it with a background image, a color scheme and a card style. Check <strong>Preview in the theme editor</strong> to see it while you edit; answers are not remembered while previewing.</li>
</ol>
<p>Raising the minimum age asks every visitor again. A decline is never remembered. The age verifier is a
self-declaration, not an identity check: make sure it meets the rules that apply to your products in the countries you
sell to.</p>
</section>

<section class="entry" id="gift-wrapping-entry">
<h2 id="gift-wrapping">Gift wrapping</h2>
<p>Adds a gift wrapping checkbox, and an optional gift message, to the cart drawer and the cart page. Checking the box
adds your wrapping product to the cart in quantity 1 and records the cart attribute <strong>Gift wrapping: Yes</strong>.
The message is saved as the cart attribute <strong>Gift message</strong>. Both appear on the order in your admin.</p>
<ol class="steps">
  <li>Create a product for the wrapping, for example <q>Gift wrapping</q>, with the price the buyer pays and an image. Make it available on the Online Store sales channel, and keep it out of your collections.</li>
  <li>In <a href="theme-settings.html#ts-gift-wrapping">Theme settings, Gift wrapping</a>, check <strong>Offer gift wrapping</strong> and pick it as the <strong>Wrapping product</strong>. The option only shows once an available product is chosen.</li>
  <li>Adjust the <strong>Checkbox label</strong>, the help text, the gift message and its maximum length, and where it shows: cart drawer, cart page or both.</li>
</ol>
<p>The wrapping line stays at quantity 1, and a cart that holds only the wrapping is emptied, so nobody checks out with
the wrapping alone.</p>
</section>

<section class="entry" id="lookbook-entry">
<h2 id="lookbook">Lookbook</h2>
<p>The <a href="sections.html#s-lookbook">Lookbook</a> section turns a photo into a shop: each point on the image opens
the product card, with its quick add. On a phone a tap opens the same content as a sheet from the bottom of the screen.</p>
<ol class="steps">
  <li>Add a <strong>Lookbook</strong> section and choose an image, plus an optional mobile image.</li>
  <li>Add one <strong>Hotspot</strong> block per product and pick the product. A hotspot can carry a text and a link instead.</li>
  <li>Place each hotspot with <strong>Horizontal position</strong> and <strong>Vertical position</strong>, in percent of the image: 0% is the left or top edge, 100% the right or bottom edge. Desktop and mobile positions are separate.</li>
  <li>For a shoppable list, set <strong>Layout</strong> to <strong>Image with product list</strong>: the products line up beside the image, and hovering a card lights its hotspot.</li>
</ol>
</section>

<section class="entry" id="compare-products-entry">
<h2 id="compare-products">Compare products</h2>
<p>The <a href="sections.html#s-compare-products">Compare products</a> section sets up to five products side by side.
Built in rows show the image, the badges, the price, the availability, the vendor and the rating. Each row you add
reads one fact on every compared product: a metafield of your choice, or the vendor, product type, tags, SKU, barcode,
weight or unit price.</p>
<ol class="steps">
  <li>Create one product metafield definition per fact you want to compare, in Settings, Custom data, Products. For example <q>Texture</q> and <q>Skin type</q> (Single line text), <q>Fragrance free</q> (True or false).</li>
  <li>Fill the values on each product.</li>
  <li>Add the section, pick the products, then add one <strong>Row</strong> block per fact. Keep <strong>Source</strong> on Metafield and type the metafield's name in <strong>Metafield</strong>, for example <q>Skin type</q>, or its key, <code>custom.skin_type</code>. Type a <strong>Label</strong> for the left column, or leave it empty to use the name of the source.</li>
</ol>
<p>Each value is drawn by its type: a check mark or a cross for true or false, a number followed by the row's
<strong>Unit</strong>, a list as a sentence, a color with its swatch. A product without a value shows a hyphen.
<strong>Highlight differences</strong> marks the rows where products differ. <strong>Mobile layout</strong> shows one
card per product on a phone, or the table with the labels in place while the products scroll. The full example is in
<a href="metafields.html#compare">Metafields, Compare products rows</a>.</p>
</section>

<section class="entry" id="recently-viewed-entry">
<h2 id="recently-viewed">Recently viewed</h2>
<p>The product page records each product a visitor opens, in that visitor's own browser. The
<a href="sections.html#s-recently-viewed">Recently viewed</a> section reads that list and shows the products, newest
first. Nothing is sent to a server and no app or account is needed. The section takes no space until the visitor has a
history; in the theme editor it shows example cards instead.</p>
<p>Add it to the product template, below Product recommendations, with <strong>Exclude the current product</strong> on,
or to the cart, collection or home page. <strong>Maximum products</strong> caps the list.</p>
</section>

<section class="entry" id="pagination-entry">
<h2 id="pagination">Pagination</h2>
<p>The Collection and Search sections have a <strong>Pagination</strong> setting with three modes:</p>
<ul>
  <li><strong>Page numbers</strong>: classic numbered pages.</li>
  <li><strong>Load more button</strong>: the next page is added under the grid when the shopper asks for it.</li>
  <li><strong>Infinite scroll</strong>: the next page is added as the shopper reaches the end of the grid. After three pages a Load more button takes over, so the footer stays reachable.</li>
</ul>
<p>Load more and infinite scroll show a Showing X of Y counter. The number of products per page is set with
<strong>Products per page</strong> on collections and <strong>Results per page</strong> on search. The blog, the list of
collections and blog post comments use page numbers, with their own per page setting. Promo tiles appear on the first
page only.</p>
</section>

<section class="entry" id="translations-entry">
<h2 id="translations">Translations</h2>
<p>Balm Studio ships in five languages: English, French, German, Italian and Spanish. That covers every storefront text of the
theme (buttons, cart, forms, filters, accessibility labels) and the theme editor itself, which follows the language of
your admin.</p>
<ol class="steps">
  <li>Add and publish your languages in <strong>Settings, Languages</strong>. The theme's own texts switch automatically.</li>
  <li>Translate the content you typed in the editor (headings, paragraphs, button labels) with Shopify's free Translate &amp; Adapt app.</li>
  <li>Leave the text settings marked <em>Leave empty to use the translated default</em> empty on a multilingual store: they then show the built in text in each language.</li>
</ol>
<p>To change the wording of a theme text, use <strong>Edit default theme content</strong> in the theme's <strong>...</strong>
menu in your theme library. For a language Balm Studio does not ship, Translate &amp; Adapt can translate the theme texts too.</p>
</section>

<section class="entry" id="combined-listings-entry">
<h2 id="combined-listings">Combined listings</h2>
<p>Combined listings group separate products into one listing, for example one product per color, and are available to
Shopify Plus stores through Shopify's Combined Listings app. Balm Studio supports them with nothing to configure:</p>
<ul>
  <li>On the product page, picking a value that belongs to another product of the listing switches the page to that product without a reload, keeping the values already chosen and updating the address.</li>
  <li>Swatches on product cards link to the matching product.</li>
  <li>In quick view, a value from another product loads that product into the modal.</li>
  <li>In the quick add option picker, such a value opens that product's page, where the full picker takes over.</li>
</ul>
</section>

<section class="entry" id="pre-order-entry">
<h2 id="pre-order">Pre-order</h2>
<p>Pre-order turns itself on: there is nothing to enable. A variant becomes a pre-order when its quantity is tracked,
its stock is at 0 and <strong>Continue selling when out of stock</strong> is checked in the product admin. The add to
cart button, the sticky add to cart bar and the quick add button then read <strong>Pre-order</strong>, or the
<strong>Button label</strong> you set in <a href="theme-settings.html#ts-pre-order">Theme settings, Pre-order</a>. The
variant can still be bought, so the accelerated checkout buttons (Buy it now) stay visible, unlike on a sold out variant.
The Stock status block keeps its own text.</p>
<p>The label does not change how checkout works: the order is paid at checkout like any other. To take a deposit or
charge later, use a pre-order app that creates selling plans; its options then show in the Purchase options block.
Tell buyers when the product will ship, for example in a Text block or a Collapsible row.</p>
</section>

<section class="entry" id="type-sizes-entry">
<h2 id="type-sizes">Type sizes</h2>
<p>Every text of Balm Studio sits on one fluid type scale, from phones to large screens. A size is reached at 390 px wide for
its mobile value and at 1440 px for its desktop value, and grows in a straight line in between, so a heading never jumps
from one size to another as the window widens. The text size settings of the sections and blocks follow the same rule,
and their defaults sit on the scale: a section you add matches its neighbors without any tuning.</p>
<ul>
  <li>To make the whole store read larger or smaller, move <strong>Heading scale</strong> or <strong>Body scale</strong> in <a href="theme-settings.html#ts-typography">Theme settings, Typography</a> (80 to 130%). They multiply every size, those set in sections included, so the proportions between levels stay.</li>
  <li>To change one element, use its own size settings: they stay on the fluid rule and the scales still apply to them.</li>
  <li>Product card titles and prices are set once for all the grids in <a href="theme-settings.html#ts-tiles">Theme settings, Product cards</a>.</li>
</ul>
<p>The announcement bar and the mega menu switch their sizes at 1200 px, the menu breakpoint. Logos and decorative
texts are sized on their own, off the scale: the Large logo of the footer fills its width, and the text behind cutouts
of the product page or the two words across the Gallery banner keep a desktop and a mobile size.</p>
</section>

<section class="entry" id="page-width-entry">
<h2 id="page-width">Page width</h2>
<p>One setting, <strong>Page width</strong> in <a href="theme-settings.html#ts-layout">Theme settings, Layout</a>, sets
how wide the shopping pages grow: the product page, the collection and search pages, and the Featured collection,
Product recommendations and Recently viewed sections. <strong>Standard</strong> keeps them to 1400 px,
<strong>Wide</strong> to 1600 px, and <strong>Full width with margins</strong> fills the screen less the side
margins of the header, so the page, the breadcrumbs and the footer line up with the header's logo and icons. On a large
screen, Wide shows bigger product cards and a bigger gallery; the card images are served at the new size, so they stay
sharp. The other sections set their width with <a href="#section-width">Section width</a>, whose default, Theme
default, follows <strong>Default section width</strong> in the same Layout group.</p>
</section>

<section class="entry" id="header-colors-entry">
<h2 id="header-colors">Automatic header colors</h2>
<p>The header can lie over the top of the page, transparent, and wear the colors that read on what is under it, with
nothing to set in each section. It does so with <strong>Header behavior</strong> on <strong>Transparent at top</strong>
(the default: over the first section, then the card on scroll) or <strong>Adaptive</strong> (at every scroll position,
on every page).</p>
<ol class="steps">
  <li>In the <a href="sections.html#s-header">Header</a> section, set <strong>Colors over dark backgrounds</strong> to a color scheme with light text. Scheme 2 of the Balm Studio preset, white on near black, is the default.</li>
  <li>Upload a light version of your logo in <strong>Logo for dark backgrounds</strong>. It shares the size and the place of the main logo, so nothing moves when they swap.</li>
  <li>Let the first section of the page reach under the header: <strong>Allow transparent header</strong> on a Hero, Slideshow, Video, Products showcase or Brand story hero, or <strong>Header over this section</strong> on the other sections that offer it (see <a href="sections.html#transparent-header">The header over a section</a>).</li>
</ol>
<p>The header then reads the backgrounds painted under its middle line: colors, gradients, each product's gradient,
and, over a picture or a video, a small thumbnail of the part it covers, overlay included. Over a dark background it
takes the colors over dark backgrounds and the logo for dark backgrounds; over a light one, its own color scheme and
main logo. It reads again as the page scrolls, as a slideshow changes slide and as a Products showcase moves to the next
spotlight. An open menu, search panel or mobile menu always keeps the standard colors. A floating announcement bar can
follow it with <strong>Use the header's colors over dark backgrounds</strong>.</p>
<p>Preview versions of Balm Studio asked for the tone in some sections (<strong>Tone under the header</strong>, <strong>Header
colors at rest</strong>) and offered <strong>Transparent header over the first section</strong>; these settings have
been removed. A store that used the transparent header keeps it, Transparent at top being the default.</p>
</section>

<section class="entry" id="section-width-entry">
<h2 id="section-width">Section width</h2>
<p>Almost every section has a <strong>Section width</strong> setting, right after its color scheme, with four options:</p>
<ul>
  <li><strong>Theme default</strong>, the default: the <strong>Default section width</strong> of <a href="theme-settings.html#ts-layout">Theme settings, Layout</a> (Full width with margins unless you change it), so every section left on it changes width at once.</li>
  <li><strong>Full width</strong>: the background, the picture or the video runs from one edge of the screen to the other, with square corners. Text keeps a readable width inside.</li>
  <li><strong>Full width with margins</strong>: the section stops at the <strong>Section side margins</strong> of Theme settings, Layout, one value on desktop and one on mobile.</li>
  <li><strong>Page width</strong>: the section stops at the <a href="#page-width">Page width</a> of Theme settings, Layout, with its side margin, in line with the product, collection and search pages.</li>
</ul>
<p>Mixing the options on one page builds a rhythm: a Full width hero, products and texts at Page width, then a picture
in Full width with margins with rounded corners. Inset, Before and after and the Slideshow take a <strong>Corner
radius</strong> of their own, the media radius of the theme by default. Product, Contact and Collection keep their
background edge to edge in every width, for a transparent header, and move only their content. See
<a href="sections.html#section-width">Sections, Section width</a>.</p>
</section>

<section class="entry" id="glass-entry">
<h2 id="social-media">Social media</h2>
<p>Your social media profiles are typed once, in <a href="theme-settings.html#ts-social-media">Theme settings, Social
media</a>, and every icon of the store reads them.</p>
<ol class="steps">
  <li>In Theme settings, Social media, paste the full address of each profile you have, for example <code>https://www.tiktok.com/@yourbrand</code>. Facebook, Instagram, TikTok, X, YouTube, Pinterest, Snapchat, Threads, Tumblr, Vimeo and LinkedIn are offered.</li>
  <li>Choose where the icons appear: the <strong>Social media links</strong> block of the footer, the <a href="sections.html#s-socials">Social media links</a> section, and the header on desktop with <strong>Show social media icons</strong> in the Header section.</li>
</ol>
<p>Only the networks with an address show, each with its icon, in a new tab. Screen readers name each link after your
store, such as <q>Balm on Instagram</q>. The footer block can also show Shopify's Follow on Shop button. How your pages
look when someone shares them is set separately, in <a href="theme-settings.html#ts-social-media-sharing">Social media
sharing</a>.</p>
</section>

<section class="entry" id="sticky-add-to-cart-entry">
<h2 id="sticky-add-to-cart">Sticky add to cart</h2>
<p>A bar that keeps the product and its add to cart button within reach while the shopper scrolls a long product page.
It is the <a href="sections.html#s-sticky-atc">Sticky add to cart</a> section, which the product template places below
the Product section.</p>
<ul>
  <li><strong>Enable the bar</strong> turns it on. <strong>Position (desktop)</strong> and <strong>Position (mobile)</strong> put it at the top or at the bottom of the screen; the bottom suits phones, where the main button quickly scrolls away.</li>
  <li>It shows the <strong>Product thumbnail</strong> (desktop and mobile apart), the <strong>Product title</strong>, the <strong>Selected variant</strong> (left out on a product without variants) and the <strong>Price</strong>, each one optional.</li>
  <li>By default it appears once the main buy button scrolls out of view; <strong>Always visible</strong> keeps it on screen.</li>
  <li>The button follows the variant chosen on the page and says Pre-order on a pre-order variant. Its colors are <strong>Button background</strong> and <strong>Button text</strong>; with the Product gradient background, the product's end color becomes its accent when it stays readable.</li>
</ul>
<p>The back to top button lifts above the bar. In the theme editor, the bar steps aside while another section is
selected.</p>
</section>

<section class="entry" id="spotlight-spinning-badge-entry">
<h2 id="collection-columns">Column selector</h2>
<p>The <a href="sections.html#s-main-collection">Collection</a> section can let shoppers choose how many products they
see per row. <strong>Columns (desktop)</strong> and <strong>Columns (mobile)</strong> set the starting layout; then:</p>
<ul>
  <li><strong>Let visitors change the column count (desktop)</strong> adds 2, 3 and 4 buttons beside the sort.</li>
  <li><strong>Let visitors change the column count (mobile)</strong> adds 1 and 2 buttons beside the filters on phones.</li>
</ul>
<p>On desktop the buttons sit on one row with the filters, the product count and the sort; on a phone, on one row with
the Filter and sort button and the count. Each device keeps its own choice for the rest of the visit, after a filter or
a page reload too. Both are off by default.</p>
</section>
'''

# ------------------------------------------------------------------ Metafields
META_LEAD = ('Metafields give every product its own color, cutout, texts and images. This page lists the '
             'metafields Balm Studio reads, with the exact name, key and type to create.')

META_ROWS_PRODUCT = [
    ('Background color', 'custom.background_color', 'Color', 'Product: Background color, Gradient start, Base color'),
    ('Background color end', 'custom.background_color_end', 'Color', 'Product: Gradient end'),
    ('Accent color', 'custom.accent_color', 'Color', 'Product: Halo color'),
    ('Overlay color', 'custom.overlay_color', 'Color', 'Product: Overlay color'),
    ('Curve color', 'custom.curve_color', 'Color', 'Product: Curve color'),
    ('Background image', 'custom.background_image', 'File', 'Product: Background image'),
    ('Background media', 'custom.background_media', 'File', 'Product: Vignette image'),
    ('Buy button label', 'custom.buy_button_label', 'Single line text', 'Buy buttons: Add to cart label'),
    ('Specs label', 'custom.specs_label', 'Single line text', 'Popup: Trigger label'),
    ('Specifications', 'custom.specifications', 'Rich text', 'Popup: Content'),
    ('Row heading', 'custom.row_heading', 'Single line text', 'Collapsible row: Heading'),
    ('Ingredients', 'custom.ingredients', 'Rich text', 'Collapsible row: Content'),
    ('Icon image 1', 'custom.icon_image_1', 'File', 'Icon item 1: Icon image (2 and 3 for the next items)'),
    ('Icon text 1', 'custom.icon_text_1', 'Single line or Multi-line text', 'Icon item 1: Heading or Text (2 and 3 for the next items), or Spotlight: Claim 1 text'),
    ('Product image', 'custom.product_image', 'File', 'Image block: Image'),
    ('Image caption', 'custom.image_caption', 'Single line text', 'Image block: Caption'),
    ('Spec label', 'custom.spec_label', 'Single line text', 'Specification: Label'),
    ('Net weight', 'custom.net_weight', 'Single line text', 'Specification: Value'),
]

META_ROWS_SHOP = [
    ('Background color', 'shop.background_color', 'Color', 'Background color, Gradient start, Base color'),
    ('Background color end', 'shop.background_color_end', 'Color', 'Gradient end'),
    ('Accent color', 'shop.accent_color', 'Color', 'Halo color'),
    ('Overlay color', 'shop.overlay_color', 'Color', 'Overlay color'),
    ('Background image', 'shop.background_image', 'File', 'Background image'),
]


def _rows(rows):
    out = []
    for name, key, ty, target in rows:
        out.append(f'<tr><td><q>{name}</q></td><td><code>{key}</code></td><td>{ty}</td><td>{target}</td></tr>')
    return ''.join(out)


METAFIELDS = '''
<h2 id="before-you-start">Before you start</h2>
<p><strong>The theme cannot create a metafield definition; only you can, in your admin.</strong> This is a platform rule:
a setting can only be connected to a definition that already exists, with the right type. So the definition always comes
first, the connection second, the values third.</p>
<ul>
  <li>Definitions are created in <strong>Settings, Custom data</strong>, under <strong>Products</strong>, <strong>Collections</strong>, <strong>Pages</strong> or <strong>Shop</strong>, depending on what carries the value.</li>
  <li>Type the <strong>Name</strong> exactly as listed below. The admin derives the key from the name, in lowercase with underscores, so the key matches on its own. If you rename a definition, check its key before saving: the connection works by key.</li>
  <li>Names are shown in quotation marks here and in the theme editor so you can see where they start and end. The quotation marks are not part of the name.</li>
  <li>The namespace and key are suggestions; the <strong>type</strong> is not. A setting refuses a definition of the wrong type.</li>
  <li>Every connectable setting repeats the definition it expects in its own help text in the editor.</li>
</ul>

<h2 id="product-color">Product color</h2>
<p>Balm Studio dresses every page in the color of the product it shows. Each product needs two colors, a dark one and
a light one; the theme works out the grounds and the texts of the page from them and checks their contrast. The theme
reads these keys directly: create the definitions once, then fill the values on each product. There is nothing to
connect in the theme editor.</p>
<div class="table-wrap"><table class="plain">
<thead><tr><th scope="col">Name</th><th scope="col">Namespace and key</th><th scope="col">Type</th><th scope="col">Where it shows</th><th scope="col">Without a value</th></tr></thead>
<tbody>
<tr><td><q>Background color</q></td><td><code>custom.background_color</code></td><td>Color</td><td>The dark color of the product: the Deep ground, the text on light grounds. Every page and section that shows the product.</td><td>Derived from the light color. Without either, the house pair of <a href="theme-settings.html#ts-tone">Theme settings, Tone</a>.</td></tr>
<tr><td><q>Background color end</q></td><td><code>custom.background_color_end</code></td><td>Color</td><td>The light color of the product: the Field ground of its page, tile, band and step.</td><td>Derived from the dark color.</td></tr>
<tr><td><q>Cutout</q></td><td><code>custom.cutout</code></td><td>File (image)</td><td>The product standing on its own: Hero sequence, tiles, collection index, Color library, Line-up, Hue finder, product stage, cart drawer, sticky bar. Use a PNG or WebP with a transparent background, cropped tight to the object.</td><td>The product's main image, contained in its box instead of standing.</td></tr>
<tr><td><q>Name lines</q></td><td><code>custom.name_lines</code></td><td>Single line text</td><td>The product name in layers, for example <q>Lavender|Night|Cream</q>: lines separated by a vertical bar. The first line is the watermark of the tile.</td><td>The title, cut into three lines at most between words.</td></tr>
<tr><td><q>Volume</q></td><td><code>custom.volume</code></td><td>Single line text</td><td>The format after the type, for example <q>Night cream, 50 ml</q>.</td><td>The value of the first option, else the type alone.</td></tr>
<tr><td><q>Next product</q></td><td><code>custom.next_product</code></td><td>Product (one value)</td><td><strong>Next formula</strong> on the product page.</td><td>The next product of the primary collection, else nothing.</td></tr>
</tbody></table></div>
<p>The same two colors can be set on a <strong>variant</strong> (<code>custom.background_color</code>,
<code>custom.background_color_end</code> and <code>custom.cutout</code>, under <strong>Settings, Custom data,
Variants</strong>): choosing that variant on the product page recolors the page. A variant without them uses the color
of its swatch, then the product's. On a <strong>collection</strong>, the same two color keys (under <strong>Settings,
Custom data, Collections</strong>) give the collection page its color; without them, the color of the first product.</p>
<ol class="steps">
  <li>In <strong>Settings, Custom data, Products</strong>, choose <strong>Add definition</strong>. Name <q>Background color</q>, namespace and key <code>custom.background_color</code>, type <strong>Color</strong>. Save.</li>
  <li>Repeat with <q>Background color end</q> (<code>custom.background_color_end</code>, <strong>Color</strong>), <q>Cutout</q> (<code>custom.cutout</code>, <strong>File</strong>, images only), <q>Name lines</q> (<code>custom.name_lines</code>, <strong>Single line text</strong>), <q>Volume</q> (<code>custom.volume</code>, <strong>Single line text</strong>) and <q>Next product</q> (<code>custom.next_product</code>, <strong>Product</strong>, one value).</li>
  <li>Open a product, scroll to its <strong>Metafields</strong> card and fill the values: a deep color and a light color of the same hue work best.</li>
  <li>Open the product on your store: the page, the header and the tile wear its color.</li>
</ol>

<h2 id="product-texts">Product texts</h2>
<p>The product passport (the Specification rows of the product page) and the Texture section print texts you connect
to metafields of your choice, so that every product says its own. Create the definitions first: Shopify refuses to
save a template connected to a definition that does not exist yet. Suggested definitions, all on products:</p>
<div class="table-wrap"><table class="plain">
<thead><tr><th scope="col">Name</th><th scope="col">Namespace and key</th><th scope="col">Type</th><th scope="col">Connect it to</th></tr></thead>
<tbody>
<tr><td><q>Skin type</q></td><td><code>custom.skin_type</code></td><td>Single line text</td><td>A Specification row of the product page</td></tr>
<tr><td><q>Skin feel</q></td><td><code>custom.skin_feel</code></td><td>Single line text</td><td>A Specification row, and <strong>Skin feel</strong> of the Texture section</td></tr>
<tr><td><q>Texture</q></td><td><code>custom.texture</code></td><td>Single line text</td><td>A Specification row, and <strong>Texture</strong> of the Texture section</td></tr>
<tr><td><q>Aroma</q></td><td><code>custom.aroma</code></td><td>Single line text</td><td>A Specification row</td></tr>
<tr><td><q>Dosage</q></td><td><code>custom.dosage</code></td><td>Single line text</td><td>A Specification row</td></tr>
<tr><td><q>How to use</q></td><td><code>custom.how_to_use</code></td><td>Multi-line text</td><td><strong>How to use</strong> of the Texture section</td></tr>
</tbody></table></div>
<p>To connect one, select the setting in the theme editor, choose the dynamic source icon next to it and pick the
metafield. A row or a text whose metafield is empty on a product is not printed.</p>

<h2 id="article-product">Article product</h2>
<p>A blog <strong>article</strong> metafield, <q>Product</q> (<code>custom.product</code>, type <strong>Product</strong>,
one value, under <strong>Settings, Custom data, Blog posts</strong>), links an article to one product. The Journal and
Journal article sections then paint the article in that product's color and show the product at the end of the
article. Without it, the article uses the house pair.</p>

<h2 id="metaobjects">Metaobjects</h2>
<p>Balm Studio reads no metaobject: there is nothing to create under <strong>Settings, Custom data, Metaobject
definitions</strong>. The Ingredient atlas is built from its own Ingredient blocks, each with a name, a note and the
products that contain it.</p>

<h2 id="read-directly">Metafields the theme reads directly</h2>
<p>These keys need a definition and a value, and nothing else: the theme reads them by key, so there is nothing to
connect in the theme editor. Create each definition once, with exactly this namespace and key, then fill the value on
each product, in the <strong>Metafields</strong> card of the product page in your admin.</p>
<div class="table-wrap"><table class="plain">
<thead><tr><th scope="col">Name</th><th scope="col">Namespace and key</th><th scope="col">Type</th><th scope="col">Where it shows</th><th scope="col">How to create it</th></tr></thead>
<tbody>
<tr><td><q>Tagline</q></td><td><code>custom.tagline</code></td><td>Single line text</td><td>Under the name in the Hero sequence, the Color library and the Hue finder; on the product page, the Text block with <strong>Source</strong> set to <strong>Tagline</strong>; under each product of a mega menu Products block, when <strong>Show product tagline</strong> is on in the Header.</td><td><strong>Settings, Custom data, Products</strong>, <strong>Add definition</strong>: name <q>Tagline</q>, type <strong>Single line text</strong>, one value. <a href="#tagline">Step by step</a>.</td></tr>
<tr><td><q>Badge label</q></td><td><code>custom.badge_label</code></td><td>Single line text</td><td>The Custom badge: on product cards, in quick view, in Compare products, and on the product page, on the gallery (<strong>Badges on media</strong> set to Automatic) and in the Badge block (Automatic).</td><td><strong>Settings, Custom data, Products</strong>, <strong>Add definition</strong>: name <q>Badge label</q>, type <strong>Single line text</strong>, one value. <a href="#badge-label">Step by step</a>.</td></tr>
<tr><td><q>Badge color</q></td><td><code>custom.badge_color</code></td><td>Color</td><td>The background of that product's Custom badge, everywhere the badge shows (cards, quick view, Compare products, gallery, Badge block). Empty: the <strong>Custom background</strong> of Theme settings. Filled without a badge text color, the text turns dark or light by itself, at a contrast of at least 4.5:1. Optional.</td><td><strong>Settings, Custom data, Products</strong>, <strong>Add definition</strong>: name <q>Badge color</q>, type <strong>Color</strong>. <a href="#badge-colors">Step by step</a>.</td></tr>
<tr><td><q>Badge text color</q></td><td><code>custom.badge_text_color</code></td><td>Color</td><td>The text of that product's Custom badge, in the same places. Empty: the <strong>Custom text</strong> of Theme settings, or the automatic text when <code>custom.badge_color</code> is filled. Optional.</td><td><strong>Settings, Custom data, Products</strong>, <strong>Add definition</strong>: name <q>Badge text color</q>, type <strong>Color</strong>. <a href="#badge-colors">Step by step</a>.</td></tr>
<tr><td><q>Primary collection</q></td><td><code>custom.primary_collection</code></td><td>Collection (one value)</td><td>On a product page, the collection shown in the breadcrumb trail and in its structured data when the visitor did not come through a collection, with <strong>Show the collection</strong> on in Theme settings, Breadcrumbs. Without it, the product's first collection. Optional.</td><td><strong>Settings, Custom data, Products</strong>, <strong>Add definition</strong>: name <q>Primary collection</q>, type <strong>Collection</strong>, one value. <a href="#primary-collection">Step by step</a>.</td></tr>
<tr><td><q>Banner image</q></td><td><code>custom.banner_image</code></td><td>File (image)</td><td>A <strong>collection</strong> metafield: the picture of the collection banner, before the Banner image of the Collection section and the collection's own image, framed at the focal point set in Files. Optional.</td><td><strong>Settings, Custom data, Collections</strong>, <strong>Add definition</strong>: name <q>Banner image</q>, type <strong>File</strong>, images only. <a href="#banner-image">Step by step</a>.</td></tr>
<tr><td><q>Image</q></td><td><code>custom.image</code></td><td>File (image)</td><td>A <strong>page</strong> metafield: the picture of a page in the dropdowns of the main menu and in a mega menu Image cards block set to Automatic. Collections, products and blog posts use their own image. Optional.</td><td><strong>Settings, Custom data, Pages</strong>, <strong>Add definition</strong>: name <q>Image</q>, type <strong>File</strong>, images only. <a href="#page-image">Step by step</a>.</td></tr>
<tr><td><em>Shopify standard</em></td><td><code>reviews.rating</code>, <code>reviews.rating_count</code></td><td>Rating, Integer</td><td>The Rating block, the ratings on cards, in quick view and in Compare products.</td><td>Nothing to create: a review app creates and fills them. See <a href="#reviews">Review metafields</a>.</td></tr>
</tbody></table></div>
<p>Compare products reads no fixed key: each of its rows reads the metafield you name. See
<a href="#compare">Compare products rows</a>.</p>

<h3 id="badge-label">Badge label, step by step</h3>
<ol class="steps">
  <li>In your admin, open <strong>Settings</strong>, then <strong>Custom data</strong>, then <strong>Products</strong>.</li>
  <li>Choose <strong>Add definition</strong>.</li>
  <li>Name: <q>Badge label</q>. Check that the namespace and key read <code>custom.badge_label</code>.</li>
  <li>Select the type <strong>Single line text</strong> (under Text), keep <strong>One value</strong>, and save.</li>
  <li>Open a product, find the <strong>Metafields</strong> card, type the badge text in <strong>Badge label</strong>, for example <q>Limited edition</q>, and save.</li>
</ol>
<p>The badge now shows wherever that product appears as a card, in quick view and in Compare products. On the product
page it shows when <strong>Badges on media</strong> is on Automatic or a Badge block is in the column. Its colors are in
<a href="theme-settings.html#ts-product-badges">Theme settings, Product badges</a>, unless the product has its own
(below). Clear the value and the badge goes.</p>

<h3 id="badge-colors">Badge colors, step by step</h3>
<p>Optional: only for products whose Custom badge should not wear the colors of Theme settings.</p>
<ol class="steps">
  <li>In <strong>Settings, Custom data, Products</strong>, choose <strong>Add definition</strong>. Name: <q>Badge color</q>, namespace and key <code>custom.badge_color</code>, type <strong>Color</strong>. Save.</li>
  <li>Choose <strong>Add definition</strong> again. Name: <q>Badge text color</q>, namespace and key <code>custom.badge_text_color</code>, type <strong>Color</strong>. Save.</li>
  <li>Open a product that has a <strong>Badge label</strong>, and in its <strong>Metafields</strong> card pick a <strong>Badge color</strong>, for example a deep green. Pick a <strong>Badge text color</strong> too, or leave it empty.</li>
</ol>
<p>With only the badge color, the text is picked for you: the text color or the background color of Scheme 1,
whichever contrasts more with the badge, or pure black or white when neither reaches 4.5:1. With only the text color,
the text sits on the Custom background of Theme settings. Create both as <strong>Color</strong>: a value that is not a
color, such as a word typed in a text metafield, is ignored. The two colors apply to the Custom badge only, never to
Sale, Sold out or New, and not to the Spinning badge, which keeps the colors set in its block.</p>

<h3 id="primary-collection">Primary collection, step by step</h3>
<p>Optional: for products that sit in several collections, to choose the one the breadcrumb trail shows.</p>
<ol class="steps">
  <li>In <strong>Settings, Custom data, Products</strong>, choose <strong>Add definition</strong>. Name: <q>Primary collection</q>, namespace and key <code>custom.primary_collection</code>, type <strong>Collection</strong> (under References), one value. Save.</li>
  <li>Open a product, and in its <strong>Metafields</strong> card pick the collection in <strong>Primary collection</strong>.</li>
  <li>Check that <strong>Show breadcrumbs</strong> and <strong>Show the collection</strong> are on in <a href="theme-settings.html#ts-breadcrumbs">Theme settings, Breadcrumbs</a>.</li>
</ol>
<p>A visitor who arrives from a collection grid still sees that collection in the trail; the metafield decides for the
others, such as a visitor coming from a search engine. Search engines read the same trail.</p>

<h3 id="banner-image">Banner image, step by step</h3>
<p>Optional: for collections whose banner needs another picture than the collection image, or a precise framing.</p>
<ol class="steps">
  <li>In <strong>Settings, Custom data, Collections</strong>, choose <strong>Add definition</strong>. Name: <q>Banner image</q>, namespace and key <code>custom.banner_image</code>, type <strong>File</strong>, with images accepted. Save.</li>
  <li>Open a collection in <strong>Products, Collections</strong>, and in its <strong>Metafields</strong> card pick the picture.</li>
  <li>To control the framing, set the focal point of the picture in <strong>Content, Files</strong>.</li>
</ol>
<p>The banner takes, in this order, this metafield, the <strong>Banner image</strong> of the Collection section, then
the collection's own image. Shopify keeps no focal point on a collection's own image, which is why the metafield and
the section setting exist.</p>

<h3 id="page-image">Page image, step by step</h3>
<p>Optional: for pages linked from the main menu, so their link shows a picture in the dropdowns and in Image cards.</p>
<ol class="steps">
  <li>In <strong>Settings, Custom data, Pages</strong>, choose <strong>Add definition</strong>. Name: <q>Image</q>, namespace and key <code>custom.image</code>, type <strong>File</strong>, with images accepted. Save.</li>
  <li>Open a page in <strong>Online Store, Pages</strong>, and pick its picture in the <strong>Metafields</strong> card.</li>
</ol>
<p>A page without it shows its link without a picture, and an Image cards block set to Automatic leaves it out.</p>

<h3 id="tagline">Tagline, step by step</h3>
<ol class="steps">
  <li>In <strong>Settings, Custom data, Products</strong>, choose <strong>Add definition</strong>.</li>
  <li>Name: <q>Tagline</q>, namespace and key <code>custom.tagline</code>, type <strong>Single line text</strong>. Save.</li>
  <li>Fill it on each product, for example <q>Rich overnight repair for dry skin</q>.</li>
  <li>The default product template already has a Text block with <strong>Source</strong> set to <strong>Tagline</strong> under the title. On another template, add a Text block and choose that source.</li>
</ol>
<p>A product without a tagline shows nothing there, not even the space of the line. In the theme editor, a dimmed
example stands in so you can place and size the block.</p>

<h2 id="product-metafields">Product metafields you connect</h2>
<p>Create these in <strong>Settings, Custom data, Products</strong>, then connect them with the dynamic source icon next
to the setting. The names and keys are suggestions; only the type matters.</p>
<div class="table-wrap"><table class="plain">
<thead><tr><th scope="col">Name</th><th scope="col">Namespace and key</th><th scope="col">Type</th><th scope="col">Connect it to</th></tr></thead>
<tbody>''' + _rows(META_ROWS_PRODUCT) + '''</tbody></table></div>

<h3 id="icon-metafields">Icon metafields, step by step</h3>
<p>The Icon list of the product page holds up to three claims, each an <strong>Icon item</strong> block, and each
claim can come from the product: an icon picture and a line of text per item, numbered by item. Create the ones you need:</p>
<div class="table-wrap"><table class="plain">
<thead><tr><th scope="col">Name</th><th scope="col">Namespace and key</th><th scope="col">Type</th><th scope="col">Where it shows</th></tr></thead>
<tbody>
<tr><td><q>Icon image 1</q>, <q>Icon image 2</q>, <q>Icon image 3</q></td><td><code>custom.icon_image_1</code> to <code>custom.icon_image_3</code></td><td>File (image)</td><td>The <strong>Icon image</strong> of the first, second and third Icon item. A picture keeps its proportions and sits on the bottom of its box.</td></tr>
<tr><td><q>Icon text 1</q>, <q>Icon text 2</q>, <q>Icon text 3</q></td><td><code>custom.icon_text_1</code> to <code>custom.icon_text_3</code></td><td>Single line text, or Multi-line text</td><td>The <strong>Heading</strong> (or the <strong>Text</strong>) of the first, second and third Icon item. Each line of a Multi-line text shows on its own line. The same metafields can feed <strong>Claim 1 text</strong> to <strong>Claim 4 text</strong> of a Products showcase spotlight, read on the spotlight's product.</td></tr>
</tbody></table></div>
<ol class="steps">
  <li>In <strong>Settings, Custom data, Products</strong>, add the definitions: for example <q>Icon image 1</q>, type <strong>File</strong>, and <q>Icon text 1</q>, type <strong>Multi-line text</strong> (or Single line text for one line).</li>
  <li>Fill them on each product, for example a leaf picture and <q>Vegan formula</q>.</li>
  <li>In the theme editor, open a product, select the first <strong>Icon item</strong> of the Icon list, then next to <strong>Icon image</strong> select the dynamic source icon and pick <q>Icon image 1</q>. Do the same next to <strong>Heading</strong> with <q>Icon text 1</q>. Repeat for the second and third items.</li>
</ol>
<p>These names and keys are suggestions: any key works, as long as the type matches, since you connect them yourself.
An item whose heading and text both come back empty stays hidden on the storefront and leaves no gap; in the theme
editor it keeps a small badge that says why.</p>

<h2 id="typed-keys">Metafields you type by key</h2>
<p>A few settings are plain text fields where you type the <code>namespace.key</code> yourself instead of using the
dynamic source icon.</p>
<div class="table-wrap"><table class="plain">
<thead><tr><th scope="col">Where</th><th scope="col">What to type</th><th scope="col">Metafield type</th></tr></thead>
<tbody>
<tr><td>Product section, Packshot captions: <strong>Caption source</strong> set to Product metafield (list), then <strong>Metafield</strong></td><td><code>custom.media_captions</code></td><td>List of single line text on products. Entry 1 captions media 1, and so on; media without an entry use their alt text.</td></tr>
<tr><td>Theme settings, Quick view: <strong>Short description metafield</strong></td><td>For example <code>custom.short_description</code></td><td>Single line or multi-line text on products. Without it, quick view shows the first paragraph of the description.</td></tr>
<tr><td>Compare products, Row block: <strong>Metafield</strong>, with <strong>Source</strong> on Metafield</td><td>The name, for example <q>Texture</q>, or the key, for example <code>custom.texture</code></td><td>Any type: each one is drawn as such. See <a href="#compare">Compare products rows</a>.</td></tr>
</tbody></table></div>

<h2 id="product-lists">Product list metafields</h2>
<p>The <strong>Products</strong> setting of the Product upsell block, of the Complementary products block and of the
cart drawer suggestions can be connected to a product metafield of type <strong>Product</strong>, set to accept a list of
products. Each product then carries its own hand picked selection, for example <q>Upsell products</q> with the key
<code>custom.upsell_products</code>. The block's <strong>Products come from</strong> setting must be on
<strong>A manual selection</strong>.</p>

<h2 id="shop-metafields">Shop metafields</h2>
<p>Every other section that paints a background (rich text, featured collection, FAQ, contact, image with text and so on)
offers the same <a href="sections.html#section-background">Section background</a> settings. Those sections are not tied
to a product, so their colors connect to <strong>shop</strong> metafields, created in <strong>Settings, Custom data,
Shop</strong>. One value then applies storewide, which lets you restyle every connected section at once.</p>
<div class="table-wrap"><table class="plain">
<thead><tr><th scope="col">Name</th><th scope="col">Namespace and key</th><th scope="col">Type</th><th scope="col">Connect it to</th></tr></thead>
<tbody>''' + _rows(META_ROWS_SHOP) + '''</tbody></table></div>

<h2 id="reviews">Review metafields</h2>
<p>The Rating block, the ratings on product cards, in quick view and in Compare products read Shopify's standard review
metafields, <code>reviews.rating</code> (Rating) and <code>reviews.rating_count</code> (Integer). Review apps fill them;
you have nothing to create. Until they are filled, the ratings stay hidden.</p>

<h2 id="compare">Compare products rows</h2>
<p><a href="features.html#compare-products">Compare products</a> has no metafield of its own. Each Row block with
<strong>Source</strong> set to Metafield reads the product metafield you name in its <strong>Metafield</strong> setting,
on every compared product, so you decide which facts the table compares. Type the metafield's name, exactly as it
shows in <strong>Settings, Custom data, Products</strong> (<q>Skin type</q>), or its key (<code>custom.skin_type</code>).
A name is turned into the key the admin gives it by default: namespace <code>custom</code>, the name in lowercase with
underscores. If you changed the key of a definition, type the key.</p>
<p>The field takes no dynamic source on purpose: a connected metafield would give the value of the page's product in
every column. To name the row after the metafield, connect it to the row's <strong>Label</strong> instead, or leave
Label empty to show the name you typed. For example, to compare three creams of a range:</p>
<div class="table-wrap"><table class="plain">
<thead><tr><th scope="col">Name</th><th scope="col">Namespace and key</th><th scope="col">Type</th><th scope="col">Where it shows</th><th scope="col">How to create it</th></tr></thead>
<tbody>
<tr><td><q>Texture</q></td><td><code>custom.texture</code></td><td>Single line text</td><td>A Row block with <strong>Metafield</strong> <q>Texture</q>. Each product shows its value, for example <q>Rich balm</q> or <q>Light gel</q>.</td><td><strong>Settings, Custom data, Products</strong>, <strong>Add definition</strong>: name <q>Texture</q>, type <strong>Single line text</strong>, one value.</td></tr>
<tr><td><q>Skin type</q></td><td><code>custom.skin_type</code></td><td>Single line text, or a list</td><td>A Row block with <strong>Metafield</strong> <q>Skin type</q>, for example <q>Dry to very dry</q>. A list of values reads as a sentence.</td><td><strong>Settings, Custom data, Products</strong>, <strong>Add definition</strong>: name <q>Skin type</q>, type <strong>Single line text</strong>.</td></tr>
<tr><td><q>Fragrance free</q></td><td><code>custom.fragrance_free</code></td><td>True or false</td><td>A Row block with <strong>Metafield</strong> <q>Fragrance free</q>: a check mark for true, a cross for false.</td><td><strong>Settings, Custom data, Products</strong>, <strong>Add definition</strong>: name <q>Fragrance free</q>, type <strong>True or false</strong>.</td></tr>
<tr><td><q>Volume</q></td><td><code>custom.volume</code></td><td>Volume, or Integer</td><td>A Row block with <strong>Metafield</strong> <q>Volume</q>. A volume, weight or dimension carries its unit; for a plain number, type the <strong>Unit</strong> of the row, such as ml or %.</td><td><strong>Settings, Custom data, Products</strong>, <strong>Add definition</strong>: name <q>Volume</q>, type <strong>Volume</strong>.</td></tr>
</tbody></table></div>
<ol class="steps">
  <li>Create one definition per fact, as in the table. These names and keys are examples: any name works, as long as the row names the same metafield.</li>
  <li>Fill the values on each product you compare, in the <strong>Metafields</strong> card of the product.</li>
  <li>In the theme editor, open the Compare products section and add one <strong>Row</strong> block per fact. Keep <strong>Source</strong> on Metafield, type the name or the key in <strong>Metafield</strong>, and a <strong>Label</strong> if the left column should read differently.</li>
</ol>
<p>Every metafield type is drawn as such: true or false as icons, a list as a sentence, a number with the row's unit,
rich text and multi-line text with their lines, a money amount, a rating out of its scale, a color with its swatch, an
image, and a reference (a product, a collection, a page) by its title. A product without a value shows a hyphen, read
as n/a by screen readers. In the theme editor, a row whose metafield none of the compared products has says so, so you
can fix the name.</p>
<p>The other sources need no metafield: <strong>Vendor</strong>, <strong>Product type</strong>, <strong>Tags</strong>,
<strong>SKU</strong>, <strong>Barcode</strong>, <strong>Weight</strong> and <strong>Unit price</strong> read the
product's own fields. The rating row reads the review metafields (see <a href="#reviews">Review metafields</a>).</p>

<h2 id="empty-values">What happens on a product with no value</h2>
<p>Nothing breaks and nothing goes blank, which is what lets you fill only the products you care about. A background
color that comes back empty falls through, in this order:</p>
<ol>
  <li>the <strong>Fallback background color</strong> setting, if you set one;</li>
  <li>otherwise the background of the section's color scheme.</li>
</ol>
<p>In a Products showcase spotlight and in Featured set, the order is the override field, then the product's
metafield, then the background of the section's color scheme. In the Product gradient mode of the product page, one
color alone paints a flat background and no color leaves the color scheme; the fallback color is not used there. For
the Custom badge, an empty <code>custom.badge_color</code> or <code>custom.badge_text_color</code> leaves the Custom
colors of Theme settings. Behind cutout images, an empty tagline shows no text, and an empty
<code>custom.background_color_end</code> gives the text the scheme text color.</p>
<p>Never connect the fallback color itself to a metafield: it is the safety net. If one end of a gradient is empty, the
other end fills the whole wash; if a halo color is empty, the halo is not drawn and the base color stays. An empty
text, rich text or image metafield shows nothing on the storefront: never an example text, never an empty box. The
tagline, a popup, an accordion row, a claim line, a specification row, the rating and the badges hide themselves and
leave no gap. In the theme editor a dimmed example stands in.</p>

<h2 id="not-connectable">Settings that cannot be connected</h2>
<p>Shopify only allows connections on colors, text, rich text, images, videos, links, pages, collections, products and
metaobjects. Sliders, checkboxes, dropdowns, the color scheme and Liquid code are fixed for the whole template. When one
product needs a different value for one of those, give it a
<a href="product-page.html#second-template">second product template</a>.</p>
'''

# ------------------------------------------------------------------ Custom code
CODE_LEAD = ('Balm Studio is built to be shaped from the theme editor, without code. If you or a developer do edit the theme '
             'code, read this page first.')

CUSTOM_CODE = '''
<div class="callout callout--warn" role="note">
  <p class="callout__title">Duplicate the theme before any code change</p>
  <p>Before you edit a single file, make a copy of the theme: in your admin, go to <strong>Online Store, Themes</strong>,
  open the <strong>...</strong> menu of Balm Studio and choose <strong>Duplicate</strong>. Make your changes on the copy, preview
  it, and publish it only once it works. Your live theme stays untouched, and you can go back to it at any moment.</p>
</div>

<h2 id="hire-a-partner">Get help from a Shopify Partner</h2>
<p>Code customizations are outside the scope of Balm Studio support. For custom features, design changes or integrations, we
recommend working with a Shopify Partner: developers and agencies vetted by Shopify, listed in the
<a href="https://www.shopify.com/partners/directory">Shopify Partner Directory</a>.</p>

<h2 id="before-coding">Try the editor first</h2>
<p>Many changes need no edit to the theme files:</p>
<ul>
  <li>The <a href="sections.html#s-custom-liquid">Custom Liquid</a> section, and the Liquid blocks of the product page and of the content sections, accept your own Liquid, HTML and app snippets.</li>
  <li>Shopify's <strong>Custom CSS</strong> field, at the bottom of each section's settings and in Theme settings, takes CSS scoped to that section or to the whole store.</li>
  <li>The <a href="sections.html#s-apps">Apps</a> section and app blocks place app content without touching the code.</li>
</ul>
<p>Code added this way is kept when you update the theme.</p>

<h2 id="updates-and-code">Theme updates and your code</h2>
<p>When you update Balm Studio, Shopify installs the new version as a separate copy and carries over your theme editor settings
and content, but not the changes you made in the theme files. Keep a list of every file you changed and why, so the
changes can be applied again to the new version.</p>

<h2 id="support-scope">What support covers</h2>
<p>Balm Studio support covers the theme as shipped. When a problem shows up on a theme whose code was modified, we may ask you
to reproduce it on an unmodified copy of Balm Studio first. See <a href="support.html">Support</a>.</p>
'''

# ------------------------------------------------------------------ FAQ
FAQ_LEAD = 'Answers to the questions merchants ask most about Balm Studio.'

FAQ = [
    ('Can I use Balm Studio on more than one store?', '''
<p>A theme bought from the Shopify Theme Store is licensed for one store. To use Balm Studio on another store, buy it again
from that store. Trying the theme is free on any store.</p>'''),
    ('How do I update Balm Studio without losing my settings?', '''
<p>When an update is available, your theme library shows a notice. Shopify adds the new version as a separate copy that
keeps your theme editor settings and content. Preview it, then publish it. Changes you made in the theme code are not
carried over; see <a href="custom-code.html#updates-and-code">Custom code</a>.</p>'''),
    ('How do I make the header transparent over my hero?', '''
<ol>
  <li>In the Header section, keep <strong>Header behavior</strong> on <strong>Transparent at top</strong>, the default,
  or choose <strong>Adaptive</strong>.</li>
  <li>Make sure the first section of the page is a Hero, Slideshow, Video, Products showcase or Brand story hero with
  <strong>Allow transparent header</strong> checked, or another section with <strong>Header over this section</strong>
  checked.</li>
  <li>If your hero is dark, upload a light version of your logo in <strong>Logo for dark backgrounds</strong>, and check
  that <strong>Colors over dark backgrounds</strong> is a scheme with light text. The header picks them on its own over
  a dark image.</li>
</ol>
<p>A floating announcement bar over the same image can follow those colors: check <strong>Use the header's colors over
dark backgrounds</strong> in the Announcement bar section. See the
<a href="sections.html#s-header-tone">white header example</a>.</p>
<p>On the product page, the Product section can run its Product gradient under the transparent header: see
<a href="product-page.html#bg-under-header">Extend the gradient under the header</a>.</p>'''),
    ('Why does the product gradient not reach under the header?', '''
<p>Four conditions, all needed: <strong>Background mode</strong> of the Product section is <strong>Product gradient
(metafields)</strong>, <strong>Extend the background under the header</strong> is checked, the Header section has
<strong>Header behavior</strong> on Transparent at top or Adaptive, and the Product section is the first section of
the product template. A Solid announcement bar in full width stays above the gradient; a Floating or Glass bar lets it
run underneath. The header picks light or dark colors for each product on its own: if its text is hard to read over a
dark gradient, check that <strong>Colors over dark backgrounds</strong> in the Header is a scheme with light text.
See <a href="product-page.html#bg-under-header">Extend the gradient under the header</a>.</p>'''),
    ('Why is there no country or language selector in my header?', '''
<p>The selectors only show when there is a choice to make. The country selector needs at least two countries or
regions in <strong>Settings, Markets</strong>; the language selector needs at least two published languages in
<strong>Settings, Languages</strong>, active in the visitor's market. Then check that <strong>Country and language
selectors</strong> in the Header section is not set to Off. See
<a href="sections.html#s-header-localization">Country and language selectors</a>.</p>'''),
    ('Why are there no filters on my collection pages?', '''
<p>Filters come from Shopify's free Search &amp; Discovery app. Install it, add the filters you want (availability,
price, product type, color and so on), then check that <strong>Enable filters</strong> is on in the Collection and
Search sections. A filter only shows when the products of the page have values for it.</p>'''),
    ('How do I set up a mega menu?', '''
<p>Create your main menu in your admin first. Then, in the Header section, add a <strong>Mega menu</strong> block and
type the exact title of a top level menu item in <strong>Linked menu item</strong>, for example <q>Shop</q>. Pick a
<strong>Layout</strong>: Links and images builds the panel from that item's sub-links on its own; Custom blocks uses the
Link column, Image, Image cards, Products, Promo or Banner blocks you add inside it. The panel opens when a shopper
hovers that item. See
<a href="sections.html#mega-menu-blocks">Mega menu blocks</a>.</p>'''),
    ('How do I give each product its own background color?', '''
<p>Create two product metafield definitions of type Color, <q>Background color</q> (<code>custom.background_color</code>)
and <q>Background color end</q> (<code>custom.background_color_end</code>), and fill them on each product. Then set
<strong>Background mode</strong> of the Product section to <strong>Product gradient (metafields)</strong>: there is
nothing to connect, and one color alone gives a flat background. For a solid color or a radial halo, connect the
metafield to the setting instead. Both ways are on <a href="metafields.html#product-color">Metafields</a>.</p>'''),
    ('How do I make all headings, or all text, larger?', '''
<p>Use <strong>Heading scale</strong> and <strong>Body scale</strong> in Theme settings, Typography. They multiply every
size of the theme, the ones set in sections and blocks included, from 80 to 130%. Changing each section's sizes one by
one is only worth it for a single element. See <a href="features.html#type-sizes">Type sizes</a>.</p>'''),
    ('Why is there no text behind my product image?', '''
<p>The text of <strong>Text behind cutouts</strong> only shows behind PNG and WebP images; JPG images, videos and 3D
models never get it. Check that <strong>Show on desktop</strong> or <strong>Show on mobile</strong> is on for the device
you are looking at, and that the first media of the gallery is a PNG or WebP image when <strong>Apply to</strong> is
First image only. With <strong>Text</strong> on Product tagline, a product whose <code>custom.tagline</code> is empty
shows no text. See <a href="product-page.html#text-behind-cutouts">Text behind cutout images</a>.</p>'''),
    ('Why does the spinning badge not show on some products?', '''
<p>The ring prints the product's <code>custom.badge_label</code> metafield and has no text of its own: a product with
no value shows no ring. Fill the metafield on that product (see <a href="metafields.html#badge-label">Badge label, step
by step</a>). With <strong>Next to the title</strong>, the page also needs a Title block.</p>'''),
    ('Where are Balm spotlight, Lifestyle strip, the Sticky add to cart and Quantity blocks?', '''
<p>They belonged to preview versions of Balm Studio and were removed before release, together with the free text of the
spinning badge.</p>
<ul>
  <li><strong>Balm spotlight</strong>, the second version of the Product section: its gradient and its spinning badge are now the <a href="product-page.html#bg-product-gradient">Product gradient</a> background mode and the positions of the <a href="product-page.html#pb-product-badge">Spinning badge</a> block, on the one Product section.</li>
  <li><strong>Lifestyle strip</strong>, two photos side by side: the section has been removed.</li>
  <li><strong>Sticky add to cart block</strong>: the bar is the <a href="sections.html#s-sticky-atc">Sticky add to cart</a> section, placed below the Product section in the product template.</li>
  <li><strong>Spinning badge text</strong>: the ring of the product page reads the product's <code>custom.badge_label</code> metafield only. The spotlights of the Products showcase keep a text of their own: see <a href="product-page.html#pb-product-badge">Spinning badge of a spotlight</a>.</li>
  <li><strong>Quantity block</strong>: the quantity selector is part of the <a href="product-page.html#pb-product-buy-buttons">Buy buttons</a> block, set by <strong>Quantity selector (desktop)</strong> and <strong>Quantity selector (mobile)</strong>.</li>
</ul>'''),
    ('Why can I not connect a setting to my metafield?', '''
<p>Three usual causes. The definition does not exist yet: create it in Settings, Custom data first. The type does not
match: a color setting only accepts a Color metafield, an image setting a File metafield. Or the definition was created
for the wrong resource: product page settings need a <strong>Products</strong> definition, other sections a
<strong>Shop</strong> definition. The help text of each connectable setting names the exact definition it expects.</p>'''),
    ('How do I add product reviews and star ratings?', '''
<p>Install a reviews app that writes Shopify's standard review metafields (most do). Balm Studio's Rating block, the ratings on
product cards and quick view read them automatically once reviews come in. If the app offers an app block for its review
list, add it to the product page from the block picker.</p>'''),
    ('How do I add a size guide or ingredients list to product pages?', '''
<p>Create a page with the content in Online Store, Pages. On the product page, add a <strong>Popup</strong> block (a link
that opens a dialog) or a <strong>Collapsible row</strong>, and set <strong>Content comes from</strong> to <strong>A
page</strong>. For content that differs per product, connect the block's Content to a rich text metafield instead.</p>'''),
    ('Can I change the color of the Shop Pay or PayPal buttons?', '''
<p>No theme can. The accelerated checkout buttons are drawn by Shopify with the brand colors of each payment provider.
Balm Studio matches everything Shopify allows: height, corner radius, spacing and the loading placeholder. See
<a href="product-page.html#accelerated-checkout">The accelerated checkout buttons</a>.</p>'''),
    ('How do I show a free shipping progress bar?', '''
<p>In <a href="theme-settings.html#ts-cart">Theme settings, Cart</a>, keep <strong>Show the free shipping bar</strong>
checked and type the amount in <strong>Free shipping threshold</strong>. The bar only displays progress: create the matching free shipping rate or automatic
discount in your admin, and keep the two amounts the same, or buyers will be promised something checkout does not
apply.</p>'''),
    ('Why does the Buy it now button disappear on some variants?', '''
<p>The accelerated checkout buttons (Buy it now, Shop Pay, PayPal and the other wallets) are hidden while the selected
variant is sold out, since it cannot be bought, and come back when the shopper picks a variant in stock. A variant that
sells as a pre-order can be bought, so it keeps them. See
<a href="product-page.html#accelerated-checkout">The accelerated checkout buttons</a>.</p>'''),
    ('How do I offer pre-orders?', '''
<p>Set the variant to continue selling when out of stock in the product admin. At 0 stock its buttons read Pre-order,
or the label you set in Theme settings, Pre-order. To take a deposit or charge later, use a pre-order app. See
<a href="features.html#pre-order">Pre-order</a>.</p>'''),
    ('How do I translate my store?', '''
<p>Add and publish your languages in Settings, Languages. Balm Studio's own texts are already translated into French, German,
Italian and Spanish. Translate what you typed in the editor with the Translate &amp; Adapt app. See
<a href="features.html#translations">Translations</a>.</p>'''),
    ('The newsletter popup does not appear. What should I check?', '''
<ul>
  <li><strong>Enable popup</strong> is checked in the Newsletter popup section, and the section is on the template you are viewing (by default, the home page only).</li>
  <li>You closed it earlier: it stays hidden for the number of days in <strong>Reappear after</strong>. Test in a private window.</li>
  <li>The <strong>Open delay</strong> has not passed yet.</li>
</ul>'''),
    ('Why does my header change color as I scroll?', '''
<p>With <strong>Header behavior</strong> on Transparent at top or Adaptive, the header reads what lies under it and
wears the colors that read best there: its own color scheme and logo over a light background, <strong>Colors over dark
backgrounds</strong> and <strong>Logo for dark backgrounds</strong> over a dark one. With Adaptive it does so at every
scroll position, so it changes as dark and light sections pass under it. To keep one look everywhere, set Header
behavior to <strong>Standard</strong>. See <a href="features.html#header-colors">Automatic header colors</a>.</p>'''),
    ('How do I line up a section with the header or make it edge to edge?', '''
<p>Use the section's <strong>Section width</strong> setting. <strong>Full width</strong> runs the background or the
picture from one edge of the screen to the other, <strong>Full width with margins</strong> stops at the
<strong>Section side margins</strong> of Theme settings, Layout, and <strong>Page width</strong> lines it up with the
product and collection pages. <strong>Theme default</strong>, the default, follows <strong>Default section width</strong>
in Theme settings, Layout: change it there to move every section left on it at once. See
<a href="features.html#section-width">Section width</a>.</p>'''),
    ('Where do I add my Instagram, TikTok and other social media links?', '''
<p>In <a href="theme-settings.html#ts-social-media">Theme settings, Social media</a>: paste the full address of each
profile. The icons then show in the footer's Social media links block and in the Social media links section, and in the
header on desktop when <strong>Show social media icons</strong> is checked. Networks without an address stay hidden.
See <a href="features.html#social-media">Social media</a>.</p>'''),
    ('How do I hide the Sale badges in one section only?', '''
<p>Set that section's <strong>Badges</strong> setting to <strong>Custom only</strong> (only your
<code>custom.badge_label</code> badges) or <strong>None</strong>. The other sections keep their own choice. Every
section with product cards has it, as do the Bento Product tile and the Complementary products block. See
<a href="features.html#badges-per-section">Choose the badges of each section</a>.</p>'''),
    ('How do I let shoppers choose the number of columns on collection pages?', '''
<p>In the Collection section, check <strong>Let visitors change the column count (desktop)</strong>, which adds 2, 3
and 4 buttons beside the sort, and <strong>Let visitors change the column count (mobile)</strong>, which adds 1 and 2
buttons beside the filters on phones. Each device keeps the shopper's choice for the rest of the visit. See
<a href="features.html#collection-columns">Column selector</a>.</p>'''),
    ('My speed score dropped after I turned on the page loader. Why?', '''
<p>A loader covers the page while it loads, which speed tools measure as a slower page. Set <strong>Page loader</strong>
to <strong>First visit only</strong>, the recommended setting, or turn it off. <strong>Every page</strong> shows it on
each page view and has the largest effect.</p>'''),
]

# ------------------------------------------------------------------ Support
SUPPORT_LEAD = 'Balm Studio support answers questions about the theme and fixes its bugs. Here is what it covers and how to reach it.'

SUPPORT = f'''
<p class="cta"><a class="button" href="{SUPPORT_FORM}" rel="noopener">Contact Balm Studio support</a></p>

<h2 id="covered">What support covers</h2>
<ul>
  <li><strong>Bugs</strong> in the theme as shipped: something that does not work as this documentation describes.</li>
  <li><strong>Questions</strong> about the theme: installing it, its settings, sections, blocks and features, and how to reach a result with them.</li>
</ul>

<h2 id="not-covered">What support does not cover</h2>
<ul>
  <li><strong>Customizations</strong>: changes to the theme code, new features, custom designs, or code added in Custom Liquid sections, Liquid blocks or Custom CSS. For this work we recommend a <a href="https://www.shopify.com/partners/directory">Shopify Partner</a>.</li>
  <li>Problems caused by edits to the theme files. We may ask you to reproduce the problem on an unmodified copy of Balm Studio.</li>
  <li>Third party apps and services, and Shopify features outside the theme (checkout, payments, shipping rules, domains). For those, contact the app developer or Shopify Support.</li>
</ul>

<h2 id="response-time">Response time</h2>
<p>We reply within <strong>two business days</strong> (Monday to Friday), usually sooner.</p>

<h2 id="request">How to send a request</h2>
<p>Use the <a href="{SUPPORT_FORM}" rel="noopener">support form</a>. To help us answer in one go, include:</p>
<ul>
  <li>your store address (<code>yourstore.myshopify.com</code>) and the name of the theme in your library;</li>
  <li>the link of the page where the problem happens;</li>
  <li>what you did, what you expected and what happened instead, with a screenshot or a short video if you can;</li>
  <li>the browser and device you used;</li>
  <li>whether the theme code was modified.</li>
</ul>
<p>Before writing, it is worth checking the <a href="faq.html">FAQ</a> and searching this documentation. If an app
could be involved, try with it turned off.</p>
'''
