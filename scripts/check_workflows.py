#!/usr/bin/env python3
"""GATE 0 — todo workflow do CI existe de verdade.

POR QUE ISSO EXISTE
-------------------
Um workflow com YAML invalido NAO falha: ele nao roda. O GitHub nem cria job
(`total_count: 0`, "startup failure"). Nao ha vermelho na PR, nao ha alerta, nao
ha log — o arquivo esta la, com nome bonito, e nao faz absolutamente nada.

Foi o que aconteceu com o `guard-main.yml`: nasceu em 15/06/2026 com uma string
multi-linha comecando na coluna 0 dentro de um bloco `run: |` (o que ENCERRA o
bloco e quebra o parse do arquivo inteiro). Ficou **um mes** e **100 runs**, todos
"failure" sem um unico job executado. Ninguem viu, porque ninguem olha o run de um
workflow que deveria ser silencioso quando esta tudo bem.

O custo nao foi teorico: aquele workflow e quem RESTAURA aula apagada por push
defasado (o incidente 6cd5b3b9) e quem avanca a tag `last-good`. Como nunca rodou,
a tag ficou congelada 1.683 commits atras — e o proprio arquivo manda usa-la para
"restaurar tudo a qualquer momento". Uma rede que mente e pior que nao ter rede.

E irmao do CANARIO: aquele prova que o gate ainda MORDE; este prova que o gate
ainda EXISTE.

Checa, em todo .yml de .github/workflows/:
  1. parseia como YAML;
  2. tem `on:` (senao nunca dispara);
  3. tem `jobs:` com pelo menos um job (senao nao faz nada).

Uso:  python3 scripts/check_workflows.py
"""
import glob
import os
import sys

try:
    import yaml
except ImportError:
    print("PyYAML ausente — instale com: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(ROOT, ".github", "workflows")


def main():
    arquivos = sorted(glob.glob(os.path.join(DIR, "*.yml")) +
                      glob.glob(os.path.join(DIR, "*.yaml")))
    if not arquivos:
        print("nenhum workflow encontrado — isso ja e suspeito")
        return 1

    falhas = []
    for p in arquivos:
        rel = os.path.relpath(p, ROOT)
        try:
            d = yaml.safe_load(open(p, encoding="utf-8"))
        except Exception as e:
            msg = " ".join(str(e).split())[:160]
            falhas.append(f"{rel}: YAML INVALIDO — o GitHub nao roda este workflow "
                          f"(startup failure, zero jobs, zero alerta). {msg}")
            continue
        if not isinstance(d, dict):
            falhas.append(f"{rel}: nao e um mapa YAML")
            continue
        # `on:` vira True no safe_load (YAML 1.1 le "on" como booleano)
        if "on" not in d and True not in d:
            falhas.append(f"{rel}: sem `on:` — nunca dispara")
        jobs = d.get("jobs")
        if not isinstance(jobs, dict) or not jobs:
            falhas.append(f"{rel}: sem `jobs:` — nao executa nada")

    for f in falhas:
        print(f"  X {f}")
    if falhas:
        print(f"\nGATE 0 REPROVADO — {len(falhas)} workflow(s) que nao rodam.")
        print("Dica: dentro de `run: |` TODA linha fica indentada. Continuacao na coluna 0")
        print("encerra o bloco e quebra o arquivo inteiro. Para texto multi-linha use")
        print("`-m` repetido (git commit) ou heredoc indentado + --body-file (gh).")
        return 1
    print(f"GATE 0 OK — {len(arquivos)} workflows parseiam, disparam e tem jobs.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
