#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera MP3s ElevenLabs da aula 3 da Simone a partir de phrases.json.
Skips existentes. Modelo eleven_multilingual_v2. Vozes Arthur/Ellen (REGRA 35)."""
import os, json, time, urllib.request, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))            # wt-simone
OUTDIR = os.path.join(ROOT, 'public', 'audio', 'simone-quiles-de-santana-marques')
ENV = '/home/dan/dev/work/better/alumni-plano-gerador/.env.local'
VOICES = {'arthur': 'sfJopaWaOtauCD3HKX6Q', 'ellen': 'BIvP0GN1cAtSRTxNHnWS'}

key = None
for line in open(ENV, encoding='utf-8'):
    line = line.strip()
    if line.startswith('ELEVENLABS_API_KEY'):
        key = line.split('=', 1)[1].strip().strip('"').strip("'")
assert key, 'no ELEVENLABS_API_KEY in ' + ENV

phrases = json.load(open(os.path.join(HERE, 'phrases.json'), encoding='utf-8'))
os.makedirs(OUTDIR, exist_ok=True)
gen = skip = err = 0
for p in phrases:
    fp = os.path.join(OUTDIR, p['file'])
    if os.path.exists(fp):
        skip += 1; continue
    body = json.dumps({'text': p['text'], 'model_id': 'eleven_multilingual_v2',
        'voice_settings': {'stability': 0.5, 'similarity_boost': 0.75, 'style': 0.0, 'use_speaker_boost': True}}).encode('utf-8')
    req = urllib.request.Request('https://api.elevenlabs.io/v1/text-to-speech/' + VOICES[p['voice']],
        data=body, headers={'xi-api-key': key, 'Content-Type': 'application/json', 'Accept': 'audio/mpeg'}, method='POST')
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            data = r.read()
        with open(fp, 'wb') as f:
            f.write(data)
        gen += 1; print('+ %s (%s, %d bytes)' % (p['file'], p['voice'], len(data)))
        time.sleep(0.4)
    except urllib.error.HTTPError as e:
        err += 1; print('! HTTP %s on %s: %s' % (e.code, p['file'], e.read()[:200]))
    except Exception as e:
        err += 1; print('! %s on %s: %s' % (type(e).__name__, p['file'], str(e)[:120]))
print('\ngen=%d skip=%d err=%d total=%d' % (gen, skip, err, len(phrases)))
