#!/usr/bin/env node
/**
 * Generates /public/professor/nilo-mesquita-patucci.html
 * Reads CSS from patricia-ruffo template, content from aluno file.
 */
const fs = require('fs');
const path = require('path');

const BASE = path.join(__dirname, '..');
const TEMPLATE = path.join(BASE, 'public/professor/patricia-ruffo.html');
const ALUNO = path.join(BASE, 'public/aluno/nilo-mesquita-patucci.html');
const OUTPUT = path.join(BASE, 'public/professor/nilo-mesquita-patucci.html');

// --- READ FILES ---
const tmpl = fs.readFileSync(TEMPLATE, 'utf8');
const aluno = fs.readFileSync(ALUNO, 'utf8');

// --- EXTRACT CSS FROM TEMPLATE ---
let css = tmpl.match(/<style>([\s\S]*?)<\/style>/)[1];
// Replace accent colors
css = css
  .replace(/--accent:\s*#2D6A4F/g, '--accent: #7B2D3B')
  .replace(/--accent-light:\s*#40916C/g, '--accent-light: #9A4054')
  .replace(/rgba\(45,106,79/g, 'rgba(123,45,59')
  .replace(/#7BEFB2/g, '#F0B8C4')
  .replace(/#52D18A/g, '#E89BA8')
  .replace(/rgba\(51,107,135/g, 'rgba(123,45,59')
  .replace(/--sarah-blue:\s*#5b9bd5/, '--sarah-blue: #3B7DD8');
// Add dialogue avatar + dark slide accent override
css += `
.dialogue-avatar.sarah{background:#3B7DD8}
.dialogue-avatar.nilo{background:var(--accent)}
.slide-image .accent,.slide-image .accent-bold,.slide-dark .accent,.slide-dark .accent-bold{color:#F0B8C4}
`;

// --- EXTRACT CONTENT FROM ALUNO ---
function extract(html, startMarker, endMarker) {
  const s = html.indexOf(startMarker);
  const e = html.indexOf(endMarker, s);
  if (s === -1 || e === -1) return '';
  return html.substring(s, e + endMarker.length);
}

const preclassContent = extract(aluno, '<div class="tab-content active" id="tab-exercises">', '</div><!-- /tab-exercises -->');
const complementaresContent = extract(aluno, '<div class="tab-content" id="tab-complementary">', '</div><!-- /tab-complementary -->');

// --- EXPANDED AUDIOMAP ---
const audioMap = {
  // Survival phrases
  "Could you repeat that, please?": "/audio/nilo-mesquita-patucci/could_you_repeat_that_please.mp3",
  "I am not sure I understand. Could you explain?": "/audio/nilo-mesquita-patucci/i_am_not_sure_i_understand_could_you_explain.mp3",
  "Let me think about that for a moment.": "/audio/nilo-mesquita-patucci/let_me_think_about_that_for_a_moment.mp3",
  "That is a great question.": "/audio/nilo-mesquita-patucci/that_is_a_great_question.mp3",
  "In my experience, I would say...": "/audio/nilo-mesquita-patucci/in_my_experience_i_would_say.mp3",
  // Vocab words
  "Introduce": "/audio/nilo-mesquita-patucci/introduce.mp3",
  "Represent": "/audio/nilo-mesquita-patucci/represent.mp3",
  "Oversee": "/audio/nilo-mesquita-patucci/oversee.mp3",
  "Compliance": "/audio/nilo-mesquita-patucci/compliance.mp3",
  "Governance": "/audio/nilo-mesquita-patucci/governance.mp3",
  "Background": "/audio/nilo-mesquita-patucci/background.mp3",
  "Currently": "/audio/nilo-mesquita-patucci/currently.mp3",
  "Responsible": "/audio/nilo-mesquita-patucci/responsible.mp3",
  // Vocab example sentences
  "Let me introduce myself. I am Nilo Patucci, Chief Compliance Officer at Corinthians.": "/audio/nilo-mesquita-patucci/let_me_introduce_myself_i_am_nilo_patucci_chief_co.mp3",
  "I represent Brazil in the FIFA Leadership in Football program.": "/audio/nilo-mesquita-patucci/i_represent_brazil_in_the_fifa_leadership_in_footb.mp3",
  "I oversee all compliance and governance operations at the club.": "/audio/nilo-mesquita-patucci/i_oversee_all_compliance_and_governance_operations.mp3",
  "Compliance means following rules and regulations in an organization.": "/audio/nilo-mesquita-patucci/compliance_means_following_rules_and_regulations_i.mp3",
  "Good governance is essential for the future of football.": "/audio/nilo-mesquita-patucci/good_governance_is_essential_for_the_future_of_foo.mp3",
  "My background is in law, specifically labor law and sports law.": "/audio/nilo-mesquita-patucci/my_background_is_in_law_specifically_labor_law_and.mp3",
  "I am currently preparing for the FIFA program in Miami.": "/audio/nilo-mesquita-patucci/i_am_currently_preparing_for_the_fifa_program_in_m.mp3",
  "I am responsible for the entire compliance department at Corinthians.": "/audio/nilo-mesquita-patucci/i_am_responsible_for_the_entire_compliance_departm.mp3",
  // Fill-in data-phrase
  "Let me introduce myself at the FIFA event.": "/audio/nilo-mesquita-patucci/let_me_introduce_myself_at_the_fifa_event.mp3",
  "I represent Brazil as the only delegate in this program.": "/audio/nilo-mesquita-patucci/i_represent_brazil_as_the_only_delegate_in_this_pr.mp3",
  "I am responsible for the governance framework at the club.": "/audio/nilo-mesquita-patucci/i_am_responsible_for_the_governance_framework_at_t.mp3",
  "I oversee the compliance operations at Corinthians.": "/audio/nilo-mesquita-patucci/i_oversee_the_compliance_operations_at_corinthians.mp3",
  "My background includes fifteen years in sports law.": "/audio/nilo-mesquita-patucci/my_background_includes_fifteen_years_in_sports_law.mp3",
  // Ordering
  "[order-l1]": "/audio/nilo-mesquita-patucci/order_l1_ordering.mp3",
  // Speech card phrases
  "I am Nilo Patucci, Chief Compliance Officer at Corinthians.": "/audio/nilo-mesquita-patucci/i_am_nilo_patucci_chief_compliance_officer_at_cori.mp3",
  "I have been working in sports law for over fifteen years.": "/audio/nilo-mesquita-patucci/i_have_been_working_in_sports_law_for_over_fifteen.mp3",
  // Survival card lesson phrases
  "Let me introduce myself.": "/audio/nilo-mesquita-patucci/let_me_introduce_myself.mp3",
  "I am responsible for compliance at Corinthians.": "/audio/nilo-mesquita-patucci/i_am_responsible_for_compliance_at_corinthians.mp3",
  "I represent Brazil in the FIFA program.": "/audio/nilo-mesquita-patucci/i_represent_brazil_in_the_fifa_program.mp3",
  "I have been working in law for over fifteen years.": "/audio/nilo-mesquita-patucci/i_have_been_working_in_law_for_over_fifteen_years.mp3",
  // === IN CLASS DIALOGUE ===
  "Welcome to the FIFA Leadership in Football program! I am Sarah Mitchell, the program coordinator.": "/audio/nilo-mesquita-patucci/welcome_to_the_fifa_leadership_in_football_program.mp3",
  "Thank you! Let me introduce myself. I am Nilo Patucci, Chief Compliance Officer at Corinthians.": "/audio/nilo-mesquita-patucci/thank_you_let_me_introduce_myself_i_am_nilo_patucc.mp3",
  "Corinthians! That is impressive. What is your background in football governance?": "/audio/nilo-mesquita-patucci/corinthians_that_is_impressive_what_is_your_backgr.mp3",
  "I have been working in sports law for over fifteen years. I currently oversee all compliance operations at the club.": "/audio/nilo-mesquita-patucci/i_have_been_working_in_sports_law_for_over_fifteen_i_c.mp3",
  "Fascinating! And you are the only representative from Brazil, correct?": "/audio/nilo-mesquita-patucci/fascinating_and_you_are_the_only_representative_fr.mp3",
  "Yes, I represent Brazil in this program. It is a great honor and responsibility.": "/audio/nilo-mesquita-patucci/yes_i_represent_brazil_in_this_program_it_is_a_gre.mp3",
  "What do you hope to achieve during the program?": "/audio/nilo-mesquita-patucci/what_do_you_hope_to_achieve_during_the_program.mp3",
  "I want to learn from the best practices in governance worldwide and bring that knowledge back to Brazilian football.": "/audio/nilo-mesquita-patucci/i_want_to_learn_from_the_best_practices_in_governa.mp3",
  // === GRAMMAR EXAMPLES ===
  "I work at Corinthians.": "/audio/nilo-mesquita-patucci/i_work_at_corinthians.mp3",
  "He oversees the compliance department.": "/audio/nilo-mesquita-patucci/he_oversees_the_compliance_department.mp3",
  "She represents her country at FIFA.": "/audio/nilo-mesquita-patucci/she_represents_her_country_at_fifa.mp3",
  "I have worked in law for fifteen years.": "/audio/nilo-mesquita-patucci/i_have_worked_in_law_for_fifteen_years.mp3",
  "He has represented Brazil since 2025.": "/audio/nilo-mesquita-patucci/he_has_represented_brazil_since_2025.mp3",
  "She has overseen three major projects.": "/audio/nilo-mesquita-patucci/she_has_overseen_three_major_projects.mp3",
  // === LISTENING 1 ===
  "Good afternoon, everyone. My name is Nilo Patucci. I am the Chief Compliance Officer at Sport Club Corinthians Paulista, based in Sao Paulo, Brazil. I have been working in sports law and governance for over fifteen years. I am currently the only representative from Brazil in the FIFA Leadership in Football program. My background is in labor law and sports law, and I oversee all compliance and governance operations at the club.": "/audio/nilo-mesquita-patucci/listening1_self_intro.mp3",
  // === LISTENING 2 ===
  "Hello everyone, and welcome to the FIFA Leadership Program reception. My name is Dr. Rebecca Torres. I work with football associations across Latin America on governance and compliance. I have overseen regulatory reforms in three different countries. Currently, I am leading a project on anti-corruption measures in football. I am always excited to meet colleagues who share the same passion for integrity in sport.": "/audio/nilo-mesquita-patucci/listening2_networking.mp3",
};

// --- CURRICULUM TABLE (96 rows) ---
const curriculum = [
  [1,"Who Is Nilo in English?","Present Simple + Present Perfect","Conference role-play","Record 2-min self-intro"],
  [2,"My Professional World","Present Simple for routines","Department description","Write professional bio"],
  [3,"Career Timeline","Present Perfect for experience","Career presentation","Record career summary"],
  [4,"The FIFA Mission","Future forms (will/going to)","Goal-setting discussion","Write 3 professional goals"],
  [5,"First Impressions","Question forms","Networking warm-up","Practice small talk"],
  [6,"My City, My Culture","There is/are + adjectives","City presentation","Record city description"],
  [7,"Compliance Framework","Modal verbs (must/should)","Compliance case study","Define 5 compliance terms"],
  [8,"Sports Governance 101","Passive voice basics","Governance role-play","Read FIFA governance article"],
  [9,"Email Essentials","Formal register markers","Email drafting","Write 2 professional emails"],
  [10,"Phone and Video Calls","Reported speech intro","Call simulation","Record voicemail message"],
  [11,"Block 1 Review","All structures reviewed","Mixed simulation","Review vocabulary journal"],
  [12,"Block 1 Simulation","All Block 1 content","Full networking simulation","Reflection audio"],
  [13,"Opinions That Count","Modal verbs for opinion","Opinion debate","Watch TED Talk + summary"],
  [14,"The Art of Disagreement","Hedging language","Meeting role-play","Write disagreement email"],
  [15,"Meeting Dynamics","Interrupting and turn-taking","Meeting simulation","Listen to meeting podcast"],
  [16,"Presentation Opening","Present Perfect Continuous","Opening statement practice","Draft presentation hook"],
  [17,"Presentation Body","Sequencers and connectors","Structured presentation","Create talk outline"],
  [18,"Presentation Close","Question tags","Q&A simulation","Prepare 5 Q&A responses"],
  [19,"Case Study Discussion","Comparing and contrasting","Case analysis","Read compliance case"],
  [20,"Numbers and Data","Describing trends","Data presentation","Analyze FIFA report"],
  [21,"News and Current Affairs","Past Simple vs Past Continuous","News discussion","Read sports governance news"],
  [22,"Cultural Sensitivity","Would/could for politeness","Cross-cultural scenarios","Research Miami customs"],
  [23,"Block 2 Review","All Block 2 structures","Mixed practice","Vocabulary review"],
  [24,"Block 2 Simulation","All content integrated","Mini conference","Record presentation"],
  [25,"FIFA Program Overview","Future Perfect","Program discussion","Review FIFA agenda"],
  [26,"Networking Mastery","Phrasal verbs","Advanced networking sim","Practice elevator pitch"],
  [27,"Panel Discussion Skills","Complex sentences","Panel simulation","Watch panel discussion"],
  [28,"Debate and Argumentation","Third conditional","Formal debate","Prepare debate points"],
  [29,"Travel English Refresher","Review travel vocabulary","Travel scenarios","Pack a language bag"],
  [30,"American Culture","Idioms and cultural phrases","Cultural scenarios","Research Miami business"],
  [31,"Listening to Accents","Connected speech","Multi-accent listening","Listen to diverse podcasts"],
  [32,"Spontaneous Responses","Fillers and time-buying","Impromptu speaking","Record impromptu responses"],
  [33,"Leadership Language","Advanced modals","Leadership scenarios","Read leadership article"],
  [34,"Mock Presentation 1","All structures","Full 10-min presentation","Review recording"],
  [35,"Pre-Miami Review","All Miami content","Comprehensive review","Final preparation checklist"],
  [36,"Miami Dress Rehearsal","All content","45-min immersion","Final reflection audio"],
  [37,"Miami Debrief","Past tenses review","Experience sharing","Write Miami reflection"],
  [38,"Lessons Learned","Present Perfect for results","Feedback discussion","List 5 lessons learned"],
  [39,"Advanced Compliance","Legal conditionals","Regulatory case study","Read regulatory article"],
  [40,"Legal Terminology","Legal collocations","Legal document analysis","Define 10 legal terms"],
  [41,"Report Writing","Formal writing structures","Report drafting","Write summary report"],
  [42,"Negotiation Basics","Conditional structures","Negotiation role-play","Prepare negotiation strategy"],
  [43,"Conflict Resolution","Diplomatic language","Mediation simulation","Listen to mediation podcast"],
  [44,"Moroccan Context","Wish/if only","Cultural comparison","Research Rabat customs"],
  [45,"Advanced Listening","Accent recognition","Multi-accent exercise","International speakers"],
  [46,"Storytelling in English","Narrative tenses","Story presentation","Prepare professional story"],
  [47,"Pre-Rabat Review","All Rabat content","Comprehensive review","Final preparation"],
  [48,"Rabat Dress Rehearsal","All content","45-min immersion","Reflection audio"],
  [49,"Rabat Debrief","Comparing experiences","Discussion and reflection","Write Rabat reflection"],
  [50,"Anti-corruption Language","Passive voice advanced","Anti-corruption case","Read FCPA article"],
  [51,"Due Diligence","Question formation advanced","Investigation simulation","Review due diligence"],
  [52,"Risk Assessment","Probability language","Risk presentation","Create risk matrix in EN"],
  [53,"Ethics and Integrity","Abstract noun phrases","Ethics debate","Write code of ethics excerpt"],
  [54,"Policy Writing","Formal imperatives","Policy drafting","Draft policy section"],
  [55,"Stakeholder Communication","Reported speech advanced","Board presentation","Write stakeholder update"],
  [56,"Crisis Communication","Stress and intonation","Crisis simulation","Draft crisis statement"],
  [57,"Media Relations","Direct vs indirect speech","Press conference sim","Write press statement"],
  [58,"Whistleblower Protocols","Euphemism and softening","Whistleblower scenario","Review protocol language"],
  [59,"Block 5 Review","All compliance vocab","Mixed practice","Vocabulary consolidation"],
  [60,"Mid-Program Assessment","All structures","Comprehensive assessment","Record progress reflection"],
  [61,"Swiss Business Culture","Cultural comparisons","Swiss scenarios","Research Zurich customs"],
  [62,"Keynote Structure","Discourse markers","Keynote outlining","Create keynote outline"],
  [63,"Visual Aids","Describing visuals","Visual presentation drill","Describe 3 charts in EN"],
  [64,"Audience Engagement","Rhetorical questions","Engagement drill","Practice 5 engagement hooks"],
  [65,"Tough Questions","Deflection and reframing","Q&A battle","Prepare 10 tough Q responses"],
  [66,"Body Language and Presence","Emphasis and pausing","Presence exercises","Record with body focus"],
  [67,"Advanced Modals","Mixed modals","Nuance detection","Identify modal nuances"],
  [68,"Diplomatic Language","Hedging expressions","Diplomatic draft","Rewrite direct to diplomatic"],
  [69,"Mock Keynote 1","All presentation skills","Full 15-min keynote","Review and annotate"],
  [70,"Peer Review","Comparative structures","Peer feedback sim","Write feedback on a talk"],
  [71,"Pre-Zurich Review","All Zurich content","Comprehensive review","Final checklist"],
  [72,"Zurich Dress Rehearsal","All content","45-min immersion","Final reflection"],
  [73,"Zurich Debrief","Summarizing experiences","Full program discussion","Write comprehensive reflection"],
  [74,"Impromptu Speaking","Time-buying strategies","Impromptu drill","Practice impromptu daily"],
  [75,"Advanced Networking","Phrasal verbs advanced","Deep networking sim","Follow up with contact"],
  [76,"Mentoring in English","Advisory language","Mentoring role-play","Prepare mentoring session"],
  [77,"Industry Analysis","Trend language","Industry presentation","Read FIFA trends report"],
  [78,"Comparative Governance","Comparing and contrasting","Cross-sport analysis","Research NBA/NFL governance"],
  [79,"Innovation Language","Future tenses advanced","Innovation pitch","Write innovation proposal"],
  [80,"Sustainability in Sports","Cause and effect language","Sustainability presentation","Read ESG sports article"],
  [81,"Personal Branding","Self-description advanced","Personal brand pitch","Create LinkedIn summary EN"],
  [82,"Cross-functional Communication","Simplification strategies","Cross-team meeting","Explain legal to non-legal"],
  [83,"Block 7 Review","All advanced structures","Mixed production drill","Record spontaneous speech"],
  [84,"Advanced Simulation","All content","Complex multi-party sim","Reflection and goals"],
  [85,"Writing Mastery","Complex sentence structures","Advanced email writing","Write formal proposal"],
  [86,"Speaking Mastery","Connected speech","Speed debate","Record timed responses"],
  [87,"Listening Mastery","Reduction and linking","Native speed comprehension","Listen to fast podcasts"],
  [88,"Vocabulary Integration","Collocations and idioms","Vocabulary auction game","Review all word lists"],
  [89,"Grammar Integration","Error correction drills","Grammar under pressure","Self-correct recording"],
  [90,"Pronunciation Polish","Stress and intonation","Pronunciation clinic","Record and compare"],
  [91,"Capstone Part 1","All skills integrated","20-min keynote delivery","Finalize presentation"],
  [92,"Capstone Part 2","All skills integrated","15-min Q&A session","Review Q&A recording"],
  [93,"Mock Interview","Interview techniques","Press interview sim","Prepare interview responses"],
  [94,"Final Assessment","All competencies","Comprehensive evaluation","Self-assessment reflection"],
  [95,"Reflection and Future Goals","Goal-setting language","Future planning","Write English learning plan"],
  [96,"Graduation","All skills celebration","Final simulation","Record final reflection audio"],
];

function buildCurriculumRows() {
  return curriculum.map(r => `<tr><td>${r[0]}</td><td>${r[1]}</td><td>${r[2]}</td><td>${r[3]}</td><td>${r[4]}</td></tr>`).join('\n');
}

// --- SLIDE BUILDER ---
function S(num, type, phase, teacher, content, bgUrl) {
  const cls = type === 'image' ? 'slide slide-image' : type === 'dark' ? 'slide slide-dark' : 'slide slide-light';
  const active = num === 1 ? ' active' : '';
  const style = bgUrl ? ` style="background-image:url('${bgUrl}')"` : '';
  const dt = ` data-teacher="${teacher.replace(/"/g, '&quot;').replace(/'/g, '&#39;')}"`;
  return `<div class="${cls}${active}" data-slide="${num}" data-phase="${phase}"${dt}${style}>\n  <div class="slide-inner">\n${content}\n  </div>\n</div>`;
}

const SVG_CHECK = '<svg viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></svg>';
const SVG_PLAY = '<svg viewBox="0 0 24 24"><polygon points="6 3 20 12 6 21 6 3"/></svg>';
const SVG_PAUSE = '<svg viewBox="0 0 24 24"><rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/></svg>';
const SVG_BACK = '<svg viewBox="0 0 24 24"><polyline points="11 17 6 12 11 7"/><line x1="6" y1="12" x2="18" y2="12"/></svg>';
const SVG_FWD = '<svg viewBox="0 0 24 24"><polyline points="13 7 18 12 13 17"/><line x1="6" y1="12" x2="18" y2="12"/></svg>';
const SVG_VOL = '<svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 010 7.07"/></svg>';

function vocabCard(word, hint, def, example, iconSvg, gradStart, gradEnd) {
  return `<div class="vocab-card" onclick="revealVocab(this)">
  <div class="card-icon" style="background:linear-gradient(135deg,${gradStart},${gradEnd})">
    ${iconSvg}
    <div class="card-hint">${hint}</div>
  </div>
  <div class="card-body">
    <div class="card-word">${word}</div>
    <div class="card-def">${def}</div>
    <div class="card-example">"${example}"</div>
    <div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('${word}',this)">${SVG_VOL} Listen</button></div>
  </div>
</div>`;
}

function listeningPlayer(id, src) {
  return `<div class="listening-player" id="${id}" data-src="${src}">
  <div class="lp-seekbar" onclick="seekAudio(event,'${id}')"><div class="lp-progress" id="progress-${id}"></div></div>
  <div class="lp-time"><span id="time-current-${id}">0:00</span><span id="time-total-${id}">0:00</span></div>
  <div class="lp-controls">
    <button class="lp-btn" onclick="skipAudio('${id}',-5)">${SVG_BACK}</button>
    <button class="lp-btn lp-play" onclick="togglePlayer('${id}')">${SVG_PLAY}<span class="lp-icon-pause" style="display:none!important">${SVG_PAUSE}</span></button>
    <button class="lp-btn" onclick="skipAudio('${id}',5)">${SVG_FWD}</button>
  </div>
  <div class="lp-label">Speed</div>
  <div class="lp-speed">
    <button class="lp-speed-btn" onclick="setPlayerSpeed('${id}',0.5,this)">0.5x</button>
    <button class="lp-speed-btn" onclick="setPlayerSpeed('${id}',0.75,this)">0.75x</button>
    <button class="lp-speed-btn active" onclick="setPlayerSpeed('${id}',1,this)">1x</button>
    <button class="lp-speed-btn" onclick="setPlayerSpeed('${id}',1.25,this)">1.25x</button>
  </div>
</div>`;
}

// --- BUILD SLIDES ---
const slidesHTML = [
  // CHAPTER 1: The Man Behind the Badge (slides 1-4)
  S(1,'image',1,'Abertura (2 min): Compartilhe a tela. Cumprimente o Nilo normalmente em inglês. Deixe o slide título visível enquanto faz rapport.',`
    <div class="chapter-label">Lesson 1 &mdash; Business English</div>
    <h1 class="slide-title">Who Is<br>Nilo in <span class="accent">English</span>?</h1>
    <p class="slide-subtitle">B1 &mdash; 90 minutes &mdash; Alumni by Better</p>
  `, 'https://images.unsplash.com/photo-1431324155629-1a6deb1dec8d?w=1400&q=80'),

  S(2,'dark',1,'Transição (30 seg): Avance quando estiver pronto para o warm-up.',`
    <div class="chapter-label">Chapter 1</div>
    <h2 class="slide-heading">The Man Behind<br>the <span class="accent">Badge</span></h2>
    <p class="slide-subtitle" style="opacity:.7">Warm-up &amp; Diagnostic</p>
  `),

  S(3,'dark',1,'Warm-up (7 min): NÃO corrija agora. ANOTE mentalmente: vocabulário que ele já usa, estruturas corretas/incorretas, nível de confiança, hesitações. Este diagnóstico guiará as próximas 95 aulas.',`
    <div class="chapter-label">Chapter 1: The Man Behind the Badge</div>
    <h2 class="slide-heading">Let&rsquo;s Talk About <span class="accent">You</span></h2>
    <div class="warm-questions">
      <div class="warm-q">&ldquo;Tell me about yourself as if we just met at a FIFA event in Miami.&rdquo;</div>
      <div class="warm-q">&ldquo;What does a Chief Compliance Officer do, in your own words?&rdquo;</div>
      <div class="warm-q">&ldquo;What is the most exciting thing about the FIFA program?&rdquo;</div>
    </div>
  `),

  S(4,'dark',1,'Diagnóstico profundo (8 min): MOMENTO MAIS IMPORTANTE. Peça ao Nilo que se apresente SEM scaffolding. Observe: registro formal vs informal, uso de present simple/perfect, vocabulário técnico, code-switching. ANOTE os 3 maiores gaps.',`
    <div class="chapter-label">Chapter 1: The Man Behind the Badge</div>
    <h2 class="slide-heading">Your <span class="accent">Moment</span></h2>
    <div class="warm-questions">
      <div class="warm-q">&ldquo;Imagine you are at the FIFA reception in Miami. A delegate from Morocco approaches you: &lsquo;Hi, I am Ahmed. Nice to meet you. Tell me about yourself.&rsquo; &mdash; Respond as if this were real.&rdquo;</div>
    </div>
    <p class="slide-subtitle" style="margin-top:2rem;opacity:.6;font-size:.85rem">No script. No support. Just you and your English.</p>
  `),

  // CHAPTER 2: Packing Words (slides 5-7)
  S(5,'dark',2,'Transição para vocabulário.',`
    <div class="chapter-label">Chapter 2</div>
    <h2 class="slide-heading">Packing <span class="accent">Words</span></h2>
    <p class="slide-subtitle" style="opacity:.7">Click on each card to discover the word</p>
  `),

  S(6,'light',2,'Vocabulário 1 (7 min): Clique em cada card. Para cada palavra: (1) leia a pista, pergunte &ldquo;What word do you think this is?&rdquo;, (2) revele, (3) leia a definição, (4) faça drilling 3x. COMPLIANCE e OVERSEE o Nilo já conhece do dia a dia. Aprofunde: &ldquo;compliance framework&rdquo;, &ldquo;oversee operations&rdquo;.',`
    <div class="chapter-label">Chapter 2: Packing Words</div>
    <h2 class="slide-heading">Key <span class="accent">Vocabulary</span> (1/2)</h2>
    <div class="vocab-grid" id="vocabGrid1">
      ${vocabCard('Introduce','To present yourself or someone','to present yourself or someone to others','Let me introduce myself.','<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5"><path d="M16 21v-2a4 4 0 00-4-4H6a4 4 0 00-4-4v2"/><circle cx="9" cy="7" r="4"/><line x1="19" y1="8" x2="19" y2="14"/><line x1="22" y1="11" x2="16" y2="11"/></svg>','#7B2D3B','#9A4054')}
      ${vocabCard('Represent','To speak or act officially for a group','to speak or act officially for a group or organization','I represent Brazil in the FIFA program.','<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>','#5C3D2E','#7D5A48')}
      ${vocabCard('Oversee','To watch and direct an activity','to watch and direct an activity or a group of workers','I oversee all compliance operations.','<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>','#2C5282','#3B7DD8')}
      ${vocabCard('Compliance','Following rules, laws, and regulations','the act of following rules, laws, and regulations','Compliance is essential for good governance.','<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5"><path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2h11"/></svg>','#1B4D3E','#2D7A5F')}
    </div>
    <div class="vocab-counter" id="vocabCount1">0 / 4 words revealed</div>
  `),

  S(7,'light',2,'Vocabulário 2 (7 min): Mesma dinâmica. BACKGROUND pode confundir (Nilo pode pensar em &ldquo;fundo&rdquo;). CCQ: &ldquo;Does background mean the color behind you, or your education and experience?&rdquo; (education/experience). CURRENTLY: CCQ: &ldquo;Does currently mean always, or right now?&rdquo; (right now).',`
    <div class="chapter-label">Chapter 2: Packing Words</div>
    <h2 class="slide-heading">Key <span class="accent">Vocabulary</span> (2/2)</h2>
    <div class="vocab-grid" id="vocabGrid2">
      ${vocabCard('Governance','The system of directing an organization','the system by which an organization is directed and controlled','Good governance is essential for football.','<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/></svg>','#4A3728','#6B5240')}
      ${vocabCard('Background','Education, experience, and history','a person&rsquo;s education, experience, and professional history','My background is in law and sports law.','<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5"><path d="M2 3h6a4 4 0 014 4v14a3 3 0 00-3-3H2z"/><path d="M22 3h-6a4 4 0 00-4 4v14a3 3 0 013-3h7z"/></svg>','#6B4C3B','#8D6E5D')}
      ${vocabCard('Currently','At the present time; now','at the present time; now','I am currently preparing for Miami.','<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>','#4A5568','#718096')}
      ${vocabCard('Responsible','Having the duty to manage something','having the duty to manage or take care of something','I am responsible for the compliance department.','<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5"><path d="M22 11.08V12a10 10 0 11-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>','#553C7B','#7B5EA7')}
    </div>
    <div class="vocab-counter" id="vocabCount2">0 / 4 words revealed</div>
  `),

  // CHAPTER 3: The Code (slides 8-12)
  S(8,'dark',3,'Transição para gramática.',`
    <div class="chapter-label">Chapter 3</div>
    <h2 class="slide-heading">The <span class="accent">Code</span></h2>
    <p class="slide-subtitle" style="opacity:.7">Grammar Discovery</p>
  `),

  S(9,'light',3,'Gramática Discovery (5 min): NÃO diga a regra primeiro. Mostre os exemplos. Pergunte: &ldquo;What is different between these two groups?&rdquo; Guie o Nilo a descobrir que Present Simple = fatos/rotinas, Present Perfect = experiência/duração. CCQ: &ldquo;If I say I work at Corinthians, is it now or in the past?&rdquo; (now). &ldquo;If I say I have worked for fifteen years, did I start recently?&rdquo; (no).',`
    <div class="chapter-label">Chapter 3: The Code</div>
    <h2 class="slide-heading">What Do These Have in <span class="accent">Common</span>?</h2>
    <div class="grammar-sentences">
      <div class="grammar-sentence">I <strong>work</strong> at Corinthians.</div>
      <div class="grammar-sentence">He <strong>oversees</strong> the compliance department.</div>
      <div class="grammar-sentence" style="margin-top:1rem;padding-top:1rem;border-top:2px dashed var(--border)">I <strong>have worked</strong> in law for fifteen years.</div>
      <div class="grammar-sentence">She <strong>has represented</strong> her country since 2020.</div>
    </div>
    <p style="text-align:center;margin-top:1.5rem;font-style:italic;color:var(--text-dim)">What is the difference between the two groups?</p>
    <div style="text-align:center;margin-top:1rem"><button class="btn-primary" onclick="revealGrammar()">Reveal the Rule</button></div>
    <div class="grammar-table-wrap" id="grammarTable">
      <table class="grammar-table">
        <thead><tr><th>Tense</th><th>Use</th><th>Example</th></tr></thead>
        <tbody>
          <tr><td>Present Simple</td><td>Facts, habits, routines</td><td>I <strong>work</strong> at Corinthians.</td></tr>
          <tr><td>Present Perfect</td><td>Experience, duration, unfinished past</td><td>I <strong>have worked</strong> in law for fifteen years.</td></tr>
        </tbody>
      </table>
    </div>
  `),

  S(10,'light',3,'Erro Comum (3 min): Este é o EXATO erro que o Nilo provavelmente comete. Mostre a versão errada primeiro, pergunte: &ldquo;Can you find the mistake?&rdquo; Depois revele a correção. Drilling da frase correta 3x. Reforce: SINCE + ponto no tempo, FOR + duração.',`
    <div class="chapter-label">Chapter 3: The Code</div>
    <h2 class="slide-heading">Common <span class="accent">Mistake</span></h2>
    <div class="mistake-card">
      <div class="mistake-item mistake-wrong"><div class="mistake-icon"><svg viewBox="0 0 24 24" fill="none" stroke="#dc2626" stroke-width="2.5"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></div>&ldquo;I work in compliance since fifteen years.&rdquo;</div>
      <div class="mistake-item mistake-right"><div class="mistake-icon"><svg viewBox="0 0 24 24" fill="none" stroke="#16a34a" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg></div>&ldquo;I have been working in compliance for fifteen years.&rdquo;</div>
    </div>
    <p style="text-align:center;margin-top:1.5rem;font-size:.9rem;color:var(--text-dim)"><strong>since</strong> + point in time (since 2010) &nbsp;&bull;&nbsp; <strong>for</strong> + duration (for fifteen years)</p>
  `),

  S(11,'light',3,'Prática Gramatical (5 min): Para cada frase, peça ao Nilo que complete ORALMENTE antes de revelar. Se errar, pergunte: &ldquo;Is this a fact or an experience over time?&rdquo; Obstáculo previsto: frase 3 (&ldquo;have represented&rdquo; particípio irregular).',`
    <div class="chapter-label">Chapter 3: The Code</div>
    <h2 class="slide-heading">Grammar <span class="accent">Practice</span></h2>
    <div class="fill-grid">
      <div class="fill-item" onclick="revealFill(this)"><div class="fill-text">I <span class="fill-blank">___</span><span class="fill-answer">have worked</span> at Corinthians since 2020.</div></div>
      <div class="fill-item" onclick="revealFill(this)"><div class="fill-text">She <span class="fill-blank">___</span><span class="fill-answer">oversees</span> the program every year.</div></div>
      <div class="fill-item" onclick="revealFill(this)"><div class="fill-text">They <span class="fill-blank">___</span><span class="fill-answer">have represented</span> their countries since the program started.</div></div>
      <div class="fill-item" onclick="revealFill(this)"><div class="fill-text">He currently <span class="fill-blank">___</span><span class="fill-answer">manages</span> the legal department.</div></div>
    </div>
  `),

  S(12,'light',3,'CCQs extras (2 min): &ldquo;If someone says I have overseen three projects, how many projects?&rdquo; (three). &ldquo;Is this finished or still possible to do more?&rdquo; (still possible). &ldquo;Can I use since with for fifteen years?&rdquo; (no, since + point in time, for + duration).',`
    <div class="chapter-label">Chapter 3: The Code</div>
    <h2 class="slide-heading">Quick <span class="accent">Check</span></h2>
    <div class="comp-questions">
      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">1. &ldquo;I have overseen three projects.&rdquo; &mdash; Is this finished forever, or can there be more projects?</div><div class="q-answer">There can be more projects. Present Perfect connects past to now.</div></div>
      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">2. Which is correct: &ldquo;I work here since 2010&rdquo; or &ldquo;I have worked here since 2010&rdquo;?</div><div class="q-answer">&ldquo;I have worked here since 2010.&rdquo; (since + point in time = Present Perfect)</div></div>
      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">3. &ldquo;He oversees the department.&rdquo; &mdash; Is this a fact or an experience?</div><div class="q-answer">A fact about his current role. Present Simple for permanent facts.</div></div>
    </div>
  `),

  // CHAPTER 4: Getting There (slides 13-19)
  S(13,'dark',4,'Transição para contexto.',`
    <div class="chapter-label">Chapter 4</div>
    <h2 class="slide-heading">Getting <span class="accent">There</span></h2>
    <p class="slide-subtitle" style="opacity:.7">Context, Listening &amp; Dialogue</p>
  `),

  S(14,'light',4,'Artefato (5 min): Leia o email juntos. Peça ao Nilo que identifique as 8 palavras do vocabulário no texto. Comprehension oral antes de revelar respostas.',`
    <div class="chapter-label">Chapter 4: Getting There</div>
    <h2 class="slide-heading">A Special <span class="accent">Email</span></h2>
    <div class="email-card">
      <div class="email-header">
        <div class="email-field"><strong>From:</strong> programs@fifa.org</div>
        <div class="email-field"><strong>To:</strong> nilo.patucci@corinthians.com.br</div>
        <div class="email-field"><strong>Subject:</strong> Confirmation &mdash; FIFA Leadership in Football Program</div>
      </div>
      <div class="email-body-ic">
        <p>Dear Mr. Patucci,</p>
        <p>We are pleased to confirm your participation in the <strong>FIFA Leadership in Football</strong> program. You have been selected to <strong>represent</strong> Brazil as the only delegate from your country.</p>
        <p>Your <strong>background</strong> in sports law and <strong>compliance</strong> makes you an ideal candidate. As Chief Compliance Officer, you <strong>currently</strong> <strong>oversee</strong> <strong>governance</strong> operations at one of South America&rsquo;s largest football clubs.</p>
        <p>The program will take place in Miami (October 2025), Rabat (December 2025), and Zurich (March 2026). You are <strong>responsible</strong> for arranging your travel.</p>
        <p>We look forward to welcoming you. Please do not hesitate to <strong>introduce</strong> yourself to other delegates before the program begins.</p>
        <p>Best regards,<br>Sarah Mitchell<br>Program Coordinator, FIFA</p>
      </div>
    </div>
  `),

  S(15,'light',4,'Comprehensão do email (3 min): Clique em cada pergunta. Peça resposta ORAL completa antes de revelar.',`
    <div class="chapter-label">Chapter 4: Getting There</div>
    <h2 class="slide-heading">Email <span class="accent">Comprehension</span></h2>
    <div class="comp-questions">
      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">1. What program has Nilo been confirmed for?</div><div class="q-answer">The FIFA Leadership in Football program.</div></div>
      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">2. How many cities will the program visit?</div><div class="q-answer">Three: Miami, Rabat, and Zurich.</div></div>
      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">3. Why was Nilo selected?</div><div class="q-answer">His background in sports law and compliance, and his role as CCO at Corinthians.</div></div>
    </div>
  `),

  S(16,'dark',4,'Listening 1 (5 min): Toque o áudio SEM texto na tela. Nilo ouve a si mesmo (voz Ash, masculina). Depois de terminar, revele as perguntas. Se Nilo pedir para ler, diga: &ldquo;Let us listen first. You will see the questions after.&rdquo;',`
    <div class="chapter-label">Chapter 4: Getting There</div>
    <h2 class="slide-heading" style="text-align:center">Listen to This <span class="accent">Introduction</span></h2>
    <p style="text-align:center;color:rgba(255,255,255,.7);margin-bottom:1.5rem">Listen carefully. Questions will appear after the audio ends.</p>
    ${listeningPlayer('lp-listen1','/audio/nilo-mesquita-patucci/listening1_self_intro.mp3')}
    <div class="comp-questions" id="questions-lp-listen1" style="display:none">
      <div class="comp-q" onclick="revealComp(this)" style="background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.15)"><div class="q-text" style="color:rgba(255,255,255,.9)">1. What is the speaker&rsquo;s name and role?</div><div class="q-answer" style="color:#F0B8C4">Nilo Patucci, Chief Compliance Officer at Corinthians.</div></div>
      <div class="comp-q" onclick="revealComp(this)" style="background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.15)"><div class="q-text" style="color:rgba(255,255,255,.9)">2. How long has he been working in sports law?</div><div class="q-answer" style="color:#F0B8C4">Over fifteen years.</div></div>
      <div class="comp-q" onclick="revealComp(this)" style="background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.15)"><div class="q-text" style="color:rgba(255,255,255,.9)">3. What does he oversee?</div><div class="q-answer" style="color:#F0B8C4">All compliance and governance operations at the club.</div></div>
    </div>
  `),

  S(17,'dark',4,'Diálogo (10 min): Clique &ldquo;Next Line&rdquo; para cada troca. Fase 1: ouçam juntos. Fase 2: Nilo lê suas falas, professor lê Sarah. Fase 3: invertem papéis. Vocabulário em negrito, pause para drilling rápido.',`
    <div class="chapter-label">Chapter 4: Getting There</div>
    <h2 class="slide-heading" style="text-align:center">FIFA Reception <span class="accent">Dialogue</span></h2>
    <div class="dialogue-box" id="dialogueBox">
      <div class="dialogue-line visible" data-line="1" data-voice="riley"><div class="dialogue-avatar sarah">S</div><div class="dialogue-bubble dr-bubble">Welcome to the FIFA Leadership in Football program! I am Sarah Mitchell, the program coordinator.<span class="audio-inline" onclick="speakText('Welcome to the FIFA Leadership in Football program! I am Sarah Mitchell, the program coordinator.',this)">${SVG_VOL}</span></div></div>
      <div class="dialogue-line" data-line="2" data-voice="ash"><div class="dialogue-avatar nilo">N</div><div class="dialogue-bubble patricia-bubble">Thank you! Let me <span class="vocab-highlight">introduce</span> myself. I am Nilo Patucci, Chief <span class="vocab-highlight">Compliance</span> Officer at Corinthians.<span class="audio-inline" onclick="speakText('Thank you! Let me introduce myself. I am Nilo Patucci, Chief Compliance Officer at Corinthians.',this)">${SVG_VOL}</span></div></div>
      <div class="dialogue-line" data-line="3" data-voice="riley"><div class="dialogue-avatar sarah">S</div><div class="dialogue-bubble dr-bubble">Corinthians! That is impressive. What is your <span class="vocab-highlight">background</span> in football <span class="vocab-highlight">governance</span>?<span class="audio-inline" onclick="speakText('Corinthians! That is impressive. What is your background in football governance?',this)">${SVG_VOL}</span></div></div>
      <div class="dialogue-line" data-line="4" data-voice="ash"><div class="dialogue-avatar nilo">N</div><div class="dialogue-bubble patricia-bubble">I have been working in sports law for over fifteen years. I <span class="vocab-highlight">currently</span> <span class="vocab-highlight">oversee</span> all compliance operations at the club.<span class="audio-inline" onclick="speakText('I have been working in sports law for over fifteen years. I currently oversee all compliance operations at the club.',this)">${SVG_VOL}</span></div></div>
      <div class="dialogue-line" data-line="5" data-voice="riley"><div class="dialogue-avatar sarah">S</div><div class="dialogue-bubble dr-bubble">Fascinating! And you are the only <span class="vocab-highlight">represent</span>ative from Brazil, correct?<span class="audio-inline" onclick="speakText('Fascinating! And you are the only representative from Brazil, correct?',this)">${SVG_VOL}</span></div></div>
      <div class="dialogue-line" data-line="6" data-voice="ash"><div class="dialogue-avatar nilo">N</div><div class="dialogue-bubble patricia-bubble">Yes, I <span class="vocab-highlight">represent</span> Brazil in this program. It is a great honor and <span class="vocab-highlight">responsible</span>ility.<span class="audio-inline" onclick="speakText('Yes, I represent Brazil in this program. It is a great honor and responsibility.',this)">${SVG_VOL}</span></div></div>
      <div class="dialogue-line" data-line="7" data-voice="riley"><div class="dialogue-avatar sarah">S</div><div class="dialogue-bubble dr-bubble">What do you hope to achieve during the program?<span class="audio-inline" onclick="speakText('What do you hope to achieve during the program?',this)">${SVG_VOL}</span></div></div>
      <div class="dialogue-line" data-line="8" data-voice="ash"><div class="dialogue-avatar nilo">N</div><div class="dialogue-bubble patricia-bubble">I want to learn from the best practices in <span class="vocab-highlight">governance</span> worldwide and bring that knowledge back to Brazilian football.<span class="audio-inline" onclick="speakText('I want to learn from the best practices in governance worldwide and bring that knowledge back to Brazilian football.',this)">${SVG_VOL}</span></div></div>
    </div>
    <button class="btn-primary" id="nextLineBtn" onclick="nextDialogueLine()">Next Line</button>
  `),

  S(18,'light',4,'Comprehensão do diálogo (3 min): Perguntas sobre a SARAH (interlocutor), NÃO sobre o Nilo.',`
    <div class="chapter-label">Chapter 4: Getting There</div>
    <h2 class="slide-heading">Dialogue <span class="accent">Comprehension</span></h2>
    <div class="comp-questions">
      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">1. What is Sarah Mitchell&rsquo;s role?</div><div class="q-answer">She is the program coordinator at FIFA.</div></div>
      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">2. What did Sarah ask about Nilo&rsquo;s background?</div><div class="q-answer">She asked about his background in football governance.</div></div>
      <div class="comp-q" onclick="revealComp(this)"><div class="q-text">3. What word did Sarah use that means &ldquo;amazing&rdquo;?</div><div class="q-answer">Fascinating.</div></div>
    </div>
  `),

  S(19,'dark',4,'Listening 2 (5 min): Áudio com VOZ FEMININA (Riley). Nilo ouve sem texto. Depois perguntas. Este listening tem conteúdo diferente (outra delegada se apresentando). Simula ambiente multicultural da FIFA.',`
    <div class="chapter-label">Chapter 4: Getting There</div>
    <h2 class="slide-heading" style="text-align:center">Another <span class="accent">Introduction</span></h2>
    <p style="text-align:center;color:rgba(255,255,255,.7);margin-bottom:1.5rem">Listen to another delegate at the reception.</p>
    ${listeningPlayer('lp-listen2','/audio/nilo-mesquita-patucci/listening2_networking.mp3')}
    <div class="comp-questions" id="questions-lp-listen2" style="display:none">
      <div class="comp-q" onclick="revealComp(this)" style="background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.15)"><div class="q-text" style="color:rgba(255,255,255,.9)">1. What is the speaker&rsquo;s name?</div><div class="q-answer" style="color:#F0B8C4">Dr. Rebecca Torres.</div></div>
      <div class="comp-q" onclick="revealComp(this)" style="background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.15)"><div class="q-text" style="color:rgba(255,255,255,.9)">2. How many countries has she worked in?</div><div class="q-answer" style="color:#F0B8C4">Three countries.</div></div>
      <div class="comp-q" onclick="revealComp(this)" style="background:rgba(255,255,255,.08);border-color:rgba(255,255,255,.15)"><div class="q-text" style="color:rgba(255,255,255,.9)">3. What is she currently leading?</div><div class="q-answer" style="color:#F0B8C4">A project on anti-corruption measures in football.</div></div>
    </div>
  `),

  // CHAPTER 5: Practice (slides 20-26)
  S(20,'dark',5,'Transição para prática.',`
    <div class="chapter-label">Chapter 5</div>
    <h2 class="slide-heading"><span class="accent">Practice</span></h2>
    <p class="slide-subtitle" style="opacity:.7">Quick Fire, Spot the Error &amp; Oral Drilling</p>
  `),

  S(21,'light',5,'Quick Fire (8 min): Uma situação por vez. Nilo responde ORALMENTE, depois clica &ldquo;Show Answer&rdquo; para comparar. Não é para acertar palavra por palavra, é para produzir sob pressão leve.',`
    <div class="chapter-label">Chapter 5: Practice</div>
    <h2 class="slide-heading">Quick <span class="accent">Fire</span></h2>
    <div style="position:relative">
      <div class="challenge-score" id="challengeScore">0 / 6</div>
      <div class="challenge-card" id="challengeCard">
        <div class="challenge-counter" id="challengeCounter">Question 1 of 6</div>
        <div class="challenge-prompt" id="challengePrompt">A FIFA delegate asks: &ldquo;What do you do?&rdquo; Introduce yourself professionally.</div>
        <div class="challenge-answer" id="challengeAnswer">&ldquo;I am Nilo Patucci, Chief Compliance Officer at Corinthians. I am responsible for governance and compliance.&rdquo;</div>
        <button class="btn-primary" id="showAnswerBtn" onclick="showChallengeAnswer()">Show Answer</button>
        <button class="btn-secondary" id="nextChallengeBtn" onclick="nextChallenge()" style="display:none">Next Question</button>
      </div>
    </div>
  `),

  S(22,'light',5,'Spot the Error (5 min): Nilo lê cada frase e identifica o erro ANTES de clicar. Se não encontrar, dê pista: &ldquo;Is this present simple or present perfect? Should it be?&rdquo; Obstáculo: frase 4 (&ldquo;have overseen&rdquo; particípio irregular).',`
    <div class="chapter-label">Chapter 5: Practice</div>
    <h2 class="slide-heading">Spot the <span class="accent">Error</span></h2>
    <div class="error-grid">
      <div class="error-card" onclick="revealError(this)"><div class="error-sentence">&ldquo;I work in the compliance since fifteen years.&rdquo;</div><div class="error-fix">&ldquo;I have been working in compliance for fifteen years.&rdquo;</div></div>
      <div class="error-card" onclick="revealError(this)"><div class="error-sentence">&ldquo;I am represent Brazil in this program.&rdquo;</div><div class="error-fix">&ldquo;I represent Brazil in this program.&rdquo;</div></div>
      <div class="error-card" onclick="revealError(this)"><div class="error-sentence">&ldquo;My background is on law and football.&rdquo;</div><div class="error-fix">&ldquo;My background is in law and football.&rdquo;</div></div>
      <div class="error-card" onclick="revealError(this)"><div class="error-sentence">&ldquo;I oversee the compliance since I arrived.&rdquo;</div><div class="error-fix">&ldquo;I have overseen compliance since I arrived.&rdquo;</div></div>
    </div>
    <div class="error-score" id="errorScore">0 / 4 errors found</div>
  `),

  S(23,'light',5,'Oral Drilling 1 (5 min): Leia cada situação. Nilo responde ORALMENTE com frase completa. Depois revele o modelo. Se a resposta for diferente mas correta, valide. Só corrija se a estrutura estiver errada.',`
    <div class="chapter-label">Chapter 5: Practice</div>
    <h2 class="slide-heading">Oral <span class="accent">Drilling</span> (1/2)</h2>
    <div class="oral-grid">
      <div class="oral-item" onclick="this.classList.toggle('revealed')"><div class="oral-situation">1. Someone asks: &ldquo;What is your name and what do you do?&rdquo;</div><div class="oral-model">&ldquo;I am Nilo Patucci. I am the Chief Compliance Officer at Corinthians.&rdquo;</div></div>
      <div class="oral-item" onclick="this.classList.toggle('revealed')"><div class="oral-situation">2. A delegate asks: &ldquo;How long have you been in this field?&rdquo;</div><div class="oral-model">&ldquo;I have been working in sports law for over fifteen years.&rdquo;</div></div>
      <div class="oral-item" onclick="this.classList.toggle('revealed')"><div class="oral-situation">3. Someone asks: &ldquo;What exactly do you do at Corinthians?&rdquo;</div><div class="oral-model">&ldquo;I oversee all compliance and governance operations at the club.&rdquo;</div></div>
    </div>
  `),

  S(24,'light',5,'Oral Drilling 2 (5 min): Mesma dinâmica. Situações mais complexas exigindo frases mais longas.',`
    <div class="chapter-label">Chapter 5: Practice</div>
    <h2 class="slide-heading">Oral <span class="accent">Drilling</span> (2/2)</h2>
    <div class="oral-grid">
      <div class="oral-item" onclick="this.classList.toggle('revealed')"><div class="oral-situation">4. Tell the group about your background.</div><div class="oral-model">&ldquo;My background is in labor law and sports law. I have worked in the legal field for over fifteen years.&rdquo;</div></div>
      <div class="oral-item" onclick="this.classList.toggle('revealed')"><div class="oral-situation">5. Explain why you are in the FIFA program.</div><div class="oral-model">&ldquo;I represent Brazil as the only delegate. I want to learn from the best practices in governance worldwide.&rdquo;</div></div>
      <div class="oral-item" onclick="this.classList.toggle('revealed')"><div class="oral-situation">6. Describe your current focus at work.</div><div class="oral-model">&ldquo;I am currently preparing for the FIFA Leadership Program. I am responsible for the entire compliance department.&rdquo;</div></div>
    </div>
  `),

  S(25,'light',5,'Sentence Building (5 min): Nilo monta as frases oralmente.',`
    <div class="chapter-label">Chapter 5: Practice</div>
    <h2 class="slide-heading">Sentence <span class="accent">Building</span></h2>
    <div class="oral-grid">
      <div class="oral-item" onclick="this.classList.toggle('revealed')"><div class="oral-situation">compliance / oversee / I / at / the / operations / club</div><div class="oral-model">&ldquo;I oversee the compliance operations at the club.&rdquo;</div></div>
      <div class="oral-item" onclick="this.classList.toggle('revealed')"><div class="oral-situation">fifteen / in / have / I / law / for / worked / years</div><div class="oral-model">&ldquo;I have worked in law for fifteen years.&rdquo;</div></div>
      <div class="oral-item" onclick="this.classList.toggle('revealed')"><div class="oral-situation">Brazil / the / represent / in / I / program / FIFA</div><div class="oral-model">&ldquo;I represent Brazil in the FIFA program.&rdquo;</div></div>
      <div class="oral-item" onclick="this.classList.toggle('revealed')"><div class="oral-situation">currently / for / am / I / preparing / Miami</div><div class="oral-model">&ldquo;I am currently preparing for Miami.&rdquo;</div></div>
      <div class="oral-item" onclick="this.classList.toggle('revealed')"><div class="oral-situation">responsible / department / the / compliance / am / for / I</div><div class="oral-model">&ldquo;I am responsible for the compliance department.&rdquo;</div></div>
    </div>
  `),

  S(26,'light',5,'Pronúncia (5 min): Foque nas palavras que o Nilo mais errou no drilling. Drilling de &ldquo;compliance&rdquo; (com-PLI-ance), &ldquo;governance&rdquo; (GOV-er-nance), &ldquo;responsible&rdquo; (re-SPON-si-ble). Peça 3x cada.',`
    <div class="chapter-label">Chapter 5: Practice</div>
    <h2 class="slide-heading">Pronunciation <span class="accent">Focus</span></h2>
    <div class="oral-grid">
      <div class="oral-item" style="cursor:default"><div class="oral-situation" style="font-size:1.2rem;text-align:center"><strong>com</strong>&middot;PLI&middot;ance<br><button class="audio-btn-sm" onclick="speakText('Compliance',this)" style="margin-top:.5rem">${SVG_VOL} Listen</button></div></div>
      <div class="oral-item" style="cursor:default"><div class="oral-situation" style="font-size:1.2rem;text-align:center"><strong>GOV</strong>&middot;er&middot;nance<br><button class="audio-btn-sm" onclick="speakText('Governance',this)" style="margin-top:.5rem">${SVG_VOL} Listen</button></div></div>
      <div class="oral-item" style="cursor:default"><div class="oral-situation" style="font-size:1.2rem;text-align:center">re&middot;<strong>SPON</strong>&middot;si&middot;ble<br><button class="audio-btn-sm" onclick="speakText('Responsible',this)" style="margin-top:.5rem">${SVG_VOL} Listen</button></div></div>
      <div class="oral-item" style="cursor:default"><div class="oral-situation" style="font-size:1.2rem;text-align:center"><strong>IN</strong>&middot;tro&middot;duce<br><button class="audio-btn-sm" onclick="speakText('Introduce',this)" style="margin-top:.5rem">${SVG_VOL} Listen</button></div></div>
    </div>
  `),

  // CHAPTER 6: Your Turn (slides 27-32)
  S(27,'dark',6,'Transição para produção.',`
    <div class="chapter-label">Chapter 6</div>
    <h2 class="slide-heading">Your <span class="accent">Turn</span></h2>
    <p class="slide-subtitle" style="opacity:.7">From Guided to Free</p>
  `),

  S(28,'dark',6,'Role-play Guiado (5 min): Nilo se apresenta usando keywords como apoio. Professor faz papel do delegate marroquino. Observe se Nilo usa as 8 palavras do vocabulário. NÃO corrija durante, anote erros para delayed feedback.',`
    <div class="chapter-label">Chapter 6: Your Turn</div>
    <h2 class="slide-heading">Role-play: <span class="accent">Guided</span></h2>
    <div class="roleplay-card">
      <div class="card-icon" style="background:linear-gradient(135deg,#7B2D3B,#9A4054);height:80px;display:flex;align-items:center;justify-content:center;border-radius:14px 14px 0 0"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" style="width:40px;height:40px"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4-4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/></svg></div>
      <div class="roleplay-body">
        <div class="roleplay-scenario">You are at the FIFA Leadership Program welcome reception in Miami. A delegate from Morocco approaches you. Introduce yourself using your name, role, organization, background, and current mission.</div>
        <div class="roleplay-keywords"><span class="roleplay-kw">Nilo Patucci</span><span class="roleplay-kw">Corinthians</span><span class="roleplay-kw">compliance</span><span class="roleplay-kw">governance</span><span class="roleplay-kw">fifteen years</span><span class="roleplay-kw">Brazil</span></div>
      </div>
    </div>
  `),

  S(29,'dark',6,'Role-play Semi-livre (5 min): Menos apoio. Nilo explica seu trabalho no Corinthians. Professor faz delegate curioso. Obstáculo previsto: Nilo pode reverter ao inglês informal quando sai do script, anote para feedback.',`
    <div class="chapter-label">Chapter 6: Your Turn</div>
    <h2 class="slide-heading">Role-play: <span class="accent">Semi-free</span></h2>
    <div class="roleplay-card">
      <div class="card-icon" style="background:linear-gradient(135deg,#4A3728,#6B5240);height:80px;display:flex;align-items:center;justify-content:center;border-radius:14px 14px 0 0"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" style="width:40px;height:40px"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/></svg></div>
      <div class="roleplay-body">
        <div class="roleplay-scenario">You are at a coffee break during the program. Another delegate asks about your work at Corinthians. Explain your responsibilities and what makes your role unique.</div>
        <div class="roleplay-keywords"><span class="roleplay-kw">oversee</span><span class="roleplay-kw">responsible</span><span class="roleplay-kw">represent</span></div>
      </div>
    </div>
  `),

  S(30,'dark',6,'Role-play Livre (5 min): ZERO apoio na tela. Nilo conversa livremente com &ldquo;FIFA official&rdquo;. NÃO corrija durante a produção. Tome notas dos erros para o próximo slide.',`
    <div class="chapter-label">Chapter 6: Your Turn</div>
    <h2 class="slide-heading">Role-play: <span class="accent">Free</span></h2>
    <div class="roleplay-card">
      <div class="card-icon" style="background:linear-gradient(135deg,#2C5282,#3B7DD8);height:80px;display:flex;align-items:center;justify-content:center;border-radius:14px 14px 0 0"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5" style="width:40px;height:40px"><circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15.3 15.3 0 014 10 15.3 15.3 0 01-4 10 15.3 15.3 0 01-4-10 15.3 15.3 0 014-10z"/></svg></div>
      <div class="roleplay-body">
        <div class="roleplay-scenario">You are at the final dinner of the Miami session. A senior FIFA official asks you to tell them about yourself and your vision for compliance in Brazilian football. Speak freely for 2 minutes. No keywords. No script. Just you.</div>
      </div>
    </div>
  `),

  S(31,'light',6,'Delayed Error Correction (5 min): Compartilhe 3-5 erros que você anotou durante a produção livre. Para cada: o que Nilo disse, o que deveria ter dito. Peça que repita a versão correta 2x. Foque nos erros de ESTRUTURA (present simple vs perfect), não de vocabulário.',`
    <div class="chapter-label">Chapter 6: Your Turn</div>
    <h2 class="slide-heading">Error <span class="accent">Correction</span></h2>
    <p style="font-size:.9rem;color:var(--text-dim);margin-bottom:1rem">Teacher: type the errors you observed during the free role-play below.</p>
    <div style="background:#fff;border:2px solid var(--border);border-radius:10px;padding:1.5rem;min-height:200px" contenteditable="true">
      <p style="color:var(--text-dim);font-style:italic">Click here and type the errors observed...</p>
    </div>
  `),

  S(32,'dark',6,'Produção Livre (5 min): Nilo grava áudio de 2 minutos se apresentando. Esta gravação será comparada com a da Aula 48 para mostrar evolução.',`
    <div class="chapter-label">Chapter 6: Your Turn</div>
    <h2 class="slide-heading" style="text-align:center">Record Your <span class="accent">Introduction</span></h2>
    <div class="record-card">
      <div class="record-prompt">Record a 2-minute self-introduction. Use all 8 vocabulary words. This recording will be compared with your Lesson 48 recording to show your progress.</div>
      <button class="record-btn" onclick="toggleReflectionRecord(this)"><svg viewBox="0 0 24 24"><path d="M12 1a3 3 0 00-3 3v8a3 3 0 006 0V4a3 3 0 00-3-3z" fill="#fff"/><path d="M19 10v2a7 7 0 01-14 0v-2" fill="none" stroke="#fff" stroke-width="2"/><line x1="12" y1="19" x2="12" y2="23" stroke="#fff" stroke-width="2"/></svg></button>
      <div id="reflectionResult"></div>
    </div>
  `),

  // CHAPTER 7: Wrap-up (slides 33-37)
  S(33,'dark',7,'Transição para encerramento.',`
    <div class="chapter-label">Chapter 7</div>
    <h2 class="slide-heading"><span class="accent">Wrap</span>-up</h2>
    <p class="slide-subtitle" style="opacity:.7">What You Learned Today</p>
  `),

  S(34,'light',7,'Checklist (3 min): Leia cada item. Pergunte: &ldquo;Can you say yes to this?&rdquo; Se sim, clique o checkbox juntos. Se não, marque para revisão na próxima aula.',`
    <div class="chapter-label">Self-Assessment</div>
    <h2 class="slide-heading">What I <span class="accent">Learned</span></h2>
    <div class="check-grid" id="checkGrid">
      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box">${SVG_CHECK}</div><span>I can introduce myself professionally in English.</span></div>
      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box">${SVG_CHECK}</div><span>I know 8 words related to compliance and governance.</span></div>
      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box">${SVG_CHECK}</div><span>I can use Present Simple for facts and current roles.</span></div>
      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box">${SVG_CHECK}</div><span>I can use Present Perfect for experience and duration.</span></div>
      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box">${SVG_CHECK}</div><span>I can read and understand a formal FIFA email.</span></div>
      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box">${SVG_CHECK}</div><span>I can have a basic networking conversation.</span></div>
      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box">${SVG_CHECK}</div><span>I can describe my background and current position.</span></div>
      <div class="check-item" onclick="toggleCheck(this)"><div class="check-box">${SVG_CHECK}</div><span>I feel more confident about the FIFA program in English.</span></div>
    </div>
  `),

  S(35,'dark',7,'Celebração (1 min): Valide o progresso. Diga: &ldquo;Day 1 is done. You already have the content. We are going to give it the right suit.&rdquo;',`
    <div class="badge-card">
      <div class="badge-icon">
        <div class="badge-circle"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" style="width:48px;height:48px"><path d="M12 15l-3 3 1 4 2-1 2 1 1-4-3-3z"/><circle cx="12" cy="8" r="7"/></svg></div>
        <div class="sparkles"><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div></div>
      </div>
      <h2 style="color:#fff;font-family:'Cormorant Garamond',serif;font-size:2rem">Aula 1 Complete!</h2>
      <p style="color:rgba(255,255,255,.7);margin-top:.5rem">You already have the content. We are going to give it the right suit.</p>
    </div>
  `),

  S(36,'dark',7,'Preview (2 min): &ldquo;Next class: My Professional World, we will practice describing your role and organization in detail.&rdquo; Homework (diga ORALMENTE): 1) Gravar áudio de 2 minutos se apresentando. 2) Ouvir podcast Compliance Perspectives, 1 episódio. 3) Anotar 3 situações do dia a dia no Corinthians onde usou inglês.',`
    <div class="chapter-label">Next Lesson Preview</div>
    <h2 class="slide-heading">Coming <span class="accent">Next</span></h2>
    <p class="slide-subtitle" style="margin-top:1rem;opacity:.8">Aula 2: My Professional World &mdash; Describing Your Role &amp; Organization</p>
    <p class="slide-subtitle" style="opacity:.5;font-size:.85rem;margin-top:1rem">Homework is given orally by the teacher.</p>
  `),

  S(37,'image',7,'Encerramento (1 min): Slide final. Diga: &ldquo;Great first class, Nilo. See you next time.&rdquo;',`
    <div class="chapter-label">Lesson Complete</div>
    <h2 class="slide-title">Day 1 &mdash; <span class="accent">Complete.</span></h2>
    <p class="slide-subtitle" style="opacity:.8;margin-top:1rem">Next lesson: My Professional World &mdash; Describing Your Role &amp; Organization</p>
  `,'https://images.unsplash.com/photo-1431324155629-1a6deb1dec8d?w=1400&q=80'),
].join('\n\n');

// --- EXTRACT JS FROM TEMPLATE ---
// Find the main script block
const jsStart = tmpl.indexOf('// ===== TAB SWITCHING');
const jsEnd = tmpl.indexOf('<\/script>\n<script src="/lib/lesson-progress.js">', jsStart);
let jsBlock = tmpl.substring(jsStart, jsEnd);

// Replace student-specific values
jsBlock = jsBlock
  .replace(/patricia-ruffo/g, 'nilo-mesquita-patucci')
  .replace(/totalSlides\s*=\s*\d+/, 'totalSlides = 37')
  .replace(/totalLessons\s*=\s*\d+/, 'totalLessons = 1')
  .replace(/slidePhases\s*=\s*\{[^}]*\}/, 'slidePhases = {1:1,2:1,3:1,4:1,5:2,6:2,7:2,8:3,9:3,10:3,11:3,12:3,13:4,14:4,15:4,16:4,17:4,18:4,19:4,20:5,21:5,22:5,23:5,24:5,25:5,26:5,27:6,28:6,29:6,30:6,31:6,32:6,33:7,34:7,35:7,36:7,37:7}')
  .replace(/#2D6A4F/g, '#7B2D3B').replace(/#40916C/g, '#9A4054');

// Replace challenges array
const challengesData = [
  {prompt:"A FIFA delegate asks: 'What do you do?' Introduce yourself professionally.",answer:'"I am Nilo Patucci, Chief Compliance Officer at Corinthians. I am responsible for governance and compliance."'},
  {prompt:"Someone asks: 'How long have you been in sports law?' Answer using present perfect.",answer:'"I have been working in sports law for over fifteen years."'},
  {prompt:"A coordinator asks about your role. Describe what you oversee.",answer:'"I oversee all compliance and governance operations at the club."'},
  {prompt:"A delegate asks about your background. Tell them.",answer:'"My background is in labor law and sports law. I have worked with Corinthians for several years."'},
  {prompt:"Someone asks why you are in the FIFA program. Explain.",answer:'"I represent Brazil as the only delegate. I want to learn best practices in football governance."'},
  {prompt:"Describe your current focus in one sentence.",answer:'"I am currently preparing for the FIFA Leadership Program events in Miami, Rabat, and Zurich."'},
];
const challengesJS = 'var challenges = ' + JSON.stringify(challengesData) + ';';
jsBlock = jsBlock.replace(/var challenges\s*=\s*\[[\s\S]*?\];/, challengesJS);

// Replace confetti colors
jsBlock = jsBlock.replace(
  /var colors\s*=\s*\[[^\]]*\]/,
  "var colors = ['#7B2D3B','#9A4054','#003080','#16a34a','#d97706','#dc2626','#3B7DD8']"
);

// --- ASSEMBLE PROFESSOR FILE ---
const preclassTab = preclassContent || '<div class="tab-content" id="tab-exercises"><p>Pre-class content not found.</p></div>';

const html = `<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow">
<title>Professor View &mdash; Nilo Mesquita Patucci | Business English | Alumni by Better</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&display=swap" rel="stylesheet">
<script>
var audioMap = ${JSON.stringify(audioMap, null, 2)};
<\/script>
<style>
${css}
</style>
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.min.js"><\/script>
<script src="/lib/supabase-config.js"><\/script>
<script>window.STUDENT_SLUG='nilo-mesquita-patucci';window.TOTAL_AULAS=96;<\/script>
</head>
<body>

<!-- LOGO BAR -->
<div class="logo-bar">
  <img src="/assets/logo-alumni.png" alt="Alumni by Better">
  <span class="prof-badge">Professor View</span>
  <span class="slide-counter" id="slideCounter">01 / 37</span>
</div>

<!-- ============================== MAIN CONTENT ============================== -->
<div class="main-content">

<!-- HEADER HERO -->
<div class="header" style="background-image:url('https://images.unsplash.com/photo-1431324155629-1a6deb1dec8d?w=1400&q=80')">
  <div class="header-content">
    <div class="passport-badge">Business English &amp; FIFA Preparation &mdash; 96 Aulas</div>
    <h1>Nilo Mesquita Patucci</h1>
    <p class="subtitle">De &ldquo;me virar no dia a dia&rdquo; a representar o Brasil na FIFA com a autoridade e o inglês que combinam com quem você é</p>
    <div class="student-info">
      <span>B1</span>
      <span>Bragança Paulista / São Paulo, SP</span>
      <span>CCO &mdash; Corinthians / Advogado Esportivo</span>
      <span>90 min / Online</span>
    </div>
    <div class="progress-passport">
      <div class="progress-label"><span>Progresso Geral</span><span id="progressPercent">0%</span></div>
      <div class="progress-bar-outer"><div class="progress-bar-inner" id="progressBar"></div></div>
      <div class="stamps-row">
        <div class="stamp" id="stamp1" data-label="Identity" style="background-image:url('https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=200&q=80')"></div>
      </div>
    </div>
  </div>
</div>

<div class="container">

<!-- SPEED CONTROL -->
<div class="speed-control">
  <span class="speed-label">Velocidade:</span>
  <button class="speed-btn" data-speed="0.5" onclick="setAudioSpeed(0.5,this)">0.5x</button>
  <button class="speed-btn" data-speed="0.75" onclick="setAudioSpeed(0.75,this)">0.75x</button>
  <button class="speed-btn active" data-speed="1" onclick="setAudioSpeed(1,this)">1x</button>
  <button class="speed-btn" data-speed="1.25" onclick="setAudioSpeed(1.25,this)">1.25x</button>
</div>

<!-- TABS -->
<div class="tabs-wrapper">
  <div class="tabs">
    <button class="tab-btn active" onclick="switchTab('planning')">Planejamento</button>
    <button class="tab-btn" onclick="switchTab('exercises')">Pre-class</button>
    <button class="tab-btn" onclick="switchTab('inclass')">IN CLASS</button>
    <button class="tab-btn" onclick="switchTab('complementary')">Complementares</button>
  </div>
</div>

<!-- ========== TAB 1: PLANEJAMENTO ========== -->
<div class="tab-content active" id="tab-planning">

<div class="info-grid">
  <div class="info-item"><label>Nome</label><span>Nilo Mesquita Patucci</span></div>
  <div class="info-item"><label>Idade</label><span>40 anos</span></div>
  <div class="info-item"><label>Profissão</label><span>CCO Corinthians / Advogado Esportivo</span></div>
  <div class="info-item"><label>Cidade</label><span>Bragança Paulista / São Paulo, SP</span></div>
  <div class="info-item"><label>Nível</label><span>B1 (Intermediário)</span></div>
  <div class="info-item"><label>Foco</label><span>Business English &amp; FIFA Leadership Program</span></div>
  <div class="info-item"><label>Total de Aulas</label><span>96 aulas de 90 min</span></div>
  <div class="info-item"><label>Formato</label><span>Online (Zoom) &mdash; 2x/semana</span></div>
</div>

<div class="journey-box">
  <h4>Jornada de Transformação</h4>
  <p><strong>De:</strong> Um compliance officer que &ldquo;consegue se virar em viagem e dia a dia&rdquo; mas trava quando o inglês precisa ter o mesmo peso do seu terno.</p>
  <p style="margin-top:.5rem"><strong>Para:</strong> O único representante do Brasil no programa FIFA que faz networking, palestras e reuniões com a mesma presença que tem em português.</p>
</div>

<div style="padding:1.2rem;background:var(--accent-dim);border:1px solid rgba(123,45,59,.15);border-radius:10px;margin-bottom:1.5rem">
  <h4 style="font-family:'Cormorant Garamond',serif;font-size:1.1rem;color:var(--accent);margin-bottom:.5rem">Promessa do Programa</h4>
  <p style="font-size:.9rem;line-height:1.7">&ldquo;De &lsquo;me virar no dia a dia&rsquo; a representar o Brasil na FIFA com a autoridade e o inglês que combinam com quem você é.&rdquo;</p>
</div>

<div class="sw-grid">
  <div class="sw-box strengths">
    <h4>Forças</h4>
    <ul>
      <li>Inglês funcional já estabelecido para viagem e dia a dia</li>
      <li>Vocabulário técnico-profissional presente (compliance, governance)</li>
      <li>Alta motivação intrínseca com evento-alvo real (FIFA)</li>
      <li>Autoconsciência linguística, sabe onde precisa melhorar</li>
      <li>Repertório cultural e profissional extenso</li>
    </ul>
  </div>
  <div class="sw-box weaknesses">
    <h4>Pontos de Melhoria</h4>
    <ul>
      <li>Registro formal e linguagem executiva em inglês</li>
      <li>Erros sistemáticos de vocabulário técnico</li>
      <li>Fluência sob pressão e produção espontânea</li>
      <li>Escuta de sotaques não americanos</li>
      <li>Uso inconsistente de tempos verbais</li>
    </ul>
  </div>
</div>

<h3 style="font-family:'Cormorant Garamond',serif;font-size:1.3rem;margin-bottom:1rem">Currículo &mdash; 96 Aulas</h3>
<div class="curriculum-wrapper">
  <table class="curriculum-table">
    <thead><tr><th>#</th><th>Tema</th><th>Foco Linguístico</th><th>Atividade Principal</th><th>Homework</th></tr></thead>
    <tbody>
${buildCurriculumRows()}
    </tbody>
  </table>
</div>

</div><!-- /tab-planning -->

<!-- ========== TAB 2: PRE-CLASS ========== -->
${preclassTab.replace('tab-content active', 'tab-content')}

<!-- ========== TAB 3: IN CLASS ========== -->
<div class="tab-content" id="tab-inclass">
<h3 style="font-family:'Cormorant Garamond',serif;font-size:1.3rem;margin-bottom:1rem">Selecione a aula</h3>
<div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" onclick="enterSlideMode()">
  <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">01</div>
  <div><div style="font-weight:600;font-size:.95rem">Who Is Nilo in English?</div><div style="font-size:.8rem;color:var(--text-dim)">Diagnostic + Self-Introduction &mdash; 37 slides</div></div>
</div>
</div><!-- /tab-inclass -->

<!-- ========== TAB 4: COMPLEMENTARES ========== -->
${complementaresContent}

</div><!-- /container -->
</div><!-- /main-content -->

<!-- ============================== SLIDES WRAPPER (OUTSIDE main-content!) ============================== -->
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
  <span class="phase-label current" data-phase="1">The Man Behind the Badge</span>
  <span class="phase-label" data-phase="2">Packing Words</span>
  <span class="phase-label" data-phase="3">The Code</span>
  <span class="phase-label" data-phase="4">Getting There</span>
  <span class="phase-label" data-phase="5">Practice</span>
  <span class="phase-label" data-phase="6">Your Turn</span>
  <span class="phase-label" data-phase="7">Wrap-up</span>
</div>

<div class="slides-container" id="slidesContainer">
${slidesHTML}
</div><!-- /slides-container -->
</div><!-- /slides-wrapper -->

<!-- Teacher T Icon -->
<div class="teacher-t" id="teacherT">T<div class="teacher-t-panel" id="teacherPanel"></div></div>

<!-- Navigation Bar (IN CLASS) -->
<div class="nav-bar">
  <button class="nav-btn" id="prevBtn" onclick="changeSlide(-1)" disabled><svg viewBox="0 0 24 24"><polyline points="15 18 9 12 15 6"/></svg></button>
  <div class="slide-dots" id="slideDots"></div>
  <button class="nav-btn" id="nextBtn" onclick="changeSlide(1)"><svg viewBox="0 0 24 24"><polyline points="9 6 15 12 9 18"/></svg></button>
</div>

<!-- Confetti container -->
<div class="confetti-container" id="confettiContainer"></div>

<script>
${jsBlock}
<\/script>
<script src="/lib/lesson-progress.js"><\/script>
<script src="/lib/controle-aulas.js"><\/script>
</body>
</html>`;

fs.writeFileSync(OUTPUT, html);
console.log('Professor file written:', OUTPUT);
console.log('Size:', html.length, 'chars,', html.split('\n').length, 'lines');
