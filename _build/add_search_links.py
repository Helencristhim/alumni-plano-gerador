#!/usr/bin/env python3
"""Adiciona link de BUSCA clicável aos cards de complementares que estão SEM
link. Preserva cards que já têm <a href>. Vídeo/série/youtube -> busca YouTube;
podcast -> busca Google. Não inventa URL (só link de busca pelo título exato).
Uso: add_search_links.py <arquivo.html> [...]"""
import re, sys
from urllib.parse import quote_plus
from html import unescape

def clean_title(t):
    t=re.sub(r'<[^>]+>','',t)
    t=unescape(t)                       # &amp;->& &mdash;->— etc
    t=t.replace('—',' ').replace('--',' ').replace('"','').strip()
    t=re.sub(r'\s+',' ',t)
    return t

def search_link(title, mid):
    suffix=mid.rsplit('-',1)[-1].lower()
    q=quote_plus(title)
    if suffix in ('podcast','listen'):
        url=f'https://www.google.com/search?q={q}'
        label='Find the podcast &#8599;'
    else:
        url=f'https://www.youtube.com/results?search_query={q}'
        label='Watch on YouTube &#8599;'
    return (f'<p style="margin-top:.4rem"><a href="{url}" target="_blank" rel="noopener" '
            f'style="font-size:.78rem;color:var(--accent);font-weight:600;text-decoration:none;'
            f'border-bottom:1px solid var(--accent)">{label}</a></p>')

def run(path):
    h=open(path,encoding='utf-8').read()
    ci=h.find('id="tab-complementary"')
    if ci<0: print(path,'-> sem tab-complementary'); return
    cj=h.find('<script', ci)
    head, seg, tail = h[:ci], h[ci:cj], h[cj:]
    out=[]; i=0; added=0; kept=0
    while True:
        j=seg.find('<div class="media-card-wrapper"', i)
        if j<0: out.append(seg[i:]); break
        out.append(seg[i:j])
        d=0; e=None
        for m in re.finditer(r'<div\b|</div>', seg[j:]):
            d+= 1 if m.group(0)=='<div' else -1
            if d==0: e=j+m.end(); break
        card=seg[j:e]
        if '<a ' in card and 'href=' in card:
            kept+=1                      # já tem link, preserva
        else:
            mid=re.search(r'data-media="([^"]+)"', card)
            h5=re.search(r'<h5[^>]*>(.*?)</h5>', card, re.S)
            if mid and h5:
                title=clean_title(h5.group(1))
                link=search_link(title, mid.group(1))
                # insere antes do </div> que fecha .media-info
                k=card.rfind('</div></div>')         # fecha media-info + media-card
                if k<0: k=card.rfind('</div>')
                card=card[:k]+link+card[k:]; added+=1
        out.append(card); i=e
    h2=head+''.join(out)+tail
    bal=len(re.findall(r'<div\b',h2))-h2.count('</div>')
    open(path,'w',encoding='utf-8').write(h2)
    print(f'{path.split("/")[-1]}: +{added} links de busca | {kept} já tinham | div-delta={bal}')

if __name__=='__main__':
    for p in sys.argv[1:]: run(p)
