#!/usr/bin/env python3
"""
CONSERTA a colisão de áudio: o aluno lê uma frase e OUVE OUTRA.

O BUG
-----
O snake() do builder corta o nome do mp3 em 48 chars e NÃO é injetivo. Duas frases
distintas com o mesmo começo caem no MESMO arquivo:

    "I started my career in technology ten years ago."  ┐
    "I got my first job in 2008."                       ┘ -> aula3_i_..._goals.mp3

O aluno lê uma frase na tela e ouve a outra. Invisível para todo gate existente: o
arquivo EXISTE, e existência é tudo que eles sabem perguntar.

POR QUE REGERO TODAS AS FRASES DO GRUPO (e não só "a errada")
-------------------------------------------------------------
O mp3 que está no disco hoje foi gravado a partir de UMA das frases colididas — e
NÃO HÁ COMO SABER QUAL. O nome do arquivo é o mesmo para ambas; o conteúdo é opaco.
Se eu chutasse qual "já está certa", teria 50% de chance de deixar um aluno ouvindo
frase errada e jurar que consertei.

Então: toda frase de um grupo em colisão ganha nome NOVO (sufixo de hash, o mesmo
esquema do builder corrigido) e áudio NOVO. Custa alguns milhares de caracteres e
elimina a dúvida. O mp3 antigo fica órfão — inofensivo.

Frase SEM colisão não é tocada: nome igual, áudio igual, zero regeração.

    ELEVENLABS_API_KEY=... python3 scripts/fix_audio_collisions.py --dry
    ELEVENLABS_API_KEY=... python3 scripts/fix_audio_collisions.py
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.request

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIC = os.path.join(RAIZ, 'public')
KEY = os.environ.get('ELEVENLABS_API_KEY', '')
DRY = '--dry' in sys.argv

VOZES = {'arthur': 'sfJopaWaOtauCD3HKX6Q', 'ellen': 'BIvP0GN1cAtSRTxNHnWS'}

MAPA_RE = re.compile(r'(?:var|const|let)\s+audioMap\s*=\s*\{.*?\n\};', re.S)
PAR_RE = re.compile(r'"((?:[^"\\]|\\.)*)"\s*:\s*"([^"]+\.mp3)"')

# o speakText normaliza: ponto final / caixa / espaço extra NÃO são colisão
norm = lambda s: re.sub(r'\s+', ' ', s).strip().rstrip('.').lower()
jsun = lambda k: k.replace('\\"', '"').replace("\\'", "'").replace('\\\\', '\\')


def htmls():
    saida = subprocess.run(['git', 'ls-files', 'public/professor', 'public/aluno'],
                           cwd=RAIZ, capture_output=True, text=True).stdout
    return [os.path.join(RAIZ, l) for l in saida.split('\n') if l.endswith('.html')]


def voz_de(html, frase):
    """data-voice do elemento que fala a frase; senão REGRA 7 (1-2 palavras=arthur)."""
    esc = re.escape(frase[:40])
    m = re.search(rf'data-voice="([a-z]+)"[^>]*>[\s\S]{{0,600}}?{esc}', html)
    if m and m.group(1) in VOZES:
        return m.group(1)
    return 'arthur' if len(frase.split()) <= 2 else 'ellen'


def gerar(texto, voz, destino):
    corpo = json.dumps({'text': texto, 'model_id': 'eleven_multilingual_v2',
                        'voice_settings': {'stability': 0.5, 'similarity_boost': 0.75}}).encode()
    req = urllib.request.Request(
        f'https://api.elevenlabs.io/v1/text-to-speech/{VOZES[voz]}', data=corpo,
        headers={'xi-api-key': KEY, 'Content-Type': 'application/json', 'Accept': 'audio/mpeg'})
    with urllib.request.urlopen(req, timeout=180) as r:
        dados = r.read()
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    open(destino, 'wb').write(dados)


def main():
    if not KEY and not DRY:
        sys.exit('ELEVENLABS_API_KEY ausente. (--dry simula sem chave.)')

    # ── passo 1: descobrir as colisões e decidir o nome NOVO de cada frase.
    #    Feito GLOBALMENTE antes de escrever nada: a MESMA frase aparece no arquivo do
    #    professor E no do aluno E no hub, e os três TÊM de receber o mesmo nome novo.
    renome = {}      # (mp3_antigo, frase_normalizada) -> mp3_novo
    voz_da = {}      # frase_real -> voz
    real_de = {}     # frase_normalizada -> frase real (a que vai pra ElevenLabs)
    grupos = 0

    for caminho in htmls():
        html = open(caminho, encoding='utf-8', errors='replace').read()
        b = MAPA_RE.search(html)
        if not b:
            continue
        por_mp3 = {}
        for k, v in PAR_RE.findall(b.group(0)):
            chave = jsun(k)
            por_mp3.setdefault(v.split('?')[0], {})[norm(chave)] = chave

        for mp3, frases in por_mp3.items():
            if len(frases) < 2:
                continue                       # sem colisão: NÃO TOCA
            grupos += 1
            base = mp3[:-4]                    # tira o .mp3
            for nkey, real in frases.items():
                h = hashlib.sha1(real.encode('utf-8')).hexdigest()[:6]
                novo = f'{base}_{h}.mp3'       # mesmo esquema do builder corrigido
                renome[(mp3, nkey)] = novo
                real_de.setdefault(nkey, real)
                voz_da.setdefault(real, voz_de(html, real))

    frases_unicas = {}                          # mp3_novo -> (texto, voz)
    for (mp3, nkey), novo in renome.items():
        real = real_de[nkey]
        frases_unicas[novo] = (real, voz_da[real])

    print(f'grupos em colisão      : {grupos}')
    print(f'frases a renomear      : {len(renome)}')
    print(f'MP3s novos a gerar     : {len(frases_unicas)}')
    print(f'caracteres p/ ElevenLabs: {sum(len(t) for t, _ in frases_unicas.values())}')

    if not renome:
        print('\nNada a fazer.')
        return 0

    # ── passo 2: gerar os MP3s novos
    if not DRY:
        for i, (ref, (texto, voz)) in enumerate(sorted(frases_unicas.items()), 1):
            destino = os.path.join(PUBLIC, ref.lstrip('/'))
            if os.path.exists(destino):
                continue
            gerar(texto, voz, destino)
            if i % 25 == 0:
                print(f'  ... {i}/{len(frases_unicas)} MP3s')

    # ── passo 3: reescrever o audioMap de TODO arquivo que cite a frase
    tocados = 0
    for caminho in htmls():
        html = open(caminho, encoding='utf-8', errors='replace').read()
        b = MAPA_RE.search(html)
        if not b:
            continue

        def troca(m):
            chave, mp3 = jsun(m.group(1)), m.group(2).split('?')[0]
            novo = renome.get((mp3, norm(chave)))
            return f'"{m.group(1)}": "{novo}"' if novo else m.group(0)

        bloco = PAR_RE.sub(troca, b.group(0))
        if bloco != b.group(0):
            novo_html = html[:b.start()] + bloco + html[b.end():]
            tocados += 1
            if not DRY:
                open(caminho, 'w', encoding='utf-8').write(novo_html)

    print(f'arquivos HTML atualizados: {tocados}')
    if DRY:
        print('\n(--dry — nada gerado, nada gravado)')
    else:
        print('\nLEMBRE: git add --sparse public/audio  (o sparse-checkout ignora silenciosamente)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
