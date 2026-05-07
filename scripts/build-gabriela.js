#!/usr/bin/env node
/**
 * Build Gabriela Pires — gera professor + aluno + audioMap base
 */

const fs = require('fs');
const path = require('path');
const { getHeadHTML, getCommonJS, esc } = require('./gabriela-helpers');
const D = require('./gabriela-data-merged');
const BLOCK_LESSONS = D.BLOCK_LESSONS;
const { buildTab1Planning, buildTab2PreClass } = require('./gabriela-tabs-1-2');
const { buildTab3Plan, buildTab4Material, buildTab5Activities } = require('./gabriela-tabs-3-4-5');

// ============= COLETAR FRASES PARA AUDIO MAP =============
function collectAudioPhrases() {
  const phrases = new Set();
  // Vocab pre-class (exA) e material (exB)
  Object.values(D.vocab).forEach(arr => arr.forEach(v => {
    phrases.add(v.exA.replace(/^"|"$/g,''));
    phrases.add(v.exB.replace(/^"|"$/g,''));
  }));
  // Fill-in phrases
  Object.values(D.fillIn).forEach(arr => arr.forEach(f => phrases.add(f.phrase)));
  // Pronunciation
  Object.values(D.pronunciation).forEach(arr => arr.forEach(p => phrases.add(p.phrase)));
  // Think suggestion
  Object.values(D.thinkAboutIt).forEach(t => phrases.add(t.suggestion));
  // Survival
  Object.values(D.survivalCards).forEach(arr => arr.forEach(p => phrases.add(p.en)));
  // Dialogues
  Object.values(D.dialogues).forEach(d => d.lines.forEach(l => phrases.add(l.text)));
  // Emergency
  ['I am sorry, I do not understand.','Could you speak more slowly, please?','How do you say that in English?','Could you repeat that, please?','Wait a moment, please.'].forEach(p => phrases.add(p));
  return Array.from(phrases).filter(p => p && p.length > 0).sort();
}

function slugifyAudioFile(text) {
  return text.toLowerCase()
    .replace(/[áàãâä]/g, 'a').replace(/[éèêë]/g, 'e').replace(/[íìîï]/g, 'i')
    .replace(/[óòõôö]/g, 'o').replace(/[úùûü]/g, 'u').replace(/[ç]/g, 'c')
    .replace(/'/g, '').replace(/"/g, '').replace(/[^a-z0-9 ]/g, '')
    .trim().replace(/\s+/g, '_').substring(0, 60);
}

function buildAudioMap() {
  const phrases = collectAudioPhrases();
  const map = {};
  phrases.forEach(p => {
    const slug = slugifyAudioFile(p);
    map[p] = `/audio/${D.studentInfo.slug}/${slug}.mp3`;
  });
  return map;
}

// ============= MONTAR HTML PROFESSOR =============
function buildProfessor(audioMapJSON) {
  const head = getHeadHTML('Professor View — Gabriela Pires | Teen English: Paris 2027 | Alumni by Better');
  const stamps = BLOCK_LESSONS.map(n => `<div class="stamp" id="stamp${n}" data-label="${esc(D.stampLabels[n])}" style="background-image:url('${D.stampImages[n]}')"></div>`).join('\n');

  const body = `<body>

<div class="logo-bar">
  <img src="../assets/logo-alumni.png" alt="Alumni by Better">
  <span class="prof-badge">Professor View</span>
</div>

<div class="header">
  <div class="header-content">
    <div class="passport-badge">Teen English Program — Paris 2027</div>
    <h1>Gabriela Pires</h1>
    <div class="subtitle">From "tentar falar" to "pedir o caminho em Paris" &mdash; 48 aulas</div>
    <div class="student-info">
      <span>São Paulo, SP</span>
      <span>Nível A1+</span>
      <span>15-16 anos &mdash; Estudante</span>
      <span>3x/semana &middot; 60 min</span>
    </div>
    <div class="progress-passport">
      <div class="progress-label">
        <span>Blocos 1 + 2 &mdash; Aulas 1-5 e 21-25</span>
        <span id="progressPercent">0%</span>
      </div>
      <div class="progress-bar-outer">
        <div class="progress-bar-inner" id="progressBar"></div>
      </div>
    </div>
    <div class="stamps-row">${stamps}</div>
  </div>
</div>

<div class="container">

  <div style="display:flex;align-items:center;gap:8px;justify-content:flex-end;margin-bottom:1rem;padding:8px 0;flex-wrap:wrap;">
    <span style="font-size:0.8rem;color:var(--text-dim);font-weight:500;">Velocidade do áudio:</span>
    <button class="speed-btn" data-speed="0.5" onclick="setAudioSpeed(0.5,this)">0.5x</button>
    <button class="speed-btn" data-speed="0.75" onclick="setAudioSpeed(0.75,this)">0.75x</button>
    <button class="speed-btn active" data-speed="1" onclick="setAudioSpeed(1,this)">1x</button>
    <button class="speed-btn" data-speed="1.25" onclick="setAudioSpeed(1.25,this)">1.25x</button>
  </div>

  <div class="tabs">
    <button class="tab-btn active" onclick="switchTab('planning')">Planejamento</button>
    <button class="tab-btn" onclick="switchTab('exercises')">Pre-class</button>
    <button class="tab-btn" onclick="switchTab('plan')">Plano de Aula</button>
    <button class="tab-btn" onclick="switchTab('teacher')">Material do Professor</button>
    <button class="tab-btn" onclick="switchTab('complementary')">Complementares</button>
  </div>

  ${buildTab1Planning()}

  ${buildTab2PreClass()}

  ${buildTab3Plan()}

  ${buildTab4Material()}

  ${buildTab5Activities()}

</div>

<script>
var audioMap = ${audioMapJSON};
${getCommonJS(D.studentInfo.slug, BLOCK_LESSONS)}
</script>
</body>
</html>`;

  return head + '\n' + body;
}

// ============= MONTAR HTML ALUNO =============
function buildAluno(audioMapJSON) {
  const head = getHeadHTML('Gabriela Pires — Teen English: Paris 2027 | Alumni by Better');
  const stamps = BLOCK_LESSONS.map(n => `<div class="stamp" id="stamp${n}" data-label="${esc(D.stampLabels[n])}" style="background-image:url('${D.stampImages[n]}')"></div>`).join('\n');

  const body = `<body>

<div class="logo-bar">
  <img src="../assets/logo-alumni.png" alt="Alumni by Better">
  <span class="student-badge">Aluna</span>
</div>

<div class="header">
  <div class="header-content">
    <div class="passport-badge">Teen English &mdash; Paris 2027</div>
    <h1>Gabriela Pires</h1>
    <div class="subtitle">De "tentar falar com apoio do português" a "pedir o caminho em Paris sem travar"</div>
    <div class="student-info">
      <span>São Paulo, SP</span>
      <span>Nível A1+</span>
      <span>48 aulas &middot; 60 min</span>
    </div>
    <div class="progress-passport">
      <div class="progress-label"><span>Meu progresso &mdash; Blocos 1 + 2</span><span id="progressPercent">0%</span></div>
      <div class="progress-bar-outer"><div class="progress-bar-inner" id="progressBar"></div></div>
    </div>
    <div class="stamps-row">${stamps}</div>
  </div>
</div>

<div class="container">

  <div style="display:flex;align-items:center;gap:8px;justify-content:flex-end;margin-bottom:1rem;padding:8px 0;flex-wrap:wrap;">
    <span style="font-size:0.8rem;color:var(--text-dim);font-weight:500;">Velocidade do áudio:</span>
    <button class="speed-btn" data-speed="0.5" onclick="setAudioSpeed(0.5,this)">0.5x</button>
    <button class="speed-btn" data-speed="0.75" onclick="setAudioSpeed(0.75,this)">0.75x</button>
    <button class="speed-btn active" data-speed="1" onclick="setAudioSpeed(1,this)">1x</button>
    <button class="speed-btn" data-speed="1.25" onclick="setAudioSpeed(1.25,this)">1.25x</button>
  </div>

  <div class="tabs">
    <button class="tab-btn active" onclick="switchTab('exercises')">Pre-class</button>
    <button class="tab-btn" onclick="switchTab('complementary')">Atividades Complementares</button>
  </div>

  ${buildTab2PreClass().replace('<div class="tab-content"', '<div class="tab-content active"')}

  ${buildTab5Activities()}

</div>

<script>
var audioMap = ${audioMapJSON};
${getCommonJS(D.studentInfo.slug + '-aluna', BLOCK_LESSONS)}
</script>
</body>
</html>`;

  return head + '\n' + body;
}

// ============= EXECUTAR =============
const audioMap = buildAudioMap();
const audioMapJSON = JSON.stringify(audioMap, null, 2);

// Salvar audioMap em json para o gerador de áudio usar
const audioDir = path.resolve(__dirname, `../public/audio/${D.studentInfo.slug}`);
if (!fs.existsSync(audioDir)) fs.mkdirSync(audioDir, { recursive: true });
fs.writeFileSync(path.join(audioDir, 'audioMap.json'), audioMapJSON, 'utf-8');
console.log(`✓ audioMap.json: ${Object.keys(audioMap).length} frases`);

// Professor
const profHTML = buildProfessor(audioMapJSON);
const profPath = path.resolve(__dirname, `../public/professor/${D.studentInfo.slug}.html`);
fs.writeFileSync(profPath, profHTML, 'utf-8');
console.log(`✓ Professor: ${profPath} (${profHTML.split('\n').length} linhas)`);

// Aluno
const alunoHTML = buildAluno(audioMapJSON);
const alunoPath = path.resolve(__dirname, `../public/aluno/${D.studentInfo.slug}.html`);
fs.writeFileSync(alunoPath, alunoHTML, 'utf-8');
console.log(`✓ Aluno: ${alunoPath} (${alunoHTML.split('\n').length} linhas)`);

console.log('\n--- Build complete ---');
console.log(`Professor: https://alumni-plano-gerador.vercel.app/professor/${D.studentInfo.slug}.html`);
console.log(`Aluno:     https://alumni-plano-gerador.vercel.app/aluno/${D.studentInfo.slug}.html`);
