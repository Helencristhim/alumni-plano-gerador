#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A TROCA DO MOTOR DE AUDIO, na derivacao artefato -> shell (AUT-004).

    "Web Speech API, speechSynthesis e SpeechSynthesisUtterance sao proibidos no build
     oficial." — Anexo P-A, Regra canonica

POR QUE AQUI, E NAO NO ARTEFATO
--------------------------------
O artefato usa sintese do navegador COM RAZAO: ele e prototipo numa pagina do claude.ai,
onde nao ha MP3 para servir, e o proprio anexo (§1) admite esse modo -- "Prototipo/validacao:
sintese do navegador admitida, NAO publicavel para uso oficial". Mexer no artefato quebraria
o `--check`, que existe para provar que o shell E o artefato e que nada foi reescrito no
caminho.

A derivacao ja e o lugar onde "prototipo vira producao": e ela que carimba
`alumni-anatomia`, que troca a chave de estado e que tira o nome de pessoa do `STORE`. A
troca do motor e mais uma transformacao declarada da mesma natureza.

O QUE MUDA, E O QUE NAO
------------------------
NAO muda a interface: `say`, `sayAs`, `playTalk`, `audStop`, `audMain` e `stopSay` mantem a
assinatura, entao NENHUM HTML de aula precisa ser reescrito -- e sao 82 call sites so no
molde. Tambem nao mudam o transporte (`audEstado`, `audBuild`, `audUni`, `audOpcao`) nem o
realce (`markSpeaker`).

MUDA o que produz o som: em vez de enfileirar `SpeechSynthesisUtterance`, o motor toca um
ARQUIVO APROVADO, resolvido em `AUD_MAP` pelo proprio texto (fala) ou pela chave do trecho
(dialogo). E somem `pickVoice`, `enVoices`, `pickCast`, `voiceReport` e `VOICE_PREF` -- a
tabela que escolhia voz por NOME COMERCIAL do sistema ("Microsoft Aria", "Samantha"), que o
§4 proibe com todas as letras: "os nomes comerciais de voz nao substituem Voice IDs".

TRES DECISOES QUE VALEM SER LIDAS
----------------------------------
1. **Velocidade e `playbackRate`, nao arquivo novo.** "Normal" e "Slower" sao o MESMO audio.
   Gerar os dois dobraria custo, QA e chance de divergirem na proxima edicao do texto. O
   artefato passava 0.95 e 0.85 ao TTS; aqui vira `rate/0.95`, entao 0.95 e a velocidade
   natural da gravacao.
2. **Um arquivo por dialogo, com os instantes de cada turno.** O §3 exige "um arquivo final
   por dialogo". Sozinho, isso mataria o realce de quem fala. O endpoint
   `text-to-dialogue/with-timestamps` devolve o inicio de cada turno, esses instantes vao
   para o `AUD_MAP`, e o realce passa a ser dirigido pelo relogio do proprio audio.
3. **Falha de midia NAO cai para o navegador.** O §1 e explicito. Sem o arquivo, o player
   escreve o estado no proprio componente e para -- que e onde a pessoa esta olhando.
"""

MOTOR = """/* ---------------- AUDIO OFICIAL (Anexo P-A) ----------------
   O motor toca ARQUIVO APROVADO, gerado no pipeline seguro antes da publicacao. Web Speech
   e proibido aqui, e a voz e escolhida por Voice ID na geracao -- nunca por nome comercial
   do sistema no navegador. Ver scripts/consultivo/_motor_audio.py. */
var AUD_MAP=(typeof AUD_MAP!=='undefined')?AUD_MAP:{};
var AUD_EL=null;
/* O que pode faltar e o ARQUIVO, nunca o suporte: <audio> existe em todo navegador que
   abre este material. Por isso a pergunta migrou de "ha sintese?" para "ha fonte?". */
function audSuportado(){ return true; }
function audEntrada(chave){ return AUD_MAP&&Object.prototype.hasOwnProperty.call(AUD_MAP,chave)?AUD_MAP[chave]:null; }
function audFonte(chave){ var e=audEntrada(chave); return e?(e.src||e):null; }
function audTurnos(chave){ var e=audEntrada(chave); return (e&&e.turnos)||null; }
/* A velocidade do artefato era do TTS (0.95 normal, 0.85 devagar). Numa GRAVACAO, 0.95 e a
   velocidade natural -- entao ela vira 1, e o "Slower" vira a razao. */
function audRate(r){ return r?(r/0.95):1; }
function audParar(){ if(AUD_EL){ try{AUD_EL.pause();}catch(e){} AUD_EL=null; } }"""

# ---------------------------------------------------------------------------
# as substituicoes, em ordem. cada uma tem de casar EXATAMENTE uma vez.
# ---------------------------------------------------------------------------
TROCAS = [
    # 1. o seletor de voz do navegador sai inteiro
    ("pickVoice/fora",
     """var _voice=null;
function pickVoice(){
  if(!('speechSynthesis' in window))return null;
  var vs=speechSynthesis.getVoices()||[];
  var pref=['Google US English','Microsoft Aria','Microsoft Jenny','Samantha','Alex'];
  for(var p=0;p<pref.length;p++)for(var i=0;i<vs.length;i++)if(vs[i].name.indexOf(pref[p])>-1)return vs[i];
  for(var j=0;j<vs.length;j++)if(vs[j].lang&&vs[j].lang.indexOf('en-US')===0)return vs[j];
  for(var k=0;k<vs.length;k++)if(vs[k].lang&&vs[k].lang.indexOf('en')===0)return vs[k];
  return null;
}
if('speechSynthesis' in window){speechSynthesis.onvoiceschanged=function(){_voice=pickVoice()};_voice=pickVoice();}""",
     MOTOR),

    # 2. capacidade: deixa de perguntar pela sintese
    ("audSuportado/arquivo",
     "function audSuportado(){ return 'speechSynthesis' in window; }",
     ""),

    # 3. o transporte: fila de utterances -> elemento <audio>
    ("audFala/arquivo",
     """function audFala(grupo,montar){
  if(!audSuportado()){ audAviso(grupo); return; }
  speechSynthesis.cancel();
  AUD.dono=grupo; AUD.refazer=montar;
  montar();
  var fim=new SpeechSynthesisUtterance(' ');
  fim.onend=function(){ if(AUD.dono===grupo)audEstado('fim'); };
  speechSynthesis.speak(fim);
  audEstado('tocando');
}""",
     """/* `montar()` deixa de ENFILEIRAR som e passa a DESCREVER o que tocar:
     {src, rate, turnos, show}. O transporte e o mesmo em todo lugar -- era assim com a
     fila da sintese e continua sendo com o <audio>. */
function audFala(grupo,montar){
  audParar();
  var spec=montar();
  if(!spec||!spec.src){ audAviso(grupo); return; }
  AUD.dono=grupo; AUD.refazer=montar;
  var a=new Audio(spec.src);
  AUD_EL=a;
  a.playbackRate=spec.rate||1;
  /* o realce de quem fala e dirigido pelo RELOGIO do proprio arquivo: um MP3 por dialogo
     (Anexo P-A §3) com os instantes que o endpoint with-timestamps devolveu. */
  if(spec.show&&spec.turnos&&spec.turnos.length){
    var ult=-2;
    a.addEventListener('timeupdate',function(){
      var t=a.currentTime,i,quem=-1;
      for(i=0;i<spec.turnos.length;i++){ if(t>=spec.turnos[i].inicio)quem=spec.turnos[i].speaker; }
      if(quem!==ult){ ult=quem; markSpeaker(quem); }
    });
  }
  a.addEventListener('ended',function(){
    if(AUD.dono===grupo){ markSpeaker(-1); audEstado('fim'); }
  });
  /* Falha de midia NAO autoriza fallback para sintese do navegador (Anexo P-A §1). */
  a.addEventListener('error',function(){ if(AUD.dono===grupo)audAviso(grupo); });
  a.play().catch(function(){ audAviso(grupo); });
  audEstado('tocando');
}"""),

    # 4. o aviso deixa de falar em navegador e passa a falar do arquivo
    ("audAviso/arquivo",
     "if(st)st.textContent='Audio not available in this browser';",
     "if(st)st.textContent='Audio not available for this item';"),

    # 5. pausa e retomada no elemento
    ("audAlterna/arquivo",
     """function audAlterna(g){
  if(!g||AUD.dono!==g||!audSuportado())return false;
  if(AUD.estado==='tocando'){ speechSynthesis.pause(); audEstado('pausado'); return true; }
  if(AUD.estado==='pausado'){ speechSynthesis.resume(); audEstado('tocando'); return true; }
  return false;
}""",
     """function audAlterna(g){
  if(!g||AUD.dono!==g||!AUD_EL)return false;
  if(AUD.estado==='tocando'){ AUD_EL.pause(); audEstado('pausado'); return true; }
  if(AUD.estado==='pausado'){ AUD_EL.play(); audEstado('tocando'); return true; }
  return false;
}"""),

    # 6. o stop para o elemento
    ("audStop/arquivo",
     "  if(audSuportado())speechSynthesis.cancel();",
     "  audParar();"),

    # 7. say: o texto vira chave de busca no mapa
    ("say/arquivo",
     """  if(!audSuportado()){ audAviso(g); return; }
  audFala(g,function(){
    var u=new SpeechSynthesisUtterance(text);
    u.rate=rate||0.95; u.pitch=1; u.lang='en-US';
    if(!_voice)_voice=pickVoice();
    if(_voice)u.voice=_voice;
    speechSynthesis.speak(u);
  });""",
     """  audFala(g,function(){ return {src:audFonte(text),rate:audRate(rate)}; });"""),

    # 8. o elenco de vozes do sistema sai inteiro
    ("VOICE_PREF/fora",
     """var VOICE_PREF={
  f:['Microsoft Aria','Microsoft Jenny','Microsoft Michelle','Microsoft Zira','Google US English','Samantha','Victoria','Karen','Female'],
  m:['Microsoft Guy','Microsoft Christopher','Microsoft Eric','Microsoft David','Microsoft Mark','Alex','Daniel','Male']
};""",
     """/* A tabela de nomes comerciais do sistema saiu daqui: o Anexo P-A §4 diz que "os nomes
   comerciais de voz nao substituem Voice IDs". A voz de cada personagem e decidida na
   GERACAO, pelo `voices` do config, e chega pronta dentro do arquivo. */"""),
    # 9. sayAs: mesma chave (o texto); a voz ja veio decidida dentro do arquivo
    ("sayAs/arquivo",
     """  if(!audSuportado()){ audAviso(grp); return; }
  audFala(grp,function(){
  var en=enVoices(),pref=VOICE_PREF[g]||[],pick=null,p,j;
  for(p=0;p<pref.length&&!pick;p++)for(j=0;j<en.length;j++)if(en[j].name.indexOf(pref[p])>-1){pick=en[j];break;}
  var u=new SpeechSynthesisUtterance(text);
  u.lang='en-US'; u.rate=rate||0.95;
  if(pick){u.voice=pick;u.pitch=1;}
  else if(en.length){u.voice=en[0];u.pitch=(g==='m')?0.82:1.14;}
  speechSynthesis.speak(u);
  });""",
     """  /* O `g` (genero) some do runtime de proposito: ele servia para ESCOLHER voz no
     navegador, e agora a voz ja esta gravada no arquivo. Continua na assinatura para o
     HTML da aula nao mudar -- sao 4 call sites so no molde, e o valor segue documentando
     de quem e a fala. */
  audFala(grp,function(){ return {src:audFonte(text),rate:audRate(rate)}; });"""),

    # 10. playTalk: a chave e o TRECHO, e os turnos vem do manifesto
    ("playTalk/arquivo",
     """  if(!audSuportado()){ audAviso(grp); return; }
  audFala(grp,function(){
  var TK=talkDe(alvo);
  var vs=pickCast(),fb=enVoices()[0]||null,a=(from==null?0:from),b=(to==null?TK.length-1:to),i;
  var pit={f:1.14,m:0.82};
  for(i=a;i<=b;i++){
    (function(turn){
      var u=new SpeechSynthesisUtterance(turn.t);
      u.lang='en-US'; u.rate=rate||0.95;
      if(vs[turn.s]){u.voice=vs[turn.s];u.pitch=1;}
      else if(fb){u.voice=fb;u.pitch=pit[CAST[turn.s].g];}
      u.onstart=function(){if(show)markSpeaker(turn.s);};
      speechSynthesis.speak(u);
    })(TK[i]);
  }
  });""",
     """  audFala(grp,function(){
    var TK=talkDe(alvo);
    var a=(from==null?0:from),b=(to==null?TK.length-1:to);
    /* A aula sai do proprio botao, como em `talkDe`: o mesmo botao responde certo em
       qualquer aula, sem variavel global de estado. */
    var s=alvo&&alvo.closest?alvo.closest('.slide'):null;
    var n=s?s.getAttribute('data-lesson'):null;
    if(!n){ for(var k in TALKS){ n=k; break; } }
    var chave='#talk'+n+':'+a+':'+b;
    return {src:audFonte(chave),rate:audRate(rate),turnos:audTurnos(chave),show:show};
  });"""),
]

# funcoes que deixam de existir porque so serviam a sintese do navegador
FORA = ["enVoices", "pickCast", "voiceReport"]
