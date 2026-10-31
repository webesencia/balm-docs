// Captures of the demo store for the documentation, from the preview of the development
// theme: each view at 1440 x 900 (name-desktop.jpg) and 390 x 844 (name-mobile.jpg), in
// assets/shots/. Needs the theme repository's harness for Playwright and Chrome, and the
// storefront password in STOREFRONT_PASSWORD.
//
//   HARNESS=/path/to/balm-theme/harness node _tools/shots.mjs          every capture
//   ONLY=header,texture node _tools/shots.mjs                          some of them
import fs from 'fs';
import path from 'path';

const HERE = path.dirname(new URL(import.meta.url).pathname);
const OUT = path.join(HERE, '..', 'assets', 'shots');
const HARNESS = process.env.HARNESS || '/Users/david/Documents/fresh-backup/harness';
const { chromium, CHROME } = await import(path.join(HARNESS, 'lib.mjs'));
const BASE = process.env.BASE || 'https://balm-skin-2.myshopify.com';
const PT = 'preview_theme_id=' + (process.env.THEME_ID || '206639268177');
const ONLY = (process.env.ONLY || '').split(',').filter(Boolean);
const wait = (ms) => new Promise((r) => setTimeout(r, ms));

// name: [path, how], how: sel (scrolled to the top of the screen, less offset screens),
// y (screens from the top), hover or click (a selector), hover2 (a second hover, in an open panel), slide (the product gallery on that slide), cart (a product added first),
// d / m (desktop only, phone only).
const SHOTS = {
  'hero-sequence': ['/', { y: 0, settle: 2200 }],
  campaign: ['/', { sel: '.camp' }],
  'color-library': ['/', { sel: '.lib', hover: '.lib__band:nth-child(3)', settle: 1800 }],
  lineup: ['/', { sel: '.lu' }],
  'day-in-color': ['/', { sel: '.day' }],
  'routine-builder': ['/', { sel: '.build' }],
  reviews: ['/', { sel: '.voices', screens: -0.1 }],
  'hue-finder': ['/', { sel: '.hf', settle: 1600 }],
  atelier: ['/', { sel: '.atelier' }],
  'tone-footer': ['/', { sel: '.tft' }],
  header: ['/', { y: 0, hover: '.header__nav-item.has-mega', hover2: '[data-mmi-cat="all"]', d: true, settle: 1500 }],
  'header-sheet': ['/', { y: 0, click: '.header__burger', m: true, settle: 1500 }],
  'main-product': ['/products/lavender-night-renewal', { y: 0, settle: 1500 }],
  'main-product-gallery': ['/products/lavender-night-renewal', { y: 0, slide: 1, settle: 1500 }],
  'main-product-passport': ['/products/lavender-night-renewal', { sel: '.mp-sp__list', screens: -0.2 }],
  // The illustrations (texture, texture-gel and the three below) were taken on
  // 2026-10-31 before the texture photos (T65): to take them again, set Source on
  // Illustration in the editor first, else they show the photos.
  'texture-photo': ['/products/lavender-night-renewal', { sel: '.txr', settle: 2600 }],
  texture: ['/products/lavender-night-renewal', { sel: '.txr', settle: 2200 }],
  'texture-gel': ['/products/rosewater-calm-gel', { sel: '.txr', settle: 2200 }],
  'texture-cream': ['/products/oat-comfort-cleanser', { sel: '.txr', settle: 2200 }],
  'texture-fluid': ['/products/blossom-day-fluid-spf-30', { sel: '.txr', settle: 2200 }],
  'texture-serum': ['/products/sage-balance-serum', { sel: '.txr', settle: 2200 }],
  'sticky-atc': ['/products/lavender-night-renewal', { y: 1.6, m: true, settle: 1500 }],
  'main-collection': ['/collections/all', { y: 0 }],
  'main-collection-all': ['/collections/sun-care', { sel: '.mc2__main' }],
  'main-collection-index': ['/collections/all', { y: 0, click: '[data-mc2-view="index"]', settle: 1500 }],
  chapters: ['/pages/about', { y: 0 }],
  'ingredient-atlas': ['/pages/about', { sel: '.atl' }],
  numbers: ['/pages/about', { sel: '.nums' }],
  'main-contact': ['/pages/contact', { y: 0 }],
  'main-journal': ['/blogs/journal', { y: 0 }],
  'main-journal-article': ['/blogs/journal/why-we-only-make-seven-formulas', { y: 0 }],
  'cart-drawer': ['/products/lavender-night-renewal', { y: 0, cart: true, click: '.header__action--cart', settle: 1800 }],
};

fs.mkdirSync(OUT, { recursive: true });
const browser = await chromium.launch({ executablePath: CHROME });
const written = [];
for (const [w, h, suffix] of [[1440, 900, 'desktop'], [390, 844, 'mobile']]) {
  const ctx = await browser.newContext({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
  // The preview bar, the cookie banner and the reserved scrollbar gutter of a headless
  // browser are not part of the store.
  await ctx.addInitScript(() => { addEventListener('DOMContentLoaded', () => { const st = document.createElement('style'); st.textContent = '#PBarNextFrameWrapper,#preview-bar-iframe,#shopify-pc__banner,.shopify-pc__banner__dialog{display:none!important}html{scrollbar-gutter:auto!important}'; document.head.appendChild(st); }); });
  const page = await ctx.newPage();
  await page.goto(BASE + '/password', { waitUntil: 'domcontentloaded' });
  if (await page.$('input[type="password"]')) {
    await page.fill('input[type="password"]', process.env.STOREFRONT_PASSWORD || '');
    await Promise.all([page.waitForNavigation({ waitUntil: 'domcontentloaded' }), page.press('input[type="password"]', 'Enter')]);
  }
  for (const [name, [at, o]] of Object.entries(SHOTS)) {
    if (ONLY.length && !ONLY.includes(name)) continue;
    if (o.d && suffix === 'mobile') continue;
    if (o.m && suffix === 'desktop') continue;
    try {
      if (o.cart) {
        await page.goto(`${BASE}${at}?${PT}`, { waitUntil: 'load' });
        await page.evaluate(async () => { await fetch('/cart/clear.js', { method: 'POST' }); const v = document.querySelector('form[action*="/cart/add"] [name="id"]'); if (v) await fetch('/cart/add.js', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ items: [{ id: +v.value, quantity: 1 }] }) }); });
      }
      await page.goto(`${BASE}${at}${at.includes('?') ? '&' : '?'}${PT}`, { waitUntil: 'load', timeout: 90000 });
      await page.mouse.move(2, h - 2);
      await wait(1500);
      let top = null;
      if (o.sel) {
        top = await page.evaluate(([s, k]) => { const el = document.querySelector(s); return el ? el.getBoundingClientRect().top + scrollY + k * innerHeight : null; }, [o.sel, o.screens || 0]);
        if (top === null) { console.log('missing', name, suffix, o.sel); continue; }
      } else if (o.y != null) {
        top = o.y * h;
      }
      if (top !== null) {
        // In steps, so the scripts that follow the scroll keep up.
        await page.evaluate(async (t) => { const from = scrollY, n = 12; for (let i = 1; i <= n; i++) { scrollTo(0, from + (t - from) * i / n); await new Promise((r) => setTimeout(r, 30)); } }, Math.max(0, top));
      }
      if (o.hover) { const el = await page.$(o.hover); if (el) await el.hover(); else console.log('no hover target', name, suffix); }
      if (o.slide != null) await page.evaluate((i) => document.querySelector('main-product').setActiveIndex(i), o.slide);
      if (o.hover2) { await wait(700); const el = await page.$(o.hover2); if (el) await el.hover(); else console.log('no hover target', name, suffix); }
      if (o.click) { const el = await page.$(o.click); if (el) await el.click(); else console.log('no click target', name, suffix); }
      await wait(o.settle || 1300);
      const file = path.join(OUT, `${name}-${suffix}.jpg`);
      await page.screenshot({ path: file, type: 'jpeg', quality: 80 });
      written.push(path.basename(file));
      if (o.cart) await page.evaluate(() => fetch('/cart/clear.js', { method: 'POST' }));
    } catch (e) {
      console.log('failed', name, suffix, e.message.split('\n')[0]);
    }
  }
  await ctx.close();
}
await browser.close();
console.log('written', written.length, written.join(' '));
