#!/usr/bin/env python3
"""GATE 31 — o botao Reset zera TUDO que conta progresso.

O Reset limpava matching, fill-in, quiz e speech, mas NAO os vocab cards nem os think
cards. Como o `collectState()` recolhe o estado direto do DOM logo em seguida, as classes
que sobravam eram salvas de novo: a aula "resetada" voltava a marcar 20-30% em vez de 0%,
e o aluno nao conseguia refazer o Pre-class.
Medido em 19/08/2026 (rafael-pelizaro, aulas 12-20 presas entre 21% e 33%).

A regra que este gate cobra e a REGRA 18.1: os tipos de exercicio que contam progresso
sao os mesmos que o Reset tem de limpar. Nao basta consertar os dois que faltavam — se
alguem adicionar um tipo novo ao progresso e esquecer o Reset, o defeito volta. Por isso
o gate falha nos DOIS sentidos: tipo contado que o Reset nao limpa, e tipo novo aparecendo
no progresso sem estar declarado aqui.

Uso: python3 scripts/check_reset_completo.py [--selftest]
"""
import re
import sys
from pathlib import Path

LIB = Path("public/lib/activity-sync.js")

# REGRA 18.1 — (container, classe que marca "feito"). Fonte: CLAUDE.md.
TIPOS = [
    (".vocab-card-pc", "listened"),
    (".match-row", "correct"),
    (".blank-input", "correct"),
    (".quiz-option", "correct"),
    (".speech-result", "show"),
    (".order-item", "correct-order"),
    (".think-card", "recorded"),
]


def bloco(src: str, nome: str) -> str:
    i = src.find("function " + nome)
    if i == -1:
        return ""
    d, k = 0, src.index("{", i)
    for j in range(k, len(src)):
        if src[j] == "{":
            d += 1
        elif src[j] == "}":
            d -= 1
            if d == 0:
                return src[i:j + 1]
    return src[i:]


def check(src: str) -> list[str]:
    errs = []
    reset = bloco(src, "limparMarcadores")
    if not reset:
        return ["limparMarcadores() nao encontrado — o gate cegou, revise o padrao"]

    # os dois caminhos de reset (o botao e o remoto via _resetAt) tem de usar a MESMA
    # limpeza; se um deles parar de chamar, volta a divergir e o defeito renasce.
    for fn in ("resetLesson", "aplicarResetRemoto"):
        b = bloco(src, fn)
        if not b:
            errs.append(f"{fn}() nao encontrado")
        elif "limparMarcadores(" not in b:
            errs.append(f"{fn}() nao chama limparMarcadores() — os dois resets divergem")

    # 1) todo tipo que conta progresso e limpo pelo Reset
    for cont, cls in TIPOS:
        sel = cont.lstrip(".")
        toca = re.search(r"querySelectorAll\('\." + re.escape(sel) + r"[^']*'\)", reset)
        limpa = re.search(r"classList\.remove\([^)]*['\"]" + re.escape(cls) + r"['\"]", reset)
        if not toca:
            errs.append(f"limparMarcadores() nao toca em {cont} — a aula nao zera (REGRA 18.1)")
        elif not limpa:
            errs.append(f"limparMarcadores() toca em {cont} mas nao remove a classe '{cls}'")

    # 1b) o reset remoto tem de ser honrado ANTES do merge-uniao. Se o merge rodar
    # primeiro, o estado local ressuscita o que o servidor apagou — que e o defeito
    # original. A ordem dentro do loadFromSupabase e o que garante isso.
    load = bloco(src, "loadFromSupabase")
    if not load:
        errs.append("loadFromSupabase() nao encontrado")
    else:
        pos_reset = load.find("aplicarResetRemoto(")
        pos_merge = load.find("mergeState(")
        if pos_reset == -1:
            errs.append("loadFromSupabase() nao chama aplicarResetRemoto() — reset feito no "
                        "servidor sera desfeito pelo navegador")
        elif pos_merge != -1 and pos_reset > pos_merge:
            errs.append("loadFromSupabase() faz o merge ANTES de honrar o reset remoto — "
                        "o progresso apagado ressuscita")
        if "resetKey" not in load:
            errs.append("loadFromSupabase() nao consulta resetKey — o reset repetiria a cada "
                        "abertura, ou nunca aconteceria")

    # 2) tipo novo no progresso que ninguem declarou aqui
    prog = bloco(src, "updateProgress") or src
    achados = set(re.findall(r"querySelectorAll\('\.([a-z-]+)\.([a-z-]+)'\)", prog))
    conhecidos = {(c.lstrip("."), k) for c, k in TIPOS}
    for cont, cls in sorted(achados - conhecidos):
        errs.append(
            f"o progresso conta '.{cont}.{cls}', que nao esta declarado no gate — "
            "adicione em TIPOS e garanta que o resetLesson limpa"
        )
    return errs


def selftest() -> int:
    src = LIB.read_text(encoding="utf-8")
    if check(src):
        print("SELFTEST FALHOU: o arquivo atual deveria PASSAR", file=sys.stderr)
        for e in check(src):
            print("   " + e, file=sys.stderr)
        return 1
    # o defeito real de 19/08: tirar a limpeza dos vocab cards
    mut = re.sub(
        r"escopo\.querySelectorAll\('\.vocab-card-pc'\)[\s\S]*?\}\);\n", "", src, count=1
    )
    if mut == src:
        print("SELFTEST FALHOU: mutacao nao alterou nada", file=sys.stderr)
        return 1
    if not check(mut):
        print("SELFTEST FALHOU: o gate nao pegou o Reset sem vocab card", file=sys.stderr)
        return 1
    print("  ok — gate morde: Reset que esquece o vocab card")
    print("SELFTEST OK — o gate reprova o defeito de 19/08/2026")
    return 0


def main() -> int:
    if not LIB.exists():
        print(f"ERRO: {LIB} nao existe", file=sys.stderr)
        return 1
    if "--selftest" in sys.argv:
        return selftest()
    errs = check(LIB.read_text(encoding="utf-8"))
    if errs:
        print("GATE 31 FALHOU — o Reset nao zera tudo que conta progresso:\n", file=sys.stderr)
        for e in errs:
            print("  " + e, file=sys.stderr)
        return 1
    print(f"GATE 31 OK — os {len(TIPOS)} tipos que contam progresso sao limpos pelo Reset")
    return 0


if __name__ == "__main__":
    sys.exit(main())
