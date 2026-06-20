#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insercao ADITIVA dos snippets da aula 17 no hub existente (prof + aluno).
Apenas insere por ancora de string; aulas 1-16 ficam intactas."""
import re, os

ROOT = '/home/dan/dev/work/better/wt-rafgasp-g2-a17'
SNIP = os.path.join(ROOT, '_build/rafael-gasparelli-lima-aula17/hub_snippets.html')
snip = open(SNIP, encoding='utf-8').read()

# --- extrair blocos do snippet ---
# Accordion: do <div class="lesson-card" id="ex-lesson-17"> ate o marcador 3b
acc_start = snip.index('<div class="lesson-card" id="ex-lesson-17">')
acc_end_marker = '<!-- 3b. COMPLEMENTARES'
accordion = snip[acc_start:snip.index(acc_end_marker)].rstrip() + '\n'

# Complementares: do primeiro media-card-wrapper l17 ate o marcador 4.
comp_start = snip.index('<div class="media-card-wrapper" data-media="l17-series">')
comp_end_marker = '<!-- 4. ENTRADAS de audioMap'
complementary = snip[comp_start:snip.index(comp_end_marker)].rstrip() + '\n'

# audioMap: entre <script> e </script> do bloco 4
am_block = snip[snip.index('<!-- 4. ENTRADAS de audioMap'):]
am_inner = am_block[am_block.index('<script>')+len('<script>'):am_block.index('</script>')].strip('\n')
audiomap_entries = am_inner.rstrip() + '\n'

# Stamp
stamp = '''        <div class="stamp" id="stamp17" data-label="The Fine Print" style="background-image:url('https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=200&q=80')"></div>'''

# Menu card no formato do hub (inclass-lesson-card) — uniforme com aulas anteriores
menu_card = '''<a href="/professor/rafael-gasparelli-lima-aula17.html?autostart=1" class="inclass-lesson-card" style="text-decoration:none;color:inherit">
  <div class="ilc-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg></div>
  <div class="ilc-info">
    <div class="ilc-number">LESSON 17 &mdash; 60 MINUTES</div>
    <div class="ilc-title">Legal Basics &mdash; Contracts and Terms</div>
    <div class="ilc-desc">Contract terms &amp; obligation modals (shall/must/may) &mdash; Lesson 17 &mdash; 28 slides</div>
  </div>
  <div class="ilc-arrow">&#8594;</div>
</a>
'''


def insert_before(s, anchor, block):
    i = s.index(anchor)
    return s[:i] + block + '\n' + s[i:]


def process(path, is_prof):
    s = open(path, encoding='utf-8').read()
    orig_len = len(s)
    # guard: nao reinserir
    assert 'id="ex-lesson-17"' not in s, f'{path} ja tem aula 17'

    # 1. audioMap (apos 'var audioMap = {\n')
    s = s.replace('var audioMap = {\n', 'var audioMap = {\n' + audiomap_entries, 1)

    # 2. stamp (apos a linha do stamp16)
    s = re.sub(r'(<div class="stamp" id="stamp16"[^\n]*\n)', r'\1' + stamp + '\n', s, count=1)

    # 3. accordion (antes de /tab-exercises)
    s = insert_before(s, '</div><!-- /tab-exercises -->', accordion)

    # 4. complementares (antes de /tab-complementary)
    s = insert_before(s, '</div><!-- /tab-complementary -->', complementary)

    # 5. menu card (prof: antes de /tab-inclass)
    if is_prof:
        s = insert_before(s, '</div><!-- /tab-inclass -->', menu_card)

    # 6. totalLessons 16 -> 17
    s = s.replace('var totalLessons=16;', 'var totalLessons=17;', 1)

    open(path, 'w', encoding='utf-8').write(s)
    print(f'  {os.path.basename(path)}: {orig_len} -> {len(s)} (+{len(s)-orig_len})')


process(os.path.join(ROOT, 'public/professor/rafael-gasparelli-lima.html'), True)
process(os.path.join(ROOT, 'public/aluno/rafael-gasparelli-lima.html'), False)
print('done')
