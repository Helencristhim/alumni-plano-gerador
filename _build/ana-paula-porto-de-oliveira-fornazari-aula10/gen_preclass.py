#!/usr/bin/env python3
# Generates preclass.html for Ana Paula aula 10 (Plans & Intentions).
# Future plans vocab + grammar: going to (intentions) and present continuous (arrangements).
# Match-grid options are shuffled (REGRA 24: option order != word order).
import random, html

random.seed(110)

# word -> (definition, example)
VOCAB = [
    ("Goal",                "something you want to achieve in the future",   "My main goal is to speak English with confidence."),
    ("To intend",           "to plan or mean to do something",               "I intend to work as a doctor abroad."),
    ("To look forward to",  "to feel excited about a future event",          "I am looking forward to my trip in the spring."),
    ("Upcoming",            "happening soon, in the near future",            "I am a little nervous about my upcoming exam."),
    ("To arrange",          "to plan and organize something in advance",     "I arranged a meeting with my advisor."),
    ("Appointment",         "a fixed time to meet someone or do something",  "I have an appointment at the clinic on Monday."),
    ("To postpone",         "to move an event to a later time",              "We had to postpone the trip until June."),
    ("Deadline",            "the latest time to finish something",           "The deadline for the exam is in May."),
    ("To sign up",          "to add your name to join a course or event",    "I am going to sign up for a design course."),
    ("To figure out",       "to find a solution or make a decision",         "I need to figure out my next steps."),
    ("Ahead",               "in the future, or coming soon in time",         "There is a busy year ahead of me."),
    ("To make up my mind",  "to make a final decision",                      "I finally made up my mind to move next year."),
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

HTML = f'''<div class="lesson-card" id="ex-lesson-10">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1506784983877-45594efa4cbe?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 10 -- Pre-class</div>
      <h3>Plans &amp; Intentions</h3>
      <div class="lesson-desc">Talk about the future. Key words: goal, intend, look forward to, upcoming, arrange, appointment, postpone, deadline, sign up, figure out, ahead, make up your mind. Grammar: going to for intentions, present continuous for fixed arrangements.</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="10" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="10">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Twelve words to talk about your plans and the future. Listen to each one and read the example. Tap Listen to hear it.</p>
      <div class="vocab-cards">
        {vocab_cards}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each word with the correct definition.</p>
      <div class="match-grid" id="match-l10">
        {match_rows}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text and answer the questions.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>This year I <strong>made up my mind</strong> to be more organized. My main <strong>goal</strong> is to improve my English, so next month I <strong>am going to sign up</strong> for a course. I already <strong>arranged</strong> a study schedule: I <strong>am meeting</strong> my group every Tuesday evening. I also have an <strong>appointment</strong> with an advisor to <strong>figure out</strong> the next steps. The exam has a strict <strong>deadline</strong>, but I am really <strong>looking forward to</strong> the year <strong>ahead</strong>.</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. Which sentence is a plan or intention (going to)?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "Next month I am going to sign up for a course."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Yesterday I am going to a course."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I go to sign up a course."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. Which sentence is a fixed arrangement (present continuous)?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "I am meeting my group every Tuesday evening."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "I meet my group last week."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I will maybe meet my group."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. Which sentence is correct?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "I am going to study medicine."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "I going to study medicine."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I am go to study medicine."</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Two Ways to Talk About the Future</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Use "going to" for intentions and plans, and the present continuous for fixed arrangements.</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Use it for</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Going to (+)</td><td style="padding:.6rem">plans and intentions</td><td style="padding:.6rem">I <strong>am going to</strong> sign up for a course.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Going to (-)</td><td style="padding:.6rem">a plan you will not do</td><td style="padding:.6rem">I <strong>am not going to</strong> postpone the exam.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Going to (?)</td><td style="padding:.6rem">asking about plans</td><td style="padding:.6rem">What <strong>are</strong> you <strong>going to</strong> do next year?</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">Present continuous</td><td style="padding:.6rem">fixed arrangements with a time or place</td><td style="padding:.6rem">I <strong>am meeting</strong> my advisor on Friday.</td></tr>
        </tbody>
      </table></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the correct word. Tap Listen to hear the whole sentence.</p>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"Next month I am going to <input class="blank-input" data-answer="sign up" data-hint="Hint: to join a course or event" data-phrase="Next month I am going to sign up for a new course." placeholder="___"> for a new course."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"My main <input class="blank-input" data-answer="goal" data-hint="Hint: something you want to achieve" data-phrase="My main goal this year is to pass the exam." placeholder="___"> this year is to pass the exam."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"I have an important <input class="blank-input" data-answer="appointment" data-hint="Hint: a fixed time to meet someone" data-phrase="I have an important appointment with my advisor on Monday." placeholder="___"> with my advisor on Monday."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"The course has a strict <input class="blank-input" data-answer="deadline" data-hint="Hint: the last time to finish" data-phrase="The course has a strict deadline for the final exam." placeholder="___"> for the final exam."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"On Friday I am <input class="blank-input" data-answer="meeting" data-hint="Hint: present continuous for a fixed arrangement" data-phrase="On Friday I am meeting my study group at six." placeholder="___"> my study group at six."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"I had to <input class="blank-input" data-answer="postpone" data-hint="Hint: to move to a later time" data-phrase="I had to postpone my trip until next month." placeholder="___"> my trip until next month."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Story in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen first, then put the sentences of the story in the correct order.</p>
      <button class="btn btn-listen" onclick="speakText('[order-l10]', this)" style="margin-bottom:1rem;display:inline-flex;align-items:center;gap:.4rem;padding:.55rem 1.2rem;background:var(--accent);color:#fff;border:none;border-radius:8px;font-size:.85rem;font-weight:600;cursor:pointer"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/></svg> Listen</button>
      <div class="order-container" id="order-l10">
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l10')"><span class="order-num">?</span><span class="order-text">Then I signed up for an advanced course with a strict deadline.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l10')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l10')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l10')"><span class="order-num">?</span><span class="order-text">This year I finally made up my mind to plan the future.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l10')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l10')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l10')"><span class="order-num">?</span><span class="order-text">Next month I have an important appointment to figure out the next steps.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l10')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l10')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l10')"><span class="order-num">?</span><span class="order-text">First, I wrote down my main goal for English.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l10')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l10')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l10')"><span class="order-num">?</span><span class="order-text">I arranged a study schedule and I am meeting my group every Tuesday.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l10')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l10')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l10')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it.</p>
      <div class="speech-card" data-phrase="This year I am going to be more organized about my plans.">
        <div class="speech-phrase">This year I am going to be more organized about my plans.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="Next month I am signing up for an advanced course.">
        <div class="speech-phrase">Next month I am signing up for an advanced course.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="On Friday I am meeting my advisor at three.">
        <div class="speech-phrase">On Friday I am meeting my advisor at three.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="I am really looking forward to the year ahead.">
        <div class="speech-phrase">I am really looking forward to the year ahead.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each real situation.</p>
      <div class="quiz-item"><div class="quiz-question">A friend asks: "What are your plans for next year?" You answer:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "Next year I am going to change jobs."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Next year I changed jobs yesterday."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Next year I am change jobs."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You want to talk about a fixed meeting on Friday. Which is correct?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "On Friday I am meeting my advisor at three."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "On Friday I meet my advisor last week."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "On Friday I meeting my advisor."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You describe your main goal. Which is correct?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "My goal is to pass the exam."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "My goal is passed the exam."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "My goal to passing the exam."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You need to move an event to a later time. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "I have to postpone the trip."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "I have to deadline the trip."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I have to upcoming the trip."</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. There is no right or wrong answer.</p>
      <div class="think-card">
        <div class="think-question">Look at the year ahead. What are your main goals? What are you going to do to reach them? What fixed plans do you already have this month (with a day or a time)? Is there anything you had to postpone? Mix going to for your intentions and the present continuous for your arrangements. Take your time.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-10"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 10</h4>
      <div class="survival-phrase"><span class="sp-num">1</span><span class="sp-en">This year I am going to be more organized about my plans.</span><button class="btn btn-listen" onclick="speakText('This year I am going to be more organized about my plans.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">2</span><span class="sp-en">My main goal is to speak English with confidence.</span><button class="btn btn-listen" onclick="speakText('My main goal is to speak English with confidence.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">3</span><span class="sp-en">Next month I am signing up for a new course.</span><button class="btn btn-listen" onclick="speakText('Next month I am signing up for a new course.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">4</span><span class="sp-en">I am really looking forward to the year ahead.</span><button class="btn btn-listen" onclick="speakText('I am really looking forward to the year ahead.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">5</span><span class="sp-en">I had to postpone my move, but it is the right choice.</span><button class="btn btn-listen" onclick="speakText('I had to postpone my move, but it is the right choice.',this)">&#9835;</button></div>
    </div>

  </div>
</div>
'''

open("_build/ana-paula-porto-de-oliveira-fornazari-aula10/preclass.html", "w").write(HTML)
print("preclass.html written")
print("rows:", len(rows), "vocab:", len(vc))
