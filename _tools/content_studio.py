"""Prose of the Balm Studio pages: Getting started, the Sections overview, one page per
section of the demo store, More sections, Theme settings, Metafields and FAQ.

Every section, block and setting named here is checked against the theme by
_tools/build.py (labels read from the schemas): a name the theme no longer has stops the
build. Write in US English, sentence case, without the dash characters that
_tools/check_dashes.py refuses.
"""


def shot(key, alt, caption, mobile=True, desktop=True):
    """A capture of the demo store: desktop at 1440 px, phone at 390 px."""
    d = (f'<img class="shot__d" src="assets/shots/{key}-desktop.jpg" width="1440" height="900" '
         f'alt="{alt}, on a desktop screen" loading="lazy" decoding="async">') if desktop else ''
    m = (f'<img class="shot__m" src="assets/shots/{key}-mobile.jpg" width="390" height="844" '
         f'alt="{alt}, on a phone" loading="lazy" decoding="async">') if mobile else ''
    cls = 'shot' if (desktop and mobile) else ('shot shot--wide' if desktop else 'shot shot--phone')
    return f'<figure class="{cls}">{d}{m}<figcaption>{caption}</figcaption></figure>'


# ------------------------------------------------------------------ the demo sections
# One page each. 'group' places it on the Sections page; 'lead' opens the page; 'use'
# says what it is for; 'how' how it behaves; 'tips' are content tips; 'names' lists the
# settings and blocks the prose names, checked against the schema by the build.
DEMO_GROUPS = [
    ('home', 'Home page', 'The sections of the demo home page, in their order.'),
    ('product', 'Product page', 'The product template: the product itself is on <a href="product-page.html">Product page blocks</a>.'),
    ('collection', 'Collection', 'The collection template.'),
    ('about', 'About page', 'The <code>page.about</code> template.'),
    ('contact', 'Contact page', 'The <code>page.contact</code> template.'),
    ('journal', 'Journal', 'The blog and blog post templates.'),
    ('everywhere', 'Every page', 'The header and footer groups, and the cart drawer.'),
]

DEMO = [
    {'key': 'hero-sequence', 'group': 'home',
     'lead': 'Your products one after the other at the top of the home page, each in its own color, as the visitor scrolls.',
     'use': '<p>Open the store on the products themselves. Three to five products work best: each one fills the screen in turn, with its name set large around its cutout and a bar to buy it.</p>',
     'how': '''<p>Each <strong>Product</strong> block is one step. The product name is set in layers behind the cutout, its
last line in front of it, and a bar at the bottom shows the name, the type and format, the first sentence of the
tagline, the price, <strong>View formula</strong> and <strong>Add to bag</strong>. Scrolling lifts the product away
while the next one rises, and the whole page glides to the next color, with a short pause on each product.</p>
<p><strong>Scroll length per step</strong> sets how long each product stays, on desktop and on phones;
<strong>Object height</strong> sets the size of the cutout; <strong>Bar surface</strong> paints the bar in Field,
Deep or Paper. Without JavaScript, and for visitors who ask for reduced motion, the products stand one under the
other, each a still screen in its own color, and the page scrolls on to the next section.</p>''',
     'tips': ['Give each product its two colors, its cutout and its name lines (see <a href="metafields.html">Metafields</a>): the step uses all three.',
              'A block\'s <strong>Name lines</strong> cut that step\'s name as you like, for example Sage|Balance|Serum; <strong>Use custom layering</strong> chooses which of its lines stand in front of the product. See <a href="sections.html#large-name">The large name</a>.',
              'Write a tagline whose first sentence stands alone: the bar shows only that sentence.',
              'Until you choose a product in one of its blocks, the section shows the first products of your store, one per block. Once you choose one, a block without a product is left out of the store.'],
     'names': ['Product', 'Scroll length per step (desktop)', 'Object height (desktop)', 'Bar surface', 'Name lines', 'Use custom layering', 'Default layering', 'Name size'],
     'shots': [('hero-sequence', 'Hero sequence on its first product', 'Hero sequence: the first product, its name in layers around the cutout.'),
               ('hero-sequence-name', 'Hero sequence with the first and last lines in front', 'Hero sequence: Default layering on First and last lines in front, Opacity of lines in front at 80 percent.')]},

    {'key': 'campaign', 'group': 'home',
     'lead': 'A photograph and a short text on a flat panel: the story of a season or of a launch.',
     'use': '<p>Between the hero and the products, a campaign gives the range a context: a photo, a heading of a few words, two or three sentences, a link and the credit of the photograph.</p>',
     'how': '''<p><strong>Image position (desktop)</strong> puts the photo left or right; <strong>Image position
(mobile)</strong> above or below the text. <strong>Surface</strong> paints the text panel in the Paper, Field or Deep
of the page color. The photo settles once, with a slow zoom, when the section comes into view; without JavaScript or
with reduced motion it is at rest. Without a photo the text stands alone.</p>''',
     'tips': ['Keep the heading short: it is set very large, a few words per line.',
              'Credit the photographer in <strong>Credit</strong>.',
              'Use <strong>Anchor</strong> to link to the section from a menu (for example <code>/#campaign</code>).'],
     'names': ['Image position (desktop)', 'Image position (mobile)', 'Surface', 'Credit', 'Anchor'],
     'shots': [('campaign', 'Campaign with a photo and a short heading', 'Campaign: the photo, then the text on Paper.')]},

    {'key': 'color-library', 'group': 'home',
     'lead': 'The whole range at a glance: one tall band per product, each in its color.',
     'use': '<p>Let visitors browse by color. Each band carries a product name written upright; opening it shows the product, its text and the buttons to buy it.</p>',
     'how': '''<p>Pick up to 12 products in <strong>Products</strong>, or a <strong>Collection</strong>, whose first 12
products are used when no product is picked; with neither, the first 12 products of your store. Opening a band, on hover, on click or with the keyboard, widens it, shows
the product upright with its name, type, tagline, price, <strong>View formula</strong> and <strong>Add to bag</strong>,
and gives the section and the page that product's color. <strong>Band open at start</strong> chooses the band open
first. On phones the bands stack as an accordion. Without JavaScript each band opens and closes on its own.</p>''',
     'tips': ['Give every product its two colors: without them, each product takes a color of its own derived from the house pair.',
              'The large word of the open band is the first word of the name, or its first line: <strong>Number of lines</strong> shows up to four lines, and <strong>Default layering</strong> can bring them in front of the product. See <a href="sections.html#large-name">The large name</a>.',
              'Order the products from light to dark, or by family: the row of colors is the first thing seen.'],
     'names': ['Products', 'Collection', 'Band open at start', 'Show price', 'Show add to cart button'],
     'shots': [('color-library', 'Color library with one band open', 'Color library: one band open, the others in their colors.')]},

    {'key': 'lineup', 'group': 'home',
     'lead': 'Your products standing side by side on a ruler, each at its real height.',
     'use': '<p>Show how big each product really is, for a range with several formats. The tallest product fills the shelf and the others are drawn on the same scale.</p>',
     'how': '''<p>Each <strong>Product</strong> block has a <strong>Product</strong> and a <strong>Height</strong>, in
millimeters, that you type. Pointing at a product or focusing it gives the section its color and shows its name,
type, format, height, price and link in the caption; the others fade. <strong>Word at rest</strong> is set large behind
the products until one is chosen. <strong>Show the height range</strong> prints the shortest and the tallest heights.
On phones the line-up scrolls sideways and the product in the middle is the chosen one.</p>''',
     'tips': ['Measure the products as they stand, cap included.', 'Until you choose a product in one of its blocks, the section shows the first products of your store, one per block. Once you choose one, a block without a product is left out of the store.'],
     'names': ['Height', 'Word at rest', 'Show the height range', 'Caption heading'],
     'shots': [('lineup', 'Line-up with the products on the ruler', 'Line-up: the products at true scale on the ruler.')]},

    {'key': 'day-in-color', 'group': 'home',
     'lead': 'A day told in steps, from morning to night, each with the product that fits it.',
     'use': '<p>Turn a routine into a story: an hour, a moment, a product and a line on how to use it, step after step.</p>',
     'how': '''<p>Each <strong>Step</strong> block has a large <strong>Time</strong>, a <strong>Label</strong>, a
<strong>Product</strong> and a <strong>How to use</strong> line. <strong>Ground</strong> picks the light or the dark
color of that product: light for the day, dark for the evening. As the visitor scrolls, the hour, the product and the
color change from one step to the next, and a line of hours under the stage marks the current one.
<strong>Scroll length per step</strong> sets how long each step stays. Without JavaScript the steps are a list, each in
its own color.</p>''',
     'tips': ['Write the hours as people read them, for example 7:00 and 22:00.',
              'Keep each How to use line to one sentence.',
              'Until you choose a product in one of its steps, the section shows the first products of your store, one per step, and an empty Label or How to use shows the product\'s type or its tagline. Once you choose one, a step without a product is left out of the store.'],
     'names': ['Time', 'Label', 'Product', 'How to use', 'Ground', 'Scroll length per step (desktop)'],
     'shots': [('day-in-color', 'A day in color on its morning step', 'A day in color: the morning step on the light ground of its product.')]},

    {'key': 'routine-builder', 'group': 'home',
     'lead': 'Shoppers build their routine, one product per step, and add it to the cart in one click.',
     'use': '<p>A large paragraph introduces the routine, with small cutouts of products set in the line; under it, one column per step lets shoppers choose a product, and the total of their choice is added in one go.</p>',
     'how': '''<p>In <strong>Paragraph</strong>, <code>[1]</code>, <code>[2]</code> and <code>[3]</code> become the cutouts of
<strong>Inline product 1</strong> to <strong>3</strong>. Each <strong>Step</strong> block has a <strong>Label</strong>
and two or three <strong>Products</strong>, written as words; choosing one paints the column in that product's color
and brings its cutout in. The summary lists the chosen products, then your <strong>Offer text</strong>, then the real
total of their prices. With a <strong>Discount in percent</strong>, the total is struck through and followed by the
reduced total, rounded as your money format prints prices (to the unit when it has no decimals). The button adds the
chosen products together and opens the cart.
Without JavaScript each step is a group of radio buttons in a real add to cart form.</p>''',
     'tips': ['To offer a discount on the routine, create it in your admin (Discounts), describe it in <strong>Offer text</strong> and type its percent in <strong>Discount in percent</strong>. See <a href="index.html#routine-discount">The routine discount</a>.',
              'Pick products that are in stock: a step starts on its first available product.',
              'Until you choose a product in a step or inline, the steps share the first products of your store (seven products give two, two and three), and each inline product is the first one of its step.'],
     'names': ['Paragraph', 'Inline product 1', 'Offer text', 'Button label', 'Label', 'Products', 'Surface'],
     'shots': [('routine-builder', 'Routine builder with three steps', 'Routine builder: the paragraph with its inline products, then the steps.')]},

    {'key': 'reviews', 'group': 'home',
     'lead': 'A summary of your reviews and up to three quotes from your customers, each linked to its product.',
     'use': '<p>Show what customers say, under the products they talk about. Nothing is written for you: the summary, the quotes, the names and the ratings are yours.</p>',
     'how': '''<p><strong>Summary</strong> is a line you write, for example your average rating and the number of reviews,
with a link to all your reviews. Each <strong>Review</strong> block has a <strong>Quote</strong>, an
<strong>Author</strong>, a <strong>Rating</strong> and a <strong>Product</strong>: the quote shows its stars, and the
author line ends with a small square in the color of that product and a link to it. <strong>Columns</strong> is set per
device. A review without a quote is hidden on your store.</p>''',
     'tips': ['Quote real customers, in their own words.', 'Write in <strong>Summary</strong> only what your reviews support.'],
     'names': ['Summary', 'Quote', 'Author', 'Rating', 'Product', 'Columns (desktop)'],
     'shots': [('reviews', 'Reviews with three quotes', 'Reviews: three quotes, each with the color of its product.')]},

    {'key': 'hue-finder', 'group': 'home',
     'lead': 'A short quiz that leads a hesitant shopper to one product.',
     'use': '<p>Three questions, answered with a word each, lead to the product that fits best. The section slides toward the color of the product in the lead after every answer.</p>',
     'how': '''<p>Each <strong>Question</strong> block has a question and up to four answers. Each answer points to up to
three products, in <strong>Products for answer 1</strong> and the next ones: the first product of an answer gets
three points, the second two, the third one. The last screen shows the product in the lead, with its price,
<strong>Add to bag</strong>, <strong>View formula</strong> and <strong>Start again</strong>. The section opens in the
dark color of <strong>Starting color</strong>. <strong>Remember the result for 30 days</strong>, off by default, keeps
the result on the visitor's device and adds a link to forget it; off, nothing is saved. Without JavaScript the first
question shows and each answer links to its first product.</p>''',
     'tips': ['Ask about what the shopper feels, not about the product: "How does your skin feel by midday?"',
              'Keep answers to one or two words.',
              'Until you choose products for an answer, the answers share the first products of your store, so the quiz works from the start.',
              'Once you choose products, a question without text, or without an answer that has products, is skipped.'],
     'names': ['Question', 'Products for answer 1', 'Starting color', 'Remember the result for 30 days', 'Note'],
     'shots': [('hue-finder', 'Hue finder on its first question', 'Hue finder: a question and its answers in words.')]},

    {'key': 'atelier', 'group': 'home',
     'lead': 'A wide photo of your place, then its address, its hours and how to visit.',
     'use': '<p>Tell visitors where you make your products or where your shop is, and how to come. The demo uses it on the home page and on the Contact page.</p>',
     'how': '''<p>Under the photo, on a panel painted by <strong>Surface</strong>, the <strong>Heading</strong> sits beside
<strong>Column</strong> blocks: each has a <strong>Text</strong> and an underlined link. <strong>Photo height</strong>
is set per device; the focal point of the image places it. A column without text and without a link is left out of the
store.</p>''',
     'tips': ['Put the address and the opening hours in one column, the appointments in another.',
              'Link the address to a map in <strong>Link</strong>.'],
     'names': ['Heading', 'Surface', 'Photo height (desktop)', 'Text', 'Link'],
     'shots': [('atelier', 'Atelier with a wide photo and two columns', 'Atelier: the photo, then the address and the appointments on Deep.')]},

    {'key': 'texture', 'group': 'product',
     'lead': 'A photo of the product\'s texture, or its matter drawn in its color, with its texture, its skin feel and how to use it.',
     'use': '<p>Under the product details, show what the formula feels like. The section belongs to the product template and reads the product of the page.</p>',
     'how': '''<p><strong>Source</strong> on Automatic, the default, shows the texture photo of the product when it has
one: the image of the <code>custom.texture_image</code> metafield (File, image), cut out, large and centered on the
tinted paper with a soft shadow. As the section comes into view it slides in and spreads a little; without JavaScript or
with reduced motion it stands still. A product without a photo, or the section with <strong>Source</strong> on
Illustration, shows the illustration instead.</p>
<p><strong>Material</strong> picks the illustration among five renderings, each clearly its own: Gel (a translucent dome
with a sharp highlight and micro-bubbles), Cream (an opaque satin swirl with thick edges and soft peaks), Balm (a dense,
waxy swatch with a light sheen), Fluid (a thin, wide spread with a liquid edge) and Serum (a drop running ahead of a
glossy trail). On Automatic, the default, the section reads the texture metafield of the product
(<code>custom.texture</code>), then the <strong>Texture</strong> line, and looks for the words gel, cream, balm, fluid or
serum, in any of the theme's languages; without one it draws Cream. The color always comes from the product. The
matter comes in as the section comes into view; without JavaScript or with reduced motion it is drawn at once. Beside
it: <strong>Subheading</strong> and the <strong>Texture</strong> line set large,
<strong>Skin feel label</strong> and <strong>Skin feel</strong>; under it, <strong>How to use</strong>, the price and
<strong>Add to bag</strong>. Connect the three texts to product metafields so each product shows its own: empty,
<strong>Texture</strong> reads <code>custom.texture</code> and <strong>Skin feel</strong> reads
<code>custom.skin_feel</code>. An empty text is not printed.</p>''',
     'tips': ['For the photo, create the product metafield <code>custom.texture_image</code> of type File, accepting images (see <a href="metafields.html">Metafields</a>), and upload a PNG or WebP with a transparent background, about 2,000 px wide, the matter centered with some empty margin around it: the margin may pass under the texts, the matter stays between them.',
              'Connect How to use to <code>custom.how_to_use</code>, a multi-line text metafield (see <a href="metafields.html">Metafields</a>).',
              'Write the texture of each product with one of the five words, for example Soft balm or Bouncy gel, and keep <strong>Material</strong> on Automatic: one template then serves the whole range.',
              'Choosing a variant with its own colors recolors the matter too.'],
     'names': ['Source', 'Material', 'Subheading', 'Texture', 'Skin feel label', 'Skin feel', 'How to use'],
     'shots': [('texture-photo', 'Texture with the photo of a balm', 'Texture: the photo of the texture, on the paper tinted by the product.'),
               ('texture', 'Texture of a balm, illustrated', 'Illustration: Balm, a dense waxy swatch, beside the texture and the skin feel.'),
               ('texture-gel', 'Texture of a gel, illustrated', 'Illustration: Gel, a translucent dome with micro-bubbles.'),
               ('texture-cream', 'Texture of a cream, illustrated', 'Illustration: Cream, an opaque swirl with soft peaks.'),
               ('texture-fluid', 'Texture of a fluid, illustrated', 'Illustration: Fluid, a thin wide spread.'),
               ('texture-serum', 'Texture of a serum, illustrated', 'Illustration: Serum, a drop and its glossy trail.')]},

    {'key': 'sticky-atc', 'group': 'product',
     'lead': 'A bar at the bottom of the product page, with the product and its button, once the page button has scrolled away.',
     'use': '<p>Keep the purchase one tap away on long product pages.</p>',
     'how': '''<p>The bar shows the product thumbnail, its name and its price, on Deep, and its button presses the page's
own buy button, with the same words, for example Add to bag. It appears when the page button leaves the screen at the
top, unless <strong>Always visible</strong> is on. Each part can be hidden per device. Without JavaScript the bar stays
hidden: the page button remains the way to buy.</p>''',
     'tips': ['Hide the price on phones (<strong>Price (mobile)</strong>) to leave room for the name.'],
     'names': ['Enable the bar', 'Always visible', 'Price (mobile)'],
     'shots': [('sticky-atc', 'Sticky add to cart bar', 'Sticky add to cart: the bar at the bottom of the product page.', True, False)]},

    {'key': 'main-collection', 'group': 'collection',
     'lead': 'The collection page: a head with the title and a menu of collections, then the products as tiles or as an index.',
     'use': '<p>Every collection page. Each tile wears the color of its product, and the page takes the color of the tile in view as visitors scroll.</p>',
     'how': '''<p>The <strong>Menu</strong> of <em>Collection navigation</em> shows a menu of collections as words beside the
title, the current one underlined: the demo uses a menu named <code>shop-filters</code> (All, Cleanse, Treat, Hydrate,
Protect). <strong>Default view on desktop</strong> and <strong>Default view on mobile</strong> choose Grid, tiles in the color of each
product, or Index, rows that preview each product as you point at it; <strong>Let visitors switch between Grid and
Index</strong> adds the two words to the tools. The products follow the sort order of the collection set in your admin.
Filters come from Shopify's Search and Discovery app.</p>
<p><strong>Show the product rating</strong> prints the rating of each product above its name, with the number of
reviews (see <a href="index.html#ratings">Product ratings</a>). <strong>Show color swatches</strong> draws the values of
its color option as swatches, each a link to its variant. Both are off on the demo.</p>
<p><strong>Show an All tile</strong> closes the grid with a tile on the background of the page, its first word set large
like the names of the tiles, that links to all products: <strong>All tile collection</strong> (empty:
<code>/collections/all</code>) and <strong>All tile label</strong> (All formulas on the demo). It fills the empty cells
of the last row, for the column count of each device and the one a visitor picks, and hides when the row is full; it
never shows on its own collection.</p>''',
     'tips': ['Give each collection its two colors (<code>custom.background_color</code> and <code>custom.background_color_end</code>) to tint its head.',
              'Set the order of the products in your admin (Products, Collections, Sort): the page keeps it.'],
     'names': ['Menu', 'Default view on desktop', 'Default view on mobile', 'Let visitors switch between Grid and Index', 'Enable filters', 'Show the product rating', 'Show color swatches', 'Show an All tile', 'All tile collection', 'All tile label'],
     'shots': [('main-collection', 'The collection as tiles', 'Collection: tiles in the color of each product.'),
               ('main-collection-index', 'The collection as an index', 'Collection: the Index view, rows that preview each product.'),
               ('main-collection-all', 'A collection closed by the All tile', 'Collection: one product, then the All tile in the empty cells of the row.')]},

    {'key': 'chapters', 'group': 'about',
     'lead': 'Your story in chapters, each on the color of the product it led to.',
     'use': '<p>The About page of the demo: three chapters, each a full screen with a numeral, a heading, a text and a product.</p>',
     'how': '''<p>Each <strong>Chapter</strong> block has a <strong>Numeral</strong>, a <strong>Heading</strong>, a
<strong>Text</strong>, a <strong>Product</strong> (its cutout leans in the corner when <strong>Show the product</strong>
is on) and an optional link. The chapter is painted in the color of its product. <strong>Tint the page with the first
chapter</strong> gives the whole page, header and footer included, the color of the first chapter.</p>''',
     'tips': ['Roman numerals read well at this size: I, II, III.', 'Keep each text to two sentences.'],
     'names': ['Numeral', 'Heading', 'Text', 'Product', 'Show the product', 'Tint the page with the first chapter'],
     'shots': [('chapters', 'Chapters on its first chapter', 'Chapters: the first chapter, in the color of its product.')]},

    {'key': 'ingredient-atlas', 'group': 'about',
     'lead': 'A wall of ingredient names: point at one to see what it does and which products contain it.',
     'use': '<p>Show the key ingredients of the range, each linked to the products that use it.</p>',
     'how': '''<p>Each <strong>Ingredient</strong> block has a <strong>Name</strong>, a <strong>Note</strong> and up to four
<strong>Products</strong>. The names are set large, each with the number of its products; pointing at a name, focusing
it or tapping it fills the note beside the wall with the name, the note and the products in their colors, and gives the
section the color of the first product. <strong>Note heading</strong> and <strong>Note text</strong> fill the note at
rest. The atlas reads its blocks only: there is no metaobject to create. Without JavaScript the names and the note at
rest show.</p>''',
     'tips': ['Say what each ingredient does in one sentence.', 'An ingredient without a name is hidden on your store.'],
     'names': ['Name', 'Note', 'Products', 'Note heading', 'Note text'],
     'shots': [('ingredient-atlas', 'Ingredient atlas at rest', 'Ingredient atlas: the wall of names and the note.')]},

    {'key': 'numbers', 'group': 'about',
     'lead': 'Large figures with a line of text under each.',
     'use': '<p>Three facts about how you make your products, set large on Deep at the end of the About page.</p>',
     'how': '<p>Each <strong>Number</strong> block has a <strong>Figure</strong> and a <strong>Text</strong>. <strong>Columns (desktop)</strong> sets how many sit side by side; phones show one per row. The figures are printed as you type them: the section counts and animates nothing.</p>',
     'tips': ['Type only figures that are true for your brand.'],
     'names': ['Figure', 'Text', 'Columns (desktop)', 'Surface'],
     'shots': [('numbers', 'Numbers with three figures', 'Numbers: three figures on Deep.')]},

    {'key': 'main-contact', 'group': 'contact',
     'lead': 'The contact page: a heading, your details and the contact form.',
     'use': '<p>Your support details and the form, on the Contact page.</p>',
     'how': '''<p>Beside the <strong>Heading</strong> and the <strong>Text</strong>, <strong>Detail</strong> blocks list ways
to reach you, each a <strong>Label</strong>, a <strong>Value</strong> and an optional link; a detail without a value is
not printed. The form has underlined fields and a choice of <strong>Subjects</strong>, separated by commas, the first
one chosen at first. The form works without JavaScript and its messages come back with the page.</p>''',
     'tips': ['Add your email and your phone number as Detail blocks: the demo leaves them empty for you.',
              'Keep the subjects to a few words each: they are set as words to choose from.'],
     'names': ['Heading', 'Text', 'Label', 'Value', 'Subjects', 'Success message'],
     'shots': [('main-contact', 'Contact with its form', 'Contact: the details and the form.')]},

    {'key': 'main-journal', 'group': 'journal',
     'lead': 'The blog as a journal: the newest article large, in the color of its product, then the others as rows.',
     'use': '<p>Every blog page. Each article is linked to one product, whose color it wears.</p>',
     'how': '''<p>With <strong>Feature the newest article</strong> on, the newest article opens the page in the color of
its product, with its category, its reading time, its title, its excerpt and <strong>Read label</strong>. The other
articles follow as rows; pointing at a row gives it the dark color of its product. The product of an article is its
<code>custom.product</code> metafield; its category is its first tag; its reading time is its
<code>custom.reading_time</code> metafield, or is worked out from its length (see
<a href="metafields.html#articles">Metafields, Articles</a>).</p>''',
     'tips': ['Write an excerpt for each article: it is the text of the featured one.', 'Give each article a first tag such as Routine or Ingredients.'],
     'names': ['Feature the newest article', 'Read label', 'Articles per page'],
     'shots': [('main-journal', 'Journal with its featured article', 'Journal: the newest article in the color of its product.')]},

    {'key': 'main-journal-article', 'group': 'journal',
     'lead': 'The article page: the title in the color of the article product, the text, the product and the next article.',
     'use': '<p>Long reads that end on the product they talk about.</p>',
     'how': '''<p>The page takes the color of the article's <code>custom.product</code>. The top shows the category, the
reading time, the date, the title and the excerpt; the text follows on Paper in a column centred on the page, with the
product under <strong>Product label</strong> in the right margin on wide screens (1280 pixels and more) and under the
text below, then the next article in the color of its own product. In the left margin, on the same wide screens, the
meta column sets the category, the reading time, the date, a link back to the blog and a Copy link button
against the text, and stays in view with the product as the visitor reads; on smaller
screens it is one line above the text. Copy link copies the article's address and says Link copied, which screen
readers announce. <strong>Show tag</strong>, <strong>Show reading time</strong>, <strong>Show date</strong>,
<strong>Show link to the blog</strong> and <strong>Show copy link button</strong> turn each part on or off. <strong>Show the reading bar</strong>, on by
default, draws a thin bar at the top of the screen that fills as the visitor reads. It is a setting of this section,
so the bar shows on article pages only, and on every article that uses the template.</p>''',
     'tips': ['A quote in the article (the Quote format of the editor) is set large in the color of the product.'],
     'names': ['Show the reading bar', "Show the article's product", 'Product label', 'Show the next article', 'Show tag', 'Show reading time', 'Show date', 'Show link to the blog', 'Show copy link button'],
     'shots': [('main-journal-article', 'Journal article at its top', 'Journal article: the title in the color of its product.')]},

    {'key': 'header', 'group': 'everywhere',
     'lead': 'Your logo or wordmark, the main menu with its mega menus, search, the account and the bag.',
     'use': '<p>The header of every page, with the announcement bar above it.</p>',
     'how': '''<p><strong>Logo type</strong> shows your logo image or your store name as a wordmark. The <strong>Menu</strong>
is the desktop navigation; a top item opens a mega menu when a Mega menu block names it in <strong>Linked menu
item</strong>. Its <strong>Layout</strong> can be an Index (the categories set large with their product count, the
products of the category in view and a preview in the product color), Chapters, Links and images, Images only, Links
only or Custom blocks. In Chapters, each chapter links to the sub-link of the menu item at its place: the first chapter
to the first sub-link, and so on. A link to a part of the page, such as <code>/#day</code> to a section whose
<strong>Anchor</strong> is <code>day</code>, closes the menu and scrolls to the section, under the header.</p>
<p>In the Index, <strong>Show an All entry</strong> adds All after the categories, with the number of products of
<strong>All entry collection</strong> (empty: all products, <code>/collections/all</code>). Pointing at it lists those
products in the middle column, then a link set by <strong>All entry link label</strong> (View all formulas on the
demo); <strong>All entry label</strong> names the entry.</p>
<p>On phones the menu opens as a sheet: its large links are the <strong>Main links</strong> menu, each with the number
of products of its collection (the demo uses the <code>shop</code> menu), followed by <strong>Secondary links</strong>
(the demo uses <code>more</code>). Search opens full screen, with your <strong>Popular products</strong> and your
<strong>Search suggestions</strong> as words.</p>
<p>With <strong>Header behavior</strong> on Transparent at top, the header lies over a first section that allows it.
As the page scrolls, it takes the surface of the section under it, with its text kept readable, hides on the way down
and comes back on the way up.</p>''',
     'tips': ['Create the menus <code>main-menu</code>, <code>shop</code> and <code>more</code> in your admin (see <a href="index.html#menus">Menus</a>).',
              'Upload a white logo in <strong>Logo for dark backgrounds</strong> if your logo is dark.'],
     'names': ['Logo type', 'Menu', 'Main links', 'Secondary links', 'Popular products', 'Search suggestions', 'Header behavior', 'Logo for dark backgrounds', 'Show an All entry', 'All entry collection', 'All entry label', 'All entry link label'],
     'extra_sections': ['announcement-bar'],
     'shots': [('header', 'The header with the Shop mega menu open on All', 'Header: the Shop mega menu, an index of categories on Deep, All listing every formula.', False),
               ('header-sheet', 'The menu sheet', 'Header on a phone: the menu sheet on Deep.', True, False)]},

    {'key': 'tone-footer', 'group': 'everywhere',
     'lead': 'The newsletter, your menus, your store name set across the page and the legal lines.',
     'use': '<p>The footer of every page, in the footer group.</p>',
     'how': '''<p>The blocks sit in columns, the first one twice as wide: a <strong>Newsletter</strong> block with an
underlined field, <strong>Links</strong> blocks that each show a menu, and <strong>Text</strong> blocks. Under them,
<strong>Show the store name mark</strong> sets your store name (or <strong>Mark</strong>) on one line from one gutter to
the other, whatever the width of the screen and the length of the name, then
<strong>Copyright</strong>, <strong>Second legal line</strong> and, with <strong>Show policy links</strong>, the links to
your policies. <strong>Surface</strong> paints it Deep or Field, in the color of the page. A block with nothing to show
is left out of the store.</p>''',
     'tips': ['The demo uses the menus <code>shop</code> and <code>footer</code> in its two Links blocks.',
              'Subscribers are added to your customers with the newsletter tag.'],
     'names': ['Newsletter', 'Links', 'Show the store name mark', 'Mark', 'Copyright', 'Second legal line', 'Show policy links', 'Surface'],
     'shots': [('tone-footer', 'Footer with the newsletter and two menus', 'Footer: the newsletter, two menus and the store name.')]},

    {'key': 'cart-drawer', 'group': 'everywhere',
     'lead': 'The cart, opened from the side as a sheet in the color of the last product added.',
     'use': '<p>The cart opens as a drawer from every page when <strong>Cart type</strong> is Drawer in Theme settings.</p>',
     'how': '''<p>The drawer has no settings of its own: everything is in <a href="theme-settings.html#ts-cart">Theme settings,
Cart</a> and <a href="theme-settings.html#ts-gift-wrapping">Gift wrapping</a>. It lists the lines with their quantity,
the free shipping bar, the gift wrap checkbox, recommendations, the order note, the total and the checkout button.
When the cart is empty it shows your empty cart message and button.</p>''',
     'tips': ['Set <strong>Free shipping threshold</strong> to the amount of your shipping rate: the theme cannot read it.',
              'Pick your wrapping product in Gift wrapping to show the checkbox.'],
     'names': [],
     'shots': [('cart-drawer', 'The cart drawer', 'Cart drawer: the lines, the gift wrap checkbox and the total.')]},
]

SECTIONS_LEAD = ('Balm Studio is built from sections you add, remove and reorder in the theme editor. Each section of the demo '
                 'store has its own page; the sections of the first version of the theme are on '
                 '<a href="more-sections.html">More sections</a>.')

SECTIONS_SHARED = '''
<h2 id="tone">Every section wears a color</h2>
<p>Each product carries two colors, a dark and a light one, in its metafields (see <a href="metafields.html">Metafields</a>).
The theme works out six colors from them on the server, with the contrast of every text checked: the light ground
(Field), the color itself (Tone), the text (Ink), a dark ground (Deep), a color for large text on Deep, and an almost
white ground (Paper). A product page, a collection or a section that shows a product takes these colors, and the page
glides from one color to the next as the visitor scrolls. Pages without a product color use the house pair of
<a href="theme-settings.html#ts-tone">Theme settings, Tone</a>. A product without its own colors takes a color of its
own, derived from the house pair: the same on its page, its tile, the menu, the cart and every section that shows
it, different from one product to the next, never gray.</p>

<h2 id="large-name">The large name</h2>
<p>Hero sequence, Color library, the product page and Featured product set the product's name large behind the
product. Its lines come from <strong>Name lines</strong> in a Hero sequence block, else from the product's
<code>custom.name_lines</code> metafield (a bar | at each break, four lines at most), else from its title, cut into
<strong>Number of lines</strong> (Auto: three at most). <strong>Default layering</strong> brings lines in front of the
product: Behind the product, Last line in front, First and last lines in front or All in front; in a Hero sequence
block, <strong>Use custom layering</strong> and <strong>Line 1 in front</strong> to <strong>Line 4 in front</strong>
choose line by line. <strong>Opacity of lines in front</strong> lets the product show through them.
<strong>Name size</strong> Fixed follows the screen, Auto sizes the longest line to most of the width of the scene;
<strong>Scale</strong> makes it smaller or larger, from 60 to 130 percent. Whatever the settings, no line runs off the
screen or under the header, and the name keeps its size for visitors who ask for reduced motion.</p>

<h2 id="shared-settings">Settings most sections share</h2>
<section class="entry" id="section-background-entry">
<h3 id="section-background">Surface</h3>
<p>Most sections have a <strong>Surface</strong> setting that paints their background:</p>
<ul>
  <li><strong>Field</strong>: the light ground of the page color.</li>
  <li><strong>Deep</strong>: the dark ground of the same color, with light text.</li>
  <li><strong>Paper</strong>: an almost white ground tinted with the color.</li>
  <li><strong>Color scheme</strong>: the section's color scheme (see <a href="theme-settings.html#ts-colors">Theme settings, Colors</a>) instead of the page color.</li>
  <li><strong>Image</strong>: a picture behind the section, with the color scheme for the text.</li>
</ul>
<p>Some sections offer only some of these surfaces.</p>
</section>
<section class="entry" id="section-width-entry">
<h3 id="section-width">Section width</h3>
<p>The sections that have <strong>Section width</strong> reach Page width, Full width with margins or Full width.
<strong>Theme default</strong> follows <strong>Default section width</strong> of
<a href="theme-settings.html#ts-layout">Theme settings, Layout</a>, so every section left on it changes at once.</p>
</section>
<section class="entry" id="transparent-header-entry">
<h3 id="transparent-header">The header over a section</h3>
<p>With <strong>Header behavior</strong> on Transparent at top in the <a href="section-header.html">Header</a>, the header
lies over the first section of a page when that section allows it. The demo sections that open a page (Hero sequence,
Contact, Journal, Journal article and Chapters) allow it on their own. Many sections of
<a href="more-sections.html">More sections</a> have <strong>Header over this section</strong> or <strong>Allow
transparent header</strong> for the same purpose.</p>
</section>
<section class="entry" id="spacing-entry">
<h3 id="spacing">Desktop and mobile values</h3>
<p>Sizes and spacings come in pairs: a label ending in (desktop) and one ending in (mobile). Text sizes are fluid
between the two and are multiplied by <strong>Heading scale</strong> or <strong>Body scale</strong> of
<a href="theme-settings.html#ts-typography">Theme settings, Typography</a>. Use the device switch at the top of the
editor to preview both.</p>
</section>
<section class="entry" id="anchor-entry">
<h3 id="anchor">Anchor and breadcrumbs</h3>
<p><strong>Anchor</strong> names a section so a menu link can point at it, for example <code>/#lineup</code>.
<strong>Breadcrumbs on this page</strong> shows or hides the breadcrumb trail on one page, whatever
<a href="theme-settings.html#ts-breadcrumbs">Theme settings, Breadcrumbs</a> says.</p>
</section>
<section class="entry" id="empty-entry">
<h3 id="empty">Empty content</h3>
<p>An empty text prints nothing on your store, and a block that misses what it needs (a review without a quote, a step
without a product, once the section has products) is left out. A section of products where you have chosen none shows
the first products of your store, and a store without products shows Shopify's product placeholders there. In the theme editor such a block keeps its frame with a short note that says why it is
hidden, so you can still select it.</p>
</section>
'''

# ------------------------------------------------------------------ More sections
MORE_INTRO = '''<p>These sections come from the first version of Balm Studio. They follow the same colors, fonts and
square corners as the rest of the theme, and they are not used by the demo store. Add them from <strong>Add
section</strong> in the theme editor.</p>'''

MORE_GROUPS = [
    ('more-story', 'Images and storytelling', ['hero', 'slideshow', 'image', 'image-with-text', 'rich-text', 'scroll-text', 'video', 'marquee', 'before-after', 'bento']),
    ('more-products', 'Products and collections', ['featured-product', 'featured-set', 'featured-collection', 'collection-list', 'routine', 'lookbook', 'compare-products', 'recently-viewed', 'product-recommendations']),
    ('more-trust', 'Trust and engagement', ['key-ingredients', 'key-figures', 'multicolumn', 'testimonials', 'logo-list', 'countdown', 'newsletter', 'newsletter-popup', 'socials', 'faq']),
    ('more-about', 'About page', ['about-hero', 'about-problem-shift', 'about-feels-off', 'about-community']),
    ('more-contact', 'Contact and stores', ['contact', 'find-us']),
    ('more-layout', 'Layout, code and apps', ['divider', 'custom-liquid', 'apps']),
    ('more-templates', 'Template sections', ['main-search', 'main-cart', 'main-list-collections', 'main-page', 'main-blog', 'main-article', 'main-404', 'main-password', 'main-gift-card', 'footer']),
]

MORE_TEXT = {
    'hero': 'A large image or video with a heading, a text and up to two buttons, its content on a panel in the colors of the section.',
    'slideshow': 'Up to six slides, each with its desktop and mobile images, a heading, a text and buttons, with Previous and Next in words and the slide numbers as tabs.',
    'image': 'One picture, at the width you choose, with a separate mobile image, a link, a caption and Reveal on scroll.',
    'image-with-text': 'An image beside a column of theme blocks: heading, text, button, image, spacer or Liquid.',
    'rich-text': 'A column of theme blocks. Its Statement style sets the text as one large paragraph, where Product inline blocks place a product cutout in the line.',
    'scroll-text': 'One large statement whose words light up one after the other as the section scrolls.',
    'video': 'A Shopify-hosted video, or a YouTube or Vimeo video, each with an optional mobile version.',
    'marquee': 'A line of words that scrolls across the page, paused on hover and on focus.',
    'before-after': 'Two images in one frame, the second revealed by a handle the visitor drags.',
    'bento': 'A grid of tiles of several kinds: image, text, product, figure and video.',
    'featured-product': 'One product page in small, picked in the section, on any page, with the blocks of the product page.',
    'featured-set': 'One product with a heading, a tagline in two parts and its buy button, over a background color or image.',
    'featured-collection': 'The products of one collection, as tiles in their colors or as index rows.',
    'collection-list': 'Collections you pick, as index rows or as tiles in the color of each collection.',
    'routine': 'A care routine step by step, each step a product, a text and its moment, morning or evening.',
    'lookbook': 'One image with up to twelve hotspots, each showing a product or a short text.',
    'compare-products': 'Up to five products side by side in a table, with rows you turn on or add.',
    'recently-viewed': 'The products the visitor opened, newest first, read from their browser.',
    'product-recommendations': 'Products related to, or bought with, the product of the page, from Shopify recommendations.',
    'key-ingredients': 'The ingredients of a product or a range: a picture, a name, what it does and a detail.',
    'key-figures': 'A row of figures with a label and an optional source.',
    'multicolumn': 'Columns of an image or an icon, a heading, a text and a link.',
    'testimonials': 'Quotes from customers, with their name and an optional rating.',
    'logo-list': 'A row of press or partner logos, in the text color or in their own colors.',
    'countdown': 'A countdown to a date you type, in the time zone of your store.',
    'newsletter': 'A band with a newsletter signup form.',
    'newsletter-popup': 'A newsletter signup in a popup that opens after a delay you set, and comes back after the number of days you choose.',
    'socials': 'Your social media profiles as words, from Theme settings, Social media.',
    'faq': 'Questions and answers as accordions with a turning "+".',
    'about-hero': 'An opening for an About page: a heading and a text on a panel beside a photo.',
    'about-problem-shift': 'Two panels side by side to compare a before and an after.',
    'about-feels-off': 'A checklist of short items, each with an optional link, on a panel.',
    'about-community': 'Two words set large on a band over a background, a row of images, each with an optional link, and a link under the band.',
    'contact': 'A contact form with a heading and a text, in underlined fields.',
    'find-us': 'Where to buy your products: one or two columns of stores and online sellers, with a map, over a background image.',
    'divider': 'A thin rule between two sections.',
    'custom-liquid': 'Your own Liquid, HTML and CSS, in a section with the theme spacing.',
    'apps': 'Holds app blocks added straight onto a template.',
    'main-search': 'The search results page, with the same tiles, filters and sorting as a collection.',
    'main-cart': 'The cart page, set up in Theme settings, Cart.',
    'main-list-collections': 'The list of all collections, as index rows or tiles.',
    'main-page': 'A standard page: its title, then its content on Paper.',
    'main-blog': 'A blog as a list of articles. The demo uses Journal instead.',
    'main-article': 'An article page. The demo uses Journal article instead.',
    'main-404': 'The page shown for an address that does not exist, with a search field.',
    'main-password': 'The page shown while your store is protected by a password.',
    'main-gift-card': 'The page of a gift card, with its balance, its code and a QR code.',
    'footer': 'The footer of the first version, with a large logo, link columns, a newsletter and social media links. The demo uses the newer Footer.',
}


# ------------------------------------------------------------------ Getting started
GS_LEAD = ('Balm Studio is a Shopify theme where every product dresses the store in its own color. This guide takes you '
           'from installation to a store ready to publish: the preset, the color of each product, the metafields and '
           'menus to create, and the first settings.')

GETTING_STARTED = '''
<ul class="cards">
  <li><a href="theme-settings.html"><strong>Theme settings</strong><span>Colors, tone, fonts, buttons, cart and storewide features.</span></a></li>
  <li><a href="sections.html"><strong>Sections</strong><span>Every section of the demo store, one page each.</span></a></li>
  <li><a href="product-page.html"><strong>Product page blocks</strong><span>Build the product page, block by block.</span></a></li>
  <li><a href="metafields.html"><strong>Metafields</strong><span>The colors, cutouts and texts of each product.</span></a></li>
  <li><a href="features.html"><strong>Features</strong><span>Quick view, badges, gift wrapping, age verifier and more.</span></a></li>
  <li><a href="faq.html"><strong>FAQ</strong><span>Answers to the questions merchants ask most.</span></a></li>
</ul>

<h2 id="install">Install Balm Studio</h2>
<ol class="steps">
  <li>Open the Balm Studio page on the <a href="https://themes.shopify.com/">Shopify Theme Store</a> while logged in to your store.</li>
  <li>Select <strong>View demo store</strong> to browse Balm Studio with its content before you install it.</li>
  <li>Select <strong>Try theme</strong> to add a trial copy to your theme library, or buy the theme. A trial lets you customize everything; you pay when you publish.</li>
  <li>In your admin, go to <strong>Online Store, Themes</strong> and select <strong>Customize</strong> on Balm Studio to open the theme editor.</li>
  <li>When the store is ready, open the theme's <strong>...</strong> menu in the theme library and choose <strong>Publish</strong>.</li>
</ol>
<p>Balm Studio needs no app. Apps that offer app blocks, such as reviews or subscriptions, plug into the product page and
into most sections.</p>
<h3 id="updates">Updating Balm Studio</h3>
<p>When a new version is released, your theme library shows a notice. Shopify adds the new version as a separate copy
that keeps your theme editor settings and content, so you can review it before publishing it. Changes made in the theme
code are not carried over: see <a href="custom-code.html">Custom code</a>. What changed is listed in the
<a href="changelog.html">Changelog</a>.</p>

<h2 id="preset">The Balm Studio preset</h2>
<p>Balm Studio comes with one preset, also named Balm Studio, and your store starts from it:</p>
<ul>
  <li><strong>Fonts.</strong> Headings in Gloock, text in Instrument Sans, on one fluid type scale.</li>
  <li><strong>House colors.</strong> A deep violet (<code>#2A1F5E</code>) and a lavender (<code>#7464B6</code>): the colors of every page that shows no product, set in <a href="theme-settings.html#ts-tone">Theme settings, Tone</a>.</li>
  <li><strong>Color schemes.</strong> White, near black, deep violet and pale lavender, for the sections set to the Color scheme surface.</li>
  <li><strong>Layout.</strong> Pages in Full width with margins, with side margins of 60 px on desktop and 20 px on phones, and square corners.</li>
  <li><strong>Details.</strong> Medium buttons, breadcrumbs separated by a slash, the New badge on products tagged <code>new</code>, and an empty cart that points to the color library.</li>
</ul>
<p>The demo templates (home page, product, collection, About, Contact and Journal) are filled with sections and example
texts you replace with yours. Every value is a starting point that you change in the theme editor.</p>

<h2 id="tone-on-tone">Tone on tone</h2>
<p>Each product carries two colors, a dark one and a light one, in two metafields. From them the theme works out, on the
server, a light ground, the color itself, a text color, a dark ground, a color for large text on the dark ground and an
almost white ground, and it checks the contrast of every text before the page is sent. Then:</p>
<ul>
  <li>the product page, its header and its footer wear the colors of the product, and a variant with its own colors recolors the page when it is chosen;</li>
  <li>tiles, bands and steps show each product in its colors, and the page glides from one color to the next as the visitor scrolls;</li>
  <li>a collection with its own two colors tints its head;</li>
  <li>a page without a product color uses the house pair of the preset, and a product without colors takes a color of
  its own derived from it, the same on every page.</li>
</ul>
<p>Everything reads correctly without JavaScript, and visitors who ask for reduced motion see each color at once. Give
every product its two colors before anything else: it is what makes the store look like the demo.</p>

<h2 id="metafields">Metafield definitions to create</h2>
<p>Create these definitions in your admin, under <strong>Settings, Custom data</strong>, with exactly the namespace and
key shown (<code>custom</code> is the namespace). The theme reads them as soon as they exist; a product that leaves one
empty simply does not show that part. Details and examples are on <a href="metafields.html">Metafields</a>.</p>
{META_TABLES}
<p>Some texts are connected in the demo product template rather than read by the code: the product passport rows, the
How to use and Ingredients rows, and the Texture section. If you create these definitions after installing the theme,
the connections of the demo template work as they are; with other keys, connect each setting to your metafield with the
dynamic source icon of the theme editor.</p>

<h2 id="ratings">Product ratings</h2>
<p>The product page Rating block, the quick view and Compare products show a rating when the product has one: first the
standard <code>reviews.rating</code> and <code>reviews.rating_count</code> metafields that review apps write, else
<code>custom.rating</code> (a rating, or a number out of 5) and <code>custom.rating_count</code> (an integer) that you fill
yourself. Without either, nothing is shown. The collection tiles show it too when <strong>Show the product rating</strong>
is on in the <a href="section-main-collection.html">Collection</a> section.</p>

<h2 id="complementary">Products that go well together</h2>
<p>The <strong>Complementary products</strong> block of the product page (Works well with on the demo) and the
recommendations of the cart read Shopify's complementary products. Choose them per product in Shopify's free
<strong>Search and Discovery</strong> app, under Product recommendations. Until you do, the block shows related
products, or nothing.</p>

<h2 id="menus">Menus</h2>
<p>Create these menus in <strong>Content, Menus</strong> with these handles: the demo templates already point to them.</p>
<div class="table-wrap"><table class="settings"><thead><tr><th scope="col">Menu handle</th><th scope="col">Used by</th><th scope="col">What to put in it</th></tr></thead><tbody>
<tr><th scope="row" data-label="Menu handle"><code>main-menu</code></th><td data-label="Used by">Header, Menu</td><td data-label="What to put in it">Shop, with your categories under it (Cleanse, Treat, Hydrate and Protect on the demo) for the Index mega menu; Journal; Rituals, with links to the sections of the home page; About.</td></tr>
<tr><th scope="row" data-label="Menu handle"><code>shop</code></th><td data-label="Used by">Header, Main links (the menu sheet on phones); the first Links block of the footer</td><td data-label="What to put in it">All formulas and your collections, each linked to a collection so its number of products shows.</td></tr>
<tr><th scope="row" data-label="Menu handle"><code>shop-filters</code></th><td data-label="Used by">Collection, Menu</td><td data-label="What to put in it">All (linked to <code>/collections/all</code>), then one link per category collection.</td></tr>
<tr><th scope="row" data-label="Menu handle"><code>footer</code></th><td data-label="Used by">The second Links block of the footer</td><td data-label="What to put in it">Delivery, Returns, Contact, Journal: your help pages.</td></tr>
<tr><th scope="row" data-label="Menu handle"><code>more</code></th><td data-label="Used by">Header, Secondary links (under the large links of the menu sheet)</td><td data-label="What to put in it">The links to the sections of the home page, Journal, About and Contact.</td></tr>
</tbody></table></div>

<h2 id="routine-discount">The routine discount</h2>
<p>The <a href="section-routine-builder.html">Routine builder</a> adds the products a shopper chose and shows the total
of their prices. To reward a full routine, create the discount in your admin, under <strong>Discounts</strong>, for
example an automatic discount on the products of the routine, describe it in the section's <strong>Offer text</strong>
and type its percent in <strong>Discount in percent</strong>: the total is then struck through and followed by the
reduced total, for example 114 € and 103 € for ten percent. The setting changes what the page shows; checkout applies
the discount of your admin, so keep the two in step.</p>

<h2 id="first-setup">First setup, step by step</h2>
<ol class="steps">
  <li><strong>Colors of each product.</strong> Create the definitions above, then give every product its two colors, its cutout and its name lines.</li>
  <li><strong>House colors and fonts.</strong> In <a href="theme-settings.html#ts-tone">Tone</a> and <a href="theme-settings.html#ts-typography">Typography</a>, set the colors of the pages without a product and your fonts.</li>
  <li><strong>Header.</strong> Open the <a href="section-header.html">Header</a>: your logo or your store name as a wordmark, and the menus above. Add a Mega menu block for Shop with the Index layout.</li>
  <li><strong>Home page.</strong> Replace the products, photos and texts of each section: see <a href="sections.html">Sections</a>.</li>
  <li><strong>Product page.</strong> Open a product in the editor and review its blocks: see <a href="product-page.html">Product page blocks</a>.</li>
  <li><strong>Collections.</strong> Set the order of each collection in your admin, give each collection its two colors, and install Search and Discovery for the filters.</li>
  <li><strong>Cart.</strong> In <a href="theme-settings.html#ts-cart">Theme settings, Cart</a>, set the free shipping threshold and the empty cart; in <a href="theme-settings.html#ts-gift-wrapping">Gift wrapping</a>, pick your wrapping product.</li>
  <li><strong>Journal.</strong> Link each article to a product and give it a reading time (see <a href="metafields.html#articles">Metafields, Articles</a>).</li>
  <li><strong>Pages.</strong> Create your About and Contact pages and assign them the <code>page.about</code> and <code>page.contact</code> templates.</li>
  <li><strong>Check and publish.</strong> Preview every page type on a desktop screen and on a phone, place a test order, then publish.</li>
</ol>

<h2 id="templates">Templates included</h2>
<p>Home page, product, collection, list of collections, search, cart, blog, blog post, page, 404, password and gift card;
a second collection template, <code>collection.colorful</code> (the collection on Deep); and five page templates:
<code>page.about</code> (About), <code>page.contact</code> (Contact), <code>page.faq</code> (FAQ), <code>page.find-us</code>
(Store locator) and <code>page.products</code> (Products). All of them are built from sections you can change in the
editor.</p>

<h2 id="help">Need help?</h2>
<p>Search this documentation with the box at the top of the page, read the <a href="faq.html">FAQ</a>, or contact
<a href="support.html">Balm Studio support</a>.</p>
'''

# ------------------------------------------------------------------ Metafields
# (owner, key, type, where it is read)
META = {
    'product': [
        ('custom.background_color', 'Color', 'The dark color of the product. Every page, tile and section that shows the product.'),
        ('custom.background_color_end', 'Color', 'The light color of the product. Without it the theme derives it from the dark one.'),
        ('custom.cutout', 'File (image)', 'The product standing, on a transparent background, cropped tight. Without it the featured image is used.'),
        ('custom.name_lines', 'Single line text', 'The name in lines, separated by <code>|</code>, for example <code>Lavender|Night|Renewal</code>. Hero sequence, the product page, tiles.'),
        ('custom.volume', 'Single line text', 'The format, for example <code>50 ml</code>. Hero sequence, Color library, Line-up, index rows.'),
        ('custom.tagline', 'Single line text', 'A short description. Hero sequence (its first sentence), Color library, Hue finder, and the Text block of the product page with its Source on Tagline.'),
        ('custom.next_product', 'Product', 'The product Next product opens on the product page. Without it, the next one in the collection.'),
        ('custom.primary_collection', 'Collection', 'The collection of the breadcrumb and of Next product.'),
        ('custom.badge_label', 'Single line text', 'The text of the custom badge.'),
        ('custom.skin_type', 'Single line text', 'Passport row Suited to; Compare products.'),
        ('custom.skin_feel', 'Single line text', 'Passport row Skin feel; Texture, Skin feel.'),
        ('custom.key_ingredients', 'Single line text', 'Passport row Key ingredients.'),
        ('custom.texture', 'Single line text', 'Passport row Texture; Texture, the heading and the choice of its illustration.'),
        ('custom.texture_image', 'File (image)', 'A photo of the texture, cut out on a transparent background. Texture shows it, large and centered, when its Source is on Automatic; without it, the illustration.'),
        ('custom.aroma', 'Single line text', 'Passport row Aroma.'),
        ('custom.dosage', 'Single line text', 'Passport row Dosage.'),
        ('custom.how_to_use', 'Multi-line text', 'The How to use row of the product page; Texture, How to use.'),
        ('custom.ingredients', 'Multi-line text', 'The Ingredients row of the product page.'),
        ('custom.rating', 'Rating, or decimal number', 'The rating out of 5, when no review app writes <code>reviews.rating</code>.'),
        ('custom.rating_count', 'Integer', 'The number of reviews, when no review app writes <code>reviews.rating_count</code>.'),
    ],
    'variant': [
        ('custom.background_color', 'Color', 'The dark color of a variant that differs from its product: choosing it recolors the page.'),
        ('custom.background_color_end', 'Color', 'The light color of that variant.'),
        ('custom.cutout', 'File (image)', 'The cutout of that variant on the product page.'),
    ],
    'collection': [
        ('custom.background_color', 'Color', 'The dark color of the collection: its head and its tile.'),
        ('custom.background_color_end', 'Color', 'The light color of the collection.'),
        ('custom.banner_image', 'File (image)', 'The banner of the collection page, before the Banner image of the section.'),
    ],
    'article': [
        ('custom.product', 'Product', 'The product of the article: its colors, its cutout, and its tile on the article page.'),
        ('custom.reading_time', 'Integer', 'The reading time in minutes. Without it, worked out from the length of the article.'),
    ],
    'page': [
        ('custom.image', 'File (image)', 'The picture of a page in the cards of a mega menu.'),
    ],
}
META_TITLES = {'product': 'Products', 'variant': 'Variants', 'collection': 'Collections', 'article': 'Articles (blog posts)', 'page': 'Pages'}

META_LEAD = ('Metafields give each product, variant, collection and article its own colors, cutout and texts. This page '
             'lists every metafield Balm Studio reads, with its key and its type.')

METAFIELDS_INTRO = '''
<p>Create each definition in your admin, under <strong>Settings, Custom data</strong>, then choose the owner (Products,
Variants, Collections, Blog posts or Pages) and type the namespace and key exactly as shown: <code>custom</code> is the
namespace. Then fill the values on each product, collection or article. A metafield left empty shows nothing, or the
fallback described below.</p>
<h2 id="colors">The two colors</h2>
<p>The dark color (<code>custom.background_color</code>) and the light color (<code>custom.background_color_end</code>)
are the heart of the theme: from them it works out the light ground, the text, the dark ground and the paper of every
page and section that shows the product, with the contrast checked. Pick the dark color deep enough to carry white text,
and the light one as the color of the product itself.</p>
<h2 id="cutout">The cutout</h2>
<p>Upload a PNG of the product standing upright on a transparent background, cropped tight to the product, about 450 by
1100 pixels for a tube. It stands in the hero, the bands, the line-up and the product page. Without it the featured
image of the product is used, which looks best when it is also a cutout.</p>
'''

META_RATINGS = '''
<h2 id="ratings">Ratings</h2>
<p>The Rating block of the product page, the quick view, Compare products and the collection tiles (with Show the
product rating on) read the standard
<code>reviews.rating</code> and <code>reviews.rating_count</code> metafields first: review apps write them for you. Without
them they read <code>custom.rating</code> and <code>custom.rating_count</code>, which you fill yourself. Without either,
no rating is shown.</p>
<h2 id="connect">Connecting a setting to a metafield</h2>
<p>A text setting of a block or a section can show a metafield instead of a fixed text: select the dynamic source icon
next to the setting in the theme editor and pick the metafield. The definition has to exist first. The demo product
template is already connected to the keys above for the passport, the How to use and Ingredients rows and the Texture
section.</p>
'''

# ------------------------------------------------------------------ Theme settings
SETTINGS_INTRO = ('Theme settings apply to the whole store. Open them from the gear icon of the theme editor. Each group '
                  'is explained below, with the full list of its settings.')

SETTINGS_GROUPS = {
    'Colors': '<p>The color schemes of the store. A section uses a scheme when its <strong>Surface</strong> is Color scheme or Image, and the header, the mega menu and some template pages pick one. Most demo sections use the colors of the products instead.</p>',
    'Tone': '<p>The house pair: the dark and the light colors of every page that shows no product, such as the cart page, a plain page or the 404. The theme derives every ground and text color from them, as it does for a product, and checks their contrast. A product without colors of its own takes a color derived from this pair, turned to a hue of its own.</p>',
    'Typography': '<p>The heading font and the text font, the two scales that enlarge or reduce every heading and every text at once, and the shared recipes of headings, button labels and small labels: case, style, weight and letter spacing. Gloock, the heading font of the preset, has one weight: a heavier Heading weight does not make it bolder.</p>',
    'Layout': '<p><strong>Page width</strong> sets how wide the product, collection and search pages run; <strong>Default section width</strong> is the width of every section left on Theme default; <strong>Section side margins</strong> sets the margins of Full width with margins, on desktop and on phones.</p>',
    'Buttons': '<p>The size, the border width and the font weight of every button of the theme, the filled Add to bag button included.</p>',
    'Tiles': '<p>The tiles that show products in their colors in every product grid: the size of the product name and of the price, the name set large behind the product (the watermark), and the small turn of the product on hover.</p>',
    'Product badges': '<p>Where badges sit on tiles and in the quick view, what the Sale badge says, and when a product is New: never, when it has a tag, or for some days after it was created.</p>',
    'Pre-order': '<p>The label of the buy buttons for a variant that keeps selling once its stock reaches 0.</p>',
    'Quick view': '<p>What the quick view shows when a visitor opens a product from its tile: vendor, rating, a short description, pickup availability and a link to the product page. Turn the quick view on in each section that shows products.</p>',
    'Cart': '<p>The cart type (a drawer, the cart page or a notification), the size of the drawer, the free shipping bar, the recommendations, the order note, the discount code field, the checkout buttons and the empty cart. The free shipping bar only shows progress toward the amount you type: create the matching shipping rate in your admin.</p>',
    'Gift wrapping': '<p>A checkbox in the cart that adds your wrapping product to the order, with an optional gift message. Pick the wrapping product, a product you create in your admin; without it the checkbox does not show.</p>',
    'Back to top': '<p>A Back to top link at the end of every page, before the footer, on desktop, on phones, or both.</p>',
    'Age verifier': '<p>A window that asks visitors to confirm their age before they see the store, with what happens when they decline and how long the answer is remembered.</p>',
    'Favicon': '<p>The small icon of your store in browser tabs and bookmarks.</p>',
    'Social media': '<p>The addresses of your profiles. Only the networks with an address show, in the header when <strong>Show social media icons</strong> is on and in the Social media links section.</p>',
    'Social media sharing': '<p>The image used when a page without its own image is shared, and your X account.</p>',
    'Breadcrumbs': '<p>The trail of links back to the home page on product, collection and article pages: whether it shows, with the collection or not, where, with which separator and how it is aligned. A page can override it with <strong>Breadcrumbs on this page</strong>.</p>',
    'Search': '<p>What the store searches: products only, or products, articles and pages.</p>',
    'Search engines': '<p>Which pages ask search engines not to list them: search results, filtered collections, or nothing.</p>',
}

# ------------------------------------------------------------------ FAQ
FAQ_LEAD = 'Answers to the questions merchants ask most about Balm Studio.'

FAQ = [
    ('Can I use Balm Studio on more than one store?', '''
<p>A theme bought from the Shopify Theme Store is licensed for one store. To use Balm Studio on another store, buy it again
from that store. Trying the theme is free on any store.</p>'''),
    ('How do I update Balm Studio without losing my settings?', '''
<p>When an update is available, your theme library shows a notice. Shopify adds the new version as a separate copy that
keeps your theme editor settings and content. Preview it, then publish it. Changes you made in the theme code are not
carried over; see <a href="custom-code.html">Custom code</a>.</p>'''),
    ('How do I give each product its own color?', '''
<p>Create the two color metafields, <code>custom.background_color</code> (the dark color) and
<code>custom.background_color_end</code> (the light color), then fill them on each product. See
<a href="metafields.html#colors">Metafields, The two colors</a>.</p>'''),
    ('Why does a product without colors show a color I did not choose?', '''
<p>The product has no colors of its own yet: fill its two color metafields. Until then it takes a color of its own,
derived from the house pair of <a href="theme-settings.html#ts-tone">Theme settings, Tone</a>, the same on its page,
its tile, the menu and the cart. The color follows the product's place in your All products collection (its first
50 products; after them, the product's ID), so it changes if that order changes. Its own two colors always come
first.</p>'''),
    ('Why is my product shown as a square photo instead of standing upright?', '''
<p>It has no cutout. Upload a PNG of the product on a transparent background, cropped tight, in its
<code>custom.cutout</code> metafield. See <a href="metafields.html#cutout">Metafields, The cutout</a>.</p>'''),
    ('How do I show star ratings?', '''
<p>Install a reviews app that writes Shopify's standard rating metafields, or fill <code>custom.rating</code> and
<code>custom.rating_count</code> on each product yourself. To show them on the collection tiles too, turn on
<strong>Show the product rating</strong> in the Collection section. See <a href="index.html#ratings">Product
ratings</a>.</p>'''),
    ('How do I set up the Shop mega menu?', '''
<p>In your <code>main-menu</code>, put your category collections under Shop. In the <a href="section-header.html">Header</a>,
add a <strong>Mega menu</strong> block, type <code>Shop</code> in <strong>Linked menu item</strong> and choose the Index
layout. The categories show with their number of products, and pointing at a product previews it in its colors.</p>'''),
    ('Why are there no filters on my collection pages?', '''
<p>Filters come from Shopify's free Search and Discovery app: install it and choose the filters there. Then keep
<strong>Enable filters</strong> on in the <a href="section-main-collection.html">Collection</a> section.</p>'''),
    ('How do I show the categories above a collection?', '''
<p>Create a menu with the handle <code>shop-filters</code>: All, linked to <code>/collections/all</code>, then one link per
collection. The Collection section of the demo already points to it in its <strong>Menu</strong> setting.</p>'''),
    ('How do I give an article its color and its reading time?', '''
<p>Fill the article's <code>custom.product</code> metafield with a product: the article takes its colors and shows its
tile. Fill <code>custom.reading_time</code> with the minutes; without it the time is worked out from the length of the
text. See <a href="metafields.html#articles">Metafields, Articles</a>.</p>'''),
    ('Why does Heading weight not make my headings bolder?', '''
<p>Gloock, the heading font of the preset, has a single weight. The theme never fakes a bolder one, so every weight shows
the same letters. Choose a heading font with several weights in <a href="theme-settings.html#ts-typography">Typography</a>
to use Heading weight.</p>'''),
    ('Why does my header change color as I scroll?', '''
<p>The header takes the surface of the section under it, with its text kept readable, so it always belongs to what it
sits on. There is nothing to set per section.</p>'''),
    ('How do I set up gift wrapping?', '''
<p>Create a product for the wrapping, with its price. In <a href="theme-settings.html#ts-gift-wrapping">Theme settings, Gift
wrapping</a>, turn on <strong>Offer gift wrapping</strong> and pick it in <strong>Wrapping product</strong>. The checkbox
then shows in the cart.</p>'''),
    ('What do the product sections of the home page show after I install the theme?', '''
<p>Your products. The theme installs the layout of the demo store without its content: no products, collections,
pictures or menus of the demo. Without a product chosen in them, Hero sequence, Color library, Line-up, A day in color,
Routine builder and Hue finder show the products of your store, in the order of your All products collection, as many
as each section has places for, each in its own two colors or, without them, in a color derived from
<a href="theme-settings.html#ts-tone">Theme settings, Tone</a>. As soon as you choose a product in a section, it shows
your choice. A store without products shows Shopify's product placeholders in the same places, on the store too. Texts
show an example that says what to write.</p>'''),
    ('How do I show a free shipping progress bar?', '''
<p>In <a href="theme-settings.html#ts-cart">Theme settings, Cart</a>, keep <strong>Show the free shipping bar</strong> on
and type the amount in <strong>Free shipping threshold</strong>. The bar only displays progress: create the matching free
shipping rate in your admin and keep the two amounts the same.</p>'''),
    ('How do I offer a discount on a routine?', '''
<p>The Routine builder shows the real total of the chosen products. Create the discount in your admin, under Discounts,
and describe it in the section's <strong>Offer text</strong>. See <a href="index.html#routine-discount">The routine
discount</a>.</p>'''),
    ('Can I change the color of the Shop Pay or PayPal buttons?', '''
<p>No theme can. The accelerated checkout buttons are drawn by Shopify with the colors of each payment provider.</p>'''),
    ('How do I offer pre-orders?', '''
<p>Set the variant to continue selling when out of stock in the product admin. At 0 stock its buttons read Pre-order, or
the label you set in <a href="theme-settings.html#ts-pre-order">Theme settings, Pre-order</a>. To take a deposit or charge
later, use a pre-order app.</p>'''),
    ('How do I hide the breadcrumbs on one page?', '''
<p>Set <strong>Breadcrumbs on this page</strong> to Hide in the main section of that page, or turn them off for the whole
store in <a href="theme-settings.html#ts-breadcrumbs">Theme settings, Breadcrumbs</a>.</p>'''),
    ('How do I translate my store?', '''
<p>Add and publish your languages in Settings, Languages. Balm Studio's own texts are already translated into French,
German, Italian and Spanish. Translate what you typed in the editor with Shopify's Translate and Adapt app.</p>'''),
]



# ------------------------------------------------------------------ blocks
THEME_BLOCKS_INTRO = ('<p>General purpose blocks accepted by Image with text and Rich text. Stack them in any order to '
                      'build a column of content.</p>')
THEME_BLOCK_TEXT = {
    'heading': '<p>A heading, set in the heading font. <strong>Heading level (semantic)</strong> sets its level for search engines and screen readers without changing its size.</p>',
    'text': '<p>A paragraph of rich text, with an optional maximum width.</p>',
    'button': '<p>A link shown as a Solid or Outline button, or as an underlined text link.</p>',
    'image': '<p>An image with a ratio, a width per device and an optional height limit.</p>',
    'spacer': '<p>Empty space, with its own height on desktop and on phones.</p>',
    'liquid': '<p>Your own Liquid or HTML. See <a href="custom-code.html">Custom code</a>.</p>',
    '_inline-product': '<p>In a Rich text set to the Statement style, places the cutout of a <strong>Product</strong> in the line of the paragraph, leaning by <strong>Tilt</strong>.</p>',
}

MEGA_INTRO = ('<p>A mega menu is a panel that opens under a top item of the main menu on desktop. Add a <strong>Mega menu</strong> '
              'block to the Header, type the exact title of that menu item in <strong>Linked menu item</strong> and choose its '
              '<strong>Layout</strong>. On phones the menu sheet lists the Main links instead.</p>')
MEGA_TEXT = {
    '_mega-menu': '<p>The panel itself. <strong>Layout</strong> builds it from the sub-links of the linked menu item: Index (the categories set large with their product count, the products of the category in view and a preview of the product in its colors, as on the demo Shop menu), Chapters (Promo blocks without an image as numbered chapters, each linked to the sub-link of the menu item at its place, as on the demo Rituals menu), Links and images, Images only or Links only; or from the blocks you add inside it, with Custom blocks.</p>',
    '_mega-column': '<p>A list of links from a menu: all its links, or only those under a <strong>Parent link</strong>, with an optional heading.</p>',
    '_mega-image': '<p>An image with an optional caption, subtitle and link. Nothing shows on your store without a picture.</p>',
    '_mega-cards': '<p>A row of picture cards. With <strong>Image source</strong> on Automatic, each card shows what a sub-link of the linked menu item points to: a collection, a product with its price, a blog post, or a page through its <code>custom.image</code> metafield. With Custom cards, it shows the Image card blocks you add inside it.</p>',
    '_mega-card': '<p>One card of an Image cards block set to Custom cards: an image, a heading, a subtitle, a link and an optional button label.</p>',
    '_mega-products': '<p>A few products as small cards with their image, title and price.</p>',
    '_mega-promo': '<p>An image tile with a heading, a short text and a link.</p>',
    '_mega-banner': '<p>A wide banner with a background image, a heading, a short text and a link.</p>',
}

META_MORE = '''
<h2 id="typed-keys">Metafields you type by key</h2>
<p>A few settings are text fields where you type the <code>namespace.key</code> yourself instead of using the dynamic
source icon.</p>
<div class="table-wrap"><table class="plain">
<thead><tr><th scope="col">Where</th><th scope="col">What to type</th><th scope="col">Metafield type</th></tr></thead>
<tbody>
<tr><td>Theme settings, Quick view: <strong>Short description metafield</strong></td><td>For example <code>custom.short_description</code></td><td>Single line or multi-line text on products. Without it, quick view shows the first paragraph of the description.</td></tr>
<tr><td>Compare products, Row block: <strong>Metafield</strong>, with <strong>Source</strong> on Metafield</td><td>The name, for example <q>Texture</q>, or the key, for example <code>custom.texture</code></td><td>Any type: each one is drawn as such. See <a href="#compare">Compare products rows</a>.</td></tr>
</tbody></table></div>

<h2 id="product-lists">Product list metafields</h2>
<p>The <strong>Products</strong> setting of the Product upsell block, of the Complementary products block and of the
cart recommendations can be connected to a product metafield of type Product, set to accept a list of products, so each
product carries its own selection. <strong>Products come from</strong> must then be on A manual selection.</p>

<h2 id="compare">Compare products rows</h2>
<p>Each Row block of Compare products with <strong>Source</strong> on Metafield reads the product metafield you name in
its <strong>Metafield</strong> setting, on every compared product. Type the name of the metafield, exactly as it shows in
<strong>Settings, Custom data, Products</strong> (<q>Skin type</q>), or its key (<code>custom.skin_type</code>). The field
takes no dynamic source on purpose: a connected metafield would give the value of the product of the page in every
column. Every type is drawn as such: true or false as icons, a list as a sentence, a number with the row's
<strong>Unit</strong>, a rating out of its scale, a color with its swatch, a reference by its title. A product without a
value shows a hyphen. The other sources (Vendor, Product type, Tags, SKU, Barcode, Weight and Unit price) read the
product's own fields.</p>

<h2 id="not-connectable">Settings that cannot be connected</h2>
<p>Shopify allows connections on colors, texts, rich texts, images, videos, links, pages, collections, products and
metaobjects only. Sliders, checkboxes, dropdowns, the color scheme and Liquid code are the same for the whole template.
When one product needs a different value for one of those, give it a
<a href="product-page.html#second-template">second product template</a>.</p>
'''

# ------------------------------------------------------------------ Features
FEATURES_LEAD = ('The features that span several sections or the whole store: what they do, where to turn them on and '
                 'what to know before you rely on them.')

FEATURES = '''
<section class="entry" id="quick-view-entry">
<h2 id="quick-view">Quick view</h2>
<p>Quick view opens a product in a sheet from its tile, so shoppers choose a variant and add it to the cart without
leaving the page. The sheet wears the colors of the product and shows its gallery, its price, its rating, the same
variant picker as the product page, the add to cart button, pickup availability, a short description and a link to the
full product page.</p>
<ol class="steps">
  <li>Open a section that shows tiles: Collection, Featured collection, Search, Recently viewed or Lookbook.</li>
  <li>Set <strong>Quick view</strong> to Show on hover or Always show. The tile then shows the word Quick view.</li>
  <li>In <a href="theme-settings.html#ts-quick-view">Theme settings, Quick view</a>, choose what the sheet shows.</li>
</ol>
<p>Without JavaScript the word opens the product page.</p>
</section>

<section class="entry" id="product-badges-entry">
<h2 id="product-badges">Product badges</h2>
<p>Four badges can appear on tiles, in quick view, in Compare products and on the product page. Each states a fact of the
product. Their position and the text of the Sale badge are set in
<a href="theme-settings.html#ts-product-badges">Theme settings, Product badges</a>.</p>
<ul>
  <li><strong>Sale</strong>: when the variant shown has a compare-at price above its price. It reads Sale, the percentage off or the amount saved.</li>
  <li><strong>Sold out</strong>: when the product can no longer be bought. It replaces Sale and New.</li>
  <li><strong>New</strong>: off by default; on, for products with a tag (<code>new</code> on the demo) or created in the last days you set.</li>
  <li><strong>Custom</strong>: the text of the product's <code>custom.badge_label</code> metafield.</li>
</ul>
<p>Sections that show tiles have a <strong>Badges</strong> setting (All, Automatic only, Custom only or None). On the
product page, the Badge block and <strong>Badges on media</strong> of the Product section show them.</p>
</section>

<section class="entry" id="tile-rating-swatches-entry">
<h2 id="tile-rating-swatches">Ratings and swatches on tiles</h2>
<p>In the <a href="section-main-collection.html">Collection</a> section, <strong>Show the product rating</strong> prints the
rating of each product above its name, with the number of reviews, read as on the product page (see
<a href="index.html#ratings">Product ratings</a>). <strong>Show color swatches</strong> draws the values of the first
option named in <strong>Swatch option name</strong> (Color, Colour or Couleur by default) with the swatch saved on each
value in your admin, or as a word when a value has none. Each swatch is a link to its variant, up to <strong>Maximum
swatches before "+N"</strong>, in the <strong>Swatch size</strong> and <strong>Swatch shape</strong> you choose. Both
settings are off by default.</p>
</section>

<section class="entry" id="grid-and-index-entry">
<h2 id="grid-and-index">Grid and Index views</h2>
<p>The Collection section shows its products as a grid of tiles in their colors, or as an index: rows of names set large,
each previewing its product as you point at it. <strong>Default view on desktop</strong> and <strong>Default view on
mobile</strong> choose the view; <strong>Let visitors switch between Grid and Index</strong> adds the two words to the
tools, and the choice is kept while the visitor browses. See <a href="section-main-collection.html">Collection</a>.</p>
</section>

<section class="entry" id="collection-columns-entry">
<h2 id="collection-columns">Column selector</h2>
<p>The Collection section can let shoppers choose how many products they see per row. <strong>Columns (desktop)</strong>
and <strong>Columns (mobile)</strong> set the starting layout; <strong>Let visitors change the column count
(desktop)</strong> and <strong>(mobile)</strong> add the buttons. Each device keeps its own choice for the rest of the
visit. Both are off by default.</p>
</section>

<section class="entry" id="pagination-entry">
<h2 id="pagination">Pagination</h2>
<p>The Collection and Search sections have a <strong>Pagination</strong> setting with three modes: Page numbers, Load
more button, or Infinite scroll, where the next page is added as the shopper reaches the end of the grid and a Load more
button takes over after three pages so the footer stays reachable.</p>
</section>

<section class="entry" id="header-colors-entry">
<h2 id="header-colors">Header colors</h2>
<p>The header takes the surface of the section under it, Field, Deep, Paper, a color scheme or an image, with its text
and the announcement bar kept readable. It hides on the way down and comes back on the way up. There is nothing to set
per section. See <a href="section-header.html">Header</a>.</p>
</section>

<section class="entry" id="gift-wrapping-entry">
<h2 id="gift-wrapping">Gift wrapping</h2>
<p>Adds a gift wrapping checkbox, and an optional gift message, to the cart drawer and the cart page. Checking the box
adds your wrapping product to the cart in quantity 1 and records the cart attribute Gift wrapping: Yes; the message is
saved as the cart attribute Gift message. Both appear on the order in your admin.</p>
<ol class="steps">
  <li>Create a product for the wrapping, for example <q>Gift wrapping</q>, with its price and an image, available on the Online Store, and keep it out of your collections.</li>
  <li>In <a href="theme-settings.html#ts-gift-wrapping">Theme settings, Gift wrapping</a>, turn on <strong>Offer gift wrapping</strong> and pick it as the <strong>Wrapping product</strong>.</li>
  <li>Adjust the label, the help text, the gift message and where it shows.</li>
</ol>
<p>The wrapping line stays at quantity 1, and a cart that holds only the wrapping is emptied.</p>
</section>

<section class="entry" id="age-verifier-entry">
<h2 id="age-verifier">Age verifier</h2>
<p>A window that asks visitors to confirm their age before they browse the store, on every page of the online store,
never at checkout.</p>
<ol class="steps">
  <li>In <a href="theme-settings.html#ts-age-verifier">Theme settings, Age verifier</a>, turn on <strong>Enable the age verifier</strong>.</li>
  <li>Set the <strong>Minimum age</strong>. Fields left empty use the translated storefront text.</li>
  <li>Choose what happens when the visitor declines, and how long the answer is remembered.</li>
  <li>Add a background image if you like, and turn on <strong>Preview in the theme editor</strong> to see it while you edit.</li>
</ol>
<p>The age verifier is a self-declaration, not an identity check: make sure it meets the rules that apply to your
products where you sell.</p>
</section>

<section class="entry" id="pre-order-entry">
<h2 id="pre-order">Pre-order</h2>
<p>A variant becomes a pre-order when its quantity is tracked, its stock is at 0 and Continue selling when out of stock is
checked in the product admin. Its buttons then read Pre-order, or the <strong>Button label</strong> of
<a href="theme-settings.html#ts-pre-order">Theme settings, Pre-order</a>, and it keeps the accelerated checkout buttons.
The Stock status block keeps its own text. The order is paid at checkout like any other: to take a deposit or charge
later, use a pre-order app whose options show in the Purchase options block.</p>
</section>

<section class="entry" id="combined-listings-entry">
<h2 id="combined-listings">Combined listings</h2>
<p>Combined listings group separate products into one listing, for example one product per size, on Shopify Plus stores
with Shopify's Combined Listings app. On the product page, picking a value that belongs to another product of the
listing switches the page to that product without a reload, keeping the values already chosen. In quick view, such a
value loads that product into the sheet.</p>
</section>

<section class="entry" id="lookbook-entry">
<h2 id="lookbook">Lookbook</h2>
<p>The <a href="more-sections.html#s-lookbook">Lookbook</a> section turns a photo into a shop: each point on the image
opens a product, with its quick add; on a phone, a tap opens it as a sheet. Add one Hotspot block per product and place
it in percent of the image, desktop and mobile apart. With <strong>Layout</strong> on Image with product list, the
products line up beside the image.</p>
</section>

<section class="entry" id="compare-products-entry">
<h2 id="compare-products">Compare products</h2>
<p>The <a href="more-sections.html#s-compare-products">Compare products</a> section sets up to five products side by
side. Built in rows show the price, the availability, the vendor and the rating; each Row block you add reads one fact
on every product, from a metafield you name or from a field of the product. <strong>Highlight differences</strong> marks
the rows where products differ, and <strong>Mobile layout</strong> shows cards or a table that scrolls. See
<a href="metafields.html#compare">Metafields, Compare products rows</a>.</p>
</section>

<section class="entry" id="recently-viewed-entry">
<h2 id="recently-viewed">Recently viewed</h2>
<p>The product page records each product a visitor opens, in that visitor's own browser, and the
<a href="more-sections.html#s-recently-viewed">Recently viewed</a> section shows them, newest first. Nothing is sent to a
server. The section takes no space until the visitor has a history. <strong>Exclude the current product</strong> and
<strong>Maximum products</strong> shape the list.</p>
</section>

<section class="entry" id="type-sizes-entry">
<h2 id="type-sizes">Type sizes</h2>
<p>Every text sits on one fluid type scale: a size is reached at 390 px wide for its mobile value and at 1440 px for its
desktop value, and grows in a straight line in between. To make the whole store read larger or smaller, move
<strong>Heading scale</strong> or <strong>Body scale</strong> in <a href="theme-settings.html#ts-typography">Theme settings,
Typography</a>: they multiply every size, those set in sections included. Product names and prices on tiles are set in
<a href="theme-settings.html#ts-tiles">Theme settings, Tiles</a>.</p>
</section>

<section class="entry" id="page-width-entry">
<h2 id="page-width">Page width</h2>
<p><strong>Page width</strong> in <a href="theme-settings.html#ts-layout">Theme settings, Layout</a> sets how wide the
shopping pages grow: the product page and the collection and search pages. Standard, Wide, or Full width with margins,
which fills the screen less the side margins. The other sections set their width with
<a href="sections.html#section-width">Section width</a>.</p>
</section>

<section class="entry" id="back-to-top-entry">
<h2 id="back-to-top">Back to top</h2>
<p>A Back to top link at the end of every page, just before the footer, set in
<a href="theme-settings.html#ts-back-to-top">Theme settings, Back to top</a>. It works without JavaScript, and goes up at
once for visitors who ask for reduced motion.</p>
</section>

<section class="entry" id="translations-entry">
<h2 id="translations">Translations</h2>
<p>Balm Studio ships in English, French, German, Italian and Spanish: every storefront text of the theme and the theme
editor itself, which follows the language of your admin. Add and publish your languages in Settings, Languages, then
translate the content you typed in the editor with Shopify's Translate and Adapt app. To change the wording of a theme
text, use Edit default theme content in the theme's <strong>...</strong> menu in your theme library.</p>
</section>
'''
