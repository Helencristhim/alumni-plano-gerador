#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate ElevenLabs MP3s for Milton Aula 8 from phrases.json. Skips existing.
Voices: arthur/ellen (REGRA 35). model eleven_multilingual_v2."""
import os, re, json, time, urllib.request, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
# worktree root = parents of _build/milton-aula8
WT = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(WT, 'public', 'audio', 'milton-sayegh')
# key lives in the canonical clone's .env.local (gitignored, not in the worktree)
ENV_CANDIDATES = [
    os.path.join(WT, '.env.local'),
    '/home/dan/dev/work/better/alumni-plano-gerador/.env.local',
]
VOICES = {'arthur': 'sfJopaWaOtauCD3HKX6Q', 'ellen': 'BIvP0GN1cAtSRTxNHnWS'}

def api_key():
    k = os.environ.get('ELEVENLABS_API_KEY')
    if k:
        return k
    for p in ENV_CANDIDATES:
        try:
            m = re.search(r'ELEVENLABS_API_KEY=(\S+)', open(p).read())
            if m:
                return m.group(1)
        except OSError:
            pass
    return None

def main():
    key = api_key()
    assert key, 'ELEVENLABS_API_KEY not found'
    os.makedirs(OUT, exist_ok=True)
    phrases = json.load(open(os.path.join(HERE, 'phrases.json'), encoding='utf-8'))
    gen = skip = err = 0
    for p in phrases:
        fp = os.path.join(OUT, p['file'])
        if os.path.exists(fp):
            skip += 1; print('  . skip', p['file']); continue
        body = json.dumps({
            'text': p['text'],
            'model_id': 'eleven_multilingual_v2',
            'voice_settings': {'stability': 0.5, 'similarity_boost': 0.75, 'style': 0.0, 'use_speaker_boost': True},
        }).encode('utf-8')
        url = 'https://api.elevenlabs.io/v1/text-to-speech/' + VOICES[p['voice']]
        req = urllib.request.Request(url, data=body, headers={
            'xi-api-key': key, 'Content-Type': 'application/json', 'Accept': 'audio/mpeg'}, method='POST')
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                data = r.read()
            with open(fp, 'wb') as f:
                f.write(data)
            gen += 1; print('  + gen  %s (%s, %d bytes)' % (p['file'], p['voice'], len(data)))
            time.sleep(0.3)
        except urllib.error.HTTPError as e:
            err += 1; print('  ! ERR  %s -> HTTP %s %s' % (p['file'], e.code, e.read().decode('utf-8','ignore')[:120]))
        except Exception as e:
            err += 1; print('  ! ERR  %s -> %s' % (p['file'], str(e)[:120]))
    print('\nDone: %d generated, %d skipped, %d errors' % (gen, skip, err))

main()
