#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""checklinks.py — confere que cada link dos Complementares abre de verdade e traz o
titulo esperado. Link de midia vai ao episodio/video EXATO (REGRA 17): se o titulo
voltar 'YouTube' puro, ou 404, o video nao existe mais e o link NAO pode ir pro ar.

USO: python3 _build/felipe-de-araujo-dias-common/checklinks.py <url> [<url> ...]
     python3 ... --files <arquivo.html> ...
"""
import json
import re
import sys
import urllib.parse
import urllib.request

UA = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/126.0 Safari/537.36')


def title_of(url):
    # YouTube devolve pagina de consentimento sem <title> util. O oembed responde
    # 200 + titulo para video PUBLICO e 404 para removido/privado — e o unico check
    # honesto de "esse video existe mesmo".
    if 'youtube.com/watch' in url or 'youtu.be/' in url:
        api = ('https://www.youtube.com/oembed?url='
               + urllib.parse.quote(url, safe='') + '&format=json')
        req = urllib.request.Request(api, headers={'User-Agent': UA})
        try:
            with urllib.request.urlopen(req, timeout=25) as r:
                data = json.loads(r.read().decode('utf-8', 'ignore'))
                return r.getcode(), f"{data.get('title', '?')} [{data.get('author_name', '?')}]"
        except Exception as e:  # noqa: BLE001
            return None, f'ERRO {e}'
    req = urllib.request.Request(url, headers={'User-Agent': UA,
                                               'Accept-Language': 'en-US,en;q=0.9'})
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            body = r.read(400000).decode('utf-8', 'ignore')
            code = r.getcode()
    except Exception as e:  # noqa: BLE001
        return None, f'ERRO {e}'
    m = re.search(r'<title>(.*?)</title>', body, re.S | re.I)
    return code, (m.group(1).strip() if m else '(sem <title>)')


def main():
    args = sys.argv[1:]
    urls = []
    if args and args[0] == '--files':
        for p in args[1:]:
            urls += re.findall(r'href="(https://[^"]+)"', open(p, encoding='utf-8').read())
    else:
        urls = args
    bad = 0
    for u in urls:
        code, t = title_of(u)
        flag = ''
        if code != 200:
            flag, bad = '  <<< FALHOU', bad + 1
        elif t.strip().lower() in ('youtube', '- youtube', 'youtube - youtube'):
            flag, bad = '  <<< VIDEO INDISPONIVEL', bad + 1
        print(f'{code} | {t[:100]:100s} | {u}{flag}')
    print(f'--- {len(urls)} link(s), {bad} problema(s)')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
