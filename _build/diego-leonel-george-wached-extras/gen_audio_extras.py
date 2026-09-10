#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera os MP3 ElevenLabs das 3 abas suplementares do Diego e alimenta o audioMap.

POR QUE ESTE SCRIPT EXISTE
--------------------------
O `_build/model/gen_audio.py` gera audio a partir do `config.json` de UMA AULA.
As abas suplementares nao sao uma aula: nao tem slides, nem fases, nem config de
aula. Este script faz a mesma coisa para elas, com as MESMAS garantias:

* REGRA 7: todo `data-phrase` tem MP3 de verdade. Web Speech e emergencia, nunca
  o metodo principal. (Sem isto o `validate_lesson.py` reprova o hub.)
* REGRA 7 (alternancia de vozes): 1-2 palavras = SEMPRE Arthur; 3+ palavras =
  alterna Arthur/Ellen. Nunca uma voz so no material inteiro.
* REGRA 7.2 / GATE 5c: grava a PROCEDENCIA no `_src.json` -- o sha1 de
  "voz|texto" que produziu cada arquivo. Texto reescrito depois = REGENERA, em
  vez de manter para sempre o audio do rascunho anterior.
* ADITIVO: os MP3 tem prefixo proprio (xp/us/gs), que nao existe no material
  atual (que usa pc*/a*), entao nenhum arquivo existente e sobrescrito. No
  audioMap so entram CHAVES NOVAS -- nenhuma entrada existente e alterada.

MODELO: mesma escolha do gen_audio.py -- turbo_v2_5 com language_code travado
para 1-2 palavras (falta contexto para o modelo deduzir o idioma) e
multilingual_v2 para o resto. NUNCA eleven_monolingual_v1, que foi descontinuado
e devolve 400.

USO
    ELEVENLABS_API_KEY=... python3 gen_audio_extras.py [--dry-run] [--only a,b]
"""
import hashlib
import json
import os
import re
import sys
import time
import urllib.request

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, '..', '..'))
SLUG = 'diego-leonel-george-wached'
HUB = os.path.join(RAIZ, 'public', 'aluno', SLUG + '.html')
OUT = os.path.join(RAIZ, 'public', 'audio', SLUG)
LEDGER = os.path.join(OUT, '_src.json')
# (prefixo, arquivo, atributos que declaram audio, par de vozes)
#
# As TRES primeiras abas ficam EXATAMENTE como estavam -- mesmos atributos
# (data-phrase), mesmo par de vozes, mesma ordem. E o que garante que rodar este
# script de novo nao regere um unico MP3 delas.
#
# A aba EXPRESSIONS entra com duas diferencas, e as duas sao de proposito:
#   * le tambem `data-speak`, porque ali o audio da expressao e o da frase moram
#     no botao Listen do card, nao num speech-card;
#   * usa Arthur + SARAH, as duas com accent=american na ElevenLabs. A aba
#     inteira existe para ensinar como o americano fala; a Ellen, que atende o
#     resto do material, esta catalogada como accent=german.
SNIPPETS = [('xp', 'xpractice.html', ('data-phrase',), ('arthur', 'ellen')),
            ('us', 'uslife.html', ('data-phrase',), ('arthur', 'ellen')),
            ('gs', 'gospel.html', ('data-phrase',), ('arthur', 'ellen')),
            ('ae', 'expressions.html', ('data-phrase', 'data-speak'), ('arthur', 'sarah_us'))]

VOICES = json.load(open(os.path.join(RAIZ, '_build', 'model', 'voices.json'), encoding='utf-8'))
KEY = os.environ.get('ELEVENLABS_API_KEY', '')
SHORT_WORDS = 2


def _model_for(text):
    if len(text.split()) <= SHORT_WORDS:
        return 'eleven_turbo_v2_5', 'en'
    return 'eleven_multilingual_v2', None


def tts(text, voice):
    model, lang = _model_for(text)
    payload = {'text': text, 'model_id': model,
               'voice_settings': {'stability': 0.5, 'similarity_boost': 0.75,
                                  'style': 0.0, 'use_speaker_boost': True}}
    if lang:
        payload['language_code'] = lang
    req = urllib.request.Request(
        'https://api.elevenlabs.io/v1/text-to-speech/' + VOICES[voice],
        data=json.dumps(payload).encode('utf-8'),
        headers={'xi-api-key': KEY, 'Content-Type': 'application/json',
                 'Accept': 'audio/mpeg'})
    with urllib.request.urlopen(req, timeout=90) as r:
        return r.read()


def _src_hash(text, voice):
    return hashlib.sha1((voice + '|' + text).encode('utf-8')).hexdigest()


def nome(prefixo, texto):
    """Nome POSICIONAL no padrao do repo: prefixo + texto em snake_case, max 60."""
    s = re.sub(r'[^a-z0-9]+', '_', texto.lower()).strip('_')[:60].rstrip('_')
    return '%s_%s.mp3' % (prefixo, s)


def frases_dos_snippets():
    """Coleta, EM ORDEM DE TELA, todo data-phrase das abas novas.

    A ordem importa: e ela que define a alternancia de vozes, entao o resultado
    tem de ser identico a cada execucao (build reproduzivel).
    """
    achadas, vistas = [], set()
    for prefixo, arquivo, atributos, vozes in SNIPPETS:
        caminho = os.path.join(AQUI, arquivo)
        if not os.path.exists(caminho):
            continue
        html = open(caminho, encoding='utf-8').read()
        padrao = r'data-(?:%s)="([^"]+)"' % '|'.join(a.replace('data-', '') for a in atributos)
        for m in re.finditer(padrao, html):
            txt = m.group(1)
            # o HTML guarda entidades; o navegador entrega o texto ja desescapado,
            # e e ESSE texto que vira chave do audioMap.
            txt = (txt.replace('&amp;', '&').replace('&quot;', '"')
                      .replace('&lt;', '<').replace('&gt;', '>'))
            if txt in vistas:
                continue
            vistas.add(txt)
            achadas.append((prefixo, txt, vozes))
    return achadas


def main():
    dry = '--dry-run' in sys.argv
    only = None
    for a in sys.argv[1:]:
        if a.startswith('--only='):
            only = set(a.split('=', 1)[1].split(','))

    if not dry and not KEY:
        sys.exit('ERRO: ELEVENLABS_API_KEY nao definida.')

    frases = frases_dos_snippets()
    if not frases:
        sys.exit('ERRO: nenhum data-phrase encontrado nos snippets.')

    os.makedirs(OUT, exist_ok=True)
    try:
        ledger = json.load(open(LEDGER, encoding='utf-8'))
    except (IOError, ValueError):
        ledger = {}

    # REGRA 7: 1-2 palavras sempre a voz masculina; 3+ alterna o par DA ABA.
    #
    # O contador continua GLOBAL e na ordem da lista, de proposito: e o que
    # mantem cada frase ja publicada com a MESMA voz de antes. Aba nova entra
    # sempre no FIM -- assim ela nao desloca a paridade de ninguem, e o ledger
    # de procedencia (voz|texto) das abas antigas continua batendo, entao nao
    # se regera um MP3 sequer do que ja esta no ar.
    voz_longa = 0
    plano = []
    for prefixo, txt, vozes in frases:
        if len(txt.split()) <= SHORT_WORDS:
            voz = vozes[0]
        else:
            voz = vozes[0] if voz_longa % 2 == 0 else vozes[1]
            voz_longa += 1
        plano.append((nome(prefixo, txt), txt, voz))

    dupes = [n for n, _, _ in plano if [x for x, _, _ in plano].count(n) > 1]
    if dupes:
        sys.exit('ERRO: nomes de arquivo repetidos: %s' % sorted(set(dupes))[:5])

    gerar = []
    for arq, txt, voz in plano:
        caminho = os.path.join(OUT, arq)
        h = _src_hash(txt, voz)
        if only and arq not in only:
            continue
        if os.path.exists(caminho) and ledger.get(arq) == h:
            continue          # hash bate: nada mudou
        gerar.append((arq, txt, voz, h))

    chars = sum(len(t) for _, t, _, _ in gerar)
    print('frases nas abas novas : %d' % len(plano))
    print('a gerar               : %d  (%d caracteres)' % (len(gerar), chars))
    from collections import Counter
    print('vozes                 : %s'
          % ', '.join('%s %d' % (v, n) for v, n in sorted(Counter(x[2] for x in gerar).items())))

    if dry:
        for arq, txt, voz, _ in gerar[:5]:
            print('  %-52s %-6s %s' % (arq, voz, txt[:44]))
        print('--dry-run: nada gerado, nada gravado')
        return

    for i, (arq, txt, voz, h) in enumerate(gerar, 1):
        for tentativa in range(3):
            try:
                dados = tts(txt, voz)
                break
            except Exception as e:                       # noqa: BLE001
                if tentativa == 2:
                    sys.exit('ERRO em %s: %s' % (arq, e))
                time.sleep(2 * (tentativa + 1))
        with open(os.path.join(OUT, arq), 'wb') as f:
            f.write(dados)
        ledger[arq] = h
        print('  [%3d/%3d] %-6s %-46s %6d bytes' % (i, len(gerar), voz, arq[:46], len(dados)))
        with open(LEDGER, 'w', encoding='utf-8') as lf:
            json.dump(ledger, lf, indent=1, sort_keys=True, ensure_ascii=False)
            lf.write('\n')

    injeta_audiomap(plano)
    limpa_orfaos(plano)


def limpa_orfaos(plano):
    """Tira do audioMap as chaves MINHAS que o HTML nao usa mais.

    O `injeta_audiomap` so ACRESCENTA. Quando uma frase e reescrita (foi o caso
    das letras que ganharam pontuacao na 2a rodada), a chave antiga fica para
    tras apontando para o mesmo MP3 -- e como o nome do arquivo ignora
    pontuacao, duas chaves passam a apontar para o mesmo audio. O GATE 8 chama
    isso de COLISAO DE AUDIO, e com razao: e o sintoma de uma frase orfa.

    Mexe SO em entradas cujo arquivo tem prefixo xp_/us_/gs_ -- ou seja, so no
    que este script criou. O audio do material original nao e tocado.
    """
    hub = open(HUB, encoding='utf-8').read()
    # data-speak conta: na aba Expressions o audio da expressao e o da frase de
    # exemplo moram no botao Listen do card, nao num speech-card. Sem isto, as
    # chaves novas seriam apagadas como orfas no instante seguinte a insercao.
    vivas = set(re.findall(r'data-(?:phrase|speak)="([^"]+)"', hub))
    vivas |= {t.replace('&amp;', '&').replace('&quot;', '"') for t in vivas}

    ini = hub.index('var audioMap = {')
    fim = hub.index('\n};', ini)
    linhas = hub[ini:fim].split('\n')

    meus = re.compile(r'"/audio/%s/(xp|us|gs|ae)_' % re.escape(SLUG))
    mantidas, removidas = [], []
    for ln in linhas:
        m = re.match(r'\s*"((?:[^"\\]|\\.)*)":\s*("/audio/[^"]+")', ln)
        if m and meus.search(m.group(2)):
            chave = m.group(1).replace('\\"', '"')
            if chave not in vivas:
                removidas.append(chave)
                continue
        mantidas.append(ln)

    if not removidas:
        print('audioMap: nenhuma chave orfa')
    else:
        hub = hub[:ini] + '\n'.join(mantidas) + hub[fim:]
        with open(HUB, 'w', encoding='utf-8') as f:
            f.write(hub)
        print('audioMap: -%d chave(s) orfa(s) (frase reescrita na rodada nova)' % len(removidas))
        for k in removidas[:3]:
            print('    - %s' % k[:60])

    # MP3 meus que nenhuma entrada referencia mais
    hub = open(HUB, encoding='utf-8').read()
    usados = set(v.split('/')[-1] for v in re.findall(r'"(/audio/%s/[^"]+)"' % re.escape(SLUG), hub))
    try:
        ledger = json.load(open(LEDGER, encoding='utf-8'))
    except (IOError, ValueError):
        return
    sumiram = [a for a in os.listdir(OUT)
               if a.startswith(('xp_', 'us_', 'gs_', 'ae_')) and a not in usados]
    for a in sumiram:
        os.remove(os.path.join(OUT, a))
        ledger.pop(a, None)
    if sumiram:
        with open(LEDGER, 'w', encoding='utf-8') as lf:
            json.dump(ledger, lf, indent=1, sort_keys=True, ensure_ascii=False)
            lf.write('\n')
        print('disco: -%d MP3 orfao(s)' % len(sumiram))


def injeta_audiomap(plano):
    """Acrescenta SO chaves novas ao audioMap do hub. Nao altera nenhuma existente."""
    hub = open(HUB, encoding='utf-8').read()
    ini = hub.index('var audioMap = {')
    fim = hub.index('\n};', ini)
    bloco = hub[ini:fim]

    existentes = set(re.findall(r'\n  "((?:[^"\\]|\\.)*)":', bloco))
    novas = []
    for arq, txt, _ in plano:
        chave = txt.replace('\\', '\\\\').replace('"', '\\"')
        if chave in existentes:
            continue
        existentes.add(chave)
        novas.append('  "%s": "/audio/%s/%s",' % (chave, SLUG, arq))

    if not novas:
        print('audioMap ja cobria tudo, nada a inserir')
        return

    marca = '\n  // --- abas suplementares (Extra Practice / Living in the USA / Gospel / Expressions) ---\n'
    hub = hub[:fim] + marca + '\n'.join(novas) + hub[fim:]
    with open(HUB, 'w', encoding='utf-8') as f:
        f.write(hub)
    print('audioMap: +%d entradas novas (nenhuma existente alterada)' % len(novas))


if __name__ == '__main__':
    main()
