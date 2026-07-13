#!/usr/bin/env python3
"""
check_lesson_integrity.py — TRAVA DE DEPLOY.

Varre as aulas publicadas (public/aluno + public/professor) e FALHA (exit 1)
se encontrar qualquer um dos sintomas de geração interrompida pela cota:

  1. HTML vazio / corrompido / truncado (sem </html> no fim) — geração cortada
     no meio do arquivo.
  2. Referência a um .mp3 que NÃO existe em public/audio/ — o HTML foi publicado
     apontando para um áudio que nunca foi gerado (aula "sem som").

Uso:
  python3 scripts/check_lesson_integrity.py            # varre tudo (modo build/gate)
  python3 scripts/check_lesson_integrity.py a.html b.html   # varre só os arquivos dados

Ignora arquivos *backup* e *teste* (não são servidos a aluno).
Pensado para entrar no buildCommand da Vercel: build falha => deploy não sai =>
é fisicamente impossível subir aula sem áudio.
"""
import os
import re
import sys
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIC = os.path.join(ROOT, "public")
SKIP = re.compile(r"backup|teste|test|-new-", re.I)
REF = re.compile(r"/audio/[A-Za-z0-9_./-]+\.mp3")


def _audios_versionados():
    """O DISCO NÃO É A FONTE DA VERDADE — o repositório é.

    O repo usa sparse-checkout com `!/public/audio/`: os 60 mil MP3s estão versionados
    mas NÃO materializados na árvore local (são gigabytes). Um os.path.exists() puro
    responde "não existe" para TODO áudio do projeto — e este gate, que existe para
    dizer "a aula subiu sem som", passa a gritar em cima de aula perfeitamente sonora.

    No CI o checkout é completo, então lá passava verde. Localmente acusava 51 áudios
    faltando numa aula cujos 51 MP3s estavam commitados. É falso positivo (alarme sem
    incêndio, nunca o contrário) — mas já enganou quem estava gerando aula, e alarme
    que mente é alarme que se aprende a ignorar.

    Consultamos o disco E o git: existe se estiver em qualquer um dos dois.
    """
    import subprocess
    try:
        saida = subprocess.run(["git", "ls-files", "public/audio"], cwd=ROOT,
                               capture_output=True, text=True, timeout=60).stdout
        return {l.strip() for l in saida.splitlines() if l.strip()}
    except Exception:
        return set()          # sem git: cai para o disco, comportamento antigo


_VERSIONADOS = _audios_versionados()


def audio_existe(ref):
    """ref = '/audio/slug/x.mp3'"""
    return (os.path.exists(os.path.join(PUBLIC, ref.lstrip("/")))
            or ("public" + ref) in _VERSIONADOS)


def lesson_files():
    fs = []
    for sub in ("aluno", "professor"):
        fs += sorted(glob.glob(os.path.join(PUBLIC, sub, "*.html")))
    return fs


def check(files):
    errors = []
    checked = 0
    for f in files:
        base = os.path.basename(f)
        if SKIP.search(base):
            continue
        try:
            content = open(f, encoding="utf-8").read()
        except Exception as e:
            errors.append(f"{base}: ilegível ({e})")
            continue
        checked += 1
        size = len(content)
        lines = content.count("\n")
        if size < 500 or lines < 10:
            errors.append(f"{base}: VAZIO/CORROMPIDO ({lines} linhas / {size} bytes)")
            continue
        if "</html>" not in content[-3000:]:
            errors.append(f"{base}: TRUNCADO (sem </html> no final — geração cortada)")
        miss = sorted({r for r in REF.findall(content) if not audio_existe(r)})
        if miss:
            shown = ", ".join(os.path.basename(m) for m in miss[:6])
            extra = f" (+{len(miss) - 6})" if len(miss) > 6 else ""
            errors.append(f"{base}: {len(miss)} ÁUDIO(S) FALTANDO -> {shown}{extra}")
    return checked, errors


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    files = args if args else lesson_files()
    checked, errors = check(files)
    if errors:
        print("=" * 60)
        print(f"  TRAVA DE INTEGRIDADE: {len(errors)} PROBLEMA(S) — DEPLOY BLOQUEADO")
        print("=" * 60)
        for e in errors:
            print(f"  ✗ {e}")
        print("\nNenhuma aula sobe sem áudio/íntegra. Corrija os itens acima.")
        sys.exit(1)
    print(f"✓ Integridade OK — {checked} aulas, áudio completo, sem corrupção.")
    sys.exit(0)


if __name__ == "__main__":
    main()
