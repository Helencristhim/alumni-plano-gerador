#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inline Aula 17 into the Elaine monolith (prof+aluno). ADITIVO ONLY: adds stamp17,
ex-lesson-17 (Pre-class), IN CLASS menu card startLesson(449,476), 28 slides (data-slide
449..476), slidePhases, audioMap, complementary l17. Bumps totalSlides 448->476 and
totalLessons ->17 (Pre-class progress loop). counterMap ja estendido ate vocabGrid30."""
import os, re, json
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
PROF = os.path.join(ROOT, 'public', 'professor', 'elaine-mieko-pinho.html')
ALUNO = os.path.join(ROOT, 'public', 'aluno', 'elaine-mieko-pinho.html')
REF = os.path.join(HERE, '_standalone_ref', 'elaine-mieko-pinho-aula17.html')  # prof standalone = source of slides
N = 17; OFF = 28 * (N - 1)            # 448
VG = (19, 20)
TITLE = 'Sightseeing -- Tickets and Tours'; SUB = 'Booking a tour'
STAMP = '<div class="stamp" id="stamp17" data-label="Sightseeing" style="background-image:url(\'https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?w=200&q=80\')"></div>'
PREV_STAMP = '<div class="stamp" id="stamp16" data-label="Review 2" style="background-image:url(\'https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?w=200&q=80\')"></div>'
PREV_CARD_CLOSE = '</div><!-- /lesson-card L16 -->'
PREV_TOTSLIDES = 'var totalSlides = 448;'; NEW_TOTSLIDES = 'var totalSlides = 476;'

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()
def write(p, s):
    with open(p, 'w', encoding='utf-8') as f: f.write(s)
def between(s, a, b):
    i = s.index(a) + len(a); return s[i:s.index(b, i)]

ref = read(REF)
preclass = read(os.path.join(HERE, 'preclass.html'))
compl = read(os.path.join(HERE, 'complementary.html')).strip()
phrases = json.loads(read(os.path.join(HERE, 'phrases.json')))

# extract slides from the standalone ref (they are data-slide 1..28)
s = between(ref, '<div class="slides-container" id="slidesContainer">', '</div><!-- /slides-container -->')
s = re.sub(r'data-slide="(\d+)"', lambda m: 'data-slide="%d"' % (int(m.group(1)) + OFF), s)
s = s.replace('class="slide active ', 'class="slide ')
s = s.replace('class="dialogue-line" data-line', 'class="dialogue-line visible" data-line')
s = re.sub(r'<button class="primary-btn" id="nextLineBtn"[^>]*>Next Line</button>', '', s)
s = s.replace('id="vocabGrid1"', 'id="vocabGrid%d"' % VG[0]).replace('id="vocabGrid2"', 'id="vocabGrid%d"' % VG[1])
s = s.replace('id="vocabCount1"', 'id="vocabCount%d"' % VG[0]).replace('id="vocabCount2"', 'id="vocabCount%d"' % VG[1])
assert s.count('data-slide="%d"' % (OFF + 1)) == 1 and s.count('data-slide="%d"' % (OFF + 28)) == 1

pmap = {int(m.group(1)): int(m.group(2)) for m in re.finditer(r'data-slide="(\d+)"[^>]*data-phase="(\d+)"', s)}
assert len(pmap) == 28, len(pmap)
phase_add = ','.join('%d:%d' % (k, pmap[k]) for k in sorted(pmap))

card = preclass[preclass.index('<div class="lesson-card" id="ex-lesson-%d">' % N): preclass.index('</div><!-- /lesson-card L%d -->' % N) + len('</div><!-- /lesson-card L%d -->' % N)]
pairs = [(json.dumps(p['key'], ensure_ascii=False), json.dumps('/audio/elaine-mieko-pinho/' + p['file'], ensure_ascii=False)) for p in phrases]

def merge_audiomap(html, pairs):
    bs = html.index('var audioMap = {'); ins = bs + len('var audioMap = {')
    existing = html[bs: html.index('\n};', bs)]; add = []; seen = set()
    for k, v in pairs:
        if k in seen: continue
        seen.add(k)
        if ('\n  %s:' % k) in existing or (' %s:' % k) in existing: continue
        add.append('\n  %s: %s,' % (k, v))
    return html[:ins] + ''.join(add) + html[ins:] if add else html

CARD = ('  <div class="inclass-lesson-card" onclick="startLesson(%d,%d)" style="display:flex;align-items:center;gap:1.2rem;padding:1.2rem 1.5rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:12px;cursor:pointer;transition:all .3s">\n'
        '    <div style="width:52px;height:52px;border-radius:50%%;background:var(--accent);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:1.1rem;flex-shrink:0">%d</div>\n'
        '    <div style="flex:1"><div style="font-weight:700;font-size:1rem;color:#1a1a2e;margin-bottom:.2rem">%s</div><div style="font-size:.82rem;color:var(--text-dim)">%s</div></div>\n'
        '    <div style="font-size:.75rem;color:var(--accent);font-weight:600">28 slides</div>\n'
        '    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 6 15 12 9 18"/></svg>\n'
        '  </div>') % (OFF + 1, OFF + 28, N, TITLE, SUB)

def inline(html, is_prof):
    assert 'data-slide="%d"' % (OFF + 1) not in html, 'aula already inlined?'
    assert 'id="ex-lesson-%d"' % N not in html, 'ex-lesson already present?'
    # totalLessons: bump to N so Pre-class progress loop covers the new card
    html = re.sub(r'var totalLessons\s*=\s*\d+;', 'var totalLessons=%d;' % N, html, count=1)
    html = html.replace(PREV_STAMP, PREV_STAMP + '\n' + STAMP, 1)
    html = html.replace(PREV_CARD_CLOSE, PREV_CARD_CLOSE + '\n\n' + card, 1)
    html = html.replace('</div><!-- /tab-complementary -->', '\n' + compl + '\n</div><!-- /tab-complementary -->', 1)
    html = merge_audiomap(html, pairs)
    if is_prof:
        html = html.replace('</div><!-- /slides-container -->', s + '\n</div><!-- /slides-container -->', 1)
        html = re.sub(r'(var slidePhases = \{[^}]*?)\};', r'\1,' + phase_add + '};', html, count=1)
        html = html.replace(PREV_TOTSLIDES, NEW_TOTSLIDES)
        idx = html.index('</div><!-- /tab-inclass -->')
        cc = html.rfind('</div>', 0, idx)
        html = html[:cc] + CARD + '\n' + html[cc:]
    return html

write(PROF, inline(read(PROF), True))
write(ALUNO, inline(read(ALUNO), False))
print('OK aula%d inlined; phases %d; audioMap pairs %d' % (N, len(pmap), len(pairs)))
