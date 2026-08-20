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

NOTAS = {}
for _x in json.load(open(os.path.join(AQUI, 'notas_professor.json'), encoding='utf-8')):
    NOTAS[(_x['l'], _x['s'])] = _x['teacher']

def nota(n, tela_antiga):
    return NOTAS.get((n, tela_antiga), '')

NOTA_RETASK = (
    '<strong>Goal:</strong> To run the corrected part again, in context, so it lands where it '
    'will land on 31 August.<br><br>'
    '<strong>Run it:</strong> She starts with the part you just corrected &mdash; twenty to forty '
    'seconds &mdash; and then keeps going from there. Interrupt once, as the visitor would.<br><br>'
    '<strong>Check:</strong> The correction survives the interruption.<br><br>'
    '<strong>If needed:</strong> Cut the retask to the single sentence you corrected.<br><br>'
    '<strong>Move on when:</strong> She has said the corrected part once, cleanly, inside the flow.')

# ------------------------------------------------------------------ o deck
def deck_da_aula(a):
    n = a['n']
    t = []
    add = t.append

    # 1 - abertura
    add(R.tela(n, 1, 1, 'slide-open',
        R.abertura('Lesson %02d &middot; %s' % (n, a['data']), a['titulo'], a['sub']), nota(n, 1)))
    # 2 - o que a aula pede
    corpo = '\n'.join([R.pill('1 &middot; What this lesson is for'),
                       R.heading(a['tema'].replace('&amp;', '&amp;')),
                       R.brief(a['brief']),
                       R.split('Before your <span class="accent">first version</span>',
                               R.subprompt('Answer out loud. These answers are the draft of what you will say.') + '\n' +
                               R.qlist(a['perguntas']))])
    add(R.tela(n, 2, 1, 'slide-dark', corpo, nota(n, 2)))
    # 3 - onde quebra
    corpo = '\n'.join([R.pill('2 &middot; What can go wrong'),
                       R.heading('Where it <span class="accent">breaks</span>'),
                       R.lead('Three things that happen in a real meeting. Click each one to see what you do.'),
                       R.reveals(a['riscos'])])
    add(R.tela(n, 3, 2, 'slide-dark', corpo, nota(n, 3)))
    # 4 - primeira versao
    tit, sub, prompt = a['tentativa']
    corpo = '\n'.join([R.pill('3 &middot; Your first version'),
                       R.heading(tit), R.lead(sub), R.pergunta(prompt)])
    add(R.tela(n, 4, 3, 'slide-dark', corpo, nota(n, 4)))
    # 5 - o modelo
    corpo = '\n'.join([R.pill('3 &middot; One way to do it'),
                       R.heading('A model, <span class="accent">after your version</span>'),
                       R.subprompt('Read each one. Click to see what it does.'),
                       R.cards(a['modelo']),
                       R.pergunta(a['modelo_q'])])
    add(R.tela(n, 5, 3, 'slide-light', corpo, nota(n, 5)))
    # 6 - as linhas
    corpo = '\n'.join([R.pill('4 &middot; What you take with you'),
                       R.heading('The lines that <span class="accent">carry it</span>'),
                       R.lead('Say each one once. Change one element each time &mdash; never the same repetition twice.'),
                       R.frases(a['linhas'])])
    add(R.tela(n, 6, 4, 'slide-light', corpo, nota(n, 6)))
    # 7 - apoio / encaminhamento
    cab, linhas = a['apoio_tab']
    corpo = '\n'.join([R.pill('4 &middot; When you do not have it'),
                       R.heading(a['apoio_t']),
                       R.frases(a['apoio']),
                       R.botao_bloco('l%ds7tab' % n, 'What he hears'),
                       R.split('What he <span class="accent">hears</span>', R.tabela(cab, linhas), 'l%ds7tab' % n)])
    add(R.tela(n, 7, 4, 'slide-dark', corpo, nota(n, 7)))
    # 8 - ensaio, tres ouvintes
    corpo = '\n'.join([R.pill('5 &middot; Rehearsal'),
                       R.heading('Same thing, <span class="accent">different listener</span>'),
                       R.lead('Three rounds. What you keep is the shape; what changes is what the listener needs.'),
                       R.reveals(a['ensaio'])])
    add(R.tela(n, 8, 5, 'slide-light', corpo, nota(n, 8)))
    # 9 - ensaio com o mapa
    corpo = '\n'.join([R.pill('5 &middot; Rehearsal'),
                       R.heading('Now the whole thing, <span class="accent">with your map</span>'),
                       R.lead('One full run, with the map in front of you. Consulting it is not failure &mdash; you will have it on 31 August.'),
                       R.mapa(a['mapa'])])
    add(R.tela(n, 9, 5, 'slide-light', corpo, nota(n, 9)))
    # 10 - a coisa real
    tit, cond, blocos, kw = a['perf']
    corpo = '\n'.join([R.pill('6 &middot; The real thing'), R.heading(tit), R.lead(cond),
                       R.roleplay(blocos, kw)])
    add(R.tela(n, 10, 6, 'slide-dark', corpo, nota(n, 10)))
    # 11 - feedback
    corpo = '\n'.join([R.pill('7 &middot; Feedback'),
                       R.heading('How it <span class="accent">went</span>'),
                       R.quadro_feedback(n),
                       R.botao_bloco('l%dfbcheck' % n, 'Check the difference', condicional=True),
                       R.split('Same fact, <span class="accent">two ways</span>',
                               R.pergunta('Which one tells him more &mdash; and what does he do differently after each?') + '\n' +
                               R.comparacao(a['cmp']), 'l%dfbcheck' % n)])
    add(R.tela(n, 11, 7, 'slide-light', corpo, NOTAS.get((n, 11), '')))
    # 12 - retask
    tit, sub, blocos, kw = a['retask']
    corpo = '\n'.join([R.pill('8 &middot; Retask'), R.heading(tit), R.pergunta(sub),
                       R.roleplay(blocos, kw)])
    add(R.tela(n, 12, 8, 'slide-dark', corpo, NOTA_RETASK))
    # 13 - fecho
    corpo = R.fecho(n, a['fecho_t']) + '\n' + R.subprompt(a['proxima'])
    add(R.tela(n, 13, 8, 'slide-dark', corpo, nota(n, 12)))
    return ''.join(t)

def decks():
    return '\n'.join('<!-- ================= AULA %d &mdash; %s ================= -->\n%s'
                     % (n, AULAS[n]['data'], deck_da_aula(AULAS[n])) for n in sorted(AULAS))


# ------------------------------------------------------------------ pre-class
from content_pre import PRE
from content_post import POST
from content_perfil import ALUNO, CICLO, ARTEFATO, CABECALHO, PERFIL_PROF, PLANNING_ALUNO, SYLLABUS, PREP

def _sec(titulo, instr, corpo, badge=''):
    return ('  <div class="exercise-section">\n'
            '    <div class="section-header-row"><h4>%s</h4>%s</div>\n'
            '    <p class="task-instr">%s</p>\n%s\n  </div>\n' % (titulo, badge, instr, corpo))

def _doc(doc):
    if not doc:
        return ''
    t, linhas = doc
    return ('    <div class="callout rule-box doc-block"><span class="callout-title">%s</span>%s</div>\n'
            % (t, '<br>'.join(linhas)))

def ex_html(n, k, e):
    """Um exercicio do pre-class. O id de cada mecanica carrega a aula: pc3 e da aula 3."""
    ident = 'l%dq%d' % (n, k)
    t = e['t']; instr = e['instr']
    if e['k'] == 'multi':
        ops = ''.join('<div class="quiz-option" data-ok="%d" onclick="tog(this)"><span>%s</span></div>' % (ok, txt)
                      for txt, ok in e['ops'])
        corpo = (_doc(e.get('doc')) +
                 '    <div class="quiz-item"><div class="quiz-options" id="%s">%s</div>'
                 '<div class="rationale">%s</div></div>\n'
                 '    <button class="verify-all-btn ghost" onclick="selCheck(this,\'%s\')">Check</button>\n'
                 '    <div class="score-out" id="%s-out"></div>\n' % (ident, ops, e['rat'], ident, ident))
        return _sec('%d &middot; %s' % (k, t), instr, corpo)
    if e['k'] in ('quiz', 'leitura'):
        letras = 'ABCDEF'
        ops = ''.join('<div class="quiz-option" onclick="pick(this,%d)"><span class="option-letter">%s</span><span>%s</span></div>'
                      % (ok, letras[i], txt) for i, (txt, ok) in enumerate(e['ops']))
        texto = ('    <div class="callout rule-box"><span class="callout-title">Read</span>%s</div>\n' % e['texto']) if e['k'] == 'leitura' else ''
        corpo = (_doc(e.get('doc')) + texto +
                 '    <div class="quiz-item"><p class="quiz-question">%s</p>'
                 '<div class="quiz-options">%s</div><div class="rationale">%s</div></div>\n'
                 % (e['q'], ops, e['rat']))
        return _sec('%d &middot; %s' % (k, t), instr, corpo)
    if e['k'] == 'match':
        defs = [d for _, d in e['pares']]
        ordem = [defs[i] for i in _embaralha(len(defs))]
        linhas = ''
        for i, (palavra, correta) in enumerate(e['pares']):
            ops = ''.join('<option value="%d">%s</option>' % (defs.index(d), d) for d in ordem)
            linhas += ('<div class="match-row"><span class="match-word">%d &middot; %s</span>'
                       '<select data-ok="%d" data-k="pre_%s_%d"><option value="" selected>&mdash;</option>%s</select></div>'
                       % (i + 1, palavra, defs.index(correta), ident, i, ops))
        corpo = ('    <div class="match-grid" id="%s">%s</div>\n'
                 '    <button class="verify-all-btn ghost" onclick="mCheck(this,\'%s\')">Check</button>\n'
                 '    <div class="score-out" id="%s-out"></div>\n' % (ident, linhas, ident, ident))
        return _sec('%d &middot; %s' % (k, t), instr, corpo)
    if e['k'] == 'gap':
        itens = ''.join('<div class="fill-blank-item"><span class="fill-blank-sentence">%s'
                        '<input class="blank-input" data-ok="%s" placeholder="..." data-k="pre_%s_%d">%s</span></div>'
                        % (a, resp, ident, i, b) for i, (a, resp, b) in enumerate(e['itens']))
        corpo = ('    <div id="%s">%s</div>\n'
                 '    <button class="verify-all-btn ghost" onclick="czCheck(this,\'%s\')">Check</button>\n'
                 '    <div class="score-out" id="%s-out"></div>\n' % (ident, itens, ident, ident))
        return _sec('%d &middot; %s' % (k, t), instr, corpo)
    if e['k'] == 'pair':
        linhas = ''.join('<div class="pair-row" data-ok="%s"><span class="pair-word">%s</span>'
                         '<button class="pair-opt" data-v="a" onclick="ppPick(this)">%s</button>'
                         '<button class="pair-opt" data-v="b" onclick="ppPick(this)">%s</button></div>'
                         % (ok, frase, a, b) for frase, ok, a, b in e['linhas'])
        corpo = ('    <div class="pair-grid" id="%s">%s</div>\n'
                 '    <button class="verify-all-btn ghost" onclick="ppCheck(this,\'%s\')">Check</button>\n'
                 '    <div class="score-out" id="%s-out"></div>\n' % (ident, linhas, ident, ident))
        return _sec('%d &middot; %s' % (k, t), instr, corpo)
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
            '          <h5 class="prep-h">B &middot; Percurso da aula</h5>\n'
            '          <p class="prep-p" data-lf="percurso"></p>\n'
            '          <p class="prep-p" data-lf="etapas"></p>\n'
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
            '<textarea id="sfb%d-w" class="writebox" data-k="sfb_l%d_worked" oninput="persSave(this);autoCresce(this)" lang="en"></textarea></div>\n'
            '          <div class="fb-item"><label for="sfb%d-d">Keep developing</label>'
            '<textarea id="sfb%d-d" class="writebox" data-k="sfb_l%d_develop" oninput="persSave(this);autoCresce(this)" lang="en"></textarea></div>\n'
            '          <div class="btn-bar" style="justify-content:flex-start;margin-top:var(--space-3)">'
            '<button class="btn-ghost" onclick="avalResetAsk(%d)">Limpar registro</button>'
            '<button class="btn-primary" onclick="avalSave(%d)">Confirmar registro</button></div>\n'
            '        </div>\n      </div>\n'
            % (n, n, n, a['desc'], n, n, n, n, n, n, n, n, p['objetivo'], p['produto'], antes, obs,
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
        po = POST[n]
        recap = ''.join('<tr><td style="width:180px"><strong>%s</strong></td><td>%s</td></tr>' % (k, v) for k, v in po['recap'])
        ex = '<br>'.join(po['exemplos'])
        sit, top = po['fala']
        topicos = ''.join('<li>%s</li>' % x for x in top)
        prompt, placeholder = po['escrita']
        blocos += (
          '  <div id="ps%d"%s>\n    <h3 class="sub"></h3>\n'
          '    <div class="callout ok"><span class="callout-title">Optional</span>'
          'Everything here is optional. Choose what is useful and come back whenever you like.</div>\n'
          '    <p class="eyebrow" style="margin-top:var(--space-5)">Review the lesson</p>\n'
          '    <div class="exercise-section"><div class="section-header-row"><h4>Lesson recap</h4></div>\n'
          '      <p class="task-instr">A quick reference to the situation and the language from the lesson.</p>\n'
          '      <div class="tbl-wrap"><table class="data" style="min-width:520px"><tbody>%s</tbody></table></div>\n'
          '      <div class="callout rule-box"><span class="callout-title">Three short examples</span>%s</div>\n'
          '    </div>\n'
          '    <p class="eyebrow" style="margin-top:var(--space-5h)">Optional practice</p>\n'
          '    <div class="exercise-section"><div class="section-header-row"><h4>Speak More</h4>'
          '<span class="badge badge-open">About 90 seconds</span></div>\n'
          '      <p class="task-instr">Record it once. You can listen back and try again.</p>\n'
          '      <div class="callout rule-box"><span class="callout-title">The situation</span>%s</div>\n'
          '      <p class="task-instr">You could cover:</p>\n'
          '      <ul style="font-size:.88rem;line-height:1.75;padding-left:var(--space-4h);color:var(--text-mid)">%s</ul>\n'
          '      <div class="rec-bar">'
          '<button class="audio-btn-sm" id="rec%d-start" onclick="rcStart(\'rec%d\')">&#9679; Start recording</button>'
          '<button class="audio-btn-sm" id="rec%d-stop" style="display:none;background:var(--danger);border-color:var(--danger)" onclick="rcStop(\'rec%d\')">&#9632; Stop</button>'
          '<span class="rec-time" id="rec%d-time">00:00</span></div>\n'
          '      <audio id="rec%d-player" controls style="display:none;width:100%%;margin-top:var(--space-3)"></audio>\n'
          '      <div id="rec%d-done" style="display:none;gap:var(--space-2h);margin-top:var(--space-2h);flex-wrap:wrap">'
          '<button class="audio-btn-sm ghost" onclick="rcApaga(\'rec%d\')">Delete recording</button></div>\n'
          '      <div class="callout warn" id="rec%d-msg" style="display:none"></div>\n'
          '    </div>\n'
          '    <div class="exercise-section"><div class="section-header-row"><h4>Write More</h4></div>\n'
          '      <p class="task-instr">%s</p>\n'
          '      <textarea class="writebox" id="pw%d" data-k="post_l%d_write" placeholder="%s" '
          'oninput="persSave(this);autoCresce(this);pwCount(\'pw%d\',\'pw%d-out\',\'post_l%d_write\')"></textarea>\n'
          '      <div class="score-out" id="pw%d-out"></div>\n'
          '    </div>\n'
          '    <p class="eyebrow" style="margin-top:var(--space-5h)">%s</p>\n'
          '    <div class="exercise-section"><div class="section-header-row"><h4>One line to bring</h4></div>\n'
          '      <p class="task-instr">%s</p>\n'
          '      <textarea class="writebox" id="br%d" data-k="post_l%d_bring" oninput="persSave(this);autoCresce(this)"></textarea>\n'
          '    </div>\n  </div>\n'
          % (n, '' if n == 1 else ' style="display:none"', recap, ex, sit, topicos,
             n, n, n, n, n, n, n, n, n, prompt, n, n, placeholder, n, n, n, n,
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
