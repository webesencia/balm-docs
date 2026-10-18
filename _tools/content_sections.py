INTRO = ('Every section Balm Studio offers, with where it can be used, what it does, a typical use and its full list of '
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
<p>A gradient takes a <strong>Gradient style</strong>: Linear, Radial glow (a halo of the lighter color, placed and
sized by the halo settings) or Aurora (soft fields of the two colors, which
<a href="theme-settings.html#ts-backgrounds">Theme settings, Backgrounds</a> can set in slow motion). An image takes an
optional <strong>Background image (mobile)</strong>, used under 768 px, and each picture shows at its focal point.
<strong>Grain</strong> lays a light texture over any mode; 0 turns it off.</p>
<p>The colors and the image can be connected to <strong>shop metafields</strong>, so one value restyles every section
at once. The <strong>Fallback background color</strong> is used when a connected metafield is empty; leave it on None
to fall back to the color scheme, and never connect it to a metafield itself. The keys to create are listed on
<a href="metafields.html#shop-metafields">Metafields</a>. On the product page the same settings connect to
<strong>product</strong> metafields instead, so every product can carry its own background. The Product section also
has a sixth mode, <strong>Product gradient (metafields)</strong>, which reads each product's colors with nothing to
connect: see <a href="product-page.html#bg-product-gradient">Product gradient</a>.</p>
</section>

<section class="entry" id="spacing-entry">
<h3 id="spacing">Spacing, desktop and mobile</h3>
<p>Sizes and spacings come in pairs: a label ending in <strong>(desktop)</strong> applies from 768 px wide, one ending
in <strong>(mobile)</strong> applies below. Top and bottom padding set the space inside the section, above and below its
content.</p>
<p>Text sizes are the exception: they are fluid. The (mobile) value applies on a screen 390 px wide, the (desktop)
value from 1440 px, and the size moves smoothly in between, then Heading scale or Body scale multiplies it. See
<a href="theme-settings.html#ts-typography">Theme settings, Typography</a>. The announcement bar and the mega menu
switch their text sizes at 1200 px instead, and decorative texts, such as the text behind cutouts of the Product
section, keep a desktop and a mobile size off the scale.</p>
</section>

<section class="entry" id="section-width-entry">
<h3 id="section-width">Section width</h3>
<p>Almost every section has a <strong>Section width</strong> setting, right after its color scheme. It sets how far the
section's background, image or card reaches:</p>
<ul>
  <li><strong>Full width</strong>: from one edge of the screen to the other. Pictures and videos (Image, Image with text,
  Before and after, Video, Slideshow) run edge to edge; text sections keep their text to a readable width inside.</li>
  <li><strong>Full width with margins</strong>: the whole screen less the side margins of the header. The section's
  edges line up with the header's at every width, and with the floating header card when the header floats.</li>
  <li><strong>Page width</strong>: stops at the <strong>Page width</strong> of
  <a href="theme-settings.html#ts-layout">Theme settings, Layout</a>, with its side margin, so the section lines up with
  the product, collection and search pages.</li>
</ul>
<p>The setting replaces the width settings that some sections used to have on their own (Before and after, Image,
Image with text, Lookbook, Custom Liquid, Slideshow, Video and Apps).</p>
</section>

<section class="entry" id="transparent-header-entry">
<h3 id="transparent-header">The header over a section</h3>
<p>With <strong>Header behavior</strong> set to <strong>Transparent at top</strong> (the default) or
<strong>Adaptive</strong> in the Header section, the header can lie over the first section of a page, transparent, in
the colors that suit what is under it. See <a href="#s-header-tone">Automatic header colors</a>.</p>
<ul>
  <li>Hero, Slideshow, Video, Products showcase and Brand story hero carry <strong>Allow transparent header</strong>.
  When the section is first on the page, the header lies over it and starts transparent. The extra top padding settings
  keep your content clear of the header only while it is transparent.</li>
  <li>Many other sections carry <strong>Header over this section</strong>, off by default: Contact, FAQ, Image, Page,
  Rich text, Multicolumn, Routine, Key ingredients, Key figures, Bento, Scroll-revealed text, Featured product, Before
  and after, Collection list, Compare products, Custom Liquid, Logo list, Blog, Blog post, 404, List of collections and
  Collection. Checked on the first section of the template, the section's background (color, gradient or image) runs up
  behind the announcement bar and the header, and its content starts under the header.</li>
  <li>The Product section has neither. In its Product gradient background mode, <strong>Extend the background under the
  header</strong> plays that part: see <a href="product-page.html#bg-under-header">Extend the gradient under the
  header</a>.</li>
</ul>
<p>With Header behavior on Standard, these settings have no effect: the header keeps its card above the page.</p>
</section>

<section class="entry" id="text-colors-entry">
<h3 id="text-colors">Text colors</h3>
<p>Most recent sections have a <strong>Text colors</strong> setting. <strong>Color scheme</strong> keeps the text of
the section's scheme. <strong>Auto</strong> reads the real background of the section (its color, gradient or picture)
and keeps the scheme's text when it reaches a contrast of 4.5:1 there, otherwise switches to white or black, for the
text, icons, lines and buttons. Pick Auto when a section background makes the scheme's text hard to read.</p>
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
<p>Shopify protects the contact and newsletter forms with hCaptcha, which must be disclosed. Balm Studio prints the required
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
     ['hero', 'slideshow', 'products-showcase', 'featured-set', 'image', 'image-with-text', 'rich-text',
      'scroll-text', 'bento', 'video', 'marquee', 'before-after']),
    ('products-and-collections', 'Products and collections',
     '<p>Sections that show products or collections and let shoppers buy from them.</p>',
     ['featured-product', 'featured-collection', 'collection-list', 'routine', 'lookbook', 'compare-products',
      'recently-viewed']),
    ('trust-and-engagement', 'Trust and engagement',
     '<p>Reassurance, proof, social proof and ways to stay in touch.</p>',
     ['key-ingredients', 'key-figures', 'multicolumn', 'testimonials', 'logo-list', 'countdown', 'newsletter',
      'newsletter-popup', 'socials', 'faq']),
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
<p class="page-note">Preview versions of Balm Studio also offered a Lifestyle strip section, two photos side by side in one
rounded card. It has been removed.</p>
'''

TEXT = {
    'announcement-bar': ('''
<p>A thin bar above the header, made of <strong>Message</strong> blocks. With two messages or more they rotate on
their own, with optional previous and next arrows, and each message can link somewhere. With <strong>Show close
button</strong> on, visitors can dismiss the bar for the rest of their visit.</p>
<p><strong>Display</strong> set to <strong>Scroll continuously</strong> runs the messages across the bar in a loop,
like the Marquee section: <strong>Scrolling speed</strong> in pixels per second, <strong>Direction</strong>, a
<strong>Separator</strong> between the messages (Dot, Dash or Custom text), <strong>Pause on hover</strong> and a pause
button for visitors. Keyboard focus on a link stops the band and brings the link into view. Visitors who ask for
reduced motion see the messages standing still, centred, on as many lines as they need. It works in every layout and
style of the bar, Floating, Glass and Content color Auto included.</p>
<p><strong>Scroll behavior</strong> keeps the bar pinned, lets it scroll away with the page, or hides it on the way
down and brings it back on the way up. <strong>Bar layout</strong> set to Floating turns it into a card that matches the
floating header, and <strong>Bar style</strong> set to Glass uses the shared glass recipe.</p>
<p>A floating bar sits over the first section when the header is transparent there. <strong>Use the header's colors
over dark backgrounds</strong>, off by default, then gives it the header's <strong>Colors over dark backgrounds</strong>
whenever the header wears them: at rest over a dark first section, and over every dark section with Adaptive. It
returns to its own color scheme together with the header. <strong>Content color</strong> set to Auto keeps the text, the
link and the icons readable on the bar's own color, or on what shows through its glass. See
<a href="#s-header-tone">Automatic header colors</a>.</p>
''', 'Two or three short messages that rotate: a free shipping threshold, a returns promise and a launch announcement that links to the new product.'),

    'header': ('''
<p>The logo, the main menu, predictive search, the account and cart icons, country and language selectors, and on
desktop the icons of your social media profiles (<strong>Show social media icons</strong>, which uses the links of
<a href="theme-settings.html#ts-social-media">Theme settings, Social media</a>). The logo is an image, or a text wordmark
set in the heading font. On phones the menu opens as a sheet under the header or as a full height drawer.</p>
<p><strong>Header behavior</strong> sets how the header sits on the page:</p>
<ul>
  <li><strong>Standard</strong>: the header always shows its card, in its color scheme.</li>
  <li><strong>Transparent at top</strong>, the default: over a first section that allows it (see
  <a href="#transparent-header">The header over a section</a>), the header is transparent, in the colors that suit
  that section, then takes its card on scroll.</li>
  <li><strong>Adaptive</strong>: the header stays transparent or glass at every scroll position, on every page, and its
  colors and logo follow the section under it. <strong>Background when scrolled</strong> picks Glass or
  Transparent.</li>
</ul>
<p><strong>Card background</strong> sets the card of Standard, and of Transparent at top once the page scrolls: Solid,
in the header color scheme, or Glass. <strong>Floating header (detached)</strong> pulls the header away from the screen
edges as a rounded card, with its own top margin, side margins and corner radius on desktop and on mobile.</p>
<h4 id="s-header-tone">Automatic header colors</h4>
<p>With Transparent at top or Adaptive, the header works out on its own whether what lies under it is light or dark,
with nothing to set per section. It reads the backgrounds painted under its middle line (colors, gradients by their
stops, product gradients) and lets the color or the surface that covers most of its width decide. Over a picture or a
video, it reads a small thumbnail of the part under the header, overlay included. It reads again as the page scrolls,
as a slideshow changes slide and as a Products showcase wipes to the next spotlight.</p>
<ul>
  <li>Over a <strong>light</strong> background, the header keeps its own <strong>Color scheme</strong> and its main
  <strong>Logo image</strong>.</li>
  <li>Over a <strong>dark</strong> background, it takes <strong>Colors over dark backgrounds</strong>, a color scheme
  with light text (Scheme 2 by default), and swaps in the <strong>Logo for dark backgrounds</strong> when you upload
  one. The text color goes to the menu links, the icons, the cart count, the text logo and the focus ring.</li>
</ul>
<p>An open mega menu, search panel or mobile menu always keeps the standard colors. A floating announcement bar can
follow the header with <strong>Use the header's colors over dark backgrounds</strong>.</p>
<h4 id="s-header-transparent-colors">Example: white logo and white text over a dark image</h4>
<ol class="steps">
  <li>In the first section of the page, for example a Hero with a dark image, turn on <strong>Allow transparent header</strong>.</li>
  <li>In the Header section, keep <strong>Header behavior</strong> on <strong>Transparent at top</strong>.</li>
  <li>Upload the white version of your logo in <strong>Logo for dark backgrounds</strong>. Your usual logo stays in <strong>Logo image</strong>.</li>
  <li>Set <strong>Colors over dark backgrounds</strong> to a scheme with white text, such as Scheme 2 of the Balm Studio preset (white on near black).</li>
  <li>If a floating announcement bar sits over the same image, tick <strong>Use the header's colors over dark backgrounds</strong> in the Announcement bar section, so its text turns white with the header.</li>
</ol>
<p>At the top of the page the logo, the menu and the icons are white over the dark image. On scroll the header takes its
card with your usual logo and colors, and the announcement bar returns to its own scheme at the same moment.</p>
<p>Mega menu panels follow the header. With <strong>Mega menu surface</strong> on Match header, the default, they turn
glass over a glass header, and the header card and the open panel form one surface at the opacity you set, so nothing
of the page reads through. Under a solid header the panels stay opaque. Set Mega menu surface to Solid to keep opaque
panels under a glass header too.</p>
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
  <li>To sell in more countries, go to <strong>Settings, Markets</strong> in your Shopify admin and add the countries
  or regions to a market. Each country shows the currency of its market.</li>
  <li>To offer more languages, go to <strong>Settings, Languages</strong>, add a language, translate your store with
  a translation app, then publish the language.</li>
  <li>Check that each published language is active in the markets where you want to offer it: the selector only lists
  the languages available to the visitor's market.</li>
</ol>
<p>Mega menus are built from blocks. Add a <strong>Mega menu</strong> block and type the exact title of a top level
item of your main menu in <strong>Linked menu item</strong>. Its <strong>Layout</strong> builds the panel from the
sub-links of that item (Links and images, Images only, Links only), or from the Link column, Image, Image cards,
Products, Promo and Banner blocks you add to it (Custom blocks). See <a href="#mega-menu-blocks">Mega menu
blocks</a>. A top level item without a Mega menu block opens a plain dropdown, each sub-link with the picture of what
it points to.</p>
''', 'A header that floats transparent over the home page hero and turns to glass on scroll, with a mega menu under the Shop item: two link columns and four best sellers.'),

    'footer': ('''
<p>The footer is a row of blocks: <strong>Large logo</strong>, <strong>Brand / logo</strong>, <strong>Link
column</strong> (one of your menus), <strong>Newsletter</strong>, <strong>Social media links</strong> (the icons of
your profiles and the Follow on Shop button), <strong>Text</strong> and <strong>Localization</strong> (country or currency, and language selectors,
shown only when there is more than one choice). Each block sets its own width and margins for desktop and mobile. The
Large logo always takes a row of its own, wherever it sits among the blocks.</p>
<p>Under <strong>Typography</strong>, <strong>Column heading size</strong> and <strong>Link size</strong> each have a
desktop and a mobile value (14 and 13 px by default). They are fluid like every text size of the theme: the desktop
value applies from 1440 px wide and moves toward the mobile value on narrower screens.</p>
<p>An optional <strong>Top decorative band</strong> draws a curve, a wave, a diagonal or your own image where the footer
meets the section above. The <strong>Copyright bar</strong> at the bottom can take its own color scheme. Newsletter sign
ups are added to your Shopify customers, with the tag you choose.</p>
''', 'The store name as a large wordmark across the footer, then the logo and tagline, Shop and Help link columns, a newsletter block, and a localization block for a store that sells in several countries.'),

    'hero': ('''
<p>A full screen image or Shopify hosted video with a title and a button. Desktop and mobile each get their own image
and video, cropped on the focal point you set in the admin. Video playback covers autoplay per device, a sound button,
what happens at the end (loop, stop, or show the cover again), and the style and position of the controls. The cover
always paints first, the video fades in over it, and the controls appear with the video, never before it.</p>
<p><strong>While the video loads</strong> has two styles. <strong>Cover image, then fade</strong>, the default, shows
the cover sharp until the video plays. <strong>Blurred cover, then fade</strong> keeps the cover blurred until then.
The hero has no loader of its own: for a loading screen, turn on the <a href="features.html#page-loader">Page
loader</a> in Theme settings, Loader. A hero set to a loader style in a preview version of Balm Studio now shows Cover image,
then fade.</p>
<p>The text block is placed separately on desktop and mobile, with a fine vertical offset, over an optional darkening
overlay. <strong>Height mode (desktop)</strong> and <strong>Height mode (mobile)</strong> fit the screen, adapt to the content or take a custom height.</p>
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
<p>One spotlight presents one product. Pick it in <strong>Product</strong> and the spotlight fills itself: the
product's title as the name, linked to its page, its <code>custom.tagline</code> metafield as the tagline, its <code>custom.background_color</code> and
<code>custom.background_color_end</code> metafields as the background gradient, and its main image.
<strong>Show the price</strong> adds the price under the tagline. On phones the product picture never covers the
name, the tagline or the price: on a short screen it gets smaller to fit between them and the button. The button opens the product page; with
<strong>Action</strong> set to Add to cart, a product with a single variant goes to the cart in one click and the cart
drawer opens, while a product with options, or sold out, keeps the link to its page. The metafields are read directly:
there is nothing to connect. See <a href="metafields.html#showcase">Metafields</a>.</p>
<p>Each field of the <strong>Override (optional)</strong> group replaces one of those values: name, tagline, background
color, background color end, image and link. Leave a field empty to use the product's value. Without a product, the
override fields are the spotlight's content. A background that neither the override nor the product colors takes the
background of the section's <strong>Color scheme</strong>; a start color without an end color gives a single color.</p>
<p>Each spotlight also carries highlights (a title and up to four claims with icons), an optional featured set
cartouche and a watermark. <strong>Claim 1 text</strong> to <strong>Claim 4 text</strong> are rich text fields that
can be connected to a Single line text or Multi-line text metafield of the spotlight's product, each line on its own
line (see <a href="metafields.html#icon-metafields">Icon metafields</a>). Section settings share the ingredients, the
size subtitle, the gradient style, the color scheme and the image sizing across every spotlight, and can hide the
header while the section holds the screen.</p>
<p>Each spotlight can turn a <strong>Spinning badge</strong> on its slide: an image, or a text set around a circle or a
rounded square. See <a href="features.html#spotlight-spinning-badge">Spinning badge of a spotlight</a>.</p>
''', 'Presenting a small range, three to five products, one by one on the home page or on the Products page template: pick each product once, and its metafields keep the spotlight in step with the catalog.'),

    'featured-set': ('''
<p>One product, usually a bundle or a discovery set, presented as a full width banner: a heading, a tagline in two
parts and an add to cart button. Pick the <strong>Product</strong> and the section fills itself: its title as the
heading, its <code>custom.tagline</code> metafield as the tagline, its <code>custom.background_color</code> metafield as
the background, and its image. The button adds that product to the cart. Each field of the <strong>Override
(optional)</strong> group replaces one of those values: leave a field empty to use the product's value, and a
background that neither gives takes the color scheme's. <strong>Tagline, second part</strong> has no product value: it
shows only what you type. Your own desktop and mobile background images replace the product image, darkened by an
optional overlay. Until a product is picked, the section shows a placeholder in the editor and nothing on the
storefront. See <a href="metafields.html#showcase">Metafields</a>.</p>
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
<p>Up to five products side by side. Built in rows show the image, the badges, the price, the availability, the
vendor and the rating. Each <strong>Row</strong> block adds a line: its <strong>Label</strong> sits in the left column,
and its value is read on every compared product from its <strong>Source</strong>: Metafield, Vendor, Product type, Tags,
SKU, Barcode, Weight or Unit price. With Metafield, type the metafield's name as in your admin (Skin type) or its key
(custom.skin_type) in <strong>Metafield</strong>. Each value is drawn by its type: yes and no as icons, a list as a
sentence, a number with the row's <strong>Unit</strong>, a color with its swatch, a reference by its title.</p>
<p><strong>Highlight differences</strong> marks the rows where products differ, and an empty value shows a hyphen.
<strong>Mobile layout</strong> shows one card per product (Cards), or keeps the table with the label column in place
while the product columns scroll (Scroll). See <a href="metafields.html#compare">Metafields, Compare products rows</a>
for an example.</p>
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
<p>A heading, the icons of your social media profiles and an optional button. The icons are the links typed once in
<a href="theme-settings.html#ts-social-media">Theme settings, Social media</a>: only the networks with a URL show. The
button, outlined or in glass, appears only when <strong>Button link</strong> is filled. Previous versions of Balm Studio named
this section Socials.</p>
''', 'An @yourbrand band with the Instagram, TikTok and Pinterest icons and a Follow us button, above the footer.'),

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

    'image': ('''
<p>One picture, with an optional <strong>Image (mobile)</strong> shown under 768 px. Each picture shows at its own
focal point, and a phone downloads only its own. <strong>Ratio (desktop)</strong> and <strong>Ratio (mobile)</strong>
keep the picture's own shape (Original) or set one (1:1, 4:5, 3:2, 16:9, 21:9 or a custom height), with
<strong>Fit</strong> to fill or contain. A link, a corner radius, a border, an overlay and a <strong>Scroll
animation</strong> (Fade in, Zoom out or Parallax, never for visitors who ask for reduced motion) complete it.
<strong>Visibility</strong> shows it on both devices, desktop only or mobile only. Add a <strong>Caption</strong> block
for a line of text under the picture.</p>
<p>As the first section of a page, the picture loads at once, with a high priority. With <strong>Section width</strong>
on Full width and <strong>Header over this section</strong> checked, the header lies over the picture and reads its
tone.</p>
''', 'A wide lifestyle photo between two sections of the home page, or a campaign visual at the top of a landing page, with a lighter crop for phones.'),

    'scroll-text': ('''
<p>One strong statement whose words light up one after another as it scrolls into view. Type it in
<strong>Text</strong>; a line break starts a new paragraph, and words between asterisks, <code>*like this*</code>, are
highlighted in the <strong>Highlight style</strong> you pick: Italic, Accent color or Underline. <strong>Strength of
unread words</strong> sets how faint the words are before they light up; it is raised automatically when needed, so
they always keep a contrast of 3:1 with the background. Visitors who ask for reduced motion, and browsers without scroll
animations, see every word lit at once.</p>
''', 'The brand promise in two short sentences between the hero and the products, with two key words highlighted.'),

    'bento': ('''
<p>A grid of tiles of different sizes: four columns on desktop, two on phones. Add <strong>Image tile</strong>,
<strong>Text tile</strong>, <strong>Product tile</strong>, <strong>Stat tile</strong> and <strong>Video tile</strong>
blocks, and give each a <strong>Size (desktop)</strong> and a <strong>Size (mobile)</strong> of one or two columns and
one or two rows. <strong>Order on mobile</strong> moves a tile forward on phones without changing the desktop order.
<strong>Row height</strong>, <strong>Card gap</strong> and <strong>Corner radius</strong> set the grid; rows grow when a
tile, such as a product card, needs more room.</p>
''', 'A home page block that mixes a large lifestyle photo, a best seller, a key figure such as 98% natural origin and a short brand text.'),

    'featured-product': ('''
<p>One product, picked in <strong>Product</strong>, presented on any page with the blocks of the product page: title,
price, variant picker, Buy buttons with the quantity and Buy it now, description, collapsible rows and the others, plus
the <a href="#theme-blocks">theme blocks</a> and app blocks. Its media show in a gallery: images, Shopify hosted
videos, YouTube and Vimeo videos and 3D models with the AR button, with the gallery arrows of
<a href="theme-settings.html#ts-carousels">Theme settings, Carousels</a>.</p>
<p>Choosing a variant updates the price and shows the variant's image, without changing the page address. Add to cart
opens the cart as <a href="theme-settings.html#ts-cart">Theme settings, Cart</a> says. Without a product, the theme
editor shows a placeholder and nothing shows on the storefront.</p>
''', 'Launching a new product on the home page, with its gallery, its variant picker and Add to cart, two sections under the hero.'),

    'routine': ('''
<p>A care routine, step by step. Each <strong>Step</strong> block holds a step label, a product, a short text and a
moment: Morning, Evening, or both. With <strong>Show Morning and Evening tabs</strong>, two tabs show the steps of one
moment at a time; they appear only when at least one step is for a single moment. <strong>Show the total
price</strong> adds the price of the moment's products, and the button adds them all to the cart in one go, then opens
the cart as <a href="theme-settings.html#ts-cart">Theme settings, Cart</a> says. It works without JavaScript too.</p>
<p><strong>Columns</strong> and <strong>Card style</strong> set the layout. <strong>Second image on hover</strong>
crossfades to the step's <strong>Image on hover</strong>, or to the product's second image.</p>
''', 'A Morning and evening routine of four products (cleanser, serum, cream and night balm) on a product page or the home page, with Add the routine.'),

    'key-ingredients': ('''
<p>The ingredients that make a product work, one <strong>Ingredient</strong> block each: a picture, a name, the benefit
it brings and a detail. <strong>Layout (desktop)</strong> and <strong>Layout (mobile)</strong> show them as a grid, a
carousel, or Auto, a carousel only when the cards outnumber the columns. The carousel uses the arrows of
<a href="theme-settings.html#ts-carousels">Theme settings, Carousels</a>.</p>
<p><strong>Detail</strong> set to Over the picture shows the detail on the picture on hover or focus with a mouse, and
through each ingredient's More about button on every device; set to Always under the benefit, it is always visible.
Turn off <strong>Show button</strong> in an ingredient to remove its button. <strong>Image ratio</strong> takes a
square, portrait, landscape or circle frame.</p>
''', 'Three hero ingredients of a serum, each with a close up photo, the benefit in one line and where it comes from.'),

    'key-figures': ('''
<p>A row of figures, one <strong>Figure</strong> block each: a number with an optional prefix and suffix, a label and a
source note. <strong>Count up the numbers</strong> counts each figure up once when it scrolls into view; it works on
plain numbers, such as 98 or 4.8, and never for visitors who ask for reduced motion. The real figure is always in the
page for screen readers. Columns, gaps, alignment, number sizes and <strong>Card style</strong> (None, Solid, Outline or
Glass) set the look.</p>
<p>Only state figures you can prove, and say where each one comes from in its <strong>Source note</strong>.</p>
''', 'Results of a consumer test under a product launch: 98% feel softer skin, 4.8 out of 5 average rating, 30 days of use, with the study named in the source notes.'),

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
<p>The product page: media gallery on one side, a column of blocks on the other. It is the main section of the product
template, so it is not offered in <strong>Add section</strong>. Preview versions of Balm Studio also offered a second version
of it there, Balm spotlight; it has been removed. Its product gradient background and its spinning badge are now a
background mode of the Product section and the positions of the Spinning badge block.</p>
''', ''),

    'product-recommendations': ('''
<p>Product cards under the product page. <strong>Recommendation intent</strong> picks where they come from:
<strong>Related (similar products)</strong> are generated by Shopify, <strong>Complementary (pairs well with)</strong>
are the ones you curate in the Search &amp; Discovery app, and <strong>Random from a collection</strong> shows products
of the <strong>Collection</strong> you pick, in a new order on every visit. <strong>Fill up from the collection</strong>
completes Shopify's recommendations from that collection when they are fewer than the maximum. Neither ever shows a
product twice, nor the product of the page.</p>
<p>The cards sit in a grid or a carousel per device, with the arrows of
<a href="theme-settings.html#ts-carousels">Theme settings, Carousels</a>, and <strong>Badges</strong> picks which
badges they show.</p>
''', 'Four related products under every product page, with the custom badge showing on new formulas.'),

    'sticky-atc': ('''
<p>A bar with the product thumbnail, title, selected variant, price and add to cart button that stays at the top or
bottom of the screen, on desktop and mobile separately. By default it appears once the main buy button scrolls out of
view. A variant that sells as a pre-order says Pre-order here too.</p>
<p>The bar exists only as this section, which the product template places below the Product section. Preview versions
of Balm Studio also offered it as a Sticky add to cart block inside the Product section; that block has been removed.</p>
''', 'At the bottom of the screen on phones, where the main buy button quickly scrolls away.'),

    'main-collection': ('''
<p>The collection page: a banner with the title, description and image, an optional row of collection links, filters
and sorting, and the product grid. Filters come from the Search &amp; Discovery app and can sit in a column, a drawer
or a horizontal bar, whose drawer style is set in <a href="theme-settings.html#ts-filters">Theme settings,
Filters</a>. Pagination is page numbers, a Load more button or infinite scroll. Visitors can change the column count
when you allow it (see <a href="features.html#collection-columns">Column selector</a>), and <strong>Promo
tile</strong> blocks take the place of a card on the first page. <strong>Badges</strong> picks the badges of the cards,
and <strong>Text behind cutouts</strong> prints the product's title behind PNG and WebP pictures. It is the main section
of the collection template, so it is not offered in <strong>Add section</strong>.</p>
<p>The banner shows, in this order, the collection's <code>custom.banner_image</code> metafield, the <strong>Banner
image</strong> set in the section, or the collection's own image. Shopify keeps no focal point on a collection's image:
pick the picture in the section or in the metafield to frame it at the focal point set in Files. See
<a href="metafields.html#banner-image">Metafields, Banner image</a>.</p>
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
<p>The cart page: the lines beside a summary that follows the scroll, with quantity rules, the order note, the
discount code, the free shipping bar, the totals and the accelerated checkout buttons. It works without JavaScript.
What it shows is set once for the page and the drawer in <a href="theme-settings.html#ts-cart">Theme settings,
Cart</a>; the section keeps its color scheme, width and background. Gift wrapping appears here when it is on in Theme
settings.</p>
''', 'An order note for delivery instructions and the accelerated checkout buttons under the checkout button.'),

    'cart-drawer': ('''
<p>The panel that slides in when a product is added to the cart, or the short notification that replaces it. It has no
settings of its own: its type, style, free shipping bar, recommendations, order note, discount code and checkout
buttons are set in <a href="theme-settings.html#ts-cart">Theme settings, Cart</a>, shared with the cart page.</p>
<p>The free shipping bar only displays progress toward the amount you type. It does not create free shipping or a
discount: set the real rule in your admin (Settings, Shipping and delivery, or Discounts) and keep the two amounts the
same.</p>
''', 'A floating glass drawer with a free shipping bar at 50 in your currency, three complementary suggestions in a carousel and the order note.'),

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
    'footer/large_logo': '''<p>A large logo across the whole footer, on a row of its own. It comes first in the footer the
theme ships with, and one footer holds one Large logo.</p>
<ul>
  <li><strong>Text</strong>, the default, sets the store name, or the <strong>Text</strong> you type, in the heading font, with the case, weight and style of Theme settings, Typography. The size is worked out so the letters fill the width on one line, and follows the width as the screen changes.</li>
  <li><strong>Image</strong> takes your own artwork. Use an SVG, served as it is, or a transparent PNG at least 3000 px wide, so the logo stays sharp across a large screen; a PNG or JPG is served up to 3840 px wide. <strong>Recolor SVG</strong> draws a single color SVG in the color you choose; other images keep their own colors. Fill <strong>Alt text</strong> only when the header logo does not already give the store name: left empty, screen readers skip the image.</li>
</ul>
<p><strong>Width</strong> lines the logo up with the footer columns (Content width) or runs it from one edge of the
screen to the other (Full width). <strong>Alignment</strong> only has an effect when the logo is narrower than the row, which a
fitted text or an image at full width never is. <strong>Crop bottom</strong> hides up to half of the logo's height, so
it looks cut off by the edge of the footer. <strong>Color</strong> takes the text color of the color scheme or a custom
color, <strong>Opacity</strong> softens it, and <strong>Show on mobile</strong> hides it on phones, where a hidden image
is not loaded. Without an image, Image mode shows nothing on the storefront.</p>''',
    'footer/brand': '<p>Your logo, or the store name when no logo is set, with an optional tagline.</p>',
    'footer/link_column': '<p>A heading and one of your menus.</p>',
    'footer/newsletter': '<p>An email sign up field. Subscribers are added to your customers with the tag you set, which email apps such as Klaviyo or Mailchimp can read.</p>',
    'footer/social': '<p>The icons of the profiles typed in <a href="theme-settings.html#ts-social-media">Theme settings, Social media</a>, only the networks with a URL, and the Follow on Shop button, which Shopify shows only on stores that use the Shop sales channel.</p>',
    'image/caption': '<p>A short text under the picture, with its size per device, its alignment and its spacing. <strong>Text color</strong> left empty takes a color that reads on the section background.</p>',
    'routine/step': '<p>One step of the routine: a <strong>Step label</strong> (the number of the step when empty), a product, an optional <strong>Image</strong> that replaces the product\'s, a short text and its <strong>Moment</strong>: Morning and evening, Morning or Evening.</p>',
    'key-ingredients/ingredient': '<p>One ingredient: a picture, a name, the benefit and a detail. With <strong>Show button</strong>, a More about button reveals the detail; fill <strong>Button link</strong> to make it open a page instead.</p>',
    'key-figures/figure': '<p>One figure: the <strong>Number</strong>, an optional <strong>Prefix</strong> and <strong>Suffix</strong> (keep the unit there, so the number counts up), a <strong>Label</strong> that says what it measures and an optional <strong>Source note</strong>.</p>',
    'bento/image': '<p>A picture with an optional heading over it, in white over a dark gradient, and an optional link.</p>',
    'bento/text': '<p>A heading, a text and an optional button, on a color scheme of its own (Scheme 2 by default).</p>',
    'bento/product': '<p>A product card, with its own <strong>Badges</strong> setting (All, Automatic only, Custom only or None).</p>',
    'bento/stat': '<p>A large number and its label, on a color scheme of its own.</p>',
    'bento/video': '<p>A video uploaded to Shopify. It plays muted, with its controls, only when the visitor starts it.</p>',
    'footer/text': '<p>A heading and rich text, for an address or a short note.</p>',
    'footer/localization': '<p>Country or currency, and language selectors. Each appears only when your markets and languages offer more than one choice.</p>',
    'slideshow/slide': '<p>One slide: images, overlay, heading, subtext, content position and up to two buttons.</p>',
    'products-showcase/spotlight': '<p>One product spotlight: the product that fills it, the override fields, the image size and position, the Shop now or Add to cart button, highlights, the featured set cartouche, visibility and watermark.</p>',
    'featured-collection/promo_tile': '<p>A tile that takes the place of a product card at the position you choose, on the first page of the grid only.</p>',
    'main-collection/promo_tile': '<p>A tile that takes the place of a product card at the position you choose, on the first page of the grid only.</p>',
    'collection-list/collection': '<p>One collection card.</p>',
    'lookbook/hotspot': '<p>One point on the image, linked to a product or carrying a text, with its desktop and mobile position.</p>',
    'compare-products/row': '<p>One comparison line: a <strong>Label</strong>, and a <strong>Source</strong> read on every compared product (a metafield by its name or key, the vendor, the product type, the tags, the SKU, the barcode, the weight or the unit price). See <a href="metafields.html#compare">Metafields</a>.</p>',
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
    '_mega-menu': '''<p>The panel itself: which menu item opens it, its layout, width, background and padding.
<strong>Layout</strong> builds the panel from the sub-links of the linked menu item (<strong>Links and images</strong>,
<strong>Images only</strong> or <strong>Links only</strong>) or from the blocks you add inside it (<strong>Custom
blocks</strong>).</p>
<p>With Custom blocks, the blocks sit on one row of the panel and wrap onto a new row when they do not fit, exactly
<strong>Block spacing (desktop)</strong> apart. Each block has a <strong>Width (desktop)</strong>: Auto (its content),
1/4, 1/3, 1/2, 2/3 or Fill (what the others leave). <strong>Horizontal alignment (desktop)</strong> and
<strong>Vertical alignment (desktop)</strong> place them when they leave room. <strong>Media height (desktop)</strong>
on Match tallest, the default, gives every block with a picture the height of the tallest one, text under the picture
included, so every bottom lines up; Fixed uses the height you set.</p>
<p>In the mobile menu the links come first, then the cards (Promo, Image and each card of Image cards), all of the same
width and <strong>Card ratio (mobile)</strong>, laid out by <strong>Mobile cards layout</strong>: Carousel (one row that
scrolls sideways, the next card showing), Grid (two columns) or Stack.</p>''',
    '_mega-column': '''<p>A list of links. <strong>Menu</strong> picks one of your menus, the header's main menu when empty.
<strong>Links</strong> shows All links, or Only the links under a <strong>Parent link</strong>, by default the item the
mega menu opens from. <strong>Heading</strong> defaults to the title of the parent link; in the mobile menu the heading
folds the links like an accordion, and without it they show at once.</p>
<p>Second and third level links get a <strong>Sub-link indent</strong>. <strong>Group spacing</strong> sets the space
between the first level links, each with the links under it, and <strong>Link spacing</strong> the space between the
links under them, on desktop and on mobile. <strong>Show thumbnails</strong> puts the picture of each product and
collection link before it, with its size and corner radius; the other links keep its room, so the texts line up.</p>''',
    '_mega-image': '<p>An image with an optional caption, subtitle and link label, under the picture or on it, cropped at its focal point. Nothing shows on the storefront without a picture.</p>',
    '_mega-cards': '''<p>A row of up to four picture cards. <strong>Image source</strong> set to <strong>Automatic</strong>
shows the picture of what each sub-link of the linked menu item points to: a collection or a product (with its price), a
blog post, or a page through its <code>custom.image</code> metafield (see
<a href="metafields.html#page-image">Metafields, Page image</a>). <strong>Custom cards</strong> shows the
<strong>Image card</strong> blocks you add inside it.</p>
<p>Every picture is cropped at its focal point, in the <strong>Image ratio (desktop)</strong> you pick (Original,
Square, three portrait and three landscape ratios, or a fixed height), with the media corner radius of Theme settings
or your own, and a <strong>Hover effect</strong> (Zoom, Fade or None). The text sits below the picture or on it: on the
picture, place it in one of nine positions per device and add a <strong>Text backdrop</strong> (Soft gradient or Soft
glow) only where the text is, so it reads on any photo.</p>''',
    '_mega-card': '<p>One card of an Image cards block set to Custom cards: an image, a heading, a subtitle, a link and an optional button label.</p>',
    '_mega-products': '<p>Two to four products as mini cards with image, title and price. With <strong>Show product tagline</strong> on in the Header section, each card also shows the product\'s <code>custom.tagline</code> metafield.</p>',
    '_mega-promo': '<p>An image tile with a heading, a short text and a link.</p>',
    '_mega-banner': '<p>A wide banner with a background image, a heading, a short text and a button or link.</p>',
}
