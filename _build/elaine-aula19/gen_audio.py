#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate ElevenLabs MP3s for Elaine Aula 18 from phrases.json (Python fallback; node absent).
Skips existing files (REGRA C9). Model eleven_multilingual_v2. Roster per REGRA 35/C1."""
import os, json, time, urllib.request, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
OUTDIR = os.path.join(ROOT, 'public', 'audio', 'elaine-mieko-pinho')
ENV = '/home/dan/dev/work/better/alumni-plano-gerador/.env.local'

VOICES = {'arthur':'sfJopaWaOtauCD3HKX6Q','ellen':'BIvP0GN1cAtSRTxNHnWS',
          'josh':'TxGEqnHWrfWFTfGW9XjX','rachel':'21m00Tcm4TlvDq8ikWAM',
          'domi':'AZnzlk1XvdvUeBnXmlld','bella':'EXAVITQu4vr4xnSDxMaL'}

key = os.environ.get('ELEVENLABS_API_KEY')
if not key and os.path.exists(ENV):
    for line in open(ENV, encoding='utf-8'):
        line = line.strip()
        if line.startswith('ELEVENLABS_API_KEY'):
            key = line.split('=',1)[1].strip().strip('"').strip("'")
assert key, 'no ELEVENLABS_API_KEY in env or ' + ENV

phrases = json.load(open(os.path.join(HERE,'phrases.json'), encoding='utf-8'))
os.makedirs(OUTDIR, exist_ok=True)

gen=skip=err=0
for p in phrases:
    fp = os.path.join(OUTDIR, p['file'])
    if os.path.exists(fp):
        skip+=1; continue
    vid = VOICES[p['voice']]
    body = json.dumps({'text':p['text'],'model_id':'eleven_multilingual_v2',
        'voice_settings':{'stability':0.5,'similarity_boost':0.75,'style':0.0,'use_speaker_boost':True}}).encode('utf-8')
    req = urllib.request.Request('https://api.elevenlabs.io/v1/text-to-speech/'+vid,
        data=body, headers={'xi-api-key':key,'Content-Type':'application/json'}, method='POST')
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            data = r.read()
        with open(fp,'wb') as f: f.write(data)
        gen+=1; print('+ '+p['file'])
        time.sleep(0.3)
    except urllib.error.HTTPError as e:
        err+=1; print('ERROR %s %s -> %s' % (e.code, p['file'], e.read()[:200]))
    except Exception as e:
        err+=1; print('ERROR %s -> %r' % (p['file'], e))
print('\nDone: %d generated, %d skipped, %d errors' % (gen, skip, err))
