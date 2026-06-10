#!/usr/bin/env node
const fs=require('fs'),path=require('path');
const API='https://api.elevenlabs.io/v1/text-to-speech';
const V={arthur:'sfJopaWaOtauCD3HKX6Q',ellen:'BIvP0GN1cAtSRTxNHnWS',josh:'TxGEqnHWrfWFTfGW9XjX',rachel:'21m00Tcm4TlvDq8ikWAM',domi:'AZnzlk1XvdvUeBnXmlld',bella:'EXAVITQu4vr4xnSDxMaL'};
const KEY=process.env.ELEVENLABS_API_KEY, OUT=path.join(__dirname,'..','public','audio','elaine-mieko-pinho');
if(!KEY){console.error('Set ELEVENLABS_API_KEY');process.exit(1);} if(!fs.existsSync(OUT))fs.mkdirSync(OUT,{recursive:true});
const phrases=[
  { text: "Size", file: "size.mp3", voice: "ellen" },
  { text: "Color", file: "color.mp3", voice: "ellen" },
  { text: "Try on", file: "try_on.mp3", voice: "ellen" },
  { text: "Fitting room", file: "fitting_room.mp3", voice: "ellen" },
  { text: "Cheap", file: "cheap.mp3", voice: "ellen" },
  { text: "Expensive", file: "expensive.mp3", voice: "ellen" },
  { text: "Discount", file: "discount.mp3", voice: "ellen" },
  { text: "Fit", file: "fit.mp3", voice: "ellen" },
  { text: "Which subway goes to Times Square?", file: "which_subway_goes_to_times_square.mp3", voice: "ellen" },
  { text: "How much is a ticket?", file: "d14_how_much_ticket.mp3", voice: "ellen" },
  { text: "Do you have this in a bigger size?", file: "do_you_have_bigger_size.mp3", voice: "ellen" },
  { text: "Can I try it on?", file: "can_i_try_it_on.mp3", voice: "ellen" },
  { text: "Is it on sale?", file: "is_it_on_sale.mp3", voice: "ellen" },
  { text: "How much is it?", file: "how_much_is_it.mp3", voice: "ellen" },
  { text: "I go into a clothing store in New York. An assistant asks if she can help me. I want a shirt, so I ask, do you have this in a bigger size? Yes, she says, we have it in medium and large. Do you have it in blue? Yes, here it is. I want to try it on, so I ask, where is the fitting room? It is at the back. The shirt fits well. How much is it? she asks. It is on sale today, only thirty dollars. I am happy with the discount, so I take it.", file: "listening15_clothes_store.mp3", voice: "ellen" },
  { text: "I love a good sale. Today the store has a big discount on shoes. The normal price is sixty dollars, but on sale they are forty dollars. That is much cheaper. I ask the assistant, do you have these in my size? She brings my size and I try them on. They fit well and they are not expensive now. A discount makes shopping more fun, and I always ask, is it on sale?", file: "listening15_sale.mp3", voice: "ellen" },
  { text: "Hi! Can I help you find anything?", file: "d15_can_i_help_you.mp3", voice: "bella" },
  { text: "Yes, please. Do you have this shirt in a bigger size?", file: "d15_shirt_bigger_size.mp3", voice: "ellen" },
  { text: "Let me check. Yes, we have it in medium and large.", file: "d15_medium_and_large.mp3", voice: "bella" },
  { text: "Do you have it in blue?", file: "d15_in_blue.mp3", voice: "ellen" },
  { text: "Yes, here is the blue one. Would you like to try it on?", file: "d15_blue_try_it_on.mp3", voice: "bella" },
  { text: "Yes. Where is the fitting room?", file: "d15_where_fitting_room.mp3", voice: "ellen" },
  { text: "The fitting room is at the back, on the right.", file: "d15_fitting_room_back_right.mp3", voice: "bella" },
  { text: "Thank you. It fits well! How much is it?", file: "d15_it_fits_how_much.mp3", voice: "ellen" },
  { text: "It is forty dollars, but today it is on sale: thirty dollars.", file: "d15_forty_on_sale_thirty.mp3", voice: "bella" },
  { text: "Great, a discount! Is there a cheaper one?", file: "d15_discount_cheaper.mp3", voice: "ellen" },
  { text: "This one is the best price. It is a good deal.", file: "d15_best_price_good_deal.mp3", voice: "bella" },
  { text: "Perfect. I will take it. Thank you!", file: "d15_i_will_take_it.mp3", voice: "ellen" },
  { text: "Do you have this in a bigger size?", file: "do_you_have_bigger_size.mp3", voice: "ellen" },
  { text: "Where is the fitting room?", file: "where_is_the_fitting_room.mp3", voice: "ellen" },
  { text: "Do you have it in blue?", file: "do_you_have_it_in_blue.mp3", voice: "ellen" },
  { text: "Is there a cheaper one?", file: "is_there_a_cheaper_one.mp3", voice: "ellen" },
  { text: "I will take it.", file: "i_will_take_it.mp3", voice: "ellen" },
  { text: "Elaine goes into a clothing store. She asks if they have the shirt in a bigger size. The assistant brings it in blue. Elaine tries it on in the fitting room. It fits well. She asks the price and buys it on sale.", file: "order_l15_sequence.mp3", voice: "ellen" },
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
