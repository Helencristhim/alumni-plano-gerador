#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Patch ADITIVO dos hubs do Estephano para a aula 6.
PROF: card IN CLASS (link standalone) + stamp6 + ex-lesson-6 + complementares l6 + audioMap + totalLessons=6.
ALUNO: ESPELHO do prof -> adiciona ex-lesson-5 (dessync) + ex-lesson-6 + complementares l5+l6 +
       stamp6 + audioMap + totalLessons=6.
Aulas passadas nao sao reescritas (so insercao). Idempotente: aborta se ja aplicado.
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
PROF = os.path.join(ROOT, 'public', 'professor', 'estephano-akihito-ishii.html')
ALUNO = os.path.join(ROOT, 'public', 'aluno', 'estephano-akihito-ishii.html')

AUDIO_BASE = '/audio/estephano-akihito-ishii/'
preclass6 = open(os.path.join(HERE, 'preclass.html'), encoding='utf-8').read().strip()
comp6 = open(os.path.join(HERE, 'complementary.html'), encoding='utf-8').read().strip()

# --- audioMap entries (do hub_snippets section 4) + [order-l6] ---
snip = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()
m = re.search(r'4\. ENTRADAS de audioMap.*?<script>\n(.*?)</script>', snip, re.S)
amap_lines = m.group(1).rstrip('\n')
amap_lines += f'\n  "[order-l6]": "{AUDIO_BASE}a6_order_market.mp3",'

CARD6 = ('    <a href="/professor/estephano-akihito-ishii-aula6.html?autostart=1" style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);border:1px solid rgba(200,200,190,.5);border-radius:12px;cursor:pointer;transition:all .2s;text-decoration:none;color:inherit" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
         '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">06</div>\n'
         '      <div><div style="font-weight:600;font-size:.95rem">Food and Drinks</div><div style="font-size:.8rem;color:var(--text-dim)">some / any + food vocabulary -- 28 slides</div></div>\n'
         '    </a>\n')
STAMP6 = '\n      <div class="stamp" id="stamp6" data-label="Aula 6" style="background-image:url(\'https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=200&q=80\')"></div>'


def add_audiomap(s, entries):
    i = s.index('var audioMap')
    j = s.index('};', i)
    return s[:j] + entries + '\n' + s[j:]


def set_totallessons(s):
    return re.sub(r'var totalLessons\s*=\s*\d+', 'var totalLessons = 6', s)


def add_stamp6(s):
    i = s.index('id="stamp5"')
    e = s.index('></div>', i) + len('></div>')
    return s[:e] + STAMP6 + s[e:]


def patch_prof():
    s = open(PROF, encoding='utf-8').read()
    assert 'id="ex-lesson-6"' not in s, 'PROF ja tem ex-lesson-6 (abortando)'
    # 1. card IN CLASS
    a = '\n  </div>\n</div>\n\n<!-- ═══════════════════ TAB 4: COMPLEMENTARES'
    assert s.count(a) == 1, f'anchor card IN CLASS nao unico ({s.count(a)})'
    s = s.replace(a, '\n' + CARD6 + a, 1)
    # 2. stamp6
    s = add_stamp6(s)
    # 3. ex-lesson-6
    mk = '<!-- /lesson-card aula 5 -->'
    s = s.replace(mk, mk + '\n\n' + preclass6 + '\n<!-- /lesson-card aula 6 -->', 1)
    # 4. complementares l6
    ca = '\n  </div>\n</div>\n\n</div><!-- /container -->'
    assert s.count(ca) == 1, f'anchor comp PROF nao unico ({s.count(ca)})'
    s = s.replace(ca, '\n' + comp6 + ca, 1)
    # 5. audioMap + totalLessons
    s = add_audiomap(s, amap_lines)
    s = set_totallessons(s)
    open(PROF, 'w', encoding='utf-8').write(s)
    print('PROF: ex-lesson-6', s.count('id="ex-lesson-6"'), '| stamp6', s.count('id="stamp6"'),
          '| l6 media', s.count('data-media="l6-'), '| totalLessons',
          re.search(r'var totalLessons\s*=\s*(\d+)', s).group(1))


def extract_prof_block(prof_s, start_marker, end_marker):
    s = prof_s.rfind('<div class="lesson-card"', 0, prof_s.index(start_marker))
    e = prof_s.index(end_marker) + len(end_marker)
    return prof_s[s:e]


def patch_aluno():
    prof_s = open(PROF, encoding='utf-8').read()  # ja patchado -> tem ex-lesson-5 original
    # ex-lesson-5 block do prof (pre-class identico prof/aluno)
    ex5 = extract_prof_block(prof_s, 'id="ex-lesson-5"', '<!-- /lesson-card aula 5 -->')
    # complementares l5 do prof
    h5 = prof_s.rfind('<h3', 0, prof_s.index('-- Aula 5</h3>'))
    ca = '\n  </div>\n</div>\n\n</div><!-- /container -->'
    # prof_s ja foi patchado com comp6 (l6) inserido logo antes de `ca`.
    # comp5 = bloco da Aula 5 SOMENTE (para antes do bloco l6 recem-inserido).
    comp5 = prof_s[h5:prof_s.index('\n' + comp6 + ca)]

    s = open(ALUNO, encoding='utf-8').read()
    assert 'id="ex-lesson-5"' not in s, 'ALUNO ja tem ex-lesson-5'
    assert 'id="ex-lesson-6"' not in s, 'ALUNO ja tem ex-lesson-6'
    # ex-lesson-5 + ex-lesson-6 apos aula 4
    mk = '<!-- /lesson-card aula 4 -->'
    ins = mk + '\n\n' + ex5 + '\n\n' + preclass6 + '\n<!-- /lesson-card aula 6 -->'
    s = s.replace(mk, ins, 1)
    # complementares l5 + l6
    assert s.count(ca) == 1, f'anchor comp ALUNO nao unico ({s.count(ca)})'
    s = s.replace(ca, '\n' + comp5 + '\n' + comp6 + ca, 1)
    # stamp6 + audioMap + totalLessons
    s = add_stamp6(s)
    s = add_audiomap(s, amap_lines)
    s = set_totallessons(s)
    open(ALUNO, 'w', encoding='utf-8').write(s)
    print('ALUNO: ex-lesson', re.findall(r'id="ex-lesson-(\d)"', s), '| stamp6', s.count('id="stamp6"'),
          '| l5 media', s.count('data-media="l5-'), '| l6 media', s.count('data-media="l6-'),
          '| totalLessons', re.search(r'var totalLessons\s*=\s*(\d+)', s).group(1),
          '| order-l5 in amap', '[order-l5]' in s)


if __name__ == '__main__':
    patch_prof()
    patch_aluno()
    print('OK')
