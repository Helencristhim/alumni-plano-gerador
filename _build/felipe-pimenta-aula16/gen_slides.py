# -*- coding: utf-8 -*-
"""Gera slides.html da AULA 16 do Felipe Pimenta -- a ULTIMA do contrato (16/16).

Aula PAR => modelo de LEITURA (ic-reading + gist + true/false), REGRA 29 item 2.
Encerramento do PROGRAMA: mede a distancia contra o baseline gravado na aula 1.
Lingua nova (recorte pequeno e legitimo p/ um milestone): FUTURE PERFECT e FUTURE
PERFECT CONTINUOUS -- olhar para tras a partir de um ponto no futuro, o espelho
exato do present perfect que abriu o programa na aula 1.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, '_build', 'felipe-pimenta-common'))
import felipe_lib as L  # noqa: E402

S = []
add = S.append

# ============================================================ CHAPTER 1 -- The Baseline
add(L.s_title(
    1, 1,
    '<strong>Abertura (2 min):</strong> Compartilhe a tela. Diga: '
    '&#39;Sixteen lessons ago a head-hunter called you and you had to take it in English '
    'for the first time. Tonight you take that call again.&#39; NAO cumprimente de forma '
    'scriptada (REGRA 27A). Avise que esta e a ULTIMA aula do pacote &mdash; e que ela nao '
    'ensina uma habilidade nova, ela MEDE.',
    'Lesson 16 &middot; Milestone Review',
    'From Aqua Capital Silence to', 'CFO Fluency',
    'You have not come to learn a new skill tonight. You have come to find out how far the old one travelled.'))

add(L.s_hook(
    2, 1,
    '<strong>Warm-up + callback (5 min):</strong> Retome a aula 15 ANTES do tema de hoje '
    '(REGRA 20). Pergunte, em registro social e rapido: &#39;You are at that dinner again. '
    'Ask me two things about my weekend &mdash; one with a tag.&#39; Espere as tags '
    '(isn&#39;t it / are you) e uma resposta curta (So am I / Neither do I). Depois vire a '
    'chave: &#39;Now we go back to the very first evening.&#39; Nao adiante nada: o slide 3 '
    'faz o trabalho sozinho.',
    'Chapter 1: The Baseline',
    'Sixteen Lessons Ago You Recorded', 'Three Minutes',
    'You have never listened to that file. Tonight you find out what it was actually measuring.'))

# ---- SLIDE 3: as frases LITERAIS do survival card da aula 1 -------------------
L1_PHRASES = [
    'In my current role, I oversee the finance team at a fintech.',
    'I&#39;ve been a CFO for three years.',
    'Before that, I spent two years in private equity.',
    'My background is in corporate finance and controlling.',
    'I&#39;m responsible for the budget, the forecast and investor reporting.',
]
_cards = ''.join(
    '<div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;'
    f'padding:.9rem 1rem;font-size:.92rem">{p}</div>' for p in L1_PHRASES)
add(L._slide(
    3, 1, 'slide-light',
    '<strong>O momento da aula (6 min):</strong> Estas sao, PALAVRA POR PALAVRA, as cinco '
    'frases do survival card da AULA 1. Leia o titulo e diga apenas: &#39;Same five ideas. '
    'Say them again &mdash; the way you say them today.&#39; E ENTAO FIQUE EM SILENCIO. Nao '
    'ajude, nao sugira, nao complete. O que voce quer medir e se ele SOBE de registro '
    'sozinho: se aparece hedging, um cleft, um numero, uma frase mais longa sem pedir '
    'licenca. Anote as cinco versoes novas &mdash; elas voltam no role-play final. Se ele '
    'repetir identico, tudo bem: isso tambem e dado.',
    '  <div class="slide-inner">\n'
    '    <div class="chapter-label">Lesson 1, Word for Word</div>\n'
    '    <h2 class="slide-heading">This Is What You Said <span class="accent">Then</span></h2>\n'
    '    <p style="text-align:center;font-size:.85rem;color:var(--text-dim);margin-top:.4rem">'
    'Same five ideas. Say them again, the way you say them today.</p>\n'
    '    <div style="display:flex;flex-direction:column;gap:.6rem;max-width:600px;margin:1.2rem auto 0">'
    f'{_cards}</div>\n  </div>'))

# ---- SLIDE 4: o programa inteiro em blocos -----------------------------------
BLOCKS = [
    ('01 &ndash; 03', 'The Starting Point',
     'who you are, what went wrong, and owning it out loud'),
    ('04 &ndash; 07', 'The Hard Conversations',
     'regret, hypotheticals, bad news, and standing your ground'),
    ('08 &ndash; 11', 'The Room',
     'delegating, negotiating, reporting numbers, signposting a talk'),
    ('12 &ndash; 14', 'The Boardroom',
     'disagreeing with power, reading a trend, answering a panel'),
    ('15 &ndash; 16', 'Beyond the Desk',
     'the dinner after the interview &mdash; and the measurement'),
]
_bl = ''.join(
    '<div style="background:var(--accent-dim);border:1px solid var(--accent);border-radius:10px;'
    f'padding:.9rem;text-align:center"><p style="font-size:.72rem;color:var(--text-dim);'
    f'letter-spacing:.5px">{a}</p><p style="font-weight:700;font-size:.9rem">{b}</p>'
    f'<p style="font-size:.78rem;color:var(--text-dim)">{c}</p></div>' for a, b, c in BLOCKS)
add(L._slide(
    4, 1, 'slide-light',
    '<strong>Mapa do programa (4 min):</strong> Percorra os cinco blocos e, em CADA um, '
    'pergunte: &#39;Which of these do you actually use in a normal week?&#39; O objetivo nao '
    'e nostalgia, e inventario: ele precisa ver que nao aprendeu dezesseis assuntos, '
    'aprendeu cinco movimentos. Anote quais blocos ele nao citar &mdash; sao os que entram '
    'na conversa de manutencao no fim da aula.',
    '  <div class="slide-inner">\n'
    '    <div class="chapter-label">The Whole Program</div>\n'
    '    <h2 class="slide-heading">Sixteen Lessons, <span class="accent">Five Moves</span></h2>\n'
    '    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));'
    f'gap:.8rem;max-width:760px;margin:1.5rem auto 0">{_bl}</div>\n'
    '    <p style="text-align:center;font-size:.88rem;color:var(--text-dim);margin-top:1.2rem;'
    'max-width:560px;margin-left:auto;margin-right:auto">You did not learn sixteen subjects. '
    'You learned five moves, and tonight you choose between them without being told which one.</p>\n'
    '  </div>'))

add(L.s_cards3(
    5, 1,
    '<strong>Objetivo (2 min):</strong> Diga: &#39;Three things tonight: the words for '
    'distance, one last structure, and the same three minutes you recorded on day one.&#39; '
    'Antecipe o final: o role-play livre e o cenario IDENTICO da aula 1, e voce vai tocar as '
    'duas gravacoes lado a lado.',
    'Tonight&#39;s Goal', 'Three', 'Missions',
    [('1. The Words',
      'baseline, benchmark, muscle memory, off the cuff, blind spot, to come a long way...'),
     ('2. The Code',
      'future perfect &mdash; standing at a deadline and looking back at what is already done'),
     ('3. The Same Three Minutes',
      'the screening call from Lesson 1, run again, on the same clock')],
    'Everything else tonight you already own. The only new thing is how you talk about what comes next.'))

# ============================================================ CHAPTER 2 -- vocab
add(L.s_chapter(
    6, 2,
    '<strong>Transicao vocab (1 min):</strong> Diga: &#39;Twelve words for something you have '
    'never had to describe in English: your own progress.&#39; Passe ao proximo.',
    'Chapter 2: The Language of Distance',
    'Words for How Far You', 'Have Come', '', L.IMG['vocab']))

VOCAB = [
    ('A baseline', 'the first measurement, the one that everything later is compared with', '',
     'We recorded a baseline on the first evening and nobody has listened to it since.'),
    ('A benchmark', 'a standard from outside that you measure yourself against', '',
     'The benchmark is not a native speaker; it is the man who answered that first call.'),
    ('To take stock', 'to stop and look honestly at where you are', '',
     'Before the next move, take stock of what has actually changed.'),
    ('Second nature', 'so familiar to you that it happens without any thinking', '',
     'Opening a meeting in English is second nature to him now.'),
    ('Muscle memory', 'a skill that the body repeats on its own after enough practice', '',
     'Fluency is mostly muscle memory; the phrases arrive before you choose them.'),
    ('Off the cuff', 'with no preparation and with no notes in front of you', '',
     'She asked something nobody expected and he answered off the cuff.'),
    ('To hold your own', 'to perform as well as everyone else in a demanding room', '',
     'I hold my own in a meeting; a crowded call on a bad line is still work.'),
    ('A stepping stone', 'something that carries you to the next stage of a journey', '',
     'That first screening call was a stepping stone, not the destination.'),
    ('Incremental', 'growing in small steps rather than in one visible jump', '',
     'The gain was incremental, which is why he could not feel it week by week.'),
    ('To fall back on', 'to use as support at the moment when everything else fails', '',
     'When the line breaks, he falls back on three phrases that always work.'),
    ('A blind spot', 'a weakness in yourself that you are not able to see', '',
     'Everybody has a blind spot; his was asking for a question to be repeated.'),
    ('To come a long way', 'to have made great progress from where you started', '',
     'You have come a long way from the man who sat silent at Aqua Capital.'),
]

add(L.s_vocab(
    7, 2,
    '<strong>Vocab 1 (5 min):</strong> Clique em cada card e leia a definicao ANTES de revelar '
    'a palavra. Estes seis sao de MEDIDA: baseline, benchmark, take stock, second nature, '
    'muscle memory, off the cuff. CCQ para <em>benchmark</em>: &#39;Is a benchmark something '
    'you set, or something you compare yourself to?&#39; (compare). CCQ para <em>second '
    'nature</em>: &#39;If it is second nature, do you have to think about it?&#39; (no). Clique '
    'de novo fecha o card (REGRA 27E).',
    'of Measurement', VOCAB[:6], '1', 0))

add(L.s_vocab(
    8, 2,
    '<strong>Vocab 2 (5 min):</strong> Estes seis sao de TRAJETORIA e de LIMITE: hold your own, '
    'stepping stone, incremental, fall back on, blind spot, come a long way. CCQ para '
    '<em>blind spot</em>: &#39;Can you see your own blind spot?&#39; (no &mdash; somebody has '
    'to tell you). Pergunte, sem dar a resposta: &#39;What is yours?&#39; A resposta dele volta '
    'no listening 2.',
    'of the Journey', VOCAB[6:], '2', 6))

add(L.s_pron(
    9, 2,
    '<strong>Pronuncia (4 min):</strong> Tres armadilhas aqui. <em>Baseline</em> tem o acento na '
    'PRIMEIRA silaba (BASE-line). <em>Incremental</em> tem o acento em MEN (in-cre-MEN-tal) e '
    'o <em>i</em> inicial e curto. <em>Off the cuff</em> sai em UM bloco, sem pausa entre as '
    'tres palavras. Peca tres repeticoes de cada e nao aceite a versao lenta.',
    ['Baseline', 'Benchmark', 'Incremental', 'Muscle memory', 'Off the cuff', 'A blind spot']))

add(L.s_fill(
    10, 2,
    '<strong>Em contexto (4 min):</strong> Leia cada frase em voz alta com a lacuna aberta e '
    'peca que o Felipe complete ANTES de clicar. Clique so para conferir. Se ele acertar os '
    'seis de primeira, acelere &mdash; o peso da aula esta no fim, nao aqui.',
    'In Context', 'Fill the', 'Gap',
    'Say the missing word out loud, then click to check',
    [('We recorded a ', 'baseline', ' on the first evening, and nobody has listened to it since.'),
     ('Opening a meeting in English is ', 'second nature', ' to him now.'),
     ('She asked a question nobody expected and he answered ', 'off the cuff', '.'),
     ('The gain was ', 'incremental', ', which is why he could not feel it week by week.'),
     ('Everybody has a ', 'blind spot', '; his was asking for a question to be repeated.'),
     ('You have ', 'come a long way', ' from the man who sat silent in those meetings.')]))

# ============================================================ CHAPTER 3 -- reading
add(L.s_chapter(
    11, 3,
    '<strong>Transicao leitura (1 min):</strong> Diga: &#39;A case study. A finance director who '
    'recorded himself on day one and could not finish the file at the end.&#39; NAO resuma o '
    'texto &mdash; o slide de tarefa vem antes e ja diz o que procurar.',
    'Chapter 3: One Year On',
    'The Recording He Never Played', 'Back', '', L.IMG['context']))

add(L.s_blocks(
    12, 3,
    '<strong>Leitura (8 min):</strong> Leitura silenciosa primeiro, 3 min, com as afirmacoes do '
    'True/False ja na cabeca dele (o slide anterior). Depois peca que ele leia o TERCEIRO '
    'paragrafo em voz alta &mdash; e o que descreve a re-gravacao, e ouvir a propria voz dizendo '
    'isso muda a temperatura da aula. So entao clique na ideia principal.',
    'Read for the Main Idea', 'Two Recordings,', 'One Man', ['reading', 'gist'],
    'Read once for the whole shape, then choose the summary that survives the fourth paragraph'))

add(L.s_blocks(
    13, 3,
    '<strong>True or False (5 min):</strong> Uma afirmacao por vez. ANTES de revelar, exija a '
    'justificativa em voz alta: &#39;Where in the text?&#39; Clique revela o veredito e a linha '
    'que prova. A quarta e a que importa: o ganho foi incremental, e por isso invisivel &mdash; '
    'e exatamente o motivo de esta aula existir.',
    'Check Understanding', 'True or', 'False', ['tf']))

add(L.s_blocks(
    14, 3,
    '<strong>Discussao (5 min):</strong> Tres perguntas abertas. Deixe o Felipe falar sem '
    'correcao no meio; anote e devolva depois (ele trava se for cortado). A segunda pergunta '
    'e a que voce quer de verdade: qual e o silencio que ele ainda preenche com um pedido de '
    'desculpa.',
    'Discuss', 'Talk It', 'Through', ['guiding']))

# ============================================================ CHAPTER 4 -- the code
add(L.s_chapter(
    15, 4,
    '<strong>Transicao gramatica (1 min):</strong> Diga: &#39;One last structure, and it is the '
    'mirror of the first one you learned. Lesson 1 was the present perfect &mdash; standing '
    'here, looking back. Tonight you stand in the future and look back from there.&#39;',
    'Chapter 4: The Code',
    'Standing in the Future,', 'Looking Back', '', L.IMG['code']))

add(L.s_discovery(
    16, 4,
    '<strong>Discovery (7 min):</strong> NUNCA revele a regra primeiro (REGRA 27). Toque os '
    'quatro exemplos e pergunte o que se repete. Guie: &#39;Where is the speaker standing when '
    'he says this &mdash; now, or later?&#39; (later). &#39;And is the action finished at that '
    'moment?&#39; (yes, in the first three). So entao clique em Reveal the Rule. CCQ final: '
    '&#39;By June I will have led the team for a year &mdash; am I leading it now?&#39; (yes, '
    'and I still will be in June).',
    [('&#39;By the time the board meets, we <span class="accent">will have closed</span> the quarter.&#39;',
      'By the time the board meets, we will have closed the quarter.'),
     ('&#39;By December I <span class="accent">will have presented</span> four sets of results in English.&#39;',
      'By December I will have presented four sets of results in English.'),
     ('&#39;By the fourteenth I <span class="accent">will have sent</span> you the deck.&#39;',
      'By the fourteenth I will have sent you the deck.'),
     ('&#39;By this time next year I <span class="accent">will have been leading</span> in English for eighteen months.&#39;',
      'By this time next year I will have been leading in English for eighteen months.')],
    'All four sentences stand at a point in the future. What has to appear in every one of them?',
    [('will have + past participle', 'finished before a future point', 'By Friday I will have signed it.'),
     ('will have been + -ing', 'still running at that point, seen as a length',
      'By June I will have been leading the team for two years.'),
     ('by + a future point', 'the deadline the sentence looks back from', 'by then &middot; by 2027 &middot; by the fourteenth'),
     ('by the time + PRESENT tense', 'the deadline clause never takes will', 'By the time they ask, I will have prepared it.'),
     ('present perfect vs future perfect', 'looking back from now vs from later',
      'I have led it for six months. / By June I will have led it for a year.')],
    'Two questions decide the form. Is it finished at that point, or still running? Finished takes '
    '<strong>will have done</strong>; still running takes <strong>will have been doing</strong>. And where '
    'is the deadline? If the deadline is a clause, it stays in the present &mdash; <strong>by the time they '
    'ask</strong>, never by the time they will ask.',
    'rule16'))

add(L.s_mistake(
    17, 4,
    '<strong>Common mistake (4 min):</strong> Os tres erros que um brasileiro faz aqui. O '
    'primeiro e o futuro duplicado depois de <em>by the time</em>. O segundo e <em>until</em> no '
    'lugar de <em>by</em> &mdash; em portugues os dois viram <em>ate</em>, e por isso este erro '
    'sobrevive ao B2. O terceiro e o futuro simples onde a frase pede duracao. Peca a versao '
    'certa em voz alta antes de mostrar o lado verde.',
    [('By the time they will ask, I will have prepared it.',
      'By the time they ask, I will have prepared it.'),
     ('Until Friday I will have signed the contract.',
      'By Friday I will have signed the contract.'),
     ('By June I will work here for two years.',
      'By June I will have been working here for two years.')],
    '<strong>Until</strong> is the whole stretch of time before a moment; <strong>by</strong> is the deadline '
    'itself. And a clause after <strong>by the time</strong> stays in the present: the future is already '
    'carried by the main verb.'))

add(L.s_fill(
    18, 4,
    '<strong>Grammar practice (5 min):</strong> Ele diz a frase INTEIRA em voz alta antes de '
    'clicar. Exija a contracao natural (<em>I&#39;ll have</em>), nao a forma cheia. Se ele '
    'hesitar entre as duas formas, volte a pergunta do discovery: finished, or still running?',
    'Practice', 'Stand at the Deadline and', 'Look Back',
    'Say the whole sentence out loud, then click to check',
    [('By the time the audit committee meets, I ', 'will have presented', ' the numbers twice.'),
     ('By this time next year I ', 'will have been working', ' in English every day for eighteen months.'),
     ('By Friday we ', 'will have closed', ' the quarter.'),
     ('By the time you land in London, I ', 'will have sent', ' you the deck.'),
     ('By December I ', 'will have been leading', ' this team for two years.')]))

# ============================================================ CHAPTER 5 -- the call again
add(L.s_chapter(
    19, 5,
    '<strong>Transicao (1 min):</strong> Diga: &#39;The same head-hunter who called you in Lesson '
    '1 is calling again. Same woman, same accent, one year later.&#39; Nao explique mais nada.',
    'Chapter 5: The Call, Again',
    'Sarah Whitmore Is on the Line &mdash;', 'One Year Later', '', L.IMG['practice']))

DIALOGUE = [
    ('sarah', 'S', 'ellen',
     'Felipe, Sarah Whitmore. A year ago I called you about a CFO role and you took the call in '
     'English for the first time. I want to put you in front of a board next month. Before I do '
     '&mdash; how would you describe where you are now?',
     'Felipe, Sarah Whitmore. A year ago I called you about a CFO role and you took the call in '
     'English for the first time. I want to put you in front of a board next month. Before I do, '
     'how would you describe where you are now?'),
    ('felipe', 'F', 'arthur',
     'Honestly? I&#39;d say I&#39;ve <span class="accent">come a long way</span>, though I&#39;d '
     'stop short of calling it finished. Twelve months ago I could follow everything and produce '
     'almost nothing. Now I chair the quarterly call myself.',
     'Honestly? I&#39;d say I&#39;ve come a long way, though I&#39;d stop short of calling it '
     'finished. Twelve months ago I could follow everything and produce almost nothing. Now I '
     'chair the quarterly call myself.'),
    ('sarah', 'S', 'ellen',
     'That is a real shift. What made the difference, do you think?',
     'That is a real shift. What made the difference, do you think?'),
    ('felipe', 'F', 'arthur',
     'Repetition, mostly. It is <span class="accent">muscle memory</span> more than knowledge '
     '&mdash; the phrases arrive before I choose them. And I stopped apologizing for the pause. '
     'Now I <span class="accent">fall back on</span> one line: let me put that another way.',
     'Repetition, mostly. It is muscle memory more than knowledge. The phrases arrive before I '
     'choose them. And I stopped apologizing for the pause. Now I fall back on one line: let me '
     'put that another way.'),
    ('sarah', 'S', 'ellen',
     'Some candidates tell me they are fluent and then freeze on the first difficult question. '
     'Where would you say your <span class="accent">blind spot</span> still is?',
     'Some candidates tell me they are fluent and then freeze on the first difficult question. '
     'Where would you say your blind spot still is?'),
    ('felipe', 'F', 'arthur',
     'On a bad line, with three people talking at once. I <span class="accent">hold my own</span> '
     'in a meeting; a crowded call is still work. I would rather be candid about that than '
     'oversell it.',
     'On a bad line, with three people talking at once. I hold my own in a meeting; a crowded '
     'call is still work. I would rather be candid about that than oversell it.'),
    ('sarah', 'S', 'ellen',
     'That answer is exactly why I am calling. One more thing &mdash; the board meets on the '
     'fourteenth. Will you be ready?',
     'That answer is exactly why I am calling. One more thing: the board meets on the fourteenth. '
     'Will you be ready?'),
    ('felipe', 'F', 'arthur',
     'By the fourteenth I <span class="accent">will have presented</span> these numbers four '
     'times, so yes. And by then I <span class="accent">will have been running</span> this '
     'function in English for a full year. It will not be my first difficult room.',
     'By the fourteenth I will have presented these numbers four times, so yes. And by then I '
     'will have been running this function in English for a full year. It will not be my first '
     'difficult room.'),
    ('sarah', 'S', 'ellen',
     'Good. I will send you the brief tonight. You have changed since that first call, '
     'haven&#39;t you?',
     'Good. I will send you the brief tonight. You have changed since that first call, '
     'haven&#39;t you?'),
    ('felipe', 'F', 'arthur',
     'I have. Same numbers &mdash; different voice.',
     'I have. Same numbers, different voice.'),
]

add(L.s_dialogue(
    20, 5,
    '<strong>Dialogo (8 min):</strong> Uma fala por vez no botao Next Line. Pare depois da '
    'quarta fala e pergunte: &#39;Which lesson does that sentence come from?&#39; (muscle memory '
    '/ fall back on = hoje; a tag do fim = aula 15; o hedging do <em>I would rather be candid</em> '
    '= aula 12). Na penultima fala, faca ele NOTAR a tag da Sarah. Depois, releia o dialogo com '
    'ele fazendo a voz do Felipe &mdash; e a fala dele, literalmente.',
    'A Call You Could Not Have', 'Taken', DIALOGUE))

add(L.s_comprehension(
    21, 5,
    '<strong>Comprehension (4 min):</strong> As perguntas sao sobre a SARAH, nunca sobre o proprio '
    'Felipe (REGRA 27F). Ele responde em voz alta ANTES de clicar. A terceira e a mais '
    'importante: ela liga por causa da resposta CANDIDA, nao da confiante &mdash; e a licao de '
    'senioridade do programa inteiro.',
    'About', 'Sarah',
    [('What does Sarah want to do next month, and what does she do before that?',
      'She wants to put him in front of a board, and before that she asks him to describe where his English is now.'),
     ('What does Sarah say some other candidates do?',
      'They tell her they are fluent, and then they freeze on the first difficult question.'),
     ('Which of his answers does Sarah say is the reason she is calling?',
      'The candid one about the blind spot on a crowded line, not the confident one.'),
     ('What date does Sarah give him, and what does she promise to send?',
      'The board meets on the fourteenth, and she will send the brief tonight.')]))

add(L.s_listening(
    22, 5,
    '<strong>Listening 1 (5 min):</strong> LEIA AS PERGUNTAS EM VOZ ALTA COM O FELIPE ANTES de '
    'tocar (elas ja estao na tela). Diga: &#39;Sarah again, but this is a voicemail &mdash; the '
    'same kind of message she left you in Lesson 1.&#39; Toque SEM texto, duas vezes. Depois '
    'volte as perguntas.',
    1, 'Listening', 'The Same Voicemail,', 'One Year On',
    'A head-hunter leaves a message she has left before. Sound first, no text. Read the questions first.',
    'a16_listening_sarah.mp3', 'felipe-pimenta',
    [('What is different about this role compared with the one a year ago?',
      'It is bigger, and the conversation is with the board rather than the chief executive &mdash; four people, one hour.'),
     ('What advice does she give every senior candidate?',
      'Do not try to sound perfect; be able to say what you do not know, in a full sentence, without apologizing for it.'),
     ('Why does she tell him to listen to the first message again?',
      'Because he will not recognize the man who answered it &mdash; the distance is the point.')]))

add(L.s_listening(
    23, 5,
    '<strong>Listening 2 (5 min):</strong> LEIA AS PERGUNTAS COM ELE ANTES de tocar. Este audio e '
    'a conversa de MANUTENCAO da aula: o que fazer quando o pacote acaba. Toque duas vezes e '
    'depois pergunte, fora do slide: &#39;Which of those three will you actually do?&#39; Anote a '
    'resposta &mdash; ela e o homework real do fim de contrato.',
    2, 'Listening 2', 'What Happens When the Course', 'Ends',
    'A corporate language lead on the part nobody plans for. Sound first, no text. Read the questions first.',
    'a16_listening_coach.mp3', 'felipe-pimenta',
    [('According to the speaker, what fades first when you stop using the language?',
      'Not grammar &mdash; speed. You still understand everything, you just take a second longer to produce it.'),
     ('What does he recommend doing once a month, and why?',
      'Recording yourself and keeping the files, because the progress is too slow to feel but obvious on two recordings six months apart.'),
     ('Which benchmark does he reject, and what does he put in its place?',
      'He rejects the native speaker as a benchmark and puts your own first-day recording in its place.')]))

# ============================================================ CHAPTER 6 -- your turn
add(L.s_chapter(
    24, 6,
    '<strong>Transicao (1 min):</strong> Diga: &#39;Now everything at once. Nobody tells you which '
    'structure to use tonight &mdash; that is the whole exam.&#39;',
    'Chapter 6: Your Turn',
    'Every Structure, No', 'Labels', '', L.IMG['turn']))

add(L.s_error(
    25, 6,
    '<strong>Spot the error (6 min):</strong> Um erro de cada bloco do programa: futuro perfeito, '
    'condicional misto, discurso indireto, present perfect, question tag e causativo. Ele nomeia '
    'o erro ANTES de clicar &mdash; nao basta consertar, ele tem de dizer QUAL estrutura foi '
    'violada. Se travar, volte ao mapa do slide 4.',
    [('By the time they will ask, I will have prepared the answer.',
      'By the time they ask, I will have prepared the answer.'),
     ('If I would have started earlier, I would be fluent now.',
      'If I had started earlier, I would be fluent now.'),
     ('She told me that she will send the brief tonight.',
      'She told me she would send the brief tonight.'),
     ('I am working in corporate finance since 2014.',
      'I have been working in corporate finance since 2014.'),
     ('She is not from here, is not she?',
      'She is not from here, is she?'),
     ('We had the agency to prepare the board pack.',
      'We had the agency prepare the board pack.')]))

add(L.s_artifact(
    26, 6,
    '<strong>Artefato (5 min):</strong> Este e o registro do programa dele, com o nome dele. Leia '
    'linha por linha em voz alta. As duas ultimas linhas sao as que importam: o que ele leva '
    'ADIANTE (nao esta consertado) e o proximo benchmark. Na terceira pergunta, exija a frase '
    'INTEIRA no future perfect &mdash; e o compromisso saindo da boca dele, nao da tela.',
    'The Artifact', 'The Program', 'Record',
    'ALUMNI BY BETTER', 'Program record',
    [('Student', 'Felipe Pimenta &mdash; CFO, Fintech'),
     ('Program', 'Business English &mdash; Finance &amp; Career'),
     ('Lessons', '16 of 16 &mdash; complete'),
     ('Baseline (Lesson 1)', 'Three minutes, recorded, no notes'),
     ('Milestone (Lesson 16)', 'Same prompt, same clock, recorded again'),
     ('Carried forward', 'Speed on a crowded line &middot; asking for repetition without apologizing'),
     ('Next benchmark', 'By this time next year: eighteen months leading in English')],
    [('Which two recordings does this record put side by side, and why those two?',
      'The Lesson 1 baseline and the Lesson 16 milestone &mdash; same prompt, same clock, so the only thing that changed is you.'),
     ('What does the record list as carried forward rather than finished?',
      'Speed on a crowded line, and asking for a question to be repeated without apologizing for it.'),
     ('Read the last line out loud as a full sentence. What does it commit you to?',
      'By this time next year I will have been leading in English for eighteen months.')]))

add(L.s_quickfire(
    27, 6,
    '<strong>Quick fire (6 min):</strong> UMA situacao por vez, Previous/Next. Aqui esta a prova '
    'real da aula: ele nao tem de produzir a frase certa, ele tem de ESCOLHER a ferramenta certa. '
    'Peca a estrutura EM VOZ ALTA antes de abrir Tips (&#39;third conditional&#39;, '
    '&#39;signposting&#39;, &#39;STAR&#39;). So depois abra as dicas para comparar.',
    'Which Tool Does This Moment', 'Need?'))

add(L.s_roleplay(
    28, 6,
    '<strong>Role-play guiado (4 min):</strong> Voce e a Sarah. Pergunte: &#39;How would you '
    'describe where your English is now?&#39; Tres frases, nao mais. Exija a estrutura: onde '
    'estava, onde esta, e UMA coisa que ainda e trabalho. Se ele so elogiar a si mesmo, pare e '
    'peca a terceira parte de novo &mdash; a franqueza e o que a Sarah compra.',
    'Where You Are', 'Now',
    'Sarah asks you to describe where your English is today. Three sentences: where you were '
    'twelve months ago, where you are now, and one thing that is still work.',
    ['twelve months ago', 'come a long way', 'second nature', 'hold my own', 'blind spot']))

add(L.s_roleplay(
    29, 6,
    '<strong>Role-play semi-livre (4 min):</strong> Menos pistas. Voce e a Sarah e pergunta se ele '
    'estara pronto no dia catorze. Ele NAO pode responder so &#39;yes&#39;: tem de sustentar o '
    'compromisso com o que ja estara feito ate la, no future perfect, e com um numero. Se sair no '
    'futuro simples, devolva a pergunta do discovery: finished, or still running?',
    'Commit to the', 'Fourteenth',
    'The board meets on the fourteenth and Sarah asks whether you will be ready. Say yes &mdash; '
    'and back it with what will already be done by then, and by how much.',
    ['by the fourteenth', 'will have presented', 'four times', 'by then', 'will have been leading']))

add(L.s_roleplay(
    30, 6,
    '<strong>Free practice &mdash; O MOMENTO DO PROGRAMA (8 min):</strong> Este cenario e IDENTICO, '
    'palavra por palavra, ao free practice da AULA 1. Mesmo relogio, zero pistas. NAO interrompa, '
    'NAO corrija no meio. Quando terminar: abra a gravacao dele da aula 1 (aba Pre-class, Stage 5 '
    'da aula 1, ou o Supabase) e TOQUE AS DUAS, uma depois da outra, sem comentar. Deixe o '
    'silencio fazer o trabalho. So depois pergunte: &#39;What do you hear?&#39; CELEBRE muito.',
    'The Screening Call,', 'Again',
    'From Hello to Let us set up the next call: take the screening call end to end. Introduce '
    'yourself, tell your story, explain why you want the move, ask about the client and the '
    'process, and agree on a next step. This is the exact task you recorded in Lesson 1 &mdash; '
    'same scenario, same clock.',
    []))

# ============================================================ CHAPTER 7 -- wrap-up
add(L.s_chapter(
    31, 7,
    '<strong>Transicao wrap-up (1 min):</strong> Diga: &#39;Sixteen lessons ago that call would '
    'have finished you. Tonight it did not.&#39; Passe ao proximo.',
    'Chapter 7: Wrap-Up',
    'You Took the Call You Could Not', 'Take', '', L.IMG['wrap']))

add(L.s_survival(
    32, 7,
    '<strong>Survival card (3 min):</strong> Estas cinco nao sao frases de aula, sao frases de '
    'carreira &mdash; ele vai usa-las em uma sala de verdade nos proximos meses. Leia cada uma, '
    'toque o audio, peca a repeticao. A quarta e a mais dificil de dizer sem se desculpar: '
    'insista ate sair firme, sem sorriso de pedido de licenca.',
    'Five Phrases for the Next', 'Twelve Months',
    ['I&#39;ve come a long way, though I&#39;d stop short of calling it finished.',
     'By the fourteenth I&#39;ll have presented these numbers four times.',
     'I hold my own in a meeting; a crowded call is still work.',
     'I don&#39;t know that off the cuff, but I&#39;ll have an answer by Friday.',
     'Sorry, I lost you there &mdash; could you give me that last part again?']))

add(L.s_checklist(
    33, 7,
    '<strong>Checklist (2 min):</strong> Diga: &#39;Click each item if you feel confident.&#39; '
    'Leia cada item. Os 5 checks marcados = aula completa e stamp 16 no passaporte (registra no '
    'Supabase) &mdash; e o pacote fecha em 16 de 16.',
    16,
    ['I can describe where my English was, where it is, and what is still work &mdash; without apologizing.',
     'I use the future perfect to commit to a deadline: by then I will have done it.',
     'I choose the structure the moment needs &mdash; third conditional, STAR, hedging, signposting &mdash; without being told which.',
     'I fill a pause with a phrase I can fall back on instead of an apology.',
     'I know my words: baseline, benchmark, second nature, muscle memory, off the cuff, blind spot, to hold my own, to come a long way.']))

# ---- SLIDE 34: fim do PROGRAMA (nao ha aula 17) -------------------------------
add(L._slide(
    34, 7, 'slide-dark',
    '<strong>Encerramento do PROGRAMA (3 min):</strong> Esta e a ULTIMA aula do contrato &mdash; '
    'nao prometa uma proxima, ela nao existe. Diga: &#39;Sixteen of sixteen, Felipe. Program '
    'complete.&#39; Depois, ORALMENTE (nunca escrito na tela), deixe o plano de manutencao: (1) '
    'quinze minutos falando em voz alta, tres vezes por semana &mdash; velocidade, nao '
    'vocabulario; (2) gravar tres minutos uma vez por mes e GUARDAR o arquivo, sempre com o mesmo '
    'prompt da aula 1; (3) entrar de proposito em uma sala por mes onde ele seja o menos fluente '
    'presente. Feche pedindo que ele mande a gravacao de hoje junto com a da aula 1 &mdash; as '
    'duas, no mesmo e-mail, para ele mesmo.',
    '  <div class="slide-inner" style="text-align:center">\n'
    '    <div class="chapter-label">Program Complete</div>\n'
    '    <div class="badge-card">\n'
    '      <div class="badge-icon">\n'
    '        <div class="badge-circle"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
    'stroke-width="1.5"><path d="M12 2l2.4 7.4H22l-6 4.6 2.3 7.4-6.3-4.6L5.7 21.4 8 14 2 9.4h7.6z"/>'
    '</svg></div>\n'
    '        <div class="sparkles">' + '<div class="sparkle"></div>' * 6 + '</div>\n'
    '      </div>\n'
    '      <h2 class="slide-heading" style="color:#fff">Sixteen of <span class="accent">Sixteen</span></h2>\n'
    '      <p style="color:rgba(255,255,255,.78);font-size:1rem;margin-top:.5rem">You started this '
    'program as the man who understood every word in the room and said none of them. Tonight you '
    'ran the whole call, and then you listened to the man who could not.</p>\n'
    '      <p style="color:rgba(255,255,255,.82);font-size:.85rem;margin-top:1.5rem">'
    'Lesson 16 &mdash; Complete. Program complete.</p>\n'
    '      <p style="color:var(--accent-light);font-size:.9rem;margin-top:.5rem">The baseline was '
    'never the verdict. It was the distance you were about to travel.</p>\n'
    '    </div>\n  </div>'))

html = '\n'.join(S)
open(os.path.join(HERE, 'slides.html'), 'w', encoding='utf-8').write(html)
import re  # noqa: E402
print('slides:', len(re.findall(r'<div class="slide ', html)),
      '| speakable:', len(set(L.SPEAKABLE)))
bad = re.findall(r"speakText\('[^']*'", html)
assert not bad, f'REGRA 7.1 violada: {bad[:2]}'
