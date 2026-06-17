#!/usr/bin/env node
const fs=require('fs'),path=require('path');
const API='https://api.elevenlabs.io/v1/text-to-speech';
const V={arthur:'sfJopaWaOtauCD3HKX6Q',ellen:'BIvP0GN1cAtSRTxNHnWS',josh:'TxGEqnHWrfWFTfGW9XjX',rachel:'21m00Tcm4TlvDq8ikWAM',domi:'AZnzlk1XvdvUeBnXmlld',bella:'EXAVITQu4vr4xnSDxMaL'};
const KEY=process.env.ELEVENLABS_API_KEY, OUT=path.join(__dirname,'..','public','audio','elaine-mieko-pinho');
if(!KEY){console.error('Set ELEVENLABS_API_KEY');process.exit(1);} if(!fs.existsSync(OUT))fs.mkdirSync(OUT,{recursive:true});
const phrases=[
  { text: "Menu", file: "a16_menu.mp3", voice: "ellen" },
  { text: "Allergic", file: "a16_allergic.mp3", voice: "ellen" },
  { text: "Bill", file: "a16_bill.mp3", voice: "ellen" },
  { text: "Order", file: "a16_order.mp3", voice: "ellen" },
  { text: "Directions", file: "a16_directions.mp3", voice: "ellen" },
  { text: "Subway", file: "a16_subway.mp3", voice: "ellen" },
  { text: "Ticket", file: "a16_ticket.mp3", voice: "ellen" },
  { text: "Discount", file: "a16_discount.mp3", voice: "ellen" },
  { text: "I would like a coffee, please.", file: "a16_i_would_like_a_coffee.mp3", voice: "arthur" },
  { text: "I am allergic to nuts.", file: "a16_i_am_allergic_to_nuts.mp3", voice: "ellen" },
  { text: "Could I have the bill, please?", file: "a16_could_i_have_the_bill.mp3", voice: "ellen" },
  { text: "Where is the subway station?", file: "a16_where_is_the_subway_station.mp3", voice: "arthur" },
  { text: "Which line goes to Times Square?", file: "a16_which_line_goes_to_times_square.mp3", voice: "ellen" },
  { text: "How much is a ticket?", file: "a16_how_much_is_a_ticket.mp3", voice: "arthur" },
  { text: "Is there a discount today?", file: "a16_is_there_a_discount_today.mp3", voice: "ellen" },
  { text: "Elaine has a full day in New York. In the morning, she goes to a restaurant. She reads the menu and orders eggs and coffee. She tells the waiter, I am allergic to nuts. After breakfast, she asks for the bill and pays. Then she wants to find a museum, so she asks a man on the street, Excuse me, where is the museum? It is next to the bank, on the corner. The museum is far, so Elaine takes the subway. She asks, Which line goes to Times Square, and how much is a ticket? In the afternoon, she goes shopping. She finds a nice jacket and asks, Do you have this in blue? Is there a discount today? At the end of the day, Elaine is tired but happy. She did everything in English.", file: "a16_listening_full_day.mp3", voice: "ellen" },
  { text: "Good morning! Here is the menu. What would you like?", file: "a16_d_waiter_menu.mp3", voice: "arthur" },
  { text: "I would like eggs and a coffee, please. And I am allergic to nuts.", file: "a16_d_elaine_order.mp3", voice: "ellen" },
  { text: "No problem. No nuts. Enjoy your breakfast!", file: "a16_d_waiter_noproblem.mp3", voice: "arthur" },
  { text: "Thank you. Could I have the bill, please?", file: "a16_d_elaine_bill.mp3", voice: "ellen" },
  { text: "Excuse me, where is the museum?", file: "a16_d_elaine_where.mp3", voice: "ellen" },
  { text: "It is next to the bank, on the corner. But it is far. Take the subway.", file: "a16_d_man_directions.mp3", voice: "josh" },
  { text: "Which line goes to Times Square, and how much is a ticket?", file: "a16_d_elaine_subway.mp3", voice: "ellen" },
  { text: "The red line. A ticket is three dollars.", file: "a16_d_man_redline.mp3", voice: "josh" },
  { text: "Do you have this jacket in blue? Is there a discount today?", file: "a16_d_elaine_shop.mp3", voice: "ellen" },
  { text: "Yes, in blue. And today there is a twenty percent discount.", file: "a16_d_clerk_discount.mp3", voice: "rachel" },
  { text: "I would like eggs and coffee, please. I am allergic to nuts.", file: "a16_oral_1.mp3", voice: "ellen" },
  { text: "Could I have the bill, please? How much is it?", file: "a16_oral_2.mp3", voice: "ellen" },
  { text: "Excuse me, where is the museum? Which line goes to Times Square?", file: "a16_oral_3.mp3", voice: "ellen" },
  { text: "Do you have this in blue? Is there a discount today?", file: "a16_oral_4.mp3", voice: "ellen" },
  { text: "First, Elaine orders breakfast at a restaurant. Then she pays the bill. Next, she asks a man for directions to the museum. After that, she takes the subway. Finally, she goes shopping and asks for a discount.", file: "a16_order_steps.mp3", voice: "ellen" }
];
async function gen(t,f,v){const fp=path.join(OUT,f); if(fs.existsSync(fp))return{s:1};
  const r=await fetch(`${API}/${v}`,{method:'POST',headers:{'xi-api-key':KEY,'Content-Type':'application/json'},body:JSON.stringify({text:t,model_id:'eleven_multilingual_v2',voice_settings:{stability:0.5,similarity_boost:0.75,style:0,use_speaker_boost:true}})});
  if(!r.ok)throw new Error(r.status+' '+t.slice(0,30)); fs.writeFileSync(fp,Buffer.from(await r.arrayBuffer())); return{s:0};}
(async()=>{let g=0,s=0,e=0;for(const p of phrases){try{const r=await gen(p.text,p.file,V[p.voice]);if(r.s){s++;}else{g++;await new Promise(x=>setTimeout(x,300));}}catch(x){e++;console.error(x.message);}}console.log(`done ${g} gen, ${s} skip, ${e} err`);})();
