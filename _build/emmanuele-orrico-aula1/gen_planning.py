#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera planning.html (aba Planejamento do hub) da Emmanuele Orrico.

A tabela curricular das 33 aulas vem do perfil 360 (fonte da verdade), nao e digitada
a mao. Foco Linguistico e Atividade sao resumidos (a celula da tabela nao comporta o
paragrafo inteiro do perfil).
"""
import html
import json
import re

PERFIL = '/home/dan/alumni-tools/perfis/emmanuele-orrico.json'
OUT = 'planning.html'

d = json.load(open(PERFIL, encoding='utf-8'))
curriculo = d['curriculo']
assert len(curriculo) == 33, f'esperava 33 aulas, achei {len(curriculo)}'


def esc(s):
    return html.escape(s, quote=False)


def foco_resumo(fl):
    """Extrai o miolo gramatical do focoLinguistico (o campo tem paragrafos inteiros)."""
    m = re.search(r'Grammar \(new\):\s*(.+?)(?:;|\.\s|$)', fl)
    if m:
        return m.group(1).strip().rstrip('.')
    m = re.search(r'Grammar focus:\s*(.+?)(?:;|\.\s|$)', fl)
    if m:
        return m.group(1).strip().rstrip('.')
    m = re.search(r'Grammar \(review[^)]*\):\s*(.+?)(?:;|\.\s|$)', fl)
    if m:
        return m.group(1).strip().rstrip('.')
    return fl.split(';')[0].split('. ')[0].strip().rstrip('.')


def ativ_resumo(a):
    """Primeira fase util da atividadeEmAula, curta."""
    m = re.search(r'Phase 3[^:]*:\s*(.+?)(?:\.\s|$)', a)
    if m:
        return m.group(1).strip().rstrip('.')
    return a.split('. ')[0].strip().rstrip('.')


def trunc(s, n):
    s = s.strip()
    return s if len(s) <= n else s[: n - 1].rstrip(' ,;') + '&hellip;'


rows = []
for c in curriculo:
    n = c['aula']
    tema = esc(c['tema'])
    foco = trunc(esc(foco_resumo(c['focoLinguistico'])), 110)
    ativ = trunc(esc(ativ_resumo(c['atividadeEmAula'])), 95)
    if n == 1:
        tr = ('<tr style="border-bottom:1px solid var(--border);background:var(--accent-dim)">'
              f'<td style="padding:.5rem;font-weight:700">1</td>'
              f'<td style="padding:.5rem">{tema}</td>'
              f'<td style="padding:.5rem">{foco}</td>'
              f'<td style="padding:.5rem">{ativ}</td>'
              '<td style="padding:.5rem;font-weight:700;color:var(--accent)">Atual</td></tr>')
    else:
        bg = ';background:var(--bg-elevated)' if n % 2 == 1 else ''
        tr = (f'<tr style="border-bottom:1px solid var(--border){bg}">'
              f'<td style="padding:.5rem">{n}</td>'
              f'<td style="padding:.5rem">{tema}</td>'
              f'<td style="padding:.5rem">{foco}</td>'
              f'<td style="padding:.5rem">{ativ}</td>'
              '<td style="padding:.5rem;color:var(--text-dim)">Pr&#243;xima</td></tr>')
    rows.append('        ' + tr)

TABLE = '\n'.join(rows)

HTML = f'''
<div class="planning-section">

  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:1rem;margin-bottom:2rem">
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:1rem"><span style="font-size:.75rem;color:var(--text-dim);text-transform:uppercase;letter-spacing:1px">Nome</span><p style="font-weight:600;margin-top:.3rem">Emmanuele Orrico</p></div>
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:1rem"><span style="font-size:.75rem;color:var(--text-dim);text-transform:uppercase;letter-spacing:1px">Idade</span><p style="font-weight:600;margin-top:.3rem">44 anos</p></div>
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:1rem"><span style="font-size:.75rem;color:var(--text-dim);text-transform:uppercase;letter-spacing:1px">Empresa</span><p style="font-weight:600;margin-top:.3rem">Sanofi &mdash; ind&#250;stria farmac&#234;utica (matriz francesa)</p></div>
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:1rem"><span style="font-size:.75rem;color:var(--text-dim);text-transform:uppercase;letter-spacing:1px">Profiss&#227;o</span><p style="font-weight:600;margin-top:.3rem">Gerente Nacional de Demanda &mdash; Imunologia (8 doen&#231;as: dermatite at&#243;pica, asma, DPOC, rinossinusite...)</p></div>
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:1rem"><span style="font-size:.75rem;color:var(--text-dim);text-transform:uppercase;letter-spacing:1px">N&#237;vel</span><p style="font-weight:600;margin-top:.3rem">A2 (B&#225;sico) &mdash; compreende bem; a produ&#231;&#227;o oral est&#225; pr&#243;xima de A1 e trava sob press&#227;o</p></div>
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:1rem"><span style="font-size:.75rem;color:var(--text-dim);text-transform:uppercase;letter-spacing:1px">Foco</span><p style="font-weight:600;margin-top:.3rem">100% Business &mdash; reuni&#245;es com a Global, apresenta&#231;&#227;o de resultados, congressos m&#233;dicos, jantares com executivos. (Ingl&#234;s de sobreviv&#234;ncia/viagem fica nas aulas em GRUPO.)</p></div>
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:1rem"><span style="font-size:.75rem;color:var(--text-dim);text-transform:uppercase;letter-spacing:1px">Frequ&#234;ncia</span><p style="font-weight:600;margin-top:.3rem">2x por semana (segundas e sextas, 17h) &mdash; Online (Zoom), 60 min</p></div>
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:1rem"><span style="font-size:.75rem;color:var(--text-dim);text-transform:uppercase;letter-spacing:1px">Total de Aulas</span><p style="font-weight:600;margin-top:.3rem">33 aulas (60 min)</p></div>
  </div>

  <div style="background:linear-gradient(135deg,var(--accent-dim),rgba(91,33,182,.03));border:1px solid var(--accent);border-radius:12px;padding:1.5rem;margin-bottom:1.5rem">
    <h4 style="font-family:'Cormorant Garamond',serif;font-size:1.2rem;margin-bottom:.8rem">Personagem-Jornada</h4>
    <p style="font-size:.9rem"><strong>De:</strong> Executiva que domina imunologia, acesso a mercado e execu&#231;&#227;o de campo &mdash; e trava por completo quando a conversa vira para o ingl&#234;s. Ela mesma definiu: <em>&#8220;Se voc&#234; tentar falar comigo em ingl&#234;s aqui agora eu vou travar. Quando voc&#234; desligar, eu vou: ai, ela falou isso.&#8221;</em> Ciclos repetidos de tentativa e abandono: <em>&#8220;n&#227;o vai ser to be esse inferno na minha vida, que eu j&#225; aprendi, desaprendi, aprendi, desaprendi.&#8221;</em></p>
    <p style="font-size:.9rem;margin-top:.5rem"><strong>Para:</strong> Gerente que, na &#250;ltima semana de agosto, apresenta resultados, desafios e oportunidades do Brasil para o time Global da Sanofi &mdash; em ingl&#234;s, de p&#233;, sem pedir para outra pessoa falar por ela. Ela disse: <em>&#8220;Eu deveria fazer, se eu tiver coragem.&#8221;</em> O programa inteiro existe para transformar esse &#8220;se&#8221; em &#8220;vou&#8221;.</p>
  </div>

  <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:12px;padding:1.5rem;margin-bottom:1.5rem">
    <h4 style="font-family:'Cormorant Garamond',serif;font-size:1.2rem;margin-bottom:.8rem">Promessa Transformadora</h4>
    <p style="font-size:.9rem">O problema da Emmanuele <strong>n&#227;o &#233; conhecimento</strong> &mdash; ela descreve com precis&#227;o cir&#250;rgica perfil de paciente, PCDT, SUS, operadoras e din&#226;mica competitiva contra Lilly, AstraZeneca e GSK. O problema &#233; o <strong>canal de sa&#237;da</strong>: o racioc&#237;nio dela tenta traduzir o tempo inteiro e a frase n&#227;o se forma a tempo. Cada aula ataca isso com o material real dela &mdash; resultados, lan&#231;amentos, brand plan, time de campo, reuni&#227;o com a Global &mdash; e entrega <strong>andaimes</strong> (frases prontas, sentence starters) para que ela nunca fique em sil&#234;ncio. A Alumni &#233; <em>&#8220;a minha &#250;ltima cartada&#8221;</em>: o material n&#227;o pode parecer mais um curso.</p>
  </div>

  <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-bottom:2rem">
    <div style="background:var(--success-bg);border:1px solid var(--success-border);border-radius:10px;padding:1.2rem">
      <h5 style="color:var(--success);font-size:.85rem;margin-bottom:.6rem">For&#231;as</h5>
      <ul style="font-size:.85rem;padding-left:1.2rem;display:flex;flex-direction:column;gap:.3rem">
        <li>Dom&#237;nio profundo da &#225;rea &mdash; o problema &#233; o c&#243;digo (ingl&#234;s), n&#227;o a mensagem</li>
        <li>Autoconsci&#234;ncia rara sobre o pr&#243;prio bloqueio: <em>&#8220;meu racioc&#237;nio ainda demora demais para conectar, tenta traduzir o tempo inteiro&#8221;</em></li>
        <li>Contexto de uso alt&#237;ssimo e definido: Global, resultados, Rain Plan, congressos, jantares</li>
        <li>H&#225;bito auditivo di&#225;rio j&#225; instalado: <em>&#8220;todo dia eu consigo ouvir podcast&#8221;</em></li>
        <li>Evento-alvo com data: &#250;ltima semana de agosto de 2026, apresenta&#231;&#227;o ao time Global</li>
        <li>Aprende praticando: <em>&#8220;eu funciono muito praticando&#8221;</em></li>
      </ul>
    </div>
    <div style="background:var(--danger-bg);border:1px solid var(--danger-border);border-radius:10px;padding:1.2rem">
      <h5 style="color:var(--danger);font-size:.85rem;margin-bottom:.6rem">Pontos de Melhoria</h5>
      <ul style="font-size:.85rem;padding-left:1.2rem;display:flex;flex-direction:column;gap:.3rem">
        <li>Produ&#231;&#227;o oral praticamente inexistente em contexto real &mdash; travamento total sob press&#227;o</li>
        <li>Tradu&#231;&#227;o mental constante impede fluidez conversacional</li>
        <li>Hist&#243;rico de inconsist&#234;ncia e baixa prioriza&#231;&#227;o &mdash; risco real de abandono</li>
        <li>Pre-class ainda percebido como obriga&#231;&#227;o: <em>&#8220;vai ter que fazer, eu vou ter que me esfor&#231;ar&#8221;</em></li>
        <li>Participa&#231;&#227;o passiva nas reuni&#245;es &mdash; n&#227;o assume protagonismo em ingl&#234;s</li>
        <li>Baixa toler&#226;ncia ao erro &mdash; exige seguran&#231;a psicol&#243;gica desde a aula 1</li>
      </ul>
    </div>
  </div>

  <h4 style="font-family:'Cormorant Garamond',serif;font-size:1.2rem;margin-bottom:1rem">Curr&#237;culo Completo &mdash; 33 Aulas</h4>
  <div style="overflow-x:auto">
    <table style="width:100%;border-collapse:collapse;font-size:.82rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
      <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.6rem;text-align:left">#</th><th style="padding:.6rem;text-align:left">Tema</th><th style="padding:.6rem;text-align:left">Foco Lingu&#237;stico</th><th style="padding:.6rem;text-align:left">Atividade Principal</th><th style="padding:.6rem;text-align:left">Status</th></tr></thead>
      <tbody>
{TABLE}
      </tbody>
    </table>
  </div>

  <h4 style="font-family:'Cormorant Garamond',serif;font-size:1.2rem;margin:2rem 0 1rem">Metodologia</h4>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1rem;margin-bottom:2rem">
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:1.2rem">
      <h5 style="font-size:.9rem;margin-bottom:.5rem">1. A gram&#225;tica NUNCA &#233; o t&#237;tulo da aula</h5>
      <p style="font-size:.82rem;color:var(--text-mid)">Ela foi expl&#237;cita: <em>&#8220;n&#227;o vai ser to be esse inferno na minha vida.&#8221;</em> Nenhuma aula se chama &#8220;verbo X&#8221;. A estrutura aparece DENTRO do contexto dela (resultados, lan&#231;amentos, reuni&#227;o com a Global) e sempre por <strong>discovery</strong>: exemplos primeiro, regra depois. Zero conjuga&#231;&#227;o descontextualizada.</p>
    </div>
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:1.2rem">
      <h5 style="font-size:.9rem;margin-bottom:.5rem">2. Andaimes contra o travamento</h5>
      <p style="font-size:.82rem;color:var(--text-mid)">Ela trava e traduz mentalmente. Toda aula entrega <strong>frases prontas</strong> (sentence starters, survival card) que ela s&#243; precisa PEGAR, n&#227;o construir. Produ&#231;&#227;o livre sem apoio, no come&#231;o, s&#243; refor&#231;a o bloqueio.</p>
    </div>
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:1.2rem">
      <h5 style="font-size:.9rem;margin-bottom:.5rem">3. 100% Business (o particular)</h5>
      <p style="font-size:.82rem;color:var(--text-mid)">Combinado com a consultora: viagem e ingl&#234;s de sobreviv&#234;ncia ficam nas <strong>aulas em grupo</strong>. Aqui: imunologia, dermatite at&#243;pica, asma, DPOC, acesso, brand plan, congresso, jantar com executivo. Nada de aeroporto, hotel ou restaurante.</p>
    </div>
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:1.2rem">
      <h5 style="font-size:.9rem;margin-bottom:.5rem">4. Praticar &#233; o m&#233;todo</h5>
      <p style="font-size:.82rem;color:var(--text-mid)"><em>&#8220;Eu funciono muito praticando.&#8221;</em> Estilo cinest&#233;sico-auditivo: role-play, simula&#231;&#227;o, escuta ativa com resposta oral imediata. Atividade nova a cada 12-15 minutos &mdash; nunca 20 minutos de explica&#231;&#227;o.</p>
    </div>
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:1.2rem">
      <h5 style="font-size:.9rem;margin-bottom:.5rem">5. Progresso vis&#237;vel e erro normalizado</h5>
      <p style="font-size:.82rem;color:var(--text-mid)">Ela j&#225; desistiu de v&#225;rios cursos por <em>&#8220;nunca conseguir avan&#231;ar&#8221;</em>. O professor <strong>nomeia em voz alta</strong> o que ela conseguiu fazer em cada aula. Baseline gravado na aula 1, recomparado na 17. Toler&#226;ncia ao erro baixa &mdash; seguran&#231;a psicol&#243;gica desde o primeiro minuto.</p>
    </div>
  </div>

  <h4 style="font-family:'Cormorant Garamond',serif;font-size:1.2rem;margin-bottom:1rem">Mapa de Personalidade</h4>
  <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:12px;padding:1.5rem">
    <div style="display:flex;flex-direction:column;gap:.8rem">
      <div><div style="display:flex;justify-content:space-between;font-size:.82rem;margin-bottom:.3rem"><span>Introvertido</span><span>Extrovertido</span></div><div style="height:8px;background:var(--bg-elevated);border-radius:4px;overflow:hidden"><div style="width:60%;height:100%;background:var(--accent);border-radius:4px"></div></div></div>
      <div><div style="display:flex;justify-content:space-between;font-size:.82rem;margin-bottom:.3rem"><span>L&#250;dico</span><span>S&#233;rio, orientado a resultado</span></div><div style="height:8px;background:var(--bg-elevated);border-radius:4px;overflow:hidden"><div style="width:50%;height:100%;background:var(--accent);border-radius:4px"></div></div></div>
      <div><div style="display:flex;justify-content:space-between;font-size:.82rem;margin-bottom:.3rem"><span>Impulsivo</span><span>Reflexivo</span></div><div style="height:8px;background:var(--bg-elevated);border-radius:4px;overflow:hidden"><div style="width:70%;height:100%;background:var(--accent);border-radius:4px"></div></div></div>
      <div><div style="display:flex;justify-content:space-between;font-size:.82rem;margin-bottom:.3rem"><span>Aprendiz leitura/escrita</span><span>Aprendiz cinest&#233;sico (praticando)</span></div><div style="height:8px;background:var(--bg-elevated);border-radius:4px;overflow:hidden"><div style="width:90%;height:100%;background:var(--accent);border-radius:4px"></div></div></div>
      <div><div style="display:flex;justify-content:space-between;font-size:.82rem;margin-bottom:.3rem"><span>Toler&#226;ncia ao erro baixa</span><span>Toler&#226;ncia ao erro alta</span></div><div style="height:8px;background:var(--bg-elevated);border-radius:4px;overflow:hidden"><div style="width:30%;height:100%;background:var(--accent);border-radius:4px"></div></div></div>
      <div><div style="display:flex;justify-content:space-between;font-size:.82rem;margin-bottom:.3rem"><span>Insegura em ingl&#234;s</span><span>Confiante em ingl&#234;s</span></div><div style="height:8px;background:var(--bg-elevated);border-radius:4px;overflow:hidden"><div style="width:40%;height:100%;background:var(--accent);border-radius:4px"></div></div></div>
      <div><div style="display:flex;justify-content:space-between;font-size:.82rem;margin-bottom:.3rem"><span>Foco acad&#234;mico</span><span>Foco profissional</span></div><div style="height:8px;background:var(--bg-elevated);border-radius:4px;overflow:hidden"><div style="width:98%;height:100%;background:var(--accent);border-radius:4px"></div></div></div>
    </div>
  </div>

</div>
'''

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(HTML)
print(f'wrote {OUT} ({len(curriculo)} aulas na tabela curricular)')
