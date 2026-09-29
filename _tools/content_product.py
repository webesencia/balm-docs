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
<tr><td>2</td><td>Text</td><td>A short tagline under the title, read from the product's <code>custom.tagline</code> metafield. Nothing shows on a product without it.</td></tr>
<tr><td>3</td><td>Popup</td><td>A small Specifications link that opens a dialog, for ingredients, sizing or nutrition, shown once it has content.</td></tr>
<tr><td>4</td><td>Price</td><td>Price, compare-at price and unit price.</td></tr>
<tr><td>5</td><td>Variant picker</td><td>The options the customer chooses from.</td></tr>
<tr><td>6</td><td>Quantity</td><td>Quantity selector, with any per order limits you have set.</td></tr>
<tr><td>7</td><td>Volume pricing</td><td>Quantity break pricing, shown only when the variant has price breaks.</td></tr>
<tr><td>8</td><td>Purchase options</td><td>Subscription or delivery options, shown only when the product has selling plans.</td></tr>
<tr><td>9</td><td>Gift card recipient</td><td>Recipient name, email and message, shown only on gift card products.</td></tr>
<tr><td>10</td><td>Buy buttons</td><td>Add to cart and the accelerated checkout buttons, hidden while the selected variant is sold out. A variant that keeps selling at 0 stock says Pre-order instead and keeps both.</td></tr>
<tr><td>11</td><td>Back in stock</td><td>A Notify me when available form, shown only when the selected variant is sold out.</td></tr>
<tr><td>12</td><td>Pickup availability</td><td>Local pickup for the selected variant, shown only when a location offers it.</td></tr>
<tr><td>13</td><td>Payment icons</td><td>A secure checkout line with your store's payment icons.</td></tr>
<tr><td>14</td><td>Product upsell</td><td>Frequently bought together, picked automatically.</td></tr>
<tr><td>15</td><td>Icon list</td><td>Three short reassurance claims with icons, each shown once it has a heading or a text.</td></tr>
<tr><td>16</td><td>Description</td><td>The product description from the product admin page.</td></tr>
<tr><td>17</td><td>Collapsible row</td><td>Details, a closed accordion row, shown once it has content.</td></tr>
<tr><td>18</td><td>Collapsible row</td><td>Shipping and returns, a closed accordion row, shown once it has content.</td></tr>
<tr><td>19</td><td>Product navigation</td><td>Previous and next links to the neighboring products.</td></tr>
</tbody></table></div>
<p>Blocks marked <em>shown only when</em> render nothing on products that do not need them, so the page stays short even
though the stack is long. The template carries no example text: a block whose text is empty shows nothing on the
storefront, not even its spacing, and a dimmed example in the theme editor. Below the section, the template also places <a href="sections.html#s-product-recommendations">Product
recommendations</a> and a <a href="sections.html#s-sticky-atc">Sticky add to cart</a> bar.</p>
<p>The Product section is the main section of the product template, so it is not offered in <strong>Add
section</strong>. Preview versions of Balm offered a second version there, Balm spotlight; it has been removed. What set
it apart is now available on the standard page: a <a href="#bg-product-gradient">Product gradient</a> background and
the <a href="#pb-product-spin-badge">Spinning badge</a> block, placed on the gallery or next to the title.</p>

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
section settings, with six modes: <em>None (use the color scheme)</em>, <em>Solid color</em>, <em>Gradient (two
colors)</em>, <em>Image</em>, <em>Radial halo</em> and <em>Product gradient (metafields)</em>. The template default is
<em>None (use the color scheme)</em>. The three combinations below are ready to copy, and the fourth,
<a href="#bg-product-gradient">Product gradient</a>, gives every product its own colors with nothing to connect.</p>
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
on <a href="metafields.html#per-product-background">Metafields</a>. For a gradient, the Product gradient mode below
does it without any connection.</p>
<h3 id="bg-product-gradient">D. Product gradient</h3>
<p>Each product paints its own gradient from two Color metafields, read directly: <code>custom.background_color</code>
for the start and <code>custom.background_color_end</code> for the end. There is nothing to connect in the theme editor:
create the two definitions once (see <a href="metafields.html#showcase">Metafields</a>), fill them on each product, and
choose the mode.</p>
<div class="table-wrap"><table class="plain"><thead><tr><th scope="col">Setting</th><th scope="col">Value</th></tr></thead><tbody>
<tr><td>Background mode</td><td>Product gradient (metafields)</td></tr>
<tr><td>Gradient direction</td><td><code>180</code> (top to bottom), or the angle you want</td></tr>
</tbody></table></div>
<ul>
  <li><strong>Both colors filled</strong>: the gradient runs from the first to the second, in the direction set.</li>
  <li><strong>One color filled</strong>: the section is that one color.</li>
  <li><strong>Neither</strong>: the background of the section's color scheme, as in None. <strong>Fallback background color</strong> plays no part in this mode.</li>
</ul>
<p>The Sticky add to cart bar takes the end color as its accent, as in the Gradient mode. The Products showcase
spotlights read the same two metafields, and Featured set the first one, so a product keeps its colors from the home
page to its own page.</p>
<h3 id="bg-under-header">Extend the gradient under the header</h3>
<p>Over a hero, a transparent header lets the image run to the top of the screen. The product page can do the same with
its gradient. The setting is <strong>Extend the background under the header</strong>, shown in the Product gradient
mode, off by default. It needs two conditions:</p>
<ul>
  <li>the Header section has <strong>Transparent header over the first section</strong> turned on;</li>
  <li>the Product section is the first section of the product template, as it is in the template Balm ships.</li>
</ul>
<p>The gradient then starts at the top of the screen, under the header and under a Floating or Glass announcement bar. A
Solid announcement bar in full width keeps its place above it. The header is transparent at rest and materializes on
scroll, as it does over a hero. The product content and the breadcrumbs stay clear of it: the section adds the height
of the header to its top padding. Without either condition, the setting has no effect.</p>
<p><strong>Header colors at rest</strong> picks the colors of the transparent header over the gradient:</p>
<ul>
  <li><strong>Standard colors</strong>, the default: the header color scheme and the main logo. The right choice for a light gradient.</li>
  <li><strong>Transparent header colors</strong>: the colors the header wears over a transparent hero, with the <strong>Logo image (transparent header)</strong> when you have uploaded one, for a dark gradient. The text takes the <strong>Transparent header color scheme</strong> when <strong>Use different colors while transparent</strong> is ticked in the Header. See the <a href="sections.html#s-header-transparent-colors">white header example</a>.</li>
</ul>
<p>A floating announcement bar set to follow the transparent header colors follows them here too.</p>

<h2 id="sticky-columns">Sticky columns</h2>
<p><strong>Sticky columns (desktop)</strong>, in the Layout group of the Product section, is on by default. From 768 px
wide, the shorter of the two columns, the gallery or the product information, stays in view under the header while
the other one scrolls, and the end of the section releases it. A column taller than the screen scrolls until its bottom
shows, then holds. On phones the columns stack and nothing is sticky. The setting was named Sticky product info in
preview versions, when only the information column could hold.</p>

<h2 id="text-behind-cutouts">Text behind cutout images</h2>
<p>The Product section can print a large decorative text behind the cutout images of its gallery: PNG and WebP images,
whose transparent areas let the text show through. JPG images, videos and 3D models stay as they are. The theme knows a
cutout by its file format only, so a PNG without transparency also gets the text, hidden behind its opaque pixels. The
settings are in the <strong>Text behind cutouts</strong> group, off by default.</p>
<ol class="steps">
  <li>Check <strong>Show on desktop</strong>, <strong>Show on mobile</strong>, or both. Desktop starts at 768 px wide.</li>
  <li>Choose the <strong>Text</strong>: <strong>Product title</strong> (the default), <strong>Product tagline (custom.tagline)</strong>, read from the product's metafield, or <strong>Custom text</strong>, the same on every product. A product whose tagline is empty shows no text.</li>
  <li>Set <strong>Apply to</strong>: <strong>First image only</strong> (the default) shows the text when the first media of the gallery is a PNG or WebP image; <strong>All cutout images</strong> puts it behind every one.</li>
  <li>Style it: <strong>Font</strong> (heading or body font), <strong>Font weight</strong> (Bold by default), <strong>Text case</strong> (UPPERCASE by default), <strong>Text size</strong> (160 px on desktop, 80 px on mobile) and the <strong>Vertical position</strong> and <strong>Horizontal position</strong> of each device (centered by default).</li>
  <li>Pick the <strong>Text color</strong>: <strong>Color scheme text</strong>, <strong>Gradient end color (custom.background_color_end)</strong>, which falls back to the scheme text on a product without the metafield, or a <strong>Custom color</strong>. <strong>Text opacity</strong>, 15% by default, keeps it in the background.</li>
</ol>
<p>The text stays inside the image's frame. A word wider than the image is never split: it runs past the side the
alignment leaves free and is cut at the edge of the image. The text is hidden from screen readers and never catches a
click, so the zoom and the arrows work as usual. With the Product gradient background and the gradient end color,
each product's packshot stands on a text in a color of its own gradient.</p>

<h2 id="accelerated-checkout">The accelerated checkout buttons</h2>
<p>With <strong>Dynamic checkout buttons</strong> on, the wallet buttons (Shop Pay, PayPal, Google Pay, Apple Pay) show
under Add to cart. Which ones appear depends on the payment methods your store has enabled and on the visitor's browser,
so the row differs from one shopper to the next.</p>
<p>The row follows the selected variant: it is hidden while that variant is sold out or unavailable and comes back as
soon as a variant that can be bought is chosen. A pre-order variant can be bought, so it keeps the row. Quick view and
the sticky add to cart bar have no accelerated checkout buttons.</p>
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
                          'connect to, and the <a href="#bg-product-gradient">Product gradient</a> that reads them '
                          'directly), product vignette, bottom curve, layout (<a href="#sticky-columns">sticky columns</a> '
                          'and one collapsible row open at a time), gallery, badges on media, packshot captions, '
                          '<a href="#text-behind-cutouts">text behind cutouts</a>, video and 3D, spacing and breadcrumbs. '
                          'The spacing between collapsible rows is set on each row. Select the section in the editor, '
                          'above its blocks, to see them.</p>')

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
    '_product-liquid',
]

BLOCK_TEXT = {
    '_product-title': '<p>The product title, the main heading of the page. Keep one Title block on H1; any extra title block should use a subheading level.</p>',
    '_product-vendor': '<p>The brand or maker name, from the product admin page.</p>',
    '_product-price': '<p>The price, the compare-at price, the unit price and an optional taxes and shipping note. It follows the selected variant.</p>',
    '_product-sku': '<p>The SKU of the selected variant, with an optional prefix.</p>',
    '_product-rating': '<p>Stars, the numeric value and the review count, read from the standard <code>reviews.rating</code> and <code>reviews.rating_count</code> metafields that review apps fill. It renders nothing until an app fills them.</p>',
    '_product-text': '<p>A free rich text paragraph, the same on every product, or with <strong>Source</strong> set to <strong>Tagline</strong>, the product\'s own <code>custom.tagline</code> metafield, read directly. Empty, it shows nothing on the storefront.</p>',
    '_product-variant-picker': '<p>The options the customer chooses from, in one of six styles (see <a href="#variant-picker-styles">Variant picker styles</a>). It handles products with many variants, combined listings and unavailable combinations.</p>',
    '_product-quantity': '<p>The quantity selector. It respects the minimum, maximum and increment of quantity rules set in B2B catalogs.</p>',
    '_product-volume-pricing': '<p>Quantity price breaks, as a table or a list. It renders nothing when the variant has none.</p>',
    '_product-selling-plans': '<p>One-time purchase and subscription options from your subscription app, with the plan names, descriptions and savings. It renders nothing unless the product has a selling plan.</p>',
    '_product-gift-card-recipient': '<p>Lets the buyer send a gift card to someone else, with a name, an email, a message and a send date. It only renders on gift card products.</p>',
    '_product-buy-buttons': '<p>Add to cart, the accelerated checkout buttons and the Shop Pay Installments banner. The accelerated checkout buttons (Buy it now and the wallets) are hidden while the selected variant is sold out and come back with a variant in stock; a pre-order variant can be bought, so it keeps them, and its button reads Pre-order. See <a href="#buy-button-styles">Buy button styles</a>, <a href="#accelerated-checkout">accelerated checkout</a> and <a href="features.html#pre-order">Pre-order</a>.</p>',
    '_product-inventory': '<p>In stock, low stock or out of stock for the selected variant, with a colored dot and an optional exact quantity. Low stock only applies when inventory is tracked and the variant stops selling at zero.</p>',
    '_product-notify-me': '<p>A back in stock form, shown only while the selected variant is sold out. Requests arrive as contact form messages, at the store address set in Settings, Notifications, and name the exact variant; no app is needed.</p>',
    '_product-pickup': '<p>Local pickup availability for the selected variant, and a button that opens the list of locations. It renders nothing unless a location has pickup enabled.</p>',
    '_product-payment-icons': '<p>A reassurance line and the icons of the payment methods enabled in your store (Settings, Payments). A theme cannot add or reorder these icons; to show another badge, upload it as the block image.</p>',
    '_product-upsell': '''<p>Frequently bought together: products to buy alongside this one, from Shopify recommendations or your own selection. <strong>Bundle (tick boxes, one total)</strong> adds every ticked product in one action; <strong>Simple list (add one by one)</strong> gives each product its own button.</p>
<p>The block takes the look of the product cards. <strong>Card style</strong> is <strong>Card</strong> (filled with the secondary background of the color scheme), <strong>Bordered</strong> (a fine outline, the default) or <strong>Plain</strong> (no box), with the corner radius of the cards set in <a href="theme-settings.html#ts-corner-style">Theme settings, Corner style</a>. Thumbnails are square and never cropped, with their own size on desktop (72 px) and on mobile (64 px). In the bundle list, each row shows a checkbox, the thumbnail, the title and the price, with a quiet variant menu underneath for products with options, and a thin rule between rows; a Total line and a full width button close the block. <strong>Button style</strong> is Solid or Glass, separate from the card style.</p>''',
    '_product-complementary': '<p>A small grid of product cards: complementary products from Shopify recommendations, curated in the Search &amp; Discovery app, or your own selection, which can be connected to a product list metafield.</p>',
    '_product-description': '<p>The product description from the product admin page.</p>',
    '_product-collapsible-row': '''<p>An accordion row whose content is rich text, which can be connected to a metafield, or a page, to share one policy page across every product. A row without heading or content shows nothing on the storefront.</p>
<p><strong>Style</strong> is <strong>Lines</strong> (the default: heading on the left, icon on the right, thin rules and no frame), <strong>Boxed</strong> (a framed row) or <strong>Filled</strong> (the secondary background of the color scheme). <strong>Open and close icon</strong> is a Chevron that turns over, or a Plus that becomes a minus. The heading has its alignment, its size on desktop and on mobile, and its weight; <strong>Inner padding</strong> and <strong>Space between rows</strong> are set per device too. Space between rows only shows with Boxed and Filled: stacked Lines rows share one rule between them. Set the style on each row, and give the rows of one stack the same values.</p>
<p><strong>Open by default</strong> opens the row when the page loads: check it on the first row to show its content at once. To let only one row stay open, turn on <strong>One collapsible row open at a time</strong> in the Product section. Rows open with a short animation where the browser supports it, and at once for visitors who ask for reduced motion.</p>''',
    '_product-popup': '<p>A link or button that opens a dialog with rich text or a page. The Under-title link style sits right below the product title. Without content, it shows nothing on the storefront.</p>',
    '_product-specs': '<p>A label and value table built from Specification blocks, with lines, dots or zebra stripes between rows.</p>',
    '_product-spec-row': '<p>One row of the Specifications block. Both the label and the value can be connected to product metafields.</p>',
    '_product-icon-list': '<p>Reassurance claims built from Icon item blocks, stacked, side by side, or on one row with a button. <strong>Icon stroke</strong> (Light, Regular, Medium or Bold) sets the line weight of the built in icons; your own images keep theirs. <strong>Title weight</strong> and <strong>Body text weight</strong> set the weight of the two lines of text, and <strong>Alignment (desktop)</strong> and <strong>Alignment (mobile)</strong> place each claim, icon and text together, on the left, in the center or on the right of its column. Icon sizes, text sizes and gaps have a desktop and a mobile value.</p>',
    '_product-icon-item': '<p>One claim of the Icon list: a built in glyph or your own image, a heading and a text.</p>',
    '_product-image': '<p>An image inside the information column, with an optional caption. Connect it to a metafield to show a different image per product.</p>',
    '_product-badge': '<p><strong>Automatic (Sale, Sold out, New, Custom)</strong>, the default, shows the same badges as the product cards, styled in Theme settings, Product badges, and nothing when none applies. Sale and Sold out follow the selected variant, and the Custom badge wears the product\'s own colors when its <code>custom.badge_color</code> or <code>custom.badge_text_color</code> metafield is filled (see <a href="features.html#custom-badge-colors">badge colors</a>). <strong>Image</strong> places your own artwork in a corner of the product area.</p>',
    '_product-spin-badge': '''<p>The product's <code>custom.badge_label</code> text turning around a ring. The ring has no text field of its own: each product says its own words through the metafield, and a product without it shows no ring. In the theme editor, an example stands in.</p>
<p><strong>Position (desktop)</strong> and <strong>Position (mobile)</strong> place the ring on a corner of the gallery (top left, top right, bottom left, bottom right) or <strong>Next to the title</strong>, on the title's row. Desktop starts at 768 px wide, and the ring moves when the screen crosses that width. Next to the title needs a Title block; without one, the ring shows where the Spinning badge block sits. <strong>Place behind the product</strong> slides the ring behind the product image, which cuts into it, on the gallery positions only. Size and offsets are set per device. The rotation stops for visitors who ask for reduced motion.</p>''',
    '_product-share': '<p>Share links for X, Facebook and Pinterest, and a copy link button.</p>',
    '_product-nav': '<p>Links to the previous and next product of a collection (the product\'s first collection by default). Only the first 50 products of the collection are read.</p>',
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
