# -*- coding: utf-8 -*-
"""Insere os snippets da Aula 8 nos hubs PROF e ALUNO da Gleice (aditivo).
ADD ONLY -- nunca toca aulas 1-7. Adiciona stamp8, accordion Pre-class (ex-lesson-8),
bloco de Complementares (l8), card no menu IN CLASS (prof) -> standalone#slides,
merge das entradas a8_/pc8_ + [order-l8] no audioMap, e totalLessons -> 8."""
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

# audioMap entries (snippet section 4) + [order-l8]
m = re.search(r'4\. ENTRADAS.*?<script>\n(.*?)</script>', snip, re.S)
audio_lines = m.group(1).rstrip('\n')
audio_lines += f'\n  "[order-l8]": "{AUDIO_BASE}a8_order_product.mp3",'

MENU_CARD = (
'  <div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" '
"onclick=\"location.href='/professor/gleice-leonardo-rocha-de-souza-aula8.html#slides'\" "
'onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
'    <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">08</div>\n'
'    <div><div style="font-weight:600;font-size:.95rem">The Pharma World</div><div style="font-size:.8rem;color:var(--text-dim)">Industry Vocabulary: Present Simple -- 27 slides</div></div>\n'
'  </div>\n')

CARD7_END = ('<div style="font-size:.8rem;color:var(--text-dim)">Turning Points: Simple Past -- 27 slides</div></div>\n'
             '  </div>\n')

STAMP8 = ("\n        <div class=\"stamp\" id=\"stamp8\" data-label=\"Pharma World\" "
          "style=\"background-image:url('https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=200&q=80')\"></div>")

# fim da aba Complementares (ultimo conteudo antes do <script> principal):
COMP_ANCHOR = re.compile(r'\n</div>\n</div>\n\n?<script>\n// ===== TAB SWITCHING =====')


def must(h, old, new):
    assert h.count(old) == 1, 'anchor not unique (%d): %.70s' % (h.count(old), old)
    return h.replace(old, new)


def patch(path, is_prof):
    h = open(path, encoding='utf-8').read()
    before = (h.count('<div'), h.count('</div>'))
    assert 'id="ex-lesson-8"' not in h, f'{path}: aula 8 ja inserida'
    assert 'id="stamp8"' not in h, f'{path}: stamp8 ja existe'

    # 1) audioMap entries
    h = must(h, 'var audioMap = {', 'var audioMap = {\n' + audio_lines)

    # 2) accordion Pre-class antes do fim da tab-exercises
    h = must(h, '</div><!-- /tab-exercises -->', accordion + '</div><!-- /tab-exercises -->')

    # 3) bloco de Complementares (l8) antes do fim da #tab-complementary
    nmatch = len(COMP_ANCHOR.findall(h))
    assert nmatch == 1, f'{path}: COMP_ANCHOR nao unico ({nmatch})'
    h = COMP_ANCHOR.sub(lambda mm: '\n' + complementary + mm.group(0), h, count=1)

    # 4) stamp8 na stamps-row (apos stamp7)
    m7 = re.search(r'<div class="stamp" id="stamp7"[^>]*></div>', h)
    assert m7, f'{path}: stamp7 ausente'
    h = h.replace(m7.group(0), m7.group(0) + STAMP8, 1)

    # 5) menu card IN CLASS (so prof)
    if is_prof:
        h = must(h, CARD7_END, CARD7_END + MENU_CARD)

    # 6) totalLessons -> 8
    h = re.sub(r'totalLessons\s*=\s*\d+', 'totalLessons=8', h)

    after = (h.count('<div'), h.count('</div>'))
    assert (after[0] - before[0]) == (after[1] - before[1]), 'div imbalance: %s -> %s' % (before, after)
    open(path, 'w', encoding='utf-8').write(h)
    print('  patched %-5s div delta +%d (balanced), %d bytes' %
          ('prof' if is_prof else 'aluno', after[0] - before[0], len(h)))


patch(PROF, True)
patch(ALUN, False)
print('hub wired OK')
