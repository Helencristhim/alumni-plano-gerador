#!/usr/bin/env python3
"""
GATE bloqueante: impede a REINTRODUCAO de padroes ja consertados.

Existe porque os gates de aula sao permissivos com arquivos MODIFICADOS
(validate_lesson roda em modo aviso pra nao travar legado) e o anti-regressao so
conta ex-lesson/stamp/slide. Resultado: uma branch ramificada ANTES de um
conserto sobrescreve o arquivo e reintroduz o bug ao mergear, em silencio.
Aconteceu em 10/07/2026 com o alert do Chrome e com os links de busca.

Criterio: NAO e "zero ocorrencias" (49 paginas legadas ainda tem link de busca, e
travar todo PR que as toque seria pior que o bug). E "nao PIOROU vs a base":
  - arquivo NOVO       -> qualquer ocorrencia reprova
  - arquivo MODIFICADO -> reprova so se o PR AUMENTA a contagem vs a base
  - arquivo que MELHORA -> passa (e o caminho pra zerar o legado aos poucos)

Padroes:
  1. alert('Please use Google Chrome') — sem SpeechRecognition (Safari/Firefox/
     celular) o guard abortava a gravacao inteira. REGRA 8.1: proibido. O certo e
     hasSR=false -> MediaRecorder grava, aluno se ouve, audio sobe pro Supabase,
     exercicio conta como feito.
  2. Link de BUSCA em Complementares — REGRA 17: cada media card aponta pro
     recurso direto. Link de busca muda de resultado e joga o aluno numa pagina
     de pesquisa.

Uso:  python3 scripts/check_forbidden_patterns.py [--base origin/main] <arquivos...>
"""
import re
import subprocess
import sys

# zilaudio: material morto (lista de exclusao). Seu startRecording legado vem de
# public/components/exercises.js e nao tem MediaRecorder — retrofit exigiria
# reescrita, nao substituicao. Isento ate ser removido.
EXEMPT = ("zilaudio",)

PATTERNS = [
    (re.compile(r"Please use Google Chrome"),
     "alert Chrome-only no startRecording — mata a gravacao em Safari/Firefox/celular "
     "(REGRA 8.1). Use o fallback hasSR do modelo (public/professor/helen-mendes-aula1.html)."),
    (re.compile(r'href="[^"]*(?:youtube\.com/results\?search_query|google\.com/search\?)'),
     "link de BUSCA em Complementares — use a URL canonica do recurso (REGRA 17)."),
    (re.compile(r'href="[^"]*(?:businessenglishpod\.com|eslpod\.com|englishclass101\.com|hbr\.org)'),
     "link de conteudo PAGO/cadastro em Complementares — curso pago "
     "(BusinessEnglishPod/ESLPod/EnglishClass101) ou paywall (HBR). O aluno tem de so "
     "clicar e acessar, sem cadastro nem dinheiro: use recurso gratuito e aberto "
     "(YouTube/TED/VOA Learning English/BBC Learning English) — REGRA 17."),
]

TARGET = re.compile(r"public/(aluno|professor)/[^/]+\.html$")


def base_text(ref, path):
    """Conteudo do arquivo na base. Vazio => arquivo novo no PR."""
    r = subprocess.run(["git", "show", f"{ref}:{path}"],
                       capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ""


def main():
    argv = sys.argv[1:]
    ref = "origin/main"
    if "--base" in argv:
        i = argv.index("--base")
        ref = argv[i + 1]
        argv = argv[:i] + argv[i + 2:]

    paths = [a for a in argv if TARGET.search(a)]
    if not paths:
        print("nenhum arquivo de aluno/professor no PR — nada a checar.")
        return 0

    fails, improved = [], []
    for p in paths:
        if any(x in p for x in EXEMPT):
            continue
        try:
            with open(p, encoding="utf-8", errors="replace") as fh:
                now = fh.read()
        except FileNotFoundError:
            continue  # deletado no PR
        was = base_text(ref, p)
        for rx, why in PATTERNS:
            n_now = len(rx.findall(now))
            n_was = len(rx.findall(was))
            if n_now > n_was:
                fails.append((p, n_was, n_now, why))
            elif n_now < n_was:
                improved.append((p, n_was, n_now))

    print(f"=== padroes proibidos — {len(paths)} arquivo(s), base {ref} ===\n")
    for p, n_was, n_now, why in fails:
        print(f"  X {p}: {n_was} -> {n_now}  {why}")
    for p, n_was, n_now in improved:
        print(f"  + {p}: {n_was} -> {n_now} (melhorou)")

    if fails:
        print(f"\nBLOQUEADO — {len(fails)} reintroducao(oes). "
              f"Rebase na base atual e refaca por cima do conserto.")
        return 1
    print("\n  OK — nenhuma reintroducao.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
