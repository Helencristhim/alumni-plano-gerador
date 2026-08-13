#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""htmlpatch.py — enxertos de HTML que nao dependem de sorte.

`append_to_inline_script` existe por causa de um defeito INVISIVEL: escrever codigo antes
do ULTIMO `</script>` do arquivo parece obvio e funciona... ate o arquivo terminar com
`<script src="/lib/algo.js"></script>`. Ai o codigo vira CONTEUDO de uma tag que tem `src`
— e o navegador IGNORA o conteudo inline de um script com src. Nada de erro, nada no
console: a funcao simplesmente nunca existe.

Aconteceu com o arrastar do exercicio de ordenar (13/08/2026): o JS caiu dentro do
`<script src="/lib/contrast-guard.js">` do hub e o arrastar continuou morto. So apareceu
porque a medicao no navegador perguntou "a funcao carregou?" em vez de "o texto esta no
arquivo?". Grep teria dito que sim.
"""
import re


def append_to_inline_script(s, code):
    """Poe `code` no fim do ULTIMO <script> SEM src. Se nao houver, cria um antes de </body>."""
    alvo = None
    for m in re.finditer(r'<script\b([^>]*)>', s):
        if 'src=' in m.group(1):
            continue
        fim = s.find('</script>', m.end())
        if fim > 0:
            alvo = fim
    if alvo is None:
        i = s.rfind('</body>')
        bloco = '<script>\n' + code + '\n</script>\n'
        return (s[:i] + bloco + s[i:]) if i > 0 else s + bloco
    return s[:alvo] + code + '\n' + s[alvo:]
