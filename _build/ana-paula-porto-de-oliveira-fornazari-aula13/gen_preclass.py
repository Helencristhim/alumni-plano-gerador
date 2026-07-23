#!/usr/bin/env python3
# Generates preclass.html for Ana Paula aula 13 (Midpoint Review -- Lessons 1-12).
# Review vocab (reused on purpose, whitelisted) + grammar: review of tenses
# (present, past, present perfect, future, modals).
# Match-grid options are shuffled (REGRA 24: option order != word order).
import random, html

random.seed(113)

# word -> (definition, example)
VOCAB = [
    ("Journey",       "a long trip, or the process of learning and growing over time", "Learning English has been an amazing journey."),
    ("Routine",       "the things you usually do every day",                           "My morning routine starts at six."),
    ("Neighborhood",  "the area around your home where you live",                      "I live in a quiet neighborhood."),
    ("Hobby",         "an activity you do for fun in your free time",                  "Reading is my favorite hobby."),
    ("Schedule",      "a plan of when things happen during your day or week",          "My schedule is very busy this week."),
    ("Goal",          "something you want to achieve in the future",                   "My goal is to speak English fluently."),
    ("Milestone",     "an important moment or achievement in your life",               "Finishing school was a big milestone."),
    ("Opportunity",   "a chance to do something good",                                 "Every class is an opportunity to learn."),
    ("Abroad",        "in or to a foreign country",                                    "I want to work abroad one day."),
    ("Highlight",     "the best or most memorable part of an experience",              "The trip was the highlight of my year."),
    ("To overcome",   "to succeed in dealing with a problem or difficulty",            "I have overcome my fear of speaking."),
    ("Bucket list",   "a list of things you want to do in your life",                  "Seeing snow is on my bucket list."),
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

HTML = f'''<div class="lesson-card" id="ex-lesson-13">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1499750310107-5fef28a66643?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 13 -- Pre-class</div>
      <h3>Midpoint Review -- How Far Have You Come?</h3>
      <div class="lesson-desc">A midpoint review of your first twelve lessons. Key words: journey, routine, neighborhood, hobby, schedule, goal, milestone, opportunity, abroad, highlight, overcome, bucket list. Grammar: review of tenses -- present, past, present perfect and future.</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="13" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="13">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Twelve key words from your first twelve lessons. Listen to each one and read the example. Tap Listen to hear it.</p>
      <div class="vocab-cards">
        {vocab_cards}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each word with the correct definition.</p>
      <div class="match-grid" id="match-l13">
        {match_rows}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text and answer the questions. Notice how one story uses many tenses.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>When I <strong>started</strong> this course, I <strong>could</strong> only say a few words, and speaking felt scary. These days I <strong>have</strong> a busy <strong>routine</strong>, but I <strong>study</strong> almost every day. Learning English <strong>has been</strong> a long <strong>journey</strong>, and every class is an <strong>opportunity</strong> to grow. So far, I <strong>have reached</strong> a few <strong>milestones</strong> and I <strong>have overcome</strong> many mistakes. In the future, I <strong>am going to</strong> work <strong>abroad</strong>, and I <strong>will</strong> keep practicing until my <strong>goal</strong> comes true.</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. Which sentence talks about the START of her journey (past simple)?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "When I started, I could only say a few words."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "These days I study every day."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "One day I am going to work abroad."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. Which sentence talks about her journey SO FAR (present perfect)?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "I have overcome many mistakes."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "I started the course last year."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I study English every day."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. Which sentence talks about a future plan?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "I am going to work abroad."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "I have reached a few milestones."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "When I started, I felt nervous."</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- One Story, Many Tenses</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">When you review your progress, you mix tenses. Choose each one by the TIME you mean, not by the word.</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Tense</th><th style="padding:.7rem;text-align:left">Use it for</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Past simple</td><td style="padding:.6rem">the beginning, a finished time</td><td style="padding:.6rem">I <strong>started</strong>, I <strong>learned</strong>.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Present simple</td><td style="padding:.6rem">your life now, routines</td><td style="padding:.6rem">I <strong>study</strong> every day.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Present perfect</td><td style="padding:.6rem">the journey so far</td><td style="padding:.6rem">I <strong>have overcome</strong> many mistakes.</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Future (going to / will)</td><td style="padding:.6rem">plans and predictions</td><td style="padding:.6rem">I <strong>am going to</strong> work abroad.</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">Modals (can)</td><td style="padding:.6rem">ability</td><td style="padding:.6rem">I <strong>can</strong> hold a conversation.</td></tr>
        </tbody>
      </table></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the correct word. Tap Listen to hear the whole sentence.</p>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"Learning English has been a long <input class="blank-input" data-answer="journey" data-hint="Hint: a long trip or the process of growing over time" data-phrase="Learning English has been a long journey." placeholder="___">."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"I study every day as part of my <input class="blank-input" data-answer="routine" data-hint="Hint: the things you usually do every day" data-phrase="I study every day as part of my routine." placeholder="___">."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"Every class is an <input class="blank-input" data-answer="opportunity" data-hint="Hint: a chance to do something good" data-phrase="Every class is an opportunity to grow." placeholder="___"> to grow."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"Speaking for one minute was a big <input class="blank-input" data-answer="milestone" data-hint="Hint: an important moment or achievement" data-phrase="Speaking for one minute was a big milestone for me." placeholder="___"> for me."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"My <input class="blank-input" data-answer="goal" data-hint="Hint: something you want to achieve in the future" data-phrase="My goal is to work abroad as a doctor." placeholder="___"> is to work abroad as a doctor."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"Seeing snow is on my <input class="blank-input" data-answer="bucket list" data-hint="Hint: a list of things you want to do in your life" data-phrase="Seeing snow is on my bucket list." placeholder="___">."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Story in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen first, then put the sentences of the story in the correct order.</p>
      <button class="btn btn-listen" onclick="speakText('[order-l13]', this)" style="margin-bottom:1rem;display:inline-flex;align-items:center;gap:.4rem;padding:.55rem 1.2rem;background:var(--accent);color:#fff;border:none;border-radius:8px;font-size:.85rem;font-weight:600;cursor:pointer"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/></svg> Listen</button>
      <div class="order-container" id="order-l13">
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l13')"><span class="order-num">?</span><span class="order-text">Later, I talked about my goals and the milestones I want to reach.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l13')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l13')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l13')"><span class="order-num">?</span><span class="order-text">When I started this course, I could only say a few words.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l13')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l13')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l13')"><span class="order-num">?</span><span class="order-text">Now I am ready for the second half of my English journey.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l13')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l13')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l13')"><span class="order-num">?</span><span class="order-text">In the first lessons, I learned to describe my neighborhood and my daily routine.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l13')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l13')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l13')"><span class="order-num">?</span><span class="order-text">Along the way, I have overcome many of my mistakes.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l13')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l13')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l13')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it.</p>
      <div class="speech-card" data-phrase="Learning English has been a long journey.">
        <div class="speech-phrase">Learning English has been a long journey.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="So far, I have overcome many mistakes.">
        <div class="speech-phrase">So far, I have overcome many mistakes.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="One day, I am going to work abroad.">
        <div class="speech-phrase">One day, I am going to work abroad.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="Now I can hold a real conversation.">
        <div class="speech-phrase">Now I can hold a real conversation.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each real situation.</p>
      <div class="quiz-item"><div class="quiz-question">You talk about the very start of your course. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "When I started, I knew only a few words."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "When I start, I know only a few words."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "When I am starting, I am knowing a few words."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You describe your English now. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "These days, I study almost every day."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "These days, I studied almost every day."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "These days, I will study almost every day."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You talk about your journey so far. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "I have reached a few important milestones."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "I reach a few important milestones."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I am reach a few important milestones."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You talk about a plan for the second half. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "Next, I am going to work on my pronunciation."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Next, I go to work on my pronunciation yesterday."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Next, I have worked on my pronunciation tomorrow."</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. There is no right or wrong answer.</p>
      <div class="think-card">
        <div class="think-question">Tell the story of your English so far. Where did you start, and how did you feel? What is your routine now, and what have you overcome? What are your goals and your bucket list for the second half of the course? Mix the past, the present, the present perfect and the future, and take your time.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-13"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 13</h4>
      <div class="survival-phrase"><span class="sp-num">1</span><span class="sp-en">When I started, I could only say a few words.</span><button class="btn btn-listen" onclick="speakText('When I started, I could only say a few words.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">2</span><span class="sp-en">Learning English has been a long journey.</span><button class="btn btn-listen" onclick="speakText('Learning English has been a long journey.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">3</span><span class="sp-en">I have overcome many of my mistakes.</span><button class="btn btn-listen" onclick="speakText('I have overcome many of my mistakes.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">4</span><span class="sp-en">Now I can hold a real conversation.</span><button class="btn btn-listen" onclick="speakText('Now I can hold a real conversation.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">5</span><span class="sp-en">One day, I am going to work abroad.</span><button class="btn btn-listen" onclick="speakText('One day, I am going to work abroad.',this)">&#9835;</button></div>
    </div>

  </div>
</div>
'''

open("_build/ana-paula-porto-de-oliveira-fornazari-aula13/preclass.html", "w").write(HTML)
print("preclass.html written")
print("rows:", len(rows), "vocab:", len(vc))
