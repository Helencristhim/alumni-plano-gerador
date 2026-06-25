#!/usr/bin/env python3
"""Inserção ESTRITAMENTE ADITIVA da aula 19 nos hubs prof + aluno da Fabiana.
Âncoras de string inequívocas. Idempotente: aborta se a19 já existe."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SNIP = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()

def section(name_start, name_end):
    s = SNIP.index(name_start) + len(name_start)
    e = SNIP.index(name_end)
    return SNIP[s:e].strip('\n')

MENU   = section('inserir na lista de cards da tab-inclass, prof e aluno c/ /aluno/) -->', '<!-- 2. STAMP')
STAMP  = section('inserir na stamps-row do header) -->', '<!-- 3. ACCORDION')
ACCORD = section('inserir após o ex-lesson anterior, prof E aluno) -->', '<!-- 3b. COMPLEMENTARES')
COMP   = section('inserir na tab-complementary, prof E aluno) -->', '<!-- 4. ENTRADAS de audioMap')
AUDIO  = section('mesclar no audioMap do hub, prof E aluno) -->', '<!-- 5. Ajustar')
# o snippet embrulha as entradas em <script>...</script>; só as linhas de entrada entram no objeto audioMap existente
AUDIO  = AUDIO.replace('<script>', '').replace('</script>', '').strip('\n')

def insert_after(html, anchor, block):
    i = html.index(anchor) + len(anchor)
    return html[:i] + '\n' + block + html[i:]

def insert_before(html, anchor, block):
    i = html.index(anchor)
    return html[:i] + block + '\n' + html[i:]

def end_of_wrapper(html, find_from):
    """Da posição do data-media wrapper, fecha 3 </div> (media-info, media-card, wrapper)."""
    info_tip = html.index('media-tip', find_from)
    pos = html.index('</p>', info_tip)
    for _ in range(3):
        pos = html.index('</div>', pos) + len('</div>')
    return pos

def patch(path, is_prof):
    html = open(path, encoding='utf-8').read()
    if 'ex-lesson-19' in html or 'stamp19' in html:
        print(f'  SKIP {os.path.basename(path)} — aula19 já presente'); return
    orig = html

    # STAMP: após o </div> do stamp18
    a = '<div class="stamp" id="stamp18"'
    end = html.index('</div>', html.index(a)) + len('</div>')
    html = html[:end] + '\n' + STAMP + html[end:]

    # ACCORDION Pre-class: imediatamente antes do fim da tab Pre-class
    html = insert_before(html, '</div><!-- /tab-exercises -->', ACCORD)

    # COMPLEMENTARES: após o wrapper l18-youtube
    pos = end_of_wrapper(html, html.index('data-media="l18-youtube"'))
    html = html[:pos] + '\n' + COMP + html[pos:]

    # MENU IN CLASS (só prof): após o </a> do card da aula 18
    if is_prof:
        m = html.index('</a>', html.index('aula18.html?autostart=1')) + len('</a>')
        html = html[:m] + '\n    ' + MENU.strip() + html[m:]

    # audioMap: antes do fechamento '};' do bloco var audioMap
    am = html.index('var audioMap = {')
    close = html.index('\n};', am)
    html = html[:close] + '\n' + AUDIO + html[close:]

    # totalLessons 18 -> 19
    html = html.replace('var totalLessons = 18;', 'var totalLessons = 19;')

    assert html != orig and 'ex-lesson-19' in html, 'inserção falhou'
    open(path, 'w', encoding='utf-8').write(html)
    print(f'  OK {os.path.basename(path)} (+{len(html)-len(orig)} bytes)')

patch(os.path.join(ROOT, 'public/professor/fabiana-michelly-silva.html'), True)
patch(os.path.join(ROOT, 'public/aluno/fabiana-michelly-silva.html'), False)
print('done.')
