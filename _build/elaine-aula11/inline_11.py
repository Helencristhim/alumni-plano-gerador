#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inline Aula 11 into the Elaine monolith (prof+aluno), like aulas 8/9/10.
Also backfills the missing Aula 9 + Aula 10 Complementares into tab-complementary."""
import os, re, json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
PROF = os.path.join(ROOT, 'public', 'professor', 'elaine-mieko-pinho.html')
ALUNO = os.path.join(ROOT, 'public', 'aluno', 'elaine-mieko-pinho.html')
A11 = os.path.join(ROOT, 'public', 'professor', 'elaine-mieko-pinho-aula11.html')
A9 = os.path.join(ROOT, 'public', 'professor', 'elaine-mieko-pinho-aula9.html')
CMP10 = os.path.join(ROOT, '_build', 'elaine-aula10', 'complementary.html')

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()
def write(p, s):
    with open(p, 'w', encoding='utf-8') as f: f.write(s)
def between(s, a, b):
    i = s.index(a) + len(a); return s[i:s.index(b, i)]

a11 = read(A11)
preclass = read(os.path.join(HERE, 'preclass.html'))
compl11 = read(os.path.join(HERE, 'complementary.html'))
compl10 = read(CMP10)
phrases = json.loads(read(os.path.join(HERE, 'phrases.json')))

# ---- aula11 slides (offset +280, lesson 11, static dialogue, vocab grids 7/8) ----
s11 = between(a11, '<div class="slides-container" id="slidesContainer">', '</div><!-- /slides-container -->')
s11 = re.sub(r'data-slide="(\d+)"', lambda m: 'data-slide="%d"' % (int(m.group(1)) + 280), s11)
s11 = s11.replace('class="slide active ', 'class="slide ')
s11 = s11.replace('class="dialogue-line" data-line', 'class="dialogue-line visible" data-line')
s11 = re.sub(r'<button class="primary-btn" id="nextLineBtn"[^>]*>Next Line</button>', '', s11)
s11 = s11.replace('id="vocabGrid1"', 'id="vocabGrid7"').replace('id="vocabGrid2"', 'id="vocabGrid8"')
s11 = s11.replace('id="vocabCount1"', 'id="vocabCount7"').replace('id="vocabCount2"', 'id="vocabCount8"')
assert s11.count('data-slide="281"') == 1 and s11.count('data-slide="308"') == 1

# phase additions
pmap = {int(m.group(1)): int(m.group(2)) for m in re.finditer(r'data-slide="(\d+)"[^>]*data-phase="(\d+)"', s11)}
assert len(pmap) == 28
phase_add = ','.join('%d:%d' % (k, pmap[k]) for k in sorted(pmap))

# aula11 pre-class card + complementary
card11 = preclass[preclass.index('<div class="lesson-card" id="ex-lesson-11">'): preclass.index('</div><!-- /lesson-card L11 -->') + len('</div><!-- /lesson-card L11 -->')]

# aula9 complementary inner (from standalone)
compl9 = between(read(A9), '<div class="tab-content" id="tab-complementary">', '</div><!-- /tab-complementary -->').strip()
compl10 = compl10.strip()
compl11 = compl11.strip()

# audioMap pairs
a11_pairs = [(json.dumps(p['key'], ensure_ascii=False), json.dumps('/audio/elaine-mieko-pinho/' + p['file'], ensure_ascii=False)) for p in phrases]

def merge_audiomap(html, pairs):
    bs = html.index('var audioMap = {'); ins = bs + len('var audioMap = {')
    existing = html[bs: html.index('\n};', bs)]; add = []; seen = set()
    for k, v in pairs:
        if k in seen: continue
        seen.add(k)
        if ('\n  %s:' % k) in existing or (' %s:' % k) in existing: continue
        add.append('\n  %s: %s,' % (k, v))
    return html[:ins] + ''.join(add) + html[ins:] if add else html

def inclass_card(num, start, end, title, sub):
    return ('  <div class="inclass-lesson-card" onclick="startLesson(%d,%d)" style="display:flex;align-items:center;gap:1.2rem;padding:1.2rem 1.5rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:12px;cursor:pointer;transition:all .3s">\n'
            '    <div style="width:52px;height:52px;border-radius:50%%;background:var(--accent);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:1.1rem;flex-shrink:0">%02d</div>\n'
            '    <div style="flex:1"><div style="font-weight:700;font-size:1rem;color:#1a1a2e;margin-bottom:.2rem">%s</div><div style="font-size:.82rem;color:var(--text-dim)">%s</div></div>\n'
            '    <div style="font-size:.75rem;color:var(--accent);font-weight:600">28 slides</div>\n'
            '    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 6 15 12 9 18"/></svg>\n'
            '  </div>') % (start, end, num, title, sub)

CARD11 = inclass_card(11, 281, 308, 'Paying the Bill', 'Numbers &amp; paying politely')

def compl_block(title, inner):
    # match monolith style (h3 with margin-top spacing). inner already has its own h3/p/grid.
    return '\n' + inner + '\n'

# ============ PROFESSOR ============
prof = read(PROF)
assert 'data-slide="281"' not in prof, 'aula11 already inlined?'
# slides
prof = prof.replace('</div><!-- /slides-container -->', s11 + '\n</div><!-- /slides-container -->', 1)
# slidePhases + totals
prof = re.sub(r'(var slidePhases = \{[^}]*?)\};', r'\1,' + phase_add + '};', prof, count=1)
prof = prof.replace('var totalSlides = 280;', 'var totalSlides = 308;')
prof = prof.replace('var totalLessons = 10;', 'var totalLessons = 11;')
# stamp11 after stamp10
stamp10 = '<div class="stamp" id="stamp10" data-label="Allergies" style="background-image:url(\'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=200&q=80\')"></div>'
prof = prof.replace(stamp10, stamp10 + '\n<div class="stamp" id="stamp11" data-label="Paying" style="background-image:url(\'https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=200&q=80\')"></div>', 1)
# pre-class card after ex-lesson-10
prof = prof.replace('</div><!-- /lesson-card L10 -->', '</div><!-- /lesson-card L10 -->\n\n' + card11, 1)
# IN CLASS menu: insert CARD11 before the cards-container close (the </div> right before tab close)
idx = prof.index('</div><!-- /tab-inclass -->')
cc = prof.rfind('</div>', 0, idx)  # cards-container close
prof = prof[:cc] + CARD11 + '\n' + prof[cc:]
# complementary: add 9, 10, 11 before close
prof = prof.replace('</div><!-- /tab-complementary -->',
                    compl_block(9, compl9) + compl_block(10, compl10) + compl_block(11, compl11) + '\n</div><!-- /tab-complementary -->', 1)
# audioMap
prof = merge_audiomap(prof, a11_pairs)
write(PROF, prof)

# ============ ALUNO ============
aluno = read(ALUNO)
aluno = aluno.replace('var totalLessons = 10;', 'var totalLessons = 11;')
aluno = aluno.replace(stamp10, stamp10 + '\n<div class="stamp" id="stamp11" data-label="Paying" style="background-image:url(\'https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=200&q=80\')"></div>', 1)
aluno = aluno.replace('</div><!-- /lesson-card L10 -->', '</div><!-- /lesson-card L10 -->\n\n' + card11, 1)
aluno = aluno.replace('</div><!-- /tab-complementary -->',
                      compl_block(9, compl9) + compl_block(10, compl10) + compl_block(11, compl11) + '\n</div><!-- /tab-complementary -->', 1)
aluno = merge_audiomap(aluno, a11_pairs)
write(ALUNO, aluno)

print('OK aula11 inlined; phase additions', len(pmap), '; audioMap pairs', len(a11_pairs))
