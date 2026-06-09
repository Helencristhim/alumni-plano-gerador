#!/usr/bin/env node
const fs=require('fs'),path=require('path'),https=require('https');
const API_KEY=process.env.ELEVENLABS_API_KEY,DIR=path.join(__dirname,'..','public','audio','nilo-mesquita-patucci');
const ASH='VU16byTywsWv5JpI8rbc',RILEY='hA4zGnmTwX2NQiTRMt7o';
if(!fs.existsSync(DIR))fs.mkdirSync(DIR,{recursive:true});
const E=[
["Regulation","aula7_regulation.mp3",ASH],
["Framework","aula7_framework.mp3",RILEY],
["Violation","aula7_violation.mp3",ASH],
["Sanction","aula7_sanction.mp3",RILEY],
["Transparency","aula7_transparency.mp3",ASH],
["Accountability","aula7_accountability.mp3",RILEY],
["Procedure","aula7_procedure.mp3",ASH],
["Audit","aula7_audit.mp3",RILEY],
["All clubs must follow FIFA regulations on financial transparency.","aula7_ex_regulation.mp3",ASH],
["We need a clear framework to guide our compliance efforts.","aula7_ex_framework.mp3",RILEY],
["A violation of the transfer rules can result in severe penalties.","aula7_ex_violation.mp3",ASH],
["The club received a sanction for failing to comply with fair play rules.","aula7_ex_sanction.mp3",RILEY],
["Transparency in decision-making builds trust among stakeholders.","aula7_ex_transparency.mp3",ASH],
["Accountability means that every officer must explain their actions.","aula7_ex_accountability.mp3",RILEY],
["There is a specific procedure for reporting compliance violations.","aula7_ex_procedure.mp3",ASH],
["An independent audit revealed several irregularities in the accounts.","aula7_ex_audit.mp3",RILEY],
["Nilo, I have been studying compliance frameworks across different football associations. What does Corinthians have in place?","aula7_dia1.mp3",RILEY],
["We have a comprehensive framework that covers financial transparency, transfer regulations, and internal procedures. Every department must follow it.","aula7_dia2.mp3",ASH],
["That is impressive. How do you handle violations when they occur?","aula7_dia3.mp3",RILEY],
["We have a clear procedure for reporting violations. The compliance team must investigate every case and recommend appropriate sanctions.","aula7_dia4.mp3",ASH],
["And what about accountability? How do you ensure officers follow the rules?","aula7_dia5.mp3",RILEY],
["Every officer must submit quarterly reports. We also conduct regular audits to ensure accountability across all departments.","aula7_dia6.mp3",ASH],
["Do you think transparency is the most important element of a compliance framework?","aula7_dia7.mp3",RILEY],
["Absolutely. Transparency should be the foundation of every framework. Without it, you cannot build trust or enforce regulations effectively.","aula7_dia8.mp3",ASH],
["All clubs must comply with the new financial regulations.","aula7_fill1.mp3",ASH],
["You should review the compliance framework before the meeting.","aula7_fill2.mp3",RILEY],
["Officers must not ignore violations of the code of conduct.","aula7_fill3.mp3",ASH],
["We have to submit the audit report by Friday.","aula7_fill4.mp3",RILEY],
["The board should prioritize transparency in all decisions.","aula7_fill5.mp3",ASH],
["Every club must follow FIFA regulations on transparency.","aula7_speech1.mp3",ASH],
["We should conduct regular audits to ensure accountability.","aula7_speech2.mp3",ASH],
["Officers must not ignore compliance violations.","aula7_speech3.mp3",ASH],
["Good morning, delegates. Today I want to discuss the key elements of a compliance framework in football. Every football association must have clear regulations that govern financial transparency, transfer procedures, and governance standards. When a violation occurs, there must be a defined procedure for investigation. The compliance officer must investigate the case thoroughly and recommend appropriate sanctions. Accountability is fundamental. Every officer must submit regular reports, and independent audits should be conducted at least twice a year. Remember, transparency is not optional. It must be at the core of everything we do. Without transparency, there can be no trust between the club, the fans, and the governing bodies.","aula7_listening1.mp3",RILEY],
["Good afternoon. I am the Chief Compliance Officer at Sport Club Corinthians Paulista. Our compliance framework is built on four pillars: regulation, transparency, accountability, and procedure. First, every department must follow both internal regulations and FIFA standards. We have a clear procedure for reporting any violation, and all reports must be confidential. Second, we conduct quarterly audits to ensure accountability. Every officer must submit their reports on time. Third, we believe transparency should guide every decision. Our financial reports are published for all stakeholders to review. Finally, when a violation is confirmed, we must apply appropriate sanctions. This framework has transformed governance at Corinthians, and I am proud of the progress we have made.","aula7_listening2.mp3",ASH],
["Identify the regulation. Review the procedure. Report the violation. Conduct an audit. Apply the sanction.","aula7_order_l7.mp3",ASH],
];
function gen(t,f,v){return new Promise((r,j)=>{const fp=path.join(DIR,f);if(fs.existsSync(fp)&&fs.statSync(fp).size>1000){console.log('  SKIP:',f);return r();}const b=JSON.stringify({text:t,model_id:'eleven_turbo_v2_5',voice_settings:{stability:.5,similarity_boost:.75}});const o={hostname:'api.elevenlabs.io',path:`/v1/text-to-speech/${v}`,method:'POST',headers:{'xi-api-key':API_KEY,'Content-Type':'application/json','Accept':'audio/mpeg','Content-Length':Buffer.byteLength(b)}};const q=https.request(o,res=>{if(res.statusCode!==200){let e='';res.on('data',d=>e+=d);res.on('end',()=>{console.error('  ERR',res.statusCode,f,e.substring(0,200));j(new Error('HTTP '+res.statusCode));});return;}const c=[];res.on('data',d=>c.push(d));res.on('end',()=>{const buf=Buffer.concat(c);fs.writeFileSync(fp,buf);console.log('  OK:',f,buf.length,'bytes');r();});});q.on('error',j);q.write(b);q.end();});}
async function main(){console.log(`Generating ${E.length} audio files for Nilo Aula 7...`);let ok=0,err=0;for(let i=0;i<E.length;i++){try{await gen(E[i][0],E[i][1],E[i][2]);ok++;if(i<E.length-1)await new Promise(r=>setTimeout(r,150));}catch(e){err++;console.error('Failed:',E[i][1],e.message);}}console.log(`Done: ${ok} OK, ${err} errors`);}
main().catch(console.error);
