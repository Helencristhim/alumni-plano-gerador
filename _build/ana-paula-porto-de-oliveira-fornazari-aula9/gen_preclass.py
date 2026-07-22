# -*- coding: utf-8 -*-
import random
random.seed(909)

vocab = [
    ("Wellbeing", "the state of feeling healthy, comfortable, and happy", "Good sleep is important for your wellbeing."),
    ("Balanced", "having the right amount of different things", "A balanced diet has fruit, vegetables, and protein."),
    ("Exhausted", "extremely tired, with no energy left", "After a double shift, I feel completely exhausted."),
    ("Stress", "a feeling of worry from a difficult or busy situation", "Too much stress can affect your health."),
    ("Symptom", "a sign in your body that shows you may be ill", "A bad headache can be a symptom of stress."),
    ("Checkup", "a medical exam to see if you are healthy", "You should book a checkup once a year."),
    ("To recover", "to get well again after being ill or very tired", "Your body needs time to recover after exercise."),
    ("Fit", "healthy and strong, usually from exercise", "Walking every day keeps you fit."),
    ("Mindful", "calmly aware of the present moment and how you feel", "Take a mindful minute and breathe slowly."),
    ("To avoid", "to keep away from something that could harm you", "You should avoid too much caffeine at night."),
    ("To cut down on", "to reduce the amount of something", "I need to cut down on sugar and coffee."),
    ("To cope with", "to deal successfully with a problem or with stress", "Exercise helps me cope with a busy week."),
]

match_defs = {
    "Wellbeing": "the state of being healthy and happy",
    "Balanced": "with the right amount of each thing",
    "Exhausted": "extremely tired, with no energy",
    "Stress": "worry from a hard or busy time",
    "Symptom": "a body sign that you may be ill",
    "Checkup": "a medical exam of your health",
    "To recover": "to get well again after illness",
    "Fit": "healthy and strong from exercise",
    "Mindful": "calmly aware of the present moment",
    "To avoid": "to keep away from something bad",
    "To cut down on": "to reduce the amount of something",
    "To cope with": "to deal with a problem or stress",
}
all_defs = [match_defs[w] for w, _, _ in vocab]

# --- Vocab cards ---
vc = []
for w, d, ex in vocab:
    vc.append(
        f'        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header"><span class="vocab-card-word">{w}</span><span class="vocab-card-dot"> -- </span><span class="vocab-card-def">{d}</span></div><div class="vocab-card-example">"{ex}"</div></div><button class="audio-btn" onclick="speakText(\'{w}\',this)">Listen</button></div>'
    )
vocab_cards = "\n".join(vc)

# --- Matching (shuffled; correct option never at same row index) ---
rows = []
for i, (w, _, _) in enumerate(vocab):
    ans = match_defs[w]
    opts = all_defs[:]
    while True:
        random.shuffle(opts)
        if opts.index(ans) != i:
            break
    opt_html = '<option value="">Select...</option>' + "".join(
        f'<option value="{o}">{o}</option>' for o in opts
    )
    rows.append(
        f'        <div class="match-row" data-answer="{ans}"><span class="match-word" style="flex:0 0 150px">{w}</span><select style="flex:1;width:100%" onchange="checkMatch(this)">{opt_html}</select></div>'
    )
match_rows = "\n".join(rows)

TEMPLATE = f'''<div class="lesson-card" id="ex-lesson-9">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 09 -- Pre-class</div>
      <h3>Health &amp; Wellbeing</h3>
      <div class="lesson-desc">Talking about health, energy, and wellbeing. Key words: wellbeing, balanced, exhausted, stress, symptom, checkup, to recover, fit, mindful, to avoid, to cut down on, to cope with. Structure: modals of advice -- should and shouldn't for friendly suggestions, must and mustn't for strong necessity, always followed by the base verb.</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="9" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="9">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each word and read the example. Tap Listen to hear it.</p>
      <div class="vocab-cards">
{vocab_cards}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each word with the correct definition.</p>
      <div class="match-grid" id="match-l9">
{match_rows}
      </div>
      <button class="verify-all-btn" onclick="verifyAllMatches('match-l9')">Check Answers</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text and answer the questions.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>Ana Paula's friend Tom feels <strong>exhausted</strong> and full of <strong>stress</strong>. As a doctor, she gives him some advice. She says he <strong>should cut down on</strong> coffee and he <strong>should</strong> sleep more, because rest is important for his <strong>wellbeing</strong>. He <strong>should</strong> also eat a more <strong>balanced</strong> diet and take <strong>mindful</strong> breaks to <strong>cope with</strong> his busy days. But his headaches are a worrying <strong>symptom</strong>, so Ana Paula is firm: he <strong>must</strong> book a <strong>checkup</strong>, and he <strong>must not</strong> ignore the problem. If he follows this advice, he will soon feel <strong>fit</strong> and <strong>recover</strong> his energy.</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. Why do we say "he should sleep" and not "he should sleeps"?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> After should, we use the base verb, with no -s.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Sleep" has no third-person form.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Should" is only used with "I" and "you".</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. In "he must book a checkup", what does "must" show?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> A soft suggestion he can ignore.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> A strong necessity, almost a rule.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Something that happened in the past.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. Which sentence gives friendly advice correctly?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "You should to rest more."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "You should rest more."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "You should resting more."</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Should and Must</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">How to give advice (should) and show a strong necessity (must). After both, use the base verb.</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Modal</th><th style="padding:.7rem;text-align:left">Affirmative</th><th style="padding:.7rem;text-align:left">Negative &amp; Question</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">should<br>(advice)</td><td style="padding:.6rem">You <strong>should rest</strong> more.<br><em>a good idea</em></td><td style="padding:.6rem">You <strong>shouldn't skip</strong> meals.<br><strong>Should</strong> I see a doctor?</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">must<br>(strong necessity)</td><td style="padding:.6rem">You <strong>must sleep</strong> more.<br><em>almost a rule</em></td><td style="padding:.6rem">You <strong>mustn't ignore</strong> it.<br><em>= it is not allowed</em></td></tr>
          <tr><td style="padding:.6rem;font-weight:600">After the modal</td><td style="padding:.6rem" colspan="2">Always the <strong>base verb</strong>: no <strong>to</strong>, no <strong>-ing</strong>, no <strong>-s</strong>. "She <strong>should drink</strong> water" (not "drinks", not "to drink").</td></tr>
        </tbody>
      </table></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence. Tap Listen to hear the whole sentence.</p>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"You look pale. You <input class="blank-input" data-answer="should" data-hint="Hint: friendly advice, a good idea" data-phrase="You look pale. You should drink more water." placeholder="___"> drink more water."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"This medicine is important. You <input class="blank-input" data-answer="must" data-hint="Hint: strong necessity, almost a rule" data-phrase="This medicine is important. You must take it every day." placeholder="___"> take it every day."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"You are exhausted. You should <input class="blank-input" data-answer="rest" data-hint="Hint: base verb after should -- no to, no -ing" data-phrase="You are exhausted. You should rest this weekend." placeholder="___"> this weekend."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"To sleep well, you should <input class="blank-input" data-answer="avoid" data-hint="Hint: base verb -- to keep away from" data-phrase="To sleep well, you should avoid too much caffeine." placeholder="___"> too much caffeine."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"Your symptoms are serious. You must <input class="blank-input" data-answer="see" data-hint="Hint: base verb after must" data-phrase="Your symptoms are serious. You must see a doctor today." placeholder="___"> a doctor today."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"A busy week is hard, but you should <input class="blank-input" data-answer="take" data-hint="Hint: base verb -- short mindful pauses" data-phrase="A busy week is hard, but you should take mindful breaks." placeholder="___"> mindful breaks."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Advice in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the steps of giving good health advice in the correct order. Tap Listen to hear the full description.</p>
      <button class="btn btn-listen" onclick="speakText('[order-l9]', this)" style="margin-bottom:1rem;display:inline-flex;align-items:center;gap:.4rem;padding:.55rem 1.2rem;background:var(--accent);color:#fff;border:none;border-radius:8px;font-size:.85rem;font-weight:600;cursor:pointer"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/></svg> Listen</button>
      <div class="order-container" id="order-l9">
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l9')"><span class="order-num">?</span><span class="order-text">Say what they should avoid or cut down on.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l9')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l9')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l9')"><span class="order-num">?</span><span class="order-text">Give one final, kind piece of advice.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l9')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l9')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l9')"><span class="order-num">?</span><span class="order-text">Notice how your body feels and name the main symptom.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l9')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l9')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l9')"><span class="order-num">?</span><span class="order-text">Say what they must do if the problem is serious.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l9')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l9')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l9')"><span class="order-num">?</span><span class="order-text">Say what the person should do to feel better.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l9')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l9')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l9')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it.</p>
      <div class="speech-card" data-phrase="You should get more sleep every night.">
        <div class="speech-phrase">You should get more sleep every night.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="You mustn't ignore these symptoms.">
        <div class="speech-phrase">You mustn't ignore these symptoms.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="You should cut down on coffee and sugar.">
        <div class="speech-phrase">You should cut down on coffee and sugar.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="If the pain continues, you must see a doctor.">
        <div class="speech-phrase">If the pain continues, you must see a doctor.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="A balanced diet is good for your wellbeing.">
        <div class="speech-phrase">A balanced diet is good for your wellbeing.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each real situation.</p>
      <div class="quiz-item"><div class="quiz-question">A friend has a bad cold. You give friendly advice:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "You should to stay home."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "You should stay home and rest."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "You should staying home."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">Your colleague has a very high fever. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "You must see a doctor today."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "You must seeing a doctor today."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "You must to see a doctor today."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You want to advise a friend against a bad habit. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "You shouldn't skip your meals."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "You not should skip your meals."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "You shouldn't to skip your meals."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You give advice about someone else (third person). Which is correct?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "She should drinks more water."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "She should drink more water."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "She musts drink more water."</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. There is no right or wrong answer.</p>
      <div class="think-card">
        <div class="think-question">Someone in your life feels tired and stressed -- a patient, a friend, or a family member. Give them real health advice. Say what they should do to feel better, what they should avoid or cut down on, and what they must do if the problem is serious. Use should and must with the base verb. Take your time.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-9"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 9</h4>
      <div class="survival-phrase"><span class="sp-num">1</span><span class="sp-en">You should get more sleep to protect your wellbeing.</span><button class="btn btn-listen" onclick="speakText('You should get more sleep to protect your wellbeing.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">2</span><span class="sp-en">You should cut down on coffee and sugar.</span><button class="btn btn-listen" onclick="speakText('You should cut down on coffee and sugar.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">3</span><span class="sp-en">You must not ignore these symptoms.</span><button class="btn btn-listen" onclick="speakText('You must not ignore these symptoms.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">4</span><span class="sp-en">You should take short, mindful breaks during the day.</span><button class="btn btn-listen" onclick="speakText('You should take short, mindful breaks during the day.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">5</span><span class="sp-en">If the pain continues, you must see a doctor.</span><button class="btn btn-listen" onclick="speakText('If the pain continues, you must see a doctor.',this)">&#9835;</button></div>
    </div>

  </div>
</div>
'''

open("_build/ana-paula-porto-de-oliveira-fornazari-aula9/preclass.html", "w", encoding="utf-8").write(TEMPLATE)
print("wrote preclass.html")
