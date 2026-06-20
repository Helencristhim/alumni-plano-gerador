#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insercao ADITIVA dos snippets da aula 12 no hub de rafael-gasparelli-lima.
Insere por ancora de string (idempotente: aborta se ja inserido). Aulas 1-11 intactas."""
import sys

SNIP = '_build/rafael-gasparelli-lima-aula12/hub_snippets.html'
PROF = 'public/professor/rafael-gasparelli-lima.html'
ALUNO = 'public/aluno/rafael-gasparelli-lima.html'


def read(p):
    with open(p, encoding='utf-8') as f:
        return f.read()


def write(p, s):
    with open(p, 'w', encoding='utf-8') as f:
        f.write(s)


snip_lines = read(SNIP).split('\n')
# Section ranges (0-based line indices, per grep markers)
accordion = '\n'.join(snip_lines[11:168]).strip()          # lines 12-168 -> accordion
complementary = '\n'.join(snip_lines[171:209]).strip()      # lines 172-209 -> l12 media block
audiomap = '\n'.join(snip_lines[213:240]).strip()           # lines 214-240 -> audioMap entries (no <script> tags)

# Sanity
assert 'id="ex-lesson-12"' in accordion, 'accordion slice wrong'
assert 'data-media="l12-series"' in complementary, 'complementary slice wrong'
assert 'pc12_attachment.mp3' in audiomap, 'audiomap slice wrong'

INCLASS_CARD = '''<a href="/professor/rafael-gasparelli-lima-aula12.html?autostart=1" class="inclass-lesson-card" style="text-decoration:none;color:inherit">
  <div class="ilc-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg></div>
  <div class="ilc-info">
    <div class="ilc-number">LESSON 12 &mdash; 60 MINUTES</div>
    <div class="ilc-title">Review &amp; Consolidation: Lessons 7 to 11</div>
    <div class="ilc-desc">Mid-Program Review &mdash; Lesson 12 &mdash; 28 slides</div>
  </div>
  <div class="ilc-arrow">&#8594;</div>
</a>
'''

STAMP = '''        <div class="stamp" id="stamp12" data-label="Mid-Program Review" style="background-image:url('https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=200&q=80')"></div>
'''


def process(path, is_prof):
    c = read(path)
    if 'id="ex-lesson-12"' in c:
        print(f'  SKIP {path} (ja tem aula 12)')
        return
    # 1. accordion: antes de </div><!-- /tab-exercises -->
    anchor_ex = '</div><!-- /tab-exercises -->'
    assert anchor_ex in c, f'no tab-exercises anchor in {path}'
    c = c.replace(anchor_ex, accordion + '\n\n' + anchor_ex, 1)
    # 2. stamp: depois da linha do stamp11
    anchor_stamp = '<div class="stamp" id="stamp11"'
    i = c.index(anchor_stamp)
    eol = c.index('\n', i) + 1
    c = c[:eol] + STAMP + c[eol:]
    # 3. complementary: antes de </div><!-- /tab-complementary -->
    anchor_comp = '</div><!-- /tab-complementary -->'
    assert anchor_comp in c, f'no tab-complementary anchor in {path}'
    c = c.replace(anchor_comp, complementary + '\n\n' + anchor_comp, 1)
    # 4. audioMap: depois de var audioMap = {
    anchor_am = 'var audioMap = {'
    i = c.index(anchor_am)
    eol = c.index('\n', i) + 1
    c = c[:eol] + audiomap + '\n' + c[eol:]
    # 5. totalLessons 11 -> 12
    assert 'totalLessons=11' in c, f'no totalLessons=11 in {path}'
    c = c.replace('totalLessons=11', 'totalLessons=12', 1)
    # 6. IN CLASS card (so prof)
    if is_prof:
        anchor_ic = '</div><!-- /tab-inclass -->'
        assert anchor_ic in c, f'no tab-inclass anchor in {path}'
        c = c.replace(anchor_ic, INCLASS_CARD + '\n' + anchor_ic, 1)
    write(path, c)
    print(f'  OK {path}')


process(PROF, True)
process(ALUNO, False)
print('done')
