#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""retrofit_gap_drag.py — liga o drag and drop do gap-fill numa aula JA PUBLICADA.

Aula nova ja nasce com ele (BUILDER_GEN 3). Aula antiga so recebe quando alguem pede
AQUELE aluno (REGRA 30) — e por isso este tool existe em vez de uma varredura.

Por que nao regerar a aula pelo builder: o builder evoluiu desde que a aula foi gerada, e
a regeracao traz junto mudancas que ninguem pediu (medido em 14/09/2026 na aula 2 da
Helena Andrade: data-teacher reescrito e o marcador data-grammar sumindo). Aqui entram SO
as duas pecas do drag and drop, com as MESMAS funcoes que o builder usa:

  1. ensure_gap_drag  -> <script src="/lib/gap-drag.js"> antes de </body>
  2. apply_gap_answers -> data-answer nas .ic-blank, lido do gapfill do config
                          (["1","resposta"]; lacuna sem resposta no config fica sem)

Nao mexe no carimbo alumni-gen: a aula continua sendo da geracao em que nasceu.
Idempotente. Toca o professor E o espelho do aluno.

USO (da raiz): python3 _build/model/retrofit_gap_drag.py _build/{slug}-aula{N}/config.json [...]
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
import build_from_model as B  # noqa: E402


def respostas_do_config(cfg):
    out = {}
    for bloco in (cfg['lesson'].get('inclass_blocks') or {}).values():
        for b in bloco if isinstance(bloco, list) else []:
            if isinstance(b, dict) and b.get('kind') == 'gapfill':
                out.update(B.gapfill_respostas(b))
    return out


def main():
    cfgs = [a for a in sys.argv[1:] if not a.startswith('--')]
    if not cfgs:
        print(__doc__)
        sys.exit(2)
    for cfg_path in cfgs:
        cfg = json.load(open(cfg_path, encoding='utf-8'))
        n = cfg['lesson']['n']
        resp = respostas_do_config(cfg)
        for pasta in ('professor', 'aluno'):
            p = os.path.join(ROOT, 'public', pasta, f'{cfg["slug"]}-aula{n}.html')
            if not os.path.exists(p):
                print(f'  {os.path.relpath(p, ROOT)}: nao existe, pulado')
                continue
            s = open(p, encoding='utf-8').read()
            novo = B.ensure_gap_drag(B.apply_gap_answers(s, resp))
            if novo == s:
                print(f'  {os.path.relpath(p, ROOT)}: nada a mudar')
                continue
            open(p, 'w', encoding='utf-8').write(novo)
            print(f'  {os.path.relpath(p, ROOT)}: gap-drag ligado, {len(resp)} gabarito(s)')


if __name__ == '__main__':
    main()
