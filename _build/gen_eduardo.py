#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate ElevenLabs MP3s for Eduardo aula N. Usage: python3 _build/gen_eduardo.py N
Skips existing (REGRA C9). Key from alumni-plano-gerador/.env.local or env."""
import os, json, time, urllib.request, sys

N = int(sys.argv[1])
HERE = os.path.dirname(os.path.abspath(__file__))
WT   = os.path.abspath(os.path.join(HERE, '..'))
OUT  = os.path.join(WT, 'public', 'audio', 'eduardo-chiba')
ENV  = '/home/dan/dev/work/better/alumni-plano-gerador/.env.local'
VOICES = {'arthur': 'sfJopaWaOtauCD3HKX6Q', 'ellen': 'BIvP0GN1cAtSRTxNHnWS',
          'josh': 'TxGEqnHWrfWFTfGW9XjX', 'rachel': '21m00Tcm4TlvDq8ikWAM',
          'domi': 'AZnzlk1XvdvUeBnXmlld', 'bella': 'EXAVITQu4vr4xnSDxMaL'}

def load_key():
    k = os.environ.get('ELEVENLABS_API_KEY')
    if k: return k
    if os.path.exists(ENV):
        for line in open(ENV, encoding='utf-8'):
            if line.strip().startswith('ELEVENLABS_API_KEY='):
                return line.split('=', 1)[1].strip().strip('"').strip("'")
    return None

KEY = load_key(); assert KEY, 'ELEVENLABS_API_KEY not set'
os.makedirs(OUT, exist_ok=True)
phrases = json.load(open(os.path.join(HERE, 'aula%d' % N, 'phrases.json'), encoding='utf-8'))

gen = skip = err = 0
for p in phrases:
    fp = os.path.join(OUT, p['file'])
    if os.path.exists(fp): skip += 1; continue
    body = json.dumps({'text': p['text'], 'model_id': 'eleven_multilingual_v2',
        'voice_settings': {'stability': 0.5, 'similarity_boost': 0.75, 'style': 0.0, 'use_speaker_boost': True}}).encode('utf-8')
    req = urllib.request.Request('https://api.elevenlabs.io/v1/text-to-speech/' + VOICES[p['voice']],
        data=body, headers={'xi-api-key': KEY, 'Content-Type': 'application/json', 'Accept': 'audio/mpeg'})
    try:
        with urllib.request.urlopen(req, timeout=120) as r: data = r.read()
        with open(fp, 'wb') as f: f.write(data)
        gen += 1; print('  + %s (%s, %d B)' % (p['file'], p['voice'], len(data))); time.sleep(0.3)
    except Exception as e:
        err += 1; print('  ! ERR %s -> %s' % (p['file'], str(e)[:140]))
print('\naula%d audio: %d generated, %d skipped, %d errors' % (N, gen, skip, err))
sys.exit(1 if err else 0)
