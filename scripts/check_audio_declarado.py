#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE 19 — anatomia que pede audio TEM de ter audio.

POR QUE ISTO EXISTE (07/08/2026)
--------------------------------
A aula 1 da stephanie-vicente nasceu com `audioMap` VAZIO e passou em tudo. Nenhum gate
reclamou, porque todos os que existiam faziam a pergunta seguinte:

    "o MP3 que o audioMap promete existe no disco?"   (GATE 5, check_audio_quality)

E um audioMap vazio nao promete nada. Zero promessas, zero quebradas: verde.

A pergunta que faltava e a ANTERIOR:

    "foi prometido ALGUM?"

DE ONDE VEM A EXIGENCIA — nao de opiniao, de medicao
----------------------------------------------------
Ordem do Dan (07/08/2026): "se no artefato existe necessidade de um audio ali, entao
precisamos de um gate pra incluir audio".

Medido no artefato da Stephanie (o exemplo que define a anatomia guided-discovery):

    botoes "Listen"      59
    speechSynthesis      19       say()  26       playCall  12
    .mp3                  0       audioMap  0

O artefato ESTABELECE A NECESSIDADE — 59 pontos onde a aluna ouve — e implementa com TTS
do navegador. Ele mesmo confessa na tela que so 1 das 3 vozes foi encontrada com o genero
certo. A REGRA 7 do repo resolve o outro lado: ElevenLabs, tolerancia zero com Web Speech
como metodo principal.

    A NECESSIDADE VEM DO ARTEFATO. O MOTOR VEM DO REPO.

Este gate cobra so a necessidade. Quem cobra o motor ja existe (GATE 5).

ESCOPO — anatomia, nao repo
---------------------------
So os frameworks da anatomia guided-discovery. O imersivo tem os gates dele e um piso
proprio; aula legada sem audioMap e divida do GATE 8, nao problema deste.

USO:
    python3 scripts/check_audio_declarado.py                 # repo inteiro
    python3 scripts/check_audio_declarado.py A.html B.html   # so estes
    python3 scripts/check_audio_declarado.py --selftest      # prova que morde
"""
import glob
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ANATOMIA_GD = ('reading-into-speaking', 'listening-into-interaction',
               'grammar-for-communication', 'esp-real-world')

# Piso: uma aula de 55 min em que a aluna nunca ouve nada nao e a anatomia do artefato.
# Nao e um numero pedagogico — e o minimo que separa "tem audio" de "esqueceram o audio".
MINIMO = 1


def framework_de(html):
    m = re.search(r'<meta name="alumni-framework" content="([a-z-]+)"', html)
    return m.group(1) if m else None


def entradas_do_audiomap(html):
    m = re.search(r'var audioMap\s*=\s*\{(.*?)\};', html, re.S)
    if not m:
        m = re.search(r'const audioMap\s*=\s*\{(.*?)\};', html, re.S)
    if not m:
        return None  # nao ha audioMap nenhum — outro problema, nao deste gate
    return len(re.findall(r'"[^"]+"\s*:\s*"[^"]+\.mp3', m.group(1)))


def eh_aula(p):
    return bool(re.search(r'-aula\d+\.html$', os.path.basename(p)))


def verifica(paths):
    fails, checados = [], 0
    for p in paths:
        if not eh_aula(p):
            continue
        with open(p, encoding='utf-8', errors='replace') as fh:
            h = fh.read()
        fw = framework_de(h)
        if fw not in ANATOMIA_GD:
            continue  # nao e a anatomia deste gate
        checados += 1
        n = entradas_do_audiomap(h)
        rel = os.path.relpath(p, RAIZ)
        if n is None:
            fails.append(f'{rel}: framework {fw} e NAO TEM audioMap nenhum no HTML.')
        elif n < MINIMO:
            fails.append(
                f'{rel}: framework {fw} com audioMap VAZIO. A anatomia guided-discovery pede '
                f'audio (59 botoes Listen no artefato que a define) — uma aula de 55 min em '
                f'que a aluna nunca ouve nada nao e ela. Marque as frases ouviveis com '
                f'data-speak e rode gen_audio.py.')
    return fails, checados


def selftest():
    casos = [
        ('audioMap vazio', '<meta name="alumni-framework" content="esp-real-world">'
                           '<script>var audioMap = {};</script>', True),
        ('sem audioMap',   '<meta name="alumni-framework" content="esp-real-world">', True),
        ('com audio',      '<meta name="alumni-framework" content="esp-real-world">'
                           '<script>var audioMap = {"Hi.":"/audio/x/hi.mp3"};</script>', False),
        ('imersivo vazio — nao e deste gate',
                           '<meta name="alumni-framework" content="imersivo-prototipo">'
                           '<script>var audioMap = {};</script>', False),
    ]
    import tempfile
    falhou = False
    for rotulo, html, deve_falhar in casos:
        d = tempfile.mkdtemp()
        p = os.path.join(d, 'x-aula1.html')
        with open(p, 'w', encoding='utf-8') as fh:
            fh.write(html)
        fails, _ = verifica([p])
        pegou = bool(fails)
        ok = pegou == deve_falhar
        print(f"  {'OK  ' if ok else 'FALHA'}  {rotulo}")
        falhou |= not ok
    if falhou:
        print('\nSELFTEST FALHOU — o gate parou de morder.')
        return 1
    print('\nSELFTEST OK — os 4 casos.')
    return 0


def main():
    if '--selftest' in sys.argv:
        return selftest()
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    paths = args or (glob.glob(os.path.join(RAIZ, 'public', 'professor', '*.html'))
                     + glob.glob(os.path.join(RAIZ, 'public', 'aluno', '*.html')))
    fails, checados = verifica(paths)
    print('=== GATE 19 — anatomia que pede audio tem audio ===')
    print(f'{checados} aula(s) da anatomia guided-discovery conferida(s)')
    if fails:
        for f in fails:
            print(f'  ERRO  {f}')
        return 1
    print('OK — nenhuma aula da anatomia nova sem audio.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
