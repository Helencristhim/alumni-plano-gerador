#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""serve_local.py — abre o site localmente COM os audios.

Os MP3s moram no Vercel Blob (scripts/audio_sync.mjs) e so ficam no disco quando
materializados. Um `python3 -m http.server` puro daria 404 em todo audio que nao esta no
disco. Este servidor faz o mesmo que o rewrite do vercel.json: serve public/ e, quando um
/audio/... nao existe localmente, redireciona para o Blob.

USO: python3 scripts/serve_local.py [porta]      (padrao 8000) -> http://localhost:8000/
"""
import functools
import http.server
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIC = os.path.join(ROOT, 'public')
BLOB_BASE = 'https://gbuok0mwkuvmaraz.public.blob.vercel-storage.com'  # = scripts/audio_sync.mjs


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        caminho = self.path.split('?')[0]
        if caminho.startswith('/audio/') and not os.path.exists(self.translate_path(caminho)):
            self.send_response(302)
            self.send_header('Location', BLOB_BASE + self.path)
            self.end_headers()
            return
        super().do_GET()


def main():
    porta = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    h = functools.partial(Handler, directory=PUBLIC)
    with http.server.ThreadingHTTPServer(('127.0.0.1', porta), h) as srv:
        print(f'http://localhost:{porta}/  (audio fora do disco vem do Blob)')
        srv.serve_forever()


if __name__ == '__main__':
    main()
