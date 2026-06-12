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
assert KEY, 'ELEVENLABS_API_KEY not set'
os.makedirs(OUT, exist_ok=True)

gen = skip = err = 0
for p in manifest:
    fp = os.path.join(OUT, p['file'])
    if os.path.exists(fp):
        skip += 1
        continue
    body = json.dumps({'text': p['text'], 'model_id': 'eleven_multilingual_v2',
                       'voice_settings': {'stability': 0.5, 'similarity_boost': 0.75,
                                          'style': 0.0, 'use_speaker_boost': True}}).encode('utf-8')
    req = urllib.request.Request('https://api.elevenlabs.io/v1/text-to-speech/' + VOICES[p['voice']],
                                 data=body, headers={'xi-api-key': KEY, 'Content-Type': 'application/json',
                                                     'Accept': 'audio/mpeg'})
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            data = r.read()
        open(fp, 'wb').write(data)
        gen += 1
        print('  + %s (%s, %d b)' % (p['file'], p['voice'], len(data)))
        time.sleep(0.3)
    except Exception as e:
        err += 1
        print('  ! ERR %s -> %s' % (p['file'], str(e)[:140]))
print('Done: %d gen, %d skip, %d err (total %d)' % (gen, skip, err, len(manifest)))
sys.exit(1 if err else 0)
