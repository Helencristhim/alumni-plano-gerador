# -*- coding: utf-8 -*-
"""Gerador de conteudo das aulas 7-11 da Andrea Aggio, fiel ao layout aula6.
Emite slides.html + preclass.html + complementary.html + config.json a partir de
_build/andrea-aggio-aula{N}/data.py (dict D). Layout clona a aula6 (que passou os gates).

USO: python3 _build/andrea_gen.py {N}
"""
import json
import os
import random
import re
import sys
import importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))

ACCENT = "#8E3B76"
ACCENT_LIGHT = "#B4568F"
ACCENT_RGB = "142,59,118"

LISTEN_SVG = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
              '<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/>'
              '<path d="M15.54 8.46a5 5 0 010 7.07"/></svg>')

ICONS = [
    ("linear-gradient(135deg,#0e7490,#22d3ee)", '<path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/>'),
    ("linear-gradient(135deg,#7c3aed,#a78bfa)", '<path d="M3 12a9 9 0 019-9 9 9 0 016.7 3L21 8"/><path d="M21 3v5h-5"/><path d="M21 12a9 9 0 01-9 9 9 9 0 01-6.7-3L3 16"/><path d="M3 21v-5h5"/>'),
    ("linear-gradient(135deg,#15803d,#4ade80)", '<path d="M4 4h16v12H5.2L4 17.4z"/><path d="M8 9h8M8 12h5"/>'),
    ("linear-gradient(135deg,#b45309,#f59e0b)", '<path d="M12 3v18"/><path d="M5 8l7-5 7 5"/><path d="M5 16l7 5 7-5"/>'),
    ("linear-gradient(135deg,#9f1239,#fb7185)", '<path d="M12 21s-7-4.5-7-10a7 7 0 0114 0c0 5.5-7 10-7 10z"/><circle cx="12" cy="11" r="2.5"/>'),
    ("linear-gradient(135deg,#4338ca,#818cf8)", '<rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20"/><path d="M6 15h4"/>'),
    ("linear-gradient(135deg,#c2410c,#fb923c)", '<path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><path d="M14 2v6h6"/><path d="M8 13h8M8 17h5"/>'),
    ("linear-gradient(135deg,#0d9488,#2dd4bf)", '<rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/><path d="M7 8l3 3 5-5"/>'),
    ("linear-gradient(135deg,#ca8a04,#fde047)", '<path d="M12 2l2.4 7.4H22l-6 4.6 2.3 7.4-6.3-4.6L5.7 21.4 8 14 2 9.4h7.6z"/>'),
    ("linear-gradient(135deg,#0369a1,#38bdf8)", '<path d="M12 2l2 5 5 .5-4 3.5 1 5-4-2.5L8 16l1-5-4-3.5 5-.5z"/><path d="M5 21h14"/>'),
    ("linear-gradient(135deg,#0f766e,#5eead4)", '<path d="M3 21V7l6-4 6 4v14"/><path d="M15 21V11l6 4v6"/><path d="M6 9h.01M6 13h.01M6 17h.01"/>'),
    ("linear-gradient(135deg,#1d4ed8,#60a5fa)", '<path d="M3 3v18h18"/><path d="M7 16l4-6 3 3 5-7"/>'),
]

DARK_BG = "linear-gradient(rgba(20,15,25,.72),rgba(20,15,25,.88))"
IMG_BG = "linear-gradient(rgba(20,15,25,.78),rgba(20,15,25,.9))"


def clean_def(d):
    """Remove o parentetico PT do fim da definicao (IN CLASS = zero portugues na tela)."""
    return re.sub(r'\s*\([^)]*\)\s*$', '', d).strip()


def audiobtn_sm(text):
    return (f'<button class="audio-btn-sm" onclick="event.stopPropagation();speakText(\'{text}\',this)">'
            f'{LISTEN_SVG} Listen</button>')


class SlideBuilder:
    def __init__(self):
        self.slides = []
        self.n = 0

    def add(self, cls, phase, teacher, inner, bg=None, inner_style=None):
        self.n += 1
        if self.n == 1:
            cls = cls + ' active'
        style = ''
        if bg:
            overlay = IMG_BG if 'slide-image' in cls else DARK_BG
            style = (f' style="background-image:{overlay},url(\'{bg}\');'
                     'background-size:cover;background-position:center"')
        istyle = f' style="{inner_style}"' if inner_style else ''
        self.slides.append(
            f'<!-- ========== SLIDE {self.n} ========== -->\n'
            f'<div class="{cls}" data-slide="{self.n}" data-phase="{phase}" data-teacher="{teacher}"{style}>\n'
            f'  <div class="slide-inner"{istyle}>\n{inner}\n  </div>\n</div>\n')

    def html(self):
        return '\n'.join(self.slides)


def teacher_map(D):
    """Instrucoes do icone T por slide (PT-BR, sem aspas duplas). Timing + como conduzir + CCQ."""
    p = D['partner_name'].capitalize()
    nxt = D['next_lesson']
    grp = D.get('grammar_point_pt', 'a estrutura-alvo da aula')
    ro = D.get('roleplay_teacher', [
        'Role-play guiado (4 min): Voce da o cenario e as keywords. Deixe a Andrea produzir com calma; corrija so no fim.',
        'Role-play semi-livre (4 min): Menos apoio. A Andrea usa as keywords sozinha. Anote os acertos.',
        'Pratica livre (5 min): ZERO pistas. NAO interrompa; anote os erros para o feedback. CELEBRE muito.'])
    return {
        'title': '<strong>Abertura (2 min):</strong> Compartilhe a tela. NAO cumprimente de forma scriptada (REGRA 27A). Va direto ao tema da aula com energia.',
        'warmup': f'<strong>Warm-up + callback (3 min):</strong> Ponte com a aula anterior. Faca a pergunta do slide e deixe a Andrea falar; ZERO correcao nesta etapa.',
        'agenda': '<strong>Agenda (1 min):</strong> Apresente as tres missoes da aula. Tom caloroso e direto. Passe ao proximo.',
        'vocab_trans': '<strong>Transicao vocab (1 min):</strong> Diga: doze palavras e expressoes novas. Click each card to reveal. Passe ao proximo.',
        'vocab1': '<strong>Vocab reveal 1-6 (6 min):</strong> Leia a pista em ingles, a Andrea tenta a palavra, depois revele e toque o audio. Faca CCQ curto em 2 palavras (ex: significado literal vs uso real).',
        'vocab2': '<strong>Vocab reveal 7-12 (6 min):</strong> Mesma dinamica. Confirme a compreensao com CCQs rapidas e peca 1 frase-exemplo da Andrea para 2 palavras.',
        'match': '<strong>Consolidar vocab (3 min):</strong> A Andrea liga cada palavra a definicao em voz alta. Leitura guiada; confirme as duplas que costumam confundir.',
        'read_trans': '<strong>Transicao leitura (1 min):</strong> Diga: read for the main idea first, do not worry about every word. Passe ao proximo.',
        'reading': '<strong>Reading + Gist (5 min):</strong> De 2 minutos de leitura silenciosa. Depois: what is the main idea? A Andrea clica a alternativa certa (fica verde). NAO peca traducao palavra a palavra.',
        'tf': '<strong>True / False (4 min):</strong> A Andrea decide TRUE ou FALSE ANTES de clicar. Ao clicar, o veredito e a justificativa aparecem. Discuta cada uma voltando ao texto.',
        'gapfill': '<strong>Gap-fill (5 min):</strong> Exercicio-chave. A Andrea le o resumo e escolhe a palavra certa do banco, EM VOZ ALTA. Sem gabarito visivel. Use o vocab-note para reforcar a gramatica.',
        'bank': '<strong>Useful language (3 min):</strong> Apresente as frases-modelo. Peca que a Andrea leia cada chip em voz alta e complete uma delas com um contexto real do trabalho dela.',
        'gram_trans': f'<strong>Transicao gramatica (1 min):</strong> Diga que o foco agora e {grp}. Passe ao proximo.',
        'gram_disc': '<strong>Grammar discovery (6 min):</strong> Leia os 3 exemplos. NAO mostre a regra primeiro. Pergunte o que cada frase faz e espere a Andrea notar o padrao. So entao clique Reveal the Rule. Faca 1 CCQ sobre a forma correta.',
        'lf': '<strong>Language Focus (4 min):</strong> A Andrea le cada linha e classifica a funcao. Use como ponte para o erro comum do proximo slide.',
        'mistake': '<strong>Common mistake (3 min):</strong> Mostre certo (verde) vs errado (vermelho). Peca que a Andrea leia as versoes certas 2 vezes em voz alta.',
        'dialogue': f'<strong>Dialogo (6 min):</strong> Voce e o {p}. Click Next Line a cada fala. Para cada fala da Andrea, peca que ELA fale primeiro, depois toque o audio. Celebre o uso correto da estrutura-alvo.',
        'comp': f'<strong>Comprehension (3 min):</strong> Perguntas sobre o {p} (o interlocutor), nao sobre a Andrea (REGRA 27F). A Andrea tenta antes de revelar; click para mostrar a resposta.',
        'listen1': '<strong>Listening 1 (5 min):</strong> Toque SEM texto, 2 vezes. As perguntas aparecem ao final do audio. Use 0.75x se ela pedir.',
        'listen2': '<strong>Listening 2 (4 min):</strong> Toque SEM texto, 2 vezes. As perguntas aparecem ao final. Compare o contexto com o listening 1.',
        'scenarios': '<strong>Scenarios (5 min):</strong> Para cada cena, a Andrea produz a resposta em voz alta usando a estrutura-alvo. Sem gabarito visivel; ela produz.',
        'answerkey': '<strong>Answer key (2 min):</strong> O accordion fica fechado. A Andrea so clica depois de tentar o gap-fill e os cenarios. Controle do professor (toggle); use para conferir.',
        'roleplay': ro,
        'survival': '<strong>Survival lines (3 min):</strong> Leia cada frase, toque o audio e peca que a Andrea repita. Sao as frases-chave da aula.',
        'learned': '<strong>Checklist (2 min):</strong> Diga: click each item if you feel confident. Leia cada item. Os 5 checks = aula completa e stamp no passaporte.',
        'badge': f'<strong>Encerramento (2 min):</strong> Parabenize a Andrea e entregue o badge. Passe o homework ORALMENTE (gravacao + tarefa escrita da aula). Proxima aula: {nxt}.',
    }


def build_slides(D):
    sb = SlideBuilder()
    D['t'] = teacher_map(D)
    acc = 'class="accent"'
    partner = D['partner_name']

    # 1 TITLE
    sb.add('slide slide-image', 1, D['t']['title'],
           f'    <div class="chapter-label">Lesson {D["n"]} &middot; {D["chapter_tag"]}</div>\n'
           f'    <h1 class="slide-heading" style="font-size:2.4rem;color:#fff">{D["title_h1"]}</h1>\n'
           f'    <p style="color:rgba(255,255,255,.85);font-size:1.05rem;margin-top:1rem">{D["title_sub"]}</p>',
           bg=D['bg_title'], inner_style='text-align:center')

    # 2 WARM-UP
    sb.add('slide slide-dark', 1, D['t']['warmup'],
           f'    <div class="chapter-label">Warm-Up</div>\n'
           f'    <h2 class="slide-heading" style="color:#fff">{D["warm_h2"]}</h2>\n'
           f'    <p style="color:rgba(255,255,255,.82);font-size:1rem;margin:1rem auto 0;max-width:580px">{D["warm_p"]}</p>\n'
           f'    <p style="color:var(--accent-light);font-size:.92rem;margin-top:1.3rem">{D["warm_prompt"]}</p>',
           inner_style='text-align:center')

    # 3 AGENDA
    missions = ''
    for i, m in enumerate(D['missions'], 1):
        missions += (f'      <div style="display:flex;gap:.9rem;align-items:center;background:var(--bg-card);border:1px solid var(--border);border-radius:12px;padding:1rem 1.2rem">'
                     f'<div style="width:34px;height:34px;border-radius:9px;background:var(--accent);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;flex-shrink:0">{i}</div>'
                     f'<p style="font-size:.95rem">{m}</p></div>\n')
    sb.add('slide slide-light', 1, D['t']['agenda'],
           f'    <div class="chapter-label">Today</div>\n'
           f'    <h2 class="slide-heading">Three <span {acc}>Missions</span></h2>\n'
           f'    <div style="display:flex;flex-direction:column;gap:.8rem;max-width:540px;margin:1.4rem auto 0">\n{missions}    </div>')

    # 4 VOCAB TRANSITION
    sb.add('slide slide-image', 2, D['t']['vocab_trans'],
           f'    <div class="chapter-label">Chapter 2: {D["phases"][1]}</div>\n'
           f'    <h2 class="slide-heading" style="font-size:2rem;color:#fff">{D["vocab_trans_h2"]}</h2>\n'
           f'    <p style="color:rgba(255,255,255,.82);font-size:1rem;margin-top:.5rem">12 key words and expressions</p>',
           bg=D['bg_vocab'], inner_style='text-align:center')

    # 5 & 6 VOCAB reveal
    def vocab_slide(cards, gridid, countid, label, teacher):
        cells = ''
        for (word, deff, ex), (grad, svg) in cards:
            cd = clean_def(deff)
            cells += (f'      <div class="vocab-card" onclick="revealVocab(this)">\n'
                      f'        <div class="card-icon" style="background:{grad}"><svg viewBox="0 0 24 24" fill="none" stroke="#fff">{svg}</svg><div class="card-hint">{cd}</div></div>\n'
                      f'        <div class="card-body"><div class="card-word">{word}</div><div class="card-def">{cd}</div><div class="card-example">"{ex}"</div><div class="card-audio">{audiobtn_sm(word)}</div></div>\n'
                      f'      </div>\n')
        return (f'    <div class="chapter-label">Vocabulary</div>\n'
                f'    <h2 class="slide-heading">Words <span {acc}>{label}</span></h2>\n'
                f'    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem"><span id="{countid}">0 / 6 words revealed</span></p>\n'
                f'    <div class="vocab-grid" id="{gridid}">\n{cells}    </div>')

    voc = D['vocab']
    paired = list(zip(voc, ICONS))
    sb.add('slide slide-light', 2, D['t']['vocab1'],
           vocab_slide(paired[:6], 'vocabGrid1', 'vocabCount1', '1-6', None))
    sb.add('slide slide-light', 2, D['t']['vocab2'],
           vocab_slide(paired[6:12], 'vocabGrid2', 'vocabCount2', '7-12', None))

    # 7 MATCHING consolidate
    sb.add('slide slide-light', 2, D['t']['match'],
           f'    <div class="chapter-label">Consolidate</div>\n'
           f'    <h2 class="slide-heading">Match the <span {acc}>Meaning</span></h2>\n'
           f'    <!--IC-BLOCKS:vocab-->')

    if D['reading']:
        # 8 READING TRANSITION
        sb.add('slide slide-image', 3, D['t']['read_trans'],
               f'    <div class="chapter-label">Chapter 3: {D["phases"][2]}</div>\n'
               f'    <h2 class="slide-heading" style="font-size:2rem;color:#fff">{D["read_trans_h2"]}</h2>\n'
               f'    <p style="color:rgba(255,255,255,.82);font-size:1rem;margin-top:.5rem">Read for the main idea</p>',
               bg=D['bg_read'], inner_style='text-align:center')
        # 9 READING + GIST
        sb.add('slide slide-light', 3, D['t']['reading'],
               f'    <div class="chapter-label">Read for the Main Idea</div>\n'
               f'    <h2 class="slide-heading">{D["reading_h2"]}</h2>\n'
               f'    <!--IC-BLOCKS:reading-->')
        # 10 TRUE/FALSE
        sb.add('slide slide-light', 3, D['t']['tf'],
               f'    <div class="chapter-label">Check Understanding</div>\n'
               f'    <h2 class="slide-heading">True or <span {acc}>False?</span></h2>\n'
               f'    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem">Decide first, then tap to reveal the answer and why</p>\n'
               f'    <!--IC-BLOCKS:tf-->')

    ph3 = 3
    # GAP-FILL + note
    sb.add('slide slide-light', ph3, D['t']['gapfill'],
           f'    <div class="chapter-label">Complete the Summary</div>\n'
           f'    <h2 class="slide-heading">Fill the <span {acc}>Gaps</span></h2>\n'
           f'    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem">Read the summary and choose a word from the bank for each gap</p>\n'
           f'    <!--IC-BLOCKS:gapfill-->')
    # BANK
    sb.add('slide slide-light', ph3, D['t']['bank'],
           f'    <div class="chapter-label">{D["bank_label_top"]}</div>\n'
           f'    <h2 class="slide-heading">Useful <span {acc}>Phrases</span></h2>\n'
           f'    <!--IC-BLOCKS:bank-->')

    # GRAMMAR transition
    sb.add('slide slide-image', 4, D['t']['gram_trans'],
           f'    <div class="chapter-label">Chapter 4: {D["phases"][3]}</div>\n'
           f'    <h2 class="slide-heading" style="font-size:2rem;color:#fff">{D["gram_trans_h2"]}</h2>\n'
           f'    <p style="color:rgba(255,255,255,.82);font-size:1rem;margin-top:.5rem">{D["gram_trans_sub"]}</p>',
           bg=D['bg_gram'], inner_style='text-align:center')

    # GRAMMAR DISCOVERY
    ex_rows = ''
    for txt, spoken, colorhtml in D['gram_examples']:
        ex_rows += (f'      <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:.8rem;display:flex;justify-content:space-between;align-items:center;gap:.6rem">'
                    f'<p style="font-size:.92rem">{colorhtml}</p>{audiobtn_sm(spoken)}</div>\n')
    tbl_rows = ''
    for i, (form, use, exm) in enumerate(D['gram_table']):
        bg = 'background:var(--bg-elevated);' if i % 2 == 1 else ''
        border = 'border-bottom:1px solid var(--border)' if i < len(D['gram_table']) - 1 else ''
        tbl_rows += (f'          <tr style="{bg}{border}"><td style="padding:.5rem;font-weight:600">{form}</td>'
                     f'<td style="padding:.5rem">{use}</td><td style="padding:.5rem">{exm}</td></tr>\n')
    rid = f'rule{D["n"]}'
    sb.add('slide slide-light', 4, D['t']['gram_disc'],
           f'    <div class="chapter-label">Grammar Discovery</div>\n'
           f'    <h2 class="slide-heading">Listen and <span {acc}>Notice</span></h2>\n'
           f'    <div style="display:flex;flex-direction:column;gap:.7rem;max-width:600px;margin:1rem auto 0">\n{ex_rows}    </div>\n'
           f'    <p style="text-align:center;font-size:.85rem;color:var(--text-dim);margin-top:1rem">{D["gram_disc_q"]}</p>\n'
           f'    <button class="primary-btn" style="margin:1rem auto 0;display:block;background:var(--accent);color:#fff;border:none;border-radius:8px;padding:.6rem 1.4rem;font-size:.9rem;font-weight:600;cursor:pointer" onclick="var t=document.getElementById(\'{rid}\');t.style.display=(t.style.display===\'none\'||!t.style.display)?\'block\':\'none\'">Reveal the Rule</button>\n'
           f'    <div id="{rid}" style="display:none;max-width:600px;margin:1rem auto 0;overflow-x:auto">\n'
           f'      <table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">\n'
           f'        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.6rem;text-align:left">Form</th><th style="padding:.6rem;text-align:left">Use</th><th style="padding:.6rem;text-align:left">Example</th></tr></thead>\n'
           f'        <tbody>\n{tbl_rows}        </tbody>\n      </table>\n'
           f'      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.6rem;text-align:center">{D["gram_rule_foot"]}</p>\n'
           f'    </div>')

    # LANGUAGE FOCUS
    sb.add('slide slide-light', 4, D['t']['lf'],
           f'    <div class="chapter-label">Language Focus</div>\n'
           f'    <h2 class="slide-heading">{D["lf_h2"]}</h2>\n'
           f'    <!--IC-BLOCKS:lf-->')

    # COMMON MISTAKE
    pairs = ''
    for wrong, right in D['mistakes']:
        pairs += (f'      <div style="display:grid;grid-template-columns:1fr 1fr;gap:.8rem">\n'
                  f'        <div style="background:var(--danger-bg);border:1px solid var(--danger-border);border-radius:10px;padding:1rem"><p style="font-size:.78rem;color:var(--danger);font-weight:700;margin-bottom:.3rem">&#10007; WRONG</p><p style="font-size:.88rem">"{wrong}"</p></div>\n'
                  f'        <div style="background:var(--success-bg);border:1px solid var(--success-border);border-radius:10px;padding:1rem"><p style="font-size:.78rem;color:var(--success);font-weight:700;margin-bottom:.3rem">&#10003; RIGHT</p><p style="font-size:.88rem">{right}</p></div>\n'
                  f'      </div>\n')
    sb.add('slide slide-light', 4, D['t']['mistake'],
           f'    <div class="chapter-label">Common Mistake</div>\n'
           f'    <h2 class="slide-heading">Right vs <span {acc}>Wrong</span></h2>\n'
           f'    <div style="display:flex;flex-direction:column;gap:1rem;max-width:540px;margin:1.2rem auto 0">\n{pairs}    </div>\n'
           f'    <p style="font-size:.82rem;color:var(--text-dim);margin:1rem auto 0;max-width:480px;text-align:center">{D["mistake_note"]}</p>')

    # DIALOGUE
    lines = ''
    for i, (who, voice, text, disp) in enumerate(D['dialogue'], 1):
        cls_av = 'andrea' if who == 'andrea' else partner
        letter = 'A' if who == 'andrea' else partner[0].upper()
        vis = ' visible' if i == 1 else ''
        lines += (f'      <div class="dialogue-line{vis}" data-line="{i}" data-voice="{voice}">'
                  f'<div class="dialogue-avatar {cls_av}">{letter}</div>'
                  f'<div class="dialogue-bubble {cls_av}-bubble">{disp} '
                  f'<span class="audio-inline" onclick="speakText(\'{text}\',this)">{LISTEN_SVG}</span></div></div>\n')
    sb.add('slide slide-dark', 5, D['t']['dialogue'],
           f'    <div class="chapter-label">Dialogue</div>\n'
           f'    <h2 class="slide-heading" style="color:#fff">{D["dialogue_h2"]}</h2>\n'
           f'    <div class="dialogue-box" id="dialogueBox">\n{lines}    </div>\n'
           f'    <button class="primary-btn" id="nextLineBtn" onclick="nextDialogueLine()" style="margin:1.2rem auto 0;display:block;background:var(--accent);color:#fff;border:none;border-radius:8px;padding:.6rem 1.4rem;font-size:.9rem;font-weight:600;cursor:pointer">Next Line</button>')

    # COMPREHENSION (about partner)
    cq = ''
    for q, a in D['comprehension']:
        cq += (f'      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">{q}</div><div class="q-answer">{a}</div></div>\n')
    sb.add('slide slide-light', 5, D['t']['comp'],
           f'    <div class="chapter-label">Did You Catch It?</div>\n'
           f'    <h2 class="slide-heading">About <span {acc}>{partner.capitalize()}</span></h2>\n'
           f'    <div class="comp-questions" style="max-width:540px;margin:1.2rem auto 0">\n{cq}    </div>')

    # LISTENING 1 & 2
    def listening_slide(idx, li, label, h2, sub, qs):
        pid = f'mp-listen{idx}'
        wf = f'waveform{idx}'
        qid = f'listening{idx}Qs'
        bars = ''.join('<div class="bar"></div>' for _ in range(20))
        qhtml = ''
        for q, a in qs:
            qhtml += (f'      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">{q}</div><div class="q-answer">{a}</div></div>\n')
        return (f'    <div class="chapter-label">Listening {idx}</div>\n'
                f'    <h2 class="slide-heading" style="color:#fff">{h2}</h2>\n'
                f'    <p style="color:rgba(255,255,255,.78);font-size:.9rem;margin-bottom:1rem">{sub}</p>\n'
                f'    <div class="waveform waveform-paused" id="{wf}">{bars}</div>\n'
                f'    <div class="mock-player" id="{pid}" data-src="/audio/andrea-aggio/{li["file"]}" data-waveform="{wf}" data-questions="{qid}" style="max-width:460px;margin:.8rem auto 0">\n'
                f'      <div class="lp-seekbar" onclick="mpSeek(event,\'{pid}\')" style="width:100%;height:6px;background:rgba(255,255,255,.12);border-radius:3px;cursor:pointer;position:relative"><div class="lp-progress" id="progress-{pid}" style="width:0%;height:100%;background:var(--accent-light);border-radius:3px;transition:width .1s"></div></div>\n'
                f'      <div style="display:flex;justify-content:space-between;margin:.4rem 0 .6rem"><span id="time-current-{pid}" style="font-size:.72rem;color:rgba(255,255,255,.78)">0:00</span><span id="time-total-{pid}" style="font-size:.72rem;color:rgba(255,255,255,.78)">0:00</span></div>\n'
                f'      <div style="display:flex;align-items:center;justify-content:center;gap:1rem;margin-bottom:.6rem">\n'
                f'        <button class="lp-btn" onclick="mpSkip(\'{pid}\',-5)" aria-label="Back 5 seconds" style="background:transparent;border:1px solid rgba(255,255,255,.3);color:#fff;border-radius:50%;width:38px;height:38px;cursor:pointer;font-size:.65rem;font-weight:700">-5s</button>\n'
                f'        <button class="lp-btn lp-play" id="play-{pid}" onclick="mpToggle(\'{pid}\')" aria-label="Play or pause" style="background:var(--accent);border:none;color:#fff;border-radius:50%;width:48px;height:48px;cursor:pointer"><svg class="lp-icon-play" viewBox="0 0 24 24" width="18" height="18"><polygon points="5 3 19 12 5 21 5 3" fill="currentColor"/></svg><svg class="lp-icon-pause" viewBox="0 0 24 24" width="18" height="18" style="display:none"><rect x="6" y="4" width="4" height="16" fill="currentColor"/><rect x="14" y="4" width="4" height="16" fill="currentColor"/></svg></button>\n'
                f'        <button class="lp-btn" onclick="mpSkip(\'{pid}\',5)" aria-label="Forward 5 seconds" style="background:transparent;border:1px solid rgba(255,255,255,.3);color:#fff;border-radius:50%;width:38px;height:38px;cursor:pointer;font-size:.65rem;font-weight:700">+5s</button>\n'
                f'      </div>\n'
                f'      <div style="display:flex;gap:.4rem;justify-content:center">\n'
                f'        <button class="lp-speed-btn" onclick="mpSpeed(\'{pid}\',0.5,this)" style="background:transparent;border:1px solid rgba(255,255,255,.25);color:rgba(255,255,255,.82);border-radius:6px;padding:.2rem .6rem;font-size:.7rem;cursor:pointer">0.5x</button>\n'
                f'        <button class="lp-speed-btn" onclick="mpSpeed(\'{pid}\',0.75,this)" style="background:transparent;border:1px solid rgba(255,255,255,.25);color:rgba(255,255,255,.82);border-radius:6px;padding:.2rem .6rem;font-size:.7rem;cursor:pointer">0.75x</button>\n'
                f'        <button class="lp-speed-btn lp-speed-active" onclick="mpSpeed(\'{pid}\',1,this)" style="background:var(--accent);border:1px solid var(--accent);color:#fff;border-radius:6px;padding:.2rem .6rem;font-size:.7rem;cursor:pointer">1x</button>\n'
                f'        <button class="lp-speed-btn" onclick="mpSpeed(\'{pid}\',1.25,this)" style="background:transparent;border:1px solid rgba(255,255,255,.25);color:rgba(255,255,255,.82);border-radius:6px;padding:.2rem .6rem;font-size:.7rem;cursor:pointer">1.25x</button>\n'
                f'      </div>\n'
                f'    </div>\n'
                f'    <div class="comp-questions" id="{qid}" style="display:none;max-width:520px;margin:1.2rem auto 0">\n{qhtml}    </div>')

    sb.add('slide slide-dark', 5, D['t']['listen1'],
           listening_slide(1, D['listenings'][0], 'Listening 1', D['listen1_h2'], D['listen1_sub'], D['listen1_qs']),
           inner_style='text-align:center')
    sb.add('slide slide-dark', 5, D['t']['listen2'],
           listening_slide(2, D['listenings'][1], 'Listening 2', D['listen2_h2'], D['listen2_sub'], D['listen2_qs']),
           inner_style='text-align:center')

    # SCENARIOS
    sb.add('slide slide-light', 6, D['t']['scenarios'],
           f'    <div class="chapter-label">Chapter 6: {D["phases"][5]}</div>\n'
           f'    <h2 class="slide-heading">{D["scenarios_h2"]}</h2>\n'
           f'    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem">From guided to free &mdash; say each one out loud</p>\n'
           f'    <!--IC-BLOCKS:practice-->')

    # ANSWER KEY
    sb.add('slide slide-light', 6, D['t']['answerkey'],
           f'    <div class="chapter-label">Check Your Work</div>\n'
           f'    <h2 class="slide-heading">Model <span {acc}>Answers</span></h2>\n'
           f'    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin:.3rem auto 0;max-width:480px">Try the gap-fill and the scenarios first. Reveal the key only to compare.</p>\n'
           f'    <div style="max-width:560px;margin:1rem auto 0">\n      <!--IC-BLOCKS:answerkey-->\n    </div>')

    # ROLE-PLAYS
    for idx, rp in enumerate(D['roleplays'], 1):
        label = {1: 'Guided', 2: 'Semi-free', 3: 'Free'}[idx]
        chips = ''
        if rp.get('keywords'):
            chip_html = ''.join(
                f'<span style="border:1px solid var(--accent);color:var(--accent);border-radius:20px;padding:.3rem .9rem;font-size:.82rem">{k}</span>'
                for k in rp['keywords'])
            chips = (f'      <div style="display:flex;flex-wrap:wrap;gap:.5rem;justify-content:center">{chip_html}</div>\n')
        else:
            chips = '      <p style="font-size:.85rem;color:var(--text-dim);font-style:italic">No keywords. The conversation is yours!</p>\n'
        sb.add('slide slide-light', 6, D['t']['roleplay'][idx - 1],
               f'    <div class="chapter-label">Role-Play {idx} of 3 &mdash; {label}</div>\n'
               f'    <h2 class="slide-heading">{rp["h2"]}</h2>\n'
               f'    <div class="roleplay-body" style="max-width:500px;margin:1rem auto 0;background:linear-gradient(135deg,rgba({ACCENT_RGB},.12),rgba({ACCENT_RGB},.03));border:1px solid var(--accent);border-radius:12px;padding:1.5rem">\n'
               f'      <p class="roleplay-scenario" style="font-size:.9rem;margin-bottom:1rem"><strong>Scenario:</strong> {rp["scenario"]}</p>\n{chips}    </div>')

    # SURVIVAL
    surv = ''
    for i, (en, pt) in enumerate(D['survival'], 1):
        surv += (f'      <div class="survival-item-ic"><div class="survival-num-ic">{i}</div><div class="survival-text-ic">"{en}"</div>'
                 f'<button class="audio-btn-sm" onclick="speakText(\'{en}\',this)">{LISTEN_SVG}</button></div>\n')
    sb.add('slide slide-dark', 7, D['t']['survival'],
           f'    <div class="chapter-label">Chapter 7: Wrap-Up</div>\n'
           f'    <h2 class="slide-heading" style="color:#fff">{D["survival_h2"]}</h2>\n'
           f'    <div class="survival-grid" style="max-width:560px;margin:1.5rem auto 0">\n{surv}    </div>',
           inner_style='text-align:center')

    # WHAT I LEARNED
    checks = ''
    for c in D['learned']:
        checks += (f'      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg></div>{c}</div>\n')
    sb.add('slide slide-dark', 7, D['t']['learned'],
           f'    <div class="chapter-label">Self-Assessment</div>\n'
           f'    <h2 class="slide-heading" style="color:#fff">What I <span {acc}>Learned</span></h2>\n'
           f'    <div class="check-grid" id="checklist-{D["n"]}" style="max-width:540px;margin:1.2rem auto 0;display:flex;flex-direction:column;gap:.5rem;text-align:left">\n{checks}    </div>',
           inner_style='text-align:center')

    # BADGE
    sb.add('slide slide-dark', 7, D['t']['badge'],
           f'    <div class="chapter-label">Lesson Complete</div>\n'
           f'    <div class="badge-card">\n'
           f'      <div class="badge-icon">\n'
           f'        <div class="badge-circle"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2l2.4 7.4H22l-6 4.6 2.3 7.4-6.3-4.6L5.7 21.4 8 14 2 9.4h7.6z"/></svg></div>\n'
           f'        <div class="sparkles"><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div></div>\n'
           f'      </div>\n'
           f'      <h2 class="slide-heading" style="color:#fff">{D["badge_name"]} <span {acc}>Earned!</span></h2>\n'
           f'      <p style="color:rgba(255,255,255,.78);font-size:1rem;margin-top:.5rem">{D["badge_p"]}</p>\n'
           f'      <p style="color:rgba(255,255,255,.82);font-size:.85rem;margin-top:1.5rem">Lesson {D["n"]} -- Complete.</p>\n'
           f'      <p style="color:var(--accent-light);font-size:.9rem;margin-top:.5rem">Next lesson: {D["next_lesson"]}</p>\n'
           f'    </div>',
           inner_style='text-align:center')

    return sb.html(), sb.n


# -------------------- PRE-CLASS --------------------
def build_preclass(D):
    n = D['n']
    voc = D['vocab']
    words = [v[0] for v in voc]
    defs = [v[1] for v in voc]
    # matching answer = the pure english def (strip parenthetical PT)
    def clean_def(d):
        return re.sub(r'\s*\([^)]*\)\s*$', '', d).strip()
    match_pairs = [(w, clean_def(d)) for w, d in zip(words, defs)]
    all_defs = [p[1] for p in match_pairs]

    rng = random.Random(1000 + n)
    rows = ''
    for wi, (w, ans) in enumerate(match_pairs):
        opts = all_defs[:]
        # shuffle until answer not at same index as word
        for _ in range(50):
            rng.shuffle(opts)
            if opts.index(ans) != wi:
                break
        opt_html = '<option value="">Select...</option>' + ''.join(
            f'<option value="{o}">{o}</option>' for o in opts)
        rows += (f'        <div class="match-row" data-answer="{ans}"><span class="match-word" style="flex:0 0 150px">{w}</span>'
                 f'<select style="flex:1;width:100%" onchange="checkMatch(this)">{opt_html}</select></div>\n')

    vocab_cards = ''
    for w, d, ex in voc:
        vocab_cards += (f'        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header">'
                        f'<span class="vocab-card-word">{w}</span><span class="vocab-card-dot"> -- </span>'
                        f'<span class="vocab-card-def">{d}</span></div>'
                        f'<div class="vocab-card-example">"{ex}"</div></div>'
                        f'<button class="audio-btn" onclick="speakText(\'{w}\',this)">Listen</button></div>\n')

    # context quiz
    ctx_quiz = ''
    for q, opts in D['context_quiz']:
        oh = ''
        for letter, txt, corr in opts:
            oh += (f'<div class="quiz-option" onclick="selectQuiz(this)" data-correct="{str(corr).lower()}"><span class="option-letter">{letter}</span> {txt}</div>\n')
        ctx_quiz += (f'      <div class="quiz-item"><div class="quiz-question">{q}</div><div class="quiz-options">\n{oh}</div></div>\n')

    # grammar tip table
    tip_rows = ''
    for i, (form, use, ex) in enumerate(D['tip_rows']):
        bg = 'background:var(--bg-elevated);' if i % 2 == 1 else ''
        border = 'border-bottom:1px solid var(--border);' if i < len(D['tip_rows']) - 1 else 'border-bottom:1px solid var(--border);'
        tip_rows += (f'          <tr style="{border}{bg}"><td style="padding:.6rem;font-weight:600">{form}</td>'
                     f'<td style="padding:.6rem">{use}</td><td style="padding:.6rem">{ex}</td></tr>\n')

    # fill
    fill = ''
    for pre, ans, hint, phrase, post in D['fill']:
        fill += (f'      <div class="fill-blank-item"><div class="fill-blank-sentence">{pre}'
                 f'<input class="blank-input" data-answer="{ans}" data-hint="{hint}" data-phrase="{phrase}" placeholder="___">{post}</div>'
                 f'<button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>'
                 f'<button class="check-btn" onclick="checkBlank(this)">Check</button></div>\n')

    # order
    order_items = ''
    order = D['order']
    order_display = list(enumerate(order, 1))
    shuffled = order_display[:]
    rng.shuffle(shuffled)
    for correct_pos, text in shuffled:
        order_items += (f'        <div class="order-item" draggable="true" data-order="{correct_pos}" onclick="selectOrderItem(this,\'order-l{n}\')">'
                        f'<span class="order-num">?</span><span class="order-text">{text}</span>'
                        f'<span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l{n}\')">&#9650;</button>'
                        f'<button class="arrow-btn" onclick="moveItem(this,1,\'order-l{n}\')">&#9660;</button></span></div>\n')

    # speech
    speech = ''
    for en, pt in D['speech']:
        speech += (f'      <div class="speech-card" data-phrase="{en}">\n'
                   f'        <div class="speech-phrase">{en}</div>\n'
                   f'        <div class="speech-translation">{pt}</div>\n'
                   f'        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>\n'
                   f'        <div class="speech-result"></div>\n'
                   f'      </div>\n')

    # situational quiz
    sit_quiz = ''
    for q, opts in D['quiz']:
        oh = ''
        for letter, txt, corr in opts:
            oh += (f'<div class="quiz-option" onclick="selectQuiz(this)" data-correct="{str(corr).lower()}"><span class="option-letter">{letter}</span> {txt}</div>\n')
        sit_quiz += (f'      <div class="quiz-item"><div class="quiz-question">{q}</div><div class="quiz-options">\n{oh}</div></div>\n')

    # survival card
    surv = ''
    for i, (en, pt) in enumerate(D['survival'], 1):
        surv += (f'      <div class="survival-phrase"><span class="sp-num">{i}</span><span class="sp-en">{en}</span>'
                 f'<span class="sp-pt">{pt}</span><button class="btn btn-listen" onclick="speakText(\'{en}\',this)">&#9835;</button></div>\n')

    html = f'''<div class="lesson-card" id="ex-lesson-{n}">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('{D["bg_lesson_card"]}')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Aula {n:02d} -- Pre-class</div>
      <h3>{D["preclass_title"]}</h3>
      <div class="lesson-desc">{D["preclass_desc"]}</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="{n}" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="{n}">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ouça cada palavra e leia o exemplo. Toque em Listen para escutar.</p>
      <div class="vocab-cards">
{vocab_cards}      </div>
    </div>
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Relacione cada palavra com a definição correta.</p>
      <div class="match-grid" id="match-l{n}">
{rows}      </div>
    </div>
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Leia o texto e responda às perguntas.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>{D["context"]}</p>
      </div>
{ctx_quiz}    </div>
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- {D["tip_title"]}</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">{D["tip_sub"]}</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Use / Uso</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
{tip_rows}        </tbody>
      </table></div>
    </div>
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete cada frase com a forma correta. Toque em Listen para ouvir a frase inteira.</p>
{fill}    </div>
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Conversation in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">{D["order_intro"]}</p>
      <div class="order-container" id="order-l{n}">
{order_items}      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l{n}')">Check Order</button>
    </div>
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ouça cada frase e depois grave você mesma dizendo-a.</p>
{speech}    </div>
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Escolha a melhor resposta para cada situação real de trabalho.</p>
{sit_quiz}    </div>
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Grave você mesma respondendo à pergunta abaixo. Não há resposta certa ou errada.</p>
      <div class="think-card">
        <div class="think-question">{D["think"]}</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-{n}"></div>
      </div>
    </div>
    <div class="survival-card">
      <h4>Survival Card -- Lesson {n}</h4>
{surv}    </div>
  </div>
</div>
'''
    return html


# -------------------- COMPLEMENTARY --------------------
def build_complementary(D):
    n = D['n']
    SVG = {
        'series': '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="var(--accent)" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="2.18" ry="2.18"/><path d="M7 2v20"/><path d="M17 2v20"/><path d="M2 12h20"/><path d="M2 7h5"/><path d="M2 17h5"/><path d="M17 17h5"/><path d="M17 7h5"/></svg>',
        'podcast': '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="var(--accent)" stroke-width="2"><path d="M3 18v-6a9 9 0 0118 0v6"/><path d="M21 19a2 2 0 01-2 2h-1a2 2 0 01-2-2v-3a2 2 0 012-2h3zM3 19a2 2 0 002 2h1a2 2 0 002-2v-3a2 2 0 00-2-2H3z"/></svg>',
        'youtube': '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="var(--accent)" stroke-width="2"><path d="M22.54 6.42a2.78 2.78 0 00-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 00-1.94 2A29 29 0 001 11.75a29 29 0 00.46 5.33A2.78 2.78 0 003.4 19.1c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 001.94-2 29 29 0 00.46-5.25 29 29 0 00-.46-5.43z"/><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02"/></svg>',
    }
    label = {'series': 'Series', 'podcast': 'Podcast', 'youtube': 'YouTube'}
    action = {'series': 'Watch', 'podcast': 'Listen', 'youtube': 'Watch on YouTube'}
    cards = ''
    for kind, title, desc, tip, link in D['media']:
        cards += f'''
<div class="media-card-wrapper" data-media="l{n}-{kind}">
  <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
  <div class="media-card">
    <div class="media-thumb">{SVG[kind]}</div>
    <div class="media-info">
      <div class="media-type">{label[kind]}</div>
      <h5>{title}</h5>
      <p>{desc}</p>
      <p class="media-tip">{tip}</p>
      <a href="{link}" target="_blank" rel="noopener" style="display:inline-block;margin-top:.5rem;font-size:.75rem;color:var(--accent);font-weight:600;text-decoration:none;border-bottom:1px solid var(--accent)">{action[kind]} &#8599;</a>
    </div>
  </div>
</div>
'''
    return cards


# -------------------- CONFIG --------------------
def build_config(D, slide_count):
    n = D['n']
    inclass = {'vocab': [{
        'kind': 'matching', 'title': 'Match each word to its meaning',
        'words': [[str(i + 1), v[0]] for i, v in enumerate(D['vocab'])],
        'defs': [[chr(97 + i), re.sub(r'\s*\([^)]*\)\s*$', '', v[1]).strip()] for i, v in enumerate(D['vocab'])],
    }]}
    if D['reading']:
        inclass['reading'] = [
            {'kind': 'reading', 'rtitle': D['read_block']['rtitle'], 'paras': D['read_block']['paras'],
             'source': D['read_block']['source'], 'link': D['read_block']['link']},
            {'kind': 'gist', 'prompt': D['read_block']['gist_prompt'], 'choices': D['read_block']['gist_choices']},
        ]
        inclass['tf'] = [{'kind': 'tf', 'items': D['read_block']['tf']}]
    inclass['gapfill'] = [
        {'kind': 'gapfill', 'parts': D['gapfill_parts'], 'bank': D['gapfill_bank']},
        {'kind': 'vocabnote', 'text': D['vocabnote']},
    ]
    inclass['bank'] = [{'kind': 'bank', 'label': D['bank_label'], 'items': D['bank_items']}]
    inclass['lf'] = [
        {'kind': 'lf', 'title': D['lf_title'], 'items': D['lf_items']},
        {'kind': 'followup', 'text': D['lf_followup']},
    ]
    inclass['practice'] = [{'kind': 'scenarios', 'items': D['scenario_items']}]
    inclass['answerkey'] = [{'kind': 'answer', 'title': 'Reveal the answer key',
                             'list': D['answerkey_list'], 'note': D['answerkey_note']}]

    cfg = {
        'slug': 'andrea-aggio', 'student_name': 'Andrea Aggio', 'first_name': 'Andrea', 'gender': 'f',
        'program': 'Conversational English -- Travel &amp; Hospitality', 'total_aulas': 15,
        'palette': {'accent': ACCENT, 'accent_light': ACCENT_LIGHT},
        'header': ['B2 (Intermedi&#225;rio-Avan&#231;ado)', 'S&#227;o Paulo, SP',
                   'Diretora Comercial &mdash; Escape Turismo', '90 min &middot; Online'],
        'characters': {'andrea': 'ellen', D['partner_name']: 'arthur'},
        'hub_subtitle': 'Conversa&#231;&#227;o para Feiras Internacionais de Turismo &amp; Hotelaria',
        'stamps': [{'id': n, 'label': D['stamp_label'], 'img': D['stamp_img']}],
        'lesson': {
            'n': n, 'menu_num': f'{n:02d}', 'menu_title': D['menu_title'],
            'menu_desc': f'{D["menu_desc"]} -- {slide_count} slides',
            'subtitle': f'Aula {n} -- {D["short_title"]}',
            'title_tag': f'Professor View -- Andrea Aggio | Aula {n} -- {D["short_title"]}',
            'phases': D['phases'],
            'listenings': [{'file': li['file'], 'voice': li['voice'], 'text': li['text']} for li in D['listenings']],
            'inclass_blocks': inclass,
        },
        'hub': 'snippets',
    }
    return cfg


def main():
    n = int(sys.argv[1])
    ldir = os.path.join(HERE, f'andrea-aggio-aula{n}')
    spec = importlib.util.spec_from_file_location('data', os.path.join(ldir, 'data.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    D = mod.D
    assert D['n'] == n

    slides, count = build_slides(D)
    with open(os.path.join(ldir, 'slides.html'), 'w', encoding='utf-8') as f:
        f.write(slides)
    with open(os.path.join(ldir, 'preclass.html'), 'w', encoding='utf-8') as f:
        f.write(build_preclass(D))
    with open(os.path.join(ldir, 'complementary.html'), 'w', encoding='utf-8') as f:
        f.write(build_complementary(D))
    cfg = build_config(D, count)
    with open(os.path.join(ldir, 'config.json'), 'w', encoding='utf-8') as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)
    print(f'aula {n}: {count} slides, {len(D["vocab"])} vocab; wrote slides/preclass/complementary/config')


if __name__ == '__main__':
    main()
