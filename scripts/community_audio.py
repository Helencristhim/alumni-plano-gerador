#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""community_audio.py — gera/audita os MP3 dos materiais Community (fora do gerador).

Os materiais em public/community/<aluna>/ nao passam pelo builder: cada HTML carrega o
seu proprio `window.AUDIO_MAP` e os MP3 ficam em `audio/` ao lado. Este script le o
AUDIO_MAP de cada HTML e:

  --check   (default) lista o que o HTML pede e o disco nao tem, e o que o disco tem
            e nenhum HTML pede mais (orfaos — NAO deleta: outro material pode usar)
  --gen     gera SO os que faltam, com a voz declarada (Ellen, a mesma dos MP3 ja
            publicados — registrado nos commits do lote) e escreve o ledger _src.json

Ledger. `_src.json` guarda sha1(voz|texto) de cada arquivo gerado. O nome do MP3 vem do
TEXTO, entao reescrever a frase gera nome novo e nao ha risco de fossilizar o audio do
rascunho anterior — mas o ledger deixa a procedencia auditavel do mesmo jeito.

  python3 scripts/community_audio.py public/community/fernanda
  python3 scripts/community_audio.py public/community/fernanda --gen
"""
import glob
import hashlib
import json
import os
import re
import sys
import time
import urllib.request

VOZ = 'ellen'
VOICE_ID = {'arthur': 'sfJopaWaOtauCD3HKX6Q', 'ellen': 'BIvP0GN1cAtSRTxNHnWS'}
MIN_BYTES_PER_CHAR = 400
MAX_TRIES = 3


def key():
    k = os.environ.get('ELEVENLABS_API_KEY')
    if not k:
        p = os.path.expanduser('~/.config/alumni/elevenlabs.key')
        if os.path.exists(p):
            k = open(p, encoding='utf-8').read().strip()
    assert k, 'ELEVENLABS_API_KEY nao setada e ~/.config/alumni/elevenlabs.key nao existe'
    return k


def tts(text, voice, k):
    body = json.dumps({'text': text, 'model_id': 'eleven_multilingual_v2',
                       'voice_settings': {'stability': 0.5, 'similarity_boost': 0.75,
                                          'style': 0.0, 'use_speaker_boost': True}}).encode('utf-8')
    req = urllib.request.Request(
        'https://api.elevenlabs.io/v1/text-to-speech/' + VOICE_ID[voice], data=body,
        headers={'xi-api-key': k, 'Content-Type': 'application/json', 'Accept': 'audio/mpeg'})
    with urllib.request.urlopen(req, timeout=90) as r:
        return r.read()


def audio_maps(root):
    """{arquivo_html: {texto: nome_mp3}} para cada HTML do diretorio."""
    out = {}
    for f in sorted(glob.glob(os.path.join(root, '*.html'))):
        h = open(f, encoding='utf-8').read()
        m = re.search(r'window\.AUDIO_MAP=(\{.*?\});', h, re.S)
        if m:
            out[os.path.basename(f)] = json.loads(m.group(1))
    return out


def main(argv):
    root = argv[1].rstrip('/')
    gen = '--gen' in argv
    aud = os.path.join(root, 'audio')
    maps = audio_maps(root)

    pedidos = {}          # nome_mp3 -> (texto, [htmls])
    for html, amap in maps.items():
        for texto, mp3 in amap.items():
            pedidos.setdefault(mp3, (texto, []))[1].append(html)

    no_disco = set(os.path.basename(p) for p in glob.glob(os.path.join(aud, '*.mp3')))
    faltam = [(mp3, t) for mp3, (t, _) in sorted(pedidos.items()) if mp3 not in no_disco]
    orfaos = sorted(no_disco - set(pedidos))

    print('HTMLs com AUDIO_MAP : %d' % len(maps))
    print('frases pedidas      : %d' % len(pedidos))
    print('MP3 no disco        : %d' % len(no_disco))
    print('FALTAM              : %d' % len(faltam))
    for mp3, t in faltam:
        print('   - %-62s  %s' % (mp3, t[:70]))
    print('orfaos (nao deletar): %d' % len(orfaos))

    if not gen:
        return 1 if faltam else 0

    if not faltam:
        print('nada a gerar')
        return 0

    k = key()
    ledger_path = os.path.join(aud, '_src.json')
    try:
        ledger = json.load(open(ledger_path, encoding='utf-8'))
    except (IOError, ValueError):
        ledger = {}

    erros = 0
    for mp3, texto in faltam:
        piso = len(texto) * MIN_BYTES_PER_CHAR
        data = None
        for tentativa in range(1, MAX_TRIES + 1):
            try:
                data = tts(texto, VOZ, k)
            except Exception as e:
                print('  ! ERR %s -> %s' % (mp3, str(e)[:120]))
                data = None
                time.sleep(1.5)
                continue
            if len(data) >= piso:
                break
            print('  ~ %s CURTO (%d b p/ %d chars, min %d) — re-tentando %d/%d'
                  % (mp3, len(data), len(texto), piso, tentativa, MAX_TRIES))
            data = None
            time.sleep(1.2)
        if data is None:
            erros += 1
            print('  X NAO GRAVADO: %s' % mp3)
            continue
        open(os.path.join(aud, mp3), 'wb').write(data)
        ledger[mp3] = hashlib.sha1((VOZ + '|' + texto).encode('utf-8')).hexdigest()
        print('  + %-62s %d b (%s)' % (mp3, len(data), VOZ))
        time.sleep(0.3)

    with open(ledger_path, 'w', encoding='utf-8') as lf:
        json.dump(ledger, lf, indent=1, sort_keys=True, ensure_ascii=False)
        lf.write('\n')
    print('gerados: %d   erros: %d' % (len(faltam) - erros, erros))
    return 1 if erros else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
