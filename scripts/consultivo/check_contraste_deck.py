#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 52 — nada fica ilegivel nas telas ESCURAS do deck (REG-005).

POR QUE ISTO EXISTE (02/09/2026)
--------------------------------
Revisao do Dan sobre a aula 9 da Joice:

    "No slide 06, a pergunta [...] fica apagada, sem contraste com o fundo escuro E o
     botao 'Check' tambem fica pouco visivel."

Medido no navegador, com a razao WCAG computada sobre o fundo real:

    .verify-all-btn.ghost   1.49 : 1     -- o botao "Check" some no fundo
    .task-instr             1.75 : 1     -- o ENUNCIADO do exercicio some

Eram 28 ocorrencias em 4 dos 6 materiais. A causa nao foi uma cor errada: foi uma regra
que nunca chegou a ser escrita. `.btn-ghost`, `.audio-btn-sm.ghost` e `.aud-estado` todos
tem a variante `.slide-dark`/`.slide-open` logo abaixo da regra clara; estas duas nasceram
sem a delas e ficaram com a cor do fundo claro (`--accent` #003080, `--text-mid` #33405E).

    Peca que herda a cor do tema claro numa tela escura nao da erro, nao quebra layout e
    passa em todo gate estatico. Ela simplesmente nao e lida -- e quem esta na aula supoe
    que o exercicio e daquele jeito.

O caso do enunciado e o pior: a tela mostra as alternativas e esconde a PERGUNTA. E a
mesma familia da REGRA 2.1 do CLAUDE.md ("a pergunta vem antes do audio") por outro
caminho -- ali a tarefa nascia com `display:none`, aqui ela nasce da cor do fundo.

O QUE ELE MEDE
--------------
Tela a tela, DENTRO do deck aberto (as telas nascem em display:none; medir a pagina
parada mede zero elementos e devolve verde falso), e com os blocos recolhiveis da tela JA
ABERTOS -- o que a professora mostra com um clique na aula e tela como o resto. Para cada
elemento com texto proprio numa tela `.slide-dark`/`.slide-open`:

    razao WCAG entre a cor computada do texto e o fundo EFETIVO

O fundo efetivo sobe a arvore compondo as camadas semitransparentes ate achar uma opaca --
`rgba(255,255,255,.06)` sobre azul-marinho e azul-marinho, nao branco. Texto com alpha e
composto do mesmo jeito. Limiar 4.5:1, ou 3.0:1 quando o texto e grande (>=24px, ou
>=18.66px em negrito), que e o que a WCAG AA define.

O QUE ELE NAO MEDE
------------------
As telas CLARAS. Nao por serem menos importantes, mas porque a origem do defeito e
especifica: e a variante escura que falta. Um gate que varresse tudo mediria tambem os
cinzas deliberados do tema claro, e a discussao sobre eles nao e esta.

ESCOPO: o carimbo `alumni-anatomia=consultivo`, e so o arquivo do PROFESSOR -- o do aluno
nao tem deck (GATE 36), entao nao ha tela escura para medir.
DEPENDENCIA: playwright + chromium. Ausentes, o gate DIZ que nao pode rodar e falha.

USO:
    python3 scripts/consultivo/check_contraste_deck.py [arquivo.html ...]
    python3 scripts/consultivo/check_contraste_deck.py --selftest
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

# A sonda mede a tela ATIVA. Quem anda pelas telas e o main, chamando a navegacao da
# propria pagina -- assim a medicao ve o que a professora ve, e nao um DOM que o gate
# tornou visivel a forca.
SONDA = r"""() => {
  const lum = (c) => {
    const f = (v) => { v /= 255; return v <= 0.03928 ? v/12.92 : Math.pow((v+0.055)/1.055, 2.4); };
    return 0.2126*f(c[0]) + 0.7152*f(c[1]) + 0.0722*f(c[2]);
  };
  const parse = (s) => {
    const m = String(s).match(/rgba?\(([\d.]+),\s*([\d.]+),\s*([\d.]+)(?:,\s*([\d.]+))?/);
    return m ? [+m[1], +m[2], +m[3], m[4] === undefined ? 1 : +m[4]] : null;
  };
  // camada semitransparente sobre o que esta atras dela
  const sobre = (f, b) => [f[0]*f[3] + b[0]*(1-f[3]), f[1]*f[3] + b[1]*(1-f[3]),
                           f[2]*f[3] + b[2]*(1-f[3]), 1];
  // o fundo EFETIVO: sobe ate achar uma camada opaca e recompoe as translucidas por cima
  const fundoDe = (el) => {
    const pilha = [];
    for (let n = el; n && n !== document.documentElement; n = n.parentElement) {
      const c = parse(getComputedStyle(n).backgroundColor);
      if (c && c[3] > 0) { pilha.push(c); if (c[3] >= 0.999) break; }
    }
    let base = [255, 255, 255, 1];
    if (pilha.length && pilha[pilha.length-1][3] >= 0.999) base = pilha.pop();
    for (let i = pilha.length - 1; i >= 0; i--) base = sobre(pilha[i], base);
    return base;
  };
  const razao = (a, b) => {
    const la = lum(a), lb = lum(b), hi = Math.max(la, lb), lo = Math.min(la, lb);
    return (hi + 0.05) / (lo + 0.05);
  };
  const tela = document.querySelector('.slide.active');
  if (!tela || !/slide-dark|slide-open/.test(tela.className)) return [];
  const achados = [];
  tela.querySelectorAll('*').forEach((el) => {
    // so o texto do PROPRIO elemento: senao o container herda o pior filho e o relatorio
    // aponta para a caixa em vez da linha
    const txt = Array.from(el.childNodes).filter(n => n.nodeType === 3)
      .map(n => n.textContent.trim()).join(' ').trim();
    if (!txt) return;
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden' || +cs.opacity === 0) return;
    if (!el.getClientRects().length) return;
    const fg0 = parse(cs.color); if (!fg0) return;
    const bg = fundoDe(el);
    const fg = fg0[3] < 1 ? sobre(fg0, bg) : fg0;
    const px = parseFloat(cs.fontSize), peso = parseInt(cs.fontWeight) || 400;
    const lim = ((px >= 24) || (px >= 18.66 && peso >= 700)) ? 3.0 : 4.5;
    const r = razao(fg, bg);
    if (r < lim) achados.push({
      tela: tela.getAttribute('data-slide'), aula: tela.getAttribute('data-lesson'),
      cls: String(el.className || '').slice(0, 40), tag: el.tagName.toLowerCase(),
      txt: txt.slice(0, 46), razao: Math.round(r * 100) / 100, lim,
      cor: cs.color, fundo: 'rgb(' + bg.slice(0, 3).map(Math.round).join(',') + ')'});
  });
  return achados;
}"""


# OS BLOCOS QUE O PROFESSOR ABRE NA AULA TAMBEM SAO TELA (revisao de 03/09/2026)
#
# A sonda pula `display:none`, e esta certa: o que nunca aparece nao tem contraste a medir.
# Mas parte do deck NASCE fechada e abre com um clique durante a aula -- o Replay, a nova
# reserva, o apoio da tela 8. Para o gate, "fechado" e "inexistente" eram a mesma coisa: um
# `.doc-brief` sem par escuro dentro de uma `.slide-dark` passou verde porque estava
# recolhido, e so ia aparecer projetado, na aula, no momento em que a aluna precisasse dele.
#
# Entao a tela e medida com tudo o que ela pode mostrar aberto. E o mesmo criterio do resto:
# medir o que a professora VE, e nao o que o arquivo tem.
ABRE_RECOLHIDOS = """() => {
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
        print("GATE 52 NAO PODE RODAR: playwright ausente. "
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
                print(f"GATE 52 NAO PODE RODAR: chromium nao abre ({str(e)[:120]})",
                      file=sys.stderr)
                return None
            for rel in rels:
                ctx = nav.new_context(viewport={"width": 1440, "height": 900})
                pg = ctx.new_page()
                pg.on("dialog", lambda d: d.dismiss())
                pg.goto(f"http://127.0.0.1:{porta}/{rel}", wait_until="load")
                pg.wait_for_timeout(400)
                achados, telas = [], 0
                try:
                    aulas = pg.evaluate("() => Object.keys(LESSONS).map(Number)")
                except Exception as e:                                # noqa: BLE001
                    out[rel] = {"__sonda__": f"nao achei LESSONS: {str(e)[:100]}"}
                    ctx.close()
                    continue
                for n in aulas:
                    pg.evaluate(f"openLesson({n})")
                    pg.wait_for_timeout(220)
                    visto = None
                    for _ in range(80):
                        pg.evaluate(ABRE_RECOLHIDOS)
                        pg.wait_for_timeout(90)
                        achados += pg.evaluate(SONDA)
                        telas += 1
                        atual = pg.evaluate(
                            "() => {const s=document.querySelector('.slide.active');"
                            "return s ? s.getAttribute('data-slide') : null}")
                        if atual == visto:
                            break
                        visto = atual
                        pg.evaluate("go(1)")
                        pg.wait_for_timeout(140)
                        if pg.evaluate(
                                "() => {const s=document.querySelector('.slide.active');"
                                "return s ? s.getAttribute('data-slide') : null}") == atual:
                            break
                    pg.evaluate("closeLesson()")
                    pg.wait_for_timeout(120)
                out[rel] = {"achados": achados, "telas": telas, "aulas": len(aulas)}
                ctx.close()
            nav.close()
    finally:
        srv.shutdown()
    return out


def avalia(dados):
    if "__sonda__" in dados:
        return [f"a sonda nao rodou — {dados['__sonda__']}"]
    # o mesmo defeito aparece em varias telas: agrupa por classe para o relatorio dizer
    # ONDE consertar (uma regra de CSS) em vez de listar vinte sintomas
    porcls, erros = {}, []
    for a in dados["achados"]:
        porcls.setdefault((a["cls"], a["tag"], a["razao"]), []).append(a)
    for (cls, tag, razao), grupo in sorted(porcls.items(), key=lambda x: x[0][2]):
        um = grupo[0]
        onde = ", ".join(sorted({f"aula {g['aula']} tela {g['tela']}" for g in grupo})[:4])
        erros.append(
            f"REG-005 · <{tag} class=\"{cls}\"> mede {razao}:1 no escuro (minimo {um['lim']}) "
            f"— {um['cor']} sobre {um['fundo']}. {len(grupo)}x: {onde}. \"{um['txt']}\"")
    return erros


def alvos_padrao():
    """So o professor: o arquivo do aluno nao tem deck, entao nao tem tela escura."""
    fora = []
    for p in sorted(glob.glob(os.path.join(RAIZ, "public", "professor", "*.html"))):
        try:
            with open(p, encoding="utf-8") as f:
                if carimbo(f.read(4000)) == ANATOMIA:
                    fora.append(os.path.relpath(p, RAIZ))
        except OSError:
            pass
    return fora


def _selftest():
    base = os.path.join(RAIZ, "public", "professor", "stephanie-vicente.html")
    if not os.path.exists(base):
        print("SELFTEST INCONCLUSIVO — o molde nao esta no lugar.")
        return 1
    limpo = open(base, encoding="utf-8").read()
    # Cada caso injeta uma REGRA no fim do <style> do molde. Assim o defeito plantado passa
    # pela mesma cascata que o real -- um `style=` inline provaria menos.
    def css(regra):
        return lambda s: s.replace("</style>", regra + "</style>", 1)

    # As duas pecas do defeito de 02/09/2026 (`.task-instr` e `.verify-all-btn.ghost`) nao
    # existem em tela escura NESTE molde -- a Stephanie nao tem exercicio de escolha no
    # escuro. Entao o selftest as PLANTA na primeira tela escura, junto com a cor errada.
    # Sem isso os dois casos passariam por nao haver o que medir, que e o modo mais comum de
    # um selftest ficar verde sem provar nada.
    RX_ESCURA = re.compile(r'(<div class="slide slide-dark"[^>]*>\s*(?:<div class="[^"]*"'
                           r'[^>]*></div>\s*)?<div class="slide-inner">)')

    def planta(marcacao, regra):
        def muta(s):
            novo, n = RX_ESCURA.subn(r"\1" + marcacao, s, count=1)
            if n != 1:
                raise SystemExit("SELFTEST: nao achei a primeira tela escura do molde para "
                                 "plantar o caso. A forma da tela mudou -- releia antes de "
                                 "afrouxar a busca.")
            return novo.replace("</style>", regra + "</style>", 1)
        return muta

    casos = [
        ("o enunciado com a cor do tema claro",
         planta('<p class="task-instr">Which two answers give the essential information?</p>',
                ".slide-dark .task-instr,.slide-open .task-instr{color:#33405E}"),
         "task-instr"),
        ("o botao Check com o azul-marinho do tema claro",
         planta('<button class="verify-all-btn ghost">Check</button>',
                ".slide-dark .verify-all-btn.ghost,.slide-open .verify-all-btn.ghost"
                "{color:#003080}"),
         "verify-all-btn"),
        ("texto GRANDE com contraste de 2.8:1 — o limiar frouxo tambem morde",
         css(".slide-dark .slide-title,.slide-open .slide-title"
             "{color:#4a5f8a;font-size:40px}"),
         "slide-title"),
        ("a mesma peca com o cinza proprio do tema escuro — NAO pode reprovar",
         planta('<p class="task-instr">Which two answers give the essential information?</p>',
                ".slide-dark .task-instr,.slide-open .task-instr{color:#C6D4EA}"),
         None),
        # O caso que so existe desde 03/09/2026: o defeito dentro de um bloco RECOLHIDO.
        # Antes de `ABRE_RECOLHIDOS` a sonda pulava o `display:none` e devolvia verde — e
        # era assim que uma peca sem par escuro chegava projetada na aula sem nunca ter sido
        # medida. Se alguem tirar a abertura, este caso deixa de acusar e o selftest cai.
        ("o defeito dentro do bloco que so abre no clique",
         planta('<button class="verify-all-btn" onclick="abrirBloco(\'st52\',this)">Show</button>'
                '<div id="st52" style="display:none">'
                '<p class="task-instr">Which two answers give the essential information?</p>'
                '</div>',
                ".slide-dark .task-instr,.slide-open .task-instr{color:#33405E}"),
         "task-instr"),
    ]
    tmpdir = os.path.join(RAIZ, "public", "professor", "_gate52_tmp")
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
            errs = avalia(dados[rel])
            if esperado is None:
                bom = not errs
                motivo = "ignorado, como deve" if bom else f"REPROVOU: {errs[0][:46]}"
            else:
                bom = any(esperado in e for e in errs)
                motivo = (errs[0][:56] if errs else "nao acusou nada")
            print(f"  {'OK  ' if bom else 'FALHA'}  {nome:52} {motivo}")
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
    pegar = sum(1 for _, _, esperado in casos if esperado)
    print(f"SELFTEST OK — {len(casos)} casos: {pegar} ilegibilidades pegas "
          f"(uma delas dentro de bloco recolhido), {len(casos) - pegar} cinza legitimo poupado.")
    return 0


def main():
    if "--selftest" in sys.argv:
        return _selftest()
    alvos = [a for a in sys.argv[1:] if a.endswith(".html")] or alvos_padrao()
    if not alvos:
        print(f"GATE 52 — nenhum arquivo com o carimbo {ANATOMIA}.")
        return 0
    print(f"=== GATE 52 — contraste WCAG nas telas escuras do deck (chromium), "
          f"anatomia {ANATOMIA} ===")
    dados = mede(alvos)
    if dados is None:
        return 1
    total = 0
    for rel in alvos:
        errs = avalia(dados[rel])
        if errs:
            total += len(errs)
            print(f"{VERMELHO}FAIL{ZERA}  {rel}")
            for e in errs[:12]:
                print(f"        {e}")
        else:
            d = dados[rel]
            print(f"{VERDE}ok{ZERA}    {rel}  ({d['aulas']} aula(s), {d['telas']} tela(s))")
    print()
    if total:
        print(f"{VERMELHO}GATE 52 — {total} peca(s) ilegivel(is) no escuro.{ZERA}")
        return 1
    print(f"GATE 52 OK — {len(alvos)} arquivo(s): nada abaixo do minimo WCAG nas telas escuras.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
