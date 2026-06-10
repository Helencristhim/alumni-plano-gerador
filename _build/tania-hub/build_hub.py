#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inline ALL of Tania's lessons (2-9) into the monolithic hub (prof + aluno),
matching the Elaine/Milton inline-monolith standard:
  - Pre-class: every lesson is an inline accordion (no link-out)
  - IN CLASS: every lesson's slides live in the hub; menu uses startLesson(start,end);
    slide nav has an Exit ("voltar pra lista") button via exitSlideMode()
Aula 1 (already inline) keeps its interactive engine. Aulas 2-9 are inlined STATIC/self-contained
to avoid collisions with aula1's globals:
  - dialogue -> all lines visible, Next Line removed
  - quick-fire -> static reveal cards (parsed from each lesson's `challenges` array)
  - grammar reveal -> relative (this.closest(...).querySelector('.grammar-table-wrap'))
  - spot-the-error -> self-contained this.classList.toggle('revealed')
  - listening 2-7 -> custom player kept, ids made unique per lesson (shared togglePlayer)
  - listening 8-9 -> shared playListenSeq(btn) + data-lines (sequence via speakText)
  - vocab/grammarTable/error ids made unique per lesson
NEVER regenerates content — only relocates + de-collides.
"""
import os, re, json, html as _html

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
def P(*a): return os.path.join(ROOT, 'public', *a)
def read(p):
    with open(p, encoding='utf-8') as f: return f.read()
def write(p, s):
    with open(p, 'w', encoding='utf-8') as f: f.write(s)

TITLES = {
 1:("Who Is Tânia?","Diagnostic + Personal Introduction"),
 2:("At the Airport","Navigating International Terminals"),
 3:("Hotel Check-In","Booking and Settling In"),
 4:("Getting Around","Directions and Transportation"),
 5:("At the Restaurant","Ordering Food and Handling the Bill"),
 6:("Shopping and Souvenirs","Prices, Sizes, and Bargaining"),
 7:("Cultural Conversations","Places, People, and Traditions"),
 8:("Emergency Situations","Health, Safety, and Asking for Help"),
 9:("Family Travel","Coordinating with Family"),
}
LEN = {1:30, 2:37,3:37,4:37,5:37,6:37,7:37,8:37,9:37}
START = {}; END = {}
acc = 1
for L in range(1,10):
    START[L] = acc; END[L] = acc + LEN[L] - 1; acc = END[L] + 1
TOTAL = END[9]

# ----------------------------- generic helpers -----------------------------
def balanced_div(s, start):
    """Return substring of one <div ...>...</div> starting at index `start`."""
    depth = 0; i = start; n = len(s)
    while i < n:
        if s.startswith('<div', i): depth += 1; i = s.index('>', i) + 1; continue
        if s.startswith('</div>', i):
            depth -= 1; i += 6
            if depth == 0: return s[start:i]
            continue
        i += 1
    raise ValueError('unbalanced from %d' % start)

def slides_of(html):
    a = html.index('<div class="slides-container" id="slidesContainer">') + len('<div class="slides-container" id="slidesContainer">')
    b = html.index('<div class="teacher-t"', a)
    body = html[a:b]
    body = body.rstrip()
    # strip the two wrapper closers (</slides-container></slides-wrapper>)
    body = re.sub(r'(\s*</div>){2}\s*$', '', body)
    return body.strip()

def preclass_card(html, L, closed=True):
    start = html.index('<div class="lesson-card open" id="ex-lesson-%d">' % L)
    card = balanced_div(html, start)
    if closed:
        card = card.replace('class="lesson-card open" id="ex-lesson-%d"' % L,
                            'class="lesson-card" id="ex-lesson-%d"' % L, 1)
    return card

def complementary_of(html):
    a = html.index('<div class="tab-content" id="tab-complementary">')
    inner = balanced_div(html, a)
    # strip the outer tab-content wrapper, keep inner content
    inner = inner[inner.index('>')+1 : inner.rindex('</div>')]
    return inner.strip()

def audiomap_pairs(html):
    blk = html[html.index('var audioMap = {'): html.index('\n};', html.index('var audioMap = {'))]
    return re.findall(r'\n\s*("(?:[^"\\]|\\.)*")\s*:\s*("(?:[^"\\]|\\.)*")', blk)

def parse_challenges(html):
    m = re.search(r'var challenges\s*=\s*\[(.*?)\];', html, re.S)
    if not m: return []
    body = m.group(1)
    out = []
    for pm in re.finditer(r"\{prompt:'((?:\\.|[^'\\])*)',answer:'((?:\\.|[^'\\])*)'\}", body):
        pr = pm.group(1).replace("\\'", "'").replace('\\\\', '\\')
        an = pm.group(2).replace("\\'", "'").replace('\\\\', '\\')
        out.append((pr, an))
    return out

def parse_listening_lines(html):
    arrs = re.findall(r'var lines=\[(.*?)\];', html, re.S)
    res = []
    for a in arrs:
        lines = [x.replace("\\'", "'").replace('\\\\', '\\')
                 for x in re.findall(r"'((?:\\.|[^'\\])*)'", a)]
        res.append(lines)
    return res

# ----------------------------- slide transforms -----------------------------
def split_slides(body):
    parts = re.split(r'(?=<div class="slide )', body)
    return [p for p in parts if p.strip()]

def open_tag(block):
    return block[:block.index('>')+1]

def rebuild_quickfire(block, L, challenges):
    tag = open_tag(block)
    cards = []
    for i,(pr,an) in enumerate(challenges, 1):
        cards.append('<div class="oral-item" onclick="this.classList.toggle(\'revealed\')">'
                     '<div class="oral-situation">%d. %s</div>'
                     '<div class="oral-model">%s</div></div>' % (i, pr, an))
    inner = ('<div class="slide-inner" style="overflow-y:auto;max-height:75vh">'
             '<div class="chapter-label">Chapter 5: Practice</div>'
             '<h2 class="slide-heading">Quick <span class="accent">Fire</span></h2>'
             '<p style="font-size:.9rem;color:var(--text-dim);margin-bottom:.8rem">Click on each card to reveal the answer.</p>'
             '<div class="oral-grid">' + ''.join(cards) + '</div></div>')
    return tag + '\n  ' + inner + '\n</div>\n'

def transform_lesson(html, L):
    body = slides_of(html)
    off = START[L] - 1
    challenges = parse_challenges(html)
    listen = parse_listening_lines(html)   # only for 8/9
    blocks = split_slides(body)
    out = []
    li = 0  # listening index for 8/9
    for k, blk in enumerate(blocks):
        # offset data-slide
        blk = re.sub(r'data-slide="(\d+)"', lambda m: 'data-slide="%d"' % (int(m.group(1))+off), blk)
        # data-lesson
        blk = re.sub(r'\s*data-lesson="\d+"', '', blk, count=1)
        blk = re.sub(r'(<div class="slide[^"]*"\s+data-slide="\d+")', r'\1 data-lesson="%d"' % L, blk, count=1)
        # drop ' active' from the slide tag (only the lesson's title slide has it; engine sets active)
        blk = re.sub(r'(<div class="slide[^"]*?)\s+active(")', r'\1\2', blk, count=1)
        # quick-fire -> static
        if 'id="challengeCard"' in blk:
            blk = rebuild_quickfire(blk, L, challenges)
            out.append(blk); continue
        # dialogue -> static
        if 'class="dialogue-box"' in blk or 'class="dialogue-line"' in blk:
            blk = blk.replace('class="dialogue-line" data-', 'class="dialogue-line visible" data-')
            blk = re.sub(r'<div style="text-align:center;margin-top:1rem"><button class="btn-primary" id="nextLineBtn".*?</button></div>', '', blk, flags=re.S)
        # grammar reveal -> relative + unique table id
        if 'revealGrammar()' in blk:
            blk = blk.replace('onclick="revealGrammar()"',
                              'onclick="this.closest(\'.slide-inner\').querySelector(\'.grammar-table-wrap\').classList.add(\'show\')"')
            blk = blk.replace('id="grammarTable"', 'id="grammarTable_%d"' % L)
        # spot-the-error -> self-contained
        if 'revealError(this)' in blk:
            blk = blk.replace('onclick="revealError(this)"', 'onclick="this.classList.toggle(\'revealed\')"')
            blk = blk.replace('id="errorGrid"', 'id="errorGrid_%d"' % L).replace('id="errorScore"', 'id="errorScore_%d"' % L)
        # vocab ids unique (cosmetic / HTML validity)
        blk = (blk.replace('id="vocabGrid1"', 'id="vocabGrid_%dA"' % L).replace('id="vocabGrid2"', 'id="vocabGrid_%dB"' % L)
                  .replace('id="vocabCount1"', 'id="vocabCount_%dA"' % L).replace('id="vocabCount2"', 'id="vocabCount_%dB"' % L))
        # listening 2-7: unique player ids (shared togglePlayer).
        # use negative lookahead so 'player-2' never matches inside a freshly-made 'player-2a'.
        if "togglePlayer('player-" in blk:
            for base in ('player', 'play-btn', 'progress', 'current-time', 'total-time'):
                blk = re.sub(base + r'-1(?![0-9a-z])', '%s-%da' % (base, L), blk)
                blk = re.sub(base + r'-2(?![0-9a-z])', '%s-%db' % (base, L), blk)
        # listening 8-9: toggleListening -> playListenSeq + data-lines
        if 'toggleListening1(this)' in blk or 'toggleListening2(this)' in blk:
            lines = listen[li] if li < len(listen) else []
            li += 1
            dl = json.dumps(lines, ensure_ascii=False).replace('"', '&quot;')
            blk = re.sub(r'onclick="toggleListening[12]\(this\)"', 'onclick="playListenSeq(this)" data-lines="%s"' % dl, blk, count=1)
            blk = re.sub(r'\s*id="listening[12]PlayBtn"', '', blk, count=1)
        out.append(blk)
    return '\n'.join(out)

# ----------------------------- engine JS -----------------------------
def build_phase_map(all_slides_html, aula1_phases):
    pm = dict(aula1_phases)
    for m in re.finditer(r'data-slide="(\d+)"[^>]*data-phase="(\d+)"', all_slides_html):
        pm[int(m.group(1))] = int(m.group(2))
    return pm

PLAYLISTEN = (
"function playListenSeq(btn){if(btn.dataset.playing)return;btn.dataset.playing='1';"
"var slide=btn.closest('.slide');var wf=slide.querySelector('.waveform');if(wf)wf.classList.remove('waveform-paused');"
"var lines=[];try{lines=JSON.parse(btn.getAttribute('data-lines'))}catch(e){}"
"var d=0;lines.forEach(function(l){setTimeout(function(){speakText(l,btn)},d);d+=4200});"
"setTimeout(function(){if(wf)wf.classList.add('waveform-paused');btn.dataset.playing='';"
"var q=slide.querySelector('.comp-questions');if(q){q.style.display='flex';q.style.flexDirection='column';}},d+1500);}\n")

EXIT_BTN = ('  <button class="nav-btn" onclick="exitSlideMode()" title="Voltar à lista de aulas" aria-label="Voltar" style="margin-right:auto">'
            '<svg viewBox="0 0 24 24"><line x1="19" y1="12" x2="5" y2="12"/><polyline points="12 19 5 12 12 5"/></svg></button>\n')

def inclass_card(L):
    s,e = START[L], END[L]; t,sub = TITLES[L]
    return ('    <div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" onclick="startLesson(%d,%d)" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
            '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">%02d</div>\n'
            '      <div><div style="font-weight:600;font-size:.95rem">%s</div><div style="font-size:.8rem;color:var(--text-dim)">%s &mdash; %d slides</div></div>\n'
            '    </div>') % (s, e, L, t, sub, LEN[L])

# ============================ load sources ============================
MONO = read(P('professor','tania-rosa.html'))
MONO_A = read(P('aluno','tania-rosa.html'))
STD = {L: read(P('professor','tania-rosa-aula%d.html'%L)) for L in range(2,10)}
STD_A = {L: read(P('aluno','tania-rosa-aula%d.html'%L)) for L in range(2,10)}

# aula1 existing slidePhases
m1 = re.search(r'var slidePhases=\{([^}]*)\}', MONO)
aula1_phases = {}
for a,b in re.findall(r'(\d+):(\d+)', m1.group(1)):
    if 1 <= int(a) <= 30: aula1_phases[int(a)] = int(b)

# transform lessons 2-9
xslides = {L: transform_lesson(STD[L], L) for L in range(2,10)}
all_new_slides = '\n\n'.join(xslides[L] for L in range(2,10))

# sanity: renumber boundaries
for L in range(2,10):
    assert ('data-slide="%d"' % START[L]) in xslides[L], 'L%d start %d missing' % (L,START[L])
    assert ('data-slide="%d"' % END[L]) in xslides[L], 'L%d end %d missing' % (L,END[L])

pmap = build_phase_map(all_new_slides, aula1_phases)
assert len(pmap) == TOTAL, 'phase map %d != %d' % (len(pmap), TOTAL)
slidephases_js = 'var slidePhases={' + ','.join('%d:%d'%(k,pmap[k]) for k in sorted(pmap)) + '};'

# extra audioMap entries: aula8 listening-2 fragments (were TTS in the standalone; now real MP3s)
EXTRA_AUDIO = [
 ('"I need some help, please."', '"/audio/tania-rosa-aula8/i_need_some_help_please.mp3"'),
 ('"You need to take it twice a day."', '"/audio/tania-rosa-aula8/you_need_to_take_it_twice_a_day.mp3"'),
 ('"You have to take it after meals."', '"/audio/tania-rosa-aula8/you_have_to_take_it_after_meals.mp3"'),
 ('"You need to see a doctor."', '"/audio/tania-rosa-aula8/you_need_to_see_a_doctor.mp3"'),
]

# audioMap union (aula1 already present in MONO; add 2-9 + extras)
def merge_audiomap(html):
    ins = html.index('var audioMap = {') + len('var audioMap = {')
    existing = html[html.index('var audioMap = {'): html.index('\n};', html.index('var audioMap = {'))]
    add = []; seen = set()
    for k,v in [p for L in range(2,10) for p in audiomap_pairs(STD[L])] + EXTRA_AUDIO:
        if k in seen: continue
        seen.add(k)
        if ('\n  %s:' % k) in existing or ('{%s:' % k) in existing: continue
        add.append('\n  %s: %s,' % (k,v))
    return html[:ins] + ''.join(add) + html[ins:]

# ============================ PROFESSOR ============================
prof = MONO
# 1) data-lesson="1" on aula1 slides
prof = re.sub(r'(<div class="slide[^"]*" data-slide="\d+")(?![^>]*data-lesson)', r'\1 data-lesson="1"', prof)
# 2) engine swap
prof = prof.replace(
 "function enterSlideMode(){document.body.classList.add('slide-mode');if(currentSlide)goToSlide(currentSlide);else goToSlide(1)}",
 "var lessonStartSlide=1,lessonEndSlide=30;\n"
 "function startLesson(s,e){lessonStartSlide=s;lessonEndSlide=e;document.body.classList.add('slide-mode');goToSlide(s)}\n"
 "function exitSlideMode(){document.body.classList.remove('slide-mode');document.querySelectorAll('.tab-content').forEach(function(t){t.classList.remove('active')});var ic=document.getElementById('tab-inclass');if(ic)ic.classList.add('active');document.querySelectorAll('.tab-btn').forEach(function(b){b.classList.remove('active');if((b.getAttribute('onclick')||'').indexOf('inclass')>-1)b.classList.add('active')});window.scrollTo({top:0})}\n"
 "function enterSlideMode(){startLesson(1,30)}\n" + PLAYLISTEN, 1)
assert 'function startLesson' in prof, 'engine swap failed'
prof = prof.replace('var totalSlides=30;', 'var totalSlides=%d;' % TOTAL, 1)
prof = re.sub(r'var slidePhases=\{[^}]*\};', slidephases_js, prof, count=1)
prof = prof.replace(
 "function changeSlide(dir){var next=currentSlide+dir;if(next<1||next>totalSlides)return;goToSlide(next)}",
 "function changeSlide(dir){var next=currentSlide+dir;if(next<lessonStartSlide||next>lessonEndSlide)return;goToSlide(next)}", 1)
prof = re.sub(
 r"function updateNav\(\)\{document\.getElementById\('slideCounter'\)\.textContent=[^}]*?dots\.forEach\([^}]*\}\)\}",
 "function updateNav(){var rel=currentSlide-lessonStartSlide+1,tot=lessonEndSlide-lessonStartSlide+1;document.getElementById('slideCounter').textContent=String(rel).padStart(2,'0')+' / '+String(tot).padStart(2,'0');document.getElementById('prevBtn').disabled=currentSlide<=lessonStartSlide;document.getElementById('nextBtn').disabled=currentSlide>=lessonEndSlide}",
 prof, count=1)
assert 'lessonStartSlide+1' in prof, 'updateNav swap failed'
# remove dots IIFE
prof = re.sub(r"\(function\(\)\{var dotsEl=document\.getElementById\('slideDots'\);.*?\}\)\(\);", '', prof, count=1, flags=re.S)
# exit button in nav-bar (before prevBtn)
prof = prof.replace('<div class="nav-bar">\n  <button class="nav-btn" id="prevBtn"',
                    '<div class="nav-bar">\n' + EXIT_BTN + '  <button class="nav-btn" id="prevBtn"', 1)
# 3) IN CLASS menu rebuild
ic_start = prof.index('<div style="display:flex;flex-direction:column;gap:1rem">', prof.index('id="tab-inclass"'))
ic_div = balanced_div(prof, ic_start)
new_ic = '<div style="display:flex;flex-direction:column;gap:1rem">\n' + '\n'.join(inclass_card(L) for L in range(1,10)) + '\n  </div>'
prof = prof[:ic_start] + new_ic + prof[ic_start+len(ic_div):]
# 4) Pre-class: replace link cards 2-9 with inline accordions
for L in range(2,10):
    st = prof.index('<div class="lesson-card" id="ex-lesson-%d">' % L)
    old = balanced_div(prof, st)
    acc_card = preclass_card(STD[L], L, closed=True)
    prof = prof[:st] + acc_card + prof[st+len(old):]
# 5) complementary: append lessons 2-9 before close of tab-complementary
tc = prof.index('<div class="tab-content" id="tab-complementary">')
tc_block = balanced_div(prof, tc)
tc_end = tc + len(tc_block)
extra_comp = ''.join('\n<hr style="border:none;border-top:1px solid var(--border);margin:2rem 0">\n' + complementary_of(STD[L]) for L in range(2,10))
prof = prof[:tc_end-len('</div>')] + extra_comp + '\n' + prof[tc_end-len('</div>'):]
# 6) slides: append 2-9 before slides-container close
CLOSE = '\n\n</div>\n</div>\n\n<div class="teacher-t" id="teacherT">'
assert prof.count(CLOSE) == 1, 'slides-container close marker not unique (%d)' % prof.count(CLOSE)
prof = prof.replace(CLOSE, '\n\n' + all_new_slides + CLOSE, 1)
# totalLessons
prof = prof.replace('var totalLessons=1;', 'var totalLessons=9;')
# audioMap
prof = merge_audiomap(prof)

write(P('professor','tania-rosa.html'), prof)

# ============================ ALUNO ============================
aluno = MONO_A
for L in range(2,10):
    st = aluno.index('<div class="lesson-card" id="ex-lesson-%d">' % L)
    old = balanced_div(aluno, st)
    acc_card = preclass_card(STD_A[L], L, closed=True)
    aluno = aluno[:st] + acc_card + aluno[st+len(old):]
tc = aluno.index('<div class="tab-content" id="tab-complementary">')
tc_block = balanced_div(aluno, tc); tc_end = tc + len(tc_block)
extra_comp = ''.join('\n<hr style="border:none;border-top:1px solid var(--border);margin:2rem 0">\n' + complementary_of(STD_A[L]) for L in range(2,10))
aluno = aluno[:tc_end-len('</div>')] + extra_comp + '\n' + aluno[tc_end-len('</div>'):]
aluno = aluno.replace('var totalLessons=1;', 'var totalLessons=9;')
# aluno audioMap union
ins = aluno.index('var audioMap = {') + len('var audioMap = {')
existing = aluno[aluno.index('var audioMap = {'): aluno.index('\n};', aluno.index('var audioMap = {'))]
add=[]; seen=set()
for L in range(2,10):
    for k,v in audiomap_pairs(STD_A[L]):
        if k in seen: continue
        seen.add(k)
        if ('\n  %s:'%k) in existing: continue
        add.append('\n  %s: %s,'%(k,v))
aluno = aluno[:ins] + ''.join(add) + aluno[ins:]
write(P('aluno','tania-rosa.html'), aluno)

print('OK — Tânia inline monolith built')
print('  lessons:', {L:(START[L],END[L]) for L in range(1,10)})
print('  total slides:', TOTAL, '| phase map:', len(pmap))
print('  prof bytes:', len(prof), '| aluno bytes:', len(aluno))
