# -*- coding: utf-8 -*-
"""As notas do Teacher's Guide, uma por tela.

A aula 1 usa as notas da REGUA, palavra por palavra: sao a referencia de forma e de tom.
As aulas 2 a 6 saem da mesma rubrica -- a mesma etapa, o mesmo procedimento, os mesmos
minutos -- com o CONTEUDO citado da propria aula (a linha 3, o segundo movimento de reparo,
o que ela tem de dizer). Assim a nota nao pode divergir do que esta na tela: ela e feita do
mesmo material.

Onde a aula pede algo que a rubrica nao prevê (a confidencialidade dos numeros na aula 5,
o 'nada de conteudo novo' na aula 6), a aula declara o acrescimo em 'notas'.
"""
import json, os

AQUI = os.path.dirname(os.path.abspath(__file__))
_REGUA = {x['s']: x['teacher'] for x in
          json.load(open(os.path.join(AQUI, 'notas_aula1_regua.json'), encoding='utf-8'))}

MINUTOS = [2, 3, 5, 5, 3, 6, 3, 5, 5, 9, 7, 2]

TITULOS = ['Opening', 'What this lesson has to do', 'What makes this hard', 'First version',
           'One way it can sound', 'Five lines', 'When something goes wrong', 'Change one thing',
           'Essential message, then details', 'The real thing', 'What just happened, and once more', 'Close']

def _b(t):
    return '<strong>%s</strong>' % t

def monta(a, i):
    """Nota da tela i (1..12) da aula a."""
    if a['n'] == 1:
        return _REGUA[i]
    n, tema = a['n'], a['tema']
    l1 = a['linhas'][0][0]
    l3 = a['linhas'][2][0]
    ap2 = a['apoio'][1][0]
    partes = ['%s (%d min)' % (_b('%s' % TITULOS[i - 1]), MINUTOS[i - 1])]
    extra = (a.get('notas') or {}).get(i, '')

    if i == 1:
        partes += [_b('Goal:') + ' To name what this lesson produces &mdash; %s &mdash; and to connect it to what she built last time.' % a['desc'].lower(),
                   _b('Run it:') + ' Read the subtitle aloud and ask her to say, in one sentence, what she took from the last lesson. Two or three exchanges.',
                   _b('Check:') + ' Can she say in her own words what today produces?',
                   _b('If needed:') + ' If she starts on the whole presentation, say that today is this block only.',
                   _b('Move on when:') + ' The scope is clear to her.']
    elif i == 2:
        partes += [_b('Goal:') + ' To fix the interlocutor, the moment, the outcome and the support before any language is taught.',
                   _b('Run it:') + ' Go through the lines of the brief. Stop on <em>With you</em> and say it plainly: the slide and the speech map stay in front of her, today and on the day.',
                   _b('Check:') + ' Ask her to name what the block has to do. The list is on the next screens; she does not need it from memory.',
                   _b('If needed:') + ' If she asks for a figure the deck does not give, do not supply one &mdash; and show her that not having it is itself something she can say.',
                   _b('Move on when:') + ' She can state what a successful version looks like.']
    elif i == 3:
        partes += [_b('Goal:') + ' To name the four risks before they happen, so the toolkit in stage 4 answers something she has already recognized.',
                   _b('Run it:') + ' Read the four rows. Then ask which one worries her most, and let her choose one.',
                   _b('Check:') + ' Her choice is diagnostic &mdash; write it down, with the reason she gives.',
                   _b('If needed:') + ' If she says all four, ask which one has actually happened to her.',
                   _b('Move on when:') + ' She has chosen one and said why. Do not give the repair language here: naming the risk is this stage, the language is stage 4.']
    elif i == 4:
        partes += [_b('Goal:') + ' To obtain an unmodelled sample of this block, which is the diagnostic instrument of the lesson.',
                   _b('Run it:') + ' Set the scene in one sentence, then stop talking. Do not correct, do not prompt, do not finish her sentences. Write down what she says, in her own words &mdash; you will use it in stage 7.',
                   _b('Check:') + ' What arrives on its own, and what does not appear at all. If she pauses after an unknown word, observe how she recovers.',
                   _b('If needed:') + ' If she stops completely, wait a few seconds before helping. The recovery is the evidence.',
                   _b('Move on when:') + ' She has produced something, however short. Do not ask for a second attempt here.']
    elif i == 5:
        partes += [_b('Goal:') + ' To let her compare her own version with a plain model, and to find the functions rather than the words.',
                   _b('Run it:') + ' Let her read it silently first. Then ask the question at the bottom.',
                   _b('Check:') + ' Can she name at least one difference between the model and her version? If she names vocabulary only, ask what the model DOES that hers did not.',
                   _b('If needed:') + ' If she says the model is too simple, agree &mdash; simple is what survives at speed.',
                   _b('Optional:') + ' If she did the pre-class, say that this is the same language she met there; it is meant to come back.',
                   _b('Move on when:') + ' She has named at least one difference.']
    elif i == 6:
        partes += [_b('Goal:') + ' To install five reusable chunks, one per communicative function of this block.',
                   _b('Run it:') + ' Say each line once at natural speed, then once slowly. She repeats. Then change one element and have her say it again &mdash; identical repetition does not count as practice.',
                   _b('Check:') + ' Can she locate and produce each line with the speech map available? If <em>%s</em> breaks, split it and rebuild it.' % l3,
                   _b('If needed:') + ' Treat a long line as one block, not as grammar to explain. The grammar is not the lesson.',
                   _b('Move on when:') + ' She can produce lines 1, 2 and 5 on request, with or without consulting the map.']
    elif i == 7:
        partes += [_b('Goal:') + ' To give her four short moves that keep the interaction alive when the language or the data fails.',
                   _b('Run it:') + ' One line each, said out loud. Then interrupt her with a fast question and have her use one of them.',
                   _b('Check:') + ' Two of the four used under interruption, without an apology in front of them. The last move protects the facts: a company figure that is not confirmed is never completed or invented &mdash; not by her, and not by you.',
                   _b('If needed:') + ' If only one move is retained, prioritize <em>%s</em>, which redirects what is outside her responsibility.' % ap2,
                   _b('Move on when:') + ' She has used two of them under interruption.']
    elif i == 8:
        partes += [_b('Goal:') + ' To make the lines flexible rather than memorized, by changing one element at a time.',
                   _b('Run it:') + ' Four changes, no more. You name the change, she says the line. Keep the pace fast &mdash; this is drilling, not discussion.',
                   _b('Check:') + ' Does the message remain clear when one element changes?',
                   _b('If needed:') + ' If she is losing the thread, drop to two changes and drill those to fluency instead.',
                   _b('Move on when:') + ' She can use the right line after each prompt. Every repetition must change something.']
    elif i == 9:
        partes += [_b('Goal:') + ' To build the block by content, adding functions one at a time rather than filling a duration.',
                   _b('Run it:') + ' First pass with the essential part. Then add the two details. The map stays visible in both passes &mdash; and in the retask too: consulting it is an authorized strategy, not a failure.',
                   _b('Check:') + ' Does the second pass add what is missing without losing what she already had?',
                   _b('If needed:') + ' If the expanded version breaks down, go back to the essential part and add only one thing.',
                   _b('Move on when:') + ' She has completed one pass with everything, however imperfect.']
    elif i == 10:
        partes += [_b('Goal:') + ' To run the main production of the lesson under the real conditions of the visit, without interruption.',
                   _b('Run it:') + ' Play the visitor. Greet her, then let her speak. Do not correct during the production. When she finishes, ask the questions on the screen.',
                   _b('Check:') + ' What arrived, and what happened at the first hesitation. Note her exact words &mdash; stage 7 is built from what you actually hear.',
                   _b('If needed:') + ' Intervene only on complete communication breakdown, or on a factual error about the company. An error that does not block communication is noted, not interrupted.',
                   _b('Move on when:') + ' She has produced once and answered at least two questions.']
    elif i == 11:
        partes += [_b('Goal:') + ' To return one thing that worked and one thing that would change the message, and to have her say the corrected stretch straight after building it.',
                   _b('Run it:') + ' Type into the board in front of her, choosing the point from the production you actually heard. Then go to the block at the bottom and have her say only that stretch. The clearer version stays on the screen while she says it.',
                   _b('Check:') + ' The two top fields are the same data she sees in her Feedback tab &mdash; what you write there reaches her, and nothing else on this screen does. In the retask, does the change hold?',
                   _b('If needed:') + ' If nothing needs changing, say so and go straight to the closing. An invented correction is worse than none.',
                   _b('Move on when:') + ' The corrected stretch has been said once more.']
    else:
        partes += [_b('Goal:') + ' To confirm what was worked on today and to name the continuity into the next lesson.',
                   _b('Run it:') + ' Read the blocks. Then close the lesson with <em>Finish lesson</em> in the bar below.',
                   _b('Check:') + ' Nothing. This screen registers, it does not test &mdash; a partial lesson is still a lesson, and the closing has to be true in that case too.',
                   _b('If needed:') + ' If something did not appear today, say which part carries into the next lesson instead of marking it missing.',
                   _b('Move on when:') + ' The lesson is closed.']
    if extra:
        partes.append(_b('For this lesson:') + ' ' + extra)
    return '<br><br>'.join(partes)
