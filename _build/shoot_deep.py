#!/usr/bin/env python3
"""Varredura VISUAL PROFUNDA de um hub: abas roladas até o fim + accordions do
Pre-class abertos + amostra de slides do IN CLASS. Para revisao por subagente.
Uso: shoot_deep.py <slug> <out_dir>  (servidor em http://localhost:8731)"""
import sys, os
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
        p.wait_for_timeout(800)
    except Exception: pass

def slice_capture(p, prefix, maxslices=8):
    # captura a aba ativa em fatias de viewport ate o fim (cap em maxslices)
    H=p.evaluate('Math.max(document.body.scrollHeight, document.documentElement.scrollHeight)')
    vh=p.viewport_size['height']; y=0; i=0
    while y < H and i < maxslices:
        p.evaluate(f'window.scrollTo(0,{y})'); p.wait_for_timeout(250)
        f=f'{out}/{prefix}-{i:02d}.png'; p.screenshot(path=f); shots.append(f); i+=1; y+=vh-80

def tabs_for(p):
    return [b.strip() for b in p.eval_on_selector_all('button.tab-btn','e=>e.map(x=>x.textContent)')]

with sync_playwright() as pw:
    b=pw.chromium.launch()
    for role in ['aluno','professor']:
        url=f'{BASE}/{role}/{slug}.html'
        p=b.new_page(viewport={'width':1100,'height':1300})
        try:
            r=p.goto(url, wait_until='networkidle', timeout=25000)
            if not r or r.status>=400: p.close(); continue
        except Exception as e:
            print(f"SKIP {role}: {e}"); p.close(); continue
        # foco por papel p/ evitar redundância e cortar custo:
        #  aluno = Pre-class (deep) + Complementares (leve)
        #  professor = IN CLASS (slides) + Planejamento
        ALLOW = {'aluno': ['pre-class','complement'], 'professor': ['in-class','inclass','planejamento']}[role]
        for t in tabs_for(p):
            safe=t.lower().replace(' ','-').replace('/','')
            if not any(a in safe for a in ALLOW): continue
            try: p.click(f'button.tab-btn:has-text("{t}")', timeout=4000); p.wait_for_timeout(400)
            except Exception: continue
            wait_imgs(p)
            if 'pre-class' in safe or 'exerc' in safe:
                # 1) lista colapsada inteira
                slice_capture(p, f'{role}-preclass-list', maxslices=10)
                # 2) abre amostra de accordions (1, meio, ultimo) e captura o corpo
                ids=p.eval_on_selector_all('.lesson-card','els=>els.map(e=>e.id)')
                pick=[]
                if ids:
                    pick=[ids[0], ids[len(ids)//2], ids[-1]]
                for lid in dict.fromkeys(pick):
                    try:
                        p.eval_on_selector(f'#{lid} .lesson-header','el=>{el.parentElement.classList.add("open"); el.scrollIntoView();}')
                        p.wait_for_timeout(500); wait_imgs(p)
                        # captura a partir do topo do card, 3 fatias
                        top=p.eval_on_selector(f'#{lid}','el=>el.getBoundingClientRect().top+window.scrollY')
                        for k in range(3):
                            p.evaluate(f'window.scrollTo(0,{top+ k*1100})'); p.wait_for_timeout(250)
                            f=f'{out}/{role}-preclass-open-{lid}-{k}.png'; p.screenshot(path=f); shots.append(f)
                        p.eval_on_selector(f'#{lid} .lesson-header','el=>el.parentElement.classList.remove("open")')
                    except Exception: pass
            elif 'in-class' in safe or 'inclass' in safe:
                # menu
                f=f'{out}/{role}-inclass-menu.png'; p.screenshot(path=f); shots.append(f)
                # entra na 1a aula e percorre ~7 slides
                try:
                    # entra no modo-slide de forma robusta: clica o 1o card do menu
                    # (startLesson/enterSlideMode/goToSlide) ou chama a função existente
                    entered=p.evaluate('''()=>{
                        var el=document.querySelector('[onclick*="startLesson"],[onclick*="enterSlideMode"],[onclick*="goToSlide"]');
                        if(el){el.click();return true;}
                        if(typeof enterSlideMode==='function'){enterSlideMode(1);return true;}
                        if(typeof startLesson==='function'){startLesson(1,30);return true;}
                        return false; }''')
                    if entered:
                        p.wait_for_timeout(600)
                        for k in range(7):
                            f=f'{out}/{role}-inclass-slide-{k:02d}.png'; p.screenshot(path=f); shots.append(f)
                            moved=p.evaluate('''()=>{ if(typeof changeSlide==='function'){changeSlide(1);return true;}
                                document.dispatchEvent(new KeyboardEvent('keydown',{key:'ArrowRight'})); return true; }''')
                            p.wait_for_timeout(400); wait_imgs(p)
                        p.evaluate('''()=>{document.body.classList.remove('slide-mode'); if(typeof switchTab==='function')try{switchTab('inclass')}catch(e){} }''')
                except Exception: pass
            elif 'complement' in safe:
                slice_capture(p, f'{role}-complementares', maxslices=2)
            else:
                slice_capture(p, f'{role}-{safe}', maxslices=3)
        p.close()
    b.close()
print('\n'.join(shots))
print(f"\nTOTAL_SHOTS={len(shots)}")
