// Tabs 1 (Planejamento) e 2 (Pre-class) para o professor

const { esc, escForJS } = require('./gabriela-helpers');
const D = require('./gabriela-data-merged');
const BLOCK_LESSONS = D.BLOCK_LESSONS;

// Curriculum table — todas as 48 aulas
const fullCurriculum = [
  [1,'Who Is Gabriela? Diagnostic','To be + personal info','Self-introduction baseline + Victory Wall poster','60s baseline audio + Profile Card'],
  [2,'Hello, Nice to Meet You!','To be + alphabet + greetings','Hotel check-in role-play','Spell name aloud + 8 to-be sentences'],
  [3,'This Is My World','this/that/these/those + articles','Map of my week + Gossip Girl scene','5 photos with this/are sentences'],
  [4,'My Daily Life','Present simple + frequency adverbs','Routine vs. Rory Gilmore comparison','Full routine paragraph + 90s audio'],
  [5,'Do You Like It?','Like/love/hate + Do you like…?','Hot Takes game + French student role-play','My Favorites List + 60s audio'],
  [6,'Numbers, Time & Dates','Cardinals/ordinals + telling time','Paris itinerary simulation','Dream Paris itinerary'],
  [7,'Where Are You From?','To be + nationalities','Celebrity Nationality Game + hostel role-play','10 celebrity nationality sentences'],
  [8,'Can You Do That?','Modal can + survival expressions','Paris survival situations','5+5 can/can\'t list + 90s audio'],
  [9,'Where Is It?','Prepositions + directions imperative','Find the hotel map task + outdoor sim','Neighborhood map + directions audio'],
  [10,'What Do You Look Like?','Descriptive adjectives + has/is','Gossip Girl character profile cards','Character description + 60s self-description'],
  [11,'Let\'s Eat!','Would like + countable/uncountable','Café de Paris full restaurant simulation','Restaurant dialogue + audio'],
  [12,'Shopping in the City','How much + comparatives','Paris boutique shopping role-play','Shopping dialogue + 60s audio'],
  [13,'What Were You Doing?','Past continuous + when/while','Alibi game + Gossip Girl retelling','Yesterday paragraph + 90s audio'],
  [14,'What Happened?','Past simple regular/irregular','Weekend story + verb wall','Weekend story + 2min audio'],
  [15,'Have You Ever…?','Present perfect + ever/never','Bucket list activity + role-play','10 ever questions + 90s audio'],
  [16,'Tell Me About Your Plans!','Future going to + plans','Plan your Paris week + phone call role-play','Full Paris trip plan + 2min audio'],
  [17,'Emergency Mode','Have/feel + symptoms + should','Pharmacy + emergency simulations','Emergency Card + 90s pharmacy audio'],
  [18,'Let\'s Compare!','Comparatives + superlatives','SP vs Paris vs NY + opinion debate','10 comparison sentences + 90s audio'],
  [19,'Making Plans & Inviting','Would you like + Let\'s + What about','Paris social weekend role-play','3 invitation scenarios + 90s audio'],
  [20,'Block 1 Review','All structures recycled','Paris Survival Mega Role-play','Re-record baseline + Vocabulary Book'],
  [21,'I Love My City','Present simple + describing places','São Paulo tour for Sarah','City description audio'],
  [22,'Family & Relationships','Possessive adjectives','Family tree presentation','Family description + audio'],
  [23,'Telling Stories','Past simple narrative','Tell my best memory','Memory story audio'],
  [24,'Series Marathon Recap','Past simple + opinion','Episode review + recommendation','Episode recap audio'],
  [25,'Going Viral','Vocabulary social media','TikTok script in English','60s English TikTok-style audio'],
  [26,'School Life','Vocabulary school + frequency','School schedule presentation','School week audio'],
  [27,'My Future Self','Will + future plans','Where will I be in 10 years?','5-year vision audio'],
  [28,'Music & Culture','Like + comparatives','Brazilian vs international playlist','Music recommendation audio'],
  [29,'Travel Stories','Past simple + sequence','Last vacation full retelling','Vacation story audio'],
  [30,'Asking Better Questions','Wh-questions advanced','Interview a celebrity simulation','10 interview questions audio'],
  [31,'Dream Big','Want to + would like to','My biggest dreams pitch','Dream pitch 90s audio'],
  [32,'Pop Culture Deep Dive','Recycled vocab + opinion','Defend favorite show debate','Opinion piece audio'],
  [33,'Pronunciation Sprint I','TH/R/L sounds','Minimal pairs drill','15 minimal pairs audio'],
  [34,'Texts & Messages','Informal English','WhatsApp in English challenge','WhatsApp screenshots'],
  [35,'I Disagree, But Politely','Polite disagreement','Friendly debate role-play','Debate audio'],
  [36,'If I Could Go Anywhere','Conditional 1','Imagined trip planning','If audio (5 sentences)'],
  [37,'Career Conversations','Job vocabulary','Career interview simulation','Career story audio'],
  [38,'Pronunciation Sprint II','Stress + intonation','Stress pattern drills','10 stress sentences audio'],
  [39,'France 101','Country vocabulary + culture','French culture quiz + roleplay','Paris facts audio'],
  [40,'Your Paris Survival Kit','All survival vocab integrated','Full Paris simulation: airport to dinner','Survival recap audio'],
  [41,'Telling Jokes & Stories','Past + present mixed','Tell a funny story','Joke/story audio'],
  [42,'Real-Time Listening','Listening strategies','Watch + summarize','Summary audio'],
  [43,'Speaking Marathon','All structures','Timed speaking tasks','Self-recorded marathon'],
  [44,'Networking with Teens','Social English advanced','Meet new friend simulation','Friend-making audio'],
  [45,'Defending Your Opinion','Opinion + reasons + softeners','Mini debate','Defense audio'],
  [46,'Storytelling for Impact','Narrative structure','Personal story 3min','Story performance'],
  [47,'Final Simulation','Full integration','Paris arrival to departure simulation','Reflection audio'],
  [48,'Final Class — Celebration','Celebration + plan','Final assessment + certificate','Continue your English journey!'],
];

function buildTab1Planning() {
  let curriculumRows = '';
  fullCurriculum.forEach(row => {
    curriculumRows += `<tr><td class="aula-cell">${String(row[0]).padStart(2,'0')}</td><td>${esc(row[1])}</td><td>${esc(row[2])}</td><td>${esc(row[3])}</td><td>${esc(row[4])}</td></tr>\n`;
  });

  return `<div class="tab-content active" id="tab-planning">

<div style="text-align:center;margin-bottom:2rem;">
  <img src="../assets/logo-alumni.png" alt="Alumni by Better" style="height:40px;margin-bottom:1rem;">
  <h2 style="font-family:'Cormorant Garamond',serif;font-size:2rem;font-weight:700;color:var(--accent);">Planejamento Pedagógico</h2>
  <p style="font-size:0.85rem;color:var(--text-dim);">Gabriela Pires — Teen English: Paris 2027 — 48 Aulas</p>
</div>

<div class="info-grid">
  <div class="info-item"><div class="info-label">Nome</div><div class="info-value">Gabriela Pires</div></div>
  <div class="info-item"><div class="info-label">Idade</div><div class="info-value">15-16 anos</div></div>
  <div class="info-item"><div class="info-label">Localização</div><div class="info-value">São Paulo, SP</div></div>
  <div class="info-item"><div class="info-label">Profissão</div><div class="info-value">Estudante do ensino médio</div></div>
  <div class="info-item"><div class="info-label">Foco</div><div class="info-value">Comunicação oral + Paris 2027</div></div>
  <div class="info-item"><div class="info-label">Nível</div><div class="info-value">A1+ (em transição para A2)</div></div>
  <div class="info-item"><div class="info-label">Frequência</div><div class="info-value">3x/semana, 60 min, presencial</div></div>
  <div class="info-item"><div class="info-label">Evento-âncora</div><div class="info-value">Viagem Europa — Fev/2027</div></div>
  <div class="info-item" style="grid-column: span 2;"><div class="info-label">Objetivo</div><div class="info-value">Chegar à França e se virar em inglês em situações reais de turismo, com confiança e autonomia.</div></div>
  <div class="info-item" style="grid-column: span 2;"><div class="info-label">Distribuição</div><div class="info-value">50% Speaking · 30% Listening · 15% Vocabulário · 5% Writing</div></div>
</div>

<div class="journey-box">
  <h4>Jornada do Personagem</h4>
  <div class="journey-from">${esc(D.studentInfo.journeyFrom)}</div>
  <div class="journey-arrow">&#8595;</div>
  <div class="journey-to">${esc(D.studentInfo.journeyTo)}</div>
</div>

<div class="promise-box">
  <p>${esc(D.studentInfo.promise)}</p>
</div>

<div class="sw-grid">
  <div class="sw-col strengths">
    <h4>Forças</h4>
    <ul>
      <li>Pronúncia com base fonética sólida — sem travas articulatórias</li>
      <li>Disposição para tentar comunicar mesmo sem domínio completo</li>
      <li>Alta tolerância ao erro — baixo filtro afetivo natural</li>
      <li>Motivação ancorada em evento concreto (Paris 2027)</li>
      <li>Alta energia e engajamento durante consultoria</li>
      <li>2+ horas de estudo fora das aulas — alto potencial de imersão</li>
    </ul>
  </div>
  <div class="sw-col weaknesses">
    <h4>Pontos de Atenção</h4>
    <ul>
      <li>Forte dependência do português — barreira principal à fluência</li>
      <li>Interlanguage em construção — sistema linguístico ainda frágil</li>
      <li>Engajamento variável típico de adolescentes</li>
      <li>Produção escrita praticamente não desenvolvida</li>
    </ul>
  </div>
</div>

<h3 style="font-family:'Cormorant Garamond',serif;font-size:1.3rem;font-weight:600;color:var(--white);margin-bottom:1rem;">Currículo — 48 Aulas</h3>
<div style="overflow-x:auto;">
<table class="curriculum-table">
  <thead><tr><th>Aula</th><th>Tema</th><th>Foco Linguístico</th><th>Atividade Principal</th><th>Dever de Casa</th></tr></thead>
  <tbody>${curriculumRows}</tbody>
</table>
</div>

<h3 style="font-family:'Cormorant Garamond',serif;font-size:1.3rem;font-weight:600;color:var(--white);margin:2rem 0 1rem;">Metodologia</h3>
<div style="display:grid;gap:0.8rem;margin-bottom:2rem;">
  <div class="method-card"><h5>1. PPP (Presentation, Practice, Production)</h5><p>Cada aula segue o ciclo PPP adaptado a 60 min: aquecimento, vocabulário com contexto, prática guiada, produção oral em pares e role-play livre.</p></div>
  <div class="method-card"><h5>2. Personalização Pop Culture</h5><p>Conteúdo ancorado em Gossip Girl, Friends, Gilmore Girls, celebridades e a viagem para Paris 2027.</p></div>
  <div class="method-card"><h5>3. Speaking First</h5><p>50% do tempo dedicado à produção oral. Gabriela aprende fazendo — não ouvindo explicações longas.</p></div>
  <div class="method-card"><h5>4. Cinestésico + Lúdico</h5><p>Flashcards físicos, role-plays, simulações, objetos reais. Jogos de pattern drilling com variação de contexto.</p></div>
  <div class="method-card"><h5>5. Survival Card Progressivo</h5><p>A cada aula, Gabriela ganha 5 frases novas para sobreviver em Paris. O cartão cresce até a viagem.</p></div>
</div>

<div class="personality-card">
  <h4>Mapa de Personalidade</h4>
  <div class="personality-item"><div class="p-label">Idade</div><div class="p-value">15-16 anos — adolescente teen, peer-like</div></div>
  <div class="personality-item"><div class="p-label">Stake</div><div class="p-value">${esc(D.studentInfo.stake)}</div></div>
  <div class="personality-item"><div class="p-label">Vitória</div><div class="p-value">${esc(D.studentInfo.vitoria)}</div></div>
  <div class="personality-item"><div class="p-label">Citação-âncora</div><div class="p-value">"Disposição para tentar se comunicar mesmo com apoio do português" — base do programa.</div></div>
  <div class="personality-item"><div class="p-label">Estilo de Aprendizagem</div><div class="p-value">Cinestésico + auditivo — aprende fazendo, praticando, repetindo em contexto real.</div></div>
  <div class="personality-item"><div class="p-label">Energia Preferida</div><div class="p-value">Dinâmica e variada — tédio é o maior risco. Atividades curtas, transições a cada 10-12 min.</div></div>
  <div class="personality-item"><div class="p-label">Tolerância ao Erro</div><div class="p-value">Alta — ri das próprias falhas e segue. Pode desafiar mais, com produção sem script.</div></div>
  <div class="personality-item"><div class="p-label">Interesses Pop Culture</div><div class="p-value">Gossip Girl, Friends, Gilmore Girls, Notting Hill, Blake Lively, fofoca leve, viagem.</div></div>
</div>

</div>`;
}

// ===== TAB 2: PRE-CLASS =====
function buildVocabSection(n) {
  let cards = '';
  D.vocab[n].forEach(v => {
    cards += `<div class="vocab-card">
  <div class="vocab-card-content">
    <div class="vocab-card-header"><span class="vocab-card-word">${esc(v.word)}</span><span class="vocab-card-dot">&middot;</span><span class="vocab-card-translation">${esc(v.pt)}</span></div>
    <div class="vocab-card-example">&ldquo;${esc(v.exA.replace(/^"|"$/g,''))}&rdquo;</div>
  </div>
  <button class="audio-btn" onclick="speakText('${escForJS(v.exA.replace(/^"|"$/g,''))}', this)" aria-label="Ouvir">&#9654; Ouvir</button>
</div>\n`;
  });
  return `<div class="exercise-section">
  <div class="section-header-row">
    <h4>Vocabulário <span class="badge badge-vocab">Vocabulário</span></h4>
    <button class="listen-all-btn" onclick="listenAllVocab(this)">&#9654; Ouvir todos</button>
  </div>
  <p class="microcopy">Olha a palavra, a tradução e o exemplo juntos. Toca em Ouvir — o som ajuda muito a memória.</p>
  <div class="vocab-cards">${cards}</div>
</div>`;
}

function buildMatchingSection(n) {
  let rows = '';
  D.matching[n].forEach((m, i) => {
    const opts = [...m.distractors, m.correct].sort(() => Math.random() - 0.5);
    let optsHtml = '<option value="">Select...</option>';
    opts.forEach(o => { optsHtml += `<option value="${esc(o)}">${esc(o)}</option>`; });
    rows += `<div class="match-row" data-answer="${esc(m.correct)}"><span class="match-word">${esc(m.word)}</span><select onchange="checkMatch(this)" aria-label="Tradução de ${esc(m.word)}">${optsHtml}</select></div>\n`;
  });
  return `<div class="exercise-section">
  <h4>V1. Match the words to their meanings <span class="badge badge-vocab">Vocabulary</span></h4>
  <p class="microcopy">Selecione a tradução correta para cada palavra. Errou? Leia o exemplo de novo — é aí que se aprende.</p>
  <div class="match-grid" id="match-l${n}">${rows}</div>
  <button class="verify-all-btn" onclick="verifyAllMatches('match-l${n}')">Check Answers</button>
</div>`;
}

function buildFillSection(n) {
  let items = '';
  D.fillIn[n].forEach(f => {
    items += `<div class="fill-blank-item">
  <div class="fill-blank-sentence">${esc(f.sentence).replace(/___/g, `<input class="blank-input" data-answer="${esc(f.answer)}" data-hint="${esc(f.hint)}" data-phrase="${esc(f.phrase)}" placeholder="___" aria-label="Complete a frase">`)}</div>
  <div class="hint-text">${esc(f.hint)}</div>
  <button class="btn check-btn" onclick="checkBlank(this)">Check</button>
  <button class="btn listen-blank-btn" onclick="listenBlank(this)">Listen</button>
</div>\n`;
  });
  return `<div class="exercise-section">
  <h4>P1. Complete with the correct word <span class="badge badge-practice">Practice</span></h4>
  <p class="microcopy">Faça um de cada vez. Errou? Lê a dica em inglês com calma — é assim que se aprende de verdade.</p>
  ${items}
</div>`;
}

function buildMCSection(n) {
  let items = '';
  D.multipleChoice[n].forEach(mc => {
    let opts = '';
    mc.options.forEach((o, i) => {
      const correct = i === mc.correct ? 'true' : 'false';
      const letter = String.fromCharCode(65 + i);
      opts += `<div class="quiz-option" tabindex="0" role="button" onclick="selectQuiz(this)" data-correct="${correct}"><span class="option-letter">${letter}</span> ${esc(o)}</div>\n`;
    });
    items += `<div class="quiz-item">
  <div class="quiz-question">${esc(mc.q)}</div>
  <div class="quiz-options">${opts}</div>
</div>\n`;
  });
  return `<div class="exercise-section">
  <h4>P2. Choose the best answer <span class="badge badge-quiz">Quiz</span></h4>
  <p class="microcopy">Clica na resposta. Verde = certo, vermelho = tente de novo. Errou? Lê tudo de novo com calma.</p>
  ${items}
</div>`;
}

function buildOrderingSection(n) {
  const o = D.ordering[n];
  let shuffled = [...o.items].sort(() => Math.random() - 0.5);
  let items = '';
  shuffled.forEach(item => {
    items += `<div class="order-item" draggable="true" data-order="${item.order}" onclick="selectOrderItem(this,'order-l${n}')"><span class="order-num">?</span><span class="order-text">${esc(item.text)}</span><span class="order-arrows"><button class="arrow-btn" onclick="event.stopPropagation();moveItem(this,-1,'order-l${n}')">&#9650;</button><button class="arrow-btn" onclick="event.stopPropagation();moveItem(this,1,'order-l${n}')">&#9660;</button></span></div>\n`;
  });
  return `<div class="exercise-section">
  <h4>P3. ${esc(o.title)} <span class="badge badge-order">Practice</span></h4>
  <p class="microcopy">Toque em cada item na ordem certa, ou use as setas para mover. Quando estiver pronta, clique em Check Order.</p>
  <div class="order-container" id="order-l${n}">${items}</div>
  <button class="btn check-btn" onclick="checkOrder('order-l${n}')" style="margin-top:1rem;">Check Order</button>
</div>`;
}

function buildPronSection(n) {
  let cards = '';
  D.pronunciation[n].forEach(p => {
    cards += `<div class="speech-card" data-phrase="${esc(p.phrase)}">
  <div class="speech-phrase">${esc(p.phrase)}</div>
  <div class="speech-translation">${esc(p.pt)}</div>
  <div class="speech-controls">
    <button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Ouvir</button>
    <button class="btn btn-record" onclick="startRecording(this)">&#9679; Gravar</button>
    <button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Parar</button>
  </div>
  <div class="speech-result"></div>
</div>\n`;
  });
  return `<div class="exercise-section">
  <h4>P4. Read aloud <span class="badge badge-speak">Speaking</span></h4>
  <p class="microcopy">Ouça a frase, depois grave você falando. Use o Chrome — o sistema compara palavra por palavra.</p>
  ${cards}
</div>`;
}

function buildThinkSection(n) {
  const t = D.thinkAboutIt[n];
  return `<div class="exercise-section">
  <h4>T1. Think and respond <span class="badge badge-think">Reflection</span></h4>
  <p class="microcopy">Aqui não tem resposta certa — é pra você pensar em inglês. Toque no microfone e responde como vier.</p>
  <div class="think-card">
    <div style="font-size:0.92rem;color:var(--text);margin-bottom:1rem;line-height:1.8;">${esc(t.question)}</div>
    <div class="speech-card" data-phrase="${esc(t.suggestion)}" style="background:var(--accent-dim);border:1px solid rgba(212,50,106,0.25);">
      <div style="font-size:0.72rem;font-weight:600;text-transform:uppercase;letter-spacing:1.5px;color:var(--accent);margin-bottom:0.5rem;">Sugestão de resposta</div>
      <div class="speech-phrase" style="font-size:1.05rem;">&ldquo;${esc(t.suggestion)}&rdquo;</div>
      <div class="speech-translation">${esc(t.suggestionPt)}</div>
      <div class="speech-controls">
        <button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Ouvir</button>
        <button class="btn btn-record" onclick="startRecording(this)">&#9679; Gravar e comparar</button>
        <button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Parar</button>
      </div>
      <div class="speech-result"></div>
    </div>
  </div>
</div>`;
}

function buildSurvivalCard(n) {
  let phrases = '';
  D.survivalCards[n].forEach((p, i) => {
    phrases += `<div class="survival-phrase"><span class="sp-num">${i+1}</span><span class="sp-en">${esc(p.en)}</span><span class="sp-pt">${esc(p.pt)}</span><button class="btn btn-listen" onclick="speakText('${escForJS(p.en)}', this)">&#9654;</button></div>\n`;
  });
  return `<div class="survival-card">
  <h4>Survival Card — Lesson ${n}: ${esc(D.lessonTitles[n].split('—')[0].trim())}</h4>
  ${phrases}
</div>`;
}

function buildPreClassLesson(n) {
  const padded = String(n).padStart(2, '0');
  return `<div class="lesson-card" id="ex-lesson-${n}">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('${D.lessonHeaderImages[n]}')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Aula ${padded} — Pre-class</div>
      <h3>${esc(D.lessonTitles[n])}</h3>
      <div class="lesson-desc">${esc(D.lessonPromises[n])}</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="${n}" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="${n}">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">
    <p style="font-size:0.85rem;color:var(--text-mid);margin-bottom:1.5rem;"><strong style="color:var(--accent);">Objetivo:</strong> ${esc(D.lessonObjectives[n])}</p>
    ${buildVocabSection(n)}
    ${buildMatchingSection(n)}
    ${buildFillSection(n)}
    ${buildMCSection(n)}
    ${buildOrderingSection(n)}
    ${buildPronSection(n)}
    ${buildThinkSection(n)}
    ${buildSurvivalCard(n)}
  </div>
</div>`;
}

function buildTab2PreClass() {
  // Renderiza aulas geradas (Bloco 1 + 2) intercaladas com placeholders das outras
  const generated = new Set(BLOCK_LESSONS);
  let allLessonsHTML = '';
  for (let n = 1; n <= 48; n++) {
    if (generated.has(n)) {
      allLessonsHTML += buildPreClassLesson(n) + '\n';
    } else {
      const padded = String(n).padStart(2, '0');
      allLessonsHTML += `<div class="lesson-card">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=600&q=80');opacity:0.35;"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Aula ${padded} — Pre-class</div>
      <h3 style="opacity:0.7;">${esc(D.lessonTitles[n] || 'Próximo bloco')}</h3>
      <div class="lesson-desc" style="font-style:italic;color:var(--text-dim);">Conteúdo será adicionado no próximo bloco.</div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body"><p style="text-align:center;padding:2rem;color:var(--text-dim);font-style:italic;">Conteúdo será adicionado no próximo bloco.</p></div>
</div>\n`;
    }
  }

  return `<div class="tab-content" id="tab-exercises">

<div class="welcome-card">
  <h3>Bem-vinda, Gabriela!</h3>
  <p>Seu programa Teen English começa aqui. Em 48 aulas, você vai transformar "tentar falar com apoio do português" em "pedir o caminho em Paris sem travar".</p>
  <blockquote>"Disposição para tentar se comunicar mesmo com apoio do português."</blockquote>
  <div class="emergency-phrases">
    <h4>Frases de emergência (memorize antes da Aula 1)</h4>
    <div style="display:grid;gap:0.8rem">
      <div style="background:var(--bg-elevated);padding:0.8rem 1rem;border-radius:8px;display:flex;align-items:center;justify-content:space-between;gap:0.8rem;flex-wrap:wrap;"><div><strong style="font-size:0.9rem">I am sorry, I do not understand.</strong><br><span style="font-size:0.8rem;color:var(--text-dim)">Desculpe, não entendi.</span></div><button class="audio-btn" onclick="speakText('I am sorry, I do not understand.', this)">&#9654; Ouvir</button></div>
      <div style="background:var(--bg-elevated);padding:0.8rem 1rem;border-radius:8px;display:flex;align-items:center;justify-content:space-between;gap:0.8rem;flex-wrap:wrap;"><div><strong style="font-size:0.9rem">Could you speak more slowly, please?</strong><br><span style="font-size:0.8rem;color:var(--text-dim)">Pode falar mais devagar, por favor?</span></div><button class="audio-btn" onclick="speakText('Could you speak more slowly, please?', this)">&#9654; Ouvir</button></div>
      <div style="background:var(--bg-elevated);padding:0.8rem 1rem;border-radius:8px;display:flex;align-items:center;justify-content:space-between;gap:0.8rem;flex-wrap:wrap;"><div><strong style="font-size:0.9rem">How do you say that in English?</strong><br><span style="font-size:0.8rem;color:var(--text-dim)">Como se diz isso em inglês?</span></div><button class="audio-btn" onclick="speakText('How do you say that in English?', this)">&#9654; Ouvir</button></div>
      <div style="background:var(--bg-elevated);padding:0.8rem 1rem;border-radius:8px;display:flex;align-items:center;justify-content:space-between;gap:0.8rem;flex-wrap:wrap;"><div><strong style="font-size:0.9rem">Could you repeat that, please?</strong><br><span style="font-size:0.8rem;color:var(--text-dim)">Pode repetir, por favor?</span></div><button class="audio-btn" onclick="speakText('Could you repeat that, please?', this)">&#9654; Ouvir</button></div>
      <div style="background:var(--bg-elevated);padding:0.8rem 1rem;border-radius:8px;display:flex;align-items:center;justify-content:space-between;gap:0.8rem;flex-wrap:wrap;"><div><strong style="font-size:0.9rem">Wait a moment, please.</strong><br><span style="font-size:0.8rem;color:var(--text-dim)">Um momento, por favor.</span></div><button class="audio-btn" onclick="speakText('Wait a moment, please.', this)">&#9654; Ouvir</button></div>
    </div>
  </div>
</div>

${allLessonsHTML}
</div>`;
}

module.exports = { buildTab1Planning, buildTab2PreClass };
