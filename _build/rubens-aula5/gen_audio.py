#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate ElevenLabs MP3s for Rubens aula 5 from phrases.json (stdlib only; no node).
Key: ELEVENLABS_API_KEY env, or read from alumni-plano-gerador/.env.local. Skips existing files."""
import os, re, json, time, urllib.request, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
OUT  = os.path.join(ROOT, 'public', 'audio', 'rubens-tofolo')
VOICES = {'arthur':'sfJopaWaOtauCD3HKX6Q','ellen':'BIvP0GN1cAtSRTxNHnWS',
          'josh':'TxGEqnHWrfWFTfGW9XjX','rachel':'21m00Tcm4TlvDq8ikWAM',
          'domi':'AZnzlk1XvdvUeBnXmlld','bella':'EXAVITQu4vr4xnSDxMaL'}

def get_key():
    k = os.environ.get('ELEVENLABS_API_KEY')
    if k: return k.strip()
    for env in ('/home/dan/dev/work/better/alumni-plano-gerador/.env.local',):
        if os.path.exists(env):
            for line in open(env, encoding='utf-8'):
                m = re.match(r'\s*ELEVENLABS_API_KEY\s*=\s*["\']?([^"\'\s]+)', line)
                if m: return m.group(1)
    raise SystemExit('No ELEVENLABS_API_KEY found')

KEY = get_key()
os.makedirs(OUT, exist_ok=True)
phrases = json.load(open(os.path.join(HERE, 'phrases.json'), encoding='utf-8'))

gen = skip = err = 0
for p in phrases:
    fp = os.path.join(OUT, p['file'])
    if os.path.exists(fp):
        skip += 1; continue
    vid = VOICES[p['voice']]
    body = json.dumps({'text': p['text'], 'model_id': 'eleven_multilingual_v2',
        'voice_settings': {'stability': 0.5, 'similarity_boost': 0.75, 'style': 0, 'use_speaker_boost': True}}).encode()
    req = urllib.request.Request('https://api.elevenlabs.io/v1/text-to-speech/' + vid,
        data=body, headers={'xi-api-key': KEY, 'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            data = r.read()
        with open(fp, 'wb') as f: f.write(data)
        gen += 1; print('gen %-45s %s' % (p['file'], p['voice'])); time.sleep(0.3)
    except urllib.error.HTTPError as e:
        err += 1; print('ERR %s -> HTTP %s %s' % (p['file'], e.code, e.read()[:120]))
    except Exception as e:
        err += 1; print('ERR %s -> %s' % (p['file'], e))
print('done: %d generated, %d skipped, %d errors' % (gen, skip, err))
