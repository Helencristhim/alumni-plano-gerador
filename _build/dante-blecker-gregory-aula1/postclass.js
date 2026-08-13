(function(){
/* ==========================================================================
   DANTE -- AULA 01 -- DRAGON RIDER (Kids A2) -- PERCURSO POST-CLASS

   COPIADO do artefato "Dante Blecker Gregory · Kids A2 · Professor View", que e
   a ESPECIFICACAO desta peca: o percurso "The Helper Quest" veio inteiro, mecanica por
   mecanica. So mudou o que estava QUEBRADO nele (marcado CORRIGIDO abaixo) e o
   AUDIO_PHRASES, que o builder usa para gerar os MP3 (REGRA 7).
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
  "I can fly, but I can't swim.",
  "I can't swim, but I can breathe fire!",
  "dive",
  "carry",
  "climb",
  "A fish can swim.",
  "A dragon can breathe fire.",
  "Pip can swim, but she can't fly.",
  "I can run, but I can't fly.",
  "A heavy box is in front of the Dragon School gate. Nina can climb, but she can't carry the box. Pip can swim and dive, but she can't carry it. Storm can fly and carry the box.",
  "Storm",
  "Storm moves the box. Nina wants to help too. Nina can climb, but she can't carry the box.",
  "I can climb, but I can't carry the box.",
  "I can swim.",
  "I can climb.",
  "I can run.",
  "I can dive.",
  "I can fly.",
  "I can breathe fire."
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
   Tudo abaixo sai da versao FINAL de dante-aula01.html (Dragon Rider, Kids
   A2). Nenhum item introduz palavra, estrutura ou personagem que nao tenha
   sido trabalhado na aula -- e nenhum repete literalmente um exercicio dela.
   ==================================================================== */
/* PESOS -- somam 100 exatos, e cada um dentro da sua faixa normativa.
   Conferido por SOMA, nao por leitura: e a segunda das cinco armadilhas
   registradas do modelo ("peso por item != numero de itens").

     Supported Recall  20   secao 5: 15-20   |  secao 7 recall: 20-25
     Power Words       20   secao 5: 20-30   (10 + 10, em duas atividades)
     Language Move     30   secao 5: 30-40   -- o chunk leva o MAIOR peso
     New Mission       15   secao 5: 10-15
     Final Challenge   15   secao 5: 15-20
                      ---
                      100

   Consolidacao (Power Words + Language Move) = 50  -> secao 7: 40-50
   Transferencia (New Mission + Final)        = 30  -> secao 7: 25-35        */
var STAGES = [
  { id:'story',   name:'Story',    icon:'&#128270;', weight:20 },
  { id:'words1',  name:'Words',    icon:'&#11088;',  weight:10 },
  { id:'words2',  name:'Actions',  icon:'&#128172;', weight:10 },
  { id:'sayit',   name:'Say It',   icon:'&#128483;', weight:30 },
  { id:'mission', name:'New',      icon:'&#128506;&#65039;', weight:15 },
  { id:'final',   name:'Help!',    icon:'&#127937;', weight:15 }
];

/* --- RECAP: o contexto da aula, de volta na tela ---------------------
   O aluno nao pode rever o in-class. "Memoria apoiada" (secao 5 do framework):
   todo detalhe exigido na resposta tem de ser reapresentado aqui. */
function recapHTML(){
  /* O que cada personagem PODE fazer fica na tira -- e o criterio, nao a
     resposta. Sem isso os dois itens do Story Spot mediriam memoria episodica
     em vez de raciocinio. "Pip is cold and wet" esta aqui porque o item 2
     pergunta POR QUE Storm sopra fogo: a causa tem de ser inferivel.        */
  return '<h3>&#128218; The story so far</h3>' +
    '<div class="who">' +
      '<span>&#128009; Storm &mdash; can fly &middot; can breathe fire</span>' +
      '<span>&#128050; Pip &mdash; can swim &middot; can dive</span>' +
      '<span>&#128105; Nina &mdash; the rider</span>' +
    '</div>' +
    '<p class="story">The key is <b>in the lake</b>. Storm flies over the water&hellip; ' +
    'but he stops.<br>' +
    'Then Pip goes into the cold water. Now <b>Pip is very cold and very wet</b>.</p>';
}

/* --- 2. Story Replay: listen and choose / who said it? --------------- */
var STORY_ITEMS = [
  {
    /* O audio NAO diz quem fala -- diria a resposta. O aluno cruza a fala com
       a tira: quem voa e nao nada? Primeira das cinco armadilhas do modelo. */
    audio: "I can fly, but I can't swim.",
    q: 'Who says this?',
    opts: [
      { key:'storm', em:'&#128009;', lbl:'Storm' },
      { key:'pip',   em:'&#128050;', lbl:'Pip' },
      { key:'nina',  em:'&#128105;', lbl:'Nina' }
    ],
    answer: 'storm',
    ok:  'Yes! Storm can fly, but he can’t swim. That’s why he stops.',
    tip: 'Listen again. Who can fly? Look at the panel above. &#128009;',
    exp: 'Storm says it. He can fly and breathe fire — but not swim.'
  },
  {
    /* Causa simples -- o que a faixa A2 pede (secao 5.1). A resposta nao esta
       no audio: sai de cruzar a fala com "Pip is very cold and very wet".   */
    audio: "I can't swim, but I can breathe fire!",
    q: 'Why does Storm breathe fire?',
    opts: [
      { key:'dry',  em:'&#9925;', lbl:'to dry Pip' },
      { key:'key',  em:'&#128273;', lbl:'to find the key' },
      { key:'gate', em:'&#128682;', lbl:'to open the gate' }
    ],
    answer: 'dry',
    ok:  'Yes! Pip is cold and wet, so Storm makes her warm and dry.',
    tip: 'Look at the panel again. How does Pip feel after the water? &#128167;',
    exp: 'Pip is cold and wet. Storm can’t swim — but his fire can dry her.'
  }
];

/* --- 3. Power Words A: match action to picture ----------------------
   Tres das seis acoes da aula -- as que menos aparecem no dia a dia dele.
   fly e swim ficam de fora aqui porque voltam no gap-fill e no Say It.   */
var PAIRS = [
  { key:'dive',  word:'dive',  em:'&#129414;' },
  { key:'carry', word:'carry', em:'&#127890;' },
  { key:'climb', word:'climb', em:'&#128018;' }
];

/* --- 4. Power Words B: gap-fill, banco PARCIAL ----------------------
   Regra A2 (secao 6 do modelo): "reducao parcial do banco". O A1 tinha
   5 palavras para 3 lacunas; aqui sao 3 para 2 -- ha um distrator, e nao
   dois. Menos rede, mas ainda com rede.

   ok  = acerto.  exp = resposta revelada apos o segundo erro.
   Sao campos SEPARADOS de proposito: reaproveitar o texto de acerto faria
   o quiz dizer "Yes!" depois de dois erros. Quarta armadilha do modelo.  */
var BANK = ['breathe fire','swim','fly'];
var GAPS = [
  { before:'A fish can ', after:'.', answer:'swim', em:'&#128031;',
    ok:'Yes! A fish can swim.',
    exp:'The answer is: A fish can swim. &#128031;',
    tip:'What does a fish do in the water? &#127946;' },
  { before:'A dragon can ', after:'.', answer:'breathe fire', em:'&#128009;',
    ok:'Yes! A dragon can breathe fire.',
    exp:'The answer is: A dragon can breathe fire. &#128293;',
    tip:'Storm did this to dry Pip. &#128293;' }
];

/* --- 5. Language Move: sentence builder -- o chunk-alvo ---------------
   NENHUMA das duas frases e a que a aula ja montou no unjumble ("He can fly,
   but he can't swim." / "Pip can dive, but she can't breathe fire." / "I can
   climb, but I can't fly."). Repetir a mesma frase seria copia, e o modelo
   pede "repeticao transformada".

   A primeira e sobre a Pip -- terceira pessoa, como na aula. A segunda e na
   PRIMEIRA pessoa e sobre o proprio aluno: e a ponte para o Final Challenge,
   onde ele vai precisar dizer o que ELE pode fazer.                        */
var BUILDS = [
  { target:['Pip','can swim,','but she','can’t fly.'],
    shown: ['but she','can’t fly.','Pip','can swim,'], em:'&#128050;',
    say:'Pip can swim, but she can’t fly.' },
  { target:['I','can run,','but I','can’t fly.'],
    shown: ['can’t fly.','I','can run,','but I'], em:'&#127939;',
    say:'I can run, but I can’t fly.' }
];

/* ==========================================================================
   A CENA DO PORTAO -- serve a New Mission e o Final Challenge
   Uma funcao, dois usos: o cenario nao muda entre as duas telas, so a
   consequencia. A crianca ve o MESMO quadro e nao reconstroi nada de cabeca.

   O portao e desenhado (dois montantes e uma travessa), nao e emoji: precisa
   ser reconhecivel como PORTAO para que a caixa parada nele leia como
   obstaculo. A caixa vem depois dos montantes no DOM e fica no vao.
   Rotulo nomeia OBJETO (the gate, the box, nina, pip, storm) -- nunca relacao.
   ========================================================================== */
function gateScene(){
  return '<div class="scene">' +
    '<div class="sc-bar" style="left:0%;top:88%;width:100%;height:12%"></div>' +

    '<div class="sc-bar sc-trunk" style="left:38%;top:30%;width:24%;height:5%"></div>' +
    '<div class="sc-bar sc-trunk" style="left:40%;top:34%;width:3.5%;height:54%"></div>' +
    '<div class="sc-bar sc-trunk" style="left:56.5%;top:34%;width:3.5%;height:54%"></div>' +
    '<div class="sc-tag" style="left:50%;top:24%">the gate</div>' +

    '<div class="sc-tag" style="left:50%;top:67%">the box</div>' +
    '<div class="sc-obj" style="left:50%;top:77%;font-size:2.8rem">&#128230;</div>' +

    /* os tres no chao, dos dois lados do portao */
    '<div class="sc-obj" style="left:15%;top:79%;font-size:2rem">&#128105;</div>' +
    '<div class="sc-tag" style="left:15%;top:93%">nina</div>' +
    '<div class="sc-obj" style="left:76%;top:80%;font-size:1.8rem">&#128050;</div>' +
    '<div class="sc-tag" style="left:76%;top:93%">pip</div>' +
    '<div class="sc-obj" style="left:90%;top:78%;font-size:2.3rem">&#128009;</div>' +
    '<div class="sc-tag" style="left:90%;top:93%">storm</div>' +
  '</div>';
}

/* --- 6. NEW MISSION: problema NOVO com linguagem CONHECIDA ----------------
   O limite da exigencia de "contexto novo" (secao 7):

     contexto novo + linguagem conhecida   <- e isto
     contexto novo + CAMPO LEXICAL novo    <- nao e isto

   Os personagens e as habilidades sao os da aula 01 -- Nina, Pip, Storm; fly,
   swim, climb, dive, carry. "box" e "gate" tambem sao da aula, e "gate" e uma
   das seis palavras produtivas dela ("lake - key - gate - wings - wet"). O
   aluno aplica o CRITERIO (quem pode fazer o que) a um problema que nunca
   resolveu, sem ter de aprender palavra nenhuma para chegar a resposta.

   AS TRES ALTERNATIVAS ESTAO NO CENARIO, cada uma com o que PODE e o que NAO
   pode. Nada inferido de idade, tamanho ou aparencia: o texto declara tudo, e a
   cena mostra os tres presentes.

   O criterio e UM so e esta dito tres vezes -- carregar a caixa. Nina e Pip sao
   descartadas pelo que NAO podem, nao por algo que o aluno tenha de deduzir.   */
var MISSION = {
  sceneHTML: gateScene(),
  scene: 'A heavy box is in front of the Dragon School gate. Nina can climb, but she can’t carry the box. Pip can swim and dive, but she can’t carry it. Storm can fly and carry the box.',
  em: '&#128230;&#128682;',
  q: 'Who can move the box?',
  opts: [
    { key:'nina',  em:'&#128105;', lbl:'Nina' },
    { key:'pip',   em:'&#128050;', lbl:'Pip' },
    { key:'storm', em:'&#128009;', lbl:'Storm' }
  ],
  answer:'storm',
  ok:  'Yes! Storm can carry the box.',
  tip: 'Look again. Who can carry the box? &#128230;',
  exp: 'Storm can move the box. He can carry it.'
};

/* --- 7. FINAL CHALLENGE: resolver a missao COM o chunk --------------------
   MESMA cena, e a consequencia da escolha anterior. O que se avalia e o
   chunk-alvo (can..., but can't...), nao linguagem lateral.

   ESTA TELA E AUTOSSUFICIENTE: ela REPETE o que Nina pode e nao pode, em vez de
   remeter a tela anterior. A cena mostra quem esta presente, nao o que cada um
   consegue fazer -- habilidade nao se desenha. Sem a frase repetida aqui, a
   resposta dependeria de memoria da tela anterior, e o percurso inteiro existe
   para nao depender de memoria desassistida.

   A tarefa deixa de ser adivinhar e passa a ser transformar a 3a pessoa na 1a:
   operacao linguistica, com resposta sustentada pelo proprio texto.          */
var FINAL = {
  sceneHTML: gateScene(),
  scene: 'Storm moves the box. Nina wants to help too. Nina can climb, but she can’t carry the box.',
  em: '&#128230;&#128522;',
  q: 'What does Nina say?',
  opts: [
    { key:'a', lbl:'"I can climb, but I can’t carry the box."' },
    { key:'b', lbl:'"I can fly, but I can’t swim."' },
    { key:'c', lbl:'"I can carry the box, but I can’t climb."' }
  ],
  answer:'a',
  ok:  'Great! Nina can climb, but she can’t carry the box. Mission complete!',
  tip: 'What can Nina do? What can’t she do? &#128105;',
  exp: 'Nina says: “I can climb, but I can’t carry the box.”'
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
  if (n === 6) renderScene('s-final', 'Move the box!', '&#127937;', 'Final Challenge',
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
      '<div style="font-size:3.4rem">' + st.avatar + ' &#128230; &#128009;</div>' +
      /* REGRA: esta mensagem serve QUALQUER faixa de pontuacao, e por isso fala
         so de CONCLUSAO. Celebrar ter concluido e verdade para quem errou e
         seguiu depois da revelacao; afirmar acerto que pode nao ter havido, nao.
         Nenhuma variante que afirme desempenho pode existir nesta tela -- nem em
         comentario, para nao reaparecer em busca de validacao.
         E a UNICA mensagem de conclusao abaixo dos emojis. */
      '<p class="instr" style="margin:0 0 6px">You completed the Helper Quest. <b>The gate is clear!</b></p>' +
      '<div class="scorebig">' + pct + '%</div>' +
      '<div class="band">' + band + '</div>' +
      '<p class="instr" style="margin-bottom:6px">' + msg + '</p>' +
      '<div style="font-size:1.3rem;color:var(--star);font-weight:800">&#11088; ' + st.stars + ' stars</div>' +
      '<div class="badge"><span class="em">&#129464;</span> Badge unlocked: Can-Do Hero</div>' +
    '</div>' +
    review +
    '<div class="bonus">' +
      '<span class="tag">Bonus &middot; not scored</span>' +
      '<p style="margin:0 0 10px;font-size:1.1rem;font-weight:700">Your turn! Choose one and say the whole sentence:</p>' +
      '<p style="margin:0 0 10px;font-size:1.3rem;font-weight:800;color:var(--accent)">I can ______, but I can’t ______.</p>' +
      '<div class="bank" id="bonusBank"></div>' +
      '<div class="fb" id="fbz"></div>' +
    '</div>' +
    '<div class="actions" style="justify-content:center">' +
      /* CORRIGIDO: era onclick="restart()", e restart NAO e global (o arquivo
         inteiro e uma IIFE): o botao nao fazia nada. Chama o que esta exposto. */
      '<button class="btn btn-ghost" onclick="pcRestart1()">&#128260; Play again</button>' +
    '</div>';

  /* BONUS -- fora do percurso essencial e NAO pontuado (regra do modelo).
     O aluno escolhe uma acao e completa a frase sobre si mesmo: o chunk sai
     da historia e vai para a vida dele, que e o ponto da transferencia.   */
  var bz = document.getElementById('bonusBank');
  /* dive com o MESMO emoji da aula (o pato), e nao a lontra: o simbolo faz
     parte da palavra para uma crianca de 8 anos. */
  [['swim','&#127946;'],['climb','&#129495;'],['run','&#127939;'],['dive','&#129414;'],['fly','&#128038;'],['breathe fire','&#128293;']]
    .forEach(function(p){
      var c = document.createElement('div');
      c.className = 'chip';
      c.innerHTML = p[1] + ' ' + p[0];
      c.onclick = function(){
        speak('I can ' + p[0] + '.');
        fb(document.getElementById('fbz'), 'good',
           '&#128483; Now finish it: <b>I can ' + p[0] + ', but I can’t ______.</b>');
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

window.pcGo1 = go; window.pcRestart1 = restart;
})();