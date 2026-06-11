const fs = require('fs');
const path = require('path');
const https = require('https');
const ELEVENLABS_API_KEY = process.env.ELEVENLABS_API_KEY;
if (!ELEVENLABS_API_KEY) { console.error('ERROR: ELEVENLABS_API_KEY not set'); process.exit(1); }
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const RACHEL = '21m00Tcm4TlvDq8ikWAM';
const OUTPUT_DIR = path.join(__dirname, 'public', 'audio', 'anna-flavia-miranda-da-silva');

const audioMap = {
  "My name is Anna Flavia. I am from Minas Gerais.": "aula5_intro_1.mp3",
  "I work at Usina Cururique in the financial area.": "aula5_intro_2.mp3",
  "Our company exports sugar to many countries.": "aula5_intro_3.mp3",
  "I wake up at six thirty and commute to the office by car.": "aula5_routine_1.mp3",
  "I check my schedule and emails every morning.": "aula5_routine_2.mp3",
  "I do not work on weekends.": "aula5_routine_3.mp3",
  "There is a computer and a calculator on my desk.": "aula5_workspace_1.mp3",
  "There are two meeting rooms on our floor.": "aula5_workspace_2.mp3",
  "My manager is Ricardo. He is very experienced.": "aula5_people_1.mp3",
  "Her name is Marina. She is friendly and organized.": "aula5_people_2.mp3",
  "Our team has five people in the finance department.": "aula5_people_3.mp3",
  "Good morning everyone. Thank you for being here today.": "aula5_dial_anna_1.mp3",
  "My name is Anna Flavia. I am from Minas Gerais, and I work at Usina Cururique.": "aula5_dial_anna_2.mp3",
  "I work in the financial area. Our company exports sugar to many countries.": "aula5_dial_anna_3.mp3",
  "I usually wake up at six thirty and commute to the office by car.": "aula5_dial_anna_4.mp3",
  "In the morning, I check my emails and my schedule. I have meetings with my team.": "aula5_dial_anna_5.mp3",
  "In the afternoon, I write reports and check the export numbers.": "aula5_dial_anna_6.mp3",
  "There is a computer and a calculator on my desk. There are many folders on my shelf.": "aula5_dial_anna_7.mp3",
  "My manager is Ricardo. He is experienced and organized.": "aula5_dial_anna_8.mp3",
  "My closest colleague is Marina. She is very friendly. Our team has five people.": "aula5_dial_anna_9.mp3",
  "I am happy to be at the Sao Paulo office. Thank you!": "aula5_dial_anna_10.mp3",
  "Thank you, Anna Flavia! That was a great introduction. I have a question.": "aula5_dial_partner_1.mp3",
  "What does your company export?": "aula5_dial_partner_2.mp3",
  "How many people are on your team?": "aula5_dial_partner_3.mp3",
  "Do you work on weekends?": "aula5_dial_partner_4.mp3",
  "Good morning everyone. My name is Anna Flavia. I am from Minas Gerais. I work at Usina Cururique in the financial area. Our company exports sugar to many countries. I wake up at six thirty every morning. I commute to the office by car. I check my schedule and emails first. In the afternoon, I write reports and check the export numbers. I do not work on weekends. There is a computer on my desk. There are many folders on my shelf. My manager is Ricardo. He is experienced. My colleague Marina is very friendly. Our team has five people. I am happy to be here. Thank you.": "aula5_listening.mp3",
  "My name is Anna Flavia and I work at Usina Cururique.": "aula5_surv_1.mp3",
  "I wake up at six thirty and commute by car.": "aula5_surv_2.mp3",
  "There is a computer on my desk.": "aula5_surv_3.mp3",
  "My manager is Ricardo. He is experienced.": "aula5_surv_4.mp3",
  "Our team has five people in the finance department.": "aula5_surv_5.mp3",
  "My name is Anna Flavia. I am from Minas Gerais. I work at Usina Cururique in the financial area. Our company exports sugar.": "aula5_speech_1.mp3",
  "I wake up at six thirty. I commute by car. I check my schedule every morning. I do not work on weekends.": "aula5_speech_2.mp3",
  "There is a computer on my desk. My manager is Ricardo. Her name is Marina. Our team has five people.": "aula5_speech_3.mp3",
  "My name is Anna Flavia. I work at Usina Cururique. I wake up at six thirty. There is a computer on my desk. My manager is Ricardo.": "aula5_order.mp3"
};

const partnerLines = ["Thank you, Anna Flavia! That was a great introduction. I have a question.","What does your company export?","How many people are on your team?","Do you work on weekends?"];
function countWords(t){return t.trim().split(/\s+/).length}
let alt=0;
function getVoice(text){
  if(partnerLines.includes(text)) return {id:RACHEL,name:'Rachel'};
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
  console.log('Generating '+entries.length+' Aula 5 audio files...');
  for(let i=0;i<entries.length;i++){
    const[text,file]=entries[i];const out=path.join(OUTPUT_DIR,file);
    if(fs.existsSync(out)&&fs.statSync(out).size>1000){skip++;if(countWords(text)>2&&!partnerLines.includes(text))alt++;continue}
    const voice=getVoice(text);
    try{await generateAudio(text,voice.id,out);gen++;console.log(`Generated ${gen+skip}/${entries.length}: ${file} (${voice.name})`)}
    catch(err){console.error(`FAILED ${file}: ${err.message}`)}
    if(i<entries.length-1) await new Promise(r=>setTimeout(r,500));
  }
  console.log(`Done! Generated: ${gen}, Skipped: ${skip}`);
}
main().catch(console.error);
