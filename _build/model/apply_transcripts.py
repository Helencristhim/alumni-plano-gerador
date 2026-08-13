#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""apply_transcripts.py — liga o Transcript accordion em aulas JA GERADAS.

Aula nova pega a feature pela chave "transcript": true no config.json — o builder injeta
sozinho. Este script e para o outro caso: o aluno ja tem as aulas geradas e a professora
pediu o transcript agora (foi o caso da Joice, aulas 4-20).

USO
  dry-run:  python3 _build/model/apply_transcripts.py joice-lopes-leite --aulas 4-20
  aplicar:  python3 _build/model/apply_transcripts.py joice-lopes-leite --aulas 4-20 --apply

O texto sai de `lesson.listenings[].text` do config de cada aula — o MESMO campo de que o
MP3 nasceu (ver transcripts.py). Aula sem config nao entra: sem fonte, sem transcript.
Idempotente: rodar duas vezes nao duplica caixa nenhuma.

REGRA 30: so passe aulas que o aluno AINDA NAO TEVE. O script nao sabe a agenda dele —
quem sabe e voce (lesson_progress no Supabase, ou a planilha de attendance).
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
import transcripts  # noqa: E402


def faixa(spec):
    out = []
    for parte in spec.split(','):
        if '-' in parte:
            a, b = parte.split('-')
            out += list(range(int(a), int(b) + 1))
        else:
            out.append(int(parte))
    return out


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    slug = argv[0]
    aplicar = '--apply' in argv
    spec = None
    for i, a in enumerate(argv):
        if a == '--aulas' and i + 1 < len(argv):
            spec = argv[i + 1]
    if not spec:
        print('!! falta --aulas (ex: --aulas 4-20)')
        return 2

    total_caixas = total_arqs = 0
    for n in faixa(spec):
        cfg_p = os.path.join(ROOT, '_build', f'{slug}-aula{n}', 'config.json')
        if not os.path.exists(cfg_p):
            print(f'  aula{n}: SEM config.json — pulada (sem fonte para o transcript)')
            continue
        with open(cfg_p, encoding='utf-8') as f:
            cfg = json.load(f)
        listenings = (cfg.get('lesson') or {}).get('listenings') or []
        if not listenings:
            print(f'  aula{n}: config sem lesson.listenings — pulada')
            continue
        for papel in ('professor', 'aluno'):
            fp = os.path.join(ROOT, 'public', papel, f'{slug}-aula{n}.html')
            if not os.path.exists(fp):
                continue
            with open(fp, encoding='utf-8') as f:
                s0 = f.read()
            s, caixas = transcripts.inject(s0, listenings)
            if caixas:
                s = transcripts.ensure_assets(s)
                s = transcripts.fix_teacher_notes(s)   # no aluno e no-op: nao ha data-teacher
            if s != s0:
                total_caixas += caixas
                total_arqs += 1
                print(f'  aula{n}/{papel}: +{caixas} caixa(s)')
                if aplicar:
                    with open(fp, 'w', encoding='utf-8') as f:
                        f.write(s)
            else:
                print(f'  aula{n}/{papel}: nada a fazer (ja tem)')
    print(f'\n{total_caixas} caixa(s) em {total_arqs} arquivo(s).'
          + ('' if aplicar else '  [DRY-RUN — use --apply para gravar]'))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
