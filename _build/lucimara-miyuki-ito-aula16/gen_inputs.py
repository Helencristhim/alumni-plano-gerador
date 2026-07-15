# -*- coding: utf-8 -*-
"""Authoring helper for lucimara-miyuki-ito aula 16 (reported speech, reading model).
Emits slides.html + preclass.html into this dir. Shares vocab data so IN CLASS and
Pre-class stay identical. Input to build_from_model.py — NOT a build contorno."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))

ACCENT = "#5B2D5F"

# word, definition, example (example is display-only), icon gradient, icon svg inner
VOCAB = [
    ("Walkable", "easy to get around on foot",
     '"She said the downtown was walkable, so I left the car behind."',
     "#0e7490,#22d3ee", '<path d="M13 4a2 2 0 11-4 0 2 2 0 014 0z"/><path d="M9 8l2 4-1 8M11 12l3 2 3 5M8 11l3-1"/>'),
    ("Grid system", "streets laid out in a regular pattern of numbered blocks",
     '"He told me the streets followed a grid system, so they were easy to find."',
     "#b45309,#f59e0b", '<rect x="4" y="4" width="16" height="16" rx="1"/><path d="M4 10h16M4 15h16M10 4v16M15 4v16"/>'),
    ("Urban sprawl", "the spread of a city outward over a large area",
     '"A friend said the urban sprawl went on for miles."',
     "#4338ca,#818cf8", '<path d="M3 21h18M5 21V9l4-2 4 2 6-2v14M8 12h2M8 16h2M15 12h2M15 16h2"/>'),
    ("To carpool", "to share a car ride with other people going the same way",
     '"She said that most people carpooled to work."',
     "#0d9488,#2dd4bf", '<circle cx="8" cy="8" r="2.2"/><circle cx="16" cy="8" r="2.2"/><path d="M3 19a5 5 0 0110 0M11 19a5 5 0 0110 0"/>'),
    ("Surge pricing", "higher rideshare prices when a lot of people want a ride",
     '"He warned me that the app used surge pricing at rush hour."',
     "#b91c1c,#f87171", '<path d="M4 18l5-6 4 3 6-8"/><path d="M15 7h4v4"/>'),
    ("Bike lane", "a marked part of the road only for bicycles",
     '"She told me there was a bike lane along the river."',
     "#15803d,#4ade80", '<circle cx="6" cy="17" r="3"/><circle cx="18" cy="17" r="3"/><path d="M6 17l4-8h5l3 8M10 9l4 0"/>'),
    ("To reroute", "to change a planned route to avoid a problem",
     '"He said the app would reroute me around the traffic."',
     "#9f1239,#fb7185", '<path d="M4 7h9a4 4 0 010 8H8"/><path d="M8 12l-4 3 4 3"/>'),
    ("Bottleneck", "a narrow point where traffic slows down and backs up",
     '"She said a rideshare would only trap me in a bottleneck."',
     "#c2410c,#fb923c", '<path d="M6 3h12l-4 7v6a2 2 0 01-4 0v-6z"/>'),
    ("Crosstown", "going from one side of the city to the other",
     '"He told me the subway was best for a crosstown trip."',
     "#0369a1,#38bdf8", '<path d="M3 12h18M3 12l4-4M3 12l4 4M21 12l-4-4M21 12l-4 4"/>'),
    ("On foot", "walking instead of using a car or transport",
     '"She said that in some cities you move on foot."',
     "#0f766e,#5eead4", '<path d="M8 4l1 9 2 1-1 6M12 13l3 1 2 5M9 13l4-1"/>'),
    ("Toll booth", "a place on a road or bridge where you stop to pay",
     '"He said we would stop at a toll booth on the bridge."',
     "#ca8a04,#fde047", '<path d="M5 21V10l7-4 7 4v11M5 21h14M9 21v-6h6v6"/>'),
    ("To flag down", "to signal a taxi or bus to stop for you",
     '"She told me to flag down a cab on the avenue."',
     "#1d4ed8,#60a5fa", '<path d="M6 21V4M6 4h11l-2 4 2 4H6"/>'),
]

LISTEN_ICON = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
               '<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/>'
               '<path d="M15.54 8.46a5 5 0 010 7.07"/></svg>')


def reveal_card(word, definition, example, grad, svg):
    return (
        '      <div class="vocab-card" onclick="revealVocab(this)">\n'
        f'        <div class="card-icon" style="background:linear-gradient(135deg,{grad})"><svg viewBox="0 0 24 24" fill="none" stroke="#fff">{svg}</svg><div class="card-hint">{definition}</div></div>\n'
        f'        <div class="card-body"><div class="card-word">{word}</div><div class="card-def">{definition}</div><div class="card-example">{example}</div><div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText(\'{word}\',this)">{LISTEN_ICON} Listen</button></div></div>\n'
        '      </div>')


def listen_btn(phrase):
    return (f'<button class="audio-btn-sm" onclick="event.stopPropagation();speakText(\'{phrase}\',this)">{LISTEN_ICON} Listen</button>')


# ---------------------------------------------------------------- SLIDES
def build_slides():
    S = []
    A = "var(--accent)"
    # 1 hero
    S.append(f'''<!-- ========== SLIDE 1 ========== -->
<div class="slide slide-image active" data-slide="1" data-phase="1" data-teacher="<strong>Abertura (2 min):</strong> Compartilhe a tela. NAO cumprimente de forma scriptada (REGRA 27A). Va direto ao tema: hoje a Lucimara vai aprender a RELATAR os conselhos que recebe sobre como se locomover em cidades americanas." style="background-image:linear-gradient(rgba(20,12,22,.78),rgba(20,12,22,.9)),url('https://images.unsplash.com/photo-1524850011238-e3d235c7d4c9?w=1400&q=80');background-size:cover;background-position:center">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label">Lesson 16 &middot; Getting Around Like a Local</div>
    <h1 class="slide-heading" style="font-size:2.4rem;color:#fff">Getting Around Like a <span class="accent">Local</span></h1>
    <p style="color:rgba(255,255,255,.85);font-size:1.05rem;margin-top:1rem">Every American city moves differently. Learn the words for it, then report the advice a local gives you.</p>
  </div>
</div>''')
    # 2 warm-up (callback aula15 small talk)
    S.append(f'''<!-- ========== SLIDE 2 ========== -->
<div class="slide slide-dark" data-slide="2" data-phase="1" data-teacher="<strong>Warm-up + callback (3 min):</strong> Ponte com a aula 15 (small talk). Faca a pergunta do slide e deixe a Lucimara falar sobre uma cidade onde se sentiu perdida. ZERO correcao aqui.">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label">Warm-Up</div>
    <h2 class="slide-heading" style="color:#fff">Whose Advice Do You <span class="accent">Trust?</span></h2>
    <p style="color:rgba(255,255,255,.82);font-size:1rem;margin:1rem auto 0;max-width:600px">Last time you kept a conversation going with small talk. Today you go one step further: when a local gives you real advice about getting around their city, you will pass it on to someone else. New York or Los Angeles? Subway or car? By the end of this hour, you will report exactly what people told you.</p>
    <p style="color:var(--accent-light);font-size:.92rem;margin-top:1.3rem">In one sentence: what is the hardest city you have ever tried to get around, and why?</p>
  </div>
</div>''')
    # 3 agenda
    S.append(f'''<!-- ========== SLIDE 3 ========== -->
<div class="slide slide-light" data-slide="3" data-phase="1" data-teacher="<strong>Agenda (1 min):</strong> Apresente as tres missoes. Tom caloroso e direto. Passe ao proximo.">
  <div class="slide-inner">
    <div class="chapter-label">Today</div>
    <h2 class="slide-heading">Three <span class="accent">Missions</span></h2>
    <div style="display:flex;flex-direction:column;gap:.8rem;max-width:540px;margin:1.4rem auto 0">
      <div style="display:flex;gap:.9rem;align-items:center;background:var(--bg-card);border:1px solid var(--border);border-radius:12px;padding:1rem 1.2rem"><div style="width:34px;height:34px;border-radius:9px;background:{A};color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;flex-shrink:0">1</div><p style="font-size:.95rem">Learn the words for how American cities really move.</p></div>
      <div style="display:flex;gap:.9rem;align-items:center;background:var(--bg-card);border:1px solid var(--border);border-radius:12px;padding:1rem 1.2rem"><div style="width:34px;height:34px;border-radius:9px;background:{A};color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;flex-shrink:0">2</div><p style="font-size:.95rem">Use reported speech to pass on what a local told you.</p></div>
      <div style="display:flex;gap:.9rem;align-items:center;background:var(--bg-card);border:1px solid var(--border);border-radius:12px;padding:1rem 1.2rem"><div style="width:34px;height:34px;border-radius:9px;background:{A};color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;flex-shrink:0">3</div><p style="font-size:.95rem">Report real travel advice out loud, clearly and confidently.</p></div>
    </div>
  </div>
</div>''')
    # 4 vocab transition
    S.append(f'''<!-- ========== SLIDE 4 ========== -->
<div class="slide slide-image" data-slide="4" data-phase="2" data-teacher="<strong>Transicao vocab (1 min):</strong> Diga: doze palavras e expressoes novas sobre como se locomover. Click each card to reveal. Passe ao proximo." style="background-image:linear-gradient(rgba(20,12,22,.78),rgba(20,12,22,.9)),url('https://images.unsplash.com/photo-1490644658840-3f2e3f8c5625?w=1400&q=80');background-size:cover;background-position:center">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label">Chapter 2: Local Words</div>
    <h2 class="slide-heading" style="font-size:2rem;color:#fff">Words for Getting <span class="accent">Around</span></h2>
    <p style="color:rgba(255,255,255,.82);font-size:1rem;margin-top:.5rem">12 key words and expressions</p>
  </div>
</div>''')
    # 5 reveal 1-6
    cards1 = '\n'.join(reveal_card(*VOCAB[i]) for i in range(6))
    S.append(f'''<!-- ========== SLIDE 5 ========== -->
<div class="slide slide-light" data-slide="5" data-phase="2" data-teacher="<strong>Vocab reveal 1-6 (6 min):</strong> Leia a pista em ingles, a Lucimara tenta a palavra, depois revele e toque o audio. CCQ curto (ex: walkable -- easy to walk? yes).">
  <div class="slide-inner">
    <div class="chapter-label">Vocabulary</div>
    <h2 class="slide-heading">Words <span class="accent">1-6</span></h2>
    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem"><span id="vocabCount1">0 / 6 words revealed</span></p>
    <div class="vocab-grid" id="vocabGrid1">
{cards1}
    </div>
  </div>
</div>''')
    # 6 reveal 7-12
    cards2 = '\n'.join(reveal_card(*VOCAB[i]) for i in range(6, 12))
    S.append(f'''<!-- ========== SLIDE 6 ========== -->
<div class="slide slide-light" data-slide="6" data-phase="2" data-teacher="<strong>Vocab reveal 7-12 (6 min):</strong> Mesma dinamica. Confirme com CCQs rapidas e peca 1 frase-exemplo da Lucimara para 2 palavras (ex: crosstown, on foot).">
  <div class="slide-inner">
    <div class="chapter-label">Vocabulary</div>
    <h2 class="slide-heading">Words <span class="accent">7-12</span></h2>
    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem"><span id="vocabCount2">0 / 6 words revealed</span></p>
    <div class="vocab-grid" id="vocabGrid2">
{cards2}
    </div>
  </div>
</div>''')
    # 7 matching (block)
    S.append(f'''<!-- ========== SLIDE 7 ========== -->
<div class="slide slide-light" data-slide="7" data-phase="2" data-teacher="<strong>Consolidar vocab (3 min):</strong> A Lucimara liga cada palavra a definicao em voz alta. Leitura guiada; confirme as duplas que costumam confundir (grid system / urban sprawl).">
  <div class="slide-inner">
    <div class="chapter-label">Consolidate</div>
    <h2 class="slide-heading">Match the <span class="accent">Meaning</span></h2>
    <!--IC-BLOCKS:vocab-->
  </div>
</div>''')
    # 8 reading transition
    S.append(f'''<!-- ========== SLIDE 8 ========== -->
<div class="slide slide-image" data-slide="8" data-phase="3" data-teacher="<strong>Transicao leitura (1 min):</strong> Diga: read for the main idea first, do not worry about every word. Passe ao proximo." style="background-image:linear-gradient(rgba(20,12,22,.78),rgba(20,12,22,.9)),url('https://images.unsplash.com/photo-1502920514313-52581002a659?w=1400&q=80');background-size:cover;background-position:center">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label">Chapter 3: The Advice</div>
    <h2 class="slide-heading" style="font-size:2rem;color:#fff">Read the <span class="accent">Advice</span></h2>
    <p style="color:rgba(255,255,255,.82);font-size:1rem;margin-top:.5rem">Read for the main idea</p>
  </div>
</div>''')
    # 9 reading + gist
    S.append(f'''<!-- ========== SLIDE 9 ========== -->
<div class="slide slide-light" data-slide="9" data-phase="3" data-teacher="<strong>Reading + Gist (5 min):</strong> De 2 minutos de leitura silenciosa. Depois: what is the main idea? A Lucimara clica a alternativa certa (fica verde). NAO peca traducao palavra a palavra.">
  <div class="slide-inner">
    <div class="chapter-label">Read for the Main Idea</div>
    <h2 class="slide-heading">The City Decides How You <span class="accent">Move</span></h2>
    <!--IC-BLOCKS:reading-->
  </div>
</div>''')
    # 10 tf
    S.append(f'''<!-- ========== SLIDE 10 ========== -->
<div class="slide slide-light" data-slide="10" data-phase="3" data-teacher="<strong>True / False (4 min):</strong> A Lucimara decide TRUE ou FALSE ANTES de clicar. Ao clicar, o veredito e a justificativa aparecem. Discuta cada uma voltando ao texto.">
  <div class="slide-inner">
    <div class="chapter-label">Check Understanding</div>
    <h2 class="slide-heading">True or <span class="accent">False?</span></h2>
    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem">Decide first, then tap to reveal the answer and why</p>
    <!--IC-BLOCKS:tf-->
  </div>
</div>''')
    # 11 gapfill
    S.append(f'''<!-- ========== SLIDE 11 ========== -->
<div class="slide slide-light" data-slide="11" data-phase="3" data-teacher="<strong>Gap-fill (5 min):</strong> A Lucimara le o resumo e escolhe a palavra certa do banco, EM VOZ ALTA. Sem gabarito visivel. Use o vocab-note para reforcar a gramatica.">
  <div class="slide-inner">
    <div class="chapter-label">Complete the Summary</div>
    <h2 class="slide-heading">Fill the <span class="accent">Gaps</span></h2>
    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem">Read the summary and choose a word from the bank for each gap</p>
    <!--IC-BLOCKS:gapfill-->
  </div>
</div>''')
    # 12 bank
    S.append(f'''<!-- ========== SLIDE 12 ========== -->
<div class="slide slide-light" data-slide="12" data-phase="3" data-teacher="<strong>Useful language (3 min):</strong> Apresente as frases-modelo de reported speech. Peca que a Lucimara leia cada chip em voz alta.">
  <div class="slide-inner">
    <div class="chapter-label">Report It</div>
    <h2 class="slide-heading">Useful <span class="accent">Phrases</span></h2>
    <!--IC-BLOCKS:bank-->
  </div>
</div>''')
    # 13 grammar transition
    S.append(f'''<!-- ========== SLIDE 13 ========== -->
<div class="slide slide-image" data-slide="13" data-phase="4" data-teacher="<strong>Transicao gramatica (1 min):</strong> Diga que o foco agora e RELATAR o que alguem disse: say/told + verbo um passo no passado. Passe ao proximo." style="background-image:linear-gradient(rgba(20,12,22,.78),rgba(20,12,22,.9)),url('https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?w=1400&q=80');background-size:cover;background-position:center">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label">Chapter 4: Reporting It</div>
    <h2 class="slide-heading" style="font-size:2rem;color:#fff">Say What They <span class="accent">Said</span></h2>
    <p style="color:rgba(255,255,255,.82);font-size:1rem;margin-top:.5rem">said / told &middot; present &rarr; past &middot; will &rarr; would &middot; can &rarr; could</p>
  </div>
</div>''')
    # 14 grammar discovery (data-grammar injected here)
    ex = [
        "She said that she lived near a subway station.",
        "He told me that I would need a car there.",
        "She said that the app raised prices at rush hour.",
    ]
    hi = ['lived', 'would', 'raised']
    rows = ''
    for e, h in zip(ex, hi):
        marked = e.replace(h, f'<span class="accent" style="font-weight:700">{h}</span>', 1)
        rows += (f'      <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:.8rem;display:flex;justify-content:space-between;align-items:center;gap:.6rem"><p style="font-size:.92rem">"{marked}"</p>{listen_btn(e)}</div>\n')
    S.append(f'''<!-- ========== SLIDE 14 ========== -->
<div class="slide slide-light" data-slide="14" data-phase="4" data-teacher="<strong>Grammar discovery (6 min):</strong> Leia os 3 exemplos. NAO mostre a regra primeiro. Pergunte o que acontece com o verbo quando relatamos o que alguem disse (present vira past; will vira would). So entao clique Reveal the Rule.">
  <div class="slide-inner">
    <div class="chapter-label">Grammar Discovery</div>
    <h2 class="slide-heading">Listen and <span class="accent">Notice</span></h2>
    <div style="display:flex;flex-direction:column;gap:.7rem;max-width:620px;margin:1rem auto 0">
{rows}    </div>
    <p style="text-align:center;font-size:.85rem;color:var(--text-dim);margin-top:1rem">Each person is reporting what someone else said. What happens to the verb -- and when do we use "said" and when "told me"?</p>
    <button class="primary-btn" style="margin:1rem auto 0;display:block;background:{A};color:#fff;border:none;border-radius:8px;padding:.6rem 1.4rem;font-size:.9rem;font-weight:600;cursor:pointer" onclick="var t=document.getElementById('rule16');t.style.display=(t.style.display==='none'||!t.style.display)?'block':'none'">Reveal the Rule</button>
    <div id="rule16" style="display:none;max-width:620px;margin:1rem auto 0;overflow-x:auto">
      <table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:{A};color:#fff"><th style="padding:.6rem;text-align:left">Direct speech</th><th style="padding:.6rem;text-align:left">Reported speech</th><th style="padding:.6rem;text-align:left">Change</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.5rem">"I <strong>live</strong> here."</td><td style="padding:.5rem">She said that she <strong>lived</strong> there.</td><td style="padding:.5rem">present &rarr; past</td></tr>
          <tr style="background:var(--bg-elevated);border-bottom:1px solid var(--border)"><td style="padding:.5rem">"You <strong>will</strong> need a car."</td><td style="padding:.5rem">He told me that I <strong>would</strong> need a car.</td><td style="padding:.5rem">will &rarr; would</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.5rem">"You <strong>can</strong> walk."</td><td style="padding:.5rem">She said that I <strong>could</strong> walk.</td><td style="padding:.5rem">can &rarr; could</td></tr>
          <tr style="background:var(--bg-elevated)"><td style="padding:.5rem">say / tell</td><td style="padding:.5rem"><strong>said (that)</strong> &middot; <strong>told me (that)</strong></td><td style="padding:.5rem">tell needs a person; say does not</td></tr>
        </tbody>
      </table>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.6rem;text-align:center">Move the verb one step into the past. Use SAY with no person ("she said that...") and TELL with a person ("she told me that...").</p>
    </div>
  </div>
</div>''')
    # 15 language focus (lf block)
    S.append(f'''<!-- ========== SLIDE 15 ========== -->
<div class="slide slide-light" data-slide="15" data-phase="4" data-teacher="<strong>Language Focus (4 min):</strong> A Lucimara le cada linha e completa a frase relatada. Use como ponte para o erro comum do proximo slide.">
  <div class="slide-inner">
    <div class="chapter-label">Language Focus</div>
    <h2 class="slide-heading">Complete the <span class="accent">Report</span></h2>
    <!--IC-BLOCKS:lf-->
  </div>
</div>''')
    # 16 common mistake
    S.append(f'''<!-- ========== SLIDE 16 ========== -->
<div class="slide slide-light" data-slide="16" data-phase="4" data-teacher="<strong>Common mistake (3 min):</strong> Mostre certo (verde) vs errado (vermelho). Reforce: TELL precisa de pessoa (tell me); SAY nao (say that). E o verbo volta um passo (will -> would). Peca que a Lucimara leia as versoes certas 2 vezes.">
  <div class="slide-inner">
    <div class="chapter-label">Common Mistake</div>
    <h2 class="slide-heading">Right vs <span class="accent">Wrong</span></h2>
    <div style="display:flex;flex-direction:column;gap:1rem;max-width:560px;margin:1.2rem auto 0">
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:.8rem">
        <div style="background:var(--danger-bg);border:1px solid var(--danger-border);border-radius:10px;padding:1rem"><p style="font-size:.78rem;color:var(--danger);font-weight:700;margin-bottom:.3rem">&#10007; WRONG</p><p style="font-size:.88rem">"She said me the city was walkable."</p></div>
        <div style="background:var(--success-bg);border:1px solid var(--success-border);border-radius:10px;padding:1rem"><p style="font-size:.78rem;color:var(--success);font-weight:700;margin-bottom:.3rem">&#10003; RIGHT</p><p style="font-size:.88rem">She <strong>told me</strong> the city was walkable.</p></div>
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:.8rem">
        <div style="background:var(--danger-bg);border:1px solid var(--danger-border);border-radius:10px;padding:1rem"><p style="font-size:.78rem;color:var(--danger);font-weight:700;margin-bottom:.3rem">&#10007; WRONG</p><p style="font-size:.88rem">"He told that I would need a car."</p></div>
        <div style="background:var(--success-bg);border:1px solid var(--success-border);border-radius:10px;padding:1rem"><p style="font-size:.78rem;color:var(--success);font-weight:700;margin-bottom:.3rem">&#10003; RIGHT</p><p style="font-size:.88rem">He <strong>told me that</strong> I would need a car.</p></div>
      </div>
    </div>
    <p style="font-size:.82rem;color:var(--text-dim);margin:1rem auto 0;max-width:500px;text-align:center">TELL always needs a person: tell me, tell her. SAY never takes a person: say that... And move the verb back a step: will becomes would.</p>
  </div>
</div>''')
    # 17 spot the error
    S.append(f'''<!-- ========== SLIDE 17 ========== -->
<div class="slide slide-light" data-slide="17" data-phase="4" data-teacher="<strong>Spot the error (4 min):</strong> A Lucimara le cada frase e diz onde esta o erro ANTES de clicar. Ao clicar, a versao certa aparece em verde. Reforce a estrutura-alvo em cada correcao.">
  <div class="slide-inner">
    <div class="chapter-label">Spot the Error</div>
    <h2 class="slide-heading">Find the <span class="accent">Mistake</span></h2>
    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem">Tap each card to reveal the correction</p>
    <div class="error-grid" style="max-width:600px;margin:1.2rem auto 0">
      <div class="error-card" onclick="revealError(this)"><div class="error-sentence">"She said me the streets were numbered."</div><div class="error-fix">She told me the streets were numbered.</div></div>
      <div class="error-card" onclick="revealError(this)"><div class="error-sentence">"He told that I would need a car."</div><div class="error-fix">He told me that I would need a car.</div></div>
      <div class="error-card" onclick="revealError(this)"><div class="error-sentence">"She said that she will take the subway."</div><div class="error-fix">She said that she would take the subway.</div></div>
      <div class="error-card" onclick="revealError(this)"><div class="error-sentence">"My friend told me the city is walkable."</div><div class="error-fix">My friend told me the city was walkable.</div></div>
    </div>
    <div class="error-score" id="errorScore" style="margin-top:1rem">0 / 4 errors found</div>
  </div>
</div>''')
    # 18 voices transition
    S.append(f'''<!-- ========== SLIDE 18 ========== -->
<div class="slide slide-image" data-slide="18" data-phase="5" data-teacher="<strong>Transicao (1 min):</strong> Ponte para a parte de fala. Diga que agora a Lucimara vai ouvir conselhos reais e relata-los. Passe ao proximo." style="background-image:linear-gradient(rgba(20,12,22,.78),rgba(20,12,22,.9)),url('https://images.unsplash.com/photo-1449824913935-59a10b8d2000?w=1400&q=80');background-size:cover;background-position:center">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label">Chapter 5: Voices</div>
    <h2 class="slide-heading" style="font-size:2rem;color:#fff">Voices on the <span class="accent">Street</span></h2>
    <p style="color:rgba(255,255,255,.82);font-size:1rem;margin-top:.5rem">Hear real advice, then report it in your own words.</p>
  </div>
</div>''')
    # 19 register: from their words to yours
    S.append(f'''<!-- ========== SLIDE 19 ========== -->
<div class="slide slide-light" data-slide="19" data-phase="5" data-teacher="<strong>From direct to reported (4 min):</strong> Mostre a fala direta e peca que a Lucimara a RELATE ANTES de revelar. Reforce say/told e o back-shift do verbo.">
  <div class="slide-inner">
    <div class="chapter-label">From Their Words to Yours</div>
    <h2 class="slide-heading">Report <span class="accent">It</span></h2>
    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem">Read what they said, then tap to see how you report it</p>
    <div class="comp-questions" style="max-width:580px;margin:1.2rem auto 0">
      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">A friend: "The city is walkable."</div><div class="q-answer">She said that the city was walkable.</div></div>
      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">A local: "You will need a car."</div><div class="q-answer">He told me that I would need a car.</div></div>
      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">The app: "Prices are higher now."</div><div class="q-answer">It said that prices were higher then.</div></div>
      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">A colleague: "I can walk to work."</div><div class="q-answer">She said that she could walk to work.</div></div>
    </div>
  </div>
</div>''')
    # 20 dialogue (each line ONE physical line)
    dlines = [
        ('1', 'ellen', 'lucimara', 'L', 'lucimara-bubble',
         'Marcus, before my trip I asked a few friends how to get around, and everyone said something different!'),
        ('2', 'arthur', 'marcus', 'M', 'marcus-bubble',
         'Ha, that sounds right. What did your New York friend tell you?'),
        ('3', 'ellen', 'lucimara', 'L', 'lucimara-bubble',
         'She told me that I would barely need a car, because the city was <span class="vocab-highlight">walkable</span> and the subway ran everywhere.'),
        ('4', 'arthur', 'marcus', 'M', 'marcus-bubble',
         'Smart. And the friend in Los Angeles?'),
        ('5', 'ellen', 'lucimara', 'L', 'lucimara-bubble',
         'He said that I would be lost without a car, and that the <span class="vocab-highlight">urban sprawl</span> went on for miles.'),
        ('6', 'arthur', 'marcus', 'M', 'marcus-bubble',
         'So they told you two opposite things. What did you decide?'),
        ('7', 'ellen', 'lucimara', 'L', 'lucimara-bubble',
         'One friend told me that the smartest travelers always ask a local. So that is exactly what I am doing right now!'),
        ('8', 'arthur', 'marcus', 'M', 'marcus-bubble',
         'Then here is my local tip: take the subway <span class="vocab-highlight">crosstown</span>, and let the app <span class="vocab-highlight">reroute</span> you around any <span class="vocab-highlight">bottleneck</span>.'),
    ]

    def plain(t):
        import re as _re
        return _re.sub('<[^>]+>', '', t)
    dl = []
    for num, voice, who, initial, bubble, text in dlines:
        vis = ' visible' if num == '1' else ''
        spoken = plain(text)
        dl.append(f'      <div class="dialogue-line{vis}" data-line="{num}" data-voice="{voice}"><div class="dialogue-avatar {who}">{initial}</div><div class="dialogue-bubble {bubble}">{text} <span class="audio-inline" onclick="speakText(\'{spoken}\',this)">{LISTEN_ICON}</span></div></div>')
    dialogue = '\n'.join(dl)
    S.append(f'''<!-- ========== SLIDE 20 ========== -->
<div class="slide slide-dark" data-slide="20" data-phase="5" data-teacher="<strong>Dialogo (6 min):</strong> Voce e o Marcus. Click Next Line a cada fala. Para cada fala da Lucimara, peca que ELA fale primeiro, depois toque o audio. Celebre o uso correto de said/told.">
  <div class="slide-inner">
    <div class="chapter-label">Dialogue</div>
    <h2 class="slide-heading" style="color:#fff">Reporting the <span class="accent">Advice</span></h2>
    <div class="dialogue-box" id="dialogueBox">
{dialogue}
    </div>
    <button class="primary-btn" id="nextLineBtn" onclick="nextDialogueLine()" style="margin:1.2rem auto 0;display:block;background:{A};color:#fff;border:none;border-radius:8px;padding:.6rem 1.4rem;font-size:.9rem;font-weight:600;cursor:pointer">Next Line</button>
  </div>
</div>''')
    # 21 dialogue comprehension (about the friends / Marcus = third parties)
    S.append(f'''<!-- ========== SLIDE 21 ========== -->
<div class="slide slide-light" data-slide="21" data-phase="5" data-teacher="<strong>Comprehension (3 min):</strong> Perguntas sobre o que os AMIGOS e o Marcus disseram (REGRA 27F -- nao sobre a Lucimara). A Lucimara tenta antes de revelar; click para mostrar.">
  <div class="slide-inner">
    <div class="chapter-label">Did You Catch It?</div>
    <h2 class="slide-heading">What Did They <span class="accent">Say?</span></h2>
    <div class="comp-questions" style="max-width:560px;margin:1.2rem auto 0">
      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">1. What did the New York friend tell Lucimara?</div><div class="q-answer">That she would barely need a car, because the city was walkable and the subway ran everywhere.</div></div>
      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">2. What did the friend in Los Angeles say?</div><div class="q-answer">That she would be lost without a car, and that the urban sprawl went on for miles.</div></div>
      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">3. What is Marcus's local tip?</div><div class="q-answer">Take the subway crosstown and let the app reroute you around any bottleneck.</div></div>
    </div>
  </div>
</div>''')
    # 22 artifact: text thread
    S.append(f'''<!-- ========== SLIDE 22 ========== -->
<div class="slide slide-light" data-slide="22" data-phase="5" data-teacher="<strong>Documento real (4 min):</strong> De 1 minuto de leitura silenciosa das mensagens. Depois pergunte o que cada amigo disse. NAO peca traducao palavra a palavra.">
  <div class="slide-inner">
    <div class="chapter-label">Text Thread</div>
    <h2 class="slide-heading">Lucimara's <span class="accent">Travel Group Chat</span></h2>
    <div style="max-width:440px;margin:1.2rem auto 0;background:var(--bg-card);border:1px solid var(--border);border-radius:16px;padding:1rem;text-align:left">
      <div style="font-size:.78rem;color:var(--text-dim);text-align:center;border-bottom:1px solid var(--border);padding-bottom:.5rem;margin-bottom:.7rem">Trip Advice &middot; 3 people</div>
      <div style="margin-bottom:.6rem"><div style="font-size:.72rem;color:var(--accent);font-weight:700;margin-bottom:.15rem">Daniel &middot; New York</div><div style="background:var(--bg-elevated);border-radius:12px;padding:.6rem .8rem;font-size:.86rem">Honestly, you will not need a car. The city is walkable and the streets follow a grid system, so they are easy to find.</div></div>
      <div style="margin-bottom:.6rem"><div style="font-size:.72rem;color:var(--accent);font-weight:700;margin-bottom:.15rem">Paula &middot; Los Angeles</div><div style="background:var(--bg-elevated);border-radius:12px;padding:.6rem .8rem;font-size:.86rem">Opposite here! Most people drive or carpool. Watch out for surge pricing on the apps at rush hour.</div></div>
      <div style="margin-bottom:.2rem"><div style="font-size:.72rem;color:var(--accent);font-weight:700;margin-bottom:.15rem">Rosa &middot; Chicago</div><div style="background:var(--bg-elevated);border-radius:12px;padding:.6rem .8rem;font-size:.86rem">Whatever city you land in, ask a local first. They always know the fastest crosstown route.</div></div>
    </div>
  </div>
</div>''')
    # 23 artifact comprehension
    S.append(f'''<!-- ========== SLIDE 23 ========== -->
<div class="slide slide-light" data-slide="23" data-phase="5" data-teacher="<strong>Comprehension do documento (3 min):</strong> A Lucimara RELATA o que cada amigo disse ANTES de clicar para revelar. Volte as mensagens para justificar com said/told.">
  <div class="slide-inner">
    <div class="chapter-label">Report the Chat</div>
    <h2 class="slide-heading">Who Said <span class="accent">What?</span></h2>
    <div class="comp-questions" style="max-width:560px;margin:1.2rem auto 0">
      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">1. Report what Daniel said about New York.</div><div class="q-answer">He said that the city was walkable and that the streets followed a grid system.</div></div>
      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">2. Report Paula's warning about the apps in Los Angeles.</div><div class="q-answer">She told me that there was surge pricing on the apps at rush hour.</div></div>
      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">3. Report Rosa's advice for any city.</div><div class="q-answer">She said that I should always ask a local, because they knew the fastest crosstown route.</div></div>
    </div>
  </div>
</div>''')
    # 24, 25 listening players
    def listening_slide(num, mpid, wfid, qid, src, title, subtitle, questions):
        bars = ''.join('<div class="bar"></div>' for _ in range(20))
        qs = '\n'.join(
            f'      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">{q}</div><div class="q-answer">{a}</div></div>'
            for q, a in questions)
        return f'''<!-- ========== SLIDE {num} ========== -->
<div class="slide slide-dark" data-slide="{num}" data-phase="5" data-teacher="<strong>Listening (5 min):</strong> Leia as perguntas EM VOZ ALTA COM a Lucimara ANTES de tocar (elas ja estao na tela). Toque SEM texto, 2 vezes. Use 0.75x se ela pedir.">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label">Listening {1 if num==24 else 2}</div>
    <h2 class="slide-heading" style="color:#fff">{title}</h2>
    <p style="color:rgba(255,255,255,.78);font-size:.9rem;margin-bottom:1rem">{subtitle} Sound first -- no text.</p>
    <div class="waveform waveform-paused" id="{wfid}">{bars}</div>
    <div class="mock-player" id="{mpid}" data-src="/audio/lucimara-miyuki-ito/{src}" data-waveform="{wfid}" data-questions="{qid}" style="max-width:460px;margin:.8rem auto 0">
      <div class="lp-seekbar" onclick="mpSeek(event,'{mpid}')" style="width:100%;height:6px;background:rgba(255,255,255,.12);border-radius:3px;cursor:pointer;position:relative"><div class="lp-progress" id="progress-{mpid}" style="width:0%;height:100%;background:var(--accent-light);border-radius:3px;transition:width .1s"></div></div>
      <div style="display:flex;justify-content:space-between;margin:.4rem 0 .6rem"><span id="time-current-{mpid}" style="font-size:.72rem;color:rgba(255,255,255,.78)">0:00</span><span id="time-total-{mpid}" style="font-size:.72rem;color:rgba(255,255,255,.78)">0:00</span></div>
      <div style="display:flex;align-items:center;justify-content:center;gap:1rem;margin-bottom:.6rem">
        <button class="lp-btn" onclick="mpSkip('{mpid}',-5)" aria-label="Back 5 seconds" style="background:transparent;border:1px solid rgba(255,255,255,.3);color:#fff;border-radius:50%;width:38px;height:38px;cursor:pointer;font-size:.65rem;font-weight:700">-5s</button>
        <button class="lp-btn lp-play" id="play-{mpid}" onclick="mpToggle('{mpid}')" aria-label="Play or pause" style="background:var(--accent);border:none;color:#fff;border-radius:50%;width:48px;height:48px;cursor:pointer"><svg class="lp-icon-play" viewBox="0 0 24 24" width="18" height="18"><polygon points="5 3 19 12 5 21 5 3" fill="currentColor"/></svg><svg class="lp-icon-pause" viewBox="0 0 24 24" width="18" height="18" style="display:none"><rect x="6" y="4" width="4" height="16" fill="currentColor"/><rect x="14" y="4" width="4" height="16" fill="currentColor"/></svg></button>
        <button class="lp-btn" onclick="mpSkip('{mpid}',5)" aria-label="Forward 5 seconds" style="background:transparent;border:1px solid rgba(255,255,255,.3);color:#fff;border-radius:50%;width:38px;height:38px;cursor:pointer;font-size:.65rem;font-weight:700">+5s</button>
      </div>
      <div style="display:flex;gap:.4rem;justify-content:center">
        <button class="lp-speed-btn" onclick="mpSpeed('{mpid}',0.5,this)" style="background:transparent;border:1px solid rgba(255,255,255,.25);color:rgba(255,255,255,.82);border-radius:6px;padding:.2rem .6rem;font-size:.7rem;cursor:pointer">0.5x</button>
        <button class="lp-speed-btn" onclick="mpSpeed('{mpid}',0.75,this)" style="background:transparent;border:1px solid rgba(255,255,255,.25);color:rgba(255,255,255,.82);border-radius:6px;padding:.2rem .6rem;font-size:.7rem;cursor:pointer">0.75x</button>
        <button class="lp-speed-btn lp-speed-active" onclick="mpSpeed('{mpid}',1,this)" style="background:var(--accent);border:1px solid var(--accent);color:#fff;border-radius:6px;padding:.2rem .6rem;font-size:.7rem;cursor:pointer">1x</button>
        <button class="lp-speed-btn" onclick="mpSpeed('{mpid}',1.25,this)" style="background:transparent;border:1px solid rgba(255,255,255,.25);color:rgba(255,255,255,.82);border-radius:6px;padding:.2rem .6rem;font-size:.7rem;cursor:pointer">1.25x</button>
      </div>
    </div>
    <div class="comp-questions" id="{qid}" style="max-width:520px;margin:1.2rem auto 0">
{qs}
    </div>
  </div>
</div>'''
    S.append(listening_slide(
        24, 'mp-listen1', 'waveform1', 'listening1Qs', 'a16_listening_voicemail.mp3',
        'A Friend&#39;s <span class="accent">Voicemail</span>',
        'A friend leaves advice about getting around the city.',
        [("1. What does Sofia say about getting around downtown?",
          "It is completely walkable, so you will not need a car for most of the trip."),
         ("2. What warning does she give about rideshare at rush hour?",
          "The app uses surge pricing, so you will pay a lot more."),
         ("3. What does she suggest for crosstown trips?",
          "Walk or take the subway; the app will reroute you around the bottleneck.")]))
    S.append(listening_slide(
        25, 'mp-listen2', 'waveform2', 'listening2Qs', 'a16_listening_grammartip.mp3',
        'How to <span class="accent">Report It</span>',
        'A short tip on reporting what people said.',
        [("1. When you report what someone said, what usually happens to the verb?",
          "It moves one step into the past (present becomes past)."),
         ("2. What do 'will' and 'can' become in reported speech?",
          "'will' becomes 'would' and 'can' becomes 'could'."),
         ("3. What is the difference between 'say' and 'tell'?",
          "'say' takes no person (she said that); 'tell' needs a person (she told me that).")]))
    # 26 pronunciation
    pron = [
        ("She told me that the city was walkable.", "link 'told me' -- TOALD-mee; keep 'that' light."),
        ("He said that I would need a car.", "'would' is short -- wud; stress NEED."),
        ("My friend explained that the streets were numbered.", "ex-PLAINED; 'were' stays weak -- wer."),
        ("They said that prices went up at rush hour.", "link 'went up' -- WEN-tup; RUSH-hour."),
    ]
    pcards = ''
    for ph, tip in pron:
        pcards += (f'      <div style="display:flex;justify-content:space-between;align-items:center;gap:.8rem;background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:.9rem 1.1rem"><div style="text-align:left"><p style="font-size:.95rem;font-weight:600">"{ph}"</p><p style="font-size:.78rem;color:var(--text-dim);margin-top:.2rem">{tip}</p></div>{listen_btn(ph)}</div>\n')
    S.append(f'''<!-- ========== SLIDE 26 ========== -->
<div class="slide slide-light" data-slide="26" data-phase="5" data-teacher="<strong>Say it naturally (4 min):</strong> Toque cada frase, aponte a fala conectada (linking) e peca que a Lucimara repita 2 vezes. Foco na naturalidade.">
  <div class="slide-inner">
    <div class="chapter-label">Pronunciation</div>
    <h2 class="slide-heading">Say It <span class="accent">Naturally</span></h2>
    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem">Listen for the linking, then repeat twice</p>
    <div style="display:flex;flex-direction:column;gap:.7rem;max-width:560px;margin:1.2rem auto 0">
{pcards}    </div>
  </div>
</div>''')
    # 27 your turn transition
    S.append(f'''<!-- ========== SLIDE 27 ========== -->
<div class="slide slide-image" data-slide="27" data-phase="6" data-teacher="<strong>Transicao (1 min):</strong> Ponte para a producao livre. Diga que agora a Lucimara assume e relata os conselhos sozinha. Passe ao proximo." style="background-image:linear-gradient(rgba(20,12,22,.78),rgba(20,12,22,.9)),url('https://images.unsplash.com/photo-1519677100203-a0e668c92439?w=1400&q=80');background-size:cover;background-position:center">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label">Chapter 6: Your Turn</div>
    <h2 class="slide-heading" style="font-size:2rem;color:#fff">Now You <span class="accent">Report</span></h2>
    <p style="color:rgba(255,255,255,.82);font-size:1rem;margin-top:.5rem">Your turn: pass on the advice you heard, out loud.</p>
  </div>
</div>''')
    # 28 quickfire
    S.append(f'''<!-- ========== SLIDE 28 ========== -->
<div class="slide slide-light" data-slide="28" data-phase="6" data-teacher="<strong>Quick fire (5 min):</strong> Uma situacao por vez. A Lucimara relata em voz alta com said/told e back-shift, SEM ver as tips. Use Tips so se ela travar. Navegue com Previous/Next.">
  <div class="slide-inner">
    <div class="chapter-label">Quick Fire</div>
    <h2 class="slide-heading">Report on Your <span class="accent">Feet</span></h2>
    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem">One quote at a time &mdash; report it out loud, then check the tips</p>
    <!--IC-BLOCKS:quickfire-->
  </div>
</div>''')
    # 29 scenarios
    S.append(f'''<!-- ========== SLIDE 29 ========== -->
<div class="slide slide-light" data-slide="29" data-phase="6" data-teacher="<strong>Scenarios (5 min):</strong> Para cada cena, a Lucimara produz a resposta em voz alta usando reported speech. Sem gabarito visivel; ela produz.">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 6: Your Turn</div>
    <h2 class="slide-heading">Pass It <span class="accent">On</span></h2>
    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem">From guided to free &mdash; say each one out loud</p>
    <!--IC-BLOCKS:practice-->
  </div>
</div>''')
    # 30 answer key
    S.append(f'''<!-- ========== SLIDE 30 ========== -->
<div class="slide slide-light" data-slide="30" data-phase="6" data-teacher="<strong>Answer key (2 min):</strong> O accordion fica fechado. A Lucimara so clica depois de tentar o gap-fill e os cenarios. Controle do professor (toggle); use para conferir.">
  <div class="slide-inner">
    <div class="chapter-label">Check Your Work</div>
    <h2 class="slide-heading">Model <span class="accent">Answers</span></h2>
    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin:.3rem auto 0;max-width:480px">Try the gap-fill and the scenarios first. Reveal the key only to compare.</p>
    <div style="max-width:560px;margin:1rem auto 0">
      <!--IC-BLOCKS:answerkey-->
    </div>
  </div>
</div>''')
    # 31-33 roleplays
    S.append(f'''<!-- ========== SLIDE 31 ========== -->
<div class="slide slide-light" data-slide="31" data-phase="6" data-teacher="Role-play guiado (4 min): Voce e um colega curioso. A Lucimara relata o que UM amigo disse sobre Nova York. Deixe-a produzir com calma; corrija so no fim.">
  <div class="slide-inner">
    <div class="chapter-label">Role-Play 1 of 3 &mdash; Guided</div>
    <h2 class="slide-heading">Pass On the <span class="accent">New York Tip</span></h2>
    <div class="roleplay-body" style="max-width:500px;margin:1rem auto 0;background:linear-gradient(135deg,rgba(91,45,95,.12),rgba(91,45,95,.03));border:1px solid {A};border-radius:12px;padding:1.5rem">
      <p class="roleplay-scenario" style="font-size:.9rem;margin-bottom:1rem"><strong>Scenario:</strong> A colleague asks what your New York friend told you. Report two things using "She told me that..." and a past-tense verb.</p>
      <div style="display:flex;flex-wrap:wrap;gap:.5rem;justify-content:center"><span style="border:1px solid {A};color:{A};border-radius:20px;padding:.3rem .9rem;font-size:.82rem">She told me that</span><span style="border:1px solid {A};color:{A};border-radius:20px;padding:.3rem .9rem;font-size:.82rem">walkable</span><span style="border:1px solid {A};color:{A};border-radius:20px;padding:.3rem .9rem;font-size:.82rem">would not need</span></div>
    </div>
  </div>
</div>''')
    S.append(f'''<!-- ========== SLIDE 32 ========== -->
<div class="slide slide-light" data-slide="32" data-phase="6" data-teacher="Role-play semi-livre (4 min): Menos apoio. A Lucimara relata o aviso de Los Angeles sozinha. Anote os acertos.">
  <div class="slide-inner">
    <div class="chapter-label">Role-Play 2 of 3 &mdash; Semi-free</div>
    <h2 class="slide-heading">Report the <span class="accent">LA Warning</span></h2>
    <div class="roleplay-body" style="max-width:500px;margin:1rem auto 0;background:linear-gradient(135deg,rgba(91,45,95,.12),rgba(91,45,95,.03));border:1px solid {A};border-radius:12px;padding:1.5rem">
      <p class="roleplay-scenario" style="font-size:.9rem;margin-bottom:1rem"><strong>Scenario:</strong> A friend is about to visit Los Angeles. Report what your LA friend told you about cars and rideshare apps. Use "He said that..." and back-shift the verbs.</p>
      <div style="display:flex;flex-wrap:wrap;gap:.5rem;justify-content:center"><span style="border:1px solid {A};color:{A};border-radius:20px;padding:.3rem .9rem;font-size:.82rem">He said that</span><span style="border:1px solid {A};color:{A};border-radius:20px;padding:.3rem .9rem;font-size:.82rem">carpool</span><span style="border:1px solid {A};color:{A};border-radius:20px;padding:.3rem .9rem;font-size:.82rem">surge pricing</span></div>
    </div>
  </div>
</div>''')
    S.append(f'''<!-- ========== SLIDE 33 ========== -->
<div class="slide slide-light" data-slide="33" data-phase="6" data-teacher="Pratica livre (5 min): ZERO pistas. NAO interrompa; anote os erros para o feedback. CELEBRE muito.">
  <div class="slide-inner">
    <div class="chapter-label">Role-Play 3 of 3 &mdash; Free</div>
    <h2 class="slide-heading">Report the Whole <span class="accent">Group Chat</span></h2>
    <div class="roleplay-body" style="max-width:500px;margin:1rem auto 0;background:linear-gradient(135deg,rgba(91,45,95,.12),rgba(91,45,95,.03));border:1px solid {A};border-radius:12px;padding:1.5rem">
      <p class="roleplay-scenario" style="font-size:.9rem;margin-bottom:1rem"><strong>Scenario:</strong> Tell a friend about the advice from all three people in your group chat. Report at least three statements, using both "said" and "told me" correctly.</p>
      <p style="font-size:.85rem;color:var(--text-dim);font-style:italic">No keywords. The report is yours!</p>
    </div>
  </div>
</div>''')
    # 34 survival
    surv = [
        "She told me that the city was walkable.",
        "He said that I would need a car.",
        "My friend told me that the subway ran all night.",
        "They said that prices went up at rush hour.",
        "A local told me that I could walk everywhere.",
    ]
    sitems = ''
    for i, ph in enumerate(surv, 1):
        sitems += (f'      <div class="survival-item-ic"><div class="survival-num-ic">{i}</div><div class="survival-text-ic">"{ph}"</div><button class="audio-btn-sm" onclick="speakText(\'{ph}\',this)">{LISTEN_ICON}</button></div>\n')
    S.append(f'''<!-- ========== SLIDE 34 ========== -->
<div class="slide slide-dark" data-slide="34" data-phase="7" data-teacher="<strong>Survival lines (3 min):</strong> Leia cada frase, toque o audio e peca que a Lucimara repita. Sao as frases-chave da aula.">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label">Chapter 7: Wrap-Up</div>
    <h2 class="slide-heading" style="color:#fff">Report Like a <span class="accent">Local</span></h2>
    <div class="survival-grid" style="max-width:560px;margin:1.5rem auto 0">
{sitems}    </div>
  </div>
</div>''')
    # 35 checklist
    checks = [
        "I can report a statement using 'said (that)' and back-shift the verb.",
        "I know that 'tell' needs a person (tell me) and 'say' does not (say that).",
        "I can change will to would and can to could in reported speech.",
        "I can report advice I received about getting around a city.",
        "I know the words: walkable, grid system, urban sprawl, to carpool, surge pricing, bike lane, to reroute, bottleneck, crosstown, on foot, toll booth, to flag down.",
    ]
    citems = ''
    for c in checks:
        citems += (f'      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg></div>{c}</div>\n')
    S.append(f'''<!-- ========== SLIDE 35 ========== -->
<div class="slide slide-dark" data-slide="35" data-phase="7" data-teacher="<strong>Checklist (2 min):</strong> Diga: click each item if you feel confident. Leia cada item. Os 5 checks = aula completa e stamp no passaporte.">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label">Self-Assessment</div>
    <h2 class="slide-heading" style="color:#fff">What I <span class="accent">Learned</span></h2>
    <div class="check-grid" id="checklist-16" style="max-width:560px;margin:1.2rem auto 0;display:flex;flex-direction:column;gap:.5rem;text-align:left">
{citems}    </div>
  </div>
</div>''')
    # 36 closing
    S.append(f'''<!-- ========== SLIDE 36 ========== -->
<div class="slide slide-dark" data-slide="36" data-phase="7" data-teacher="<strong>Encerramento (2 min):</strong> Parabenize a Lucimara e entregue o badge. Passe o homework ORALMENTE (gravar 90s relatando o conselho de um amigo com reported speech; ouvir um episodio e anotar 3 frases; estudar o vocab). Proxima aula: Checking In, Speaking Up.">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label">Lesson Complete</div>
    <div class="badge-card">
      <div class="badge-icon">
        <div class="badge-circle"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="10" r="3"/><path d="M12 2a8 8 0 00-8 8c0 5.4 8 12 8 12s8-6.6 8-12a8 8 0 00-8-8z"/></svg></div>
        <div class="sparkles"><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div></div>
      </div>
      <h2 class="slide-heading" style="color:#fff">Local Insider Badge <span class="accent">Earned!</span></h2>
      <p style="color:rgba(255,255,255,.78);font-size:1rem;margin-top:.5rem">You can take any advice a local gives you and report it clearly -- said, told, and every verb one step into the past. Well done, Lucimara.</p>
      <p style="color:rgba(255,255,255,.82);font-size:.85rem;margin-top:1.5rem">Lesson 16 -- Complete.</p>
      <p style="color:var(--accent-light);font-size:.9rem;margin-top:.5rem">Next lesson: Checking In, Speaking Up</p>
    </div>
  </div>
</div>''')
    return '\n\n'.join(S) + '\n'


# ---------------------------------------------------------------- PRECLASS
def rot(lst, k):
    k %= len(lst)
    return lst[k:] + lst[:k]


def build_preclass():
    N = 16
    defs = [v[1] for v in VOCAB]
    # vocab cards
    vcards = ''
    for word, d, ex, _, _ in VOCAB:
        vcards += (f'        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header"><span class="vocab-card-word">{word}</span><span class="vocab-card-dot"> -- </span><span class="vocab-card-def">{d}</span></div><div class="vocab-card-example">{ex}</div></div><button class="audio-btn" onclick="speakText(\'{word}\',this)">Listen</button></div>\n')
    # matching (shuffled per row)
    mrows = ''
    for i, (word, d, _, _, _) in enumerate(VOCAB):
        opts = rot(defs, (i * 5 + 3))
        # ensure correct answer not at same visual index as row -> rotation guarantees
        optshtml = '<option value="">Select...</option>' + ''.join(
            f'<option value="{o}">{o}</option>' for o in opts)
        mrows += (f'        <div class="match-row" data-answer="{d}"><span class="match-word" style="flex:0 0 150px">{word}</span><select style="flex:1;width:100%" onchange="checkMatch(this)">{optshtml}</select></div>\n')
    # grammar in context text
    gic_text = ('Before her trip, Lucimara asked her friends how to get around. Her New York friend '
                '<strong>said that</strong> the city <strong>was</strong> walkable, so she could walk or take the subway. '
                'Her friend in Los Angeles <strong>told her that</strong> she <strong>would</strong> need a car, because the '
                'urban sprawl went on for miles. The app, he said, <strong>raised</strong> prices with surge pricing at rush hour. '
                'In the end, one friend <strong>told her that</strong> the smartest travelers always ask a local first.')
    # fill blanks
    blanks = [
        ("She said that the city was ", "walkable", "Hint: easy to get around on foot",
         "She said that the city was walkable.", " downtown."),
        ("He told ", "me", "Hint: TELL always needs a person",
         "He told me that I would need a car.", " that I would need a car."),
        ("She said that she ", "lived", "Hint: back-shift the verb 'live' to the past",
         "She said that she lived in New York.", " in New York."),
        ("He told me that I ", "would", "Hint: 'will' becomes this in reported speech",
         "He told me that I would love the ferry.", " love the ferry."),
        ("The app raised prices with ", "surge", "Hint: higher prices when demand is high",
         "The app raised prices with surge pricing at rush hour.", " pricing at rush hour."),
        ("She said that I ", "could", "Hint: 'can' becomes this in reported speech",
         "She said that I could walk everywhere downtown.", " walk everywhere downtown."),
    ]
    bhtml = ''
    for pre, ans, hint, phrase, post in blanks:
        bhtml += (f'      <div class="fill-blank-item"><div class="fill-blank-sentence">"{pre}<input class="blank-input" data-answer="{ans}" data-hint="{hint}" data-phrase="{phrase}" placeholder="___">{post}"</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>\n')
    # order steps
    order = [
        (1, "Listen carefully to what the person tells you."),
        (2, "Notice the exact words: is it a fact, a 'will', or a 'can'?"),
        (3, "Choose your reporting verb: say (no person) or tell (a person)."),
        (4, "Move the verb one step into the past."),
        (5, "Report it to someone else in a full sentence."),
    ]
    display_order = [order[2], order[4], order[0], order[3], order[1]]
    ohtml = ''
    for o, text in display_order:
        ohtml += (f'        <div class="order-item" draggable="true" data-order="{o}" onclick="selectOrderItem(this,\'order-l{N}\')"><span class="order-num">?</span><span class="order-text">{text}</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l{N}\')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,\'order-l{N}\')">&#9660;</button></span></div>\n')
    # speech cards
    speech = [
        "She told me that the city was walkable.",
        "He said that I would need a car.",
        "My friend explained that the streets were numbered.",
        "They told me that prices went up at rush hour.",
        "She said that I could walk everywhere downtown.",
    ]
    shtml = ''
    for ph in speech:
        shtml += (f'''      <div class="speech-card" data-phrase="{ph}">
        <div class="speech-phrase">{ph}</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
''')
    # survival
    surv = [
        "She told me that the city was walkable.",
        "He said that I would need a car.",
        "My friend told me that the subway ran all night.",
        "They said that prices went up at rush hour.",
        "A local told me that I could walk everywhere.",
    ]
    survhtml = ''
    for i, ph in enumerate(surv, 1):
        survhtml += (f'      <div class="survival-phrase"><span class="sp-num">{i}</span><span class="sp-en">{ph}</span><button class="btn btn-listen" onclick="speakText(\'{ph}\',this)">&#9835;</button></div>\n')

    html = f'''<div class="lesson-card" id="ex-lesson-{N}">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1524850011238-e3d235c7d4c9?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson {N} -- Pre-class</div>
      <h3>Getting Around Like a Local</h3>
      <div class="lesson-desc">How different American cities move -- and how to report the travel advice a local gives you. Key words: walkable, grid system, urban sprawl, to carpool, surge pricing, bike lane, to reroute, bottleneck, crosstown, on foot, toll booth, to flag down. Structure: reported speech (said / told + verb one step into the past).</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="{N}" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="{N}">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each word and read the example. Tap Listen to hear it.</p>
      <div class="vocab-cards">
{vcards}      </div>
    </div>
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each word with the correct definition.</p>
      <div class="match-grid" id="match-l{N}">
{mrows}      </div>
    </div>
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text and answer the questions.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>{gic_text}</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. In "She said that the city was walkable", why is the verb "was" and not "is"?</div><div class="quiz-options">
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> In reported speech the verb moves one step into the past.</div>
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Because the city is not walkable anymore.</div>
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because "say" is always followed by "was".</div>
</div></div>
      <div class="quiz-item"><div class="quiz-question">2. The text uses "told her that" and "said that". What is the difference?</div><div class="quiz-options">
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> They mean exactly the same and follow the same pattern.</div>
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "tell" needs a person (told her); "say" does not (said that).</div>
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "say" needs a person; "tell" does not.</div>
</div></div>
      <div class="quiz-item"><div class="quiz-question">3. The direct words were "You will need a car." Which report is correct?</div><div class="quiz-options">
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> He told her that she would need a car.</div>
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> He told that she will need a car.</div>
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> He said her that she would need a car.</div>
</div></div>
    </div>
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Reported Speech</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">How to report what someone said to you.</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Direct speech</th><th style="padding:.7rem;text-align:left">Reported speech</th><th style="padding:.7rem;text-align:left">Change</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border);"><td style="padding:.6rem">"I <strong>live</strong> here."</td><td style="padding:.6rem">She said that she <strong>lived</strong> there.</td><td style="padding:.6rem">present &rarr; past</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated);"><td style="padding:.6rem">"You <strong>will</strong> need a car."</td><td style="padding:.6rem">He told me that I <strong>would</strong> need a car.</td><td style="padding:.6rem">will &rarr; would</td></tr>
          <tr style="border-bottom:1px solid var(--border);"><td style="padding:.6rem">"You <strong>can</strong> walk."</td><td style="padding:.6rem">She said that I <strong>could</strong> walk.</td><td style="padding:.6rem">can &rarr; could</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated);"><td style="padding:.6rem">say / tell</td><td style="padding:.6rem"><strong>said (that)</strong> &middot; <strong>told me (that)</strong></td><td style="padding:.6rem">tell needs a person; say does not</td></tr>
        </tbody>
      </table></div>
    </div>
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the correct word. Tap Listen to hear the whole sentence.</p>
{bhtml}    </div>
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Steps in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the steps for reporting someone's advice in the correct order.</p>
      <div class="order-container" id="order-l{N}">
{ohtml}      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l{N}')">Check Order</button>
    </div>
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it.</p>
{shtml}    </div>
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best way to report what each person said.</p>
      <div class="quiz-item"><div class="quiz-question">Your friend said: "I live in New York." You report:</div><div class="quiz-options">
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> She said that she lived in New York.</div>
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> She said that she live in New York.</div>
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> She said me that she lived in New York.</div>
</div></div>
      <div class="quiz-item"><div class="quiz-question">A local said: "You will need a car." You report:</div><div class="quiz-options">
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> He told me that I would need a car.</div>
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> He told that I would need a car.</div>
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> He said me that I will need a car.</div>
</div></div>
      <div class="quiz-item"><div class="quiz-question">The app said: "Prices are high now." You report:</div><div class="quiz-options">
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> It said that prices were high then.</div>
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> It said that prices are high now.</div>
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> It told that prices were high.</div>
</div></div>
      <div class="quiz-item"><div class="quiz-question">Which sentence is correct?</div><div class="quiz-options">
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> She told me that she could drive.</div>
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> She said me that she could drive.</div>
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> She told that she could drive.</div>
</div></div>
    </div>
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. There is no right or wrong answer.</p>
      <div class="think-card">
        <div class="think-question">Think of three tips a friend once gave you about getting around a city. Record a one-minute answer reporting what they said. Use "She told me that..." and "He said that..." at least once each, and move the verbs one step into the past. Take your time.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-{N}"></div>
      </div>
    </div>
    <div class="survival-card">
      <h4>Survival Card -- Lesson {N}</h4>
{survhtml}    </div>
  </div>
</div>
'''
    return html


if __name__ == '__main__':
    open(os.path.join(HERE, 'slides.html'), 'w', encoding='utf-8').write(build_slides())
    open(os.path.join(HERE, 'preclass.html'), 'w', encoding='utf-8').write(build_preclass())
    print('wrote slides.html + preclass.html')
