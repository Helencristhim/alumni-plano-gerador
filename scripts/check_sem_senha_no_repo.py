#!/usr/bin/env python3
"""GATE 32 — senha de aluno nunca entra no repositorio.

O repo e PUBLICO. As senhas de acesso vivem em ~/alumni-senhas (fora do git) e na env
var ACESSO_ALUNOS da Vercel. Se um dia alguem commitar a lista — ou um hash dela, que
com 4 digitos se quebra offline em milissegundos — a protecao acaba na hora, e o
historico do git guarda isso para sempre.

Procura o formato do mapa (slug de aluno -> 4 digitos) e o valor da env var em
qualquer arquivo versionado.

Uso: python3 scripts/check_sem_senha_no_repo.py [--selftest]
"""
import re
import subprocess
import sys
from pathlib import Path

PAR = re.compile(r'["\']([a-z][a-z0-9-]{4,})["\']\s*:\s*["\'](\d{4})["\']')
ENV = re.compile(r'ACESSO_ALUNOS\s*=\s*["\']?\{')
IGNORAR = {"scripts/check_sem_senha_no_repo.py"}


def alunos() -> set[str]:
    d = Path("public/aluno")
    if not d.exists():
        return set()
    return {re.sub(r"-aula\d+$", "", f.stem) for f in d.glob("*.html")}


def varrer(arquivos, conhecidos) -> list[str]:
    achados = []
    for f in arquivos:
        p = Path(f)
        if not p.is_file() or str(p) in IGNORAR:
            continue
        if p.suffix in {".png", ".jpg", ".jpeg", ".mp3", ".mp4", ".pdf", ".zip", ".webm", ".wav"}:
            continue
        try:
            txt = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        if ENV.search(txt):
            achados.append(f"{f}: valor de ACESSO_ALUNOS embutido no arquivo")
        pares = [(s, d) for s, d in PAR.findall(txt) if s in conhecidos]
        if len(pares) >= 3:
            achados.append(
                f"{f}: {len(pares)} pares slug->4 digitos (ex: {pares[0][0]}) — "
                "parece a lista de senhas"
            )
    return achados


def selftest() -> int:
    conhecidos = alunos() or {"aluno-teste-um", "aluno-teste-dois", "aluno-teste-tres"}
    amostra = sorted(conhecidos)[:3]
    tmp = Path("/tmp/_gate32_selftest.json")
    tmp.write_text("{" + ",".join(f'"{s}":"1234"' for s in amostra) + "}", encoding="utf-8")
    try:
        if not varrer([str(tmp)], conhecidos):
            print("SELFTEST FALHOU: nao pegou a lista de senhas", file=sys.stderr)
            return 1
        print("  ok — gate morde: lista de senhas em arquivo")
        tmp.write_text('ACESSO_ALUNOS={"x":"1"}', encoding="utf-8")
        if not varrer([str(tmp)], conhecidos):
            print("SELFTEST FALHOU: nao pegou a env embutida", file=sys.stderr)
            return 1
        print("  ok — gate morde: valor da env var embutido")
    finally:
        tmp.unlink(missing_ok=True)
    print("SELFTEST OK")
    return 0


def main() -> int:
    if "--selftest" in sys.argv:
        return selftest()
    versionados = subprocess.run(["git", "ls-files"], capture_output=True, text=True).stdout.split()
    achados = varrer(versionados, alunos())
    if achados:
        print("GATE 32 FALHOU — senha de aluno no repositorio PUBLICO:\n", file=sys.stderr)
        for a in achados:
            print("  " + a, file=sys.stderr)
        print("\n  As senhas vivem em ~/alumni-senhas e na env ACESSO_ALUNOS da Vercel.", file=sys.stderr)
        return 1
    print(f"GATE 32 OK — nenhuma senha de aluno versionada ({len(versionados)} arquivos)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
