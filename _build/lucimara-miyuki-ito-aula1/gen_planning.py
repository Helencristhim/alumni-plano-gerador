#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera planning.html (aba Planejamento do hub) a partir do perfil 360 da Lucimara."""
import json
import os
import re

PERFIL = '/home/dan/alumni-tools/perfis/lucimara-miyuki-ito.json'
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'planning.html')

d = json.load(open(PERFIL, encoding='utf-8'))
cur = d['curriculo']


def esc(t):
    return (t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            .replace('—', '&mdash;').replace('–', '&ndash;')
            .replace('“', '&#8220;').replace('”', '&#8221;').replace('’', "'"))


def foco_curto(c):
    """1a frase util do focoLinguistico (o campo e um paragrafo longo)."""
    f = c['focoLinguistico']
    f = re.sub(r'^Diagnostic focus:\s*', '', f)
    f = re.sub(r'^Grammar \([^)]*\):\s*', '', f)
    parts = re.split(r'(?<=[.;])\s+', f)
    s = parts[0].strip()
    if len(s) > 130:
        s = s[:127].rsplit(' ', 1)[0] + '...'
    return s


def ativ_curta(c):
    """Rotulo da fase de PRODUCAO da aula (role-play / simulacao); fallback = Phase 4."""
    if c['aula'] == 1:
        return 'Conversa espontanea + baseline gravado de 90s + contrato de aprendizagem'
    a = c['atividadeEmAula']
    segs = [s for s in re.split(r'(?=Phase \d+)', a) if s.strip()]
    pick = next((s for s in segs if re.search(r'role-?play|simulation', s, re.I)), None)
    if pick is None:
        pick = segs[3] if len(segs) > 3 else segs[-1]
    # tira o prefixo "Phase N (...) — " / "Phase N (...): "
    s = re.sub(r'^Phase \d+\s*(?:\([^)]*\))?\s*[—:-]*\s*', '', pick).strip()
    head = re.split(r'[:.]', s)[0].strip()
    s = head if 12 <= len(head) <= 90 else s
    if len(s) > 90:
        s = s[:87].rsplit(' ', 1)[0] + '...'
    return s


rows = []
for c in cur:
    n = c['aula']
    atual = (n == 1)
    zebra = ' background:var(--bg-elevated);' if (n % 2 == 0 and not atual) else ''
    if atual:
        zebra = ' background:var(--accent-dim);'
    status = ('<td style="padding:.5rem;font-weight:700;color:var(--accent)">Atual</td>' if atual
              else '<td style="padding:.5rem;color:var(--text-dim)">Pr&#243;xima</td>')
    fw = ';font-weight:700' if atual else ''
    rows.append(
        f'<tr style="border-bottom:1px solid var(--border);{zebra}">'
        f'<td style="padding:.5rem{fw}">{n}</td>'
        f'<td style="padding:.5rem{fw}">{esc(c["tema"])}</td>'
        f'<td style="padding:.5rem">{esc(foco_curto(c))}</td>'
        f'<td style="padding:.5rem">{esc(ativ_curta(c))}</td>'
        f'{status}</tr>')

TABLE = '\n        '.join(rows)

HTML = f'''
<div class="planning-section">

  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:1rem;margin-bottom:2rem">
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:1rem"><span style="font-size:.75rem;color:var(--text-dim);text-transform:uppercase;letter-spacing:1px">Nome</span><p style="font-weight:600;margin-top:.3rem">Lucimara Miyuki Ito</p></div>
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:1rem"><span style="font-size:.75rem;color:var(--text-dim);text-transform:uppercase;letter-spacing:1px">Idade</span><p style="font-weight:600;margin-top:.3rem">55 anos</p></div>
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:1rem"><span style="font-size:.75rem;color:var(--text-dim);text-transform:uppercase;letter-spacing:1px">Cidade</span><p style="font-weight:600;margin-top:.3rem">S&#227;o Paulo, SP &mdash; Perdizes (40 min de carro at&#233; Guarulhos)</p></div>
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:1rem"><span style="font-size:.75rem;color:var(--text-dim);text-transform:uppercase;letter-spacing:1px">Profiss&#227;o</span><p style="font-weight:600;margin-top:.3rem">Diretora de ind&#250;stria qu&#237;mica (Guarulhos) &mdash; produ&#231;&#227;o e assuntos regulat&#243;rios (Anvisa); reuni&#245;es com fornecedores chineses</p></div>
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:1rem"><span style="font-size:.75rem;color:var(--text-dim);text-transform:uppercase;letter-spacing:1px">N&#237;vel</span><p style="font-weight:600;margin-top:.3rem">B1 (Intermedi&#225;rio) &mdash; exposi&#231;&#227;o real forte; o gargalo &#233; a COMPREENS&#195;O ORAL</p></div>
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:1rem"><span style="font-size:.75rem;color:var(--text-dim);text-transform:uppercase;letter-spacing:1px">Foco</span><p style="font-weight:600;margin-top:.3rem">55% Viagens e cotidiano &middot; 20% Listening intensivo &middot; 15% Business pontual e atualidades &middot; 10% Gram&#225;tica e escrita</p></div>
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:1rem"><span style="font-size:.75rem;color:var(--text-dim);text-transform:uppercase;letter-spacing:1px">Frequ&#234;ncia</span><p style="font-weight:600;margin-top:.3rem">2x por semana &mdash; segundas 18h e quartas 11h, Online (Zoom), 60 min</p></div>
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:1rem"><span style="font-size:.75rem;color:var(--text-dim);text-transform:uppercase;letter-spacing:1px">Total de Aulas</span><p style="font-weight:600;margin-top:.3rem">48 aulas (60 min) &mdash; meta: Nova York, setembro de 2026</p></div>
  </div>

  <div style="background:linear-gradient(135deg,var(--accent-dim),rgba(91,45,95,.03));border:1px solid var(--accent);border-radius:12px;padding:1.5rem;margin-bottom:1.5rem">
    <h4 style="font-family:'Cormorant Garamond',serif;font-size:1.2rem;margin-bottom:.8rem">Personagem-Jornada</h4>
    <p style="font-size:.9rem"><strong>De:</strong> Viajante frequente que &#8220;fica patinando&#8221; &mdash; trava no listening, perdeu a disciplina com a professora que virou amiga e sente que o ingl&#234;s n&#227;o evolui apesar das viagens. Nas palavras dela: <em>&#8220;Eu tenho um pouco de pressa, porque eu t&#244; meio que, sabe, quando voc&#234; fica patinando na coisa.&#8221;</em></p>
    <p style="font-size:.9rem;margin-top:.5rem"><strong>Para:</strong> Diretora que circula por Nova York, conduz reuni&#245;es com parceiros chineses e navega feiras internacionais com autonomia real &mdash; e que ENTENDE o que o outro est&#225; dizendo, na velocidade em que ele diz.</p>
  </div>

  <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:12px;padding:1.5rem;margin-bottom:1.5rem">
    <h4 style="font-family:'Cormorant Garamond',serif;font-size:1.2rem;margin-bottom:.8rem">Promessa Transformadora</h4>
    <p style="font-size:.9rem">Lucimara para de &#8220;patinar&#8221; e passa a entender o que os americanos falam &mdash; de Nova York &#224; China, sem depender de ningu&#233;m. O gargalo dela N&#195;O &#233; vocabul&#225;rio nem coragem: &#233; o <strong>canal auditivo</strong>. Ela mesma nomeou: <em>&#8220;O entendimento. Eu tenho bastante dificuldade. O listening.&#8221;</em> Por isso TODA aula deste programa carrega listening de verdade &mdash; &#225;udio ElevenLabs, player com controle de velocidade, e um podcast recomendado para os 80 minutos di&#225;rios de carro. O ouvido se treina como o corpo: ela j&#225; malha 5x por semana, ent&#227;o sabe exatamente do que estamos falando.</p>
  </div>

  <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-bottom:2rem">
    <div style="background:var(--success-bg);border:1px solid var(--success-border);border-radius:10px;padding:1.2rem">
      <h5 style="color:var(--success);font-size:.85rem;margin-bottom:.6rem">For&#231;as</h5>
      <ul style="font-size:.85rem;padding-left:1.2rem;display:flex;flex-direction:column;gap:.3rem">
        <li>Exposi&#231;&#227;o real e frequente &mdash; viaja ao exterior a cada 2-3 meses (Nova York, Fort Lauderdale, China)</li>
        <li>Clareza total de objetivo: conversa&#231;&#227;o para viagens. Zero interesse em certifica&#231;&#227;o</li>
        <li>Autoconhecimento &mdash; identificou sozinha o problema da professora-amiga e buscou estrutura</li>
        <li>J&#225; reservou a janela de estudo: 40 min de ida + 40 de volta, todo dia, ouvindo no carro</li>
        <li>Motiva&#231;&#227;o intr&#237;nseca &mdash; o ingl&#234;s est&#225; atrelado ao que ela ama (viajar), n&#227;o a obriga&#231;&#227;o</li>
        <li>Disciplina comprovada em outra &#225;rea: corre no Ibirapuera e treina 5x por semana, de manh&#227; cedo</li>
      </ul>
    </div>
    <div style="background:var(--danger-bg);border:1px solid var(--danger-border);border-radius:10px;padding:1.2rem">
      <h5 style="color:var(--danger);font-size:.85rem;margin-bottom:.6rem">Pontos de Melhoria</h5>
      <ul style="font-size:.85rem;padding-left:1.2rem;display:flex;flex-direction:column;gap:.3rem">
        <li><strong>Listening em ritmo nativo</strong> &mdash; o gap n&#186; 1, declarado por ela mesma</li>
        <li>Disciplina de estudo aut&#244;nomo &mdash; hist&#243;rico de irregularidade sem estrutura clara</li>
        <li>Poss&#237;vel superestima&#231;&#227;o do n&#237;vel (autodeclara &#8220;intermedi&#225;rio para avan&#231;ado&#8221;; o listening diz B1)</li>
        <li>Escrita e leitura menos desenvolvidas que a fala &mdash; ela pediu explicitamente para trabalhar as duas</li>
        <li>Cren&#231;a limitante sobre a idade: <em>&#8220;pessoas de mais de cinquenta anos j&#225; t&#234;m mais dificuldade&#8221;</em>. O material desmente isso pela PR&#193;TICA (progresso vis&#237;vel, baseline gravado) &mdash; nunca pelo discurso</li>
      </ul>
    </div>
  </div>

  <h4 style="font-family:'Cormorant Garamond',serif;font-size:1.2rem;margin-bottom:1rem">Curr&#237;culo Completo &mdash; 48 Aulas</h4>
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
      <h5 style="font-size:.9rem;margin-bottom:.5rem">1. Listening em TODA aula &mdash; o gap n&#186; 1</h5>
      <p style="font-size:.82rem;color:var(--text-mid)">Dois &#225;udios longos por aula, com player completo e controle de velocidade (0.5x a 1.25x). Protocolo fixo: som primeiro, sem texto; &#8220;what did you catch?&#8221;; segunda escuta mais lenta; s&#243; ent&#227;o as perguntas. Nunca tradu&#231;&#227;o.</p>
    </div>
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:1.2rem">
      <h5 style="font-size:.9rem;margin-bottom:.5rem">2. Os 80 minutos de carro viram sala de aula</h5>
      <p style="font-size:.82rem;color:var(--text-mid)">Ela mesma ofereceu a janela: <em>&#8220;mesmo que eu v&#225; ouvindo no carro, s&#227;o quarenta minutos de ida, quarenta de volta&#8221;</em>. Os Complementares priorizam <strong>podcast e &#225;udio</strong> (ela assiste pouca s&#233;rie) e sempre com tarefa concreta: 3 frases entendidas, 2 n&#227;o captadas.</p>
    </div>
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:1.2rem">
      <h5 style="font-size:.9rem;margin-bottom:.5rem">3. Contexto de viagem, n&#227;o de curso</h5>
      <p style="font-size:.82rem;color:var(--text-mid)">Aeroporto, hotel, t&#225;xi, restaurante, feira internacional, jantar com parceiro chin&#234;s. O conte&#250;do &#233; o que ela vai viver em setembro em Nova York &mdash; nunca ingl&#234;s gen&#233;rico. Business entra pontual: reuni&#245;es com chineses e atualidades.</p>
    </div>
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:1.2rem">
      <h5 style="font-size:.9rem;margin-bottom:.5rem">4. Ritmo calmo, adulto-adulto (REGRA 14 &mdash; 50+)</h5>
      <p style="font-size:.82rem;color:var(--text-mid)">Repeti&#231;&#227;o generosa, pausas, tempo para pensar. Zero gamifica&#231;&#227;o infantil e zero condescend&#234;ncia: ela &#233; diretora de uma ind&#250;stria. A viv&#234;ncia internacional dela &#233; recurso pedag&#243;gico, n&#227;o enfeite.</p>
    </div>
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:1.2rem">
      <h5 style="font-size:.9rem;margin-bottom:.5rem">5. V&#237;nculo profissional, NUNCA amizade</h5>
      <p style="font-size:.82rem;color:var(--text-mid)">O ponto cr&#237;tico do hist&#243;rico dela: a professora anterior virou amiga e a aula virou conversa. Seja caloroso e mantenha a autoridade pedag&#243;gica. Cada aula precisa mostrar PROGRESSO TANG&#205;VEL &mdash; &#233; o que sustenta a motiva&#231;&#227;o dela.</p>
    </div>
  </div>

  <h4 style="font-family:'Cormorant Garamond',serif;font-size:1.2rem;margin-bottom:1rem">Mapa de Personalidade</h4>
  <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:12px;padding:1.5rem">
    <div style="display:flex;flex-direction:column;gap:.8rem">
      <div><div style="display:flex;justify-content:space-between;font-size:.82rem;margin-bottom:.3rem"><span>Introvertida</span><span>Extrovertida</span></div><div style="height:8px;background:var(--bg-elevated);border-radius:4px;overflow:hidden"><div style="width:80%;height:100%;background:var(--accent);border-radius:4px"></div></div></div>
      <div><div style="display:flex;justify-content:space-between;font-size:.82rem;margin-bottom:.3rem"><span>L&#250;dica</span><span>S&#233;ria, orientada a resultado</span></div><div style="height:8px;background:var(--bg-elevated);border-radius:4px;overflow:hidden"><div style="width:60%;height:100%;background:var(--accent);border-radius:4px"></div></div></div>
      <div><div style="display:flex;justify-content:space-between;font-size:.82rem;margin-bottom:.3rem"><span>Impulsiva</span><span>Reflexiva</span></div><div style="height:8px;background:var(--bg-elevated);border-radius:4px;overflow:hidden"><div style="width:60%;height:100%;background:var(--accent);border-radius:4px"></div></div></div>
      <div><div style="display:flex;justify-content:space-between;font-size:.82rem;margin-bottom:.3rem"><span>Aprendiz leitura/escrita</span><span>Aprendiz auditiva/oral</span></div><div style="height:8px;background:var(--bg-elevated);border-radius:4px;overflow:hidden"><div style="width:85%;height:100%;background:var(--accent);border-radius:4px"></div></div></div>
      <div><div style="display:flex;justify-content:space-between;font-size:.82rem;margin-bottom:.3rem"><span>Toler&#226;ncia ao erro baixa</span><span>Toler&#226;ncia ao erro alta</span></div><div style="height:8px;background:var(--bg-elevated);border-radius:4px;overflow:hidden"><div style="width:80%;height:100%;background:var(--accent);border-radius:4px"></div></div></div>
      <div><div style="display:flex;justify-content:space-between;font-size:.82rem;margin-bottom:.3rem"><span>Insegura em ingl&#234;s</span><span>Confiante em ingl&#234;s</span></div><div style="height:8px;background:var(--bg-elevated);border-radius:4px;overflow:hidden"><div style="width:55%;height:100%;background:var(--accent);border-radius:4px"></div></div></div>
      <div><div style="display:flex;justify-content:space-between;font-size:.82rem;margin-bottom:.3rem"><span>Foco profissional</span><span>Foco viagem e vida</span></div><div style="height:8px;background:var(--bg-elevated);border-radius:4px;overflow:hidden"><div style="width:80%;height:100%;background:var(--accent);border-radius:4px"></div></div></div>
    </div>
  </div>

</div>
'''

open(OUT, 'w', encoding='utf-8').write(HTML)
print(f'planning.html: {len(HTML)//1024} KB, {len(cur)} aulas na tabela')
