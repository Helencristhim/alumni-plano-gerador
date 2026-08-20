# -*- coding: utf-8 -*-
"""As frases faladas do intensivo, e de onde sai cada MP3.

REGRA 7: a fala do material e ElevenLabs, nunca a voz do sistema. O molde falava por
speechSynthesis -- serve para um artefato de laboratorio, nao para o material de uma aluna:
a voz muda em cada maquina, some no Safari e nao e a voz do curso.

Quem fala: as linhas do mapa de fala e os movimentos de reparo sao da RITA. Voz feminina
(ellen). Se um dia entrar a fala do visitante, ela vai em arthur -- o par do dialogo se
declara aqui, nao no HTML.

O nome do arquivo sai do TEXTO (slug + hash), nunca da posicao: assim, reescrever uma linha
gera um arquivo novo em vez de reaproveitar em silencio o audio do rascunho anterior.
"""
import hashlib
import html
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from content_aulas import AULAS

SLUG = 'rita-rodrigues'
VOZ_DELA = 'ellen'

def texto_puro(h):
    """O que a aluna LE na tela, sem marcacao -- e e isso que o MP3 diz."""
    t = re.sub(r'<[^>]+>', '', h)
    t = html.unescape(t)
    return ' '.join(t.split())

def para_falar(t):
    """O que a ElevenLabs recebe. Difere do da tela em um caso: o [name] do encaminhamento
    e uma lacuna que o professor preenche com a pessoa certa -- lido em voz alta viraria
    'colchete name colchete'. O audio fica com a parte que e sempre verdadeira."""
    t = re.sub(r'\s*&mdash;\s*\[name\][^.]*\.', '.', t)
    t = re.sub(r'\s*—\s*\[name\][^.]*\.', '.', t)
    t = t.replace('[Name] can provide more detail.', 'The person responsible can provide more detail.')
    return ' '.join(t.split())

def nome(t):
    s = re.sub(r'[^a-z0-9]+', '_', t.lower()).strip('_')[:52].strip('_')
    return '%s_%s.mp3' % (s, hashlib.sha1(t.encode('utf-8')).hexdigest()[:6])

def frases():
    """[(texto_na_tela, texto_falado, voz, arquivo)] -- sem repetir o que ja saiu."""
    out, visto = [], set()
    for n in sorted(AULAS):
        a = AULAS[n]
        for linha, _fn in list(a['linhas']) + list(a['apoio']):
            tela = texto_puro(linha)
            fala = para_falar(tela)
            if tela in visto:
                continue
            visto.add(tela)
            out.append((tela, fala, VOZ_DELA, nome(fala)))
    return out

# A chave e o texto FALADO, que e o que o say() recebe: quando a tela e o audio
# divergem (o [name] do encaminhamento), quem chega ao say() e o data-say.
MAPA = {fala: '/audio/%s/%s' % (SLUG, arq) for _t, fala, _v, arq in frases()}
FALA = {tela: fala for tela, fala, _v, _a in frases() if fala != tela}

if __name__ == '__main__':
    import json
    destino = os.path.join(AQUI, 'rita')
    os.makedirs(destino, exist_ok=True)
    manifesto = [{'text': fala, 'voice': voz, 'file': arq} for _t, fala, voz, arq in frases()]
    with open(os.path.join(destino, 'audio_manifest.json'), 'w', encoding='utf-8') as f:
        json.dump(manifesto, f, indent=1, ensure_ascii=False)
        f.write('\n')
    with open(os.path.join(destino, 'config.json'), 'w', encoding='utf-8') as f:
        json.dump({'slug': SLUG, 'lang': 'en',
                   'comentario': 'so o que o gen_audio.py precisa: o intensivo nao passa pelo build_from_model'},
                  f, indent=1, ensure_ascii=False)
        f.write('\n')
    print('frases:', len(manifesto))
    for m in manifesto[:4]:
        print('  %-10s %-58s %s' % (m['voice'], m['text'][:56], m['file']))
