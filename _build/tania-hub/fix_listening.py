#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix single-voice listenings in the Tânia inline hub (professor).
Aulas 1-7 play a single-voice MP3 (custom togglePlayer); aulas 2-7's listening_1==listening_2
(dup bug). Convert each to the SAME playListenSeq + data-lines mechanism already used by aulas
8-9, feeding that lesson's DIALOGUE lines (which already have distinct per-voice MP3s) — so the
listening replays the conversation with alternating voices, reusing existing audio (zero new MP3s).
Idempotent: after running there are no `listening-player` blocks, so re-running is a no-op.
"""
import os, re, json
F = os.path.join(os.path.dirname(__file__), '..', '..', 'public', 'professor', 'tania-rosa.html')
F = os.path.abspath(F)
h = open(F, encoding='utf-8').read()

if 'class="listening-player"' not in h:
    print('nothing to fix (no listening-player blocks)'); raise SystemExit

# 1) map lesson -> dialogue lines (audio-inline speakText texts of the dialogue slide)
dmap = {}
for m in re.finditer(r'<div class="slide[^"]*" data-slide="\d+" data-lesson="(\d+)"[^>]*>(.*?)(?=<div class="slide |<div class="teacher-t")', h, re.S):
    L = int(m.group(1)); seg = m.group(2)
    if 'class="dialogue-box"' in seg:
        lines = [t.replace("\\'", "'") for t in
                 re.findall(r"audio-inline\" onclick=\"speakText\('((?:[^'\\]|\\.)*)'", seg)]
        if lines:
            dmap[L] = lines
print('dialogue lines per lesson:', {k: len(v) for k, v in sorted(dmap.items())})

def waveform_player(dlines):
    dl = json.dumps(dlines, ensure_ascii=False).replace('"', '&quot;')
    bars = ''.join('<div class="bar"></div>' for _ in range(12))
    return ('<div class="waveform waveform-paused">' + bars + '</div>\n'
            '    <button class="play-btn" onclick="playListenSeq(this)" data-lines="' + dl + '">'
            '<svg class="icon-play" viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"/></svg>'
            '<svg class="icon-pause" viewBox="0 0 24 24" style="display:none"><rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/></svg>'
            '</button>')

# 2) replace each listening-player block using its slide's lesson
def repl(m):
    before = h[:m.start()]
    ls = re.findall(r'data-lesson="(\d+)"', before)
    L = int(ls[-1]) if ls else 1
    return waveform_player(dmap.get(L, dmap.get(1, [])))

h2, n = re.subn(r'<div class="listening-player"[^>]*>.*?</audio>', repl, h, flags=re.S)
print('listening blocks converted:', n)
assert 'class="listening-player"' not in h2, 'leftover listening-player'

# sanity: data-slide count unchanged, every data-lines line has an audioMap key
ds_before = len(re.findall(r'<div class="slide[^"]*" data-slide="\d+"', h))
ds_after  = len(re.findall(r'<div class="slide[^"]*" data-slide="\d+"', h2))
assert ds_before == ds_after, 'slide count changed %d->%d' % (ds_before, ds_after)
am = h2[h2.index('var audioMap = {'): h2.index('\n};', h2.index('var audioMap = {'))]
keys = set(k[1:-1] for k, _ in re.findall(r'\n\s*("(?:[^"\\]|\\.)*")\s*:\s*("(?:[^"\\]|\\.)*")', am))
missing = set()
for dl in re.findall(r'data-lines="([^"]*)"', h2):
    for s in json.loads(dl.replace('&quot;', '"')):
        if s not in keys: missing.add(s)
if missing:
    print('!!! data-lines phrases missing from audioMap:', len(missing))
    for x in list(missing)[:10]: print('   ', repr(x))
else:
    print('audio coverage OK — every listening line has an MP3 in audioMap')

open(F, 'w', encoding='utf-8').write(h2)
print('written:', F, '| playListenSeq total now:', h2.count('onclick="playListenSeq(this)"'),
      '| slides:', ds_after)
