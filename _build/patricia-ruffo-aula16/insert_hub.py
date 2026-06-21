#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insercao ADITIVA dos snippets da aula 16 (LACUNA) no hub prof + aluno de patricia-ruffo.
Insere IMEDIATAMENTE APOS os blocos da aula 15 em cada secao (accordion apos ex-lesson-15;
card IN CLASS apos card-15; stamp apos stamp15; complementares apos o bloco da Lesson 15).
NAO incrementa totalLessons/TOTAL_AULAS: a lacuna ja esta contabilizada (hub=18, alvo final=20).
Idempotente: aborta se a aula 16 ja estiver presente. Nao toca aulas 1-15, 17, 18."""
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SNIP = open(os.path.join(os.path.dirname(__file__), 'hub_snippets.html'), encoding='utf-8').read()


def block(after_marker, end_marker):
    i = SNIP.index(after_marker) + len(after_marker)
    j = SNIP.index(end_marker, i)
    return SNIP[i:j].strip('\n')


CARD   = block('-- 1. CARD do menu IN CLASS (inserir na lista de cards da tab-inclass, prof e aluno c/ /aluno/) -->', '<!-- 2. STAMP')
STAMP  = block('-- 2. STAMP (inserir na stamps-row do header) -->', '<!-- 3. ACCORDION')
ACCORD = block('-- 3. ACCORDION Pre-class (inserir após o ex-lesson anterior, prof E aluno) -->', '<!-- 3b. COMPLEMENTARES')
COMP   = block('-- 3b. COMPLEMENTARES da aula 16 (inserir na tab-complementary, prof E aluno) -->', '<!-- 4. ENTRADAS')
# audioMap entries: between <script> and </script>
am_i = SNIP.index('<!-- 4. ENTRADAS')
am_start = SNIP.index('<script>', am_i) + len('<script>')
am_end = SNIP.index('</script>', am_start)
AUDIO = SNIP[am_start:am_end].strip('\n')

# --- ANCORAS DA AULA 15 NO HUB (inserimos a 16 logo depois de cada uma) ---

# 1. STAMP: depois de stamp15
STAMP15 = ("<div class=\"stamp\" id=\"stamp15\" data-label=\"Keynote Speaker\" "
           "style=\"background-image:url('https://images.unsplash.com/photo-1505373877841-8d25f7d46678?w=200&q=80')\"></div>")

# 2. ACCORDION: inserir ANTES do ex-lesson que segue ex-lesson-15 no DOM (= ex-lesson-18).
ACCORD_NEXT = '<div class="lesson-card" id="ex-lesson-18">'

# 3. CARD IN CLASS (so prof): card-15 completo (link aula15 + numero 15 + titulo), inserimos a 16 logo apos.
CARD15_END = ('      <div><div style="font-weight:600;font-size:.95rem">Review -- Conference Presentation</div>'
              '<div style="font-size:.8rem;color:var(--text-dim)">Block 3 review: structure a full conference talk, '
              'describe data, explain methods and cause-effect, and deliver under the spotlight -- 30 slides</div></div>\n    </a>')

# 4. COMPLEMENTARES: fim do bloco da Lesson 15 = antes do heading da Lesson 18 (proximo no DOM apos a Lesson 15).
COMP_NEXT = ('<h4 style="font-family:\'Cormorant Garamond\',serif;font-size:1.2rem;margin:1.5rem 0 1rem;'
             'color:var(--accent)">Lesson 18 -- Leading a Research Discussion</h4>')


def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    assert 'id="ex-lesson-16"' not in s, f'{path}: aula 16 JA presente -- abortando'

    # 1. STAMP apos stamp15
    assert STAMP15 in s, f'{path}: anchor stamp15 nao encontrado'
    s = s.replace(STAMP15, STAMP15 + '\n' + STAMP, 1)

    # 2. ACCORDION antes do ex-lesson-18 (= logo apos o fim do ex-lesson-15 no DOM)
    assert ACCORD_NEXT in s, f'{path}: anchor ex-lesson-18 nao encontrado'
    s = s.replace(ACCORD_NEXT, ACCORD + '\n\n' + ACCORD_NEXT, 1)

    # 3. CARD IN CLASS (so prof) apos o card-15
    if is_prof:
        assert CARD15_END in s, f'{path}: card IN CLASS aula15 nao encontrado'
        s = s.replace(CARD15_END, CARD15_END + '\n' + CARD, 1)

    # 4. COMPLEMENTARES antes do heading da Lesson 18 (= logo apos o fim da Lesson 15)
    assert COMP_NEXT in s, f'{path}: heading complementares Lesson 18 nao encontrado'
    s = s.replace(COMP_NEXT, COMP + '\n' + COMP_NEXT, 1)

    # 5. audioMap entries apos `var audioMap = {`
    am_anchor = 'var audioMap = {'
    assert am_anchor in s, f'{path}: var audioMap nao encontrado'
    s = s.replace(am_anchor, am_anchor + '\n' + AUDIO, 1)

    # 6. totalLessons / TOTAL_AULAS: NAO mexer (lacuna ja contabilizada; hub=18, alvo=20)

    open(path, 'w', encoding='utf-8').write(s)
    print(f'  patched {os.path.relpath(path, ROOT)}')


patch(os.path.join(ROOT, 'public/professor/patricia-ruffo.html'), is_prof=True)
patch(os.path.join(ROOT, 'public/aluno/patricia-ruffo.html'), is_prof=False)
print('OK')
