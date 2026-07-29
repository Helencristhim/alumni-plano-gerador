#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera a tabela curricular do Planejamento a partir do curriculo do perfil 360.

Uso (da raiz do worktree):
    python3 _build/braulio-zemel-aula1/gen_table.py <aula_atual> > /tmp/table.html

Monta APENAS as linhas + cabecalho da tabela do bloco de 12 aulas que contem a
aula atual. O resto do Planejamento vem de planning_head.html / planning_tail.html.
"""
import html
import json
import re
import os
import sys

PERFIL = os.path.expanduser('~/alumni-tools/perfis/braulio-zemel.json')
atual = int(sys.argv[1]) if len(sys.argv) > 1 else 1

cur = json.load(open(PERFIL, encoding='utf-8'))['curriculo']
total = len(cur)
bloco_ini = ((atual - 1) // 12) * 12 + 1
bloco_fim = min(bloco_ini + 11, total)


def esc(s):
    return html.escape(str(s or ''), quote=False)


def resumo(txt, limite=190):
    """A tabela do Planejamento e um PANORAMA: o foco completo do curriculo tem
    600+ caracteres por aula e transformaria a tabela num muro de texto. Aqui fica
    a primeira ideia (ate o 1o ponto) cortada em `limite`; o texto integral vive no
    perfil 360, que e onde o professor le com calma."""
    t = re.sub(r'\s+', ' ', str(txt or '')).strip()
    t = re.sub(r'^(?:Grammar|Gram\u00e1tica)[^:]{0,60}:\s*', '', t)
    # o curriculo escreve a atividade como 'Phase 1 (10 min) - Warm-up: ...';
    # o rotulo da fase nao informa nada numa tabela de panorama.
    t = re.sub(r'^Phase\s*\d+\s*\([^)]*\)\s*[\u2014\u2013-]\s*[^:]{0,30}:\s*', '', t)
    corte = t.split('. ')[0]
    if len(corte) > limite:
        corte = corte[:limite].rsplit(' ', 1)[0] + '...'
    return esc(corte.rstrip('.') + '.')


print(f'\n  <h4 style="font-family:\'Cormorant Garamond\',serif;font-size:1.2rem;margin-bottom:1rem">'
      f'Curr&#237;culo &mdash; Bloco {(bloco_ini - 1) // 12 + 1} (Aulas {bloco_ini}-{bloco_fim} de {total})</h4>')
print('  <div style="overflow-x:auto">')
print('    <table style="width:100%;border-collapse:collapse;font-size:.82rem;background:var(--bg-card);'
      'border:1px solid var(--border);border-radius:8px;overflow:hidden">')
print('      <thead><tr style="background:var(--accent);color:#fff">'
      '<th style="padding:.6rem;text-align:left">#</th>'
      '<th style="padding:.6rem;text-align:left">Tema</th>'
      '<th style="padding:.6rem;text-align:left">Foco Lingu&#237;stico</th>'
      '<th style="padding:.6rem;text-align:left">Atividade Principal</th>'
      '<th style="padding:.6rem;text-align:left">Status</th></tr></thead>')
print('      <tbody>')
for t in cur[bloco_ini - 1:bloco_fim]:
    n = t.get('aula')
    zebra = ';background:var(--bg-elevated)' if n % 2 == 1 and n != atual else ''
    if n == atual:
        tr = 'style="border-bottom:1px solid var(--border);background:var(--accent-dim)"'
        num = f'<td style="padding:.5rem;font-weight:700">{n}</td>'
        status = '<td style="padding:.5rem;font-weight:700;color:var(--accent)">Atual</td>'
    else:
        tr = f'style="border-bottom:1px solid var(--border){zebra}"'
        num = f'<td style="padding:.5rem">{n}</td>'
        rot = 'Publicada' if n < atual else 'Pr&#243;xima'
        cor = 'color:var(--success)' if n < atual else 'color:var(--text-dim)'
        status = f'<td style="padding:.5rem;{cor}">{rot}</td>'
    modelo = 'leitura' if n % 2 == 0 else 'fala'
    print(f'        <tr {tr}>{num}'
          f'<td style="padding:.5rem">{esc(t.get("tema"))}</td>'
          f'<td style="padding:.5rem">{resumo(t.get("focoLinguistico"))}</td>'
          f'<td style="padding:.5rem">{resumo(t.get("atividadeEmAula") or t.get("atividadePrincipal"), 150)} '
          f'<em style="color:var(--text-dim)">({modelo})</em></td>'
          f'{status}</tr>')
print('      </tbody>')
print('    </table>')
print('  </div>')
print(f'  <p style="font-size:.78rem;color:var(--text-dim);margin-top:.6rem;font-style:italic">'
      f'Programa de <strong>{total} aulas</strong>. A gera&#231;&#227;o alterna os dois formatos por n&#250;mero de aula: '
      f'aula <strong>&#237;mpar</strong> gira em torno de <strong>di&#225;logo e role-play</strong>, aula '
      f'<strong>par</strong> em torno de um <strong>texto autêntico</strong> com gist e true/false &mdash; '
      f'atendendo ao pedido do aluno por um texto por aula sem transformar o curso inteiro em leitura. '
      f'Cada aula acrescenta 12 expressões novas, e nenhuma expressão volta como conte&#250;do novo '
      f'(REGRA 22). Os blocos seguintes s&#227;o detalhados ao final de cada bloco de 12.</p>')
