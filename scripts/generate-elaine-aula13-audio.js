#!/usr/bin/env node
const fs=require('fs'),path=require('path');
const API='https://api.elevenlabs.io/v1/text-to-speech';
const V={arthur:'sfJopaWaOtauCD3HKX6Q',ellen:'BIvP0GN1cAtSRTxNHnWS',josh:'TxGEqnHWrfWFTfGW9XjX',rachel:'21m00Tcm4TlvDq8ikWAM',domi:'AZnzlk1XvdvUeBnXmlld',bella:'EXAVITQu4vr4xnSDxMaL'};
const KEY=process.env.ELEVENLABS_API_KEY, OUT=path.join(__dirname,'..','public','audio','elaine-mieko-pinho');
if(!KEY){console.error('Set ELEVENLABS_API_KEY');process.exit(1);} if(!fs.existsSync(OUT))fs.mkdirSync(OUT,{recursive:true});
const phrases=[
  { text: "Left", file: "left.mp3", voice: "ellen" },
  { text: "Right", file: "right.mp3", voice: "ellen" },
  { text: "Straight", file: "straight.mp3", voice: "ellen" },
  { text: "Corner", file: "corner.mp3", voice: "ellen" },
  { text: "Block", file: "block.mp3", voice: "ellen" },
  { text: "Across from", file: "across_from.mp3", voice: "ellen" },
  { text: "Next to", file: "next_to.mp3", voice: "ellen" },
  { text: "Between", file: "between.mp3", voice: "ellen" },
  { text: "Can I get a coffee, please?", file: "can_i_get_a_coffee_please.mp3", voice: "ellen" },
  { text: "How is your day going?", file: "how_is_your_day_going.mp3", voice: "ellen" },
  { text: "Where is the museum?", file: "where_is_the_museum.mp3", voice: "ellen" },
  { text: "How do I get to the station?", file: "how_do_i_get_to_the_station.mp3", voice: "ellen" },
  { text: "Go straight and turn left.", file: "go_straight_and_turn_left.mp3", voice: "ellen" },
  { text: "It is next to the bank.", file: "it_is_next_to_the_bank.mp3", voice: "ellen" },
  { text: "I want to visit the Metropolitan Museum. I stop a friendly man on the street. Excuse me, where is the museum? I ask. It is not far, he says. Go straight for two blocks, then turn left at the corner. The museum is on your right, next to a big park. It is across from the bank. How do I get there? Can I walk? Yes, you can walk, he says. It is about five minutes. I say thank you and I find the museum easily.", file: "listening13_directions.mp3", voice: "ellen" },
  { text: "Yesterday I was a little lost in the city. I could not find the train station. So I asked a woman, how do I get to the station? She said, go straight, turn right at the second corner, and the station is between a hotel and a coffee shop. I followed the directions. Go straight, turn right, and there it was. Asking for directions is easy and people like to help.", file: "listening13_lost.mp3", voice: "ellen" },
  { text: "Excuse me, where is the Metropolitan Museum?", file: "d13_excuse_me_where_museum.mp3", voice: "ellen" },
  { text: "Hi! It is not far. Go straight for two blocks.", file: "d13_not_far_two_blocks.mp3", voice: "josh" },
  { text: "Go straight for two blocks. Okay.", file: "d13_go_straight_okay.mp3", voice: "ellen" },
  { text: "Then turn left at the corner.", file: "d13_turn_left_corner.mp3", voice: "josh" },
  { text: "Turn left at the corner. And then?", file: "d13_turn_left_and_then.mp3", voice: "ellen" },
  { text: "The museum is on your right, next to a big park.", file: "d13_on_right_next_to_park.mp3", voice: "josh" },
  { text: "Is it across from the bank?", file: "d13_across_from_bank.mp3", voice: "ellen" },
  { text: "Yes, exactly. It is between the park and a coffee shop.", file: "d13_between_park_cafe.mp3", voice: "josh" },
  { text: "How do I get there? Can I walk?", file: "d13_how_get_there_walk.mp3", voice: "ellen" },
  { text: "Yes, you can walk. It is about five minutes.", file: "d13_yes_walk_five_minutes.mp3", voice: "josh" },
  { text: "Thank you so much for your help!", file: "d13_thank_you_so_much.mp3", voice: "ellen" },
  { text: "You are welcome. Have a nice day!", file: "d13_you_are_welcome_nice_day.mp3", voice: "josh" },
  { text: "Excuse me, where is the museum?", file: "drill_excuse_me_where_museum.mp3", voice: "ellen" },
  { text: "Go straight and turn left at the corner.", file: "drill_go_straight_turn_left_corner.mp3", voice: "ellen" },
  { text: "It is next to the bank, across from the park.", file: "drill_next_to_across_from.mp3", voice: "ellen" },
  { text: "Is it next to the bank?", file: "is_it_next_to_the_bank.mp3", voice: "ellen" },
  { text: "Thank you for your help!", file: "thank_you_for_your_help.mp3", voice: "ellen" },
  { text: "Turn right at the corner.", file: "turn_right_at_the_corner.mp3", voice: "ellen" },
  { text: "Elaine wants to find the museum. She asks a man, excuse me, where is the museum? He says, go straight for two blocks. Then turn left at the corner. The museum is on the right, next to the park. Elaine says thank you and walks there.", file: "order_l13_sequence.mp3", voice: "ellen" },
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
