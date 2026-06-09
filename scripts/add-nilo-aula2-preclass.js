#!/usr/bin/env node
/**
 * Add Pre-class Lesson 2 + Complementares Lesson 2 to professor and aluno files
 */
const fs = require('fs');
const path = require('path');
const BASE = path.join(__dirname, '..');

const PROF = path.join(BASE, 'public/professor/nilo-mesquita-patucci.html');
const ALUNO = path.join(BASE, 'public/aluno/nilo-mesquita-patucci.html');
const IMG2 = 'https://images.unsplash.com/photo-1497366216548-37526070297c';

// --- PRE-CLASS LESSON 2 HTML ---
const lesson2HTML = `
<!-- LESSON 2 CARD -->
<div class="lesson-card" id="ex-lesson-2">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('${IMG2}?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Aula 02 &mdash; Pre-class</div>
      <h3>My Professional World</h3>
      <div class="lesson-desc">Describing Your Role &amp; Organization: Present Simple for routines</div>
      <div class="lesson-progress-mini">
        <div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="2" style="width:0%"></div></div>
        <span class="mini-percent" data-lesson-pct="2">0%</span>
      </div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <!-- STAGE 1.1: VOCAB CARDS -->
    <div class="exercise-section">
      <div class="section-header-row">
        <h4>Stage 1.1: Vocabulary</h4>
        <span class="badge badge-vocab">Vocabulary</span>
      </div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">These are the key words for this lesson. Tap Listen to hear the pronunciation.</p>
      <div class="vocab-cards">
        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header"><span class="vocab-card-word">Department</span><span class="vocab-card-dot"> &mdash; </span><span class="vocab-card-def">a division of a large organization responsible for a specific area</span></div><div class="vocab-card-example">&ldquo;I manage the compliance department at Corinthians.&rdquo;</div></div><button class="audio-btn" onclick="speakText('Department',this)">Listen</button></div>
        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header"><span class="vocab-card-word">Responsibilities</span><span class="vocab-card-dot"> &mdash; </span><span class="vocab-card-def">the tasks and duties that are part of your job</span></div><div class="vocab-card-example">&ldquo;My responsibilities include enforcing FIFA regulations.&rdquo;</div></div><button class="audio-btn" onclick="speakText('Responsibilities',this)">Listen</button></div>
        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header"><span class="vocab-card-word">Manage</span><span class="vocab-card-dot"> &mdash; </span><span class="vocab-card-def">to be in charge of and make decisions about a team or project</span></div><div class="vocab-card-example">&ldquo;I manage a team of five compliance professionals.&rdquo;</div></div><button class="audio-btn" onclick="speakText('Manage',this)">Listen</button></div>
        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header"><span class="vocab-card-word">Report to</span><span class="vocab-card-dot"> &mdash; </span><span class="vocab-card-def">to have someone as your direct supervisor; to answer to a boss</span></div><div class="vocab-card-example">&ldquo;I report to the General Director of the club.&rdquo;</div></div><button class="audio-btn" onclick="speakText('Report to',this)">Listen</button></div>
        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header"><span class="vocab-card-word">Coordinate</span><span class="vocab-card-dot"> &mdash; </span><span class="vocab-card-def">to organize people or activities so they work well together</span></div><div class="vocab-card-example">&ldquo;We coordinate with the legal department on investigations.&rdquo;</div></div><button class="audio-btn" onclick="speakText('Coordinate',this)">Listen</button></div>
        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header"><span class="vocab-card-word">Headquarters</span><span class="vocab-card-dot"> &mdash; </span><span class="vocab-card-def">the main office where the leaders of an organization work</span></div><div class="vocab-card-example">&ldquo;Our headquarters is located in Sao Paulo.&rdquo;</div></div><button class="audio-btn" onclick="speakText('Headquarters',this)">Listen</button></div>
        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header"><span class="vocab-card-word">Enforce</span><span class="vocab-card-dot"> &mdash; </span><span class="vocab-card-def">to make sure that people follow a law, rule, or regulation</span></div><div class="vocab-card-example">&ldquo;We enforce internal regulations and FIFA standards.&rdquo;</div></div><button class="audio-btn" onclick="speakText('Enforce',this)">Listen</button></div>
        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header"><span class="vocab-card-word">Investigate</span><span class="vocab-card-dot"> &mdash; </span><span class="vocab-card-def">to carefully examine a situation to find the truth</span></div><div class="vocab-card-example">&ldquo;The team investigates potential violations of governance rules.&rdquo;</div></div><button class="audio-btn" onclick="speakText('Investigate',this)">Listen</button></div>
      </div>
      <button class="listen-all-btn" onclick="listenAllVocab(this)" style="margin-top:.8rem">Listen to all words</button>
    </div>

    <!-- STAGE 1.2: MATCHING -->
    <div class="exercise-section">
      <div class="section-header-row">
        <h4>Stage 1.2: Matching</h4>
        <span class="badge badge-practice">Practice</span>
      </div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each word to its definition.</p>
      <div class="match-grid" id="match-l2">
        <div class="match-row" data-answer="a division responsible for a specific area"><span class="match-word">Department</span><select onchange="checkMatch(this)"><option value="">Select...</option><option value="to organize people so they work together">to organize people so they work together</option><option value="a division responsible for a specific area">a division responsible for a specific area</option><option value="to make sure people follow rules">to make sure people follow rules</option><option value="the main office of an organization">the main office of an organization</option><option value="to be in charge of a team">to be in charge of a team</option><option value="to have someone as your boss">to have someone as your boss</option><option value="the tasks that are part of your job">the tasks that are part of your job</option><option value="to examine carefully to find the truth">to examine carefully to find the truth</option></select></div>
        <div class="match-row" data-answer="the tasks that are part of your job"><span class="match-word">Responsibilities</span><select onchange="checkMatch(this)"><option value="">Select...</option><option value="to examine carefully to find the truth">to examine carefully to find the truth</option><option value="the tasks that are part of your job">the tasks that are part of your job</option><option value="a division responsible for a specific area">a division responsible for a specific area</option><option value="to make sure people follow rules">to make sure people follow rules</option><option value="the main office of an organization">the main office of an organization</option><option value="to organize people so they work together">to organize people so they work together</option><option value="to be in charge of a team">to be in charge of a team</option><option value="to have someone as your boss">to have someone as your boss</option></select></div>
        <div class="match-row" data-answer="to be in charge of a team"><span class="match-word">Manage</span><select onchange="checkMatch(this)"><option value="">Select...</option><option value="the main office of an organization">the main office of an organization</option><option value="to have someone as your boss">to have someone as your boss</option><option value="to be in charge of a team">to be in charge of a team</option><option value="the tasks that are part of your job">the tasks that are part of your job</option><option value="to examine carefully to find the truth">to examine carefully to find the truth</option><option value="a division responsible for a specific area">a division responsible for a specific area</option><option value="to organize people so they work together">to organize people so they work together</option><option value="to make sure people follow rules">to make sure people follow rules</option></select></div>
        <div class="match-row" data-answer="to have someone as your boss"><span class="match-word">Report to</span><select onchange="checkMatch(this)"><option value="">Select...</option><option value="to make sure people follow rules">to make sure people follow rules</option><option value="to organize people so they work together">to organize people so they work together</option><option value="the main office of an organization">the main office of an organization</option><option value="to have someone as your boss">to have someone as your boss</option><option value="a division responsible for a specific area">a division responsible for a specific area</option><option value="to be in charge of a team">to be in charge of a team</option><option value="to examine carefully to find the truth">to examine carefully to find the truth</option><option value="the tasks that are part of your job">the tasks that are part of your job</option></select></div>
        <div class="match-row" data-answer="to organize people so they work together"><span class="match-word">Coordinate</span><select onchange="checkMatch(this)"><option value="">Select...</option><option value="to be in charge of a team">to be in charge of a team</option><option value="to examine carefully to find the truth">to examine carefully to find the truth</option><option value="to organize people so they work together">to organize people so they work together</option><option value="the tasks that are part of your job">the tasks that are part of your job</option><option value="to have someone as your boss">to have someone as your boss</option><option value="to make sure people follow rules">to make sure people follow rules</option><option value="a division responsible for a specific area">a division responsible for a specific area</option><option value="the main office of an organization">the main office of an organization</option></select></div>
        <div class="match-row" data-answer="the main office of an organization"><span class="match-word">Headquarters</span><select onchange="checkMatch(this)"><option value="">Select...</option><option value="the tasks that are part of your job">the tasks that are part of your job</option><option value="a division responsible for a specific area">a division responsible for a specific area</option><option value="to have someone as your boss">to have someone as your boss</option><option value="the main office of an organization">the main office of an organization</option><option value="to be in charge of a team">to be in charge of a team</option><option value="to examine carefully to find the truth">to examine carefully to find the truth</option><option value="to make sure people follow rules">to make sure people follow rules</option><option value="to organize people so they work together">to organize people so they work together</option></select></div>
        <div class="match-row" data-answer="to make sure people follow rules"><span class="match-word">Enforce</span><select onchange="checkMatch(this)"><option value="">Select...</option><option value="to organize people so they work together">to organize people so they work together</option><option value="to make sure people follow rules">to make sure people follow rules</option><option value="to have someone as your boss">to have someone as your boss</option><option value="to be in charge of a team">to be in charge of a team</option><option value="the main office of an organization">the main office of an organization</option><option value="a division responsible for a specific area">a division responsible for a specific area</option><option value="the tasks that are part of your job">the tasks that are part of your job</option><option value="to examine carefully to find the truth">to examine carefully to find the truth</option></select></div>
        <div class="match-row" data-answer="to examine carefully to find the truth"><span class="match-word">Investigate</span><select onchange="checkMatch(this)"><option value="">Select...</option><option value="to have someone as your boss">to have someone as your boss</option><option value="the main office of an organization">the main office of an organization</option><option value="to be in charge of a team">to be in charge of a team</option><option value="to organize people so they work together">to organize people so they work together</option><option value="to examine carefully to find the truth">to examine carefully to find the truth</option><option value="the tasks that are part of your job">the tasks that are part of your job</option><option value="to make sure people follow rules">to make sure people follow rules</option><option value="a division responsible for a specific area">a division responsible for a specific area</option></select></div>
      </div>
      <button class="verify-all-btn" onclick="verifyAllMatches('match-l2')">Check Answers</button>
    </div>

    <!-- STAGE 1.3: GRAMMAR IN CONTEXT -->
    <div class="exercise-section">
      <div class="section-header-row">
        <h4>Stage 1.3: Grammar in Context</h4>
        <span class="badge badge-grammar">Grammar</span>
      </div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text below. Pay attention to the words in bold.</p>
      <div style="padding:1.2rem;background:rgba(255,255,255,.4);border:1px solid rgba(200,200,190,.5);border-radius:10px;font-size:.92rem;line-height:1.8;margin-bottom:1rem">
        <p>Nilo <strong>manages</strong> the compliance <strong>department</strong> at Sport Club Corinthians Paulista. He <strong>reports to</strong> the General Director, and his team has five full-time employees.</p>
        <p style="margin-top:.6rem">The department has three main <strong>responsibilities</strong>: they <strong>enforce</strong> internal regulations and FIFA standards, they <strong>investigate</strong> potential violations, and they <strong>coordinate</strong> with external auditors and the Brazilian Football Confederation.</p>
        <p style="margin-top:.6rem">Their <strong>headquarters</strong> <strong>is</strong> in the Parque Sao Jorge area of Sao Paulo. Nilo <strong>works</strong> from the Barra Funda office every day. He <strong>does not work</strong> alone. His team <strong>meets</strong> every Monday to review open cases.</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. How many people work in the compliance department?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Three people</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Five full-time employees</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Ten people</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. Who does Nilo report to?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> The CEO</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> The FIFA President</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> The General Director</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. When does the team meet to review cases?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Every Monday</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Every Friday</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Once a month</div></div></div>
    </div>

    <!-- STAGE 1.4: GRAMMAR TIP -->
    <div class="exercise-section">
      <div class="section-header-row">
        <h4>Stage 1.4: Grammar Tip</h4>
        <span class="badge badge-grammar">Grammar</span>
      </div>
      <div style="padding:1.2rem;background:rgba(255,255,255,.4);border:1px solid rgba(200,200,190,.5);border-radius:10px;font-size:.9rem;line-height:1.8">
        <p><strong>Present Simple</strong> &mdash; Use for routines, habits, facts, and permanent situations.</p>
        <table style="width:100%;border-collapse:collapse;margin:.8rem 0;font-size:.85rem"><thead><tr style="border-bottom:2px solid var(--accent)"><th style="padding:.5rem;text-align:left;color:var(--accent)">Form</th><th style="padding:.5rem;text-align:left">Example</th></tr></thead><tbody>
        <tr style="border-bottom:1px solid #e5e5e0"><td style="padding:.5rem">I/You/We/They + verb</td><td style="padding:.5rem">I <strong>manage</strong> the team.</td></tr>
        <tr style="border-bottom:1px solid #e5e5e0"><td style="padding:.5rem">He/She/It + verb + <strong>-s</strong></td><td style="padding:.5rem">She <strong>coordinates</strong> with FIFA.</td></tr>
        <tr style="border-bottom:1px solid #e5e5e0"><td style="padding:.5rem">Negative: do/does + not + verb</td><td style="padding:.5rem">He <strong>does not work</strong> alone.</td></tr>
        <tr><td style="padding:.5rem">Question: Do/Does + subject + verb</td><td style="padding:.5rem"><strong>Does</strong> he <strong>manage</strong> the team?</td></tr>
        </tbody></table>
        <div style="padding:.8rem;background:rgba(220,38,38,.06);border:1px solid rgba(220,38,38,.15);border-radius:8px;margin-top:.6rem"><strong style="color:#dc2626">Common Mistake:</strong> <span style="text-decoration:line-through;color:#dc2626">He manage the department.</span> &rarr; <span style="color:#16a34a">He manage<strong>s</strong> the department.</span><br><span style="text-decoration:line-through;color:#dc2626">Does she coordinates?</span> &rarr; <span style="color:#16a34a">Does she coordinate?</span> (no -s after does)</div>
      </div>
    </div>

    <!-- STAGE 1.5: FILL-IN -->
    <div class="exercise-section">
      <div class="section-header-row">
        <h4>Stage 1.5: Fill in the Blank</h4>
        <span class="badge badge-practice">Practice</span>
      </div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence with the correct word.</p>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"I <input class="blank-input" data-answer="manage" data-hint="Hint: to be in charge of a team" data-phrase="I manage a team of five people." placeholder="___"> a team of five people."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"I <input class="blank-input" data-answer="report" data-alt="report to" data-hint="Hint: to have someone as your direct supervisor" data-phrase="I report to the General Director." placeholder="___"> to the General Director."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"We <input class="blank-input" data-answer="coordinate" data-hint="Hint: to organize people to work together" data-phrase="We coordinate with external auditors every quarter." placeholder="___"> with external auditors every quarter."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"Our <input class="blank-input" data-answer="headquarters" data-hint="Hint: the main office" data-phrase="Our headquarters is in the Parque Sao Jorge area." placeholder="___"> is in the Parque Sao Jorge area."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"My team <input class="blank-input" data-answer="investigates" data-hint="Hint: to examine carefully (he/she/it form)" data-phrase="My team investigates compliance violations." placeholder="___"> compliance violations."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
    </div>

    <!-- STAGE 2: ORDERING -->
    <div class="exercise-section">
      <div class="section-header-row">
        <h4>Stage 2: Put in Order</h4>
        <span class="badge badge-order">Order</span>
      </div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen first, then put the sentences in the correct order.</p>
      <button class="btn btn-listen" onclick="speakText('[order-l2]',this)" style="margin-bottom:.8rem">Listen</button>
      <div class="order-container" id="order-l2">
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l2')"><span class="order-num">?</span><span class="order-text">&ldquo;We enforce FIFA standards and investigate violations.&rdquo;</span><span class="order-arrows"><button class="arrow-btn" onclick="event.stopPropagation();moveItem(this,-1,'order-l2')">&#9650;</button><button class="arrow-btn" onclick="event.stopPropagation();moveItem(this,1,'order-l2')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l2')"><span class="order-num">?</span><span class="order-text">&ldquo;I manage the compliance department.&rdquo;</span><span class="order-arrows"><button class="arrow-btn" onclick="event.stopPropagation();moveItem(this,-1,'order-l2')">&#9650;</button><button class="arrow-btn" onclick="event.stopPropagation();moveItem(this,1,'order-l2')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l2')"><span class="order-num">?</span><span class="order-text">&ldquo;I report to the General Director.&rdquo;</span><span class="order-arrows"><button class="arrow-btn" onclick="event.stopPropagation();moveItem(this,-1,'order-l2')">&#9650;</button><button class="arrow-btn" onclick="event.stopPropagation();moveItem(this,1,'order-l2')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l2')"><span class="order-num">?</span><span class="order-text">&ldquo;We also coordinate with the Brazilian Football Confederation.&rdquo;</span><span class="order-arrows"><button class="arrow-btn" onclick="event.stopPropagation();moveItem(this,-1,'order-l2')">&#9650;</button><button class="arrow-btn" onclick="event.stopPropagation();moveItem(this,1,'order-l2')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l2')"><span class="order-num">?</span><span class="order-text">&ldquo;We have a team of five full-time employees.&rdquo;</span><span class="order-arrows"><button class="arrow-btn" onclick="event.stopPropagation();moveItem(this,-1,'order-l2')">&#9650;</button><button class="arrow-btn" onclick="event.stopPropagation();moveItem(this,1,'order-l2')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l2')">Check Order</button>
    </div>

    <!-- STAGE 3: PRONUNCIATION -->
    <div class="exercise-section">
      <div class="section-header-row">
        <h4>Stage 3: Pronunciation</h4>
        <span class="badge badge-speak">Speaking</span>
      </div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen first, then record yourself. The system will compare your pronunciation word by word.</p>
      <div class="speech-card" data-phrase="I manage the compliance department and I report to the General Director."><div class="speech-phrase">I manage the compliance department and I report to the General Director.</div><div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">Listen</button><button class="btn btn-record" onclick="startRecording(this)">Record</button><button class="btn btn-stop" onclick="stopRecording(this)">Stop</button></div><div class="speech-result"></div></div>
      <div class="speech-card" data-phrase="My responsibilities include enforcing FIFA standards and investigating violations."><div class="speech-phrase">My responsibilities include enforcing FIFA standards and investigating violations.</div><div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">Listen</button><button class="btn btn-record" onclick="startRecording(this)">Record</button><button class="btn btn-stop" onclick="stopRecording(this)">Stop</button></div><div class="speech-result"></div></div>
      <div class="speech-card" data-phrase="We coordinate with the legal department and external auditors."><div class="speech-phrase">We coordinate with the legal department and external auditors.</div><div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">Listen</button><button class="btn btn-record" onclick="startRecording(this)">Record</button><button class="btn btn-stop" onclick="stopRecording(this)">Stop</button></div><div class="speech-result"></div></div>
    </div>

    <!-- STAGE 4: QUIZ -->
    <div class="exercise-section">
      <div class="section-header-row">
        <h4>Stage 4: Situational Quiz</h4>
        <span class="badge badge-quiz">Quiz</span>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. A delegate asks: &ldquo;How is your department structured?&rdquo; What is the best answer?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;I am managing five people.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> &ldquo;I manage a team of five. I report to the General Director.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;My department is big.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. Which sentence uses Present Simple correctly?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;She coordinate with FIFA.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> &ldquo;She coordinates with FIFA every quarter.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;She is coordinates with FIFA.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. Someone asks: &ldquo;Where is your headquarters?&rdquo; Best response?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> &ldquo;Our headquarters is in Sao Paulo.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> &ldquo;My headquarters are very big.&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;I headquarters in Sao Paulo.&rdquo;</div></div></div>
      <div class="quiz-item"><div class="quiz-question">4. Which question form is correct?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;Does she manages the team?&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> &ldquo;Do she manage the team?&rdquo;</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> &ldquo;Does she manage the team?&rdquo;</div></div></div>
    </div>

    <!-- STAGE 5: THINK ABOUT IT -->
    <div class="exercise-section">
      <div class="section-header-row">
        <h4>Stage 5: Think About It</h4>
        <span class="badge badge-think">Reflection</span>
      </div>
      <div class="think-card">
        <div class="think-question">Imagine a FIFA delegate from Japan asks you: &ldquo;Tell me about your department at Corinthians. What do you do every day? Who do you work with?&rdquo; Record your answer. Speak for at least 60 seconds. Use the 8 vocabulary words from this lesson.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)">Stop</button></div>
        <div id="think-result-2"></div>
      </div>
    </div>

    <!-- SURVIVAL CARD -->
    <div class="survival-card">
      <h4 style="font-family:'Cormorant Garamond',serif;font-size:1.1rem;font-weight:600;margin-bottom:.8rem;color:#1a1a1a">Survival Card &mdash; Lesson 2</h4>
      <div class="survival-phrase"><span class="sp-num">1</span><span class="sp-en">I manage the compliance department.</span><button class="audio-btn" onclick="speakText('I manage the compliance department.',this)">Listen</button></div>
      <div class="survival-phrase"><span class="sp-num">2</span><span class="sp-en">I report to the General Director.</span><button class="audio-btn" onclick="speakText('I report to the General Director.',this)">Listen</button></div>
      <div class="survival-phrase"><span class="sp-num">3</span><span class="sp-en">My main responsibilities include enforcing regulations.</span><button class="audio-btn" onclick="speakText('My main responsibilities include enforcing regulations.',this)">Listen</button></div>
      <div class="survival-phrase"><span class="sp-num">4</span><span class="sp-en">We enforce FIFA regulations at the club.</span><button class="audio-btn" onclick="speakText('We enforce FIFA regulations at the club.',this)">Listen</button></div>
      <div class="survival-phrase"><span class="sp-num">5</span><span class="sp-en">Our headquarters is in Sao Paulo.</span><button class="audio-btn" onclick="speakText('Our headquarters is in Sao Paulo.',this)">Listen</button></div>
    </div>

  </div>
</div>`;

// --- COMPLEMENTARES LESSON 2 HTML ---
const complementares2HTML = `
<h4 style="font-family:'Cormorant Garamond',serif;font-size:1.1rem;margin:1.5rem 0 .8rem">Aula 2: My Professional World</h4>
<div class="media-grid">
<div class="media-card-wrapper" data-media="l2-series"><label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label><div class="media-card"><div class="media-thumb"><svg viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2" style="width:24px;height:24px"><rect x="2" y="2" width="20" height="20" rx="2.18"/><line x1="7" y1="2" x2="7" y2="22"/><line x1="17" y1="2" x2="17" y2="22"/><line x1="2" y1="12" x2="22" y2="12"/></svg></div><div class="media-info"><div class="media-type">Series</div><h5>Ted Lasso &mdash; Season 1, Episode 1 (Apple TV+)</h5><p>An American football coach manages a British soccer team. Perfect for football vocabulary, leadership language, and British vs American English.</p><p class="media-tip">Tip: Watch with English subtitles. Note how Ted describes his role to the team.</p></div></div></div>
<div class="media-card-wrapper" data-media="l2-podcast"><label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label><div class="media-card"><div class="media-thumb"><svg viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2" style="width:24px;height:24px"><path d="M12 1a3 3 0 00-3 3v8a3 3 0 006 0V4a3 3 0 00-3-3z"/><path d="M19 10v2a7 7 0 01-14 0v-2"/></svg></div><div class="media-info"><div class="media-type">Podcast</div><h5>ESPN FC &mdash; Any Recent Episode</h5><p>Global football discussion in English. Great for hearing how analysts describe roles, teams, and organizations.</p><p class="media-tip">Tip: Listen during your commute. Focus on how they describe what teams and managers do.</p></div></div></div>
<div class="media-card-wrapper" data-media="l2-ted"><label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label><div class="media-card"><div class="media-thumb"><svg viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2" style="width:24px;height:24px"><polygon points="5 3 19 12 5 21 5 3"/></svg></div><div class="media-info"><div class="media-type">TED Talk</div><h5>How Great Leaders Inspire Action &mdash; Simon Sinek</h5><p>Simon Sinek explains the &ldquo;Golden Circle&rdquo; of leadership. Excellent vocabulary for describing what you do and why.</p><p class="media-tip">Tip: Pay attention to how Sinek uses Present Simple to describe what leaders do.</p></div></div></div>
</div>`;

// --- INSERT INTO BOTH FILES ---
function insertContent(filePath) {
  let html = fs.readFileSync(filePath, 'utf8');

  // Insert Pre-class lesson 2 before </div><!-- /tab-exercises -->
  html = html.replace(
    '</div><!-- /tab-exercises -->',
    lesson2HTML + '\n</div><!-- /tab-exercises -->'
  );

  // Insert Complementares lesson 2 before </div><!-- /tab-complementary -->
  html = html.replace(
    '</div><!-- /tab-complementary -->',
    complementares2HTML + '\n</div><!-- /tab-complementary -->'
  );

  fs.writeFileSync(filePath, html);
  console.log('Updated:', filePath, '(' + html.split('\n').length + ' lines)');
}

insertContent(PROF);
insertContent(ALUNO);
console.log('Pre-class and Complementares added to both files.');
