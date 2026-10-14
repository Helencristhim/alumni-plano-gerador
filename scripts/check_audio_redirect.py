#!/usr/bin/env python3
"""
GATE A2 — o /audio sai do site por REDIRECT temporario para o Vercel Blob.

    python3 scripts/check_audio_redirect.py             # confere o vercel.json
    python3 scripts/check_audio_redirect.py --selftest  # prova que a trava morde

Por que existe (14/10/2026, PR #3267): o /audio era um REWRITE para o Blob. O cache
do site guardava a sonda do Safari (Range: bytes=0-1, resposta 206 de 2 bytes) e
devolvia esses 2 bytes para QUALQUER pedido do mesmo MP3. O audio nao tocava e a
pagina caia na voz sintetica do navegador, sem avisar ninguem. O Blob direto
responde certo. Por isso:

  1. nenhum rewrite (nem route sem status de redirect) pode atender /audio;
  2. tem que existir um redirect de /audio para o Blob com "permanent": false
     (307 — permanente o navegador do aluno memoriza e nao da para voltar atras).

Voltar o /audio para "servir pelo mesmo dominio" reabre o defeito do Safari.
"""
import json
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
BLOB_HOST = '.public.blob.vercel-storage.com'
STATUS_REDIRECT = {301, 302, 303, 307, 308}


def _eh_audio(src):
    s = (src or '').lstrip('^')
    return s == '/audio' or s.startswith('/audio/') or s.startswith('/audio(')


def checar(cfg):
    """Lista de erros (vazia = ok)."""
    erros = []
    for r in cfg.get('rewrites') or []:
        if _eh_audio(r.get('source')):
            erros.append(f"rewrite em {r.get('source')} — o /audio nao pode passar pelo cache do site "
                         "(o Safari recebe 2 bytes e a aula cai na voz robotica)")
    for r in cfg.get('routes') or []:
        if _eh_audio(r.get('src')) and r.get('status') not in STATUS_REDIRECT:
            erros.append(f"route em {r.get('src')} sem status de redirect — mesmo defeito do rewrite")

    redirs = [r for r in cfg.get('redirects') or [] if _eh_audio(r.get('source'))]
    if not redirs:
        erros.append('falta o redirect de /audio para o Vercel Blob')
    for r in redirs:
        if BLOB_HOST not in (r.get('destination') or ''):
            erros.append(f"redirect de {r.get('source')} nao aponta para o Vercel Blob ({BLOB_HOST})")
        if r.get('permanent') is not False:
            erros.append(f"redirect de {r.get('source')} precisa de \"permanent\": false "
                         "(307; o padrao da Vercel e permanente)")
    return erros


def selftest():
    blob = 'https://abc' + BLOB_HOST + '/audio/:path*'
    ok = {'redirects': [{'source': '/audio/:path*', 'destination': blob, 'permanent': False}]}
    ruins = {
        'rewrite antigo (o defeito de 14/10)': {'rewrites': [{'source': '/audio/:path*', 'destination': blob}]},
        'redirect permanente': {'redirects': [{'source': '/audio/:path*', 'destination': blob, 'permanent': True}]},
        'redirect sem permanent (padrao = permanente)': {'redirects': [{'source': '/audio/:path*', 'destination': blob}]},
        'redirect fora do Blob': {'redirects': [{'source': '/audio/:path*', 'destination': '/x/:path*', 'permanent': False}]},
        'route servindo /audio': {**ok, 'routes': [{'src': '/audio/(.*)', 'dest': blob}]},
        'sem regra de /audio': {'redirects': []},
    }
    falhas = []
    if checar(ok):
        falhas.append(f'config correta foi REPROVADA: {checar(ok)}')
    for nome, cfg in ruins.items():
        if not checar(cfg):
            falhas.append(f'config ruim PASSOU: {nome}')
    if falhas:
        for f in falhas:
            print(f'::error::SELFTEST GATE A2: {f}')
        return 1
    print(f'ok: selftest — {len(ruins)} configs ruins reprovadas, a correta aprovada')
    return 0


def main():
    if '--selftest' in sys.argv[1:]:
        return selftest()
    with open(os.path.join(ROOT, 'vercel.json'), encoding='utf-8') as f:
        erros = checar(json.load(f))
    if erros:
        for e in erros:
            print(f'::error::vercel.json: {e}')
        print('::error::Regra do audio: /audio sai por redirect 307 direto para o Blob '
              '(scripts/check_audio_redirect.py explica o porque).')
        return 1
    print('ok: /audio sai por redirect temporario para o Vercel Blob')
    return 0


if __name__ == '__main__':
    sys.exit(main())
