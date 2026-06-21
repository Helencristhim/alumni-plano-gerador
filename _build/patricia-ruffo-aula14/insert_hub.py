#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inserção ADITIVA dos snippets da aula 14 (LACUNA) no hub prof + aluno de patricia-ruffo.
Insere ENTRE a aula 13 e a 15: cada bloco da aula 14 entra IMEDIATAMENTE APÓS o bloco
correspondente da aula 13 (accordion após ex-lesson-13; card após card-13; stamp após
stamp13; complementares após o bloco da Lesson 13).
NÃO incrementa totalLessons/TOTAL_AULAS: a lacuna já está contabilizada (hub=18, alvo final=20).
Idempotente: aborta se a aula 14 já estiver presente. Não toca aulas 1-13, 15, 17, 18."""
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
COMP   = block('-- 3b. COMPLEMENTARES da aula 14 (inserir na tab-complementary, prof E aluno) -->', '<!-- 4. ENTRADAS')
# audioMap entries: between <script> and </script>
am_i = SNIP.index('<!-- 4. ENTRADAS')
am_start = SNIP.index('<script>', am_i) + len('<script>')
am_end = SNIP.index('</script>', am_start)
AUDIO = SNIP[am_start:am_end].strip('\n')

# --- ÂNCORAS DA AULA 13 NO HUB (inserimos a 14 logo depois de cada uma) ---

# 1. STAMP: depois de stamp13
STAMP13 = ("<div class=\"stamp\" id=\"stamp13\" data-label=\"Methods Master\" "
           "style=\"background-image:url('https://images.unsplash.com/photo-1532187863486-abf9dbad1b69?w=200&q=80')\"></div>")

# 2. ACCORDION: fim do bloco ex-lesson-13 = última survival-phrase + fechamento, antes de ex-lesson-17.
#    Usamos como âncora o início do ACCORDION seguinte no DOM (ex-lesson-17) e inserimos ANTES dele.
ACCORD_NEXT = '<div class="lesson-card" id="ex-lesson-17">'

# 3. CARD IN CLASS (só prof): fim do card-13 (linha do </a> que fecha o card da aula 13).
#    Âncora = o card-13 completo (3 linhas), inserimos a 14 logo após.
CARD13_END = ('      <div><div style="font-weight:600;font-size:.95rem">Explaining Methods & Processes</div>'
              '<div style="font-size:.8rem;color:var(--text-dim)">Describing how a study was done with the passive voice: '
              'the sample was analyzed, the data were obtained -- 28 slides</div></div>\n    </a>')

# 4. COMPLEMENTARES: fim do bloco da Lesson 13 = antes do heading da Lesson 17 (próximo no DOM).
COMP_NEXT = ('<h4 style="font-family:\'Cormorant Garamond\',serif;font-size:1.2rem;margin:1.5rem 0 1rem;'
             'color:var(--accent)">Lesson 17 -- Networking at Conferences</h4>')


def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    assert 'id="ex-lesson-14"' not in s, f'{path}: aula 14 JÁ presente — abortando'

    # 1. STAMP após stamp13
    assert STAMP13 in s, f'{path}: anchor stamp13 não encontrado'
    s = s.replace(STAMP13, STAMP13 + '\n' + STAMP, 1)

    # 2. ACCORDION antes do ex-lesson-17 (= logo após o fim do ex-lesson-13)
    assert ACCORD_NEXT in s, f'{path}: anchor ex-lesson-17 não encontrado'
    s = s.replace(ACCORD_NEXT, ACCORD + '\n\n' + ACCORD_NEXT, 1)

    # 3. CARD IN CLASS (só prof — o hub aluno não tem lista de cards IN CLASS) após o card-13
    if is_prof:
        assert CARD13_END in s, f'{path}: card IN CLASS aula13 não encontrado'
        s = s.replace(CARD13_END, CARD13_END + '\n' + CARD, 1)

    # 4. COMPLEMENTARES antes do heading da Lesson 17 (= logo após o fim da Lesson 13)
    assert COMP_NEXT in s, f'{path}: heading complementares Lesson 17 não encontrado'
    s = s.replace(COMP_NEXT, COMP + '\n' + COMP_NEXT, 1)

    # 5. audioMap entries após `var audioMap = {`
    am_anchor = 'var audioMap = {'
    assert am_anchor in s, f'{path}: var audioMap não encontrado'
    s = s.replace(am_anchor, am_anchor + '\n' + AUDIO, 1)

    # 6. totalLessons / TOTAL_AULAS: NÃO mexer (lacuna já contabilizada; hub=18, alvo=20)

    open(path, 'w', encoding='utf-8').write(s)
    print(f'  patched {os.path.relpath(path, ROOT)}')


patch(os.path.join(ROOT, 'public/professor/patricia-ruffo.html'), is_prof=True)
patch(os.path.join(ROOT, 'public/aluno/patricia-ruffo.html'), is_prof=False)
print('OK')
