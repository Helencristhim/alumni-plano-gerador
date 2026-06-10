#!/usr/bin/env node
const fs=require('fs'),path=require('path'),https=require('https');
const API_KEY=process.env.ELEVENLABS_API_KEY,DIR=path.join(__dirname,'..','public','audio','natalie-viegas');
const RILEY='hA4zGnmTwX2NQiTRMt7o',ASH='VU16byTywsWv5JpI8rbc';
if(!fs.existsSync(DIR))fs.mkdirSync(DIR,{recursive:true});
const E=[
// === VOCAB (10 palavras — aluna=Riley, alternando) ===
["Proposal","aula4_proposal.mp3",RILEY],
["Scope","aula4_scope.mp3",ASH],
["Deliverable","aula4_deliverable.mp3",RILEY],
["Allocate","aula4_allocate.mp3",ASH],
["Streamline","aula4_streamline.mp3",RILEY],
["Roll out","aula4_roll_out.mp3",ASH],
["Assess","aula4_assess.mp3",RILEY],
["Sprint","aula4_sprint.mp3",ASH],
["Track","aula4_track.mp3",RILEY],
["Scalable","aula4_scalable.mp3",ASH],
// === VOCAB EXAMPLES (10 frases — voz da aluna=Riley, alternando) ===
["We submitted a proposal to the Ministry of Justice last month.","aula4_we_submitted_a_proposal.mp3",RILEY],
["The scope of this project includes cloud migration and data security.","aula4_the_scope_of_this_project.mp3",ASH],
["The first deliverable is due at the end of this sprint.","aula4_the_first_deliverable_is_due.mp3",RILEY],
["I have allocated the budget for the next quarter.","aula4_i_have_allocated_the_budget.mp3",RILEY],
["We need to streamline the procurement process to save time.","aula4_we_need_to_streamline.mp3",ASH],
["We are rolling out the new case management system this month.","aula4_we_are_rolling_out.mp3",RILEY],
["I am assessing the risks before the next sprint begins.","aula4_i_am_assessing_the_risks.mp3",RILEY],
["The team has completed three sprints so far.","aula4_the_team_has_completed_three_sprints.mp3",ASH],
["I track all the deliverables in our project dashboard.","aula4_i_track_all_the_deliverables.mp3",RILEY],
["The system needs to be scalable for other government agencies.","aula4_the_system_needs_to_be_scalable.mp3",ASH],
// === FILL-IN (6 frases — alternando) ===
["I am currently working on a new proposal for the government.","aula4_fill_i_am_currently_working.mp3",RILEY],
["We have already completed the first three sprints.","aula4_fill_we_have_already_completed.mp3",ASH],
["She is rolling out the new system this quarter.","aula4_fill_she_is_rolling_out.mp3",RILEY],
["They have allocated the budget for the next phase.","aula4_fill_they_have_allocated.mp3",ASH],
["I have streamlined the approval process to save time.","aula4_fill_i_have_streamlined.mp3",RILEY],
["The team is tracking all the deliverables in the dashboard.","aula4_fill_the_team_is_tracking.mp3",ASH],
// === SPEECH (3 frases — voz da aluna=Riley) ===
["I am currently working on a cloud migration project for the Ministry of Justice.","aula4_speech_i_am_currently_working.mp3",RILEY],
["We have completed three sprints so far and delivered the core features.","aula4_speech_we_have_completed_three_sprints.mp3",RILEY],
["The system is scalable, and two other agencies have already expressed interest.","aula4_speech_the_system_is_scalable.mp3",RILEY],
// === ORDERING ===
["We received the proposal from the Ministry of Justice. I assessed the scope and allocated the budget. The team has completed three sprints so far. We are currently rolling out the first module. Two more agencies have expressed interest in the system.","order_l4_ordering.mp3",RILEY],
// === SURVIVAL (5 frases — voz da aluna=Riley) ===
["I am currently working on a major project for the Ministry of Justice.","aula4_surv_i_am_currently_working.mp3",RILEY],
["We have completed three sprints so far.","aula4_surv_we_have_completed.mp3",RILEY],
["I have allocated the budget for next quarter.","aula4_surv_i_have_allocated.mp3",RILEY],
["The team is tracking all the deliverables.","aula4_surv_the_team_is_tracking.mp3",RILEY],
["The system has been designed to be scalable.","aula4_surv_the_system_has_been_designed.mp3",RILEY],
// === DIALOGUE (Carlos=Ash, Natalie=Riley) ===
["Good morning, Natalie. Can you give me a quick update on the Ministry of Justice project?","aula4_dlg_carlos_1.mp3",ASH],
["Of course, Carlos. We are making great progress. We have completed three sprints so far.","aula4_dlg_natalie_1.mp3",RILEY],
["That is excellent. What are you working on right now?","aula4_dlg_carlos_2.mp3",ASH],
["I am currently rolling out the first module. The team is tracking all the deliverables in our project dashboard.","aula4_dlg_natalie_2.mp3",RILEY],
["Have you allocated the budget for next quarter?","aula4_dlg_carlos_3.mp3",ASH],
["Yes, I have. I have also streamlined the approval process. It is now thirty percent faster.","aula4_dlg_natalie_3.mp3",RILEY],
["Impressive. Is the system scalable for other agencies?","aula4_dlg_carlos_4.mp3",ASH],
["Absolutely. We have designed it to be scalable from the start. Two other agencies have already expressed interest.","aula4_dlg_natalie_4.mp3",RILEY],
// === LISTENING 1: Standup meeting (Ash — male narrator) ===
["Good morning, everyone. Let us go through our current status. Natalie, you are leading the Ministry of Justice project. The team has completed the third sprint this week. We are currently working on the security module. I have assessed the risks, and we need to allocate more resources to the compliance review. The proposal was approved last month, and the scope has not changed. We are on track to deliver the first set of features by the end of June. The system is scalable, so we are already planning the rollout for the next two agencies.","aula4_listening_1_standup.mp3",ASH],
// === LISTENING 2: Project briefing (Riley — Natalie presenting) ===
["Thank you for joining this project briefing. I am Natalie Viegas, and I am leading the digital transformation project for the Ministry of Justice. We have completed three out of five sprints. The team has delivered the core database module, and we are now rolling out the case management features. I have allocated the budget for Q3, and I have streamlined the procurement process. We are currently tracking fifteen deliverables, and twelve are already complete. The remaining three are in progress. This system is designed to be scalable. We have already received proposals from two additional agencies. I am assessing their requirements this week.","aula4_listening_2_briefing.mp3",RILEY],
// === ERROR CORRECTION (alternando) ===
["I am work on a new proposal right now.","aula4_ic_error_i_am_working.mp3",ASH],
["We have complete three sprints so far.","aula4_ic_error_we_have_completed.mp3",RILEY],
["She is allocate the budget this week.","aula4_ic_error_she_is_allocating.mp3",ASH],
["They has already rolled out the system.","aula4_ic_error_they_have_already.mp3",RILEY],
];
function gen(t,f,v){return new Promise((r,j)=>{const fp=path.join(DIR,f);if(fs.existsSync(fp)&&fs.statSync(fp).size>1000){console.log('  SKIP:',f);return r();}const b=JSON.stringify({text:t,model_id:'eleven_turbo_v2_5',voice_settings:{stability:.5,similarity_boost:.75}});const o={hostname:'api.elevenlabs.io',path:`/v1/text-to-speech/${v}`,method:'POST',headers:{'xi-api-key':API_KEY,'Content-Type':'application/json','Accept':'audio/mpeg','Content-Length':Buffer.byteLength(b)}};const q=https.request(o,res=>{if(res.statusCode!==200){let e='';res.on('data',d=>e+=d);res.on('end',()=>{console.error('  ERR',res.statusCode,f,e.substring(0,200));j(new Error('HTTP '+res.statusCode));});return;}const c=[];res.on('data',d=>c.push(d));res.on('end',()=>{const buf=Buffer.concat(c);fs.writeFileSync(fp,buf);console.log('  OK:',f,buf.length,'bytes');r();});});q.on('error',j);q.write(b);q.end();});}
async function main(){console.log(`Generating ${E.length} audio files for Natalie Aula 4...`);let ok=0,err=0;for(let i=0;i<E.length;i++){try{await gen(E[i][0],E[i][1],E[i][2]);ok++;if(i<E.length-1)await new Promise(r=>setTimeout(r,150));}catch(e){err++;console.error('Failed:',E[i][1],e.message);}}console.log(`Done: ${ok} OK, ${err} errors`);}
main().catch(console.error);
