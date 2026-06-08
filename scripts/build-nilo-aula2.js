#!/usr/bin/env node
/**
 * Build Nilo Aula 2: standalone IN CLASS file + update main professor/aluno files
 */
const fs = require('fs');
const path = require('path');
const BASE = path.join(__dirname, '..');

// --- READ TEMPLATE ---
const tmplAula2 = fs.readFileSync(path.join(BASE, 'public/professor/patricia-ruffo-aula2.html'), 'utf8');

// --- EXTRACT CSS AND JS ---
let css = tmplAula2.match(/<style>([\s\S]*?)<\/style>/)[1];
const jsStart = tmplAula2.indexOf('// ===== AUDIO');
const jsEnd = tmplAula2.lastIndexOf('<\/script>');
let js = tmplAula2.substring(jsStart, jsEnd);

// --- COLOR REPLACEMENT ---
css = css
  .replace(/#2D6A4F/g, '#7B2D3B').replace(/#40916C/g, '#9A4054')
  .replace(/rgba\(45,106,79/g, 'rgba(123,45,59')
  .replace(/#7BEFB2/g, '#F0B8C4').replace(/#52D18A/g, '#E89BA8')
  .replace(/rgba\(51,107,135/g, 'rgba(123,45,59');

js = js.replace(/patricia-ruffo/g, 'nilo-mesquita-patucci')
  .replace(/#2D6A4F/g, '#7B2D3B').replace(/#40916C/g, '#9A4054')
  .replace(/#7BEFB2/g, '#F0B8C4');

// Replace challenges in JS
const newChallenges = `var qcCurrent = 0;
var qcTotal = 6;
var qcScore = 0;`;
js = js.replace(/var qcCurrent[\s\S]*?var qcScore\s*=\s*\d+;/, newChallenges);

// Replace confetti colors
js = js.replace(/var colors\s*=\s*\[[^\]]*\]/, "var colors = ['#7B2D3B','#9A4054','#003080','#16a34a','#d97706','#3B7DD8','#F0B8C4']");

// Replace listening text in toggleListening
js = js.replace(/if \(id === 'listening1'\)[\s\S]*?speakText\(listeningText, btn\);\s*\}/, `if (id === 'listening1') {
    speakText(audioMap['[listening2-full]'] ? '[listening2-full]' : 'The compliance department at Sport Club Corinthians Paulista has five full-time employees.', btn);
  }`);

// --- AUDIOMAP ---
const audioMap = {
  "Department": "/audio/nilo-mesquita-patucci/aula2_department.mp3",
  "Responsibilities": "/audio/nilo-mesquita-patucci/aula2_responsibilities.mp3",
  "Manage": "/audio/nilo-mesquita-patucci/aula2_manage.mp3",
  "Report to": "/audio/nilo-mesquita-patucci/aula2_report_to.mp3",
  "Coordinate": "/audio/nilo-mesquita-patucci/aula2_coordinate.mp3",
  "Headquarters": "/audio/nilo-mesquita-patucci/aula2_headquarters.mp3",
  "Enforce": "/audio/nilo-mesquita-patucci/aula2_enforce.mp3",
  "Investigate": "/audio/nilo-mesquita-patucci/aula2_investigate.mp3",
  "I manage the compliance department at Corinthians.": "/audio/nilo-mesquita-patucci/aula2_i_manage_the_compliance_department_at_corinthi.mp3",
  "My responsibilities include enforcing FIFA regulations.": "/audio/nilo-mesquita-patucci/aula2_my_responsibilities_include_enforcing_fifa_re.mp3",
  "I report to the General Director of the club.": "/audio/nilo-mesquita-patucci/aula2_i_report_to_the_general_director_of_the_club.mp3",
  "We coordinate with the legal department on investigations.": "/audio/nilo-mesquita-patucci/aula2_we_coordinate_with_the_legal_department_on_in.mp3",
  "Our headquarters is located in Sao Paulo.": "/audio/nilo-mesquita-patucci/aula2_our_headquarters_is_located_in_sao_paulo.mp3",
  "We enforce internal regulations and FIFA standards.": "/audio/nilo-mesquita-patucci/aula2_we_enforce_internal_regulations_and_fifa_stand.mp3",
  "The team investigates potential violations of governance rules.": "/audio/nilo-mesquita-patucci/aula2_the_team_investigates_potential_violations_of.mp3",
  "We have a team of five people in the department.": "/audio/nilo-mesquita-patucci/aula2_we_have_a_team_of_five_people_in_the_departme.mp3",
  // Fill-in
  "I manage a team of five people.": "/audio/nilo-mesquita-patucci/aula2_i_manage_a_team_of_five_people.mp3",
  "I report to the General Director.": "/audio/nilo-mesquita-patucci/aula2_i_report_to_the_general_director.mp3",
  "We coordinate with external auditors every quarter.": "/audio/nilo-mesquita-patucci/aula2_we_coordinate_with_external_auditors_every_qu.mp3",
  "Our headquarters is in the Parque Sao Jorge area.": "/audio/nilo-mesquita-patucci/aula2_our_headquarters_is_in_the_parque_sao_jorge_a.mp3",
  "My team investigates compliance violations.": "/audio/nilo-mesquita-patucci/aula2_my_team_investigates_compliance_violations.mp3",
  // Dialogue
  "So, Nilo, what does a typical day look like for you at Corinthians?": "/audio/nilo-mesquita-patucci/aula2_dia_so_nilo_what_does_a_typical_day.mp3",
  "Well, I manage the compliance department. We have a team of five people who work directly with me.": "/audio/nilo-mesquita-patucci/aula2_dia_well_i_manage_the_compliance_department.mp3",
  "That sounds like a lot of responsibility. Who do you report to?": "/audio/nilo-mesquita-patucci/aula2_dia_that_sounds_like_a_lot_of_responsibility.mp3",
  "I report to the General Director. I also coordinate with the legal department on investigations.": "/audio/nilo-mesquita-patucci/aula2_dia_i_report_to_the_general_director.mp3",
  "Interesting! And where is your headquarters?": "/audio/nilo-mesquita-patucci/aula2_dia_interesting_and_where_is_your_headquarter.mp3",
  "Our headquarters is in the Parque Sao Jorge area of Sao Paulo. But I work from our office in Barra Funda.": "/audio/nilo-mesquita-patucci/aula2_dia_our_headquarters_is_in_the_parque_sao_jor.mp3",
  "What is the hardest part of your job?": "/audio/nilo-mesquita-patucci/aula2_dia_what_is_the_hardest_part_of_your_job.mp3",
  "Investigating potential violations is challenging. We enforce FIFA regulations at the club level, and sometimes that creates tension.": "/audio/nilo-mesquita-patucci/aula2_dia_investigating_potential_violations_is_cha.mp3",
  // Grammar examples
  "I manage the team.": "/audio/nilo-mesquita-patucci/aula2_i_manage_the_team.mp3",
  "She coordinates with FIFA.": "/audio/nilo-mesquita-patucci/aula2_she_coordinates_with_fifa.mp3",
  "He reports to the director.": "/audio/nilo-mesquita-patucci/aula2_he_reports_to_the_director.mp3",
  "They investigate violations.": "/audio/nilo-mesquita-patucci/aula2_they_investigate_violations.mp3",
  "Does he manage the department?": "/audio/nilo-mesquita-patucci/aula2_does_he_manage_the_department.mp3",
  "What does the team do?": "/audio/nilo-mesquita-patucci/aula2_what_does_the_team_do.mp3",
  // Listening 1
  "[listening2-full]": "/audio/nilo-mesquita-patucci/aula2_listening1_department.mp3",
  // Listening 2
  "[listening2b-full]": "/audio/nilo-mesquita-patucci/aula2_listening2_amara.mp3",
  // Survival
  "I manage the compliance department.": "/audio/nilo-mesquita-patucci/aula2_i_manage_the_compliance_department.mp3",
  "My main responsibilities include enforcing regulations.": "/audio/nilo-mesquita-patucci/aula2_my_main_responsibilities_include_enforcing_re.mp3",
  "We enforce FIFA regulations at the club.": "/audio/nilo-mesquita-patucci/aula2_we_enforce_fifa_regulations_at_the_club.mp3",
  "[order-l2]": "/audio/nilo-mesquita-patucci/aula2_order_l2.mp3",
  // Speech cards
  "I manage the compliance department and I report to the General Director.": "/audio/nilo-mesquita-patucci/aula2_speech_i_manage_the_compliance.mp3",
  "My responsibilities include enforcing FIFA standards and investigating violations.": "/audio/nilo-mesquita-patucci/aula2_speech_my_responsibilities.mp3",
  "We coordinate with the legal department and external auditors.": "/audio/nilo-mesquita-patucci/aula2_speech_we_coordinate.mp3",
};

// --- SLIDE HELPER ---
function S(num, type, teacherText, content, bgUrl) {
  const cls = (type === 'cover' && num === 1) ? 'slide dark active' : type === 'cover' ? 'slide dark' : type === 'dark' ? 'slide dark' : 'slide light';
  const bg = bgUrl ? ` style="background-image:url('${bgUrl}');background-size:cover;background-position:center"` : '';
  const overlay = bgUrl ? '<div style="position:absolute;inset:0;background:linear-gradient(to bottom,rgba(26,26,46,.7),rgba(26,26,46,.92));z-index:0"></div>' : '';
  const dt = ` data-teacher="${teacherText.replace(/"/g, '&quot;').replace(/'/g, '&#39;')}"`;
  const zIdx = bgUrl ? ' style="position:relative;z-index:1"' : '';
  return `<!-- SLIDE ${num} -->
<div class="${cls}" data-slide="${num}"${dt}${bg}>
${overlay}${bgUrl ? '<div' + zIdx + '>' : ''}
${content}
${bgUrl ? '</div>' : ''}
</div>`;
}

const VOL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width:14px;height:14px"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg>';

// --- SLIDE CONTENT (37 slides) ---
const IMG2 = 'https://images.unsplash.com/photo-1497366216548-37526070297c?w=1400&q=80';
const slides = [];

// Ch1: Your World (1-4)
slides.push(S(1,'cover','Abertura (2 min): Cumprimente normalmente. Deixe o slide visível enquanto faz rapport.',`
<div class="slide-chapter-label">Lesson 2 &mdash; Business English</div>
<h1 class="slide-title">My Professional<br><span class="accent">World</span></h1>
<p class="slide-subtitle">B1 &mdash; 90 minutes &mdash; Alumni by Better</p>
`, IMG2));

slides.push(S(2,'dark','Transição.',`
<div class="slide-chapter-label">Chapter 1</div>
<h2 class="slide-title" style="font-size:2.4rem">Your <span class="accent">World</span></h2>
<p class="slide-subtitle" style="opacity:.7">Warm-up &amp; Callback from Lesson 1</p>
`));

slides.push(S(3,'dark','Callback (5 min): TESTE se o Nilo reteve o vocabulário da Aula 1. Pergunte: "Last class we learned 8 words. Can you introduce yourself using at least 5 of them?" Se travar, dê a primeira letra como pista. NÃO pule o callback.',`
<div class="slide-content">
<div class="slide-chapter-label">Chapter 1: Your World</div>
<h2 class="slide-title" style="font-size:2rem">Callback: <span class="accent">Lesson 1</span></h2>
<div style="display:flex;flex-direction:column;gap:1.5rem;margin-top:1.5rem">
<p style="font-size:1.1rem;color:rgba(255,255,255,.85);font-style:italic;padding-left:1.5rem;border-left:3px solid var(--accent)">&ldquo;Last class you learned 8 words. Can you introduce yourself using at least 5 of them?&rdquo;</p>
<div style="display:flex;flex-wrap:wrap;gap:.5rem;margin-top:1rem">
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
`));

slides.push(S(4,'dark','Warm-up (5 min): Pergunte sobre a rotina. Observe: o Nilo usa Present Simple corretamente? Diz "I manage" ou "I am manage"? Anote erros para contextualizar a gramática.',`
<div class="slide-content">
<div class="slide-chapter-label">Chapter 1: Your World</div>
<h2 class="slide-title" style="font-size:2rem">Your <span class="accent">Routine</span></h2>
<div style="display:flex;flex-direction:column;gap:1.5rem;margin-top:1.5rem">
<p style="font-size:1.15rem;color:rgba(255,255,255,.85);font-style:italic;padding-left:1.5rem;border-left:3px solid var(--accent)">&ldquo;Tell me: what does a typical Monday look like at Corinthians?&rdquo;</p>
<p style="font-size:1.15rem;color:rgba(255,255,255,.85);font-style:italic;padding-left:1.5rem;border-left:3px solid var(--accent)">&ldquo;How many people work with you? Who do you talk to every day?&rdquo;</p>
</div>
</div>
`));

// Ch2: Packing Words (5-7)
slides.push(S(5,'dark','Transição para vocabulário.',`
<div class="slide-chapter-label">Chapter 2</div>
<h2 class="slide-title" style="font-size:2.4rem">Packing <span class="accent">Words</span></h2>
<p class="slide-subtitle" style="opacity:.7">Click on each card to discover the word</p>
`));

slides.push(S(6,'dark','Vocabulário 1 (7 min): Clique em cada card. DEPARTMENT: CCQ "Is a department a person or a division of a company?" (division). MANAGE: CCQ "If I manage a team, am I the boss or an employee?" (boss). REPORT TO: este é novo para o Nilo, faça drilling extra. "I report TO the director" (preposição TO obrigatória).',`
<div class="slide-content">
<div class="slide-chapter-label">Chapter 2: Packing Words</div>
<div class="section-label" style="color:var(--accent-light)">Key Vocabulary (1/2)</div>
<div class="vocab-grid">
<div class="v-card" onclick="this.classList.toggle('revealed')">
<div class="v-card-icon" style="background:linear-gradient(135deg,#7B2D3B,#9A4054)"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" style="width:24px;height:24px"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/></svg></div>
<div class="v-card-hint">A section of an organization responsible for a specific area</div>
<div class="v-card-body"><div class="v-word">Department</div><div class="v-def">A division of a large organization that handles a specific area of work.</div><div class="v-example">&ldquo;I manage the compliance department at Corinthians.&rdquo;</div><button class="v-listen-btn" onclick="event.stopPropagation();speakText('Department',this)">${VOL} Listen</button></div>
</div>
<div class="v-card" onclick="this.classList.toggle('revealed')">
<div class="v-card-icon" style="background:linear-gradient(135deg,#2C5282,#3B7DD8)"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" style="width:24px;height:24px"><path d="M16 4h2a2 2 0 012 2v14a2 2 0 01-2 2H6a2 2 0 01-2-2V6a2 2 0 012-2h2"/><rect x="8" y="2" width="8" height="4" rx="1"/><line x1="9" y1="12" x2="15" y2="12"/><line x1="9" y1="16" x2="13" y2="16"/></svg></div>
<div class="v-card-hint">The tasks and duties that are part of your job</div>
<div class="v-card-body"><div class="v-word">Responsibilities</div><div class="v-def">The duties and tasks that someone must do as part of their role.</div><div class="v-example">&ldquo;My responsibilities include enforcing FIFA regulations.&rdquo;</div><button class="v-listen-btn" onclick="event.stopPropagation();speakText('Responsibilities',this)">${VOL} Listen</button></div>
</div>
<div class="v-card" onclick="this.classList.toggle('revealed')">
<div class="v-card-icon" style="background:linear-gradient(135deg,#553C7B,#7B5EA7)"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" style="width:24px;height:24px"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4-4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/></svg></div>
<div class="v-card-hint">To be in charge of and make decisions about a team</div>
<div class="v-card-body"><div class="v-word">Manage</div><div class="v-def">To be in charge of and make decisions about a project, team, or department.</div><div class="v-example">&ldquo;I manage a team of five compliance professionals.&rdquo;</div><button class="v-listen-btn" onclick="event.stopPropagation();speakText('Manage',this)">${VOL} Listen</button></div>
</div>
<div class="v-card" onclick="this.classList.toggle('revealed')">
<div class="v-card-icon" style="background:linear-gradient(135deg,#1B4D3E,#2D7A5F)"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" style="width:24px;height:24px"><polyline points="16 3 21 3 21 8"/><line x1="4" y1="20" x2="21" y2="3"/><polyline points="21 16 21 21 16 21"/><line x1="15" y1="15" x2="21" y2="21"/></svg></div>
<div class="v-card-hint">To have someone as your direct supervisor</div>
<div class="v-card-body"><div class="v-word">Report to</div><div class="v-def">To be directly supervised by someone; to have someone as your boss.</div><div class="v-example">&ldquo;I report to the General Director of the club.&rdquo;</div><button class="v-listen-btn" onclick="event.stopPropagation();speakText('Report to',this)">${VOL} Listen</button></div>
</div>
</div>
<div class="vocab-counter" id="vocabCount1">Click on each card to reveal</div>
</div>
`));

slides.push(S(7,'dark','Vocabulário 2 (7 min): COORDINATE: drilling "co-OR-di-nate" (stress no 2o). ENFORCE: diferente de "force", mais formal. INVESTIGATE: CCQ "If you investigate something, do you already know the answer?" (no, you are looking for it). HEADQUARTERS: "head-QUAR-ters", plural mas usado como singular "Our headquarters IS...".',`
<div class="slide-content">
<div class="slide-chapter-label">Chapter 2: Packing Words</div>
<div class="section-label" style="color:var(--accent-light)">Key Vocabulary (2/2)</div>
<div class="vocab-grid">
<div class="v-card" onclick="this.classList.toggle('revealed')">
<div class="v-card-icon" style="background:linear-gradient(135deg,#6B4C3B,#8D6E5D)"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" style="width:24px;height:24px"><circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15.3 15.3 0 014 10 15.3 15.3 0 01-4 10 15.3 15.3 0 01-4-10 15.3 15.3 0 014-10z"/></svg></div>
<div class="v-card-hint">To organize people or activities so they work together</div>
<div class="v-card-body"><div class="v-word">Coordinate</div><div class="v-def">To organize different people or activities so they work well together.</div><div class="v-example">&ldquo;We coordinate with the legal department on investigations.&rdquo;</div><button class="v-listen-btn" onclick="event.stopPropagation();speakText('Coordinate',this)">${VOL} Listen</button></div>
</div>
<div class="v-card" onclick="this.classList.toggle('revealed')">
<div class="v-card-icon" style="background:linear-gradient(135deg,#4A5568,#718096)"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" style="width:24px;height:24px"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg></div>
<div class="v-card-hint">The main office where the leaders of an organization work</div>
<div class="v-card-body"><div class="v-word">Headquarters</div><div class="v-def">The main office or center of operations of an organization.</div><div class="v-example">&ldquo;Our headquarters is located in Sao Paulo.&rdquo;</div><button class="v-listen-btn" onclick="event.stopPropagation();speakText('Headquarters',this)">${VOL} Listen</button></div>
</div>
<div class="v-card" onclick="this.classList.toggle('revealed')">
<div class="v-card-icon" style="background:linear-gradient(135deg,#5C3D2E,#7D5A48)"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" style="width:24px;height:24px"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>
<div class="v-card-hint">To make sure people follow a law, rule, or regulation</div>
<div class="v-card-body"><div class="v-word">Enforce</div><div class="v-def">To make sure that people follow a law, rule, or regulation.</div><div class="v-example">&ldquo;We enforce internal regulations and FIFA standards.&rdquo;</div><button class="v-listen-btn" onclick="event.stopPropagation();speakText('Enforce',this)">${VOL} Listen</button></div>
</div>
<div class="v-card" onclick="this.classList.toggle('revealed')">
<div class="v-card-icon" style="background:linear-gradient(135deg,#4A3728,#6B5240)"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" style="width:24px;height:24px"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg></div>
<div class="v-card-hint">To carefully examine a situation to find the truth</div>
<div class="v-card-body"><div class="v-word">Investigate</div><div class="v-def">To carefully examine a situation to find the truth about something.</div><div class="v-example">&ldquo;The team investigates potential violations of governance rules.&rdquo;</div><button class="v-listen-btn" onclick="event.stopPropagation();speakText('Investigate',this)">${VOL} Listen</button></div>
</div>
</div>
<div class="vocab-counter" id="vocabCount2">Click on each card to reveal</div>
</div>
`));

// Ch3: The Code (8-12)
slides.push(S(8,'dark','Transição para gramática.',`<div class="slide-chapter-label">Chapter 3</div><h2 class="slide-title" style="font-size:2.4rem">The <span class="accent">Code</span></h2><p class="slide-subtitle" style="opacity:.7">Grammar: Present Simple for Routines</p>`));

slides.push(S(9,'dark','Gramática Discovery (5 min): NÃO diga a regra. Pergunte: "Look at these sentences. What do you notice about the verbs?" Guie: Present Simple para rotinas, responsabilidades, fatos. 3a pessoa: he/she + -s. CCQ: "Does he manage means now or in the past?" (now/always).',`
<div class="slide-content">
<div class="slide-chapter-label">Chapter 3: The Code</div>
<h2 class="slide-title" style="font-size:1.8rem">What Do You <span class="accent">Notice</span>?</h2>
<div class="grammar-examples">
<div class="g-example">I <span class="highlight">manage</span> the compliance department.</div>
<div class="g-example">She <span class="highlight">coordinates</span> with FIFA every quarter.</div>
<div class="g-example">He <span class="highlight">reports</span> to the General Director.</div>
<div class="g-example">They <span class="highlight">investigate</span> violations.</div>
<div class="g-example"><span class="highlight">Does</span> he <span class="highlight">manage</span> the department?</div>
<div class="g-example">What <span class="highlight">does</span> the team <span class="highlight">do</span>?</div>
</div>
<p style="text-align:center;color:rgba(255,255,255,.6);font-style:italic">What do the highlighted words have in common?</p>
<button class="g-reveal-btn" onclick="this.classList.add('used');this.nextElementSibling.classList.add('show')">Reveal the Rule</button>
<div class="g-rule">
<h4>Present Simple</h4>
<table><thead><tr><th>Form</th><th>Structure</th><th>Example</th></tr></thead>
<tbody>
<tr><td>Affirmative</td><td>I/You/We/They + verb</td><td>I <strong>manage</strong> the team.</td></tr>
<tr><td>Affirmative</td><td>He/She/It + verb + <strong>s</strong></td><td>She <strong>coordinates</strong> with FIFA.</td></tr>
<tr><td>Negative</td><td>do/does + not + verb</td><td>He <strong>does not work</strong> alone.</td></tr>
<tr><td>Question</td><td>Do/Does + subject + verb</td><td><strong>Does</strong> he <strong>manage</strong> the team?</td></tr>
</tbody></table>
</div>
</div>
`));

slides.push(S(10,'dark','Revelação (2 min): Confirme a regra. Reforce o -S na 3a pessoa e a forma com DOES para perguntas. Drilling: "She coordinates" 3x, "Does he manage?" 3x.',`
<div class="slide-content">
<div class="slide-chapter-label">Chapter 3: The Code</div>
<h2 class="slide-title" style="font-size:1.8rem">Common <span class="accent">Mistake</span></h2>
<div class="mistake-box">
<div class="mistake-wrong"><div class="mistake-icon"><svg viewBox="0 0 24 24" fill="none" stroke="#dc2626" stroke-width="2.5" style="width:24px;height:24px"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></div>&ldquo;He manage the department.&rdquo;</div>
<div class="mistake-right"><div class="mistake-icon"><svg viewBox="0 0 24 24" fill="none" stroke="#16a34a" stroke-width="2.5" style="width:24px;height:24px"><polyline points="20 6 9 17 4 12"/></svg></div>&ldquo;He manage<strong>s</strong> the department.&rdquo;</div>
<div class="mistake-wrong" style="margin-top:1rem"><div class="mistake-icon"><svg viewBox="0 0 24 24" fill="none" stroke="#dc2626" stroke-width="2.5" style="width:24px;height:24px"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></div>&ldquo;Does he manages the team?&rdquo;</div>
<div class="mistake-right"><div class="mistake-icon"><svg viewBox="0 0 24 24" fill="none" stroke="#16a34a" stroke-width="2.5" style="width:24px;height:24px"><polyline points="20 6 9 17 4 12"/></svg></div>&ldquo;Does he manage the team?&rdquo;</div>
</div>
</div>
`));

slides.push(S(11,'dark','Prática (5 min): Para cada frase, Nilo completa ORALMENTE. Clique para revelar. Se errar, não corrija direto, pergunte: "Is this he/she or I/we?" Obstáculo: frase 3 ("Does...investigate" sem -s no verbo base).',`
<div class="slide-content">
<div class="slide-chapter-label">Chapter 3: The Code</div>
<div class="section-label" style="color:var(--accent-light)">Grammar Practice</div>
<div class="fill-practice">
<div class="fp-item" onclick="this.classList.toggle('open')"><div class="fp-sentence">She <span class="fp-blank">___</span> (coordinate) with the legal team every week.</div><div class="fp-answer">coordinates</div></div>
<div class="fp-item" onclick="this.classList.toggle('open')"><div class="fp-sentence">I <span class="fp-blank">___</span> (report) directly to the General Director.</div><div class="fp-answer">report</div></div>
<div class="fp-item" onclick="this.classList.toggle('open')"><div class="fp-sentence"><span class="fp-blank">___</span> the team <span class="fp-blank">___</span> (investigate) every complaint?</div><div class="fp-answer">Does ... investigate</div></div>
<div class="fp-item" onclick="this.classList.toggle('open')"><div class="fp-sentence">He <span class="fp-blank">___</span> (not / manage) the legal department. He <span class="fp-blank">___</span> (manage) compliance.</div><div class="fp-answer">does not manage ... manages</div></div>
</div>
</div>
`));

slides.push(S(12,'dark','CCQs extras (2 min): "If I say She coordinates with FIFA, does she do this one time or regularly?" (regularly). "If I say Does he manage, do I add -s to manage?" (no, DOES already carries the -s).',`
<div class="slide-content">
<div class="slide-chapter-label">Chapter 3: The Code</div>
<h2 class="slide-title" style="font-size:1.8rem">Quick <span class="accent">Check</span></h2>
<div style="display:flex;flex-direction:column;gap:.8rem;max-width:700px;width:100%">
<div class="fp-item" onclick="this.classList.toggle('open')"><div class="fp-sentence">1. &ldquo;She coordinates with FIFA.&rdquo; Does she do this one time or regularly?</div><div class="fp-answer">Regularly. Present Simple = habits and routines.</div></div>
<div class="fp-item" onclick="this.classList.toggle('open')"><div class="fp-sentence">2. &ldquo;Does he manage the department?&rdquo; Why is there no -s on &ldquo;manage&rdquo;?</div><div class="fp-answer">Because DOES already carries the third-person marker.</div></div>
<div class="fp-item" onclick="this.classList.toggle('open')"><div class="fp-sentence">3. &ldquo;They investigate violations.&rdquo; Is this a temporary or permanent activity?</div><div class="fp-answer">Permanent. It is part of their job responsibilities.</div></div>
</div>
</div>
`));

// Ch4-7: Getting There, Practice, Your Turn, Wrap-up (slides 13-37)
// I'll generate these more compactly

slides.push(S(13,'dark','Transição para contexto.',`<div class="slide-chapter-label">Chapter 4</div><h2 class="slide-title" style="font-size:2.4rem">Getting <span class="accent">There</span></h2><p class="slide-subtitle" style="opacity:.7">Context, Listening &amp; Dialogue</p>`));

// Org chart artifact
slides.push(S(14,'light','Artefato (5 min): Mostre o organograma. Pergunte: "Who does Nilo report to?", "How many people does Nilo manage?", "What do the three boxes at the bottom represent?" Identifique as 8 palavras no visual.',`
<div class="slide-content">
<div class="slide-chapter-label">Chapter 4: Getting There</div>
<div class="section-label">Compliance Department Structure</div>
<div style="max-width:600px;width:100%;background:#fff;border-radius:12px;padding:2rem;box-shadow:0 8px 32px rgba(0,0,0,.15)">
<div style="text-align:center;margin-bottom:1.5rem">
<div style="display:inline-block;padding:.6rem 1.5rem;background:linear-gradient(135deg,#1a365d,#7B2D3B);color:#fff;border-radius:8px;font-weight:600;font-size:.85rem">General Director</div>
<div style="width:2px;height:30px;background:#ccc;margin:0 auto"></div>
<div style="display:inline-block;padding:.8rem 1.5rem;background:var(--accent);color:#fff;border-radius:8px;font-weight:700;font-size:.95rem">Nilo Patucci<br><span style="font-size:.75rem;font-weight:400">Chief Compliance Officer</span></div>
<div style="width:2px;height:30px;background:#ccc;margin:0 auto"></div>
<div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap">
<div style="padding:.5rem 1rem;background:rgba(123,45,59,.08);border:1px solid rgba(123,45,59,.2);border-radius:6px;font-size:.78rem;color:#1a1a2e"><strong>Enforce</strong><br>Regulations</div>
<div style="padding:.5rem 1rem;background:rgba(123,45,59,.08);border:1px solid rgba(123,45,59,.2);border-radius:6px;font-size:.78rem;color:#1a1a2e"><strong>Investigate</strong><br>Violations</div>
<div style="padding:.5rem 1rem;background:rgba(123,45,59,.08);border:1px solid rgba(123,45,59,.2);border-radius:6px;font-size:.78rem;color:#1a1a2e"><strong>Coordinate</strong><br>Auditors</div>
</div>
</div>
<p style="text-align:center;font-size:.82rem;color:#6b6b7a;margin-top:1rem"><strong>Headquarters:</strong> Barra Funda, Sao Paulo &mdash; <strong>Team:</strong> 5 employees</p>
</div>
</div>
`));

slides.push(S(15,'dark','Comprehensão do artefato (3 min): Perguntas orais sobre o organograma.',`
<div class="slide-content">
<div class="slide-chapter-label">Chapter 4: Getting There</div>
<div class="section-label" style="color:var(--accent-light)">Comprehension</div>
<div style="display:flex;flex-direction:column;gap:.8rem;max-width:700px;width:100%">
<div class="fp-item" onclick="this.classList.toggle('open')"><div class="fp-sentence">1. Who does Nilo report to?</div><div class="fp-answer">The General Director.</div></div>
<div class="fp-item" onclick="this.classList.toggle('open')"><div class="fp-sentence">2. What are the three main responsibilities of the department?</div><div class="fp-answer">Enforce regulations, investigate violations, coordinate with auditors.</div></div>
<div class="fp-item" onclick="this.classList.toggle('open')"><div class="fp-sentence">3. Where is the headquarters?</div><div class="fp-answer">Barra Funda, Sao Paulo.</div></div>
</div>
</div>
`));

// Listening 1
slides.push(S(16,'dark','Listening 1 (5 min): Toque o áudio (voz Ash). Nilo ouve SEM texto. Depois perguntas. Se pedir para ler: "Let us listen first."',`
<div class="slide-content" style="text-align:center">
<div class="slide-chapter-label">Chapter 4: Getting There</div>
<h2 class="slide-title" style="font-size:1.8rem">Listen to This <span class="accent">Description</span></h2>
<p style="color:rgba(255,255,255,.7);margin-bottom:1.5rem">Listen carefully. Questions will appear after the audio ends.</p>
<div class="listening-player" id="lp-listen1" data-src="/audio/nilo-mesquita-patucci/aula2_listening1_department.mp3">
<div class="lp-seekbar" onclick="seekAudio(event,'lp-listen1')"><div class="lp-progress" id="progress-lp-listen1"></div></div>
<div class="lp-time"><span id="time-current-lp-listen1">0:00</span><span id="time-total-lp-listen1">0:00</span></div>
<div class="lp-controls"><button class="lp-btn" onclick="skipAudio('lp-listen1',-5)"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="11 17 6 12 11 7"/><line x1="6" y1="12" x2="18" y2="12"/></svg></button><button class="lp-btn lp-play" onclick="togglePlayer('lp-listen1')"><svg viewBox="0 0 24 24"><polygon points="6 3 20 12 6 21 6 3" fill="currentColor"/></svg></button><button class="lp-btn" onclick="skipAudio('lp-listen1',5)"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="13 7 18 12 13 17"/><line x1="6" y1="12" x2="18" y2="12"/></svg></button></div>
<div class="lp-label" style="font-size:.7rem;color:rgba(255,255,255,.5);text-transform:uppercase;letter-spacing:1.5px;margin-bottom:6px">Speed</div>
<div class="lp-speed"><button class="lp-speed-btn" onclick="setPlayerSpeed('lp-listen1',0.5,this)">0.5x</button><button class="lp-speed-btn" onclick="setPlayerSpeed('lp-listen1',0.75,this)">0.75x</button><button class="lp-speed-btn active" onclick="setPlayerSpeed('lp-listen1',1,this)">1x</button><button class="lp-speed-btn" onclick="setPlayerSpeed('lp-listen1',1.25,this)">1.25x</button></div>
</div>
<div id="questions-lp-listen1" style="display:none;flex-direction:column;gap:.8rem;margin-top:1.5rem;max-width:700px;width:100%">
<div class="fp-item" onclick="this.classList.toggle('open')" style="cursor:pointer"><div class="fp-sentence">1. How many employees are in the compliance department?</div><div class="fp-answer" style="color:var(--accent-light)">Five full-time employees.</div></div>
<div class="fp-item" onclick="this.classList.toggle('open')" style="cursor:pointer"><div class="fp-sentence">2. Who does Nilo report to?</div><div class="fp-answer" style="color:var(--accent-light)">The General Director.</div></div>
<div class="fp-item" onclick="this.classList.toggle('open')" style="cursor:pointer"><div class="fp-sentence">3. What are the three main responsibilities?</div><div class="fp-answer" style="color:var(--accent-light)">Enforce regulations, investigate violations, coordinate with auditors and CBF.</div></div>
</div>
</div>
`));

// Dialogue
slides.push(S(17,'dark','Diálogo (10 min): Lisa Park (voz Riley) e Nilo (voz Ash). Clique Next Line. Fase 1: ouçam. Fase 2: Nilo lê suas falas. Fase 3: invertem papéis. Vocabulário em destaque.',`
<div class="slide-content">
<div class="slide-chapter-label">Chapter 4: Getting There</div>
<h2 class="slide-title" style="font-size:1.8rem;text-align:center">FIFA Networking <span class="accent">Dialogue</span></h2>
<div id="dialogueBox" style="display:flex;flex-direction:column;gap:.6rem;max-width:700px;width:100%;max-height:50vh;overflow-y:auto">
<div class="d-line visible" data-line="1" data-voice="riley"><div class="d-avatar" style="background:#3B7DD8">L</div><div class="d-bubble left">So, Nilo, what does a typical day look like for you at Corinthians?<span class="d-audio" onclick="speakText('So, Nilo, what does a typical day look like for you at Corinthians?',this)">${VOL}</span></div></div>
<div class="d-line" data-line="2" data-voice="ash"><div class="d-avatar" style="background:var(--accent)">N</div><div class="d-bubble right">Well, I <strong class="accent">manage</strong> the compliance <strong class="accent">department</strong>. We have a team of five people who work directly with me.<span class="d-audio" onclick="speakText('Well, I manage the compliance department. We have a team of five people who work directly with me.',this)">${VOL}</span></div></div>
<div class="d-line" data-line="3" data-voice="riley"><div class="d-avatar" style="background:#3B7DD8">L</div><div class="d-bubble left">That sounds like a lot of <strong class="accent">responsibility</strong>. Who do you <strong class="accent">report to</strong>?<span class="d-audio" onclick="speakText('That sounds like a lot of responsibility. Who do you report to?',this)">${VOL}</span></div></div>
<div class="d-line" data-line="4" data-voice="ash"><div class="d-avatar" style="background:var(--accent)">N</div><div class="d-bubble right">I <strong class="accent">report to</strong> the General Director. I also <strong class="accent">coordinate</strong> with the legal department on <strong class="accent">investigate</strong>ions.<span class="d-audio" onclick="speakText('I report to the General Director. I also coordinate with the legal department on investigations.',this)">${VOL}</span></div></div>
<div class="d-line" data-line="5" data-voice="riley"><div class="d-avatar" style="background:#3B7DD8">L</div><div class="d-bubble left">Interesting! And where is your <strong class="accent">headquarters</strong>?<span class="d-audio" onclick="speakText('Interesting! And where is your headquarters?',this)">${VOL}</span></div></div>
<div class="d-line" data-line="6" data-voice="ash"><div class="d-avatar" style="background:var(--accent)">N</div><div class="d-bubble right">Our <strong class="accent">headquarters</strong> is in the Parque Sao Jorge area of Sao Paulo. But I work from our office in Barra Funda.<span class="d-audio" onclick="speakText('Our headquarters is in the Parque Sao Jorge area of Sao Paulo. But I work from our office in Barra Funda.',this)">${VOL}</span></div></div>
<div class="d-line" data-line="7" data-voice="riley"><div class="d-avatar" style="background:#3B7DD8">L</div><div class="d-bubble left">What is the hardest part of your job?<span class="d-audio" onclick="speakText('What is the hardest part of your job?',this)">${VOL}</span></div></div>
<div class="d-line" data-line="8" data-voice="ash"><div class="d-avatar" style="background:var(--accent)">N</div><div class="d-bubble right"><strong class="accent">Investigate</strong>ing potential violations is challenging. We <strong class="accent">enforce</strong> FIFA regulations at the club level, and sometimes that creates tension.<span class="d-audio" onclick="speakText('Investigating potential violations is challenging. We enforce FIFA regulations at the club level, and sometimes that creates tension.',this)">${VOL}</span></div></div>
</div>
<button class="g-reveal-btn" id="nextLineBtn" onclick="nextDialogueLine()" style="margin-top:1rem;max-width:300px">Next Line</button>
</div>
`));

slides.push(S(18,'dark','Comprehensão (3 min): Perguntas sobre LISA (interlocutor), não Nilo.',`
<div class="slide-content">
<div class="slide-chapter-label">Chapter 4: Getting There</div>
<div class="section-label" style="color:var(--accent-light)">Dialogue Comprehension</div>
<div style="display:flex;flex-direction:column;gap:.8rem;max-width:700px;width:100%">
<div class="fp-item" onclick="this.classList.toggle('open')"><div class="fp-sentence">1. What did Lisa ask about first?</div><div class="fp-answer" style="color:var(--accent-light)">What a typical day looks like at Corinthians.</div></div>
<div class="fp-item" onclick="this.classList.toggle('open')"><div class="fp-sentence">2. What did Lisa call &ldquo;a lot of&rdquo;?</div><div class="fp-answer" style="color:var(--accent-light)">Responsibility.</div></div>
<div class="fp-item" onclick="this.classList.toggle('open')"><div class="fp-sentence">3. What was Lisa&rsquo;s last question about?</div><div class="fp-answer" style="color:var(--accent-light)">The hardest part of the job.</div></div>
</div>
</div>
`));

// Listening 2
slides.push(S(19,'dark','Listening 2 (5 min): Voz Riley (Dr. Amara Osei do Ghana). Nilo ouve sem texto. Depois perguntas.',`
<div class="slide-content" style="text-align:center">
<div class="slide-chapter-label">Chapter 4: Getting There</div>
<h2 class="slide-title" style="font-size:1.8rem">Another <span class="accent">Organization</span></h2>
<p style="color:rgba(255,255,255,.7);margin-bottom:1.5rem">Listen to another delegate describe their organization.</p>
<div class="listening-player" id="lp-listen2" data-src="/audio/nilo-mesquita-patucci/aula2_listening2_amara.mp3">
<div class="lp-seekbar" onclick="seekAudio(event,'lp-listen2')"><div class="lp-progress" id="progress-lp-listen2"></div></div>
<div class="lp-time"><span id="time-current-lp-listen2">0:00</span><span id="time-total-lp-listen2">0:00</span></div>
<div class="lp-controls"><button class="lp-btn" onclick="skipAudio('lp-listen2',-5)"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="11 17 6 12 11 7"/><line x1="6" y1="12" x2="18" y2="12"/></svg></button><button class="lp-btn lp-play" onclick="togglePlayer('lp-listen2')"><svg viewBox="0 0 24 24"><polygon points="6 3 20 12 6 21 6 3" fill="currentColor"/></svg></button><button class="lp-btn" onclick="skipAudio('lp-listen2',5)"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="13 7 18 12 13 17"/><line x1="6" y1="12" x2="18" y2="12"/></svg></button></div>
<div class="lp-label" style="font-size:.7rem;color:rgba(255,255,255,.5);text-transform:uppercase;letter-spacing:1.5px;margin-bottom:6px">Speed</div>
<div class="lp-speed"><button class="lp-speed-btn" onclick="setPlayerSpeed('lp-listen2',0.5,this)">0.5x</button><button class="lp-speed-btn" onclick="setPlayerSpeed('lp-listen2',0.75,this)">0.75x</button><button class="lp-speed-btn active" onclick="setPlayerSpeed('lp-listen2',1,this)">1x</button><button class="lp-speed-btn" onclick="setPlayerSpeed('lp-listen2',1.25,this)">1.25x</button></div>
</div>
<div id="questions-lp-listen2" style="display:none;flex-direction:column;gap:.8rem;margin-top:1.5rem;max-width:700px;width:100%">
<div class="fp-item" onclick="this.classList.toggle('open')"><div class="fp-sentence">1. What is Dr. Osei&rsquo;s role?</div><div class="fp-answer" style="color:var(--accent-light)">She manages the governance unit at the Ghana Football Association.</div></div>
<div class="fp-item" onclick="this.classList.toggle('open')"><div class="fp-sentence">2. How many people are on her team?</div><div class="fp-answer" style="color:var(--accent-light)">Eight people.</div></div>
<div class="fp-item" onclick="this.classList.toggle('open')"><div class="fp-sentence">3. What do they investigate?</div><div class="fp-answer" style="color:var(--accent-light)">Match-fixing allegations.</div></div>
</div>
</div>
`));

// Ch5: Practice (20-26)
slides.push(S(20,'dark','Transição.',`<div class="slide-chapter-label">Chapter 5</div><h2 class="slide-title" style="font-size:2.4rem"><span class="accent">Practice</span></h2><p class="slide-subtitle" style="opacity:.7">Quick Fire, Spot the Error &amp; Drilling</p>`));

slides.push(S(21,'dark','Quick Fire (8 min): Uma por vez. Nilo responde ORALMENTE, clica Show Answer.',`
<div class="slide-content" style="text-align:center">
<div class="slide-chapter-label">Chapter 5: Practice</div>
<div class="section-label" style="color:var(--accent-light)">Quick Fire</div>
<div id="qcScore" style="position:absolute;top:1rem;right:1rem;background:var(--accent);color:#fff;padding:.3rem .8rem;border-radius:20px;font-size:.8rem;font-weight:700">0 / 6</div>
<div class="qc-card active" data-qc="1"><div style="font-size:.8rem;color:rgba(255,255,255,.5);margin-bottom:1rem">Question 1 of 6</div><div style="font-family:'Cormorant Garamond',serif;font-size:1.3rem;color:#fff;margin-bottom:1.5rem">Someone asks: &ldquo;What do you do at Corinthians?&rdquo; Describe your role.</div><div class="qc-answer-box" style="display:none;background:rgba(123,45,59,.12);border:1px solid rgba(123,45,59,.25);border-radius:10px;padding:1rem;color:var(--accent-light);font-weight:600">&ldquo;I manage the compliance department. My responsibilities include enforcing FIFA regulations.&rdquo;</div><button class="g-reveal-btn" onclick="showQcAnswer(this)" style="max-width:200px">Show Answer</button><button class="g-reveal-btn qc-next-btn" onclick="nextQc()" style="display:none;max-width:200px;margin-top:.5rem">Next Question</button></div>
<div class="qc-card" data-qc="2"><div style="font-size:.8rem;color:rgba(255,255,255,.5);margin-bottom:1rem">Question 2 of 6</div><div style="font-family:'Cormorant Garamond',serif;font-size:1.3rem;color:#fff;margin-bottom:1.5rem">A delegate asks: &ldquo;Who is your boss?&rdquo; Answer formally.</div><div class="qc-answer-box" style="display:none;background:rgba(123,45,59,.12);border:1px solid rgba(123,45,59,.25);border-radius:10px;padding:1rem;color:var(--accent-light);font-weight:600">&ldquo;I report to the General Director of the club.&rdquo;</div><button class="g-reveal-btn" onclick="showQcAnswer(this)" style="max-width:200px">Show Answer</button><button class="g-reveal-btn qc-next-btn" onclick="nextQc()" style="display:none;max-width:200px;margin-top:.5rem">Next Question</button></div>
<div class="qc-card" data-qc="3"><div style="font-size:.8rem;color:rgba(255,255,255,.5);margin-bottom:1rem">Question 3 of 6</div><div style="font-family:'Cormorant Garamond',serif;font-size:1.3rem;color:#fff;margin-bottom:1.5rem">Explain what your team does day to day.</div><div class="qc-answer-box" style="display:none;background:rgba(123,45,59,.12);border:1px solid rgba(123,45,59,.25);border-radius:10px;padding:1rem;color:var(--accent-light);font-weight:600">&ldquo;We enforce internal regulations, investigate potential violations, and coordinate with external auditors.&rdquo;</div><button class="g-reveal-btn" onclick="showQcAnswer(this)" style="max-width:200px">Show Answer</button><button class="g-reveal-btn qc-next-btn" onclick="nextQc()" style="display:none;max-width:200px;margin-top:.5rem">Next Question</button></div>
<div class="qc-card" data-qc="4"><div style="font-size:.8rem;color:rgba(255,255,255,.5);margin-bottom:1rem">Question 4 of 6</div><div style="font-family:'Cormorant Garamond',serif;font-size:1.3rem;color:#fff;margin-bottom:1.5rem">Where is your headquarters?</div><div class="qc-answer-box" style="display:none;background:rgba(123,45,59,.12);border:1px solid rgba(123,45,59,.25);border-radius:10px;padding:1rem;color:var(--accent-light);font-weight:600">&ldquo;Our headquarters is in the Parque Sao Jorge area of Sao Paulo. I work from our office in Barra Funda.&rdquo;</div><button class="g-reveal-btn" onclick="showQcAnswer(this)" style="max-width:200px">Show Answer</button><button class="g-reveal-btn qc-next-btn" onclick="nextQc()" style="display:none;max-width:200px;margin-top:.5rem">Next Question</button></div>
<div class="qc-card" data-qc="5"><div style="font-size:.8rem;color:rgba(255,255,255,.5);margin-bottom:1rem">Question 5 of 6</div><div style="font-family:'Cormorant Garamond',serif;font-size:1.3rem;color:#fff;margin-bottom:1.5rem">What is the most challenging part of your role?</div><div class="qc-answer-box" style="display:none;background:rgba(123,45,59,.12);border:1px solid rgba(123,45,59,.25);border-radius:10px;padding:1rem;color:var(--accent-light);font-weight:600">&ldquo;Investigating potential violations is challenging. We enforce regulations at the club level, and sometimes that creates tension.&rdquo;</div><button class="g-reveal-btn" onclick="showQcAnswer(this)" style="max-width:200px">Show Answer</button><button class="g-reveal-btn qc-next-btn" onclick="nextQc()" style="display:none;max-width:200px;margin-top:.5rem">Next Question</button></div>
<div class="qc-card" data-qc="6"><div style="font-size:.8rem;color:rgba(255,255,255,.5);margin-bottom:1rem">Question 6 of 6</div><div style="font-family:'Cormorant Garamond',serif;font-size:1.3rem;color:#fff;margin-bottom:1.5rem">How does your department work with other departments?</div><div class="qc-answer-box" style="display:none;background:rgba(123,45,59,.12);border:1px solid rgba(123,45,59,.25);border-radius:10px;padding:1rem;color:var(--accent-light);font-weight:600">&ldquo;We coordinate with the legal department and with external auditors every quarter.&rdquo;</div><button class="g-reveal-btn" onclick="showQcAnswer(this)" style="max-width:200px">Show Answer</button></div>
</div>
`));

// Spot the Error
slides.push(S(22,'dark','Spot the Error (5 min): Nilo identifica antes de clicar.',`
<div class="slide-content">
<div class="slide-chapter-label">Chapter 5: Practice</div>
<div class="section-label" style="color:var(--accent-light)">Spot the Error</div>
<div style="display:flex;flex-direction:column;gap:.8rem;max-width:700px;width:100%">
<div class="fp-item" onclick="this.classList.toggle('open')"><div class="fp-sentence" style="color:#fca5a5">&ldquo;He manage the compliance department.&rdquo;</div><div class="fp-answer" style="color:#86efac">&ldquo;He manage<strong>s</strong> the compliance department.&rdquo; (3rd person -s)</div></div>
<div class="fp-item" onclick="this.classList.toggle('open')"><div class="fp-sentence" style="color:#fca5a5">&ldquo;Does she coordinates with FIFA?&rdquo;</div><div class="fp-answer" style="color:#86efac">&ldquo;Does she coordinate with FIFA?&rdquo; (no -s after does)</div></div>
<div class="fp-item" onclick="this.classList.toggle('open')"><div class="fp-sentence" style="color:#fca5a5">&ldquo;I am report to the General Director.&rdquo;</div><div class="fp-answer" style="color:#86efac">&ldquo;I report to the General Director.&rdquo; (Present Simple, no &ldquo;am&rdquo;)</div></div>
<div class="fp-item" onclick="this.classList.toggle('open')"><div class="fp-sentence" style="color:#fca5a5">&ldquo;The team investigate the violations every month.&rdquo;</div><div class="fp-answer" style="color:#86efac">&ldquo;The team investigate<strong>s</strong> the violations every month.&rdquo; (&ldquo;the team&rdquo; = singular)</div></div>
</div>
</div>
`));

// Oral drilling slides 23-26
slides.push(S(23,'dark','Oral Drilling (5 min): Situações. Nilo responde oralmente.',`
<div class="slide-content">
<div class="slide-chapter-label">Chapter 5: Practice</div>
<div class="section-label" style="color:var(--accent-light)">Oral Drilling (1/2)</div>
<div style="display:flex;flex-direction:column;gap:.8rem;max-width:700px;width:100%">
<div class="fp-item" onclick="this.classList.toggle('open')"><div class="fp-sentence">1. Describe your department in one sentence.</div><div class="fp-answer">&ldquo;I manage the compliance department at Corinthians.&rdquo;</div></div>
<div class="fp-item" onclick="this.classList.toggle('open')"><div class="fp-sentence">2. Who is your direct supervisor?</div><div class="fp-answer">&ldquo;I report to the General Director.&rdquo;</div></div>
<div class="fp-item" onclick="this.classList.toggle('open')"><div class="fp-sentence">3. How do you work with other departments?</div><div class="fp-answer">&ldquo;I coordinate with the legal department on investigations.&rdquo;</div></div>
</div>
</div>
`));

slides.push(S(24,'dark','Oral Drilling 2 (5 min).',`
<div class="slide-content">
<div class="slide-chapter-label">Chapter 5: Practice</div>
<div class="section-label" style="color:var(--accent-light)">Oral Drilling (2/2)</div>
<div style="display:flex;flex-direction:column;gap:.8rem;max-width:700px;width:100%">
<div class="fp-item" onclick="this.classList.toggle('open')"><div class="fp-sentence">4. Where is the main office?</div><div class="fp-answer">&ldquo;Our headquarters is in Sao Paulo.&rdquo;</div></div>
<div class="fp-item" onclick="this.classList.toggle('open')"><div class="fp-sentence">5. What does your team do when there is a problem?</div><div class="fp-answer">&ldquo;We investigate potential violations of governance rules.&rdquo;</div></div>
<div class="fp-item" onclick="this.classList.toggle('open')"><div class="fp-sentence">6. How do you make sure people follow the rules?</div><div class="fp-answer">&ldquo;We enforce internal regulations and FIFA standards.&rdquo;</div></div>
</div>
</div>
`));

slides.push(S(25,'dark','Sentence Building (5 min).',`
<div class="slide-content">
<div class="slide-chapter-label">Chapter 5: Practice</div>
<div class="section-label" style="color:var(--accent-light)">Sentence Building</div>
<div style="display:flex;flex-direction:column;gap:.8rem;max-width:700px;width:100%">
<div class="fp-item" onclick="this.classList.toggle('open')"><div class="fp-sentence">department / the / compliance / manage / I</div><div class="fp-answer">&ldquo;I manage the compliance department.&rdquo;</div></div>
<div class="fp-item" onclick="this.classList.toggle('open')"><div class="fp-sentence">to / Director / I / the / General / report</div><div class="fp-answer">&ldquo;I report to the General Director.&rdquo;</div></div>
<div class="fp-item" onclick="this.classList.toggle('open')"><div class="fp-sentence">coordinates / she / quarter / every / FIFA / with</div><div class="fp-answer">&ldquo;She coordinates with FIFA every quarter.&rdquo;</div></div>
<div class="fp-item" onclick="this.classList.toggle('open')"><div class="fp-sentence">regulations / enforce / we / FIFA / club / the / at</div><div class="fp-answer">&ldquo;We enforce FIFA regulations at the club.&rdquo;</div></div>
<div class="fp-item" onclick="this.classList.toggle('open')"><div class="fp-sentence">does / team / the / what / do / ?</div><div class="fp-answer">&ldquo;What does the team do?&rdquo;</div></div>
</div>
</div>
`));

slides.push(S(26,'dark','Pronúncia (5 min): Foco nas palavras com stress diferente do PT. Drilling 3x cada.',`
<div class="slide-content" style="text-align:center">
<div class="slide-chapter-label">Chapter 5: Practice</div>
<div class="section-label" style="color:var(--accent-light)">Pronunciation Focus</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;max-width:500px;width:100%">
<div style="background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);border-radius:10px;padding:1.2rem;text-align:center"><div style="font-size:1.2rem;color:#fff">de&middot;<strong>PART</strong>&middot;ment</div><button class="v-listen-btn" onclick="speakText('Department',this)" style="margin-top:.5rem">${VOL} Listen</button></div>
<div style="background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);border-radius:10px;padding:1.2rem;text-align:center"><div style="font-size:1.2rem;color:#fff">re&middot;spon&middot;si&middot;<strong>BIL</strong>&middot;i&middot;ties</div><button class="v-listen-btn" onclick="speakText('Responsibilities',this)" style="margin-top:.5rem">${VOL} Listen</button></div>
<div style="background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);border-radius:10px;padding:1.2rem;text-align:center"><div style="font-size:1.2rem;color:#fff">co&middot;<strong>OR</strong>&middot;di&middot;nate</div><button class="v-listen-btn" onclick="speakText('Coordinate',this)" style="margin-top:.5rem">${VOL} Listen</button></div>
<div style="background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);border-radius:10px;padding:1.2rem;text-align:center"><div style="font-size:1.2rem;color:#fff">in&middot;<strong>VES</strong>&middot;ti&middot;gate</div><button class="v-listen-btn" onclick="speakText('Investigate',this)" style="margin-top:.5rem">${VOL} Listen</button></div>
</div>
</div>
`));

// Ch6: Your Turn (27-32)
slides.push(S(27,'dark','Transição.',`<div class="slide-chapter-label">Chapter 6</div><h2 class="slide-title" style="font-size:2.4rem">Your <span class="accent">Turn</span></h2><p class="slide-subtitle" style="opacity:.7">From Guided to Free</p>`));

slides.push(S(28,'dark','Role-play Guiado (5 min): Professor é delegate curioso. Nilo descreve seu departamento. NÃO corrija, anote erros.',`
<div class="slide-content" style="text-align:center">
<div class="slide-chapter-label">Chapter 6: Your Turn</div>
<div class="section-label" style="color:var(--accent-light)">Role-play: Guided</div>
<div style="max-width:500px;width:100%;background:rgba(255,255,255,.04);border:2px solid var(--accent);border-radius:16px;padding:2rem">
<div style="width:60px;height:60px;border-radius:50%;background:linear-gradient(135deg,#7B2D3B,#9A4054);margin:0 auto 1rem;display:flex;align-items:center;justify-content:center"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" style="width:28px;height:28px"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4-4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/></svg></div>
<p style="font-size:1rem;color:rgba(255,255,255,.85);line-height:1.6;margin-bottom:1.5rem">A delegate from Japan asks you to describe your department at Corinthians. Use the keywords below.</p>
<div style="display:flex;flex-wrap:wrap;gap:.4rem;justify-content:center">
<span style="padding:.3rem .7rem;background:rgba(123,45,59,.15);border:1px solid rgba(123,45,59,.3);border-radius:16px;font-size:.8rem;color:var(--accent-light)">department</span>
<span style="padding:.3rem .7rem;background:rgba(123,45,59,.15);border:1px solid rgba(123,45,59,.3);border-radius:16px;font-size:.8rem;color:var(--accent-light)">manage</span>
<span style="padding:.3rem .7rem;background:rgba(123,45,59,.15);border:1px solid rgba(123,45,59,.3);border-radius:16px;font-size:.8rem;color:var(--accent-light)">report to</span>
<span style="padding:.3rem .7rem;background:rgba(123,45,59,.15);border:1px solid rgba(123,45,59,.3);border-radius:16px;font-size:.8rem;color:var(--accent-light)">responsibilities</span>
<span style="padding:.3rem .7rem;background:rgba(123,45,59,.15);border:1px solid rgba(123,45,59,.3);border-radius:16px;font-size:.8rem;color:var(--accent-light)">five people</span>
<span style="padding:.3rem .7rem;background:rgba(123,45,59,.15);border:1px solid rgba(123,45,59,.3);border-radius:16px;font-size:.8rem;color:var(--accent-light)">headquarters</span>
</div>
</div>
</div>
`));

slides.push(S(29,'dark','Role-play Semi-livre (5 min): Menos keywords.',`
<div class="slide-content" style="text-align:center">
<div class="slide-chapter-label">Chapter 6: Your Turn</div>
<div class="section-label" style="color:var(--accent-light)">Role-play: Semi-free</div>
<div style="max-width:500px;width:100%;background:rgba(255,255,255,.04);border:2px solid rgba(255,255,255,.15);border-radius:16px;padding:2rem">
<p style="font-size:1rem;color:rgba(255,255,255,.85);line-height:1.6;margin-bottom:1.5rem">You are having lunch with delegates from three different countries. They want to know how your organization is structured and what makes your role unique.</p>
<div style="display:flex;flex-wrap:wrap;gap:.4rem;justify-content:center">
<span style="padding:.3rem .7rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.15);border-radius:16px;font-size:.8rem;color:rgba(255,255,255,.6)">enforce</span>
<span style="padding:.3rem .7rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.15);border-radius:16px;font-size:.8rem;color:rgba(255,255,255,.6)">investigate</span>
<span style="padding:.3rem .7rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.15);border-radius:16px;font-size:.8rem;color:rgba(255,255,255,.6)">coordinate</span>
</div>
</div>
</div>
`));

slides.push(S(30,'dark','Role-play Livre (5 min): ZERO apoio. NÃO corrija. Anote erros.',`
<div class="slide-content" style="text-align:center">
<div class="slide-chapter-label">Chapter 6: Your Turn</div>
<div class="section-label" style="color:var(--accent-light)">Role-play: Free</div>
<div style="max-width:500px;width:100%;background:rgba(255,255,255,.04);border:2px solid rgba(255,255,255,.15);border-radius:16px;padding:2rem">
<p style="font-size:1rem;color:rgba(255,255,255,.85);line-height:1.6">The FIFA program director asks you to explain your organization to the entire group. Speak for 2 minutes. No keywords. No script. Just you and your professional world.</p>
</div>
</div>
`));

slides.push(S(31,'light','Delayed Error Correction (5 min): Compartilhe 3-5 erros. Foque em Present Simple (3a pessoa -s, forma com does). Nilo repete a versão correta 2x.',`
<div class="slide-content">
<div class="slide-chapter-label">Chapter 6: Your Turn</div>
<div class="section-label">Error Correction</div>
<p style="font-size:.9rem;color:var(--text-dim);margin-bottom:1rem">Teacher: type the errors you observed during the free role-play.</p>
<div style="background:#fff;border:2px solid var(--border);border-radius:10px;padding:1.5rem;min-height:200px" contenteditable="true"><p style="color:var(--text-dim);font-style:italic">Click here and type the errors observed...</p></div>
</div>
`));

slides.push(S(32,'dark','Produção (5 min): Nilo descreve o departamento gravando áudio de 2 min.',`
<div class="slide-content" style="text-align:center">
<div class="slide-chapter-label">Chapter 6: Your Turn</div>
<h2 class="slide-title" style="font-size:1.8rem">Describe Your <span class="accent">Department</span></h2>
<div style="max-width:500px;width:100%;background:rgba(255,255,255,.04);border:2px solid rgba(255,255,255,.08);border-radius:16px;padding:2rem;margin:0 auto">
<p style="color:rgba(255,255,255,.85);margin-bottom:1.5rem">Describe your department to a new colleague. Include: what you manage, who you report to, your responsibilities, and where your headquarters is.</p>
<button style="width:72px;height:72px;border-radius:50%;background:#dc2626;border:none;color:#fff;cursor:pointer;display:flex;align-items:center;justify-content:center;margin:0 auto" onclick="toggleReflectionRecord(this)"><svg viewBox="0 0 24 24" style="width:28px;height:28px"><path d="M12 1a3 3 0 00-3 3v8a3 3 0 006 0V4a3 3 0 00-3-3z" fill="#fff"/><path d="M19 10v2a7 7 0 01-14 0v-2" fill="none" stroke="#fff" stroke-width="2"/></svg></button>
<div id="reflectionResult" style="margin-top:1rem"></div>
</div>
</div>
`));

// Ch7: Wrap-up (33-37)
slides.push(S(33,'dark','Transição.',`<div class="slide-chapter-label">Chapter 7</div><h2 class="slide-title" style="font-size:2.4rem"><span class="accent">Wrap</span>-up</h2><p class="slide-subtitle" style="opacity:.7">What You Learned Today</p>`));

slides.push(S(34,'light','Checklist (3 min): Leia cada item. Pergunte: "Can you say yes to this?" Clique juntos.',`
<div class="slide-content">
<div class="section-label">Self-Assessment</div>
<h2 style="font-family:'Cormorant Garamond',serif;font-size:1.8rem;margin-bottom:1.2rem;color:var(--text)">What I <span style="color:var(--accent)">Learned</span></h2>
<div style="display:flex;flex-direction:column;gap:.5rem;max-width:700px;width:100%">
<div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3" style="width:14px;height:14px;opacity:0"><polyline points="20 6 9 17 4 12"/></svg></div><span>I can describe my department and responsibilities.</span></div>
<div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3" style="width:14px;height:14px;opacity:0"><polyline points="20 6 9 17 4 12"/></svg></div><span>I know 8 words about organizational structure.</span></div>
<div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3" style="width:14px;height:14px;opacity:0"><polyline points="20 6 9 17 4 12"/></svg></div><span>I can use Present Simple for routines and facts.</span></div>
<div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3" style="width:14px;height:14px;opacity:0"><polyline points="20 6 9 17 4 12"/></svg></div><span>I can add -s to verbs with he/she/it.</span></div>
<div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3" style="width:14px;height:14px;opacity:0"><polyline points="20 6 9 17 4 12"/></svg></div><span>I can explain who I report to.</span></div>
<div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3" style="width:14px;height:14px;opacity:0"><polyline points="20 6 9 17 4 12"/></svg></div><span>I can ask questions with &ldquo;Does he/she...?&rdquo;</span></div>
<div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3" style="width:14px;height:14px;opacity:0"><polyline points="20 6 9 17 4 12"/></svg></div><span>I understand the structure of a compliance department.</span></div>
<div class="check-item" onclick="toggleCheck(this)"><div class="check-box"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3" style="width:14px;height:14px;opacity:0"><polyline points="20 6 9 17 4 12"/></svg></div><span>I feel more confident describing my professional world.</span></div>
</div>
</div>
`));

slides.push(S(35,'dark','Celebração (1 min): Valide o progresso.',`
<div style="text-align:center">
<div style="width:120px;height:120px;margin:0 auto 1.5rem;position:relative">
<div style="width:120px;height:120px;border-radius:50%;background:linear-gradient(135deg,var(--accent),#9A4054);display:flex;align-items:center;justify-content:center"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" style="width:48px;height:48px"><path d="M12 15l-3 3 1 4 2-1 2 1 1-4-3-3z"/><circle cx="12" cy="8" r="7"/></svg></div>
</div>
<h2 style="color:#fff;font-family:'Cormorant Garamond',serif;font-size:2rem">Aula 2 Complete!</h2>
<p style="color:rgba(255,255,255,.7);margin-top:.5rem">Your professional world is now in English.</p>
</div>
`));

slides.push(S(36,'dark','Preview (2 min): "Next class: Career Timeline. We will practice talking about your professional history." Homework (ORAL): 1) Gravar áudio de 2 min descrevendo o departamento. 2) Ouvir um episódio de ESPN FC. 3) Anotar 3 frases que usa no dia a dia sobre rotina.',`
<div style="text-align:center">
<div class="slide-chapter-label">Next Lesson Preview</div>
<h2 class="slide-title" style="font-size:2rem">Coming <span class="accent">Next</span></h2>
<p class="slide-subtitle" style="margin-top:1rem;opacity:.8">Aula 3: Career Timeline &mdash; Narrating Professional History</p>
<p class="slide-subtitle" style="opacity:.5;font-size:.85rem;margin-top:1rem">Homework is given orally by the teacher.</p>
</div>
`));

slides.push(S(37,'cover','Encerramento (1 min): "Great class, Nilo. Your professional world is ready for Miami."',`
<div class="slide-chapter-label">Lesson Complete</div>
<h1 class="slide-title">Day 2 &mdash; <span class="accent">Complete.</span></h1>
<p class="slide-subtitle" style="opacity:.8;margin-top:1rem">Next: Career Timeline</p>
`, IMG2));

// --- ASSEMBLE STANDALONE FILE ---
// Extract the HTML structure (head, body wrapper) from template
const tmplHead = tmplAula2.substring(0, tmplAula2.indexOf('<style>'));
const tmplBodyStart = tmplAula2.substring(tmplAula2.indexOf('</head>'), tmplAula2.indexOf('<!-- SLIDE 1'));
const tmplBodyEnd = tmplAula2.substring(tmplAula2.lastIndexOf('</div><!-- /slide-deck -->'));

// Build the file using the template structure but our content
const aula2HTML = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow">
<title>IN CLASS &mdash; Nilo Mesquita Patucci | Lesson 2 | Alumni by Better</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Cormorant+Garamond:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
${css}
</style>
<script>window.STUDENT_SLUG='nilo-mesquita-patucci';window.TOTAL_AULAS=96;<\/script>
</head>
<body>

<!-- TOP BAR -->
<div class="top-bar">
<div class="top-bar-left">
<img src="/assets/logo-alumni.png" alt="Alumni" class="top-bar-logo">
<div class="chapter-bar" id="chapterBar"></div>
</div>
<div class="top-bar-right">
<span class="slide-counter" id="slideCounter">01 / 37</span>
</div>
</div>

<!-- TEACHER CUE -->
<div class="t-cue" id="tCue" onclick="document.getElementById('tPanel').classList.toggle('show')">T</div>
<div class="t-panel" id="tPanel"></div>

<!-- SLIDE DECK -->
<div class="slide-deck" id="slideDeck">
${slides.join('\n\n')}
</div>

<!-- DOT NAV -->
<div class="dot-nav" id="dotNav"></div>

<!-- NAV ARROWS -->
<div class="nav-arrows">
<button class="nav-btn" id="prevBtn" onclick="changeSlide(-1)"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 18 9 12 15 6"/></svg></button>
<button class="nav-btn" id="nextBtn" onclick="changeSlide(1)"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="9 6 15 12 9 18"/></svg></button>
</div>

<!-- Confetti -->
<div id="confettiContainer" style="position:fixed;inset:0;pointer-events:none;z-index:9999"></div>

<script>
var audioMap = ${JSON.stringify(audioMap, null, 2)};

${js}
</script>
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.min.js"><\/script>
<script src="/lib/supabase-config.js"><\/script>
<script src="/lib/lesson-progress.js"><\/script>
<script src="/lib/controle-aulas.js"><\/script>
<script src="/lib/activity-sync.js"><\/script>
</body>
</html>`;

fs.writeFileSync(path.join(BASE, 'public/professor/nilo-mesquita-patucci-aula2.html'), aula2HTML);
console.log('Standalone aula2 file written:', aula2HTML.length, 'chars,', aula2HTML.split('\n').length, 'lines');

// --- UPDATE MAIN PROFESSOR FILE ---
let prof = fs.readFileSync(path.join(BASE, 'public/professor/nilo-mesquita-patucci.html'), 'utf8');

// 1. Add stamp2 after stamp1
prof = prof.replace(
  /<div class="stamp" id="stamp1"[^>]*><\/div>/,
  match => match + '\n        <div class="stamp" id="stamp2" data-label="My World" style="background-image:url(\'https://images.unsplash.com/photo-1497366216548-37526070297c?w=200&q=80\')"></div>'
);

// 2. Add Aula 2 IN CLASS menu card
prof = prof.replace(
  /<\/div><!-- \/tab-inclass -->/,
  `<div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s;margin-top:1rem" onclick="window.location.href='/professor/nilo-mesquita-patucci-aula2.html'">
  <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">02</div>
  <div><div style="font-weight:600;font-size:.95rem">My Professional World</div><div style="font-size:.8rem;color:var(--text-dim)">Describing Role &amp; Organization &mdash; 37 slides</div></div>
</div>
</div><!-- /tab-inclass -->`
);

// 3. Add audioMap entries for Aula 2
const newAudioEntries = Object.entries(audioMap).map(([k,v]) => `  "${k.replace(/"/g, '\\"')}": "${v}"`).join(',\n');
prof = prof.replace(
  /\};\s*<\/script>/,
  `,\n${newAudioEntries}\n};\n<\/script>`
);

// 4. Update totalLessons in JS
prof = prof.replace(/totalLessons\s*=\s*1/, 'totalLessons = 2');

fs.writeFileSync(path.join(BASE, 'public/professor/nilo-mesquita-patucci.html'), prof);
console.log('Professor main file updated');

// --- UPDATE ALUNO FILE ---
let alunoFile = fs.readFileSync(path.join(BASE, 'public/aluno/nilo-mesquita-patucci.html'), 'utf8');

// Add stamp2
alunoFile = alunoFile.replace(
  /<div class="stamp" id="stamp1"[^>]*><\/div>/,
  match => match + '\n        <div class="stamp" id="stamp2" data-label="My World" style="background-image:url(\'https://images.unsplash.com/photo-1497366216548-37526070297c?w=200&q=80\')"></div>'
);

// Add audioMap entries
alunoFile = alunoFile.replace(
  /\};\s*<\/script>/,
  `,\n${newAudioEntries}\n};\n<\/script>`
);

// Update totalLessons
alunoFile = alunoFile.replace(/totalLessons\s*=\s*1/, 'totalLessons = 2');

fs.writeFileSync(path.join(BASE, 'public/aluno/nilo-mesquita-patucci.html'), alunoFile);
console.log('Aluno file updated');

console.log('\nAll done! Now generate audio and add Pre-class lesson 2 content.');
