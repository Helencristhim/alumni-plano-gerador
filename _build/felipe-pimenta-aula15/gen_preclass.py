# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 15 (B2, ZERO portugues na tela do aluno)."""

WORDS = [
    ("Small talk", "easy, light conversation about the ordinary things in life",
     "\"The first ten minutes of any dinner are small talk, and they matter more than people think.\""),
    ("To catch up", "to meet someone and share news since you last met",
     "\"We should catch up properly the next time I am in London.\""),
    ("To hit it off", "to like each other immediately, from the first minute",
     "\"We hit it off over a plate of pasta and talked for three hours.\""),
    ("To be into", "to be genuinely interested in something",
     "\"I am really into cooking; I did a French course and an Italian one.\""),
    ("To be up for", "to be willing and keen to do something",
     "\"Are you up for dinner on Friday? I know a place.\""),
    ("To grab a bite", "to eat something quick and informal",
     "\"We can grab a bite near the office before your train.\""),
    ("A hidden gem", "a wonderful place that very few people know about",
     "\"That little place behind the market is a real hidden gem.\""),
    ("Comfort food", "simple food that makes you feel safe and at home",
     "\"For me, comfort food is rice and beans on a Sunday.\""),
    ("Overrated", "praised much more than it deserves",
     "\"Honestly, the famous one is overrated; the corner place is better.\""),
    ("To wind down", "to relax slowly at the end of a day or a week",
     "\"I wind down by cooking something slow on a Saturday.\""),
    ("Homesick", "sad because you are far from home",
     "\"The first month abroad I was homesick, mostly for the food.\""),
    ("Down-to-earth", "practical and easy to talk to, with no airs",
     "\"The whole team is down-to-earth; nobody mentions titles at dinner.\""),
]

VOL = "<svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\"><polygon points=\"11 5 6 9 2 9 2 15 6 15 11 19 11 5\"/><path d=\"M15.54 8.46a5 5 0 010 7.07\"/></svg>"


def vocab_cards():
    out = []
    for w, d, ex in WORDS:
        out.append(
            f'        <div class="vocab-card-pc"><div class="vocab-card-content">'
            f'<div class="vocab-card-header"><span class="vocab-card-word">{w}</span>'
            f'<span class="vocab-card-dot"> -- </span><span class="vocab-card-def">{d}</span></div>'
            f'<div class="vocab-card-example">{ex}</div></div>'
            f'<button class="audio-btn" data-speak="{w}" onclick="speakText(this.dataset.speak,this)">{VOL} Listen</button></div>')
    return "\n".join(out)


def match_rows():
    defs = [d for _, d, _ in WORDS]
    out = []
    for i, (w, d, _) in enumerate(WORDS):
        # ordem embaralhada e DIFERENTE da ordem das palavras (rotacao + espelho)
        rot = defs[i + 3:] + defs[:i + 3]
        opts = list(reversed(rot))
        if opts[i % len(opts)] == d:  # garante que a correta nao caia na mesma posicao do indice
            opts = opts[1:] + opts[:1]
        options = "".join(f'<option value="{o}">{o}</option>' for o in opts)
        out.append(
            f'        <div class="match-row" data-answer="{d}">'
            f'<span class="match-word" style="flex:0 0 150px">{w}</span>'
            f'<select style="flex:1;width:100%" onchange="checkMatch(this)">'
            f'<option value="">Select...</option>{options}</select></div>')
    return "\n".join(out)


TEMPLATE = '''<div class="lesson-card" id="ex-lesson-15">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 15 -- Pre-class</div>
      <h3>Life Beyond the Spreadsheet -- Food, Culture &amp; Daily Life</h3>
      <div class="lesson-desc">They already know you can do the job; the dinner afterwards decides whether they want to sit next to you. Key words: small talk, to catch up, to hit it off, to be into, to be up for, to grab a bite, a hidden gem, comfort food, overrated, to wind down, homesick, down-to-earth. Structure: question tags and short responses -- the tag that flips the sentence and borrows its auxiliary (isn't it, are you, don't you), and the two-word answer that keeps the rally alive (So am I, Neither do I, Did you?).</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="15" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="15">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each expression and read the example. None of these words is technical -- and that is exactly why nobody ever taught them to you at work.</p>
      <div class="vocab-cards">
{VOCAB}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each expression with its correct definition.</p>
      <div class="match-grid" id="match-l15">
{MATCH}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text and answer the questions.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>The interview was over, and then they booked a table. No numbers, no slides -- ten minutes of <strong>small talk</strong> while the menus came round. His colleague opened the way people open at a table: <strong>You are not from here originally, are you?</strong> Notice the shape of it. The sentence is negative, so the tag is positive; it is not really a question, it is a way of checking something she already half-knew. He said no, three weeks, and that he still got a little <strong>homesick</strong> -- mostly for the food. <strong>Do you?</strong> she said, and the conversation had somewhere to go. He told her he was genuinely <strong>into</strong> cooking, that he <strong>winds down</strong> with something slow on a Saturday, and that his <strong>comfort food</strong> was rice and beans. Then, instead of stopping, he handed it back: and you? She laughed. I cook badly and constantly. <strong>So do I</strong>, he said. By the second course they had agreed the famous place on the square was <strong>overrated</strong> -- <strong>it is, isn't it?</strong> -- and that the six-table room behind the market was the real <strong>hidden gem</strong>. They <strong>hit it off</strong> over pasta. She asked whether he was <strong>up for</strong> Friday. He was. Nobody mentioned the job once.</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. Why does his colleague say "You are not from here originally, are you?" instead of "aren't you?"</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> The sentence is negative, so the tag flips to positive.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Both are possible; she simply chose the shorter one.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> She is not sure of the answer, so she uses a softer form.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. What does "So do I" do in that moment?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> It corrects what she said about her own cooking.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> It agrees in one beat, using the auxiliary from her sentence.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> It asks her to repeat what she has just said.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. What is the one move that keeps the conversation alive after he answers?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> He gives longer answers with more detail each time.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> He returns to his professional experience to sound credible.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> Instead of stopping, he hands the question straight back to her.</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Question Tags and Short Responses</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">A tag is not a question -- it is an invitation. A short response is not an answer -- it is a pass back. Both are built the same way: take the auxiliary out of the sentence in front of you and reuse it.</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Use</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Positive sentence &rarr; negative tag</td><td style="padding:.6rem">invite agreement, warmly</td><td style="padding:.6rem">"That was a hidden gem, wasn't it?"</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Negative sentence &rarr; positive tag</td><td style="padding:.6rem">check something you half-know</td><td style="padding:.6rem">"You're not from here, are you?"</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">The tag copies the auxiliary</td><td style="padding:.6rem">be &middot; have &middot; do &middot; the modal</td><td style="padding:.6rem">"You can cook, can't you?"</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">So + auxiliary + I &middot; Neither + auxiliary + I</td><td style="padding:.6rem">agree in one beat</td><td style="padding:.6rem">"I'm into food." &mdash; "So am I."</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Echo: auxiliary + you?</td><td style="padding:.6rem">show interest, hand the turn back</td><td style="padding:.6rem">"Did you? What was that like?"</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>The test that never fails:</strong> find the auxiliary, then flip it. <strong>have &rarr; haven't you</strong>, <strong>are &rarr; aren't you</strong>, <strong>am &rarr; so am I</strong>, <strong>did &rarr; did you?</strong> If there is no auxiliary in the sentence, the auxiliary is <strong>do</strong> -- "You like Italian food, <strong>don't you?</strong>". And remember that <strong>too</strong> never agrees with a negative; <strong>neither</strong> does.</p>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the correct word. Tap Listen to hear the whole sentence.</p>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"That little place behind the market is a real <input class="blank-input" data-answer="hidden gem" data-hint="Hint: a great place almost nobody knows about" data-phrase="That little place behind the market is a real hidden gem." placeholder="___">."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"The famous restaurant on the square is a bit <input class="blank-input" data-answer="overrated" data-hint="Hint: praised more than it deserves" data-phrase="The famous restaurant on the square is a bit overrated." placeholder="___">."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"We <input class="blank-input" data-answer="hit it off" data-hint="Hint: liked each other immediately" data-phrase="We hit it off the moment we started talking about food." placeholder="___"> the moment we started talking about food."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"Are you <input class="blank-input" data-answer="up for" data-hint="Hint: willing and keen to do it" data-phrase="Are you up for grabbing a bite on Friday?" placeholder="___"> grabbing a bite on Friday?"</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"For me, <input class="blank-input" data-answer="comfort food" data-hint="Hint: simple food that makes you feel at home" data-phrase="For me, comfort food is rice and beans on a Sunday." placeholder="___"> is rice and beans on a Sunday."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"You are not from here originally, <input class="blank-input" data-answer="are you" data-hint="Hint: a negative sentence takes a positive tag" data-phrase="You are not from here originally, are you?" placeholder="___">?"</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: The Anatomy of a Rally</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the five moves of a good exchange in the right order. Answering and then stopping is the mistake that leaves the table silent.</p>
      <div class="order-container" id="order-l15">
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l15')"><span class="order-num">?</span><span class="order-text">Echo what they say to show interest -- Did you? Really?</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l15')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l15')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l15')"><span class="order-num">?</span><span class="order-text">Answer the question about yourself -- briefly.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l15')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l15')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l15')"><span class="order-num">?</span><span class="order-text">Turn the interest into a plan -- are you up for Friday?</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l15')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l15')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l15')"><span class="order-num">?</span><span class="order-text">Add the one thing you are genuinely into.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l15')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l15')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l15')"><span class="order-num">?</span><span class="order-text">Hand it back -- ask them the same thing.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l15')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l15')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l15')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it. Let the tag fall, not rise -- a tag that rises sounds like doubt, and these are invitations.</p>
      <div class="speech-card" data-phrase="I'm really into cooking, actually. Do you cook at all?">
        <div class="speech-phrase">I'm really into cooking, actually. Do you cook at all?</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="That little place is a real hidden gem, isn't it?">
        <div class="speech-phrase">That little place is a real hidden gem, isn't it?</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="You're not from here originally, are you?">
        <div class="speech-phrase">You're not from here originally, are you?</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="Did you? What was that like?">
        <div class="speech-phrase">Did you? What was that like?</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="Are you up for grabbing a bite on Friday? This one is on me.">
        <div class="speech-phrase">Are you up for grabbing a bite on Friday? This one is on me.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the answer that keeps the conversation alive.</p>
      <div class="quiz-item"><div class="quiz-question">A colleague asks what you do outside work. The strongest answer is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I am a CFO. I manage a team of forty."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I'm really into cooking, actually. Do you cook at all?"</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Not much, honestly. I work a lot."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You suspect the person opposite you did not grow up in this city. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "You're not from here originally, are you?"</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "You are not from here, aren't you?"</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "You are not from here, no?"</div></div></div>
      <div class="quiz-item"><div class="quiz-question">She says: "I don't eat much meat during the week." You agree:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I don't too."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Me also."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> "Neither do I, most of the week."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">He says: "I lived in Liverpool for a year." The reply that keeps the rally going:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "That is interesting."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Did you? What was that like?"</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I have been to England too."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">A colleague praises the famous restaurant on the square. You disagree warmly:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "No, that place is bad."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "It is famous, isn't it? Honestly, though, I find it a bit overrated."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Yes, I agree completely."</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the prompt below. There is no right or wrong answer -- speak for 2 to 3 minutes, without a script.</p>
      <div class="think-card">
        <div class="think-question">You are at a dinner table abroad with two people you have just met, the night after a job offer. Not one word about work. Talk about what you are into and how you wind down, name one place you think is overrated and one hidden gem you would take them to, and say what your comfort food is and why you miss it. Somewhere in it, use a question tag and a short response -- and finish by inviting them out on Friday.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-15"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 15</h4>
      <div class="survival-phrase"><span class="sp-num">1</span><span class="sp-en">I'm really into cooking, actually. Do you cook at all?</span><button class="btn btn-listen" data-speak="I'm really into cooking, actually. Do you cook at all?" onclick="speakText(this.dataset.speak,this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">2</span><span class="sp-en">That little place is a real hidden gem, isn't it?</span><button class="btn btn-listen" data-speak="That little place is a real hidden gem, isn't it?" onclick="speakText(this.dataset.speak,this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">3</span><span class="sp-en">You're not from here originally, are you?</span><button class="btn btn-listen" data-speak="You're not from here originally, are you?" onclick="speakText(this.dataset.speak,this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">4</span><span class="sp-en">Did you? What was that like?</span><button class="btn btn-listen" data-speak="Did you? What was that like?" onclick="speakText(this.dataset.speak,this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">5</span><span class="sp-en">Are you up for grabbing a bite on Friday? This one is on me.</span><button class="btn btn-listen" data-speak="Are you up for grabbing a bite on Friday? This one is on me." onclick="speakText(this.dataset.speak,this)">&#9835;</button></div>
    </div>

  </div>
</div>
'''

out = TEMPLATE.replace("{VOCAB}", vocab_cards()).replace("{MATCH}", match_rows())
with open("_build/felipe-pimenta-aula15/preclass.html", "w", encoding="utf-8") as f:
    f.write(out)
print("preclass.html written; words:", len(WORDS))
import re
rows = re.findall(r'<div class="match-row" data-answer="([^"]+)">(.*?)</select>', out, re.S)
bad = 0
for ans, body in rows:
    opts = re.findall(r'<option value="([^"]*)">', body)
    if ans not in opts:
        bad += 1
        print("MISSING option for answer:", ans)
print("match rows:", len(rows), "bad:", bad)
