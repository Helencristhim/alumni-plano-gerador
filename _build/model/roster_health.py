#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""roster_health.py — SAÚDE DO ROSTER num relatório só.

Junta as dimensões determinísticas que os incidentes recentes exigiram, para o
sistema achar os defeitos (não a pessoa). Roda sobre os arquivos no disco.

Dimensões (por aluno):
  LINKS    : cards de Complementary ainda apontando p/ busca do YouTube
             (results?search_query) — séries deviam ser texto, YouTube vídeo real
  COMP     : Complementary fora do padrão (cards sem .media-grid / grids != aulas)
  CONTRAST : texto ESCURO sobre fundo colorido (razão WCAG < 3) — em hub e standalones
  ORDER    : exercício "Put the Story in Order" com [order-lN] órfão no audioMap

Complementa o ../audit_master.py (completude, leak, áudio, audiomap, botões,
prof=aluno, 20) — rode os dois para o quadro completo.

USO:  python3 _build/model/roster_health.py            # tabela do roster
      python3 _build/model/roster_health.py <slug>     # detalhe de um aluno
"""
import re, os, sys, glob
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
from check_contrast import scan as contrast_scan, hexs, lum  # scanner validado

JUNK = {'maisa','vanessa-maluf','zilaudio','helen-mendes','helen-mendes-teste','patricia-ruffo',
        'elaine-v-b','percival-jr','percival-jrV2','percival-jr-v2','luiz-bressane-backup-a2',
        'eduarda-gabriel-new','daniela-feitoza','maisa-de-oliveira-santos'}
UTIL = {'dashboard','index','perfil','plano','roster-status','intake','governanca','audio-audit','controle-aulas'}
SUF = re.compile(r'-(aula\d+|listening|palestra|speech-training)$')

def students():
    out = []
    for f in sorted(glob.glob(os.path.join(ROOT, 'public/aluno/*.html'))):
        s = os.path.basename(f)[:-5]
        if SUF.search(s) or s in JUNK or s in UTIL: continue
        out.append(s)
    return out

def files_of(slug):
    fs = []
    for role in ('aluno', 'professor'):
        for f in sorted(glob.glob(os.path.join(ROOT, f'public/{role}/{slug}*.html'))):
            s = os.path.basename(f)[:-5]
            if s == slug or re.match(re.escape(slug) + r'-aula\d+$', s):
                fs.append(f)
    return fs

def comp_block(h):
    i = h.find('id="tab-complementary"')
    return h[i:] if i >= 0 else ''

def check_links(h):
    c = comp_block(h)
    ser = len(re.findall(r'media-type">(?:Series|Movie|Film|Série|Filme|Serie)</div>\s*<h5>.*?results\?search_query', c, re.S))
    yt  = len(re.findall(r'media-type">(?:YouTube|TED Talk|BBC)</div>\s*<h5>.*?results\?search_query', c, re.S))
    return ser, yt

def check_comp(h):
    c = comp_block(h)
    if not c: return None
    wraps = len(re.findall(r'media-card-wrapper', c))
    grids = len(re.findall(r'class="media-grid"', c))
    if wraps == 0: return None
    if grids == 0: return 'NO-GRID'
    if grids < max(1, wraps // 4): return 'grid-parcial'
    return None

def check_order(h):
    used = set(re.findall(r"speakText\('(\[order-l\d+\])'", h))
    orphan = [k for k in used if not re.search(r'"' + re.escape(k) + r'"\s*:', h)]
    return orphan

def check_contrast_dark(path):
    # só texto ESCURO sobre cor (a direção "quebrada", tipo bug vocab-clue)
    out = []
    for cls, tc, bg, r in contrast_scan(path):
        t = hexs(tc)
        if t and lum(t) < 0.3:
            out.append((cls, tc, bg, r))
    return out

def audit(slug):
    hub = os.path.join(ROOT, 'public/aluno', slug + '.html')
    h = open(hub, encoding='utf-8').read() if os.path.exists(hub) else ''
    ser, yt = check_links(h)
    comp = check_comp(h)
    order = check_order(h)
    contrast = []
    for f in files_of(slug):
        for fnd in check_contrast_dark(f):
            contrast.append((os.path.basename(f), *fnd))
    return {'links_ser': ser, 'links_yt': yt, 'comp': comp, 'order': order, 'contrast': contrast}

def main():
    if len(sys.argv) > 1 and sys.argv[1] not in ('-v', '--verbose'):
        slug = sys.argv[1]; r = audit(slug)
        print(f"\n### {slug}")
        print(f"  LINKS    séries→busca={r['links_ser']}  youtube→busca={r['links_yt']}")
        print(f"  COMP     {r['comp'] or 'ok'}")
        print(f"  ORDER    {('órfãos: ' + ', '.join(r['order'])) if r['order'] else 'ok'}")
        if r['contrast']:
            print(f"  CONTRAST {len(r['contrast'])} achados (texto escuro sobre cor):")
            for fn, cls, tc, bg, ratio in r['contrast'][:12]:
                print(f"             {ratio:>4} {fn:38} {tc} sobre {bg} [{cls}]")
        else:
            print(f"  CONTRAST ok")
        return
    rows = []
    for s in students():
        r = audit(s)
        bad = (r['links_ser'] + r['links_yt'] > 0) or r['comp'] or r['order'] or r['contrast']
        rows.append((s, r, bool(bad)))
    print(f"\n=== ROSTER HEALTH — {len(rows)} alunos ===")
    print(f"{'aluno':40} {'LINKS':>7} {'COMP':>12} {'ORDER':>6} {'CONTR':>6}")
    tot = {'links': 0, 'comp': 0, 'order': 0, 'contrast': 0}
    for s, r, bad in rows:
        if not bad: continue
        L = r['links_ser'] + r['links_yt']
        if L: tot['links'] += 1
        if r['comp']: tot['comp'] += 1
        if r['order']: tot['order'] += 1
        if r['contrast']: tot['contrast'] += 1
        print(f"{s:40} {L if L else '·':>7} {(r['comp'] or '·'):>12} {(len(r['order']) or '·'):>6} {(len(r['contrast']) or '·'):>6}")
    clean = sum(1 for _, _, b in rows if not b)
    print(f"\n{clean}/{len(rows)} 100% OK nessas 4 dimensões.")
    print(f"alunos com: LINKS={tot['links']}  COMP={tot['comp']}  ORDER={tot['order']}  CONTRAST={tot['contrast']}")
    print("\n(completude/leak/áudio/audiomap/botões/prof=aluno/20 → rodar ../audit_master.py)")

if __name__ == '__main__':
    main()
