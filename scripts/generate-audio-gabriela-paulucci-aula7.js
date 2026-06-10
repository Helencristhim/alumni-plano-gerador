#!/usr/bin/env node
/* Aula 7 — Gabriela Paulucci — "Let's Eat! Ordering at a Restaurant"
 * ElevenLabs. Model eleven_multilingual_v2 (REGRA C1). Voices: ellen=Gabriela, arthur=Waiter/male, rachel=3rd (REGRA 35).
 * Never overwrites existing MP3 (REGRA C9). Key from ../alumni-plano-gerador/.env.local or ELEVENLABS_API_KEY. */
const fs=require('fs'),path=require('path');
const ENV='/home/dan/dev/work/better/alumni-plano-gerador/.env.local';
const KEY=process.env.ELEVENLABS_API_KEY||((fs.readFileSync(ENV,'utf8').match(/ELEVENLABS_API_KEY\s*=\s*(.+)/)||[])[1]||'').trim();
if(!KEY){console.error('No ELEVENLABS_API_KEY');process.exit(1);}
const VOICES={arthur:'sfJopaWaOtauCD3HKX6Q',ellen:'BIvP0GN1cAtSRTxNHnWS',josh:'TxGEqnHWrfWFTfGW9XjX',rachel:'21m00Tcm4TlvDq8ikWAM',domi:'AZnzlk1XvdvUeBnXmlld',bella:'EXAVITQu4vr4xnSDxMaL'};
const OUT=path.join(__dirname,'..','public','audio','gabriela-paulucci');
const phrases=[
  { text: "Menu", file: "aula7_menu_word.mp3", voice: "ellen" },
  { text: "Waiter", file: "aula7_waiter_word.mp3", voice: "ellen" },
  { text: "Drink", file: "aula7_drink_word.mp3", voice: "ellen" },
  { text: "Water", file: "aula7_water_word.mp3", voice: "ellen" },
  { text: "Coffee", file: "aula7_coffee_word.mp3", voice: "ellen" },
  { text: "Dessert", file: "aula7_dessert_word.mp3", voice: "ellen" },
  { text: "The bill", file: "aula7_the_bill_word.mp3", voice: "ellen" },
  { text: "Order", file: "aula7_order_word.mp3", voice: "ellen" },
  { text: "Can I see the menu, please?", file: "aula7_menu.mp3", voice: "ellen" },
  { text: "Excuse me, waiter!", file: "aula7_waiter.mp3", voice: "ellen" },
  { text: "I would like a drink.", file: "aula7_drink.mp3", voice: "ellen" },
  { text: "Can I have some water?", file: "aula7_water.mp3", voice: "ellen" },
  { text: "I would like a coffee, please.", file: "aula7_coffee.mp3", voice: "ellen" },
  { text: "I'll have the chocolate dessert.", file: "aula7_dessert.mp3", voice: "ellen" },
  { text: "Can I have the bill, please?", file: "aula7_bill.mp3", voice: "ellen" },
  { text: "I'm ready to order.", file: "aula7_order.mp3", voice: "ellen" },
  { text: "I'd like a salad.", file: "aula7_id_like_salad.mp3", voice: "ellen" },
  { text: "I'll have the chicken.", file: "aula7_ill_have_chicken.mp3", voice: "ellen" },
  { text: "Would you like a dessert?", file: "aula7_would_you_like_dessert.mp3", voice: "arthur" },
  { text: "Good evening! Are you ready to order?", file: "aula7_dia_1.mp3", voice: "arthur" },
  { text: "Yes. Can I see the menu, please?", file: "aula7_dia_2.mp3", voice: "ellen" },
  { text: "Of course. Here you are. Would you like a drink?", file: "aula7_dia_3.mp3", voice: "arthur" },
  { text: "Yes, I would like a coffee, please.", file: "aula7_dia_4.mp3", voice: "ellen" },
  { text: "And to eat?", file: "aula7_dia_5.mp3", voice: "arthur" },
  { text: "I'll have the chicken salad.", file: "aula7_dia_6.mp3", voice: "ellen" },
  { text: "Good choice! Would you like a dessert?", file: "aula7_dia_7.mp3", voice: "arthur" },
  { text: "Yes, can I have the chocolate cake?", file: "aula7_dia_8.mp3", voice: "ellen" },
  { text: "Sure. I'll bring it soon.", file: "aula7_dia_9.mp3", voice: "arthur" },
  { text: "Thank you. Can I have the bill, please?", file: "aula7_dia_10.mp3", voice: "ellen" },
  { text: "Good evening. I am at my favorite restaurant. First, I would like a coffee and some water. To eat, I'll have the chicken salad. For dessert, I would like the chocolate cake. At the end, I always say: can I have the bill, please?", file: "aula7_listening1_restaurant.mp3", voice: "ellen" },
  { text: "I would like a pizza and a Coke.", file: "aula7_listening2_p1.mp3", voice: "arthur" },
  { text: "Can I have a salad and some water, please?", file: "aula7_listening2_p2.mp3", voice: "ellen" },
  { text: "I'll have the soup and a coffee.", file: "aula7_listening2_p3.mp3", voice: "rachel" },
  { text: "I would like a coffee. I'll have the chicken salad. Can I have a dessert? Can I have the bill, please?", file: "aula7_order_seq.mp3", voice: "ellen" },
  { text: "My favorite restaurant is Italian. I would like a pizza and a Coke. For dessert, I'll have ice cream.", file: "aula7_reflection.mp3", voice: "ellen" }
];
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
(async()=>{
  if(!fs.existsSync(OUT))fs.mkdirSync(OUT,{recursive:true});
  let g=0,s=0,e=0;
  for(const p of phrases){
    const fp=path.join(OUT,p.file);
    if(fs.existsSync(fp)){s++;process.stdout.write('.');continue;}
    try{
      const r=await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${VOICES[p.voice]}`,{method:'POST',
        headers:{'xi-api-key':KEY,'Content-Type':'application/json'},
        body:JSON.stringify({text:p.text,model_id:'eleven_multilingual_v2',voice_settings:{stability:0.5,similarity_boost:0.75,style:0.0,use_speaker_boost:true}})});
      if(!r.ok)throw new Error(r.status+' '+(await r.text()).slice(0,120));
      fs.writeFileSync(fp,Buffer.from(await r.arrayBuffer()));g++;process.stdout.write('+');await sleep(350);
    }catch(err){e++;console.error('\n[ERROR] '+p.file+': '+err.message);}
  }
  console.log(`\nDone. generated=${g} skipped=${s} errors=${e} total=${phrases.length}`);
  process.exit(e?2:0);
})();
