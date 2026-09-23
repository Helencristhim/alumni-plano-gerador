# -*- coding: utf-8 -*-
# Aula 7 -- The Full Room (modelo FALA: dialogo line-by-line + 3 role-plays)
U = 'https://images.unsplash.com/'

L = {
    'model': 'speaking',
    'title_html': "The Full <span class='accent'>Room</span>",
    'hero_line': 'Four nationalities, three interpretation booths and one moderator keeping time',
    'menu_desc': 'Moderating a multilateral panel, and the order of words in front of the noun',
    'grammar_point': 'adjective order in complex executive noun phrases',
    'phases': ['The Lineup', 'Words of the Panel', 'The Code', 'On Stage', 'Practice', 'Your Turn', 'Wrap-Up'],
    'guest_key': 'amara', 'guest_voice': 'ellen',
    'imgs': {
        'hero': U + 'photo-1511578314322-379afb476865?w=1400&q=80',
        'ch2': U + 'photo-1587825140708-dfaf72ae4b04?w=1400&q=80',
        'ch_grammar': U + 'photo-1455390582262-044cdead277a?w=1400&q=80',
        'ch4': U + 'photo-1475721027785-f74eccf877e2?w=1400&q=80',
        'ch5': U + 'photo-1517245386807-bb43f82c33c4?w=1400&q=80',
        'ch_rp': U + 'photo-1540575467063-178a50c2df87?w=1400&q=80',
        'ch7': U + 'photo-1473341304170-971dccb5ac1e?w=1400&q=80',
        'pc': U + 'photo-1511578314322-379afb476865?w=600&q=80',
    },
    'warmup': {
        'heading': "What the Moderator <span class='accent'>Did Right</span>",
        'sub': 'Think of the best multilateral panel you have attended. What did the moderator do that you already do, and what would you do differently? Use two words from last lesson: a lede, on background, a key message, a holding statement.',
    },
    'target': {
        'heading': "Run a Room That Speaks <span class='accent'>Four Languages</span>",
        'steps': [
            'Set the ground rules and the clock before the first answer, not after the third.',
            'Describe people and projects precisely, with words in the order a native listener expects.',
            'Speak for the interpreters as well as the room: noun early, pause at the end of the idea.',
        ],
    },
    'diagnostic': {
        'heading': "Introduce <span class='accent'>the Lineup</span>",
        'p1': 'Four panelists: a director from a multilateral development bank, a Chinese policy bank, a Canadian pension fund and the Brazilian ministry.',
        'p2': 'Introduce all four in under sixty seconds, with one precise description for each. Do it now.',
    },
    'ch2': {'heading': "The Words of <span class='accent'>the Panel</span>",
            'sub': 'Fourteen words for running a panel from the first rule to the last thought'},
    'vocab': [
        {'word': 'A multilateral development bank', 'def': 'A bank owned by several countries that lends money for development projects', 'ex': 'A multilateral development bank took the first loss on the rail project.', 'icon': 'globe'},
        {'word': 'A rapporteur', 'def': 'The person who records a discussion and reports its conclusions', 'ex': 'The rapporteur will present the conclusions at eleven forty.', 'icon': 'pen'},
        {'word': 'Ground rules', 'def': 'The basic rules everyone agrees to follow in a discussion', 'ex': 'Two ground rules: ninety seconds per answer, and no slides.', 'icon': 'scale'},
        {'word': 'A speaking slot', 'def': 'The fixed amount of time a person is given to speak', 'ex': 'Each panelist has a three-minute speaking slot.', 'icon': 'clock'},
        {'word': 'To time-box', 'def': 'To give a discussion or activity a strict time limit', 'ex': 'Let me time-box the questions from the floor to ten minutes.', 'icon': 'calendar'},
        {'word': 'A follow-up question', 'def': 'A second question that asks for more detail about an answer', 'ex': 'Let me ask a follow-up question on that number.', 'icon': 'message'},
        {'word': 'A lightning round', 'def': 'A fast series of short questions, each answered in a few seconds', 'ex': 'We will finish with a lightning round: one word each.', 'icon': 'zap'},
        {'word': 'A closing round', 'def': 'The final moment when each panelist gives a last short comment', 'ex': 'In the closing round, every panelist has thirty seconds.', 'icon': 'refresh'},
        {'word': 'A parting thought', 'def': 'A final idea someone leaves the audience with', 'ex': 'Her parting thought was to fund the projects that are ready.', 'icon': 'star'},
        {'word': 'Simultaneous interpretation', 'def': 'Spoken translation delivered at the same time as the speaker is talking', 'ex': 'The panel has simultaneous interpretation into Spanish and Mandarin.', 'icon': 'mic'},
        {'word': 'A breakout session', 'def': 'A smaller group discussion that runs alongside the main program', 'ex': 'The licensing debate continues in the breakout session after lunch.', 'icon': 'users'},
        {'word': 'A consensus statement', 'def': 'A short text that everyone in a discussion agrees to sign', 'ex': 'The panel agreed to publish a consensus statement by Friday.', 'icon': 'doc'},
        {'word': 'To wrap up', 'def': 'To bring a discussion or event to its end', 'ex': 'We have two minutes, so let me wrap up.', 'icon': 'target'},
        {'word': 'A lineup', 'def': 'The group of speakers chosen for a panel or an event', 'ex': 'The lineup includes two banks, a fund and the ministry.', 'icon': 'layers'},
    ],
    'pron_heading': "The Noun Arrives, Then the <span class='accent'>Pause</span>",
    'pron': ['A rapporteur', 'Simultaneous interpretation', 'A multilateral development bank', 'What the funds need is a credible long-term multilateral guarantee.'],
    'vocab_fill': [
        ('The person who will summarize the conclusions at the end is ', 'a rapporteur', '.'),
        ('Before the first question, the moderator explained the ', 'ground rules', ': ninety seconds per answer.'),
        ('The answer was vague, so the moderator asked ', 'a follow-up question', '.'),
        ('We have forty people waiting to ask questions, so I need to ', 'time-box', ' this part to ten minutes.'),
        ('Mandarin and Spanish speakers followed the panel through ', 'simultaneous interpretation', '.'),
        ('Two minutes before the end, the moderator started to ', 'wrap up', ' the discussion.'),
    ],
    'ch_grammar': {'heading': "The Order Nobody <span class='accent'>Teaches</span>",
                   'sub': 'Every word is correct, and one phrase still sounds wrong'},
    'grammar': {
        'heading': "Three Sound Natural. <span class='accent'>One Does Not.</span>",
        'examples': [
            "a <span style='color:#b91c1c;font-weight:700'>robust</span> <span style='color:#b45309;font-weight:700'>long-term</span> <span style='color:#1d4ed8;font-weight:700'>bilateral</span> <span style='color:#15803d;font-weight:700'>infrastructure</span> framework",
            "an <span style='color:#b91c1c;font-weight:700'>ambitious</span> <span style='color:#b45309;font-weight:700'>new</span> <span style='color:#1d4ed8;font-weight:700'>Brazilian</span> <span style='color:#15803d;font-weight:700'>rail</span> concession",
            "two <span style='color:#b91c1c;font-weight:700'>experienced</span> <span style='color:#1d4ed8;font-weight:700'>Canadian</span> <span style='color:#15803d;font-weight:700'>pension</span> funds",
            "a bilateral long-term robust infrastructure framework",
        ],
        'prompt': 'Every word in the last phrase is correct English, and a native listener would still stop you. Look at the colors in the first three: which kind of word always comes first, which kind always sits next to the noun, and what comes in between?',
        'rule_head': ['Position', 'Kind of word', 'Example'],
        'rule_rows': [
            ('1. Opinion', 'robust, ambitious, credible, experienced', 'a <strong>credible</strong> plan'),
            ('2. Size, age or time', 'large, new, long-term, early-stage', 'a credible <strong>long-term</strong> plan'),
            ('3. Origin or scope', 'Brazilian, regional, bilateral, multilateral', 'a credible long-term <strong>regional</strong> plan'),
            ('4. Type or purpose (closest to the noun)', 'infrastructure, rail, pension, risk-mitigation', 'a credible long-term regional <strong>infrastructure</strong> plan'),
            ('Hyphens before the noun', 'long-term, early-stage, risk-mitigation', 'a <strong>long-term</strong> plan, but the plan is <strong>long term</strong>'),
            ('Know when to stop', 'three or four before the noun, then use a clause', 'a regional infrastructure plan <strong>that is credible and long term</strong>'),
            ('The trap', 'the word next to the noun is never plural', 'Not <em>a pensions fund</em>. Say <strong>a pension fund</strong>.'),
        ],
        'oneliner': 'Opinion, then time, then origin, then the word that says what kind -- and the more technical the word, the closer it sits to the noun.',
    },
    'grammar_practice': {
        'heading': "Put the Words in <span class='accent'>Their Place</span>",
        'items': [
            ('We need ', 'a credible long-term regional', ' infrastructure plan. (opinion, time, scope)'),
            ('The bank financed ', 'an ambitious new Brazilian rail', ' concession. (opinion, age, origin, type)'),
            ('Two ', 'experienced Canadian pension', ' funds joined the panel. (opinion, origin, type)'),
            ('The guarantee is ', 'a comprehensive early-stage risk-mitigation', ' mechanism. (opinion, time, purpose)'),
            ('The contract lasts thirty years, so it is ', 'long term', '. (after the verb, no hyphen)'),
            ('Every ', 'pension', ' fund in the room asked about currency. (never plural next to the noun)'),
        ],
    },
    'ch4': {'heading': "The Multilateral <span class='accent'>Panel</span>",
            'sub': 'On stage with a development bank, two recordings and the run sheet'},
    'dialogue': {
        'heading': "Ninety Seconds <span class='accent'>per Answer</span>",
        'guest_name': 'Amara', 'guest_initial': 'A',
        'lines': [
            ('g', 'Welcome back. Two <span class="vocab-highlight">ground rules</span>: ninety seconds per answer, and everyone gets a closing round. Amara, you lead infrastructure at <span class="vocab-highlight">a multilateral development bank</span>. Why is your bank in this room?'),
            ('a', 'Because we are the ones who can take the first loss. A robust long-term guarantee from us changes how every pension fund reads a Brazilian rail concession.'),
            ('g', 'Let me ask <span class="vocab-highlight">a follow-up question</span> on that. First loss for how long, and on which risks?'),
            ('a', 'The first seven years, on construction and currency. After that, the project has to stand on its own.'),
            ('g', 'That is the key message for the funds here tonight. I am going to <span class="vocab-highlight">time-box</span> the next part with <span class="vocab-highlight">a lightning round</span>: ten seconds each. Amara, one word for the biggest obstacle.'),
            ('a', 'Licensing.'),
            ('g', 'And one word for what would unlock it?'),
            ('a', 'Predictability. Although I suspect that is two ideas hiding in one word.'),
            ('g', 'It counts. We have <span class="vocab-highlight">a rapporteur</span> taking notes and <span class="vocab-highlight">simultaneous interpretation</span> for our colleagues from Beijing, so let me summarize for the booth: the bank takes early risk, and licensing is the bottleneck. Amara, your <span class="vocab-highlight">parting thought</span>.'),
            ('a', 'Stop asking whether Brazil is ready. Ask which projects are ready, and fund those first.'),
        ],
        'comp': [
            ('What does Amara lead, and why does she say her bank is in the room?', 'Infrastructure at a multilateral development bank. Her bank is there because it can take the first loss.'),
            ('For how long, and on which risks, does her bank take the first loss?', 'For the first seven years, on construction and currency.'),
            ('What are her two answers in the lightning round?', 'Licensing is the biggest obstacle, and predictability would unlock it.'),
            ('What is her parting thought?', 'Stop asking whether Brazil is ready; ask which projects are ready, and fund those first.'),
        ],
    },
    'listenings': [
        {'label': 'Listening 1 &middot; An Interpreter', 'title': "A Few Words <span class='accent'>Behind You</span>",
         'blurb': 'A conference interpreter on what speakers do to the booth. Sound first &mdash; no text.',
         'voice': 'arthur',
         'text': 'I have interpreted conferences for twenty years, so let me tell you what happens in the booth while you speak. We are always a few words behind you. If you pile four adjectives in front of a noun, we have to wait for the noun to know what the adjectives describe, and by then you are already in your next sentence. If you tell a joke that depends on a play on words, we cannot translate it, and half the room will laugh ten seconds after the other half. The speakers we love most do three simple things. They put the noun early. They pause at the end of each idea. And they send us their notes the night before, even if they plan to ignore them.',
         'qs': [
             ('Why does the interpreter say long strings of adjectives are a problem?', 'Because interpreters must wait for the noun to know what the adjectives describe, and by then the speaker is in the next sentence.'),
             ('What happens when a speaker tells a joke based on a play on words?', 'The interpreters cannot translate it, and half the room laughs ten seconds after the other half.'),
             ('What three things do the speakers interpreters love most do?', 'They put the noun early, pause at the end of each idea, and send their notes the night before.'),
         ]},
        {'label': 'Listening 2 &middot; The Rapporteur', 'title': "Three Conclusions and <span class='accent'>One Disagreement</span>",
         'blurb': 'The rapporteur closes a multilateral panel. Sound first &mdash; no text.',
         'voice': 'ellen',
         'text': 'Thank you. As rapporteur, I will keep this to two minutes. The panel reached three conclusions. First, a credible long-term guarantee from a multilateral development bank is what brings pension funds into early-stage projects. Second, licensing, not financing, is now the main bottleneck for new concessions. Third, large foreign investors want a neutral arbitration mechanism before they commit. There was one clear disagreement: whether the guarantee should cover currency risk, or construction risk only. The panelists agreed to publish a short consensus statement by Friday, and the discussion on licensing will continue in the breakout session this afternoon.',
         'qs': [
             ('What are the three conclusions of the panel?', 'A credible long-term guarantee from a multilateral development bank brings pension funds into early-stage projects; licensing is now the main bottleneck; and foreign investors want a neutral arbitration mechanism.'),
             ('What was the one disagreement?', 'Whether the guarantee should cover currency risk, or construction risk only.'),
             ('What will be published by Friday, and where will the licensing discussion continue?', 'A short consensus statement. The licensing discussion continues in the breakout session that afternoon.'),
         ]},
    ],
    'artifact': {
        'heading': "The Run Sheet for <span class='accent'>Panel 3</span>",
        'title': 'PANEL RUN SHEET', 'subtitle': 'Multilateral Finance for Latin American Infrastructure &middot; 10:30&ndash;11:45',
        'rows': [
            ('Lineup', 'Multilateral development bank (A. Osei) &middot; Chinese policy bank &middot; Canadian pension fund &middot; Brazilian ministry', False),
            ('Format', 'Opening 3 min &middot; two rounds &middot; lightning round &middot; closing round', False),
            ('Ground rules', '90 seconds per answer; no slides', True),
            ('Interpretation', 'Simultaneous: English, Spanish, Mandarin', False),
            ('Output', 'Rapporteur summary at 11:40; consensus statement by Friday', True),
        ],
        'note': 'Booth request: avoid idioms, name each speaker before giving them the floor, and pause after key numbers.',
        'qs': [
            ('Who is in the lineup, and in which languages is the interpretation?', 'A multilateral development bank, a Chinese policy bank, a Canadian pension fund and the Brazilian ministry. Interpretation is in English, Spanish and Mandarin.'),
            ('What are the ground rules, and what are the two outputs?', 'Ninety seconds per answer and no slides. The outputs are the rapporteur summary at eleven forty and a consensus statement by Friday.'),
            ('What does the interpretation booth ask the moderator to do?', 'Avoid idioms, name each speaker before giving them the floor, and pause after key numbers.'),
        ],
    },
    'ch5': {'heading': "Train Like a <span class='accent'>Moderator</span>", 'sub': 'Detective &middot; Speaking &middot; Building'},
    'detective': [
        ('It is a Brazilian new ambitious rail concession.', 'It is an <strong>ambitious new Brazilian</strong> rail concession.'),
        ('Two pensions funds from Canada joined the panel.', 'Two Canadian <strong>pension funds</strong> joined the panel.'),
        ('We need a long term guarantee.', 'We need a <strong>long-term</strong> guarantee.'),
        ('Now we will do a round of lightning.', 'Now we will do a <strong>lightning round</strong>.'),
    ],
    'speaking': [
        ('How do you open a panel with four nationalities and interpretation?', 'I set two ground rules, name each speaker before they talk, and avoid idioms, so the interpreters can keep up.'),
        ('Describe the guarantee the funds want from the bank.', 'A credible long-term multilateral guarantee on construction and currency risk for the first seven years.'),
        ('A panelist gives a vague answer. What do you do?', 'I ask a follow-up question: for how long, on which risks, and at what cost?'),
        ('The panel is running late. How do you end it?', 'I time-box the closing round, one parting thought each in fifteen seconds, and then I hand over to the rapporteur.'),
    ],
    'building': [
        ('a / credible / regional / long-term / plan', 'a credible long-term regional plan'),
        ('an / Brazilian / ambitious / rail / new / concession', 'an ambitious new Brazilian rail concession'),
        ('two / pension / Canadian / experienced / funds', 'two experienced Canadian pension funds'),
        ('a / early-stage / comprehensive / risk-mitigation / mechanism', 'a comprehensive early-stage risk-mitigation mechanism'),
    ],
    'roleplays': {
        'heading': "The Full Room, <span class='accent'>Three Times</span>",
        'items': [
            {'heading': "Open the <span class='accent'>Multilateral Panel</span>",
             'scenario': 'Set the ground rules, introduce the four panelists with one precise description each, and ask Amara the first question.',
             'chips': ['ground rules', 'a lineup', 'a credible long-term', 'a follow-up question']},
            {'heading': "The <span class='accent'>Lightning Round</span>",
             'scenario': 'The ministry&rsquo;s representative keeps giving vague, long answers. Time-box the rest of the session, run a lightning round, and ask one sharp follow-up question.',
             'chips': ['to time-box', 'a lightning round', 'a follow-up question', 'simultaneous interpretation']},
            {'heading': "Four Minutes of <span class='accent'>the Real Panel</span>",
             'scenario': 'Open the panel for real: one inversion, the four panelists introduced with what each one has argued before, two precise noun phrases, and a closing line with a contrast.',
             'footer': 'No notes, four minutes. Everything from Lessons 1 to 7 is allowed.'},
        ],
    },
    'ch7': {'heading': "Five Sentences for <span class='accent'>Any Panel</span>", 'sub': 'What you say when the room speaks four languages'},
    'survival_heading': "Five Sentences for <span class='accent'>Any Panel</span>",
    'survival': [
        'Two ground rules before we start: ninety seconds per answer, and a closing round for everyone.',
        'Let me ask a follow-up question: for how long, and on which risks?',
        'What the funds need is a credible long-term multilateral guarantee.',
        'For our colleagues in the booth, let me summarize that in one sentence.',
        'We are out of time, so one parting thought from each of you, in fifteen seconds.',
    ],
    'checklist': [
        'I can set ground rules and time-box a panel before it runs late.',
        'I put words in front of a noun in the natural order: opinion, time, origin, type.',
        'I use hyphens before the noun and never make the word next to the noun plural.',
        'I can run a lightning round and a closing round, and ask a sharp follow-up question.',
        'I know the words: a multilateral development bank, a rapporteur, ground rules, a speaking slot, to time-box, a follow-up question, a lightning round, a closing round, a parting thought, simultaneous interpretation, a breakout session, a consensus statement, to wrap up, a lineup.',
    ],
    'badge': {'name': 'The Full Room', 'line': 'Ground rules first, the noun in its place, and a room that speaks four languages.',
              'next': 'Next lesson: Full Circle -- the final simulation and your benchmark, in reading'},
    'teacher': {
        'opening': '<strong>Abertura (2 min):</strong> Va direto: \'Guilherme, today the room speaks four languages.\' Penultima aula: e a aula de integracao em palco. Moderar painel multilateral e o que ele faz de verdade (investidores canadenses, europeus, arabes e chineses, citados na consultoria). Conecte ao pedido de ingles neutro: aqui a inteligibilidade e testada pela cabine de interpretacao.',
        'warmup': '<strong>Warm-up com callback (5 min):</strong> Callback da aula 6: duas palavras (a lede, on background, a key message, a holding statement). Depois deixe ele comparar um moderador que admira com ele mesmo: e autoavaliacao entre pares, sem correcao.',
        'target': '<strong>Enquadramento (2 min):</strong> Tres regras. A terceira (falar para a cabine) liga direto ao pedido dele de ser entendido por indianos e chineses: pergunte se ele ja pensou nos interpretes quando fala.',
        'diagnostic': '<strong>Pergunta-gatilho (3 min):</strong> Sessenta segundos, quatro apresentacoes. ANOTE as descricoes que ele usou: quantos adjetivos antes do substantivo, e em que ordem. Quase certo aparece alguma ordem estranha ou plural no modificador (\'pensions fund\').',
        'ch2': '<strong>Transicao vocab (1 min):</strong> Diga: \'Fourteen words for running a panel.\'',
        'vocab1': '<strong>Vocab reveal 1-5 (5 min):</strong> CCQ \'a rapporteur\': \'Does the rapporteur moderate or report? (Relata.)\' Pronuncia: ra-por-TUR. CCQ \'ground rules\': \'Before or after the discussion? (Antes.)\' CCQ \'to time-box\': \'Flexible or strict limit? (Estrito.)\'',
        'vocab2': '<strong>Vocab reveal 6-10 (5 min):</strong> CCQ \'a follow-up question\': \'New topic or more detail? (Mais detalhe.)\' CCQ \'a lightning round\': \'Long or short answers? (Curtissimas.)\' CCQ \'simultaneous interpretation\': \'Written or spoken? At the same time or after? (Falada, ao mesmo tempo.)\'',
        'vocab3': '<strong>Vocab reveal 11-14 (4 min):</strong> CCQ \'a breakout session\': \'Main stage or smaller room? (Sala menor.)\' CCQ \'a consensus statement\': \'Signed by one or by all? (Todos.)\' Peca que ele descreva o lineup real do ultimo evento do GRI que moderou.',
        'pron': '<strong>Pronuncia (4 min):</strong> ra-por-TEUR, si-mul-TA-ne-ous (americano: sai-mul-TEI-ni-us), mul-ti-LAT-er-al. Na frase longa, a sequencia de adjetivos precisa de ritmo leve e o acento principal cai em GUARANTEE &mdash; e o que o interprete do Listening 1 vai pedir.',
        'vocab_fill': '<strong>Vocab in context (3 min):</strong> Banco embaixo. Ele diz antes de clicar. Se fechar rapido, peca que use tres das palavras numa frase de abertura de painel.',
        'ch_grammar': '<strong>Transicao gramatica (1 min):</strong> Diga: \'Every word is correct, and one phrase still sounds wrong.\'',
        'grammar': '<strong>Grammar discovery (7 min):</strong> Ele le as quatro em voz alta. Pergunte qual soa errada e por que. Depois as cores: vermelho = opiniao, laranja = tempo/idade, azul = origem/escopo, verde = tipo, colado no substantivo. So entao Reveal the Rule. CCQ: \'rail concession &mdash; can rail move to the front? (Nao, e o tipo.)\' CCQ: \'a long-term plan x the plan is long term &mdash; where is the hyphen? (So antes do substantivo.)\' Obstaculo classico do brasileiro avancado: plural no modificador (\'pensions fund\', \'infrastructures projects\') e ordem pelo portugues. Pragmatica: C1+ costuma produzir sequencias gramaticalmente corretas e ritmicamente estranhas &mdash; e isso que a cabine de interpretacao sente.',
        'grammar_practice': '<strong>Practice (4 min):</strong> Frase inteira antes de clicar, com ritmo leve nos adjetivos e acento no substantivo. Nas duas ultimas, cobre hifen e singular.',
        'ch4': '<strong>Transicao (1 min):</strong> Diga: \'On stage with a development bank, two recordings and the run sheet.\'',
        'dialogue': '<strong>Dialogo (7 min):</strong> Voce e a Amara Osei, diretora de infraestrutura de um banco multilateral: precisa, bem-humorada, economica. Next Line e audio. Nas falas do Guilherme, ele fala PRIMEIRO. PRAGMATICA para o fim: ele define regras, faz follow-up, time-boxa, resume para a cabine e pede parting thought &mdash; e o roteiro inteiro de moderacao em dez falas.',
        'dialogue_comp': '<strong>Comprehension (3 min):</strong> Perguntas sobre a AMARA (REGRA 27F). Na quarta, pergunte se ele concorda com o parting thought dela.',
        'listening1': '<strong>Listening 1 (5 min):</strong> LEIA AS PERGUNTAS EM VOZ ALTA COM ELE ANTES de tocar. Interprete de conferencia. Toque duas vezes. Esta gravacao fecha o arco do pedido dele: ingles neutro e ser entendido por quem nao e nativo. Pergunte: \'Which of the three things do you already do?\'',
        'listening2': '<strong>Listening 2 (5 min):</strong> LEIA AS PERGUNTAS ANTES de tocar. Rapporteur fechando o painel. Repare nos sintagmas nominais longos (a credible long-term guarantee from a multilateral development bank): peca que ele repita dois deles.',
        'artifact': '<strong>Artefato (4 min):</strong> Run sheet do painel 3. Peca que ele transforme cada linha em frase de moderacao em voz alta. Depois as perguntas. A nota da cabine repete o Listening 1: aponte.',
        'ch5': '<strong>Transicao practice (1 min):</strong> Diga: \'Now we train: detective, your own answers, and building.\'',
        'detective': '<strong>Detective (4 min):</strong> Ele corrige antes de clicar. Ordem de adjetivos, plural no modificador, hifen, e o calco \'round of lightning\'. Se algum apareceu no diagnostico do slide 4, mostre a anotacao.',
        'speaking': '<strong>Speaking (5 min):</strong> Perguntas em velocidade normal. Toda resposta com pelo menos um sintagma nominal preciso. Correcao em bloco no fim.',
        'building': '<strong>Sentence Building (4 min):</strong> Ele monta o sintagma em voz alta, com ritmo, e so depois clica. Se fechar os quatro, peca um quinto sobre um projeto real do GRI.',
        'ch_rp': '<strong>Transicao role-play (1 min):</strong> Diga: \'The full room, three times. The last one is four minutes of the real panel.\'',
        'rp1': '<strong>Role-play guiado (4 min):</strong> Voce e a Amara. Ele repete a abertura do slide 4 com regras e uma descricao precisa para cada painelista. Compare com o diagnostico: a ordem melhorou? Diga a ele.',
        'rp2': '<strong>Role-play semi-livre (5 min):</strong> Voce e o representante do ministerio, vago e longo. Ele time-boxa, faz lightning round e um follow-up afiado. Nao facilite.',
        'rp3': '<strong>Role-play livre (6 min):</strong> Quatro minutos, sem nota. E a previa da simulacao final da aula 8. No fim, cheque: inversao? reported speech na apresentacao? sintagmas na ordem? conectivo de contraste no fechamento? E UMA observacao de ritmo para a cabine.',
        'ch7': '<strong>Transicao wrap-up (1 min):</strong> Diga: \'Five sentences for any panel.\'',
        'survival': '<strong>Survival card (3 min):</strong> Audio e repeticao. Peca que use uma no proximo painel real e conte na aula 8.',
        'checklist': '<strong>Checklist (2 min):</strong> Todos os 5 = aula concluida e stamp 7. Item em que ele hesitar entra na revisao da aula 8.',
        'complete': '<strong>Encerramento (2 min):</strong> Diga: \'Ground rules first, the noun in its place, and a room that speaks four languages.\' Homework (ORALMENTE, nunca escrito na tela): gravar 4 minutos simulando a abertura do painel de hoje (inversao, dois sintagmas nominais longos, os quatro painelistas apresentados com reported speech, fechamento com conectivo de contraste) e escrever um resumo de rapporteur de 100 palavras. Proxima aula: a ultima &mdash; simulacao final e o benchmark, em leitura.',
    },
    'pc': {
        'title': 'The Full Room -- The Order in Front of the Noun',
        'desc': 'A multilateral panel with four nationalities and three interpretation booths, and a moderator who has to be understood by all of them.',
        'match_idx': [1, 2, 4, 6, 9, 11],
        'context': [
            'Advanced speakers rarely make grammar mistakes in front of a noun. They make rhythm mistakes. &ldquo;A bilateral long-term robust infrastructure framework&rdquo; is built from correct words, and a native listener still stops, because English puts those words in a fixed order.',
            'The order is roughly this. <strong>Opinion</strong> comes first: robust, credible, ambitious. Then <strong>size, age or time</strong>: new, long-term, early-stage. Then <strong>origin or scope</strong>: Brazilian, regional, bilateral, multilateral. Closest to the noun comes the word that says <strong>what kind</strong> of thing it is: infrastructure, rail, pension. So: &ldquo;a <strong>credible long-term regional infrastructure</strong> plan,&rdquo; &ldquo;two <strong>experienced Canadian pension</strong> funds.&rdquo;',
            'Two details matter. Compound words take a hyphen before the noun (&ldquo;a <strong>long-term</strong> plan&rdquo;) but not after the verb (&ldquo;the plan is <strong>long term</strong>&rdquo;). And the word next to the noun is never plural: a <strong>pension fund</strong>, not a pensions fund, even when there are many pensions.',
            'The last rule comes from the interpretation booth. If you stack five words before the noun, <strong>simultaneous interpretation</strong> falls behind, because the interpreter cannot know what the adjectives describe until the noun arrives. Stop at three or four, and put the rest in a clause. The <strong>rapporteur</strong>, the <strong>lineup</strong> and every listener in a second language will thank you.',
        ],
        'context_quiz': [
            ('According to the text, what kind of mistake do advanced speakers make in front of a noun?', ['Spelling mistakes.', 'Rhythm mistakes in word order.', 'Pronunciation mistakes.'], 1),
            ('Which word sits closest to the noun?', ['The word that says what kind of thing it is.', 'The opinion adjective.', 'The word about time.'], 0),
            ('Why does the text recommend stopping at three or four words before the noun?', ['Because English does not allow more.', 'Because it sounds too formal.', 'Because interpreters cannot know what the adjectives describe until the noun arrives.'], 2),
        ],
        'tip_title': 'Adjective Order in Executive Noun Phrases',
        'tip_lead': 'Opinion, then time, then origin, then the word that says what kind -- closest to the noun.',
        'tip_rows': [
            ('1. Opinion', 'credible, robust, ambitious', 'a <strong>credible</strong> plan'),
            ('2. Size, age or time', 'new, long-term, early-stage', 'a credible <strong>long-term</strong> plan'),
            ('3. Origin or scope', 'Brazilian, regional, multilateral', 'a credible long-term <strong>regional</strong> plan'),
            ('4. Type (next to the noun)', 'infrastructure, rail, pension', 'a credible long-term regional <strong>infrastructure</strong> plan'),
            ('Hyphens', 'before the noun only', 'a <strong>long-term</strong> plan &middot; the plan is <strong>long term</strong>'),
            ('Singular modifier', 'the word next to the noun is not plural', 'a <strong>pension</strong> fund'),
        ],
        'tip_never': 'a Brazilian new ambitious concession &middot; two pensions funds &middot; an infrastructures plan &middot; a round of lightning',
        'blanks': [
            ('We need a credible ', 'long-term', ' regional plan.', 'Hint: time comes after opinion, and it takes a hyphen before the noun -- one word with a hyphen', None),
            ('Two experienced Canadian ', 'pension', ' funds joined the panel.', 'Hint: the type word next to the noun, never plural -- one word', None),
            ('The bank financed an ambitious new ', 'Brazilian', ' rail concession.', 'Hint: origin comes before the type word -- one word', None),
            ('Let me ask ', 'a follow-up question', ' on that number.', 'Hint: a second question for more detail -- three words', None),
            ('The conclusions will be presented by ', 'a rapporteur', '.', 'Hint: the person who reports the discussion -- two words', None),
            ('We are out of time, so let me ', 'wrap up', '.', 'Hint: bring the discussion to an end -- two words', None),
        ],
        'order_title': 'Put the Moderation in Order',
        'order_lead': 'Put the moments of a multilateral panel in a logical order.',
        'order': [
            'Two ground rules: ninety seconds per answer, and a closing round for everyone.',
            'Our lineup today includes a multilateral development bank and two experienced Canadian pension funds.',
            'Amara, why is your bank in this room?',
            'Let me ask a follow-up question: for how long, and on which risks?',
            'I will time-box the next part with a lightning round, ten seconds each.',
            'We are out of time, so one parting thought from each of you.',
        ],
        'quiz': [
            ('You want to describe a guarantee precisely. You say:', ['a multilateral long-term credible guarantee', 'a credible long-term multilateral guarantee', 'a long-term credible multilateral guarantee'], 1),
            ('A panelist gave a vague answer about numbers. You say:', ['Let me ask a follow-up question on that number.', 'Let me ask another question different.', 'Can you repeat all again?'], 0),
            ('The panel is running late. You say:', ['We are late, stop please.', 'We have no more time, finish.', 'We are out of time, so one parting thought from each of you.'], 2),
            ('You want to help the interpreters. You say:', ['For our colleagues in the booth, let me summarize that in one sentence.', 'Interpreters, translate fast now.', 'Sorry for the booth.'], 0),
        ],
        'think': 'You are opening a multilateral panel on infrastructure finance. Record two minutes: two ground rules, the four panelists introduced with one precise noun phrase each, the first question, and one sentence summarized for the interpretation booth.',

        # ── Stages 1.6 a 1.9 — preparacao de prova (22/09/2026) ───────────────
        # Anatomia trazida da aula 2, depois do feedback do professor Andre.
        # Nenhum item daqui existe no deck: a pre-class PREPARA, nao repete.
        'reading_title': 'How a Room of Sixty Reaches One Sentence',
        'reading': [
            'The hardest format in this business is not the keynote. It is the closed session: sixty people '
            'around a horseshoe, four nationalities, three languages, and ninety minutes to produce '
            'something that can be written down afterwards.',

            'It begins before anybody speaks, with <b>the lineup</b>. A good one is not a list of the most '
            'senior people available; it is a list chosen so that the disagreements already in the room are '
            'represented on the floor. If everyone at the table would answer the question the same way, the '
            'session has failed before it opens and the chair has ninety minutes to fill.',

            'Then come <b>ground rules</b>, and they are worth the two minutes they cost. Who may be quoted. '
            'Whether <b>a follow-up question</b> is allowed from the floor or only from the chair. How long '
            '<b>a speaking slot</b> runs. A chair who says none of this will spend the hour negotiating it '
            'one intervention at a time.',

            '<b>Simultaneous interpretation</b> changes everything about pace. The interpreter is roughly '
            'eight seconds behind, which means a joke lands twice and an interruption lands on top of '
            'somebody else&rsquo;s sentence. Experienced chairs <b>time-box</b> each intervention on purpose '
            'and say the number out loud, because a delegate who knows she has four minutes takes four '
            'minutes, and one who does not takes eleven.',

            'The machinery in the middle is familiar enough. <b>A breakout session</b> takes twenty people '
            'into a smaller room where they will actually speak. <b>A lightning round</b> puts one question '
            'to everybody in turn, sixty seconds each, and it is the fastest way to find out where a room '
            'really is. <b>A rapporteur</b> writes down what was said, which is a defined job and not a '
            'favour asked of the youngest person present.',

            'The end is where most sessions are lost. <b>A closing round</b> in which everyone offers '
            '<b>a parting thought</b> is pleasant and produces nothing at all. If the session was convened '
            'to deliver <b>a consensus statement</b>, somebody has to put a draft sentence on the screen '
            'before the room starts to leave, and the chair has to <b>wrap up</b> by reading it aloud. '
            '<b>A multilateral development bank</b> will send four people to a session like this, and '
            'either all four report the same sentence or none of them does.',
        ],
        'comprehension': [
            ('What makes a good lineup, according to the text?',
             ['The most senior people who are available that day.',
              'A list chosen so the disagreements in the room are represented on the floor.',
              'A balance of nationalities and languages.',
              'Speakers who have not appeared at the event before.'], 1),
            ('Why are ground rules worth stating at the start?',
             ['The organisers require them to be read out.',
              'Otherwise the chair spends the hour negotiating them one intervention at a time.',
              'They protect the rapporteur from being quoted.',
              'They shorten the closing round.'], 1),
            ('What effect does simultaneous interpretation have?',
             ['It makes the session longer by about a third.',
              'It puts the interpreter eight seconds behind, so interruptions land on other people.',
              'It prevents follow-up questions from the floor.',
              'It requires every speaking slot to be written out in advance.'], 1),
            ('Why do experienced chairs say the time limit out loud?',
             ['The interpreters need it for their notes.',
              'A delegate who knows she has four minutes takes four, and one who does not takes eleven.',
              'It is a requirement of the ground rules.',
              'It allows the rapporteur to time the session.'], 1),
            ('What does the text say about the rapporteur?',
             ['The role should rotate between the delegates.',
              'It is a defined job, not a favour asked of the youngest person there.',
              'The rapporteur should also chair the breakout sessions.',
              'The notes are confidential until the statement is agreed.'], 1),
            ('Why is a closing round of parting thoughts criticised?',
             ['It runs over time in almost every session.',
              'It is pleasant and produces nothing that can be written down.',
              'It excludes the delegates who spoke earlier.',
              'It cannot be interpreted accurately.'], 1),
        ],
        'word_formation': [
            ('The chair&rsquo;s ', 'insistence', ' on the time limit saved the session. (INSIST)',
             'Noun from the verb.', None),
            ('Sixty people in three languages is ', 'unmanageable', ' without ground rules. (MANAGE)',
             'Negative prefix + -able adjective.', None),
            ('The rapporteur produced a ', 'summary', ' of four hundred words. (SUM)',
             'Noun. Not &ldquo;summation&rdquo;: this is the document.', None),
            ('', 'Surprisingly', ', the lightning round produced the only real disagreement. (SURPRISE)',
             'Sentence adverb, capital letter, comma after it.', None),
            ('A breakout room should be small enough to make silence ', 'uncomfortable', '. (COMFORT)',
             'Negative prefix + adjective.', None),
            ('The delegates reached ', 'agreement', ' on a single sentence. (AGREE)',
             'Noun from the verb.', None),
            ('Her ', 'interventions', ' were short and never wasted. (INTERVENE)',
             'Plural noun from the verb. Watch the internal change.', None),
        ],
        'transformations': [
            ('The table was round, it was old, and it was made of wood.', 'WOODEN',
             'It was ', 'an old round wooden', ' table.',
             'Age, then shape, then material.', None),
            ('The delegate was young, Brazilian, and extremely articulate.', 'BRAZILIAN',
             'She was ', 'an extremely articulate young Brazilian', ' delegate.',
             'Opinion, then age, then origin.', None),
            ('The room was small, square, and painted white.', 'WHITE',
             'It was ', 'a small square white', ' room.',
             'Size, then shape, then colour.', None),
            ('She used a pointer that was thin, black, and made of metal.', 'METAL',
             'She used ', 'a thin black metal', ' pointer.',
             'Size, then colour, then material.', None),
            ('They booked a room for the breakout sessions; it was large and on the second floor.', 'BREAKOUT',
             'They booked ', 'a large second-floor breakout', ' room.',
             'Size, then location, then purpose.', None),
            ('The rapporteur produced notes that were detailed, handwritten, and six pages long.', 'HANDWRITTEN',
             'The rapporteur produced ', 'detailed six-page handwritten', ' notes.',
             'Opinion, then measurement, then the participle that behaves like material.', None),
        ],
        'listen': {
            'file': 'pc7_listen_choose.mp3', 'voice': 'sarah_us',
            'caption': 'A conference producer, on what makes a closed session work. She is not a speaker '
                       'you heard in the lesson.',
            'text': (
                "People think producing one of these is about logistics. Rooms, microphones, name cards. It "
                "is not. It is about who is sitting where, and about the first eight minutes. "
                "The seating is not neutral. If you put the two people who disagree at opposite ends of a "
                "horseshoe, they will speak past each other for an hour and the room will watch a tennis "
                "match. Put them three seats apart and they have to talk, because it becomes physically "
                "awkward to perform. I have moved a name card twenty minutes before a session and changed "
                "the entire outcome. "
                "The first eight minutes decide the rest. If the first three interventions are all "
                "agreement, you are finished. Everybody who was going to say something difficult has now "
                "decided this is not that kind of room, and they will say it to you in the corridor "
                "afterwards, which is no use to anybody. So I brief one person in advance to go second and "
                "disagree. Not aggressively. Just clearly. "
                "The other thing nobody plans for is the end. Chairs plan the opening in detail and then "
                "improvise the last ten minutes, which is exactly backwards. If you want a sentence out of "
                "the room, you draft that sentence before the session, you put it up imperfect, and you let "
                "them correct it. People will not write a sentence together. They will happily fix one."),
        },
        'listen_choose': [
            ('What does the speaker say producing a session is really about?',
             ['Logistics: rooms, microphones and name cards.',
              'Who is sitting where, and the first eight minutes.',
              'Choosing the most senior speakers available.',
              'Keeping strictly to the published timings.'], 1),
            ('What happens if the two people who disagree sit at opposite ends?',
             ['The interpreters cannot follow the exchange.',
              'They speak past each other and the room watches a tennis match.',
              'The chair loses control of the timings.',
              'Neither of them speaks at all.'], 1),
            ('Why does she seat them three seats apart instead?',
             ['So the microphones reach both of them.',
              'Because it becomes physically awkward to perform, so they have to talk.',
              'Because the rapporteur can hear both sides.',
              'So the chair can interrupt either one.'], 1),
            ('What is the problem if the first three interventions all agree?',
             ['The session will finish early.',
              'Anyone with something difficult to say decides this is not that kind of room.',
              'The chair has to change the ground rules.',
              'The lightning round becomes impossible.'], 1),
            ('What does she do about it?',
             ['She asks the chair to challenge the first speaker.',
              'She briefs someone in advance to go second and disagree clearly.',
              'She shortens the opening remarks.',
              'She moves the breakout session earlier.'], 1),
            ('What does she say about getting a sentence out of the room?',
             ['Ask the rapporteur to draft it during the session.',
              'Draft it beforehand, put it up imperfect, and let them correct it.',
              'Leave the last ten minutes free for it.',
              'Take it to a breakout group of five people.'], 1),
        ],
    },
    'media': [
        {'id': 'podcast', 'type': 'Podcast', 'title': 'Freakonomics Radio &mdash; &ldquo;How to Make Meetings Less Terrible&rdquo;',
         'desc': 'What research says about running meetings that work: clear rules, strict time and the right people. A panel is a meeting with an audience.',
         'tip': 'Tip: write down the one rule you would add to the ground rules of your next panel.',
         'url': 'https://freakonomics.com/podcast/how-to-make-meetings-less-terrible-ep-389/', 'cta': 'Listen on Freakonomics'},
        {'id': 'talk', 'type': 'Talk', 'title': 'Celeste Headlee &mdash; &ldquo;10 ways to have a better conversation&rdquo; (TED)',
         'desc': 'A radio host who interviewed people for decades explains how to ask better questions and follow up without dominating. Everything a moderator does between the first and the last question.',
         'tip': 'Tip: choose the two rules that matter most on stage and use them in your next panel.',
         'url': 'https://www.ted.com/talks/celeste_headlee_10_ways_to_have_a_better_conversation', 'cta': 'Watch on TED'},
        {'id': 'video', 'type': 'Talk', 'title': 'Simon Sinek &mdash; &ldquo;How great leaders inspire action&rdquo; (TED)',
         'desc': 'One of the most watched talks ever, built on a single clear idea repeated in precise language. Listen to how he describes organizations: short noun phrases, in the natural order.',
         'tip': 'Tip: note three noun phrases he uses and check the order of the words in each one.',
         'url': 'https://www.ted.com/talks/simon_sinek_how_great_leaders_inspire_action', 'cta': 'Watch on TED'},
    ],
}
