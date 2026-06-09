#!/usr/bin/env node
const fs=require('fs'),path=require('path'),https=require('https');
const API_KEY=process.env.ELEVENLABS_API_KEY,DIR=path.join(__dirname,'..','public','audio','nilo-mesquita-patucci');
const ASH='VU16byTywsWv5JpI8rbc',RILEY='hA4zGnmTwX2NQiTRMt7o';
if(!fs.existsSync(DIR))fs.mkdirSync(DIR,{recursive:true});
const E=[
// === VOCAB (8 palavras — alternar vozes) ===
["Goal","aula4_goal.mp3",ASH],
["Strategy","aula4_strategy.mp3",RILEY],
["Objective","aula4_objective.mp3",ASH],
["Commitment","aula4_commitment.mp3",RILEY],
["Deadline","aula4_deadline.mp3",ASH],
["Priority","aula4_priority.mp3",RILEY],
["Outcome","aula4_outcome.mp3",ASH],
["Vision","aula4_vision.mp3",RILEY],
// === VOCAB EXAMPLES (8 frases — voz do aluno = Ash) ===
["My goal is to implement a new compliance framework.","aula4_my_goal_is_to_implement.mp3",ASH],
["We need a clear strategy for the next three years.","aula4_we_need_a_clear_strategy.mp3",RILEY],
["The main objective of the program is leadership development.","aula4_the_main_objective.mp3",ASH],
["This requires full commitment from every delegate.","aula4_this_requires_full_commitment.mp3",RILEY],
["The deadline for the project proposal is next Friday.","aula4_the_deadline_for_the_project.mp3",ASH],
["Governance reform is our top priority this year.","aula4_governance_reform_is_our_top.mp3",RILEY],
["The outcome of the program will benefit Brazilian football.","aula4_the_outcome_of_the_program.mp3",ASH],
["My vision is to make Corinthians a model of compliance.","aula4_my_vision_is_to_make.mp3",ASH],
// === FILL-IN (5 frases) ===
["I will present my strategy at the next session.","aula4_fill1.mp3",ASH],
["The deadline is going to be extended until March.","aula4_fill2.mp3",RILEY],
["We are going to focus on governance as our main priority.","aula4_fill3.mp3",ASH],
["I think the outcome will be very positive.","aula4_fill4.mp3",RILEY],
["I am going to set three specific objectives for my team.","aula4_fill5.mp3",ASH],
// === DIALOGUE (8 falas: Sarah=Riley, Nilo=Ash) ===
["Nilo, what are your main goals for the FIFA program?","aula4_dia1.mp3",RILEY],
["I am going to focus on learning best practices in compliance. My main objective is to bring that knowledge back to Corinthians.","aula4_dia2.mp3",ASH],
["That sounds like a strong commitment. What is your strategy?","aula4_dia3.mp3",RILEY],
["I will attend every workshop and network with delegates from other countries. I believe the outcome will be transformative.","aula4_dia4.mp3",ASH],
["What about deadlines? The cohort has several milestones to meet.","aula4_dia5.mp3",RILEY],
["Yes, I am going to submit my project proposal before the first deadline. It is my top priority right now.","aula4_dia6.mp3",ASH],
["And what is your long-term vision for compliance at Corinthians?","aula4_dia7.mp3",RILEY],
["My vision is to make Corinthians a global model for governance in football. I will work toward that goal every day.","aula4_dia8.mp3",ASH],
// === LISTENING 1: Delegate presenting goals at FIFA workshop (Ash) ===
["My name is Carlos Mendez, and I am the Head of Governance at Club America in Mexico. My main goal for the FIFA Leadership Program is to develop a comprehensive strategy for anti-corruption in Latin American football. I am going to focus on three specific objectives during the program. First, I will study best practices from European clubs. Second, I am going to build a network of compliance professionals across the continent. Third, my priority is to create a governance toolkit that any club can use. The deadline for our cohort project is December, and I am committed to delivering something impactful. I believe the outcome will help transform football governance across Latin America. My vision is that within ten years, every major club will have a dedicated compliance department.","aula4_listening1.mp3",ASH],
// === LISTENING 2: Program director on priorities and deadlines (Riley) ===
["Good morning, everyone. I am Dr. Laura Chen, the Program Director. I want to outline the key deadlines and priorities for this cohort. Your first objective is to submit a project proposal by the end of month one. We are going to review each proposal and provide feedback within two weeks. The second priority is the group workshop in month three. You will work in teams to develop a governance strategy for a real case study. The final deadline is the capstone presentation in month six. The expected outcome is a practical document that you can implement at your home organization. My vision for this program is simple: every delegate will leave with a clear strategy and the commitment to make football governance better. I will be here to support you every step of the way.","aula4_listening2.mp3",RILEY],
// === ORDERING (sequência completa) ===
["Set a clear goal. Develop a strategy. Define specific objectives. Establish a deadline. Make it your priority.","aula4_order_l4.mp3",ASH],
// === SPEECH (3 frases — voz do aluno = Ash) ===
["I am going to present my compliance strategy at the next FIFA session.","aula4_speech1.mp3",ASH],
["My main goal is to improve governance at Corinthians before the next deadline.","aula4_speech2.mp3",ASH],
["I will make compliance my top priority and work toward a positive outcome.","aula4_speech3.mp3",ASH],
];
function gen(t,f,v){return new Promise((r,j)=>{const fp=path.join(DIR,f);if(fs.existsSync(fp)&&fs.statSync(fp).size>1000){console.log('  SKIP:',f);return r();}const b=JSON.stringify({text:t,model_id:'eleven_turbo_v2_5',voice_settings:{stability:.5,similarity_boost:.75}});const o={hostname:'api.elevenlabs.io',path:`/v1/text-to-speech/${v}`,method:'POST',headers:{'xi-api-key':API_KEY,'Content-Type':'application/json','Accept':'audio/mpeg','Content-Length':Buffer.byteLength(b)}};const q=https.request(o,res=>{if(res.statusCode!==200){let e='';res.on('data',d=>e+=d);res.on('end',()=>{console.error('  ERR',res.statusCode,f,e.substring(0,200));j(new Error('HTTP '+res.statusCode));});return;}const c=[];res.on('data',d=>c.push(d));res.on('end',()=>{const buf=Buffer.concat(c);fs.writeFileSync(fp,buf);console.log('  OK:',f,buf.length,'bytes');r();});});q.on('error',j);q.write(b);q.end();});}
async function main(){console.log(`Generating ${E.length} audio files for Nilo Aula 4...`);let ok=0,err=0;for(let i=0;i<E.length;i++){try{await gen(E[i][0],E[i][1],E[i][2]);ok++;if(i<E.length-1)await new Promise(r=>setTimeout(r,150));}catch(e){err++;console.error('Failed:',E[i][1],e.message);}}console.log(`Done: ${ok} OK, ${err} errors`);}
main().catch(console.error);
