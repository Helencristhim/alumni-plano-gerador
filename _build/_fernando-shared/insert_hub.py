#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""insert_hub.py — insere os snippets (gerados pelo builder em modo hub:"snippets")
no hub existente do aluno (prof E aluno), de forma ADITIVA e determinística.

USO (da raiz do worktree):
  python3 _build/_fernando-shared/insert_hub.py _build/fernando-varela-aula{N}/hub_snippets.html {N}

Insere:
  - PROF (public/professor/fernando-varela.html):
      menu card IN CLASS + accordion Pre-class + bloco Complementares
      + entradas de audioMap + var totalLessons = N
  - ALUNO (public/aluno/fernando-varela.html):
      accordion Pre-class + bloco Complementares + entradas de audioMap
      + var totalLessons = N   (sem menu card — aluno não tem aba IN CLASS)

NÃO toca aulas anteriores. Idempotência: aborta se já houver ex-lesson-{N} no hub.
"""
import os
import re
import sys

ROOT = os.getcwd()
PROF = os.path.join(ROOT, 'public', 'professor', 'fernando-varela.html')
ALUNO = os.path.join(ROOT, 'public', 'aluno', 'fernando-varela.html')


def read(p):
    with open(p, encoding='utf-8') as f:
        return f.read()


def write(p, s):
    with open(p, 'w', encoding='utf-8') as f:
        f.write(s)


def section(snip, start_pat, end_pats):
    """Pega o texto entre o comentário start_pat e o primeiro dos end_pats."""
    m = re.search(start_pat, snip)
    if not m:
        return ''
    start = m.end()
    ends = [snip.find(e, start) for e in end_pats]
    ends = [e for e in ends if e != -1]
    end = min(ends) if ends else len(snip)
    return snip[start:end].strip('\n')


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(2)
    snip = read(os.path.abspath(sys.argv[1]))
    n = int(sys.argv[2])

    menu_card = section(snip, r'<!-- 1\. CARD[^>]*-->\n', ['<!-- 2.', '<!-- 3.'])
    accordion = section(snip, r'<!-- 3\. ACCORDION[^>]*-->\n', ['<!-- 3b.'])
    comp = section(snip, r'<!-- 3b\. COMPLEMENTARES[^>]*-->\n', ['<!-- 4.'])
    # audioMap entries: linhas entre <script>\n ... </script>
    mm = re.search(r'<!-- 4\. ENTRADAS de audioMap[^>]*-->\n<script>\n(.*?)</script>', snip, re.S)
    amap_lines = mm.group(1) if mm else ''

    assert accordion, 'accordion Pre-class não encontrado no snippet'
    assert comp, 'Complementares não encontrado no snippet'
    assert amap_lines.strip(), 'audioMap vazio no snippet'

    for path, is_prof in ((PROF, True), (ALUNO, False)):
        h = read(path)
        assert f'id="ex-lesson-{n}"' not in h, f'{path}: ex-lesson-{n} já existe — abortando (não duplicar)'

        # 1. Pre-class accordion -> antes de </div><!-- /tab-exercises -->
        anchor = '</div><!-- /tab-exercises -->'
        assert anchor in h, f'{path}: âncora tab-exercises não encontrada'
        h = h.replace(anchor, accordion + '\n\n' + anchor, 1)

        # 2. Complementares -> antes de </div><!-- /tab-complementary -->
        anchor = '</div><!-- /tab-complementary -->'
        assert anchor in h, f'{path}: âncora tab-complementary não encontrada'
        h = h.replace(anchor, comp + '\n\n' + anchor, 1)

        # 3. Menu card (só prof) -> antes do fechamento do container de cards do tab-inclass
        if is_prof and menu_card:
            anchor = '  </div>\n</div>\n\n<!-- ========== TAB 4: COMPLEMENTARES ========== -->'
            assert anchor in h, f'{path}: âncora tab-inclass não encontrada'
            h = h.replace(anchor, '    ' + menu_card.strip() + '\n' + anchor, 1)

        # 4. audioMap -> logo após "var audioMap = {"
        anchor = 'var audioMap = {'
        idx = h.find(anchor)
        assert idx != -1, f'{path}: var audioMap não encontrado'
        ins = idx + len(anchor)
        h = h[:ins] + '\n' + amap_lines.rstrip('\n') + h[ins:]

        # 5. totalLessons
        h2 = re.sub(r'var totalLessons\s*=\s*\d+\s*;', f'var totalLessons={n};', h, count=1)
        assert h2 != h, f'{path}: var totalLessons não atualizado'
        h = h2

        write(path, h)
        print(f'OK {os.path.relpath(path, ROOT)}: aula {n} inserida (card={"sim" if is_prof and menu_card else "n/a"})')


if __name__ == '__main__':
    main()
