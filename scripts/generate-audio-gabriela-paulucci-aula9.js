#!/usr/bin/env node
/* Aula 9 — Gabriela Paulucci — "Where Is It? Asking for Directions". eleven_multilingual_v2. ellen=Gabriela, arthur=Local, rachel=3rd. Never overwrites (C9). */
const fs=require('fs'),path=require('path');
const ENV='/home/dan/dev/work/better/alumni-plano-gerador/.env.local';
const KEY=process.env.ELEVENLABS_API_KEY||((fs.readFileSync(ENV,'utf8').match(/ELEVENLABS_API_KEY\s*=\s*(.+)/)||[])[1]||'').trim();
if(!KEY){console.error('No ELEVENLABS_API_KEY');process.exit(1);}
const VOICES={arthur:'sfJopaWaOtauCD3HKX6Q',ellen:'BIvP0GN1cAtSRTxNHnWS',josh:'TxGEqnHWrfWFTfGW9XjX',rachel:'21m00Tcm4TlvDq8ikWAM',domi:'AZnzlk1XvdvUeBnXmlld',bella:'EXAVITQu4vr4xnSDxMaL'};
const OUT=path.join(__dirname,'..','public','audio','gabriela-paulucci');
const phrases=[
  { text: "Map", file: "aula9_map_word.mp3", voice: "ellen" },
  { text: "Street", file: "aula9_street_word.mp3", voice: "ellen" },
  { text: "Corner", file: "aula9_corner_word.mp3", voice: "ellen" },
  { text: "Left", file: "aula9_left_word.mp3", voice: "ellen" },
  { text: "Right", file: "aula9_right_word.mp3", voice: "ellen" },
  { text: "Straight", file: "aula9_straight_word.mp3", voice: "ellen" },
  { text: "Near", file: "aula9_near_word.mp3", voice: "ellen" },
  { text: "Next to", file: "aula9_nextto_word.mp3", voice: "ellen" },
  { text: "Can I see the map?", file: "aula9_map.mp3", voice: "ellen" },
  { text: "This is a long street.", file: "aula9_street.mp3", voice: "ellen" },
  { text: "The shop is on the corner.", file: "aula9_corner.mp3", voice: "ellen" },
  { text: "Turn left.", file: "aula9_left.mp3", voice: "ellen" },
  { text: "Turn right.", file: "aula9_right.mp3", voice: "ellen" },
  { text: "Go straight.", file: "aula9_straight.mp3", voice: "ellen" },
  { text: "Is it near here?", file: "aula9_near.mp3", voice: "ellen" },
  { text: "It's next to the bank.", file: "aula9_nextto.mp3", voice: "ellen" },
  { text: "Where is the bank?", file: "aula9_where_bank.mp3", voice: "ellen" },
  { text: "It's next to the pharmacy.", file: "aula9_nextto_pharmacy.mp3", voice: "ellen" },
  { text: "Excuse me, where is the bank?", file: "aula9_dia_1.mp3", voice: "ellen" },
  { text: "Go straight on this street.", file: "aula9_dia_2.mp3", voice: "arthur" },
  { text: "Straight? OK.", file: "aula9_dia_3.mp3", voice: "ellen" },
  { text: "Then turn right at the corner.", file: "aula9_dia_4.mp3", voice: "arthur" },
  { text: "Turn right at the corner.", file: "aula9_dia_5.mp3", voice: "ellen" },
  { text: "The bank is next to the pharmacy.", file: "aula9_dia_6.mp3", voice: "arthur" },
  { text: "Yes, it's very near. Two minutes.", file: "aula9_dia_8.mp3", voice: "arthur" },
  { text: "Thank you very much!", file: "aula9_dia_9.mp3", voice: "ellen" },
  { text: "You're welcome!", file: "aula9_dia_10.mp3", voice: "arthur" },
  { text: "Let me tell you how to find my house. Go straight on Main Street. Turn right at the corner. My house is next to the school. It's near the park. It's easy!", file: "aula9_listening1_directions.mp3", voice: "ellen" },
  { text: "Go straight and turn left. It's on the corner.", file: "aula9_listening2_p1.mp3", voice: "arthur" },
  { text: "The store is next to the bank.", file: "aula9_listening2_p2.mp3", voice: "ellen" },
  { text: "It's near here, only two minutes.", file: "aula9_listening2_p3.mp3", voice: "rachel" },
  { text: "Excuse me, where is the bank? Go straight. Turn right at the corner. It's next to the pharmacy.", file: "aula9_order_seq.mp3", voice: "ellen" },
  { text: "Excuse me, where is the train station? Go straight on this street. Turn left at the corner. It's next to the park.", file: "aula9_reflection.mp3", voice: "ellen" }
];
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
(async()=>{if(!fs.existsSync(OUT))fs.mkdirSync(OUT,{recursive:true});let g=0,s=0,e=0;
 for(const p of phrases){const fp=path.join(OUT,p.file);if(fs.existsSync(fp)){s++;process.stdout.write('.');continue;}
  try{const r=await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${VOICES[p.voice]}`,{method:'POST',headers:{'xi-api-key':KEY,'Content-Type':'application/json'},body:JSON.stringify({text:p.text,model_id:'eleven_multilingual_v2',voice_settings:{stability:0.5,similarity_boost:0.75,style:0.0,use_speaker_boost:true}})});
   if(!r.ok)throw new Error(r.status+' '+(await r.text()).slice(0,120));fs.writeFileSync(fp,Buffer.from(await r.arrayBuffer()));g++;process.stdout.write('+');await sleep(350);}catch(err){e++;console.error('\n[ERROR] '+p.file+': '+err.message);}}
 console.log(`\nDone. generated=${g} skipped=${s} errors=${e} total=${phrases.length}`);process.exit(e?2:0);})();
