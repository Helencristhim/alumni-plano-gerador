# -*- coding: utf-8 -*-
"""Gera slides.html, preclass.html, complementary.html, config.json, audio_manifest.json
para Rubens aula 20 (Food & Culture). Grammar NOVA: like/love/enjoy/can't stand + gerund
e agreement (So do I / Neither do I). Vocab NOVO (12). REGRA 22 garantida."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))

# 12 vocab: (word, def_en, example, pt_gloss, gradient, svg_inner, hint)
VOCAB = [
 ("Cuisine","the style of cooking of a country or region",'"Brazilian cuisine uses fresh fruit and fish."',"Culin&#225;ria","#7c2d12,#ea580c",
  '<path d="M3 11h18"/><path d="M12 3v8"/><path d="M5 11a7 7 0 0 0 14 0"/><line x1="12" y1="19" x2="12" y2="22"/>',"The style of cooking of a country"),
 ("Specialty","a dish a place is famous for and does very well",'"Fish stew is the specialty of this region."',"Especialidade","#9d174d,#ec4899",
  '<path d="M12 2l2.4 7.4H22l-6 4.5 2.3 7.1L12 16.6 5.7 21l2.3-7.1-6-4.5h7.6z"/>',"A dish a place is famous for"),
 ("Flavor","the taste of a food or drink",'"This soup has a rich, deep flavor."',"Sabor","#b45309,#f59e0b",
  '<path d="M12 2a7 7 0 0 0-7 7c0 5 7 13 7 13s7-8 7-13a7 7 0 0 0-7-7z"/><circle cx="12" cy="9" r="2.5"/>',"The taste of a food or drink"),
 ("Ingredient","one of the foods used to make a dish",'"Garlic is a key ingredient in this recipe."',"Ingrediente","#15803d,#4ade80",
  '<rect x="4" y="3" width="16" height="18" rx="2"/><line x1="4" y1="9" x2="20" y2="9"/><line x1="9" y1="13" x2="15" y2="13"/>',"One of the foods used to make a dish"),
 ("Recipe","a set of instructions for cooking a dish",'"My grandmother gave me this recipe."',"Receita","#0e7490,#22d3ee",
  '<path d="M4 4h12a2 2 0 0 1 2 2v14H6a2 2 0 0 1-2-2z"/><line x1="8" y1="8" x2="14" y2="8"/><line x1="8" y1="12" x2="14" y2="12"/>',"Instructions for cooking a dish"),
 ("Savory","tasting of salt or spice, not sweet",'"I prefer savory food to sweet desserts."',"Salgado / saboroso","#475569,#94a3b8",
  '<path d="M3 12h18"/><path d="M6 12V8a6 6 0 0 1 12 0v4"/><path d="M5 12l1 7h12l1-7"/>',"Tasting of salt or spice, not sweet"),
 ("Staple","a basic food eaten very often",'"Rice and beans are a staple in Brazil."',"Alimento b&#225;sico","#1e3a8a,#3b82f6",
  '<path d="M5 10c0-2 3-4 7-4s7 2 7 4"/><path d="M5 10v4c0 2 3 4 7 4s7-2 7-4v-4"/>',"A basic food eaten very often"),
 ("Seasoning","salt, herbs, or spices added to food",'"Add a little seasoning to bring out the flavor."',"Tempero","#9a3412,#fb923c",
  '<path d="M8 2h8l-1 6H9z"/><path d="M9 8h6l1 12H8z"/><circle cx="11" cy="13" r=".6"/><circle cx="13" cy="15" r=".6"/>',"Salt, herbs, or spices added to food"),
 ("Homemade","made at home, not bought in a shop",'"The homemade bread was still warm."',"Caseiro","#0d9488,#5eead4",
  '<path d="M3 11l9-8 9 8"/><path d="M5 10v10h14V10"/><rect x="10" y="14" width="4" height="6"/>',"Made at home, not bought in a shop"),
 ("Street food","food sold by vendors on the street",'"We tried delicious street food at the market."',"Comida de rua","#ca8a04,#facc15",
  '<path d="M3 9l2-4h14l2 4"/><path d="M4 9v11h16V9"/><line x1="12" y1="12" x2="12" y2="17"/>',"Food sold by vendors on the street"),
 ("Delicacy","a special, rare food that people enjoy",'"This cheese is a local delicacy."',"Iguaria","#7c3aed,#a78bfa",
  '<path d="M6 4h12l-2 5H8z"/><path d="M8 9v8a4 4 0 0 0 8 0V9"/>',"A special, rare food people enjoy"),
 ("Hearty","large and satisfying (a meal)",'"After the hike, we had a hearty meal."',"Substancial / refor&#231;ado","#b91c1c,#ef4444",
  '<path d="M12 21s-7-4.5-9.5-9A5 5 0 0 1 12 6a5 5 0 0 1 9.5 6C19 16.5 12 21 12 21z"/>',"Large and satisfying meal"),
]

PT = {w[0]: w[3] for w in VOCAB}

# ---- speakText escape: apostrophes -> doubled for JS single-quote literal in onclick ----
def esc(t):
    return t.replace("'", "\\'")

# Build a config + manifest where listenings/extra_audio declared, slides extracted by builder.
ACCENT = "#336B87"
ACCENT_LIGHT = "#4A8EB0"

# ============ SLIDES ============
def vocab_card(v):
    word, defen, ex, pt, grad, svg, hint = v
    return f'''      <div class="vocab-card" onclick="revealVocab(this)" style="cursor:pointer;border:1px solid var(--border);border-radius:12px;overflow:hidden;transition:all .3s">
        <div class="card-icon" style="background:linear-gradient(135deg,{grad});padding:1.2rem;text-align:center;position:relative"><svg viewBox="0 0 24 24" width="32" height="32" fill="none" stroke="#fff" stroke-width="1.5">{svg}</svg><div class="card-hint" style="color:rgba(255,255,255,.85);font-size:.78rem;margin-top:.5rem">{hint}</div></div>
        <div class="card-body"><div class="card-word">{word}</div><div class="card-def">{defen}</div><div class="card-example">{ex}</div><div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('{esc(word)}',this)"><svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div></div>
      </div>'''

def listen_line(txt):
    return f'''<button class="audio-btn-sm" onclick="speakText('{esc(txt)}',this)"><svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button>'''

# Listening texts (MONOLOGUE, distinct voices)
LISTEN1 = ("Welcome to today's food walking tour. My name is Sofia, and I love showing visitors the flavors of our city. "
 "Our first stop is the central market, where you can try street food from many vendors. The local specialty is a fish stew "
 "made with fresh ingredients and simple seasoning. I really enjoy eating it on cold days, because it is hearty and warm. "
 "Next, we visit a small bakery. The owner makes homemade bread every morning, and the smell is wonderful. If you like savory "
 "food, you will love the cheese bread. And if you prefer something sweet, there is a dessert stall at the end. Brazilian cuisine "
 "is rich and varied, so come hungry. Let us begin and taste the city together.")
LISTEN2 = ("Whenever I travel for a conference, I always make time to try the local food. I think a country's cuisine tells you a lot "
 "about its culture. I love tasting street food, because it is simple, fresh, and full of flavor. I do not enjoy eating at the hotel, "
 "because the food is always the same. On my last trip, a colleague took me to a small place that served a regional delicacy. It was a "
 "savory dish with an unusual seasoning, and I cannot stand spicy food, but this was perfect for me. These days I do not eat as much red meat "
 "as I used to, so I prefer light, healthy dishes. For me, sharing a hearty meal with new people is the best part of any trip.")
ORDER_TXT = ("Here is how I explore the food of a new city. First, I find a market where I can try street food. Then I look for the local "
 "specialty that everyone recommends. After that, I taste a homemade dish made with fresh ingredients. Next, I ask the vendor about the "
 "seasoning and the recipe. Finally, I sit down and enjoy a hearty meal with new friends.")

slides = []
# SLIDE 1 TITLE
slides.append(f'''<!-- ============================================================ -->
<!-- CHAPTER 1: A TASTE OF THE CITY (slides 1-3, phase 1)        -->
<!-- ============================================================ -->

<!-- ========== SLIDE 1: TITLE ========== -->
<div class="slide active slide-dark" data-slide="1" data-lesson="20" data-phase="1" data-teacher="<strong>Abertura (2 min):</strong> Compartilhe a tela. Diga: 'Welcome back, Rubens! Last class you went sightseeing: you joined a city tour and described places with who, which, and that. Today is your last lesson of the block -- Food &amp; Culture. You will explore local cuisine, talk about what you like and do not like eating, and react to other people with So do I and Neither do I.' Crie um clima de celebra&ccedil;&atilde;o: esta &eacute; a aula 20, fecha o pacote." style="background-image:linear-gradient(rgba(20,20,30,.85),rgba(20,20,30,.92)),url('https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=1400&q=80');background-size:cover;background-position:center">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label">Chapter 1 -- A Taste of the City</div>
    <h1 class="slide-heading" style="font-size:2.5rem">Day 20 -- Food <span class="accent">&amp; Culture</span></h1>
    <p style="color:rgba(255,255,255,.6);font-size:1.1rem;margin-top:1rem">Explore local cuisine and say what you love eating</p>
    <p style="color:rgba(255,255,255,.4);font-size:.9rem;margin-top:.5rem">The final lesson of the block -- 60 min</p>
  </div>
</div>''')

# SLIDE 2 WARM-UP
slides.append(f'''
<!-- ========== SLIDE 2: WARM-UP CALLBACK ========== -->
<div class="slide slide-light" data-slide="2" data-lesson="20" data-phase="1" data-teacher="<strong>Warm-up + Callback (3 min):</strong> Toque os 2 audios e pe&ccedil;a Rubens repetir. Fa&ccedil;a o callback da Aula 19: 'Last class you described places on a tour -- the cathedral which is the oldest building, the guide who knows the city.' Depois a ponte: 'After a tour, you get hungry. Now we talk about FOOD -- and how to say what you like and dislike eating. We use a verb of liking plus an -ing verb: I love trying new dishes.' CCQ: 'After love, do we say try or trying? (trying.)'">
  <div class="slide-inner">
    <div class="chapter-label">Warm-up</div>
    <h2 class="slide-heading">From the Tour to the <span class="accent">Table</span></h2>
    <p style="color:var(--text-dim);font-size:1rem;margin-top:1rem;max-width:600px;margin-left:auto;margin-right:auto">Last class you explored the city. Today, after the tour, you sit down to eat and talk about local food:</p>
    <div style="display:flex;flex-direction:column;gap:.7rem;max-width:520px;margin:1.2rem auto 0">
      <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:.8rem;display:flex;justify-content:space-between;align-items:center;gap:.6rem"><p style="font-size:.92rem">"Last class you said: It is a market that sells local crafts."</p>{listen_line("Last class you said: It is a market that sells local crafts.")}</div>
      <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:.8rem;display:flex;justify-content:space-between;align-items:center;gap:.6rem"><p style="font-size:.92rem">"Today you can say: I love trying the local cuisine."</p>{listen_line("Today you can say: I love trying the local cuisine.")}</div>
    </div>
    <div style="max-width:520px;margin:1.5rem auto 0;background:var(--accent-dim);border:1px solid var(--accent);border-radius:12px;padding:1.2rem">
      <p style="font-weight:600;font-size:.95rem;margin-bottom:.5rem">Now think:</p>
      <p style="font-size:.9rem;color:var(--text-dim)">When you travel, what kind of food do you most enjoy trying -- and is there any food you cannot stand?</p>
    </div>
  </div>
</div>''')

# SLIDE 3 GOAL
slides.append(f'''
<!-- ========== SLIDE 3: TODAY'S GOAL ========== -->
<div class="slide slide-light" data-slide="3" data-lesson="20" data-phase="1" data-teacher="<strong>Objetivo (2 min):</strong> Diga: 'Three steps today. First, the words for food and culture -- cuisine, flavor, ingredient, recipe. Then a grammar focus: say what you like and dislike with a verb plus -ing, and react with So do I and Neither do I. Finally, you sit at a real table and talk about food.' Passe ao proximo.">
  <div class="slide-inner">
    <div class="chapter-label">Today's Goal</div>
    <h2 class="slide-heading">Three Steps <span class="accent">Today</span></h2>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:.8rem;max-width:640px;margin:1.5rem auto 0">
      <div style="background:var(--accent-dim);border:1px solid var(--accent);border-radius:10px;padding:1rem;text-align:center">
        <svg viewBox="0 0 24 24" width="32" height="32" fill="none" stroke="var(--accent)" stroke-width="1.5" style="margin-bottom:.5rem"><path d="M3 11h18"/><path d="M5 11a7 7 0 0 0 14 0"/><line x1="12" y1="19" x2="12" y2="22"/></svg>
        <p style="font-weight:700;font-size:.95rem">1. Words</p>
        <p style="font-size:.8rem;color:var(--text-dim)">For food &amp; culture</p>
      </div>
      <div style="background:var(--accent-dim);border:1px solid var(--accent);border-radius:10px;padding:1rem;text-align:center">
        <svg viewBox="0 0 24 24" width="32" height="32" fill="none" stroke="var(--accent)" stroke-width="1.5" style="margin-bottom:.5rem"><path d="M12 21s-7-4.5-9.5-9A5 5 0 0 1 12 6a5 5 0 0 1 9.5 6C19 16.5 12 21 12 21z"/></svg>
        <p style="font-weight:700;font-size:.95rem">2. The Code</p>
        <p style="font-size:.8rem;color:var(--text-dim)">like / love + -ing</p>
      </div>
      <div style="background:var(--accent-dim);border:1px solid var(--accent);border-radius:10px;padding:1rem;text-align:center">
        <svg viewBox="0 0 24 24" width="32" height="32" fill="none" stroke="var(--accent)" stroke-width="1.5" style="margin-bottom:.5rem"><path d="M3 9l2-4h14l2 4"/><path d="M4 9v11h16V9"/></svg>
        <p style="font-weight:700;font-size:.95rem">3. At the Table</p>
        <p style="font-size:.8rem;color:var(--text-dim)">Talk about food</p>
      </div>
    </div>
  </div>
</div>''')

# CHAPTER 2 vocab transition + 3 vocab slides + check
slides.append(f'''
<!-- ============================================================ -->
<!-- CHAPTER 2: FOOD &amp; CULTURE WORDS (slides 4-8, phase 2)       -->
<!-- ============================================================ -->

<!-- ========== SLIDE 4: CHAPTER TRANSITION ========== -->
<div class="slide slide-dark" data-slide="4" data-lesson="20" data-phase="2" data-teacher="<strong>Transicao vocab (1 min):</strong> Diga: 'To talk about food and culture, you need precise words -- cuisine, flavor, ingredient, recipe. Twelve new words. Click each card to reveal.' Passe ao proximo." style="background-image:linear-gradient(rgba(20,20,30,.78),rgba(20,20,30,.88)),url('https://images.unsplash.com/photo-1556910103-1c02745aae4d?w=1400&q=80');background-size:cover;background-position:center">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label">Chapter 2 -- Food &amp; Culture Words</div>
    <h2 class="slide-heading" style="font-size:2rem;color:#fff">Words for the <span class="accent">Table</span></h2>
    <p style="color:rgba(255,255,255,.6);font-size:1rem;margin-top:.5rem">12 new words for food and culture</p>
  </div>
</div>''')

# vocab slides 5,6,7
for gi, (s, e, cid, rng) in enumerate([(0,4,'1','1-4'),(4,8,'2','5-8'),(8,12,'3','9-12')]):
    cards = "\n\n".join(vocab_card(v) for v in VOCAB[s:e])
    sl = 5+gi
    ccqs = {1:"CCQ para 'cuisine': 'Is cuisine the cooking style of a country? (Yes.)' CCQ 'specialty': 'Is a specialty a dish a place is famous for? (Yes.)' CCQ 'flavor': 'Is flavor the taste of food? (Yes.)' CCQ 'ingredient': 'Is an ingredient a food used to make a dish? (Yes.)'",
            2:"CCQ 'recipe': 'Is a recipe the instructions to cook a dish? (Yes.)' CCQ 'savory': 'Is savory salty, not sweet? (Yes.)' CCQ 'staple': 'Is a staple a basic food eaten often? (Yes.)' CCQ 'seasoning': 'Is seasoning salt or spices added to food? (Yes.)'",
            3:"CCQ 'homemade': 'Is homemade food made at home, not bought? (Yes.)' CCQ 'street food': 'Is street food sold by vendors on the street? (Yes.)' CCQ 'delicacy': 'Is a delicacy a special, rare food? (Yes.)' CCQ 'hearty': 'Does hearty mean large and satisfying? (Yes.)' Peca Rubens usar duas palavras numa frase."}[gi+1]
    slides.append(f'''
<!-- ========== SLIDE {sl}: VOCAB {rng} ========== -->
<div class="slide slide-light" data-slide="{sl}" data-lesson="20" data-phase="2" data-teacher="<strong>Vocab reveal {rng} (4 min):</strong> Leia a pista, Rubens adivinha, clique para revelar. Toque o audio e peca que repita. {ccqs}">
  <div class="slide-inner">
    <div class="chapter-label">Vocabulary</div>
    <h2 class="slide-heading">Words <span class="accent">{rng}</span></h2>
    <p style="text-align:center;font-size:.8rem;color:var(--text-dim);margin-top:.3rem"><span id="vocabCount{cid}">0 / 4 words revealed</span></p>
    <div class="vocab-grid" id="vocabGrid{cid}" style="display:grid;grid-template-columns:repeat(2,1fr);gap:.8rem;max-width:600px;margin:1rem auto 0">

{cards}

    </div>
  </div>
</div>''')

# SLIDE 8 vocab check
chips = "\n      ".join(f'<span style="background:var(--bg-card);border:1px solid var(--border);border-radius:20px;padding:.4rem .8rem;font-size:.8rem;font-weight:500">{w[0].lower()}</span>' for w in VOCAB)
slides.append(f'''
<!-- ========== SLIDE 8: VOCAB CHECK ========== -->
<div class="slide slide-light" data-slide="8" data-lesson="20" data-phase="2" data-teacher="<strong>Vocab check (3 min):</strong> Leia o prompt. Deixe Rubens falar livremente usando as palavras novas. Corrija pronuncia. Sugira: 'Describe a meal from your favorite cuisine.' Anote erros. Se ele travar, de um exemplo: 'I love the local cuisine. The specialty is a hearty dish with fresh ingredients and simple seasoning.'">
  <div class="slide-inner">
    <div class="chapter-label">Vocabulary Check</div>
    <h2 class="slide-heading">Use Your <span class="accent">New Words</span></h2>
    <div style="max-width:560px;margin:1.5rem auto 0;background:var(--accent-dim);border:1px solid var(--accent);border-radius:12px;padding:1.4rem">
      <p style="font-size:.95rem;font-weight:600;margin-bottom:.6rem">Describe a meal from your favorite cuisine.</p>
      <p style="font-size:.88rem;color:var(--text-dim)">Use at least three new words from today. Think about: the specialty, the main ingredients, the flavor, and the seasoning.</p>
    </div>
    <div style="display:flex;flex-wrap:wrap;gap:.5rem;justify-content:center;margin-top:1.2rem;max-width:560px;margin-left:auto;margin-right:auto">
      {chips}
    </div>
  </div>
</div>''')

# CHAPTER 3 grammar (9-13)
slides.append(f'''
<!-- ============================================================ -->
<!-- CHAPTER 3: THE CODE (slides 9-13, phase 3)                  -->
<!-- ============================================================ -->

<!-- ========== SLIDE 9: CHAPTER TRANSITION ========== -->
<div class="slide slide-dark" data-slide="9" data-lesson="20" data-phase="3" data-teacher="<strong>Transicao grammar (1 min):</strong> Diga: 'When we talk about food, we say what we like and dislike. We use a verb of feeling -- like, love, enjoy, do not like, cannot stand -- and then an -ing verb. And to react to someone, we use So do I (I feel the same, positive) or Neither do I (I feel the same, negative). Let us find the pattern.' Passe ao proximo." style="background-image:linear-gradient(rgba(20,20,30,.78),rgba(20,20,30,.88)),url('https://images.unsplash.com/photo-1559339352-11d035aa65de?w=1400&q=80');background-size:cover;background-position:center">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label">Chapter 3 -- The Code</div>
    <h2 class="slide-heading" style="font-size:2rem;color:#fff">Grammar <span class="accent">Discovery</span></h2>
    <p style="color:rgba(255,255,255,.6);font-size:1rem;margin-top:.5rem">Saying what you like + reacting (So do I / Neither do I)</p>
  </div>
</div>''')

# SLIDE 10 discovery
gd = [
 ("I <span class=\"accent\" style=\"font-weight:700\">love trying</span> new dishes.","I love trying new dishes.","(like + -ing)"),
 ("I <span class=\"accent\" style=\"font-weight:700\">enjoy cooking</span> on weekends.","I enjoy cooking on weekends.","(enjoy + -ing)"),
 ("I <span class=\"accent\" style=\"font-weight:700\">do not like eating</span> late at night.","I do not like eating late at night.","(negative + -ing)"),
 ("\"I love spicy food.\" -- \"<span class=\"accent\" style=\"font-weight:700\">So do I!</span>\"","I love spicy food. So do I!","(react: same, positive)"),
]
gdrows = "\n".join(f'''      <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:.8rem;display:flex;justify-content:space-between;align-items:center;gap:.6rem"><p style="font-size:.9rem">"{disp}" {tag}</p>{listen_line(audio)}</div>''' for disp,audio,tag in gd)
slides.append(f'''
<!-- ========== SLIDE 10: GRAMMAR DISCOVERY ========== -->
<div class="slide slide-light" data-slide="10" data-lesson="20" data-phase="3" data-teacher="<strong>Grammar discovery (5 min):</strong> Leia cada frase. Pergunte: 'What comes after love, enjoy, and do not like? An -ing verb. And how do we agree with someone? With So do I (positive) or Neither do I (negative).' CCQ: 'After love, do we say try or trying? (trying.) Someone says I love spicy food and you agree -- So do I or Neither do I? (So do I.)' Faca Rubens repetir.">
  <div class="slide-inner">
    <div class="chapter-label">Grammar Discovery</div>
    <h2 class="slide-heading">Listen and <span class="accent">Notice</span></h2>
    <p style="font-size:.88rem;color:var(--text-dim);text-align:center;margin-top:.5rem">How do we say what we like to eat, and how do we agree?</p>
    <div style="display:flex;flex-direction:column;gap:.7rem;max-width:600px;margin:1rem auto 0">
{gdrows}
    </div>
  </div>
</div>''')

# SLIDE 11 reveal rule
slides.append(f'''
<!-- ========== SLIDE 11: REVEAL THE RULE ========== -->
<div class="slide slide-light" data-slide="11" data-lesson="20" data-phase="3" data-teacher="<strong>Reveal the Rule (3 min):</strong> Clique 'Reveal the Rule'. Explique: depois de like, love, enjoy, prefer, do not like, cannot stand vem o verbo com -ing. Para reagir: So + do/am/can + I = concordo (positivo); Neither + do/am/can + I = concordo (negativo). CCQ: 'After enjoy, cook or cooking? (cooking.) I do not like fish -- you agree: So do I or Neither do I? (Neither do I.)' Peca Rubens formar uma frase com cada estrutura.">
  <div class="slide-inner">
    <div class="chapter-label">Grammar Rule</div>
    <h2 class="slide-heading">like + -ing <span class="accent">/ So do I</span></h2>
    <button class="primary-btn" style="margin:1rem auto 0;display:block;background:var(--accent);color:#fff;border:none;border-radius:8px;padding:.6rem 1.4rem;font-size:.9rem;font-weight:600;cursor:pointer" onclick="var t=document.getElementById('grammarTable');t.style.display=(t.style.display==='none'||!t.style.display)?'block':'none'">Reveal the Rule</button>
    <div id="grammarTable" style="display:none;max-width:680px;margin:1rem auto 0;overflow-x:auto;animation:fadeIn .4s ease">
      <table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.6rem;text-align:left">Use for</th><th style="padding:.6rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.5rem">Like / love / enjoy + verb-ing</td><td style="padding:.5rem">I love trying new dishes. I enjoy cooking.</td></tr>
          <tr style="background:var(--bg-elevated);border-bottom:1px solid var(--border)"><td style="padding:.5rem">Dislike: do not like / cannot stand + -ing</td><td style="padding:.5rem">I do not like eating late. I cannot stand wasting food.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.5rem">Agree (positive): So + do/am/can + I</td><td style="padding:.5rem">"I love spicy food." -- "So do I!"</td></tr>
          <tr><td style="padding:.5rem">Agree (negative): Neither + do/am/can + I</td><td style="padding:.5rem">"I do not eat meat." -- "Neither do I."</td></tr>
        </tbody>
      </table>
      <div style="background:var(--accent-dim);border:1px solid var(--accent);border-radius:8px;padding:.8rem;margin-top:.8rem">
        <p style="font-size:.82rem;color:var(--text-mid)"><strong>Key idea:</strong> after a verb of liking, use the <strong>-ing</strong> form. To agree with a positive sentence say <strong>So do I</strong>; to agree with a negative one say <strong>Neither do I</strong>. Say "I love <strong>trying</strong> food", never "I love <strong>try</strong> food".</p>
      </div>
    </div>
  </div>
</div>''')

# SLIDE 12 common mistake
slides.append(f'''
<!-- ========== SLIDE 12: COMMON MISTAKE ========== -->
<div class="slide slide-light" data-slide="12" data-lesson="20" data-phase="3" data-teacher="<strong>Common Mistake (2 min):</strong> Mostre o erro. Explique: depois de love/enjoy usamos -ing, nao o infinitivo simples; e para concordar com algo negativo usamos Neither do I, nao So do I. CCQ: 'After love, try or trying? (trying.) Someone says I do not like fish and you agree -- So do I or Neither do I? (Neither do I.)'">
  <div class="slide-inner">
    <div class="chapter-label">Common Mistake</div>
    <h2 class="slide-heading">Watch <span class="accent">Out</span></h2>
    <div class="mistake-card" style="max-width:540px;margin:1.2rem auto 0;background:var(--bg-card);border:1px solid var(--border);border-radius:12px;overflow:hidden">
      <div class="mistake-item" style="display:flex;align-items:flex-start;gap:.8rem;padding:1rem;border-bottom:1px solid var(--border);background:var(--danger-bg)">
        <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="var(--danger)" stroke-width="2.5" style="flex-shrink:0;margin-top:2px"><circle cx="12" cy="12" r="10"/><line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/></svg>
        <div style="font-size:.9rem;color:var(--danger)"><s>"I love <strong>try</strong> new dishes." / "I do not eat meat." -- "<strong>So do I</strong>."</s></div>
      </div>
      <div class="mistake-item" style="display:flex;align-items:flex-start;gap:.8rem;padding:1rem;background:var(--success-bg)">
        <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="var(--success)" stroke-width="2.5" style="flex-shrink:0;margin-top:2px"><path d="M22 11.08V12a10 10 0 11-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
        <div style="font-size:.9rem;color:var(--success)">"I love <strong>trying</strong> new dishes." / "I do not eat meat." -- "<strong>Neither do I</strong>."</div>
      </div>
    </div>
    <p style="font-size:.82rem;color:var(--text-dim);text-align:center;margin-top:1rem;max-width:540px;margin-left:auto;margin-right:auto">After <strong>like / love / enjoy</strong> use the <strong>-ing</strong> form. Agree with a negative idea using <strong>Neither do I</strong>, not So do I.</p>
  </div>
</div>''')

# SLIDE 13 grammar practice
gp = [
 ('"I love <span class="fill-blank">_____</span><span class="fill-answer">trying</span> new dishes." (try + -ing)'),
 ('"I enjoy <span class="fill-blank">_____</span><span class="fill-answer">cooking</span> on weekends." (cook + -ing)'),
 ('"I do not like <span class="fill-blank">_____</span><span class="fill-answer">eating</span> late at night." (eat + -ing)'),
 ('"I love savory food." -- "<span class="fill-blank">_____</span><span class="fill-answer">So do I</span>!" (agree, positive)'),
]
gprows = "\n".join(f'      <div class="fill-item" onclick="revealFill(this)"><div class="fill-text">{x}</div></div>' for x in gp)
slides.append(f'''
<!-- ========== SLIDE 13: GRAMMAR PRACTICE ========== -->
<div class="slide slide-light" data-slide="13" data-lesson="20" data-phase="3" data-teacher="<strong>Grammar Practice (4 min):</strong> Leia cada frase. Peca Rubens completar ORALMENTE antes de revelar. Clique para revelar a resposta. Corrija pronuncia. Peca que repita a frase completa. Se errar, volte ao slide 11 para rever a regra.">
  <div class="slide-inner">
    <div class="chapter-label">Grammar Practice</div>
    <h2 class="slide-heading">Complete the <span class="accent">Sentence</span></h2>
    <div style="display:flex;flex-direction:column;gap:.7rem;max-width:600px;margin:1.2rem auto 0">
{gprows}
    </div>
  </div>
</div>''')

# CHAPTER 4 (14-19): transition, listening1, comp, artefact, dialogue, listening2
slides.append(f'''
<!-- ============================================================ -->
<!-- CHAPTER 4: AT THE TABLE (slides 14-19, phase 4)             -->
<!-- ============================================================ -->

<!-- ========== SLIDE 14: CHAPTER TRANSITION ========== -->
<div class="slide slide-dark" data-slide="14" data-lesson="20" data-phase="4" data-teacher="<strong>Transicao contexto (1 min):</strong> Diga: 'Now the real situation. First you hear a food guide introduce the flavors of the city. Then you sit at a table and talk about what you like.' Crie expectativa." style="background-image:linear-gradient(rgba(20,20,30,.78),rgba(20,20,30,.88)),url('https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=1400&q=80');background-size:cover;background-position:center">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label">Chapter 4 -- At the Table</div>
    <h2 class="slide-heading" style="font-size:2rem;color:#fff">Food in <span class="accent">Real Life</span></h2>
    <p style="color:rgba(255,255,255,.6);font-size:1rem;margin-top:.5rem">From the food guide to the table</p>
  </div>
</div>''')

def player(pid, src, qid):
    return f'''    <div class="mp-player" id="{pid}" data-src="{src}" data-questions="{qid}" style="max-width:500px;margin:1.5rem auto 0;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:12px;padding:1.2rem">
      <div class="mp-bar" onclick="mpSeek(event,'{pid}')" style="width:100%;height:6px;background:rgba(255,255,255,.15);border-radius:3px;cursor:pointer;margin-bottom:.8rem"><div class="mp-fill" id="progress-{pid}" style="width:0%;height:100%;background:var(--accent);border-radius:3px;transition:width .1s"></div></div>
      <div class="mp-controls" style="display:flex;align-items:center;justify-content:center;gap:.8rem">
        <button onclick="mpSkip('{pid}',-5)" style="background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);color:#fff;border-radius:6px;padding:.4rem .6rem;font-size:.75rem;cursor:pointer">-5s</button>
        <button class="mp-play" id="play-{pid}" onclick="mpToggle('{pid}')" style="background:var(--accent);border:none;color:#fff;border-radius:50%;width:44px;height:44px;font-size:1.2rem;cursor:pointer;display:flex;align-items:center;justify-content:center"><span class="lp-icon-play">&#9654;</span><span class="lp-icon-pause" style="display:none">&#10074;&#10074;</span></button>
        <button onclick="mpSkip('{pid}',5)" style="background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);color:#fff;border-radius:6px;padding:.4rem .6rem;font-size:.75rem;cursor:pointer">+5s</button>
        <span class="mp-time" style="color:rgba(255,255,255,.6);font-size:.75rem;min-width:80px"><span id="time-current-{pid}">0:00</span> / <span id="time-total-{pid}">0:00</span></span>
      </div>
      <div class="mp-speed" style="display:flex;gap:.4rem;justify-content:center;margin-top:.6rem">
        <button class="lp-speed-btn" onclick="mpSpeed('{pid}',0.75,this)" style="background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.15);color:rgba(255,255,255,.7);border-radius:4px;padding:.2rem .5rem;font-size:.7rem;cursor:pointer">0.75x</button>
        <button class="lp-speed-btn active" onclick="mpSpeed('{pid}',1,this)" style="background:var(--accent);border:1px solid var(--accent);color:#fff;border-radius:4px;padding:.2rem .5rem;font-size:.7rem;cursor:pointer">1x</button>
        <button class="lp-speed-btn" onclick="mpSpeed('{pid}',1.25,this)" style="background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.15);color:rgba(255,255,255,.7);border-radius:4px;padding:.2rem .5rem;font-size:.7rem;cursor:pointer">1.25x</button>
      </div>
    </div>'''

# SLIDE 15 listening 1
slides.append(f'''
<!-- ========== SLIDE 15: LISTENING 1 ========== -->
<div class="slide slide-dark" data-slide="15" data-lesson="20" data-phase="4" data-teacher="<strong>Listening 1 (5 min):</strong> Diga: 'You hear the food guide introduce the flavors of the city. Listen carefully -- no text on screen. After the audio, I will ask you three questions.' Toque o audio. Deixe Rubens ouvir sem ajuda. Se necessario, toque novamente mais devagar. NAO mostre o texto. Perguntas no proximo slide.">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label" style="color:rgba(255,255,255,.6)">Listening 1</div>
    <h2 class="slide-heading" style="color:#fff">The Food Guide's <span class="accent">Welcome</span></h2>
    <p style="color:rgba(255,255,255,.5);font-size:.9rem;margin-top:.5rem">Listen first. Questions come next.</p>

{player('player1','/audio/rubens-tofolo/a20_listening1_sofia.mp3','listening1Questions')}
  </div>
</div>''')

# SLIDE 16 comp
def comp_q(n, q, a, dark=False):
    bg = "rgba(255,255,255,.08)" if dark else "var(--bg-card)"
    br = "rgba(255,255,255,.12)" if dark else "var(--border)"
    qc = "#fff" if dark else ""
    return f'''      <div class="comp-question" onclick="this.classList.toggle('revealed')" style="background:{bg};border:1px solid {br};border-radius:10px;padding:.9rem;cursor:pointer;transition:all .3s">
        <p style="font-size:.9rem;font-weight:600;{('color:'+qc) if qc else ''}">{n}. {q}</p>
        <p class="fill-answer" style="display:none;font-size:.88rem;color:var(--accent);margin-top:.5rem">{a}</p>
      </div>'''

slides.append(f'''
<!-- ========== SLIDE 16: LISTENING 1 COMPREHENSION ========== -->
<div class="slide slide-light" data-slide="16" data-lesson="20" data-phase="4" data-teacher="<strong>Comprehension (3 min):</strong> Peca Rubens responder cada pergunta ANTES de revelar. Clique para mostrar a resposta. Se errar, volte ao audio. CCQ adicional: 'What is the local specialty? (A fish stew with fresh ingredients.) What does the bakery owner make every morning? (Homemade bread.)'">
  <div class="slide-inner">
    <div class="chapter-label">Comprehension</div>
    <h2 class="slide-heading">About the <span class="accent">Welcome</span></h2>
    <div id="listening1Questions" style="display:flex;flex-direction:column;gap:.7rem;max-width:560px;margin:1.2rem auto 0">

{comp_q(1,"What is the local specialty, and how does the guide describe it?","A fish stew made with fresh ingredients and simple seasoning; it is hearty and warm.")}

{comp_q(2,"What does the bakery owner make every morning?","Homemade bread -- and the cheese bread is great for people who like savory food.")}

{comp_q(3,"What can visitors try at the central market?","Street food from many vendors.")}

    </div>
    <p style="font-size:.78rem;color:var(--text-dim);text-align:center;margin-top:.8rem">Click each question to reveal the answer</p>
  </div>
</div>''')

# SLIDE 17 artefact: menu / tasting card
slides.append(f'''
<!-- ========== SLIDE 17: ARTEFACT -- TASTING MENU ========== -->
<div class="slide slide-light" data-slide="17" data-lesson="20" data-phase="4" data-teacher="<strong>Artefato menu de degustacao (4 min):</strong> Diga: 'This is the tasting menu for Rubens'' food tour.' Peca Rubens ler cada linha em voz alta. Pergunte: 'What is the specialty? Which dish is savory? Is the dessert homemade?' Depois peca uma frase de gosto: 'I love trying the local specialty.'">
  <div class="slide-inner">
    <div class="chapter-label">Artefact</div>
    <h2 class="slide-heading">The Tasting <span class="accent">Menu</span></h2>
    <div style="max-width:560px;margin:1.2rem auto 0;background:#fff;border:1px solid var(--border);border-radius:12px;overflow:hidden;max-height:55vh;overflow-y:auto">
      <div style="background:#7c2d12;padding:.8rem 1rem;color:#fff">
        <p style="font-weight:700;font-size:.9rem;letter-spacing:.5px">OLD TOWN FOOD TOUR &middot; TASTING MENU</p>
        <p style="font-size:.74rem;color:rgba(255,255,255,.75);margin-top:.2rem">Guest: Rubens Tofolo &middot; Guide: Sofia &middot; 5 stops</p>
      </div>
      <div style="padding:1.2rem;font-size:.86rem;line-height:1.6;color:#2d2d3a">
        <div style="display:flex;justify-content:space-between;background:var(--bg-elevated);border:1px solid var(--border);border-radius:8px;padding:.6rem .8rem;margin-bottom:.5rem">
          <span><strong>Stop 1 -- Market</strong></span><span style="color:var(--text-dim)">Street food, many vendors</span>
        </div>
        <div style="display:flex;justify-content:space-between;background:var(--bg-elevated);border:1px solid var(--border);border-radius:8px;padding:.6rem .8rem;margin-bottom:.5rem">
          <span><strong>Stop 2 -- Specialty</strong></span><span style="color:var(--text-dim)">Fish stew -- fresh ingredients</span>
        </div>
        <div style="display:flex;justify-content:space-between;background:var(--bg-elevated);border:1px solid var(--border);border-radius:8px;padding:.6rem .8rem;margin-bottom:.5rem">
          <span><strong>Stop 3 -- Bakery</strong></span><span style="color:var(--text-dim)">Homemade bread (savory)</span>
        </div>
        <div style="display:flex;justify-content:space-between;background:var(--bg-elevated);border:1px solid var(--border);border-radius:8px;padding:.6rem .8rem;margin-bottom:.5rem">
          <span><strong>Stop 4 -- Delicacy</strong></span><span style="color:var(--text-dim)">Regional cheese with seasoning</span>
        </div>
        <div style="display:flex;justify-content:space-between;background:#7c2d12;border-radius:8px;padding:.7rem .8rem;color:#fff;margin-top:.6rem">
          <span style="font-weight:700">Stop 5 -- Dessert</span><span>Homemade, included in your ticket</span>
        </div>
      </div>
    </div>
  </div>
</div>''')

# SLIDE 18 dialogue
def dline(n, voice, av, avbg, name, bubble_bg, bubble_br, txt, audio):
    return f'''      <div class="dialogue-line{' visible' if n==1 else ''}" data-line="{n}" data-voice="{voice}">
        <div class="dialogue-avatar {name}" style="background:{avbg};width:36px;height:36px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:.85rem;flex-shrink:0">{av}</div>
        <div class="dialogue-bubble {name}-bubble" style="background:{bubble_bg};border:1px solid {bubble_br};border-radius:10px;padding:.7rem;flex:1">
          <p style="font-size:.88rem;color:#fff">"{txt}"</p>
          <button class="audio-btn-sm" data-voice="{voice}" onclick="event.stopPropagation();speakText('{esc(audio)}',this)" style="margin-top:.4rem"><svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button>
        </div>
      </div>'''

S_BG, S_BR = "rgba(255,255,255,.1)","rgba(255,255,255,.15)"
R_BG, R_BR = "rgba(51,107,135,.2)","rgba(51,107,135,.3)"
dialogue = [
 (1,"ellen","S","#8a5a2d","sofia",S_BG,S_BR,"Welcome to the table, Rubens. Our specialty today is a fish stew. Do you enjoy trying local dishes?","Welcome to the table, Rubens. Our specialty today is a fish stew. Do you enjoy trying local dishes?"),
 (2,"arthur","R","#336B87","rubens",R_BG,R_BR,"Yes, I love trying new cuisine. The flavor smells wonderful. What are the main ingredients?","Yes, I love trying new cuisine. The flavor smells wonderful. What are the main ingredients?"),
 (3,"ellen","S","#8a5a2d","sofia",S_BG,S_BR,"Fresh fish, tomatoes, and a little seasoning. I love cooking it at home too.","Fresh fish, tomatoes, and a little seasoning. I love cooking it at home too."),
 (4,"arthur","R","#336B87","rubens",R_BG,R_BR,"So do I! But I cannot stand very spicy food. Is this dish savory or hot?","So do I! But I cannot stand very spicy food. Is this dish savory or hot?"),
 (5,"ellen","S","#8a5a2d","sofia",S_BG,S_BR,"It is savory, not hot. And for dessert there is homemade cake. I do not like eating too much sugar, though.","It is savory, not hot. And for dessert there is homemade cake. I do not like eating too much sugar, though."),
 (6,"arthur","R","#336B87","rubens",R_BG,R_BR,"Neither do I. This is exactly the kind of meal that I enjoy the most. Let's eat!","Neither do I. This is exactly the kind of meal that I enjoy the most. Let us eat!"),
]
dlines = "\n\n".join(dline(*d) for d in dialogue)
slides.append(f'''
<!-- ========== SLIDE 18: DIALOGUE ========== -->
<div class="slide slide-dark" data-slide="18" data-lesson="20" data-phase="4" data-teacher="<strong>Dialogo (5 min):</strong> Clique 'Next Line' para revelar cada fala. Toque o audio e peca Rubens repetir as falas dele. Corrija pronuncia. Destaque os verbos de gosto + -ing e as reacoes So do I / Neither do I. Pergunte: 'What is the specialty? (A fish stew.) Is the dish savory or hot? (Savory.)' Apos todas as linhas, peca Rubens reagir a uma frase com So do I ou Neither do I.">
  <div class="slide-inner">
    <div class="chapter-label">Dialogue</div>
    <h2 class="slide-heading" style="color:#fff">At the <span class="accent">Table</span></h2>
    <div class="dialogue-box" id="dialogue1" style="max-width:560px;margin:1rem auto 0;max-height:340px;overflow-y:auto">

{dlines}

    </div>
    <button class="primary-btn" id="nextLineBtn" onclick="nextDialogueLine()" style="margin:1rem auto 0;display:block;background:var(--accent);color:#fff;border:none;border-radius:8px;padding:.6rem 1.4rem;font-size:.9rem;font-weight:600;cursor:pointer">Next Line</button>
  </div>
</div>''')

# SLIDE 19 listening 2 (with inline questions, dark)
slides.append(f'''
<!-- ========== SLIDE 19: LISTENING 2 ========== -->
<div class="slide slide-dark" data-slide="19" data-lesson="20" data-phase="4" data-teacher="<strong>Listening 2 (5 min):</strong> Diga: 'Now listen to Rubens describe how he enjoys food when he travels.' Toque o audio. Depois revele as perguntas e peca Rubens responder. CCQ: 'Why does he love street food? (Simple, fresh, full of flavor.) Why does he not enjoy eating at the hotel? (The food is always the same.)'">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label" style="color:rgba(255,255,255,.6)">Listening 2</div>
    <h2 class="slide-heading" style="color:#fff">A Doctor Who <span class="accent">Loves Food</span></h2>
    <p style="color:rgba(255,255,255,.5);font-size:.9rem;margin-top:.5rem">Listen first. Questions come next.</p>

{player('player2','/audio/rubens-tofolo/a20_listening2_rubens.mp3','listening2Questions')}

    <div id="listening2Questions" style="display:none;max-width:500px;margin:1.2rem auto 0">
      <div class="comp-question" onclick="this.classList.toggle('revealed')" style="background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.12);border-radius:10px;padding:.8rem;cursor:pointer;margin-bottom:.5rem">
        <p style="font-size:.88rem;font-weight:600;color:#fff">1. Why does Rubens love eating street food?</p>
        <p class="fill-answer" style="display:none;font-size:.85rem;color:var(--accent);margin-top:.4rem">Because it is simple, fresh, and full of flavor.</p>
      </div>
      <div class="comp-question" onclick="this.classList.toggle('revealed')" style="background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.12);border-radius:10px;padding:.8rem;cursor:pointer;margin-bottom:.5rem">
        <p style="font-size:.88rem;font-weight:600;color:#fff">2. Why does he not enjoy eating at the hotel?</p>
        <p class="fill-answer" style="display:none;font-size:.85rem;color:var(--accent);margin-top:.4rem">Because the food is always the same.</p>
      </div>
      <div class="comp-question" onclick="this.classList.toggle('revealed')" style="background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.12);border-radius:10px;padding:.8rem;cursor:pointer">
        <p style="font-size:.88rem;font-weight:600;color:#fff">3. What did a colleague take him to try on his last trip?</p>
        <p class="fill-answer" style="display:none;font-size:.85rem;color:var(--accent);margin-top:.4rem">A regional delicacy -- a savory dish with an unusual seasoning.</p>
      </div>
    </div>
  </div>
</div>''')

# CHAPTER 5 practice (20-22)
qf = [
 ("Say what you love eating from a local cuisine.","I love trying the local cuisine."),
 ("React to: \"I enjoy cooking at home.\" (you agree).","So do I!"),
 ("Say one food you cannot stand.","I cannot stand eating very spicy food."),
 ("React to: \"I do not like eating late at night.\" (you agree).","Neither do I."),
]
def qf_card(i, q, a, last=False):
    nxt = ('<p style="font-size:.78rem;color:var(--text-dim);margin-top:.5rem">All questions complete!</p>'
           if last else '<button onclick="nextQF()" style="background:var(--accent);color:#fff;border:none;border-radius:8px;padding:.5rem 1.2rem;font-size:.85rem;font-weight:600;cursor:pointer">Next Question</button>')
    disp = "" if i==1 else 'display:none;'
    return f'''      <div class="qf-card" data-qf="{i}" style="{disp}background:var(--bg-card);border:1px solid var(--border);border-radius:12px;padding:1.2rem">
        <p style="font-size:.92rem;font-weight:600;margin-bottom:.6rem">{q}</p>
        <button class="primary-btn qf-show" onclick="this.style.display='none';this.nextElementSibling.style.display='block'" style="background:var(--accent);color:#fff;border:none;border-radius:8px;padding:.5rem 1.2rem;font-size:.85rem;font-weight:600;cursor:pointer">Show Answer</button>
        <div class="qf-answer" style="display:none">
          <p style="font-size:.88rem;color:var(--accent);font-weight:500;margin-bottom:.6rem">"{a}"</p>
          {nxt}
        </div>
      </div>'''
qfcards = "\n\n".join(qf_card(i+1,q,a,last=(i==len(qf)-1)) for i,(q,a) in enumerate(qf))
slides.append(f'''
<!-- ============================================================ -->
<!-- CHAPTER 5: PRACTICE (slides 20-22, phase 5)                 -->
<!-- ============================================================ -->

<!-- ========== SLIDE 20: QUICK FIRE ========== -->
<div class="slide slide-light" data-slide="20" data-lesson="20" data-phase="5" data-teacher="<strong>Quick Fire (4 min):</strong> Uma situacao por vez. Leia, Rubens responde usando um verbo de gosto + -ing ou uma reacao (So do I / Neither do I). Clique 'Show Answer' para revelar a sugestao. Clique 'Next Question' para avancar. Se travar, de o inicio: 'I love...' ou 'So do I!'">
  <div class="slide-inner">
    <div class="chapter-label">Quick Fire</div>
    <h2 class="slide-heading">Talk About <span class="accent">Food</span></h2>
    <p style="text-align:center;font-size:.82rem;color:var(--text-dim);margin-top:.3rem"><span id="qfScore">0 / 4</span></p>
    <div id="qfContainer" style="max-width:520px;margin:1rem auto 0">

{qfcards}

    </div>
  </div>
</div>''')

# SLIDE 21 spot the error
err = [
 ('I love <span style="color:var(--danger);text-decoration:line-through;font-weight:600">cook</span> at home.','I love <strong>cooking</strong> at home.'),
 ('I enjoy <span style="color:var(--danger);text-decoration:line-through;font-weight:600">to try</span> new dishes.','I enjoy <strong>trying</strong> new dishes.'),
 ('"I do not eat meat." -- "<span style="color:var(--danger);text-decoration:line-through;font-weight:600">So do I</span>."','"I do not eat meat." -- "<strong>Neither do I</strong>."'),
 ('I cannot stand <span style="color:var(--danger);text-decoration:line-through;font-weight:600">waste</span> food.','I cannot stand <strong>wasting</strong> food.'),
]
def err_card(bad, good):
    return f'''      <div class="error-card" onclick="revealError(this)" style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:.9rem;cursor:pointer;transition:all .3s">
        <p style="font-size:.9rem">"{bad}"</p>
        <p class="fill-answer" style="display:none;font-size:.88rem;color:var(--success);font-weight:600;margin-top:.5rem">"{good}"</p>
      </div>'''
errcards = "\n\n".join(err_card(b,g) for b,g in err)
slides.append(f'''
<!-- ========== SLIDE 21: SPOT THE ERROR ========== -->
<div class="slide slide-light" data-slide="21" data-lesson="20" data-phase="5" data-teacher="<strong>Spot the Error (3 min):</strong> Leia cada frase. Peca Rubens identificar o erro. Clique no card para revelar a correcao. CCQ apos cada erro: 'After love/enjoy, do we use -ing or to? (-ing.) To agree with a negative, So do I or Neither do I? (Neither do I.)'">
  <div class="slide-inner">
    <div class="chapter-label">Spot the Error</div>
    <h2 class="slide-heading">Find the <span class="accent">Mistake</span></h2>
    <p style="text-align:center;font-size:.82rem;color:var(--text-dim);margin-top:.3rem"><span id="errorScore">0 / 4 errors found</span></p>
    <div class="error-grid" style="display:flex;flex-direction:column;gap:.7rem;max-width:580px;margin:1rem auto 0">

{errcards}

    </div>
    <p style="font-size:.78rem;color:var(--text-dim);text-align:center;margin-top:.8rem">Click each card to reveal the correction</p>
  </div>
</div>''')

# SLIDE 22 grammar fill-in (vocab combined)
mp = [
 ('"The local <span class="fill-blank">_____</span><span class="fill-answer">specialty</span> is a fish stew." (a dish a place is famous for)'),
 ('"This dish has a rich, deep <span class="fill-blank">_____</span><span class="fill-answer">flavor</span>." (the taste of food)'),
 ('"The owner makes <span class="fill-blank">_____</span><span class="fill-answer">homemade</span> bread every morning." (made at home)'),
 ('"After the walk, we had a <span class="fill-blank">_____</span><span class="fill-answer">hearty</span> meal." (large and satisfying)'),
]
mprows = "\n".join(f'      <div class="fill-item" onclick="revealFill(this)"><div class="fill-text">{x}</div></div>' for x in mp)
slides.append(f'''
<!-- ========== SLIDE 22: MORE PRACTICE ========== -->
<div class="slide slide-light" data-slide="22" data-lesson="20" data-phase="5" data-teacher="<strong>Grammar fill-in (3 min):</strong> Leia cada frase. Rubens completa ORALMENTE. Clique para revelar. Estas frases combinam os verbos de gosto com o vocabulario da aula: specialty, flavor, homemade, hearty. Destaque isso.">
  <div class="slide-inner">
    <div class="chapter-label">More Practice</div>
    <h2 class="slide-heading">Complete the <span class="accent">Sentence</span></h2>
    <div style="display:flex;flex-direction:column;gap:.7rem;max-width:600px;margin:1.2rem auto 0">
{mprows}
    </div>
  </div>
</div>''')

# CHAPTER 6 your turn (23-26)
slides.append(f'''
<!-- ============================================================ -->
<!-- CHAPTER 6: YOUR TURN (slides 23-26, phase 6)                -->
<!-- ============================================================ -->

<!-- ========== SLIDE 23: ROLE-PLAY GUIDED ========== -->
<div class="slide slide-dark" data-slide="23" data-lesson="20" data-phase="6" data-teacher="<strong>Role-play Guided (3 min):</strong> Diga: 'Your turn. I am the food guide at the table. Tell me what local food you love trying and ask about the specialty. Use the keywords on screen.' Seja a guia. Corrija erros ao FINAL, nao durante. Anote erros para o feedback.">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label" style="color:rgba(255,255,255,.6)">Your Turn -- Guided</div>
    <h2 class="slide-heading" style="color:#fff">Sit at the <span class="accent">Table</span></h2>
    <div style="max-width:480px;margin:1.5rem auto 0;background:linear-gradient(135deg,rgba(51,107,135,.15),rgba(51,107,135,.08));border:1px solid rgba(51,107,135,.25);border-radius:16px;padding:1.5rem;text-align:center">
      <svg viewBox="0 0 24 24" width="40" height="40" fill="none" stroke="var(--accent-light)" stroke-width="1.5" style="margin-bottom:.8rem"><path d="M3 11h18"/><path d="M5 11a7 7 0 0 0 14 0"/><line x1="12" y1="19" x2="12" y2="22"/></svg>
      <p style="font-size:.95rem;font-weight:600;color:#fff;margin-bottom:.8rem">Welcome! Our specialty today is a fish stew. Do you enjoy trying local food?</p>
      <div style="display:flex;flex-wrap:wrap;gap:.4rem;justify-content:center;margin-top:.8rem">
        <span style="background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:.3rem .7rem;font-size:.78rem;color:rgba(255,255,255,.8)">I love trying</span>
        <span style="background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:.3rem .7rem;font-size:.78rem;color:rgba(255,255,255,.8)">specialty</span>
        <span style="background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:.3rem .7rem;font-size:.78rem;color:rgba(255,255,255,.8)">ingredients</span>
      </div>
    </div>
  </div>
</div>''')

slides.append(f'''
<!-- ========== SLIDE 24: ROLE-PLAY SEMI-FREE ========== -->
<div class="slide slide-dark" data-slide="24" data-lesson="20" data-phase="6" data-teacher="<strong>Role-play Semi-free (3 min):</strong> Diga: 'Now tell me two foods you love and one you cannot stand. I will react, and you react to me with So do I or Neither do I.' Menos keywords. Avalie se Rubens usa verbo + -ing e as reacoes espontaneamente. Corrija ao final.">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label" style="color:rgba(255,255,255,.6)">Your Turn -- Semi-free</div>
    <h2 class="slide-heading" style="color:#fff">Likes &amp; <span class="accent">Dislikes</span></h2>
    <div style="max-width:480px;margin:1.5rem auto 0;background:linear-gradient(135deg,rgba(74,142,176,.15),rgba(74,142,176,.08));border:1px solid rgba(74,142,176,.25);border-radius:16px;padding:1.5rem;text-align:center">
      <svg viewBox="0 0 24 24" width="40" height="40" fill="none" stroke="#7fb2cc" stroke-width="1.5" style="margin-bottom:.8rem"><path d="M12 21s-7-4.5-9.5-9A5 5 0 0 1 12 6a5 5 0 0 1 9.5 6C19 16.5 12 21 12 21z"/></svg>
      <p style="font-size:.95rem;font-weight:600;color:#fff;margin-bottom:.8rem">Tell me two foods you love and one you cannot stand -- then react to me.</p>
      <div style="display:flex;flex-wrap:wrap;gap:.4rem;justify-content:center;margin-top:.8rem">
        <span style="background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:.3rem .7rem;font-size:.78rem;color:rgba(255,255,255,.8)">love / enjoy + -ing</span>
        <span style="background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:.3rem .7rem;font-size:.78rem;color:rgba(255,255,255,.8)">cannot stand</span>
        <span style="background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:20px;padding:.3rem .7rem;font-size:.78rem;color:rgba(255,255,255,.8)">So do I / Neither do I</span>
      </div>
    </div>
  </div>
</div>''')

slides.append(f'''
<!-- ========== SLIDE 25: ROLE-PLAY FREE ========== -->
<div class="slide slide-dark" data-slide="25" data-lesson="20" data-phase="6" data-teacher="<strong>Role-play Free (3 min):</strong> Diga: 'Final challenge. No keywords. Tell me about the cuisine of your region: describe one specialty, its main ingredients and flavor, and say what you love eating and what you cannot stand.' Avalie fluencia, vocabulario e o uso correto de verbo + -ing e das reacoes. Anote pontos fortes e areas de melhoria. Esta e a ultima producao do pacote -- celebre.">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label" style="color:rgba(255,255,255,.6)">Your Turn -- Free</div>
    <h2 class="slide-heading" style="color:#fff">Your Own <span class="accent">Cuisine</span></h2>
    <div style="max-width:480px;margin:1.5rem auto 0;background:linear-gradient(135deg,rgba(51,107,135,.12),rgba(74,142,176,.08));border:1px solid rgba(51,107,135,.2);border-radius:16px;padding:1.5rem;text-align:center">
      <svg viewBox="0 0 24 24" width="40" height="40" fill="none" stroke="var(--accent-light)" stroke-width="1.5" style="margin-bottom:.8rem"><path d="M12 20h9"/><path d="M16.5 3.5a2.12 2.12 0 013 3L7 19l-4 1 1-4z"/></svg>
      <p style="font-size:.95rem;font-weight:600;color:#fff;margin-bottom:.8rem">Describe the cuisine of your region: a specialty, its ingredients and flavor, and what you love eating and cannot stand.</p>
      <p style="font-size:.82rem;color:rgba(255,255,255,.5);margin-top:.6rem">No keywords. Show everything you have learned.</p>
    </div>
  </div>
</div>''')

# SLIDE 26 dialogue comprehension
slides.append(f'''
<!-- ========== SLIDE 26: DIALOGUE COMPREHENSION ========== -->
<div class="slide slide-light" data-slide="26" data-lesson="20" data-phase="6" data-teacher="<strong>Dialogue Comprehension (2 min):</strong> Peca Rubens responder ANTES de revelar. Estas perguntas testam a conversa com a guia (slide 18). CCQ final: 'What is the specialty? (A fish stew.) Is the dish savory or hot? (Savory.)'">
  <div class="slide-inner">
    <div class="chapter-label">Dialogue Review</div>
    <h2 class="slide-heading">About the <span class="accent">Meal</span></h2>
    <div style="display:flex;flex-direction:column;gap:.7rem;max-width:560px;margin:1.2rem auto 0">

{comp_q(1,"What is the specialty, and what are its main ingredients?","A fish stew made with fresh fish, tomatoes, and a little seasoning.")}

{comp_q(2,"How does Rubens react when Sofia says she loves cooking it at home?","He says &quot;So do I!&quot; because he agrees.")}

{comp_q(3,"What does Rubens say about very spicy food?","He cannot stand it, but the dish is savory, not hot.")}

    </div>
    <p style="font-size:.78rem;color:var(--text-dim);text-align:center;margin-top:.8rem">Click each question to reveal the answer</p>
  </div>
</div>''')

# CHAPTER 7 wrap-up (27-28)
sc = [
 "I love trying the local cuisine.",
 "I enjoy cooking with fresh ingredients.",
 "I cannot stand eating very spicy food.",
 '"I do not eat much sugar." "Neither do I."',
 "What is the specialty of this region?",
]
def sc_row(i, txt):
    audio = txt.replace('"','')
    return f'''      <div style="background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:10px;padding:.8rem;display:flex;justify-content:space-between;align-items:center;gap:.6rem">
        <div style="display:flex;align-items:center;gap:.6rem"><span style="background:var(--accent);color:#fff;width:26px;height:26px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.75rem;flex-shrink:0">{i}</span><p style="font-size:.88rem;color:#fff">{txt}</p></div>
        <button class="audio-btn-sm" onclick="speakText('{esc(audio)}',this)"><svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button>
      </div>'''
scrows = "\n\n".join(sc_row(i+1,t) for i,t in enumerate(sc))
slides.append(f'''
<!-- ============================================================ -->
<!-- CHAPTER 7: WRAP-UP (slides 27-28, phase 7)                  -->
<!-- ============================================================ -->

<!-- ========== SLIDE 27: SURVIVAL CARD ========== -->
<div class="slide slide-dark" data-slide="27" data-lesson="20" data-phase="7" data-teacher="<strong>Survival Card (3 min):</strong> Diga: 'These are your five key phrases for food and culture. Listen, repeat each one, and memorize them.' Toque cada audio e peca Rubens repetir. Corrija pronuncia e entonacao.">
  <div class="slide-inner">
    <div class="chapter-label" style="color:rgba(255,255,255,.6)">Survival Card</div>
    <h2 class="slide-heading" style="color:#fff">5 Key <span class="accent">Phrases</span></h2>
    <div style="display:flex;flex-direction:column;gap:.6rem;max-width:540px;margin:1.2rem auto 0">

{scrows}

    </div>
  </div>
</div>''')

# SLIDE 28 what I learned + preview/close
checks = [
 "I can talk about local cuisine and dishes",
 "I can say what I like and love with a verb + -ing",
 "I can say what I dislike (do not like / cannot stand)",
 "I can agree with So do I and Neither do I",
 "I know 12 new words about food and culture",
]
def chk(t):
    return f'''      <div class="check-item" onclick="this.classList.toggle('checked')" style="display:flex;align-items:center;gap:.7rem;padding:.7rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;cursor:pointer;transition:all .2s">
        <svg class="check-svg" viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
        <span style="font-size:.9rem">{t}</span>
      </div>'''
chkrows = "\n".join(chk(t) for t in checks)
slides.append(f'''
<!-- ========== SLIDE 28: WHAT I LEARNED ========== -->
<div class="slide slide-light" data-slide="28" data-lesson="20" data-phase="7" data-teacher="<strong>Wrap-up (3 min):</strong> Peca Rubens clicar nos checks enquanto voce resume a aula. Marque os 5 itens. Diga: 'Congratulations, Rubens! This was the final lesson of your block. Today you learned 12 food and culture words and how to talk about what you like and dislike eating, and how to agree with So do I and Neither do I. You have completed all 20 lessons!' Homework (oral): 'Record a one-minute description of your favorite cuisine: name a specialty, its ingredients and flavor, and say what you love eating and cannot stand.' Nao ha preview -- celebre o fim do pacote.">
  <div class="slide-inner">
    <div class="chapter-label">Wrap-up</div>
    <h2 class="slide-heading">What I <span class="accent">Learned</span></h2>
    <div class="check-grid" data-lesson="20" style="display:flex;flex-direction:column;gap:.5rem;max-width:520px;margin:1.2rem auto 0">
{chkrows}
    </div>
    <div style="max-width:520px;margin:1.5rem auto 0;background:var(--accent-dim);border:1px solid var(--accent);border-radius:12px;padding:1.2rem;text-align:center">
      <h3 style="font-size:1.1rem;font-weight:700;color:var(--accent)">Day 20 -- Food &amp; Culture Complete</h3>
      <p style="font-size:.88rem;color:var(--text-dim);margin-top:.5rem">Milestone reached: <strong>20 of 20 lessons complete</strong>. Congratulations, Rubens!</p>
    </div>
  </div>
</div>''')

SLIDES = "\n".join(slides) + "\n"
open(os.path.join(HERE,'slides.html'),'w',encoding='utf-8').write(SLIDES)
print("slides.html written", SLIDES.count('data-slide='), "slides")

# ---- write listening/order texts to a side file for config build ----
TEXTS = {"listen1":LISTEN1,"listen2":LISTEN2,"order":ORDER_TXT}
open(os.path.join(HERE,'_texts.json'),'w',encoding='utf-8').write(json.dumps(TEXTS,ensure_ascii=False,indent=1))
print("texts written")
