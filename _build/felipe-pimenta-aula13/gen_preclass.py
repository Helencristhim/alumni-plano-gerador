# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 13 (B2, ZERO portugues na tela do aluno)."""

WORDS = [
    ("Top line", "a company's total revenue, before any cost is taken out",
     "\"The top line grew nine per cent, but the real story is in the margin.\""),
    ("Year on year", "compared with the same period twelve months earlier",
     "\"Revenue is up eleven per cent year on year.\""),
    ("Like-for-like", "compared on the same basis, with any distortion stripped out",
     "\"On a like-for-like basis, growth is closer to four per cent.\""),
    ("Underlying", "the real trend once one-off items are removed",
     "\"Underlying demand is stronger than the headline suggests.\""),
    ("To outperform", "to do better than the plan, the market, or your peers",
     "\"We outperformed the sector by six points this quarter.\""),
    ("To lag", "to fall behind the plan or the competition",
     "\"Cash collection is lagging the forecast by two weeks.\""),
    ("To edge up", "to rise slowly and by a small amount",
     "\"Margins edged up from twenty-one to twenty-two per cent.\""),
    ("To surge", "to rise sharply and fast",
     "\"New sign-ups surged after the launch.\""),
    ("To plateau", "to stop rising and level off",
     "\"Growth plateaued in the second half of the year.\""),
    ("A one-off", "a single item that will not happen again",
     "\"That gain was a one-off; do not build it into next year.\""),
    ("To offset", "to cancel out one movement with an opposite one",
     "\"Higher volumes offset the drop in price.\""),
    ("Momentum", "the sense that a trend is feeding on itself and building",
     "\"The numbers show real momentum going into the fourth quarter.\""),
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


TEMPLATE = '''<div class="lesson-card" id="ex-lesson-13">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 13 -- Pre-class</div>
      <h3>Numbers Do Not Lie -- Discussing Financial Performance</h3>
      <div class="lesson-desc">A number on its own means almost nothing -- dress it in a trend and a comparison. Key words: top line, year on year, like-for-like, underlying, to outperform, to lag, to edge up, to surge, to plateau, a one-off, to offset, momentum. Structure: the language of trends and comparison -- verbs of movement sized to the change (edged up, surged, plateaued), prepositions of change (up from... to..., by, at) and comparison frames (year on year, like-for-like, ahead of plan).</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="13" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="13">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each term and read the example. Notice that every example is a real sentence from a results review -- this is how you comment on a number out loud, not how you write it in a report.</p>
      <div class="vocab-cards">
{VOCAB}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each term with its correct definition.</p>
      <div class="match-grid" id="match-l13">
{MATCH}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text and answer the questions.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>An analyst asked Felipe a simple question: how was the quarter? He did not just read a number. <strong>The top line grew</strong> nine per cent <strong>year on year</strong>, he said, but he did not stop there. <strong>On a like-for-like basis</strong> the growth was closer to five, because part of it came from an acquisition. Gross margin <strong>edged up</strong> a point, <strong>from twenty-one to twenty-two per cent</strong>; new sign-ups <strong>had surged</strong> after the launch, though the trend <strong>plateaued</strong> in December. Costs rose, but higher volumes <strong>largely offset</strong> them, so profit was broadly flat. And then the honest part: one line looked wonderful only because of a tax gain -- <strong>a one-off</strong> -- so <strong>underlying</strong> profit had barely moved. We <strong>outperformed</strong> the sector on revenue, he finished, but cash collection is <strong>lagging</strong> the plan by two weeks. Notice how few of the sentences are just a number. Each one carries a direction, a speed, and a comparison -- that is what tells the analyst what the number actually means.</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. Why does Felipe give the like-for-like figure as well as the headline nine per cent?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Because part of the growth came from an acquisition, so like-for-like shows the real, comparable trend.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Because nine per cent is a mistake and five is the correct number.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because the board only accepts single-digit growth.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. He says the margin "edged up" a point rather than "surged". Why that verb?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because "edged up" and "surged" mean exactly the same thing.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Because the verb has to match the size of the change -- one point is a small, slow move.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because "surged" is never used for margins.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. The profit line looked wonderful. What does Felipe volunteer about it?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> That it proves momentum is accelerating.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> That it was flattered by a one-off tax gain, so underlying profit had barely moved.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> That he cannot explain the number.</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- The Language of Trends and Comparison</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">A number is a photograph; a trend is the film. To describe performance precisely you need three things: a verb that matches the SIZE of the move, a preposition that carries the CHANGE, and a frame that anchors the COMPARISON.</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Tool</th><th style="padding:.7rem;text-align:left">Choices</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Verb (small &rarr; big)</td><td style="padding:.6rem">edged up &middot; rose &middot; climbed &middot; surged</td><td style="padding:.6rem">"Margin edged up; sign-ups surged."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Verb (flat / down)</td><td style="padding:.6rem">plateaued &middot; was broadly flat &middot; dipped &middot; fell</td><td style="padding:.6rem">"Growth plateaued in December."</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Adverb of degree</td><td style="padding:.6rem">marginally &middot; steadily &middot; sharply &middot; significantly</td><td style="padding:.6rem">"Revenue fell marginally, not sharply."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Preposition of change</td><td style="padding:.6rem">up FROM 21 TO 22 &middot; grew BY 9% &middot; now AT 22%</td><td style="padding:.6rem">"Up from twenty-one to twenty-two per cent."</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Comparison frame</td><td style="padding:.6rem">year on year &middot; like-for-like &middot; ahead of / behind plan</td><td style="padding:.6rem">"Up eleven per cent year on year."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Honesty layer</td><td style="padding:.6rem">underlying &middot; a one-off &middot; offset by &middot; broadly flat</td><td style="padding:.6rem">"Underlying profit was broadly flat."</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>The test that never fails:</strong> read your sentence back and ask -- direction, speed, comparison. If a listener still cannot tell which way the number is moving, how fast, and against what, you have given them a photograph, not the film. And always separate the headline from the underlying: a one-off makes a good quarter look better than it is, and the board that trusts you in the good quarter believes you in the bad one.</p>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the correct word. Tap Listen to hear the whole sentence.</p>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"Revenue is up eleven per cent <input class="blank-input" data-answer="year on year" data-hint="Hint: compared with the same period twelve months earlier" data-phrase="Revenue is up eleven per cent year on year." placeholder="___"> ."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"On a <input class="blank-input" data-answer="like-for-like" data-hint="Hint: compared on the same basis, distortion stripped out" data-phrase="On a like-for-like basis, growth is closer to five per cent." placeholder="___"> basis, growth is closer to five per cent."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"The headline looks strong, but <input class="blank-input" data-answer="underlying" data-hint="Hint: the real trend once one-offs are removed" data-phrase="The headline looks strong, but underlying demand is broadly flat." placeholder="___"> demand is broadly flat."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"Gross margin <input class="blank-input" data-answer="edged up" data-hint="Hint: rose slowly, by a small amount" data-phrase="Gross margin edged up from twenty-one to twenty-two per cent." placeholder="___"> from twenty-one to twenty-two per cent."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"Higher costs were largely <input class="blank-input" data-answer="offset" data-hint="Hint: cancelled out by an opposite movement" data-phrase="Higher costs were largely offset by higher volumes." placeholder="___"> by higher volumes."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"That tax gain was a <input class="blank-input" data-answer="one-off" data-hint="Hint: a single item that will not happen again" data-phrase="That tax gain was a one-off; do not build it into next year." placeholder="___"> ; do not build it into next year."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Performance Comment in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the steps of commenting on a result in the right order. Reading out the headline number and stopping there -- with no trend and no comparison -- is the mistake that tells an analyst nothing.</p>
      <div class="order-container" id="order-l13">
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l13')"><span class="order-num">?</span><span class="order-text">Anchor it to a comparison -- year on year and like-for-like.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l13')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l13')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l13')"><span class="order-num">?</span><span class="order-text">State the headline number clearly.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l13')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l13')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l13')"><span class="order-num">?</span><span class="order-text">Close with what the trend means going forward.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l13')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l13')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l13')"><span class="order-num">?</span><span class="order-text">Give the direction and the speed -- up or down, edged up or surged.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l13')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l13')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l13')"><span class="order-num">?</span><span class="order-text">Strip out the one-offs and give the underlying figure.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l13')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l13')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l13')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it. For each one, name the trend tool you are using -- verb of movement, preposition of change, or comparison frame.</p>
      <div class="speech-card" data-phrase="The top line grew nine per cent year on year.">
        <div class="speech-phrase">The top line grew nine per cent year on year.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="On a like-for-like basis, growth is closer to five per cent.">
        <div class="speech-phrase">On a like-for-like basis, growth is closer to five per cent.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="Gross margin edged up from twenty-one to twenty-two per cent.">
        <div class="speech-phrase">Gross margin edged up from twenty-one to twenty-two per cent.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="Underlying profit was broadly flat once we strip out the one-off.">
        <div class="speech-phrase">Underlying profit was broadly flat once we strip out the one-off.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="We outperformed the sector on revenue, but cash collection is lagging the plan.">
        <div class="speech-phrase">We outperformed the sector on revenue, but cash collection is lagging the plan.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best way to describe each movement in a results review.</p>
      <div class="quiz-item"><div class="quiz-question">Margin moved from 21% to 22% -- a single point. The precise verb is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Margin surged from twenty-one to twenty-two per cent."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Margin edged up from twenty-one to twenty-two per cent."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Margin plateaued from twenty-one to twenty-two per cent."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">Revenue rose 9%, but part of it came from an acquisition. The honest line is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "Up nine per cent, but on a like-for-like basis closer to five."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Up nine per cent, and that is the whole story."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Revenue is ninety million."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">Profit beat the plan only because of a tax gain that will not repeat. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Profit surged -- real momentum."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "The beat is a one-off; underlying profit was broadly flat."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Profit is up, no caveats."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">Costs rose, but higher volumes cancelled the effect. The net comment is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Costs surged and profit collapsed."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Higher costs were largely offset by higher volumes, so profit was broadly flat."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Costs rose and that is all I can say."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">Growth was strong for three quarters, then stopped in the fourth. You describe it as:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "Growth outperformed plan for three quarters, then plateaued in the fourth."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Growth is fine."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Growth surged all year."</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the prompt below. There is no right or wrong answer -- speak for 2 to 3 minutes, without a script.</p>
      <div class="think-card">
        <div class="think-question">An analyst asks you to walk them through last quarter's performance. Speak for 2-3 minutes. Do not read numbers naked: for each figure, give a direction and a speed (use a verb sized to the move -- edged up, surged, plateaued), a preposition of change (up from... to..., by, at), and a comparison frame (year on year, like-for-like, ahead of or behind plan). Then separate one headline from its underlying figure, and name any one-off honestly. Finish with what the momentum means for the next quarter.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-13"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 13</h4>
      <div class="survival-phrase"><span class="sp-num">1</span><span class="sp-en">The top line grew nine per cent year on year.</span><button class="btn btn-listen" data-speak="The top line grew nine per cent year on year." onclick="speakText(this.dataset.speak,this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">2</span><span class="sp-en">On a like-for-like basis, growth is closer to five per cent.</span><button class="btn btn-listen" data-speak="On a like-for-like basis, growth is closer to five per cent." onclick="speakText(this.dataset.speak,this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">3</span><span class="sp-en">Gross margin edged up from twenty-one to twenty-two per cent.</span><button class="btn btn-listen" data-speak="Gross margin edged up from twenty-one to twenty-two per cent." onclick="speakText(this.dataset.speak,this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">4</span><span class="sp-en">The beat is a one-off; underlying profit was broadly flat.</span><button class="btn btn-listen" data-speak="The beat is a one-off; underlying profit was broadly flat." onclick="speakText(this.dataset.speak,this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">5</span><span class="sp-en">We outperformed the sector, but cash collection is lagging the plan.</span><button class="btn btn-listen" data-speak="We outperformed the sector, but cash collection is lagging the plan." onclick="speakText(this.dataset.speak,this)">&#9835;</button></div>
    </div>

  </div>
</div>
'''

out = TEMPLATE.replace("{VOCAB}", vocab_cards()).replace("{MATCH}", match_rows())
with open("_build/felipe-pimenta-aula13/preclass.html", "w", encoding="utf-8") as f:
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
