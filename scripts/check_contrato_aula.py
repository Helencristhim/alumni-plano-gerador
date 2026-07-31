#!/usr/bin/env python3
"""GATE 12 — a aula entrega o que o CONTRATO do framework dela promete.

O PROBLEMA QUE ISTO RESOLVE
--------------------------
"Gere 3 aulas do tipo Leitura pra aluna X" só é uma instrução confiável se alguma
coisa CONFERIR que saiu uma aula de leitura. Hoje os gates são universais (vozes,
áudio, português na tela...) e valem pra qualquer aula; nenhum deles sabe dizer que
UMA AULA DE LEITURA precisa ter texto central, gist e true/false. Sem isso, esquecer
o true/false gera uma aula que passa em tudo e não é o que foi pedido.

O contrato mora em public/data/frameworks.json (`contrato` de cada framework) e é
editável pelo catálogo. Os exercícios que ele pode citar vêm de
public/data/exercicios.json — o banco PROVADO contra o builder.

A REGRA QUE PROTEGE O ALUNO ATUAL (é o coração deste arquivo)
--------------------------------------------------------------
Editar um contrato NUNCA pode reprovar aula que já existe. Duas travas:

1. **Aula sem o carimbo `<meta name="alumni-contrato">` é IGNORADA.** Todo o legado
   (Pelizaro incluído) está aí: nasceu antes do eixo e não será tocado (REGRA 30).

2. **Contrato é VERSIONADO e a aula carimba a versão em que nasceu** (`ppp@1`). O
   gate julga cada aula pelo contrato DAQUELA versão, buscado no histórico. Tirar um
   exercício do contrato hoje cria a versão 2 e não mexe em nada que nasceu na 1.

Sem a versão, o editor seria uma arma: uma edição inocente no navegador viraria
centenas de aulas vermelhas no CI, e a saída seria "desliga o gate" — que é como
gate morre.

Uso:
  python3 scripts/check_contrato_aula.py                 # varre o repo
  python3 scripts/check_contrato_aula.py --selftest      # prova que morde
  python3 scripts/check_contrato_aula.py --sugerir ppp   # mede as aulas e propõe contrato
"""

import argparse
import glob
import json
import os
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
BANCO = RAIZ / "public" / "data" / "exercicios.json"
FRAMEWORKS = RAIZ / "public" / "data" / "frameworks.json"


def carrega_banco():
    d = json.loads(BANCO.read_text(encoding="utf-8"))
    return {e["id"]: e for e in d["exercicios"]}


def carrega_contratos():
    """{framework_id: {versao: contrato}} — atual + histórico, achatados por versão."""
    d = json.loads(FRAMEWORKS.read_text(encoding="utf-8"))
    out = {}
    for cat in d.get("categorias", []):
        for f in cat.get("frameworks", []):
            c = f.get("contrato")
            if not c:
                continue
            porv = {int(c["versao"]): c}
            for velho in f.get("contrato_historico", []):
                porv[int(velho["versao"])] = velho
            out[f["id"]] = {"label": f.get("label", f["id"]), "versoes": porv}
    return out


def eh_aula(path):
    """Hub NÃO é aula. O builder carimba o framework no hub também (ele é a capa do
    aluno), mas o hub não tem slides — julgá-lo pelo contrato faria toda aula "faltar"
    todo exercício. Contrato é sobre a AULA: {slug}-aula{N}.html."""
    return bool(re.search(r"-aula\d+\.html$", os.path.basename(path)))


def corpo_dos_slides(h):
    i = h.find('class="slides-wrapper"')
    if i < 0:
        i = h.find("slides-wrapper")
    j = h.find("</body>")
    return h[i:j] if i >= 0 else h


def exercicios_presentes(corpo, banco):
    """Quais exercícios do banco aparecem no HTML — pelo MARCADOR (classe exclusiva).
    Exercício sem marcador não é detectável e nunca entra aqui: ver `verificavel`."""
    achados = set()
    for eid, e in banco.items():
        for m in e["marcadores"]:
            if re.search(r'class="[^"]*\b' + re.escape(m) + r'\b', corpo):
                achados.add(eid)
                break
    return achados


def valida_arquivo(path, banco, contratos, fails):
    if not eh_aula(path):
        return False
    h = pathlib.Path(path).read_text(encoding="utf-8", errors="replace")
    m = re.search(r'<meta name="alumni-contrato" content="([a-z0-9\-]+)@(\d+)"', h)
    if not m:
        return False  # legado / aula sem contrato — não é problema deste gate
    fw, versao = m.group(1), int(m.group(2))
    rel = os.path.relpath(path, RAIZ)

    if fw not in contratos:
        fails.append(f"{rel}: carimba contrato de '{fw}', que não existe em frameworks.json")
        return True
    if versao not in contratos[fw]["versoes"]:
        fails.append(
            f"{rel}: carimba {fw}@{versao}, mas essa versão sumiu do frameworks.json. "
            f"Versão de contrato NUNCA se apaga — o histórico é o que protege a aula "
            f"antiga de ser julgada por regra nova.")
        return True

    contrato = contratos[fw]["versoes"][versao]
    presentes = exercicios_presentes(corpo_dos_slides(h), banco)

    for eid in contrato.get("obrigatorios", []):
        if eid not in banco:
            fails.append(f"{rel}: contrato {fw}@{versao} exige '{eid}', que não está no banco")
        elif not banco[eid]["verificavel"]:
            continue  # declarado como não detectável — o banco já diz isso
        elif eid not in presentes:
            fails.append(
                f"{rel}: contrato {fw}@{versao} exige o exercício '{eid}' "
                f"({banco[eid]['label']}) e a aula não tem")
    for eid in contrato.get("proibidos", []):
        if eid in presentes:
            fails.append(
                f"{rel}: contrato {fw}@{versao} proíbe '{eid}' "
                f"({banco[eid]['label']}) e a aula tem")
    minimo = contrato.get("min_slides")
    if minimo:
        n = len(re.findall(r'class="slide[ "]', corpo_dos_slides(h)))
        if n < minimo:
            fails.append(f"{rel}: contrato {fw}@{versao} pede {minimo}+ slides, a aula tem {n}")
    return True


def varre():
    banco, contratos = carrega_banco(), carrega_contratos()
    fails, com_contrato = [], 0
    alvos = glob.glob(str(RAIZ / "public" / "professor" / "*.html"))
    alvos += glob.glob(str(RAIZ / "public" / "aluno" / "*.html"))
    for p in sorted(alvos):
        if valida_arquivo(p, banco, contratos, fails):
            com_contrato += 1

    if fails:
        print(f"GATE 12 FALHOU — {len(fails)} problema(s):", file=sys.stderr)
        for f in fails:
            print(f"  {f}", file=sys.stderr)
        return 1
    print(f"GATE 12 OK — {com_contrato} arquivo(s) com contrato conferido, "
          f"{len(alvos) - com_contrato} sem carimbo (legado, ignorado por regra)")
    return 0


def sugerir(fw):
    """Mede as aulas que JÁ rodam esse framework e propõe um contrato: obrigatório =
    o que está em TODAS (interseção), opcional = o que está em alguma. Semente para o
    humano editar no catálogo — medição não decide pedagogia, só mostra o que há."""
    banco = carrega_banco()
    achados = []
    for p in sorted(glob.glob(str(RAIZ / "public" / "professor" / "*.html"))):
        if not eh_aula(p):
            continue
        h = pathlib.Path(p).read_text(encoding="utf-8", errors="replace")
        if not re.search(r'<meta name="alumni-framework" content="' + re.escape(fw) + '"', h):
            continue
        corpo = corpo_dos_slides(h)
        achados.append((os.path.basename(p),
                        exercicios_presentes(corpo, banco),
                        len(re.findall(r'class="slide[ "]', corpo))))
    if not achados:
        print(f"nenhuma aula carimbada com framework '{fw}'")
        return 1
    inter = set.intersection(*(a[1] for a in achados))
    uniao = set().union(*(a[1] for a in achados))
    print(f"framework '{fw}' — {len(achados)} aula(s) medida(s):")
    for nome, ex, n in achados:
        print(f"  {nome:34} {n:3} slides  {sorted(ex)}")
    print(f"\n  obrigatorios (em TODAS): {sorted(inter)}")
    print(f"  opcionais (em alguma):   {sorted(uniao - inter)}")
    print(f"  min_slides sugerido:     {min(a[2] for a in achados)}")
    return 0


def selftest():
    """Prova que o gate morde: aula sintética sem o exercício obrigatório tem de falhar,
    e a MESMA aula sem o carimbo tem de passar (legado intocado)."""
    banco = carrega_banco()
    contratos = {"x": {"label": "X", "versoes": {1: {"versao": 1,
                                                    "obrigatorios": ["reading"],
                                                    "proibidos": ["quickfire"]}}}}
    import tempfile
    ok = True
    corpo_sem = ('<div class="slides-wrapper"><div class="slide"><div class="qf-card">'
                 'q</div></div></div></body>')
    with tempfile.TemporaryDirectory() as d:
        # 1) com carimbo: falta o obrigatório E usa o proibido -> 2 falhas
        p = os.path.join(d, "x-aula1.html")
        pathlib.Path(p).write_text('<meta name="alumni-contrato" content="x@1">' + corpo_sem)
        fails = []
        valida_arquivo(p, banco, contratos, fails)
        if len(fails) != 2:
            print(f"selftest FALHOU: esperava 2 falhas, veio {len(fails)}: {fails}", file=sys.stderr)
            ok = False
        # 2) mesma aula SEM carimbo: o gate não pode dizer nada (legado)
        p2 = os.path.join(d, "x-aula2.html")
        pathlib.Path(p2).write_text(corpo_sem)
        fails2 = []
        tocou = valida_arquivo(p2, banco, contratos, fails2)
        if tocou or fails2:
            print(f"selftest FALHOU: aula sem carimbo foi julgada ({fails2})", file=sys.stderr)
            ok = False
        # 3) versão inexistente no histórico tem de acusar
        p3 = os.path.join(d, "x-aula3.html")
        pathlib.Path(p3).write_text('<meta name="alumni-contrato" content="x@9">' + corpo_sem)
        fails3 = []
        valida_arquivo(p3, banco, contratos, fails3)
        if not fails3:
            print("selftest FALHOU: versão de contrato sumida passou batido", file=sys.stderr)
            ok = False
    print("GATE 12 selftest OK — morde no que deve e cala no legado" if ok else "selftest FALHOU")
    return 0 if ok else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--sugerir", metavar="FRAMEWORK")
    a = ap.parse_args()
    if a.selftest:
        raise SystemExit(selftest())
    if a.sugerir:
        raise SystemExit(sugerir(a.sugerir))
    raise SystemExit(varre())
