#!/usr/bin/env python3
# Generates preclass.html for Ana Paula aula 14 (Phrasal Verbs in Real Life).
# Everyday phrasal verbs + grammar: phrasal verbs (separable and inseparable).
# Match-grid options are shuffled (REGRA 24: option order != word order).
import random, html

random.seed(114)

# word -> (definition, example)
VOCAB = [
    ("To wake up",     "to stop sleeping",                                  "I wake up at six o'clock every day."),
    ("To get up",      "to leave your bed after you wake up",               "I do not get up right away."),
    ("To run into",    "to meet someone by chance",                         "I ran into an old friend at the store."),
    ("To look after",  "to take care of someone or something",              "I look after my daughter in the evening."),
    ("To give up",     "to stop trying to do something",                    "I never give up when things get hard."),
    ("To turn down",   "to say no to an offer or invitation",               "I had to turn down the invitation."),
    ("To fill out",    "to complete a form with your information",          "I filled out three long forms."),
    ("To drop off",    "to take someone somewhere and leave them there",    "I drop off my daughter at school."),
    ("To pick up",     "to go and collect someone or something",            "I pick up my daughter after work."),
    ("To sort out",    "to solve a problem or put things in order",         "I need to sort out my schedule."),
    ("To put off",     "to move something to a later time",                 "Do not put off your rest."),
    ("To get along",   "to have a friendly relationship with someone",      "I get along well with my neighbors."),
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

HTML = f'''<div class="lesson-card" id="ex-lesson-14">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1484480974693-6ca0a78fb36b?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 14 -- Pre-class</div>
      <h3>Phrasal Verbs in Real Life</h3>
      <div class="lesson-desc">Everyday phrasal verbs for your daily routine and social life. Key verbs: wake up, get up, run into, look after, give up, turn down, fill out, drop off, pick up, sort out, put off, get along. Grammar: phrasal verbs, separable and inseparable.</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="14" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="14">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Twelve everyday phrasal verbs for your daily routine and social life. Listen to each one and read the example. Tap Listen to hear it.</p>
      <div class="vocab-cards">
        {vocab_cards}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each phrasal verb with the correct definition.</p>
      <div class="match-grid" id="match-l14">
        {match_rows}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text and answer the questions.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>Every weekday I <strong>wake up</strong> at six, but I do not <strong>get up</strong> right away. When I finally <strong>get up</strong>, I <strong>drop off</strong> my daughter at school. At the hospital I <strong>fill out</strong> forms and <strong>sort out</strong> small problems, and I never <strong>give up</strong>. On my way home I sometimes <strong>run into</strong> a neighbor, and we <strong>get along</strong> really well. In the evening I <strong>pick up</strong> my daughter and <strong>look after</strong> her. If I am tired, I <strong>turn down</strong> invitations, because I do not like to <strong>put off</strong> my rest.</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. Which sentence uses a phrasal verb correctly?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "I drop off my daughter at school."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "I drop my daughter school."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I dropping off my daughter."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. "I run into a neighbor" means...</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> I meet the neighbor by chance.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> I hit the neighbor with my car.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> I run away from the neighbor.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. Which sentence puts the pronoun in the right place?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "I pick her up after work."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "I pick up her after work."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I pick after work her up."</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Separable &amp; Inseparable Phrasal Verbs</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">A phrasal verb is a verb plus a small word (up, out, off, into) with a new meaning. Some are separable (an object can go in the middle), and some are inseparable (the words stay together). A pronoun always goes in the middle of a separable verb.</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Type</th><th style="padding:.7rem;text-align:left">Rule</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Separable</td><td style="padding:.6rem">object can go in the middle</td><td style="padding:.6rem">I <strong>filled out</strong> the form. / I <strong>filled</strong> the form <strong>out</strong>.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Separable + pronoun</td><td style="padding:.6rem">pronoun MUST go in the middle</td><td style="padding:.6rem">I <strong>picked</strong> her <strong>up</strong>. (not "picked up her")</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Inseparable</td><td style="padding:.6rem">the words stay together</td><td style="padding:.6rem">I <strong>ran into</strong> a friend. (not "ran a friend into")</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">Meaning</td><td style="padding:.6rem">learn it as one word</td><td style="padding:.6rem"><strong>look after</strong> = take care of</td></tr>
        </tbody>
      </table></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the correct verb. Tap Listen to hear the whole sentence.</p>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"I <input class="blank-input" data-answer="wake" data-hint="Hint: to stop sleeping (wake ___ )" data-phrase="I wake up early every day." placeholder="___"> up early every day."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"I <input class="blank-input" data-answer="drop" data-hint="Hint: to take someone somewhere and leave them ( ___ off )" data-phrase="I drop off my daughter at school." placeholder="___"> off my daughter at school."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"I had to <input class="blank-input" data-answer="fill" data-hint="Hint: to complete a form ( ___ out )" data-phrase="I had to fill out three forms." placeholder="___"> out three forms."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"I <input class="blank-input" data-answer="ran" data-hint="Hint: past of to meet by chance ( ___ into )" data-phrase="I ran into an old friend yesterday." placeholder="___"> into an old friend yesterday."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"I <input class="blank-input" data-answer="look" data-hint="Hint: to take care of someone ( ___ after )" data-phrase="I look after my daughter in the evening." placeholder="___"> after my daughter in the evening."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"I never <input class="blank-input" data-answer="give" data-hint="Hint: to stop trying ( ___ up )" data-phrase="I never give up when things get hard." placeholder="___"> up when things get hard."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Story in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen first, then put the sentences of the story in the correct order.</p>
      <button class="btn btn-listen" onclick="speakText('[order-l14]', this)" style="margin-bottom:1rem;display:inline-flex;align-items:center;gap:.4rem;padding:.55rem 1.2rem;background:var(--accent);color:#fff;border:none;border-radius:8px;font-size:.85rem;font-weight:600;cursor:pointer"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/></svg> Listen</button>
      <div class="order-container" id="order-l14">
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l14')"><span class="order-num">?</span><span class="order-text">At work, I fill out forms and sort out small problems.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l14')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l14')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l14')"><span class="order-num">?</span><span class="order-text">On a busy morning, I wake up before my alarm.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l14')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l14')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l14')"><span class="order-num">?</span><span class="order-text">In the evening, I pick up my daughter and look after her.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l14')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l14')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l14')"><span class="order-num">?</span><span class="order-text">I get up, make coffee, and drop off my daughter at school.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l14')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l14')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l14')"><span class="order-num">?</span><span class="order-text">On my way home, I run into a friend at the store.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l14')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l14')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l14')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it.</p>
      <div class="speech-card" data-phrase="I wake up early, but I do not get up right away.">
        <div class="speech-phrase">I wake up early, but I do not get up right away.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="I ran into an old friend at the pharmacy.">
        <div class="speech-phrase">I ran into an old friend at the pharmacy.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="I pick up my daughter and look after her.">
        <div class="speech-phrase">I pick up my daughter and look after her.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="I get along really well with my neighbors.">
        <div class="speech-phrase">I get along really well with my neighbors.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each real situation.</p>
      <div class="quiz-item"><div class="quiz-question">A friend asks what time your day starts. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "I get up at six every morning."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "I get on at six every morning."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I get six up morning."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You met an old colleague by chance today. You tell a friend:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "I ran into an old colleague today."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "I ran an old colleague into today."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I ran into today an old colleague."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You are too tired to accept an invitation. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "Thanks, but I have to turn down your invitation tonight."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Thanks, but I have to turn on your invitation tonight."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Thanks, but I have to fill out your invitation tonight."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You want to say you have a good relationship with your neighbors. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "I get along really well with my neighbors."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "I give up really well with my neighbors."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I put off really well with my neighbors."</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. There is no right or wrong answer.</p>
      <div class="think-card">
        <div class="think-question">Walk me through a normal day, from morning to night. What time do you wake up and get up? Who do you drop off or pick up? At work, what do you sort out or fill out? Do you ever run into people you know? In the evening, who do you look after, and do you sometimes turn down invitations? Use as many phrasal verbs as you can, and take your time.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-14"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 14</h4>
      <div class="survival-phrase"><span class="sp-num">1</span><span class="sp-en">I wake up early, but I do not get up right away.</span><button class="btn btn-listen" onclick="speakText('I wake up early, but I do not get up right away.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">2</span><span class="sp-en">I drop off my daughter and pick her up after work.</span><button class="btn btn-listen" onclick="speakText('I drop off my daughter and pick her up after work.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">3</span><span class="sp-en">I had to fill out a lot of forms this week.</span><button class="btn btn-listen" onclick="speakText('I had to fill out a lot of forms this week.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">4</span><span class="sp-en">I ran into an old friend and we get along well.</span><button class="btn btn-listen" onclick="speakText('I ran into an old friend and we get along well.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">5</span><span class="sp-en">I do not like to put off my rest.</span><button class="btn btn-listen" onclick="speakText('I do not like to put off my rest.',this)">&#9835;</button></div>
    </div>

  </div>
</div>
'''

open("_build/ana-paula-porto-de-oliveira-fornazari-aula14/preclass.html", "w").write(HTML)
print("preclass.html written")
print("rows:", len(rows), "vocab:", len(vc))
