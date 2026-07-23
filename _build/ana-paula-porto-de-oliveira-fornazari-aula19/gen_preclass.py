# -*- coding: utf-8 -*-
import random
random.seed(1909)

vocab = [
    ("Field", "the area of work or study a person is trained in", "Her field is medicine, and mine is engineering."),
    ("Qualification", "an official record that shows you finished training or passed an exam", "You need the right qualifications to work as a nurse."),
    ("To specialize", "to focus on one particular area of your work", "She decided to specialize in children's health."),
    ("Expertise", "special skill or deep knowledge in a particular area", "His expertise in surgery is respected by everyone."),
    ("To pursue", "to work toward a goal steadily over a long time", "He left his old job to pursue a career in research."),
    ("Transition", "the process of changing from one situation to another", "The transition to a new country was difficult but exciting."),
    ("Colleague", "a person you work with", "My colleagues at the clinic are very supportive."),
    ("License", "official permission to work in a profession", "A doctor needs a license to treat patients here."),
    ("Degree", "a qualification you receive from a university", "She has a degree in medicine from a Brazilian university."),
    ("Residency", "a period of supervised hospital training for a doctor after medical school", "During his residency, he worked long night shifts."),
    ("To adapt", "to change your behavior to fit a new situation", "It takes time to adapt to a new health system."),
    ("Demanding", "needing a lot of time, effort, or skill", "Medicine is a demanding but rewarding profession."),
]

match_defs = {
    "Field": "the area of work you are trained in",
    "Qualification": "proof that you finished training or passed an exam",
    "To specialize": "to focus on one particular area",
    "Expertise": "special skill or knowledge in an area",
    "To pursue": "to work toward a goal over time",
    "Transition": "a change from one situation to another",
    "Colleague": "a person you work with",
    "License": "official permission to work in a profession",
    "Degree": "a qualification from a university",
    "Residency": "supervised training in a hospital after medical school",
    "To adapt": "to change to fit a new situation",
    "Demanding": "needing a lot of time and effort",
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

TEMPLATE = f'''<div class="lesson-card" id="ex-lesson-19">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1584515933487-779824d29309?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 19 -- Pre-class</div>
      <h3>The Language of Professional Identity</h3>
      <div class="lesson-desc">Introducing yourself as a medical professional in transition. Key words: field, qualification, to specialize, expertise, to pursue, transition, colleague, license, degree, residency, to adapt, demanding. Function: how to describe your career background and current situation clearly and naturally.</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="19" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="19">0%</span></div>
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
      <div class="match-grid" id="match-l19">
{match_rows}
      </div>
      <button class="verify-all-btn" onclick="verifyAllMatches('match-l19')">Check Answers</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text and answer the questions.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>Ana Paula is a doctor going through a big <strong>transition</strong>. She earned her medical <strong>degree</strong> in Brazil and <strong>has worked</strong> as a physician for more than ten years. Her main <strong>field</strong> is family medicine, and she recently began to <strong>specialize</strong> in care for older patients. Now she lives in the United States, where she <strong>is pursuing</strong> a new <strong>license</strong> to practice. The process is <strong>demanding</strong>: she <strong>has passed</strong> two exams already, but she still studies every night. Her new <strong>colleagues</strong> value her <strong>expertise</strong>, and slowly she <strong>is learning</strong> to <strong>adapt</strong> to a different health system. "My <strong>qualifications</strong> travel with me," she says. "My experience never disappears."</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. Where did Ana Paula earn her medical degree?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> In Brazil.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> In the United States.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> The text does not say.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. What is she doing now in the United States?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> She has stopped working as a doctor forever.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> She is pursuing a new license to practice.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> She is studying to become an engineer.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. Why does she say "my qualifications travel with me"?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because she travels a lot for work.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Because her training and experience stay with her in any country.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because she lost her old documents.</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Background &amp; Now</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">To describe your professional identity, you mix three tenses. Use the <strong>present perfect</strong> to link your past to now (how long, what you have achieved), the <strong>past simple</strong> for finished moments, and the <strong>present simple</strong> for who you are today.</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Use</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Present perfect (past &rarr; now)</td><td style="padding:.6rem">"I <strong>have worked</strong> as a doctor for ten years." &middot; "I <strong>have just passed</strong> my exam."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Past simple (finished time)</td><td style="padding:.6rem">"I <strong>studied</strong> medicine in Brazil." &middot; "I <strong>graduated</strong> in 2012."</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Present simple (who I am now)</td><td style="padding:.6rem">"I <strong>am</strong> a family doctor." &middot; "I <strong>work</strong> at a clinic in Boston."</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">Present continuous (right now)</td><td style="padding:.6rem">"I <strong>am pursuing</strong> a new license." &middot; "I <strong>am learning</strong> the system."</td></tr>
        </tbody>
      </table></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence. Tap Listen to hear the whole sentence.</p>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"I <input class="blank-input" data-answer="have worked" data-hint="Hint: present perfect -- past to now, use 'have' + past participle" data-phrase="I have worked as a doctor for more than ten years." placeholder="___"> as a doctor for more than ten years."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"My main <input class="blank-input" data-answer="field" data-hint="Hint: the area of work you are trained in" data-phrase="My main field is family medicine." placeholder="___"> is family medicine."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"I am going through a career <input class="blank-input" data-answer="transition" data-hint="Hint: a change from one situation to another" data-phrase="I am going through a career transition." placeholder="___">."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"I <input class="blank-input" data-answer="studied" data-hint="Hint: past simple -- finished time" data-phrase="I studied medicine in Brazil." placeholder="___"> medicine in Brazil."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"I recently started to <input class="blank-input" data-answer="specialize" data-hint="Hint: to focus on one particular area" data-phrase="I recently started to specialize in care for older patients." placeholder="___"> in care for older patients."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"It takes time to <input class="blank-input" data-answer="adapt" data-hint="Hint: to change to fit a new situation" data-phrase="It takes time to adapt to a new health system." placeholder="___"> to a new health system."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Steps in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the steps of a clear professional introduction in the correct order. Tap Listen to hear the full description.</p>
      <button class="btn btn-listen" onclick="speakText('[order-l19]', this)" style="margin-bottom:1rem;display:inline-flex;align-items:center;gap:.4rem;padding:.55rem 1.2rem;background:var(--accent);color:#fff;border:none;border-radius:8px;font-size:.85rem;font-weight:600;cursor:pointer"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/></svg> Listen</button>
      <div class="order-container" id="order-l19">
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l19')"><span class="order-num">?</span><span class="order-text">Say how long you have worked and what you specialize in.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l19')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l19')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l19')"><span class="order-num">?</span><span class="order-text">Say your name and your field, so people know who you are.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l19')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l19')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l19')"><span class="order-num">?</span><span class="order-text">Say what you are working toward now and what comes next.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l19')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l19')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l19')"><span class="order-num">?</span><span class="order-text">Give your main qualification and where you studied.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l19')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l19')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l19')"><span class="order-num">?</span><span class="order-text">Explain your current situation or the transition you are going through.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l19')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l19')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l19')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it.</p>
      <div class="speech-card" data-phrase="I have worked as a doctor for ten years.">
        <div class="speech-phrase">I have worked as a doctor for ten years.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="My field is family medicine.">
        <div class="speech-phrase">My field is family medicine.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="I am going through a career transition.">
        <div class="speech-phrase">I am going through a career transition.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="I am pursuing a new license here.">
        <div class="speech-phrase">I am pursuing a new license here.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="My colleagues value my expertise.">
        <div class="speech-phrase">My colleagues value my expertise.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each real situation.</p>
      <div class="quiz-item"><div class="quiz-question">A new colleague asks what you do. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I am doctor thing in the medicine."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I am a doctor. My field is family medicine."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I doctor since many years ago."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You want to say how long you have been a doctor (from the past until now). You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "I have worked as a doctor for twelve years."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "I work as a doctor since twelve years."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I am working doctor twelve years ago."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You explain your current situation in a new country. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I pursued a license, and it finished yesterday forever."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Right now, I am pursuing a new license to practice."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I license the practice new."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You describe your training background. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I have studied medicine in Brazil in 2012."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I studied medicine in Brazil and did my residency there."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I study medicine yesterday in Brazil."</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. There is no right or wrong answer.</p>
      <div class="think-card">
        <div class="think-question">Introduce yourself as a professional. Say your name and your field, give your main qualification and where you studied, say how long you have worked and what you specialize in, and explain your current situation or transition. Use the present perfect for "how long", the past simple for finished moments, and the present simple for who you are now. Take your time.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-19"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 19</h4>
      <div class="survival-phrase"><span class="sp-num">1</span><span class="sp-en">I am a doctor, and my field is family medicine.</span><button class="btn btn-listen" onclick="speakText('I am a doctor, and my field is family medicine.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">2</span><span class="sp-en">I have worked as a physician for over ten years.</span><button class="btn btn-listen" onclick="speakText('I have worked as a physician for over ten years.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">3</span><span class="sp-en">I studied medicine in Brazil and did my residency there.</span><button class="btn btn-listen" onclick="speakText('I studied medicine in Brazil and did my residency there.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">4</span><span class="sp-en">Right now, I am pursuing my license here.</span><button class="btn btn-listen" onclick="speakText('Right now, I am pursuing my license here.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">5</span><span class="sp-en">A career transition takes time, but experience stays.</span><button class="btn btn-listen" onclick="speakText('A career transition takes time, but experience stays.',this)">&#9835;</button></div>
    </div>

  </div>
</div>
'''

open("_build/ana-paula-porto-de-oliveira-fornazari-aula19/preclass.html", "w", encoding="utf-8").write(TEMPLATE)
print("wrote preclass.html")
