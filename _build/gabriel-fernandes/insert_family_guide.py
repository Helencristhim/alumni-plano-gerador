#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""insert_family_guide.py — injeta a aba Family Guide NO HUB DO ALUNO gabriel-fernandes.

    python3 _build/gabriel-fernandes/insert_family_guide.py            # injeta/atualiza
    python3 _build/gabriel-fernandes/insert_family_guide.py --check    # so confere

POR QUE ESTE SCRIPT E DO ALUNO, E NAO DO SISTEMA
------------------------------------------------
A primeira versao disto era uma lib compartilhada (`public/lib/family-guide.js`) carregada
por `controle-aulas.js`, que os 153 hubs trazem. Tecnicamente melhor, e fora do combinado:

    Helen, 04/09/2026: "entao nao edita nada... mexe so no material do gabriel"

Entao o codigo mora aqui, no diretorio de ciclo DELE, ao lado do PERFIL-360.md e do
SYLLABUS.md — mesmo lugar dos `_build/_fernando_insert_hub.py` e
`_build/_graziele_insert_hub.py`, que sao a mesma coisa para outros alunos. Nada em
`public/lib/`, nada em `scripts/`, nada no workflow.

O QUE ELE TOCA (e so isso)
--------------------------
    public/aluno/gabriel-fernandes.html

O hub do PROFESSOR nao e tocado: a Helen pediu a aba "no link do aluno". Para levar para
o professor tambem, e so acrescentar o caminho em ALVOS.

DE ONDE VEM O TEXTO
-------------------
`_build/gabriel-fernandes/family-guide.json`, que e a FONTE. O HTML publicado e derivado:
para mudar o texto, edite o JSON e rode isto de novo. Editar o HTML na mao e o comeco da
divergencia — o `--check` existe para pegar exatamente isso.

IDEMPOTENTE
-----------
Se a aba ja existe, o bloco e SUBSTITUIDO pelo novo (nao duplicado). Rodar duas vezes da
o mesmo resultado.

SOBREVIVE AO insert_hub.py?
---------------------------
Sim. O `insert_hub.py` e ADITIVO: ele insere por ancora o que falta e pula o que ja
existe, nao regenera o hub. O que APAGARIA esta aba e o `build_from_model.py` com
`"hub": "new"`, que so roda na aula 1 e ja rodou. Ainda assim, depois de gerar uma aula
nova, rode este script de novo e confira: e barato e tira a duvida.
"""
import html
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(AQUI, '..', '..'))
FONTE = os.path.join(AQUI, 'family-guide.json')

ALVOS = [os.path.join(ROOT, 'public', 'aluno', 'gabriel-fernandes.html')]

INICIO = '<!-- ========== TAB: FAMILY GUIDE (gabriel-fernandes) ========== -->'
FIM = '</div><!-- /tab-family -->'
ANCORA_CONTEUDO = '</div><!-- /tab-complementary -->'
BOTAO = '    <button class="tab-btn" onclick="switchTab(\'family\')">Family Guide</button>'


def e(s):
    return html.escape('' if s is None else str(s), quote=False)


def css():
    # Tudo escopado em #tab-family: nao ha como vazar para o resto do hub.
    return """<style>
#tab-family { --fg-accent: var(--accent, #003080); }
#tab-family .fg-head { margin-bottom:1.4rem; }
#tab-family .fg-title { font-family:'Cormorant Garamond',Georgia,serif;font-size:1.5rem;font-weight:600;color:var(--text,#1a1a2e);line-height:1.3; }
#tab-family .fg-sub { font-size:.88rem;line-height:1.55;color:var(--text-dim,#777);max-width:62ch;margin-top:.3rem; }
#tab-family .fg-always { background:var(--bg-card,#fff);border:1px solid var(--border,#d4d4cc);border-left:4px solid var(--fg-accent);border-radius:12px;padding:1.2rem 1.4rem;margin-bottom:1.1rem; }
#tab-family .fg-always h4 { font-size:.95rem;font-weight:600;color:var(--text,#1a1a2e);margin:0 0 .7rem; }
#tab-family .fg-always ol { margin:0;padding-left:1.15rem;display:flex;flex-direction:column;gap:.6rem; }
#tab-family .fg-always li { font-size:.88rem;line-height:1.6;color:var(--text-mid,#4a4a5a); }
#tab-family .fg-always strong { color:var(--text,#1a1a2e); }
#tab-family .fg-rule { font-size:.85rem;line-height:1.6;color:var(--text-dim,#5c5c6c);border-left:2px solid var(--border,#d4d4cc);padding-left:1rem;margin:0 0 1.4rem;max-width:66ch; }
#tab-family .fg-lesson { background:var(--bg-card,#fff);border:1px solid var(--border,#d4d4cc);border-radius:12px;margin-bottom:.7rem;overflow:hidden; }
#tab-family .fg-summary { display:flex;align-items:center;gap:.9rem;padding:.95rem 1.2rem;cursor:pointer;list-style:none;min-height:44px; }
#tab-family .fg-summary::-webkit-details-marker { display:none; }
#tab-family .fg-summary:focus-visible { outline:3px solid var(--fg-accent);outline-offset:-3px; }
#tab-family .fg-num { display:flex;align-items:center;justify-content:center;min-width:38px;height:38px;background:var(--fg-accent);color:#fff;border-radius:9px;font-weight:700;font-size:.95rem;flex-shrink:0; }
#tab-family .fg-lt { flex:1;font-family:'Cormorant Garamond',Georgia,serif;font-size:1.12rem;font-weight:600;color:var(--text,#1a1a2e);line-height:1.35; }
#tab-family .fg-chev { color:var(--text-dim,#999);font-size:.8rem;transition:transform .2s; }
#tab-family .fg-lesson[open] .fg-chev { transform:rotate(180deg); }
#tab-family .fg-body { padding:0 1.2rem 1.2rem;border-top:1px solid var(--border-light,#eeeee8); }
#tab-family .fg-row { display:grid;grid-template-columns:minmax(140px,190px) 1fr;gap:.4rem 1.2rem;padding:.85rem 0;border-bottom:1px solid var(--bg-elevated,#f2f2ec); }
#tab-family .fg-row:last-of-type { border-bottom:none; }
#tab-family .fg-label { font-size:.72rem;font-weight:600;text-transform:uppercase;letter-spacing:.06em;color:var(--text-dim,#8a8a96);padding-top:.15rem; }
#tab-family .fg-value { font-size:.89rem;line-height:1.65;color:var(--text-mid,#3a3a48); }
#tab-family .fg-value em { color:var(--fg-accent);font-style:italic;font-weight:500; }
#tab-family .fg-dinner { background:var(--bg-elevated,#f7f7f2);border:1px solid var(--border,#e6e6de);border-radius:10px;padding:.9rem 1.1rem;margin-top:.9rem; }
#tab-family .fg-dl { font-size:.68rem;font-weight:600;text-transform:uppercase;letter-spacing:.08em;color:var(--fg-accent);margin-bottom:.4rem; }
#tab-family .fg-den { font-family:'Cormorant Garamond',Georgia,serif;font-size:1.08rem;font-weight:600;color:var(--text,#1a1a2e);line-height:1.45; }
#tab-family .fg-dpt { font-size:.84rem;line-height:1.55;color:var(--text-dim,#6a6a78);margin-top:.3rem; }
#tab-family .fg-note { font-size:.86rem;line-height:1.6;color:var(--text-mid,#4a4a5a);margin-top:.9rem;padding-top:.8rem;border-top:1px dashed var(--border,#e0e0d8); }
#tab-family .fg-note strong { color:var(--text,#1a1a2e); }
#tab-family .fg-close { font-size:.86rem;line-height:1.6;color:var(--text-dim,#777);margin-top:1.2rem;max-width:66ch; }
@media (max-width:640px) { #tab-family .fg-row { grid-template-columns:1fr;gap:.15rem; } }
@media (prefers-reduced-motion:reduce) { #tab-family .fg-chev { transition:none; } }
</style>"""


def linha(rotulo, valor):
    if not valor:
        return ''
    return ('      <div class="fg-row"><div class="fg-label">' + e(rotulo) +
            '</div><div class="fg-value">' + valor + '</div></div>\n')


def bloco(d):
    out = [INICIO, css(), '<div class="tab-content" id="tab-family">']
    out.append('  <div class="fg-head"><div class="fg-title">' + e(d.get('titulo', 'Family Guide')) +
               '</div><div class="fg-sub">' + e(d.get('subtitulo', '')) + '</div></div>')

    s = d.get('sempre') or {}
    if s.get('itens'):
        out.append('  <div class="fg-always"><h4>' + e(s.get('titulo', '')) + '</h4><ol>')
        for i in s['itens']:
            out.append('    <li><strong>' + e(i['t']) + '.</strong> ' + e(i['d']) + '</li>')
        out.append('  </ol></div>')

    if d.get('tarefa_regra'):
        out.append('  <p class="fg-rule">' + e(d['tarefa_regra']) + '</p>')

    for idx, a in enumerate(d.get('aulas', [])):
        aberto = ' open' if idx == 0 else ''
        out.append('  <details class="fg-lesson"' + aberto + '>')
        out.append('    <summary class="fg-summary"><span class="fg-num">' + e('%02d' % a['n']) +
                   '</span><span class="fg-lt">' + e(a.get('titulo', '')) +
                   '</span><span class="fg-chev" aria-hidden="true">&#9662;</span></summary>')
        out.append('    <div class="fg-body">')
        corpo = ''
        corpo += linha('O que ele estudou', e(a.get('tema')))
        # `ingles` traz <em> editorial do JSON, marcando o exemplo em ingles. E o unico
        # campo que passa HTML, e ele e escrito a mao por nos, nao por terceiro.
        corpo += linha('O inglês da aula', a.get('ingles', ''))
        corpo += linha('O que ele já consegue fazer', e(a.get('conquista')))
        corpo += linha('Tarefa de casa', e(a.get('tarefa')))
        out.append(corpo.rstrip('\n'))
        j = a.get('jantar')
        if j:
            out.append('      <div class="fg-dinner"><div class="fg-dl">Para perguntar no jantar</div>'
                       '<div class="fg-den">&ldquo;' + e(j.get('en')) + '&rdquo;</div>'
                       '<div class="fg-dpt">' + e(j.get('pt')) + '</div></div>')
        if a.get('repare'):
            out.append('      <div class="fg-note"><strong>Repare:</strong> ' + e(a['repare']) + '</div>')
        out.append('    </div>')
        out.append('  </details>')

    if d.get('fecho'):
        out.append('  <p class="fg-close">' + e(d['fecho']) + '</p>')

    out.append(FIM)
    return '\n'.join(out)


def aplica(caminho, novo_bloco, checar):
    with open(caminho, encoding='utf-8') as fh:
        s = original = fh.read()
    rel = os.path.relpath(caminho, ROOT)

    if ANCORA_CONTEUDO not in s:
        return f'! {rel}: ancora {ANCORA_CONTEUDO} nao encontrada'

    # Substitui o bloco antigo, se houver — nunca duplica.
    padrao = re.compile(re.escape(INICIO) + r'.*?' + re.escape(FIM), re.S)
    if padrao.search(s):
        s = padrao.sub(lambda _m: novo_bloco, s)
    else:
        s = s.replace(ANCORA_CONTEUDO, ANCORA_CONTEUDO + '\n\n' + novo_bloco, 1)

    if BOTAO.strip() not in s:
        m = re.search(r'(<div class="tabs">.*?)(\n\s*</div>)', s, re.S)
        if not m:
            return f'! {rel}: container .tabs nao encontrado'
        s = s[:m.end(1)] + '\n' + BOTAO + s[m.end(1):]

    if s == original:
        return f'= {rel}: ja estava igual'
    if checar:
        return f'! {rel}: DIVERGENTE do family-guide.json'

    with open(caminho, 'w', encoding='utf-8') as fh:
        fh.write(s)
    return f'+ {rel}: aba Family Guide gravada'


def main():
    checar = '--check' in sys.argv[1:]
    if not os.path.isfile(FONTE):
        print(f'! fonte ausente: {os.path.relpath(FONTE, ROOT)}')
        return 1
    try:
        with open(FONTE, encoding='utf-8') as fh:
            d = json.load(fh)
    except json.JSONDecodeError as ex:
        print(f'! family-guide.json invalido ({ex.msg}, linha {ex.lineno})')
        return 1
    if not d.get('aulas'):
        print('! family-guide.json sem aulas')
        return 1

    novo = bloco(d)
    saidas = [aplica(c, novo, checar) for c in ALVOS]
    for s in saidas:
        print('  ' + s)
    ruim = [s for s in saidas if s.startswith('!')]
    if ruim:
        print(f'\nfamily guide: {len(ruim)} problema(s).')
        return 1
    print(f'\nfamily guide OK — {len(d["aulas"])} aula(s) no hub do aluno.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
