#!/usr/bin/env node
/* Aula 8 — Gabriela Paulucci — "Let's Go Shopping!". eleven_multilingual_v2. ellen=Gabriela, rachel=Assistant, arthur=male. Never overwrites (C9). */
const fs=require('fs'),path=require('path');
const ENV='/home/dan/dev/work/better/alumni-plano-gerador/.env.local';
const KEY=process.env.ELEVENLABS_API_KEY||((fs.readFileSync(ENV,'utf8').match(/ELEVENLABS_API_KEY\s*=\s*(.+)/)||[])[1]||'').trim();
if(!KEY){console.error('No ELEVENLABS_API_KEY');process.exit(1);}
const VOICES={arthur:'sfJopaWaOtauCD3HKX6Q',ellen:'BIvP0GN1cAtSRTxNHnWS',josh:'TxGEqnHWrfWFTfGW9XjX',rachel:'21m00Tcm4TlvDq8ikWAM',domi:'AZnzlk1XvdvUeBnXmlld',bella:'EXAVITQu4vr4xnSDxMaL'};
const OUT=path.join(__dirname,'..','public','audio','gabriela-paulucci');
const phrases=[
  { text: "Shirt", file: "aula8_shirt_word.mp3", voice: "ellen" },
  { text: "Dress", file: "aula8_dress_word.mp3", voice: "ellen" },
  { text: "Shoes", file: "aula8_shoes_word.mp3", voice: "ellen" },
  { text: "Jacket", file: "aula8_jacket_word.mp3", voice: "ellen" },
  { text: "Size", file: "aula8_size_word.mp3", voice: "ellen" },
  { text: "Price", file: "aula8_price_word.mp3", voice: "ellen" },
  { text: "Store", file: "aula8_store_word.mp3", voice: "ellen" },
  { text: "Try on", file: "aula8_try_on_word.mp3", voice: "ellen" },
  { text: "I'm looking for a shirt.", file: "aula8_shirt.mp3", voice: "ellen" },
  { text: "I love this blue dress.", file: "aula8_dress.mp3", voice: "ellen" },
  { text: "These shoes are nice.", file: "aula8_shoes.mp3", voice: "ellen" },
  { text: "How much is this jacket?", file: "aula8_jacket.mp3", voice: "ellen" },
  { text: "What size are you?", file: "aula8_size.mp3", voice: "rachel" },
  { text: "It's a good price.", file: "aula8_price.mp3", voice: "ellen" },
  { text: "The store is open today.", file: "aula8_store.mp3", voice: "ellen" },
  { text: "Can I try it on?", file: "aula8_try_on.mp3", voice: "ellen" },
  { text: "How much is it?", file: "aula8_how_much.mp3", voice: "ellen" },
  { text: "I'm looking for a dress.", file: "aula8_looking_dress.mp3", voice: "ellen" },
  { text: "I'll take it.", file: "aula8_take_it.mp3", voice: "ellen" },
  { text: "Hello! Can I help you?", file: "aula8_dia_1.mp3", voice: "rachel" },
  { text: "Yes, I'm looking for a dress.", file: "aula8_dia_2.mp3", voice: "ellen" },
  { text: "I'm a medium.", file: "aula8_dia_4.mp3", voice: "ellen" },
  { text: "This blue dress is nice.", file: "aula8_dia_5.mp3", voice: "rachel" },
  { text: "I like it! Can I try it on?", file: "aula8_dia_6.mp3", voice: "ellen" },
  { text: "Of course. The fitting room is there.", file: "aula8_dia_7.mp3", voice: "rachel" },
  { text: "It fits! How much is it?", file: "aula8_dia_8.mp3", voice: "ellen" },
  { text: "It's forty dollars.", file: "aula8_dia_9.mp3", voice: "rachel" },
  { text: "Great. I'll take it.", file: "aula8_dia_10.mp3", voice: "ellen" },
  { text: "I love shopping. Today I'm looking for a new dress. I am a medium. I try on a blue dress and it fits. How much is it? It's forty dollars. That's a good price. I'll take it!", file: "aula8_listening1_shopping.mp3", voice: "ellen" },
  { text: "I'm looking for black shoes. I'm a size forty.", file: "aula8_listening2_p1.mp3", voice: "arthur" },
  { text: "How much is this jacket? I'll take it.", file: "aula8_listening2_p2.mp3", voice: "ellen" },
  { text: "Can I try on this shirt, please?", file: "aula8_listening2_p3.mp3", voice: "rachel" },
  { text: "I'm looking for a dress. How much is it? Can I try it on? I'll take it.", file: "aula8_order_seq.mp3", voice: "ellen" },
  { text: "I love shopping. I'm looking for a blue jacket. I'm a medium. How much is it? I'll take it!", file: "aula8_reflection.mp3", voice: "ellen" }
];
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
(async()=>{if(!fs.existsSync(OUT))fs.mkdirSync(OUT,{recursive:true});let g=0,s=0,e=0;
 for(const p of phrases){const fp=path.join(OUT,p.file);if(fs.existsSync(fp)){s++;process.stdout.write('.');continue;}
  try{const r=await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${VOICES[p.voice]}`,{method:'POST',headers:{'xi-api-key':KEY,'Content-Type':'application/json'},body:JSON.stringify({text:p.text,model_id:'eleven_multilingual_v2',voice_settings:{stability:0.5,similarity_boost:0.75,style:0.0,use_speaker_boost:true}})});
   if(!r.ok)throw new Error(r.status+' '+(await r.text()).slice(0,120));fs.writeFileSync(fp,Buffer.from(await r.arrayBuffer()));g++;process.stdout.write('+');await sleep(350);}catch(err){e++;console.error('\n[ERROR] '+p.file+': '+err.message);}}
 console.log(`\nDone. generated=${g} skipped=${s} errors=${e} total=${phrases.length}`);process.exit(e?2:0);})();
