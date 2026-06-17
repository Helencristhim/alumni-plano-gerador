#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pre-check: snake(text)[:48] of EVERY distinct audio phrase must be UNIQUE.
Replicates build_from_model.snake / extract_phrases so we catch filename collisions
BEFORE running the builder (this student has hit this twice)."""
import json, re, unicodedata, sys, os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))

def snake(text, maxlen=48):
    t = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode()
    t = re.sub(r"[^a-z0-9]+", '_', t.lower()).strip('_')
    return t[:maxlen].rstrip('_')

def extract_phrases(html):
    out = []
    for line in html.split('\n'):
        for m in re.finditer(r"speakText\('((?:[^'\\]|\\.)*)'", line):
            t = m.group(1).replace("\\'", "'")
            if not t.startswith('['):
                out.append(t)
        for m in re.finditer(r'data-phrase="([^"]*)"', line):
            out.append(m.group(1))
    return out

cfg = json.load(open(os.path.join(HERE, 'config.json'), encoding='utf-8'))
slides = open(os.path.join(HERE, 'slides.html'), encoding='utf-8').read()
preclass = open(os.path.join(HERE, 'preclass.html'), encoding='utf-8').read()

# slide phrases (prefix a14_) + listenings (own filenames) + preclass (prefix pc14_)
groups = {}
slide_entries = []
seen = set()
for t in extract_phrases(slides):
    if t not in seen:
        seen.add(t); slide_entries.append(t)
for t in slide_entries:
    groups[f'a14_{snake(t)}.mp3'] = ('slide', t)

for li in cfg['lesson'].get('listenings', []):
    groups[li['file']] = ('listening', li['text'])

seen_pc = set()
for t in extract_phrases(preclass):
    if t not in seen_pc:
        seen_pc.add(t)
        groups.setdefault(f'pc14_{snake(t)}.mp3', ('preclass', t))

# detect collisions: two DIFFERENT texts -> same filename
file_to_texts = defaultdict(set)
# rebuild from scratch to catch within-group AND we must check 48-char prefix per prefix bucket
buckets = defaultdict(dict)  # prefix -> {snake48: text}
def check(prefix, text):
    key = snake(text)
    if key in buckets[prefix] and buckets[prefix][key] != text:
        return (prefix, key, buckets[prefix][key], text)
    buckets[prefix][key] = text
    return None

collisions = []
for t in slide_entries:
    c = check('a14_', t)
    if c: collisions.append(c)
for t in [li['text'] for li in cfg['lesson'].get('listenings', [])]:
    pass  # listenings have explicit unique filenames, skip
for t in sorted(seen_pc):
    c = check('pc14_', t)
    if c: collisions.append(c)

# also: a slide phrase and a preclass phrase could share text but different prefix -> different file, OK.
total = len(slide_entries) + len(cfg['lesson'].get('listenings', [])) + len(seen_pc)
print(f'distinct: slides={len(slide_entries)} listenings={len(cfg["lesson"].get("listenings",[]))} preclass={len(seen_pc)} total={total}')
if collisions:
    print('COLLISIONS FOUND:')
    for prefix, key, a, b in collisions:
        print(f'  [{prefix}{key}]  A="{a}"  B="{b}"')
    sys.exit(1)
print('OK: no snake[:48] collisions within any prefix bucket.')
