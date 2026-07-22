#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""gen_audio.py — gera os MP3s ElevenLabs de uma aula buildada pelo build_from_model.py.
Lê o audio_manifest.json ao lado do config.json. Pula existentes. Vozes em voices.json
(REGRA 35: arthur/ellen — Ash/Kristen NÃO existem na conta). Modelo: eleven_multilingual_v2.

USO: ELEVENLABS_API_KEY=... python3 _build/model/gen_audio.py _build/{slug}-aula{N}/config.json
"""
import json
import os
import sys
import time
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
VOICES = json.load(open(os.path.join(HERE, 'voices.json'), encoding='utf-8'))

cfg_path = os.path.abspath(sys.argv[1])
cfg = json.load(open(cfg_path, encoding='utf-8'))
manifest = json.load(open(os.path.join(os.path.dirname(cfg_path), 'audio_manifest.json'), encoding='utf-8'))
OUT = os.path.join(ROOT, 'public', 'audio', cfg['slug'])
KEY = os.environ.get('ELEVENLABS_API_KEY')
if not KEY:
    # Fallback PERMANENTE: a key fica fora do repo público (nunca commitada), em
    # ~/.config/alumni/elevenlabs.key. Assim o áudio roda sem precisar passar a key
    # toda vez (env continua tendo prioridade). Ver memória elevenlabs-key-local.
    _keyfile = os.path.expanduser('~/.config/alumni/elevenlabs.key')
    if os.path.exists(_keyfile):
        with open(_keyfile, encoding='utf-8') as _kf:
            KEY = _kf.read().strip()
assert KEY, ('ELEVENLABS_API_KEY não setada e ~/.config/alumni/elevenlabs.key não existe. '
             'Crie o arquivo com a key (chmod 600) ou exporte a variável.')
os.makedirs(OUT, exist_ok=True)

# Vozes: voices.json (arthur/ellen, inglês) + override por config (cfg['voices']).
# REGRA: material NÃO-inglês (lang != 'en') NUNCA pode usar voz de inglês — exige
# override com vozes do idioma-alvo (ex: espanhol = vozes de Espanha). Trava de código.
VOICES = {**VOICES, **cfg.get('voices', {})}
LANG = cfg.get('lang', 'en')
assert LANG == 'en' or cfg.get('voices'), (
    f"aula lang='{LANG}' SEM 'voices' no config — material não-inglês exige vozes do "
    f"idioma-alvo (proibido usar arthur/ellen, que são vozes de inglês).")

FORCE = '--force' in sys.argv or os.environ.get('GEN_AUDIO_FORCE') == '1'

# GUARD DE TRUNCAMENTO (nasce certo, não depende só do GATE 5b).
# A ElevenLabs às vezes devolve um clipe curto/parcial (foi o que truncou o Stage 2 da
# Anna). gen_audio gravava cego + pulava existentes => o arquivo ruim fossilizava e só o
# gate downstream pegava. Aqui medimos o retorno vs. o TEXTO (text-aware, MESMO corte do
# scripts/check_order_audio_len.py) e RE-TENTAMOS na hora. Piso 400 B/char: áudio saudável
# tem ~600-1150 B/char; truncado <200. Texto de 1-2 palavras fica muito acima de 400, então
# NUNCA re-tenta à toa. Se todas as tentativas vierem curtas, NÃO grava e conta como erro
# (sys.exit(1) => alto, dá pra re-rodar) em vez de gravar podre silenciosamente.
MIN_BYTES_PER_CHAR = 400
MAX_TRIES = 3


def tts(text, voice):
    body = json.dumps({'text': text, 'model_id': 'eleven_multilingual_v2',
                       'voice_settings': {'stability': 0.5, 'similarity_boost': 0.75,
                                          'style': 0.0, 'use_speaker_boost': True}}).encode('utf-8')
    req = urllib.request.Request('https://api.elevenlabs.io/v1/text-to-speech/' + VOICES[voice],
                                 data=body, headers={'xi-api-key': KEY, 'Content-Type': 'application/json',
                                                     'Accept': 'audio/mpeg'})
    with urllib.request.urlopen(req, timeout=90) as r:
        return r.read()


gen = skip = err = 0
for p in manifest:
    fp = os.path.join(OUT, p['file'])
    if os.path.exists(fp) and not FORCE:
        skip += 1
        continue
    floor = len(p['text']) * MIN_BYTES_PER_CHAR  # tamanho mínimo compatível com o texto
    data = None
    try:
        for attempt in range(1, MAX_TRIES + 1):
            data = tts(p['text'], p['voice'])
            if len(data) >= floor:
                break  # tamanho bate com o texto — ok
            print('  ~ %s CURTO (%d b p/ %d chars, min %d) — re-tentando %d/%d'
                  % (p['file'], len(data), len(p['text']), floor, attempt, MAX_TRIES))
            data = None
            time.sleep(1.2)
    except Exception as e:
        err += 1
        print('  ! ERR %s -> %s' % (p['file'], str(e)[:140]))
        continue
    if data is None:
        err += 1
        print('  ! TRUNCADO %s — %d tentativas vieram curtas p/ o texto; NAO gravado (re-rode)'
              % (p['file'], MAX_TRIES))
        continue
    open(fp, 'wb').write(data)
    gen += 1
    print('  + %s (%s, %d b)' % (p['file'], p['voice'], len(data)))
    time.sleep(0.3)
print('Done: %d gen, %d skip, %d err (total %d)' % (gen, skip, err, len(manifest)))
sys.exit(1 if err else 0)
