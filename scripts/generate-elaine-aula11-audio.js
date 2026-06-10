#!/usr/bin/env node
const fs=require('fs'),path=require('path');
const API='https://api.elevenlabs.io/v1/text-to-speech';
const V={arthur:'sfJopaWaOtauCD3HKX6Q',ellen:'BIvP0GN1cAtSRTxNHnWS',josh:'TxGEqnHWrfWFTfGW9XjX',rachel:'21m00Tcm4TlvDq8ikWAM',domi:'AZnzlk1XvdvUeBnXmlld',bella:'EXAVITQu4vr4xnSDxMaL'};
const KEY=process.env.ELEVENLABS_API_KEY, OUT=path.join(__dirname,'..','public','audio','elaine-mieko-pinho');
if(!KEY){console.error('Set ELEVENLABS_API_KEY');process.exit(1);} if(!fs.existsSync(OUT))fs.mkdirSync(OUT,{recursive:true});
const phrases=[
  { text: "Bill", file: "bill.mp3", voice: "ellen" },
  { text: "Cash", file: "cash.mp3", voice: "ellen" },
  { text: "Card", file: "card.mp3", voice: "ellen" },
  { text: "Change", file: "change_word.mp3", voice: "ellen" },
  { text: "Receipt", file: "receipt.mp3", voice: "ellen" },
  { text: "Total", file: "total.mp3", voice: "ellen" },
  { text: "Split", file: "split.mp3", voice: "ellen" },
  { text: "Cents", file: "cents.mp3", voice: "ellen" },
  { text: "I am allergic to nuts.", file: "i_am_allergic_to_nuts.mp3", voice: "ellen" },
  { text: "Can you make it without dairy?", file: "can_you_make_it_without_dairy.mp3", voice: "ellen" },
  { text: "How much is it?", file: "how_much_is_it.mp3", voice: "ellen" },
  { text: "Could I have the bill, please?", file: "could_i_have_the_bill_please.mp3", voice: "ellen" },
  { text: "Can I pay by card?", file: "can_i_pay_by_card.mp3", voice: "ellen" },
  { text: "Can we split the bill?", file: "can_we_split_the_bill.mp3", voice: "ellen" },
  { text: "The dinner is over. The waiter comes to my table. I say, could I have the bill, please? He brings the bill and says the total is forty-two dollars. I ask, how much is the tip, usually? About twenty percent, he says. I want to pay, so I ask, can I pay by card? Yes, he says, we take cards and cash. I pay by card and I ask for a receipt. I leave a good tip and I say, keep the change. Thank you, he says. Have a good evening.", file: "listening11_paying_bill.mp3", voice: "ellen" },
  { text: "I am at a cafe with my friend. We finish our coffee and cake. The total is forty dollars. My friend says, can we split the bill? Good idea, I say. So we split the bill. Each person pays twenty dollars. I pay by card and my friend pays with cash. We both ask for a receipt. It is easy and fair.", file: "listening11_splitting.mp3", voice: "ellen" },
  { text: "Are you finished? Can I bring you anything else?", file: "d11_are_you_finished_anything_else.mp3", voice: "arthur" },
  { text: "No, thank you. Could I have the bill, please?", file: "d11_no_thank_you_bill.mp3", voice: "ellen" },
  { text: "Of course. Here is the bill. The total is forty-two dollars.", file: "d11_here_is_bill_total.mp3", voice: "arthur" },
  { text: "How much is the tip, usually?", file: "d11_how_much_tip.mp3", voice: "ellen" },
  { text: "About fifteen to twenty percent. It is your choice.", file: "d11_fifteen_twenty_percent.mp3", voice: "arthur" },
  { text: "Okay. Can I pay by card?", file: "d11_okay_pay_by_card.mp3", voice: "ellen" },
  { text: "Yes, of course. We take cards and cash.", file: "d11_we_take_cards_cash.mp3", voice: "arthur" },
  { text: "I will pay by card. And could I have a receipt, please?", file: "d11_pay_card_receipt.mp3", voice: "ellen" },
  { text: "Sure. Here is your card and your receipt.", file: "d11_here_card_receipt.mp3", voice: "arthur" },
  { text: "Thank you. Keep the change.", file: "d11_keep_the_change.mp3", voice: "ellen" },
  { text: "Thank you very much! Have a good evening.", file: "d11_thank_you_good_evening.mp3", voice: "arthur" },
  { text: "You too. The dinner was wonderful.", file: "d11_you_too_wonderful.mp3", voice: "ellen" },
  { text: "How much is it? Can I pay by card?", file: "drill_how_much_pay_card.mp3", voice: "ellen" },
  { text: "Can we split the bill, please?", file: "drill_split_the_bill_please.mp3", voice: "ellen" },
  { text: "Could I have a receipt? Keep the change.", file: "drill_receipt_keep_change.mp3", voice: "ellen" },
  { text: "Could I have a receipt, please?", file: "could_i_have_a_receipt_please.mp3", voice: "ellen" },
  { text: "Keep the change.", file: "keep_the_change.mp3", voice: "ellen" },
  { text: "The dinner is over. Elaine asks the waiter for the bill. The waiter brings the bill with the total. Elaine asks if she can pay by card. She pays and leaves a tip. She asks for a receipt and says keep the change.", file: "order_l11_sequence.mp3", voice: "ellen" },
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
