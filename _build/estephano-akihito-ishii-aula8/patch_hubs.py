#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Patch ADITIVO dos hubs do Estephano para a aula 8 (hub ja em sincronia 1-7).
PROF: card IN CLASS (link standalone) + stamp8 + ex-lesson-8 + complementares l8 + audioMap + totalLessons=8.
ALUNO: ESPELHO do prof -> ex-lesson-8 + complementares l8 + stamp8 + audioMap + totalLessons=8
       (o hub do aluno tem so 2 abas: Pre-class + Complementares -- sem IN CLASS, REGRA 3).
Aulas passadas nao sao reescritas (so insercao). Idempotente: aborta se ja aplicado.
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
PROF = os.path.join(ROOT, 'public', 'professor', 'estephano-akihito-ishii.html')
ALUNO = os.path.join(ROOT, 'public', 'aluno', 'estephano-akihito-ishii.html')

AUDIO_BASE = '/audio/estephano-akihito-ishii/'
preclass8 = open(os.path.join(HERE, 'preclass.html'), encoding='utf-8').read().strip()
comp8 = open(os.path.join(HERE, 'complementary.html'), encoding='utf-8').read().strip()

# --- audioMap entries (do hub_snippets section 4) + [order-l8] ---
snip = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()
m = re.search(r'4\. ENTRADAS de audioMap.*?<script>\n(.*?)</script>', snip, re.S)
amap_lines = m.group(1).rstrip('\n')
amap_lines += f'\n  "[order-l8]": "{AUDIO_BASE}a8_order_party.mp3",'

CARD8 = ('    <a href="/professor/estephano-akihito-ishii-aula8.html?autostart=1" style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);border:1px solid rgba(200,200,190,.5);border-radius:12px;cursor:pointer;transition:all .2s;text-decoration:none;color:inherit" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
         '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">08</div>\n'
         '      <div><div style="font-weight:600;font-size:.95rem">Block 1 Review</div><div style="font-size:.8rem;color:var(--text-dim)">Meet someone new -- 28 slides</div></div>\n'
         '    </a>\n')
STAMP8 = '\n      <div class="stamp" id="stamp8" data-label="Aula 8" style="background-image:url(\'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=200&q=80\')"></div>'


def add_audiomap(s, entries):
    i = s.index('var audioMap')
    j = s.index('};', i)
    return s[:j] + entries + '\n' + s[j:]


def set_totallessons(s):
    return re.sub(r'var totalLessons\s*=\s*\d+', 'var totalLessons = 8', s)


def add_stamp8(s):
    i = s.index('id="stamp7"')
    e = s.index('></div>', i) + len('></div>')
    return s[:e] + STAMP8 + s[e:]


def patch_prof():
    s = open(PROF, encoding='utf-8').read()
    assert 'id="ex-lesson-8"' not in s, 'PROF ja tem ex-lesson-8 (abortando)'
    # 1. card IN CLASS
    a = '\n  </div>\n</div>\n\n<!-- ═══════════════════ TAB 4: COMPLEMENTARES'
    assert s.count(a) == 1, f'anchor card IN CLASS nao unico ({s.count(a)})'
    s = s.replace(a, '\n' + CARD8 + a, 1)
    # 2. stamp8
    s = add_stamp8(s)
    # 3. ex-lesson-8
    mk = '<!-- /lesson-card aula 7 -->'
    assert s.count(mk) == 1, f'marker aula 7 nao unico ({s.count(mk)})'
    s = s.replace(mk, mk + '\n\n' + preclass8 + '\n<!-- /lesson-card aula 8 -->', 1)
    # 4. complementares l8
    ca = '\n  </div>\n</div>\n\n</div><!-- /container -->'
    assert s.count(ca) == 1, f'anchor comp PROF nao unico ({s.count(ca)})'
    s = s.replace(ca, '\n' + comp8 + ca, 1)
    # 5. audioMap + totalLessons
    s = add_audiomap(s, amap_lines)
    s = set_totallessons(s)
    open(PROF, 'w', encoding='utf-8').write(s)
    print('PROF: ex-lesson-8', s.count('id="ex-lesson-8"'), '| stamp8', s.count('id="stamp8"'),
          '| l8 media', s.count('data-media="l8-'), '| card8', s.count('aula8.html?autostart=1'),
          '| totalLessons', re.search(r'var totalLessons\s*=\s*(\d+)', s).group(1))


def patch_aluno():
    s = open(ALUNO, encoding='utf-8').read()
    assert 'id="ex-lesson-8"' not in s, 'ALUNO ja tem ex-lesson-8'
    # ex-lesson-8 apos aula 7
    mk = '<!-- /lesson-card aula 7 -->'
    assert s.count(mk) == 1, f'marker aula 7 nao unico no ALUNO ({s.count(mk)})'
    s = s.replace(mk, mk + '\n\n' + preclass8 + '\n<!-- /lesson-card aula 8 -->', 1)
    # complementares l8
    ca = '\n  </div>\n</div>\n\n</div><!-- /container -->'
    assert s.count(ca) == 1, f'anchor comp ALUNO nao unico ({s.count(ca)})'
    s = s.replace(ca, '\n' + comp8 + ca, 1)
    # stamp8 + audioMap + totalLessons
    s = add_stamp8(s)
    s = add_audiomap(s, amap_lines)
    s = set_totallessons(s)
    open(ALUNO, 'w', encoding='utf-8').write(s)
    print('ALUNO: ex-lesson', re.findall(r'id="ex-lesson-(\d)"', s), '| stamp8', s.count('id="stamp8"'),
          '| l8 media', s.count('data-media="l8-'),
          '| totalLessons', re.search(r'var totalLessons\s*=\s*(\d+)', s).group(1),
          '| order-l8 in amap', '[order-l8]' in s)


if __name__ == '__main__':
    patch_prof()
    patch_aluno()
    print('OK')
