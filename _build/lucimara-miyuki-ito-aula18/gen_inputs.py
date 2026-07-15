# -*- coding: utf-8 -*-
"""Authoring helper for lucimara-miyuki-ito aula 18 (second conditional, reading model).
Emits slides.html + preclass.html into this dir. Shares vocab data so IN CLASS and
Pre-class stay identical. Input to build_from_model.py -- NOT a build contorno."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))

ACCENT = "#5B2D5F"

# word, definition, example (display-only), icon gradient, icon svg inner
VOCAB = [
    ("Server", "the person who takes your order and brings your food",
     '"The server told us about the daily specials before we ordered."',
     "#0e7490,#22d3ee", '<path d="M12 3v2M7 21h10M12 5a6 6 0 016 6H6a6 6 0 016-6zM4 11h16"/>'),
    ("Daily special", "a dish the restaurant offers only that day, not on the regular menu",
     '"If they had a fish daily special, I would definitely try it."',
     "#b45309,#f59e0b", '<path d="M12 2l2.4 4.9 5.4.8-3.9 3.8.9 5.4L12 15l-4.8 2.5.9-5.4L4.2 8.3l5.4-.8z"/>'),
    ("House specialty", "the dish a restaurant is most famous for",
     '"She said the slow-cooked short rib was the house specialty."',
     "#4338ca,#818cf8", '<path d="M3 21h18M5 21V8l7-5 7 5v13M9 21v-6h6v6"/>'),
    ("To eat out", "to have a meal in a restaurant instead of at home",
     '"When I travel, I love to eat out and try the local food."',
     "#0d9488,#2dd4bf", '<path d="M4 3v7a2 2 0 002 2h0v9M6 3v6M18 3c-1.5 0-2 2-2 4s.5 4 2 4v9"/>'),
    ("To go with", "to choose something from the menu",
     '"I think I will go with the grilled salmon."',
     "#b91c1c,#f87171", '<path d="M9 6l6 6-6 6M5 6l6 6-6 6"/>'),
    ("To split the check", "to divide the bill so each person pays a share",
     '"We are old friends, so we always split the check."',
     "#15803d,#4ade80", '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 8h8M8 12h8M8 16h5M12 3v18"/>'),
    ("Leftovers", "the food you do not finish and take home to eat later",
     '"The portion was huge, so I took the leftovers home."',
     "#9f1239,#fb7185", '<path d="M5 8h14l-1 12a2 2 0 01-2 2H8a2 2 0 01-2-2zM9 8V6a3 3 0 016 0v2"/>'),
    ("On the house", "free, paid for by the restaurant",
     '"The dessert was on the house because it was my birthday."',
     "#c2410c,#fb923c", '<path d="M3 11l9-7 9 7M5 10v10h14V10M9 20v-6h6v6"/>'),
    ("Allergen", "a food that can cause an allergic reaction, like nuts or shellfish",
     '"I always ask about allergens because I cannot eat nuts."',
     "#7c3aed,#a78bfa", '<circle cx="12" cy="12" r="9"/><path d="M12 8v4M12 16h.01"/>'),
    ("Dressing on the side", "salad sauce served separately so you add your own amount",
     '"Could I have the dressing on the side, please?"',
     "#0369a1,#38bdf8", '<path d="M6 3h8l1 4H5zM6 7l1 12a2 2 0 002 2h2a2 2 0 002-2l1-12M17 5h3v6h-3"/>'),
    ("Well-done", "cooked all the way through, with no pink inside",
     '"He ordered his steak well-done."',
     "#ca8a04,#fde047", '<path d="M4 13a8 8 0 0116 0M4 13h16M6 17h12M9 21h6"/>'),
    ("Happy hour", "a time when drinks and snacks cost less",
     '"If we arrived before seven, we would catch happy hour."',
     "#1d4ed8,#60a5fa", '<path d="M5 3h14l-6 8v6h3M11 17H8m-3-8l6 8M12 3v0"/>'),
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
<div class="slide slide-image active" data-slide="1" data-phase="1" data-teacher="<strong>Abertura (2 min):</strong> Compartilhe a tela. NAO cumprimente de forma scriptada (REGRA 27A). Va direto ao tema: hoje a Lucimara vai pedir comida com confianca num restaurante americano e imaginar cenarios com o second conditional." style="background-image:linear-gradient(rgba(20,12,22,.78),rgba(20,12,22,.9)),url('https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=1400&q=80');background-size:cover;background-position:center">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label">Lesson 18 &middot; Ordering with Confidence</div>
    <h1 class="slide-heading" style="font-size:2.4rem;color:#fff">Ordering with <span class="accent">Confidence</span></h1>
    <p style="color:rgba(255,255,255,.85);font-size:1.05rem;margin-top:1rem">A New York table, a business guest, and a menu you can handle. Learn the words, then imagine any meal with the second conditional.</p>
  </div>
</div>''')
    # 2 warm-up (callback aula17 hotels)
    S.append(f'''<!-- ========== SLIDE 2 ========== -->
<div class="slide slide-dark" data-slide="2" data-phase="1" data-teacher="<strong>Warm-up + callback (3 min):</strong> Ponte com a aula 17 (hoteis, pedir com educacao). Faca a pergunta do slide e deixe a Lucimara falar de uma refeicao memoravel no exterior. ZERO correcao aqui.">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label">Warm-Up</div>
    <h2 class="slide-heading" style="color:#fff">A Meal You Still <span class="accent">Remember</span></h2>
    <p style="color:rgba(255,255,255,.82);font-size:1rem;margin:1rem auto 0;max-width:600px">Last time you spoke up at a hotel front desk. Today you sit down at a restaurant. You will read the specials, ask about what is in a dish, send something back if you need to, and split the check, all without switching to Portuguese. And you will learn to imagine any meal: if you could eat anywhere tonight, where would you go?</p>
    <p style="color:var(--accent-light);font-size:.92rem;margin-top:1.3rem">In one sentence: what is the best meal you have ever had abroad, and did you get exactly what you expected?</p>
  </div>
</div>''')
    # 3 agenda
    S.append(f'''<!-- ========== SLIDE 3 ========== -->
<div class="slide slide-light" data-slide="3" data-phase="1" data-teacher="<strong>Agenda (1 min):</strong> Apresente as tres missoes. Tom caloroso e direto. Passe ao proximo.">
  <div class="slide-inner">
    <div class="chapter-label">Today</div>
    <h2 class="slide-heading">Three <span class="accent">Missions</span></h2>
    <div style="display:flex;flex-direction:column;gap:.8rem;max-width:540px;margin:1.4rem auto 0">
      <div style="display:flex;gap:.9rem;align-items:center;background:var(--bg-card);border:1px solid var(--border);border-radius:12px;padding:1rem 1.2rem"><div style="width:34px;height:34px;border-radius:9px;background:{A};color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;flex-shrink:0">1</div><p style="font-size:.95rem">Learn the words of an American restaurant table.</p></div>
      <div style="display:flex;gap:.9rem;align-items:center;background:var(--bg-card);border:1px solid var(--border);border-radius:12px;padding:1rem 1.2rem"><div style="width:34px;height:34px;border-radius:9px;background:{A};color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;flex-shrink:0">2</div><p style="font-size:.95rem">Use the second conditional to imagine any meal.</p></div>
      <div style="display:flex;gap:.9rem;align-items:center;background:var(--bg-card);border:1px solid var(--border);border-radius:12px;padding:1rem 1.2rem"><div style="width:34px;height:34px;border-radius:9px;background:{A};color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;flex-shrink:0">3</div><p style="font-size:.95rem">Order for yourself and a guest, out loud and confidently.</p></div>
    </div>
  </div>
</div>''')
    # 4 vocab transition
    S.append(f'''<!-- ========== SLIDE 4 ========== -->
<div class="slide slide-image" data-slide="4" data-phase="2" data-teacher="<strong>Transicao vocab (1 min):</strong> Diga: doze palavras e expressoes novas sobre pedir comida. Click each card to reveal. Passe ao proximo." style="background-image:linear-gradient(rgba(20,12,22,.78),rgba(20,12,22,.9)),url('https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=1400&q=80');background-size:cover;background-position:center">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label">Chapter 2: Menu Words</div>
    <h2 class="slide-heading" style="font-size:2rem;color:#fff">Words at the <span class="accent">Table</span></h2>
    <p style="color:rgba(255,255,255,.82);font-size:1rem;margin-top:.5rem">12 key words and expressions</p>
  </div>
</div>''')
    # 5 reveal 1-6
    cards1 = '\n'.join(reveal_card(*VOCAB[i]) for i in range(6))
    S.append(f'''<!-- ========== SLIDE 5 ========== -->
<div class="slide slide-light" data-slide="5" data-phase="2" data-teacher="<strong>Vocab reveal 1-6 (6 min):</strong> Leia a pista em ingles, a Lucimara tenta a palavra, depois revele e toque o audio. CCQ curto (ex: on the house -- do you pay? no).">
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
<div class="slide slide-light" data-slide="6" data-phase="2" data-teacher="<strong>Vocab reveal 7-12 (6 min):</strong> Mesma dinamica. Confirme com CCQs rapidas e peca 1 frase-exemplo da Lucimara para 2 palavras (ex: leftovers, allergen).">
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
<div class="slide slide-light" data-slide="7" data-phase="2" data-teacher="<strong>Consolidar vocab (3 min):</strong> A Lucimara liga cada palavra a definicao em voz alta. Leitura guiada; confirme as duplas que costumam confundir (daily special / house specialty).">
  <div class="slide-inner">
    <div class="chapter-label">Consolidate</div>
    <h2 class="slide-heading">Match the <span class="accent">Meaning</span></h2>
    <!--IC-BLOCKS:vocab-->
  </div>
</div>''')
    # 8 reading transition
    S.append(f'''<!-- ========== SLIDE 8 ========== -->
<div class="slide slide-image" data-slide="8" data-phase="3" data-teacher="<strong>Transicao leitura (1 min):</strong> Diga: read for the main idea first, do not worry about every word. Passe ao proximo." style="background-image:linear-gradient(rgba(20,12,22,.78),rgba(20,12,22,.9)),url('https://images.unsplash.com/photo-1424847651672-bf20a4b0982b?w=1400&q=80');background-size:cover;background-position:center">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label">Chapter 3: House Rules</div>
    <h2 class="slide-heading" style="font-size:2rem;color:#fff">Read the <span class="accent">Rules</span></h2>
    <p style="color:rgba(255,255,255,.82);font-size:1rem;margin-top:.5rem">Read for the main idea</p>
  </div>
</div>''')
    # 9 reading + gist
    S.append(f'''<!-- ========== SLIDE 9 ========== -->
<div class="slide slide-light" data-slide="9" data-phase="3" data-teacher="<strong>Reading + Gist (5 min):</strong> De 2 minutos de leitura silenciosa. Depois: what is the main idea? A Lucimara clica a alternativa certa (fica verde). NAO peca traducao palavra a palavra.">
  <div class="slide-inner">
    <div class="chapter-label">Read for the Main Idea</div>
    <h2 class="slide-heading">Eating Out, American <span class="accent">Style</span></h2>
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
<div class="slide slide-light" data-slide="12" data-phase="3" data-teacher="<strong>Useful language (3 min):</strong> Apresente as frases-modelo. Peca que a Lucimara leia cada chip em voz alta.">
  <div class="slide-inner">
    <div class="chapter-label">At the Table</div>
    <h2 class="slide-heading">Useful <span class="accent">Phrases</span></h2>
    <!--IC-BLOCKS:bank-->
  </div>
</div>''')
    # 13 grammar transition
    S.append(f'''<!-- ========== SLIDE 13 ========== -->
<div class="slide slide-image" data-slide="13" data-phase="4" data-teacher="<strong>Transicao gramatica (1 min):</strong> Diga que o foco agora e IMAGINAR: if + passado, would + verbo base. E o second conditional. Passe ao proximo." style="background-image:linear-gradient(rgba(20,12,22,.78),rgba(20,12,22,.9)),url('https://images.unsplash.com/photo-1466978913421-dad2ebd01d17?w=1400&q=80');background-size:cover;background-position:center">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label">Chapter 4: If I Were You</div>
    <h2 class="slide-heading" style="font-size:2rem;color:#fff">The Second <span class="accent">Conditional</span></h2>
    <p style="color:rgba(255,255,255,.82);font-size:1rem;margin-top:.5rem">imaginary &middot; if + past &middot; would + base verb &middot; 'were' for everybody</p>
  </div>
</div>''')
    # 14 grammar discovery (data-grammar injected here)
    ex = [
        "If I were you, I would go with the house specialty.",
        "If the server recommended the fish, I would order it.",
        "If we arrived before seven, we would catch happy hour.",
    ]
    hi = ['were', 'recommended', 'arrived']
    rows = ''
    for e, h in zip(ex, hi):
        marked = e.replace(h, f'<span class="accent" style="font-weight:700">{h}</span>', 1)
        rows += (f'      <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:.8rem;display:flex;justify-content:space-between;align-items:center;gap:.6rem"><p style="font-size:.92rem">"{marked}"</p>{listen_btn(e)}</div>\n')
    S.append(f'''<!-- ========== SLIDE 14 ========== -->
<div class="slide slide-light" data-slide="14" data-phase="4" data-teacher="<strong>Grammar discovery (6 min):</strong> Leia os 3 exemplos. NAO mostre a regra primeiro. Pergunte que tempo verbal vem depois de 'if' (passado) e o que vem depois (would + base). CCQ: isso ja aconteceu? Nao -- e imaginario. So entao clique Reveal the Rule.">
  <div class="slide-inner">
    <div class="chapter-label">Grammar Discovery</div>
    <h2 class="slide-heading">Listen and <span class="accent">Notice</span></h2>
    <div style="display:flex;flex-direction:column;gap:.7rem;max-width:620px;margin:1rem auto 0">
{rows}    </div>
    <p style="text-align:center;font-size:.85rem;color:var(--text-dim);margin-top:1rem">These situations are imaginary, not real. What verb form comes after "if" -- and what comes after "would"?</p>
    <button class="primary-btn" style="margin:1rem auto 0;display:block;background:{A};color:#fff;border:none;border-radius:8px;padding:.6rem 1.4rem;font-size:.9rem;font-weight:600;cursor:pointer" onclick="var t=document.getElementById('rule18');t.style.display=(t.style.display==='none'||!t.style.display)?'block':'none'">Reveal the Rule</button>
    <div id="rule18" style="display:none;max-width:620px;margin:1rem auto 0;overflow-x:auto">
      <table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:{A};color:#fff"><th style="padding:.6rem;text-align:left">Situation</th><th style="padding:.6rem;text-align:left">Structure</th><th style="padding:.6rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.5rem">Real / likely (first)</td><td style="padding:.5rem">if + <strong>present</strong>, <strong>will</strong> + base</td><td style="padding:.5rem">"If they <strong>have</strong> the salmon, I <strong>will</strong> order it."</td></tr>
          <tr style="background:var(--bg-elevated);border-bottom:1px solid var(--border)"><td style="padding:.5rem">Imaginary (second)</td><td style="padding:.5rem">if + <strong>past</strong>, <strong>would</strong> + base</td><td style="padding:.5rem">"If they <strong>had</strong> the salmon, I <strong>would</strong> order it."</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.5rem">Giving advice</td><td style="padding:.5rem">If I <strong>were</strong> you, I <strong>would</strong>...</td><td style="padding:.5rem">"If I <strong>were</strong> you, I <strong>would</strong> try the special."</td></tr>
          <tr style="background:var(--bg-elevated)"><td style="padding:.5rem">'were' for everybody</td><td style="padding:.5rem">if I / he / she <strong>were</strong></td><td style="padding:.5rem">"If she <strong>were</strong> here, she <strong>would</strong> love this."</td></tr>
        </tbody>
      </table>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.6rem;text-align:center">Second conditional = imaginary. If + past simple, would + base verb. Use "were" for every subject.</p>
    </div>
  </div>
</div>''')
    # 15 language focus (lf block)
    S.append(f'''<!-- ========== SLIDE 15 ========== -->
<div class="slide slide-light" data-slide="15" data-phase="4" data-teacher="<strong>Language Focus (4 min):</strong> A Lucimara le cada linha e completa a frase no second conditional. Use como ponte para o erro comum do proximo slide.">
  <div class="slide-inner">
    <div class="chapter-label">Language Focus</div>
    <h2 class="slide-heading">Complete the <span class="accent">Sentence</span></h2>
    <!--IC-BLOCKS:lf-->
  </div>
</div>''')
    # 16 common mistake
    S.append(f'''<!-- ========== SLIDE 16 ========== -->
<div class="slide slide-light" data-slide="16" data-phase="4" data-teacher="<strong>Common mistake (3 min):</strong> Mostre certo (verde) vs errado (vermelho). Reforce: apos 'if' vem o PASSADO (nao 'would'); e usamos 'were', nao 'was', em ingles cuidadoso. Peca que a Lucimara leia as versoes certas 2 vezes.">
  <div class="slide-inner">
    <div class="chapter-label">Common Mistake</div>
    <h2 class="slide-heading">Right vs <span class="accent">Wrong</span></h2>
    <div style="display:flex;flex-direction:column;gap:1rem;max-width:560px;margin:1.2rem auto 0">
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:.8rem">
        <div style="background:var(--danger-bg);border:1px solid var(--danger-border);border-radius:10px;padding:1rem"><p style="font-size:.78rem;color:var(--danger);font-weight:700;margin-bottom:.3rem">&#10007; WRONG</p><p style="font-size:.88rem">"If I would be you, I would order the fish."</p></div>
        <div style="background:var(--success-bg);border:1px solid var(--success-border);border-radius:10px;padding:1rem"><p style="font-size:.78rem;color:var(--success);font-weight:700;margin-bottom:.3rem">&#10003; RIGHT</p><p style="font-size:.88rem">If I <strong>were</strong> you, I would order the fish.</p></div>
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:.8rem">
        <div style="background:var(--danger-bg);border:1px solid var(--danger-border);border-radius:10px;padding:1rem"><p style="font-size:.78rem;color:var(--danger);font-weight:700;margin-bottom:.3rem">&#10007; WRONG</p><p style="font-size:.88rem">"If she had time, she will cook at home."</p></div>
        <div style="background:var(--success-bg);border:1px solid var(--success-border);border-radius:10px;padding:1rem"><p style="font-size:.78rem;color:var(--success);font-weight:700;margin-bottom:.3rem">&#10003; RIGHT</p><p style="font-size:.88rem">If she had time, she <strong>would</strong> cook at home.</p></div>
      </div>
    </div>
    <p style="font-size:.82rem;color:var(--text-dim);margin:1rem auto 0;max-width:500px;text-align:center">After "if", use the past simple, not "would". And in careful English, use "were" for every subject: if I were, if she were.</p>
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
      <div class="error-card" onclick="revealError(this)"><div class="error-sentence">"If I would be you, I would order the special."</div><div class="error-fix">If I were you, I would order the special.</div></div>
      <div class="error-card" onclick="revealError(this)"><div class="error-sentence">"If she had the money, she will travel more."</div><div class="error-fix">If she had the money, she would travel more.</div></div>
      <div class="error-card" onclick="revealError(this)"><div class="error-sentence">"If we split the check, it be easier."</div><div class="error-fix">If we split the check, it would be easier.</div></div>
      <div class="error-card" onclick="revealError(this)"><div class="error-sentence">"If I was the chef, I would change the menu."</div><div class="error-fix">If I were the chef, I would change the menu.</div></div>
    </div>
    <div class="error-score" id="errorScore" style="margin-top:1rem">0 / 4 errors found</div>
  </div>
</div>''')
    # 18 voices transition
    S.append(f'''<!-- ========== SLIDE 18 ========== -->
<div class="slide slide-image" data-slide="18" data-phase="5" data-teacher="<strong>Transicao (1 min):</strong> Ponte para a parte de fala. Diga que agora a Lucimara vai ouvir um garcom de verdade e depois pedir. Passe ao proximo." style="background-image:linear-gradient(rgba(20,12,22,.78),rgba(20,12,22,.9)),url('https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1400&q=80');background-size:cover;background-position:center">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label">Chapter 5: Real Voices</div>
    <h2 class="slide-heading" style="font-size:2rem;color:#fff">Voices at the <span class="accent">Restaurant</span></h2>
    <p style="color:rgba(255,255,255,.82);font-size:1rem;margin-top:.5rem">Hear a real server, then order in your own words.</p>
  </div>
</div>''')
    # 19 from menu to your choice
    S.append(f'''<!-- ========== SLIDE 19 ========== -->
<div class="slide slide-light" data-slide="19" data-phase="5" data-teacher="<strong>From menu to choice (4 min):</strong> Mostre a situacao e peca que a Lucimara diga a frase no second conditional ANTES de revelar. Reforce if + passado, would + base.">
  <div class="slide-inner">
    <div class="chapter-label">Imagine the Meal</div>
    <h2 class="slide-heading">What Would You <span class="accent">Say?</span></h2>
    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem">Read the situation, then tap to see one good answer</p>
    <div class="comp-questions" style="max-width:580px;margin:1.2rem auto 0">
      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">A friend cannot decide. Give advice.</div><div class="q-answer">If I were you, I would go with the house specialty.</div></div>
      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">They ask about a hypothetical free dinner anywhere.</div><div class="q-answer">If I could eat anywhere, I would go to a rooftop restaurant in New York.</div></div>
      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">Your steak arrives too rare.</div><div class="q-answer">If my steak were too rare, I would ask them to cook it a bit more.</div></div>
      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">Your guest has a nut allergy.</div><div class="q-answer">If my guest ate nuts, it would be dangerous, so I would tell the server about the allergen.</div></div>
    </div>
  </div>
</div>''')
    # 20 dialogue (each line ONE physical line)
    dlines = [
        ('1', 'arthur', 'ryan', 'R', 'ryan-bubble',
         'Good evening, welcome to The Smith. My name is Ryan, I will be your <span class="vocab-highlight">server</span> tonight. Can I start you off with anything to drink?'),
        ('2', 'ellen', 'lucimara', 'L', 'lucimara-bubble',
         'Thank you. Two sparkling waters, please. And could you tell us about the <span class="vocab-highlight">daily special</span>?'),
        ('3', 'arthur', 'ryan', 'R', 'ryan-bubble',
         'Of course. Tonight it is a pan-seared salmon. But if I <span class="vocab-highlight">were</span> you, I would go with our <span class="vocab-highlight">house specialty</span>, the slow-cooked short rib.'),
        ('4', 'ellen', 'lucimara', 'L', 'lucimara-bubble',
         'That sounds perfect. One question first: my guest cannot eat nuts. Is there any <span class="vocab-highlight">allergen</span> in the short rib?'),
        ('5', 'arthur', 'ryan', 'R', 'ryan-bubble',
         'No nuts at all, and if there were, the kitchen would prepare it separately. Would you like a salad with that?'),
        ('6', 'ellen', 'lucimara', 'L', 'lucimara-bubble',
         'Yes, one salad, with the <span class="vocab-highlight">dressing on the side</span>, please. And we will <span class="vocab-highlight">split the check</span> at the end.'),
        ('7', 'arthur', 'ryan', 'R', 'ryan-bubble',
         'Absolutely. And since you came before seven, your first drinks are <span class="vocab-highlight">on the house</span>. If you cannot finish the short rib, we are happy to box up your <span class="vocab-highlight">leftovers</span>.'),
        ('8', 'ellen', 'lucimara', 'L', 'lucimara-bubble',
         'Wonderful. If every restaurant were this easy, I would eat out every night. Thank you, Ryan!'),
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
<div class="slide slide-dark" data-slide="20" data-phase="5" data-teacher="<strong>Dialogo (6 min):</strong> Voce e o Ryan (garcom). Click Next Line a cada fala. Para cada fala da Lucimara, peca que ELA fale primeiro, depois toque o audio. Celebre o uso do second conditional.">
  <div class="slide-inner">
    <div class="chapter-label">Dialogue</div>
    <h2 class="slide-heading" style="color:#fff">Ordering at <span class="accent">The Smith</span></h2>
    <div class="dialogue-box" id="dialogueBox">
{dialogue}
    </div>
    <button class="primary-btn" id="nextLineBtn" onclick="nextDialogueLine()" style="margin:1.2rem auto 0;display:block;background:{A};color:#fff;border:none;border-radius:8px;padding:.6rem 1.4rem;font-size:.9rem;font-weight:600;cursor:pointer">Next Line</button>
  </div>
</div>''')
    # 21 dialogue comprehension (about the server = third party)
    S.append(f'''<!-- ========== SLIDE 21 ========== -->
<div class="slide slide-light" data-slide="21" data-phase="5" data-teacher="<strong>Comprehension (3 min):</strong> Perguntas sobre o que o RYAN (garcom) disse (REGRA 27F -- nao sobre a Lucimara). A Lucimara tenta antes de revelar; click para mostrar.">
  <div class="slide-inner">
    <div class="chapter-label">Did You Catch It?</div>
    <h2 class="slide-heading">What Did Ryan <span class="accent">Say?</span></h2>
    <div class="comp-questions" style="max-width:560px;margin:1.2rem auto 0">
      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">1. What did Ryan recommend, and how did he say it?</div><div class="q-answer">The house specialty, the slow-cooked short rib. He said, "If I were you, I would go with our house specialty."</div></div>
      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">2. What did Ryan say about the nut allergy?</div><div class="q-answer">There were no nuts in the short rib, and if there were, the kitchen would prepare it separately.</div></div>
      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">3. Why were the first drinks on the house?</div><div class="q-answer">Because they arrived before seven, so they caught happy hour.</div></div>
    </div>
  </div>
</div>''')
    # 22 artifact: the menu
    S.append(f'''<!-- ========== SLIDE 22 ========== -->
<div class="slide slide-light" data-slide="22" data-phase="5" data-teacher="<strong>Documento real (4 min):</strong> De 1 minuto de leitura silenciosa do cardapio. Depois pergunte o que a Lucimara pediria e por que. NAO peca traducao palavra a palavra.">
  <div class="slide-inner">
    <div class="chapter-label">The Menu</div>
    <h2 class="slide-heading">The Smith &mdash; <span class="accent">Dinner Menu</span></h2>
    <div style="max-width:440px;margin:1.2rem auto 0;background:var(--bg-card);border:1px solid var(--border);border-radius:16px;padding:1.2rem;text-align:left">
      <div style="font-size:.78rem;color:var(--text-dim);text-align:center;letter-spacing:.12em;border-bottom:1px solid var(--border);padding-bottom:.5rem;margin-bottom:.7rem">THE SMITH &middot; NEW YORK</div>
      <div style="font-size:.72rem;color:var(--accent);font-weight:700;text-transform:uppercase;letter-spacing:.08em;margin-bottom:.35rem">Starters</div>
      <div style="display:flex;justify-content:space-between;font-size:.86rem;margin-bottom:.25rem"><span>Garden Salad <span style="color:var(--text-dim);font-size:.76rem">&mdash; dressing on the side</span></span><span>$11</span></div>
      <div style="display:flex;justify-content:space-between;font-size:.86rem;margin-bottom:.7rem"><span>Soup of the Day</span><span>$9</span></div>
      <div style="font-size:.72rem;color:var(--accent);font-weight:700;text-transform:uppercase;letter-spacing:.08em;margin-bottom:.35rem">Mains</div>
      <div style="display:flex;justify-content:space-between;font-size:.86rem;margin-bottom:.25rem"><span>Short Rib <span style="color:var(--accent);font-size:.72rem;font-weight:700">&middot; House Specialty</span></span><span>$28</span></div>
      <div style="display:flex;justify-content:space-between;font-size:.86rem;margin-bottom:.25rem"><span>Pan-Seared Salmon <span style="color:var(--text-dim);font-size:.76rem">&mdash; today's special</span></span><span>$26</span></div>
      <div style="display:flex;justify-content:space-between;font-size:.86rem;margin-bottom:.7rem"><span>Grilled Ribeye <span style="color:var(--text-dim);font-size:.76rem">&mdash; well-done on request</span></span><span>$34</span></div>
      <div style="font-size:.74rem;color:var(--text-dim);border-top:1px solid var(--border);padding-top:.5rem">Happy hour until 7 pm &middot; Please tell us about any allergen &middot; 20% gratuity added for parties of six or more</div>
    </div>
  </div>
</div>''')
    # 23 artifact comprehension
    S.append(f'''<!-- ========== SLIDE 23 ========== -->
<div class="slide slide-light" data-slide="23" data-phase="5" data-teacher="<strong>Comprehension do documento (3 min):</strong> A Lucimara responde no second conditional ANTES de clicar para revelar. Volte ao cardapio para justificar.">
  <div class="slide-inner">
    <div class="chapter-label">Read the Menu</div>
    <h2 class="slide-heading">Order from <span class="accent">The Smith</span></h2>
    <div class="comp-questions" style="max-width:560px;margin:1.2rem auto 0">
      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">1. Which dish is the house specialty, and how much is it?</div><div class="q-answer">The Short Rib, at $28.</div></div>
      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">2. If you wanted your salad sauce separate, what would you ask for?</div><div class="q-answer">I would ask for the Garden Salad with the dressing on the side.</div></div>
      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">3. If you arrived at 6:30, what would be cheaper?</div><div class="q-answer">The drinks, because happy hour runs until 7 pm.</div></div>
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
        24, 'mp-listen1', 'waveform1', 'listening1Qs', 'a18_listening_specials.mp3',
        'The Server&#39;s <span class="accent">Specials</span>',
        'A server welcomes you and describes tonight&#39;s specials.',
        [("1. What is tonight's daily special?",
          "A pan-seared salmon with a lemon butter sauce, roasted vegetables and a small salad."),
         ("2. Which dish does the server recommend, and why?",
          "The slow-cooked short rib, the house specialty people come back for; it is what he would order himself."),
         ("3. What does the server say about happy hour?",
          "It runs until seven, so your first drink is on the house.")]))
    S.append(listening_slide(
        25, 'mp-listen2', 'waveform2', 'listening2Qs', 'a18_listening_grammartip.mp3',
        'How to <span class="accent">Imagine It</span>',
        'A short tip on the second conditional.',
        [("1. What two parts make the second conditional?",
          "'if' + a past-tense verb, and 'would' + the base verb."),
         ("2. When do we use 'were', according to the tip?",
          "For everybody / all subjects (if I were, if she were)."),
         ("3. What is the difference between the first and second conditional?",
          "First (present + will) is for real, likely things; second (past + would) is for imaginary situations.")]))
    # 26 pronunciation
    pron = [
        ("If I were you, I would go with the special.", "'I would' links to I'd; keep 'were' short -- wer."),
        ("Could I have the dressing on the side?", "'Could I' links -- COO-dai; rise at the end."),
        ("We would like to split the check, please.", "'We would' -- we'd; stress SPLIT and CHECK."),
        ("If they had it, I would order it.", "'had it' links -- HA-dit; 'would order' -- wud-ORder."),
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
<div class="slide slide-image" data-slide="27" data-phase="6" data-teacher="<strong>Transicao (1 min):</strong> Ponte para a producao livre. Diga que agora a Lucimara assume a mesa e pede sozinha. Passe ao proximo." style="background-image:linear-gradient(rgba(20,12,22,.78),rgba(20,12,22,.9)),url('https://images.unsplash.com/photo-1552566626-52f8b828add9?w=1400&q=80');background-size:cover;background-position:center">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label">Chapter 6: Your Turn</div>
    <h2 class="slide-heading" style="font-size:2rem;color:#fff">Now You <span class="accent">Order</span></h2>
    <p style="color:rgba(255,255,255,.82);font-size:1rem;margin-top:.5rem">Your turn: order for yourself and a guest, out loud.</p>
  </div>
</div>''')
    # 28 quickfire
    S.append(f'''<!-- ========== SLIDE 28 ========== -->
<div class="slide slide-light" data-slide="28" data-phase="6" data-teacher="<strong>Quick fire (5 min):</strong> Uma situacao por vez. A Lucimara responde em voz alta no second conditional, SEM ver as tips. Use Tips so se ela travar. Navegue com Previous/Next.">
  <div class="slide-inner">
    <div class="chapter-label">Quick Fire</div>
    <h2 class="slide-heading">Imagine on Your <span class="accent">Feet</span></h2>
    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem">One situation at a time &mdash; answer out loud, then check the tips</p>
    <!--IC-BLOCKS:quickfire-->
  </div>
</div>''')
    # 29 scenarios
    S.append(f'''<!-- ========== SLIDE 29 ========== -->
<div class="slide slide-light" data-slide="29" data-phase="6" data-teacher="<strong>Scenarios (5 min):</strong> Para cada cena, a Lucimara produz a resposta em voz alta usando o second conditional. Sem gabarito visivel; ela produz.">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 6: Your Turn</div>
    <h2 class="slide-heading">At the <span class="accent">Table</span></h2>
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
<div class="slide slide-light" data-slide="31" data-phase="6" data-teacher="Role-play guiado (4 min): Voce e o garcom. A Lucimara pede uma entrada e um prato principal usando o vocab e uma frase no second conditional. Deixe-a produzir com calma; corrija so no fim.">
  <div class="slide-inner">
    <div class="chapter-label">Role-Play 1 of 3 &mdash; Guided</div>
    <h2 class="slide-heading">Order Your <span class="accent">Dinner</span></h2>
    <div class="roleplay-body" style="max-width:500px;margin:1rem auto 0;background:linear-gradient(135deg,rgba(91,45,95,.12),rgba(91,45,95,.03));border:1px solid {A};border-radius:12px;padding:1.5rem">
      <p class="roleplay-scenario" style="font-size:.9rem;margin-bottom:1rem"><strong>Scenario:</strong> The server asks what you would like. Order a starter and a main, and add one sentence with "If I were..." to explain your choice.</p>
      <div style="display:flex;flex-wrap:wrap;gap:.5rem;justify-content:center"><span style="border:1px solid {A};color:{A};border-radius:20px;padding:.3rem .9rem;font-size:.82rem">I'll go with</span><span style="border:1px solid {A};color:{A};border-radius:20px;padding:.3rem .9rem;font-size:.82rem">house specialty</span><span style="border:1px solid {A};color:{A};border-radius:20px;padding:.3rem .9rem;font-size:.82rem">If I were...</span></div>
    </div>
  </div>
</div>''')
    S.append(f'''<!-- ========== SLIDE 32 ========== -->
<div class="slide slide-light" data-slide="32" data-phase="6" data-teacher="Role-play semi-livre (4 min): Menos apoio. A Lucimara pede considerando a alergia do convidado e pede a comida sem um ingrediente. Anote os acertos.">
  <div class="slide-inner">
    <div class="chapter-label">Role-Play 2 of 3 &mdash; Semi-free</div>
    <h2 class="slide-heading">Handle the <span class="accent">Allergy</span></h2>
    <div class="roleplay-body" style="max-width:500px;margin:1rem auto 0;background:linear-gradient(135deg,rgba(91,45,95,.12),rgba(91,45,95,.03));border:1px solid {A};border-radius:12px;padding:1.5rem">
      <p class="roleplay-scenario" style="font-size:.9rem;margin-bottom:1rem"><strong>Scenario:</strong> Your guest cannot eat gluten. Ask the server about allergens and request a change to a dish. Use "If... I would..." at least once.</p>
      <div style="display:flex;flex-wrap:wrap;gap:.5rem;justify-content:center"><span style="border:1px solid {A};color:{A};border-radius:20px;padding:.3rem .9rem;font-size:.82rem">allergen</span><span style="border:1px solid {A};color:{A};border-radius:20px;padding:.3rem .9rem;font-size:.82rem">dressing on the side</span><span style="border:1px solid {A};color:{A};border-radius:20px;padding:.3rem .9rem;font-size:.82rem">If it had...</span></div>
    </div>
  </div>
</div>''')
    S.append(f'''<!-- ========== SLIDE 33 ========== -->
<div class="slide slide-light" data-slide="33" data-phase="6" data-teacher="Pratica livre (5 min): ZERO pistas. NAO interrompa; anote os erros para o feedback. CELEBRE muito.">
  <div class="slide-inner">
    <div class="chapter-label">Role-Play 3 of 3 &mdash; Free</div>
    <h2 class="slide-heading">Your Dream <span class="accent">Dinner</span></h2>
    <div class="roleplay-body" style="max-width:500px;margin:1rem auto 0;background:linear-gradient(135deg,rgba(91,45,95,.12),rgba(91,45,95,.03));border:1px solid {A};border-radius:12px;padding:1.5rem">
      <p class="roleplay-scenario" style="font-size:.9rem;margin-bottom:1rem"><strong>Scenario:</strong> Describe your dream dinner anywhere in the world. Say where you would go, who you would bring, and what you would order, using the second conditional at least three times.</p>
      <p style="font-size:.85rem;color:var(--text-dim);font-style:italic">No keywords. The meal is yours!</p>
    </div>
  </div>
</div>''')
    # 34 survival
    surv = [
        "If I were you, I would go with the house specialty.",
        "Could I have the dressing on the side, please?",
        "Is there any allergen in this dish?",
        "We would like to split the check, please.",
        "Could we get a box for the leftovers?",
    ]
    sitems = ''
    for i, ph in enumerate(surv, 1):
        sitems += (f'      <div class="survival-item-ic"><div class="survival-num-ic">{i}</div><div class="survival-text-ic">"{ph}"</div><button class="audio-btn-sm" onclick="speakText(\'{ph}\',this)">{LISTEN_ICON}</button></div>\n')
    S.append(f'''<!-- ========== SLIDE 34 ========== -->
<div class="slide slide-dark" data-slide="34" data-phase="7" data-teacher="<strong>Survival lines (3 min):</strong> Leia cada frase, toque o audio e peca que a Lucimara repita. Sao as frases-chave da aula.">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label">Chapter 7: Wrap-Up</div>
    <h2 class="slide-heading" style="color:#fff">Order Like a <span class="accent">Regular</span></h2>
    <div class="survival-grid" style="max-width:560px;margin:1.5rem auto 0">
{sitems}    </div>
  </div>
</div>''')
    # 35 checklist
    checks = [
        "I can form the second conditional: if + past simple, would + base verb.",
        "I can give advice with 'If I were you, I would...'.",
        "I know to use 'were' for every subject (if I were, if she were).",
        "I can order for myself and a guest, and ask about an allergen.",
        "I know the words: server, daily special, house specialty, to eat out, to go with, to split the check, leftovers, on the house, allergen, dressing on the side, well-done, happy hour.",
    ]
    citems = ''
    for c in checks:
        citems += (f'      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg></div>{c}</div>\n')
    S.append(f'''<!-- ========== SLIDE 35 ========== -->
<div class="slide slide-dark" data-slide="35" data-phase="7" data-teacher="<strong>Checklist (2 min):</strong> Diga: click each item if you feel confident. Leia cada item. Os 5 checks = aula completa e stamp no passaporte.">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label">Self-Assessment</div>
    <h2 class="slide-heading" style="color:#fff">What I <span class="accent">Learned</span></h2>
    <div class="check-grid" id="checklist-18" style="max-width:560px;margin:1.2rem auto 0;display:flex;flex-direction:column;gap:.5rem;text-align:left">
{citems}    </div>
  </div>
</div>''')
    # 36 closing
    S.append(f'''<!-- ========== SLIDE 36 ========== -->
<div class="slide slide-dark" data-slide="36" data-phase="7" data-teacher="<strong>Encerramento (2 min):</strong> Parabenize a Lucimara e entregue o badge. Passe o homework ORALMENTE (gravar 90s sobre a refeicao ideal em Nova York com 2+ second conditionals e 5 palavras de hoje; assistir 5 min de video sobre pedir comida e anotar 3 frases novas; escolher um pedido completo de um cardapio real de NY). Proxima aula: Small Talk That Works.">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label">Lesson Complete</div>
    <div class="badge-card">
      <div class="badge-icon">
        <div class="badge-circle"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 3v9M9 3v4a3 3 0 006 0V3M18 3c-1.5 0-2 3-2 5s.5 4 2 4v9"/></svg></div>
        <div class="sparkles"><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div></div>
      </div>
      <h2 class="slide-heading" style="color:#fff">Confident Diner Badge <span class="accent">Earned!</span></h2>
      <p style="color:rgba(255,255,255,.78);font-size:1rem;margin-top:.5rem">You can read a menu, ask about an allergen, order for a guest, split the check, and imagine any meal with the second conditional. Well done, Lucimara.</p>
      <p style="color:rgba(255,255,255,.82);font-size:.85rem;margin-top:1.5rem">Lesson 18 -- Complete.</p>
      <p style="color:var(--accent-light);font-size:.9rem;margin-top:.5rem">Next lesson: Small Talk That Works</p>
    </div>
  </div>
</div>''')
    return '\n\n'.join(S) + '\n'


# ---------------------------------------------------------------- PRECLASS
def rot(lst, k):
    k %= len(lst)
    return lst[k:] + lst[:k]


def build_preclass():
    N = 18
    defs = [v[1] for v in VOCAB]
    # vocab cards
    vcards = ''
    for word, d, ex, _, _ in VOCAB:
        vcards += (f'        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header"><span class="vocab-card-word">{word}</span><span class="vocab-card-dot"> -- </span><span class="vocab-card-def">{d}</span></div><div class="vocab-card-example">{ex}</div></div><button class="audio-btn" onclick="speakText(\'{word}\',this)">Listen</button></div>\n')
    # matching (shuffled per row)
    mrows = ''
    for i, (word, d, _, _, _) in enumerate(VOCAB):
        opts = rot(defs, (i * 5 + 3))
        optshtml = '<option value="">Select...</option>' + ''.join(
            f'<option value="{o}">{o}</option>' for o in opts)
        mrows += (f'        <div class="match-row" data-answer="{d}"><span class="match-word" style="flex:0 0 150px">{word}</span><select style="flex:1;width:100%" onchange="checkMatch(this)">{optshtml}</select></div>\n')
    # grammar in context text
    gic_text = ('When Lucimara imagines the perfect dinner, she uses the second conditional. '
                '<strong>If</strong> she <strong>were</strong> in New York tonight, she <strong>would</strong> eat out at a rooftop restaurant. '
                '<strong>If</strong> the server <strong>recommended</strong> the house specialty, she <strong>would</strong> order it. '
                'And <strong>if</strong> her guest <strong>had</strong> an allergy, the kitchen <strong>would</strong> prepare the dish separately. '
                'None of this is happening right now -- it is all imaginary, which is exactly what the second conditional is for.')
    # fill blanks
    blanks = [
        ("If I ", "were", "Hint: use this form of 'be' for all subjects in the second conditional",
         "If I were you, I would order the house specialty.", " you, I would order the house specialty."),
        ("If they had it, I ", "would", "Hint: this modal comes after the if-clause",
         "If they had it, I would order it right away.", " order it right away."),
        ("If the server ", "recommended", "Hint: past form of 'recommend'",
         "If the server recommended it, I would try it.", " it, I would try it."),
        ("Could I have the dressing ", "on", "Hint: dressing served separately is 'on the ___ side'",
         "Could I have the dressing on the side, please?", " the side, please?"),
        ("We would like to ", "split", "Hint: to divide the bill",
         "We would like to split the check, please.", " the check, please."),
        ("If we arrived before seven, we would catch happy ", "hour", "Hint: cheaper drinks time",
         "If we arrived before seven, we would catch happy hour.", "."),
    ]
    bhtml = ''
    for pre, ans, hint, phrase, post in blanks:
        bhtml += (f'      <div class="fill-blank-item"><div class="fill-blank-sentence">"{pre}<input class="blank-input" data-answer="{ans}" data-hint="{hint}" data-phrase="{phrase}" placeholder="___">{post}"</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>\n')
    # order steps
    order = [
        (1, "Read the menu and the daily specials."),
        (2, "Ask the server what they would recommend."),
        (3, "Mention any allergen or change you need."),
        (4, "Say your choice: 'I'll go with...'."),
        (5, "At the end, ask to split the check."),
    ]
    display_order = [order[2], order[4], order[0], order[3], order[1]]
    ohtml = ''
    for o, text in display_order:
        ohtml += (f'        <div class="order-item" draggable="true" data-order="{o}" onclick="selectOrderItem(this,\'order-l{N}\')"><span class="order-num">?</span><span class="order-text">{text}</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,\'order-l{N}\')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,\'order-l{N}\')">&#9660;</button></span></div>\n')
    # speech cards
    speech = [
        "If I were you, I would go with the house specialty.",
        "Could you tell us about the daily special?",
        "Is there any allergen in this dish?",
        "We would like to split the check, please.",
        "If they had a vegetarian option, I would order it.",
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
        "If I were you, I would go with the house specialty.",
        "Could I have the dressing on the side, please?",
        "Is there any allergen in this dish?",
        "We would like to split the check, please.",
        "Could we get a box for the leftovers?",
    ]
    survhtml = ''
    for i, ph in enumerate(surv, 1):
        survhtml += (f'      <div class="survival-phrase"><span class="sp-num">{i}</span><span class="sp-en">{ph}</span><button class="btn btn-listen" onclick="speakText(\'{ph}\',this)">&#9835;</button></div>\n')

    html = f'''<div class="lesson-card" id="ex-lesson-{N}">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson {N} -- Pre-class</div>
      <h3>Ordering with Confidence</h3>
      <div class="lesson-desc">A New York restaurant with a business guest -- read the specials, ask about allergens, send back a dish, and split the check. Key words: server, daily special, house specialty, to eat out, to go with, to split the check, leftovers, on the house, allergen, dressing on the side, well-done, happy hour. Structure: the second conditional (if + past, would + base verb).</div>
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
      <div class="quiz-item"><div class="quiz-question">1. In "If she were in New York, she would eat out", why is the verb "were"?</div><div class="quiz-options">
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> The second conditional uses the past form, and "were" is used for all subjects.</div>
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Because there were two or more people.</div>
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because "if" is always followed by "were".</div>
</div></div>
      <div class="quiz-item"><div class="quiz-question">2. The direct idea is "Maybe I will order the salmon (real)." How do you make it imaginary?</div><div class="quiz-options">
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> If they have the salmon, I will order it.</div>
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> If they had the salmon, I would order it.</div>
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> If they would have the salmon, I will order it.</div>
</div></div>
      <div class="quiz-item"><div class="quiz-question">3. Which sentence is correct?</div><div class="quiz-options">
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> If I were you, I would try the house specialty.</div>
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> If I would be you, I would try the house specialty.</div>
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> If I were you, I will try the house specialty.</div>
</div></div>
    </div>
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Second Conditional</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">How to talk about imaginary situations.</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Situation</th><th style="padding:.7rem;text-align:left">Structure</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border);"><td style="padding:.6rem">Real / likely (first)</td><td style="padding:.6rem">if + <strong>present</strong>, <strong>will</strong> + base</td><td style="padding:.6rem">"If they <strong>have</strong> it, I <strong>will</strong> order it."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated);"><td style="padding:.6rem">Imaginary (second)</td><td style="padding:.6rem">if + <strong>past</strong>, <strong>would</strong> + base</td><td style="padding:.6rem">"If they <strong>had</strong> it, I <strong>would</strong> order it."</td></tr>
          <tr style="border-bottom:1px solid var(--border);"><td style="padding:.6rem">Giving advice</td><td style="padding:.6rem">If I <strong>were</strong> you, I <strong>would</strong>...</td><td style="padding:.6rem">"If I <strong>were</strong> you, I <strong>would</strong> try the special."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated);"><td style="padding:.6rem">'were' for everybody</td><td style="padding:.6rem">if I / he / she <strong>were</strong></td><td style="padding:.6rem">"If she <strong>were</strong> here, she <strong>would</strong> love it."</td></tr>
        </tbody>
      </table></div>
    </div>
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the correct word. Tap Listen to hear the whole sentence.</p>
{bhtml}    </div>
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Steps in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the steps for ordering at an American restaurant in the correct order.</p>
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
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best sentence for each situation at the restaurant.</p>
      <div class="quiz-item"><div class="quiz-question">A friend cannot decide what to order. You give advice:</div><div class="quiz-options">
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> If I were you, I would go with the house specialty.</div>
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> If I am you, I will go with the house specialty.</div>
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> If I would be you, I would go with the house specialty.</div>
</div></div>
      <div class="quiz-item"><div class="quiz-question">You want your salad sauce served separately. You say:</div><div class="quiz-options">
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Could I have the dressing on the side, please?</div>
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Could I have the dressing in the corner, please?</div>
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Could I have the salad without the salad, please?</div>
</div></div>
      <div class="quiz-item"><div class="quiz-question">You and a friend want to divide the bill. You say:</div><div class="quiz-options">
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> We would like to split the check, please.</div>
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> We would like to break the check, please.</div>
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> We would like to cut the money, please.</div>
</div></div>
      <div class="quiz-item"><div class="quiz-question">Imagine a hypothetical free dinner anywhere. Which sentence is correct?</div><div class="quiz-options">
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> If I could eat anywhere, I would go to New York.</div>
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> If I can eat anywhere, I would go to New York.</div>
<div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> If I could eat anywhere, I will go to New York.</div>
</div></div>
    </div>
    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. There is no right or wrong answer.</p>
      <div class="think-card">
        <div class="think-question">Imagine your ideal meal in New York. Record a one-minute answer: where you would go, what you would order, and who you would bring. Use the second conditional ("If I were... I would...") at least twice, and include five words from today. Take your time.</div>
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
