#!/usr/bin/env node
const fs=require('fs'),path=require('path');
const API='https://api.elevenlabs.io/v1/text-to-speech';
const V={arthur:'sfJopaWaOtauCD3HKX6Q',ellen:'BIvP0GN1cAtSRTxNHnWS',josh:'TxGEqnHWrfWFTfGW9XjX',rachel:'21m00Tcm4TlvDq8ikWAM',domi:'AZnzlk1XvdvUeBnXmlld',bella:'EXAVITQu4vr4xnSDxMaL'};
const KEY=process.env.ELEVENLABS_API_KEY, OUT=path.join(__dirname,'..','public','audio','elaine-mieko-pinho');
if(!KEY){console.error('Set ELEVENLABS_API_KEY');process.exit(1);} if(!fs.existsSync(OUT))fs.mkdirSync(OUT,{recursive:true});
const phrases=[
  { text: "Subway", file: "subway.mp3", voice: "ellen" },
  { text: "Bus", file: "bus.mp3", voice: "ellen" },
  { text: "Ticket", file: "ticket.mp3", voice: "ellen" },
  { text: "Stop", file: "stop_word.mp3", voice: "ellen" },
  { text: "Platform", file: "platform.mp3", voice: "ellen" },
  { text: "Line", file: "line.mp3", voice: "ellen" },
  { text: "Transfer", file: "transfer.mp3", voice: "ellen" },
  { text: "Schedule", file: "schedule.mp3", voice: "ellen" },
  { text: "Where is the museum?", file: "where_is_the_museum.mp3", voice: "ellen" },
  { text: "How do I get to the station?", file: "how_do_i_get_to_the_station.mp3", voice: "ellen" },
  { text: "Which subway goes to Times Square?", file: "which_subway_goes_to_times_square.mp3", voice: "ellen" },
  { text: "How do I get to the airport?", file: "how_do_i_get_to_the_airport.mp3", voice: "ellen" },
  { text: "Where is the nearest subway?", file: "where_is_the_nearest_subway.mp3", voice: "ellen" },
  { text: "Do I need to transfer?", file: "do_i_need_to_transfer.mp3", voice: "ellen" },
  { text: "I want to go to Times Square by subway. I find the station and I ask the clerk, which subway goes to Times Square? The red line, she says. A ticket is three dollars. I buy a ticket and I go down to the platform. I do not need to transfer, because the red line is direct. It is about six stops. I watch the schedule on the screen, and soon my train arrives. The subway is fast and easy.", file: "listening14_subway.mp3", voice: "ellen" },
  { text: "Sometimes I take the bus instead of the subway. I wait at the bus stop and I ask the driver, does this bus go to the park? Yes, he says, it is four stops. I pay and I find a seat. The bus is slower than the subway, but I can see the city. When my stop comes, I press the button and I get off. Taking the bus is a nice way to travel.", file: "listening14_bus.mp3", voice: "ellen" },
  { text: "Excuse me, which subway goes to Times Square?", file: "d14_which_subway_times_square.mp3", voice: "ellen" },
  { text: "The red line goes to Times Square. The station is over there.", file: "d14_red_line_station_there.mp3", voice: "domi" },
  { text: "How much is a ticket?", file: "d14_how_much_ticket.mp3", voice: "ellen" },
  { text: "A single ticket is three dollars. Here you are.", file: "d14_single_ticket_three.mp3", voice: "domi" },
  { text: "Thank you. Where is the platform?", file: "d14_where_is_platform.mp3", voice: "ellen" },
  { text: "Go down the stairs. The platform is on your left.", file: "d14_down_stairs_platform_left.mp3", voice: "domi" },
  { text: "Do I need to transfer?", file: "d14_do_i_need_transfer.mp3", voice: "ellen" },
  { text: "No, the red line is direct. No transfer.", file: "d14_red_line_direct.mp3", voice: "domi" },
  { text: "How many stops is it?", file: "d14_how_many_stops.mp3", voice: "ellen" },
  { text: "It is about six stops. Watch the schedule on the screen.", file: "d14_six_stops_schedule.mp3", voice: "domi" },
  { text: "Great. Where is the bus stop, just in case?", file: "d14_where_bus_stop.mp3", voice: "ellen" },
  { text: "The bus stop is across the street. Have a safe trip!", file: "d14_bus_stop_across_safe_trip.mp3", voice: "domi" },
  { text: "How much is a ticket?", file: "d14_how_much_ticket.mp3", voice: "ellen" },
  { text: "Where is the platform?", file: "where_is_the_platform.mp3", voice: "ellen" },
  { text: "Which bus goes to the park?", file: "which_bus_goes_to_the_park.mp3", voice: "ellen" },
  { text: "Does this bus go to the park?", file: "does_this_bus_go_to_the_park.mp3", voice: "ellen" },
  { text: "Elaine wants to go to Times Square. She asks which subway goes there. The clerk says the red line. Elaine buys a ticket. She goes down to the platform. The train arrives and she gets on.", file: "order_l14_sequence.mp3", voice: "ellen" },
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
