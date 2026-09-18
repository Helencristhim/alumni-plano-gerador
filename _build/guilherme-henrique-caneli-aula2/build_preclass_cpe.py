#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Monta o card Pre-class da Aula 2 no formato de prova e grava preclass.html.

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
        ("Reading", "25 min", "Gapped text (Paper 1, Part 6) and multiple choice (Part 5) on one essay."),
        ("Use of English", "18 min", "Word formation (Part 3) and key-word transformations (Part 4)."),
        ("Listening", "24 min", "Sentence completion (Paper 3, Part 2) and multiple matching, two tasks at once (Part 4). Each heard twice."),
        ("Grammar", "10 min", "Agency: four ways to name the party who acted, and two ways to lose them."),
        ("Speaking &amp; Writing", "in class", "Long turn, collaborative task, and a briefing note of 280&ndash;320 words."),
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
                     body=L.match_grid('match-l2-discriminate', C.MATCH_ROWS, opts))


def s_collocation():
    opts = [(o, o) for o in C.COLLOC_OPTS]
    rows = [('<span style="font-size:.9rem">%s</span>' % q, a) for q, a in C.COLLOC_ROWS]
    body = (L.collocation_bank(C.COLLOC_BANK) +
            '<p style="font-size:.84rem;color:var(--text-dim);margin:1rem 0 .6rem;font-style:italic">'
            'Now the verb. Only one of the six is idiomatic in each sentence; the others are what a very good '
            'non-native speaker says.</p>' +
            L.match_grid('match-l2-colloc', rows, opts, left_style=' style="flex:2"'))
    return L.section('Stage 2.3 -- Words That Travel Together', 'Practice', 'badge badge-practice',
                     rubric=paper('Collocation &middot; 4 min') +
                     'Read the bank aloud once. Then choose the verb that belongs.',
                     body=body)


def s_cloze():
    bank = '<div style="font-size:.86rem;background:var(--bg-elevated);border:1px solid var(--border);'\
           'border-radius:8px;padding:.7rem .9rem;margin-bottom:1rem"><b>Bank:</b> %s</div>' % ' &middot; '.join(
               C.CLOZE_BANK)
    text, rows, n = [], [], 0
    for chunk, ans in C.CLOZE_TEXT:
        text.append(chunk)
        if ans:
            n += 1
            text.append(L.gap(n))
            rows.append(('<b>%d</b>' % n, ans))
    body = (bank +
            '<div class="context-text" style="line-height:2.1">%s</div>' % ''.join(text) +
            L.match_grid('match-l2-cloze', rows, [(o, o) for o in C.CLOZE_BANK],
                         left_style=' style="flex:0 0 2rem"'))
    return L.section('Stage 2.4 -- Put the Lexis to Work', 'Practice', 'badge badge-practice',
                     rubric=paper('Word-bank cloze &middot; 4 min') +
                     'Complete the passage using <b>only</b> the expressions in the bank. Each gap offers the '
                     'whole bank; one expression is <b>not needed</b>. Meaning decides, and so does the grammar '
                     'of the sentence around the gap.',
                     body=body)


def s_reading_gapped():
    paras = []
    for before, n, after in C.ARTICLE:
        if n:
            paras.append('<p style="margin-bottom:.9rem">%s%s%s</p>' % (before, L.gap(n), after))
        else:
            paras.append('<p style="margin-bottom:.9rem">%s</p>' % before)
    opts = '<div style="margin:1.2rem 0 .8rem">%s</div>' % ''.join(
        '<div style="display:flex;gap:.6rem;padding:.5rem .7rem;border:1px solid var(--border);'
        'border-radius:8px;margin-bottom:.4rem;font-size:.88rem;line-height:1.55">'
        '<b style="color:var(--accent);flex:0 0 1rem">%s</b><span>%s</span></div>' % (k, v)
        for k, v in C.GAP_OPTIONS)
    body = ('<div style="text-align:center;margin-bottom:1rem">'
            '<div style="font-family:\'Cormorant Garamond\',serif;font-size:1.5rem;font-weight:700">%s</div>'
            '<div style="font-size:.74rem;color:var(--text-dim);letter-spacing:.06em">%s</div></div>'
            % (C.ARTICLE_TITLE, C.ARTICLE_STANDFIRST) +
            '<div class="context-text" style="line-height:1.95;text-align:justify">%s</div>' % ''.join(paras) +
            '<p style="font-size:.84rem;font-weight:700;margin:1.2rem 0 .2rem">Choose from these sentences '
            '(one is not used):</p>' + opts +
            L.match_grid('match-l2-gapped', [('<b>Gap %s</b>' % k, v) for k, v in C.GAP_ANSWERS],
                         [(k, '%s -- %s' % (k, v[:58] + '...')) for k, v in C.GAP_OPTIONS],
                         left_style=' style="flex:0 0 4rem"') +
            L.reveal('Reveal &amp; explain -- why each sentence fits only where it fits', C.GAP_KEY))
    return L.section('Stage 2.5 -- Gapped Text', 'Reading', 'badge badge-quiz',
                     rubric=paper('Paper 1 &middot; Part 6 &middot; 14 min') +
                     'Six sentences have been removed from the article. Choose from <b>A&ndash;G</b> the one that '
                     'fits each gap. There is <b>one extra</b> sentence you will not need. Read the whole '
                     'paragraph before you commit: what gives a gap away is reference, cohesion and the line of '
                     'the argument, never a single repeated word.',
                     body=body)


def s_reading_mcq():
    body = L.quiz(C.MCQ) + L.reveal('Reveal answers &amp; reasoning', C.MCQ_KEY)
    return L.section('Stage 2.6 -- Multiple Choice', 'Reading', 'badge badge-quiz',
                     rubric=paper('Paper 1 &middot; Part 5 &middot; 11 min') +
                     'Now the text is whole, answer on it. Choose the option the writer\'s argument actually '
                     'supports, not the one that repeats a word from the passage. At least one option in every '
                     'item is <b>true and still wrong</b>.',
                     body=body)


def s_word_formation():
    return L.section('Stage 2.7 -- Word Formation', 'Use of English', 'badge badge-grammar',
                     rubric=paper('Paper 1 &middot; Part 3 &middot; 8 min') +
                     'Use the word in capitals to form a word that fits the gap. Watch for negative prefixes, '
                     'for part of speech, and for the internal change some of these words make.',
                     body=L.fill_items(C.WORD_FORMATION))


def s_transformations():
    items = []
    for t in C.TRANSFORMATIONS:
        lead = ('<div style="font-size:.88rem;margin-bottom:.35rem">%s</div>'
                '<div style="font-size:.74rem;letter-spacing:.1em;font-weight:800;color:var(--accent);'
                'margin-bottom:.3rem">%s</div>' % (t['lead'], t['key']))
        items.append(dict(before=lead + t['before'], after=t['after'], answer=t['answer'],
                          alt=t.get('alt'), hint=t['hint']))
    body = L.fill_items(items) + L.reveal('Reveal the answer key', C.TRANSFORM_KEY)
    return L.section('Stage 2.8 -- Key-word Transformations', 'Use of English', 'badge badge-grammar',
                     rubric=paper('Paper 1 &middot; Part 4 &middot; 10 min') +
                     'Complete the second sentence so that it means the same as the first, using the word given. '
                     '<b>Do not change that word.</b> Use between three and eight words. Say your answer aloud '
                     'before you type it.',
                     body=body)


def s_listening_completion():
    body = (L.player('lp-l2-talk', AUDIO + C.TALK_FILE,
                     'An infrastructure investment director, speaking at an investor evening. '
                     'In the exam you hear it <b>twice</b> -- press play a second time before you check.') +
            L.fill_items(C.TALK_ITEMS) +
            L.reveal('Show transcript (only after your second listening)',
                     '<span style="font-weight:400;line-height:1.8">%s</span>' % C.TALK_TEXT))
    return L.section('Stage 2.9 -- Sentence Completion', 'Listening', 'badge badge-quiz',
                     rubric=paper('Paper 3 &middot; Part 2 &middot; 12 min') +
                     'Complete each sentence with a word or short phrase. The words you need are said, so write '
                     'what you hear and not what you would have written. Do not open the transcript until you '
                     'have listened twice.',
                     body=body)


def s_listening_matching():
    players = []
    for s in C.SPEAKERS:
        players.append(L.player('lp-l2-mm%d' % s['n'], AUDIO + s['file'], '<b>Speaker %d</b>' % s['n']))
    t1 = L.match_grid('match-l2-mm1',
                      [('<b>Speaker %d</b>' % s['n'], s['task1']) for s in C.SPEAKERS],
                      [(k, '%s -- %s' % (k, v)) for k, v in C.TASK1_OPTS],
                      left_style=' style="flex:0 0 6rem"')
    t2 = L.match_grid('match-l2-mm2',
                      [('<b>Speaker %d</b>' % s['n'], s['task2']) for s in C.SPEAKERS],
                      [(k, '%s -- %s' % (k, v)) for k, v in C.TASK2_OPTS],
                      left_style=' style="flex:0 0 6rem"')
    def optlist(title, opts):
        return ('<p style="font-size:.84rem;font-weight:700;margin:1.1rem 0 .3rem">%s</p>'
                '<div style="font-size:.85rem;line-height:1.7;margin-bottom:.6rem">%s</div>' % (
                    title, ''.join('<div><b style="color:var(--accent)">%s</b> &nbsp;%s</div>' % (k, v)
                                   for k, v in opts)))
    transcripts = ''.join(
        '<p style="margin-bottom:.7rem"><b>Speaker %d:</b> %s</p>' % (s['n'], s['text']) for s in C.SPEAKERS)
    body = (''.join(players) +
            optlist('Task One -- what each speaker is (A&ndash;H, three are not used)', C.TASK1_OPTS) + t1 +
            optlist('Task Two -- the main point each one makes (A&ndash;H, three are not used)', C.TASK2_OPTS) + t2 +
            L.reveal('Show transcripts', '<span style="font-weight:400;line-height:1.75">%s</span>' % transcripts))
    return L.section('Stage 2.10 -- Multiple Matching: Two Tasks at Once', 'Listening', 'badge badge-quiz',
                     rubric=paper('Paper 3 &middot; Part 4 &middot; 12 min') +
                     'You will hear five short extracts. <b>Two tasks run at the same time</b>: what each speaker '
                     '<i>is</i>, and the main point each one <i>makes</i>. Listen to all five once for Task One, '
                     'then all five again for Task Two. Three options in each list are not used.',
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
            'sentence means.</p>' + L.quiz(C.GRAMMAR_QUIZ) +
            '<p style="font-size:.84rem;color:var(--text-dim);margin:1.2rem 0 .6rem;font-style:italic">'
            'Now produce the structure, not a single word. Listen first if you want the rhythm of the whole '
            'sentence.</p>' + L.fill_items(C.GRAMMAR_PRODUCTION))
    return L.section('Stage 2.11 -- Who Made It Happen', 'Grammar', 'badge badge-grammar',
                     rubric=paper('Grammar in focus &middot; 10 min') +
                     'Four structures you already produce. The question is no longer how to form them, but what '
                     'each one does to the party who acted: names them, hides them, or reports that something was '
                     'done <i>to</i> you.',
                     body=body)


def s_delivery():
    return L.section('Stage 2.12 -- Delivery', 'Speaking', 'badge badge-speak',
                     rubric=paper('Pronunciation &amp; stress &middot; 6 min') +
                     'Record each one. What is being judged here is not the sounds but where the stress lands: '
                     'these sentences are built so that the word that matters arrives last.',
                     body=L.speech_cards(C.SPEECH_PHRASES))


def s_speaking():
    body = (L.think_card(C.LONG_TURN, 'think-result-l2') +
            '<div style="height:.8rem"></div>' +
            L.think_card(C.COLLAB_TASK, 'think-result-l2b'))
    return L.section('Stage 2.13 -- Long Turn and Collaborative Task', 'Speaking', 'badge badge-speak',
                     rubric=paper('Paper 5 &middot; Parts 2&ndash;3 &middot; in class') +
                     'Record the long turn before the lesson so that you hear yourself once before anyone else '
                     'does. The collaborative task is for the lesson itself.',
                     body=body)


def s_writing():
    # NAO usa .think-card aqui: updateProgress conta todo .think-card como uma
    # unidade que so fecha com gravacao. Sem microfone nesta tarefa, o card
    # ficaria eternamente pendente e a aula nunca chegaria a 100%.
    body = ('<div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;'
            'padding:1rem 1.1rem;font-size:.92rem;line-height:1.7">%s</div>' % C.WRITING_TASK +
            L.reveal('What a strong answer does (open only after you have written yours)', C.WRITING_MODEL))
    return L.section('Stage 2.14 -- The Briefing Note', 'Writing', 'badge badge-think',
                     rubric=paper('Paper 2 &middot; Part 2 &middot; after class') +
                     'Bring it to the next lesson. It will be read for the argument first and the language '
                     'second, which is the order the fund reads in too.',
                     body=body)


HEADER = '''<div class="lesson-card" data-gen="3" id="ex-lesson-2">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 02 -- Pre-class</div>
      <h3>The Language of Capital -- Who Made It Happen</h3>
      <div class="lesson-desc">A sovereign fund reads your term sheet. Every sentence either names the agent or hides it, and the fund notices. Exam-format tasks throughout: gapped text and multiple choice (Paper 1, Parts 6 and 5), word formation and key-word transformations (Parts 3 and 4), sentence completion and multiple matching (Paper 3, Parts 2 and 4). Key words: A risk-adjusted return, A leverage ratio, Subordinated debt, An equity stake, Blended finance, A de-risking mechanism, An off-take agreement, Credit enhancement, Concessional lending, Yield compression, Fiduciary duty, Capital deployment, A currency hedge, An anchor investor. Structure: causative have and get versus the passive in investment language.</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="2" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="2">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">
'''


def build():
    parts = [HEADER, plan_at_a_glance(), s_lead_in(), s_vocab(), s_matching(), s_collocation(), s_cloze(),
             s_reading_gapped(), s_reading_mcq(), s_word_formation(), s_transformations(),
             s_listening_completion(), s_listening_matching(), s_grammar(), s_delivery(), s_speaking(),
             s_writing(), '  </div>\n</div>\n']
    return '\n'.join(parts)


if __name__ == '__main__':
    out = os.path.join(HERE, 'preclass.html')
    html = build()
    open(out, 'w', encoding='utf-8').write(html)
    print('preclass.html: %d KB' % (len(html) // 1024))
