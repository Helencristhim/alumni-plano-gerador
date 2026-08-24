#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 36 — ISOLAMENTO: a URL do aluno nao entrega nada que nao seja dele.

A REGRA (Stephanie, 24/08/2026; 00 §5, 04 §13, P1 §3.1/§3.2, P2 §3.2, P3 §3)
---------------------------------------------------------------------------
    "A URL do aluno contem exclusivamente o conteudo destinado ao aluno. Gabaritos,
     Teacher's Guide, registros internos, hipoteses pedagogicas, evidencias reservadas e
     controles docentes nao podem estar apenas ocultos no HTML do aluno: nao devem integrar
     o arquivo, payload ou estado entregue por essa URL."

E, no P3 §3, a frase que define o metodo deste gate:

    "display:none nao e separacao. Remover o alternador tambem nao basta. A suite deve
     procurar conteudo e caminhos docentes nos BYTES e nas REQUISICOES do build do aluno."

DUAS MEDICOES, PORQUE SAO DUAS COISAS DIFERENTES
------------------------------------------------
  1. BYTES -- o que o arquivo entrega. Aqui a busca e pela FORMA, nunca pela palavra: um
     comentario que CITA "Teacher's Guide" nao entrega guia nenhum, e reprova-lo ensinaria a
     apagar o comentario em vez do guia (P2 §15: "a mencao nao e a expressao").
  2. ELEVACAO DE PAPEL -- o que alguem consegue FAZER com a pagina aberta. Um arquivo pode
     estar limpo e ainda assim ter a porta: `?mode=teacher-guide`, o alternador, ou uma
     chave no armazenamento que a pagina le e obedece. O gate TENTA as tres, no navegador,
     e exige que nada docente apareca.

A segunda existe porque a primeira, sozinha, aprova o defeito mais provavel: o build do
aluno saiu do build do professor: se o script inicial continuar lendo o papel gravado (era
assim no artefato, e continuou assim na minha primeira derivacao), basta um valor no
localStorage para a pagina se declarar docente. Nenhuma busca por texto acha isso.

USO:
    python3 scripts/black/check_isolamento_aluno.py
    python3 scripts/black/check_isolamento_aluno.py --selftest
"""
import functools
import http.server
import json
import os
import re
import socketserver
import sys
import threading

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ALVOS = ["_build/model/shells/black-aluno.html"]

# (rotulo, regex sobre os BYTES, de quem e aquilo)
FORMAS_DOCENTES = [
    ("nota de conducao", r'data-teacher\s*=\s*"', "a nota do professor, tela a tela"),
    ("painel de gabarito", r'class="ak(-bar)?"', "os gabaritos do pre-class"),
    ("dados do gabarito", r"\bvar\s+PC_NOTAS\s*=", "as respostas das seis atividades"),
    ("Teacher's Guide", r"\bvar\s+GUIDE\s*=\s*\{\s*\d", "os 14 campos do guia, por aula"),
    ("checkpoint", r"\bvar\s+CP\s*=\s*\[", "o instrumento de checkpoint"),
    ("estado pedagogico", r"\bvar\s+EP_MAPA\s*=", "o estado do ciclo"),
    ("escala do registro", r"\bvar\s+(ESCALA|ENGAJ|AVAL_CRIT)\s*=", "o registro pos-aula"),
    ("alternador de visao", r'class="view-switch"', "o controle que troca de papel"),
    # A FORMA, nao a palavra: o comentario do proprio codigo explica a rota escrevendo
    # `?mode=teacher-guide&lesson=N`, e reprovar isso ensinaria a apagar o comentario em vez
    # de fechar a porta. O que se procura e a rota EXPRESSA -- literal de string no JS ou
    # dentro de um atributo.
    ("rota do guia", r"""['\"]teacher-guide['\"]|=["'][^"']*mode=teacher-guide""",
     "a URL que abre o guia"),
    ("deck projetado", r'class="slides-wrapper"', "o in-class, que e do professor"),
    # `getItem(STORE)` e a carga do estado do PROPRIO aluno -- legitima. O que nao pode e
    # o papel SAIR dali: a comparacao contra 'professor'/'aluno'.
    ("papel lido do armazenamento",
     r"\.view\s*===|\bview\s*===\s*['\"](professor|aluno)['\"]",
     "a porta que promove papel por estado"),
    ("elemento marcado como do professor", r'data-view="professor"', "o que o artefato marca"),
]

# O que NAO pode aparecer na pagina depois de uma tentativa de elevacao.
SONDA_ELEVACAO = """() => {
  var r = {};
  r.dataView = document.body.getAttribute('data-view');
  /* o BODY entra na conta quando a propria tentativa poe o atributo nele: o que interessa
     e se apareceu CONTEUDO docente, nao se o atributo que eu mesmo escrevi esta la */
  r.professorNoDom = [].filter.call(document.querySelectorAll('[data-view="professor"]'),
                                    function(e){ return e !== document.body; }).length;
  r.ak = document.querySelectorAll('.ak, .ak-bar').length;
  r.deck = document.querySelectorAll('.slide, .slides-wrapper').length;
  r.guia = document.querySelectorAll('.tg-guia, #teacherPanel, #tgGuiaCabeca').length;
  r.temGUIDE = (typeof GUIDE !== 'undefined') && Object.keys(GUIDE || {}).length > 0;
  r.temNOTAS = (typeof PC_NOTAS !== 'undefined');
  r.temSetView = (typeof setView === 'function');
  return r;
}"""



def descobre(padrao, rotulo):
    """Todo material da anatomia, achado pelo CARIMBO -- nunca por lista escrita aqui.

    Lista no gate envelhece: o material seguinte nasce fora dela e o gate passa dizendo que
    esta tudo bem. O carimbo <meta name="alumni-anatomia" content="private-black"> esta no
    shell, e por isso em tudo que sai dele."""
    import glob
    achados = []
    for caminho in sorted(glob.glob(os.path.join(RAIZ, padrao))):
        try:
            with open(caminho, encoding="utf-8", errors="replace") as fh:
                if 'content="private-black"' not in fh.read(4000):
                    continue
        except OSError:
            continue
        achados.append((rotulo % os.path.basename(caminho),
                        os.path.relpath(caminho, RAIZ), False))
    return achados

def _servidor(diretorio):
    class Silencioso(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a, **k):
            pass
    srv = socketserver.TCPServer(("127.0.0.1", 0),
                                 functools.partial(Silencioso, directory=diretorio))
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, srv.server_address[1]


def confere_bytes(caminho):
    with open(caminho, encoding="utf-8") as fh:
        s = fh.read()
    # A regra do CSS `body[data-view="aluno"] [data-view="professor"]{display:none}` cita o
    # seletor sem entregar elemento nenhum. Folha de estilo nao e markup: procurar
    # `data-view="professor"` dentro dela acusa o inocente -- e foi o que aconteceu na
    # primeira execucao deste gate, com 6 "ocorrencias" que eram uma regra de CSS.
    sem_css = re.sub(r"<style[^>]*>.*?</style>", "", s, flags=re.S)
    # O mesmo raciocinio vale para o <script>: `'<span data-view="professor">'` dentro de uma
    # funcao e um MOLDE, nao um elemento entregue -- e a funcao que o usaria nao e chamada
    # neste build. O que a marca cobra e MARKUP servido ao aluno. O lado do JS ja e coberto
    # pelo nome: GUIDE, PC_NOTAS, CP e EP_MAPA sao procurados como declaracao, e a tentativa
    # de elevacao mede o comportamento.
    so_markup = re.sub(r"<script[^>]*>.*?</script>", "", sem_css, flags=re.S)
    achados = []
    for rotulo, rx, de_quem in FORMAS_DOCENTES:
        alvo = so_markup if rotulo.startswith("elemento marcado") else s
        n = len(re.findall(rx, alvo))
        if n:
            m = re.search(rx, alvo)
            trecho = alvo[max(0, m.start() - 60):m.start() + 60].replace("\n", " ")
            achados.append(f"{rotulo}: {n} ocorrencia(s) — {de_quem}. …{trecho}…")
    return achados


def tenta_elevar(rel):
    """Abre a pagina e tenta virar professor por TRES portas. Nada docente pode aparecer."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("GATE 36 NAO PODE RODAR: playwright ausente.", file=sys.stderr)
        return None
    srv, porta = _servidor(RAIZ)
    saidas = {}
    try:
        with sync_playwright() as p:
            try:
                nav = p.chromium.launch()
            except Exception as e:  # noqa: BLE001
                print(f"GATE 36 NAO PODE RODAR: chromium nao abre ({str(e)[:100]})",
                      file=sys.stderr)
                return None
            url = f"http://127.0.0.1:{porta}/{rel}"

            # porta 1 — o atributo, direto
            pg = nav.new_page()
            pg.goto(url, wait_until="load")
            pg.wait_for_timeout(400)
            pg.evaluate("()=>{document.body.setAttribute('data-view','professor');"
                        "if(typeof setView==='function')setView('professor');}")
            pg.wait_for_timeout(200)
            saidas["atributo"] = pg.evaluate(SONDA_ELEVACAO)
            pg.close()

            # porta 2 — o armazenamento (o papel gravado da sessao do professor)
            pg = nav.new_page()
            pg.add_init_script(
                "try{var k=Object.keys(localStorage);}catch(e){}"
                "localStorage.setItem('pv_private-black-modelo_v1',"
                "JSON.stringify({view:'professor'}));")
            pg.goto(url, wait_until="load")
            pg.wait_for_timeout(400)
            saidas["armazenamento"] = pg.evaluate(SONDA_ELEVACAO)
            pg.close()

            # porta 3 — a query do guia
            pg = nav.new_page()
            pg.goto(url + "?mode=teacher-guide&lesson=19", wait_until="load")
            pg.wait_for_timeout(400)
            saidas["query"] = pg.evaluate(SONDA_ELEVACAO)
            pg.close()
            nav.close()
    finally:
        srv.shutdown()
    return saidas


def avalia_elevacao(saidas):
    erros = []
    for porta, r in saidas.items():
        # Na porta "atributo" quem escreveu 'professor' no body foi o proprio teste: cobrar
        # que o valor tenha voltado seria cobrar que uma pagina estatica resista ao devtools,
        # o que nenhuma resiste. O que importa ali e que NADA docente apareca por causa
        # disso. Nas outras duas portas quem decide o papel e a pagina, e ai o valor conta.
        if porta != "atributo" and r["dataView"] != "aluno":
            erros.append(f"elevacao por {porta}: a pagina passou a se declarar "
                         f"'{r['dataView']}'. O papel nao pode mudar aqui.")
        for chave, rotulo in (("professorNoDom", "elementos marcados como do professor"),
                              ("ak", "paineis de gabarito"),
                              ("deck", "telas do in-class"),
                              ("guia", "painel do Teacher's Guide")):
            if r[chave]:
                erros.append(f"elevacao por {porta}: apareceram {r[chave]} {rotulo}.")
        if r["temGUIDE"]:
            erros.append(f"elevacao por {porta}: o objeto GUIDE tem conteudo.")
        if r["temNOTAS"]:
            erros.append(f"elevacao por {porta}: PC_NOTAS (os gabaritos) existe.")
        if r["temSetView"]:
            erros.append(f"elevacao por {porta}: setView() existe — o alternador e uma rota.")
    return erros


def _selftest():
    import shutil
    import tempfile
    origem = os.path.join(RAIZ, ALVOS[0])
    if not os.path.exists(origem):
        print("FALHA: build do aluno ausente; rode scripts/black/extrai_shell.py")
        return 1
    s = open(origem, encoding="utf-8").read()
    tmp = tempfile.mkdtemp(prefix="isol_", dir=RAIZ)
    rel_dir = os.path.basename(tmp)
    ok = True
    try:
        if confere_bytes(origem):
            print("FALHA: o build do aluno real ja reprova nos bytes.")
            for e in confere_bytes(origem):
                print("   ", e[:150])
            return 1
        print("  OK    build do aluno real passa nos bytes")

        casos = [
            ("gabarito devolvido ao arquivo",
             s.replace("</body>", '<div class="ak">Answer key</div></body>', 1),
             "painel de gabarito"),
            ("nota de conducao devolvida",
             s.replace("<body ", '<body data-teacher="Goal: ..." ', 1),
             "nota de conducao"),
            ("rota do guia devolvida",
             s.replace("</body>", "<script>var u='?mode=teacher-guide';</script></body>", 1),
             "rota do guia"),
        ]
        for rotulo, conteudo, esperado in casos:
            f = os.path.join(tmp, re.sub(r"\W+", "-", rotulo) + ".html")
            open(f, "w", encoding="utf-8").write(conteudo)
            achados = confere_bytes(f)
            if not any(a.startswith(esperado) for a in achados):
                print(f"FALHA: '{rotulo}' NAO foi pego. achados={achados}")
                ok = False
            else:
                print(f"  OK    {rotulo}")

        # a mutacao que so a tentativa de elevacao pega: a pagina volta a ler o papel
        f = os.path.join(tmp, "papel-por-armazenamento.html")
        # A porta so abre se as DUAS travas cairem: o script inicial voltar a ler o papel
        # gravado E o boot deixar de fixa-lo. Com uma so, a outra reverte -- e foi isso que
        # a primeira versao deste caso negativo descobriu: o build resistia a mutacao, e o
        # teste acusava o gate de nao morder quando o defeito e que nao havia defeito.
        # Caso negativo que nao produz o defeito nao prova nada (P2 §22).
        conteudo = s.replace(
            "document.body.setAttribute('data-view','aluno');",
            "try{var d=JSON.parse(localStorage.getItem('pv_private-black-modelo_v1')||'{}');"
            "document.body.setAttribute('data-view',d.view==='professor'?'professor':'aluno');}"
            "catch(e){document.body.setAttribute('data-view','aluno');}", 1)
        conteudo = conteudo.replace(
            "  document.body.setAttribute('data-view','aluno');\n  migraLinguagem();",
            "  migraLinguagem();", 1)
        open(f, "w", encoding="utf-8").write(conteudo)
        saidas = tenta_elevar(f"{rel_dir}/papel-por-armazenamento.html")
        if saidas is None:
            return 1
        erros = avalia_elevacao(saidas)
        if not any("armazenamento" in e for e in erros):
            print("FALHA: papel promovido pelo armazenamento NAO foi pego.")
            ok = False
        else:
            print("  OK    papel promovido pelo armazenamento (so a elevacao pega)")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    if not ok:
        return 1
    print("\nSELFTEST OK — bytes e elevacao de papel, cada um pegando o que so ele pega.")
    return 0


def main():
    if "--selftest" in sys.argv:
        return _selftest()
    print("=== GATE 36 — isolamento do build do aluno ===")
    erros = []
    alvos = list(ALVOS) + [c for _, c, _ in descobre("public/aluno/*.html", "%s")]
    for rel in alvos:
        caminho = os.path.join(RAIZ, rel)
        if not os.path.exists(caminho):
            print(f"  (ausente, ignorado) {rel}")
            continue
        b = confere_bytes(caminho)
        erros += [f"{rel} [bytes] {e}" for e in b]
        saidas = tenta_elevar(rel)
        if saidas is None:
            return 1
        e = avalia_elevacao(saidas)
        erros += [f"{rel} [elevacao] {x}" for x in e]
        print(f"  {'FALHA' if (b or e) else 'ok   '} {rel}  "
              f"bytes={len(b)} elevacao={len(e)} "
              f"(portas testadas: {', '.join(saidas)})")
    if erros:
        print()
        for e in erros:
            print("  FALHA:", e[:220])
        return 1
    print("\nOK — nada docente no arquivo, e nenhuma das tres portas promove papel.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
