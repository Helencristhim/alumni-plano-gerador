#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 55 — o portugues que chega ao aluno chega como portugues.

DE ONDE ISTO VEIO (revisao da professora, 03/09/2026)
-----------------------------------------------------
A caixa que confirma o "Reset my answers" da Vanessa saiu assim na tela dela:

    Reset Lesson 01 answers? &middot; Limpar as respostas da aula 01?
    Isto apaga as suas respostas do pre-class da aula 01, e so dela.
    Nada do que a professora escreveu e afetado, e as outras aulas ficam como estao.
    [ Cancel ]  [ Clear my answers &middot; Limpar ]

Dois defeitos diferentes na mesma caixa, e os dois so aparecem NA TELA.

1. `&middot;` NAO E UM CARACTERE. E uma entidade HTML, e ela so vira "·" quando alguem
   INTERPRETA o HTML. O titulo e o rotulo do botao sao escritos com `textContent`
   (`askOpen`: `askTitle.textContent=titulo`, `ok.textContent=rotulo`), e `textContent` nao
   interpreta nada -- entra caractere por caractere. O corpo da mesma caixa vai por
   `innerHTML` e ali a entidade aparecia certa: metade da caixa certa, metade com o codigo
   cru. E nada acusa: o HTML e valido, o console fica limpo, e o texto so existe depois do
   clique. E o mesmo erro de categoria da REGRA 7.1 do imersivo -- tratar o texto ESCRITO
   como se fosse o texto EXECUTADO.

2. O PORTUGUES SAIU SEM ACENTO. "e so dela", "e afetado", "ficam como estao". Os scripts
   deste repo sao escritos sem acento de proposito (sao codigo), e o texto nasceu dentro de
   um deles -- levou junto uma convencao que valia para o codigo e nao vale para a frase.
   A aluna que le essa caixa e a razao de o material ser bilingue: ela e A0 real. Portugues
   sem acento e a lingua dela escrita errado, na tela dela, exatamente no lugar em que ela
   precisa entender antes de apertar um botao que apaga o trabalho dela.

POR QUE NO NAVEGADOR, E NAO NO ARQUIVO
--------------------------------------
Os dois defeitos vivem no texto RENDERIZADO. No arquivo, `&middot;` dentro de uma string JS
e indistinguivel do `&middot;` dentro de um `<span>` -- o primeiro e defeito, o segundo e
correto, e so o navegador sabe qual e qual. Entao o gate abre a pagina, ABRE A CAIXA (que e
uma superficie que so existe depois de um clique) e le o que esta escrito.

O QUE ELE MEDE, no arquivo do ALUNO
-----------------------------------
  A. nenhum texto visivel contem uma entidade HTML crua (`&alguma;` / `&#123;`) -- em
     qualquer lugar da pagina, e dentro da caixa de confirmacao depois de aberta;
  B. nenhuma palavra da lista fechada aparece sem acento no apoio em portugues.

A LISTA DE (B) E FECHADA E CONSERVADORA, e isso e proposital. Ela so tem palavras que
(i) em portugues SEMPRE levam acento e (ii) nao sao tambem uma palavra inglesa -- por isso
"so", "e" e "ate" ficam de fora, apesar de serem os erros mais comuns: "so" e "ate" existem
em ingles e o material e bilingue por definicao. Um gate que gera um falso positivo por
material vira ruido e passa a ser ignorado; este prefere deixar passar um acento a acusar
uma palavra inglesa. A lista CRESCE quando um caso real aparecer.

ESCOPO: o carimbo `alumni-anatomia=consultivo`, e os dois nao tem o mesmo alcance de
proposito. (A) vale para TODO material da anatomia: entidade crua na tela nao tem nada a ver
com bilinguismo, e o mesmo defeito ja estava em cinco exercicios da aula 3 ("I am in Lisbon.
&rarr; negative") por outro caminho -- o autor escreveu a entidade num campo que o emissor
ESCAPA, e o `&` virou `&amp;`. (B) so vale onde o config declara `apoio.bilingue`: material
que nao promete portugues nao tem portugues a cobrar. Gate novo nasce escopado.

DEPENDENCIA: playwright + chromium. Ausentes, o gate DIZ que nao pode rodar e falha.

USO:
    python3 scripts/consultivo/check_pt_na_tela.py [arquivo.html ...]
    python3 scripts/consultivo/check_pt_na_tela.py --selftest
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

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ANATOMIA = "consultivo"
VERDE, VERMELHO, ZERA = "\033[32m", "\033[31m", "\033[0m"

# (A) entidade HTML que sobreviveu ao navegador. Se o texto renderizado ainda tem isto,
# ninguem interpretou o HTML: o caractere certo nunca chegou na tela.
RX_ENTIDADE = re.compile(r"&(?:[a-zA-Z][a-zA-Z0-9]{1,10}|#[0-9]{1,5}|#x[0-9a-fA-F]{1,5});")

# (B) A lista fechada. Cada palavra: sempre acentuada em portugues, e nao e palavra inglesa.
SEM_ACENTO = {
    "nao": "não", "sao": "são", "entao": "então", "estao": "estão", "serao": "serão",
    "voce": "você", "voces": "vocês", "ingles": "inglês", "portugues": "português",
    "tambem": "também", "ja": "já", "apos": "após", "atras": "atrás", "tres": "três",
    "alem": "além", "amanha": "amanhã", "atencao": "atenção", "informacao": "informação",
    "informacoes": "informações", "opcao": "opção", "opcoes": "opções", "licao": "lição",
    "questao": "questão", "razao": "razão", "proximo": "próximo", "proxima": "próxima",
    "numero": "número", "musica": "música", "facil": "fácil", "dificil": "difícil",
    "ultima": "última", "ultimo": "último",
}

SONDA = r"""() => {
  /* O texto RENDERIZADO, no e-folha: pegar o textContent da raiz devolveria tambem o que
     esta dentro de <script>, que e codigo e nao e tela. */
  const visivel = (e) => {
    const cs = getComputedStyle(e);
    return cs.display !== 'none' && cs.visibility !== 'hidden';
  };
  const folhas = [];
  const it = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  for (let n = it.nextNode(); n; n = it.nextNode()) {
    const p = n.parentElement;
    if (!p) continue;
    const tag = p.tagName;
    if (tag === 'SCRIPT' || tag === 'STYLE' || tag === 'TEXTAREA') continue;
    const t = (n.nodeValue || '').trim();
    if (!t) continue;
    /* `data-teacher` e prosa do professor e nao e tela do aluno; ele nem existe no arquivo
       do aluno. Aqui a poda e por elemento invisivel, que cobre painel fechado. */
    if (!visivel(p)) continue;
    folhas.push({txt: t, cls: (p.className || '').toString().slice(0, 40),
                 lang: p.closest('[lang]') ? p.closest('[lang]').getAttribute('lang') : ''});
  }
  return folhas;
}"""

# As superficies que so existem depois de um clique. Cada uma: o que rodar e o que ela abre.
ABERTURAS = [
    ("a caixa de confirmacao do Reset my answers",
     "() => { _preAtual = (typeof CICLO !== 'undefined' ? CICLO.primeira : 1); preResetAsk(); }"),
]


def carimbo(c):
    m = re.search(r'<meta\s+name="alumni-anatomia"\s+content="([^"]+)"', c[:4000])
    return m.group(1) if m else None


def bilingues():
    """Os slugs cujo config declara o modo. A promessa esta no config, nao no HTML."""
    fora = {}
    for cfg in glob.glob(os.path.join(RAIZ, "_build", "consultivo", "*", "config.json")):
        d = json.load(open(cfg, encoding="utf-8"))
        if (d.get("apoio") or {}).get("bilingue"):
            fora[d["slug"]] = d
    return fora


def _servidor():
    h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=RAIZ)

    class Q(socketserver.TCPServer):
        allow_reuse_address = True

        def handle_error(self, *a):
            pass          # 404 de MP3 nao materializado nao e assunto deste gate

    srv = Q(("127.0.0.1", 0), h)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, srv.server_address[1]


def e_apoio(folha):
    """A folha de texto e apoio em portugues? Ou esta marcada, ou usa a classe do apoio."""
    if (folha.get("lang") or "").lower().startswith("pt"):
        return True
    cls = folha.get("cls") or ""
    return any(c in cls.split() for c in ("slide-pt", "item-pt", "sp-pt"))


def avalia(folhas, rotulo_da_tela, bilingue=True):
    fora = []
    for f in folhas:
        for ent in RX_ENTIDADE.findall(f["txt"]):
            fora.append(f'{rotulo_da_tela}: a entidade {ent} chegou CRUA na tela, em '
                        f'"{f["txt"][:70]}". Quem escreve por `textContent` nao interpreta '
                        f'HTML — ponha o caractere, nao a entidade.')
        if not bilingue or not e_apoio(f):
            continue
        for p in re.findall(r"[A-Za-zÀ-ÿ]+", f["txt"]):
            certo = SEM_ACENTO.get(p.lower())
            if certo:
                fora.append(f'{rotulo_da_tela}: "{p}" sem acento no apoio em portugues '
                            f'(é "{certo}"), em "{f["txt"][:70]}".')
    return fora


def mede(rels):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("GATE 55 NAO PODE RODAR: playwright ausente. "
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
                print(f"GATE 55 NAO PODE RODAR: chromium nao abre ({str(e)[:120]})",
                      file=sys.stderr)
                return None
            for rel, bi in rels:
                ctx = nav.new_context(viewport={"width": 1440, "height": 900})
                pg = ctx.new_page()
                pg.on("dialog", lambda d: d.dismiss())
                pg.goto(f"http://127.0.0.1:{porta}/{rel}", wait_until="load")
                pg.wait_for_timeout(450)
                achados = []
                try:
                    achados += avalia(pg.evaluate(SONDA), "a pagina", bi)
                    for nome, roda in ABERTURAS:
                        try:
                            pg.evaluate(roda)
                        except Exception as e:                        # noqa: BLE001
                            achados.append(f"{nome}: nao abriu — {str(e)[:90]}")
                            continue
                        pg.wait_for_timeout(150)
                        achados += avalia(pg.evaluate(SONDA), nome, bi)
                except Exception as e:                                # noqa: BLE001
                    achados.append(f"a sonda nao rodou — {str(e)[:140]}")
                out[rel] = achados
                ctx.close()
            nav.close()
    finally:
        srv.shutdown()
    return out


def alvos_padrao(decl):
    fora = []
    for p in sorted(glob.glob(os.path.join(RAIZ, "public", "aluno", "*.html"))):
        slug = re.sub(r"-c(?:iclo)?\d+$", "", os.path.basename(p)[:-5])
        try:
            with open(p, encoding="utf-8") as f:
                if carimbo(f.read(4000)) == ANATOMIA:
                    fora.append((os.path.relpath(p, RAIZ), slug in decl))
        except OSError:
            pass
    return fora


def main(argv):
    decl = bilingues()
    print(f"=== GATE 55 — o portugues chega como portugues (anatomia {ANATOMIA}) ===")
    pedidos = [a for a in argv if not a.startswith("--")]
    if pedidos:
        alvos = [(os.path.relpath(a, RAIZ),
                  re.sub(r"-c(?:iclo)?\d+$", "", os.path.basename(a)[:-5]) in decl)
                 for a in pedidos]
    else:
        alvos = alvos_padrao(decl)
    if not alvos:
        print(f"{VERDE}GATE 55 OK{ZERA} — nenhum arquivo da anatomia {ANATOMIA}.")
        return 0
    res = mede(alvos)
    if res is None:
        return 1
    total = 0
    for rel, erros in res.items():
        if erros:
            total += len(erros)
            for e in erros:
                print(f"  {VERMELHO}FAIL{ZERA}   {rel}: {e}")
        else:
            print(f"  {VERDE}ok{ZERA}     {rel}")
    if total:
        print(f"\n{VERMELHO}GATE 55 — {total} problema(s) em {len(res)} arquivo(s).{ZERA}")
        return 1
    print(f"\n{VERDE}GATE 55 OK{ZERA} — {len(res)} arquivo(s) com o portugues inteiro na tela.")
    return 0


def selftest():
    falhas = []
    # (A) entidade crua
    if not avalia([{"txt": "Reset Lesson 01 &middot; Limpar", "cls": "", "lang": ""}], "x"):
        falhas.append("nao viu a entidade crua no texto renderizado")
    if avalia([{"txt": "Reset Lesson 01 · Limpar", "cls": "", "lang": ""}], "x"):
        falhas.append("acusou o caractere certo como se fosse entidade")
    if avalia([{"txt": "Marina & Co. 5 < 7", "cls": "", "lang": ""}], "x"):
        falhas.append("acusou um & solto, que nao e entidade")
    # (B) acento, e SO no apoio em portugues
    if not avalia([{"txt": "as outras aulas ficam como estao", "cls": "", "lang": "pt-BR"}], "x"):
        falhas.append("nao viu 'estao' sem acento no apoio marcado por lang")
    if not avalia([{"txt": "o tempo hoje, voce escolhe", "cls": "slide-pt", "lang": ""}], "x"):
        falhas.append("nao viu 'voce' sem acento no .slide-pt")
    if avalia([{"txt": "as outras aulas ficam como estao", "cls": "", "lang": "en"}], "x"):
        falhas.append("cobrou acento fora do apoio em portugues")
    if avalia([{"txt": "estão", "cls": "", "lang": "pt-BR"}], "x"):
        falhas.append("acusou a palavra ja acentuada")
    # a lista NAO tem as palavras que colidem com o ingles
    for p in ("so", "ate", "e"):
        if p in SEM_ACENTO:
            falhas.append(f"{p!r} entrou na lista e tambem e palavra inglesa")
    if falhas:
        print(VERMELHO + "selftest FALHOU" + ZERA)
        for f in falhas:
            print("  -", f)
        return 1
    print(f"{VERDE}selftest OK{ZERA} — ve a entidade crua, poupa o '&' solto, cobra acento "
          f"so no apoio em portugues e nao usa palavra que colide com o ingles.")
    return 0


if __name__ == "__main__":
    sys.exit(selftest() if "--selftest" in sys.argv else main(sys.argv[1:]))
