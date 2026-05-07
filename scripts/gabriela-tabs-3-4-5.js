// Tabs 3 (Plano de Aula), 4 (Material do Professor) e 5 (Atividades)

const { esc, escForJS } = require('./gabriela-helpers');
const D = require('./gabriela-data');

// ===== TAB 3: PLANO DE AULA =====
const planTimings = {
  1: [
    ['0–3','Warm-up','<strong>Rapport.</strong> "Hi Gabriela! Welcome to your first English class. Tell me — how are you today?" Permita resposta livre, mesmo em português. Observe nível de espontaneidade.'],
    ['3–8','Warm-up','<strong>Brain dump em PT.</strong> "Em uma palavra: o que mais te empolga sobre Paris 2027?" Anote a resposta. Diga: "Vamos transformar essa palavra em uma história em inglês."'],
    ['8–10','Warm-up','<strong>Set goal.</strong> "Hoje você sai daqui sabendo se apresentar em inglês — nome, idade, cidade, sonho. Em 60 minutos."'],
    ['10–13','Pre-teach','<strong>Word 1: name.</strong> "My <em>name</em> is Gabriela." Drill /neim/ — som /ei/ longo. Eliciar: "What is your name in English?"'],
    ['13–15','Pre-teach','<strong>Word 2: live.</strong> "I <em>live</em> in São Paulo." Drill /liv/ — diferenciar de "leave" /li:v/. Eliciar onde ela mora.'],
    ['15–17','Pre-teach','<strong>Word 3: student.</strong> "I am a <em>student</em>." Drill /ˈstu-dənt/. Atenção ao som /st/ — sem vogal antes (não é "estudent").'],
    ['17–19','Pre-teach','<strong>Word 4: hobby.</strong> "My favorite <em>hobby</em> is watching series." Drill /ˈhɒ-bi/. Eliciar 2 hobbies dela.'],
    ['19–21','Pre-teach','<strong>Word 5: travel.</strong> "I want to <em>travel</em> to France." Drill /ˈtræ-vəl/. Sempre seguido de "to + lugar".'],
    ['21–23','Pre-teach','<strong>Word 6: dream.</strong> "My <em>dream</em> is to visit Paris." Drill /dri:m/. Pode ser sonho enquanto dorme OU objetivo de vida.'],
    ['23–25','Pre-teach','<strong>Words 7-8: favorite + learn.</strong> Drill rápido. "favorite" /ˈfei-və-rət/ — só duas sílabas, não três. "learn" /lɜrn/ — som /ɜr/ americano.'],
    ['25–28','Teach','<strong>To be — Present.</strong> Quadro: I AM / You ARE / She IS. "Em inglês usamos <strong>to be</strong> com idade — não <strong>to have</strong>. Não é I HAVE 16 years. É I AM 16 years old." Drill 5x.'],
    ['28–32','Teach','<strong>Self-introduction structure.</strong> Mostrar na tela (Aba 4): 1) Hi! My name is… 2) I am [age] years old. 3) I am from… 4) I am a student. 5) My favorite hobby is… 6) My dream is to…'],
    ['32–35','Teach','<strong>Modelo (dialogue Sarah aeroporto).</strong> Mostrar diálogo na tela. Professor lê Sarah, Gabriela lê suas falas. Feedback positivo de pronúncia.'],
    ['35–38','Teach','<strong>CCQs.</strong> 1) "Em \'I am 16\', uso to be ou to have?" → To be. 2) "\'I from Brazil\' está certo?" → Não, falta IS: "I AM from Brazil". 3) "Após \'I am a\', vem o quê?" → Substantivo (student, fan, etc.).'],
    ['38–46','Practice','<strong>Oral Drilling — 8 prompts em PT, resposta em EN.</strong> Ver Aba 4. Cada prompt 30s. Se travar, soprar a primeira palavra.'],
    ['46–50','Practice','<strong>Error Correction (5 frases).</strong> Mostrar erros típicos na tela (Aba 4). Gabriela identifica e corrige cada um. Foco em "I have 16" → "I am 16".'],
    ['50–55','Production','<strong>Stage 1 — Guided.</strong> Gabriela lê o modelo e preenche com seus dados. 2 vezes até fluir.'],
    ['55–58','Production','<strong>Stage 2 — Semi-free.</strong> Sem o modelo. Apenas keywords: name, age, city, school, hobby, dream.'],
    ['58–60','Wrap-up','<strong>Gravar baseline + homework + preview.</strong> "Grave 60 segundos: nome, idade, cidade, hobby, sonho. Próxima aula: cumprimentos e check-in de hotel em Paris!"'],
  ],
  2: [
    ['0–3','Warm-up','<strong>Callback Aula 1.</strong> "Gabriela, apresente-se em 30 segundos como se fosse a primeira vez. Vai!" Observar progresso desde a baseline.'],
    ['3–6','Warm-up','<strong>Homework review.</strong> Ouvir o áudio de baseline. 2 elogios genuínos, 1 ponto a melhorar. Tom de parceira.'],
    ['6–10','Warm-up','<strong>Set goal.</strong> "Hoje você vai sobreviver a um check-in de hotel em Paris totalmente em inglês. Sem travar."'],
    ['10–13','Pre-teach','<strong>Hello / Good morning / Good evening.</strong> Drill ritualizado. Variar — Gabriela cumprimenta de 5 jeitos diferentes. Distinguir formal × informal.'],
    ['13–16','Pre-teach','<strong>Nice to meet you.</strong> Drill como chunk único. /nais tu mit ju/. Resposta: "Nice to meet you too."'],
    ['16–19','Pre-teach','<strong>Spell + last name.</strong> "Can you <em>spell</em> your <em>last name</em>?" Drill alfabeto rápido. Foco nas letras armadilha: A /ei/, E /i:/, I /ai/, G /dʒi:/, J /dʒei/, R /ɑr/.'],
    ['19–22','Pre-teach','<strong>How are you / Fine, thank you.</strong> Drill ritual de cumprimento. Gabriela ouve resposta longa em PT e percebe que aqui é curto.'],
    ['22–25','Pre-teach','<strong>Goodbye.</strong> Drill rápido. Variações: "Bye!", "See you!", "Have a nice day!"'],
    ['25–30','Teach','<strong>Alfabeto americano completo.</strong> Cantar com Gabriela. Foco específico: A-E-I, G-J, M-N, R. Soletrar GABRIELA e PIRES.'],
    ['30–35','Teach','<strong>Hotel check-in dialogue.</strong> Mostrar na tela (Aba 4). Ler junto. Gabriela é a hóspede. Praticar 2x.'],
    ['35–38','Teach','<strong>CCQs.</strong> 1) "\'Nice to meet you\' usa-se quando?" → Primeiro encontro. 2) "Letra I em inglês é /i/ ou /ai/?" → /ai/. 3) "\'How are you?\' espera resposta longa?" → Não, é cumprimento ritual.'],
    ['38–46','Practice','<strong>Oral Drilling — 8 prompts.</strong> Ver Aba 4. Foco em soletração e cumprimentos rituais.'],
    ['46–50','Practice','<strong>Error Correction (5 frases).</strong> Foco em "Nice meet you" → "Nice TO meet you" e na pronúncia de letras isoladas.'],
    ['50–56','Production','<strong>Stage 1 → 2 → 3.</strong> Hotel check-in completo. Aeroporto. Cafeteria. Cada um mais livre que o anterior.'],
    ['56–60','Wrap-up','<strong>Survival Card review + homework.</strong> "Próxima aula: você apresenta SEU mundo — sua escola, seus amigos, sua cidade — em inglês."'],
  ],
  3: [
    ['0–3','Warm-up','<strong>Callback Aulas 1-2.</strong> "Hi! Apresente-se com cumprimento, soletre seu nome, conte sua idade e diga seu sonho." Mini-revisão.'],
    ['3–6','Warm-up','<strong>Homework review.</strong> Ouvir o áudio de soletração. Feedback sobre as letras armadilha (E vs I).'],
    ['6–10','Warm-up','<strong>Show and tell.</strong> "Coloque 3 objetos da sua mochila na mesa." Atividade física para ativar this/that.'],
    ['10–13','Pre-teach','<strong>this.</strong> Apontar para objeto perto. "<em>This</em> is my phone." Drill /ðis/. Som /ð/ — língua entre os dentes.'],
    ['13–16','Pre-teach','<strong>that + these + those.</strong> Mostrar regra visual: this (perto, sing.), that (longe, sing.), these (perto, plural), those (longe, plural).'],
    ['16–19','Pre-teach','<strong>friend / family / school.</strong> Drill rápido em chunks. "This is my friend. My family lives in São Paulo. My school is on Paulista Avenue."'],
    ['19–22','Pre-teach','<strong>neighborhood.</strong> Palavra longa — drill devagar. /ˈnei-bər-hʊd/. Significa "bairro".'],
    ['22–25','Pre-teach','<strong>Quick-fire review.</strong> Apontar objetos da sala — Gabriela usa this/that/these/those.'],
    ['25–30','Teach','<strong>Articles a / an / the.</strong> "I am <em>a</em> student. I am <em>an</em> only child. <em>The</em> school is closed today." A vs AN é por som, não por letra.'],
    ['30–35','Teach','<strong>School tour dialogue.</strong> Mostrar na tela (Aba 4). Sarah visita a escola de Gabriela.'],
    ['35–38','Teach','<strong>CCQs.</strong> 1) "Aponto para meu celular: this ou that?" → this. 2) "Mostro 5 fotos longe: these ou those?" → those. 3) "\'a student\' ou \'an student\'?" → a (som de consoante /st/).'],
    ['38–46','Practice','<strong>Oral Drilling.</strong> Apontar objetos físicos da sala — produzir frase. Mostrar fotos no celular — usar these/those.'],
    ['46–50','Practice','<strong>Error Correction.</strong> Foco em "this is my friends" → "these are my friends" e "I live in the Brazil" → "I live in Brazil".'],
    ['50–56','Production','<strong>Tour da minha escola/quarto.</strong> 4 fotos no celular, 4 frases mínimo. Pergunta de volta.'],
    ['56–60','Wrap-up','<strong>Survival Card 3 + homework.</strong> "Próxima aula: você conta seu dia inteiro em inglês — manhã, tarde e noite."'],
  ],
  4: [
    ['0–3','Warm-up','<strong>Callback.</strong> "Em 3 frases com this/that/these/those, mostre algo da sua casa agora." Webcam tour rápido.'],
    ['3–6','Warm-up','<strong>Homework review.</strong> Olhar as 5 fotos com legendas EN. Corrigir 1-2 erros se houver.'],
    ['6–10','Warm-up','<strong>Brain dump.</strong> "Cinco coisas que você fez HOJE de manhã, em PT." Anotar — vamos traduzir juntas.'],
    ['10–13','Pre-teach','<strong>wake up.</strong> Drill /weik ʌp/. Phrasal verb. "I wake up at seven."'],
    ['13–16','Pre-teach','<strong>have breakfast.</strong> Chunk único — não traduzir literal. "I have breakfast at home."'],
    ['16–19','Pre-teach','<strong>go to school + study + watch.</strong> Drill rápido. Atenção: GO TO school (com TO), não "go school".'],
    ['19–22','Pre-teach','<strong>always / usually / never.</strong> Linha de frequência no quadro: 100% always > 80% usually > 50% sometimes > 0% never.'],
    ['22–25','Pre-teach','<strong>Quick-fire.</strong> Gabriela diz a frequência de cada atividade da sua rotina.'],
    ['25–30','Teach','<strong>Present Simple — 3ª pessoa singular.</strong> She/He/It + verbo + S. Visual: "I wake up. She <strong>wakes</strong> up." Drill 5 frases sobre Rory Gilmore.'],
    ['30–35','Teach','<strong>Position of frequency adverbs.</strong> Antes do verbo principal: "I <strong>always</strong> have breakfast." NÃO: "I have always breakfast."'],
    ['35–38','Teach','<strong>CCQs.</strong> 1) "She wake up — está certo?" → Não, falta -s: wakes. 2) "0% das vezes: which adverb?" → never. 3) "Onde colocar always?" → Antes do verbo principal.'],
    ['38–46','Practice','<strong>Oral Drilling — 8 prompts da rotina.</strong> Ver Aba 4. Cobrir manhã, tarde e noite.'],
    ['46–50','Practice','<strong>Error Correction.</strong> Foco em "she wake up", "I have always", "I no skip class".'],
    ['50–56','Production','<strong>Stage 1-2-3.</strong> Timeline visual → sem timeline → videocall com Sarah pedindo "What does your day look like?"'],
    ['56–60','Wrap-up','<strong>Survival Card 4 + homework.</strong> "Próxima aula: suas séries, seus crushes, suas opiniões fortes — tudo em inglês."'],
  ],
  5: [
    ['0–3','Warm-up','<strong>Callback.</strong> "Conte 3 coisas que você sempre faz e 1 coisa que você nunca faz." Revisão de frequency adverbs.'],
    ['3–6','Warm-up','<strong>Homework review.</strong> Ouvir o áudio "This is my day". Feedback positivo, 1 correção fina.'],
    ['6–10','Warm-up','<strong>Hot reactions.</strong> Mostrar capas: Gossip Girl, horror movie, novela brasileira, Friends. Reação rápida em EN: "I love this!" "I hate that!"'],
    ['10–13','Pre-teach','<strong>love + like.</strong> Drill com objetos físicos: doce, tênis, capa de série. Gabriela reage. Distinguir intensidade: love > like.'],
    ['13–16','Pre-teach','<strong>don\'t like + hate.</strong> "I <em>don\'t like</em> horror movies." "I <em>hate</em> Mondays." Hate é forte — usar com cuidado.'],
    ['16–19','Pre-teach','<strong>series / character / celebrity.</strong> Distinguir: series = série; character = personagem (na ficção); celebrity = celebridade real.'],
    ['19–22','Pre-teach','<strong>obsessed with.</strong> Frase pronta. /əb-SEST wɪð/. "I am <em>obsessed with</em> Friends."'],
    ['22–25','Pre-teach','<strong>Quick-fire.</strong> Gabriela completa: "I love ___. I like ___. I don\'t like ___. I hate ___. I am obsessed with ___."'],
    ['25–30','Teach','<strong>Like + verb-ing OR noun.</strong> "I like Friends." "I like watching Friends." Os dois funcionam. Após "like/love", verbo vai para -ING.'],
    ['30–35','Teach','<strong>Do you like…? — Yes, I do / No, I don\'t.</strong> Estrutura de pergunta com auxiliar DO. Sem "do" não é pergunta.'],
    ['35–38','Teach','<strong>CCQs.</strong> 1) "I AM like Friends — certo?" → Não, "I LIKE". 2) "Negativa: \'I no like\' ou \'I don\'t like\'?" → don\'t. 3) "obsessed = pouco ou muito?" → muito.'],
    ['38–46','Practice','<strong>Oral Drilling — 8 prompts pop culture.</strong> Ver Aba 4.'],
    ['46–50','Practice','<strong>Error Correction.</strong> Foco em "I am like" e "you like Friends?" sem auxiliar.'],
    ['50–56','Production','<strong>Stage 1-2-3.</strong> Reações rápidas → Top 3 séries com justificativa → Conversa com fã francesa.'],
    ['56–60','Wrap-up','<strong>Survival Card 5 + homework.</strong> "Próxima aula: números, horas e datas — para sobreviver em Paris."'],
  ],
};

function buildPlanLesson(n) {
  let rows = '';
  planTimings[n].forEach(t => {
    rows += `<tr><td class="time-cell">${t[0]}</td><td class="activity-cell">${esc(t[1])}</td><td>${t[2]}</td></tr>\n`;
  });

  let ccqsList = '';
  D.ccqs[n].forEach(c => { ccqsList += `<li><strong>"${esc(c.q)}"</strong> &rarr; <em>${esc(c.a)}</em></li>`; });

  let obstaclesList = '';
  D.obstacles[n].forEach(o => { obstaclesList += `<li><strong>${esc(o.label)}:</strong> ${esc(o.text)}</li>`; });

  let homeworkList = '';
  D.homework[n].forEach(h => { homeworkList += `<li>${esc(h)}</li>`; });

  let checklistList = '';
  D.checklistItems[n].forEach(c => { checklistList += `<li><input type="checkbox" onchange="toggleChecklist(this)"> ${esc(c)}</li>`; });

  return `<div class="teacher-lesson">
  <div class="teacher-hero" style="background-image:url('${D.lessonImages[n]}')">
    <h3>Aula 0${n} — ${esc(D.lessonTitles[n].split('—')[0].trim())}</h3>
    <div class="hero-sub">${esc(D.lessonTitles[n].split('—').slice(1).join('—').trim())} — 60 min</div>
  </div>
  <div class="teacher-body">
    <table class="plan-table">
      <thead><tr><th>Tempo</th><th>Fase</th><th>Atividade</th></tr></thead>
      <tbody>${rows}</tbody>
    </table>

    <div class="teacher-section" style="margin-top:2rem;">
      <h4>Detailed Teacher Guide <span class="phase-tag phase-teach">Reference</span></h4>

      <div class="teacher-tip"><strong>Promessa transformadora desta aula:</strong> ${esc(D.lessonPromises[n])}</div>

      <div class="teacher-tip"><strong>Critério de sucesso mensurável:</strong> ${esc(D.lessonObjectives[n])}</div>

      <div class="teacher-tip"><strong>CCQs com respostas esperadas:</strong><ul style="margin-top:0.5rem;padding-left:1.2rem;">${ccqsList}</ul></div>

      <div class="obstacle-alert"><strong>Antecipação de obstáculos específicos para Gabriela:</strong><ul style="margin-top:0.5rem;padding-left:1.2rem;">${obstaclesList}</ul></div>

      <div class="teacher-tip"><strong>Tom desta aula:</strong> Tom de parceira, não de autoridade. Gabriela é alta tolerância ao erro — pode desafiar mais. Energia dinâmica e variada — transições a cada 10-12 min. Usar interesses pop culture (Gossip Girl, Friends, Gilmore Girls) sempre que possível para manter engajamento.</div>

      <div class="teacher-tip"><strong>Delayed feedback (Production Stage 3):</strong> Não interromper durante o role-play. Anotar 3 positivos genuínos primeiro, depois 2 áreas de melhoria. Sempre fechar com positivo. Gabriela ri das próprias falhas — celebrar isso como força.</div>
    </div>

    <div class="homework-box">
      <h4>Homework — Aula ${n}</h4>
      <ul>${homeworkList}</ul>
    </div>
  </div>
</div>`;
}

function buildTab3Plan() {
  let lessons = '';
  for (let n = 1; n <= 5; n++) lessons += buildPlanLesson(n) + '\n';
  return `<div class="tab-content" id="tab-plan">
  ${lessons}
  <div style="background:var(--bg-card);border:1px solid var(--border);padding:2rem;border-radius:6px;text-align:center;margin-top:2rem;">
    <p style="font-style:italic;color:var(--text-dim);">Planos das aulas 6-48 serão adicionados nos próximos blocos.</p>
  </div>
</div>`;
}

// ===== TAB 4: MATERIAL DO PROFESSOR =====
const warmUpQuestions = {
  1: [
    'Hi Gabriela! How are you today?',
    'Tell me one thing you love about your week.',
    'If you could fly to Paris tomorrow, what is the FIRST place you would visit?',
    'What is your favorite series right now?',
    'In one English word: how do you feel about starting this course?',
  ],
  2: [
    'Apresente-se em 30 segundos. Vai!',
    'How was your homework? Did you record the audio?',
    'If a French girl your age says "Bonjour, what is your name?" — what do you answer?',
    'Did you watch any series in English this week?',
    'What is the most difficult letter to pronounce in English for you?',
  ],
  3: [
    'In 30 seconds, introduce yourself in English. Go!',
    'Spell your name aloud — letter by letter.',
    'Show me one object near you and say one sentence about it.',
    'Tell me about your school in 3 sentences.',
    'If Sarah from France visits São Paulo, where do you take her first?',
  ],
  4: [
    'Show me 3 things from your bag using "this is" or "these are".',
    'Tell me 2 sentences about your best friend.',
    'In 5 words: describe a typical Monday.',
    'Did you wake up early or late today?',
    'What is the first thing you do every morning?',
  ],
  5: [
    'Tell me 3 things you ALWAYS do and 1 thing you NEVER do.',
    'How was your homework? Did you record your full day?',
    'In 1 word: how was Friday last week?',
    'What is the LAST series you watched? Did you like it?',
    'Who is your favorite character in any series? Tell me in English.',
  ],
};

function buildMaterialLesson(n) {
  let warmHTML = '';
  warmUpQuestions[n].forEach((q, i) => {
    warmHTML += `<p style="font-size:0.9rem;color:var(--text);margin-bottom:0.5rem;">${i+1}. ${esc(q)}</p>\n`;
  });

  let vocabRows = '';
  D.vocab[n].forEach(v => {
    const sentence = v.exB.replace(/^"|"$/g,'');
    vocabRows += `<tr><td class="word-cell">${esc(v.word)}</td><td>&ldquo;${esc(sentence)}&rdquo;</td><td><button class="audio-btn" onclick="speakText('${escForJS(sentence)}', this)">&#9654;</button></td></tr>\n`;
  });

  let grammarHTML = `<div style="background:var(--bg-input);border:1px solid var(--border);padding:1.5rem;border-radius:4px;margin-bottom:1rem;">
    <p style="font-size:0.85rem;font-weight:600;color:var(--accent);margin-bottom:0.8rem;text-transform:uppercase;letter-spacing:1.5px;">Grammar Focus</p>
    <p style="font-size:0.95rem;color:var(--text);line-height:1.8;">${D.grammarTips[n]}</p>
  </div>`;

  // Dialogue
  const dlg = D.dialogues[n];
  let dlgLines = '';
  dlg.lines.forEach(l => {
    const avatar = l.side === 'staff' ? 'avatar-staff' : 'avatar-you';
    const bubble = l.side === 'staff' ? '' : 'your-turn';
    dlgLines += `<div class="dialogue-line"><div class="dialogue-avatar ${avatar}">${esc(l.speaker)}</div><div class="dialogue-bubble ${bubble}"><div class="speaker">${esc(l.name)}</div>${esc(l.text)} <button class="audio-btn" onclick="speakText('${escForJS(l.text)}', this)" style="margin-left:0.5rem;">&#9654;</button></div></div>\n`;
  });

  // Listening questions
  const listeningQs = {
    1: ['What is Sarah\'s name?', 'Where is Gabriela from?', 'What is Gabriela\'s dream?'],
    2: ['What is the name of the hotel?', 'How does Gabriela spell her last name?', 'How does she feel after the trip?'],
    3: ['Who is Gabriela\'s best friend?', 'What is at the gym?', 'What is Gabriela\'s favorite place at school?'],
    4: ['What time does Gabriela wake up?', 'How does she go to school?', 'What does she always do before sleeping?'],
    5: ['Who is Gabriela\'s favorite character?', 'Why does she like Blair?', 'Does Gabriela like horror movies?'],
  };
  let listenHTML = '';
  listeningQs[n].forEach((q, i) => {
    listenHTML += `<p style="font-size:0.9rem;color:var(--text);margin-bottom:0.5rem;font-weight:500;">${i+1}. ${esc(q)}</p>\n`;
  });

  // Oral drills
  let drillHTML = '';
  D.oralDrills[n].forEach((d, i) => {
    drillHTML += `<div style="background:var(--bg-input);border:1px solid var(--border);padding:1rem;border-radius:4px;margin-bottom:0.5rem;">
      <p style="font-size:0.9rem;color:var(--text);font-weight:500;">${i+1}. ${esc(d.pt)}</p>
      <p style="font-size:0.82rem;color:var(--text-dim);font-style:italic;">Expected: ${esc(d.en)}</p>
    </div>\n`;
  });

  // Error correction
  let errorHTML = '';
  D.errorCorrection[n].forEach((e, i) => {
    errorHTML += `<div style="background:var(--danger-bg);border:1px solid var(--danger-border);padding:1rem;border-radius:4px;margin-bottom:0.5rem;">
      <p style="font-size:0.9rem;color:var(--text);">${i+1}. ${esc(e.wrong)}</p>
      <p style="font-size:0.82rem;color:var(--success);font-weight:500;margin-top:0.3rem;">Correct: ${esc(e.right)}</p>
    </div>\n`;
  });

  // Production scenarios
  let prodHTML = '';
  D.productionScenarios[n].forEach(p => {
    prodHTML += `<div style="background:var(--accent-glow);border:1px solid rgba(212,50,106,0.2);padding:1.2rem;border-radius:4px;margin-bottom:0.8rem;">
      <p style="font-size:0.85rem;font-weight:600;color:var(--accent);margin-bottom:0.4rem;text-transform:uppercase;letter-spacing:1.5px;">${esc(p.label)}</p>
      <p style="font-size:0.88rem;color:var(--text);line-height:1.7;">${esc(p.text)}</p>
    </div>\n`;
  });

  // Substitution drill (simple — based on key sentence per lesson)
  const subDrills = {
    1: [
      ['"I am from São Paulo."','"Rio de Janeiro"','"I am from Rio de Janeiro."'],
      ['"My name is Gabriela."','"Helena"','"My name is Helena."'],
      ['"I am 16 years old."','"15"','"I am 15 years old."'],
      ['"I am a student."','"a fan"','"I am a fan."'],
    ],
    2: [
      ['"Good morning!"','"evening"','"Good evening!"'],
      ['"My last name is Pires."','"Silva"','"My last name is Silva."'],
      ['"I am fine, thank you."','"great"','"I am great, thank you."'],
      ['"Nice to meet you."','"see"','"Nice to see you."'],
    ],
    3: [
      ['"This is my phone."','"laptop"','"This is my laptop."'],
      ['"That is my school."','"house"','"That is my house."'],
      ['"These are my friends."','"books"','"These are my books."'],
      ['"My family lives in São Paulo."','"in Rio"','"My family lives in Rio."'],
    ],
    4: [
      ['"I wake up at seven."','"eight"','"I wake up at eight."'],
      ['"I always have breakfast."','"never"','"I never have breakfast."'],
      ['"She studies English."','"Helena"','"Helena studies English."'],
      ['"I go to school by metro."','"by bus"','"I go to school by bus."'],
    ],
    5: [
      ['"I love Gossip Girl."','"Friends"','"I love Friends."'],
      ['"I do not like horror movies."','"romantic"','"I do not like romantic movies."'],
      ['"Blair is my favorite character."','"Rory"','"Rory is my favorite character."'],
      ['"I am obsessed with Friends."','"Gilmore Girls"','"I am obsessed with Gilmore Girls."'],
    ],
  };
  let subHTML = '';
  subDrills[n].forEach(s => {
    subHTML += `<div style="background:var(--bg-input);border:1px solid var(--border);padding:1rem;border-radius:4px;margin-bottom:0.5rem;">
      <p style="font-size:0.9rem;color:var(--text);">${esc(s[0])} &rarr; Now say it with ${esc(s[1])}</p>
      <p style="font-size:0.82rem;color:var(--text-dim);font-style:italic;">Expected: ${esc(s[2])}</p>
    </div>\n`;
  });

  // Wrap-up checklist
  let checklistHTML = '';
  D.checklistItems[n].forEach(c => { checklistHTML += `<li><input type="checkbox" onchange="toggleChecklist(this)"> ${esc(c)}</li>\n`; });

  // Survival card for material
  let svHTML = '';
  D.survivalCards[n].forEach((p, i) => {
    svHTML += `<div class="survival-phrase"><span class="sp-num">${i+1}</span><span class="sp-en">${esc(p.en)}</span><span class="sp-pt">${esc(p.pt)}</span><button class="btn btn-listen" onclick="speakText('${escForJS(p.en)}', this)">&#9654;</button></div>\n`;
  });

  return `<div class="teacher-lesson">
  <div class="teacher-hero" style="background-image:url('${D.lessonImages[n]}')">
    <h3>Lesson 0${n} — ${esc(D.lessonTitles[n].split('—')[0].trim())}</h3>
    <div class="hero-sub">Screen-share content — ${esc(D.lessonTitles[n].split('—').slice(1).join('—').trim())}</div>
  </div>
  <div class="teacher-body">

    <div class="teacher-section">
      <h4>Warm-up <span class="phase-tag phase-warm">10 min</span></h4>
      <p style="font-size:0.85rem;color:var(--text-dim);margin-bottom:1rem;">Mostre estas perguntas na tela. Sem botão de áudio nesta seção.</p>
      <div style="background:var(--bg-input);border:1px solid var(--border);padding:1rem;border-radius:4px;">
        ${warmHTML}
      </div>
    </div>

    <div class="teacher-section">
      <h4>Vocabulary <span class="phase-tag phase-vocab">15 min</span></h4>
      <p style="font-size:0.85rem;color:var(--text-dim);margin-bottom:1rem;">Frases-exemplo DIFERENTES das do pre-class. Sem traduções na tela.</p>
      <table class="vocab-table">
        <thead><tr><th>Word</th><th>Example Sentence</th><th>Audio</th></tr></thead>
        <tbody>${vocabRows}</tbody>
      </table>
    </div>

    <div class="teacher-section">
      <h4>Grammar <span class="phase-tag phase-teach">10 min</span></h4>
      ${grammarHTML}
    </div>

    <div class="teacher-section">
      <h4>Dialogue — ${esc(dlg.title)} <span class="phase-tag phase-teach">Reference</span></h4>
      <p style="font-size:0.85rem;color:var(--text-dim);margin-bottom:1rem;">${esc(dlg.context)}</p>
      <div class="dialogue-container">${dlgLines}</div>
    </div>

    <div class="teacher-section">
      <h4>Listening Comprehension <span class="phase-tag phase-practice">5 min</span></h4>
      <p style="font-size:0.85rem;color:var(--text-dim);margin-bottom:1rem;">Após tocar o diálogo, pergunte (sem mostrar respostas):</p>
      <div style="background:var(--bg-input);border:1px solid var(--border);padding:1rem;border-radius:4px;">${listenHTML}</div>
    </div>

    <div class="teacher-section">
      <h4>Oral Drilling <span class="phase-tag phase-practice">8 min</span></h4>
      <p style="font-size:0.85rem;color:var(--text-dim);margin-bottom:1rem;">Mostre na tela. Professor lê em PT, aluna responde em EN.</p>
      ${drillHTML}
    </div>

    <div class="teacher-section">
      <h4>Error Correction <span class="phase-tag phase-practice">8 min</span></h4>
      <p style="font-size:0.85rem;color:var(--text-dim);margin-bottom:1rem;">Compartilhe na tela. Gabriela identifica e corrige cada erro.</p>
      ${errorHTML}
    </div>

    <div class="teacher-section">
      <h4>Production — Role-Play Scenarios <span class="phase-tag phase-production">15 min</span></h4>
      ${prodHTML}
    </div>

    <div class="teacher-section">
      <h4>Substitution Drill <span class="phase-tag phase-practice">Reference</span></h4>
      <p style="font-size:0.85rem;color:var(--text-dim);margin-bottom:1rem;">Diga a frase, depois troque a parte sublinhada.</p>
      ${subHTML}
    </div>

    <div class="teacher-section">
      <h4>Wrap-up — O que eu aprendi <span class="phase-tag phase-wrap">5 min</span></h4>
      <p style="font-size:0.85rem;color:var(--text-dim);margin-bottom:1rem;">Leia em voz alta com a aluna e marque conforme a confirmação.</p>
      <ul class="checklist" id="checklist-${n}">${checklistHTML}</ul>
    </div>

    ${buildSurvivalCardForMaterial(n, svHTML)}
  </div>
</div>`;
}

function buildSurvivalCardForMaterial(n, svHTML) {
  return `<div class="survival-card">
  <h4>Survival Card — Lesson ${n}: ${esc(D.lessonTitles[n].split('—')[0].trim())}</h4>
  ${svHTML}
</div>`;
}

function buildTab4Material() {
  let lessons = '';
  for (let n = 1; n <= 5; n++) lessons += buildMaterialLesson(n) + '\n';
  return `<div class="tab-content" id="tab-teacher">
  ${lessons}
</div>`;
}

// ===== TAB 5: ATIVIDADES COMPLEMENTARES =====
function buildTab5Activities() {
  return `<div class="tab-content" id="tab-complementary">

<div style="text-align:center;margin-bottom:2rem;">
  <h2 style="font-family:'Cormorant Garamond',serif;font-size:1.8rem;font-weight:700;color:var(--accent);">Atividades Complementares</h2>
  <p style="font-size:0.85rem;color:var(--text-dim);">Séries, filmes e canais para acelerar seu progresso entre as aulas.</p>
</div>

<h3 style="font-family:'Cormorant Garamond',serif;font-size:1.3rem;font-weight:600;color:var(--accent);margin-bottom:1rem;">Pop Culture & Séries Teen</h3>
<div class="media-grid" style="margin-bottom:2rem;">
  <div class="media-card-wrapper" data-media="media-1">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb series"></div>
      <div class="media-info">
        <div class="media-type">Série</div>
        <h5>Gossip Girl (HBO Max / Max)</h5>
        <p>Sua série favorita — aproveite. Vocabulário teen + Manhattan + fashion.</p>
        <div class="media-tip">Aulas 1-3: legenda PT-BR + EN. Aulas 4-7: só EN. Anote 3 frases/episódio.</div>
      </div>
    </div>
  </div>
  <div class="media-card-wrapper" data-media="media-2">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb series"></div>
      <div class="media-info">
        <div class="media-type">Série</div>
        <h5>Friends (Max)</h5>
        <p>Diálogos curtos, alta repetição de cumprimentos e expressões cotidianas.</p>
        <div class="media-tip">Comece pelo S01E01 com legenda PT-BR. Depois reveja com legenda EN.</div>
      </div>
    </div>
  </div>
  <div class="media-card-wrapper" data-media="media-3">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb series"></div>
      <div class="media-info">
        <div class="media-type">Série</div>
        <h5>Gilmore Girls (Netflix)</h5>
        <p>Vocabulário rico em contexto natural. Fala mais rápido — desafio na medida.</p>
        <div class="media-tip">Use para ouvir advérbios de frequência e rotinas (Aula 4).</div>
      </div>
    </div>
  </div>
  <div class="media-card-wrapper" data-media="media-4">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb movie"></div>
      <div class="media-info">
        <div class="media-type">Filme</div>
        <h5>Notting Hill (1999)</h5>
        <p>Romance com inglês britânico acessível. Cenas curtas reutilizáveis.</p>
        <div class="media-tip">Assista uma cena por dia — máximo 10 min.</div>
      </div>
    </div>
  </div>
</div>

<h3 style="font-family:'Cormorant Garamond',serif;font-size:1.3rem;font-weight:600;color:var(--accent);margin-bottom:1rem;">Paris & Viagem 2027</h3>
<div class="media-grid" style="margin-bottom:2rem;">
  <div class="media-card-wrapper" data-media="media-5">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb youtube"></div>
      <div class="media-info">
        <div class="media-type">YouTube</div>
        <h5>Emily in Paris (Netflix) — Cenas em inglês</h5>
        <p>Personagem americana em Paris. Vocabulário de viagem + situações reais.</p>
        <div class="media-tip">Aulas 6-9: foco em pedir direção, fazer pedido, check-in.</div>
      </div>
    </div>
  </div>
  <div class="media-card-wrapper" data-media="media-6">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb youtube"></div>
      <div class="media-info">
        <div class="media-type">YouTube</div>
        <h5>Walking Tours of Paris (Prowalk Tours)</h5>
        <p>Caminhadas reais em 4K em Paris, narradas em inglês simples.</p>
        <div class="media-tip">Use como background enquanto faz outra coisa. Imersão passiva.</div>
      </div>
    </div>
  </div>
  <div class="media-card-wrapper" data-media="media-7">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb youtube"></div>
      <div class="media-info">
        <div class="media-type">YouTube</div>
        <h5>The Travel Mum / Lost LeBlanc — Paris guides</h5>
        <p>Vlogs de viagem em inglês claro, com legenda automática.</p>
        <div class="media-tip">1 vlog por semana. Anote 5 frases novas por vlog.</div>
      </div>
    </div>
  </div>
</div>

<h3 style="font-family:'Cormorant Garamond',serif;font-size:1.3rem;font-weight:600;color:var(--accent);margin-bottom:1rem;">Pronúncia & Vocabulário Diário</h3>
<div class="media-grid" style="margin-bottom:2rem;">
  <div class="media-card-wrapper" data-media="media-8">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb youtube"></div>
      <div class="media-info">
        <div class="media-type">YouTube</div>
        <h5>English with Lucy</h5>
        <p>Canal britânico, vídeos curtos para iniciantes. Visual e dinâmico.</p>
        <div class="media-tip">Vídeos de 5-7 min. Comece pelo "Pronunciation Basics".</div>
      </div>
    </div>
  </div>
  <div class="media-card-wrapper" data-media="media-9">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb app"></div>
      <div class="media-info">
        <div class="media-type">App</div>
        <h5>Duolingo Stories</h5>
        <p>Micronarrativas em inglês com suporte em PT-BR. Adequado para A1+.</p>
        <div class="media-tip">15 min por dia. Foco nas histórias com diálogos curtos.</div>
      </div>
    </div>
  </div>
  <div class="media-card-wrapper" data-media="media-10">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb youtube"></div>
      <div class="media-info">
        <div class="media-type">YouTube</div>
        <h5>Easy English (Canguro English)</h5>
        <p>Inglês de rua com legendas, acessível para A1+.</p>
        <div class="media-tip">Episódios "Learn English with…" são ouro para listening.</div>
      </div>
    </div>
  </div>
  <div class="media-card-wrapper" data-media="media-11">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb podcast"></div>
      <div class="media-info">
        <div class="media-type">Podcast</div>
        <h5>6 Minute English (BBC)</h5>
        <p>Curto, claro, ótimo para prática diária no caminho da escola.</p>
        <div class="media-tip">1 episódio por dia no metrô. Anote 1 expressão nova.</div>
      </div>
    </div>
  </div>
</div>

<h3 style="font-family:'Cormorant Garamond',serif;font-size:1.3rem;font-weight:600;color:var(--accent);margin-bottom:1rem;">Por Aula — Conexões diretas</h3>
<div class="media-grid" style="margin-bottom:2rem;">
  <div class="media-card-wrapper" data-media="aula-1">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb series"></div>
      <div class="media-info">
        <div class="media-type">Aula 1</div>
        <h5>Friends — S01E01 (primeiros 5 min)</h5>
        <p>Apresentações pessoais entre amigos. Anote 3 frases que entendeu.</p>
      </div>
    </div>
  </div>
  <div class="media-card-wrapper" data-media="aula-2">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb youtube"></div>
      <div class="media-info">
        <div class="media-type">Aula 2</div>
        <h5>"English Alphabet Pronunciation" no YouTube</h5>
        <p>Vídeo de 5 min sobre o alfabeto americano. Anote as 3 letras mais diferentes do português.</p>
      </div>
    </div>
  </div>
  <div class="media-card-wrapper" data-media="aula-3">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb series"></div>
      <div class="media-info">
        <div class="media-type">Aula 3</div>
        <h5>Gossip Girl — Qualquer cena de S01</h5>
        <p>Conte quantas vezes ouve "this" ou "that" em uma cena. Anote o número.</p>
      </div>
    </div>
  </div>
  <div class="media-card-wrapper" data-media="aula-4">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb series"></div>
      <div class="media-info">
        <div class="media-type">Aula 4</div>
        <h5>Gilmore Girls — Cena de café da manhã</h5>
        <p>Anote 3 verbos de rotina em inglês que você ouviu.</p>
      </div>
    </div>
  </div>
  <div class="media-card-wrapper" data-media="aula-5">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb series"></div>
      <div class="media-info">
        <div class="media-type">Aula 5</div>
        <h5>Friends — 10 min com legenda EN</h5>
        <p>Conte quantas vezes ouve "I like", "I love" ou "I don't like". Escreva 3 frases.</p>
      </div>
    </div>
  </div>
</div>

<button class="reset-btn" onclick="resetProgress()">Resetar todo o progresso</button>

</div>`;
}

module.exports = { buildTab3Plan, buildTab4Material, buildTab5Activities };
