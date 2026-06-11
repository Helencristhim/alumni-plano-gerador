#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build standalone Aula 5 (Gleice) — Block 1 Review: Confidence Check.
Scaffold = a PRÓPRIA aula 4 da Gleice (engine custom dela, navbar com EXIT pós-#79),
trocando: audit, título, audioMap, stamps, abas e slides. A estrutura dela NÃO tem os
marcadores Elaine (<!-- /tab-... -->); os splices usam as aberturas das abas seguintes
como âncora de fim. Áudios novos com prefixo aula5_ (convenção dela: aula2_/aula4_).
Outputs: public/{professor,aluno}/gleice-leonardo-rocha-de-souza-aula5.html + phrases.json."""
import os, re, json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
SLUG = 'gleice-leonardo-rocha-de-souza'
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
  'listening5_message': ('aula5_listening_message.mp3', 'arthur',
    "Hello Gleice, this is Marc, from Sanofi France. I visit the Santo André office on Monday. "
    "I want to meet you and your team, and learn about your projects. My day is free after ten "
    "o'clock. See you soon!"),
  'listening5_presentation': ('aula5_listening_presentation.mp3', 'ellen',
    "Good morning, everyone. My name is Ana. I am from São Paulo, Brazil. I work at a "
    "pharmaceutical company. I am a logistics manager. My team has eight people. I always start "
    "my day with a team meeting, and I usually have many calls in the afternoon. I love my job "
    "because I like to connect with people."),
  '[order-l5]': ('aula5_order_sequence.mp3', 'arthur',
    "Marc arrives at the Santo André office. Gleice welcomes him and introduces her team. "
    "She talks about her routine and her projects. Marc asks questions about the projects. "
    "They plan the next steps together."),
}

def slugify(text):
    s = re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")
    return 'aula5_' + (s[:52].rstrip("_")) + ".mp3"

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
toggle = ['ellen', 'arthur']; ti = 0
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
SCENARIO FIT - Aula 5 (Block 1 Review - Confidence Check)
Can-do: "I can host a visitor in English: welcome, introduce myself and my team, talk about my routine, and ask questions to connect."
Estruturas-alvo (TODAS revisão, Aulas 1-4): I am / I work at; she works / my team has (3a pessoa + possessivos); always/usually/never; What/Where + do + you...?
Vocab-alvo (revisão): department, role, project, performance, strategy, routine.
Cenario escolhido: Marc Dubois (Sanofi France) visita o escritório de Santo André para o kickoff do projeto de transformação; Gleice recebe e conduz a simulação integrada (atividade-objetivo do currículo).
Por que elicita o alvo: receber um visitante OBRIGA apresentação pessoal (A1), descrição do time (A2), rotina (A3) e perguntas (A4). 100% revisão, zero conteúdo novo (REGRA 22).

CONTINUIDADE - Aula 5
Itens novos: NENHUM (aula de revisão por design do currículo).
Itens revisados: todos os itens-chave das Aulas 1-4.
Callback no warm-up (slide 2): retoma ATIVAMENTE 2 frases da Aula 4 ("Can I ask you a question?" / "What projects do you work on?") e faz a ponte perguntas -> conversa completa.
-->'''

MENU = ('  <h3 style="font-family:\'Cormorant Garamond\',serif;font-size:1.3rem;margin-bottom:1rem">IN CLASS &mdash; Aula 5</h3>\n'
        '  <div style="display:flex;flex-direction:column;gap:1rem">\n'
        '    <div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" onclick="startLesson(1,28)" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
        '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">05</div>\n'
        '      <div><div style="font-weight:600;font-size:.95rem">Block 1 Review &mdash; Confidence Check</div><div style="font-size:.8rem;color:var(--text-dim)">Lessons 1-4 + the full simulation &mdash; 28 slides</div></div>\n'
        '    </div>\n  </div>\n')

STAMP5 = '\n        <div class="stamp" id="stamp5" data-label="Review" style="background-image:url(\'https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=200&q=80\')"></div>'

def replace_between(s, start, end, new_inner):
    i = s.index(start); j = s.index(end, i + len(start))
    return s[:i] + start + '\n' + new_inner + '\n' + end + s[j + len(end):]

def build(scaffold, is_aluno):
    h = scaffold
    h = replace_between(h, '<body>', '<div class="logo-bar"', AUDIT + '\n\n')
    h = h.replace('Aula 4 | Questions That Connect', 'Aula 5 | Block 1 Review: Confidence Check')
    h = h.replace(SLUG + '-aula4', SLUG + '-aula5')
    m = re.search(r'<div class="stamp" id="stamp4"[^>]*></div>', h)
    assert m, 'stamp4 nao encontrado'
    earned4 = m.group(0).replace('class="stamp"', 'class="stamp earned"')
    h = h.replace(m.group(0), earned4 + STAMP5)
    i = h.index('var audioMap = {'); j = h.index('};', i)
    h = h[:i] + AUDIOMAP + h[j+1:]
    if is_aluno:
        pre_start = '<div class="tab-content active" id="tab-exercises">'
        h = replace_between(h, pre_start, '<div class="tab-content" id="tab-complementary">', preclass + '</div>\n')
        h = replace_between(h, '<div class="tab-content" id="tab-complementary">', '</div><!-- /container -->', compl + '</div>\n')
    else:
        h = replace_between(h, '<div class="tab-content" id="tab-exercises">', '<div class="tab-content" id="tab-inclass">', preclass + '</div>\n')
        h = replace_between(h, '<div class="tab-content" id="tab-inclass">', '<div class="tab-content" id="tab-complementary">', MENU + '</div>\n')
        h = replace_between(h, '<div class="tab-content" id="tab-complementary">', '</div><!-- /container -->', compl + '</div>\n')
        # fim dos slides: preserva teacher-t (icone T); fecha slidesContainer + slides-wrapper
        h = replace_between(h, '<div class="slides-container" id="slidesContainer">', '<div class="teacher-t"', slides + '</div>\n</div>\n\n')
        h = h.replace('LESSON 4', 'LESSON 5')
        h = h.replace('dialogueLine >= 10', 'dialogueLine >= 12')  # dialogo da aula 5 tem 12 falas
    return h

prof = build(read(PROF_SCAFFOLD), False)
aluno = build(read(ALUNO_SCAFFOLD), True)
assert 'data-lesson="4"' not in prof, 'sobrou slide da aula 4 no professor'
assert prof.count('<div') == prof.count('</div>'), 'div imbalance no professor: %d vs %d' % (prof.count('<div'), prof.count('</div>'))
assert aluno.count('<div') == aluno.count('</div>'), 'div imbalance no aluno'
with open(PROF_OUT, 'w', encoding='utf-8') as f: f.write(prof)
with open(ALUNO_OUT, 'w', encoding='utf-8') as f: f.write(aluno)
print('OK aula5 built; audioMap keys=%d, phrases=%d, slides=%d' % (len(audio_map), len(phrases), N))
