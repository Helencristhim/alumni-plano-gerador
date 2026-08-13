#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE — audio FORA DE SINCRONIA com o texto que ele deveria falar.

O DEFEITO QUE ESTE GATE EXISTE PARA MATAR
-----------------------------------------
O nome do MP3 de exercicio e POSICIONAL, nao derivado do texto:
`a7_order_sequence.mp3` continua se chamando assim depois de a historia inteira
ser reescrita. E o gen_audio PULA arquivo existente. Entao:

    1. escreve-se o rascunho A  ->  gera a7_order_sequence.mp3 (fala o rascunho A)
    2. reescreve-se o exercicio ->  agora a tela mostra o rascunho B
    3. roda-se o gen_audio de novo -> "ja existe", PULA
    4. commita-se: HTML=B, manifesto=B, MP3=A

Nenhum gate anterior via isso, e nao por descuido: o MP3 e valido, tem o tamanho
certo para o texto (GATE 5b passa), o arquivo existe (GATE 5 passa) e o manifesto
— que e o DESEJADO, nao o PRODUZIDO — bate com a tela (check_order_audio passa).
So OUVINDO da para perceber. Foi assim que a Fabiana ficou com as aulas 6 a 10
narrando uma historia com outros personagens no "Put the story in order".

A TRAVA
-------
O gen_audio passa a gravar `public/audio/{slug}/_src.json`: para cada MP3, o
sha1 de "voz|texto" que o PRODUZIU. Isso e a PROCEDENCIA — o unico dado que
distingue "o audio certo" de "um audio plausivel". Este gate cobra:

  R1  MP3 que o PR traz (novo ou modificado) TEM de ter procedencia no _src.json.
      Sem isso, o audio volta a ser um arquivo anonimo e o defeito renasce.
  R2  manifesto que o PR traz: para todo item cujo MP3 JA tem procedencia, o
      sha1 gravado tem de bater com o texto atual. Divergiu = o texto foi
      reescrito depois do audio (o passo 2/3 acima) -> BLOQUEIA.

LEGADO (REGRA 30): arquivo sem entrada no _src.json e anterior a esta trava —
nao ha como saber de que texto nasceu, e o gate NAO exige nada dele. Ele so
cobra o que o PR toca. Divida legada nao vira tarefa.

USO: python3 scripts/check_audio_src.py <arquivos do PR...>
     exit 1 se algum audio do PR estiver sem procedencia ou fora de sincronia.
"""
import hashlib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def src_hash(text, voice):
    return hashlib.sha1((voice + '|' + text).encode('utf-8')).hexdigest()


def load_ledger(slug):
    p = os.path.join(ROOT, 'public', 'audio', slug, '_src.json')
    try:
        with open(p, encoding='utf-8') as f:
            return json.load(f)
    except (IOError, ValueError):
        return {}


def main(argv):
    files = [f for f in argv if f.strip()]
    mp3s = {}       # slug -> [nome do arquivo]
    manifests = []  # (slug, caminho do manifesto)
    for f in files:
        m = re.match(r'public/audio/([^/]+)/(.+\.mp3)$', f)
        if m:
            mp3s.setdefault(m.group(1), []).append(m.group(2))
            continue
        m = re.match(r'(_build/([^/]+)-aula\d+)/audio_manifest\.json$', f)
        if m:
            manifests.append((re.sub(r'-aula\d+$', '', os.path.basename(m.group(1))), f))

    fails = []

    # R1 — audio novo/modificado sem procedencia
    for slug, names in sorted(mp3s.items()):
        led = load_ledger(slug)
        for n in sorted(names):
            if n not in led:
                fails.append('SEM PROCEDENCIA  public/audio/%s/%s — nao consta em '
                             'public/audio/%s/_src.json. Gere pelo _build/model/gen_audio.py '
                             '(ele grava o ledger) em vez de escrever o MP3 na mao.'
                             % (slug, n, slug))

    # R2 — texto reescrito depois do audio
    for slug, mpath in sorted(set(manifests)):
        led = load_ledger(slug)
        if not led:
            continue
        try:
            with open(os.path.join(ROOT, mpath), encoding='utf-8') as f:
                entries = json.load(f)
        except (IOError, ValueError) as e:
            print('  ! manifesto ilegivel %s: %s' % (mpath, e))
            continue
        for e in entries:
            fn, txt, voice = e.get('file'), e.get('text', ''), e.get('voice', '')
            if not fn or fn not in led:
                continue          # legado sem procedencia: nao se cobra (REGRA 30)
            if led[fn] != src_hash(txt, voice):
                fails.append('FORA DE SINCRONIA public/audio/%s/%s — o MP3 foi gerado de '
                             'OUTRO texto (ou outra voz). O exercicio foi reescrito depois '
                             'do audio. Re-rode: python3 _build/model/gen_audio.py %s'
                             % (slug, fn, os.path.join(os.path.dirname(mpath), 'config.json')))

    if fails:
        print('GATE audio-src: %d problema(s)' % len(fails))
        for f in fails:
            print('  X ' + f)
        return 1
    print('GATE audio-src: ok (%d mp3, %d manifesto)' % (sum(len(v) for v in mp3s.values()),
                                                         len(set(manifests))))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
