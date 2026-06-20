#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert builder-produced hub_snippets.html (aula 13) into Marlene's existing hubs.
ADDITIVE ONLY: never touches lessons 1-12. Idempotent (aborts if stamp13 already present)."""
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SNIP = open(os.path.join(os.path.dirname(__file__), 'hub_snippets.html'), encoding='utf-8').read()


def between(s, start_marker, end_marker):
    i = s.index(start_marker) + len(start_marker)
    j = s.index(end_marker, i)
    return s[i:j].strip('\n')


CARD = between(SNIP, '(inserir na lista de cards da tab-inclass, prof e aluno c/ /aluno/) -->\n',
               '\n\n<!-- 2. STAMP')
STAMP = between(SNIP, '(inserir na stamps-row do header) -->\n', '\n\n<!-- 3. ACCORDION')
ACCORDION = between(SNIP, '(inserir após o ex-lesson anterior, prof E aluno) -->\n',
                    '\n\n<!-- 3b. COMPLEMENTARES')
COMP = between(SNIP, '(inserir na tab-complementary, prof E aluno) -->\n', '\n\n<!-- 4. ENTRADAS')
AUDIO = between(SNIP, '<script>\n', '\n</script>')  # raw audioMap lines


def insert_common(c):
    assert 'id="stamp13"' not in c, 'stamp13 já presente — abortando (não duplicar)'
    # (b) stamp after stamp12
    m = re.search(r'(<div class="stamp" id="stamp12"[^>]*></div>)', c)
    c = c[:m.end()] + '\n        ' + STAMP + c[m.end():]
    # (c) ex-lesson-13 accordion right before the Celebration card
    anchor = '\n<!-- Celebration card -->'
    if anchor in c:
        i = c.index(anchor)
    else:
        i = c.index('</div><!-- /tab-exercises -->')
    c = c[:i] + '\n' + ACCORDION + '\n' + c[i:]
    # (d) complementary block before /tab-complementary
    i = c.index('</div><!-- /tab-complementary -->')
    c = c[:i] + COMP + '\n\n' + c[i:]
    # (e) audioMap entries right after `var audioMap = {`
    m = re.search(r'var audioMap = \{\n', c)
    c = c[:m.end()] + AUDIO + '\n' + c[m.end():]
    # totalLessons 12 -> 13
    c = re.sub(r'var totalLessons=12', 'var totalLessons=13', c)
    c = re.sub(r'var totalLessons = 12', 'var totalLessons = 13', c)
    return c


# ---- PROFESSOR ----
pp = os.path.join(ROOT, 'public', 'professor', 'marlene-landucci.html')
c = open(pp, encoding='utf-8').read()
c = insert_common(c)
# (a) menu card: after the aula-12 menu <a>...</a> card.
mark = 'marlene-landucci-aula12.html?autostart=1'
mi = c.index(mark)
ai = c.index('</a>', mi) + len('</a>')
c = c[:ai] + '\n' + CARD + c[ai:]
open(pp, 'w', encoding='utf-8').write(c)
print('professor: inserted (%d KB)' % (len(c) // 1024))

# ---- ALUNO ---- (no tab-inclass menu card; TOTAL_AULAS 12->13)
ap = os.path.join(ROOT, 'public', 'aluno', 'marlene-landucci.html')
c = open(ap, encoding='utf-8').read()
c = insert_common(c)
c = re.sub(r"window\.TOTAL_AULAS=12\b", 'window.TOTAL_AULAS=13', c)
open(ap, 'w', encoding='utf-8').write(c)
print('aluno: inserted (%d KB)' % (len(c) // 1024))
