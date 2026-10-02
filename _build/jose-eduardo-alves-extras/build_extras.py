#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Abas "Post-class" e "From Your Class" do Jose Eduardo Alves, 02/10/2026.

POR QUE EXISTE. O aluno pediu mais exercicio de fixacao depois da aula: os Extras
dele sao series, palestras e podcasts para assistir, nada para praticar. A Helen
pediu duas abas:
  1. POST-CLASS: o terceiro pilar da aula. Pre-class prepara, a aula com a
     professora ensina, o post-class poe em pratica com situacoes NOVAS. Um bloco
     por aula (1 a 10), e toda aula nova que for gerada para ele ganha o seu.
  2. FROM YOUR CLASS: exercicios montados das analises de aula (Zoom) dele. As
     frases que ele disse em aula, os sons que a professora corrigiu e as palavras
     que ele perguntou. Um bloco por aula dada; cresce depois de cada aula.

REGRAS QUE ESTE ARQUIVO SEGUE
- Teto de nivel: o post-class da aula N so usa a gramatica das aulas 1..N; o bloco
  de uma aula dada so usa a gramatica ja vista ate aquela data.
- Nao repete item de tarefa do pre-class nem da aula (vocabulario pode repetir).
- Listening = recado de voz de uma pessoa do elenco dele, uma voz so, com resposta
  LITERAL no audio (feedback da teacher Malu em 21/09/2026).
- Resposta certa sorteada, nunca na mesma posicao em sequencia.
- Ids proprios `po-` e `fc-`, fora do updateProgress (barra e stamps nao mudam).
- A aba e `tab-afterclass`, NUNCA `tab-postclass`: esse id e o percurso do modelo Kids
  (REGRA 33) e o validate_lesson cobra window.PV_POSTS de quem o tiver.
- So chama funcao que o hub ja tem. O insert_hub_extras recusa qualquer outra.
- Nenhuma resposta, opcao certa, frase de pronuncia ou pergunta livre pode colidir
  com o resto do hub (loadState restaura por texto): ver checa_colisoes().

USO:  python3 build_extras.py      (escreve postclass.html e fromclass.html ao lado
                                    e confere colisao contra o hub do aluno)

COMO CRESCE (decisao da Helen, 02/10/2026: "as proximas aulas que forem geradas precisam
seguir o mesmo padrao")
- AULA NOVA GERADA (11, 12...): no mesmo PR da aula, acrescentar a entrada dela em POST
  (mesmos 6 stages, gramatica da aula nova como teto, elenco fixo dele), e entao:
      python3 build_extras.py
      python3 ../model/insert_hub_extras.py --replace --hub public/{aluno,professor}/jose-eduardo-alves.html \
          --aba afterclass:_build/jose-eduardo-alves-extras/postclass.html:"Post-class" \
          --aba fromclass:_build/jose-eduardo-alves-extras/fromclass.html:"From Your Class"
      ELEVENLABS_API_KEY=... python3 gen_audio_extras.py
  e ampliar FOTO com a imagem de cabecalho da aula nova.
- AULA DADA E ANALISADA: acrescentar a entrada em CLASSES a partir de
  /api/analise?id=<id> (lista em /api/analises, filtro aluno_id) e rodar o mesmo trio.
  Aula com falha de audio/transcricao (ex.: analise 1504, 17/09) nao vira bloco.
"""
import os
import random
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, '..', '..'))
HUB = os.path.join(RAIZ, 'public', 'aluno', 'jose-eduardo-alves.html')
IMG = 'https://images.unsplash.com/photo-'
FOTO = {1: '1521737711867-e3b97375f902', 2: '1450101499163-c8848c66ca85',
        3: '1506784983877-45594efa4cbe', 4: '1423592707957-3b212afa6733',
        5: '1434030216411-0b793f4b4173', 6: '1494412574643-ff11b0a5c1c3',
        7: '1444723121867-7a241cacace9', 8: '1519003722824-194d4455a60c',
        9: '1450101499163-c8848c66ca85', 10: '1524995997946-a1c2e315a42f'}


def esc(t):
    return (t.replace('&', '&amp;').replace('"', '&quot;')
             .replace('<', '&lt;').replace('>', '&gt;'))


class Sorteio:
    """Posicao da resposta certa: equilibrada e nunca igual a anterior."""

    def __init__(self, semente):
        self.rnd = random.Random(semente)
        self.ultima = None
        self.saco = []

    def proxima(self, n):
        if not self.saco:
            self.saco = list(range(n)) * 2
            self.rnd.shuffle(self.saco)
        for i, p in enumerate(self.saco):
            if p != self.ultima and p < n:
                self.ultima = self.saco.pop(i)
                return self.ultima
        self.saco = []
        return self.proxima(n)


def quiz(items, sorteio):
    out = ''
    for q, certa, erradas in items:
        pos = sorteio.proxima(len(erradas) + 1)
        opts = list(erradas)
        opts.insert(pos, certa)
        o = ''.join(
            f'<div class="quiz-option" onclick="selectQuiz(this)" data-correct="{str(j == pos).lower()}">'
            f'<span class="option-letter">{"ABCDE"[j]}</span> {t}</div>'
            for j, t in enumerate(opts))
        out += (f'      <div class="quiz-item"><div class="quiz-question">{q}</div>'
                f'<div class="quiz-options">{o}</div></div>\n')
    return out


def blanks(items):
    """(antes, resposta, depois, dica[, alternativa])"""
    out = ''
    for it in items:
        antes, resp, depois, dica = it[:4]
        alt = it[4] if len(it) > 4 else None
        frase = f'{antes}{resp}{depois}'
        alt_attr = f' data-alt="{esc(alt)}"' if alt else ''
        out += (f'      <div class="fill-blank-item"><div class="fill-blank-sentence">&quot;{esc(antes)}'
                f'<input class="blank-input" data-answer="{esc(resp)}"{alt_attr} data-hint="{esc(dica)}" '
                f'data-phrase="{esc(frase)}" placeholder="___">{esc(depois)}&quot;</div>'
                f'<button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>'
                f'<button class="check-btn" onclick="checkBlank(this)">Check</button></div>\n')
    return out


def matching(gid, pares, giro=2):
    defs = [d for _, d in pares]
    k = giro % len(defs) or 1
    opcoes = defs[k:] + defs[:k]
    rows = ''
    for w, d in pares:
        o = ''.join(f'<option value="{esc(x)}">{esc(x)}</option>' for x in opcoes)
        rows += (f'        <div class="match-row" data-answer="{esc(d)}">'
                 f'<span class="match-word" style="flex:0 0 170px">{w}</span>'
                 f'<select style="flex:1;width:100%" onchange="checkMatch(this)">'
                 f'<option value="">Select...</option>{o}</select></div>\n')
    return (f'      <div class="match-grid" id="{gid}">\n{rows}      </div>\n'
            f'      <button class="verify-all-btn" onclick="verifyAllMatches(\'{gid}\')">Check Answers</button>\n')


def speech(frases):
    out = ''
    for f in frases:
        out += (f'      <div class="speech-card" data-phrase="{esc(f)}">\n'
                f'        <div class="speech-phrase">{esc(f)}</div>\n'
                f'        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button>'
                f'<button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button>'
                f'<button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Stop</button></div>\n'
                f'        <div class="speech-result"></div>\n'
                f'      </div>\n')
    return out


def think(rid, pergunta):
    return (f'      <div class="think-card">\n'
            f'        <div class="think-question">{esc(pergunta)}</div>\n'
            f'        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Free Record</button>'
            f'<button class="btn btn-stop" onclick="stopFreeRecording(this)">&#9632; Stop</button></div>\n'
            f'        <div id="{rid}"></div>\n'
            f'      </div>\n')


def mensagem(texto, voz, quem):
    return (f'      <div style="background:var(--bg-card);border:1px solid var(--border);border-left:3px solid var(--accent);'
            f'border-radius:8px;padding:1rem;margin-bottom:1rem">'
            f'<p style="font-size:.88rem;margin-bottom:.6rem">A voice message from <strong>{quem}</strong>. '
            f'Listen first. Every answer is in the message.</p>'
            f'<button class="audio-btn" data-speak="{esc(texto)}" data-voice="{voz}" '
            f'onclick="speakText(this.dataset.speak,this)">&#9654; Listen to the message</button>'
            f'<details style="margin-top:.8rem"><summary style="cursor:pointer;font-size:.82rem;color:var(--text-dim)">'
            f'Read the message (after you answer)</summary>'
            f'<p style="font-size:.88rem;line-height:1.7;margin-top:.5rem">{esc(texto)}</p></details></div>\n')


def secao(titulo, badge_cls, badge, lead, corpo):
    return (f'    <div class="exercise-section">\n'
            f'      <div class="section-header-row"><h4>{titulo}</h4>'
            f'<span class="badge {badge_cls}">{badge}</span></div>\n'
            f'      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">{lead}</p>\n'
            f'{corpo}    </div>\n')


def card(cid, rotulo, titulo, desc, img, corpo):
    return f'''<div class="lesson-card" id="{cid}">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('{IMG}{img}?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">{rotulo}</div>
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


def aba(slot, titulo, intro, cards):
    return (f'<!-- ========== ABA SUPLEMENTAR: {titulo} (aditiva, fora do progresso) ========== -->\n'
            f'<div class="tab-content" id="tab-{slot}">\n'
            f'<div style="margin-bottom:1.2rem"><h2 style="font-size:1.25rem;margin-bottom:.4rem">{titulo}</h2>'
            f'<p style="font-size:.9rem;color:var(--text-dim);line-height:1.6">{intro}</p></div>\n'
            + ''.join(cards) +
            f'</div><!-- /tab-{slot} -->\n')


# ════════════════════════════════════════════════════════════════════════════
# POST-CLASS: uma licao por aula. Mesma gramatica, situacao nova.
# ════════════════════════════════════════════════════════════════════════════
# Cada licao: titulo, desc, gramatica (lead do stage 1), stage1 blanks,
# recado (texto, voz, quem), perguntas do recado, situacional, e-mail (para quem,
# blanks), frases de pronuncia, pergunta livre.
POST = [
    dict(n=1, titulo='The Person in the Room', desc='Present simple with I, you and we, at a dinner for speakers in Chicago.',
         s1_lead='Complete with the verb. Two answers are negative and one is a question: the hint tells you which.',
         s1=[('My partners and I ', 'work with', ' three trading companies in Goiás.',
              'Hint: work + with. We work WITH these companies every day.'),
             ('We ', 'do not travel', ' to Europe every month. We meet the traders online.',
              'Hint: NEGATIVE of travel. We + do not + verb.', "don't travel"),
             ('', 'Do you import', ' corn or soybeans?',
              'Hint: QUESTION with import. Do + you + verb.'),
             ('I ', 'check the deadline', ' first, and then I read the clauses.',
              'Hint: check + the deadline. With I, no -s.'),
             ('We ', 'do not work', ' for banks. We work for the traders.',
              'Hint: NEGATIVE of work. We + do not + verb.', "don't work")],
         msg=("Hello, Eduardo. This is Nora Vieira from the Agri Law conference in Chicago. "
              "We have a dinner for speakers on Tuesday, at eight o'clock, at the Lake Hotel. "
              "You sit at table six, with three grain traders from Ohio. They import fertilizer from Brazil, "
              "and they want to meet a Brazilian lawyer. Please bring twenty business cards. "
              "We start at eight and we finish at ten. You do not need a jacket. My number is 312 555 0147."),
         voz='ellen', quem='Nora Vieira, Agri Law conference',
         msg_q=[('When is the dinner?', "On Tuesday, at eight o'clock",
                 ["On Thursday, at eight o'clock", "On Tuesday, at ten o'clock"]),
                ('Who sits at table six with Eduardo?', 'Three grain traders from Ohio',
                 ['Three lawyers from Chicago', 'Two grain traders from Iowa']),
                ('What does Eduardo need to bring?', 'Twenty business cards',
                 ['A jacket and a tie', 'Two photos and his passport'])],
         sit=[('At the dinner, a trader asks: "What do you do?" You say:',
               '"I\'m a partner in a law firm. We advise grain traders."',
               ['"I am advise grain traders in a law firm."', '"My lawyer, and I advise grain traders."']),
              ('A trader asks: "Do you go to court a lot?" You answer:',
               '"No, we don\'t. Most of our work is on paper."',
               ['"No, we not go. Our work is on paper."', '"No, I don\'t go to court never."']),
              ('You want to know where he buys his soybeans. You ask:',
               '"Where do you buy your soybeans?"',
               ['"Where you buy your soybeans?"', '"Where does you buy your soybeans?"'])],
         mail_to='Nora',
         mail=[('Thank you, Nora. I ', 'accept the invitation', ' for Tuesday.',
                'Hint: accept + the invitation. With I, no -s.'),
               ('I ', 'work every day with', ' grain traders, so table six is perfect for me.',
                'Hint: work + every day + with.'),
               ('I ', 'do not eat', ' meat. Is there a fish option?',
                'Hint: NEGATIVE of eat. I + do not + verb.', "don't eat"),
               ('', 'Do you have', ' a list of the people at table six?',
                'Hint: QUESTION with have. Do + you + verb.')],
         fala=["I'm a partner, and we advise grain traders and their banks.",
               "We don't go to court every month. Most of our work is on paper."],
         livre=('At the speakers\' dinner, a trader from Ohio asks: "What do you do, and why are you here?" '
                'Answer in four sentences: who you are, what you practice, who you work for, and why you are in Chicago.')),

    dict(n=2, titulo='My Professional World', desc='The third person and the -s, about a new colleague in Chicago.',
         s1_lead='Complete with the verb. Remember the -s with he, she and it. One answer is negative and one is a question.',
         s1=[('Marina ', 'reviews the draft', ' before every signature.',
              'Hint: review + the draft. She: add -s.'),
             ('Rafael ', 'does not handle', ' the sugar deals. He handles the cargo cases.',
              'Hint: NEGATIVE of handle. He + does not + verb (no -s).', "doesn't handle"),
             ('', 'Does the associate', ' go to the hearings?',
              'Hint: QUESTION. Does + the associate + verb.'),
             ('Our client ', 'exports soybeans', ' to China every month.',
              'Hint: export + soybeans. Our client = it: add -s.'),
             ('Paulo ', 'specializes in', ' fertilizer imports.',
              'Hint: specialize + in. He: add -s.')],
         msg=("Eduardo, Tom Baker here. I want you to meet my colleague, Sarah Wells. She joins our Chicago office on Monday. "
              "Sarah specializes in fertilizer contracts. She reads Portuguese, but she does not speak it. "
              "She handles the American buyers, and she talks to them every day. She does not go to court. "
              "She has a question about the Agrovale contract, so she calls you on Thursday at nine, Brazil time. "
              "Please send her the last draft before Wednesday."),
         voz='arthur', quem='Tom Baker, Harrow Shipping',
         msg_q=[('What does Sarah specialize in?', 'Fertilizer contracts', ['Sugar contracts', 'Shipping cases']),
                ('Does Sarah speak Portuguese?', 'No. She reads it, but she does not speak it.',
                 ['Yes. She speaks it every day.', 'No. She does not read it.']),
                ('When does Sarah call Eduardo?', 'On Thursday at nine, Brazil time',
                 ['On Wednesday at nine, Brazil time', 'On Thursday at nine, Chicago time'])],
         sit=[('A new client asks about your partner. You say:',
               '"My partner handles the shipping cases. He talks to the traders every day."',
               ['"My partner handle the shipping cases. He talk to the traders every day."',
                '"My partner, he handles the shipping cases. He talks to the traders."']),
              ('You want to know if Sarah reviews every contract. You ask:',
               '"Does she review every contract herself?"',
               ['"Do she reviews every contract herself?"', '"Does she reviews every contract herself?"']),
              ('Somebody says your associate goes to the hearings. That is wrong. You say:',
               '"No, she doesn\'t go to hearings. She prepares the files."',
               ['"No, she don\'t go to hearings. She prepares the files."',
                '"No, she doesn\'t goes to hearings. She prepare the files."'])],
         mail_to='Sarah Wells',
         mail=[('Our firm ', 'works for three', ' grain traders in Mato Grosso.',
                'Hint: work + for + three. Our firm = it: add -s.'),
               ('My associate, Ana, ', 'sends you', ' the last draft today.',
                'Hint: send + you. Ana = she: add -s.'),
               ('Paulo ', 'does not accept', " the buyer's contract.",
                'Hint: NEGATIVE of accept. He + does not + verb.', "doesn't accept"),
               ('', 'Does your client', ' need the English version or the Portuguese one?',
                'Hint: QUESTION. Does + your client + verb.')],
         fala=['She specializes in fertilizer contracts, and she handles the American buyers.',
               "He doesn't go to court. He reads, and he prepares the files."],
         livre=('Describe one person in your firm to Sarah: what this person does, what he or she does not do, '
                'and how often you work together. Four sentences, all in the third person.')),

    dict(n=3, titulo='Last Week at the Office', desc='The past simple, the -ed and the did, in a week report.',
         s1_lead='Complete with the verb in the past simple. One answer is negative and one is a question.',
         s1=[('On Monday the buyer ', 'sent us', ' a new draft.',
              'Hint: send + us. The past of send is irregular.'),
             ('We ', 'did not sign', ' anything on Tuesday.',
              'Hint: NEGATIVE of sign. Did not + verb.', "didn't sign"),
             ('', 'Did the client call', ' you after the meeting?',
              'Hint: QUESTION with call. Did + the client + verb.'),
             ('We ', 'postponed the meeting', ' to Thursday.',
              'Hint: postpone + the meeting. Regular: add -d.'),
             ('I ', 'met the bank manager', ' on Wednesday morning.',
              'Hint: meet + the bank manager. The past of meet is irregular.')],
         msg=("Good morning, Eduardo. Teresa here, with last week in one minute. On Monday I flew to Rotterdam. "
              "On Tuesday I attended two meetings at the terminal. The buyer did not bring the contract, so we did not sign. "
              "On Wednesday Marina found a problem in clause nine, and she called the client. "
              "On Thursday we postponed the signature to Monday. On Friday I came back to São Paulo. "
              "I did not go to the office. I went home and slept."),
         voz='ellen', quem='Teresa Nunes, your partner',
         msg_q=[('Where did Teresa fly on Monday?', 'To Rotterdam', ['To Geneva', 'To Cairo']),
                ('Why did they not sign on Tuesday?', 'The buyer did not bring the contract.',
                 ['The client did not like clause nine.', 'The ship arrived late.']),
                ('When is the new date for the signature?', 'Monday', ['Friday', 'Thursday'])],
         sit=[('Your supervisor asks: "Did you go to the meeting on Friday?" You answer:',
               '"Yes, I did. I attended it, and I filed the papers."',
               ['"Yes, I did. I am attended it, and I filed the papers."',
                '"Yes, I went the meeting, and I file the papers."']),
              ('You want to know if the buyer read the draft. You ask:',
               '"Did the buyer read the draft?"',
               ['"Did the buyer reads the draft?"', '"The buyer did read the draft?"']),
              ('The buyer said no to your price. You report:',
               '"They didn\'t accept our price."',
               ['"They not accepted our price."', '"They didn\'t accepted our price."'])],
         mail_to='Tom Baker',
         mail=[('Last week we ', 'closed the deal', ' with the buyer in Rotterdam.',
                'Hint: close + the deal. Regular: add -d.'),
               ('On Wednesday the bank ', 'asked for', ' two more documents.',
                'Hint: ask + for. Regular: add -ed.'),
               ('I ', 'did not travel', ' to Geneva this time.',
                'Hint: NEGATIVE of travel. Did not + verb.', "didn't travel"),
               ('', 'Did you receive', ' my documents on Thursday?',
                'Hint: QUESTION with receive. Did + you + verb.')],
         fala=['They postponed the meeting, and we accepted the new date.',
               'I flew to Rotterdam on Monday and came back on Friday.'],
         livre=('Tell Tom about your last week: three things you did, one thing you did not do, and one problem. '
                'Use the days of the week.')),

    dict(n=4, titulo='What Is Happening Now', desc='Present continuous for now, present simple for always, at harvest time.',
         s1_lead='Complete with the right form. Now and this month: am, is, are + -ing. Always and usually: the simple form.',
         s1=[('This month I ', 'am preparing', ' an application for a master\'s degree.',
              'Hint: prepare, THIS MONTH. I + am + verb-ing.', "i'm preparing"),
             ('My colleagues ', 'are handling my cases', ' while I am away.',
              'Hint: handle + my cases, NOW. They + are + verb-ing.'),
             ('I usually ', 'review contracts', ' on Monday mornings.',
              'Hint: review + contracts, USUALLY = routine. No -ing.'),
             ('', 'Are you working on', ' the appeal this week?',
              'Hint: QUESTION. Are + you + working + on.'),
             ('I ', 'am not answering', ' the buyer today. I need to talk to Paulo first.',
              'Hint: NEGATIVE of answer, TODAY. I + am not + verb-ing.', "i'm not answering")],
         msg=("Eduardo, Paulo Rezende. A quick update from the farm. We are harvesting the soybeans this week, "
              "but it is raining, and the trucks are moving slowly. Normally we load two hundred trucks a day. "
              "This week we are loading ninety. The buyer in Shanghai is asking for the documents, and my team is preparing them now. "
              "I am not signing the new contract before you read it. I am at the farm until Friday. Call me after six."),
         voz='arthur', quem='Paulo Rezende, Agrovale',
         msg_q=[('What is happening at the farm this week?', 'They are harvesting the soybeans in the rain.',
                 ['They are loading two hundred trucks a day.', 'They are signing the new contract.']),
                ('How many trucks are they loading a day this week?', 'Ninety', ['Two hundred', 'Nineteen']),
                ('Where is Paulo until Friday?', 'At the farm', ['At the port', 'In Shanghai'])],
         sit=[('A colleague asks what is different this month. You say:',
               '"I\'m preparing an application, so my partners are handling my cases."',
               ['"I prepare an application, so my partners handle my cases now."',
                '"I preparing an application, so my partners handling my cases."']),
              ('You want to know if your colleague is working from home today. You ask:',
               '"Are you working from home today?"',
               ['"You are working from home today?"', '"Do you working from home today?"']),
              ('A client asks: "Do you understand the clause?" You say:',
               '"Yes, I understand it."',
               ['"Yes, I\'m understanding it."', '"Yes, I am understand it."'])],
         mail_to='Renata Lima',
         mail=[('Currently I ', 'am reading', ' the two articles you sent.',
                'Hint: read, CURRENTLY. I + am + verb-ing.', "i'm reading"),
               ('Professor Hughes ', 'is checking my proposal', ' this week.',
                'Hint: check + my proposal, THIS WEEK. He + is + verb-ing.'),
               ('I ', 'usually write', ' in the morning, before the office opens.',
                'Hint: usually + write. Routine: no -ing. Usually goes BEFORE the verb.'),
               ('', 'Are you accepting', ' new documents this week?',
                'Hint: QUESTION with accept. Are + you + verb-ing.')],
         fala=["I usually review contracts on Mondays, but this week I'm reading applications.",
               "My colleagues are handling my cases while I'm away."],
         livre=('Tell Renata what is different in your life this month: two things you are doing now, '
                'two things you usually do, and one thing you are not doing.')),

    dict(n=5, titulo='Planning Ahead', desc='Going to for plans, will for decisions on the spot, for a visit to the university.',
         s1_lead='Complete with going to (a plan) or will (a decision now). One answer is negative and one is a question.',
         s1=[('Next year I ', 'am going to apply', " for a master's degree in Miami.",
              'Hint: apply, a PLAN. I + am + going to + verb.', "i'm going to apply"),
             ('We ', 'are not going to renew', ' the old agreement.',
              'Hint: NEGATIVE of renew, a PLAN. We + are not + going to + verb.', "aren't going to renew"),
             ('', 'Are they going to arrange', ' the interview in November?',
              'Hint: QUESTION with arrange. Are + they + going to + verb.'),
             ('You need the contract today? OK, I ', 'will send it', ' after lunch.',
              'Hint: send + it, a decision NOW. Will + verb.', "'ll send it"),
             ('Look at the sky. It ', 'is going to rain', ' this afternoon.',
              'Hint: rain. You can SEE it now: is + going to + verb.')],
         msg=("Good morning, Eduardo. Renata Lima, from the academic office. Here is the plan for your visit. "
              "You are going to arrive on the twelfth of January. On the thirteenth you are going to meet Professor Hughes at ten. "
              "After lunch, a student is going to show you the library. We are not going to have an exam. "
              "On the fourteenth you are going to attend two seminars. The bus is going to pick you up at the hotel at eight. "
              "Please send me your flight number."),
         voz='ellen', quem='Renata Lima, academic office',
         msg_q=[('When is Eduardo going to meet Professor Hughes?', 'On the thirteenth, at ten',
                 ['On the twelfth, at ten', 'On the fourteenth, at eight']),
                ('What is going to happen after lunch?', 'A student is going to show him the library.',
                 ['He is going to have an exam.', 'He is going to attend two seminars.']),
                ('What does Renata need from Eduardo?', 'His flight number', ['His passport', 'His thesis'])],
         sit=[('Your partner says: "The printer is broken." You decide now. You say:',
               '"No problem. I\'ll print it at home."',
               ['"No problem. I print it at home."', '"No problem. I will to print it at home."']),
              ('You want to know when they are going to call the candidates. You ask:',
               '"When are they going to call the candidates?"',
               ['"When they are going to call the candidates?"', '"When are they go to call the candidates?"']),
              ('You say no to the January intake. You say:',
               '"I\'m going to turn it down. January is too early for me."',
               ['"I\'m going to the turn down it. January is too early."',
                '"I going to turn it down. January is too early for me."'])],
         mail_to='Renata Lima',
         mail=[('My flight ', 'is going to arrive', ' at six in the morning.',
                'Hint: arrive, a PLAN. It + is + going to + verb.'),
               ('I ', 'am going to stay', ' at the hotel near the campus.',
                'Hint: stay, a PLAN. I + am + going to + verb.', "i'm going to stay"),
               ('I ', 'am not going to bring', ' my family this time.',
                'Hint: NEGATIVE of bring. I + am not + going to + verb.', "i'm not going to bring"),
               ('If the bus is late, I ', 'will take a taxi', '.',
                'Hint: take + a taxi, a decision NOW. Will + verb.', "'ll take a taxi")],
         fala=["I'm going to arrange a call with the admissions team next week.",
               "The printer is broken? Then I'll print it at home."],
         livre=('Your partner asks about your plans for next year. Say three things that are already decided, '
                'one thing you are not going to do, and one decision you make right now.')),

    dict(n=6, titulo='How Much, How Many?', desc='What you count and what you measure, in a cargo and a course.',
         s1_lead='Complete with the right quantity word. Count it one by one: many, a few. Measure it: much, a little.',
         s1=[('', 'How many trucks', ' do we need for the cargo?',
              'Hint: QUESTION. Trucks: you count them. How + many + trucks.'),
             ('There is ', 'not much space', ' in the warehouse this week.',
              'Hint: space: you measure it. Not + much + space.'),
             ('We have ', 'a few days', ' to load the vessel.',
              'Hint: days: you count them. A + few + days = some, not many.'),
             ('The government cut the quota, so we have ', 'fewer containers', ' this month.',
              'Hint: containers: you count them. The smaller number = fewer.'),
             ('Is there ', 'any information', ' about the new tuition?',
              'Hint: QUESTION. Information: you measure it. Any + information (no -s).')],
         msg=("Eduardo, Tom Baker. Some numbers for the new contract. We have forty thousand tons of corn, "
              "but we do not have many vessels this month. There are only two, and they are small. "
              "There is not much space at the port, and there is a lot of traffic. The buyer has a few questions about the price. "
              "He does not have much time: he needs an answer by Friday. I need some help with clause twelve."),
         voz='arthur', quem='Tom Baker, Harrow Shipping',
         msg_q=[('How much corn do they have?', 'Forty thousand tons',
                 ['Fourteen thousand tons', 'Four thousand tons']),
                ('How many vessels are there this month?', 'Only two, and they are small',
                 ['Twelve, and they are big', 'A lot, but they are small']),
                ('What does Tom need help with?', 'Clause twelve', ['The price', 'The traffic at the port'])],
         sit=[('You want to know the number of credits. You ask:',
               '"How many credits do I need for the degree?"',
               ['"How much credits do I need for the degree?"', '"How many credit do I need for the degree?"']),
              ('The client asks about time. There is very little. You say:',
               '"We don\'t have much time. The deadline is Friday."',
               ['"We don\'t have many time. The deadline is Friday."', '"We have a few time. The deadline is Friday."']),
              ('You have two or three questions about the tuition. You say:',
               '"I have a few questions about the tuition."',
               ['"I have a little questions about the tuition."', '"I have much questions about the tuition."'])],
         mail_to='David Hughes',
         mail=[('', 'How much is', ' the tuition for the second year?',
                'Hint: QUESTION about money. How + much + is.'),
               ('I have ', 'some questions', ' about the credits.',
                'Hint: questions: you count them. Some + questions.'),
               ('I do not have ', 'much free time', ' during the week.',
                'Hint: time: you measure it. Much + free time.'),
               ('Are there ', 'any classes', ' on Saturday?',
                'Hint: QUESTION. Classes: you count them. Any + classes.')],
         fala=["We don't have many vessels this month, and there isn't much space at the port.",
               'How many credits are compulsory, and how much is the tuition?'],
         livre=('A client asks about a shipment. Say how much cargo there is, how many trucks or vessels you need, '
                'how much time you have, and one problem.')),

    dict(n=7, titulo='Comparing Deals, Programs and Cities', desc='Bigger, more complex, the best: two buyers and two programs.',
         s1_lead='Complete with the comparative or the superlative. Short words take -er and -est; long words take more and the most.',
         s1=[('Paranaguá is ', 'smaller than', ' Santos, but it is faster.',
              'Hint: small, two ports. Small + -er + than.'),
             ('This contract is ', 'more complex than', ' the old one.',
              'Hint: complex is a long word. More + complex + than.'),
             ('Miami is ', 'the cheapest', ' of the three programs.',
              'Hint: cheap, three programs. The + cheap + -est.'),
             ('The new clause is ', 'clearer than', ' the old one.',
              'Hint: clear, two clauses. Clear + -er + than.'),
             ('London is ', 'as expensive as', ' New York.',
              'Hint: the SAME price. As + expensive + as.')],
         msg=("Good morning, Eduardo. Bianca Duarte, from the desk. You asked about the two buyers, so here is my comparison. "
              "The buyer in Shanghai is bigger, and he pays a higher price: four hundred dollars a ton. "
              "The buyer in Rotterdam pays less, three hundred and eighty, but he is faster. He pays in ten days, and Shanghai pays in thirty. "
              "The Rotterdam contract is also shorter and simpler. For me, Rotterdam is the safest choice."),
         voz='ellen', quem='Bianca Duarte, the desk',
         msg_q=[('Which buyer pays a higher price?', 'The buyer in Shanghai',
                 ['The buyer in Rotterdam', 'They pay the same price']),
                ('How fast does the Rotterdam buyer pay?', 'In ten days', ['In thirty days', 'In three days']),
                ("What is Bianca's choice?", 'Rotterdam, the safest choice',
                 ['Shanghai, the biggest buyer', 'Rotterdam, the cheapest contract'])],
         sit=[('One flight takes nine hours and the other takes twelve. You say:',
               '"The first flight is shorter than the second."',
               ['"The first flight is more short than the second."', '"The first flight is shortest than the second."']),
              ('You compare three programs. Boston has the highest fees. You say:',
               '"Boston is the most expensive of the three."',
               ['"Boston is the more expensive of the three."', '"Boston is most expensive than the three."']),
              ('Two contracts have the same number of pages. You say:',
               '"This contract is as long as that one."',
               ['"This contract is as long than that one."', '"This contract is so long as that one."'])],
         mail_to='Nora',
         mail=[('The Miami program is ', 'closer to', ' my office.',
                'Hint: close, two places. Close + -r + to.'),
               ('The London classes are ', 'bigger than', ' the Miami classes.',
                'Hint: big, two cities. Big + g + -er + than.'),
               ('For me, Miami is ', 'the most convenient', ' option.',
                'Hint: convenient is a long word. The + most + convenient.'),
               ('London is famous, but it is ', 'less convenient', ' for my family.',
                'Hint: the opposite of more convenient. Less + convenient.')],
         fala=['The Rotterdam buyer pays less, but he pays faster than Shanghai.',
               'For me, the shortest contract is the safest choice.'],
         livre=('Compare two clients, two cities or two courses you know. Say which one is bigger, cheaper or more difficult, '
                'and which one is the best for you, and why.')),

    dict(n=8, titulo='When the Deal Was Happening', desc='The long action and the short one that cuts it, in a video call.',
         s1_lead='Complete with the past continuous (was, were + -ing) for the long action, or the past simple for the short one.',
         s1=[('I ', 'was reading the contract', ' when the buyer called.',
              'Hint: read + the contract, the LONG action. I + was + verb-ing.'),
             ('While I ', 'was driving', ' to the airport, Tom sent me a message.',
              'Hint: drive, the LONG action. I + was + verb-ing.'),
             ('The client ', 'was not listening', ' when I explained the clause.',
              'Hint: NEGATIVE of listen. He + was not + verb-ing.', "wasn't listening"),
             ('', 'What were they discussing', ' when you arrived?',
              'Hint: QUESTION with discuss. What + were + they + verb-ing.'),
             ('We were signing the contract when the lights ', 'went out', '.',
              'Hint: go out, the SHORT action. Past simple of go.')],
         msg=("Eduardo, Tom Baker. Something strange happened yesterday. At three o'clock we were having a video call with the buyer in Cairo. "
              "His lawyer was reading the price clause, and I was taking notes. Suddenly the screen went black. "
              "While my assistant was calling the technician, the buyer sent an email. He accepted our price. "
              "Nobody in the room was expecting that. We signed the contract at five."),
         voz='arthur', quem='Tom Baker, Harrow Shipping',
         msg_q=[("What were they doing at three o'clock?", 'Having a video call with the buyer in Cairo',
                 ['Signing the contract in Cairo', 'Calling the technician']),
                ('What was Tom doing when the screen went black?', 'He was taking notes.',
                 ['He was reading the price clause.', 'He was sending an email.']),
                ('When did they sign the contract?', 'At five', ['At three', 'The next day'])],
         sit=[('Your partner asks what you were doing at ten last night. You say:',
               '"I was reviewing the Agrovale contract."',
               ['"I was review the Agrovale contract."', '"I were reviewing the Agrovale contract."']),
              ('You tell a story: a long action, then a short one. You say:',
               '"We were meeting the client when the ship arrived."',
               ['"We was meeting the client when the ship arrived."', '"We were meeting the client when the ship was arrive."']),
              ('You ask a colleague about the moment of the problem. You say:',
               '"When the bank called, what were you doing?"',
               ['"When the bank called, what you were doing?"', '"When the bank called, what did you doing?"'])],
         mail_to='Teresa',
         mail=[('Yesterday at noon I ', 'was working at home', ' when the client called.',
                'Hint: work + at home, the LONG action. I + was + verb-ing.'),
               ('He ', 'told me', ' about a problem with the regulator.',
                'Hint: tell + me, the SHORT action. Past simple of tell.'),
               ('While I ', 'was looking for', ' the document, he waited on the phone.',
                'Hint: look + for, the LONG action. I + was + verb-ing + for.'),
               ('', 'Were you', ' in the office at that time?',
                'Hint: QUESTION. Were + you.')],
         fala=['While I was driving to the airport, the client called me.',
               'We were having lunch when the buyer sent the counter-offer.'],
         livre=('Tell a colleague about a day when something interrupted your work. '
                'What were you doing, what happened, and what did you do next?')),

    dict(n=9, titulo='What Should I Do?', desc='Should, could and might, for an interview at the university.',
         s1_lead='Complete with should (advice), could (an option) or might (it is possible). One answer is negative and one is a question.',
         s1=[('You ', 'should read', ' the clause again before you sign.',
              'Hint: read, ADVICE. Should + verb.'),
             ('The ship ', 'might arrive', ' late because of the rain.',
              'Hint: arrive, it is POSSIBLE. Might + verb.'),
             ('We ', 'could ask', ' the bank for more time.',
              'Hint: ask, an OPTION. Could + verb.'),
             ('You ', 'should not send', ' the draft before Marina reviews it.',
              'Hint: NEGATIVE advice with send. Should not + verb.', "shouldn't send"),
             ('', 'Should we call', ' the client today?',
              'Hint: QUESTION. Should + we + verb.')],
         msg=("Eduardo, Grace Oliveira from the admissions office. Your interview is on Monday, so here is my advice. "
              "You should arrive fifteen minutes early. You should bring a copy of your cover letter. "
              "The professors might ask about your work in agribusiness, so you could prepare two short examples. "
              "You should not read your answers. The interview might take forty minutes. "
              "After the interview, you should send a short email to say thank you."),
         voz='ellen', quem='Grace Oliveira, admissions office',
         msg_q=[('How early should Eduardo arrive?', 'Fifteen minutes early', ['Fifty minutes early', 'Five minutes early']),
                ('What might the professors ask about?', 'His work in agribusiness', ['His grades', 'His family']),
                ('What should he do after the interview?', 'Send a short email to say thank you',
                 ['Call the admissions office', 'Bring a copy of his cover letter'])],
         sit=[('A junior lawyer asks for advice about a late ship. You say:',
               '"You should call the client today and tell him the number."',
               ['"You should to call the client today and tell him the number."',
                '"You should calling the client today and tell him the number."']),
              ('You are not sure about the weather at the port. You say:',
               '"It might rain at the port tomorrow."',
               ['"It might to rain at the port tomorrow."', '"It mights rain at the port tomorrow."']),
              ('You give an option, not an order. You say:',
               '"We could ask the buyer for two more days."',
               ['"We could asked the buyer for two more days."', '"We can could ask the buyer for two more days."'])],
         mail_to='Lucas, your associate',
         mail=[('You ', 'should check', ' the dates in clause four.',
                'Hint: check, ADVICE. Should + verb.'),
               ('The buyer ', 'might not accept', ' the new price.',
                'Hint: NEGATIVE possibility with accept. Might not + verb.'),
               ('We ', 'could send', ' him a counter-offer on Monday.',
                'Hint: send, an OPTION. Could + verb.'),
               ('You ', 'should not promise', ' anything before we talk.',
                'Hint: NEGATIVE advice with promise. Should not + verb.', "shouldn't promise")],
         fala=['You should arrive early, and you could prepare two short examples.',
               'The ship might be late, so we should warn the client today.'],
         livre=('A colleague is going to negotiate with a difficult buyer next week. '
                'Give three pieces of advice with should, one option with could, and one risk with might.')),

    dict(n=10, titulo='I Used to Practice Differently', desc='Used to for the habits that ended, at a family farm that changed.',
         s1_lead='Complete with used to (a past habit that ended), or with the present simple for today. One answer is negative and one is a question.',
         s1=[('I ', 'used to write', ' every contract in Portuguese.',
              'Hint: write, a PAST habit. Used to + verb.'),
             ('We ', 'did not use to have', ' clients outside Brazil.',
              'Hint: NEGATIVE of have, in the past. Did not + use to + verb (no -d).', "didn't use to have"),
             ('', 'Did you use to work', ' in real estate?',
              'Hint: QUESTION with work, in the past. Did + you + use to + verb.'),
             ('Clients ', 'used to call', ' the office. Now they send messages.',
              'Hint: call, a PAST habit. Used to + verb.'),
             ('Now I ', 'read contracts in English', ' every week.',
              'Hint: read + contracts + in English, TODAY. Present simple, no used to.')],
         msg=("Eduardo, Paulo Rezende. You asked about the old days at Agrovale. My father used to sell all the soybeans to one buyer in São Paulo. "
              "He used to sign the contract with a handshake. We did not use to have lawyers. "
              "We used to send the trucks to Santos, and they used to wait for weeks. "
              "Today we sell to buyers in four countries, and every contract has forty pages. That is why I call you every week."),
         voz='arthur', quem='Paulo Rezende, Agrovale',
         msg_q=[("Who did Paulo's father use to sell to?", 'One buyer in São Paulo',
                 ['Buyers in four countries', 'One buyer in Santos']),
                ('How did he use to sign the contract?', 'With a handshake', ['By email', 'With a lawyer']),
                ('How many pages does a contract have today?', 'Forty', ['Fourteen', 'Four'])],
         sit=[('You talk about an old habit that ended. You say:',
               '"I used to work only on domestic cases."',
               ['"I use to work only on domestic cases."', '"I used to working only on domestic cases."']),
              ('You ask a colleague about her past. You say:',
               '"Did you use to work in a big firm?"',
               ['"Did you used to work in a big firm?"', '"Do you used to work in a big firm?"']),
              ('This is true today, not in the past. You say:',
               '"Now I work with three legal systems."',
               ['"Now I used to work with three legal systems."', '"Now I use to work with three legal systems."'])],
         mail_to='Clara Nogueira',
         mail=[('Ten years ago I ', 'used to travel', ' to the farms every month.',
                'Hint: travel, a PAST habit. Used to + verb.'),
               ('I ', 'did not use to speak', ' English with clients.',
                'Hint: NEGATIVE of speak, in the past. Did not + use to + verb.', "didn't use to speak"),
               ('My first foreign client ', 'changed everything', '.',
                'Hint: change + everything, ONE moment in the past. Past simple.'),
               ('Now I ', 'keep up with', ' the news from Chicago every morning.',
                'Hint: keep + up + with, TODAY. Present simple.')],
         fala=['I used to work only on domestic cases. Now I work with buyers in four countries.',
               "We didn't use to have foreign clients, and now they are half of our work."],
         livre=('Tell Tom how your work changed: two things you used to do, one thing you did not use to do, '
                'the turning point, and what you do now.')),
]


def post_card(L, sorteio):
    n = L['n']
    corpo = (
        secao('Stage 1: Use It at Work', 'badge-practice', 'Grammar', L['s1_lead'], blanks(L['s1']))
        + secao('Stage 2: Listen to the Message', 'badge-quiz', 'Listening',
                'Listen to the message, then answer. The answers are words you hear.',
                mensagem(L['msg'], L['voz'], L['quem']) + quiz(L['msg_q'], sorteio))
        + secao('Stage 3: What Do You Say?', 'badge-quiz', 'Quiz',
                'Choose what a real speaker says.', quiz(L['sit'], sorteio))
        + secao('Stage 4: Write the Email', 'badge-practice', 'Writing',
                f'You are writing an email to {L["mail_to"]}. Complete each line. Tap Listen to hear the full line.',
                blanks(L['mail']))
        + secao('Stage 5: Say It', 'badge-speak', 'Speaking',
                'Listen, then record yourself. You get a word-by-word score.', speech(L['fala']))
        + secao('Stage 6: Your Answer', 'badge-think', 'Reflection',
                'Think, then record your answer. There is no wrong answer here.',
                think(f'think-result-po{n}', L['livre'])))
    return card(f'po-lesson-{n}', f'Post-class {n:02d}', L['titulo'], L['desc'], FOTO[n], corpo)


# ════════════════════════════════════════════════════════════════════════════
# FROM YOUR CLASS: um bloco por aula dada, das analises de aula (Zoom).
# Fonte: alumni-dashboard-analisedeaula /api/analise?id=<id>
#   grammar_errors (said x correct), resumo_aluno.correcoes, pronuncia,
#   nao_entendeu, palavras_novas. So entra o que a transcricao sustenta: fala
#   ininteligivel do STT ("Monthly Liar", "decline science") fica de fora.
# ════════════════════════════════════════════════════════════════════════════
CLASSES = [
    dict(analise=1128, data='27 August', aula=1, tema='Introducing yourself and your firm',
         fix=[('In class you said: "Does you advise companies that buy and sell grain?" Choose the correct question.',
               '"Do you advise companies that buy and sell grain?"',
               ['"Does you advise companies that buy and sell grain?"', '"Do you advises companies that buy and sell grain?"']),
              ('In class you said: "I not sign for the client." Choose the correct sentence.',
               '"I don\'t sign for the client."', ['"I not sign for the client."', '"I don\'t signs for the client."']),
              ('In class you said: "I am advised companies." Choose the correct sentence.',
               '"I advise companies."', ['"I am advised companies."', '"I am advise companies."'])],
         write=[('', "I'm a lawyer", ', and I advise companies.',
                 'In class you said: "My lawyer, and I advise companies." Start with I + am.', 'i am a lawyer'),
                ('We work with ', 'deadlines', ' every day.',
                 'In class you said: "We live with deadline." More than one: add -s.'),
                ('People ', "don't speak", ' English well.',
                 'In class you said: "That people not speak well English." Negative: don\'t + verb.', 'do not speak')],
         say_lead='Grain sounds like grey + n. In both, put your tongue between your teeth. Most rhymes with both.',
         say=['Most of our clients are grain traders.', "Both of my partners have a master's degree."],
         words=[('soybean', 'the bean that traders buy and sell as soya'),
                ('subdivision', 'a piece of land that is cut into many small lots'),
                ('to meet a deadline', 'to finish the work on the last day or before it'),
                ('to miss a deadline', 'to finish the work after the last day')]),

    dict(analise=1172, data='31 August', aula=2, tema='Your firm, your clients and your week',
         fix=[('In class you said: "We not go to a hearing every week." Choose the correct sentence.',
               '"We don\'t go to a hearing every week."',
               ['"We not go to a hearing every week."', '"We doesn\'t go to a hearing every week."']),
              ('In class you said: "I make any tests," about your son. Choose the natural sentence.',
               '"My son does a test every Friday."', ['"My son makes a test every Friday."', '"My son do a test every Friday."']),
              ('In class you said: "They export grains as soya, sugar." Choose the correct sentence.',
               '"They export grains such as soya and sugar."',
               ['"They export grains as soya and sugar."', '"They export grains like as soya and sugar."'])],
         write=[('A few of my clients ', 'import diesel', '.',
                 'In class you said "impart diesel". The verb is import: to bring goods into the country.'),
                ('The client wants somebody who reads ', 'both languages', '.',
                 'In class it sounded like "who reads buff". Both: tongue between your teeth.'),
                ('I am a partner ', 'in a law firm', '.',
                 'In class you said: "I work for... to any partners? In our law firm." Say: a partner + in + a law firm.')],
         say_lead='Evening starts with a long E, like in "eat". Mostly: MOST + ly. Chain starts like "change".',
         say=['In the evening I read the contracts, mostly in English.',
              'Trading companies work in the supply chain of grain.'],
         words=[('role', 'the job or the part that a person has in a team'),
                ('insurer', 'a company that pays when something bad happens to your goods'),
                ('arbitration', 'a way to solve a dispute without a court'),
                ('paperwork', 'all the documents that a job needs')]),

    dict(analise=1254, data='3 September', aula=2, tema='Roles in a law firm, in the third person',
         fix=[('In class you said: "She advised our company clients," about her work every day. Choose the correct sentence.',
               '"She advises our company clients."', ['"She advised our company clients."', '"She advise our company clients."']),
              ('In class you said: "The firm do not negotiated the price." Choose the correct sentence.',
               '"The firm doesn\'t negotiate the price."',
               ['"The firm do not negotiated the price."', '"The firm doesn\'t negotiates the price."']),
              ('In class you said: "She don\'t have our partner." Choose the correct sentence.',
               '"She is not a partner."', ['"She don\'t have our partner."', '"She doesn\'t is a partner."'])],
         write=[("She doesn't go ", 'to hearings', '.',
                 'In class you said: "She doesn\'t go a hearing." Go + to + the place, and more than one: hearings.'),
                ('Marina reviews the sugar contract ', 'on Monday at', ' ten a.m.',
                 'In class you said: "Marina reviews sugar contract in mold." Days: on. Hours: at.'),
                ('', 'Does she review', ' every contract?',
                 'In class you asked "Do you review...?" about Marina. She: does + verb, no -s.')],
         say_lead='Clause starts with CL and ends with a Z sound: it is not "cause". Commodity: co-MMO-di-ty.',
         say=['This clause is about the commodity price.', 'My associate prepares the schedule of fees.'],
         words=[('put into writing', 'to write an agreement down so that it is official'),
                ('to run a firm', 'to be the boss of a law office'),
                ('to go to court', 'to be at a hearing in front of a judge'),
                ('a commodity', 'a product like corn or sugar that is sold in big amounts')]),

    dict(analise=1314, data='9 September', aula=3, tema='A normal week in your office',
         fix=[('In class you said: "With me, it works... and associates." Choose the correct sentence.',
               '"Associates work with me."', ['"With me work associates."', '"With me, it works associates."']),
              ('In class you said: "Our firm doesn\'t not... go to hearings." Choose the correct sentence.',
               '"Our firm doesn\'t go to hearings."',
               ['"Our firm doesn\'t not go to hearings."', '"Our firm don\'t go to hearings."']),
              ('In class you asked: "They charge a fee with your clients?" Choose the correct question.',
               '"Does your law firm charge fees to clients?"',
               ['"Does your law firm charges fees with clients?"', '"Your law firm charge fees with clients?"'])],
         write=[('We have many ', 'activities', ' in a normal week.',
                 'In class it sounded like "many achievicts". Say: ac-TI-vi-ties.'),
                ('We ', 'draft contracts', ' for traders and banks.',
                 'In class you said: "they call us to make a contract." A lawyer drafts a contract.'),
                ('The ', 'grain trade', ' is our main market.',
                 'In class it sounded like "the green trade". Grain sounds like grey + n.')],
         say_lead='Machine is ma-SHEEN, not "machini". Review is re-VIEW, not "reveal". Which starts like "witch".',
         say=['A machine for disagreeing politely.', 'Which clause do you review first?'],
         words=[('an owner', 'the person or the company that has something'),
                ('out loud', 'in a voice that other people can hear'),
                ('a dispute', 'a serious disagreement between two companies'),
                ('to draw up', 'to write a formal document, like a contract')]),

    dict(analise=1384, data='14 September', aula=3, tema='Last week, in the past simple',
         fix=[('In class you said: "They not accepted the delivery clause." Choose the correct sentence.',
               '"They didn\'t accept the delivery clause."',
               ['"They not accepted the delivery clause."', '"They didn\'t accepted the delivery clause."']),
              ('In class you said: "We breached an agreement on Friday." You wanted to say it was a success. Choose the correct sentence.',
               '"We reached an agreement on Friday."',
               ['"We breached an agreement on Friday."', '"We reach an agreement on Friday."']),
              ('In class you said: "I attended the meeting, and they file the papers." Choose the correct sentence.',
               '"I attended the meeting and filed the papers."',
               ['"I attended the meeting and file the papers."', '"I attend the meeting and filed the papers."'])],
         write=[('They ', 'sent the first draft', ' on Monday.',
                 'In class you said: "They set the first draft." The verb is send, and the past is sent.'),
                ('She ', 'makes', ' the report every Friday.',
                 'In class you said: "She make it." Every Friday = routine. She + verb + s.'),
                ('', 'What did she do', ' last week?',
                 'In class you said: "In the last week, she did do..." Question: What + did + she + do?')],
         say_lead='Called and filed end in a D sound, with no extra E. Colleague is CO-league. Read, in the past, sounds like "red".',
         say=['I called my colleague and filed the papers.', 'I read the draft last night.'],
         words=[('to breach', 'to break the rules of an agreement'),
                ('to reach an agreement', 'to say yes to the same deal after a negotiation'),
                ('a business trip', 'a journey that you make for your work'),
                ('a lawsuit', 'a case that one side takes to a court')]),

    dict(analise=1554, data='21 September', aula=3, tema='Events at the terminal, in the past simple',
         fix=[('In class you said: "We was meeting with the client." Choose the correct sentence.',
               '"We had a meeting with the client."',
               ['"We was meeting with the client."', '"We was have a meeting with the client."']),
              ('In class you said: "I am attended the terminal meeting." Choose the correct sentence.',
               '"I attended the terminal meeting."',
               ['"I am attended the terminal meeting."', '"I was attend the terminal meeting."']),
              ('You wanted to ask about the client and the draft. Choose the correct question.',
               '"Was the client happy with the draft?"',
               ['"Did the client was happy with the draft?"', '"Did the client happy with the draft?"'])],
         write=[('We called the client ', 'in', ' São Paulo.',
                 'In class you said: "called the client São Paulo." Before a city: in.'),
                ('I ', 'received', ' the documents on Friday.',
                 'In class you said: "I recepted." The verb is receive, and the past is received.'),
                ("I didn't travel ", 'anywhere', ' last month.',
                 'In class you paused: "I didn\'t travel... anywhere." The word goes at the end.')],
         say_lead='Wednesday sounds like WENZ-day. Postponed, signed and stayed end in a D sound, with no extra E. Fifteen: fif-TEEN. Fifty: FIF-ty.',
         say=['On Wednesday they postponed the call, and we signed on Friday.',
              'Fifteen people stayed, and fifty people left.'],
         words=[('a terminal', 'the part of a port where ships load and unload'),
                ('to close a deal', 'to finish a negotiation with a signed agreement'),
                ('a negotiation call', 'a phone meeting where the two sides discuss a deal'),
                ('to file', 'to send a document to an office in the official way')]),

    dict(analise=1645, data='24 September', aula=4, tema='What is happening now, at work and at university',
         fix=[('In class you said: "She are living in Amsterdam." Choose the correct sentence.',
               '"She is living in Amsterdam."', ['"She are living in Amsterdam."', '"She living in Amsterdam."']),
              ('In class you asked: "What you are working on at the moment?" Choose the correct question.',
               '"What are you working on at the moment?"',
               ['"What you are working on at the moment?"', '"What do you working on at the moment?"']),
              ('In class you said: "She\'s attendees seminars," about her routine. Choose the correct sentence.',
               '"She attends seminars every Tuesday."',
               ['"She is attends seminars every Tuesday."', '"She attending seminars every Tuesday."'])],
         write=[("I'm working ", 'on a big contract', ' this month.',
                 'In class you said: "I do, big contract." Now: am + working + on + a big contract.'),
                ('Her colleagues ', 'send her', ' an update every Friday.',
                 'In class you said: "Her colleague is send her an update." Every Friday = routine = send.'),
                ("I'm working on ", 'an import contract', ' this month.',
                 'In class it sounded like "an imparte du mof". Say: an IM-port contract.')],
         say_lead='Proposal: pro-PO-sal. Semester: se-MES-ter. Research has the sound of "chip". Ship has the sound of "she". Thesis starts with TH.',
         say=['Her supervisor is reading the proposal this semester.',
              "She's researching the ship's delivery dates for her thesis."],
         words=[('to argue', 'to give reasons so that people accept your idea'),
                ('at a standstill', 'not moving at all, with no progress'),
                ('a bank statement', 'a document from the bank that shows your money'),
                ('equipment', 'the machines and the tools that a job needs')]),

    dict(analise=1701, data='28 September', aula=4, tema='Routine against this month',
         fix=[('In class you said: "This month I prepare an application." Choose the correct sentence.',
               '"This month I\'m preparing an application."',
               ['"This month I prepare an application."', '"This month I\'m prepare an application."']),
              ('In class you said: "My colleague is handles a contract." Choose the correct sentence.',
               '"My colleague is handling a contract."',
               ['"My colleague is handles a contract."', '"My colleague handling a contract."']),
              ('In class you said: "I\'m knowing the answer to that question." Choose the correct sentence.',
               '"I know the answer to that question."',
               ['"I\'m knowing the answer to that question."', '"I am know the answer to that question."'])],
         write=[("I'm working ", 'on an appeal', ' this week.',
                 'In class you said: "I\'m working in the appeal." You work ON a case.'),
                ('The government imposed tariffs ', 'on imports', ' from Brazil.',
                 'In class you said: "imposed the tariffs to the imports." A tariff is ON something.'),
                ('She ', 'usually reviews', ' the contracts on Friday.',
                 'In class you said: "Renata review all Friday the contracts." Usually goes before the verb; she: add -s.')],
         say_lead='Thesis starts with TH, tongue between your teeth: THEE-sis. Currently: CUR-rent-ly. Review: re-VIEW.',
         say=["I'm currently working on an appeal, and the proposal is almost ready.",
              'He reviews the thesis every week.'],
         words=[('an appeal', 'a request to a higher court to change a decision'),
                ('behind', 'later than the plan says'),
                ('a tariff', 'a tax on goods that come from another country'),
                ('to impose', 'to make a rule that other people have to follow')]),

    dict(analise=1784, data='1 October', aula=5, tema='Going to and will, for your application',
         fix=[('In class you said: "I\'m going to the submit." Choose the correct sentence.',
               '"I\'m going to submit the documents on Friday."',
               ['"I\'m going to the submit the documents on Friday."', '"I\'m going submit the documents on Friday."']),
              ('In class you asked: "When they are going to arrange the interview?" Choose the correct question.',
               '"When are they going to arrange the interview?"',
               ['"When they are going to arrange the interview?"', '"When are they go to arrange the interview?"']),
              ('In class you started: "I will... the flight to Rio tomorrow." Choose the correct sentence.',
               '"I will book the flight to Rio tomorrow."',
               ['"I will the flight to Rio tomorrow."', '"I will to book the flight to Rio tomorrow."'])],
         write=[('My goal is simple: ', 'to follow the seminars', '.',
                 'In class you said: "My goal is simple, follow the seminars." After "my goal is": to + verb.'),
                ("I'm not going ", 'to turn down', ' the offer.',
                 'In class you said: "I\'m not going through turn down an offer." Going + to + verb.'),
                ('My thesis is about ', 'delivery clauses', '.',
                 'In class it sounded like "delivery cars". Clause: CL + aws + Z.')],
         say_lead='Thesis: THEE-sis, tongue between your teeth. Semester: se-MES-ter. Teaches has the sound of "chip": TEA-ches.',
         say=["I'm going to write my thesis in the second semester.", 'She teaches the Monday group.'],
         words=[('an entry requirement', 'the thing you need before a program accepts you'),
                ('an academic calendar', 'the dates when the classes start and end in a university year'),
                ('a goal', 'the thing that you want to get in the future'),
                ('hectic', 'very busy, with too many things to do')]),
]


def class_card(i, C, sorteio):
    corpo = (
        secao('Stage 1: Fix What You Said', 'badge-quiz', 'Grammar',
              'These are sentences from your class. Choose the correct version.', quiz(C['fix'], sorteio))
        + secao('Stage 2: Write It Right', 'badge-practice', 'Writing',
                'Write the missing words. The hint shows what you said in class.', blanks(C['write']))
        + secao('Stage 3: Say It Right', 'badge-speak', 'Pronunciation', C['say_lead'], speech(C['say']))
        + secao('Stage 4: Words From Class', 'badge-practice', 'Vocabulary',
                'Words you met or asked about in this class. Match each one with its meaning.',
                matching(f'fc-match-{i}', C['words'], giro=i + 1)))
    return card(f'fc-class-{i}', f'Class of {C["data"]} &middot; Lesson {C["aula"]}', C['tema'],
                'Made from your own class: your sentences, your sounds, your new words.', FOTO[C['aula']], corpo)


# ════════════════════════════════════════════════════════════════════════════
# COLISAO: o loadState do hub restaura por texto, no documento inteiro.
# ════════════════════════════════════════════════════════════════════════════
def _assinaturas(html):
    txt = lambda s: re.sub(r'<[^>]+>', '', s).replace('&quot;', '"').replace('&amp;', '&').strip()
    a = {}
    a['blank'] = re.findall(r'data-answer="([^"]+)"[^>]*placeholder', html)
    a['blank'] += [m for m in re.findall(r'class="blank-input"[^>]*data-answer="([^"]+)"', html)]
    a['quiz'] = [txt(m)[:30] for m in re.findall(
        r'<div class="quiz-option"[^>]*data-correct="true">(.*?)</div>', html)]
    a['match'] = [txt(m) for m in re.findall(r'<span class="match-word"[^>]*>(.*?)</span>', html)]
    a['speech'] = re.findall(r'class="speech-card" data-phrase="([^"]+)"', html)
    a['think'] = [txt(m)[:40] for m in re.findall(r'<div class="think-question">(.*?)</div>', html)]
    a['order'] = re.findall(r'class="order-container" id="([^"]+)"', html)
    a['id'] = re.findall(r'\sid="([^"]+)"', html)
    return {k: [x.lower() for x in set(v)] if k == 'blank' else set(v) for k, v in a.items()}


def checa_colisoes(novas):
    hub = open(HUB, encoding='utf-8').read()
    for slot in ('afterclass', 'fromclass'):           # o hub sem as minhas abas
        hub = re.sub(r'<!-- ========== ABA SUPLEMENTAR.*?</div><!-- /tab-%s -->' % slot, '', hub, flags=re.S)
    velho = _assinaturas(hub)
    erros = []
    todos = {k: [] for k in velho}
    for html in novas:
        a = _assinaturas(html)
        for k in a:
            todos[k] += list(a[k])
            for x in a[k]:
                alvo = velho[k] if k != 'blank' else set(velho['blank'])
                if x in alvo:
                    erros.append('%s colide com o hub: %r' % (k, x))
    for k, v in todos.items():
        rep = sorted(set(x for x in v if v.count(x) > 1))
        if rep:
            erros.append('%s repetido entre as abas novas: %s' % (k, rep))
    return erros


def main():
    s_post = Sorteio('jose-eduardo-alves/postclass')
    s_fc = Sorteio('jose-eduardo-alves/fromclass')
    post = aba('afterclass', 'Post-class',
               'The third part of every lesson. Pre-class prepares you, the class with your teacher teaches you, '
               'and the post-class puts it to work in new situations. Do it after the class, in about fifteen minutes.',
               [post_card(L, s_post) for L in POST])
    fc = aba('fromclass', 'From Your Class',
             'Exercises made from your own classes: the sentences you said, the sounds your teacher corrected, '
             'and the words you asked about. A new block arrives after each class.',
             [class_card(i, C, s_fc) for i, C in enumerate(CLASSES, 1)])
    erros = checa_colisoes([post, fc])
    if erros:
        print('\n'.join(erros))
        sys.exit('ERRO: %d colisao(oes). Nada foi gravado.' % len(erros))
    for nome, html in (('postclass.html', post), ('fromclass.html', fc)):
        with open(os.path.join(AQUI, nome), 'w', encoding='utf-8') as f:
            f.write(html)
        print('ok  %-16s %6d bytes' % (nome, len(html.encode('utf-8'))))


if __name__ == '__main__':
    main()
