#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""gen_pc_audio.py — gera SO os MP3 Pre-class (pc{N}_) de uma aula, ADITIVO.

Usa EXATAMENTE snake/extract_phrases/assign_voices do builder oficial para que
os nomes batam com o audioMap que o hub vai gerar. Le config.json + preclass.html.
Escreve pc_audio_manifest.json (so pra inspecao) e gera os mp3 em public/audio/{slug}.
Pula existentes (a menos de --force). NAO toca o audio_manifest.json do standalone.

USO: set -a && source .env.local && set +a
     python3 _build/gen_pc_audio.py _build/pricila-adamo-aulaN/config.json
"""
import json
import os
import sys
import time
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
sys.path.insert(0, os.path.join(HERE, 'model'))
from build_from_model import extract_phrases, assign_voices  # noqa: E402

VOICES = json.load(open(os.path.join(HERE, 'model', 'voices.json'), encoding='utf-8'))

cfg_path = os.path.abspath(sys.argv[1])
cfg = json.load(open(cfg_path, encoding='utf-8'))
VOICES = {**VOICES, **cfg.get('voices', {})}
cdir = os.path.dirname(cfg_path)
pc = open(os.path.join(cdir, 'preclass.html'), encoding='utf-8').read()
n = cfg['lesson']['n']

entries = assign_voices(extract_phrases(pc), prefix=f'pc{n}_', cfg=cfg)
manifest = [dict(text=t, voice=m['voice'], file=m['file']) for t, m in entries.items()]
for item in cfg['lesson'].get('extra_audio', []):
    manifest.append(dict(text=item['text'], voice=item['voice'], file=item['file']))

json.dump(manifest, open(os.path.join(cdir, 'pc_audio_manifest.json'), 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print(f'pc manifest: {len(manifest)} entries (lesson {n})')

KEY = os.environ.get('ELEVENLABS_API_KEY')
assert KEY, 'ELEVENLABS_API_KEY not set'
OUT = os.path.join(ROOT, 'public', 'audio', cfg['slug'])
os.makedirs(OUT, exist_ok=True)
FORCE = '--force' in sys.argv
gen = skip = err = 0
for p in manifest:
    fp = os.path.join(OUT, p['file'])
    if os.path.exists(fp) and not FORCE:
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
