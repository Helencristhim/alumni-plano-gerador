#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fill_planning.py — monta _build/luiza-sato-eccheli/planning.html.

As aulas 1-10 descrevem o material GERADO (BLOCO1 abaixo). Da 11 em diante a tabela vem do
curriculo do Perfil 360 (~/alumni-tools/perfis/luiza-sato-eccheli.json, campo `curriculo`);
se ele ainda nao existir, sai so o bloco 1 e uma linha dizendo que o resto vem do Perfil 360.

USO: python3 _build/luiza-sato-eccheli/fill_planning.py
"""
import html
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
PERFIL = os.path.expanduser('~/alumni-tools/perfis/luiza-sato-eccheli.json')

SPEAK = 'Di&#225;logo line-by-line + 3 role-plays'
READ = 'Leitura central + gist e true/false'
BLOCO1 = [
    ('The Application Story', 'Present perfect simple e continuous para contar a trajet&#243;ria', SPEAK, 'Record your two-minute English story and bring the sentence where you stumbled'),
    ('The Treaty Is Not the Problem', 'Voz passiva em texto jur&#237;dico e institucional', READ, 'Read one article of a real treaty and list every passive verb'),
    ('Say It Once, Clearly', 'Reported speech para resumir o que algu&#233;m disse', SPEAK, 'Summarize a class discussion out loud in ninety seconds'),
    ('Who Judges a State?', 'Ora&#231;&#245;es relativas (defining, non-defining, whose)', READ, 'Explain one international court to a friend in five sentences'),
    ('A Semester Abroad', 'Condicionais 2, 3 e mistas', SPEAK, 'Record what you would do in your first week abroad'),
    ('How the TOEFL Reads You', 'Modais de dedu&#231;&#227;o no presente e no passado', READ, 'Take one timed reading section and mark every inference question'),
    ('The Tutorial Voice', 'Causativa have / get something done e sequ&#234;ncia de processo', SPEAK, 'Record a sixty-second tutorial about something you know how to do'),
    ('The Fine Print You Already Signed', 'Modais de obriga&#231;&#227;o e permiss&#227;o na linguagem jur&#237;dica', READ, 'Find three obligations in the terms of an app you use'),
    ('Forty-Five Seconds of Opinion', 'Concess&#227;o e contraste (although, whereas, despite)', SPEAK, 'Answer three opinion questions in forty-five seconds each'),
    ('The First Draft', 'Future perfect e future continuous para planos', READ, 'Outline a short essay about your exchange plans'),
]


def curto(t, n):
    """Primeira frase, sem o rotulo inicial; corta em n caracteres. Devolve HTML ja escapado."""
    t = re.sub(r'\s+', ' ', t or '').strip()
    t = re.sub(r'^Aula \d+ \u2014 ', '', t)
    t = re.sub(r'^(Grammar|Task \d+)[^:]{0,80}:\s*', '', t)
    t = re.split(r'(?<=[.;])\s| \u2014 | - ', t)[0].strip().rstrip('.')
    if len(t) > n:
        return html.escape(t[:n].rsplit(' ', 1)[0].rstrip(',;:')) + '&hellip;'
    return html.escape(t)


def main():
    rows = ['      <tr class="phase-row"><td colspan="5">Bloco 1: Funda&#231;&#245;es &#8212; a trajet&#243;ria, o direito internacional e o formato do TOEFL (Aulas 1-10)</td></tr>']
    for i, (tema, foco, ativ, hw) in enumerate(BLOCO1, 1):
        rows.append('      <tr style="background:var(--accent-dim)"><td><strong>%d</strong></td><td><strong>%s</strong></td><td>%s</td><td>%s</td><td>%s</td></tr>'
                    % (i, tema, foco, ativ, hw))
    cur = None
    if os.path.exists(PERFIL):
        cur = json.load(open(PERFIL, encoding='utf-8')).get('curriculo')
    if cur:
        bloco = 1
        for a in cur:
            n = int(a['aula'])
            if n <= 10:
                continue
            b = (n - 1) // 10 + 1
            if b != bloco:
                bloco = b
                rows.append('      <tr class="phase-row"><td colspan="5">Bloco %d (Aulas %d-%d)</td></tr>' % (b, (b - 1) * 10 + 1, b * 10))
            tema = curto(a.get('tema', ''), 80)
            foco = curto(a.get('focoLinguistico', ''), 90)
            ativ = READ if n % 2 == 0 else SPEAK
            hw = curto(a.get('homework', ''), 80)
            rows.append('      <tr><td>%d</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % (n, tema, foco, ativ, hw))
    else:
        rows.append('      <tr><td colspan="5" style="font-style:italic;color:var(--text-dim)">Aulas 11-80: temas do curr&#237;culo do Perfil 360.</td></tr>')
    tpl = open(os.path.join(HERE, 'planning.tpl.html'), encoding='utf-8').read()
    out = tpl.replace('<!--ROWS-->', '\n'.join(rows))
    open(os.path.join(HERE, 'planning.html'), 'w', encoding='utf-8').write(out)
    print('planning.html:', len(rows), 'linhas;', 'curriculo' if cur else 'sem curriculo ainda')


if __name__ == '__main__':
    main()
