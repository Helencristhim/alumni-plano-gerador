#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract every speakText()/data-phrase audio call from slides.html + preclass.html,
map reused texts to the EXISTING hub audioMap files (REGRA C9 — never regenerate),
assign new aula5_ files + voices to the rest, and emit phrases.json.
Listening MP3s (data-src) are added explicitly. Voice: dialogue from data-voice; else arthur (Eduardo=male)."""
import os, re, json, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
WT   = os.path.dirname(os.path.dirname(HERE))            # wt-eduardo/
HUB  = os.path.join(WT, 'public', 'professor', 'eduardo-chiba.html')
SLUG = 'eduardo-chiba'

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()

slides   = read(os.path.join(HERE, 'slides.html'))
preclass = read(os.path.join(HERE, 'preclass.html'))
hub      = read(HUB)

# ---- existing hub audioMap: text -> /audio/eduardo-chiba/file.mp3 ----
blk = hub[hub.index('audioMap'):hub.index('};', hub.index('audioMap'))]
existing = {}
for k, v in re.findall(r'"((?:[^"\\]|\\.)*)":\s*"(/audio/%s/[^"]+\.mp3)"' % re.escape(SLUG), blk):
    existing[k.replace('\\"', '"')] = v

# ---- detect dialogue voices: map speakText text inside a dialogue-line -> data-voice ----
voice_of = {}
for line in re.findall(r'<div class="dialogue-line"[^>]*data-voice="([^"]+)"[^>]*>.*?</div>\s*</div>', slides, re.S):
    pass
for m in re.finditer(r'data-voice="([^"]+)"[^>]*>.*?speakText\(\'((?:[^\'\\]|\\.)*)\'', slides, re.S):
    v, t = m.group(1), m.group(2).replace("\\'", "'")
    voice_of[t] = v

# ---- collect all calls (order-preserving, unique) ----
calls = []
seen = set()
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
    return 'aula5_' + s[:42] + '_' + h + '.mp3'

phrases = []
reused = new = 0
for t in calls:
    if t in existing:
        f = os.path.basename(existing[t]); reused += 1; voice = 'arthur'
    else:
        f = slug_file(t); new += 1; voice = voice_of.get(t, 'arthur')
    phrases.append({'key': t, 'text': t, 'file': f, 'voice': voice})

# ---- listening MP3s (data-src, not in calls) — full pitch texts ----
listenings = [
    {'key': 'aula5_listening1_pitch', 'file': 'aula5_listening1_pitch.mp3', 'voice': 'arthur',
     'text': "Hi, I am Eduardo Chiba, Head of B2B at Quinto Andar. We connect real estate agencies to millions of renters through a digital marketplace. Our platform is faster and more scalable than traditional agencies. We have grown our partner network by forty percent this year, well above the industry benchmark. Could we schedule a call to discuss a partnership?"},
    {'key': 'aula5_listening2_partner', 'file': 'aula5_listening2_partner.mp3', 'voice': 'ellen',
     'text': "Hello, I am Sofia Marino, founder of RentEasy. We help small landlords fill empty apartments fast. Our competitive advantage is a lower commission and faster onboarding than big agencies. We have kept retention above ninety percent for two years. Could we set up a short meeting to explore a partnership?"},
]
phrases += listenings

with open(os.path.join(HERE, 'phrases.json'), 'w', encoding='utf-8') as f:
    json.dump(phrases, f, ensure_ascii=False, indent=2)

print('phrases.json: %d total (%d reused existing, %d new + %d listenings)' % (len(phrases), reused, new, len(listenings)))
print('voices used:', sorted(set(p['voice'] for p in phrases)))
new_files = [p['file'] for p in phrases if p['file'].startswith('aula5_')]
print('new files to generate:', len(new_files))
