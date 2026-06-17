#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build Milton Sayegh - Aula 8 (Review & Consolidation, Lessons 1-7).
Reuses the approved Aula 7 standalone as scaffold (CSS/JS/contrast/REGRA 38),
splices in authored Aula 8 content. Auto-derives audioMap + phrases.json from
the actual speakText()/data-phrase strings so coverage is 100% (REGRA 7).
"""
import os, re, json

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC_PROF = os.path.join(ROOT, 'public/professor/milton-sayegh-aula7.html')
OUT_PROF = os.path.join(ROOT, 'public/professor/milton-sayegh-aula8.html')
OUT_ALUNO = os.path.join(ROOT, 'public/aluno/milton-sayegh-aula8.html')
PHRASES_JSON = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'phrases.json')

IMG = "https://images.unsplash.com/photo-1521737711867-e3b97375f902"  # business team at table

# ---- voice map: default arthur (Milton, male student); ellen for female char / alternation
ELLEN = {
    "My pleasure, Milton. Thank you for the invitation.",
    "How long have you worked with this supplier?",
    "I am preparing the agenda for our next meeting.",
    "Could you send me the invoice by Friday?",
    "Impressive. Your operation is very well organized.",
}

def fname(text):
    s = text.lower()
    s = s.replace("'", "")
    s = re.sub(r"[^a-z0-9]+", "_", s).strip("_")
    return s[:60].rstrip("_") + ".mp3"

# =====================================================================
# CONTENT BLOCKS
# =====================================================================

PRECLASS = '''<div class="tab-content" id="tab-exercises">

<div class="lesson-card open" id="ex-lesson-8">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('%(img)s?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Aula 08 - Pre-class</div>
      <h3>Review and Consolidation</h3>
      <div class="lesson-desc">Lessons 1-7 Together - Tenses, Modals &amp; Comparisons</div>
      <div class="lesson-progress-mini">
        <div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="8" style="width:0%%"></div></div>
        <span class="mini-percent" data-lesson-pct="8">0%%</span>
      </div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <!-- STAGE 1.1: VOCABULARY REVIEW -->
    <div class="exercise-section">
      <span class="badge badge-vocab">Vocabulary</span>
      <h3>Stage 1.1: Vocabulary Review</h3>
      <p>These 8 words from Lessons 1-7 come back today. Click each card to listen and review.</p>
      <div class="vocab-grid">
        <div class="vocab-card"><h4>Supplier</h4><div class="vocab-def">A company that provides goods or materials to your business.</div><div class="vocab-ex">"We work with a trusted <strong>supplier</strong> in Italy."</div><button class="audio-btn" onclick="speakText('Supplier',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
        <div class="vocab-card"><h4>Client</h4><div class="vocab-def">A person or company that buys your products or services.</div><div class="vocab-ex">"Our biggest <strong>client</strong> is based in New York."</div><button class="audio-btn" onclick="speakText('Client',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
        <div class="vocab-card"><h4>Deal</h4><div class="vocab-def">A business agreement, especially about buying or selling.</div><div class="vocab-ex">"We closed a great <strong>deal</strong> at the trade show."</div><button class="audio-btn" onclick="speakText('Deal',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
        <div class="vocab-card"><h4>Agenda</h4><div class="vocab-def">A list of the topics to discuss in a meeting.</div><div class="vocab-ex">"The first item on the <strong>agenda</strong> is the budget."</div><button class="audio-btn" onclick="speakText('Agenda',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
        <div class="vocab-card"><h4>Deadline</h4><div class="vocab-def">The latest time by which something must be finished.</div><div class="vocab-ex">"The <strong>deadline</strong> for the order is Friday."</div><button class="audio-btn" onclick="speakText('Deadline',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
        <div class="vocab-card"><h4>Invoice</h4><div class="vocab-def">A document that lists products sold and the price to pay.</div><div class="vocab-ex">"Please send the <strong>invoice</strong> to our finance team."</div><button class="audio-btn" onclick="speakText('Invoice',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
        <div class="vocab-card"><h4>Launch</h4><div class="vocab-def">To introduce a new product to the market.</div><div class="vocab-ex">"We will <strong>launch</strong> the new collection in March."</div><button class="audio-btn" onclick="speakText('Launch',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
        <div class="vocab-card"><h4>Schedule</h4><div class="vocab-def">A plan that shows when things will happen.</div><div class="vocab-ex">"My <strong>schedule</strong> is full this week."</div><button class="audio-btn" onclick="speakText('Schedule',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
        <div class="vocab-card"><h4>Forecast</h4><div class="vocab-def">A prediction of future figures or results.</div><div class="vocab-ex">"The <strong>forecast</strong> for next quarter is positive."</div><button class="audio-btn" onclick="speakText('Forecast',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
      </div>
    </div>

    <!-- STAGE 1.2: MATCHING -->
    <div class="exercise-section">
      <span class="badge badge-practice">Practice</span>
      <h3>Stage 1.2: Match the Words</h3>
      <p>Match each word to its definition.</p>
      <div class="match-grid" id="match-l8">
        <div class="match-row" data-answer="a company that provides goods"><span class="match-word">Supplier</span><select onchange="checkMatch(this)"><option value="">Select...</option><option value="a business agreement">a business agreement</option><option value="a company that provides goods">a company that provides goods</option><option value="a list of meeting topics">a list of meeting topics</option><option value="a document listing prices">a document listing prices</option><option value="a person who buys from you">a person who buys from you</option></select></div>
        <div class="match-row" data-answer="a person who buys from you"><span class="match-word">Client</span><select onchange="checkMatch(this)"><option value="">Select...</option><option value="a list of meeting topics">a list of meeting topics</option><option value="a person who buys from you">a person who buys from you</option><option value="a company that provides goods">a company that provides goods</option><option value="a document listing prices">a document listing prices</option><option value="a business agreement">a business agreement</option></select></div>
        <div class="match-row" data-answer="a business agreement"><span class="match-word">Deal</span><select onchange="checkMatch(this)"><option value="">Select...</option><option value="a document listing prices">a document listing prices</option><option value="a person who buys from you">a person who buys from you</option><option value="a business agreement">a business agreement</option><option value="a list of meeting topics">a list of meeting topics</option><option value="a company that provides goods">a company that provides goods</option></select></div>
        <div class="match-row" data-answer="a list of meeting topics"><span class="match-word">Agenda</span><select onchange="checkMatch(this)"><option value="">Select...</option><option value="a company that provides goods">a company that provides goods</option><option value="a list of meeting topics">a list of meeting topics</option><option value="a business agreement">a business agreement</option><option value="a person who buys from you">a person who buys from you</option><option value="a document listing prices">a document listing prices</option></select></div>
        <div class="match-row" data-answer="a document listing prices"><span class="match-word">Invoice</span><select onchange="checkMatch(this)"><option value="">Select...</option><option value="a person who buys from you">a person who buys from you</option><option value="a document listing prices">a document listing prices</option><option value="a list of meeting topics">a list of meeting topics</option><option value="a business agreement">a business agreement</option><option value="a company that provides goods">a company that provides goods</option></select></div>
      </div>
      <button class="verify-all-btn" onclick="verifyAllMatches('match-l8')">Check Answers</button>
    </div>

    <!-- STAGE 1.3: GRAMMAR IN CONTEXT -->
    <div class="exercise-section">
      <span class="badge badge-grammar">Grammar</span>
      <h3>Stage 1.3: Grammar in Context</h3>
      <p>Read the text and answer the questions. Notice the different tenses from Lessons 1-7.</p>
      <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:8px;padding:1.2rem;margin-bottom:1rem;font-size:.88rem;line-height:1.7;color:var(--text)">
        Milton <strong>manages</strong> a luxury jewelry business in Sao Paulo. Every day, he <strong>works</strong> with suppliers and clients around the world. This week, his team <strong>is preparing</strong> a new product launch for the US market. "We <strong>have worked</strong> with our main supplier for over ten years," Milton says. "Last quarter <strong>was</strong> the best in our history, and our profit <strong>was higher than</strong> the year before. <strong>Could</strong> we do even better next year? I believe we can." Right now, Milton <strong>is reviewing</strong> the agenda for an important board meeting. He <strong>has already sent</strong> the invoices and confirmed the deadlines.
      </div>
      <div class="quiz-item"><div class="quiz-question">1. What does Milton do every day?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> He works with suppliers and clients</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> He travels to the US</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> He designs the products himself</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. How long has Milton worked with his main supplier?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> For one year</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> For over ten years</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> For six months</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. What is his team doing this week?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Preparing a new product launch</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Closing the company</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Hiring new staff</div></div></div>
    </div>

    <!-- STAGE 1.4: GRAMMAR TIP -->
    <div class="exercise-section">
      <span class="badge badge-grammar">Grammar</span>
      <h3>Stage 1.4: Grammar Tip - Tenses Review</h3>
      <p>Lessons 1-7 covered these key structures. Use the right one for the right situation.</p>
      <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:8px;padding:1.2rem;margin-bottom:1rem">
        <table class="curriculum-table" style="margin:0">
          <thead><tr><th>Structure</th><th>Use it for</th><th>Example</th></tr></thead>
          <tbody>
            <tr><td><strong>Present Simple</strong></td><td>routines &amp; facts</td><td>"I <strong>manage</strong> an export business."</td></tr>
            <tr><td><strong>Present Continuous</strong></td><td>now &amp; current projects</td><td>"We <strong>are launching</strong> a new line."</td></tr>
            <tr><td><strong>Present Perfect</strong></td><td>experience &amp; results</td><td>"I <strong>have worked</strong> here for 30 years."</td></tr>
            <tr><td><strong>Modals (could/would/should)</strong></td><td>polite proposals</td><td>"<strong>Could</strong> you send the invoice?"</td></tr>
            <tr><td><strong>Comparatives/Superlatives</strong></td><td>compare figures</td><td>"This was <strong>the best</strong> quarter."</td></tr>
          </tbody>
        </table>
        <p style="font-size:.82rem;color:var(--text-dim);margin-top:.8rem;font-style:italic">Reminder: Present Simple adds <strong>-s</strong> for he/she/it ("he works"). Present Perfect uses <strong>have/has + past participle</strong> ("have been", not "have went").</p>
      </div>
    </div>

    <!-- STAGE 1.5: FILL-IN-THE-BLANK -->
    <div class="exercise-section">
      <span class="badge badge-practice">Practice</span>
      <h3>Stage 1.5: Complete the Sentences</h3>
      <p>Fill in with the correct form. Think about which tense fits.</p>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"He <input class="blank-input" data-answer="manages" data-hint="Hint: Present Simple, he/she/it adds -s" data-phrase="He manages the export department." placeholder="___"> the export department."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button> <button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"Right now, we <input class="blank-input" data-answer="are expanding" data-hint="Hint: Present Continuous (be + -ing), 2 words" data-phrase="We are expanding into the US market." placeholder="___"> into the US market."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button> <button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"I <input class="blank-input" data-answer="have visited" data-hint="Hint: Present Perfect (have + past participle), 2 words" data-phrase="I have visited New York three times." placeholder="___"> New York three times."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button> <button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"You <input class="blank-input" data-answer="should" data-hint="Hint: modal of advice" data-phrase="You should confirm the order today." placeholder="___"> confirm the order today."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button> <button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"This is <input class="blank-input" data-answer="the most important" data-hint="Hint: superlative of a long adjective, 3 words" data-phrase="This is the most important deal of the year." placeholder="___"> deal of the year."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button> <button class="check-btn" onclick="checkBlank(this)">Check</button></div>
    </div>

    <!-- STAGE 2: ORDERING -->
    <div class="exercise-section">
      <span class="badge badge-order">Order</span>
      <h3>Stage 2: Open a Business Meeting</h3>
      <p>Arrange the opening of a meeting in the correct order.</p>
      <div class="order-container" id="order-l8">
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l8')"><span class="order-num">?</span><span class="order-text">"First, let's look at last quarter's results."</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l8')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l8')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l8')"><span class="order-num">?</span><span class="order-text">"Good morning, everyone. Thank you for coming."</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l8')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l8')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l8')"><span class="order-num">?</span><span class="order-text">"Finally, let's agree on the next steps."</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l8')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l8')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l8')"><span class="order-num">?</span><span class="order-text">"Let me share the agenda for today."</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l8')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l8')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l8')"><span class="order-num">?</span><span class="order-text">"Then, we will discuss the new launch."</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l8')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l8')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l8')">Check Order</button>
    </div>

    <!-- STAGE 3: PRONUNCIATION -->
    <div class="exercise-section">
      <span class="badge badge-speak">Speaking</span>
      <h3>Stage 3: Pronunciation Practice</h3>
      <p>Listen to each phrase, then record yourself. These review the tenses from Lessons 1-7.</p>
      <div class="speech-card" data-phrase="I manage a jewelry export business."><div class="speech-phrase">"I manage a jewelry export business."</div><div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Stop</button></div><div class="speech-result"></div></div>
      <div class="speech-card" data-phrase="We are launching a new collection this month."><div class="speech-phrase">"We are launching a new collection this month."</div><div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Stop</button></div><div class="speech-result"></div></div>
      <div class="speech-card" data-phrase="I have worked in this industry for thirty years."><div class="speech-phrase">"I have worked in this industry for thirty years."</div><div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Stop</button></div><div class="speech-result"></div></div>
      <div class="speech-card" data-phrase="Could you send me the contract by Friday?"><div class="speech-phrase">"Could you send me the contract by Friday?"</div><div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Stop</button></div><div class="speech-result"></div></div>
      <div class="speech-card" data-phrase="This was our best quarter ever."><div class="speech-phrase">"This was our best quarter ever."</div><div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Stop</button></div><div class="speech-result"></div></div>
    </div>

    <!-- STAGE 4: SITUATIONAL QUIZ -->
    <div class="exercise-section">
      <span class="badge badge-quiz">Quiz</span>
      <h3>Stage 4: Situational Quiz</h3>
      <p>Choose the best option for each situation from your business day.</p>
      <div class="quiz-item"><div class="quiz-question">1. You meet a new client at a trade show. What do you say?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "Nice to meet you. I'm Milton, from Sayegh Jewelry."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Me Milton. Jewelry."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "I am the Milton of jewelry."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. You describe what your company does. Which is correct?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "We design and export luxury jewelry."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "We is designing jewelry."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "We exports a jewelry."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. You want to propose a price politely in a negotiation. Which is best?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "Could we agree on a price of fifty dollars per unit?"</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "You give me fifty dollars."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Price is fifty, yes?"</div></div></div>
      <div class="quiz-item"><div class="quiz-question">4. You present your best-ever results to the board. Which phrase?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "This is gooder than before."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "This was our best quarter ever."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "This is the most best quarter."</div></div></div>
    </div>

    <!-- STAGE 5: FREE PRODUCTION -->
    <div class="exercise-section">
      <span class="badge badge-think">Reflection</span>
      <h3>Stage 5: Free Production</h3>
      <p>Record yourself speaking freely.</p>
      <div class="think-card">
        <div class="think-question">Describe a typical business day for you. Use at least three different structures from Lessons 1-7: a Present Simple fact, a Present Continuous current project, and a Present Perfect experience. Mention a client, a supplier, or a deal.</div>
        <div class="speech-controls">
          <button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Free Record</button>
          <button class="btn btn-stop" onclick="stopFreeRecording(this)">&#9632; Stop</button>
        </div>
        <div id="think-result-8"></div>
      </div>
    </div>

    <!-- SURVIVAL CARD -->
    <div class="survival-card">
      <h4>Survival Card - Lesson 8</h4>
      <div class="survival-phrase"><span class="sp-num">1</span><span class="sp-en">Let me walk you through our process.</span><button class="btn btn-listen" onclick="speakText('Let me walk you through our process.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">2</span><span class="sp-en">We have worked together for many years.</span><button class="btn btn-listen" onclick="speakText('We have worked together for many years.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">3</span><span class="sp-en">I am preparing the report now.</span><button class="btn btn-listen" onclick="speakText('I am preparing the report now.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">4</span><span class="sp-en">Could we schedule a meeting next week?</span><button class="btn btn-listen" onclick="speakText('Could we schedule a meeting next week?',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">5</span><span class="sp-en">This is the best option for both of us.</span><button class="btn btn-listen" onclick="speakText('This is the best option for both of us.',this)">&#9835;</button></div>
    </div>

    <!-- CHECKLIST -->
    <div style="margin-top:1.5rem;">
      <h4 style="font-family:'Cormorant Garamond',serif;font-size:1rem;color:var(--accent);margin-bottom:0.8rem;">Checklist - Aula 8</h4>
      <ul class="checklist" id="checklist-8">
        <li><input type="checkbox" onchange="toggleChecklist(this)"> I reviewed the 8 vocabulary words</li>
        <li><input type="checkbox" onchange="toggleChecklist(this)"> I completed the matching exercise</li>
        <li><input type="checkbox" onchange="toggleChecklist(this)"> I read the Grammar in Context text</li>
        <li><input type="checkbox" onchange="toggleChecklist(this)"> I reviewed the Grammar Tip (tenses review)</li>
        <li><input type="checkbox" onchange="toggleChecklist(this)"> I completed the fill-in-the-blanks</li>
        <li><input type="checkbox" onchange="toggleChecklist(this)"> I ordered the meeting opening</li>
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
  <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">08</div>
  <div><div style="font-weight:600;font-size:.95rem">Review and Consolidation</div><div style="font-size:.8rem;color:var(--text-dim)">Putting Lessons 1-7 Together — 32 slides</div></div>
</div>
</div>'''

COMPLEMENTARY = '''<div class="tab-content" id="tab-complementary">
<h3 style="font-family:'Cormorant Garamond',serif;margin-bottom:.5rem;color:var(--text)">Complementary Materials - Lesson 8</h3>
<p style="font-size:.82rem;color:var(--text-dim);margin-bottom:1rem">Topic: Review of Lessons 1-7. Watch and listen to how professionals combine tenses, modals and comparisons across a full business day.</p>
<div class="media-grid">
  <div class="media-card-wrapper" data-media="l8-series">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb"><svg viewBox="0 0 24 24"><rect x="2" y="2" width="20" height="20" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><polygon points="10 8 16 12 10 16 10 8" fill="currentColor"/></svg></div>
      <div class="media-info">
        <div class="media-type">Series</div>
        <h5>Suits - Season 1, Episode 1 ("Pilot")</h5>
        <p>A full business day at a law firm: introductions, negotiations, meetings and deals. Listen for the mix of Present Simple ("I work at..."), Present Perfect ("I've closed..."), and polite modals ("Could you...?") - all the structures from Lessons 1-7.</p>
        <p class="media-tip">Tip: Watch with English audio + English subtitles. Note one sentence in each tense (Simple, Continuous, Perfect).</p>
      </div>
    </div>
  </div>
  <div class="media-card-wrapper" data-media="l8-podcast">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" fill="none" stroke="currentColor" stroke-width="2"/><polygon points="10 8 16 12 10 16 10 8" fill="currentColor"/></svg></div>
      <div class="media-info">
        <div class="media-type">Podcast</div>
        <h5>Business English Pod - Business English for Meetings &amp; Negotiations</h5>
        <p>Reviews exactly the language of Lessons 1-7: opening a meeting, presenting an agenda, making proposals with modals, and comparing results. Perfect consolidation before moving on.</p>
        <p class="media-tip">Tip: Listen twice. The second time, pause and repeat the meeting and negotiation phrases out loud.</p>
        <a href="https://open.spotify.com/show/4nCHpl7GXuMu41Jn4xDLtH" target="_blank" rel="noopener" style="display:inline-block;margin-top:.5rem;font-size:.75rem;color:var(--accent);font-weight:600;text-decoration:none;border-bottom:1px solid var(--accent)">Listen on Spotify &#8599;</a>
      </div>
    </div>
  </div>
  <div class="media-card-wrapper" data-media="l8-youtube">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb"><svg viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3" fill="currentColor"/></svg></div>
      <div class="media-info">
        <div class="media-type">YouTube</div>
        <h5>English Tenses Review - Present Simple, Continuous &amp; Perfect</h5>
        <p>A clear review of the three present tenses you used in Lessons 1-7, with business examples. Great to consolidate when to use each one before Lesson 9.</p>
        <p class="media-tip">Tip: Watch with English subtitles. After each tense, say one sentence about your own business.</p>
        <a href="https://www.youtube.com/watch?v=jEQ7DnfQAk0" target="_blank" rel="noopener" style="display:inline-block;margin-top:.5rem;font-size:.75rem;color:var(--accent);font-weight:600;text-decoration:none;border-bottom:1px solid var(--accent)">Watch on YouTube &#8599;</a>
      </div>
    </div>
  </div>
</div>
</div>

</div><!-- /container -->'''

# ---------------------------------------------------------------- SLIDES
def slide(n, phase, cls, teacher, inner, style=""):
    st = (' style="%s"' % style) if style else ""
    return ('<div class="slide %s" data-slide="%d" data-phase="%d" data-lesson="8" data-teacher="%s"%s>\n'
            '  <div class="slide-inner">\n%s\n  </div>\n</div>\n') % (cls, n, phase, teacher, st, inner)

def img_slide(n, phase, teacher, label, title, sub, imgurl):
    subp = ('<p style="color:rgba(255,255,255,.6);font-size:1rem;margin-top:1rem">%s</p>' % sub) if sub else ""
    inner = ('    <div class="chapter-label">%s</div>\n    <h2 class="slide-title">%s</h2>\n    %s'
             % (label, title, subp))
    return ('<div class="slide slide-image" data-slide="%d" data-phase="%d" data-lesson="8" data-teacher="%s" style="background-image:url(\'%s?w=1400&q=80\')">\n'
            '  <div class="slide-inner">\n%s\n  </div>\n</div>\n') % (n, phase, teacher, imgurl, inner)

def audiobtn(text, voice):
    return ('<button class="audio-btn-sm" data-voice="%s" onclick="speakText(\'%s\',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg></button>' % (voice, text))

SL = []
# ---- CHAPTER 1: THE DREAM
SL.append(img_slide(1, 1, "<strong>Cover (30s):</strong> Compartilhe a tela. 'Today we review and put together everything from Lessons 1 to 7 - a full business day in English.' Avance.",
    "Review &amp;", "Review<br><span class=\"accent\">&amp; Consolidation</span>", "Lesson 8 - Putting Lessons 1-7 Together", IMG))

SL.append(slide(2, 1, "slide-dark", "<strong>Quick Review (4 min):</strong> Retome a Aula 7 (numeros e comparativos). Leia cada pergunta; Milton responde usando o vocabulario da aula passada. Objetivo: ativar o que ele ja sabe antes de revisar tudo.",
    '''    <div class="chapter-label">Quick Review - Lesson 7</div>
    <h2 class="slide-heading">Quick <span class="accent">Review</span> - Lesson 7</h2>
    <div style="display:flex;flex-direction:column;gap:1.2rem;margin-top:1rem;width:100%">
      <div style="border-left:3px solid var(--accent-light);padding-left:1rem">
        <p style="color:rgba(255,255,255,.9);font-size:.95rem;font-weight:600">"How do you compare this quarter to last year?"</p>
        <div class="starter-card"><div class="starter-label" style="color:var(--accent-light)">Comparative</div><div class="starter-text" style="color:rgba(255,255,255,.7)">"higher than, more profitable than ..."</div></div>
      </div>
      <div style="border-left:3px solid var(--accent-light);padding-left:1rem">
        <p style="color:rgba(255,255,255,.9);font-size:.95rem;font-weight:600">"How do you describe your best result of the year?"</p>
        <div class="starter-card"><div class="starter-label" style="color:#7dd3fc">Superlative</div><div class="starter-text" style="color:rgba(255,255,255,.7)">"the best, the most profitable ..."</div></div>
      </div>
      <div style="border-left:3px solid var(--accent-light);padding-left:1rem">
        <p style="color:rgba(255,255,255,.9);font-size:.95rem;font-weight:600">"Today we put together everything: introducing, describing, negotiating, presenting. Ready?"</p>
      </div>
    </div>'''))

SL.append(slide(3, 1, "slide-dark", "<strong>Review Map (3 min):</strong> Mostre o mapa das Aulas 1-7. Para cada aula, pergunte rapidamente: 'What do you remember?' Nao se aprofunde - apenas reative. Marque com Milton quais sao mais uteis para ele.",
    '''    <div class="chapter-label">Your Journey So Far</div>
    <h2 class="slide-heading">Lessons <span class="accent">1 to 7</span></h2>
    <div style="display:flex;flex-direction:column;gap:.7rem;margin-top:1rem;width:100%">
      <div style="display:flex;gap:.8rem;align-items:center;padding:.6rem .9rem;background:rgba(255,255,255,.06);border-radius:8px"><span style="color:var(--accent-light);font-weight:700;min-width:1.4rem">1</span><span style="color:rgba(255,255,255,.85);font-size:.9rem">Introducing yourself - Present Simple &amp; Continuous</span></div>
      <div style="display:flex;gap:.8rem;align-items:center;padding:.6rem .9rem;background:rgba(255,255,255,.06);border-radius:8px"><span style="color:var(--accent-light);font-weight:700;min-width:1.4rem">2</span><span style="color:rgba(255,255,255,.85);font-size:.9rem">Your business - products &amp; operations</span></div>
      <div style="display:flex;gap:.8rem;align-items:center;padding:.6rem .9rem;background:rgba(255,255,255,.06);border-radius:8px"><span style="color:var(--accent-light);font-weight:700;min-width:1.4rem">3</span><span style="color:rgba(255,255,255,.85);font-size:.9rem">Networking - small talk &amp; introductions</span></div>
      <div style="display:flex;gap:.8rem;align-items:center;padding:.6rem .9rem;background:rgba(255,255,255,.06);border-radius:8px"><span style="color:var(--accent-light);font-weight:700;min-width:1.4rem">4</span><span style="color:rgba(255,255,255,.85);font-size:.9rem">Negotiation - modals (could/would/should)</span></div>
      <div style="display:flex;gap:.8rem;align-items:center;padding:.6rem .9rem;background:rgba(255,255,255,.06);border-radius:8px"><span style="color:var(--accent-light);font-weight:700;min-width:1.4rem">5</span><span style="color:rgba(255,255,255,.85);font-size:.9rem">Board meetings - Present Perfect &amp; opinions</span></div>
      <div style="display:flex;gap:.8rem;align-items:center;padding:.6rem .9rem;background:rgba(255,255,255,.06);border-radius:8px"><span style="color:var(--accent-light);font-weight:700;min-width:1.4rem">6</span><span style="color:rgba(255,255,255,.85);font-size:.9rem">Email etiquette - linking words</span></div>
      <div style="display:flex;gap:.8rem;align-items:center;padding:.6rem .9rem;background:rgba(255,255,255,.06);border-radius:8px"><span style="color:var(--accent-light);font-weight:700;min-width:1.4rem">7</span><span style="color:rgba(255,255,255,.85);font-size:.9rem">Numbers &amp; data - comparatives &amp; superlatives</span></div>
    </div>'''))

SL.append(slide(4, 1, "slide-dark", "<strong>Warm-up (2 min):</strong> Faca a pergunta. Espere Milton responder livremente. Objetivo: ele refletir sobre o proprio progresso e escolher o que quer praticar mais.",
    '''    <div class="chapter-label">Warm-up</div>
    <h2 class="slide-heading">What was the <span class="accent">most useful</span> thing you learned?</h2>
    <p style="color:rgba(255,255,255,.6);font-size:.92rem;margin-top:1rem">Think about: Which skill do you use the most at work? Which one is still difficult?</p>'''))

# ---- CHAPTER 2: PACKING WORDS (vocab review)
SL.append(img_slide(5, 2, "<strong>Transition (10s):</strong> 'Let us review the key words from the last seven lessons.' Avance.",
    "Packing", "Packing<br><span class=\"accent\">Words</span>", "", "https://images.unsplash.com/photo-1450101499163-c8848c66ca85"))

def vcard(gid, color1, color2, svg_inner, clue, word, definition, example):
    return ('''      <div class="vocab-card-ic" onclick="this.classList.toggle('revealed')">
        <div class="vocab-front"><div class="vocab-icon"><svg width="48" height="48" viewBox="0 0 48 48"><defs><linearGradient id="%s" x1="0" y1="0" x2="1" y2="1"><stop offset="0%%" stop-color="%s"/><stop offset="100%%" stop-color="%s"/></linearGradient></defs><rect width="48" height="48" rx="10" fill="url(#%s)"/>%s</svg></div><div class="vocab-clue">%s</div></div>
        <div class="vocab-back"><h4>%s</h4><div class="vocab-def-ic">%s</div><div class="vocab-ex-ic">%s</div><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('%s',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div>
      </div>''' % (gid, color1, color2, gid, svg_inner, clue, word, definition, example, word))

box = '<rect x="13" y="14" width="22" height="20" rx="3" stroke="#fff" stroke-width="2" fill="none"/>'
truck = '<rect x="13" y="18" width="14" height="11" rx="1" stroke="#fff" stroke-width="2" fill="none"/><path d="M27 22h5l3 4v3h-8z" stroke="#fff" stroke-width="2" fill="none"/><circle cx="18" cy="31" r="2" fill="#fff"/><circle cx="31" cy="31" r="2" fill="#fff"/>'
person = '<circle cx="24" cy="19" r="5" stroke="#fff" stroke-width="2" fill="none"/><path d="M15 35c0-5 4-8 9-8s9 3 9 8" stroke="#fff" stroke-width="2" fill="none"/>'
hand = '<path d="M16 18l8-3 8 3M14 22h20v10H14z" stroke="#fff" stroke-width="2" fill="none"/>'
list_ic = '<path d="M16 16h16M16 22h16M16 28h10" stroke="#fff" stroke-width="2" stroke-linecap="round"/>'
clock = '<circle cx="24" cy="24" r="10" stroke="#fff" stroke-width="2" fill="none"/><path d="M24 18v6l4 3" stroke="#fff" stroke-width="2" stroke-linecap="round"/>'
doc = '<rect x="16" y="13" width="16" height="22" rx="2" stroke="#fff" stroke-width="2" fill="none"/><path d="M20 19h8M20 24h8M20 29h5" stroke="#fff" stroke-width="2" stroke-linecap="round"/>'
rocket = '<path d="M24 12c5 4 6 10 4 16l-4 4-4-4c-2-6-1-12 4-16z" stroke="#fff" stroke-width="2" fill="none"/><circle cx="24" cy="22" r="2" fill="#fff"/>'
cal = '<rect x="14" y="16" width="20" height="18" rx="2" stroke="#fff" stroke-width="2" fill="none"/><path d="M14 22h20M19 13v5M29 13v5" stroke="#fff" stroke-width="2" stroke-linecap="round"/>'

SL.append(slide(6, 2, "slide-dark", "<strong>Vocab Review (3 min):</strong> 'Click on each card to reveal the word.' Milton clica e relembra. Peca um exemplo proprio para cada palavra. Corrija pronuncia de: supplier /suh-PLY-er/, invoice /IN-voys/.",
    '''    <div class="chapter-label">Vocabulary Review</div>
    <h2 class="slide-heading">Click to <span class="accent">remember</span></h2>
    <div class="vocab-grid-ic">
''' + vcard("gb1","#0d7377","#14b8a6",truck,"A company that provides goods","Supplier","A company that provides goods or materials.","\"We work with a trusted supplier in Italy.\"") + "\n"
    + vcard("gb2","#2563eb","#60a5fa",person,"Someone who buys from you","Client","A person or company that buys your products.","\"Our biggest client is in New York.\"") + "\n"
    + vcard("gb3","#7c3aed","#a78bfa",hand,"A business agreement","Deal","A business agreement to buy or sell.","\"We closed a great deal at the trade show.\"") + "\n"
    + vcard("gb4","#B8860B","#D4A84B",list_ic,"A list of meeting topics","Agenda","A list of topics to discuss in a meeting.","\"The first item on the agenda is the budget.\"") + '''
    </div>
    <div class="vocab-counter">Click on the cards to reveal - 0 / 4 words</div>'''))

SL.append(slide(7, 2, "slide-dark", "<strong>Vocab Review (3 min):</strong> Mesma dinamica. Corrija pronuncia de: deadline /DED-line/, schedule /SKED-jool/ (US).",
    '''    <div class="chapter-label">Vocabulary Review</div>
    <h2 class="slide-heading">4 more <span class="accent">words</span></h2>
    <div class="vocab-grid-ic">
''' + vcard("gb5","#dc2626","#f87171",clock,"The last time to finish","Deadline","The latest time something must be finished.","\"The deadline for the order is Friday.\"") + "\n"
    + vcard("gb6","#ea580c","#fb923c",doc,"A document with prices","Invoice","A document listing products sold and the price.","\"Please send the invoice to finance.\"") + "\n"
    + vcard("gb7","#059669","#34d399",rocket,"To introduce a new product","Launch","To introduce a new product to the market.","\"We will launch the new line in March.\"") + "\n"
    + vcard("gb8","#0891b2","#67e8f9",cal,"A plan of when things happen","Schedule","A plan that shows when things will happen.","\"My schedule is full this week.\"") + '''
    </div>
    <div class="vocab-counter">Click on the cards to reveal - 0 / 4 words</div>'''))

# ---- CHAPTER 3: THE CODE (grammar review)
SL.append(img_slide(8, 3, "<strong>Transition (10s):</strong> 'Now let us review the grammar code - the tenses you use every day.' Avance.",
    "The", "The<br><span class=\"accent\">Code</span>", "", "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40"))

SL.append(slide(9, 3, "slide-dark", "<strong>Discovery (3 min):</strong> Leia cada frase com Milton. Pergunte: 'Which tense is each sentence?' Resposta: 1=Present Simple, 2=Present Continuous, 3=Present Perfect, 4=modal. Se ele nao lembrar, de dicas.",
    '''    <div class="chapter-label">Grammar Discovery</div>
    <h2 class="slide-heading">Which <span class="accent">tense</span> is each?</h2>
    <div style="display:flex;flex-direction:column;gap:1rem;margin-top:1.5rem;width:100%">
      <div style="padding:.8rem 1rem;background:rgba(255,255,255,.06);border-left:3px solid var(--accent);border-radius:0 8px 8px 0;color:rgba(255,255,255,.85);font-size:.95rem;">"I <strong style="color:var(--accent-light)">manage</strong> a jewelry business."</div>
      <div style="padding:.8rem 1rem;background:rgba(255,255,255,.06);border-left:3px solid var(--accent);border-radius:0 8px 8px 0;color:rgba(255,255,255,.85);font-size:.95rem;">"We <strong style="color:var(--accent-light)">are launching</strong> a new collection."</div>
      <div style="padding:.8rem 1rem;background:rgba(255,255,255,.06);border-left:3px solid var(--accent);border-radius:0 8px 8px 0;color:rgba(255,255,255,.85);font-size:.95rem;">"I <strong style="color:var(--accent-light)">have worked</strong> here for 30 years."</div>
      <div style="padding:.8rem 1rem;background:rgba(255,255,255,.06);border-left:3px solid var(--accent);border-radius:0 8px 8px 0;color:rgba(255,255,255,.85);font-size:.95rem;">"<strong style="color:var(--accent-light)">Could</strong> you send me the invoice?"</div>
    </div>
    <p style="color:var(--accent-light);font-size:1rem;font-weight:600;margin-top:1.5rem">Routine, now, experience, or polite request?</p>'''))

SL.append(slide(10, 3, "slide-dark", "<strong>Rule (2 min):</strong> Clique em Reveal the Rule. Leia cada linha com Milton. Para cada estrutura, peca uma frase sobre o negocio dele.",
    '''    <div class="chapter-label">Grammar Rule</div>
    <h2 class="slide-heading">Tenses <span class="accent">Review</span></h2>
    <button class="primary-btn" onclick="var box=this.nextElementSibling;box.classList.toggle('visible');this.textContent=box.classList.contains('visible')?'Hide the Rule':'Reveal the Rule'">Reveal the Rule</button>
    <div class="rule-box">
      <table class="grammar-table-ic">
        <thead><tr><th>Structure</th><th>Use</th><th>Example</th></tr></thead>
        <tbody>
          <tr><td><strong>Present Simple</strong></td><td>routines</td><td>"I manage / he manages"</td></tr>
          <tr><td><strong>Present Continuous</strong></td><td>now</td><td>"we are launching"</td></tr>
          <tr><td><strong>Present Perfect</strong></td><td>experience</td><td>"I have worked"</td></tr>
          <tr><td><strong>Modals</strong></td><td>proposals</td><td>"could / would / should"</td></tr>
        </tbody>
      </table>
    </div>'''))

SL.append(slide(11, 3, "slide-dark", "<strong>Common Mistake (2 min):</strong> Mostre os dois pares. Pergunte: 'Which one is correct?' Resposta: o verde. Reforce: he/she/it adiciona -s; Present Perfect usa 'been', nao 'went'.",
    '''    <div class="chapter-label">Common Mistakes</div>
    <h2 class="slide-heading">Spot the <span class="accent">Fix</span></h2>
    <div style="display:flex;flex-direction:column;gap:1.5rem;margin-top:1.5rem;width:100%;max-width:560px">
      <div style="padding:1rem;background:rgba(220,38,38,.1);border:1px solid rgba(220,38,38,.3);border-radius:8px;display:flex;align-items:center;gap:.8rem">
        <span style="font-size:1.5rem;color:#f87171">&#10007;</span>
        <span style="color:rgba(255,255,255,.85);font-size:.92rem">"He <strong>work</strong> with suppliers." &rarr; "He <strong>works</strong> with suppliers."</span>
      </div>
      <div style="padding:1rem;background:rgba(220,38,38,.1);border:1px solid rgba(220,38,38,.3);border-radius:8px;display:flex;align-items:center;gap:.8rem">
        <span style="font-size:1.5rem;color:#f87171">&#10007;</span>
        <span style="color:rgba(255,255,255,.85);font-size:.92rem">"I have <strong>went</strong> to New York." &rarr; "I have <strong>been</strong> to New York."</span>
      </div>
    </div>
    <p style="color:rgba(255,255,255,.5);font-size:.82rem;margin-top:1.5rem;font-style:italic">he/she/it + -s in the Present Simple. Present Perfect = have/has + past participle.</p>'''))

SL.append(slide(12, 3, "slide-dark", "<strong>Practice (3 min):</strong> Milton completa cada frase oralmente. Clique para revelar. Respostas: 1=check, 2=are preparing, 3=have worked, 4=better than.",
    '''    <div class="chapter-label">Grammar Practice</div>
    <h2 class="slide-heading">Complete the <span class="accent">sentence</span></h2>
    <div class="comp-questions">
      <div class="comp-q" onclick="this.querySelector('.q-answer').style.display=this.querySelector('.q-answer').style.display==='block'?'none':'block'">
        <div class="q-text">1. "Every day, I ___ (check) my emails." (routine)</div>
        <div class="q-answer">check</div>
      </div>
      <div class="comp-q" onclick="this.querySelector('.q-answer').style.display=this.querySelector('.q-answer').style.display==='block'?'none':'block'">
        <div class="q-text">2. "Right now, we ___ (prepare) the launch." (now)</div>
        <div class="q-answer">are preparing</div>
      </div>
      <div class="comp-q" onclick="this.querySelector('.q-answer').style.display=this.querySelector('.q-answer').style.display==='block'?'none':'block'">
        <div class="q-text">3. "I ___ (work) here since 1995." (experience)</div>
        <div class="q-answer">have worked</div>
      </div>
      <div class="comp-q" onclick="this.querySelector('.q-answer').style.display=this.querySelector('.q-answer').style.display==='block'?'none':'block'">
        <div class="q-text">4. "This deal is ___ (good) the last one." (compare)</div>
        <div class="q-answer">better than</div>
      </div>
    </div>'''))

# ---- CHAPTER 4: GETTING THERE (context)
SL.append(img_slide(13, 4, "<strong>Transition (10s):</strong> 'Let us look at a real business day - Milton's schedule.' Avance.",
    "Getting", "Getting<br><span class=\"accent\">There</span>", "", "https://images.unsplash.com/photo-1497032628192-86f99bcd76bc"))

SL.append(slide(14, 4, "slide-light", "<strong>Schedule (3 min):</strong> Leia a agenda com Milton. Para cada item, peca uma frase usando o tempo verbal certo: 'At 9 I have a supplier call', 'I am meeting a client at 11'. Corrija os tempos.",
    '''    <div class="chapter-label">A Full Business Day</div>
    <h2 class="slide-heading" style="color:var(--text)">Milton's <span class="accent">Schedule</span></h2>
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:1.2rem;width:100%;max-width:520px;box-shadow:0 4px 16px rgba(0,0,0,.06)">
      <div style="font-size:.78rem;font-weight:700;color:var(--accent);text-transform:uppercase;letter-spacing:1px;margin-bottom:.8rem">Tuesday - Sayegh Jewelry</div>
      <div style="display:flex;flex-direction:column;gap:.6rem;font-size:.9rem;color:var(--text)">
        <div style="display:flex;gap:1rem;padding-bottom:.5rem;border-bottom:1px solid var(--border)"><strong style="color:var(--accent);min-width:3.4rem">09:00</strong><span>Call the supplier about the new order</span></div>
        <div style="display:flex;gap:1rem;padding-bottom:.5rem;border-bottom:1px solid var(--border)"><strong style="color:var(--accent);min-width:3.4rem">11:00</strong><span>Meet a client to discuss the deal</span></div>
        <div style="display:flex;gap:1rem;padding-bottom:.5rem;border-bottom:1px solid var(--border)"><strong style="color:var(--accent);min-width:3.4rem">14:00</strong><span>Board meeting - present the quarter results</span></div>
        <div style="display:flex;gap:1rem"><strong style="color:var(--accent);min-width:3.4rem">16:00</strong><span>Send follow-up emails and invoices</span></div>
      </div>
    </div>'''))

SL.append(slide(15, 4, "slide-dark", "<strong>Comprehension (2 min):</strong> Milton clica em cada pergunta para revelar a resposta. Confirme que ele leu a agenda corretamente.",
    '''    <div class="chapter-label">Comprehension</div>
    <h2 class="slide-heading">Read the <span class="accent">Schedule</span></h2>
    <div class="comp-questions">
      <div class="comp-q" onclick="this.querySelector('.q-answer').style.display=this.querySelector('.q-answer').style.display==='block'?'none':'block'">
        <div class="q-text">1. What does Milton do at 9:00?</div>
        <div class="q-answer">He calls the supplier about the new order.</div>
      </div>
      <div class="comp-q" onclick="this.querySelector('.q-answer').style.display=this.querySelector('.q-answer').style.display==='block'?'none':'block'">
        <div class="q-text">2. When is the board meeting?</div>
        <div class="q-answer">At 14:00 - he presents the quarter results.</div>
      </div>
      <div class="comp-q" onclick="this.querySelector('.q-answer').style.display=this.querySelector('.q-answer').style.display==='block'?'none':'block'">
        <div class="q-text">3. What does he do at the end of the day?</div>
        <div class="q-answer">He sends follow-up emails and invoices.</div>
      </div>
    </div>'''))

SL.append(slide(16, 4, "slide-dark", "<strong>Listening (3 min):</strong> Toque cada frase. Milton ouve e repete. Para cada uma pergunte: 'Which tense is this?'. Vozes alternadas Arthur/Ellen.",
    '''    <div class="chapter-label">Listening</div>
    <h2 class="slide-heading">Listen and <span class="accent">Identify</span></h2>
    <p style="color:rgba(255,255,255,.6);font-size:.88rem;margin-bottom:1.5rem">Which tense do you hear? Listen to each phrase.</p>
    <div style="display:flex;flex-direction:column;gap:1rem;width:100%">
      <div style="display:flex;align-items:center;gap:.8rem;padding:.8rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:8px">
        <span style="color:var(--accent-light);font-weight:700;min-width:1.5rem">1</span>
        <span style="color:rgba(255,255,255,.85);flex:1;font-size:.92rem">"We supply jewelry to clients in the United States."</span>
        ''' + audiobtn("We supply jewelry to clients in the United States.", "arthur") + '''
      </div>
      <div style="display:flex;align-items:center;gap:.8rem;padding:.8rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:8px">
        <span style="color:var(--accent-light);font-weight:700;min-width:1.5rem">2</span>
        <span style="color:rgba(255,255,255,.85);flex:1;font-size:.92rem">"I am preparing the agenda for our next meeting."</span>
        ''' + audiobtn("I am preparing the agenda for our next meeting.", "ellen") + '''
      </div>
      <div style="display:flex;align-items:center;gap:.8rem;padding:.8rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:8px">
        <span style="color:var(--accent-light);font-weight:700;min-width:1.5rem">3</span>
        <span style="color:rgba(255,255,255,.85);flex:1;font-size:.92rem">"We have worked with this supplier for ten years."</span>
        ''' + audiobtn("We have worked with this supplier for ten years.", "arthur") + '''
      </div>
      <div style="display:flex;align-items:center;gap:.8rem;padding:.8rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:8px">
        <span style="color:var(--accent-light);font-weight:700;min-width:1.5rem">4</span>
        <span style="color:rgba(255,255,255,.85);flex:1;font-size:.92rem">"Could you send me the invoice by Friday?"</span>
        ''' + audiobtn("Could you send me the invoice by Friday?", "ellen") + '''
      </div>
    </div>'''))

# dialogue (Milton arthur + Ms. Whitman ellen)
def dline(did, speaker, voice, color, initials, bg, text, display):
    return ('''      <div class="dialogue-line" id="%s" data-speaker="%s" data-voice="%s" style="display:%s;gap:.8rem;padding:.8rem;background:rgba(255,255,255,.06);border-radius:8px%s">
        <div style="width:36px;height:36px;border-radius:50%%;background:%s;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:.75rem;flex-shrink:0">%s</div>
        <div><div class="dialogue-name" style="color:%s">%s</div><p style="color:rgba(255,255,255,.85);font-size:.88rem">"%s"</p></div>
        %s
      </div>''' % (did, speaker, voice, display, (";opacity:1" if display=="flex" else ""), bg, initials, color, speaker, text, audiobtn(text, voice)))

SL.append(slide(17, 4, "slide-dark", "<strong>Dialogue (4 min):</strong> 'Milton, your investor Ms. Whitman is visiting your office. Read it line by line.' Clique Next Line. Milton le a parte dele em voz alta. Corrija os tempos verbais.",
    '''    <div class="chapter-label">Dialogue</div>
    <h2 class="slide-heading">Hosting <span class="accent">a Visit</span></h2>
    <p style="color:rgba(255,255,255,.6);font-size:.88rem;margin-bottom:1rem">Ms. Whitman visits your office for a tour.</p>
    <div id="dialogueLines" style="display:flex;flex-direction:column;gap:.8rem;width:100%">
''' + dline("dl1","Milton (You)","arthur","var(--accent-light)","MS","var(--accent)","Good morning, Ms. Whitman. Thank you for coming to our office today.","flex") + "\n"
    + dline("dl2","Ms. Whitman","ellen","#7dd3fc","IW","#2563eb","My pleasure, Milton. Thank you for the invitation.","none") + "\n"
    + dline("dl3","Milton (You)","arthur","var(--accent-light)","MS","var(--accent)","We work with suppliers in three countries. Right now, we are launching a new collection.","none") + "\n"
    + dline("dl4","Ms. Whitman","ellen","#7dd3fc","IW","#2563eb","How long have you worked with this supplier?","none") + "\n"
    + dline("dl5","Milton (You)","arthur","var(--accent-light)","MS","var(--accent)","We have worked with our main supplier for over ten years.","none") + "\n"
    + dline("dl6","Ms. Whitman","ellen","#7dd3fc","IW","#2563eb","Impressive. Your operation is very well organized.","none") + '''
    </div>
    <button class="primary-btn" style="margin-top:1rem" onclick="var lines=['dl2','dl3','dl4','dl5','dl6'];for(var i=0;i<lines.length;i++){var el=document.getElementById(lines[i]);if(el.style.display==='none'){el.style.display='flex';break}}">Next Line</button>'''))

# ---- CHAPTER 5: PRACTICE
SL.append(img_slide(18, 5, "<strong>Transition (10s):</strong> 'Time to practice everything together!' Avance.",
    "More", "More<br><span class=\"accent\">Practice</span>", "", "https://images.unsplash.com/photo-1517245386807-bb43f82c33c4"))

SL.append(slide(19, 5, "slide-dark", "<strong>Quick Fire (4 min):</strong> Uma situacao por vez. Milton responde antes de revelar. Cada situacao revisa uma aula diferente (intro, business, negotiation, results).",
    '''    <div class="chapter-label">Quick Fire</div>
    <h2 class="slide-heading">Quick <span class="accent">Fire</span></h2>
    <div id="qf8" style="width:100%">
      <div class="challenge-card" id="qf8-1">
        <div style="font-size:.75rem;color:var(--accent-light);font-weight:700;margin-bottom:1rem">Challenge 1 / 4</div>
        <p style="color:rgba(255,255,255,.85);font-size:.95rem;line-height:1.6;margin-bottom:1.5rem">You meet a new client at a trade show. Introduce yourself.</p>
        <button class="primary-btn" id="qf8ShowBtn1" onclick="document.getElementById('qf8Answer1').style.display='block';this.style.display='none';document.getElementById('qf8NextBtn1').style.display='inline-flex'">Show Answer</button>
        <div id="qf8Answer1" style="display:none;margin-top:1rem;padding:1rem;background:rgba(22,163,74,.1);border:1px solid rgba(22,163,74,.3);border-radius:8px;color:#4ade80;font-weight:600">"Nice to meet you. I'm Milton, from Sayegh Jewelry." - clear and professional.</div>
        <button class="secondary-btn" id="qf8NextBtn1" style="display:none;margin-top:1rem" onclick="document.getElementById('qf8-1').style.display='none';document.getElementById('qf8-2').style.display='flex'">Next Question</button>
      </div>
      <div class="challenge-card" id="qf8-2" style="display:none">
        <div style="font-size:.75rem;color:var(--accent-light);font-weight:700;margin-bottom:1rem">Challenge 2 / 4</div>
        <p style="color:rgba(255,255,255,.85);font-size:.95rem;line-height:1.6;margin-bottom:1.5rem">Describe what your company does (a fact / routine).</p>
        <button class="primary-btn" id="qf8ShowBtn2" onclick="document.getElementById('qf8Answer2').style.display='block';this.style.display='none';document.getElementById('qf8NextBtn2').style.display='inline-flex'">Show Answer</button>
        <div id="qf8Answer2" style="display:none;margin-top:1rem;padding:1rem;background:rgba(22,163,74,.1);border:1px solid rgba(22,163,74,.3);border-radius:8px;color:#4ade80;font-weight:600">"We design and export luxury jewelry." - Present Simple for facts.</div>
        <button class="secondary-btn" id="qf8PrevBtn2" style="margin-top:.5rem" onclick="document.getElementById('qf8-2').style.display='none';document.getElementById('qf8-1').style.display='flex'">Previous</button>
        <button class="secondary-btn" id="qf8NextBtn2" style="display:none;margin-top:.5rem" onclick="document.getElementById('qf8-2').style.display='none';document.getElementById('qf8-3').style.display='flex'">Next Question</button>
      </div>
      <div class="challenge-card" id="qf8-3" style="display:none">
        <div style="font-size:.75rem;color:var(--accent-light);font-weight:700;margin-bottom:1rem">Challenge 3 / 4</div>
        <p style="color:rgba(255,255,255,.85);font-size:.95rem;line-height:1.6;margin-bottom:1.5rem">Propose a price politely in a negotiation.</p>
        <button class="primary-btn" id="qf8ShowBtn3" onclick="document.getElementById('qf8Answer3').style.display='block';this.style.display='none';document.getElementById('qf8NextBtn3').style.display='inline-flex'">Show Answer</button>
        <div id="qf8Answer3" style="display:none;margin-top:1rem;padding:1rem;background:rgba(22,163,74,.1);border:1px solid rgba(22,163,74,.3);border-radius:8px;color:#4ade80;font-weight:600">"Could we agree on a price of fifty dollars per unit?" - polite modal.</div>
        <button class="secondary-btn" id="qf8PrevBtn3" style="margin-top:.5rem" onclick="document.getElementById('qf8-3').style.display='none';document.getElementById('qf8-2').style.display='flex'">Previous</button>
        <button class="secondary-btn" id="qf8NextBtn3" style="display:none;margin-top:.5rem" onclick="document.getElementById('qf8-3').style.display='none';document.getElementById('qf8-4').style.display='flex'">Next Question</button>
      </div>
      <div class="challenge-card" id="qf8-4" style="display:none">
        <div style="font-size:.75rem;color:var(--accent-light);font-weight:700;margin-bottom:1rem">Challenge 4 / 4</div>
        <p style="color:rgba(255,255,255,.85);font-size:.95rem;line-height:1.6;margin-bottom:1.5rem">Present your best-ever results to the board.</p>
        <button class="primary-btn" id="qf8ShowBtn4" onclick="document.getElementById('qf8Answer4').style.display='block';this.style.display='none'">Show Answer</button>
        <div id="qf8Answer4" style="display:none;margin-top:1rem;padding:1rem;background:rgba(22,163,74,.1);border:1px solid rgba(22,163,74,.3);border-radius:8px;color:#4ade80;font-weight:600">"This was our best quarter ever." - superlative + clear data.</div>
        <button class="secondary-btn" style="margin-top:.5rem" onclick="document.getElementById('qf8-4').style.display='none';document.getElementById('qf8-3').style.display='flex'">Previous</button>
      </div>
    </div>'''))

SL.append(slide(20, 5, "slide-dark", "<strong>Spot the Error (3 min):</strong> Milton clica em cada frase para revelar o erro e a correcao. Pergunte por que esta errado. 1=doesn't (3a pessoa), 2=are working (-ing), 3=have seen (participio).",
    '''    <div class="chapter-label">Spot the Error</div>
    <h2 class="slide-heading">Find the <span class="accent">Mistake</span></h2>
    <div class="error-grid">
      <div class="error-card" onclick="this.classList.toggle('open')">
        <div class="error-sentence">"He <span class="wrong">don't</span> have the invoice."</div>
        <div class="error-fix">Correct: "He <strong>doesn't</strong> have the invoice."</div>
      </div>
      <div class="error-card" onclick="this.classList.toggle('open')">
        <div class="error-sentence">"We <span class="wrong">are work</span> with a new supplier."</div>
        <div class="error-fix">Correct: "We <strong>are working</strong> with a new supplier."</div>
      </div>
      <div class="error-card" onclick="this.classList.toggle('open')">
        <div class="error-sentence">"I <span class="wrong">have saw</span> the report."</div>
        <div class="error-fix">Correct: "I <strong>have seen</strong> the report."</div>
      </div>
    </div>'''))

SL.append(slide(21, 5, "slide-dark", "<strong>Delayed Error Correction (3 min):</strong> Use os campos editaveis para anotar erros reais que Milton cometeu durante a aula e corrija ao vivo. Foque em -s da 3a pessoa, participios e tempos.",
    '''    <div class="chapter-label">Error Correction</div>
    <h2 class="slide-heading">Let's Fix <span class="accent">Together</span></h2>
    <div style="display:flex;flex-direction:column;gap:1rem;margin-top:1.5rem;width:100%">
      <div style="padding:1rem;background:rgba(220,38,38,.08);border:1px solid rgba(220,38,38,.2);border-radius:8px">
        <div style="font-size:.72rem;font-weight:700;color:#f87171;text-transform:uppercase;letter-spacing:1px;margin-bottom:.4rem">Error 1</div>
        <div contenteditable="true" style="min-height:2rem;padding:.4rem;border-bottom:1px dashed rgba(255,255,255,.3);color:rgba(255,255,255,.85);font-size:.88rem;outline:none">Type the error here...</div>
      </div>
      <div style="padding:1rem;background:rgba(22,163,74,.08);border:1px solid rgba(22,163,74,.2);border-radius:8px">
        <div style="font-size:.72rem;font-weight:700;color:#4ade80;text-transform:uppercase;letter-spacing:1px;margin-bottom:.4rem">Correction 1</div>
        <div contenteditable="true" style="min-height:2rem;padding:.4rem;border-bottom:1px dashed rgba(255,255,255,.3);color:rgba(255,255,255,.85);font-size:.88rem;outline:none">Type the correction here...</div>
      </div>
      <div style="padding:1rem;background:rgba(220,38,38,.08);border:1px solid rgba(220,38,38,.2);border-radius:8px">
        <div style="font-size:.72rem;font-weight:700;color:#f87171;text-transform:uppercase;letter-spacing:1px;margin-bottom:.4rem">Error 2</div>
        <div contenteditable="true" style="min-height:2rem;padding:.4rem;border-bottom:1px dashed rgba(255,255,255,.3);color:rgba(255,255,255,.85);font-size:.88rem;outline:none">Type the error here...</div>
      </div>
      <div style="padding:1rem;background:rgba(22,163,74,.08);border:1px solid rgba(22,163,74,.2);border-radius:8px">
        <div style="font-size:.72rem;font-weight:700;color:#4ade80;text-transform:uppercase;letter-spacing:1px;margin-bottom:.4rem">Correction 2</div>
        <div contenteditable="true" style="min-height:2rem;padding:.4rem;border-bottom:1px dashed rgba(255,255,255,.3);color:rgba(255,255,255,.85);font-size:.88rem;outline:none">Type the correction here...</div>
      </div>
    </div>'''))

# ---- CHAPTER 6: YOUR TURN (production)
SL.append(img_slide(22, 6, "<strong>Transition (10s):</strong> 'Now it is your turn - from guided to free.' Avance.",
    "Your", "Your<br><span class=\"accent\">Turn</span>", "From guided to free - show what you learned", "https://images.unsplash.com/photo-1556761175-5973dc0f32e7"))

SL.append(slide(23, 6, "slide-dark", "<strong>Role-play Guided (3 min):</strong> Milton descreve o proprio dia de trabalho usando as keywords. Deve usar pelo menos 3 tempos verbais diferentes. Ajude se precisar.",
    '''    <div class="chapter-label">Role-play - Guided</div>
    <h2 class="slide-heading">Describe Your <span class="accent">Day</span></h2>
    <div class="roleplay-card">
      <div class="roleplay-scenario">Walk your teacher through a typical business day. Use the keywords below and at least 3 different tenses (Simple, Continuous, Perfect).</div>
      <div style="margin-top:1rem;display:flex;flex-wrap:wrap;gap:.5rem">
        <span class="roleplay-kw">supplier call</span>
        <span class="roleplay-kw">client meeting</span>
        <span class="roleplay-kw">we are launching</span>
        <span class="roleplay-kw">I have worked</span>
        <span class="roleplay-kw">send invoices</span>
      </div>
    </div>'''))

SL.append(slide(24, 6, "slide-dark", "<strong>Role-play Semi-free (3 min):</strong> Milton apresenta o negocio para um novo cliente, com apoio minimo. Deve combinar introducao, descricao da empresa e uma proposta com modal.",
    '''    <div class="chapter-label">Role-play - Semi-free</div>
    <h2 class="slide-heading">Meet a New <span class="accent">Client</span></h2>
    <div class="roleplay-card">
      <div class="roleplay-scenario">A new client is interested in your jewelry. Introduce yourself, describe your company, and make a polite proposal. Read any numbers out loud.</div>
      <div style="margin-top:1rem;display:flex;flex-wrap:wrap;gap:.5rem">
        <span class="roleplay-kw">introduce</span>
        <span class="roleplay-kw">we design and export</span>
        <span class="roleplay-kw">could we...?</span>
      </div>
    </div>'''))

SL.append(slide(25, 6, "slide-dark", "<strong>Role-play Free (3 min):</strong> Milton apresenta o proprio negocio real ao professor, sem apoio. Deve incluir: quem ele e, o que a empresa faz, um projeto atual, uma experiencia e uma comparacao. Avalie fluencia.",
    '''    <div class="chapter-label">Role-play - Free</div>
    <h2 class="slide-heading">Present <span class="accent">Freely</span></h2>
    <div class="roleplay-card">
      <div class="roleplay-scenario">Present your REAL business to your teacher. Include: who you are, what your company does, a current project, an experience ("I have..."), and one comparison. No keywords this time.</div>
    </div>'''))

SL.append(slide(26, 6, "slide-dark", "<strong>Oral Drill (3 min):</strong> Milton repete cada frase. Aponte para cada uma. Corrija pronuncia de: launching /LAWN-ching/, worked /werkt/, contract /KON-trakt/.",
    '''    <div class="chapter-label">Oral Drill</div>
    <h2 class="slide-heading">Repeat Each <span class="accent">Phrase</span></h2>
    <div style="display:flex;flex-direction:column;gap:1rem;margin-top:1.5rem;">
      <div style="padding:.8rem 1rem;background:rgba(255,255,255,.06);border-left:3px solid var(--accent);border-radius:0 8px 8px 0;color:rgba(255,255,255,.85);font-size:.95rem;">"I <strong>manage</strong> a jewelry export business."</div>
      <div style="padding:.8rem 1rem;background:rgba(255,255,255,.06);border-left:3px solid var(--accent);border-radius:0 8px 8px 0;color:rgba(255,255,255,.85);font-size:.95rem;">"We <strong>are launching</strong> a new collection this month."</div>
      <div style="padding:.8rem 1rem;background:rgba(255,255,255,.06);border-left:3px solid var(--accent);border-radius:0 8px 8px 0;color:rgba(255,255,255,.85);font-size:.95rem;">"I <strong>have worked</strong> in this industry for thirty years."</div>
      <div style="padding:.8rem 1rem;background:rgba(255,255,255,.06);border-left:3px solid var(--accent);border-radius:0 8px 8px 0;color:rgba(255,255,255,.85);font-size:.95rem;">"<strong>Could</strong> you send me the contract by Friday?"</div>
      <div style="padding:.8rem 1rem;background:rgba(255,255,255,.06);border-left:3px solid var(--accent);border-radius:0 8px 8px 0;color:rgba(255,255,255,.85);font-size:.95rem;">"This was <strong>the best</strong> quarter ever."</div>
    </div>'''))

# ---- CHAPTER 7: WRAP-UP
SL.append(img_slide(27, 7, "<strong>Transition (10s):</strong> 'Excellent work! Let us review what you consolidated today.' Avance.",
    "Wrapping", "Wrapping<br><span class=\"accent\">Up</span>", "", "https://images.unsplash.com/photo-1521737604893-d14cc237f11d"))

SL.append(slide(28, 7, "slide-light", "<strong>Checklist (2 min):</strong> Milton clica cada checkbox. Quando todos estiverem marcados, a aula conta como concluida no sistema. Pergunte: 'Which structure do you feel most confident with now?'",
    '''    <div class="chapter-label">What I Learned</div>
    <h2 class="slide-heading">Lesson 8 <span class="accent">Checklist</span></h2>
    <div class="check-grid">
      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div>I can introduce myself and my company.</div>
      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div>I can use Present Simple, Continuous and Perfect correctly.</div>
      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div>I can make polite proposals with modals.</div>
      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div>I can compare results with comparatives and superlatives.</div>
      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div>I can handle a full business day in English.</div>
    </div>'''))

SL.append(slide(29, 7, "slide-dark", "<strong>Feedback (3 min):</strong> De feedback personalizado sobre a revisao. Destaque os pontos fortes e 1-2 areas para focar nas proximas aulas. Termine sempre positivo.",
    '''    <div class="chapter-label">Feedback</div>
    <h2 class="slide-heading">Teacher <span class="accent">Feedback</span></h2>
    <div style="display:flex;flex-direction:column;gap:1.2rem;margin-top:1.5rem;">
      <div style="padding:1rem;background:rgba(22,163,74,.1);border:1px solid rgba(22,163,74,.3);border-radius:8px;">
        <div style="color:#4ade80;font-weight:700;margin-bottom:.5rem;">Strengths</div>
        <div contenteditable="true" style="color:rgba(255,255,255,.7);font-size:.9rem;min-height:2rem;outline:none;border-bottom:1px dashed rgba(255,255,255,.2);padding-bottom:.3rem">Note Milton's strong points here during the lesson.</div>
      </div>
      <div style="padding:1rem;background:rgba(217,119,6,.1);border:1px solid rgba(217,119,6,.3);border-radius:8px;">
        <div style="color:#fbbf24;font-weight:700;margin-bottom:.5rem;">Areas to Improve</div>
        <div contenteditable="true" style="color:rgba(255,255,255,.7);font-size:.9rem;min-height:2rem;outline:none;border-bottom:1px dashed rgba(255,255,255,.2);padding-bottom:.3rem">Note areas for improvement during the lesson.</div>
      </div>
    </div>'''))

SL.append(slide(30, 7, "slide-dark", "<strong>Homework (1 min):</strong> DIGA ORALMENTE (nao mostrar escrito): '1. Complete the Pre-class for Lesson 8. 2. Record a 2-minute reflection on your progress in Lessons 1-7. 3. Watch Suits S1E1. 4. Listen to the Business English Pod meetings episode.'",
    '''    <div class="chapter-label">Homework</div>
    <h2 class="slide-heading" style="color:#fff">Your <span class="accent">Mission</span></h2>
    <p style="color:rgba(255,255,255,.6);font-size:1rem;margin-top:1rem;">Your teacher will explain your homework now.</p>
    <div style="margin-top:2rem;padding:1rem;background:rgba(255,255,255,.06);border-radius:10px;display:inline-block">
      <svg viewBox="0 0 24 24" width="48" height="48" fill="none" stroke="rgba(255,255,255,.4)" stroke-width="1.5"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg>
    </div>''', style="text-align:center"))

SL.append(slide(31, 7, "slide-dark", "<strong>Badge (1 min):</strong> Celebre! 'You earned your eighth stamp, Milton! You can now combine everything from Lessons 1-7 in a real business day.' Confetti automatico.",
    '''    <div class="badge-card">
      <div class="badge-icon">
        <div class="sparkles"><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div></div>
        <div class="badge-circle"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg></div>
      </div>
      <h2 class="slide-heading" style="color:#fff">Stamp <span class="accent">Earned</span>!</h2>
      <p style="color:rgba(255,255,255,.7);font-size:1rem">Day 8: Review &amp; Consolidation - Complete</p>
    </div>'''))

SL.append(slide(32, 7, "slide-dark", "<strong>Closing (30s):</strong> 'Next lesson: Contracts and Agreements - legal vocabulary and the Past Simple. See you next week!' Encerre com energia.",
    '''    <div class="chapter-label">See You Next Time</div>
    <h2 class="slide-heading" style="color:#fff">Day 8 - <span class="accent">Complete</span></h2>
    <p style="color:rgba(255,255,255,.5);font-size:.92rem;margin-top:1rem">Next: Lesson 9 - Contracts and Agreements</p>
    <p style="color:rgba(255,255,255,.4);font-size:.82rem;margin-top:.5rem">Legal Vocabulary &amp; the Past Simple</p>''', style="text-align:center"))

SLIDES = ("<!-- ===== AULA 8 SLIDES ===== -->\n" + "\n".join(SL)).rstrip() + "\n\n</div><!-- /slides-container -->"

# =====================================================================
# ASSEMBLE
# =====================================================================
def splice(s, start, end, new, inclusive_end=True):
    i = s.index(start)
    j = s.index(end, i) + (len(end) if inclusive_end else 0)
    return s[:i] + new + s[j:]

html = open(SRC_PROF, encoding='utf-8').read()

# title
html = html.replace(
    '<title>Professor View — Milton Sayegh | Aula 7 | Business English for Luxury Export | Alumni by Better</title>',
    '<title>Professor View — Milton Sayegh | Aula 8 | Business English for Luxury Export | Alumni by Better</title>')

# stamp row: add stamp8 after stamp7
html = html.replace(
    '''        <div class="stamp" id="stamp7" data-label="Numbers" style="background-image:url('https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=200&q=80')"></div>''',
    '''        <div class="stamp" id="stamp7" data-label="Numbers" style="background-image:url('https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=200&q=80')"></div>
        <div class="stamp" id="stamp8" data-label="Review" style="background-image:url('%s?w=200&q=80')"></div>''' % IMG)

# pre-class
html = splice(html, '<div class="tab-content" id="tab-exercises">', '</div><!-- /tab-exercises -->', PRECLASS)
# inclass menu
html = splice(html, '<div class="tab-content" id="tab-inclass">', '</div>\n\n<!-- ========== TAB 4', INCLASS_MENU + '\n\n<!-- ========== TAB 4')
# complementary
html = splice(html, '<div class="tab-content" id="tab-complementary">', '</div><!-- /container -->', COMPLEMENTARY)
# slides
html = splice(html, '<!-- ===== CHAPTER 1: THE DREAM (WARM-UP) ===== -->', '</div><!-- /slides-container -->', SLIDES)

# ---- audioMap: derive from speakText() + data-phrase
texts = set()
for m in re.finditer(r"speakText\('((?:[^'\\]|\\')*)'", html):
    texts.add(m.group(1).replace("\\'", "'"))
for m in re.finditer(r'data-phrase="([^"]*)"', html):
    texts.add(m.group(1))
texts = sorted(texts)
amap = {t: "/audio/milton-sayegh/" + fname(t) for t in texts}
am_lines = ",\n".join('    "%s": "%s"' % (t.replace('"', '\\"'), p) for t, p in [(t, amap[t]) for t in texts])
new_audiomap = "var audioMap = {\n" + am_lines + "\n};"
html = splice(html, 'var audioMap = {', '};', new_audiomap)

open(OUT_PROF, 'w', encoding='utf-8').write(html)
print("wrote prof:", OUT_PROF, len(html), "bytes")

# phrases.json
phrases = []
for t in texts:
    v = 'ellen' if t in ELLEN else 'arthur'
    phrases.append({"key": t, "text": t, "file": fname(t), "voice": v})
json.dump(phrases, open(PHRASES_JSON, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print("wrote phrases.json:", len(phrases), "phrases;", sum(1 for p in phrases if p['voice']=='ellen'), "ellen")
