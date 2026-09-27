INTRO = ('Balm ships one product page, and every product uses it. You shape it from the theme editor, and you can '
         'let each product carry its own colors and texts through metafields, so you never need a second template.')

BODY_BEFORE = '''
<h2 id="how-it-is-built">How the page is built</h2>
<p>The <strong>Product</strong> section is a two column layout: the media gallery on one side, a column of blocks on the
other. Add, remove and reorder the blocks in the theme editor: <strong>Online Store, Themes, Customize</strong>, then pick
<strong>Products</strong> in the page menu at the top. The section also accepts <strong>app blocks</strong>, so any app
that offers a block (reviews, subscriptions, bundles) drops straight into the column, and the general
<a href="sections.html#theme-blocks">theme blocks</a> (Heading, Button, Spacer and the others).</p>
<p>The template, <code>templates/product.json</code>, starts with this stack:</p>
<div class="table-wrap"><table class="plain">
<thead><tr><th scope="col">Order</th><th scope="col">Block</th><th scope="col">What it does</th></tr></thead>
<tbody>
<tr><td>1</td><td>Title</td><td>The product title.</td></tr>
<tr><td>2</td><td>Text</td><td>A short tagline under the title. Rich text, so you can bold or link.</td></tr>
<tr><td>3</td><td>Popup</td><td>A small Specifications link that opens a dialog, for ingredients, sizing or nutrition.</td></tr>
<tr><td>4</td><td>Price</td><td>Price, compare-at price and unit price.</td></tr>
<tr><td>5</td><td>Variant picker</td><td>The options the customer chooses from.</td></tr>
<tr><td>6</td><td>Quantity</td><td>Quantity selector, with any per order limits you have set.</td></tr>
<tr><td>7</td><td>Volume pricing</td><td>Quantity break pricing, shown only when the variant has price breaks.</td></tr>
<tr><td>8</td><td>Purchase options</td><td>Subscription or delivery options, shown only when the product has selling plans.</td></tr>
<tr><td>9</td><td>Gift card recipient</td><td>Recipient name, email and message, shown only on gift card products.</td></tr>
<tr><td>10</td><td>Buy buttons</td><td>Add to cart and the accelerated checkout buttons. A variant that keeps selling at 0 stock says Pre-order instead.</td></tr>
<tr><td>11</td><td>Back in stock</td><td>A Notify me when available form, shown only when the selected variant is sold out.</td></tr>
<tr><td>12</td><td>Pickup availability</td><td>Local pickup for the selected variant, shown only when a location offers it.</td></tr>
<tr><td>13</td><td>Payment icons</td><td>A secure checkout line with your store's payment icons.</td></tr>
<tr><td>14</td><td>Product upsell</td><td>Frequently bought together, picked automatically.</td></tr>
<tr><td>15</td><td>Icon list</td><td>Three short reassurance claims with icons.</td></tr>
<tr><td>16</td><td>Description</td><td>The product description from the product admin page.</td></tr>
<tr><td>17</td><td>Collapsible row</td><td>Details, a closed accordion row.</td></tr>
<tr><td>18</td><td>Collapsible row</td><td>Shipping and returns, a closed accordion row.</td></tr>
<tr><td>19</td><td>Product navigation</td><td>Previous and next links to the neighboring products.</td></tr>
</tbody></table></div>
<p>Blocks marked <em>shown only when</em> render nothing on products that do not need them, so the page stays short even
though the stack is long. Below the section, the template also places <a href="sections.html#s-product-recommendations">Product
recommendations</a> and a <a href="sections.html#s-sticky-atc">Sticky add to cart</a> bar.</p>
<p>The section picker offers a second version of the section, <strong>Balm spotlight</strong>: a dark page with a stacked
gallery, a radial halo background, a spinning badge, a specifications popup, an icon list and three collapsible rows.
Use it as a starting point for a hero product.</p>

<h2 id="buy-button-styles">Buy button styles</h2>
<p>The <strong>Style</strong> setting of the Buy buttons block offers five looks. Each keeps its own
<strong>Corner radius</strong>, <strong>Font weight</strong> and <strong>Letter case</strong> settings, so you can land
anywhere between them.</p>
<div class="table-wrap"><table class="plain">
<thead><tr><th scope="col">Style</th><th scope="col">Looks like</th><th scope="col">Good for</th></tr></thead>
<tbody>
<tr><td><strong>Solid</strong> (default)</td><td>A filled button in your color scheme's button color.</td><td>Most stores. Reads clearly on any background.</td></tr>
<tr><td><strong>Outline</strong></td><td>A bordered button that fills in on hover.</td><td>Quiet, editorial pages where the button should not shout.</td></tr>
<tr><td><strong>Soft</strong></td><td>Filled, generously rounded, lifted by a soft shadow.</td><td>A modern, app like feel.</td></tr>
<tr><td><strong>Signature pill</strong></td><td>An asymmetric italic pill with one square corner.</td><td>A bold, branded look. The only style that can weld to the packs menu.</td></tr>
<tr><td><strong>Glass</strong></td><td>A frosted panel: tinted fill, hairline border, blurred backdrop.</td><td>Pages with a photo, gradient or halo background, where the button should sit in the artwork.</td></tr>
</tbody></table></div>
<p><strong>Welding</strong> joins the buy button to the Packs menu variant picker so the two read as one shape. It needs
the Signature pill style, because the seam depends on its square corner. Turn on <strong>Weld to the buy button</strong>
in the Variant picker block and <strong>Weld to the packs menu</strong> in the Buy buttons block.</p>

<h3 id="glass-style">About the Glass style</h3>
<p>Glass takes its recipe from <a href="theme-settings.html#ts-glass-effect">Theme settings, Glass effect</a>: one tint,
one opacity, one blur and one border opacity, shared by every glass surface. Change it once and the buy button, the
upsell buttons, the popup trigger, the newsletter card and the cart panel move together.</p>
<p>The label keeps the text color of the section's color scheme. Balm measures the contrast between that color and the
frosted surface, and only when it falls below 3:1 (the WCAG floor for large text) does it switch the label to black or
white, whichever reads better. Over a background image or a gradient the backdrop changes from pixel to pixel, so the
theme leaves your scheme color alone there: check the contrast yourself.</p>
<p>Glass is available on the buy button, on the Product upsell buttons (<strong>Button style</strong>, separate from the
card style) and on the Popup trigger.</p>

<h2 id="variant-picker-styles">Variant picker styles</h2>
<div class="table-wrap"><table class="plain">
<thead><tr><th scope="col">Style</th><th scope="col">Looks like</th></tr></thead>
<tbody>
<tr><td><strong>Buttons (pills)</strong> (default)</td><td>Pill shaped option buttons.</td></tr>
<tr><td><strong>Dropdown menu</strong></td><td>A select menu. Best when a product has many values.</td></tr>
<tr><td><strong>Color swatches</strong></td><td>Round color dots, from the swatches saved on your option values in the admin.</td></tr>
<tr><td><strong>Image swatches</strong></td><td>Small image tiles, from the same swatches.</td></tr>
<tr><td><strong>Signature pill</strong></td><td>Large italic pills.</td></tr>
<tr><td><strong>Packs menu</strong></td><td>A single pill that opens a menu of pack sizes, with a price per option.</td></tr>
</tbody></table></div>
<p>Swatch styles fall back to a text pill for option values with no swatch saved. <strong>Unavailable option values</strong>
grays out or hides combinations that cannot be bought. Products that belong to a combined listing switch to the sibling
product when a shopper picks one of its values: see <a href="features.html#combined-listings">Combined listings</a>.</p>

<h2 id="backgrounds">Ready-made backgrounds</h2>
<p>The Product section can paint its own background. The setting is <strong>Background mode</strong>, at the top of the
section settings, with five modes: <em>None (use the color scheme)</em>, <em>Solid color</em>, <em>Gradient (two
colors)</em>, <em>Image</em> and <em>Radial halo</em>. The template default is <em>None (use the color scheme)</em>. The
three combinations below are ready to copy.</p>
<h3 id="bg-soft-gradient">A. Soft gradient</h3>
<p>A near white wash that lifts the packshot without coloring it. These gradient colors are already typed into the
template, so switching the mode is all it takes.</p>
<div class="table-wrap"><table class="plain"><thead><tr><th scope="col">Setting</th><th scope="col">Value</th></tr></thead><tbody>
<tr><td>Background mode</td><td>Gradient (two colors)</td></tr>
<tr><td>Gradient start</td><td><code>#faf8f5</code></td></tr>
<tr><td>Gradient end</td><td><code>#ffffff</code></td></tr>
<tr><td>Gradient direction</td><td><code>180</code></td></tr>
<tr><td>Show bottom curve</td><td>Off</td></tr>
</tbody></table></div>
<h3 id="bg-warm-paper">B. Warm paper</h3>
<p>A single flat color. The calmest option, and the easiest to connect to a metafield so each product carries its own
shade.</p>
<div class="table-wrap"><table class="plain"><thead><tr><th scope="col">Setting</th><th scope="col">Value</th></tr></thead><tbody>
<tr><td>Background mode</td><td>Solid color</td></tr>
<tr><td>Background color</td><td><code>#f4f1ec</code></td></tr>
<tr><td>Show bottom curve</td><td>Off</td></tr>
</tbody></table></div>
<h3 id="bg-radial-halo">C. Radial halo</h3>
<p>A dark halo anchored in one corner over a light base. The most dramatic of the three; use it when the packshot is cut
out on a transparent background.</p>
<div class="table-wrap"><table class="plain"><thead><tr><th scope="col">Setting</th><th scope="col">Value</th></tr></thead><tbody>
<tr><td>Background mode</td><td>Radial halo</td></tr>
<tr><td>Base color</td><td><code>#f4f1ea</code></td></tr>
<tr><td>Halo color</td><td><code>#1a1a1a</code></td></tr>
<tr><td>Halo position</td><td>Top right</td></tr>
<tr><td>Halo size (desktop)</td><td><code>160</code></td></tr>
<tr><td>Halo size (mobile)</td><td><code>130</code></td></tr>
<tr><td>Halo solid area</td><td><code>24</code></td></tr>
<tr><td>Show bottom curve</td><td>On, Curve color <code>#ffffff</code></td></tr>
</tbody></table></div>
<p>To give every product its own background color, connect these colors to product metafields: the step by step guide is
on <a href="metafields.html#per-product-background">Metafields</a>.</p>

<h2 id="accelerated-checkout">The accelerated checkout buttons</h2>
<p>With <strong>Dynamic checkout buttons</strong> on, the wallet buttons (Shop Pay, PayPal, Google Pay, Apple Pay) show
under Add to cart. Which ones appear depends on the payment methods your store has enabled and on the visitor's browser,
so the row differs from one shopper to the next.</p>
<p>These buttons are drawn by Shopify, inside an element no theme and no app can style directly. Shopify exposes a short
list of settings instead, and Balm sets all of them from your Add to cart button:</p>
<div class="table-wrap"><table class="plain"><thead><tr><th scope="col">What</th><th scope="col">Follows</th></tr></thead><tbody>
<tr><td>Height</td><td>Your <strong>Button height</strong> setting, within Shopify's range of 25 to 55 px</td></tr>
<tr><td>Corner radius</td><td>Your <strong>Corner radius</strong> setting, the same value as Add to cart</td></tr>
<tr><td>Shadow</td><td>Removed, so the row stays flat like the buy button</td></tr>
<tr><td>Alignment</td><td>Centered</td></tr>
<tr><td>Space between wallet rows</td><td>Matched to the gap under the buy button</td></tr>
<tr><td>Loading placeholder</td><td>Your color scheme, instead of Shopify's default gray</td></tr>
</tbody></table></div>
<p>No theme can change the brand color of each button, its logo, its label or its font: Shop Pay stays purple and PayPal
yellow on every Shopify store. Because Shopify caps the wallet height at 55 px, a <strong>Button height</strong> above 55
makes Add to cart taller than the wallet row; keep it at 55 or below if you want the two to match. The cart drawer and
the cart page get the same treatment.</p>
'''

SECTION_SETTINGS_INTRO = ('<p>Settings of the Product section itself: background (with the product metafields they '
                          'connect to), product vignette, bottom curve, layout, gallery, packshot captions, video and 3D, '
                          'spacing, collapsible rows and breadcrumbs. Select the section in the editor, above its blocks, to '
                          'see them.</p>')

BLOCKS_INTRO = ('<p>Every block of the product information column, with the name the block picker shows. Settings that '
                'can be connected to a product metafield say so in their notes, with the exact definition to create; the '
                'full list is on <a href="metafields.html">Metafields</a>.</p>')

BLOCK_ORDER = [
    '_product-title', '_product-vendor', '_product-price', '_product-sku', '_product-rating', '_product-text',
    '_product-variant-picker', '_product-quantity', '_product-volume-pricing', '_product-selling-plans',
    '_product-gift-card-recipient', '_product-buy-buttons', '_product-inventory', '_product-notify-me',
    '_product-pickup', '_product-payment-icons', '_product-upsell', '_product-complementary', '_product-description',
    '_product-collapsible-row', '_product-popup', '_product-specs', '_product-spec-row', '_product-icon-list',
    '_product-icon-item', '_product-image', '_product-badge', '_product-spin-badge', '_product-share', '_product-nav',
    '_product-sticky-atc', '_product-liquid',
]

BLOCK_TEXT = {
    '_product-title': '<p>The product title, the main heading of the page. Keep one Title block on H1; any extra title block should use a subheading level.</p>',
    '_product-vendor': '<p>The brand or maker name, from the product admin page.</p>',
    '_product-price': '<p>The price, the compare-at price, the unit price and an optional taxes and shipping note. It follows the selected variant.</p>',
    '_product-sku': '<p>The SKU of the selected variant, with an optional prefix.</p>',
    '_product-rating': '<p>Stars, the numeric value and the review count, read from the standard <code>reviews.rating</code> and <code>reviews.rating_count</code> metafields that review apps fill. It renders nothing until an app fills them.</p>',
    '_product-text': '<p>A free rich text paragraph. Connect it to the <code>custom.tagline</code> metafield to give each product its own tagline.</p>',
    '_product-variant-picker': '<p>The options the customer chooses from, in one of six styles (see <a href="#variant-picker-styles">Variant picker styles</a>). It handles products with many variants, combined listings and unavailable combinations.</p>',
    '_product-quantity': '<p>The quantity selector. It respects the minimum, maximum and increment of quantity rules set in B2B catalogs.</p>',
    '_product-volume-pricing': '<p>Quantity price breaks, as a table or a list. It renders nothing when the variant has none.</p>',
    '_product-selling-plans': '<p>One-time purchase and subscription options from your subscription app, with the plan names, descriptions and savings. It renders nothing unless the product has a selling plan.</p>',
    '_product-gift-card-recipient': '<p>Lets the buyer send a gift card to someone else, with a name, an email, a message and a send date. It only renders on gift card products.</p>',
    '_product-buy-buttons': '<p>Add to cart, the accelerated checkout buttons and the Shop Pay Installments banner. See <a href="#buy-button-styles">Buy button styles</a> and <a href="#accelerated-checkout">accelerated checkout</a>.</p>',
    '_product-inventory': '<p>In stock, low stock or out of stock for the selected variant, with a colored dot and an optional exact quantity. Low stock only applies when inventory is tracked and the variant stops selling at zero.</p>',
    '_product-notify-me': '<p>A back in stock form, shown only while the selected variant is sold out. Requests arrive as contact form messages, at the store address set in Settings, Notifications, and name the exact variant; no app is needed.</p>',
    '_product-pickup': '<p>Local pickup availability for the selected variant, and a button that opens the list of locations. It renders nothing unless a location has pickup enabled.</p>',
    '_product-payment-icons': '<p>A reassurance line and the icons of the payment methods enabled in your store (Settings, Payments). A theme cannot add or reorder these icons; to show another badge, upload it as the block image.</p>',
    '_product-upsell': '<p>Products to buy alongside this one, from Shopify recommendations or your own selection. <strong>Bundle (tick boxes, one total)</strong> adds every ticked product in one action; <strong>Simple list (add one by one)</strong> adds them separately.</p>',
    '_product-complementary': '<p>A small grid of product cards: complementary products from Shopify recommendations, curated in the Search &amp; Discovery app, or your own selection, which can be connected to a product list metafield.</p>',
    '_product-description': '<p>The product description from the product admin page.</p>',
    '_product-collapsible-row': '<p>An accordion row whose content is rich text, which can be connected to a metafield, or a page, to share one policy page across every product. The Product section can keep only one row open at a time.</p>',
    '_product-popup': '<p>A link or button that opens a dialog with rich text or a page. The Under-title link style sits right below the product title.</p>',
    '_product-specs': '<p>A label and value table built from Specification blocks, with lines, dots or zebra stripes between rows.</p>',
    '_product-spec-row': '<p>One row of the Specifications block. Both the label and the value can be connected to product metafields.</p>',
    '_product-icon-list': '<p>Reassurance claims built from Icon item blocks, stacked, side by side, or on one row with a button.</p>',
    '_product-icon-item': '<p>One claim of the Icon list: a built in glyph or your own image, a heading and a text.</p>',
    '_product-image': '<p>An image inside the information column, with an optional caption. Connect it to a metafield to show a different image per product.</p>',
    '_product-badge': '<p><strong>Automatic (Sale, Sold out, New, Custom)</strong> shows the same badges as the product cards, styled in Theme settings, Product badges. <strong>Text</strong> and <strong>Image</strong> place a sticker of your own in a corner of the gallery.</p>',
    '_product-spin-badge': '<p>A round badge with text turning around a ring, placed over a corner of the product image or behind it. The rotation stops for visitors who ask for reduced motion.</p>',
    '_product-share': '<p>Share links for X, Facebook and Pinterest, and a copy link button.</p>',
    '_product-nav': '<p>Links to the previous and next product of a collection (the product\'s first collection by default). Only the first 50 products of the collection are read.</p>',
    '_product-sticky-atc': '<p>The sticky add to cart bar as a block, for a product template that does not use the Sticky add to cart section. Use one or the other, not both.</p>',
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
<p>Early versions of Balm shipped extra product templates. They have been folded into the default one. A product still
assigned to one of them falls back to the default product template and renders normally. To clear the setting, open the
product in the admin and choose <strong>Default product</strong> under <strong>Theme template</strong>.</p>
'''
