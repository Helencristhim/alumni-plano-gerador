#!/usr/bin/env node
/**
 * Build Nilo Aula 3: Career Timeline — Present Perfect for experience
 * 1. Standalone IN CLASS file (same CSS as main file)
 * 2. Update main professor + aluno files (Pre-class, stamp, complementares, IN CLASS menu)
 */
const fs = require('fs');
const path = require('path');
const BASE = path.join(__dirname, '..');

// --- READ MAIN FILE FOR CSS ---
const mainFile = fs.readFileSync(path.join(BASE, 'public/professor/nilo-mesquita-patucci.html'), 'utf8');
const css = mainFile.match(/<style>([\s\S]*?)<\/style>/)[1];
const audioMapContent = mainFile.match(/var audioMap = \{([\s\S]*?)\};/)[1];

// --- AULA 3 AUDIO ENTRIES ---
const aula3Audio = {
  "Experience": "/audio/nilo-mesquita-patucci/aula3_experience.mp3",
  "Achievement": "/audio/nilo-mesquita-patucci/aula3_achievement.mp3",
  "Career": "/audio/nilo-mesquita-patucci/aula3_career.mp3",
  "Milestone": "/audio/nilo-mesquita-patucci/aula3_milestone.mp3",
  "Promotion": "/audio/nilo-mesquita-patucci/aula3_promotion.mp3",
  "Transition": "/audio/nilo-mesquita-patucci/aula3_transition.mp3",
  "Specialize": "/audio/nilo-mesquita-patucci/aula3_specialize.mp3",
  "Degree": "/audio/nilo-mesquita-patucci/aula3_degree.mp3",
  "I have worked in law for over fifteen years.": "/audio/nilo-mesquita-patucci/aula3_i_have_worked_in_law_for_over_fifteen_years.mp3",
  "She has achieved remarkable results in governance.": "/audio/nilo-mesquita-patucci/aula3_she_has_achieved_remarkable_results.mp3",
  "My career began in labor law in Rio Grande do Sul.": "/audio/nilo-mesquita-patucci/aula3_my_career_began_in_labor_law.mp3",
  "Reaching the CCO position was a major milestone.": "/audio/nilo-mesquita-patucci/aula3_reaching_the_cco_position.mp3",
  "I received a promotion to lead the compliance team.": "/audio/nilo-mesquita-patucci/aula3_i_received_a_promotion.mp3",
  "The transition from private practice to corporate was challenging.": "/audio/nilo-mesquita-patucci/aula3_the_transition_from_private_practice.mp3",
  "I decided to specialize in sports law early in my career.": "/audio/nilo-mesquita-patucci/aula3_i_decided_to_specialize.mp3",
  "I earned my law degree from a university in southern Brazil.": "/audio/nilo-mesquita-patucci/aula3_i_earned_my_law_degree.mp3",
  "I have worked in law for over fifteen years. My career began in labor law.": "/audio/nilo-mesquita-patucci/aula3_fill1.mp3",
  "I have achieved several milestones in my career.": "/audio/nilo-mesquita-patucci/aula3_fill2.mp3",
  "The transition to sports law was the best decision of my career.": "/audio/nilo-mesquita-patucci/aula3_fill3.mp3",
  "I specialize in compliance and governance.": "/audio/nilo-mesquita-patucci/aula3_fill4.mp3",
  "I earned my degree and then started working immediately.": "/audio/nilo-mesquita-patucci/aula3_fill5.mp3",
  "[order-l3]": "/audio/nilo-mesquita-patucci/aula3_order_l3.mp3",
  "I have built my career in sports law over the past fifteen years.": "/audio/nilo-mesquita-patucci/aula3_speech1.mp3",
  "The biggest milestone in my career was being selected for the FIFA program.": "/audio/nilo-mesquita-patucci/aula3_speech2.mp3",
  "I specialized in labor law before making the transition to sports law.": "/audio/nilo-mesquita-patucci/aula3_speech3.mp3",
  // Dialogue
  "Tell me about your career path, Nilo. How did you end up in football compliance?": "/audio/nilo-mesquita-patucci/aula3_dia1.mp3",
  "I earned my law degree in southern Brazil. I started in labor law, working with small firms.": "/audio/nilo-mesquita-patucci/aula3_dia2.mp3",
  "When did you make the transition to sports law?": "/audio/nilo-mesquita-patucci/aula3_dia3.mp3",
  "About ten years ago. I decided to specialize in sports law because I saw a growing need for compliance in football.": "/audio/nilo-mesquita-patucci/aula3_dia4.mp3",
  "That is impressive foresight. What has been your biggest achievement so far?": "/audio/nilo-mesquita-patucci/aula3_dia5.mp3",
  "Being selected for the FIFA program is definitely a milestone. But I am also proud of building the compliance department at Corinthians from the ground up.": "/audio/nilo-mesquita-patucci/aula3_dia6.mp3",
  "Have you ever thought about working for FIFA directly?": "/audio/nilo-mesquita-patucci/aula3_dia7.mp3",
  "I have considered it. But for now, my experience at the club level gives me a unique perspective that I want to share with other organizations.": "/audio/nilo-mesquita-patucci/aula3_dia8.mp3",
  // Listenings
  "[listening3a]": "/audio/nilo-mesquita-patucci/aula3_listening1.mp3",
  "[listening3b]": "/audio/nilo-mesquita-patucci/aula3_listening2.mp3",
};

const fullAudioMap = 'var audioMap = {' + audioMapContent + ',\n' + Object.entries(aula3Audio).map(([k,v]) => `  "${k.replace(/"/g,'\\"')}": "${v}"`).join(',\n') + '\n};';

// --- SLIDE HELPER (same pattern as Aula 1/2) ---
const SVG_VOL = '<svg viewBox="0 0 24 24" style="width:12px;height:12px" fill="none" stroke="#fff" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg>';
const SVG_CHECK = '<svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>';

const IMG3 = 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=1400&q=80';

function vocabCard(word, hint, def, example, gradStart, gradEnd, svgIcon) {
  return `<div class="vocab-card" onclick="revealVocab(this)">
<div class="card-icon" style="background:linear-gradient(135deg,${gradStart},${gradEnd})">${svgIcon}<div class="card-hint">${hint}</div></div>
<div class="card-body"><div class="card-word">${word}</div><div class="card-def">${def}</div><div class="card-example">&ldquo;${example}&rdquo;</div><div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('${word}',this)">${SVG_VOL} Listen</button></div></div>
</div>`;
}

const iconExp = '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" style="width:48px;height:48px"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>';
const iconAch = '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" style="width:48px;height:48px"><path d="M12 15l-3 3 1 4 2-1 2 1 1-4-3-3z"/><circle cx="12" cy="8" r="7"/></svg>';
const iconCar = '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" style="width:48px;height:48px"><path d="M2 3h6a4 4 0 014 4v14a3 3 0 00-3-3H2z"/><path d="M22 3h-6a4 4 0 00-4 4v14a3 3 0 013-3h7z"/></svg>';
const iconMil = '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" style="width:48px;height:48px"><path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/><line x1="4" y1="22" x2="4" y2="15"/></svg>';
const iconPro = '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" style="width:48px;height:48px"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/></svg>';
const iconTra = '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" style="width:48px;height:48px"><polyline points="16 3 21 3 21 8"/><line x1="4" y1="20" x2="21" y2="3"/><polyline points="21 16 21 21 16 21"/><line x1="15" y1="15" x2="21" y2="21"/></svg>';
const iconSpe = '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" style="width:48px;height:48px"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>';
const iconDeg = '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" style="width:48px;height:48px"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c0 1.66 2.69 3 6 3s6-1.34 6-3v-5"/></svg>';

// Build slides content (37 slides, same structure as Aula 1/2)
const slidesHTML = `
<!-- Ch1: The Journey So Far (1-4) -->
<div class="slide slide-image active" data-slide="1" data-phase="1" data-teacher="Abertura (2 min): Cumprimente o Nilo. Deixe o slide visível enquanto faz rapport." style="background-image:url('${IMG3}')">
<div class="slide-inner"><div class="chapter-label">Lesson 3 &mdash; Business English</div><h1 class="slide-title">Career<br><span class="accent">Timeline</span></h1><p class="slide-subtitle">B1 &mdash; 90 minutes &mdash; Alumni by Better</p></div></div>

<div class="slide slide-image" data-slide="2" data-phase="1" data-teacher="Transição. Diga: &quot;Today we will talk about your professional journey, from your first job to where you are now.&quot;" style="background-image:url('${IMG3}')">
<div class="slide-inner"><div class="chapter-label">Chapter 1</div><h2 class="slide-title">The Journey <span class="accent">So Far</span></h2><p class="slide-subtitle">Warm-up, callback from Lessons 1 and 2, and your career story.</p></div></div>

<div class="slide slide-dark" data-slide="3" data-phase="1" data-teacher="Callback (5 min): Peça ao Nilo que descreva seu departamento usando vocabulário das Aulas 1 e 2. Deve usar: manage, report to, department, responsibilities, oversee, coordinate. Se travar, dê pista.">
<div class="slide-inner"><div class="chapter-label">Chapter 1: The Journey So Far</div><h2 class="slide-heading">Callback: <span class="accent">Lessons 1 &amp; 2</span></h2>
<div class="warm-questions"><div class="warm-q">&ldquo;In 30 seconds, introduce yourself and describe your department. Use words from our previous lessons.&rdquo;</div></div>
<div style="display:flex;flex-wrap:wrap;gap:.5rem;margin-top:2rem;justify-content:center">
<span style="padding:.4rem .8rem;border:1px solid rgba(255,255,255,.15);border-radius:16px;font-size:.82rem;color:rgba(255,255,255,.5)">introduce</span><span style="padding:.4rem .8rem;border:1px solid rgba(255,255,255,.15);border-radius:16px;font-size:.82rem;color:rgba(255,255,255,.5)">manage</span><span style="padding:.4rem .8rem;border:1px solid rgba(255,255,255,.15);border-radius:16px;font-size:.82rem;color:rgba(255,255,255,.5)">report to</span><span style="padding:.4rem .8rem;border:1px solid rgba(255,255,255,.15);border-radius:16px;font-size:.82rem;color:rgba(255,255,255,.5)">department</span><span style="padding:.4rem .8rem;border:1px solid rgba(255,255,255,.15);border-radius:16px;font-size:.82rem;color:rgba(255,255,255,.5)">responsible</span><span style="padding:.4rem .8rem;border:1px solid rgba(255,255,255,.15);border-radius:16px;font-size:.82rem;color:rgba(255,255,255,.5)">coordinate</span>
</div></div></div>

<div class="slide slide-dark" data-slide="4" data-phase="1" data-teacher="Warm-up (5 min): Pergunte sobre a trajetória. Observe se usa Present Perfect corretamente para experiência. Anote erros.">
<div class="slide-inner"><div class="chapter-label">Chapter 1: The Journey So Far</div><h2 class="slide-heading">Your <span class="accent">Story</span></h2>
<div class="warm-questions"><div class="warm-q">&ldquo;Tell me: how did you get into law? What was your first job?&rdquo;</div><div class="warm-q">&ldquo;What made you decide to work in football?&rdquo;</div></div></div></div>

<!-- Ch2: Packing Words (5-7) -->
<div class="slide slide-image" data-slide="5" data-phase="2" data-teacher="Transição." style="background-image:url('https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?w=1400&q=80')">
<div class="slide-inner"><div class="chapter-label">Chapter 2</div><h2 class="slide-title">Packing <span class="accent">Words</span></h2><p class="slide-subtitle">8 words for telling your professional story: education, career moves, and achievements.</p></div></div>

<div class="slide slide-light" data-slide="6" data-phase="2" data-teacher="Vocabulário 1 (7 min): EXPERIENCE: CCQ &quot;Is experience something you learn from books or from doing things?&quot; (doing). ACHIEVEMENT: &quot;Is an achievement easy or hard to reach?&quot; (hard). CAREER: drilling &quot;ca-REER&quot; (stress on 2nd syllable).">
<div class="slide-inner"><div class="chapter-label">Chapter 2: Packing Words</div><h2 class="slide-heading">Key <span class="accent">Vocabulary</span> (1/2)</h2>
<div class="vocab-grid" id="vocabGrid1">
${vocabCard('Experience','Knowledge gained from doing something over time','knowledge or skill gained from doing something over time','I have worked in law for over fifteen years.','#7B2D3B','#9A4054',iconExp)}
${vocabCard('Achievement','Something difficult that you accomplished','something important that you succeeded in doing through effort','She has achieved remarkable results in governance.','#2C5282','#3B7DD8',iconAch)}
${vocabCard('Career','The series of jobs you have during your working life','the series of jobs that a person has in a particular area of work','My career began in labor law in Rio Grande do Sul.','#553C7B','#7B5EA7',iconCar)}
${vocabCard('Milestone','An important event or stage in development','an important event or achievement in the development of something','Reaching the CCO position was a major milestone.','#1B4D3E','#2D7A5F',iconMil)}
</div><div class="vocab-counter" id="vocabCount1">0 / 4 words revealed</div></div></div>

<div class="slide slide-light" data-slide="7" data-phase="2" data-teacher="Vocabulário 2 (7 min): PROMOTION: CCQ &quot;If you get a promotion, do you go up or down?&quot; (up). TRANSITION: &quot;Is a transition a sudden change or a gradual move?&quot; (gradual). SPECIALIZE: drilling &quot;SPEH-shuh-lize&quot;. DEGREE: &quot;Where do you get a degree?&quot; (university).">
<div class="slide-inner"><div class="chapter-label">Chapter 2: Packing Words</div><h2 class="slide-heading">Key <span class="accent">Vocabulary</span> (2/2)</h2>
<div class="vocab-grid" id="vocabGrid2">
${vocabCard('Promotion','Moving to a higher position at work','when someone is given a more important job in the same organization','I received a promotion to lead the compliance team.','#6B4C3B','#8D6E5D',iconPro)}
${vocabCard('Transition','A change from one situation to another','the process of changing from one state or condition to another','The transition from private practice to corporate was challenging.','#4A5568','#718096',iconTra)}
${vocabCard('Specialize','To focus on one particular area of work','to concentrate on and become expert in a particular area','I decided to specialize in sports law early in my career.','#5C3D2E','#7D5A48',iconSpe)}
${vocabCard('Degree','A qualification from a university','an academic title given by a university after completing a course of study','I earned my law degree from a university in southern Brazil.','#4A3728','#6B5240',iconDeg)}
</div><div class="vocab-counter" id="vocabCount2">0 / 4 words revealed</div></div></div>

<!-- Ch3: The Code (8-12) -->
<div class="slide slide-image" data-slide="8" data-phase="3" data-teacher="Transição. Diga: &quot;You already used Present Perfect in Lesson 1. Now let us go deeper: for, since, ever, never.&quot;" style="background-image:url('https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=1400&q=80')">
<div class="slide-inner"><div class="chapter-label">Chapter 3</div><h2 class="slide-title">The <span class="accent">Code</span></h2><p class="slide-subtitle">Present Perfect deep dive: for, since, ever, never. The grammar of your career story.</p></div></div>

<div class="slide slide-light" data-slide="9" data-phase="3" data-teacher="Grammar Discovery (5 min): NÃO diga a regra. Pergunte: &quot;What words do you see after have/has?&quot; Guie: FOR + duração, SINCE + ponto, EVER em perguntas, NEVER em negativas.">
<div class="slide-inner"><div class="chapter-label">Chapter 3: The Code</div><h2 class="slide-heading">What Do You <span class="accent">Notice</span>?</h2>
<div class="grammar-sentences">
<div class="grammar-sentence">I have worked in law <strong>for</strong> fifteen years.</div>
<div class="grammar-sentence">She has been at FIFA <strong>since</strong> 2018.</div>
<div class="grammar-sentence">Have you <strong>ever</strong> worked outside Brazil?</div>
<div class="grammar-sentence">I have <strong>never</strong> missed a compliance deadline.</div>
</div>
<p style="text-align:center;margin-top:1.5rem;font-style:italic;color:var(--text-dim)">What is the difference between for, since, ever, and never?</p>
<div style="text-align:center;margin-top:1rem"><button class="btn-primary" onclick="revealGrammar()">Reveal the Rule</button></div>
<div class="grammar-table-wrap" id="grammarTable"><table class="grammar-table"><thead><tr><th>Word</th><th>Use</th><th>Example</th></tr></thead><tbody>
<tr><td><strong>for</strong></td><td>Duration (how long)</td><td>for fifteen years, for six months</td></tr>
<tr><td><strong>since</strong></td><td>Point in time (when it started)</td><td>since 2010, since I graduated</td></tr>
<tr><td><strong>ever</strong></td><td>Questions (at any time in your life)</td><td>Have you ever worked abroad?</td></tr>
<tr><td><strong>never</strong></td><td>Negative (at no time)</td><td>I have never missed a deadline.</td></tr>
</tbody></table></div></div></div>

<div class="slide slide-light" data-slide="10" data-phase="3" data-teacher="Erro Comum (3 min): &quot;I have worked since fifteen years&quot; é o erro mais provável. Drilling: FOR + duração, SINCE + ponto.">
<div class="slide-inner"><div class="chapter-label">Chapter 3: The Code</div><h2 class="slide-heading">Common <span class="accent">Mistake</span></h2>
<div class="mistake-card"><div class="mistake-item mistake-wrong"><div class="mistake-icon"><svg viewBox="0 0 24 24" fill="none" stroke="#dc2626" stroke-width="2.5"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></div>&ldquo;I have worked since fifteen years.&rdquo;</div>
<div class="mistake-item mistake-right"><div class="mistake-icon"><svg viewBox="0 0 24 24" fill="none" stroke="#16a34a" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg></div>&ldquo;I have worked <strong>for</strong> fifteen years.&rdquo;</div></div>
<div class="mistake-card" style="margin-top:1.5rem"><div class="mistake-item mistake-wrong"><div class="mistake-icon"><svg viewBox="0 0 24 24" fill="none" stroke="#dc2626" stroke-width="2.5"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></div>&ldquo;Did you ever work in sports law?&rdquo;</div>
<div class="mistake-item mistake-right"><div class="mistake-icon"><svg viewBox="0 0 24 24" fill="none" stroke="#16a34a" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg></div>&ldquo;<strong>Have</strong> you ever worked in sports law?&rdquo;</div></div></div></div>

<div class="slide slide-light" data-slide="11" data-phase="3" data-teacher="Grammar Practice (5 min): Nilo completa ORALMENTE.">
<div class="slide-inner"><div class="chapter-label">Chapter 3: The Code</div><h2 class="slide-heading">Grammar <span class="accent">Practice</span></h2>
<div class="fill-grid">
<div class="fill-item" onclick="revealFill(this)"><div class="fill-text">I have worked in compliance <span class="fill-blank">___</span><span class="fill-answer">for</span> five years.</div></div>
<div class="fill-item" onclick="revealFill(this)"><div class="fill-text">She has been at Corinthians <span class="fill-blank">___</span><span class="fill-answer">since</span> 2020.</div></div>
<div class="fill-item" onclick="revealFill(this)"><div class="fill-text">Have you <span class="fill-blank">___</span><span class="fill-answer">ever</span> attended a FIFA event?</div></div>
<div class="fill-item" onclick="revealFill(this)"><div class="fill-text">I have <span class="fill-blank">___</span><span class="fill-answer">never</span> worked outside Brazil.</div></div>
</div></div></div>

<div class="slide slide-light" data-slide="12" data-phase="3" data-teacher="CCQs (2 min): &quot;FOR fifteen years or SINCE fifteen years?&quot; (FOR). &quot;SINCE 2010 or FOR 2010?&quot; (SINCE). &quot;Have you EVER or Did you EVER?&quot; (Have you ever).">
<div class="slide-inner"><div class="chapter-label">Chapter 3: The Code</div><h2 class="slide-heading">Quick <span class="accent">Check</span></h2>
<div class="comp-questions">
<div class="comp-q" onclick="revealComp(this)"><div class="q-text">1. Which is correct: &ldquo;for 2010&rdquo; or &ldquo;since 2010&rdquo;?</div><div class="q-answer">Since 2010. SINCE + point in time.</div></div>
<div class="comp-q" onclick="revealComp(this)"><div class="q-text">2. &ldquo;I have never missed a deadline.&rdquo; Does this mean zero times?</div><div class="q-answer">Yes, never = at no time in my career.</div></div>
<div class="comp-q" onclick="revealComp(this)"><div class="q-text">3. &ldquo;Have you ever presented at a conference?&rdquo; What does ever mean here?</div><div class="q-answer">At any time in your life. It asks about experience.</div></div>
</div></div></div>

<!-- Ch4: Getting There (13-19) -->
<div class="slide slide-image" data-slide="13" data-phase="4" data-teacher="Transição." style="background-image:url('https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=1400&q=80')">
<div class="slide-inner"><div class="chapter-label">Chapter 4</div><h2 class="slide-title">Getting <span class="accent">There</span></h2><p class="slide-subtitle">Your career story in context: a LinkedIn profile, listening exercises, and a networking dialogue.</p></div></div>

<div class="slide slide-light" data-slide="14" data-phase="4" data-teacher="Artefato LinkedIn (5 min): Leia o perfil juntos. Peça ao Nilo que identifique as 8 palavras no texto.">
<div class="slide-inner"><div class="chapter-label">Chapter 4: Getting There</div><h2 class="slide-heading">LinkedIn <span class="accent">Profile</span></h2>
<div class="email-card" style="max-width:560px;margin:1rem auto">
<div class="email-header" style="background:linear-gradient(135deg,#0077b5,#004182);padding:1rem 1.5rem"><strong style="color:#fff;font-size:.78rem;letter-spacing:2px">LINKEDIN</strong></div>
<div class="email-body-ic">
<p style="font-weight:700;font-size:1.1rem">Nilo Mesquita Patussi</p>
<p style="color:var(--text-dim);font-size:.85rem;margin-bottom:.8rem">Chief Compliance Officer at Sport Club Corinthians Paulista</p>
<p>I have built my <strong>career</strong> in sports law and governance over the past fifteen years. After earning my law <strong>degree</strong> in southern Brazil, I began <strong>specializing</strong> in labor law.</p>
<p style="margin-top:.6rem">The <strong>transition</strong> to sports law was a pivotal moment. I received a <strong>promotion</strong> to lead the compliance team at Corinthians, which has been my greatest professional <strong>achievement</strong>.</p>
<p style="margin-top:.6rem">Key <strong>milestones</strong>: built a compliance department from scratch, selected as the only Brazilian delegate for the FIFA Leadership in Football program. I have gained valuable <strong>experience</strong> working with international organizations.</p>
</div></div></div></div>

<div class="slide slide-light" data-slide="15" data-phase="4" data-teacher="Comprehensão (3 min): Perguntas orais sobre o perfil.">
<div class="slide-inner"><div class="chapter-label">Chapter 4: Getting There</div><h2 class="slide-heading">Profile <span class="accent">Comprehension</span></h2>
<div class="comp-questions">
<div class="comp-q" onclick="revealComp(this)"><div class="q-text">1. What did Nilo specialize in first?</div><div class="q-answer">Labor law.</div></div>
<div class="comp-q" onclick="revealComp(this)"><div class="q-text">2. What was his greatest achievement?</div><div class="q-answer">Leading the compliance team at Corinthians (promotion to CCO).</div></div>
<div class="comp-q" onclick="revealComp(this)"><div class="q-text">3. What are his key milestones?</div><div class="q-answer">Built a compliance department from scratch and selected for the FIFA program.</div></div>
</div></div></div>

<div class="slide slide-dark" data-slide="16" data-phase="4" data-teacher="Listening 1 (5 min): Voz Ash. Nilo ouve sem texto. Depois perguntas.">
<div class="slide-inner" style="text-align:center"><div class="chapter-label">Chapter 4: Getting There</div><h2 class="slide-heading">Listen to a <span class="accent">Career Story</span></h2>
<p style="color:rgba(255,255,255,.7);margin-bottom:1.5rem">Listen carefully. Questions will appear after the audio ends.</p>
<div class="listening-player" id="lp-listen1" data-src="/audio/nilo-mesquita-patucci/aula3_listening1.mp3"><div class="lp-seekbar" onclick="seekAudio(event,'lp-listen1')"><div class="lp-progress" id="progress-lp-listen1"></div></div><div class="lp-time"><span id="time-current-lp-listen1">0:00</span><span id="time-total-lp-listen1">0:00</span></div><div class="lp-controls"><button class="lp-btn" onclick="skipAudio('lp-listen1',-5)"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="11 17 6 12 11 7"/><line x1="6" y1="12" x2="18" y2="12"/></svg></button><button class="lp-btn lp-play" onclick="togglePlayer('lp-listen1')"><svg viewBox="0 0 24 24"><polygon points="6 3 20 12 6 21 6 3" fill="currentColor"/></svg></button><button class="lp-btn" onclick="skipAudio('lp-listen1',5)"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="13 7 18 12 13 17"/><line x1="6" y1="12" x2="18" y2="12"/></svg></button></div><div class="lp-label">Speed</div><div class="lp-speed"><button class="lp-speed-btn" onclick="setPlayerSpeed('lp-listen1',0.5,this)">0.5x</button><button class="lp-speed-btn" onclick="setPlayerSpeed('lp-listen1',0.75,this)">0.75x</button><button class="lp-speed-btn active" onclick="setPlayerSpeed('lp-listen1',1,this)">1x</button><button class="lp-speed-btn" onclick="setPlayerSpeed('lp-listen1',1.25,this)">1.25x</button></div></div>
<div class="comp-questions" id="questions-lp-listen1" style="display:none">
<div class="comp-q" onclick="revealComp(this)" style="background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.15)"><div class="q-text" style="color:rgba(255,255,255,.9)">1. Where did the speaker start their career?</div><div class="q-answer" style="color:#F0B8C4">In a small law firm in southern Brazil.</div></div>
<div class="comp-q" onclick="revealComp(this)" style="background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.15)"><div class="q-text" style="color:rgba(255,255,255,.9)">2. How long has the speaker been in sports law?</div><div class="q-answer" style="color:#F0B8C4">About ten years.</div></div>
<div class="comp-q" onclick="revealComp(this)" style="background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.15)"><div class="q-text" style="color:rgba(255,255,255,.9)">3. What was the biggest milestone?</div><div class="q-answer" style="color:#F0B8C4">Being selected for the FIFA Leadership program.</div></div>
</div></div></div>

<div class="slide slide-dark" data-slide="17" data-phase="4" data-teacher="Diálogo (10 min): David Chen (Ash) e Nilo (Ash). Problema: ambos masculinos. Use 2a pessoa &quot;you&quot; para Nilo. Fase 1: ouçam. Fase 2: Nilo lê suas falas. Fase 3: invertem.">
<div class="slide-inner"><div class="chapter-label">Chapter 4: Getting There</div><h2 class="slide-heading" style="text-align:center">Career <span class="accent">Dialogue</span></h2>
<div class="dialogue-box" id="dialogueBox">
<div class="dialogue-line visible" data-line="1" data-voice="riley"><div class="dialogue-avatar" style="background:#3B7DD8">D</div><div class="dialogue-bubble dr-bubble">Tell me about your career path, Nilo. How did you end up in football compliance?<span class="audio-inline" onclick="speakText('Tell me about your career path, Nilo. How did you end up in football compliance?',this)"><svg viewBox="0 0 24 24" style="width:14px;height:14px" fill="none" stroke="var(--accent)" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg></span></div></div>
<div class="dialogue-line" data-line="2" data-voice="ash"><div class="dialogue-avatar" style="background:var(--accent)">N</div><div class="dialogue-bubble patricia-bubble">I earned my law <span class="vocab-highlight">degree</span> in southern Brazil. I started in labor law, working with small firms.<span class="audio-inline" onclick="speakText('I earned my law degree in southern Brazil. I started in labor law, working with small firms.',this)"><svg viewBox="0 0 24 24" style="width:14px;height:14px" fill="none" stroke="var(--accent)" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg></span></div></div>
<div class="dialogue-line" data-line="3" data-voice="riley"><div class="dialogue-avatar" style="background:#3B7DD8">D</div><div class="dialogue-bubble dr-bubble">When did you make the <span class="vocab-highlight">transition</span> to sports law?<span class="audio-inline" onclick="speakText('When did you make the transition to sports law?',this)"><svg viewBox="0 0 24 24" style="width:14px;height:14px" fill="none" stroke="var(--accent)" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg></span></div></div>
<div class="dialogue-line" data-line="4" data-voice="ash"><div class="dialogue-avatar" style="background:var(--accent)">N</div><div class="dialogue-bubble patricia-bubble">About ten years ago. I decided to <span class="vocab-highlight">specialize</span> in sports law because I saw a growing need for compliance in football.<span class="audio-inline" onclick="speakText('About ten years ago. I decided to specialize in sports law because I saw a growing need for compliance in football.',this)"><svg viewBox="0 0 24 24" style="width:14px;height:14px" fill="none" stroke="var(--accent)" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg></span></div></div>
<div class="dialogue-line" data-line="5" data-voice="riley"><div class="dialogue-avatar" style="background:#3B7DD8">D</div><div class="dialogue-bubble dr-bubble">That is impressive foresight. What has been your biggest <span class="vocab-highlight">achievement</span> so far?<span class="audio-inline" onclick="speakText('That is impressive foresight. What has been your biggest achievement so far?',this)"><svg viewBox="0 0 24 24" style="width:14px;height:14px" fill="none" stroke="var(--accent)" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg></span></div></div>
<div class="dialogue-line" data-line="6" data-voice="ash"><div class="dialogue-avatar" style="background:var(--accent)">N</div><div class="dialogue-bubble patricia-bubble">Being selected for the FIFA program is definitely a <span class="vocab-highlight">milestone</span>. But I am also proud of building the compliance department at Corinthians from the ground up.<span class="audio-inline" onclick="speakText('Being selected for the FIFA program is definitely a milestone. But I am also proud of building the compliance department at Corinthians from the ground up.',this)"><svg viewBox="0 0 24 24" style="width:14px;height:14px" fill="none" stroke="var(--accent)" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg></span></div></div>
<div class="dialogue-line" data-line="7" data-voice="riley"><div class="dialogue-avatar" style="background:#3B7DD8">D</div><div class="dialogue-bubble dr-bubble">Have you ever thought about working for FIFA directly?<span class="audio-inline" onclick="speakText('Have you ever thought about working for FIFA directly?',this)"><svg viewBox="0 0 24 24" style="width:14px;height:14px" fill="none" stroke="var(--accent)" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg></span></div></div>
<div class="dialogue-line" data-line="8" data-voice="ash"><div class="dialogue-avatar" style="background:var(--accent)">N</div><div class="dialogue-bubble patricia-bubble">I have considered it. But for now, my <span class="vocab-highlight">experience</span> at the club level gives me a unique perspective that I want to share with other organizations.<span class="audio-inline" onclick="speakText('I have considered it. But for now, my experience at the club level gives me a unique perspective that I want to share with other organizations.',this)"><svg viewBox="0 0 24 24" style="width:14px;height:14px" fill="none" stroke="var(--accent)" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg></span></div></div>
</div><button class="btn-primary" id="nextLineBtn" onclick="nextDialogueLine()">Next Line</button></div></div>

<div class="slide slide-light" data-slide="18" data-phase="4" data-teacher="Comprehensão (3 min): Perguntas sobre DAVID (interlocutor).">
<div class="slide-inner"><div class="chapter-label">Chapter 4: Getting There</div><h2 class="slide-heading">Dialogue <span class="accent">Comprehension</span></h2>
<div class="comp-questions">
<div class="comp-q" onclick="revealComp(this)"><div class="q-text">1. What did David ask about first?</div><div class="q-answer">How Nilo ended up in football compliance.</div></div>
<div class="comp-q" onclick="revealComp(this)"><div class="q-text">2. What word did David use for &ldquo;an important event&rdquo;?</div><div class="q-answer">Achievement.</div></div>
<div class="comp-q" onclick="revealComp(this)"><div class="q-text">3. What did David ask about FIFA?</div><div class="q-answer">If Nilo has ever thought about working for FIFA directly.</div></div>
</div></div></div>

<div class="slide slide-dark" data-slide="19" data-phase="4" data-teacher="Listening 2 (5 min): Voz Riley. Outra delegada conta sua trajetória.">
<div class="slide-inner" style="text-align:center"><div class="chapter-label">Chapter 4: Getting There</div><h2 class="slide-heading">Another <span class="accent">Career Story</span></h2>
<p style="color:rgba(255,255,255,.7);margin-bottom:1.5rem">Listen to another delegate describe their career path.</p>
<div class="listening-player" id="lp-listen2" data-src="/audio/nilo-mesquita-patucci/aula3_listening2.mp3"><div class="lp-seekbar" onclick="seekAudio(event,'lp-listen2')"><div class="lp-progress" id="progress-lp-listen2"></div></div><div class="lp-time"><span id="time-current-lp-listen2">0:00</span><span id="time-total-lp-listen2">0:00</span></div><div class="lp-controls"><button class="lp-btn" onclick="skipAudio('lp-listen2',-5)"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="11 17 6 12 11 7"/><line x1="6" y1="12" x2="18" y2="12"/></svg></button><button class="lp-btn lp-play" onclick="togglePlayer('lp-listen2')"><svg viewBox="0 0 24 24"><polygon points="6 3 20 12 6 21 6 3" fill="currentColor"/></svg></button><button class="lp-btn" onclick="skipAudio('lp-listen2',5)"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="13 7 18 12 13 17"/><line x1="6" y1="12" x2="18" y2="12"/></svg></button></div><div class="lp-label">Speed</div><div class="lp-speed"><button class="lp-speed-btn" onclick="setPlayerSpeed('lp-listen2',0.5,this)">0.5x</button><button class="lp-speed-btn" onclick="setPlayerSpeed('lp-listen2',0.75,this)">0.75x</button><button class="lp-speed-btn active" onclick="setPlayerSpeed('lp-listen2',1,this)">1x</button><button class="lp-speed-btn" onclick="setPlayerSpeed('lp-listen2',1.25,this)">1.25x</button></div></div>
<div class="comp-questions" id="questions-lp-listen2" style="display:none">
<div class="comp-q" onclick="revealComp(this)" style="background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.15)"><div class="q-text" style="color:rgba(255,255,255,.9)">1. What was the speaker&rsquo;s first career?</div><div class="q-answer" style="color:#F0B8C4">Journalism.</div></div>
<div class="comp-q" onclick="revealComp(this)" style="background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.15)"><div class="q-text" style="color:rgba(255,255,255,.9)">2. What was her biggest career transition?</div><div class="q-answer" style="color:#F0B8C4">From journalism to football governance.</div></div>
<div class="comp-q" onclick="revealComp(this)" style="background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.15)"><div class="q-text" style="color:rgba(255,255,255,.9)">3. How long has she been in governance?</div><div class="q-answer" style="color:#F0B8C4">For eight years.</div></div>
</div></div></div>

<!-- Ch5: Practice (20-26) -->
<div class="slide slide-image" data-slide="20" data-phase="5" data-teacher="Transição." style="background-image:url('https://images.unsplash.com/photo-1517649763962-0c623066013b?w=1400&q=80')">
<div class="slide-inner"><div class="chapter-label">Chapter 5</div><h2 class="slide-title"><span class="accent">Practice</span></h2><p class="slide-subtitle">Quick challenges, error spotting, and oral drilling about career stories.</p></div></div>

<div class="slide slide-light" data-slide="21" data-phase="5" data-teacher="Quick Fire (8 min): Uma por vez.">
<div class="slide-inner"><div class="chapter-label">Chapter 5: Practice</div><h2 class="slide-heading">Quick <span class="accent">Fire</span></h2>
<div style="position:relative"><div class="challenge-score" id="challengeScore">0 / 6</div>
<div class="challenge-card" id="challengeCard"><div class="challenge-counter" id="challengeCounter">Question 1 of 6</div><div class="challenge-prompt" id="challengePrompt">Someone asks: &ldquo;How long have you been in law?&rdquo; Answer with Present Perfect.</div><div class="challenge-answer" id="challengeAnswer">&ldquo;I have been in law for over fifteen years.&rdquo;</div><button class="btn-primary" id="showAnswerBtn" onclick="showChallengeAnswer()">Show Answer</button><button class="btn-secondary" id="nextChallengeBtn" onclick="nextChallenge()" style="display:none">Next Question</button></div></div></div></div>

<div class="slide slide-light" data-slide="22" data-phase="5" data-teacher="Spot the Error (5 min).">
<div class="slide-inner"><div class="chapter-label">Chapter 5: Practice</div><h2 class="slide-heading">Spot the <span class="accent">Error</span></h2>
<div class="error-grid">
<div class="error-card" onclick="revealError(this)"><div class="error-sentence">&ldquo;I have worked since fifteen years.&rdquo;</div><div class="error-fix">&ldquo;I have worked <strong>for</strong> fifteen years.&rdquo;</div></div>
<div class="error-card" onclick="revealError(this)"><div class="error-sentence">&ldquo;Did you ever work abroad?&rdquo;</div><div class="error-fix">&ldquo;<strong>Have</strong> you ever worked abroad?&rdquo;</div></div>
<div class="error-card" onclick="revealError(this)"><div class="error-sentence">&ldquo;I never have missed a deadline.&rdquo;</div><div class="error-fix">&ldquo;I have <strong>never</strong> missed a deadline.&rdquo;</div></div>
<div class="error-card" onclick="revealError(this)"><div class="error-sentence">&ldquo;She has been at FIFA for 2018.&rdquo;</div><div class="error-fix">&ldquo;She has been at FIFA <strong>since</strong> 2018.&rdquo;</div></div>
</div><div class="error-score" id="errorScore">0 / 4 errors found</div></div></div>

<div class="slide slide-light" data-slide="23" data-phase="5" data-teacher="Oral Drilling (5 min).">
<div class="slide-inner"><div class="chapter-label">Chapter 5: Practice</div><h2 class="slide-heading">Oral <span class="accent">Drilling</span> (1/2)</h2>
<div class="oral-grid">
<div class="oral-item" onclick="this.classList.toggle('revealed')"><div class="oral-situation">1. Tell me about your education.</div><div class="oral-model">&ldquo;I earned my law degree from a university in southern Brazil.&rdquo;</div></div>
<div class="oral-item" onclick="this.classList.toggle('revealed')"><div class="oral-situation">2. How long have you been in sports law?</div><div class="oral-model">&ldquo;I have been in sports law for about ten years.&rdquo;</div></div>
<div class="oral-item" onclick="this.classList.toggle('revealed')"><div class="oral-situation">3. What was your biggest career change?</div><div class="oral-model">&ldquo;The transition from private practice to corporate compliance was my biggest career change.&rdquo;</div></div>
</div></div></div>

<div class="slide slide-light" data-slide="24" data-phase="5" data-teacher="Oral Drilling 2 (5 min).">
<div class="slide-inner"><div class="chapter-label">Chapter 5: Practice</div><h2 class="slide-heading">Oral <span class="accent">Drilling</span> (2/2)</h2>
<div class="oral-grid">
<div class="oral-item" onclick="this.classList.toggle('revealed')"><div class="oral-situation">4. What is your proudest achievement?</div><div class="oral-model">&ldquo;Building the compliance department at Corinthians from scratch has been my proudest achievement.&rdquo;</div></div>
<div class="oral-item" onclick="this.classList.toggle('revealed')"><div class="oral-situation">5. Have you ever worked outside Brazil?</div><div class="oral-model">&ldquo;No, I have never worked outside Brazil, but the FIFA program will be my first international experience.&rdquo;</div></div>
<div class="oral-item" onclick="this.classList.toggle('revealed')"><div class="oral-situation">6. What made you specialize in compliance?</div><div class="oral-model">&ldquo;I decided to specialize in compliance because I saw a growing need for governance in Brazilian football.&rdquo;</div></div>
</div></div></div>

<div class="slide slide-light" data-slide="25" data-phase="5" data-teacher="Sentence Building (5 min).">
<div class="slide-inner"><div class="chapter-label">Chapter 5: Practice</div><h2 class="slide-heading">Sentence <span class="accent">Building</span></h2>
<div class="oral-grid">
<div class="oral-item" onclick="this.classList.toggle('revealed')"><div class="oral-situation">have / I / in / law / worked / fifteen / for / years</div><div class="oral-model">&ldquo;I have worked in law for fifteen years.&rdquo;</div></div>
<div class="oral-item" onclick="this.classList.toggle('revealed')"><div class="oral-situation">ever / you / have / a / attended / FIFA / event / ?</div><div class="oral-model">&ldquo;Have you ever attended a FIFA event?&rdquo;</div></div>
<div class="oral-item" onclick="this.classList.toggle('revealed')"><div class="oral-situation">milestone / being / was / the / biggest / selected / my</div><div class="oral-model">&ldquo;Being selected was my biggest milestone.&rdquo;</div></div>
<div class="oral-item" onclick="this.classList.toggle('revealed')"><div class="oral-situation">she / FIFA / since / at / been / 2018 / has</div><div class="oral-model">&ldquo;She has been at FIFA since 2018.&rdquo;</div></div>
</div></div></div>

<div class="slide slide-light" data-slide="26" data-phase="5" data-teacher="Pronúncia (5 min): Drilling 3x cada.">
<div class="slide-inner"><div class="chapter-label">Chapter 5: Practice</div><h2 class="slide-heading">Pronunciation <span class="accent">Focus</span></h2>
<div class="oral-grid" style="text-align:center">
<div class="oral-item" style="cursor:default"><div class="oral-situation" style="font-size:1.2rem">ex&middot;<strong>PE</strong>&middot;ri&middot;ence<br><button class="audio-btn-sm" onclick="speakText('Experience',this)" style="margin-top:.5rem">${SVG_VOL} Listen</button></div></div>
<div class="oral-item" style="cursor:default"><div class="oral-situation" style="font-size:1.2rem">a&middot;<strong>CHIEVE</strong>&middot;ment<br><button class="audio-btn-sm" onclick="speakText('Achievement',this)" style="margin-top:.5rem">${SVG_VOL} Listen</button></div></div>
<div class="oral-item" style="cursor:default"><div class="oral-situation" style="font-size:1.2rem"><strong>MILE</strong>&middot;stone<br><button class="audio-btn-sm" onclick="speakText('Milestone',this)" style="margin-top:.5rem">${SVG_VOL} Listen</button></div></div>
<div class="oral-item" style="cursor:default"><div class="oral-situation" style="font-size:1.2rem"><strong>SPEH</strong>&middot;shuh&middot;lize<br><button class="audio-btn-sm" onclick="speakText('Specialize',this)" style="margin-top:.5rem">${SVG_VOL} Listen</button></div></div>
</div></div></div>

<!-- Ch6: Your Turn (27-32) -->
<div class="slide slide-image" data-slide="27" data-phase="6" data-teacher="Transição." style="background-image:url('https://images.unsplash.com/photo-1475721027785-f74eccf877e2?w=1400&q=80')">
<div class="slide-inner"><div class="chapter-label">Chapter 6</div><h2 class="slide-title">Your <span class="accent">Turn</span></h2><p class="slide-subtitle">Tell your career story. From guided to completely free.</p></div></div>

<div class="slide slide-dark" data-slide="28" data-phase="6" data-teacher="Role-play Guiado (5 min): NÃO corrija durante. Anote erros.">
<div class="slide-inner"><div class="chapter-label">Chapter 6: Your Turn</div><h2 class="slide-heading">Role-play: <span class="accent">Guided</span></h2>
<div class="roleplay-card"><div class="card-icon" style="background:linear-gradient(135deg,#7B2D3B,#9A4054);height:80px;display:flex;align-items:center;justify-content:center;border-radius:14px 14px 0 0"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" style="width:40px;height:40px"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg></div><div class="roleplay-body"><div class="roleplay-scenario">A delegate at the FIFA program asks about your career. Tell your story from university to today.</div><div class="roleplay-keywords"><span class="roleplay-kw">degree</span><span class="roleplay-kw">labor law</span><span class="roleplay-kw">specialize</span><span class="roleplay-kw">transition</span><span class="roleplay-kw">Corinthians</span><span class="roleplay-kw">fifteen years</span></div></div></div></div></div>

<div class="slide slide-dark" data-slide="29" data-phase="6" data-teacher="Semi-livre (5 min): Menos keywords.">
<div class="slide-inner"><div class="chapter-label">Chapter 6: Your Turn</div><h2 class="slide-heading">Role-play: <span class="accent">Semi-free</span></h2>
<div class="roleplay-card"><div class="card-icon" style="background:linear-gradient(135deg,#4A3728,#6B5240);height:80px;display:flex;align-items:center;justify-content:center;border-radius:14px 14px 0 0"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" style="width:40px;height:40px"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/></svg></div><div class="roleplay-body"><div class="roleplay-scenario">You are at dinner with delegates. Someone asks: &ldquo;What is the most important milestone in your career?&rdquo;</div><div class="roleplay-keywords"><span class="roleplay-kw">achievement</span><span class="roleplay-kw">milestone</span><span class="roleplay-kw">experience</span></div></div></div></div></div>

<div class="slide slide-dark" data-slide="30" data-phase="6" data-teacher="Livre (5 min): ZERO apoio. NÃO corrija. Anote.">
<div class="slide-inner"><div class="chapter-label">Chapter 6: Your Turn</div><h2 class="slide-heading">Role-play: <span class="accent">Free</span></h2>
<div class="roleplay-card"><div class="card-icon" style="background:linear-gradient(135deg,#2C5282,#3B7DD8);height:80px;display:flex;align-items:center;justify-content:center;border-radius:14px 14px 0 0"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" style="width:40px;height:40px"><circle cx="12" cy="12" r="10"/><path d="M2 12h20"/></svg></div><div class="roleplay-body"><div class="roleplay-scenario">The FIFA moderator asks each delegate to share their 3-minute career story. Tell yours from beginning to now. No script, no keywords.</div></div></div></div></div>

<div class="slide slide-light" data-slide="31" data-phase="6" data-teacher="Delayed Error Correction (5 min): Foque em for/since e Present Perfect vs Past Simple.">
<div class="slide-inner"><div class="chapter-label">Chapter 6: Your Turn</div><h2 class="slide-heading">Error <span class="accent">Correction</span></h2>
<p style="font-size:.9rem;color:var(--text-dim);margin-bottom:1rem">Teacher: type the errors you observed during the free role-play.</p>
<div style="background:#fff;border:2px solid var(--border);border-radius:10px;padding:1.5rem;min-height:200px" contenteditable="true"><p style="color:var(--text-dim);font-style:italic">Click here and type the errors observed...</p></div></div></div>

<div class="slide slide-dark" data-slide="32" data-phase="6" data-teacher="Produção (5 min): Nilo grava áudio de 3 min contando sua trajetória.">
<div class="slide-inner" style="text-align:center"><div class="chapter-label">Chapter 6: Your Turn</div><h2 class="slide-heading">Record Your <span class="accent">Career Story</span></h2>
<div class="record-card"><div class="record-prompt">Record a 3-minute career story. Start from your university years and end with the FIFA program. Use all 8 vocabulary words and the Present Perfect with for, since, ever, and never.</div><button class="record-btn" onclick="toggleReflectionRecord(this)"><svg viewBox="0 0 24 24" style="width:28px;height:28px"><path d="M12 1a3 3 0 00-3 3v8a3 3 0 006 0V4a3 3 0 00-3-3z" fill="#fff"/><path d="M19 10v2a7 7 0 01-14 0v-2" fill="none" stroke="#fff" stroke-width="2"/></svg></button><div id="reflectionResult"></div></div></div></div>

<!-- Ch7: Wrap-up (33-37) -->
<div class="slide slide-image" data-slide="33" data-phase="7" data-teacher="Transição." style="background-image:url('https://images.unsplash.com/photo-1504384308090-c894fdcc538d?w=1400&q=80')">
<div class="slide-inner"><div class="chapter-label">Chapter 7</div><h2 class="slide-title"><span class="accent">Wrap</span>-up</h2><p class="slide-subtitle">Review your progress and celebrate another step forward.</p></div></div>

<div class="slide slide-light" data-slide="34" data-phase="7" data-teacher="Checklist (3 min): Leia cada item. Clique juntos.">
<div class="slide-inner"><div class="chapter-label">Self-Assessment</div><h2 class="slide-heading">What I <span class="accent">Learned</span></h2>
<div class="check-grid" id="checkGrid">
<div class="check-item" onclick="toggleCheck(this)"><div class="check-box">${SVG_CHECK}</div><span>I can tell my career story in English.</span></div>
<div class="check-item" onclick="toggleCheck(this)"><div class="check-box">${SVG_CHECK}</div><span>I know 8 words about career development.</span></div>
<div class="check-item" onclick="toggleCheck(this)"><div class="check-box">${SVG_CHECK}</div><span>I can use FOR with duration and SINCE with a point in time.</span></div>
<div class="check-item" onclick="toggleCheck(this)"><div class="check-box">${SVG_CHECK}</div><span>I can use EVER in questions and NEVER in negatives.</span></div>
<div class="check-item" onclick="toggleCheck(this)"><div class="check-box">${SVG_CHECK}</div><span>I can describe my education and career transitions.</span></div>
<div class="check-item" onclick="toggleCheck(this)"><div class="check-box">${SVG_CHECK}</div><span>I can talk about achievements and milestones.</span></div>
<div class="check-item" onclick="toggleCheck(this)"><div class="check-box">${SVG_CHECK}</div><span>I can understand another person&rsquo;s career story.</span></div>
<div class="check-item" onclick="toggleCheck(this)"><div class="check-box">${SVG_CHECK}</div><span>I feel more confident sharing my professional journey.</span></div>
</div></div></div>

<div class="slide slide-dark" data-slide="35" data-phase="7" data-teacher="Celebração (1 min).">
<div class="slide-inner"><div class="badge-card"><div class="badge-icon"><div class="badge-circle"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" style="width:48px;height:48px"><path d="M12 15l-3 3 1 4 2-1 2 1 1-4-3-3z"/><circle cx="12" cy="8" r="7"/></svg></div><div class="sparkles"><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div></div></div><h2 style="color:#fff;font-family:'Cormorant Garamond',serif;font-size:2rem">Aula 3 Complete!</h2><p style="color:rgba(255,255,255,.7);margin-top:.5rem">Your career story is ready for the world stage.</p></div></div></div>

<div class="slide slide-dark" data-slide="36" data-phase="7" data-teacher="Preview (2 min): &quot;Next class: The FIFA Mission. We will practice talking about goals and the future.&quot; Homework (ORAL): 1) Gravar áudio de 3 min contando sua trajetória. 2) Atualizar LinkedIn em inglês. 3) Ouvir TED Talk sobre storytelling.">
<div class="slide-inner" style="text-align:center"><div class="chapter-label">Next Lesson Preview</div><h2 class="slide-heading">Coming <span class="accent">Next</span></h2><p class="slide-subtitle" style="margin-top:1rem;opacity:.8">Aula 4: The FIFA Mission &mdash; Goals &amp; Future Plans</p><p class="slide-subtitle" style="opacity:.5;font-size:.85rem;margin-top:1rem">Homework is given orally by the teacher.</p></div></div>

<div class="slide slide-image" data-slide="37" data-phase="7" data-teacher="Encerramento." style="background-image:url('${IMG3}')">
<div class="slide-inner"><div class="chapter-label">Lesson Complete</div><h2 class="slide-title">Day 3 &mdash; <span class="accent">Complete.</span></h2><p class="slide-subtitle" style="opacity:.8;margin-top:1rem">Next: The FIFA Mission</p></div></div>`;

// Use the rebuild script pattern from Aula 2
const rebuildScript = fs.readFileSync(path.join(BASE, 'scripts/rebuild-nilo-aula2.js'), 'utf8');

// Extract the JS template from the Aula 2 file and modify for Aula 3
const aula2File = fs.readFileSync(path.join(BASE, 'public/professor/nilo-mesquita-patucci-aula2.html'), 'utf8');
const jsStart = aula2File.indexOf('// ===== SLIDE NAVIGATION');
const jsEnd = aula2File.lastIndexOf('</script>');
let jsBlock = aula2File.substring(jsStart, jsEnd);

// Replace challenges for Aula 3
const aula3Challenges = JSON.stringify([
  {prompt:'Someone asks: "How long have you been in law?" Answer with Present Perfect.',answer:'"I have been in law for over fifteen years."'},
  {prompt:'Tell the group about your education.',answer:'"I earned my law degree from a university in southern Brazil."'},
  {prompt:'Describe your biggest career transition.',answer:'"The transition from private practice to sports law compliance was the most important move in my career."'},
  {prompt:'What is your proudest achievement?',answer:'"Building the compliance department at Corinthians from the ground up has been my proudest achievement."'},
  {prompt:'Have you ever worked internationally?',answer:'"No, I have never worked outside Brazil, but the FIFA program will be my first international experience."'},
  {prompt:'When did you start specializing in sports law?',answer:'"I have specialized in sports law since about ten years ago, when I saw a growing need for compliance."'},
]);
jsBlock = jsBlock.replace(/var challenges=\[[\s\S]*?\];/, 'var challenges=' + aula3Challenges + ';');

// Build the standalone file
const html = `<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow">
<title>IN CLASS — Nilo Mesquita Patussi | Aula 3 | Alumni by Better</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&display=swap" rel="stylesheet">
<script>
${fullAudioMap}
<\/script>
<style>
${css}
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
<div class="logo-bar"><img src="/assets/logo-alumni.png" alt="Alumni by Better"><span class="prof-badge">Professor View</span><span class="slide-counter" id="slideCounter">01 / 37</span></div>
<div class="slides-wrapper" id="slidesWrapper">
<div class="phase-bar" id="phaseBar"><div class="phase-segment current" data-phase="1"></div><div class="phase-segment upcoming" data-phase="2"></div><div class="phase-segment upcoming" data-phase="3"></div><div class="phase-segment upcoming" data-phase="4"></div><div class="phase-segment upcoming" data-phase="5"></div><div class="phase-segment upcoming" data-phase="6"></div><div class="phase-segment upcoming" data-phase="7"></div></div>
<div class="phase-labels" id="phaseLabels"><span class="phase-label current" data-phase="1">The Journey So Far</span><span class="phase-label" data-phase="2">Packing Words</span><span class="phase-label" data-phase="3">The Code</span><span class="phase-label" data-phase="4">Getting There</span><span class="phase-label" data-phase="5">Practice</span><span class="phase-label" data-phase="6">Your Turn</span><span class="phase-label" data-phase="7">Wrap-up</span></div>
<div class="slides-container" id="slidesContainer">
${slidesHTML}
</div></div>
<div class="teacher-t" id="teacherT">T<div class="teacher-t-panel" id="teacherPanel"></div></div>
<div class="nav-bar"><button class="nav-btn" id="prevBtn" onclick="changeSlide(-1)" disabled><svg viewBox="0 0 24 24"><polyline points="15 18 9 12 15 6"/></svg></button><div class="slide-dots" id="slideDots"></div><button class="nav-btn" id="nextBtn" onclick="changeSlide(1)"><svg viewBox="0 0 24 24"><polyline points="9 6 15 12 9 18"/></svg></button></div>
<div class="confetti-container" id="confettiContainer"></div>
<script>
${jsBlock}
<\/script>
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.min.js"><\/script>
<script src="/lib/supabase-config.js"><\/script>
<script src="/lib/lesson-progress.js"><\/script>
</body>
</html>`;

fs.writeFileSync(path.join(BASE, 'public/professor/nilo-mesquita-patucci-aula3.html'), html);
console.log('Aula 3 standalone written:', html.split('\n').length, 'lines');

// --- UPDATE MAIN FILES ---
// Add stamp3
[path.join(BASE,'public/professor/nilo-mesquita-patucci.html'), path.join(BASE,'public/aluno/nilo-mesquita-patucci.html')].forEach(fp => {
  let f = fs.readFileSync(fp, 'utf8');
  // Add stamp3 after stamp2
  f = f.replace(
    /(<div class="stamp" id="stamp2"[^>]*><\/div>)/,
    '$1\n        <div class="stamp" id="stamp3" data-label="Career" style="background-image:url(\'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=200&q=80\')"></div>'
  );
  // Update totalLessons
  f = f.replace(/totalLessons\s*=\s*2/, 'totalLessons = 3');
  // Add aula3 audio entries to audioMap
  const newEntries = Object.entries(aula3Audio).map(([k,v]) => `  "${k.replace(/"/g,'\\"')}": "${v}"`).join(',\n');
  f = f.replace(/\};\s*<\/script>/, ',\n' + newEntries + '\n};\n<\/script>');
  fs.writeFileSync(fp, f);
  console.log('Updated:', fp);
});

// Add IN CLASS menu card for Aula 3 in professor file
let prof = fs.readFileSync(path.join(BASE,'public/professor/nilo-mesquita-patucci.html'), 'utf8');
prof = prof.replace(
  /<\/div><!-- \/tab-inclass -->/,
  `<div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s;margin-top:1rem" onclick="window.location.href='/professor/nilo-mesquita-patucci-aula3.html'">
  <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">03</div>
  <div><div style="font-weight:600;font-size:.95rem">Career Timeline</div><div style="font-size:.8rem;color:var(--text-dim)">Present Perfect deep dive &mdash; 37 slides</div></div>
</div>
</div><!-- /tab-inclass -->`
);
fs.writeFileSync(path.join(BASE,'public/professor/nilo-mesquita-patucci.html'), prof);

console.log('\nDone! Now add Pre-class + Complementares and generate audio.');
