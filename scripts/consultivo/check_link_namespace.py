#!/usr/bin/env python3
"""GATE 48 -- link e porta: o arquivo do aluno nao aponta para o do professor.

DE ONDE VEM
-----------
Da fase de transicao. Enquanto o molde novo convive com o antigo, o aluno vai ter DOIS
materiais, e a ligacao entre eles e um botao. Botao e `href`, e `href` e porta.

O GATE 36 (isolamento) mede duas coisas: os BYTES do arquivo do aluno e a tentativa de
virar professor no navegador. Nenhuma das duas ve para ONDE a pagina aponta. Um arquivo de
aluno impecavel -- sem `data-teacher`, sem deck, sem `data-view="professor"` -- pode ter um
link para `/professor/{slug}.html` e entregar tudo aquilo em um clique, com os dois gates
verdes.

Nao e hipotese: o padrao ja existe no repositorio, em material antigo, escrito assim de
proposito ("o conteudo completo esta no arquivo principal" + link para /professor/). E
legado e fica onde esta (REGRA 30) -- mas o molde novo nao vai nascer com ele.

O QUE MEDE
----------
Arquivo servido em `/aluno/` nao contem `href` para `/professor/`. So isso, e pela FORMA:
um comentario que CITE o caminho nao abre porta nenhuma.

ESCOPO: o carimbo `alumni-anatomia=consultivo`. Nao varre o imersivo -- a divida de la esta
congelada no legacy-baseline por decisao do Dan, e um gate novo de repo inteiro so faria o
GATE 8 acusar arquivo que ninguem vai consertar.
"""
import glob
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MARCA = 'name="alumni-anatomia" content="consultivo"'


def main():
    alvos = [p for p in glob.glob(os.path.join(RAIZ, "public", "aluno", "*.html"))
             if MARCA in open(p, encoding="utf-8", errors="ignore").read(6000)]
    if not alvos:
        print("✓ GATE 48 — nenhum material de aluno na anatomia consultivo ainda.")
        return 0
    faltas = []
    for p in sorted(alvos):
        s = re.sub(r"<!--.*?-->", " ", open(p, encoding="utf-8").read(), flags=re.S)
        for m in re.finditer(r'href\s*=\s*"([^"]*/professor/[^"]*)"', s):
            faltas.append(f"  {os.path.relpath(p, RAIZ)}\n    aponta para {m.group(1)}")
    if faltas:
        print("GATE 48 — o arquivo do aluno tem porta para o do professor.\n")
        print("\n\n".join(faltas))
        print("\nO arquivo pode estar limpo e o clique entregar o deck, as notas de "
              "conducao e os gabaritos. Aponte para /aluno/ — a versao dele existe.")
        return 1
    print(f"✓ GATE 48 — {len(alvos)} arquivo(s) de aluno: nenhuma porta para /professor/.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
