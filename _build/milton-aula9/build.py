#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Milton Aula 9 - Contracts and Agreements (Past Simple). Scaffold = aula7
(canonical markers + REGRA 38). Auto-derives audioMap + phrases.json (REGRA 7)."""
import os, re, json
ROOT = '/home/dan/dev/work/better/wt-milton'
SRC = os.path.join(ROOT, 'public/professor/milton-sayegh-aula7.html')
OUT = os.path.join(ROOT, 'public/professor/milton-sayegh-aula9.html')
PHR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'phrases.json')
LESSON = 9
COVER = "https://images.unsplash.com/photo-1450101499163-c8848c66ca85"
IMG = COVER
ELLEN = {
    "Of course, Milton. I read it carefully last night.",
    "Yes. I noticed one clause about the delivery deadline. Did you discuss it?",
    "Excellent. Everything looks clear and well protected.",
    "The distributor accepted our terms.",
    "Both parties agreed on every clause.",
}
def fname(t):
    s=t.lower().replace("'","");s=re.sub(r"[^a-z0-9]+","_",s).strip("_");return s[:60].rstrip("_")+".mp3"

PRECLASS = '''<div class="tab-content" id="tab-exercises">

<div class="lesson-card open" id="ex-lesson-9">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('%(img)s?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Aula 09 - Pre-class</div>
      <h3>Contracts and Agreements</h3>
      <div class="lesson-desc">Legal Vocabulary &amp; the Past Simple</div>
      <div class="lesson-progress-mini">
        <div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="9" style="width:0%%"></div></div>
        <span class="mini-percent" data-lesson-pct="9">0%%</span>
      </div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <span class="badge badge-vocab">Vocabulary</span>
      <h3>Stage 1.1: Legal &amp; Contract Vocabulary</h3>
      <p>Click on each card to listen and learn. These 8 words are essential for contracts and agreements.</p>
      <div class="vocab-grid">
        <div class="vocab-card"><h4>Contract</h4><div class="vocab-def">A formal written agreement between two parties.</div><div class="vocab-ex">"We signed a <strong>contract</strong> with our US distributor."</div><button class="audio-btn" onclick="speakText('Contract',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
        <div class="vocab-card"><h4>Agreement</h4><div class="vocab-def">An arrangement that both sides accept.</div><div class="vocab-ex">"We reached an <strong>agreement</strong> after two meetings."</div><button class="audio-btn" onclick="speakText('Agreement',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
        <div class="vocab-card"><h4>Clause</h4><div class="vocab-def">A specific section or condition in a contract.</div><div class="vocab-ex">"The delivery <strong>clause</strong> protects both companies."</div><button class="audio-btn" onclick="speakText('Clause',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
        <div class="vocab-card"><h4>Terms</h4><div class="vocab-def">The conditions of an agreement.</div><div class="vocab-ex">"We agreed on the <strong>terms</strong> of payment."</div><button class="audio-btn" onclick="speakText('Terms',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
        <div class="vocab-card"><h4>Signature</h4><div class="vocab-def">Your name written to approve a document.</div><div class="vocab-ex">"The contract needs your <strong>signature</strong> here."</div><button class="audio-btn" onclick="speakText('Signature',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
        <div class="vocab-card"><h4>Party</h4><div class="vocab-def">A person or company in a contract.</div><div class="vocab-ex">"Both <strong>parties</strong> signed the same day."</div><button class="audio-btn" onclick="speakText('Party',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
        <div class="vocab-card"><h4>Obligation</h4><div class="vocab-def">Something you must do under the contract.</div><div class="vocab-ex">"Delivery on time is our main <strong>obligation</strong>."</div><button class="audio-btn" onclick="speakText('Obligation',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
        <div class="vocab-card"><h4>Breach</h4><div class="vocab-def">Breaking the terms of a contract.</div><div class="vocab-ex">"A late payment is a <strong>breach</strong> of the agreement."</div><button class="audio-btn" onclick="speakText('Breach',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
      </div>
    </div>

    <div class="exercise-section">
      <span class="badge badge-practice">Practice</span>
      <h3>Stage 1.2: Match the Words</h3>
      <p>Match each word to its definition.</p>
      <div class="match-grid" id="match-l9">
        <div class="match-row" data-answer="a formal written agreement"><span class="match-word">Contract</span><select onchange="checkMatch(this)"><option value="">Select...</option><option value="a section of a contract">a section of a contract</option><option value="a formal written agreement">a formal written agreement</option><option value="the conditions of a deal">the conditions of a deal</option><option value="breaking the terms">breaking the terms</option><option value="a person or company">a person or company</option></select></div>
        <div class="match-row" data-answer="a section of a contract"><span class="match-word">Clause</span><select onchange="checkMatch(this)"><option value="">Select...</option><option value="the conditions of a deal">the conditions of a deal</option><option value="a section of a contract">a section of a contract</option><option value="a formal written agreement">a formal written agreement</option><option value="a person or company">a person or company</option><option value="breaking the terms">breaking the terms</option></select></div>
        <div class="match-row" data-answer="the conditions of a deal"><span class="match-word">Terms</span><select onchange="checkMatch(this)"><option value="">Select...</option><option value="breaking the terms">breaking the terms</option><option value="a person or company">a person or company</option><option value="the conditions of a deal">the conditions of a deal</option><option value="a formal written agreement">a formal written agreement</option><option value="a section of a contract">a section of a contract</option></select></div>
        <div class="match-row" data-answer="a person or company"><span class="match-word">Party</span><select onchange="checkMatch(this)"><option value="">Select...</option><option value="a formal written agreement">a formal written agreement</option><option value="a person or company">a person or company</option><option value="a section of a contract">a section of a contract</option><option value="breaking the terms">breaking the terms</option><option value="the conditions of a deal">the conditions of a deal</option></select></div>
        <div class="match-row" data-answer="breaking the terms"><span class="match-word">Breach</span><select onchange="checkMatch(this)"><option value="">Select...</option><option value="a person or company">a person or company</option><option value="breaking the terms">breaking the terms</option><option value="the conditions of a deal">the conditions of a deal</option><option value="a section of a contract">a section of a contract</option><option value="a formal written agreement">a formal written agreement</option></select></div>
      </div>
      <button class="verify-all-btn" onclick="verifyAllMatches('match-l9')">Check Answers</button>
    </div>

    <div class="exercise-section">
      <span class="badge badge-grammar">Grammar</span>
      <h3>Stage 1.3: Grammar in Context</h3>
      <p>Read the text and answer the questions. Notice the Past Simple verbs.</p>
      <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:8px;padding:1.2rem;margin-bottom:1rem;font-size:.88rem;line-height:1.7;color:var(--text)">
        Last month, Milton <strong>signed</strong> an important contract with a US distributor. First, the two parties <strong>met</strong> in New York and <strong>discussed</strong> the main terms. Milton's lawyer <strong>reviewed</strong> every clause carefully. They <strong>agreed</strong> on the price, the delivery dates, and the payment terms. Then Milton <strong>sent</strong> the final version by email, and both parties <strong>signed</strong> it the same week. Nobody <strong>breached</strong> the agreement, and the first order <strong>arrived</strong> on time. It <strong>was</strong> the smoothest deal of the year.
      </div>
      <div class="quiz-item"><div class="quiz-question">1. What did Milton sign last month?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> A contract with a US distributor</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> A new office lease</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> An employment contract</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. Who reviewed every clause?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> The distributor</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Milton's lawyer</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> The bank</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. Did anyone breach the agreement?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> No, nobody breached it</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Yes, the distributor did</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Yes, Milton did</div></div></div>
    </div>

    <div class="exercise-section">
      <span class="badge badge-grammar">Grammar</span>
      <h3>Stage 1.4: Grammar Tip - The Past Simple</h3>
      <p>Use the Past Simple for completed actions in the past (a specific finished time).</p>
      <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:8px;padding:1.2rem;margin-bottom:1rem">
        <table class="curriculum-table" style="margin:0">
          <thead><tr><th>Form</th><th>Rule</th><th>Example</th></tr></thead>
          <tbody>
            <tr><td><strong>Regular (+)</strong></td><td>verb + <strong>-ed</strong></td><td>"We <strong>signed</strong> / reviewed / agreed."</td></tr>
            <tr><td><strong>Irregular (+)</strong></td><td>special past form</td><td>"send &rarr; <strong>sent</strong>, meet &rarr; met, make &rarr; made, pay &rarr; paid"</td></tr>
            <tr><td><strong>Negative (-)</strong></td><td><strong>did not (didn't)</strong> + base verb</td><td>"We <strong>didn't change</strong> the terms."</td></tr>
            <tr><td><strong>Question (?)</strong></td><td><strong>Did</strong> + subject + base verb</td><td>"<strong>Did</strong> you <strong>send</strong> the contract?"</td></tr>
          </tbody>
        </table>
        <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem;font-style:italic">After "did" / "didn't", always use the BASE verb (not the past form): "Did you <strong>send</strong>?" (not "Did you sent?").</p>
      </div>
    </div>

    <div class="exercise-section">
      <span class="badge badge-practice">Practice</span>
      <h3>Stage 1.5: Complete the Sentences</h3>
      <p>Fill in with the correct Past Simple form.</p>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"We <input class="blank-input" data-answer="signed" data-hint="Hint: regular past of 'sign'" data-phrase="We signed the contract yesterday." placeholder="___"> the contract yesterday."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button> <button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"The distributor <input class="blank-input" data-answer="accepted" data-hint="Hint: regular past of 'accept'" data-phrase="The distributor accepted our terms last week." placeholder="___"> our terms last week."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button> <button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"I <input class="blank-input" data-answer="sent" data-hint="Hint: irregular past of 'send'" data-phrase="I sent the email last night." placeholder="___"> the email last night."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button> <button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"They <input class="blank-input" data-answer="met" data-hint="Hint: irregular past of 'meet'" data-phrase="They met the lawyer on Monday." placeholder="___"> the lawyer on Monday."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button> <button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"We <input class="blank-input" data-answer="didn't change" data-alt="did not change" data-hint="Hint: negative past, 2 words" data-phrase="We didn't change the terms." placeholder="___"> the terms."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button> <button class="check-btn" onclick="checkBlank(this)">Check</button></div>
    </div>

    <div class="exercise-section">
      <span class="badge badge-order">Order</span>
      <h3>Stage 2: How the Deal Happened</h3>
      <p>Arrange the steps of the deal in the correct order.</p>
      <div class="order-container" id="order-l9">
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l9')"><span class="order-num">?</span><span class="order-text">"Our lawyer reviewed every clause."</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l9')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l9')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l9')"><span class="order-num">?</span><span class="order-text">"First, the two parties met in New York."</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l9')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l9')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l9')"><span class="order-num">?</span><span class="order-text">"Finally, both parties signed the contract."</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l9')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l9')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l9')"><span class="order-num">?</span><span class="order-text">"Then they discussed the main terms."</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l9')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l9')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l9')"><span class="order-num">?</span><span class="order-text">"Milton sent the final version by email."</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l9')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l9')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l9')">Check Order</button>
    </div>

    <div class="exercise-section">
      <span class="badge badge-speak">Speaking</span>
      <h3>Stage 3: Pronunciation Practice</h3>
      <p>Listen to each phrase, then record yourself. Notice the Past Simple endings.</p>
      <div class="speech-card" data-phrase="We signed a new contract last month."><div class="speech-phrase">"We signed a new contract last month."</div><div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Stop</button></div><div class="speech-result"></div></div>
      <div class="speech-card" data-phrase="I reviewed every clause carefully."><div class="speech-phrase">"I reviewed every clause carefully."</div><div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Stop</button></div><div class="speech-result"></div></div>
      <div class="speech-card" data-phrase="The two parties agreed on the terms."><div class="speech-phrase">"The two parties agreed on the terms."</div><div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Stop</button></div><div class="speech-result"></div></div>
      <div class="speech-card" data-phrase="We sent the final version yesterday."><div class="speech-phrase">"We sent the final version yesterday."</div><div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Stop</button></div><div class="speech-result"></div></div>
      <div class="speech-card" data-phrase="Did you send the signed copy?"><div class="speech-phrase">"Did you send the signed copy?"</div><div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Stop</button></div><div class="speech-result"></div></div>
    </div>

    <div class="exercise-section">
      <span class="badge badge-quiz">Quiz</span>
      <h3>Stage 4: Situational Quiz</h3>
      <p>Choose the best option for each situation.</p>
      <div class="quiz-item"><div class="quiz-question">1. You describe a completed action last week. Which is correct?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "We signed the contract last week."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "We sign the contract last week."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "We have signed last week."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. You ask a colleague about a past action. Which is correct?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "Did you send the contract?"</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Did you sent the contract?"</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "You did send the contract?"</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. You say a past action did NOT happen. Which is correct?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "We didn't change the terms."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "We didn't changed the terms."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "We not changed the terms."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">4. A late payment broke the contract conditions. How do you say it?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "The payment was a clause."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "The late payment was a breach of the contract."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "The payment signed the contract."</div></div></div>
    </div>

    <div class="exercise-section">
      <span class="badge badge-think">Reflection</span>
      <h3>Stage 5: Free Production</h3>
      <p>Record yourself speaking freely.</p>
      <div class="think-card">
        <div class="think-question">Describe the last important deal or contract you closed. Use the Past Simple: when you met the other party, what you discussed, what you agreed, and when you signed. Use at least two irregular verbs (sent, met, made, paid).</div>
        <div class="speech-controls">
          <button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Free Record</button>
          <button class="btn btn-stop" onclick="stopFreeRecording(this)">&#9632; Stop</button>
        </div>
        <div id="think-result-9"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card - Lesson 9</h4>
      <div class="survival-phrase"><span class="sp-num">1</span><span class="sp-en">Let me review the terms of the contract.</span><button class="btn btn-listen" onclick="speakText('Let me review the terms of the contract.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">2</span><span class="sp-en">We agreed on the main conditions.</span><button class="btn btn-listen" onclick="speakText('We agreed on the main conditions.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">3</span><span class="sp-en">Could you send me the signed copy?</span><button class="btn btn-listen" onclick="speakText('Could you send me the signed copy?',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">4</span><span class="sp-en">Both parties must respect the agreement.</span><button class="btn btn-listen" onclick="speakText('Both parties must respect the agreement.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">5</span><span class="sp-en">We signed the contract last week.</span><button class="btn btn-listen" onclick="speakText('We signed the contract last week.',this)">&#9835;</button></div>
    </div>

    <div style="margin-top:1.5rem;">
      <h4 style="font-family:'Cormorant Garamond',serif;font-size:1rem;color:var(--accent);margin-bottom:0.8rem;">Checklist - Aula 9</h4>
      <ul class="checklist" id="checklist-9">
        <li><input type="checkbox" onchange="toggleChecklist(this)"> I studied the 8 legal/contract words</li>
        <li><input type="checkbox" onchange="toggleChecklist(this)"> I completed the matching exercise</li>
        <li><input type="checkbox" onchange="toggleChecklist(this)"> I read the Grammar in Context text</li>
        <li><input type="checkbox" onchange="toggleChecklist(this)"> I reviewed the Grammar Tip (Past Simple)</li>
        <li><input type="checkbox" onchange="toggleChecklist(this)"> I completed the fill-in-the-blanks</li>
        <li><input type="checkbox" onchange="toggleChecklist(this)"> I ordered the steps of the deal</li>
        <li><input type="checkbox" onchange="toggleChecklist(this)"> I practiced pronunciation (5 phrases)</li>
        <li><input type="checkbox" onchange="toggleChecklist(this)"> I answered the situational quiz</li>
        <li><input type="checkbox" onchange="toggleChecklist(this)"> I recorded the free production</li>
      </ul>
    </div>

  </div><!-- /lesson-body -->
</div><!-- /lesson-card -->

</div><!-- /tab-exercises -->''' % {"img": IMG}

INCLASS_MENU = '''<div class="tab-content" id="tab-inclass">
<h3 style="font-family:'Cormorant Garamond',serif;margin-bottom:1rem;color:var(--text)">IN CLASS — Select Lesson</h3>
<div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" onclick="enterSlideMode();" onmouseover="this.style.borderColor='var(--accent)'" onmouseout="this.style.borderColor='rgba(200,200,190,.5)'">
  <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">09</div>
  <div><div style="font-weight:600;font-size:.95rem">Contracts and Agreements</div><div style="font-size:.8rem;color:var(--text-dim)">Legal Vocabulary &amp; the Past Simple — 32 slides</div></div>
</div>
</div>'''

COMPLEMENTARY = '''<div class="tab-content" id="tab-complementary">
<h3 style="font-family:'Cormorant Garamond',serif;margin-bottom:.5rem;color:var(--text)">Complementary Materials - Lesson 9</h3>
<p style="font-size:.82rem;color:var(--text-dim);margin-bottom:1rem">Topic: Contracts and Agreements. Pay attention to how people talk about completed actions (Past Simple) and contract language.</p>
<div class="media-grid">
  <div class="media-card-wrapper" data-media="l9-series">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb"><svg viewBox="0 0 24 24"><rect x="2" y="2" width="20" height="20" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><polygon points="10 8 16 12 10 16 10 8" fill="currentColor"/></svg></div>
      <div class="media-info">
        <div class="media-type">Series</div>
        <h5>Suits - Season 1, Episode 6 ("Tricks of the Trade")</h5>
        <p>The lawyers review contracts, discuss clauses and close deals. Listen for Past Simple narration of what happened ("we signed", "they agreed", "I sent") and contract vocabulary like terms, clause and breach.</p>
        <p class="media-tip">Tip: Watch with English audio + subtitles. Write down 5 Past Simple verbs (regular and irregular) you hear.</p>
      </div>
    </div>
  </div>
  <div class="media-card-wrapper" data-media="l9-podcast">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" fill="none" stroke="currentColor" stroke-width="2"/><polygon points="10 8 16 12 10 16 10 8" fill="currentColor"/></svg></div>
      <div class="media-info">
        <div class="media-type">Podcast</div>
        <h5>Business English Pod - Contracts &amp; Agreements (Legal English)</h5>
        <p>Teaches the exact language of contracts: terms, clauses, obligations and agreements, plus how to describe what happened in a deal using the Past Simple.</p>
        <p class="media-tip">Tip: Listen twice. The second time, pause and repeat the contract phrases out loud.</p>
        <a href="https://open.spotify.com/show/4nCHpl7GXuMu41Jn4xDLtH" target="_blank" rel="noopener" style="display:inline-block;margin-top:.5rem;font-size:.75rem;color:var(--accent);font-weight:600;text-decoration:none;border-bottom:1px solid var(--accent)">Listen on Spotify &#8599;</a>
      </div>
    </div>
  </div>
  <div class="media-card-wrapper" data-media="l9-youtube">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb"><svg viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3" fill="currentColor"/></svg></div>
      <div class="media-info">
        <div class="media-type">YouTube</div>
        <h5>Simple Past Tense Examples for Business English</h5>
        <p>A practical lesson with business examples of the Past Simple - exactly the structure you need to describe a signed deal or a completed negotiation.</p>
        <p class="media-tip">Tip: Watch with English subtitles. After each example, say one Past Simple sentence about your own business.</p>
        <a href="https://www.youtube.com/watch?v=dYE_kwb1WDQ" target="_blank" rel="noopener" style="display:inline-block;margin-top:.5rem;font-size:.75rem;color:var(--accent);font-weight:600;text-decoration:none;border-bottom:1px solid var(--accent)">Watch on YouTube &#8599;</a>
      </div>
    </div>
  </div>
</div>
</div>

</div><!-- /container -->'''

# ---- slides
def slide(n, phase, cls, teacher, inner, style=""):
    st=(' style="%s"'%style) if style else ""
    return ('<div class="slide %s" data-slide="%d" data-phase="%d" data-lesson="%d" data-teacher="%s"%s>\n  <div class="slide-inner">\n%s\n  </div>\n</div>\n'%(cls,n,phase,LESSON,teacher,st,inner))
def img_slide(n, phase, teacher, label, title, sub, imgurl):
    subp=('<p style="color:rgba(255,255,255,.6);font-size:1rem;margin-top:1rem">%s</p>'%sub) if sub else ""
    inner='    <div class="chapter-label">%s</div>\n    <h2 class="slide-title">%s</h2>\n    %s'%(label,title,subp)
    return ('<div class="slide slide-image" data-slide="%d" data-phase="%d" data-lesson="%d" data-teacher="%s" style="background-image:url(\'%s?w=1400&q=80\')">\n  <div class="slide-inner">\n%s\n  </div>\n</div>\n'%(n,phase,LESSON,teacher,imgurl,inner))
def audiobtn(t,v):
    return '<button class="audio-btn-sm" data-voice="%s" onclick="speakText(\'%s\',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg></button>'%(v,t)
def vcard(gid,c1,c2,svg,clue,word,d,ex):
    return ('      <div class="vocab-card-ic" onclick="this.classList.toggle(\'revealed\')">\n        <div class="vocab-front"><div class="vocab-icon"><svg width="48" height="48" viewBox="0 0 48 48"><defs><linearGradient id="%s" x1="0" y1="0" x2="1" y2="1"><stop offset="0%%" stop-color="%s"/><stop offset="100%%" stop-color="%s"/></linearGradient></defs><rect width="48" height="48" rx="10" fill="url(#%s)"/>%s</svg></div><div class="vocab-clue">%s</div></div>\n        <div class="vocab-back"><h4>%s</h4><div class="vocab-def-ic">%s</div><div class="vocab-ex-ic">%s</div><button class="audio-btn-sm" onclick="event.stopPropagation();speakText(\'%s\',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div>\n      </div>'%(gid,c1,c2,gid,svg,clue,word,d,ex,word))
def dline(did,sp,v,color,ini,bg,text,disp):
    return ('      <div class="dialogue-line" id="%s" data-speaker="%s" data-voice="%s" style="display:%s;gap:.8rem;padding:.8rem;background:rgba(255,255,255,.06);border-radius:8px%s">\n        <div style="width:36px;height:36px;border-radius:50%%;background:%s;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:.75rem;flex-shrink:0">%s</div>\n        <div><div class="dialogue-name" style="color:%s">%s</div><p style="color:rgba(255,255,255,.85);font-size:.88rem">"%s"</p></div>\n        %s\n      </div>'%(did,sp,v,disp,(";opacity:1" if disp=="flex" else ""),bg,ini,color,sp,text,audiobtn(text,v)))

doc='<rect x="15" y="12" width="18" height="24" rx="2" stroke="#fff" stroke-width="2" fill="none"/><path d="M19 18h10M19 23h10M19 28h6" stroke="#fff" stroke-width="2" stroke-linecap="round"/>'
hands='<path d="M14 24l6-4 4 3 6-5" stroke="#fff" stroke-width="2" fill="none" stroke-linecap="round"/><path d="M14 30h20" stroke="#fff" stroke-width="2" stroke-linecap="round"/>'
sect='<rect x="14" y="14" width="20" height="20" rx="2" stroke="#fff" stroke-width="2" fill="none"/><path d="M14 21h20" stroke="#fff" stroke-width="2"/>'
gear='<rect x="16" y="16" width="16" height="16" rx="2" stroke="#fff" stroke-width="2" fill="none"/><path d="M20 24h8" stroke="#fff" stroke-width="2" stroke-linecap="round"/>'
pen='<path d="M16 32l2-6 12-12 4 4-12 12-6 2z" stroke="#fff" stroke-width="2" fill="none" stroke-linejoin="round"/>'
people='<circle cx="19" cy="20" r="3" stroke="#fff" stroke-width="2" fill="none"/><circle cx="29" cy="20" r="3" stroke="#fff" stroke-width="2" fill="none"/><path d="M13 32c0-3 3-5 6-5s6 2 6 5M23 32c0-3 3-5 6-5s6 2 6 5" stroke="#fff" stroke-width="2" fill="none"/>'
shield='<path d="M24 13l9 4v7c0 6-5 9-9 11-4-2-9-5-9-11v-7z" stroke="#fff" stroke-width="2" fill="none"/>'
broken='<path d="M22 14l-4 10h6l-4 10" stroke="#fff" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'

SL=[]
SL.append(img_slide(1,1,"<strong>Cover (30s):</strong> Compartilhe a tela. 'Today we learn how to talk about contracts and agreements, and how to describe completed actions with the Past Simple.' Avance.",
    "Contracts &amp;","Contracts<br><span class=\"accent\">&amp; Agreements</span>","Lesson 9 - Legal Vocabulary &amp; the Past Simple",COVER))
SL.append(slide(2,1,"slide-dark","<strong>Quick Review (4 min):</strong> Retome a Aula 8 (revisao de tempos). Pergunte e Milton responde. Objetivo: reativar antes de focar no Past Simple.",
    '''    <div class="chapter-label">Quick Review - Lesson 8</div>
    <h2 class="slide-heading">Quick <span class="accent">Review</span></h2>
    <div style="display:flex;flex-direction:column;gap:1.2rem;margin-top:1rem;width:100%">
      <div style="border-left:3px solid var(--accent-light);padding-left:1rem"><p style="color:rgba(255,255,255,.9);font-size:.95rem;font-weight:600">"Tell me one thing you do every day at work." (Present Simple)</p></div>
      <div style="border-left:3px solid var(--accent-light);padding-left:1rem"><p style="color:rgba(255,255,255,.9);font-size:.95rem;font-weight:600">"What are you working on right now?" (Present Continuous)</p></div>
      <div style="border-left:3px solid var(--accent-light);padding-left:1rem"><p style="color:rgba(255,255,255,.9);font-size:.95rem;font-weight:600">"Today: how do we talk about a deal that already finished? That is the Past Simple."</p></div>
    </div>'''))
SL.append(slide(3,1,"slide-dark","<strong>Warm-up (3 min):</strong> Faca a pergunta. Milton conta livremente sobre um contrato real. Anote verbos no passado que ele usar (ou evitar) para trabalhar depois.",
    '''    <div class="chapter-label">Warm-up</div>
    <h2 class="slide-heading">When did you sign your <span class="accent">last contract</span>?</h2>
    <p style="color:rgba(255,255,255,.6);font-size:.92rem;margin-top:1rem">Think about: Who were the parties? What did you agree? Was it easy or difficult?</p>'''))
SL.append(slide(4,1,"slide-dark","<strong>Context (2 min):</strong> Introduza o cenario do dia: Milton fechou um contrato com um distribuidor americano. 'Today we will review that contract and tell its story in English.'",
    '''    <div class="chapter-label">Today's Mission</div>
    <h2 class="slide-heading">Review a <span class="accent">Distribution Contract</span></h2>
    <p style="color:rgba(255,255,255,.6);font-size:.92rem;margin-top:1rem">You closed a deal with a US distributor. Let's learn the words and tell the story.</p>'''))

SL.append(img_slide(5,2,"<strong>Transition (10s):</strong> 'Let us learn the words you need for contracts.' Avance.","Packing","Packing<br><span class=\"accent\">Words</span>","","https://images.unsplash.com/photo-1526628953301-3e589a6a8b74"))
SL.append(slide(6,2,"slide-dark","<strong>Vocab (3 min):</strong> Milton clica em cada card. Leia definicao + exemplo. Corrija pronuncia de: clause /klawz/, breach /breech/.",
    '''    <div class="chapter-label">Vocabulary</div>
    <h2 class="slide-heading">Click to <span class="accent">reveal</span></h2>
    <div class="vocab-grid-ic">
'''+vcard("gc1","#0d7377","#14b8a6",doc,"A formal written agreement","Contract","A formal written agreement between two parties.","\"We signed a contract with our distributor.\"")+"\n"
   +vcard("gc2","#2563eb","#60a5fa",hands,"An arrangement both accept","Agreement","An arrangement that both sides accept.","\"We reached an agreement after two meetings.\"")+"\n"
   +vcard("gc3","#7c3aed","#a78bfa",sect,"A section of a contract","Clause","A specific section or condition in a contract.","\"The delivery clause protects both sides.\"")+"\n"
   +vcard("gc4","#B8860B","#D4A84B",gear,"The conditions of a deal","Terms","The conditions of an agreement.","\"We agreed on the terms of payment.\"")+'''
    </div>
    <div class="vocab-counter">Click on the cards to reveal - 0 / 4 words</div>'''))
SL.append(slide(7,2,"slide-dark","<strong>Vocab (3 min):</strong> Mesma dinamica. Corrija pronuncia de: signature /SIG-nuh-cher/, obligation /ob-li-GAY-shun/.",
    '''    <div class="chapter-label">Vocabulary</div>
    <h2 class="slide-heading">4 more <span class="accent">words</span></h2>
    <div class="vocab-grid-ic">
'''+vcard("gc5","#059669","#34d399",pen,"Your name to approve","Signature","Your name written to approve a document.","\"The contract needs your signature here.\"")+"\n"
   +vcard("gc6","#0891b2","#67e8f9",people,"A person or company in a deal","Party","A person or company in a contract.","\"Both parties signed the same day.\"")+"\n"
   +vcard("gc7","#ea580c","#fb923c",shield,"Something you must do","Obligation","Something you must do under the contract.","\"On-time delivery is our main obligation.\"")+"\n"
   +vcard("gc8","#dc2626","#f87171",broken,"Breaking the terms","Breach","Breaking the terms of a contract.","\"A late payment is a breach of the agreement.\"")+'''
    </div>
    <div class="vocab-counter">Click on the cards to reveal - 0 / 4 words</div>'''))

SL.append(img_slide(8,3,"<strong>Transition (10s):</strong> 'Now the code - how to talk about finished actions: the Past Simple.' Avance.","The","The<br><span class=\"accent\">Code</span>","","https://images.unsplash.com/photo-1450101499163-c8848c66ca85"))
SL.append(slide(9,3,"slide-dark","<strong>Discovery (3 min):</strong> Leia cada frase. Pergunte: 'When did these actions happen - now or in the past?' Resposta: passado, terminado. Peca para Milton apontar os verbos.",
    '''    <div class="chapter-label">Grammar Discovery</div>
    <h2 class="slide-heading">Look at the <span class="accent">gold verbs</span></h2>
    <div style="display:flex;flex-direction:column;gap:1rem;margin-top:1.5rem;width:100%">
      <div style="padding:.8rem 1rem;background:rgba(255,255,255,.06);border-left:3px solid var(--accent);border-radius:0 8px 8px 0;color:rgba(255,255,255,.85);font-size:.95rem;">"We <strong style="color:var(--accent-light)">signed</strong> the contract last week."</div>
      <div style="padding:.8rem 1rem;background:rgba(255,255,255,.06);border-left:3px solid var(--accent);border-radius:0 8px 8px 0;color:rgba(255,255,255,.85);font-size:.95rem;">"They <strong style="color:var(--accent-light)">agreed</strong> on the terms."</div>
      <div style="padding:.8rem 1rem;background:rgba(255,255,255,.06);border-left:3px solid var(--accent);border-radius:0 8px 8px 0;color:rgba(255,255,255,.85);font-size:.95rem;">"I <strong style="color:var(--accent-light)">sent</strong> the final version."</div>
      <div style="padding:.8rem 1rem;background:rgba(255,255,255,.06);border-left:3px solid var(--accent);border-radius:0 8px 8px 0;color:rgba(255,255,255,.85);font-size:.95rem;">"We <strong style="color:var(--accent-light)">met</strong> in New York."</div>
    </div>
    <p style="color:var(--accent-light);font-size:1rem;font-weight:600;margin-top:1.5rem">All finished. Which end in -ed? Which are irregular?</p>'''))
SL.append(slide(10,3,"slide-dark","<strong>Rule (2 min):</strong> Clique em Reveal the Rule. Leia cada linha. Reforce: regular = -ed; irregular = forma propria; pergunta/negativo com 'did' + verbo base.",
    '''    <div class="chapter-label">Grammar Rule</div>
    <h2 class="slide-heading">The Past <span class="accent">Simple</span></h2>
    <button class="primary-btn" onclick="var box=this.nextElementSibling;box.classList.toggle('visible');this.textContent=box.classList.contains('visible')?'Hide the Rule':'Reveal the Rule'">Reveal the Rule</button>
    <div class="rule-box">
      <table class="grammar-table-ic">
        <thead><tr><th>Form</th><th>Pattern</th><th>Example</th></tr></thead>
        <tbody>
          <tr><td><strong>Regular +</strong></td><td>verb + -ed</td><td>signed, agreed, reviewed</td></tr>
          <tr><td><strong>Irregular +</strong></td><td>special form</td><td>send&rarr;sent, meet&rarr;met, pay&rarr;paid</td></tr>
          <tr><td><strong>Negative -</strong></td><td>didn't + base</td><td>"we didn't change"</td></tr>
          <tr><td><strong>Question ?</strong></td><td>Did + base</td><td>"Did you send?"</td></tr>
        </tbody>
      </table>
    </div>'''))
SL.append(slide(11,3,"slide-dark","<strong>Common Mistake (2 min):</strong> Mostre os pares. Pergunte qual esta certo (verde). Reforce: depois de 'did/didn't' usa-se o verbo BASE, nao a forma do passado.",
    '''    <div class="chapter-label">Common Mistake</div>
    <h2 class="slide-heading">After "did", use the <span class="accent">base verb</span></h2>
    <div style="display:flex;flex-direction:column;gap:1.5rem;margin-top:1.5rem;width:100%;max-width:540px">
      <div style="padding:1rem;background:rgba(220,38,38,.1);border:1px solid rgba(220,38,38,.3);border-radius:8px;display:flex;align-items:center;gap:.8rem"><span style="font-size:1.5rem;color:#f87171">&#10007;</span><span style="color:rgba(255,255,255,.85);font-size:.92rem">"<strong>Did</strong> you <strong>sent</strong> the contract?"</span></div>
      <div style="padding:1rem;background:rgba(22,163,74,.1);border:1px solid rgba(22,163,74,.3);border-radius:8px;display:flex;align-items:center;gap:.8rem"><span style="font-size:1.5rem;color:#4ade80">&#10003;</span><span style="color:rgba(255,255,255,.85);font-size:.92rem">"<strong>Did</strong> you <strong>send</strong> the contract?"</span></div>
    </div>
    <p style="color:rgba(255,255,255,.5);font-size:.82rem;margin-top:1.5rem;font-style:italic">The "did" already shows the past. The main verb stays in its base form.</p>'''))
SL.append(slide(12,3,"slide-dark","<strong>Practice (3 min):</strong> Milton completa oralmente. Clique para revelar. Respostas: 1=signed, 2=sent, 3=didn't change, 4=Did...meet.",
    '''    <div class="chapter-label">Grammar Practice</div>
    <h2 class="slide-heading">Complete the <span class="accent">sentence</span></h2>
    <div class="comp-questions">
      <div class="comp-q" onclick="this.querySelector('.q-answer').style.display=this.querySelector('.q-answer').style.display==='block'?'none':'block'"><div class="q-text">1. "We ___ (sign) the contract yesterday." (regular)</div><div class="q-answer">signed</div></div>
      <div class="comp-q" onclick="this.querySelector('.q-answer').style.display=this.querySelector('.q-answer').style.display==='block'?'none':'block'"><div class="q-text">2. "I ___ (send) the email last night." (irregular)</div><div class="q-answer">sent</div></div>
      <div class="comp-q" onclick="this.querySelector('.q-answer').style.display=this.querySelector('.q-answer').style.display==='block'?'none':'block'"><div class="q-text">3. "We ___ (not change) the terms." (negative)</div><div class="q-answer">didn't change</div></div>
      <div class="comp-q" onclick="this.querySelector('.q-answer').style.display=this.querySelector('.q-answer').style.display==='block'?'none':'block'"><div class="q-text">4. "___ you ___ (meet) the distributor?" (question)</div><div class="q-answer">Did you meet</div></div>
    </div>'''))

SL.append(img_slide(13,4,"<strong>Transition (10s):</strong> 'Let us look at a real contract.' Avance.","Getting","Getting<br><span class=\"accent\">There</span>","","https://images.unsplash.com/photo-1555421689-d68471e189f2"))
SL.append(slide(14,4,"slide-light","<strong>Contract (3 min):</strong> Leia o contrato com Milton. Para cada clausula, peca uma frase no passado: 'We signed this on...', 'Both parties agreed...'. Corrija o Past Simple.",
    '''    <div class="chapter-label">The Document</div>
    <h2 class="slide-heading" style="color:var(--text)">Distribution <span class="accent">Agreement</span></h2>
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:1.2rem;width:100%;max-width:540px;box-shadow:0 4px 16px rgba(0,0,0,.06)">
      <div style="font-size:.78rem;font-weight:700;color:var(--accent);text-transform:uppercase;letter-spacing:1px;margin-bottom:.8rem;text-align:center">Distribution Agreement</div>
      <div style="font-size:.85rem;color:var(--text);line-height:1.7">
        <p style="margin-bottom:.6rem"><strong>Parties:</strong> Sayegh Jewelry (Brazil) and Crown Imports (USA).</p>
        <p style="margin-bottom:.6rem"><strong>Clause 1 - Terms:</strong> Crown Imports buys 5,000 units per year.</p>
        <p style="margin-bottom:.6rem"><strong>Clause 2 - Delivery:</strong> Each order ships within 30 days.</p>
        <p style="margin-bottom:.6rem"><strong>Clause 3 - Payment:</strong> Payment is due 60 days after delivery.</p>
        <div style="display:flex;justify-content:space-between;margin-top:1rem;padding-top:.8rem;border-top:1px solid var(--border);font-size:.8rem;color:var(--text-mid)"><span>Signature: M. Sayegh</span><span>Date: signed last week</span></div>
      </div>
    </div>'''))
SL.append(slide(15,4,"slide-dark","<strong>Comprehension (2 min):</strong> Milton clica para revelar. Confirme que ele leu as clausulas corretamente.",
    '''    <div class="chapter-label">Comprehension</div>
    <h2 class="slide-heading">Read the <span class="accent">Contract</span></h2>
    <div class="comp-questions">
      <div class="comp-q" onclick="this.querySelector('.q-answer').style.display=this.querySelector('.q-answer').style.display==='block'?'none':'block'"><div class="q-text">1. Who are the two parties?</div><div class="q-answer">Sayegh Jewelry (Brazil) and Crown Imports (USA).</div></div>
      <div class="comp-q" onclick="this.querySelector('.q-answer').style.display=this.querySelector('.q-answer').style.display==='block'?'none':'block'"><div class="q-text">2. What does Clause 2 say?</div><div class="q-answer">Each order ships within 30 days.</div></div>
      <div class="comp-q" onclick="this.querySelector('.q-answer').style.display=this.querySelector('.q-answer').style.display==='block'?'none':'block'"><div class="q-text">3. When is payment due?</div><div class="q-answer">60 days after delivery.</div></div>
    </div>'''))
SL.append(slide(16,4,"slide-dark","<strong>Listening (3 min):</strong> Toque cada frase. Milton ouve e repete. Pergunte: regular ou irregular? Vozes alternadas Arthur/Ellen.",
    '''    <div class="chapter-label">Listening</div>
    <h2 class="slide-heading">Listen and <span class="accent">Identify</span></h2>
    <p style="color:rgba(255,255,255,.6);font-size:.88rem;margin-bottom:1.5rem">Regular or irregular past? Listen to each phrase.</p>
    <div style="display:flex;flex-direction:column;gap:1rem;width:100%">
      <div style="display:flex;align-items:center;gap:.8rem;padding:.8rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:8px"><span style="color:var(--accent-light);font-weight:700;min-width:1.5rem">1</span><span style="color:rgba(255,255,255,.85);flex:1;font-size:.92rem">"We signed the agreement last Friday."</span>'''+audiobtn("We signed the agreement last Friday.","arthur")+'''</div>
      <div style="display:flex;align-items:center;gap:.8rem;padding:.8rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:8px"><span style="color:var(--accent-light);font-weight:700;min-width:1.5rem">2</span><span style="color:rgba(255,255,255,.85);flex:1;font-size:.92rem">"The distributor accepted our terms."</span>'''+audiobtn("The distributor accepted our terms.","ellen")+'''</div>
      <div style="display:flex;align-items:center;gap:.8rem;padding:.8rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:8px"><span style="color:var(--accent-light);font-weight:700;min-width:1.5rem">3</span><span style="color:rgba(255,255,255,.85);flex:1;font-size:.92rem">"I sent the contract to our lawyer yesterday."</span>'''+audiobtn("I sent the contract to our lawyer yesterday.","arthur")+'''</div>
      <div style="display:flex;align-items:center;gap:.8rem;padding:.8rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:8px"><span style="color:var(--accent-light);font-weight:700;min-width:1.5rem">4</span><span style="color:rgba(255,255,255,.85);flex:1;font-size:.92rem">"Both parties agreed on every clause."</span>'''+audiobtn("Both parties agreed on every clause.","ellen")+'''</div>
    </div>'''))
SL.append(slide(17,4,"slide-dark","<strong>Dialogue (4 min):</strong> 'You review the signed contract with your legal counsel, Ms. Reed. Read line by line.' Clique Next Line. Milton le a parte dele. Corrija o Past Simple.",
    '''    <div class="chapter-label">Dialogue</div>
    <h2 class="slide-heading">Reviewing the <span class="accent">Contract</span></h2>
    <p style="color:rgba(255,255,255,.6);font-size:.88rem;margin-bottom:1rem">You discuss the signed contract with your legal counsel, Ms. Reed.</p>
    <div id="dialogueLines" style="display:flex;flex-direction:column;gap:.8rem;width:100%">
'''+dline("dl1","Milton (You)","arthur","var(--accent-light)","MS","var(--accent)","Good morning, Ms. Reed. Thank you for reviewing our distribution contract.","flex")+"\n"
   +dline("dl2","Ms. Reed","ellen","#7dd3fc","MR","#2563eb","Of course, Milton. I read it carefully last night.","none")+"\n"
   +dline("dl3","Milton (You)","arthur","var(--accent-light)","MS","var(--accent)","Last week, we agreed on the main terms and we signed the final version yesterday.","none")+"\n"
   +dline("dl4","Ms. Reed","ellen","#7dd3fc","MR","#2563eb","Yes. I noticed one clause about the delivery deadline. Did you discuss it?","none")+"\n"
   +dline("dl5","Milton (You)","arthur","var(--accent-light)","MS","var(--accent)","We discussed it and both parties accepted thirty days for each order.","none")+"\n"
   +dline("dl6","Ms. Reed","ellen","#7dd3fc","MR","#2563eb","Excellent. Everything looks clear and well protected.","none")+'''
    </div>
    <button class="primary-btn" style="margin-top:1rem" onclick="var lines=['dl2','dl3','dl4','dl5','dl6'];for(var i=0;i<lines.length;i++){var el=document.getElementById(lines[i]);if(el.style.display==='none'){el.style.display='flex';break}}">Next Line</button>'''))

SL.append(img_slide(18,5,"<strong>Transition (10s):</strong> 'Time to practice the Past Simple!' Avance.","More","More<br><span class=\"accent\">Practice</span>","","https://images.unsplash.com/photo-1497032628192-86f99bcd76bc"))
SL.append(slide(19,5,"slide-dark","<strong>Quick Fire (4 min):</strong> Uma situacao por vez. Milton responde antes de revelar.",
    '''    <div class="chapter-label">Quick Fire</div>
    <h2 class="slide-heading">Quick <span class="accent">Fire</span></h2>
    <div id="qf9" style="width:100%">
      <div class="challenge-card" id="qf9-1"><div style="font-size:.75rem;color:var(--accent-light);font-weight:700;margin-bottom:1rem">Challenge 1 / 4</div><p style="color:rgba(255,255,255,.85);font-size:.95rem;line-height:1.6;margin-bottom:1.5rem">Say that you finished a deal last week (completed action).</p><button class="primary-btn" id="qf9ShowBtn1" onclick="document.getElementById('qf9Answer1').style.display='block';this.style.display='none';document.getElementById('qf9NextBtn1').style.display='inline-flex'">Show Answer</button><div id="qf9Answer1" style="display:none;margin-top:1rem;padding:1rem;background:rgba(22,163,74,.1);border:1px solid rgba(22,163,74,.3);border-radius:8px;color:#4ade80;font-weight:600">"We closed the deal last week." / "We signed the contract last week."</div><button class="secondary-btn" id="qf9NextBtn1" style="display:none;margin-top:1rem" onclick="document.getElementById('qf9-1').style.display='none';document.getElementById('qf9-2').style.display='flex'">Next Question</button></div>
      <div class="challenge-card" id="qf9-2" style="display:none"><div style="font-size:.75rem;color:var(--accent-light);font-weight:700;margin-bottom:1rem">Challenge 2 / 4</div><p style="color:rgba(255,255,255,.85);font-size:.95rem;line-height:1.6;margin-bottom:1.5rem">Ask a colleague if they sent the contract (past question).</p><button class="primary-btn" id="qf9ShowBtn2" onclick="document.getElementById('qf9Answer2').style.display='block';this.style.display='none';document.getElementById('qf9NextBtn2').style.display='inline-flex'">Show Answer</button><div id="qf9Answer2" style="display:none;margin-top:1rem;padding:1rem;background:rgba(22,163,74,.1);border:1px solid rgba(22,163,74,.3);border-radius:8px;color:#4ade80;font-weight:600">"Did you send the contract?" - Did + base verb.</div><button class="secondary-btn" id="qf9PrevBtn2" style="margin-top:.5rem" onclick="document.getElementById('qf9-2').style.display='none';document.getElementById('qf9-1').style.display='flex'">Previous</button><button class="secondary-btn" id="qf9NextBtn2" style="display:none;margin-top:.5rem" onclick="document.getElementById('qf9-2').style.display='none';document.getElementById('qf9-3').style.display='flex'">Next Question</button></div>
      <div class="challenge-card" id="qf9-3" style="display:none"><div style="font-size:.75rem;color:var(--accent-light);font-weight:700;margin-bottom:1rem">Challenge 3 / 4</div><p style="color:rgba(255,255,255,.85);font-size:.95rem;line-height:1.6;margin-bottom:1.5rem">Say a past action did NOT happen (you did not change the price).</p><button class="primary-btn" id="qf9ShowBtn3" onclick="document.getElementById('qf9Answer3').style.display='block';this.style.display='none';document.getElementById('qf9NextBtn3').style.display='inline-flex'">Show Answer</button><div id="qf9Answer3" style="display:none;margin-top:1rem;padding:1rem;background:rgba(22,163,74,.1);border:1px solid rgba(22,163,74,.3);border-radius:8px;color:#4ade80;font-weight:600">"We didn't change the price." - didn't + base verb.</div><button class="secondary-btn" id="qf9PrevBtn3" style="margin-top:.5rem" onclick="document.getElementById('qf9-3').style.display='none';document.getElementById('qf9-2').style.display='flex'">Previous</button><button class="secondary-btn" id="qf9NextBtn3" style="display:none;margin-top:.5rem" onclick="document.getElementById('qf9-3').style.display='none';document.getElementById('qf9-4').style.display='flex'">Next Question</button></div>
      <div class="challenge-card" id="qf9-4" style="display:none"><div style="font-size:.75rem;color:var(--accent-light);font-weight:700;margin-bottom:1rem">Challenge 4 / 4</div><p style="color:rgba(255,255,255,.85);font-size:.95rem;line-height:1.6;margin-bottom:1.5rem">Use an irregular verb: you "send" became...?</p><button class="primary-btn" id="qf9ShowBtn4" onclick="document.getElementById('qf9Answer4').style.display='block';this.style.display='none'">Show Answer</button><div id="qf9Answer4" style="display:none;margin-top:1rem;padding:1rem;background:rgba(22,163,74,.1);border:1px solid rgba(22,163,74,.3);border-radius:8px;color:#4ade80;font-weight:600">sent - "I sent the documents." (send / met / made / paid are irregular)</div><button class="secondary-btn" style="margin-top:.5rem" onclick="document.getElementById('qf9-4').style.display='none';document.getElementById('qf9-3').style.display='flex'">Previous</button></div>
    </div>'''))
SL.append(slide(20,5,"slide-dark","<strong>Spot the Error (3 min):</strong> Milton clica para revelar erro e correcao. 1=signed, 2=Did...send (base), 3=didn't agree.",
    '''    <div class="chapter-label">Spot the Error</div>
    <h2 class="slide-heading">Find the <span class="accent">Mistake</span></h2>
    <div class="error-grid">
      <div class="error-card" onclick="this.classList.toggle('open')"><div class="error-sentence">"I <span class="wrong">sign</span> the contract yesterday."</div><div class="error-fix">Correct: "I <strong>signed</strong> the contract yesterday."</div></div>
      <div class="error-card" onclick="this.classList.toggle('open')"><div class="error-sentence">"<span class="wrong">Did you sent</span> the email?"</div><div class="error-fix">Correct: "<strong>Did you send</strong> the email?"</div></div>
      <div class="error-card" onclick="this.classList.toggle('open')"><div class="error-sentence">"We <span class="wrong">not agreed</span> on the price."</div><div class="error-fix">Correct: "We <strong>didn't agree</strong> on the price."</div></div>
    </div>'''))
SL.append(slide(21,5,"slide-dark","<strong>Delayed Error Correction (3 min):</strong> Anote erros reais de Milton e corrija ao vivo. Foque em: -ed regular, verbos irregulares, 'did + base'.",
    '''    <div class="chapter-label">Error Correction</div>
    <h2 class="slide-heading">Let's Fix <span class="accent">Together</span></h2>
    <div style="display:flex;flex-direction:column;gap:1rem;margin-top:1.5rem;width:100%">
      <div style="padding:1rem;background:rgba(220,38,38,.08);border:1px solid rgba(220,38,38,.2);border-radius:8px"><div style="font-size:.72rem;font-weight:700;color:#f87171;text-transform:uppercase;letter-spacing:1px;margin-bottom:.4rem">Error 1</div><div contenteditable="true" style="min-height:2rem;padding:.4rem;border-bottom:1px dashed rgba(255,255,255,.3);color:rgba(255,255,255,.85);font-size:.88rem;outline:none">Type the error here...</div></div>
      <div style="padding:1rem;background:rgba(22,163,74,.08);border:1px solid rgba(22,163,74,.2);border-radius:8px"><div style="font-size:.72rem;font-weight:700;color:#4ade80;text-transform:uppercase;letter-spacing:1px;margin-bottom:.4rem">Correction 1</div><div contenteditable="true" style="min-height:2rem;padding:.4rem;border-bottom:1px dashed rgba(255,255,255,.3);color:rgba(255,255,255,.85);font-size:.88rem;outline:none">Type the correction here...</div></div>
      <div style="padding:1rem;background:rgba(220,38,38,.08);border:1px solid rgba(220,38,38,.2);border-radius:8px"><div style="font-size:.72rem;font-weight:700;color:#f87171;text-transform:uppercase;letter-spacing:1px;margin-bottom:.4rem">Error 2</div><div contenteditable="true" style="min-height:2rem;padding:.4rem;border-bottom:1px dashed rgba(255,255,255,.3);color:rgba(255,255,255,.85);font-size:.88rem;outline:none">Type the error here...</div></div>
      <div style="padding:1rem;background:rgba(22,163,74,.08);border:1px solid rgba(22,163,74,.2);border-radius:8px"><div style="font-size:.72rem;font-weight:700;color:#4ade80;text-transform:uppercase;letter-spacing:1px;margin-bottom:.4rem">Correction 2</div><div contenteditable="true" style="min-height:2rem;padding:.4rem;border-bottom:1px dashed rgba(255,255,255,.3);color:rgba(255,255,255,.85);font-size:.88rem;outline:none">Type the correction here...</div></div>
    </div>'''))

SL.append(img_slide(22,6,"<strong>Transition (10s):</strong> 'Now it is your turn - from guided to free.' Avance.","Your","Your<br><span class=\"accent\">Turn</span>","From guided to free - tell the story of a deal","https://images.unsplash.com/photo-1556761175-5973dc0f32e7"))
SL.append(slide(23,6,"slide-dark","<strong>Role-play Guided (3 min):</strong> Milton conta a historia do contrato usando as keywords. Deve usar pelo menos 3 verbos no passado (1 irregular). Ajude se precisar.",
    '''    <div class="chapter-label">Role-play - Guided</div>
    <h2 class="slide-heading">Tell the <span class="accent">Deal Story</span></h2>
    <div class="roleplay-card"><div class="roleplay-scenario">Tell the story of how you closed the distribution deal. Use the keywords and at least 3 Past Simple verbs (include one irregular).</div><div style="margin-top:1rem;display:flex;flex-wrap:wrap;gap:.5rem"><span class="roleplay-kw">we met</span><span class="roleplay-kw">discussed the terms</span><span class="roleplay-kw">agreed on the price</span><span class="roleplay-kw">sent the contract</span><span class="roleplay-kw">signed last week</span></div></div>'''))
SL.append(slide(24,6,"slide-dark","<strong>Role-play Semi-free (3 min):</strong> Milton explica as clausulas principais do contrato com apoio minimo. Deve descrever obrigacoes e o que aconteceu.",
    '''    <div class="chapter-label">Role-play - Semi-free</div>
    <h2 class="slide-heading">Explain the <span class="accent">Contract</span></h2>
    <div class="roleplay-card"><div class="roleplay-scenario">Explain the main clauses of your contract to a colleague: the parties, the terms, the delivery and the payment. Say what each party agreed to do.</div><div style="margin-top:1rem;display:flex;flex-wrap:wrap;gap:.5rem"><span class="roleplay-kw">the parties</span><span class="roleplay-kw">clause / terms</span><span class="roleplay-kw">obligation</span></div></div>'''))
SL.append(slide(25,6,"slide-dark","<strong>Role-play Free (3 min):</strong> Milton conta sobre um contrato REAL do proprio negocio, sem apoio. Deve incluir: as partes, o que negociaram, o que assinaram e quando. Avalie fluencia e Past Simple.",
    '''    <div class="chapter-label">Role-play - Free</div>
    <h2 class="slide-heading">Your Real <span class="accent">Deal</span></h2>
    <div class="roleplay-card"><div class="roleplay-scenario">Tell your teacher about a REAL contract or agreement from your business. Include: the parties, what you negotiated, what you agreed, and when you signed. Use the Past Simple. No keywords this time.</div></div>'''))
SL.append(slide(26,6,"slide-dark","<strong>Oral Drill (3 min):</strong> Milton repete cada frase. Corrija pronuncia de: signed /SYND/, agreed /uh-GREED/, sent /sent/.",
    '''    <div class="chapter-label">Oral Drill</div>
    <h2 class="slide-heading">Repeat Each <span class="accent">Phrase</span></h2>
    <div style="display:flex;flex-direction:column;gap:1rem;margin-top:1.5rem;">
      <div style="padding:.8rem 1rem;background:rgba(255,255,255,.06);border-left:3px solid var(--accent);border-radius:0 8px 8px 0;color:rgba(255,255,255,.85);font-size:.95rem;">"We <strong>signed</strong> a new contract last month."</div>
      <div style="padding:.8rem 1rem;background:rgba(255,255,255,.06);border-left:3px solid var(--accent);border-radius:0 8px 8px 0;color:rgba(255,255,255,.85);font-size:.95rem;">"I <strong>reviewed</strong> every clause carefully."</div>
      <div style="padding:.8rem 1rem;background:rgba(255,255,255,.06);border-left:3px solid var(--accent);border-radius:0 8px 8px 0;color:rgba(255,255,255,.85);font-size:.95rem;">"The two parties <strong>agreed</strong> on the terms."</div>
      <div style="padding:.8rem 1rem;background:rgba(255,255,255,.06);border-left:3px solid var(--accent);border-radius:0 8px 8px 0;color:rgba(255,255,255,.85);font-size:.95rem;">"We <strong>sent</strong> the final version yesterday."</div>
      <div style="padding:.8rem 1rem;background:rgba(255,255,255,.06);border-left:3px solid var(--accent);border-radius:0 8px 8px 0;color:rgba(255,255,255,.85);font-size:.95rem;">"<strong>Did</strong> you <strong>send</strong> the signed copy?"</div>
    </div>'''))

SL.append(img_slide(27,7,"<strong>Transition (10s):</strong> 'Great work! Let us review what you learned.' Avance.","Wrapping","Wrapping<br><span class=\"accent\">Up</span>","","https://images.unsplash.com/photo-1521737604893-d14cc237f11d"))
SL.append(slide(28,7,"slide-light","<strong>Checklist (2 min):</strong> Milton clica cada checkbox. Quando todos marcados, a aula conta como concluida. Pergunte: 'Which past verb is hardest to remember?'",
    '''    <div class="chapter-label">What I Learned</div>
    <h2 class="slide-heading">Lesson 9 <span class="accent">Checklist</span></h2>
    <div class="check-grid">
      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div>I know 8 contract and legal words.</div>
      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div>I can form regular Past Simple verbs with -ed.</div>
      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div>I know key irregular past verbs (sent, met, made, paid).</div>
      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div>I can ask and answer past questions with "did".</div>
      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div>I can describe a contract and tell the story of a deal.</div>
    </div>'''))
SL.append(slide(29,7,"slide-dark","<strong>Feedback (3 min):</strong> De feedback personalizado. Pontos fortes e 1-2 areas a focar. Termine sempre positivo.",
    '''    <div class="chapter-label">Feedback</div>
    <h2 class="slide-heading">Teacher <span class="accent">Feedback</span></h2>
    <div style="display:flex;flex-direction:column;gap:1.2rem;margin-top:1.5rem;">
      <div style="padding:1rem;background:rgba(22,163,74,.1);border:1px solid rgba(22,163,74,.3);border-radius:8px;"><div style="color:#4ade80;font-weight:700;margin-bottom:.5rem;">Strengths</div><div contenteditable="true" style="color:rgba(255,255,255,.7);font-size:.9rem;min-height:2rem;outline:none;border-bottom:1px dashed rgba(255,255,255,.2);padding-bottom:.3rem">Note Milton's strong points here during the lesson.</div></div>
      <div style="padding:1rem;background:rgba(217,119,6,.1);border:1px solid rgba(217,119,6,.3);border-radius:8px;"><div style="color:#fbbf24;font-weight:700;margin-bottom:.5rem;">Areas to Improve</div><div contenteditable="true" style="color:rgba(255,255,255,.7);font-size:.9rem;min-height:2rem;outline:none;border-bottom:1px dashed rgba(255,255,255,.2);padding-bottom:.3rem">Note areas for improvement during the lesson.</div></div>
    </div>'''))
SL.append(slide(30,7,"slide-dark","<strong>Homework (1 min):</strong> DIGA ORALMENTE (nao mostrar escrito): '1. Complete the Pre-class for Lesson 9. 2. Read a sample contract clause in English. 3. Write 5 Past Simple sentences about your last deal. 4. Watch Suits S1E6.'",
    '''    <div class="chapter-label">Homework</div>
    <h2 class="slide-heading" style="color:#fff">Your <span class="accent">Mission</span></h2>
    <p style="color:rgba(255,255,255,.6);font-size:1rem;margin-top:1rem;">Your teacher will explain your homework now.</p>
    <div style="margin-top:2rem;padding:1rem;background:rgba(255,255,255,.06);border-radius:10px;display:inline-block"><svg viewBox="0 0 24 24" width="48" height="48" fill="none" stroke="rgba(255,255,255,.4)" stroke-width="1.5"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg></div>''',style="text-align:center"))
SL.append(slide(31,7,"slide-dark","<strong>Badge (1 min):</strong> Celebre! 'You earned your ninth stamp, Milton! You can now read contracts and talk about completed actions with confidence.' Confetti automatico.",
    '''    <div class="badge-card">
      <div class="badge-icon"><div class="sparkles"><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div></div><div class="badge-circle"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg></div></div>
      <h2 class="slide-heading" style="color:#fff">Stamp <span class="accent">Earned</span>!</h2>
      <p style="color:rgba(255,255,255,.7);font-size:1rem">Day 9: Contracts and Agreements - Complete</p>
    </div>'''))
SL.append(slide(32,7,"slide-dark","<strong>Closing (30s):</strong> 'Next lesson: Supply Chain - from Brazil to the U.S., with the Passive Voice. See you next week!' Encerre com energia.",
    '''    <div class="chapter-label">See You Next Time</div>
    <h2 class="slide-heading" style="color:#fff">Day 9 - <span class="accent">Complete</span></h2>
    <p style="color:rgba(255,255,255,.5);font-size:.92rem;margin-top:1rem">Next: Lesson 10 - Supply Chain</p>
    <p style="color:rgba(255,255,255,.4);font-size:.82rem;margin-top:.5rem">From Brazil to the U.S. - the Passive Voice</p>''',style="text-align:center"))

SLIDES = ("<!-- ===== AULA 9 SLIDES ===== -->\n" + "\n".join(SL)).rstrip() + "\n\n</div><!-- /slides-container -->"

# ---- assemble
def splice(s,start,end,new):
    i=s.index(start); j=s.index(end,i)+len(end); return s[:i]+new+s[j:]
html=open(SRC,encoding='utf-8').read()
html=html.replace('| Aula 7 | Business English','| Aula 9 | Business English')
# stamps: add 8 + 9 after stamp7
html=html.replace(
    '''<div class="stamp" id="stamp7" data-label="Numbers" style="background-image:url('https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=200&q=80')"></div>''',
    '''<div class="stamp" id="stamp7" data-label="Numbers" style="background-image:url('https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=200&q=80')"></div>
        <div class="stamp" id="stamp8" data-label="Review" style="background-image:url('https://images.unsplash.com/photo-1521737711867-e3b97375f902?w=200&q=80')"></div>
        <div class="stamp" id="stamp9" data-label="Contracts" style="background-image:url('%s?w=200&q=80')"></div>'''%COVER)
html=splice(html,'<div class="tab-content" id="tab-exercises">','</div><!-- /tab-exercises -->',PRECLASS)
html=splice(html,'<div class="tab-content" id="tab-inclass">','</div>\n\n<!-- ========== TAB 4',INCLASS_MENU+'\n\n<!-- ========== TAB 4')
html=splice(html,'<div class="tab-content" id="tab-complementary">','</div><!-- /container -->',COMPLEMENTARY)
html=splice(html,'<!-- ===== CHAPTER 1: THE DREAM (WARM-UP) ===== -->','</div><!-- /slides-container -->',SLIDES)
# audioMap derive
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
