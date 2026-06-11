#!/usr/bin/env python3
"""Generate ElevenLabs MP3s for Nilo Aula 9 from phrases.json. Skips existing (REGRA C9)."""
import os, json, time, urllib.request, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))  # wt-nilo
OUT  = os.path.join(ROOT, 'public', 'audio', 'nilo-mesquita-patucci')

VOICES = {
    'arthur': 'sfJopaWaOtauCD3HKX6Q',  # Male (protagonist Nilo)
    'ellen': 'BIvP0GN1cAtSRTxNHnWS',   # Female (Carla / Ms. Klein)
}

KEY = os.environ.get('ELEVENLABS_API_KEY')
if not KEY:
    # fall back to .env.local in the canonical clone
    for envp in [os.path.join(ROOT, '.env.local'),
                 os.path.join(ROOT, '..', 'alumni-plano-gerador', '.env.local')]:
        if os.path.exists(envp):
            for line in open(envp):
                if line.startswith('ELEVENLABS_API_KEY='):
                    KEY = line.split('=', 1)[1].strip().strip('"').strip("'")
assert KEY, 'ELEVENLABS_API_KEY not set'
os.makedirs(OUT, exist_ok=True)
phrases = json.load(open(os.path.join(HERE, 'phrases.json'), encoding='utf-8'))

made = skip = fail = 0
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
        'xi-api-key': KEY, 'Content-Type': 'application/json', 'Accept': 'audio/mpeg'})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            data = r.read()
        with open(fp, 'wb') as f:
            f.write(data)
        made += 1; print('  + made', p['file'], '(%d bytes)' % len(data))
        time.sleep(0.3)
    except Exception as e:
        fail += 1; print('  ! FAIL', p['file'], e, file=sys.stderr)

print('\nDONE: made=%d skip=%d fail=%d  ->  %s' % (made, skip, fail, OUT))
sys.exit(1 if fail else 0)
