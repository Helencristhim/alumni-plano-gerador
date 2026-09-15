#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 75 — dois cartoes da mesma tela nao encostam um no outro.

O DEFEITO (revisao da aula 21 da Gabriela Pires, PR #2626, 14/09/2026)
----------------------------------------------------------------------
    "IN CLASS, slide 10: o .word-bank ("Ways to start") nasce com margin-top 0 e o
     .two-col das opcoes A/B nao tem margin-bottom, entao os cards encostavam (0px)."

E o mesmo defeito, com outra causa, da tela 8 da aula 19 (PR #2595): ao abrir "Show what Maya
actually wrote", a resposta revelada encostava no cartao do Chris logo abaixo.

Os dois estavam em HTML valido, com classe existente e contraste certo — todo gate estatico
passava. So se ve o encosto com a tela desenhada: a margem que falta e a soma do que o CSS
do shell da e do que o fragmento esqueceu de pedir. Por isso este gate MEDE NO NAVEGADOR
(memoria `medir-no-navegador-nao-no-grep`), com os blocos recolhidos ABERTOS — foi aberto
que a aula 19 encostou.

O QUE CONTA COMO CARTAO
-----------------------
Uma caixa que o olho le como caixa: fundo nao transparente, borda visivel ou sombra — e com
largura de bloco (>= 120px). Texto solto nao e cartao; botao dentro de barra tambem nao
(a barra e que se mede).

QUANDO DOIS CARTOES "ENCOSTAM"
------------------------------
B esta logo abaixo de A, os dois se sobrepoem na horizontal, nenhum contem o outro, e a
distancia vertical entre a base de A e o topo de B e menor que 2px.

Fica de fora, pela FORMA e nunca pelo nome da classe:
  - linhas de uma mesma lista dentro de um cartao (irmaos com o MESMO pai e a mesma classe:
    `.phrase-row` numa `.phrase-list`, `.q-item` numa `.qlist`) — ali o empilhamento com
    divisoria e o desenho;
  - celulas de tabela.

ESCOPO: aulas com `geracao.json` gen >= 1 (scripts/consultivo/geracao.py), medidas no
arquivo publicado do PROFESSOR (e o que se projeta). Com `--todas`, mede tudo — e a sonda.

DEPENDENCIA: playwright + chromium. Ausentes, o gate DIZ que nao pode rodar e falha.

USO:
    python3 scripts/consultivo/check_cartoes_encostados.py
    python3 scripts/consultivo/check_cartoes_encostados.py --todas
    python3 scripts/consultivo/check_cartoes_encostados.py --selftest
"""
import functools
import glob
import http.server
import json
import os
import re
import socketserver
import sys
import threading

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(os.path.dirname(AQUI))
sys.path.insert(0, AQUI)
import geracao  # noqa: E402

GEN = 1
LARGURA = 1440
FOLGA = 2          # px: abaixo disto os dois cartoes sao lidos como uma coisa so
VERDE, VERMELHO, ZERA = "\033[32m", "\033[31m", "\033[0m"

SONDA = r"""(folga) => {
  const tela = document.querySelector('.slide.active');
  if (!tela) return [];
  const transparente = (c) => !c || c === 'transparent' || /rgba\([^)]*,\s*0\)$/.test(c);
  const ehCartao = (e) => {
    const cs = getComputedStyle(e);
    if (cs.display === 'none' || cs.visibility === 'hidden' || +cs.opacity === 0) return false;
    if (cs.display === 'inline' || cs.display.startsWith('table') || e.closest('table')) return false;
    const r = e.getBoundingClientRect();
    if (r.width < 120 || r.height < 16) return false;
    const borda = ['Top', 'Right', 'Bottom', 'Left'].some(l =>
      parseFloat(cs['border' + l + 'Width']) > 0 && cs['border' + l + 'Style'] !== 'none'
      && !transparente(cs['border' + l + 'Color']));
    return !transparente(cs.backgroundColor) || borda || cs.boxShadow !== 'none';
  };
  const caixas = Array.from(tela.querySelectorAll('.slide-inner *')).filter(ehCartao);
  const achados = [];
  for (const a of caixas) {
    const ra = a.getBoundingClientRect();
    for (const b of caixas) {
      if (a === b || a.contains(b) || b.contains(a)) continue;
      const rb = b.getBoundingClientRect();
      const gap = rb.top - ra.bottom;
      if (gap < -1 || gap >= folga) continue;
      const sobre = Math.min(ra.right, rb.right) - Math.max(ra.left, rb.left);
      if (sobre < 0.4 * Math.min(ra.width, rb.width)) continue;
      // linhas da mesma lista: mesmo pai, mesma classe -- o empilhamento e o desenho
      if (a.parentElement === b.parentElement && a.className === b.className) continue;
      achados.push({tela: tela.getAttribute('data-slide'), aula: tela.getAttribute('data-lesson'),
                    a: (a.tagName + '.' + String(a.className)).slice(0, 44),
                    b: (b.tagName + '.' + String(b.className)).slice(0, 44),
                    gap: Math.round(gap * 10) / 10,
                    txt: (b.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 40)});
    }
  }
  return achados;
}"""

ABRE_RECOLHIDOS = r"""() => {
  const t = document.querySelector('.slide.active');
  if (!t) return 0;
  let n = 0;
  t.querySelectorAll('[onclick*="abrirBloco"]').forEach((b) => {
    const m = /abrirBloco\('([^']+)'/.exec(b.getAttribute('onclick') || '');
    if (!m) return;
    const alvo = document.getElementById(m[1]);
    if (alvo && (alvo.style.display === 'none' || !alvo.style.display)) { b.click(); n++; }
  });
  return n;
}"""


def publicado(cfg):
    """O arquivo do PROFESSOR que o builder escreve para este config (mesma regra do main)."""
    slug = cfg["slug"]
    nome = cfg.get("arquivo") or (f"{slug}-ciclo{cfg['ciclo']['numero']}"
                                  if cfg.get("fase") == "piloto" else slug)
    return os.path.join("public", "professor", f"{nome}.html")


def alvos(todas):
    """{arquivo publicado: [numeros de aula a medir]}"""
    saida = {}
    for cp in sorted(glob.glob(os.path.join(geracao.BASE, "*", "config.json"))):
        cfg = json.load(open(cp, encoding="utf-8"))
        base = os.path.dirname(cp)
        aulas = [n for n in cfg.get("aulas", [])
                 if todas or geracao.gen(os.path.join(base, f"aula{n}")) >= GEN]
        if aulas:
            saida[publicado(cfg)] = aulas
    return saida


def _servidor():
    class Calado(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a):
            pass

    h = functools.partial(Calado, directory=RAIZ)

    class Q(socketserver.TCPServer):
        allow_reuse_address = True

        def handle_error(self, *a):
            pass

    srv = Q(("127.0.0.1", 0), h)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, srv.server_address[1]


def mede(por_arquivo):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("GATE 75 NAO PODE RODAR: playwright ausente.", file=sys.stderr)
        return None
    out = {}
    srv, porta = _servidor()
    try:
        with sync_playwright() as p:
            try:
                nav = p.chromium.launch()
            except Exception as e:                                    # noqa: BLE001
                print(f"GATE 75 NAO PODE RODAR: chromium nao abre ({str(e)[:120]})",
                      file=sys.stderr)
                return None
            for rel, aulas in por_arquivo.items():
                ctx = nav.new_context(viewport={"width": LARGURA, "height": 900})
                pg = ctx.new_page()
                pg.on("dialog", lambda d: d.dismiss())
                pg.goto(f"http://127.0.0.1:{porta}/{rel}", wait_until="load")
                pg.wait_for_timeout(400)
                achados, telas = [], 0
                for n in aulas:
                    pg.evaluate(f"openLesson({n})")
                    pg.wait_for_timeout(220)
                    visto = None
                    for _ in range(80):
                        pg.wait_for_timeout(120)
                        achados += pg.evaluate(SONDA, FOLGA)
                        if pg.evaluate(ABRE_RECOLHIDOS):
                            pg.wait_for_timeout(120)
                            achados += pg.evaluate(SONDA, FOLGA)
                        telas += 1
                        atual = pg.evaluate(
                            "() => {const s=document.querySelector('.slide.active');"
                            "return s ? s.getAttribute('data-slide') : null}")
                        if atual == visto:
                            break
                        visto = atual
                        pg.evaluate("go(1)")
                        pg.wait_for_timeout(160)
                        if pg.evaluate(
                                "() => {const s=document.querySelector('.slide.active');"
                                "return s ? s.getAttribute('data-slide') : null}") == atual:
                            break
                    pg.evaluate("closeLesson()")
                    pg.wait_for_timeout(120)
                # o mesmo par visto antes e depois de abrir os recolhidos conta uma vez
                unicos = {(a["aula"], a["tela"], a["a"], a["b"]): a for a in achados}
                out[rel] = {"achados": list(unicos.values()), "telas": telas}
                ctx.close()
            nav.close()
    finally:
        srv.shutdown()
    return out


def relata(dados):
    falhas = []
    for rel, d in dados.items():
        for a in d["achados"]:
            falhas.append(f"{rel} aula {a['aula']} tela {a['tela']}: <{a['b']}> encosta em "
                          f"<{a['a']}> ({a['gap']}px) — “{a['txt']}”. Separe com a escala "
                          f"de espaco do Kit (ex.: margin-top:var(--space-4)).")
    return falhas


def main(argv):
    todas = "--todas" in argv
    por = alvos(todas)
    if not por:
        print(f"{VERDE}GATE 75 OK{ZERA} — nenhuma aula com gen >= {GEN} para medir.")
        return 0
    dados = mede(por)
    if dados is None:
        return 1
    falhas = relata(dados)
    for f in falhas:
        print(f"{VERMELHO}FALHA{ZERA} {f}")
    telas = sum(d["telas"] for d in dados.values())
    if falhas:
        print(f"\n{VERMELHO}GATE 75 REPROVOU{ZERA} — {len(falhas)} par(es) de cartoes "
              f"encostados em {telas} tela(s).")
        return 1
    print(f"{VERDE}GATE 75 OK{ZERA} — {telas} tela(s) de "
          f"{sum(len(v) for v in por.values())} aula(s): nenhum cartao encosta no outro.")
    return 0


def selftest():
    """Uma tela do molde com o defeito plantado da aula 21 (dois cartoes sem margem entre
    eles) tem de reprovar; a mesma tela com a margem da correcao, e as linhas de uma lista,
    tem de passar."""
    base = os.path.join(RAIZ, "public", "professor", "stephanie-vicente.html")
    if not os.path.exists(base):
        print("SELFTEST INCONCLUSIVO — o molde publicado nao esta no lugar.")
        return 1
    limpo = open(base, encoding="utf-8").read()
    m = re.search(r'<div class="slide-inner">', limpo)
    if not m:
        print("SELFTEST INCONCLUSIVO — o molde nao tem slide-inner.")
        return 1
    CARTOES = ('<div class="two-col"><div class="brief" style="margin-top:0"><p>Option A</p>'
               '</div><div class="brief" style="margin-top:0"><p>Option B</p></div></div>'
               '<div class="word-bank" style="margin-top:{m}"><p class="wb-rot">Ways to start'
               '</p><p>What &middot; Where</p></div>')
    LISTA = ('<div class="phrase-list"><div class="phrase-row"><span class="phrase-en">One'
             '</span></div><div class="phrase-row"><span class="phrase-en">Two</span></div>'
             '</div>')
    RECOLHIDO = ('<div class="phrase-list"><div class="phrase-row"><span class="phrase-en">'
                 'Maya</span></div></div><div class="btn-bar" style="margin-top:var(--space-2h)">'
                 '<button class="verify-all-btn" onclick="abrirBloco(\'st75\',this)">Show</button>'
                 '</div><div id="st75" style="display:none;margin-top:var(--space-2h)">'
                 '<div class="phrase-list"><div class="phrase-row"><span class="phrase-en">'
                 'Maya, in full</span></div></div></div><div class="phrase-list" style="margin-top:0">'
                 '<div class="phrase-row"><span class="phrase-en">Chris</span></div></div>')
    casos = [
        ("aula 21, tela 10, antes do conserto (margin-top 0)", CARTOES.format(m="0"), True),
        ("a mesma tela com a margem da correcao", CARTOES.format(m="var(--space-4)"), False),
        ("linhas de uma lista empilhadas nao sao defeito", LISTA, False),
        ("aula 19, tela 8: o revelado encosta no cartao de baixo", RECOLHIDO, True),
    ]
    tmpdir = os.path.join(RAIZ, "public", "_gate75_tmp")
    os.makedirs(tmpdir, exist_ok=True)
    por, meta = {}, {}
    try:
        for i, (nome, html_, deve) in enumerate(casos):
            s = limpo[:m.end()] + html_ + limpo[m.end():]
            p = os.path.join(tmpdir, f"c{i}.html")
            open(p, "w", encoding="utf-8").write(s)
            rel = os.path.relpath(p, RAIZ)
            por[rel] = [1]
            meta[rel] = (nome, deve)
        dados = mede(por)
        if dados is None:
            return 1
        erros = 0
        for rel, (nome, deve) in meta.items():
            # so conta o que foi plantado: a tela 1 da aula 1 do molde
            pegou = any(a["tela"] == "1" and a["aula"] == "1" for a in dados[rel]["achados"])
            ok = pegou == deve
            erros += not ok
            print(f"  {(VERDE + 'ok' + ZERA) if ok else (VERMELHO + 'ERRO' + ZERA)}  {nome}: "
                  f"esperado {'FALHA' if deve else 'passa'}, deu {'FALHA' if pegou else 'passa'}")
    finally:
        for f in glob.glob(os.path.join(tmpdir, "*.html")):
            os.remove(f)
        os.rmdir(tmpdir)
    print("SELFTEST OK" if not erros else f"SELFTEST com {erros} erro(s)")
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv[1:] else main(sys.argv[1:]))
