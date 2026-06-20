#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""gen_preclass_audio.py — gera os MP3s pc{N}_ do Pre-class de UMA aula, SEM tocar
hub/standalone/manifest. Lê o preclass.html (speakText('...') + data-phrase) + o
extra_audio do config.json, atribui vozes (mesma lógica do build_from_model:
1-2 palavras=arthur; frases alternam ellen/arthur; data-voice vence; fala 1a pessoa
da aluna=voz do gênero) e gera pc{N}_<snake>.mp3 em public/audio/{slug}/.
Pula existentes. ElevenLabs eleven_multilingual_v2.

USO: set -a && source .env.local && set +a
     python3 _build/gen_preclass_audio.py _build/{slug}-aula{N}/config.json
"""
import json, os, re, sys, time, unicodedata, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = os.path.join(HERE, 'model')
ROOT = os.path.abspath(os.path.join(HERE, '..'))
VOICES = json.load(open(os.path.join(MODEL, 'voices.json'), encoding='utf-8'))


def snake(text, maxlen=48):
    t = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode()
    t = re.sub(r"[^a-z0-9]+", '_', t.lower()).strip('_')
    return t[:maxlen].rstrip('_')


def extract_phrases(html):
    out = []
    for line in html.split('\n'):
        mv = re.search(r'data-voice="([a-z]+)"', line)
        hint = mv.group(1) if mv else None
        for m in re.finditer(r"speakText\('((?:[^'\\]|\\.)*)'", line):
            t = m.group(1).replace("\\'", "'")
            if not t.startswith('['):
                out.append((t, hint))
        for m in re.finditer(r'data-phrase="([^"]*)"', line):
            out.append((m.group(1), hint))
    return out


def assign_voices(phrases, prefix, cfg):
    student_voice = 'ellen' if cfg['gender'] == 'f' else 'arthur'
    first = re.escape(cfg['first_name'])
    first_person = re.compile(rf"\bI am {first}\b|\bI'm {first}\b|\bMy name is {first}\b")
    entries, alt = {}, 0
    for text, hint in phrases:
        if text in entries:
            continue
        if hint:
            voice = hint
        elif len(text.split()) <= 2:
            voice = 'arthur'
        elif first_person.search(text):
            voice = student_voice
        else:
            voice = 'ellen' if alt % 2 == 0 else 'arthur'
            alt += 1
        assert voice in VOICES, f'voz desconhecida "{voice}"'
        entries[text] = dict(voice=voice, file=f'{prefix}{snake(text)}.mp3')
    return entries


def main():
    cfg_path = os.path.abspath(sys.argv[1])
    cdir = os.path.dirname(cfg_path)
    cfg = json.load(open(cfg_path, encoding='utf-8'))
    n = cfg['lesson']['n']
    prefix = f'pc{n}_'
    pc = open(os.path.join(cdir, 'preclass.html'), encoding='utf-8').read()
    entries = assign_voices(extract_phrases(pc), prefix=prefix, cfg=cfg)
    manifest = [dict(text=t, voice=m['voice'], file=m['file']) for t, m in entries.items()]
    # extra_audio (ex.: [order-lN] concatenado) declarado no config
    for e in cfg['lesson'].get('extra_audio', []):
        manifest.append(dict(text=e['text'], voice=e['voice'], file=e['file']))
    # dump pc manifest ao lado do config (rastreio)
    json.dump(manifest, open(os.path.join(cdir, 'preclass_audio_manifest.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    OUT = os.path.join(ROOT, 'public', 'audio', cfg['slug'])
    os.makedirs(OUT, exist_ok=True)
    KEY = os.environ.get('ELEVENLABS_API_KEY')
    assert KEY, 'ELEVENLABS_API_KEY not set (set -a && source .env.local && set +a)'
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
            print('  ! ERR %s -> %s' % (p['file'], str(e)[:160]))
    print('Done aula %d preclass: %d gen, %d skip, %d err (total %d)' % (n, gen, skip, err, len(manifest)))
    if err:
        sys.exit(1)


if __name__ == '__main__':
    main()
