# -*- coding: utf-8 -*-
"""Monta o material do intensivo da Rita a partir do shell do molde + do conteudo.

    python3 build.py

Emite DOIS arquivos de uma fonte so:
    public/intensivo/rita-rodrigues.html        visao do professor
    public/intensivo/rita-rodrigues-aluna.html  visao da aluna

A divisao e mecanica: sai do arquivo do professor tudo que e [data-view="aluno"], e do
arquivo da aluna tudo que e [data-view="professor"]. Nao ha um terceiro lugar onde a
divergencia possa nascer -- o que a aluna nao pode ver simplesmente NAO ESTA no arquivo
dela, e nao a um Ctrl+U de distancia.
"""
import json, os, re, sys, io

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import render as R
from content_aulas import AULAS, ESTAGIOS

RAIZ = os.path.abspath(os.path.join(AQUI, '..', '..'))
SAIDA_PROF = os.path.join(RAIZ, 'public', 'intensivo', 'rita-rodrigues.html')
SAIDA_ALUNA = os.path.join(RAIZ, 'public', 'intensivo', 'rita-rodrigues-aluna.html')

import notas as N

def deck_da_aula(a):
    n = a['n']
    t = []
    add = t.append
    nota = lambda i: N.monta(a, i)

    # 1 - abertura
    add(R.tela(n, 1, 1, 'slide-open',
        R.abertura('Lesson %02d &middot; %s' % (n, a['data']), a['titulo'], a['sub']), nota(1)))

    # 2 - o que este bloco tem de fazer
    corpo = '\n'.join([R.pill('1 &middot; What this lesson has to do'),
                       R.heading(a['nav'][1]),
                       R.brief(a['brief']),
                       R.split('Before your <span class="accent">first version</span>',
                               R.subprompt('Answer out loud. Nothing is corrected yet.') + '\n' + R.qlist(a['perguntas']))])
    add(R.tela(n, 2, 1, 'slide-dark', corpo, nota(2)))

    # 3 - o que torna isto dificil (tabela: o que acontece x o que faz com voce)
    cab, linhas = a['riscos_tab']
    corpo = '\n'.join([R.pill('2 &middot; What makes this hard'),
                       R.heading('Four things that can <span class="accent">interrupt you</span>'),
                       R.tabela(cab, linhas, largura=560),
                       R.pergunta('Which one worries you most?')])
    add(R.tela(n, 3, 2, 'slide-light', corpo, nota(3)))

    # 4 - primeira versao
    tit, sub, prompt = a['tentativa']
    corpo = '\n'.join([R.pill('3 &middot; Your first version'), R.heading(tit), R.lead(sub), R.pergunta(prompt)])
    add(R.tela(n, 4, 3, 'slide-dark', corpo, nota(4)))

    # 5 - uma forma de dizer
    corpo = '\n'.join([R.pill('3 &middot; One way it can sound'),
                       R.heading(a['modelo_t']),
                       '    <div class="brief">%s</div>' % ''.join('<p class="rp-line">%s</p>' % x for x in a['modelo_txt']),
                       R.pergunta(a['modelo_q'])])
    add(R.tela(n, 5, 3, 'slide-light', corpo, nota(5)))

    # 6 - as cinco linhas: o mapa de fala
    corpo = '\n'.join([R.pill('4 &middot; Five lines you can reuse'),
                       R.heading(a['linhas_t']),
                       R.subprompt('Lesson %02d &middot; speech map &mdash; it stays with you, today and on the day.' % n),
                       R.frases(a['linhas'])])
    add(R.tela(n, 6, 4, 'slide-light', corpo, nota(6)))

    # 7 - quando algo da errado
    corpo = '\n'.join([R.pill('4 &middot; When something goes wrong'),
                       R.heading(a['apoio_t']),
                       R.frases(a['apoio'])])
    add(R.tela(n, 7, 4, 'slide-light', corpo, nota(7)))

    # 8 - mude uma coisa
    corpo = '\n'.join([R.pill('5 &middot; Change one thing'),
                       R.heading(a['ensaio_t']),
                       R.lead('You name the change, she says the line. Never the same repetition twice.'),
                       R.reveals(a['ensaio'])])
    add(R.tela(n, 8, 5, 'slide-light', corpo, nota(8)))

    # 9 - mensagem essencial, depois os detalhes
    corpo = '\n'.join([R.pill('5 &middot; Building it'),
                       R.heading(a['mapa_t']),
                       R.lead(a['mapa_lead']),
                       R.mapa(a['mapa'])])
    add(R.tela(n, 9, 5, 'slide-dark', corpo, nota(9)))

    # 10 - a coisa real
    tit, cond, blocos, kw = a['perf']
    corpo = '\n'.join([R.pill('6 &middot; The real thing'), R.heading(tit), R.lead(cond),
                       R.roleplay(blocos, kw),
                       R.botao_bloco('l%dmapa' % n, 'Your speech map'),
                       R.split('Your <span class="accent">speech map</span>',
                               R.frases([(x[0], '') for x in a['linhas']]), 'l%dmapa' % n)])
    add(R.tela(n, 10, 6, 'slide-dark', corpo, nota(10)))

    # 11 - feedback e retask focado, na mesma tela
    corpo = '\n'.join([R.pill('7 &middot; Feedback and focused retask'),
                       R.heading('One thing that worked, <span class="accent">one thing to change</span>'),
                       R.quadro_feedback(n),
                       R.botao_bloco('l%dcmp' % n, 'Same fact, two ways', condicional=True),
                       R.split('Same fact, <span class="accent">two ways</span>', R.comparacao(a['cmp']), 'l%dcmp' % n),
                       '    <div class="close-block" style="margin-top:var(--space-4h)">'
                       '<h5>8 &middot; Focused retask</h5><p class="cb-sub">%s</p></div>' % a['retask']])
    add(R.tela(n, 11, 7, 'slide-light', corpo, nota(11)))

    # 12 - fecho
    blocos = ''.join('<div class="close-block"><h5>%s</h5><p class="cb-sub">%s</p></div>' % (t_, d)
                     for t_, d in a['fecho'])
    corpo = '\n'.join(['    <p class="chapter-label" style="text-align:center">8 &middot; Close</p>',
                       '    <h2 class="slide-title" style="text-align:center">%s</h2>' % R.titulo(a['fecho_t']),
                       '    <div class="close-flow">%s' % blocos,
                       '      <div class="close-block"><h5>What we worked on today</h5><div id="recapList%d"></div></div>' % n,
                       '      <div class="close-block"><h5>How confident do you feel right now?</h5><div id="confList%d"></div></div>' % n,
                       '    </div>',
                       R.subprompt(a['proxima'])])
    add(R.tela(n, 12, 8, 'slide-dark', corpo, nota(12)))
    return ''.join(t)

def decks():
    return '\n'.join('<!-- ================= AULA %d &mdash; %s ================= -->\n%s'
                     % (n, AULAS[n]['data'], deck_da_aula(AULAS[n])) for n in sorted(AULAS))


# ------------------------------------------------------------------ pre-class
from content_pre import PRE
from content_post import POST
from content_perfil import (ALUNO, CICLO, ARTEFATO, CABECALHO, PERFIL_PROF, PLANNING_ALUNO,
                            SYLLABUS, PREP, _MARGEM as MARGEM)

def _sec(rotulo_pt, n, instr, corpo):
    """Uma atividade do pre-class, no formato da regua: o rotulo da FUNCAO em portugues
    (do professor) e 'Activity N' em ingles (dela) -- cada um sai no arquivo do seu papel."""
    return ('  <div class="exercise-section">\n'
            '    <p class="eyebrow" data-view="professor">%d &middot; %s</p>\n'
            '    <p class="eyebrow" data-view="aluno" lang="en">Activity %d</p>\n'
            '    <div lang="en">\n      <p class="task-instr">%s</p>\n%s    </div>\n'
            '  </div>\n' % (n, rotulo_pt, n, instr, corpo))

def _doc(doc):
    if not doc:
        return ''
    t, linhas = doc
    return ('      <div class="callout rule-box doc-block"><span class="callout-title">%s</span>%s</div>\n'
            % (t, '<br>'.join(linhas)))

def ex_html(n, k, e):
    """Um exercicio do pre-class. O id carrega a aula: l3q2 e a atividade 2 da aula 3."""
    ident = 'l%dq%d' % (n, k)
    instr = e['instr']
    def fecha(corpo):
        return _sec(e['t'], k, instr, corpo)

    if e['k'] == 'multi':
        ops = ''.join('<div class="quiz-option" data-ok="%d" onclick="tog(this)"><span>%s</span></div>' % (ok, txt)
                      for txt, ok in e['ops'])
        return fecha(_doc(e.get('doc')) +
                 '      <div class="quiz-item"><div class="quiz-options" id="%s">%s</div>'
                 '<div class="rationale">%s</div></div>\n'
                 '      <button class="verify-all-btn ghost" onclick="selCheck(this,\'%s\')">Check</button>\n'
                 '      <div class="score-out" id="%s-out"></div>\n' % (ident, ops, e['rat'], ident, ident))

    if e['k'] in ('quiz', 'leitura'):
        letras = 'ABCDEF'
        def um(q, ops, rat, i=0):
            o = ''.join('<div class="quiz-option" onclick="pick(this,%d)"><span class="option-letter">%s</span>'
                        '<span>%s</span></div>' % (ok, letras[j], txt) for j, (txt, ok) in enumerate(ops))
            return ('      <div class="quiz-item"><p class="quiz-question">%s</p>'
                    '<div class="quiz-options">%s</div><div class="rationale">%s</div></div>\n' % (q, o, rat))
        texto = ('      <div class="callout rule-box"><span class="callout-title">Read</span>%s</div>\n' % e['texto']) if e['k'] == 'leitura' else ''
        perguntas = e['perguntas'] if 'perguntas' in e else [(e['q'], e['ops'], e['rat'])]
        return fecha(_doc(e.get('doc')) + texto + ''.join(um(*x) for x in perguntas))

    if e['k'] == 'match':
        defs = [d for _, d in e['pares']]
        ordem = [defs[i] for i in _embaralha(len(defs))]
        linhas = ''
        for i, (palavra, correta) in enumerate(e['pares']):
            ops = ''.join('<option value="%d">%s</option>' % (defs.index(d), d) for d in ordem)
            linhas += ('<div class="match-row"><span class="match-word">%d &middot; %s</span>'
                       '<select data-ok="%d" data-k="pre_%s_%d"><option value="" selected>&mdash;</option>%s</select></div>'
                       % (i + 1, palavra, defs.index(correta), ident, i, ops))
        return fecha('      <div class="match-grid" id="%s">%s</div>\n'
                     '      <button class="verify-all-btn ghost" onclick="mCheck(this,\'%s\')">Check</button>\n'
                     '      <div class="score-out" id="%s-out"></div>\n' % (ident, linhas, ident, ident))

    if e['k'] == 'gap':
        banco = ('      <p class="task-instr"><strong>%s</strong></p>\n'
                 % ' &middot; '.join(e['banco'])) if e.get('banco') else ''
        itens = ''.join('<div class="fill-blank-item"><span class="fill-blank-sentence">%d. %s'
                        '<input class="blank-input" data-ok="%s" placeholder="..." data-k="pre_%s_%d">%s</span></div>'
                        % (i + 1, a, resp, ident, i, b) for i, (a, resp, b) in enumerate(e['itens']))
        return fecha(banco +
                     '      <div id="%s">%s</div>\n'
                     '      <button class="verify-all-btn ghost" onclick="czCheck(this,\'%s\')">Check</button>\n'
                     '      <div class="score-out" id="%s-out"></div>\n' % (ident, itens, ident, ident))

    if e['k'] == 'pair':
        linhas = ''.join('<div class="pair-row" data-ok="%s"><span class="pair-word">%s</span>'
                         '<button class="pair-opt" data-v="a" onclick="ppPick(this)">%s</button>'
                         '<button class="pair-opt" data-v="b" onclick="ppPick(this)">%s</button></div>'
                         % (ok, frase, a, b) for frase, ok, a, b in e['linhas'])
        return fecha('      <div class="pair-grid" id="%s">%s</div>\n'
                     '      <button class="verify-all-btn ghost" onclick="ppCheck(this,\'%s\')">Check</button>\n'
                     '      <div class="score-out" id="%s-out"></div>\n' % (ident, linhas, ident, ident))

    if e['k'] == 'ord':
        total = len(e['linhas'])
        opts = ''.join('<option>%d</option>' % (i + 1) for i in range(total))
        emb = _embaralha(total)
        linhas = ''.join(
            '<div class="match-row"><select class="ord-sel" data-k="pre_%s_%d" aria-label="position">'
            '<option value="" selected>&ndash;</option>%s</select>'
            '<span class="ord-frase" data-a="%d">%s</span></div>'
            % (ident, i, opts, e['linhas'][emb[i]][1], e['linhas'][emb[i]][0]) for i in range(total))
        return fecha('      <div class="match-grid" id="%s">%s</div>\n'
                     '      <button class="verify-all-btn ghost" onclick="ordCheck(this,\'%s\')">Check</button>\n'
                     '      <div class="score-out" id="%s-out"></div>\n' % (ident, linhas, ident, ident))

    if e['k'] == 'escrita':
        campos = ''.join('<div class="fb-field"><label for="%s-%d">%d. %s</label>'
                         '<textarea id="%s-%d" class="writebox" data-k="pre_%s_%d" '
                         'oninput="preSave(this);autoCresce(this)" lang="en"></textarea></div>'
                         % (ident, i, i + 1, q, ident, i, ident, i) for i, q in enumerate(e['perguntas']))
        modelo = ''.join('<p class="rp-line">%s</p>' % m for m in e['modelo'])
        return fecha('      <p class="subprompt">%s</p>\n'
                     '      <div class="fb-board">%s</div>\n'
                     '      <div class="btn-bar" style="justify-content:flex-start;margin-top:var(--space-3)">'
                     '<button class="btn-ghost" onclick="toggleEl(\'%s-mod\',this,\'See two possible answers\',\'Hide the answers\')">'
                     'See two possible answers</button></div>\n'
                     '      <div id="%s-mod" style="display:none" class="callout ok">%s</div>\n'
                     % (e.get('aviso', 'Do not record anything &mdash; you will say these out loud in the lesson.'),
                        campos, ident, ident, modelo))

    raise SystemExit('tipo de exercicio desconhecido: ' + e['k'])

def _embaralha(n):
    """Ordem fixa e DIFERENTE da original (REGRA 24), sem random no build.

    Rotacao por k com 0<k<n: e sempre uma permutacao completa e nao deixa nenhum item na
    posicao original. A primeira versao usava (i*3+1)%n, que para n=6 repetia indices e
    servia quatro vezes a mesma definicao -- o matching so podia dar 2 de 6.
    """
    k = n // 2 + 1
    return [(i + k) % n for i in range(n)]

def preclass():
    bot = ''.join('<button class="%s" id="pcb%d" onclick="preSel(%d)"></button>'
                  % ('btn-primary' if n == 1 else 'btn-ghost', n, n) for n in sorted(AULAS))
    blocos = ''
    for n in sorted(AULAS):
        ex = ''.join(ex_html(n, k + 1, e) for k, e in enumerate(PRE[n]['ex']))
        blocos += ('  <div id="pc%d"%s>\n    <h3 class="sub"></h3>\n'
                   '    <p class="task-instr">%s</p>\n    <hr class="rule">\n%s'
                   '    <div class="btn-bar" style="justify-content:flex-start;margin-top:var(--space-4)">'
                   '<button class="btn-ghost" onclick="preResetAsk()">Clear my answers</button></div>\n  </div>\n'
                   % (n, '' if n == 1 else ' style="display:none"', PRE[n]['intro'], ex))
    return ('<div class="tab-content" id="tab-preclass" data-consulta="1">\n'
            '  <p class="eyebrow" data-view="professor">Antes da aula</p>\n'
            '  <p class="eyebrow" data-view="aluno">Before class</p>\n'
            '  <h2 class="sec">Pre-class</h2>\n'
            '  <div class="btn-bar" style="justify-content:flex-start;margin-bottom:var(--space-4)">%s</div>\n%s'
            % (bot, blocos)) + '</div>\n'

# ------------------------------------------------------------------ in-class
def cartao(n):
    a = AULAS[n]; p = PREP[n]
    antes = ''.join('<li>%s</li>' % x for x in p['antes'])
    obs = ''.join('<li>%s</li>' % x for x in p['observar'])
    aval = ''.join(
        '<div class="aval-item"><p class="aval-crit">%s</p><p class="aval-desc">%s</p>'
        '<div class="aval-escala" data-aval="af_l%d_%s"%s role="radiogroup" aria-label="%s"></div></div>'
        % (rot, desc, n, ch, ' data-esc="engaj"' if ch == 'engaj' else '', rot)
        for ch, rot, desc in [
            ('fala', 'Fala e intera&ccedil;&atilde;o', 'Manter e desenvolver a intera&ccedil;&atilde;o oral com coer&ecirc;ncia, clareza e participa&ccedil;&atilde;o ativa.'),
            ('escuta', 'Compreens&atilde;o auditiva', 'Compreender a pergunta, reagir de forma adequada e acompanhar a conversa.'),
            ('precisao', 'Precis&atilde;o do dado', 'Dizer o n&uacute;mero que tem, encaminhar o que n&atilde;o tem, sem inventar.'),
            ('engaj', 'Engajamento', 'Disposi&ccedil;&atilde;o para produzir, arriscar e retomar depois do erro.')])
    return ('      <div class="lesson-card" id="lc%d">\n'
            '        <div class="lc-head"><span class="lc-badge">Aula %02d</span><span class="lc-fw"></span>'
            '<span class="lc-status" id="lcst%d">N&atilde;o iniciada</span></div>\n'
            '        <h3 class="lc-title"></h3>\n'
            '        <p class="lc-desc">%s</p>\n'
            '        <p class="lc-meta"></p>\n'
            '        <div class="btn-bar" style="justify-content:flex-start;margin-top:var(--space-3)">\n'
            '          <button class="btn-ghost" data-painel="lcprep%d" aria-expanded="false" onclick="cartaoPainel(\'lcprep%d\',this)">Estrutura e prepara&ccedil;&atilde;o</button>\n'
            '          <button class="btn-primary" onclick="openLesson(%d)">Abrir a aula</button>\n'
            '          <button class="btn-ghost" data-view="professor" onclick="tgAbrir(%d,this)"><span>Abrir o <span lang="en">Teacher&rsquo;s Guide</span></span></button>\n'
            '          <button class="btn-ghost" data-painel="lcfb%d" aria-expanded="false" onclick="cartaoPainel(\'lcfb%d\',this)">Registro p&oacute;s-aula</button>\n'
            '        </div>\n'
            '        <p class="tg-aviso-cartao" id="tgAviso%d" data-view="professor" hidden>O navegador n&atilde;o abriu a janela. O Teacher&rsquo;s Guide continua dispon&iacute;vel dentro da aula, no bot&atilde;o do canto superior direito.</p>\n'
            '        <div id="lcprep%d" style="display:none;margin-top:var(--space-4)">\n'
            '          <h5 class="prep-h">A &middot; Objetivo e produto</h5>\n'
            '          <p class="prep-p"><strong>Objetivo comunicativo:</strong> %s</p>\n'
            '          <p class="prep-p"><strong>Produto principal:</strong> %s</p>\n'
            '          <p class="prep-p"><strong>Crit&eacute;rio:</strong> %s</p>\n'
            '          <h5 class="prep-h">B &middot; Percurso da aula</h5>\n'
            '          <p class="prep-p" data-lf="percurso"></p>\n'
            '          <p class="prep-p" data-lf="etapas"></p>\n'
            '          <p class="prep-p">%s</p>\n'
            '          <h5 class="prep-h">C &middot; Antes de abrir a aula</h5>\n          <ul class="prep-list">%s</ul>\n'
            '          <h5 class="prep-h">D &middot; O que observar</h5>\n          <ul class="prep-list">%s</ul>\n'
            '        </div>\n'
            '        <div id="lcfb%d" style="display:none;margin-top:var(--space-4)">\n'
            '          <div class="fb-grid">\n'
            '            <div class="fb-item"><label for="af%d-data">Data de realiza&ccedil;&atilde;o</label>'
            '<input type="date" id="af%d-data" class="blank-input" data-k="af_l%d_data" oninput="persSave(this)"></div>\n'
            '            <div class="fb-item"><label for="af%d-status">Status</label>'
            '<select id="af%d-status" data-k="af_l%d_status" onchange="persSave(this)"><option value="">N&atilde;o iniciada</option>'
            '<option value="Em andamento">Em andamento</option><option value="Realizada">Realizada</option></select></div>\n'
            '          </div>\n'
            '          <h5 class="prep-h">Desempenho &mdash; mesma escala nas seis aulas</h5>\n'
            '          <div class="aval-grid">%s</div>\n'
            '          <h5 class="prep-h">Evid&ecirc;ncia e a&ccedil;&atilde;o</h5>\n'
            '          <div class="fb-item"><label for="af%d-evi">O que a aluna efetivamente fez ou disse</label>'
            '<textarea id="af%d-evi" class="writebox" data-k="af_l%d_evidencia" oninput="persSave(this);autoCresce(this)"></textarea></div>\n'
            '          <div class="fb-item"><label for="af%d-dif">Dificuldade, impacto na comunica&ccedil;&atilde;o e linguagem retomada</label>'
            '<textarea id="af%d-dif" class="writebox" data-k="af_l%d_dificuldade" oninput="persSave(this);autoCresce(this)"></textarea></div>\n'
            '          <div class="fb-item"><label for="af%d-acao">Ajuste ou retask para a aula seguinte</label>'
            '<textarea id="af%d-acao" class="writebox" data-k="af_l%d_acao" oninput="persSave(this);autoCresce(this)"></textarea></div>\n'
            '          <h5 class="prep-h">Feedback para a aluna &mdash; em ingl&ecirc;s, ela l&ecirc; na aba Feedback</h5>\n'
            '          <div class="fb-item"><label for="sfb%d-w">What worked</label>'
            '<textarea id="sfb%d-w" class="writebox" data-k="sfb_l%d_worked" oninput="persSave(this);autoCresce(this);fbEspelha(this)" lang="en"></textarea></div>\n'
            '          <div class="fb-item"><label for="sfb%d-d">Keep developing</label>'
            '<textarea id="sfb%d-d" class="writebox" data-k="sfb_l%d_develop" oninput="persSave(this);autoCresce(this);fbEspelha(this)" lang="en"></textarea></div>\n'
            '          <div class="btn-bar" style="justify-content:flex-start;margin-top:var(--space-3)">'
            '<button class="btn-ghost" onclick="avalResetAsk(%d)">Limpar registro</button>'
            '<button class="btn-primary" onclick="avalSave(%d)">Confirmar registro</button></div>\n'
            '        </div>\n      </div>\n'
            % (n, n, n, a['desc'], n, n, n, n, n, n, n, n, p['objetivo'], p['produto'],
               p['criterio'], MARGEM, antes, obs,
               n, n, n, n, n, n, n, aval, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n))

def inclass():
    return ('<div class="tab-content active" data-view="professor" id="tab-inclass">\n'
            '  <p class="eyebrow">Modo apresenta&ccedil;&atilde;o</p>\n'
            '  <h2 class="sec">In-class &mdash; uma aula por cart&atilde;o</h2>\n'
            '  <div class="lesson-grid">\n%s  </div>\n'
            % ''.join(cartao(n) for n in sorted(AULAS))) + '</div>\n'

# ------------------------------------------------------------------ feedback
def feedback():
    bot = ''.join('<button class="%s" id="sfb%d" onclick="fbSel(%d)">Lesson %d</button>'
                  % ('btn-primary' if n == 1 else 'btn-ghost', n, n, n) for n in sorted(AULAS))
    blocos = ''.join(
        '  <div id="sf%d"%s>\n    <h3 class="sub"></h3>\n'
        '    <div class="brief" id="sf%d-box" style="display:none"><dl>'
        '<dt>What worked</dt><dd id="sf%d-worked">&mdash;</dd>'
        '<dt>Keep developing</dt><dd id="sf%d-develop">&mdash;</dd></dl></div>\n'
        '    <p class="subprompt" id="sf%d-empty">Feedback will be available after the lesson.</p>\n  </div>\n'
        % (n, '' if n == 1 else ' style="display:none"', n, n, n, n) for n in sorted(AULAS))
    return ('<div class="tab-content" data-view="aluno" id="tab-feedback">\n'
            '  <p class="eyebrow">After each lesson</p>\n  <h2 class="sec">Feedback</h2>\n'
            '  <div class="btn-bar" style="justify-content:flex-start;margin-bottom:var(--space-4)">%s</div>\n%s'
            % (bot, blocos)) + '</div>\n'

# ------------------------------------------------------------------ post-class
def postclass():
    bot = ''.join('<button class="%s" id="psb%d" onclick="postSel(%d)"></button>'
                  % ('btn-primary' if n == 1 else 'btn-ghost', n, n) for n in sorted(AULAS))
    blocos = ''
    for n in sorted(AULAS):
        a, po = AULAS[n], POST[n]
        linhas = ' &middot; '.join('<em>%s</em>' % x[0] for x in a['linhas'])
        apoio = ' &middot; '.join('<em>%s</em>' % x[0] for x in a['apoio'])
        vocab = ' &middot; '.join('<em>%s</em>' % v for v in po['vocab'])
        recap = ''.join('<tr><td style="width:170px"><strong>%s</strong></td><td>%s</td></tr>' % (k, v)
                        for k, v in [('Situation', po['situacao']), ('What you are doing', po['fazendo']),
                                     (po['titulo'], linhas), ('Keeping it going', apoio),
                                     ('Key vocabulary', vocab)])
        lac = ''.join('<div class="fill-blank-item"><span class="fill-blank-sentence">%d. %s'
                      '<input class="blank-input" data-ok="%s" placeholder="..." data-k="post_l%d_g%d">%s</span></div>'
                      % (i + 1, x, r, n, i, y) for i, (x, r, y) in enumerate(po['lacunas']))
        perg = ''.join('<div class="reveal-item" onclick="this.classList.toggle(\'revealed\')">'
                       '<div class="r-front">%d. %s</div><div class="r-back">%s</div></div>'
                       % (i + 1, q, r) for i, (q, r) in enumerate(po['perguntas']))
        blocos += (
          '  <div id="ps%d"%s>\n    <h3 class="sub"></h3>\n'
          '    <p class="eyebrow" data-view="professor">%s</p>\n'
          '    <p class="prep-p" data-view="professor">%s</p>\n'
          '    <p class="task-instr" data-view="aluno" lang="en">The first part is the lesson, once more, on your own. '
          'Everything after it is optional &mdash; open what interests you, and come back whenever you like.</p>\n'
          '    <div lang="en">\n'
          '      <p class="eyebrow" style="margin-top:var(--space-5)">Review the lesson</p>\n'
          '      <div class="exercise-section"><div class="section-header-row"><h4>Lesson recap</h4></div>\n'
          '        <p class="task-instr">A quick reference to the situation and the language from the lesson.</p>\n'
          '        <div class="tbl-wrap"><table class="data" style="min-width:520px"><tbody>%s</tbody></table></div>\n'
          '      </div>\n'
          '      <div class="exercise-section"><div class="section-header-row"><h4>Complete the five lines</h4></div>\n'
          '        <p class="task-instr">Use your speech map if you need it.</p>\n'
          '        <div id="pl%d">%s</div>\n'
          '        <button class="verify-all-btn ghost" onclick="czCheck(this,\'pl%d\')">Check</button>\n'
          '        <div class="score-out" id="pl%d-out"></div>\n'
          '      </div>\n'
          '      <div class="exercise-section"><div class="section-header-row"><h4>Three questions to answer out loud</h4></div>\n'
          '        <p class="task-instr">Answer out loud, then open the answer to compare.</p>\n%s\n'
          '      </div>\n'
          '      <p class="eyebrow" style="margin-top:var(--space-5h)">Optional practice</p>\n'
          '      <div class="exercise-section"><div class="section-header-row"><h4>Speak More</h4>'
          '<span class="badge badge-open">Optional</span></div>\n'
          '        <p class="task-instr">%s You can listen to your recording and record again if you wish.</p>\n'
          '        <div class="rec-bar">'
          '<button class="audio-btn-sm" id="rec%d-start" onclick="rcStart(\'rec%d\')">Record</button>'
          '<button class="audio-btn-sm" id="rec%d-stop" style="display:none;background:var(--danger);border-color:var(--danger)" onclick="rcStop(\'rec%d\')">Stop</button>'
          '<span class="rec-time" id="rec%d-time">00:00</span></div>\n'
          '        <audio id="rec%d-player" controls style="display:none;width:100%%;margin-top:var(--space-3)"></audio>\n'
          '        <div id="rec%d-done" style="display:none;gap:var(--space-2h);margin-top:var(--space-2h);flex-wrap:wrap">'
          '<button class="audio-btn-sm ghost" onclick="rcBaixar(\'rec%d\')">Download</button>'
          '<button class="audio-btn-sm ghost" onclick="rcApaga(\'rec%d\')">Delete recording</button></div>\n'
          '        <div class="callout warn" id="rec%d-msg" style="display:none"></div>\n'
          '        <p class="subprompt"><strong>Local only.</strong> The recording stays on this computer. '
          'It is not sent to your teacher and it is not saved anywhere else.</p>\n'
          '      </div>\n'
          '      <div class="exercise-section"><div class="section-header-row"><h4>Write More</h4>'
          '<span class="badge badge-open">Optional</span></div>\n'
          '        <p class="task-instr">%s</p>\n'
          '        <textarea class="writebox" id="pw%d" data-k="post_l%d_write" placeholder="%s" '
          'oninput="preSave(this);autoCresce(this);pwCount(\'pw%d\',\'pw%d-out\',\'post_l%d_write\')"></textarea>\n'
          '        <div class="score-out" id="pw%d-out"></div>\n'
          '      </div>\n'
          '      <p class="eyebrow" style="margin-top:var(--space-5h)">%s</p>\n'
          '      <div class="exercise-section"><div class="section-header-row"><h4>One line to bring</h4></div>\n'
          '        <p class="task-instr">%s</p>\n'
          '        <textarea class="writebox" id="br%d" data-k="post_l%d_bring" '
          'oninput="preSave(this);autoCresce(this)"></textarea>\n'
          '      </div>\n    </div>\n  </div>\n'
          % (n, '' if n == 1 else ' style="display:none"', po['rotulo'], po['intro_pt'], recap,
             n, lac, n, n, perg, po['fala'], n, n, n, n, n, n, n, n, n, n,
             po['escrita'][0], n, n, po['escrita'][1], n, n, n, n,
             ('Before the meeting' if n == 6 else 'Before lesson %d' % (n + 1)), po['linha'], n, n))
    return ('<div class="tab-content" id="tab-postclass">\n'
            '  <p class="eyebrow" data-view="professor">Depois da aula</p>\n'
            '  <p class="eyebrow" data-view="aluno">After class</p>\n'
            '  <h2 class="sec">Post-class</h2>\n'
            '  <div class="btn-bar" style="justify-content:flex-start;margin-bottom:var(--space-4)">%s</div>\n%s'
            % (bot, blocos)) + '</div>\n'

# ------------------------------------------------------------------ cabecalho
def header():
    info = ''.join('<span>%s</span>' % x for x in CABECALHO['info'])
    return ('<header class="header">\n  <div class="header-content">\n'
            '    <div class="view-switch" role="group" aria-label="Vis&atilde;o do material">\n'
            '      <button class="view-btn on" id="vw-prof" onclick="setView(\'professor\')">Vis&atilde;o professor</button>\n'
            '      <button class="view-btn" id="vw-alu" onclick="setView(\'aluno\')">Vis&atilde;o aluno</button>\n'
            '    </div>\n'
            '    <span class="passport-badge" data-view="professor" data-lf="ciclo">%s</span>\n'
            '    <span class="passport-badge" data-view="aluno" data-lf="ciclo-aluno">%s</span>\n'
            '    <h1 data-lf="aluno-nome">%s %s</h1>\n'
            '    <p class="subtitle">%s</p>\n'
            '    <div class="student-info">%s</div>\n'
            '    <div class="progress-passport">\n'
            '      <div class="progress-label"><span id="hubRotulo">%s</span><span class="hub-nums">'
            '<span id="progressPercent">0 de %d realizadas</span>'
            '<span id="hubDisp" data-view="professor">%d dispon&iacute;veis</span></span></div>\n'
            '      <div class="progress-bar-outer"><div class="progress-bar-inner" id="progressBar" style="width:0%%"></div></div>\n'
            '      <div class="ciclo-mapa" id="cicloMapa" aria-label="Aulas do intensivo"></div>\n'
            '      <p class="ciclo-legenda" id="cicloLegenda"></p>\n'
            '    </div>\n  </div>\n</header>\n'
            % (CICLO['badge'], CICLO['badgeAluno'], ALUNO['nome'], ALUNO['sobrenome'],
               CABECALHO['subtitulo'], info, CICLO['rotulo'], CICLO['aulas'], len(AULAS)))

def planning():
    return ('<div class="tab-content" id="tab-planning">\n'
            '  <div data-view="professor">%s</div>\n  <div data-view="aluno">%s</div>\n</div>\n'
            % (PERFIL_PROF, PLANNING_ALUNO))

# ------------------------------------------------------------------ dados no JS
def js(v):
    if isinstance(v, str):
        return "'" + v.replace('\\', '\\\\').replace("'", "\\'") + "'"
    if isinstance(v, bool):
        return 'true' if v else 'false'
    if isinstance(v, (int, float)):
        return str(v)
    if isinstance(v, (list, tuple)):
        return '[' + ','.join(js(x) for x in v) + ']'
    if isinstance(v, dict):
        return '{' + ','.join('%s:%s' % (js(str(k)), js(x)) for k, x in v.items()) + '}'
    raise SystemExit('valor sem tradutor para JS: %r' % (v,))

def dados():
    lessons = {}
    for n, a in sorted(AULAS.items()):
        lessons[n] = {'n': n, 'bloco': 1, 'mod': a['mod'], 'cod': a['cod'],
                      'fwNome': 'Personalized Real-World English',
                      'tema': a['tema'], 'temaPre': a['temaPre'],
                      'data': a['data'], 'statusKey': 'af_l%d_status' % n,
                      'nav': a['nav'], 'stages': a['stages']}
    notas = {}
    for n in sorted(PRE):
        for k, e in enumerate(PRE[n]['ex']):
            if e.get('nota'):
                notas['%d-%d' % (n, k + 1)] = e['nota']
    fecho = {n: {'recap': a['recap'], 'conf': a['conf']} for n, a in sorted(AULAS.items())}
    return ('var STORE=%s;\nvar NAULAS=%d;\nvar ALUNO=%s;\nvar CICLO=%s;\nvar ARTEFATO=%s;\n'
            'var NUM_EXT={8:\'Oito\'};\nvar CONF_LB=[\'Not yet\',\'Getting there\',\'Comfortable\',\'Confident\'];\n'
            'var LESSONS=%s;\nvar PC_NOTAS=%s;\nvar FECHO=%s;\n'
            % (js('rita_intensivo_v1'), len(AULAS), js(ALUNO), js(CICLO), js(ARTEFATO),
               js(lessons), js(notas), js(fecho)))

# ------------------------------------------------------------------ montagem
def patches(s):
    """Ajustes no motor que o molde trazia cravados em quatro aulas."""
    # os construtores de fecho saem do registro, para qualquer numero de aulas
    i = s.index('var BUILDERS=['); j = s.index('];', i) + 2
    s = s[:i] + ("var BUILDERS=(function(){\n"
                 "  var a=[{h:'gdsort',also:[],f:function(){gdBuild();}},\n"
                 "         {h:'gdverify',also:[],f:function(){gdvBuild();}}],n;\n"
                 "  for(n=1;n<=NAULAS;n++)(function(k){\n"
                 "    a.push({h:'recapList'+k,also:['confList'+k],f:function(){closeBuild(k,FECHO[k].recap,FECHO[k].conf);}});\n"
                 "  })(n);\n  return a;\n})();") + s[j:]
    # a aula 1 deixa de ser caso especial na chave do fecho
    velho = "var d=load(),out=[],k,re=(n===1)?/^(rc|cf)\\d+$/:new RegExp('^l'+n+'(rc|cf)\\\\d+$');"
    assert velho in s, 'keysOf mudou de forma'
    s = s.replace(velho, "var d=load(),out=[],k,re=new RegExp('^l'+n+'(rc|cf)\\\\d+$');")
    # recapBuild era o fecho da aula 1 sozinho: sai inteiro
    i = s.index('function recapBuild(){'); j = s.index('\nfunction confPick(', i)
    s = s[:i] + s[j + 1:]
    # boot
    s = s.replace('deckInit(1); gdBuild(); gdvBuild(); cpBuild(); recapBuild();',
                  'deckInit(1); gdBuild(); gdvBuild(); cpBuild();')
    velho = 'closeBuild(2,RECAP2,CONF2); closeBuild(3,RECAP3,CONF3); closeBuild(4,RECAP4,CONF4); tabFromHash();'
    assert velho in s, 'boot do fecho mudou de forma'
    s = s.replace(velho, 'for(var _c=1;_c<=NAULAS;_c++)closeBuild(_c,FECHO[_c].recap,FECHO[_c].conf); tabFromHash();')
    # o post-class e caderno da aluna: sem isto as respostas dela caem no espaco do
    # professor, que load() nao devolve na visao dela -- ela escreve e nao ve mais
    velho = "if(k.indexOf('pre_')===0)return 'aluno';"
    assert velho in s, 'papelDe mudou de forma'
    s = s.replace(velho, velho + "\n  if(k.indexOf('post_')===0)return 'aluno';")
    # ESPELHO do feedback: a mesma chave sfb_l{n}_* existe na tela 7 da aula E no cartao.
    # O professor escreve onde estiver e o outro lugar acompanha -- e a aba da aluna repinta
    # no mesmo instante. Sem isto, haveria dois campos com o mesmo nome e valores diferentes.
    ancora = "function autoCresce(el){"
    assert ancora in s, 'autoCresce mudou de forma'
    s = s.replace(ancora, """function fbEspelha(origem){
  var k=origem.getAttribute('data-k'); if(!k)return;
  var els=document.querySelectorAll('[data-k="'+k+'"]'),i;
  for(i=0;i<els.length;i++){
    if(els[i]===origem)continue;
    els[i].value=origem.value;
    autoCresce(els[i]);
  }
  if(typeof sfBuild==='function')sfBuild();
}
""" + ancora)
    # BAIXAR a gravacao: a regua deixa a aluna levar o arquivo. Sem isto a gravacao morre
    # ao fechar a aba, e a promessa "you can listen back" vale so enquanto a pagina existe.
    ancora = "function rcApaga(id) {"
    assert ancora in s, 'rcApaga mudou de forma'
    s = s.replace(ancora, """function rcBaixar(id) {
  var r = _rc[id]; if (!r || !r.url) return;
  var a = document.createElement('a');
  a.href = r.url; a.download = id + '.webm';
  document.body.appendChild(a); a.click(); a.parentNode.removeChild(a);
}
""" + ancora)
    # o gabarito ganha duas linhas que a regua tem e o molde nao: a FONTE do fato (o deck
    # de marco de 2026, o site publico) e o que e SO RECONHECIMENTO -- aparece no texto e
    # nao se cobra em producao. Sem elas, o professor nao sabe o que pode exigir.
    velho = "      if(nota.duvida)h+=akLinha('Pode gerar d\\u00favida',nota.duvida);"
    assert velho in s, 'akBuild mudou de forma'
    s = s.replace(velho, velho + """
      if(nota.recon)h+=akLinha('S\\u00f3 reconhecimento',nota.recon);
      if(nota.fonte)h+=akLinha('Fonte do fato',nota.fonte);""")
    # ORDENAR: mecanica que o molde da Erica nao tem e a regua da Rita pede -- as cinco
    # linhas da abertura na ordem em que ela vai dize-las. A checagem e a mesma ideia do
    # matching (compara o escolhido com o esperado), e o gabarito le do mesmo lugar.
    ancora = "function czCheck(btn,id){"
    assert ancora in s, 'czCheck mudou de forma'
    s = s.replace(ancora, """function ordCheck(btn,id){
  if(preConsulta(btn))return;
  var host=document.getElementById(id); if(!host)return;
  var rows=host.querySelectorAll('.match-row'),n=0,i,sel,esp;
  for(i=0;i<rows.length;i++){
    sel=rows[i].querySelector('select'); esp=rows[i].querySelector('.ord-frase').getAttribute('data-a');
    rows[i].classList.remove('correct','wrong');
    if(!sel.value)continue;
    if(sel.value===esp){rows[i].classList.add('correct');n++;}
    else rows[i].classList.add('wrong');
  }
  var out=document.getElementById(id+'-out'); if(out)out.textContent=n+' / '+rows.length;
  var key=document.getElementById(id+'-key'); if(key&&n===rows.length)key.style.display='block';
}
""" + ancora)
    # o gabarito tambem le a ordem
    ancora = "  /* lacunas: o data-ok de cada campo, na ordem */"
    assert ancora in s, 'akExpected mudou de forma'
    s = s.replace(ancora, """  /* ordenar: a frase na posicao que o data-a declara */
  var od=sec.querySelectorAll('.ord-frase[data-a]');
  if(od.length){
    var o=[],pos=[];
    for(i=0;i<od.length;i++)pos.push([od[i].getAttribute('data-a'),od[i].textContent.trim()]);
    pos.sort(function(a,b){return parseInt(a[0],10)-parseInt(b[0],10);});
    for(i=0;i<pos.length;i++)o.push(pos[i][0]+'. '+pos[i][1]);
    r.push({t:'Ordem',v:o});
  }
""" + ancora)
    # o CSS da linha de ordenar: o select cabe a esquerda, a frase ocupa o resto
    s = s.replace('.phrase-list{', '.ord-sel{flex:0 0 auto;min-width:64px}\n.ord-frase{flex:1;font-size:.89rem;color:var(--text)}\n.phrase-list{')
    # a tarja do cabecalho sai do registro (intensivo nao e "Ciclo 1")
    s = s.replace("if(el)el.innerHTML='Ciclo '+CICLO.numero+' &middot; '+CICLO.aulas+' aulas &middot; '+CICLO.nivel;",
                  "if(el)el.innerHTML=CICLO.badge||('Ciclo '+CICLO.numero+' &middot; '+CICLO.aulas+' aulas &middot; '+CICLO.nivel);")
    s = s.replace("if(el)el.innerHTML='Cycle '+CICLO.numero+' &middot; '+CICLO.aulas+' lessons';",
                  "if(el)el.innerHTML=CICLO.badgeAluno||('Cycle '+CICLO.numero+' &middot; '+CICLO.aulas+' lessons');")
    return s

SLOTS = [('HEADER', header), ('PLANNING', planning),
         ('SYLLABUS', lambda: '<div class="tab-content" data-view="professor" id="tab-syllabus">\n'
                              + SYLLABUS + '</div>\n'),
         ('PRECLASS', preclass), ('INCLASS', inclass), ('FEEDBACK', feedback),
         ('POSTCLASS', postclass), ('DECKS', decks)]

def monta():
    s = open(os.path.join(AQUI, 'shell.html'), encoding='utf-8').read()
    for nome, fn in SLOTS:
        marca = '<!--SLOT:%s-->' % nome
        assert marca in s, 'slot ausente no shell: ' + nome
        s = s.replace(marca, fn())
    s = s.replace('/*SLOT:DADOS*/', dados())
    s = patches(s)
    cabeca = ('<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.min.js"></script>\n'
              '<script src="/lib/supabase-config.js"></script>\n')
    s = s.replace('</head>', cabeca + '</head>')
    ponte = ("<script>window.INTENSIVO={slug:'rita-rodrigues',papel:'__PAPEL__'};</script>\n"
             '<script src="/lib/intensivo-sync.js"></script>\n')
    s = s.replace('</body>', ponte + '</body>')
    assert 'SLOT:' not in s, 'sobrou marcador de slot'
    return s

# ------------------------------------------------- uma fonte, dois arquivos
def separa(doc, papel):
    """Tira do documento tudo que pertence ao OUTRO papel. Nao esconde: remove.

    So o MARKUP e varrido: o motor tambem monta rotulo com data-view dentro de string JS,
    e um varredor cego confundiria as duas coisas. As strings do motor sao tratadas depois,
    em rotulos_do_papel().
    """
    corte = doc.rindex('<script>', 0, doc.index('function switchTab('))
    s, cauda = doc[:corte], doc[corte:]
    fora = 'aluno' if papel == 'professor' else 'professor'
    saida, i = [], 0
    while True:
        m = re.search(r'<(?!body\b)(\w+)([^>]*\sdata-view="%s")' % fora, s[i:])
        if not m:
            saida.append(s[i:]); break
        ini = i + m.start()
        saida.append(s[i:ini])
        tag = m.group(1)
        # acha o fechamento correspondente, contando aninhamento da mesma tag
        p = i + m.end(); nivel = 1
        for t in re.finditer(r'<(/?)%s\b[^>]*?(/?)>' % tag, s[p:]):
            if t.group(2) == '/':
                continue
            nivel += -1 if t.group(1) else 1
            if nivel == 0:
                i = p + t.end(); break
        else:
            raise SystemExit('elemento data-view="%s" sem fechamento (<%s>)' % (fora, tag))
    return ''.join(saida) + rotulos_do_papel(cauda, papel)

def rotulos_do_papel(js_, papel):
    """Os rotulos que o motor monta em STRING tambem obedecem ao papel do arquivo.

    O motor concatena '<span data-view="professor">Aula N</span><span data-view="aluno">
    Lesson N</span>' para servir as duas visoes do mesmo documento. Num arquivo que JA e
    uma visao so, a metade do outro papel nao pode ser injetada e escondida: ela sai da
    string, e o rotulo sai direto.
    """
    prof = (papel == 'professor')
    alvo = re.compile(r"return '<span data-view=\"professor\">.*?</em>';", re.S)
    _r1 = ("return 'Aula '+n+' \\u00b7 '+fwLabel(n)+' \\u2014 <em>'+titulo+'</em>';" if prof
           else "return 'Lesson '+n+' \\u2014 <em>'+titulo+'</em>';")
    js_, k1 = alvo.subn(lambda m: _r1, js_)
    alvo2 = re.compile(r"el\.innerHTML='<span data-view=\"professor\">Aula '\+n\+' \\u00b7 '"
                       r"\+L\.mod\+'</span><span data-view=\"aluno\">Lesson '\+n\+'</span>'")
    _r2 = ("el.innerHTML='Aula '+n+' \\u00b7 '+L.mod" if prof else "el.innerHTML='Lesson '+n")
    js_, k2 = alvo2.subn(lambda m: _r2, js_)
    assert (k1, k2) == (1, 2), 'os rotulos do motor mudaram de forma: %r' % ((k1, k2),)
    assert 'data-view="aluno"' not in js_ and 'data-view="professor"' not in js_, \
        'sobrou rotulo com data-view dentro do motor'
    # a visao nao e mais escolha: e o arquivo
    velho = "setView(load().view==='aluno'?'aluno':'professor');"
    assert velho in js_, 'o boot da visao mudou de forma'
    js_ = js_.replace(velho, "setView('%s');" % papel)
    # o gabarito do pre-class e dado do PROFESSOR: no arquivo dela nao existe
    if not prof:
        js_, k3 = re.subn(r'^var PC_NOTAS=.*$', 'var PC_NOTAS={};', js_, count=1, flags=re.M)
        assert k3 == 1, 'PC_NOTAS nao encontrado para limpar'
        # ... e o construtor do gabarito tambem sai: ele deriva a RESPOSTA do proprio
        # exercicio, entao esvaziar PC_NOTAS nao bastaria - o painel nasceria com o
        # gabarito extraido, escondido no DOM dela.
        i = js_.index('function akBuild(){')
        j = js_.index('\nfunction akToggle(', i)
        js_ = js_[:i] + 'function akBuild(){/* o gabarito e do professor */}' + js_[j:]
    return js_

def tira_bloco(s, abertura):
    """Remove um elemento inteiro a partir do inicio da sua tag de abertura."""
    i = s.index(abertura)
    p = s.index('>', i) + 1
    nivel = 1
    for t in re.finditer(r'<(/?)div\b[^>]*?(/?)>', s[p:]):
        if t.group(2) == '/':
            continue
        nivel += -1 if t.group(1) else 1
        if nivel == 0:
            return s[:i] + s[p + t.end():]
    raise SystemExit('bloco sem fechamento: ' + abertura)

def escreve(caminho, s):
    with io.open(caminho, 'w', encoding='utf-8') as f:
        f.write(s)
    print('%-46s %8d bytes' % (os.path.relpath(caminho, RAIZ), len(s)))

if __name__ == '__main__':
    base = monta()
    prof = separa(base, 'professor')
    alu = separa(base, 'aluno').replace('<body data-view="professor">', '<body data-view="aluno">')
    # o seletor de visao nao faz sentido quando cada ARQUIVO ja e uma visao
    prof = tira_bloco(prof, '<div class="view-switch"').replace('__PAPEL__', 'professor')
    alu = tira_bloco(alu, '<div class="view-switch"').replace('__PAPEL__', 'aluno')
    escreve(SAIDA_PROF, prof)
    escreve(SAIDA_ALUNA, alu)
