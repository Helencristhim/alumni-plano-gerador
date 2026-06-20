# -*- coding: utf-8 -*-
"""Insere os snippets da Aula 18 nos hubs PROF e ALUNO da Gleice (aditivo).
ADD ONLY -- nunca toca aulas 1-17. Adiciona stamp18, accordion Pre-class (ex-lesson-18),
bloco de Complementares (l18), card no menu IN CLASS (prof) -> standalone#slides,
merge das entradas a18_/pc18_ + [order-l18] no audioMap, e totalLessons -> 18.
Ancora do card IN CLASS = FIM do card da aula 17 (CARD17_END)."""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SLUG = 'gleice-leonardo-rocha-de-souza'
AUDIO_BASE = f'/audio/{SLUG}/'
PROF = os.path.join(ROOT, 'public', 'professor', SLUG + '.html')
ALUN = os.path.join(ROOT, 'public', 'aluno', SLUG + '.html')

accordion = open(os.path.join(HERE, 'preclass.html'), encoding='utf-8').read().rstrip() + '\n'
complementary = open(os.path.join(HERE, 'complementary.html'), encoding='utf-8').read().rstrip() + '\n'
snip = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()

# audioMap entries (snippet section 4) + [order-l18]
m = re.search(r'4\. ENTRADAS.*?<script>\n(.*?)</script>', snip, re.S)
audio_lines = m.group(1).rstrip('\n')
audio_lines += f'\n  "[order-l18]": "{AUDIO_BASE}a18_order_career.mp3",'

MENU_CARD = (
'  <div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" '
"onclick=\"location.href='/professor/gleice-leonardo-rocha-de-souza-aula18.html#slides'\" "
'onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
'    <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">18</div>\n'
'    <div><div style="font-weight:600;font-size:.95rem">Talking About Your Career Story</div><div style="font-size:.8rem;color:var(--text-dim)">Present perfect with for and since -- 27 slides</div></div>\n'
'  </div>\n')

# Ancora = FIM do card da aula 17 (desc + divs de fechamento)
CARD17_END = ('Present perfect for experiences vs past simple -- 27 slides</div></div>\n'
              '  </div>\n')

STAMP18 = ("\n        <div class=\"stamp\" id=\"stamp18\" data-label=\"Career Story\" "
           "style=\"background-image:url('https://images.unsplash.com/photo-1521737711867-e3b97375f902?w=200&q=80')\"></div>")

# fim da aba Complementares (ultimo conteudo antes do <script> principal):
COMP_ANCHOR = re.compile(r'\n</div>\n</div>\n\n?<script>\n// ===== TAB SWITCHING =====')


def must(h, old, new):
    assert h.count(old) == 1, 'anchor not unique (%d): %.70s' % (h.count(old), old)
    return h.replace(old, new)


def patch(path, is_prof):
    h = open(path, encoding='utf-8').read()
    before = (h.count('<div'), h.count('</div>'))
    assert 'id="ex-lesson-18"' not in h, f'{path}: aula 18 ja inserida'
    assert 'id="stamp18"' not in h, f'{path}: stamp18 ja existe'

    # 1) audioMap entries
    h = must(h, 'var audioMap = {', 'var audioMap = {\n' + audio_lines)

    # 2) accordion Pre-class antes do fim da tab-exercises
    h = must(h, '</div><!-- /tab-exercises -->', accordion + '</div><!-- /tab-exercises -->')

    # 3) bloco de Complementares (l18) antes do fim da #tab-complementary
    nmatch = len(COMP_ANCHOR.findall(h))
    assert nmatch == 1, f'{path}: COMP_ANCHOR nao unico ({nmatch})'
    h = COMP_ANCHOR.sub(lambda mm: '\n' + complementary + mm.group(0), h, count=1)

    # 4) stamp18 na stamps-row (apos stamp17)
    m17 = re.search(r'<div class="stamp" id="stamp17"[^>]*></div>', h)
    assert m17, f'{path}: stamp17 ausente'
    h = h.replace(m17.group(0), m17.group(0) + STAMP18, 1)

    # 5) menu card IN CLASS (so prof) -> ancora no FIM do card da aula 17
    if is_prof:
        h = must(h, CARD17_END, CARD17_END + MENU_CARD)

    # 6) totalLessons -> 18
    h = re.sub(r'totalLessons\s*=\s*\d+', 'totalLessons=18', h)

    after = (h.count('<div'), h.count('</div>'))
    assert (after[0] - before[0]) == (after[1] - before[1]), 'div imbalance: %s -> %s' % (before, after)
    open(path, 'w', encoding='utf-8').write(h)
    print('  patched %-5s div delta +%d (balanced), %d bytes' %
          ('prof' if is_prof else 'aluno', after[0] - before[0], len(h)))


patch(PROF, True)
patch(ALUN, False)
print('hub wired OK')
