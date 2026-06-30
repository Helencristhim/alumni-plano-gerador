#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_audio_quality.py — valida que os MP3 de uma aula NÃO estão PODRES.

O furo histórico (incidente Fabiana): gen_audio.py grava QUALQUER corpo que a
ElevenLabs devolver (rate-limit, erro JSON, corpo truncado) e o gate de
integridade do deploy só checa se o arquivo EXISTE — não se é um MP3 válido.
Resultado: áudio corrompido com arquivo presente passa batido e vai pro ar.

Este checker faz parsing puro-Python dos frames MPEG (sem ffmpeg/mutagen):
- pula tag ID3v2 se houver;
- caminha pelos frames, soma a duração real;
- REPROVA arquivo abaixo do tamanho mínimo, sem frames válidos, ou com
  duração abaixo do piso (default 0.30s — pega corpo de erro/silêncio/truncado).

USO:
  # valida tudo do manifest de uma aula:
  python3 _build/model/check_audio_quality.py _build/{slug}-aula{N}/config.json
  # ou valida um diretório/arquivos soltos:
  python3 _build/model/check_audio_quality.py public/audio/{slug}
  python3 _build/model/check_audio_quality.py a.mp3 b.mp3 ...

Saída: lista os PODRES e sai com código 1 se houver qualquer um (gate bloqueante).
Imprime, p/ cada podre, o caminho relativo — alimente o gen_audio.py --force só nesses.
"""
import json
import os
import sys

MIN_BYTES = 1200        # corpo de erro/JSON da ElevenLabs é tipicamente < 1KB
MIN_SECONDS = 0.30      # abaixo disso não é fala real (mesmo "Hi" dá > 0.4s)

_BITRATES = {  # kbps por (version_id, layer_id) -> índice; só o que a ElevenLabs usa (MPEG-1 L3)
    # MPEG-1 Layer III
    (3, 1): [0, 32, 40, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320, 0],
    # MPEG-2/2.5 Layer III
    (2, 1): [0, 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 144, 160, 0],
    (0, 1): [0, 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 144, 160, 0],
}
_SRATES = {3: [44100, 48000, 32000], 2: [22050, 24000, 16000], 0: [11025, 12000, 8000]}
_SAMPLES = {3: 1152, 2: 576, 0: 576}  # samples por frame, Layer III


def _skip_id3(b):
    if b[:3] == b'ID3' and len(b) >= 10:
        size = (b[6] << 21) | (b[7] << 14) | (b[8] << 7) | b[9]  # synchsafe
        return 10 + size
    return 0


def mp3_duration(path):
    """Retorna (duração_segundos, n_frames). (0,0) se não houver frame válido."""
    with open(path, 'rb') as f:
        b = f.read()
    i = _skip_id3(b)
    n = len(b)
    dur = 0.0
    frames = 0
    while i + 4 <= n:
        if b[i] != 0xFF or (b[i + 1] & 0xE0) != 0xE0:
            i += 1
            if frames == 0 and i > 4096:  # nenhum sync nos primeiros 4KB = lixo
                break
            continue
        ver = (b[i + 1] >> 3) & 0x3      # 3=MPEG1,2=MPEG2,0=MPEG2.5 (1=reservado)
        layer = (b[i + 1] >> 1) & 0x3    # 1 = Layer III
        bri = (b[i + 2] >> 4) & 0xF
        sri = (b[i + 2] >> 2) & 0x3
        pad = (b[i + 2] >> 1) & 0x1
        if ver == 1 or layer != 1 or bri in (0, 15) or sri == 3 or (ver, layer) not in _BITRATES:
            i += 1
            continue
        bitrate = _BITRATES[(ver, layer)][bri] * 1000
        srate = _SRATES[ver][sri]
        if bitrate == 0 or srate == 0:
            i += 1
            continue
        flen = (144 * bitrate) // srate + pad
        if flen <= 0:
            i += 1
            continue
        dur += _SAMPLES[ver] / srate
        frames += 1
        i += flen
    return dur, frames


def check(path):
    """Retorna (ok, motivo)."""
    if not os.path.exists(path):
        return False, 'arquivo ausente'
    size = os.path.getsize(path)
    if size < MIN_BYTES:
        return False, f'tamanho {size}b < {MIN_BYTES}b (provável corpo de erro)'
    dur, frames = mp3_duration(path)
    if frames == 0:
        return False, 'sem frames MPEG válidos (não é MP3)'
    if dur < MIN_SECONDS:
        return False, f'duração {dur:.2f}s < {MIN_SECONDS}s (truncado/silêncio)'
    return True, f'{dur:.1f}s, {frames} frames, {size}b'


def collect(args):
    files = []
    for a in args:
        if a.endswith('config.json'):
            cfg = json.load(open(a, encoding='utf-8'))
            mani = json.load(open(os.path.join(os.path.dirname(a), 'audio_manifest.json'), encoding='utf-8'))
            root = os.path.abspath(os.path.join(os.path.dirname(a), '..', '..'))
            out = os.path.join(root, 'public', 'audio', cfg['slug'])
            files += [os.path.join(out, m['file']) for m in mani]
        elif os.path.isdir(a):
            for fn in sorted(os.listdir(a)):
                if fn.endswith('.mp3'):
                    files.append(os.path.join(a, fn))
        else:
            files.append(a)
    return files


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    files = collect(sys.argv[1:])
    bad = []
    for fp in files:
        ok, why = check(fp)
        if not ok:
            bad.append((fp, why))
    print(f'checados: {len(files)} | PODRES: {len(bad)}')
    for fp, why in bad:
        print(f'  ! {fp}  ->  {why}')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
