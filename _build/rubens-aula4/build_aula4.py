#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build standalone Aula 4 (Rubens Tofolo) — Life Experiences (Present Perfect: ever/never/already/yet).
Splices authored content into the proven Elaine aula15 scaffold (CSS+JS verbatim), swapping the
student identity, accent palette, planning, header, audioMap, audit and all four tabs.
Audio strings are EXTRACTED from the authored HTML, so the audioMap can never miss a phrase.
Outputs: public/professor/rubens-tofolo-aula4.html + public/aluno/rubens-tofolo-aula4.html + phrases.json."""
import os, re, json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
PROF_SCAFFOLD  = os.path.join(ROOT, 'public', 'professor', 'elaine-mieko-pinho-aula15.html')
ALUNO_SCAFFOLD = os.path.join(ROOT, 'public', 'aluno', 'elaine-mieko-pinho-aula15.html')
PROF_OUT  = os.path.join(ROOT, 'public', 'professor', 'rubens-tofolo-aula4.html')
ALUNO_OUT = os.path.join(ROOT, 'public', 'aluno', 'rubens-tofolo-aula4.html')
SLUG = 'rubens-tofolo'

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()

slides   = read(os.path.join(HERE, 'slides.html'))
preclass = read(os.path.join(HERE, 'preclass.html'))
compl    = read(os.path.join(HERE, 'complementary.html'))
N = len(re.findall(r'data-slide="\d+"', slides)); assert N == 28, 'expected 28 slides, got %d' % N

# ---------- AUDIO: special long-form keys (full narration -> single MP3) ----------
SPECIAL = {
  'listening4_journey': ('listening4_journey.mp3', 'ellen',
    "Two years ago, I went on the most unforgettable journey of my life. My destination was New "
    "Zealand. I had never been so far from home. I explored green mountains and quiet beaches, and I "
    "tried the local cuisine every day. I have visited many countries, but I have never seen a place "
    "so beautiful. I still keep a small souvenir from that trip on my desk."),
  'listening4_conference': ('listening4_conference.mp3', 'arthur',
    "This is my first journey to Lisbon, and it has been wonderful. I have already registered at the "
    "congress and visited the Belem Tower. But I haven't explored the old town yet, and I haven't "
    "tried the famous Portuguese cuisine. Tomorrow I want to buy a souvenir for my family. It has "
    "been an unforgettable destination."),
  '[order-l4]': ('order_l4_sequence.mp3', 'arthur',
    "Rubens planned his itinerary. He traveled to his destination, Lisbon. He has already explored "
    "the old town. He has tried the local cuisine. He bought a souvenir to remember the journey."),
}

def slugify(text):
    s = re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")
    return (s[:60].rstrip("_")) + ".mp3"

# Extract dialogue voice map: phrase text -> voice (from data-voice on same dialogue-line)
dialogue_voice = {}
for line in slides.splitlines():
    if 'data-voice="' in line and "speakText('" in line:
        v = re.search(r'data-voice="([^"]+)"', line)
        t = re.search(r"speakText\('((?:[^'\\]|\\.)*)'", line)
        if v and t:
            dialogue_voice[t.group(1).replace("\\'", "'")] = v.group(1)

# Collect all audio strings in order of appearance (preclass first, then slides)
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

audio_map = {}   # speakText-arg/key -> /audio/rubens-tofolo/file.mp3
phrases = []     # {text, file, voice} for the audio generator
toggle = ['arthur', 'ellen']; ti = 0
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
        voice = 'arthur'                       # single words: student gender (male)
    else:
        voice = toggle[ti % 2]; ti += 1        # general sentences: alternate
    phrases.append({'text': t, 'file': fname, 'voice': voice})

AUDIOMAP = 'var audioMap = {\n' + ',\n'.join(
    '  %s: %s' % (json.dumps(k, ensure_ascii=False), json.dumps(v, ensure_ascii=False))
    for k, v in audio_map.items()) + '\n}'

with open(os.path.join(HERE, 'phrases.json'), 'w', encoding='utf-8') as f:
    json.dump(phrases, f, ensure_ascii=False, indent=2)

# ---------- content blocks ----------
AUDIT = '''<!--
SCENARIO FIT - Aula 4
Can-do: "I can talk about my life experiences: ask 'Have you ever...?' and say what I have already / never / not yet done."
Gramatica-alvo: present perfect com ever / never / already / yet (have/has + past participle).
Vocab-alvo: journey, destination, landmark, souvenir, cuisine, itinerary, explore, unforgettable.
Cenario escolhido: coffee break de um congresso medico internacional em Lisboa; Rubens conversa com a colega Dra. Sofia sobre lugares visitados, comida e o que ainda falta fazer.
Por que elicita o alvo: falar de experiencias de vida e do itinerario do congresso OBRIGA o uso de "Have you ever...?", already e yet. >70% dos itens-alvo elicitados.

CONTINUIDADE - Aula 4
Itens novos: journey, destination, landmark, souvenir, cuisine, itinerary, explore, unforgettable; present perfect com ever/never/already/yet.
Itens revisados (Aula 3, Past Simple): "Years ago, I lived in California."; "I studied endocrinology there."
Callback no warm-up (slide 2): retoma ATIVAMENTE 2 frases em past simple da Aula 3 (lived / studied) e faz a ponte: past simple = tempo terminado; present perfect = a vida inteira, sem tempo especifico ("Have you ever...?").
-->'''

PLANNING = read(os.path.join(HERE, 'planning.html'))

MENU = ('  <h3 style="font-family:\'Cormorant Garamond\',serif;font-size:1.3rem;margin-bottom:1rem">IN CLASS &mdash; Aula 4</h3>\n'
        '  <div style="display:flex;flex-direction:column;gap:1rem">\n'
        '    <div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" onclick="startLesson(1,28)" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
        '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">04</div>\n'
        '      <div><div style="font-weight:600;font-size:.95rem">Life Experiences</div><div style="font-size:.8rem;color:var(--text-dim)">Present perfect: ever, never, already, yet &mdash; 28 slides</div></div>\n'
        '    </div>\n  </div>\n')

STAMPS = ('<div class="stamps-row">\n'
  '<div class="stamp earned" id="stamp1" data-label="Who Is" style="background-image:url(\'https://images.unsplash.com/photo-1559839734-2b71ea197ec2?w=200&q=80\')"></div>\n'
  '<div class="stamp earned" id="stamp2" data-label="Routine" style="background-image:url(\'https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=200&q=80\')"></div>\n'
  '<div class="stamp earned" id="stamp3" data-label="Past" style="background-image:url(\'https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=200&q=80\')"></div>\n'
  '<div class="stamp" id="stamp4" data-label="Life" style="background-image:url(\'https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=200&q=80\')"></div>\n'
  '</div>')

# ---------- splice helpers ----------
def replace_between(s, start, end, new_inner):
    i = s.index(start); j = s.index(end, i + len(start))
    return s[:i] + start + '\n' + new_inner + '\n' + end + s[j + len(end):]

def soft(s, old, new):
    return s.replace(old, new)

def build(scaffold, is_aluno):
    h = scaffold
    # audit (after <body>)
    h = replace_between(h, '<body>', '<!-- LOGO BAR -->', AUDIT + '\n\n')
    # title
    h = soft(h, 'Aula 15 | Shopping: Stores | Travel English', 'Aula 4 | Life Experiences | English for Medicine')
    # student identity (name handled by global slug/name replace below)
    h = soft(h, 'Elaine Mieko Pinho', 'Rubens Tofolo')
    h = soft(h, 'elaine-mieko-pinho', 'rubens-tofolo')
    h = soft(h, 'window.TOTAL_AULAS=32', 'window.TOTAL_AULAS=144')
    # accent palette (Elaine roxo -> Rubens azul mineral)
    h = soft(h, '#5E4B6D', '#336B87')
    h = soft(h, '#C4A8D8', '#4A8EB0')
    h = soft(h, '#E0CFF0', '#8FC1D6')
    h = soft(h, '94,75,109', '51,107,135')
    h = soft(h, '196,168,216', '74,142,176')
    # header text
    h = soft(h, 'Travel English -- 32 Aulas', 'English for Medicine -- 20 Aulas')
    h = soft(h, 'De viajante insegura para viajante independente e confiante em 32 aulas',
                'De ingles travado para fluencia em congressos e atendimento internacional')
    h = soft(h, '<span>A2</span>', '<span>B1-</span>')
    h = soft(h, '<span>Indaiatuba, SP</span>', '<span>Belem, PA</span>')
    h = soft(h, '<span>Advogada / Administradora de Empresa</span>', '<span>Endocrinologista</span>')
    # stamps
    h = re.sub(r'<div class="stamps-row">.*?</div>\s*</div>', STAMPS, h, count=1, flags=re.S)
    # audioMap
    i = h.index('var audioMap = {'); j = h.index('}', h.index('};', i))  # end of object
    j = h.index('};', i)
    h = h[:i] + AUDIOMAP + h[j+1:]
    # tab: pre-class
    pre_start = '<div class="tab-content active" id="tab-exercises">' if 'active" id="tab-exercises"' in h else '<div class="tab-content" id="tab-exercises">'
    h = replace_between(h, pre_start, '</div><!-- /tab-exercises -->', preclass)
    # tab: complementary
    h = replace_between(h, '<div class="tab-content" id="tab-complementary">', '</div><!-- /tab-complementary -->', compl)
    if not is_aluno:
        # tab: planning
        h = replace_between(h, '<div class="tab-content active" id="tab-planning">', '</div><!-- /tab-planning -->', PLANNING)
        # tab: in-class menu
        h = replace_between(h, '<div class="tab-content" id="tab-inclass">', '<!-- ========== TAB 4: COMPLEMENTARES ========== -->', MENU + '</div>\n\n')
        # slides
        h = replace_between(h, '<div class="slides-container" id="slidesContainer">', '</div><!-- /slides-container -->', slides)
    return h

with open(PROF_OUT, 'w', encoding='utf-8') as f: f.write(build(read(PROF_SCAFFOLD), False))
with open(ALUNO_OUT, 'w', encoding='utf-8') as f: f.write(build(read(ALUNO_SCAFFOLD), True))
print('OK aula4 built; audioMap keys=%d, phrases to generate=%d, slides=%d' % (len(audio_map), len(phrases), N))
