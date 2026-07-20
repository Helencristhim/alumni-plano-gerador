#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""repair_order_audio.py — detecta [order-lN] com áudio truncado e regenera o MP3
narrando as frases do exercício na ordem correta (ElevenLabs). Le do disco (working tree).

Detecção: chave "[order-lN]" cujo arquivo mapeado tem < FLOOR bytes (~2.5s).
Reparo: extrai as .order-text ordenadas por data-order do container do exercício,
concatena, e (com --apply) regenera o MP3 SOBRESCREVENDO o arquivo mapeado.

USO:
  dry-run:  python3 scripts/repair_order_audio.py <slug> [<slug> ...]
  aplicar:  set -a && source .env.local && set +a
            python3 scripts/repair_order_audio.py --apply <slug> [...]
"""
import re,os,sys,glob,html as _html,json,urllib.request,time
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FLOOR=40000
BYTES_PER_CHAR=400  # < isso por char = truncado (text-aware)
VOICES=json.load(open(os.path.join(ROOT,'_build/model/voices.json')))

def blobsize_disk(p):
    return os.path.getsize(p) if os.path.exists(p) else None

def audiomap(h):
    out={}
    for k,v in re.findall(r'"((?:[^"\\]|\\.)*)":\s*"(/audio/[^"]+\.mp3)"',h):
        out[k.replace('\\"','"').replace("\\'","'")]=v.split('?')[0]
    return out

def order_sentences(h,n):
    """frases do exercício id=order-lN (ou order-l{n}) ordenadas por data-order."""
    m=re.search(r'id="order-l%d"(.*?)(?:<button[^>]*verify-all|</div>\s*</div>\s*</div>)'%n,h,re.S)
    if not m:
        m=re.search(r'id="order-l%d"(.*?)verify'%n,h,re.S)
    if not m: return None
    seg=m.group(1)
    items=re.findall(r'data-order="(\d+)"[^>]*>.*?<span class="order-text">(.*?)</span>',seg,re.S)
    if not items: return None
    items.sort(key=lambda x:int(x[0]))
    sents=[_html.unescape(re.sub(r'<[^>]+>','',t)).strip().strip('"').strip() for _,t in items]
    return [s for s in sents if s]

def find_targets(slug):
    """retorna lista de (htmlpath, key, filepath, size, sentences)."""
    res=[]
    for f in sorted(glob.glob(f'public/professor/{slug}*.html')+glob.glob(f'public/aluno/{slug}*.html')):
        h=open(f,encoding='utf-8').read()
        am=audiomap(h)
        for k,v in am.items():
            mo=re.match(r'\[order-l(\d+)\]$',k)
            if not mo: continue
            n=int(mo.group(1))
            fp='public'+v
            sz=blobsize_disk(fp)
            if sz is None:  # sparse: pega do git
                try:
                    import subprocess
                    bh=subprocess.check_output(['git','ls-files','-s',fp]).split()
                    sz=int(subprocess.check_output(['git','cat-file','-s',bh[1]])) if bh else None
                except: sz=None
            if sz is not None:
                sents=order_sentences(h,n)
                if sents:
                    chars=len(' '.join(sents))
                    if sz < chars*BYTES_PER_CHAR:   # text-aware: curto p/ o texto = truncado
                        res.append((f,k,fp,sz,sents))
    return res

def gen(text,voice,fp,key):
    body=json.dumps({'text':text,'model_id':'eleven_multilingual_v2',
        'voice_settings':{'stability':0.5,'similarity_boost':0.75,'style':0.0,'use_speaker_boost':True}}).encode()
    req=urllib.request.Request('https://api.elevenlabs.io/v1/text-to-speech/'+VOICES[voice],
        data=body,headers={'xi-api-key':os.environ['ELEVENLABS_API_KEY'],'Content-Type':'application/json','Accept':'audio/mpeg'})
    with urllib.request.urlopen(req,timeout=120) as r: data=r.read()
    if len(data)<FLOOR:
        raise RuntimeError(f'regen ainda curto ({len(data)}b) para {key}')
    os.makedirs(os.path.dirname(fp),exist_ok=True)
    open(fp,'wb').write(data)
    return len(data)

def main():
    apply='--apply' in sys.argv
    slugs=[a for a in sys.argv[1:] if not a.startswith('--')]
    grand=0
    for slug in slugs:
        tg=find_targets(slug)
        # dedup por filepath (mesmo arquivo pode ser referenciado no prof e no aluno)
        seen={}
        for f,k,fp,sz,sents in tg:
            seen.setdefault(fp,(k,sz,sents,f))
        print(f"\n===== {slug}: {len(seen)} order-audio truncado(s) =====")
        for fp,(k,sz,sents,f) in sorted(seen.items()):
            print(f"  {os.path.basename(fp)}  ({sz}b ~{round(sz/16000,1)}s)  key={k}  src={os.path.basename(f)}")
            if not sents:
                print(f"     !! NÃO consegui extrair frases do exercício — PULAR (revisar manual)")
                continue
            txt=' '.join(sents)
            print(f"     frases({len(sents)}): {txt[:120]}{'...' if len(txt)>120 else ''}")
            if apply:
                try:
                    nb=gen(txt,'arthur',fp,k); print(f"     -> REGENERADO {nb}b ~{round(nb/16000,1)}s"); grand+=1; time.sleep(0.3)
                except Exception as e:
                    print(f"     -> ERRO: {str(e)[:140]}")
    print(f"\nTOTAL {'regenerado' if apply else '(dry-run) a regenerar'}: {grand if apply else 'ver acima'}")

if __name__=='__main__': main()
