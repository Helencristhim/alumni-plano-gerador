# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 12 (B2, ZERO portugues na tela do aluno)."""
import os

WORDS = [
    ("To push back", "to resist or challenge a proposal, without hostility",
     "\"I'd gently push back on the timing, not the strategy.\""),
    ("To hedge", "to soften a claim so you do not commit to it fully",
     "\"I'll hedge the forecast: it might hold, but I'm not certain.\""),
    ("To take issue with", "to disagree with one specific point, not the whole",
     "\"I take issue with the assumption, not with the plan.\""),
    ("To concede", "to admit that part of the other view is right",
     "\"I concede the goal is right; it's the timing I question.\""),
    ("A reservation", "a specific doubt that stops you fully agreeing",
     "\"I have one reservation, and I think it's worth a minute.\""),
    ("To beg to differ", "a polite, slightly formal way to say you disagree",
     "\"I beg to differ on the number, and I'll tell you why.\""),
    ("To play devil's advocate", "to argue the opposite side on purpose, to test an idea",
     "\"Let me play devil's advocate for a moment on this deal.\""),
    ("To stand your ground", "to hold your position calmly under pressure",
     "\"On this one figure, I'd ask to stand my ground.\""),
    ("A sticking point", "the one issue that is blocking the agreement",
     "\"The sticking point isn't the deal; it's the sequence.\""),
    ("Common ground", "the points both sides already agree on",
     "\"On the strategy we have common ground; my doubt is timing.\""),
    ("To qualify", "to add a limit that makes a statement less absolute",
     "\"Let me qualify that: it works only if we refinance first.\""),
    ("Tentative", "cautious and not final, leaving room to change",
     "\"My view is tentative; I'd want to see the covenants first.\""),
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


TEMPLATE = '''<div class="lesson-card" id="ex-lesson-12">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1600880292203-757bb62b4baf?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 12 -- Pre-class</div>
      <h3>The Art of Pushback -- Disagreeing in Board Meetings</h3>
      <div class="lesson-desc">Disagree with a board without turning the meeting into a fight -- and never confuse silence with loyalty. Key words: to push back, to hedge, to take issue with, to concede, a reservation, to beg to differ, to play devil's advocate, to stand your ground, a sticking point, common ground, to qualify, tentative. Structure: diplomatic disagreement and hedging -- soften a claim with might/could, downtone with not entirely, concede then counter, and disagree as a question.</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="12" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="12">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each term and read the example. Every example is a real sentence from a board meeting -- this is how you disagree out loud, not how you write it in a memo.</p>
      <div class="vocab-cards">
{VOCAB}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each term with its correct definition.</p>
      <div class="match-grid" id="match-l12">
{MATCH}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text and answer the questions.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>The board wanted to close the acquisition this quarter, and every head was nodding. Felipe had a doubt, and this time he did not swallow it. <strong>I'm with you on the logic</strong>, he said, <strong>but I'd gently push back</strong> on the timing. He did not say the deal was wrong; he registered a reservation. <strong>I'm not entirely convinced</strong> the covenant headroom is enough, he went on, and <strong>could we be</strong> underestimating the downside? Notice what he did: he conceded first -- <strong>while I concede the target is right</strong> -- and only then named the one thing he could not move on. <strong>That might be a quarter too early</strong>, he said, softening the certainty rather than flattening it. On everything else, he told the chair, we have common ground; on this one figure, I'd stand my ground. Nobody left the room angry, and the refinancing was arranged first. None of the phrases in bold attack anyone. They hedge, they concede, they ask -- and that is exactly why the board kept listening.</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. Why does Felipe open with "I'm with you on the logic" BEFORE he disagrees?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Conceding the common ground first is what keeps the room listening instead of defending.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Because he actually agrees with everything and has no real objection.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because it is rude to start a sentence with a verb.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. What does turning "you are wrong" into "could we be underestimating...?" achieve?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> It hides Felipe's opinion so nobody knows what he thinks.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> It disagrees as a question, so the room reasons WITH him instead of feeling attacked.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> It adds a new financial fact to the debate.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. He says "that might be a quarter too early" instead of "that is too early." Why hedge?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because he is not sure the room can hear him.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Might" softens the certainty, leaving the board room to move rather than a flat verdict to resist.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because "might" is more formal and impressive than "is."</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Hedging &amp; Diplomatic Disagreement</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">How to disagree without the word "wrong". The order is the trick: concede what is true, hedge what is uncertain, and be unequivocal only on the one line that matters.</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Move</th><th style="padding:.7rem;text-align:left">Structure</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Soften with a modal</td><td style="padding:.6rem">might &middot; could &middot; would &middot; I'd tend to think</td><td style="padding:.6rem">"That might be too optimistic."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Downtone the claim</td><td style="padding:.6rem">not quite &middot; not entirely &middot; a little &middot; somewhat</td><td style="padding:.6rem">"I'm not entirely convinced it holds."</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Concede, then counter</td><td style="padding:.6rem">While I take your point, ... &middot; I see the logic, but ...</td><td style="padding:.6rem">"While I agree on the goal, I'd question the timing."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Disagree as a question</td><td style="padding:.6rem">Could we be...? &middot; Is it possible that...?</td><td style="padding:.6rem">"Could we be moving too fast?"</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Register a reservation</td><td style="padding:.6rem">I have one reservation... &middot; My hesitation is...</td><td style="padding:.6rem">"I have one reservation about the assumptions."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Hold your ground, warmly</td><td style="padding:.6rem">I hear you, and I'd still... &middot; That may be so, but...</td><td style="padding:.6rem">"I hear you -- and I'd still flag the covenant."</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>The test that never fails:</strong> disagreement that lands as an attack ends the conversation; disagreement that concedes, hedges, and asks keeps it open. Say no by first saying yes to everything you honestly can -- then be unequivocal on the one line that matters, and warm about all the rest.</p>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the correct word. Tap Listen to hear the whole sentence.</p>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"I'm with you on the strategy, but I'd gently <input class="blank-input" data-answer="push back" data-hint="Hint: challenge a proposal without hostility" data-phrase="I'm with you on the strategy, but I'd gently push back on the timing." placeholder="___"> on the timing."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"I have one <input class="blank-input" data-answer="reservation" data-hint="Hint: a specific doubt that stops you fully agreeing" data-phrase="I have one reservation, and I think it's worth a minute." placeholder="___"> , and I think it's worth a minute."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"I <input class="blank-input" data-answer="concede" data-hint="Hint: admit that part of the other view is right" data-phrase="I concede the goal is right; it's the timing I question." placeholder="___"> the goal is right; it's the timing I question."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"On the strategy we have <input class="blank-input" data-answer="common ground" data-hint="Hint: the points both sides already agree on" data-phrase="On the strategy we have common ground; my doubt is the sequence." placeholder="___"> ; my doubt is the sequence."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"The <input class="blank-input" data-answer="sticking point" data-hint="Hint: the one issue that is blocking the agreement" data-phrase="The sticking point isn't the deal; it's the debt." placeholder="___"> isn't the deal; it's the debt."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"Let me <input class="blank-input" data-answer="qualify" data-hint="Hint: add a limit that makes a statement less absolute" data-phrase="Let me qualify that: it works only if we refinance first." placeholder="___"> that: it works only if we refinance first."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Pushback in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the steps of a diplomatic disagreement in the right order. Leading with "no", instead of conceding first, is the mistake that makes the room stop listening.</p>
      <div class="order-container" id="order-l12">
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l12')"><span class="order-num">?</span><span class="order-text">Hedge the uncertain part and turn the accusation into a question.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l12')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l12')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l12')"><span class="order-num">?</span><span class="order-text">Concede what is genuinely right, so the room knows you have listened.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l12')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l12')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l12')"><span class="order-num">?</span><span class="order-text">Ask what would change their mind, and then listen.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l12')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l12')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l12')"><span class="order-num">?</span><span class="order-text">Register your one reservation, out loud and clearly.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l12')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l12')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l12')"><span class="order-num">?</span><span class="order-text">Name your sticking point and stand your ground on it, warmly.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l12')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l12')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l12')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it. For each one, notice which move it is -- concede, hedge, question, or hold your ground.</p>
      <div class="speech-card" data-phrase="I'm with you on the logic, but I'd gently push back on the timing.">
        <div class="speech-phrase">I'm with you on the logic, but I'd gently push back on the timing.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="While I take your point, could we be underestimating the downside?">
        <div class="speech-phrase">While I take your point, could we be underestimating the downside?</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="I have one reservation, and I think it's worth a minute.">
        <div class="speech-phrase">I have one reservation, and I think it's worth a minute.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="On everything else we have common ground; on this one figure, I'd stand my ground.">
        <div class="speech-phrase">On everything else we have common ground; on this one figure, I'd stand my ground.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="I beg to differ, and I'll tell you exactly why.">
        <div class="speech-phrase">I beg to differ, and I'll tell you exactly why.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best response for each real moment of a board meeting.</p>
      <div class="quiz-item"><div class="quiz-question">A director proposes doubling the marketing budget. You disagree. The best opener is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "No, that's far too much money."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I'm with you on the ambition, but I'd push back gently on the size of the number."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Say nothing and let the budget pass.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You think a forecast is too optimistic. The most diplomatic move is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "That might be a little optimistic; I'm not entirely convinced the top line holds."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Those numbers are wrong."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "You always overestimate revenue."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You want to challenge a risky assumption without attacking the person. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "You are underestimating the risk."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Could we be underestimating the downside here?"</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "This whole idea is a mistake."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You agree with 90% of a plan but not the timing. The best framing is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "I disagree with the plan."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "On the strategy we have common ground; my one sticking point is the sequence."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Fine, whatever the room prefers."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">The board pressures you to drop your one objection. You should:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "I hear you -- and I'd still flag the covenant. I'm not blocking, I'm flagging."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Give in immediately to keep the peace.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Raise your voice and refuse to continue.</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the prompt below. There is no right or wrong answer -- speak for 2 to 3 minutes, without a script.</p>
      <div class="think-card">
        <div class="think-question">Your board wants to approve a decision you have doubts about. Speak for 2-3 minutes and disagree diplomatically. Open by conceding what is genuinely right and naming the common ground. Register your one reservation. Hedge the uncertain part ("that might be...", "I'm not entirely convinced...") and turn one accusation into a question ("could we be...?"). Name your sticking point and stand your ground on it -- warmly, without attacking anyone. Finish by asking what would change their mind.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-12"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 12</h4>
      <div class="survival-phrase"><span class="sp-num">1</span><span class="sp-en">I'm with you on the logic -- but I'd gently push back on the timing.</span><button class="btn btn-listen" data-speak="I'm with you on the logic, but I'd gently push back on the timing." onclick="speakText(this.dataset.speak,this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">2</span><span class="sp-en">While I take your point, could we be underestimating the downside?</span><button class="btn btn-listen" data-speak="While I take your point, could we be underestimating the downside?" onclick="speakText(this.dataset.speak,this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">3</span><span class="sp-en">I have one reservation, and I think it's worth a minute.</span><button class="btn btn-listen" data-speak="I have one reservation, and I think it's worth a minute." onclick="speakText(this.dataset.speak,this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">4</span><span class="sp-en">On everything else we have common ground; on this one figure, I'd stand my ground.</span><button class="btn btn-listen" data-speak="On everything else we have common ground; on this one figure, I'd stand my ground." onclick="speakText(this.dataset.speak,this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">5</span><span class="sp-en">I beg to differ -- and I'll tell you exactly why.</span><button class="btn btn-listen" data-speak="I beg to differ, and I'll tell you exactly why." onclick="speakText(this.dataset.speak,this)">&#9835;</button></div>
    </div>

  </div>
</div>
'''

out = TEMPLATE.replace("{VOCAB}", vocab_cards()).replace("{MATCH}", match_rows())
here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "preclass.html"), "w", encoding="utf-8") as f:
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
    if opts and opts[1] == ans:  # correct should not be first real option (after Select...)
        pass
print("match rows:", len(rows), "bad:", bad)
