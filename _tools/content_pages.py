SUPPORT_FORM = 'https://form.jotform.com/262695466571066'

# ------------------------------------------------------------------ Getting started
GS_LEAD = ('Balm is an Online Store 2.0 theme for Shopify: every page is built from sections and blocks that you add, '
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

<h2 id="install">Install Balm from the Theme Store</h2>
<ol class="steps">
  <li>Open the Balm page on the <a href="https://themes.shopify.com/">Shopify Theme Store</a> while logged in to your store.</li>
  <li>Select <strong>View demo store</strong> to browse Balm with its content before you install it.</li>
  <li>Select <strong>Try theme</strong> to add a trial copy to your theme library, or buy the theme straight away. A trial lets you customize everything; you pay when you publish.</li>
  <li>In your admin, go to <strong>Online Store, Themes</strong>. Balm is in your theme library. Select <strong>Customize</strong> to open the theme editor.</li>
  <li>When the store is ready, open the theme's <strong>...</strong> menu in the theme library and choose <strong>Publish</strong>.</li>
</ol>
<p>Balm needs no app to work. Apps that offer app blocks, such as reviews, subscriptions or bundles, plug into the
product page and into most sections.</p>

<h3 id="updates">Updating Balm</h3>
<p>When a new version is released, your theme library shows an update notice. Shopify adds the new version to your
library as a separate copy that keeps your theme editor settings and content, so you can review it before publishing.
Changes made directly in the theme code are not carried over: see <a href="custom-code.html">Custom code</a>. What changed
in each version is listed in the <a href="changelog.html">Changelog</a>.</p>

<h2 id="preset">The Balm preset</h2>
<p>A preset is a starting style: color schemes, font pairing, corner radii, glass recipe and typography recipes. Balm
comes with one preset, also named Balm, and your store starts from it.</p>
<ul>
  <li><strong>Look.</strong> Clean and neutral: a white scheme and a near black scheme, sentence case headings and buttons, a white frosted glass. A calm base that lets product photography lead.</li>
  <li><strong>Fonts.</strong> Inter 600 for headings, Inter for body text.</li>
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
<strong>(mobile)</strong>, so you can tune phones without touching large screens. Use the device switch at the top of
the editor to preview both.</p>

<h2 id="first-setup">First setup, step by step</h2>
<ol class="steps">
  <li><strong>Logo and menu.</strong> Open the <a href="sections.html#s-header">Header</a> section. Set <strong>Logo type</strong> and upload your <strong>Logo image</strong>, then pick your main menu under <strong>Menu</strong>. Menus themselves are edited in your admin, under Content, Menus (Online Store, Navigation on older admins).</li>
  <li><strong>Colors.</strong> In <a href="theme-settings.html#ts-colors">Theme settings, Colors</a>, adjust the two color schemes of the Balm preset to your brand. Every section picks one of them.</li>
  <li><strong>Fonts and corners.</strong> Set the <strong>Heading font</strong> and <strong>Body font</strong> in <a href="theme-settings.html#ts-typography">Typography</a>, and the corner radii in <a href="theme-settings.html#ts-corner-style">Corner style</a>.</li>
  <li><strong>Home page.</strong> The home page starts with a Hero, a Marquee, a Products showcase, Socials, Image with text, Rich text and the Newsletter popup. Replace their images and texts, remove what you do not need, and add sections with <strong>Add section</strong>.</li>
  <li><strong>Product page.</strong> Open a product in the editor and review the block stack. See <a href="product-page.html">Product page blocks</a>, and <a href="metafields.html">Metafields</a> if each product should carry its own color or texts.</li>
  <li><strong>Collections and search.</strong> Install Shopify's free Search &amp; Discovery app to choose the filters shown on collection and search pages, then set their layout in the <a href="sections.html#s-main-collection">Collection</a> section.</li>
  <li><strong>Cart.</strong> Open the <a href="sections.html#s-cart-drawer">Cart drawer</a> for the reward progress bar, suggestions and the order note. Turn on <a href="features.html#gift-wrapping">gift wrapping</a> if you offer it.</li>
  <li><strong>Footer.</strong> Add your menus, newsletter, social links and, if you sell in several countries, the Localization block.</li>
  <li><strong>Favicon and sharing.</strong> Upload a favicon and a fallback share image in Theme settings.</li>
  <li><strong>Pages.</strong> Create your About, Contact, FAQ and Where to buy pages in Online Store, Pages, and assign them the matching template under <strong>Theme template</strong>: <code>page.about</code>, <code>page.contact</code>, <code>page.faq</code>, <code>page.find-us</code>. The <code>page.products</code> template presents your range with a Featured set and a Products showcase.</li>
  <li><strong>Check and publish.</strong> Preview every page type on desktop and on a phone, place a test order, then publish.</li>
</ol>

<h2 id="templates">Templates included</h2>
<p>Home page, product, collection, list of collections, search, cart, blog, blog post, page, 404, password and gift card,
plus five page templates: <code>page.about</code> (About), <code>page.contact</code> (Contact), <code>page.faq</code> (FAQ),
<code>page.find-us</code> (Store locator) and <code>page.products</code> (Products). All of them are built from sections,
so you can reshape any of them in the editor.</p>

<h2 id="help">Need help?</h2>
<p>Search this documentation with the box at the top of the page, read the <a href="faq.html">FAQ</a>, or contact
<a href="support.html">Balm support</a>.</p>
'''

# ------------------------------------------------------------------ Features
FEATURES_LEAD = ('The features that span several sections or the whole store: what they do, where to turn them on '
                 'and what to know before you rely on them.')

FEATURES = '''
<nav class="contents" aria-label="Features"><ol class="contents__list contents__list--cols">
<li><a href="#quick-view">Quick view</a></li><li><a href="#product-badges">Product badges</a></li>
<li><a href="#page-loader">Page loader</a></li><li><a href="#age-verifier">Age verifier</a></li>
<li><a href="#gift-wrapping">Gift wrapping</a></li><li><a href="#lookbook">Lookbook</a></li>
<li><a href="#compare-products">Compare products</a></li><li><a href="#recently-viewed">Recently viewed</a></li>
<li><a href="#pagination">Pagination</a></li><li><a href="#translations">Translations</a></li>
<li><a href="#combined-listings">Combined listings</a></li><li><a href="#pre-order">Pre-order</a></li>
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
  <li>Set <strong>Quick view</strong> to <strong>Button on hover</strong> or <strong>Icon</strong>. On touch screens the button is always visible.</li>
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
<tr><th scope="row">Custom</th><td>The product has a value in its <code>custom.badge_label</code> metafield.</td><td>Colors. The text is the metafield value.</td></tr>
</tbody></table></div>
<h3 id="custom-badge">Set up the Custom badge</h3>
<ol class="steps">
  <li>Create the <code>custom.badge_label</code> definition once, as described in <a href="metafields.html#badge-label">Metafields, Badge label</a>.</li>
  <li>Fill it on the products that need a badge, for example <q>Limited edition</q> or <q>Vegan</q>. Leave it empty on the others.</li>
  <li>That is all: the cards, quick view, Compare products and the product page read the metafield directly. There is no key to type and nothing to connect in the theme editor.</li>
</ol>
<h3 id="badges-product-page">Badges on the product page</h3>
<ul>
  <li><strong>Badges on media</strong>, in the Product section settings, shows the badges in the corner of the gallery: <strong>Off</strong> (the default) or <strong>Automatic</strong>, the same Sale, Sold out, New and Custom badges as the cards.</li>
  <li>The <strong>Badge</strong> block, in the information column, draws the same badges in a row when its <strong>Badge type</strong> is <strong>Automatic (Sale, Sold out, New, Custom)</strong>, the default. Its other type, <strong>Image</strong>, places your own artwork in a corner of the product area.</li>
  <li>The <strong>Spinning badge</strong> block turns the <code>custom.badge_label</code> text around a ring. A product without the metafield shows no ring.</li>
</ul>
<p>On the product page, Sale and Sold out follow the selected variant: choosing a variant without a compare-at price
removes Sale, choosing a sold out one shows Sold out. When no badge applies, nothing is drawn and no space is left.</p>
</section>

<section class="entry" id="page-loader-entry">
<h2 id="page-loader">Page loader</h2>
<p>An optional loading screen shown while pages open, with your logo, a progress bar or a spinner, and an exit animation.
Turn it on in <a href="theme-settings.html#ts-loader">Theme settings, Loader</a>, under <strong>Page loader</strong>:</p>
<ul>
  <li><strong>First visit only</strong> (recommended) shows it once per visit.</li>
  <li><strong>Every page</strong> shows it on each page view. It can lower speed scores, because the page stays covered while it loads.</li>
</ul>
<p><strong>Layout</strong> combines the logo with a progress bar or a spinner, or shows the bar alone. With a progress
bar, <strong>Bar ends</strong> (Square or Rounded, which rounds the track and the fill), <strong>Bar thickness</strong>
(1 to 6 px) and <strong>Bar animation</strong> set its look: None moves the fill in steps, Smooth fills it continuously,
Shimmer adds a gleam in the background color that crosses the filled part in a loop. The logo is the
<strong>Logo image</strong> you pick here, or else the header logo, then the brand logo from your Shopify settings, then
the store name. <strong>Background</strong> is Solid or Glass, on the <strong>Color scheme</strong> you choose. The
<strong>Exit animation</strong> (Fade, Slide up, Split, Zoom, Circle reveal) plays when the page is ready, never before
the <strong>Minimum display time</strong> and never after the <strong>Maximum display time</strong>.
<strong>Page transitions</strong> plays the exit in reverse when a visitor follows a link to another page of the store.</p>
<p>To adjust the look, check <strong>Preview in the theme editor</strong>. To test First visit only on the live store,
open a private window, or add <code>?preview_loader=1</code> to a page address while the preview is on. Visitors who ask
for reduced motion see no animation, no transition on the bar and no gleam, and without JavaScript the loader never
shows.</p>
</section>

<section class="entry" id="age-verifier-entry">
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
Built in rows show the image, price, availability, vendor and rating. Each row you add reads the product metafield of
your choice, by its key.</p>
<ol class="steps">
  <li>Create one product metafield definition per fact you want to compare, in Settings, Custom data, Products. For example <code>custom.texture</code> and <code>custom.skin_type</code> (Single line text), <code>custom.fragrance_free</code> (True or false).</li>
  <li>Fill the values on each product.</li>
  <li>Add the section, pick the products, then add one <strong>Row</strong> block per fact: a <strong>Label</strong>, the <strong>Product metafield</strong> key, and a <strong>Value type</strong>: Text, Number with unit (with its <strong>Unit</strong>, such as ml) or Yes or no.</li>
</ol>
<p>A product without a value shows a dash, and a row that no product has a value for is left out of the storefront.
<strong>Highlight differences</strong> marks the rows where products differ. On a phone the label column stays in place
while the product columns scroll. The full example is in <a href="metafields.html#compare">Metafields, Compare products rows</a>.</p>
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
<p>Balm ships in five languages: English, French, German, Italian and Spanish. That covers every storefront text of the
theme (buttons, cart, forms, filters, accessibility labels) and the theme editor itself, which follows the language of
your admin.</p>
<ol class="steps">
  <li>Add and publish your languages in <strong>Settings, Languages</strong>. The theme's own texts switch automatically.</li>
  <li>Translate the content you typed in the editor (headings, paragraphs, button labels) with Shopify's free Translate &amp; Adapt app.</li>
  <li>Leave the text settings marked <em>Leave empty to use the translated default</em> empty on a multilingual store: they then show the built in text in each language.</li>
</ol>
<p>To change the wording of a theme text, use <strong>Edit default theme content</strong> in the theme's <strong>...</strong>
menu in your theme library. For a language Balm does not ship, Translate &amp; Adapt can translate the theme texts too.</p>
</section>

<section class="entry" id="combined-listings-entry">
<h2 id="combined-listings">Combined listings</h2>
<p>Combined listings group separate products into one listing, for example one product per color, and are available to
Shopify Plus stores through Shopify's Combined Listings app. Balm supports them with nothing to configure:</p>
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
'''

# ------------------------------------------------------------------ Metafields
META_LEAD = ('Metafields let one template give every product its own colors, texts and images. This page lists the '
             'metafields Balm reads, with the exact name, key and type to create.')

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
    ('Claim title', 'custom.claim_title', 'Single line text', 'Icon item: Heading'),
    ('Claim body', 'custom.claim_body', 'Single line text', 'Icon item: Text'),
    ('Claim icon', 'custom.claim_icon', 'File', 'Icon item: Icon image'),
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
  <li>Definitions are created in <strong>Settings, Custom data</strong>, under <strong>Products</strong> or <strong>Shop</strong>.</li>
  <li>Type the <strong>Name</strong> exactly as listed below. The admin derives the key from the name, in lowercase with underscores, so the key matches on its own. If you rename a definition, check its key before saving: the connection works by key.</li>
  <li>Names are shown in quotation marks here and in the theme editor so you can see where they start and end. The quotation marks are not part of the name.</li>
  <li>The namespace and key are suggestions; the <strong>type</strong> is not. A setting refuses a definition of the wrong type.</li>
  <li>Every connectable setting repeats the definition it expects in its own help text in the editor.</li>
</ul>

<h2 id="read-directly">Metafields the theme reads directly</h2>
<p>These keys need a definition and a value, and nothing else: the theme reads them by key, so there is nothing to
connect in the theme editor. Create each definition once, with exactly this namespace and key, then fill the value on
each product, in the <strong>Metafields</strong> card of the product page in your admin.</p>
<div class="table-wrap"><table class="plain">
<thead><tr><th scope="col">Name</th><th scope="col">Namespace and key</th><th scope="col">Type</th><th scope="col">Where it shows</th><th scope="col">How to create it</th></tr></thead>
<tbody>
<tr><td><q>Tagline</q></td><td><code>custom.tagline</code></td><td>Single line text</td><td>On the product page, the Text block with <strong>Source</strong> set to <strong>Tagline</strong>, under the title in the default template. Under the name of a Products showcase spotlight and under the heading of Featured set, for the product picked in them. Under each product of a mega menu Products block, when <strong>Show product tagline</strong> is on in the Header.</td><td><strong>Settings, Custom data, Products</strong>, <strong>Add definition</strong>: name <q>Tagline</q>, type <strong>Single line text</strong>, one value. <a href="#tagline">Step by step</a>.</td></tr>
<tr><td><q>Background color</q></td><td><code>custom.background_color</code></td><td>Color</td><td>The background of a Products showcase spotlight (the start of its gradient) and of Featured set, for the product picked in them. On the product page the same metafield is connected instead: see <a href="#per-product-background">Per product background colors</a>.</td><td><strong>Settings, Custom data, Products</strong>, <strong>Add definition</strong>: name <q>Background color</q>, type <strong>Color</strong>. <a href="#showcase">Step by step</a>.</td></tr>
<tr><td><q>Background color end</q></td><td><code>custom.background_color_end</code></td><td>Color</td><td>The end of a Products showcase spotlight's background gradient. Without it, the spotlight is one color. Featured set paints one color and does not read it.</td><td><strong>Settings, Custom data, Products</strong>, <strong>Add definition</strong>: name <q>Background color end</q>, type <strong>Color</strong>. <a href="#showcase">Step by step</a>.</td></tr>
<tr><td><q>Badge label</q></td><td><code>custom.badge_label</code></td><td>Single line text</td><td>The Custom badge: on product cards, in quick view, in Compare products, and on the product page, on the gallery (<strong>Badges on media</strong> set to Automatic) and in the Badge block (Automatic). Also the text of the Spinning badge block.</td><td><strong>Settings, Custom data, Products</strong>, <strong>Add definition</strong>: name <q>Badge label</q>, type <strong>Single line text</strong>, one value. <a href="#badge-label">Step by step</a>.</td></tr>
<tr><td><em>Shopify standard</em></td><td><code>reviews.rating</code>, <code>reviews.rating_count</code></td><td>Rating, Integer</td><td>The Rating block, the ratings on cards, in quick view and in Compare products.</td><td>Nothing to create: a review app creates and fills them. See <a href="#reviews">Review metafields</a>.</td></tr>
</tbody></table></div>
<p>Compare products reads no fixed key: each of its rows reads the metafield you choose. See
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
<a href="theme-settings.html#ts-product-badges">Theme settings, Product badges</a>. Clear the value and the badge goes.</p>

<h3 id="tagline">Tagline, step by step</h3>
<ol class="steps">
  <li>In <strong>Settings, Custom data, Products</strong>, choose <strong>Add definition</strong>.</li>
  <li>Name: <q>Tagline</q>, namespace and key <code>custom.tagline</code>, type <strong>Single line text</strong>. Save.</li>
  <li>Fill it on each product, for example <q>Rich overnight repair for dry skin</q>.</li>
  <li>The default product template already has a Text block with <strong>Source</strong> set to <strong>Tagline</strong> under the title. On another template, add a Text block and choose that source.</li>
</ol>
<p>A product without a tagline shows nothing there, not even the space of the line. In the theme editor, a dimmed
example stands in so you can place and size the block.</p>

<h3 id="showcase">Products showcase and Featured set, step by step</h3>
<ol class="steps">
  <li>In <strong>Settings, Custom data, Products</strong>, create the definitions you want: <q>Tagline</q> (<code>custom.tagline</code>, <strong>Single line text</strong>), <q>Background color</q> (<code>custom.background_color</code>, <strong>Color</strong>) and <q>Background color end</q> (<code>custom.background_color_end</code>, <strong>Color</strong>).</li>
  <li>Fill them on each product, for example a soft sage and a deeper sage for a calming balm.</li>
  <li>In the theme editor, open a <strong>Spotlight</strong> block of the Products showcase, or the Featured set section, and pick the product in <strong>Product</strong>. There is nothing to connect: the name, the link, the tagline, the colors and the image follow.</li>
  <li>Keep the fields of the <strong>Override (optional)</strong> group empty: a filled field wins over the product. A spotlight set up before these settings existed keeps what was typed in it (name, tagline, colors, image, link) as overrides; clear those fields to let the product take over.</li>
</ol>
<p>A product without these values falls back cleanly: no tagline line, and the background of the section's color
scheme. A spotlight with a background color and no end color is one color. In the theme editor a dimmed example stands
in for a missing tagline.</p>

<h2 id="per-product-background">Per product background colors, step by step</h2>
<p>The most common use: one product template, a different background shade on every product.</p>
<h3 id="step-1">Step 1. Create the definition (once)</h3>
<ol class="steps">
  <li>In your admin, open <strong>Settings, Custom data, Products</strong> and choose <strong>Add definition</strong>.</li>
  <li>Name: <q>Background color</q>. Namespace and key: <code>custom.background_color</code>. Type: <strong>Color</strong>.</li>
  <li>Save.</li>
</ol>
<h3 id="step-2">Step 2. Connect it to the setting (once)</h3>
<ol class="steps">
  <li>In the theme editor, open a product page and select the <strong>Product</strong> section.</li>
  <li>Set <strong>Background mode</strong> to <strong>Solid color</strong> (or Gradient (two colors), or Radial halo; the same idea applies to each of their colors).</li>
  <li>Next to <strong>Background color</strong>, select the dynamic source icon (a small database symbol) and pick <strong>Background color</strong>.</li>
  <li>The field now shows the metafield name instead of a swatch. Save.</li>
</ol>
<h3 id="step-3">Step 3. Fill in the values (per product)</h3>
<ol class="steps">
  <li>In your admin, open a product and scroll to the <strong>Metafields</strong> card.</li>
  <li>Set <strong>Background color</strong> to that product's shade and save. Products you leave empty fall back cleanly, as explained below.</li>
</ol>
<h3 id="step-4">Step 4. Check it</h3>
<p>Open two products on the storefront, one with a value and one without. The first shows its own shade, the second
falls back. If both look the same, the connection of step 2 was not saved.</p>
<p>For a gradient, repeat step 1 with <q>Background color end</q> (<code>custom.background_color_end</code>) and connect
it to <strong>Gradient end</strong>. For a halo, create <q>Accent color</q> (<code>custom.accent_color</code>) and
connect it to <strong>Halo color</strong>.</p>

<h2 id="product-metafields">Product metafields you connect</h2>
<p>Create these in <strong>Settings, Custom data, Products</strong>, then connect them with the dynamic source icon next
to the setting. The names and keys are suggestions; only the type matters.</p>
<div class="table-wrap"><table class="plain">
<thead><tr><th scope="col">Name</th><th scope="col">Namespace and key</th><th scope="col">Type</th><th scope="col">Connect it to</th></tr></thead>
<tbody>''' + _rows(META_ROWS_PRODUCT) + '''</tbody></table></div>

<h2 id="typed-keys">Metafields you type by key</h2>
<p>A few settings are plain text fields where you type the <code>namespace.key</code> yourself instead of using the
dynamic source icon.</p>
<div class="table-wrap"><table class="plain">
<thead><tr><th scope="col">Where</th><th scope="col">What to type</th><th scope="col">Metafield type</th></tr></thead>
<tbody>
<tr><td>Product section, Packshot captions: <strong>Caption source</strong> set to Product metafield (list), then <strong>Metafield</strong></td><td><code>custom.media_captions</code></td><td>List of single line text on products. Entry 1 captions media 1, and so on; media without an entry use their alt text.</td></tr>
<tr><td>Theme settings, Quick view: <strong>Short description metafield</strong></td><td>For example <code>custom.short_description</code></td><td>Single line or multi-line text on products. Without it, quick view shows the first paragraph of the description.</td></tr>
<tr><td>Compare products, Row block: <strong>Product metafield</strong></td><td>For example <code>custom.texture</code></td><td>Any type that fits the row's <strong>Value type</strong>. See <a href="#compare">Compare products rows</a>.</td></tr>
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
<p><a href="features.html#compare-products">Compare products</a> has no metafield of its own. Each Row block reads the
product metafield of your choice: you type its <code>namespace.key</code> in the row's <strong>Product metafield</strong>
setting, so you decide which facts the table compares, and each row can read a different metafield. For example, to
compare three creams of a range:</p>
<div class="table-wrap"><table class="plain">
<thead><tr><th scope="col">Name</th><th scope="col">Namespace and key</th><th scope="col">Type</th><th scope="col">Where it shows</th><th scope="col">How to create it</th></tr></thead>
<tbody>
<tr><td><q>Texture</q></td><td><code>custom.texture</code></td><td>Single line text</td><td>A Row block with <strong>Product metafield</strong> <code>custom.texture</code> and <strong>Value type</strong> Text. Each product shows its value, for example <q>Rich balm</q> or <q>Light gel</q>.</td><td><strong>Settings, Custom data, Products</strong>, <strong>Add definition</strong>: name <q>Texture</q>, type <strong>Single line text</strong>, one value.</td></tr>
<tr><td><q>Skin type</q></td><td><code>custom.skin_type</code></td><td>Single line text</td><td>A Row block with <strong>Product metafield</strong> <code>custom.skin_type</code> and <strong>Value type</strong> Text, for example <q>Dry to very dry</q>.</td><td><strong>Settings, Custom data, Products</strong>, <strong>Add definition</strong>: name <q>Skin type</q>, type <strong>Single line text</strong>, one value.</td></tr>
<tr><td><q>Fragrance free</q></td><td><code>custom.fragrance_free</code></td><td>True or false</td><td>A Row block with <strong>Product metafield</strong> <code>custom.fragrance_free</code> and <strong>Value type</strong> Yes or no: a check mark for true, a cross for false.</td><td><strong>Settings, Custom data, Products</strong>, <strong>Add definition</strong>: name <q>Fragrance free</q>, type <strong>True or false</strong>.</td></tr>
</tbody></table></div>
<ol class="steps">
  <li>Create one definition per fact, as in the table. These names and keys are examples: any namespace and key work, as long as the row reads the same key.</li>
  <li>Fill the values on each product you compare, in the <strong>Metafields</strong> card of the product.</li>
  <li>In the theme editor, open the Compare products section and add one <strong>Row</strong> block per fact. Type the <strong>Label</strong> shown in the first column, for example <q>Texture</q>, and the <strong>Product metafield</strong> key, for example <code>custom.texture</code>, without spaces. Then choose the <strong>Value type</strong>.</li>
</ol>
<p>Match the <strong>Value type</strong> to the metafield type:</p>
<ul>
  <li><strong>Text</strong>: single line text, multi-line text, or any value you want printed as it is.</li>
  <li><strong>Number with unit</strong>: an integer or decimal, followed by the <strong>Unit</strong> you type (ml, g, %). Leave the unit empty for weight, volume and dimension metafields, which carry their own.</li>
  <li><strong>Yes or no</strong>: a True or false metafield, drawn as a check mark or a cross.</li>
</ul>
<p>A product without a value shows a dash in that row. A row that no product has a value for is left out of the
storefront; the theme editor keeps it so you can fix the key. A row without a label shows its key instead.</p>

<h2 id="empty-values">What happens on a product with no value</h2>
<p>Nothing breaks and nothing goes blank, which is what lets you fill only the products you care about. A background
color that comes back empty falls through, in this order:</p>
<ol>
  <li>the <strong>Fallback background color</strong> setting, if you set one;</li>
  <li>otherwise the background of the section's color scheme.</li>
</ol>
<p>In a Products showcase spotlight and in Featured set, the order is the override field, then the product's
metafield, then the background of the section's color scheme.</p>
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
CODE_LEAD = ('Balm is built to be shaped from the theme editor, without code. If you or a developer do edit the theme '
             'code, read this page first.')

CUSTOM_CODE = '''
<div class="callout callout--warn" role="note">
  <p class="callout__title">Duplicate the theme before any code change</p>
  <p>Before you edit a single file, make a copy of the theme: in your admin, go to <strong>Online Store, Themes</strong>,
  open the <strong>...</strong> menu of Balm and choose <strong>Duplicate</strong>. Make your changes on the copy, preview
  it, and publish it only once it works. Your live theme stays untouched, and you can go back to it at any moment.</p>
</div>

<h2 id="hire-a-partner">Get help from a Shopify Partner</h2>
<p>Code customizations are outside the scope of Balm support. For custom features, design changes or integrations, we
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
<p>When you update Balm, Shopify installs the new version as a separate copy and carries over your theme editor settings
and content, but not the changes you made in the theme files. Keep a list of every file you changed and why, so the
changes can be applied again to the new version.</p>

<h2 id="support-scope">What support covers</h2>
<p>Balm support covers the theme as shipped. When a problem shows up on a theme whose code was modified, we may ask you
to reproduce it on an unmodified copy of Balm first. See <a href="support.html">Support</a>.</p>
'''

# ------------------------------------------------------------------ FAQ
FAQ_LEAD = 'Answers to the questions merchants ask most about Balm.'

FAQ = [
    ('Can I use Balm on more than one store?', '''
<p>A theme bought from the Shopify Theme Store is licensed for one store. To use Balm on another store, buy it again
from that store. Trying the theme is free on any store.</p>'''),
    ('How do I update Balm without losing my settings?', '''
<p>When an update is available, your theme library shows a notice. Shopify adds the new version as a separate copy that
keeps your theme editor settings and content. Preview it, then publish it. Changes you made in the theme code are not
carried over; see <a href="custom-code.html#updates-and-code">Custom code</a>.</p>'''),
    ('How do I make the header transparent over my hero?', '''
<ol>
  <li>In the Header section, check <strong>Transparent header over the first section</strong>, and pick a
  <strong>Transparent header color scheme</strong> with light text if your hero is dark.</li>
  <li>Make sure the first section of the page is a Hero, Slideshow, Video, Products showcase or Brand story hero, with
  <strong>Allow transparent header</strong> checked.</li>
</ol>
<p>Upload a light version of your logo in <strong>Logo image (transparent header)</strong> if your normal logo is dark.</p>'''),
    ('Why are there no filters on my collection pages?', '''
<p>Filters come from Shopify's free Search &amp; Discovery app. Install it, add the filters you want (availability,
price, product type, color and so on), then check that <strong>Enable filters</strong> is on in the Collection and
Search sections. A filter only shows when the products of the page have values for it.</p>'''),
    ('How do I set up a mega menu?', '''
<p>Create your main menu in your admin first. Then, in the Header section, add a <strong>Mega menu</strong> block and
type the exact title of a top level menu item in <strong>Linked menu item</strong>, for example <q>Shop</q>. Add Link
column, Image, Products, Promo or Banner blocks inside it. The panel opens when a shopper hovers that item. See
<a href="sections.html#mega-menu-blocks">Mega menu blocks</a>.</p>'''),
    ('How do I give each product its own background color?', '''
<p>Create a product metafield definition named <q>Background color</q> of type Color, connect it to the Background
color setting of the Product section, then fill it on each product. The full walkthrough is on
<a href="metafields.html#per-product-background">Metafields</a>.</p>'''),
    ('Why can I not connect a setting to my metafield?', '''
<p>Three usual causes. The definition does not exist yet: create it in Settings, Custom data first. The type does not
match: a color setting only accepts a Color metafield, an image setting a File metafield. Or the definition was created
for the wrong resource: product page settings need a <strong>Products</strong> definition, other sections a
<strong>Shop</strong> definition. The help text of each connectable setting names the exact definition it expects.</p>'''),
    ('How do I add product reviews and star ratings?', '''
<p>Install a reviews app that writes Shopify's standard review metafields (most do). Balm's Rating block, the ratings on
product cards and quick view read them automatically once reviews come in. If the app offers an app block for its review
list, add it to the product page from the block picker.</p>'''),
    ('How do I add a size guide or ingredients list to product pages?', '''
<p>Create a page with the content in Online Store, Pages. On the product page, add a <strong>Popup</strong> block (a link
that opens a dialog) or a <strong>Collapsible row</strong>, and set <strong>Content comes from</strong> to <strong>A
page</strong>. For content that differs per product, connect the block's Content to a rich text metafield instead.</p>'''),
    ('Can I change the color of the Shop Pay or PayPal buttons?', '''
<p>No theme can. The accelerated checkout buttons are drawn by Shopify with the brand colors of each payment provider.
Balm matches everything Shopify allows: height, corner radius, spacing and the loading placeholder. See
<a href="product-page.html#accelerated-checkout">The accelerated checkout buttons</a>.</p>'''),
    ('How do I show a free shipping progress bar?', '''
<p>Open the Cart drawer section, check <strong>Show the reward progress bar</strong> and type the amount in
<strong>Reward threshold</strong>. The bar only displays progress: create the matching free shipping rate or automatic
discount in your admin, and keep the two amounts the same, or buyers will be promised something checkout does not
apply.</p>'''),
    ('How do I offer pre-orders?', '''
<p>Set the variant to continue selling when out of stock in the product admin. At 0 stock its buttons read Pre-order,
or the label you set in Theme settings, Pre-order. To take a deposit or charge later, use a pre-order app. See
<a href="features.html#pre-order">Pre-order</a>.</p>'''),
    ('How do I translate my store?', '''
<p>Add and publish your languages in Settings, Languages. Balm's own texts are already translated into French, German,
Italian and Spanish. Translate what you typed in the editor with the Translate &amp; Adapt app. See
<a href="features.html#translations">Translations</a>.</p>'''),
    ('The newsletter popup does not appear. What should I check?', '''
<ul>
  <li><strong>Enable popup</strong> is checked in the Newsletter popup section, and the section is on the template you are viewing (by default, the home page only).</li>
  <li>You closed it earlier: it stays hidden for the number of days in <strong>Reappear after</strong>. Test in a private window.</li>
  <li>The <strong>Open delay</strong> has not passed yet.</li>
</ul>'''),
    ('My speed score dropped after I turned on the page loader. Why?', '''
<p>A loader covers the page while it loads, which speed tools measure as a slower page. Set <strong>Page loader</strong>
to <strong>First visit only</strong>, the recommended setting, or turn it off. <strong>Every page</strong> shows it on
each page view and has the largest effect.</p>'''),
]

# ------------------------------------------------------------------ Support
SUPPORT_LEAD = 'Balm support answers questions about the theme and fixes its bugs. Here is what it covers and how to reach it.'

SUPPORT = f'''
<p class="cta"><a class="button" href="{SUPPORT_FORM}" rel="noopener">Contact Balm support</a></p>

<h2 id="covered">What support covers</h2>
<ul>
  <li><strong>Bugs</strong> in the theme as shipped: something that does not work as this documentation describes.</li>
  <li><strong>Questions</strong> about the theme: installing it, its settings, sections, blocks and features, and how to reach a result with them.</li>
</ul>

<h2 id="not-covered">What support does not cover</h2>
<ul>
  <li><strong>Customizations</strong>: changes to the theme code, new features, custom designs, or code added in Custom Liquid sections, Liquid blocks or Custom CSS. For this work we recommend a <a href="https://www.shopify.com/partners/directory">Shopify Partner</a>.</li>
  <li>Problems caused by edits to the theme files. We may ask you to reproduce the problem on an unmodified copy of Balm.</li>
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
