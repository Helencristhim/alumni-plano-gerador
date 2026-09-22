#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Monta o card Pre-class da Aula 2 e grava preclass.html.

A Pre-class PREPARA a aula; nao e a aula. Ate 22/09/2026 ela era: as duas
superficies liam as mesmas constantes do lesson2_content.py, e 53 dos 69 itens
eram identicos em casa e na tela projetada. O professor Andre viu e disse: "pre
class e licao sao exatamente a mesma coisa".

Agora os stages de prova leem as constantes _PC, que sao itens proprios sobre o
MESMO lexico e o MESMO grammar_point (REGRA 1). O deck nao le nenhuma delas e
por isso nao muda.

USO (da raiz do repo):
    python3 _build/guilherme-henrique-caneli-aula2/build_preclass_cpe.py

Escreve _build/guilherme-henrique-caneli-aula2/preclass.html. Quem enfia no hub
e o patch_hub_l2.py (o insert_hub.py do modelo e ADITIVO: pula aula que ja
existe, e esta aula existe).
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import cpe_lib as L          # noqa: E402
import lesson2_content as C  # noqa: E402

A = 'guilherme-henrique-caneli'
AUDIO = '/audio/%s/' % A


def plan_at_a_glance():
    rows = [
        ("Vocabulary", "13 min", "The lexis of the capital stack: meanings that discriminate, a collocation bank, and a word-bank cloze with one item too many."),
        ("Reading", "14 min", "A case note on one financed project, read for understanding, with six comprehension questions."),
        ("Use of English", "18 min", "Word formation (Part 3) and key-word transformations (Part 4)."),
        ("Listening", "10 min", "One talk, heard twice, and six choices."),
        ("Grammar", "10 min", "Agency: four ways to name the party who acted, and two ways to lose them."),
        ("In the lesson", "&mdash;", "The exam papers themselves: gapped text, multiple choice, sentence completion, multiple matching, the long turn, the debates and the briefing note."),
    ]
    out = ['<div style="border:1px solid var(--border);border-radius:10px;overflow:hidden;margin:.2rem 0 1.4rem">']
    for i, (a, b, c) in enumerate(rows):
        bg = 'var(--bg-elevated)' if i % 2 == 0 else 'transparent'
        out.append('<div style="display:grid;grid-template-columns:minmax(96px,1fr) 64px 3fr;gap:.6rem;'
                   'padding:.6rem .8rem;background:%s;font-size:.82rem;align-items:baseline">'
                   '<span style="font-weight:700;color:var(--accent)">%s</span>'
                   '<span style="color:var(--text-dim)">%s</span><span>%s</span></div>' % (bg, a, b, c))
    out.append('</div>')
    return '\n'.join(out)


def s_lead_in():
    qs = [
        "A fund manager calls your project &ldquo;attractive but unbankable&rdquo;. What, precisely, has she said no to?",
        "Your government guarantees a project's revenue. Whose risk has disappeared, and whose has merely moved?",
        "A briefing note says you &ldquo;were advised&rdquo; to revise the tariff. Who advised you, and why does the sentence not say?",
    ]
    body = '<ul style="margin:0;padding-left:1.1rem;line-height:1.9;font-size:.92rem">%s</ul>' % ''.join(
        '<li>%s</li>' % q for q in qs)
    return L.section('Lead-in -- Before Any Vocabulary', 'Think', 'badge badge-think',
                     rubric=paper('Speaking &middot; 5 min') +
                     'Books closed. Answer aloud, in full sentences, before you read a single word below.',
                     body=body)


def paper(t):
    return L.paper_tag(t)


def s_vocab():
    return L.section('Stage 2.1 -- The Lexis of the Capital Stack', 'Vocabulary', 'badge badge-vocab',
                     rubric=paper('Vocabulary &middot; 5 min') +
                     'Tap Listen for each term. Say the meaning aloud in your own words <b>first</b>, then read '
                     'the definition and check whether you were more precise than it, or less.',
                     body=L.vocab_cards(C.VOCAB))


def s_matching():
    opts = [(o, o) for o in C.MATCH_OPTS]
    return L.section('Stage 2.2 -- Which One Is It, Exactly', 'Practice', 'badge badge-practice',
                     rubric=paper('Vocabulary &middot; Part 1 &middot; 4 min') +
                     'These are not the definitions from the cards above. Each one is a distinction, and the '
                     'distractors are close enough to be tempting. Every meaning is used exactly once.',
                     body=L.exam('l2-discriminate', 'Vocabulary', len(C.MATCH_ROWS),
                                 L.match_grid('match-l2-discriminate', C.MATCH_ROWS, opts),
                                 label='Which one is it, exactly'))


def s_collocation():
    opts = [(o, o) for o in C.COLLOC_OPTS]
    rows = [('<span style="font-size:.9rem">%s</span>' % q, a) for q, a in C.COLLOC_ROWS]
    body = (L.collocation_bank(C.COLLOC_BANK) +
            '<p style="font-size:.84rem;color:var(--text-dim);margin:1rem 0 .6rem;font-style:italic">'
            'Now the whole chunk, not the verb on its own. Only one of the six is idiomatic in each '
            'sentence; the others are what a very good non-native speaker says.</p>' +
            L.exam('l2-colloc', 'Vocabulary', len(C.COLLOC_ROWS),
                   L.match_grid('match-l2-colloc', rows, opts, left_style=' style="flex:2"'),
                   label='Collocation in a sentence'))
    return L.section('Stage 2.3 -- Words That Travel Together', 'Practice', 'badge badge-practice',
                     rubric=paper('Collocation &middot; 4 min') +
                     'Read the bank aloud once. Then complete each sentence with the whole expression, '
                     'not just the verb: a collocation is remembered as a block or it is not remembered.',
                     body=body)


def s_cloze():
    bank = ('<div style="font-size:.86rem;background:var(--bg-elevated);border:1px solid var(--border);'
            'border-radius:8px;padding:.7rem .9rem;margin-bottom:1rem"><b>Bank:</b> %s</div>'
            % ' &middot; '.join(C.CLOZE_BANK))
    body = bank + L.exam('l2-cloze', 'Vocabulary', len(C.CLOZE_ITEMS_PC),
                         L.typed_gaps(C.CLOZE_ITEMS_PC), label='Word-bank cloze') + L.reveal(
        'Which one was not needed?',
        'These eight sentences never need <b>%s</b>. It names what happens to a <i>price</i> when too '
        'much money chases too few assets, and not one of these sentences is about a price.'
        % C.CLOZE_NOT_NEEDED_PC)
    return L.section('Stage 2.4 -- Put the Lexis to Work', 'Practice', 'badge badge-practice',
                     rubric=paper('Word-bank cloze &middot; 5 min') +
                     'Complete each sentence with an expression from the bank. <b>Type it</b>, do not '
                     'choose it: the open cloze in the exam is typed, and recognising a term is easier '
                     'than producing it. One expression is <b>not needed</b>.',
                     body=body)


def s_reading():
    """Stage 2.5: leitura NOVA, para entender, nao para fazer prova.

    Pedido do professor (22/09/2026): "pode fazer outro reading com as mesmas
    palavras e fazer comprehension questions; so pra ler e entender e reforcar o
    vocabulario. Que seria juntar o 2.5 + 2.6."

    Entao o gapped text (Part 6) e o multiple choice (Part 5) saem daqui e ficam
    SO na aula, com o artigo da aula. Aqui entra um caso narrativo, os mesmos 14
    termos em contexto, e seis perguntas de compreensao.
    """
    paras = ''.join('<p style="margin-bottom:.9rem">%s</p>' % t for t in C.ARTICLE_PC)
    body = ('<div style="text-align:center;margin-bottom:1rem">'
            '<div style="font-family:\'Cormorant Garamond\',serif;font-size:1.5rem;font-weight:700">%s</div>'
            '<div style="font-size:.74rem;color:var(--text-dim);letter-spacing:.06em">%s</div></div>'
            % (C.ARTICLE_PC_TITLE, C.ARTICLE_PC_STANDFIRST) +
            '<div class="context-text" style="line-height:1.95;text-align:justify">%s</div>' % paras +
            L.exam('l2-reading-pc', 'Reading', len(C.COMPREHENSION_PC),
                   L.quiz(C.COMPREHENSION_PC), label='Comprehension') +
            L.reveal('Reveal answers &amp; where the text says it', C.COMPREHENSION_PC_KEY))
    return L.section('Stage 2.5 -- Read and Understand', 'Reading', 'badge badge-quiz',
                     rubric=paper('Reading for understanding &middot; 14 min') +
                     'Read it once straight through, without stopping at the terms you half know. Then read '
                     'it again and answer. Every expression from Stage 2.1 is in here doing a job: this is '
                     'where you find out what each one is <i>for</i>. The exam tasks on this lexis happen in '
                     'the lesson, not here.',
                     body=body)


def s_word_formation():
    return L.section('Stage 2.7 -- Word Formation', 'Use of English', 'badge badge-grammar',
                     rubric=paper('Paper 1 &middot; Part 3 &middot; 8 min') +
                     'Use the word in capitals to form a word that fits the gap. Watch for negative prefixes, '
                     'for part of speech, and for the internal change some of these words make.',
                     body=L.exam('l2-wordform', 'Use of English', len(C.WORD_FORMATION_PC),
                                 L.fill_items(C.WORD_FORMATION_PC), label='Paper 1, Part 3'))


def s_transformations():
    items = []
    for t in C.TRANSFORMATIONS_PC:
        lead = ('<div style="font-size:.88rem;margin-bottom:.35rem">%s</div>'
                '<div style="font-size:.74rem;letter-spacing:.1em;font-weight:800;color:var(--accent);'
                'margin-bottom:.3rem">%s</div>' % (t['lead'], t['key']))
        items.append(dict(before=lead + t['before'], after=t['after'], answer=t['answer'],
                          alt=t.get('alt'), hint=t['hint']))
    body = (L.exam('l2-transform', 'Use of English', len(C.TRANSFORMATIONS_PC),
                   L.fill_items(items), label='Paper 1, Part 4') +
            L.reveal('Reveal the answer key', C.TRANSFORM_PC_KEY))
    return L.section('Stage 2.8 -- Key-word Transformations', 'Use of English', 'badge badge-grammar',
                     rubric=paper('Paper 1 &middot; Part 4 &middot; 10 min') +
                     'Complete the second sentence so that it means the same as the first, using the word given. '
                     '<b>Do not change that word.</b> Use between three and eight words. Say your answer aloud '
                     'before you type it.',
                     body=body)


def s_listening():
    """Stage 2.9: UMA atividade, listen + choose.

    Pedido do professor (22/09/2026): "2.9 + 2.10 fazer so uma atividade listen
    + choose." Entao a sentence completion (Part 2) e o multiple matching de
    duas tarefas (Part 4) saem daqui e ficam so na aula, com os audios da aula.

    Audio proprio, voz propria: as cinco vozes dos falantes e a do talk da aula
    nao aparecem aqui, senao o aluno chega na aula tendo ouvido a mesma pessoa
    dizer as mesmas coisas.
    """
    body = (L.player('lp-l2-pc', AUDIO + C.LISTEN_PC_FILE,
                     'The head of infrastructure at a pension fund, on what she looks at before the '
                     'numbers. You hear it <b>twice</b>: play it a second time before you answer.') +
            L.exam('l2-listen-pc', 'Listening', len(C.LISTEN_CHOOSE_PC),
                   L.quiz(C.LISTEN_CHOOSE_PC), label='Listen and choose') +
            L.reveal('Reveal answers', C.LISTEN_CHOOSE_PC_KEY) +
            L.reveal('Show transcript (only after your second listening)',
                     '<span style="font-weight:400;line-height:1.8">%s</span>' % C.LISTEN_PC_TEXT))
    return L.section('Stage 2.9 -- Listen and Choose', 'Listening', 'badge badge-quiz',
                     rubric=paper('Listening for the argument &middot; 10 min') +
                     'One speaker, heard twice, and six questions. She is not describing a deal: she is '
                     'describing how she decides. Listen for the order of her reasoning, not for the '
                     'vocabulary, and do not open the transcript until you have listened twice.',
                     body=body)


def s_grammar():
    rows = ''.join(
        '<tr><td style="padding:.55rem .7rem;border-bottom:1px solid var(--border);font-weight:700;'
        'white-space:nowrap;font-size:.82rem">%s</td>'
        '<td style="padding:.55rem .7rem;border-bottom:1px solid var(--border);font-size:.84rem">%s</td>'
        '<td style="padding:.55rem .7rem;border-bottom:1px solid var(--border);font-size:.84rem">%s</td></tr>'
        % r for r in C.GRAMMAR_ROWS)
    table = ('<div style="overflow-x:auto"><table style="width:100%%;border-collapse:collapse;'
             'border:1px solid var(--border);border-radius:8px">'
             '<thead><tr style="background:var(--accent);color:#fff">'
             '<th style="padding:.5rem .7rem;text-align:left;font-size:.76rem;letter-spacing:.06em">FORM</th>'
             '<th style="padding:.5rem .7rem;text-align:left;font-size:.76rem;letter-spacing:.06em">WHAT IT DOES TO THE AGENT</th>'
             '<th style="padding:.5rem .7rem;text-align:left;font-size:.76rem;letter-spacing:.06em">EXAMPLE</th>'
             '</tr></thead><tbody>%s</tbody></table></div>' % rows)
    body = (table +
            '<p style="font-size:.84rem;color:var(--text-dim);margin:1.2rem 0 .6rem;font-style:italic">'
            'Five items on the difference the form makes. Every option is grammatical; only one is what the '
            'sentence means.</p>' +
            L.exam('l2-grammar-choice', 'Grammar', len(C.GRAMMAR_QUIZ),
                   L.quiz(C.GRAMMAR_QUIZ), label='What the form does') +
            '<p style="font-size:.84rem;color:var(--text-dim);margin:1.2rem 0 .6rem;font-style:italic">'
            'Now produce the structure, not a single word. Listen first if you want the rhythm of the whole '
            'sentence.</p>' +
            L.exam('l2-grammar-produce', 'Grammar', len(C.GRAMMAR_PRODUCTION),
                   L.fill_items(C.GRAMMAR_PRODUCTION), label='Produce the structure'))
    return L.section('Stage 2.11 -- Who Made It Happen', 'Grammar', 'badge badge-grammar',
                     rubric=paper('Grammar in focus &middot; 10 min') +
                     'Four structures you already produce. The question is no longer how to form them, but what '
                     'each one does to the party who acted: names them, hides them, or reports that something was '
                     'done <i>to</i> you.',
                     body=body)


# Os stages 2.12 (Delivery), 2.13 (Long Turn, Follow-up e Collaborative Task),
# 2.14 (Two Debates) e 2.15 (The Briefing Note) FORAM REMOVIDOS daqui em
# 22/09/2026, a pedido do professor. Eram prompt estatico previewando o que a
# aula ia fazer: falar e escrever acontecem na aula, com ele na frente. As
# constantes deles (LONG_TURN, COLLAB_TASK, DEBATE_*, WRITING_TASK, FOLLOW_UP)
# continuam no lesson2_content.py porque o DECK as usa, nos slides 50 a 56.
#
# O Survival Card continua: ele nao e stage nem exercicio, e o validate_lesson
# exige pelo menos um por aula.


def grade():
    """O painel de nota final. Os totais vem do CONTEUDO, nao de numero escrito a
    mao: se uma tarefa ganhar ou perder uma questao, o painel acompanha sozinho."""
    papers = [
        ('Vocabulary', len(C.MATCH_ROWS) + len(C.COLLOC_ROWS) + len(C.CLOZE_ITEMS_PC)),
        ('Reading', len(C.COMPREHENSION_PC)),
        ('Use of English', len(C.WORD_FORMATION_PC) + len(C.TRANSFORMATIONS_PC)),
        ('Listening', len(C.LISTEN_CHOOSE_PC)),
        ('Grammar', len(C.GRAMMAR_QUIZ) + len(C.GRAMMAR_PRODUCTION)),
    ]
    return L.grade_panel(
        papers,
        'This is preparation, not the exam. The exam papers themselves &mdash; the gapped text, the multiple '
        'choice, the sentence completion, the multiple matching, the speaking and the briefing note &mdash; '
        'happen in the lesson. This panel counts only what has a right answer, and it counts your '
        '<b>first</b> answer, which is the only one the exam counts.')


HEADER = '''<div class="lesson-card" data-gen="3" id="ex-lesson-2">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 02 -- Pre-class</div>
      <h3>The Language of Capital -- Who Made It Happen</h3>
      <div class="lesson-desc">A sovereign fund reads your term sheet. Every sentence either names the agent or hides it, and the fund notices. Preparation for the lesson: the lexis of the capital stack, a case note read for understanding, word formation and key-word transformations (Paper 1, Parts 3 and 4), and one talk to listen to. The exam papers themselves are done in the lesson. Key words: A risk-adjusted return, A leverage ratio, Subordinated debt, An equity stake, Blended finance, A de-risking mechanism, An off-take agreement, Credit enhancement, Concessional lending, Yield compression, Fiduciary duty, Capital deployment, A currency hedge, An anchor investor. Structure: causative have and get versus the passive in investment language.</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="2" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="2">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">
'''


def build():
    parts = [HEADER, plan_at_a_glance(), s_lead_in(), s_vocab(), s_matching(), s_collocation(), s_cloze(),
             s_reading(), s_word_formation(), s_transformations(), s_listening(), s_grammar(),
             grade(), L.survival_card(2, C.SPEECH_PHRASES), '  </div>\n</div>\n']
    return '\n'.join(parts)


def confere_totais(html):
    """O contador nao pode mentir: o data-total declarado tem de bater com o numero
    de questoes que existem DENTRO do bloco. Se alguem tirar uma questao e esquecer
    o total, o aluno ve "5 / 6" com 5 questoes na tela e acha que perdeu uma."""
    import re
    for m in re.finditer(r'<div class="cpe-exam" data-exam="([^"]+)" data-paper="[^"]+" data-total="(\d+)">', html):
        depth, i, corpo = 0, m.start(), ''
        for t in re.finditer(r'<div\b|</div\s*>', html[i:]):
            depth += 1 if t.group(0).startswith('<div') else -1
            if depth == 0:
                corpo = html[i:i + t.end()]
                break
        n = (len(re.findall(r'class="match-row"', corpo)) +
             len(re.findall(r'class="fill-blank-item"', corpo)) +
             len(re.findall(r'class="quiz-item"', corpo)))
        assert n == int(m.group(2)), ('bloco %s diz %s questoes e tem %d'
                                      % (m.group(1), m.group(2), n))
    # e o painel de nota tem de somar exatamente o mesmo
    blocos = sum(int(x) for x in re.findall(r'class="cpe-exam"[^>]*data-total="(\d+)"', html))
    painel = int(re.search(r'class="cpe-grade" id="cpe-grade-l2" data-total="(\d+)"', html).group(1))
    assert blocos == painel, 'painel de nota diz %d e as atividades somam %d' % (painel, blocos)
    return blocos


if __name__ == '__main__':
    out = os.path.join(HERE, 'preclass.html')
    html = build()
    print('nota: %d questoes valendo' % confere_totais(html))
    open(out, 'w', encoding='utf-8').write(html)
    print('preclass.html: %d KB' % (len(html) // 1024))
