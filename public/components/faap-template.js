/* ═══════════════════════════════════════════════════════════════
   ALUMNI BY BETTER — FAAP LESSON TEMPLATE ENGINE
   Gera estrutura completa de aula no padrao FAAP.
   Usa os componentes de exercises.js, audio-generator.js e
   image-validator.js.

   Dependencias (carregue antes deste arquivo):
   - exercises.js      → createMatchingDropdown, createFillBlank, etc.
   - audio-generator.js → speakWithFallback, createAudioButton
   - image-validator.js → getThemeImages, validateAndFixImages

   Depende de design-system.css para estilos.
   ═══════════════════════════════════════════════════════════════ */

/* ── Microcopy banco — voz pedagogica FAAP ── */
const MICROCOPY = {
  objective: 'Este é o seu objetivo para esta aula. Ao final, você vai conseguir fazer isso com confiança.',
  gallery: 'Explore as imagens. Elas mostram o universo que você vai aprender a navegar em inglês.',
  intro: 'Leia com calma. Depois toque em <strong>Ouvir</strong> para escutar a pronúncia natural.',
  vocab: 'Estas são as palavras-chave da aula. Escute cada uma e repita em voz alta.',
  vocabPractice: 'Agora vamos praticar. Errou? Sem problema — é assim que se aprende.',
  context: 'Leia o texto, escute o áudio e depois pratique a pronúncia. Sem pressa.',
  grammar: 'Não precisa decorar. Precisa entender o padrão para usar na hora certa.',
  practice: 'Hora de praticar tudo junto. Faça os exercícios no seu ritmo.',
  thinkAboutIt: 'Aqui não tem certo ou errado. Use o inglês que você já tem.',
  checklist: 'Marque o que você já se sente capaz de fazer. Seja honesto(a) — é para você.',
  survivalCard: 'Estas frases são o seu kit de sobrevivência. Salve no celular ou tire um print.'
};

/* ── Lucide SVG icons (inline) ── */
const TPL_ICONS = {
  target: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>',
  image: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>',
  book: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>',
  volume: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>',
  award: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg>',
  checkCircle: '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>',
  zap: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>',
  brain: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96.44 2.5 2.5 0 0 1-2.96-3.08 3 3 0 0 1-.34-5.58 2.5 2.5 0 0 1 1.32-4.24 2.5 2.5 0 0 1 1.98-3A2.5 2.5 0 0 1 9.5 2z"/><path d="M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96.44 2.5 2.5 0 0 0 2.96-3.08 3 3 0 0 0 .34-5.58 2.5 2.5 0 0 0-1.32-4.24 2.5 2.5 0 0 0-1.98-3A2.5 2.5 0 0 0 14.5 2z"/></svg>',
  clipboard: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1" ry="1"/></svg>',
  shield: '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>'
};

function _esc(str) {
  return String(str || '').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}

/* ═══════════════════════════════════════════════════════════════
   SECTION RENDERERS
   Each returns a complete HTML string for one section.
   ═══════════════════════════════════════════════════════════════ */

/* ── 1. Objective ── */
function renderObjective(data) {
  return `
    <section class="lesson-objective" style="margin-top:var(--space-xl);">
      <div class="lesson-objective__label">${TPL_ICONS.target} OBJETIVO DA AULA ${data.number || ''}</div>
      <div class="lesson-objective__text">${_esc(data.objective)}</div>
      <p class="microcopy" style="margin-top:var(--space-md);margin-bottom:0;">${MICROCOPY.objective}</p>
    </section>`;
}

/* ── 2. Image Gallery ── */
function renderImageGallery(images, theme) {
  if (!images || images.length === 0) return '';

  let items = '';
  images.forEach((url, i) => {
    const label = theme ? `${_esc(theme)} ${i + 1}` : '';
    items += `
      <div class="image-gallery__item" data-label="${label}">
        <img src="${_esc(url)}" alt="${_esc(theme || 'Lesson image')} ${i + 1}" loading="lazy" onerror="this.style.display='none';">
      </div>`;
  });

  return `
    <section style="margin-top:var(--space-xl);">
      <h2 class="image-gallery__title">${TPL_ICONS.image} Explorar o universo: ${_esc(theme)}</h2>
      <p class="microcopy">${MICROCOPY.gallery}</p>
      <div class="image-gallery">
        ${items}
      </div>
    </section>`;
}

/* ── 3. Introduction ── */
function renderIntroduction(data) {
  const audioBtn = data.context && data.context.introAudio
    ? `<button class="audio-btn-student" onclick="(function(){var a=new Audio('${_esc(data.context.introAudio)}');a.play().catch(function(){var u=new SpeechSynthesisUtterance('${_esc((data.context.introText || '').replace(/'/g, "\\'"))}');u.lang='en-US';u.rate=0.85;speechSynthesis.speak(u);});})()">${TPL_ICONS.volume} Ouvir</button>`
    : (data.context && data.context.introText
      ? `<button class="audio-btn-student" onclick="(function(){var u=new SpeechSynthesisUtterance('${_esc(data.context.introText.replace(/'/g, "\\'"))}');u.lang='en-US';u.rate=0.85;speechSynthesis.speak(u);})()">${TPL_ICONS.volume} Ouvir</button>`
      : '');

  const introText = (data.context && data.context.introText) || '';
  if (!introText) return '';

  return `
    <section style="margin-top:var(--space-xl);">
      <h2 style="font:var(--text-h2);color:var(--text-primary);margin-bottom:var(--space-sm);">${TPL_ICONS.book} Introduction</h2>
      <p class="microcopy">${MICROCOPY.intro}</p>
      <div class="card" style="line-height:1.8;font:var(--text-base);">
        ${introText}
        <div style="margin-top:var(--space-md);">${audioBtn}</div>
      </div>
    </section>`;
}

/* ── 4. Vocabulary ── */
function renderVocabulary(vocab) {
  if (!vocab || vocab.length === 0) return '';

  let items = '';
  vocab.forEach((item, i) => {
    const audioHandler = item.audio
      ? `var a=new Audio('${_esc(item.audio)}');a.play().catch(function(){var u=new SpeechSynthesisUtterance('${_esc(item.en.replace(/'/g, "\\'"))}');u.lang='en-US';u.rate=0.85;speechSynthesis.speak(u);});`
      : `var u=new SpeechSynthesisUtterance('${_esc(item.en.replace(/'/g, "\\'"))}');u.lang='en-US';u.rate=0.85;speechSynthesis.speak(u);`;

    items += `
      <div class="card" style="padding:var(--space-md) var(--space-lg);margin-bottom:var(--space-sm);">
        <div style="display:flex;align-items:center;justify-content:space-between;gap:var(--space-md);flex-wrap:wrap;">
          <div style="flex:1;min-width:200px;">
            <div style="font:var(--text-h3);color:var(--alumni-navy);margin-bottom:2px;">${_esc(item.en)}</div>
            <div style="font:var(--text-small);color:var(--text-dim);font-style:italic;">${_esc(item.pt)}</div>
          </div>
          <button class="btn btn--secondary btn--sm" onclick="(function(){${audioHandler}})()" style="flex-shrink:0;" aria-label="Ouvir ${_esc(item.en)}">
            ${TPL_ICONS.volume}
          </button>
        </div>
        ${item.example ? `<div style="margin-top:var(--space-sm);font:var(--text-small);color:var(--text-muted);padding:var(--space-xs) var(--space-sm);background:var(--bg-subtle);border-radius:var(--radius-sm);">"${_esc(item.example)}"</div>` : ''}
      </div>`;
  });

  return `
    <section style="margin-top:var(--space-xl);">
      <h2 style="font:var(--text-h2);color:var(--text-primary);margin-bottom:var(--space-sm);">${TPL_ICONS.book} Vocabulary</h2>
      <p class="microcopy">${MICROCOPY.vocab}</p>
      ${items}
    </section>`;
}

/* ── 5. Vocabulary Practice (V1-V4) ── */
function renderVocabPractice(data) {
  if (!data.vocab || data.vocab.length < 2) return '';

  let html = `
    <section style="margin-top:var(--space-xl);">
      <h2 style="font:var(--text-h2);color:var(--text-primary);margin-bottom:var(--space-sm);">${TPL_ICONS.zap} Vocabulary Practice</h2>
      <p class="microcopy">${MICROCOPY.vocabPractice}</p>`;

  // V1: Matching Dropdown
  if (typeof createMatchingDropdown === 'function') {
    const pairs = data.vocab.slice(0, 5).map(v => {
      const wrongOptions = data.vocab
        .filter(w => w.pt !== v.pt)
        .map(w => w.pt)
        .sort(() => Math.random() - 0.5)
        .slice(0, 2);
      return {
        en: v.en,
        options: [v.pt, ...wrongOptions].sort(() => Math.random() - 0.5),
        correct: v.pt
      };
    });
    html += createMatchingDropdown(
      `${data.number || 'lesson'}_v1_matching`,
      pairs
    );
  }

  // V2: Fill-in with hint
  if (typeof createFillBlankWithHint === 'function' && data.vocab.length >= 3) {
    const items = data.vocab.slice(0, 4).filter(v => v.example).map(v => {
      const answer = v.en.toLowerCase();
      const sentence = v.example.replace(new RegExp(v.en, 'gi'), '___');
      return { sentence, answer, hint: v.pt };
    });
    if (items.length > 0) {
      html += createFillBlankWithHint(
        `${data.number || 'lesson'}_v2_fill`,
        items
      );
    }
  }

  html += '</section>';
  return html;
}

/* ── 6. Context ── */
function renderContext(context) {
  if (!context || !context.text) return '';

  const audioBtn = context.audio
    ? `<button class="audio-btn-student" onclick="(function(){var a=new Audio('${_esc(context.audio)}');a.play().catch(function(){var u=new SpeechSynthesisUtterance('${_esc(context.text.substring(0,200).replace(/'/g, "\\'"))}');u.lang='en-US';u.rate=0.85;speechSynthesis.speak(u);});})()">${TPL_ICONS.volume} Ouvir o texto</button>`
    : `<button class="audio-btn-student" onclick="(function(){var u=new SpeechSynthesisUtterance('${_esc(context.text.substring(0,500).replace(/'/g, "\\'"))}');u.lang='en-US';u.rate=0.85;speechSynthesis.speak(u);})()">${TPL_ICONS.volume} Ouvir o texto</button>`;

  let pronunciationBlock = '';
  if (typeof createPronunciation === 'function') {
    // Pick a key sentence for pronunciation practice
    const sentences = context.text.split(/[.!?]+/).filter(s => s.trim().length > 10);
    const targetSentence = sentences[0] ? sentences[0].trim() : context.text.substring(0, 60);
    pronunciationBlock = createPronunciation(
      'context_pronunciation',
      targetSentence,
      context.audio || null
    );
  }

  return `
    <section style="margin-top:var(--space-xl);">
      <h2 style="font:var(--text-h2);color:var(--text-primary);margin-bottom:var(--space-sm);">${TPL_ICONS.book} Context</h2>
      <p class="microcopy">${MICROCOPY.context}</p>
      <div class="card" style="line-height:1.9;font:var(--text-base);">
        ${context.text}
        <div style="margin-top:var(--space-lg);">${audioBtn}</div>
      </div>
      ${pronunciationBlock}
    </section>`;
}

/* ── 7. Grammar ── */
function renderGrammar(grammar) {
  if (!grammar) return '';

  const audioBtn = grammar.audio
    ? `<button class="audio-btn-student" onclick="(function(){var a=new Audio('${_esc(grammar.audio)}');a.play();})()">${TPL_ICONS.volume} Ouvir</button>`
    : (grammar.text
      ? `<button class="audio-btn-student" onclick="(function(){var u=new SpeechSynthesisUtterance('${_esc(grammar.text.substring(0,400).replace(/'/g, "\\'"))}');u.lang='en-US';u.rate=0.85;speechSynthesis.speak(u);})()">${TPL_ICONS.volume} Ouvir</button>`
      : '');

  let examplesHtml = '';
  if (grammar.examples && grammar.examples.length > 0) {
    examplesHtml = '<div style="margin-top:var(--space-md);">';
    grammar.examples.forEach(ex => {
      const exText = typeof ex === 'string' ? ex : ex.text || ex.en || '';
      examplesHtml += `
        <div style="padding:var(--space-sm) var(--space-md);background:var(--bg-subtle);border-radius:var(--radius-sm);margin-bottom:var(--space-xs);font:var(--text-base);border-left:3px solid var(--alumni-navy);">
          ${_esc(exText)}
        </div>`;
    });
    examplesHtml += '</div>';
  }

  return `
    <section style="margin-top:var(--space-xl);">
      <h2 style="font:var(--text-h2);color:var(--text-primary);margin-bottom:var(--space-sm);">${TPL_ICONS.brain} Grammar</h2>
      <p class="pedagogy-voice">${MICROCOPY.grammar}</p>
      <div class="card card--bordered-left">
        <h3 style="font:var(--text-h3);color:var(--alumni-navy);margin-bottom:var(--space-sm);">${_esc(grammar.rule || '')}</h3>
        <div style="font:var(--text-base);line-height:1.8;">
          ${grammar.text || grammar.explanation || ''}
        </div>
        ${examplesHtml}
        <div style="margin-top:var(--space-md);">${audioBtn}</div>
      </div>
    </section>`;
}

/* ── 8. Main Practice (10 exercises) ── */
function renderMainPractice(exercises) {
  if (!exercises || exercises.length === 0) return '';

  let html = `
    <section style="margin-top:var(--space-2xl);">
      <h2 style="font:var(--text-h2);color:var(--text-primary);margin-bottom:var(--space-sm);">${TPL_ICONS.zap} Practice</h2>
      <p class="microcopy">${MICROCOPY.practice}</p>`;

  exercises.forEach((ex, i) => {
    const exId = `practice_ex_${i + 1}`;

    switch (ex.type) {
      case 'matching':
      case 'matchingDropdown':
        if (typeof createMatchingDropdown === 'function') {
          html += createMatchingDropdown(exId, ex.data.pairs || ex.data);
        }
        break;

      case 'fillBlank':
      case 'fill':
        if (typeof createFillBlank === 'function') {
          html += createFillBlank(exId, ex.data.items || ex.data);
        }
        break;

      case 'fillBlankHint':
      case 'fillHint':
        if (typeof createFillBlankWithHint === 'function') {
          html += createFillBlankWithHint(exId, ex.data.items || ex.data);
        }
        break;

      case 'multipleChoice':
      case 'quiz':
        if (typeof createMultipleChoice === 'function') {
          html += createMultipleChoice(
            exId,
            ex.data.question,
            ex.data.options,
            ex.data.correctIndex
          );
        }
        break;

      case 'ordering':
      case 'order':
        if (typeof createOrdering === 'function') {
          html += createOrdering(
            exId,
            ex.data.correctOrder,
            ex.data.shuffledOrder || _shuffleExerciseOrder(ex.data.correctOrder)
          );
        }
        break;

      case 'pronunciation':
      case 'speak':
        if (typeof createPronunciation === 'function') {
          html += createPronunciation(
            exId,
            ex.data.targetPhrase || ex.data.phrase,
            ex.data.audioSrc || ex.data.audio || null
          );
        }
        break;

      case 'thinkAboutIt':
      case 'think':
        if (typeof createThinkAboutIt === 'function') {
          html += createThinkAboutIt(
            exId,
            ex.data.question || ex.data
          );
        }
        break;

      default:
        html += `<div class="card" style="margin-bottom:var(--space-md);padding:var(--space-lg);"><p style="color:var(--text-dim);">Tipo de exercicio desconhecido: ${_esc(ex.type)}</p></div>`;
    }
  });

  html += '</section>';
  return html;
}

/* Helper: shuffle array for ordering exercises */
function _shuffleExerciseOrder(arr) {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  // Ensure it's actually shuffled (not identical to original)
  if (JSON.stringify(a) === JSON.stringify(arr) && a.length > 1) {
    [a[0], a[1]] = [a[1], a[0]];
  }
  return a;
}

/* ── 9. Think About It ── */
function renderThinkAboutIt(question) {
  if (!question) return '';
  if (typeof createThinkAboutIt === 'function') {
    return `
      <section style="margin-top:var(--space-xl);">
        <h2 style="font:var(--text-h2);color:var(--text-primary);margin-bottom:var(--space-sm);">${TPL_ICONS.brain} Think About It</h2>
        <p class="microcopy">${MICROCOPY.thinkAboutIt}</p>
        ${createThinkAboutIt('lesson_think_about_it', question)}
      </section>`;
  }

  // Fallback if exercises.js not loaded
  return `
    <section style="margin-top:var(--space-xl);">
      <h2 style="font:var(--text-h2);color:var(--text-primary);margin-bottom:var(--space-sm);">${TPL_ICONS.brain} Think About It</h2>
      <p class="microcopy">${MICROCOPY.thinkAboutIt}</p>
      <div class="card card--bordered-left" style="border-left-color:#7c3aed;">
        <p style="font:var(--text-base);font-weight:500;line-height:1.7;">${_esc(question)}</p>
      </div>
    </section>`;
}

/* ── 10. Checklist "O que eu aprendi" ── */
function renderChecklist(items, studentName) {
  if (!items || items.length === 0) return '';

  let listItems = '';
  items.forEach((item, i) => {
    listItems += `
      <li class="learning-checklist__item" id="checklist_item_${i}" onclick="(function(){
        var el = document.getElementById('checklist_item_${i}');
        el.classList.toggle('is-checked');
        // Save to localStorage
        var key = 'alumni_checklist_' + (location.pathname || 'lesson');
        var state = JSON.parse(localStorage.getItem(key) || '{}');
        state[${i}] = el.classList.contains('is-checked');
        localStorage.setItem(key, JSON.stringify(state));
      })()" style="cursor:pointer;user-select:none;">
        ${_esc(item)}
      </li>`;
  });

  return `
    <section style="margin-top:var(--space-xl);">
      <h2 style="font:var(--text-h2);color:var(--text-primary);margin-bottom:var(--space-sm);">${TPL_ICONS.clipboard} O que eu aprendi</h2>
      <p class="microcopy">${MICROCOPY.checklist}</p>
      <div class="learning-checklist">
        <div class="learning-checklist__title">${studentName ? _esc(studentName) + ', ' : ''}marque o que você já consegue fazer:</div>
        <ul class="learning-checklist__items">
          ${listItems}
        </ul>
      </div>
      <script>
      (function(){
        var key = 'alumni_checklist_' + (location.pathname || 'lesson');
        var state = JSON.parse(localStorage.getItem(key) || '{}');
        for(var idx in state){
          if(state[idx]){
            var el = document.getElementById('checklist_item_' + idx);
            if(el) el.classList.add('is-checked');
          }
        }
      })();
      </script>
    </section>`;
}

/* ── 11. Survival Card ── */
function renderSurvivalCard(phrases, studentName) {
  if (!phrases || phrases.length === 0) return '';

  let phraseItems = '';
  phrases.forEach((phrase, i) => {
    const text = typeof phrase === 'string' ? phrase : phrase.text || phrase.en || '';
    const pt = typeof phrase === 'object' ? (phrase.pt || '') : '';

    phraseItems += `
      <div style="padding:var(--space-sm) 0;border-bottom:1px solid var(--border-light);display:flex;align-items:center;gap:var(--space-sm);">
        <span style="width:24px;height:24px;background:var(--alumni-navy);color:var(--text-inverse);border-radius:var(--radius-full);display:flex;align-items:center;justify-content:center;font:var(--text-micro);font-weight:700;flex-shrink:0;">${i + 1}</span>
        <div style="flex:1;">
          <div style="font:var(--text-base);font-weight:600;color:var(--text-primary);">${_esc(text)}</div>
          ${pt ? `<div style="font:var(--text-small);color:var(--text-dim);font-style:italic;">${_esc(pt)}</div>` : ''}
        </div>
        <button class="btn btn--ghost btn--sm" style="flex-shrink:0;padding:6px;" onclick="(function(){var u=new SpeechSynthesisUtterance('${_esc(text.replace(/'/g, "\\'"))}');u.lang='en-US';u.rate=0.85;speechSynthesis.speak(u);})()" aria-label="Ouvir">${TPL_ICONS.volume}</button>
      </div>`;
  });

  return `
    <section style="margin-top:var(--space-xl);">
      <h2 style="font:var(--text-h2);color:var(--text-primary);margin-bottom:var(--space-sm);">${TPL_ICONS.shield} Survival Card</h2>
      <p class="microcopy">${MICROCOPY.survivalCard}</p>
      <div class="survival-card">
        <div class="survival-card__title">${TPL_ICONS.award} ${studentName ? _esc(studentName) + ' — ' : ''}Survival Card</div>
        ${phraseItems}
      </div>
    </section>`;
}


/* ═══════════════════════════════════════════════════════════════
   MAIN GENERATOR: generateFAAPLesson(lessonData)

   lessonData: {
     number: 1,
     theme: "Hotel Check-in",
     objective: "Ao final desta aula...",
     studentName: "Zilaudio",
     vocab: [{en, pt, example, audio}],
     context: {text, audio, introText, introAudio},
     grammar: {rule, text, examples, audio},
     exercises: [{type, data}],
     thinkAboutIt: "question string",
     checklist: ["Consigo pedir um quarto", ...],
     images: ["url1", "url2", ...],
     survivalCard: ["phrase1", ...] or [{text, pt}]
   }

   Returns: complete HTML string for the lesson body.
   ═══════════════════════════════════════════════════════════════ */
function generateFAAPLesson(lessonData) {
  const data = lessonData || {};
  let html = '';

  // 1. Header with objective
  html += renderObjective(data);

  // 2. Image gallery
  if (data.images && data.images.length > 0) {
    html += renderImageGallery(data.images, data.theme);
  } else if (data.theme && typeof getThemeImages === 'function') {
    // Auto-generate theme images from image-validator
    const autoImages = getThemeImages(data.theme, 6);
    html += renderImageGallery(autoImages, data.theme);
  }

  // 3. Introduction
  html += renderIntroduction(data);

  // 4. Vocabulary
  html += renderVocabulary(data.vocab);

  // 5. Vocabulary practice (V1-V4)
  html += renderVocabPractice(data);

  // 6. Context with audio + pronunciation
  html += renderContext(data.context);

  // 7. Grammar
  html += renderGrammar(data.grammar);

  // 8. Main practice (exercises)
  html += renderMainPractice(data.exercises);

  // 9. Think about it
  html += renderThinkAboutIt(data.thinkAboutIt);

  // 10. Checklist
  html += renderChecklist(data.checklist, data.studentName);

  // 11. Survival Card
  html += renderSurvivalCard(data.survivalCard, data.studentName);

  return html;
}


/* ═══════════════════════════════════════════════════════════════
   generateFullPage(lessonData, options)
   Gera uma pagina HTML completa (com <html>, <head>, etc.)
   pronta para deploy.

   options: {
     cssPath: path to design-system.css,
     logoPath: path to Alumni logo,
     prevLesson: url or null,
     nextLesson: url or null
   }
   ═══════════════════════════════════════════════════════════════ */
function generateFullPage(lessonData, options) {
  options = options || {};
  const cssPath = options.cssPath || '/styles/design-system.css';
  const logoPath = options.logoPath || '/assets/alumni-logo.png';
  const data = lessonData || {};

  const lessonBody = generateFAAPLesson(data);

  let nav = '';
  if (options.prevLesson || options.nextLesson) {
    nav = `
      <div style="display:flex;justify-content:space-between;align-items:center;padding:var(--space-lg) 0;margin-top:var(--space-2xl);border-top:1px solid var(--border-light);">
        ${options.prevLesson ? `<a href="${_esc(options.prevLesson)}" class="btn btn--ghost">&larr; Voltar</a>` : '<span></span>'}
        ${options.nextLesson ? `<a href="${_esc(options.nextLesson)}" class="btn btn--primary">Proxima &rarr;</a>` : '<span></span>'}
      </div>`;
  }

  return `<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="theme-color" content="#003080">
  <title>Aula ${_esc(String(data.number || ''))} — ${_esc(data.theme || 'Alumni')}</title>
  <link rel="stylesheet" href="${_esc(cssPath)}">
</head>
<body>
  <header class="alumni-header">
    <img src="${_esc(logoPath)}" alt="Alumni by Better" class="alumni-header__logo">
    <div class="alumni-header__title">Aula ${_esc(String(data.number || ''))} — ${_esc(data.theme || '')}</div>
    <span class="alumni-header__badge">${_esc(data.studentName || 'Aluno')}</span>
  </header>

  <main class="container">
    ${lessonBody}
    ${nav}
  </main>

  <footer class="alumni-footer">
    <img src="${_esc(logoPath)}" alt="Alumni by Better" class="alumni-footer__logo">
  </footer>

  <script src="/components/exercises.js"><\/script>
  <script src="/components/activity-tracker.js"><\/script>
  <script src="/components/audio-generator.js"><\/script>
  <script src="/components/image-validator.js"><\/script>
</body>
</html>`;
}


/* ═══════════════════════════════════════════════════════════════
   EXPORTS
   ═══════════════════════════════════════════════════════════════ */
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    MICROCOPY,
    generateFAAPLesson,
    generateFullPage,
    renderObjective,
    renderImageGallery,
    renderIntroduction,
    renderVocabulary,
    renderVocabPractice,
    renderContext,
    renderGrammar,
    renderMainPractice,
    renderThinkAboutIt,
    renderChecklist,
    renderSurvivalCard
  };
}
