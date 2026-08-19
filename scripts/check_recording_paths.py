#!/usr/bin/env python3
"""GATE 16b — a gravacao do PROFESSOR nunca cai no path do ALUNO.

O bucket `recordings` do Supabase NAO versiona e todo upload e `upsert:true`. Enquanto o
path era montado como `{slug}/{frase}.{ext}`, o link do professor e o do aluno escreviam
no MESMO objeto: um teste do professor sobrescrevia a gravacao do aluno na mesma frase.
E o sintoma era invisivel — a URL publica nao muda, so o conteudo do arquivo, entao o
botao "Your Pronunciation" do aluno passava a tocar a voz do professor sem nenhum aviso.

Incidente de 19/08/2026: rafael-pelizaro, pre-class aula 9. Recuperado so porque o
fallback `findRecordingPhraseId()` sobe uma segunda copia com nome `recording-{ts}.webm`
que nunca e sobrescrita. Esse backup e acidental — nao e garantia de nada.

A regra: TODO path do bucket `recordings` sai de `window.__alumniRecPath(slug, nome)`,
que separa a view. Concatenar `slug + '/' + ...` na mao = FAIL.

Uso:
  python3 scripts/check_recording_paths.py [--selftest]
"""
import re
import sys
from pathlib import Path

TARGET = Path("public/lib/activity-sync.js")
HELPER = "window.__alumniRecPath"

# `var filePath = <expr>;` — toda montagem de path do bucket passa por aqui.
ASSIGN = re.compile(r"^\s*var\s+filePath\s*=\s*(?P<expr>.+?);\s*$", re.M)


def check(src: str, label: str) -> list[str]:
    errs: list[str] = []

    if HELPER not in src:
        errs.append(f"{label}: helper {HELPER}() ausente — sem ele nao ha separacao por view")
    else:
        # o helper tem de DE FATO olhar a view; um helper que ignora o pathname
        # passaria no teste de nome e reintroduziria o bug.
        m = re.search(r"window\.__alumniRecPath\s*=\s*function[\s\S]{0,400}?\n\};", src)
        body = m.group(0) if m else ""
        if "/aluno/" not in body or "pathname" not in body:
            errs.append(
                f"{label}: {HELPER}() nao distingue a view "
                "(precisa olhar window.location.pathname e o segmento /aluno/)"
            )

    found = ASSIGN.findall(src)
    if not found:
        errs.append(f"{label}: nenhuma atribuicao de filePath encontrada — o gate cegou, revise o padrao")
    for expr in found:
        if HELPER not in expr:
            errs.append(
                f"{label}: path do bucket montado na mao -> `var filePath = {expr};`\n"
                f"    use {HELPER}(slug, nome) — senao o professor sobrescreve o aluno"
            )
    return errs


def selftest() -> int:
    """Prova que o gate ainda morde o padrao exato do incidente."""
    good = Path(TARGET).read_text(encoding="utf-8")
    if check(good, "atual"):
        print("SELFTEST FALHOU: o arquivo atual deveria PASSAR", file=sys.stderr)
        for e in check(good, "atual"):
            print("   " + e, file=sys.stderr)
        return 1

    cases = {
        "path concatenado na mao": good.replace(
            "var filePath = window.__alumniRecPath(slug, phraseId + '.webm');",
            "var filePath = slug + '/' + phraseId + '.webm';",
            1,
        ),
        "helper removido": good.replace(HELPER + " = function", "window.__unused = function", 1),
        "helper que ignora a view": re.sub(
            r"window\.__alumniRecPath\s*=\s*function[\s\S]*?\n\};",
            "window.__alumniRecPath = function (slug, name) {\n  return slug + '/' + name;\n};",
            good,
            count=1,
        ),
    }
    for name, mutated in cases.items():
        if mutated == good:
            print(f"SELFTEST FALHOU: mutacao '{name}' nao alterou nada", file=sys.stderr)
            return 1
        if not check(mutated, "mutante"):
            print(f"SELFTEST FALHOU: gate nao pegou '{name}'", file=sys.stderr)
            return 1
        print(f"  ok — gate morde: {name}")
    print("SELFTEST OK — o gate reprova os 3 jeitos de reintroduzir o defeito")
    return 0


def main() -> int:
    if not TARGET.exists():
        print(f"ERRO: {TARGET} nao existe", file=sys.stderr)
        return 1
    if "--selftest" in sys.argv:
        return selftest()

    errs = check(TARGET.read_text(encoding="utf-8"), str(TARGET))
    if errs:
        print("GATE 16b FALHOU — gravacao do professor pode sobrescrever a do aluno:\n", file=sys.stderr)
        for e in errs:
            print("  " + e, file=sys.stderr)
        return 1
    print(f"GATE 16b OK — todo path do bucket `recordings` passa por {HELPER}()")
    return 0


if __name__ == "__main__":
    sys.exit(main())
