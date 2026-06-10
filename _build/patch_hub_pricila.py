#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Patch genérico dos hubs (prof+aluno) da Pricila para a aula N.
Uso: python3 _build/patch_hub_pricila.py N
- accordion ex-lesson-N inline (recolhido) em tab-exercises
- audioMap entries da aula N (vírgula-safe)
- stampN em stamps-row
- var totalLessons -> N
- (prof) card no menu IN CLASS + handler #inclass (1x)
Idempotente: pula arquivo que já tem id="ex-lesson-N".
"""
import os, json, sys

N = int(sys.argv[1])
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
D = os.path.join(HERE, 'pricila-aula%d' % N)
meta = json.load(open(os.path.join(D, 'meta.json'), encoding='utf-8'))
preclass = open(os.path.join(D, 'preclass.html'), encoding='utf-8').read()
welcome = meta['welcome']
phrases = json.load(open(os.path.join(D, 'phrases.json'), encoding='utf-8'))
IMG = meta['stamp_img']
PREV_STAMP = {7:('Airport','photo-1436491865332-7a61a109cc05'),8:('Hotel','photo-1566073771259-6a8506099945'),
              9:('Transport','photo-1502602898657-3e91760cbb34'),10:('Dining','photo-1517248135467-4c7edcad34c4')}
prev_lbl, prev_img = PREV_STAMP[N]

ACCORDION = ('<div class="lesson-card" id="ex-lesson-%d">\n' % N
  + '  <div class="lesson-header" onclick="toggleLesson(this)">\n'
  + '    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/' + IMG + '?w=600&q=80\')"></div>\n'
  + '    <div class="lesson-header-content">\n      <div class="lesson-number">Aula %02d -- Pre-class</div>\n' % N
  + '      <h3>' + meta['accordion_h3'] + '</h3>\n      <div class="lesson-desc">' + meta['accordion_desc'] + '</div>\n'
  + '      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="%d" style="width:0%%"></div></div><span class="mini-percent" data-lesson-pct="%d">0%%</span></div>\n' % (N, N)
  + '    </div>\n    <div class="expand-icon">&#9660;</div>\n  </div>\n'
  + '  <div class="lesson-body">\n' + welcome + '\n' + preclass + '\n  </div>\n</div><!-- /lesson-card Aula %d -->\n' % N)

STAMP = '<div class="stamp" id="stamp%d" data-label="%s" style="background-image:url(\'https://images.unsplash.com/%s?w=200&q=80\')"></div>\n' % (N, meta['stamp_label'], IMG)

INCLASS_CARD = ('    <a href="/professor/pricila-adamo-aula%d.html?autostart=1" target="_blank" style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s;text-decoration:none;color:inherit" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n' % N
  + '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">%02d</div>\n' % N
  + '      <div><div style="font-weight:600;font-size:.95rem">' + meta['accordion_h3'] + '</div><div style="font-size:.8rem;color:var(--text-dim)">' + meta['card_sub'] + ' -- 29 slides</div></div>\n    </a>\n')

INCLASS_HASH = ('<script>\ndocument.addEventListener("DOMContentLoaded", function () {\n'
  '  if (window.location.hash === "#inclass") {\n    var b = document.querySelector(\'.tab-btn[onclick*="inclass"]\');\n    if (b) b.click();\n  }\n});\n</script>\n')

def audiomap_entries(existing):
    lines = []
    for p in phrases:
        k = json.dumps(p['key'], ensure_ascii=False)
        if (k + ':') in existing or (k + ' :') in existing: continue
        lines.append('  %s: %s' % (k, json.dumps('/audio/pricila-adamo/' + p['file'], ensure_ascii=False)))
    return (',\n'.join(lines) + ',\n') if lines else ''

def patch(path, is_prof):
    h = open(path, encoding='utf-8').read()
    if 'id="ex-lesson-%d"' % N in h:
        print('  skip (já tem):', path); return
    am_open = h.index('var audioMap = {'); am_close = h.index('};', am_open)
    region = h[am_open:am_close]; entries = audiomap_entries(region)
    if entries:
        last = region.rstrip()
        prefix = '' if (last.endswith(',') or last.endswith('{')) else ',\n'
        h = h[:am_close] + prefix + entries + h[am_close:]
    prev_stamp_html = '<div class="stamp" id="stamp%d" data-label="%s" style="background-image:url(\'https://images.unsplash.com/%s?w=200&q=80\')"></div>\n' % (N-1, prev_lbl, prev_img)
    assert prev_stamp_html in h, 'stamp%d nao encontrado em %s' % (N-1, path)
    h = h.replace(prev_stamp_html, prev_stamp_html + STAMP, 1)
    marker = '</div><!-- /tab-exercises -->'
    assert marker in h
    h = h.replace(marker, ACCORDION + '\n' + marker, 1)
    h = h.replace('var totalLessons = %d;' % (N-1), 'var totalLessons = %d;' % N)
    if is_prof:
        prev_href = '<a href="/professor/pricila-adamo-aula%d.html?autostart=1"' % (N-1)
        idx = h.index(prev_href); close = h.index('</a>', idx) + len('</a>') + 1
        h = h[:close] + INCLASS_CARD + h[close:]
        if 'location.hash === "#inclass"' not in h:
            h = h.replace('</body>', INCLASS_HASH + '</body>', 1)
    open(path, 'w', encoding='utf-8').write(h)
    print('  patched:', path, '(+%d audioMap)' % entries.count('/audio/'))

patch(os.path.join(ROOT, 'public', 'professor', 'pricila-adamo.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'pricila-adamo.html'), False)
print('hub patch aula %d done' % N)
