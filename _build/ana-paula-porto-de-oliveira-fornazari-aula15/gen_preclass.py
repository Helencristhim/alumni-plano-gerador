# -*- coding: utf-8 -*-
import random
random.seed(1509)

vocab = [
    ("Point of view", "the way you think about a subject; your opinion", "From my point of view, both cities are great places to live."),
    ("To bring up", "to start talking about a topic", "She brought up an interesting idea during dinner."),
    ("To point out", "to mention a fact that others may not have noticed", "He pointed out that the plan had one small problem."),
    ("To admit", "to agree that something is true, even if you do not want to", "I have to admit that you were right about the movie."),
    ("Honestly", "used to show you are saying what you really think", "Honestly, I did not enjoy the book very much."),
    ("Actually", "used to add a fact or gently correct someone", "Actually, I think the second option is better."),
    ("To suppose", "to think that something is probably true", "I suppose you are right, but I still have doubts."),
    ("To insist", "to say very firmly that something is true or must happen", "My brother insists that his team is the best."),
    ("To convince", "to make someone believe or agree with you", "She convinced me to try the new restaurant."),
    ("To disagree", "to have a different opinion from someone", "I respect your idea, but I disagree with it."),
    ("To argue", "to give reasons for or against an idea", "Some people argue that working from home is better."),
    ("Biased", "showing an unfair preference for one side; not neutral", "The review felt biased, so I did not fully trust it."),
]

match_defs = {
    "Point of view": "the way you think about a subject",
    "To bring up": "to start talking about a topic",
    "To point out": "to mention a fact others may not notice",
    "To admit": "to agree something is true, even unwillingly",
    "Honestly": "used to show you really mean it",
    "Actually": "used to add or gently correct a fact",
    "To suppose": "to think something is probably true",
    "To insist": "to say very firmly something is true",
    "To convince": "to make someone believe or agree",
    "To disagree": "to have a different opinion",
    "To argue": "to give reasons for or against an idea",
    "Biased": "unfairly favoring one side; not neutral",
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

TEMPLATE = f'''<div class="lesson-card" id="ex-lesson-15">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 15 -- Pre-class</div>
      <h3>Making Your Voice Heard</h3>
      <div class="lesson-desc">Sharing your opinion in everyday conversation. Key words: point of view, to bring up, to point out, to admit, honestly, actually, to suppose, to insist, to convince, to disagree, to argue, biased. Function: how to give your opinion, agree, disagree politely, and soften your words (hedging).</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="15" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="15">0%</span></div>
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
      <div class="match-grid" id="match-l15">
{match_rows}
      </div>
      <button class="verify-all-btn" onclick="verifyAllMatches('match-l15')">Check Answers</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text and answer the questions.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>At dinner, Ana Paula's friend <strong>brought up</strong> a question: is it better to live in a big city or a small town? "<strong>In my opinion</strong>, a big city is more exciting," she said. <strong>Honestly</strong>, her friend did not agree. "I see your <strong>point of view</strong>, but I <strong>disagree</strong>," he replied. "<strong>Actually</strong>, I <strong>suppose</strong> a small town is calmer and safer." Ana Paula <strong>pointed out</strong> that cities have more jobs, and she had to <strong>admit</strong> that was important for her career. Her friend <strong>insisted</strong> that peace matters more, and he tried to <strong>convince</strong> her. Neither of them was <strong>biased</strong>; they simply saw it differently. "You could <strong>argue</strong> both sides," Ana Paula laughed. "Let's just agree to disagree."</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. Which phrase does Ana Paula use to give her opinion?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "In my opinion, a big city is more exciting."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "I have to go to the city."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "The city is at eight o'clock."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. How does her friend disagree politely?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "You are completely wrong."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I see your point of view, but I disagree."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Stop talking about the city."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. What does "she had to admit" show about Ana Paula?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> She refused to accept the other idea.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> She accepted a true point, even if she did not want to.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> She was not listening at all.</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- The Language of Opinions</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">There is no new tense here. Instead, you learn set phrases to give an opinion, agree, disagree politely, and soften your words. Keep them ready and natural.</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Function</th><th style="padding:.7rem;text-align:left">Useful phrases</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Give an opinion</td><td style="padding:.6rem">In my opinion, ... &middot; I think (that) ... &middot; If you ask me, ... &middot; From my point of view, ...</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Agree</td><td style="padding:.6rem">I totally agree. &middot; That is a good point. &middot; Exactly. &middot; You are right.</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Disagree politely</td><td style="padding:.6rem">I see your point, but ... &middot; I am not sure I agree. &middot; I am afraid I disagree. &middot; Actually, I think ...</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">Soften (hedging)</td><td style="padding:.6rem">I suppose ... &middot; It seems to me ... &middot; kind of / sort of &middot; to be honest ...</td></tr>
        </tbody>
      </table></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence. Tap Listen to hear the whole sentence.</p>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"In my <input class="blank-input" data-answer="opinion" data-hint="Hint: a phrase to introduce what you think" data-phrase="In my opinion, both plans are good." placeholder="___">, both plans are good."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"I see your point, <input class="blank-input" data-answer="but" data-hint="Hint: a small word to introduce a polite disagreement" data-phrase="I see your point, but I still disagree." placeholder="___"> I still disagree."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"I have to <input class="blank-input" data-answer="admit" data-hint="Hint: to accept a true point, even unwillingly" data-phrase="I have to admit that you were right." placeholder="___"> that you were right."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"That is a good <input class="blank-input" data-answer="point" data-hint="Hint: a common phrase to agree with an idea" data-phrase="That is a good point, I had not thought of that." placeholder="___">, I had not thought of that."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"Honestly, I am not <input class="blank-input" data-answer="sure" data-hint="Hint: used to disagree gently -- I am not ... I agree" data-phrase="Honestly, I am not sure I agree with that." placeholder="___"> I agree with that."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"Actually, I <input class="blank-input" data-answer="suppose" data-hint="Hint: to soften -- I ... you are right" data-phrase="Actually, I suppose you are right about that." placeholder="___"> you are right about that."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Steps in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the steps of sharing an opinion politely in the correct order. Tap Listen to hear the full description.</p>
      <button class="btn btn-listen" onclick="speakText('[order-l15]', this)" style="margin-bottom:1rem;display:inline-flex;align-items:center;gap:.4rem;padding:.55rem 1.2rem;background:var(--accent);color:#fff;border:none;border-radius:8px;font-size:.85rem;font-weight:600;cursor:pointer"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/></svg> Listen</button>
      <div class="order-container" id="order-l15">
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l15')"><span class="order-num">?</span><span class="order-text">Add a reason or point out a fact that supports your idea.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l15')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l15')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l15')"><span class="order-num">?</span><span class="order-text">Bring up the topic and say what you are talking about.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l15')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l15')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l15')"><span class="order-num">?</span><span class="order-text">Soften your words or find common ground to keep it friendly.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l15')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l15')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l15')"><span class="order-num">?</span><span class="order-text">Give your opinion clearly, with "In my opinion" or "I think".</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l15')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l15')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l15')"><span class="order-num">?</span><span class="order-text">Listen to the other person and agree or disagree politely.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l15')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l15')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l15')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it.</p>
      <div class="speech-card" data-phrase="In my opinion, a big city is more exciting.">
        <div class="speech-phrase">In my opinion, a big city is more exciting.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="I see your point, but I disagree.">
        <div class="speech-phrase">I see your point, but I disagree.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="Honestly, I am not sure I agree.">
        <div class="speech-phrase">Honestly, I am not sure I agree.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="That is a good point, I had not thought of that.">
        <div class="speech-phrase">That is a good point, I had not thought of that.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="Actually, I suppose you are right about that.">
        <div class="speech-phrase">Actually, I suppose you are right about that.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each real situation.</p>
      <div class="quiz-item"><div class="quiz-question">A friend asks what you think about a new restaurant. You give your opinion:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "The restaurant is a place."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "In my opinion, the food is great but a bit expensive."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I will restaurant tomorrow."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You do not agree, but you want to be polite. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "I see your point, but I am not sure I agree."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "That is a stupid idea."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "You are always wrong."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You strongly agree with your colleague's idea. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Maybe, I do not know."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Exactly, that is a really good point."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Let us talk about something else."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You want to soften your opinion so it sounds friendly. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "This is the only correct answer."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "It seems to me the first plan is a little better."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "You must do what I say."</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. There is no right or wrong answer.</p>
      <div class="think-card">
        <div class="think-question">Think of a topic you have an opinion about (a movie, your city, working from home, or social media). Give your point of view clearly, add one reason, and then say what someone who disagrees might argue. Finish by softening your words or finding common ground. Take your time.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-15"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 15</h4>
      <div class="survival-phrase"><span class="sp-num">1</span><span class="sp-en">In my opinion, this is the best option.</span><button class="btn btn-listen" onclick="speakText('In my opinion, this is the best option.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">2</span><span class="sp-en">That is a good point, I agree.</span><button class="btn btn-listen" onclick="speakText('That is a good point, I agree.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">3</span><span class="sp-en">I see your point, but I disagree.</span><button class="btn btn-listen" onclick="speakText('I see your point, but I disagree.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">4</span><span class="sp-en">Honestly, I am not sure about that.</span><button class="btn btn-listen" onclick="speakText('Honestly, I am not sure about that.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">5</span><span class="sp-en">Actually, I suppose you are right.</span><button class="btn btn-listen" onclick="speakText('Actually, I suppose you are right.',this)">&#9835;</button></div>
    </div>

  </div>
</div>
'''

open("_build/ana-paula-porto-de-oliveira-fornazari-aula15/preclass.html", "w", encoding="utf-8").write(TEMPLATE)
print("wrote preclass.html")
