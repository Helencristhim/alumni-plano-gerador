#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera os MP3s ElevenLabs da Helen Mendes (mock) a partir de audio_manifest.json.
Pula existentes. Vozes REGRA 35 (arthur/ellen). multilingual_v2.
Uso: ELEVENLABS_API_KEY=... python3 _build/helen-mendes/gen_audio_helen.py"""
import os, json, time, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
OUT = os.path.join(ROOT, 'public', 'audio', 'helen-mendes')
VOICES = {'arthur': 'sfJopaWaOtauCD3HKX6Q', 'ellen': 'BIvP0GN1cAtSRTxNHnWS'}
KEY = os.environ.get('ELEVENLABS_API_KEY'); assert KEY, 'ELEVENLABS_API_KEY not set'
os.makedirs(OUT, exist_ok=True)
manifest = json.load(open(os.path.join(HERE, 'audio_manifest.json'), encoding='utf-8'))
gen = skip = err = 0
for p in manifest:
    fp = os.path.join(OUT, p['file'])
    if os.path.exists(fp): skip += 1; continue
    body = json.dumps({'text': p['text'], 'model_id': 'eleven_multilingual_v2',
        'voice_settings': {'stability': 0.5, 'similarity_boost': 0.75, 'style': 0.0, 'use_speaker_boost': True}}).encode('utf-8')
    req = urllib.request.Request('https://api.elevenlabs.io/v1/text-to-speech/' + VOICES[p['voice']],
        data=body, headers={'xi-api-key': KEY, 'Content-Type': 'application/json', 'Accept': 'audio/mpeg'})
    try:
        with urllib.request.urlopen(req, timeout=90) as r: data = r.read()
        open(fp, 'wb').write(data); gen += 1; print('  + %s (%s, %d b)' % (p['file'], p['voice'], len(data))); time.sleep(0.3)
    except Exception as e:
        err += 1; print('  ! ERR %s -> %s' % (p['file'], str(e)[:140]))
print('Done: %d gen, %d skip, %d err (total %d)' % (gen, skip, err, len(manifest)))
