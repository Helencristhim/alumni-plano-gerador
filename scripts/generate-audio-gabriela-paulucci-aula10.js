#!/usr/bin/env node
/* Aula 10 — Gabriela Paulucci — "Checkpoint 2: A Day in Your World" (NEW combined-scene audio; review cards reuse aula6-9). eleven_multilingual_v2. ellen=Gabriela, rachel=Sarah, arthur=male. Never overwrites (C9). */
const fs=require('fs'),path=require('path');
const ENV='/home/dan/dev/work/better/alumni-plano-gerador/.env.local';
const KEY=process.env.ELEVENLABS_API_KEY||((fs.readFileSync(ENV,'utf8').match(/ELEVENLABS_API_KEY\s*=\s*(.+)/)||[])[1]||'').trim();
if(!KEY){console.error('No ELEVENLABS_API_KEY');process.exit(1);}
const VOICES={arthur:'sfJopaWaOtauCD3HKX6Q',ellen:'BIvP0GN1cAtSRTxNHnWS',josh:'TxGEqnHWrfWFTfGW9XjX',rachel:'21m00Tcm4TlvDq8ikWAM',domi:'AZnzlk1XvdvUeBnXmlld',bella:'EXAVITQu4vr4xnSDxMaL'};
const OUT=path.join(__dirname,'..','public','audio','gabriela-paulucci');
const phrases=[
  { text: "Hi Gabriela! What do you want to do today?", file: "aula10_dia_1.mp3", voice: "rachel" },
  { text: "I love shopping! Let's go to the mall.", file: "aula10_dia_2.mp3", voice: "ellen" },
  { text: "Great! But first, I'm hungry.", file: "aula10_dia_3.mp3", voice: "rachel" },
  { text: "Me too. Let's have lunch. I'll have a salad.", file: "aula10_dia_4.mp3", voice: "ellen" },
  { text: "Good idea. Where is the restaurant?", file: "aula10_dia_5.mp3", voice: "rachel" },
  { text: "Go straight and turn left. It's next to the store.", file: "aula10_dia_6.mp3", voice: "ellen" },
  { text: "Perfect. And after lunch, shopping!", file: "aula10_dia_7.mp3", voice: "rachel" },
  { text: "Yes! I'm looking for a new dress.", file: "aula10_dia_8.mp3", voice: "ellen" },
  { text: "How much is your budget?", file: "aula10_dia_9.mp3", voice: "rachel" },
  { text: "Not much! But I love a good price.", file: "aula10_dia_10.mp3", voice: "ellen" },
  { text: "Yesterday I had a great day. In the morning, I went to my favorite cafe. I love coffee! Then I went shopping. I was looking for a dress. I found a beautiful blue dress for a good price, so I took it. The store was easy to find: go straight and turn left, next to the bank. It was a perfect day!", file: "aula10_listening1_dayout.mp3", voice: "ellen" },
  { text: "I love cooking, but today I'll have lunch at a restaurant.", file: "aula10_listening2_p1.mp3", voice: "arthur" },
  { text: "I'm looking for shoes. How much are they?", file: "aula10_listening2_p2.mp3", voice: "ellen" },
  { text: "The store is near here. Go straight and turn right.", file: "aula10_listening2_p3.mp3", voice: "rachel" },
  { text: "I love shopping. I would like a coffee. How much is it? Go straight and turn left.", file: "aula10_order_seq.mp3", voice: "ellen" },
  { text: "Yesterday I had a great day. I love shopping. I had lunch at a restaurant and I ordered a coffee. Then I bought a dress for a good price.", file: "aula10_reflection.mp3", voice: "ellen" }
];
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
(async()=>{if(!fs.existsSync(OUT))fs.mkdirSync(OUT,{recursive:true});let g=0,s=0,e=0;
 for(const p of phrases){const fp=path.join(OUT,p.file);if(fs.existsSync(fp)){s++;process.stdout.write('.');continue;}
  try{const r=await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${VOICES[p.voice]}`,{method:'POST',headers:{'xi-api-key':KEY,'Content-Type':'application/json'},body:JSON.stringify({text:p.text,model_id:'eleven_multilingual_v2',voice_settings:{stability:0.5,similarity_boost:0.75,style:0.0,use_speaker_boost:true}})});
   if(!r.ok)throw new Error(r.status+' '+(await r.text()).slice(0,120));fs.writeFileSync(fp,Buffer.from(await r.arrayBuffer()));g++;process.stdout.write('+');await sleep(350);}catch(err){e++;console.error('\n[ERROR] '+p.file+': '+err.message);}}
 console.log(`\nDone. generated=${g} skipped=${s} errors=${e} total=${phrases.length}`);process.exit(e?2:0);})();
