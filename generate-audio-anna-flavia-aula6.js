const fs = require('fs');
const path = require('path');
const https = require('https');
const ELEVENLABS_API_KEY = process.env.ELEVENLABS_API_KEY;
if (!ELEVENLABS_API_KEY) { console.error('ERROR: ELEVENLABS_API_KEY not set'); process.exit(1); }
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const JOSH = 'TxGEqnHWrfWFTfGW9XjX';
const RACHEL = '21m00Tcm4TlvDq8ikWAM';
const OUTPUT_DIR = path.join(__dirname, 'public', 'audio', 'anna-flavia-miranda-da-silva');

const audioMap = {
  "Email": "aula6_email.mp3","Subject": "aula6_subject.mp3","Attachment": "aula6_attachment.mp3",
  "Reply": "aula6_reply.mp3","Forward": "aula6_forward.mp3","Request": "aula6_request.mp3",
  "Confirm": "aula6_confirm.mp3","Available": "aula6_available.mp3",
  "Could you please send me the report?": "aula6_could_send.mp3",
  "Can you check the attachment?": "aula6_can_check.mp3",
  "Could I have the export numbers?": "aula6_could_have.mp3",
  "I am writing to request the sugar export report.": "aula6_writing_to.mp3",
  "Please find the attachment below.": "aula6_please_find.mp3",
  "Could you confirm the meeting time?": "aula6_confirm_meeting.mp3",
  "I am available on Monday afternoon.": "aula6_available_monday.mp3",
  "I will reply to your email today.": "aula6_will_reply.mp3",
  "Hi Mr. Tanaka, my name is Anna Flavia from Usina Cururique. I am writing to request the sugar export report for March. Could you please send it to me? I am available for a meeting on Monday if you would like to discuss. Thank you. Best regards, Anna Flavia": "aula6_dial_email_1.mp3",
  "Hi Anna Flavia, thank you for your email. Please find the report attached. Could we schedule a meeting for Monday at two? Please confirm if you are available. Best regards, Kenji Tanaka": "aula6_dial_email_2.mp3",
  "Hi Mr. Tanaka, thank you for the attachment. I can confirm that Monday at two works for me. I will forward the report to my manager. See you on Monday! Best regards, Anna Flavia": "aula6_dial_email_3.mp3",
  "Anna Flavia, could you please forward the report to Ricardo? He needs it before the deadline. Thank you. Marina": "aula6_dial_email_4.mp3",
  "Good morning. My name is Anna Flavia from Usina Cururique. I am writing to request the March export report. Could you please send it as an attachment? I would also like to confirm our meeting on Monday. I am available in the afternoon. Could you please reply with a time that works for you? Thank you. Best regards, Anna Flavia Miranda da Silva.": "aula6_listening.mp3",
  "Could you please send me the report?": "aula6_surv_send.mp3",
  "Please find the attachment below.": "aula6_surv_attachment.mp3",
  "I am writing to request information.": "aula6_surv_writing.mp3",
  "Could you confirm the meeting time?": "aula6_surv_confirm.mp3",
  "I am available on Monday afternoon.": "aula6_surv_available.mp3",
  "Could you please send me the March export report?": "aula6_speech_1.mp3",
  "Please find the attachment below. Could you confirm you received it?": "aula6_speech_2.mp3",
  "I am available on Monday. Could we schedule a meeting?": "aula6_speech_3.mp3",
  "I will forward the report to my manager.": "aula6_oral_forward.mp3",
  "Dear Mr. Tanaka. I am writing to request the report. Could you please send it? Please find the attachment. I am available on Monday. Could you confirm? Best regards.": "aula6_order.mp3"
};

// Email 1 = Anna Flavia (Ellen), Email 2 = Mr. Tanaka (Josh - distinct male), Email 3 = Anna Flavia (Ellen), Email 4 = Marina (Rachel)
const annaEmails = [audioMap["Hi Mr. Tanaka, my name is Anna Flavia from Usina Cururique. I am writing to request the sugar export report for March. Could you please send it to me? I am available for a meeting on Monday if you would like to discuss. Thank you. Best regards, Anna Flavia"],audioMap["Hi Mr. Tanaka, thank you for the attachment. I can confirm that Monday at two works for me. I will forward the report to my manager. See you on Monday! Best regards, Anna Flavia"]];
const tanakaEmail = "Hi Anna Flavia, thank you for your email. Please find the report attached. Could we schedule a meeting for Monday at two? Please confirm if you are available. Best regards, Kenji Tanaka";
const marinaEmail = "Anna Flavia, could you please forward the report to Ricardo? He needs it before the deadline. Thank you. Marina";

function countWords(t){return t.trim().split(/\s+/).length}
let alt=0;
function getVoice(text){
  if(text===tanakaEmail) return {id:JOSH,name:'Josh'};
  if(text===marinaEmail) return {id:RACHEL,name:'Rachel'};
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
  console.log('Generating '+entries.length+' Aula 6 audio files...');
  for(let i=0;i<entries.length;i++){
    const[text,file]=entries[i];const out=path.join(OUTPUT_DIR,file);
    if(fs.existsSync(out)&&fs.statSync(out).size>1000){skip++;if(countWords(text)>2&&text!==tanakaEmail&&text!==marinaEmail)alt++;continue}
    const voice=getVoice(text);
    try{await generateAudio(text,voice.id,out);gen++;console.log(`Generated ${gen+skip}/${entries.length}: ${file} (${voice.name})`)}
    catch(err){console.error(`FAILED ${file}: ${err.message}`)}
    if(i<entries.length-1) await new Promise(r=>setTimeout(r,500));
  }
  console.log(`Done! Generated: ${gen}, Skipped: ${skip}`);
}
main().catch(console.error);
