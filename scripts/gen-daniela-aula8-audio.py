#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera MP3s ElevenLabs da Aula 8 (Daniela) a partir de daniela-aula8-audio.json.
Skip existentes (REGRA C9). Roster REGRA 35/C1 (worktree). Modelo multilingual_v2."""
import os, json, time, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT  = os.path.join(ROOT, 'public', 'audio', 'daniela-feitoza-aula8')
VOICES = {
    'arthur': 'sfJopaWaOtauCD3HKX6Q', 'ellen': 'BIvP0GN1cAtSRTxNHnWS',
    'josh': 'TxGEqnHWrfWFTfGW9XjX', 'rachel': '21m00Tcm4TlvDq8ikWAM',
    'domi': 'AZnzlk1XvdvUeBnXmlld', 'bella': 'EXAVITQu4vr4xnSDxMaL',
}
KEY = os.environ.get('ELEVENLABS_API_KEY')
assert KEY, 'ELEVENLABS_API_KEY not set'
os.makedirs(OUT, exist_ok=True)
phrases = json.load(open(os.path.join(HERE, 'daniela-aula8-audio.json'), encoding='utf-8'))

gen = skip = err = 0
for p in phrases:
    fp = os.path.join(OUT, p['file'])
    if os.path.exists(fp) and os.path.getsize(fp) > 0:
        skip += 1; print('  . skip', p['file']); continue
    body = json.dumps({
        'text': p['text'],
        'model_id': 'eleven_multilingual_v2',
        'voice_settings': {'stability': 0.5, 'similarity_boost': 0.75, 'style': 0.0, 'use_speaker_boost': True},
    }).encode('utf-8')
    url = 'https://api.elevenlabs.io/v1/text-to-speech/' + VOICES[p['voice']]
    req = urllib.request.Request(url, data=body, headers={
        'xi-api-key': KEY, 'Content-Type': 'application/json', 'Accept': 'audio/mpeg'})
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            data = r.read()
        with open(fp, 'wb') as f:
            f.write(data)
        gen += 1; print('  + gen  %s (%s, %d bytes)' % (p['file'], p['voice'], len(data)))
        time.sleep(0.3)
    except Exception as e:
        err += 1; print('  ! ERR  %s -> %s' % (p['file'], str(e)[:160]))

print('\nDone: %d generated, %d skipped, %d errors' % (gen, skip, err))
