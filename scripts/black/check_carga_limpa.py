#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 35 — CARGA LIMPA: a pagina abre sem erro e os componentes existem, contados.

POR QUE ISTO EXISTE (P3 §1.1)
-----------------------------
    "Antes de qualquer verificacao de conteudo, a pagina abre e o console fica limpo. Este
     teste custa segundos e vale mais que centenas de checagens de texto, porque e o unico
     que enxerga a classe de defeito que nenhuma delas alcanca."

O caso que originou a regra, no proprio artefato de referencia: um acesso de propriedade
sobrevivente a um renome derrubava o preenchimento do pre-class -- e o que sumiu foi o
transporte de audio do material INTEIRO. O texto estava intacto: a funcao existia, o
identificador existia, e 435 casos negativos estaticos passaram.

E ACONTECEU AQUI, na primeira derivacao do shell (24/08/2026). Eu troquei a chave de estado
por `var STORE='pv_'+artefatoId()+'_v1'` -- correto pelo P1 §3, que proibe dado pessoal em
identificador tecnico. So que `var STORE` aparece na secao de persistencia, muito antes de
`var ARTEFATO` existir: artefatoId() rodava com ARTEFATO undefined, o boot morria na
primeira linha e levava junto TODOS os construtores. Nenhum gate estatico viu. Este viu, e
o artefato ao lado -- que boota limpo -- provou que o defeito era meu, nao dele.

AS DUAS EVIDENCIAS SAO DISTINTAS (e o P3 exige as duas)
-------------------------------------------------------
    "introduzir um erro em qualquer funcao do boot e confirmar que a suite reprova por nao
     haver componente construido, e nao apenas por haver erro no console -- as duas
     evidencias sao distintas, e a segunda sem a primeira deixa passar um construtor que
     falha em silencio."

Por isso o gate mede DUAS coisas: console limpo E componente construido. Um construtor que
engole a propria excecao (try/catch, ou um `if(!host)return` sobre um host que sumiu) nao
produz erro nenhum -- e a peca simplesmente nao esta la.

MEDIR CONSTRUCAO, NAO TEXTO -- E POR QUE ISSO EXIGIU UM TRUQUE
--------------------------------------------------------------
O artefato de referencia foi SALVO PELO NAVEGADOR: o .html que se guarda de uma pagina viva
e o DOM DEPOIS do boot. Ou seja, os players, os paineis de gabarito e o mapa do ciclo ja
vem escritos no arquivo. Contar `.aud-stop` no documento carregado, portanto, nao prova que
o construtor rodou -- prova que ALGUEM escreveu aquilo, um dia. Descobri isso aqui: quebrei
o boot de proposito e todas as contagens continuaram batendo.

Por isso o gate LIMPA OS HOSTS antes de o boot rodar. Um script de inicializacao registra o
seu DOMContentLoaded ANTES de qualquer script da pagina (e por isso roda primeiro), apaga o
que os construtores deveriam produzir, e so entao o boot da pagina acontece. O que aparecer
depois foi CONSTRUIDO agora.

E a mesma licao que este repo ja pagou noutra forma: defeito de comportamento se mede
mexendo no mecanismo, nao procurando a classe no texto.

O N DERIVA DA PAGINA, NUNCA DESTE ARQUIVO
------------------------------------------
Nenhuma contagem esperada esta escrita aqui (P2 §17: "para slides, telas e componentes, N
deriva dos blocos existentes"). Cada componente declara COMO derivar o esperado do proprio
documento -- numero de aulas do registro, numero de secoes do pre-class, tamanho da lista
que o construtor percorre. Uma constante aqui reprovaria a aula seguinte, que tem outra
quantidade, e pareceria rigor.

O ARTEFATO E CONTROLE POSITIVO
------------------------------
Ele roda junto, toda vez. Se o artefato falhar, o defeito e do AFERIDOR (playwright, versao
do chromium, servidor local), nao do shell -- e o gate diz isso em vez de acusar o inocente.

USO:
    python3 scripts/black/check_carga_limpa.py
    python3 scripts/black/check_carga_limpa.py --selftest
"""
import functools
import http.server
import json
import os
import socketserver
import sys
import threading

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# (rotulo, caminho relativo, e_controle_positivo)
ALVOS = [
    ("artefato (controle positivo)", "_build/model/artefatos/marcos-private-black.html", True),
    ("shell professor", "_build/model/shells/black.html", False),
    ("shell aluno", "_build/model/shells/black-aluno.html", False),
]

# Cada componente: como CONTAR o construido e como DERIVAR o esperado, os dois do proprio
# documento. `esperado` devolvendo 0 significa "nao ha o que construir aqui" e o item e
# pulado -- e como o mesmo gate serve a um build que legitimamente nao tem aquela peca.
COMPONENTES = [
    ("player de audio",
     "document.querySelectorAll('.aud-stop').length",
     "document.querySelectorAll('[data-audgrupo]').length"),
    # o mapa mostra o CICLO inteiro, nao so as aulas ja escritas: as posteriores aparecem
    # como "ainda indisponivel". Por isso o esperado sai de CICLO.aulas, e nao de LESSONS --
    # foi o proprio gate que me corrigiu aqui, acusando 20 construidos contra 2 esperados.
    ("mapa de aulas do ciclo",
     "(document.getElementById('cicloMapa')||{}).childElementCount||0",
     "(typeof CICLO==='undefined')?0:CICLO.aulas"),
    ("answer key do pre-class",
     "document.querySelectorAll('.ak').length",
     "(typeof PC_NOTAS==='undefined')?0:Object.keys(PC_NOTAS).length"),
    ("escala do registro pos-aula",
     "document.querySelectorAll('.aval-op').length",
     "document.querySelectorAll('.aval-escala').length&&"
     "document.querySelectorAll('.aval-escala').length*0+"
     "[].reduce.call(document.querySelectorAll('.aval-escala'),function(a,g){"
     "return a+((g.getAttribute('data-esc')==='engaj')?ENGAJ.length:ESCALA.length);},0)"),
    ("checklist do checkpoint",
     "(document.getElementById('cp-checklist')||{}).childElementCount||0",
     "(typeof CP==='undefined')?0:CP.length"),
    # O esperado sai de LESSONS.nav SO quando ha deck: o build do aluno nao tem deck, e
    # LESSONS continua la (o mapa do ciclo precisa dele). Sem esta condicao, o gate cobraria
    # 20 telas de um arquivo que legitimamente nao tem nenhuma.
    ("telas do deck",
     "document.querySelectorAll('.slide').length",
     "(!document.querySelector('.slides-wrapper')||typeof LESSONS==='undefined')?0:"
     "Object.keys(LESSONS).reduce(function(a,k){return a+((LESSONS[k].nav||[]).length);},0)"),
]

# Apaga o que os construtores deveriam produzir. Roda no DOMContentLoaded registrado ANTES
# dos scripts da pagina -- ouvintes disparam na ordem de registro, entao este vem primeiro.
# Cada linha desfaz TAMBEM a marca que faz o construtor pular ("ja existe"): sem isso o
# construtor decide que nao ha nada a fazer e a limpeza vira um apagao permanente.
LIMPEZA = """
document.addEventListener('DOMContentLoaded', function(){
  var i, ns;
  ns = document.querySelectorAll('.ak, .ak-bar');
  for (i=0;i<ns.length;i++) ns[i].parentNode.removeChild(ns[i]);
  ns = document.querySelectorAll('.aud-stop');
  for (i=0;i<ns.length;i++) ns[i].parentNode.removeChild(ns[i]);
  ns = document.querySelectorAll('[data-audgrupo]');
  for (i=0;i<ns.length;i++) ns[i].removeAttribute('data-audgrupo');
  ns = document.querySelectorAll('#cicloMapa, #cp-checklist, #gdsort, #ts19, [data-brief], .aval-escala');
  for (i=0;i<ns.length;i++) ns[i].innerHTML = '';
}, false);
"""

SONDA = """() => {
  var r = {};
  %s
  return r;
}"""


def _servidor(diretorio):
    class Silencioso(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a, **k):
            pass
    handler = functools.partial(Silencioso, directory=diretorio)
    srv = socketserver.TCPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, srv.server_address[1]


def mede(caminhos):
    """Abre cada arquivo no chromium e devolve {caminho: {erros, componentes}}.

    Serve por HTTP: file:// costuma estar bloqueado para automacao, e o artefato publicado
    roda em origem isolada (P2 §26)."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("GATE 35 NAO PODE RODAR: playwright ausente. "
              "`pip install playwright && python3 -m playwright install chromium`.",
              file=sys.stderr)
        return None

    sonda = SONDA % "\n  ".join(
        f"r[{json.dumps(nome)}]={{feito:({feito}),esperado:({esperado})}};"
        for nome, feito, esperado in COMPONENTES)

    out = {}
    srv, porta = _servidor(RAIZ)
    try:
        with sync_playwright() as p:
            try:
                nav = p.chromium.launch()
            except Exception as e:  # noqa: BLE001
                print(f"GATE 35 NAO PODE RODAR: chromium nao abre ({str(e)[:120]})",
                      file=sys.stderr)
                return None
            for rel in caminhos:
                pg = nav.new_page()
                pg.add_init_script(LIMPEZA)
                erros = []
                pg.on("pageerror", lambda e: erros.append(str(e)))
                pg.on("console",
                      lambda m: erros.append("console.error: " + m.text)
                      if m.type == "error" else None)
                pg.goto(f"http://127.0.0.1:{porta}/{rel}", wait_until="load")
                pg.wait_for_timeout(600)
                try:
                    comp = pg.evaluate(sonda)
                except Exception as e:  # noqa: BLE001
                    comp = {"__sonda__": {"feito": -1, "esperado": str(e)[:90]}}
                out[rel] = {"erros": erros, "componentes": comp}
                pg.close()
            nav.close()
    finally:
        srv.shutdown()
    return out


def avalia(rel, dados, controle):
    erros = []
    if dados["erros"]:
        quem = "O AFERIDOR" if controle else "o arquivo"
        erros.append(f"{rel}: {len(dados['erros'])} erro(s) na carga — o problema e {quem}. "
                     f"Primeiro: {dados['erros'][0][:160]}")
    for nome, c in dados["componentes"].items():
        esperado, feito = c.get("esperado"), c.get("feito")
        if not isinstance(esperado, int) or esperado == 0:
            continue
        if feito != esperado:
            erros.append(f"{rel}: '{nome}' construiu {feito} de {esperado} — "
                         f"construtor que nao rodou, ou rodou e falhou em silencio.")
    return erros


def _selftest():
    """Duas mutacoes, porque as duas evidencias sao distintas (P3 §1.1)."""
    import shutil
    import tempfile
    origem = os.path.join(RAIZ, "_build", "model", "shells", "black.html")
    if not os.path.exists(origem):
        print("FALHA: shell ausente; rode scripts/black/extrai_shell.py")
        return 1
    tmp = tempfile.mkdtemp(prefix="carga_", dir=RAIZ)
    rel_dir = os.path.basename(tmp)
    try:
        s = open(origem, encoding="utf-8").read()
        # (a) erro no boot: reprova pelo console E por componente ausente
        a = os.path.join(tmp, "erro-no-boot.html")
        open(a, "w", encoding="utf-8").write(
            s.replace("document.addEventListener('DOMContentLoaded',function(){\n  deckInit(",
                      "document.addEventListener('DOMContentLoaded',function(){\n"
                      "  NAO_EXISTE.x=1; deckInit(", 1))
        # (b) construtor que falha EM SILENCIO: o host some, o `if(!host)return` engole,
        #     console limpo, peca ausente. E o caso que a checagem de console sozinha perde.
        b = os.path.join(tmp, "silencio.html")
        open(b, "w", encoding="utf-8").write(
            s.replace('id="cp-checklist"', 'id="cp-checklist-sumiu"', 1))

        res = mede([f"{rel_dir}/erro-no-boot.html", f"{rel_dir}/silencio.html"])
        if res is None:
            return 1
        ea = avalia("a", res[f"{rel_dir}/erro-no-boot.html"], False)
        eb = avalia("b", res[f"{rel_dir}/silencio.html"], False)
        ok = True
        if not any("erro(s) na carga" in e for e in ea):
            print("FALHA: erro no boot NAO foi pego pelo console."); ok = False
        else:
            print("  OK    erro no boot -> console")
        if not any("construiu" in e for e in ea):
            print("FALHA: erro no boot NAO derrubou componente — a 2a evidencia falta.")
            ok = False
        else:
            print("  OK    erro no boot -> componente ausente (as duas evidencias)")
        if any("erro(s) na carga" in e for e in eb):
            print("FALHA: o caso do silencio deveria ter console LIMPO."); ok = False
        elif not any("construiu" in e for e in eb):
            print("FALHA: construtor que falha em silencio NAO foi pego."); ok = False
        else:
            print("  OK    construtor silencioso -> pego so pela contagem")
        if not ok:
            return 1
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print("\nSELFTEST OK — as duas evidencias sao medidas em separado.")
    return 0


def main():
    if "--selftest" in sys.argv:
        return _selftest()
    print("=== GATE 35 — carga limpa (chromium) ===")
    alvos = [(r, c, ctrl) for r, c, ctrl in ALVOS if os.path.exists(os.path.join(RAIZ, c))]
    res = mede([c for _, c, _ in alvos])
    if res is None:
        return 1
    erros = []
    for rotulo, caminho, controle in alvos:
        d = res[caminho]
        e = avalia(rotulo, d, controle)
        erros += e
        marca = "FALHA" if e else "ok   "
        comp = d["componentes"]
        resumo = " ".join(f"{n.split()[0]}={c['feito']}" for n, c in comp.items()
                          if isinstance(c.get("esperado"), int) and c["esperado"])
        print(f"  {marca} {rotulo:32s} erros={len(d['erros'])}  {resumo}")
    if erros:
        print()
        for e in erros:
            print("  FALHA:", e)
        return 1
    print("\nOK — carga limpa e componentes construidos, contados contra o proprio documento.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
