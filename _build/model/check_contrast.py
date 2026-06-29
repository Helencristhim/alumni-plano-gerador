#!/usr/bin/env python3
"""Scanner determinístico de contraste: razão WCAG de texto sobre fundo colorido
inline (linear-gradient/solid), com casamento correto da <div> do container
(exclui sub-containers com fundo próprio). Estático, sem browser."""
import re,sys,os
def hexs(c):
    c=c.strip().lstrip('#')
    if len(c)==3: c=''.join(ch*2 for ch in c)
    if len(c)!=6: return None
    try: return tuple(int(c[i:i+2],16) for i in (0,2,4))
    except: return None
def lum(rgb):
    def f(v):
        v/=255
        return v/12.92 if v<=0.03928 else ((v+0.055)/1.055)**2.4
    r,g,b=rgb; return 0.2126*f(r)+0.7152*f(g)+0.0722*f(b)
def ratio(a,b):
    la,lb=lum(a),lum(b); hi,lo=max(la,lb),min(la,lb); return (hi+0.05)/(lo+0.05)
def varmap(h):
    return {k:v for k,v in re.findall(r'(--[\w-]+)\s*:\s*(#[0-9a-fA-F]{3,6})',h)}
def resolve(val,vm):
    val=val.strip()
    mv=re.match(r'var\((--[\w-]+)\)',val)
    if mv: val=vm.get(mv.group(1),'')
    val=val.strip()
    if val.startswith('#'): return hexs(val)
    mr=re.match(r'rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)',val)
    if mr: return tuple(int(mr.group(i)) for i in (1,2,3))
    return None
def classcolors(h,vm):
    cm={}
    for sel,body in re.findall(r'\.([\w-]+)\s*\{([^}]*)\}',h):
        m=re.search(r'(?<!-)color\s*:\s*([^;]+)',body)
        if m:
            rgb=resolve(m.group(1),vm)
            if rgb: cm.setdefault(sel,rgb)
    return cm
def inner_div(h,open_start):
    i=h.find('>',open_start)+1; depth=1; j=i
    while j<len(h) and depth>0:
        nd=h.find('<div',j); cd=h.find('</div>',j)
        if cd==-1: return h[i:]
        if nd!=-1 and nd<cd: depth+=1; j=nd+4
        else: depth-=1; j=cd+6
    return h[i:cd]
def bgclasses(h):
    s=set()
    for sel,body in re.findall(r'([^{}]+)\{([^}]*)\}',h):
        if re.search(r'background(-color)?\s*:\s*(?!none|transparent|inherit)\S',body):
            for tok in re.findall(r'\.([\w-]+)',sel): s.add(tok)
    return s
def strip_bg(seg,bgc):
    # remove iterativamente sub-divs FOLHA (sem <div interno) que têm fundo próprio
    # (inline OU classe com background) — deixa só texto direto sobre ESTE container
    pat=re.compile(r'<div\b((?:[^>"]|"[^"]*")*?)>((?:(?!<div\b).)*?)</div>',re.S)
    changed=True
    while changed:
        changed=False
        out=[]; last=0
        for m in pat.finditer(seg):
            attrs=m.group(1)
            has=bool(re.search(r'style="[^"]*background:',attrs)) or any(tok in bgc for cattr in re.findall(r'class="([^"]*)"',attrs) for tok in cattr.split())
            if has:
                out.append(seg[last:m.start()]); last=m.end(); changed=True
        out.append(seg[last:])
        seg=''.join(out)
    return seg
def darkctx_overrides(h,vm):
    # em slides escuros (.slide-dark / .slide-image) o texto recebe cor clara via cascade
    ov={}
    for sel,body in re.findall(r'([^{}]+)\{([^}]*)\}',h):
        if '.slide-dark' not in sel and '.slide-image' not in sel: continue
        m=re.search(r'(?<!-)color\s*:\s*([^;!]+)',body)
        if not m: continue
        rgb=resolve(m.group(1),vm)
        if not rgb: continue
        for cls in re.findall(r'\.(?:slide-dark|slide-image)\s+\.([\w-]+)',sel): ov.setdefault(cls,rgb)
    return ov
def hiddenclasses(h):
    s=set()
    for sel,body in re.findall(r'([^{}]+)\{([^}]*)\}',h):
        if re.search(r'(?:opacity\s*:\s*0(?!\.)|display\s*:\s*none|visibility\s*:\s*hidden)',body):
            for tok in re.findall(r'\.([\w-]+)',sel): s.add(tok)
    return s
def scan(path):
    h=open(path,encoding='utf-8').read()
    vm=varmap(h); cm=classcolors(h,vm); bgc=bgclasses(h); ov=darkctx_overrides(h,vm)
    hid=hiddenclasses(h); findings=[]
    for m in re.finditer(r'<div[^>]*style="([^"]*)"',h):
        style=m.group(1)
        bgm=re.search(r'background(?:-color|-image)?\s*:\s*([^;]+)',style)
        if not bgm: continue
        bgval=bgm.group(1)
        # só fundos coloridos: hex no VALOR do background (não no color/border)
        stops=[s for s in (hexs(x) for x in re.findall(r'#[0-9a-fA-F]{3,6}',bgval)) if s]
        if not stops: continue
        # ignora fundos essencialmente brancos/claros (rgba branco, #fff): texto escuro ali é OK
        if all(lum(s)>0.7 for s in stops): continue
        is_dark=max(lum(s) for s in stops)<0.18   # fundo escuro => contexto slide-dark/slide-image
        seg=inner_div(h,m.start())
        seg2=strip_bg(seg,bgc)
        # se o fundo tem um stop branco/claro, o texto real provavelmente fica sobre
        # a parte clara só na borda — não medir contra o stop escuro como se fosse sólido.
        for cls in set(re.findall(r'class="([\w-]+)"',seg2)):
            if cls in bgc or cls in hid: continue   # fundo próprio, ou texto escondido (opacity:0/none)
            if cls in cm and re.search(r'class="[^"]*\b'+re.escape(cls)+r'\b[^"]*"[^>]*>[^<]*[A-Za-z]{3}',seg2):
                txt=ov.get(cls,cm[cls]) if is_dark else cm[cls]
                mn=min(ratio(txt,st) for st in stops)
                if mn<3.0: findings.append((cls,'#%02x%02x%02x'%txt,'/'.join('#%02x%02x%02x'%s for s in stops),round(mn,2)))
        for tag in re.findall(r'<[^>]*style="([^"]*color:\s*#[0-9a-fA-F]{3,6}[^"]*)"[^>]*>[^<]*[A-Za-z]{3}',seg2):
            if 'background' in tag: continue   # elemento com fundo próprio
            cmi=re.search(r'color:\s*(#[0-9a-fA-F]{3,6})',tag).group(1); txt=hexs(cmi)
            if txt:
                mn=min(ratio(txt,st) for st in stops)
                if mn<3.0: findings.append(('inline',cmi,'/'.join('#%02x%02x%02x'%s for s in stops),round(mn,2)))
    return sorted(set(findings),key=lambda x:x[3])
if __name__=='__main__':
    perstu={}; tot=0
    for f in sys.argv[1:]:
        fs=scan(f)
        if fs:
            stu=re.sub(r'-aula\d+','',os.path.basename(f)[:-5])
            perstu.setdefault(stu,{})[f]=fs; tot+=len(fs)
    for stu in sorted(perstu):
        print(f"\n### {stu}")
        for f,fs in perstu[stu].items():
            for cls,tc,bg,r in fs[:6]:
                print(f"  {os.path.basename(f):42} {r:>4}  txt {tc} sobre {bg}  [{cls}]")
    print(f"\n=== TOTAL achados <3.0: {tot} em {len(perstu)} alunos ===")
