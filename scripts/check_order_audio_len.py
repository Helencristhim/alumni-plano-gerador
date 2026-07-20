#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE — áudio de ordenação [order-lN] truncado (o defeito que gerava ~1s de nada).

O check_lesson_integrity (GATE 5) pega áudio FALTANDO, mas um MP3 VÁLIDO porém
truncado (a API devolveu ~1s) passa despercebido: o exercício "Put in Order" toca
1 segundo e nada mais. Este gate compara o TAMANHO do áudio com o ESPERADO pelo
TEXTO do exercício (nº de caracteres das frases na ordem) — text-aware, então NÃO
flagra word-scramble (1 frase curta, ~2s é o certo).

Calibração: áudio saudável ~800-1140 B/char; truncado ~100-200 B/char. Corte 400.

USO: python3 scripts/check_order_audio_len.py <arquivo.html> [...]
     exit 1 se algum [order-lN] em arquivo dado estiver truncado.
"""
import re,os,sys,subprocess,html as _html
BYTES_PER_CHAR=400  # abaixo disto = truncado

def clean(t): return _html.unescape(re.sub(r'<[^>]+>','',t)).strip().strip('"').strip()

def audiomap(h):
    out={}
    for k,v in re.findall(r'"((?:[^"\\]|\\.)*)":\s*"(/audio/[^"]+\.mp3)"',h):
        out[k.replace('\\"','"').replace("\\'","'")]=v.split('?')[0]
    return out

def order_sentences(h,n):
    m=re.search(r'id="order-l%d"(.*?)verify'%n,h,re.S)
    if not m: return None
    items=re.findall(r'data-order="(\d+)"[^>]*>.*?<span class="order-text">(.*?)</span>',m.group(1),re.S)
    if not items: return None
    items.sort(key=lambda x:int(x[0]))
    s=[clean(t) for _,t in items if clean(t)]
    return s or None

def size_of(fp):
    if os.path.exists(fp): return os.path.getsize(fp)
    try:
        bh=subprocess.check_output(['git','ls-files','-s',fp],stderr=subprocess.DEVNULL).split()
        return int(subprocess.check_output(['git','cat-file','-s',bh[1]])) if bh else None
    except: return None

def main():
    files=[a for a in sys.argv[1:] if a.endswith('.html') and os.path.exists(a)]
    fails=[]
    for f in files:
        h=open(f,encoding='utf-8').read()
        for k,v in audiomap(h).items():
            mo=re.match(r'\[order-l(\d+)\]$',k)
            if not mo: continue
            n=int(mo.group(1))
            sents=order_sentences(h,n)
            if not sents: continue  # órfão/estrutura diferente: fora do escopo deste gate
            chars=len(' '.join(sents))
            sz=size_of('public'+v)
            if sz is None: continue  # GATE 5 pega arquivo faltando
            if sz < chars*BYTES_PER_CHAR:
                fails.append((f,k,v.split('/')[-1],sz,chars,round(sz/max(chars,1))))
    if fails:
        print("⛔ ÁUDIO DE ORDENAÇÃO TRUNCADO (toca ~1s de nada):")
        for f,k,fn,sz,ch,bpc in fails:
            print(f"   {os.path.basename(f)}  {k} -> {fn}: {sz}b p/ {ch} chars (~{bpc} B/char, mín {BYTES_PER_CHAR}) = truncado")
        print(f"\n{len(fails)} truncado(s). Regenere: python3 scripts/repair_order_audio.py --apply <slug>")
        sys.exit(1)
    print(f"✓ order-audio OK ({len(files)} arquivo(s) verificado(s))")

if __name__=='__main__': main()
