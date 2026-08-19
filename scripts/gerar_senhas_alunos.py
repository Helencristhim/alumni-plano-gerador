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
EQUIPE = DEST / "senhas-para-equipe.csv"
BASE_URL = "https://alumni-plano-gerador.vercel.app/aluno/"
ENVFILE = DEST / "ACESSO_ALUNOS.txt"
ALUNOS = Path("public/aluno")


# Moldes, testes e paginas auxiliares: nao sao aluno, nao recebem codigo.
NAO_SAO_ALUNO = {
    "helen-mendes", "helen-mendes-teste", "helen-mendes-v4",   # a aluna modelo
    "stephanie-vicente", "theo", "bento",                       # moldes adulto/teens/kids
    "luiz-bressane-backup-a2",                                  # backup de material
}


def eh_redirecionamento(f: Path) -> bool:
    """Pagina que so manda para outra (ex: daniela-feitoza -> daniela-feitoza-v2).

    Nunca pode pedir codigo: o aluno digitaria uma vez aqui e outra no destino.
    Sem codigo, o redirect passa direto e a senha e pedida so no material real.
    """
    try:
        t = f.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return False
    if len(t) > 60_000:          # material de verdade; redirect e sempre pequeno
        return False
    return ("location.replace" in t or "http-equiv=\"refresh\"" in t
            or "Redirecting" in t)


def slugs() -> list[str]:
    """Um material por aluno: o hub (sem sufixo -aulaN), fora moldes e redirects."""
    out = set()
    for f in ALUNOS.glob("*.html"):
        nome = f.stem
        if re.search(r"-aula\d+$", nome):
            continue
        if nome in NAO_SAO_ALUNO:
            continue
        if eh_redirecionamento(f):
            continue
        out.add(nome)

    # Aluno com dois conjuntos de material (X e X-v2, os dois reais): fica so o V2.
    # Ordem do Dan (19/08/2026): "tira os antigos, deixa so os V2".
    for nome in list(out):
        if nome + "-v2" in out:
            out.discard(nome)
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

    validos = set(slugs())
    removidos = [s for s in atual if s not in validos]
    for s in removidos:
        del atual[s]

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

    # Lista para a equipe distribuir: nome e link, nao slug. O nome sai do <h1> do
    # proprio material, entao acompanha qualquer correcao feita la.
    import html as _html
    linhas = []
    for slug in sorted(atual):
        f = ALUNOS / f"{slug}.html"
        nome = slug.replace("-", " ").title()
        if f.exists():
            m = re.search(r"<h1[^>]*>(.*?)</h1>", f.read_text(encoding="utf-8", errors="ignore"), re.S)
            if m:
                bruto = re.sub(r"<[^>]+>", "", m.group(1))
                bruto = _html.unescape(bruto).strip()
                if bruto:
                    nome = bruto
        linhas.append([nome, BASE_URL + slug + ".html", atual[slug]])

    with EQUIPE.open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["Aluno", "Link do material", "Codigo de acesso"])
        w.writerows(linhas)
    os.chmod(EQUIPE, 0o600)

    print(f"alunos: {len(atual)}   senhas novas geradas: {novos}   codigos revogados: {len(removidos)}")
    for s in removidos:
        print(f"    revogado: {s}")
    print(f"lista p/ equipe: {EQUIPE}")
    if rotacionar:
        print(f"senha rotacionada: {rotacionar} -> {atual.get(rotacionar)}")
    print(f"\nlista em claro : {CSV}")
    print(f"valor da env   : {ENVFILE}")
    print("\nPROXIMO PASSO (uma vez): copie o conteudo de ACESSO_ALUNOS.txt para a")
    print("variavel de ambiente ACESSO_ALUNOS do projeto na Vercel (Production).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
