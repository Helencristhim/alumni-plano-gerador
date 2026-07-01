#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Substitui o bloco Pre-class B1 antigo (id="ex-lesson-N") no hub prof+aluno da
Pricila pelo bloco B2 ja autorado em _build/pricila-adamo-aula{N}/preclass.html, e
mescla as entradas de audioMap (pc{N}_*) a partir de pc_audio_manifest.json.
NAO toca standalones, complementares, stamps nem totalLessons. REGRA 29.
Uso: python3 _build/patch_hub_coherence.py N
Idempotente por chave de audioMap; a troca de bloco e sempre feita.
"""
import json, os, re, sys

N = int(sys.argv[1])
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
D = os.path.join(HERE, 'pricila-adamo-aula%d' % N)

new_block = open(os.path.join(D, 'preclass.html'), encoding='utf-8').read().rstrip('\n')
_mf = os.path.join(D, 'pc_audio_manifest.json')
if not os.path.exists(_mf):
    _mf = os.path.join(D, 'preclass_audio_manifest.json')
manifest = json.load(open(_mf, encoding='utf-8'))
AUDIO_BASE = '/audio/pricila-adamo/'


def block_range(h, n):
    m = re.search(r'<div class="lesson-card[^"]*" id="ex-lesson-%d">' % n, h)
    assert m, 'ex-lesson-%d nao encontrado' % n
    i = m.start(); depth = 0; j = i
    for t in re.finditer(r'<(/?)div\b[^>]*>', h[i:]):
        depth += 1 if t.group(1) == '' else -1
        if depth == 0:
            j = i + t.end(); break
    assert depth == 0, 'div desbalanceado em ex-lesson-%d' % n
    return i, j


def audiomap_inject(h):
    open_tag = 'var audioMap = {\n'
    oi = h.index(open_tag) + len(open_tag)
    region_end = h.index('};', oi)
    region = h[oi:region_end]
    order_re = re.compile(r'pc%d_order' % N)
    lines = []
    for e in manifest:
        # O botao Ouvir do Stage 2 chama speakText('[order-lN]'); a chave no audioMap
        # DEVE ser "[order-lN]" (nao o texto da historia). Re-aponta a entrada B1 antiga
        # (order_lN_*.mp3) para o MP3 B2 (pcN_order_*.mp3).
        if order_re.search(e['file']):
            key = '[order-l%d]' % N
            newval = json.dumps(AUDIO_BASE + e['file'])
            pat = re.compile(r'("\[order-l%d\]":\s*)"[^"]*"' % N)
            if pat.search(h):
                h = pat.sub(lambda m: m.group(1) + newval, h, count=1)
            else:
                h = h[:oi] + '  %s: %s,\n' % (json.dumps(key), newval) + h[oi:]
                oi += len('  %s: %s,\n' % (json.dumps(key), newval))
            continue
        key = json.dumps(e['text'], ensure_ascii=False)
        if (key + ':') in region or (key + ' :') in region:
            continue
        lines.append('  %s: %s,' % (key, json.dumps(AUDIO_BASE + e['file'])))
    if lines:
        h = h[:oi] + '\n'.join(lines) + '\n' + h[oi:]
    return h, len(lines)


def patch(path):
    h = open(path, encoding='utf-8').read()
    i, j = block_range(h, N)
    h = h[:i] + new_block + h[j:]
    h, added = audiomap_inject(h)
    open(path, 'w', encoding='utf-8').write(h)
    print('  patched %s (audioMap +%d)' % (os.path.relpath(path, ROOT), added))


patch(os.path.join(ROOT, 'public', 'professor', 'pricila-adamo.html'))
patch(os.path.join(ROOT, 'public', 'aluno', 'pricila-adamo.html'))
print('hub coherence patch aula %d done' % N)
