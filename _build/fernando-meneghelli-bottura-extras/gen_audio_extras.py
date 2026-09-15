#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera os MP3 ElevenLabs das abas suplementares do Fernando e alimenta o audioMap.

Mesmo contrato do `_build/diego-leonel-george-wached-extras/gen_audio_extras.py`
(REGRA 7, alternancia de vozes, procedencia no `_src.json` / GATE 5c, so chaves
novas no audioMap), com tres diferencas:

1. DOIS HUBS. As abas entram no hub do aluno e no do professor, entao o audioMap
   e alimentado (e limpo de orfas) nos dois.

2. VOZ DE SOTAQUE POR CARD. Na aba Accents cada card (`ac-voice-N`) declara a
   voz em `data-accent` no botao do monologo. TODA frase daquele card (o
   monologo e a linha de eco do speech card) sai com essa voz: o aluno repete o
   mesmo sotaque que acabou de ouvir. As vozes ficam AQUI, nao no voices.json
   global (README, "Voz de sotaque": decisao pedagogica por aluno). Vieram da
   conta compartilhada e ainda NAO foram validadas de ouvido.

3. Real-Speed English usa Arthur + Sarah, as duas accent=american: a aba existe
   para ensinar como o americano fala (a Ellen esta catalogada como german).

Prefixos wr_ / rs_ / ac_ nao existem no material dele (que usa pc* / a*), entao
nenhum MP3 existente e sobrescrito. Studyweek e Series & Films nao tem audio.

USO
    ELEVENLABS_API_KEY=... python3 gen_audio_extras.py [--dry-run] [--only=a.mp3,b.mp3]
"""
import hashlib
import json
import os
import re
import sys
import time
import urllib.request
from collections import Counter

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, '..', '..'))
SLUG = 'fernando-meneghelli-bottura'
HUBS = [os.path.join(RAIZ, 'public', v, SLUG + '.html') for v in ('aluno', 'professor')]
OUT = os.path.join(RAIZ, 'public', 'audio', SLUG)
LEDGER = os.path.join(OUT, '_src.json')
PREFIXOS = ('wr_', 'rs_', 'ac_')

# (prefixo, arquivo, atributos que declaram audio, par de vozes)
SNIPPETS = [('wr', 'wordreview.html', ('data-phrase',), ('arthur', 'ellen')),
            ('rs', 'realspeed.html', ('data-phrase', 'data-speak'), ('arthur', 'sarah_us')),
            ('ac', 'accents.html', ('data-phrase', 'data-speak'), ('arthur', 'ellen'))]

# Vozes de sotaque (conta compartilhada, conferidas pela API em 15/09/2026).
# O terceiro campo e a velocidade: o recrutador de Nova York fala mais rapido.
SOTAQUES = {
    'ny_m': ('sB7vwSCyX0tQmU24cW2C', 'Jon, american male', 1.1),
    'london_f': ('Xb7hH8MSUJpSbSDYk0k2', 'Alice, british female', None),
    'india_m': ('0fG9G8SOloOw7kMp3Ijj', 'Kumar, indian male', None),
    'sydney_f': ('IdDgBtBBVTnSVb4wDvbT', 'Samantha, australian female', None),
    'brussels_f': ('dTmTLshIypwp08eftJH6', 'Sylvie, french female', None),
    'rotterdam_m': ('SVmtrm5iuquj8zKn5ZMg', 'Will, dutch male', None),
}

VOICES = json.load(open(os.path.join(RAIZ, '_build', 'model', 'voices.json'), encoding='utf-8'))
KEY = os.environ.get('ELEVENLABS_API_KEY', '')
SHORT_WORDS = 2


def voice_id(voz):
    return SOTAQUES[voz][0] if voz in SOTAQUES else VOICES[voz]


def _model_for(text):
    if len(text.split()) <= SHORT_WORDS:
        return 'eleven_turbo_v2_5', 'en'
    return 'eleven_multilingual_v2', None


def tts(text, voz):
    model, lang = _model_for(text)
    settings = {'stability': 0.5, 'similarity_boost': 0.75, 'style': 0.0, 'use_speaker_boost': True}
    if voz in SOTAQUES and SOTAQUES[voz][2]:
        settings['speed'] = SOTAQUES[voz][2]
    payload = {'text': text, 'model_id': model, 'voice_settings': settings}
    if lang:
        payload['language_code'] = lang
    req = urllib.request.Request(
        'https://api.elevenlabs.io/v1/text-to-speech/' + voice_id(voz),
        data=json.dumps(payload).encode('utf-8'),
        headers={'xi-api-key': KEY, 'Content-Type': 'application/json', 'Accept': 'audio/mpeg'})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read()


def _src_hash(text, voz):
    return hashlib.sha1((voz + '|' + text).encode('utf-8')).hexdigest()


def nome(prefixo, texto):
    s = re.sub(r'[^a-z0-9]+', '_', texto.lower()).strip('_')[:60].rstrip('_')
    return '%s_%s.mp3' % (prefixo, s)


def _unesc(t):
    return t.replace('&amp;', '&').replace('&quot;', '"').replace('&lt;', '<').replace('&gt;', '>')


def frases_dos_snippets():
    """(prefixo, texto, par de vozes, voz fixa ou None), em ordem de tela."""
    achadas, vistas = [], set()
    for prefixo, arquivo, atributos, vozes in SNIPPETS:
        caminho = os.path.join(AQUI, arquivo)
        if not os.path.exists(caminho):
            continue
        html = open(caminho, encoding='utf-8').read()
        # Accents: recorta por card e herda o data-accent do card inteiro.
        if prefixo == 'ac':
            pedacos = re.split(r'(?=<div class="lesson-card" id="ac-voice-\d+">)', html)
        else:
            pedacos = [html]
        padrao = r'data-(?:%s)="([^"]+)"' % '|'.join(a.replace('data-', '') for a in atributos)
        for pedaco in pedacos:
            fixa = None
            if prefixo == 'ac':
                m = re.search(r'data-accent="([^"]+)"', pedaco)
                if not m:
                    continue
                fixa = m.group(1)
                if fixa not in SOTAQUES:
                    sys.exit('ERRO: data-accent desconhecido: %s' % fixa)
            for m in re.finditer(padrao, pedaco):
                txt = _unesc(m.group(1))
                if txt in vistas:
                    continue
                vistas.add(txt)
                achadas.append((prefixo, txt, vozes, fixa))
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
        sys.exit('ERRO: nenhuma frase encontrada nos snippets.')
    os.makedirs(OUT, exist_ok=True)
    try:
        ledger = json.load(open(LEDGER, encoding='utf-8'))
    except (IOError, ValueError):
        ledger = {}

    voz_longa = 0
    plano = []
    for prefixo, txt, vozes, fixa in frases:
        if fixa:
            voz = fixa
        elif len(txt.split()) <= SHORT_WORDS:
            voz = vozes[0]
        else:
            voz = vozes[0] if voz_longa % 2 == 0 else vozes[1]
            voz_longa += 1
        plano.append((nome(prefixo, txt), txt, voz))

    nomes = [n for n, _, _ in plano]
    dupes = sorted(set(n for n in nomes if nomes.count(n) > 1))
    if dupes:
        sys.exit('ERRO: nomes de arquivo repetidos: %s' % dupes[:5])

    gerar = []
    for arq, txt, voz in plano:
        h = _src_hash(txt, voz)
        if only and arq not in only:
            continue
        if os.path.exists(os.path.join(OUT, arq)) and ledger.get(arq) == h:
            continue
        gerar.append((arq, txt, voz, h))

    print('frases nas abas novas : %d' % len(plano))
    print('a gerar               : %d  (%d caracteres)' % (len(gerar), sum(len(t) for _, t, _, _ in gerar)))
    print('vozes                 : %s' % ', '.join('%s %d' % kv for kv in sorted(Counter(x[2] for x in gerar).items())))
    if dry:
        for arq, txt, voz, _ in gerar[:8]:
            print('  %-52s %-11s %s' % (arq, voz, txt[:40]))
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
        print('  [%3d/%3d] %-11s %-46s %7d bytes' % (i, len(gerar), voz, arq[:46], len(dados)))
        with open(LEDGER, 'w', encoding='utf-8') as lf:
            json.dump(ledger, lf, indent=1, sort_keys=True, ensure_ascii=False)
            lf.write('\n')

    for hub in HUBS:
        injeta_audiomap(hub, plano)
        limpa_orfaos(hub)
    limpa_mp3_orfaos()


def _bloco_audiomap(src):
    ini = src.index('var audioMap = {')
    return ini, src.index('\n};', ini)


def injeta_audiomap(hub, plano):
    src = open(hub, encoding='utf-8').read()
    if 'id="tab-wordreview"' not in src:
        sys.exit('ERRO: %s ainda nao tem as abas novas. Rode o insert_hub_extras antes.' % hub)
    ini, fim = _bloco_audiomap(src)
    existentes = set(re.findall(r'\n  "((?:[^"\\]|\\.)*)":', src[ini:fim]))
    novas = []
    for arq, txt, _ in plano:
        chave = txt.replace('\\', '\\\\').replace('"', '\\"')
        if chave in existentes:
            continue
        existentes.add(chave)
        novas.append('  "%s": "/audio/%s/%s",' % (chave, SLUG, arq))
    if not novas:
        print('%s: audioMap ja cobria tudo' % os.path.basename(os.path.dirname(hub)))
        return
    marca = '\n  // --- abas suplementares (Word Review / Real-Speed English / Accents) ---\n'
    src = src[:fim] + marca + '\n'.join(novas) + src[fim:]
    with open(hub, 'w', encoding='utf-8') as f:
        f.write(src)
    print('%s: audioMap +%d entradas (nenhuma existente alterada)'
          % (os.path.basename(os.path.dirname(hub)), len(novas)))


def limpa_orfaos(hub):
    """Tira do audioMap as chaves MINHAS (wr_/rs_/ac_) que o HTML nao usa mais."""
    src = open(hub, encoding='utf-8').read()
    vivas = set(_unesc(t) for t in re.findall(r'data-(?:phrase|speak)="([^"]+)"', src))
    ini, fim = _bloco_audiomap(src)
    meus = re.compile(r'"/audio/%s/(%s)' % (re.escape(SLUG), '|'.join(PREFIXOS)))
    mantidas, removidas = [], []
    for ln in src[ini:fim].split('\n'):
        m = re.match(r'\s*"((?:[^"\\]|\\.)*)":\s*("/audio/[^"]+")', ln)
        if m and meus.search(m.group(2)) and m.group(1).replace('\\"', '"') not in vivas:
            removidas.append(m.group(1))
            continue
        mantidas.append(ln)
    if removidas:
        src = src[:ini] + '\n'.join(mantidas) + src[fim:]
        with open(hub, 'w', encoding='utf-8') as f:
            f.write(src)
        print('%s: audioMap -%d chave(s) orfa(s)' % (os.path.basename(os.path.dirname(hub)), len(removidas)))


def limpa_mp3_orfaos():
    usados = set()
    for hub in HUBS:
        src = open(hub, encoding='utf-8').read()
        usados |= set(v.split('/')[-1] for v in re.findall(r'"(/audio/%s/[^"]+)"' % re.escape(SLUG), src))
    try:
        ledger = json.load(open(LEDGER, encoding='utf-8'))
    except (IOError, ValueError):
        return
    sumiram = [a for a in os.listdir(OUT) if a.startswith(PREFIXOS) and a not in usados]
    for a in sumiram:
        os.remove(os.path.join(OUT, a))
        ledger.pop(a, None)
    if sumiram:
        with open(LEDGER, 'w', encoding='utf-8') as lf:
            json.dump(ledger, lf, indent=1, sort_keys=True, ensure_ascii=False)
            lf.write('\n')
        print('disco: -%d MP3 orfao(s)' % len(sumiram))


if __name__ == '__main__':
    main()
