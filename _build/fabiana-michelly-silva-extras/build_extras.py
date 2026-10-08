#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aba "Practice" da Fabiana Michelly Silva, 08/10/2026.

POR QUE EXISTE. A Helen pediu uma aba nova no hub da Fabiana com exercicios para
ela praticar, montados das ANALISES DE AULA dela (dashboard Analise de Aulas), a
partir de dois pontos de cada aula:
  - "Principais gaps"  = analysis.resumo_aluno.quadro_executivo.gaps
  - "Plano de estudo"  = analysis.resumo_aluno.plano_estudo
Um bloco por aula analisada. grammar_errors / correcoes / palavras_novas so
entram como o detalhe concreto por tras de um gap ou de um item do plano.

FONTE DO CONTEUDO: content.json ao lado (um objeto por aula, campo `analise` = id
em /api/analise?id=). O conteudo foi escrito em sessao, nao por API paga.

REGRAS QUE ESTE ARQUIVO SEGUE (mesmo contrato do _build/jose-eduardo-alves-extras)
- "In class you said" so cita fala que esta na analise (said / voce_disse).
- Ids proprios `fp-`, fora do updateProgress (barra e stamps nao mudam).
- So chama funcao que o hub ja tem. O insert_hub_extras recusa qualquer outra.
- Resposta certa sorteada, nunca na mesma posicao em sequencia.
- Nenhuma resposta, opcao certa, palavra, frase de pronuncia ou pergunta livre
  pode colidir com o resto do hub (loadState restaura por texto): checa_colisoes().
- Aula mais recente primeiro: e a que ela vai praticar agora.

USO:  python3 build_extras.py   (escreve practice.html ao lado e confere colisao)

COMO CRESCE: aula nova analisada = acrescentar a entrada em content.json e rodar
      python3 build_extras.py
      python3 ../model/insert_hub_extras.py --replace --hub public/{aluno,professor}/fabiana-michelly-silva.html \\
          --aba practice:_build/fabiana-michelly-silva-extras/practice.html:"Practice"
      ELEVENLABS_API_KEY=... python3 gen_audio_extras.py
"""
import json
import os
import random
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, '..', '..'))
HUB = os.path.join(RAIZ, 'public', 'aluno', 'fabiana-michelly-silva.html')
SLOT = 'practice'
IMG = 'https://images.unsplash.com/photo-'
# fotos que o hub dela ja usa (todas no ar), em rodizio
FOTOS = ['1454165804606-c3d57bc86b40', '1460925895917-afdab827c52f', '1494412574643-ff11b0a5c1c3',
         '1504384308090-c894fdcc538d', '1517048676732-d65bc937f952', '1521737604893-d14cc237f11d',
         '1526778548025-fa2f459cd5c1', '1531482615713-2afd69097998', '1551288049-bebda4e38f71',
         '1552664730-d307ca884978', '1553877522-43269d4ea984', '1556761175-5973dc0f32e7',
         '1573497491208-6b1acb260507', '1543286386-713bdd548da4']


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
            f'<span class="option-letter">{"ABCDE"[j]}</span> {esc(t)}</div>'
            for j, t in enumerate(opts))
        out += (f'      <div class="quiz-item"><div class="quiz-question">{esc(q)}</div>'
                f'<div class="quiz-options">{o}</div></div>\n')
    return out


def blanks(items):
    """(antes, resposta, depois, dica[, alternativa])"""
    out = ''
    for it in items:
        antes, resp, depois, dica = it[:4]
        alt = it[4] if len(it) > 4 and it[4] else None
        frase = f'{antes}{resp}{depois}'
        alt_attr = f' data-alt="{esc(alt)}"' if alt else ''
        dica = dica if dica.startswith('Hint:') else 'Hint: ' + dica
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
                 f'<span class="match-word" style="flex:0 0 170px">{esc(w)}</span>'
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


def foco(linhas):
    li = ''.join(f'<li style="margin-bottom:.35rem">{esc(x)}</li>' for x in linhas)
    return (f'    <div style="background:var(--bg-card);border:1px solid var(--border);border-left:3px solid var(--accent);'
            f'border-radius:8px;padding:1rem 1.1rem;margin-bottom:1.2rem">'
            f'<p style="font-size:.78rem;text-transform:uppercase;letter-spacing:2px;color:var(--accent);font-weight:600;margin-bottom:.5rem">'
            f'Your focus from this class</p>'
            f'<ul style="font-size:.9rem;line-height:1.6;padding-left:1.1rem;margin:0">{li}</ul></div>\n')


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
      <h3>{esc(titulo)}</h3>
      <div class="lesson-desc">{desc}</div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

{corpo}
  </div>
</div>
'''


def aba(titulo, intro, cards):
    return (f'<!-- ========== ABA SUPLEMENTAR: {titulo} (aditiva, fora do progresso) ========== -->\n'
            f'<div class="tab-content" id="tab-{SLOT}">\n'
            f'<div style="margin-bottom:1.2rem"><h2 style="font-size:1.25rem;margin-bottom:.4rem">{titulo}</h2>'
            f'<p style="font-size:.9rem;color:var(--text-dim);line-height:1.6">{intro}</p></div>\n'
            + ''.join(cards) +
            f'</div><!-- /tab-{SLOT} -->\n')


def class_card(i, C, sorteio):
    a = C['analise']
    corpo = (
        foco(C['foco'])
        + secao('Stage 1: Fix It', 'badge-quiz', 'Quiz',
                'Choose the best version. These come from your gaps in this class.', quiz(C['fix'], sorteio))
        + secao('Stage 2: Write It Right', 'badge-practice', 'Practice',
                'Write the missing words. Tap Listen to hear the full sentence.', blanks(C['write']))
        + secao('Stage 3: Words That Matter', 'badge-vocab', 'Vocabulary',
                'Expressions from your study plan. Match each one with its meaning.',
                matching(f'fp-match-{a}', C['words'], giro=i + 1))
        + secao('Stage 4: Say It', 'badge-speak', 'Speaking',
                'Listen, then record yourself. You get a word-by-word score.', speech(C['say']))
        + secao('Stage 5: Your Turn', 'badge-think', 'Reflection',
                'This is the speaking task from your study plan. Record your answer.',
                think(f'think-result-fp{a}', C['livre'])))
    return card(f'fp-class-{a}', f'Class of {C["data"]}', C['tema'],
                'Built from your class analysis: your gaps and your study plan.',
                FOTOS[i % len(FOTOS)], corpo)


# ════════════════════════════════════════════════════════════════════════════
# COLISAO: o loadState do hub restaura por texto, no documento inteiro.
# ════════════════════════════════════════════════════════════════════════════
def _assinaturas(html):
    txt = lambda s: re.sub(r'<[^>]+>', '', s).replace('&quot;', '"').replace('&amp;', '&').strip()
    a = {}
    a['blank'] = re.findall(r'class="blank-input"[^>]*data-answer="([^"]+)"', html)
    a['quiz'] = [txt(m)[:30] for m in re.findall(
        r'<div class="quiz-option"[^>]*data-correct="true">(.*?)</div>', html)]
    a['match'] = [txt(m) for m in re.findall(r'<span class="match-word"[^>]*>(.*?)</span>', html)]
    a['speech'] = re.findall(r'class="speech-card" data-phrase="([^"]+)"', html)
    a['think'] = [txt(m)[:40] for m in re.findall(r'<div class="think-question">(.*?)</div>', html)]
    a['id'] = re.findall(r'\sid="([^"]+)"', html)
    return {k: [x.lower() for x in v] if k == 'blank' else list(v) for k, v in a.items()}


def checa_colisoes(nova):
    hub = open(HUB, encoding='utf-8').read()
    hub = re.sub(r'<!-- ========== ABA SUPLEMENTAR.*?</div><!-- /tab-%s -->' % SLOT, '', hub, flags=re.S)
    velho = {k: set(v) for k, v in _assinaturas(hub).items()}
    erros = []
    a = _assinaturas(nova)
    for k, v in a.items():
        for x in set(v):
            if x in velho[k]:
                erros.append('%s colide com o hub: %r' % (k, x))
        rep = sorted(set(x for x in v if v.count(x) > 1))
        if rep:
            erros.append('%s repetido dentro da aba: %s' % (k, rep))
    return erros


def checa_conteudo(L):
    erros = []
    for C in L:
        a = C['analise']
        for campo, n in (('fix', 3), ('write', 4), ('words', 4), ('say', 2)):
            if len(C[campo]) != n:
                erros.append('%s: %s tem %d itens (esperado %d)' % (a, campo, len(C[campo]), n))
        for _, d in C['words']:
            if not re.search(r'\b(the|a|an|to|of|that|which|who|by|for|with|when|you|in|on|is|are|it)\b', d):
                erros.append('%s: definicao sem function word (GATE 8): %r' % (a, d))
        if '—' in json.dumps(C, ensure_ascii=False):
            erros.append('%s: travessao no texto' % a)
    return erros


def main():
    L = json.load(open(os.path.join(AQUI, 'content.json'), encoding='utf-8'))
    L = sorted(L, key=lambda C: C['analise'], reverse=True)       # mais recente primeiro
    erros = checa_conteudo(L)
    s = Sorteio('fabiana-michelly-silva/practice')
    html = aba('Practice',
               'Exercises made from the analysis of each of your classes: the gaps your teacher noticed and '
               'your study plan. One block per class, the most recent first. About fifteen minutes each.',
               [class_card(i, C, s) for i, C in enumerate(L)])
    erros += checa_colisoes(html)
    if erros:
        print('\n'.join(erros))
        sys.exit('ERRO: %d problema(s). Nada foi gravado.' % len(erros))
    with open(os.path.join(AQUI, 'practice.html'), 'w', encoding='utf-8') as f:
        f.write(html)
    print('ok  practice.html  %d aulas  %d bytes' % (len(L), len(html.encode('utf-8'))))


if __name__ == '__main__':
    main()
