INTRO = ('Every section Balm offers, with where it can be used, what it does, a typical use and its full list of '
         'settings. Add a section from the theme editor with <strong>Add section</strong>; drag it to reorder it. '
         'Settings tables are folded: open one to see every label, its values and its default.')

SHARED = '''
<h2 id="shared-settings">Settings most sections share</h2>
<p>A handful of settings come back in almost every section. They work the same way everywhere, so they are explained
once here.</p>

<section class="entry" id="color-scheme-entry">
<h3 id="color-scheme">Color scheme</h3>
<p>Picks one of the schemes defined in <a href="theme-settings.html#ts-colors">Theme settings, Colors</a>. The scheme
paints the section background, its text and its buttons.</p>
</section>

<section class="entry" id="section-background-entry">
<h3 id="section-background">Section background</h3>
<p>Most sections can paint their own background on top of the color scheme. <strong>Background mode</strong> offers
five choices, and the settings of the mode you pick appear right below it:</p>
<ul>
  <li><strong>None (use the color scheme)</strong>: the default. The scheme background shows, like everywhere else.</li>
  <li><strong>Solid color</strong>: one <strong>Background color</strong>.</li>
  <li><strong>Gradient (two colors)</strong>: <strong>Gradient start</strong>, <strong>Gradient end</strong> and
  <strong>Gradient angle</strong>.</li>
  <li><strong>Image</strong>: a <strong>Background image</strong> with an optional <strong>Overlay color</strong> and
  <strong>Overlay opacity</strong> to keep text readable.</li>
  <li><strong>Radial halo</strong>: a <strong>Halo color</strong> glowing from one corner over a <strong>Base color</strong>,
  with <strong>Halo position</strong>, <strong>Halo size (desktop)</strong>, <strong>Halo size (mobile)</strong> and
  <strong>Halo solid area</strong>.</li>
</ul>
<p>The colors and the image can be connected to <strong>shop metafields</strong>, so one value restyles every section
at once. The <strong>Fallback background color</strong> is used when a connected metafield is empty; leave it on None
to fall back to the color scheme, and never connect it to a metafield itself. The keys to create are listed on
<a href="metafields.html#shop-metafields">Metafields</a>. On the product page the same settings connect to
<strong>product</strong> metafields instead, so every product can carry its own background.</p>
</section>

<section class="entry" id="spacing-entry">
<h3 id="spacing">Spacing, desktop and mobile</h3>
<p>Sizes and spacings come in pairs: a label ending in <strong>(desktop)</strong> applies from 768 px wide, one ending
in <strong>(mobile)</strong> applies below. Top and bottom padding set the space inside the section, above and below its
content.</p>
</section>

<section class="entry" id="transparent-header-entry">
<h3 id="transparent-header">Transparent header</h3>
<p>Hero, Slideshow, Video, Products showcase and Brand story hero carry an <strong>Allow transparent header</strong>
setting. When the section is first on the page and the Header section has <strong>Transparent header over the first
section</strong> turned on, the header floats over it, transparent, then materializes on scroll. The extra top padding
settings keep your content clear of the header only while it is transparent. The colors the header wears while
transparent are set in the Header section, see <a href="#s-header-transparent-colors">white logo and white text over a
dark image</a>.</p>
</section>

<section class="entry" id="inner-panel-entry">
<h3 id="inner-panel">Inner panel and text color</h3>
<p>The About page sections and Contact place their content on an inner panel, the layer between the background and the
text: <strong>Solid</strong> uses the color and opacity you set, <strong>Glass</strong> uses the shared glass recipe,
<strong>Hidden</strong> removes it. <strong>Text color</strong> left on None lets the section work out a readable color
from the background and the panel; pick a color only to force one.</p>
</section>

<section class="entry" id="heading-level-entry">
<h3 id="heading-level">Heading level</h3>
<p>Search engines and screen readers expect exactly one main heading (H1) per page. Sections that often open a page
(Hero, FAQ, Contact, Featured set, Store locator, Brand story hero) let you choose <strong>Main heading (H1)</strong>
or a subheading level. The templates that open with one of them already set H1; keep H2 anywhere else. Product,
collection, blog and page templates set their own H1.</p>
</section>

<section class="entry" id="translated-defaults-entry">
<h3 id="translated-defaults">Text left empty</h3>
<p>Many text settings say <em>Leave empty to use the translated default</em>. Left empty, they show a built in text
that is already translated into every language the theme ships (English, French, German, Italian and Spanish). Typing
your own text replaces it in every language, so on a multilingual store either leave these fields empty or translate
your text with the Translate &amp; Adapt app. See <a href="features.html#translations">Translations</a>.</p>
</section>

<section class="entry" id="spam-notice-entry">
<h3 id="spam-notice">Spam protection notice</h3>
<p>Shopify protects the contact and newsletter forms with hCaptcha, which must be disclosed. Balm prints the required
sentence, with its two links, under each form, which removes the hCaptcha badge from the corner of the page. The
<strong>Spam protection notice</strong> settings only change its size, color and alignment.</p>
</section>
'''

CATEGORIES = [
    ('header-and-footer', 'Header and footer',
     '<p>These sections live in the header and footer groups, shared by every page of the store.</p>',
     ['announcement-bar', 'header', 'footer']),
    ('hero-and-storytelling', 'Hero and storytelling',
     '<p>Large visual sections, usually at the top of the home page or of a landing page.</p>',
     ['hero', 'slideshow', 'products-showcase', 'featured-set', 'image-with-text', 'rich-text', 'video', 'marquee',
      'before-after', 'product-lifestyle']),
    ('products-and-collections', 'Products and collections',
     '<p>Sections that show products or collections and let shoppers buy from them.</p>',
     ['featured-collection', 'collection-list', 'lookbook', 'compare-products', 'recently-viewed']),
    ('trust-and-engagement', 'Trust and engagement',
     '<p>Reassurance, social proof and ways to stay in touch.</p>',
     ['multicolumn', 'testimonials', 'logo-list', 'countdown', 'newsletter', 'newsletter-popup', 'socials', 'faq']),
    ('about-page', 'About page',
     '<p>Four sections built for a brand story page. The About template (<code>page.about</code>) opens with them, and '
     'each one can be added to any other page too.</p>',
     ['about-hero', 'about-problem-shift', 'about-feels-off', 'about-community']),
    ('contact-and-stores', 'Contact and stores',
     '<p>Used by the Contact (<code>page.contact</code>) and Store locator (<code>page.find-us</code>) templates.</p>',
     ['contact', 'find-us']),
    ('layout-and-code', 'Layout, code and apps', '', ['divider', 'custom-liquid', 'apps']),
    ('template-sections', 'Template sections',
     '<p>The main section of each template: what a product, collection, cart or blog page shows. Most of them cannot be '
     'removed from their template, but their settings are yours.</p>',
     ['main-product', 'product-recommendations', 'sticky-atc', 'main-collection', 'main-search', 'main-list-collections',
      'main-cart', 'cart-drawer', 'main-blog', 'main-article', 'main-page', 'main-404', 'main-password', 'main-gift-card']),
]

INTERNAL = {'quick-view', 'predictive-search', 'pickup-availability'}

INTERNAL_NOTE = '''
<p class="page-note">Three more sections exist in the theme files without appearing in the section list: Quick view,
Predictive search and Pickup availability. They have no settings; the theme loads them on demand to fill the quick view
modal, the search suggestions and the pickup details. Quick view is configured in
<a href="theme-settings.html#ts-quick-view">Theme settings, Quick view</a>, predictive search in the Header section.</p>
'''

TEXT = {
    'announcement-bar': ('''
<p>A thin bar above the header, made of <strong>Message</strong> blocks. With two messages or more they rotate on
their own, with optional previous and next arrows, and each message can link somewhere. With <strong>Show close
button</strong> on, visitors can dismiss the bar for the rest of their visit.</p>
<p><strong>Scroll behavior</strong> keeps the bar pinned, lets it scroll away with the page, or hides it on the way
down and brings it back on the way up. <strong>Bar layout</strong> set to Floating turns it into a card that matches the
floating header, and <strong>Bar style</strong> set to Glass uses the shared glass recipe.</p>
<p>A floating bar sits over the first section when the header is transparent there. <strong>Use the transparent header
colors on the announcement bar</strong>, off by default and offered with the Floating layout only, then gives it the
header's transparent colors at the top of the page: its text and controls, and the background of a Solid bar. It returns
to its own color scheme together with the header, on scroll or when a menu or the search opens. See the
<a href="#s-header-transparent-colors">white header example</a>.</p>
''', 'Two or three short messages that rotate: a free shipping threshold, a returns promise and a launch announcement that links to the new product.'),

    'header': ('''
<p>The logo, the main menu, predictive search, the account and cart icons, country and language selectors, and an
optional Instagram link. The logo is
an image, or a text wordmark set in the heading font. On phones the menu opens as a sheet under the header or as a
full height drawer.</p>
<p>The header can take three looks. <strong>Materialized surface</strong> is Solid or Glass. <strong>Transparent header
over the first section</strong> lets it float, transparent, over a first section that allows it, then materialize on
scroll; <strong>Logo image (transparent header)</strong> swaps in a light logo while it is transparent.
<strong>Floating header (detached)</strong> pulls it away from the screen edges as a rounded card.</p>
<p>While it is transparent, the header keeps the text color of its own color scheme. To give it other colors over the
first section, tick <strong>Use different colors while transparent</strong>, right under the transparent logo, then pick
a <strong>Transparent header color scheme</strong>. Its text color goes to the menu links and their arrows, underlines
and hover states, the search, account and cart icons, the cart count, the mobile menu button, the text logo and the
keyboard focus ring. The colors go back to the header color scheme exactly when the logo does: on scroll, or when a mega
menu, the search or the mobile menu opens, in the same crossfade, or at once for visitors who ask for reduced motion.
Open panels always keep the normal colors. Nothing switches on its own depending on the image under the header: the
colors are the ones you choose.</p>
<h4 id="s-header-transparent-colors">Example: white logo and white text over a dark image</h4>
<ol class="steps">
  <li>In the first section of the page, for example a Hero with a dark image, turn on <strong>Allow transparent header</strong>.</li>
  <li>In the Header section, turn on <strong>Transparent header over the first section</strong>.</li>
  <li>Upload the white version of your logo in <strong>Logo image (transparent header)</strong>. Your usual logo stays in <strong>Logo image</strong>.</li>
  <li>Tick <strong>Use different colors while transparent</strong> and set <strong>Transparent header color scheme</strong> to a scheme with white text, such as Scheme 2 of the Balm preset (white on near black).</li>
  <li>If a floating announcement bar sits over the same image, tick <strong>Use the transparent header colors on the announcement bar</strong> in the Announcement bar section, so its text turns white with the header.</li>
</ol>
<p>At the top of the page the logo, the menu and the icons are white over the image. On scroll the header materializes
with your usual logo and colors, and the announcement bar returns to its own scheme at the same moment.</p>
<h4 id="s-header-localization">Country and language selectors</h4>
<p><strong>Country and language selectors</strong> adds them to the header: Both (the default), Country/region only,
Language only, or Off. On desktop a globe sits just before the search, account and cart icons, at their size, stroke
and colors, the transparent header colors included. <strong>Selector style</strong> shows the globe alone (Icon only) or
followed by the current language and currency codes, such as EN · USD (Icon and code). A click opens a panel in the
material of the mega menu: a Country/region list that gives each country's currency, with a search field once there
are more than ten countries, and a Language list. The current country and language are checked. The panel hangs under
the header, aligned on the globe. While a transparent header sits at rest over the first section, with no background
drawn, it opens just under the globe instead, and an open panel follows the header as it materializes on scroll. On phones
and tablets the selectors sit at the bottom of the mobile menu, sheet or drawer, as a compact row of buttons that each
open their own list. Choosing a country or a language reloads the same page with it.</p>
<p>A selector shows only when there is a choice to make: the country selector needs at least two countries or regions,
the language selector at least two languages. A store that sells in one country and one language shows neither,
whatever the setting. The Localization block of the footer uses the same form, so both places always offer the same
choices.</p>
<ol class="steps">
  <li>To sell in more countries, go to <strong>Settings &gt; Markets</strong> in your Shopify admin and add the countries
  or regions to a market. Each country shows the currency of its market.</li>
  <li>To offer more languages, go to <strong>Settings &gt; Languages</strong>, add a language, translate your store with
  a translation app, then publish the language.</li>
  <li>Check that each published language is active in the markets where you want to offer it: the selector only lists
  the languages available to the visitor's market.</li>
</ol>
<p>Mega menus are built from blocks. Add a <strong>Mega menu</strong> block, type the exact title of a top level item
of your main menu in <strong>Linked menu item</strong>, then fill the panel with Link column, Image, Products, Promo
and Banner blocks. See <a href="#mega-menu-blocks">Mega menu blocks</a>.</p>
''', 'A header that floats transparent over the home page hero and turns to glass on scroll, with a mega menu under the Shop item: two link columns and four best sellers.'),

    'footer': ('''
<p>The footer is a row of blocks: <strong>Brand / logo</strong>, <strong>Link column</strong> (one of your menus),
<strong>Newsletter</strong>, <strong>Social</strong> (Instagram and the Follow on Shop button), <strong>Text</strong>
and <strong>Localization</strong> (country or currency, and language selectors, shown only when there is more than one
choice). Each block sets its own width and margins for desktop and mobile.</p>
<p>An optional <strong>Top decorative band</strong> draws a curve, a wave, a diagonal or your own image where the footer
meets the section above. The <strong>Copyright bar</strong> at the bottom can take its own color scheme. Newsletter sign
ups are added to your Shopify customers, with the tag you choose.</p>
''', 'Logo and tagline on the left, Shop and Help link columns, a newsletter block, and a localization block for a store that sells in several countries.'),

    'hero': ('''
<p>A full screen image or Shopify hosted video with a title and a button. Desktop and mobile each get their own image
and video, cropped on the focal point you set in the admin. Video playback covers autoplay per device, a sound button,
what happens at the end (loop, stop, or show the cover again), the style and position of the controls, and whether the
cover stays sharp or blurred while the video loads. The cover always paints first, the video fades in over it, and the
controls appear with the video, never before it.</p>
<p>The text block is placed separately on desktop and mobile, with a fine vertical offset, over an optional darkening
overlay. <strong>Height mode</strong> fits the screen, adapts to the content or takes a custom height.</p>
''', 'The first section of the home page: a short muted video of the product in use, a two line title, one Shop now button, and the header transparent over it.'),

    'slideshow': ('''
<p>A carousel of <strong>Slide</strong> blocks. Each slide has its own desktop and mobile image, color scheme and
overlay, a heading and subtext placed in one of nine positions, and up to two buttons in Solid, Outline or Glass style.
Slides change on their own or on demand, with a slide or fade transition, arrows and dots.</p>
''', 'Two to four campaigns at the top of the home page: a new product, a seasonal collection and a bundle offer.'),

    'products-showcase': ('''
<p>Full screen product <strong>Spotlight</strong> blocks that take over the screen one after another. On desktop a
scroll pinned wipe reveals the next product as the visitor scrolls, progressively or with a snap and a pause; phones get
the same animation with a layout of their own, or a simple vertical stack. When animations are off, or the visitor asks
for reduced motion, spotlights stack. The animation library loads only when the section comes near the screen.</p>
<p>Pick a <strong>Product</strong> and the spotlight fills itself: the product's title as the name, linked to its
page, its <code>custom.tagline</code> metafield as the tagline, its <code>custom.background_color</code> and
<code>custom.background_color_end</code> metafields as the background gradient, and its main image.
<strong>Show the price</strong> adds the price under the tagline. The button opens the product page; with
<strong>Action</strong> set to Add to cart, a product with a single variant goes to the cart in one click and the cart
drawer opens, while a product with options, or sold out, keeps the link to its page. The metafields are read directly:
there is nothing to connect. See <a href="metafields.html#showcase">Metafields</a>.</p>
<p>Each field of the <strong>Override (optional)</strong> group replaces one of those values: name, tagline, background
color, background color end, image and link. Leave a field empty to use the product's value. Without a product, the
override fields are the spotlight's content. A background that neither the override nor the product colors takes the
background of the section's <strong>Color scheme</strong>; a start color without an end color gives a single color.</p>
<p>Each spotlight also carries highlights (a title and up to four claims with icons), an optional featured set
cartouche and a watermark. Section settings share the ingredients, the size subtitle, the spinning badge, the color
scheme and the image sizing across every spotlight, and can hide the header while the section holds the screen.</p>
''', 'Presenting a small range, three to five products, one by one on the home page or on the Products page template: pick each product once, and its metafields keep the spotlight in step with the catalog.'),

    'featured-set': ('''
<p>One product, usually a bundle or a discovery set, presented as a full width banner: a heading, a tagline in two
parts and an add to cart button. Pick the <strong>Product</strong> and the section fills itself: its title as the
heading, its <code>custom.tagline</code> metafield as the tagline, its <code>custom.background_color</code> metafield as
the background, and its image. Each field of the <strong>Override (optional)</strong> group replaces one of those
values; a background that neither gives takes the color scheme's. Your own desktop and mobile background images
replace the product image, darkened by an optional overlay. Until a product is picked, the section shows a placeholder
in the editor and nothing on the storefront.</p>
''', 'Promoting a discovery set at the top of the Products page template (page.products), which opens with this section.'),

    'image-with-text': ('''
<p>An image beside a content column you build from <a href="#theme-blocks">theme blocks</a>: headings, text, buttons,
images, spacers and custom Liquid. Choose the image side on desktop, the order on mobile, the image width and ratio,
and the gap. <strong>Translucent card (glass)</strong> lets the content card overlap the image on desktop.</p>
''', 'Telling the brand story or explaining one product benefit, with a photo, a heading, two short paragraphs and a button.'),

    'rich-text': ('''
<p>A single column of <a href="#theme-blocks">theme blocks</a> (headings, text, buttons, images, spacers, custom
Liquid) in a narrow, normal or wide measure, aligned separately on desktop and mobile. <strong>Background</strong> set
to Transparent lets the section sit on the page without its own fill.</p>
''', 'A brand statement between two visual sections, or an introduction paragraph at the top of a landing page.'),

    'video': ('''
<p>A video from Shopify (uploaded in the admin) or from YouTube or Vimeo, with its own mobile source. External videos
load as a click to play cover: nothing from the third party loads before the click. Shopify videos can instead play
muted on a loop with no controls. Choose the aspect ratio, full width or a maximum width, and an optional heading.</p>
''', 'A one minute brand film on the About page, or a muted loop of the product being prepared on the home page.'),

    'marquee': ('''
<p>A band of text that scrolls across the screen. Type one message per line; the separator you pick (a dot, a dash,
your own text or a small image) is inserted between them automatically. Set the speed, the direction and the height,
and keep the pause button on: accessibility guidelines ask for one on any animation that runs by itself.</p>
''', 'Short claims between two sections, such as Free delivery from 40 euros, Vegan, Made in France.'),

    'before-after': ('''
<p>Two images stacked on top of each other with a handle the visitor drags to compare them, horizontally or vertically.
Add labels, a starting position, a round handle or a plain line, a heading and text. The handle also works from the
keyboard, through a slider.</p>
''', 'Showing the result of a product: a surface before and after cleaning, skin before and after four weeks, a room before and after.'),

    'product-lifestyle': ('''
<p>Two photos side by side that form one rounded card, stacked on phones. Set the gap, the corner radius and the photo
ratio for desktop and mobile, and describe each photo with its own alt text.</p>
''', 'Lifestyle photography between product sections: the product on a breakfast table next to a close up of its texture.'),

    'featured-collection': ('''
<p>A grid of products from one collection, with the full product card: second image on hover, quick add, quick view,
badges, vendor and a button. <strong>Promo tile</strong> blocks take the place of a card at the position you choose, and
a <strong>View all</strong> button can link to the collection.</p>
''', 'Best sellers on the home page: four products, quick add on, a promo tile in third position and a View all button.'),

    'collection-list': ('''
<p>Cards for the collections you pick with <strong>Collection</strong> blocks, with their image, title and an optional
product count. Set the columns, the gap, the image ratio and fit.</p>
''', 'A Shop by category row on the home page with three or four collections.'),

    'lookbook': ('''
<p>An image with <strong>Hotspot</strong> blocks. Each hotspot points at a product or shows a text; on desktop it opens
a popover with the product card and its quick add, on a phone a sheet from the bottom of the screen. The Image with
product list layout lines the products up as cards beside the image, and hovering a card lights its hotspot. Hotspots
have separate desktop and mobile positions.</p>
''', 'Shop the look: a styled photo of three products used together, each one clickable and addable to the cart.'),

    'compare-products': ('''
<p>Up to five products side by side. Built in rows show the image, price, availability, vendor and rating; each
<strong>Row</strong> block adds a line read from the product metafield of your choice, by its key, as text, a number
with its unit, or yes and no. <strong>Highlight differences</strong> marks the rows where products differ. On a phone
the label column stays in place while the product columns scroll. See <a href="metafields.html#compare">Metafields,
Compare products rows</a> for an example.</p>
''', 'Comparing the three creams of a range on their key facts: texture, skin type and whether they are fragrance free.'),

    'recently-viewed': ('''
<p>The products the visitor opened most recently, newest first. The list is kept in the visitor's own browser, so it
needs no app and no account; the section takes no space until there is a history. The theme editor shows example
cards instead.</p>
''', 'At the bottom of product pages, with the current product excluded, or on the cart page.'),

    'multicolumn': ('''
<p>A row of <strong>Column</strong> blocks, each with an image (square, landscape, portrait or circle), a heading, text
and a link, plus an optional button for the whole section. On phones the columns stack or become a horizontal slider.</p>
''', 'Three reasons to buy, or How it works in three steps, each with a small illustration.'),

    'testimonials': ('''
<p><strong>Testimonial</strong> blocks with a quote, a star rating, an author, a role or source and an avatar, as a grid
or a horizontal slider. The slider can rotate on its own; it pauses on hover and focus and stops for good once the
visitor takes control. Cards are Solid, Outline or Glass.</p>
''', 'Five short customer quotes in a slider under the product showcase, or press quotes with the name of the publication as the source.'),

    'logo-list': ('''
<p>A row of <strong>Logo</strong> blocks with an optional heading, shown still or scrolling as a marquee. Logos can be
grayscale until hovered and can each link somewhere.</p>
''', 'An As seen in row of press logos, or the retailers that stock your products.'),

    'countdown': ('''
<p>A timer counting down to a date and time in your store's timezone (format <code>YYYY-MM-DD HH:MM</code>), with days,
hours, minutes and seconds you can show or hide and rename. When it reaches zero it shows a message or hides the
section.</p>
''', 'The last days of a sale, or the launch of a limited edition.'),

    'newsletter': ('''
<p>An email sign up band with a heading and subtext, on a solid or glass panel or on no panel at all, over the section
background. Sign ups are added to your Shopify customers with email marketing consent.</p>
''', 'A 10% welcome offer above the footer, over a lifestyle photo.'),

    'newsletter-popup': ('''
<p>An email sign up popup that opens after a delay and comes back after the number of days you set once closed (0
shows it on every visit). The card is Tinted glass, Glass or Solid over a dimmed page. Sign ups are added to your
Shopify customers with the tag <code>newsletter</code>. The home page template includes it; add it to other templates
when you want it there too.</p>
''', 'A welcome offer shown five seconds after arrival, once every 30 days.'),

    'socials': ('''
<p>A title and one button to your social profile, outlined or in glass, on the section color scheme and background.</p>
''', 'An @yourbrand band with a Follow us button, above the footer.'),

    'faq': ('''
<p>A title column beside an accordion of <strong>FAQ item</strong> blocks (a question and a rich text answer), with an
optional subheading and button. Alignment, gaps and row heights are set separately for desktop and mobile. The FAQ
page template (<code>page.faq</code>) opens with it.</p>
''', 'An FAQ page of eight to twelve questions on delivery, returns and ingredients, with a Contact us button under the title.'),

    'about-hero': ('''
<p>The opening section of the About page: a three part italic title, a heading, body text, a button and an image, on
an inner panel over the section background.</p>
''', 'The top of the About page, with the brand promise in the title and the founding story in two short paragraphs.'),

    'about-problem-shift': ('''
<p>Two panels side by side, each with a title, a subtitle and body text, on an inner panel over the section background.</p>
''', 'The problem on the left and how your product changes it on the right.'),

    'about-feels-off': ('''
<p>An interactive checklist of <strong>Check item</strong> blocks that visitors tick, beside a heading, a subheading
and a button. Once items are ticked, the button leads to the link of the first or last ticked item that has one, or to
the button link.</p>
''', 'A Does this sound like you? list of four situations, each linked to the product that answers it.'),

    'about-community': ('''
<p>A background image crossed by a colored band with two large words, a link below the band, and a gallery of
<strong>Element</strong> blocks (images, round or square, optionally linked) that scrolls sideways with arrows.</p>
''', 'Photos from your community or your Instagram at the bottom of the About page.'),

    'contact': ('''
<p>The Shopify contact form in a card, with a heading, a subtitle and a success message. Messages reach the email
address of your store. The Contact page template (<code>page.contact</code>) uses it.</p>
''', 'The Contact page, with a subtitle that gives your response time.'),

    'find-us': ('''
<p>A store locator page over a background photo: two columns of <strong>Stores</strong> and <strong>Online</strong>
lists (rich text, shown as accordions), and a map slot for an app block or a <strong>Custom Liquid</strong> block where
you paste a store locator embed. The Store locator template (<code>page.find-us</code>) uses it.</p>
''', 'A Where to buy page listing your retailers city by city, with the map of a store locator app.'),

    'divider': ('''
<p>A line or an empty space between two sections, with its own height for desktop and mobile, line thickness, width
and opacity.</p>
''', 'A thin line between two sections that share the same background.'),

    'custom-liquid': ('''
<p>Your own Liquid, HTML or app snippet in a section of its own, contained or full width, with the usual color scheme,
background and spacing settings. Read <a href="custom-code.html">Custom code</a> before using it.</p>
''', 'An embed code provided by a third party service that has no app block.'),

    'apps': ('''
<p>A container for app blocks, with a color scheme and spacing, and an option to remove the content width limit so an
app can draw edge to edge.</p>
''', 'Reviews carousel or Instagram feed from an app, placed between two sections of the home page.'),

    'main-product': ('''
<p>The product page: media gallery on one side, a column of blocks on the other. Two versions can be added from the
section picker: <strong>Product</strong>, the standard page, and <strong>Balm spotlight</strong>, a dark page with a
stacked gallery, a radial halo background and a spinning badge.</p>
''', ''),

    'product-recommendations': ('''
<p>Product cards under the product page, filled by Shopify: <strong>Related (similar products)</strong> are generated
automatically, <strong>Complementary (pairs well with)</strong> are the ones you curate in the Search &amp; Discovery
app.</p>
''', 'Four related products under every product page, with the custom badge showing on new formulas.'),

    'sticky-atc': ('''
<p>A bar with the product thumbnail, title, selected variant, price and add to cart button that stays at the top or
bottom of the screen, on desktop and mobile separately. By default it appears once the main buy button scrolls out of
view. A variant that sells as a pre-order says Pre-order here too.</p>
''', 'At the bottom of the screen on phones, where the main buy button quickly scrolls away.'),

    'main-collection': ('''
<p>The collection page: a banner with the title, description and image, an optional row of collection links, filters
and sorting, and the product grid. Filters come from the Search &amp; Discovery app and can sit in a column, a drawer
or a horizontal bar. Pagination is page numbers, a Load more button or infinite scroll. Visitors can change the column
count or switch to a list view when you allow it, and <strong>Promo tile</strong> blocks take the place of a card on
the first page.</p>
''', 'Filters in a column on desktop and a drawer on mobile, 24 products per page with a Load more button, color swatches on the cards.'),

    'main-search': ('''
<p>The search results page, with the same filters, sorting, pagination and product cards as the collection page. What
it searches (products only, or products, articles and pages) is set in
<a href="theme-settings.html#ts-search">Theme settings, Search</a>.</p>
''', 'Filters in a drawer on every device, with infinite scroll.'),

    'main-list-collections': ('''
<p>The page that lists your collections (<code>/collections</code>): every collection alphabetically, or only the ones
you pick, in the order you pick them.</p>
''', 'A curated list of six collections, with the product count on each card.'),

    'main-cart': ('''
<p>The cart page, with quantity rules, an order note, the taxes and shipping note and the accelerated checkout
buttons. It works without JavaScript. Gift wrapping appears here when it is on in Theme settings.</p>
''', 'An order note for delivery instructions and the accelerated checkout buttons under the checkout button.'),

    'cart-drawer': ('''
<p>The panel that slides in when a product is added to the cart. It can show a reward progress bar, suggestions from
Shopify or from your own selection, a promotion note on each line, a shipping notice, the order note, the taxes and
shipping note and the accelerated checkout buttons, on a solid or glass panel.</p>
<p>The reward bar only displays progress toward the amount you type. It does not create free shipping or a discount:
set the real rule in your admin (Settings, Shipping and delivery, or Discounts) and keep the two amounts the same.</p>
''', 'A free shipping bar at 50 in your currency, three complementary suggestions in a carousel and the order note.'),

    'main-blog': ('''
<p>The blog page: article cards with image, date, author, excerpt and tags, an optional row of tag filters, and page
numbers.</p>
''', 'Three columns on desktop, one on mobile, with the tag filter row for recipes and news.'),

    'main-article': ('''
<p>A blog post: featured image, date, author, tags, share buttons, links to the previous and next posts, and comments
when the blog allows them, in a reading column whose width and type sizes you set.</p>
''', 'A reading column of about 700 px with the share buttons and the previous and next links.'),

    'main-page': ('''
<p>A standard page from your admin (Online Store, Pages) in a reading column, with its title and content.</p>
''', 'Legal pages, shipping information and other text pages.'),

    'main-404': ('''
<p>The page shown when a link is broken: a heading, a message, a button home, an optional search bar and a few products
from a collection of your choice.</p>
''', 'A friendly message, the search bar and four best sellers to keep the visitor in the store.'),

    'main-password': ('''
<p>The page visitors see while your store is password protected, with your logo, the password form and a background.
The message above the form is set in Online Store, Preferences.</p>
''', 'A coming soon page before launch.'),

    'main-gift-card': ('''
<p>The page a customer opens from their gift card email, with the card value, the code, a QR code, and buttons to copy
the code, print the page and go to the store.</p>
''', 'Your logo on top, on your main color scheme.'),
}

BLOCK_TEXT = {
    'announcement-bar/message': '<p>One message, with an optional link that makes the whole message clickable.</p>',
    'footer/brand': '<p>Your logo, or the store name when no logo is set, with an optional tagline.</p>',
    'footer/link_column': '<p>A heading and one of your menus.</p>',
    'footer/newsletter': '<p>An email sign up field. Subscribers are added to your customers with the tag you set, which email apps such as Klaviyo or Mailchimp can read.</p>',
    'footer/social': '<p>An Instagram icon and the Follow on Shop button, which Shopify shows only on stores that use the Shop sales channel.</p>',
    'footer/text': '<p>A heading and rich text, for an address or a short note.</p>',
    'footer/localization': '<p>Country or currency, and language selectors. Each appears only when your markets and languages offer more than one choice.</p>',
    'slideshow/slide': '<p>One slide: images, overlay, heading, subtext, content position and up to two buttons.</p>',
    'products-showcase/spotlight': '<p>One product spotlight: the product that fills it, the override fields, the image size and position, the Shop now or Add to cart button, highlights, the featured set cartouche, visibility and watermark.</p>',
    'featured-collection/promo_tile': '<p>A tile that takes the place of a product card at the position you choose, on the first page of the grid only.</p>',
    'main-collection/promo_tile': '<p>A tile that takes the place of a product card at the position you choose, on the first page of the grid only.</p>',
    'collection-list/collection': '<p>One collection card.</p>',
    'lookbook/hotspot': '<p>One point on the image, linked to a product or carrying a text, with its desktop and mobile position.</p>',
    'compare-products/row': '<p>One comparison line read from a product metafield. See <a href="metafields.html#compare">Metafields</a>.</p>',
    'multicolumn/column': '<p>One column: image, heading, text and link.</p>',
    'testimonials/testimonial': '<p>One testimonial card.</p>',
    'logo-list/logo': '<p>One logo, with an optional link.</p>',
    'faq/item': '<p>One question and its answer.</p>',
    'about-feels-off/item': '<p>One line of the checklist, with an optional link the button can take over.</p>',
    'about-community/element': '<p>One image of the gallery, with an optional link and its own shape.</p>',
    'find-us/liquid': '<p>Paste the embed code of a store locator service here.</p>',
}

BLOCKS_INTRO = '<p>Blocks that several sections accept, and the blocks that build the header mega menus.</p>'

THEME_BLOCKS_INTRO = ('<p>General purpose blocks accepted by Image with text, Rich text and the product information '
                      'column. Stack them in any order to build a content column.</p>')

THEME_BLOCK_TEXT = {
    'heading': '<p>A heading. <strong>Heading level (semantic)</strong> sets the level for search engines and screen readers without changing the size.</p>',
    'text': '<p>A rich text paragraph, with an optional maximum width.</p>',
    'button': '<p>A link styled as a Solid, Outline or Glass button, or as a text link.</p>',
    'image': '<p>An image with a ratio, a width, an optional height limit and a corner radius.</p>',
    'spacer': '<p>Empty space, with its own height on desktop and mobile.</p>',
    'liquid': '<p>Your own Liquid or HTML. See <a href="custom-code.html">Custom code</a>.</p>',
}

MEGA_INTRO = ('<p>A mega menu is a panel that opens under a top level item of the main menu. Add a <strong>Mega menu</strong> '
              'block to the Header section, type the exact title of that menu item in <strong>Linked menu item</strong>, '
              'then add the blocks below inside it. On phones the panel becomes an accordion in the mobile menu.</p>')

MEGA_TEXT = {
    '_mega-menu': '<p>The panel itself: which menu item opens it, its grid, width and padding.</p>',
    '_mega-column': '<p>A heading and the links of one of your menus.</p>',
    '_mega-image': '<p>An image with an optional caption and link.</p>',
    '_mega-products': '<p>Two to four products as mini cards with image, title and price. With <strong>Show product tagline</strong> on in the Header section, each card also shows the product\'s <code>custom.tagline</code> metafield.</p>',
    '_mega-promo': '<p>An image tile with a heading, a short text and a link.</p>',
    '_mega-banner': '<p>A wide banner with a background image, a heading, a short text and a button or link.</p>',
}
