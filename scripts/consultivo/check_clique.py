#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 42 — o que acontece quando alguem CLICA (REG-004, PRO-011).

    REG-004 · Controle visual sem funcao · BLOCKER
    "Botao, selecao, reset, finish, transcript ou player existe, mas nao executa a acao
     prometida."  — Detectacao recomendada: Runtime.

Todos os outros gates leem o arquivo parado. Este abre no chromium e CLICA. E a unica
familia de defeito que nenhuma leitura estatica alcanca: o HTML e valido, o console fica
limpo na carga, e o defeito so existe no instante do clique.

AS TRES PERGUNTAS
-----------------
 1. **Clicar estoura?** Um `TypeError` no handler mata o clique e tudo que vinha depois
    dele. Na carga isso o GATE 35 pega; no CLIQUE, ninguem pegava.

    A rede que pega e o `pageerror`, NAO o try/catch em volta do `dispatchEvent`: excecao
    dentro de handler inline nao propaga para quem disparou o evento -- ela sobe como erro
    nao capturado na janela. O try/catch fica porque cobre o caso em que o proprio
    `dispatchEvent` falha, mas quem acusa de verdade e o listener.
 2. **O painel que o handler nomeia existe, e alterna?** `cartaoPainel('lcprep3',this)`
    diz em voz alta qual elemento vai abrir. Se aquele id nao existe, o clique e um
    no-op silencioso -- e o id sai errado exatamente quando o material tem outra numeracao
    de aula, que e o caso de todo aluno que nao seja o do artefato.
 3. **O pre-class responde na URL certa, e SO nela?** Ver abaixo; e a regra mais
    interessante das tres.

O PRE-CLASS RESPONDE PARA A ALUNA E NAO RESPONDE PARA O PROFESSOR
------------------------------------------------------------------
`tog(el)` alterna `.sel` -- mas comeca com `if(preConsulta(el))return;`. Na URL do
PROFESSOR o pre-class e MODO CONSULTA: ele le o que a aluna respondeu, nao responde no
lugar dela. Medido no molde: **aluno 33/33 alternam, professor 0/33**.

Entao a regra tem DOIS lados, e os dois sao defeito:
  - controle que nao responde no arquivo da ALUNA  -> exercicio morto;
  - controle que responde no arquivo do PROFESSOR  -> o modo consulta caiu, e o professor
    passa a poder sobrescrever a resposta dela sem perceber.

Um gate que so olhasse um lado deixaria o outro passar.

O QUE NAO ESTA AQUI, E POR QUE — a medicao que me fez desistir
---------------------------------------------------------------
A tentacao obvia e "clique em tudo e exija que o DOM mude". Eu implementei e MEDI:
**193 dos 360 controles do molde nao mudam o DOM** -- 54%. E quase todos por motivo
legitimo: `aoTopo` rola a pagina, `say`/`playTalk` tocam audio, `ppPick` grava valor, e os
33 `tog` do professor sao BLOQUEADOS DE PROPOSITO pelo modo consulta.

Um gate com 54% de falso positivo nao protege nada: ele ensina a ignorar gate. Por isso o
que entra aqui e expectativa POR FAMILIA, onde da para dizer sem ambiguidade o que tinha de
acontecer -- e nao um veredito universal sobre "fez alguma coisa".

ESCOPO: o carimbo `alumni-anatomia=consultivo`.

DEPENDENCIA: playwright + chromium. Ausentes, o gate DIZ que nao pode rodar e falha -- nunca
finge que passou. Mesma postura do GATE 35.

USO:
    python3 scripts/consultivo/check_clique.py [arquivo.html ...]
    python3 scripts/consultivo/check_clique.py --selftest
"""
import functools
import glob
import http.server
import os
import re
import socketserver
import sys
import threading

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ANATOMIA = "consultivo"
VERDE, VERMELHO, ZERA = "\033[32m", "\033[31m", "\033[0m"

# A sonda roda DENTRO da pagina. Devolve dados, nunca veredito: quem julga e o Python, para
# que a regra fique legivel num lugar so.
# CADA FASE NUMA CARGA LIMPA, e nao ha atalho aqui.
#
# A primeira versao rodava as tres na mesma pagina e se auto-sabotou: a fase 1 clica TUDO,
# e "tudo" inclui `setView('aluno')` -- o botao que troca a URL do professor para a previa
# da aluna. Depois dele o modo consulta some (com razao: dali em diante e a visao dela), e
# a fase 3 media a pagina errada e acusava o molde. Quem pegou foi o proprio gate, na
# primeira execucao.
#
# Estado acumulado e o veneno de todo teste de interface. Recarregar por fase custa
# ~300 ms e compra a certeza de que cada resposta e sobre a pagina que a pergunta descreve.
SONDA = r"""(fase) => {
  const out = {estouros: [], paineis: [], tog: {n: 0, alternou: 0}};

  // 1 · clicar nao pode estourar
  if (fase === 1) document.querySelectorAll('[onclick]').forEach((el) => {
    const h = (el.getAttribute('onclick') || '').slice(0, 70);
    try {
      el.dispatchEvent(new MouseEvent('click', {bubbles: true, cancelable: true}));
    } catch (e) {
      out.estouros.push({handler: h, texto: (el.textContent || '').trim().slice(0, 40),
                         erro: String(e).slice(0, 120)});
    }
  });

  // 2 · painel nomeado no proprio handler: existe? alterna?
  const vis = (e) => (e ? getComputedStyle(e).display !== 'none' : null);
  if (fase === 2) document.querySelectorAll('[onclick]').forEach((el) => {
    const h = el.getAttribute('onclick') || '';
    const m = h.match(/^(cartaoPainel|showEl)\(\s*'([^']+)'/);
    if (!m) return;
    const alvo = document.getElementById(m[2]);
    const antes = vis(alvo);
    el.dispatchEvent(new MouseEvent('click', {bubbles: true, cancelable: true}));
    out.paineis.push({fn: m[1], id: m[2], existe: !!alvo, alternou: alvo ? vis(alvo) !== antes : false});
  });

  // 3 · o pre-class responde? (a resposta CERTA depende de qual URL e)
  if (fase === 3) document.querySelectorAll('[onclick^="tog(this)"]').forEach((el) => {
    const antes = el.className;
    el.dispatchEvent(new MouseEvent('click', {bubbles: true, cancelable: true}));
    out.tog.n += 1;
    if (el.className !== antes) out.tog.alternou += 1;
  });
  return out;
}"""


def carimbo(c):
    m = re.search(r'<meta\s+name="alumni-anatomia"\s+content="([^"]+)"', c[:4000])
    return m.group(1) if m else None


def eh_professor(c):
    return 'id="tab-inclass"' in c


def _servidor():
    """`file://` costuma estar bloqueado para automacao, e o material publicado roda em
    origem isolada (P2 §26). Servir por HTTP e o que se parece com producao."""
    h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=RAIZ)

    class Q(socketserver.TCPServer):
        allow_reuse_address = True

        def handle_error(self, *a):
            pass          # 404 de MP3 nao materializado nao e erro DESTE gate

    srv = Q(("127.0.0.1", 0), h)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, srv.server_address[1]


def mede(rels):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("GATE 42 NAO PODE RODAR: playwright ausente. "
              "`pip install playwright && python3 -m playwright install chromium`.",
              file=sys.stderr)
        return None
    out = {}
    srv, porta = _servidor()
    try:
        with sync_playwright() as p:
            try:
                nav = p.chromium.launch()
            except Exception as e:                                    # noqa: BLE001
                print(f"GATE 42 NAO PODE RODAR: chromium nao abre ({str(e)[:120]})",
                      file=sys.stderr)
                return None
            for rel in rels:
                erros = []
                dados = {"estouros": [], "paineis": [], "tog": {"n": 0, "alternou": 0}}
                for fase in (1, 2, 3):
                    # CONTEXTO NOVO, nao so pagina nova. Recarregar nao basta: a fase 1
                    # clica `setView('aluno')`, que GRAVA a visao escolhida no
                    # localStorage, e o reload volta ja na previa da aluna -- com o modo
                    # consulta desligado, com razao. A fase 3 media a pagina errada e
                    # acusava o molde. Contexto novo zera o armazenamento junto.
                    ctx = nav.new_context()
                    pg = ctx.new_page()
                    pg.on("pageerror", lambda e: erros.append(str(e)))
                    # confirm()/alert() de um Reset travariam a pagina para sempre
                    pg.on("dialog", lambda d: d.dismiss())
                    pg.goto(f"http://127.0.0.1:{porta}/{rel}", wait_until="load")
                    pg.wait_for_timeout(400)
                    try:
                        parcial = pg.evaluate(SONDA, fase)
                    except Exception as e:                            # noqa: BLE001
                        dados = {"__sonda__": str(e)[:150]}
                        ctx.close()
                        break
                    dados["estouros"] += parcial["estouros"]
                    dados["paineis"] += parcial["paineis"]
                    if parcial["tog"]["n"]:
                        dados["tog"] = parcial["tog"]
                    pg.wait_for_timeout(200)
                    ctx.close()
                dados["pageerror"] = erros
                out[rel] = dados
            nav.close()
    finally:
        srv.shutdown()
    return out


def avalia(rel, d, professor):
    erros = []
    if "__sonda__" in d:
        return [f"a sonda nao rodou: {d['__sonda__']}"]

    for x in d.get("estouros", []):
        erros.append(f"REG-004: clicar em {x['texto']!r} ({x['handler']}) ESTOURA — "
                     f"{x['erro']}. O clique morre, e tudo que vinha depois dele tambem.")
    for e in d.get("pageerror", []):
        erros.append(f"REG-004: excecao nao capturada durante os cliques — {e[:140]}")

    for p in d.get("paineis", []):
        if not p["existe"]:
            erros.append(f"PRO-011: {p['fn']}('{p['id']}') aponta para um id que NAO EXISTE "
                         f"no documento. O clique e um no-op silencioso.")
        elif not p["alternou"]:
            erros.append(f"REG-004: {p['fn']}('{p['id']}') nao alterna a visibilidade do "
                         f"painel. O botao existe e nao executa o que promete.")

    t = d.get("tog", {"n": 0, "alternou": 0})
    if t["n"]:
        if professor and t["alternou"]:
            erros.append(
                f"MODO CONSULTA CAIU: {t['alternou']} de {t['n']} controles do pre-class "
                f"RESPONDEM na URL do professor. Ali o pre-class e so leitura do que a aluna "
                f"fez — respondendo, o professor sobrescreve a resposta dela sem perceber.")
        if not professor and t["alternou"] != t["n"]:
            erros.append(
                f"REG-004: {t['n'] - t['alternou']} de {t['n']} controles do pre-class NAO "
                f"respondem ao clique na URL da aluna. O exercicio esta morto.")
    return erros


def alvos_padrao():
    fora = []
    for p in sorted(glob.glob(os.path.join(RAIZ, "public", "professor", "*.html")) +
                    glob.glob(os.path.join(RAIZ, "public", "aluno", "*.html"))):
        try:
            with open(p, encoding="utf-8") as f:
                if carimbo(f.read(4000)) == ANATOMIA:
                    fora.append(os.path.relpath(p, RAIZ))
        except OSError:
            pass
    return fora


def _selftest():
    """Planta os defeitos num arquivo temporario DENTRO do repo -- o servidor serve a RAIZ,
    e um /tmp nao seria alcancavel por HTTP."""
    base = os.path.join(RAIZ, "public", "aluno", "stephanie-vicente.html")
    prof = os.path.join(RAIZ, "public", "professor", "stephanie-vicente.html")
    if not (os.path.exists(base) and os.path.exists(prof)):
        print("SELFTEST INCONCLUSIVO — o molde nao esta no lugar.")
        return 1
    limpo_a = open(base, encoding="utf-8").read()
    limpo_p = open(prof, encoding="utf-8").read()

    casos = [
        ("REG-004 clique que estoura", limpo_a, False,
         lambda s: s.replace("</body>",
                             '<button onclick="naoExisteEssaFuncao_42()">x</button></body>', 1),
         "REG-004"),
        ("PRO-011 painel apontando para id inexistente", limpo_p, True,
         lambda s: s.replace('cartaoPainel(\'lcprep1\'', 'cartaoPainel(\'lcprep99\'', 1),
         "NAO EXISTE"),
        # A mutacao tem de deixar o CONTROLE no lugar e matar o EFEITO. Trocar o onclick
        # tirava o elemento do seletor, e o gate media 32/32 -- verde, medindo menos.
        ("REG-004 controle do pre-class morto na URL da aluna", limpo_a, False,
         lambda s: s.replace("el.classList.toggle('sel');", "", 1),
         "NAO respondem"),
        ("modo consulta caiu na URL do professor", limpo_p, True,
         # so a GUARDA sai. Renomear a funcao junto quebrava os outros chamadores dela, e
         # o gate acusava por excecao em vez de acusar o modo consulta -- pelo motivo
         # errado, que num selftest e tao ruim quanto nao acusar.
         lambda s: s.replace("if(preConsulta(el))return;", "", 1),
         "MODO CONSULTA CAIU"),
    ]
    tmpdir = os.path.join(RAIZ, "public", "_gate42_tmp")
    os.makedirs(tmpdir, exist_ok=True)
    rels, meta = [], []
    try:
        for i, (nome, src, prof_flag, muta, esperado) in enumerate(casos):
            p = os.path.join(tmpdir, f"c{i}.html")
            with open(p, "w", encoding="utf-8") as f:
                f.write(muta(src))
            rels.append(os.path.relpath(p, RAIZ))
            meta.append((nome, prof_flag, esperado))
        dados = mede(rels)
        if dados is None:
            return 1
        falhou = False
        for rel, (nome, prof_flag, esperado) in zip(rels, meta):
            errs = avalia(rel, dados[rel], prof_flag)
            bom = any(esperado in e for e in errs)
            print(f"  {'OK  ' if bom else 'FALHA'}  {nome:48} "
                  f"{(errs[0][:52] if errs else 'nao acusou nada')}")
            if not bom:
                falhou = True
    finally:
        for f in glob.glob(os.path.join(tmpdir, "*.html")):
            os.remove(f)
        os.rmdir(tmpdir)
    print()
    if falhou:
        print("SELFTEST FALHOU — alguma regra parou de morder.")
        return 1
    print(f"SELFTEST OK — {len(casos)} defeitos de runtime, todos pegos.")
    return 0


def main():
    if "--selftest" in sys.argv:
        return _selftest()
    alvos = [os.path.relpath(a, RAIZ) if os.path.isabs(a) else a
             for a in sys.argv[1:] if a.endswith(".html")]
    alvos = [a for a in alvos
             if carimbo(open(os.path.join(RAIZ, a), encoding="utf-8").read()) == ANATOMIA] \
        if alvos else alvos_padrao()
    if not alvos:
        print(f"GATE 42 — nenhum arquivo com o carimbo {ANATOMIA}. Nada a clicar.")
        return 0

    print(f"=== GATE 42 — o clique (chromium), anatomia {ANATOMIA} ===")
    dados = mede(alvos)
    if dados is None:
        return 1
    total = 0
    for rel in alvos:
        c = open(os.path.join(RAIZ, rel), encoding="utf-8").read()
        errs = avalia(rel, dados[rel], eh_professor(c))
        d = dados[rel]
        if errs:
            total += len(errs)
            print(f"{VERMELHO}FAIL{ZERA}  {rel}")
            for e in errs:
                print(f"        {e}")
        else:
            t = d.get("tog", {})
            print(f"{VERDE}ok{ZERA}    {rel}  "
                  f"(paineis={len(d.get('paineis', []))} · pre-class "
                  f"{t.get('alternou', 0)}/{t.get('n', 0)})")
    print()
    if total:
        print(f"{VERMELHO}GATE 42 — {total} problema(s) de runtime.{ZERA}")
        return 1
    print(f"GATE 42 OK — {len(alvos)} arquivo(s): nenhum clique estoura, "
          f"todo painel abre, e o pre-class responde a quem deve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
