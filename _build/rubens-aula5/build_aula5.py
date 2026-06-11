#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build standalone Aula 5 (Rubens Tofolo) — Describing People & Places.
Scaffold = a PRÓPRIA aula 4 do Rubens (marcadores Elaine, navbar com EXIT pós-#79),
trocando: audit, título, audioMap, stamps, abas e slides. Áudios novos com prefixo a5_.
Outputs: public/{professor,aluno}/rubens-tofolo-aula5.html + phrases.json."""
import os, re, json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SLUG = 'rubens-tofolo'
PROF_SCAFFOLD  = os.path.join(ROOT, 'public', 'professor', SLUG + '-aula4.html')
ALUNO_SCAFFOLD = os.path.join(ROOT, 'public', 'aluno', SLUG + '-aula4.html')
PROF_OUT  = os.path.join(ROOT, 'public', 'professor', SLUG + '-aula5.html')
ALUNO_OUT = os.path.join(ROOT, 'public', 'aluno', SLUG + '-aula5.html')

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()

slides   = read(os.path.join(HERE, 'slides.html'))
preclass = read(os.path.join(HERE, 'preclass.html'))
compl    = read(os.path.join(HERE, 'complementary.html'))
N = len(re.findall(r'data-slide="\d+"', slides)); assert N == 28, 'expected 28 slides, got %d' % N

SPECIAL = {
  'listening5_porto': ('a5_listening_porto.mp3', 'ellen',
    "Rubens, you make me curious about Brazil! Let me tell you about MY hometown, Porto. "
    "It is smaller than Lisbon, but for me it is more charming. The historic center is "
    "breathtaking, and the wine is the best in Portugal, of course! My favorite thing is "
    "the view of the river at sunset. Maybe one day you visit Porto, and I visit Belém!"),
  'listening5_belem': ('a5_listening_belem.mp3', 'arthur',
    "Welcome to Belém, the gateway to the Amazon! Our city is hot and humid, with rain "
    "almost every afternoon — but do not worry, it is short. This is the Ver-o-Peso, the "
    "biggest open-air market in Latin America: crowded, lively, and full of fruits you "
    "have never seen. The people here are among the most welcoming in Brazil. And tonight, "
    "do not miss the sunset over the river — it is simply breathtaking."),
  '[order-l5]': ('a5_order_sequence.mp3', 'arthur',
    "Sofia asks Rubens about his city. He describes the weather: hotter and more humid "
    "than Lisbon. He compares the prices: Belém is more affordable. He talks about the "
    "best things: the market and the sunset. Sofia decides she wants to visit Belém."),
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
phrases = []
toggle = ['arthur', 'ellen']; ti = 0   # aluno homem: começa em Arthur
for t in ordered:
    if t in SPECIAL:
        fname, voice, narration = SPECIAL[t]
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

AUDIT = '''<!--
SCENARIO FIT - Aula 5 (Describing People & Places)
Can-do: "I can describe my city and my people with adjectives, and compare two places with comparatives and superlatives."
Gramatica-alvo: comparativos (hotter than, more lively than, better than) e superlativos (the biggest, the most welcoming, the best).
Vocab-alvo: crowded, humid, lively, charming, historic, affordable, welcoming, breathtaking.
Cenario escolhido: coffee break do congresso em Lisboa; Dr. Sofia descobre que Rubens é de Belém (a Torre de Belém!) e pede que ele descreva a cidade dele — o gancho perfeito do currículo ("Describe Belém to a foreigner").
Por que elicita o alvo: descrever e comparar Belém com Lisboa OBRIGA adjetivos + comparativos + superlativos. >70% dos itens-alvo elicitados.

CONTINUIDADE - Aula 5
Itens novos: crowded, humid, lively, charming, historic, affordable, welcoming, breathtaking; comparativos e superlativos.
Itens revisados (Aula 4, present perfect): "I have already visited the Belem Tower."; "It has been an unforgettable journey."
Callback no warm-up (slide 2): retoma ATIVAMENTE 2 frases da Aula 4 e faz a ponte Torre de Belém (Lisboa) -> Belém (PA).
-->'''

MENU = ('  <h3 style="font-family:\'Cormorant Garamond\',serif;font-size:1.3rem;margin-bottom:1rem">IN CLASS &mdash; Aula 5</h3>\n'
        '  <div style="display:flex;flex-direction:column;gap:1rem">\n'
        '    <div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" onclick="startLesson(1,28)" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
        '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">05</div>\n'
        '      <div><div style="font-weight:600;font-size:.95rem">Describing People &amp; Places</div><div style="font-size:.8rem;color:var(--text-dim)">Comparatives &amp; superlatives &mdash; 28 slides</div></div>\n'
        '    </div>\n  </div>\n')

STAMP5 = '\n        <div class="stamp" id="stamp5" data-label="Bel&eacute;m" style="background-image:url(\'https://images.unsplash.com/photo-1483729558449-99ef09a8c325?w=200&q=80\')"></div>'

def replace_between(s, start, end, new_inner):
    i = s.index(start); j = s.index(end, i + len(start))
    return s[:i] + start + '\n' + new_inner + '\n' + end + s[j + len(end):]

def build(scaffold, is_aluno):
    h = scaffold
    h = replace_between(h, '<body>', '<!-- LOGO BAR -->', AUDIT + '\n\n')
    h = h.replace('Aula 4 | Life Experiences', 'Aula 5 | Describing People & Places')
    m = re.search(r'<div class="stamp" id="stamp4"[^>]*></div>', h)
    assert m, 'stamp4 nao encontrado'
    earned4 = m.group(0).replace('class="stamp"', 'class="stamp earned"')
    h = h.replace(m.group(0), earned4 + STAMP5)
    i = h.index('var audioMap = {'); j = h.index('};', i)
    h = h[:i] + AUDIOMAP + h[j+1:]
    pre_start = '<div class="tab-content active" id="tab-exercises">' if 'active" id="tab-exercises"' in h else '<div class="tab-content" id="tab-exercises">'
    h = replace_between(h, pre_start, '</div><!-- /tab-exercises -->', preclass)
    h = replace_between(h, '<div class="tab-content" id="tab-complementary">', '</div><!-- /tab-complementary -->', compl)
    if not is_aluno:
        h = replace_between(h, '<div class="tab-content" id="tab-inclass">', '<!-- ========== TAB 4: COMPLEMENTARES ========== -->', MENU + '</div>\n\n')
        h = replace_between(h, '<div class="slides-container" id="slidesContainer">', '</div><!-- /slides-container -->', slides)
        h = h.replace('LESSON 4', 'LESSON 5')
    return h

prof = build(read(PROF_SCAFFOLD), False)
aluno = build(read(ALUNO_SCAFFOLD), True)
assert 'data-lesson="4"' not in prof, 'sobrou slide da aula 4 no professor'
assert prof.count('<div') == prof.count('</div>'), 'div imbalance prof'
assert aluno.count('<div') == aluno.count('</div>'), 'div imbalance aluno'
with open(PROF_OUT, 'w', encoding='utf-8') as f: f.write(prof)
with open(ALUNO_OUT, 'w', encoding='utf-8') as f: f.write(aluno)
print('OK aula5 built; audioMap keys=%d, phrases=%d, slides=%d' % (len(audio_map), len(phrases), N))
