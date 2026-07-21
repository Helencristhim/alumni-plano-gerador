# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 11 (B2, ZERO portugues na tela do aluno)."""
import html

WORDS = [
    ("Agenda", "the running order you promise the room at the start",
     "\"Let me give you the agenda before I show a single number.\""),
    ("Headline number", "the one figure that matters most in the whole deck",
     "\"The headline number is this: we are two million below plan.\""),
    ("Bottom line", "the essential conclusion, with the detail stripped away",
     "\"The bottom line is that the fix is already working.\""),
    ("To drill down", "to move from the summary into the detail of one point",
     "\"Let me drill down into the three drivers behind that gap.\""),
    ("Caveat", "a warning that limits or qualifies what you just said",
     "\"I want to flag this figure with one honest caveat.\""),
    ("To gloss over", "to pass over something quickly so nobody examines it",
     "\"Do not gloss over the one number you are frightened of.\""),
    ("To circle back", "to return to a point you deliberately postponed",
     "\"Let me circle back to that question in two minutes.\""),
    ("Ballpark", "an approximate figure, close but not exact",
     "\"In ballpark terms it is around three million.\""),
    ("To field a question", "to take and answer a question from the room",
     "\"I will field questions at the end, not during the numbers.\""),
    ("Deep dive", "a long, detailed look at one part of the story",
     "\"Slide nine is a deep dive into what changed this quarter.\""),
    ("Recap", "a short summary of what you have just covered",
     "\"Let me give you a thirty-second recap before questions.\""),
    ("Sanity check", "a quick test that a number is roughly reasonable",
     "\"One sanity check: does that margin even look possible?\""),
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


TEMPLATE = '''<div class="lesson-card" id="ex-lesson-11">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1573497620053-ea5300f94f21?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 11 -- Pre-class</div>
      <h3>Holding the Room -- High-Stakes Financial Presentations</h3>
      <div class="lesson-desc">Guide a room, do not just present to it -- and never gloss over the number you are frightened of. Key words: agenda, headline number, bottom line, to drill down, caveat, to gloss over, to circle back, ballpark, to field a question, deep dive, recap, sanity check. Structure: signposting language -- the phrases that carry no facts and yet decide whether a board follows you or gets lost (open, move on, drill down, defer, flag a caveat, conclude).</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="11" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="11">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each term and read the example. Notice that every example is a real sentence from a meeting room -- this is how you say it, not how you write it in a report.</p>
      <div class="vocab-cards">
{VOCAB}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each term with its correct definition.</p>
      <div class="match-grid" id="match-l11">
{MATCH}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text and answer the questions.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>Felipe had the right numbers and still used to lose the room. This quarter he did it differently. <strong>Let me start by</strong> giving you the <strong>agenda</strong>, he said, and the <strong>bottom line</strong> is that we are two million below plan. He did not build up to it; he gave the <strong>headline number</strong> first. When the chair fired a hard question mid-slide, he did not panic. <strong>That is exactly the right question,</strong> he said, <strong>let me circle back to</strong> it in two minutes, when the next slide makes the answer obvious. He did not <strong>gloss over</strong> the weak figure either. <strong>I want to flag</strong> one number with an honest <strong>caveat</strong>, he said, and slowed down instead of speeding up. <strong>Let me drill down into</strong> the margin. And when he did not have an exact split, he did not invent one: in <strong>ballpark</strong> terms it is around 1.4 million, he said, and I will confirm the exact figure tonight. <strong>To sum up,</strong> he closed, three things matter -- the miss, the caveat, and the fix. Notice that none of the phrases in bold carry a fact. They are signposts: they tell the board where they are.</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. Why does Felipe give the headline number FIRST, instead of building up to it?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Because a board that does not know where you are going stops listening and starts hunting.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Because the headline number is always good news.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because he wants to fill the first slide with text.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. What do the phrases in bold ("Let me start by...", "That brings me to...") actually do?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> They add extra financial detail to each number.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> They carry no fact -- they tell the room where they are (opening, moving, deferring, closing).</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> They are optional decoration with no effect on the audience.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. He does not have the exact revenue split. What is the senior move?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Invent a precise-sounding number and hope nobody checks.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Give the ballpark figure and promise the exact one -- "around 1.4 million; I will confirm tonight."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Say nothing and move quickly to the next slide.</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Signposting Language</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">How to guide a room without adding a single fact. A signpost tells the listener WHERE they are: opening, moving on, drilling down, deferring, flagging, or closing.</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Function</th><th style="padding:.7rem;text-align:left">Signpost</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Open / agenda</td><td style="padding:.6rem">Let me start by... &middot; I'll cover three things</td><td style="padding:.6rem">"Let me start by giving you the agenda."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Move on</td><td style="padding:.6rem">That brings me to... &middot; Moving on to...</td><td style="padding:.6rem">"That brings me to the headline number."</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Drill down</td><td style="padding:.6rem">Let me drill down into... &middot; If we look more closely</td><td style="padding:.6rem">"Let me drill down into the margin."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Defer</td><td style="padding:.6rem">Let me circle back to... &middot; I'll come back to that</td><td style="padding:.6rem">"Let me circle back to that in two minutes."</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Flag a caveat</td><td style="padding:.6rem">I want to flag... &middot; One caveat here</td><td style="padding:.6rem">"I want to flag one figure with a caveat."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Conclude</td><td style="padding:.6rem">To sum up... &middot; The bottom line is...</td><td style="padding:.6rem">"To sum up, three things matter tonight."</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>The test that never fails:</strong> delete the signpost. Is any number lost? No. So what is lost? The map. A signpost adds no fact -- it tells the room where they are. That map is exactly what keeps a board following you instead of hunting you. Open with the headline number, flag the weak one, defer a hard question out loud, and close with a clean recap.</p>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the correct word. Tap Listen to hear the whole sentence.</p>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"Let me give you the <input class="blank-input" data-answer="agenda" data-hint="Hint: the running order you promise at the start" data-phrase="Let me give you the agenda: three things, then questions." placeholder="___"> : three things, then questions."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"The <input class="blank-input" data-answer="bottom line" data-hint="Hint: the essential conclusion, detail stripped away" data-phrase="The bottom line is that we are two million below plan." placeholder="___"> is that we are two million below plan."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"That is the right question -- let me <input class="blank-input" data-answer="circle back" data-hint="Hint: return to a point you postponed" data-phrase="Let me circle back to that in two minutes." placeholder="___"> to that in two minutes."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"I want to flag one figure here with an honest <input class="blank-input" data-answer="caveat" data-hint="Hint: a warning that qualifies what you said" data-phrase="I want to flag one figure here with an honest caveat." placeholder="___"> ."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"I do not have the exact split; in <input class="blank-input" data-answer="ballpark" data-hint="Hint: an approximate figure, not exact" data-phrase="In ballpark terms it is around three million." placeholder="___"> terms it is around three million."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"Do not <input class="blank-input" data-answer="gloss over" data-hint="Hint: pass over quickly so nobody examines it" data-phrase="Do not gloss over the one number you are frightened of." placeholder="___"> the one number you are frightened of."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Board Presentation in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the steps of a high-stakes board presentation in the right order. Building up to the headline number, instead of opening with it, is the mistake that makes a board stop listening.</p>
      <div class="order-container" id="order-l11">
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l11')"><span class="order-num">?</span><span class="order-text">Flag the weak number as a caveat -- slow down, do not gloss over it.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l11')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l11')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l11')"><span class="order-num">?</span><span class="order-text">Open with the agenda and the headline number in the first thirty seconds.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l11')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l11')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l11')"><span class="order-num">?</span><span class="order-text">Close with a clean recap of exactly three things, then field questions.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l11')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l11')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l11')"><span class="order-num">?</span><span class="order-text">Drill down into the reason behind the miss, one driver at a time.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l11')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l11')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l11')"><span class="order-num">?</span><span class="order-text">Park any hard question out loud and circle back to it with a time.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l11')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l11')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l11')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it. For each one, say which signpost you are using -- open, defer, flag, or close.</p>
      <div class="speech-card" data-phrase="Let me start with the agenda and the headline number.">
        <div class="speech-phrase">Let me start with the agenda and the headline number.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="The bottom line is that we are two million below plan.">
        <div class="speech-phrase">The bottom line is that we are two million below plan.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="That is exactly the right question. Let me circle back to it in two minutes.">
        <div class="speech-phrase">That is exactly the right question. Let me circle back to it in two minutes.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="I want to flag one figure here that deserves a proper caveat.">
        <div class="speech-phrase">I want to flag one figure here that deserves a proper caveat.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="To sum up: the headline number, the one caveat, and the fix.">
        <div class="speech-phrase">To sum up: the headline number, the one caveat, and the fix.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best response for each real moment of a board presentation.</p>
      <div class="quiz-item"><div class="quiz-question">You open a board meeting after missing plan. The best first line is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "A lot happened this quarter, let me walk you through every slide."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "The bottom line is this: we are two million below plan. Here is the agenda."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I will save the main number for the end."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">A director interrupts with a hard question mid-slide. You should:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "That is exactly the right question -- let me circle back to it in two minutes."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Panic and answer it immediately, out of order.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Ignore it and keep reading the slide.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You reach the number you are most afraid of. The senior move is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Say it fast and quietly and move on before anyone reacts.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I want to flag one figure with a caveat" -- slow down and give the reason.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Skip the slide entirely and hope nobody asks.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">Someone asks for a figure you do not have exactly. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "It is exactly 3,142,000." (you are guessing)</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "In ballpark terms around three million; I will confirm the exact figure and circle back."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I have no idea, sorry."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You have two minutes left and three slides. The best move is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Sprint silently through all three slides.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Let me skip the detail and give you the recap: three things matter tonight."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Stop mid-sentence and end abruptly.</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the prompt below. There is no right or wrong answer -- speak for 2 to 3 minutes, without a script.</p>
      <div class="think-card">
        <div class="think-question">You are presenting a quarter that missed plan to a nervous board. Speak for 2-3 minutes. Open with the agenda and the headline number in the first thirty seconds -- do not build up to it. Signpost at least two transitions ("that brings me to...", "let me drill down into..."). Flag one honest caveat and slow down on it instead of glossing over it. Then imagine a hard question, park it out loud with a time, and circle back. Finish with a clean recap of exactly three things.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-11"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 11</h4>
      <div class="survival-phrase"><span class="sp-num">1</span><span class="sp-en">Let me start with the agenda and the headline number.</span><button class="btn btn-listen" data-speak="Let me start with the agenda and the headline number." onclick="speakText(this.dataset.speak,this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">2</span><span class="sp-en">The bottom line is that we are two million below plan.</span><button class="btn btn-listen" data-speak="The bottom line is that we are two million below plan." onclick="speakText(this.dataset.speak,this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">3</span><span class="sp-en">That is exactly the right question -- let me circle back to it in two minutes.</span><button class="btn btn-listen" data-speak="That is exactly the right question. Let me circle back to it in two minutes." onclick="speakText(this.dataset.speak,this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">4</span><span class="sp-en">I want to flag one figure here that deserves a proper caveat.</span><button class="btn btn-listen" data-speak="I want to flag one figure here that deserves a proper caveat." onclick="speakText(this.dataset.speak,this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">5</span><span class="sp-en">To sum up: the headline number, the one caveat, and the fix.</span><button class="btn btn-listen" data-speak="To sum up: the headline number, the one caveat, and the fix." onclick="speakText(this.dataset.speak,this)">&#9835;</button></div>
    </div>

  </div>
</div>
'''

out = TEMPLATE.replace("{VOCAB}", vocab_cards()).replace("{MATCH}", match_rows())
with open("_build/felipe-pimenta-aula11/preclass.html", "w", encoding="utf-8") as f:
    f.write(out)
print("preclass.html written; words:", len(WORDS))
# sanity: every data-answer must be a valid option value in its row
import re
rows = re.findall(r'<div class="match-row" data-answer="([^"]+)">(.*?)</select>', out, re.S)
bad = 0
for ans, body in rows:
    opts = re.findall(r'<option value="([^"]*)">', body)
    if ans not in opts:
        bad += 1
        print("MISSING option for answer:", ans)
    # shuffle check: correct not in same index as row position handled; check not first
print("match rows:", len(rows), "bad:", bad)
