#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Conteudo-fonte das 4 abas suplementares da Joice + emissor dos snippets.

A ALUNA PEDIU (consultoria com a direcao, 14/09/2026):
  "eu quero falar, so isso" -- conversacao, nao gramatica decorada
  gostou das musicas e das expressions que a Helen mostrou na tela do Diego
  tem o TEDx de Belem em novembro/2026 como alvo declarado

REGRAS QUE ESTE ARQUIVO OBEDECE
-------------------------------
* ADITIVO PURO. As 4 abas entram DEPOIS de <!-- /tab-complementary -->. Nenhum
  byte do material atual e alterado (REGRAS 12/21/30).
* SEM JS NOVO. So funcoes que o hub ja define: speakText, speakPhrase,
  startRecording, stopRecording, startFreeRecording, stopFreeRecording,
  checkMatch, verifyAllMatches, checkBlank, listenBlank, selectQuiz,
  toggleLesson, toggleMediaDone.
* REGRA 7.1: o texto vai no ATRIBUTO (data-speak / data-phrase), nunca dentro
  da string do handler.
* IDS PROPRIOS: mu-song-N / ev-group-N / fd-block-N / tx-step-N. NUNCA
  ex-lesson-N, stampN, data-slide, data-lesson-progress -- updateProgress()
  do hub varre so ex-lesson-1..20 e nao pode se mexer.
* think-result com id PROPRIO (think-result-mu1...), porque startFreeRecording
  usa o id como nome do arquivo no Storage: repetir id sobrescreve gravacao de
  aula que ela ja teve.
* REGRA 13 -- A JOICE E A1, entao a tela e BILINGUE: traducao no vocab card,
  .speech-translation no speech card, hint e enunciado em portugues, igual ao
  Pre-class dela.
* TETO DE NIVEL (aulas 1..10): to be, present simple (3a pessoa), do/does,
  possessivos, preposicoes de lugar e de tempo, adverbios de frequencia,
  can/can't, like + -ing / want to, how much/how many e some/any. Nada fora
  disso -- nem passado, nem continuo, nem going to.
* REGRA 24: opcoes do matching embaralhadas (seed fixa = build reproduzivel).
* REGRA 17: todo link vai ao video EXATO (os cinco IDs foram conferidos por
  requisicao ao YouTube em 15/09/2026), nunca a uma busca.
* SEM LETRA DE MUSICA NA TELA: a letra fica na legenda do proprio video (CC).
  As frases de pronuncia sao autorais, sobre o tema da musica.

USO: python3 _build/joice-lopes-leite-extras/build_extras.py
     (escreve os 4 snippets ao lado deste arquivo e confere as colisoes)
"""
import os
import random
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, '..', '..'))
HUBS = [os.path.join(RAIZ, 'public', 'aluno', 'joice-lopes-leite.html'),
        os.path.join(RAIZ, 'public', 'professor', 'joice-lopes-leite.html')]

ITAL = 'font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic'
INTRO = 'font-size:.85rem;color:var(--text-dim);margin-bottom:1.5rem'
LINK_STYLE = ('display:inline-block;margin-top:.5rem;font-size:.78rem;color:var(--accent);'
              'font-weight:600;text-decoration:none;border-bottom:1px solid var(--accent)')


def esc(s):
    return (s.replace('&', '&amp;').replace('<', '&lt;')
             .replace('>', '&gt;').replace('"', '&quot;'))


# ----------------------------------------------------------------- componentes
def vocab_cards(itens):
    """itens: (palavra, traducao, exemplo_en, exemplo_pt)"""
    out = ['      <div class="vocab-cards">']
    for palavra, trad, ex_en, ex_pt in itens:
        out.append(
            '        <div class="vocab-card-pc"><div class="vocab-card-content">'
            '<div class="vocab-card-header"><span class="vocab-card-word">%s</span>'
            '<span class="vocab-card-dot"> -- </span><span class="vocab-card-def">%s</span></div>'
            '<div class="vocab-card-example">"%s" (%s)</div></div>'
            '<button class="audio-btn" data-speak="%s" onclick="speakText(this.dataset.speak,this)">Listen</button></div>'
            % (esc(palavra), esc(trad), esc(ex_en), esc(ex_pt), esc(palavra)))
    out.append('      </div>')
    return '\n'.join(out)


def matching(grid_id, pares, seed):
    defs = [d for _, d in pares]
    out = ['      <div class="match-grid" id="%s">' % grid_id]
    for i, (palavra, definicao) in enumerate(pares):
        opts = defs[:]
        random.Random(seed + i).shuffle(opts)
        out.append('        <div class="match-row" data-answer="%s">' % esc(definicao))
        out.append('          <span class="match-word" style="flex:0 0 130px">%s</span>' % esc(palavra))
        out.append('          <select style="flex:1;width:100%" onchange="checkMatch(this)">')
        out.append('            <option value="">Selecione...</option>')
        for o in opts:
            out.append('            <option value="%s">%s</option>' % (esc(o), esc(o)))
        out.append('          </select>')
        out.append('        </div>')
    out.append('      </div>')
    out.append('      <button class="verify-all-btn" onclick="verifyAllMatches(\'%s\')">Conferir</button>' % grid_id)
    return '\n'.join(out)


def fill_in(itens):
    """itens: (antes, resposta, depois, dica_pt, frase_completa)"""
    out = []
    for antes, resp, depois, dica, frase in itens:
        out.append(
            '      <div class="fill-blank-item"><div class="fill-blank-sentence">%s'
            '<input class="blank-input" data-answer="%s" data-hint="%s" data-phrase="%s" placeholder="___">'
            '%s</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>'
            '<button class="check-btn" onclick="checkBlank(this)">Check</button></div>'
            % (esc(antes), esc(resp), esc(dica), esc(frase), esc(depois)))
    return '\n'.join(out)


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


def speech(frases, voz='ellen'):
    """frases: (en, pt)"""
    out = []
    for en, pt in frases:
        out.append(
            '      <div class="speech-card" data-phrase="%s" data-voice="%s">\n'
            '        <div class="speech-phrase">%s</div>\n'
            '        <div class="speech-translation">%s</div>\n'
            '        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Ouvir</button>'
            '<button class="btn btn-record" onclick="startRecording(this)">&#9679; Gravar</button>'
            '<button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Parar</button></div>\n'
            '        <div class="speech-result"></div>\n'
            '      </div>' % (esc(en), voz, esc(en), esc(pt)))
    return '\n'.join(out)


def think(result_id, pergunta):
    return ('      <div class="think-card">\n'
            '        <div class="think-question">%s</div>\n'
            '        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Gravar</button>'
            '<button class="btn btn-stop" onclick="stopFreeRecording(this)">&#9632; Parar</button></div>\n'
            '        <div id="%s"></div>\n'
            '      </div>' % (esc(pergunta), result_id))


def secao(titulo, badge, badge_cls, instrucao, corpo):
    return ('    <div class="exercise-section">\n'
            '      <div class="section-header-row"><h4>%s</h4><span class="badge %s">%s</span></div>\n'
            '      <p style="%s">%s</p>\n%s\n    </div>'
            % (esc(titulo), badge_cls, esc(badge), ITAL, esc(instrucao), corpo))


def barra_card(chave):
    return ('      <div class="lesson-progress-mini"><div class="mini-bar">'
            '<div class="mini-bar-fill" data-extra-progress="%s" style="width:0%%"></div></div>'
            '<span class="mini-percent" data-extra-pct="%s">0%%</span></div>' % (chave, chave))


def painel_aba(slot, rotulo):
    return ('<div class="extras-progress-panel" style="background:var(--bg-card);'
            'border:1px solid var(--border);border-radius:8px;padding:.9rem 1.1rem;margin-bottom:1.5rem">\n'
            '  <div style="display:flex;justify-content:space-between;align-items:baseline;gap:.8rem;'
            'flex-wrap:wrap;font-size:.78rem;color:var(--text-dim);margin-bottom:.5rem">\n'
            '    <span style="font-weight:600;color:var(--text)">%s</span>\n'
            '    <span><span data-extra-tab-done="%s">0</span> de <span data-extra-tab-total="%s">0</span> '
            'exercícios &middot; <strong data-extra-tab-pct="%s" style="color:var(--accent)">0%%</strong></span>\n'
            '  </div>\n'
            '  <div class="mini-bar" style="height:6px"><div class="mini-bar-fill" '
            'data-extra-tab="%s" style="width:0%%"></div></div>\n'
            '</div>' % (esc(rotulo), slot, slot, slot, slot))


def card(card_id, img, numero, titulo, desc, blocos):
    return ('<div class="lesson-card" id="%s">\n'
            '  <div class="lesson-header" onclick="toggleLesson(this)">\n'
            '    <div class="lesson-header-img" style="background-image:url(\'%s\')"></div>\n'
            '    <div class="lesson-header-content">\n'
            '      <div class="lesson-number">%s</div>\n'
            '      <h3>%s</h3>\n'
            '      <div class="lesson-desc">%s</div>\n'
            '%s\n'
            '    </div>\n'
            '    <div class="expand-icon">&#9660;</div>\n'
            '  </div>\n'
            '  <div class="lesson-body">\n\n%s\n\n  </div>\n'
            '</div>' % (card_id, img, esc(numero), esc(titulo), esc(desc),
                        barra_card(card_id), '\n\n'.join(blocos)))


def video(url, rotulo):
    return ('      <p><a href="%s" target="_blank" rel="noopener" style="%s">%s &#8594;</a></p>'
            % (url, LINK_STYLE, esc(rotulo)))


IMG = {
    'musica': 'https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?w=600&q=80',
    'reuniao': 'https://images.unsplash.com/photo-1517048676732-d65bc937f952?w=600&q=80',
    'escola': 'https://images.unsplash.com/photo-1523240795612-9a054b0db644?w=600&q=80',
    'palco': 'https://images.unsplash.com/photo-1475721027785-f74eccf877e2?w=600&q=80',
}


# ================================================================= ABA MUSICAS
MUSICAS = [
    dict(n=1, titulo='Imagine -- John Lennon',
         url='https://www.youtube.com/watch?v=YkgkThdzX-8',
         desc='A música mais lenta e mais clara da lista. Ótima para começar: frases curtas e quase tudo no presente.',
         quiz=[('Na primeira linha, o cantor pede para você fazer o quê? (What does he ask you to do?)',
                [('Imagine.', True), ('Listen.', False), ('Answer.', False)]),
               ('A palavra "people" aparece várias vezes. O que ela significa? (What does "people" mean?)',
                [('pessoas', True), ('lugares', False), ('perguntas', False)])],
         fala=[('I like listening to slow songs in English.', 'Gosto de ouvir músicas lentas em inglês.'),
               ('This song is about peace.', 'Esta música fala sobre paz.'),
               ('I can understand some words now.', 'Consigo entender algumas palavras agora.')],
         think=('Fale por 30 segundos: de que música em inglês você gosta, e por quê? '
                'Comece com "I like..." e use "because". (Speak for 30 seconds about a song you like.)')),
    dict(n=2, titulo='Count on Me -- Bruno Mars',
         url='https://www.youtube.com/watch?v=6k8cpUkKK4c',
         desc='Vídeo com a letra na tela. Tema: amizade. A frase do refrão serve no trabalho também.',
         quiz=[('No refrão, o cantor diz "you can count on ___". Qual é a palavra? (Which word?)',
                [('me', True), ('them', False), ('us', False)]),
               ('No trabalho, "count on me" quer dizer: (What does it mean at work?)',
                [('Pode contar comigo.', True), ('Conte os números.', False), ('Me ligue amanhã.', False)])],
         fala=[('You can count on me.', 'Pode contar comigo.'),
               ('I can help you with this.', 'Posso te ajudar com isso.'),
               ('We work together every week.', 'Trabalhamos juntas toda semana.')],
         think=('Fale por 30 segundos sobre uma pessoa do seu time com quem você pode contar. '
                'Use "I can count on..." e diga o que essa pessoa faz. (Talk about someone you can count on.)')),
    dict(n=3, titulo='Hello -- Adele',
         url='https://www.youtube.com/watch?v=YQHsXMglC9A',
         desc='Uma ligação telefônica cantada. Treina o ouvido para o começo de uma conversa ao telefone.',
         quiz=[('A primeira palavra da música é: (The first word is:)',
                [('Hello', True), ('Sorry', False), ('Listen', False)]),
               ('"Hello, it\'s me" quer dizer: (It means:)',
                [('Alô, sou eu.', True), ('Alô, é você?', False), ('Alô, quem fala?', False)])],
         fala=[('Hello, this is Joice speaking.', 'Alô, aqui é a Joice.'),
               ('Can you hear me?', 'Você consegue me ouvir?'),
               ('Sorry, can you say it again, please?', 'Desculpe, pode dizer de novo, por favor?')],
         think=('Grave o primeiro minuto de uma ligação: diga alô, diga seu nome, diga de onde você fala '
                'e pergunte se a pessoa tem tempo agora. (Record the first minute of a phone call.)')),
    dict(n=4, titulo='Perfect -- Ed Sheeran',
         url='https://www.youtube.com/watch?v=2Vv-BfVoq4g',
         desc='Frases simples e pronúncia bem clara. Ative a legenda em inglês (CC) e acompanhe cantando baixinho.',
         quiz=[('O cantor fala de qual momento? (He sings about:)',
                [('Uma dança com a pessoa amada.', True), ('Uma reunião de trabalho.', False), ('Uma viagem de avião.', False)]),
               ('"Perfect" em português é: (In Portuguese:)',
                [('perfeito', True), ('primeiro', False), ('possível', False)])],
         fala=[('I like this song very much.', 'Gosto muito desta música.'),
               ('I listen to music every morning.', 'Ouço música toda manhã.'),
               ('This singer speaks very clearly.', 'Este cantor fala muito claramente.')],
         think=('Fale por 30 segundos: em que momento do dia você ouve música? De manhã, no carro, no trabalho? '
                'Use "I usually listen to music..." (When do you listen to music?)')),
    dict(n=5, titulo='Let It Be -- The Beatles',
         url='https://www.youtube.com/watch?v=QDYfEBY9NM4',
         desc='Clássico, devagar e com muita repetição, e repetição é o que faz a frase grudar.',
         quiz=[('"Let it be" é um conselho. Em português, fica perto de: (In Portuguese:)',
                [('Deixa como está.', True), ('Deixe aqui.', False), ('Vamos embora.', False)]),
               ('A palavra "words" aparece no refrão. Ela significa: (What does "words" mean?)',
                [('palavras', True), ('mundos', False), ('trabalhos', False)])],
         fala=[('There is an answer. Let it be.', 'Existe uma resposta. Deixa como está.'),
               ('I do not have all the answers today.', 'Não tenho todas as respostas hoje.'),
               ('It is OK to take my time.', 'Tudo bem eu ir no meu tempo.')],
         think=('Fale por 30 segundos sobre uma coisa do trabalho que você não precisa resolver hoje. '
                'Comece com "I do not need to..." (Talk about something that can wait.)')),
]


def render_musicas():
    cards = []
    for m in MUSICAS:
        blocos = [
            secao('Ouça a música', 'Media', 'badge-media',
                  'Abra o vídeo, ative a legenda em inglês (CC) e ouça uma vez inteira, sem parar. '
                  'Depois ouça de novo lendo a legenda.',
                  video(m['url'], 'Abrir no YouTube')),
            secao('O que você ouviu', 'Quiz', 'badge-quiz',
                  'Responda depois de ouvir duas vezes. Errar aqui faz parte do treino do ouvido.',
                  quiz(m['quiz'])),
            secao('Say it out loud', 'Speaking', 'badge-speak',
                  'Toque em Ouvir, repita em voz alta e depois grave. A nota por palavra aparece na hora.',
                  speech(m['fala'])),
            secao('Sua vez de falar', 'Reflection', 'badge-think',
                  'Não existe resposta certa. Grave, ouça a sua voz e, se quiser, grave de novo.',
                  think('think-result-mu%d' % m['n'], m['think'])),
        ]
        cards.append(card('mu-song-%d' % m['n'], IMG['musica'], 'Música %02d' % m['n'],
                          m['titulo'], m['desc'], blocos))
    return ('  <p style="%s">Música é o jeito mais leve de acostumar o ouvido, e foi o que você pediu na '
            'nossa conversa. São cinco músicas, da mais lenta para a mais rápida. Não precisa entender tudo: '
            'entender algumas palavras já é progresso.</p>\n  %s\n\n%s'
            % (INTRO, painel_aba('music', 'Músicas'), '\n\n'.join(cards)))


# ============================================================== ABA EXPRESSIONS
GRUPOS = [
    dict(n=1, titulo='Na reunião', img=IMG['reuniao'],
         desc='As quatro frases que resolvem a maior parte de uma reunião curta em inglês.',
         vocab=[('Sounds good.', 'combinado, parece bom', 'Sounds good. Thank you.', 'Combinado. Obrigada.'),
                ('That works for me.', 'para mim funciona', 'Friday? That works for me.', 'Sexta? Para mim funciona.'),
                ('Let me check.', 'deixa eu conferir', 'Let me check and send it to you.', 'Deixa eu conferir e te envio.'),
                ('Go ahead.', 'pode falar, pode seguir', 'Go ahead, I am listening.', 'Pode falar, estou ouvindo.')],
         pares=[('Sounds good.', 'combinado, parece bom'), ('That works for me.', 'para mim funciona'),
                ('Let me check.', 'deixa eu conferir'), ('Go ahead.', 'pode falar, pode seguir')],
         fill=[('"Friday at nine? That ', 'works', ' for me."', 'Dica: a frase é "that works for me"',
                'Friday at nine? That works for me.'),
               ('"', 'Sounds', ' good. Thank you."', 'Dica: começa com S e quer dizer "parece"',
                'Sounds good. Thank you.')],
         fala=[('Sounds good. Thank you.', 'Combinado. Obrigada.'),
               ('That works for me.', 'Para mim funciona.'),
               ('Let me check and send it to you.', 'Deixa eu conferir e te envio.')],
         think=('Grave 30 segundos: alguém sugere uma reunião na quinta às 10h. Aceite, diga que vai conferir '
                'uma informação e diga quando envia. (Someone suggests a meeting on Thursday at ten.)')),
    dict(n=2, titulo='Quando você não sabe', img=IMG['reuniao'],
         desc='Não saber um número ou uma palavra é normal. O que muda tudo é ter a frase pronta.',
         vocab=[('I am not sure.', 'não tenho certeza', 'I am not sure about this number.', 'Não tenho certeza sobre este número.'),
                ('I can send it tomorrow.', 'posso enviar amanhã', 'I can send it tomorrow morning.', 'Posso enviar amanhã de manhã.'),
                ('Slowly, please.', 'devagar, por favor', 'Slowly, please. Thank you.', 'Devagar, por favor. Obrigada.'),
                ('What does it mean?', 'o que isso quer dizer?', 'What does "deadline" mean?', 'O que "deadline" quer dizer?')],
         pares=[('I am not sure.', 'não tenho certeza'), ('I can send it tomorrow.', 'posso enviar amanhã'),
                ('Slowly, please.', 'devagar, por favor'), ('What does it mean?', 'o que isso quer dizer?')],
         fill=[('"I am not ', 'sure', ' about this number."', 'Dica: "certeza" em inglês, começa com S',
                'I am not sure about this number.'),
               ('"', 'Slowly', ', please. Thank you."', 'Dica: vem de "slow", que quer dizer "lento"',
                'Slowly, please. Thank you.')],
         fala=[('I am not sure about this number.', 'Não tenho certeza sobre este número.'),
               ('Can you say that again, slowly, please?', 'Você pode dizer de novo, devagar, por favor?'),
               ('What does this word mean?', 'O que esta palavra quer dizer?')],
         think=('Grave 30 segundos: alguém pergunta quantas escolas participam este ano e você não tem o número '
                'exato. Responda mesmo assim. (Someone asks for a number you do not have.)')),
    dict(n=3, titulo='Small talk', img=IMG['reuniao'],
         desc='Os dois minutos antes de a reunião começar. É aqui que a conversa esquenta.',
         vocab=[('How is your week?', 'como está a sua semana?', 'Hi, Ruth. How is your week?', 'Oi, Ruth. Como está a sua semana?'),
                ('Busy', 'cheio, corrido', 'My week is very busy.', 'Minha semana está muito corrida.'),
                ('I could use a coffee.', 'eu bem que queria um café', 'It is Monday. I could use a coffee.', 'É segunda. Eu bem que queria um café.'),
                ('Have a good weekend.', 'bom fim de semana', 'See you on Monday. Have a good weekend.', 'Até segunda. Bom fim de semana.')],
         pares=[('How is your week?', 'como está a sua semana?'), ('Busy', 'cheio, corrido'),
                ('I could use a coffee.', 'eu bem que queria um café'), ('Have a good weekend.', 'bom fim de semana')],
         fill=[('"My week is very ', 'busy', ', but it is good."', 'Dica: "corrida", começa com B',
                'My week is very busy, but it is good.'),
               ('"Have a good ', 'weekend', '."', 'Dica: sábado e domingo, numa palavra só',
                'Have a good weekend.')],
         fala=[('Hi. How is your week?', 'Oi. Como está a sua semana?'),
               ('My week is busy, but it is good.', 'Minha semana está corrida, mas está boa.'),
               ('Have a good weekend.', 'Bom fim de semana.')],
         think=('Grave 30 segundos de small talk: cumprimente, diga como está a sua semana e faça uma pergunta '
                'de volta. (Thirty seconds of small talk.)')),
    dict(n=4, titulo='Pedir e oferecer', img=IMG['reuniao'],
         desc='Pedir ajuda em inglês não é sinal de fraqueza. É o que mantém a conversa viva.',
         vocab=[('Can I ask a question?', 'posso fazer uma pergunta?', 'Can I ask a question about the report?', 'Posso fazer uma pergunta sobre o relatório?'),
                ('Would you like some coffee?', 'você gostaria de um café?', 'Would you like some coffee before we start?', 'Você gostaria de um café antes de começarmos?'),
                ('Let me know.', 'me avise', 'Let me know, please.', 'Me avise, por favor.'),
                ('Thank you for your help.', 'obrigada pela ajuda', 'Thank you for your help today.', 'Obrigada pela ajuda hoje.')],
         pares=[('Can I ask a question?', 'posso fazer uma pergunta?'),
                ('Would you like some coffee?', 'você gostaria de um café?'),
                ('Let me know.', 'me avise'), ('Thank you for your help.', 'obrigada pela ajuda')],
         fill=[('"Can I ', 'ask', ' a question about the report?"', 'Dica: o verbo "perguntar"',
                'Can I ask a question about the report?'),
               ('"Thank you for your ', 'help', ' today."', 'Dica: "ajuda", começa com H',
                'Thank you for your help today.')],
         fala=[('Can I ask a question about the report?', 'Posso fazer uma pergunta sobre o relatório?'),
               ('Would you like some coffee before we start?', 'Você gostaria de um café antes de começarmos?'),
               ('Thank you for your help today.', 'Obrigada pela ajuda hoje.')],
         think=('Grave 30 segundos: peça ajuda para entender uma palavra e agradeça no final. '
                '(Ask for help with a word, then say thank you.)')),
]


def render_expressions():
    cards = []
    for g in GRUPOS:
        blocos = [
            secao('As frases', 'Vocabulary', 'badge-vocab',
                  'Toque em Listen e repita em voz alta. Ouça quantas vezes quiser.',
                  vocab_cards(g['vocab'])),
            secao('Ligue a frase ao sentido', 'Practice', 'badge-practice',
                  'Escolha a tradução de cada frase e clique em Conferir.',
                  matching('match-ev%d' % g['n'], g['pares'], 700 + g['n'])),
            secao('Complete', 'Practice', 'badge-practice',
                  'Escreva a palavra que falta. Toque em Listen para ouvir a frase inteira antes.',
                  fill_in(g['fill'])),
            secao('Say it out loud', 'Speaking', 'badge-speak',
                  'Ouça, repita e grave. O objetivo não é acertar tudo: é a sua boca se acostumar.',
                  speech(g['fala'])),
            secao('Sua vez de falar', 'Reflection', 'badge-think',
                  'Sem correção e sem resposta certa.',
                  think('think-result-ev%d' % g['n'], g['think'])),
        ]
        cards.append(card('ev-group-%d' % g['n'], g['img'], 'Bloco %02d' % g['n'],
                          g['titulo'], g['desc'], blocos))
    return ('  <p style="%s">Expressões prontas do dia a dia e de reunião, do jeito que as pessoas falam de '
            'verdade. Cada frase tem áudio, tradução e um lugar para você gravar a sua voz.</p>\n  %s\n\n%s'
            % (INTRO, painel_aba('expressions', 'Expressões do dia a dia'), '\n\n'.join(cards)))


# ================================================================ ABA SEU TRABALHO
BLOCOS_FIELD = [
    dict(n=1, titulo='Formação de professores', img=IMG['escola'],
         desc='Falar do seu trabalho com formação: quem participa, quanto tempo leva, o que muda.',
         vocab=[('Teacher training', 'formação de professores', 'I work with teacher training.', 'Trabalho com formação de professores.'),
                ('Classroom', 'sala de aula', 'The teacher uses the tool in the classroom.', 'O professor usa a ferramenta na sala de aula.'),
                ('Tool', 'ferramenta', 'This tool is easy to learn.', 'Esta ferramenta é fácil de aprender.'),
                ('To learn', 'aprender', 'Teachers learn fast when they practice.', 'Professores aprendem rápido quando praticam.')],
         fala=[('I work with teacher training in public schools.', 'Trabalho com formação de professores em escolas públicas.'),
               ('Teachers need about thirty minutes to learn the platform.', 'Os professores precisam de uns trinta minutos para aprender a plataforma.'),
               ('I like working with teachers.', 'Gosto de trabalhar com professores.')],
         think=('Grave 1 minuto: explique o que você faz na formação de professores. Diga quantas pessoas '
                'participam e quanto tempo dura. (Explain your work in teacher training.)')),
    dict(n=2, titulo='Escolas públicas', img=IMG['escola'],
         desc='O contexto que só você tem: rede pública, escolas grandes e escolas pequenas.',
         vocab=[('Public school', 'escola pública', 'I work with public schools.', 'Trabalho com escolas públicas.'),
                ('Principal', 'diretor ou diretora de escola', 'The principal asks about the training.', 'A diretora da escola pergunta sobre a formação.'),
                ('State', 'estado', 'The program is in six states.', 'O programa está em seis estados.'),
                ('Student', 'aluno, aluna', 'Students use the platform at home too.', 'Os alunos usam a plataforma em casa também.')],
         fala=[('I work with public schools in São Paulo.', 'Trabalho com escolas públicas em São Paulo.'),
               ('The program is in six states.', 'O programa está em seis estados.'),
               ('Small schools need more help than big schools.', 'Escolas pequenas precisam de mais ajuda que escolas grandes.')],
         think=('Grave 1 minuto: fale sobre as escolas com quem você trabalha. Quantas são, onde ficam e '
                'do que elas precisam. (Talk about the schools you work with.)')),
    dict(n=3, titulo='Dados e resultados', img=IMG['reuniao'],
         desc='As palavras da reunião em que você apresenta números, que é onde você mais usa inglês.',
         vocab=[('Budget', 'orçamento', 'The budget for the training is small.', 'O orçamento da formação é pequeno.'),
                ('Result', 'resultado', 'The results are good this year.', 'Os resultados estão bons este ano.'),
                ('To show', 'mostrar', 'The numbers show a big change.', 'Os números mostram uma grande mudança.'),
                ('Chart', 'gráfico', 'This chart shows the results.', 'Este gráfico mostra os resultados.')],
         fala=[('The results are good this year.', 'Os resultados estão bons este ano.'),
               ('We have some results, but not enough.', 'Temos alguns resultados, mas não o suficiente.'),
               ('I can show you the chart.', 'Posso te mostrar o gráfico.')],
         think=('Grave 1 minuto apresentando os números do seu programa, como se fosse o começo de uma reunião. '
                '(Present the numbers of your program.)')),
    dict(n=4, titulo='Tecnologia e IA na educação', img=IMG['escola'],
         desc='O assunto que você domina em português e ainda não tem em inglês.',
         vocab=[('App', 'aplicativo', 'Teachers use the app on the phone.', 'Os professores usam o aplicativo no celular.'),
                ('Device', 'aparelho, dispositivo', 'Some schools do not have enough devices.', 'Algumas escolas não têm aparelhos suficientes.'),
                ('Online', 'on-line, pela internet', 'The training is online.', 'A formação é on-line.'),
                ('Safe', 'seguro, protegido', 'We keep data about students safe.', 'Mantemos os dados dos alunos protegidos.')],
         fala=[('The training is online, and it is short.', 'A formação é on-line e é curta.'),
               ('Some schools do not have enough devices.', 'Algumas escolas não têm aparelhos suficientes.'),
               ('We keep data about students safe.', 'Mantemos os dados dos alunos protegidos.')],
         think=('Grave 1 minuto: o que a tecnologia muda na sala de aula? Diga uma coisa boa e uma '
                'preocupação. (What does technology change in the classroom?)')),
]


def render_field():
    cards = []
    for b in BLOCOS_FIELD:
        blocos = [
            secao('As palavras do seu trabalho', 'Vocabulary', 'badge-vocab',
                  'Toque em Listen e repita. São palavras que você já usa em português todo dia.',
                  vocab_cards(b['vocab'])),
            secao('Say it out loud', 'Speaking', 'badge-speak',
                  'Frases inteiras, prontas para usar numa reunião. Ouça, repita e grave.',
                  speech(b['fala'])),
            secao('Um minuto seu', 'Reflection', 'badge-think',
                  'Um minuto falando sozinha, sem parar. Número aproximado também é número.',
                  think('think-result-fd%d' % b['n'], b['think'])),
        ]
        cards.append(card('fd-block-%d' % b['n'], b['img'], 'Bloco %02d' % b['n'],
                          b['titulo'], b['desc'], blocos))
    return ('  <p style="%s">O inglês do que você faz: formação de professores, escolas públicas, dados e '
            'tecnologia na educação. Aqui não tem tema genérico, só o seu.</p>\n  %s\n\n%s'
            % (INTRO, painel_aba('field', 'O inglês do seu trabalho'), '\n\n'.join(cards)))


# ==================================================================== ABA TEDX
PASSOS = [
    dict(n=1, titulo='Os primeiros trinta segundos',
         desc='Como você entra no palco: nome, de onde vem e o que faz. Nada mais.',
         fala=[('Good evening. My name is Joice Lopes Leite.', 'Boa noite. Meu nome é Joice Lopes Leite.'),
               ('I am from Brazil, and I work in education.', 'Sou do Brasil e trabalho com educação.'),
               ('Thank you for the invitation.', 'Obrigada pelo convite.')],
         think=('Grave 1 minuto: a sua abertura. Nome, país, trabalho e uma frase sobre por que esse assunto '
                'importa para você. (Record your opening.)')),
    dict(n=2, titulo='Dizer do que você vai falar',
         desc='A frase que organiza a plateia, e organiza você também.',
         fala=[('Today I want to talk about teachers.', 'Hoje quero falar sobre professores.'),
               ('I have three things to show you.', 'Tenho três coisas para mostrar a vocês.'),
               ('First, the numbers. Then, one story.', 'Primeiro, os números. Depois, uma história.')],
         think=('Grave 1 minuto: diga em três partes o que você vai apresentar em novembro. '
                'Use "First... Then... Finally..." (Say the three parts of your talk.)')),
    dict(n=3, titulo='Passar de uma parte para outra',
         desc='As pontes. São frases curtas, e só elas já sustentam uma apresentação.',
         fala=[('Now, the numbers.', 'Agora, os números.'),
               ('Let me give you an example.', 'Deixa eu dar um exemplo.'),
               ('This is the important part.', 'Esta é a parte importante.')],
         think=('Grave 1 minuto usando as três pontes: os números, um exemplo e a parte importante. '
                '(Use the three bridges in one minute.)')),
    dict(n=4, titulo='Responder à plateia',
         desc='A parte que mais assusta, e a que tem as frases mais fáceis.',
         fala=[('That is a good question.', 'Essa é uma boa pergunta.'),
               ('I do not have the exact number, but I can send it.', 'Não tenho o número exato, mas posso enviar.'),
               ('Can you repeat the question, please?', 'Você pode repetir a pergunta, por favor?')],
         think=('Grave 1 minuto: alguém da plateia pergunta quantos professores participam do programa. '
                'Responda, mesmo sem o número exato. (Answer a question from the audience.)')),
]


def render_tedx():
    cards = []
    for p in PASSOS:
        blocos = [
            secao('As frases do palco', 'Speaking', 'badge-speak',
                  'Ouça, repita e grave. Depois ouça a sua gravação: é assim que você vai soar em novembro.',
                  speech(p['fala'])),
            secao('Um minuto seu', 'Reflection', 'badge-think',
                  'Grave, ouça e grave de novo. Você tem até novembro, e cada gravação fica salva aqui.',
                  think('think-result-tx%d' % p['n'], p['think'])),
        ]
        cards.append(card('tx-step-%d' % p['n'], IMG['palco'], 'Passo %02d' % p['n'],
                          p['titulo'], p['desc'], blocos))
    return ('  <p style="%s">Novembro, Belém, inglês no palco. São quatro passos, cada um com as frases prontas '
            'e um minuto de gravação. Dá para repetir quantas vezes quiser até sair natural.</p>\n  %s\n\n%s'
            % (INTRO, painel_aba('stage', 'TEDx Belém'), '\n\n'.join(cards)))


# ============================================================== CHECAGENS/MAIN
ABAS = [('music', 'musica.html', render_musicas, 'Músicas'),
        ('expressions', 'expressions.html', render_expressions, 'Expressões do dia a dia'),
        ('field', 'field.html', render_field, 'O inglês do seu trabalho'),
        ('stage', 'tedx.html', render_tedx, 'TEDx Belém')]

H3 = "font-family:'Cormorant Garamond',serif;font-size:1.2rem;margin-bottom:1rem"


def envelope(n, slot, titulo, corpo):
    """O CONTEINER DA ABA vem do snippet, nao do inseridor.

    O insert_hub_extras.py so pendura o botao e cola o snippet depois do ultimo
    `</div><!-- /tab-... -->`. Sem este envelope o conteudo entra SOLTO no fim
    da pagina (sempre visivel, fora de qualquer aba) e a aba seguinte e colada
    ANTES da anterior, porque o ultimo fecho continua sendo o dos Complementares.
    """
    return ('<!-- ========== TAB %d: %s (aditivo, 15/09/2026) ========== -->\n'
            '<div class="tab-content" id="tab-%s">\n'
            '<h3 style="%s">%s</h3>\n%s\n'
            '</div><!-- /tab-%s -->' % (n, slot.upper(), slot, H3, titulo, corpo, slot))

RESERVADOS = ['ex-lesson-', 'id="stamp', 'data-slide', 'data-lesson-progress', 'data-lesson-pct']


def colisoes(snippets):
    """A trava do loadState: ele restaura por CONTEUDO, no documento inteiro.

    Resposta de fill-in, palavra de matching, primeiros 30 caracteres da opcao
    certa do quiz e data-phrase do speech card que ja existam no hub fariam um
    acerto aqui marcar exercicio das aulas 1..20 -- e inflar o progresso dela.
    """
    hub = ''
    for h in HUBS:
        hub += open(h, encoding='utf-8').read()
    novo = '\n'.join(snippets)
    erros = []

    def achados(padrao, texto):
        return set(re.findall(padrao, texto))

    for rotulo, padrao in [('fill-in (data-answer)', r'class="blank-input" data-answer="([^"]+)"'),
                           ('matching (data-answer)', r'class="match-row" data-answer="([^"]+)"'),
                           ('speech (data-phrase)', r'class="speech-card" data-phrase="([^"]+)"')]:
        dupla = achados(padrao, novo) & achados(padrao, hub)
        for d in sorted(dupla):
            erros.append('%s: "%s" ja existe no hub' % (rotulo, d))

    quiz_novo = {t[:30] for t in re.findall(r'data-correct="true"><span class="option-letter">[A-D]</span> ([^<]+)', novo)}
    quiz_hub = {t[:30] for t in re.findall(r'data-correct="true"><span class="option-letter">[A-D]</span> ([^<]+)', hub)}
    for d in sorted(quiz_novo & quiz_hub):
        erros.append('quiz (30 primeiros caracteres): "%s" ja existe no hub' % d)

    ids_novos = re.findall(r'id="([^"]+)"', novo)
    for i in ids_novos:
        if ids_novos.count(i) > 1:
            erros.append('id repetido no proprio snippet: %s' % i)
        if 'id="%s"' % i in hub:
            erros.append('id "%s" ja existe no hub' % i)
    for r in RESERVADOS:
        if r in novo:
            erros.append('marcacao reservada do Pre-class usada no snippet: %s' % r)
    return erros


def main():
    snippets = []
    for n, (slot, arquivo, render, titulo) in enumerate(ABAS, 3):
        corpo = envelope(n, slot, titulo, render())
        caminho = os.path.join(AQUI, arquivo)
        open(caminho, 'w', encoding='utf-8').write(corpo + '\n')
        snippets.append(corpo)
        print('  escrito %s (%d KB)' % (arquivo, len(corpo) // 1024))
    erros = colisoes(snippets)
    if erros:
        print('\nCOLISAO -- nao insira assim:')
        for e in erros:
            print('  X ' + e)
        sys.exit(1)
    print('\nsem colisao com o hub (fill-in, matching, quiz, speech, ids) e sem marcacao reservada.')


if __name__ == '__main__':
    main()
