"""Reads the Balm theme schemas and resolves every t: key to its English label."""
import glob
import json
import os
import re

LOC = {}


def t(v):
    if isinstance(v, str) and v.startswith('t:'):
        cur = LOC
        for p in v[2:].split('.'):
            if not isinstance(cur, dict) or p not in cur:
                return '??' + v
            cur = cur[p]
        return cur
    return v


def schema_of(path):
    src = open(path, encoding='utf-8').read()
    m = re.search(r'{%-?\s*schema\s*-?%}(.*?){%-?\s*endschema\s*-?%}', src, re.S)
    return json.loads(m.group(1)) if m else None


def norm_setting(s):
    out = {'type': s.get('type'), 'id': s.get('id')}
    for k in ('label', 'info', 'content', 'placeholder'):
        if k in s: out[k] = t(s[k])
    if 'default' in s: out['default'] = t(s['default']) if isinstance(s['default'], str) else s['default']
    for k in ('min', 'max', 'step', 'unit'):
        if k in s: out[k] = t(s[k]) if k == 'unit' else s[k]
    if 'options' in s: out['options'] = [{'value': o['value'], 'label': t(o['label'])} for o in s['options']]
    if 'visible_if' in s: out['visible_if'] = s['visible_if']
    return out


def norm_schema(sc):
    if sc is None: return None
    out = {'name': t(sc.get('name')), 'settings': [norm_setting(s) for s in sc.get('settings', [])]}
    for k in ('class', 'tag', 'limit', 'max_blocks', 'enabled_on', 'disabled_on'):
        if k in sc: out[k] = sc[k]
    out['blocks'] = []
    for b in sc.get('blocks', []):
        nb = {'type': b.get('type'), 'name': t(b.get('name')) if b.get('name') else None, 'settings': [norm_setting(s) for s in b.get('settings', [])]}
        if 'limit' in b: nb['limit'] = b['limit']
        out['blocks'].append(nb)
    out['presets'] = [{'name': t(p.get('name')), 'category': t(p.get('category')) if p.get('category') else None} for p in sc.get('presets', [])]
    return out


def extract(theme):
    """Returns the settings groups, sections and blocks of the theme with resolved labels."""
    LOC.clear()
    LOC.update(json.load(open(os.path.join(theme, 'locales', 'en.default.schema.json'), encoding='utf-8')))
    data = {'settings': [], 'sections': {}, 'blocks': {}}
    for g in json.load(open(os.path.join(theme, 'config', 'settings_schema.json'), encoding='utf-8')):
        if g['name'] == 'theme_info':
            continue
        data['settings'].append({'name': t(g['name']), 'settings': [norm_setting(s) for s in g['settings']]})
    for p in sorted(glob.glob(os.path.join(theme, 'sections', '*.liquid'))):
        data['sections'][os.path.basename(p)[:-7]] = norm_schema(schema_of(p))
    for p in sorted(glob.glob(os.path.join(theme, 'blocks', '*.liquid'))):
        data['blocks'][os.path.basename(p)[:-7]] = norm_schema(schema_of(p))
    unresolved = sorted(set(re.findall(r'\?\?t:[\w.]+', json.dumps(data, ensure_ascii=False))))
    if unresolved:
        raise SystemExit('unresolved translation keys: ' + ', '.join(unresolved[:10]))
    return data
