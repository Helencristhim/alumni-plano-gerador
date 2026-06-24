#!/usr/bin/env python3
"""Reformata vocab LEGADO (vocab-card-pc > vocab-word/def/example) para o
markup do MODELO (vocab-card-pc > vocab-card-content > header + example),
troca o container vocab-grid-preclass -> vocab-cards e remove o display:none
inline dos lesson-body legados. Conteúdo 100% preservado.
Uso: reformat_legacy_vocab.py <arquivo.html> [...]"""
import re, sys

def transform_card(block):
    word=re.search(r'class="vocab-word">(.*?)</div>', block, re.S)
    deff=re.search(r'class="vocab-def">(.*?)</div>', block, re.S)
    ex  =re.search(r'class="vocab-example">(.*?)</div>', block, re.S)
    btn =re.search(r'<button class="audio-btn".*?</button>', block, re.S)
    if not (word and deff): return block
    w=word.group(1).strip(); d=deff.group(1).strip(); e=ex.group(1).strip() if ex else ''
    b=btn.group(0) if btn else ''
    inner=(f'<div class="vocab-card-content"><div class="vocab-card-header">'
           f'<span class="vocab-card-word">{w}</span><span class="vocab-card-dot"> -- </span>'
           f'<span class="vocab-card-def">{d}</span></div>')
    if e: inner+=f'<div class="vocab-card-example">{e}</div>'
    inner+='</div>'+b
    return f'<div class="vocab-card-pc">{inner}</div>'

def run(path):
    h=open(path,encoding='utf-8').read()
    out=[]; i=0; cnt=0
    while True:
        j=h.find('<div class="vocab-card-pc">', i)
        if j<0: out.append(h[i:]); break
        out.append(h[i:j])
        d=0; e=None
        for m in re.finditer(r'<div\b|</div>', h[j:]):
            d+= 1 if m.group(0)=='<div' else -1
            if d==0: e=j+m.end(); break
        block=h[j:e]
        if 'class="vocab-word"' in block:
            block=transform_card(block); cnt+=1
        out.append(block); i=e
    h=''.join(out)
    h=h.replace('class="vocab-grid-preclass"','class="vocab-cards"')
    h=h.replace('class="lesson-body" style="display:none"','class="lesson-body"')
    bal=len(re.findall(r'<div\b',h))-h.count('</div>')
    open(path,'w',encoding='utf-8').write(h)
    print(f'{path.split("/")[-1]}: {cnt} cards reformatados | div-delta={bal}')

if __name__=='__main__':
    for p in sys.argv[1:]: run(p)
