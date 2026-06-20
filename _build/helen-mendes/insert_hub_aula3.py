#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""insert_hub_aula3.py — integra a AULA 3 do MODELO no hub helen-mendes (prof + aluno),
de forma 100% ADITIVA (REGRA 20 / padrão "hub SÓ ADITIVO"): NÃO toca aulas 1-2.

Insere por âncora de string:
  1. stamp3 na stamps-row do header
  2. accordion Pre-class ex-lesson-3 (após o fim do ex-lesson-2, antes de /tab-exercises)
  3. card IN CLASS aula 3 no menu (link p/ standalone) — só se ainda não houver
  4. bloco de Complementares l3- (antes de /tab-complementary)
  5. entradas pc3_ + [order-l3] no audioMap do hub (mescladas, sem duplicar)
  6. var totalLessons 2 -> 3

Idempotente: se ex-lesson-3 já existe, não reinsere.
USO: python3 _build/helen-mendes/insert_hub_aula3.py
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
PROF = os.path.join(ROOT, 'public', 'professor', 'helen-mendes.html')
ALUNO = os.path.join(ROOT, 'public', 'aluno', 'helen-mendes.html')

STAMP3 = ('<div class="stamp" id="stamp3" data-label="The Mind-Body Reset" '
          "style=\"background-image:url('https://images.unsplash.com/photo-1545205597-3d9d02c29597?w=200&q=80')\"></div>\n")

MENU_CARD = (
    '    <a href="/professor/helen-mendes-aula3.html?autostart=1" style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s;text-decoration:none;color:inherit" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
    '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">03</div>\n'
    '      <div><div style="font-weight:600;font-size:.95rem">The Mind-Body Reset</div><div style="font-size:.8rem;color:var(--text-dim)">Modals of advice + B2 reading blocks, wellness at work -- 28 slides</div></div>\n'
    '    </a>')


def read(p):
    return open(p, encoding='utf-8').read()


def write(p, s):
    open(p, 'w', encoding='utf-8').write(s)
    print(f'  wrote {os.path.relpath(p, ROOT)} ({len(s)//1024} KB)')


def amap_lines():
    am = json.load(open(os.path.join(HERE, 'audiomap_hub_aula3.json'), encoding='utf-8'))
    return [f'  {json.dumps(k, ensure_ascii=False)}: {json.dumps(v)},' for k, v in am.items()]


def insert(hub_path, preclass, complementary, is_aluno):
    s = read(hub_path)
    if 'id="ex-lesson-3"' in s:
        print(f'  ex-lesson-3 já presente em {os.path.basename(hub_path)} — pulando')
        return
    href = '/aluno/helen-mendes-aula3.html?autostart=1' if is_aluno else '/professor/helen-mendes-aula3.html?autostart=1'

    # 1. stamp3 — após stamp2 (idempotente)
    if 'id="stamp3"' not in s:
        anchor = s.index('id="stamp2"')
        end = s.index('</div>', anchor) + len('</div>') + 1
        s = s[:end] + STAMP3 + s[end:]

    # 2. accordion ex-lesson-3 — antes de </div><!-- /tab-exercises -->
    s = s.replace('</div><!-- /tab-exercises -->', '\n' + preclass.strip() + '\n\n</div><!-- /tab-exercises -->', 1)

    # 3. card IN CLASS — no menu da tab-inclass (prof tem links; aluno também).
    #    Insere após o último card do menu (antes de fechar o div de cards do menu).
    if 'helen-mendes-aula3.html' not in s.split('<!-- ========== TAB 4')[0]:
        card = MENU_CARD.replace('/professor/helen-mendes-aula3.html?autostart=1', href)
        # âncora: último </a> da lista de cards do menu IN CLASS, antes do </div></div>
        mlist = re.search(r'(IN CLASS -- Selecione a Aula.*?)(\n\s*</div>\s*</div>\s*\n\s*<!-- ========== TAB 4)', s, flags=re.S)
        if mlist:
            inject_at = mlist.start(2)
            s = s[:inject_at] + '\n' + card + s[inject_at:]

    # 4. Complementares l3- — antes de </div><!-- /tab-complementary -->
    s = s.replace('</div><!-- /tab-complementary -->', '\n' + complementary.strip() + '\n\n</div><!-- /tab-complementary -->', 1)

    # 5. audioMap: mescla pc3_/[order-l3] logo após "var audioMap = {"
    new_lines = amap_lines()
    def add_amap(m):
        existing = m.group(0)
        adds = '\n'.join(l for l in new_lines if l.split(':')[0].strip() not in existing)
        return 'var audioMap = {\n' + adds + '\n' if adds else m.group(0)
    s = re.sub(r'var audioMap = \{', add_amap, s, count=1)

    # 6. totalLessons 2 -> 3
    s = re.sub(r'var totalLessons\s*=\s*2', 'var totalLessons=3', s)

    assert 'id="ex-lesson-3"' in s and 'id="stamp3"' in s and 'data-media="l3-' in s
    assert 'roberto' not in s.lower()
    write(hub_path, s)


def main():
    pc = read(os.path.join(HERE, 'preclass-aula3.html'))
    comp = read(os.path.join(HERE, 'complementary-aula3.html'))
    print('== hub professor ==')
    insert(PROF, pc, comp, is_aluno=False)
    print('== hub aluno ==')
    insert(ALUNO, pc, comp, is_aluno=True)


if __name__ == '__main__':
    main()
