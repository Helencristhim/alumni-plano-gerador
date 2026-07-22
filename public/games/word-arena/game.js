// ===== Word Arena — arcade de vocabulário de inglês =====
// Motor reaproveitado do "Tabuada do Dino" (repo interno better-learn):
// mesma mecânica quiz+mascote+áudio, re-tematizada para vocabulário.
// Regra Alumni (A2+): 100% inglês na tela — a palavra vem em EN, a
// definição vem em EN, e o TTS pronuncia a palavra em en-US.
(() => {
  "use strict";

  // ---------- Baralhos (decks) — palavra + definição em inglês simples ----------
  // Temas casados com o perfil do aluno teen (games, esportes, dia a dia).
  const DECKS = [
    {
      id: "gaming", name: "Gaming", emoji: "🎮",
      words: [
        { w: "level", def: "a stage in a game" },
        { w: "score", def: "the points you have" },
        { w: "win", def: "to finish in first place" },
        { w: "player", def: "a person who plays" },
        { w: "team", def: "a group that plays together" },
        { w: "pause", def: "to stop for a moment" },
        { w: "restart", def: "to start again" },
        { w: "skill", def: "something you are good at" },
      ],
    },
    {
      id: "football", name: "Football", emoji: "⚽",
      words: [
        { w: "goal", def: "when the ball goes in the net" },
        { w: "match", def: "a game between two teams" },
        { w: "coach", def: "the person who trains the team" },
        { w: "fan", def: "a person who loves a team" },
        { w: "pass", def: "to give the ball to a teammate" },
        { w: "field", def: "the place where you play" },
        { w: "win", def: "to beat the other team" },
        { w: "practice", def: "to do something to get better" },
      ],
    },
    {
      id: "everyday", name: "Everyday", emoji: "💬",
      words: [
        { w: "friend", def: "a person you like and trust" },
        { w: "school", def: "the place where you study" },
        { w: "phone", def: "you use it to call and text" },
        { w: "music", def: "sounds you listen to and enjoy" },
        { w: "weekend", def: "Saturday and Sunday" },
        { w: "homework", def: "school work you do at home" },
        { w: "hungry", def: "when you want to eat" },
        { w: "tired", def: "when you want to sleep" },
      ],
    },
  ];

  const QUESTIONS_PER_ROUND = 8;

  // ---------- Elementos ----------
  const hudDeck = document.getElementById("hud-deck");
  const hudScore = document.getElementById("hud-score");
  const hudStreak = document.getElementById("hud-streak");
  const hudProgress = document.getElementById("hud-progress");
  const muteBtn = document.getElementById("mute-btn");
  const backBtn = document.getElementById("back-btn");
  const mascotEl = document.getElementById("mascot");
  const wordEl = document.getElementById("word");
  const sayBtn = document.getElementById("say-btn");
  const answersEl = document.getElementById("answers");
  const overlayStart = document.getElementById("overlay-start");
  const overlayResult = document.getElementById("overlay-result");
  const deckGrid = document.getElementById("deck-grid");
  const resultMascot = document.getElementById("result-mascot");
  const resultTitle = document.getElementById("result-title");
  const resultStars = document.getElementById("result-stars");
  const resultText = document.getElementById("result-text");
  const againBtn = document.getElementById("again-btn");
  const menuBtn = document.getElementById("menu-btn");

  // ---------- Estado ----------
  let deck = null;      // baralho escolhido (null = misturado)
  let questions = [];   // [{w, def}]
  let allWords = [];     // pool de defs para distratores
  let qIndex = 0;
  let score = 0;
  let streak = 0;
  let correctCount = 0;
  let busy = false;
  let muted = false;

  const PRAISE = ["Nice!", "Awesome!", "You got it!", "Great job!", "Perfect!"];
  const ENCOURAGE = ["Almost!", "Try the next one!", "Keep going!", "You can do it!"];

  DECKS.forEach((d) => d.words.forEach((x) => allWords.push(x)));

  // ---------- Áudio (Web Audio API) — SFX ----------
  let audioCtx = null;
  function initAudio() {
    if (!audioCtx) {
      try { audioCtx = new (window.AudioContext || window.webkitAudioContext)(); }
      catch (e) { audioCtx = null; }
    }
    if (audioCtx && audioCtx.state === "suspended") audioCtx.resume();
  }
  function tone(freq, start, dur, type = "sine", vol = 0.25) {
    if (!audioCtx || muted) return;
    const t0 = audioCtx.currentTime + start;
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.type = type;
    osc.frequency.setValueAtTime(freq, t0);
    gain.gain.setValueAtTime(0.0001, t0);
    gain.gain.exponentialRampToValueAtTime(vol, t0 + 0.02);
    gain.gain.exponentialRampToValueAtTime(0.0001, t0 + dur);
    osc.connect(gain).connect(audioCtx.destination);
    osc.start(t0);
    osc.stop(t0 + dur + 0.02);
  }
  const sfx = {
    click() { tone(420, 0, 0.08, "square", 0.18); },
    correct() {
      tone(523.25, 0, 0.12, "triangle", 0.3);
      tone(659.25, 0.1, 0.12, "triangle", 0.3);
      tone(783.99, 0.2, 0.2, "triangle", 0.3);
    },
    wrong() {
      tone(220, 0, 0.18, "sawtooth", 0.22);
      tone(160, 0.12, 0.25, "sawtooth", 0.22);
    },
    win() {
      const notes = [523.25, 587.33, 659.25, 783.99, 1046.5];
      notes.forEach((f, i) => tone(f, i * 0.14, 0.2, "triangle", 0.3));
    },
  };

  // ---------- Voz (inglês, en-US) ----------
  let enVoice = null;
  function pickVoice() {
    if (!("speechSynthesis" in window)) return;
    const voices = speechSynthesis.getVoices();
    enVoice = voices.find((v) => /en[-_]US/i.test(v.lang)) ||
              voices.find((v) => /^en/i.test(v.lang)) || null;
  }
  if ("speechSynthesis" in window) {
    pickVoice();
    speechSynthesis.onvoiceschanged = pickVoice;
  }
  function speak(text, rate = 1.0) {
    if (muted || !("speechSynthesis" in window)) return;
    speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(text);
    u.lang = "en-US";
    u.rate = rate;
    u.pitch = 1.05;
    if (enVoice) u.voice = enVoice;
    speechSynthesis.speak(u);
  }

  // ---------- Tela inicial: escolher o deck ----------
  function buildDeckGrid() {
    deckGrid.innerHTML = "";
    DECKS.forEach((d) => {
      const b = document.createElement("button");
      b.className = "deck-btn";
      b.innerHTML = `<span class="deck-emoji">${d.emoji}</span>${d.name}`;
      b.addEventListener("click", () => { initAudio(); sfx.click(); startRound(d); });
      deckGrid.appendChild(b);
    });
    const mix = document.createElement("button");
    mix.className = "deck-btn mix";
    mix.innerHTML = `<span class="deck-emoji">🎲</span>Mixed`;
    mix.addEventListener("click", () => { initAudio(); sfx.click(); startRound(null); });
    deckGrid.appendChild(mix);
  }

  // ---------- Geração das perguntas ----------
  function buildQuestions(d) {
    const pool = d ? d.words.slice() : allWords.slice();
    shuffle(pool);
    return pool.slice(0, Math.min(QUESTIONS_PER_ROUND, pool.length));
  }

  function buildOptions(correct) {
    const opts = new Set([correct.def]);
    const pool = shuffle((deck ? deck.words : allWords).slice());
    for (const x of pool) {
      if (opts.size >= 4) break;
      if (x.def !== correct.def) opts.add(x.def);
    }
    return shuffle([...opts]);
  }

  // ---------- Fluxo ----------
  function startRound(d) {
    deck = d;
    questions = buildQuestions(d);
    qIndex = 0; score = 0; streak = 0; correctCount = 0; busy = false;
    hudDeck.textContent = d ? d.emoji + " " + d.name : "🎲 Mixed";
    overlayStart.classList.add("hidden");
    overlayResult.classList.add("hidden");
    updateHud();
    showQuestion();
  }

  function showQuestion() {
    const q = questions[qIndex];
    busy = false;
    mascotEl.className = "mascot";
    mascotEl.textContent = "🦊";
    wordEl.textContent = q.w;
    hudProgress.textContent = `${qIndex + 1}/${questions.length}`;

    const options = buildOptions(q);
    answersEl.innerHTML = "";
    options.forEach((def) => {
      const btn = document.createElement("button");
      btn.className = "opt";
      btn.innerHTML = `<span>${def}</span>`;
      btn.addEventListener("click", () => choose(btn, def, q.def));
      answersEl.appendChild(btn);
    });

    speak(q.w, 0.95); // pronuncia a palavra em inglês
  }

  function choose(btn, def, answer) {
    if (busy) return;
    busy = true;
    initAudio();
    const opts = [...answersEl.children];
    opts.forEach((e) => e.classList.add("disabled"));

    if (def === answer) {
      btn.classList.add("correct");
      score += 10 + streak * 2;
      streak++; correctCount++;
      mascotEl.className = "mascot happy";
      sfx.correct();
      speak(rand(PRAISE));
    } else {
      btn.classList.add("wrong");
      opts.forEach((e) => {
        if (e.querySelector("span").textContent === answer) e.classList.add("correct");
      });
      streak = 0;
      mascotEl.className = "mascot sad";
      mascotEl.textContent = "😅";
      sfx.wrong();
      speak(rand(ENCOURAGE));
    }
    updateHud();

    setTimeout(() => {
      qIndex++;
      if (qIndex >= questions.length) finishRound();
      else showQuestion();
    }, def === answer ? 1000 : 1700);
  }

  function finishRound() {
    const n = questions.length;
    const stars = correctCount >= n - 1 ? 3 : correctCount >= Math.ceil(n * 0.6) ? 2 : correctCount >= Math.ceil(n * 0.3) ? 1 : 0;
    resultStars.textContent = "★".repeat(stars) + "☆".repeat(3 - stars);
    resultText.textContent = `You got ${correctCount} of ${n}!`;

    let title, mascot, voice;
    if (correctCount >= n - 1) { title = "Amazing!"; mascot = "🏆"; voice = "Amazing! You are a vocabulary master!"; }
    else if (correctCount >= Math.ceil(n * 0.6)) { title = "Well done!"; mascot = "🦊"; voice = "Well done! Keep practicing!"; }
    else { title = "Keep practicing!"; mascot = "💪"; voice = "Keep practicing, you can do it!"; }
    resultTitle.textContent = title;
    resultMascot.textContent = mascot;

    overlayResult.classList.remove("hidden");
    sfx.win();
    speak(voice);
  }

  function updateHud() {
    hudScore.textContent = score;
    hudStreak.textContent = "🔥" + streak;
  }

  function showMenu() {
    if ("speechSynthesis" in window) speechSynthesis.cancel();
    overlayResult.classList.add("hidden");
    overlayStart.classList.remove("hidden");
  }

  // ---------- Utilidades ----------
  function rnd(min, max) { return Math.floor(Math.random() * (max - min + 1)) + min; }
  function rand(arr) { return arr[rnd(0, arr.length - 1)]; }
  function shuffle(arr) {
    for (let i = arr.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
  }

  // ---------- Botões ----------
  muteBtn.addEventListener("click", () => {
    muted = !muted;
    muteBtn.textContent = muted ? "🔇" : "🔊";
    if (muted && "speechSynthesis" in window) speechSynthesis.cancel();
  });
  backBtn.addEventListener("click", () => { sfx.click(); showMenu(); });
  sayBtn.addEventListener("click", () => { initAudio(); if (questions[qIndex]) speak(questions[qIndex].w, 0.9); });
  againBtn.addEventListener("click", () => { initAudio(); sfx.click(); startRound(deck); });
  menuBtn.addEventListener("click", () => { sfx.click(); showMenu(); });

  buildDeckGrid();
})();
