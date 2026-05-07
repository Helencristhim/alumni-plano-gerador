#!/usr/bin/env node
/**
 * Build roberto-pires.html (professor + aluno) following CLAUDE.md rules 1-26.
 *
 * - REGRA 7  : audioMap with absolute paths /audio/{slug}/...
 * - REGRA 9  : canonical global handlers (checkBlank, selectQuiz, verifyAllMatches, etc.)
 * - REGRA 4  : 5 mandatory steps per lesson on Pre-class
 * - REGRA 15 : lesson-card with .lesson-header-img, .lesson-progress-mini
 * - REGRA 16 : survival-phrase with .sp-num/.sp-en/.sp-pt
 * - REGRA 18 : storage keys alumni-progress-{slug}, {slug}-professor / {slug}-aluno
 * - REGRA 19 : material.css linked absolute /styles/material.css
 * - REGRA 26 : canonical JS block copied verbatim
 */

const fs = require('fs');
const path = require('path');

const ROOT     = path.join(__dirname, '..');
const CONTENT  = JSON.parse(fs.readFileSync(path.join(__dirname, 'roberto-pires-content.json'), 'utf8'));
const AUDIO    = JSON.parse(fs.readFileSync(path.join(__dirname, 'roberto-audio-list.json'),    'utf8'));
const SLUG     = 'roberto-pires';
const PROF_OUT = path.join(ROOT, 'public', 'professor', `${SLUG}.html`);
const ALUNO_DIR = path.join(ROOT, 'public', 'aluno');
const ALUNO_OUT = path.join(ALUNO_DIR, `${SLUG}.html`);

if (!fs.existsSync(ALUNO_DIR)) fs.mkdirSync(ALUNO_DIR, { recursive: true });

// ───────────────────────────────────────────── helpers
function esc(s) {
  return String(s ?? '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}
function escAttr(s) { return esc(s).replace(/'/g, '&#39;'); }
function shuffle(arr) {
  const a = arr.slice();
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  // Ensure at least one position differs from original
  if (a.length > 1 && a.every((v, i) => v === arr[i])) [a[0], a[1]] = [a[1], a[0]];
  return a;
}
function audioBtn(text) {
  return `<button class="audio-btn" onclick="speakText('${escAttr(text)}', this)" aria-label="Listen: ${escAttr(text)}">&#9835;</button>`;
}

// ───────────────────────────────────────────── audioMap
function buildAudioMap() {
  const lines = AUDIO.map(it => `        ${JSON.stringify(it.text)}: ${JSON.stringify('/audio/' + SLUG + '/' + it.filename)}`);
  return `    const audioMap = {\n${lines.join(',\n')}\n    };`;
}

// ───────────────────────────────────────────── lesson hero images
const LESSON_HERO = {
  1: 'https://images.unsplash.com/photo-1521737604893-d14cc237f11d?w=800&q=80',
  2: 'https://images.unsplash.com/photo-1502920917128-1aa500764cbd?w=800&q=80',
  3: 'https://images.unsplash.com/photo-1555529669-e69e7aa0ba9a?w=800&q=80',
  4: 'https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=800&q=80',
  5: 'https://images.unsplash.com/photo-1565017228812-9f6e2691b8b9?w=800&q=80',
};

// ───────────────────────────────────────────── PRE-CLASS LESSON CARD
function renderEtapa1_Vocab(aula) {
  const cards = aula.vocabulario.map(v => `
        <div class="vocab-card">
          <div class="vocab-card-content">
            <div class="vocab-card-header">
              <span class="vocab-card-word">${esc(v.en)}</span>
              <span class="vocab-card-dot">&middot;</span>
              <span class="vocab-card-translation">${esc(v.pt)}</span>
            </div>
            <div class="vocab-card-example">${esc(v.ex)}</div>
          </div>
          ${audioBtn(v.ex)}
        </div>`).join('');
  return `
      <div class="exercise-section">
        <div class="section-header-row">
          <h4>1.1 Vocabul&aacute;rio &amp; expressoes <span class="badge badge-vocab">Vocabulary</span></h4>
          <button class="listen-all-btn" onclick="listenAllVocab(this)" aria-label="Ouvir todos">&#9835; Ouvir todos</button>
        </div>
        <p class="microcopy">Olha a palavra, a tradu&ccedil;&atilde;o e o exemplo juntos. Toca em ouvir &mdash; o som ajuda muito a mem&oacute;ria.</p>
        <div class="vocab-cards">${cards}</div>
      </div>`;
}

function renderEtapa1_Matching(aula) {
  const exId = `match-l${aula.numero}`;
  const pairs = aula.preClassExercicios.matching;
  const allTranslations = shuffle(pairs.map(p => p.correct));
  const rows = pairs.map(p => {
    const opts = ['<option value="">Select...</option>']
      .concat(allTranslations.map(t => `<option value="${escAttr(t)}">${esc(t)}</option>`))
      .join('');
    return `
        <div class="match-row" data-answer="${escAttr(p.correct)}">
          <span class="match-word">${esc(p.word)}</span>
          <select onchange="checkMatch(this)" aria-label="Translation of ${escAttr(p.word)}">${opts}</select>
        </div>`;
  }).join('');
  return `
      <div class="exercise-section">
        <h4>1.2 Match the words <span class="badge badge-vocab">Vocabulary</span></h4>
        <p class="microcopy">Combine cada palavra com sua tradu&ccedil;&atilde;o. Errou? Sem problema, leia e tente de novo.</p>
        <div class="match-grid" id="${exId}">${rows}</div>
        <button class="verify-all-btn" onclick="verifyAllMatches('${exId}')">Check answers</button>
      </div>`;
}

function renderEtapa1_Context(aula) {
  // Build a short context paragraph from frasesModeloMaterial (3-4 sentences using new vocab)
  const sentences = aula.frasesModeloMaterial.slice(0, 4).map(s => esc(s)).join(' ');
  const audio = aula.frasesModeloMaterial.slice(0, 4).map(s => audioBtn(s)).join(' ');
  // Comprehension quiz from preClassExercicios.multipleChoice (use first one)
  const q = aula.preClassExercicios.multipleChoice[0];
  const opts = q.options.map((o, i) => `
        <div class="quiz-option" onclick="selectQuiz(this)" data-correct="${i === q.correct ? 'true' : 'false'}">
          <span class="option-letter">${String.fromCharCode(65 + i)}</span> ${esc(o)}
        </div>`).join('');
  return `
      <div class="exercise-section">
        <h4>1.3 Context &amp; comprehension <span class="badge badge-quiz">Reading</span></h4>
        <p class="microcopy">Leia o trecho abaixo &mdash; ele usa o vocabul&aacute;rio que voc&ecirc; acabou de ver. Depois responda a pergunta.</p>
        <div class="speech-card" style="margin-bottom:1rem;">
          <div class="speech-phrase" style="font-size:1.05rem;line-height:1.7;">${sentences}</div>
          <div class="speech-controls">${audio}</div>
        </div>
        <div class="quiz-item">
          <div class="quiz-question">${esc(q.q)}</div>
          <div class="quiz-options">${opts}</div>
        </div>
      </div>`;
}

function renderEtapa1_Grammar(aula) {
  const g = aula.gramaticaFoco;
  const examples = g.exemplos.map(e => `<li>${esc(e)} ${audioBtn(e)}</li>`).join('');
  return `
      <div class="exercise-section">
        <h4>1.4 Grammar focus <span class="badge badge-vocab">Grammar</span></h4>
        <p class="microcopy">A regra primeiro em ingl&ecirc;s, depois em portugu&ecirc;s. Leia, ou&ccedil;a os exemplos, e siga.</p>
        <div class="teacher-tip">
          <p><strong>Structure (EN):</strong> ${esc(g.estrutura)}</p>
          <p style="margin-top:0.5rem;"><strong>Estrutura (PT):</strong> ${esc(g.estrutura)} &mdash; modelo: <em>${esc(g.modelo)}</em>.</p>
        </div>
        <ul style="list-style:none;padding-left:0;margin-top:0.6rem;display:flex;flex-direction:column;gap:0.4rem;font-size:0.9rem;">${examples}</ul>
      </div>`;
}

function renderEtapa1_Application(aula) {
  const items = aula.preClassExercicios.fillBlankWithHint;
  const blocks = items.map(it => {
    const sentence = esc(it.sentence).replace('___',
      `<input class="blank-input" type="text" data-answer="${escAttr(it.answer)}" data-hint="Hint: ${escAttr(it.hint)}" data-phrase="${escAttr(it.phrase)}" placeholder="___" autocomplete="off">`);
    return `
        <div class="fill-blank-item">
          <div class="fill-blank-sentence">${sentence}</div>
          <div class="hint-text">Hint: ${esc(it.hint)}</div>
          <button class="check-btn btn" onclick="checkBlank(this)">Check</button>
          <button class="listen-blank-btn" onclick="listenBlank(this)" aria-label="Listen">&#9835; Listen</button>
        </div>`;
  }).join('');
  return `
      <div class="exercise-section">
        <h4>1.5 Apply: fill in the blank <span class="badge badge-practice">Practice</span></h4>
        <p class="microcopy">Escreva a palavra que falta. A dica em ingl&ecirc;s ajuda. Toque Listen para ouvir a frase completa.</p>
        ${blocks}
      </div>`;
}

function renderEtapa2_Practice(aula) {
  const o = aula.preClassExercicios.ordering;
  if (!o) return '';
  const exId = `order-l${aula.numero}`;
  const correct = o.correct;
  const items = o.shuffled.map((it, idx) => {
    // Find the data-order: position of it in correct array (1-indexed)
    const order = correct.indexOf(it) + 1;
    return `
        <div class="order-item" draggable="true" data-order="${order}" data-text="${escAttr(it)}" onclick="selectOrderItem(this,'${exId}')">
          <span class="order-num">?</span>
          <span class="order-text">${esc(it)}</span>
          <span class="order-arrows">
            <button class="arrow-btn" onclick="moveItem(this,-1,'${exId}')" aria-label="Mover para cima">&#9650;</button>
            <button class="arrow-btn" onclick="moveItem(this,1,'${exId}')" aria-label="Mover para baixo">&#9660;</button>
          </span>
        </div>`;
  }).join('');
  return `
      <div class="exercise-section">
        <h4>2. Vocabulary practice &mdash; put in order <span class="badge badge-order">Order</span></h4>
        <p class="microcopy">${esc(o.instructions)}</p>
        <div class="order-container" id="${exId}">${items}</div>
        <button class="verify-all-btn" onclick="checkOrder('${exId}')">Check order</button>
      </div>`;
}

function renderEtapa3_Pronunciation(aula) {
  const items = aula.preClassExercicios.pronunciation;
  const cards = items.map(p => `
        <div class="speech-card" data-phrase="${escAttr(p.phrase)}">
          <div class="speech-phrase">${esc(p.phrase)}</div>
          <div class="speech-translation">${esc(p.ipa)}</div>
          <div class="speech-controls">
            <button class="btn btn-listen" onclick="speakPhrase(this)" aria-label="Listen">&#9654; Ouvir</button>
            <button class="btn btn-record" onclick="startRecording(this)" aria-label="Record">&#9679; Gravar</button>
            <button class="btn btn-stop" onclick="stopRecording(this)" aria-label="Stop">&#9632; Parar</button>
          </div>
          <div class="speech-result"></div>
        </div>`).join('');
  return `
      <div class="exercise-section">
        <h4>3. Pronunciation lab <span class="badge badge-speak">Speaking</span></h4>
        <p class="microcopy">Toque Ouvir, depois Gravar. Fale a frase e veja palavra a palavra como sua pron&uacute;ncia se compara.</p>
        ${cards}
      </div>`;
}

function renderEtapa4_QuizSituacional(aula) {
  const items = aula.preClassExercicios.multipleChoice.slice(1); // skip 1st (used in 1.3)
  if (items.length === 0) return '';
  const blocks = items.map(q => {
    const opts = q.options.map((o, i) => `
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="${i === q.correct ? 'true' : 'false'}">
            <span class="option-letter">${String.fromCharCode(65 + i)}</span> ${esc(o)}
          </div>`).join('');
    return `
        <div class="quiz-item">
          <div class="quiz-question">${esc(q.q)}</div>
          <div class="quiz-options">${opts}</div>
        </div>`;
  }).join('');
  return `
      <div class="exercise-section">
        <h4>4. Situational quiz <span class="badge badge-quiz">Quiz</span></h4>
        <p class="microcopy">Cen&aacute;rios reais de viagem. Errou? Leia a explica&ccedil;&atilde;o &mdash; &eacute; a&iacute; que se aprende.</p>
        ${blocks}
      </div>`;
}

function renderEtapa5_FreeProduction(aula) {
  const q = aula.preClassExercicios.thinkAboutIt;
  return `
      <div class="exercise-section">
        <h4>5. Think about it &mdash; free production <span class="badge badge-think">Reflection</span></h4>
        <p class="microcopy">Aqui n&atilde;o tem resposta certa &mdash; &eacute; pra voc&ecirc; pensar em ingl&ecirc;s. Toque no microfone e responda como vier.</p>
        <div class="think-card">
          <div class="think-question">${esc(q)}</div>
          <div class="speech-controls">
            <button class="btn btn-record" onclick="startFreeRecording(this)" aria-label="Record">&#9679; Gravar livre</button>
            <button class="btn btn-stop" onclick="stopFreeRecording(this)" aria-label="Stop">&#9632; Parar</button>
          </div>
          <div id="think-result-${aula.numero}"></div>
        </div>
      </div>`;
}

function renderSurvivalCard(aula) {
  if (!aula.survivalCard) return '';
  const phrases = aula.survivalCard.linhas.map((l, i) => `
        <div class="survival-phrase">
          <span class="sp-num">${i + 1}</span>
          <span class="sp-en">${esc(l.en)}</span>
          <span class="sp-pt">${esc(l.pt)}</span>
          <button class="btn btn-listen" onclick="speakText('${escAttr(l.en)}', this)" aria-label="Listen">&#9835;</button>
        </div>`).join('');
  return `
      <div class="survival-card">
        <h4>${esc(aula.survivalCard.titulo)}</h4>
        ${phrases}
      </div>`;
}

function renderChecklist(aula) {
  const items = aula.materialProfessorExercicios.checklistAprendi.map((c, i) => `
          <li><input type="checkbox" id="aula${aula.numero}-check${i}" onchange="toggleChecklist(this)"> <label for="aula${aula.numero}-check${i}">${esc(c)}</label></li>`).join('');
  return `
      <div class="exercise-section" style="background:var(--bg-card);">
        <h4>Checklist &mdash; o que eu aprendi <span class="badge badge-vocab">Self-check</span></h4>
        <p class="microcopy">Leia cada frase em voz alta. Se conseguir dizer &ldquo;sim, eu sei fazer isso&rdquo; pra todas, fechou &mdash; a li&ccedil;&atilde;o t&aacute; dominada.</p>
        <ul class="checklist" id="checklist-${aula.numero}">${items}</ul>
      </div>`;
}

function renderLessonPreClass(aula) {
  return `
    <div class="lesson-card" id="ex-lesson-${aula.numero}">
      <div class="lesson-header" onclick="toggleLesson(this)">
        <div class="lesson-header-img" style="background-image:url('${LESSON_HERO[aula.numero]}')"></div>
        <div class="lesson-header-content">
          <div class="lesson-number">Aula ${String(aula.numero).padStart(2, '0')} &mdash; Pre-class</div>
          <h3>${esc(aula.tema)}</h3>
          <div class="lesson-desc">${esc(aula.subtema)}</div>
          <div class="lesson-progress-mini">
            <div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="${aula.numero}" style="width:0%"></div></div>
            <span class="mini-percent" data-lesson-pct="${aula.numero}">0%</span>
          </div>
        </div>
        <div class="expand-icon">&#9660;</div>
      </div>
      <div class="lesson-body">
        <div class="promise-box" style="margin-bottom:1.5rem;">
          <p>${esc(aula.promessa)}</p>
        </div>
        ${renderEtapa1_Vocab(aula)}
        ${renderEtapa1_Matching(aula)}
        ${renderEtapa1_Context(aula)}
        ${renderEtapa1_Grammar(aula)}
        ${renderEtapa1_Application(aula)}
        ${renderEtapa2_Practice(aula)}
        ${renderEtapa3_Pronunciation(aula)}
        ${renderEtapa4_QuizSituacional(aula)}
        ${renderEtapa5_FreeProduction(aula)}
        ${renderSurvivalCard(aula)}
        ${renderChecklist(aula)}
      </div>
    </div>`;
}

function renderLessonPlaceholder(num, kind = 'pre') {
  return `
    <div class="lesson-card" style="opacity:0.55;">
      <div class="lesson-header" style="cursor:default;">
        <div class="lesson-header-img" style="background:var(--bg-elevated);"></div>
        <div class="lesson-header-content">
          <div class="lesson-number">Aula ${String(num).padStart(2, '0')} &mdash; ${kind === 'pre' ? 'Pre-class' : kind === 'plan' ? 'Plano de Aula' : kind === 'teacher' ? 'Material' : 'Complementares'}</div>
          <h3>Aula ${num}</h3>
          <div class="lesson-desc"><em>Conte&uacute;do ser&aacute; adicionado no pr&oacute;ximo bloco</em></div>
        </div>
        <div class="expand-icon">&middot;</div>
      </div>
    </div>`;
}

// ───────────────────────────────────────────── TAB 1 — PLANNING
function renderTabPlanning() {
  const curriculumRows = [
    ...CONTENT.aulas.map(a => `
        <tr>
          <td class="aula-cell">${String(a.numero).padStart(2, '0')}</td>
          <td>${esc(a.tema)}</td>
          <td>${esc(a.gramaticaFoco.estrutura.split(';')[0])}</td>
          <td>${esc(a.materialProfessorExercicios.rolePlays[0]?.titulo || a.subtema)}</td>
          <td>${esc(a.homework.split('.')[0])}.</td>
        </tr>`),
    ...Array.from({ length: 15 }, (_, i) => i + 6).map(i => `
        <tr style="opacity:0.55;">
          <td class="aula-cell">${String(i).padStart(2, '0')}</td>
          <td colspan="4"><em>Conte&uacute;do ser&aacute; adicionado no pr&oacute;ximo bloco</em></td>
        </tr>`),
    `
        <tr style="opacity:0.55;">
          <td class="aula-cell">21-48</td>
          <td colspan="4"><em>Aulas 21 a 48 ser&atilde;o adicionadas em blocos subsequentes (5 aulas por bloco).</em></td>
        </tr>`,
  ].join('');

  const journey = CONTENT._meta.personagemJornada;
  const promise = CONTENT._meta.promessaTransformadora;

  return `
    <div class="tab-content active" id="tab-planning">
      <div class="info-grid">
        <div class="info-item"><div class="info-label">Nome</div><div class="info-value">Roberto Pires</div></div>
        <div class="info-item"><div class="info-label">Idade</div><div class="info-value">45 anos</div></div>
        <div class="info-item"><div class="info-label">Cidade</div><div class="info-value">S&atilde;o Paulo, SP</div></div>
        <div class="info-item"><div class="info-label">Profiss&atilde;o</div><div class="info-value">Empres&aacute;rio</div></div>
        <div class="info-item"><div class="info-label">N&iacute;vel</div><div class="info-value">A2</div></div>
        <div class="info-item"><div class="info-label">Frequ&ecirc;ncia</div><div class="info-value">3x semana &middot; 60 min</div></div>
        <div class="info-item"><div class="info-label">Total</div><div class="info-value">48 aulas</div></div>
        <div class="info-item"><div class="info-label">Foco</div><div class="info-value">Travel English Barcelona+Paris</div></div>
      </div>

      <div class="journey-box">
        <h4>Personagem-jornada</h4>
        <div class="journey-from">${esc(journey.de)}</div>
        <div class="journey-arrow">&darr;</div>
        <div class="journey-to">${esc(journey.para)}</div>
      </div>

      <div class="promise-box">
        <p>${esc(promise)}</p>
      </div>

      <div class="sw-grid">
        <div class="sw-col strengths">
          <h4>For&ccedil;as</h4>
          <ul>
            <li>Pron&uacute;ncia clara e intelig&iacute;vel</li>
            <li>Vocabul&aacute;rio funcional b&aacute;sico presente</li>
            <li>Compreens&atilde;o auditiva &agrave; frente da produ&ccedil;&atilde;o</li>
            <li>Objetivo claro e prazo real (agosto)</li>
            <li>Energia constante e animada</li>
          </ul>
        </div>
        <div class="sw-col weaknesses">
          <h4>Pontos de aten&ccedil;&atilde;o</h4>
          <ul>
            <li>Constru&ccedil;&atilde;o de frases truncada (SVO incompleto)</li>
            <li>Code-switching frequente para o portugu&ecirc;s</li>
            <li>Repert&oacute;rio de chunks limitado</li>
            <li>Toler&acirc;ncia ao erro vari&aacute;vel (depende do dia)</li>
            <li>Lacuna de hobbies/hist&oacute;rico no perfil</li>
          </ul>
        </div>
      </div>

      <h3 style="font-family:'Cormorant Garamond',serif;font-size:1.4rem;margin:2rem 0 1rem;color:var(--white);">Curr&iacute;culo &mdash; 48 aulas</h3>
      <div style="overflow-x:auto;">
        <table class="curriculum-table">
          <thead>
            <tr><th>#</th><th>Tema</th><th>Foco lingu&iacute;stico</th><th>Atividade</th><th>Homework</th></tr>
          </thead>
          <tbody>${curriculumRows}</tbody>
        </table>
      </div>

      <h3 style="font-family:'Cormorant Garamond',serif;font-size:1.4rem;margin:2rem 0 1rem;color:var(--white);">Metodologia</h3>
      <div style="display:grid;gap:0.6rem;margin-bottom:2rem;">
        <div class="method-card"><h5>1. PPP em 60 min adaptado para A2 cinest&eacute;sico</h5><p>Warm-up &middot; Lead-in &middot; Pre-teach &middot; Teach+CCQs &middot; Practice &middot; Semi-free &middot; Production &middot; Wrap-up.</p></div>
        <div class="method-card"><h5>2. Chunks-first &mdash; nunca palavras isoladas</h5><p>Cada item lexical aparece dentro de uma frase-modelo de 5-8 palavras.</p></div>
        <div class="method-card"><h5>3. Cinest&eacute;sico-comunicativo</h5><p>Role-plays em p&eacute;, simula&ccedil;&otilde;es com objetos f&iacute;sicos, drilling com movimento.</p></div>
        <div class="method-card"><h5>4. Survival Card progressivo</h5><p>Aula 1: 6 linhas. Aula 5: 12 linhas-chave de viagem dom&iacute;nadas no autom&aacute;tico.</p></div>
        <div class="method-card"><h5>5. &ldquo;Could I&hellip;?&rdquo; como padr&atilde;o de cortesia</h5><p>Nunca &ldquo;I want&rdquo; como pedido. &ldquo;Could I have/pay/see&hellip;?&rdquo; desde a Aula 1.</p></div>
      </div>

      <div class="personality-card">
        <h4>Mapa de personalidade pedag&oacute;gica</h4>
        <div class="personality-item"><div class="p-label">Estilo de aprendizagem</div><div class="p-value">Cinest&eacute;sico-comunicativo &mdash; aprende fazendo.</div></div>
        <div class="personality-item"><div class="p-label">Energia preferida</div><div class="p-value">Din&acirc;mica e variada &mdash; blocos de 12-15 min.</div></div>
        <div class="personality-item"><div class="p-label">Toler&acirc;ncia a tradu&ccedil;&atilde;o</div><div class="p-value">Alta &mdash; PT-BR seletivo &eacute; suporte cognitivo.</div></div>
        <div class="personality-item"><div class="p-label">Perfil emocional</div><div class="p-value">Depende do dia &mdash; em dias ruins, mais scaffolding.</div></div>
        <div class="personality-item"><div class="p-label">Stake</div><div class="p-value">Chegar em Barcelona/Paris e n&atilde;o conseguir pedir ajuda.</div></div>
        <div class="personality-item"><div class="p-label">Vit&oacute;ria</div><div class="p-value">Circular com autonomia, pedir tapas sem apontar, perguntar dire&ccedil;&otilde;es em Paris sem travar.</div></div>
      </div>
    </div>`;
}

// ───────────────────────────────────────────── TAB 2 — PRE-CLASS
function renderTabExercises() {
  const o = CONTENT.onboarding;
  const phrases = o.frasesEmergencia.map(p => `
        <div class="speech-card" data-phrase="${escAttr(p.en)}">
          <div class="speech-phrase">${esc(p.en)}</div>
          <div class="speech-translation">${esc(p.pt)}</div>
          <div class="speech-controls">
            <button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Ouvir</button>
          </div>
        </div>`).join('');

  const lessons = CONTENT.aulas.map(renderLessonPreClass).join('');
  const placeholders = Array.from({ length: 15 }, (_, i) => renderLessonPlaceholder(i + 6, 'pre')).join('');

  return `
    <div class="tab-content" id="tab-exercises">
      <div class="welcome-card">
        <h3>${esc(o.saudacao)}</h3>
        <p>${esc(o.introducao)}</p>
        <blockquote>${esc(o.citacao)}</blockquote>
        <div class="emergency-phrases">
          <h4>5 Frases de emerg&ecirc;ncia para a viagem</h4>
          <p class="microcopy">Ou&ccedil;a cada uma e tente repetir em voz alta. Salvam qualquer situa&ccedil;&atilde;o em Barcelona ou Paris.</p>
          ${phrases}
        </div>
        <div class="teacher-tip" style="margin-top:1rem;text-align:left;">
          <p><strong>Desafio leve antes da Aula 1:</strong> ${esc(o.desafioLeve)}</p>
        </div>
      </div>

      ${lessons}

      <h3 style="font-family:'Cormorant Garamond',serif;font-size:1.3rem;margin:2rem 0 1rem;color:var(--text-dim);">Aulas 6 a 20 (pr&oacute;ximos blocos)</h3>
      ${placeholders}

      <div class="celebration-card" id="celebrationCard" style="display:none;">
        <h3>Bloco 1 conclu&iacute;do</h3>
        <p>Roberto, voc&ecirc; dominou as 5 primeiras aulas. Agora &eacute; hora de avan&ccedil;ar para Barcelona &mdash; check-in no hotel, restaurantes e tapas. Continue assim!</p>
      </div>
    </div>`;
}

// ───────────────────────────────────────────── TAB 3 — PLANO DE AULA
function renderLessonPlan(aula) {
  const rows = aula.planoDeAulaPPP.map(r => `
        <tr><td class="time-cell">${esc(r.tempo)}</td><td class="activity-cell">${esc(r.fase)}</td><td>${esc(r.atividade)}</td></tr>`).join('');
  const ccqs = aula.gramaticaFoco.ccqs.map(c => `
      <div class="teacher-tip">
        <p><strong>CCQ:</strong> ${esc(c.q)}</p>
        <p style="margin-top:0.3rem;"><strong>Resposta esperada:</strong> ${esc(c.a)}</p>
      </div>`).join('');
  const obstacles = aula.alertasObstaculo.map(o => `
      <div class="obstacle-alert">
        <p><strong>Onde:</strong> ${esc(o.ondeOcorre)}</p>
        <p style="margin-top:0.3rem;"><strong>Obst&aacute;culo:</strong> ${esc(o.obstaculo)}</p>
        <p style="margin-top:0.3rem;"><strong>Solu&ccedil;&atilde;o:</strong> ${esc(o.solucao)}</p>
      </div>`).join('');
  const callback = aula.callbackAulaAnterior ? `
      <div class="callback-box">
        <h4>Callback da aula anterior</h4>
        <p>${esc(aula.callbackAulaAnterior)}</p>
      </div>` : '';
  return `
    <div class="lesson-card" id="plan-lesson-${aula.numero}">
      <div class="lesson-header" onclick="toggleLesson(this)">
        <div class="lesson-header-img" style="background-image:url('${LESSON_HERO[aula.numero]}')"></div>
        <div class="lesson-header-content">
          <div class="lesson-number">Aula ${String(aula.numero).padStart(2, '0')} &mdash; Plano de Aula</div>
          <h3>${esc(aula.tema)}</h3>
          <div class="lesson-desc">${esc(aula.criterioSucesso)}</div>
        </div>
        <div class="expand-icon">&#9660;</div>
      </div>
      <div class="lesson-body">
        ${callback}
        <h4 style="font-family:'Cormorant Garamond',serif;font-size:1.1rem;margin-bottom:0.6rem;">Roteiro PPP minuto a minuto (60 min)</h4>
        <table class="plan-table">
          <thead><tr><th>Tempo</th><th>Fase</th><th>Atividade do professor</th></tr></thead>
          <tbody>${rows}</tbody>
        </table>

        <h4 style="font-family:'Cormorant Garamond',serif;font-size:1.1rem;margin:1.2rem 0 0.6rem;">Concept Check Questions (escritas, n&atilde;o improvisar)</h4>
        ${ccqs}

        <h4 style="font-family:'Cormorant Garamond',serif;font-size:1.1rem;margin:1.2rem 0 0.6rem;">Antecipa&ccedil;&atilde;o de obst&aacute;culos</h4>
        ${obstacles}

        <div class="homework-box">
          <h4>Homework para a pr&oacute;xima aula</h4>
          <ul><li>${esc(aula.homework)}</li></ul>
        </div>
      </div>
    </div>`;
}

function renderTabPlan() {
  const lessons = CONTENT.aulas.map(renderLessonPlan).join('');
  const placeholders = Array.from({ length: 15 }, (_, i) => renderLessonPlaceholder(i + 6, 'plan')).join('');
  return `
    <div class="tab-content" id="tab-plan">
      ${lessons}
      <h3 style="font-family:'Cormorant Garamond',serif;font-size:1.3rem;margin:2rem 0 1rem;color:var(--text-dim);">Aulas 6 a 20 (pr&oacute;ximos blocos)</h3>
      ${placeholders}
    </div>`;
}

// ───────────────────────────────────────────── TAB 4 — MATERIAL DO PROFESSOR
function renderTeacherSection(title, phaseTag, body) {
  return `
      <div class="teacher-section">
        <h4>${esc(title)} <span class="phase-tag ${phaseTag}">${phaseTag.replace('phase-', '').toUpperCase()}</span></h4>
        ${body}
      </div>`;
}

function renderLessonTeacher(aula) {
  const m = aula.materialProfessorExercicios;
  const warmUp = m.warmUp.map(q => `<li>${esc(q)}</li>`).join('');
  const vocabRows = m.vocabularyContextSentences.map(v => `
        <tr><td class="word-cell">${esc(v.word)}</td><td>${esc(v.sentence)} ${audioBtn(v.sentence)}</td></tr>`).join('');
  const dialogue = m.dialogue ? m.dialogue.lines.map(l => {
    const isYou = l.speaker === 'ROBERTO';
    return `
            <div class="dialogue-line">
              <div class="dialogue-avatar ${isYou ? 'avatar-you' : 'avatar-staff'}">${esc(l.speaker.slice(0,3))}</div>
              <div class="dialogue-bubble ${isYou ? 'your-turn' : ''}">
                <div class="speaker">${esc(l.speaker)}</div>
                <div>${esc(l.text)} ${audioBtn(l.text)}</div>
              </div>
            </div>`;
  }).join('') : '';
  const drilling = m.oralDrillingPrompts.map(p => `
        <tr><td>${esc(p.pt)}</td><td>${esc(p.en)} ${audioBtn(p.en)}</td></tr>`).join('');
  const errors = m.errorCorrection.map(e => `
        <tr>
          <td style="color:var(--danger);text-decoration:line-through;">${esc(e.wrong)}</td>
          <td style="color:var(--success);font-weight:600;">${esc(e.right)} ${audioBtn(e.right)}</td>
          <td style="font-size:0.8rem;color:var(--text-dim);font-style:italic;">${esc(e.note)}</td>
        </tr>`).join('');
  const sub = m.substitutionDrill;
  const subRendered = sub ? sub.substituicoes.map(s => {
    const r = sub.modelo.replace('___', s);
    return `<li>${esc(r)} ${audioBtn(r)}</li>`;
  }).join('') : '';
  const plays = m.rolePlays.map(rp => `
        <div class="callback-box" style="margin-bottom:0.6rem;">
          <h4>Role-play &middot; ${esc(rp.tipo)} &mdash; ${esc(rp.titulo)}</h4>
          <p style="font-size:0.875rem;color:var(--text-mid);"><strong>Cen&aacute;rio:</strong> ${esc(rp.prompt)}</p>
          <p style="font-size:0.875rem;color:var(--text-mid);margin-top:0.3rem;"><strong>Output esperado:</strong> <em>${esc(rp.esperado)}</em></p>
        </div>`).join('');

  return `
    <div class="teacher-lesson">
      <div class="teacher-hero" style="background-image:url('${LESSON_HERO[aula.numero]}')">
        <div class="hero-sub">Aula ${String(aula.numero).padStart(2, '0')} &middot; Material do Professor</div>
        <h3>${esc(aula.tema)}</h3>
      </div>
      <div class="teacher-body">
        ${renderTeacherSection('1. Warm-up &middot; 5 perguntas', 'phase-warm', `<ul style="padding-left:1.2rem;font-size:0.9rem;line-height:1.8;color:var(--text-mid);">${warmUp}</ul>`)}
        ${renderTeacherSection('2. Vocabulary in context', 'phase-vocab', `
          <table class="vocab-table">
            <thead><tr><th>Word</th><th>Example sentence</th></tr></thead>
            <tbody>${vocabRows}</tbody>
          </table>`)}
        ${m.dialogue ? renderTeacherSection(`3. Dialogue &mdash; ${esc(m.dialogue.title)}`, 'phase-vocab', `<div class="dialogue-container">${dialogue}</div>`) : ''}
        ${renderTeacherSection('4. Grammar focus', 'phase-teach', `
          <div class="teacher-tip">
            <p><strong>Structure:</strong> ${esc(aula.gramaticaFoco.estrutura)}</p>
            <p style="margin-top:0.4rem;"><strong>Modelo:</strong> ${esc(aula.gramaticaFoco.modelo)}</p>
          </div>
          <ul style="list-style:none;padding-left:0;display:flex;flex-direction:column;gap:0.4rem;font-size:0.9rem;margin-top:0.6rem;">
            ${aula.gramaticaFoco.exemplos.map(e => `<li>${esc(e)} ${audioBtn(e)}</li>`).join('')}
          </ul>`)}
        ${renderTeacherSection('5. Practice &mdash; oral drilling', 'phase-practice', `
          <p class="microcopy">Diga em PT, Roberto produz em EN. Sem tempo para pensar.</p>
          <table class="vocab-table">
            <thead><tr><th>Voc&ecirc; diz (PT)</th><th>Roberto produz (EN)</th></tr></thead>
            <tbody>${drilling}</tbody>
          </table>`)}
        ${sub ? renderTeacherSection('6. Substitution drill', 'phase-practice', `
          <p style="font-size:0.92rem;color:var(--text);margin-bottom:0.4rem;"><strong>Modelo:</strong> ${esc(sub.modelo)} ${audioBtn(sub.modelo)}</p>
          <p class="microcopy">Voc&ecirc; varia o complemento, Roberto adapta a frase preservando a estrutura.</p>
          <ul style="list-style:none;padding-left:0;display:flex;flex-direction:column;gap:0.3rem;font-size:0.9rem;">${subRendered}</ul>`) : ''}
        ${renderTeacherSection('7. Error correction', 'phase-teach', `
          <p class="microcopy">Erros recorrentes do A2 brasileiro &mdash; reformule no momento, com gentileza.</p>
          <table class="vocab-table">
            <thead><tr><th>Errado</th><th>Certo</th><th>Por qu&ecirc;</th></tr></thead>
            <tbody>${errors}</tbody>
          </table>`)}
        ${renderTeacherSection('8. Production &mdash; role-plays guided &rarr; semi-free &rarr; free', 'phase-production', `
          <p class="microcopy">Rampa progressiva. Em dia ruim, fique mais tempo no guided.</p>
          ${plays}`)}
        ${renderSurvivalCard(aula)}
      </div>
    </div>`;
}

function renderTabTeacher() {
  const lessons = CONTENT.aulas.map(renderLessonTeacher).join('');
  const placeholders = Array.from({ length: 15 }, (_, i) => renderLessonPlaceholder(i + 6, 'teacher')).join('');
  return `
    <div class="tab-content" id="tab-teacher">
      ${lessons}
      <h3 style="font-family:'Cormorant Garamond',serif;font-size:1.3rem;margin:2rem 0 1rem;color:var(--text-dim);">Aulas 6 a 20 (pr&oacute;ximos blocos)</h3>
      ${placeholders}
    </div>`;
}

// ───────────────────────────────────────────── TAB 5 — COMPLEMENTARES
const TYPE_TO_THUMB = {
  'Filme':         'https://images.unsplash.com/photo-1489599735734-79b4af4cf6ad?w=300&q=80',
  'Série':         'https://images.unsplash.com/photo-1522869635100-9f4c5e86aa37?w=300&q=80',
  'Serie':         'https://images.unsplash.com/photo-1522869635100-9f4c5e86aa37?w=300&q=80',
  'YouTube':       'https://images.unsplash.com/photo-1611162617213-7d7a39e9b1d7?w=300&q=80',
  'Podcast':       'https://images.unsplash.com/photo-1590602847861-f357a9332bbc?w=300&q=80',
  'Documentário':  'https://images.unsplash.com/photo-1594908900066-3f47337549d8?w=300&q=80',
  'Documentario':  'https://images.unsplash.com/photo-1594908900066-3f47337549d8?w=300&q=80',
  'App':           'https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=300&q=80',
};

function renderLessonComplementary(aula) {
  const cards = aula.complementares.map((c, i) => `
        <div class="media-card-wrapper" data-media="l${aula.numero}-m${i}">
          <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
          <div class="media-card">
            <div class="media-thumb" style="background-image:url('${TYPE_TO_THUMB[c.tipo] || TYPE_TO_THUMB['Filme']}')"></div>
            <div class="media-info">
              <div class="media-type">${esc(c.tipo)}</div>
              <h5>${esc(c.titulo)}</h5>
              <p>${esc(c.descricao)}</p>
              <p class="media-tip">${esc(c.tip)}</p>
            </div>
          </div>
        </div>`).join('');
  return `
    <div class="lesson-card" id="comp-lesson-${aula.numero}">
      <div class="lesson-header" onclick="toggleLesson(this)">
        <div class="lesson-header-img" style="background-image:url('${LESSON_HERO[aula.numero]}')"></div>
        <div class="lesson-header-content">
          <div class="lesson-number">Aula ${String(aula.numero).padStart(2, '0')} &mdash; Complementares</div>
          <h3>${esc(aula.tema)}</h3>
          <div class="lesson-desc">${esc(aula.subtema)}</div>
        </div>
        <div class="expand-icon">&#9660;</div>
      </div>
      <div class="lesson-body">
        <div class="media-grid">${cards}</div>
      </div>
    </div>`;
}

function renderTabComplementary() {
  const lessons = CONTENT.aulas.map(renderLessonComplementary).join('');
  return `
    <div class="tab-content" id="tab-complementary">
      <p class="microcopy" style="margin-bottom:1.5rem;font-size:0.95rem;">Filmes, s&eacute;ries, canais e podcasts curados para cada aula. N&atilde;o &eacute; obriga&ccedil;&atilde;o &mdash; &eacute; combust&iacute;vel pra quando voc&ecirc; tiver fome de mais ingl&ecirc;s entre as aulas.</p>
      ${lessons}
    </div>`;
}

// ───────────────────────────────────────────── CANONICAL JS BLOCK (REGRA 26)
function buildCanonicalJs(roleSlug /* 'professor' | 'aluno' */) {
  const totalLessons = CONTENT.aulas.length;
  const audioMapJs = buildAudioMap();
  const stateKey = `${SLUG}-${roleSlug}`;
  return `
${audioMapJs}

    // ===== TAB SWITCHING =====
    function switchTab(tabId) {
        document.querySelectorAll('.tab-content').forEach(t => t.classList.remove('active'));
        document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        document.getElementById('tab-' + tabId).classList.add('active');
        if (event && event.currentTarget) event.currentTarget.classList.add('active');
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function toggleLesson(header) { header.parentElement.classList.toggle('open'); }

    let currentAudio = null;
    let audioSpeed = parseFloat(localStorage.getItem('alumni-audio-speed') || '1');

    function setAudioSpeed(speed, btn) {
        audioSpeed = speed;
        localStorage.setItem('alumni-audio-speed', speed);
        document.querySelectorAll('.speed-btn').forEach(function(b) {
            b.style.background = 'var(--bg-card)'; b.style.color = 'var(--text)';
            b.style.borderColor = 'var(--border)'; b.style.fontWeight = '400';
        });
        btn.style.background = 'var(--accent)'; btn.style.color = '#fff';
        btn.style.borderColor = 'var(--accent)'; btn.style.fontWeight = '600';
    }

    document.addEventListener('DOMContentLoaded', function() {
        var saved = parseFloat(localStorage.getItem('alumni-audio-speed') || '1');
        var btn = document.querySelector('.speed-btn[data-speed="' + saved + '"]');
        if (btn) setAudioSpeed(saved, btn);
    });

    function speakText(text, btn) {
        if (currentAudio) { currentAudio.pause(); currentAudio.currentTime = 0; }
        var cleanText = text.replace(/\\\\'/g, "'");
        var file = audioMap[cleanText] || audioMap[cleanText.replace(/\\.$/, '')] || audioMap[cleanText + '.'];
        if (file) {
            currentAudio = new Audio(file);
            currentAudio.playbackRate = audioSpeed;
            currentAudio.play().catch(function() {
                if ("speechSynthesis" in window) {
                    window.speechSynthesis.cancel();
                    var u = new SpeechSynthesisUtterance(cleanText);
                    u.lang = "en-US"; u.rate = audioSpeed * 0.85; u.pitch = 1;
                    window.speechSynthesis.speak(u);
                }
            });
        } else {
            if ("speechSynthesis" in window) {
                window.speechSynthesis.cancel();
                var u = new SpeechSynthesisUtterance(cleanText);
                u.lang = "en-US"; u.rate = audioSpeed * 0.85; u.pitch = 1;
                window.speechSynthesis.speak(u);
            }
        }
    }

    function speakPhrase(btn) {
        var card = btn.closest('.speech-card');
        if (card) speakText(card.dataset.phrase, btn);
    }

    // ===== SPEECH RECOGNITION =====
    var activeRecognition = null;

    function startRecording(btn) {
        var SR = window.SpeechRecognition || window.webkitSpeechRecognition;
        if (!SR) { alert('Please use Google Chrome for voice recognition.'); return; }
        var card = btn.closest('.speech-card');
        var target = card.dataset.phrase.toLowerCase().replace(/[^a-z0-9' ]/g, '');
        var resultDiv = card.querySelector('.speech-result');
        var stopBtn = card.querySelector('.btn-stop');
        if (btn.classList.contains('recording')) return;
        btn.classList.add('recording', 'hidden');
        stopBtn.classList.add('visible');
        var r = new SR();
        r.lang = 'en-US'; r.interimResults = false; r.maxAlternatives = 3; r.continuous = true;
        activeRecognition = { recognition: r, btn: btn, stopBtn: stopBtn, card: card };
        r.start();
        function resetButtons() { btn.classList.remove('recording', 'hidden'); stopBtn.classList.remove('visible'); activeRecognition = null; }
        r.onresult = function(event) {
            var best = event.results[event.results.length - 1][0].transcript.toLowerCase().replace(/[^a-z0-9' ]/g, '');
            var analysis = analyzeWords(target, best);
            var totalWords = analysis.expected.length;
            var correctWords = analysis.expected.filter(function(w) { return w.status === 'correct'; }).length;
            resultDiv.classList.add('show'); resultDiv.classList.remove('good', 'try-again', 'bad');
            var html = '';
            if (analysis.score >= 0.8) { resultDiv.classList.add('good'); html += '<strong>Score: ' + correctWords + '/' + totalWords + '</strong> &mdash; Excellent!'; updateProgress(); }
            else if (analysis.score >= 0.5) { resultDiv.classList.add('try-again'); html += '<strong>Score: ' + correctWords + '/' + totalWords + '</strong> &mdash; Almost there!'; }
            else { resultDiv.classList.add('bad'); html += '<strong>Score: ' + correctWords + '/' + totalWords + '</strong> &mdash; Keep practicing!'; }
            html += '<div class="word-comparison"><div class="comp-label">Word-by-word:</div><div class="comp-words">';
            analysis.expected.forEach(function(w) { html += '<span class="word-box word-' + (w.status === 'correct' ? 'correct' : 'missing') + '"><span class="word-icon">' + (w.status === 'correct' ? '&#10003;' : '&#10007;') + '</span> ' + w.word + '</span>'; });
            html += '</div><div class="comp-label">You said:</div><div class="comp-words">';
            analysis.spoken.forEach(function(w) {
                var cls = w.status === 'correct' ? 'correct' : w.status === 'extra' ? 'extra' : 'wrong';
                var icon = w.status === 'correct' ? '&#10003;' : w.status === 'extra' ? '~' : '&#10007;';
                html += '<span class="word-box word-' + cls + '"><span class="word-icon">' + icon + '</span> ' + w.word + '</span>';
            });
            html += '</div>';
            if (analysis.wrongWords.length > 0) {
                html += '<div class="speech-suggestion"><strong>Focus on:</strong> ';
                html += analysis.wrongWords.map(function(w) { return '"<strong>' + w.expected + '</strong>"' + (w.got ? ' (you said "' + w.got + '")' : ''); }).join(' &middot; ');
                html += '</div>';
            }
            html += '</div>';
            resultDiv.innerHTML = html;
            resetButtons();
        };
        r.onerror = function() { resetButtons(); resultDiv.classList.add('show', 'try-again'); resultDiv.innerHTML = 'Could not hear you. Check your microphone.'; };
        r.onend = function() { resetButtons(); };
        setTimeout(function() { if (btn.classList.contains('recording')) { r.stop(); resetButtons(); } }, 30000);
    }

    function stopRecording(stopBtn) { if (activeRecognition) activeRecognition.recognition.stop(); }

    function analyzeWords(targetStr, spokenStr) {
        var tw = targetStr.split(/ +/).filter(function(w) { return w; });
        var sw = spokenStr.split(/ +/).filter(function(w) { return w; });
        var m = tw.length, n = sw.length;
        var dp = Array.from({ length: m + 1 }, function() { return Array(n + 1).fill(0); });
        for (var i = 1; i <= m; i++) for (var j = 1; j <= n; j++) dp[i][j] = wordsMatch(tw[i-1], sw[j-1]) ? dp[i-1][j-1] + 1 : Math.max(dp[i-1][j], dp[i][j-1]);
        var mt = new Set(), ms = new Set(); var i = m, j = n;
        while (i > 0 && j > 0) { if (wordsMatch(tw[i-1], sw[j-1])) { mt.add(i-1); ms.add(j-1); i--; j--; } else if (dp[i-1][j] > dp[i][j-1]) i--; else j--; }
        var expected = tw.map(function(w, i) { return { word: w, status: mt.has(i) ? 'correct' : 'missing' }; });
        var spoken = sw.map(function(w, i) { return { word: w, status: ms.has(i) ? 'correct' : 'wrong' }; });
        var wrongWords = [], missedTW = tw.filter(function(_, i) { return !mt.has(i); }), wrongSW = sw.filter(function(_, i) { return !ms.has(i); });
        missedTW.forEach(function(t, i) { wrongWords.push({ expected: t, got: wrongSW[i] || null }); });
        wrongSW.slice(missedTW.length).forEach(function(s) { spoken.forEach(function(sp) { if (sp.word === s && sp.status === 'wrong') sp.status = 'extra'; }); });
        return { expected: expected, spoken: spoken, wrongWords: wrongWords, score: mt.size / Math.max(m, 1) };
    }

    function wordsMatch(a, b) { if (a === b) return true; var ca = a.replace(/'/g, ''), cb = b.replace(/'/g, ''); if (ca === cb) return true; if (a.length > 3 && b.length > 3 && levenshtein(a, b) <= 1) return true; return false; }
    function levenshtein(a, b) { var m = []; for (var i = 0; i <= b.length; i++) m[i] = [i]; for (var j = 0; j <= a.length; j++) m[0][j] = j; for (var i = 1; i <= b.length; i++) for (var j = 1; j <= a.length; j++) m[i][j] = b[i-1] === a[j-1] ? m[i-1][j-1] : Math.min(m[i-1][j-1] + 1, m[i][j-1] + 1, m[i-1][j] + 1); return m[b.length][a.length]; }

    // ===== FILL-IN-THE-BLANK =====
    function checkBlank(btn) {
        var item = btn.closest('.fill-blank-item'), input = item.querySelector('.blank-input');
        input.classList.remove('correct', 'wrong');
        var answer = (input.dataset.answer || '').toLowerCase().trim();
        var altAnswer = input.dataset.alt ? input.dataset.alt.toLowerCase().trim() : null;
        var value = (input.value || '').toLowerCase().trim();
        var hintEl = item.querySelector('.blank-hint-feedback');
        if (hintEl) hintEl.classList.remove('visible');
        if (value === answer || (altAnswer && value === altAnswer)) {
            input.classList.add('correct');
            updateProgress();
        } else {
            input.classList.add('wrong');
            if (input.dataset.hint) {
                if (!hintEl) { hintEl = document.createElement('div'); hintEl.className = 'blank-hint-feedback'; item.appendChild(hintEl); }
                hintEl.textContent = input.dataset.hint; hintEl.classList.add('visible');
            }
            setTimeout(function() { input.classList.remove('wrong'); }, 1500);
        }
    }

    function listenBlank(btn) {
        var item = btn.closest('.fill-blank-item'), input = item.querySelector('.blank-input');
        if (input.dataset.phrase) speakText(input.dataset.phrase, btn);
    }

    // ===== QUIZ =====
    function selectQuiz(o) {
        var p = o.closest('.quiz-options'); if (p.querySelector('.correct')) return;
        if (o.dataset.correct === 'true') { o.classList.add('correct'); updateProgress(); }
        else { o.classList.add('wrong'); setTimeout(function() { o.classList.remove('wrong'); }, 800); }
    }

    // ===== ORDER =====
    var orderSelection = {};
    function selectOrderItem(item, containerId) {
        if (item.classList.contains('correct-order')) return;
        if (!orderSelection[containerId]) orderSelection[containerId] = [];
        var idx = orderSelection[containerId].indexOf(item);
        if (idx > -1) { orderSelection[containerId].splice(idx, 1); item.querySelector('.order-num').textContent = '?'; item.style.borderColor = ''; }
        else { orderSelection[containerId].push(item); item.querySelector('.order-num').textContent = orderSelection[containerId].length; item.style.borderColor = 'var(--accent)'; }
    }

    function checkOrder(containerId) {
        var container = document.getElementById(containerId);
        var items = container.querySelectorAll('.order-item');
        var allCorrect = true;
        // Check by current DOM position
        Array.from(items).forEach(function(item, idx) {
            var expected = parseInt(item.dataset.order, 10);
            if (expected === idx + 1) {
                item.classList.add('correct-order');
                item.querySelector('.order-num').textContent = idx + 1;
            } else {
                allCorrect = false;
                item.classList.add('wrong');
                item.style.borderColor = 'var(--danger)';
                setTimeout(function() {
                    item.classList.remove('wrong');
                    item.style.borderColor = '';
                    item.querySelector('.order-num').textContent = '?';
                }, 1200);
            }
        });
        if (allCorrect) updateProgress();
    }

    function moveItem(btn, direction, containerId) {
        var item = btn.closest('.order-item');
        var container = document.getElementById(containerId);
        var items = Array.from(container.querySelectorAll('.order-item'));
        var idx = items.indexOf(item);
        if (direction === -1 && idx > 0) container.insertBefore(item, items[idx - 1]);
        else if (direction === 1 && idx < items.length - 1) container.insertBefore(items[idx + 1], item);
    }

    // ===== DRAG =====
    var draggedItem = null;
    document.addEventListener('DOMContentLoaded', function() {
        document.querySelectorAll('.order-container').forEach(function(container) {
            container.addEventListener('dragstart', function(e) { var item = e.target.closest('.order-item'); if (!item || item.classList.contains('correct-order')) return; draggedItem = item; item.classList.add('dragging'); e.dataTransfer.effectAllowed = 'move'; });
            container.addEventListener('dragend', function(e) { var item = e.target.closest('.order-item'); if (item) item.classList.remove('dragging'); container.querySelectorAll('.order-item').forEach(function(i) { i.classList.remove('drag-over'); }); draggedItem = null; });
            container.addEventListener('dragover', function(e) { e.preventDefault(); e.dataTransfer.dropEffect = 'move'; var target = e.target.closest('.order-item'); if (target && target !== draggedItem) { container.querySelectorAll('.order-item').forEach(function(i) { i.classList.remove('drag-over'); }); target.classList.add('drag-over'); } });
            container.addEventListener('drop', function(e) { e.preventDefault(); var target = e.target.closest('.order-item'); if (target && draggedItem && target !== draggedItem) { var items = Array.from(container.querySelectorAll('.order-item')); if (items.indexOf(draggedItem) < items.indexOf(target)) container.insertBefore(draggedItem, target.nextSibling); else container.insertBefore(draggedItem, target); } container.querySelectorAll('.order-item').forEach(function(i) { i.classList.remove('drag-over'); }); });
        });
    });

    // ===== FREE RECORDING =====
    var freeRecorder = null;
    var freeChunks = [];
    function startFreeRecording(btn) {
        var stopBtn = btn.parentElement.querySelector('.btn-stop');
        navigator.mediaDevices.getUserMedia({ audio: true }).then(function(stream) {
            var mimeType = MediaRecorder.isTypeSupported('audio/mp4') ? 'audio/mp4' : MediaRecorder.isTypeSupported('audio/webm;codecs=opus') ? 'audio/webm;codecs=opus' : '';
            freeRecorder = mimeType ? new MediaRecorder(stream, { mimeType: mimeType }) : new MediaRecorder(stream);
            freeChunks = [];
            freeRecorder.ondataavailable = function(e) { if (e.data.size > 0) freeChunks.push(e.data); };
            freeRecorder.onstop = function() {
                var blob = new Blob(freeChunks, { type: freeRecorder.mimeType });
                var url = URL.createObjectURL(blob);
                var thinkCard = btn.closest('.think-card');
                var resultDiv = thinkCard.querySelector('[id^="think-result"]');
                if (resultDiv) resultDiv.innerHTML = '<audio controls src="' + url + '" style="width:100%;margin-top:0.5rem;"></audio><p style="font-size:0.72rem;color:var(--success);margin-top:0.3rem;">Grava&ccedil;&atilde;o salva!</p>';
                stream.getTracks().forEach(function(t) { t.stop(); });
            };
            freeRecorder.start(100);
            btn.classList.add('hidden');
            stopBtn.classList.add('visible');
        }).catch(function() { alert('N&atilde;o foi poss&iacute;vel acessar o microfone.'); });
    }

    function stopFreeRecording(stopBtn) {
        if (freeRecorder && freeRecorder.state === 'recording') freeRecorder.stop();
        var recordBtn = stopBtn.parentElement.querySelector('.btn-record');
        recordBtn.classList.remove('hidden');
        stopBtn.classList.remove('visible');
    }

    // ===== CHECKLIST =====
    function toggleChecklist(cb) {
        var li = cb.closest('li');
        if (cb.checked) li.classList.add('checked'); else li.classList.remove('checked');
        updateProgress();
    }

    // ===== PROGRESS =====
    function updateProgress() {
        var totalLessons = ${totalLessons};
        var completedLessons = 0;
        for (var l = 1; l <= totalLessons; l++) {
            var cl = document.getElementById('checklist-' + l);
            if (!cl) continue;
            var allChecks = cl.querySelectorAll('input[type="checkbox"]');
            var checkedChecks = cl.querySelectorAll('input[type="checkbox"]:checked');
            var lessonPct = allChecks.length > 0 ? Math.round(checkedChecks.length / allChecks.length * 100) : 0;
            var bar = document.querySelector('[data-lesson-progress="' + l + '"]');
            var lbl = document.querySelector('[data-lesson-pct="' + l + '"]');
            if (bar) bar.style.width = lessonPct + '%';
            if (lbl) lbl.textContent = lessonPct + '%';
            var stampEl = document.getElementById('stamp' + l);
            if (stampEl) { if (lessonPct === 100) stampEl.classList.add('earned'); else stampEl.classList.remove('earned'); }
            if (allChecks.length > 0 && checkedChecks.length === allChecks.length) completedLessons++;
        }
        var overallPct = Math.round(completedLessons / totalLessons * 100);
        var pb = document.getElementById('progressBar');
        var pp = document.getElementById('progressPercent');
        if (pb) pb.style.width = overallPct + '%';
        if (pp) pp.textContent = overallPct + '%';
        var celCard = document.getElementById('celebrationCard');
        if (celCard) celCard.style.display = overallPct === 100 ? 'block' : 'none';
        try { localStorage.setItem('alumni-progress-${SLUG}', JSON.stringify({ concluidas: completedLessons, total: totalLessons })); } catch(e) {}
        saveState();
    }

    function saveState() {
        var s = { dropdowns: [], blanks: [], quiz: [], speech: [], checklists: {}, mediaChecks: {}, matches: [] };
        document.querySelectorAll('.media-card-wrapper').forEach(function(w) { var id = w.dataset.media; var cb = w.querySelector('input[type="checkbox"]'); if (id && cb) s.mediaChecks[id] = cb.checked; });
        document.querySelectorAll('.match-row.correct select').forEach(function(sel) { s.matches.push(sel.closest('.match-row').querySelector('.match-word').textContent + '|' + sel.value); });
        document.querySelectorAll('.blank-input.correct').forEach(function(e) { s.blanks.push(e.dataset.answer); });
        document.querySelectorAll('.quiz-option.correct').forEach(function(e) { s.quiz.push(e.textContent.trim().substring(0, 30)); });
        document.querySelectorAll('.speech-result.good').forEach(function(e) { s.speech.push(e.closest('.speech-card').dataset.phrase); });
        document.querySelectorAll('.checklist input[type="checkbox"]').forEach(function(cb, i) { s.checklists[i] = cb.checked; });
        try { localStorage.setItem('${stateKey}', JSON.stringify(s)); } catch(e) {}
    }

    function loadState() {
        var r = localStorage.getItem('${stateKey}'); if (!r) return;
        try {
        var s = JSON.parse(r);
        if (s.matches) s.matches.forEach(function(d) { var parts = d.split('|'); var word = parts[0]; var val = parts[1]; document.querySelectorAll('.match-row').forEach(function(row) { if (row.querySelector('.match-word').textContent === word) { var sel = row.querySelector('select'); sel.value = val; row.classList.add('correct'); sel.disabled = true; } }); });
        if (s.blanks) s.blanks.forEach(function(a) { document.querySelectorAll('.blank-input[data-answer="' + a + '"]').forEach(function(e) { e.value = a; e.classList.add('correct'); }); });
        if (s.quiz) s.quiz.forEach(function(t) { document.querySelectorAll('.quiz-option[data-correct="true"]').forEach(function(e) { if (e.textContent.trim().substring(0, 30) === t) e.classList.add('correct'); }); });
        if (s.checklists) { document.querySelectorAll('.checklist input[type="checkbox"]').forEach(function(cb, i) { if (s.checklists[i]) { cb.checked = true; cb.closest('li').classList.add('checked'); } }); }
        if (s.mediaChecks) { document.querySelectorAll('.media-card-wrapper').forEach(function(w) { var id = w.dataset.media; var cb = w.querySelector('input[type="checkbox"]'); if (id && cb && s.mediaChecks[id]) { cb.checked = true; w.classList.add('done'); } }); }
        updateProgress();
        } catch(e) {}
    }

    function resetProgress() { if (confirm('Resetar todo o progresso?')) { localStorage.removeItem('${stateKey}'); location.reload(); } }

    function listenAllVocab(btn) {
        var section = btn.closest('.exercise-section') || btn.closest('.teacher-section');
        var audioBtns = section.querySelectorAll('.vocab-card .audio-btn');
        var i = 0;
        function playNext() { if (i < audioBtns.length) { audioBtns[i].click(); i++; setTimeout(playNext, 2500); } }
        playNext();
    }

    function verifyAllMatches(gridId) {
        var grid = document.getElementById(gridId);
        var rows = grid.querySelectorAll('.match-row');
        rows.forEach(function(row) {
            var select = row.querySelector('select');
            var answer = row.dataset.answer;
            row.classList.remove('correct', 'wrong');
            if (select.value === answer) { row.classList.add('correct'); }
            else if (select.value !== '') { row.classList.add('wrong'); setTimeout(function() { row.classList.remove('wrong'); }, 1800); }
        });
        updateProgress();
    }

    function checkMatch(select) {
        var row = select.closest('.match-row');
        var answer = row.dataset.answer;
        row.classList.remove('correct', 'wrong');
        if (select.value === answer) { row.classList.add('correct'); select.disabled = true; updateProgress(); }
        else if (select.value !== '') { row.classList.add('wrong'); setTimeout(function() { row.classList.remove('wrong'); select.value = ''; }, 1000); }
    }

    function toggleMediaDone(checkbox) {
        var wrapper = checkbox.closest('.media-card-wrapper');
        wrapper.classList.toggle('done', checkbox.checked);
        saveState();
    }

    // ===== INIT =====
    document.addEventListener('DOMContentLoaded', function() {
        loadState();
        document.querySelectorAll('.match-row select').forEach(function(sel) {
            var word = sel.closest('.match-row').querySelector('.match-word');
            if (word) sel.setAttribute('aria-label', 'Translation of ' + word.textContent);
        });
    });
`;
}

// ───────────────────────────────────────────── HEAD + SHELL
function buildShell({ role, body, title }) {
  const isProf = role === 'professor';
  return `<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="noindex, nofollow">
  <title>${title}</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Cormorant+Garamond:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/styles/material.css">
  <style>
    :root {
      --accent: #B91C1C;
      --accent-light: #DC2626;
      --accent-dark: #7F1D1D;
      --accent-dim: rgba(185,28,28,0.08);
      --accent-glow: rgba(185,28,28,0.05);
      --black: #1a1a2e;
      --bg: #f5f5f0;
      --bg-card: #ffffff;
      --bg-elevated: #f0f0eb;
      --bg-input: #fafaf7;
      --border: #d4d4cc;
      --border-light: #c0c0b8;
      --white: #1a1a2e;
      --text: #2d2d3a;
      --text-mid: #4a4a5a;
      --text-dim: #5c5c6c;
      --success: #16a34a;
      --success-bg: rgba(22,163,74,0.08);
      --success-border: rgba(22,163,74,0.25);
      --danger: #dc2626;
      --danger-bg: rgba(220,38,38,0.08);
      --danger-border: rgba(220,38,38,0.25);
      --warn: #d97706;
      --warn-bg: rgba(217,119,6,0.08);
      --warn-border: rgba(217,119,6,0.25);
    }
  </style>
</head>
<body>

<div class="logo-bar">
  <img src="/assets/logo-alumni.png" alt="Alumni by Better">
  <span class="${isProf ? 'prof-badge' : 'aluno-badge'}">${isProf ? 'PROFESSOR VIEW' : 'ALUNO'}</span>
</div>

<div class="header" style="background-image:url('https://images.unsplash.com/photo-1583422409516-2895a77efded?w=1600&q=80');">
  <div class="header-content">
    <div class="passport-badge">Travel English &middot; A2 &middot; 48 Aulas</div>
    <h1>Roberto Pires</h1>
    <p class="subtitle">De &ldquo;travo quando preciso falar&rdquo; a viajante independente em Barcelona e Paris.</p>
    <div class="student-info">
      <span>S&atilde;o Paulo, SP</span>
      <span>A2 (Pre-Intermediate)</span>
      <span>Empres&aacute;rio</span>
      <span>3x semana &middot; 60 min</span>
    </div>
    <div class="progress-passport">
      <div class="progress-label">
        <span>Progresso do Bloco 1 (Aulas 1-5)</span>
        <span id="progressPercent">0%</span>
      </div>
      <div class="progress-bar-outer">
        <div class="progress-bar-inner" id="progressBar"></div>
      </div>
    </div>
    <div class="stamps-row">
      <div class="stamp" id="stamp1" data-label="Diagn&oacute;stico" style="background-image:url('${LESSON_HERO[1]}')"></div>
      <div class="stamp" id="stamp2" data-label="Survival 1" style="background-image:url('${LESSON_HERO[2]}')"></div>
      <div class="stamp" id="stamp3" data-label="Survival 2" style="background-image:url('${LESSON_HERO[3]}')"></div>
      <div class="stamp" id="stamp4" data-label="Aeroporto" style="background-image:url('${LESSON_HERO[4]}')"></div>
      <div class="stamp" id="stamp5" data-label="Bagagem" style="background-image:url('${LESSON_HERO[5]}')"></div>
    </div>
  </div>
</div>

<div class="container">
  <div class="speed-control" style="justify-content:flex-end;">
    <span style="font-size:0.8rem;color:var(--text-dim);font-weight:500;">Velocidade do &aacute;udio:</span>
    <button class="speed-btn" data-speed="0.5" onclick="setAudioSpeed(0.5,this)">0.5x</button>
    <button class="speed-btn" data-speed="0.75" onclick="setAudioSpeed(0.75,this)">0.75x</button>
    <button class="speed-btn active" data-speed="1" onclick="setAudioSpeed(1,this)">1x</button>
    <button class="speed-btn" data-speed="1.25" onclick="setAudioSpeed(1.25,this)">1.25x</button>
  </div>

  ${body}

  <button class="reset-btn" onclick="resetProgress()">Resetar progresso</button>
</div>

<script>
${buildCanonicalJs(role)}
</script>

</body>
</html>`;
}

// ───────────────────────────────────────────── ASSEMBLY
function buildProfessor() {
  const body = `
  <div class="tabs">
    <button class="tab-btn active" onclick="switchTab('planning')">Planejamento</button>
    <button class="tab-btn" onclick="switchTab('exercises')">Pre-class</button>
    <button class="tab-btn" onclick="switchTab('plan')">Plano de Aula</button>
    <button class="tab-btn" onclick="switchTab('teacher')">Material do Professor</button>
    <button class="tab-btn" onclick="switchTab('complementary')">Complementares</button>
  </div>

  ${renderTabPlanning()}
  ${renderTabExercises()}
  ${renderTabPlan()}
  ${renderTabTeacher()}
  ${renderTabComplementary()}
`;
  const html = buildShell({
    role: 'professor',
    body,
    title: 'Alumni — Roberto Pires — Professor',
  });
  fs.writeFileSync(PROF_OUT, html, 'utf8');
  console.log('Professor written:', PROF_OUT, '(' + html.length + ' bytes)');
}

function buildAluno() {
  // Aluno: only Pre-class + Complementares (REGRA 3)
  // Make Pre-class the default active tab
  const exercisesTab = renderTabExercises().replace('class="tab-content"', 'class="tab-content active"');
  const body = `
  <div class="tabs">
    <button class="tab-btn active" onclick="switchTab('exercises')">Pre-class</button>
    <button class="tab-btn" onclick="switchTab('complementary')">Complementares</button>
  </div>

  ${exercisesTab}
  ${renderTabComplementary()}
`;
  const html = buildShell({
    role: 'aluno',
    body,
    title: 'Alumni — Roberto Pires — Aluno',
  });
  fs.writeFileSync(ALUNO_OUT, html, 'utf8');
  console.log('Aluno written:    ', ALUNO_OUT, '(' + html.length + ' bytes)');
}

buildProfessor();
buildAluno();
console.log('Done.');
