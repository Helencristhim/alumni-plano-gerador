# -*- coding: utf-8 -*-
"""Insere os snippets da Aula 17 nos hubs PROF e ALUNO da Gleice (aditivo).
ADD ONLY -- nunca toca aulas 1-16. Adiciona stamp17, accordion Pre-class (ex-lesson-17),
bloco de Complementares (l17), card no menu IN CLASS (prof) -> standalone#slides,
merge das entradas a17_/pc17_ + [order-l17] no audioMap, e totalLessons -> 17.
Ancora do card IN CLASS = FIM do card da aula 16 (CARD16_END)."""
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

# audioMap entries (snippet section 4) + [order-l17]
m = re.search(r'4\. ENTRADAS.*?<script>\n(.*?)</script>', snip, re.S)
audio_lines = m.group(1).rstrip('\n')
audio_lines += f'\n  "[order-l17]": "{AUDIO_BASE}a17_order_experiences.mp3",'

MENU_CARD = (
'  <div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" '
"onclick=\"location.href='/professor/gleice-leonardo-rocha-de-souza-aula17.html#slides'\" "
'onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
'    <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">17</div>\n'
'    <div><div style="font-weight:600;font-size:.95rem">Talking About Experiences</div><div style="font-size:.8rem;color:var(--text-dim)">Present perfect for experiences vs past simple -- 27 slides</div></div>\n'
'  </div>\n')

# Ancora = FIM do card da aula 16 (desc + divs de fechamento)
CARD16_END = ('Checkpoint 3: Business Communication Review -- 27 slides</div></div>\n'
              '  </div>\n')

STAMP17 = ("\n        <div class=\"stamp\" id=\"stamp17\" data-label=\"Experiences\" "
           "style=\"background-image:url('https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=200&q=80')\"></div>")

# fim da aba Complementares (ultimo conteudo antes do <script> principal):
COMP_ANCHOR = re.compile(r'\n</div>\n</div>\n\n?<script>\n// ===== TAB SWITCHING =====')


def must(h, old, new):
    assert h.count(old) == 1, 'anchor not unique (%d): %.70s' % (h.count(old), old)
    return h.replace(old, new)


def patch(path, is_prof):
    h = open(path, encoding='utf-8').read()
    before = (h.count('<div'), h.count('</div>'))
    assert 'id="ex-lesson-17"' not in h, f'{path}: aula 17 ja inserida'
    assert 'id="stamp17"' not in h, f'{path}: stamp17 ja existe'

    # 1) audioMap entries
    h = must(h, 'var audioMap = {', 'var audioMap = {\n' + audio_lines)

    # 2) accordion Pre-class antes do fim da tab-exercises
    h = must(h, '</div><!-- /tab-exercises -->', accordion + '</div><!-- /tab-exercises -->')

    # 3) bloco de Complementares (l17) antes do fim da #tab-complementary
    nmatch = len(COMP_ANCHOR.findall(h))
    assert nmatch == 1, f'{path}: COMP_ANCHOR nao unico ({nmatch})'
    h = COMP_ANCHOR.sub(lambda mm: '\n' + complementary + mm.group(0), h, count=1)

    # 4) stamp17 na stamps-row (apos stamp16)
    m16 = re.search(r'<div class="stamp" id="stamp16"[^>]*></div>', h)
    assert m16, f'{path}: stamp16 ausente'
    h = h.replace(m16.group(0), m16.group(0) + STAMP17, 1)

    # 5) menu card IN CLASS (so prof) -> ancora no FIM do card da aula 16
    if is_prof:
        h = must(h, CARD16_END, CARD16_END + MENU_CARD)

    # 6) totalLessons -> 17
    h = re.sub(r'totalLessons\s*=\s*\d+', 'totalLessons=17', h)

    after = (h.count('<div'), h.count('</div>'))
    assert (after[0] - before[0]) == (after[1] - before[1]), 'div imbalance: %s -> %s' % (before, after)
    open(path, 'w', encoding='utf-8').write(h)
    print('  patched %-5s div delta +%d (balanced), %d bytes' %
          ('prof' if is_prof else 'aluno', after[0] - before[0], len(h)))


patch(PROF, True)
patch(ALUN, False)
print('hub wired OK')
