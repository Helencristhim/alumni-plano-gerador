#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""REPLACE (substitui) a aula 7 nos hubs prof + aluno do Rafael Pelizaro.
A aula 7 JA EXISTE (formato antigo, speaking). Este script TROCA o conteudo da
aula 7 (accordion Pre-class, complementares, entradas a7_/pc7_ do audioMap,
texto do card de menu IN CLASS e a linha 7 do Planejamento) pelo conteudo novo
da aula de LEITURA, gerado pelo builder em hub_snippets.html. NAO mexe nas aulas
1-6 nem 8-20. NAO altera totalLessons/stamp7 (e replace, contagem inalterada).
Idempotente o suficiente: re-rodar reaplica os mesmos blocos novos."""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SNIP = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()

NEW_MENU_DESC = 'Reading a board brief + formal connectors -- 28 slides'
OLD_MENU_DESC = 'Connectors + Formal Register -- 28 slides'
OLD_PLAN_ROW = ('<td>7</td><td>The Board Presentation -- Executive Communication</td>'
                '<td>Connectors, formal register</td>'
                '<td>5-min board presentation</td>'
                '<td>Prepare slides outline</td></tr>')
NEW_PLAN_ROW = ('<td>7</td><td>The Board Presentation -- Executive Communication</td>'
                '<td>Formal connectors and register</td>'
                '<td>Reading a board brief + True/False</td>'
                '<td>Record a 1-min board update</td></tr>')

# ---- extrair secoes do hub_snippets.html ----
ACCORDION = SNIP[SNIP.index('<div class="lesson-card" id="ex-lesson-7">'):SNIP.index('<!-- 3b.')].rstrip('\n ')
COMP = SNIP[SNIP.index('<h4', SNIP.index('<!-- 3b.')):SNIP.index('<!-- 4.')].rstrip('\n ')
_a = SNIP.index('<script>', SNIP.index('<!-- 4.')) + len('<script>')
_b = SNIP.index('</script>', _a)
AUDIO_ENTRIES = SNIP[_a:_b].strip('\n')


def match_div_end(s, start):
    depth = 0
    for m in re.finditer(r'<div\b|</div>', s[start:]):
        if m.group(0) == '</div>':
            depth -= 1
            if depth == 0:
                return start + m.end()
        else:
            depth += 1
    raise AssertionError('div nao fechou')


def replace_accordion(s):
    i = s.index('<div class="lesson-card" id="ex-lesson-7">')
    j = match_div_end(s, i)
    return s[:i] + ACCORDION + s[j:]


def replace_complementary(s):
    ci = s.index('id="tab-complementary"')
    h4 = s.index('<h4', ci)
    while 'Lesson 7 ' not in s[h4:h4 + 90]:
        h4 = s.index('<h4', h4 + 4)
    nxt = s.index('<h4', h4 + 4)  # proximo h4 (Lesson 8) ou subsequente
    return s[:h4] + COMP + '\n' + s[nxt:]


def strip_old_audio(s):
    lines = s.split('\n')
    out = [ln for ln in lines
           if '/audio/rafael-pelizaro/a7_' not in ln
           and '/audio/rafael-pelizaro/pc7_' not in ln]
    return '\n'.join(out)


def insert_audio(s):
    am = s.index('var audioMap = {')
    end = s.index('\n};', am)
    return s[:end] + '\n' + AUDIO_ENTRIES + s[end:]


def patch(path, is_prof):
    s = open(path, encoding='utf-8').read()
    assert 'id="ex-lesson-7"' in s, f'{path}: ex-lesson-7 ausente'

    # 1) card de menu IN CLASS (so prof): trocar a descricao
    if is_prof:
        assert OLD_MENU_DESC in s, f'{path}: desc do menu aula7 nao encontrada'
        s = s.replace(OLD_MENU_DESC, NEW_MENU_DESC, 1)
        # 1b) linha 7 do Planejamento
        assert OLD_PLAN_ROW in s, f'{path}: linha 7 do Planejamento nao encontrada'
        s = s.replace(OLD_PLAN_ROW, NEW_PLAN_ROW, 1)

    # 2) accordion Pre-class
    s = replace_accordion(s)
    # 3) complementares
    s = replace_complementary(s)
    # 4) audioMap: remover a7_/pc7_ antigos e inserir novos
    s = strip_old_audio(s)
    s = insert_audio(s)

    open(path, 'w', encoding='utf-8').write(s)
    print(f'  REPLACED aula 7 em {os.path.relpath(path, ROOT)}')


patch(os.path.join(ROOT, 'public', 'professor', 'rafael-pelizaro.html'), is_prof=True)
patch(os.path.join(ROOT, 'public', 'aluno', 'rafael-pelizaro.html'), is_prof=False)
print('hub REPLACE OK (aula 7 trocada; contagem inalterada)')
