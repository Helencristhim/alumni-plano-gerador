#!/usr/bin/env node
/**
 * Rebuild Nilo Aula 2 using the SAME CSS from the main professor file.
 * This ensures visual consistency between Aula 1 and Aula 2.
 */
const fs = require('fs');
const path = require('path');
const BASE = path.join(__dirname, '..');

// Read main professor file to extract CSS
const mainFile = fs.readFileSync(path.join(BASE, 'public/professor/nilo-mesquita-patucci.html'), 'utf8');
const cssMatch = mainFile.match(/<style>([\s\S]*?)<\/style>/);
const css = cssMatch[1];

// Read the audioMap from the main file (includes aula2 entries)
const audioMapMatch = mainFile.match(/var audioMap = \{([\s\S]*?)\};/);
const audioMapContent = 'var audioMap = {' + audioMapMatch[1] + '};';

// Build standalone aula2 with SAME CSS as main file
const html = `<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow">
<title>IN CLASS — Nilo Mesquita Patucci | Aula 2 | Alumni by Better</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&display=swap" rel="stylesheet">
<script>
${audioMapContent}
<\/script>
<style>
${css}

/* Standalone overrides */
body { overflow: hidden; height: 100vh; }
body.slide-mode .main-content { display: none; }
.logo-bar { background: rgba(26,26,46,.92); border-bottom: 1px solid rgba(255,255,255,.06); }
.logo-bar img { filter: brightness(10); }
.logo-bar .prof-badge { display: none; }
.logo-bar .slide-counter { display: block; }
.slides-wrapper { display: block !important; }
.nav-bar { display: flex !important; }
.teacher-t { display: flex !important; }
</style>
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.min.js"><\/script>
<script src="/lib/supabase-config.js"><\/script>
<script>window.STUDENT_SLUG='nilo-mesquita-patucci';window.TOTAL_AULAS=96;<\/script>
</head>
<body class="slide-mode">

<!-- LOGO BAR -->
<div class="logo-bar">
  <img src="/assets/logo-alumni.png" alt="Alumni by Better">
  <span class="prof-badge">Professor View</span>
  <span class="slide-counter" id="slideCounter">01 / 37</span>
</div>

<!-- SLIDES WRAPPER -->
<div class="slides-wrapper" id="slidesWrapper">

<!-- Phase bar -->
<div class="phase-bar" id="phaseBar">
  <div class="phase-segment current" data-phase="1"></div>
  <div class="phase-segment upcoming" data-phase="2"></div>
  <div class="phase-segment upcoming" data-phase="3"></div>
  <div class="phase-segment upcoming" data-phase="4"></div>
  <div class="phase-segment upcoming" data-phase="5"></div>
  <div class="phase-segment upcoming" data-phase="6"></div>
  <div class="phase-segment upcoming" data-phase="7"></div>
</div>
<div class="phase-labels" id="phaseLabels">
  <span class="phase-label current" data-phase="1">Your World</span>
  <span class="phase-label" data-phase="2">Packing Words</span>
  <span class="phase-label" data-phase="3">The Code</span>
  <span class="phase-label" data-phase="4">Getting There</span>
  <span class="phase-label" data-phase="5">Practice</span>
  <span class="phase-label" data-phase="6">Your Turn</span>
  <span class="phase-label" data-phase="7">Wrap-up</span>
</div>

<div class="slides-container" id="slidesContainer">

<!-- ══════ CHAPTER 1: YOUR WORLD ══════ -->

<div class="slide slide-image active" data-slide="1" data-phase="1" data-teacher="Abertura (2 min): Cumprimente o Nilo normalmente. Deixe o slide visível enquanto faz rapport." style="background-image:url('https://images.unsplash.com/photo-1497366216548-37526070297c?w=1400&q=80')">
  <div class="slide-inner">
    <div class="chapter-label">Lesson 2 &mdash; Business English</div>
    <h1 class="slide-title">My Professional<br><span class="accent">World</span></h1>
    <p class="slide-subtitle">B1 &mdash; 90 minutes &mdash; Alumni by Better</p>
  </div>
</div>

<div class="slide slide-image" data-slide="2" data-phase="1" data-teacher="Transição. Diga: &quot;Today we will describe your department, your responsibilities, and how your organization works.&quot;" style="background-image:url('https://images.unsplash.com/photo-1497366216548-37526070297c?w=1400&q=80')">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 1</div>
    <h2 class="slide-title">Your <span class="accent">World</span></h2>
    <p class="slide-subtitle">Warm-up, callback from Lesson 1, and a look at your professional routine.</p>
  </div>
</div>

<div class="slide slide-dark" data-slide="3" data-phase="1" data-teacher="Callback (5 min): TESTE se o Nilo reteve o vocabulário da Aula 1. Pergunte: &quot;Last class we learned 8 words. Can you introduce yourself using at least 5 of them?&quot; Se travar, dê a primeira letra como pista. NÃO pule o callback.">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 1: Your World</div>
    <h2 class="slide-heading">Callback: <span class="accent">Lesson 1</span></h2>
    <div class="warm-questions">
      <div class="warm-q">&ldquo;Last class you learned 8 words. Can you introduce yourself using at least 5 of them?&rdquo;</div>
    </div>
    <div style="display:flex;flex-wrap:wrap;gap:.5rem;margin-top:2rem;justify-content:center">
      <span style="padding:.4rem .8rem;border:1px solid rgba(255,255,255,.15);border-radius:16px;font-size:.82rem;color:rgba(255,255,255,.5)">introduce</span>
      <span style="padding:.4rem .8rem;border:1px solid rgba(255,255,255,.15);border-radius:16px;font-size:.82rem;color:rgba(255,255,255,.5)">represent</span>
      <span style="padding:.4rem .8rem;border:1px solid rgba(255,255,255,.15);border-radius:16px;font-size:.82rem;color:rgba(255,255,255,.5)">oversee</span>
      <span style="padding:.4rem .8rem;border:1px solid rgba(255,255,255,.15);border-radius:16px;font-size:.82rem;color:rgba(255,255,255,.5)">compliance</span>
      <span style="padding:.4rem .8rem;border:1px solid rgba(255,255,255,.15);border-radius:16px;font-size:.82rem;color:rgba(255,255,255,.5)">governance</span>
      <span style="padding:.4rem .8rem;border:1px solid rgba(255,255,255,.15);border-radius:16px;font-size:.82rem;color:rgba(255,255,255,.5)">background</span>
      <span style="padding:.4rem .8rem;border:1px solid rgba(255,255,255,.15);border-radius:16px;font-size:.82rem;color:rgba(255,255,255,.5)">currently</span>
      <span style="padding:.4rem .8rem;border:1px solid rgba(255,255,255,.15);border-radius:16px;font-size:.82rem;color:rgba(255,255,255,.5)">responsible</span>
    </div>
  </div>
</div>

<div class="slide slide-dark" data-slide="4" data-phase="1" data-teacher="Warm-up (5 min): Pergunte sobre a rotina. Observe: o Nilo usa Present Simple corretamente? Diz &quot;I manage&quot; ou &quot;I am manage&quot;? Anote erros.">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 1: Your World</div>
    <h2 class="slide-heading">Your <span class="accent">Routine</span></h2>
    <div class="warm-questions">
      <div class="warm-q">&ldquo;Tell me: what does a typical Monday look like at Corinthians?&rdquo;</div>
      <div class="warm-q">&ldquo;How many people work with you? Who do you talk to every day?&rdquo;</div>
    </div>
  </div>
</div>

<!-- ══════ CHAPTER 2: PACKING WORDS ══════ -->

<div class="slide slide-image" data-slide="5" data-phase="2" data-teacher="Transição. Diga: &quot;Now let us build your vocabulary for describing your professional world.&quot;" style="background-image:url('https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?w=1400&q=80')">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 2</div>
    <h2 class="slide-title">Packing <span class="accent">Words</span></h2>
    <p class="slide-subtitle">8 essential words for describing your department, responsibilities, and organization.</p>
  </div>
</div>

<div class="slide slide-light" data-slide="6" data-phase="2" data-teacher="Vocabulário 1 (7 min): Clique em cada card. DEPARTMENT: CCQ &quot;Is a department a person or a division?&quot; (division). MANAGE: CCQ &quot;If I manage a team, am I the boss?&quot; (yes). REPORT TO: drilling extra &quot;I report TO the director&quot;.">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 2: Packing Words</div>
    <h2 class="slide-heading">Key <span class="accent">Vocabulary</span> (1/2)</h2>
    <div class="vocab-grid" id="vocabGrid1">
      <div class="vocab-card" onclick="revealVocab(this)">
        <div class="card-icon" style="background:linear-gradient(135deg,#7B2D3B,#9A4054)"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" style="width:48px;height:48px"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/></svg><div class="card-hint">A section of an organization responsible for a specific area</div></div>
        <div class="card-body"><div class="card-word">Department</div><div class="card-def">A division of a large organization that handles a specific area of work.</div><div class="card-example">&ldquo;I manage the compliance department at Corinthians.&rdquo;</div><div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('Department',this)"><svg viewBox="0 0 24 24" style="width:12px;height:12px" fill="none" stroke="#fff" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div></div>
      </div>
      <div class="vocab-card" onclick="revealVocab(this)">
        <div class="card-icon" style="background:linear-gradient(135deg,#2C5282,#3B7DD8)"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" style="width:48px;height:48px"><path d="M16 4h2a2 2 0 012 2v14a2 2 0 01-2 2H6a2 2 0 01-2-2V6a2 2 0 012-2h2"/><rect x="8" y="2" width="8" height="4" rx="1"/></svg><div class="card-hint">The tasks and duties that are part of your job</div></div>
        <div class="card-body"><div class="card-word">Responsibilities</div><div class="card-def">The duties and tasks that someone must do as part of their role.</div><div class="card-example">&ldquo;My responsibilities include enforcing FIFA regulations.&rdquo;</div><div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('Responsibilities',this)"><svg viewBox="0 0 24 24" style="width:12px;height:12px" fill="none" stroke="#fff" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div></div>
      </div>
      <div class="vocab-card" onclick="revealVocab(this)">
        <div class="card-icon" style="background:linear-gradient(135deg,#553C7B,#7B5EA7)"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" style="width:48px;height:48px"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4-4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/></svg><div class="card-hint">To be in charge of and make decisions about a team</div></div>
        <div class="card-body"><div class="card-word">Manage</div><div class="card-def">To be in charge of and make decisions about a project, team, or department.</div><div class="card-example">&ldquo;I manage a team of five compliance professionals.&rdquo;</div><div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('Manage',this)"><svg viewBox="0 0 24 24" style="width:12px;height:12px" fill="none" stroke="#fff" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div></div>
      </div>
      <div class="vocab-card" onclick="revealVocab(this)">
        <div class="card-icon" style="background:linear-gradient(135deg,#1B4D3E,#2D7A5F)"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" style="width:48px;height:48px"><polyline points="16 3 21 3 21 8"/><line x1="4" y1="20" x2="21" y2="3"/></svg><div class="card-hint">To have someone as your direct supervisor</div></div>
        <div class="card-body"><div class="card-word">Report to</div><div class="card-def">To be directly supervised by someone; to have someone as your boss.</div><div class="card-example">&ldquo;I report to the General Director of the club.&rdquo;</div><div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('Report to',this)"><svg viewBox="0 0 24 24" style="width:12px;height:12px" fill="none" stroke="#fff" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div></div>
      </div>
    </div>
    <div class="vocab-counter" id="vocabCount1">0 / 4 words revealed</div>
  </div>
</div>

<div class="slide slide-light" data-slide="7" data-phase="2" data-teacher="Vocabulário 2 (7 min): COORDINATE: drilling co-OR-di-nate. ENFORCE: diferente de force, mais formal. INVESTIGATE: CCQ &quot;If you investigate, do you already know the answer?&quot; (no). HEADQUARTERS: plural mas singular &quot;Our headquarters IS...&quot;">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 2: Packing Words</div>
    <h2 class="slide-heading">Key <span class="accent">Vocabulary</span> (2/2)</h2>
    <div class="vocab-grid" id="vocabGrid2">
      <div class="vocab-card" onclick="revealVocab(this)">
        <div class="card-icon" style="background:linear-gradient(135deg,#6B4C3B,#8D6E5D)"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" style="width:48px;height:48px"><circle cx="12" cy="12" r="10"/><path d="M2 12h20"/></svg><div class="card-hint">To organize people or activities so they work together</div></div>
        <div class="card-body"><div class="card-word">Coordinate</div><div class="card-def">To organize different people or activities so they work well together.</div><div class="card-example">&ldquo;We coordinate with the legal department.&rdquo;</div><div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('Coordinate',this)"><svg viewBox="0 0 24 24" style="width:12px;height:12px" fill="none" stroke="#fff" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div></div>
      </div>
      <div class="vocab-card" onclick="revealVocab(this)">
        <div class="card-icon" style="background:linear-gradient(135deg,#4A5568,#718096)"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" style="width:48px;height:48px"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg><div class="card-hint">The main office where the leaders work</div></div>
        <div class="card-body"><div class="card-word">Headquarters</div><div class="card-def">The main office or center of operations of an organization.</div><div class="card-example">&ldquo;Our headquarters is located in Sao Paulo.&rdquo;</div><div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('Headquarters',this)"><svg viewBox="0 0 24 24" style="width:12px;height:12px" fill="none" stroke="#fff" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div></div>
      </div>
      <div class="vocab-card" onclick="revealVocab(this)">
        <div class="card-icon" style="background:linear-gradient(135deg,#5C3D2E,#7D5A48)"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" style="width:48px;height:48px"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg><div class="card-hint">To make sure people follow a law or regulation</div></div>
        <div class="card-body"><div class="card-word">Enforce</div><div class="card-def">To make sure that people follow a law, rule, or regulation.</div><div class="card-example">&ldquo;We enforce internal regulations and FIFA standards.&rdquo;</div><div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('Enforce',this)"><svg viewBox="0 0 24 24" style="width:12px;height:12px" fill="none" stroke="#fff" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div></div>
      </div>
      <div class="vocab-card" onclick="revealVocab(this)">
        <div class="card-icon" style="background:linear-gradient(135deg,#4A3728,#6B5240)"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" style="width:48px;height:48px"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg><div class="card-hint">To carefully examine a situation to find the truth</div></div>
        <div class="card-body"><div class="card-word">Investigate</div><div class="card-def">To carefully examine a situation to find the truth about something.</div><div class="card-example">&ldquo;The team investigates potential violations.&rdquo;</div><div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('Investigate',this)"><svg viewBox="0 0 24 24" style="width:12px;height:12px" fill="none" stroke="#fff" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div></div>
      </div>
    </div>
    <div class="vocab-counter" id="vocabCount2">0 / 4 words revealed</div>
  </div>
</div>

<!-- ══════ CHAPTER 3: THE CODE ══════ -->

<div class="slide slide-image" data-slide="8" data-phase="3" data-teacher="Transição. Diga: &quot;You know the words. Now let us understand the code: Present Simple for routines and responsibilities.&quot;" style="background-image:url('https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=1400&q=80')">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 3</div>
    <h2 class="slide-title">The <span class="accent">Code</span></h2>
    <p class="slide-subtitle">Present Simple for routines, habits, and professional responsibilities. The grammar that describes your daily world.</p>
  </div>
</div>

<div class="slide slide-light" data-slide="9" data-phase="3" data-teacher="Grammar Discovery (5 min): NÃO diga a regra. Pergunte: &quot;Look at these sentences. What do you notice about the verbs?&quot; Guie: Present Simple para rotinas. 3a pessoa: he/she + -s.">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 3: The Code</div>
    <h2 class="slide-heading">What Do You <span class="accent">Notice</span>?</h2>
    <div class="grammar-sentences">
      <div class="grammar-sentence">I <strong>manage</strong> the compliance department.</div>
      <div class="grammar-sentence">She <strong>coordinates</strong> with FIFA every quarter.</div>
      <div class="grammar-sentence">He <strong>reports</strong> to the General Director.</div>
      <div class="grammar-sentence"><strong>Does</strong> he <strong>manage</strong> the department?</div>
    </div>
    <p style="text-align:center;margin-top:1.5rem;font-style:italic;color:var(--text-dim)">What do the highlighted words have in common?</p>
    <div style="text-align:center;margin-top:1rem"><button class="btn-primary" onclick="revealGrammar()">Reveal the Rule</button></div>
    <div class="grammar-table-wrap" id="grammarTable">
      <table class="grammar-table">
        <thead><tr><th>Form</th><th>Structure</th><th>Example</th></tr></thead>
        <tbody>
          <tr><td>Affirmative</td><td>I/You/We/They + verb</td><td>I <strong>manage</strong> the team.</td></tr>
          <tr><td>Affirmative</td><td>He/She/It + verb + <strong>s</strong></td><td>She <strong>coordinates</strong> with FIFA.</td></tr>
          <tr><td>Negative</td><td>do/does + not + verb</td><td>He <strong>does not work</strong> alone.</td></tr>
          <tr><td>Question</td><td>Do/Does + subject + verb</td><td><strong>Does</strong> he <strong>manage</strong>?</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="slide slide-light" data-slide="10" data-phase="3" data-teacher="Erro Comum (3 min): Mostre a versão errada. Pergunte: &quot;Can you find the mistake?&quot; Drilling da frase correta 3x.">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 3: The Code</div>
    <h2 class="slide-heading">Common <span class="accent">Mistake</span></h2>
    <div class="mistake-card">
      <div class="mistake-item mistake-wrong"><div class="mistake-icon"><svg viewBox="0 0 24 24" fill="none" stroke="#dc2626" stroke-width="2.5"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></div>&ldquo;He manage the department.&rdquo;</div>
      <div class="mistake-item mistake-right"><div class="mistake-icon"><svg viewBox="0 0 24 24" fill="none" stroke="#16a34a" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg></div>&ldquo;He manage<strong>s</strong> the department.&rdquo;</div>
    </div>
    <div class="mistake-card" style="margin-top:1.5rem">
      <div class="mistake-item mistake-wrong"><div class="mistake-icon"><svg viewBox="0 0 24 24" fill="none" stroke="#dc2626" stroke-width="2.5"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></div>&ldquo;Does she coordinates with FIFA?&rdquo;</div>
      <div class="mistake-item mistake-right"><div class="mistake-icon"><svg viewBox="0 0 24 24" fill="none" stroke="#16a34a" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg></div>&ldquo;Does she coordinate with FIFA?&rdquo;</div>
    </div>
  </div>
</div>

<div class="slide slide-light" data-slide="11" data-phase="3" data-teacher="Grammar Practice (5 min): Nilo completa ORALMENTE antes de clicar. Se errar, pergunte: &quot;Is this he/she or I/we?&quot;">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 3: The Code</div>
    <h2 class="slide-heading">Grammar <span class="accent">Practice</span></h2>
    <div class="fill-grid">
      <div class="fill-item" onclick="revealFill(this)"><div class="fill-text">She <span class="fill-blank">___</span><span class="fill-answer">coordinates</span> with the legal team every week.</div></div>
      <div class="fill-item" onclick="revealFill(this)"><div class="fill-text">I <span class="fill-blank">___</span><span class="fill-answer">report</span> directly to the General Director.</div></div>
      <div class="fill-item" onclick="revealFill(this)"><div class="fill-text"><span class="fill-blank">___</span><span class="fill-answer">Does</span> the team <span class="fill-blank">___</span><span class="fill-answer">investigate</span> every complaint?</div></div>
      <div class="fill-item" onclick="revealFill(this)"><div class="fill-text">He <span class="fill-blank">___</span><span class="fill-answer">does not manage</span> the legal department. He <span class="fill-blank">___</span><span class="fill-answer">manages</span> compliance.</div></div>
    </div>
  </div>
</div>

<div class="slide slide-light" data-slide="12" data-phase="3" data-teacher="CCQs (2 min): &quot;She coordinates with FIFA. Does she do this one time or regularly?&quot; (regularly). &quot;Does he manage: why no -s?&quot; (DOES carries it).">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 3: The Code</div>
    <h2 class="slide-heading">Quick <span class="accent">Check</span></h2>
    <div class="comp-questions">
      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">1. &ldquo;She coordinates with FIFA.&rdquo; Does she do this one time or regularly?</div><div class="q-answer">Regularly. Present Simple = habits and routines.</div></div>
      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">2. &ldquo;Does he manage?&rdquo; Why no -s on manage?</div><div class="q-answer">Because DOES already carries the third-person marker.</div></div>
      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">3. &ldquo;They investigate violations.&rdquo; Temporary or permanent?</div><div class="q-answer">Permanent. It is part of their job responsibilities.</div></div>
    </div>
  </div>
</div>

<!-- ══════ CHAPTER 4: GETTING THERE ══════ -->

<div class="slide slide-image" data-slide="13" data-phase="4" data-teacher="Transição. Diga: &quot;Now let us put your vocabulary and grammar into real context.&quot;" style="background-image:url('https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=1400&q=80')">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 4</div>
    <h2 class="slide-title">Getting <span class="accent">There</span></h2>
    <p class="slide-subtitle">An org chart, listening exercises, and a networking dialogue about your department.</p>
  </div>
</div>

<div class="slide slide-light" data-slide="14" data-phase="4" data-teacher="Artefato (5 min): Mostre o organograma. Pergunte: &quot;Who does Nilo report to?&quot;, &quot;How many people does Nilo manage?&quot;, &quot;What are the three responsibilities?&quot;">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 4: Getting There</div>
    <h2 class="slide-heading">Compliance <span class="accent">Structure</span></h2>
    <div class="email-card" style="max-width:600px;margin:1rem auto">
      <div class="email-header" style="background:linear-gradient(135deg,#1a365d,#7B2D3B);text-align:center;padding:1rem"><strong style="color:#fff;font-size:.85rem;letter-spacing:2px">CORINTHIANS COMPLIANCE DEPARTMENT</strong></div>
      <div class="email-body-ic" style="text-align:center;padding:1.5rem">
        <p style="margin-bottom:.8rem"><strong>General Director</strong></p>
        <p style="color:var(--text-dim);font-size:.8rem">&darr; reports to</p>
        <p style="margin:.8rem 0;padding:.6rem;background:var(--accent);color:#fff;border-radius:8px;font-weight:700">Nilo Patucci &mdash; Chief Compliance Officer</p>
        <p style="color:var(--text-dim);font-size:.8rem">&darr; manages team of 5</p>
        <div style="display:flex;gap:.6rem;justify-content:center;margin-top:.8rem;flex-wrap:wrap">
          <span style="padding:.4rem .8rem;background:var(--accent-dim);border:1px solid rgba(123,45,59,.2);border-radius:6px;font-size:.78rem"><strong>Enforce</strong> Regulations</span>
          <span style="padding:.4rem .8rem;background:var(--accent-dim);border:1px solid rgba(123,45,59,.2);border-radius:6px;font-size:.78rem"><strong>Investigate</strong> Violations</span>
          <span style="padding:.4rem .8rem;background:var(--accent-dim);border:1px solid rgba(123,45,59,.2);border-radius:6px;font-size:.78rem"><strong>Coordinate</strong> Auditors</span>
        </div>
        <p style="font-size:.78rem;color:var(--text-dim);margin-top:.8rem"><strong>Headquarters:</strong> Barra Funda, Sao Paulo</p>
      </div>
    </div>
  </div>
</div>

<div class="slide slide-light" data-slide="15" data-phase="4" data-teacher="Comprehensão (3 min): Perguntas orais sobre o organograma.">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 4: Getting There</div>
    <h2 class="slide-heading">Org Chart <span class="accent">Comprehension</span></h2>
    <div class="comp-questions">
      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">1. Who does Nilo report to?</div><div class="q-answer">The General Director.</div></div>
      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">2. What are the three main responsibilities?</div><div class="q-answer">Enforce regulations, investigate violations, coordinate with auditors.</div></div>
      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">3. Where is the headquarters?</div><div class="q-answer">Barra Funda, Sao Paulo.</div></div>
    </div>
  </div>
</div>

<div class="slide slide-dark" data-slide="16" data-phase="4" data-teacher="Listening 1 (5 min): Toque o áudio (voz Ash). Nilo ouve SEM texto. Depois perguntas.">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label">Chapter 4: Getting There</div>
    <h2 class="slide-heading">Listen to This <span class="accent">Description</span></h2>
    <p style="color:rgba(255,255,255,.7);margin-bottom:1.5rem">Listen carefully. Questions will appear after the audio ends.</p>
    <div class="listening-player" id="lp-listen1" data-src="/audio/nilo-mesquita-patucci/aula2_listening1_department.mp3">
      <div class="lp-seekbar" onclick="seekAudio(event,'lp-listen1')"><div class="lp-progress" id="progress-lp-listen1"></div></div>
      <div class="lp-time"><span id="time-current-lp-listen1">0:00</span><span id="time-total-lp-listen1">0:00</span></div>
      <div class="lp-controls"><button class="lp-btn" onclick="skipAudio('lp-listen1',-5)"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="11 17 6 12 11 7"/><line x1="6" y1="12" x2="18" y2="12"/></svg></button><button class="lp-btn lp-play" onclick="togglePlayer('lp-listen1')"><svg viewBox="0 0 24 24"><polygon points="6 3 20 12 6 21 6 3" fill="currentColor"/></svg></button><button class="lp-btn" onclick="skipAudio('lp-listen1',5)"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="13 7 18 12 13 17"/><line x1="6" y1="12" x2="18" y2="12"/></svg></button></div>
      <div class="lp-label">Speed</div>
      <div class="lp-speed"><button class="lp-speed-btn" onclick="setPlayerSpeed('lp-listen1',0.5,this)">0.5x</button><button class="lp-speed-btn" onclick="setPlayerSpeed('lp-listen1',0.75,this)">0.75x</button><button class="lp-speed-btn active" onclick="setPlayerSpeed('lp-listen1',1,this)">1x</button><button class="lp-speed-btn" onclick="setPlayerSpeed('lp-listen1',1.25,this)">1.25x</button></div>
    </div>
    <div class="comp-questions" id="questions-lp-listen1" style="display:none">
      <div class="comp-q" onclick="revealComp(this)" style="background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.15)"><div class="q-text" style="color:rgba(255,255,255,.9)">1. How many employees in the department?</div><div class="q-answer" style="color:#F0B8C4">Five full-time employees.</div></div>
      <div class="comp-q" onclick="revealComp(this)" style="background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.15)"><div class="q-text" style="color:rgba(255,255,255,.9)">2. Who does Nilo report to?</div><div class="q-answer" style="color:#F0B8C4">The General Director.</div></div>
      <div class="comp-q" onclick="revealComp(this)" style="background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.15)"><div class="q-text" style="color:rgba(255,255,255,.9)">3. What are the three main responsibilities?</div><div class="q-answer" style="color:#F0B8C4">Enforce regulations, investigate violations, coordinate with auditors and CBF.</div></div>
    </div>
  </div>
</div>

<div class="slide slide-dark" data-slide="17" data-phase="4" data-teacher="Diálogo (10 min): Lisa Park (voz Riley) e Nilo (voz Ash). Fase 1: ouçam. Fase 2: Nilo lê suas falas. Fase 3: invertem papéis.">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 4: Getting There</div>
    <h2 class="slide-heading" style="text-align:center">FIFA Networking <span class="accent">Dialogue</span></h2>
    <div class="dialogue-box" id="dialogueBox">
      <div class="dialogue-line visible" data-line="1" data-voice="riley"><div class="dialogue-avatar" style="background:#3B7DD8">L</div><div class="dialogue-bubble dr-bubble">So, Nilo, what does a typical day look like for you at Corinthians?<span class="audio-inline" onclick="speakText('So, Nilo, what does a typical day look like for you at Corinthians?',this)"><svg viewBox="0 0 24 24" style="width:14px;height:14px" fill="none" stroke="var(--accent)" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg></span></div></div>
      <div class="dialogue-line" data-line="2" data-voice="ash"><div class="dialogue-avatar" style="background:var(--accent)">N</div><div class="dialogue-bubble patricia-bubble">Well, I <span class="vocab-highlight">manage</span> the compliance <span class="vocab-highlight">department</span>. We have a team of five people who work directly with me.<span class="audio-inline" onclick="speakText('Well, I manage the compliance department. We have a team of five people who work directly with me.',this)"><svg viewBox="0 0 24 24" style="width:14px;height:14px" fill="none" stroke="var(--accent)" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg></span></div></div>
      <div class="dialogue-line" data-line="3" data-voice="riley"><div class="dialogue-avatar" style="background:#3B7DD8">L</div><div class="dialogue-bubble dr-bubble">That sounds like a lot of <span class="vocab-highlight">responsibility</span>. Who do you <span class="vocab-highlight">report to</span>?<span class="audio-inline" onclick="speakText('That sounds like a lot of responsibility. Who do you report to?',this)"><svg viewBox="0 0 24 24" style="width:14px;height:14px" fill="none" stroke="var(--accent)" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg></span></div></div>
      <div class="dialogue-line" data-line="4" data-voice="ash"><div class="dialogue-avatar" style="background:var(--accent)">N</div><div class="dialogue-bubble patricia-bubble">I <span class="vocab-highlight">report to</span> the General Director. I also <span class="vocab-highlight">coordinate</span> with the legal department on investigations.<span class="audio-inline" onclick="speakText('I report to the General Director. I also coordinate with the legal department on investigations.',this)"><svg viewBox="0 0 24 24" style="width:14px;height:14px" fill="none" stroke="var(--accent)" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg></span></div></div>
      <div class="dialogue-line" data-line="5" data-voice="riley"><div class="dialogue-avatar" style="background:#3B7DD8">L</div><div class="dialogue-bubble dr-bubble">Interesting! And where is your <span class="vocab-highlight">headquarters</span>?<span class="audio-inline" onclick="speakText('Interesting! And where is your headquarters?',this)"><svg viewBox="0 0 24 24" style="width:14px;height:14px" fill="none" stroke="var(--accent)" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg></span></div></div>
      <div class="dialogue-line" data-line="6" data-voice="ash"><div class="dialogue-avatar" style="background:var(--accent)">N</div><div class="dialogue-bubble patricia-bubble">Our <span class="vocab-highlight">headquarters</span> is in the Parque Sao Jorge area. But I work from Barra Funda.<span class="audio-inline" onclick="speakText('Our headquarters is in the Parque Sao Jorge area of Sao Paulo. But I work from our office in Barra Funda.',this)"><svg viewBox="0 0 24 24" style="width:14px;height:14px" fill="none" stroke="var(--accent)" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg></span></div></div>
      <div class="dialogue-line" data-line="7" data-voice="riley"><div class="dialogue-avatar" style="background:#3B7DD8">L</div><div class="dialogue-bubble dr-bubble">What is the hardest part of your job?<span class="audio-inline" onclick="speakText('What is the hardest part of your job?',this)"><svg viewBox="0 0 24 24" style="width:14px;height:14px" fill="none" stroke="var(--accent)" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg></span></div></div>
      <div class="dialogue-line" data-line="8" data-voice="ash"><div class="dialogue-avatar" style="background:var(--accent)">N</div><div class="dialogue-bubble patricia-bubble"><span class="vocab-highlight">Investigating</span> potential violations is challenging. We <span class="vocab-highlight">enforce</span> FIFA regulations at the club level, and sometimes that creates tension.<span class="audio-inline" onclick="speakText('Investigating potential violations is challenging. We enforce FIFA regulations at the club level, and sometimes that creates tension.',this)"><svg viewBox="0 0 24 24" style="width:14px;height:14px" fill="none" stroke="var(--accent)" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg></span></div></div>
    </div>
    <button class="btn-primary" id="nextLineBtn" onclick="nextDialogueLine()">Next Line</button>
  </div>
</div>

<div class="slide slide-light" data-slide="18" data-phase="4" data-teacher="Comprehensão (3 min): Perguntas sobre LISA (interlocutor).">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 4: Getting There</div>
    <h2 class="slide-heading">Dialogue <span class="accent">Comprehension</span></h2>
    <div class="comp-questions">
      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">1. What did Lisa ask about first?</div><div class="q-answer">What a typical day looks like at Corinthians.</div></div>
      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">2. What did Lisa call &ldquo;a lot of&rdquo;?</div><div class="q-answer">Responsibility.</div></div>
      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">3. What was Lisa&rsquo;s last question about?</div><div class="q-answer">The hardest part of the job.</div></div>
    </div>
  </div>
</div>

<div class="slide slide-dark" data-slide="19" data-phase="4" data-teacher="Listening 2 (5 min): Voz Riley (Dr. Amara Osei, Ghana). Nilo ouve sem texto. Depois perguntas.">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label">Chapter 4: Getting There</div>
    <h2 class="slide-heading">Another <span class="accent">Organization</span></h2>
    <p style="color:rgba(255,255,255,.7);margin-bottom:1.5rem">Listen to another delegate describe their organization.</p>
    <div class="listening-player" id="lp-listen2" data-src="/audio/nilo-mesquita-patucci/aula2_listening2_amara.mp3">
      <div class="lp-seekbar" onclick="seekAudio(event,'lp-listen2')"><div class="lp-progress" id="progress-lp-listen2"></div></div>
      <div class="lp-time"><span id="time-current-lp-listen2">0:00</span><span id="time-total-lp-listen2">0:00</span></div>
      <div class="lp-controls"><button class="lp-btn" onclick="skipAudio('lp-listen2',-5)"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="11 17 6 12 11 7"/><line x1="6" y1="12" x2="18" y2="12"/></svg></button><button class="lp-btn lp-play" onclick="togglePlayer('lp-listen2')"><svg viewBox="0 0 24 24"><polygon points="6 3 20 12 6 21 6 3" fill="currentColor"/></svg></button><button class="lp-btn" onclick="skipAudio('lp-listen2',5)"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="13 7 18 12 13 17"/><line x1="6" y1="12" x2="18" y2="12"/></svg></button></div>
      <div class="lp-label">Speed</div>
      <div class="lp-speed"><button class="lp-speed-btn" onclick="setPlayerSpeed('lp-listen2',0.5,this)">0.5x</button><button class="lp-speed-btn" onclick="setPlayerSpeed('lp-listen2',0.75,this)">0.75x</button><button class="lp-speed-btn active" onclick="setPlayerSpeed('lp-listen2',1,this)">1x</button><button class="lp-speed-btn" onclick="setPlayerSpeed('lp-listen2',1.25,this)">1.25x</button></div>
    </div>
    <div class="comp-questions" id="questions-lp-listen2" style="display:none">
      <div class="comp-q" onclick="revealComp(this)" style="background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.15)"><div class="q-text" style="color:rgba(255,255,255,.9)">1. What is Dr. Osei&rsquo;s role?</div><div class="q-answer" style="color:#F0B8C4">She manages the governance unit at the Ghana Football Association.</div></div>
      <div class="comp-q" onclick="revealComp(this)" style="background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.15)"><div class="q-text" style="color:rgba(255,255,255,.9)">2. How many people on her team?</div><div class="q-answer" style="color:#F0B8C4">Eight.</div></div>
      <div class="comp-q" onclick="revealComp(this)" style="background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.15)"><div class="q-text" style="color:rgba(255,255,255,.9)">3. What do they investigate?</div><div class="q-answer" style="color:#F0B8C4">Match-fixing allegations.</div></div>
    </div>
  </div>
</div>

<!-- ══════ CHAPTER 5: PRACTICE ══════ -->

<div class="slide slide-image" data-slide="20" data-phase="5" data-teacher="Transição." style="background-image:url('https://images.unsplash.com/photo-1517649763962-0c623066013b?w=1400&q=80')">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 5</div>
    <h2 class="slide-title"><span class="accent">Practice</span></h2>
    <p class="slide-subtitle">Quick challenges, error spotting, and oral drilling to sharpen your skills.</p>
  </div>
</div>

<div class="slide slide-light" data-slide="21" data-phase="5" data-teacher="Quick Fire (8 min): Uma por vez. Nilo responde ORALMENTE, clica Show Answer.">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 5: Practice</div>
    <h2 class="slide-heading">Quick <span class="accent">Fire</span></h2>
    <div style="position:relative"><div class="challenge-score" id="challengeScore">0 / 6</div>
    <div class="challenge-card" id="challengeCard"><div class="challenge-counter" id="challengeCounter">Question 1 of 6</div><div class="challenge-prompt" id="challengePrompt">Someone asks: &ldquo;What do you do at Corinthians?&rdquo; Describe your role.</div><div class="challenge-answer" id="challengeAnswer">&ldquo;I manage the compliance department. My responsibilities include enforcing FIFA regulations.&rdquo;</div><button class="btn-primary" id="showAnswerBtn" onclick="showChallengeAnswer()">Show Answer</button><button class="btn-secondary" id="nextChallengeBtn" onclick="nextChallenge()" style="display:none">Next Question</button></div></div>
  </div>
</div>

<div class="slide slide-light" data-slide="22" data-phase="5" data-teacher="Spot the Error (5 min): Nilo identifica antes de clicar.">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 5: Practice</div>
    <h2 class="slide-heading">Spot the <span class="accent">Error</span></h2>
    <div class="error-grid">
      <div class="error-card" onclick="revealError(this)"><div class="error-sentence">&ldquo;He manage the compliance department.&rdquo;</div><div class="error-fix">&ldquo;He manage<strong>s</strong> the compliance department.&rdquo;</div></div>
      <div class="error-card" onclick="revealError(this)"><div class="error-sentence">&ldquo;Does she coordinates with FIFA?&rdquo;</div><div class="error-fix">&ldquo;Does she coordinate with FIFA?&rdquo;</div></div>
      <div class="error-card" onclick="revealError(this)"><div class="error-sentence">&ldquo;I am report to the General Director.&rdquo;</div><div class="error-fix">&ldquo;I report to the General Director.&rdquo;</div></div>
      <div class="error-card" onclick="revealError(this)"><div class="error-sentence">&ldquo;The team investigate the violations every month.&rdquo;</div><div class="error-fix">&ldquo;The team investigate<strong>s</strong> the violations every month.&rdquo;</div></div>
    </div>
    <div class="error-score" id="errorScore">0 / 4 errors found</div>
  </div>
</div>

<div class="slide slide-light" data-slide="23" data-phase="5" data-teacher="Oral Drilling (5 min): Leia cada situação. Nilo responde. Depois revele.">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 5: Practice</div>
    <h2 class="slide-heading">Oral <span class="accent">Drilling</span> (1/2)</h2>
    <div class="oral-grid">
      <div class="oral-item" onclick="this.classList.toggle('revealed')"><div class="oral-situation">1. Describe your department in one sentence.</div><div class="oral-model">&ldquo;I manage the compliance department at Corinthians.&rdquo;</div></div>
      <div class="oral-item" onclick="this.classList.toggle('revealed')"><div class="oral-situation">2. Who is your direct supervisor?</div><div class="oral-model">&ldquo;I report to the General Director.&rdquo;</div></div>
      <div class="oral-item" onclick="this.classList.toggle('revealed')"><div class="oral-situation">3. How do you work with other departments?</div><div class="oral-model">&ldquo;I coordinate with the legal department on investigations.&rdquo;</div></div>
    </div>
  </div>
</div>

<div class="slide slide-light" data-slide="24" data-phase="5" data-teacher="Oral Drilling 2 (5 min).">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 5: Practice</div>
    <h2 class="slide-heading">Oral <span class="accent">Drilling</span> (2/2)</h2>
    <div class="oral-grid">
      <div class="oral-item" onclick="this.classList.toggle('revealed')"><div class="oral-situation">4. Where is the main office?</div><div class="oral-model">&ldquo;Our headquarters is in Sao Paulo.&rdquo;</div></div>
      <div class="oral-item" onclick="this.classList.toggle('revealed')"><div class="oral-situation">5. What does your team do when there is a problem?</div><div class="oral-model">&ldquo;We investigate potential violations of governance rules.&rdquo;</div></div>
      <div class="oral-item" onclick="this.classList.toggle('revealed')"><div class="oral-situation">6. How do you make sure people follow the rules?</div><div class="oral-model">&ldquo;We enforce internal regulations and FIFA standards.&rdquo;</div></div>
    </div>
  </div>
</div>

<div class="slide slide-light" data-slide="25" data-phase="5" data-teacher="Sentence Building (5 min): Nilo monta oralmente.">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 5: Practice</div>
    <h2 class="slide-heading">Sentence <span class="accent">Building</span></h2>
    <div class="oral-grid">
      <div class="oral-item" onclick="this.classList.toggle('revealed')"><div class="oral-situation">department / the / compliance / manage / I</div><div class="oral-model">&ldquo;I manage the compliance department.&rdquo;</div></div>
      <div class="oral-item" onclick="this.classList.toggle('revealed')"><div class="oral-situation">to / Director / I / the / General / report</div><div class="oral-model">&ldquo;I report to the General Director.&rdquo;</div></div>
      <div class="oral-item" onclick="this.classList.toggle('revealed')"><div class="oral-situation">coordinates / she / quarter / every / FIFA / with</div><div class="oral-model">&ldquo;She coordinates with FIFA every quarter.&rdquo;</div></div>
      <div class="oral-item" onclick="this.classList.toggle('revealed')"><div class="oral-situation">regulations / enforce / we / FIFA / club / the / at</div><div class="oral-model">&ldquo;We enforce FIFA regulations at the club.&rdquo;</div></div>
      <div class="oral-item" onclick="this.classList.toggle('revealed')"><div class="oral-situation">does / team / the / what / do / ?</div><div class="oral-model">&ldquo;What does the team do?&rdquo;</div></div>
    </div>
  </div>
</div>

<div class="slide slide-light" data-slide="26" data-phase="5" data-teacher="Pronúncia (5 min): Drilling 3x cada.">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 5: Practice</div>
    <h2 class="slide-heading">Pronunciation <span class="accent">Focus</span></h2>
    <div class="oral-grid" style="text-align:center">
      <div class="oral-item" style="cursor:default"><div class="oral-situation" style="font-size:1.2rem"><strong>de</strong>&middot;PART&middot;ment<br><button class="audio-btn-sm" onclick="speakText('Department',this)" style="margin-top:.5rem"><svg viewBox="0 0 24 24" style="width:12px;height:12px" fill="none" stroke="#fff" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div></div>
      <div class="oral-item" style="cursor:default"><div class="oral-situation" style="font-size:1.2rem">co&middot;<strong>OR</strong>&middot;di&middot;nate<br><button class="audio-btn-sm" onclick="speakText('Coordinate',this)" style="margin-top:.5rem"><svg viewBox="0 0 24 24" style="width:12px;height:12px" fill="none" stroke="#fff" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div></div>
      <div class="oral-item" style="cursor:default"><div class="oral-situation" style="font-size:1.2rem">in&middot;<strong>VES</strong>&middot;ti&middot;gate<br><button class="audio-btn-sm" onclick="speakText('Investigate',this)" style="margin-top:.5rem"><svg viewBox="0 0 24 24" style="width:12px;height:12px" fill="none" stroke="#fff" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div></div>
      <div class="oral-item" style="cursor:default"><div class="oral-situation" style="font-size:1.2rem"><strong>HEAD</strong>&middot;quar&middot;ters<br><button class="audio-btn-sm" onclick="speakText('Headquarters',this)" style="margin-top:.5rem"><svg viewBox="0 0 24 24" style="width:12px;height:12px" fill="none" stroke="#fff" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div></div>
    </div>
  </div>
</div>

<!-- ══════ CHAPTER 6: YOUR TURN ══════ -->

<div class="slide slide-image" data-slide="27" data-phase="6" data-teacher="Transição. Diga: &quot;Now it is your turn. Three role-plays: guided, semi-free, and free.&quot;" style="background-image:url('https://images.unsplash.com/photo-1475721027785-f74eccf877e2?w=1400&q=80')">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 6</div>
    <h2 class="slide-title">Your <span class="accent">Turn</span></h2>
    <p class="slide-subtitle">Three role-plays, from guided to completely free. No corrections during production, only after.</p>
  </div>
</div>

<div class="slide slide-dark" data-slide="28" data-phase="6" data-teacher="Role-play Guiado (5 min): Professor é delegate. Nilo descreve departamento. NÃO corrija, anote.">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 6: Your Turn</div>
    <h2 class="slide-heading">Role-play: <span class="accent">Guided</span></h2>
    <div class="roleplay-card"><div class="card-icon" style="background:linear-gradient(135deg,#7B2D3B,#9A4054);height:80px;display:flex;align-items:center;justify-content:center;border-radius:14px 14px 0 0"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" style="width:40px;height:40px"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4-4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/></svg></div><div class="roleplay-body"><div class="roleplay-scenario">A delegate from Japan asks you to describe your department at Corinthians. Use the keywords below.</div><div class="roleplay-keywords"><span class="roleplay-kw">department</span><span class="roleplay-kw">manage</span><span class="roleplay-kw">report to</span><span class="roleplay-kw">responsibilities</span><span class="roleplay-kw">five people</span><span class="roleplay-kw">headquarters</span></div></div></div>
  </div>
</div>

<div class="slide slide-dark" data-slide="29" data-phase="6" data-teacher="Semi-livre (5 min): Menos keywords. Nilo explica o que torna seu papel único.">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 6: Your Turn</div>
    <h2 class="slide-heading">Role-play: <span class="accent">Semi-free</span></h2>
    <div class="roleplay-card"><div class="card-icon" style="background:linear-gradient(135deg,#4A3728,#6B5240);height:80px;display:flex;align-items:center;justify-content:center;border-radius:14px 14px 0 0"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" style="width:40px;height:40px"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/></svg></div><div class="roleplay-body"><div class="roleplay-scenario">You are having lunch with delegates. They want to know how your organization is structured and what makes your role unique.</div><div class="roleplay-keywords"><span class="roleplay-kw">enforce</span><span class="roleplay-kw">investigate</span><span class="roleplay-kw">coordinate</span></div></div></div>
  </div>
</div>

<div class="slide slide-dark" data-slide="30" data-phase="6" data-teacher="Livre (5 min): ZERO apoio. NÃO corrija. Anote erros para o próximo slide.">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 6: Your Turn</div>
    <h2 class="slide-heading">Role-play: <span class="accent">Free</span></h2>
    <div class="roleplay-card"><div class="card-icon" style="background:linear-gradient(135deg,#2C5282,#3B7DD8);height:80px;display:flex;align-items:center;justify-content:center;border-radius:14px 14px 0 0"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" style="width:40px;height:40px"><circle cx="12" cy="12" r="10"/><path d="M2 12h20"/></svg></div><div class="roleplay-body"><div class="roleplay-scenario">The FIFA program director asks you to explain your organization to the entire group. Speak for 2 minutes. No keywords. No script. Just you and your professional world.</div></div></div>
  </div>
</div>

<div class="slide slide-light" data-slide="31" data-phase="6" data-teacher="Delayed Error Correction (5 min): Compartilhe 3-5 erros. Foque no Present Simple (3a pessoa -s, forma com does). Nilo repete a versão correta 2x.">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 6: Your Turn</div>
    <h2 class="slide-heading">Error <span class="accent">Correction</span></h2>
    <p style="font-size:.9rem;color:var(--text-dim);margin-bottom:1rem">Teacher: type the errors you observed during the free role-play.</p>
    <div style="background:#fff;border:2px solid var(--border);border-radius:10px;padding:1.5rem;min-height:200px" contenteditable="true"><p style="color:var(--text-dim);font-style:italic">Click here and type the errors observed...</p></div>
  </div>
</div>

<div class="slide slide-dark" data-slide="32" data-phase="6" data-teacher="Produção (5 min): Nilo descreve o departamento gravando 2 min.">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label">Chapter 6: Your Turn</div>
    <h2 class="slide-heading">Describe Your <span class="accent">Department</span></h2>
    <div class="record-card"><div class="record-prompt">Describe your department to a new colleague. Include: what you manage, who you report to, your responsibilities, and where your headquarters is.</div><button class="record-btn" onclick="toggleReflectionRecord(this)"><svg viewBox="0 0 24 24" style="width:28px;height:28px"><path d="M12 1a3 3 0 00-3 3v8a3 3 0 006 0V4a3 3 0 00-3-3z" fill="#fff"/><path d="M19 10v2a7 7 0 01-14 0v-2" fill="none" stroke="#fff" stroke-width="2"/></svg></button><div id="reflectionResult"></div></div>
  </div>
</div>

<!-- ══════ CHAPTER 7: WRAP-UP ══════ -->

<div class="slide slide-image" data-slide="33" data-phase="7" data-teacher="Transição." style="background-image:url('https://images.unsplash.com/photo-1504384308090-c894fdcc538d?w=1400&q=80')">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 7</div>
    <h2 class="slide-title"><span class="accent">Wrap</span>-up</h2>
    <p class="slide-subtitle">Let us review what you learned today and celebrate your progress.</p>
  </div>
</div>

<div class="slide slide-light" data-slide="34" data-phase="7" data-teacher="Checklist (3 min): Leia cada item. Pergunte: &quot;Can you say yes to this?&quot; Clique juntos.">
  <div class="slide-inner">
    <div class="chapter-label">Self-Assessment</div>
    <h2 class="slide-heading">What I <span class="accent">Learned</span></h2>
    <div class="check-grid" id="checkGrid">
      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div><span>I can describe my department and responsibilities.</span></div>
      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div><span>I know 8 words about organizational structure.</span></div>
      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div><span>I can use Present Simple for routines and facts.</span></div>
      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div><span>I can add -s to verbs with he/she/it.</span></div>
      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div><span>I can explain who I report to.</span></div>
      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div><span>I can ask questions with &ldquo;Does he/she...?&rdquo;</span></div>
      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div><span>I understand the structure of a compliance department.</span></div>
      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg></div><span>I feel more confident describing my professional world.</span></div>
    </div>
  </div>
</div>

<div class="slide slide-dark" data-slide="35" data-phase="7" data-teacher="Celebração (1 min): Valide o progresso.">
  <div class="slide-inner">
    <div class="badge-card"><div class="badge-icon"><div class="badge-circle"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" style="width:48px;height:48px"><path d="M12 15l-3 3 1 4 2-1 2 1 1-4-3-3z"/><circle cx="12" cy="8" r="7"/></svg></div><div class="sparkles"><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div></div></div><h2 style="color:#fff;font-family:'Cormorant Garamond',serif;font-size:2rem">Aula 2 Complete!</h2><p style="color:rgba(255,255,255,.7);margin-top:.5rem">Your professional world is now in English.</p></div>
  </div>
</div>

<div class="slide slide-dark" data-slide="36" data-phase="7" data-teacher="Preview (2 min): &quot;Next class: Career Timeline. We will practice talking about your professional history.&quot; Homework (ORAL): 1) Gravar áudio descrevendo o departamento. 2) Ouvir ESPN FC. 3) Anotar 3 frases de rotina.">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label">Next Lesson Preview</div>
    <h2 class="slide-heading">Coming <span class="accent">Next</span></h2>
    <p class="slide-subtitle" style="margin-top:1rem;opacity:.8">Aula 3: Career Timeline &mdash; Narrating Professional History</p>
    <p class="slide-subtitle" style="opacity:.5;font-size:.85rem;margin-top:1rem">Homework is given orally by the teacher.</p>
  </div>
</div>

<div class="slide slide-image" data-slide="37" data-phase="7" data-teacher="Encerramento (1 min): &quot;Great class, Nilo. Your professional world is ready for Miami.&quot;" style="background-image:url('https://images.unsplash.com/photo-1497366216548-37526070297c?w=1400&q=80')">
  <div class="slide-inner">
    <div class="chapter-label">Lesson Complete</div>
    <h2 class="slide-title">Day 2 &mdash; <span class="accent">Complete.</span></h2>
    <p class="slide-subtitle" style="opacity:.8;margin-top:1rem">Next: Career Timeline</p>
  </div>
</div>

</div><!-- /slides-container -->
</div><!-- /slides-wrapper -->

<!-- Teacher T Icon -->
<div class="teacher-t" id="teacherT">T<div class="teacher-t-panel" id="teacherPanel"></div></div>

<!-- Navigation Bar -->
<div class="nav-bar">
  <button class="nav-btn" id="prevBtn" onclick="changeSlide(-1)" disabled><svg viewBox="0 0 24 24"><polyline points="15 18 9 12 15 6"/></svg></button>
  <div class="slide-dots" id="slideDots"></div>
  <button class="nav-btn" id="nextBtn" onclick="changeSlide(1)"><svg viewBox="0 0 24 24"><polyline points="9 6 15 12 9 18"/></svg></button>
</div>

<div class="confetti-container" id="confettiContainer"></div>

<script>
// ===== SLIDE NAVIGATION =====
var currentSlide = 1;
var totalSlides = 37;
var slidePhases = {1:1,2:1,3:1,4:1,5:2,6:2,7:2,8:3,9:3,10:3,11:3,12:3,13:4,14:4,15:4,16:4,17:4,18:4,19:4,20:5,21:5,22:5,23:5,24:5,25:5,26:5,27:6,28:6,29:6,30:6,31:6,32:6,33:7,34:7,35:7,36:7,37:7};

function changeSlide(dir) { var n=currentSlide+dir; if(n<1||n>totalSlides)return; goToSlide(n); }
function goToSlide(n) {
  var prev=document.querySelector('.slide[data-slide="'+currentSlide+'"]');
  if(prev) prev.classList.remove('active');
  currentSlide=n;
  var s=document.querySelector('.slide[data-slide="'+currentSlide+'"]');
  if(s){s.classList.add('active');s.scrollTop=0;}
  var t=s?s.getAttribute('data-teacher')||'':'';
  document.getElementById('teacherPanel').innerHTML=t;
  updateNav(); updatePhaseBar();
}
function updateNav() {
  document.getElementById('slideCounter').textContent=String(currentSlide).padStart(2,'0')+' / '+String(totalSlides).padStart(2,'0');
  document.getElementById('prevBtn').disabled=currentSlide===1;
  document.getElementById('nextBtn').disabled=currentSlide===totalSlides;
  document.querySelectorAll('.slide-dot').forEach(function(d,i){d.classList.toggle('active',i+1===currentSlide);});
}
function updatePhaseBar() {
  var cp=slidePhases[currentSlide];
  document.querySelectorAll('.phase-segment').forEach(function(seg){var p=parseInt(seg.dataset.phase);seg.classList.remove('completed','current','upcoming');if(p<cp)seg.classList.add('completed');else if(p===cp)seg.classList.add('current');else seg.classList.add('upcoming');});
  document.querySelectorAll('.phase-label').forEach(function(lbl){var p=parseInt(lbl.dataset.phase);lbl.classList.remove('completed','current');if(p<cp)lbl.classList.add('completed');else if(p===cp)lbl.classList.add('current');});
}
// Build dots
(function(){var d=document.getElementById('slideDots');for(var i=1;i<=totalSlides;i++){var dot=document.createElement('div');dot.className='slide-dot'+(i===1?' active':'');dot.onclick=(function(n){return function(){goToSlide(n);};})(i);d.appendChild(dot);}})();
// Keyboard nav
document.addEventListener('keydown',function(e){if(e.key==='ArrowRight'||e.key==='ArrowDown'){e.preventDefault();changeSlide(1);}if(e.key==='ArrowLeft'||e.key==='ArrowUp'){e.preventDefault();changeSlide(-1);}});

// ===== AUDIO =====
var currentAudio=null;
var audioSpeed=1;
function speakText(text,btn){if(currentAudio){currentAudio.pause();currentAudio.currentTime=0;}var f=audioMap[text]||audioMap[text.replace(/\\.$/,'')]||audioMap[text+'.'];if(f){currentAudio=new Audio(f);currentAudio.playbackRate=audioSpeed;currentAudio.play().catch(function(){ttsSpeak(text);});}else{ttsSpeak(text);}}
function ttsSpeak(t){if('speechSynthesis' in window){window.speechSynthesis.cancel();var u=new SpeechSynthesisUtterance(t);u.lang='en-US';u.rate=audioSpeed*0.85;window.speechSynthesis.speak(u);}}

// ===== VOCAB REVEAL (toggle) =====
function revealVocab(card){card.classList.toggle('revealed');var g=card.closest('.vocab-grid');var c=g.querySelectorAll('.vocab-card.revealed').length;var t=g.querySelectorAll('.vocab-card').length;var id=g.id==='vocabGrid1'?'vocabCount1':'vocabCount2';document.getElementById(id).textContent=c+' / '+t+' words revealed';}

// ===== GRAMMAR/FILL/COMP/ERROR =====
function revealGrammar(){document.getElementById('grammarTable').classList.add('show');}
function revealFill(item){item.classList.add('revealed');}
function revealComp(q){q.classList.add('revealed');}
var errorCount=0;
function revealError(card){if(card.classList.contains('revealed'))return;card.classList.add('revealed');errorCount++;document.getElementById('errorScore').textContent=errorCount+' / 4 errors found';}

// ===== DIALOGUE =====
var dialogueLine=0;
function nextDialogueLine(){dialogueLine++;var l=document.querySelector('.dialogue-line[data-line="'+dialogueLine+'"]');if(l){l.classList.add('visible');if(dialogueLine>=8){document.getElementById('nextLineBtn').textContent='Dialogue Complete';document.getElementById('nextLineBtn').disabled=true;}}}

// ===== QUICK CHALLENGE =====
var challenges=[
  {prompt:'Someone asks: "What do you do at Corinthians?" Describe your role.',answer:'"I manage the compliance department. My responsibilities include enforcing FIFA regulations."'},
  {prompt:'A delegate asks: "Who is your boss?" Answer formally.',answer:'"I report to the General Director of the club."'},
  {prompt:'Explain what your team does day to day.',answer:'"We enforce internal regulations, investigate potential violations, and coordinate with external auditors."'},
  {prompt:'Where is your headquarters?',answer:'"Our headquarters is in the Parque Sao Jorge area of Sao Paulo. I work from our office in Barra Funda."'},
  {prompt:'What is the most challenging part of your role?',answer:'"Investigating potential violations is challenging. We enforce regulations at the club level, and sometimes that creates tension."'},
  {prompt:'How does your department work with other departments?',answer:'"We coordinate with the legal department and with external auditors every quarter."'}
];
var challengeIndex=0,challengeCorrect=0;
function showChallengeAnswer(){document.getElementById('challengeAnswer').classList.add('show');document.getElementById('showAnswerBtn').style.display='none';document.getElementById('nextChallengeBtn').style.display='inline-flex';challengeCorrect++;document.getElementById('challengeScore').textContent=challengeCorrect+' / 6';}
function nextChallenge(){challengeIndex++;if(challengeIndex>=challenges.length){document.getElementById('challengeCard').innerHTML='<div style="text-align:center"><h3 style="font-family:Cormorant Garamond,serif;font-size:2rem;color:var(--accent)">Challenge Complete!</h3></div>';triggerConfetti();return;}document.getElementById('challengePrompt').textContent=challenges[challengeIndex].prompt;document.getElementById('challengeAnswer').textContent=challenges[challengeIndex].answer;document.getElementById('challengeAnswer').classList.remove('show');document.getElementById('showAnswerBtn').style.display='inline-flex';document.getElementById('nextChallengeBtn').style.display='none';document.getElementById('challengeCounter').textContent='Question '+(challengeIndex+1)+' of 6';}

// ===== LISTENING PLAYER =====
var lpPlayers={};
function initPlayer(id){var el=document.getElementById(id);if(!el)return;var src=el.getAttribute('data-src');if(!src)return;var audio=new Audio(src);lpPlayers[id]={audio:audio,speed:1,playing:false};audio.addEventListener('timeupdate',function(){updatePlayerUI(id);});audio.addEventListener('loadedmetadata',function(){updatePlayerUI(id);});audio.addEventListener('ended',function(){lpPlayers[id].playing=false;var pb=document.querySelector('#'+id+' .lp-play');if(pb)pb.classList.remove('playing');var qs=document.getElementById('questions-'+id);if(qs)qs.style.display='flex';});}
function togglePlayer(id){if(!lpPlayers[id])initPlayer(id);if(!lpPlayers[id])return;var p=lpPlayers[id];var pb=document.querySelector('#'+id+' .lp-play');if(p.playing){p.audio.pause();p.playing=false;if(pb)pb.classList.remove('playing');}else{if(currentAudio){currentAudio.pause();currentAudio.currentTime=0;}p.audio.playbackRate=p.speed;p.audio.play();p.playing=true;if(pb)pb.classList.add('playing');}}
function skipAudio(id,s){if(!lpPlayers[id])return;var a=lpPlayers[id].audio;a.currentTime=Math.max(0,Math.min(a.duration||0,a.currentTime+s));}
function seekAudio(e,id){if(!lpPlayers[id])return;var r=e.currentTarget.getBoundingClientRect();lpPlayers[id].audio.currentTime=((e.clientX-r.left)/r.width)*(lpPlayers[id].audio.duration||0);}
function setPlayerSpeed(id,speed,btn){if(!lpPlayers[id])initPlayer(id);if(!lpPlayers[id])return;lpPlayers[id].speed=speed;lpPlayers[id].audio.playbackRate=speed;var c=document.getElementById(id);if(c)c.querySelectorAll('.lp-speed-btn').forEach(function(b){b.classList.remove('active');});if(btn)btn.classList.add('active');}
function updatePlayerUI(id){var p=lpPlayers[id];if(!p)return;var c=p.audio.currentTime||0,t=p.audio.duration||0;var bar=document.getElementById('progress-'+id);if(bar)bar.style.width=(t>0?c/t*100:0)+'%';var tc=document.getElementById('time-current-'+id);var tt=document.getElementById('time-total-'+id);if(tc)tc.textContent=fmtTime(c);if(tt)tt.textContent=fmtTime(t);}
function fmtTime(s){if(isNaN(s))return'0:00';var m=Math.floor(s/60);var sec=Math.floor(s%60);return m+':'+(sec<10?'0':'')+sec;}

// ===== CHECKLIST + CONFETTI + RECORDING =====
function toggleCheck(item){item.classList.toggle('checked');}
function triggerConfetti(){var c=document.getElementById('confettiContainer');var colors=['#7B2D3B','#9A4054','#003080','#16a34a','#d97706','#3B7DD8'];for(var i=0;i<80;i++){var p=document.createElement('div');p.className='confetti-piece';p.style.left=Math.random()*100+'%';p.style.background=colors[Math.floor(Math.random()*colors.length)];p.style.animationDelay=Math.random()*2+'s';p.style.animationDuration=(2+Math.random()*2)+'s';var sz=4+Math.random()*8;p.style.width=sz+'px';p.style.height=sz+'px';p.style.borderRadius=Math.random()>.5?'50%':'2px';c.appendChild(p);}setTimeout(function(){c.innerHTML='';},5000);}
var reflectionRecording=false,reflectionRecorder=null,reflectionChunks=[];
function toggleReflectionRecord(btn){if(!reflectionRecording){navigator.mediaDevices.getUserMedia({audio:true}).then(function(stream){var mt=MediaRecorder.isTypeSupported('audio/mp4')?'audio/mp4':MediaRecorder.isTypeSupported('audio/webm;codecs=opus')?'audio/webm;codecs=opus':'';reflectionRecorder=mt?new MediaRecorder(stream,{mimeType:mt}):new MediaRecorder(stream);reflectionChunks=[];reflectionRecorder.ondataavailable=function(e){if(e.data.size>0)reflectionChunks.push(e.data);};reflectionRecorder.onstop=function(){var blob=new Blob(reflectionChunks,{type:reflectionRecorder.mimeType});var url=URL.createObjectURL(blob);document.getElementById('reflectionResult').innerHTML='<audio controls src="'+url+'" style="width:100%;margin-top:.5rem"><\\/audio>';stream.getTracks().forEach(function(t){t.stop();});};reflectionRecorder.start(100);btn.classList.add('recording');reflectionRecording=true;}).catch(function(){alert('Microphone access required.');});}else{if(reflectionRecorder&&reflectionRecorder.state==='recording')reflectionRecorder.stop();btn.classList.remove('recording');reflectionRecording=false;}}

// Init teacher panel
var is=document.querySelector('.slide[data-slide="1"]');
if(is)document.getElementById('teacherPanel').innerHTML=is.getAttribute('data-teacher')||'';
<\/script>
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.min.js"><\/script>
<script src="/lib/supabase-config.js"><\/script>
<script src="/lib/lesson-progress.js"><\/script>
</body>
</html>`;

fs.writeFileSync(path.join(BASE, 'public/professor/nilo-mesquita-patucci-aula2.html'), html);
console.log('Aula 2 rebuilt with main file CSS:', html.split('\\n').length, 'lines');
