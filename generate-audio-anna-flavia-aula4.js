const fs = require('fs');
const path = require('path');
const https = require('https');
const ELEVENLABS_API_KEY = process.env.ELEVENLABS_API_KEY;
if (!ELEVENLABS_API_KEY) { console.error('ERROR: ELEVENLABS_API_KEY not set'); process.exit(1); }
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const OUTPUT_DIR = path.join(__dirname, 'public', 'audio', 'anna-flavia-miranda-da-silva');

const audioMap = {
  "Colleague": "aula4_colleague.mp3", "Manager": "aula4_manager.mp3", "Team": "aula4_team.mp3",
  "Department": "aula4_department.mp3", "Friendly": "aula4_friendly.mp3", "Organized": "aula4_organized.mp3",
  "Experienced": "aula4_experienced.mp3", "Responsible": "aula4_responsible.mp3",
  "My colleague is very friendly.": "aula4_my_colleague.mp3",
  "His name is Carlos.": "aula4_his_name.mp3",
  "Her department is finance.": "aula4_her_department.mp3",
  "Our team is small but organized.": "aula4_our_team.mp3",
  "Their manager is very experienced.": "aula4_their_manager.mp3",
  "Your office is on the third floor.": "aula4_your_office.mp3",
  "My manager is responsible for the export reports.": "aula4_my_manager.mp3",
  "Her name is Marina. She is very organized.": "aula4_her_name.mp3",
  "Tell me about your team, Anna Flavia.": "aula4_dial_carlos_1.mp3",
  "Well, my team has five people. Our manager is Ricardo.": "aula4_dial_anna_1.mp3",
  "What is Ricardo like?": "aula4_dial_carlos_2.mp3",
  "He is very experienced and organized. His office is next to mine.": "aula4_dial_anna_2.mp3",
  "And who is your closest colleague?": "aula4_dial_carlos_3.mp3",
  "Her name is Marina. She is very friendly. Her department is also finance.": "aula4_dial_anna_3.mp3",
  "It sounds like a great team! Is their office on this floor too?": "aula4_dial_carlos_4.mp3",
  "Yes! Our department is all on the third floor. Their desks are near mine.": "aula4_dial_anna_4.mp3",
  "I work at the Sao Paulo office with my team. My manager is Ricardo. He is very experienced and organized. His office is next to mine. My closest colleague is Marina. Her department is finance, like mine. She is very friendly. Our team has five people. Their desks are all on the third floor. I like my colleagues. They are responsible and helpful.": "aula4_listening.mp3",
  "My manager is Ricardo.": "aula4_surv_manager.mp3",
  "Her name is Marina.": "aula4_surv_hername.mp3",
  "Our team has five people.": "aula4_surv_ourteam.mp3",
  "His office is next to mine.": "aula4_surv_hisoffice.mp3",
  "Their desks are on the third floor.": "aula4_surv_their.mp3",
  "My manager is Ricardo. He is experienced and organized.": "aula4_speech_1.mp3",
  "Her name is Marina. She is very friendly.": "aula4_speech_2.mp3",
  "Our team has five people in the finance department.": "aula4_speech_3.mp3",
  "My manager is Ricardo. His office is next to mine. Her name is Marina. Our team has five people. Their desks are on the third floor.": "aula4_order.mp3"
};

const carlosLines = ["Tell me about your team, Anna Flavia.","What is Ricardo like?","And who is your closest colleague?","It sounds like a great team! Is their office on this floor too?"];
const annaLines = ["Well, my team has five people. Our manager is Ricardo.","He is very experienced and organized. His office is next to mine.","Her name is Marina. She is very friendly. Her department is also finance.","Yes! Our department is all on the third floor. Their desks are near mine."];

function countWords(t){return t.trim().split(/\s+/).length}
let alt=0;
function getVoice(text){
  if(carlosLines.includes(text)) return {id:ARTHUR,name:'Arthur'};
  if(annaLines.includes(text)) return {id:ELLEN,name:'Ellen'};
  if(countWords(text)<=2) return {id:ELLEN,name:'Ellen'};
  const v=alt%2===0?{id:ELLEN,name:'Ellen'}:{id:ARTHUR,name:'Arthur'};alt++;return v;
}

function generateAudio(text,voiceId,outputPath){
  return new Promise((resolve,reject)=>{
    const postData=JSON.stringify({text,model_id:'eleven_multilingual_v2',voice_settings:{stability:0.5,similarity_boost:0.75}});
    const options={hostname:'api.elevenlabs.io',path:'/v1/text-to-speech/'+voiceId+'?output_format=mp3_44100_128',method:'POST',headers:{'Content-Type':'application/json','xi-api-key':ELEVENLABS_API_KEY,'Content-Length':Buffer.byteLength(postData)}};
    const req=https.request(options,(res)=>{if(res.statusCode!==200){let b='';res.on('data',d=>b+=d);res.on('end',()=>reject(new Error('API '+res.statusCode+': '+b)));return}const chunks=[];res.on('data',c=>chunks.push(c));res.on('end',()=>{fs.writeFileSync(outputPath,Buffer.concat(chunks));resolve()})});
    req.on('error',reject);req.write(postData);req.end();
  });
}

async function main(){
  const entries=Object.entries(audioMap);let gen=0,skip=0;
  console.log('Generating '+entries.length+' Aula 4 audio files...');
  for(let i=0;i<entries.length;i++){
    const[text,file]=entries[i];const out=path.join(OUTPUT_DIR,file);
    if(fs.existsSync(out)&&fs.statSync(out).size>1000){skip++;if(countWords(text)>2&&!carlosLines.includes(text)&&!annaLines.includes(text))alt++;continue}
    const voice=getVoice(text);
    try{await generateAudio(text,voice.id,out);gen++;console.log(`Generated ${gen+skip}/${entries.length}: ${file} (${voice.name})`)}
    catch(err){console.error(`FAILED ${file}: ${err.message}`)}
    if(i<entries.length-1) await new Promise(r=>setTimeout(r,500));
  }
  console.log(`Done! Generated: ${gen}, Skipped: ${skip}`);
}
main().catch(console.error);
