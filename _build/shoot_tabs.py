#!/usr/bin/env python3
"""Varredura de LAYOUT das 3 abas do aluno (Pre-class, Complementares, Controle de
Aulas) — roladas até o fim. Para revisao visual por subagente.
Uso: shoot_tabs.py <slug> <out_dir>  (servidor em http://localhost:8731)"""
import sys, os, re
from playwright.sync_api import sync_playwright

slug, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
BASE='http://localhost:8731'
shots=[]

def wait_imgs(p):
    try:
        p.evaluate("""async()=>{const h=document.body.scrollHeight;
          for(let y=0;y<h;y+=700){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,25));}
          window.scrollTo(0,0);
          await Promise.all([...document.images].filter(i=>!i.complete).map(i=>new Promise(r=>{i.onload=i.onerror=r;setTimeout(r,2500);})));}""")
        p.wait_for_timeout(700)
    except Exception: pass

def slice_full(p, prefix, maxslices=12):
    H=p.evaluate('Math.max(document.body.scrollHeight,document.documentElement.scrollHeight)')
    vh=p.viewport_size['height']; y=0; i=0
    while y < H and i < maxslices:
        p.evaluate(f'window.scrollTo(0,{y})'); p.wait_for_timeout(250)
        f=f'{out}/{prefix}-{i:02d}.png'; p.screenshot(path=f); shots.append(f); i+=1; y+=vh-70

with sync_playwright() as pw:
    b=pw.chromium.launch()
    url=f'{BASE}/aluno/{slug}.html'
    p=b.new_page(viewport={'width':1100,'height':1300})
    r=p.goto(url, wait_until='networkidle', timeout=25000)
    if not r or r.status>=400:
        print(f"ERRO: {url} -> {r.status if r else 'sem resposta'}"); sys.exit(1)
    # as 3 abas que importam (Controle de Aulas é injetada por controle-aulas.js)
    p.wait_for_timeout(800)  # da tempo do controle-aulas.js injetar a aba
    want=[('pre-class','exercises'),('complementares','complementary'),('controle','controle')]
    tabs=p.eval_on_selector_all('button.tab-btn','e=>e.map(x=>x.textContent.trim())')
    for label,key in want:
        # acha o botão da aba por texto aproximado
        btn=None
        for t in tabs:
            tl=t.lower()
            if (label=='pre-class' and 'pre-class' in tl) or \
               (label=='complementares' and 'complement' in tl) or \
               (label=='controle' and 'controle' in tl):
                btn=t; break
        if not btn:
            print(f"[aviso] aba '{label}' não encontrada (tabs={tabs})"); continue
        try:
            p.click(f'button.tab-btn:has-text("{btn}")', timeout=4000); p.wait_for_timeout(500)
            wait_imgs(p)
            slice_full(p, f'{label}', maxslices=12)
        except Exception as e:
            print(f"[erro] aba {label}: {e}")
    p.close(); b.close()
print('\n'.join(shots))
print(f"TOTAL_SHOTS={len(shots)} | tabs_vistas={[s.split('/')[-1].rsplit('-',1)[0] for s in shots]}")
