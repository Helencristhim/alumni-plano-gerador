#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 44 — itens que o catalogo marcou "Semantico" e que TEM forma observavel.

POR QUE ESTE ARQUIVO EXISTE
---------------------------
Porque eu errei. Depois de encontrar o INT-002 -- que o catalogo classificava como
"Script + semantico" e so apareceu quando a pergunta foi reformulada --, eu escrevi que a
coluna "Deteccao recomendada" era sugestao e nao limite... e mesmo assim usei "Semantico"
como sacola para os 31 itens que nao examinei. Extrapolei da amostra, que e exatamente o
erro que o metodo inteiro existe para evitar.

Lendo os 31 um a um, pela coluna MANIFESTACAO (que descreve o que aparece no arquivo) em
vez do rotulo, pelo menos catorze tem forma. Estes quatro eu consegui enunciar sem
ambiguidade E medir no molde antes de escrever:

  INT-005/006  nivel por habilidade, cada uma com base propria
  PRO-001      atividade de descoberta com itens comparaveis e checagem
  PRO-016      producao aberta nao carrega gabarito rigido
  PRO-005      audio de narracao/dialogo nao e a leitura do que ja esta na tela

O ANCORA E O `data-ok`, E LEVOU TRES TENTATIVAS ERRADAS PARA APARECER
----------------------------------------------------------------------
O PRO-001 pede "ao menos dois contrastes, decisao, justificativa". Procurei isso por
`reveal-card`: achei 4 de 8. Por `sortcol`/`gdCol`: achei 1. Por `.opt`/`ppPick`: achei
ZERO -- e havia oito atividades legitimas na minha frente.

O problema era sempre o mesmo: eu contava o WIDGET, e a mesma operacao pedagogica aparece
em widgets diferentes conforme o conteudo. O que nao muda e o GABARITO: toda atividade
fechada carrega `data-ok` no item. Ancorado nele, a contagem passou a bater com o que se ve
na tela -- 8 atividades, 8 com checagem.

    Classe e implementacao. `data-ok` e contrato.

O QUE CONTINUA DE FORA, E AGORA COM NOME
------------------------------------------
Nao por serem "semanticos", mas porque a manifestacao depende de comparar o material com
algo que o repositorio NAO TEM:

  INT-004, INT-007, INT-008, INT-009  exigem a FONTE (a consultoria, o que a aluna disse)
                                      para saber se o campo foi observado ou inferido
  INT-011, PRO-012, PRO-013, PRO-014  exigem julgar se a operacao mudou de fato
  INT-016                             exige detectar conflito entre normas
  PRO-003, PRO-004                    exigem classificar a funcao real da atividade
  SEQ-003, SEQ-007                    exigem saber o que ja foi trabalhado e quando

Para esses o catalogo ja traz o criterio de teste, e ele e para uma pessoa ler.

ESCOPO: o carimbo `alumni-anatomia=consultivo`.

USO:
    python3 scripts/consultivo/check_pedagogico.py [arquivo.html ...]
    python3 scripts/consultivo/check_pedagogico.py --selftest
"""
import glob
import json
import os
import re
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ANATOMIA = "consultivo"
VERDE, VERMELHO, ZERA = "\033[32m", "\033[31m", "\033[0m"

HABILIDADES = ["Reading", "Listening", "Speaking", "Interaction", "Writing"]
# audio cuja funcao E ser lido junto com o texto na tela -- ver r_audio_duplicativo
CATEGORIAS_MODELO = {"frase-modelo/pronúncia", "palavra ou expressão isolada"}


def carimbo(c):
    m = re.search(r'<meta\s+name="alumni-anatomia"\s+content="([^"]+)"', c[:4000])
    return m.group(1) if m else None


def eh_professor(c):
    return 'id="tab-inclass"' in c


def sem_codigo(c):
    c = re.sub(r"<!--.*?-->", " ", c, flags=re.S)
    return re.sub(r"<script\b.*?</script>|<style\b.*?</style>", " ", c, flags=re.S | re.I)


def telas(c):
    """Cada `.slide` isolada, com a aula e a etapa dela.

    Fatiar de slide a slide importa: a primeira versao desta medicao pegava do primeiro ao
    ultimo slide da aula e somava tudo junto, o que deu 0 reveal onde havia 4."""
    L = sem_codigo(c)
    pos = [m.start() for m in re.finditer(r'<div class="slide[^"]*"[^>]*data-slide=', L)]
    pos.append(len(L))
    fora = []
    for i in range(len(pos) - 1):
        s = L[pos[i]:pos[i + 1]]
        al = re.search(r'data-lesson="(\d+)"', s)
        st = re.search(r'data-stage="(\d+)"', s)
        fora.append({"html": s, "aula": al.group(1) if al else "?",
                     "etapa": st.group(1) if st else "?"})
    return fora


# ---------------------------------------------------------------------------
def r_nivel_por_habilidade(c, ctx):
    """INT-005 · INT-006 — nivel sem base, e generalizacao entre habilidades.

    O catalogo pede evidencia SEPARADA para Reading, Listening, Speaking, Interaction e
    Writing, e que cada nivel aponte a base. No molde isso e uma tabela de tres colunas:
    habilidade, faixa, e o que sustenta a estimativa. A terceira coluna E a base."""
    if not ctx["professor"]:
        return []
    m = re.search(r"Habilidade.{0,90}?Faixa.{0,140}?</tr>(.*?)</table>", ctx["tela"], re.S)
    if not m:
        return ["INT-005: nao ha tabela de nivel POR HABILIDADE no perfil. Nivel geral "
                "sozinho e generalizacao entre habilidades (INT-006)."]
    erros, vistas = [], []
    for tr in re.findall(r"<tr>(.*?)</tr>", m.group(1), re.S):
        tds = [" ".join(re.sub(r"<[^>]+>", " ", t).split())
               for t in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", tr, re.S)]
        if len(tds) < 3:
            continue
        vistas.append(tds[0])
        if len(tds[2].strip()) < 15:
            erros.append(f"INT-005: {tds[0]!r} declara {tds[1]!r} sem base — a coluna que "
                         f"sustenta a estimativa esta vazia ou generica.")
    faltam = [h for h in HABILIDADES if h not in vistas]
    if faltam:
        erros.append(f"INT-006: {faltam} sem linha propria. Evidencia de uma habilidade nao "
                     f"conclui nivel nas demais.")
    return erros


def r_descoberta(c, ctx):
    """PRO-001 — Guided Discovery nominal.

    Atividade FECHADA e a que carrega gabarito no item (`data-ok`). O criterio do catalogo
    -- "ao menos dois contrastes, decisao" -- vira: dois ou mais itens comparaveis, e um
    controle que confere.

    A "explicacao posterior" e a "justificativa" do criterio ficam de fora: exigem julgar se
    o texto que vem depois de fato explica. Ficam para quem le."""
    erros = []
    for t in ctx["telas"]:
        itens = len(re.findall(r'data-ok="', t["html"]))
        if itens < 2:
            continue
        check = len(re.findall(r'verify-all-btn|onclick="[a-zA-Z]*[Cc]heck\(', t["html"]))
        if not check:
            erros.append(f"PRO-001: aula {t['aula']}, etapa {t['etapa']} — {itens} itens com "
                         f"gabarito e NENHUM controle de checagem. Sem conferir, a decisao "
                         f"da aluna nao vira evidencia de nada.")
    return erros


def r_gabarito_desproporcional(c, ctx):
    """PRO-016 — Answer Key desproporcional.

    "Tarefa aberta recebe gabarito" e o lado que da para medir: producao livre (`textarea`)
    na MESMA tela que um gabarito rigido (`data-ok`) transforma resposta em acerto/erro.
    O outro lado (tarefa fechada sem mapeamento) e o PRO-001 acima."""
    erros = []
    for t in ctx["telas"]:
        if "<textarea" in t["html"] and 'data-ok="' in t["html"]:
            erros.append(f"PRO-016: aula {t['aula']}, etapa {t['etapa']} — producao aberta "
                         f"(textarea) na mesma tela que gabarito rigido (data-ok). Tarefa "
                         f"aberta nao tem resposta unica.")
    return erros


def r_audio_duplicativo(c, ctx):
    """PRO-005 — audio duplicativo.

    "Audio apenas le o que ja esta visivel, sem funcao propria."

    A CATEGORIA decide, e sem ela a regra e inutil: medi sem escopo e 15 das 20 falas do
    molde "duplicavam" -- porque frase-modelo de PRONUNCIA existe justamente para ser vista
    e ouvida ao mesmo tempo (o Anexo P-A §3 pede "ritmo imitavel"). A regra vale para
    narracao e dialogo, onde a funcao e decodificar pelo ouvido."""
    manifesto = ctx.get("manifesto")
    if not manifesto or not ctx["mapa"]:
        return []
    cat = {x.get("chave"): x.get("category") for x in manifesto}
    texto = " ".join(re.sub(r"<[^>]+>", " ",
                            re.sub(r'\sdata-teacher="[^"]*"', " ", ctx["tela"])).split())
    erros = []
    for chave in ctx["mapa"]:
        if chave.startswith("#") or cat.get(chave) in CATEGORIAS_MODELO:
            continue
        if len(chave) > 40 and chave[:60] in texto:
            erros.append(f"PRO-005: o audio de {cat.get(chave)!r} apenas le o que ja esta "
                         f"escrito na tela — \"{chave[:60]}...\". Sem funcao propria, ele "
                         f"nao e escuta: e legenda falada.")
    return erros


REGRAS = [r_nivel_por_habilidade, r_descoberta, r_gabarito_desproporcional,
          r_audio_duplicativo]


def confere(caminho):
    c = open(caminho, encoding="utf-8").read()
    if carimbo(c) != ANATOMIA:
        return False, []
    mapa = {}
    m = re.search(r"var AUD_MAP=(\{.*?\});", c, re.S)
    if m:
        try:
            mapa = json.loads(m.group(1))
        except ValueError:
            mapa = {}
    # O MANIFESTO E O DO ALUNO DESTE ARQUIVO, e isto nao e detalhe.
    #
    # Antes: `glob(_build/consultivo/*/audio_manifest.json)` e `break` no primeiro. O
    # primeiro e o que a ordem do diretorio devolver -- outro aluno, na maioria das vezes. A
    # regra PRO-005 pergunta "qual e a CATEGORIA deste audio?" e ia procurar a chave num
    # manifesto de outra pessoa: nao acha, `cat.get()` devolve None, None nao esta nas
    # categorias de modelo, e toda fala longa que aparece na tela vira "legenda falada".
    #
    # Ele reprovava ou passava conforme a ORDEM DO SISTEMA DE ARQUIVOS: verde no runner do
    # CI, vermelho na maquina onde o diretorio do outro aluno vem antes. Falso positivo que
    # muda de lado sozinho e pior do que gate ausente -- ninguem sabe de que lado olhar.
    manifesto = None
    slug = re.sub(r"-(?:c|ciclo)\d+$", "", os.path.basename(caminho)[:-len(".html")])
    p = os.path.join(RAIZ, "_build", "consultivo", slug, "audio_manifest.json")
    if os.path.exists(p):
        try:
            manifesto = json.load(open(p, encoding="utf-8"))
        except (OSError, ValueError):
            manifesto = None
    ctx = {"tela": sem_codigo(c), "telas": telas(c), "professor": eh_professor(c),
           "mapa": mapa, "manifesto": manifesto}
    erros = []
    for r in REGRAS:
        erros.extend(r(c, ctx))
    return True, erros


def alvos_padrao():
    fora = []
    for p in sorted(glob.glob(os.path.join(RAIZ, "public", "professor", "*.html")) +
                    glob.glob(os.path.join(RAIZ, "public", "aluno", "*.html"))):
        try:
            with open(p, encoding="utf-8") as f:
                if carimbo(f.read(4000)) == ANATOMIA:
                    fora.append(p)
        except OSError:
            pass
    return fora


def _confere_texto(t):
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(t)
        p = f.name
    try:
        return confere(p)
    finally:
        os.unlink(p)


def _selftest():
    prof = os.path.join(RAIZ, "public", "professor", "stephanie-vicente.html")
    if not os.path.exists(prof):
        print("SELFTEST INCONCLUSIVO — o molde nao esta no lugar.")
        return 1
    limpo = open(prof, encoding="utf-8").read()
    _, e = _confere_texto(limpo)
    if e:
        print("SELFTEST INCONCLUSIVO — o molde JA esta reprovando:")
        for x in e:
            print("   ", x)
        return 1

    casos = [
        ("INT-005 habilidade sem base",
         lambda s: re.sub(r"(<tr>\s*<td[^>]*>Writing</td>\s*<td[^>]*>[^<]*</td>\s*<td[^>]*>)"
                          r"[^<]*", r"\1—", s, count=1), "INT-005"),
        ("INT-006 habilidade sem linha propria",
         lambda s: s.replace(">Interaction<", ">Reading<", 1), "INT-006"),
        # Matar SO a classe nao basta: o mesmo botao tambem casa por `onclick="...Check("`.
        # A regra tem duas portas de proposito -- o molde usa as duas -- e a mutacao tem de
        # fechar as duas para provar que a regra morde.
        ("PRO-001 atividade fechada sem checagem",
         lambda s: s.replace('class="verify-all-btn', 'class="xx-all-btn')
                    .replace("Check(this", "Xheck(this"), "PRO-001"),
        # O textarea tem de estar DENTRO de um slide: a regra le tela a tela, e o primeiro
        # <textarea> do documento fica no registro pos-aula, fora do deck.
        ("PRO-016 producao aberta com gabarito rigido",
         lambda s: s.replace('<textarea id="l1fb1"', '<span data-ok="Z"></span><textarea id="l1fb1"', 1),
         "PRO-016"),
    ]
    falhou = False
    for nome, muta, esperado in casos:
        _, errs = _confere_texto(muta(limpo))
        bom = any(esperado in x for x in errs)
        print(f"  {'OK  ' if bom else 'FALHA'}  {nome:44} "
              f"{(errs[0][:54] if errs else 'nao acusou nada')}")
        if not bom:
            falhou = True
    print()
    if falhou:
        print("SELFTEST FALHOU — alguma regra parou de morder.")
        return 1
    print(f"SELFTEST OK — {len(casos)} defeitos, todos pegos.")
    return 0


def main():
    if "--selftest" in sys.argv:
        return _selftest()
    alvos = [a for a in sys.argv[1:] if a.endswith(".html")] or alvos_padrao()
    print(f"=== GATE 44 — pedagogico observavel (anatomia {ANATOMIA}) ===")
    total = vistos = 0
    for a in alvos:
        if not os.path.exists(a):
            continue
        aplicou, erros = confere(a)
        if not aplicou:
            continue
        vistos += 1
        rel = os.path.relpath(a, RAIZ)
        if erros:
            total += len(erros)
            print(f"{VERMELHO}FAIL{ZERA}  {rel}")
            for e in erros:
                print(f"        {e}")
        else:
            print(f"{VERDE}ok{ZERA}    {rel}  ({len(REGRAS)} regras)")
    print()
    if total:
        print(f"{VERMELHO}GATE 44 — {total} problema(s) em {vistos} arquivo(s).{ZERA}")
        return 1
    print(f"GATE 44 OK — {vistos} arquivo(s), {len(REGRAS)} regras.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
