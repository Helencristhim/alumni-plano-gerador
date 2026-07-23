#!/usr/bin/env python3
# Generates preclass.html for Ana Paula aula 18 (Navigating the Unexpected).
# Everyday clarification vocab + grammar: clarification and repair strategies
# (asking for repetition, buying time). Match-grid options shuffled (REGRA 24).
import random, html

random.seed(118)

# word -> (definition, example)
VOCAB = [
    ("To clarify",      "to make something clearer or easier to understand",           "Could you clarify what you mean?"),
    ("To rephrase",     "to say the same thing again using different words",            "Let me rephrase that more simply."),
    ("To catch",        "to hear and understand what someone says",                     "Sorry, I did not catch your name."),
    ("Confusing",       "hard to understand; not clear",                                "The directions were a little confusing."),
    ("To make sense",   "to be clear and easy to understand",                           "Now your explanation makes sense."),
    ("Vague",           "not clear or not exact",                                       "His answer was vague, so I asked again."),
    ("To hesitate",     "to pause before speaking because you are not sure",            "Do not hesitate to ask me to repeat."),
    ("Filler",          "a small word like well or um that gives you time to think",    "Well is a common filler in English."),
    ("To recap",        "to repeat the main points quickly",                            "Let me recap what we decided."),
    ("To bear with",    "to ask someone to be patient and wait",                        "Bear with me while I find the word."),
    ("To hold on",      "to wait for a short moment",                                   "Hold on a second, please."),
    ("Straightforward", "simple, clear and easy to understand",                         "Her instructions were straightforward."),
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

HTML = f'''<div class="lesson-card" id="ex-lesson-18">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1516387938699-a93567ec168e?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 18 -- Pre-class</div>
      <h3>Navigating the Unexpected</h3>
      <div class="lesson-desc">Everyday words for clarifying and the repair strategies that keep you in control when a conversation is confusing. Key words: clarify, rephrase, catch, confusing, make sense, vague, hesitate, filler, recap, bear with, hold on, straightforward. Grammar: clarification and repair strategies -- asking for repetition, buying time and checking you understood.</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="18" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="18">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Twelve everyday words for staying clear when a conversation is hard. Listen to each one and read the example. Tap Listen to hear it.</p>
      <div class="vocab-cards">
        {vocab_cards}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each clarifying word with the correct definition.</p>
      <div class="match-grid" id="match-l18">
        {match_rows}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text and answer the questions.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>On the phone, the clinic spoke fast and I could not <strong>catch</strong> the time. Instead of pretending, I asked, "<strong>Could you say that again?</strong>" When a word was <strong>confusing</strong>, I said, "<strong>What do you mean by that?</strong>" I needed a moment, so I used a <strong>filler</strong> -- "Well, let me think for a second" -- to <strong>hold on</strong> and think. At the end, just to <strong>recap</strong>, I repeated the address back to check I understood. None of this is rude; it keeps the conversation <strong>straightforward</strong>.</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. "Could you say that again?" is a polite way to...</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> ask someone to repeat something.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> end the conversation.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> change the subject.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. You do not know a word. The best question is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "What do you mean by that?"</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Why you talk?"</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "So do I."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. A "filler" like "well" or "let me see" helps you...</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> buy a little time to think.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> finish the conversation faster.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> correct your grammar.</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Clarification &amp; Repair Strategies</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">When you do not understand or need a moment, you have four simple tools. Keep the tone polite: start with "Sorry" or "Could you", and the request sounds friendly, never rude.</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Function</th><th style="padding:.7rem;text-align:left">Phrase</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Ask to repeat</td><td style="padding:.6rem">Could you say that again?</td><td style="padding:.6rem">"Sorry, I did not catch that. <strong>Could you say that again?</strong>"</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Ask for meaning</td><td style="padding:.6rem">What do you mean by...?</td><td style="padding:.6rem">"<strong>What do you mean by</strong> 'checkup'?"</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Buy time</td><td style="padding:.6rem">Let me think for a second.</td><td style="padding:.6rem">"That is a good question -- <strong>let me think for a second</strong>."</td></tr>
          <tr><td style="padding:.6rem;font-weight:600">Check / recap</td><td style="padding:.6rem">So, just to recap...?</td><td style="padding:.6rem">"<strong>So, just to recap,</strong> we meet at three, right?"</td></tr>
        </tbody>
      </table></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the correct word. Tap Listen to hear the whole sentence.</p>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"Sorry, I did not <input class="blank-input" data-answer="catch" data-hint="Hint: to hear and understand" data-phrase="Sorry, I did not catch your name. Could you say it again?" placeholder="___"> your name. Could you say it again?"</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"That word is new to me. Could you <input class="blank-input" data-answer="rephrase" data-hint="Hint: say it again in different words" data-phrase="That word is new to me. Could you rephrase it in simpler words?" placeholder="___"> it in simpler words?"</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"Can you <input class="blank-input" data-answer="hold" data-hint="Hint: hold ___ for a second -- wait a moment" data-phrase="Can you hold on for a second, please?" placeholder="___"> on for a second, please?"</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"So, just to <input class="blank-input" data-answer="recap" data-hint="Hint: to repeat the main points quickly" data-phrase="So, just to recap, the meeting is at three." placeholder="___">, the meeting is at three."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"Her directions were <input class="blank-input" data-answer="vague" data-hint="Hint: not clear or exact" data-phrase="Her directions were vague, so I asked her to explain again." placeholder="___">, so I asked her to explain again."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"Now your explanation makes <input class="blank-input" data-answer="sense" data-hint="Hint: to be clear -- to make ___" data-phrase="Now your explanation makes sense to me." placeholder="___"> to me."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Story in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen first, then put the sentences of the story in the correct order.</p>
      <button class="btn btn-listen" onclick="speakText('[order-l18]', this)" style="margin-bottom:1rem;display:inline-flex;align-items:center;gap:.4rem;padding:.55rem 1.2rem;background:var(--accent);color:#fff;border:none;border-radius:8px;font-size:.85rem;font-weight:600;cursor:pointer"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/></svg> Listen</button>
      <div class="order-container" id="order-l18">
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l18')"><span class="order-num">?</span><span class="order-text">I asked her to clarify and to rephrase it in simpler words.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l18')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l18')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l18')"><span class="order-num">?</span><span class="order-text">Last week I called a clinic to book a checkup.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l18')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l18')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l18')"><span class="order-num">?</span><span class="order-text">To recap, I repeated the address back to check I understood.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l18')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l18')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l18')"><span class="order-num">?</span><span class="order-text">The receptionist spoke fast, and I did not catch the time.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l18')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l18')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l18')"><span class="order-num">?</span><span class="order-text">I used a filler to hold on and think for a second.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l18')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l18')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l18')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each phrase, then record yourself saying it.</p>
      <div class="speech-card" data-phrase="Sorry, I did not catch that. Could you say it again?">
        <div class="speech-phrase">Sorry, I did not catch that. Could you say it again?</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="What do you mean by that, exactly?">
        <div class="speech-phrase">What do you mean by that, exactly?</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="Let me think for a second before I answer.">
        <div class="speech-phrase">Let me think for a second before I answer.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="So, just to recap, we meet at three, right?">
        <div class="speech-phrase">So, just to recap, we meet at three, right?</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the most natural thing to say in each real situation.</p>
      <div class="quiz-item"><div class="quiz-question">Someone gives you a phone number too fast. What do you say?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "Sorry, could you say that again?"</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Yes, thank you, goodbye."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I number not have."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">A word in the conversation is new to you and you want its meaning. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "What do you mean by that?"</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "So do I."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I mean nothing."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You need a moment to think about a hard question. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "Let me think for a second."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Repeat now, please."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I think so fast."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">The instructions were long and you want to check you understood. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "So, just to recap, is that right?"</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "I recap you now."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Neither do I."</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. There is no right or wrong answer.</p>
      <div class="think-card">
        <div class="think-question">Think about a time when you did not understand someone -- on the phone, at a store or in a fast conversation. Describe it in English. What was confusing? What could you say next time to stay in control? Try to use the repair strategies from this lesson: "Sorry, could you say that again?", "What do you mean by that?", "Let me think for a second", "So, just to recap...". Take your time and speak naturally.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-18"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 18</h4>
      <div class="survival-phrase"><span class="sp-num">1</span><span class="sp-en">Sorry, could you say that again?</span><button class="btn btn-listen" onclick="speakText('Sorry, could you say that again?',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">2</span><span class="sp-en">What do you mean by that, exactly?</span><button class="btn btn-listen" onclick="speakText('What do you mean by that, exactly?',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">3</span><span class="sp-en">Let me think for a second.</span><button class="btn btn-listen" onclick="speakText('Let me think for a second.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">4</span><span class="sp-en">Could you rephrase that in simpler words?</span><button class="btn btn-listen" onclick="speakText('Could you rephrase that in simpler words?',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">5</span><span class="sp-en">So, just to recap, is that correct?</span><button class="btn btn-listen" onclick="speakText('So, just to recap, is that correct?',this)">&#9835;</button></div>
    </div>

  </div>
</div>
'''

open("_build/ana-paula-porto-de-oliveira-fornazari-aula18/preclass.html", "w").write(HTML)
print("preclass.html written")
print("rows:", len(rows), "vocab:", len(vc))
