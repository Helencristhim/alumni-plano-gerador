#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Conteudo-fonte das 3 abas suplementares do Diego + emissor dos snippets.

O ALUNO PEDIU (mensagem de 09/09/2026 para a Helen):
  1. mais licoes de pre-class para treinar mais
  2. extras com musicas gospel em ingles
  3. aulas de general English sobre o cotidiano nos EUA (ele quer morar la)

REGRAS QUE ESTE ARQUIVO OBEDECE
-------------------------------
* ADITIVO PURO (ordem da Helen: "nao mexe em NADA que ja existe"). As 3 abas
  entram DEPOIS de <!-- /tab-complementary -->; os 2 botoes que ja existem nao
  sao tocados. Nenhum byte do material atual e alterado. REGRAS 12/21/30.
* SEM JS NOVO. So se chamam funcoes que ja existem no hub: checkMatch,
  verifyAllMatches, checkBlank, listenBlank, selectQuiz, speakPhrase,
  startRecording, stopRecording, toggleLesson, toggleMediaDone, speakText.
  (GATE check_undefined_handlers verde; REGRA 12 respeitada.)
* REGRA 7.1: o texto vai no ATRIBUTO (data-speak / data-phrase), NUNCA dentro
  da string do handler.
* IDS PROPRIOS: xp-lesson-N / us-lesson-N / gs-song-N. NUNCA ex-lesson-N.
  updateProgress() no hub varre so ex-lesson-1..10, entao a barra de progresso
  e os 10 stamps das aulas medicas NAO se mexem.
* SEM data-lesson-progress, SEM id="stampN", SEM data-slide.
* REGRA 13 -- O DIEGO E B1, ENTAO ZERO PORTUGUES NA TELA. Todo texto visivel
  aqui e em ingles, incluindo data-hint, <option> e placeholder.
* TETO DE NIVEL (B1): so os grammar points ja dados nas aulas 1..10 dele --
  1 present simple/continuous, 2 passive, 3 past simple em perguntas e
  negativas, 4 must/have to/should/can, 5 relative clauses, 6 past perfect/
  continuous, 7 indirect questions e polite requests, 8 zero/1st conditional,
  9 2nd conditional, 10 will/going to. Nada fora disso.
* REGRA 146/29: a aba Extra Practice usa o MESMO vocabulario e a MESMA
  gramatica das Licoes 1..3, com exercicios DIFERENTES.
* REGRA 24: opcoes do matching embaralhadas (seed fixa = build reproduzivel).
* REGRA 17: todo link vai ao video EXATO, nunca a uma busca.
* AUDIO A CUSTO ZERO: nenhuma frase nova entra no audioMap, entao speakText()
  cai no ttsSpeak(). Nenhum MP3 gerado, o audioMap existente nao e tocado.

USO: python3 build_extras.py   (escreve os 3 snippets ao lado deste arquivo)
"""
import os
import random

AQUI = os.path.dirname(os.path.abspath(__file__))

SVG_MUSIC = ('<svg viewBox="0 0 24 24" width="24" height="24" fill="none" '
             'stroke="var(--accent)" stroke-width="2"><path d="M9 18V5l10-2v13"/>'
             '<circle cx="6" cy="18" r="3"/><circle cx="16" cy="16" r="3"/></svg>')

LINK_STYLE = ('display:inline-block;margin-top:.5rem;font-size:.75rem;'
              'color:var(--accent);font-weight:600;text-decoration:none;'
              'border-bottom:1px solid var(--accent)')

ITAL = 'font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic'
H3 = "font-family:'Cormorant Garamond',serif;font-size:1.2rem;margin-bottom:1rem"
INTRO = 'font-size:.85rem;color:var(--text-dim);margin-bottom:1.5rem'


def esc(s):
    return (s.replace('&', '&amp;').replace('<', '&lt;')
             .replace('>', '&gt;').replace('"', '&quot;'))


def matching(grid_id, pares, seed):
    defs = [d for _, d in pares]
    out = ['      <div class="match-grid" id="%s">' % grid_id]
    for i, (palavra, definicao) in enumerate(pares):
        opts = defs[:]
        random.Random(seed + i).shuffle(opts)
        out.append('        <div class="match-row" data-answer="%s">' % esc(definicao))
        out.append('          <span class="match-word">%s</span>' % esc(palavra))
        out.append('          <select onchange="checkMatch(this)">')
        out.append('            <option value="">Select...</option>')
        for o in opts:
            out.append('            <option value="%s">%s</option>' % (esc(o), esc(o)))
        out.append('          </select>')
        out.append('        </div>')
    out.append('      </div>')
    out.append('      <button class="verify-all-btn" onclick="verifyAllMatches(\'%s\')">Check Answers</button>' % grid_id)
    return '\n'.join(out)


def fill_in(itens):
    """itens: (antes, resposta, depois, hint_em_ingles, frase_completa[, alt])"""
    out = []
    for it in itens:
        antes, resp, depois, dica, frase = it[:5]
        alt = (' data-alt="%s"' % esc(it[5])) if len(it) > 5 else ''
        out.append(
            '      <div class="fill-blank-item"><div class="fill-blank-sentence">%s'
            '<input class="blank-input" data-answer="%s"%s data-hint="%s" data-phrase="%s" placeholder="___">'
            '%s</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>'
            '<button class="check-btn" onclick="checkBlank(this)">Check</button></div>'
            % (esc(antes), esc(resp), alt, esc(dica), esc(frase), esc(depois)))
    return '\n'.join(out)


def word_bank(palavras):
    chips = ''.join(
        '<span style="display:inline-block;background:var(--bg-card);border:1px solid var(--border);'
        'border-radius:999px;padding:.25rem .7rem;margin:.15rem;font-size:.78rem">%s</span>' % esc(p)
        for p in palavras)
    return '      <div style="margin-bottom:.9rem;line-height:2">%s</div>' % chips


def quiz(perguntas):
    out = []
    for n, (q, opcoes) in enumerate(perguntas, 1):
        out.append('      <div class="quiz-item"><div class="quiz-question">%d. %s</div><div class="quiz-options">' % (n, esc(q)))
        for letra, (txt, ok) in zip('ABCD', opcoes):
            out.append('<div class="quiz-option" onclick="selectQuiz(this)" data-correct="%s">'
                       '<span class="option-letter">%s</span> %s</div>'
                       % ('true' if ok else 'false', letra, esc(txt)))
        out.append('</div></div>')
    return '\n'.join(out)


def pronunciation(frases):
    out = []
    for f in frases:
        out.append(
            '      <div class="speech-card" data-phrase="%s">\n'
            '        <div class="speech-phrase">%s</div>\n'
            '        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button>'
            '<button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button>'
            '<button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Stop</button></div>\n'
            '        <div class="speech-result"></div>\n'
            '      </div>' % (esc(f), esc(f)))
    return '\n'.join(out)


def survival(titulo, frases):
    linhas = []
    for i, f in enumerate(frases, 1):
        linhas.append('      <div class="survival-phrase"><span class="sp-num">%d</span>'
                      '<span class="sp-en">%s</span>'
                      '<button class="audio-btn" data-speak="%s" onclick="speakText(this.dataset.speak,this)">Listen</button></div>'
                      % (i, esc(f), esc(f)))
    return ('    <div class="survival-card">\n      <h4>%s</h4>\n%s\n    </div>'
            % (esc(titulo), '\n'.join(linhas)))


def secao(titulo, badge, badge_cls, instrucao, corpo):
    return ('    <div class="exercise-section">\n'
            '      <div class="section-header-row"><h4>%s</h4><span class="badge %s">%s</span></div>\n'
            '      <p style="%s">%s</p>\n%s\n    </div>'
            % (esc(titulo), badge_cls, esc(badge), ITAL, esc(instrucao), corpo))


def lesson_card(card_id, img, numero, titulo, desc, blocos):
    return ('<div class="lesson-card" id="%s">\n'
            '  <div class="lesson-header" onclick="toggleLesson(this)">\n'
            '    <div class="lesson-header-img" style="background-image:url(\'%s\')"></div>\n'
            '    <div class="lesson-header-content">\n'
            '      <div class="lesson-number">%s</div>\n'
            '      <h3>%s</h3>\n'
            '      <div class="lesson-desc">%s</div>\n'
            '    </div>\n'
            '    <div class="expand-icon">&#9660;</div>\n'
            '  </div>\n'
            '  <div class="lesson-body">\n\n%s\n\n  </div>\n'
            '</div>' % (card_id, img, esc(numero), esc(titulo), esc(desc), '\n\n'.join(blocos)))


# ============================================================ ABA: EXTRA PRACTICE
# REGRA 146: mesmo vocabulario e mesma gramatica das Licoes 1..3 do hub,
# exercicios DIFERENTES. As definicoes do matching foram REESCRITAS -- nenhuma
# repete a do material original.

XP = [
    dict(n=1, card='xp-lesson-1',
         img='https://images.unsplash.com/photo-1631217868264-e5b90bb7e133?w=600&q=80',
         titulo='More Practice -- Opening the Consultation',
         gram='present simple and present continuous',
         desc='A second round of Lesson 1. Same words, same structure, exercises you have not seen. Do it after you finish the Lesson 1 Pre-class.',
         vocab=[('A chief complaint', 'the problem the patient names first when you ask why they came'),
                ('A rash', 'a patch of skin that has changed colour and texture'),
                ('Itchy', 'giving the constant urge to rub or scratch'),
                ('To flare up', 'to get sharply worse after a quiet period'),
                ('Tender', 'sore under light pressure'),
                ('Over-the-counter', 'sold at a pharmacy with no prescription needed'),
                ('A follow-up', 'the return appointment that checks the result'),
                ('A referral', 'a letter sending the patient on to a specialist')],
         banco=['Is', 'applies', 'is flaring', 'run', 'am booking', 'Does'],
         fills=[('"', 'Is', ' the rash itchy at night?"', 'Hint: a yes/no question with the verb to be', 'Is the rash itchy at night?'),
                ('"She ', 'applies', ' an over-the-counter cream twice a day."', 'Hint: present simple, third person singular', 'She applies an over-the-counter cream twice a day.'),
                ('"The rash ', 'is flaring', ' up again this week."', 'Hint: present continuous, two words', 'The rash is flaring up again this week.'),
                ('"Skin problems ', 'run', ' in her family."', 'Hint: the subject is plural, so no final s', 'Skin problems run in her family.'),
                ('"I ', 'am booking', ' a follow-up for you in six weeks."', 'Hint: present continuous, two words', 'I am booking a follow-up for you in six weeks.'),
                ('"', 'Does', ' the referral go straight to the hospital?"', 'Hint: the present simple auxiliary in a question', 'Does the referral go straight to the hospital?')],
         quiz=[('A patient says: "It comes and goes." What is she telling you?',
                [('That the rash is there all the time and never changes.', False),
                 ('That the rash appears and disappears, again and again.', True),
                 ('That she is leaving the appointment now.', False),
                 ('That the cream is finished.', False)]),
               ('You want to know whether the problem is happening right now, this week. Which question fits?',
                [('Does it flare up in winter?', False),
                 ('Is it flaring up at the moment?', True),
                 ('Did it flare up last year?', False),
                 ('Has it flared up before?', False)]),
               ('The patient bought a cream at the pharmacy with no prescription. How do you write that?',
                [('She used a referral cream.', False),
                 ('She used a follow-up cream.', False),
                 ('She used an over-the-counter cream.', True),
                 ('She used a chief complaint cream.', False)]),
               ('Which sentence is correct?',
                [('The rash is itching her every night this week.', False),
                 ('The rash itches every night. It is the usual pattern.', True),
                 ('The rash itch every night.', False),
                 ('The rash are itchy every night.', False)])],
         fala=['Can you tell me what brought you in today?',
               'Is the area tender when I press it, or only itchy?',
               'How often does it flare up, and how long does it last?',
               'I am writing you a referral, just in case.',
               'Let us book a follow-up in six weeks.'],
         survival=['What brings you in today?',
                   'Is it tender when I press here?',
                   'Does it run in the family?',
                   'The rash is spreading this week.',
                   'I am booking a follow-up for you.']),

    dict(n=2, card='xp-lesson-2',
         img='https://images.unsplash.com/photo-1532187863486-abf9dbad1b69?w=600&q=80',
         titulo='More Practice -- How a Paper Is Built',
         gram='the passive voice, present and past simple',
         desc='A second round of Lesson 2. Same research vocabulary, same passive voice, new sentences.',
         vocab=[('A trial', 'a planned study that tests a treatment on people'),
                ('To enroll', 'to sign a participant into the study'),
                ('A cohort', 'the group of people followed together in a study'),
                ('Baseline', 'the first measurement, taken before treatment starts'),
                ('An outcome', 'the result the study set out to measure'),
                ('To assess', 'to measure and judge something carefully'),
                ('Adherence', 'how closely patients follow the treatment as prescribed'),
                ('Significant', 'unlikely to be explained by chance alone')],
         banco=['was enrolled', 'is assessed', 'was measured', 'were reported', 'is collected', 'was found'],
         fills=[('"Each participant ', 'was enrolled', ' at the start of the study."', 'Hint: past passive, singular subject, two words', 'Each participant was enrolled at the start of the study.'),
                ('"The primary outcome ', 'is assessed', ' at twelve weeks."', 'Hint: present passive, singular subject, two words', 'The primary outcome is assessed at twelve weeks.'),
                ('"Adherence ', 'was measured', ' by pill count."', 'Hint: past passive, singular subject, two words', 'Adherence was measured by pill count.'),
                ('"The results ', 'were reported', ' in a peer-reviewed journal."', 'Hint: past passive, plural subject, two words', 'The results were reported in a peer-reviewed journal.'),
                ('"Baseline data ', 'is collected', ' before the first dose."', 'Hint: present passive, two words', 'Baseline data is collected before the first dose.'),
                ('"The difference ', 'was found', ' to be significant."', 'Hint: past passive of the verb to find', 'The difference was found to be significant.')],
         quiz=[('Why does the methods section use the passive so much?',
                [('Because the action matters more than who performed it.', True),
                 ('Because the passive is more polite in English.', False),
                 ('Because scientists are not allowed to write we.', False),
                 ('Because the passive is always shorter than the active.', False)]),
               ('"Patients were assessed at baseline." Who did the assessing?',
                [('The patients themselves, clearly.', False),
                 ('The sentence does not say, and that is the point.', True),
                 ('The journal editors.', False),
                 ('It is a mistake in the paper.', False)]),
               ('You read: "Adherence was low in the treatment cohort." What does that mean?',
                [('The treatment did not work at all.', False),
                 ('Few patients were enrolled in that group.', False),
                 ('That group did not take the treatment as prescribed.', True),
                 ('The outcome was not significant.', False)]),
               ('Which sentence is in the passive voice?',
                [('The team concluded that the drug works.', False),
                 ('The drug was well tolerated by the cohort.', True),
                 ('The cohort tolerated the drug well.', False),
                 ('The trial reports a significant outcome.', False)])],
         fala=['The trial enrolled two hundred patients over eighteen months.',
               'Adherence was assessed by pill count at every visit.',
               'The difference between the two groups was significant.',
               'One limitation is that the cohort was very small.',
               'These results are associated with better outcomes.'],
         survival=['The outcome is assessed at twelve weeks.',
                   'Two hundred patients were enrolled.',
                   'Adherence was measured by pill count.',
                   'The difference was found to be significant.',
                   'One limitation is the size of the cohort.']),

    dict(n=3, card='xp-lesson-3',
         img='https://images.unsplash.com/photo-1584982751601-97dcc096659c?w=600&q=80',
         titulo='More Practice -- Taking the History',
         gram='the past simple in questions and negatives',
         desc='A second round of Lesson 3. Same skin vocabulary, same past simple questions and negatives, new exercises.',
         vocab=[('Onset', 'the moment a symptom first appeared'),
                ('A patch', 'one small marked area of skin'),
                ('Scaly', 'covered in dry flakes that come away'),
                ('A trigger', 'the thing that sets the problem off'),
                ('To scratch', 'to rub the skin hard with the nails'),
                ('Swollen', 'larger than normal because of fluid'),
                ('A blister', 'a small bubble of fluid under the skin'),
                ('Persistent', 'continuing without stopping or going away')],
         banco=['was the onset', 'Did', 'did not stop', 'Was', 'did not notice', 'were'],
         fills=[('"When ', 'was the onset', ' of the rash?"', 'Hint: three words, a past question with the verb to be', 'When was the onset of the rash?'),
                ('"', 'Did', ' you scratch it during the night?"', 'Hint: the past simple auxiliary in a question', 'Did you scratch it during the night?'),
                ('"The cream ', 'did not stop', ' the itching."', 'Hint: past simple negative, three words', 'The cream did not stop the itching.'),
                ('"', 'Was', ' the area swollen when you woke up?"', 'Hint: past of the verb to be, in a question', 'Was the area swollen when you woke up?'),
                ('"She ', 'did not notice', ' the blister at first."', 'Hint: past simple negative, three words', 'She did not notice the blister at first.'),
                ('"How long ', 'were', ' the patches persistent?"', 'Hint: past of the verb to be, plural subject', 'How long were the patches persistent?')],
         quiz=[('You want to know when the problem started. Which question is correct?',
                [('When did the onset was?', False),
                 ('When was the onset?', True),
                 ('When did the onset?', False),
                 ('When the onset was?', False)]),
               ('Which negative sentence is correct in the past simple?',
                [('She did not scratched the patch.', False),
                 ('She not scratched the patch.', False),
                 ('She did not scratch the patch.', True),
                 ('She was not scratch the patch.', False)]),
               ('A patient says the lesion is scaly and persistent. What are you being told?',
                [('It is wet and it disappears quickly.', False),
                 ('It flakes and it does not go away.', True),
                 ('It is swollen and painful to touch.', False),
                 ('It is a blister filled with fluid.', False)]),
               ('You are looking for the trigger. Which question gets you there?',
                [('Did anything change before it started?', True),
                 ('Does it run in the family?', False),
                 ('Is it tender when I press it?', False),
                 ('Will it settle down on its own?', False)])],
         fala=['When exactly was the onset of the first patch?',
               'Did anything change before the rash appeared?',
               'Was the area swollen, or only red?',
               'The cream did not stop the itching, is that right?',
               'I would like to examine the patch and rule a few things out.'],
         survival=['When was the onset?',
                   'Did anything change before it started?',
                   'Did you scratch it during the night?',
                   'The cream did not stop the itching.',
                   'Was the area swollen this morning?']),
]


def render_xpractice():
    cards = []
    for x in XP:
        s1 = secao('Stage 1: Matching', 'Vocabulary', 'badge-vocab',
                   'Choose the meaning of each word. These definitions are new, so read them carefully.',
                   matching('match-xp%d' % x['n'], x['vocab'], seed=1100 + x['n'] * 10))
        s2 = secao('Stage 2: Fill in the Blank', 'Practice', 'badge-practice',
                   'Use the word bank. Complete each sentence, then check your answer.',
                   word_bank(x['banco']) + '\n' + fill_in(x['fills']))
        s3 = secao('Stage 3: Situations', 'Quiz', 'badge-quiz',
                   'Choose the best answer for each situation.', quiz(x['quiz']))
        s4 = secao('Stage 4: Pronunciation', 'Speaking', 'badge-speak',
                   'Listen, then record yourself. You will get a word-by-word score.',
                   pronunciation(x['fala']))
        sc = survival('Survival Card -- Extra Practice %02d' % x['n'], x['survival'])
        cards.append(lesson_card(x['card'], x['img'],
                                 'Extra Practice %02d' % x['n'], x['titulo'],
                                 '%s Structure: %s.' % (x['desc'], x['gram']),
                                 [s1, s2, s3, s4, sc]))

    return ('<!-- ========== TAB 3: EXTRA PRACTICE (aditivo, 09/09/2026) ========== -->\n'
            '<div class="tab-content" id="tab-xpractice">\n'
            '<h3 style="%s">Extra Practice</h3>\n'
            '<p style="%s">More practice on the lessons you have already done. Same vocabulary and same grammar as the Pre-class, '
            'with exercises you have not seen before. Do each one after you finish the matching Pre-class lesson.</p>\n'
            '%s\n'
            '</div><!-- /tab-xpractice -->\n' % (H3, INTRO, '\n\n'.join(cards)))


# ========================================================= ABA: LIVING IN THE USA
# General English do cotidiano americano -- ZERO jargao medico, que e justamente
# o que falta no material dele. AUTOESTUDO: nao consome as 80 aulas contratadas
# e nao altera nada do professor. Cada licao ancora num grammar point ja dado.

US = [
    dict(n=1, card='us-lesson-1',
         img='https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=600&q=80',
         titulo='Finding a Place to Live',
         gram='present simple and modals -- should, have to',
         desc='The first thing you do after you land: find an apartment, read the lease and understand what you are actually paying for.',
         vocab=[('A lease', 'the signed contract that lets you live there for a fixed time'),
                ('A security deposit', 'money held back and returned if you leave no damage'),
                ('Utilities', 'electricity, water, gas and internet'),
                ('A landlord', 'the person who owns the place and collects the rent'),
                ('A realtor', 'the agent who shows you apartments and handles the paperwork'),
                ('Rent', 'the amount you pay every month to live there'),
                ('A credit check', 'a look at your payment history before you are approved'),
                ('Furnished', 'already has the furniture in it')],
         banco=['will have to', 'should read', 'does not include', 'returns', 'Should', 'is not'],
         fills=[('"You ', 'will have to', ' sign the lease before you get the keys."', 'Hint: future plus obligation, three words', 'You will have to sign the lease before you get the keys.'),
                ('"You ', 'should read', ' the whole lease before you sign it."', 'Hint: advice, not obligation, two words', 'You should read the whole lease before you sign it.'),
                ('"The rent ', 'does not include', ' utilities, so you pay them separately."', 'Hint: present simple negative, three words', 'The rent does not include utilities, so you pay them separately.'),
                ('"The landlord ', 'returns', ' the deposit if there is no damage."', 'Hint: present simple, third person singular', 'The landlord returns the deposit if there is no damage.'),
                ('"', 'Should', ' I bring my passport to the credit check?"', 'Hint: asking for advice', 'Should I bring my passport to the credit check?'),
                ('"The apartment ', 'is not', ' furnished, so we need a bed."', 'Hint: present simple negative of the verb to be', 'The apartment is not furnished, so we need a bed.')],
         quiz=[('The listing says $1,800/month plus utilities. What do you actually pay?',
                [('Exactly 1,800 dollars, everything included.', False),
                 ('1,800 dollars plus electricity, water, gas and internet.', True),
                 ('1,800 dollars minus the deposit.', False),
                 ('1,800 dollars only in the first month.', False)]),
               ('You want to know if you get your deposit back. What do you ask?',
                [('When do I get the security deposit back?', True),
                 ('When do I pay the rent?', False),
                 ('Is the apartment furnished?', False),
                 ('Who is the landlord?', False)]),
               ('The realtor says: "We will need to run a credit check." What is happening?',
                [('They want to see your medical records.', False),
                 ('They will look at your payment history before approving you.', True),
                 ('They are charging you an extra fee.', False),
                 ('They are checking whether the apartment is furnished.', False)]),
               ('Which sentence gives advice, not an obligation?',
                [('You have to pay the deposit before you move in.', False),
                 ('You must sign the lease today.', False),
                 ('You should take photos of the apartment on your first day.', True),
                 ('You cannot paint the walls.', False)])],
         fala=['Hi, I saw your listing online. Is the apartment still available?',
               'How much is the security deposit, and when do I get it back?',
               'Are utilities included in the rent?',
               'I would like to see the place this weekend, if possible.',
               'Could you send me a copy of the lease before I sign?'],
         survival=['Is the apartment still available?',
                   'Are utilities included in the rent?',
                   'How much is the security deposit?',
                   'You should read the whole lease first.',
                   'I have to sign the lease before I get the keys.']),

    dict(n=2, card='us-lesson-2',
         img='https://images.unsplash.com/photo-1542838132-92c53300491e?w=600&q=80',
         titulo='Everyday Errands',
         gram='indirect questions and polite requests',
         desc='The grocery store, the bank and the phone plan. Short exchanges you will have a hundred times, where sounding polite matters more than sounding perfect.',
         vocab=[('A checkout', 'the counter where you pay before leaving the store'),
                ('A cart', 'the metal basket on wheels you push around the store'),
                ('A receipt', 'the printed proof of what you paid'),
                ('Change', 'the coins and bills you get back when you overpay'),
                ('A checking account', 'the everyday bank account you pay bills from'),
                ('A debit card', 'the card that takes the money straight from your account'),
                ('A prepaid plan', 'a phone plan you pay for before you use it'),
                ('Coverage', 'how well the signal reaches where you live')],
         banco=['Could', 'what time', 'if', 'giving', 'costs', 'have'],
         fills=[('"', 'Could', ' you tell me where the milk is?"', 'Hint: the polite way to open a request', 'Could you tell me where the milk is?'),
                ('"Do you know ', 'what time', ' the pharmacy closes?"', 'Hint: two words, an indirect question about the hour', 'Do you know what time the pharmacy closes?'),
                ('"I was wondering ', 'if', ' you take debit cards."', 'Hint: one word, introduces an indirect yes/no question', 'I was wondering if you take debit cards.', 'whether'),
                ('"Would you mind ', 'giving', ' me the receipt?"', 'Hint: after would you mind, the verb takes -ing', 'Would you mind giving me the receipt?'),
                ('"Could you tell me how much this ', 'costs', '?"', 'Hint: present simple, third person singular', 'Could you tell me how much this costs?'),
                ('"Excuse me, could I ', 'have', ' a bag, please?"', 'Hint: the verb you use to ask for something politely', 'Excuse me, could I have a bag, please?')],
         quiz=[('Which one sounds most polite to a stranger in a store?',
                [('Where is the milk?', False),
                 ('Tell me where the milk is.', False),
                 ('Could you tell me where the milk is?', True),
                 ('I want the milk.', False)]),
               ('Which indirect question is built correctly?',
                [('Do you know what time does the bank open?', False),
                 ('Do you know what time the bank opens?', True),
                 ('Do you know what time opens the bank?', False),
                 ('Do you know what time does open the bank?', False)]),
               ('At the checkout the cashier asks: "Debit or credit?" What are they asking?',
                [('Whether you want a receipt.', False),
                 ('Which type of card you are paying with.', True),
                 ('Whether you have a loyalty card.', False),
                 ('How much change you need.', False)]),
               ('You are choosing a phone plan and you live outside the city. What matters most?',
                [('Whether the plan is prepaid.', False),
                 ('The coverage where you live.', True),
                 ('The colour of the SIM card.', False),
                 ('Whether they give you a receipt.', False)])],
         fala=['Excuse me, could you tell me where the milk is?',
               'Do you know what time the pharmacy closes?',
               'I was wondering if you take debit cards.',
               'Would you mind giving me a receipt, please?',
               'I would like to open a checking account.'],
         survival=['Could you tell me where the milk is?',
                   'Do you know what time it closes?',
                   'I was wondering if you take debit cards.',
                   'Could I have a bag, please?',
                   'I would like to open a checking account.']),

    dict(n=3, card='us-lesson-3',
         img='https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=600&q=80',
         titulo='Small Talk with Americans',
         gram='the past simple in questions and negatives',
         desc='The two minutes in the elevator, the hallway and the break room. Small talk is not empty in the US, it is how people decide whether they know you.',
         vocab=[('A neighbor', 'the person who lives next door or very close'),
                ('A block', 'one stretch of street between two corners'),
                ('A cookout', 'an informal meal cooked outdoors, usually in a yard'),
                ('To catch up', 'to meet and share news after some time apart'),
                ('To grab a coffee', 'to meet somewhere quickly for a drink and a chat'),
                ('A heads-up', 'a short warning so you are not taken by surprise'),
                ('Downtown', 'the central business part of an American city'),
                ('The weekend', 'Saturday and Sunday, when most people are off')],
         banco=['Did', 'did not go', 'did', 'Was', 'did not stay', 'were'],
         fills=[('"', 'Did', ' you have a good weekend?"', 'Hint: the past simple auxiliary opening a question', 'Did you have a good weekend?'),
                ('"I ', 'did not go', ' downtown on Saturday."', 'Hint: past simple negative, three words', 'I did not go downtown on Saturday.'),
                ('"Where ', 'did', ' you live before you moved here?"', 'Hint: the past simple auxiliary after a question word', 'Where did you live before you moved here?'),
                ('"', 'Was', ' the cookout fun?"', 'Hint: past of the verb to be, singular, in a question', 'Was the cookout fun?'),
                ('"We ', 'did not stay', ' long, it was cold."', 'Hint: past simple negative, three words', 'We did not stay long, it was cold.'),
                ('"How long ', 'were', ' you in Brazil?"', 'Hint: past of the verb to be, with you', 'How long were you in Brazil?')],
         quiz=[('A neighbor says: "We should grab a coffee sometime." What is happening?',
                [('A firm invitation with a date already set.', False),
                 ('A friendly, open invitation with no date yet.', True),
                 ('A complaint about your schedule.', False),
                 ('A request for you to buy them a coffee.', False)]),
               ('Which question is correct in the past simple?',
                [('Where did you lived before?', False),
                 ('Where you lived before?', False),
                 ('Where did you live before?', True),
                 ('Where did lived you before?', False)]),
               ('Someone gives you a heads-up about street parking. What did they do?',
                [('They warned you in advance so you are not caught out.', True),
                 ('They complained about your car.', False),
                 ('They asked you to move the car right now.', False),
                 ('They offered you a ride downtown.', False)]),
               ('You just moved into the building. What is a natural first line to a neighbor?',
                [('What is your salary?', False),
                 ('Hi, I just moved in downstairs. I am Diego.', True),
                 ('Why do you live here?', False),
                 ('Tell me about yourself.', False)])],
         fala=['Hi, I just moved in downstairs. I am Diego.',
               'Did you have a good weekend?',
               'We should grab a coffee sometime.',
               'Thanks for the heads-up, I appreciate it.',
               'Sorry, I did not catch your name.'],
         survival=['Hi, I just moved in downstairs.',
                   'Did you have a good weekend?',
                   'We should grab a coffee sometime.',
                   'Thanks for the heads-up.',
                   'Sorry, I did not catch your name.']),
]


def render_uslife():
    cards = []
    for u in US:
        s1 = secao('Stage 1: Matching', 'Vocabulary', 'badge-vocab',
                   'Choose the meaning of each word.',
                   matching('match-us%d' % u['n'], u['vocab'], seed=2200 + u['n'] * 10))
        s2 = secao('Stage 2: Fill in the Blank', 'Practice', 'badge-practice',
                   'Use the word bank. Complete each sentence, then check your answer.',
                   word_bank(u['banco']) + '\n' + fill_in(u['fills']))
        s3 = secao('Stage 3: Situations', 'Quiz', 'badge-quiz',
                   'Choose the best answer for each situation.', quiz(u['quiz']))
        s4 = secao('Stage 4: Pronunciation', 'Speaking', 'badge-speak',
                   'Listen, then record yourself. You will get a word-by-word score.',
                   pronunciation(u['fala']))
        sc = survival('Survival Card -- Living in the USA %02d' % u['n'], u['survival'])
        cards.append(lesson_card(u['card'], u['img'],
                                 'Living in the USA %02d' % u['n'], u['titulo'],
                                 '%s Structure: %s.' % (u['desc'], u['gram']),
                                 [s1, s2, s3, s4, sc]))

    return ('<!-- ========== TAB 4: LIVING IN THE USA (aditivo, 09/09/2026) ========== -->\n'
            '<div class="tab-content" id="tab-uslife">\n'
            '<h3 style="%s">Living in the USA</h3>\n'
            '<p style="%s">General English for everyday life in the United States, outside the clinic. '
            'These lessons are yours to study on your own, whenever you want. They do not replace any of your scheduled lessons.</p>\n'
            '%s\n'
            '</div><!-- /tab-uslife -->\n' % (H3, INTRO, '\n\n'.join(cards)))


# ================================================================= ABA: GOSPEL
# 12 musicas. Cada link foi VERIFICADO um a um pelo oembed do YouTube em
# 09/09/2026 (titulo + canal conferidos); todos sao canal oficial do artista
# (REGRA 17: link para o video EXATO, nunca busca).
# Cada musica esta ancorada num grammar point que ele JA VIU (teto de nivel).
# As lacunas sao trechos CURTOS, 1 a 3 palavras -- nunca a letra inteira.

GOSPEL = [
    dict(vid='KBD18rsVJHk', artista='Chris Tomlin', titulo='How Great Is Our God',
         gram='Present simple',
         nota='The chorus is one sentence repeated until you cannot get it wrong: subject, present simple verb, complement. It is the structure of your Lesson 1, sung slowly.',
         tip='Tip: sing along twice. The second time, listen to how is almost always reduced to a z sound attached to the word before it.',
         gaps=[('"How great ', 'is', ' our God, sing with me"', 'Hint: present simple of the verb to be, third person', 'How great is our God, sing with me'),
               ('"Let all the earth ', 'rejoice', '"', 'Hint: a verb meaning to feel and show great joy', 'Let all the earth rejoice')]),

    dict(vid='izrk-erhDdk', artista='Hillsong Worship', titulo='Cornerstone',
         gram='Relative clauses',
         nota='A song built on relative clauses. Good for hearing the linking you practised in Lesson 5, at a speed you can follow.',
         tip='Tip: find every that and who in the lyrics. Write down which word each one refers back to.',
         gaps=[('"My hope is built on nothing ', 'less', '"', 'Hint: the opposite of more', 'My hope is built on nothing less'),
               ('"Weak made ', 'strong', " in the Savior's love\"", 'Hint: the opposite of weak', "Weak made strong in the Savior's love")]),

    dict(vid='iBmwwwiHrOk', artista='Chris Tomlin', titulo='Good Good Father',
         gram='Relative clauses',
         nota='The chorus is literally a relative clause: it is who You are. If you understand that line, you have understood all of Lesson 5.',
         tip='Tip: notice that who here does not open a question. It links two ideas. That is exactly the difference Lesson 5 worked on.',
         gaps=[("\"You're a good, good ", 'Father', '"', 'Hint: the word in the title of the song', "You're a good, good Father"),
               ("\"It's ", 'who', ' You are"', 'Hint: the relative pronoun used for people', "It's who You are")]),

    dict(vid='SzG-WKIVH0w', artista='Matt Redman', titulo='10,000 Reasons (Bless the Lord)',
         gram='Present simple',
         nota='British English, very clean diction and a slow tempo. The verse is all present simple and imperatives, the two simplest forms you have.',
         tip='Tip: this is the best one on the list to start with. Listen once just listening, then read the lyrics out loud along with it.',
         gaps=[('"', 'Bless', ' the Lord, O my soul"', 'Hint: the verb that opens the song, in the imperative', 'Bless the Lord O my soul'),
               ('"Sing like never ', 'before', '"', 'Hint: the opposite of after', 'Sing like never before')]),

    dict(vid='IvSuGyJQ6oM', artista='Bethel Music and Jenn Johnson', titulo='Goodness of God',
         gram='Present continuous',
         nota='Your goodness is running after me is present continuous, and the image is easy to remember. Same structure as Lesson 1.',
         tip='Tip: listen to the chorus three times in a row. Notice that is running describes something in progress, not a habit.',
         gaps=[('"Your ', 'goodness', ' is running after me"', 'Hint: the noun in the title of the song', 'Your goodness is running after me'),
               ('"I sing of the goodness of ', 'God', '"', 'Hint: who the song is about', 'I sing of the goodness of God')]),

    dict(vid='KwX1f2gYKZ4', artista='Elevation Worship', titulo='Graves Into Gardens',
         gram='Present simple',
         nota='The chorus repeats the same structure four times, changing only the object: You turn X into Y. Excellent for fixing the present simple without effort.',
         tip='Tip: after listening, build three sentences of your own with You turn ___ into ___ and record yourself saying them.',
         gaps=[('"You turn ', 'graves', ' into gardens"', 'Hint: the word in the title, plural', 'You turn graves into gardens'),
               ('"You turn seas into ', 'highways', '"', 'Hint: wide fast roads, in American English', 'You turn seas into highways')]),

    dict(vid='N8WK9HmF53w', artista='Lauren Daigle', titulo='You Say',
         gram='Present simple and passive',
         nota='The whole song is a contrast between two present simple sentences, and the answers come in the passive: I am loved, I am strong. Lesson 1 and Lesson 2 on the same track.',
         tip='Tip: split a page into two columns, You say and I say, and write each line on the right side as you listen.',
         gaps=[('"You ', 'say', " I am loved when I can't feel a thing\"", 'Hint: the verb in the title', "You say I am loved when I can't feel a thing"),
               ('"You say I am strong when I think I am ', 'weak', '"', 'Hint: the opposite of strong', 'You say I am strong when I think I am weak')]),

    dict(vid='JGYjKR69M6U', artista='Zach Williams', titulo='Chain Breaker',
         gram='First conditional',
         nota='Every line of the chorus is a first conditional: if you have got pain, He is a pain taker. It is all of Lesson 8, in the form of a song.',
         tip='Tip: count how many times if appears. Then write three sentences of your own in the same shape: If ___, ___.',
         gaps=[("\"If you've got pain, He's a pain ", 'taker', '"', 'Hint: the person who takes something, built from take', "If you've got pain, He's a pain taker"),
               ('"If you feel lost, He\'s a way ', 'maker', '"', 'Hint: the person who makes something, built from make', "If you feel lost, He's a way maker")]),

    dict(vid='ZNDEyxEMNp0', artista='MercyMe', titulo='I Can Only Imagine',
         gram='Future with will',
         nota='The song is a sequence of future questions with will: will I dance, will I sing. Exactly what you worked on in Lesson 10.',
         tip='Tip: write down the questions with will that the song asks. Then answer each one out loud.',
         gaps=[('"What ', 'will', ' my heart feel?"', 'Hint: the future auxiliary from Lesson 10', 'What will my heart feel'),
               ('"Will I dance for You, Jesus, or in awe of You be ', 'still', '?"', 'Hint: not moving at all', 'Will I dance for You Jesus or in awe of You be still')]),

    dict(vid='dy9nwe9_xzw', artista='Hillsong UNITED', titulo='Oceans (Where Feet May Fail)',
         gram='Future with will',
         nota='Slow, with a lot of space between the words, so it is one of the best on this list for training your ear. The chorus alternates present simple and future with will.',
         tip='Tip: because it is slow, use the 0.75x speed button at the top of this material to follow the lyrics without rushing.',
         gaps=[("\"You've never failed and You ", "won't", ' start now"', 'Hint: the contracted negative of will', "You've never failed and You won't start now", 'will not'),
               ('"Spirit ', 'lead', ' me where my trust is without borders"', 'Hint: to guide someone', 'Spirit lead me where my trust is without borders')]),

    dict(vid='-pD2zIuiC2g', artista='Tasha Cobbs', titulo='Break Every Chain',
         gram='Present simple with there is',
         nota='A very short lyric, repeated many times. Perfect for day one: you learn the whole song in a single listen.',
         tip='Tip: sing along without looking at the lyrics on the third time. There are few words, and the repetition does the work.',
         gaps=[('"There is power in the ', 'name', ' of Jesus"', 'Hint: what you call a person', 'There is power in the name of Jesus'),
               ('"To break every ', 'chain', '"', 'Hint: the word in the title, singular', 'To break every chain')]),

    dict(vid='0YUGwUgBvTU', artista='Casting Crowns', titulo='Praise You In This Storm',
         gram='Past simple',
         nota='The lyric tells a story in the past before it reaches the chorus. It is the narrative past simple you saw in Lesson 6, in very well articulated American English.',
         tip='Tip: listen to the first verse only and underline every past tense verb. Then retell the story in your own words.',
         gaps=[("\"And I'll praise You in this ", 'storm', '"', 'Hint: the word in the title, bad weather', "And I'll praise You in this storm"),
               ('"I was ', 'sure', ' by now You would have reached down"', 'Hint: certain, with no doubt', 'I was sure by now You would have reached down')]),
]


def render_gospel():
    cards = []
    for i, s in enumerate(GOSPEL, 1):
        gaps = fill_in(s['gaps'])
        cards.append(
            '<div class="media-card-wrapper" data-media="gs-song-%d">\n'
            '  <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>\n'
            '  <div class="media-card">\n'
            '    <div class="media-thumb">%s</div>\n'
            '    <div class="media-info">\n'
            '      <div class="media-type">Gospel &middot; %s</div>\n'
            '      <h5>%s &mdash; %s</h5>\n'
            '      <p>%s</p>\n'
            '      <p class="media-tip">%s</p>\n'
            '      <a href="https://www.youtube.com/watch?v=%s" target="_blank" rel="noopener" style="%s">Listen on YouTube &#8599;</a>\n'
            '      <div style="margin-top:.9rem;padding-top:.8rem;border-top:1px solid var(--border)">\n'
            '        <div style="font-size:.78rem;font-weight:600;margin-bottom:.5rem">Fill in what you hear</div>\n%s\n'
            '      </div>\n'
            '    </div>\n'
            '  </div>\n'
            '</div>' % (i, SVG_MUSIC, esc(s['gram']), esc(s['artista']), esc(s['titulo']),
                        esc(s['nota']), esc(s['tip']), s['vid'], LINK_STYLE, gaps))

    return ('<!-- ========== TAB 5: GOSPEL (aditivo, 09/09/2026) ========== -->\n'
            '<div class="tab-content" id="tab-gospel">\n'
            '<h3 style="%s">Gospel Playlist</h3>\n'
            '<p style="%s">Twelve gospel songs in English to listen to outside class. Each one was chosen for a structure you have already studied, '
            'and comes with two short gaps for you to complete by ear. Mark each song as done after you listen to it.</p>\n'
            '<div class="media-grid">\n%s\n</div>\n'
            '</div><!-- /tab-gospel -->\n' % (H3, INTRO, '\n\n'.join(cards)))


# ===================================================================== EMISSOR

SNIPPETS = [('xpractice.html', render_xpractice),
            ('uslife.html', render_uslife),
            ('gospel.html', render_gospel)]


def main():
    for nome, fn in SNIPPETS:
        destino = os.path.join(AQUI, nome)
        html = fn()
        with open(destino, 'w', encoding='utf-8') as f:
            f.write(html)
        print('%-16s %6d bytes' % (nome, len(html.encode('utf-8'))))


if __name__ == '__main__':
    main()
