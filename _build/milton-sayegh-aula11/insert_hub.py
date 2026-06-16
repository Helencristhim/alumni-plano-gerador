#!/usr/bin/env python3
"""Insere os snippets da aula 11 nos hubs prof+aluno do Milton, SO ADITIVO.
Aulas 1-10 ficam intactas. Idempotente: nao insere se ex-lesson-11 ja existe."""
import re, sys

ROOT = '/home/dan/dev/work/better/wt-camp-milton'
SNIP = ROOT + '/_build/milton-sayegh-aula11/hub_snippets.html'

snip = open(SNIP, encoding='utf-8').read()

def section(tag_start, tag_end=None):
    i = snip.index(tag_start)
    j = snip.index(tag_end, i) if tag_end else len(snip)
    return snip[i+len(tag_start):j].strip()

# Parse snippet parts by their comment headers
parts = {}
markers = [
    ('stamp', '<!-- 2. STAMP', '<!-- 3. ACCORDION'),
    ('accordion', '<!-- 3. ACCORDION Pre-class (inserir após o ex-lesson anterior, prof E aluno) -->', '<!-- 3b. COMPLEMENTARES'),
    ('comp', '<!-- 3b. COMPLEMENTARES da aula 11 (inserir na tab-complementary, prof E aluno) -->', '<!-- 4. ENTRADAS'),
    ('audiomap', '<!-- 4. ENTRADAS de audioMap (mesclar no audioMap do hub, prof E aluno) -->\n<script>', '</script>'),
]
for name, a, b in markers:
    i = snip.index(a) + len(a)
    j = snip.index(b, i)
    parts[name] = snip[i:j].strip()

STAMP = parts['stamp']
ACCORDION = parts['accordion']
COMP = parts['comp']
AUDIO = parts['audiomap'].strip()
if AUDIO.endswith(','):
    pass

# IN CLASS card (legacy style, matching aulas 6-10 in Milton's hub)
INCLASS_CARD = '''<a href="/professor/milton-sayegh-aula11.html?autostart=1" style="text-decoration:none;color:inherit">
<div class="inclass-lesson-card" style="cursor:pointer">
  <div class="ilc-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg></div>
  <div class="ilc-info">
    <div class="ilc-number">LESSON 11 — 60 MINUTES</div>
    <div class="ilc-title">Problem Solving</div>
    <div class="ilc-desc">When Things Go Wrong - First &amp; Second Conditionals — 32 slides</div>
  </div>
  <div class="ilc-arrow">&#8594;</div>
</div>
</a>
'''

def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    if 'id="ex-lesson-11"' in s:
        print(f'  SKIP {path} (ex-lesson-11 already present)')
        return
    # 1. STAMP after stamp10
    m = re.search(r'(<div class="stamp" id="stamp10"[^>]*></div>)', s)
    assert m, f'{path}: stamp10 not found'
    s = s[:m.end()] + '\n        ' + STAMP + s[m.end():]
    # 2. ACCORDION Pre-class: after ex-lesson-10 closes, before </div><!-- /tab-exercises -->
    anchor = '</div><!-- /tab-exercises -->'
    assert anchor in s, f'{path}: tab-exercises close not found'
    s = s.replace(anchor, ACCORDION + '\n\n' + anchor, 1)
    # 3. COMPLEMENTARES: before </div><!-- /tab-complementary -->
    canchor = '</div><!-- /tab-complementary -->'
    assert canchor in s, f'{path}: tab-complementary close not found'
    s = s.replace(canchor, COMP + '\n\n' + canchor, 1)
    # 4. IN CLASS card (prof only): before </div><!-- /tab-inclass -->
    if is_prof:
        ianchor = '</div><!-- /tab-inclass -->'
        assert ianchor in s, f'{path}: tab-inclass close not found'
        s = s.replace(ianchor, INCLASS_CARD + '\n' + ianchor, 1)
    # 5. audioMap entries: right after 'var audioMap = {'
    m = re.search(r'var audioMap = \{', s)
    assert m, f'{path}: audioMap open not found'
    s = s[:m.end()] + '\n' + AUDIO + '\n' + s[m.end():]
    # 6. totalLessons 10 -> 11
    s2 = re.sub(r'var totalLessons=10', 'var totalLessons=11', s)
    assert s2 != s, f'{path}: totalLessons=10 not replaced'
    s = s2
    open(path, 'w', encoding='utf-8').write(s)
    print(f'  PATCHED {path}')

patch(ROOT + '/public/professor/milton-sayegh.html', is_prof=True)
patch(ROOT + '/public/aluno/milton-sayegh.html', is_prof=False)
print('done')
