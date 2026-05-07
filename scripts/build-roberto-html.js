#!/usr/bin/env node
/**
 * Build roberto-pires.html (professor + aluno) from content JSON.
 *
 * - Reads scripts/roberto-pires-content.json (the master plan)
 * - Reads scripts/roberto-audio-list.json (380 phrases → mp3 paths)
 * - Reads public/professor/roberto-pires.html (skeleton with placeholders)
 * - Writes:
 *     public/professor/roberto-pires.html (full, 5 tabs)
 *     public/aluno/roberto-pires.html     (full, 2 tabs)
 *
 * Replaces the 4 placeholders:
 *   <!-- TAB-EXERCISES-CONTENT -->     → Pre-class tab
 *   <!-- TAB-PLAN-CONTENT -->          → Plano de Aula tab
 *   <!-- TAB-TEACHER-CONTENT -->       → Material do Professor tab
 *   <!-- TAB-COMPLEMENTARY-CONTENT --> → Complementares tab
 *
 * Also injects the audioMap object into the script section.
 */

const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const CONTENT = JSON.parse(fs.readFileSync(path.join(__dirname, 'roberto-pires-content.json'), 'utf8'));
const AUDIO   = JSON.parse(fs.readFileSync(path.join(__dirname, 'roberto-audio-list.json'),    'utf8'));
const PROF_PATH  = path.join(ROOT, 'public', 'professor', 'roberto-pires.html');
const ALUNO_DIR  = path.join(ROOT, 'public', 'aluno');
const ALUNO_PATH = path.join(ALUNO_DIR, 'roberto-pires.html');

if (!fs.existsSync(ALUNO_DIR)) fs.mkdirSync(ALUNO_DIR, { recursive: true });

// ------------------------------------------------------------------
// helpers
// ------------------------------------------------------------------
function esc(s) {
  return String(s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}
function escAttr(s) { return esc(s).replace(/'/g, '&#39;'); }
function escJs(s) {
  // Escape for use inside a single-quoted JS string literal
  return String(s).replace(/\\/g, '\\\\').replace(/'/g, "\\'");
}
function audioBtn(text, label = 'Ouvir') {
  return `<button class="audio-btn" onclick="speakText('${escJs(text)}', this)" aria-label="Ouvir: ${escAttr(text)}">&#9654; ${label}</button>`;
}
function speechBtn(text) {
  return `<button class="btn btn-listen" onclick="speakText('${escJs(text)}', this)" aria-label="Ouvir: ${escAttr(text)}">&#9654; Ouvir</button>`;
}
function shuffle(arr) {
  const a = arr.slice();
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

// ------------------------------------------------------------------
// AUDIO MAP (phrase → mp3 path)
// ------------------------------------------------------------------
function buildAudioMapJs() {
  const lines = AUDIO.map(item => {
    const k = escJs(item.text);
    const v = `../audio/roberto-pires/${item.filename}`;
    return `    '${k}': '${v}'`;
  });
  return `var audioMap = {\n${lines.join(',\n')}\n  };`;
}

// ------------------------------------------------------------------
// TAB 2 — PRE-CLASS
// ------------------------------------------------------------------
function renderOnboarding() {
  const o = CONTENT.onboarding;
  const phrases = o.frasesEmergencia.map(p => `
    <div class="speech-card" data-phrase="${escAttr(p.en)}">
      <div style="flex:1;min-width:0;">
        <div class="speech-phrase">${esc(p.en)}</div>
        <div class="speech-translation">${esc(p.pt)}</div>
      </div>
      <div class="speech-controls">${speechBtn(p.en)}</div>
    </div>`).join('');
  return `
    <div class="welcome-card">
      <h3>${esc(o.saudacao)}</h3>
      <p>${esc(o.introducao)}</p>
      <blockquote>&ldquo;${esc(o.citacao)}&rdquo;</blockquote>
      <div class="emergency-phrases">
        <h4>5 Frases de Emerg&ecirc;ncia para a viagem</h4>
        <p class="microcopy">Ou&ccedil;a cada uma e tente repetir em voz alta. Essas frases salvam qualquer situa&ccedil;&atilde;o em Barcelona ou Paris.</p>
        ${phrases}
      </div>
      <div style="margin-top:1.2rem;padding:0.8rem 1rem;background:rgba(217,119,6,0.06);border-left:3px solid var(--warn);border-radius:4px;">
        <h4 style="color:var(--warn);font-size:0.7rem;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;margin-bottom:0.4rem;">Desafio leve antes da Aula 1</h4>
        <p style="font-size:0.88rem;color:var(--text);line-height:1.5;">${esc(o.desafioLeve)}</p>
      </div>
    </div>
  `;
}

function renderVocabCards(aula) {
  const cards = aula.vocabulario.map(v => `
    <div class="vocab-card">
      <div class="vocab-card-content">
        <div class="vocab-card-header">
          <span class="vocab-card-word">${esc(v.en)}</span>
          <span class="vocab-card-dot">&middot;</span>
          <span class="vocab-card-translation">${esc(v.pt)}</span>
        </div>
        <div class="vocab-card-example">&ldquo;${esc(v.ex)}&rdquo;</div>
      </div>
      ${audioBtn(v.ex)}
    </div>`).join('');
  return `
    <div class="exercise-section">
      <div class="section-header-row">
        <h4>Vocabul&aacute;rio da aula <span class="badge badge-vocab">Vocabulary</span></h4>
      </div>
      <p class="microcopy">Olha a palavra, a tradu&ccedil;&atilde;o e o exemplo juntos. Toca em Ouvir &mdash; o som ajuda muito a mem&oacute;ria.</p>
      <div class="vocab-cards">${cards}</div>
    </div>
  `;
}

function renderMatching(aula, idx) {
  const exId = `match-l${aula.numero}`;
  const pairs = aula.preClassExercicios.matching;
  const allTranslations = shuffle(pairs.map(p => p.correct));
  const rows = pairs.map((p, i) => {
    const opts = ['<option value="">— select —</option>'].concat(
      allTranslations.map(t => `<option value="${escAttr(t)}">${esc(t)}</option>`)
    ).join('');
    return `
      <div class="match-row" data-answer="${escAttr(p.correct)}">
        <span class="match-word">${esc(p.word)}</span>
        <select onchange="window._handleMatchSelect && window._handleMatchSelect(this)">${opts}</select>
      </div>`;
  }).join('');
  return `
    <div class="exercise-section">
      <div class="section-header-row">
        <h4>V${idx}. Match the words <span class="badge badge-vocab">Vocabulary</span></h4>
      </div>
      <p class="microcopy">Combine cada palavra em ingl&ecirc;s com sua tradu&ccedil;&atilde;o. Errou? Sem problema, leia a explica&ccedil;&atilde;o e tente de novo.</p>
      <div class="match-grid" id="${exId}">${rows}</div>
      <button class="verify-all-btn" onclick="window._verifyMatching && window._verifyMatching('${exId}')">Check answers</button>
      <p class="feedback-msg" id="${exId}-feedback"></p>
    </div>
  `;
}

function renderFillWithHint(aula, idx) {
  const items = aula.preClassExercicios.fillBlankWithHint;
  const blocks = items.map((it, i) => {
    const sentence = it.sentence.replace('___',
      `<input class="blank-input" type="text" data-answer="${escAttr(it.answer)}" data-phrase="${escAttr(it.phrase)}" placeholder="___" autocomplete="off">`);
    return `
      <div class="fill-blank-item">
        <div class="fill-blank-sentence">${sentence}</div>
        <div class="hint-text">Hint: ${esc(it.hint)}</div>
        <button class="check-btn" onclick="window._checkFill && window._checkFill(this)">Check</button>
        <button class="listen-blank-btn" onclick="speakText('${escJs(it.phrase)}', this)">&#9654; Listen</button>
        <p class="feedback-msg"></p>
      </div>`;
  }).join('');
  return `
    <div class="exercise-section">
      <div class="section-header-row">
        <h4>V${idx}. Complete with the correct word <span class="badge badge-vocab">Vocabulary</span></h4>
      </div>
      <p class="microcopy">Escreva a palavra que falta. A dica em ingl&ecirc;s te ajuda. Toque em Listen para ouvir a frase completa.</p>
      ${blocks}
    </div>
  `;
}

function renderFill(aula, idx) {
  const items = aula.preClassExercicios.fillBlank;
  const blocks = items.map(it => {
    const sentence = it.sentence.replace('___',
      `<input class="blank-input" type="text" data-answer="${escAttr(it.answer)}" data-phrase="${escAttr(it.phrase)}" placeholder="___" autocomplete="off">`);
    return `
      <div class="fill-blank-item">
        <div class="fill-blank-sentence">${sentence}</div>
        <button class="check-btn" onclick="window._checkFill && window._checkFill(this)">Check</button>
        <button class="listen-blank-btn" onclick="speakText('${escJs(it.phrase)}', this)">&#9654; Listen</button>
        <p class="feedback-msg"></p>
      </div>`;
  }).join('');
  return `
    <div class="exercise-section">
      <div class="section-header-row">
        <h4>P${idx}. Complete with the correct word (memory) <span class="badge badge-practice">Practice</span></h4>
      </div>
      <p class="microcopy">Sem dicas agora. Lembra do vocabul&aacute;rio l&aacute; em cima? Use!</p>
      ${blocks}
    </div>
  `;
}

function renderQuiz(aula, idx) {
  const items = aula.preClassExercicios.multipleChoice;
  const blocks = items.map((q, i) => {
    const opts = q.options.map((o, j) => `
      <button class="quiz-option" onclick="window._handleQuiz && window._handleQuiz(this, ${j === q.correct})">${String.fromCharCode(65 + j)}. ${esc(o)}</button>`).join('');
    return `
      <div class="quiz-item">
        <div class="quiz-question">${esc(q.q)}</div>
        <div class="quiz-options">${opts}</div>
        <div class="quiz-feedback success" data-feedback="${escAttr(q.feedback)}"></div>
      </div>`;
  }).join('');
  return `
    <div class="exercise-section">
      <div class="section-header-row">
        <h4>P${idx}. Choose the best answer <span class="badge badge-quiz">Quiz</span></h4>
      </div>
      <p class="microcopy">Fa&ccedil;a um de cada vez. Errou? Leia a explica&ccedil;&atilde;o com calma &mdash; &eacute; a&iacute; que voc&ecirc; aprende.</p>
      ${blocks}
    </div>
  `;
}

function renderOrdering(aula, idx) {
  const o = aula.preClassExercicios.ordering;
  if (!o) return '';
  const exId = `order-l${aula.numero}`;
  const items = o.shuffled.map((it, i) => `
    <div class="ordering-item" data-text="${escAttr(it)}">
      <span>${esc(it)}</span>
      <div class="ordering-controls">
        <button class="order-btn" onclick="window._orderMove && window._orderMove(this, -1)" aria-label="Mover para cima">&#9650;</button>
        <button class="order-btn" onclick="window._orderMove && window._orderMove(this, 1)" aria-label="Mover para baixo">&#9660;</button>
      </div>
    </div>`).join('');
  return `
    <div class="exercise-section">
      <div class="section-header-row">
        <h4>P${idx}. Put in order <span class="badge badge-practice">Practice</span></h4>
      </div>
      <p class="microcopy">${esc(o.instructions)}</p>
      <div class="ordering-list" id="${exId}" data-correct="${escAttr(o.correct.join('|'))}">${items}</div>
      <button class="verify-all-btn" onclick="window._verifyOrder && window._verifyOrder('${exId}')">Check order</button>
      <p class="feedback-msg" id="${exId}-feedback"></p>
    </div>
  `;
}

function renderPronunciation(aula, idx) {
  const items = aula.preClassExercicios.pronunciation;
  const blocks = items.map((p, i) => {
    const id = `pron-l${aula.numero}-${i}`;
    return `
      <div class="pron-card" id="${id}" data-target="${escAttr(p.phrase)}">
        <div class="pron-target">${esc(p.phrase)}</div>
        <div class="pron-ipa">${esc(p.ipa)}</div>
        <div class="pron-controls">
          <button class="pron-btn" onclick="speakText('${escJs(p.phrase)}', this)">&#9654; Listen</button>
          <button class="pron-btn" style="background:var(--warn);" onclick="window._pronRecord && window._pronRecord('${id}', this)">&#127908; Record</button>
        </div>
        <div class="pron-result" id="${id}-result"></div>
      </div>`;
  }).join('');
  return `
    <div class="exercise-section">
      <div class="section-header-row">
        <h4>P${idx}. Read aloud <span class="badge badge-practice">Pronunciation</span></h4>
      </div>
      <p class="microcopy">Toque em Listen, ou&ccedil;a, e depois em Record. Fale a frase e veja como sua pron&uacute;ncia se compara &mdash; cada palavra colorida verde voc&ecirc; acertou.</p>
      ${blocks}
    </div>
  `;
}

function renderThink(aula, idx) {
  const q = aula.preClassExercicios.thinkAboutIt;
  const id = `think-l${aula.numero}`;
  return `
    <div class="exercise-section">
      <div class="section-header-row">
        <h4>T${idx}. Think about it <span class="badge badge-quiz">Reflection</span></h4>
      </div>
      <p class="microcopy">Aqui n&atilde;o tem resposta certa &mdash; &eacute; pra voc&ecirc; pensar em ingl&ecirc;s. Toque no microfone e responda como vier.</p>
      <div class="think-card">
        <div class="think-question">${esc(q)}</div>
        <div class="think-controls">
          <button class="think-btn" id="${id}-btn" onclick="window._thinkRecord && window._thinkRecord('${id}', this)">&#127908; Record your thought</button>
          <button class="think-btn" style="background:var(--text-mid);" onclick="window._thinkPlay && window._thinkPlay('${id}')">&#9654; Play back</button>
        </div>
      </div>
    </div>
  `;
}

function renderSurvivalCard(aula) {
  if (!aula.survivalCard) return '';
  const lines = aula.survivalCard.linhas.map(l => `
    <div class="survival-line" data-phrase="${escAttr(l.en)}">
      <div style="flex:1;min-width:0;">
        <div class="survival-en">${esc(l.en)}</div>
        <div class="survival-pt">${esc(l.pt)}</div>
      </div>
      ${audioBtn(l.en, '')}
    </div>`).join('');
  return `
    <div class="survival-card">
      <h4>${esc(aula.survivalCard.titulo)}</h4>
      ${lines}
    </div>
  `;
}

function renderLessonPreClass(aula) {
  return `
    <div class="lesson-card" id="lesson-${aula.numero}-pre">
      <div class="lesson-header" onclick="toggleLesson(this.parentElement)">
        <div class="lesson-num">${String(aula.numero).padStart(2,'0')}</div>
        <div class="lesson-title-area">
          <div class="lesson-title">${esc(aula.tema)}</div>
          <div class="lesson-subtitle">${esc(aula.subtema)}</div>
        </div>
        <div class="lesson-toggle">&#9656;</div>
      </div>
      <div class="lesson-body">
        <div class="promise-bar">
          <h5>Promessa desta aula</h5>
          <p>${esc(aula.promessa)}</p>
        </div>
        ${renderVocabCards(aula)}
        ${renderMatching(aula, 1)}
        ${renderFillWithHint(aula, 2)}
        ${renderFill(aula, 1)}
        ${renderQuiz(aula, 2)}
        ${renderOrdering(aula, 3)}
        ${renderPronunciation(aula, 4)}
        ${renderThink(aula, 1)}
        ${renderSurvivalCard(aula)}
      </div>
    </div>
  `;
}

function buildTabExercises() {
  const lessons = CONTENT.aulas.map(renderLessonPreClass).join('');
  const placeholders = [];
  for (let i = 6; i <= 20; i++) {
    placeholders.push(`
      <div class="lesson-card" style="opacity:0.55;">
        <div class="lesson-header" style="cursor:default;">
          <div class="lesson-num">${String(i).padStart(2,'0')}</div>
          <div class="lesson-title-area">
            <div class="lesson-title">Aula ${i}</div>
            <div class="lesson-subtitle"><em>Conte&uacute;do ser&aacute; adicionado no pr&oacute;ximo bloco</em></div>
          </div>
        </div>
      </div>`);
  }
  return `
    ${renderOnboarding()}
    <h2 style="margin-top:2rem;">Exerc&iacute;cios pr&eacute;-aula &mdash; Aulas 1 a 5</h2>
    <p class="intro-text">Cada aula vem com um conjunto fechado de exerc&iacute;cios para ativar o vocabul&aacute;rio antes do encontro com o professor. Fa&ccedil;a com calma. N&atilde;o &eacute; prova.</p>
    ${lessons}
    <h3 style="margin-top:2rem;color:var(--text-dim);">Aulas 6 a 20</h3>
    ${placeholders.join('')}
  `;
}

// ------------------------------------------------------------------
// TAB 3 — PLANO DE AULA (PPP minute-by-minute + Teacher Guide)
// ------------------------------------------------------------------
function renderLessonPlan(aula) {
  const rows = aula.planoDeAulaPPP.map(r => `
    <tr>
      <td class="time-cell">${esc(r.tempo)}</td>
      <td class="activity-cell">${esc(r.fase)}</td>
      <td>${esc(r.atividade)}</td>
    </tr>`).join('');
  const ccqs = aula.gramaticaFoco.ccqs.map(c => `
    <div class="ccq-box">
      <div class="ccq-q">CCQ: ${esc(c.q)}</div>
      <div class="ccq-a">Resposta esperada: ${esc(c.a)}</div>
    </div>`).join('');
  const obstacles = aula.alertasObstaculo.map(o => `
    <div class="obstacle-alert">
      <h6>Alerta de obst&aacute;culo</h6>
      <p><span class="obstacle-where">Onde:</span> ${esc(o.ondeOcorre)}</p>
      <p><strong>Obst&aacute;culo:</strong> ${esc(o.obstaculo)}</p>
      <p><strong>Solu&ccedil;&atilde;o:</strong> ${esc(o.solucao)}</p>
    </div>`).join('');
  const blocos = aula.blocosDominados.map(b => `<li>${esc(b)}</li>`).join('');
  const callback = aula.callbackAulaAnterior ? `
    <div class="teacher-tip">
      <h6>Callback da aula anterior</h6>
      <p>${esc(aula.callbackAulaAnterior)}</p>
    </div>` : '';
  return `
    <div class="lesson-card" id="lesson-${aula.numero}-plan">
      <div class="lesson-header" onclick="toggleLesson(this.parentElement)">
        <div class="lesson-num">${String(aula.numero).padStart(2,'0')}</div>
        <div class="lesson-title-area">
          <div class="lesson-title">${esc(aula.tema)}</div>
          <div class="lesson-subtitle">${esc(aula.subtema)}</div>
        </div>
        <div class="lesson-toggle">&#9656;</div>
      </div>
      <div class="lesson-body">
        <div class="promise-bar">
          <h5>Crit&eacute;rio de sucesso</h5>
          <p>${esc(aula.criterioSucesso)}</p>
        </div>
        ${callback}
        <h3 style="margin-top:1rem;">Roteiro PPP minuto a minuto (60 min)</h3>
        <table class="plan-table">
          <thead>
            <tr><th>Tempo</th><th>Fase</th><th>Atividade do professor</th></tr>
          </thead>
          <tbody>${rows}</tbody>
        </table>

        <h3 style="margin-top:1.2rem;">Foco gramatical</h3>
        <div class="teacher-tip">
          <h6>Estrutura</h6>
          <p>${esc(aula.gramaticaFoco.estrutura)}</p>
          <p style="margin-top:0.4rem;"><strong>Modelo:</strong> ${esc(aula.gramaticaFoco.modelo)}</p>
        </div>
        <h3 style="margin-top:1rem;font-size:1.05rem;">Concept Check Questions (j&aacute; escritas, n&atilde;o improvisar)</h3>
        ${ccqs}

        <h3 style="margin-top:1.2rem;">Antecipa&ccedil;&atilde;o de obst&aacute;culos</h3>
        ${obstacles}

        <h3 style="margin-top:1.2rem;">Blocos de linguagem que o aluno sair&aacute; dominando</h3>
        <ul style="padding-left:1.2rem;font-size:0.92rem;color:var(--text-mid);line-height:1.7;">${blocos}</ul>

        <h3 style="margin-top:1.2rem;">Homework para a pr&oacute;xima aula</h3>
        <p style="font-size:0.92rem;color:var(--text);background:var(--bg-elevated);padding:0.9rem 1.1rem;border-radius:8px;border-left:3px solid var(--warn);">${esc(aula.homework)}</p>
      </div>
    </div>
  `;
}

function buildTabPlan() {
  const lessons = CONTENT.aulas.map(renderLessonPlan).join('');
  const placeholders = [];
  for (let i = 6; i <= 20; i++) {
    placeholders.push(`
      <div class="lesson-card" style="opacity:0.55;">
        <div class="lesson-header" style="cursor:default;">
          <div class="lesson-num">${String(i).padStart(2,'0')}</div>
          <div class="lesson-title-area">
            <div class="lesson-title">Aula ${i}</div>
            <div class="lesson-subtitle"><em>Conte&uacute;do ser&aacute; adicionado no pr&oacute;ximo bloco</em></div>
          </div>
        </div>
      </div>`);
  }
  return `
    <h2>Plano de Aula &mdash; Aulas 1 a 5</h2>
    <p class="intro-text">Roteiro PPP minuto a minuto, CCQs prontas e antecipa&ccedil;&atilde;o de obst&aacute;culos espec&iacute;ficos do Roberto. Use durante a aula como guia &mdash; o conte&uacute;do visual fica na aba <strong>Material do Professor</strong>.</p>
    ${lessons}
    <h3 style="margin-top:2rem;color:var(--text-dim);">Aulas 6 a 20</h3>
    ${placeholders.join('')}
  `;
}

// ------------------------------------------------------------------
// TAB 4 — MATERIAL DO PROFESSOR (tela compartilhada)
// ------------------------------------------------------------------
function renderTeacherWarmUp(aula) {
  const items = aula.materialProfessorExercicios.warmUp.map(q => `<li>${esc(q)}</li>`).join('');
  return `
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:8px;padding:1rem 1.2rem;margin:1rem 0;">
      <h4 style="font-size:0.78rem;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:var(--accent);margin-bottom:0.6rem;">1. Warm-up &middot; 5 perguntas (5 min)</h4>
      <ul style="padding-left:1.2rem;font-size:0.92rem;color:var(--text);line-height:1.8;">${items}</ul>
    </div>
  `;
}

function renderTeacherVocab(aula) {
  // Diferentes do Pre-class — frases-modelo do material
  const cards = aula.materialProfessorExercicios.vocabularyContextSentences.map(v => `
    <div class="vocab-card">
      <div class="vocab-card-content">
        <div class="vocab-card-header">
          <span class="vocab-card-word">${esc(v.word)}</span>
        </div>
        <div class="vocab-card-example">&ldquo;${esc(v.sentence)}&rdquo;</div>
      </div>
      ${audioBtn(v.sentence)}
    </div>`).join('');
  return `
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:8px;padding:1rem 1.2rem;margin:1rem 0;">
      <h4 style="font-size:0.78rem;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:var(--accent);margin-bottom:0.6rem;">2. Vocabulary in context (10 min)</h4>
      <p class="microcopy">Cada palavra reaparece numa frase nova &mdash; n&atilde;o &eacute; o exemplo do pre-class. Apresente, leia em voz alta, pe&ccedil;a Roberto para repetir.</p>
      <div class="vocab-cards">${cards}</div>
    </div>
  `;
}

function renderTeacherDialogue(aula) {
  const d = aula.materialProfessorExercicios.dialogue;
  if (!d) return '';
  const lines = d.lines.map(l => {
    const isYou = l.speaker === 'ROBERTO';
    const avatarClass = isYou ? 'avatar-you' : 'avatar-staff';
    const bubbleClass = isYou ? 'dialogue-bubble your-turn' : 'dialogue-bubble';
    return `
      <div class="dialogue-line">
        <div class="dialogue-avatar ${avatarClass}">${esc(l.speaker.slice(0,3))}</div>
        <div class="${bubbleClass}" data-phrase="${escAttr(l.text)}">
          <div style="flex:1;min-width:0;">
            <div class="speaker-name">${esc(l.speaker)}</div>
            <div class="dialogue-text">${esc(l.text)}</div>
          </div>
          ${audioBtn(l.text, '')}
        </div>
      </div>`;
  }).join('');
  const qs = aula.materialProfessorExercicios.listeningQuestions.map(q => `<li>${esc(q.q)}</li>`).join('');
  return `
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:8px;padding:1rem 1.2rem;margin:1rem 0;">
      <h4 style="font-size:0.78rem;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:var(--accent);margin-bottom:0.6rem;">3. Context dialogue (8 min)</h4>
      <p style="font-size:0.92rem;font-weight:600;color:var(--text);margin-bottom:0.6rem;">${esc(d.title)}</p>
      <div class="dialogue-container">${lines}</div>
      <h5 style="font-size:0.78rem;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:var(--text-dim);margin:1rem 0 0.4rem;">Listening comprehension &mdash; perguntas para o aluno</h5>
      <ul style="padding-left:1.2rem;font-size:0.9rem;color:var(--text);line-height:1.8;">${qs}</ul>
    </div>
  `;
}

function renderTeacherGrammar(aula) {
  const g = aula.gramaticaFoco;
  const examples = g.exemplos.map(e => `<li>${esc(e)} ${audioBtn(e, '')}</li>`).join('');
  return `
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:8px;padding:1rem 1.2rem;margin:1rem 0;">
      <h4 style="font-size:0.78rem;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:var(--accent);margin-bottom:0.6rem;">4. Grammar focus (8 min)</h4>
      <p style="font-size:0.92rem;color:var(--text);margin-bottom:0.4rem;"><strong>Estrutura:</strong> ${esc(g.estrutura)}</p>
      <p style="font-size:0.92rem;color:var(--text-mid);margin-bottom:0.6rem;font-family:'Cormorant Garamond',serif;font-style:italic;">${esc(g.modelo)}</p>
      <ul style="list-style:none;padding-left:0;display:flex;flex-direction:column;gap:0.3rem;">${examples}</ul>
    </div>
  `;
}

function renderTeacherDrilling(aula) {
  const rows = aula.materialProfessorExercicios.oralDrillingPrompts.map(p => `
    <tr><td class="pt-cell">${esc(p.pt)}</td><td class="en-cell">${esc(p.en)} ${audioBtn(p.en, '')}</td></tr>`).join('');
  return `
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:8px;padding:1rem 1.2rem;margin:1rem 0;">
      <h4 style="font-size:0.78rem;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:var(--accent);margin-bottom:0.6rem;">5. Practice &mdash; oral drilling (8 min)</h4>
      <p class="microcopy">Voc&ecirc; diz a situa&ccedil;&atilde;o em portugu&ecirc;s, Roberto produz a frase em ingl&ecirc;s. Sem tempo para pensar &mdash; quanto mais autom&aacute;tico, melhor.</p>
      <table class="drilling-table">
        <thead><tr><th>Voc&ecirc; diz (PT)</th><th>Roberto produz (EN)</th></tr></thead>
        <tbody>${rows}</tbody>
      </table>
    </div>
  `;
}

function renderTeacherErrorCorrection(aula) {
  const rows = aula.materialProfessorExercicios.errorCorrection.map(e => `
    <tr>
      <td class="wrong-cell">${esc(e.wrong)}</td>
      <td class="right-cell">${esc(e.right)} ${audioBtn(e.right, '')}</td>
      <td class="note-cell">${esc(e.note)}</td>
    </tr>`).join('');
  return `
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:8px;padding:1rem 1.2rem;margin:1rem 0;">
      <h4 style="font-size:0.78rem;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:var(--accent);margin-bottom:0.6rem;">6. Error correction (5 min)</h4>
      <p class="microcopy">Erros recorrentes do A2 brasileiro &mdash; reformule no momento, com gentileza.</p>
      <table class="error-table">
        <tbody>${rows}</tbody>
      </table>
    </div>
  `;
}

function renderTeacherSubstitution(aula) {
  const s = aula.materialProfessorExercicios.substitutionDrill;
  if (!s) return '';
  const subs = s.substituicoes.map(sub => {
    const rendered = s.modelo.replace('___', sub);
    return `<li>${esc(rendered)} ${audioBtn(rendered, '')}</li>`;
  }).join('');
  return `
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:8px;padding:1rem 1.2rem;margin:1rem 0;">
      <h4 style="font-size:0.78rem;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:var(--accent);margin-bottom:0.6rem;">7. Substitution drill (3 min)</h4>
      <p style="font-size:0.92rem;color:var(--text);margin-bottom:0.4rem;"><strong>Modelo:</strong> ${esc(s.modelo)}</p>
      <p class="microcopy">Voc&ecirc; varia o complemento, Roberto adapta a frase inteira preservando a estrutura.</p>
      <ul style="list-style:none;padding-left:0;display:flex;flex-direction:column;gap:0.3rem;font-size:0.9rem;color:var(--text);">${subs}</ul>
    </div>
  `;
}

function renderTeacherRolePlays(aula) {
  const plays = aula.materialProfessorExercicios.rolePlays.map(rp => `
    <div class="scenario-card">
      <span class="scenario-tag">Role-play &middot; ${esc(rp.tipo)}</span>
      <h5>${esc(rp.titulo)}</h5>
      <p><strong>Cen&aacute;rio:</strong> ${esc(rp.prompt)}</p>
      <p style="margin-top:0.3rem;"><strong>Output esperado:</strong> <em>${esc(rp.esperado)}</em></p>
    </div>`).join('');
  return `
    <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:8px;padding:1rem 1.2rem;margin:1rem 0;">
      <h4 style="font-size:0.78rem;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:var(--accent);margin-bottom:0.6rem;">8. Production &mdash; role-plays guided &rarr; semi-free &rarr; free (12 min)</h4>
      <p class="microcopy">Rampa progressiva. Em dia ruim, fique mais tempo no guided. Em dia bom, avance r&aacute;pido para o free.</p>
      ${plays}
    </div>
  `;
}

function renderTeacherChecklist(aula) {
  const items = aula.materialProfessorExercicios.checklistAprendi.map((c, i) => `
    <label><input type="checkbox" data-key="aula${aula.numero}-check${i}"> ${esc(c)}</label>`).join('');
  return `
    <div class="checklist">
      <h4>Checklist &ldquo;O que eu aprendi&rdquo; &mdash; Aula ${aula.numero}</h4>
      <p class="microcopy">Leia cada frase em voz alta. Se conseguir dizer &ldquo;sim, eu sei fazer isso&rdquo; pra todas, fechou &mdash; a li&ccedil;&atilde;o t&aacute; dominada.</p>
      ${items}
    </div>
  `;
}

function renderLessonTeacher(aula) {
  return `
    <div class="lesson-card" id="lesson-${aula.numero}-teacher">
      <div class="lesson-header" onclick="toggleLesson(this.parentElement)">
        <div class="lesson-num">${String(aula.numero).padStart(2,'0')}</div>
        <div class="lesson-title-area">
          <div class="lesson-title">${esc(aula.tema)}</div>
          <div class="lesson-subtitle">${esc(aula.subtema)}</div>
        </div>
        <div class="lesson-toggle">&#9656;</div>
      </div>
      <div class="lesson-body">
        <div class="promise-bar">
          <h5>Promessa desta aula</h5>
          <p>${esc(aula.promessa)}</p>
        </div>
        ${renderTeacherWarmUp(aula)}
        ${renderTeacherVocab(aula)}
        ${renderTeacherDialogue(aula)}
        ${renderTeacherGrammar(aula)}
        ${renderTeacherDrilling(aula)}
        ${renderTeacherSubstitution(aula)}
        ${renderTeacherErrorCorrection(aula)}
        ${renderTeacherRolePlays(aula)}
        ${renderSurvivalCard(aula)}
        ${renderTeacherChecklist(aula)}
      </div>
    </div>
  `;
}

function buildTabTeacher() {
  const lessons = CONTENT.aulas.map(renderLessonTeacher).join('');
  const placeholders = [];
  for (let i = 6; i <= 20; i++) {
    placeholders.push(`
      <div class="lesson-card" style="opacity:0.55;">
        <div class="lesson-header" style="cursor:default;">
          <div class="lesson-num">${String(i).padStart(2,'0')}</div>
          <div class="lesson-title-area">
            <div class="lesson-title">Aula ${i}</div>
            <div class="lesson-subtitle"><em>Conte&uacute;do ser&aacute; adicionado no pr&oacute;ximo bloco</em></div>
          </div>
        </div>
      </div>`);
  }
  return `
    <h2>Material do Professor &mdash; tela compartilhada</h2>
    <p class="intro-text">Esta &eacute; a tela que voc&ecirc; mostra para o Roberto na aula. Sem tradu&ccedil;&otilde;es, sem gabaritos. As respostas e instru&ccedil;&otilde;es ficam na aba <strong>Plano de Aula</strong>. Cada aula segue 8 fases na ordem PPP.</p>
    ${lessons}
    <h3 style="margin-top:2rem;color:var(--text-dim);">Aulas 6 a 20</h3>
    ${placeholders.join('')}
  `;
}

// ------------------------------------------------------------------
// TAB 5 — COMPLEMENTARES
// ------------------------------------------------------------------
const TYPE_TO_THUMB = {
  'Filme': 'movie',
  'Série': 'serie',
  'Serie': 'serie',
  'YouTube': 'youtube',
  'Podcast': 'podcast',
  'Documentário': 'documentary',
  'Documentario': 'documentary',
  'App': 'app',
};

function renderLessonComplementary(aula) {
  const cards = aula.complementares.map(c => `
    <div class="media-card">
      <div class="media-thumb ${TYPE_TO_THUMB[c.tipo] || 'movie'}"></div>
      <div class="media-info">
        <div class="media-type">${esc(c.tipo)}</div>
        <h5>${esc(c.titulo)}</h5>
        <p>${esc(c.descricao)}</p>
        <div class="media-tip">${esc(c.tip)}</div>
      </div>
    </div>`).join('');
  return `
    <div class="lesson-card" id="lesson-${aula.numero}-comp">
      <div class="lesson-header" onclick="toggleLesson(this.parentElement)">
        <div class="lesson-num">${String(aula.numero).padStart(2,'0')}</div>
        <div class="lesson-title-area">
          <div class="lesson-title">${esc(aula.tema)}</div>
          <div class="lesson-subtitle">${esc(aula.subtema)}</div>
        </div>
        <div class="lesson-toggle">&#9656;</div>
      </div>
      <div class="lesson-body">
        <div class="media-grid">${cards}</div>
      </div>
    </div>
  `;
}

function buildTabComplementary() {
  const lessons = CONTENT.aulas.map(renderLessonComplementary).join('');
  return `
    <h2>Atividades Complementares</h2>
    <p class="intro-text">Filmes, s&eacute;ries, canais e podcasts curados para cada aula. N&atilde;o &eacute; obriga&ccedil;&atilde;o &mdash; &eacute; combust&iacute;vel pra quando voc&ecirc; tiver fome de mais ingl&ecirc;s entre as aulas.</p>
    ${lessons}
  `;
}

// ------------------------------------------------------------------
// JS HELPERS injected (handlers for FAAP-style exercises)
// ------------------------------------------------------------------
const EXERCISE_JS = `
  // Matching dropdown
  window._handleMatchSelect = function(sel) {
    var row = sel.closest('.match-row');
    if (sel.value === row.dataset.answer) row.classList.add('correct'), row.classList.remove('incorrect');
    else if (sel.value) row.classList.add('incorrect'), row.classList.remove('correct');
  };
  window._verifyMatching = function(id) {
    var grid = document.getElementById(id);
    var rows = grid.querySelectorAll('.match-row');
    var ok = 0, total = rows.length;
    rows.forEach(r => {
      var sel = r.querySelector('select');
      if (sel.value === r.dataset.answer) { r.classList.add('correct'); r.classList.remove('incorrect'); ok++; }
      else { r.classList.add('incorrect'); }
    });
    var fb = document.getElementById(id + '-feedback');
    if (fb) {
      fb.className = 'feedback-msg ' + (ok === total ? 'success' : 'error');
      fb.innerText = ok === total ? 'Boa! Acertou todas.' : 'Voc&ecirc; acertou ' + ok + ' de ' + total + '. Revise as vermelhas e tente de novo.';
    }
  };
  // Fill blank
  window._checkFill = function(btn) {
    var item = btn.closest('.fill-blank-item');
    var inp = item.querySelector('.blank-input');
    var fb = item.querySelector('.feedback-msg');
    var v = (inp.value || '').trim().toLowerCase();
    var a = (inp.dataset.answer || '').trim().toLowerCase();
    if (v === a) {
      inp.classList.add('correct'); inp.classList.remove('incorrect');
      fb.className = 'feedback-msg success'; fb.innerText = 'Perfeito!';
    } else {
      inp.classList.add('incorrect'); inp.classList.remove('correct');
      fb.className = 'feedback-msg error';
      fb.innerText = 'Quase. A resposta &eacute; "' + (inp.dataset.answer || '') + '". Tente de novo.';
    }
  };
  // Quiz
  window._handleQuiz = function(btn, isCorrect) {
    var item = btn.closest('.quiz-item');
    var fb = item.querySelector('.quiz-feedback');
    item.querySelectorAll('.quiz-option').forEach(o => o.classList.remove('correct','incorrect'));
    if (isCorrect) {
      btn.classList.add('correct');
      fb.classList.add('show');
      fb.innerText = 'Boa! ' + (fb.dataset.feedback || '');
    } else {
      btn.classList.add('incorrect');
      // Mark correct answer
      var opts = item.querySelectorAll('.quiz-option');
      // The correct one is found via onclick attr containing 'true'
      opts.forEach(o => { if ((o.getAttribute('onclick')||'').match(/, true\\)/)) o.classList.add('correct'); });
      fb.classList.add('show');
      fb.innerText = 'Quase. ' + (fb.dataset.feedback || '');
    }
  };
  // Ordering
  window._orderMove = function(btn, dir) {
    var item = btn.closest('.ordering-item');
    var list = item.parentElement;
    var sib = dir < 0 ? item.previousElementSibling : item.nextElementSibling;
    if (sib) {
      if (dir < 0) list.insertBefore(item, sib);
      else list.insertBefore(sib, item);
    }
  };
  window._verifyOrder = function(id) {
    var list = document.getElementById(id);
    var correct = (list.dataset.correct || '').split('|');
    var items = list.querySelectorAll('.ordering-item');
    var ok = true;
    items.forEach((it, i) => {
      if ((it.dataset.text || '') === correct[i]) it.classList.add('correct');
      else { it.classList.remove('correct'); ok = false; }
    });
    var fb = document.getElementById(id + '-feedback');
    if (fb) {
      fb.className = 'feedback-msg ' + (ok ? 'success' : 'error');
      fb.innerText = ok ? 'Perfeito! Ordem correta.' : 'Ainda n&atilde;o. Continue ajustando.';
    }
  };
  // Pronunciation (Web Speech recognition)
  window._pronRecord = function(id, btn) {
    var card = document.getElementById(id);
    var target = (card.dataset.target || '').toLowerCase();
    var resBox = document.getElementById(id + '-result');
    var SR = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SR) {
      resBox.classList.add('show');
      resBox.innerText = 'Seu navegador n&atilde;o tem reconhecimento de fala. Use Chrome.';
      return;
    }
    var rec = new SR();
    rec.lang = 'en-US';
    rec.interimResults = false;
    rec.maxAlternatives = 1;
    btn.style.background = 'var(--danger)'; btn.innerText = '&#127908; Listening...';
    rec.onresult = function(ev) {
      var said = (ev.results[0][0].transcript || '').toLowerCase().trim();
      var targetWords = target.replace(/[^a-z'\\s]/g,'').split(/\\s+/);
      var saidWords = said.replace(/[^a-z'\\s]/g,'').split(/\\s+/);
      var html = targetWords.map((w, i) => {
        var hit = saidWords.includes(w);
        return '<span class="pron-word-' + (hit ? 'correct' : 'wrong') + '">' + w + '</span>';
      }).join(' ');
      var hits = targetWords.filter(w => saidWords.includes(w)).length;
      resBox.classList.add('show');
      resBox.innerHTML = '<strong>You said:</strong> ' + said + '<br><strong>Score:</strong> ' + hits + '/' + targetWords.length + '<br>' + html;
    };
    rec.onend = function() {
      btn.style.background = 'var(--warn)';
      btn.innerHTML = '&#127908; Record again';
    };
    rec.onerror = function() {
      resBox.classList.add('show');
      resBox.innerText = 'Microfone n&atilde;o autorizado ou erro. Permita o acesso e tente de novo.';
      btn.style.background = 'var(--warn)';
      btn.innerHTML = '&#127908; Record';
    };
    rec.start();
  };
  // Think (record + play with localStorage as base64 fallback)
  window._thinkRecord = function(id, btn) {
    if (!navigator.mediaDevices || !window.MediaRecorder) {
      alert('Seu navegador n&atilde;o suporta grava&ccedil;&atilde;o. Use Chrome ou Edge.');
      return;
    }
    if (btn.classList.contains('recording')) {
      // Stop
      window['_thinkRec_' + id].stop();
      return;
    }
    navigator.mediaDevices.getUserMedia({audio: true}).then(stream => {
      var rec = new MediaRecorder(stream);
      var chunks = [];
      rec.ondataavailable = e => chunks.push(e.data);
      rec.onstop = () => {
        var blob = new Blob(chunks, {type: 'audio/webm'});
        var url = URL.createObjectURL(blob);
        window['_thinkBlob_' + id] = url;
        btn.classList.remove('recording');
        btn.innerHTML = '&#127908; Record again';
        stream.getTracks().forEach(t => t.stop());
      };
      rec.start();
      btn.classList.add('recording');
      btn.innerHTML = '&#9209; Stop';
      window['_thinkRec_' + id] = rec;
    }).catch(() => alert('Permiss&atilde;o do microfone negada.'));
  };
  window._thinkPlay = function(id) {
    var url = window['_thinkBlob_' + id];
    if (!url) { alert('Voc&ecirc; ainda n&atilde;o gravou.'); return; }
    new Audio(url).play();
  };
`;

// ------------------------------------------------------------------
// ASSEMBLY
// ------------------------------------------------------------------
function buildProfessor() {
  let html = fs.readFileSync(PROF_PATH, 'utf8');
  html = html.replace('<!-- TAB-EXERCISES-CONTENT -->',     buildTabExercises());
  html = html.replace('<!-- TAB-PLAN-CONTENT -->',           buildTabPlan());
  html = html.replace('<!-- TAB-TEACHER-CONTENT -->',        buildTabTeacher());
  html = html.replace('<!-- TAB-COMPLEMENTARY-CONTENT -->',  buildTabComplementary());
  // Inject audioMap
  html = html.replace('var audioMap = {};', buildAudioMapJs());
  // Append exercise handlers JS
  html = html.replace('// ============== AUDIO MAP', EXERCISE_JS + '\n  // ============== AUDIO MAP');
  fs.writeFileSync(PROF_PATH, html, 'utf8');
  console.log('Professor: wrote', PROF_PATH, '(' + html.length + ' bytes)');
}

function buildAluno() {
  // Aluno = professor sem Aba 1 (Planejamento), Aba 3 (Plano de Aula), Aba 4 (Material do Professor)
  // Mantém: Pre-class + Complementares
  let html = fs.readFileSync(PROF_PATH, 'utf8');
  // Replace title
  html = html.replace(/<title>.*?<\/title>/, '<title>Roberto Pires — Travel English | Alumni by Better</title>');
  // Replace prof badge with aluno badge
  html = html.replace('<span class="prof-badge">Professor</span>', '<span class="prof-badge" style="background:var(--accent-light);">Aluno</span>');
  // Remove planning tab button + content
  html = html.replace(/<button class="tab-btn active" onclick="switchTab\('planning'\)">Planejamento<\/button>/, '');
  html = html.replace(/<div class="tab-content active" id="tab-planning">[\s\S]*?<!-- ===================== PLACEHOLDER PARA OUTRAS ABAS =====================/, '<!-- ===================== STUDENT TABS =====================');
  // Remove plan tab button + content
  html = html.replace(/<button class="tab-btn" onclick="switchTab\('plan'\)">Plano de Aula<\/button>/, '');
  html = html.replace(/<div class="tab-content" id="tab-plan">[\s\S]*?<\/div>\s*<div class="tab-content" id="tab-teacher">/, '<div class="tab-content" id="tab-teacher" style="display:none;">');
  // Remove teacher tab button + content
  html = html.replace(/<button class="tab-btn" onclick="switchTab\('teacher'\)">Material do Professor<\/button>/, '');
  html = html.replace(/<div class="tab-content" id="tab-teacher"[^>]*>[\s\S]*?<\/div>\s*<div class="tab-content" id="tab-complementary">/, '<div class="tab-content" id="tab-complementary">');
  // Make exercises tab the active default
  html = html.replace('<button class="tab-btn" onclick="switchTab(\'exercises\')">Pre-class</button>',
                      '<button class="tab-btn active" onclick="switchTab(\'exercises\')">Pre-class</button>');
  html = html.replace('<div class="tab-content" id="tab-exercises">', '<div class="tab-content active" id="tab-exercises">');
  // Update components path (from public/professor/ to public/aluno/ both go up one level — same path)
  // Update progress bar storage key isolation
  html = html.replace("var STORAGE_KEY = 'roberto-pires-progress-v1'", "var STORAGE_KEY = 'roberto-pires-aluno-progress-v1'");
  fs.writeFileSync(ALUNO_PATH, html, 'utf8');
  console.log('Aluno: wrote', ALUNO_PATH, '(' + html.length + ' bytes)');
}

// Run
buildProfessor();
buildAluno();
console.log('Done.');
