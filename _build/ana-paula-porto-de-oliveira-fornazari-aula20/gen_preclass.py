#!/usr/bin/env python3
# Generates preclass.html for Ana Paula aula 20 (Fluency Under Pressure).
# Fluency vocab + functional focus: sustained fluency and spontaneous production
# (integration milestone). Match-grid options shuffled (REGRA 24).
# NOTE: strings inside speakText('...') stay apostrophe-free (REGRA 7.1 convention).
import random, html

random.seed(120)

# word -> (definition, example)
VOCAB = [
    ("Fluency",       "the ability to speak smoothly and easily",                     "Your fluency has improved so much this year."),
    ("Confident",     "sure of yourself and not nervous",                             "I feel confident speaking English now."),
    ("Effortless",    "so easy that it needs no effort",                              "After practice, small talk feels effortless."),
    ("To stumble",    "to stop or make a mistake while speaking",                     "I still stumble on long words sometimes."),
    ("To elaborate",  "to explain something in more detail",                          "Could you elaborate on that idea?"),
    ("Pace",          "how fast or slow you speak",                                   "Try a calm, steady pace when you talk."),
    ("To express",    "to say what you think or feel",                                "I can express my opinion more clearly now."),
    ("To keep up",    "to follow a fast conversation without falling behind",         "I can keep up with native speakers now."),
    ("Tongue-tied",   "unable to speak because you are nervous",                      "I used to get tongue-tied in meetings."),
    ("To get across", "to make people understand your idea",                          "I got my point across without any trouble."),
    ("Breakthrough",  "a sudden, important improvement",                              "Speaking for a whole minute was a real breakthrough."),
    ("To sustain",    "to keep something going for a long time",                      "I can sustain a conversation for several minutes."),
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

HTML = f'''<div class="lesson-card" id="ex-lesson-20">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 20 -- Pre-class</div>
      <h3>Fluency Under Pressure</h3>
      <div class="lesson-desc">The milestone lesson: keep a real conversation going without freezing. Key words: fluency, confident, effortless, stumble, elaborate, pace, express, keep up, tongue-tied, get across, breakthrough, sustain. Focus: sustained fluency and spontaneous production -- paraphrase a missing word, buy a second, and keep the conversation flowing.</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="20" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="20">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Twelve words about speaking freely and keeping a conversation alive. Listen to each one and read the example. Tap Listen to hear it.</p>
      <div class="vocab-cards">
        {vocab_cards}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each fluency word with the correct definition.</p>
      <div class="match-grid" id="match-l20">
        {match_rows}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text and answer the questions.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>A year ago I always <strong>stumbled</strong> on hard words and felt <strong>tongue-tied</strong>. I translated every sentence in my head, so I could never <strong>keep up</strong> with a fast conversation. Then I stopped waiting for the perfect sentence. When I forgot a word, I <strong>expressed</strong> the idea in other words and kept going. I learned to speak at a calm <strong>pace</strong> and to <strong>sustain</strong> a chat for several minutes. Last week I got my point <strong>across</strong> for ten whole minutes -- that was a real <strong>breakthrough</strong>, and it felt almost <strong>effortless</strong>.</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. To "keep up" with a conversation means to...</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> follow it without falling behind.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> end it quickly.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> translate every word.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. When Ana Paula forgets a word, the best thing to do is...</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> describe the idea in other words and keep going.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> stop and stay silent.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> start the sentence again in Portuguese.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. For Ana Paula, a "breakthrough" was...</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> speaking freely for ten minutes without translating.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> learning one new grammar rule.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> making zero mistakes.</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- The Fluency Toolkit</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">Spontaneous production means speaking without a script. When something is missing, you do not stop -- you use one of four simple moves and keep the conversation flowing.</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Move</th><th style="padding:.7rem;text-align:left">Phrase</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Paraphrase a missing word</td><td style="padding:.6rem">What I mean is... / It is the thing you use to...</td><td style="padding:.6rem">"I forgot the word -- <strong>it is the thing you use to</strong> cook."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Buy a second</td><td style="padding:.6rem">Give me a second. / Let me think.</td><td style="padding:.6rem">"That is a good question -- <strong>give me a second</strong>."</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Pass the turn back</td><td style="padding:.6rem">What about you? / Tell me more.</td><td style="padding:.6rem">"It was great. <strong>What about you?</strong>"</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">Add detail (elaborate)</td><td style="padding:.6rem">For example... / because...</td><td style="padding:.6rem">"I love it, <strong>for example</strong>, when it saves me time."</td></tr>
        </tbody>
      </table></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the correct word. Tap Listen to hear the whole sentence.</p>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"I can now <input class="blank-input" data-answer="sustain" data-hint="Hint: to keep something going for a long time" data-phrase="I can now sustain a conversation for several minutes." placeholder="___"> a conversation for several minutes."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"When I forget a word, I <input class="blank-input" data-answer="express" data-hint="Hint: to say what you think or feel" data-phrase="When I forget a word, I express the idea in other words." placeholder="___"> the idea in other words."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"I used to feel <input class="blank-input" data-answer="tongue-tied" data-alt="tongue tied" data-hint="Hint: unable to speak because you are nervous" data-phrase="I used to feel tongue-tied in every meeting." placeholder="___"> in every meeting."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"Speaking for ten minutes was a real <input class="blank-input" data-answer="breakthrough" data-hint="Hint: a sudden, important improvement" data-phrase="Speaking for ten minutes was a real breakthrough for me." placeholder="___"> for me."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"Try to speak at a calm, steady <input class="blank-input" data-answer="pace" data-hint="Hint: how fast or slow you speak" data-phrase="Try to speak at a calm, steady pace." placeholder="___">."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"I got my point <input class="blank-input" data-answer="across" data-hint="Hint: to get an idea ___ -- make people understand it" data-phrase="I got my point across without any trouble." placeholder="___"> without any trouble."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Story in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen first, then put the sentences of the story in the correct order.</p>
      <button class="btn btn-listen" onclick="speakText('[order-l20]', this)" style="margin-bottom:1rem;display:inline-flex;align-items:center;gap:.4rem;padding:.55rem 1.2rem;background:var(--accent);color:#fff;border:none;border-radius:8px;font-size:.85rem;font-weight:600;cursor:pointer"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/></svg> Listen</button>
      <div class="order-container" id="order-l20">
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l20')"><span class="order-num">?</span><span class="order-text">When I forgot a word, I described it and kept going.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l20')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l20')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l20')"><span class="order-num">?</span><span class="order-text">A year ago, I translated every sentence in my head.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l20')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l20')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l20')"><span class="order-num">?</span><span class="order-text">Last week I spoke for ten minutes without translating -- that was my breakthrough.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l20')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l20')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l20')"><span class="order-num">?</span><span class="order-text">I stumbled on hard words and often felt tongue-tied.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l20')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l20')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l20')"><span class="order-num">?</span><span class="order-text">Then I stopped waiting for the perfect sentence.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l20')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l20')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l20')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each phrase, then record yourself saying it.</p>
      <div class="speech-card" data-phrase="I can keep the conversation going, even when I forget a word.">
        <div class="speech-phrase">I can keep the conversation going, even when I forget a word.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="What I mean is, I describe it in other words.">
        <div class="speech-phrase">What I mean is, I describe it in other words.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="Give me a second to think, and then I will answer.">
        <div class="speech-phrase">Give me a second to think, and then I will answer.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="I made mistakes, but I got my point across.">
        <div class="speech-phrase">I made mistakes, but I got my point across.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the most natural thing to say in each real situation.</p>
      <div class="quiz-item"><div class="quiz-question">You forget the English word for something. What do you say?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "Sorry, I forgot the word -- it is the thing you use to cook."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "I stop now, goodbye."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Word no have me."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">A friend asks about your weekend. You want to keep the conversation going. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "It was great -- I relaxed a lot. What about you?"</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Good."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "So do I."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">Someone asks a hard question and you need a moment. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "That is a good question -- give me a second."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "I think very fast now."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Repeat, please, again."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You want to add more detail to your idea. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "For example, last week it saved me a lot of time."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "That is all, the end."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Neither do I."</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. There is no right or wrong answer.</p>
      <div class="think-card">
        <div class="think-question">This is your final lesson -- look back on your English journey. How do you feel about speaking now, compared with a year ago? Talk for one or two minutes without stopping. If you forget a word, do not freeze: describe it, buy a second, and keep going. Try to use words from this lesson: fluency, confident, effortless, to keep up, breakthrough, to get across. Speak freely and enjoy it -- you have earned this.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-20"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 20</h4>
      <div class="survival-phrase"><span class="sp-num">1</span><span class="sp-en">What I mean is...</span><button class="btn btn-listen" onclick="speakText('What I mean is...',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">2</span><span class="sp-en">Let me think for a second.</span><button class="btn btn-listen" onclick="speakText('Let me think for a second.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">3</span><span class="sp-en">Can you tell me more about that?</span><button class="btn btn-listen" onclick="speakText('Can you tell me more about that?',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">4</span><span class="sp-en">So, what about you?</span><button class="btn btn-listen" onclick="speakText('So, what about you?',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">5</span><span class="sp-en">Anyway, as I was saying...</span><button class="btn btn-listen" onclick="speakText('Anyway, as I was saying...',this)">&#9835;</button></div>
    </div>

  </div>
</div>
'''

open("_build/ana-paula-porto-de-oliveira-fornazari-aula20/preclass.html", "w").write(HTML)
print("preclass.html written")
print("rows:", len(rows), "vocab:", len(vc))
