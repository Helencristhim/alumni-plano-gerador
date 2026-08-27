#!/usr/bin/env python3
"""Emite public/data/anatomias.json — quem ja tem material do framework novo.

QUAL E A PERGUNTA
-----------------
A aba "Alunos Consultivo" mostra os alunos que **ja ganharam material do framework novo**.
Isso nao e uma marcacao que alguem liga: e um FATO do disco. O carimbo
`<meta name="alumni-anatomia" content="consultivo">` esta no `<head>` do arquivo, e so
existe porque o builder o escreveu.

Derivar em vez de marcar tem uma consequencia pratica que vale mais que a elegancia: o
aluno entra na aba **no instante em que o material dele existe**, e nao entra antes. Um
campo manual erra nos dois sentidos -- marcado sem material (o painel promete um link que
nao abre) e material gerado sem marcar (o aluno some da vista de quem vai dar a aula).

O QUE ELE NAO DECIDE
--------------------
Nada de pedagogia, e nada sobre quem DEVE migrar. Ele so le o que existe.

    python3 scripts/build_anatomias.py           # escreve
    python3 scripts/build_anatomias.py --check   # falha se o commitado divergir do disco
"""
import glob
import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAIDA = os.path.join(RAIZ, "public", "data", "anatomias.json")
MARCA = 'name="alumni-anatomia" content="consultivo"'
MOLDE = 'name="alumni-molde"'


def slug_de(caminho):
    return os.path.splitext(os.path.basename(caminho))[0]


def levanta():
    """{slug: {"professor": bool, "aluno": bool}} para quem tem carimbo consultivo.

    `{slug}-cN` E o aluno -- e a chave e o `{slug}`.

    Enquanto o aluno tem aula no material antigo, o link dele (`{slug}.html`) NAO se toca:
    o material do framework novo nasce ao lado, em `{slug}-c1.html`. Se o indice ignorasse
    esse sufixo, o aluno geraria o bloco novo e NAO apareceria na aba Alunos Consultivo --
    que e a unica coisa que a aba existe para dizer. Por isso o ciclo e ATRIBUIDO ao aluno,
    nao descartado.

    Continuam de fora, porque nao representam um aluno:
      `{slug}-aulaN`    -- standalone de aula; um aluno com 20 aulas viraria 20 linhas
      `{slug}-anterior` -- o hub congelado, se um dia o material novo tomar a URL canonica

    E o MOLDE, que e ficcao (ver abaixo)."""
    achado = {}
    for papel in ("professor", "aluno"):
        for p in sorted(glob.glob(os.path.join(RAIZ, "public", papel, "*.html"))):
            slug = slug_de(p)
            if re.search(r"-aula\d|-anterior$", slug):
                continue
            # `{slug}-c1` conta PARA `{slug}`: e o mesmo aluno, no ciclo dele.
            slug = re.sub(r"-c\d+$", "", slug)
            with open(p, encoding="utf-8", errors="ignore") as fh:
                cabeca = fh.read(6000)
            if MARCA not in cabeca:
                continue
            # O MOLDE nao e aluno. `stephanie-vicente` e ficcao -- sem contrato, fora de
            # `perfis` -- e ate 26/08/2026 este indice a contava: dizia "1 aluno no
            # consultivo" quando o numero certo era zero.
            if MOLDE in cabeca:
                continue
            achado.setdefault(slug, {"professor": False, "aluno": False})[papel] = True
    return achado


MARCADOR_REAL = "viewport"
MINIMO_REAL = 5000


def materiais():
    """Quem TEM material publicado, medido no disco em vez de por HTTP.

    O painel perguntava isso com uma requisicao por arquivo, por aluno, a CADA visita --
    252 requisicoes com `cache: 'no-store'`, que e por construcao nao-cacheavel. Medido em
    producao em 27/08/2026: primeiro cartao em 3,7s e rede so parada aos 15,8s.

    O criterio e o MESMO que o `isRealPage()` aplica, letra por letra: mais de 5000 bytes e
    a palavra `viewport` no primeiro KB (o marcador que separa material real dos stubs de
    redirect). Aqui ele custa uma leitura de disco no build em vez de uma ida a rede por
    aluno.

    O painel continua sabendo perguntar por HTTP: material que nao esteja neste indice --
    fora da convencao, ou publicado sem passar pelo build -- cai no caminho antigo. O
    indice ACELERA o caso comum; nao vira a unica verdade."""
    fora = {"professor": [], "aluno": []}
    for papel in ("professor", "aluno"):
        for p in sorted(glob.glob(os.path.join(RAIZ, "public", papel, "*.html"))):
            slug = slug_de(p)
            # So os HUBS. O painel pergunta por `{id}.html`, um por perfil -- nunca pelos
            # standalones por aula. Inclui-los inchava o indice de 5 KB para 172 KB com
            # 1.867 entradas que ninguem consulta, e um indice que ninguem le e so peso.
            if re.search(r"-aula\d", slug):
                continue
            try:
                if os.path.getsize(p) <= MINIMO_REAL:
                    continue
                with open(p, encoding="utf-8", errors="ignore") as fh:
                    if MARCADOR_REAL not in fh.read(1024).lower():
                        continue
            except OSError:
                continue
            fora[papel].append(slug)
    return fora


def monta():
    achado = levanta()
    return {
        "_leia": ("Quem ja tem material da anatomia CONSULTIVO (o framework novo). "
                  "GERADO por scripts/build_anatomias.py lendo o carimbo "
                  "<meta name=\"alumni-anatomia\"> do <head> de cada hub — nao editar a "
                  "mao. A chave e o slug do arquivo, que e o mesmo perfis.id de que o "
                  "painel deriva os links. `professor`/`aluno` dizem qual dos dois "
                  "arquivos existe: material com um so dos lados e material pela metade, "
                  "e o painel avisa em vez de oferecer um link que nao abre."),
        "consultivo": achado,
        "_materiais": ("Quem tem material publicado, pelo MESMO criterio do isRealPage() do "
                       "painel: mais de 5000 bytes e `viewport` no primeiro KB. Existe para o "
                       "painel nao precisar de uma requisicao por arquivo a cada visita. Nao e "
                       "a unica verdade: o que nao estiver aqui o painel continua perguntando "
                       "por HTTP."),
        "materiais": materiais(),
    }


def main():
    novo = monta()
    if "--check" in sys.argv:
        if not os.path.exists(SAIDA):
            print(f"FALHA — {os.path.relpath(SAIDA, RAIZ)} nao existe. Rode "
                  f"`python3 scripts/build_anatomias.py`.")
            return 1
        atual = json.load(open(SAIDA, encoding="utf-8"))
        if atual.get("materiais") != novo["materiais"]:
            print("FALHA — a lista de materiais do anatomias.json nao bate com o disco.\n")
            a, b = set(atual.get("materiais", {})), set(novo["materiais"])
            for s2 in sorted(b - a)[:10]:
                print(f"  falta: {s2}")
            for s2 in sorted(a - b)[:10]:
                print(f"  declarado e sem material no disco: {s2}")
            print("\n  python3 scripts/build_anatomias.py")
            return 1
        if atual.get("consultivo") != novo["consultivo"]:
            print("FALHA — o anatomias.json commitado nao bate com o disco.\n")
            a, b = set(atual.get("consultivo", {})), set(novo["consultivo"])
            for s in sorted(b - a):
                print(f"  falta declarar: {s}")
            for s in sorted(a - b):
                print(f"  declarado e sem carimbo no disco: {s}")
            for s in sorted(a & b):
                if atual["consultivo"][s] != novo["consultivo"][s]:
                    print(f"  mudou de lado: {s} "
                          f"{atual['consultivo'][s]} -> {novo['consultivo'][s]}")
            print("\n  python3 scripts/build_anatomias.py")
            return 1
        print(f"✓ anatomias.json em dia — {len(novo['consultivo'])} aluno(s) no "
              f"consultivo, {len(novo['materiais'])} com material publicado.")
        return 0
    os.makedirs(os.path.dirname(SAIDA), exist_ok=True)
    with open(SAIDA, "w", encoding="utf-8") as fh:
        json.dump(novo, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print(f"✓ {os.path.relpath(SAIDA, RAIZ)} — {len(novo['consultivo'])} no consultivo "
          f"({', '.join(sorted(novo['consultivo'])) or 'nenhum'}); "
          f"{len(novo['materiais'])} com material publicado")
    return 0


if __name__ == "__main__":
    sys.exit(main())
