#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 18 da Maria Clara I10 (A2, lideranca institucional & professora, Maceio).

Tema: "When Things Go Wrong -- Managing Misunderstandings, Asking for Clarification, and
Handling the Unexpected in English". Gramatica (nova, funcional): polite requests (Could
you...? / Would it be possible to...?) + apologies for problems (I'm sorry for... /
I apologize for...) + clarification/buy-time chunks (Just to make sure... / Bear with me.).
Contexto: um dia em Seul em que a reserva se perdeu, o voo foi cancelado e o cracha veio errado.

Garante:
  - REGRA 4: as 5 etapas + sub-etapas 1.1..1.5 (vocab, matching, grammar in context,
    grammar tip, fill-in-the-blank), + Stage 2 (order), 3 (pronuncia), 4 (quiz), 5 (producao)
  - REGRA 13: A2 => 8 palavras novas e ZERO portugues na tela da aluna (definicao em ingles
    simples no lugar da traducao; instrucoes, hints, quiz, grammar tip e survival todos em
    ingles). PT so onde a aluna NAO ve (data-teacher / Planejamento).
  - REGRA 22: as 8 novas (mistake, delay, cancel, apologize, solve, replace, misunderstanding,
    reservation) sao DISJUNTAS do conjunto de vocab-card-word das aulas 1-17 (verificado no hub).
    Ja em circulacao (nao ensinado como novo): clarify, confirm, unexpected, situation, urgent,
    document, available, handle, request, schedule.
  - REGRA 24: matching com opcoes EMBARALHADAS (ordem diferente por linha)
  - REGRA 29: o Pre-class PREVIEWA a aula 18 IN CLASS (mesmo tema: um dia em Seul que deu
    errado; mesmo vocab; mesma gramatica: pedidos educados + desculpas)
  - GATE botao morto (REGRA 7.1): NENHUM texto vai dentro do argumento string de um onclick.
    Todo texto falavel viaja em ATRIBUTO (data-speak / data-phrase).
  - PERFIL (colapso pro portugues sob pressao): a aula da a ela frases-reflexo em ingles para
    NAO voltar pro portugues; tom que celebra a tentativa; frase-identidade no survival card.
"""
import random

random.seed(18)

OUT = 'preclass.html'

# (word, definicao em ingles simples A2 -- a MESMA string vai no matching, exemplo real)
VOCAB = [
    ("Mistake", "something that is wrong, done by accident, not on purpose",
     "I think there might be a mistake with my reservation."),
    ("Delay", "when something happens later than the planned time",
     "There is a delay, so my flight will arrive late."),
    ("Cancel", "to stop something that was planned, so it does not happen",
     "The airline had to cancel the flight."),
    ("Apologize", "to say you are sorry for a problem or a mistake",
     "I apologize for the delay."),
    ("Solve", "to find an answer to a problem, so it is finished",
     "I can solve this problem with one polite question."),
    ("Replace", "to put a new thing in the place of another one",
     "Could you replace this badge, please?"),
    ("Misunderstanding", "when two people understand something in different ways",
     "It was a small misunderstanding about the room."),
    ("Reservation", "a room, table, or seat you booked before you arrive",
     "There is a problem with my hotel reservation."),
]

out = []
w = out.append

w('<div class="lesson-card" id="ex-lesson-18">')
w('  <div class="lesson-header" onclick="toggleLesson(this)">')
w('    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1506784983877-45594efa4cbe?w=600&q=80\')"></div>')
w('    <div class="lesson-header-content">')
w('      <div class="lesson-number">Lesson 18 -- Pre-class</div>')
w('      <h3>When Things Go Wrong -- Misunderstandings, Clarification, and the Unexpected</h3>')
w('      <div class="lesson-desc">Stay in English when a trip goes wrong. Learn <strong>polite requests</strong> '
  '(Could you check that again? / Would it be possible to change the room?), <strong>apologies for problems</strong> '
  '(I\'m sorry for the delay. / I apologize for the misunderstanding.), and the <strong>clarification and buy-time '
  'chunks</strong> that keep you from switching to Portuguese (Just to make sure... / Bear with me.). '
  'Key words: mistake, delay, cancel, apologize, solve, replace, misunderstanding, reservation. Expression: '
  '"Just to make sure..." Idiom of the lesson: "Bear with me."</div>')
w('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="18" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="18">0%</span></div>')
w('    </div>')
w('    <div class="expand-icon">&#9660;</div>')
w('  </div>')
w('  <div class="lesson-body">')
w('')

# ---------------------------------------------------------------- Stage 1.1
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each word and read the example. These are the eight words for a day when things go wrong.</p>')
w('      <div class="vocab-cards">')
for word, dfn, ex in VOCAB:
    w(f'        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header">'
      f'<span class="vocab-card-word">{word}</span><span class="vocab-card-dot"> -- </span>'
      f'<span class="vocab-card-def">{dfn}</span></div>'
      f'<div class="vocab-card-example">"{ex}"</div></div>'
      f'<button class="audio-btn" data-speak="{word}" onclick="speakText(this.dataset.speak,this)">Listen</button></div>')
w('      </div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.2 (REGRA 24)
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each word with its definition.</p>')
w('      <div class="match-grid" id="match-l18">')
all_defs = [d for _, d, _ in VOCAB]
for word, dfn, _ex in VOCAB:
    opts = all_defs[:]
    while True:
        random.shuffle(opts)
        if opts != all_defs:
            break
    o = ''.join(f'<option value="{d}">{d}</option>' for d in opts)
    w(f'        <div class="match-row" data-answer="{dfn}">'
      f'<span class="match-word" style="flex:0 0 150px">{word}</span>'
      f'<select style="flex:1;width:100%" onchange="checkMatch(this)">'
      f'<option value="">Select...</option>{o}</select></div>')
w('      </div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.3
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text and answer the questions.</p>')
w('      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">')
w('        <p>Maria Clara arrives at her hotel in Seoul. Her name is not on the list, and there is a problem with her '
  '<strong>reservation</strong>. For a second, she wants to switch to Portuguese. Instead, she stays calm and says, '
  '"I think there might be a <strong>mistake</strong>. <strong>Could you</strong> check again, please?" The receptionist '
  'checks: the date is wrong. "I\'m <strong>sorry for</strong> the <strong>misunderstanding</strong>," he says. '
  '"<strong>Would it be possible to</strong> give me a room for tonight?" she asks. The problem is <strong>solved</strong>. '
  'The next day, the interpreter\'s flight is <strong>delayed</strong> and then the airline <strong>cancels</strong> it, '
  'and the conference desk gives her the wrong badge. "Just to make sure," she says, "could you <strong>replace</strong> '
  'this badge?" She did not need perfect English. She needed calm English, and she solved every problem, one polite '
  'question at a time.</p>')
w('      </div>')
w('      <div class="quiz-item"><div class="quiz-question">1. She says "<strong>Could you</strong> check again, please?" Why "Could you"?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Because <strong>Could you + verb</strong> is a polite request, not an order.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Because "check" is a difficult word.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because the sentence is in the past.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">2. The receptionist says "I\'m <strong>sorry for</strong> the misunderstanding." What is this?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> A question about the room.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> An apology: <strong>I\'m sorry for + noun</strong>.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> An order to leave the hotel.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">3. She asks "<strong>Would it be possible to</strong> give me a room?" This is:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> A rude order.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> A very polite request: <strong>Would it be possible to + verb</strong>.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> A way to say goodbye.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">4. Which sentence is correct?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "You repeat that? Sorry the delay."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Could you repeat that, please? I\'m sorry for the delay."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Would you possible change? I apologize the mistake."</div>'
  '</div></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.4
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Asking, Apologizing, and Clarifying</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">When something goes wrong, English gives you three tools: a polite <strong>request</strong>, an <strong>apology</strong>, and a way to <strong>clarify</strong> or buy time. This is the map.</p>')
w('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
w('        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">When you want to...</th><th style="padding:.7rem;text-align:left">Structure</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>')
w('        <tbody>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Ask politely</td>'
  '<td style="padding:.6rem"><strong>Could you</strong> + base verb...?</td>'
  '<td style="padding:.6rem"><strong>Could you check</strong> the list again?</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Ask if it is possible</td>'
  '<td style="padding:.6rem"><strong>Would it be possible to</strong> + base verb...?</td>'
  '<td style="padding:.6rem"><strong>Would it be possible to change</strong> the room?</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Say you are sorry</td>'
  '<td style="padding:.6rem"><strong>I\'m sorry for</strong> / <strong>I apologize for</strong> + noun</td>'
  '<td style="padding:.6rem"><strong>I\'m sorry for the delay.</strong> &middot; <strong>I apologize for the mistake.</strong></td></tr>')
w('          <tr><td style="padding:.6rem;font-weight:600">Clarify / buy time</td>'
  '<td style="padding:.6rem"><strong>Could you repeat that?</strong> &middot; <strong>Just to make sure...</strong> &middot; <strong>Bear with me.</strong></td>'
  '<td style="padding:.6rem"><strong>Could you say that again, please?</strong></td></tr>')
w('        </tbody>')
w('      </table></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Common mistake:</strong> '
  'many people say <strong>"Repeat that?"</strong> or <strong>"I want change the room."</strong> or <strong>"Sorry the delay."</strong>. '
  'The polite forms are <strong>Could you repeat that, please?</strong>, <strong>Would it be possible to change the room?</strong>, '
  'and <strong>I\'m sorry for the delay.</strong> Asking someone to repeat is not weak &mdash; it keeps you in English.</p>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.5
BLANKS = [
    ("could", "Hint: a polite request starts with Could you + verb",
     "Could you check the list again, please?",
     '"', ' you check the list again, please?"'),
    ("possible", "Hint: Would it be possible to + verb",
     "Would it be possible to change the room?",
     '"Would it be ', ' to change the room?"'),
    ("sorry", "Hint: to apologize, say I'm sorry for + noun",
     "I'm sorry for the delay.",
     '"I\'m ', ' for the delay."'),
    ("apologize", "Hint: I apologize for + noun",
     "I apologize for the misunderstanding.",
     '"I ', ' for the misunderstanding."'),
    ("sure", "Hint: Just to make sure... opens a careful check",
     "Just to make sure, could you repeat that?",
     '"Just to make ', ', could you repeat that?"'),
    ("replace", "Hint: to put a new one in place of the wrong one",
     "Could you replace this badge, please?",
     '"Could you ', ' this badge, please?"'),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence to make a polite request or an apology. Tap Listen to hear the full sentence.</p>')
for ans, hint, phrase, pre, post in BLANKS:
    w(f'      <div class="fill-blank-item"><div class="fill-blank-sentence">{pre}'
      f'<input class="blank-input" data-answer="{ans}" data-hint="{hint}" data-phrase="{phrase}" placeholder="___">'
      f'{post}</div>'
      f'<button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>'
      f'<button class="check-btn" onclick="checkBlank(this)">Check</button></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 2 (order)
ORDER = [
    (1, "Excuse me, I think there might be a mistake."),
    (2, "Could you check my reservation again, please?"),
    (3, "I'm sorry, could you say that again?"),
    (4, "Would it be possible to give me a room for tonight?"),
    (5, "Thank you very much. That solves it."),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 2: Put the Repair in Order</h4><span class="badge badge-order">Order</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the sentences in order, from the problem to the solution, at the hotel front desk.</p>')
w('      <div class="order-container" id="order-l18">')
shuffled = ORDER[:]
random.shuffle(shuffled)
for n, text in shuffled:
    w(f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l18\')">'
      f'<span class="order-num">?</span><span class="order-text">{text}</span>'
      f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l18\')">&#9650;</button>'
      f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l18\')">&#9660;</button></span></div>')
w('      </div>')
w('      <button class="verify-all-btn" onclick="checkOrder(\'order-l18\')">Check Order</button>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 3 (pronuncia)
SPEECH = [
    "I think there might be a mistake. Could you check again, please?",
    "I'm sorry -- could you say that again?",
    "Would it be possible to change the room?",
    "I'm sorry for the delay. My flight was cancelled.",
    "I do not need perfect English. I need calm English.",
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence and then record yourself saying it. There is no wrong way to try &mdash; the last one is your phrase: say it out loud, and mean it.</p>')
for en in SPEECH:
    w(f'      <div class="speech-card" data-phrase="{en}">')
    w(f'        <div class="speech-phrase">{en}</div>')
    w('        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button>'
      '<button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button>'
      '<button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>')
    w('        <div class="speech-result"></div>')
    w('      </div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 4 (quiz situacional)
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each moment when something goes wrong.</p>')
w('      <div class="quiz-item"><div class="quiz-question">Your name is not on the hotel list. You say:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Your list is wrong. Fix it now."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I think there might be a mistake. Could you check again, please?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> (Say nothing and switch to Portuguese.)</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">The coordinator speaks too fast and you do not understand. You say:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Repeat that."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I\'m sorry -- could you speak more slowly, please?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I no understand you."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">You want to ask for a different room. You say:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I want change the room."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Change the room for me."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> "Would it be possible to change the room?"</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">Your flight was cancelled and you arrive late. You say:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "I\'m sorry for the delay. My flight was cancelled."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Sorry the delay. Flight cancel."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "It is not my problem."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">You need a few seconds to find the English words. You say:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> (Stay silent for a long time.)</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Bear with me, please. Just to make sure I understand..."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Wait, wait, I speak Portuguese now."</div>'
  '</div></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 5 (producao livre)
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. There is no right or wrong answer &mdash; speak for one or two minutes, with no script. Every attempt counts.</p>')
w('      <div class="think-card">')
w('        <div class="think-question">Imagine you arrive at your hotel in Seoul and your <strong>reservation</strong> is not on the '
  'list. Tell the story out loud: what is the problem, and what do you say to <strong>solve</strong> it? Use <strong>Could you...?</strong>, '
  '<strong>Would it be possible to...?</strong>, and an apology if you need one (<strong>I\'m sorry for...</strong>). If you feel lost, '
  'use <strong>"Bear with me"</strong> or <strong>"Just to make sure..."</strong> &mdash; and stay in English. Take your time.</div>')
w('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button>'
  '<button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>')
w('        <div id="think-result-18"></div>')
w('      </div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Survival card
w('    <div class="survival-card">')
w('      <h4>Survival Card -- Lesson 18</h4>')
for i, en in enumerate(SPEECH, 1):
    w(f'      <div class="survival-phrase"><span class="sp-num">{i}</span>'
      f'<span class="sp-en">{en}</span>'
      f'<button class="btn btn-listen" data-speak="{en}" onclick="speakText(this.dataset.speak,this)">&#9835;</button></div>')
w('    </div>')
w('')
w('  </div>')
w('</div>')

with open(OUT, 'w', encoding='utf-8') as f:
    f.write('\n'.join(out) + '\n')
print(f'wrote {OUT} ({len(VOCAB)} vocab, {len(BLANKS)} blanks, {len(SPEECH)} speech cards)')
