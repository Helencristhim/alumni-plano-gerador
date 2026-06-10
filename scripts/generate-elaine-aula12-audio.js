#!/usr/bin/env node
const fs=require('fs'),path=require('path');
const API='https://api.elevenlabs.io/v1/text-to-speech';
const V={arthur:'sfJopaWaOtauCD3HKX6Q',ellen:'BIvP0GN1cAtSRTxNHnWS',josh:'TxGEqnHWrfWFTfGW9XjX',rachel:'21m00Tcm4TlvDq8ikWAM',domi:'AZnzlk1XvdvUeBnXmlld',bella:'EXAVITQu4vr4xnSDxMaL'};
const KEY=process.env.ELEVENLABS_API_KEY, OUT=path.join(__dirname,'..','public','audio','elaine-mieko-pinho');
if(!KEY){console.error('Set ELEVENLABS_API_KEY');process.exit(1);} if(!fs.existsSync(OUT))fs.mkdirSync(OUT,{recursive:true});
const phrases=[
  { text: "Barista", file: "barista.mp3", voice: "ellen" },
  { text: "To go", file: "to_go.mp3", voice: "ellen" },
  { text: "Refill", file: "refill.mp3", voice: "ellen" },
  { text: "Straw", file: "straw.mp3", voice: "ellen" },
  { text: "Napkin", file: "napkin.mp3", voice: "ellen" },
  { text: "Muffin", file: "muffin.mp3", voice: "ellen" },
  { text: "Decaf", file: "decaf.mp3", voice: "ellen" },
  { text: "Mug", file: "mug.mp3", voice: "ellen" },
  { text: "How much is it?", file: "how_much_is_it.mp3", voice: "ellen" },
  { text: "Can I pay by card?", file: "can_i_pay_by_card.mp3", voice: "ellen" },
  { text: "Can I get a coffee, please?", file: "can_i_get_a_coffee_please.mp3", voice: "ellen" },
  { text: "For here or to go?", file: "for_here_or_to_go.mp3", voice: "rachel" },
  { text: "I will have a muffin, too.", file: "i_will_have_a_muffin_too.mp3", voice: "ellen" },
  { text: "How is your day going?", file: "how_is_your_day_going.mp3", voice: "ellen" },
  { text: "I go into a small coffee shop in New York. The barista smiles and says, what can I get for you? I say, can I get a medium coffee, please? For here or to go? she asks. For here, please. I also order a muffin. The refill is free, she says. We talk a little about the weather. It is a nice, sunny day. I pay six dollars and I say, have a good one. It is a lovely morning.", file: "listening12_cafe_order.mp3", voice: "ellen" },
  { text: "The barista is friendly, so we make small talk. How is your day going? she asks. Pretty good, thank you, I say. It is busy today. Nice weather, isn't it? Yes, it is lovely. Small talk is easy and polite. You can talk about the weather, the day, or the coffee. Then you say, have a good one, and you smile.", file: "listening12_small_talk.mp3", voice: "ellen" },
  { text: "Hi! Welcome. What can I get for you?", file: "d12_welcome_what_can_i_get.mp3", voice: "rachel" },
  { text: "Hi! Can I get a medium coffee, please?", file: "d12_can_i_get_medium_coffee.mp3", voice: "ellen" },
  { text: "Sure. For here or to go?", file: "d12_sure_for_here_or_to_go.mp3", voice: "rachel" },
  { text: "For here, please. Is the refill free?", file: "d12_for_here_refill_free.mp3", voice: "ellen" },
  { text: "Yes, the refill is free. Anything else?", file: "d12_refill_free_anything_else.mp3", voice: "rachel" },
  { text: "I will have a muffin, too. Do you have decaf?", file: "d12_muffin_decaf.mp3", voice: "ellen" },
  { text: "Yes, we have decaf. Would you like a straw and a napkin?", file: "d12_decaf_straw_napkin.mp3", voice: "rachel" },
  { text: "Just a napkin, please. How is your day going?", file: "d12_just_napkin_how_is_day.mp3", voice: "ellen" },
  { text: "Pretty good, thank you! It is busy today. Nice weather, isn't it?", file: "d12_pretty_good_nice_weather.mp3", voice: "rachel" },
  { text: "Yes, it is lovely. How much is it?", file: "d12_lovely_how_much.mp3", voice: "ellen" },
  { text: "Six dollars. Can I get your name for the cup?", file: "d12_six_dollars_name_cup.mp3", voice: "rachel" },
  { text: "It is Elaine. Thank you. Have a good one!", file: "d12_elaine_have_a_good_one.mp3", voice: "ellen" },
  { text: "Can I get a coffee, please? For here.", file: "drill_get_coffee_for_here.mp3", voice: "ellen" },
  { text: "I will have a muffin, too. Do you have decaf?", file: "drill_muffin_decaf.mp3", voice: "ellen" },
  { text: "How is your day going? Nice weather, isn't it?", file: "drill_how_day_nice_weather.mp3", voice: "ellen" },
  { text: "Have a good one!", file: "drill_have_a_good_one.mp3", voice: "ellen" },
  { text: "Can I get a tea, please?", file: "can_i_get_a_tea_please.mp3", voice: "ellen" },
  { text: "For here, please.", file: "for_here_please.mp3", voice: "ellen" },
  { text: "Elaine goes into the coffee shop. The barista asks what she wants. Elaine asks for a coffee and a muffin. The barista asks, for here or to go? They make small talk about the weather. Elaine pays and says, have a good one.", file: "order_l12_sequence.mp3", voice: "ellen" },
  { text: "Could you repeat that, please?", file: "could_you_repeat_that_please.mp3", voice: "ellen" },
  { text: "I am not sure I understand. Could you explain?", file: "i_am_not_sure_i_understand_could_you_explain.mp3", voice: "ellen" },
  { text: "Could you speak more slowly, please?", file: "could_you_speak_more_slowly_please.mp3", voice: "ellen" },
  { text: "I am not sure how to say this in English.", file: "i_am_not_sure_how_to_say_this_in_english_v2.mp3", voice: "ellen" },
  { text: "Thank you for your patience.", file: "thank_you_for_your_patience.mp3", voice: "ellen" }
];
async function gen(t,f,v){const fp=path.join(OUT,f); if(fs.existsSync(fp))return{s:1};
  const r=await fetch(`${API}/${v}`,{method:'POST',headers:{'xi-api-key':KEY,'Content-Type':'application/json'},body:JSON.stringify({text:t,model_id:'eleven_multilingual_v2',voice_settings:{stability:0.5,similarity_boost:0.75,style:0,use_speaker_boost:true}})});
  if(!r.ok)throw new Error(r.status+' '+t.slice(0,30)); fs.writeFileSync(fp,Buffer.from(await r.arrayBuffer())); return{s:0};}
(async()=>{let g=0,s=0,e=0;for(const p of phrases){try{const r=await gen(p.text,p.file,V[p.voice]);if(r.s){s++;}else{g++;await new Promise(x=>setTimeout(x,300));}}catch(x){e++;console.error(x.message);}}console.log(`done ${g} gen, ${s} skip, ${e} err`);})();
