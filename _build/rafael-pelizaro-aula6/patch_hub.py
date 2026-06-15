#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Patch aditivo do hub (prof + aluno) para a aula 6 do Rafael Pelizaro.
Insere: stamp6, accordion ex-lesson-6, card IN CLASS (so prof), bloco complementares l6,
entradas pc6_ no audioMap (+ [order-l6]) e totalLessons 5->6. NAO toca aulas anteriores."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))

preclass = open(os.path.join(HERE, 'preclass.html'), encoding='utf-8').read().rstrip('\n')
complementary = open(os.path.join(HERE, 'complementary.html'), encoding='utf-8').read().rstrip('\n')
manifest = json.load(open(os.path.join(HERE, 'audio_manifest.json'), encoding='utf-8'))

AUDIO_BASE = '/audio/rafael-pelizaro/'
# entradas do audioMap que o HUB precisa: so as do Pre-class (pc6_) + [order-l6]
amap_lines = []
for e in manifest:
    if e['file'].startswith('pc6_'):
        amap_lines.append(f'  {json.dumps(e["text"], ensure_ascii=False)}: {json.dumps(AUDIO_BASE + e["file"])},')
order_file = next(e['file'] for e in manifest if e['file'] == 'a6_order_disagree_steps.mp3')
amap_lines.append(f'  {json.dumps("[order-l6]")}: {json.dumps(AUDIO_BASE + order_file)},')
amap_block = '\n'.join(amap_lines)

STAMP5 = ('<div class="stamp" id="stamp5" data-label="Sprint" '
          'style="background-image:url(\'https://images.unsplash.com/photo-1531482615713-2afd69097998?w=200&q=80\')"></div>')
STAMP6 = ('<div class="stamp" id="stamp6" data-label="Pushback" '
          'style="background-image:url(\'https://images.unsplash.com/photo-1573497491208-6b1acb260507?w=200&q=80\')"></div>')

INCLASS_CARD5_END = (
    '      <div><div style="font-weight:600;font-size:.95rem">The Sprint Review -- Technical Updates for Non-Tech People</div>'
    '<div style="font-size:.8rem;color:var(--text-dim)">Past Simple + Simplification -- 32 slides</div></div>\n'
    '    </a>')
INCLASS_CARD6 = (
    '\n    <a href="/professor/rafael-pelizaro-aula6.html#slides" target="_blank" '
    'style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);'
    'backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;'
    'transition:all .3s;text-decoration:none;color:inherit" onmouseover="this.style.borderColor=\'var(--accent)\'" '
    'onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
    '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;'
    'align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">06</div>\n'
    '      <div><div style="font-weight:600;font-size:.95rem">Handling Pushback -- Disagreeing Professionally</div>'
    '<div style="font-size:.8rem;color:var(--text-dim)">First Conditional + Opinion Frames -- 28 slides</div></div>\n'
    '    </a>')


def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    orig = s
    # 1. stamp6
    assert s.count(STAMP5) == 1, f'{path}: stamp5 anchor x{s.count(STAMP5)}'
    s = s.replace(STAMP5, STAMP5 + '\n' + STAMP6, 1)
    # 2. accordion ex-lesson-6 (antes do fim da tab-exercises)
    assert 'id="ex-lesson-6"' not in s, f'{path}: ja tem ex-lesson-6'
    marker = '</div><!-- /tab-exercises -->'
    assert s.count(marker) == 1, f'{path}: marker tab-exercises x{s.count(marker)}'
    s = s.replace(marker, preclass + '\n' + marker, 1)
    # 3. card IN CLASS (so prof)
    if is_prof:
        assert s.count(INCLASS_CARD5_END) == 1, f'{path}: inclass card5 anchor x{s.count(INCLASS_CARD5_END)}'
        s = s.replace(INCLASS_CARD5_END, INCLASS_CARD5_END + INCLASS_CARD6, 1)
    # 4. complementares l6
    cmarker = '</div><!-- /tab-complementary -->'
    assert s.count(cmarker) == 1, f'{path}: marker tab-complementary x{s.count(cmarker)}'
    s = s.replace(cmarker, complementary + '\n' + cmarker, 1)
    # 5. audioMap pc6 + order
    amarker = 'var audioMap = {'
    assert s.count(amarker) == 1, f'{path}: audioMap anchor x{s.count(amarker)}'
    s = s.replace(amarker, amarker + '\n' + amap_block, 1)
    # 6. totalLessons 5 -> 6
    assert s.count('var totalLessons=5;') == 1, f'{path}: totalLessons anchor'
    s = s.replace('var totalLessons=5;', 'var totalLessons=6;', 1)
    assert s != orig
    open(path, 'w', encoding='utf-8').write(s)
    print(f'  patched {os.path.relpath(path, ROOT)} (+{len(s)-len(orig)} bytes)')


patch(os.path.join(ROOT, 'public', 'professor', 'rafael-pelizaro.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'rafael-pelizaro.html'), False)
print('OK')
