#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""regen_hub.py — REGENERA (substitui) um slot de aula JA EXISTENTE no hub
monolitico de maria-claudia-curimbaba (prof + aluno), a partir do hub_snippets.html
gerado pelo build_from_model.py (modo "snippets").

Diferente de insert_hub.py (que e ADITIVO e da SKIP se o slot ja existe), este
SUBSTITUI in-place os 5 artefatos do slot N:
  1. card <a> de lancamento IN CLASS (SO no prof; aluno nao tem card)
  2. stamp do header (stampN)
  3. accordion Pre-class (ex-lesson-N)  [div balanceado]
  4. bloco Complementares da aula (h4 "Lesson/Aula N" + media-grid l{N}-*)
  5. entradas de audioMap da aula (remove as antigas aula{N}_/a{N}_/pc{N}_ e insere as novas)

NAO mexe em totalLessons / TOTAL_AULAS (regeneracao = troca de conteudo, nao de contagem).
NAO toca em nenhum outro slot. Idempotente no sentido de que rodar 2x com o mesmo
snippet produz o mesmo resultado.

USO (da raiz do worktree):
  python3 _build/maria-claudia-curimbaba-regen/regen_hub.py <N> _build/maria-claudia-curimbaba-aula<N>/hub_snippets.html
"""
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SLUG = 'maria-claudia-curimbaba'

N = int(sys.argv[1])
SNIPPET_PATH = os.path.abspath(sys.argv[2])
SN = open(SNIPPET_PATH, encoding='utf-8').read()


def between(a, b):
    i = SN.index(a) + len(a)
    j = SN.index(b, i)
    return SN[i:j].strip('\n')


card = between('prof e aluno c/ /aluno/) -->\n', '\n\n<!-- 2. STAMP').strip('\n')
stamp = between('na stamps-row do header) -->\n', '\n\n<!-- 3. ACCORDION').strip('\n')
accordion = between('prof E aluno) -->\n', '\n\n<!-- 3b. COMPLEMENTARES').strip('\n')
comp = between('tab-complementary, prof E aluno) -->\n', '\n\n<!-- 4. ENTRADAS').strip('\n')
amap_entries = between('prof E aluno) -->\n<script>\n', '</script>').strip('\n')


def div_end(s, start):
    """Indice logo APOS o </div> que fecha o <div ...> que comeca em `start`."""
    depth = 0
    for m in re.finditer(r'<div\b|</div>', s[start:]):
        depth += 1 if m.group(0) == '<div' else -1
        if depth == 0:
            return start + m.end()
    raise RuntimeError('div desbalanceado a partir de %d' % start)


def replace_stamp(s):
    pat = re.compile(r'<div class="stamp" id="stamp%d"[^>]*></div>' % N)
    m = pat.search(s)
    if not m:
        raise RuntimeError('stamp%d nao encontrado' % N)
    return s[:m.start()] + stamp + s[m.end():], 1


def replace_accordion(s):
    anchor = '<div class="lesson-card" id="ex-lesson-%d">' % N
    st = s.index(anchor)
    en = div_end(s, st)
    return s[:st] + accordion + s[en:], 1


def replace_card(s):
    """SO no prof. Mantem o <a> existente (target=_blank, estilo, onmouse) e troca
    APENAS o titulo e a descricao visiveis pelos do snippet novo (tema B2)."""
    new_title = re.search(r'font-weight:600;font-size:\.95rem">(.*?)</div>', card, re.S).group(1)
    new_desc = re.search(r'font-size:\.8rem;color:var\(--text-dim\)">(.*?)</div>', card, re.S).group(1)
    pat = re.compile(
        r'(<a href="/professor/%s-aula%d\.html\?autostart=1".*?</a>)' % (re.escape(SLUG), N),
        flags=re.S)
    m = pat.search(s)
    if not m:
        raise RuntimeError('card da aula%d nao encontrado (prof)' % N)
    block = m.group(1)
    block = re.sub(r'(font-weight:600;font-size:\.95rem">).*?(</div>)',
                   lambda mm: mm.group(1) + new_title + mm.group(2), block, count=1, flags=re.S)
    block = re.sub(r'(font-size:\.8rem;color:var\(--text-dim\)">).*?(</div>)',
                   lambda mm: mm.group(1) + new_desc + mm.group(2), block, count=1, flags=re.S)
    return s[:m.start()] + block + s[m.end():], 1


def replace_comp(s):
    """Bloco complementar da aula: do <h4>...l{N}... ate antes do proximo <h4> de aula
    (ou ate o fim da media area). Ancorado no primeiro wrapper l{N}-*."""
    mk = re.search(r'data-media="l%d-' % N, s)
    if not mk:
        raise RuntimeError('complementares l%d nao encontrados' % N)
    # h4 que precede o primeiro wrapper l{N}
    h4 = s.rfind('<h4', 0, mk.start())
    # proximo <h4 depois do ultimo wrapper l{N}
    last = None
    for m in re.finditer(r'data-media="l%d-' % N, s):
        last = m
    nxt = s.find('<h4', last.end())
    if nxt == -1:
        raise RuntimeError('nao achei delimitador final do complementar l%d' % N)
    return s[:h4] + comp + '\n\n  ' + s[nxt:], 1


def replace_audiomap(s):
    """Remove linhas de audioMap da aula N (aula{N}_, a{N}_, pc{N}_) e insere as novas
    logo apos `var audioMap = {`."""
    am = re.search(r'var audioMap\s*=\s*\{', s)
    if not am:
        raise RuntimeError('var audioMap nao encontrado')
    # remover linhas antigas do slot N (tokens de arquivo desta aula)
    tok = re.compile(r'/audio/%s/(aula%d_|a%d_|pc%d_)' % (re.escape(SLUG), N, N, N))
    lines = s.split('\n')
    kept = [ln for ln in lines if not (tok.search(ln) and '.mp3' in ln and ':' in ln)]
    removed = len(lines) - len(kept)
    s = '\n'.join(kept)
    # reinserir
    am = re.search(r'var audioMap\s*=\s*\{', s)
    s = s[:am.end()] + '\n' + amap_entries + s[am.end():]
    return s, removed


def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    orig = len(s)
    s, _ = replace_stamp(s)
    s, _ = replace_accordion(s)
    s, _ = replace_comp(s)
    if is_prof:
        s, _ = replace_card(s)
    s, removed = replace_audiomap(s)
    open(path, 'w', encoding='utf-8').write(s)
    print('  %s  (%+d bytes, %d old audioMap lines removed)'
          % (os.path.relpath(path, ROOT), len(s) - orig, removed))


patch(os.path.join(ROOT, 'public', 'professor', '%s.html' % SLUG), True)
patch(os.path.join(ROOT, 'public', 'aluno', '%s.html' % SLUG), False)
print('OK regen aula %d' % N)
