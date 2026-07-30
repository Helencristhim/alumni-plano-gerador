#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Preenche os buracos historicos de `lesson_progress`: para cada aluno, marca como
concluidas todas as aulas ATE a maior que ja tem inclass_done.

Por que. O progresso e SEQUENCIAL -- quem esta na aula 15 ja teve as 14 antes. O
material do aluno sempre tratou assim (stamps e barra usam maxCompleted, decisao de
24/07/2026), mas o BANCO guardava so as aulas que a professora chegou a marcar, e os
paineis (controle-aulas, roster-status, roster_dashboard) CONTAM LINHAS. Os dois
discordavam: a Maria Claudia aparecia com 7/60 no material e "3 concluidas" no painel.

O lesson-progress.js ja nao cria buracos novos (marcar a N grava 1..N). Este script
existe para o que ficou para tras.

O que ele NAO faz:
  - nao inventa progresso: nunca vai alem da maior aula ja marcada pela professora;
  - nao apaga nem sobrescreve linha nenhuma (o upsert so manda inclass_done, entao
    `inclass_marked_at` de uma aula marcada de verdade fica intacto);
  - nao preenche linha nova com data: aula inferida NAO tem `inclass_marked_at`, e e
    assim que se distingue "foi dada e marcada" de "foi inferida".

USO:
    python3 scripts/backfill_lesson_progress.py            # dry-run (nao escreve)
    python3 scripts/backfill_lesson_progress.py --apply    # escreve no Supabase
    python3 scripts/backfill_lesson_progress.py --apply --slug maria-claudia-curimbaba
"""

import argparse
import json
import sys
import urllib.error
import urllib.request
from collections import defaultdict

URL = "https://xxdggcopydghbmgqqebq.supabase.co"
KEY = "sb_publishable_RjekGapp8WtVbDx0J8etDg_hVq7na29"
HEAD = {"apikey": KEY, "Authorization": "Bearer " + KEY, "Content-Type": "application/json"}


def get(path):
    req = urllib.request.Request(URL + path, headers=HEAD)
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())


def upsert(rows):
    body = json.dumps(rows).encode()
    h = dict(HEAD)
    h["Prefer"] = "resolution=merge-duplicates"
    req = urllib.request.Request(
        URL + "/rest/v1/lesson_progress?on_conflict=student_slug,lesson_number",
        data=body, headers=h, method="POST",
    )
    with urllib.request.urlopen(req, timeout=90) as r:
        return r.status


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="escreve de verdade (sem isso e dry-run)")
    ap.add_argument("--slug", help="restringe a um aluno")
    args = ap.parse_args()

    data = get("/rest/v1/lesson_progress?select=student_slug,lesson_number,inclass_done"
               "&inclass_done=eq.true&limit=5000")
    feitas = defaultdict(set)
    for r in data:
        feitas[r["student_slug"]].add(r["lesson_number"])

    plano = []
    for s, nums in sorted(feitas.items()):
        if args.slug and s != args.slug:
            continue
        maior = max(nums)
        faltando = sorted(set(range(1, maior + 1)) - nums)
        if faltando:
            plano.append((s, len(nums), maior, faltando))

    if not plano:
        print("nada a preencher — todo aluno ja tem 1..maior completo")
        return 0

    total = sum(len(f) for _, _, _, f in plano)
    print(f"{len(plano)} aluno(s) com buraco, {total} linha(s) a criar\n")
    for s, tem, maior, faltando in plano:
        mostra = str(faltando if len(faltando) <= 12 else faltando[:12] + ["..."])
        print(f"  {s:45} tem={tem:>3} maior={maior:>3} faltam={len(faltando):>3}  {mostra}")

    if not args.apply:
        print("\nDRY-RUN — nada foi escrito. Use --apply para gravar.")
        return 0

    print("\naplicando…")
    escritas = 0
    for s, _, _, faltando in plano:
        rows = [{"student_slug": s, "lesson_number": n, "inclass_done": True} for n in faltando]
        try:
            upsert(rows)
            escritas += len(rows)
            print(f"  ok {s}: +{len(rows)}")
        except urllib.error.HTTPError as e:
            print(f"  ERRO {s}: {e.code} {e.read()[:200]}")
            return 1
    print(f"\n{escritas} linha(s) gravada(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
