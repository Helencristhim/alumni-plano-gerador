#!/usr/bin/env python3
"""Gera a senha de acesso de cada aluno (sequencial: 0001, 0002, ...).

O REPO E PUBLICO. Por isso este script NUNCA escreve senha (nem hash de senha) dentro
do repositorio: a lista em claro vai para um arquivo FORA do git, e o que o servidor
usa e uma variavel de ambiente na Vercel. Com 4 digitos, um hash publicado seria
quebrado por forca bruta offline em milissegundos — publicar hash aqui daria a
sensacao de protecao sem a protecao.

Saidas:
  ~/alumni-senhas/senhas-alunos.csv   lista em claro, para distribuir (fora do git)
  ~/alumni-senhas/ACESSO_ALUNOS.txt   valor unico para colar na env var da Vercel

Uso:
  python3 scripts/gerar_senhas_alunos.py            # so os que ainda nao tem senha
  python3 scripts/gerar_senhas_alunos.py --rotacionar SLUG   # troca a senha de um aluno
"""
import csv
import json
import os
import re
import sys
from pathlib import Path

DEST = Path.home() / "alumni-senhas"
CSV = DEST / "senhas-alunos.csv"
ENVFILE = DEST / "ACESSO_ALUNOS.txt"
ALUNOS = Path("public/aluno")


def slugs() -> list[str]:
    """Um material por aluno: o hub (sem sufixo -aulaN)."""
    out = set()
    for f in ALUNOS.glob("*.html"):
        nome = f.stem
        if re.search(r"-aula\d+$", nome):
            continue
        out.add(nome)
    return sorted(out)


def carrega() -> dict:
    if not CSV.exists():
        return {}
    with CSV.open(encoding="utf-8") as fh:
        return {r["slug"]: r["senha"] for r in csv.DictReader(fh)}


def main() -> int:
    DEST.mkdir(mode=0o700, exist_ok=True)
    atual = carrega()
    rotacionar = None
    if "--rotacionar" in sys.argv:
        rotacionar = sys.argv[sys.argv.index("--rotacionar") + 1]
        atual.pop(rotacionar, None)

    # SEQUENCIAL, por decisao do Dan (19/08/2026), ciente de que 0001/0002 se descobre
    # testando: o que isto barra e o acesso casual, nao alguem determinado.
    #
    # A numeracao NAO e recalculada por ordem alfabetica a cada execucao. Se fosse, um
    # aluno novo comecando com "A" empurraria o numero de todos os outros e invalidaria
    # senhas ja distribuidas. Quem ja tem senha mantem a sua; aluno novo recebe o proximo
    # numero livre.
    usados = {int(v) for v in atual.values() if str(v).isdigit()}
    proximo = (max(usados) + 1) if usados else 1

    novos = 0
    for s in slugs():
        if s not in atual:
            while proximo in usados:
                proximo += 1
            atual[s] = f"{proximo:04d}"
            usados.add(proximo)
            novos += 1

    with CSV.open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["slug", "senha"])
        for s in sorted(atual):
            w.writerow([s, atual[s]])
    os.chmod(CSV, 0o600)

    ENVFILE.write_text(json.dumps(atual, separators=(",", ":")), encoding="utf-8")
    os.chmod(ENVFILE, 0o600)

    print(f"alunos: {len(atual)}   senhas novas geradas: {novos}")
    if rotacionar:
        print(f"senha rotacionada: {rotacionar} -> {atual.get(rotacionar)}")
    print(f"\nlista em claro : {CSV}")
    print(f"valor da env   : {ENVFILE}")
    print("\nPROXIMO PASSO (uma vez): copie o conteudo de ACESSO_ALUNOS.txt para a")
    print("variavel de ambiente ACESSO_ALUNOS do projeto na Vercel (Production).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
