#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build standalone Aula 5 (Aline Sberci) — Have You Ever...? Travel Stories.
NOTA: a Aula 4 gerada ("Looking Ahead") cobriu o tema da linha 5 do currículo
(going to/will); esta Aula 5 cobre a linha 4 ("Have You Ever...? — Travel
Stories", present perfect ever/never) — troca de ordem, zero repetição (REGRA 22).
Scaffold = a PRÓPRIA aula 4 da Aline (marcadores Elaine, EXIT pós-#79).
A aula 4 dela só tem stamps 1-3: o build acrescenta stamp4 (earned) + stamp5.
Outputs: public/{professor,aluno}/aline-sberci-aula5.html + phrases.json."""
import os, re, json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SLUG = 'aline-sberci'
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
  'listening5_daniel': ('a5_listening_daniel.mp3', 'arthur',
    "Hi Aline, it is Daniel. Big news: I am going to Barcelona next month, for the global "
    "offsite! It is my first trip abroad — I have never traveled to another country, and I am "
    "a little nervous. You have traveled a lot, right? Can we have lunch this week? I want to "
    "hear your travel stories. Thank you!"),
  'listening5_carla': ('a5_listening_carla.mp3', 'ellen',
    "Have I ever been abroad? Yes, I have — I have visited Argentina and Mexico. Have I ever "
    "traveled alone? No, I have never traveled alone, always with family or friends. Have I "
    "ever tried a foreign food and loved it? Yes! Mexican tacos, amazing. Have I ever visited "
    "a famous landmark? Yes, the pyramids near Mexico City. And my most memorable trip? Mexico "
    "City, for sure — the culture and the food. I will never forget it."),
  '[order-l5]': ('a5_order_sequence.mp3', 'arthur',
    "Daniel says he is going to Barcelona. He asks: have you ever been to Spain? Aline answers: "
    "she has visited Portugal. She tells the story of her most memorable trip. Daniel feels "
    "ready for his first adventure."),
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
toggle = ['ellen', 'arthur']; ti = 0   # aluna mulher: começa em Ellen
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
SCENARIO FIT - Aula 5 (Have You Ever...? - Travel Stories)
Can-do: "I can ask and answer about life experiences with the present perfect (ever/never), and switch to past simple for specific times."
Gramatica-alvo: present perfect ever/never (have/has + participio); follow-up no past simple (When did you...?).
Vocab-alvo: abroad, adventure, sightseeing, culture, foreign, memorable, destination, landmark.
Cenario escolhido: lunch break na Novartis; Daniel vai para o offsite global em Barcelona (primeira viagem ao exterior dele) e pede as historias de viagem da Aline.
Por que elicita o alvo: trocar historias de viagem OBRIGA "Have you ever...?" / "I have never..." + follow-ups com when did. >70% dos itens-alvo elicitados.
NOTA DE CURRICULO: a Aula 4 gerada ("Looking Ahead") cobriu going to/will (linha 5 do curriculo); esta aula cobre a linha 4 (present perfect) — ordem trocada, cobertura intacta, zero repeticao (REGRA 22).

CONTINUIDADE - Aula 5
Itens novos: abroad, adventure, sightseeing, culture, foreign, memorable, destination, landmark; present perfect ever/never.
Itens revisados (Aula 4, going to/will): "We are going to start Project Aurora next month."; "I will lead the planning meetings."
Callback no warm-up (slide 2): retoma ATIVAMENTE 2 frases de planos da Aula 4 e faz a ponte planos (futuro) -> experiencias (vida toda).
-->'''

MENU = ('  <h3 style="font-family:\'Cormorant Garamond\',serif;font-size:1.3rem;margin-bottom:1rem">IN CLASS &mdash; Aula 5</h3>\n'
        '  <div style="display:flex;flex-direction:column;gap:1rem">\n'
        '    <div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" onclick="startLesson(1,28)" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
        '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">05</div>\n'
        '      <div><div style="font-weight:600;font-size:.95rem">Have You Ever...? &mdash; Travel Stories</div><div style="font-size:.8rem;color:var(--text-dim)">Present perfect: ever / never &mdash; 28 slides</div></div>\n'
        '    </div>\n  </div>\n')

STAMP45 = ('\n        <div class="stamp earned" id="stamp4" data-label="Plans" style="background-image:url(\'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=200&q=80\')"></div>'
           '\n        <div class="stamp" id="stamp5" data-label="Travel" style="background-image:url(\'https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?w=200&q=80\')"></div>')

def replace_between(s, start, end, new_inner):
    i = s.index(start); j = s.index(end, i + len(start))
    return s[:i] + start + '\n' + new_inner + '\n' + end + s[j + len(end):]

def build(scaffold, is_aluno):
    h = scaffold
    h = replace_between(h, '<body>', '<!-- LOGO BAR -->', AUDIT + '\n\n')
    h = h.replace('Aula 4 | Looking Ahead', 'Aula 5 | Have You Ever? Travel Stories')
    h = h.replace(SLUG + '-aula4', SLUG + '-aula5')
    m = re.search(r'<div class="stamp[^"]*" id="stamp3"[^>]*></div>', h)
    assert m, 'stamp3 nao encontrado'
    h = h.replace(m.group(0), m.group(0) + STAMP45)
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
assert prof.count('<div') == prof.count('</div>'), 'div imbalance prof: %d vs %d' % (prof.count('<div'), prof.count('</div>'))
assert aluno.count('<div') == aluno.count('</div>'), 'div imbalance aluno'
with open(PROF_OUT, 'w', encoding='utf-8') as f: f.write(prof)
with open(ALUNO_OUT, 'w', encoding='utf-8') as f: f.write(aluno)
print('OK aula5 built; audioMap keys=%d, phrases=%d, slides=%d' % (len(audio_map), len(phrases), N))
