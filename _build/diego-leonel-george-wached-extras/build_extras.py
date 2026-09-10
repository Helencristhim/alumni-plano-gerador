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

    dict(n=4, card='xp-lesson-4',
         img='https://images.unsplash.com/photo-1587854692152-cbe660dbde88?w=600&q=80',
         titulo='More Practice -- The Pharmacy Aisle',
         gram='modals of obligation and advice -- must, have to, should, can',
         desc='A second round of Lesson 4. Same pharmacy vocabulary, same modals, new sentences and situations.',
         vocab=[('A prescription', 'the written order a doctor gives for a medicine'),
                ('A refill', 'a repeat of the same prescription without a new visit'),
                ('A dosage', 'the amount of a medicine and the times you take it'),
                ('An expiration date', 'the day after which the product should not be used'),
                ('Generic', 'the same medicine sold without the brand name'),
                ('A copay', 'the fixed part of the cost the patient pays'),
                ('A pharmacist', 'the professional who prepares and hands out medicines'),
                ('To run out of', 'to have none of something left')],
         banco=['must finish', 'should check', 'have to show', 'can buy', 'must not double', 'should not stop'],
         fills=[('"You ', 'must finish', ' the whole course, even if you feel better."', 'Hint: strong obligation plus the verb, two words', 'You must finish the whole course, even if you feel better.'),
                ('"You ', 'should check', ' the expiration date before you use it."', 'Hint: advice plus the verb, two words', 'You should check the expiration date before you use it.'),
                ('"You ', 'have to show', ' the prescription to get a refill."', 'Hint: obligation from a rule plus the verb, three words', 'You have to show the prescription to get a refill.'),
                ('"You ', 'can buy', ' the generic version for much less."', 'Hint: possibility plus the verb, two words', 'You can buy the generic version for much less.'),
                ('"You ', 'must not double', ' the dosage if you miss a day."', 'Hint: prohibition plus the verb, three words', 'You must not double the dosage if you miss a day.'),
                ('"You ', 'should not stop', ' the cream as soon as the rash fades."', 'Hint: negative advice plus the verb, three words', 'You should not stop the cream as soon as the rash fades.')],
         quiz=[('The patient asks if she can stop the medicine early. What is the safest answer?',
                [('You can stop whenever you feel better.', False),
                 ('You must finish the whole course, even if the rash clears.', True),
                 ('You have to double the dosage instead.', False),
                 ('You should throw the rest away today.', False)]),
               ('Which sentence is advice rather than an obligation?',
                [('You have to sign for this medicine.', False),
                 ('You must not take it on an empty stomach.', False),
                 ('You should keep it in the fridge.', True),
                 ('You can only get it with a prescription.', False)]),
               ('A patient says she has run out of her cream. What does she need?',
                [('A refill.', True), ('A copay.', False),
                 ('An expiration date.', False), ('An aisle.', False)]),
               ('What is a generic medicine?',
                [('A medicine that works less well.', False),
                 ('The same medicine sold without the brand name.', True),
                 ('A medicine for general symptoms.', False),
                 ('A medicine that needs no prescription.', False)])],
         fala=['You have to show the prescription to get a refill.',
               'You should check the expiration date before you use it.',
               'The generic works exactly the same, and it costs less.',
               'You must not stop the treatment as soon as it clears.',
               'Ask the pharmacist if you are not sure about the dosage.'],
         survival=['You must finish the whole course.',
                   'You should check the expiration date.',
                   'You have to show the prescription.',
                   'You can ask the pharmacist about the dosage.',
                   'Come back before you run out of it.']),

    dict(n=5, card='xp-lesson-5',
         img='https://images.unsplash.com/photo-1666214280557-f1b5022eb634?w=600&q=80',
         titulo='More Practice -- In Plain English',
         gram='defining relative clauses -- who, that, which',
         desc='A second round of Lesson 5. Same vocabulary for explaining a diagnosis, same relative clauses, new exercises.',
         vocab=[('Chronic', 'lasting a long time and coming back'),
                ('To manage', 'to keep something under control without curing it'),
                ('A cure', 'a treatment that makes an illness go away completely'),
                ('Inflammation', 'redness, heat and swelling in a part of the body'),
                ('Harmless', 'not able to cause damage'),
                ('Contagious', 'able to spread from one person to another by contact'),
                ('To reassure', 'to say something that removes worry'),
                ('A relapse', 'the return of an illness after a period of improvement')],
         banco=['who', 'that', 'which', 'who', 'that', 'which'],
         fills=[('"This is a condition ', 'that', ' we manage, not one we cure."', 'Hint: the relative pronoun for things', 'This is a condition that we manage, not one we cure.'),
                ('"The patients ', 'who', ' follow the plan have far fewer relapses."', 'Hint: the relative pronoun for people', 'The patients who follow the plan have far fewer relapses.'),
                ('"It is a harmless rash ', 'which', ' looks worse than it is."', 'Hint: another relative pronoun for things', 'It is a harmless rash which looks worse than it is.'),
                ('"The nurse ', 'who', ' called you will explain the next step."', 'Hint: the relative pronoun for people', 'The nurse who called you will explain the next step.'),
                ('"Inflammation is the process ', 'that', ' causes the redness."', 'Hint: the relative pronoun for things', 'Inflammation is the process that causes the redness.'),
                ('"This is not something ', 'that', ' you can pass to your children."', 'Hint: the relative pronoun for things', 'This is not something that you can pass to your children.')],
         quiz=[('A patient asks: "Is it contagious?" What are they worried about?',
                [('Whether it will come back.', False),
                 ('Whether other people can catch it.', True),
                 ('Whether it will leave a mark.', False),
                 ('Whether the cream is expensive.', False)]),
               ('Which sentence explains chronic in plain English?',
                [('It is something that will never affect you again.', False),
                 ('It is something that comes back and that we keep under control.', True),
                 ('It is something that only children get.', False),
                 ('It is something that a single dose will cure.', False)]),
               ('You want to reassure a worried patient. Which line does that best?',
                [('The lesion which I found is harmless, and it will not spread.', True),
                 ('We will run more tests and see.', False),
                 ('It is hard to say at this stage.', False),
                 ('That is a question for the specialist.', False)]),
               ('Which sentence uses the relative pronoun correctly?',
                [('The patient which arrived first is still waiting.', False),
                 ('The patient who arrived first is still waiting.', True),
                 ('The patient what arrived first is still waiting.', False),
                 ('The patient whose arrived first is still waiting.', False)])],
         fala=['This is a condition that we manage, not one we cure.',
               'It is harmless, and it is not contagious.',
               'To put it simply, the redness is inflammation.',
               'The patients who follow the plan have far fewer relapses.',
               'A relapse does not mean the treatment failed.'],
         survival=['This is something we manage, not something we cure.',
                   'It is harmless and it is not contagious.',
                   'To put it simply, that redness is inflammation.',
                   'A relapse does not mean the treatment failed.',
                   'The plan that works is the one you can keep.']),

    dict(n=6, card='xp-lesson-6',
         img='https://images.unsplash.com/photo-1579154204601-01588f351e67?w=600&q=80',
         titulo='More Practice -- The Case Report',
         gram='narrative tenses -- past perfect and past continuous',
         desc='A second round of Lesson 6. Same case report vocabulary, same narrative tenses, new chronology to build.',
         vocab=[('A lesion', 'an area of tissue that has been damaged or changed'),
                ('A biopsy', 'the removal of tissue so it can be examined'),
                ('A margin', 'the healthy edge of tissue around what is removed'),
                ('To excise', 'to cut something out surgically'),
                ('Pigmented', 'containing colouring, darker than the skin around it'),
                ('Asymmetry', 'the two halves not matching each other'),
                ('A stage', 'how far a disease has advanced'),
                ('A delay in presentation', 'the time between noticing a problem and seeking help')],
         banco=['had noticed', 'was growing', 'had already spread', 'was working', 'had not seen', 'were waiting'],
         fills=[('"She ', 'had noticed', ' the lesion two years before the appointment."', 'Hint: past perfect, two words', 'She had noticed the lesion two years before the appointment.'),
                ('"The lesion ', 'was growing', ' slowly while she waited."', 'Hint: past continuous, two words', 'The lesion was growing slowly while she waited.'),
                ('"By the time of the biopsy, it ', 'had already spread', '."', 'Hint: past perfect with already, three words', 'By the time of the biopsy, it had already spread.'),
                ('"She ', 'was working', ' abroad when the changes started."', 'Hint: past continuous, two words', 'She was working abroad when the changes started.'),
                ('"She ', 'had not seen', ' a dermatologist before that day."', 'Hint: past perfect negative, three words', 'She had not seen a dermatologist before that day.'),
                ('"The results ', 'were waiting', ' in the system for a week."', 'Hint: past continuous, plural subject, two words', 'The results were waiting in the system for a week.')],
         quiz=[('Which sentence shows that one action happened BEFORE another past action?',
                [('She noticed the lesion and came in.', False),
                 ('She had noticed the lesion long before she came in.', True),
                 ('She is noticing the lesion now.', False),
                 ('She will notice the lesion later.', False)]),
               ('"She was working abroad when the changes started" tells us that',
                [('the work finished before the changes.', False),
                 ('the work was in progress when the changes began.', True),
                 ('she started working because of the changes.', False),
                 ('she never worked abroad.', False)]),
               ('What does a delay in presentation refer to?',
                [('The time the laboratory took to reply.', False),
                 ('The time between noticing the problem and seeking help.', True),
                 ('The time the surgery lasted.', False),
                 ('The time the patient waited in the room.', False)]),
               ('In a case report, why do the narrative tenses matter so much?',
                [('They make the report longer.', False),
                 ('They show the order in which things happened.', True),
                 ('They are required by the journal style guide.', False),
                 ('They replace the need for dates.', False)])],
         fala=['She had noticed the lesion two years before she came in.',
               'The lesion was growing slowly while she waited.',
               'By the time of the biopsy, it had already spread.',
               'She was working abroad when the first changes appeared.',
               'The delay in presentation changed the stage at diagnosis.'],
         survival=['She had noticed it two years earlier.',
                   'The lesion was growing while she waited.',
                   'By then it had already spread.',
                   'She was working abroad at the time.',
                   'The delay in presentation changed the stage.']),
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

    dict(n=4, card='us-lesson-4',
         img='https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?w=600&q=80',
         titulo='Paperwork and Appointments',
         gram='modals -- must, have to, should, can',
         desc='The part of moving that nobody warns you about: the social security number, the ID, the DMV line and the appointment you have to book weeks ahead.',
         vocab=[('A Social Security number', 'the nine-digit number the US government uses to identify you'),
                ('An ID', 'an official document that proves who you are'),
                ('The DMV', 'the state office that handles drivers licenses and vehicles'),
                ('An appointment', 'a time booked in advance to be seen by someone'),
                ('A form', 'a printed document with spaces for your information'),
                ('Proof of address', 'a document showing where you live'),
                ('A deadline', 'the latest time by which something must be done'),
                ('To apply for', 'to make a formal request for something')],
         banco=['have to book', 'must bring', 'should arrive', 'can apply', 'do not have to pay', 'must not miss'],
         fills=[('"You ', 'have to book', ' an appointment at the DMV online."', 'Hint: obligation from a rule plus the verb, three words', 'You have to book an appointment at the DMV online.'),
                ('"You ', 'must bring', ' proof of address to the interview."', 'Hint: strong obligation plus the verb, two words', 'You must bring proof of address to the interview.'),
                ('"You ', 'should arrive', ' twenty minutes early, just in case."', 'Hint: advice plus the verb, two words', 'You should arrive twenty minutes early, just in case.'),
                ('"You ', 'can apply', ' for the Social Security number in person."', 'Hint: possibility plus the verb, two words', 'You can apply for the Social Security number in person.'),
                ('"You ', 'do not have to pay', ' anything for the number itself."', 'Hint: absence of obligation plus the verb, five words', 'You do not have to pay anything for the number itself.'),
                ('"You ', 'must not miss', ' the deadline on the form."', 'Hint: prohibition plus the verb, three words', 'You must not miss the deadline on the form.')],
         quiz=[('The clerk asks for proof of address. What can you show?',
                [('Your passport photo page.', False),
                 ('A utility bill with your name and address on it.', True),
                 ('Your plane ticket.', False),
                 ('A photo of your building.', False)]),
               ('Which sentence means there is NO obligation?',
                [('You must not bring the original.', False),
                 ('You do not have to bring the original.', True),
                 ('You have to bring the original.', False),
                 ('You should bring the original.', False)]),
               ('You need a drivers license. Where do you go?',
                [('The DMV.', True), ('The pharmacy.', False),
                 ('The Social Security office.', False), ('The landlord.', False)]),
               ('How do you ask politely whether an appointment is needed?',
                [('I need appointment now.', False),
                 ('Do I have to make an appointment, or can I just come in?', True),
                 ('Appointment?', False),
                 ('Give me an appointment.', False)])],
         fala=['Do I have to make an appointment, or can I just walk in?',
               'I would like to apply for a Social Security number.',
               'What do I have to bring as proof of address?',
               'Could you tell me what the deadline is?',
               'I filled in the form, but I am not sure about this part.'],
         survival=['Do I have to make an appointment?',
                   'What do I need to bring with me?',
                   'I would like to apply for a Social Security number.',
                   'Could you tell me what the deadline is?',
                   'I am not sure about this part of the form.']),

    dict(n=5, card='us-lesson-5',
         img='https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?w=600&q=80',
         titulo='Getting Around the City',
         gram='defining relative clauses -- who, that, which',
         desc='The subway, the bus, the ride you order on your phone and the stranger you ask for directions when the phone dies.',
         vocab=[('A transit card', 'the card you load with money to ride buses and trains'),
                ('A ride', 'a trip in a car, often one you order on an app'),
                ('A stop', 'the place where a bus or train lets people off'),
                ('A transfer', 'a change from one line or bus to another'),
                ('Rush hour', 'the part of the day when traffic is heaviest'),
                ('One-way', 'going in a single direction only'),
                ('A crosswalk', 'the marked part of the street where people cross'),
                ('To get off', 'to leave a bus or train')],
         banco=['that', 'who', 'which', 'that', 'who', 'which'],
         fills=[('"This is the train ', 'that', ' goes downtown."', 'Hint: the relative pronoun for things', 'This is the train that goes downtown.'),
                ('"The driver ', 'who', ' picked me up was very friendly."', 'Hint: the relative pronoun for people', 'The driver who picked me up was very friendly.'),
                ('"I missed the stop ', 'which', ' is closest to my building."', 'Hint: another relative pronoun for things', 'I missed the stop which is closest to my building.'),
                ('"Is this the bus ', 'that', ' stops at the hospital?"', 'Hint: the relative pronoun for things', 'Is this the bus that stops at the hospital?'),
                ('"The woman ', 'who', ' gave me directions was a nurse too."', 'Hint: the relative pronoun for people', 'The woman who gave me directions was a nurse too.'),
                ('"I take the line ', 'which', ' runs every ten minutes."', 'Hint: another relative pronoun for things', 'I take the line which runs every ten minutes.')],
         quiz=[('You are on the train and you are not sure where to leave. What do you ask?',
                [('Where I get off?', False),
                 ('Could you tell me which stop is closest to the hospital?', True),
                 ('Stop hospital where?', False),
                 ('I want hospital.', False)]),
               ('What is a transfer?',
                [('The money you pay for the ride.', False),
                 ('A change from one line or bus to another.', True),
                 ('The card you tap at the gate.', False),
                 ('The last stop on the line.', False)]),
               ('Someone says: "You want the one that runs express." What do they mean?',
                [('That train skips some stops and is faster.', True),
                 ('That train is out of service.', False),
                 ('That train costs more.', False),
                 ('That train only runs at night.', False)]),
               ('Which sentence is correct?',
                [('This is the bus who goes downtown.', False),
                 ('This is the bus that goes downtown.', True),
                 ('This is the bus what goes downtown.', False),
                 ('This is the bus where goes downtown.', False)])],
         fala=['Excuse me, is this the train that goes downtown?',
               'Could you tell me which stop is closest to the hospital?',
               'Do I have to transfer, or does this one go straight there?',
               'I think I missed my stop. Where should I get off?',
               'How much do I need to put on the transit card?'],
         survival=['Is this the train that goes downtown?',
                   'Which stop is closest to the hospital?',
                   'Do I have to transfer?',
                   'I think I missed my stop.',
                   'How much do I put on the card?']),

    dict(n=6, card='us-lesson-6',
         img='https://images.unsplash.com/photo-1497366216548-37526070297c?w=600&q=80',
         titulo='Starting a New Job',
         gram='future -- will, going to and the present continuous',
         desc='The first week in an American workplace: introducing yourself, understanding what is expected, and saying what you are going to do next.',
         vocab=[('An onboarding', 'the process of settling a new person into a job'),
                ('A shift', 'the set hours a person works'),
                ('A supervisor', 'the person who is responsible for your work'),
                ('A deadline', 'the latest time by which something must be done'),
                ('To follow up', 'to check back on something after a first contact'),
                ('To reach out', 'to contact someone'),
                ('A heads-up', 'a short warning given in advance'),
                ('To be on call', 'to be available to work if you are needed')],
         banco=['will', 'am going to', 'am meeting', 'will not', 'is going to', 'are starting'],
         fills=[('"I ', 'will', ' send you the file this afternoon."', 'Hint: a decision made as you speak, one word', 'I will send you the file this afternoon.'),
                ('"I ', 'am going to', ' apply for the license next month."', 'Hint: a decision already made, three words', 'I am going to apply for the license next month.'),
                ('"I ', 'am meeting', ' my supervisor at nine tomorrow."', 'Hint: present continuous for a fixed arrangement, two words', 'I am meeting my supervisor at nine tomorrow.'),
                ('"I ', 'will not', ' be able to take that shift on Friday."', 'Hint: the full negative of will, two words', 'I will not be able to take that shift on Friday.'),
                ('"The team ', 'is going to', ' change the schedule in April."', 'Hint: a decision already made, three words', 'The team is going to change the schedule in April.'),
                ('"We ', 'are starting', ' the new system on Monday."', 'Hint: present continuous for a fixed arrangement, two words', 'We are starting the new system on Monday.')],
         quiz=[('A colleague says: "I will get back to you." What does that mean?',
                [('They will contact you again later.', True),
                 ('They are leaving the company.', False),
                 ('They disagree with you.', False),
                 ('They want you to go back.', False)]),
               ('Which sentence describes a plan you already decided before speaking?',
                [('I will call the lab, then.', False),
                 ('I am going to call the lab this week.', True),
                 ('I call the lab every week.', False),
                 ('I called the lab yesterday.', False)]),
               ('Your supervisor asks you to give them a heads-up. They want you to',
                [('warn them in advance.', True),
                 ('raise your hand in meetings.', False),
                 ('finish earlier than planned.', False),
                 ('send a written report.', False)]),
               ('Which is the most natural way to introduce yourself on day one?',
                [('I am the new one.', False),
                 ('Hi, I am Diego. I just started this week, in dermatology.', True),
                 ('Diego. Dermatology. Hello.', False),
                 ('You will work with me now.', False)])],
         fala=['Hi, I am Diego. I just started this week.',
               'I am meeting my supervisor at nine tomorrow.',
               'I am going to apply for the license next month.',
               'I will follow up with you by the end of the day.',
               'Thanks for the heads-up. I will keep that in mind.'],
         survival=['Hi, I am Diego. I just started this week.',
                   'I will follow up by the end of the day.',
                   'I am going to apply for the license next month.',
                   'I am meeting my supervisor tomorrow.',
                   'Thanks for the heads-up.']),
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
#
# 12 musicas, cada uma virando uma mini-licao. Links do YouTube e do Genius
# VERIFICADOS um a um por HTTP (REGRA 17: video/pagina EXATOS, nunca busca).
#
# SOBRE A LETRA -- por que ela nao esta aqui dentro
# -------------------------------------------------
# Letra de musica e conteudo protegido, entao o material NAO a reproduz: nem
# inteira, nem remontada pela soma dos exercicios. A aluno chega na letra pelo
# botao "Read the lyrics", que aponta para a pagina oficial no Genius.
# Em consequencia, o exercicio de escuta usa 3 trechos CURTOS e NAO CONTIGUOS,
# e o volume de pratica vem de um bloco NOVO -- "Practise the structure" --
# com 4 frases ESCRITAS PARA O DIEGO na mesma gramatica da musica. Da mais
# exercicio que ampliar as lacunas da letra, e ensina melhor: aplicar a
# estrutura num contexto novo vale mais que completar o mesmo verso.
#
# Cada musica: 3 lacunas de escuta + 6 palavras de matching + 4 lacunas de
# aplicacao + 3 perguntas de compreensao + 1 speech card = 17 itens
# (contra 2 na primeira versao).

GOSPEL = [
    dict(vid='KBD18rsVJHk', lyr='https://genius.com/Chris-tomlin-how-great-is-our-god-lyrics',
         artista='Chris Tomlin', titulo='How Great Is Our God', gram='Present simple',
         nota='The chorus is one sentence repeated until you cannot get it wrong: subject, present simple verb, complement. It is the structure of your Lesson 1, sung slowly.',
         tip='Tip: sing along twice. The second time, listen to how is almost always reduced to a z sound attached to the word before it.',
         ouca=[('"How great ', 'is', ' our God, sing with me"', 'Hint: present simple of the verb to be, third person', 'How great is our God, sing with me'),
               ('"Let all the earth ', 'rejoice', '"', 'Hint: a verb meaning to feel and show great joy', 'Let all the earth rejoice'),
               ('"Age to age He ', 'stands', '"', 'Hint: present simple of the verb to stand', 'Age to age He stands')],
         vocab=[('Splendor', 'great beauty that attracts attention'),
                ('Majesty', 'the dignity and power of a king'),
                ('To rejoice', 'to feel and show great joy'),
                ('To tremble', 'to shake, often from fear or cold'),
                ('Darkness', 'the total absence of light'),
                ('Age to age', 'from one period of history to the next')],
         aplica=[('"My shift ', 'starts', ' at seven every morning."', 'Hint: present simple, third person singular', 'My shift starts at seven every morning.'),
                 ('"The clinic ', 'closes', ' at six on Fridays."', 'Hint: present simple, third person singular', 'The clinic closes at six on Fridays.'),
                 ('"I ', 'sing', ' this song on the way to work."', 'Hint: present simple, first person', 'I sing this song on the way to work.'),
                 ('"Nurses ', 'work', ' longer hours than people think."', 'Hint: present simple, plural subject, no final s', 'Nurses work longer hours than people think.')],
         quiz=[('What does the song ask everyone on earth to do?',
                [('To stay silent.', False), ('To rejoice and sing.', True),
                 ('To tremble in fear.', False), ('To wait until morning.', False)]),
               ('"Age to age He stands" suggests that God',
                [('changes with every generation.', False), ('stood only once, long ago.', False),
                 ('does not change as time passes.', True), ('will stand only in the future.', False)]),
               ('Why is the whole chorus in the present simple?',
                [('Because it describes something always true, not a single moment.', True),
                 ('Because the present simple is easier to sing.', False),
                 ('Because it happened yesterday.', False),
                 ('Because it is a plan for next week.', False)])],
         fala='I sing this song when I need to remember what is always true.'),

    dict(vid='izrk-erhDdk', lyr='https://genius.com/Hillsong-worship-cornerstone-lyrics',
         artista='Hillsong Worship', titulo='Cornerstone', gram='Relative clauses',
         nota='A song built on relative clauses. Good for hearing the linking you practised in Lesson 5, at a speed you can follow.',
         tip='Tip: open the lyrics and find every that and who. Write down which word each one refers back to.',
         ouca=[('"My hope is built on nothing ', 'less', '"', 'Hint: the opposite of more', 'My hope is built on nothing less'),
               ('"Weak made ', 'strong', " in the Savior's love\"", 'Hint: the opposite of weak', "Weak made strong in the Savior's love"),
               ('"Christ alone, ', 'cornerstone', '"', 'Hint: the word in the title of the song', 'Christ alone, cornerstone')],
         vocab=[('A cornerstone', 'the first stone set, that the whole building lines up with'),
                ('Hope', 'the feeling that what you want can happen'),
                ('An oath', 'a serious formal promise'),
                ('An anchor', 'a heavy object that holds a ship in place'),
                ('A gale', 'a very strong wind'),
                ('To sink', 'to go down below the surface')],
         aplica=[('"The colleague ', 'who', ' covered my shift is from Recife."', 'Hint: the relative pronoun for people', 'The colleague who covered my shift is from Recife.'),
                 ('"The cream ', 'that', ' I prescribed is over-the-counter."', 'Hint: the relative pronoun for things', 'The cream that I prescribed is over-the-counter.'),
                 ('"The hospital ', 'which', ' trained me is in Sao Paulo."', 'Hint: another relative pronoun for things', 'The hospital which trained me is in Sao Paulo.'),
                 ('"The patient ', 'who', ' called yesterday is waiting outside."', 'Hint: the relative pronoun for people', 'The patient who called yesterday is waiting outside.')],
         quiz=[('In building, what is a cornerstone?',
                [('A decorative stone on the roof.', False),
                 ('The first stone set, that the rest of the building lines up with.', True),
                 ('The last stone added at the end.', False),
                 ('A stone used to block a door.', False)]),
               ('"In every high and stormy gale" refers to',
                [('good weather for sailing.', False), ('the hardest moments of life.', True),
                 ('a holiday by the sea.', False), ('the sound of the choir.', False)]),
               ('Calling Christ the cornerstone means that',
                [('everything else is built on Him.', True),
                 ('He is one option among many.', False),
                 ('He is at the top of the building.', False),
                 ('He is only decoration.', False)])],
         fala='The song calls Christ the cornerstone, which means everything else is built on Him.'),

    dict(vid='iBmwwwiHrOk', lyr='https://genius.com/Chris-tomlin-good-good-father-lyrics',
         artista='Chris Tomlin', titulo='Good Good Father', gram='Relative clauses',
         nota='The chorus is literally a relative clause: it is who You are. If you understand that line, you have understood all of Lesson 5.',
         tip='Tip: notice that who here does not open a question. It links two ideas. That is exactly the difference Lesson 5 worked on.',
         ouca=[("\"You're a good, good ", 'Father', '"', 'Hint: the word in the title of the song', "You're a good, good Father"),
               ("\"It's ", 'who', ' You are"', 'Hint: the relative pronoun for people', "It's who You are"),
               ('"And I\'m ', 'loved', ' by You"', 'Hint: past participle of the verb to love, in the passive', "And I'm loved by You")],
         vocab=[('To whisper', 'to speak very quietly'),
                ('Perfect', 'with no faults at all'),
                ('Peace', 'a state of calm, with no worry or conflict'),
                ('Identity', 'who a person really is'),
                ('To overwhelm', 'to affect someone very strongly'),
                ('Beloved', 'deeply loved')],
         aplica=[('"The nurse ', 'who', ' trained me still works here."', 'Hint: the relative pronoun for people', 'The nurse who trained me still works here.'),
                 ('"The paper ', 'that', ' I read last night was excellent."', 'Hint: the relative pronoun for things', 'The paper that I read last night was excellent.'),
                 ('"This is the clinic ', 'where', ' I did my residency."', 'Hint: the relative word for places', 'This is the clinic where I did my residency.'),
                 ('"The rash', 'that', ' worried her turned out to be harmless."', 'Hint: the relative pronoun for things', 'The rash that worried her turned out to be harmless.')],
         quiz=[('In "It is who You are", the word who refers to',
                [('the singer.', False), ('the Father just mentioned.', True),
                 ('a question being asked.', False), ('nobody in particular.', False)]),
               ('The song contrasts the stories people tell with',
                [('what the singer has found to be true.', True),
                 ('what the newspapers report.', False),
                 ('what the choir sings.', False),
                 ('what happened last year.', False)]),
               ('"I am loved by You" is an example of',
                [('the present continuous.', False), ('the passive voice.', True),
                 ('a question.', False), ('the past simple.', False)])],
         fala='The line that stays with me is the one that says it is who You are.'),

    dict(vid='SzG-WKIVH0w', lyr='https://genius.com/Matt-redman-10000-reasons-bless-the-lord-lyrics',
         artista='Matt Redman', titulo='10,000 Reasons (Bless the Lord)', gram='Present simple',
         nota='British English, very clean diction and a slow tempo. The verse is all present simple and imperatives, the two simplest forms you have.',
         tip='Tip: this is the best one on the list to start with. Listen once just listening, then read the lyrics out loud along with it.',
         ouca=[('"', 'Bless', ' the Lord, O my soul"', 'Hint: the verb that opens the song, in the imperative', 'Bless the Lord, O my soul'),
               ('"Worship His ', 'holy', ' name"', 'Hint: pure and set apart', 'Worship His holy name'),
               ('"Sing like never ', 'before', '"', 'Hint: the opposite of after', 'Sing like never before')],
         vocab=[('To bless', 'to praise, to speak well of someone'),
                ('The soul', 'the spiritual part of a person'),
                ('To worship', 'to show deep respect and love'),
                ('Holy', 'pure and set apart'),
                ('Dawn', 'the first light of the morning'),
                ('Whatever', 'anything at all that')],
         aplica=[('"The sun ', 'comes', ' up before my first patient arrives."', 'Hint: present simple, third person singular', 'The sun comes up before my first patient arrives.'),
                 ('"I ', 'count', ' the good things at the end of the day."', 'Hint: present simple, first person', 'I count the good things at the end of the day.'),
                 ('"Gratitude ', 'changes', ' how a long shift feels."', 'Hint: present simple, third person singular', 'Gratitude changes how a long shift feels.'),
                 ('"My colleagues ', 'sing', ' this one in the car."', 'Hint: present simple, plural subject', 'My colleagues sing this one in the car.')],
         quiz=[('When the singer says "O my soul", who is he speaking to?',
                [('The congregation.', False), ('Himself.', True),
                 ('A friend beside him.', False), ('The band.', False)]),
               ('"Sing like never before" is',
                [('an instruction he gives himself.', True), ('a complaint.', False),
                 ('a question.', False), ('a report about yesterday.', False)]),
               ('What is the singer counting in this song?',
                [('The years of his life.', False), ('Reasons to be thankful.', True),
                 ('The people in the room.', False), ('The verses of the song.', False)])],
         fala='Every morning gives me one more reason to be thankful.'),

    dict(vid='IvSuGyJQ6oM', lyr='https://genius.com/Bethel-music-goodness-of-god-lyrics',
         artista='Bethel Music and Jenn Johnson', titulo='Goodness of God', gram='Present continuous',
         nota='"Your goodness is running after me" is present continuous, and the image is easy to remember. Same structure as Lesson 1.',
         tip='Tip: listen to the chorus three times in a row. Notice that is running describes something in progress, not a habit.',
         ouca=[('"Your ', 'goodness', ' is running after me"', 'Hint: the noun in the title of the song', 'Your goodness is running after me'),
               ('"I sing of the goodness of ', 'God', '"', 'Hint: who the song is about', 'I sing of the goodness of God'),
               ('"With my life laid ', 'down', '"', 'Hint: the opposite of up', 'With my life laid down')],
         vocab=[('Goodness', 'the quality of being kind and good'),
                ('Faithful', 'always loyal, never failing'),
                ('Mercy', 'kindness shown when punishment could be given'),
                ('To surrender', 'to stop fighting and give up control'),
                ('To sustain', 'to keep someone going through difficulty'),
                ('All my life', 'from the beginning until now')],
         aplica=[('"I ', 'am learning', ' to notice the good days."', 'Hint: present continuous, two words', 'I am learning to notice the good days.'),
                 ('"My English ', 'is getting', ' better this year."', 'Hint: present continuous, two words', 'My English is getting better this year.'),
                 ('"She ', 'is running', ' late for the consultation."', 'Hint: present continuous, two words', 'She is running late for the consultation.'),
                 ('"We ', 'are moving', ' to the United States next year."', 'Hint: present continuous for a firm future plan, two words', 'We are moving to the United States next year.')],
         quiz=[('"Your goodness is running after me" pictures goodness as',
                [('something far away.', False), ('something chasing him.', True),
                 ('something he lost.', False), ('something he must earn.', False)]),
               ('The form "is running" tells us the action is',
                [('finished long ago.', False), ('in progress.', True),
                 ('a fixed habit.', False), ('impossible.', False)]),
               ('"All my life You have been faithful" looks at',
                [('one single day.', False), ('the whole of his life up to now.', True),
                 ('only the future.', False), ('other people, not him.', False)])],
         fala='I am learning to notice what is happening in my life right now.'),

    dict(vid='KwX1f2gYKZ4', lyr='https://genius.com/Elevation-worship-graves-into-gardens-lyrics',
         artista='Elevation Worship', titulo='Graves Into Gardens', gram='Present simple',
         nota='The chorus repeats the same structure four times, changing only the object: You turn X into Y. Excellent for fixing the present simple without effort.',
         tip='Tip: after listening, build three sentences of your own with You turn ___ into ___ and record yourself saying them.',
         ouca=[('"You turn ', 'graves', ' into gardens"', 'Hint: the word in the title, plural', 'You turn graves into gardens'),
               ('"You turn seas into ', 'highways', '"', 'Hint: wide fast roads, in American English', 'You turn seas into highways'),
               ('"You turn bones into ', 'armies', '"', 'Hint: large organized groups of soldiers, plural', 'You turn bones into armies')],
         vocab=[('A grave', 'the place where a dead person is buried'),
                ('A garden', 'a piece of ground for growing plants'),
                ('A highway', 'a wide road built for fast traffic'),
                ('An army', 'a large organized group of soldiers'),
                ('Shame', 'a painful feeling about something you did'),
                ('Glory', 'great honour and praise')],
         aplica=[('"Rest ', 'turns', ' a bad week into a manageable one."', 'Hint: present simple, third person singular', 'Rest turns a bad week into a manageable one.'),
                 ('"Practice ', 'makes', ' the hard cases feel routine."', 'Hint: present simple, third person singular', 'Practice makes the hard cases feel routine.'),
                 ('"Small habits ', 'change', ' the whole year."', 'Hint: present simple, plural subject', 'Small habits change the whole year.'),
                 ('"This song ', 'reminds', ' me that nothing is finished yet."', 'Hint: present simple, third person singular', 'This song reminds me that nothing is finished yet.')],
         quiz=[('What do the four images of the chorus have in common?',
                [('Something dead becomes something alive.', True),
                 ('They all describe the weather.', False),
                 ('They are all about buildings.', False),
                 ('They all happened in the past.', False)]),
               ('"You turn seas into highways" suggests that',
                [('the sea is dangerous.', False), ('a way opens where there was none.', True),
                 ('the singer likes driving.', False), ('the journey is cancelled.', False)]),
               ('The verb form "You turn" is used because the song is describing',
                [('a single event last night.', False), ('what is always true.', True),
                 ('a plan for tomorrow.', False), ('something impossible.', False)])],
         fala='Rest turns a bad week into a manageable one.'),

    dict(vid='N8WK9HmF53w', lyr='https://genius.com/Lauren-daigle-you-say-lyrics',
         artista='Lauren Daigle', titulo='You Say', gram='Present simple and passive',
         nota='The whole song is a contrast between two present simple sentences, and the answers come in the passive: I am loved, I am strong. Lesson 1 and Lesson 2 on the same track.',
         tip='Tip: open the lyrics and split a page into two columns, You say and I say. Write each line on the right side.',
         ouca=[('"You ', 'say', " I am loved when I can't feel a thing\"", 'Hint: the verb in the title', "You say I am loved when I can't feel a thing"),
               ('"You say I am strong when I think I am ', 'weak', '"', 'Hint: the opposite of strong', 'You say I am strong when I think I am weak'),
               ('"I ', 'believe', ' what You say of me"', 'Hint: to accept that something is true', 'I believe what You say of me')],
         vocab=[('Worth', 'the value that someone or something has'),
                ('Identity', 'who a person really is'),
                ('To remind', 'to help someone remember'),
                ('To belong', 'to be in the right place'),
                ('To doubt', 'to feel unsure that something is true'),
                ('In spite of', 'even though something is the case')],
         aplica=[('"The diagnosis ', 'was confirmed', ' by the biopsy."', 'Hint: past passive, two words', 'The diagnosis was confirmed by the biopsy.'),
                 ('"These results ', 'are reviewed', ' every six months."', 'Hint: present passive, plural, two words', 'These results are reviewed every six months.'),
                 ('"I ', 'was told', ' the referral had already been sent."', 'Hint: past passive of the verb to tell, two words', 'I was told the referral had already been sent.'),
                 ('"The form ', 'is signed', ' by the patient, not the doctor."', 'Hint: present passive, singular, two words', 'The form is signed by the patient, not the doctor.')],
         quiz=[('What does the song contrast?',
                [('Two different singers.', False),
                 ('What the singer feels and what God says.', True),
                 ('The past and the future.', False),
                 ('Two cities.', False)]),
               ('"I am loved" and "I am held" are examples of',
                [('the passive voice.', True), ('questions.', False),
                 ('the imperative.', False), ('the past continuous.', False)]),
               ('"when I cannot feel a thing" describes a moment when the singer',
                [('is completely certain.', False), ('feels nothing at all.', True),
                 ('is physically hurt.', False), ('is asleep.', False)])],
         fala='What I feel about myself and what is true about me are not always the same thing.'),

    dict(vid='JGYjKR69M6U', lyr='https://genius.com/Zach-williams-chain-breaker-lyrics',
         artista='Zach Williams', titulo='Chain Breaker', gram='First conditional',
         nota='Every line of the chorus is a first conditional: if you have got pain, He is a pain taker. It is all of Lesson 8, in the form of a song.',
         tip='Tip: count how many times if appears in the lyrics. Then write three sentences of your own in the same shape: If ___, ___.',
         ouca=[("\"If you've got pain, He's a pain ", 'taker', '"', 'Hint: the person who takes something, built from take', "If you've got pain, He's a pain taker"),
               ('"If you feel lost, He\'s a way ', 'maker', '"', 'Hint: the person who makes something, built from make', "If you feel lost, He's a way maker"),
               ('"If you ', 'believe', ' it, if you receive it"', 'Hint: to accept that something is true', 'If you believe it, if you receive it')],
         vocab=[('A chain', 'connected metal rings used to tie something up'),
                ('A breaker', 'a person or thing that breaks something'),
                ('Freedom', 'the state of being free'),
                ('A prison', 'a place where people are locked up'),
                ('To shake', 'to move quickly back and forth'),
                ('To receive', 'to take or accept something that is given')],
         aplica=[('"If the rash ', 'spreads', ', call the clinic."', 'Hint: first conditional, present simple after if', 'If the rash spreads, call the clinic.'),
                 ('"If I ', 'finish', ' early, I will study English."', 'Hint: present simple after if, even for the future', 'If I finish early, I will study English.'),
                 ('"If you take the cream twice a day, it ', 'will work', ' faster."', 'Hint: the future half of the first conditional, two words', 'If you take the cream twice a day, it will work faster.'),
                 ('"If the test ', 'comes', ' back clear, we will stop the treatment."', 'Hint: present simple after if, third person singular', 'If the test comes back clear, we will stop the treatment.')],
         quiz=[('What pattern does every line of the chorus follow?',
                [('A question and an answer.', False),
                 ('If + a situation, then who He is.', True),
                 ('A list of names.', False),
                 ('A story in the past.', False)]),
               ('"A prison-shaking Savior" suggests someone',
                [('strong enough to open what is locked.', True),
                 ('who is afraid of prisons.', False),
                 ('who built the prison.', False),
                 ('who is locked up himself.', False)]),
               ('In "If you have got chains", the word chains stands for',
                [('jewellery.', False), ('whatever is holding the person back.', True),
                 ('a bicycle part.', False), ('a kind of music.', False)])],
         fala='If you feel stuck, this is the song to put on.'),

    dict(vid='ZNDEyxEMNp0', lyr='https://genius.com/Mercyme-i-can-only-imagine-lyrics',
         artista='MercyMe', titulo='I Can Only Imagine', gram='Future with will',
         nota='The song is a sequence of future questions with will: will I dance, will I sing. Exactly what you worked on in Lesson 10.',
         tip='Tip: open the lyrics and write down every question with will. Then answer each one out loud.',
         ouca=[('"What ', 'will', ' my heart feel?"', 'Hint: the future auxiliary from Lesson 10', 'What will my heart feel?'),
               ('"Will I dance for You, Jesus, or in awe of You be ', 'still', '?"', 'Hint: not moving at all', 'Will I dance for You, Jesus, or in awe of You be still?'),
               ('"Surrounded by Your ', 'glory', '"', 'Hint: great splendour and honour', 'Surrounded by Your glory')],
         vocab=[('To imagine', 'to form a picture of something in your mind'),
                ('Awe', 'a feeling of great respect mixed with wonder'),
                ('Surrounded', 'with things or people on every side'),
                ('Glory', 'great splendour and honour'),
                ('Still', 'not moving at all'),
                ('Forever', 'for all time, with no end')],
         aplica=[('"I ', 'will finish', ' my residency next year."', 'Hint: future with will, two words', 'I will finish my residency next year.'),
                 ('"', 'Will', ' you send me the results tomorrow?"', 'Hint: the auxiliary that opens a future question', 'Will you send me the results tomorrow?'),
                 ('"The clinic ', 'will not', ' open on the holiday."', 'Hint: the full negative of will, two words', 'The clinic will not open on the holiday.'),
                 ('"I ', 'am going', ' to apply for the exam in March."', 'Hint: going to, for a decision already made, two words', 'I am going to apply for the exam in March.')],
         quiz=[('The whole song is built on',
                [('questions about the future.', True), ('memories of childhood.', False),
                 ('instructions for the band.', False), ('a list of names.', False)]),
               ('"In awe of You be still" describes someone who',
                [('is bored.', False), ('is too amazed to move.', True),
                 ('is running away.', False), ('is asleep.', False)]),
               ('"I can only imagine" means the singer',
                [('has already been there.', False),
                 ('can picture it but does not know for certain.', True),
                 ('refuses to think about it.', False),
                 ('is describing a memory.', False)])],
         fala='I can only imagine what that day will be like.'),

    dict(vid='dy9nwe9_xzw', lyr='https://genius.com/Hillsong-united-oceans-where-feet-may-fail-lyrics',
         artista='Hillsong UNITED', titulo='Oceans (Where Feet May Fail)', gram='Future with will',
         nota='Slow, with a lot of space between the words, so it is one of the best on this list for training your ear. The chorus alternates present simple and future with will.',
         tip='Tip: because it is slow, use the 0.75x speed button at the top of this material to follow the lyrics without rushing.',
         ouca=[("\"You've never failed and You ", "won't", ' start now"', 'Hint: the contracted negative of will', "You've never failed and You won't start now", 'will not'),
               ('"Spirit ', 'lead', ' me where my trust is without borders"', 'Hint: to guide someone', 'Spirit lead me where my trust is without borders'),
               ('"Let me walk upon the ', 'waters', '"', 'Hint: another word for the sea, plural', 'Let me walk upon the waters')],
         vocab=[('An ocean', 'a very large area of sea'),
                ('A border', 'a line that marks where something ends'),
                ('Trust', 'firm belief that someone is reliable'),
                ('Deeper', 'further down below the surface'),
                ('To fail', 'to not succeed'),
                ('To wander', 'to walk with no fixed direction')],
         aplica=[('"I ', 'will let', ' you know as soon as the result arrives."', 'Hint: future with will, two words', 'I will let you know as soon as the result arrives.'),
                 ('"We ', 'are going', ' to live in the United States."', 'Hint: going to, for a decision already made, two words', 'We are going to live in the United States.'),
                 ('"She ', "won't", ' be back before Monday."', 'Hint: the contracted negative of will', "She won't be back before Monday.", 'will not'),
                 ('"The flight ', 'leaves', ' at six tomorrow morning."', 'Hint: present simple for a timetable', 'The flight leaves at six tomorrow morning.')],
         quiz=[('"Trust without borders" means trust that',
                [('has no limits.', True), ('needs a passport.', False),
                 ('is only for home.', False), ('has already ended.', False)]),
               ('"You have never failed and You will not start now" combines',
                [('two questions.', False), ('the past and the future.', True),
                 ('two commands.', False), ('two names.', False)]),
               ('"Where feet may fail" describes a place where',
                [('walking is easy.', False), ('you cannot stand on your own.', True),
                 ('shoes are required.', False), ('the singer grew up.', False)])],
         fala='I want a trust that has no borders.'),

    dict(vid='-pD2zIuiC2g', lyr='https://genius.com/Tasha-cobbs-leonard-break-every-chain-lyrics',
         artista='Tasha Cobbs', titulo='Break Every Chain', gram='Present simple with there is',
         nota='A very short lyric, repeated many times. Perfect for day one: you learn the whole song in a single listen.',
         tip='Tip: sing along without looking at the lyrics on the third time. There are few words, and the repetition does the work.',
         ouca=[('"There is ', 'power', ' in the name of Jesus"', 'Hint: the ability to do something', 'There is power in the name of Jesus'),
               ('"There is power in the ', 'name', ' of Jesus"', 'Hint: what a person is called', 'There is power in the name of Jesus'),
               ('"To break every ', 'chain', '"', 'Hint: the word in the title, singular', 'To break every chain')],
         vocab=[('Power', 'the ability to do something'),
                ('A chain', 'connected metal rings used to tie something up'),
                ('An army', 'a large organized group of soldiers'),
                ('To rise up', 'to stand up and move upward'),
                ('To break', 'to separate into pieces by force'),
                ('Every', 'each one, with no exception')],
         aplica=[('"There ', 'is', ' a pharmacy on the corner."', 'Hint: singular, for one thing', 'There is a pharmacy on the corner.'),
                 ('"There ', 'are', ' three patients waiting outside."', 'Hint: plural, for more than one', 'There are three patients waiting outside.'),
                 ('"There ', 'is not', ' any cream left in the drawer."', 'Hint: the full negative, singular, two words', 'There is not any cream left in the drawer.'),
                 ('"', 'Is', ' there a form I have to sign?"', 'Hint: the question form, singular', 'Is there a form I have to sign?')],
         quiz=[('"There is power in the name of Jesus" uses there is to',
                [('give an order.', False), ('say that something exists.', True),
                 ('ask a question.', False), ('describe the past.', False)]),
               ('Why does the song repeat the same lines so many times?',
                [('The writer ran out of words.', False),
                 ('So a whole room can sing it together without the words in front of them.', True),
                 ('To make the song longer than the others.', False),
                 ('Because the lines are hard to pronounce.', False)]),
               ('In this song, chains stand for',
                [('anything that keeps a person trapped.', True),
                 ('a piece of jewellery.', False),
                 ('part of a bicycle.', False),
                 ('a type of dance.', False)])],
         fala='There is power in a song you can sing without the words in front of you.'),

    dict(vid='0YUGwUgBvTU', lyr='https://genius.com/Casting-crowns-praise-you-in-this-storm-lyrics',
         artista='Casting Crowns', titulo='Praise You In This Storm', gram='Past simple',
         nota='The lyric tells a story in the past before it reaches the chorus. It is the narrative past simple you saw in Lesson 6, in very well articulated American English.',
         tip='Tip: open the lyrics and underline every past tense verb in the first verse. Then retell the story in your own words.',
         ouca=[("\"And I'll praise You in this ", 'storm', '"', 'Hint: very bad weather with strong wind', "And I'll praise You in this storm"),
               ('"I was ', 'sure', ' by now You would have reached down"', 'Hint: certain, with no doubt', 'I was sure by now You would have reached down'),
               ('"And wiped our ', 'tears', ' away"', 'Hint: drops of water from the eyes', 'And wiped our tears away')],
         vocab=[('A storm', 'very bad weather with strong wind and rain'),
                ('Thunder', 'the loud noise that follows lightning'),
                ('Tears', 'drops of water that come from the eyes'),
                ('To praise', 'to express strong approval or admiration'),
                ('To reach down', 'to stretch your hand down towards someone'),
                ('To wipe away', 'to remove something by rubbing gently')],
         aplica=[('"The pain ', 'began', ' three weeks before she came in."', 'Hint: past simple of the verb to begin', 'The pain began three weeks before she came in.'),
                 ('"She ', 'did not tell', ' anyone at first."', 'Hint: past simple negative, three words', 'She did not tell anyone at first.'),
                 ('"', 'Did', ' the treatment help at all?"', 'Hint: the past simple auxiliary in a question', 'Did the treatment help at all?'),
                 ('"I ', 'was', ' on call the night it happened."', 'Hint: past of the verb to be, first person', 'I was on call the night it happened.')],
         quiz=[('When does the singer praise God?',
                [('Only after the storm has passed.', False),
                 ('While the storm is still happening.', True),
                 ('Before the storm begins.', False),
                 ('He decides not to praise at all.', False)]),
               ('"I was sure by now You would have reached down" expresses',
                [('an expectation that was not met.', True),
                 ('a promise he made.', False),
                 ('a plan for next week.', False),
                 ('a question he asked a friend.', False)]),
               ('The first verse of the song is mostly in',
                [('the present simple.', False), ('the past simple.', True),
                 ('the imperative.', False), ('the future with will.', False)])],
         fala='I was sure the answer would come sooner, and it did not.'),
]


def render_gospel():
    cards = []
    for i, s in enumerate(GOSPEL, 1):
        blocos = (
            '      <div style="margin-top:.9rem;padding-top:.8rem;border-top:1px solid var(--border)">\n'
            '        <div style="font-size:.78rem;font-weight:600;margin-bottom:.5rem">1. Fill in what you hear</div>\n%s\n'
            '        <div style="font-size:.78rem;font-weight:600;margin:.9rem 0 .5rem">2. Words from this song</div>\n%s\n'
            '        <div style="font-size:.78rem;font-weight:600;margin:.9rem 0 .5rem">3. Practise the structure</div>\n'
            '        <p style="%s">Same grammar as the song, in sentences from your own week.</p>\n%s\n'
            '        <div style="font-size:.78rem;font-weight:600;margin:.9rem 0 .5rem">4. Did you get the message?</div>\n%s\n'
            '        <div style="font-size:.78rem;font-weight:600;margin:.9rem 0 .5rem">5. Say it out loud</div>\n%s\n'
            '      </div>'
            % (fill_in(s['ouca']),
               matching('match-gs%d' % i, s['vocab'], seed=3300 + i * 10),
               ITAL, fill_in(s['aplica']),
               quiz(s['quiz']),
               pronunciation([s['fala']])))

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
            '      <a href="%s" target="_blank" rel="noopener" style="%s;margin-left:1rem">Read the lyrics &#8599;</a>\n'
            '%s\n'
            '    </div>\n'
            '  </div>\n'
            '</div>' % (i, SVG_MUSIC, esc(s['gram']), esc(s['artista']), esc(s['titulo']),
                        esc(s['nota']), esc(s['tip']), s['vid'], LINK_STYLE,
                        s['lyr'], LINK_STYLE, blocos))

    return ('<!-- ========== TAB 5: GOSPEL (aditivo, 09/09/2026) ========== -->\n'
            '<div class="tab-content" id="tab-gospel">\n'
            '<h3 style="%s">Gospel Playlist</h3>\n'
            '<p style="%s">Twelve gospel songs in English. Each one was chosen for a structure you have already studied, and each comes with the lyrics, '
            'a listening exercise, the vocabulary of the song, practice in your own context, and a line to record. '
            'Mark each song as done after you work through it.</p>\n'
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
