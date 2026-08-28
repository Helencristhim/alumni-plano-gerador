#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GATE 28 — O REVEAL TEM DE REVELAR. MEDIDO CLICANDO, NUM NAVEGADOR DE VERDADE.

O DEFEITO
---------
    <button onclick="var t=document.getElementById('rule13');
                     t.classList.toggle('revealed');...">Reveal the Rule</button>
    <div id="rule13" style="display:none">  <- a tabela da regra

O clique poe a classe `revealed` no div. Nenhuma regra CSS casa `#rule13.revealed`,
e o `display:none` e INLINE — inline vence stylesheet. Resultado: o botao troca de
texto para "Hide the Rule", a classe entra no DOM, e A REGRA NUNCA APARECE. A
professora compartilha a tela, clica, e o slide fica vazio.

Aconteceu em 130 slides de 4 alunos (daniela-feitoza, daniela-feitoza-v2,
victor-malvezi-paschotto, milton-sayegh, sandra-hayasaki), desde junho de 2026.

POR QUE NENHUM GATE VIU
-----------------------
O GATE 10 (check_vocab_reveal.py) e exatamente o gate deste defeito — mas ele
identifica o alvo por CLASSE, com uma lista fixa de tres familias (vocab-back,
q-answer, error-fix). A tabela da regra e um `<div id="ruleN">` SEM CLASSE
NENHUMA: cai fora da lista e o gate passa reto.

E o problema e mais fundo que a lista: TODO gate estatico daqui le o HTML como
TEXTO. Um handler que chama `classList.toggle('revealed')` PARECE vivo para quem
le. Saber se ele revela alguma coisa exige (a) casar seletor CSS de verdade,
(b) resolver a cascata e a especificidade, (c) saber que inline vence stylesheet
menos quando ha !important. Escrever isso e reescrever um navegador. Prova de que
a estatica erra nos DOIS sentidos: uma varredura por regex acusou
rafael-pelizaro.html (grammar-box com display:none inline + classList.add('show'))
— e o arquivo esta CERTO, porque a regra dele e `.grammar-box.show{display:block
!important}`, e o !important ganha do inline.

Entao este gate nao le: ele CLICA. Abre o arquivo no Chromium, aperta o botao, e
compara o computed style de TODOS os elementos antes e depois. Se nada mudou fora
do proprio botao, o reveal nao revela — FAIL. E agnostico de mecanismo: pega
display, visibility, opacity e max-height, sem saber qual deles o autor usou.

ESCOPO
------
So elementos cujo texto visivel comeca com "Reveal " (Reveal the Rule / the
Toolkit / the Map / the Table). E a familia do defeito e mantem o gate longe de
falso positivo em botao que legitimamente so muda estado interno.

    python3 scripts/check_reveal_clica.py a.html b.html   # os arquivos do PR
    python3 scripts/check_reveal_clica.py --selftest      # prova que o gate morde
"""
import os
import pathlib
import re
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Mede o que MUDOU no documento por causa do clique. Nao presume mecanismo:
# display, visibility, opacity e max-height cobrem as quatro formas de esconder
# que o repo usa. O proprio botao (e o que esta dentro dele) sai da conta, senao
# trocar o texto de "Reveal" para "Hide" ja contaria como revelacao.
# O `await espera(900)` depois do clique NAO e folga: e o defeito que este gate
# teve por um mes. O alvo do "Reveal the Rule" do molde antigo abre por
# `max-height` com `transition: max-height .6s`. Medir o computed style no
# instante seguinte ao clique le max-height ainda em 0px -- a classe ja entrou,
# o CSS ja casa, e o valor so chega em ~600 ms. O gate concluia "nao mudou nada"
# e REPROVAVA botao que funciona (5 aulas do nilo-mesquita-patucci, professor e
# aluno, em 28/08/2026). Esperar nao afrouxa nada: reveal morto continua sem
# mudar coisa alguma depois de 900 ms.
JS = r"""async () => {
  const espera = ms => new Promise(r => setTimeout(r, ms));
  const assinatura = () => [...document.querySelectorAll('*')].map(e => {
    const s = getComputedStyle(e);
    return s.display + '|' + s.visibility + '|' + s.opacity + '|' + s.maxHeight;
  });
  const out = [];
  const botoes = [...document.querySelectorAll('button, a, div, span')].filter(b =>
    /^reveal\s/i.test(b.textContent.replace(/\s+/g, ' ').trim()) && b.getAttribute('onclick'));
  for (const btn of botoes) {
    const rotulo = btn.textContent.replace(/\s+/g, ' ').trim().slice(0, 40);
    const antes = assinatura();
    try { btn.click(); } catch (e) { out.push({rotulo, mudou: 0, erro: String(e).slice(0, 80)}); continue; }
    await espera(900);   // transicao de CSS: ver o comentario acima do JS
    const depois = assinatura();
    const els = [...document.querySelectorAll('*')];
    let mudou = 0;
    for (let i = 0; i < Math.min(antes.length, depois.length); i++) {
      if (antes[i] !== depois[i] && els[i] !== btn && !btn.contains(els[i])) mudou++;
    }
    out.push({rotulo, mudou});
  }
  return out;
}"""


def medir(paths):
    """[(arquivo, rotulo, mudou)] para cada botao de reveal de cada arquivo."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print('GATE 28 NAO PODE RODAR: playwright ausente. '
              'Instale com `pip install playwright && python3 -m playwright install chromium`.',
              file=sys.stderr)
        sys.exit(2)   # 2 = gate impedido de rodar. NUNCA verde por omissao.

    linhas = []
    with sync_playwright() as p:
        try:
            navegador = p.chromium.launch()
        except Exception as e:
            print('GATE 28 NAO PODE RODAR: chromium nao abre (%s)' % str(e)[:120], file=sys.stderr)
            sys.exit(2)
        pagina = navegador.new_page()
        pagina.on('dialog', lambda d: d.dismiss())
        for f in paths:
            try:
                pagina.goto('file://' + str(pathlib.Path(f).resolve()), timeout=30000)
                res = pagina.evaluate(JS)
            except Exception as e:
                # Pagina que navega sozinha (redirect) nao tem slide de regra.
                if 'context was destroyed' in str(e):
                    pagina = navegador.new_page()
                    continue
                print('  aviso: %s nao pode ser medido (%s)' % (f, str(e)[:60]))
                continue
            for r in res:
                linhas.append((f, r['rotulo'], r['mudou']))
        navegador.close()
    return linhas


def falhas(paths):
    out = []
    for f, rotulo, mudou in medir(paths):
        if mudou <= 0:
            rel = os.path.relpath(f, RAIZ) if f.startswith(RAIZ) else f
            out.append('%s: "%s" nao revela nada — o clique nao muda o estilo de '
                       'elemento nenhum (alvo escondido inline + reveal por classe?)'
                       % (rel, rotulo))
    return out


QUEBRADO = """<!doctype html><html><head><style>
.vocab-card.revealed .card-word{display:block}
</style></head><body>
<button onclick="var t=document.getElementById('rule1');t.classList.toggle('revealed');this.textContent=t.classList.contains('revealed')?'Hide the Rule':'Reveal the Rule'">Reveal the Rule</button>
<div id="rule1" style="display:none"><table><tr><td>have + been + -ing</td></tr></table></div>
</body></html>"""

OK_STYLE = """<!doctype html><html><body>
<button onclick="var t=document.getElementById('rule1');t.style.display=(t.style.display==='none'||!t.style.display)?'block':'none'">Reveal the Rule</button>
<div id="rule1" style="display:none"><table><tr><td>have + been + -ing</td></tr></table></div>
</body></html>"""

OK_CLASSE = """<!doctype html><html><head><style>
.grammar-box.show{display:block!important}
</style></head><body>
<button onclick="document.getElementById('g1').classList.add('show')">Reveal the Rule</button>
<div id="g1" class="grammar-box" style="display:none"><table><tr><td>regra</td></tr></table></div>
</body></html>"""


OK_TRANSICAO = """<!doctype html><html><head><style>
.grammar-table-wrap{overflow:hidden;max-height:0;transition:max-height .6s ease}
.grammar-table-wrap.show{max-height:500px}
</style></head><body>
<button onclick="document.getElementById('g1').classList.add('show')">Reveal the Rule</button>
<div class="grammar-table-wrap" id="g1"><table><tr><td>regra</td></tr></table></div>
</body></html>"""


def selftest():
    """Prova, em arquivos temporarios, que o gate REPROVA o quebrado e ACEITA os certos.

    O terceiro caso e o que nenhuma checagem estatica acerta sem um navegador: o
    alvo nasce display:none INLINE e mesmo assim aparece, porque a regra da classe
    tem !important. Se o gate reprovar esse, ele esta chutando pela aparencia.

    O QUARTO e o defeito do proprio gate, achado em 28/08/2026: o alvo abre por
    `max-height` com `transition: .6s`. Medido no instante seguinte ao clique, o
    computed style ainda le 0px -- a classe entrou, a regra casa, e o valor so
    chega em ~600 ms. O gate reprovava botao que funciona. Se este caso voltar a
    falhar, alguem tirou a espera.
    """
    casos = [
        ('QUEBRADO: reveal por classe sem regra CSS que case o alvo', QUEBRADO, True),
        ('OK: handler mexe no style.display (forma do modelo)', OK_STYLE, False),
        ('OK: reveal por classe COM regra !important que vence o inline', OK_CLASSE, False),
        ('OK: reveal por max-height COM transicao de .6s (o falso positivo de 28/08)', OK_TRANSICAO, False),
    ]
    erros = 0
    with tempfile.TemporaryDirectory() as d:
        for nome, html, deve_falhar in casos:
            p = os.path.join(d, 'caso.html')
            open(p, 'w', encoding='utf-8').write(html)
            falhou = bool(falhas([p]))
            ok = falhou == deve_falhar
            print('  [%s] %s' % ('ok' if ok else 'ERRO', nome))
            if not ok:
                erros += 1
    if erros:
        print('SELFTEST FALHOU: o gate parou de morder.', file=sys.stderr)
        return 1
    print('SELFTEST OK — o gate reprova o quebrado e aceita os tres certos.')
    return 0


def main(argv):
    if '--selftest' in argv:
        return selftest()
    paths = [a for a in argv if not a.startswith('--')]
    if not paths:
        print('uso: check_reveal_clica.py <arquivos.html> | --selftest')
        return 0
    paths = [p for p in paths if p.endswith('.html') and os.path.exists(p)]
    # Abrir um arquivo no navegador custa ~1s. A esmagadora maioria dos HTML do repo
    # nao tem botao de reveal nenhum, entao um filtro de texto barato antes decide
    # quem vale abrir. Isto e otimizacao, nao criterio: quem passa o filtro e medido
    # CLICANDO, e o filtro so pode tirar arquivo em que a string nem existe.
    tem_reveal = re.compile(r'>\s*Reveal\s', re.I)
    paths = [p for p in paths
             if tem_reveal.search(open(p, encoding='utf-8', errors='ignore').read())]
    if not paths:
        print('GATE 28: nenhum arquivo com botao de reveal a medir.')
        return 0
    problemas = falhas(paths)
    if problemas:
        print('GATE 28 — REVEAL QUE NAO REVELA (%d):' % len(problemas), file=sys.stderr)
        for p in problemas:
            print('  ' + p, file=sys.stderr)
        return 1
    print('GATE 28 OK — %d arquivo(s) medido(s) no Chromium, todo reveal revela.' % len(paths))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
