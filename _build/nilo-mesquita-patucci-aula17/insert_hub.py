#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insere os snippets da aula 17 nos hubs prof+aluno do Nilo (aditivo, idempotente).

Replica EXATAMENTE o padrao da aula 16: card + accordion no fim da tab-exercises,
complementares no fim da tab-complementary, audioMap mesclado, stamp17 apos stamp16,
totalLessons 16 -> 17. Nao toca aulas 1-16."""
import os, re

HERE = os.path.dirname(__file__)
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SNIP = open(os.path.join(HERE, 'hub_snippets.html'), encoding='utf-8').read()

def between(s, start_marker, end_marker):
    i = s.index(start_marker) + len(start_marker)
    j = s.index(end_marker, i)
    return s[i:j].strip()

# 3. accordion (entre o comentario 3 e o 3b)
accordion = between(SNIP, '<!-- 3. ACCORDION Pre-class (inserir após o ex-lesson anterior, prof E aluno) -->',
                    '<!-- 3b. COMPLEMENTARES')
# 3b. complementares
m = re.search(r'<!-- 3b\. COMPLEMENTARES[^>]*-->(.*?)<!-- 4\. ENTRADAS de audioMap', SNIP, re.S)
comp = m.group(1).strip()
# 4. audioMap entries (linhas "k": "v",)
amap_block = between(SNIP, '<!-- 4. ENTRADAS de audioMap (mesclar no audioMap do hub, prof E aluno) -->\n<script>', '</script>')
amap_lines = [ln for ln in amap_block.splitlines() if ln.strip().startswith('"')]
amap_insert = '\n'.join(amap_lines) + '\n'

STAMP16 = '<div class="stamp" id="stamp16" data-label="Contracts" style="background-image:url(\'https://images.unsplash.com/photo-1521791055366-0d553872125f?w=200&q=80\')"></div>'
STAMP17 = '\n        <div class="stamp" id="stamp17" data-label="Renewals" style="background-image:url(\'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=200&q=80\')"></div>'

def card_for(view):
    href = f'/{view}/nilo-mesquita-patucci-aula17.html?autostart=1'
    return (f'<a href="{href}" style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s;text-decoration:none;color:inherit;margin-top:1rem" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
            f'  <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">17</div>\n'
            f'  <div><div style="font-weight:600;font-size:.95rem">Negotiation IV -- Managing the Relationship</div><div style="font-size:.8rem;color:var(--text-dim)">After signing, manage the partnership: renewals, disputes and handling a breach -- talk about consequences with the first conditional (if we renew, we will extend the term; if they default, we will escalate the dispute) -- 28 slides</div></div>\n'
            f'</a>\n')

def patch(view):
    p = os.path.join(ROOT, 'public', view, 'nilo-mesquita-patucci.html')
    s = open(p, encoding='utf-8').read()
    if 'id="ex-lesson-17"' in s:
        print(f'  {view}: já tem aula 17 — pulando'); return
    # 1. stamp 17 após stamp 16
    assert STAMP16 in s, f'{view}: stamp16 não encontrado'
    s = s.replace(STAMP16, STAMP16 + STAMP17, 1)
    # 2. accordion + card antes do fim de tab-exercises
    EX_END = '</div><!-- /tab-exercises -->'
    assert EX_END in s, f'{view}: /tab-exercises não encontrado'
    s = s.replace(EX_END, accordion + '\n\n' + card_for(view) + '\n' + EX_END, 1)
    # 3. complementares antes do fim de tab-complementary
    CO_END = '</div><!-- /tab-complementary -->'
    assert CO_END in s, f'{view}: /tab-complementary não encontrado'
    s = s.replace(CO_END, comp + '\n' + CO_END, 1)
    # 4. audioMap: inserir antes do primeiro '};' que fecha o audioMap
    am_open = s.index('var audioMap = {')
    am_close = s.index('\n};', am_open)
    s = s[:am_close + 1] + amap_insert + s[am_close + 1:]
    # 5. totalLessons 16 -> 17
    s = re.sub(r'var totalLessons=\d+', 'var totalLessons=17', s)
    open(p, 'w', encoding='utf-8').write(s)
    print(f'  {view}: inserido (stamp17, accordion ex-lesson-17, card, complementares l17, {len(amap_lines)} audioMap, totalLessons=17)')

for v in ('professor', 'aluno'):
    patch(v)
print('OK')
