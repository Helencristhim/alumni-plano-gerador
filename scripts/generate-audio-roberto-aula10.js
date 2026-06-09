#!/usr/bin/env node
const fs=require('fs'),path=require('path'),https=require('https');
const API_KEY=process.env.ELEVENLABS_API_KEY,DIR=path.join(__dirname,'..','public','audio','roberto-pires');
const ASH='VU16byTywsWv5JpI8rbc',RILEY='hA4zGnmTwX2NQiTRMt7o';
if(!fs.existsSync(DIR))fs.mkdirSync(DIR,{recursive:true});
// Roberto = male → ASH for protagonist. RILEY for female characters (Marta). Alternate for general.
const E=[
// Vocab words (male student = ASH)
["Line","line.mp3",ASH],
["Platform","platform_noun.mp3",ASH],
["Transfer","transfer.mp3",ASH],
["Route","route.mp3",ASH],
["Connection","connection.mp3",ASH],
["Schedule","schedule.mp3",ASH],
["Fare","fare.mp3",ASH],
["Direction","direction.mp3",ASH],
// Context sentences (alternating)
["Take line 4 to Ch\u00e2telet.","take_line_4_to_chatelet.mp3",RILEY],
["Get off at the next stop.","get_off_at_the_next_stop.mp3",ASH],
["Transfer at Ch\u00e2telet to line 1.","transfer_at_chatelet_to_line_1.mp3",RILEY],
["Go to platform B.","go_to_platform_b.mp3",ASH],
["Check the schedule on the screen.","check_the_schedule_on_the_screen.mp3",RILEY],
["The fare is 2.15 euros for a single ride.","the_fare_is_215_euros_for_a_single_ride.mp3",ASH],
["What is the best route to Montmartre?","what_is_the_best_route_to_montmartre.mp3",ASH],
["There is a connection to the RER at Ch\u00e2telet.","there_is_a_connection_to_the_rer_at_chatelet.mp3",RILEY],
// Grammar sentences
["How do I get to the Eiffel Tower?","how_do_i_get_to_the_eiffel_tower.mp3",ASH],
["Which line goes to Montmartre?","which_line_goes_to_montmartre.mp3",ASH],
["Do I need to transfer?","do_i_need_to_transfer.mp3",ASH],
["Take line 12.","take_line_12.mp3",RILEY],
["Get off at Abbesses.","get_off_at_abbesses.mp3",RILEY],
["Change at Concorde.","change_at_concorde.mp3",RILEY],
// Dialogue (Roberto=ASH, Marta=RILEY)
["Excuse me, how do I get to Montmartre?","excuse_me_how_do_i_get_to_montmartre.mp3",ASH],
["Take line 12, in the direction of Front Populaire. Get off at Abbesses.","take_line_12_in_the_direction_of_front_populaire_get_off_at_.mp3",RILEY],
["Which platform is line 12?","which_platform_is_line_12.mp3",ASH],
["Go down the stairs. Platform B is on your left.","go_down_the_stairs_platform_b_is_on_your_left.mp3",RILEY],
["No, it is a direct line. Only 5 stops.","no_it_is_a_direct_line_only_5_stops.mp3",RILEY],
["And if I want to take the bus to the Eiffel Tower later?","and_if_i_want_to_take_the_bus_to_the_eiffel_tower_later.mp3",ASH],
["Take bus number 80 from Abbesses. The bus stop is right outside.","take_bus_number_80_from_abbesses_the_bus_stop_is_right_outsi.mp3",RILEY],
["How much is the fare?","how_much_is_the_fare.mp3",ASH],
["A single ticket is 2.15 euros. Or you can buy a carnet of 10.","a_single_ticket_is_215_euros_or_you_can_buy_a_carnet_of_10.mp3",RILEY],
["Thank you. You really helped me.","thank_you_you_really_helped_me.mp3",ASH],
["You are welcome. Enjoy Montmartre!","you_are_welcome_enjoy_montmartre.mp3",RILEY],
// Listening 1 (narrative about Roberto = ASH)
["Roberto is at Ch\u00e2telet metro station in Paris. It is his first time using the Paris metro. He looks at the map and finds line 12 to Montmartre. He walks down the stairs to platform B. A voice on the speaker says: Next train in 2 minutes, direction Front Populaire. Roberto waits. The train arrives. He gets on and counts the stops: Concorde, Madeleine, Trinit\u00e9, Lamarck, Abbesses. He gets off at Abbesses. The metro is faster and more efficient than he expected. He follows the signs to the exit and walks into the streets of Montmartre.","roberto_is_at_chatelet_metro_station_in_paris_it_is_his_firs.mp3",ASH],
// Listening 2 (narrative about Roberto = RILEY for variety)
["Roberto wants to go to the Eiffel Tower. He finds the bus stop outside Abbesses station. He checks the schedule on the screen. Bus number 80 comes every 10 minutes. He buys a single ticket from the machine. The bus arrives. Roberto gets on and asks the driver: Does this bus go to the Eiffel Tower? The driver says: Yes, get off at Trocad\u00e9ro. It takes about 25 minutes. Roberto sits down and watches Paris through the window. The route goes through beautiful neighborhoods. He sees a bakery, a park, and many caf\u00e9s. The bus is slower than the metro, but Roberto can see the city. He gets off at Trocad\u00e9ro and walks to the Eiffel Tower.","roberto_wants_to_go_to_the_eiffel_tower_he_finds_the_bus_sto.mp3",RILEY],
// Oral drilling (alternating)
["How do I get to the Louvre?","how_do_i_get_to_the_louvre.mp3",ASH],
["Which line goes to the Arc de Triomphe?","which_line_goes_to_the_arc_de_triomphe.mp3",ASH],
["Does this bus stop at Notre-Dame?","does_this_bus_stop_at_notre_dame.mp3",ASH],
["Excuse me, I missed my stop. How do I get back?","excuse_me_i_missed_my_stop_how_do_i_get_back.mp3",ASH],
["I need to buy a single ticket.","i_need_to_buy_a_single_ticket.mp3",ASH],
["The bus is slower than the metro, but I can see the city.","the_bus_is_slower_than_the_metro_but_i_can_see_the_city.mp3",RILEY],
// Grammar expressions
["How do I get to...","how_do_i_get_to.mp3",ASH],
["Which line goes to...","which_line_goes_to.mp3",ASH],
["Do I need to...","do_i_need_to.mp3",ASH],
];
function gen(t,f,v){return new Promise((r,j)=>{const fp=path.join(DIR,f);if(fs.existsSync(fp)&&fs.statSync(fp).size>1000){console.log('  SKIP:',f);return r();}const b=JSON.stringify({text:t,model_id:'eleven_turbo_v2_5',voice_settings:{stability:.5,similarity_boost:.75}});const o={hostname:'api.elevenlabs.io',path:`/v1/text-to-speech/${v}`,method:'POST',headers:{'xi-api-key':API_KEY,'Content-Type':'application/json','Accept':'audio/mpeg','Content-Length':Buffer.byteLength(b)}};const q=https.request(o,res=>{if(res.statusCode!==200){let e='';res.on('data',d=>e+=d);res.on('end',()=>{console.error('  ERR',res.statusCode,f,e.substring(0,200));j(new Error('HTTP '+res.statusCode));});return;}const c=[];res.on('data',d=>c.push(d));res.on('end',()=>{const buf=Buffer.concat(c);fs.writeFileSync(fp,buf);console.log('  OK:',f,buf.length,'bytes');r();});});q.on('error',j);q.write(b);q.end();});}
async function main(){console.log(`Generating ${E.length} audio files for Roberto Pires Aula 10...`);let ok=0,err=0;for(let i=0;i<E.length;i++){try{await gen(E[i][0],E[i][1],E[i][2]);ok++;if(i<E.length-1)await new Promise(r=>setTimeout(r,150));}catch(e){console.error('Failed:',E[i][1],e.message);err++;}}console.log(`Done: ${ok} OK, ${err} errors`);}
main().catch(console.error);
