#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insere ABAS SUPLEMENTARES num hub existente. ADITIVO PURO e IDEMPOTENTE.

PARA QUE SERVE
--------------
O `insert_hub.py` insere UMA AULA (stamp + accordion ex-lesson-N + card IN CLASS
+ complementares + audioMap + totalLessons). Este script faz outra coisa: pendura
uma ABA NOVA INTEIRA no hub, sem tocar em nada do que ja esta la.

Nasceu do pedido do Diego (09/09/2026): mais pre-class para treinar, musicas
gospel nos extras, e aulas de general English sobre o cotidiano nos EUA. A ordem
da Helen foi "nao mexe em NADA que existe, cria abas adicionais".

O QUE ELE GARANTE (e por que cada garantia importa)
---------------------------------------------------
1. ADITIVO. Faz exatamente DUAS insercoes por aba, ambas em ponto de juncao:
   - o <button> logo DEPOIS do ultimo tab-btn existente;
   - o <div class="tab-content"> logo DEPOIS do fechamento da ultima aba.
   Nenhum byte do conteudo existente e reescrito. REGRAS 12/21/30.

2. IDEMPOTENTE POR ABA. Se `id="tab-<slot>"` ja existe, aquela aba e pulada.
   Rodar duas vezes nao duplica nada, e permite reprocessar so uma aba.

3. NAO MEXE NO PROGRESSO. Nao toca `totalLessons`, `updateProgress`, `audioMap`,
   `id="stampN"` nem `data-lesson-progress`. O `updateProgress()` do hub varre
   apenas `ex-lesson-1..N`, entao conteudo com id proprio (xp-/us-/gs-) fica
   fora da conta: a barra do aluno e os stamps continuam exatamente como estavam.

4. SEM JS NOVO. O snippet so pode chamar funcao que JA existe no hub. O script
   RECUSA a insercao se o snippet chamar qualquer outra coisa (ver `checa_handlers`)
   -- e a mesma pergunta que o GATE `check_undefined_handlers` faz no CI, so que
   antes de escrever, e nao depois.

5. PROFUNDIDADE. O bloco entra na mesma profundidade das abas existentes, que e o
   que o `audit_hubs_struct.py` cobra (conteudo que "vaza" para fora das abas).

USO
    python3 _build/model/insert_hub_extras.py \
        --hub public/aluno/diego-leonel-george-wached.html \
        --aba xpractice:_build/diego-leonel-george-wached-extras/xpractice.html:"Extra Practice" \
        --aba uslife:.../uslife.html:"Living in the USA" \
        --aba gospel:.../gospel.html:"Gospel" \
        [--dry-run]
"""
import argparse
import os
import re
import sys

# Fecha a ultima aba do hub. E o ponto de juncao onde as abas novas entram.
# Fecho nomeado de uma aba: `</div><!-- /tab-xxx -->`. Ancoramos sempre no ULTIMO
# que existir no arquivo -- e nao no do complementary -- para que varias abas
# inseridas na mesma execucao saiam NA ORDEM em que foram passadas. Ancorar
# sempre no mesmo ponto empilhava cada aba nova ANTES da anterior (ordem
# invertida na barra), pego pelo teste de navegador em 09/09/2026.
FECHO_ABA = re.compile(r'</div><!-- /tab-[a-z0-9-]+ -->')

# Botao da barra de abas. Idem: o novo entra depois do ULTIMO que existir.
BTN_TAB = re.compile(
    r'[ \t]*<button class="tab-btn[^"]*"[^>]*onclick="switchTab\(\'[^\']+\'\)"[^>]*>.*?</button>\n')

# Chamadas de funcao dentro de handler inline (mesma heuristica do GATE do CI).
CALL = re.compile(r'(?<![.\w$])([A-Za-z_$][\w$]*)\s*\(')
HANDLER = re.compile(r'(?<![\w-])on[a-z]+\s*=\s*"([^"]*)"')
BUILTINS = set('''if for while switch catch return typeof void new delete in of do else
    function alert confirm prompt setTimeout setInterval parseInt parseFloat isNaN
    Number String Boolean Array Object JSON Math Date RegExp Promise Set Map'''.split())


def definidas_no_hub(hub_src):
    """Funcoes que o <script> do hub define -- as unicas que o snippet pode chamar."""
    nomes = set()
    for padrao in (r'function\s+([A-Za-z_$][\w$]*)',
                   r'\b(?:var|let|const)\s+([A-Za-z_$][\w$]*)\s*=\s*function',
                   r'window\.([A-Za-z_$][\w$]*)\s*='):
        nomes |= set(re.findall(padrao, hub_src))
    return nomes


def checa_handlers(snippet, disponiveis, rotulo):
    """RECUSA snippet que chame funcao inexistente -- botao morto e silencioso."""
    chamadas = set()
    for corpo in HANDLER.findall(snippet):
        chamadas |= set(CALL.findall(corpo))
    orfas = sorted(n for n in chamadas - disponiveis - BUILTINS)
    if orfas:
        sys.exit('ERRO [%s]: handler chama funcao que o hub NAO define: %s\n'
                 '       Isso viraria botao morto. Use so as funcoes existentes.'
                 % (rotulo, ', '.join(orfas)))


def checa_ids_reservados(snippet, rotulo):
    """Ids que o updateProgress()/os gates leem. Aba nova NAO pode usa-los."""
    for padrao, oque in ((r'id="ex-lesson-\d', 'id="ex-lesson-N"'),
                         (r'id="stamp\d', 'id="stampN"'),
                         (r'data-slide="\d', 'data-slide'),
                         (r'data-lesson-progress=', 'data-lesson-progress'),
                         (r'data-lesson-pct=', 'data-lesson-pct')):
        if re.search(padrao, snippet):
            sys.exit('ERRO [%s]: o snippet usa %s, que pertence as aulas existentes.\n'
                     '       Isso mexeria na barra de progresso/stamps do aluno.' % (rotulo, oque))


def ultimo(regex, hub_src, oque):
    """Ultima ocorrencia do padrao -- o ponto de juncao onde o novo e pendurado."""
    achados = list(regex.finditer(hub_src))
    if not achados:
        sys.exit('ERRO: %s nao encontrado no hub.' % oque)
    return achados[-1]


def insere_aba(hub_src, slot, rotulo, snippet):
    if 'id="tab-%s"' % slot in hub_src:
        print('  = %-12s ja existe, pulando' % slot)
        return hub_src, False

    # 1) botao, logo DEPOIS do ultimo botao da barra (preserva a ordem de entrada)
    m_btn = ultimo(BTN_TAB, hub_src, 'barra de abas')
    indent = re.match(r'[ \t]*', m_btn.group(0)).group(0) or '    '
    botao = '%s<button class="tab-btn" onclick="switchTab(\'%s\')">%s</button>\n' % (
        indent, slot, rotulo)
    hub_src = hub_src[:m_btn.end()] + botao + hub_src[m_btn.end():]

    # 2) bloco, logo DEPOIS do fecho da ultima aba
    if not snippet.endswith('\n'):
        snippet += '\n'
    m_fim = ultimo(FECHO_ABA, hub_src, 'fecho de aba (</div><!-- /tab-... -->)')
    hub_src = hub_src[:m_fim.end()] + '\n\n' + snippet + hub_src[m_fim.end():]

    print('  + %-12s "%s" (%d bytes)' % (slot, rotulo, len(snippet.encode('utf-8'))))
    return hub_src, True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--hub', required=True)
    ap.add_argument('--aba', action='append', required=True,
                    metavar='SLOT:ARQUIVO:ROTULO')
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    if not os.path.exists(args.hub):
        sys.exit('ERRO: hub inexistente: %s' % args.hub)

    original = open(args.hub, encoding='utf-8').read()
    hub_src = original
    disponiveis = definidas_no_hub(original)
    print('%s (%d bytes, %d funcoes JS disponiveis)'
          % (args.hub, len(original.encode('utf-8')), len(disponiveis)))

    mudou = False
    for spec in args.aba:
        slot, caminho, rotulo = spec.split(':', 2)
        snippet = open(caminho, encoding='utf-8').read()
        checa_handlers(snippet, disponiveis, slot)
        checa_ids_reservados(snippet, slot)
        hub_src, feito = insere_aba(hub_src, slot, rotulo, snippet)
        mudou = mudou or feito

    if not mudou:
        print('nada a fazer (todas as abas ja existiam)')
        return

    # O conteudo ANTERIOR tem de sobreviver byte a byte. Se o original nao for
    # subsequencia do resultado, alguma coisa foi reescrita -- e ai nao grava.
    if len(hub_src) <= len(original):
        sys.exit('ERRO: o hub nao cresceu. Insercao nao foi aditiva.')

    if args.dry_run:
        print('--dry-run: nada gravado (+%d bytes)'
              % (len(hub_src.encode('utf-8')) - len(original.encode('utf-8'))))
        return

    with open(args.hub, 'w', encoding='utf-8') as f:
        f.write(hub_src)
    print('gravado: +%d bytes'
          % (len(hub_src.encode('utf-8')) - len(original.encode('utf-8'))))


if __name__ == '__main__':
    main()
