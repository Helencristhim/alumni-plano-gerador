#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""audio_registro.py — "este MP3 existe?" respondido num lugar so.

Os MP3 moram no Vercel Blob (ver scripts/audio_sync.mjs). O que diz que um audio existe e:

  1. o disco (o MP3 acabou de ser gerado e ainda nao subiu), ou
  2. o indice do aluno, public/audio/{slug}/_blob.json (subiu para o Blob), ou
  3. o git (`git ls-files public/audio`) — so enquanto ainda houver MP3 versionado.

Antes, cada gate perguntava ao git por conta propria (validate_lesson, check_lesson_integrity,
check_order_audio_len, check_audio_oficial). Com os MP3 fora do git essa pergunta responderia
"nao existe" para todo audio do projeto; agora todos perguntam aqui.

Os geradores usam materializar(slug) ANTES de gerar e publicar(slug) DEPOIS: eles pulam o que
ja existe no disco, e sem o MP3 local regenerariam tudo na ElevenLabs.
"""
import glob
import json
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SYNC = os.path.join(ROOT, 'scripts', 'audio_sync.mjs')

_CACHE = {}


def _indices(root):
    """{'public/audio/slug/x.mp3': bytes} de todos os _blob.json."""
    out = {}
    for p in glob.glob(os.path.join(root, 'public', 'audio', '*', '_blob.json')):
        slug = os.path.basename(os.path.dirname(p))
        try:
            idx = json.load(open(p, encoding='utf-8'))
        except (IOError, ValueError):
            continue
        for nome, meta in idx.items():
            out['public/audio/%s/%s' % (slug, nome)] = meta.get('bytes')
    return out


def _versionados(root):
    """{'public/audio/slug/x.mp3': None} do git — vazio quando nao ha MP3 versionado."""
    try:
        saida = subprocess.run(['git', 'ls-files', 'public/audio'], cwd=root,
                               capture_output=True, text=True, timeout=120).stdout
    except (OSError, subprocess.SubprocessError):
        return {}
    return {l.strip(): None for l in saida.splitlines() if l.strip().endswith('.mp3')}


def registrados(root=ROOT):
    """Todos os MP3 conhecidos fora do disco: {caminho_rel: bytes ou None}."""
    if root not in _CACHE:
        reg = _versionados(root)
        reg.update(_indices(root))
        _CACHE[root] = reg
    return _CACHE[root]


def audio_existe(ref, root=ROOT):
    """ref = '/audio/slug/x.mp3' (aceita ?v=2). Disco OU indice do Blob OU git."""
    rel = 'public/' + ref.split('?')[0].lstrip('/')
    return os.path.exists(os.path.join(root, rel)) or rel in registrados(root)


def tamanho(ref, root=ROOT):
    """Bytes do MP3: disco, senao indice do Blob, senao git. None se desconhecido."""
    rel = 'public/' + ref.split('?')[0].lstrip('/')
    fp = os.path.join(root, rel)
    if os.path.exists(fp):
        return os.path.getsize(fp)
    n = registrados(root).get(rel)
    if n is not None:
        return n
    try:
        bh = subprocess.check_output(['git', 'ls-files', '-s', rel], cwd=root,
                                     stderr=subprocess.DEVNULL).split()
        return int(subprocess.check_output(['git', 'cat-file', '-s', bh[1]], cwd=root)) if bh else None
    except (OSError, subprocess.SubprocessError, ValueError, IndexError):
        return None


def _sync(*args):
    return subprocess.run(['node', SYNC] + list(args), cwd=ROOT).returncode


def materializar(slug):
    """Traz do Blob para o disco os MP3 do aluno que faltam. Chamar ANTES de gerar."""
    if os.path.exists(os.path.join(ROOT, 'public', 'audio', slug, '_blob.json')):
        if _sync('baixar', slug) != 0:
            raise SystemExit('audio_sync baixar %s falhou: sem os MP3 locais o gerador '
                             'regeraria audio que ja existe. Abortado.' % slug)


def _pronto_para_subir():
    """Chave do Blob + pacote @vercel/blob instalado (npm install)."""
    tem_chave = bool(os.environ.get('BLOB_READ_WRITE_TOKEN')) or os.path.exists(
        os.path.expanduser('~/.config/alumni/blob.token'))
    return tem_chave and os.path.isdir(os.path.join(ROOT, 'node_modules', '@vercel', 'blob'))


def _mp3_ainda_no_git(slug):
    try:
        saida = subprocess.run(['git', 'ls-files', 'public/audio/%s' % slug], cwd=ROOT,
                               capture_output=True, text=True, timeout=60).stdout
    except (OSError, subprocess.SubprocessError):
        return False
    return any(l.endswith('.mp3') for l in saida.splitlines())


def publicar(slug):
    """Sobe para o Blob os MP3 novos do aluno e atualiza o indice. Chamar DEPOIS de gerar."""
    if not _pronto_para_subir() and _mp3_ainda_no_git(slug):
        # Transicao: enquanto os MP3 ainda vao para o git, sem chave nao ha nada a fazer
        # aqui -- o MP3 segue no commit como sempre e a virada sobe o que faltar no Blob.
        print('(Blob: sem chave ou sem `npm install` nesta maquina — MP3 segue no git como '
              'antes. Nada a fazer.)')
        return True
    if _sync('subir', slug) != 0:
        print('⛔ MP3 gerado mas NAO subiu para o Blob. Rode: node scripts/audio_sync.mjs subir %s' % slug)
        return False
    return True


def publicar_tudo():
    """Sobe todo MP3 do disco que o Blob ainda nao tem (todas as pastas de public/audio)."""
    if _sync('subir') != 0:
        print('⛔ MP3 gerado mas NAO subiu para o Blob. Rode: node scripts/audio_sync.mjs subir')
        return False
    return True
