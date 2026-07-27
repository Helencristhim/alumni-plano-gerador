# -*- coding: utf-8 -*-
"""Gera preclass.html da aula 16 (B2, ZERO portugues na tela do aluno).

REGRA 29: este bloco PREVIEWA a aula 16 IN CLASS -- mesmo titulo, mesmo vocab
(as 12 expressoes de distancia) e mesma gramatica (future perfect / future
perfect continuous).
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))

WORDS = [
    ("A baseline", "the first measurement, the one that everything later is compared with",
     "\"We recorded a baseline on the first evening and nobody has listened to it since.\""),
    ("A benchmark", "a standard from outside that you measure yourself against",
     "\"The benchmark is not a native speaker; it is the man who answered that first call.\""),
    ("To take stock", "to stop and look honestly at where you are",
     "\"Before the next move, take stock of what has actually changed.\""),
    ("Second nature", "so familiar to you that it happens without any thinking",
     "\"Opening a meeting in English is second nature to him now.\""),
    ("Muscle memory", "a skill that the body repeats on its own after enough practice",
     "\"Fluency is mostly muscle memory; the phrases arrive before you choose them.\""),
    ("Off the cuff", "with no preparation and with no notes in front of you",
     "\"She asked something nobody expected and he answered off the cuff.\""),
    ("To hold your own", "to perform as well as everyone else in a demanding room",
     "\"I hold my own in a meeting; a crowded call on a bad line is still work.\""),
    ("A stepping stone", "something that carries you to the next stage of a journey",
     "\"That first screening call was a stepping stone, not the destination.\""),
    ("Incremental", "growing in small steps rather than in one visible jump",
     "\"The gain was incremental, which is why he could not feel it week by week.\""),
    ("To fall back on", "to use as support at the moment when everything else fails",
     "\"When the line breaks, he falls back on three phrases that always work.\""),
    ("A blind spot", "a weakness in yourself that you are not able to see",
     "\"Everybody has a blind spot; his was asking for a question to be repeated.\""),
    ("To come a long way", "to have made great progress from where you started",
     "\"You have come a long way from the man who sat silent at Aqua Capital.\""),
]

VOL = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
       '<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/>'
       '<path d="M15.54 8.46a5 5 0 010 7.07"/></svg>')


def vocab_cards():
    out = []
    for w, d, ex in WORDS:
        out.append(
            f'        <div class="vocab-card-pc"><div class="vocab-card-content">'
            f'<div class="vocab-card-header"><span class="vocab-card-word">{w}</span>'
            f'<span class="vocab-card-dot"> -- </span><span class="vocab-card-def">{d}</span></div>'
            f'<div class="vocab-card-example">{ex}</div></div>'
            f'<button class="audio-btn" data-speak="{w}" '
            f'onclick="speakText(this.dataset.speak,this)">{VOL} Listen</button></div>')
    return "\n".join(out)


def match_rows():
    """REGRA 24: as opcoes NUNCA saem na mesma ordem das palavras."""
    defs = [d for _, d, _ in WORDS]
    out = []
    for i, (w, d, _) in enumerate(WORDS):
        rot = defs[i + 5:] + defs[:i + 5]
        opts = list(reversed(rot))
        if opts[i % len(opts)] == d:
            opts = opts[1:] + opts[:1]
        options = "".join(f'<option value="{o}">{o}</option>' for o in opts)
        out.append(
            f'        <div class="match-row" data-answer="{d}">'
            f'<span class="match-word" style="flex:0 0 150px">{w}</span>'
            f'<select style="flex:1;width:100%" onchange="checkMatch(this)">'
            f'<option value="">Select...</option>{options}</select></div>')
    return "\n".join(out)


TEMPLATE = '''<div class="lesson-card" id="ex-lesson-16">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 16 -- Pre-class</div>
      <h3>Milestone Review -- From Aqua Capital Silence to CFO Fluency</h3>
      <div class="lesson-desc">The last lesson of the program. You go back to the three minutes you recorded on the very first evening and find out what they were actually measuring. Key words: a baseline, a benchmark, to take stock, second nature, muscle memory, off the cuff, to hold your own, a stepping stone, incremental, to fall back on, a blind spot, to come a long way. Structure: the future perfect and the future perfect continuous -- standing at a deadline and looking back at what will already be done by then.</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="16" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="16">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each expression and read the example. These are the words for something you have never had to describe in English: your own progress.</p>
      <div class="vocab-cards">
{VOCAB}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each expression with its correct definition.</p>
      <div class="match-grid" id="match-l16">
{MATCH}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text and answer the questions.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>On the first evening of the program he recorded three minutes about himself and never played the file back. It was, by his own account, painful. What he did not understand at the time was that the recording was not a verdict on him; it was a <strong>baseline</strong>. A year later the same man opened the same file and could not finish it, and the strangest part, he says, was hearing how hard he once had to work for sentences that are now <strong>second nature</strong>. Nothing turned in a single week. The gain was <strong>incremental</strong>, which is exactly why he could not feel it while it was happening. His <strong>blind spot</strong> was never grammar. It was the half-second of silence he used to fill with an apology, and which he now fills with a line he can <strong>fall back on</strong>. Ask him where he is going next and the answer arrives in a different tense altogether. <strong>By this time next year he will have been leading in English for eighteen months</strong>, and <strong>by the time the next audit committee meets he will have presented four sets of results</strong> in the language that used to be the reason he stayed quiet. That is not fluency arriving one morning. That is a <strong>benchmark</strong> moving.</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. Why could he not feel the progress while it was happening?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Because he was not paying attention to his own English.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Because the gain was incremental, and nothing changed in a single week.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Because he never recorded himself more than once.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. In "by the time the next audit committee meets", why is the verb "meets" and not "will meet"?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> A clause after "by the time" stays in the present; the main verb already carries the future.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> The committee meeting is a habit, so it takes the present simple.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Both forms are correct; the writer chose the shorter one.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. What does the text say his real weakness was?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Grammar, which is why he had to record himself twice.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Vocabulary, which ran out exactly where the interesting part began.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> The half-second of silence he used to fill with an apology.</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- The Future Perfect</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">In Lesson 1 you learned to stand here and look back: the present perfect. This is its mirror. You stand at a point in the future and look back from there at what is already done by then. It is the tense of a commitment, which is why boards and head-hunters hear it as seniority.</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Form</th><th style="padding:.7rem;text-align:left">Use</th><th style="padding:.7rem;text-align:left">Example</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">will have + past participle</td><td style="padding:.6rem">finished before a future point</td><td style="padding:.6rem">"By Friday I will have signed it."</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">will have been + -ing</td><td style="padding:.6rem">still running at that point, seen as a length</td><td style="padding:.6rem">"By June I will have been leading the team for two years."</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">by + a future point</td><td style="padding:.6rem">the deadline the sentence looks back from</td><td style="padding:.6rem">"by then &middot; by 2027 &middot; by the fourteenth"</td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">by the time + present tense</td><td style="padding:.6rem">the deadline clause never takes will</td><td style="padding:.6rem">"By the time they ask, I will have prepared it."</td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">present perfect vs future perfect</td><td style="padding:.6rem">looking back from now, or from later</td><td style="padding:.6rem">"I have led it for six months. / By June I will have led it for a year."</td></tr>
        </tbody>
      </table></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem"><strong>Two questions decide the form.</strong> Is the action finished at that future point, or still running? Finished takes <strong>will have done</strong>; still running takes <strong>will have been doing</strong>. And where is the deadline? If the deadline is a clause, it stays in the present: <strong>by the time they ask</strong>, never "by the time they will ask". One last trap: <strong>until</strong> is the whole stretch of time before a moment, <strong>by</strong> is the deadline itself.</p>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the correct word. Tap Listen to hear the whole sentence.</p>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"We recorded a <input class="blank-input" data-answer="baseline" data-hint="Hint: the first measurement, the one everything later is compared with" data-phrase="We recorded a baseline on the first evening and nobody has listened to it since." placeholder="___"> on the first evening and nobody has listened to it since."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"By the time the board <input class="blank-input" data-answer="meets" data-hint="Hint: after by the time, the clause stays in the present" data-phrase="By the time the board meets, I will have presented these numbers four times." placeholder="___">, I will have presented these numbers four times."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"By December I <input class="blank-input" data-answer="will have" data-hint="Hint: two words -- the future perfect continuous needs both" data-phrase="By December I will have been leading this team for two years." placeholder="___"> been leading this team for two years."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"Opening a meeting in English is <input class="blank-input" data-answer="second nature" data-hint="Hint: so familiar that it happens without any thinking" data-phrase="Opening a meeting in English is second nature to him now." placeholder="___"> to him now."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"I don't know that <input class="blank-input" data-answer="off the cuff" data-hint="Hint: with no preparation and no notes" data-phrase="I don't know that off the cuff, but I'll have an answer by Friday." placeholder="___">, but I'll have an answer by Friday."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"Everybody has a <input class="blank-input" data-answer="blind spot" data-hint="Hint: a weakness in yourself that you cannot see" data-phrase="Everybody has a blind spot; his was asking for a question to be repeated." placeholder="___">; his was asking for a question to be repeated."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: The Anatomy of a Milestone Answer</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Someone senior asks where your English is now. Put the five moves of a strong answer in the right order. Stopping after the good news is what makes an answer sound rehearsed.</p>
      <div class="order-container" id="order-l16">
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l16')"><span class="order-num">?</span><span class="order-text">Name the one thing that is still work -- the blind spot.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l16')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l16')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l16')"><span class="order-num">?</span><span class="order-text">Hand the question back -- ask what they need to see.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l16')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l16')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l16')"><span class="order-num">?</span><span class="order-text">Say where you started, in one line and without drama.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l16')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l16')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l16')"><span class="order-num">?</span><span class="order-text">Commit to the next deadline: by then I will have done it.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l16')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l16')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l16')"><span class="order-num">?</span><span class="order-text">Say what changed, and give the evidence for it.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l16')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l16')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l16')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it. Keep "I'll have" as one quick sound -- the full "I will have" is what makes a commitment sound like a rehearsal.</p>
      <div class="speech-card" data-phrase="I've come a long way, though I'd stop short of calling it finished.">
        <div class="speech-phrase">I've come a long way, though I'd stop short of calling it finished.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="By the fourteenth I'll have presented these numbers four times.">
        <div class="speech-phrase">By the fourteenth I'll have presented these numbers four times.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="I hold my own in a meeting; a crowded call is still work.">
        <div class="speech-phrase">I hold my own in a meeting; a crowded call is still work.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="I don't know that off the cuff, but I'll have an answer by Friday.">
        <div class="speech-phrase">I don't know that off the cuff, but I'll have an answer by Friday.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="Sorry, I lost you there. Could you give me that last part again?">
        <div class="speech-phrase">Sorry, I lost you there. Could you give me that last part again?</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the answer a board would read as seniority.</p>
      <div class="quiz-item"><div class="quiz-question">A head-hunter asks whether you will be ready for the board on the fourteenth:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Yes, I think so."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "By the fourteenth I'll have presented these numbers four times, so yes."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "By the fourteenth I will present these numbers four times, so yes."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You want to name Friday as the deadline you are looking back from:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Until Friday I will have signed the contract."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "By Friday I will have signed the contract."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "On Friday I will have been signing the contract."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">The action is still running at that future point. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "By June I will have been leading this team for two years."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "By June I will have led this team since two years."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "By June I am leading this team for two years."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">A recruiter asks where your English still needs work. The answer that reads as seniority is:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "My English is perfect now, there is nothing left."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "I hold my own in a meeting; a crowded call on a bad line is still work."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I am sorry, my English is not so good."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">Someone asks you for a figure you do not have in your head:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "I don't know that off the cuff, but I'll have an answer by Friday."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Sorry, my English is not good enough for that question."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I will try to know it until Friday."</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the prompt below. There is no right or wrong answer -- speak for 2 to 3 minutes, without a script. Do not listen to your Lesson 1 recording first. Record this one blind, and compare afterwards.</p>
      <div class="think-card">
        <div class="think-question">Sixteen lessons on, the same task, word for word. A headhunter opens the call: "Tell me about yourself and why you're interested in an international role." Introduce yourself: your current role, how long you've been in finance, the finished chapters of your career, and what you're looking for now. Then add the one thing you could not have said in Lesson 1: what will already be true by this time next year. Take your time and don't read from a script.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-16"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 16</h4>
      <div class="survival-phrase"><span class="sp-num">1</span><span class="sp-en">I've come a long way, though I'd stop short of calling it finished.</span><button class="btn btn-listen" data-speak="I've come a long way, though I'd stop short of calling it finished." onclick="speakText(this.dataset.speak,this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">2</span><span class="sp-en">By the fourteenth I'll have presented these numbers four times.</span><button class="btn btn-listen" data-speak="By the fourteenth I'll have presented these numbers four times." onclick="speakText(this.dataset.speak,this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">3</span><span class="sp-en">I hold my own in a meeting; a crowded call is still work.</span><button class="btn btn-listen" data-speak="I hold my own in a meeting; a crowded call is still work." onclick="speakText(this.dataset.speak,this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">4</span><span class="sp-en">I don't know that off the cuff, but I'll have an answer by Friday.</span><button class="btn btn-listen" data-speak="I don't know that off the cuff, but I'll have an answer by Friday." onclick="speakText(this.dataset.speak,this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">5</span><span class="sp-en">Sorry, I lost you there. Could you give me that last part again?</span><button class="btn btn-listen" data-speak="Sorry, I lost you there. Could you give me that last part again?" onclick="speakText(this.dataset.speak,this)">&#9835;</button></div>
    </div>

  </div>
</div>
'''

out = TEMPLATE.replace("{VOCAB}", vocab_cards()).replace("{MATCH}", match_rows())
with open(os.path.join(HERE, "preclass.html"), "w", encoding="utf-8") as f:
    f.write(out)

rows = re.findall(r'<div class="match-row" data-answer="([^"]+)">(.*?)</select>', out, re.S)
bad = 0
for ans, body in rows:
    opts = re.findall(r'<option value="([^"]*)">', body)
    if ans not in opts:
        bad += 1
        print("MISSING option for answer:", ans)
same = 0
for i, (ans, body) in enumerate(rows):
    opts = [o for o in re.findall(r'<option value="([^"]*)">', body) if o]
    if opts and opts[i] == ans:
        same += 1
print("preclass.html written; words:", len(WORDS), "| match rows:", len(rows),
      "| missing:", bad, "| answer-in-same-position:", same)
assert bad == 0
