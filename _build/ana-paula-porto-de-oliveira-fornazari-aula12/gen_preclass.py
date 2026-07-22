#!/usr/bin/env python3
# Generates preclass.html for Ana Paula aula 12 (Experiences So Far).
# Life experiences vocab + grammar: present perfect with ever / never.
# Match-grid options are shuffled (REGRA 24: option order != word order).
import random, html

random.seed(112)

# word -> (definition, example)
VOCAB = [
    ("Abroad",          "in or to a foreign country",                       "I have always wanted to work abroad."),
    ("Opportunity",     "a chance to do something good",                    "Every trip is an opportunity to learn."),
    ("To explore",      "to travel around a place to discover it",          "We explored the old town on foot."),
    ("Highlight",       "the best or most memorable part of an experience", "The safari was the highlight of the trip."),
    ("To accomplish",   "to succeed in doing something difficult",          "I have accomplished one of my biggest dreams."),
    ("Lifetime",        "the whole period of a person's life",              "It was the trip of a lifetime."),
    ("To volunteer",    "to offer to help without being paid",              "She has volunteered at a hospital."),
    ("Thrilling",       "very exciting and a bit scary",                    "Riding a roller coaster is thrilling."),
    ("To attempt",      "to try to do something difficult",                 "I have never attempted a marathon."),
    ("Brave",           "ready to face danger or difficulty",               "It was brave of you to try surfing."),
    ("Rewarding",       "giving a feeling of satisfaction",                 "Helping others is very rewarding."),
    ("Bucket list",     "a list of things you want to do in your life",     "Seeing snow is on my bucket list."),
]

def esc(s):
    return html.escape(s, quote=True)

# ---- Stage 1.1 vocab cards ----
vc = []
for w, d, ex in VOCAB:
    vc.append(
        '<div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header">'
        f'<span class="vocab-card-word">{esc(w)}</span><span class="vocab-card-dot"> -- </span>'
        f'<span class="vocab-card-def">{esc(d)}</span></div>'
        f'<div class="vocab-card-example">"{esc(ex)}"</div></div>'
        f'<button class="audio-btn" onclick="speakText(\'{w}\',this)">Listen</button></div>'
    )
vocab_cards = "\n        ".join(vc)

# ---- Stage 1.2 matching (shuffled options per row) ----
defs = [d for _, d, _ in VOCAB]
rows = []
for i, (w, d, _) in enumerate(VOCAB):
    opts = defs[:]
    while True:
        random.shuffle(opts)
        if opts.index(d) != i:
            break
    opt_html = '<option value="">Select...</option>' + "".join(
        f'<option value="{esc(o)}">{esc(o)}</option>' for o in opts
    )
    rows.append(
        f'<div class="match-row" data-answer="{esc(d)}"><span class="match-word" style="flex:0 0 150px">{esc(w)}</span>'
        f'<select style="flex:1;width:100%" onchange="checkMatch(this)">{opt_html}</select></div>'
    )
match_rows = "\n        ".join(rows)

HTML = f'''<div class="lesson-card" id="ex-lesson-12">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 12 -- Pre-class</div>
      <h3>Experiences So Far</h3>
      <div class="lesson-desc">Talk about your life experiences. Key words: abroad, opportunity, explore, highlight, accomplish, lifetime, volunteer, thrilling, attempt, brave, rewarding, bucket list. Grammar: present perfect with ever and never for life experiences.</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="12" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="12">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Twelve words to talk about your life experiences. Listen to each one and read the example. Tap Listen to hear it.</p>
      <div class="vocab-cards">
        {vocab_cards}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each word with the correct definition.</p>
      <div class="match-grid" id="match-l12">
        {match_rows}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text and answer the questions.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>I <strong>have had</strong> an interesting life so far. I <strong>have traveled abroad</strong> several times, and I <strong>have explored</strong> many cities. Volunteering at a clinic was one of the most <strong>rewarding</strong> things I <strong>have ever done</strong>. I <strong>have attempted</strong> a few <strong>brave</strong> things, like diving, and each one was <strong>thrilling</strong>. But there are still things I <strong>have never done</strong>: I <strong>have never seen</strong> snow, so it is on my <strong>bucket list</strong>. One day I hope to <strong>accomplish</strong> that dream, the <strong>highlight</strong> of a <strong>lifetime</strong>.</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. Which sentence talks about a life experience (present perfect)?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "I have traveled abroad several times."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "I travel abroad yesterday."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I am travel abroad."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. Which question asks about experience with "ever"?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "Have you ever tried diving?"</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Do you tried diving yesterday?"</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Are you ever try diving?"</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. Which sentence is correct?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "I have never seen snow."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "I have never saw snow."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I never have see snow."</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Present Perfect with Ever &amp; Never</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Use have or has + the past participle for life experiences. Add "ever" in questions and "never" for no experience.</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Use it for</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Present perfect (+)</td><td style="padding:.6rem">a life experience</td><td style="padding:.6rem">I <strong>have traveled</strong> abroad.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">(-) with never</td><td style="padding:.6rem">no experience</td><td style="padding:.6rem">I <strong>have never seen</strong> snow.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">(?) with ever</td><td style="padding:.6rem">asking about experience</td><td style="padding:.6rem"><strong>Have</strong> you <strong>ever tried</strong> diving?</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">Short answers</td><td style="padding:.6rem">a quick reply</td><td style="padding:.6rem">Yes, I <strong>have</strong>. / No, I <strong>have not</strong>.</td></tr>
        </tbody>
      </table></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the correct word. Tap Listen to hear the whole sentence.</p>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"I have <input class="blank-input" data-answer="explored" data-hint="Hint: past participle of to travel around and discover a place" data-phrase="I have explored many beautiful cities." placeholder="___"> many beautiful cities."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"Volunteering is the most <input class="blank-input" data-answer="rewarding" data-hint="Hint: giving a feeling of satisfaction" data-phrase="Volunteering is the most rewarding thing I have ever done." placeholder="___"> thing I have ever done."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"I have never <input class="blank-input" data-answer="been" data-hint="Hint: past participle of to be" data-phrase="I have never been abroad." placeholder="___"> abroad."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"Seeing snow is on my <input class="blank-input" data-answer="bucket list" data-hint="Hint: a list of things you want to do in your life" data-phrase="Seeing snow is on my bucket list." placeholder="___">."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"Have you ever <input class="blank-input" data-answer="tried" data-hint="Hint: past participle of to try" data-phrase="Have you ever tried something thrilling?" placeholder="___"> something thrilling?"</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"One day I want to <input class="blank-input" data-answer="accomplish" data-hint="Hint: to succeed in doing something difficult" data-phrase="One day I want to accomplish my biggest dream." placeholder="___"> my biggest dream."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Story in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen first, then put the sentences of the story in the correct order.</p>
      <button class="btn btn-listen" onclick="speakText('[order-l12]', this)" style="margin-bottom:1rem;display:inline-flex;align-items:center;gap:.4rem;padding:.55rem 1.2rem;background:var(--accent);color:#fff;border:none;border-radius:8px;font-size:.85rem;font-weight:600;cursor:pointer"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/></svg> Listen</button>
      <div class="order-container" id="order-l12">
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l12')"><span class="order-num">?</span><span class="order-text">There, I explored an old city, and it became the highlight of my trip.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l12')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l12')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l12')"><span class="order-num">?</span><span class="order-text">I have always loved trying new things in my life.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l12')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l12')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l12')"><span class="order-num">?</span><span class="order-text">Now, seeing the northern lights is the only thing left on my bucket list.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l12')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l12')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l12')"><span class="order-num">?</span><span class="order-text">A few years ago, I finally traveled abroad for the first time.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l12')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l12')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l12')"><span class="order-num">?</span><span class="order-text">Later, I attempted something brave and went diving in the sea.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l12')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l12')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l12')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it.</p>
      <div class="speech-card" data-phrase="I have traveled abroad several times.">
        <div class="speech-phrase">I have traveled abroad several times.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="The highlight of my life was climbing a mountain.">
        <div class="speech-phrase">The highlight of my life was climbing a mountain.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="I have never seen snow, but it is on my bucket list.">
        <div class="speech-phrase">I have never seen snow, but it is on my bucket list.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="Have you ever done anything thrilling?">
        <div class="speech-phrase">Have you ever done anything thrilling?</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each real situation.</p>
      <div class="quiz-item"><div class="quiz-question">A friend asks: "Have you ever been abroad?" You answer:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "Yes, I have been to Portugal and Italy."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Yes, I go there tomorrow."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Yes, I am been there."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You want to talk about an experience you have never had. Which is correct?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "I have never gone skydiving."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "I have never went skydiving."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I never gone skydiving."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You describe the best part of a trip. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "The safari was the highlight of the trip."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "The safari was the deadline of the trip."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "The safari was the bucket of the trip."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You ask a friend about their life experience. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "Have you ever volunteered?"</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Did you ever volunteering?"</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Have you ever volunteer?"</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. There is no right or wrong answer.</p>
      <div class="think-card">
        <div class="think-question">Look back at your life so far. What are some of the most interesting things you have done? Where have you traveled, and what have you explored? Is there anything rewarding you have done to help others? Now think of two or three things you have never done but would love to try one day. Use the present perfect (I have..., I have never...) and take your time.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-12"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 12</h4>
      <div class="survival-phrase"><span class="sp-num">1</span><span class="sp-en">I have traveled abroad several times.</span><button class="btn btn-listen" onclick="speakText('I have traveled abroad several times.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">2</span><span class="sp-en">The most rewarding thing I have ever done was to volunteer.</span><button class="btn btn-listen" onclick="speakText('The most rewarding thing I have ever done was to volunteer.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">3</span><span class="sp-en">I have never seen snow, but it is on my bucket list.</span><button class="btn btn-listen" onclick="speakText('I have never seen snow, but it is on my bucket list.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">4</span><span class="sp-en">Have you ever done anything really thrilling?</span><button class="btn btn-listen" onclick="speakText('Have you ever done anything really thrilling?',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">5</span><span class="sp-en">It was the trip of a lifetime.</span><button class="btn btn-listen" onclick="speakText('It was the trip of a lifetime.',this)">&#9835;</button></div>
    </div>

  </div>
</div>
'''

open("_build/ana-paula-porto-de-oliveira-fornazari-aula12/preclass.html", "w").write(HTML)
print("preclass.html written")
print("rows:", len(rows), "vocab:", len(vc))
