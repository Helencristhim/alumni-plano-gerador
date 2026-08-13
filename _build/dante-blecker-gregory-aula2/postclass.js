(function(){
/* ==========================================================================
   DANTE -- AULA 02 -- MY LEGO CITY (Kids A2) -- PERCURSO POST-CLASS

   COPIADO do artefato "Dante Blecker Gregory · Kids A2 · Professor View", que e
   a ESPECIFICACAO desta peca: o percurso "The Missing Piece Quest" veio inteiro, mecanica por
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
  "There are two boats here. But there is no red piece.",
  "There are five cars here. But there is no red piece.",
  "tower",
  "bridge",
  "wheel",
  "There are three streets in my city.",
  "There is a small park next to the tower.",
  "At school, Leo is building a Lego city. One red brick is missing! There are three books on the desk. There is a chair under the desk. And there is a red brick behind the door!",
  "behind the door",
  "Leo finds the red brick! Now his teacher asks him about the desk.",
  "There are three books on the desk.",
  "Is there a bed in your room?",
  "There is a bed in my room.",
  "Is there a door in your room?",
  "There is a door in my room.",
  "Is there a lamp in your room?",
  "There is a lamp in my room.",
  "Are there two windows in your room?",
  "There are two windows in my room.",
  "Are there three books in your room?",
  "There are three books in my room.",
  "Is there a chair in your room?",
  "There is a chair in my room."
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
   CONTEUDO -- fonte: dante-aula02.html
   AULA 2, My Lego City, Kids A2, chunk "There is / There are + coisa + lugar".
   Nenhum item introduz palavra, estrutura ou personagem fora dessa aula, e
   nenhum repete literalmente um exercicio dela.
   ==================================================================== */
/* PESOS -- somam 100 exatos, e cada um dentro da sua faixa normativa.
   REGRA: peso por ITEM != peso do estagio. Conferir por SOMA executada, nao
   por leitura.

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
  { id:'story',   name:'Search',   icon:'&#128269;', weight:20 },
  { id:'words1',  name:'Match',    icon:'&#11088;',  weight:10 },
  { id:'words2',  name:'Count',    icon:'&#128290;', weight:10 },
  { id:'sayit',   name:'Say It',   icon:'&#128483;', weight:30 },
  { id:'mission', name:'New',      icon:'&#128506;&#65039;', weight:15 },
  { id:'final',   name:'Find it!', icon:'&#127937;', weight:15 }
];

/* ==========================================================================
   A CENA DA CIDADE -- usada em TRES telas
   Uma funcao, tres usos: o recap (tela 1), a tira de recap que fica visivel
   durante o Search (tela 2, via comRecap) e a tela de contagem (tela 4). A
   crianca ve o MESMO mapa nas tres e nao reconstroi o cenario de cabeca.

   DUAS RELACOES ESPACIAIS, DUAS TECNICAS DIFERENTES:

   "under the bridge"  -> ALTURA basta. Os barcos ficam mais abaixo que a
                          ponte, e em cena 2D abaixo le-se como under.
   "behind the houses" -> ALTURA NAO BASTA: acima le-se como on/above. Os
                          carros ficam ATRAS de um .sc-block opaco, cortados
                          por ele. E a oclusao que diz "behind".

   O rotulo dos streets diz "streets", nunca "three streets": a tela de
   contagem pede que a crianca CONTE.
   ========================================================================== */
function cityScene() {
  return '<div class="scene">' +
    '<div class="sc-bar" style="left:4%;top:7%;width:92%;height:4%"></div>' +
    '<div class="sc-tag" style="left:50%;top:9%">the shelf</div>' +

    /* os cinco carros vem ANTES do bloco no DOM: e o que os coloca atras dele.
       Cerca de um terco coberto -- proporcao medida em tela, nao estimada: com
       pouco carro de fora a cena fica ambigua, com carro demais deixa de
       parecer "atras", e os CINCO tem de continuar contaveis (item 2). */
    '<div class="sc-obj" style="left:24%;top:31%;font-size:1.3rem">&#128663;&#128663;&#128663;&#128663;&#128663;</div>' +
    '<div class="sc-block" style="left:6%;top:32%;width:36%;height:12%"></div>' +
    '<div class="sc-obj sc-front" style="left:24%;top:38%;font-size:1.45rem">&#127968;&#127968;&#127968;</div>' +
    '<div class="sc-tag" style="left:24%;top:47%">houses</div>' +

    '<div class="sc-obj" style="left:56%;top:32%;font-size:2rem">&#128508;</div>' +
    '<div class="sc-tag" style="left:56%;top:45%">tower</div>' +
    '<div class="sc-obj" style="left:80%;top:34%">&#127795;</div>' +
    '<div class="sc-tag" style="left:80%;top:45%">park</div>' +

    '<div class="sc-bar sc-road" style="left:8%;top:55%;width:84%;height:3%"></div>' +
    '<div class="sc-bar sc-road" style="left:8%;top:62%;width:84%;height:3%"></div>' +
    '<div class="sc-bar sc-road" style="left:8%;top:69%;width:84%;height:3%"></div>' +
    '<div class="sc-tag" style="left:50%;top:76%">streets</div>' +

    '<div class="sc-bar sc-water" style="left:0%;top:80%;width:100%;height:20%"></div>' +
    '<div class="sc-tag" style="left:13%;top:84%">river</div>' +
    '<div class="sc-obj" style="left:50%;top:81%;font-size:1.5rem">&#127753;</div>' +
    '<div class="sc-obj" style="left:41%;top:93%;font-size:1.1rem">&#128676;</div>' +
    '<div class="sc-obj" style="left:59%;top:93%;font-size:1.1rem">&#128676;</div>' +
  '</div>';
}

/* --- RECAP: o contexto da aula, de volta na tela -------------------------
   "Memoria apoiada" (secao 5 do framework): o aluno nao pode rever o in-class,
   entao todo detalhe exigido na resposta esta AQUI.
   Numa aula de LUGAR isso quer dizer uma CENA, nao uma lista: os dois barcos
   estao sob a ponte na imagem, e os cinco carros ATRAS do bloco das casas.
   Sem isso, as perguntas do Search mediriam memoria em vez de leitura.      */
function recapHTML(){
  return '<h3>&#128218; The story so far</h3>' +
    '<p class="story">Max built a Lego city on the shelf. <b>One piece is missing</b> &mdash; ' +
    'the last piece of the roof. Max and Bia look for it.</p>' +
    cityScene() +
    '<div class="who">' +
      '<span>&#128102; Max &mdash; built the city</span>' +
      '<span>&#128103; Bia &mdash; helps him look</span>' +
      '<span>&#128008; Nino &mdash; the cat</span>' +
    '</div>';
}

/* --- 2. SEARCH (Supported Recall): ouvir e LOCALIZAR na cena ---------------
   A operacao e localizar, nao identificar quem falou -- essa era a do
   post-class 01, e a secao 7 proibe repetir operacao entre percursos.
   A resposta e um LUGAR, e o lugar esta na cena. REGRA: o audio nunca nomeia o
   lugar -- nomear seria dizer a resposta.                                    */
var STORY_ITEMS = [
  {
    audio: 'There are two boats here. But there is no red piece.',
    q: 'Where are Max and Bia looking?',
    opts: [
      { key:'bridge', em:'&#127753;', lbl:'under the bridge' },
      { key:'houses', em:'&#127960;&#65039;', lbl:'behind the houses' },
      { key:'park',   em:'&#127795;', lbl:'next to the park' }
    ],
    answer: 'bridge',
    ok:  'Yes! There are two boats under the bridge — and no red piece.',
    tip: 'Look at the picture. Where can you see two boats? &#128676;',
    exp: 'The two boats are under the bridge. That is where they look first.'
  },
  {
    audio: 'There are five cars here. But there is no red piece.',
    q: 'And where are they looking now?',
    opts: [
      { key:'bridge', em:'&#127753;', lbl:'under the bridge' },
      { key:'houses', em:'&#127960;&#65039;', lbl:'behind the houses' },
      { key:'river',  em:'&#127754;', lbl:'in the river' }
    ],
    answer: 'houses',
    ok:  'Yes! There are five cars behind the houses — and no red piece.',
    tip: 'Count again in the picture. Where are the five cars? &#128663;',
    exp: 'The five cars are behind the houses. Still no red piece!'
  }
];

/* --- 4. Word Power: QUANTIFICAR na cena -----------------------------------
   Operacao nova nesta faixa do percurso: contar e escolher o verbo. E o
   coracao do chunk da aula -- a quantidade decide is ou are -- e aqui a
   contagem e feita na imagem, nao de memoria.

   As tres alternativas trazem a forma verbal ja concordada (one street /
   three streets / five streets), entao o que a crianca decide e a QUANTIDADE.
   Por isso nenhum rotulo da cena pode trazer numero: com "three streets"
   escrito na imagem ela le o rotulo e escolhe, e a atividade nao mede nada.
   Rotulo de cena nomeia OBJETO -- nunca quantidade, nunca relacao.          */
var COUNT_ITEMS = [
  {
    q: 'Look at the city. How many streets are there?',
    opts: [
      { key:'a', lbl:'There is one street.' },
      { key:'b', lbl:'There are three streets.' },
      { key:'c', lbl:'There are five streets.' }
    ],
    answer:'b',
    ok:  'Yes! There are three streets. Three, so <b>are</b>.',
    tip: 'Count the grey lines in the picture. &#128290;',
    exp: 'There are three streets. More than one, so it is <b>are</b>.'
  },
  {
    q: 'And the tower? How many towers are there?',
    opts: [
      { key:'a', lbl:'There is a tower in the middle.' },
      { key:'b', lbl:'There are two towers in the middle.' },
      { key:'c', lbl:'There are three towers in the middle.' }
    ],
    answer:'a',
    ok:  'Yes! Only one tower — so <b>is</b>, not are.',
    tip: 'How many towers can you see in the picture? &#128508;',
    exp: 'There is a tower in the middle. Only one, so it is <b>is</b>.'
  }
];

/* --- 3. Word Stars: MEMORY PAIRS -----------------------------------------
   Mecanica nova neste percurso (lista A2 do modelo, secao 6) e diferente do
   match do post-class 01: la as duas colunas estavam abertas, aqui as cartas
   comecam viradas. A operacao passa a ser lembrar onde vi, nao so associar.
   Tres pares = seis cartas: o suficiente para a mecanica funcionar sem virar
   teste de memoria longo.                                                   */
var PAIRS = [
  { key:'tower',  word:'tower',  em:'&#128508;' },
  { key:'bridge', word:'bridge', em:'&#127753;' },
  { key:'wheel',  word:'wheel',  em:'&#128734;' }
];

/* --- 5. Language Move: COMPLETAR TURNO DE DIALOGO ------------------------
   Dialogue builder (lista A2, secao 6). Nao e o sentence builder solto do
   post-class 01: aqui o turno ANTERIOR esta na tela, e a frase montada tem de
   responder aquela pergunta. A forma e a mesma; o que muda e que agora existe
   um interlocutor, e a escolha de is/are depende do que ele perguntou.
   Nenhuma das duas frases e uma das que a aula ja montou no gap-fill.       */
var BUILDS = [
  { ask:  { who:'&#128103;', txt:'Max, how many streets are there?' },
    target:['There are','three streets','in my city.'],
    shown: ['in my city.','There are','three streets'], em:'&#128739;&#65039;',
    say:'There are three streets in my city.' },
  { ask:  { who:'&#128103;', txt:'And what is next to the tower?' },
    target:['There is','a small park','next to the tower.'],
    shown: ['next to the tower.','a small park','There is'], em:'&#127795;',
    say:'There is a small park next to the tower.' }
];

/* --- 6. NEW MISSION: cenario NOVO com linguagem CONHECIDA -----------------
   A secao 7 pede contexto novo. O limite dessa exigencia:

     contexto novo + linguagem conhecida   <- e isto
     contexto novo + CAMPO LEXICAL novo    <- nao e isto

   O objeto PROCURADO tem de ser palavra da aula. Se for desconhecido, o item
   para de medir There is/are + preposicao e passa a medir aquisicao de
   vocabulario. Aqui e um RED BRICK: "brick" e uma das seis palavras produtivas
   da aula ("tower - bridge - street - roof - wheel - brick"). "chair" e "book"
   tambem sao da aula, e "chair" aparece nela com esta familia de preposicao
   ("There is a door behind the chair").

   UMA palavra nova em toda a tela: DESK. Periferica -- nao e a resposta, tem
   rotulo na cena e tem desenho (a barra do tampo, com os livros em cima e a
   cadeira embaixo).

   A CENA e obrigatoria mesmo com o texto dizendo onde o brick esta: este item
   e de LEITURA, porque a aula 02 e a aula-modelo de leitura do Dante. O papel
   da cena nao e esconder a resposta, e nao CONTRADIZE-LA -- brick desenhado
   abaixo da porta ensinaria que "behind" significa "under". Dai o .sc-block.
   ========================================================================== */
function classScene(){
  return '<div class="scene">' +
    /* o tampo da mesa: livros ENCOSTADOS nele por cima, cadeira por baixo --
       "on" e "under" se resolvem por altura, como os barcos e a ponte. Os
       livros ficam colados na barra de proposito: com folga entre os dois eles
       flutuam, e "on the desk" deixa de ser o que a imagem mostra. */
    '<div class="sc-obj" style="left:26%;top:33%;font-size:1.5rem">&#128218;&#128218;&#128218;</div>' +
    '<div class="sc-bar" style="left:10%;top:37%;width:48%;height:6%"></div>' +
    '<div class="sc-tag" style="left:52%;top:49%">the desk</div>' +
    '<div class="sc-obj" style="left:28%;top:58%;font-size:1.9rem">&#129681;</div>' +
    '<div class="sc-tag" style="left:28%;top:71%">the chair</div>' +

    /* o brick vem ANTES da porta no DOM, e a porta e um bloco OPACO: o que se
       ve do brick e so a metade que sobra da borda da porta. "behind", na
       imagem. O bloco tem proporcao de porta -- alto e estreito -- porque um
       quadrado branco grande com um emoji pequeno no meio nao le como porta.
       Rotulo nenhum diz "behind the door": rotulo aqui nomeia OBJETO, nunca
       relacao, senao a cena imprime a resposta da pergunta. */
    '<div class="sc-obj" style="left:74%;top:52%;font-size:1.8rem">&#129521;</div>' +
    '<div class="sc-block" style="left:74%;top:22%;width:14%;height:46%"></div>' +
    '<div class="sc-obj sc-front" style="left:81%;top:45%;font-size:3.4rem">&#128682;</div>' +
    '<div class="sc-tag" style="left:81%;top:74%">the door</div>' +
  '</div>';
}
var MISSION = {
  sceneHTML: classScene(),
  scene: 'At school, Leo is building a Lego city. One red brick is missing! There are three books on the desk. There is a chair under the desk. And there is a red brick behind the door!',
  em: '&#129521;&#128682;',
  q: 'Where is the red brick?',
  opts: [
    { key:'desk',  em:'&#128218;', lbl:'on the desk' },
    { key:'under', em:'&#129681;', lbl:'under the desk' },
    { key:'door',  em:'&#128682;', lbl:'behind the door' }
  ],
  answer:'door',
  ok:  'Yes! There is a red brick behind the door.',
  tip: 'Read again, and look at the picture. What is on the desk? And under it? &#128269;',
  exp: 'The red brick is behind the door. On the desk there are books; under it, a chair.'
};

/* --- 7. FINAL CHALLENGE: resolver a missao COM o chunk ---------------------
   O desfecho e consequencia do que o aluno faz, e o que se avalia e o
   chunk-alvo, nao linguagem lateral.

   Complementar a New Mission: la o texto traz a resposta e o item e de leitura;
   aqui e a CENA que decide, e o aluno conta para escolher entre is e are.
   Os distratores nao sao absurdos -- erram a quantidade ou o lugar, que e
   exatamente o que a aula ensinou a controlar.                              */
var FINAL = {
  sceneHTML: classScene(),
  scene: 'Leo finds the red brick! Now his teacher asks him about the desk.',
  em: '&#129521;&#128522;',
  q: 'What does Leo say about the desk?',
  opts: [
    { key:'a', lbl:'"There are three books on the desk."' },
    { key:'b', lbl:'"There is three books on the desk."' },
    { key:'c', lbl:'"There is a book under the desk."' }
  ],
  answer:'a',
  ok:  'Great! Three books, so <b>There are</b>. Mission complete!',
  tip: 'Count the books in the picture. Then choose <b>is</b> or <b>are</b>. &#128218;',
  exp: 'There are three books on the desk. More than one, so it is <b>are</b>.'
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
  /* peso POR ITEM: Supported Recall vale 20, em 2 itens = 10 cada.
     comRecap=true liga a tira de recap -- sem ela estes dois itens
     dependeriam de memoria desassistida, que a secao 7 proibe. */
  if (n === 1) renderChoice('s-story', 'Search the city', '&#128269;', 'Supported Recall',
                            'Listen. Then find the place in the picture.',
                            STORY_ITEMS, 'story', 10, true);
  if (n === 2) renderMemory();
  if (n === 3) renderChoice('s-words2', 'Count and say', '&#128290;', 'Power Words',
                            'Look at the city. Count, then choose the right sentence.',
                            COUNT_ITEMS, 'words2', 5, false, cityScene());
  if (n === 4) renderBuild();
  if (n === 5) renderScene('s-mission', 'New Mission', '&#128506;&#65039;', 'New Mission',
                           MISSION, 'mission', 15, 'Next stop &#10132;', 6);
  if (n === 6) renderScene('s-final', 'Help Leo!', '&#127937;', 'Final Challenge',
                           FINAL, 'final', 15, 'See my result &#127942;', 7);
  if (n === 7) renderResult();
  window.scrollTo(0, 0);
}

function fb(el, kind, msg){
  el.className = 'fb show ' + kind;
  el.innerHTML = msg;
}

/* ====================================================================
   MOTOR 1 -- escolha sequencial, com audio opcional (telas SEARCH e COUNT)
   Um item por vez: "uma acao central por tela" (modelo, principios).
   ==================================================================== */
function renderChoice(elId, title, icon, eyebrow, instr, items, stageId, weightEach, comRecap, sceneHTML){
  var host = document.getElementById(elId);
  var idx = 0, tries = 0;

  function paint(){
    var it = items[idx];
    /* O botao de audio so aparece se o item TIVER audio. As telas de contagem
       nao tem: a informacao esta na cena, e um play mudo seria promessa falsa. */
    var temAudio = !!it.audio;
    host.innerHTML =
      '<div class="eyebrow">' + eyebrow + '</div>' +
      '<h2>' + icon + ' ' + title + '</h2>' +
      '<p class="instr">' + instr + '</p>' +
      /* o contexto fica VISIVEL durante as perguntas, nao so antes delas */
      (comRecap ? '<div class="recap">' + recapHTML() + '</div>' : '') +
      (sceneHTML || '') +
      (items.length > 1 ? '<div class="counter">Question ' + (idx+1) + ' of ' + items.length + '</div>' : '') +
      (temAudio
        ? '<div class="actions" style="margin:0 0 16px">' +
            '<button class="audio-btn big" data-role="say">&#128266; Listen</button>' +
          '</div>'
        : '') +
      '<p class="q">' + it.q + '</p>' +
      /* REGRA: motor chamado mais de uma vez nao usa id fixo. Este serve DUAS
         telas (Search e Count); o mesmo id sairia duas vezes no documento e
         getElementById devolve sempre a PRIMEIRA ocorrencia -- a segunda tela
         subiria com a pergunta e NENHUMA opcao, travando o percurso.
         O marcador e ATRIBUTO e nao classe, porque fb() reescreve className. */
      '<div class="opts' + (it.opts[0].em ? '' : ' lines') + '" data-role="opts"></div>' +
      '<div class="fb" data-role="fb"></div>' +
      '<div class="actions"><button class="btn" data-role="next" hidden>Next &#10132;</button></div>';

    if (temAudio) host.querySelector('[data-role="say"]').onclick = function(){ speak(it.audio, this); };
    var op = host.querySelector('[data-role="opts"]');
    it.opts.forEach(function(o){
      var d = document.createElement('div');
      d.className = 'opt';
      d.innerHTML = (o.em ? '<span class="pic">' + o.em + '</span>' : '') +
                    '<span class="lbl">' + o.lbl + '</span>';
      d.onclick = function(){ choose(o, d); };
      op.appendChild(d);
    });
    if (temAudio) setTimeout(function(){ speak(it.audio); }, 350);
  }

  function choose(o, node){
    var it = items[idx];
    var box = host.querySelector('[data-role="fb"]');
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
        if (it.audio) speak(it.audio);
      } else {
        /* segundo erro: mostrar a resposta + exemplo curto, e seguir */
        lock();
        var right = it.opts.filter(function(x){ return x.key === it.answer; })[0];
        [].forEach.call(host.querySelectorAll('[data-role="opts"] .opt'), function(el){
          if (el.querySelector('.lbl').textContent === right.lbl) el.classList.add('ok');
        });
        fb(box, 'tip', '&#128172; ' + it.exp);
        award(weightEach, false, it.exp);
        finishItem();
      }
    }
  }
  function lock(){
    [].forEach.call(host.querySelectorAll('[data-role="opts"] .opt'), function(el){ el.classList.add('lock'); });
  }
  function finishItem(){
    var nx = host.querySelector('[data-role="next"]');
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
   MOTOR 2 -- MEMORY PAIRS (Word Stars)
   Seis cartas viradas: tres palavras e tres imagens. A operacao e lembrar
   onde vi, e nao apenas associar o que esta aberto -- diferente do match de
   duas colunas do post-class 01.

   Errar NAO retira estrela (regra estrutural do modelo): o par volta a ficar
   virado e a estrela vem quando o par e fechado. O score guarda a primeira
   tentativa, e so ele distingue quem acertou de primeira.
   ==================================================================== */
function renderMemory(){
  var host = document.getElementById('s-words1');
  /* Baralho fixo: os pares sao poucos e a ordem embaralhada de verdade poderia
     colocar os dois iguais lado a lado, o que esvazia a mecanica. Esta ordem
     separa cada par. */
  var deck = [
    { key:'tower',  kind:'w' }, { key:'bridge', kind:'p' }, { key:'wheel',  kind:'w' },
    { key:'bridge', kind:'w' }, { key:'wheel',  kind:'p' }, { key:'tower',  kind:'p' }
  ];
  var aberta = null, fechados = 0, errou = {}, travado = false;

  host.innerHTML =
    '<div class="eyebrow">Power Words</div>' +
    '<h2>&#11088; Word Match</h2>' +
    '<p class="instr">Tap two cards. Find the word and its picture. Say the word out loud!</p>' +
    '<div class="mem" id="mm"></div>' +
    '<div class="fb" id="fbm"></div>' +
    '<div class="actions"><button class="btn" id="nxm" hidden>Next stop &#10132;</button></div>';

  var mm = document.getElementById('mm');
  deck.forEach(function(d, i){
    var par = PAIRS.filter(function(x){ return x.key === d.key; })[0];
    var el = document.createElement('div');
    el.className = 'mcard down';
    el.dataset.key = d.key; el.dataset.i = i;
    el.innerHTML = (d.kind === 'w')
      ? '<span class="w">' + par.word + '</span>'
      : par.em;
    el.onclick = function(){ virar(el, par); };
    mm.appendChild(el);
  });

  function virar(el, par){
    if (travado || el.classList.contains('got') || el === aberta) return;
    el.classList.remove('down'); el.classList.add('up');
    speak(par.word);
    if (!aberta){ aberta = el; return; }

    var box = document.getElementById('fbm');
    if (aberta.dataset.key === el.dataset.key){
      aberta.classList.remove('up'); aberta.classList.add('got');
      el.classList.remove('up');     el.classList.add('got');
      fechados++;
      award(10/3, !errou[par.key], errou[par.key] ? 'This is a <b>' + par.word + '</b>. ' + par.em : null);
      fb(box, 'good', '&#11088; ' + par.word + '! One star.');
      aberta = null;
      if (fechados === PAIRS.length){
        fb(box, 'good', '&#127881; All three pairs found!');
        st.doneStage.words1 = true;
        var b = document.getElementById('nxm');
        b.hidden = false; b.onclick = function(){ go(3); };
      }
    } else {
      /* Segunda tentativa sempre liberada, e nada e retirado: as duas cartas
         voltam a virar e o par fica marcado como "ja errado" so para o score. */
      errou[aberta.dataset.key] = true; errou[el.dataset.key] = true;
      fb(box, 'tip', '&#128161; Not a pair. Look again &mdash; where was it?');
      var a = aberta, b2 = el;
      travado = true; aberta = null;
      setTimeout(function(){
        a.classList.remove('up'); a.classList.add('down');
        b2.classList.remove('up'); b2.classList.add('down');
        travado = false;
      }, 900);
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
      '<h2>&#128483; Answer Bia</h2>' +
      '<p class="instr">Bia asks. Build Max&rsquo;s answer, then say it out loud!</p>' +
      '<div class="counter">Answer ' + (idx+1) + ' of ' + BUILDS.length + '</div>' +
      /* O turno de Bia fica na tela: a frase montada tem de RESPONDER a
         pergunta dela, e e a pergunta que decide is ou are. O turno anterior e
         o que distingue esta operacao de um sentence builder solto. */
      '<div class="dlg">' +
        '<div class="turn"><span class="who">' + b.ask.who + '</span>' +
          '<span class="said">' + b.ask.txt + '</span></div>' +
        '<div class="turn me"><span class="who">&#128102;</span>' +
          '<span class="said" id="mirror">&hellip;</span></div>' +
      '</div>' +
      '<div style="font-size:2.6rem;text-align:center;margin-bottom:8px">' + b.em + '</div>' +
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
    /* espelha a frase no turno do Max: a crianca ve a resposta tomando forma
       DENTRO do dialogo, nao numa linha solta ao lado dele */
    var mi = document.getElementById('mirror');
    if (mi) mi.innerHTML = chosen.length
      ? chosen.map(function(c){ return c.w; }).join(' ')
      : '&hellip;';
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
        /* erro no chunk: destacar so a parte fixa -- comecar por There is/are,
           e a quantidade decide qual -- sem entregar a frase. Modelo, secao 9. */
        fb(box, 'tip', '&#128161; Start with <b>There is</b> or <b>There are</b>. How many things? &#128266; Listen and try again.');
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
  /* Sem id nos elementos internos: tudo por host.querySelector. Ver a regra em
     renderChoice -- motor chamado mais de uma vez nao usa id fixo. */
  host.innerHTML =
    '<div class="eyebrow">' + eyebrow + '</div>' +
    '<h2>' + icon + ' ' + title + '</h2>' +
    '<div style="font-size:2.6rem;text-align:center">' + data.em + '</div>' +
    '<p class="instr" style="text-align:center;font-size:1.1rem">' + data.scene + '</p>' +
    /* A CENA, quando existe. Numa aula de lugar o texto sozinho nao estabelece
       a relacao: "behind the door" precisa ser visto. */
    (data.sceneHTML || '') +
    '<div class="actions" style="margin:0 0 16px">' +
      '<button class="audio-btn big js-say">&#128266; Listen</button>' +
    '</div>' +
    '<p class="q">' + data.q + '</p>' +
    '<div class="opts' + (data.opts[0].em ? '' : ' lines') + '" data-role="opts"></div>' +
    /* data-role e nao classe: fb() reescreve o className inteiro deste bloco. */
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
  if (pct >= 90){ band = 'Mission mastered!'; msg = 'You know what is where — and when to say is or are. Amazing work!'; }
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
      '<div style="font-size:3.4rem">' + st.avatar + ' &#129521; &#128508;</div>' +
      /* REGRA: esta mensagem serve QUALQUER faixa de pontuacao, e por isso fala
         so de CONCLUSAO. Celebrar ter concluido e verdade para quem errou e
         seguiu depois da revelacao; afirmar acerto que pode nao ter havido, nao.
         Nenhuma variante que afirme desempenho pode existir nesta tela -- nem em
         comentario, para nao reaparecer em busca de validacao. */
      '<p class="instr" style="margin:0 0 6px">You completed the Missing Piece Quest. <b>Leo found the red brick!</b></p>' +
      '<div class="scorebig">' + pct + '%</div>' +
      '<div class="band">' + band + '</div>' +
      '<p class="instr" style="margin-bottom:6px">' + msg + '</p>' +
      '<div style="font-size:1.3rem;color:var(--star);font-weight:800">&#11088; ' + st.stars + ' stars</div>' +
      '<div class="badge"><span class="em">&#128508;</span> Badge unlocked: City Finder</div>' +
    '</div>' +
    review +
    '<div class="bonus">' +
      '<span class="tag">Bonus &middot; not scored</span>' +
      '<p style="margin:0 0 10px;font-size:1.1rem;font-weight:700">Your turn! Look at your room. Choose something you can <b>really</b> see:</p>' +
      '<p style="margin:0 0 10px;font-size:1.3rem;font-weight:800;color:var(--accent)">There is / There are ______ in my room.</p>' +
      '<div class="bank" id="bonusBank"></div>' +
      '<div class="fb" id="fbz"></div>' +
    '</div>' +
    '<div class="actions" style="justify-content:center">' +
      /* CORRIGIDO: era onclick="restart()", e restart NAO e global (o arquivo
         inteiro e uma IIFE): o botao nao fazia nada. Chama o que esta exposto. */
      '<button class="btn btn-ghost" onclick="pcRestart2()">&#128260; Play again</button>' +
    '</div>';

  /* BONUS -- fora do percurso essencial e NAO pontuado (regra do modelo).
     O aluno olha o PROPRIO quarto e diz o que ha nele: o molde sai da cidade de
     Lego e vai para o lugar onde ele esta. E ai que a transferencia deixa de ser
     exercicio.

     REGRA: o sistema NAO AFIRMA sobre o mundo do aluno -- ele nao ve o quarto.
     Chip que gerasse "There are two windows in my room." ensinaria que a frase e
     formula para recitar, e nao afirmacao verdadeira; e isso destroi o proposito
     justamente da atividade que sai do exercicio. Entao o chip PERGUNTA antes, e
     a frase so existe depois do Yes. Em No nada e afirmado.

     A pergunta usa o molde da aula na forma interrogativa ("Is there a bed in
     your room?"). Extensao pequena e declarada: o aluno nao produz a pergunta,
     so toca Yes ou No, e a forma interrogativa de There is/are ja aparece neste
     percurso (o Language Move traz "how many streets are there?").

     "Something else" e obrigatorio: nenhuma lista de seis chips cobre um quarto
     real. Ali o sistema mostra os dois moldes com lacuna e devolve a frase ao
     aluno, sem afirmar nada e sem digitacao.

     Os seis chips saem todos da aula 02 (bed, door, lamp, window, book, chair
     estao na cena do quarto dela): o bonus nao introduz lexico novo.         */
  var bz = document.getElementById('bonusBank');
  var fz = document.getElementById('fbz');

  /* [rotulo, emoji, verbo, abertura da pergunta] -- o verbo e a abertura
     concordam com o numero do rotulo, para que a escolha entre is e are
     continue sendo o conteudo e nao um detalhe. */
  var ROOM = [
    ['a bed',       '&#128719;', 'is',  'Is there'],
    ['a door',      '&#128682;', 'is',  'Is there'],
    ['a lamp',      '&#128161;', 'is',  'Is there'],
    ['two windows', '&#129695;', 'are', 'Are there'],
    ['three books', '&#128218;', 'are', 'Are there'],
    ['a chair',     '&#129681;', 'is',  'Is there']
  ];

  function askRoom(p){
    var pergunta = p[3] + ' ' + p[0] + ' in your room?';
    /* data-role e nao id: este bloco e repintado a cada chip. Mesma regra do
       renderChoice. */
    fb(fz, 'tip', '&#128269; <b>' + pergunta + '</b>' +
      '<div class="actions" style="justify-content:center;margin-top:10px">' +
        '<button class="btn btn-ghost" data-role="yes">&#9989; Yes</button>' +
        '<button class="btn btn-ghost" data-role="no">&#128683; No</button>' +
      '</div>');
    speak(pergunta);
    fz.querySelector('[data-role="yes"]').onclick = function(){
      var frase = 'There ' + p[2] + ' ' + p[0] + ' in my room.';
      fb(fz, 'good', '&#128483; Say it: <b>' + frase + '</b>');
      speak(frase);
    };
    fz.querySelector('[data-role="no"]').onclick = function(){
      /* nenhuma frase e dita aqui: nada de falso sai do sistema */
      fb(fz, 'tip', '&#128077; No problem! Choose something you can really see.');
    };
  }

  ROOM.forEach(function(p){
    var c = document.createElement('div');
    c.className = 'chip';
    c.innerHTML = p[1] + ' ' + p[0];
    c.onclick = function(){ askRoom(p); };
    bz.appendChild(c);
  });

  var outro = document.createElement('div');
  outro.className = 'chip';
  outro.innerHTML = '&#10133; Something else';
  outro.onclick = function(){
    fb(fz, 'tip', '&#128483; Your turn! Look around and say it:<br>' +
       '<b>There is &hellip; in my room.</b><br><b>There are &hellip; in my room.</b>');
  };
  bz.appendChild(outro);
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

window.pcGo2 = go; window.pcRestart2 = restart;
})();