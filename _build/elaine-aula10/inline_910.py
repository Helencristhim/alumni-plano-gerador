#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inline Aulas 9 and 10 into the Elaine monolith (prof + aluno) so they behave EXACTLY
like Aula 8 (inline IN CLASS via startLesson + full Pre-class lesson card), instead of
opening separate files in a new tab.

Sources:
  - public/professor/elaine-mieko-pinho-aula9.html   (aula9 slides + ex-lesson-9 + audioMap)
  - _build/elaine-aula10/slides.html  + preclass.html + phrases.json  (aula10)
Targets (edited in place):
  - public/professor/elaine-mieko-pinho.html  (slides 225-280, menu cards, pre-class cards,
                                               slidePhases, totalSlides, audioMap merge)
  - public/aluno/elaine-mieko-pinho.html       (pre-class cards, audioMap merge)

Transforms applied to inlined slides (avoid collisions with the legacy engine):
  - data-slide  +224 (aula9) / +252 (aula10)
  - remove ' active' from the opening slide class (engine sets active on load)
  - dialogue lines -> all 'visible', drop any Next Line button (monolith nextDialogueLine
    belongs to aula1; static dialogue avoids collision and stays legible)
  - vocab grids/counters -> unique slots: aula9 = 3/4, aula10 = 5/6 (counterMap has 1..14)
  - aula9 checklist container gets class 'check-grid' (lesson-progress integration)
  - data-lesson forced to 9 / 10 on every slide
"""
import os, re, json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
PROF = os.path.join(ROOT, 'public', 'professor', 'elaine-mieko-pinho.html')
ALUNO = os.path.join(ROOT, 'public', 'aluno', 'elaine-mieko-pinho.html')
A9 = os.path.join(ROOT, 'public', 'professor', 'elaine-mieko-pinho-aula9.html')

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()
def write(p, s):
    with open(p, 'w', encoding='utf-8') as f: f.write(s)

a9 = read(A9)
a10_slides = read(os.path.join(HERE, 'slides.html'))
a10_pre = read(os.path.join(HERE, 'preclass.html'))
phrases = json.loads(read(os.path.join(HERE, 'phrases.json')))

# ---------- extract aula9 slides + lesson card + audioMap ----------
def between(s, start, end):
    i = s.index(start) + len(start); j = s.index(end, i); return s[i:j]

a9_slides = between(a9, '<div class="slides-container" id="slidesContainer">', '</div><!-- /slides-container -->')
a9_card = a9[a9.index('<div class="lesson-card" id="ex-lesson-9">'): a9.index('</div><!-- /lesson-card L9 -->') + len('</div><!-- /lesson-card L9 -->')]
a10_card = a10_pre[a10_pre.index('<div class="lesson-card" id="ex-lesson-10">'): a10_pre.index('</div><!-- /lesson-card L10 -->') + len('</div><!-- /lesson-card L10 -->')]

# aula9 audioMap entries (key -> value)
a9_am_block = between(a9, 'var audioMap = {', '\n};')
a9_pairs = re.findall(r'\n\s*("(?:[^"\\]|\\.)*")\s*:\s*("(?:[^"\\]|\\.)*")', a9_am_block)

# aula10 audioMap entries from phrases.json
a10_pairs = [(json.dumps(p['key'], ensure_ascii=False), json.dumps('/audio/elaine-mieko-pinho/' + p['file'], ensure_ascii=False)) for p in phrases]

# ---------- slide transforms ----------
def offset_slides(html, off, lesson):
    html = re.sub(r'data-slide="(\d+)"', lambda m: 'data-slide="%d"' % (int(m.group(1)) + off), html)
    html = re.sub(r'data-lesson="\d+"', 'data-lesson="%d"' % lesson, html)
    html = html.replace('class="slide active ', 'class="slide ')
    return html

def static_dialogue(html):
    # make every dialogue line visible; drop the aula10 Next Line button
    html = html.replace('class="dialogue-line" data-line', 'class="dialogue-line visible" data-line')
    html = html.replace('class="dialogue-line visible visible"', 'class="dialogue-line visible"')
    html = re.sub(r'<button class="primary-btn" id="nextLineBtn"[^>]*>Next Line</button>', '', html)
    return html

# aula9: +224, lesson 9, vocab grids 1/2->3/4, counters 1/2->3/4, dialogue static, checklist gets check-grid
s9 = offset_slides(a9_slides, 224, 9)
s9 = static_dialogue(s9)
s9 = s9.replace('id="vocabGrid1"', 'id="vocabGrid3"').replace('id="vocabGrid2"', 'id="vocabGrid4"')
s9 = s9.replace('id="vocabCount1"', 'id="vocabCount3"').replace('id="vocabCount2"', 'id="vocabCount4"')
s9 = s9.replace('<div id="checklist-9" style=', '<div id="checklist-9" class="check-grid" style=')

# aula10: +252, lesson 10, vocab grids 1/2->5/6, counters 1/2->5/6, dialogue static
s10 = offset_slides(a10_slides, 252, 10)
s10 = static_dialogue(s10)
s10 = s10.replace('id="vocabGrid1"', 'id="vocabGrid5"').replace('id="vocabGrid2"', 'id="vocabGrid6"')
s10 = s10.replace('id="vocabCount1"', 'id="vocabCount5"').replace('id="vocabCount2"', 'id="vocabCount6"')

assert s9.count('data-slide="225"') == 1 and s9.count('data-slide="252"') == 1, 'aula9 renumber failed'
assert s10.count('data-slide="253"') == 1 and s10.count('data-slide="280"') == 1, 'aula10 renumber failed'

# ---------- slidePhases additions (parse data-phase from transformed slides) ----------
def phase_map(html):
    out = {}
    for m in re.finditer(r'data-slide="(\d+)"[^>]*data-phase="(\d+)"', html):
        out[int(m.group(1))] = int(m.group(2))
    return out
pmap = {}; pmap.update(phase_map(s9)); pmap.update(phase_map(s10))
assert len(pmap) == 56, 'expected 56 phase entries, got %d' % len(pmap)
phase_additions = ','.join('%d:%d' % (k, pmap[k]) for k in sorted(pmap))

# ---------- audioMap merge helper ----------
def merge_audiomap(html, pairs):
    block_start = html.index('var audioMap = {')
    insert_at = block_start + len('var audioMap = {')
    existing = html[block_start: html.index('\n};', block_start)]
    add = []
    seen = set()
    for k, v in pairs:
        if k in seen:
            continue
        seen.add(k)
        if ('\n  %s:' % k) in existing or (' %s:' % k) in existing:
            continue
        add.append('\n  %s: %s,' % (k, v))
    if not add: return html
    return html[:insert_at] + ''.join(add) + html[insert_at:]

# ---------- IN CLASS menu inline cards (replace the <a href> link cards) ----------
def inclass_card(num, start, end, title, sub):
    return ('  <div class="inclass-lesson-card" onclick="startLesson(%d,%d)" style="display:flex;align-items:center;gap:1.2rem;padding:1.2rem 1.5rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:12px;cursor:pointer;transition:all .3s">\n'
            '    <div style="width:52px;height:52px;border-radius:50%%;background:var(--accent);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:1.1rem;flex-shrink:0">%02d</div>\n'
            '    <div style="flex:1">\n'
            '      <div style="font-weight:700;font-size:1rem;color:#1a1a2e;margin-bottom:.2rem">%s</div>\n'
            '      <div style="font-size:.82rem;color:var(--text-dim)">%s</div>\n'
            '    </div>\n'
            '    <div style="font-size:.75rem;color:var(--accent);font-weight:600">28 slides</div>\n'
            '    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 6 15 12 9 18"/></svg>\n'
            '  </div>') % (start, end, num, title, sub)

CARD9 = inclass_card(9, 225, 252, 'Restaurant Basics -- Ordering Food', 'I would like... / Could I have...?')
CARD10 = inclass_card(10, 253, 280, 'Special Requests -- Allergies', 'I am allergic to... / Can you...?')

# ============================= PROFESSOR =============================
prof = read(PROF)

# 1) replace the two IN CLASS <a> link cards with inline startLesson cards
m = re.search(r'\s*<a class="inclass-lesson-card" href="/professor/elaine-mieko-pinho-aula9\.html".*?</a>\s*<a class="inclass-lesson-card" href="/professor/elaine-mieko-pinho-aula10\.html".*?</a>', prof, re.S)
assert m, 'IN CLASS link cards not found in prof'
prof = prof[:m.start()] + '\n' + CARD9 + '\n' + CARD10 + '\n' + prof[m.end():]

# 2) replace the two Pre-class <a> link cards with full inline lesson cards
m = re.search(r'\s*<a href="/professor/elaine-mieko-pinho-aula9\.html".*?</a>\s*<a href="/professor/elaine-mieko-pinho-aula10\.html".*?</a>', prof, re.S)
assert m, 'Pre-class link cards not found in prof'
prof = prof[:m.start()] + '\n\n' + a9_card + '\n\n' + a10_card + '\n' + prof[m.end():]

# 3) inline slides before </div><!-- /slides-container -->
prof = prof.replace('</div><!-- /slides-container -->',
                    s9 + '\n' + s10 + '\n</div><!-- /slides-container -->', 1)

# 4) slidePhases + totalSlides
prof = prof.replace('29:1,', '%s,29:1,' % phase_additions, 1) if False else prof  # noop guard
prof = re.sub(r'(var slidePhases = \{[^}]*?)\};', r'\1,' + phase_additions + '};', prof, count=1)
prof = prof.replace('var totalSlides = 224;', 'var totalSlides = 280;')
prof = prof.replace('var totalLessons = 8;', 'var totalLessons = 10;')

# 5) audioMap merge (aula9 + aula10)
prof = merge_audiomap(prof, a9_pairs + a10_pairs)

write(PROF, prof)

# ============================= ALUNO =============================
aluno = read(ALUNO)
m = re.search(r'\s*<a href="/aluno/elaine-mieko-pinho-aula9\.html".*?</a>\s*<a href="/aluno/elaine-mieko-pinho-aula10\.html".*?</a>', aluno, re.S)
assert m, 'Pre-class link cards not found in aluno'
aluno = aluno[:m.start()] + '\n\n' + a9_card + '\n\n' + a10_card + '\n' + aluno[m.end():]
aluno = aluno.replace('var totalLessons = 8;', 'var totalLessons = 10;')
aluno = merge_audiomap(aluno, a9_pairs + a10_pairs)
write(ALUNO, aluno)

print('OK')
print('  aula9 audioMap pairs:', len(a9_pairs), '| aula10 pairs:', len(a10_pairs))
print('  phase additions (count):', len(pmap))
print('  prof bytes:', len(prof), '| aluno bytes:', len(aluno))
