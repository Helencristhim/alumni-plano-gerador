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

# ---- O ESCOPO FOI REAPONTADO E A PERGUNTA, ESTREITADA (08/09/2026)
#
# O gate media `-aulaN.html` + `<meta name="alumni-framework">`, e nenhum arquivo publicado
# carrega esse meta: rodava no CI dizendo `0 aula(s)` desde que nasceu. A anatomia que foi
# ao ar e a `consultivo` (ver `scripts/anatomia_quatro_modalidades.py`).
#
# A PERGUNTA MUDOU DE TAMANHO, e a medicao e que mandou:
#
#     modalidade    aulas   com audio
#     Reading         6         0
#     Grammar         6         1
#     Listening       6         6      <-- 2 a 10 falas cada
#     Real-World      6         4
#
# A regra original ("aula da anatomia com audioMap vazio = FALHA") reprovaria eleven das 24
# aulas publicadas, e as onze estao certas: a aula de LEITURA nao tem audio porque o texto
# e o input, e a de GRAMATICA descobre a forma no escrito. Exigir audio delas seria exigir
# que fossem outra modalidade.
#
# O que a medicao sustenta e o caso em que a falta e defeito por definicao: a aula de
# LISTENING sem uma unica fala. E o mesmo modo de falha que fez o gate nascer -- "aula da
# anatomia com audioMap vazio passava em tudo" -- agora dito onde ele e verdade.

ANATOMIA_GD = ('reading-into-speaking', 'listening-into-interaction',
               'grammar-for-communication', 'esp-real-world')

# Piso: uma aula de 55 min em que a aluna nunca ouve nada nao e a anatomia do artefato.
# Nao e um numero pedagogico — e o minimo que separa "tem audio" de "esqueceram o audio".
MINIMO = 1


from anatomia_quatro_modalidades import (  # noqa: E402
    ANATOMIA_PUBLICADA, anatomia_de, framework_de)


def entradas_do_audiomap(html):
    m = re.search(r'var audioMap\s*=\s*\{(.*?)\};', html, re.S)
    if not m:
        m = re.search(r'const audioMap\s*=\s*\{(.*?)\};', html, re.S)
    if not m:
        return None  # nao ha audioMap nenhum — outro problema, nao deste gate
    return len(re.findall(r'"[^"]+"\s*:\s*"[^"]+\.mp3', m.group(1)))


def eh_aula(p):
    return bool(re.search(r'-aula\d+\.html$', os.path.basename(p)))


MOD_QUE_EXIGE_AUDIO = "Listening"


def aulas_da_anatomia_publicada(html):
    """(numero, modalidade, tem_audio) de cada aula do ciclo.

    A modalidade esta em `LESSONS` (`mod:'Listening'`), e o audio no `AUD_MAP`, cujas
    chaves sao `#talk{n}:...` -- o numero da aula esta na propria chave. Nenhuma das duas
    e redigitada aqui."""
    mods = re.findall(r"\{n:(\d+),[^}]*?mod:'([^']*)'", html)
    m = re.search(r'var AUD_MAP=(\{.*?\});', html, re.S)
    com_audio = set()
    if m:
        com_audio = {int(x) for x in re.findall(r'"#talk(\d+):', m.group(1))}
    return [(int(n), mod, int(n) in com_audio) for n, mod in mods]


def verifica(paths):
    fails, checados = [], 0
    for p in paths:
        eh_antiga = eh_aula(p)
        with open(p, encoding='utf-8', errors='replace') as fh:
            h = fh.read()
        if not eh_antiga:
            # ---- A ANATOMIA PUBLICADA: um arquivo, o CICLO inteiro, uma modalidade por aula
            if anatomia_de(h) != ANATOMIA_PUBLICADA or os.sep + 'aluno' + os.sep in p:
                continue
            aulas = aulas_da_anatomia_publicada(h)
            if not aulas:
                continue
            checados += 1
            rel = os.path.relpath(p, RAIZ)
            for n, mod, tem in aulas:
                if mod == MOD_QUE_EXIGE_AUDIO and not tem:
                    fails.append(
                        f'{rel}: a aula {n} e {mod} e nao ha uma unica fala no AUD_MAP. '
                        f'A modalidade E a escuta -- sem audio ela nao e a aula que o '
                        f'syllabus promete. Declare as falas em talk.json e rode '
                        f'gen_audio_consultivo.py.')
            continue
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


def _ciclo(lessons, aud_map):
    """Um material da anatomia publicada: o ciclo inteiro num arquivo, `mod` por aula."""
    return (f'<meta name="alumni-anatomia" content="{ANATOMIA_PUBLICADA}">'
            f'<script>var LESSONS={{{lessons}}};var AUD_MAP={aud_map};</script>')


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

        # ---- A ANATOMIA PUBLICADA: a modalidade e que diz se a falta e defeito
        ('anatomia publicada: Listening COM fala', _ciclo(
            "{n:2,bloco:1,mod:'Listening',cod:'L1'}",
            '{"#talk2:0:2": {"src": "/audio/x/a.mp3"}}'), False),
        ('anatomia publicada: Listening SEM uma unica fala', _ciclo(
            "{n:2,bloco:1,mod:'Listening',cod:'L1'}", '{}'), True),
        ('anatomia publicada: Reading sem audio — e a modalidade, nao um esquecimento',
         _ciclo("{n:1,bloco:1,mod:'Reading',cod:'R1'}", '{}'), False),
        ('anatomia publicada: Grammar sem audio', _ciclo(
            "{n:3,bloco:1,mod:'Grammar',cod:'G1'}", '{}'), False),
        ('anatomia publicada: o audio da OUTRA aula nao conta', _ciclo(
            "{n:1,bloco:1,mod:'Reading',cod:'R1'},{n:2,bloco:1,mod:'Listening',cod:'L1'}",
            '{"#talk1:0:0": {"src": "/audio/x/a.mp3"}}'), True),
    ]
    import tempfile
    falhou = False
    for rotulo, html, deve_falhar in casos:
        d = tempfile.mkdtemp()
        p = os.path.join(d, 'x-ciclo1.html' if 'alumni-anatomia' in html
                            else 'x-aula1.html')
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
    print(f'\nSELFTEST OK — os {len(casos)} casos.')
    return 0


def main():
    if '--selftest' in sys.argv:
        return selftest()
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    paths = args or (glob.glob(os.path.join(RAIZ, 'public', 'professor', '*.html'))
                     + glob.glob(os.path.join(RAIZ, 'public', 'aluno', '*.html')))
    fails, checados = verifica(paths)
    print('=== GATE 19 — anatomia que pede audio tem audio ===')
    print(f'{checados} material(is) das quatro modalidades conferida(s)')
    if fails:
        for f in fails:
            print(f'  ERRO  {f}')
        return 1
    print('OK — nenhuma aula da anatomia nova sem audio.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
