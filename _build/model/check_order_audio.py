#!/usr/bin/env python3
"""Auditor de áudio dos hubs (lê de um git ref). Trata ?v=, escapes, tokens e manifesto.
Severidades:
  CRIT-orphan-token : speakText('[token]') sem entrada no audioMap -> fala lixo / nada
  CRIT-missing-file : audioMap aponta p/ mp3 que NÃO existe no git -> não toca
  CRIT-token-content: [order-lN] cujo áudio (manifesto) NÃO narra os eventos do exercício
  WARN-unwired      : speakText(frase) sem map, MAS existe mp3 c/ nome = snake(frase) -> cai em TTS à toa
  WARN-audio≠tela   : frase literal cujo TEXTO do manifesto diverge da tela (áudio fala outra coisa)
  INFO-tts-only     : speakText(frase) sem map e sem mp3 -> TTS (emergência/survival, talvez by design)
"""
import subprocess,re,sys,html as _html,json
def gshow(ref,p):
    try:return subprocess.check_output(['git','show',f'{ref}:{p}'],stderr=subprocess.DEVNULL).decode('utf-8','replace')
    except subprocess.CalledProcessError:return None
def tree(ref):
    return subprocess.check_output(['git','ls-tree','-r','--name-only',ref]).decode().splitlines()
def snake(s):
    s=_html.unescape(s or '').lower().replace('’',"'")
    return re.sub(r"[^a-z0-9]+","_",s).strip('_')
def norm(s):
    s=_html.unescape(s or '');s=re.sub(r'<[^>]+>','',s).lower().replace('’',"'")
    return re.sub(r"\s+"," ",re.sub(r"[^a-z0-9' ]"," ",s)).strip().rstrip('.')
def audiomap_block(h):
    m=re.search(r'audioMap\s*=\s*\{',h)
    if not m:return ''
    i=m.end()-1;d=0;ins=None;esc=False;st=i
    while i<len(h):
        c=h[i]
        if ins:
            if esc:esc=False
            elif c=='\\':esc=True
            elif c==ins:ins=None
        else:
            if c in '"\'':ins=c
            elif c=='{':d+=1
            elif c=='}':
                d-=1
                if d==0:break
        i+=1
    return h[st:i+1]
def parse_map(block):
    out={}
    for k,v in re.findall(r'"((?:[^"\\]|\\.)*)"\s*:\s*"([^"]+)"',block):
        vc=v.split('?')[0]                      # tira ?v=N
        if vc.endswith('.mp3'):
            out[k.replace("\\'","'").replace('\\"','"')]=vc
    return out
def speaktext_keys(h):
    # 1) forma antiga: o texto DENTRO da string JS -> speakText('...')
    ks=set(re.findall(r"speakText\('((?:[^'\\]|\\.)*)'",h))|set(re.findall(r'speakText\("((?:[^"\\]|\\.)*)"',h))
    # 2) forma nova: o texto vive num ATRIBUTO -> data-speak="..." onclick="speakText(this.dataset.speak,this)"
    #    (é a forma que NÃO quebra com apóstrofo do inglês; ver scripts/check_inline_js.mjs)
    ks|=set(re.findall(r'data-speak="([^"]*)"',h))
    ks={k.replace("\\'","'").replace('\\"','"') for k in ks}
    # 3) DESESCAPA AS ENTIDADES. Era ESTE o bug que deixava 127 frases sem áudio:
    #    o extrator gravava a chave como está no HTML ("Rachel&#39;s task"), mas em runtime
    #    o navegador entrega ao speakText o texto já desescapado ("Rachel's task"). As duas
    #    nunca casavam -> audioMap furado -> a frase caía em TTS robótico (viola REGRA 7).
    #    A chave tem de ser o que o speakText RECEBE, não o que está escrito no arquivo.
    return {_html.unescape(k) for k in ks}
def order_events(h,n):
    cm=re.search(r'id="order-l%d"(.*?)<button class="verify-all-btn"'%n,h,re.S)
    evs=[]
    if cm:
        for o,t in re.findall(r'data-order="(\d+)"[^>]*>.*?<span class="order-text">(.*?)</span>',cm.group(1),re.S):
            evs.append(norm(t))
    return evs
JUNK={'maisa','luiz-bressane-backup-a2','percival-jr-v2','eduarda-gabriel-new','helen-mendes-teste','helen-mendes','vanessa-maluf','zilaudio','elaine-v-b','patricia-ruffo'}
def audit(ref,slug,treelist=None):
    h=gshow(ref,f'public/aluno/{slug}.html')
    if h is None:return None
    TL=treelist if treelist is not None else tree(ref)
    disk={p.split('/')[-1] for p in TL if p.startswith(f'public/audio/{slug}/') and p.endswith('.mp3')}
    mani={}
    for f in [x for x in TL if re.match(rf'_build/{re.escape(slug)}-aula\d+/audio_manifest\.json$',x)]:
        try:
            for e in json.loads(gshow(ref,f) or '[]'):
                if e.get('file'):mani.setdefault(e['file'],e.get('text',''))
        except:pass
    amap=parse_map(audiomap_block(h))
    mkeys=set(amap); norm_mkeys={norm(k) for k in mkeys}
    used=speaktext_keys(h)
    F={'orphan_token':[],'missing_file':[],'token_content':[],'token_unverif':[],'unwired':[],'audio_diff':[],'tts_only':[]}
    # 1) órfãos
    for k in used:
        if k in mkeys or k.rstrip('.') in mkeys or k+'.' in mkeys or norm(k) in norm_mkeys: continue
        if k.startswith('['):
            F['orphan_token'].append(k)
        else:
            sk=snake(k)
            hit=[f for f in disk if f[:-4]==sk]
            if hit: F['unwired'].append((k[:45],hit[0]))
            else:   F['tts_only'].append(k[:40])
    # 2) entradas do map: arquivo existe? conteúdo bate?
    for k,v in amap.items():
        fn=v.split('/')[-1]
        if ('public'+v) not in TL:
            F['missing_file'].append((k[:35],fn)); continue
        mn=re.match(r'\[order-l(\d+)\]$',k)
        if mn:
            n=int(mn.group(1)); evs=order_events(h,n)
            def ratio(text):
                if not evs: return 0.0
                mtn=norm(text)
                def hit(ev):
                    w=[x for x in ev.split() if len(x)>3]
                    return (sum(1 for x in w if x in mtn)/len(w))>=0.5 if w else True
                return sum(1 for e in evs if hit(e))/len(evs)
            mt=mani.get(fn); mr=ratio(mt) if mt else 0.0
            best_f,best_r=None,0.0
            for f2,txt in mani.items():
                r=ratio(txt)
                if r>best_r: best_r,best_f=r,f2
            if evs:
                if mr>=0.8: pass                              # áudio mapeado narra os eventos: OK
                elif best_r>=0.8 and best_f!=fn:
                    F['token_content'].append((k,fn,f'aponta p/ arquivo ERRADO; deveria ser {best_f} ({int(round(best_r*len(evs)))}/{len(evs)} vs mapeado {int(round(mr*len(evs)))}/{len(evs)})'))
                elif mt is None:
                    F['token_unverif'].append((k,fn))
                else:
                    F['token_content'].append((k,fn,f'{int(round(mr*len(evs)))}/{len(evs)} eventos batem'))
            elif mt is None:
                F['token_unverif'].append((k,fn))
            continue
        if k.startswith('['): continue
        mt=mani.get(fn)
        if mt is not None and norm(mt)!=norm(k):
            F['audio_diff'].append((k[:40],fn,mt[:40]))
    return F
def crit_count(F): return len(F['orphan_token'])+len(F['missing_file'])+len(F['token_content'])

if __name__=='__main__':
    if sys.argv[1]=='--selftest':
        # Refs PRÉ-FIX imutáveis (não usar origin/main — os bugs já foram corrigidos lá)
        FAB_PRE='2e436336da87a77f4142d0d3d2a4bb6c30d14ed4'  # antes do #1037 (Fabiana order-l1)
        SIM_PRE='e172eddf17ec9aaa225db640443cab22f81b9268'  # antes do #1038 (simone order-l3)
        print("AUTOTESTE (detector tem que apitar nos bugs conhecidos):")
        f_pre=audit(FAB_PRE,'fabiana-michelly-silva')
        t1=any(k=='[order-l1]' for k in (x[0] for x in f_pre['token_content']))
        print(f"  1. Fabiana@pré-fix flag [order-l1] por conteúdo? {'PASS' if t1 else 'FALHOU'}  -> {[x for x in f_pre['token_content'] if x[0]=='[order-l1]']}")
        s_pre=audit(SIM_PRE,'simone-quiles-de-santana-marques')
        t2='[order-l3]' in s_pre['orphan_token']
        print(f"  2. simone@pré-fix flag [order-l3] órfão?         {'PASS' if t2 else 'FALHOU'}  -> orphan_tokens={s_pre['orphan_token']}")
        f_cur=audit('origin/main','fabiana-michelly-silva')
        t3=crit_count(f_cur)==0
        print(f"  3. Fabiana@main SEM críticos?                    {'PASS' if t3 else 'FALHOU'}  -> crit={crit_count(f_cur)} {f_cur['token_content'][:2]}")
        print("RESULTADO:", "TODOS PASS ✅" if (t1 and t2 and t3) else "⚠️ revisar")
        sys.exit(0)
    ref=sys.argv[1]; slugs=[s for s in sys.argv[2:] if s not in JUNK]
    TL=tree(ref)
    for slug in slugs:
        F=audit(ref,slug,TL)
        if F is None: continue
        c=crit_count(F)
        if c or F['unwired'] or F['audio_diff']:
            print(f"{'⛔' if c else '⚠️ '} {slug}: CRIT={c} (orphanTok={len(F['orphan_token'])} missFile={len(F['missing_file'])} tokenContent={len(F['token_content'])})  unwired={len(F['unwired'])} audioDiff={len(F['audio_diff'])} ttsOnly={len(F['tts_only'])}")
            for x in F['orphan_token'][:5]: print(f"      orphanTok {x}")
            for x in F['missing_file'][:3]: print(f"      missFile {x}")
            for x in F['token_content'][:5]: print(f"      tokenContent {x}")
