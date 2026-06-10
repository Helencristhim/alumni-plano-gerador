#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inline Aula 15 into the Elaine monolith (prof+aluno). Also EXTENDS the revealVocab
counterMap past 14 (vocabGrid15..30) so a15+ vocab counters work."""
import os, re, json
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
PROF = os.path.join(ROOT, 'public', 'professor', 'elaine-mieko-pinho.html')
ALUNO = os.path.join(ROOT, 'public', 'aluno', 'elaine-mieko-pinho.html')
A = os.path.join(ROOT, 'public', 'professor', 'elaine-mieko-pinho-aula15.html')
N = 15; OFF = 28 * (N - 1)            # 392
VG = (15, 16)
TITLE = 'Shopping -- Stores'; SUB = 'Sizes, colors &amp; prices'
STAMP = '<div class="stamp" id="stamp15" data-label="Shopping" style="background-image:url(\'https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=200&q=80\')"></div>'
PREV_STAMP = '<div class="stamp" id="stamp14" data-label="Transport" style="background-image:url(\'https://images.unsplash.com/photo-1556122071-e404eaedb77f?w=200&q=80\')"></div>'
PREV_TOTLESS = 'var totalLessons = 14;'; NEW_TOTLESS = 'var totalLessons = 15;'
PREV_TOTSLIDES = 'var totalSlides = 392;'; NEW_TOTSLIDES = 'var totalSlides = 420;'
PREV_CARD_CLOSE = '</div><!-- /lesson-card L14 -->'

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()
def write(p, s):
    with open(p, 'w', encoding='utf-8') as f: f.write(s)
def between(s, a, b):
    i = s.index(a) + len(a); return s[i:s.index(b, i)]

a = read(A)
preclass = read(os.path.join(HERE, 'preclass.html'))
compl = read(os.path.join(HERE, 'complementary.html')).strip()
phrases = json.loads(read(os.path.join(HERE, 'phrases.json')))

s = between(a, '<div class="slides-container" id="slidesContainer">', '</div><!-- /slides-container -->')
s = re.sub(r'data-slide="(\d+)"', lambda m: 'data-slide="%d"' % (int(m.group(1)) + OFF), s)
s = s.replace('class="slide active ', 'class="slide ')
s = s.replace('class="dialogue-line" data-line', 'class="dialogue-line visible" data-line')
s = re.sub(r'<button class="primary-btn" id="nextLineBtn"[^>]*>Next Line</button>', '', s)
s = s.replace('id="vocabGrid1"', 'id="vocabGrid%d"' % VG[0]).replace('id="vocabGrid2"', 'id="vocabGrid%d"' % VG[1])
s = s.replace('id="vocabCount1"', 'id="vocabCount%d"' % VG[0]).replace('id="vocabCount2"', 'id="vocabCount%d"' % VG[1])
assert s.count('data-slide="%d"' % (OFF + 1)) == 1 and s.count('data-slide="%d"' % (OFF + 28)) == 1

pmap = {int(m.group(1)): int(m.group(2)) for m in re.finditer(r'data-slide="(\d+)"[^>]*data-phase="(\d+)"', s)}
assert len(pmap) == 28
phase_add = ','.join('%d:%d' % (k, pmap[k]) for k in sorted(pmap))

card = preclass[preclass.index('<div class="lesson-card" id="ex-lesson-%d">' % N): preclass.index('</div><!-- /lesson-card L%d -->' % N) + len('</div><!-- /lesson-card L%d -->' % N)]
pairs = [(json.dumps(p['key'], ensure_ascii=False), json.dumps('/audio/elaine-mieko-pinho/' + p['file'], ensure_ascii=False)) for p in phrases]

# counterMap extension (idempotent): add vocabGrid15..30
CM_ANCHOR = "'vocabGrid14':'vocabCount14'"
CM_EXT = ',' + ','.join("'vocabGrid%d':'vocabCount%d'" % (i, i) for i in range(15, 31))

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
    html = html.replace(PREV_TOTLESS, NEW_TOTLESS)
    html = html.replace(PREV_STAMP, PREV_STAMP + '\n' + STAMP, 1)
    html = html.replace(PREV_CARD_CLOSE, PREV_CARD_CLOSE + '\n\n' + card, 1)
    html = html.replace('</div><!-- /tab-complementary -->', '\n' + compl + '\n</div><!-- /tab-complementary -->', 1)
    if 'vocabGrid15' not in html:
        html = html.replace(CM_ANCHOR, CM_ANCHOR + CM_EXT, 1)
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
