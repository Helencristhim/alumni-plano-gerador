#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build standalone Aula 5 (Karina Macedo) — Review + Confidence Check: Lessons 1-4.
Scaffold = a PRÓPRIA aula 4 da Karina (identidade, accent terracota e navbar com EXIT
já corretos), trocando: audit, título, audioMap, stamps, as 4 abas e os slides.
Audio strings são EXTRAÍDAS do HTML autoral (audioMap nunca perde frase); arquivos
novos ganham prefixo a5_ (namespace, igual a4_).
Outputs: public/{professor,aluno}/karina-macedo-aula5.html + phrases.json."""
import os, re, json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
PROF_SCAFFOLD  = os.path.join(ROOT, 'public', 'professor', 'karina-macedo-aula4.html')
ALUNO_SCAFFOLD = os.path.join(ROOT, 'public', 'aluno', 'karina-macedo-aula4.html')
PROF_OUT  = os.path.join(ROOT, 'public', 'professor', 'karina-macedo-aula5.html')
ALUNO_OUT = os.path.join(ROOT, 'public', 'aluno', 'karina-macedo-aula5.html')
SLUG = 'karina-macedo'

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()

slides   = read(os.path.join(HERE, 'slides.html'))
preclass = read(os.path.join(HERE, 'preclass.html'))
compl    = read(os.path.join(HERE, 'complementary.html'))
N = len(re.findall(r'data-slide="\d+"', slides)); assert N == 28, 'expected 28 slides, got %d' % N

# ---------- AUDIO: long-form keys (narração completa -> MP3 único) ----------
SPECIAL = {
  'listening5_message': ('a5_listening_message.mp3', 'arthur',
    "Hello Karina, this is David Miller, from Maple Air. Thank you for the invitation. "
    "I am at the hotel now. I arrive at your office at ten o'clock. I want to see your "
    "company and talk about the prices. See you soon!"),
  'listening5_presentation': ('a5_listening_presentation.mp3', 'ellen',
    "Good morning, and welcome! My name is Laura Costa. I am from Rio de Janeiro, Brazil. "
    "I am a businesswoman in aviation, and I have ten years of experience. My company buys "
    "and sells aircraft. We have partners in many countries. We offer excellent service, "
    "and we deliver worldwide. Thank you for your visit!"),
  '[order-l5]': ('a5_order_sequence.mp3', 'arthur',
    "David arrives at the AeroBras office. Karina welcomes him and introduces her colleague. "
    "She presents the company. David asks about prices. They plan the next meeting."),
}

def slugify(text):
    s = re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")
    return 'a5_' + (s[:55].rstrip("_")) + ".mp3"

# Voz por fala de diálogo: frase -> data-voice da mesma linha
dialogue_voice = {}
for line in slides.splitlines():
    if 'data-voice="' in line and "speakText('" in line:
        v = re.search(r'data-voice="([^"]+)"', line)
        t = re.search(r"speakText\('((?:[^'\\]|\\.)*)'", line)
        if v and t:
            dialogue_voice[t.group(1).replace("\\'", "'")] = v.group(1)

# Coleta todas as strings de áudio em ordem (preclass primeiro, depois slides)
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

audio_map = {}   # chave speakText -> /audio/karina-macedo/arquivo.mp3
phrases = []     # {text, file, voice} para o gerador de áudio
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
        voice = 'arthur'                       # palavras soltas: sempre Arthur (REGRA 7)
    else:
        voice = toggle[ti % 2]; ti += 1        # frases: alterna Ellen/Arthur
    phrases.append({'text': t, 'file': fname, 'voice': voice})

AUDIOMAP = 'var audioMap = {\n' + ',\n'.join(
    '  %s: %s' % (json.dumps(k, ensure_ascii=False), json.dumps(v, ensure_ascii=False))
    for k, v in audio_map.items()) + '\n}'

with open(os.path.join(HERE, 'phrases.json'), 'w', encoding='utf-8') as f:
    json.dump(phrases, f, ensure_ascii=False, indent=2)

# ---------- blocos de conteúdo ----------
AUDIT = '''<!--
SCENARIO FIT - Aula 5 (Review + Confidence Check)
Can-do: "I can welcome a visitor, present myself and my company, and answer price questions - a 2-minute pitch in English."
Estruturas-alvo (TODAS revisão, Aulas 1-4): to be / I work / I have N years of experience; How much does it cost? / It costs...; We have / We offer / We deliver; Where are you from? / What do you do? / Who do you work for? / This is my colleague...
Vocab-alvo (revisão): company, price, experience, colleague, business card, offer.
Cenario escolhido: David (o comprador canadense da feira, Aula 4) visita o escritório da AeroBras; Karina recebe, apresenta a empresa e fecha com o pitch "Who Is Karina?" de 2 minutos (atividade-objetivo do currículo).
Por que elicita o alvo: receber visita de cliente OBRIGA boas-vindas (A4), apresentação pessoal (A1), apresentação da empresa (A3) e preços (A2). 100% revisão, zero conteúdo novo (REGRA 22).

CONTINUIDADE - Aula 5
Itens novos: NENHUM (aula de revisão por design do currículo).
Itens revisados: todos os itens-chave das Aulas 1-4.
Callback no warm-up (slide 2): retoma ATIVAMENTE 2 frases da Aula 4 ("Nice to meet you. Here is my business card." / "I work for AeroBras.") e faz a ponte feira -> visita ao escritório.
-->'''

MENU = ('  <h3 style="font-family:\'Cormorant Garamond\',serif;font-size:1.3rem;margin-bottom:1rem">IN CLASS &mdash; Aula 5</h3>\n'
        '  <div style="display:flex;flex-direction:column;gap:1rem">\n'
        '    <div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" onclick="startLesson(1,28)" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
        '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">05</div>\n'
        '      <div><div style="font-weight:600;font-size:.95rem">Review + Confidence Check</div><div style="font-size:.8rem;color:var(--text-dim)">Lessons 1-4 + the 2-minute pitch &mdash; 28 slides</div></div>\n'
        '    </div>\n  </div>\n')

STAMP5 = '\n        <div class="stamp" id="stamp5" data-label="Pitch" style="background-image:url(\'https://images.unsplash.com/photo-1521737711867-e3b97375f902?w=200&q=80\')"></div>'

# ---------- splice helpers ----------
def replace_between(s, start, end, new_inner):
    i = s.index(start); j = s.index(end, i + len(start))
    return s[:i] + start + '\n' + new_inner + '\n' + end + s[j + len(end):]

def build(scaffold, is_aluno):
    h = scaffold
    # audit (entre <body> e o LOGO BAR)
    h = replace_between(h, '<body>', '<!-- LOGO BAR -->', AUDIT + '\n\n')
    # título e número da aula
    h = h.replace('Aula 4 | At the Aviation Fair: Meeting People',
                  'Aula 5 | Review + Confidence Check: Lessons 1-4')
    h = h.replace('karina-macedo-aula4', 'karina-macedo-aula5')
    # stamps: stamp4 vira earned + entra stamp5
    m = re.search(r'<div class="stamp" id="stamp4"[^>]*></div>', h)
    assert m, 'stamp4 nao encontrado'
    earned4 = m.group(0).replace('class="stamp"', 'class="stamp earned"')
    h = h.replace(m.group(0), earned4 + STAMP5)
    # audioMap
    i = h.index('var audioMap = {'); j = h.index('};', i)
    h = h[:i] + AUDIOMAP + h[j+1:]
    # aba pre-class
    pre_start = '<div class="tab-content active" id="tab-exercises">' if 'active" id="tab-exercises"' in h else '<div class="tab-content" id="tab-exercises">'
    h = replace_between(h, pre_start, '</div><!-- /tab-exercises -->', preclass)
    # aba complementares
    h = replace_between(h, '<div class="tab-content" id="tab-complementary">', '</div><!-- /tab-complementary -->', compl)
    if not is_aluno:
        # menu IN CLASS (planning fica igual: mesma identidade/curriculo)
        h = replace_between(h, '<div class="tab-content" id="tab-inclass">', '<!-- ========== TAB 4: COMPLEMENTARES ========== -->', MENU + '</div>\n\n')
        # slides
        h = replace_between(h, '<div class="slides-container" id="slidesContainer">', '</div><!-- /slides-container -->', slides)
        # navbar label
        h = h.replace('LESSON 4', 'LESSON 5')
    return h

prof = build(read(PROF_SCAFFOLD), False)
aluno = build(read(ALUNO_SCAFFOLD), True)
assert 'data-lesson="4"' not in prof, 'sobrou slide da aula 4 no professor'
with open(PROF_OUT, 'w', encoding='utf-8') as f: f.write(prof)
with open(ALUNO_OUT, 'w', encoding='utf-8') as f: f.write(aluno)
print('OK aula5 built; audioMap keys=%d, phrases to generate=%d, slides=%d' % (len(audio_map), len(phrases), N))
