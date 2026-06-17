#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Milton Aula 10 - Supply Chain (Passive Voice). Scaffold = aula7.
Auto-derives audioMap + phrases.json (REGRA 7)."""
import os, re, json
ROOT='/home/dan/dev/work/better/wt-milton'
SRC=os.path.join(ROOT,'public/professor/milton-sayegh-aula7.html')
OUT=os.path.join(ROOT,'public/professor/milton-sayegh-aula10.html')
PHR=os.path.join(os.path.dirname(os.path.abspath(__file__)),'phrases.json')
LESSON=10
COVER="https://images.unsplash.com/photo-1494412574643-ff11b0a5c1c3"
IMG=COVER
ELLEN={
    "Of course. The products are made here in Brazil and then packed in our warehouse.",
    "The containers are sent by sea. Last month, the shipment was delivered in twenty days.",
    "Yes. All the cargo was inspected and released without problems.",
    "The order was shipped last Friday.",
    "The cargo was inspected at customs.",
}
def fname(t):
    s=t.lower().replace("'","");s=re.sub(r"[^a-z0-9]+","_",s).strip("_");return s[:60].rstrip("_")+".mp3"

PRECLASS='''<div class="tab-content" id="tab-exercises">

<div class="lesson-card open" id="ex-lesson-10">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('%(img)s?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Aula 10 - Pre-class</div>
      <h3>Supply Chain</h3>
      <div class="lesson-desc">From Brazil to the U.S. - the Passive Voice</div>
      <div class="lesson-progress-mini">
        <div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="10" style="width:0%%"></div></div>
        <span class="mini-percent" data-lesson-pct="10">0%%</span>
      </div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <span class="badge badge-vocab">Vocabulary</span>
      <h3>Stage 1.1: Supply Chain &amp; Logistics Vocabulary</h3>
      <p>Click on each card to listen and learn. These 8 words describe how products move from Brazil to the U.S.</p>
      <div class="vocab-grid">
        <div class="vocab-card"><h4>Supply Chain</h4><div class="vocab-def">The full process from production to final delivery.</div><div class="vocab-ex">"Our <strong>supply chain</strong> starts in Brazil."</div><button class="audio-btn" onclick="speakText('Supply Chain',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
        <div class="vocab-card"><h4>Shipment</h4><div class="vocab-def">A load of goods sent together.</div><div class="vocab-ex">"The <strong>shipment</strong> was delivered in twenty days."</div><button class="audio-btn" onclick="speakText('Shipment',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
        <div class="vocab-card"><h4>Customs</h4><div class="vocab-def">The government office that checks imported goods.</div><div class="vocab-ex">"All cargo is inspected at <strong>customs</strong>."</div><button class="audio-btn" onclick="speakText('Customs',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
        <div class="vocab-card"><h4>Freight</h4><div class="vocab-def">Goods transported in bulk, or the cost of transport.</div><div class="vocab-ex">"<strong>Freight</strong> by sea is cheaper than by air."</div><button class="audio-btn" onclick="speakText('Freight',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
        <div class="vocab-card"><h4>Warehouse</h4><div class="vocab-def">A large building where goods are stored.</div><div class="vocab-ex">"The products are packed in our <strong>warehouse</strong>."</div><button class="audio-btn" onclick="speakText('Warehouse',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
        <div class="vocab-card"><h4>Cargo</h4><div class="vocab-def">Goods carried by ship, plane, or truck.</div><div class="vocab-ex">"The <strong>cargo</strong> was inspected at customs."</div><button class="audio-btn" onclick="speakText('Cargo',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
        <div class="vocab-card"><h4>Logistics</h4><div class="vocab-def">The organization of moving and storing goods.</div><div class="vocab-ex">"Our <strong>logistics</strong> team manages every shipment."</div><button class="audio-btn" onclick="speakText('Logistics',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
        <div class="vocab-card"><h4>Container</h4><div class="vocab-def">A large metal box used for shipping goods.</div><div class="vocab-ex">"The <strong>containers</strong> are sent by sea."</div><button class="audio-btn" onclick="speakText('Container',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
      </div>
    </div>

    <div class="exercise-section">
      <span class="badge badge-practice">Practice</span>
      <h3>Stage 1.2: Match the Words</h3>
      <p>Match each word to its definition.</p>
      <div class="match-grid" id="match-l10">
        <div class="match-row" data-answer="goods sent together"><span class="match-word">Shipment</span><select onchange="checkMatch(this)"><option value="">Select...</option><option value="a building for storing goods">a building for storing goods</option><option value="goods sent together">goods sent together</option><option value="goods carried by ship or truck">goods carried by ship or truck</option><option value="where imports are checked">where imports are checked</option><option value="a metal box for shipping">a metal box for shipping</option></select></div>
        <div class="match-row" data-answer="where imports are checked"><span class="match-word">Customs</span><select onchange="checkMatch(this)"><option value="">Select...</option><option value="goods carried by ship or truck">goods carried by ship or truck</option><option value="where imports are checked">where imports are checked</option><option value="goods sent together">goods sent together</option><option value="a metal box for shipping">a metal box for shipping</option><option value="a building for storing goods">a building for storing goods</option></select></div>
        <div class="match-row" data-answer="a building for storing goods"><span class="match-word">Warehouse</span><select onchange="checkMatch(this)"><option value="">Select...</option><option value="a metal box for shipping">a metal box for shipping</option><option value="a building for storing goods">a building for storing goods</option><option value="where imports are checked">where imports are checked</option><option value="goods sent together">goods sent together</option><option value="goods carried by ship or truck">goods carried by ship or truck</option></select></div>
        <div class="match-row" data-answer="goods carried by ship or truck"><span class="match-word">Cargo</span><select onchange="checkMatch(this)"><option value="">Select...</option><option value="goods sent together">goods sent together</option><option value="goods carried by ship or truck">goods carried by ship or truck</option><option value="a building for storing goods">a building for storing goods</option><option value="a metal box for shipping">a metal box for shipping</option><option value="where imports are checked">where imports are checked</option></select></div>
        <div class="match-row" data-answer="a metal box for shipping"><span class="match-word">Container</span><select onchange="checkMatch(this)"><option value="">Select...</option><option value="where imports are checked">where imports are checked</option><option value="a metal box for shipping">a metal box for shipping</option><option value="goods carried by ship or truck">goods carried by ship or truck</option><option value="a building for storing goods">a building for storing goods</option><option value="goods sent together">goods sent together</option></select></div>
      </div>
      <button class="verify-all-btn" onclick="verifyAllMatches('match-l10')">Check Answers</button>
    </div>

    <div class="exercise-section">
      <span class="badge badge-grammar">Grammar</span>
      <h3>Stage 1.3: Grammar in Context</h3>
      <p>Read the text and answer the questions. Notice the Passive Voice (be + past participle).</p>
      <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:8px;padding:1.2rem;margin-bottom:1rem;font-size:.88rem;line-height:1.7;color:var(--text)">
        At Sayegh Jewelry, every piece <strong>is made</strong> by hand in Brazil. First, the products <strong>are designed</strong> in Sao Paulo. Then they <strong>are packed</strong> carefully in the warehouse. The containers <strong>are sent</strong> by sea to the United States. Last month, a large shipment <strong>was delivered</strong> in only twenty days. When the cargo arrived, it <strong>was inspected</strong> at customs and quickly <strong>released</strong>. The whole supply chain <strong>is managed</strong> by an experienced logistics team. Thanks to this process, the jewelry <strong>is exported</strong> to clients across America.
      </div>
      <div class="quiz-item"><div class="quiz-question">1. Where is the jewelry made?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> In Brazil</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> In the United States</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> In Europe</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. How are the containers sent?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> By sea</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> By air</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> By road</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. What happened to the cargo at customs?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> It was inspected and released</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> It was returned to Brazil</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> It was lost</div></div></div>
    </div>

    <div class="exercise-section">
      <span class="badge badge-grammar">Grammar</span>
      <h3>Stage 1.4: Grammar Tip - The Passive Voice</h3>
      <p>Use the Passive Voice when the action (or the product) is more important than who does it.</p>
      <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:8px;padding:1.2rem;margin-bottom:1rem">
        <table class="curriculum-table" style="margin:0">
          <thead><tr><th>Form</th><th>Structure</th><th>Example</th></tr></thead>
          <tbody>
            <tr><td><strong>Present passive</strong></td><td>am/is/are + past participle</td><td>"The jewelry <strong>is made</strong> in Brazil."</td></tr>
            <tr><td><strong>Past passive</strong></td><td>was/were + past participle</td><td>"The order <strong>was shipped</strong> last week."</td></tr>
            <tr><td><strong>With the agent</strong></td><td>... + <strong>by</strong> + who/what</td><td>"It <strong>is managed by</strong> our team."</td></tr>
            <tr><td><strong>Question</strong></td><td>be + subject + past participle</td><td>"<strong>Was</strong> the cargo <strong>inspected</strong>?"</td></tr>
          </tbody>
        </table>
        <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem;font-style:italic">Always use the PAST PARTICIPLE after "be": made, sent, shipped, inspected. "by + agent" is optional - often we don't say who did the action.</p>
      </div>
    </div>

    <div class="exercise-section">
      <span class="badge badge-practice">Practice</span>
      <h3>Stage 1.5: Complete the Sentences</h3>
      <p>Fill in with the correct Passive Voice form.</p>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"Our jewelry <input class="blank-input" data-answer="is made" data-hint="Hint: present passive (is + past participle), 2 words" data-phrase="Our jewelry is made in Brazil." placeholder="___"> in Brazil."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button> <button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"The order <input class="blank-input" data-answer="was shipped" data-hint="Hint: past passive (was + past participle), 2 words" data-phrase="The order was shipped last week." placeholder="___"> last week."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button> <button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"Our products <input class="blank-input" data-answer="are exported" data-hint="Hint: present passive plural (are + past participle), 2 words" data-phrase="Our products are exported to the United States." placeholder="___"> to the United States."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button> <button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"The cargo <input class="blank-input" data-answer="was checked" data-hint="Hint: past passive (was + past participle), 2 words" data-phrase="The cargo was checked at customs." placeholder="___"> at customs."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button> <button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"The containers <input class="blank-input" data-answer="are sent" data-hint="Hint: present passive plural (are + past participle), 2 words" data-phrase="The containers are sent by sea." placeholder="___"> by sea."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button> <button class="check-btn" onclick="checkBlank(this)">Check</button></div>
    </div>

    <div class="exercise-section">
      <span class="badge badge-order">Order</span>
      <h3>Stage 2: The Journey of a Shipment</h3>
      <p>Arrange the supply chain steps in the correct order.</p>
      <div class="order-container" id="order-l10">
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l10')"><span class="order-num">?</span><span class="order-text">"The containers are sent by sea."</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l10')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l10')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l10')"><span class="order-num">?</span><span class="order-text">"The jewelry is made in Brazil."</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l10')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l10')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l10')"><span class="order-num">?</span><span class="order-text">"The cargo is inspected at customs."</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l10')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l10')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l10')"><span class="order-num">?</span><span class="order-text">"The products are packed in the warehouse."</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l10')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l10')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l10')"><span class="order-num">?</span><span class="order-text">"The shipment is delivered to the U.S."</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l10')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l10')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l10')">Check Order</button>
    </div>

    <div class="exercise-section">
      <span class="badge badge-speak">Speaking</span>
      <h3>Stage 3: Pronunciation Practice</h3>
      <p>Listen to each phrase, then record yourself. Notice the Passive Voice.</p>
      <div class="speech-card" data-phrase="Our products are made in Brazil."><div class="speech-phrase">"Our products are made in Brazil."</div><div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Stop</button></div><div class="speech-result"></div></div>
      <div class="speech-card" data-phrase="The jewelry is exported to the United States."><div class="speech-phrase">"The jewelry is exported to the United States."</div><div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Stop</button></div><div class="speech-result"></div></div>
      <div class="speech-card" data-phrase="The shipment was sent last week."><div class="speech-phrase">"The shipment was sent last week."</div><div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Stop</button></div><div class="speech-result"></div></div>
      <div class="speech-card" data-phrase="The containers are transported by sea."><div class="speech-phrase">"The containers are transported by sea."</div><div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Stop</button></div><div class="speech-result"></div></div>
      <div class="speech-card" data-phrase="Was the cargo checked at customs?"><div class="speech-phrase">"Was the cargo checked at customs?"</div><div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Stop</button></div><div class="speech-result"></div></div>
    </div>

    <div class="exercise-section">
      <span class="badge badge-quiz">Quiz</span>
      <h3>Stage 4: Situational Quiz</h3>
      <p>Choose the best option for each situation.</p>
      <div class="quiz-item"><div class="quiz-question">1. You explain where the products are produced. Which is correct?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "The jewelry is made in Brazil."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "The jewelry is make in Brazil."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "The jewelry makes in Brazil."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. You say the order was sent in the past. Which is correct?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "The order was shipped yesterday."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "The order is shipped yesterday."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "The order was ship yesterday."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. You ask if the cargo was checked (past passive question). Which is correct?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "Was the cargo inspected at customs?"</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Did the cargo inspected at customs?"</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Was the cargo inspect at customs?"</div></div></div>
      <div class="quiz-item"><div class="quiz-question">4. You describe who manages the process (with the agent). Which is correct?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "The supply chain is managed by our logistics team."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "The supply chain is manage by our team."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "The supply chain manages by our team."</div></div></div>
    </div>

    <div class="exercise-section">
      <span class="badge badge-think">Reflection</span>
      <h3>Stage 5: Free Production</h3>
      <p>Record yourself speaking freely.</p>
      <div class="think-card">
        <div class="think-question">Describe your company's supply chain, from production to delivery. Use the Passive Voice: where the products are made, how they are packed, how the cargo is shipped, and what happens at customs. Use at least four passive sentences.</div>
        <div class="speech-controls">
          <button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Free Record</button>
          <button class="btn btn-stop" onclick="stopFreeRecording(this)">&#9632; Stop</button>
        </div>
        <div id="think-result-10"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card - Lesson 10</h4>
      <div class="survival-phrase"><span class="sp-num">1</span><span class="sp-en">Our products are made in Brazil.</span><button class="btn btn-listen" onclick="speakText('Our products are made in Brazil.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">2</span><span class="sp-en">The shipment was sent last week.</span><button class="btn btn-listen" onclick="speakText('The shipment was sent last week.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">3</span><span class="sp-en">How is the cargo transported?</span><button class="btn btn-listen" onclick="speakText('How is the cargo transported?',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">4</span><span class="sp-en">The shipment is delivered in twenty days.</span><button class="btn btn-listen" onclick="speakText('The shipment is delivered in twenty days.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">5</span><span class="sp-en">Everything was checked at customs.</span><button class="btn btn-listen" onclick="speakText('Everything was checked at customs.',this)">&#9835;</button></div>
    </div>

    <div style="margin-top:1.5rem;">
      <h4 style="font-family:'Cormorant Garamond',serif;font-size:1rem;color:var(--accent);margin-bottom:0.8rem;">Checklist - Aula 10</h4>
      <ul class="checklist" id="checklist-10">
        <li><input type="checkbox" onchange="toggleChecklist(this)"> I studied the 8 supply chain words</li>
        <li><input type="checkbox" onchange="toggleChecklist(this)"> I completed the matching exercise</li>
        <li><input type="checkbox" onchange="toggleChecklist(this)"> I read the Grammar in Context text</li>
        <li><input type="checkbox" onchange="toggleChecklist(this)"> I reviewed the Grammar Tip (Passive Voice)</li>
        <li><input type="checkbox" onchange="toggleChecklist(this)"> I completed the fill-in-the-blanks</li>
        <li><input type="checkbox" onchange="toggleChecklist(this)"> I ordered the supply chain steps</li>
        <li><input type="checkbox" onchange="toggleChecklist(this)"> I practiced pronunciation (5 phrases)</li>
        <li><input type="checkbox" onchange="toggleChecklist(this)"> I answered the situational quiz</li>
        <li><input type="checkbox" onchange="toggleChecklist(this)"> I recorded the free production</li>
      </ul>
    </div>

  </div><!-- /lesson-body -->
</div><!-- /lesson-card -->

</div><!-- /tab-exercises -->''' % {"img": IMG}

INCLASS_MENU='''<div class="tab-content" id="tab-inclass">
<h3 style="font-family:'Cormorant Garamond',serif;margin-bottom:1rem;color:var(--text)">IN CLASS — Select Lesson</h3>
<div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" onclick="enterSlideMode();" onmouseover="this.style.borderColor='var(--accent)'" onmouseout="this.style.borderColor='rgba(200,200,190,.5)'">
  <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">10</div>
  <div><div style="font-weight:600;font-size:.95rem">Supply Chain</div><div style="font-size:.8rem;color:var(--text-dim)">From Brazil to the U.S. - the Passive Voice — 32 slides</div></div>
</div>
</div>'''

COMPLEMENTARY='''<div class="tab-content" id="tab-complementary">
<h3 style="font-family:'Cormorant Garamond',serif;margin-bottom:.5rem;color:var(--text)">Complementary Materials - Lesson 10</h3>
<p style="font-size:.82rem;color:var(--text-dim);margin-bottom:1rem">Topic: Supply Chain and logistics. Notice how processes are described with the Passive Voice (is made, are shipped, was delivered).</p>
<div class="media-grid">
  <div class="media-card-wrapper" data-media="l10-series">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb"><svg viewBox="0 0 24 24"><rect x="2" y="2" width="20" height="20" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><polygon points="10 8 16 12 10 16 10 8" fill="currentColor"/></svg></div>
      <div class="media-info">
        <div class="media-type">Documentary</div>
        <h5>How It's Made - Jewelry / Manufacturing episodes</h5>
        <p>This show explains how products are made, packed and shipped - narrated almost entirely in the Passive Voice: "the metal is heated", "the pieces are polished", "the items are packed". Exactly the structure of this lesson.</p>
        <p class="media-tip">Tip: Watch with English subtitles. Write down 8 passive sentences (is/are + past participle) you hear.</p>
      </div>
    </div>
  </div>
  <div class="media-card-wrapper" data-media="l10-podcast">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" fill="none" stroke="currentColor" stroke-width="2"/><polygon points="10 8 16 12 10 16 10 8" fill="currentColor"/></svg></div>
      <div class="media-info">
        <div class="media-type">Podcast</div>
        <h5>Business English Pod - Describing a Process &amp; Supply Chains</h5>
        <p>Teaches the language of operations and logistics: how goods are produced, shipped and delivered, using the Passive Voice throughout. Perfect for describing your own supply chain.</p>
        <p class="media-tip">Tip: Listen twice. The second time, pause and repeat each passive sentence out loud.</p>
        <a href="https://open.spotify.com/show/4nCHpl7GXuMu41Jn4xDLtH" target="_blank" rel="noopener" style="display:inline-block;margin-top:.5rem;font-size:.75rem;color:var(--accent);font-weight:600;text-decoration:none;border-bottom:1px solid var(--accent)">Listen on Spotify &#8599;</a>
      </div>
    </div>
  </div>
  <div class="media-card-wrapper" data-media="l10-youtube">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb"><svg viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3" fill="currentColor"/></svg></div>
      <div class="media-info">
        <div class="media-type">YouTube</div>
        <h5>Business English B1+ | Company Roles &amp; Passive Voice Practice</h5>
        <p>A B1+ Business English lesson on the Passive Voice with company and operations examples - the same level and structures you need to describe your supply chain.</p>
        <p class="media-tip">Tip: Watch with English subtitles. After the lesson, describe one step of your supply chain in the passive.</p>
        <a href="https://www.youtube.com/watch?v=c7R7JhU_sNs" target="_blank" rel="noopener" style="display:inline-block;margin-top:.5rem;font-size:.75rem;color:var(--accent);font-weight:600;text-decoration:none;border-bottom:1px solid var(--accent)">Watch on YouTube &#8599;</a>
      </div>
    </div>
  </div>
</div>
</div>

</div><!-- /container -->'''

def slide(n,phase,cls,teacher,inner,style=""):
    st=(' style="%s"'%style) if style else ""
    return ('<div class="slide %s" data-slide="%d" data-phase="%d" data-lesson="%d" data-teacher="%s"%s>\n  <div class="slide-inner">\n%s\n  </div>\n</div>\n'%(cls,n,phase,LESSON,teacher,st,inner))
def img_slide(n,phase,teacher,label,title,sub,imgurl):
    subp=('<p style="color:rgba(255,255,255,.6);font-size:1rem;margin-top:1rem">%s</p>'%sub) if sub else ""
    inner='    <div class="chapter-label">%s</div>\n    <h2 class="slide-title">%s</h2>\n    %s'%(label,title,subp)
    return ('<div class="slide slide-image" data-slide="%d" data-phase="%d" data-lesson="%d" data-teacher="%s" style="background-image:url(\'%s?w=1400&q=80\')">\n  <div class="slide-inner">\n%s\n  </div>\n</div>\n'%(n,phase,LESSON,teacher,imgurl,inner))
def audiobtn(t,v):
    return '<button class="audio-btn-sm" data-voice="%s" onclick="speakText(\'%s\',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg></button>'%(v,t)
def vcard(gid,c1,c2,svg,clue,word,d,ex):
    return ('      <div class="vocab-card-ic" onclick="this.classList.toggle(\'revealed\')">\n        <div class="vocab-front"><div class="vocab-icon"><svg width="48" height="48" viewBox="0 0 48 48"><defs><linearGradient id="%s" x1="0" y1="0" x2="1" y2="1"><stop offset="0%%" stop-color="%s"/><stop offset="100%%" stop-color="%s"/></linearGradient></defs><rect width="48" height="48" rx="10" fill="url(#%s)"/>%s</svg></div><div class="vocab-clue">%s</div></div>\n        <div class="vocab-back"><h4>%s</h4><div class="vocab-def-ic">%s</div><div class="vocab-ex-ic">%s</div><button class="audio-btn-sm" onclick="event.stopPropagation();speakText(\'%s\',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div>\n      </div>'%(gid,c1,c2,gid,svg,clue,word,d,ex,word))
def dline(did,sp,v,color,ini,bg,text,disp):
    return ('      <div class="dialogue-line" id="%s" data-speaker="%s" data-voice="%s" style="display:%s;gap:.8rem;padding:.8rem;background:rgba(255,255,255,.06);border-radius:8px%s">\n        <div style="width:36px;height:36px;border-radius:50%%;background:%s;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:.75rem;flex-shrink:0">%s</div>\n        <div><div class="dialogue-name" style="color:%s">%s</div><p style="color:rgba(255,255,255,.85);font-size:.88rem">"%s"</p></div>\n        %s\n      </div>'%(did,sp,v,disp,(";opacity:1" if disp=="flex" else ""),bg,ini,color,sp,text,audiobtn(text,v)))

chain='<circle cx="18" cy="18" r="4" stroke="#fff" stroke-width="2" fill="none"/><circle cx="30" cy="30" r="4" stroke="#fff" stroke-width="2" fill="none"/><path d="M21 21l6 6" stroke="#fff" stroke-width="2"/>'
boxsvg='<rect x="14" y="18" width="20" height="14" rx="1" stroke="#fff" stroke-width="2" fill="none"/><path d="M14 22h20M24 18v14" stroke="#fff" stroke-width="2"/>'
stamp_ic='<rect x="15" y="14" width="18" height="20" rx="2" stroke="#fff" stroke-width="2" fill="none"/><path d="M19 22l3 3 7-7" stroke="#fff" stroke-width="2" fill="none" stroke-linecap="round"/>'
boat='<path d="M14 28h20l-3 6H17z" stroke="#fff" stroke-width="2" fill="none" stroke-linejoin="round"/><path d="M24 14v14M24 14l6 4-6 2" stroke="#fff" stroke-width="2" fill="none"/>'
house='<path d="M14 24l10-8 10 8v10H14z" stroke="#fff" stroke-width="2" fill="none" stroke-linejoin="round"/>'
truck2='<rect x="13" y="19" width="13" height="10" rx="1" stroke="#fff" stroke-width="2" fill="none"/><path d="M26 22h5l3 4v3h-8z" stroke="#fff" stroke-width="2" fill="none"/><circle cx="18" cy="31" r="2" fill="#fff"/><circle cx="31" cy="31" r="2" fill="#fff"/>'
cog='<circle cx="24" cy="24" r="6" stroke="#fff" stroke-width="2" fill="none"/><path d="M24 14v4M24 30v4M14 24h4M30 24h4" stroke="#fff" stroke-width="2" stroke-linecap="round"/>'

SL=[]
SL.append(img_slide(1,1,"<strong>Cover (30s):</strong> Compartilhe a tela. 'Today we learn how to describe your supply chain, from Brazil to the U.S., using the Passive Voice.' Avance.",
    "Supply","Supply<br><span class=\"accent\">Chain</span>","Lesson 10 - From Brazil to the U.S. - the Passive Voice",COVER))
SL.append(slide(2,1,"slide-dark","<strong>Quick Review (4 min):</strong> Retome a Aula 9 (Past Simple e contratos). Pergunte e Milton responde. Objetivo: reativar antes de focar na Passive Voice.",
    '''    <div class="chapter-label">Quick Review - Lesson 9</div>
    <h2 class="slide-heading">Quick <span class="accent">Review</span></h2>
    <div style="display:flex;flex-direction:column;gap:1.2rem;margin-top:1rem;width:100%">
      <div style="border-left:3px solid var(--accent-light);padding-left:1rem"><p style="color:rgba(255,255,255,.9);font-size:.95rem;font-weight:600">"When did you sign your last contract?" (Past Simple)</p></div>
      <div style="border-left:3px solid var(--accent-light);padding-left:1rem"><p style="color:rgba(255,255,255,.9);font-size:.95rem;font-weight:600">"What did the two parties agree on?" (Past Simple)</p></div>
      <div style="border-left:3px solid var(--accent-light);padding-left:1rem"><p style="color:rgba(255,255,255,.9);font-size:.95rem;font-weight:600">"Today: how do we describe a process when the action matters most? The Passive Voice."</p></div>
    </div>'''))
SL.append(slide(3,1,"slide-dark","<strong>Warm-up (3 min):</strong> Faca a pergunta. Milton descreve livremente como seus produtos chegam aos EUA. Anote frases ativas que poderiam virar passivas.",
    '''    <div class="chapter-label">Warm-up</div>
    <h2 class="slide-heading">How is your jewelry <span class="accent">made and shipped</span>?</h2>
    <p style="color:rgba(255,255,255,.6);font-size:.92rem;margin-top:1rem">Think about: Where are the products made? How are they sent to the U.S.?</p>'''))
SL.append(slide(4,1,"slide-dark","<strong>Context (2 min):</strong> Apresente o tema: descrever a cadeia de suprimentos do Milton, do Brasil aos EUA. 'We will tell the journey of a shipment in English.'",
    '''    <div class="chapter-label">Today's Mission</div>
    <h2 class="slide-heading">From <span class="accent">Brazil to the U.S.</span></h2>
    <p style="color:rgba(255,255,255,.6);font-size:.92rem;margin-top:1rem">We will describe the full journey: made, packed, shipped, inspected, delivered.</p>'''))

SL.append(img_slide(5,2,"<strong>Transition (10s):</strong> 'Let us learn the words of the supply chain.' Avance.","Packing","Packing<br><span class=\"accent\">Words</span>","","https://images.unsplash.com/photo-1526628953301-3e589a6a8b74"))
SL.append(slide(6,2,"slide-dark","<strong>Vocab (3 min):</strong> Milton clica em cada card. Corrija pronuncia de: freight /frayt/, warehouse /WAIR-hous/.",
    '''    <div class="chapter-label">Vocabulary</div>
    <h2 class="slide-heading">Click to <span class="accent">reveal</span></h2>
    <div class="vocab-grid-ic">
'''+vcard("gd1","#0d7377","#14b8a6",chain,"Production to delivery","Supply Chain","The full process from production to delivery.","\"Our supply chain starts in Brazil.\"")+"\n"
   +vcard("gd2","#2563eb","#60a5fa",boxsvg,"Goods sent together","Shipment","A load of goods sent together.","\"The shipment was delivered in 20 days.\"")+"\n"
   +vcard("gd3","#B8860B","#D4A84B",stamp_ic,"Where imports are checked","Customs","The office that checks imported goods.","\"All cargo is inspected at customs.\"")+"\n"
   +vcard("gd4","#7c3aed","#a78bfa",truck2,"Goods transported in bulk","Freight","Goods transported in bulk; the cost of transport.","\"Freight by sea is cheaper than by air.\"")+'''
    </div>
    <div class="vocab-counter">Click on the cards to reveal - 0 / 4 words</div>'''))
SL.append(slide(7,2,"slide-dark","<strong>Vocab (3 min):</strong> Mesma dinamica. Corrija pronuncia de: cargo /KAR-go/, logistics /loh-JIS-tiks/.",
    '''    <div class="chapter-label">Vocabulary</div>
    <h2 class="slide-heading">4 more <span class="accent">words</span></h2>
    <div class="vocab-grid-ic">
'''+vcard("gd5","#059669","#34d399",house,"A building to store goods","Warehouse","A large building where goods are stored.","\"The products are packed in our warehouse.\"")+"\n"
   +vcard("gd6","#0891b2","#67e8f9",boat,"Goods carried by ship/plane","Cargo","Goods carried by ship, plane, or truck.","\"The cargo was inspected at customs.\"")+"\n"
   +vcard("gd7","#ea580c","#fb923c",cog,"Organizing movement of goods","Logistics","The organization of moving and storing goods.","\"Our logistics team manages every shipment.\"")+"\n"
   +vcard("gd8","#dc2626","#f87171",boxsvg,"A metal box for shipping","Container","A large metal box used for shipping goods.","\"The containers are sent by sea.\"")+'''
    </div>
    <div class="vocab-counter">Click on the cards to reveal - 0 / 4 words</div>'''))

SL.append(img_slide(8,3,"<strong>Transition (10s):</strong> 'Now the code - the Passive Voice, to describe a process.' Avance.","The","The<br><span class=\"accent\">Code</span>","","https://images.unsplash.com/photo-1450101499163-c8848c66ca85"))
SL.append(slide(9,3,"slide-dark","<strong>Discovery (3 min):</strong> Leia cada frase. Pergunte: 'Who does the action? Is it important?' Resposta: o foco e a acao/produto, nao quem faz. Peca para Milton apontar 'be + verbo'.",
    '''    <div class="chapter-label">Grammar Discovery</div>
    <h2 class="slide-heading">Look at the <span class="accent">gold verbs</span></h2>
    <div style="display:flex;flex-direction:column;gap:1rem;margin-top:1.5rem;width:100%">
      <div style="padding:.8rem 1rem;background:rgba(255,255,255,.06);border-left:3px solid var(--accent);border-radius:0 8px 8px 0;color:rgba(255,255,255,.85);font-size:.95rem;">"The jewelry <strong style="color:var(--accent-light)">is made</strong> in Brazil."</div>
      <div style="padding:.8rem 1rem;background:rgba(255,255,255,.06);border-left:3px solid var(--accent);border-radius:0 8px 8px 0;color:rgba(255,255,255,.85);font-size:.95rem;">"The products <strong style="color:var(--accent-light)">are packed</strong> in the warehouse."</div>
      <div style="padding:.8rem 1rem;background:rgba(255,255,255,.06);border-left:3px solid var(--accent);border-radius:0 8px 8px 0;color:rgba(255,255,255,.85);font-size:.95rem;">"The order <strong style="color:var(--accent-light)">was shipped</strong> last week."</div>
      <div style="padding:.8rem 1rem;background:rgba(255,255,255,.06);border-left:3px solid var(--accent);border-radius:0 8px 8px 0;color:rgba(255,255,255,.85);font-size:.95rem;">"The cargo <strong style="color:var(--accent-light)">was inspected</strong> at customs."</div>
    </div>
    <p style="color:var(--accent-light);font-size:1rem;font-weight:600;margin-top:1.5rem">Each one is "be + past participle". The doer is not important.</p>'''))
SL.append(slide(10,3,"slide-dark","<strong>Rule (2 min):</strong> Clique em Reveal the Rule. Leia cada linha. Reforce: be (is/are/was/were) + participio passado; 'by + agente' e opcional.",
    '''    <div class="chapter-label">Grammar Rule</div>
    <h2 class="slide-heading">The Passive <span class="accent">Voice</span></h2>
    <button class="primary-btn" onclick="var box=this.nextElementSibling;box.classList.toggle('visible');this.textContent=box.classList.contains('visible')?'Hide the Rule':'Reveal the Rule'">Reveal the Rule</button>
    <div class="rule-box">
      <table class="grammar-table-ic">
        <thead><tr><th>Form</th><th>Structure</th><th>Example</th></tr></thead>
        <tbody>
          <tr><td><strong>Present</strong></td><td>is/are + participle</td><td>"is made / are packed"</td></tr>
          <tr><td><strong>Past</strong></td><td>was/were + participle</td><td>"was shipped / were sent"</td></tr>
          <tr><td><strong>Agent</strong></td><td>+ by + who</td><td>"managed by our team"</td></tr>
          <tr><td><strong>Question</strong></td><td>be + subject + participle</td><td>"Was it inspected?"</td></tr>
        </tbody>
      </table>
    </div>'''))
SL.append(slide(11,3,"slide-dark","<strong>Common Mistake (2 min):</strong> Mostre os pares. Pergunte qual esta certo (verde). Reforce: depois de 'be' usa-se o PARTICIPIO (made, shipped), nao o infinitivo.",
    '''    <div class="chapter-label">Common Mistake</div>
    <h2 class="slide-heading">After "be", use the <span class="accent">past participle</span></h2>
    <div style="display:flex;flex-direction:column;gap:1.5rem;margin-top:1.5rem;width:100%;max-width:540px">
      <div style="padding:1rem;background:rgba(220,38,38,.1);border:1px solid rgba(220,38,38,.3);border-radius:8px;display:flex;align-items:center;gap:.8rem"><span style="font-size:1.5rem;color:#f87171">&#10007;</span><span style="color:rgba(255,255,255,.85);font-size:.92rem">"The jewelry <strong>is make</strong> in Brazil."</span></div>
      <div style="padding:1rem;background:rgba(22,163,74,.1);border:1px solid rgba(22,163,74,.3);border-radius:8px;display:flex;align-items:center;gap:.8rem"><span style="font-size:1.5rem;color:#4ade80">&#10003;</span><span style="color:rgba(255,255,255,.85);font-size:.92rem">"The jewelry <strong>is made</strong> in Brazil."</span></div>
    </div>
    <p style="color:rgba(255,255,255,.5);font-size:.82rem;margin-top:1.5rem;font-style:italic">be + past participle: is made, are sent, was shipped, were inspected.</p>'''))
SL.append(slide(12,3,"slide-dark","<strong>Practice (3 min):</strong> Milton completa oralmente. Clique para revelar. Respostas: 1=is made, 2=are sent, 3=was shipped, 4=Was...inspected.",
    '''    <div class="chapter-label">Grammar Practice</div>
    <h2 class="slide-heading">Complete the <span class="accent">sentence</span></h2>
    <div class="comp-questions">
      <div class="comp-q" onclick="this.querySelector('.q-answer').style.display=this.querySelector('.q-answer').style.display==='block'?'none':'block'"><div class="q-text">1. "The jewelry ___ (make) in Brazil." (present)</div><div class="q-answer">is made</div></div>
      <div class="comp-q" onclick="this.querySelector('.q-answer').style.display=this.querySelector('.q-answer').style.display==='block'?'none':'block'"><div class="q-text">2. "The containers ___ (send) by sea." (present, plural)</div><div class="q-answer">are sent</div></div>
      <div class="comp-q" onclick="this.querySelector('.q-answer').style.display=this.querySelector('.q-answer').style.display==='block'?'none':'block'"><div class="q-text">3. "The order ___ (ship) last week." (past)</div><div class="q-answer">was shipped</div></div>
      <div class="comp-q" onclick="this.querySelector('.q-answer').style.display=this.querySelector('.q-answer').style.display==='block'?'none':'block'"><div class="q-text">4. "___ the cargo ___ (inspect) at customs?" (past question)</div><div class="q-answer">Was the cargo inspected</div></div>
    </div>'''))

SL.append(img_slide(13,4,"<strong>Transition (10s):</strong> 'Let us follow a real shipment from Brazil to the U.S.' Avance.","Getting","Getting<br><span class=\"accent\">There</span>","","https://images.unsplash.com/photo-1555421689-d68471e189f2"))
SL.append(slide(14,4,"slide-light","<strong>Supply chain map (3 min):</strong> Leia o mapa com Milton. Para cada etapa, peca uma frase passiva: 'The jewelry is made...', 'The cargo is shipped...'. Corrija a Passive Voice.",
    '''    <div class="chapter-label">The Journey</div>
    <h2 class="slide-heading" style="color:var(--text)">From Brazil <span class="accent">to the U.S.</span></h2>
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:1.2rem;width:100%;max-width:540px;box-shadow:0 4px 16px rgba(0,0,0,.06)">
      <div style="font-size:.78rem;font-weight:700;color:var(--accent);text-transform:uppercase;letter-spacing:1px;margin-bottom:.8rem">Sayegh Jewelry - Supply Chain</div>
      <div style="display:flex;flex-direction:column;gap:.6rem;font-size:.9rem;color:var(--text)">
        <div style="display:flex;gap:1rem;padding-bottom:.5rem;border-bottom:1px solid var(--border)"><strong style="color:var(--accent);min-width:1.6rem">1</strong><span>The jewelry <strong>is made</strong> in Sao Paulo.</span></div>
        <div style="display:flex;gap:1rem;padding-bottom:.5rem;border-bottom:1px solid var(--border)"><strong style="color:var(--accent);min-width:1.6rem">2</strong><span>The products <strong>are packed</strong> in the warehouse.</span></div>
        <div style="display:flex;gap:1rem;padding-bottom:.5rem;border-bottom:1px solid var(--border)"><strong style="color:var(--accent);min-width:1.6rem">3</strong><span>The containers <strong>are shipped</strong> by sea from Santos.</span></div>
        <div style="display:flex;gap:1rem;padding-bottom:.5rem;border-bottom:1px solid var(--border)"><strong style="color:var(--accent);min-width:1.6rem">4</strong><span>The cargo <strong>is inspected</strong> at U.S. customs.</span></div>
        <div style="display:flex;gap:1rem"><strong style="color:var(--accent);min-width:1.6rem">5</strong><span>The shipment <strong>is delivered</strong> to clients in New York.</span></div>
      </div>
    </div>'''))
SL.append(slide(15,4,"slide-dark","<strong>Comprehension (2 min):</strong> Milton clica para revelar. Confirme que ele entendeu cada etapa da cadeia.",
    '''    <div class="chapter-label">Comprehension</div>
    <h2 class="slide-heading">Read the <span class="accent">Journey</span></h2>
    <div class="comp-questions">
      <div class="comp-q" onclick="this.querySelector('.q-answer').style.display=this.querySelector('.q-answer').style.display==='block'?'none':'block'"><div class="q-text">1. Where is the jewelry made?</div><div class="q-answer">In Sao Paulo, Brazil.</div></div>
      <div class="comp-q" onclick="this.querySelector('.q-answer').style.display=this.querySelector('.q-answer').style.display==='block'?'none':'block'"><div class="q-text">2. How are the containers shipped?</div><div class="q-answer">By sea, from the port of Santos.</div></div>
      <div class="comp-q" onclick="this.querySelector('.q-answer').style.display=this.querySelector('.q-answer').style.display==='block'?'none':'block'"><div class="q-text">3. What happens at U.S. customs?</div><div class="q-answer">The cargo is inspected.</div></div>
    </div>'''))
SL.append(slide(16,4,"slide-dark","<strong>Listening (3 min):</strong> Toque cada frase. Milton ouve e repete. Pergunte: present ou past passive? Vozes alternadas Arthur/Ellen.",
    '''    <div class="chapter-label">Listening</div>
    <h2 class="slide-heading">Listen and <span class="accent">Identify</span></h2>
    <p style="color:rgba(255,255,255,.6);font-size:.88rem;margin-bottom:1.5rem">Present or past passive? Listen to each phrase.</p>
    <div style="display:flex;flex-direction:column;gap:1rem;width:100%">
      <div style="display:flex;align-items:center;gap:.8rem;padding:.8rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:8px"><span style="color:var(--accent-light);font-weight:700;min-width:1.5rem">1</span><span style="color:rgba(255,255,255,.85);flex:1;font-size:.92rem">"Our jewelry is made in Brazil."</span>'''+audiobtn("Our jewelry is made in Brazil.","arthur")+'''</div>
      <div style="display:flex;align-items:center;gap:.8rem;padding:.8rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:8px"><span style="color:var(--accent-light);font-weight:700;min-width:1.5rem">2</span><span style="color:rgba(255,255,255,.85);flex:1;font-size:.92rem">"The order was shipped last Friday."</span>'''+audiobtn("The order was shipped last Friday.","ellen")+'''</div>
      <div style="display:flex;align-items:center;gap:.8rem;padding:.8rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:8px"><span style="color:var(--accent-light);font-weight:700;min-width:1.5rem">3</span><span style="color:rgba(255,255,255,.85);flex:1;font-size:.92rem">"The containers are sent by sea."</span>'''+audiobtn("The containers are sent by sea.","arthur")+'''</div>
      <div style="display:flex;align-items:center;gap:.8rem;padding:.8rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:8px"><span style="color:var(--accent-light);font-weight:700;min-width:1.5rem">4</span><span style="color:rgba(255,255,255,.85);flex:1;font-size:.92rem">"The cargo was inspected at customs."</span>'''+audiobtn("The cargo was inspected at customs.","ellen")+'''</div>
    </div>'''))
SL.append(slide(17,4,"slide-dark","<strong>Dialogue (4 min):</strong> 'You confirm the shipping process with your logistics partner, Ms. Lopez. Read line by line.' Clique Next Line. Milton le a parte dele. Corrija a Passive Voice.",
    '''    <div class="chapter-label">Dialogue</div>
    <h2 class="slide-heading">Confirming the <span class="accent">Shipment</span></h2>
    <p style="color:rgba(255,255,255,.6);font-size:.88rem;margin-bottom:1rem">You check the shipping process with your logistics partner, Ms. Lopez.</p>
    <div id="dialogueLines" style="display:flex;flex-direction:column;gap:.8rem;width:100%">
'''+dline("dl1","Milton (You)","arthur","var(--accent-light)","MS","var(--accent)","Good morning, Ms. Lopez. I want to confirm how our jewelry is shipped to the US.","flex")+"\n"
   +dline("dl2","Ms. Lopez","ellen","#7dd3fc","ML","#2563eb","Of course. The products are made here in Brazil and then packed in our warehouse.","none")+"\n"
   +dline("dl3","Milton (You)","arthur","var(--accent-light)","MS","var(--accent)","And how is the cargo transported?","none")+"\n"
   +dline("dl4","Ms. Lopez","ellen","#7dd3fc","ML","#2563eb","The containers are sent by sea. Last month, the shipment was delivered in twenty days.","none")+"\n"
   +dline("dl5","Milton (You)","arthur","var(--accent-light)","MS","var(--accent)","Was everything checked at customs?","none")+"\n"
   +dline("dl6","Ms. Lopez","ellen","#7dd3fc","ML","#2563eb","Yes. All the cargo was inspected and released without problems.","none")+'''
    </div>
    <button class="primary-btn" style="margin-top:1rem" onclick="var lines=['dl2','dl3','dl4','dl5','dl6'];for(var i=0;i<lines.length;i++){var el=document.getElementById(lines[i]);if(el.style.display==='none'){el.style.display='flex';break}}">Next Line</button>'''))

SL.append(img_slide(18,5,"<strong>Transition (10s):</strong> 'Time to practice the Passive Voice!' Avance.","More","More<br><span class=\"accent\">Practice</span>","","https://images.unsplash.com/photo-1497032628192-86f99bcd76bc"))
SL.append(slide(19,5,"slide-dark","<strong>Quick Fire (4 min):</strong> Uma situacao por vez. Milton responde antes de revelar.",
    '''    <div class="chapter-label">Quick Fire</div>
    <h2 class="slide-heading">Quick <span class="accent">Fire</span></h2>
    <div id="qf10" style="width:100%">
      <div class="challenge-card" id="qf10-1"><div style="font-size:.75rem;color:var(--accent-light);font-weight:700;margin-bottom:1rem">Challenge 1 / 4</div><p style="color:rgba(255,255,255,.85);font-size:.95rem;line-height:1.6;margin-bottom:1.5rem">Say where your products are produced (present passive).</p><button class="primary-btn" id="qf10ShowBtn1" onclick="document.getElementById('qf10Answer1').style.display='block';this.style.display='none';document.getElementById('qf10NextBtn1').style.display='inline-flex'">Show Answer</button><div id="qf10Answer1" style="display:none;margin-top:1rem;padding:1rem;background:rgba(22,163,74,.1);border:1px solid rgba(22,163,74,.3);border-radius:8px;color:#4ade80;font-weight:600">"The jewelry is made in Brazil." - is + made (past participle).</div><button class="secondary-btn" id="qf10NextBtn1" style="display:none;margin-top:1rem" onclick="document.getElementById('qf10-1').style.display='none';document.getElementById('qf10-2').style.display='flex'">Next Question</button></div>
      <div class="challenge-card" id="qf10-2" style="display:none"><div style="font-size:.75rem;color:var(--accent-light);font-weight:700;margin-bottom:1rem">Challenge 2 / 4</div><p style="color:rgba(255,255,255,.85);font-size:.95rem;line-height:1.6;margin-bottom:1.5rem">Say the order was sent in the past (past passive).</p><button class="primary-btn" id="qf10ShowBtn2" onclick="document.getElementById('qf10Answer2').style.display='block';this.style.display='none';document.getElementById('qf10NextBtn2').style.display='inline-flex'">Show Answer</button><div id="qf10Answer2" style="display:none;margin-top:1rem;padding:1rem;background:rgba(22,163,74,.1);border:1px solid rgba(22,163,74,.3);border-radius:8px;color:#4ade80;font-weight:600">"The order was shipped yesterday." - was + shipped.</div><button class="secondary-btn" id="qf10PrevBtn2" style="margin-top:.5rem" onclick="document.getElementById('qf10-2').style.display='none';document.getElementById('qf10-1').style.display='flex'">Previous</button><button class="secondary-btn" id="qf10NextBtn2" style="display:none;margin-top:.5rem" onclick="document.getElementById('qf10-2').style.display='none';document.getElementById('qf10-3').style.display='flex'">Next Question</button></div>
      <div class="challenge-card" id="qf10-3" style="display:none"><div style="font-size:.75rem;color:var(--accent-light);font-weight:700;margin-bottom:1rem">Challenge 3 / 4</div><p style="color:rgba(255,255,255,.85);font-size:.95rem;line-height:1.6;margin-bottom:1.5rem">Ask if the cargo was inspected (past passive question).</p><button class="primary-btn" id="qf10ShowBtn3" onclick="document.getElementById('qf10Answer3').style.display='block';this.style.display='none';document.getElementById('qf10NextBtn3').style.display='inline-flex'">Show Answer</button><div id="qf10Answer3" style="display:none;margin-top:1rem;padding:1rem;background:rgba(22,163,74,.1);border:1px solid rgba(22,163,74,.3);border-radius:8px;color:#4ade80;font-weight:600">"Was the cargo inspected at customs?" - Was + subject + participle.</div><button class="secondary-btn" id="qf10PrevBtn3" style="margin-top:.5rem" onclick="document.getElementById('qf10-3').style.display='none';document.getElementById('qf10-2').style.display='flex'">Previous</button><button class="secondary-btn" id="qf10NextBtn3" style="display:none;margin-top:.5rem" onclick="document.getElementById('qf10-3').style.display='none';document.getElementById('qf10-4').style.display='flex'">Next Question</button></div>
      <div class="challenge-card" id="qf10-4" style="display:none"><div style="font-size:.75rem;color:var(--accent-light);font-weight:700;margin-bottom:1rem">Challenge 4 / 4</div><p style="color:rgba(255,255,255,.85);font-size:.95rem;line-height:1.6;margin-bottom:1.5rem">Say who manages the supply chain (with the agent).</p><button class="primary-btn" id="qf10ShowBtn4" onclick="document.getElementById('qf10Answer4').style.display='block';this.style.display='none'">Show Answer</button><div id="qf10Answer4" style="display:none;margin-top:1rem;padding:1rem;background:rgba(22,163,74,.1);border:1px solid rgba(22,163,74,.3);border-radius:8px;color:#4ade80;font-weight:600">"The supply chain is managed by our logistics team." - by + agent.</div><button class="secondary-btn" style="margin-top:.5rem" onclick="document.getElementById('qf10-4').style.display='none';document.getElementById('qf10-3').style.display='flex'">Previous</button></div>
    </div>'''))
SL.append(slide(20,5,"slide-dark","<strong>Spot the Error (3 min):</strong> Milton clica para revelar erro e correcao. 1=is made (participio), 2=was shipped (passiva), 3=Was...inspected.",
    '''    <div class="chapter-label">Spot the Error</div>
    <h2 class="slide-heading">Find the <span class="accent">Mistake</span></h2>
    <div class="error-grid">
      <div class="error-card" onclick="this.classList.toggle('open')"><div class="error-sentence">"The jewelry <span class="wrong">is make</span> in Brazil."</div><div class="error-fix">Correct: "The jewelry <strong>is made</strong> in Brazil."</div></div>
      <div class="error-card" onclick="this.classList.toggle('open')"><div class="error-sentence">"The order <span class="wrong">was ship</span> last week."</div><div class="error-fix">Correct: "The order <strong>was shipped</strong> last week."</div></div>
      <div class="error-card" onclick="this.classList.toggle('open')"><div class="error-sentence">"<span class="wrong">Did the cargo inspected</span> at customs?"</div><div class="error-fix">Correct: "<strong>Was the cargo inspected</strong> at customs?"</div></div>
    </div>'''))
SL.append(slide(21,5,"slide-dark","<strong>Delayed Error Correction (3 min):</strong> Anote erros reais de Milton e corrija ao vivo. Foque em: be + participio, present vs past passive, perguntas passivas.",
    '''    <div class="chapter-label">Error Correction</div>
    <h2 class="slide-heading">Let's Fix <span class="accent">Together</span></h2>
    <div style="display:flex;flex-direction:column;gap:1rem;margin-top:1.5rem;width:100%">
      <div style="padding:1rem;background:rgba(220,38,38,.08);border:1px solid rgba(220,38,38,.2);border-radius:8px"><div style="font-size:.72rem;font-weight:700;color:#f87171;text-transform:uppercase;letter-spacing:1px;margin-bottom:.4rem">Error 1</div><div contenteditable="true" style="min-height:2rem;padding:.4rem;border-bottom:1px dashed rgba(255,255,255,.3);color:rgba(255,255,255,.85);font-size:.88rem;outline:none">Type the error here...</div></div>
      <div style="padding:1rem;background:rgba(22,163,74,.08);border:1px solid rgba(22,163,74,.2);border-radius:8px"><div style="font-size:.72rem;font-weight:700;color:#4ade80;text-transform:uppercase;letter-spacing:1px;margin-bottom:.4rem">Correction 1</div><div contenteditable="true" style="min-height:2rem;padding:.4rem;border-bottom:1px dashed rgba(255,255,255,.3);color:rgba(255,255,255,.85);font-size:.88rem;outline:none">Type the correction here...</div></div>
      <div style="padding:1rem;background:rgba(220,38,38,.08);border:1px solid rgba(220,38,38,.2);border-radius:8px"><div style="font-size:.72rem;font-weight:700;color:#f87171;text-transform:uppercase;letter-spacing:1px;margin-bottom:.4rem">Error 2</div><div contenteditable="true" style="min-height:2rem;padding:.4rem;border-bottom:1px dashed rgba(255,255,255,.3);color:rgba(255,255,255,.85);font-size:.88rem;outline:none">Type the error here...</div></div>
      <div style="padding:1rem;background:rgba(22,163,74,.08);border:1px solid rgba(22,163,74,.2);border-radius:8px"><div style="font-size:.72rem;font-weight:700;color:#4ade80;text-transform:uppercase;letter-spacing:1px;margin-bottom:.4rem">Correction 2</div><div contenteditable="true" style="min-height:2rem;padding:.4rem;border-bottom:1px dashed rgba(255,255,255,.3);color:rgba(255,255,255,.85);font-size:.88rem;outline:none">Type the correction here...</div></div>
    </div>'''))

SL.append(img_slide(22,6,"<strong>Transition (10s):</strong> 'Now it is your turn - from guided to free.' Avance.","Your","Your<br><span class=\"accent\">Turn</span>","From guided to free - describe your supply chain","https://images.unsplash.com/photo-1556761175-5973dc0f32e7"))
SL.append(slide(23,6,"slide-dark","<strong>Role-play Guided (3 min):</strong> Milton descreve a cadeia usando as keywords, em voz passiva. Pelo menos 3 frases passivas. Ajude se precisar.",
    '''    <div class="chapter-label">Role-play - Guided</div>
    <h2 class="slide-heading">Describe the <span class="accent">Journey</span></h2>
    <div class="roleplay-card"><div class="roleplay-scenario">Describe how your jewelry travels from Brazil to the U.S. Use the keywords and at least 3 passive sentences.</div><div style="margin-top:1rem;display:flex;flex-wrap:wrap;gap:.5rem"><span class="roleplay-kw">is made</span><span class="roleplay-kw">are packed</span><span class="roleplay-kw">are shipped by sea</span><span class="roleplay-kw">is inspected at customs</span><span class="roleplay-kw">is delivered</span></div></div>'''))
SL.append(slide(24,6,"slide-dark","<strong>Role-play Semi-free (3 min):</strong> Milton explica a logistica de um pedido especifico, com apoio minimo. Deve usar present e past passive.",
    '''    <div class="chapter-label">Role-play - Semi-free</div>
    <h2 class="slide-heading">Explain a <span class="accent">Shipment</span></h2>
    <div class="roleplay-card"><div class="roleplay-scenario">Explain how a recent order was handled: where it was made, how it was packed and shipped, and when it was delivered. Mix present and past passive.</div><div style="margin-top:1rem;display:flex;flex-wrap:wrap;gap:.5rem"><span class="roleplay-kw">was made</span><span class="roleplay-kw">was shipped</span><span class="roleplay-kw">was delivered</span></div></div>'''))
SL.append(slide(25,6,"slide-dark","<strong>Role-play Free (3 min):</strong> Milton descreve a cadeia REAL do proprio negocio, sem apoio. Deve incluir producao, embalagem, transporte, customs e entrega, em voz passiva. Avalie fluencia.",
    '''    <div class="chapter-label">Role-play - Free</div>
    <h2 class="slide-heading">Your Real <span class="accent">Supply Chain</span></h2>
    <div class="roleplay-card"><div class="roleplay-scenario">Describe your REAL supply chain to your teacher, using the Passive Voice. Include: where the products are made, how they are packed and shipped, what happens at customs, and how they are delivered. No keywords this time.</div></div>'''))
SL.append(slide(26,6,"slide-dark","<strong>Oral Drill (3 min):</strong> Milton repete cada frase. Corrija pronuncia de: made /mayd/, exported /eks-POR-tid/, transported /trans-POR-tid/.",
    '''    <div class="chapter-label">Oral Drill</div>
    <h2 class="slide-heading">Repeat Each <span class="accent">Phrase</span></h2>
    <div style="display:flex;flex-direction:column;gap:1rem;margin-top:1.5rem;">
      <div style="padding:.8rem 1rem;background:rgba(255,255,255,.06);border-left:3px solid var(--accent);border-radius:0 8px 8px 0;color:rgba(255,255,255,.85);font-size:.95rem;">"Our products <strong>are made</strong> in Brazil."</div>
      <div style="padding:.8rem 1rem;background:rgba(255,255,255,.06);border-left:3px solid var(--accent);border-radius:0 8px 8px 0;color:rgba(255,255,255,.85);font-size:.95rem;">"The jewelry <strong>is exported</strong> to the United States."</div>
      <div style="padding:.8rem 1rem;background:rgba(255,255,255,.06);border-left:3px solid var(--accent);border-radius:0 8px 8px 0;color:rgba(255,255,255,.85);font-size:.95rem;">"The shipment <strong>was sent</strong> last week."</div>
      <div style="padding:.8rem 1rem;background:rgba(255,255,255,.06);border-left:3px solid var(--accent);border-radius:0 8px 8px 0;color:rgba(255,255,255,.85);font-size:.95rem;">"The containers <strong>are transported</strong> by sea."</div>
      <div style="padding:.8rem 1rem;background:rgba(255,255,255,.06);border-left:3px solid var(--accent);border-radius:0 8px 8px 0;color:rgba(255,255,255,.85);font-size:.95rem;">"The cargo <strong>was checked</strong> at customs."</div>
    </div>'''))

SL.append(img_slide(27,7,"<strong>Transition (10s):</strong> 'Great work! Let us review what you learned.' Avance.","Wrapping","Wrapping<br><span class=\"accent\">Up</span>","","https://images.unsplash.com/photo-1521737604893-d14cc237f11d"))
SL.append(slide(28,7,"slide-light","<strong>Checklist (2 min):</strong> Milton clica cada checkbox. Quando todos marcados, a aula conta como concluida. Pergunte: 'Which step of your supply chain is the hardest to explain?'",
    '''    <div class="chapter-label">What I Learned</div>
    <h2 class="slide-heading">Lesson 10 <span class="accent">Checklist</span></h2>
    <div class="check-grid">
      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div>I know 8 supply chain and logistics words.</div>
      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div>I can form the present passive (is/are + past participle).</div>
      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div>I can form the past passive (was/were + past participle).</div>
      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div>I can ask passive questions and add "by + agent".</div>
      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div>I can describe my supply chain from Brazil to the U.S.</div>
    </div>'''))
SL.append(slide(29,7,"slide-dark","<strong>Feedback (3 min):</strong> De feedback personalizado. Pontos fortes e 1-2 areas a focar. Termine sempre positivo.",
    '''    <div class="chapter-label">Feedback</div>
    <h2 class="slide-heading">Teacher <span class="accent">Feedback</span></h2>
    <div style="display:flex;flex-direction:column;gap:1.2rem;margin-top:1.5rem;">
      <div style="padding:1rem;background:rgba(22,163,74,.1);border:1px solid rgba(22,163,74,.3);border-radius:8px;"><div style="color:#4ade80;font-weight:700;margin-bottom:.5rem;">Strengths</div><div contenteditable="true" style="color:rgba(255,255,255,.7);font-size:.9rem;min-height:2rem;outline:none;border-bottom:1px dashed rgba(255,255,255,.2);padding-bottom:.3rem">Note Milton's strong points here during the lesson.</div></div>
      <div style="padding:1rem;background:rgba(217,119,6,.1);border:1px solid rgba(217,119,6,.3);border-radius:8px;"><div style="color:#fbbf24;font-weight:700;margin-bottom:.5rem;">Areas to Improve</div><div contenteditable="true" style="color:rgba(255,255,255,.7);font-size:.9rem;min-height:2rem;outline:none;border-bottom:1px dashed rgba(255,255,255,.2);padding-bottom:.3rem">Note areas for improvement during the lesson.</div></div>
    </div>'''))
SL.append(slide(30,7,"slide-dark","<strong>Homework (1 min):</strong> DIGA ORALMENTE (nao mostrar escrito): '1. Complete the Pre-class for Lesson 10. 2. Map your company's supply chain in 6 passive sentences. 3. Watch a How It's Made episode. 4. Describe one product process in the passive.'",
    '''    <div class="chapter-label">Homework</div>
    <h2 class="slide-heading" style="color:#fff">Your <span class="accent">Mission</span></h2>
    <p style="color:rgba(255,255,255,.6);font-size:1rem;margin-top:1rem;">Your teacher will explain your homework now.</p>
    <div style="margin-top:2rem;padding:1rem;background:rgba(255,255,255,.06);border-radius:10px;display:inline-block"><svg viewBox="0 0 24 24" width="48" height="48" fill="none" stroke="rgba(255,255,255,.4)" stroke-width="1.5"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg></div>''',style="text-align:center"))
SL.append(slide(31,7,"slide-dark","<strong>Badge (1 min):</strong> Celebre! 'You earned your tenth stamp, Milton! You can now describe your whole supply chain in English.' Confetti automatico.",
    '''    <div class="badge-card">
      <div class="badge-icon"><div class="sparkles"><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div></div><div class="badge-circle"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg></div></div>
      <h2 class="slide-heading" style="color:#fff">Stamp <span class="accent">Earned</span>!</h2>
      <p style="color:rgba(255,255,255,.7);font-size:1rem">Day 10: Supply Chain - Complete</p>
    </div>'''))
SL.append(slide(32,7,"slide-dark","<strong>Closing (30s):</strong> 'You completed ten lessons, Milton! Next: Problem Solving - when things go wrong, with conditionals. Congratulations and see you next week!' Encerre com energia.",
    '''    <div class="chapter-label">See You Next Time</div>
    <h2 class="slide-heading" style="color:#fff">Day 10 - <span class="accent">Complete</span></h2>
    <p style="color:rgba(255,255,255,.5);font-size:.92rem;margin-top:1rem">Next: Lesson 11 - Problem Solving</p>
    <p style="color:rgba(255,255,255,.4);font-size:.82rem;margin-top:.5rem">When Things Go Wrong - Conditionals</p>''',style="text-align:center"))

SLIDES=("<!-- ===== AULA 10 SLIDES ===== -->\n" + "\n".join(SL)).rstrip() + "\n\n</div><!-- /slides-container -->"

def splice(s,start,end,new):
    i=s.index(start); j=s.index(end,i)+len(end); return s[:i]+new+s[j:]
html=open(SRC,encoding='utf-8').read()
html=html.replace('| Aula 7 | Business English','| Aula 10 | Business English')
html=html.replace(
    '''<div class="stamp" id="stamp7" data-label="Numbers" style="background-image:url('https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=200&q=80')"></div>''',
    '''<div class="stamp" id="stamp7" data-label="Numbers" style="background-image:url('https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=200&q=80')"></div>
        <div class="stamp" id="stamp8" data-label="Review" style="background-image:url('https://images.unsplash.com/photo-1521737711867-e3b97375f902?w=200&q=80')"></div>
        <div class="stamp" id="stamp9" data-label="Contracts" style="background-image:url('https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=200&q=80')"></div>
        <div class="stamp" id="stamp10" data-label="Supply" style="background-image:url('%s?w=200&q=80')"></div>'''%COVER)
html=splice(html,'<div class="tab-content" id="tab-exercises">','</div><!-- /tab-exercises -->',PRECLASS)
html=splice(html,'<div class="tab-content" id="tab-inclass">','</div>\n\n<!-- ========== TAB 4',INCLASS_MENU+'\n\n<!-- ========== TAB 4')
html=splice(html,'<div class="tab-content" id="tab-complementary">','</div><!-- /container -->',COMPLEMENTARY)
html=splice(html,'<!-- ===== CHAPTER 1: THE DREAM (WARM-UP) ===== -->','</div><!-- /slides-container -->',SLIDES)
texts=set()
for m in re.finditer(r"speakText\('((?:[^'\\]|\\')*)'",html): texts.add(m.group(1).replace("\\'","'"))
for m in re.finditer(r'data-phrase="([^"]*)"',html): texts.add(m.group(1))
texts=sorted(texts)
am=",\n".join('    "%s": "/audio/milton-sayegh/%s"'%(t.replace('"','\\"'),fname(t)) for t in texts)
html=splice(html,'var audioMap = {','};','var audioMap = {\n'+am+'\n};')
open(OUT,'w',encoding='utf-8').write(html)
print("wrote",OUT,len(html))
ph=[{"key":t,"text":t,"file":fname(t),"voice":('ellen' if t in ELLEN else 'arthur')} for t in texts]
json.dump(ph,open(PHR,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
print("phrases",len(ph),"ellen",sum(1 for p in ph if p['voice']=='ellen'))
