#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 4 da Emmanuele Orrico (A2, Gerente Nacional de Demanda -- Sanofi).

Garante:
  - REGRA 4: as 5 etapas + sub-etapas 1.1..1.5 (vocab, matching, grammar in context,
    grammar tip, fill-in-the-blank), + Stage 2 (order), 3 (pronuncia), 4 (quiz), 5 (producao)
  - REGRA 13: A2 => 10 palavras novas, ZERO portugues na tela da aluna (definicao em
    ingles simples no lugar da traducao; hint, instrucao, grammar tip e quiz em ingles).
    O portugues sobrevive SO onde a aluna nao ve (data-teacher / Planejamento).
  - REGRA 22: ZERO palavra das aulas 1, 2 e 3 como vocab NOVO. Fora, de proposito:
    pharmaceutical company / immunology / national manager / field team / global meeting /
    results / launch / disease area / to be responsible for / to manage / schedule / report /
    field visit / medical rep / demand plan / headquarters / to attend / to review /
    to prepare / to travel / quarter / target / challenge / opportunity / growth /
    to achieve / to exceed / to miss / market access / prescription volume
  - REGRA 24: matching com opcoes EMBARALHADAS (ordem diferente por linha)
  - REGRA 29: o Pre-class PREVIEWA a aula 4 IN CLASS (mesmo tema: small talk no jantar/
    congresso do time Global; mesmo vocab; mesma gramatica: present continuous x present simple)
  - GATE botao morto (REGRA 7.1): NENHUM texto vai dentro do argumento string de um
    onclick. Todo texto falavel viaja em ATRIBUTO (data-speak / data-phrase).
  - NUNCA nomear "verbo to be" (palavra proibida com ela): a estrutura e apresentada como
    DUAS PECAS -- am / is / are + verbo-ING.
"""
import random

random.seed(4)

OUT = 'preclass.html'

# (word, definicao EN (curta, usada no matching), exemplo)
VOCAB = [
    ("Small talk", "easy, friendly conversation before the real business starts",
     "The dinner is two hours of small talk."),
    ("Congress", "a big professional event where doctors and companies meet",
     "I go to the immunology congress every year."),
    ("Colleague", "a person who works with you, in your company or in another one",
     "I met a colleague from the French team."),
    ("Executive", "a senior leader who makes the big decisions in a company",
     "The executives from Paris are at the dinner."),
    ("Stakeholder", "a person or a group with an interest in your project",
     "Doctors and payers are our main stakeholders."),
    ("Pipeline", "the new medicines a company is developing, before they reach the market",
     "We have three new products in the pipeline."),
    ("To introduce", "to say who you are, or to present one person to another",
     "Let me introduce myself: I am Emmanuele."),
    ("To network", "to meet new people at an event and build professional contacts",
     "I network at every congress."),
    ("Currently", "now, in this period -- not every day, but at this moment in your life",
     "I am currently working on the asthma launch."),
    ("To look forward to", "to feel happy about something that is coming",
     "I am looking forward to the congress."),
]

out = []
w = out.append

w('<div class="lesson-card" id="ex-lesson-4">')
w('  <div class="lesson-header" onclick="toggleLesson(this)">')
w('    <div class="lesson-header-img" style="background-image:url(\'https://images.unsplash.com/photo-1543269865-cbf427effbad?w=600&q=80\')"></div>')
w('    <div class="lesson-header-content">')
w('      <div class="lesson-number">Lesson 04 -- Pre-class</div>')
w('      <h3>Breaking the Ice -- Small Talk at a Global Event</h3>')
w('      <div class="lesson-desc">The dinner before your presentation: how to open a conversation with a person you '
  'do not know, say in one sentence what you are doing NOW, and keep the conversation alive to the end. Key words: small talk, '
  'congress, colleague, executive, stakeholder, pipeline, to introduce, to network, currently, to look forward to. '
  'Structures: present continuous &mdash; am / is / are + verb-ING for what happens NOW (I am currently working on...), '
  'next to the present simple for what is always true (I work in immunology), plus the key question at the table: '
  '"What are you working on at the moment?" Expression of the lesson: "I am looking forward to working with your team."</div>')
w('      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="4" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="4">0%</span></div>')
w('    </div>')
w('    <div class="expand-icon">&#9660;</div>')
w('  </div>')
w('  <div class="lesson-body">')
w('')

# ---------------------------------------------------------------- Stage 1.1
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each word and read the example. These are the ten words of the dinner table and the congress hallway &mdash; none of them is on a results slide.</p>')
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
w('      <div class="match-grid" id="match-l4">')
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
w('        <p>It is the first evening of the <strong>congress</strong>, and Emmanuele is at the dinner table. She <strong>works</strong> '
  'in immunology &mdash; that is her job, and it does not change. But tonight nobody asks about her job. An <strong>executive</strong> '
  'from Paris turns to her and asks: "What <strong>are</strong> you <strong>working</strong> on at the moment?"</p>')
w('        <p style="margin-top:.8rem">Emmanuele breathes. "I am <strong>currently working</strong> on the immunology portfolio. Right now, my team '
  '<strong>is preparing</strong> a launch, and my field team <strong>is visiting</strong> the big centers." The executive smiles. "We '
  '<strong>are watching</strong> Brazil very closely this year," he says. "And I <strong>am looking</strong> at the <strong>pipeline</strong> '
  'for next year &mdash; two new molecules."</p>')
w('        <p style="margin-top:.8rem">She <strong>is not selling</strong> anything tonight. She is <strong>networking</strong>: she '
  '<strong>is meeting</strong> <strong>colleagues</strong> and <strong>stakeholders</strong> from twenty-two countries. And when the '
  'conversation ends, she says the sentence she practiced: "I am <strong>looking forward to</strong> working with your team." Tomorrow, '
  'in the meeting room, they already know her name.</p>')
w('      </div>')
w('      <div class="quiz-item"><div class="quiz-question">1. Why does she say "I <strong>am working</strong> on the portfolio" and not "I work on the portfolio"?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Because it is the project of THIS moment &mdash; it started and it will finish. NOW, not always.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Because the action finished last quarter.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because "portfolio" is a plural word.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">2. In the same text she says "She <strong>works</strong> in immunology". Why does this sentence take NO -ING?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because it is a negative sentence.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Because it is her job &mdash; always true, and it does not change next month. That is present simple.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because the subject is "she", and after "she" the -ING never comes.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">3. "My team <strong>is preparing</strong> a launch." Why is it NOT "My team preparing a launch"?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because "team" is plural and needs "are".</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Because the structure ALWAYS has two pieces: <strong>am / is / are</strong> + verb-<strong>ING</strong>. Without the first piece, the sentence breaks.</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because "prepare" is an irregular verb.</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">4. Which question is correct at the dinner table?</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "What you are working on at the moment?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "What are you working on at the moment?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "What are you work on at the moment?"</div>'
  '</div></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.4
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- What you are doing NOW: am / is / are + verb-ING</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">At a business dinner, the question is about NOW, not about always. This is how English shows the now.</p>')
w('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
w('        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Structure</th><th style="padding:.7rem;text-align:left">Use</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>')
w('        <tbody>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">I <strong>am</strong> / she <strong>is</strong> / we <strong>are</strong> + verb-<strong>ING</strong></td>'
  '<td style="padding:.6rem">The project of NOW: this week, this month, this year. It started and it will finish.</td>'
  '<td style="padding:.6rem">I <strong>am working</strong> on the launch. / My team <strong>is preparing</strong> the congress.</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Always <strong>TWO pieces</strong>, never one</td>'
  '<td style="padding:.6rem">You need both: <strong>am</strong> + <strong>working</strong>. Take one piece away and the sentence breaks.</td>'
  '<td style="padding:.6rem">We <strong>are launching</strong> a product. (never "we launching", never "we are launch")</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Negative: <strong>am not</strong> / <strong>is not</strong> + verb-ING</td>'
  '<td style="padding:.6rem">To say what is NOT happening now.</td>'
  '<td style="padding:.6rem">I <strong>am not working</strong> on that project this year.</td></tr>')
w('          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Question: <strong>What are you working on?</strong></td>'
  '<td style="padding:.6rem">The question at the table. Learn it as one block &mdash; do not build it word by word. Note that <strong>are</strong> and <strong>you</strong> change places.</td>'
  '<td style="padding:.6rem"><strong>What are you working on</strong> at the moment?</td></tr>')
w('          <tr><td style="padding:.6rem;font-weight:600">Always (present simple) x Now (-ING)</td>'
  '<td style="padding:.6rem" colspan="2">I <strong>work</strong> in immunology = my job, it does not change &middot; I <strong>am working</strong> on the asthma launch = this month, it will finish. The words that ask for the -ING: <strong>right now</strong>, <strong>currently</strong>, <strong>at the moment</strong>, <strong>this month</strong>.</td></tr>')
w('        </tbody>')
w('      </table></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Careful (a common mistake):</strong> '
  'in your language, one verb can say both things &mdash; the always and the now. In English it cannot. If you say '
  '"I work on the asthma launch" at the dinner, the executive hears that you do this every year and you always will. '
  'For the project of THIS month, English needs the two pieces: <strong>I am working on the asthma launch</strong>. '
  'The other mistake is to forget the first piece and say "I working on..." &mdash; in English, that is not a sentence.</p>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 1.5
BLANKS = [
    ("am working", "Hint: TWO pieces -- am + the verb with -ING",
     "I am currently working on the immunology portfolio.",
     '"I am currently ', ' on the immunology portfolio." (work)'),
    ("is preparing", "Hint: TWO pieces -- is + the verb with -ING (my team = one thing)",
     "This month, my team is preparing the congress.",
     '"This month, my team ', ' the congress." (prepare)'),
    ("work", "Hint: always true -- her job does not change. No -ING.",
     "I work in immunology.",
     '"I ', ' in immunology." (work -- always true)'),
    ("are launching", "Hint: TWO pieces -- are + the verb with -ING",
     "We are launching a new product in Brazil this month.",
     '"We ', ' a new product in Brazil this month." (launch)'),
    ("are you working", "Hint: in the question, are and you change places",
     "What are you working on at the moment?",
     '"What ', ' on at the moment?" (work)'),
    ("am looking forward", "Hint: the expression of the lesson -- am + look with -ING",
     "I am looking forward to working with your team.",
     '"I ', ' to working with your team." (look forward)'),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the correct form of the verb in parentheses. Careful: one of them is always true and takes NO -ING. Tap Listen to hear the full sentence.</p>')
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
    (1, "Hello. I do not think we have met. I am Emmanuele Orrico, from Sanofi Brazil."),
    (2, "It is great to finally meet you in person."),
    (3, "I am currently working on the immunology portfolio."),
    (4, "And you? What are you working on at the moment?"),
    (5, "That is very interesting. I am looking forward to hearing more about it tomorrow."),
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 2: Put the Conversation in Order</h4><span class="badge badge-order">Order</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the dinner conversation in the correct order: from the introduction to the closing.</p>')
w('      <div class="order-container" id="order-l4">')
shuffled = ORDER[:]
random.shuffle(shuffled)
for n, text in shuffled:
    w(f'        <div class="order-item" draggable="true" data-order="{n}" onclick="selectOrderItem(this,\'order-l4\')">'
      f'<span class="order-num">?</span><span class="order-text">{text}</span>'
      f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l4\')">&#9650;</button>'
      f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l4\')">&#9660;</button></span></div>')
w('      </div>')
w('      <button class="verify-all-btn" onclick="checkOrder(\'order-l4\')">Check Order</button>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 3 (pronuncia)
SPEECH = [
    "Hello. I do not think we have met. I am Emmanuele, from Sanofi Brazil.",
    "It is great to finally meet you in person.",
    "I am currently working on the immunology portfolio.",
    "And you? What are you working on at the moment?",
    "I am looking forward to working with your team.",
]
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it. These are the five sentences of the dinner. Careful: <strong>colleague</strong> has two syllables (KOL-eeg) and <strong>executive</strong> has the stress on the second one (eg-ZEK-yu-tiv).</p>')
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
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each real moment of the dinner with the Global team.</p>')
w('      <div class="quiz-item"><div class="quiz-question">You are alone in the coffee line. An executive you have never seen is next to you. You open the conversation with:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Excuse me, sorry, my English is very bad."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Hello. I do not think we have met. I am Emmanuele, from Sanofi Brazil."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Who are you and what is your function in the company?"</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">He asks: "What are you working on at the moment?" The best answer is:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I working on the immunology portfolio."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "I am work on the immunology portfolio."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> "I am currently working on the immunology portfolio. Right now, my team is preparing a launch."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">You want to say what is ALWAYS true &mdash; your area, your job title. You say:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "I work in immunology. I am the National Demand Manager."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "I am working in immunology since always."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I am work in immunology every day."</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">Now you want to ask him the same question. The correct form is:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "And you? What you are working on?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "And you? What are you working on at the moment?"</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "And you? What are you work on?"</div>'
  '</div></div>')
w('      <div class="quiz-item"><div class="quiz-question">The conversation is ending and you want to meet this person again tomorrow. You close with:</div>'
  '<div class="quiz-options">'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Ok. Bye bye. Finish."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "It was great to meet you. I am looking forward to working with your team."</div>'
  '<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I am looking forward to work with your team yesterday."</div>'
  '</div></div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Stage 5 (producao livre)
w('    <div class="exercise-section">')
w('      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>')
w('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the situation below. There is no right or wrong answer &mdash; speak for two minutes, with no script.</p>')
w('      <div class="think-card">')
w('        <div class="think-question">It is August, and you are at the dinner with the Global team. An executive from Paris sits down next to you. '
  'Nobody introduces you &mdash; you start. In this order: (1) introduce yourself (name, company, and what you do &mdash; the things that are '
  'always true); (2) say what you are working on RIGHT NOW (use "I am currently working on..." and one sentence about what your team is '
  'preparing this month); (3) ask the other person what they are working on; (4) react to the answer ("That is very interesting"); and '
  '(5) close the conversation with the expression of the lesson: "I am looking forward to..." Speak for two minutes. Do not read from a script.</div>')
w('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button>'
  '<button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>')
w('        <div id="think-result-4"></div>')
w('      </div>')
w('    </div>')
w('')

# ---------------------------------------------------------------- Survival card
w('    <div class="survival-card">')
w('      <h4>Survival Card -- Lesson 4</h4>')
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
