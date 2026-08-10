#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Roda LOCALMENTE os mesmos gates que o CI roda — todos, na mesma ordem.

POR QUE ISTO EXISTE (10/08/2026)
--------------------------------
Um PR de 4 aulas da gabriela-pires reprovou no **GATE 16** depois de o agente que as
escreveu ter rodado cinco gates e concluido que estava tudo verde. Os cinco vieram de um
briefing escrito na mao; o GATE 16 nao estava nele. E o GATE 16 so roda no CI.

O defeito NAO foi do agente. Foi de nao existir um jeito de perguntar "quais sao os
gates?" — a resposta morava, espalhada, em 439 linhas de YAML. Quem gera aula tinha duas
opcoes: decorar a lista (que muda) ou abrir um PR e descobrir no vermelho.

No mesmo dia, os outros CINCO alunos gerados passaram no GATE 16 **por sorte** — as aulas
deles ja tinham role-play por construcao. Sorte nao e cobertura.

A ESCOLHA DE DESIGN QUE IMPORTA
-------------------------------
Este script **NAO tem lista de gates**. Ele LE `.github/workflows/validate-lessons.yml`,
que e a fonte da verdade, e executa os mesmos comandos. Consequencia direta: gate novo
adicionado ao CI passa a rodar aqui **no mesmo commit**, sem ninguem lembrar de atualizar
nada. Uma lista copiada aqui nasceria certa e envelheceria em silencio — que e exatamente
o defeito que este script existe para matar.

Pelo mesmo motivo ele replica a classificacao added/modified do CI em vez de inventar a
sua: se o criterio mudar la, muda aqui.

O QUE ELE NAO FAZ
-----------------
Nao substitui o CI. O CI roda em arvore limpa; aqui roda no seu worktree, com o que voce
tem no disco. Verde aqui e "provavelmente verde la", nao garantia — e continua PROIBIDO
mergear na mao: quem mergeia e o `merge_aula.py`, que exige o check `gates` do GitHub
concluido e verde (o `main` nao tem branch protection; sem essa trava, PR vermelho entra).

USO
---
    python3 scripts/run_gates.py                 # tudo, contra origin/main
    python3 scripts/run_gates.py --base origin/main
    python3 scripts/run_gates.py --list          # so mostra o que rodaria
    python3 scripts/run_gates.py --only contrato # so os passos cujo nome/comando casam
"""
import argparse
import os
import re
import subprocess
import sys

WORKFLOW = ".github/workflows/validate-lessons.yml"
# Caminhos que o passo `id: files` do CI usa para classificar o diff do PR.
PATHSPEC = ["public/professor/*.html", "public/aluno/*.html"]


def sh(cmd, cwd=None):
    return subprocess.run(cmd, shell=True, cwd=cwd, text=True,
                          capture_output=True).stdout.strip()


def raiz_do_repo():
    r = sh("git rev-parse --show-toplevel")
    if not r:
        sys.exit("nao estou dentro de um repositorio git")
    return r


def classifica(base):
    """added/modified exatamente como o passo `id: files` do CI.

    O CI falha de proposito quando ha arquivo de aula no diff e a classificacao sai
    vazia — porque foi assim que os GATES 1-7 ficaram meses sendo pulados com o check
    verde do lado. Aqui a mesma checagem, pelo mesmo motivo.
    """
    if not sh(f"git merge-base {base} HEAD"):
        sys.exit(f"sem merge base entre {base} e HEAD — impossivel classificar. "
                 f"Rode `git fetch origin` antes.")
    ps = " ".join(f"'{p}'" for p in PATHSPEC)
    add = sh(f"git diff --name-only --diff-filter=A {base}...HEAD -- {ps}").split()
    mod = sh(f"git diff --name-only --diff-filter=M {base}...HEAD -- {ps}").split()
    dele = sh(f"git diff --name-only --diff-filter=D {base}...HEAD -- {ps}").split()
    tocados = sh(f"git diff --name-only {base}...HEAD -- {ps}").split()
    if tocados and not (add or mod or dele):
        sys.exit(f"{len(tocados)} arquivo(s) de aula no diff, mas a classificacao saiu "
                 f"VAZIA — os gates por-arquivo seriam pulados. Falhando de proposito.")
    return add, mod


def passos_do_workflow(raiz):
    """Os passos com `run:` do job `gates`, na ordem, com nome/condicao/comando."""
    import yaml
    with open(os.path.join(raiz, WORKFLOW), encoding="utf-8") as f:
        wf = yaml.safe_load(f)
    job = wf.get("jobs", {}).get("gates")
    if not job:
        sys.exit(f"job `gates` nao encontrado em {WORKFLOW}")
    out = []
    for st in job.get("steps", []):
        if "run" not in st:
            continue                      # actions/checkout, setup-python, etc.
        if st.get("id") == "files":
            continue                      # replicado por classifica(), acima
        out.append({"nome": st.get("name", "(sem nome)"),
                    "cond": st.get("if"),
                    "cmd": st["run"]})
    return out


def expande(cmd, base_ref, add, mod):
    """Troca os `${{ ... }}` do GitHub Actions pelos valores locais.

    Se aparecer uma expressao que este script nao conhece, ele PARA em vez de rodar um
    comando meio substituido — melhor recusar do que dar verde mentiroso.
    """
    cmd = cmd.replace("${{ github.base_ref }}", base_ref)
    cmd = cmd.replace("${{ steps.files.outputs.added }}", " ".join(add))
    cmd = cmd.replace("${{ steps.files.outputs.modified }}", " ".join(mod))
    resto = re.findall(r"\$\{\{[^}]*\}\}", cmd)
    if resto:
        return None, resto
    return cmd, []


def roda_condicao(cond, add, mod):
    """Só as condições que o workflow de fato usa. Desconhecida => RODA (nunca pula)."""
    if not cond:
        return True
    c = cond.strip()
    if "steps.files.outputs.added != ''" in c:
        return bool(add)
    if "steps.files.outputs.modified != ''" in c:
        return bool(mod)
    return True


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base", default="origin/main")
    ap.add_argument("--list", action="store_true", help="so lista, nao executa")
    ap.add_argument("--only", help="substring do nome ou do comando")
    a = ap.parse_args()

    raiz = raiz_do_repo()
    os.chdir(raiz)
    base_ref = a.base.split("/", 1)[1] if a.base.startswith("origin/") else a.base

    add, mod = classifica(a.base)
    print(f"base={a.base}  novos={len(add)}  modificados={len(mod)}")
    if not add and not mod:
        print("(nenhum HTML de aula no diff — só os gates de repo inteiro vão rodar)")
    print()

    passos = passos_do_workflow(raiz)
    falhas, pulados, ok = [], [], []

    for p in passos:
        cmd, resto = expande(p["cmd"], base_ref, add, mod)
        if a.only and a.only.lower() not in (p["nome"] + " " + p["cmd"]).lower():
            continue
        if not roda_condicao(p["cond"], add, mod):
            pulados.append(p["nome"])
            continue
        if cmd is None:
            print(f"?? PULADO  {p['nome']}\n   expressao nao suportada: {resto}")
            pulados.append(p["nome"])
            continue
        if a.list:
            print(f"·  {p['nome']}\n   {cmd.strip()}")
            continue

        print(f"── {p['nome']}")
        r = subprocess.run(cmd, shell=True, text=True, capture_output=True,
                           executable="/bin/bash")
        if r.returncode == 0:
            ok.append(p["nome"])
            print("   OK")
        else:
            falhas.append((p["nome"], (r.stdout + r.stderr).strip()))
            print("   FALHOU")

    if a.list:
        return 0

    print(f"\n{'='*70}\nOK: {len(ok)}   FALHOU: {len(falhas)}   pulado: {len(pulados)}")
    for nome, saida in falhas:
        print(f"\n### {nome}\n{saida[-2500:]}")
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
