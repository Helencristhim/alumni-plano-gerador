#!/usr/bin/env python3
"""GATE 46 -- o audio tem as falas que a tela promete (REG-001 no listening).

O defeito, achado no molde em 26/08/2026 e invisivel para todos os gates ate aqui:

  aula 2, seccao 4 -- titulo "Two lines, once", instrucao "Two lines from the beginning of
  the call", e o audio e UMA fala, de voz unica. A propria seccao ja falava no singular: a
  pergunta e "What is THE SPEAKER doing?" e o gabarito e "SHE names the item... it is the
  WHOLE of what she does". So o titulo e a instrucao diziam duas.

  aula 2, seccao 5 -- titulo "The same line, listening for something else", instrucao "Now
  a line from LATER in the call", e o audio e OUTRO. O titulo promete reouvir o mesmo com
  outra tarefa; nao e o que acontece.

POR QUE ESTE GATE E ESTREITO, e nao a leitura geral de "numero declarado vs itens reais"
que o REG-001 descreve: eu escrevi a versao ampla primeiro e MEDI. Deu 11 achados no
molde, e os 11 eram falso positivo -- porque numero em prosa quase nunca conta os itens da
propria seccao:

  "You will meet all six in the TWO documents"      -> os documentos sao de outra seccao
  "TWO teacher trainers talking about..."            -> sao os locutores de um podcast externo
  "TWO sentences, one moment"                        -> sao as duas frases de CADA par, e ha tres pares
  "about the TWO kinds of document you worked with"  -> os dois tipos, ao longo da aula inteira

Um gate com 100% de falso positivo nao e um gate rigoroso: e ruido que ensina a ignorar o
CI. O que sobra depois de medir e a forma em que o numero SO pode se referir ao que esta
ali: a seccao tem player proprio (`data-audgrupo`) e a frase conta FALAS.

O que este gate NAO faz: julgar se a instrucao descreve bem a tarefa. Isso e leitura
humana -- e continua sendo, de proposito.

Escopo: material da anatomia consultivo.
"""
import glob
import html as H
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NUM = {"two": 2, "three": 3, "four": 4, "five": 5, "six": 6}
# `one` nao entra: das tres ocorrencias do molde, TRES eram pronome ("the one who",
# "the one that"). Contar pronome acusa a lingua, nao o material.
UNIDADE = r"(?:lines?|sentences?|speakers?|voices|turns?|utterances?|exchanges?)"


def texto(t):
    return H.unescape(re.sub(r"<[^>]+>", "", t)).strip()


def main():
    alvos = [p for p in glob.glob(os.path.join(RAIZ, "public", "*", "*.html"))
             if 'name="alumni-anatomia" content="consultivo"' in
             open(p, encoding="utf-8", errors="ignore").read(4000)]
    if not alvos:
        raise SystemExit("GATE 46 — nenhum material do consultivo. O gate nao tem o que "
                         "medir, e isso e falha, nao um 'pulei porque nao achei'.")
    faltas = []
    for p in sorted(alvos):
        rel = os.path.relpath(p, RAIZ)
        s = re.sub(r"<style.*?</style>|<script.*?</script>|<!--.*?-->", "",
                   open(p, encoding="utf-8").read(), flags=re.S)
        cortes = list(re.finditer(r'<div class="section-header-row"><h4>(.*?)</h4>', s, re.S))
        vistas = []
        for i, m in enumerate(cortes):
            tit = texto(m.group(1))
            tr = s[m.end():cortes[i + 1].start() if i + 1 < len(cortes) else len(s)]
            if "data-audgrupo" not in tr:
                continue                      # sem player proprio nao ha o que contar aqui
            falas = list(dict.fromkeys(re.findall(r"sayAs\('(.*?)',", tr, re.S)))
            # Um dialogo pode vir num `sayAs` so, com os falantes marcados em [colchetes]:
            # ali as "linhas" sao os turnos, nao os arquivos.
            turnos = max([len(re.findall(r"\[[^\]]+\]", f)) for f in falas] or [0])
            tem = max(len(falas), turnos)
            ins = re.search(r'<p class="task-instr">(.*?)</p>', tr, re.S)
            ins = texto(ins.group(1)) if ins else ""
            for onde, frase in (("titulo", tit), ("instrucao", ins)):
                k = re.search(rf"\b({'|'.join(NUM)})\s+{UNIDADE}\b", frase, re.I)
                if k and NUM[k.group(1).lower()] != tem:
                    faltas.append(
                        f"  {rel}\n    {tit}\n    o {onde} promete {k.group(0).upper()}, e "
                        f"o audio da seccao tem {tem}\n    → {frase[:88]}")
            if re.search(r"\bthe same\b", tit, re.I) and falas and not any(
                    f in vistas for f in falas):
                faltas.append(
                    f"  {rel}\n    {tit}\n    o titulo diz 'the same', e a fala desta "
                    f"seccao nao apareceu antes\n    → {texto(falas[0])[:88]}")
            vistas += falas
    if faltas:
        print("GATE 46 — o audio nao tem as falas que a tela promete.\n")
        print("\n\n".join(faltas))
        print("\nCorrija na declaracao (blocos.json): o builder reemite os DOIS arquivos.")
        print("Se o certo for o texto e nao o audio, e o audio que muda — e ai o MP3 e")
        print("regerado, porque o nome do arquivo deriva do hash do transcript.")
        return 1
    print(f"✓ GATE 46 — {len(alvos)} arquivo(s): toda fala prometida existe no audio.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
