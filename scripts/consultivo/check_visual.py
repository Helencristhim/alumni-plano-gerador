#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 43 — nada sai da tela nem fica cortado, em nenhuma largura (REG-006).

    REG-006 · Sobreposicao ou corte visual · BLOCKER
    "Texto, botoes, players, perguntas ou expansoes se sobrepoem, sao cortados ou
     extrapolam larguras suportadas."  — Detectacao recomendada: Visual.

Mede em 375, 768, 1024 e 1440 -- celular, tablet, laptop e monitor.

AS TRES PERGUNTAS, E POR QUE ELAS E NAO OUTRAS
------------------------------------------------
 1. **A pagina rola de lado?** `scrollWidth > viewport` e o sintoma mais duro e menos
    ambiguo de layout estourado. Nenhuma excecao: material que rola horizontalmente esta
    quebrado, e ponto.

 2. **Algo ultrapassa a viewport SEM ter onde rolar?** Aqui mora a unica sutileza que
    importa. Uma tabela de 660px numa tela de 375 NAO e defeito -- e o padrao correto,
    desde que ela role DENTRO do proprio container (`overflow-x:auto`). Medi o molde antes
    de escrever a regra: a 375px havia 31 elementos "fora da viewport" no professor e 24 no
    aluno, e TODOS eram tabela ou barra de abas com scroll proprio. Uma regra que so olhasse
    a caixa acusaria 55 defeitos inexistentes na primeira execucao.

 3. **Ha texto visivel cortado?** Elemento com `overflow:hidden` cujo conteudo nao cabe.

O sr-only NAO conta, e a exclusao e pelo MECANISMO
---------------------------------------------------
O texto que existe so para leitor de tela e cortado DE PROPOSITO -- 1x1 px com
`clip:rect(0 0 0 0)`. No molde sao 20 spans assim, e a primeira versao desta regra os
acusou todos.

A exclusao NAO e por nome de classe (`.so-leitor`): nome muda, e um gate que dependa dele
para de enxergar sem avisar. E pela FORMA do padrao -- caixa de 1px ou `clip` aplicado.
Assim ele continua valendo se a classe for renomeada, e continua NAO valendo para um
elemento que so por acaso se chame parecido.

O QUE NAO ESTA AQUI
--------------------
REG-007 ("hierarquia visual incorreta": pergunta interna sem destaque proprio). Depende de
comparar peso, tamanho e espacamento com uma intencao de design que so existe na cabeca de
quem desenhou. Nao ha limiar honesto -- e um limiar desonesto vira ruido.

ESCOPO: o carimbo `alumni-anatomia=consultivo`.
DEPENDENCIA: playwright + chromium. Ausentes, o gate DIZ que nao pode rodar e falha.

USO:
    python3 scripts/consultivo/check_visual.py [arquivo.html ...]
    python3 scripts/consultivo/check_visual.py --selftest
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
LARGURAS = [375, 768, 1024, 1440]
VERDE, VERMELHO, ZERA = "\033[32m", "\033[31m", "\033[0m"

SONDA = r"""(w) => {
  const de = document.documentElement, b = document.body;
  const rolaLateral = Math.max(de.scrollWidth, b.scrollWidth) - w;

  // um ancestral que role horizontalmente torna legitimo o filho ser mais largo que a tela
  const podeRolar = (e) => {
    for (let p = e.parentElement; p; p = p.parentElement) {
      const o = getComputedStyle(p);
      if (o.overflowX === 'auto' || o.overflowX === 'scroll'
          || o.overflow === 'auto' || o.overflow === 'scroll') return true;
    }
    return false;
  };

  // o padrao "so para leitor de tela": caixa de 1px, ou clip aplicado. Pela FORMA, nunca
  // pelo nome da classe.
  const soLeitor = (e, cs) =>
    (e.clientWidth <= 1 && e.clientHeight <= 1)
    || (cs.clip && cs.clip !== 'auto')
    || (cs.clipPath && cs.clipPath !== 'none' && e.clientHeight <= 1);

  const vazando = [], cortados = [];
  document.querySelectorAll('body *').forEach((e) => {
    const cs = getComputedStyle(e);
    if (cs.display === 'none' || cs.visibility === 'hidden') return;
    const r = e.getBoundingClientRect();
    if (r.width === 0 && r.height === 0) return;

    if ((r.right > w + 1 || r.left < -1) && !podeRolar(e) && !soLeitor(e, cs)) {
      vazando.push({tag: e.tagName, cls: (e.className || '').toString().slice(0, 34),
                    esq: Math.round(r.left), dir: Math.round(r.right),
                    txt: (e.textContent || '').trim().slice(0, 34)});
    }
    const escondeY = cs.overflowY === 'hidden' || cs.overflow === 'hidden';
    if (escondeY && e.scrollHeight > e.clientHeight + 2 && e.clientHeight > 0
        && e.children.length === 0 && (e.textContent || '').trim().length > 10
        && !soLeitor(e, cs)) {
      cortados.push({tag: e.tagName, cls: (e.className || '').toString().slice(0, 34),
                     txt: (e.textContent || '').trim().slice(0, 40),
                     cabe: e.clientHeight, precisa: e.scrollHeight});
    }
  });
  return {rolaLateral, vazando: vazando.slice(0, 6), nVaz: vazando.length,
          cortados: cortados.slice(0, 6), nCort: cortados.length};
}"""


def carimbo(c):
    m = re.search(r'<meta\s+name="alumni-anatomia"\s+content="([^"]+)"', c[:4000])
    return m.group(1) if m else None


def _servidor():
    h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=RAIZ)

    class Q(socketserver.TCPServer):
        allow_reuse_address = True

        def handle_error(self, *a):
            pass          # 404 de MP3 nao materializado nao e assunto deste gate

    srv = Q(("127.0.0.1", 0), h)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, srv.server_address[1]


def mede(rels):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("GATE 43 NAO PODE RODAR: playwright ausente. "
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
                print(f"GATE 43 NAO PODE RODAR: chromium nao abre ({str(e)[:120]})",
                      file=sys.stderr)
                return None
            for rel in rels:
                out[rel] = {}
                for w in LARGURAS:
                    ctx = nav.new_context(viewport={"width": w, "height": 900})
                    pg = ctx.new_page()
                    pg.on("dialog", lambda d: d.dismiss())
                    pg.goto(f"http://127.0.0.1:{porta}/{rel}", wait_until="load")
                    pg.wait_for_timeout(450)
                    try:
                        out[rel][w] = pg.evaluate(SONDA, w)
                    except Exception as e:                            # noqa: BLE001
                        out[rel][w] = {"__sonda__": str(e)[:140]}
                    ctx.close()
            nav.close()
    finally:
        srv.shutdown()
    return out


def avalia(rel, por_largura):
    erros = []
    for w, d in sorted(por_largura.items()):
        if "__sonda__" in d:
            erros.append(f"{w}px: a sonda nao rodou — {d['__sonda__']}")
            continue
        if d["rolaLateral"] > 0:
            erros.append(f"REG-006 · {w}px: a pagina ROLA DE LADO "
                         f"({d['rolaLateral']}px a mais). Material nao rola horizontalmente.")
        for v in d["vazando"]:
            erros.append(f"REG-006 · {w}px: <{v['tag'].lower()} class=\"{v['cls']}\"> sai da "
                         f"tela ({v['esq']}..{v['dir']}) e nao tem onde rolar. "
                         f"{'Texto: ' + v['txt'] if v['txt'] else ''}")
        if d["nVaz"] > len(d["vazando"]):
            erros.append(f"REG-006 · {w}px: e mais {d['nVaz'] - len(d['vazando'])} "
                         f"elemento(s) fora da tela.")
        for c in d["cortados"]:
            erros.append(f"REG-006 · {w}px: texto CORTADO em <{c['tag'].lower()} "
                         f"class=\"{c['cls']}\"> — cabe {c['cabe']}px, precisa de "
                         f"{c['precisa']}px. \"{c['txt']}\"")
        if d["nCort"] > len(d["cortados"]):
            erros.append(f"REG-006 · {w}px: e mais {d['nCort'] - len(d['cortados'])} "
                         f"trecho(s) cortado(s).")
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
    base = os.path.join(RAIZ, "public", "aluno", "stephanie-vicente.html")
    if not os.path.exists(base):
        print("SELFTEST INCONCLUSIVO — o molde nao esta no lugar.")
        return 1
    limpo = open(base, encoding="utf-8").read()
    casos = [
        ("REG-006 a pagina rola de lado",
         lambda s: s.replace("</body>",
                             '<div style="width:2200px;height:8px"></div></body>', 1),
         "ROLA DE LADO"),
        ("REG-006 elemento fora da tela, sem onde rolar",
         lambda s: s.replace("</body>",
                             '<div style="position:absolute;left:3000px;top:10px;width:60px;'
                             'height:20px">fora</div></body>', 1),
         "sai da tela"),
        ("REG-006 texto cortado dentro da caixa",
         lambda s: s.replace("</body>",
                             '<p style="height:12px;overflow:hidden;width:200px">'
                             'texto que nao cabe nesta caixa de jeito nenhum, de forma alguma'
                             '</p></body>', 1),
         "CORTADO"),
        ("texto so para leitor de tela — NAO pode reprovar",
         lambda s: s.replace("</body>",
                             '<span style="position:absolute;width:1px;height:1px;'
                             'overflow:hidden;clip:rect(0 0 0 0)">aviso para leitor de tela'
                             '</span></body>', 1),
         None),
    ]
    tmpdir = os.path.join(RAIZ, "public", "_gate43_tmp")
    os.makedirs(tmpdir, exist_ok=True)
    rels, meta = [], []
    try:
        for i, (nome, muta, esperado) in enumerate(casos):
            p = os.path.join(tmpdir, f"c{i}.html")
            with open(p, "w", encoding="utf-8") as f:
                f.write(muta(limpo))
            rels.append(os.path.relpath(p, RAIZ))
            meta.append((nome, esperado))
        dados = mede(rels)
        if dados is None:
            return 1
        falhou = False
        for rel, (nome, esperado) in zip(rels, meta):
            errs = avalia(rel, dados[rel])
            if esperado is None:
                bom = not errs
                motivo = "ignorado, como deve" if bom else f"REPROVOU: {errs[0][:44]}"
            else:
                bom = any(esperado in e for e in errs)
                motivo = (errs[0][:52] if errs else "nao acusou nada")
            print(f"  {'OK  ' if bom else 'FALHA'}  {nome:46} {motivo}")
            if not bom:
                falhou = True
    finally:
        for f in glob.glob(os.path.join(tmpdir, "*.html")):
            os.remove(f)
        os.rmdir(tmpdir)
    print()
    if falhou:
        print("SELFTEST FALHOU — a regra parou de morder, ou passou a morder demais.")
        return 1
    print(f"SELFTEST OK — {len(casos)} casos: 3 defeitos pegos, 1 recorte legitimo poupado.")
    return 0


def main():
    if "--selftest" in sys.argv:
        return _selftest()
    alvos = [a for a in sys.argv[1:] if a.endswith(".html")] or alvos_padrao()
    if not alvos:
        print(f"GATE 43 — nenhum arquivo com o carimbo {ANATOMIA}.")
        return 0
    print(f"=== GATE 43 — layout em {', '.join(str(w) for w in LARGURAS)}px "
          f"(chromium), anatomia {ANATOMIA} ===")
    dados = mede(alvos)
    if dados is None:
        return 1
    total = 0
    for rel in alvos:
        errs = avalia(rel, dados[rel])
        if errs:
            total += len(errs)
            print(f"{VERMELHO}FAIL{ZERA}  {rel}")
            for e in errs[:12]:
                print(f"        {e}")
        else:
            print(f"{VERDE}ok{ZERA}    {rel}  ({len(LARGURAS)} larguras)")
    print()
    if total:
        print(f"{VERMELHO}GATE 43 — {total} problema(s) de layout.{ZERA}")
        return 1
    print(f"GATE 43 OK — {len(alvos)} arquivo(s): nada rola de lado, nada sai da tela, "
          f"nada fica cortado.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
