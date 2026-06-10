#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inline Aula 10 into the Tânia hub (prof + aluno), matching the inline-monolith standard.
Reads the current hub (lessons 1-9, 326 slides) + standalone aula10, appends aula10 as
slides 327-363 (data-lesson=10), accordion ex-lesson-10, startLesson(327,363) menu card,
stamp10, audioMap union, slidePhases. Aula 10 slides are de-collided self-contained:
static dialogue, static quick-fire (from challenges), listening -> playListenSeq + data-lines,
grammar relative, spot-the-error self-contained, unique vocab/grammarTable/error ids.
Idempotent guard: refuses if ex-lesson-10 already present.
"""
import os, re, json
def P(*a): return os.path.join(os.path.dirname(__file__), '..', '..', 'public', *a)
def read(p): return open(os.path.abspath(p), encoding='utf-8').read()
def write(p, s): open(os.path.abspath(p), 'w', encoding='utf-8').write(s)

L, START, END = 10, 327, 363
OFF = START - 1

HUB_P, HUB_A = P('professor','tania-rosa.html'), P('aluno','tania-rosa.html')
STD_P = read(P('professor','tania-rosa-aula10.html'))
STD_A = read(P('aluno','tania-rosa-aula10.html'))
hub_p, hub_a = read(HUB_P), read(HUB_A)
assert 'id="ex-lesson-10"' not in hub_p, 'aula10 already inlined'

# ---------- helpers ----------
def balanced_div(s, start):
    depth=0; i=start; n=len(s)
    while i<n:
        if s.startswith('<div',i): depth+=1; i=s.index('>',i)+1; continue
        if s.startswith('</div>',i):
            depth-=1; i+=6
            if depth==0: return s[start:i]
            continue
        i+=1
    raise ValueError('unbalanced')

def slides_of(html):
    a=html.index('<div class="slides-container" id="slidesContainer">')+len('<div class="slides-container" id="slidesContainer">')
    b=html.index('<div class="teacher-t"',a)
    body=re.sub(r'(\s*</div>){2}\s*$','',html[a:b].rstrip())
    return body.strip()

def preclass_card(html, closed=True):
    st=html.index('<div class="lesson-card open" id="ex-lesson-10">')
    card=balanced_div(html, st)
    if closed: card=card.replace('class="lesson-card open" id="ex-lesson-10"','class="lesson-card" id="ex-lesson-10"',1)
    return card

def complementary_of(html):
    a=html.index('<div class="tab-content" id="tab-complementary">')
    inner=balanced_div(html,a)
    return inner[inner.index('>')+1:inner.rindex('</div>')].strip()

def audiomap_pairs(html):
    blk=html[html.index('var audioMap = {'):html.index('\n};',html.index('var audioMap = {'))]
    return re.findall(r'\n\s*("(?:[^"\\]|\\.)*")\s*:\s*("(?:[^"\\]|\\.)*")', blk)

def dialogue_lines(html):
    i=html.index('class="dialogue-box"'); s=html.rfind('<div class="slide ',0,i)
    e=html.find('<div class="slide ',i); e=e if e!=-1 else len(html)
    return [t.replace("\\'","'") for t in re.findall(r"audio-inline\" onclick=\"speakText\('((?:[^'\\]|\\.)*)'",html[s:e])]

def parse_challenges(html):
    m=re.search(r'var challenges\s*=\s*\[(.*?)\];',html,re.S)
    out=[]
    for pm in re.finditer(r"\{prompt:'((?:\\.|[^'\\])*)',answer:'((?:\\.|[^'\\])*)'\}",m.group(1)):
        out.append((pm.group(1).replace("\\'","'").replace('\\\\','\\'), pm.group(2).replace("\\'","'").replace('\\\\','\\')))
    return out

def listening_lines(html):
    return [[x.replace("\\'","'").replace('\\\\','\\') for x in re.findall(r"'((?:\\.|[^'\\])*)'",a)]
            for a in re.findall(r'var lines=\[(.*?)\];',html,re.S)]

def waveform_player(dlines):
    dl=json.dumps(dlines,ensure_ascii=False).replace('"','&quot;')
    bars=''.join('<div class="bar"></div>' for _ in range(12))
    return ('<div class="waveform waveform-paused">'+bars+'</div>\n'
            '    <button class="play-btn" onclick="playListenSeq(this)" data-lines="'+dl+'">'
            '<svg class="icon-play" viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"/></svg>'
            '<svg class="icon-pause" viewBox="0 0 24 24" style="display:none"><rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/></svg>'
            '</button>')

def rebuild_quickfire(block, challenges):
    tag=block[:block.index('>')+1]
    cards=''.join('<div class="oral-item" onclick="this.classList.toggle(\'revealed\')"><div class="oral-situation">%d. %s</div><div class="oral-model">%s</div></div>'%(i,pr,an)
                  for i,(pr,an) in enumerate(challenges,1))
    inner=('<div class="slide-inner" style="overflow-y:auto;max-height:75vh"><div class="chapter-label">Chapter 5: Practice</div>'
           '<h2 class="slide-heading">Quick <span class="accent">Fire</span></h2>'
           '<p style="font-size:.9rem;color:var(--text-dim);margin-bottom:.8rem">Click on each card to reveal the answer.</p>'
           '<div class="oral-grid">'+cards+'</div></div>')
    return tag+'\n  '+inner+'\n</div>\n'

def transform(html):
    body=slides_of(html); ch=parse_challenges(html); listen=listening_lines(html)
    blocks=[p for p in re.split(r'(?=<div class="slide )',body) if p.strip()]
    out=[]; li=0
    for blk in blocks:
        blk=re.sub(r'data-slide="(\d+)"',lambda m:'data-slide="%d"'%(int(m.group(1))+OFF),blk)
        blk=re.sub(r'\s*data-lesson="\d+"','',blk,count=1)
        blk=re.sub(r'(<div class="slide[^"]*"\s+data-slide="\d+")',r'\1 data-lesson="%d"'%L,blk,count=1)
        blk=re.sub(r'(<div class="slide[^"]*?)\s+active(")',r'\1\2',blk,count=1)
        if 'id="challengeCard"' in blk:
            out.append(rebuild_quickfire(blk,ch)); continue
        if 'class="dialogue-box"' in blk:
            blk=blk.replace('class="dialogue-line" data-','class="dialogue-line visible" data-')
            blk=re.sub(r'<div style="text-align:center;margin-top:1rem"><button class="btn-primary" id="nextLineBtn".*?</button></div>','',blk,flags=re.S)
        if 'revealGrammar()' in blk:
            blk=blk.replace('onclick="revealGrammar()"','onclick="this.closest(\'.slide-inner\').querySelector(\'.grammar-table-wrap\').classList.add(\'show\')"').replace('id="grammarTable"','id="grammarTable_%d"'%L)
        if 'revealError(this)' in blk:
            blk=blk.replace('onclick="revealError(this)"','onclick="this.classList.toggle(\'revealed\')"').replace('id="errorGrid"','id="errorGrid_%d"'%L).replace('id="errorScore"','id="errorScore_%d"'%L)
        blk=(blk.replace('id="vocabGrid1"','id="vocabGrid_%dA"'%L).replace('id="vocabGrid2"','id="vocabGrid_%dB"'%L)
                .replace('id="vocabCount1"','id="vocabCount_%dA"'%L).replace('id="vocabCount2"','id="vocabCount_%dB"'%L))
        if 'toggleListening1(this)' in blk or 'toggleListening2(this)' in blk:
            lines=listen[li] if li<len(listen) else []; li+=1
            dl=json.dumps(lines,ensure_ascii=False).replace('"','&quot;')
            blk=re.sub(r'onclick="toggleListening[12]\(this\)"','onclick="playListenSeq(this)" data-lines="%s"'%dl,blk,count=1)
            blk=re.sub(r'\s*id="listening[12]PlayBtn"','',blk,count=1)
        out.append(blk)
    return '\n'.join(out)

xslides = transform(STD_P)
assert ('data-slide="%d"'%START) in xslides and ('data-slide="%d"'%END) in xslides, 'renumber failed'

# slidePhases additions
padd=','.join('%d:%d'%(int(a),int(b)) for a,b in re.findall(r'data-slide="(\d+)"[^>]*data-phase="(\d+)"',xslides))

# menu card
def inclass_card():
    return ('    <div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" onclick="startLesson(%d,%d)" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
            '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">10</div>\n'
            '      <div><div style="font-weight:600;font-size:.95rem">Putting It All Together</div><div style="font-size:.8rem;color:var(--text-dim)">Review and Confidence &mdash; 37 slides</div></div>\n'
            '    </div>') % (START, END)

STAMP10 = '<div class="stamp" id="stamp10" data-label="Mastery" style="background-image:url(\'https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=200&q=80\')"></div>'
CLOSE = '\n\n</div>\n</div>\n\n<div class="teacher-t" id="teacherT">'

def patch_prof(h):
    # stamp10 after stamp9
    h=h.replace('<div class="stamp" id="stamp9" data-label="Family"',
                STAMP10.replace('id="stamp10"','id="stamp10"')+'\n<div class="stamp" id="stamp9" data-label="Family"',1) if False else h
    h=re.sub(r'(<div class="stamp" id="stamp9"[^>]*></div>)', r'\1\n'+STAMP10, h, count=1)
    # pre-class accordion after ex-lesson-9 card
    st=h.index('<div class="lesson-card" id="ex-lesson-9">'); card9=balanced_div(h,st)
    ins=st+len(card9)
    h=h[:ins]+'\n\n'+preclass_card(STD_P)+h[ins:]
    # IN CLASS menu card after lesson-9 startLesson card
    m=re.search(r'(onclick="startLesson\(290,326\)".*?</div>\s*</div>)', h, re.S)
    h=h[:m.end()]+'\n'+inclass_card()+h[m.end():]
    # slides
    assert h.count(CLOSE)==1
    h=h.replace(CLOSE,'\n\n'+xslides+CLOSE,1)
    # slidePhases + totals
    h=re.sub(r'(var slidePhases=\{[^}]*?)\};', r'\1,'+padd+'};', h, count=1)
    h=h.replace('var totalSlides=326;','var totalSlides=363;')
    h=h.replace('var totalLessons=9;','var totalLessons=10;')
    # audioMap union
    ins2=h.index('var audioMap = {')+len('var audioMap = {')
    existing=h[h.index('var audioMap = {'):h.index('\n};',h.index('var audioMap = {'))]
    add=[]; seen=set()
    for k,v in audiomap_pairs(STD_P):
        if k in seen: continue
        seen.add(k)
        if ('\n  %s:'%k) in existing: continue
        add.append('\n  %s: %s,'%(k,v))
    h=h[:ins2]+''.join(add)+h[ins2:]
    # complementary
    tc=h.index('<div class="tab-content" id="tab-complementary">'); tcb=balanced_div(h,tc); tce=tc+len(tcb)
    extra='\n<hr style="border:none;border-top:1px solid var(--border);margin:2rem 0">\n'+complementary_of(STD_P)
    h=h[:tce-len('</div>')]+extra+'\n'+h[tce-len('</div>'):]
    return h

def patch_aluno(h):
    h=re.sub(r'(<div class="stamp" id="stamp9"[^>]*></div>)', r'\1\n'+STAMP10, h, count=1)
    st=h.index('<div class="lesson-card" id="ex-lesson-9">'); card9=balanced_div(h,st); ins=st+len(card9)
    h=h[:ins]+'\n\n'+preclass_card(STD_A)+h[ins:]
    h=h.replace('var totalLessons=9;','var totalLessons=10;')
    ins2=h.index('var audioMap = {')+len('var audioMap = {')
    existing=h[h.index('var audioMap = {'):h.index('\n};',h.index('var audioMap = {'))]
    add=[]; seen=set()
    for k,v in audiomap_pairs(STD_A):
        if k in seen: continue
        seen.add(k)
        if ('\n  %s:'%k) in existing: continue
        add.append('\n  %s: %s,'%(k,v))
    h=h[:ins2]+''.join(add)+h[ins2:]
    tc=h.index('<div class="tab-content" id="tab-complementary">'); tcb=balanced_div(h,tc); tce=tc+len(tcb)
    extra='\n<hr style="border:none;border-top:1px solid var(--border);margin:2rem 0">\n'+complementary_of(STD_A)
    h=h[:tce-len('</div>')]+extra+'\n'+h[tce-len('</div>'):]
    return h

write(HUB_P, patch_prof(hub_p))
write(HUB_A, patch_aluno(hub_a))
print('OK — aula10 inlined into hub (slides %d-%d)' % (START, END))
print('  phase additions:', len(padd.split(',')))
