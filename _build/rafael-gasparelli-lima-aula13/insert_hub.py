#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insercao ADITIVA dos snippets da aula 13 no hub de rafael-gasparelli-lima.
Insere por ancora de string (idempotente: aborta se ja inserido). Aulas 1-12 intactas."""

SNIP = '_build/rafael-gasparelli-lima-aula13/hub_snippets.html'
PROF = 'public/professor/rafael-gasparelli-lima.html'
ALUNO = 'public/aluno/rafael-gasparelli-lima.html'


def read(p):
    with open(p, encoding='utf-8') as f:
        return f.read()


def write(p, s):
    with open(p, 'w', encoding='utf-8') as f:
        f.write(s)


lines = read(SNIP).split('\n')
acc_start = next(i for i, l in enumerate(lines) if 'id="ex-lesson-13"' in l)
comp_comment = next(i for i, l in enumerate(lines) if '3b. COMPLEMENTARES' in l)
am_comment = next(i for i, l in enumerate(lines) if '4. ENTRADAS de audioMap' in l)
comp_start = next(i for i in range(comp_comment, len(lines)) if 'media-card-wrapper' in lines[i])
script_open = next(i for i in range(am_comment, len(lines)) if lines[i].strip() == '<script>')
script_close = next(i for i in range(script_open, len(lines)) if lines[i].strip() == '</script>')

accordion = '\n'.join(lines[acc_start:comp_comment]).strip()
complementary = '\n'.join(lines[comp_start:am_comment]).strip()
audiomap = '\n'.join(lines[script_open + 1:script_close]).strip()

# Sanity
assert 'id="ex-lesson-13"' in accordion, 'accordion slice wrong'
assert 'data-media="l13-series"' in complementary, 'complementary slice wrong'
assert 'pc13_launch.mp3' in audiomap, 'audiomap slice wrong'
assert '<script>' not in audiomap and '<div' not in complementary[-10:], 'slice overrun'

INCLASS_CARD = '''<a href="/professor/rafael-gasparelli-lima-aula13.html?autostart=1" class="inclass-lesson-card" style="text-decoration:none;color:inherit">
  <div class="ilc-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg></div>
  <div class="ilc-info">
    <div class="ilc-number">LESSON 13 &mdash; 60 MINUTES</div>
    <div class="ilc-title">What Happened? &mdash; Describing Past Events</div>
    <div class="ilc-desc">Past Simple regular verbs &mdash; Lesson 13 &mdash; 28 slides</div>
  </div>
  <div class="ilc-arrow">&#8594;</div>
</a>
'''

STAMP = '''        <div class="stamp" id="stamp13" data-label="Past Simple" style="background-image:url('https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=200&q=80')"></div>
'''


def process(path, is_prof):
    c = read(path)
    if 'id="ex-lesson-13"' in c:
        print(f'  SKIP {path} (ja tem aula 13)')
        return
    # 1. accordion: antes de </div><!-- /tab-exercises -->
    anchor_ex = '</div><!-- /tab-exercises -->'
    assert anchor_ex in c, f'no tab-exercises anchor in {path}'
    c = c.replace(anchor_ex, accordion + '\n\n' + anchor_ex, 1)
    # 2. stamp: depois da linha do stamp12
    anchor_stamp = '<div class="stamp" id="stamp12"'
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
    # 5. totalLessons 12 -> 13
    assert 'totalLessons=12' in c, f'no totalLessons=12 in {path}'
    c = c.replace('totalLessons=12', 'totalLessons=13', 1)
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
