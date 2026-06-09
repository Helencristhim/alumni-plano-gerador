#!/usr/bin/env node
const fs=require('fs'),path=require('path'),https=require('https');
const API_KEY=process.env.ELEVENLABS_API_KEY,DIR=path.join(__dirname,'..','public','audio','nilo-mesquita-patucci');
const ASH='VU16byTywsWv5JpI8rbc',RILEY='hA4zGnmTwX2NQiTRMt7o';
if(!fs.existsSync(DIR))fs.mkdirSync(DIR,{recursive:true});
const E=[
// === VOCAB (8 palavras — alternar vozes) ===
["Impression","aula5_impression.mp3",ASH],
["Approach","aula5_approach.mp3",RILEY],
["Colleague","aula5_colleague.mp3",ASH],
["Network","aula5_network.mp3",RILEY],
["Attend","aula5_attend.mp3",ASH],
["Involve","aula5_involve.mp3",RILEY],
["Opportunity","aula5_opportunity.mp3",ASH],
["Exchange","aula5_exchange.mp3",RILEY],
// === VOCAB EXAMPLES ===
["First impressions matter when you meet new colleagues.","aula5_ex_impression.mp3",ASH],
["I decided to approach the delegate from Argentina during the break.","aula5_ex_approach.mp3",RILEY],
["She is a colleague from the governance committee.","aula5_ex_colleague.mp3",RILEY],
["Networking events are a great way to build professional relationships.","aula5_ex_network.mp3",ASH],
["I plan to attend all the workshops during the FIFA program.","aula5_ex_attend.mp3",ASH],
["The project involves delegates from twelve different countries.","aula5_ex_involve.mp3",RILEY],
["This program is a great opportunity for professional growth.","aula5_ex_opportunity.mp3",ASH],
["We exchanged contact information after the session.","aula5_ex_exchange.mp3",RILEY],
// === DIALOGUE (Sarah=Riley, Nilo=Ash) ===
["Hi there! I am Sarah Mitchell, the program coordinator. Are you enjoying the reception?","aula5_dia1.mp3",RILEY],
["Hello, Sarah! Yes, it is a wonderful event. I am Nilo Patussi from Corinthians in Brazil. What does your role involve exactly?","aula5_dia2.mp3",ASH],
["I coordinate all the workshops and networking sessions. How did you hear about this opportunity?","aula5_dia3.mp3",RILEY],
["A colleague at the Brazilian Football Confederation recommended the program. Do you attend every edition?","aula5_dia4.mp3",ASH],
["Yes, I have attended the last three editions. Where are you based?","aula5_dia5.mp3",RILEY],
["I am based in Sao Paulo. Have you ever visited Brazil?","aula5_dia6.mp3",ASH],
["Not yet, but I would love to! What approach do you plan to take during the program?","aula5_dia7.mp3",RILEY],
["I want to exchange ideas with colleagues from different countries and make a strong impression at the final presentation.","aula5_dia8.mp3",ASH],
// === FILL-IN ===
["Do you work in compliance?","aula5_fill1.mp3",RILEY],
["What does your role involve?","aula5_fill2.mp3",ASH],
["Where are you based?","aula5_fill3.mp3",RILEY],
["Have you attended this program before?","aula5_fill4.mp3",ASH],
["How did you hear about this opportunity?","aula5_fill5.mp3",RILEY],
// === SPEECH ===
["Do you work in governance?","aula5_speech1.mp3",ASH],
["What country are you from?","aula5_speech2.mp3",ASH],
["Have you met any interesting colleagues here?","aula5_speech3.mp3",ASH],
// === LISTENING 1: Delegate introducing themselves at networking (Ash) ===
["Good evening, everyone. My name is Marco Rivera. I am the Director of Integrity at the Mexican Football Federation. This is my first time attending the FIFA Leadership Program, and I must say, the opportunity to network with colleagues from around the world is incredible. I work mainly in anti-corruption and compliance. My approach has always been to learn from best practices in other countries. I am hoping to exchange ideas with anyone who is involved in governance reform. What about you? Where are you from, and what does your role involve? I find that the best impressions happen when we are genuinely curious about each other.","aula5_listening1.mp3",ASH],
// === LISTENING 2: Two delegates small talk at FIFA reception (Riley narrator) ===
["At the FIFA reception, two delegates meet for the first time. Anna, from Sweden, approaches David, from Japan. She asks where he is based and what his role involves. David explains that he works in player welfare at the Japanese Football Association. He asks Anna how long she has been in football governance. She says she has been involved for six years. They exchange business cards and agree to attend the same workshop the next morning. Anna says her first impression of the program is very positive. David agrees and mentions that networking with international colleagues is a great opportunity.","aula5_listening2.mp3",RILEY],
// === ORDERING ===
["Approach a colleague. Introduce yourself. Ask a question about their role. Exchange contact information. Follow up after the event.","aula5_order_l5.mp3",ASH],
];
function gen(t,f,v){return new Promise((r,j)=>{const fp=path.join(DIR,f);if(fs.existsSync(fp)&&fs.statSync(fp).size>1000){console.log('  SKIP:',f);return r();}const b=JSON.stringify({text:t,model_id:'eleven_turbo_v2_5',voice_settings:{stability:.5,similarity_boost:.75}});const o={hostname:'api.elevenlabs.io',path:`/v1/text-to-speech/${v}`,method:'POST',headers:{'xi-api-key':API_KEY,'Content-Type':'application/json','Accept':'audio/mpeg','Content-Length':Buffer.byteLength(b)}};const q=https.request(o,res=>{if(res.statusCode!==200){let e='';res.on('data',d=>e+=d);res.on('end',()=>{console.error('  ERR',res.statusCode,f,e.substring(0,200));j(new Error('HTTP '+res.statusCode));});return;}const c=[];res.on('data',d=>c.push(d));res.on('end',()=>{const buf=Buffer.concat(c);fs.writeFileSync(fp,buf);console.log('  OK:',f,buf.length,'bytes');r();});});q.on('error',j);q.write(b);q.end();});}
async function main(){console.log(`Generating ${E.length} audio files for Nilo Aula 5...`);let ok=0,err=0;for(let i=0;i<E.length;i++){try{await gen(E[i][0],E[i][1],E[i][2]);ok++;if(i<E.length-1)await new Promise(r=>setTimeout(r,150));}catch(e){err++;console.error('Failed:',E[i][1],e.message);}}console.log(`Done: ${ok} OK, ${err} errors`);}
main().catch(console.error);
