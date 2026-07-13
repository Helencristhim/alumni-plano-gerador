#!/usr/bin/env python3
"""
Costura o áudio das frases que o bug do apóstrofo deixou MUDAS.

O QUE ELE CONSERTA
------------------
O bug do escape (PR #1261/#1262) não matava só o botão. Ele cegava o extrator que
descobre QUAIS MP3s gerar — porque o extrator lia a frase ainda escapada
("Rachel&#39;s task"), enquanto em runtime o speakText recebe o texto real
("Rachel's task"). Resultado: 124 frases NUNCA entraram no audioMap e nunca
ganharam MP3, e outras ~45 entraram com chave mas apontando p/ arquivo inexistente.

O botão agora compila (PR #1261) — mas cai em TTS robótico, que a REGRA 7 proíbe.
Este script fecha o último elo: gera o MP3 na voz certa e costura a chave.

COMO ELE DECIDE A VOZ (REGRA 7)
-------------------------------
1. data-voice no elemento (diálogo) VENCE — o personagem define a voz.
2. 1-2 palavras (vocab solto)  -> ARTHUR, sempre.
3. frases (3+ palavras)        -> ALTERNA Ellen/Arthur (nunca voz única).

A CHAVE DO audioMap É O QUE O speakText RECEBE
----------------------------------------------
Não o que está escrito no arquivo. Foi essa confusão que criou o buraco. Aqui a
chave é sempre o texto DESESCAPADO, e o json.dumps cuida do escape JS.

    ELEVENLABS_API_KEY=... python3 scripts/wire_dataspeak_audio.py --dry
    ELEVENLABS_API_KEY=... python3 scripts/wire_dataspeak_audio.py
"""
import json
import os
import re
import sys
import unicodedata
import urllib.request
from html import unescape

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIC = os.path.join(RAIZ, 'public')
KEY = os.environ.get('ELEVENLABS_API_KEY', '')
DRY = '--dry' in sys.argv

VOZES = {'arthur': 'sfJopaWaOtauCD3HKX6Q', 'ellen': 'BIvP0GN1cAtSRTxNHnWS'}


def audios_no_git():
    """O DISCO NÃO É A FONTE DA VERDADE — o git é.

    O repo usa sparse-checkout com `!/public/audio/`: os 60.491 MP3s estão versionados,
    mas NÃO são materializados na árvore local (são gigabytes; ver o incidente dos
    worktrees que encheram o disco). Um os.path.exists() aqui responde "não existe"
    para TODO áudio do projeto — e um script ingênuo conclui que precisa gerar o
    catálogo inteiro. Na primeira tentativa foram 94.371 MP3s / 2,9 MILHÕES de
    caracteres pedidos à ElevenLabs. O --dry pegou.
    """
    import subprocess
    saida = subprocess.run(['git', 'ls-files', 'public/audio'], cwd=RAIZ,
                           capture_output=True, text=True, check=True).stdout
    return {linha.strip() for linha in saida.splitlines() if linha.strip()}


NO_GIT = audios_no_git()


def existe_audio(ref):
    """ref = '/audio/slug/x.mp3' -> o arquivo existe no repositório?"""
    return ('public' + ref) in NO_GIT


def snake(t):
    t = unicodedata.normalize('NFKD', t).encode('ascii', 'ignore').decode()
    t = re.sub(r'[^a-z0-9]+', '_', t.lower()).strip('_')
    return t[:60]


def parse_map(html):
    """chave EXATAMENTE COMO O JAVASCRIPT A ENXERGA -> caminho do mp3.

    NÃO desescapa entidade — e a assimetria aqui é a coisa mais importante do arquivo:

      dentro de <script>   o navegador NÃO decodifica entidades. A chave do audioMap
                           É, literalmente, `Rachel&#39;s task` — com a entidade.
      dentro de um ATRIBUTO o navegador DECODIFICA. O speakText recebe `Rachel's task`.

    As duas NUNCA casam. Foi assim que a aula ficou muda mesmo COM o MP3 no disco e
    COM a chave no mapa: o lookup falhava e caía em TTS. A prova está no nome do
    próprio arquivo gerado — `a3_rachel_39_s_task_is_data_quality.mp3`. Aquele `_39_`
    é o `&#39;` que atravessou a cadeia inteira: ele foi para o nome do arquivo E para
    o texto mandado à ElevenLabs, que portanto FALOU a entidade. O áudio não está só
    inacessível: está corrompido.

    (Escrevi este parse desescapando na primeira versão — ou seja, cometi o mesmo bug
    que vim consertar. O script então "achava" que tudo casava e não consertava nada.)

    Só se desfaz o escape de STRING JS (\\' e \\"), porque esse o motor JS realmente
    desfaz ao ler o literal.
    """
    bloco = re.search(r'(?:var|const|let)\s+audioMap\s*=\s*\{.*?\n\};', html, re.S)
    if not bloco:
        return {}, None
    out = {}
    for k, v in re.findall(r'"((?:[^"\\]|\\.)*)"\s*:\s*"([^"]+)"', bloco.group(0)):
        chave = k.replace('\\"', '"').replace("\\'", "'").replace('\\\\', '\\')
        out[chave] = v.split('?')[0]
    return out, bloco.span()


def envenenada(chave):
    """Chave que carrega entidade HTML: o JS a vê escapada, o speakText nunca a acha."""
    return bool(re.search(r'&#?\w+;', chave))


def frases(html):
    """(texto REAL, voz_sugerida|None) em ordem. data-voice na mesma linha vence."""
    out = []
    for linha in html.split('\n'):
        mv = re.search(r'data-voice="([a-z]+)"', linha)
        hint = mv.group(1) if mv else None
        for m in re.finditer(r'data-speak="([^"]*)"', linha):
            out.append((unescape(m.group(1)), hint))
        # forma legada, ainda presente em aula antiga
        for m in re.finditer(r"speakText\('((?:[^'\\]|\\.)*)'", linha):
            out.append((unescape(m.group(1).replace("\\'", "'")), hint))
    return [(t, h) for t, h in out if t and not t.startswith('[')]


def gerar(texto, voz, destino):
    corpo = json.dumps({
        'text': texto,
        'model_id': 'eleven_multilingual_v2',
        'voice_settings': {'stability': 0.5, 'similarity_boost': 0.75},
    }).encode()
    req = urllib.request.Request(
        f'https://api.elevenlabs.io/v1/text-to-speech/{VOZES[voz]}',
        data=corpo,
        headers={'xi-api-key': KEY, 'Content-Type': 'application/json', 'Accept': 'audio/mpeg'},
    )
    with urllib.request.urlopen(req, timeout=120) as r:
        dados = r.read()
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    with open(destino, 'wb') as f:
        f.write(dados)
    return len(dados)


def main():
    if not KEY and not DRY:
        sys.exit('ELEVENLABS_API_KEY ausente. (Use --dry para simular sem chave.)')

    # ESCOPO EXPLÍCITO. Sem arquivos = repo todo, e o repo todo tem buracos de áudio
    # PRÉ-EXISTENTES, alheios a este bug (zilaudio, fila da Helen, a MOCK helen-mendes).
    # Gerar áudio para eles é OUTRA decisão, com OUTRO dono. Aqui só se conserta o que
    # este bug calou.
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if args:
        alvos = args
    else:
        alvos = []
        for base, _, arqs in os.walk(PUBLIC):
            for a in arqs:
                if a.endswith('.html'):
                    alvos.append(os.path.join(base, a))

    total_gerados = total_costurados = total_chars = 0
    ja_ok = 0

    for caminho in sorted(alvos):
        html = open(caminho, encoding='utf-8').read()
        if 'data-speak=' not in html and "speakText('" not in html:
            continue
        mapa, span = parse_map(html)
        if span is None:
            continue

        # o diretório de áudio deste aluno sai do PRÓPRIO mapa (nunca adivinhado)
        base_audio = None
        for v in mapa.values():
            m = re.match(r'(/audio/[^/]+/)', v)
            if m:
                base_audio = m.group(1)
                break
        if not base_audio:
            continue
        prefixo = ''
        for v in mapa.values():
            m = re.match(r'/audio/[^/]+/([a-z0-9]+_)', v)
            if m:
                prefixo = m.group(1)
                break

        novas = {}
        alt = 0
        for texto, hint in frases(html):
            if hint:
                voz = hint if hint in VOZES else 'ellen'
            elif len(texto.split()) <= 2:
                voz = 'arthur'
            else:
                voz = 'ellen' if alt % 2 == 0 else 'arthur'
                alt += 1

            ref = mapa.get(texto) or novas.get(texto, {}).get('ref')
            if not ref:
                ref = f'{base_audio}{prefixo}{snake(texto)}.mp3'
            destino = os.path.join(PUBLIC, ref.lstrip('/'))

            existe_arquivo = existe_audio(ref)   # pergunta ao GIT, não ao disco
            tem_chave = texto in mapa

            if existe_arquivo and tem_chave:
                ja_ok += 1
                continue

            if not existe_arquivo:
                total_chars += len(texto)
                if not DRY:
                    gerar(texto, voz, destino)
                total_gerados += 1

            if not tem_chave:
                novas[texto] = {'ref': ref}
                total_costurados += 1

        if novas and not DRY:
            ini, fim = span
            bloco = html[ini:fim]
            linhas = [f'  {json.dumps(t, ensure_ascii=False)}: {json.dumps(d["ref"])},'
                      for t, d in novas.items()]
            novo_bloco = bloco[:-2].rstrip() + ('\n' if not bloco[:-2].rstrip().endswith('{') else '') \
                + '\n' + '\n'.join(linhas) + '\n};'
            html = html[:ini] + novo_bloco + html[fim:]
            open(caminho, 'w', encoding='utf-8').write(html)

        if novas:
            print(f'  {os.path.basename(caminho)}: +{len(novas)} chaves')

    print()
    print(f'frases já OK (chave + mp3)  : {ja_ok}')
    print(f'MP3s gerados                : {total_gerados}')
    print(f'chaves costuradas no audioMap: {total_costurados}')
    print(f'caracteres na ElevenLabs    : {total_chars}')
    if DRY:
        print('\n(--dry — nada foi gerado nem gravado)')


if __name__ == '__main__':
    main()
