#!/usr/bin/env python3
"""Reformata COMPLETO de aulas legadas (cohort antigo) para o markup do modelo:
header, stage-title -> section-header-row + wrapper exercise-section, survival.
(o vocab já é tratado por reformat_legacy_vocab.py — rode-o antes)
Conteúdo 100% preservado. Uso: reformat_legacy_full.py <arquivo.html> [...]"""
import re, sys

def fix_header(hdr):
    hdr=hdr.replace('class="lesson-header-info"','class="lesson-header-content"')
    hdr=re.sub(r'<div class="lesson-title">(.*?)</div>', r'<h3>\1</h3>', hdr, flags=re.S)
    hdr=hdr.replace('class="mini-progress"','class="lesson-progress-mini"')
    hdr=hdr.replace('class="mini-fill"','class="mini-bar-fill"')
    hdr=hdr.replace('class="mini-pct"','class="mini-percent"')
    hdr=hdr[:-6].rstrip()+'\n        <div class="expand-icon">&#9660;</div>\n      </div>'
    return hdr

def fix_body(body):
    # 1) stage-title -> section-header-row (badge vem depois do h4 no modelo)
    def st(m):
        badge=re.search(r'<span class="badge[^>]*>.*?</span>', m.group(1), re.S)
        title=re.sub(r'<span class="badge[^>]*>.*?</span>','',m.group(1),flags=re.S).strip()
        b=badge.group(0) if badge else ''
        return f'<div class="section-header-row"><h4>{title}</h4>{b}</div>'
    body=re.sub(r'<h4 class="stage-title">(.*?)</h4>', st, body, flags=re.S)
    # 2) survival
    body=body.replace('<h4 class="survival-title">','<h4>')
    # 3) embrulha cada etapa em exercise-section: do section-header-row até o próximo
    #    (ou até o survival-card / fim do body)
    parts=[]; positions=[m.start() for m in re.finditer(r'<div class="section-header-row">', body)]
    if not positions: return body
    surv=body.find('<div class="survival-card"')
    end_zone = surv if surv>0 else len(body)
    out=body[:positions[0]]
    for idx,p in enumerate(positions):
        seg_end = positions[idx+1] if idx+1<len(positions) else end_zone
        seg=body[p:seg_end]
        out+= '<div class="exercise-section">\n'+seg.rstrip()+'\n</div>\n'
    out+=body[end_zone:]
    return out

def run(path):
    h=open(path,encoding='utf-8').read()
    out=[]; i=0; hc=0; bc=0
    ANCHOR='<div class="lesson-card"'
    while True:
        j=h.find(ANCHOR, i)
        if j<0: out.append(h[i:]); break
        out.append(h[i:j])
        d=0; e=None
        for m in re.finditer(r'<div\b|</div>', h[j:]):
            d+= 1 if m.group(0)=='<div' else -1
            if d==0: e=j+m.end(); break
        card=h[j:e]
        if 'lesson-header-info' in card or 'stage-title' in card:   # legado
            # header
            ha=card.find('<div class="lesson-header" onclick="toggleLesson(this)">')
            if ha>=0:
                d=0; he=None
                for m in re.finditer(r'<div\b|</div>', card[ha:]):
                    d+= 1 if m.group(0)=='<div' else -1
                    if d==0: he=ha+m.end(); break
                card=card[:ha]+fix_header(card[ha:he])+card[he:]; hc+=1
            # body
            ba=card.find('<div class="lesson-body"')
            if ba>=0:
                d=0; be=None
                for m in re.finditer(r'<div\b|</div>', card[ba:]):
                    d+= 1 if m.group(0)=='<div' else -1
                    if d==0: be=ba+m.end(); break
                card=card[:ba]+fix_body(card[ba:be])+card[be:]; bc+=1
        out.append(card); i=e
    h=''.join(out)
    bal=len(re.findall(r'<div\b',h))-h.count('</div>')
    open(path,'w',encoding='utf-8').write(h)
    print(f'{path.split("/")[-1]}: headers={hc} bodies={bc} | div-delta={bal} | stage-title restantes={h.count("stage-title")} | lesson-header-info restantes={h.count("lesson-header-info")}')

if __name__=='__main__':
    for p in sys.argv[1:]: run(p)
