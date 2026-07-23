# -*- coding: utf-8 -*-
import random
random.seed(1709)

vocab = [
    ("Data", "facts and numbers collected for information or study", "The doctor studied the data from hundreds of patients."),
    ("Average", "the typical amount, found by adding numbers and dividing", "The average age of the group was thirty-five."),
    ("Percentage", "an amount expressed as a part of one hundred", "A large percentage of people said they felt better."),
    ("To increase", "to become larger in number or amount", "The number of visitors increased last year."),
    ("To decrease", "to become smaller in number or amount", "Prices decreased a little after the holidays."),
    ("Rate", "how often or how fast something happens, as a number", "The success rate of the treatment was very high."),
    ("Survey", "a set of questions asked to many people to collect answers", "The survey showed that most people exercise weekly."),
    ("Result", "the information you get at the end of a study or test", "The results of the study surprised everyone."),
    ("Figure", "a number, especially in official information or statistics", "The latest figures show a small rise in cases."),
    ("Trend", "a general direction in which something is changing over time", "There is a growing trend toward remote work."),
    ("To estimate", "to guess a number or amount using the information you have", "Experts estimate that thousands of people will attend."),
    ("Roughly", "approximately; not exactly", "The trip takes roughly two hours."),
]

match_defs = {
    "Data": "facts and numbers collected for study",
    "Average": "the typical amount of a set of numbers",
    "Percentage": "an amount out of one hundred",
    "To increase": "to become larger in amount",
    "To decrease": "to become smaller in amount",
    "Rate": "how often or how fast something happens",
    "Survey": "questions asked to many people",
    "Result": "the information you get at the end",
    "Figure": "a number in official information",
    "Trend": "a general direction of change over time",
    "To estimate": "to guess a number from information",
    "Roughly": "approximately; not exactly",
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

TEMPLATE = f'''<div class="lesson-card" id="ex-lesson-17">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 17 -- Pre-class</div>
      <h3>Numbers That Speak</h3>
      <div class="lesson-desc">Talking about data and research findings in everyday conversation. Key words: data, average, percentage, to increase, to decrease, rate, survey, result, figure, trend, to estimate, roughly. Function: how to read numbers aloud, describe trends, and share results clearly.</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="17" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="17">0%</span></div>
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
      <div class="match-grid" id="match-l17">
{match_rows}
      </div>
      <button class="verify-all-btn" onclick="verifyAllMatches('match-l17')">Check Answers</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text and answer the questions.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>Last week, Ana Paula read a health <strong>survey</strong> with some surprising <strong>results</strong>. The <strong>data</strong> showed that the <strong>average</strong> adult sleeps only six and a half hours a night. According to the <strong>figures</strong>, the <strong>percentage</strong> of tired people has <strong>increased</strong> over the last ten years. One in four adults said they rarely feel rested. On the other hand, the number of people who exercise has <strong>decreased</strong> a little, but a new <strong>trend</strong> is starting: short daily walks. The <strong>rate</strong> of people walking to work went up by <strong>roughly</strong> five percent. From her own patients, Ana Paula could <strong>estimate</strong> that these numbers were true. "The results are clear," she thought. "Small changes really matter."</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. What does the data show about how much the average adult sleeps?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Only about six and a half hours a night.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Exactly ten hours a night.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> The survey did not mention sleep.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. What happened to the percentage of tired people?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> It decreased a lot.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> It increased over the last ten years.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> It stayed exactly the same.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. What new trend is starting, according to the text?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> People are sleeping much more.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> More people are taking short daily walks.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Fewer people answer surveys.</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- The Language of Numbers</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">There is no new tense here. Instead, you learn how to read numbers aloud, describe how they change, and stay approximate. Keep these phrases ready and natural.</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Function</th><th style="padding:.7rem;text-align:left">Useful phrases</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Read numbers aloud</td><td style="padding:.6rem">45% = "forty-five percent" &middot; 1 in 3 = "one in three" &middot; 2.5 = "two point five"</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Say how many</td><td style="padding:.6rem">a large number of ... &middot; the majority of ... &middot; one in four ... &middot; on average, ...</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Describe change</td><td style="padding:.6rem">go up / increase / rise &middot; go down / decrease / fall &middot; sharply / slightly</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">Stay approximate</td><td style="padding:.6rem">roughly ... &middot; about / around ... &middot; nearly ... &middot; over / more than ...</td></tr>
        </tbody>
      </table></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence. Tap Listen to hear the whole sentence.</p>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"The data shows a clear <input class="blank-input" data-answer="trend" data-hint="Hint: a general direction of change over time" data-phrase="The data shows a clear trend toward reading on screens." placeholder="___"> toward reading on screens."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"A large <input class="blank-input" data-answer="percentage" data-hint="Hint: an amount out of one hundred" data-phrase="A large percentage of people agreed." placeholder="___"> of people agreed."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"On <input class="blank-input" data-answer="average" data-hint="Hint: the typical amount of a set of numbers" data-phrase="On average, adults sleep about seven hours." placeholder="___">, adults sleep about seven hours."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"The number of readers <input class="blank-input" data-answer="increased" data-hint="Hint: became larger -- past form of to increase" data-phrase="The number of readers increased last year." placeholder="___"> last year."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"We <input class="blank-input" data-answer="estimate" data-hint="Hint: to guess a number from information" data-phrase="We estimate that thousands of people will attend." placeholder="___"> that thousands of people will attend."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"The whole trip takes <input class="blank-input" data-answer="roughly" data-hint="Hint: approximately; not exactly" data-phrase="The whole trip takes roughly two hours." placeholder="___"> two hours."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Steps in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the steps of sharing data clearly in the correct order. Tap Listen to hear the full description.</p>
      <button class="btn btn-listen" onclick="speakText('[order-l17]', this)" style="margin-bottom:1rem;display:inline-flex;align-items:center;gap:.4rem;padding:.55rem 1.2rem;background:var(--accent);color:#fff;border:none;border-radius:8px;font-size:.85rem;font-weight:600;cursor:pointer"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/></svg> Listen</button>
      <div class="order-container" id="order-l17">
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l17')"><span class="order-num">?</span><span class="order-text">Describe the trend and say if the number went up or down.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l17')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l17')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l17')"><span class="order-num">?</span><span class="order-text">Say what the data is about and where the numbers come from.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l17')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l17')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l17')"><span class="order-num">?</span><span class="order-text">Estimate what might happen next or explain why the numbers matter.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l17')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l17')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l17')"><span class="order-num">?</span><span class="order-text">Give the main figure, like a percentage or an average.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l17')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l17')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l17')"><span class="order-num">?</span><span class="order-text">Add one more result that supports your point.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l17')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l17')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l17')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it.</p>
      <div class="speech-card" data-phrase="The data shows a clear trend.">
        <div class="speech-phrase">The data shows a clear trend.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="About sixty percent of people agreed.">
        <div class="speech-phrase">About sixty percent of people agreed.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="On average, adults sleep seven hours.">
        <div class="speech-phrase">On average, adults sleep seven hours.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="The number of readers increased slightly.">
        <div class="speech-phrase">The number of readers increased slightly.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="Roughly one in three people said yes.">
        <div class="speech-phrase">Roughly one in three people said yes.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each real situation.</p>
      <div class="quiz-item"><div class="quiz-question">You want to present the main number from a study. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "The number is a number thing."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "On average, patients waited about thirty minutes."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I average the patients tomorrow."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">A figure went from 40% to 55%. How do you describe it?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "The percentage increased from forty to fifty-five percent."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "The percentage decreased a lot."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "The percentage stayed the same."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You are not sure of the exact number, so you stay approximate. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "It is exactly 1,247 people, no more, no less."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Roughly one thousand people took the survey."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Some people, I do not know how."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You describe a general direction of change over time. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "There is a survey of the numbers."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "There is a growing trend toward working from home."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "The trend is a number I read."</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. There is no right or wrong answer.</p>
      <div class="think-card">
        <div class="think-question">Think of some numbers you know well (from your work, your city, or an article you read). Share one clear finding: say what the data is about, give the main figure, describe the trend, and estimate why it matters. Use "on average", "roughly", and "the percentage increased/decreased". Take your time.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-17"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 17</h4>
      <div class="survival-phrase"><span class="sp-num">1</span><span class="sp-en">The data shows a clear trend.</span><button class="btn btn-listen" onclick="speakText('The data shows a clear trend.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">2</span><span class="sp-en">On average, it is about seven hours.</span><button class="btn btn-listen" onclick="speakText('On average, it is about seven hours.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">3</span><span class="sp-en">The percentage increased since last year.</span><button class="btn btn-listen" onclick="speakText('The percentage increased since last year.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">4</span><span class="sp-en">Roughly one in three people agreed.</span><button class="btn btn-listen" onclick="speakText('Roughly one in three people agreed.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">5</span><span class="sp-en">I estimate the number will keep rising.</span><button class="btn btn-listen" onclick="speakText('I estimate the number will keep rising.',this)">&#9835;</button></div>
    </div>

  </div>
</div>
'''

open("_build/ana-paula-porto-de-oliveira-fornazari-aula17/preclass.html", "w", encoding="utf-8").write(TEMPLATE)
print("wrote preclass.html")
