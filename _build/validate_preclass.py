#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""validate_preclass.py — gates do Pre-class B2 (fragmento accordion):
1. 5 etapas REGRA 4 presentes (1.1 vocab cards c/ audio, 1.2 matching dropdown,
   1.3 Grammar in Context texto+quiz, 1.4 Grammar Tip bilingue, 1.5 fill-in-blank)
   + Pronúncia (speech-card), Quiz situacional, Think.
2. Áudio 0 missing: cada speakText('frase')/data-phrase tem pc{N}_<snake>.mp3 no disco;
   cada [order-l{N}]/[...] está declarado no extra_audio do config.
USO: python3 _build/validate_preclass.py _build/{slug}-aula{N}/config.json
"""
import json, os, re, sys, unicodedata

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


def snake(text, maxlen=48):
    t = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode()
    t = re.sub(r"[^a-z0-9]+", '_', t.lower()).strip('_')
    return t[:maxlen].rstrip('_')


def main():
    cfg_path = os.path.abspath(sys.argv[1])
    cdir = os.path.dirname(cfg_path)
    cfg = json.load(open(cfg_path, encoding='utf-8'))
    n = cfg['lesson']['n']
    slug = cfg['slug']
    pc = open(os.path.join(cdir, 'preclass.html'), encoding='utf-8').read()
    errs, warns = [], []

    # ---- REGRA 4: 5 etapas + extras ----
    checks = {
        '1.1 Vocab cards (audio)': 'vocab-card-pc' in pc and "speakText(" in pc,
        '1.2 Matching dropdown': 'match-row' in pc and '<select' in pc and 'checkMatch' in pc,
        '1.3 Grammar in Context': re.search(r'Grammar in Context', pc) and 'selectQuiz' in pc,
        '1.4 Grammar Tip (bilingue)': re.search(r'Grammar Tip', pc) is not None,
        '1.5 Fill-in-the-blank': 'blank-input' in pc and 'checkBlank' in pc,
        'Pronúncia (speech-card)': 'speech-card' in pc and 'speakPhrase' in pc,
        'Quiz situacional': pc.count('quiz-item') >= 4,  # 1.3 (3) + stage 4 (3+)
        'Think (free production)': 'think-card' in pc and 'startFreeRecording' in pc,
    }
    for k, ok in checks.items():
        if not ok:
            errs.append(f'ETAPA FALTA: {k}')

    # Grammar Tip bilingue: precisa de PT (heurística: acento ou palavra-ponte PT)
    gt = re.search(r'Grammar Tip.*?</div>\s*</div>', pc, re.S)
    block = gt.group(0) if gt else pc
    if not re.search(r'[áàâãéêíóôõúç]| voce | para | que |Portugu', pc):
        warns.append('Grammar Tip pode não ter PT (REGRA 4 exige bilingue EN+PT)')

    # ---- Áudio 0 missing ----
    OUT = os.path.join(ROOT, 'public', 'audio', slug)
    phrases = set()
    for m in re.finditer(r"speakText\('((?:[^'\\]|\\.)*)'", pc):
        t = m.group(1).replace("\\'", "'")
        if t.startswith('['):
            # bracket key — deve estar no extra_audio
            keys = {e['key'] for e in cfg['lesson'].get('extra_audio', [])}
            if t not in keys:
                errs.append(f'BRACKET KEY {t} sem extra_audio no config')
        else:
            phrases.add(t)
    for m in re.finditer(r'data-phrase="([^"]*)"', pc):
        phrases.add(m.group(1))

    miss = []
    for p in sorted(phrases):
        f = f'pc{n}_{snake(p)}.mp3'
        if not os.path.exists(os.path.join(OUT, f)):
            miss.append(f'{f}   <- "{p[:50]}"')
    for e in cfg['lesson'].get('extra_audio', []):
        if not os.path.exists(os.path.join(OUT, e['file'])):
            miss.append(f"{e['file']}   <- extra_audio {e['key']}")
    if miss:
        errs.append('AUDIO MISSING (%d):\n   ' % len(miss) + '\n   '.join(miss))

    print(f'== validate preclass aula {n} ({slug}) ==')
    print(f'  fonemas/frases: {len(phrases)} | extra_audio: {len(cfg["lesson"].get("extra_audio", []))}')
    for w in warns:
        print('  WARN:', w)
    if errs:
        print('FAIL:')
        for e in errs:
            print('  X', e)
        sys.exit(1)
    print('  OK — 5 etapas REGRA 4 presentes, 0 audio missing')


if __name__ == '__main__':
    main()
