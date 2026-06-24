#!/usr/bin/env python3
"""Aplica links DIRETOS resolvidos: para cada card de complementares cujo
(tipo,título) foi resolvido como 'exato' ou 'podcast-show', troca o link de
BUSCA pela URL real + rótulo por domínio. Preserva links já diretos e os
'video-canal'/'none' (ficam na busca).
Uso: apply_direct_links.py <map.json> <uniq.json> <arquivo.html> [...]"""
import re, sys, json
from html import unescape

resolved=json.load(open(sys.argv[1]))   # idx -> {url,kind}
uniq=json.load(open(sys.argv[2]))        # lista [{type,title,n}]
# (type,title) -> url  só p/ exato + podcast-show
DIRECT={}
for i,item in enumerate(uniq):
    r=resolved.get(str(i)) or resolved.get(i)
    if r and r.get('url') and r.get('kind') in ('exato','podcast-show'):
        DIRECT[(item['type'].strip(), item['title'].strip())]=r['url']

def label_for(url):
    if 'ted.com' in url: return 'Watch on TED &#8599;'
    if 'youtube.com' in url or 'youtu.be' in url: return 'Watch on YouTube &#8599;'
    if 'open.spotify.com' in url: return 'Listen on Spotify &#8599;'
    if 'podcasts.apple.com' in url: return 'Listen on Apple Podcasts &#8599;'
    if 'hbr.org' in url: return 'Listen on HBR &#8599;'
    if 'culips' in url: return 'Listen on Culips &#8599;'
    return 'Open &#8599;'

def key_of(card):
    t=re.search(r'<div class="media-type">(.*?)</div>', card, re.S)
    h=re.search(r'<h5[^>]*>(.*?)</h5>', card, re.S)
    if not (t and h): return None
    typ=re.sub('<[^>]+>','',t.group(1)).strip()
    title=unescape(re.sub('<[^>]+>','',h.group(1))).strip()
    return (typ,title)

def run(path):
    h=open(path,encoding='utf-8').read()
    ci=h.find('id="tab-complementary"')
    if ci<0: print(path,'-> sem aba'); return
    cj=h.find('<script',ci)
    head, seg, tail = h[:ci], h[ci:cj], h[cj:]
    out=[]; i=0; swapped=0
    while True:
        j=seg.find('<div class="media-card-wrapper"', i)
        if j<0: out.append(seg[i:]); break
        out.append(seg[i:j])
        d=0; e=None
        for m in re.finditer(r'<div\b|</div>', seg[j:]):
            d+= 1 if m.group(0)=='<div' else -1
            if d==0: e=j+m.end(); break
        card=seg[j:e]
        k=key_of(card)
        if k and k in DIRECT:
            url=DIRECT[k]; lab=label_for(url)
            # troca SÓ o link de busca (results/search) por direto
            def rep(mm):
                href=mm.group(1)
                if 'youtube.com/results' in href or 'google.com/search' in href:
                    inner=re.sub(r'>([^<]*)</a>', '>'+lab+'</a>', mm.group(0))
                    return inner.replace(href, url, 1)
                return mm.group(0)
            new=re.sub(r'<a [^>]*href="([^"]+)"[^>]*>.*?</a>', rep, card, flags=re.S)
            if new!=card: swapped+=1; card=new
        out.append(card); i=e
    h2=head+''.join(out)+tail
    bal=len(re.findall(r'<div\b',h2))-h2.count('</div>')
    open(path,'w',encoding='utf-8').write(h2)
    print(f'{path.split("/")[-1]}: {swapped} links diretos aplicados | div-delta={bal}')

if __name__=='__main__':
    for p in sys.argv[3:]: run(p)
