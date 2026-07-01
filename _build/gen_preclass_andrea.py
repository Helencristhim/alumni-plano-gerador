#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera preclass.html de UMA aula da Andrea a partir de um dict de conteudo.
Uso: python3 _build/gen_preclass_andrea.py N   (le _build/andrea-aggio-aula{N}/preclass_data.py)
Mantem a estrutura EXATA da aula 1 (5 etapas + order + pronunciation + quiz + free + survival).
"""
import html, importlib.util, os, sys, random

N = int(sys.argv[1])
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
DATA_PATH = os.path.join(ROOT, f'_build/andrea-aggio-aula{N}/preclass_data.py')
spec = importlib.util.spec_from_file_location('d', DATA_PATH)
d = importlib.util.module_from_spec(spec); spec.loader.exec_module(d)


def esc(t):
    return (t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            .replace('á','&#225;').replace('â','&#226;').replace('ã','&#227;').replace('à','&#224;')
            .replace('é','&#233;').replace('ê','&#234;').replace('í','&#237;').replace('ó','&#243;')
            .replace('ô','&#244;').replace('õ','&#245;').replace('ú','&#250;').replace('ç','&#231;')
            .replace('Á','&#193;').replace('É','&#201;').replace('Ê','&#202;').replace('Ã','&#195;')
            .replace('Ç','&#199;').replace('Ó','&#211;').replace('ü','&#252;'))


out = []
out.append(f'<div class="lesson-card" id="ex-lesson-{N}">')
out.append('  <div class="lesson-header" onclick="toggleLesson(this)">')
out.append(f'    <div class="lesson-header-img" style="background-image:url(\'{d.IMG}\')"></div>')
out.append('    <div class="lesson-header-content">')
out.append(f'      <div class="lesson-number">Aula {N:02d} -- Pre-class</div>')
out.append(f'      <h3>{esc(d.TITLE)}</h3>')
out.append(f'      <div class="lesson-desc">{esc(d.DESC)}</div>')
out.append(f'      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="{N}" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="{N}">0%</span></div>')
out.append('    </div>')
out.append('    <div class="expand-icon">&#9660;</div>')
out.append('  </div>')
out.append('  <div class="lesson-body">')

# Stage 1.1 Vocab
out.append('    <div class="exercise-section">')
out.append('      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>')
out.append('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a cada palavra e leia o exemplo. Toque em Listen para escutar.</p>')
out.append('      <div class="vocab-cards">')
for w, deff, ex in d.VOCAB:
    out.append(f'        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header"><span class="vocab-card-word">{esc(w)}</span><span class="vocab-card-dot"> -- </span><span class="vocab-card-def">{esc(deff)}</span></div><div class="vocab-card-example">"{esc(ex)}"</div></div><button class="audio-btn" onclick="speakText(\'{esc(w)}\',this)">Listen</button></div>')
out.append('      </div>')
out.append('    </div>')

# Stage 1.2 Matching (shuffled options)
alldefs = [sd for (_, sd) in d.MATCH]
out.append('    <div class="exercise-section">')
out.append('      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>')
out.append('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Relacione cada palavra com a defini&#231;&#227;o correta.</p>')
out.append(f'      <div class="match-grid" id="match-l{N}">')
for i, (w, sd) in enumerate(d.MATCH):
    opts = alldefs[:]
    rnd = random.Random(1000 * N + i)
    rnd.shuffle(opts)
    # garante ordem diferente da posicao original (REGRA 24)
    optspans = '<option value="">Select...</option>' + ''.join(
        f'<option value="{esc(o)}">{esc(o)}</option>' for o in opts)
    out.append(f'        <div class="match-row" data-answer="{esc(sd)}"><span class="match-word" style="flex:0 0 150px">{esc(w)}</span><select style="flex:1;width:100%" onchange="checkMatch(this)">{optspans}</select></div>')
out.append('      </div>')
out.append('    </div>')

# Stage 1.3 Grammar in Context
out.append('    <div class="exercise-section">')
out.append('      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
out.append('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Leia o texto e responda &#224;s perguntas.</p>')
out.append('      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">')
out.append(f'        <p>{d.CONTEXT}</p>')
out.append('      </div>')
for q, opts in d.CONTEXT_QUIZ:
    out.append('      <div class="quiz-item"><div class="quiz-question">' + esc(q) + '</div><div class="quiz-options">')
    for letter, txt, correct in opts:
        out.append(f'<div class="quiz-option" onclick="selectQuiz(this)" data-correct="{str(correct).lower()}"><span class="option-letter">{letter}</span> {esc(txt)}</div>')
    out.append('</div></div>')
out.append('    </div>')

# Stage 1.4 Grammar Tip
out.append('    <div class="exercise-section">')
out.append(f'      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- {esc(d.TIP_TITLE)}</h4><span class="badge badge-vocab">GRAMMAR</span></div>')
out.append(f'      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">{esc(d.TIP_SUB)}</p>')
out.append('      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">')
out.append('        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Use / Uso</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>')
out.append('        <tbody>')
for idx, row in enumerate(d.TIP_ROWS):
    bg = ';background:var(--bg-elevated)' if idx % 2 == 1 else ''
    if len(row) == 2:  # colspan row
        out.append(f'          <tr><td style="padding:.6rem;font-weight:600">{row[0]}</td><td style="padding:.6rem" colspan="2">{row[1]}</td></tr>')
    else:
        out.append(f'          <tr style="border-bottom:1px solid var(--border){bg}"><td style="padding:.6rem;font-weight:600">{row[0]}</td><td style="padding:.6rem">{esc(row[1])}</td><td style="padding:.6rem">{row[2]}</td></tr>')
out.append('        </tbody>')
out.append('      </table></div>')
out.append('    </div>')

# Stage 1.5 Fill in the blank
out.append('    <div class="exercise-section">')
out.append('      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>')
out.append('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete cada frase com a forma correta. Toque em Listen para ouvir a frase inteira.</p>')
for pre, ans, hint, phrase, post in d.FILL:
    out.append(f'      <div class="fill-blank-item"><div class="fill-blank-sentence">{esc(pre)}<input class="blank-input" data-answer="{esc(ans)}" data-hint="{esc(hint)}" data-phrase="{esc(phrase)}" placeholder="___">{esc(post)}</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>')
out.append('    </div>')

# Stage 2 Ordering
out.append('    <div class="exercise-section">')
out.append('      <div class="section-header-row"><h4>Stage 2: Put the Conversation in Order</h4><span class="badge badge-order">Order</span></div>')
out.append(f'      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">{esc(d.ORDER_INTRO)}</p>')
out.append(f'      <div class="order-container" id="order-l{N}">')
# emit in a scrambled display order but with data-order = correct position
display = list(enumerate(d.ORDER, start=1))
rnd = random.Random(7 * N)
scrambled = display[:]
rnd.shuffle(scrambled)
for correct_pos, text in scrambled:
    out.append(f'        <div class="order-item" draggable="true" data-order="{correct_pos}" onclick="selectOrderItem(this,\'order-l{N}\')"><span class="order-num">?</span><span class="order-text">{esc(text)}</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l{N}\')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,\'order-l{N}\')">&#9660;</button></span></div>')
out.append(f'      </div>')
out.append(f'      <button class="verify-all-btn" onclick="checkOrder(\'order-l{N}\')">Check Order</button>')
out.append('    </div>')

# Stage 3 Pronunciation
out.append('    <div class="exercise-section">')
out.append('      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>')
out.append('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Ou&#231;a cada frase e depois grave voc&#234; mesma dizendo-a.</p>')
for en, pt in d.SPEECH:
    out.append(f'      <div class="speech-card" data-phrase="{esc(en)}">')
    out.append(f'        <div class="speech-phrase">{esc(en)}</div>')
    out.append(f'        <div class="speech-translation">{esc(pt)}</div>')
    out.append('        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>')
    out.append('        <div class="speech-result"></div>')
    out.append('      </div>')
out.append('    </div>')

# Stage 4 Situational Quiz
out.append('    <div class="exercise-section">')
out.append('      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>')
out.append('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Escolha a melhor resposta para cada situa&#231;&#227;o real de trabalho.</p>')
for q, opts in d.QUIZ:
    out.append('      <div class="quiz-item"><div class="quiz-question">' + esc(q) + '</div><div class="quiz-options">')
    for letter, txt, correct in opts:
        out.append(f'<div class="quiz-option" onclick="selectQuiz(this)" data-correct="{str(correct).lower()}"><span class="option-letter">{letter}</span> {esc(txt)}</div>')
    out.append('</div></div>')
out.append('    </div>')

# Stage 5 Free Production
out.append('    <div class="exercise-section">')
out.append('      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>')
out.append('      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Grave voc&#234; mesma respondendo &#224; pergunta abaixo. N&#227;o h&#225; resposta certa ou errada.</p>')
out.append('      <div class="think-card">')
out.append(f'        <div class="think-question">{esc(d.THINK)}</div>')
out.append('        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>')
out.append(f'        <div id="think-result-{N}"></div>')
out.append('      </div>')
out.append('    </div>')

# Survival card
out.append('    <div class="survival-card">')
out.append(f'      <h4>Survival Card -- Lesson {N}</h4>')
for i, (en, pt) in enumerate(d.SURVIVAL, start=1):
    out.append(f'      <div class="survival-phrase"><span class="sp-num">{i}</span><span class="sp-en">{esc(en)}</span><span class="sp-pt">{esc(pt)}</span><button class="btn btn-listen" onclick="speakText(\'{esc(en)}\',this)">&#9835;</button></div>')
out.append('    </div>')

out.append('  </div>')
out.append('</div>')

open(os.path.join(ROOT, f'_build/andrea-aggio-aula{N}/preclass.html'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(f'wrote _build/andrea-aggio-aula{N}/preclass.html')
