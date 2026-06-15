#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Patch ADITIVO dos hubs do Estephano para a aula 7 (hub ja em sincronia 1-6).
PROF: card IN CLASS (link standalone) + stamp7 + ex-lesson-7 + complementares l7 + audioMap + totalLessons=7.
ALUNO: ESPELHO do prof -> ex-lesson-7 + complementares l7 + stamp7 + audioMap + totalLessons=7
       (o hub do aluno tem so 2 abas: Pre-class + Complementares -- sem IN CLASS, REGRA 3).
Aulas passadas nao sao reescritas (so insercao). Idempotente: aborta se ja aplicado.
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
PROF = os.path.join(ROOT, 'public', 'professor', 'estephano-akihito-ishii.html')
ALUNO = os.path.join(ROOT, 'public', 'aluno', 'estephano-akihito-ishii.html')

AUDIO_BASE = '/audio/estephano-akihito-ishii/'
preclass7 = open(os.path.join(HERE, 'preclass.html'), encoding='utf-8').read().strip()
comp7 = open(os.path.join(HERE, 'complementary.html'), encoding='utf-8').read().strip()

# --- audioMap entries (do hub_snippets section 4) + [order-l7] ---
snip = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()
m = re.search(r'4\. ENTRADAS de audioMap.*?<script>\n(.*?)</script>', snip, re.S)
amap_lines = m.group(1).rstrip('\n')
amap_lines += f'\n  "[order-l7]": "{AUDIO_BASE}a7_order_weekend.mp3",'

CARD7 = ('    <a href="/professor/estephano-akihito-ishii-aula7.html?autostart=1" style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);border:1px solid rgba(200,200,190,.5);border-radius:12px;cursor:pointer;transition:all .2s;text-decoration:none;color:inherit" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
         '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">07</div>\n'
         '      <div><div style="font-weight:600;font-size:.95rem">My Free Time</div><div style="font-size:.8rem;color:var(--text-dim)">like + verb-ing -- 28 slides</div></div>\n'
         '    </a>\n')
STAMP7 = '\n      <div class="stamp" id="stamp7" data-label="Aula 7" style="background-image:url(\'https://images.unsplash.com/photo-1511512578047-dfb367046420?w=200&q=80\')"></div>'


def add_audiomap(s, entries):
    i = s.index('var audioMap')
    j = s.index('};', i)
    return s[:j] + entries + '\n' + s[j:]


def set_totallessons(s):
    return re.sub(r'var totalLessons\s*=\s*\d+', 'var totalLessons = 7', s)


def add_stamp7(s):
    i = s.index('id="stamp6"')
    e = s.index('></div>', i) + len('></div>')
    return s[:e] + STAMP7 + s[e:]


def patch_prof():
    s = open(PROF, encoding='utf-8').read()
    assert 'id="ex-lesson-7"' not in s, 'PROF ja tem ex-lesson-7 (abortando)'
    # 1. card IN CLASS
    a = '\n  </div>\n</div>\n\n<!-- ═══════════════════ TAB 4: COMPLEMENTARES'
    assert s.count(a) == 1, f'anchor card IN CLASS nao unico ({s.count(a)})'
    s = s.replace(a, '\n' + CARD7 + a, 1)
    # 2. stamp7
    s = add_stamp7(s)
    # 3. ex-lesson-7
    mk = '<!-- /lesson-card aula 6 -->'
    assert s.count(mk) == 1, f'marker aula 6 nao unico ({s.count(mk)})'
    s = s.replace(mk, mk + '\n\n' + preclass7 + '\n<!-- /lesson-card aula 7 -->', 1)
    # 4. complementares l7
    ca = '\n  </div>\n</div>\n\n</div><!-- /container -->'
    assert s.count(ca) == 1, f'anchor comp PROF nao unico ({s.count(ca)})'
    s = s.replace(ca, '\n' + comp7 + ca, 1)
    # 5. audioMap + totalLessons
    s = add_audiomap(s, amap_lines)
    s = set_totallessons(s)
    open(PROF, 'w', encoding='utf-8').write(s)
    print('PROF: ex-lesson-7', s.count('id="ex-lesson-7"'), '| stamp7', s.count('id="stamp7"'),
          '| l7 media', s.count('data-media="l7-'), '| card7', s.count('aula7.html?autostart=1'),
          '| totalLessons', re.search(r'var totalLessons\s*=\s*(\d+)', s).group(1))


def patch_aluno():
    s = open(ALUNO, encoding='utf-8').read()
    assert 'id="ex-lesson-7"' not in s, 'ALUNO ja tem ex-lesson-7'
    # ex-lesson-7 apos aula 6
    mk = '<!-- /lesson-card aula 6 -->'
    assert s.count(mk) == 1, f'marker aula 6 nao unico no ALUNO ({s.count(mk)})'
    s = s.replace(mk, mk + '\n\n' + preclass7 + '\n<!-- /lesson-card aula 7 -->', 1)
    # complementares l7
    ca = '\n  </div>\n</div>\n\n</div><!-- /container -->'
    assert s.count(ca) == 1, f'anchor comp ALUNO nao unico ({s.count(ca)})'
    s = s.replace(ca, '\n' + comp7 + ca, 1)
    # stamp7 + audioMap + totalLessons
    s = add_stamp7(s)
    s = add_audiomap(s, amap_lines)
    s = set_totallessons(s)
    open(ALUNO, 'w', encoding='utf-8').write(s)
    print('ALUNO: ex-lesson', re.findall(r'id="ex-lesson-(\d)"', s), '| stamp7', s.count('id="stamp7"'),
          '| l7 media', s.count('data-media="l7-'),
          '| totalLessons', re.search(r'var totalLessons\s*=\s*(\d+)', s).group(1),
          '| order-l7 in amap', '[order-l7]' in s)


if __name__ == '__main__':
    patch_prof()
    patch_aluno()
    print('OK')
