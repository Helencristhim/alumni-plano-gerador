// Helpers compartilhados entre professor e aluno (CSS, escape, JS comum)

function esc(str) {
  if (str == null) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function escAttr(str) {
  return esc(str).replace(/'/g, '&#39;');
}

// Escape texto para usar dentro de onclick="speakText('...')"
function escForJS(text) {
  return text.replace(/\\/g, '\\\\').replace(/'/g, "\\'").replace(/"/g, '&quot;');
}

// Paleta Gabriela: rose-coral (Paris/teen pop) + navy
const cssVars = `
:root {
  --accent: #d4326a;
  --accent-light: #e85d8a;
  --accent-dim: rgba(212,50,106,0.08);
  --accent-glow: rgba(212,50,106,0.05);
  --black: #1a1a2e;
  --bg: #f6f3ef;
  --bg-card: #ffffff;
  --bg-card-hover: #fafaf7;
  --bg-elevated: #f0eee9;
  --bg-input: #fafaf7;
  --border: #d8d1c8;
  --border-light: #c4bdb3;
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
  --navy: #1e2a4a;
}
`;

const cssMain = `
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family:'Inter',-apple-system,sans-serif; background:var(--bg); color:var(--text); line-height:1.7; font-size:16px; -webkit-font-smoothing:antialiased; }

.logo-bar { display:flex; align-items:center; justify-content:space-between; padding:1rem 2rem; background:var(--bg-card); border-bottom:1px solid var(--border); }
.logo-bar img { height:36px; }
.logo-bar .prof-badge, .logo-bar .student-badge { font-size:0.7rem; font-weight:700; letter-spacing:2px; text-transform:uppercase; color:#fff; background:var(--accent); padding:0.35rem 0.9rem; border-radius:4px; }

.header { position:relative; min-height:340px; display:flex; align-items:flex-end; padding:3rem 2rem; overflow:hidden; background:url('https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=1400&q=80') center/cover no-repeat; }
.header::before { content:''; position:absolute; inset:0; background:linear-gradient(to top,rgba(26,26,46,0.92) 0%,rgba(26,26,46,0.75) 40%,rgba(26,26,46,0.55) 100%); }
.header-content { position:relative; z-index:1; max-width:900px; margin:0 auto; width:100%; }
.passport-badge { display:inline-flex; align-items:center; gap:0.5rem; background:var(--accent); padding:0.5rem 1.2rem; font-size:0.75rem; font-weight:700; letter-spacing:3px; text-transform:uppercase; color:#fff; margin-bottom:1.2rem; border-radius:4px; }
.header h1 { font-family:'Cormorant Garamond',serif; font-size:3.2rem; font-weight:700; color:#fff; line-height:1.1; margin-bottom:0.5rem; }
.header .subtitle { font-size:1rem; color:#fff; margin-bottom:2rem; max-width:600px; text-shadow:0 1px 4px rgba(0,0,0,0.6); }
.student-info { display:flex; gap:2rem; flex-wrap:wrap; font-size:0.875rem; color:#e8e8e8; font-weight:500; text-shadow:0 1px 3px rgba(0,0,0,0.5); letter-spacing:0.5px; }
.student-info span { display:flex; align-items:center; gap:0.4rem; }
.student-info span::before { content:''; width:4px; height:4px; border-radius:50%; background:var(--accent-light); }

.progress-passport { margin-top:2rem; background:rgba(0,0,0,0.35); padding:1.2rem 1.5rem; border:1px solid rgba(255,255,255,0.15); backdrop-filter:blur(20px); }
.progress-passport .progress-label { display:flex; justify-content:space-between; font-size:0.8rem; color:#fff; font-weight:600; margin-bottom:0.6rem; letter-spacing:1.5px; text-transform:uppercase; }
.progress-bar-outer { background:rgba(255,255,255,0.2); height:6px; overflow:hidden; border-radius:3px; }
.progress-bar-inner { height:100%; background:var(--accent-light); transition:width 0.6s ease; width:0%; border-radius:3px; }
.stamps-row { display:flex; gap:0.8rem; margin-top:1.2rem; flex-wrap:wrap; }
.stamp { width:64px; height:64px; border-radius:4px; overflow:hidden; border:1px solid var(--border); position:relative; opacity:0.3; transition:all 0.4s ease; background-size:cover; background-position:center; filter:grayscale(100%); }
.stamp::after { content:attr(data-label); position:absolute; bottom:0; left:0; right:0; padding:0.15rem 0.2rem; font-size:0.5rem; font-weight:600; letter-spacing:1px; text-transform:uppercase; text-align:center; background:linear-gradient(transparent,rgba(0,0,0,0.9)); color:#d4d4d4; }
.stamp.earned { opacity:1; border-color:var(--accent-light); filter:grayscale(0%); box-shadow:0 0 20px rgba(212,50,106,0.3); }
.stamp.earned::after { color:#fff; }

.container { max-width:960px; margin:0 auto; padding:2rem 3rem; }
@media (max-width:768px) { .container { padding:1.5rem 1rem; } .header h1 { font-size:2.2rem; } .header { padding:2rem 1rem; } }

.tabs { display:flex; gap:0; border-bottom:1px solid var(--border); margin-bottom:2.5rem; overflow-x:auto; }
.tab-btn { flex:1; padding:1rem 0.5rem; border:none; background:transparent; cursor:pointer; font-family:'Inter',sans-serif; font-size:0.78rem; font-weight:500; color:var(--text-dim); transition:all 0.2s ease-out; letter-spacing:1px; text-transform:uppercase; position:relative; white-space:nowrap; min-height:44px; }
.tab-btn.active { color:var(--white); }
.tab-btn.active::after { content:''; position:absolute; bottom:-1px; left:0; right:0; height:2px; background:var(--accent); }
.tab-btn:hover:not(.active) { color:var(--text-mid); }
.tab-btn:focus-visible { outline:3px solid var(--accent); outline-offset:-2px; }
.tab-content { display:none; }
.tab-content.active { display:block; animation:fadeIn 0.4s ease; }

@keyframes fadeIn { from { opacity:0; transform:translateY(10px); } to { opacity:1; transform:translateY(0); } }
@keyframes shake { 0%,100% { transform:translateX(0); } 25% { transform:translateX(-4px); } 75% { transform:translateX(4px); } }
@keyframes pulse { 0%,100% { box-shadow:0 0 0 0 rgba(212,50,106,0.3); } 50% { box-shadow:0 0 0 8px rgba(212,50,106,0); } }

.lesson-card { background:var(--bg-card); border:1px solid var(--border); overflow:hidden; margin-bottom:1.5rem; transition:border-color 0.3s ease; box-shadow:0 1px 3px rgba(0,0,0,0.06); border-radius:6px; }
.lesson-card:hover { border-color:var(--border-light); }
.lesson-header { padding:0; cursor:pointer; display:flex; align-items:stretch; position:relative; user-select:none; min-height:140px; overflow:hidden; }
.lesson-header-img { width:200px; min-height:100%; background-size:cover; background-position:center; position:relative; flex-shrink:0; }
.lesson-header-img::after { content:''; position:absolute; inset:0; background:linear-gradient(to right,transparent 50%,rgba(255,255,255,0.85) 100%); }
.lesson-header-content { flex:1; padding:1.5rem; display:flex; flex-direction:column; justify-content:center; }
.lesson-number { font-size:0.75rem; font-weight:600; letter-spacing:3px; text-transform:uppercase; color:var(--accent); margin-bottom:0.4rem; }
.lesson-header-content h3 { font-family:'Cormorant Garamond',serif; font-size:1.6rem; font-weight:600; color:var(--white); margin-bottom:0.3rem; line-height:1.2; }
.lesson-desc { font-size:0.875rem; color:var(--text-dim); }
.lesson-progress-mini { display:flex; align-items:center; gap:0.6rem; margin-top:0.8rem; }
.mini-bar { flex:1; height:5px; background:var(--border); max-width:120px; overflow:hidden; border-radius:3px; }
.mini-bar-fill { height:100%; background:var(--accent); transition:width 0.3s ease; border-radius:3px; }
.mini-percent { font-size:0.75rem; color:var(--text-dim); letter-spacing:1px; font-weight:500; }
.expand-icon { position:absolute; right:1.5rem; top:50%; transform:translateY(-50%); font-size:0.7rem; color:var(--text-dim); transition:transform 0.3s ease; }
.lesson-card.open .expand-icon { transform:translateY(-50%) rotate(180deg); }
.lesson-body { display:none; padding:2rem 2.5rem; border-top:1px solid var(--border); }
.lesson-card.open .lesson-body { display:block; animation:fadeIn 0.3s ease; }
@media (max-width:768px) { .lesson-header-img { width:120px; } .lesson-body { padding:1.5rem 1rem; } }

.exercise-section { background:var(--bg-elevated); padding:1.5rem; margin-bottom:2rem; border:1px solid var(--border); border-radius:6px; }
@media (min-width:376px) { .exercise-section { padding:2rem; } }
.exercise-section h4 { font-family:'Cormorant Garamond',serif; font-size:1.25rem; font-weight:700; margin-bottom:0.75rem; display:flex; align-items:center; gap:0.6rem; color:var(--text); padding-bottom:0.8rem; border-bottom:3px solid var(--accent); flex-wrap:wrap; }
.exercise-section h4 .badge { font-family:'Inter',sans-serif; font-size:0.7rem; padding:0.3rem 0.7rem; font-weight:700; letter-spacing:1.2px; text-transform:uppercase; border-radius:3px; }
.badge-vocab { background:rgba(139,105,20,0.15); color:#5c4a08; border:1px solid rgba(139,105,20,0.35); }
.badge-speak { background:rgba(120,40,200,0.12); color:#581c87; border:1px solid rgba(120,40,200,0.35); }
.badge-practice { background:rgba(20,130,60,0.12); color:#166534; border:1px solid rgba(20,130,60,0.35); }
.badge-quiz { background:rgba(200,40,60,0.12); color:#991b1b; border:1px solid rgba(200,40,60,0.35); }
.badge-order { background:rgba(212,50,106,0.12); color:#9d1f50; border:1px solid rgba(212,50,106,0.35); }
.badge-think { background:rgba(180,130,20,0.15); color:#6b4c0a; border:1px solid rgba(180,130,20,0.4); }

.microcopy { font-size:0.875rem; color:var(--text-dim); margin-bottom:1rem; font-style:italic; }

.vocab-cards { display:grid; gap:0.6rem; margin-bottom:1rem; }
.vocab-card { background:var(--bg-card); border:1px solid var(--border); border-radius:6px; padding:1rem 1.2rem; display:flex; align-items:flex-start; justify-content:space-between; gap:1rem; transition:border-color 0.2s ease; }
.vocab-card:hover { border-color:var(--accent); }
.vocab-card-content { flex:1; }
.vocab-card-header { display:flex; align-items:baseline; gap:0.5rem; margin-bottom:0.3rem; flex-wrap:wrap; }
.vocab-card-word { font-weight:700; font-size:1rem; color:var(--white); }
.vocab-card-dot { color:var(--accent); font-weight:700; }
.vocab-card-translation { font-weight:500; font-size:0.88rem; color:var(--text-mid); }
.vocab-card-example { font-size:0.875rem; color:var(--text-dim); font-style:italic; margin-top:0.2rem; line-height:1.5; }

.section-header-row { display:flex; align-items:center; justify-content:space-between; margin-bottom:1rem; flex-wrap:wrap; gap:0.5rem; }
.section-header-row h4 { margin-bottom:0; }
.listen-all-btn { display:inline-flex; align-items:center; gap:0.3rem; background:var(--accent-dim); color:var(--accent); border:1.5px solid var(--accent); padding:0.5rem 1rem; font-size:0.8rem; cursor:pointer; border-radius:20px; font-weight:600; transition:all 0.2s ease-out; min-height:44px; }
.listen-all-btn:hover { background:var(--accent); color:#fff; }
.verify-all-btn { display:inline-flex; align-items:center; gap:0.4rem; margin-top:1rem; padding:0.6rem 1.5rem; background:var(--accent); color:#fff; border:none; font-size:0.8rem; font-weight:600; cursor:pointer; border-radius:6px; min-height:44px; }
.verify-all-btn:hover { background:var(--accent-light); }

.match-grid { display:grid; gap:0.6rem; }
.match-row { display:flex; align-items:center; gap:1rem; background:var(--bg-elevated); border:1px solid var(--border); padding:0.8rem 1rem; border-radius:6px; transition:all 0.2s ease; }
.match-row .match-word { font-weight:600; font-size:0.92rem; color:var(--white); min-width:160px; padding:0.5rem 0.8rem; background:var(--bg-card); border:1px solid var(--border); border-radius:4px; flex-shrink:0; }
.match-row select { flex:1; padding:0.75rem 1rem; border:1px solid var(--border); background:#fff; font-family:'Inter',sans-serif; font-size:0.875rem; color:var(--text); border-radius:4px; min-height:44px; cursor:pointer; outline:none; transition:border-color 0.2s ease-out; }
.match-row select:focus { border-color:var(--accent); box-shadow:0 0 0 3px rgba(212,50,106,0.15); }
.match-row.correct { border-color:var(--success); background:var(--success-bg); }
.match-row.correct select { border-color:var(--success); color:var(--success); pointer-events:none; }
.match-row.wrong { border-color:var(--danger); background:var(--danger-bg); animation:shake 0.4s ease; }
@media (max-width:600px) { .match-row { flex-direction:column; align-items:stretch; } .match-row .match-word { min-width:0; } }

.fill-blank-item { background:var(--bg-card); border:1px solid var(--border); padding:1rem; margin-bottom:0.6rem; border-radius:6px; }
.fill-blank-sentence { font-size:0.95rem; color:var(--text); margin-bottom:0.6rem; line-height:1.8; }
.blank-input { display:inline-block; min-width:120px; padding:0.4rem 0.7rem; border:1px solid var(--border); background:#fff; font-size:0.92rem; border-radius:4px; outline:none; transition:all 0.2s ease; }
.blank-input:focus { border-color:var(--accent); box-shadow:0 0 0 3px rgba(212,50,106,0.15); }
.blank-input.correct { border-color:var(--success); background:var(--success-bg); color:var(--success); font-weight:600; }
.blank-input.wrong { border-color:var(--danger); background:var(--danger-bg); animation:shake 0.4s ease; }
.hint-text { font-size:0.78rem; color:var(--text-dim); font-style:italic; margin-bottom:0.5rem; }
.blank-hint-feedback { display:none; margin-top:0.5rem; padding:0.5rem 0.8rem; background:var(--accent-glow); border:1px solid var(--accent-dim); border-radius:4px; font-size:0.82rem; color:var(--accent); }
.blank-hint-feedback.visible { display:block; }
.btn { display:inline-flex; align-items:center; gap:0.4rem; padding:0.5rem 1rem; border:1px solid var(--border); background:var(--bg-card); font-size:0.8rem; font-weight:500; cursor:pointer; transition:all 0.2s ease-out; color:var(--text); min-height:44px; border-radius:4px; }
.btn:hover { border-color:var(--accent); color:var(--accent); }
.btn-listen { background:var(--accent); color:#fff; border-color:var(--accent); }
.btn-listen:hover { background:var(--accent-light); border-color:var(--accent-light); color:#fff; }
.btn-record { background:var(--danger); color:#fff; border-color:var(--danger); }
.btn-record:hover { background:#b91c1c; border-color:#b91c1c; color:#fff; }
.btn-stop { background:#f59e0b; color:#fff; border-color:#f59e0b; display:none; }
.btn-stop.visible { display:inline-flex; }
.btn-record.recording { animation:pulse 1.2s infinite; }
.btn-record.hidden { display:none; }
.check-btn, .listen-blank-btn { margin-right:0.5rem; }

.audio-btn { display:inline-flex; align-items:center; gap:0.3rem; background:var(--accent); color:#fff; border:none; padding:0.4rem 0.8rem; font-size:0.75rem; cursor:pointer; border-radius:4px; font-weight:500; transition:all 0.2s ease; min-height:36px; min-width:36px; justify-content:center; }
.audio-btn:hover { background:var(--accent-light); }

.quiz-item { background:var(--bg-card); border:1px solid var(--border); padding:1rem; margin-bottom:0.8rem; border-radius:6px; }
.quiz-question { font-size:0.95rem; font-weight:600; color:var(--text); margin-bottom:0.8rem; }
.quiz-options { display:grid; gap:0.5rem; }
.quiz-option { padding:0.8rem 1rem; border:1px solid var(--border); background:var(--bg-elevated); cursor:pointer; transition:all 0.2s ease; border-radius:4px; font-size:0.88rem; display:flex; align-items:center; gap:0.7rem; min-height:44px; }
.quiz-option:hover { border-color:var(--accent); }
.quiz-option .option-letter { width:26px; height:26px; background:var(--accent-dim); color:var(--accent); border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:700; font-size:0.78rem; flex-shrink:0; }
.quiz-option.correct { border-color:var(--success); background:var(--success-bg); color:var(--success); }
.quiz-option.correct .option-letter { background:var(--success); color:#fff; }
.quiz-option.wrong { border-color:var(--danger); background:var(--danger-bg); animation:shake 0.4s ease; }

.order-container { display:grid; gap:0.5rem; }
.order-item { display:flex; align-items:center; gap:0.8rem; background:var(--bg-card); border:1px solid var(--border); padding:0.8rem 1rem; border-radius:6px; cursor:pointer; transition:all 0.2s ease; }
.order-item:hover { border-color:var(--accent); }
.order-item.dragging { opacity:0.5; }
.order-item.drag-over { border-color:var(--accent); background:var(--accent-glow); }
.order-num { font-weight:700; color:var(--accent); min-width:28px; height:28px; display:flex; align-items:center; justify-content:center; background:var(--accent-dim); border-radius:50%; flex-shrink:0; }
.order-text { flex:1; font-size:0.88rem; color:var(--text); }
.order-arrows { display:flex; gap:0.2rem; flex-shrink:0; }
.arrow-btn { background:var(--bg-elevated); border:1px solid var(--border); padding:0.3rem 0.6rem; cursor:pointer; border-radius:4px; font-size:0.7rem; min-height:36px; min-width:36px; }
.arrow-btn:hover { background:var(--accent-dim); border-color:var(--accent); }
.order-item.correct-order { border-color:var(--success); background:var(--success-bg); pointer-events:none; }
.order-item.correct-order .order-num { background:var(--success); color:#fff; }
.order-item.wrong { border-color:var(--danger); background:var(--danger-bg); animation:shake 0.4s ease; }

.speech-card { background:var(--bg-input); border:1px solid var(--border); padding:1.2rem; margin-bottom:0.6rem; transition:all 0.2s ease; border-radius:4px; }
.speech-phrase { font-family:'Cormorant Garamond',serif; font-size:1.25rem; font-weight:600; color:var(--white); margin-bottom:0.2rem; }
.speech-translation { font-size:0.875rem; color:var(--text-dim); margin-bottom:1rem; font-style:italic; }
.speech-controls { display:flex; gap:0.5rem; align-items:center; flex-wrap:wrap; }
.speech-result { margin-top:0.8rem; padding:1rem; border:1px solid var(--border); font-size:0.875rem; display:none; border-radius:4px; }
.speech-result.show { display:block; animation:fadeIn 0.3s ease; }
.speech-result.good { background:var(--success-bg); border-color:var(--success-border); color:var(--success); }
.speech-result.try-again { background:var(--warn-bg); border-color:var(--warn-border); color:var(--warn); }
.speech-result.bad { background:var(--danger-bg); border-color:var(--danger-border); color:var(--danger); }
.word-comparison { margin-top:0.8rem; }
.word-comparison .comp-label { font-size:0.72rem; font-weight:600; text-transform:uppercase; letter-spacing:1.5px; margin-bottom:0.4rem; opacity:0.8; }
.comp-words { display:flex; flex-wrap:wrap; gap:0.3rem; margin-bottom:0.6rem; }
.word-box { display:inline-flex; align-items:center; gap:0.2rem; padding:0.3rem 0.6rem; border-radius:3px; font-size:0.78rem; font-weight:500; }
.word-correct { background:var(--success-bg); color:var(--success); }
.word-missing, .word-wrong { background:var(--danger-bg); color:var(--danger); }
.word-extra { background:var(--warn-bg); color:var(--warn); }
.speech-suggestion { margin-top:0.6rem; padding-top:0.6rem; border-top:1px solid var(--border); font-size:0.82rem; }

.think-card { background:var(--bg-card); border:1px solid var(--border); padding:1.2rem; border-radius:6px; }

.survival-card { background:linear-gradient(135deg,var(--accent) 0%,var(--accent-light) 100%); color:#fff; padding:1.5rem; border-radius:8px; margin-top:1.5rem; box-shadow:0 4px 12px rgba(212,50,106,0.25); }
.survival-card h4 { font-family:'Cormorant Garamond',serif; font-size:1.1rem; font-weight:700; margin-bottom:1rem; color:#fff; }
.survival-phrase { display:flex; align-items:center; gap:0.7rem; padding:0.6rem 0; border-bottom:1px solid rgba(255,255,255,0.2); font-size:0.88rem; flex-wrap:wrap; }
.survival-phrase:last-child { border-bottom:none; }
.sp-num { background:rgba(255,255,255,0.25); width:26px; height:26px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:700; font-size:0.78rem; flex-shrink:0; }
.sp-en { font-weight:600; color:#fff; flex:1; min-width:200px; }
.sp-pt { color:rgba(255,255,255,0.85); font-size:0.82rem; flex:1; min-width:160px; }
.survival-card .btn-listen { background:rgba(255,255,255,0.2); color:#fff; border:1px solid rgba(255,255,255,0.4); padding:0.3rem 0.7rem; font-size:0.72rem; min-height:32px; }
.survival-card .btn-listen:hover { background:rgba(255,255,255,0.35); border-color:#fff; }

.welcome-card { background:linear-gradient(135deg,var(--accent-glow) 0%,var(--bg-card) 100%); border:1px solid var(--border); padding:2rem; border-radius:8px; margin-bottom:2rem; }
.welcome-card h3 { font-family:'Cormorant Garamond',serif; font-size:1.6rem; color:var(--accent); margin-bottom:0.5rem; }
.welcome-card p { font-size:0.92rem; color:var(--text-mid); }
.welcome-card blockquote { font-family:'Cormorant Garamond',serif; font-size:1.1rem; font-style:italic; color:var(--text); border-left:3px solid var(--accent); padding-left:1rem; margin:1rem 0; }
.emergency-phrases { text-align:left; margin:1.5rem 0; }
.emergency-phrases h4 { font-family:'Cormorant Garamond',serif; font-size:1.05rem; font-weight:600; color:var(--white); margin-bottom:0.8rem; }

.callback-box { background:var(--accent-dim); border:1px solid rgba(212,50,106,0.15); padding:1.5rem; border-radius:6px; margin-bottom:1.5rem; }
.callback-box h4 { font-family:'Cormorant Garamond',serif; font-size:1rem; font-weight:600; color:var(--accent); margin-bottom:0.8rem; }

.info-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(200px,1fr)); gap:1rem; margin-bottom:2rem; }
.info-item { background:var(--bg-card); border:1px solid var(--border); padding:1rem 1.2rem; border-radius:4px; }
.info-item .info-label { font-size:0.72rem; font-weight:700; letter-spacing:2px; text-transform:uppercase; color:var(--accent); margin-bottom:0.3rem; }
.info-item .info-value { font-size:0.88rem; font-weight:500; color:var(--white); }

.journey-box { background:var(--accent-dim); border:1px solid rgba(212,50,106,0.2); padding:2rem; border-radius:6px; margin-bottom:2rem; position:relative; }
.journey-box h4 { font-family:'Cormorant Garamond',serif; font-size:1.2rem; font-weight:700; color:var(--accent); margin-bottom:1rem; }
.journey-from, .journey-to { font-size:0.88rem; color:var(--text-mid); margin-bottom:0.5rem; padding-left:2.5rem; position:relative; line-height:1.5; }
.journey-from::before { content:'DE'; position:absolute; left:0; top:0; font-size:0.6rem; font-weight:700; color:var(--danger); letter-spacing:1px; }
.journey-to::before { content:'PARA'; position:absolute; left:0; top:0; font-size:0.6rem; font-weight:700; color:var(--success); letter-spacing:1px; }
.journey-arrow { display:flex; align-items:center; justify-content:center; margin:0.8rem 0; color:var(--accent); font-size:1.2rem; }

.promise-box { background:var(--bg-card); border:2px solid var(--accent); padding:1.5rem 2rem; border-radius:6px; margin-bottom:2rem; text-align:center; }
.promise-box p { font-family:'Cormorant Garamond',serif; font-size:1.15rem; font-weight:600; color:var(--accent); line-height:1.6; }

.sw-grid { display:grid; grid-template-columns:1fr 1fr; gap:1.5rem; margin-bottom:2rem; }
.sw-col h4 { font-family:'Cormorant Garamond',serif; font-size:1rem; font-weight:600; margin-bottom:0.8rem; padding-bottom:0.4rem; border-bottom:1px solid var(--border); }
.sw-col.strengths h4 { color:var(--success); }
.sw-col.weaknesses h4 { color:var(--danger); }
.sw-col ul { list-style:none; }
.sw-col li { padding:0.4rem 0; font-size:0.875rem; color:var(--text-mid); padding-left:1.2rem; position:relative; }
.sw-col.strengths li::before { content:'+'; position:absolute; left:0; color:var(--success); font-weight:700; }
.sw-col.weaknesses li::before { content:'-'; position:absolute; left:0; color:var(--danger); font-weight:700; }
@media (max-width:600px) { .sw-grid { grid-template-columns:1fr; } }

.curriculum-table { width:100%; border-collapse:collapse; margin-bottom:2rem; font-size:0.875rem; }
.curriculum-table thead th { padding:0.8rem 1rem; text-align:left; font-weight:600; font-size:0.72rem; letter-spacing:2px; text-transform:uppercase; color:var(--accent); background:var(--accent-dim); border-bottom:1px solid var(--border); }
.curriculum-table td { padding:0.8rem 1rem; border-bottom:1px solid var(--border); vertical-align:top; color:var(--text-mid); }
.curriculum-table .aula-cell { font-weight:700; color:var(--accent); white-space:nowrap; }

.method-card { background:var(--bg-card); border:1px solid var(--border); padding:1.5rem; border-radius:6px; margin-bottom:1rem; }
.method-card h5 { font-size:0.85rem; font-weight:600; color:var(--accent); margin-bottom:0.3rem; }
.method-card p { font-size:0.875rem; color:var(--text-dim); }

.personality-card { background:var(--bg-elevated); border:1px solid var(--border); padding:1.5rem; border-radius:6px; margin-bottom:2rem; }
.personality-card h4 { font-family:'Cormorant Garamond',serif; font-size:1.1rem; font-weight:600; color:var(--white); margin-bottom:1rem; padding-bottom:0.5rem; border-bottom:1px solid var(--border); }
.personality-item { margin-bottom:0.8rem; }
.personality-item .p-label { font-size:0.72rem; font-weight:700; letter-spacing:2px; text-transform:uppercase; color:var(--accent); }
.personality-item .p-value { font-size:0.85rem; color:var(--text-mid); margin-top:0.2rem; }

.plan-table { width:100%; border-collapse:collapse; margin-bottom:1rem; font-size:0.875rem; }
.plan-table thead th { padding:0.8rem 1rem; text-align:left; font-weight:600; font-size:0.72rem; letter-spacing:2px; text-transform:uppercase; color:var(--accent); background:var(--accent-dim); border-bottom:1px solid var(--border); }
.plan-table td { padding:0.8rem 1rem; border-bottom:1px solid var(--border); vertical-align:top; color:var(--text-mid); }
.plan-table .time-cell { font-weight:600; color:var(--accent); white-space:nowrap; width:70px; }
.plan-table .activity-cell { font-weight:600; color:var(--white); }

.teacher-lesson { background:var(--bg-card); border:1px solid var(--border); overflow:hidden; margin-bottom:1.5rem; box-shadow:0 1px 3px rgba(0,0,0,0.06); border-radius:6px; }
.teacher-hero { height:280px; display:flex; flex-direction:column; justify-content:flex-end; padding:2rem; position:relative; background-size:cover; background-position:center; }
.teacher-hero::before { content:''; position:absolute; inset:0; background:linear-gradient(to top,rgba(26,26,46,0.92) 0%,rgba(26,26,46,0.5) 50%,rgba(26,26,46,0.25) 100%); }
.teacher-hero * { position:relative; z-index:1; }
.teacher-hero h3 { font-family:'Cormorant Garamond',serif; font-size:2rem; font-weight:700; color:#fff; line-height:1.2; }
.teacher-hero .hero-sub { font-size:0.8rem; color:#ccc; margin-top:0.3rem; letter-spacing:0.5px; }
.teacher-body { padding:2rem 2.5rem; }
@media (max-width:768px) { .teacher-body { padding:1.5rem 1rem; } .teacher-hero h3 { font-size:1.4rem; } }
.teacher-section { margin-bottom:2rem; }
.teacher-section h4 { font-family:'Cormorant Garamond',serif; font-size:1.1rem; font-weight:600; margin-bottom:1rem; display:flex; align-items:center; gap:0.6rem; padding-bottom:0.6rem; border-bottom:1px solid var(--border); color:var(--white); flex-wrap:wrap; }
.phase-tag { font-family:'Inter',sans-serif; font-size:0.7rem; padding:0.3rem 0.7rem; font-weight:700; letter-spacing:1.2px; text-transform:uppercase; border-radius:3px; }
.phase-warm { background:rgba(180,130,20,0.1); color:#92610a; border:1px solid rgba(180,130,20,0.3); }
.phase-vocab { background:rgba(30,80,200,0.08); color:#1e50c8; border:1px solid rgba(30,80,200,0.25); }
.phase-teach { background:rgba(120,40,200,0.08); color:#6b21a8; border:1px solid rgba(120,40,200,0.25); }
.phase-practice { background:rgba(20,130,60,0.08); color:#15803d; border:1px solid rgba(20,130,60,0.25); }
.phase-production { background:rgba(212,50,106,0.1); color:#b91c5c; border:1px solid rgba(212,50,106,0.3); }
.phase-wrap { background:rgba(200,40,60,0.08); color:#b91c1c; border:1px solid rgba(200,40,60,0.25); }

.vocab-table { width:100%; border-collapse:collapse; margin-bottom:0.8rem; }
.vocab-table th { padding:0.6rem 1rem; background:var(--bg-elevated); text-align:left; font-size:0.72rem; font-weight:600; text-transform:uppercase; letter-spacing:1.5px; color:var(--text-dim); border-bottom:1px solid var(--border); }
.vocab-table td { padding:0.6rem 1rem; border-bottom:1px solid var(--border); font-size:0.875rem; color:var(--text-mid); }
.vocab-table .word-cell { font-weight:600; color:var(--white); }

.teacher-tip { background:var(--accent-glow); border:1px solid rgba(212,50,106,0.15); padding:1rem 1.2rem; margin:1rem 0; font-size:0.875rem; color:var(--text-mid); border-radius:4px; line-height:1.7; }
.teacher-tip strong { color:var(--accent); }
.obstacle-alert { background:var(--danger-bg); border:1px solid var(--danger-border); padding:1rem 1.2rem; margin:1rem 0; font-size:0.875rem; color:var(--text-mid); border-radius:4px; line-height:1.7; }
.obstacle-alert strong { color:var(--danger); }

.dialogue-container { background:var(--bg-input); border:1px solid var(--border); padding:1.2rem; border-radius:4px; }
.dialogue-line { display:flex; gap:0.8rem; margin-bottom:1rem; align-items:flex-start; }
.dialogue-line:last-child { margin-bottom:0; }
.dialogue-avatar { width:36px; height:36px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:0.6rem; flex-shrink:0; font-weight:700; letter-spacing:0.5px; }
.avatar-staff { background:rgba(59,130,246,0.15); color:#60a5fa; border:1px solid rgba(59,130,246,0.3); }
.avatar-you { background:var(--accent-dim); color:var(--accent); border:1px solid rgba(212,50,106,0.3); }
.dialogue-bubble { background:rgba(255,255,255,0.6); border:1px solid var(--border); padding:0.8rem 1rem; font-size:0.85rem; flex:1; border-radius:4px; line-height:1.6; }
.dialogue-bubble.your-turn { background:var(--accent-glow); border:1px solid rgba(212,50,106,0.2); }
.dialogue-bubble .speaker { font-size:0.7rem; font-weight:600; text-transform:uppercase; letter-spacing:1.5px; margin-bottom:0.3rem; color:var(--text-dim); }

.homework-box { background:var(--accent-glow); border:1px solid rgba(212,50,106,0.15); padding:1.2rem; margin-top:1rem; border-radius:4px; }
.homework-box h4 { font-family:'Cormorant Garamond',serif; font-size:1rem; font-weight:600; color:var(--accent); margin-bottom:0.6rem; }
.homework-box ul { list-style:none; }
.homework-box li { padding:0.35rem 0; font-size:0.875rem; color:var(--text-mid); padding-left:1.2rem; position:relative; }
.homework-box li::before { content:''; position:absolute; left:0; top:0.7rem; width:6px; height:6px; border:1px solid var(--accent); }

.checklist { list-style:none; }
.checklist li { padding:0.4rem 0; font-size:0.875rem; color:var(--text); display:flex; align-items:flex-start; gap:0.6rem; line-height:1.5; }
.checklist input[type="checkbox"] { width:18px; height:18px; accent-color:var(--accent); cursor:pointer; flex-shrink:0; margin-top:2px; }
.checklist li.checked { color:var(--text-dim); text-decoration:line-through; }

.media-grid { display:grid; gap:0.6rem; }
.media-card { background:var(--bg-input); border:1px solid var(--border); display:flex; gap:1rem; align-items:stretch; overflow:hidden; transition:all 0.2s ease; border-radius:4px; }
.media-card:hover { border-color:var(--border-light); transform:translateY(-1px); }
.media-thumb { width:80px; min-height:80px; background-size:cover; background-position:center; flex-shrink:0; position:relative; }
.media-thumb::after { content:''; position:absolute; inset:0; background:rgba(0,0,0,0.3); }
.media-thumb.movie { background-image:url('https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=200&q=80'); }
.media-thumb.series { background-image:url('https://images.unsplash.com/photo-1522869635100-9f4c5e86aa37?w=200&q=80'); }
.media-thumb.podcast { background-image:url('https://images.unsplash.com/photo-1590602847861-f357a9332bbc?w=200&q=80'); }
.media-thumb.youtube { background-image:url('https://images.unsplash.com/photo-1611162616475-46b635cb6868?w=200&q=80'); }
.media-thumb.app { background-image:url('https://images.unsplash.com/photo-1611078489935-0cb964de46d6?w=200&q=80'); }
.media-info { padding:0.8rem; flex:1; }
.media-info h5 { font-size:0.88rem; font-weight:600; color:var(--white); margin-bottom:0.1rem; }
.media-info .media-type { font-size:0.7rem; font-weight:700; text-transform:uppercase; letter-spacing:1.5px; color:var(--accent); }
.media-info p { font-size:0.82rem; color:var(--text-dim); margin-top:0.2rem; }
.media-info .media-tip { font-size:0.8rem; color:var(--accent); font-weight:500; margin-top:0.3rem; }
.media-card-wrapper { display:flex; align-items:stretch; gap:0; }
.media-check { display:flex; align-items:center; justify-content:center; padding:0 0.8rem; background:var(--bg-elevated); border:1px solid var(--border); border-right:none; border-radius:4px 0 0 4px; cursor:pointer; }
.media-check input[type="checkbox"] { width:20px; height:20px; accent-color:var(--accent); cursor:pointer; }
.media-card-wrapper .media-card { border-radius:0 4px 4px 0; flex:1; }
.media-card-wrapper.done .media-card { opacity:0.6; }

.reset-btn { background:transparent; border:1px solid var(--border); color:var(--text-dim); padding:0.6rem 1.2rem; cursor:pointer; border-radius:4px; font-size:0.8rem; margin-top:1rem; }
.reset-btn:hover { border-color:var(--danger); color:var(--danger); }

.speed-btn { padding:4px 10px; font-size:0.75rem; border:1px solid var(--border); background:var(--bg-card); border-radius:4px; cursor:pointer; min-height:32px; }
.speed-btn.active { background:var(--accent); color:#fff; border-color:var(--accent); font-weight:600; }
`;

function getHeadHTML(title) {
  return `<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow">
<title>${esc(title)}</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Cormorant+Garamond:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
${cssVars}
${cssMain}
</style>
</head>`;
}

// JS comum (audio, exercises, state) — recebe slug e nLessons
function getCommonJS(slug, nLessons) {
  return `
let audioSpeed = 1;
let currentAudio = null;

function setAudioSpeed(s, btn) {
  audioSpeed = s;
  document.querySelectorAll('.speed-btn').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  if (currentAudio) currentAudio.playbackRate = s;
}

function switchTab(tabId) {
  document.querySelectorAll('.tab-content').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.getElementById('tab-' + tabId).classList.add('active');
  event.currentTarget.classList.add('active');
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function toggleLesson(header) { header.parentElement.classList.toggle('open'); }

function speakText(text, btn) {
  if (currentAudio) { currentAudio.pause(); currentAudio.currentTime = 0; }
  const cleanText = text.replace(/\\\\'/g, "'");
  const file = audioMap[cleanText] || audioMap[cleanText.replace(/\\.$/, '')] || audioMap[cleanText + '.'];
  if (file) {
    currentAudio = new Audio(file);
    currentAudio.playbackRate = audioSpeed;
    currentAudio.play().catch(() => fallbackSpeak(cleanText));
  } else { fallbackSpeak(cleanText); }
}

function fallbackSpeak(text) {
  if ("speechSynthesis" in window) {
    window.speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(text);
    u.lang = "en-US"; u.rate = audioSpeed * 0.9; u.pitch = 1;
    window.speechSynthesis.speak(u);
  }
}

function speakPhrase(btn) {
  const card = btn.closest('.speech-card');
  if (card) speakText(card.dataset.phrase, btn);
}

let activeRecognition = null;
function startRecording(btn) {
  const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SR) { alert('Use Google Chrome para reconhecimento de voz.'); return; }
  const card = btn.closest('.speech-card');
  const target = card.dataset.phrase.toLowerCase().replace(/[^a-z0-9'\\s]/g, '');
  const resultDiv = card.querySelector('.speech-result');
  const stopBtn = card.querySelector('.btn-stop');
  if (btn.classList.contains('recording')) return;
  btn.classList.add('recording', 'hidden');
  stopBtn.classList.add('visible');
  const r = new SR();
  r.lang = 'en-US'; r.interimResults = false; r.maxAlternatives = 3; r.continuous = true;
  activeRecognition = { recognition: r, btn: btn, stopBtn: stopBtn, card: card };
  r.start();
  function resetButtons() { btn.classList.remove('recording', 'hidden'); stopBtn.classList.remove('visible'); activeRecognition = null; }
  r.onresult = function(event) {
    const best = event.results[event.results.length - 1][0].transcript.toLowerCase().replace(/[^a-z0-9'\\s]/g, '');
    const analysis = analyzeWords(target, best);
    const totalWords = analysis.expected.length;
    const correctWords = analysis.expected.filter(w => w.status === 'correct').length;
    resultDiv.classList.add('show'); resultDiv.classList.remove('good', 'try-again', 'bad');
    let html = '';
    if (analysis.score >= 0.8) { resultDiv.classList.add('good'); html += '<strong>Score: ' + correctWords + '/' + totalWords + '</strong> — Excelente!'; updateProgress(); }
    else if (analysis.score >= 0.5) { resultDiv.classList.add('try-again'); html += '<strong>Score: ' + correctWords + '/' + totalWords + '</strong> — Quase lá!'; }
    else { resultDiv.classList.add('bad'); html += '<strong>Score: ' + correctWords + '/' + totalWords + '</strong> — Continue praticando!'; }
    html += '<div class="word-comparison"><div class="comp-label">Palavra a palavra:</div><div class="comp-words">';
    analysis.expected.forEach(w => { html += '<span class="word-box word-' + (w.status === 'correct' ? 'correct' : 'missing') + '"><span class="word-icon">' + (w.status === 'correct' ? '\\u2713' : '\\u2717') + '</span> ' + w.word + '</span>'; });
    html += '</div><div class="comp-label">Você disse:</div><div class="comp-words">';
    analysis.spoken.forEach(w => {
      const cls = w.status === 'correct' ? 'correct' : w.status === 'extra' ? 'extra' : 'wrong';
      const icon = w.status === 'correct' ? '\\u2713' : w.status === 'extra' ? '~' : '\\u2717';
      html += '<span class="word-box word-' + cls + '"><span class="word-icon">' + icon + '</span> ' + w.word + '</span>';
    });
    html += '</div></div>';
    resultDiv.innerHTML = html;
    resetButtons();
  };
  r.onerror = function() { resetButtons(); resultDiv.classList.add('show', 'try-again'); resultDiv.innerHTML = 'Não consegui ouvir. Verifique seu microfone.'; };
  r.onend = function() { resetButtons(); };
  setTimeout(() => { if (btn.classList.contains('recording')) { r.stop(); resetButtons(); } }, 30000);
}
function stopRecording(stopBtn) { if (activeRecognition) activeRecognition.recognition.stop(); }

function analyzeWords(targetStr, spokenStr) {
  const tw = targetStr.split(/\\s+/).filter(w => w), sw = spokenStr.split(/\\s+/).filter(w => w);
  const m = tw.length, n = sw.length, dp = Array.from({ length: m + 1 }, () => Array(n + 1).fill(0));
  for (let i = 1; i <= m; i++) for (let j = 1; j <= n; j++) dp[i][j] = wordsMatch(tw[i-1], sw[j-1]) ? dp[i-1][j-1] + 1 : Math.max(dp[i-1][j], dp[i][j-1]);
  const mt = new Set(), ms = new Set(); let i = m, j = n;
  while (i > 0 && j > 0) { if (wordsMatch(tw[i-1], sw[j-1])) { mt.add(i-1); ms.add(j-1); i--; j--; } else if (dp[i-1][j] > dp[i][j-1]) i--; else j--; }
  const expected = tw.map((w, i) => ({ word: w, status: mt.has(i) ? 'correct' : 'missing' }));
  const spoken = sw.map((w, i) => ({ word: w, status: ms.has(i) ? 'correct' : 'wrong' }));
  return { expected, spoken, score: mt.size / Math.max(m, 1) };
}
function wordsMatch(a, b) { if (a === b) return true; const ca = a.replace(/'/g, ''), cb = b.replace(/'/g, ''); if (ca === cb) return true; if (a.length > 3 && b.length > 3 && levenshtein(a, b) <= 1) return true; return false; }
function levenshtein(a, b) { const m = []; for (let i = 0; i <= b.length; i++) m[i] = [i]; for (let j = 0; j <= a.length; j++) m[0][j] = j; for (let i = 1; i <= b.length; i++) for (let j = 1; j <= a.length; j++) m[i][j] = b[i-1] === a[j-1] ? m[i-1][j-1] : Math.min(m[i-1][j-1] + 1, m[i][j-1] + 1, m[i-1][j] + 1); return m[b.length][a.length]; }

function checkBlank(btn) {
  const item = btn.closest('.fill-blank-item'), input = item.querySelector('.blank-input');
  input.classList.remove('correct', 'wrong');
  const answer = input.dataset.answer.toLowerCase().trim();
  const value = input.value.toLowerCase().trim();
  let hintEl = item.querySelector('.blank-hint-feedback');
  if (hintEl) hintEl.classList.remove('visible');
  if (value === answer) { input.classList.add('correct'); updateProgress(); }
  else {
    input.classList.add('wrong');
    if (input.dataset.hint) {
      if (!hintEl) { hintEl = document.createElement('div'); hintEl.className = 'blank-hint-feedback'; item.appendChild(hintEl); }
      hintEl.textContent = input.dataset.hint;
      hintEl.classList.add('visible');
    }
    setTimeout(() => input.classList.remove('wrong'), 1500);
  }
}
function listenBlank(btn) {
  const item = btn.closest('.fill-blank-item'), input = item.querySelector('.blank-input');
  if (input.dataset.phrase) speakText(input.dataset.phrase, btn);
}

function selectQuiz(o) {
  const p = o.closest('.quiz-options'); if (p.querySelector('.correct')) return;
  if (o.dataset.correct === 'true') { o.classList.add('correct'); updateProgress(); }
  else { o.classList.add('wrong'); setTimeout(() => o.classList.remove('wrong'), 800); }
}

let orderSelection = {};
function selectOrderItem(item, containerId) {
  if (item.classList.contains('correct-order')) return;
  if (!orderSelection[containerId]) orderSelection[containerId] = [];
  const idx = orderSelection[containerId].indexOf(item);
  if (idx > -1) { orderSelection[containerId].splice(idx, 1); item.querySelector('.order-num').textContent = '?'; item.style.borderColor = ''; }
  else { orderSelection[containerId].push(item); item.querySelector('.order-num').textContent = orderSelection[containerId].length; item.style.borderColor = 'var(--accent)'; }
}
function checkOrder(containerId) {
  const container = document.getElementById(containerId);
  const items = container.querySelectorAll('.order-item');
  const selected = orderSelection[containerId] || [];
  if (selected.length !== items.length) { alert('Selecione todos os itens na ordem.'); return; }
  let allCorrect = true;
  selected.forEach((item, idx) => {
    if (parseInt(item.dataset.order) === idx + 1) { item.classList.add('correct-order'); item.querySelector('.order-num').textContent = idx + 1; }
    else { allCorrect = false; item.style.borderColor = 'var(--danger)'; item.classList.add('wrong'); setTimeout(() => { item.classList.remove('wrong'); item.style.borderColor = ''; item.querySelector('.order-num').textContent = '?'; }, 1000); }
  });
  if (!allCorrect) orderSelection[containerId] = [];
  else updateProgress();
}
function moveItem(btn, direction, containerId) {
  const item = btn.closest('.order-item');
  const container = document.getElementById(containerId);
  const items = Array.from(container.querySelectorAll('.order-item'));
  const idx = items.indexOf(item);
  if (direction === -1 && idx > 0) container.insertBefore(item, items[idx - 1]);
  else if (direction === 1 && idx < items.length - 1) container.insertBefore(items[idx + 1], item);
}

function listenAllVocab(btn) {
  const section = btn.closest('.exercise-section') || btn.closest('.teacher-section');
  const audioBtns = section.querySelectorAll('.vocab-card .audio-btn, .vocab-table .audio-btn');
  let i = 0;
  function playNext() { if (i < audioBtns.length) { audioBtns[i].click(); i++; setTimeout(playNext, 2500); } }
  playNext();
}

function verifyAllMatches(gridId) {
  const grid = document.getElementById(gridId);
  const rows = grid.querySelectorAll('.match-row');
  rows.forEach(row => {
    const select = row.querySelector('select');
    const answer = row.dataset.answer;
    row.classList.remove('correct', 'wrong');
    if (select.value === answer) { row.classList.add('correct'); }
    else if (select.value !== '') { row.classList.add('wrong'); setTimeout(() => row.classList.remove('wrong'), 1800); }
  });
  updateProgress();
}
function checkMatch(select) {
  const row = select.closest('.match-row');
  const answer = row.dataset.answer;
  row.classList.remove('correct', 'wrong');
  if (select.value === answer) { row.classList.add('correct'); select.disabled = true; updateProgress(); }
  else if (select.value !== '') { row.classList.add('wrong'); setTimeout(() => { row.classList.remove('wrong'); select.value = ''; }, 1000); }
}

function toggleMediaDone(checkbox) {
  const wrapper = checkbox.closest('.media-card-wrapper');
  wrapper.classList.toggle('done', checkbox.checked);
  saveState();
}

function toggleChecklist(cb) {
  const li = cb.closest('li');
  if (cb.checked) li.classList.add('checked'); else li.classList.remove('checked');
  updateProgress();
}

function updateProgress() {
  const totalLessons = ${nLessons};
  let completedLessons = 0;
  for (let l = 1; l <= totalLessons; l++) {
    const cl = document.getElementById('checklist-' + l);
    if (!cl) continue;
    const allChecks = cl.querySelectorAll('input[type="checkbox"]');
    const checkedChecks = cl.querySelectorAll('input[type="checkbox"]:checked');
    const lessonPct = allChecks.length > 0 ? Math.round(checkedChecks.length / allChecks.length * 100) : 0;
    const bar = document.querySelector('[data-lesson-progress="' + l + '"]');
    const lbl = document.querySelector('[data-lesson-pct="' + l + '"]');
    if (bar) bar.style.width = lessonPct + '%';
    if (lbl) lbl.textContent = lessonPct + '%';
    var stampEl = document.getElementById('stamp' + l);
    if (stampEl) { if (lessonPct === 100) stampEl.classList.add('earned'); else stampEl.classList.remove('earned'); }
    if (allChecks.length > 0 && checkedChecks.length === allChecks.length) completedLessons++;
  }
  const overallPct = Math.round(completedLessons / totalLessons * 100);
  const pb = document.getElementById('progressBar');
  const pp = document.getElementById('progressPercent');
  if (pb) pb.style.width = overallPct + '%';
  if (pp) pp.textContent = overallPct + '%';
  saveState();
}

function saveState() {
  const s = { blanks: [], quiz: [], speech: [], checklists: {}, mediaChecks: {}, matches: [] };
  document.querySelectorAll('.media-card-wrapper').forEach(w => { const id = w.dataset.media; const cb = w.querySelector('input[type="checkbox"]'); if (id && cb) s.mediaChecks[id] = cb.checked; });
  document.querySelectorAll('.match-row.correct select').forEach(sel => { s.matches.push(sel.closest('.match-row').querySelector('.match-word').textContent + '|' + sel.value); });
  document.querySelectorAll('.blank-input.correct').forEach(e => s.blanks.push(e.dataset.answer));
  document.querySelectorAll('.quiz-option.correct').forEach(e => s.quiz.push(e.textContent.trim().substring(0, 30)));
  document.querySelectorAll('.checklist input[type="checkbox"]').forEach((cb, i) => { s.checklists[i] = cb.checked; });
  try { localStorage.setItem('${slug}-progress', JSON.stringify(s)); } catch(e) {}
}
function loadState() {
  const r = localStorage.getItem('${slug}-progress'); if (!r) return;
  try {
    const s = JSON.parse(r);
    if (s.matches) s.matches.forEach(d => { const [word, val] = d.split('|'); document.querySelectorAll('.match-row').forEach(row => { if (row.querySelector('.match-word').textContent === word) { const sel = row.querySelector('select'); if (sel) { sel.value = val; row.classList.add('correct'); sel.disabled = true; } } }); });
    if (s.blanks) s.blanks.forEach(a => { document.querySelectorAll('.blank-input[data-answer="' + a + '"]').forEach(e => { e.value = a; e.classList.add('correct'); }); });
    if (s.checklists) document.querySelectorAll('.checklist input[type="checkbox"]').forEach((cb, i) => { if (s.checklists[i]) { cb.checked = true; cb.closest('li').classList.add('checked'); } });
    if (s.mediaChecks) document.querySelectorAll('.media-card-wrapper').forEach(w => { const id = w.dataset.media; const cb = w.querySelector('input[type="checkbox"]'); if (id && cb && s.mediaChecks[id]) { cb.checked = true; w.classList.add('done'); } });
    updateProgress();
  } catch(e) {}
}
function resetProgress() { if (confirm('Tem certeza que deseja resetar todo o progresso?')) { localStorage.removeItem('${slug}-progress'); location.reload(); } }
loadState();
`;
}

module.exports = { esc, escAttr, escForJS, getHeadHTML, getCommonJS, cssVars, cssMain };
