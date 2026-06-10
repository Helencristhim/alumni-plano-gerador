#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Builder da AULA 8 da Daniela Feitoza — "Networking in Action: Keeping the Conversation Going".
Reaproveita CSS + JS da aula7 (REGRA 26/34), injeta conteudo novo. Gera prof + aluno + audio json.
Fonte unica de audio (AUDIO) garante audioMap == speakText == arquivos gerados."""
import os, re, json, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROF7 = os.path.join(ROOT, 'public', 'professor', 'daniela-feitoza-aula7.html')
ALU7  = os.path.join(ROOT, 'public', 'aluno', 'daniela-feitoza-aula7.html')
PROF8 = os.path.join(ROOT, 'public', 'professor', 'daniela-feitoza-aula8.html')
ALU8  = os.path.join(ROOT, 'public', 'aluno', 'daniela-feitoza-aula8.html')
AUDIODIR = '/audio/daniela-feitoza-aula8/'

def sanitize(text):
    t = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    t = t.lower()
    t = re.sub(r"[^a-z0-9]+", "_", t)
    t = re.sub(r"_+", "_", t).strip("_")
    return t[:60].strip("_")

# ============================================================ AUDIO (fonte unica)
# (key, text, voice, file_opcional). key == texto do speakText/data-phrase/audioMap.
ELLEN, RACHEL = 'ellen', 'rachel'
AUDIO = []
def add(text, voice, key=None, file=None):
    AUDIO.append({'key': key or text, 'text': text, 'voice': voice,
                  'file': file or (sanitize(text) + '.mp3')})

# 8 vocab novos (aluna = ellen)
for w in ["Follow-up","Curious","Interested","Nod","React","Detail","Mention","Topic"]:
    add(w, ELLEN)
# Callback Aula 7 (REGRA 37)
for w in ["Launch","Challenge","Result","Deadline"]:
    add(w, ELLEN)
# Dialogo (Sophie = rachel, Daniela = ellen) — sem apostrofos (convencao aula7)
DIALOGUE = [
 ("Sophie","Hi! I do not think we have met. I am Sophie, from the Berlin office.",RACHEL),
 ("Daniela","Nice to meet you, Sophie! I am Daniela, from Sao Paulo. So, what do you do in Berlin?",ELLEN),
 ("Sophie","I work in logistics. Last month, we opened a new distribution center.",RACHEL),
 ("Daniela","Oh, really? That is interesting! What kind of center is it?",ELLEN),
 ("Sophie","It is fully automated. It was a big challenge, but the result was great.",RACHEL),
 ("Daniela","Wow, that sounds great! How long did the project take?",ELLEN),
 ("Sophie","About eight months. Honestly, the deadline was very tight.",RACHEL),
 ("Daniela","I can imagine. You mentioned automation. Can you tell me one more detail?",ELLEN),
 ("Sophie","Sure! The robots move the boxes, so the team works faster now.",RACHEL),
 ("Daniela","That is amazing. I am really curious about this topic. Let us keep in touch!",ELLEN),
]
for sp, line, v in DIALOGUE:
    add(line, v)
# Listening 2 cues
for t in ["What kind of center is it?","How long did the project take?","Oh, really? That is interesting!",
          "Can you tell me one more detail?","I am really curious about this topic."]:
    add(t, ELLEN)
# Pronunciation (4)
for t in ["Oh, really? That sounds great!","What kind of project was it?","How long did it take?",
          "That is interesting. Tell me more about it."]:
    add(t, ELLEN)
# Fill-in-the-blank phrases
for t in ["What kind of work do you do?","Where exactly is your office?","Really? That sounds great!",
          "Can you tell me more about it?","You mentioned a new system."]:
    add(t, ELLEN)
# Survival (novo)
add("Wow, that sounds great! Tell me more.", ELLEN)
# Order sequence
ORDER_SEQ = "So, what do you do? Oh, really? What kind of company is it? That is interesting! How long did you work there? You mentioned a big project. Tell me more about it. Wow, that sounds great. Let us keep in touch!"
add(ORDER_SEQ, ELLEN, key="[order-l8]", file="order_l8_ordering.mp3")

# dedup por key, mantendo 1o
seen = {}
for a in AUDIO:
    if a['key'] not in seen:
        seen[a['key']] = a
AUDIO_U = list(seen.values())
# checar colisao de arquivo entre textos distintos
byfile = {}
for a in AUDIO_U:
    byfile.setdefault(a['file'], set()).add(a['text'])
for f, texts in byfile.items():
    assert len(texts) == 1, "COLISAO de arquivo %s -> %s" % (f, texts)

# audioMap JS
am_lines = []
for a in AUDIO_U:
    am_lines.append('  %s: "%s%s",' % (json.dumps(a['key']), AUDIODIR.lstrip('/'), a['file']) if False else
                    '  %s: "%s%s",' % (json.dumps(a['key']), AUDIODIR, a['file']))
AUDIOMAP_BLOCK = "var audioMap = {\n" + "\n".join(am_lines) + "\n};"

# audio json p/ o gerador
audio_json = [{'file': a['file'], 'text': a['text'], 'voice': a['voice']} for a in AUDIO_U]
with open(os.path.join(ROOT, 'scripts', 'daniela-aula8-audio.json'), 'w', encoding='utf-8') as f:
    json.dump(audio_json, f, ensure_ascii=False, indent=2)

# helper p/ Listen SVG
SPK = '<svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg>'

# ============================================================ PLANNING
PLANNING_INNER = '''
<!--
CONTINUIDADE — Aula 8 (REGRA 37)
Itens novos desta aula (8): follow-up, curious, interested, nod, react, detail, mention, topic
Itens revisados (de aulas anteriores): past simple + launch, challenge, result, deadline (Aula 7); workflow/implement/deploy (Aula 6)
Callback no warm-up (Slide 2 + Pre-class): retoma ATIVAMENTE o past simple e palavras da Aula 7 (launch, challenge, result) — agora Daniela faz PERGUNTAS de follow-up sobre a história de sucesso que ela contou na Aula 7 ("You said you launched a system — what kind of system? What was the biggest challenge?"). O aluno USA past-simple questions (Did you...?) e REAGE, conectando NARRAR (Aula 7) a MANTER A CONVERSA (Aula 8).
Função/gramática nova: follow-up question forms (What kind of...?, How long...?, Where exactly...?), echo/short questions (Oh, really?, Did you?), reactions (That is interesting!, Tell me more). NAO ensinadas como novas nas aulas 1-7.
-->
<!--
SCENARIO FIT — Aula 8 (REGRA 36)
Can-do: "I can keep a conversation going by asking follow-up questions and showing interest."
Gramatica-alvo: follow-up question forms (What kind of...? How long...? Where exactly...?), echo/short questions (Oh, really? Did you?), active-listening reactions (That is interesting! Tell me more.)
Vocab-alvo: follow-up, curious, interested, nod, react, detail, mention, topic
Cenario escolhido: coffee break em um evento de networking internacional — dois profissionais mantendo uma conversa viva.
Por que elicita o alvo: numa conversa de networking, manter o papo vivo OBRIGA o aluno a reagir, demonstrar interesse e fazer perguntas de follow-up. >=70% dos itens-alvo sao elicitados naturalmente pelo cenario.
-->

<div class="info-grid">
  <div class="info-item"><label>Nome</label><span>Daniela Feitoza</span></div>
  <div class="info-item"><label>Idade</label><span>44 anos</span></div>
  <div class="info-item"><label>Profissão</label><span>IT Manager — SPF Group (distribuidora Centauro/Nike), São Paulo</span></div>
  <div class="info-item"><label>Nível</label><span>A2+ (Pré-Intermediário)</span></div>
  <div class="info-item"><label>Foco</label><span>Conversational English para eventos internacionais e vagas internacionais</span></div>
  <div class="info-item"><label>Total de Aulas</label><span>43 aulas de 60 min</span></div>
  <div class="info-item"><label>Frequência</label><span>2x por semana — Online</span></div>
  <div class="info-item"><label>Aula</label><span>08 — Networking in Action: Keeping the Conversation Going</span></div>
</div>

<div class="journey-box">
  <h4>Jornada de Transformação</h4>
  <p><strong>De:</strong> Profissional que já consegue se apresentar e contar a própria história (Aulas 1–7), mas trava quando o OUTRO fala — não sabe reagir, demonstrar interesse nem puxar a conversa adiante, e o papo morre.</p>
  <p style="margin-top:.5rem"><strong>Para:</strong> Networker que mantém qualquer conversa viva: reage com naturalidade, demonstra interesse genuíno e faz perguntas de follow-up — a habilidade que transforma um "oi" num contato real em eventos internacionais.</p>
</div>

<div style="padding:1.2rem;background:rgba(13,115,119,.06);border:1px solid rgba(13,115,119,.15);border-radius:10px;margin-bottom:1.5rem">
  <h4 style="font-family:'Cormorant Garamond',serif;font-size:1.1rem;color:var(--accent);margin-bottom:.5rem">Promessa da Aula 08</h4>
  <p style="font-size:.9rem;line-height:1.7">After this lesson, Daniela will keep a networking conversation going — reacting, showing interest, and asking natural follow-up questions (What kind of...? How long...? Where exactly...?) so the other person wants to keep talking.</p>
</div>

<div class="sw-grid">
  <div class="sw-box strengths">
    <h4>Forças</h4>
    <ul>
      <li>Já se apresenta e conta a própria história com segurança (Aulas 1–7)</li>
      <li>Domina past simple — base para perguntas de follow-up (Did you...? How long...?)</li>
      <li>Motivação concreta — eventos e vagas internacionais</li>
      <li>Escuta atenta de gestora — bom ponto de partida para active listening</li>
    </ul>
  </div>
  <div class="sw-box weaknesses">
    <h4>Pontos de Melhoria</h4>
    <ul>
      <li>Conversas morrem — responde mas não devolve a pergunta</li>
      <li>Pouco repertório de reações ("Oh, really?", "That is interesting!")</li>
      <li>Confunde interested / interesting</li>
      <li>Medo de "puxar assunto" e parecer invasiva</li>
    </ul>
  </div>
</div>

<h3 style="font-family:'Cormorant Garamond',serif;font-size:1.3rem;margin-bottom:1rem">Currículo — Aulas 1 a 11 (de 43)</h3>
<div class="curriculum-wrapper">
  <table class="curriculum-table">
    <thead><tr><th>#</th><th>Tema</th><th>Foco Linguístico</th><th>Atividade Principal</th><th>Homework</th></tr></thead>
    <tbody>
      <tr><td>1</td><td>Who is Daniela? — Diagnostic + Personal Introduction</td><td>Present Simple (self-introduction)</td><td>Self-introduction role-play</td><td>Record 1-min self-introduction</td></tr>
      <tr><td>2</td><td>Breaking the Ice — First Contact at International Events</td><td>Small-talk openers, present simple questions</td><td>Networking role-play</td><td>Listen to a networking podcast</td></tr>
      <tr><td>3</td><td>Talking About Your Job — IT Manager at Centauro/Nike</td><td>Present simple for job descriptions</td><td>Job-pitch role-play</td><td>Write your job pitch</td></tr>
      <tr><td>4</td><td>Articles and English Rhythm</td><td>Articles (a/an/the), stress &amp; rhythm</td><td>Pronunciation drilling</td><td>Shadow a short audio</td></tr>
      <tr><td>5</td><td>Describing Your Company — Centauro, Nike Brazil &amp; SPF Group</td><td>Superlatives (the largest, the most...)</td><td>Company description</td><td>Write 5 company sentences</td></tr>
      <tr><td>6</td><td>SAP World — Talking About Systems and Technology</td><td>Present simple for processes/systems</td><td>Explain SAP workflow to a colleague</td><td>Glossary of 10 SAP terms</td></tr>
      <tr><td>7</td><td>Past Simple: Telling Stories That Connect</td><td>Past simple (regular/irregular), time markers, narrative structure</td><td>Tell a professional success story using past simple</td><td>Write a story about a project you completed + audio</td></tr>
      <tr style="background:rgba(13,115,119,.08)"><td><strong>8</strong></td><td><strong>Networking in Action — Keeping the Conversation Going</strong></td><td><strong>Follow-up questions, active listening, showing interest (reactions &amp; echo questions)</strong></td><td><strong>Networking role-play: keep a conversation alive with reactions + follow-ups</strong></td><td><strong>Record a 1-min networking chat + write 5 follow-up questions</strong></td></tr>
      <tr><td>9</td><td>Asking and Answering Questions at Events</td><td>Question forms (Wh- / yes-no), follow-ups</td><td>Q&amp;A networking simulation</td><td>Prepare 10 questions for an event</td></tr>
      <tr><td>10</td><td>Talking About Plans and the Future</td><td>Going to / will for plans and predictions</td><td>Project-roadmap conversation</td><td>Write your goals for the year</td></tr>
      <tr><td>11</td><td>Present Perfect vs. Past Simple</td><td>Present perfect for experience/results vs past simple</td><td>Interview about professional achievements</td><td>Write 10 sentences: 5 present perfect, 5 past simple + audio</td></tr>
    </tbody>
  </table>
  <p style="font-size:.75rem;color:var(--text-dim);padding:.6rem 1rem;font-style:italic">Trecho do currículo (Aulas 1–11 de 43). Aulas 12–43 seguem no arquivo principal do aluno.</p>
</div>
'''

# ============================================================ PRE-CLASS (inner)
PRECLASS_INNER = '''<div class="lesson-card open" id="ex-lesson-8">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1543269865-cbf427effbad?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Aula 08 — Pre-class</div>
      <h3>Networking in Action: Keeping the Conversation Going</h3>
      <div class="lesson-desc">React, show interest, and ask follow-up questions</div>
      <div class="lesson-progress-mini">
        <div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="1" style="width:0%"></div></div>
        <span class="mini-percent" data-lesson-pct="1">0%</span>
      </div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div style="padding:1rem;background:rgba(13,115,119,.06);border:1px solid rgba(13,115,119,.15);border-radius:10px;margin-bottom:1.5rem">
      <p style="font-size:.9rem;line-height:1.7"><strong>Objetivo desta aula:</strong> Ao final, Daniela será capaz de manter uma conversa de networking viva — reagindo com naturalidade, demonstrando interesse e fazendo perguntas de follow-up (What kind of...? How long...? Where exactly...?) para que a outra pessoa queira continuar falando.</p>
    </div>

    <!-- WARM-UP CALLBACK (REGRA 37) -->
    <div class="exercise-section" style="border-left:3px solid var(--accent)">
      <div class="section-header-row"><h4>Warm-up — From Lesson 7</h4><span class="badge badge-speak">Callback</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:1rem;font-style:italic">Last class you told a success story in the past. Now imagine a colleague tells YOU that same story. Use these Lesson 7 words to ask <strong>follow-up questions</strong> in the past. Tap Listen to review.</p>
      <div style="display:flex;flex-direction:column;gap:.6rem">
        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header"><span class="vocab-card-word">launch</span><span class="vocab-card-dot">·</span><span class="vocab-card-def">to start something new (Lesson 7)</span></div><div class="vocab-card-example">Follow-up: "You said you launched a system — what kind of system was it?"</div></div><button class="audio-btn" onclick="speakText('Launch',this)" aria-label="Ouvir launch">&#9654; Listen</button></div>
        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header"><span class="vocab-card-word">challenge</span><span class="vocab-card-dot">·</span><span class="vocab-card-def">a difficult task (Lesson 7)</span></div><div class="vocab-card-example">Follow-up: "What was the biggest challenge? How did you solve it?"</div></div><button class="audio-btn" onclick="speakText('Challenge',this)" aria-label="Ouvir challenge">&#9654; Listen</button></div>
        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header"><span class="vocab-card-word">result</span><span class="vocab-card-dot">·</span><span class="vocab-card-def">the outcome (Lesson 7)</span></div><div class="vocab-card-example">Follow-up: "Oh, really? And what was the result?"</div></div><button class="audio-btn" onclick="speakText('Result',this)" aria-label="Ouvir result">&#9654; Listen</button></div>
      </div>
    </div>

    <!-- STAGE 1.1: VOCAB CARDS -->
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:1rem;font-style:italic">These are the key words for keeping a conversation alive. Tap Listen to hear the pronunciation.</p>
      <div class="vocab-cards">
        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header"><span class="vocab-card-word">Follow-up</span><span class="vocab-card-dot">·</span><span class="vocab-card-def">a question that asks for more information about what someone said</span></div><div class="vocab-card-example">"Can I ask a follow-up question?"</div></div><button class="audio-btn" onclick="speakText('Follow-up',this)" aria-label="Ouvir Follow-up">&#9654; Listen</button></div>
        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header"><span class="vocab-card-word">Curious</span><span class="vocab-card-dot">·</span><span class="vocab-card-def">wanting to know more about something</span></div><div class="vocab-card-example">"I am curious about your job."</div></div><button class="audio-btn" onclick="speakText('Curious',this)" aria-label="Ouvir Curious">&#9654; Listen</button></div>
        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header"><span class="vocab-card-word">Interested</span><span class="vocab-card-dot">·</span><span class="vocab-card-def">giving attention because you want to know more</span></div><div class="vocab-card-example">"She looked really interested in my story."</div></div><button class="audio-btn" onclick="speakText('Interested',this)" aria-label="Ouvir Interested">&#9654; Listen</button></div>
        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header"><span class="vocab-card-word">Nod</span><span class="vocab-card-dot">·</span><span class="vocab-card-def">to move your head up and down to show you are listening</span></div><div class="vocab-card-example">"People nod to show they are listening."</div></div><button class="audio-btn" onclick="speakText('Nod',this)" aria-label="Ouvir Nod">&#9654; Listen</button></div>
        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header"><span class="vocab-card-word">React</span><span class="vocab-card-dot">·</span><span class="vocab-card-def">to show your feelings about what someone says</span></div><div class="vocab-card-example">"It is polite to react with a smile."</div></div><button class="audio-btn" onclick="speakText('React',this)" aria-label="Ouvir React">&#9654; Listen</button></div>
        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header"><span class="vocab-card-word">Detail</span><span class="vocab-card-dot">·</span><span class="vocab-card-def">a small piece of information</span></div><div class="vocab-card-example">"Tell me one more detail."</div></div><button class="audio-btn" onclick="speakText('Detail',this)" aria-label="Ouvir Detail">&#9654; Listen</button></div>
        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header"><span class="vocab-card-word">Mention</span><span class="vocab-card-dot">·</span><span class="vocab-card-def">to say something briefly</span></div><div class="vocab-card-example">"You mentioned a new project."</div></div><button class="audio-btn" onclick="speakText('Mention',this)" aria-label="Ouvir Mention">&#9654; Listen</button></div>
        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header"><span class="vocab-card-word">Topic</span><span class="vocab-card-dot">·</span><span class="vocab-card-def">the subject of a conversation</span></div><div class="vocab-card-example">"Let us change the topic."</div></div><button class="audio-btn" onclick="speakText('Topic',this)" aria-label="Ouvir Topic">&#9654; Listen</button></div>
      </div>
      <button class="listen-all-btn" style="margin-top:1rem" onclick="listenAllVocab(this)">&#9654; Listen todas</button>
    </div>

    <!-- STAGE 1.2: MATCHING -->
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Match the Words</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:1rem;font-style:italic">Match each word with its definition.</p>
      <div class="match-grid" id="match-l8">
        <div class="match-row" data-answer="a question for more details"><span class="match-word">Follow-up</span><select onchange="checkMatch(this)"><option value="">Select...</option><option value="the subject of a conversation">the subject of a conversation</option><option value="a small piece of information">a small piece of information</option><option value="a question for more details">a question for more details</option><option value="wanting to know more">wanting to know more</option><option value="to show your feelings">to show your feelings</option><option value="head movement that shows listening">head movement that shows listening</option><option value="giving attention to know more">giving attention to know more</option><option value="to say something briefly">to say something briefly</option></select></div>
        <div class="match-row" data-answer="wanting to know more"><span class="match-word">Curious</span><select onchange="checkMatch(this)"><option value="">Select...</option><option value="to say something briefly">to say something briefly</option><option value="head movement that shows listening">head movement that shows listening</option><option value="wanting to know more">wanting to know more</option><option value="a question for more details">a question for more details</option><option value="the subject of a conversation">the subject of a conversation</option><option value="to show your feelings">to show your feelings</option><option value="a small piece of information">a small piece of information</option><option value="giving attention to know more">giving attention to know more</option></select></div>
        <div class="match-row" data-answer="giving attention to know more"><span class="match-word">Interested</span><select onchange="checkMatch(this)"><option value="">Select...</option><option value="a small piece of information">a small piece of information</option><option value="a question for more details">a question for more details</option><option value="giving attention to know more">giving attention to know more</option><option value="to show your feelings">to show your feelings</option><option value="the subject of a conversation">the subject of a conversation</option><option value="to say something briefly">to say something briefly</option><option value="wanting to know more">wanting to know more</option><option value="head movement that shows listening">head movement that shows listening</option></select></div>
        <div class="match-row" data-answer="head movement that shows listening"><span class="match-word">Nod</span><select onchange="checkMatch(this)"><option value="">Select...</option><option value="wanting to know more">wanting to know more</option><option value="the subject of a conversation">the subject of a conversation</option><option value="head movement that shows listening">head movement that shows listening</option><option value="a small piece of information">a small piece of information</option><option value="giving attention to know more">giving attention to know more</option><option value="a question for more details">a question for more details</option><option value="to say something briefly">to say something briefly</option><option value="to show your feelings">to show your feelings</option></select></div>
        <div class="match-row" data-answer="to show your feelings"><span class="match-word">React</span><select onchange="checkMatch(this)"><option value="">Select...</option><option value="giving attention to know more">giving attention to know more</option><option value="to say something briefly">to say something briefly</option><option value="to show your feelings">to show your feelings</option><option value="head movement that shows listening">head movement that shows listening</option><option value="a question for more details">a question for more details</option><option value="the subject of a conversation">the subject of a conversation</option><option value="wanting to know more">wanting to know more</option><option value="a small piece of information">a small piece of information</option></select></div>
        <div class="match-row" data-answer="a small piece of information"><span class="match-word">Detail</span><select onchange="checkMatch(this)"><option value="">Select...</option><option value="head movement that shows listening">head movement that shows listening</option><option value="wanting to know more">wanting to know more</option><option value="a small piece of information">a small piece of information</option><option value="to show your feelings">to show your feelings</option><option value="to say something briefly">to say something briefly</option><option value="a question for more details">a question for more details</option><option value="the subject of a conversation">the subject of a conversation</option><option value="giving attention to know more">giving attention to know more</option></select></div>
        <div class="match-row" data-answer="to say something briefly"><span class="match-word">Mention</span><select onchange="checkMatch(this)"><option value="">Select...</option><option value="the subject of a conversation">the subject of a conversation</option><option value="giving attention to know more">giving attention to know more</option><option value="to say something briefly">to say something briefly</option><option value="a question for more details">a question for more details</option><option value="head movement that shows listening">head movement that shows listening</option><option value="to show your feelings">to show your feelings</option><option value="wanting to know more">wanting to know more</option><option value="a small piece of information">a small piece of information</option></select></div>
        <div class="match-row" data-answer="the subject of a conversation"><span class="match-word">Topic</span><select onchange="checkMatch(this)"><option value="">Select...</option><option value="to show your feelings">to show your feelings</option><option value="a small piece of information">a small piece of information</option><option value="the subject of a conversation">the subject of a conversation</option><option value="head movement that shows listening">head movement that shows listening</option><option value="a question for more details">a question for more details</option><option value="wanting to know more">wanting to know more</option><option value="to say something briefly">to say something briefly</option><option value="giving attention to know more">giving attention to know more</option></select></div>
      </div>
      <button class="verify-all-btn" onclick="verifyAllMatches('match-l8')">Verificar Tudo</button>
    </div>

    <!-- STAGE 1.3: GRAMMAR IN CONTEXT -->
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-grammar">Grammar</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:1rem;font-style:italic">Read the short text and answer the questions. Notice the <strong>follow-up questions</strong> and <strong>reactions</strong> in bold.</p>
      <div style="padding:1rem;background:rgba(255,255,255,.6);border:1px solid rgba(200,200,190,.5);border-radius:10px;font-size:.92rem;line-height:1.8;margin-bottom:1rem">
        <p>At the coffee break, Daniela met a new contact. She was <strong>curious</strong> about his work, so she asked a <strong>follow-up</strong> question: <strong>"What kind of projects do you do?"</strong> He <strong>mentioned</strong> a big launch in Berlin. Daniela <strong>nodded</strong> and said, <strong>"Oh, really? That is interesting!"</strong> She did not change the <strong>topic</strong> too fast. She listened, asked for one more <strong>detail</strong>, and <strong>reacted</strong> with a smile. Because she looked <strong>interested</strong>, the conversation kept going.</p>
      </div>
      <div class="quiz-item">
        <div class="quiz-question">1. What did Daniela ask when she felt curious?</div>
        <div class="quiz-options">
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> She changed the topic.</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> She asked a follow-up question.</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> She said goodbye.</div>
        </div>
      </div>
      <div class="quiz-item">
        <div class="quiz-question">2. How did Daniela show she was listening?</div>
        <div class="quiz-options">
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> She looked at her phone.</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> She nodded and reacted with a smile.</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> She talked only about herself.</div>
        </div>
      </div>
      <div class="quiz-item">
        <div class="quiz-question">3. Why did the conversation keep going?</div>
        <div class="quiz-options">
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because she changed the topic quickly.</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Because she looked interested and asked for more details.</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because the other person did all the work.</div>
        </div>
      </div>
    </div>

    <!-- STAGE 1.4: GRAMMAR TIP -->
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip</h4><span class="badge badge-grammar">Grammar</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:1rem">Read the rule carefully and study the examples.</p>
      <div style="padding:1.2rem;background:rgba(0,48,128,.04);border:1px solid rgba(0,48,128,.15);border-radius:10px">
        <h5 style="font-size:.95rem;color:var(--navy);margin-bottom:.8rem">Follow-up Questions &amp; Active Listening</h5>
        <p style="font-size:.85rem;color:var(--text-mid);margin-bottom:.8rem">To keep a conversation going, do three things: <strong>react</strong>, then ask a <strong>follow-up question</strong>, then ask for a <strong>detail</strong>. Follow-up questions start with <strong>What kind of...?</strong>, <strong>How long...?</strong>, <strong>Where exactly...?</strong>, or <strong>Why...?</strong>. Short "echo" questions (<strong>Oh, really? Did you?</strong>) show you are listening.</p>
        <table style="width:100%;border-collapse:collapse;font-size:.85rem;margin-bottom:.8rem">
          <thead><tr style="background:var(--navy);color:#fff"><th style="padding:.5rem .8rem;text-align:left">Tool</th><th style="padding:.5rem .8rem;text-align:left">Example</th><th style="padding:.5rem .8rem;text-align:left">When to use</th></tr></thead>
          <tbody>
            <tr style="border-bottom:1px solid #e5e5e0"><td style="padding:.5rem .8rem;color:var(--accent);font-weight:600">React</td><td style="padding:.5rem .8rem">"Oh, really?" / "That is interesting!" / "Wow!"</td><td style="padding:.5rem .8rem;font-style:italic">right after they speak</td></tr>
            <tr style="border-bottom:1px solid #e5e5e0"><td style="padding:.5rem .8rem;color:var(--accent);font-weight:600">Follow-up</td><td style="padding:.5rem .8rem">"What kind of...?" / "How long...?" / "Where exactly...?"</td><td style="padding:.5rem .8rem;font-style:italic">to learn more</td></tr>
            <tr style="border-bottom:1px solid #e5e5e0"><td style="padding:.5rem .8rem;color:var(--accent);font-weight:600">Echo question</td><td style="padding:.5rem .8rem">"Did you?" / "Do you?" / "Really?"</td><td style="padding:.5rem .8rem;font-style:italic">to show you listen</td></tr>
            <tr><td style="padding:.5rem .8rem;color:var(--accent);font-weight:600">Ask a detail</td><td style="padding:.5rem .8rem">"Tell me more." / "Can you tell me one more detail?"</td><td style="padding:.5rem .8rem;font-style:italic">to keep it open</td></tr>
          </tbody>
        </table>
        <div style="padding:.8rem;background:rgba(220,38,38,.04);border:1px solid rgba(220,38,38,.15);border-radius:8px;font-size:.82rem">
          <strong style="color:#dc2626">Common Mistake:</strong><br>
          <span style="color:#dc2626;text-decoration:line-through">"What you do?"</span> &#10007; &#8594; <span style="color:#16a34a">"What kind of work do you do?"</span> &#10003;<br>
          <span style="color:#dc2626;text-decoration:line-through">"I am very interesting in your job."</span> &#10007; &#8594; <span style="color:#16a34a">"I am very interested in your job."</span> &#10003;<br>
          <span style="color:var(--text-dim);font-style:italic">A flat "Ok." kills a conversation. React first, then ask a follow-up — and remember: people are <strong>interested</strong>, topics are <strong>interesting</strong>.</span>
        </div>
      </div>
    </div>

    <!-- STAGE 1.5: FILL-IN-THE-BLANK -->
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Complete the Follow-ups</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:1rem">Write the missing word. Faça um de cada vez. Errou? Leia a dica com calma.</p>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"What <input class="blank-input" data-answer="kind" data-hint="What ___ of...? = pede o tipo" data-phrase="What kind of work do you do?" placeholder="___"> of work do you do?"</div><button class="check-btn" onclick="checkBlank(this)">Check</button><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"How <input class="blank-input" data-answer="long" data-hint="How ___ ? = pede duração" data-phrase="How long did the project take?" placeholder="___"> did the project take?"</div><button class="check-btn" onclick="checkBlank(this)">Check</button><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"<input class="blank-input" data-answer="where" data-hint="___ exactly...? = pede o lugar" data-phrase="Where exactly is your office?" placeholder="___"> exactly is your office?"</div><button class="check-btn" onclick="checkBlank(this)">Check</button><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"Oh, <input class="blank-input" data-answer="really" data-hint="reação curta de surpresa/interesse" data-phrase="Really? That sounds great!" placeholder="___">? That sounds great!"</div><button class="check-btn" onclick="checkBlank(this)">Check</button><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"Can you tell me <input class="blank-input" data-answer="more" data-hint="pede um detalhe a mais" data-phrase="Can you tell me more about it?" placeholder="___"> about it?"</div><button class="check-btn" onclick="checkBlank(this)">Check</button><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"You <input class="blank-input" data-answer="mentioned" data-hint="mention + -ed: retomar o que a pessoa disse" data-phrase="You mentioned a new system." placeholder="___"> a new system." <span style="color:var(--text-dim);font-size:.8rem">(mention)</span></div><button class="check-btn" onclick="checkBlank(this)">Check</button><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button></div>
    </div>

    <!-- STAGE 2: ORDERING -->
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:1rem">Listen first, then put the conversation in the correct order — from the opener to the friendly close.</p>
      <div style="margin-bottom:.8rem"><button class="audio-btn" onclick="speakText('[order-l8]',this)" aria-label="Ouvir sequência completa">&#9654; Listen sequência correta</button></div>
      <div class="order-container" id="order-l8">
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l8')"><span class="order-num">?</span><span class="order-text">"That is interesting! How long did you work there?"</span><span class="order-arrows"><button class="arrow-btn" onclick="event.stopPropagation();moveItem(this,-1,'order-l8')">&#9650;</button><button class="arrow-btn" onclick="event.stopPropagation();moveItem(this,1,'order-l8')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l8')"><span class="order-num">?</span><span class="order-text">"Wow, that sounds great. Let us keep in touch!"</span><span class="order-arrows"><button class="arrow-btn" onclick="event.stopPropagation();moveItem(this,-1,'order-l8')">&#9650;</button><button class="arrow-btn" onclick="event.stopPropagation();moveItem(this,1,'order-l8')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l8')"><span class="order-num">?</span><span class="order-text">"So, what do you do?"</span><span class="order-arrows"><button class="arrow-btn" onclick="event.stopPropagation();moveItem(this,-1,'order-l8')">&#9650;</button><button class="arrow-btn" onclick="event.stopPropagation();moveItem(this,1,'order-l8')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l8')"><span class="order-num">?</span><span class="order-text">"You mentioned a big project. Tell me more about it."</span><span class="order-arrows"><button class="arrow-btn" onclick="event.stopPropagation();moveItem(this,-1,'order-l8')">&#9650;</button><button class="arrow-btn" onclick="event.stopPropagation();moveItem(this,1,'order-l8')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l8')"><span class="order-num">?</span><span class="order-text">"Oh, really? What kind of company is it?"</span><span class="order-arrows"><button class="arrow-btn" onclick="event.stopPropagation();moveItem(this,-1,'order-l8')">&#9650;</button><button class="arrow-btn" onclick="event.stopPropagation();moveItem(this,1,'order-l8')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l8')">Verificar Ordem</button>
    </div>

    <!-- STAGE 3: PRONUNCIATION -->
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation Practice</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:1rem">Listen first, then record. Use friendly, rising intonation on the reactions and questions.</p>
      <div class="speech-card" data-phrase="Oh, really? That sounds great!"><div class="speech-phrase">Oh, really? That sounds great!</div><div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Stop</button></div><div class="speech-result"></div></div>
      <div class="speech-card" data-phrase="What kind of project was it?"><div class="speech-phrase">What kind of project was it?</div><div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Stop</button></div><div class="speech-result"></div></div>
      <div class="speech-card" data-phrase="How long did it take?"><div class="speech-phrase">How long did it take?</div><div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Stop</button></div><div class="speech-result"></div></div>
      <div class="speech-card" data-phrase="That is interesting. Tell me more about it."><div class="speech-phrase">That is interesting. Tell me more about it.</div><div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Stop</button></div><div class="speech-result"></div></div>
    </div>

    <!-- STAGE 4: SITUATIONAL QUIZ -->
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:1rem">Choose the best answer for each situation. Escolha a melhor resposta.</p>
      <div class="quiz-item">
        <div class="quiz-question">A new contact says: "I work in logistics." You want to keep the conversation going. What is best?</div>
        <div class="quiz-options">
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Ok."</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Oh, really? What kind of logistics do you do?"</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I work in IT."</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">D</span> "What you do?"</div>
        </div>
      </div>
      <div class="quiz-item">
        <div class="quiz-question">You want to say you want to know more about someone's job. Which is correct?</div>
        <div class="quiz-options">
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I am very interesting in your job."</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I am really interested in your job."</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I am interest your job."</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">D</span> "Your job is interested."</div>
        </div>
      </div>
      <div class="quiz-item">
        <div class="quiz-question">Someone mentioned a big launch last year. You want one more detail. What do you say?</div>
        <div class="quiz-options">
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Did you launched it alone?"</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Did you launch it alone, or with a team?"</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Anyway, let us change the topic."</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">D</span> "I do not care."</div>
        </div>
      </div>
    </div>

    <!-- STAGE 5: THINK ABOUT IT -->
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Think About It</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:1rem">Aqui não tem resposta certa — é pra você pensar em inglês. Toque no microfone e responda como vier.</p>
      <div class="think-card">
        <div class="think-question">Imagine you meet someone new at an international event. They say: "Last year, we launched a new app." Keep the conversation going for one minute: react, ask two follow-up questions (What kind of...? How long...?), ask for one more detail, and close in a friendly way. Speak out loud.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Free Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)">&#9632; Stop</button></div>
        <div id="think-result-1"></div>
      </div>
    </div>

    <!-- SURVIVAL CARD (Conversation Toolkit) -->
    <div class="survival-card">
      <h4 style="font-family:'Cormorant Garamond',serif;font-size:1.1rem;color:var(--accent);margin-bottom:.8rem">Conversation Toolkit — Lesson 8</h4>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">These 5 phrases keep any conversation alive. Practice them out loud!</p>
      <div class="survival-phrase"><span class="sp-num">1</span><span class="sp-en">Oh, really? That is interesting!</span><button class="btn btn-listen" onclick="speakText('Oh, really? That is interesting!',this)" style="padding:.3rem .6rem;font-size:.72rem;min-height:36px">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">2</span><span class="sp-en">What kind of project was it?</span><button class="btn btn-listen" onclick="speakText('What kind of project was it?',this)" style="padding:.3rem .6rem;font-size:.72rem;min-height:36px">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">3</span><span class="sp-en">How long did it take?</span><button class="btn btn-listen" onclick="speakText('How long did it take?',this)" style="padding:.3rem .6rem;font-size:.72rem;min-height:36px">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">4</span><span class="sp-en">Wow, that sounds great! Tell me more.</span><button class="btn btn-listen" onclick="speakText('Wow, that sounds great! Tell me more.',this)" style="padding:.3rem .6rem;font-size:.72rem;min-height:36px">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">5</span><span class="sp-en">I am really curious about this topic.</span><button class="btn btn-listen" onclick="speakText('I am really curious about this topic.',this)" style="padding:.3rem .6rem;font-size:.72rem;min-height:36px">&#9835;</button></div>
    </div>

    <!-- CHECKLIST -->
    <div style="margin-top:1.5rem" id="checklist-1">
      <h4 style="font-family:'Cormorant Garamond',serif;font-size:1.1rem;color:var(--accent);margin-bottom:.8rem">O que eu aprendi — Aula 08</h4>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read each statement out loud. If you can say yes to all of them, you have mastered this lesson.</p>
      <ul class="checklist" style="list-style:none;padding:0">
        <li style="padding:.5rem 0;border-bottom:1px solid #e5e5e0;font-size:.88rem"><label style="display:flex;align-items:center;gap:.5rem;cursor:pointer"><input type="checkbox" onchange="toggleChecklist(this)"> Eu mantenho uma conversa de networking viva, sem deixar morrer.</label></li>
        <li style="padding:.5rem 0;border-bottom:1px solid #e5e5e0;font-size:.88rem"><label style="display:flex;align-items:center;gap:.5rem;cursor:pointer"><input type="checkbox" onchange="toggleChecklist(this)"> Eu conheço 8 palavras novas (follow-up, curious, interested, nod...).</label></li>
        <li style="padding:.5rem 0;border-bottom:1px solid #e5e5e0;font-size:.88rem"><label style="display:flex;align-items:center;gap:.5rem;cursor:pointer"><input type="checkbox" onchange="toggleChecklist(this)"> Eu faço perguntas de follow-up (What kind of...? How long...? Where exactly...?).</label></li>
        <li style="padding:.5rem 0;border-bottom:1px solid #e5e5e0;font-size:.88rem"><label style="display:flex;align-items:center;gap:.5rem;cursor:pointer"><input type="checkbox" onchange="toggleChecklist(this)"> Eu reajo com naturalidade ("Oh, really?", "That is interesting!").</label></li>
        <li style="padding:.5rem 0;border-bottom:1px solid #e5e5e0;font-size:.88rem"><label style="display:flex;align-items:center;gap:.5rem;cursor:pointer"><input type="checkbox" onchange="toggleChecklist(this)"> Eu uso echo questions (Did you? Really?) para mostrar que estou ouvindo.</label></li>
        <li style="padding:.5rem 0;border-bottom:1px solid #e5e5e0;font-size:.88rem"><label style="display:flex;align-items:center;gap:.5rem;cursor:pointer"><input type="checkbox" onchange="toggleChecklist(this)"> Eu peço um detalhe a mais ("Tell me more.", "one more detail").</label></li>
        <li style="padding:.5rem 0;border-bottom:1px solid #e5e5e0;font-size:.88rem"><label style="display:flex;align-items:center;gap:.5rem;cursor:pointer"><input type="checkbox" onchange="toggleChecklist(this)"> Eu não confundo interested (pessoa) e interesting (assunto).</label></li>
        <li style="padding:.5rem 0;font-size:.88rem"><label style="display:flex;align-items:center;gap:.5rem;cursor:pointer"><input type="checkbox" onchange="toggleChecklist(this)"> Eu me sinto confiante para transformar um "oi" num contato real.</label></li>
      </ul>
    </div>

  </div>
</div>'''

# ============================================================ IN CLASS menu (inner)
INCLASS_INNER = '''
<div class="tab-content" id="tab-inclass">
  <h3 style="font-family:'Cormorant Garamond',serif;font-size:1.3rem;margin-bottom:1rem">IN CLASS — Select Lesson</h3>
  <div style="display:flex;flex-direction:column;gap:1rem">
    <div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" onclick="enterSlideMode();" onmouseover="this.style.borderColor='var(--accent)'" onmouseout="this.style.borderColor='rgba(200,200,190,.5)'">
      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">08</div>
      <div><div style="font-weight:600;font-size:.95rem">Networking in Action: Keeping the Conversation Going</div><div style="font-size:.8rem;color:var(--text-dim)">Follow-up questions, active listening, showing interest — 37 slides</div></div>
    </div>
  </div>
</div>
'''

# ============================================================ COMPLEMENTARES (inner)
COMP_INNER = '''<h3 style="font-family:'Cormorant Garamond',serif;font-size:1.3rem;margin-bottom:.5rem">Materiais Complementares — Aula 08</h3>
<p style="font-size:.82rem;color:var(--text-dim);margin-bottom:1.5rem">Tema da aula: manter conversas vivas com follow-up questions e active listening. Preste atenção em como as pessoas reagem e pedem mais detalhes. Marque como concluído ao terminar.</p>
<div class="media-grid">
  <div class="media-card-wrapper" data-media="l8-podcast">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb"><svg viewBox="0 0 24 24"><path d="M12 1a3 3 0 00-3 3v8a3 3 0 006 0V4a3 3 0 00-3-3z" fill="none" stroke="currentColor" stroke-width="2"/><path d="M19 10v2a7 7 0 01-14 0v-2" fill="none" stroke="currentColor" stroke-width="2"/></svg></div>
      <div class="media-info">
        <div class="media-type">Podcast</div>
        <h5>WorkLife with Adam Grant (TED)</h5>
        <p>Adam Grant entrevista convidados fazendo exatamente o que você praticou hoje: ele reage, demonstra interesse e faz perguntas de follow-up ("What kind of...?", "How did that feel?") para o convidado continuar falando. É uma masterclass de active listening.</p>
        <p class="media-tip">Dica: ouça um episódio e anote 5 perguntas de follow-up que o host faz.</p>
        <a href="https://www.ted.com/podcasts/worklife" target="_blank" rel="noopener" style="display:inline-block;margin-top:.5rem;font-size:.75rem;color:var(--accent);font-weight:600;text-decoration:none;border-bottom:1px solid var(--accent)">Listen on TED &#8599;</a>
      </div>
    </div>
  </div>
  <div class="media-card-wrapper" data-media="l8-youtube">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb"><svg viewBox="0 0 24 24"><rect x="2" y="3" width="20" height="14" rx="2" ry="2" fill="none" stroke="currentColor" stroke-width="2"/><polygon points="10 8 16 12 10 16 10 8" fill="currentColor"/></svg></div>
      <div class="media-info">
        <div class="media-type">YouTube</div>
        <h5>BBC Learning English — Making Conversation / Small Talk</h5>
        <p>Vídeos curtos e claros sobre como manter uma conversa: reações ("Oh, really?"), follow-up questions e small talk em inglês. Nível acessível e britânico claro — exatamente o foco da aula de hoje.</p>
        <p class="media-tip">Dica: repita em voz alta as reações e perguntas de follow-up que aparecem.</p>
        <a href="https://www.youtube.com/@bbclearningenglish" target="_blank" rel="noopener" style="display:inline-block;margin-top:.5rem;font-size:.75rem;color:var(--accent);font-weight:600;text-decoration:none;border-bottom:1px solid var(--accent)">Watch on YouTube &#8599;</a>
      </div>
    </div>
  </div>
  <div class="media-card-wrapper" data-media="l8-ted">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb"><svg viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"/></svg></div>
      <div class="media-info">
        <div class="media-type">TED Talk</div>
        <h5>Celeste Headlee — 10 Ways to Have a Better Conversation</h5>
        <p>Como ouvir de verdade e manter uma conversa interessante: fazer boas perguntas, demonstrar interesse genuíno e não monopolizar o assunto. Reforça o active listening e os follow-ups que você usou hoje.</p>
        <p class="media-tip">Dica: assista com legenda em inglês e escolha 3 dicas para usar no próximo evento.</p>
        <a href="https://www.ted.com/talks/celeste_headlee_10_ways_to_have_a_better_conversation" target="_blank" rel="noopener" style="display:inline-block;margin-top:.5rem;font-size:.75rem;color:var(--accent);font-weight:600;text-decoration:none;border-bottom:1px solid var(--accent)">Watch on TED &#8599;</a>
      </div>
    </div>
  </div>
</div>'''

# ============================================================ SLIDES (37)
SLIDES_HTML = '''<!-- ===== CHAPTER 1: THE DREAM (slides 1-4) ===== -->

<div class="slide slide-image active" data-slide="1" data-phase="1" data-teacher="<strong>Abertura (2 min):</strong> Compartilhe a tela. Deixe o slide por 15 segundos. Tom caloroso. 'Today we learn a superpower for networking — how to keep a conversation going, so it never dies.'" style="background-image:url('https://images.unsplash.com/photo-1543269865-cbf427effbad?w=1400&q=80')">
  <div class="slide-inner"><div class="chapter-label">Lesson 8</div><h1 class="slide-title">Networking<br><span class="accent">in Action</span></h1><p class="slide-subtitle">Keeping the Conversation Going — A2+ — 60 minutes — Alumni by Better</p></div>
</div>

<div class="slide slide-dark" data-slide="2" data-phase="1" data-teacher="<strong>Warm-up + Callback (5 min):</strong> Revise palavras da Aula 7 (launch, challenge, result, deadline). Agora vire o jogo: 'Last class YOU told a success story. Today, imagine a colleague tells you that story — how do you keep the conversation going?' Peça que Daniela faça perguntas de follow-up no passado: 'You said you launched a system — what kind of system? How long did it take? What was the result?' <strong>Obstáculo:</strong> se Daniela só responder sem devolver, modele: 'Good — now ask ME a follow-up question.'">
  <div class="slide-inner"><div class="chapter-label">Chapter 1: The Dream</div><h2 class="slide-heading">From Telling to <span class="accent">Asking</span></h2><p style="font-size:.9rem;color:rgba(255,255,255,.6);margin-bottom:1rem">In Lesson 7 you told your story. Now use those words to ask follow-up questions.</p>
    <div style="display:flex;flex-direction:column;gap:.6rem">
      <div style="display:flex;align-items:center;gap:.8rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:10px;padding:.7rem 1rem;cursor:pointer" onclick="speakText('Launch',this)"><strong style="color:var(--accent-light);min-width:120px">Launch</strong><span style="font-size:.85rem;color:rgba(255,255,255,.6);flex:1;font-style:italic">"You launched a system — what kind of system was it?"</span></div>
      <div style="display:flex;align-items:center;gap:.8rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:10px;padding:.7rem 1rem;cursor:pointer" onclick="speakText('Challenge',this)"><strong style="color:var(--accent-light);min-width:120px">Challenge</strong><span style="font-size:.85rem;color:rgba(255,255,255,.6);flex:1;font-style:italic">"What was the biggest challenge? How did you solve it?"</span></div>
      <div style="display:flex;align-items:center;gap:.8rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:10px;padding:.7rem 1rem;cursor:pointer" onclick="speakText('Result',this)"><strong style="color:var(--accent-light);min-width:120px">Result</strong><span style="font-size:.85rem;color:rgba(255,255,255,.6);flex:1;font-style:italic">"Oh, really? And what was the result?"</span></div>
      <div style="display:flex;align-items:center;gap:.8rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:10px;padding:.7rem 1rem;cursor:pointer" onclick="speakText('Deadline',this)"><strong style="color:var(--accent-light);min-width:120px">Deadline</strong><span style="font-size:.85rem;color:rgba(255,255,255,.6);flex:1;font-style:italic">"Was the deadline very tight? How long did you have?"</span></div>
    </div>
  </div>
</div>

<div class="slide slide-image" data-slide="3" data-phase="1" data-teacher="<strong>Conexão emocional (3 min):</strong> 'You meet someone at an event. You say So, what do you do? They answer. Then... silence. The conversation dies.' Pergunte: 'Why does this happen?' Aceite respostas em português, repita em inglês. 'After today, your conversations will not die.'" style="background-image:url('https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=1400&q=80')">
  <div class="slide-inner"><div class="chapter-label">Chapter 1: The Dream</div><h2 class="slide-title">When the Talk<br><span class="accent">Does Not Die</span></h2><p class="slide-subtitle">"So... what do you do?" — and then?</p></div>
</div>

<div class="slide slide-dark" data-slide="4" data-phase="1" data-teacher="<strong>Objetivo da aula (1 min):</strong> Leia o objetivo em voz alta. 'After today, you will keep any networking conversation alive — react, show interest, and ask natural follow-up questions!'">
  <div class="slide-inner" style="text-align:center"><div class="chapter-label">Today's Goal</div><h2 class="slide-heading" style="color:#fff">After this lesson, <span class="accent">Daniela</span> will...</h2><p style="font-size:1.2rem;color:rgba(255,255,255,.85);line-height:1.8;max-width:600px;margin:0 auto">...keep a networking conversation going — reacting, showing interest, and asking natural follow-up questions.</p></div>
</div>

<!-- ===== CHAPTER 2: PACKING WORDS (slides 5-9) ===== -->

<div class="slide slide-image" data-slide="5" data-phase="2" data-teacher="<strong>Transição (10 seg):</strong> 'To keep a conversation alive, you need the right words. Let us learn eight.'" style="background-image:url('https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=1400&q=80')">
  <div class="slide-inner"><div class="chapter-label">Chapter 2: The Words</div><h2 class="slide-title">Conversation<br><span class="accent">Vocabulary</span></h2><p class="slide-subtitle">Eight words for active listening</p></div>
</div>

<div class="slide slide-light" data-slide="6" data-phase="2" data-teacher="<strong>Vocabulário (5 min):</strong> ANTES de clicar cada card, leia o hint e pergunte: 'What word do you think this is?' Espere 5 segundos. DEPOIS de revelar: toque áudio 2x, Daniela repete. Foque: FOLLOW-up (stress na 1a), CU-rious (3 sons), IN-terested (4 sílabas, stress na 1a), NOD (curto). <strong>CCQ:</strong> 'A question for more information — is it a follow-up or a topic?' (follow-up). 'When you want to know more, are you curious or bored?' (curious).">
  <div class="slide-inner"><div class="chapter-label">Vocabulary</div><h2 class="slide-heading">Words <span class="accent">1-4</span></h2>
    <div class="vocab-grid" id="vocabGrid1">
      <div class="vocab-card" onclick="this.classList.toggle('revealed')"><div class="card-icon" style="background:linear-gradient(135deg,#0d7377,#14919b)"><svg viewBox="0 0 24 24" fill="none" stroke="#fff"><path d="M21 11.5a8.38 8.38 0 01-.9 3.8 8.5 8.5 0 01-7.6 4.7 8.38 8.38 0 01-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 01-.9-3.8 8.5 8.5 0 014.7-7.6 8.38 8.38 0 013.8-.9h.5a8.48 8.48 0 018 8v.5z"/></svg><div class="card-hint">A question that asks for more information</div></div><div class="card-body"><div class="card-word">Follow-up</div><div class="card-def">A question that asks for more information about what someone said</div><div class="card-example">"Can I ask a follow-up question?"</div><div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('Follow-up',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div></div></div>
      <div class="vocab-card" onclick="this.classList.toggle('revealed')"><div class="card-icon" style="background:linear-gradient(135deg,#7c3aed,#a78bfa)"><svg viewBox="0 0 24 24" fill="none" stroke="#fff"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg><div class="card-hint">Wanting to know more about something</div></div><div class="card-body"><div class="card-word">Curious</div><div class="card-def">Wanting to know more about something</div><div class="card-example">"I am curious about your job."</div><div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('Curious',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div></div></div>
      <div class="vocab-card" onclick="this.classList.toggle('revealed')"><div class="card-icon" style="background:linear-gradient(135deg,#059669,#34d399)"><svg viewBox="0 0 24 24" fill="none" stroke="#fff"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg><div class="card-hint">Giving attention because you want to know more</div></div><div class="card-body"><div class="card-word">Interested</div><div class="card-def">Giving attention because you want to know more</div><div class="card-example">"She looked really interested in my story."</div><div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('Interested',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div></div></div>
      <div class="vocab-card" onclick="this.classList.toggle('revealed')"><div class="card-icon" style="background:linear-gradient(135deg,#b45309,#f59e0b)"><svg viewBox="0 0 24 24" fill="none" stroke="#fff"><path d="M16 21v-2a4 4 0 00-4-4H6a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><polyline points="16 11 18 13 22 9"/></svg><div class="card-hint">Move your head up and down to show you are listening</div></div><div class="card-body"><div class="card-word">Nod</div><div class="card-def">To move your head up and down to show you are listening</div><div class="card-example">"People nod to show they are listening."</div><div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('Nod',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div></div></div>
    </div>
    <div class="vocab-counter" id="vocabCount1">0 / 4 words revealed</div>
  </div>
</div>

<div class="slide slide-light" data-slide="7" data-phase="2" data-teacher="<strong>Vocabulário (5 min):</strong> Revele as 4 últimas palavras. Foque: re-ACT (stress na 2a), DE-tail (stress na 1a), MEN-tion (som 'shun'), TOP-ic. <strong>CCQ:</strong> 'A small piece of information — is it a detail or a topic?' (detail). 'The subject of the conversation — topic or react?' (topic).">
  <div class="slide-inner"><div class="chapter-label">Vocabulary</div><h2 class="slide-heading">Words <span class="accent">5-8</span></h2>
    <div class="vocab-grid" id="vocabGrid2">
      <div class="vocab-card" onclick="this.classList.toggle('revealed')"><div class="card-icon" style="background:linear-gradient(135deg,#dc2626,#ef4444)"><svg viewBox="0 0 24 24" fill="none" stroke="#fff"><circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/></svg><div class="card-hint">Show your feelings about what someone says</div></div><div class="card-body"><div class="card-word">React</div><div class="card-def">To show your feelings about what someone says</div><div class="card-example">"It is polite to react with a smile."</div><div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('React',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div></div></div>
      <div class="vocab-card" onclick="this.classList.toggle('revealed')"><div class="card-icon" style="background:linear-gradient(135deg,#0891b2,#22d3ee)"><svg viewBox="0 0 24 24" fill="none" stroke="#fff"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg><div class="card-hint">A small piece of information</div></div><div class="card-body"><div class="card-word">Detail</div><div class="card-def">A small piece of information</div><div class="card-example">"Tell me one more detail."</div><div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('Detail',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div></div></div>
      <div class="vocab-card" onclick="this.classList.toggle('revealed')"><div class="card-icon" style="background:linear-gradient(135deg,#1e3a5f,#3b6fa0)"><svg viewBox="0 0 24 24" fill="none" stroke="#fff"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/></svg><div class="card-hint">To say something briefly</div></div><div class="card-body"><div class="card-word">Mention</div><div class="card-def">To say something briefly</div><div class="card-example">"You mentioned a new project."</div><div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('Mention',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div></div></div>
      <div class="vocab-card" onclick="this.classList.toggle('revealed')"><div class="card-icon" style="background:linear-gradient(135deg,#4338ca,#818cf8)"><svg viewBox="0 0 24 24" fill="none" stroke="#fff"><line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/></svg><div class="card-hint">The subject of a conversation</div></div><div class="card-body"><div class="card-word">Topic</div><div class="card-def">The subject of a conversation</div><div class="card-example">"Let us change the topic."</div><div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('Topic',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div></div></div>
    </div>
    <div class="vocab-counter" id="vocabCount2">0 / 4 words revealed</div>
  </div>
</div>

<div class="slide slide-light" data-slide="8" data-phase="2" data-teacher="<strong>Revisão (3 min):</strong> Clique cada palavra. Daniela repete 2x. Se errar pronúncia: modelo correto + repetição. 'Excellent, Daniela! Eight words to keep any conversation alive!'">
  <div class="slide-inner" style="overflow-y:auto;max-height:75vh"><div class="chapter-label">Review</div><h2 class="slide-heading">Say It <span class="accent">All</span></h2><p style="font-size:.9rem;color:var(--text-dim);margin-bottom:.8rem">Click on each word to listen. Repeat each one twice.</p>
    <div style="display:flex;flex-direction:column;gap:.6rem">
      <div style="display:flex;align-items:center;gap:.8rem;background:#fff;border:1px solid #e8e4df;border-radius:10px;padding:.7rem 1rem;cursor:pointer" onclick="speakText('Follow-up',this)"><strong style="color:var(--accent);min-width:120px">Follow-up</strong><span style="font-size:.85rem;color:var(--text-dim);flex:1;font-style:italic">"Can I ask a follow-up question?"</span></div>
      <div style="display:flex;align-items:center;gap:.8rem;background:#fff;border:1px solid #e8e4df;border-radius:10px;padding:.7rem 1rem;cursor:pointer" onclick="speakText('Curious',this)"><strong style="color:var(--accent);min-width:120px">Curious</strong><span style="font-size:.85rem;color:var(--text-dim);flex:1;font-style:italic">"I am curious about your job."</span></div>
      <div style="display:flex;align-items:center;gap:.8rem;background:#fff;border:1px solid #e8e4df;border-radius:10px;padding:.7rem 1rem;cursor:pointer" onclick="speakText('Interested',this)"><strong style="color:var(--accent);min-width:120px">Interested</strong><span style="font-size:.85rem;color:var(--text-dim);flex:1;font-style:italic">"She looked really interested in my story."</span></div>
      <div style="display:flex;align-items:center;gap:.8rem;background:#fff;border:1px solid #e8e4df;border-radius:10px;padding:.7rem 1rem;cursor:pointer" onclick="speakText('Nod',this)"><strong style="color:var(--accent);min-width:120px">Nod</strong><span style="font-size:.85rem;color:var(--text-dim);flex:1;font-style:italic">"People nod to show they are listening."</span></div>
      <div style="display:flex;align-items:center;gap:.8rem;background:#fff;border:1px solid #e8e4df;border-radius:10px;padding:.7rem 1rem;cursor:pointer" onclick="speakText('React',this)"><strong style="color:var(--accent);min-width:120px">React</strong><span style="font-size:.85rem;color:var(--text-dim);flex:1;font-style:italic">"It is polite to react with a smile."</span></div>
      <div style="display:flex;align-items:center;gap:.8rem;background:#fff;border:1px solid #e8e4df;border-radius:10px;padding:.7rem 1rem;cursor:pointer" onclick="speakText('Detail',this)"><strong style="color:var(--accent);min-width:120px">Detail</strong><span style="font-size:.85rem;color:var(--text-dim);flex:1;font-style:italic">"Tell me one more detail."</span></div>
      <div style="display:flex;align-items:center;gap:.8rem;background:#fff;border:1px solid #e8e4df;border-radius:10px;padding:.7rem 1rem;cursor:pointer" onclick="speakText('Mention',this)"><strong style="color:var(--accent);min-width:120px">Mention</strong><span style="font-size:.85rem;color:var(--text-dim);flex:1;font-style:italic">"You mentioned a new project."</span></div>
      <div style="display:flex;align-items:center;gap:.8rem;background:#fff;border:1px solid #e8e4df;border-radius:10px;padding:.7rem 1rem;cursor:pointer" onclick="speakText('Topic',this)"><strong style="color:var(--accent);min-width:120px">Topic</strong><span style="font-size:.85rem;color:var(--text-dim);flex:1;font-style:italic">"Let us change the topic."</span></div>
    </div>
  </div>
</div>

<div class="slide slide-dark" data-slide="9" data-phase="2" data-teacher="<strong>Bridge (2 min):</strong> 'You have the words. But the real secret is HOW you use them: react, then ask a follow-up question. That is the code of a great conversation.' Transição natural para a gramática funcional.">
  <div class="slide-inner" style="text-align:center"><div class="chapter-label">Bridge</div><h2 class="slide-heading" style="color:#fff">From Words to <span class="accent">the Code</span></h2><p style="font-size:1.1rem;color:rgba(255,255,255,.7);line-height:1.8;max-width:550px;margin:0 auto">You have the words. Now let us learn the secret: react, then ask a follow-up question.</p></div>
</div>

<!-- ===== CHAPTER 3: THE CODE (slides 10-14) ===== -->

<div class="slide slide-image" data-slide="10" data-phase="3" data-teacher="<strong>Transição (10 seg):</strong> 'Now let us discover the code — how to build follow-up questions and natural reactions!'" style="background-image:url('https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=1400&q=80')">
  <div class="slide-inner"><div class="chapter-label">Chapter 3: The Code</div><h2 class="slide-title">Follow-up<br><span class="accent">Questions</span></h2><p class="slide-subtitle">React, then ask for more</p></div>
</div>

<div class="slide slide-light" data-slide="11" data-phase="3" data-teacher="<strong>Grammar Discovery (5 min):</strong> NÃO explique a regra ainda. Aponte para as perguntas e pergunte: 'What do these questions have in common? What do they ask for?' Espere 10 segundos. Se Daniela não responder: 'Look — they all ask for MORE information. They keep the conversation going.' Só clique Reveal DEPOIS da tentativa dela.">
  <div class="slide-inner"><div class="chapter-label">Grammar Discovery</div><h2 class="slide-heading">Grammar <span class="accent">Discovery</span></h2><p style="font-size:.92rem;color:var(--text-dim);margin-bottom:.5rem">Look at the questions. What do they all ask for?</p>
    <div class="grammar-sentences">
      <div class="grammar-sentence">"<strong>What kind of</strong> work do you do?"</div>
      <div class="grammar-sentence">"<strong>How long</strong> did the project take?"</div>
      <div class="grammar-sentence">"<strong>Where exactly</strong> is your office?"</div>
      <div class="grammar-sentence">"Oh, <strong>really?</strong> Tell me more!"</div>
    </div>
    <div style="text-align:center"><button class="btn-primary" onclick="revealGrammar()"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg> Reveal the Rule</button></div>
    <div class="grammar-table-wrap" id="grammarTable"><table class="grammar-table"><thead><tr><th>Tool</th><th>How</th><th>Example</th></tr></thead><tbody><tr><td>React</td><td>short feeling word</td><td>"Oh, <strong>really?</strong>" / "<strong>Wow!</strong>"</td></tr><tr><td>Follow-up</td><td>What kind of / How long / Where exactly</td><td>"<strong>What kind of</strong> system?"</td></tr><tr><td>Echo question</td><td>Did you? / Do you?</td><td>"<strong>Did you?</strong> That is great!"</td></tr><tr><td>Ask a detail</td><td>Tell me more</td><td>"<strong>Tell me more</strong> about it."</td></tr></tbody></table></div>
  </div>
</div>

<div class="slide slide-light" data-slide="12" data-phase="3" data-teacher="<strong>Erro Comum (3 min):</strong> 'Two classic mistakes. First: questions need a helper — say What kind of work DO you do, not What you do. Second: people are interestED, topics are interestING.' Leia os erros. Pergunte: 'Which one is correct?'">
  <div class="slide-inner"><div class="chapter-label">Common Mistake</div><h2 class="slide-heading">Watch <span class="accent">Out!</span></h2>
    <div class="mistake-card"><div class="mistake-item mistake-wrong"><div class="mistake-icon"><svg viewBox="0 0 24 24" fill="none" stroke="#dc2626"><circle cx="12" cy="12" r="10"/><line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/></svg></div>"What you do?"</div><div class="mistake-item mistake-right"><div class="mistake-icon"><svg viewBox="0 0 24 24" fill="none" stroke="#16a34a"><path d="M22 11.08V12a10 10 0 11-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg></div>"What kind of work do you do?"</div></div>
    <div class="mistake-card" style="margin-top:1rem"><div class="mistake-item mistake-wrong"><div class="mistake-icon"><svg viewBox="0 0 24 24" fill="none" stroke="#dc2626"><circle cx="12" cy="12" r="10"/><line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/></svg></div>"I am very interesting in your job."</div><div class="mistake-item mistake-right"><div class="mistake-icon"><svg viewBox="0 0 24 24" fill="none" stroke="#16a34a"><path d="M22 11.08V12a10 10 0 11-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg></div>"I am very interested in your job."</div></div>
  </div>
</div>

<div class="slide slide-light" data-slide="13" data-phase="3" data-teacher="<strong>Prática (4 min):</strong> Leia cada follow-up com a lacuna. Daniela completa oralmente. DEPOIS clique para revelar. Se errar: 'What word asks for the TYPE? the TIME? the PLACE?' Celebre acertos.">
  <div class="slide-inner"><div class="chapter-label">Practice</div><h2 class="slide-heading">Complete the <span class="accent">Follow-up</span></h2>
    <div class="fill-grid">
      <div class="fill-item" onclick="revealFill(this)"><div class="fill-text">"What <span class="fill-blank">___</span><span class="fill-answer">kind</span> of company is it?"</div></div>
      <div class="fill-item" onclick="revealFill(this)"><div class="fill-text">"How <span class="fill-blank">___</span><span class="fill-answer">long</span> did you work there?"</div></div>
      <div class="fill-item" onclick="revealFill(this)"><div class="fill-text">"<span class="fill-blank">___</span><span class="fill-answer">Where</span> exactly is the office?"</div></div>
      <div class="fill-item" onclick="revealFill(this)"><div class="fill-text">"Oh, <span class="fill-blank">___</span><span class="fill-answer">really</span>? Tell me more!"</div></div>
      <div class="fill-item" onclick="revealFill(this)"><div class="fill-text">"You <span class="fill-blank">___</span><span class="fill-answer">mentioned</span> a new app. What is it?"</div></div>
    </div>
  </div>
</div>

<div class="slide slide-light" data-slide="14" data-phase="3" data-teacher="<strong>Sentence Building (3 min):</strong> Pergunte: 'How do you ask what kind of work someone does? How do you react with interest?' Espere. Corrija. Celebre tentativas.">
  <div class="slide-inner"><div class="chapter-label">Build</div><h2 class="slide-heading">Build Your <span class="accent">Follow-ups</span></h2><p style="font-size:.92rem;color:var(--text-dim);margin-bottom:1rem">Say the full question or reaction:</p>
    <div class="fill-grid">
      <div class="fill-item" onclick="revealFill(this)"><div class="fill-text">Ask what kind of work they do: "<span class="fill-blank">___</span><span class="fill-answer">What kind of work do you do?</span>"</div></div>
      <div class="fill-item" onclick="revealFill(this)"><div class="fill-text">Ask how long they worked there: "<span class="fill-blank">___</span><span class="fill-answer">How long did you work there?</span>"</div></div>
      <div class="fill-item" onclick="revealFill(this)"><div class="fill-text">React with interest: "<span class="fill-blank">___</span><span class="fill-answer">Oh, really? That is interesting!</span>"</div></div>
      <div class="fill-item" onclick="revealFill(this)"><div class="fill-text">Ask for one more detail: "<span class="fill-blank">___</span><span class="fill-answer">Can you tell me more about it?</span>"</div></div>
    </div>
  </div>
</div>

<!-- ===== CHAPTER 4: GETTING THERE (slides 15-20) ===== -->

<div class="slide slide-image" data-slide="15" data-phase="4" data-teacher="<strong>Transição (10 seg):</strong> 'Now let us hear a real networking conversation. Daniela meets Sophie, a new contact, at the coffee break of an international event.'" style="background-image:url('https://images.unsplash.com/photo-1517048676732-d65bc937f952?w=1400&q=80')">
  <div class="slide-inner"><div class="chapter-label">Chapter 4: Getting There</div><h2 class="slide-title">A Networking<br><span class="accent">Conversation</span></h2><p class="slide-subtitle">Keeping the talk alive at the coffee break</p></div>
</div>

<div class="slide slide-light" data-slide="16" data-phase="4" data-teacher="<strong>Artefato — Keep-It-Going Toolkit (3 min):</strong> 'Every great conversation follows four steps. Look at this card.' Pergunte: 'Someone says: We opened a new office. What do you say first? (react) Then? (follow-up) Then? (a detail)' Daniela responde oralmente, ativando o vocabulário.">
  <div class="slide-inner"><div class="chapter-label">Artifact</div><h2 class="slide-heading">The <span class="accent">Keep-It-Going Toolkit</span></h2>
    <div class="emergency-card-artifact">
      <div class="ec-header" style="background:linear-gradient(135deg,#0d7377,#14919b)"><h4>KEEP-IT-GOING TOOLKIT</h4><p>Four Steps</p></div>
      <div class="ec-body">
        <div class="ec-section"><h5>1. React</h5><p>Show your feelings. <em>"Oh, really? That is interesting!"</em></p></div>
        <div class="ec-section"><h5>2. Ask a Follow-up</h5><p>Ask for more. <em>"What kind of project was it?"</em></p></div>
        <div class="ec-section"><h5>3. Ask a Detail</h5><p>Go deeper. <em>"How long did it take? Tell me more."</em></p></div>
        <div class="ec-section"><h5>4. Keep it Open</h5><p>Stay curious; do not change the topic too fast. <em>"I am really curious about this."</em></p></div>
      </div>
      <div class="ec-footer">Use this shape at every networking event.</div>
    </div>
  </div>
</div>

<div class="slide slide-light" data-slide="17" data-phase="4" data-teacher="<strong>Diálogo (8 min):</strong> Clique 'Next Line' para cada fala. ANTES das falas de Daniela: 'What do you think Daniela says to keep the conversation going?' Espere. Vocabulário em destaque = palavras da aula. Toque o áudio de cada linha. Daniela repete as falas dela (são as reações e follow-ups). <strong>Dica de pronúncia:</strong> Oh REA-lly (rising), What KIND of, How LONG.">
  <div class="slide-inner"><div class="chapter-label">Dialogue</div><h2 class="slide-heading">At the <span class="accent">Coffee Break</span></h2>
    <div class="dialogue-box" id="dialogueBox">
      <div class="dialogue-line" data-line="1" data-speaker="Sophie" data-voice="rachel"><div class="dialogue-avatar pharma">S</div><div class="dialogue-bubble pharma-bubble">Hi! I do not think we have met. I am Sophie, from the Berlin office. <span class="audio-inline" onclick="speakText('Hi! I do not think we have met. I am Sophie, from the Berlin office.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg></span></div></div>
      <div class="dialogue-line" data-line="2" data-speaker="Daniela" data-voice="ellen"><div class="dialogue-avatar tania">D</div><div class="dialogue-bubble tania-bubble">Nice to meet you, Sophie! I am Daniela, from Sao Paulo. So, what do you do in Berlin? <span class="audio-inline" onclick="speakText('Nice to meet you, Sophie! I am Daniela, from Sao Paulo. So, what do you do in Berlin?',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg></span></div></div>
      <div class="dialogue-line" data-line="3" data-speaker="Sophie" data-voice="rachel"><div class="dialogue-avatar pharma">S</div><div class="dialogue-bubble pharma-bubble">I work in logistics. Last month, we opened a new distribution center. <span class="audio-inline" onclick="speakText('I work in logistics. Last month, we opened a new distribution center.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg></span></div></div>
      <div class="dialogue-line" data-line="4" data-speaker="Daniela" data-voice="ellen"><div class="dialogue-avatar tania">D</div><div class="dialogue-bubble tania-bubble">Oh, <strong class="vocab-highlight">really</strong>? That is <strong class="vocab-highlight">interesting</strong>! What kind of center is it? <span class="audio-inline" onclick="speakText('Oh, really? That is interesting! What kind of center is it?',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg></span></div></div>
      <div class="dialogue-line" data-line="5" data-speaker="Sophie" data-voice="rachel"><div class="dialogue-avatar pharma">S</div><div class="dialogue-bubble pharma-bubble">It is fully automated. It was a big <strong class="vocab-highlight">challenge</strong>, but the result was great. <span class="audio-inline" onclick="speakText('It is fully automated. It was a big challenge, but the result was great.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg></span></div></div>
      <div class="dialogue-line" data-line="6" data-speaker="Daniela" data-voice="ellen"><div class="dialogue-avatar tania">D</div><div class="dialogue-bubble tania-bubble">Wow, that sounds great! How long did the project take? <span class="audio-inline" onclick="speakText('Wow, that sounds great! How long did the project take?',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg></span></div></div>
      <div class="dialogue-line" data-line="7" data-speaker="Sophie" data-voice="rachel"><div class="dialogue-avatar pharma">S</div><div class="dialogue-bubble pharma-bubble">About eight months. Honestly, the <strong class="vocab-highlight">deadline</strong> was very tight. <span class="audio-inline" onclick="speakText('About eight months. Honestly, the deadline was very tight.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg></span></div></div>
      <div class="dialogue-line" data-line="8" data-speaker="Daniela" data-voice="ellen"><div class="dialogue-avatar tania">D</div><div class="dialogue-bubble tania-bubble">I can imagine. You <strong class="vocab-highlight">mentioned</strong> automation. Can you tell me one more <strong class="vocab-highlight">detail</strong>? <span class="audio-inline" onclick="speakText('I can imagine. You mentioned automation. Can you tell me one more detail?',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg></span></div></div>
      <div class="dialogue-line" data-line="9" data-speaker="Sophie" data-voice="rachel"><div class="dialogue-avatar pharma">S</div><div class="dialogue-bubble pharma-bubble">Sure! The robots move the boxes, so the team works faster now. <span class="audio-inline" onclick="speakText('Sure! The robots move the boxes, so the team works faster now.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg></span></div></div>
      <div class="dialogue-line" data-line="10" data-speaker="Daniela" data-voice="ellen"><div class="dialogue-avatar tania">D</div><div class="dialogue-bubble tania-bubble">That is amazing. I am really <strong class="vocab-highlight">curious</strong> about this <strong class="vocab-highlight">topic</strong>. Let us keep in touch! <span class="audio-inline" onclick="speakText('That is amazing. I am really curious about this topic. Let us keep in touch!',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg></span></div></div>
    </div>
    <div style="text-align:center;margin-top:1rem"><button class="btn-primary" id="nextLineBtn" onclick="nextDialogueLine()"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"/></svg> Next Line</button></div>
  </div>
</div>

<div class="slide slide-light" data-slide="18" data-phase="4" data-teacher="<strong>Compreensão (3 min):</strong> Perguntas sobre o que SOPHIE disse (o interlocutor). Daniela responde em frase completa. Se travar: dê o início da frase ('Sophie works in...').">
  <div class="slide-inner"><div class="chapter-label">Comprehension</div><h2 class="slide-heading">About the <span class="accent">Conversation</span></h2>
    <div class="comp-questions"><div class="comp-q" onclick="revealComp(this)"><div class="q-text">1. What does Sophie do, and what did her team open?</div><div class="q-answer">She works in logistics. Last month, her team opened a new, fully automated distribution center.</div></div><div class="comp-q" onclick="revealComp(this)"><div class="q-text">2. Which follow-up questions did Daniela ask?</div><div class="q-answer">"What kind of center is it?" and "How long did the project take?" — plus "Can you tell me one more detail?"</div></div><div class="comp-q" onclick="revealComp(this)"><div class="q-text">3. How did Daniela show she was interested?</div><div class="q-answer">She reacted ("Oh, really? That is interesting! Wow!"), asked for details, and stayed curious.</div></div></div>
  </div>
</div>

<div class="slide slide-dark" data-slide="19" data-phase="4" data-teacher="<strong>Listening 1 (5 min):</strong> 'Close your eyes and listen to the whole conversation.' Toque o áudio. NÃO mostre texto. Depois pergunte: 'What did Sophie open? What follow-up did Daniela ask?' <strong>Obstáculo:</strong> Se Daniela ficar frustrada: 'It is okay! Focus on the reactions and questions: Oh really, what kind of, how long.'">
  <div class="slide-inner" style="text-align:center"><div class="chapter-label">Listening</div><h2 class="slide-heading" style="color:#fff">The <span class="accent">Coffee Break Chat</span></h2><p style="color:rgba(255,255,255,.6);font-size:.9rem;margin-bottom:1rem">Listen to Daniela and Sophie keeping the conversation alive.</p>
    <div class="waveform waveform-paused" id="waveform1"><div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div></div>
    <button class="play-btn" id="listening1PlayBtn" onclick="toggleListening1(this)"><svg class="icon-play" viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"/></svg><svg class="icon-pause" viewBox="0 0 24 24" style="display:none"><rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/></svg></button>
    <div class="comp-questions" id="listening1Qs" style="display:none"><div class="comp-q" onclick="revealComp(this)" style="text-align:left"><div class="q-text">1. What did Sophie's team open?</div><div class="q-answer">A new, fully automated distribution center in Berlin.</div></div><div class="comp-q" onclick="revealComp(this)" style="text-align:left"><div class="q-text">2. What did Daniela do to keep the conversation going?</div><div class="q-answer">She reacted ("Oh, really?"), asked follow-ups ("What kind of...? How long...?"), and asked for one more detail.</div></div></div>
  </div>
</div>

<div class="slide slide-dark" data-slide="20" data-phase="4" data-teacher="<strong>Listening 2 (4 min):</strong> 'Now listen again, but focus on Daniela. Which reactions and follow-up questions does she use?' Toque novamente. Depois: 'Oh really, That is interesting, What kind of, How long, Tell me one more detail, I am curious!'">
  <div class="slide-inner" style="text-align:center"><div class="chapter-label">Listening</div><h2 class="slide-heading" style="color:#fff">Listen for the <span class="accent">Follow-ups</span></h2><p style="color:rgba(255,255,255,.6);font-size:.9rem;margin-bottom:1rem">Listen again. Which reactions and follow-up questions do you hear?</p>
    <div class="waveform waveform-paused" id="waveform2"><div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div></div>
    <button class="play-btn" id="listening2PlayBtn" onclick="toggleListening2(this)"><svg class="icon-play" viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"/></svg><svg class="icon-pause" viewBox="0 0 24 24" style="display:none"><rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/></svg></button>
    <div class="comp-questions" id="listening2Qs" style="display:none"><div class="comp-q" onclick="revealComp(this)" style="text-align:left"><div class="q-text">1. Which follow-up questions does Daniela ask?</div><div class="q-answer">"What kind of center is it?" and "How long did the project take?"</div></div><div class="comp-q" onclick="revealComp(this)" style="text-align:left"><div class="q-text">2. How does she react and stay curious?</div><div class="q-answer">"Oh, really? That is interesting!", "Can you tell me one more detail?", "I am really curious about this topic."</div></div></div>
  </div>
</div>

<!-- ===== CHAPTER 5: PRACTICE (slides 21-27) ===== -->

<div class="slide slide-image" data-slide="21" data-phase="5" data-teacher="<strong>Transição:</strong> 'More practice! Let us see how well you keep a conversation alive.'" style="background-image:url('https://images.unsplash.com/photo-1552664730-d307ca884978?w=1400&q=80')">
  <div class="slide-inner"><div class="chapter-label">Chapter 5: Practice</div><h2 class="slide-title">More<br><span class="accent">Practice</span></h2><p class="slide-subtitle">Quick fire, spot the error, and oral drilling</p></div>
</div>

<div class="slide slide-light" data-slide="22" data-phase="5" data-teacher="<strong>Quick Fire (6 min):</strong> Leia a situação. Daniela responde em inglês: reage E faz um follow-up. Se acertar: 'Show Answer' para confirmar. Se travar: dê o começo. 'Start with: Oh, really?...' Foco: reagir + perguntar.">
  <div class="slide-inner"><div class="chapter-label">Chapter 5: Practice</div><h2 class="slide-heading">Quick <span class="accent">Fire</span></h2>
    <div style="position:relative"><div class="challenge-score" id="challengeScore">0 / 6</div>
      <div class="challenge-card" id="challengeCard"><div class="challenge-counter" id="challengeCounter">Question 1 of 6</div><div class="challenge-prompt" id="challengePrompt">A new contact says: "I work in marketing." React and ask a follow-up.</div><div class="challenge-answer" id="challengeAnswer">"Oh, really? What kind of marketing do you do?"</div><div style="display:flex;gap:.8rem;margin-top:.5rem"><button class="btn-primary" id="showAnswerBtn" onclick="showChallengeAnswer()"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg> Show Answer</button><button class="btn-secondary" id="nextChallengeBtn" onclick="nextChallenge()" style="display:none"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"/></svg> Next Question</button></div></div>
    </div>
  </div>
</div>

<div class="slide slide-light" data-slide="23" data-phase="5" data-teacher="<strong>Spot the Error (4 min):</strong> Leia cada frase. Pergunte: 'Can you find the mistake?' Foco em question forms, interested/interesting e past questions. Se não encontrar em 10 seg, destaque a palavra errada. Celebre cada acerto.">
  <div class="slide-inner"><div class="chapter-label">Detective</div><h2 class="slide-heading">Spot the <span class="accent">Error</span></h2>
    <div class="error-grid" id="errorGrid">
      <div class="error-card" onclick="revealError(this)"><div class="error-sentence">"What you do?"</div><div class="error-fix">"What kind of work do you do?"</div></div>
      <div class="error-card" onclick="revealError(this)"><div class="error-sentence">"How long you work there?"</div><div class="error-fix">"How long did you work there?"</div></div>
      <div class="error-card" onclick="revealError(this)"><div class="error-sentence">"I am very interesting in your job."</div><div class="error-fix">"I am very interested in your job."</div></div>
      <div class="error-card" onclick="revealError(this)"><div class="error-sentence">"Did you launched a new app?"</div><div class="error-fix">"Did you launch a new app?"</div></div>
      <div class="error-card" onclick="revealError(this)"><div class="error-sentence">"Where exactly your office?"</div><div class="error-fix">"Where exactly is your office?"</div></div>
    </div>
    <div class="error-score" id="errorScore">0 / 5 errors found</div>
  </div>
</div>

<div class="slide slide-light" data-slide="24" data-phase="5" data-teacher="<strong>Oral Drilling (5 min):</strong> Leia a situação. Daniela responde oralmente. Clique para revelar o modelo. Se travar: dê scaffold: 'Start with Oh, really?...' ou 'Start with What kind of...'">
  <div class="slide-inner" style="overflow-y:auto;max-height:75vh"><div class="chapter-label">Speaking</div><h2 class="slide-heading">Oral <span class="accent">Practice</span></h2>
    <div class="oral-grid">
      <div class="oral-item" onclick="this.classList.toggle('revealed')"><div class="oral-situation">1. React with interest.</div><div class="oral-model">"Oh, really? That is interesting!"</div></div>
      <div class="oral-item" onclick="this.classList.toggle('revealed')"><div class="oral-situation">2. Ask what kind of company it is.</div><div class="oral-model">"What kind of company is it?"</div></div>
      <div class="oral-item" onclick="this.classList.toggle('revealed')"><div class="oral-situation">3. Ask how long they worked there.</div><div class="oral-model">"How long did you work there?"</div></div>
      <div class="oral-item" onclick="this.classList.toggle('revealed')"><div class="oral-situation">4. Ask for one more detail.</div><div class="oral-model">"Can you tell me more about it?"</div></div>
      <div class="oral-item" onclick="this.classList.toggle('revealed')"><div class="oral-situation">5. Show you are curious.</div><div class="oral-model">"I am really curious about this topic."</div></div>
      <div class="oral-item" onclick="this.classList.toggle('revealed')"><div class="oral-situation">6. Close in a friendly way.</div><div class="oral-model">"It was great talking to you. Let us keep in touch!"</div></div>
    </div>
  </div>
</div>

<div class="slide slide-light" data-slide="25" data-phase="5" data-teacher="<strong>Sentence Building (4 min):</strong> Leia cada frase errada em voz alta. Daniela corrige oralmente. Clique para revelar. Foco: question forms e interested/interesting.">
  <div class="slide-inner"><div class="chapter-label">Build</div><h2 class="slide-heading">Fix and <span class="accent">Improve</span></h2><p style="font-size:.92rem;color:var(--text-dim);margin-bottom:1rem">Make these sentences correct:</p>
    <div class="fill-grid">
      <div class="fill-item" onclick="revealFill(this)"><div class="fill-text">"What you do?" &#10132; "<span class="fill-blank">___</span><span class="fill-answer">What kind of work do you do?</span>"</div></div>
      <div class="fill-item" onclick="revealFill(this)"><div class="fill-text">"I am interesting in it." &#10132; "<span class="fill-blank">___</span><span class="fill-answer">I am interested in it.</span>"</div></div>
      <div class="fill-item" onclick="revealFill(this)"><div class="fill-text">"How long you work there?" &#10132; "<span class="fill-blank">___</span><span class="fill-answer">How long did you work there?</span>"</div></div>
    </div>
  </div>
</div>

<div class="slide slide-light" data-slide="26" data-phase="5" data-teacher="<strong>Review (2 min):</strong> 'Let us compare Lesson 7 and Lesson 8.' Explique: Lesson 7 = tell YOUR story (past simple). Lesson 8 = keep THEIR story going (react + follow-up). Both make you a great networker!">
  <div class="slide-inner"><div class="chapter-label">Compare</div><h2 class="slide-heading">Lesson 7 vs <span class="accent">Lesson 8</span></h2>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;margin-top:1.5rem">
      <div style="padding:1.5rem;background:rgba(91,155,213,.08);border:2px solid rgba(91,155,213,.2);border-radius:12px"><h3 style="font-family:'Cormorant Garamond',serif;color:var(--pharma-blue);font-size:1.2rem;margin-bottom:.8rem">Lesson 7: Tell Your Story</h3><p style="font-size:.9rem;line-height:1.6">Talk about what YOU did (past simple)</p><p style="font-size:.9rem;color:var(--pharma-blue);font-weight:600;margin-top:.5rem">"Last year, we launched a new system."</p></div>
      <div style="padding:1.5rem;background:var(--accent-dim);border:2px solid rgba(13,115,119,.2);border-radius:12px"><h3 style="font-family:'Cormorant Garamond',serif;color:var(--accent);font-size:1.2rem;margin-bottom:.8rem">Lesson 8: Keep It Going</h3><p style="font-size:.9rem;line-height:1.6">React to THEIR story and ask for more</p><p style="font-size:.9rem;color:var(--accent);font-weight:600;margin-top:.5rem">"Oh, really? What kind of system?"</p></div>
    </div>
  </div>
</div>

<div class="slide slide-light" data-slide="27" data-phase="5" data-teacher="<strong>Mixed Practice (3 min):</strong> Misture contar a própria história (Aula 7) e manter a conversa do outro (Aula 8). Leia situações e Daniela escolhe a frase certa. Celebre.">
  <div class="slide-inner"><div class="chapter-label">Mixed Practice</div><h2 class="slide-heading">Tell or <span class="accent">Keep Going</span>?</h2>
    <div class="fill-grid">
      <div class="fill-item" onclick="revealFill(this)"><div class="fill-text">Tell your own story: "<span class="fill-blank">___</span><span class="fill-answer">Last year, I launched a new system.</span>"</div></div>
      <div class="fill-item" onclick="revealFill(this)"><div class="fill-text">React to their story: "<span class="fill-blank">___</span><span class="fill-answer">Oh, really? That is interesting!</span>"</div></div>
      <div class="fill-item" onclick="revealFill(this)"><div class="fill-text">Ask a follow-up: "<span class="fill-blank">___</span><span class="fill-answer">What kind of system was it?</span>"</div></div>
      <div class="fill-item" onclick="revealFill(this)"><div class="fill-text">Keep it going: "<span class="fill-blank">___</span><span class="fill-answer">Tell me more about the result.</span>"</div></div>
    </div>
  </div>
</div>

<!-- ===== CHAPTER 6: YOUR TURN (slides 28-32) ===== -->

<div class="slide slide-image" data-slide="28" data-phase="6" data-teacher="<strong>Transição:</strong> 'From guided to free — now keep a real conversation alive!' Avance." style="background-image:url('https://images.unsplash.com/photo-1543269865-cbf427effbad?w=1400&q=80')">
  <div class="slide-inner"><div class="chapter-label">Chapter 6: Production</div><h2 class="slide-title">Keep It <span class="accent">Going</span></h2><p class="slide-subtitle">Three levels of practice — guided, semi-free, and free</p></div>
</div>

<div class="slide slide-light" data-slide="29" data-phase="6" data-teacher="<strong>Role-Play Guided (5 min):</strong> Você é Sophie, uma nova contato no coffee break. Diga: 'I work in logistics. Last month we opened a new center.' Daniela mantém a conversa usando os chips. Se travar: 'Use the chips — start with Oh, really?...' <strong>Obstáculo:</strong> se Daniela só responder sobre si, lembre: 'Ask ME a follow-up question!'">
  <div class="slide-inner"><div class="chapter-label">Role-Play</div><h2 class="slide-heading">Role-Play: <span class="accent">The Coffee Break</span></h2>
    <div class="roleplay-card"><div style="width:100%;height:180px;background:linear-gradient(135deg,#0d7377,#14919b);display:flex;align-items:center;justify-content:center"><svg width="80" height="80" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,.6)" stroke-width="1.2"><path d="M18 8h1a4 4 0 010 8h-1"/><path d="M2 8h16v9a4 4 0 01-4 4H6a4 4 0 01-4-4z"/><line x1="6" y1="1" x2="6" y2="4"/><line x1="10" y1="1" x2="10" y2="4"/><line x1="14" y1="1" x2="14" y2="4"/></svg></div>
      <div class="roleplay-body"><div class="roleplay-scenario">A new contact tells you about their job and a recent project. Keep the conversation going: react, ask follow-up questions, and ask for one more detail.</div><div class="roleplay-keywords"><span class="roleplay-kw">Oh, really?</span><span class="roleplay-kw">what kind of</span><span class="roleplay-kw">how long</span><span class="roleplay-kw">tell me more</span><span class="roleplay-kw">interested</span><span class="roleplay-kw">one more detail</span></div></div>
    </div>
  </div>
</div>

<div class="slide slide-light" data-slide="30" data-phase="6" data-teacher="<strong>Role-Play Semi-Free (5 min):</strong> 'You meet someone new at a conference dinner.' Você é a pessoa nova; conte algo curto e deixe Daniela puxar a conversa. Menos keywords. Anote erros — corrija DEPOIS.">
  <div class="slide-inner"><div class="chapter-label">Role-Play</div><h2 class="slide-heading">Role-Play: <span class="accent">The Conference Dinner</span></h2>
    <div class="roleplay-card"><div style="width:100%;height:180px;background:linear-gradient(135deg,#7c3aed,#a78bfa);display:flex;align-items:center;justify-content:center"><svg width="80" height="80" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,.6)" stroke-width="1.2"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/></svg></div>
      <div class="roleplay-body"><div class="roleplay-scenario">At a conference dinner, you meet someone new. Keep the conversation alive for two minutes: react, ask follow-ups, and show interest.</div><div class="roleplay-keywords"><span class="roleplay-kw">curious</span><span class="roleplay-kw">where exactly</span><span class="roleplay-kw">react</span><span class="roleplay-kw">topic</span></div></div>
    </div>
  </div>
</div>

<div class="slide slide-light" data-slide="31" data-phase="6" data-teacher="<strong>Role-Play Free (5 min):</strong> Sem keywords, sem script. 'Have a real two-minute conversation with me, like at a networking event. Keep it alive — react, ask follow-ups, show interest.' Celebre QUALQUER produção. NÃO corrija durante a fala.">
  <div class="slide-inner"><div class="chapter-label">Free Practice</div><h2 class="slide-heading">Role-Play: <span class="accent">Real Networking</span></h2>
    <div class="roleplay-card"><div style="width:100%;height:180px;background:linear-gradient(135deg,#0d7377,#0891b2);display:flex;align-items:center;justify-content:center"><svg width="80" height="80" viewBox="0 0 24 24" fill="none" stroke="rgba(255,255,255,.6)" stroke-width="1.2"><path d="M21 11.5a8.38 8.38 0 01-.9 3.8 8.5 8.5 0 01-7.6 4.7 8.38 8.38 0 01-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 01-.9-3.8 8.5 8.5 0 014.7-7.6 8.38 8.38 0 013.8-.9h.5a8.48 8.48 0 018 8v.5z"/></svg></div>
      <div class="roleplay-body"><div class="roleplay-scenario">Have a real networking conversation with your teacher. Keep it going for two minutes — no script.</div><p style="font-size:.85rem;color:var(--text-dim);margin-top:.8rem;font-style:italic">Use everything you learned today: react, follow-up questions (What kind of...? How long...? Where exactly...?), echo questions, and ask for one more detail.</p></div>
    </div>
  </div>
</div>

<div class="slide slide-dark" data-slide="32" data-phase="6" data-teacher="<strong>Correção Tardia (5 min):</strong> Compartilhe 3-5 erros que anotou durante os role-plays. Para cada erro: o que Daniela disse vs o que deveria ter dito. Daniela repete a versão correta 2x. Tom gentil: 'Errors with question forms are completely normal. You are doing great!'">
  <div class="slide-inner" style="text-align:center"><div class="chapter-label">Feedback</div><h2 class="slide-heading" style="color:#fff">Delayed Error <span class="accent">Correction</span></h2><p style="color:rgba(255,255,255,.6);font-size:.9rem;max-width:500px;margin:0 auto 1.5rem">Your teacher will share 3-5 corrections from the role-plays. Repeat each corrected version twice.</p>
    <div style="background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:12px;padding:1.5rem;max-width:500px;margin:0 auto"><p style="font-size:.9rem;color:rgba(255,255,255,.7);font-style:italic">Teacher notes corrections here during the role-plays...</p></div>
  </div>
</div>

<!-- ===== CHAPTER 7: WRAP-UP (slides 33-37) ===== -->

<div class="slide slide-light" data-slide="33" data-phase="7" data-teacher="<strong>Conversation Toolkit (3 min):</strong> Leia cada frase com Daniela. Ela repete. Toque o áudio. 'These 5 phrases keep any conversation alive!' Foque na entonação amigável (rising) das reações e perguntas.">
  <div class="slide-inner"><div class="chapter-label">Chapter 7: Wrap-Up</div><h2 class="slide-heading">5 Key <span class="accent">Phrases</span></h2>
    <div class="survival-grid">
      <div class="survival-item-ic"><div class="survival-num-ic">1</div><div class="survival-text-ic">"Oh, really? That is interesting!"</div><button class="audio-btn-sm" onclick="speakText('Oh, really? That is interesting!',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div>
      <div class="survival-item-ic"><div class="survival-num-ic">2</div><div class="survival-text-ic">"What kind of project was it?"</div><button class="audio-btn-sm" onclick="speakText('What kind of project was it?',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div>
      <div class="survival-item-ic"><div class="survival-num-ic">3</div><div class="survival-text-ic">"How long did it take?"</div><button class="audio-btn-sm" onclick="speakText('How long did it take?',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div>
      <div class="survival-item-ic"><div class="survival-num-ic">4</div><div class="survival-text-ic">"Wow, that sounds great! Tell me more."</div><button class="audio-btn-sm" onclick="speakText('Wow, that sounds great! Tell me more.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div>
      <div class="survival-item-ic"><div class="survival-num-ic">5</div><div class="survival-text-ic">"I am really curious about this topic."</div><button class="audio-btn-sm" onclick="speakText('I am really curious about this topic.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div>
    </div>
  </div>
</div>

<div class="slide slide-light" data-slide="34" data-lesson="8" data-phase="7" data-teacher="<strong>Checklist (3 min):</strong> Leia cada item. Pergunte: 'Can you say yes to this?' Se sim, clique o checkbox juntos. Encerre: 'Before this class, your conversations stopped. Now you can keep them alive!'">
  <div class="slide-inner" style="overflow-y:auto;max-height:75vh"><div class="chapter-label">What I Learned</div><h2 class="slide-heading">Lesson 8 <span class="accent">Checklist</span></h2>
    <div class="check-grid" id="checkGrid">
      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div>I can keep a networking conversation going.</div>
      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div>I know 8 words for active listening (follow-up, curious, nod...).</div>
      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div>I ask follow-up questions (What kind of...? How long...? Where exactly...?).</div>
      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div>I react naturally ("Oh, really?", "That is interesting!").</div>
      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div>I use echo questions (Did you? Really?) to show I am listening.</div>
      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div>I ask for one more detail to keep the topic open.</div>
      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div>I do not confuse interested (person) and interesting (topic).</div>
      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div>I feel confident turning a "hello" into a real contact.</div>
    </div>
  </div>
</div>

<div class="slide slide-dark" data-slide="35" data-phase="7" data-teacher="<strong>Badge (1 min):</strong> 'Congratulations, Daniela! You earned your Connector badge!' Celebre com entusiasmo.">
  <div class="slide-inner" style="text-align:center">
    <div class="badge-card"><div class="badge-icon"><div class="badge-circle"><svg viewBox="0 0 24 24"><path d="M21 11.5a8.38 8.38 0 01-.9 3.8 8.5 8.5 0 01-7.6 4.7 8.38 8.38 0 01-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 01-.9-3.8 8.5 8.5 0 014.7-7.6 8.38 8.38 0 013.8-.9h.5a8.48 8.48 0 018 8v.5z" fill="none" stroke="currentColor" stroke-width="1.5"/></svg></div><div class="sparkles"><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div></div></div>
      <h2 class="slide-heading" style="color:#fff">The <span class="accent">Connector</span></h2>
      <p style="color:rgba(255,255,255,.6);font-size:.9rem">Badge earned! You can keep any networking conversation alive.</p>
    </div>
  </div>
</div>

<div class="slide slide-image" data-slide="36" data-phase="7" data-teacher="<strong>Encerramento (2 min):</strong> 'Day 8 is complete! You can now keep any conversation alive!' Homework (diga ORALMENTE): 1) Gravar uma conversa de networking de 1 minuto (você reagindo e fazendo follow-ups). 2) Escrever 5 perguntas de follow-up que você usaria num evento. Não escreva na tela — só fale o homework." style="background-image:url('https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=1400&q=80')">
  <div class="slide-inner" style="text-align:center"><div class="chapter-label">Lesson Complete</div>
    <div class="badge-card"><div class="badge-icon"><div class="badge-circle"><svg viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" fill="none" stroke="currentColor" stroke-width="1.5"/></svg></div><div class="sparkles"><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div></div></div>
      <h2 class="slide-title">Day 8 — <span class="accent">Complete!</span></h2>
      <p class="slide-subtitle" style="opacity:.8;margin-top:1rem">Homework: Record a 1-min networking chat + write 5 follow-up questions</p>
      <p class="slide-subtitle" style="opacity:.6;margin-top:.5rem;font-size:.85rem">Next lesson: Asking and Answering Questions at Events</p>
    </div>
  </div>
</div>

<div class="slide slide-dark" data-slide="37" data-phase="7" data-teacher="<strong>Slide final.</strong> Encerre o compartilhamento de tela. Despeça-se com entusiasmo: 'Great conversation today, Daniela! See you next class!'">
  <div class="slide-inner" style="text-align:center"><div class="chapter-label">Thank You</div><h2 class="slide-title" style="color:#fff">See you<br><span class="accent">next class!</span></h2><p style="color:rgba(255,255,255,.5);font-size:.85rem;margin-top:1rem">Alumni by Better — Conversational English</p></div>
</div>'''

# ============================================================ ASSEMBLY
TAB1='<!-- ========== TAB 1: PLANEJAMENTO ========== -->'
TAB2='<!-- ========== TAB 2: PRE-CLASS ========== -->'
TAB3='<!-- ========== TAB 3: IN CLASS ========== -->'
TAB4='<!-- ========== TAB 4: COMPLEMENTARES ========== -->'
SLIDES_MARKER='<!-- ============================== SLIDES WRAPPER (IN CLASS) ============================== -->'
SLIDESCONT='<div class="slides-container" id="slidesContainer">'
TEACHERT='<div class="teacher-t" id="teacherT">'

def repl_between(text, a, b, mid):
    i = text.index(a) + len(a)
    j = text.index(b, i)
    return text[:i] + mid + text[j:]

def repl_audiomap(text):
    return re.sub(r'var audioMap = \{.*?\n\};', lambda m: AUDIOMAP_BLOCK, text, count=1, flags=re.S)

# header / title constants
PASS_OLD='<div class="passport-badge">Conversational English — Aula 07</div>'
PASS_NEW='<div class="passport-badge">Conversational English — Aula 08</div>'
SUB_OLD='<p class="subtitle">Past Simple: Telling Stories That Connect — contar uma história profissional de sucesso com confiança</p>'
SUB_NEW='<p class="subtitle">Networking in Action — Keeping the Conversation Going: follow-up questions, active listening e demonstrar interesse para manter qualquer conversa viva.</p>'
STAMP8_OLD='''<div class="stamp" id="stamp8" data-label="Perfect" style="background-image:url('https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=200&q=80')"></div>'''
STAMP8_NEW='''<div class="stamp" id="stamp8" data-label="Connect" style="background-image:url('https://images.unsplash.com/photo-1543269865-cbf427effbad?w=200&q=80')"></div>'''
STAMP7_OLD='''<div class="stamp" id="stamp7" data-label="Stories" style="background-image:url('https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=200&q=80')"></div>'''
STAMP7_NEW='''<div class="stamp" id="stamp7" data-label="Stories" style="background-image:url('https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=200&q=80')"></div>'''

# JS aula-specific
OLD_CHAL="""var challenges=[{prompt:'Start your story: a project you completed last year.',answer:'"Last year, we launched a new SAP system."'},{prompt:'Describe the biggest challenge.',answer:'"The biggest challenge was the tight deadline."'},{prompt:'Say how the team solved it.',answer:'"We made a clear plan and worked together."'},{prompt:'Say what the result was.',answer:'"In the end, we met the deadline."'},{prompt:'Talk about the impact.',answer:'"We improved the workflow for 200 people."'},{prompt:'End with how you felt.',answer:'"Going live was a major milestone for my team."'}];"""
NEW_CHAL="""var challenges=[{prompt:'A new contact says: "I work in marketing." React and ask a follow-up.',answer:'"Oh, really? What kind of marketing do you do?"'},{prompt:'Someone says: "We launched a new app last year." Show interest.',answer:'"Wow, that sounds great! How long did it take?"'},{prompt:'Keep the conversation going. Ask for one more detail.',answer:'"That is interesting. Can you tell me more about it?"'},{prompt:'Someone mentions a big project. React and ask about it.',answer:'"You mentioned a big project. What was the biggest challenge?"'},{prompt:'Ask where exactly their office is.',answer:'"Where exactly is your office?"'},{prompt:'End the conversation in a friendly way.',answer:'"It was great talking to you. Let us keep in touch!"'}];"""

OLD_L1="""var lines=['So Daniela, tell me about a big project you worked on last year.','Last year, we launched a new SAP system for the whole company.','That sounds big. What was the biggest challenge?','At first, the deadline was very tight. We only had three months.','Wow. How did you solve that problem?','We made a clear plan, and the team worked together every day.','And what happened in the end?','We met the deadline and improved the workflow for 200 people.','That is a great result. Did you achieve your main goal?','Yes! Going live was a major milestone. I felt very proud of my team.'];"""
NEW_L1="""var lines=['Hi! I do not think we have met. I am Sophie, from the Berlin office.','Nice to meet you, Sophie! I am Daniela, from Sao Paulo. So, what do you do in Berlin?','I work in logistics. Last month, we opened a new distribution center.','Oh, really? That is interesting! What kind of center is it?','It is fully automated. It was a big challenge, but the result was great.','Wow, that sounds great! How long did the project take?','About eight months. Honestly, the deadline was very tight.','I can imagine. You mentioned automation. Can you tell me one more detail?','Sure! The robots move the boxes, so the team works faster now.','That is amazing. I am really curious about this topic. Let us keep in touch!'];"""

OLD_L2="""var lines=['We launched a new system.','We worked together every day.','How did you solve that problem?','Did you achieve your main goal?','I felt very proud of my team.'];"""
NEW_L2="""var lines=['What kind of center is it?','How long did the project take?','Oh, really? That is interesting!','Can you tell me one more detail?','I am really curious about this topic.'];"""

def common_swaps(text):
    text = repl_audiomap(text)
    text = text.replace(PASS_OLD, PASS_NEW)
    text = text.replace(SUB_OLD, SUB_NEW)
    text = text.replace(STAMP7_OLD, STAMP7_NEW)
    text = text.replace(STAMP8_OLD, STAMP8_NEW)
    text = text.replace(OLD_CHAL, NEW_CHAL)
    text = text.replace(OLD_L1, NEW_L1)
    text = text.replace(OLD_L2, NEW_L2)
    return text

# ----- PROFESSOR -----
P = open(PROF7, encoding='utf-8').read()
P = P.replace('<title>Professor View — Daniela Feitoza | Aula 7 | Conversational English | Alumni by Better</title>',
              '<title>Professor View — Daniela Feitoza | Aula 8 | Networking in Action | Alumni by Better</title>')
P = common_swaps(P)
P = repl_between(P, TAB1, TAB2, '\n<div class="tab-content active" id="tab-planning">\n' + PLANNING_INNER + '\n</div>\n\n')
P = repl_between(P, TAB2, TAB3, '\n<div class="tab-content" id="tab-exercises">\n\n' + PRECLASS_INNER + '\n\n</div>\n\n')
P = repl_between(P, TAB3, TAB4, INCLASS_INNER + '\n')
P = repl_between(P, TAB4, SLIDES_MARKER, '\n<div class="tab-content" id="tab-complementary">\n' + COMP_INNER + '\n</div>\n\n</div>\n</div>\n\n')
P = repl_between(P, SLIDESCONT, TEACHERT, '\n\n' + SLIDES_HTML + '\n\n</div>\n</div>\n\n')
P = P.replace('aula7', 'aula8')
open(PROF8, 'w', encoding='utf-8').write(P)

# ----- ALUNO -----
A = open(ALU7, encoding='utf-8').read()
A = A.replace('<title>Aluno — Daniela Feitoza | Aula 7 | Conversational English | Alumni by Better</title>',
              '<title>Aluno — Daniela Feitoza | Aula 8 | Networking in Action | Alumni by Better</title>')
A = common_swaps(A)
A = repl_between(A, TAB2, TAB4, '\n<div class="tab-content active" id="tab-exercises">\n\n' + PRECLASS_INNER + '\n\n</div>\n\n')
A = repl_between(A, TAB4, TEACHERT, '\n<div class="tab-content" id="tab-complementary">\n' + COMP_INNER + '\n</div>\n\n</div>\n</div>\n\n')
A = A.replace('aula7', 'aula8')
open(ALU8, 'w', encoding='utf-8').write(A)

print("AUDIO unico:", len(AUDIO_U), "arquivos")
print("PROF:", PROF8)
print("ALU :", ALU8)
print("== build OK ==")


