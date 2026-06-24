#!/usr/bin/env python3
"""Uniformiza a aba Complementares no padrão do modelo (helen-mendes).
Reconstrói todos os cards na estrutura media-card/media-thumb/media-info,
agrupa por aula em .media-grid, e injeta o CSS .media-* do modelo.
Idempotente. Uso: fix_compl_uniform.py <arquivo.html> [...]"""
import re, sys

SVG = {
    'video':   '<svg viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg>',
    'youtube': '<svg viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg>',
    'series':  '<svg viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2"/><polyline points="8 21 16 21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>',
    'podcast': '<svg viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2"><rect x="9" y="2" width="6" height="11" rx="3"/><path d="M5 10a7 7 0 0 0 14 0"/><line x1="12" y1="19" x2="12" y2="22"/></svg>',
    'listen':  '<svg viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2"><path d="M3 18v-6a9 9 0 0 1 18 0v6"/><path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3zM3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3z"/></svg>',
}
TYPE_LABEL = {'video':'Video','youtube':'YouTube','series':'Series','podcast':'Podcast','listen':'Listen'}

MEDIA_CSS = """
/* compl uniform: estilo dos cards de complementares (padrão modelo) */
#tab-complementary .media-grid { display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:1rem;margin-bottom:.5rem; }
#tab-complementary .media-card-wrapper { position:relative;display:block;margin:0;padding:0;background:none;border:none; }
#tab-complementary .media-card-wrapper.done { opacity:.6; }
#tab-complementary .media-check { position:absolute;top:.7rem;right:.7rem;z-index:1;display:block;margin:0; }
#tab-complementary .media-check input { width:18px;height:18px;cursor:pointer;accent-color:var(--accent); }
#tab-complementary .media-card { display:block;background:#fff;border:1px solid var(--border);border-radius:10px;overflow:hidden;transition:box-shadow .2s; }
#tab-complementary .media-card:hover { box-shadow:0 4px 16px rgba(0,0,0,.06); }
#tab-complementary .media-thumb { width:auto;min-height:0;height:50px;display:flex;align-items:center;justify-content:center;background:var(--bg-elevated,#f0f2f7); }
#tab-complementary .media-thumb::after { content:none; }
#tab-complementary .media-thumb svg { width:24px;height:24px;stroke:var(--accent);fill:none;stroke-width:2; }
#tab-complementary .media-info { padding:1rem; }
#tab-complementary .media-type { font-size:.65rem;text-transform:uppercase;letter-spacing:1.5px;font-weight:700;color:var(--accent);margin-bottom:.3rem; }
#tab-complementary .media-info h5 { font-size:.9rem;font-weight:600;color:#1a1a1a;margin:0 0 .3rem; }
#tab-complementary .media-info p { font-size:.78rem;color:var(--text-dim);line-height:1.5;margin:0 0 .3rem; }
#tab-complementary .media-info p.media-tip { color:#b45309;font-style:italic;margin-top:.4rem;margin-bottom:0; }
#tab-complementary .media-info a { font-size:.78rem;color:var(--accent);font-weight:600;text-decoration:none;border-bottom:1px solid var(--accent); }
#tab-complementary h4 { grid-column:1 / -1;font-family:'Cormorant Garamond',serif;font-size:1.3rem;color:var(--accent);margin:2rem 0 1rem;padding-bottom:.4rem;border-bottom:2px solid var(--accent); }
"""

def inner_text(s):
    return s

def parse_card(block, mid):
    suffix = mid.rsplit('-',1)[-1].lower()
    typ = TYPE_LABEL.get(suffix, suffix.capitalize())
    # explicit media-type overrides suffix
    mt = re.search(r'media-type[^>]*>(.*?)</div>', block, re.S)
    if mt: typ = re.sub(r'<[^>]+>','',mt.group(1)).strip() or typ
    # title
    h5 = re.search(r'<h5[^>]*>(.*?)</h5>', block, re.S)
    title = h5.group(1).strip() if h5 else ''
    # link (preserve if any)
    link = re.search(r'<a\b[^>]*>.*?</a>', block, re.S)
    link = link.group(0) if link else ''
    # paragraphs
    ps = re.findall(r'<p\b[^>]*>(.*?)</p>', block, re.S)
    ps = [p.strip() for p in ps]
    tip=''; desc=''
    if ps:
        # tip = parágrafo com classe media-tip OU que começa com Dica/Watch-tip OU o último se houver 2+
        tip_idx=None
        for i,full in enumerate(re.findall(r'<p\b[^>]*>.*?</p>', block, re.S)):
            if 'media-tip' in full or re.match(r'(Dica|Tip)\b', re.sub('<[^>]+>','',ps[i])):
                tip_idx=i
        if tip_idx is None and len(ps)>=2: tip_idx=len(ps)-1
        if tip_idx is not None:
            tip=ps[tip_idx]; desc=' '.join(p for j,p in enumerate(ps) if j!=tip_idx)
        else:
            desc=' '.join(ps)
    # svg: reuse existing, else by type
    svg=re.search(r'<svg\b.*?</svg>', block, re.S)
    svg=svg.group(0) if svg else SVG.get(suffix, SVG['video'])
    return typ, title, desc, tip, svg, link

def emit_card(mid, typ, title, desc, tip, svg, link):
    parts=[f'<div class="media-card-wrapper" data-media="{mid}">',
           '  <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>',
           '  <div class="media-card">',
           f'    <div class="media-thumb">{svg}</div>',
           '    <div class="media-info">',
           f'      <div class="media-type">{typ}</div>',
           f'      <h5>{title}</h5>']
    if desc: parts.append(f'      <p>{desc}</p>')
    if tip:  parts.append(f'      <p class="media-tip">{tip}</p>')
    if link: parts.append(f'      <p>{link}</p>')
    parts+=['    </div>','  </div>','</div>']
    return '\n'.join(parts)

def transform(path):
    h=open(path,encoding='utf-8').read()
    ci=h.find('id="tab-complementary"')
    if ci<0: print(path,"-> sem tab-complementary"); return
    ds=h.rfind('<div',0,ci)
    depth=0;end=None
    for m in re.finditer(r'<div\b|</div>', h[ds:]):
        depth+= 1 if m.group(0)=='<div' else -1
        if depth==0: end=ds+m.end();break
    opentag=h[ds:h.find('>',ds)+1]
    inner=h[h.find('>',ds)+1:end-len('</div>')]

    # tokens em ordem: headers (h3/h4) e cards (por data-media)
    tokens=[]
    for m in re.finditer(r'<h[34]\b[^>]*>(.*?)</h[34]>|<div class="media-card-wrapper" data-media="([^"]+)"', inner, re.S):
        if m.group(2):  # card
            mid=m.group(2)
            s=m.start(); d=0; e=None
            for mm in re.finditer(r'<div\b|</div>', inner[s:]):
                d+= 1 if mm.group(0)=='<div' else -1
                if d==0: e=s+mm.end();break
            tokens.append(('card', mid, inner[s:e]))
        else:  # header
            tokens.append(('header', re.sub(r'<[^>]+>','',m.group(1)).strip()))

    # agrupa: header inicia grupo; cards entram no grupo corrente
    groups=[]; cur=None
    for t in tokens:
        if t[0]=='header':
            cur={'title':t[1],'cards':[]}; groups.append(cur)
        else:
            if cur is None: cur={'title':None,'cards':[]}; groups.append(cur)
            cur['cards'].append((t[1],t[2]))

    out=[]
    for g in groups:
        if g['title']:
            tag='h3' if g['title'].lower().startswith('materiais') else 'h4'
            out.append(f'<{tag}>{g["title"]}</{tag}>')
        if g['cards']:
            out.append('<div class="media-grid">')
            for mid,block in g['cards']:
                out.append(emit_card(mid,*parse_card(block,mid)))
            out.append('</div>')
    new_inner='\n'+'\n'.join(out)+'\n    '
    h=h[:h.find('>',ds)+1]+new_inner+h[end-len('</div>'):]

    # injeta CSS (idempotente)
    if '/* compl uniform:' not in h:
        i=h.find('</style>'); h=h[:i]+MEDIA_CSS+h[i:]
    open(path,'w',encoding='utf-8').write(h)
    print(path,f"-> {sum(len(g['cards']) for g in groups)} cards normalizados em {len(groups)} grupos")

if __name__=='__main__':
    for p in sys.argv[1:]: transform(p)
