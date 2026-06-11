#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build standalone Aula 5 (Dienane) — Numbers and Time (agendar reunião por telefone).
O padrão da Dienane: standalone SLIDES-ONLY (sem abas; ?autostart=1) + hub com
accordion Pre-class inline + card IN CLASS. Scaffold = a aula 4 dela (EXIT pós-#79).
Gera também phrases.json (prefixo a5_; listenings via data-src como SPECIAL).
Outputs: public/professor/dienane-brandao-de-mesquita-aula5.html (sem espelho aluno,
igual às aulas 2-4 dela — o aluno usa o hub)."""
import os, re, json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SLUG = 'dienane-brandao-de-mesquita'
SCAFFOLD = os.path.join(ROOT, 'public', 'professor', SLUG + '-aula4.html')
OUT = os.path.join(ROOT, 'public', 'professor', SLUG + '-aula5.html')

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()

slides = read(os.path.join(HERE, 'slides.html'))
preclass = read(os.path.join(HERE, 'preclass.html'))
N = len(re.findall(r'data-slide="\d+"', slides)); assert N == 28, 'expected 28 slides, got %d' % N

SPECIAL_FILES = [
  ('listening5_1_confirmation.mp3', 'ellen',
   "Good afternoon! This is Paula, from Doctor Silva's office. I am calling to confirm your "
   "appointment on Wednesday, at half past two. Please arrive ten minutes early. If you are "
   "not available, please call us back. Thank you, and see you on Wednesday at two thirty!"),
  ('listening5_2_schedule.mp3', 'ellen',
   "Let me tell you about my week. I start work at eight o'clock, every day. On Monday, my "
   "team meeting is at half past nine. On Tuesday and Wednesday, I am very busy all morning. "
   "On Thursday, I am available in the afternoon, after a quarter past two. And on Friday, "
   "I finish early — at four o'clock!"),
]
SPECIAL_KEYS = {
  '[order-l5]': ('a5_order_sequence.mp3', 'arthur',
   "Dienane calls the candidate. She asks if he is available this week. She checks her "
   "calendar and proposes Thursday. She says the time: half past nine. They confirm: "
   "Thursday at nine thirty."),
}

def slugify(text):
    s = re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")
    return 'a5_' + (s[:55].rstrip("_")) + ".mp3"

dialogue_voice = {}
for line in slides.splitlines():
    if 'data-voice="' in line and "speakText('" in line:
        v = re.search(r'data-voice="([^"]+)"', line)
        t = re.search(r"speakText\('((?:[^'\\]|\\.)*)'", line)
        if v and t:
            dialogue_voice[t.group(1).replace("\\'", "'")] = v.group(1)

seen, ordered = set(), []
for src in (preclass, slides):
    for m in re.finditer(r"speakText\('((?:[^'\\]|\\.)*)'", src):
        t = m.group(1).replace("\\'", "'")
        if t not in seen:
            seen.add(t); ordered.append(t)
    for m in re.finditer(r'data-phrase="([^"]+)"', src):
        t = m.group(1)
        if t not in seen:
            seen.add(t); ordered.append(t)

audio_map = {}
phrases = [{'text': t, 'file': f, 'voice': v} for (f, v, t) in SPECIAL_FILES]
toggle = ['ellen', 'arthur']; ti = 0
for t in ordered:
    if t in SPECIAL_KEYS:
        fname, voice, narration = SPECIAL_KEYS[t]
        audio_map[t] = '/audio/%s/%s' % (SLUG, fname)
        phrases.append({'text': narration, 'file': fname, 'voice': voice})
        continue
    fname = slugify(t)
    audio_map[t] = '/audio/%s/%s' % (SLUG, fname)
    if t in dialogue_voice:
        voice = dialogue_voice[t]
    elif len(t.split()) <= 2:
        voice = 'arthur'
    else:
        voice = toggle[ti % 2]; ti += 1
    phrases.append({'text': t, 'file': fname, 'voice': voice})

AUDIOMAP = 'var audioMap = {\n' + ',\n'.join(
    '  %s: %s' % (json.dumps(k, ensure_ascii=False), json.dumps(v, ensure_ascii=False))
    for k, v in audio_map.items()) + '\n}'

with open(os.path.join(HERE, 'phrases.json'), 'w', encoding='utf-8') as f:
    json.dump(phrases, f, ensure_ascii=False, indent=2)

def replace_between(s, start, end, new_inner):
    i = s.index(start); j = s.index(end, i + len(start))
    return s[:i] + start + '\n' + new_inner + '\n' + end + s[j + len(end):]

h = read(SCAFFOLD)
h = h.replace('Dienane Orders Breakfast &mdash; Lesson 4', 'Dienane Schedules a Meeting &mdash; Lesson 5')
h = h.replace('Dienane Orders Breakfast — Lesson 4', 'Dienane Schedules a Meeting — Lesson 5')
i = h.index('var audioMap = {'); j = h.index('};', i)
h = h[:i] + AUDIOMAP + h[j+1:]
h = replace_between(h, '<div class="slides-container" id="slidesContainer">', '</div><!-- /slides-container -->', slides)
h = h.replace('LESSON 4', 'LESSON 5')
assert h.count('<div') == h.count('</div>'), 'div imbalance: %d vs %d' % (h.count('<div'), h.count('</div>'))
with open(OUT, 'w', encoding='utf-8') as f: f.write(h)
print('OK aula5 built; audioMap keys=%d, phrases=%d, slides=%d' % (len(audio_map), len(phrases), N))
