#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aba "Atividades Extras" da Helena Andrade (PS-ASON), 28/09/2026.

POR QUE EXISTE. A professora pediu nivel mais baixo e foco em reading/writing, e a Helen
pediu uma aba extra focada nos gaps que as analises de aula (Zoom, analises 960, 1544 e
1688) mostraram:
  1. palavras nauticas confundidas pelo som: berth/birth, moored/murdered, bow/ball,
     adrift/aground, bridge/breed, told/tore, ship/chip;
  2. vocabulario de posicao do navio: anchorage, roadstead, berth, aground, adrift, bow,
     stern, starboard, port side, list;
  3. voz passiva escrita (the work was STOPPED, nao "was stoppage");
  4. passado simples e padroes verbais (nobody SAW, described it AS, reported it TO);
  5. mini-textos no formato da prova, com distrator de sinonimo (adequate/sufficient);
  6. numeros de relatorio: horario 24h, graus, milhas.

REGRAS QUE ESTE ARQUIVO SEGUE
- Tudo de resposta fechada (A/B/C ou completar): ela trava em resposta aberta.
- Ids proprios `xa-` (fora do updateProgress: a barra e os stamps das aulas nao mudam).
- So chama funcao que o hub ja tem (toggleLesson, selectQuiz, checkBlank, listenBlank,
  checkMatch, verifyAllMatches). O insert_hub_extras recusa qualquer outra.
- Pergunta de quiz comeca com um rotulo proprio (S1., P2., A1. ...): o loadState casa quiz
  pelos 30 primeiros caracteres, e "According to the text..." ja existe nas aulas.
- A resposta correta nunca fica na mesma posicao em sequencia.

USO:  python3 build_extras.py      (escreve atividades.html ao lado)
"""
import os

AQUI = os.path.dirname(os.path.abspath(__file__))
IMG = 'https://images.unsplash.com/photo-'


def esc(t):
    return (t.replace('&', '&amp;').replace('"', '&quot;')
             .replace('<', '&lt;').replace('>', '&gt;'))


def quiz(items):
    out = ''
    for q, opts, certa in items:
        o = ''.join(
            f'<div class="quiz-option" onclick="selectQuiz(this)" data-correct="{str(j == certa).lower()}">'
            f'<span class="option-letter">{"ABCDE"[j]}</span> {t}</div>\n'
            for j, t in enumerate(opts))
        out += (f'      <div class="quiz-item"><div class="quiz-question">{q}</div>'
                f'<div class="quiz-options">\n{o}</div></div>\n')
    return out


def blanks(items):
    out = ''
    for antes, resp, depois, dica in items:
        frase = f'{antes}{resp}{depois}'
        out += (f'      <div class="fill-blank-item"><div class="fill-blank-sentence">&quot;{antes}'
                f'<input class="blank-input" data-answer="{esc(resp)}" data-hint="{esc(dica)}" '
                f'data-phrase="{esc(frase)}" placeholder="___">{depois}&quot;</div>'
                f'<button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>'
                f'<button class="check-btn" onclick="checkBlank(this)">Check</button></div>\n')
    return out


def matching(gid, pares, giro=4):
    defs = [d for _, d in pares]
    k = giro % len(defs) or 1
    opcoes = defs[k:] + defs[:k]
    rows = ''
    for w, d in pares:
        o = ''.join(f'<option value="{esc(x)}">{x}</option>' for x in opcoes)
        rows += (f'        <div class="match-row" data-answer="{esc(d)}">'
                 f'<span class="match-word" style="flex:0 0 150px">{w}</span>'
                 f'<select style="flex:1;width:100%" onchange="checkMatch(this)">'
                 f'<option value="">Select...</option>{o}</select></div>\n')
    return (f'      <div class="match-grid" id="{gid}">\n{rows}      </div>\n'
            f'      <button class="verify-all-btn" onclick="verifyAllMatches(\'{gid}\')">Check Answers</button>\n')


def secao(titulo, badge_cls, badge, lead, corpo):
    return (f'    <div class="exercise-section">\n'
            f'      <div class="section-header-row"><h4>{titulo}</h4>'
            f'<span class="badge {badge_cls}">{badge}</span></div>\n'
            f'      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">{lead}</p>\n'
            f'{corpo}    </div>\n')


def texto(titulo, paras):
    ps = ''.join(('<p style="margin-top:.7rem">' if i else '<p>') + p + '</p>'
                 for i, p in enumerate(paras))
    return (f'      <div style="background:var(--bg-card);border:1px solid var(--border);'
            f'border-left:3px solid var(--accent);border-radius:8px;padding:1rem;margin-bottom:1rem;'
            f'font-size:.9rem;line-height:1.7"><p style="font-weight:700;margin-bottom:.5rem">{titulo}</p>{ps}</div>\n')


def card(cid, num, titulo, desc, img, corpo):
    return f'''<div class="lesson-card" id="{cid}">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('{IMG}{img}?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Extra {num:02d}</div>
      <h3>{titulo}</h3>
      <div class="lesson-desc">{desc}</div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

{corpo}
  </div>
</div>
'''


CARDS = []

# ── 1. SAME SOUND, DIFFERENT WORD ───────────────────────────────────────────
CARDS.append(card('xa-sound', 1, 'Same Sound, Different Word',
    'Words that sound almost the same but mean very different things on a ship.',
    '1546883737-da9c5102ed9c',
    secao('Stage 1: Choose the Right Word', 'badge-quiz', 'Reading',
          'Read the sentence and choose the correct word.',
          quiz([
              ('S1. The vessel lay alongside her ___ in the port.', ['birth', 'berth', 'bird'], 1),
              ('S2. The ship was ___ at the berth with four lines.', ['moored', 'murdered', 'mirrored'], 0),
              ('S3. The anchor is at the ___, the front of the ship.', ['ball', 'bowl', 'bow'], 2),
              ('S4. The ship hit the sandbank and was ___ for two days.', ['aground', 'adrift', 'abroad'], 0),
              ('S5. The engine failed, and the ship went ___ with the current.', ['aground', 'afloat', 'adrift'], 2),
              ('S6. The officer on the ___ gave the order to stop the engines.', ['breed', 'bridge', 'brush'], 1),
              ('S7. The pilot ___ the master about the low tide.', ['tore', 'toured', 'told'], 2),
              ('S8. The ___ left the port at six in the morning.', ['ship', 'chip', 'sheep'], 0),
          ]))
    + secao('Stage 2: Write the Word', 'badge-practice', 'Writing',
            'Write the missing word. Tap Listen to hear the full sentence and check the sound.',
            blanks([
                ('The ship stayed at her ', 'berth', ' for two days to unload the cargo.',
                 'Hint: the place in a port where a ship stays. Not birth.'),
                ('The tug crew ', 'moored', ' the barge to the quay with four lines.',
                 'Hint: tied a ship in place. Not murdered.'),
                ('The big waves hit ', 'the bow', ' first, at the front of the ship.',
                 'Hint: two words, the + the front part of a ship. Bow sounds like now.'),
                ('Nobody on the ', 'bridge', ' saw the small boat in the fog.',
                 'Hint: the place where the officers control the ship.'),
                ('With no engine and no anchor, the barge was ', 'adrift', ' for six hours.',
                 'Hint: moving with the current, with no control.'),
            ]))))

# ── 2. WHERE IS THE SHIP? ───────────────────────────────────────────────────
CARDS.append(card('xa-where', 2, 'Where Is the Ship?',
    'The words a report uses to say where a ship is and what position she is in.',
    '1597334948330-38795f25d05d',
    secao('Stage 1: Matching', 'badge-practice', 'Vocabulary',
          'Match each word with its meaning.',
          matching('xa-match-where', [
              ('anchorage', 'an area of water where ships wait at anchor'),
              ('roadstead', 'an open area of water outside a port where ships can anchor'),
              ('alongside', 'next to the quay or to another ship, touching it'),
              ('aground', 'stuck on the bottom, in water that is too shallow'),
              ('stern', 'the back part of a ship'),
              ('starboard', 'the right side of a ship when you look forward'),
              ('port side', 'the left side of a ship when you look forward'),
              ('list', 'the angle of a ship that leans to one side'),
          ]))
    + secao('Stage 2: Write the Word', 'badge-practice', 'Writing',
            'Write the missing word. Tap Listen to hear the full sentence.',
            blanks([
                ('Five ships were waiting at the ', 'roadstead', ' outside the port entrance.',
                 'Hint: open water outside a port where ships can anchor.'),
                ('After the cargo moved, the ship took a ', 'list', ' of seven degrees.',
                 'Hint: the angle of a ship that leans to one side.'),
                ('The rudder is at the ', 'stern', ' of the vessel.',
                 'Hint: the back part of a ship. Not the rear.'),
                ('The pilot boat came ', 'alongside', ' the tanker to take the pilot off.',
                 'Hint: next to another ship, touching it.'),
                ('The container ship waited at the ', 'anchorage', ' until a berth was free.',
                 'Hint: an area of water where ships wait at anchor.'),
            ]))))

# ── 3. PASSIVE VOICE, WRITTEN ───────────────────────────────────────────────
CARDS.append(card('xa-passive', 3, 'Passive Voice, Written',
    'The structure every incident report uses: what happened, not who did it.',
    '1570187671278-2370524a1197',
    secao('Stage 1: Choose the Correct Form', 'badge-quiz', 'Grammar',
          'Choose the correct passive form.',
          quiz([
              ('P1. The work on deck ___ for two days after the accident.',
               ['was stoppage', 'was stopped', 'was stop'], 1),
              ('P2. Every near miss ___ in the log book on this ship.',
               ['is written', 'is write', 'is wrote'], 0),
              ('P3. The damaged cargo ___ to the port authority yesterday.',
               ['is reported', 'reported', 'was reported'], 2),
              ('P4. The vessel ___ tomorrow morning at high tide.',
               ['will refloated', 'will be refloated', 'will be refloat'], 1),
          ]))
    + secao('Stage 2: Write the Passive', 'badge-practice', 'Writing',
            'Write the verb in the passive. The hint shows the active sentence; the report does not say who did it.',
            blanks([
                ('The information ', 'is passed', ' to the bridge every hour.',
                 'Hint: active = They pass the information. Present passive: is + past participle.'),
                ('Two fuel tanks ', 'were breached', ' in the grounding.',
                 'Hint: active = The grounding breached two tanks. Plural: were + past participle.'),
                ('The plan ', 'was not amended', ' by the company.',
                 'Hint: active = The company did not amend the plan. Was not + past participle.'),
                ('The chart ', 'was revised', ' after the survey.',
                 'Hint: active = They revised the chart. Past passive: was + past participle.'),
                ('The lifeboat ', 'was lowered', ' in two minutes.',
                 'Hint: active = The crew lowered the lifeboat. Past passive: was + past participle.'),
            ]))))

# ── 4. PAST SIMPLE AND VERB PATTERNS ────────────────────────────────────────
CARDS.append(card('xa-verbs', 4, 'Past Simple and Verb Patterns',
    'Small words that change a report: saw, told, described it as, reported it to.',
    '1519709042477-8de6eaf1fdc5',
    secao('Stage 1: Choose the Correct Word', 'badge-quiz', 'Grammar',
          'Read the sentence and choose the correct option.',
          quiz([
              ('V1. Last night, nobody ___ the collision happen.', ['see', 'saw', 'seen'], 1),
              ('V2. The operator described the pumps ___ adequate for normal weather.',
               ['was', 'like', 'as'], 2),
              ('V3. The master reported the near miss ___ the company.', ['to', 'at', 'for'], 0),
              ('V4. Yesterday the crew ___ the lifeboat drill for twenty minutes.',
               ['practise', 'practising', 'practised'], 2),
              ('V5. The pilot ___ the officer that the tide was low.', ['said', 'told', 'talked'], 1),
              ('V6. On board, I work ___ during the night watch.', ['a lot', 'at a lot', 'in a lot'], 0),
          ]))
    + secao('Stage 2: Write the Verb', 'badge-practice', 'Writing',
            'Write the verb in the past simple. The hint gives the base verb.',
            blanks([
                ('The lookout ', 'saw', ' the other vessel at two miles.',
                 'Hint: the past of see (irregular).'),
                ('The master ', 'told', ' the chief officer to reduce speed.',
                 'Hint: the past of tell (irregular).'),
                ('The cargo ', 'shifted', ' during the storm and the ship took a list.',
                 'Hint: the past of shift (regular, add -ed).'),
                ('The second officer ', 'kept', ' the watch alone for eight hours.',
                 'Hint: the past of keep (irregular).'),
            ]))))

# ── 5. EXAM MINIS ───────────────────────────────────────────────────────────
CARDS.append(card('xa-exam', 5, 'Exam Minis',
    'Three short texts in the exam format, with options that use other words.',
    '1532528425368-31e68a9665fe',
    secao('Text A: Refloated After Two Days', 'badge-quiz', 'Reading',
          'Read the text. Then choose one option for each question and find the line that proves it.',
          texto('Refloated After Two Days', [
              'The bulk carrier Sea Falcon ran aground near the port entrance on Monday night. The weather '
              'was bad, and the ship was waiting at the roadstead when the anchor dragged. Nobody was injured, '
              'and no pollution was reported.',
              'Two tugs tried to pull the vessel free on Tuesday, but the tide was too low. On Wednesday '
              'morning, at high tide, the ship was refloated and towed to a berth for inspection. The owner said '
              'that the damage to the hull was minor. An investigation will look at the anchor watch.'])
          + quiz([
              ('A1. According to the text, it is correct to say that:',
               ['the ship hit another vessel.', 'two people were injured.',
                'the ship was freed at high tide.', 'the tugs freed the ship on Tuesday.',
                'the ship sank near the port.'], 2),
              ('A2. Mark the option that is NOT true according to the text:',
               ['The weather was bad.', 'The anchor dragged.', 'No pollution was reported.',
                'The damage to the hull was serious.', 'The ship was towed to a berth.'], 3),
              ('A3. In the text, <em>the damage to the hull was minor</em> is closest in meaning to:',
               ['the damage was small', 'the damage was expensive', 'the damage was hidden',
                'the damage was new', 'the damage was old'], 0),
          ]))
    + secao('Text B: Adequate or Sufficient?', 'badge-quiz', 'Reading',
            'Read the text. Watch the words adequate and sufficient: the exam likes to swap them.',
            texto('Adequate or Sufficient?', [
                'Before the voyage, the operator described the fire equipment as adequate under normal '
                'conditions. In the storm, however, the pumps were not sufficient: two of them stopped after one '
                'hour, and the crew had to use buckets.',
                'The report does not say that the equipment was bad. It says that it was designed for normal '
                'conditions only, and that the conditions on that night were not normal. The company has now '
                'ordered two extra pumps for each ship in the fleet.'])
            + quiz([
                ('B1. According to the text, the operator said the fire equipment was:',
                 ['insufficient in every situation.', 'new and never used.',
                  'adequate under normal conditions.', 'never tested.', 'bad.'], 2),
                ('B2. Mark the option that is NOT true according to text B:',
                 ['Two pumps stopped.', 'The report says that the equipment was bad.',
                  'The crew used buckets.', 'The company ordered more pumps.',
                  'The conditions that night were not normal.'], 1),
                ('B3. The word <em>however</em> in the second sentence shows:',
                 ['an example', 'a result', 'a time', 'a contrast', 'a place'], 3),
            ]))
    + secao('Text C: Cyber Risk on Board', 'badge-quiz', 'Reading',
            'This text is about technology, like the 2025 exam. Same method.',
            texto('Cyber Risk on Board', [
                'Modern ships depend on computers for navigation, engines and cargo. For this reason, cyber '
                'attacks are a growing risk at sea. In 2021, the IMO asked every company to include cyber risk '
                'in its safety management system. Many companies trained their crews, but small companies often '
                'did not.',
                'Experts say that the most common problem is not a clever attack but a simple mistake: a crew '
                'member opens an email with a virus, or uses a USB stick from home. Regardless of the size of the '
                'company, training is the cheapest protection.'])
            + quiz([
                ('C1. According to text C, the most common problem is:',
                 ['a clever attack.', 'an old computer.', 'bad weather.',
                  'a simple mistake by a person.', 'the IMO rules.'], 3),
                ('C2. <em>Regardless of the size of the company</em> means:',
                 ['only in small companies', 'in companies of any size', 'only in big companies',
                  'because of the size', 'before the company grows'], 1),
                ('C3. Mark the option that is NOT true according to text C:',
                 ['Ships use computers for navigation.', 'The IMO asked companies to include cyber risk.',
                  'Training is the cheapest protection.', 'A USB stick can bring a virus.',
                  'All small companies trained their crews.'], 4),
            ]))))

# ── 6. NUMBERS ON BOARD ─────────────────────────────────────────────────────
CARDS.append(card('xa-numbers', 6, 'Numbers on Board',
    'Times, degrees and distances as a report writes them.',
    '1611570266439-446689cb6bd3',
    secao('Stage 1: Read the Number', 'badge-quiz', 'Reading',
          'Read the sentence from a report and choose what the number means.',
          quiz([
              ('N1. The report says: at 2200 the master left the bridge. What time was it?',
               ['8 p.m.', '10 p.m.', '12 midnight'], 1),
              ('N2. The pilot came on board at 0630. What time was it?',
               ['6:30 a.m.', '6:30 p.m.', '3:06 a.m.'], 0),
              ('N3. The collision happened at 1415. What time was it?',
               ['4:15 p.m.', '1:45 p.m.', '2:15 p.m.'], 2),
              ('N4. The anchorage lies four nautical miles from the harbour entrance. How far is it?',
               ['40 nautical miles', '4 nautical miles', '14 nautical miles'], 1),
              ('N5. The ship took a list of 7 degrees. What happened?',
               ['She leaned 7 degrees to one side.', 'She moved 7 miles.', 'She lost 7 crew members.'], 0),
              ('N6. No injuries were reported among the 22 crew members. What does it mean?',
               ['22 people were hurt.', '2 people were hurt.', 'Nobody was hurt.'], 2),
          ]))))

INTRO = ('Extra practice for the gaps we saw in class: words that sound alike, the position of a ship, '
         'the passive in reports, past verbs, short exam texts and numbers. All answers are closed: choose '
         'or write one word. Do one card at a time.')

html = ('<!-- ========== ATIVIDADES EXTRAS (aditivo, 28/09/2026) ========== -->\n'
        '<div class="tab-content" id="tab-atividades">\n'
        '<h3 style="font-family:\'Cormorant Garamond\',serif;font-size:1.2rem;margin-bottom:1rem">Extra Activities</h3>\n'
        f'<p style="font-size:.85rem;color:var(--text-dim);margin-bottom:1.5rem">{INTRO}</p>\n'
        + ''.join(CARDS) +
        '</div><!-- /tab-atividades -->\n')
assert html.count('<div') == html.count('</div>'), 'div desbalanceado'
open(os.path.join(AQUI, 'atividades.html'), 'w', encoding='utf-8').write(html)
print('ok atividades.html', len(html), 'bytes,', html.count('blank-input'), 'lacunas,',
      html.count('quiz-item'), 'quizzes')
