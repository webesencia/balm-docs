"""Prose of the Custom code and Support pages."""
SUPPORT_FORM = 'https://form.jotform.com/262695466571066'


# ------------------------------------------------------------------ Custom code
CODE_LEAD = ('Undertone is built to be shaped from the theme editor, without code. If you or a developer do edit the theme '
             'code, read this page first.')

CUSTOM_CODE = '''
<div class="callout callout--warn" role="note">
  <p class="callout__title">Duplicate the theme before any code change</p>
  <p>Before you edit a single file, make a copy of the theme: in your admin, go to <strong>Online Store, Themes</strong>,
  open the <strong>...</strong> menu of Undertone and choose <strong>Duplicate</strong>. Make your changes on the copy, preview
  it, and publish it only once it works. Your live theme stays untouched, and you can go back to it at any moment.</p>
</div>

<h2 id="hire-a-partner">Get help from a Shopify Partner</h2>
<p>Code customizations are outside the scope of Undertone support. For custom features, design changes or integrations, we
recommend working with a Shopify Partner: developers and agencies vetted by Shopify, listed in the
<a href="https://www.shopify.com/partners/directory">Shopify Partner Directory</a>.</p>

<h2 id="before-coding">Try the editor first</h2>
<p>Many changes need no edit to the theme files:</p>
<ul>
  <li>The <a href="more-sections.html#s-custom-liquid">Custom Liquid</a> section, and the Liquid blocks of the product page and of the content sections, accept your own Liquid, HTML and app snippets.</li>
  <li>Shopify's <strong>Custom CSS</strong> field, at the bottom of each section's settings and in Theme settings, takes CSS scoped to that section or to the whole store.</li>
  <li>The <a href="more-sections.html#s-apps">Apps</a> section and app blocks place app content without touching the code.</li>
</ul>
<p>Code added this way is kept when you update the theme.</p>

<h2 id="updates-and-code">Theme updates and your code</h2>
<p>When you update Undertone, Shopify installs the new version as a separate copy and carries over your theme editor settings
and content, but not the changes you made in the theme files. Keep a list of every file you changed and why, so the
changes can be applied again to the new version.</p>

<h2 id="support-scope">What support covers</h2>
<p>Undertone support covers the theme as shipped. When a problem shows up on a theme whose code was modified, we may ask you
to reproduce it on an unmodified copy of Undertone first. See <a href="support.html">Support</a>.</p>
'''


# ------------------------------------------------------------------ Support
SUPPORT_LEAD = 'Undertone support answers questions about the theme and fixes its bugs. Here is what it covers and how to reach it.'

SUPPORT = f'''
<p class="cta"><a class="button" href="{SUPPORT_FORM}" rel="noopener">Contact Undertone support</a></p>

<h2 id="covered">What support covers</h2>
<ul>
  <li><strong>Bugs</strong> in the theme as shipped: something that does not work as this documentation describes.</li>
  <li><strong>Questions</strong> about the theme: installing it, its settings, sections, blocks and features, and how to reach a result with them.</li>
</ul>

<h2 id="not-covered">What support does not cover</h2>
<ul>
  <li><strong>Customizations</strong>: changes to the theme code, new features, custom designs, or code added in Custom Liquid sections, Liquid blocks or Custom CSS. For this work we recommend a <a href="https://www.shopify.com/partners/directory">Shopify Partner</a>.</li>
  <li>Problems caused by edits to the theme files. We may ask you to reproduce the problem on an unmodified copy of Undertone.</li>
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
