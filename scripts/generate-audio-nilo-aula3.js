#!/usr/bin/env node
const fs=require('fs'),path=require('path'),https=require('https');
const API_KEY=process.env.ELEVENLABS_API_KEY,DIR=path.join(__dirname,'..','public','audio','nilo-mesquita-patucci');
const ASH='VU16byTywsWv5JpI8rbc',RILEY='hA4zGnmTwX2NQiTRMt7o';
if(!fs.existsSync(DIR))fs.mkdirSync(DIR,{recursive:true});
const E=[
["Experience","aula3_experience.mp3",ASH],["Achievement","aula3_achievement.mp3",ASH],["Career","aula3_career.mp3",ASH],["Milestone","aula3_milestone.mp3",ASH],["Promotion","aula3_promotion.mp3",ASH],["Transition","aula3_transition.mp3",ASH],["Specialize","aula3_specialize.mp3",ASH],["Degree","aula3_degree.mp3",ASH],
["I have worked in law for over fifteen years.","aula3_i_have_worked_in_law_for_over_fifteen_years.mp3",ASH],
["She has achieved remarkable results in governance.","aula3_she_has_achieved_remarkable_results.mp3",RILEY],
["My career began in labor law in Rio Grande do Sul.","aula3_my_career_began_in_labor_law.mp3",ASH],
["Reaching the CCO position was a major milestone.","aula3_reaching_the_cco_position.mp3",ASH],
["I received a promotion to lead the compliance team.","aula3_i_received_a_promotion.mp3",ASH],
["The transition from private practice to corporate was challenging.","aula3_the_transition_from_private_practice.mp3",ASH],
["I decided to specialize in sports law early in my career.","aula3_i_decided_to_specialize.mp3",ASH],
["I earned my law degree from a university in southern Brazil.","aula3_i_earned_my_law_degree.mp3",ASH],
["I have worked in law for over fifteen years. My career began in labor law.","aula3_fill1.mp3",ASH],
["I have achieved several milestones in my career.","aula3_fill2.mp3",ASH],
["The transition to sports law was the best decision of my career.","aula3_fill3.mp3",ASH],
["I specialize in compliance and governance.","aula3_fill4.mp3",ASH],
["I earned my degree and then started working immediately.","aula3_fill5.mp3",ASH],
["I earned my law degree in southern Brazil. I started my career in labor law. I decided to specialize in sports law. I received a promotion to Chief Compliance Officer. I was selected for the FIFA Leadership Program.","aula3_order_l3.mp3",ASH],
["I have built my career in sports law over the past fifteen years.","aula3_speech1.mp3",ASH],
["The biggest milestone in my career was being selected for the FIFA program.","aula3_speech2.mp3",ASH],
["I specialized in labor law before making the transition to sports law.","aula3_speech3.mp3",ASH],
["Tell me about your career path, Nilo. How did you end up in football compliance?","aula3_dia1.mp3",RILEY],
["I earned my law degree in southern Brazil. I started in labor law, working with small firms.","aula3_dia2.mp3",ASH],
["When did you make the transition to sports law?","aula3_dia3.mp3",RILEY],
["About ten years ago. I decided to specialize in sports law because I saw a growing need for compliance in football.","aula3_dia4.mp3",ASH],
["That is impressive foresight. What has been your biggest achievement so far?","aula3_dia5.mp3",RILEY],
["Being selected for the FIFA program is definitely a milestone. But I am also proud of building the compliance department at Corinthians from the ground up.","aula3_dia6.mp3",ASH],
["Have you ever thought about working for FIFA directly?","aula3_dia7.mp3",RILEY],
["I have considered it. But for now, my experience at the club level gives me a unique perspective that I want to share with other organizations.","aula3_dia8.mp3",ASH],
["My name is Nilo Patussi. I earned my law degree from a university in Rio Grande do Sul, in southern Brazil. I started my career in labor law, working with small firms. After about five years, I decided to specialize in sports law. I saw that football in Brazil needed better governance and compliance. The transition from private practice to a corporate role was challenging, but it was the best decision of my career. I joined Corinthians and received a promotion to Chief Compliance Officer. Building the department from scratch has been my proudest achievement. I have worked in law for over fifteen years, and I have never stopped learning. Being selected for the FIFA Leadership Program is my latest milestone.","aula3_listening1.mp3",ASH],
["My name is Ana Lucia Ferreira. I have had quite an unusual career path. I started as a journalist, covering football in Brazil for eight years. But I always felt that the real stories were behind the scenes, in the boardrooms and governance structures. So I made a major career transition. I went back to university, earned a degree in public administration, and began working in football governance. That was eight years ago. My biggest achievement has been creating a transparency program for the Brazilian Football Confederation. I have never regretted leaving journalism. The skills I gained as a reporter, asking tough questions and finding the truth, have been invaluable in governance.","aula3_listening2.mp3",RILEY],
];
function gen(t,f,v){return new Promise((r,j)=>{const fp=path.join(DIR,f);if(fs.existsSync(fp)&&fs.statSync(fp).size>1000){console.log('  SKIP:',f);return r();}const b=JSON.stringify({text:t,model_id:'eleven_turbo_v2_5',voice_settings:{stability:.5,similarity_boost:.75}});const o={hostname:'api.elevenlabs.io',path:`/v1/text-to-speech/${v}`,method:'POST',headers:{'xi-api-key':API_KEY,'Content-Type':'application/json','Accept':'audio/mpeg','Content-Length':Buffer.byteLength(b)}};const q=https.request(o,res=>{if(res.statusCode!==200){let e='';res.on('data',d=>e+=d);res.on('end',()=>{console.error('  ERR',res.statusCode,f);j(new Error('HTTP '+res.statusCode));});return;}const c=[];res.on('data',d=>c.push(d));res.on('end',()=>{const buf=Buffer.concat(c);fs.writeFileSync(fp,buf);console.log('  OK:',f,buf.length,'bytes');r();});});q.on('error',j);q.write(b);q.end();});}
async function main(){console.log(`Generating ${E.length} audio files...`);let ok=0,err=0;for(let i=0;i<E.length;i++){try{await gen(E[i][0],E[i][1],E[i][2]);ok++;if(i<E.length-1)await new Promise(r=>setTimeout(r,150));}catch(e){err++;}}console.log(`Done: ${ok} OK, ${err} errors`);}
main().catch(console.error);
