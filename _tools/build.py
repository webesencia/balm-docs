"""Builds the Balm documentation site from the theme's schemas.

Usage, from the repository root: python3 _tools/build.py /path/to/balm-theme

Labels, options, defaults, help texts and the changelog come from the theme (English
locale of the schema); the prose comes from the content_*.py files next to this one.
The pages are written to the repository root.
"""
import html
import json
import os
import re
import sys
from html.parser import HTMLParser

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
OUT = os.path.dirname(HERE)
if len(sys.argv) < 2 or not os.path.isfile(os.path.join(sys.argv[1], 'config', 'settings_schema.json')):
    raise SystemExit('usage: python3 _tools/build.py /path/to/balm-theme')
THEME = os.path.abspath(sys.argv[1])

import extract  # noqa: E402

D = extract.extract(THEME)
RAW_SETTINGS = json.load(open(f'{THEME}/config/settings_schema.json', encoding='utf-8'))
LOC = json.load(open(f'{THEME}/locales/en.default.schema.json', encoding='utf-8'))

import content_pages as CP  # noqa: E402
import content_product as CPR  # noqa: E402
import content_sections as CS  # noqa: E402
import content_settings as CST  # noqa: E402


def e(s):
    return html.escape(str(s), quote=True)


def t(v):
    if isinstance(v, str) and v.startswith('t:'):
        cur = LOC
        for p in v[2:].split('.'):
            cur = cur[p]
        return cur
    return v


# ---------------------------------------------------------------- setting formatting
TYPE_NAMES = {
    'checkbox': 'Checkbox', 'text': 'Text', 'textarea': 'Multi-line text', 'richtext': 'Rich text',
    'inline_richtext': 'Rich text', 'html': 'HTML', 'liquid': 'Liquid code', 'color': 'Color',
    'color_background': 'Gradient', 'color_scheme': 'Color scheme', 'font_picker': 'Font',
    'image_picker': 'Image', 'video': 'Shopify-hosted video', 'video_url': 'YouTube or Vimeo URL',
    'url': 'Link', 'link_list': 'Menu', 'product': 'Product', 'product_list': 'Product list',
    'collection': 'Collection', 'collection_list': 'Collection list', 'page': 'Page',
    'blog': 'Blog', 'article': 'Article', 'number': 'Number', 'text_alignment': 'Left, center or right',
    'metaobject': 'Metaobject', 'range': 'Slider', 'select': 'Choice', 'radio': 'Choice',
}
NBSP = ' '


def unit_str(u):
    return {'px': ' px', '%': '%', 'ms': ' ms', 's': ' s', 'd': ' days', 'vh': ' vh'}.get(u, (' ' + u) if u else '')


def font_name(handle):
    m = re.match(r'(.+)_([ni])(\d)$', handle or '')
    if not m:
        return handle
    name = ' '.join(w.capitalize() for w in m.group(1).split('_'))
    name = name.replace('Dm ', 'DM ')
    style = ' italic' if m.group(2) == 'i' else ''
    return f'{name} {int(m.group(3)) * 100}{style}'


def fmt_values(s):
    ty = s['type']
    if ty in ('select', 'radio'):
        return '<ul class="opts">' + ''.join(f'<li>{e(o["label"])}</li>' for o in s['options']) + '</ul>'
    if ty == 'range':
        txt = f'{s["min"]} to {s["max"]}{unit_str(s.get("unit"))}'
        if s.get('step') not in (1, None):
            txt += f', step {s["step"]}'
        return e(txt)
    return e(TYPE_NAMES.get(ty, ty))


def strip_tags(s):
    return re.sub(r'<[^>]+>', '', s or '').strip()


def fmt_default(s):
    ty = s['type']
    has = 'default' in s and s['default'] is not None
    d = s.get('default')
    info = (s.get('info') or '').lower()
    if ty == 'checkbox':
        return 'On' if d else 'Off'
    if ty in ('select', 'radio', 'text_alignment'):
        if ty == 'text_alignment':
            return e(str(d).capitalize()) if has else ''
        for o in s.get('options', []):
            if str(o['value']) == str(d):
                return e(o['label'])
        return e(d) if has else ''
    if ty == 'range':
        return e(f'{d}{unit_str(s.get("unit"))}') if has else ''
    if ty == 'number':
        return e(d) if has else 'Empty'
    if ty == 'color':
        if not has or str(d).replace(' ', '') in ('rgba(0,0,0,0)', 'transparent', ''):
            return 'None'
        return f'<span class="swatch" style="background:{e(d)}"></span><code>{e(str(d).upper())}</code>'
    if ty == 'color_scheme':
        m = re.match(r'scheme-(\d+)', str(d or ''))
        return f'Scheme {m.group(1)}' if m else ''
    if ty == 'font_picker':
        return e(font_name(d))
    if ty in ('text', 'textarea', 'richtext', 'inline_richtext'):
        if has and strip_tags(str(d)):
            txt = strip_tags(str(d))
            if len(txt) > 70:
                txt = txt[:67].rsplit(' ', 1)[0] + '...'
            return '<q>' + e(txt) + '</q>'
        if 'translated' in info:
            return 'Translated text'
        return 'Empty'
    if ty in ('url',) and has:
        return f'<code>{e(d)}</code>'
    return 'Empty' if not has else e(d)


# ---------------------------------------------------------------- visible_if in words
CLAUSE = re.compile(r"^(settings|section\.settings|block\.settings)\.(\w+)(?:\s*(==|!=)\s*('([^']*)'|blank|false|true))?$")


def cond_text(vis, own, parent):
    if not vis:
        return ''
    body = vis.strip()
    if not (body.startswith('{{') and body.endswith('}}')):
        return ''
    body = body[2:-2].strip()
    joiners = re.findall(r'\s(and|or)\s', body)
    clauses = re.split(r'\s(?:and|or)\s', body)
    words = []
    for c in clauses:
        m = CLAUSE.match(c.strip())
        if not m:
            return ''
        scope, sid, op, rhs, val = m.groups()
        if scope == 'settings':
            pools = [GLOBAL_SETTINGS]
        elif scope == 'section.settings' and parent is not None:
            pools = [parent, own]
        else:
            pools = [own]
        target = next((x for pool in pools for x in pool if x.get('id') == sid), None)
        if target is None:
            return ''
        label = target.get('label') or sid
        if op is None:
            words.append(f'{label} is on' if target['type'] == 'checkbox' else f'{label} is set')
        elif rhs == 'blank':
            words.append(f'{label} is {"empty" if op == "==" else "set"}')
        elif rhs in ('false', 'true'):
            on = (rhs == 'true') == (op == '==')
            words.append(f'{label} is {"on" if on else "off"}')
        else:
            opt = next((o['label'] for o in target.get('options', []) if str(o['value']) == val), None)
            if opt is None:
                return ''
            words.append(f'{label} is {"" if op == "==" else "not "}{opt}')
    out = words[0]
    for j, w in zip(joiners, words[1:]):
        out += f' {j} {w}'
    return 'Shown when ' + out + '.'


GLOBAL_SETTINGS = [s for g in D['settings'] for s in g['settings']]

# ---------------------------------------------------------------- settings tables
BG_HEADERS = {'Section background', 'Solid color settings', 'Gradient settings', 'Image settings', 'Radial halo settings'}
BG_IDS = {'bg_type', 'bg_fallback_color', 'bg_color', 'bg_gradient_from', 'bg_gradient_to', 'bg_gradient_angle',
          'bg_image', 'bg_section_image', 'bg_overlay_color', 'bg_overlay_opacity', 'bg_radial_base', 'bg_radial_halo',
          'bg_radial_position', 'bg_radial_size_d', 'bg_radial_size_m', 'bg_radial_spread'}


# An info text may carry Markdown links to the merchant's admin ([text](/admin/...)), which
# the theme editor renders as links. The docs have no admin to link to: the text is kept.
ADMIN_LINK = re.compile(r'\[([^\]]+)\]\((/admin/[^)]*)\)')


def setting_row(s, own, parent):
    info = ADMIN_LINK.sub(r'\1', s.get('info') or '')
    cond = cond_text(s.get('visible_if'), own, parent)
    notes = e(info)
    if cond:
        notes += (' ' if notes else '') + f'<span class="cond">{e(cond)}</span>'
    return (f'<tr><th scope="row" data-label="Setting">{e(s.get("label") or s.get("id"))}</th>'
            f'<td data-label="Values">{fmt_values(s)}</td>'
            f'<td data-label="Default">{fmt_default(s)}</td>'
            f'<td data-label="Notes">{notes}</td></tr>')


def settings_table(settings, parent=None, collapse_bg=False, scheme_definition=None):
    rows = []
    in_bg = False
    bg_done = False
    more_done = False
    count = 0
    for s in settings:
        ty = s['type']
        if ty == 'header':
            in_bg = collapse_bg and s['content'] in BG_HEADERS
            more_done = False
            if in_bg:
                if not bg_done:
                    rows.append('<tr class="group"><th colspan="4" scope="colgroup">Section background</th></tr>')
                    rows.append('<tr class="note"><td colspan="4">Background mode (None, Solid color, Gradient, Image or Radial halo) '
                                'and the settings of each mode. They are the same in every section: see '
                                '<a href="sections.html#section-background">Section background</a>.</td></tr>')
                    bg_done = True
                continue
            rows.append(f'<tr class="group"><th colspan="4" scope="colgroup">{e(s["content"])}</th></tr>')
            continue
        if ty == 'paragraph':
            if in_bg:
                continue
            rows.append(f'<tr class="note"><td colspan="4">{e(s["content"])}</td></tr>')
            continue
        if in_bg and s.get('id') in BG_IDS:
            count += 1
            continue
        if in_bg and not more_done:
            # A setting placed after the background group without a header of its own.
            rows.append('<tr class="group"><th colspan="4" scope="colgroup">More settings</th></tr>')
            more_done = True
        if ty == 'color_scheme_group':
            for dfn in scheme_definition or []:
                dd = {'type': dfn['type'], 'id': dfn['id'], 'label': t(dfn['label']), 'info': t(dfn.get('info', '')),
                      'default': dfn.get('default')}
                rows.append(setting_row(dd, settings, parent))
                count += 1
            continue
        rows.append(setting_row(s, settings, parent))
        count += 1
    table = ('<div class="table-wrap"><table class="settings"><thead><tr>'
             '<th scope="col">Setting</th><th scope="col">Values</th><th scope="col">Default</th><th scope="col">Notes</th>'
             '</tr></thead><tbody>' + ''.join(rows) + '</tbody></table></div>')
    return table, count


def details(label, table, count, open_=False):
    return (f'<details class="settings-details"{" open" if open_ else ""}><summary>{e(label)} '
            f'<span class="count">({count})</span></summary>{table}</details>')


# ---------------------------------------------------------------- slugs, availability
def slug(s):
    s = s.lower().replace('&', 'and')
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s


TEMPLATE_NAMES = {'product': 'product', 'collection': 'collection', 'search': 'search', 'cart': 'cart',
                  'blog': 'blog', 'article': 'article', 'page': 'page', '404': '404', 'password': 'password',
                  'gift_card': 'gift card', 'list-collections': 'list of collections', 'index': 'home page'}


def availability(key, sc):
    en = sc.get('enabled_on') or {}
    dis = sc.get('disabled_on') or {}
    if key == 'cart-drawer':
        return 'Part of every page. It is listed in the theme editor and cannot be removed or moved.'
    if 'templates' in en:
        names = ', '.join(TEMPLATE_NAMES.get(x, x) for x in en['templates'])
        if not sc['presets']:
            return f'Part of the {names} template.'
        return f'Only on {names} templates.'
    if en.get('groups') == ['header']:
        return 'Header group only.'
    if en.get('groups') == ['footer']:
        return 'Footer group only.'
    if dis.get('groups') == ['*']:
        return 'Any template. Not available in the header or footer group.'
    if dis.get('groups') and set(dis['groups']) >= {'header', 'footer'}:
        return 'Any template. Not available in the header or footer group.'
    return 'Any template, and the header and footer groups.'


# ---------------------------------------------------------------- mini markdown (changelog)
def inline_md(s):
    s = e(s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
    return s


def markdown(md, id_prefix='v'):
    out, para, items = [], [], []
    cur_item = None

    def flush_para():
        if para:
            out.append('<p>' + inline_md(' '.join(para)) + '</p>')
            para.clear()

    def flush_list():
        nonlocal cur_item
        if cur_item is not None:
            items.append(cur_item)
            cur_item = None
        if items:
            out.append('<ul>' + ''.join('<li>' + inline_md(i) + '</li>' for i in items) + '</ul>')
            items.clear()

    for line in md.splitlines():
        if line.startswith('# '):
            continue
        if line.startswith('## ') or line.startswith('### '):
            flush_para(); flush_list()
            level = 2 if line.startswith('## ') else 3
            text = line[level + 1:].strip()
            out.append(f'<h{level} id="{id_prefix}-{slug(text)}">{inline_md(text)}</h{level}>')
        elif line.startswith('- '):
            flush_para()
            if cur_item is not None:
                items.append(cur_item)
            cur_item = line[2:].strip()
        elif line.startswith('  ') and cur_item is not None and line.strip():
            cur_item += ' ' + line.strip()
        elif not line.strip():
            flush_para(); flush_list()
        else:
            flush_list()
            para.append(line.strip())
    flush_para(); flush_list()
    return '\n'.join(out)


# ---------------------------------------------------------------- pages
PAGES = [
    ('index.html', 'Getting started', 'Install Balm and set up your store, step by step.'),
    ('theme-settings.html', 'Theme settings', 'Every group of Balm theme settings, explained in the order of the theme editor.'),
    ('sections.html', 'Sections', 'Every Balm section, its settings and a typical use.'),
    ('product-page.html', 'Product page blocks', 'The Balm product page, its blocks, buy button styles and backgrounds.'),
    ('features.html', 'Features', 'Quick view, badges, page loader, age verifier, gift wrapping and the other Balm features.'),
    ('metafields.html', 'Metafields', 'The product and shop metafields Balm reads, with their keys and types.'),
    ('custom-code.html', 'Custom code', 'What to know before editing the Balm theme code.'),
    ('faq.html', 'FAQ', 'Answers to the questions merchants ask most about Balm.'),
    ('changelog.html', 'Changelog', 'What changed in each version of Balm.'),
    ('support.html', 'Support', 'What Balm support covers and how to reach it.'),
]


class Outline(HTMLParser):
    """Collects h2/h3/h4 with ids and the text that follows each, for the nav and the search index."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.entries = []
        self.cur = None
        self.in_h = None
        self.skip = 0
        self.in_table_td = False
        self.in_label = False
        self.stack = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ('h2', 'h3', 'h4') and a.get('id'):
            self.cur = {'level': int(tag[1]), 'id': a['id'], 'title': '', 'text': [], 'labels': []}
            self.entries.append(self.cur)
            self.in_h = tag
        if tag == 'td':
            self.in_table_td = True
        if tag == 'th' and a.get('scope') == 'row' and self.cur is not None:
            self.in_label = True
            self.cur['labels'].append('')
        if tag in ('script', 'style', 'thead', 'summary'):
            self.skip += 1

    def handle_endtag(self, tag):
        if tag == self.in_h:
            self.in_h = None
        if tag == 'td':
            self.in_table_td = False
        if tag == 'th':
            self.in_label = False
        if tag in ('script', 'style', 'thead', 'summary'):
            self.skip -= 1

    def handle_data(self, data):
        if self.skip or self.cur is None:
            return
        if self.in_h:
            self.cur['title'] += data
        elif self.in_label:
            self.cur['labels'][-1] += data
        elif not self.in_table_td:
            self.cur['text'].append(data)


def layout(fname, title, desc, body, toc, root=''):
    # root prefixes every page and asset URL. Pages sit at the domain root and link
    # relatively (root ''); the 404 is served for any missing path, however deep, so
    # it links from the domain root (root '/').
    nav = []
    for f, label, _ in PAGES:
        cur = f == fname
        cls = ' class="current"' if cur else ''
        aria = ' aria-current="page"' if cur else ''
        item = f'<li{cls}><a href="{root}{f}"{aria}>{e(label)}</a>'
        if cur and toc:
            item += '<ul class="toc">' + ''.join(f'<li><a href="#{i}">{e(tt)}</a></li>' for i, tt in toc) + '</ul>'
        item += '</li>'
        nav.append(item)
    idx = [p[0] for p in PAGES].index(fname) if fname in [p[0] for p in PAGES] else None
    pager = ''
    if idx is not None:
        prev_p = PAGES[idx - 1] if idx > 0 else None
        next_p = PAGES[idx + 1] if idx + 1 < len(PAGES) else None
        pager = '<nav class="pager" aria-label="Previous and next page">'
        pager += (f'<a class="prev" href="{root}{prev_p[0]}"><span>Previous</span>{e(prev_p[1])}</a>' if prev_p else '<span></span>')
        pager += (f'<a class="next" href="{root}{next_p[0]}"><span>Next</span>{e(next_p[1])}</a>' if next_p else '<span></span>')
        pager += '</nav>'
    page_title = f'{title} | Balm theme documentation' if fname != 'index.html' else 'Balm theme documentation'
    return f'''<!doctype html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(page_title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="icon" href="{root}assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="{root}assets/inter-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{root}assets/style.css">
<script>document.documentElement.classList.replace('no-js', 'js');</script>
<script src="{root}assets/search-index.js" defer></script>
<script src="{root}assets/docs.js" defer></script>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="topbar">
  <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="sidebar"><span class="nav-toggle__bars" aria-hidden="true"></span><span class="nav-toggle__label">Menu</span></button>
  <a class="brand" href="{root}index.html"><span class="brand__mark" aria-hidden="true">B</span><span class="brand__name">Balm</span><span class="brand__sub">Documentation</span></a>
  <div class="search" role="search">
    <label class="visually-hidden" for="search-input">Search the documentation</label>
    <input id="search-input" type="search" placeholder="Search the docs" autocomplete="off" spellcheck="false" aria-describedby="search-hint" aria-controls="search-results">
    <kbd class="search__key" aria-hidden="true">/</kbd>
    <p id="search-hint" class="visually-hidden">Results appear below as you type. Use the arrow keys to move through them.</p>
    <div id="search-results" class="search-results" hidden></div>
  </div>
</header>
<div class="layout">
  <nav id="sidebar" class="sidebar" aria-label="Documentation">
    <ul class="nav">{"".join(nav)}</ul>
  </nav>
  <main id="main" class="content" tabindex="-1">
    <article class="doc">
{body}
    </article>
    {pager}
    <footer class="site-footer"><p>Balm theme documentation, version 1.0.0. Questions? See <a href="{root}support.html">Support</a>.</p></footer>
  </main>
</div>
</body>
</html>
'''


SEARCH = []


def write_page(fname, title, desc, body):
    parser = Outline()
    parser.feed(body)
    toc = [(x['id'], re.sub(r'\s+', ' ', x['title']).strip()) for x in parser.entries if x['level'] == 2]
    page_label = next(p[1] for p in PAGES if p[0] == fname) if fname in [p[0] for p in PAGES] else title
    lead = re.search(r'<p class="lead">(.*?)</p>', body, re.S)
    SEARCH.append({'t': title, 'p': page_label, 'u': fname, 'x': strip_tags(lead.group(1)) if lead else desc})
    parents = {}
    for x in parser.entries:
        ttl = re.sub(r'\s+', ' ', x['title']).strip()
        parents[x['level']] = ttl
        ctx = ' / '.join(parents[l] for l in range(2, x['level']) if l in parents)
        txt = re.sub(r'\s+', ' ', ' '.join(x['text'])).strip()
        labels = sorted({re.sub(r'\s+', ' ', l).strip() for l in x['labels'] if l.strip()})
        if fname == 'changelog.html' and x['level'] == 3:
            ttl = f'{ttl} ({parents.get(2, "")})'
        entry = {'t': ttl, 'p': page_label + (' / ' + ctx if ctx else ''), 'u': f'{fname}#{x["id"]}', 'x': txt[:1200]}
        if labels:
            entry['l'] = ' | '.join(labels)
        SEARCH.append(entry)
    with open(os.path.join(OUT, fname), 'w', encoding='utf-8') as fh:
        fh.write(layout(fname, title, desc, body, toc))


# ---------------------------------------------------------------- page bodies
def page_head(title, lead):
    return f'<header class="doc-head"><h1>{e(title)}</h1><p class="lead">{lead}</p></header>'


def build_theme_settings():
    parts = [page_head('Theme settings', CST.INTRO)]
    toc = []
    for g in D['settings']:
        gid = 'ts-' + slug(g['name'])
        toc.append((gid, g['name']))
    parts.append('<nav class="contents" aria-label="Setting groups"><h2 class="contents__title" id="groups">Setting groups</h2><ol class="contents__list contents__list--cols">'
                 + ''.join(f'<li><a href="#{i}">{e(n)}</a></li>' for i, n in toc) + '</ol></nav>')
    scheme_def = RAW_SETTINGS[1]['settings'][0]['definition']
    for g in D['settings']:
        gid = 'ts-' + slug(g['name'])
        prose = CST.GROUPS.get(g['name'])
        if prose is None:
            raise SystemExit('missing theme settings prose for ' + g['name'])
        table, count = settings_table(g['settings'], scheme_definition=scheme_def)
        parts.append(f'<section class="entry" id="{gid}-entry"><h2 id="{gid}">{e(g["name"])}</h2>{prose}'
                     + details('Settings', table, count, open_=True) + '</section>')
    write_page('theme-settings.html', 'Theme settings', PAGES[1][2], '\n'.join(parts))


def section_entry(key, heading_level=3):
    sc = D['sections'][key]
    txt = CS.TEXT.get(key)
    if txt is None:
        raise SystemExit('missing section prose for ' + key)
    desc, use = txt
    sid = 's-' + key
    h = f'h{heading_level}'
    out = [f'<section class="entry" id="{sid}-entry"><{h} id="{sid}">{e(sc["name"])}</{h}>']
    out.append(f'<p class="where"><span>Where</span>{e(availability(key, sc))}</p>')
    out.append(desc)
    if use:
        out.append(f'<p class="use"><strong>Typical use.</strong> {use}</p>')
    if key == 'main-product':
        out.append('<p>Its settings and every block are documented on <a href="product-page.html">Product page blocks</a>.</p>')
        out.append('</section>')
        return ''.join(out)
    if sc['settings']:
        table, count = settings_table(sc['settings'], collapse_bg=True)
        out.append(details('Section settings', table, count))
    for b in sc['blocks']:
        if b['type'] in ('@app', '@theme') or not b['name']:
            continue
        bt = CS.BLOCK_TEXT.get(f'{key}/{b["type"]}', '')
        out.append(f'<h4 id="{sid}-{slug(b["type"])}">Block: {e(b["name"])}</h4>{bt}')
        if b['settings']:
            table, count = settings_table(b['settings'], parent=sc['settings'])
            out.append(details(f'{b["name"]} block settings', table, count))
    extras = [b['type'] for b in sc['blocks'] if b['type'] in ('@app', '@theme')]
    notes = []
    if '@theme' in extras:
        notes.append('accepts the <a href="#theme-blocks">theme blocks</a> (Heading, Text, Button, Image, Spacer, Liquid)')
    if '@app' in extras:
        notes.append('accepts app blocks')
    if key == 'header':
        notes.append('holds <a href="#mega-menu-blocks">Mega menu blocks</a>')
    if notes:
        out.append('<p class="accepts">This section ' + ' and '.join(notes) + '.</p>')
    out.append('</section>')
    return ''.join(out)


def block_entry(key, title_prefix='', heading='h3', prose=None, id_prefix='tb-'):
    b = D['blocks'][key]
    bid = id_prefix + slug(key.lstrip('_'))
    out = [f'<section class="entry" id="{bid}-entry"><{heading} id="{bid}">{e(title_prefix + b["name"])}</{heading}>']
    if prose:
        out.append(prose)
    if b['settings']:
        table, count = settings_table(b['settings'])
        out.append(details('Block settings', table, count))
    kids = [x['type'] for x in b['blocks']]
    if kids:
        names = ', '.join(D['blocks'][k]['name'] for k in kids if k in D['blocks'])
        out.append(f'<p class="accepts">Accepts these blocks inside it: {e(names)}.</p>')
    out.append('</section>')
    return ''.join(out)


def build_sections():
    parts = [page_head('Sections', CS.INTRO)]
    cats = CS.CATEGORIES
    listed = [k for _, _, _, keys in cats for k in keys]
    missing = [k for k, v in D['sections'].items() if v and k not in listed and k not in CS.INTERNAL]
    if missing:
        raise SystemExit('sections not placed in a category: ' + ', '.join(missing))
    # contents
    cont = ['<nav class="contents" aria-label="All sections"><h2 class="contents__title" id="all-sections">All sections</h2><div class="contents__groups">']
    for cid, ctitle, _, keys in cats:
        cont.append(f'<div><h3 class="contents__group"><a href="#{cid}">{e(ctitle)}</a></h3><ul class="contents__list">'
                    + ''.join(f'<li><a href="#s-{k}">{e(D["sections"][k]["name"])}</a></li>' for k in keys) + '</ul></div>')
    cont.append('<div><h3 class="contents__group"><a href="#blocks">Blocks used inside sections</a></h3><ul class="contents__list">'
                '<li><a href="#theme-blocks">Theme blocks</a></li><li><a href="#mega-menu-blocks">Mega menu blocks</a></li></ul></div>')
    cont.append('</div></nav>')
    parts.append(''.join(cont))
    parts.append(CS.SHARED)
    for cid, ctitle, cintro, keys in cats:
        parts.append(f'<h2 id="{cid}">{e(ctitle)}</h2>{cintro}')
        for k in keys:
            parts.append(section_entry(k))
    parts.append(CS.INTERNAL_NOTE)
    parts.append(f'<h2 id="blocks">Blocks used inside sections</h2>{CS.BLOCKS_INTRO}')
    parts.append(f'<h3 id="theme-blocks">Theme blocks</h3>{CS.THEME_BLOCKS_INTRO}')
    for k in ['heading', 'text', 'button', 'image', 'spacer', 'liquid']:
        parts.append(block_entry(k, heading='h4', prose=CS.THEME_BLOCK_TEXT[k]))
    parts.append(f'<h3 id="mega-menu-blocks">Mega menu blocks</h3>{CS.MEGA_INTRO}')
    for k in ['_mega-menu', '_mega-column', '_mega-image', '_mega-products', '_mega-promo', '_mega-banner']:
        parts.append(block_entry(k, heading='h4', prose=CS.MEGA_TEXT[k], id_prefix='mm-'))
    write_page('sections.html', 'Sections', PAGES[2][2], '\n'.join(parts))


def build_product():
    parts = [page_head('Product page blocks', CPR.INTRO)]
    parts.append(CPR.BODY_BEFORE)
    sc = D['sections']['main-product']
    table, count = settings_table(sc['settings'], collapse_bg=False)
    parts.append(f'<h2 id="product-section-settings">Product section settings</h2>{CPR.SECTION_SETTINGS_INTRO}'
                 + details('Product section settings', table, count))
    parts.append(f'<h2 id="blocks">Blocks</h2>{CPR.BLOCKS_INTRO}')
    order = CPR.BLOCK_ORDER
    known = {k for k in D['blocks'] if k.startswith('_product-')}
    missing = known - set(order)
    if missing:
        raise SystemExit('product blocks without a place: ' + ', '.join(sorted(missing)))
    parts.append('<nav class="contents" aria-label="All blocks"><ul class="contents__list contents__list--cols">'
                 + ''.join(f'<li><a href="#pb-{slug(k.lstrip("_"))}">{e(D["blocks"][k]["name"])}</a></li>' for k in order)
                 + '</ul></nav>')
    for k in order:
        parts.append(block_entry(k, prose=CPR.BLOCK_TEXT[k], id_prefix='pb-'))
    parts.append(CPR.BODY_AFTER)
    write_page('product-page.html', 'Product page blocks', PAGES[3][2], '\n'.join(parts))


def build_changelog():
    md = open(f'{THEME}/CHANGELOG.md', encoding='utf-8').read()
    body = page_head('Changelog', 'What changed in each version of Balm. The version installed in your store is shown in your theme library, under the theme name.')
    body += markdown(md)
    write_page('changelog.html', 'Changelog', PAGES[8][2], body)


def build_simple(fname, idx, title, lead, body):
    write_page(fname, title, PAGES[idx][2], page_head(title, lead) + body)


def main():
    build_simple('index.html', 0, 'Getting started', CP.GS_LEAD, CP.GETTING_STARTED)
    build_theme_settings()
    build_sections()
    build_product()
    build_simple('features.html', 4, 'Features', CP.FEATURES_LEAD, CP.FEATURES)
    build_simple('metafields.html', 5, 'Metafields', CP.META_LEAD, CP.METAFIELDS)
    build_simple('custom-code.html', 6, 'Custom code', CP.CODE_LEAD, CP.CUSTOM_CODE)
    faq = ''.join(f'<section class="entry faq" id="{slug(q)[:60]}-entry"><h2 id="{slug(q)[:60]}">{e(q)}</h2>{a}</section>' for q, a in CP.FAQ)
    build_simple('faq.html', 7, 'FAQ', CP.FAQ_LEAD, faq)
    build_changelog()
    build_simple('support.html', 9, 'Support', CP.SUPPORT_LEAD, CP.SUPPORT)
    # 404 page for GitHub Pages
    with open(os.path.join(OUT, '404.html'), 'w', encoding='utf-8') as fh:
        fh.write(layout('404.html', 'Page not found', 'This page does not exist.',
                        page_head('Page not found', 'This page does not exist, or it has moved.')
                        + '<p>Try the search above, or start again from <a href="/index.html">Getting started</a>.</p>', [],
                        root='/'))
    with open(os.path.join(OUT, 'assets', 'search-index.js'), 'w', encoding='utf-8') as fh:
        fh.write('window.BALM_SEARCH=' + json.dumps(SEARCH, ensure_ascii=False, separators=(',', ':')) + ';\n')
    print('pages written, search entries:', len(SEARCH))


if __name__ == '__main__':
    main()
