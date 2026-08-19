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
EQUIPE = DEST / "CODIGOS-ALUNOS.xlsx"
BASE_URL = "https://alumni-plano-gerador.vercel.app/aluno/"
ENVFILE = DEST / "ACESSO_ALUNOS.txt"
ALUNOS = Path("public/aluno")


# Moldes, testes e paginas auxiliares: nao sao aluno, nao recebem codigo.
NAO_SAO_ALUNO = {
    "helen-mendes", "helen-mendes-teste", "helen-mendes-v4",   # a aluna modelo
    "stephanie-vicente", "theo", "bento",                       # moldes adulto/teens/kids
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



def escreve_xlsx(destino: Path, linhas: list[list[str]]) -> None:
    """Planilha com TODAS as celulas como texto.

    Em CSV o Excel le "0001" como o numero 1 e come os zeros — e o codigo chega errado
    para o aluno. Aqui cada celula e inlineStr, entao "0001" continua "0001". Um .xlsx e
    so um zip de XMLs; nao vale uma dependencia nova (openpyxl nao instala nesta maquina,
    PEP 668).
    """
    import zipfile
    from xml.sax.saxutils import escape

    def col(i: int) -> str:
        s = ""
        while i >= 0:
            s = chr(65 + i % 26) + s
            i = i // 26 - 1
        return s

    rows = "".join(
        '<row r="%d">%s</row>' % (
            ri,
            "".join(
                '<c r="%s%d" t="inlineStr"><is><t xml:space="preserve">%s</t></is></c>'
                % (col(ci), ri, escape(str(v)))
                for ci, v in enumerate(row)
            ),
        )
        for ri, row in enumerate(linhas, 1)
    )
    sheet = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
        '<cols><col min="1" max="1" width="38" customWidth="1"/>'
        '<col min="2" max="2" width="62" customWidth="1"/>'
        '<col min="3" max="3" width="14" customWidth="1"/></cols>'
        "<sheetData>%s</sheetData></worksheet>" % rows
    )
    ct = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
          '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
          '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
          '<Default Extension="xml" ContentType="application/xml"/>'
          '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
          '<Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>'
          "</Types>")
    rels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/></Relationships>')
    wb = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
          '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
          'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
          '<sheets><sheet name="Codigos" sheetId="1" r:id="rId1"/></sheets></workbook>')
    wbr = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
           '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
           '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/></Relationships>')
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", ct)
        z.writestr("_rels/.rels", rels)
        z.writestr("xl/workbook.xml", wb)
        z.writestr("xl/_rels/workbook.xml.rels", wbr)
        z.writestr("xl/worksheets/sheet1.xml", sheet)


def materiais() -> list[str]:
    """Todo hub publicado (sem sufixo -aulaN), fora moldes e testes."""
    out = set()
    for f in ALUNOS.glob("*.html"):
        nome = f.stem
        if re.search(r"-aula\d+$", nome):
            continue
        if nome in NAO_SAO_ALUNO:
            continue
        out.add(nome)
    return sorted(out)


def raiz_do_aluno(slug: str, todos: set[str]) -> str:
    """O ALUNO dono deste material.

    O codigo e do ALUNO, nao do arquivo: quem tem varios materiais (v2, palestra,
    speech-training, backup) usa UM codigo so, o dele, em todos. A raiz e o maior
    prefixo que tambem e material publicado -- assim `nilo-...-palestra` cai em
    `nilo-...`, e `daniela-feitoza-v2` cai em `daniela-feitoza`. Sem heuristica de
    nome: so agrupa quando o prefixo existe de fato como material.
    """
    # sufixo de versao colado, sem hifen: "daniela-feitozaV2" -> "daniela-feitoza"
    colado = re.sub(r"[Vv]\d+$", "", slug)
    if colado != slug and colado in todos:
        return raiz_do_aluno(colado, todos)

    partes = slug.split("-")
    for corte in range(len(partes) - 1, 0, -1):
        pref = "-".join(partes[:corte])
        if pref in todos:
            return raiz_do_aluno(pref, todos)
    return slug


def alunos() -> dict[str, list[str]]:
    """{aluno: [materiais dele]} — a unidade que recebe codigo e o ALUNO."""
    todos = set(materiais())
    grupos: dict[str, list[str]] = {}
    for m in sorted(todos):
        grupos.setdefault(raiz_do_aluno(m, todos), []).append(m)
    return grupos


def carrega() -> dict:
    if not CSV.exists():
        return {}
    with CSV.open(encoding="utf-8") as fh:
        return {r["slug"]: r["senha"] for r in csv.DictReader(fh)}


def main() -> int:
    if not ALUNOS.is_dir():
        print(f"ABORTADO: {ALUNOS} nao existe — arvore errada?", file=sys.stderr)
        return 1
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

    grupos = alunos()
    validos = set(grupos)
    removidos = [s for s in atual if s not in validos]

    # TRAVA. Revogar codigo e o pior estrago possivel aqui: o aluno perde o numero que
    # ja recebeu e na proxima rodada ganha outro — as senhas na mao da equipe viram lixo
    # em silencio. E a causa quase sempre nao e "aluno saiu": e o comando rodando na
    # arvore errada (o dir principal fica centenas de commits atras e tem MENOS alunos).
    # Por isso revogar e SEMPRE deliberado: mais de 2 de uma vez exige confirmacao.
    limite = max(2, len(atual) // 20) if atual else 0
    if removidos and len(removidos) > limite and "--forcar-revogacao" not in sys.argv:
        print(
            f"ABORTADO: {len(removidos)} de {len(atual)} codigos seriam revogados.\n"
            f"  Isso costuma ser arvore errada (materiais faltando), nao alunos que sairam.\n"
            f"  Confira que {ALUNOS} tem TODOS os alunos.\n"
            f"  Se for intencional mesmo: --forcar-revogacao",
            file=sys.stderr,
        )
        for s in sorted(removidos)[:10]:
            print(f"    seria revogado: {s}", file=sys.stderr)
        return 1

    for s in removidos:
        del atual[s]

    novos = 0
    for s in sorted(grupos):
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

    # A env tem uma entrada por MATERIAL, mas materiais do mesmo aluno recebem o
    # MESMO codigo — o dele. Assim o servidor nao precisa adivinhar nada em runtime.
    por_material = {m: atual[a] for a, ms in grupos.items() for m in ms if a in atual}
    ENVFILE.write_text(json.dumps(por_material, separators=(",", ":")), encoding="utf-8")
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

    escreve_xlsx(EQUIPE, [["Aluno", "Link do material", "Codigo de acesso"]] + linhas)
    os.chmod(EQUIPE, 0o600)

    print(f"alunos: {len(atual)}   senhas novas geradas: {novos}   codigos revogados: {len(removidos)}")
    for s in removidos:
        print(f"    revogado: {s}")
    print(f"planilha p/ equipe: {EQUIPE}")
    if rotacionar:
        print(f"senha rotacionada: {rotacionar} -> {atual.get(rotacionar)}")
    print(f"\nlista em claro : {CSV}")
    print(f"valor da env   : {ENVFILE}")
    print("\nPROXIMO PASSO (uma vez): copie o conteudo de ACESSO_ALUNOS.txt para a")
    print("variavel de ambiente ACESSO_ALUNOS do projeto na Vercel (Production).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
