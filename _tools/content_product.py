INTRO = ('Undertone ships one product page, and every product uses it. The page wears the colors of the product, '
         'and metafields give each product its own cutout, name lines and texts, so one template serves the whole range.')

BODY_BEFORE = '''
<h2 id="how-it-is-built">How the page is built</h2>
<p>The <strong>Product</strong> section has two sides. The scene shows the product name set large in layers around the
cutout of the product. The scene is also the gallery: the product's other media follow the cutout, over the same name, and shoppers move
through them with a swipe, a mouse drag (the pointer shows a hand over the scene), a trackpad, the arrow keys once the
scene has the focus, or the two small arrows on each side of the counter (01 / 02), at the bottom of the scene, centered under the
product next to the zoom button; the arrows go round from the last media to the first. On phones the next media shows at the edge of the
screen, to say that a swipe goes on. A product with one media shows no counter and no arrows. Choosing a variant
brings its image: in the scene when the variant has its own cutout or no cutout is set, else on the variant's
slide.</p>
<p>The name in the scene follows the settings of <a href="sections.html#large-name">The large name</a>: every line
behind the product by default, or some in front of it with <strong>Default layering</strong>, which leave as another
media slides in; <strong>Name size</strong> and <strong>Scale</strong> set its size.</p>
<p>The column holds the blocks you add, remove and reorder in the theme editor (open <strong>Products</strong> in the page
menu at the top of the editor). The section also accepts app blocks and the general
<a href="more-sections.html#theme-blocks">theme blocks</a>.</p>
<p>The whole page wears the colors of the product (see <a href="index.html#tone-on-tone">Tone on tone</a>), and choosing
a variant that has its own colors recolors it. <strong>Surface</strong> picks the ground of the section, Field by
default. On desktop the scene fills the screen under the header, the product and its name centered in it, and
<strong>Sticky scene (desktop)</strong> keeps it there while the column scrolls, until the end of the section; on phones
the scene sits above the column.</p>
<p>The demo template starts with this stack:</p>
<div class="table-wrap"><table class="plain">
<thead><tr><th scope="col">Order</th><th scope="col">Block</th><th scope="col">What it does on the demo</th></tr></thead>
<tbody>
<tr><td>1</td><td>Breadcrumb</td><td><q>Shop / Night cream</q>: a link to the shop and the product type.</td></tr>
<tr><td>2</td><td>Title</td><td>The product title.</td></tr>
<tr><td>3</td><td>Rating</td><td>The stars, the rating and the number of reviews, when the product has a rating.</td></tr>
<tr><td>4</td><td>Price</td><td>The price, the compare-at price and the unit price.</td></tr>
<tr><td>5</td><td>Text</td><td>The tagline, read from <code>custom.tagline</code>.</td></tr>
<tr><td>6</td><td>Popup</td><td>A Specifications link, shown once it has content.</td></tr>
<tr><td>7</td><td>Variant picker</td><td>The sizes, as words.</td></tr>
<tr><td>8 to 10</td><td>Volume pricing, Purchase options, Gift card recipient</td><td>Shown only on products that need them.</td></tr>
<tr><td>11</td><td>Buy buttons</td><td>Add to bag, with the price in the button.</td></tr>
<tr><td>12</td><td>Specifications</td><td>The passport: Suited to, Skin feel, Key ingredients, Texture, Aroma and Dosage, each connected to a product metafield.</td></tr>
<tr><td>13 to 15</td><td>Collapsible row</td><td>How to use (open), Ingredients, and Delivery and returns.</td></tr>
<tr><td>16</td><td>Reviews</td><td>What customers say: two Review blocks, the one of this product first.</td></tr>
<tr><td>17</td><td>Complementary products</td><td>Works well with: two products from Search and Discovery.</td></tr>
<tr><td>18 and 19</td><td>Back in stock, Pickup availability</td><td>Shown only when the variant is sold out, or when a location offers pickup.</td></tr>
<tr><td>20</td><td>Description</td><td>The product description.</td></tr>
</tbody></table></div>
<p>Payment icons and Product upsell are in the template too, turned off. Below the section the template places the
<a href="section-texture.html">Texture</a> section, a <a href="section-campaign.html">Campaign</a> connected to the
product's story metafields (shown only on the products that have a story image), the
<a href="section-next-product.html">Next product</a> band, just before the footer, and the
<a href="section-sticky-atc.html">Sticky add to cart</a> bar.
A block whose text is empty shows nothing on your store, not even its spacing.</p>

<h2 id="buy-button-styles">Buy button styles</h2>
<p>The <strong>Style</strong> setting of the Buy buttons block is <strong>Solid</strong> (the filled button of the theme,
the default), <strong>Outline</strong> or <strong>Signature</strong>. <strong>Button height</strong> and <strong>Font
weight</strong> are set on the block; the size and the border of every button are set in
<a href="theme-settings.html#ts-buttons">Theme settings, Buttons</a>.</p>
<p><strong>Weld to the packs menu</strong> joins the buy button to the Packs menu variant picker so the two read as one
shape; it needs the Signature style. Turn on <strong>Weld to the buy button</strong> in the Variant picker block too.</p>

<h2 id="variant-picker-styles">Variant picker styles</h2>
<div class="table-wrap"><table class="plain">
<thead><tr><th scope="col">Style</th><th scope="col">Looks like</th></tr></thead>
<tbody>
<tr><td><strong>Buttons (pills)</strong> (default)</td><td>The values side by side, the chosen one marked.</td></tr>
<tr><td><strong>Dropdown menu</strong></td><td>A select menu. Best when a product has many values.</td></tr>
<tr><td><strong>Color swatches</strong></td><td>Color swatches, from the swatches saved on your option values in the admin.</td></tr>
<tr><td><strong>Image swatches</strong></td><td>Small image swatches, from the same swatches.</td></tr>
<tr><td><strong>Signature pill</strong></td><td>Large values in the heading font.</td></tr>
<tr><td><strong>Packs menu</strong></td><td>One control that opens a menu of pack sizes, with a price per option.</td></tr>
</tbody></table></div>
<p>Swatch styles fall back to a word for option values with no swatch saved. <strong>Unavailable option values</strong>
grays out or hides combinations that cannot be bought. Products of a combined listing switch to the sibling product when
a shopper picks one of its values: see <a href="features.html#combined-listings">Combined listings</a>.</p>

<h2 id="under-header">The product under the header</h2>
<p><strong>Extend the background under the header</strong> runs the ground of the section up behind the header, which
stays transparent at the top of the page. It needs <strong>Header behavior</strong> on Transparent at top in the
<a href="section-header.html">Header</a> and the Product section first on the page, as in the demo template. Whatever its
Section width, the Product section keeps its background edge to edge; Section width moves its content only.</p>
<p><strong>Show background illustration</strong> draws an image of your choice behind the scene, with its opacity, its
width and its place set per device.</p>

<h2 id="accelerated-checkout">The accelerated checkout buttons</h2>
<p>With <strong>Dynamic checkout buttons</strong> on, the wallet buttons (Shop Pay, PayPal, Google Pay, Apple Pay) show
under the buy button. Which ones appear depends on the payment methods of your store and on the visitor's browser. The
row is hidden while the selected variant is sold out and comes back with a variant that can be bought; a pre-order
variant keeps it. Quick view and the sticky add to cart bar have no accelerated checkout buttons.</p>
<p>These buttons are drawn by Shopify. Undertone sets what Shopify allows from your buy button:</p>
<div class="table-wrap"><table class="plain"><thead><tr><th scope="col">What</th><th scope="col">Follows</th></tr></thead><tbody>
<tr><td>Height</td><td>Your <strong>Button height</strong>, within Shopify's range of 25 to 55 px</td></tr>
<tr><td>Corners</td><td>Square, like the buy button</td></tr>
<tr><td>Shadow</td><td>None</td></tr>
<tr><td>Loading placeholder</td><td>The colors of the page, instead of Shopify's gray</td></tr>
</tbody></table></div>
<p>No theme can change the brand color, the logo or the label of each button: Shop Pay stays purple and PayPal yellow on
every Shopify store. Because Shopify caps the wallet height at 55 px, a <strong>Button height</strong> above 55 makes the
buy button taller than the wallet row.</p>
'''

SECTION_SETTINGS_INTRO = ('<p>Settings of the Product section itself: surface and background illustration, the scene, '
                          'one collapsible row open at a time, the zoom, the badges on media, video and 3D, spacing '
                          'and breadcrumbs. Select the section in the editor, above its blocks, to see them.</p>')

BLOCKS_INTRO = ('<p>Every block of the product information column, with the name the block picker shows. Settings that '
                'can be connected to a product metafield say so in their notes, with the exact definition to create; the '
                'full list is on <a href="metafields.html">Metafields</a>.</p>')

BLOCK_ORDER = [
    '_product-crumb', '_product-title', '_product-vendor', '_product-price', '_product-sku', '_product-rating', '_product-reviews', '_product-review', '_product-text',
    '_product-variant-picker', '_product-volume-pricing', '_product-selling-plans',
    '_product-gift-card-recipient', '_product-buy-buttons', '_product-inventory', '_product-notify-me',
    '_product-pickup', '_product-payment-icons', '_product-upsell', '_product-complementary', '_product-description',
    '_product-collapsible-row', '_product-popup', '_product-specs', '_product-spec-row', '_product-icon-list',
    '_product-icon-item', '_product-image', '_product-badge', '_product-share', '_product-nav',
    '_product-liquid',
]

BLOCK_TEXT = {
    '_product-title': '<p>The product title, the main heading of the page. Keep one Title block on H1; any extra title block should use a subheading level.</p>',
    '_product-vendor': '<p>The brand or maker name, from the product admin page.</p>',
    '_product-price': '<p>The price, the compare-at price, the unit price and an optional taxes and shipping note. It follows the selected variant.</p>',
    '_product-sku': '<p>The SKU of the selected variant, with an optional prefix.</p>',
    '_product-rating': '<p>Stars, the numeric value and the review count, read from the standard <code>reviews.rating</code> and <code>reviews.rating_count</code> metafields that review apps fill, else from <code>custom.rating</code> and <code>custom.rating_count</code> (see <a href="index.html#ratings">Product ratings</a>). Without either, it shows nothing.</p>',
    '_product-text': '<p>A free rich text paragraph, the same on every product, or with <strong>Source</strong> set to <strong>Tagline (custom.tagline)</strong>, the product\'s own <code>custom.tagline</code> metafield, read directly. Empty, it shows nothing on the storefront.</p>',
    '_product-variant-picker': '<p>The options the customer chooses from, in one of six styles (see <a href="#variant-picker-styles">Variant picker styles</a>). It handles products with many variants, combined listings and unavailable combinations.</p>',
    '_product-volume-pricing': '<p>Quantity price breaks, as a table or a list. It renders nothing when the variant has none.</p>',
    '_product-selling-plans': '<p>One-time purchase and subscription options from your subscription app, with the plan names, descriptions and savings. It renders nothing unless the product has a selling plan.</p>',
    '_product-gift-card-recipient': '<p>Lets the buyer send a gift card to someone else, with a name, an email, a message and a send date. It only renders on gift card products.</p>',
    '_product-buy-buttons': '<p>The quantity selector, Add to cart, the accelerated checkout buttons and the Shop Pay Installments banner. The quantity selector is the only one of the product page: <strong>Quantity selector (desktop)</strong> and <strong>Quantity selector (mobile)</strong> place it Above the buttons (the default), Inline with Add to cart, or Hidden, with its style, size and label; it follows the quantity rules of each variant and volume pricing.</p><p> The accelerated checkout buttons (Buy it now and the wallets) are hidden while the selected variant is sold out and come back with a variant in stock; a pre-order variant can be bought, so it keeps them, and its button reads Pre-order. See <a href="#buy-button-styles">Buy button styles</a>, <a href="#accelerated-checkout">accelerated checkout</a> and <a href="features.html#pre-order">Pre-order</a>.</p>',
    '_product-inventory': '<p>In stock, low stock or out of stock for the selected variant, as one line of words, with the exact quantity if you want it. Low stock only applies when inventory is tracked and the variant stops selling at zero.</p>',
    '_product-notify-me': '<p>A back in stock form, shown only while the selected variant is sold out. Requests arrive as contact form messages, at the store address set in Settings, Notifications, and name the exact variant; no app is needed.</p>',
    '_product-pickup': '<p>Local pickup availability for the selected variant, and a button that opens the list of locations. It renders nothing unless a location has pickup enabled.</p>',
    '_product-payment-icons': '<p>A reassurance line and the icons of the payment methods enabled in your store (Settings, Payments). A theme cannot add or reorder these icons; to show another badge, upload it as the block image.</p>',
    '_product-upsell': '''<p>Products to buy alongside this one, from Shopify recommendations or your own selection, with <strong>Recommendation intent</strong> on Complementary or Related. <strong>Presentation</strong> is <strong>Bundle (tick boxes, one total)</strong>, which adds every ticked product in one action, or <strong>Simple list (add one by one)</strong>, which gives each product its own button. <strong>Layout</strong> sets them as a list or a grid; thumbnails have their own size on desktop and on phones.</p>''',
    '_product-complementary': '<p>A small grid of product cards: complementary products from Shopify recommendations, curated in the Search &amp; Discovery app, or your own selection, which can be connected to a product list metafield.</p>',
    '_product-description': '<p>The product description from the product admin page.</p>',
    '_product-collapsible-row': '''<p>An accordion row whose content is rich text, which can be connected to a metafield, or a page, to share one policy page across every product. A row without heading or content shows nothing on the storefront.</p>
<p><strong>Style</strong> is <strong>Lines</strong> (the default: heading on the left, the icon on the right, thin rules and no frame), <strong>Boxed</strong> (a framed row) or <strong>Filled</strong> (a filled row). <strong>Open and close icon</strong> is a Plus that turns into a cross, or a Chevron that turns over. The heading has its alignment, its size on desktop and on mobile, and its weight; <strong>Inner padding</strong> and <strong>Space between rows (desktop)</strong> and <strong>(mobile)</strong> are set per device too. Space between rows only shows with Boxed and Filled: stacked Lines rows share one rule between them. Set the style on each row, and give the rows of one stack the same values.</p>
<p><strong>Open by default</strong> opens the row when the page loads: check it on the first row to show its content at once. To let only one row stay open, turn on <strong>One collapsible row open at a time</strong> in the Product section. Rows open with a short animation where the browser supports it, and at once for visitors who ask for reduced motion.</p>''',
    '_product-popup': '<p>A link or button that opens a dialog with rich text or a page. The Under-title link style sits right below the product title. Without content, it shows nothing on the storefront.</p>',
    '_product-specs': '<p>A list of labels and values built from Specification blocks, on two columns on desktop and one on phones, as the passport of the demo. <strong>Row separator</strong> draws a line, a dotted line or nothing between the rows.</p>',
    '_product-spec-row': '<p>One row of the Specifications block. Both the label and the value can be connected to product metafields.</p>',
    '_product-icon-list': '<p>Reassurance claims built from Icon item blocks, stacked, side by side, or on one row with a button. <strong>Icon stroke</strong> (Light, Regular, Medium or Bold) sets the line weight of the built in icons; your own images keep theirs. <strong>Heading weight</strong> and <strong>Body text weight</strong> set the weight of the two lines of text, and <strong>Alignment (desktop)</strong> and <strong>Alignment (mobile)</strong> place each claim, icon and text together, on the left, in the center or on the right of its column. Icon sizes, text sizes and gaps have a desktop and a mobile value. <strong>Icon and text gap (desktop)</strong> and <strong>(mobile)</strong> set the space the eye sees between each icon and its text, from the bottom of the icon to the top of the capitals: at 0 the letters touch the icon.</p>',
    '_product-icon-item': '<p>One claim of the Icon list: a built in glyph or your own image, a <strong>Heading</strong> and a <strong>Text</strong>. Heading and Text are rich text fields: press Enter for a new line, or connect a product metafield of type Single line text or Multi-line text with the dynamic source icon, each line of a Multi-line text on its own line. The <strong>Icon image</strong> connects to a File metafield the same way, so each product shows its own claims (see <a href="metafields.html#connect">Connecting a setting to a metafield</a>). An item with neither heading nor text stays hidden on the storefront.</p>',
    '_product-image': '<p>An image inside the information column, with an optional caption. Connect it to a metafield to show a different image per product.</p>',
    '_product-badge': '<p><strong>Badge type</strong> <strong>Automatic (Sale, Sold out, New, Custom)</strong>, the default, shows the same badges as the tiles, set in Theme settings, Product badges, and nothing when none applies; the Custom badge says the product\'s <code>custom.badge_label</code>. <strong>Image</strong> places your own artwork in a corner of the product area.</p>',
    '_product-spin-badge': '''<p>The product's <code>custom.badge_label</code> text turning around a ring. The ring has no text field of its own: each product says its own words through the metafield, and a product without it shows no ring. In the theme editor, an example stands in.</p>
<p><strong>Position (desktop)</strong> and <strong>Position (mobile)</strong> place the ring on a corner of the gallery (top left, top right, bottom left, bottom right) or <strong>Next to the title</strong>, on the title's row. Desktop starts at 768 px wide, and the ring moves when the screen crosses that width. Next to the title needs a Title block; without one, the ring shows where the Spinning badge block sits. <strong>Place behind the product</strong> slides the ring behind the product image, which cuts into it, on the gallery positions only. Size and offsets are set per device. The rotation stops for visitors who ask for reduced motion.</p>''',
    '_product-share': '<p>Share links for X, Facebook and Pinterest, and a copy link button.</p>',
    '_product-nav': '<p>For the Featured product section: <strong>Next label</strong> and the name of the next product, bottom left of its scene, which opens it. On the product page, the <a href="section-next-product.html">Next product</a> band at the foot of the page does this. The next product is the product\'s <code>custom.next_product</code> metafield, else the next one in <strong>Collection</strong>, in <code>custom.primary_collection</code> or in its first collection, from the start again with <strong>Loop around</strong>.</p>',
    '_product-liquid': '<p>Your own Liquid or HTML, or the insertion code of an app that has no app block. See <a href="custom-code.html">Custom code</a>.</p>',
}

BODY_AFTER = '''
<h2 id="second-template">When one product needs a different layout</h2>
<p>Metafields let one template carry different colors, texts and images per product. Some settings cannot be connected
to a metafield: sliders, checkboxes, dropdowns, the color scheme and Liquid code. When a product needs a different value
for one of those, create a second template: in the theme editor, open <strong>Products</strong> in the page menu, choose
<strong>Create template</strong>, base it on the default product template, then assign it to the product from its admin
page, under <strong>Theme template</strong>.</p>

<h2 id="older-templates">Products that used an older template</h2>
<p>Early versions of Undertone shipped extra product templates. They have been folded into the default one. A product still
assigned to one of them falls back to the default product template and renders normally. To clear the setting, open the
product in the admin and choose <strong>Default product</strong> under <strong>Theme template</strong>.</p>
'''


BLOCK_TEXT.pop('_product-spin-badge', None)
BLOCK_TEXT['_product-crumb'] = (
    '<p>A short breadcrumb above the title, for example <q>Shop / Night cream</q>: your <strong>Label</strong> with its '
    '<strong>Link</strong>, then the product type. It replaces the full breadcrumb trail on the product page of the demo.</p>')
BLOCK_TEXT['_product-reviews'] = (
    '<p>Short reviews under the product details, under the heading What customers say: the two quotes typed in the block, '
    'and the <strong>Review</strong> blocks you add inside it. Two Review blocks show: first the one whose '
    '<strong>Product</strong> is the product of the page, then the others in their order, so one template serves every '
    'product. Type only real reviews; a review without its quote is not shown on your store. For reviews collected by an '
    'app, use its app block instead.</p>')
BLOCK_TEXT['_product-review'] = (
    '<p>One review inside the Reviews block: a <strong>Quote</strong>, the <strong>Customer name</strong> and the '
    '<strong>Product</strong> it is about. On that product\'s page it shows first, followed by its '
    '<strong>Detail</strong> (verified buyer on the demo); on the page of another product, the name of its product '
    'takes the place of the Detail, as a link: Inès M., Bordeaux, on Blue Clarity Gel Wash.</p>')
