#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""AUDITOR — o audio do listening responde as perguntas do slide?

O DEFEITO
---------
No slide de listening convivem duas coisas escritas em momentos diferentes: o
MP3 (gerado de um texto) e as perguntas de compreensao (escritas a mao no
fragmento do slide). Se o texto do listening for reescrito depois, o MP3 pode
ficar falando o rascunho antigo -- ou, pior, as perguntas ficam cobrando um
texto que o audio nunca disse. A tela fica impecavel: player, tres perguntas,
tres respostas. So OUVINDO da para perceber.

Reportado pelo professor em 28/08 na aula 8 do nilo-mesquita-patucci, slides 15
e 18: "os audios nao tem relacao com as perguntas e respostas". Confirmado
transcrevendo: a pergunta 3 do slide 18 cobra "que resolucao foi aprovada" e a
resposta diz "auditoria anual dos gastos"; o audio diz "a resolution was passed
to create a whistleblower hotline".

COMO ELE MEDE
-------------
Transcreve o MP3 (ElevenLabs scribe) e, para cada resposta do slide, procura a
FRASE do audio que melhor a sustenta -- cobertura de palavras de conteudo,
janela de uma ou duas frases. Resposta paralelamente sustentada pontua alto;
resposta que fala de outro assunto pontua baixo.

POR QUE ISTO E UM AUDITOR E NAO UM GATE BLOQUEANTE
--------------------------------------------------
Medido em 7.781 respostas de 1.694 aulas com texto declarado no config: no
limiar que pega o Nilo, ~1,5% dos slides do repo caem -- e a amostra que abri
mostrou FALSO POSITIVO legitimo. Pergunta de INFERENCIA nao tem sustentacao
lexical nenhuma e ainda assim e a melhor pergunta da aula:

    audio: "Revenue was one million four hundred and eighty thousand.
            Margin, twenty-two percent. Overhead..."
    Q: "How many figures does he say, and how many comparisons?"
    A: "Five figures and no comparison at all."       <- cobertura 0.00

Bloquear PR por isso reprovaria material bom. Entao este script RANQUEIA
suspeitos e imprime audio e perguntas lado a lado para um humano julgar. A
medida acha o candidato; quem da o veredito le.

USO
    python3 audita_listening.py public/professor/*.html      # audita
    python3 audita_listening.py --cache X.json <arquivos>     # reaproveita STT
"""
import json, os, re, subprocess, sys, hashlib, statistics

STOP=set("a an the of to in on at for and or but is are was were be been being do does did have has had it its this that these those with as by from not no so if then than there their they them he she his her you your i my we our us what which who whose when where how why can could will would should must may might one two three about into over under before after all any some each every".split())
KEY=os.path.expanduser('~/.config/alumni/elevenlabs.key')

def palavras(t):
    t=re.sub(r'<[^>]+>',' ',t); t=re.sub(r'&[a-z]+;|&#\d+;',' ',t)
    return [w for w in re.findall(r"[a-z']+",t.lower()) if w not in STOP and len(w)>2]

def cobertura(resp,trecho):
    tw=set(palavras(trecho)); rw=palavras(resp)
    return sum(1 for w in rw if w in tw)/len(rw) if rw else 1.0

def melhor_frase(resp,texto):
    fr=[f for f in re.split(r'(?<=[.!?])\s+',texto) if f.strip()]
    cand=fr+[fr[i]+' '+fr[i+1] for i in range(len(fr)-1)]
    return max((cobertura(resp,c) for c in cand), default=0.0)

def bytes_do_mp3(caminho_rel, raiz):
    """O disco MENTE: worktree com sparse-checkout nao materializa public/audio.
    A verdade e o git."""
    abs_=os.path.join(raiz,caminho_rel)
    if os.path.exists(abs_): return open(abs_,'rb').read()
    r=subprocess.run(['git','show','origin/main:'+caminho_rel],cwd=raiz,capture_output=True)
    return r.stdout if r.returncode==0 and r.stdout else None

def transcreve(dados, cache, tmp):
    h=hashlib.sha1(dados).hexdigest()
    if h in cache: return cache[h]
    open(tmp,'wb').write(dados)
    r=subprocess.run(['curl','-s','-X','POST','https://api.elevenlabs.io/v1/speech-to-text',
                      '-H','xi-api-key: '+open(KEY).read().strip(),
                      '-F','file=@'+tmp,'-F','model_id=scribe_v1'],capture_output=True,text=True)
    try: txt=json.loads(r.stdout).get('text','')
    except Exception: txt=''
    cache[h]=txt
    return txt

def slides_de(html):
    return re.split(r'(?=<div class="slide[^"]*"[^>]*data-slide=")',html)

def audita(arquivos, raiz, cache):
    saida=[]
    # Duas familias de markup convivem no repo, e o auditor tem de ler as DUAS
    # (so a primeira deixava metade das aulas do Nilo invisiveis para a medicao):
    #   .comp-q     -> <div class="q-text">Q</div><div class="q-answer">A</div>
    #   .comp-question -> <p>Q</p><p class="fill-answer|comp-answer">A</p>
    RES_QA=[r'class="q-text"[^>]*>(.*?)</div><div class="q-answer"[^>]*>(.*?)</div>',
            r'<p[^>]*>((?:(?!</p>).)*?\d\..*?)</p>\s*<p class="(?:fill-answer|comp-answer)"[^>]*>(.*?)</p>']
    def _qa(bloco):
        for r in RES_QA:
            m=re.findall(r,bloco,re.S)
            if len(m)>=2: return m
        return []
    for f in arquivos:
        html=open(f,encoding='utf-8').read()
        parts=slides_de(html)
        for idx,p in enumerate(parts):
            m=re.search(r'data-src="([^"]+\.mp3)"',p)
            if not m: continue
            qas=_qa(p)
            # material antigo poe as perguntas no slide SEGUINTE (o de checagem),
            # sem player. Sem isto o auditor fica cego em metade do repo.
            if len(qas)<2 and idx+1<len(parts):
                prox=parts[idx+1]
                if 'data-src=' not in prox: qas=_qa(prox)
            if len(qas)<2: continue
            rel='public'+m.group(1)
            dados=bytes_do_mp3(rel,raiz)
            if not dados:
                saida.append((0.0,f,re.search(r'data-slide="(\d+)"',p).group(1),'MP3 AUSENTE '+m.group(1),[]))
                continue
            texto=transcreve(dados,cache,os.path.join(raiz,'.stt_tmp.mp3'))
            itens=[]
            for q,a in qas:
                q=re.sub(r'<[^>]+>','',q).strip(); a=re.sub(r'<[^>]+>','',a).strip()
                itens.append((round(melhor_frase(a,texto),2),q,a))
            sl=re.search(r'data-slide="(\d+)"',p).group(1)
            saida.append((statistics.median([i[0] for i in itens]), f, sl, texto, itens))
    return sorted(saida)

def main(argv):
    cachefile=None
    if '--cache' in argv:
        i=argv.index('--cache'); cachefile=argv[i+1]; del argv[i:i+2]
    arquivos=[a for a in argv if a.endswith('.html') and os.path.exists(a)]
    raiz=subprocess.run(['git','rev-parse','--show-toplevel'],capture_output=True,text=True).stdout.strip()
    cache={}
    if cachefile and os.path.exists(cachefile): cache=json.load(open(cachefile))
    res=audita(arquivos,raiz,cache)
    if cachefile: json.dump(cache,open(cachefile,'w'))
    for med,f,sl,texto,itens in res:
        marca='SUSPEITO' if med<0.45 else ('atencao' if med<0.60 else 'ok')
        print('%-9s mediana=%.2f  %s  slide %s'%(marca,med,os.path.basename(f),sl))
        if med<0.60:
            print('   AUDIO: '+texto[:400].replace('\n',' '))
            for s,q,a in itens: print('     [%.2f] Q: %s\n            A: %s'%(s,q[:100],a[:100]))
    print('\n%d slides de listening auditados; %d suspeitos (<0.45), %d em atencao (<0.60)'
          %(len(res),sum(1 for r in res if r[0]<0.45),sum(1 for r in res if 0.45<=r[0]<0.60)))
    return 0

if __name__=='__main__': sys.exit(main(sys.argv[1:]))
