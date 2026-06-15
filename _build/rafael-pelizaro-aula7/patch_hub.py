#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Patch aditivo do hub (prof + aluno) para a aula 7 do Rafael Pelizaro.
Insere: stamp7, accordion ex-lesson-7, card IN CLASS (so prof), bloco complementares l7,
entradas pc7_ no audioMap (+ [order-l7]) e totalLessons 6->7. NAO toca aulas anteriores."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))

preclass = open(os.path.join(HERE, 'preclass.html'), encoding='utf-8').read().rstrip('\n')
complementary = open(os.path.join(HERE, 'complementary.html'), encoding='utf-8').read().rstrip('\n')
manifest = json.load(open(os.path.join(HERE, 'audio_manifest.json'), encoding='utf-8'))

AUDIO_BASE = '/audio/rafael-pelizaro/'
# entradas do audioMap que o HUB precisa: so as do Pre-class (pc7_) + [order-l7]
amap_lines = []
for e in manifest:
    if e['file'].startswith('pc7_'):
        amap_lines.append(f'  {json.dumps(e["text"], ensure_ascii=False)}: {json.dumps(AUDIO_BASE + e["file"])},')
order_file = next(e['file'] for e in manifest if e['file'] == 'a7_order_present_steps.mp3')
amap_lines.append(f'  {json.dumps("[order-l7]")}: {json.dumps(AUDIO_BASE + order_file)},')
amap_block = '\n'.join(amap_lines)

STAMP6 = ('<div class="stamp" id="stamp6" data-label="Pushback" '
          'style="background-image:url(\'https://images.unsplash.com/photo-1573497491208-6b1acb260507?w=200&q=80\')"></div>')
STAMP7 = ('<div class="stamp" id="stamp7" data-label="Boardroom" '
          'style="background-image:url(\'https://images.unsplash.com/photo-1560439514-4e9645039924?w=200&q=80\')"></div>')

INCLASS_CARD6_END = (
    '      <div><div style="font-weight:600;font-size:.95rem">Handling Pushback -- Disagreeing Professionally</div>'
    '<div style="font-size:.8rem;color:var(--text-dim)">First Conditional + Opinion Frames -- 28 slides</div></div>\n'
    '    </a>')
INCLASS_CARD7 = (
    '\n    <a href="/professor/rafael-pelizaro-aula7.html#slides" target="_blank" '
    'style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);'
    'backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;'
    'transition:all .3s;text-decoration:none;color:inherit" onmouseover="this.style.borderColor=\'var(--accent)\'" '
    'onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
    '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;'
    'align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">07</div>\n'
    '      <div><div style="font-weight:600;font-size:.95rem">The Board Presentation -- Executive Communication</div>'
    '<div style="font-size:.8rem;color:var(--text-dim)">Connectors + Formal Register -- 28 slides</div></div>\n'
    '    </a>')


def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    orig = s
    # 1. stamp7
    assert s.count(STAMP6) == 1, f'{path}: stamp6 anchor x{s.count(STAMP6)}'
    s = s.replace(STAMP6, STAMP6 + '\n' + STAMP7, 1)
    # 2. accordion ex-lesson-7 (antes do fim da tab-exercises)
    assert 'id="ex-lesson-7"' not in s, f'{path}: ja tem ex-lesson-7'
    marker = '</div><!-- /tab-exercises -->'
    assert s.count(marker) == 1, f'{path}: marker tab-exercises x{s.count(marker)}'
    s = s.replace(marker, preclass + '\n' + marker, 1)
    # 3. card IN CLASS (so prof)
    if is_prof:
        assert s.count(INCLASS_CARD6_END) == 1, f'{path}: inclass card6 anchor x{s.count(INCLASS_CARD6_END)}'
        s = s.replace(INCLASS_CARD6_END, INCLASS_CARD6_END + INCLASS_CARD7, 1)
    # 4. complementares l7
    cmarker = '</div><!-- /tab-complementary -->'
    assert s.count(cmarker) == 1, f'{path}: marker tab-complementary x{s.count(cmarker)}'
    s = s.replace(cmarker, complementary + '\n' + cmarker, 1)
    # 5. audioMap pc7 + order
    amarker = 'var audioMap = {'
    assert s.count(amarker) == 1, f'{path}: audioMap anchor x{s.count(amarker)}'
    s = s.replace(amarker, amarker + '\n' + amap_block, 1)
    # 6. totalLessons 6 -> 7
    assert s.count('var totalLessons=6;') == 1, f'{path}: totalLessons anchor'
    s = s.replace('var totalLessons=6;', 'var totalLessons=7;', 1)
    assert s != orig
    open(path, 'w', encoding='utf-8').write(s)
    print(f'  patched {os.path.relpath(path, ROOT)} (+{len(s)-len(orig)} bytes)')


patch(os.path.join(ROOT, 'public', 'professor', 'rafael-pelizaro.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'rafael-pelizaro.html'), False)
print('OK')
