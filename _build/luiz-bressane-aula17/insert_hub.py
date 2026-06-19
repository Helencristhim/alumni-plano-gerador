#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insere a aula 17 nos hubs de luiz-bressane de forma ADITIVA.
Padrao luiz: aulas 9+ vivem como standalone, linkadas do hub por
(1) stamp na stamps-row, (2) card IN CLASS (so prof), (3) complementares.
NAO ha accordion Pre-class para aulas 9+, NAO se mexe em totalLessons (=8)
nem TOTAL_AULAS (=64), NAO se adiciona audioMap (audio vive no standalone).
Idempotente: se stamp17 ja existe, aborta. Aulas 1-16 intactas."""
import os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SN = open(os.path.join(os.path.dirname(__file__), 'hub_snippets.html'), encoding='utf-8').read()


def between(a, b):
    i = SN.index(a) + len(a)
    j = SN.index(b, i)
    return SN[i:j].strip('\n')


stamp = between('<!-- 2. STAMP (inserir na stamps-row do header) -->\n', '\n<!-- 3b. COMPLEMENTARES')
comp = between('tab-complementary, prof E aluno) -->\n', '\n\n\n<!-- 4. ENTRADAS')

# Card IN CLASS no FORMATO do hub luiz (inclass-lesson-card), nao o <a> do builder.
CARD = (
    "<div class=\"inclass-lesson-card\" onclick=\"window.location.href='/professor/luiz-bressane-aula17.html?autostart=1'\" style=\"background:#fff;border:2px solid var(--accent);border-radius:12px;padding:1.5rem;cursor:pointer;transition:all .3s\">\n"
    "<div style=\"font-size:.7rem;text-transform:uppercase;letter-spacing:2px;color:var(--accent);font-weight:700;margin-bottom:.4rem\">Aula 17</div>\n"
    "<h3 style=\"font-family:'Cormorant Garamond',serif;font-size:1.3rem;color:var(--text);margin-bottom:.4rem\">The Plea Bargain</h3>\n"
    "<p style=\"font-size:.82rem;color:var(--text-dim)\">Would Rather / Would Prefer + Concession &middot; Negotiating with the Prosecution</p>\n"
    "</div>"
)


def div_end(s, start):
    depth = 0
    for m in re.finditer(r'<div\b|</div>', s[start:]):
        depth += 1 if m.group(0) == '<div' else -1
        if depth == 0:
            return start + m.end()
    raise RuntimeError('unbalanced')


def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    if 'id="stamp17"' in s:
        print(f'  SKIP {os.path.basename(path)} (aula 17 ja integrada)')
        return
    orig_len = len(s)

    # 1. stamp17 apos stamp16
    m = re.search(r'<div class="stamp" id="stamp16"[^>]*></div>', s)
    s = s[:m.end()] + '\n' + stamp + s[m.end():]

    # 2. card IN CLASS (so prof) apos o card da aula 16
    if is_prof:
        ci = s.index("luiz-bressane-aula16.html?autostart=1")
        cst = s.rfind('<div class="inclass-lesson-card"', 0, ci)
        cen = div_end(s, cst)
        s = s[:cen] + '\n' + CARD + s[cen:]

    # 3. complementares l17 apos o ultimo wrapper l16
    yi = s.index('data-media="l16-youtube"')
    wst = s.rfind('<div class="media-card-wrapper"', 0, yi)
    wen = div_end(s, wst)
    s = s[:wen] + '\n' + comp + s[wen:]

    open(path, 'w', encoding='utf-8').write(s)
    print(f'  wrote {os.path.relpath(path, ROOT)} (+{len(s)-orig_len} bytes)')


patch(os.path.join(ROOT, 'public', 'professor', 'luiz-bressane.html'), True)
patch(os.path.join(ROOT, 'public', 'aluno', 'luiz-bressane.html'), False)
print('OK')
