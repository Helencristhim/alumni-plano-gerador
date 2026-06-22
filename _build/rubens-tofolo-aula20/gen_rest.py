# -*- coding: utf-8 -*-
"""Gera preclass.html, complementary.html, config.json para aula 20."""
import json, os, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("gc", os.path.join(HERE,"gen_content.py"))
# reuse VOCAB by re-importing constants
import runpy
ns = {'__file__': os.path.join(HERE,"gen_content.py"), '__name__':'gc'}
exec(compile(open(os.path.join(HERE,"gen_content.py")).read(), os.path.join(HERE,"gen_content.py"), "exec"), ns)
VOCAB = ns['VOCAB']
TEXTS = json.load(open(os.path.join(HERE,'_texts.json'),encoding='utf-8'))

# matching translations (PT gloss short, deduped)
# Build short match value per word
MATCH = [
 ("Cuisine","culin&#225;ria"),("Specialty","especialidade"),("Flavor","sabor"),("Ingredient","ingrediente"),
 ("Recipe","receita"),("Savory","salgado"),("Staple","alimento b&#225;sico"),("Seasoning","tempero"),
 ("Homemade","caseiro"),("Street food","comida de rua"),("Delicacy","iguaria"),("Hearty","substancial"),
]
ALLVALS = [m[1] for m in MATCH]

def shuffle_opts(answer):
    # deterministic shuffle: put answer at index 2, rest rotated
    rest = [v for v in ALLVALS if v != answer]
    return [rest[0], rest[1], answer] + rest[2:]

def match_row(word, answer):
    opts = shuffle_opts(answer)
    optlist = '<option value="">Selecione...</option>' + "".join(f'<option value="{o}">{o}</option>' for o in opts)
    return f'''        <div class="match-row" data-answer="{answer}"><span class="match-word" style="flex:0 0 130px">{word}</span><select style="flex:1;width:100%" onchange="checkMatch(this)">{optlist}</select></div>'''

# ---- vocab cards (pre-class) ----
def pc_card(v):
    word, defen, ex, pt, *_ = v
    return f'''        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header"><span class="vocab-card-word">{word}</span><span class="vocab-card-dot"> -- </span><span class="vocab-card-def">{defen.lower()[0]+defen[1:] if False else defen}</span></div><div class="vocab-card-example">{ex} ({pt})</div></div><button class="audio-btn" onclick="speakText('{word.replace("'","\\'")}',this)">Listen</button></div>'''

pc_cards = "\n".join(pc_card(v) for v in VOCAB)
match_rows = "\n".join(match_row(w,a) for w,a in MATCH)

PRECLASS = f'''<div class="lesson-card" id="ex-lesson-20">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Aula 20 -- Pre-class</div>
      <h3>Food &amp; Culture</h3>
      <div class="lesson-desc">Explore local cuisine and say what you like and dislike eating with verbs of liking (love / enjoy / cannot stand + -ing) and react with So do I / Neither do I. New vocabulary: cuisine, specialty, flavor, ingredient, recipe, savory, staple, seasoning, homemade, street food, delicacy, hearty.</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="20" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="20">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each word and read the example. Tap Listen to hear it.</p>
      <div class="vocab-cards">
{pc_cards}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each word with its translation.</p>
      <div class="match-grid" id="match-l20">
{match_rows}
      </div>
      <button class="verify-all-btn" onclick="verifyAllMatches('match-l20')">Check Answers</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text and answer the questions.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>On a free evening, Rubens joins a food tour. "I <strong>love trying</strong> the local <strong>cuisine</strong>," he says. The guide smiles: "<strong>So do I!</strong>" The first <strong>specialty</strong> is a <strong>hearty</strong> fish stew made with fresh <strong>ingredients</strong> and a little <strong>seasoning</strong>. Rubens <strong>enjoys eating</strong> savory food, but he <strong>cannot stand</strong> very spicy dishes. Next, a <strong>vendor</strong> sells <strong>homemade</strong> bread, a <strong>staple</strong> of the region. For dessert there is a local <strong>delicacy</strong>. "I <strong>do not like eating</strong> too much sugar," says the guide. "<strong>Neither do I</strong>," answers Rubens. The <strong>flavor</strong> of every dish tells a story about the culture.</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. After "love" and "enjoy", which verb form does the text use?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> The -ing form (trying, eating).</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> The simple infinitive (try, eat).</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> The past form (tried, ate).</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. How does Rubens agree with the negative sentence about sugar?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "So do I."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Neither do I."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Me too."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. What is the regional staple in the text?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> The fish stew.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> The homemade bread.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> The dessert.</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Verbs of Liking + -ing / So do I, Neither do I</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Depois de verbos de gosto (<em>like, love, enjoy, prefer, do not like, can't stand</em>) usamos o verbo com <strong>-ing</strong>. Para concordar: <em>So do I</em> (frase positiva) e <em>Neither do I</em> (frase negativa). / After verbs of liking (<em>like, love, enjoy, prefer, do not like, can't stand</em>) we use the verb with <strong>-ing</strong>. To agree: <em>So do I</em> (positive) and <em>Neither do I</em> (negative).</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form / Forma</th><th style="padding:.7rem;text-align:left">Example / Exemplo</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem">love / enjoy + verb-ing</td><td style="padding:.6rem">I love trying new dishes. / Eu adoro experimentar pratos novos.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem">do not like / can't stand + -ing</td><td style="padding:.6rem">I cannot stand wasting food. / N&#227;o suporto desperdi&#231;ar comida.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem">Agree (positive): So + do + I</td><td style="padding:.6rem">"I love spicy food." "So do I." / "Eu tamb&#233;m."</td></tr>
          <tr><td style="padding:.6rem">Agree (negative): Neither + do + I</td><td style="padding:.6rem">"I do not eat meat." "Neither do I." / "Eu tamb&#233;m n&#227;o."</td></tr>
        </tbody>
      </table></div>
      <div style="background:var(--accent-dim);border:1px solid var(--accent);border-radius:8px;padding:.8rem;margin-top:.8rem"><p style="font-size:.82rem;color:var(--text-mid)"><strong>Key point / Ponto-chave:</strong> diga "I love <strong>trying</strong>", nunca "I love <strong>try</strong>". Concorde com algo negativo usando <strong>Neither do I</strong>, n&#227;o "So do I".</p></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the correct word. Tap Listen to hear the full sentence.</p>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"I love <input class="blank-input" data-answer="trying" data-hint="Hint: try + -ing" data-phrase="I love trying the local cuisine." placeholder="___"> the local cuisine."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"I enjoy <input class="blank-input" data-answer="cooking" data-hint="Hint: cook + -ing" data-phrase="I enjoy cooking with fresh ingredients." placeholder="___"> with fresh ingredients."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"I cannot stand <input class="blank-input" data-answer="eating" data-hint="Hint: eat + -ing" data-phrase="I cannot stand eating very spicy food." placeholder="___"> very spicy food."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"The local <input class="blank-input" data-answer="specialty" data-hint="Hint: a dish a place is famous for" data-phrase="The local specialty is a fish stew." placeholder="___"> is a fish stew."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"The owner makes <input class="blank-input" data-answer="homemade" data-hint="Hint: made at home" data-phrase="The owner makes homemade bread every morning." placeholder="___"> bread every morning."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"\\"I do not eat much sugar.\\" \\"<input class="blank-input" data-answer="Neither" data-alt="neither" data-hint="Hint: agree with a negative idea" data-phrase="Neither do I." placeholder="___"> do I.\\""</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Food-Tour Steps in Sequence</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen first, then put the steps for exploring the food of a city in the correct order.</p>
      <button class="btn btn-listen" onclick="speakText('[order-l20]', this)" style="margin-bottom:1rem;display:inline-flex;align-items:center;gap:.4rem;padding:.55rem 1.2rem;background:var(--accent);color:#fff;border:none;border-radius:8px;font-size:.85rem;font-weight:600;cursor:pointer"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/></svg> Listen</button>
      <div class="order-container" id="order-l20">
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l20')"><span class="order-num">?</span><span class="order-text">After that, I taste a homemade dish made with fresh ingredients.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l20')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l20')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l20')"><span class="order-num">?</span><span class="order-text">First, I find a market where I can try street food.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l20')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l20')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l20')"><span class="order-num">?</span><span class="order-text">Finally, I sit down and enjoy a hearty meal with new friends.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l20')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l20')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l20')"><span class="order-num">?</span><span class="order-text">Then I look for the local specialty that everyone recommends.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l20')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l20')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l20')"><span class="order-num">?</span><span class="order-text">Next, I ask the vendor about the seasoning and the recipe.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l20')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l20')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l20')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each phrase, then record yourself saying it.</p>
      <div class="speech-card" data-phrase="I love trying the local cuisine.">
        <div class="speech-phrase">I love trying the local cuisine.</div>
        <div class="speech-translation">Eu adoro experimentar a culin&#225;ria local.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="I enjoy cooking with fresh ingredients.">
        <div class="speech-phrase">I enjoy cooking with fresh ingredients.</div>
        <div class="speech-translation">Eu gosto de cozinhar com ingredientes frescos.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="I cannot stand eating very spicy food.">
        <div class="speech-phrase">I cannot stand eating very spicy food.</div>
        <div class="speech-translation">N&#227;o suporto comer comida muito apimentada.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="The local specialty is a hearty fish stew.">
        <div class="speech-phrase">The local specialty is a hearty fish stew.</div>
        <div class="speech-translation">A especialidade local &#233; um ensopado de peixe substancial.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best phrase for each situation.</p>
      <div class="quiz-item"><div class="quiz-question">You want to say you like cooking. Which is correct?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I enjoy cook."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I enjoy cooking."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I enjoy to cook."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">A friend says "I love spicy food." You feel the same. What do you say?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "So do I!"</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Neither do I."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I am too."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">A friend says "I do not like fast food." You agree. What do you say?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "So do I."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Neither do I."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Yes, I do."</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. There is no right or wrong answer.</p>
      <div class="think-card">
        <div class="think-question">Out loud, describe the cuisine of your region: name a specialty and its main ingredients, and say what you love eating and what you cannot stand (for example, "I love trying fresh fish" or "I cannot stand eating very spicy food").</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-20"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 20</h4>
      <div class="survival-phrase"><span class="sp-num">1</span><span class="sp-en">I love trying the local cuisine.</span><span class="sp-pt">Eu adoro experimentar a culin&#225;ria local.</span><button class="btn btn-listen" onclick="speakText('I love trying the local cuisine.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">2</span><span class="sp-en">I enjoy cooking with fresh ingredients.</span><span class="sp-pt">Eu gosto de cozinhar com ingredientes frescos.</span><button class="btn btn-listen" onclick="speakText('I enjoy cooking with fresh ingredients.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">3</span><span class="sp-en">I cannot stand eating very spicy food.</span><span class="sp-pt">N&#227;o suporto comer comida muito apimentada.</span><button class="btn btn-listen" onclick="speakText('I cannot stand eating very spicy food.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">4</span><span class="sp-en">Neither do I.</span><span class="sp-pt">Eu tamb&#233;m n&#227;o.</span><button class="btn btn-listen" onclick="speakText('Neither do I.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">5</span><span class="sp-en">What is the specialty of this region?</span><span class="sp-pt">Qual &#233; a especialidade desta regi&#227;o?</span><button class="btn btn-listen" onclick="speakText('What is the specialty of this region?',this)">&#9835;</button></div>
    </div>

  </div>
</div>
'''
open(os.path.join(HERE,'preclass.html'),'w',encoding='utf-8').write(PRECLASS)
print("preclass.html written")

COMP = '''<h4 style="font-family:'Cormorant Garamond',serif;font-size:1.1rem;color:var(--accent);margin-top:2rem;margin-bottom:.8rem">Aula 20 -- Food &amp; Culture</h4>
<p style="font-size:.82rem;color:var(--text-dim);margin-bottom:1.5rem">Tema da aula: Food &amp; Culture (explorar a culin&#225;ria local e dizer o que se gosta e n&#227;o se gosta de comer com verbos de gosto + -ing e rea&#231;&#245;es So do I / Neither do I). Refor&#231;o fora de aula -- marque como conclu&#237;do ao terminar.</p>

<div class="media-grid">
  <div class="media-card-wrapper" data-media="l20-series">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb"><svg viewBox="0 0 24 24"><rect x="2" y="7" width="20" height="15" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><polyline points="17 2 12 7 7 2" fill="none" stroke="currentColor" stroke-width="2"/></svg></div>
      <div class="media-info">
        <div class="media-type">Series / Documentary</div>
        <h5>"Street Food" or "Chef's Table" (Netflix)</h5>
        <p>Watch cooks describe their cuisine, ingredients, and recipes. Listen for how they say what they love cooking and eating, and notice the food vocabulary from today.</p>
        <p class="media-tip">Dica: assista com legenda em ingl&#234;s e anote tr&#234;s pratos e duas frases com love/enjoy + -ing.</p>
      </div>
    </div>
  </div>

  <div class="media-card-wrapper" data-media="l20-youtube">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb"><svg viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3" fill="none" stroke="currentColor" stroke-width="2"/></svg></div>
      <div class="media-info">
        <div class="media-type">YouTube</div>
        <h5>BBC Learning English -- "So do I / Neither do I" &amp; verbs + -ing</h5>
        <p>A short, clear lesson on agreeing with So do I and Neither do I, and on using the -ing form after verbs of liking -- exactly today's grammar, with natural examples.</p>
        <p class="media-tip">Dica: pause ap&#243;s cada exemplo e reaja em voz alta com So do I ou Neither do I.</p>
      </div>
    </div>
  </div>

  <div class="media-card-wrapper" data-media="l20-podcast">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb"><svg viewBox="0 0 24 24"><path d="M12 1a3 3 0 00-3 3v8a3 3 0 006 0V4a3 3 0 00-3-3z"/><path d="M19 10v2a7 7 0 01-14 0v-2" fill="none" stroke="currentColor" stroke-width="2"/></svg></div>
      <div class="media-info">
        <div class="media-type">Podcast</div>
        <h5>Coffee Break English -- "Talking about food and culture"</h5>
        <p>A friendly episode about local cuisine, trying new dishes, and describing flavors -- perfect listening for a doctor who loves trying local food on conference trips.</p>
        <p class="media-tip">Dica: ou&#231;a duas vezes e anote cinco palavras de food &amp; culture e duas frases com cannot stand ou enjoy.</p>
      </div>
    </div>
  </div>
</div>
'''
open(os.path.join(HERE,'complementary.html'),'w',encoding='utf-8').write(COMP)
print("complementary.html written")

# ---- config.json: copy aula19 config, swap lesson fields + listenings ----
cfg = json.load(open(os.path.join(HERE,'config.json'),encoding='utf-8'))
# add stamp 20 if missing
ids = [s['id'] for s in cfg['stamps']]
if 20 not in ids:
    cfg['stamps'].append({"id":20,"label":"Food &amp; Culture","img":"https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=200&q=80"})
cfg['lesson'] = {
    "n":20,"menu_num":"20",
    "menu_title":"Food &amp; Culture",
    "menu_desc":"Explore local cuisine and say what you like and dislike eating, agreeing with So do I / Neither do I -- 28 slides",
    "subtitle":"Aula 20 -- Food &amp; Culture -- exploring local cuisine, talking about likes and dislikes (love / enjoy + -ing), and reacting with So do I / Neither do I",
    "title_tag":"Professor View -- Rubens Tofolo | Aula 20 -- Food &amp; Culture",
    "phases":["A Taste of the City","Food &amp; Culture Words","The Code","At the Table","Practice","Your Turn","Wrap-up"],
    "listenings":[
        {"file":"a20_listening1_sofia.mp3","voice":"ellen","text":TEXTS["listen1"]},
        {"file":"a20_listening2_rubens.mp3","voice":"arthur","text":TEXTS["listen2"]},
    ],
    "extra_audio":[
        {"key":"[order-l20]","file":"a20_order_food.mp3","voice":"arthur","text":TEXTS["order"]},
    ],
}
json.dump(cfg, open(os.path.join(HERE,'config.json'),'w',encoding='utf-8'), ensure_ascii=False, indent=2)
print("config.json written; stamps:", len(cfg['stamps']))
