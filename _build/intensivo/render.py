# -*- coding: utf-8 -*-
"""Componentes do molde Private Black, em funcoes.

Nao ha markup novo aqui: cada funcao emite EXATAMENTE as classes que o shell ja estiliza
e que o motor ja procura (.slide/.stage-pill/.brief/.reveal-item/.recap-item/...). Quem
escreve conteudo escolhe o COMPONENTE; a aparencia e o comportamento vem do molde.
"""

def esc(t):
    return (t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
             .replace('"', '&quot;'))

def _rich(t):
    """Texto do autor. E HTML: o conteudo ja vem com &mdash;, <em> e <span class="accent">.

    Escapar aqui foi tentado e imprimia a marcacao na tela do aluno. O unico lugar que
    ESCAPA e o atributo data-teacher, onde a nota do professor precisa atravessar como
    valor de atributo antes de virar innerHTML de novo.
    """
    while '**' in t:
        a = t.index('**')
        b = t.find('**', a + 2)
        if b < 0:
            break
        t = t[:a] + '<span class="accent">' + t[a + 2:b] + '</span>' + t[b + 2:]
    return t

def titulo(t):
    """Titulo de tela. O ultimo trecho entre ** vira o realce em cor."""
    return _rich(t)

# ---------------------------------------------------------------- telas do deck
def tela(n, i, stage, classe, corpo, teacher):
    return ('<div class="slide %s" data-slide="%d" data-lesson="%d" data-stage="%d" data-teacher="%s">\n'
            '  <div class="slide-inner">\n%s\n  </div>\n</div>\n' %
            (classe, i, n, stage, esc(teacher), corpo))

def abertura(kicker, titulo_html, sub):
    return ('    <p class="chapter-label">%s</p>\n'
            '    <h1 class="slide-title">%s</h1>\n'
            '    <p class="slide-subtitle">%s</p>' % (kicker, titulo(titulo_html), _rich(sub)))

def pill(t):
    return '    <span class="stage-pill">%s</span>' % t

def heading(t):
    return '    <h2 class="slide-heading">%s</h2>' % titulo(t)

def lead(t):
    return '    <p class="slide-lead">%s</p>' % _rich(t)

def pergunta(t):
    return '    <p class="slide-question">%s</p>' % _rich(t)

def subprompt(t):
    return '    <p class="subprompt">%s</p>' % _rich(t)

def brief(pares):
    linhas = ''.join('<dt>%s</dt><dd>%s</dd>' % (k, _rich(v)) for k, v in pares)
    return '    <div class="brief"><dl>%s</dl></div>' % linhas

def qlist(itens):
    return ('    <div class="qlist">%s</div>' %
            ''.join('<div class="q-item">%s</div>' % _rich(x) for x in itens))

def cards(itens, revelaveis=True):
    """itens: (rotulo, frente, verso|None)."""
    out = []
    for meta, frente, verso in itens:
        if verso and revelaveis:
            out.append('<div class="s-card reveal-card" onclick="this.classList.toggle(\'revealed\')">'
                       '<div class="s-meta">%s</div><h5>%s</h5>'
                       '<span class="rc-body">%s</span><span class="rc-hint">click to reveal</span></div>'
                       % (meta, _rich(frente), _rich(verso)))
        else:
            out.append('<div class="s-card"><div class="s-meta">%s</div><h5>%s</h5></div>'
                       % (meta, _rich(frente)))
    return '    <div class="card-row">%s</div>' % ''.join(out)

def frases(itens):
    """Linhas que a aluna leva. Estrutura identica a do molde: os tres filhos DIRETOS da
    .phrase-row (frase, funcao, acionador) -- o flex e do container, e um invólucro a mais
    cola a frase na glosa. O texto vai lido do DOM, nunca dentro da string do handler."""
    out = []
    for en, fn in itens:
        out.append('<div class="phrase-row"><span class="phrase-en">%s</span>%s'
                   '<button class="audio-btn-sm ghost" onclick="say('
                   'this.closest(\'.phrase-row\').querySelector(\'.phrase-en\').textContent,0.92,this)">'
                   '&#9654;</button></div>'
                   % (en, ('<span class="phrase-fn">%s</span>' % _rich(fn)) if fn else ''))
    return '    <div class="phrase-list">%s</div>' % ''.join(out)

def reveals(itens):
    return ''.join('    <div class="reveal-item" onclick="this.classList.toggle(\'revealed\')">'
                   '<div class="r-front">&#9656; %s</div><div class="r-back">%s</div></div>\n'
                   % (f, _rich(v)) for f, v in itens)

def roleplay(blocos, keywords):
    h = ''.join('<h5%s>%s</h5><p class="rp-line">%s</p>'
                % (' style="margin-top:var(--space-3h)"' if i else '', t, _rich(p))
                for i, (t, p) in enumerate(blocos))
    kw = ''.join('<span>%s</span>' % k for k in keywords)
    return '    <div class="roleplay-card">%s<div class="roleplay-kw">%s</div></div>' % (h, kw)

def mapa(passos):
    return ('    <div class="qlist">%s</div>' %
            ''.join('<div class="q-item">%s</div>' % _rich(p) for p in passos))

def split(titulo_html, corpo, ident=None):
    idp = (' id="%s" style="display:none"' % ident) if ident else ''
    return '    <div class="slide-split"%s>\n      <h3>%s</h3>\n%s\n    </div>' % (idp, titulo(titulo_html), corpo)

def botao_bloco(ident, rotulo, condicional=False):
    tag = '<span class="cond-tag" style="margin:0">Conditional</span>&nbsp; ' if condicional else ''
    return ('    <div class="btn-bar" style="margin-top:var(--space-4);justify-content:flex-start">'
            '<button class="verify-all-btn" onclick="abrirBloco(\'%s\',this)">%s%s</button></div>' % (ident, tag, rotulo))

def quadro_feedback(n):
    """O quadro da tela 7. Os DOIS primeiros campos sao os que chegam a aluna: a mesma chave
    sfb_l{n}_* que existe no cartao da aula, espelhada pelo fbEspelha(). O professor escreve
    onde estiver e o outro lugar acompanha -- e nada mais desta tela vai para ela."""
    def campo(cid, chave, rotulo, extra=''):
        return ('<div class="fb-field"><label for="%s">%s</label>'
                '<textarea id="%s" class="writebox" data-k="%s" '
                'oninput="persSave(this);autoCresce(this);fbEspelha(this)" lang="en"></textarea></div>%s'
                % (cid, rotulo, cid, chave, extra))
    board = (campo('sfb%d-w-in' % n, 'sfb_l%d_worked' % n, 'What worked') +
             campo('sfb%d-d-in' % n, 'sfb_l%d_develop' % n, 'Keep developing') +
             ('<div class="fb-field"><label for="fb%dclear">Clearer version</label>'
              '<textarea id="fb%dclear" class="writebox" data-k="fb_l%d_clear" '
              'oninput="persSave(this);autoCresce(this)" lang="en"></textarea></div>' % (n, n, n)))
    primeira = ('<div class="btn-bar" style="justify-content:flex-start;margin-top:var(--space-3)">'
                '<button class="btn-ghost" onclick="toggleEl(\'fb%dfirst\',this,\'Her first version\',\'Hide it\')">'
                'Her first version</button></div>'
                '<div id="fb%dfirst" style="display:none"><div class="fb-field">'
                '<label for="fb%dfv">Her first version</label>'
                '<textarea id="fb%dfv" class="writebox" data-k="fb_l%d_first" '
                'oninput="persSave(this);autoCresce(this)" lang="en"></textarea></div></div>'
                % (n, n, n, n, n))
    return '    <div class="fb-board">%s</div>\n%s' % (board, primeira)

def comparacao(pares):
    linhas = ''.join('<div class="two-col"><div class="fb-cmp">%s</div><div class="fb-cmp">%s</div></div>'
                     % (_rich(a), _rich(b)) for a, b in pares)
    return linhas

def fecho(n, titulo_txt):
    return ('    <p class="chapter-label" style="text-align:center">8 &middot; Retask and close</p>\n'
            '    <h2 class="slide-title" style="text-align:center">%s</h2>\n'
            '    <div class="close-flow">\n'
            '      <div class="close-block"><h5>What we worked on today</h5>'
            '<p class="cb-sub">Review what you worked on today.</p><div id="recapList%d"></div></div>\n'
            '      <div class="close-block"><h5>How confident do you feel right now?</h5>'
            '<div id="confList%d"></div></div>\n'
            '    </div>' % (titulo(titulo_txt), n, n))

def tabela(cabecalhos, linhas, largura=520):
    th = ''.join('<th>%s</th>' % c for c in cabecalhos)
    tr = ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % _rich(c) for c in l) for l in linhas)
    return ('    <div class="tbl-wrap" style="background:#fff"><table class="data" style="min-width:%dpx">'
            '<thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (largura, th, tr))
