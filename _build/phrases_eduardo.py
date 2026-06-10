#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generic phrases extractor for Eduardo Chiba aula N.
Usage: python3 _build/phrases_eduardo.py N
Reads _build/aula{N}/{slides,preclass}.html (+ optional aula{N}/listenings.json),
maps reused texts to EXISTING hub audioMap files (REGRA C9), assigns new aula{N}_ files + voices.
Writes _build/aula{N}/phrases.json."""
import os, re, json, hashlib, sys

N = int(sys.argv[1])
HERE = os.path.dirname(os.path.abspath(__file__))
WT   = os.path.abspath(os.path.join(HERE, '..'))
HUB  = os.path.join(WT, 'public', 'professor', 'eduardo-chiba.html')
SLUG = 'eduardo-chiba'
D    = os.path.join(HERE, 'aula%d' % N)

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()

slides   = read(os.path.join(D, 'slides.html'))
preclass = read(os.path.join(D, 'preclass.html'))
hub      = read(HUB)

blk = hub[hub.index('audioMap'):hub.index('};', hub.index('audioMap'))]
existing = {}
for k, v in re.findall(r'"((?:[^"\\]|\\.)*)":\s*"(/audio/%s/[^"]+\.mp3)"' % re.escape(SLUG), blk):
    existing[k.replace('\\"', '"')] = v

voice_of = {}
for m in re.finditer(r'data-voice="([^"]+)"[^>]*>.*?speakText\(\'((?:[^\'\\]|\\.)*)\'', slides, re.S):
    voice_of[m.group(2).replace("\\'", "'")] = m.group(1)

calls, seen = [], set()
def add(t):
    if t and t not in seen:
        seen.add(t); calls.append(t)
for src in (slides, preclass):
    for m in re.findall(r"speakText\('((?:[^'\\]|\\.)*)'", src):
        add(m.replace("\\'", "'"))
    for m in re.findall(r'data-phrase="((?:[^"\\]|\\.)*)"', src):
        add(m.replace('\\"', '"'))

def slug_file(t):
    s = re.sub(r"[^a-z0-9]+", "_", t.lower()).strip("_")
    h = hashlib.md5(t.encode('utf-8')).hexdigest()[:6]
    return 'aula%d_%s_%s.mp3' % (N, s[:40], h)

phrases, reused, new = [], 0, 0
for t in calls:
    if t in existing:
        f = os.path.basename(existing[t]); reused += 1; voice = 'arthur'
    else:
        f = slug_file(t); new += 1; voice = voice_of.get(t, 'arthur')
    phrases.append({'key': t, 'text': t, 'file': f, 'voice': voice})

# listenings.json: [{key,file,voice,text}] for player data-src MP3s (not in calls)
lp = os.path.join(D, 'listenings.json')
if os.path.exists(lp):
    phrases += json.load(open(lp, encoding='utf-8'))

with open(os.path.join(D, 'phrases.json'), 'w', encoding='utf-8') as f:
    json.dump(phrases, f, ensure_ascii=False, indent=2)

files = [p['file'] for p in phrases]
assert len(files) == len(set(files)), 'DUPLICATE FILES'
assert len({p['key'] for p in phrases}) == len(phrases), 'DUPLICATE KEYS'
print('aula%d phrases.json: %d total (%d reused, %d new, voices=%s)' % (
    N, len(phrases), reused, new, sorted(set(p['voice'] for p in phrases))))
