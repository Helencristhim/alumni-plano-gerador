(function(){
/* ==========================================================================
   DANTE -- AULA 03 -- THE ROBOT FACTORY (Kids A2) -- PERCURSO POST-CLASS

   MOTOR copiado do percurso da aula 01 ("The Helper Quest", do artefato
   "Dante Blecker Gregory · Kids A2 · Professor View") -- byte a byte, incluindo
   as tres correcoes que ele ja carrega. Desta aula sao APENAS o bloco CONTEUDO
   e os textos da tela final.
   ========================================================================== */

/* ====================================================================
   AUDIO
   AUDIO_MAP: chave = a frase exata falada, valor = caminho do mp3.
   Enquanto estiver vazio, tudo cai em TTS -- mesma degradacao da aula.
   Gravar os arquivos e preencher aqui ativa o audio sem tocar no resto.
   ==================================================================== */
var AUDIO_MAP = {};

/* TUDO que este percurso pode FALAR. O builder le esta lista, gera nome/voz de
   cada MP3, alimenta o audio_manifest.json (gen_audio) e PREENCHE o AUDIO_MAP
   acima. Frase fora daqui cai em TTS -- que a REGRA 7 so admite como emergencia.

   APOSTROFO RETO, sempre: o speak() faz text.replace(/’/g, "'") ANTES do
   lookup, entao chave com apostrofo curvo nunca casa (medido no navegador).

   So a opcao CERTA de cada tela de cena entra: o renderScene fala o rotulo
   apenas no ramo do acerto -- o material nao modela erro em audio.            */
var AUDIO_PHRASES = [
  "He checks the machines, then he carries the boxes to the truck.",
  "But today his left arm doesn't move.",
  "battery",
  "machine",
  "lift",
  "The robot lifts a car with one arm.",
  "Bolt carries the boxes to the truck.",
  "Bolt checks the machines every night.",
  "I carry my school bag every day.",
  "It is six in the morning. The night shift is over. Bolt goes to the charging room. Nina arrives, and every morning she checks the battery and writes the report. The engineer only comes at four.",
  "she checks the battery",
  "Tomorrow Dante tells his class about the factory. Bolt works every night, from ten to six.",
  "He works every night.",
  "Bolt checks every night.",
  "Bolt carries every night.",
  "Bolt lifts every night.",
  "Bolt fixes every night."
];
var current = null;

/* Parar TTS no Chrome nao e' so cancel(): um sintetizador PAUSADO ignora o
   cancel e volta a falar quando alguem o retoma. Por isso resume() vem antes.
   Sem isto, som de uma tela reaparecia na seguinte. */
function ttsClear(){
  if (!('speechSynthesis' in window)) return;
  try { window.speechSynthesis.resume(); } catch(e){}
  try { window.speechSynthesis.cancel(); } catch(e){}
}
function speak(text, btn){
  var clean = String(text).replace(/’/g, "'");
  if (current){ current.pause(); current.currentTime = 0; current = null; }
  ttsClear();
  var file = AUDIO_MAP[clean];
  if (file){
    current = new Audio(file);
    current.play().catch(function(){ tts(clean); });
  } else {
    tts(clean);
  }
  if (btn){
    var old = btn.innerHTML;
    btn.innerHTML = '&#128266; Playing...';
    setTimeout(function(){ btn.innerHTML = old; }, 1400);
  }
}
function tts(text){
  if (!('speechSynthesis' in window)) return;
  var u = new SpeechSynthesisUtterance(text);
  u.lang = 'en-US'; u.rate = .8; u.pitch = 1.05;
  window.speechSynthesis.speak(u);
}
function imgFallback(img){
  var s = document.createElement('span');
  s.className = 'imgph';
  s.innerHTML = img.getAttribute('data-emoji') || '&#10067;';
  s.title = 'missing asset: ' + img.getAttribute('src');
  img.replaceWith(s);
}
/* CORRIGIDO: o onerror chamava imgFallback, que e LOCAL desta IIFE -- handler
   inline so enxerga global (REGRA 7.1). Defeito latente no artefato porque
   nenhum PAIRS usava pic(). */
window.pcImg = imgFallback;
/* Imagem com degradacao para emoji. A arte entra depois, sem mexer no codigo. */
function pic(slug, emoji, size){
  return '<img src="/assets/kids/' + slug + '.png" alt="' + slug + '" width="' + (size||64) +
         '" data-emoji="' + emoji + '" onerror="pcImg(this)" style="max-width:100%;height:auto">';
}

/* ====================================================================
   CONTEUDO
   Tudo abaixo sai da versao FINAL de dante-blecker-gregory-aula3.html (The
   Robot Factory, Kids A2). Nenhum item introduz palavra, estrutura ou
   personagem que nao tenha sido trabalhado na aula -- e nenhum repete
   literalmente um exercicio dela.
   ==================================================================== */
/* PESOS -- somam 100 exatos, e cada um dentro da sua faixa normativa.
   Conferido por SOMA, nao por leitura: e a segunda das cinco armadilhas
   registradas do modelo ("peso por item != numero de itens").

     Supported Recall  20   |  Power Words 20 (10+10)  |  Language Move 30
     New Mission       15   |  Final Challenge 15      |  total 100        */
var STAGES = [
  { id:'story',   name:'Story',    icon:'&#128270;', weight:20 },
  { id:'words1',  name:'Words',    icon:'&#11088;',  weight:10 },
  { id:'words2',  name:'Verbs',    icon:'&#128172;', weight:10 },
  { id:'sayit',   name:'Say It',   icon:'&#128483;', weight:30 },
  { id:'mission', name:'New',      icon:'&#128506;&#65039;', weight:15 },
  { id:'final',   name:'Report',   icon:'&#127937;', weight:15 }
];

/* --- RECAP: o contexto da aula, de volta na tela ---------------------
   O aluno nao pode rever o in-class. "Memoria apoiada" (secao 5 do framework):
   todo detalhe exigido na resposta e reapresentado aqui. A ORDEM das tarefas do
   Bolt esta na tira porque o item 1 cobra o que vem primeiro; o braco parado
   esta porque o item 2 pergunta por que o engenheiro vem as quatro. */
function recapHTML(){
  return '<h3>&#128218; The story so far</h3>' +
    '<div class="who">' +
      '<span>&#129302; Bolt &mdash; the night shift, ten to six</span>' +
      '<span>&#128105; Nina &mdash; she checks the battery</span>' +
      '<span>&#128736;&#65039; the engineer &mdash; he comes at four</span>' +
    '</div>' +
    '<p class="story">Every night Bolt <b>checks the machines first</b>, and then he ' +
    '<b>carries the boxes</b> to the truck. He lifts two hundred kilos with one arm.<br>' +
    'But today <b>his left arm doesn&rsquo;t move</b>.</p>';
}

/* --- 2. Story Spot: listen and choose --------------------------------
   O audio e a fala da aula, sem dizer quem fala. O aluno cruza o que ouve com
   a tira -- nao com a memoria da aula. As perguntas sao sobre BOLT e o
   ENGENHEIRO, nunca sobre o proprio Dante (REGRA 27F). */
var STORY_ITEMS = [
  {
    audio: 'He checks the machines, then he carries the boxes to the truck.',
    q: 'What does Bolt do FIRST?',
    opts: [
      { key:'check', em:'&#128269;', lbl:'he checks the machines' },
      { key:'carry', em:'&#128230;', lbl:'he carries the boxes' },
      { key:'fix',   em:'&#128295;', lbl:'he fixes his arm' }
    ],
    answer: 'check',
    ok:  'Yes! First he checks the machines. Then he carries the boxes.',
    tip: 'Listen again. Which one comes first — check or carry? &#128269;',
    exp: 'He checks the machines first, and then he carries the boxes.'
  },
  {
    audio: "But today his left arm doesn't move.",
    q: 'Why does the engineer come at four?',
    opts: [
      { key:'arm',     em:'&#128736;&#65039;', lbl:'to fix the arm' },
      { key:'battery', em:'&#128267;', lbl:'to check the battery' },
      { key:'boxes',   em:'&#128230;', lbl:'to carry the boxes' }
    ],
    answer: 'arm',
    ok:  'Yes! The arm is the problem, so the engineer fixes it.',
    tip: 'Look at the panel. What is wrong with Bolt today? &#129302;',
    exp: 'His left arm doesn’t move — the engineer comes to fix it.'
  }
];

/* --- 3. Power Words A: match palavra <-> imagem ----------------------
   Tres das oito palavras da aula: as CONCRETAS, que a biblioteca kids tem
   (public/assets/kids). shift e heavy ficam de fora -- turno e peso nao se
   desenham sem ambiguidade (ver [[kids-image-library]]); eles voltam no
   gap-fill e na New Mission. */
var PAIRS = [
  { key:'battery', word:'battery', em:pic('battery', '&#128267;') },
  { key:'machine', word:'machine', em:pic('machine', '&#9881;&#65039;') },
  { key:'lift',    word:'lift',    em:pic('lift', '&#127947;') }
];

/* --- 4. Power Words B: gap-fill, banco PARCIAL -----------------------
   Regra A2 (secao 6 do modelo): "reducao parcial do banco" -- 3 candidatas
   para 2 lacunas, um distrator apenas. O que se cobra aqui e a FORMA da
   terceira pessoa (-s), que e a gramatica da aula: as tres candidatas ja
   vem com o -s, entao a escolha e de VERBO, e o -s entra pelo olho.

   ok  = acerto.  exp = resposta revelada apos o segundo erro.               */
var BANK = ['lifts', 'carries', 'fixes'];
var GAPS = [
  { before:'The robot ', after:' a car with one arm.', answer:'lifts', em:'&#127947;',
    ok:'Yes! The robot lifts a car with one arm.',
    exp:'The answer is: The robot lifts a car with one arm. &#127947;',
    tip:'To move something UP, with strength. &#11014;&#65039;' },
  { before:'Bolt ', after:' the boxes to the truck.', answer:'carries', em:'&#128230;',
    ok:'Yes! Bolt carries the boxes to the truck.',
    exp:'The answer is: Bolt carries the boxes to the truck. &#128230;',
    tip:'From the factory TO the truck. And remember: carry &#8594; carries. &#128666;' }
];

/* --- 5. Language Move: sentence builder -- o chunk-alvo ---------------
   O chunk da aula e a 3a pessoa com -s. NENHUMA das duas frases e a que a aula
   ja montou no Practice ("Bolt carries the heavy boxes." / "Nina checks the
   battery." / "I fix my robot." / "The machine lifts a car."): o modelo pede
   "repeticao transformada", nao copia.

   A primeira e 3a pessoa (com -s); a segunda e PRIMEIRA pessoa (sem -s), que e
   exatamente o contraste da aula e a ponte para o Final Challenge.           */
var BUILDS = [
  { target:['Bolt','checks','the machines','every night.'],
    shown: ['every night.','checks','Bolt','the machines'], em:'&#129302;',
    say:'Bolt checks the machines every night.' },
  { target:['I','carry','my school bag','every day.'],
    shown: ['my school bag','every day.','I','carry'], em:'&#127890;',
    say:'I carry my school bag every day.' }
];

/* ==========================================================================
   A CENA DA FABRICA -- serve a New Mission e o Final Challenge
   Uma funcao, dois usos: o cenario nao muda entre as duas telas, so a
   consequencia. A crianca ve o MESMO quadro e nao reconstroi nada de cabeca.

   A esteira e desenhada (uma barra longa com dois suportes), nao e emoji:
   precisa ser o CHAO da fabrica, onde as caixas estao. Rotulo nomeia OBJETO
   (the machine, the boxes, bolt, nina) -- nunca relacao.
   ========================================================================== */
function factoryScene(){
  return '<div class="scene">' +
    '<div class="sc-bar" style="left:0%;top:88%;width:100%;height:12%"></div>' +

    '<div class="sc-bar sc-trunk" style="left:20%;top:52%;width:60%;height:6%"></div>' +
    '<div class="sc-bar sc-trunk" style="left:24%;top:58%;width:3%;height:30%"></div>' +
    '<div class="sc-bar sc-trunk" style="left:73%;top:58%;width:3%;height:30%"></div>' +

    '<div class="sc-obj" style="left:32%;top:40%;font-size:2.4rem">&#9881;&#65039;</div>' +
    '<div class="sc-tag" style="left:32%;top:30%">the machine</div>' +

    '<div class="sc-obj" style="left:58%;top:41%;font-size:2.2rem">&#128230;</div>' +
    '<div class="sc-tag" style="left:58%;top:31%">the boxes</div>' +

    '<div class="sc-obj" style="left:14%;top:76%;font-size:2.3rem">&#129302;</div>' +
    '<div class="sc-tag" style="left:14%;top:93%">bolt</div>' +
    '<div class="sc-obj" style="left:88%;top:77%;font-size:2rem">&#128105;</div>' +
    '<div class="sc-tag" style="left:88%;top:93%">nina</div>' +
  '</div>';
}

/* --- 6. NEW MISSION: problema NOVO com linguagem CONHECIDA ----------------
   O limite da exigencia de "contexto novo" (secao 7):

     contexto novo + linguagem conhecida   <- e isto
     contexto novo + CAMPO LEXICAL novo    <- nao e isto

   A cena e o TURNO SEGUINTE, que a aula nao mostrou: sao seis da manha, o Bolt
   sai e a Nina chega. Personagens e verbos sao os da aula 03 -- check, carry,
   lift, fix, battery, machine, shift. O aluno aplica o criterio (quem faz o
   que, com -s) a um momento que nunca viu.

   QUEM FAZ O QUE ESTA DITO NO TEXTO, tres vezes, uma por alternativa: nada e
   deduzido de tamanho, aparencia ou papel.                                   */
var MISSION = {
  sceneHTML: factoryScene(),
  scene: 'It is six in the morning. The night shift is over. Bolt goes to the charging room. Nina arrives, and every morning she checks the battery and writes the report. The engineer only comes at four.',
  em: '&#127749;&#128105;',
  q: 'What does Nina do every morning?',
  opts: [
    { key:'nina',  em:'&#128267;', lbl:'she checks the battery' },
    { key:'bolt',  em:'&#128230;', lbl:'she carries the boxes' },
    { key:'engin', em:'&#128736;&#65039;', lbl:'she fixes the arm' }
  ],
  answer:'nina',
  ok:  'Yes! Every morning Nina checks the battery and writes the report.',
  tip: 'Read it again: what does NINA do — and what does the engineer do? &#128105;',
  exp: 'Nina checks the battery every morning. The engineer is the one who fixes the arm.'
};

/* --- 7. FINAL CHALLENGE: resolver a missao COM o chunk --------------------
   MESMA cena. O que se avalia e o chunk-alvo (3a pessoa com -s), nao
   linguagem lateral: as tres alternativas dizem A MESMA COISA, e so uma esta
   na forma certa. Por isso a errada NUNCA e falada -- o renderScene so
   pronuncia o rotulo no ramo do acerto.

   ESTA TELA E AUTOSSUFICIENTE: repete que o Bolt trabalha toda noite, em vez
   de remeter a tela anterior.                                                */
var FINAL = {
  sceneHTML: factoryScene(),
  scene: 'Tomorrow Dante tells his class about the factory. Bolt works every night, from ten to six.',
  em: '&#127979;&#128172;',
  q: 'What does Dante say about Bolt?',
  opts: [
    { key:'a', lbl:'"He works every night."' },
    { key:'b', lbl:'"He work every night."' },
    { key:'c', lbl:'"He working every night."' }
  ],
  answer:'a',
  ok:  'Great! He + verb + S. Mission complete!',
  tip: 'He, she, it — what does the verb need at the end? &#128073; S',
  exp: 'Dante says: “He works every night.” — he, she and it always take the S.'
};

/* ====================================================================
   ESTADO
   score  = acerto de PRIMEIRA tentativa, ponderado pelo peso do estagio.
            Serve para a faixa de resultado e para a revisao seletiva.
   stars  = uma estrela por item concluido. NUNCA e retirada -- o modelo
            proibe perder ponto por erro.
   ==================================================================== */
var st = {
  screen:0, avatar:'', stars:0, score:0, missed:[], doneStage:{}
};
var SCREENS = ['s-start','s-story','s-words1','s-words2','s-sayit','s-mission','s-final','s-result'];

function award(itemWeight, firstTry, reviewText){
  st.stars++;
  if (firstTry) st.score += itemWeight;
  else if (reviewText) st.missed.push(reviewText);
  document.getElementById('starCount').innerHTML = '&#11088; ' + st.stars;
}

/* ---------- mapa de progresso ---------- */
function drawMap(){
  var h = '';
  STAGES.forEach(function(s, i){
    if (i) h += '<div class="link' + (st.doneStage[STAGES[i-1].id] ? ' done' : '') + '"></div>';
    var cls = st.doneStage[s.id] ? 'done' : (st.screen === i+1 ? 'now' : '');
    h += '<div class="spot ' + cls + '">' +
           (st.screen === i+1 ? '<span class="walker">' + st.avatar + '</span>' : '') +
           '<div class="dot">' + (st.doneStage[s.id] ? '&#9989;' : s.icon) + '</div>' +
           '<div class="nm">' + s.name + '</div>' +
         '</div>';
  });
  document.getElementById('map').innerHTML = h;
}

function go(n){
  st.screen = n;
  SCREENS.forEach(function(id, i){
    document.getElementById(id).hidden = (i !== n);
  });
  drawMap();
  /* peso POR ITEM: Story Replay vale 20%, em 2 itens = 10 cada.
     O ultimo argumento liga a tira de recap -- sem ela estes dois itens
     dependeriam de memoria desassistida. */
  /* peso POR ITEM: Supported Recall vale 20, em 2 itens = 10 cada.
     O ultimo argumento liga a tira de recap -- sem ela estes dois itens
     dependeriam de memoria desassistida, que a secao 7 proibe. */
  if (n === 1) renderChoice('s-story', 'Story Spot', '&#128270;', 'Supported Recall',
                            'Listen and choose the right answer.',
                            STORY_ITEMS, 'story', 10, true);
  if (n === 2) renderMatch();
  if (n === 3) renderGaps();
  if (n === 4) renderBuild();
  if (n === 5) renderScene('s-mission', 'New Mission', '&#128506;&#65039;', 'New Mission',
                           MISSION, 'mission', 15, 'Next stop &#10132;', 6);
  if (n === 6) renderScene('s-final', 'The report', '&#127937;', 'Final Challenge',
                           FINAL, 'final', 15, 'See my result &#127942;', 7);
  if (n === 7) renderResult();
  window.scrollTo(0, 0);
}

function fb(el, kind, msg){
  el.className = 'fb show ' + kind;
  el.innerHTML = msg;
}

/* ====================================================================
   MOTOR 1 -- escolha sequencial com audio (Story Spot e Final Move)
   Um item por vez: "uma acao central por tela" (modelo, principios).
   ==================================================================== */
function renderChoice(elId, title, icon, eyebrow, instr, items, stageId, weightEach, comRecap){
  var host = document.getElementById(elId);
  var idx = 0, tries = 0;

  function paint(){
    var it = items[idx];
    host.innerHTML =
      '<div class="eyebrow">' + eyebrow + '</div>' +
      '<h2>' + icon + ' ' + title + '</h2>' +
      '<p class="instr">' + instr + '</p>' +
      /* o contexto fica VISIVEL durante as perguntas, nao so antes delas */
      (comRecap ? '<div class="recap">' + recapHTML() + '</div>' : '') +
      (items.length > 1 ? '<div class="counter">Question ' + (idx+1) + ' of ' + items.length + '</div>' : '') +
      '<div class="actions" style="margin:0 0 16px">' +
        '<button class="audio-btn big" id="ab">&#128266; Listen</button>' +
      '</div>' +
      '<p class="q">' + it.q + '</p>' +
      '<div class="opts" id="op"></div>' +
      '<div class="fb" id="fbx"></div>' +
      '<div class="actions"><button class="btn" id="nx" hidden>Next &#10132;</button></div>';

    document.getElementById('ab').onclick = function(){ speak(it.audio, this); };
    var op = document.getElementById('op');
    it.opts.forEach(function(o){
      var d = document.createElement('div');
      d.className = 'opt';
      d.innerHTML = '<span class="pic">' + o.em + '</span><span class="lbl">' + o.lbl + '</span>';
      d.onclick = function(){ choose(o, d); };
      op.appendChild(d);
    });
    setTimeout(function(){ speak(it.audio); }, 350);
  }

  function choose(o, node){
    var it = items[idx];
    var box = document.getElementById('fbx');
    if (o.key === it.answer){
      node.classList.add('ok');
      lock();
      fb(box, 'good', '&#9989; ' + it.ok);
      award(weightEach, tries === 0, tries === 0 ? null : it.exp);
      finishItem();
    } else {
      tries++;
      node.classList.add('no');
      if (tries === 1){
        fb(box, 'tip', '&#128161; ' + it.tip + ' <b>Try again!</b>');
        speak(it.audio);
      } else {
        /* segundo erro: mostrar a resposta + exemplo curto, e seguir */
        lock();
        var right = it.opts.filter(function(x){ return x.key === it.answer; })[0];
        [].forEach.call(document.querySelectorAll('#op .opt'), function(el){
          if (el.querySelector('.lbl').textContent === right.lbl) el.classList.add('ok');
        });
        fb(box, 'tip', '&#128172; ' + it.exp);
        award(weightEach, false, it.exp);
        finishItem();
      }
    }
  }
  function lock(){
    [].forEach.call(document.querySelectorAll('#op .opt'), function(el){ el.classList.add('lock'); });
  }
  function finishItem(){
    var nx = document.getElementById('nx');
    nx.hidden = false;
    nx.onclick = function(){
      idx++; tries = 0;
      if (idx < items.length){ paint(); window.scrollTo(0,0); }
      else { st.doneStage[stageId] = true; go(st.screen + 1); }
    };
    if (idx === items.length - 1) nx.innerHTML = 'Next stop &#10132;';
  }
  paint();
}

/* ====================================================================
   MOTOR 2 -- matching palavra <-> imagem (Word Stars)
   ==================================================================== */
function renderMatch(){
  var host = document.getElementById('s-words1');
  var picked = null, found = 0;
  /* Erro por par, para que o score reflita a primeira tentativa como nos outros motores. */
  var missed = {};
  var shuffled = PAIRS.slice().sort(function(){ return Math.random() - .5; });

  host.innerHTML =
    '<div class="eyebrow">Power Words</div>' +
    '<h2>&#11088; Word Stars</h2>' +
    '<p class="instr">Tap a word. Then tap its picture. Say the word out loud!</p>' +
    '<div class="match">' +
      '<div class="col"><h3>Words</h3><div id="cw"></div></div>' +
      '<div class="col"><h3>Pictures</h3><div id="cp"></div></div>' +
    '</div>' +
    '<div class="fb" id="fbm"></div>' +
    '<div class="actions"><button class="btn" id="nxm" hidden>Next stop &#10132;</button></div>';

  var cw = document.getElementById('cw'), cp = document.getElementById('cp');
  cw.style.display = cp.style.display = 'flex';
  cw.style.flexDirection = cp.style.flexDirection = 'column';
  cw.style.gap = cp.style.gap = '10px';

  PAIRS.forEach(function(p){
    var d = document.createElement('div');
    d.className = 'mi'; d.textContent = p.word; d.dataset.key = p.key;
    d.onclick = function(){
      if (picked) picked.classList.remove('sel');
      picked = d; d.classList.add('sel');
      speak(p.word);
    };
    cw.appendChild(d);
  });
  shuffled.forEach(function(p){
    var d = document.createElement('div');
    d.className = 'mi'; d.innerHTML = '<span class="pic">' + p.em + '</span>'; d.dataset.key = p.key;
    d.onclick = function(){
      var box = document.getElementById('fbm');
      if (!picked){ fb(box, 'tip', '&#128161; Tap a <b>word</b> first.'); return; }
      if (picked.dataset.key === p.key){
        picked.classList.remove('sel'); picked.classList.add('ok'); d.classList.add('ok');
        picked = null; found++;
        /* Word Stars vale 10, em 3 pares. 10/3 e nao 3 -- so assim a soma
           fecha 100 exatos. */
        award(10/3, !missed[p.key], missed[p.key] ? 'This is <b>' + p.word + '</b>. ' + p.em : null);
        fb(box, 'good', '&#11088; ' + p.word + '! One star.');
        speak(p.word);
        if (found === PAIRS.length){
          fb(box, 'good', '&#127881; All three words found!');
          st.doneStage.words1 = true;
          var b = document.getElementById('nxm');
          b.hidden = false; b.onclick = function(){ go(3); };
        }
      } else {
        missed[picked.dataset.key] = true;
        d.classList.add('shake');
        setTimeout(function(){ d.classList.remove('shake'); }, 320);
        fb(box, 'tip', '&#128161; Not this one. Look at the picture again. Which word matches it?');
      }
    };
    cp.appendChild(d);
  });
}

/* ====================================================================
   MOTOR 3 -- gap-fill com banco SEMPRE visivel (regra Kids A1)
   ==================================================================== */
function renderGaps(){
  var host = document.getElementById('s-words2');
  var idx = 0, tries = 0;

  host.innerHTML =
    '<div class="eyebrow">Power Words</div>' +
    '<h2>&#128172; Word Power</h2>' +
    '<p class="instr">Complete the sentence. Tap a word from the box.</p>' +
    '<div class="sents" id="ss"></div>' +
    '<div class="banklbl">Word box</div>' +
    '<div class="bank" id="bk"></div>' +
    '<div class="fb" id="fbg"></div>' +
    '<div class="actions"><button class="btn" id="nxg" hidden>Next stop &#10132;</button></div>';

  var ss = document.getElementById('ss');
  GAPS.forEach(function(g, i){
    var d = document.createElement('div');
    d.className = 'sent' + (i === 0 ? ' now' : '');
    d.id = 'sent' + i;
    d.innerHTML = g.em + ' ' + g.before + '<span class="blank" id="bl' + i + '">?</span>' + g.after;
    ss.appendChild(d);
  });

  /* O banco fica inteiro na tela o tempo todo -- nao some, nao encolhe. */
  var bk = document.getElementById('bk');
  BANK.forEach(function(w){
    var c = document.createElement('div');
    c.className = 'chip'; c.textContent = w;
    c.onclick = function(){ pickWord(w); };
    bk.appendChild(c);
  });

  function pickWord(w){
    if (idx >= GAPS.length) return;
    var g = GAPS[idx];
    var box = document.getElementById('fbg');
    var blank = document.getElementById('bl' + idx);
    var sent = document.getElementById('sent' + idx);
    if (w === g.answer){
      blank.textContent = w;
      sent.classList.remove('now'); sent.classList.add('ok');
      fb(box, 'good', '&#9989; ' + g.ok);
      /* CORRIGIDO: o artefato montava "A fish can swim ." -- espaco antes do
         ponto. A chave do AUDIO_MAP e a frase EXATA: com o espaco a mais ela
         nunca casaria com o MP3 e a frase cairia em TTS. */
      speak((g.before + w + g.after).replace(/\s+/g, ' ').trim());
      award(5, tries === 0, tries === 0 ? null : g.exp);
      idx++; tries = 0;
      if (idx < GAPS.length){
        document.getElementById('sent' + idx).classList.add('now');
      } else {
        st.doneStage.words2 = true;
        fb(box, 'good', '&#127881; All sentences complete!');
        var b = document.getElementById('nxg');
        b.hidden = false; b.onclick = function(){ go(4); };
      }
    } else {
      tries++;
      if (tries === 1){
        fb(box, 'tip', '&#128161; ' + g.tip + ' <b>Try again!</b>');
      } else {
        blank.textContent = g.answer;
        sent.classList.remove('now'); sent.classList.add('ok');
        fb(box, 'tip', '&#128172; ' + g.exp);
        award(5, false, g.exp);
        idx++; tries = 0;
        if (idx < GAPS.length){
          document.getElementById('sent' + idx).classList.add('now');
        } else {
          st.doneStage.words2 = true;
          var b2 = document.getElementById('nxg');
          b2.hidden = false; b2.onclick = function(){ go(4); };
        }
      }
    }
  }
}

/* ====================================================================
   MOTOR 4 -- sentence builder, "say it before you check"

   O QUE ESTE MOTOR AVALIA: a ORDEM dos blocos. Nada mais.

   A tela pede "say it out loud" e o botao Hear it oferece o modelo, mas nao
   ha gravacao nem qualquer confirmacao de que o aluno falou. Tecnicamente
   esta e uma atividade de RECONSTRUCAO com recomendacao oral -- nao uma
   atividade oral registrada, e nenhuma descricao deste material deve dizer
   que o sistema avaliou producao oral.

   Gravar exigiria getUserMedia + MediaRecorder, e dentro do iframe do
   Artifact o microfone depende de uma permissions-policy que nao esta sob
   nosso controle: o pedido apareceria e poderia falhar em silencio, num
   material que a crianca abre sozinha em casa. Fica registrado como decisao
   em aberto, nao como implementacao pendente.
   ==================================================================== */
function renderBuild(){
  var host = document.getElementById('s-sayit');
  var idx = 0, tries = 0, chosen = [];

  function paint(){
    var b = BUILDS[idx];
    chosen = [];
    host.innerHTML =
      '<div class="eyebrow">Language Move</div>' +
      '<h2>&#128483; Say It</h2>' +
      '<p class="instr">Put the words in order. Then say the sentence out loud!</p>' +
      '<div class="counter">Sentence ' + (idx+1) + ' of ' + BUILDS.length + '</div>' +
      '<div style="font-size:3.4rem;text-align:center;margin-bottom:8px">' + b.em + '</div>' +
      '<div class="line" id="ln"><span class="ph">Tap the words below...</span></div>' +
      '<div class="bank" id="bb"></div>' +
      '<div class="sayit">&#128483; Say it out loud, then tap Check.' +
        '<button class="audio-btn" id="mb" style="padding:7px 14px;font-size:.9rem">&#128266; Hear it</button></div>' +
      '<div class="fb" id="fbb"></div>' +
      '<div class="actions">' +
        '<button class="btn" id="ck" disabled>Check</button>' +
        '<button class="btn btn-ghost" id="cl">Clear</button>' +
        '<button class="btn" id="nxb" hidden>Next &#10132;</button>' +
      '</div>';

    var bb = document.getElementById('bb');
    b.shown.forEach(function(w, i){
      var c = document.createElement('div');
      c.className = 'blk'; c.textContent = w; c.dataset.i = i;
      c.onclick = function(){
        if (c.classList.contains('used')) return;
        c.classList.add('used'); chosen.push({ w:w, node:c });
        draw();
      };
      bb.appendChild(c);
    });
    document.getElementById('mb').onclick = function(){ speak(b.say, this); };
    document.getElementById('cl').onclick = reset;
    document.getElementById('ck').onclick = check;
    draw();
  }

  function draw(){
    var ln = document.getElementById('ln');
    if (!chosen.length){ ln.innerHTML = '<span class="ph">Tap the words below...</span>'; }
    else {
      ln.innerHTML = '';
      chosen.forEach(function(c, i){
        var d = document.createElement('div');
        d.className = 'blk'; d.textContent = c.w;
        d.onclick = function(){
          c.node.classList.remove('used');
          chosen.splice(i, 1); draw();
        };
        ln.appendChild(d);
      });
    }
    document.getElementById('ck').disabled = (chosen.length !== BUILDS[idx].target.length);
  }

  function reset(){
    chosen.forEach(function(c){ c.node.classList.remove('used'); });
    chosen = []; draw();
    document.getElementById('ln').classList.remove('ok');
  }

  function check(){
    var b = BUILDS[idx];
    var box = document.getElementById('fbb');
    var got = chosen.map(function(c){ return c.w; }).join(' ');
    var want = b.target.join(' ');
    if (got === want){
      document.getElementById('ln').classList.add('ok');
      document.getElementById('ck').disabled = true;
      fb(box, 'good', '&#9989; ' + want + ' &#127881;');
      speak(b.say);
      award(15, tries === 0, tries === 0 ? null : want);
      next();
    } else {
      tries++;
      if (tries === 1){
        /* erro no chunk: destacar so a parte fixa, sem entregar a frase */
        /* erro no chunk: destacar so a parte fixa -- o <b>but</b> no meio --
           sem entregar a frase. Regra do modelo, secao 9. */
        fb(box, 'tip', '&#128161; One thing you <b>can</b> do, then <b>but</b>, then one thing you <b>can’t</b>. &#128266; Listen and try again.');
        speak(b.say);
        reset();
      } else {
        fb(box, 'tip', '&#128172; The sentence is: <b>' + want + '</b>');
        speak(b.say);
        award(15, false, want);
        document.getElementById('ck').disabled = true;
        next();
      }
    }
  }

  function next(){
    var n = document.getElementById('nxb');
    n.hidden = false;
    if (idx === BUILDS.length - 1) n.innerHTML = 'Next stop &#10132;';
    n.onclick = function(){
      idx++; tries = 0;
      if (idx < BUILDS.length){ paint(); window.scrollTo(0,0); }
      else { st.doneStage.sayit = true; go(5); }
    };
  }
  paint();
}

/* ====================================================================
   MOTOR 5 -- cena com uma escolha (New Mission e Final Challenge)
   Generico porque as duas telas fazem a mesma coisa mecanicamente e coisas
   diferentes pedagogicamente: a 5 apresenta o cenario novo e pede que o
   aluno APLIQUE o criterio; a 6 pede que ele PRODUZA o chunk para resolver.
   ==================================================================== */
function renderScene(elId, title, icon, eyebrow, data, stageId, weight, nextLabel, nextScreen){
  var host = document.getElementById(elId);
  var tries = 0;
  /* Sem id nos elementos internos, e tudo por host.querySelector: DUAS telas
     usam este motor, e um id fixo apareceria duas vezes no documento. Quando
     isso aconteceu, getElementById devolvia o container da PRIMEIRA tela e a
     segunda ficava sem opcao nenhuma -- a ultima tela do quiz, muda. */
  host.innerHTML =
    '<div class="eyebrow">' + eyebrow + '</div>' +
    '<h2>' + icon + ' ' + title + '</h2>' +
    '<div style="font-size:3.4rem;text-align:center">' + data.em + '</div>' +
    '<p class="instr" style="text-align:center;font-size:1.1rem">' + data.scene + '</p>' +
    /* A CENA fica visivel DURANTE a pergunta e as alternativas: quem esta
       presente precisa ser visto enquanto se decide, nao antes. */
    (data.sceneHTML || '') +
    '<div class="actions" style="margin:0 0 16px">' +
      '<button class="audio-btn big js-say">&#128266; Listen</button>' +
    '</div>' +
    '<p class="q">' + data.q + '</p>' +
    '<div class="opts' + (data.opts[0].em ? '' : ' lines') + '" data-role="opts"></div>' +
    /* data-role, e nao classe: fb() reescreve o className inteiro do bloco de
       feedback, e uma classe marcadora seria apagada no primeiro uso. */
    '<div class="fb" data-role="fb"></div>' +
    '<div class="actions"><button class="btn" data-role="next" hidden>' + nextLabel + '</button></div>';

  host.querySelector('.js-say').onclick = function(){ speak(data.scene, this); };

  var fo = host.querySelector('[data-role="opts"]');
  data.opts.forEach(function(o){
    var d = document.createElement('div');
    d.className = 'opt';
    d.innerHTML = (o.em ? '<span class="pic">' + o.em + '</span>' : '') +
                  '<span class="lbl">' + o.lbl + '</span>';
    d.onclick = function(){
      var box = host.querySelector('[data-role="fb"]');
      if (o.key === data.answer){
        d.classList.add('ok'); lockF();
        fb(box, 'good', '&#9989; ' + data.ok);
        speak(o.lbl.replace(/[“”"]/g, ''));
        award(weight, tries === 0, tries === 0 ? null : data.exp);
        done();
      } else {
        tries++;
        d.classList.add('no');
        if (tries === 1){
          fb(box, 'tip', '&#128161; ' + data.tip + ' <b>Try again!</b>');
        } else {
          lockF();
          /* A certa sai do gabarito, nao de um texto escrito a mao: trocar o
             item quebraria a revelacao em silencio. */
          var right = data.opts.filter(function(x){ return x.key === data.answer; })[0];
          [].forEach.call(fo.querySelectorAll('.opt'), function(el){
            if (el.querySelector('.lbl').innerHTML === right.lbl) el.classList.add('ok');
          });
          fb(box, 'tip', '&#128172; ' + data.exp);
          award(weight, false, data.exp);
          done();
        }
      }
    };
    fo.appendChild(d);
  });
  function lockF(){
    [].forEach.call(fo.querySelectorAll('.opt'), function(el){ el.classList.add('lock'); });
  }
  function done(){
    st.doneStage[stageId] = true;
    var b = host.querySelector('[data-role="next"]');
    b.hidden = false; b.onclick = function(){ go(nextScreen); };
  }
}

/* ====================================================================
   TELA FINAL -- score, faixa, badge, revisao seletiva, bonus
   Chegar aqui JA conclui a missao: a pontuacao nunca bloqueia.
   ==================================================================== */
function renderResult(){
  var host = document.getElementById('s-result');
  var pct = Math.round(st.score);
  var band, msg;
  if (pct >= 90){ band = 'Mission mastered!'; msg = 'You know who can do what — and how to say it. Amazing work!'; }
  else if (pct >= 70){ band = 'Great progress!'; msg = 'Almost perfect! Look at the sentence below one more time.'; }
  else { band = 'Try one more round!'; msg = 'Good job finishing the quest. Play again to collect more stars!'; }

  var review = '';
  if (st.missed.length){
    review = '<div class="review"><h3>Look at this again</h3>' +
             st.missed.slice(0, 2).map(function(m){ return '<p>&#128073; ' + m + '</p>'; }).join('') +
             '</div>';
  }

  host.innerHTML =
    '<div class="eyebrow">Mission Complete</div>' +
    '<div style="text-align:center">' +
      '<div style="font-size:3.4rem">' + st.avatar + ' &#129302; &#9881;&#65039;</div>' +
      /* REGRA: esta mensagem serve QUALQUER faixa de pontuacao, e por isso fala
         so de CONCLUSAO. Celebrar ter concluido e verdade para quem errou e
         seguiu depois da revelacao; afirmar acerto que pode nao ter havido, nao.
         Nenhuma variante que afirme desempenho pode existir nesta tela -- nem em
         comentario, para nao reaparecer em busca de validacao.
         E a UNICA mensagem de conclusao abaixo dos emojis. */
      '<p class="instr" style="margin:0 0 6px">You completed the Night Shift Quest. <b>The factory is running!</b></p>' +
      '<div class="scorebig">' + pct + '%</div>' +
      '<div class="band">' + band + '</div>' +
      '<p class="instr" style="margin-bottom:6px">' + msg + '</p>' +
      '<div style="font-size:1.3rem;color:var(--star);font-weight:800">&#11088; ' + st.stars + ' stars</div>' +
      '<div class="badge"><span class="em">&#129302;</span> Badge unlocked: Night Shift Engineer</div>' +
    '</div>' +
    review +
    '<div class="bonus">' +
      '<span class="tag">Bonus &middot; not scored</span>' +
      '<p style="margin:0 0 10px;font-size:1.1rem;font-weight:700">Your turn! Choose one and say the whole sentence:</p>' +
      '<p style="margin:0 0 10px;font-size:1.3rem;font-weight:800;color:var(--accent)">Bolt ______ every night.</p>' +
      '<div class="bank" id="bonusBank"></div>' +
      '<div class="fb" id="fbz"></div>' +
    '</div>' +
    '<div class="actions" style="justify-content:center">' +
      /* CORRIGIDO: era onclick="restart()", e restart NAO e global (o arquivo
         inteiro e uma IIFE): o botao nao fazia nada. Chama o que esta exposto. */
      '<button class="btn btn-ghost" onclick="pcRestart3()">&#128260; Play again</button>' +
    '</div>';

  /* BONUS -- fora do percurso essencial e NAO pontuado (regra do modelo).
     O aluno escolhe uma acao e completa a frase sobre si mesmo: o chunk sai
     da historia e vai para a vida dele, que e o ponto da transferencia.   */
  var bz = document.getElementById('bonusBank');
  /* Os quatro verbos da aula JA NA 3a PESSOA: a moldura e "Bolt ______", e o
     chip tem de caber nela. Chip no infinitivo faria a crianca montar a frase
     errada e ouvir o modelo confirmando que esta certa. */
  [['checks','&#128269;'],['carries','&#128230;'],['lifts','&#127947;'],['fixes','&#128295;']]
    .forEach(function(p){
      var c = document.createElement('div');
      c.className = 'chip';
      c.innerHTML = p[1] + ' ' + p[0];
      c.onclick = function(){
        speak('Bolt ' + p[0] + ' every night.');
        fb(document.getElementById('fbz'), 'good',
           '&#128483; Now say it: <b>Bolt ' + p[0] + ' every night.</b>');
      };
      bz.appendChild(c);
    });
}

function restart(){
  st = { screen:0, avatar:st.avatar, stars:0, score:0, missed:[], doneStage:{} };
  document.getElementById('starCount').innerHTML = '&#11088; 0';
  go(0);
}

/* ---------- boot ---------- */
(function(){
  document.getElementById('recapStart').innerHTML = recapHTML();
  var avs = ['&#129490;','&#128102;','&#128103;','&#129489;'];
  var host = document.getElementById('avatars');
  avs.forEach(function(a){
    var d = document.createElement('div');
    d.className = 'av'; d.innerHTML = a;
    d.onclick = function(){
      [].forEach.call(host.children, function(x){ x.classList.remove('sel'); });
      d.classList.add('sel');
      st.avatar = a;
      document.getElementById('startBtn').disabled = false;
    };
    host.appendChild(d);
  });
  drawMap();
})();

window.pcGo3 = go; window.pcRestart3 = restart;
})();